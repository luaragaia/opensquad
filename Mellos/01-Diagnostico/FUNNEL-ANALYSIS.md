# Análise de Funil: Mellos Financiamentos

**URL:** http://mellosfinanciamentos.com.br/
**Data:** 05/08/2026
**Tipo de negócio:** Correspondente bancário (serviços financeiros)
**Tipo de funil:** Lead Gen (captação → atendimento humano no WhatsApp → contrato)
**Saúde Geral do Funil: 66/100**

> Parte 1 da trilha (Diagnóstico), etapa 4/4. Fecha o diagnóstico mapeando o caminho completo da visita ao contrato e onde ele vaza.

---

## Resumo Executivo

O funil da Mellos é um funil de geração de leads com fechamento humano: o site (ou a indicação) leva o interessado ao WhatsApp, onde um especialista conduz simulação, proposta e contrato. A grande força é o **fechamento humano** (diferencial real, o "gente de verdade, nada de robô") e a **origem por indicação**, que entra no funil já com confiança pré-construída e alta taxa de conversão. Existem dois pontos de entrada bem desenhados: CTAs de WhatsApp com mensagem pré-preenchida por público, e um formulário de simulação.

O maior gargalo está **no topo, no site**: o formulário pede 9 campos (incluindo CPF e placa) antes de qualquer relacionamento, e o CTA primário "Simule" do hero aponta para `#`. Ou seja, parte do tráfego que chegaria ao WhatsApp trava na porta de entrada. Um segundo gargalo é a **ausência de recuperação**: quem não fecha na hora simplesmente some, porque não há captura de e-mail nem nutrição. Como o negócio depende de um único canal (WhatsApp), leads frios não têm um segundo caminho de volta.

**Top 3 correções:**
1. Reduzir o formulário para captura de 2 etapas (3 campos no passo 1) e consertar o CTA "Simule" quebrado. Destrava o topo do funil.
2. Criar um fluxo de recuperação para simulações não fechadas (retomada no WhatsApp + captura leve de e-mail). Recupera valor que hoje evapora.
3. Formalizar a entrada B2B do parceiro (fluxo de indicação em 1 minuto), já que a indicação é a origem mais rentável.

---

## Mapa do Funil

```
FLUXO DO VISITANTE
==================

Origens de tráfego
  Indicação (maioria) · Direto · Busca (subutilizada) · Redes (incipiente)
  |
  v
[Site / Home] --------------- 100% dos visitantes
  |  (perde quem clica em "Simule" -> # ; e quem trava no formulário de 9 campos)
  v
[Intenção: formulário OU clique no WhatsApp] --- % reduzida pela fricção
  |
  v
[Conversa no WhatsApp] ------- especialista assume (ponto forte)
  |  informa CPF, data, placa, valor
  v
[Simulação em ~12 bancos] ---- resultado em ~30 min
  |
  v
[Proposta apresentada] ------- cliente aprova
  |
  v
[Documentos + Contrato] ------ assinatura
  |
  v
[Financiamento fechado] ------ banco libera crédito; Mellos remunerada; parceiro recebe comissão

Observação: a indicação entra já perto do meio do funil (confiança pré-construída),
por isso converte muito acima do tráfego frio.
```

---

## Análise Página a Página

### Passo 1: Home / Landing (site)
- **Ação primária:** iniciar simulação (formulário) ou abrir WhatsApp.
- **Notas:** Clareza 9 · Continuidade 8 · Motivação 8 · Fricção 5 · Confiança 8 → **Média 7,6/10**
- **Fricção:** formulário de 9 campos com CPF/placa/nascimento no primeiro contato; CTA "Simule" do hero aponta para `#`; inconsistência 12/15 bancos e 20/30 min.
- **Confiança:** prova social real, "+5000", menção a bancos e LGPD. Boa.
- **Correções:** captura em 2 etapas; consertar CTA; microcopy "não consulta Serasa"; padronizar números. (Ver LANDING-CRO.md.)

### Passo 2: Transição para o WhatsApp
- **Ação primária:** enviar a primeira mensagem (pré-preenchida).
- **Notas:** Clareza 8 · Continuidade 8 · Motivação 8 · Fricção 8 · Confiança 7 → **Média 7,8/10**
- **Força:** mensagens pré-preenchidas por público (cliente / parceiro / trabalhe conosco) reduzem atrito e qualificam a origem.
- **Risco:** dependência total de um único canal; se o lead não responde, não há plano B (sem e-mail/retargeting).

### Passo 3: Atendimento e simulação no WhatsApp
- **Ação primária:** fornecer dados e receber proposta.
- **Notas:** Clareza 8 · Continuidade 9 · Motivação 8 · Fricção 7 · Confiança 9 → **Média 8,2/10**
- **Força:** atendimento humano do começo ao fim, resultado em ~30 min, capacidade de aprovar perfis difíceis (negativado caso a caso). Este é o coração do diferencial.
- **Risco:** processo manual (planilha) limita escala; tempo de resposta pode variar em pico.

### Passo 4: Proposta → Contrato
- **Ação primária:** aprovar e assinar.
- **Notas:** Clareza 8 · Continuidade 8 · Motivação 8 · Fricção 6 · Confiança 8 → **Média 7,6/10**
- **Fricção:** coleta de documentos e assinatura; oportunidade de guiar melhor (checklist de documentos, expectativa de prazo).
- **Confiança:** quem libera e assina é o banco (reforça segurança); comunicar isso explicitamente reduz desistência de última hora.

---

## Métricas do Funil

O negócio opera hoje sobre planilha (sem analytics de funil no site). As faixas abaixo são benchmarks de referência para lead-gen; recomenda-se instrumentar para medir o real.

```
MÉTRICAS A INSTRUMENTAR
=======================

Tráfego:
  Visitantes/mês: [medir - hoje sem analytics visível]
  Origem: indicação (alta), direto, orgânico (baixo/subutilizado), social (incipiente)

Conversão (benchmark lead-gen):
  Visitante -> Lead (simulação/WhatsApp): meta 3-10%
  Lead -> Proposta apresentada: alto (atendimento humano puxa)
  Proposta -> Contrato fechado: forte no tráfego de indicação
  Overall visitante -> cliente: varia muito por origem

Pipeline interno (do contexto operacional):
  +1.100 leads registrados
  ~90 parceiros cadastrados
  ~158 contratos fechados registrados
```

**Insight:** o funil converte bem depois que o lead chega ao WhatsApp; o problema é volume e recuperação no topo. Mais eficiente investir em (a) reduzir atrito de entrada e (b) recuperar quem não fecha, do que em pressionar o meio do funil, que já performa.

---

## Análise de Impacto em Receita

Sem RPV medido, o raciocínio de alavanca é qualitativo:
- **Alavanca 1 (entrada):** cada ponto de atrito removido no formulário/CTA converte tráfego já existente em conversas no WhatsApp, sem custo de mídia adicional.
- **Alavanca 2 (recuperação):** parte dos 1.100+ leads que não fecharam é recuperável com retomada estruturada. Reengajar leads é a mídia mais barata que existe.
- **Alavanca 3 (indicação B2B):** cada parceiro ativo multiplica o topo do funil com leads de alta conversão. Escalar de ~90 parceiros é o caminho de maior retorno.

---

## Recomendações de Otimização

### Prioridade 1 — Fazer Agora (Esta Semana)
- Consertar o CTA "Simule" (hero) e "Ver mais perguntas" (hoje `#`). Impacto alto, esforço baixo.
- Padronizar 12 bancos / 30 min / 2015 em todo o site.
- Microcopy de segurança no formulário ("não consulta seu Serasa").

### Prioridade 2 — Planejar (Este Mês)
- Formulário em 2 etapas (3 campos no passo 1; CPF/placa depois). Reduz abandono no ponto de maior objeção.
- Fluxo de recuperação: mensagem de retomada no WhatsApp para simulações não concluídas + captura leve de e-mail como canal alternativo.
- Fluxo B2B de indicação em 1 minuto, com material para o parceiro.

### Prioridade 3 — Estratégico (Este Trimestre)
- Instrumentar analytics de funil (eventos: iniciou form, enviou form, abriu WhatsApp).
- Nutrição por e-mail para leads frios (ver mapeamento abaixo).
- Migração da planilha para CRM (já no roadmap interno) dá visibilidade em tempo real do funil.

---

## Avaliação de Página de Preço

Não se aplica no modelo tradicional: não há tabela de preço (o serviço é gratuito para o cliente, remunerado pelos bancos). **Isso é um ativo de conversão** e deve ser dito com mais destaque no ponto de decisão: "O nosso serviço é gratuito. Quem remunera a Mellos são os bancos." Colocar essa frase perto do formulário remove uma objeção silenciosa ("será que vão me cobrar?").

## Avaliação de Isca Digital (Lead Magnet)

Hoje não há isca digital além da própria simulação. A simulação gratuita já funciona como oferta de topo. Oportunidades de isca de baixo atrito para capturar quem ainda não quer simular:
- "Simulador de parcela" leve (estimativa sem CPF) como primeira captura.
- Checklist "Documentos para financiar seu veículo" em troca de e-mail/WhatsApp.
Ranqueadas por eficácia: ferramenta/simulador > checklist > guia.

---

## Integração com Nutrição por E-mail

| Estágio do funil | Sequência recomendada |
|---|---|
| Visitante anônimo | Sem e-mail; usar CTA de WhatsApp e (futuro) retargeting |
| Lead (simulou, não fechou) | Retomada no WhatsApp + boas-vindas curtas por e-mail se capturado |
| Lead engajado | Nutrição: como funciona, segurança, casos de aprovação de negativado |
| Cliente | Pós-venda: satisfação, pedido de avaliação no Google, indicação |
| Parceiro | Onboarding do parceiro + lembretes de como indicar em 1 minuto |

Detalhamento de sequências fica para uma fase posterior (fora do escopo Diagnóstico + Marca desta trilha).

---

## Alinhamento por Origem de Tráfego

| Origem | Intenção | Melhor entrada | Funil recomendado |
|---|---|---|---|
| Indicação (parceiro/cliente) | Alta | WhatsApp direto | Curto: direto ao especialista |
| Busca por marca | Alta | Home/simulação | Curto |
| Busca não-marca ("financiar carro negativado") | Média | Conteúdo/página de serviço (a criar) | Médio: educar e converter |
| Redes sociais | Baixa-Média | Isca/simulação leve | Longo: capturar e nutrir |
| Direto | Alta | Home | Curto |

---

## Próximos Passos

1. Destravar o topo do funil: formulário de 2 etapas + consertar CTAs quebrados.
2. Criar recuperação para simulações não fechadas (WhatsApp + e-mail leve).
3. Instrumentar analytics para sair do benchmark e medir o funil real.

*Gerado pela AI Marketing Suite — Fase 1 (Diagnóstico), etapa 4/4 · `/market funnel`*
