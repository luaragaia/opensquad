#!/usr/bin/env python3
"""
Leonardo AI image generator for Opensquad.
Supports text-to-image and image-to-image (enhance existing photos).
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.parse
import urllib.error

# Fix Unicode output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

API_BASE = "https://cloud.leonardo.ai/api/rest/v1"

# Model IDs — Phoenix 1.0 is best for food photography + image-to-image
MODEL_PHOENIX = "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3"
MODEL_LUCID   = "aa77f04e-3eec-4034-9c07-d0f619684628"  # Lucid Realism (text-to-image)

def get_api_key():
    key = os.environ.get("LEONARDO_API_KEY", "").strip()
    if not key:
        # try loading from .env file in cwd or parent dirs
        for d in [os.getcwd(), os.path.dirname(os.getcwd())]:
            env_path = os.path.join(d, ".env")
            if os.path.exists(env_path):
                with open(env_path) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("LEONARDO_API_KEY="):
                            key = line.split("=", 1)[1].strip().strip('"').strip("'")
                            break
            if key:
                break
    if not key:
        print("ERROR: LEONARDO_API_KEY not set. Add it to your .env file.", file=sys.stderr)
        sys.exit(1)
    return key


def api_request(method, path, data=None, headers=None, api_key=None):
    url = f"{API_BASE}{path}"
    h = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if headers:
        h.update(headers)

    body = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, headers=h, method=method)

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        print(f"ERROR {e.code} from Leonardo API ({path}):\n{err_body}", file=sys.stderr)
        sys.exit(1)


def upload_init_image(image_path, api_key):
    """Upload a local image as an init image and return its ID."""
    ext = os.path.splitext(image_path)[1].lower().lstrip(".")
    mime_map = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "webp": "image/webp"}
    mime = mime_map.get(ext, "image/jpeg")

    # Step 1: get pre-signed upload URL
    resp = api_request("POST", "/init-image", {"extension": ext}, api_key=api_key)
    upload_info = resp.get("uploadInitImage", {})
    image_id = upload_info.get("id")
    upload_url = upload_info.get("url")
    fields = upload_info.get("fields", {})
    # fields may be a JSON-encoded string in some API versions
    if isinstance(fields, str):
        try:
            fields = json.loads(fields)
        except (json.JSONDecodeError, TypeError):
            fields = {}

    if not image_id or not upload_url:
        print("ERROR: Could not get upload URL from Leonardo API.", file=sys.stderr)
        sys.exit(1)

    # Step 2: multipart upload to S3
    with open(image_path, "rb") as f:
        file_data = f.read()

    boundary = "----LeonardoBoundary"
    parts = []
    for k, v in fields.items():
        parts.append(
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}"
        )
    parts.append(
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{os.path.basename(image_path)}\"\r\nContent-Type: {mime}\r\n"
    )
    body = "\r\n".join(parts).encode("utf-8") + b"\r\n" + file_data + f"\r\n--{boundary}--\r\n".encode("utf-8")

    upload_req = urllib.request.Request(
        upload_url,
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(upload_req, timeout=60):
            pass
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8")
        print(f"ERROR uploading to S3 ({e.code}):\n{err_body}", file=sys.stderr)
        sys.exit(1)

    print(f"  ✓ Reference image uploaded (id: {image_id})")
    return image_id


def create_generation(prompt, mode, model_id, init_image_id=None, strength=0.6, width=1024, height=1024, api_key=None):
    """Create a generation and return the generation ID."""
    alchemy = (mode == "production")
    preset = "FOOD" if mode == "production" else None

    payload = {
        "modelId": model_id,
        "prompt": prompt,
        "width": width,
        "height": height,
        "num_images": 1,
        "guidance_scale": 7,
        "alchemy": alchemy,
    }
    if preset:
        payload["presetStyle"] = preset
    if init_image_id:
        payload["init_image_id"] = init_image_id
        payload["init_strength"] = round(1.0 - strength, 2)  # Leonardo uses inverted strength

    resp = api_request("POST", "/generations", payload, api_key=api_key)
    gen_id = resp.get("sdGenerationJob", {}).get("generationId")
    if not gen_id:
        print(f"ERROR: No generation ID in response: {resp}", file=sys.stderr)
        sys.exit(1)
    return gen_id


def poll_generation(gen_id, api_key, timeout=300):
    """Poll until complete, return list of image URLs."""
    print("  ⏳ Generating", end="", flush=True)
    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(5)
        print(".", end="", flush=True)
        resp = api_request("GET", f"/generations/{gen_id}", api_key=api_key)
        gen = resp.get("generations_by_pk", {})
        status = gen.get("status")
        if status == "COMPLETE":
            print(" done")
            images = gen.get("generated_images", [])
            return [img["url"] for img in images]
        elif status in ("FAILED", "DELETED"):
            print(f"\nERROR: Generation {status}.", file=sys.stderr)
            sys.exit(1)
    print("\nERROR: Generation timed out.", file=sys.stderr)
    sys.exit(1)


def download_image(url, output_path):
    """Download image from URL and save to output_path."""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "opensquad/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        with open(output_path, "wb") as f:
            f.write(resp.read())


def main():
    parser = argparse.ArgumentParser(description="Leonardo AI image generator for Opensquad")
    parser.add_argument("--prompt",    required=True,  help="Image prompt")
    parser.add_argument("--output",    required=True,  help="Output file path (.jpg or .png)")
    parser.add_argument("--reference", default=None,   help="Reference image for image-to-image (local path)")
    parser.add_argument("--strength",  type=float, default=0.6, help="Image-to-image strength (0.3–0.8). Higher = more faithful to reference.")
    parser.add_argument("--mode",      default="test", choices=["test", "production"], help="test (faster/cheaper) or production (Alchemy ON)")
    parser.add_argument("--width",     type=int, default=1024, help="Image width in pixels")
    parser.add_argument("--height",    type=int, default=1024, help="Image height in pixels")
    parser.add_argument("--model",     default=None, help="Override model ID (optional)")
    args = parser.parse_args()

    api_key = get_api_key()

    # Choose model
    if args.model:
        model_id = args.model
    elif args.reference:
        model_id = MODEL_PHOENIX   # best for image-to-image
    else:
        model_id = MODEL_LUCID if args.mode == "production" else MODEL_PHOENIX

    mode_label = "🎨 production (Alchemy ON)" if args.mode == "production" else "🧪 test"
    ref_label  = f"+ reference: {args.reference}" if args.reference else "text-to-image"
    print(f"\n🖼️  Leonardo AI — {mode_label} | {ref_label}")
    print(f"   Prompt: {args.prompt[:80]}{'...' if len(args.prompt) > 80 else ''}")
    print(f"   Output: {args.output}")

    # Upload reference image if provided
    init_image_id = None
    if args.reference:
        if not os.path.exists(args.reference):
            print(f"ERROR: Reference image not found: {args.reference}", file=sys.stderr)
            sys.exit(1)
        print(f"  📤 Uploading reference image...")
        init_image_id = upload_init_image(args.reference, api_key)

    # Create generation
    gen_id = create_generation(
        prompt=args.prompt,
        mode=args.mode,
        model_id=model_id,
        init_image_id=init_image_id,
        strength=args.strength,
        width=args.width,
        height=args.height,
        api_key=api_key,
    )
    print(f"  🚀 Generation started (id: {gen_id})")

    # Poll for completion
    image_urls = poll_generation(gen_id, api_key)

    if not image_urls:
        print("ERROR: No images returned.", file=sys.stderr)
        sys.exit(1)

    # Save the first image
    download_image(image_urls[0], args.output)
    print(f"  ✅ Saved to: {args.output}\n")


if __name__ == "__main__":
    main()
