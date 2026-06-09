---
name: leonardo-ai
description: >
  Generates and enhances images via Leonardo AI API.
  Supports text-to-image and image-to-image (enhance existing photos with AI).
  Ideal for enhancing real product photos with professional lighting and composition.
  Uses Phoenix 1.0 + Alchemy for maximum realism.
description_pt-BR: >
  Gera e melhora imagens via API do Leonardo AI.
  Suporta texto-para-imagem e imagem-para-imagem (melhorar fotos reais com IA).
  Ideal para melhorar fotos reais de produto com iluminação e composição profissional.
  Usa Phoenix 1.0 + Alchemy para máximo realismo.
type: script
version: "1.0.0"
script:
  path: scripts/generate.py
  runtime: python3
  invoke: "python {skill_path}/scripts/generate.py"
env:
  - LEONARDO_API_KEY
categories: [assets, images, ai, design, food-photography]
---

# Leonardo AI — Image Generator

## When to use

Use when you need to:
- **Enhance existing Vitta Food photos** (image-to-image) — improve lighting, colors, sharpness
- **Change background** of a product photo while keeping the food intact
- **Generate lifestyle images** for posts when no real photo is available

**ALWAYS check the visual-assets catalog first.** Use real Vitta Food photos as base (via `--reference`) whenever possible — the result is far more authentic than generating from scratch.

## Modes

### Test mode (`--mode test`)
- Faster, cheaper iteration — use to check composition before the final version
- Default model: Phoenix 1.0, Alchemy OFF

### Production mode (`--mode production`)
- Final output — Phoenix 1.0 + Alchemy ON + FOOD preset
- Use only when composition is approved

**Default: test mode.** Switch to production only after approving the composition.

## Usage

### Image-to-image (recommended — enhance real Vitta Food photo)

```bash
python3 skills/leonardo-ai/scripts/generate.py \
  --prompt "Professional food photography, ultra-realistic. Same meal as reference, enhanced lighting from camera-left, sharper textures, more appetizing colors. Dark slate surface. Sony A7R IV, 85mm f/4. Alchemy quality. No text." \
  --reference "Fotos Vitta/hero/parmegina-hero.jpg" \
  --output "squads/marketing-instagram/output/assets/parmegiana-slide1.jpg" \
  --strength 0.6 \
  --mode production
```

### Text-to-image (when no real photo exists)

```bash
python3 skills/leonardo-ai/scripts/generate.py \
  --prompt "Professional food photography of a fitness meal prep container with grilled chicken, brown rice and broccoli. Dark slate surface, single softbox from camera-left. Sony A7R IV, 85mm f/2.8. Ultra-realistic, photorealistic, commercial food photography." \
  --output "squads/marketing-instagram/output/assets/slide1.jpg" \
  --mode production
```

### Change background (keep food, swap background)

```bash
python3 skills/leonardo-ai/scripts/generate.py \
  --prompt "Same food as reference image, now placed on a dark marble surface with scattered fresh herbs. Single overhead softbox, professional food photography. Keep food identical, only background changes." \
  --reference "Fotos Vitta/hero/frango-grelhado-hero.jpg" \
  --output "squads/marketing-instagram/output/assets/frango-dark-marble.jpg" \
  --strength 0.4 \
  --mode production
```

## Prompt structure (5-slot formula)

```
[Prato + textura + cor] on [superfície/fundo],
[fonte de luz + direção],
[câmera + lente + abertura],
[acabamento + qualidade],
[negative: plastic, fake, blurry, text, watermark]
```

## Prompt templates by use case

**Hero shot (carrossel cover):**
```
Professional food photography of [describe dish]. Dark slate surface with scattered fresh herbs.
Single large softbox 45 degrees from camera-left, soft shadow. Sony A7R IV, 85mm f/2.8.
Ultra-realistic, photorealistic, commercial food photography, high resolution, no text, no watermark.
```

**Lifestyle (Instagram feed):**
```
Lifestyle food photography of a fitness meal prep container with [dish]. Rustic wooden table,
fresh ingredients scattered around. Natural window light from left, golden hour warm tones.
Sony A7III, 35mm f/2.8. Shallow depth of field, bokeh, Instagram editorial style, ultra-realistic.
```

**Delivery app (clean background):**
```
Professional fitness meal prep photo. [Dish description]. Clean white background, bright even lighting,
vibrant appetizing colors, sharp focus. Top-down angle. Canon EOS R5, 50mm f/5.6. No shadows, ultra-realistic.
```

## Image strength guide (for image-to-image)

| Strength | Effect |
|----------|--------|
| 0.3–0.4 | Radical change — new background, full recomposition |
| 0.5–0.6 | Balance — preserve structure, improve quality (recommended) |
| 0.7–0.8 | Subtle — keep original structure, enhance lighting only |

## Error handling

- `LEONARDO_API_KEY not set` → add it to the `.env` file
- `API quota exceeded` → check Leonardo AI account credits
- `Generation failed` → check prompt for banned content or try a different model
