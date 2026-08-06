# Auditoria de Marketing: Mellos Financiamentos

**URL:** http://mellosfinanciamentos.com.br/
**Data:** 05/08/2026
**Tipo de negócio:** Serviços financeiros (correspondente bancário) com captação por lead-gen no WhatsApp, modelo híbrido B2C + B2B
**Nota Geral de Marketing: 63/100 (Grau: C)**

> Parte 1 da trilha (Diagnóstico). Este documento é a visão macro. Os aprofundamentos estão em SEO-AUDIT.md, LANDING-CRO.md e FUNNEL-ANALYSIS.md. A camada de estratégia e marca está em COMPETITOR-REPORT.md e BRAND-VOICE.md.

---

## Resumo Executivo

A Mellos chega ao diagnóstico com uma base de marca invejável para o setor: mais de 10 anos de operação, mais de 5.000 clientes, dezenas de avaliações reais no Google e um posicionamento afiado (vários bancos competindo pela proposta do cliente, atendimento humano no WhatsApp, sem custo e sem risco para o parceiro). A copy do site é boa, direta e humana, e trata objeções de frente (o bloco "Mas é seguro? Não é golpe?" é um dos melhores ativos do site). Essa fundação sustenta a maior parte da nota.

O que segura a nota em 63 (grau C) não é a mensagem, é a **execução técnica e de conversão**. O site é uma aplicação JavaScript (SPA) com `title` genérico "Mellos" repetido em todas as páginas, sem meta description, com `lang="en"` (idioma errado), sem dados estruturados (schema), sem `robots.txt` e sem `sitemap.xml` (ambos retornam 404). Para um negócio que quer "ser conhecido" e "expandir para outros estados", isso significa deixar tráfego orgânico na mesa. Ao mesmo tempo, o formulário da home pede 9 campos, incluindo CPF, data de nascimento e placa logo de cara, o que cria fricção e ativa exatamente a objeção de segurança que a marca trabalha tão bem no texto.

Há ainda um problema de **consistência que já vaza para o público**: o site alterna entre "15 bancos", "12 disputando" e "até 15" (o padrão definido internamente é 12); a página Sobre diz "desde 2016" enquanto o padrão é 2015; o rodapé promete "Simule em 20 minutos" e o formulário promete "Resposta em até 1h útil", ambos divergindo do "30 minutos" oficial. Some-se o typo "Por que **escolhar** a Mellos?" na home. Nenhum desses erros é caro de corrigir, mas juntos corroem a percepção de credibilidade, que é justamente o principal valor da marca.

**As três ações de maior impacto:**
1. Corrigir a fundação técnica de SEO (title/meta por página, `lang="pt-BR"`, schema, robots, sitemap). Baixo esforço, destrava descoberta orgânica.
2. Reduzir a fricção do formulário (pedir só nome + WhatsApp + tipo de veículo no primeiro passo; CPF/placa só depois do "sim"). Impacto direto em leads gerados.
3. Padronizar números e mensagens em todo o site (12 bancos, 2015, 30 minutos) e corrigir o typo e os links quebrados de rodapé.

**Impacto estimado de implementar todas as recomendações:** aumento relevante no volume de simulações qualificadas e na descoberta orgânica, com esforço majoritariamente de "quick win". O gargalo hoje não é a proposta, é o atrito e a invisibilidade.

---

## Detalhamento da Nota

| Categoria | Nota | Peso | Nota Ponderada | Principal achado |
|----------|-------|--------|---------------|-------------|
| Conteúdo & Mensagem | 78/100 | 25% | 19,5 | Copy forte e humana, mas com inconsistências numéricas e um typo visível |
| Otimização de Conversão | 62/100 | 20% | 12,4 | Formulário de 9 campos pedindo CPF logo de início; CTA "Simule" aponta para `#` |
| SEO & Descoberta | 34/100 | 20% | 6,8 | Title genérico, sem meta description, `lang=en`, sem schema, sem robots/sitemap |
| Posicionamento Competitivo | 70/100 | 15% | 10,5 | Diferenciação clara (multibanco, complementar), mas sem conteúdo de comparação |
| Marca & Confiança | 76/100 | 10% | 7,6 | Prova social real e abundante; porém links de Termos e Privacidade quebrados |
| Crescimento & Estratégia | 64/100 | 10% | 6,4 | Programa de parceria sólido, mas canal único e sem captura/nutrição de e-mail |
| **TOTAL** | | **100%** | **63,2/100** | **Grau C: fundação boa, execução técnica e de conversão atrasada** |

---

## Quick Wins (Esta Semana)

1. **Corrigir `lang="en"` para `lang="pt-BR"`.** Uma linha. Afeta acessibilidade, SEO e a forma como o Google interpreta o idioma do site.
2. **Dar `title` e `meta description` únicos por página.** Ex.: Home = "Financiamento de Veículos em até 12 Bancos | Mellos Financiamentos". Cada rota (pra-voce, vendedores, sobre, faq) com seu próprio título e descrição. Impacta toda impressão de busca.
3. **Corrigir o typo "escolhar" → "escolher"** no título "Por que escolher a Mellos?". Erro de português na dobra da home mina credibilidade instantaneamente.
4. **Padronizar o número de bancos em 12** em todo o site. Hoje convivem "15 bancos", "até 15" e "12 disputando" na mesma página. Escolher um número e repeti-lo.
5. **Padronizar o tempo de resposta em 30 minutos.** Remover "Simule em 20 minutos" (rodapé) e alinhar "Resposta em até 1h útil" do formulário com a promessa oficial.
6. **Corrigir "desde 2016" → "desde 2015"** na página Sobre (o vídeo já foi corrigido; o texto ficou para trás).
7. **Consertar os links quebrados do rodapé** (Termos de Serviço e Política de Privacidade apontam para `#`). Para quem menciona LGPD como diferencial, uma Política de Privacidade inexistente é uma contradição de confiança.
8. **Adicionar `alt` descritivo às 10 imagens sem alt** (de 32 no total). Ganho de SEO e acessibilidade.

## Recomendações Estratégicas (Este Mês)

1. **Reduzir a fricção do formulário para captura em 2 etapas.** Passo 1 pede só nome, WhatsApp e tipo de veículo. CPF, placa e data de nascimento migram para a conversa no WhatsApp ou para um passo 2 após o lead demonstrar intenção. Detalhes em LANDING-CRO.md e FUNNEL-ANALYSIS.md.
2. **Criar `robots.txt` e `sitemap.xml`** e garantir renderização indexável das rotas internas (pré-renderização/SSR). Sem isso, pra-voce, vendedores, sobre e faq podem não ranquear.
3. **Marcar o FAQ com schema FAQPage (JSON-LD).** O conteúdo já existe e é excelente; o schema pode render rich results na busca. Adicionar também Organization/LocalBusiness e Review/AggregateRating.
4. **Publicar uma página de comparação "Direto no banco x Mellos".** A copy já argumenta isso ("Falar com um banco só é aceitar uma resposta"); transformar em página indexável captura busca de fundo de funil.

## Iniciativas de Longo Prazo (Este Trimestre)

1. **Motor de conteúdo/SEO local por estado.** Para sustentar a meta de expansão nacional, criar conteúdo para termos como "financiamento de veículo [cidade/estado]", "financiar carro com nome negativado" e "refinanciamento de veículo".
2. **Segundo canal de captura além do WhatsApp.** Captura de e-mail com nutrição para quem simula mas não fecha na hora, reduzindo dependência de um único canal.
3. **Portal/fluxo estruturado para o parceiro (B2B).** O programa de parceria é um diferencial de crescimento; formalizá-lo (materiais, acompanhamento de comissão) amplia a rede de indicação, que já é a maior origem de negócios.

---

## Análise Detalhada por Categoria

### Conteúdo & Mensagem (78/100)
A copy é o ponto mais forte do site. Passa no teste dos 5 segundos ("Seu próximo veículo em apenas 30 minutos e sem burocracia"), a proposta de valor multibanco é imediata, e o tom é humano e coloquial ("a gente", "gente de verdade, pelo WhatsApp. Nada de robô"). O tratamento de objeções é exemplar, com o bloco "Mas é seguro? Não é golpe?" enfrentando o maior medo do público de frente. A prova social é real e nominal.
**O que tira pontos:** inconsistências numéricas visíveis (12/15 bancos, 20/30 min, 2015/2016) e o typo "escolhar". Em um negócio cujo ativo central é credibilidade, descuido textual custa caro.

### Otimização de Conversão (62/100)
Os CTAs de WhatsApp são claros, específicos e onipresentes, com mensagens pré-preenchidas por público (cliente, parceiro, trabalhe conosco), o que é ótimo. A home ainda oferece um formulário de simulação, criando dois caminhos de conversão.
**O que tira pontos:** o formulário pede 9 campos (nome, tipo de veículo, condição, WhatsApp, CPF, data de nascimento, CNH, placa, valor), incluindo dados sensíveis logo no primeiro contato, o que aumenta abandono e ativa a objeção de segurança. O botão "Simule" do topo aponta para `#` (não leva ao formulário nem ao WhatsApp). Aprofundamento em LANDING-CRO.md.

### SEO & Descoberta (34/100)
Categoria mais fraca e a de maior alavancagem. `title` genérico "Mellos" repetido em todas as rotas, ausência de meta description, `lang="en"`, ausência de dados estruturados, `robots.txt` e `sitemap.xml` inexistentes (404), e arquitetura SPA que pode dificultar indexação das páginas internas. O conteúdo (sobretudo o FAQ) é rico e merece ser encontrado. Detalhes em SEO-AUDIT.md.

### Posicionamento Competitivo (70/100)
A diferenciação é nítida e defensável: modelo multibanco, posicionamento complementar (não concorrente) para o parceiro, e aprovação de perfis difíceis. A marca sabe exatamente contra o que compete (o "banco único" e o "não" dele).
**O que tira pontos:** essa vantagem vive só na copy solta; não há páginas de comparação nem conteúdo que capture a busca de quem está pesquisando alternativas. Detalhes em COMPETITOR-REPORT.md.

### Marca & Confiança (76/100)
Sinais de confiança fortes: mais de 10 anos, mais de 5.000 clientes, avaliações reais do Google Meu Negócio exibidas com nome, menção explícita à LGPD, bancos parceiros reconhecidos (Santander, Itaú, C6, Safra, PAN, Bradesco, BV, Volkswagen). Rostos da marca (Luara e Amilcar) disponíveis para humanizar.
**O que tira pontos:** links de Termos de Serviço e Política de Privacidade quebrados (`#`) contradizem o discurso de segurança; redes sociais no rodapé ainda sem link.

### Crescimento & Estratégia (64/100)
O programa de parceria (comissão por contrato, sem custo/risco/exclusividade) é um motor de crescimento real, alinhado ao fato de que a maioria dos novos negócios vem por indicação. Modelo de receita saudável (remunerado pelos bancos).
**O que tira pontos:** dependência de um único canal (WhatsApp), ausência de captura de e-mail e de nutrição para leads frios, e ausência de motor de conteúdo para sustentar a expansão nacional pretendida.

---

## Comparação Competitiva (resumo)

O detalhamento está em COMPETITOR-REPORT.md. Em uma linha: no eixo "canal único do banco/loja x correspondente multibanco", a Mellos ocupa um território de diferenciação que a maioria dos correspondentes locais não comunica bem. A vantagem existe; falta empacotá-la em ativos indexáveis.

---

## Resumo de Impacto por Recomendação

| Recomendação | Esforço | Impacto | Prazo |
|---------------|--------|------------|----------|
| Corrigir fundação técnica de SEO (title/meta/lang/schema/robots/sitemap) | Baixo | Alto | 1 semana |
| Reduzir fricção do formulário (captura em 2 etapas) | Médio | Alto | 2 a 4 semanas |
| Padronizar números e mensagens + corrigir typo e links quebrados | Baixo | Médio-Alto | 1 semana |
| Página de comparação "Direto no banco x Mellos" | Médio | Médio-Alto | 2 a 4 semanas |
| Motor de conteúdo/SEO local por estado | Alto | Alto | Trimestre |
| Captura de e-mail + nutrição | Médio | Médio | Trimestre |

---

## Próximos Passos

1. Executar o pacote de quick wins técnicos e de consistência (itens de "Esta Semana").
2. Redesenhar o formulário de captura para reduzir fricção (ver LANDING-CRO.md e FUNNEL-ANALYSIS.md).
3. Avançar para a camada de estratégia: consolidar diferenciação (COMPETITOR-REPORT.md) e guia de voz (BRAND-VOICE.md) para orientar todo o conteúdo futuro.

*Gerado pela AI Marketing Suite — Fase 1 (Diagnóstico), etapa 1/4 · `/market audit`*
