# Auditoria de SEO de Conteúdo

## http://mellosfinanciamentos.com.br/
### Data: 05/08/2026

> Parte 1 da trilha (Diagnóstico), etapa 2/4. Complementa MARKETING-AUDIT.md com o aprofundamento técnico e de conteúdo para busca orgânica.

---

## Nota de Saúde de SEO: 34/100

Categoria mais fraca do diagnóstico e, por isso, a de maior potencial de retorno. O conteúdo do site é bom (o FAQ é excelente), mas a fundação técnica está praticamente ausente. Hoje a Mellos depende de indicação e tráfego direto; virtualmente nada foi feito para ser encontrado por quem pesquisa "financiamento de veículo" no Google. Para a meta declarada de expandir para outros estados, isso é o gargalo número um.

---

## Checklist de SEO On-Page

### Title Tag
- **Status: Falha**
- **Atual:** `Mellos` (idêntico em todas as rotas: home, pra-voce, vendedores, sobre, depoimentos, faq)
- **Recomendado (home):** `Financiamento de Veículos em até 12 Bancos | Mellos Financiamentos`
- **Problemas:** título de uma palavra, sem palavra-chave, sem proposta de valor, duplicado em todas as páginas. Um dos ajustes de maior alavancagem do site inteiro, porque afeta cada impressão na busca.
- **Sugestões por página:**
  - `/pra-voce` → `Simule o Financiamento do Seu Carro ou Moto | Mellos`
  - `/vendedores` → `Seja Parceiro e Ganhe Comissão por Indicação | Mellos`
  - `/sobre` → `Quem Somos: Correspondente Bancário há 10+ Anos | Mellos`
  - `/depoimentos` → `Avaliações de Clientes no Google | Mellos Financiamentos`
  - `/faq` → `Perguntas Frequentes sobre Financiamento de Veículos | Mellos`

### Meta Description
- **Status: Falha** (ausente em todas as páginas)
- **Recomendado (home):** `Financie carro, moto ou utilitário com a Mellos. Colocamos até 12 bancos para disputar sua proposta e trazemos a melhor taxa no seu WhatsApp em cerca de 30 minutos. Sem consulta ao Serasa para simular.` (aprox. 155 caracteres)
- Cada rota deve ter sua própria descrição, funcionando como anúncio do resultado de busca.

### Hierarquia de Cabeçalhos (H1-H6)
- **Status: Precisa de Trabalho**
- **Home:** foram detectados **4 elementos H1** ("Seu próximo veículo...", "Simule sua proposta", "Por que escolhar a Mellos?", "Mais que crédito. Uma decisão melhor."). O ideal é **exatamente um H1 por página**. Os demais deveriam ser H2.
- **Typo no cabeçalho:** "Por que **escolhar** a Mellos?" (deveria ser "escolher"). Erro de português em cabeçalho, alto risco de percepção negativa.
- H2/H3 nas demais páginas estão razoáveis e descritivos (ex.: "Como funciona", "Por que vale a pena simular").
- **Ação:** um único H1 por rota, contendo a palavra-chave da página, com o restante rebaixado para H2/H3.

### Otimização de Imagens
- **Status: Precisa de Trabalho**
- **10 de 32 imagens sem atributo `alt`** na home.
- **Ação:** adicionar `alt` descritivo (ex.: "Logo do banco Santander, parceiro Mellos") e usar nomes de arquivo descritivos. Preferir WebP com compressão e `lazy loading` abaixo da dobra.

### Links Internos
- **Status: Precisa de Trabalho**
- A navegação principal cobre as rotas certas (pra-voce, vendedores, sobre, depoimentos, faq).
- **Problemas:** vários links apontam para `#` (âncoras vazias): "Simule" (topo), "Ver mais perguntas", "Termos de Serviço", "Política de Privacidade" e ícones de redes sociais. Links quebrados prejudicam experiência, rastreamento e confiança.
- Falta linkagem contextual entre conteúdo e páginas de conversão (ex.: o FAQ poderia linkar para pra-voce e vendedores no texto das respostas).

### Estrutura de URL
- **Status: Passa (parcial)**
- URLs limpas e legíveis (`/pra-voce`, `/vendedores`, `/sobre`, `/faq`). Bom uso de hifens, minúsculas, sem parâmetros.
- **Ressalva:** por ser SPA, todas as rotas retornam o mesmo `title`/estado inicial; é preciso garantir que cada URL entregue metadados próprios ao rastreador.

---

## Qualidade de Conteúdo (E-E-A-T)

| Dimensão | Nota | Evidência |
|---|---|---|
| Experiência | Presente | Casos reais, depoimento detalhado de parceiro (Moisés, Stop Veículos, cliente há mais de 5 anos), linguagem de quem opera o dia a dia |
| Especialização | Presente | Foco exclusivo em financiamento de veículos, explicação clara do processo, bancos nomeados |
| Autoridade | Presente-Forte | Mais de 10 anos, mais de 5.000 clientes, avaliações do Google exibidas; falta reforçar com autoria/bios (Luara e Amilcar) e menções externas |
| Confiabilidade | Precisa de Trabalho | HTTPS presente e menção à LGPD, mas Política de Privacidade e Termos apontam para `#` (inexistentes), sem endereço físico visível e sem página de autoria |

**Prioridade E-E-A-T:** publicar de fato a Política de Privacidade e os Termos (coerência com o discurso de LGPD) e adicionar uma seção de autoria com os sócios reforça Autoridade e Confiabilidade ao mesmo tempo.

---

## Análise de Palavras-Chave

- **Palavra-chave primária (home):** "financiamento de veículos" (intenção comercial/transacional)
- **Alinhamento de intenção:** bom. A home entrega simulação e prova social, coerente com quem busca financiar.
- **Colocação da palavra-chave:**
  - No title: **ausente** (corrigir)
  - No H1: presente ("Seu próximo veículo...", mas sem o termo "financiamento" explícito)
  - Nos primeiros 100 caracteres do corpo: presente ("Financiamos carros, motos e utilitários")
  - Na URL: parcial
  - Na meta description: ausente (não existe meta)

**Palavras-chave secundárias a trabalhar naturalmente no conteúdo:**
- financiamento de carro / moto / utilitário
- refinanciamento de veículo / crédito com garantia veicular
- financiar carro com nome negativado
- simulação de financiamento de veículo
- financiamento de veículo para autônomo
- correspondente bancário financiamento veículo
- financiar veículo acima de 10 anos

**Análise de intenção de busca:** o site cobre bem intenção transacional (simular/financiar) e informacional (FAQ). Falta capturar intenção **comercial** ("melhor financiamento", "direto no banco ou correspondente", "vantagens de simular em vários bancos") com páginas dedicadas.

---

## SEO Técnico

- **`lang` do documento:** `en` (**incorreto**). Deve ser `pt-BR`. Ajuste de uma linha, impacto em como o Google interpreta o idioma.
- **Viewport:** presente e correto (`width=device-width, initial-scale=1`). Mobile-friendly na base.
- **`robots.txt`:** **404 (inexistente).** Criar, permitindo rastreio e apontando o sitemap.
- **`sitemap.xml`:** **404 (inexistente).** Criar com todas as rotas e submeter ao Google Search Console.
- **Canonical:** **ausente.** Adicionar tag canônica autorreferente em cada página.
- **Open Graph / Twitter Cards:** **ausentes.** Sem OG, compartilhamentos em WhatsApp/redes ficam sem título, descrição e imagem, o que é crítico para um negócio que vive do WhatsApp.
- **Dados estruturados (JSON-LD):** **nenhum detectado.** Grande oportunidade (ver seção Schema).
- **Renderização:** aplicação SPA. O HTML inicial trouxe conteúdo legível no teste de rastreador, mas o `title`/metadados não vieram por página. Recomenda-se pré-renderização ou SSR das rotas para garantir indexação de pra-voce, vendedores, sobre e faq.
- **Velocidade:** os recursos da página são poucos (baixa contagem de requisições no teste), o que é positivo. Ainda assim, otimizar imagens (WebP) e garantir dimensões definidas evita CLS.

---

## Análise de Lacunas de Conteúdo (Content Gaps)

| Tópico ausente | Potencial de busca | Concorrência | Formato necessário | Prioridade |
|---|---|---|---|---|
| "Financiar carro com nome negativado" | Alto | Média | Página/artigo | 1 |
| "Direto no banco x correspondente bancário" | Médio-Alto | Baixa | Página de comparação | 1 |
| "Refinanciamento de veículo: como funciona" | Alto | Média | Página de serviço | 2 |
| "Financiamento para autônomo sem holerite" | Médio | Baixa | Artigo/FAQ expandido | 2 |
| "Documentos para financiar um veículo" | Médio | Baixa | Artigo (featured snippet) | 3 |
| "Financiamento de veículo em [estado/cidade]" | Alto (long-tail) | Baixa | Páginas locais (expansão) | 2 |
| "Vale a pena financiar veículo seminovo?" | Médio | Baixa | Artigo | 3 |

O site hoje é essencialmente institucional/transacional. Cada linha acima é tráfego qualificado que os concorrentes podem capturar primeiro.

---

## Oportunidades de Featured Snippet

O FAQ já está no formato ideal (pergunta como cabeçalho + resposta curta). Com pequenos ajustes, vira máquina de snippets:
- **Parágrafo:** manter respostas de 40 a 60 palavras logo abaixo de perguntas como "O que é a Mellos Financiamentos?" e "Tenho restrição no nome. Ainda consigo financiar?".
- **Lista:** transformar "Quais documentos preciso para financiar?" em lista ordenada (RG/CNH, CPF, comprovante de residência, comprovante de renda).
- **Tabela:** "Com quais bancos vocês trabalham?" pode virar tabela.
- Marcar tudo com schema FAQPage (ver abaixo).

---

## Schema Markup

| Tipo de Schema | Aplicável a | Status | Ação |
|---|---|---|---|
| Organization | Home, Sobre | Ausente | Adicionar (nome, logo, contato, redes) |
| LocalBusiness / FinancialService | Home | Ausente | Adicionar (região de origem RS, atendimento nacional) |
| FAQPage | /faq e blocos de FAQ | Ausente | Alta prioridade, conteúdo já existe |
| Review / AggregateRating | /depoimentos | Ausente | Marcar avaliações reais do Google |
| BreadcrumbList | Todas | Ausente | Adicionar |
| WebSite / SearchAction | Home | Ausente | Opcional |

**Diretriz:** usar JSON-LD, validar no Teste de Resultados Ricos do Google e manter os dados consistentes com o que aparece na página (ex.: número de bancos padronizado em 12).

---

## Oportunidades de Linkagem Interna

1. **Respostas do FAQ** devem linkar para `/pra-voce` (cliente) e `/vendedores` (parceiro) no texto.
2. **Home** deve linkar para o FAQ nos blocos de objeção ("Negativados podem financiar?" → resposta completa no FAQ).
3. **Depoimentos** deve linkar de volta para a simulação (converter prova social em ação).
4. Corrigir a âncora "Ver mais perguntas" (hoje `#`) para apontar ao `/faq`.
5. Criar hub de conteúdo (blog) que aponte para as páginas de serviço (financiamento, refinanciamento, compra à vista).

---

## Core Web Vitals (avaliação)

O site é leve (poucas requisições, script único, TTFB baixo no teste), o que é uma vantagem. Riscos a monitorar:
- **LCP:** garantir que a imagem principal do hero seja otimizada e pré-carregada.
- **CLS:** definir dimensões de imagens e reservar espaço (as 10 imagens sem alt sugerem markup de imagem descuidado).
- **INP:** SPA com um bundle JS; monitorar interatividade no mobile.
Boa performance de base sustenta conversão; não desperdiçar isso com imagens não otimizadas.

---

## Recomendações de Estratégia de Conteúdo

1. **Cadência:** iniciar com 2 a 4 conteúdos por mês focados nas lacunas de alta prioridade (negativado, refinanciamento, comparação).
2. **Formatos:** páginas de serviço + artigos de FAQ expandido + páginas de comparação. Vídeo institucional já existe (aproveitar com transcrição indexável).
3. **Estratégia de palavras-chave:** equilibrar termos comerciais de alto volume com long-tail local ("financiamento de veículo em [cidade]") para sustentar a expansão.
4. **Atualização:** revisar o FAQ trimestralmente e manter números padronizados (12 bancos, 30 min, 2015).

---

## Recomendações Priorizadas

### Crítico (Corrigir Imediatamente)
1. Trocar `lang="en"` por `lang="pt-BR"`.
2. Title e meta description únicos por página.
3. Criar `robots.txt` e `sitemap.xml` (hoje 404).
4. Corrigir o typo "escolhar" → "escolher" no H1.
5. Publicar Política de Privacidade e Termos (links hoje quebrados) e corrigir âncoras `#`.

### Alta Prioridade (Este Mês)
1. Adicionar JSON-LD: FAQPage, Organization, LocalBusiness, AggregateRating.
2. Um único H1 por página, com palavra-chave.
3. Adicionar Open Graph/Twitter Cards (essencial para compartilhamento no WhatsApp).
4. Garantir renderização indexável (pré-render/SSR) das rotas internas.
5. `alt` em todas as imagens.

### Média Prioridade (Este Trimestre)
1. Página de comparação "Direto no banco x Mellos".
2. Conteúdos das lacunas de alta prioridade (negativado, refinanciamento, autônomo).
3. Canonical e BreadcrumbList em todas as páginas.

### Baixa Prioridade (Quando Houver Recurso)
1. Páginas locais por estado/cidade para expansão.
2. Hub de conteúdo/blog com linkagem interna estruturada.

*Gerado pela AI Marketing Suite — Fase 1 (Diagnóstico), etapa 2/4 · `/market seo`*
