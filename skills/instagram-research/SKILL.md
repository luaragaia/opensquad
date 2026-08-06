---
name: instagram-research
description: >
  Research high-performing Instagram content (posts and reels) from reference accounts.
  Uses the Apify Instagram Scraper to pull recent content, identifies outliers (what beat the
  account's own average), analyzes the top videos, and extracts reusable hook formulas.
description_pt-BR: >
  Pesquisa conteúdo de alta performance no Instagram (posts e reels) de contas de referência.
  Usa o Apify Instagram Scraper para puxar o conteúdo recente, identifica outliers (o que
  superou a média da própria conta), analisa os top vídeos e extrai fórmulas de gancho
  reutilizáveis.
description_es: >
  Investiga contenido de alto rendimiento en Instagram (posts y reels) de cuentas de
  referencia. Usa el Apify Instagram Scraper para extraer el contenido reciente, identifica
  outliers, analiza los mejores videos y extrae fórmulas de gancho reutilizables.
type: prompt
version: "1.0.0"
categories: [research, instagram, reels, references]
---

# Instagram Research

## When to use

Right after `social-media-trends-research`: you have the topic, now see how it was treated in
the reels/posts that actually went viral. Feeds real references and hook formulas into the
analysis and script steps.

## Workflow

1. **List reference accounts** for the niche (competitors and inspirations).
2. **Scrape recent content** with the `apify` skill (Instagram Scraper Actor) — posts and
   reels with engagement metrics.
3. **Find outliers** — content that beat the account's own median (views/likes/comments),
   not just globally popular posts.
4. **Analyze the top pieces** — for reels, hand the URLs to `video-content-analyzer` to break
   down hook + structure.
5. **Extract hook formulas** — write down the repeatable opening patterns that worked.
6. **Deliver 3–5 strong references** + the hook formulas to the analysis step.

## Best practices

- Focus on outliers, not the average — that's where the signal is.
- Use `maxItems` on the Apify Actor to control cost.
- Save the references (links + why they worked) in the squad's reference folder.
- Never copy a reference — adapt it to the client's brand voice.

## Related skills

- `apify` — the scraping engine used to pull the content.
- `video-content-analyzer` — dissects the top reels found here.
- `social-media-trends-research` — runs before this to choose the topic.
