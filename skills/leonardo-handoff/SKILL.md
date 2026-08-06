---
name: leonardo-handoff
description: >
  Human-in-the-loop image workflow for Leonardo AI. When a squad needs to generate or
  manipulate an image, this skill prepares a complete, copy-paste-ready Leonardo brief
  (optimized prompt, negative prompt, recommended model, aspect ratio, and step-by-step),
  then pauses at a checkpoint for the user to run it manually in the Leonardo web app using
  their own credits and drop the resulting image back into the squad output. No API key.
description_pt-BR: >
  Fluxo de imagem com humano no loop para o Leonardo AI. Quando um squad precisa gerar ou
  manipular uma imagem, esta skill monta um brief completo e pronto pra copiar (prompt
  otimizado, negative prompt, modelo recomendado, proporção e passo a passo) e então pausa
  num checkpoint para o usuário gerar manualmente no app do Leonardo, com os próprios
  créditos, e devolver a imagem para a pasta de output do squad. Sem chave de API.
type: prompt
version: "1.0.0"
categories: [assets, images, design, human-in-the-loop]
---

# Leonardo Handoff

The user generates images in **Leonardo AI manually** (their account, their web credits).
The agent never calls an API and never fabricates an image. Instead, the agent's job is to
produce a **complete, ready-to-run Leonardo brief** and then **pause** until the user
delivers the real image file.

Pair this with the **`nano-banana-prompt`** skill to craft the prompt itself.

## When to use

Whenever a squad needs an image **created** or an existing image **manipulated/edited**
(restyle a photo, change a background, turn a photo into an illustration, product mockups,
social visuals, etc.) and the chosen tool is Leonardo AI.

## Workflow

1. **Craft the prompt** — use the `nano-banana-prompt` skill (or its principles: specific
   subject, style, lighting, camera/lens, mood). Then adapt for Leonardo (see tips below).
2. **Emit a Handoff Card** — the copy-paste block below, fully filled in.
3. **Checkpoint / pause** — tell the user the exact file path + filename to save the result
   as, then STOP and wait. Do not continue the pipeline until the file exists.
4. **Resume** — once the user confirms and the image file is in place, verify it exists and
   continue using it.

## Prompt style that works (client-tested)

Keep the prompt **simple and scene-first**: describe the **scene, the expression, the composition,
and the feeling** — not a wall of technical jargon.

- **Conceptual over literal.** Represent the idea (e.g. "many offers arriving at once") instead of
  the obvious thing (bank logos). Metaphors read better than clichés.
- **Never put text in the image.** Text lives in the Canva layout, not the generated art.
- **Avoid clichés**: corporate handshake, generic car-key handover, empty wallet, person looking
  desperate at a phone. Aim for the real, understated feeling ("poxa, não consegui"), not drama.
- **"Real people" wardrobe/setting**: casual-elegant, a small nice office — not a call center, not a
  corporate suit. Reinforces the brand voice.
- **Never invent a person to stand in for a customer/testimonial.** If real social proof exists
  (an authorized photo, a real Google review/testimonial), use the real thing.
- Warm light, premium composition; close-ups on hands/objects when the emotion calls for it.

When a client has a direction doc (e.g. `Mellos/03-Producao/DIRECAO-DE-IMAGEM.md`), follow it
scene by scene.

## Prompt tips for Leonardo (vs. Nano Banana)

- Leonardo's models are SDXL/Phoenix-based. They respond well to **descriptive, keyword-rich
  prompts** plus a **negative prompt** — more so than the conversational style Gemini/Nano
  Banana likes. Keep the strong prompt from `nano-banana-prompt`, but always add a negative
  prompt and pick a style preset.
- **Avoid text in images** — these models render text poorly. Add words to avoid to the
  negative prompt.
- Be explicit about composition, lighting, lens, and mood.

## Recommended settings

**Model** (pick per goal):

| Model in Leonardo    | Best for                                   |
| -------------------- | ------------------------------------------ |
| Leonardo Phoenix     | Flagship, best general quality (default)   |
| Leonardo Vision XL   | Photorealism / real-looking photos         |
| Leonardo Kino XL     | Cinematic, film-still look                  |
| Leonardo Diffusion XL| General purpose / illustration             |
| Lightning XL         | Fast, cheap drafts                          |

**Aspect ratio** (Leonardo presets): `1:1`, `2:3`, `3:2`, `16:9`, `4:3`, `4:5`, `9:16`.
Pick to match the destination (e.g. `4:5` or `9:16` for Instagram, `16:9` for a banner).

**Style preset** (optional): None, Cinematic, Creative, Dynamic, Fashion, Portrait, etc.

## Handoff Card — emit this to the user, fully filled in

```
🎨 LEONARDO — gerar imagem manualmente
Objetivo: <o que a imagem é / onde vai ser usada>

1. Abra https://app.leonardo.ai/  → Image Generation
2. Modelo: <ex: Leonardo Phoenix>
3. Proporção: <ex: 4:5>   |  Nº de imagens: <ex: 2>   |  Preset: <ex: Cinematic>
4. Prompt (copie e cole):
<prompt completo, otimizado>

5. Negative prompt (copie e cole):
<negative prompt>

6. Clique em Generate. Escolha a melhor imagem e baixe.
7. Salve o arquivo EXATAMENTE como:
   squads/<squad>/output/<run_id>/assets/<nome>.png
8. Me avise "pronto" que eu continuo.
```

### For image manipulation (image → image)

Add these steps to the card instead of a pure text prompt:

```
Esta é uma EDIÇÃO de imagem existente:
1. Em Image Generation, ative "Image to Image" (ou use o Canvas Editor).
2. Faça upload da imagem base: <caminho do arquivo de origem que você já tem>
3. Init Strength / Image Strength: <0.3–0.6> (menor = muda mais; maior = preserva o original)
4. Prompt: <o que mudar>
5. Negative prompt: <o que evitar>
6. Generate, baixe a melhor, e salve em:
   squads/<squad>/output/<run_id>/assets/<nome>.png
```

## Checkpoint rules (important)

- After emitting the card, **stop and wait**. Never invent or placeholder the image.
- Always give the user the **exact save path and filename** so the file lands where the
  pipeline expects it. Prefer `.png`.
- When the user says it's ready, **verify the file exists** at that path before continuing.
  If it's missing, ask again — do not proceed without it.
- If the squad needs several images, batch the cards (numbered) so the user can generate
  them in one Leonardo session, and give each a distinct filename.
- Reminder to include for the user when relevant: Leonardo generation uses their **web
  credits**, and `--num-images`/higher settings cost more.
