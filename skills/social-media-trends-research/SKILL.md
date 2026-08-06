---
name: social-media-trends-research
description: >
  Programmatic trend research for a niche. Finds trending topics and rising queries using
  free sources (Google Trends via pytrends, Reddit via yars, and web/social search), and
  measures keyword velocity and volume so content decisions are grounded in real demand.
description_pt-BR: >
  Pesquisa programática de tendências para um nicho. Encontra temas em alta e buscas em
  ascensão usando fontes gratuitas (Google Trends via pytrends, Reddit via yars e busca
  web/social), e mede volume e velocidade das palavras-chave para decidir o conteúdo com
  base em demanda real.
description_es: >
  Investigación programática de tendencias para un nicho. Encuentra temas en tendencia y
  búsquedas en ascenso usando fuentes gratuitas (Google Trends vía pytrends, Reddit vía
  yars y búsqueda web/social), y mide volumen y velocidad de las palabras clave.
type: prompt
version: "1.0.0"
categories: [research, trends, social-media]
---

# Social Media Trends Research

## When to use

Use this at the **start** of content production, to pick the topic/angle from what is actually
rising — not from guesswork. Pairs with `instagram-research` (see how the topic shows up in
posts/reels that already performed).

## Workflow

1. **Define the niche + seed keywords** for the active client.
2. **Google Trends (pytrends)** — pull interest-over-time and rising related queries; note
   which terms are accelerating (velocity), not just high volume.
3. **Reddit (yars)** — scan the relevant subreddits for recurring questions and pain points.
4. **Web/social search** — confirm the trend is live and find concrete examples.
5. **Cross-check with brand fit** — drop anything off-brand for the client.
6. **Deliver 2–3 topic angles** to the strategy step, each with a one-line rationale.

## Best practices

- Prefer rising queries over already-saturated ones.
- Keep the niche tight — broad terms return noise.
- Respect rate limits on free sources; cache results per run.
- Always tie a trend back to the client's brand voice before recommending it.
