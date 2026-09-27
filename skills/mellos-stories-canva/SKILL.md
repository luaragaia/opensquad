---
name: mellos-stories-canva
description: >
  Fill a Mellos Stories roteiro directly into the "Classic Brown" Canva pack via the Canva
  connector (no CSV, no Enterprise). Given a tela-by-tela roteiro, the agent picks matching
  layout pages, copies them into a fresh working design, writes the copy into each text slot,
  auto-fits when copy is longer than the slot, and delivers the EDIT LINK plus per-tela cover
  image (scene) suggestions for Leonardo. NEVER exports — the Canva design is the deliverable.
description_pt-BR: >
  Preenche um roteiro de Stories da Mellos direto no pack "Classic Brown" do Canva pelo conector
  (sem CSV, sem Enterprise). A partir do roteiro tela-a-tela, escolhe as páginas de layout,
  copia pra um arquivo de trabalho, escreve a copy em cada slot, faz auto-ajuste quando o texto
  é maior que o slot, e entrega o LINK de edição + sugestões de cena (imagem de capa) por tela
  pro Leonardo. NUNCA exporta — o arquivo Canva é a entrega.
type: prompt
version: "1.0.0"
categories: [design, assets, social-media, canva, mellos, human-in-the-loop]
---

# Mellos Stories → Canva (preenchimento direto via conector)

Apply a Mellos Stories roteiro's copy to the Classic Brown Canva pack **programmatically**,
using the Canva connector's `edit-design` (`replace_text` / `format_text` / `position_element`).
No CSV, no Autofill API, no Enterprise. Works on Canva Pro because it edits a **copy** the user owns.

## ⛔ Hard rules (user preferences — do not violate)

1. **NEVER export.** The exported PNG/JPG is NOT the final result (backgrounds still come from
   Leonardo). Do not call `export-design`. The **deliverable is the Canva edit link**.
2. **Deliver at the end:** (a) the **edit link** of the working design, and (b) **per-tela cover
   image / scene suggestions** for the user to generate in Leonardo (see [[image-pipeline-leonardo]]).
3. **Never touch the master pack.** Always work on a `copy-design` of it. Master = `DAHRePjVKZI`
   ("Cópia de Mellos", 85 pages). See [[mellos-client]].
4. Respect Mellos copy rules: **sem travessão (—/–)**, números padronizados (12 bancos · cerca de
   30 minutos · desde 2015 · +5.000 clientes), serviço gratuito, sem promessa absoluta.
5. **Sequência SEMPRE ordenada + nomeada `{dia}{letra}`** (regra geral — vale pra qualquer fill de
   Stories, todos os clientes). Cada tela recebe o código do dia + letra: `1a, 1b, 1c, 2a, 2b, …`.
   As páginas do design de trabalho ficam **na ordem exata de postagem** (`copy-design` com
   `page_numbers` na ordem das telas — nunca na ordem do pack). O roteiro/handoff usa esses códigos
   como rótulo de cada tela, e o título do design de trabalho encerra o intervalo (ex.: `… (1a→27c)`).
   Obs.: a API não renomeia título de página existente — a **ordem** das páginas carrega a sequência;
   o **código** vive no roteiro (e, se o usuário quiser visível, um pequeno rótulo de texto no canto).

## Inputs

- A roteiro like `squads/mellos-stories/output/<date>/roteiro-stories-*.md` — tela-by-tela, each
  tela naming a **Layout** archetype, a **CATEGORIA**, and the ready copy (frase grande, destaque,
  itens, corpo, rodapé), plus a `🎨 Imagem` scene prompt.

## The loop

1. **Group telas by layout archetype** and count how many pages of each you need.
2. **Pick pages** from the pack using the layout catalog below. If a layout is reused N times,
   include that page number N times isn't supported by `copy-design` (it dedupes) — instead pick
   N distinct pages of the same archetype (the pack has many capas/CTAs), or copy once and
   duplicate in-editor. Prefer distinct pages.
3. **`copy-design(design_id: DAHRePjVKZI, page_numbers: [...])`** → new working design. Its pages
   are in the order you listed. Record the mapping tela → working page index.
4. **`read-design(open_transaction: true, filter.fields: ["design_metadata"])`** to get a fresh
   `transaction_id` cheaply. Then read each page's CDF (`open_transaction` with `page_indices`)
   only if you need to confirm the current page-prefixed element IDs.
5. **Fill** each page with `replace_text` on the slot elements (see catalog). Keep `@mellosfinanciamentos`
   and the `CORAÇÃO COMPARTILHE SALVE` footer. Set `CATEGORIA` to the tela's tag.
6. **Auto-fit** (critical): capa/hero slots were sized for short words. When copy is longer:
   reduce `font_size`, `position_element` to a clear area, `resize_element` width for subtitles.
   Verify against the returned after-thumbnail before moving on.
7. **Commit IMMEDIATELY** after finishing all pages — `finalize: "commit"` with empty operations.
   ⚠️ Transactions EXPIRE if left open across idle gaps; uncommitted edits are lost. Do not pause
   between the last edit and the commit.
8. **Deliver:** the edit link + the per-tela scene suggestions file (do NOT export).

## Stable element IDs (catalog)

The **trailing element id** (after the page prefix `PBxxxx-`) is **stable across copies** — only the
page prefix changes. So target slots by their trailing id after reading the working copy's prefix.

### Layout: CAPA (hero) — pack page **40** ("PACK CLASSIC BROWN")
- Big title: `…-LBz7Lfz4YyHhK3kV` (font ~97; drop to ~50-72 for sentences)
- Eyebrow/subtitle: `…-LB5qnR1PdHDZNr5z` (short by default; widen + reposition for a full line)
- CATEGORIA: `…-LB5BNFHchlDNBHWm`
- @handle: `…-LBV043R8V12yg0nR` (keep) · footer group: `…-LBDj45dxg3NCTJtn`
- Fit recipe used: title font 50 @ top 250 left 4; subtitle width 880/900 @ top ~1120 font 30.

### Layout: CHECKLIST ("checklist do dia") — pack page **68**
- Title: `…-LBfnmtQDnbTbSLDC` · Subtitle ("Notas"): `…-LB0rHYN7hyh4TnCs`
- List (one text element, `\n`-separated): `…-LBRxmrkJSNC3hWNR` — **6 checkbox slots**, so write **6 items**.
- CATEGORIA: `…-LBb3Ck1dvrh3NqKf`
- Alt checklist: pack page **51** ("Identifique sua força", 5 items).

### Layout: CTA / SALVE ("salve esta postagem") — pack page **76**
- Hero title: `…-LBcfb0Lqkc5x7lr4` (font ~101; drop to ~58-60 for a sentence)
- Body/CTA paragraph: `…-LBrcP78NXFtyRpRp`
- Reaction chips (keep): AMOR `…-LBBF4BvMLgrcBSxm` · COMENTE `…-LBd8Ylj8cRnbGcCq` · SALVAR `…-LBPCKwT6RJmzK2DX`
- CATEGORIA: `…-LBmFGHNC6RHsQ2z3`

> Other archetypes in the pack (not yet ID-mapped): numerado 01/02 (pages 66-67), corpo de texto
> (e.g. "Por que isso é tão importante"), comparação/enquete ("QUAL É A SUA escolha?", page 59),
> citação/depoimento. Map their slot ids the first time you use them and add here.

## Delivery format (end of run)

```
✅ Dia <N> pronto — <M> telas preenchidas.
🔗 Editar no Canva: <edit_url>

🎨 Fundos pra gerar no Leonardo (imagem de capa por tela):
| Tela | Página no Canva | Cena |
| ...  | ...             | ...  |
(+ prompts prontos + negative prompt, ver template abaixo)
```

Also write a `IMAGENS-LEONARDO-dia<N>.md` in the run's output folder with: edit link, a
tela → **Canva page number** → scene table (page order ≠ tela order after copy!), ready-to-paste
Leonardo prompts (from the roteiro's `🎨 Imagem`), the standard negative prompt, and the
"como trocar o fundo" steps. See [[perplexity-trends-handoff]] style of ready-to-run handoffs.

## Gotchas

- `copy-design` regenerates page prefixes but keeps trailing element ids → catalog stays valid.
- Page order in the copy follows your `page_numbers` array, NOT tela order — track the mapping and
  label deliverables by tela, not page.
- Weird coordinates (x > 1080, negative) are normal (anchored/transformed space) — prefer editing
  text + font size over repositioning when a slot already looks right.
- Long headline in a big-font hero slot overflows/collides → always auto-fit + verify thumbnail.
