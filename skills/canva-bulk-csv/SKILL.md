---
name: canva-bulk-csv
description: >
  Turn a squad's post calendar + copy into a ready-to-use CSV for Canva's native "Bulk Create"
  feature (Canva Pro), plus a step-by-step runbook. The team fills a CSV (one row per post,
  one column per text slot); the user uploads it into Canva's Bulk Create app, connects columns
  to the text elements of their existing template once, and generates all designs at once.
  No Canva Enterprise, no Autofill API, no connector, and no special "data field" templates needed.
description_pt-BR: >
  Transforma o calendário de posts + copy de um squad num CSV pronto para o recurso nativo
  "Bulk Create" do Canva (plano Pro), com passo a passo. O time preenche um CSV (uma linha por
  post, uma coluna por campo de texto); você sobe esse CSV no app Bulk Create do Canva, conecta
  as colunas aos textos do seu template uma vez, e gera todos os designs de uma vez só.
  Sem Canva Enterprise, sem Autofill API, sem conector e sem templates com "data fields" especiais.
type: prompt
version: "1.0.0"
categories: [design, assets, social-media, human-in-the-loop]
---

# Canva Bulk Create (CSV) — Pro workflow

Apply a squad's copy to the user's Canva templates using Canva Pro's **native Bulk Create**
feature. The agent's job is to produce a **clean CSV** (the copy, structured) plus a clear
runbook. The user does the Bulk Create in Canva (one mapping, then generate all). The agent
never needs the Canva API or a connector.

## Why this path (important context)

- The user is on **Canva Pro**. The Canva **Autofill API / MCP** (`autofill-design`,
  brand-template datasets) requires **Canva Enterprise** — so that path is unavailable.
- **Bulk Create** is a built-in Canva **Pro** feature and needs NO API and NO special template
  setup — you connect CSV columns to *any* text element in a normal template.
- Result: reliable, works today, no upgrade required.

## When to use

Whenever a squad has produced multiple pieces of copy (a post calendar, a batch of captions,
carousel slides, ads, etc.) that should be poured into the user's Canva template(s).

## Workflow

### Step 1 — Gather the copy
Collect the squad's calendar + copy output (from `squads/{squad}/output/...`). Identify the
repeating fields each post has — e.g. `data`, `titulo`, `legenda`, `cta`, `hashtags`.

### Step 2 — Decide the columns (= the template's text slots)
Each **column** becomes one connectable field in Canva; each **row** becomes one design.
Name columns after the text they fill, in the user's language, e.g.:

`data, titulo, subtitulo, legenda, cta, hashtags`

If the template has an image placeholder and the copy includes image URLs, add an `imagem_url`
column (Bulk Create can connect image columns from URLs on Pro).

Keep it to the fields that actually exist as text/image elements in the template — extra
columns are fine (they just won't be connected).

### Step 3 — Write the CSV
Write a proper RFC-4180 CSV to:

```
squads/{squad}/output/{run_id}/canva/bulk-create.csv
```

Rules:
- First row = headers (the column names above).
- One row per post.
- Wrap any field containing a comma, quote, emoji-with-comma, or line break in double quotes;
  escape internal quotes by doubling them (`"`→`""`). Multi-line captions are fine inside a
  quoted field.
- Keep emojis and hashtags as-is.
- Do not merge multiple posts into one row.

After writing it, show the user a small preview (headers + first 2 rows) and the total row
count (= number of designs that will be generated).

### Step 4 — Emit the Bulk Create runbook (handoff)
Give the user this, filled in:

```
🎨 CANVA — Bulk Create (Pro)
Arquivo CSV gerado: squads/<squad>/output/<run_id>/canva/bulk-create.csv
Vai gerar: <N> designs (1 por linha)

1. Abra o seu template no Canva.
2. Barra lateral esquerda → "Apps" → busque "Bulk Create" → abra.
3. Clique em "Upload CSV" e selecione o arquivo acima.
4. Para CADA texto do design: clique com o botão direito no texto →
   "Connect data" → escolha a coluna correspondente
   (ex: título do design → coluna "titulo"; legenda → "legenda").
   (Se tiver imagem no template, conecte também a coluna "imagem_url".)
5. Clique em "Continue" → "Generate <N> designs".
6. O Canva cria todas as páginas. Revise, ajuste o que quiser e exporte.
7. (Opcional) me diga onde salvou os exports que eu sigo o pipeline.
```

### Step 5 — Checkpoint
Stop after emitting the CSV + runbook. Don't fabricate the finished designs. When the user
says it's done, continue (e.g., hand off to publishing).

## One-off edits (not bulk)
If the user just wants the copy for a single design (not a batch), skip the CSV and emit a
per-post card: the exact text for each slot + which template to open. Same handoff idea.

## Notes
- Bulk Create limits: Canva Pro allows a large number of rows per bulk run; for very large
  calendars, split into multiple CSVs (e.g., per week) if Canva caps a single upload.
- Column order in the CSV doesn't matter — connection is by column name, done once per element.
- The generated designs are normal Canva designs the user can freely edit afterward.
- If the user later moves to **Canva Enterprise**, the fully-automated Autofill API path becomes
  possible (reinstall `canva-sdks/canva-claude-skills@canva-bulk-create`). Until then, this is
  the correct approach.
