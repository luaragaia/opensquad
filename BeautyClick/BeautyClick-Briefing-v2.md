# BeautyClick — Briefing da Plataforma

> **Escopo deste documento:** o que a plataforma BeautyClick é e tudo o que ela faz hoje — portal do
> cliente e portal do profissional. É o retrato funcional atual (inclui itens em desenvolvimento/em
> teste como se estivessem prontos). A atendente de WhatsApp tem briefing próprio em
> `BeautyClickIA-Briefing-v2.md`.
> **Atualizado:** 2026-08-05.

---

## O que é

BeautyClick é uma plataforma SaaS para profissionais de beleza autônomas (cabeleireiras, manicures,
lash designers, maquiadoras, esteticistas, etc.). Reúne, num só painel: **agenda online 24h**,
**site/vitrine profissional**, **cobrança de sinal**, **dashboard financeiro**, **controle de
estoque**, **fichas de anamnese**, **combos**, **marketing/retenção** e uma **atendente de IA no
WhatsApp**. A proposta central continua a mesma: *a cliente agenda sozinha, a profissional só atende*
— e o negócio dela roda inteiro dentro da plataforma.

O produto se divide em:

- **Portal do Cliente** — a vitrine pública da profissional (`beautyclick.com/{slug}`), onde as
  clientes conhecem os serviços e agendam.
- **Portal do Profissional** (`/admin`) — onde a profissional gerencia agenda, serviços, clientes,
  finanças, estoque, marketing e a IA.
- **Landing de marketing** (`/home`) — página pública de venda da plataforma, com planos, FAQ e
  captação de interessadas.

A diferença entre os planos define o que cada profissional enxerga (ver **Planos**).

---

## Planos e liberação de recursos

A plataforma é vendida em **3 planos mensais** (assinatura recorrente). Cada recurso é liberado por
plano — a interface some/aparece conforme a assinatura ativa.

| Plano | Posicionamento | Libera |
|-------|----------------|--------|
| **Essence** | O essencial para profissionalizar a agenda. | Site profissional, link de agenda 24h, painel de agenda, dashboard financeiro, fichas de anamnese. |
| **Pro** *(mais popular)* | Tudo do Essence **+ cobrança de sinal + combos + controle de estoque**. | Tudo do Essence, mais: cobrança de sinal, combos de serviços, controle de estoque. |
| **Elite** | Plataforma completa **+ atendente IA no WhatsApp**. | Tudo do Pro, mais: a **Assistente IA no WhatsApp**. |

**Recursos e onde ficam:**

| Recurso | Essence | Pro | Elite |
|---------|:---:|:---:|:---:|
| Site profissional (vitrine) | ✅ | ✅ | ✅ |
| Link de agenda 24h / agendamento online | ✅ | ✅ | ✅ |
| Painel de agenda | ✅ | ✅ | ✅ |
| Dashboard financeiro | ✅ | ✅ | ✅ |
| Fichas de anamnese | ✅ | ✅ | ✅ |
| Cobrança de sinal | — | ✅ | ✅ |
| Combos de serviços | — | ✅ | ✅ |
| Controle de estoque | — | ✅ | ✅ |
| Assistente IA no WhatsApp | — | — | ✅ |

A gestão de planos, features e preços é feita internamente pela plataforma; a profissional pode
**trocar de plano ou cancelar** a qualquer momento pelo próprio painel (ver **Assinatura & cobrança**).

---

## Identidade visual

### Marca da plataforma

- Estilo: clean, sofisticado, feminino, moderno, mobile-first.
- Paleta institucional roxo/rosé (principal `#602094`, secundária `#BD304F`), com apoio de rosa,
  lavanda, lilás e bordô.
- Tipografia: **Stoic** (headlines), **Montserrat** (corpo/UI), **Playfair Display** (momentos
  editoriais/premium).

### Vitrine personalizável por profissional

A vitrine de cada profissional é **customizável**: ela escolhe uma **paleta de cores** para o próprio
site, além de capa, avatar/logo, biografia, uma frase de destaque, saudação do topo editável, redes
sociais, formas de pagamento aceitas e imagem de fundo do login. Assim, cada vitrine tem a cara da
profissional mantendo a base de design da plataforma.

---

## Portal do Cliente (vitrine pública)

Área pública em `beautyclick.com/{slug}`. Navegação: **Início · Serviços · Combos · Portfólio** +
entrar/minha conta + botão flutuante de WhatsApp e rodapé "by BeautyClick".

| Tela | Descrição |
|------|-----------|
| **Início (vitrine)** | Página principal: capa, avatar/logo, nome, saudação, bio, frase, horário de funcionamento, endereço (com link para mapa), redes sociais, formas de pagamento e avaliações. É o cartão de visitas da profissional. |
| **Serviços** | Catálogo com todos os serviços: nome, descrição, duração, valor, foto e se exige sinal. |
| **Combos** | Pacotes de serviços com preço promocional, economia destacada e validade. A cliente pode adquirir/agendar a partir do combo. |
| **Portfólio** | Galeria de trabalhos, organizada por categoria e vinculada a serviços. |
| **Agendar** | Fluxo guiado de agendamento (ver abaixo). |
| **Minha conta / Meus agendamentos** | Área logada da cliente: dados pessoais, agendamentos futuros e histórico, detalhes de cada agendamento e **avaliação** de atendimentos concluídos. |
| **Detalhes do agendamento** | Serviço(s), data, horário, status, valor, sinal e endereço; ações permitidas conforme as regras da profissional. |
| **Ficha de anamnese** | Formulário público (link próprio por ficha) que a cliente preenche antes do procedimento. |

### Fluxo de agendamento

Fluxo em **3 etapas** com um passo a passo visual:

| Passo | Ação |
|-------|------|
| **1. Serviços** | A cliente seleciona um ou mais serviços (ou parte de um combo). A plataforma soma a duração total. |
| **2. Data e horário** | Escolhe data e horário **realmente disponíveis**, calculados a partir do Google Calendar da profissional (bloqueios, outros compromissos e duração somada dos serviços). |
| **3. Confirmação** | Identificação da cliente (login ou cadastro rápido com **verificação de telefone por código/OTP**), aplicação de **cupom** quando houver, e — se o serviço exigir sinal — **pagamento do sinal na hora** (Mercado Pago, via checkout embutido). Sem sinal, confirma direto. Ao final: resumo, confirmação e opção de adicionar o evento ao Google Calendar da própria cliente. |

Funcionalidades do cliente: ver informações e portfólio da profissional, navegar pelo catálogo e
combos, ver horários disponíveis em tempo real, agendar um ou vários serviços, pagar sinal online,
criar conta/entrar, gerenciar agendamentos, avaliar atendimentos e receber lembretes/confirmações.

---

## Portal do Profissional (`/admin`)

Área restrita para gerenciar o negócio. O menu se adapta ao plano (itens de sinal, combos, estoque e
IA aparecem só quando o plano libera).

| Seção | Descrição |
|-------|-----------|
| **Dashboard** | Visão do dia: saudação, faturamento (mês/semana/hoje), ticket médio, indicadores (ocupação, cancelamento, no-shows, conversão), gráfico de faturamento dos últimos 30 dias, agendamentos de hoje, **fechamento do dia** (revisar concluídos/faltas) e alertas de estoque. |
| **Agenda** | Calendário completo (dia/semana/mês). Criar, confirmar, cancelar, remarcar e **bloquear horários** (folga, viagem, compromisso). Agendamentos por origem (site, IA, manual), com destaque de **encaixe**. |
| **Serviços** | CRUD de serviços com categorias: nome, descrição, duração, valor, foto, ativo/inativo, **exigência e valor de sinal**, **FAQ do serviço**, **serviço de cross-sell** ("oferecer junto") e **ficha técnica** (insumos consumidos → CMV e margem). |
| **Combos** | Catálogo de pacotes + combos vendidos (ver módulo). |
| **Estoque** | Produtos, lotes, movimentações, custos e alertas (ver módulo). |
| **Anamnese** | Modelo de ficha, banco de perguntas e perguntas próprias (ver módulo). |
| **Portfólio** | Galeria de trabalhos publicada na vitrine. |
| **Clientes** | Base de clientes com histórico, dados de contato, estatísticas e observações; edição manual e ações de privacidade (anonimização). |
| **Assistente IA** | Central da IA (resultados, conversas, pendências e configuração) — só no plano Elite. Detalhe no briefing da IA. |
| **Marketing** | Aniversariantes e cupons (ver módulo). |
| **Financeiro** | Dashboard financeiro completo (ver módulo). |
| **Configurações** | Perfil/vitrine, preferências, plano e integrações (ver **Configurações**). |

Card fixo de **"Indique e Ganhe"** e **botão de contato/suporte por WhatsApp** ficam sempre à mão.

---

## Módulo Financeiro

Dashboard financeiro com métricas, filtros de período (hoje/semana/mês/ano/personalizado) e
exportação. Organizado em abas:

| Aba | Conteúdo |
|-----|----------|
| **Visão geral** | Faturamento do período, sinais, ticket médio e — quando o estoque está ativo — **CMV (custo dos insumos), compras, perdas e margem bruta**. |
| **Faturamento** | Detalhamento da receita realizada (serviços + sinais), lançamentos manuais de transações e comparativos. |
| **Previstos** | Receita projetada a partir dos agendamentos futuros confirmados. |
| **Agendamentos** | Confirmados, concluídos, cancelados, no-shows e taxa de cancelamento. |
| **Serviços** | Desempenho por serviço: mais/menos vendidos, faturamento e ticket médio por serviço. |
| **Clientes** | Novos, recorrentes e top gastadores; base de clientes. |
| **Relatórios** | Geração e **exportação (CSV)** de relatórios: financeiro mensal, agendamentos, clientes e — com estoque — relatórios de insumos/perdas. |

O módulo cruza automaticamente as baixas de estoque com a receita para mostrar **margem por serviço e
CMV** — algo que a profissional normalmente não teria.

---

## Módulo de Estoque *(Pro/Elite)*

Controle de insumos com custo real e baixa automática. Abas: **Alertas · Produtos · Movimentações ·
Inteligência · Configurações**.

- **Produtos**: unidade base de consumo (ml/g/unidade), apresentação de compra (ex.: 1 frasco = X ml),
  dose opcional, estoque mínimo, controle de validade por **lote (FEFO)**, custo médio e categoria.
- **Compras/entradas**: quantidade, total pago (calcula custo unitário), lote/validade e fornecedor.
- **Contagem de inventário** e **registro de perdas** (com motivo).
- **Ficha técnica** (por serviço): quais produtos e quanto cada serviço consome → ao **concluir um
  agendamento, o estoque baixa automaticamente** e alimenta CMV/margem no Financeiro.
- **Alertas** de estoque baixo e vencimento próximo (com contador no menu).
- **Configurações**: ligar/desligar a baixa automática, método de custo (**média ponderada** ou
  **último preço**), antecedência de aviso de vencimento e categorias de produtos.

---

## Módulo de Combos *(Pro/Elite)*

Pacotes de serviços vendidos com preço promocional. Abas: **Catálogo · Vendidos**.

- **Catálogo**: cria/edita combos com serviços incluídos (e quantidades), preço, **economia
  destacada**, validade em dias, **sinal opcional para o 1º agendamento** (via Mercado Pago),
  políticas de cancelamento/reagendamento, limite de uso e ativo/inativo.
- **Vendidos**: acompanha cada combo comprado por cliente — **saldo por serviço** (usados/total),
  validade, status (ativo/finalizado/expirado/cancelado/aguardando pagamento), histórico de uso e
  cancelamento. Permite **registrar venda manual**.
- **Combos vencidos expiram automaticamente** (rotina diária).
- A cliente pode adquirir/usar combos pela vitrine (**Combos** e **Meus combos**).

---

## Módulo de Anamnese *(todos os planos)*

Fichas de anamnese que a cliente preenche antes do procedimento. Abas: **Meu modelo · Banco de
perguntas · Perguntas próprias · Configurações**.

- **Banco de perguntas** pronto (amplo) e **templates base por área** de atuação, para começar rápido.
- A profissional monta o **seu modelo** (adiciona/remove/reordena perguntas) e cria **perguntas
  próprias** (vários tipos de campo).
- As fichas têm **política de retenção** e podem ser **excluídas a pedido** (ver Privacidade & LGPD).
- A cliente preenche por um **link público** antes do atendimento; as respostas ficam **guardadas com
  segurança (criptografadas)** e acessíveis à profissional.

---

## Módulo de Marketing / Retenção *(todos os planos)*

Abas: **Aniversariantes · Cupons**.

- **Aniversariantes**: lista clientes que fazem aniversário no mês/dia, com botão de **mensagem pronta
  no WhatsApp** já com o desconto configurado.
- **Cupons**: cria e gerencia cupons de desconto para as clientes (percentual, validade, etc.),
  incluindo o **cupom de aniversário** que a IA usa nos disparos. (Cupons resgatáveis no fluxo de
  agendamento do site.)

---

## Avaliações / Reputação *(todos os planos)*

Após um atendimento concluído, a cliente pode deixar uma **avaliação (nota + comentário)** pela sua
conta. A profissional vê **média, total e a lista** de avaliações na seção **Avaliações**, e a nota
agregada aparece na vitrine — construindo prova social.

---

## Cadastro & Onboarding

- **Cadastro** da profissional (com suporte a **cupom de indicação** na URL) e login por e-mail/senha,
  com recuperação de senha.
- **Onboarding guiado (wizard)** após o cadastro, com tela de boas-vindas e um hub de etapas:
  1. **Meus detalhes** — perfil, contato, horários e pagamento.
  2. **Conectar Google Calendar** — agenda oficial; sem isso, clientes não conseguem agendar.
  3. **Primeiro serviço** — é preciso ao menos 1 serviço para publicar a agenda.
  4. **Pagamentos (opcional)** — conectar o Mercado Pago para cobrar sinal.
  5. **Assistente IA (Elite)** — nome, tom de voz e informações da IA.
- Enquanto o onboarding não é concluído, partes do painel ficam bloqueadas. Tudo pode ser editado
  depois em Configurações.

---

## Configurações

Hub com 4 módulos:

- **Informações e perfil (vitrine)**: capa, avatar/logo, bio, frase, endereço, horários, redes,
  formas de pagamento, **paleta de cores**, saudação do topo e link público — tudo com **preview em
  tempo real**.
- **Preferências**:
  - **Dados pessoais privados** (nascimento, CPF/CNPJ, endereço pessoal) — usados só para faturamento/
    nota fiscal, nunca aparecem para as clientes.
  - **Política de sinal**: exigir sinal por padrão, valor padrão, **janela de cancelamento gratuito**
    e **de remarcação gratuita** (em horas), sinal **reembolsável** no cancelamento e **reaproveitável**
    na remarcação. Fora das janelas, a cliente perde o sinal.
  - **Controle de estoque** (liga/desliga a baixa automática) e **atalhos de integrações**.
  - **Alterar senha**.
- **Assistente IA**: leva à Central da IA (Elite).
- **Meu plano**: ver **Assinatura & cobrança**.

---

## Assinatura & cobrança (SaaS)

- A assinatura da profissional é processada via **Stripe**: **checkout**, **portal de cobrança**,
  **troca de plano** e **cancelamento** (programado para o fim do ciclo, com opção de **reativar**).
  Status possíveis: ativa, em teste, pagamento pendente, cancelada, etc.
- Enquanto não há assinatura ativa, o acesso ao painel é bloqueado (tela de pagamento recusado /
  assinar).
- **Importante não confundir:** a **assinatura da profissional** (o que ela paga pela plataforma) é
  via **Stripe**; o **sinal que a cliente paga** no agendamento é via **Mercado Pago**, direto na
  conta da profissional.

### Indique e Ganhe (indicações)

Cada profissional tem um **link e cupom de indicação**. A cada nova profissional que assina pelo link,
quem indicou ganha **desconto na mensalidade do mês seguinte** (20% no Elite, 50% nos demais planos),
acumulando um mês de desconto por indicação. Quem é indicada também ganha **5% no primeiro mês**.

---

## Integrações

| Integração | Uso |
|------------|-----|
| **Google Calendar** | Agenda oficial da profissional. Sincronização bidirecional: bloqueios e compromissos no Google tornam horários indisponíveis; agendamentos criados na plataforma (site, painel e IA) entram no calendário. Base do cálculo de horários livres. |
| **Mercado Pago** | Recebe o **sinal** das clientes direto na conta da profissional (checkout embutido no agendamento e sinal de combo). Confirmação de pagamento por webhook, que confirma o agendamento. |
| **Stripe** | **Assinatura da plataforma** pela profissional (cobrança recorrente, portal, troca/cancelamento). |
| **WhatsApp / IA** | Atendente virtual no WhatsApp (plano Elite). Ver `BeautyClickIA-Briefing-v2.md`. |
| **Notificações** | Lembretes e confirmações por WhatsApp (via IA) e mensagens de marketing prontas. |

---

## Landing de marketing (`/home`)

Página pública de venda da plataforma: hero, benefícios, features, seção da secretária virtual (IA),
seção do financeiro, **planos**, FAQ, CTA e rodapé. Inclui um **modal de lista de espera** (nome,
WhatsApp e plano de interesse) para captar interessadas antes/na largada, e botão de contato por
WhatsApp.

---

## Privacidade & LGPD

- **Telefone obrigatório no cadastro** da cliente — inclusive no login por Google (com verificação por
  código/OTP no agendamento).
- **Anonimização de cliente (a pedido/LGPD)**: botão no detalhe da cliente que anonimiza os dados
  pessoais preservando o histórico agregado do negócio.
- **Anamnese**: política de **retenção** e **exclusão a pedido** das fichas e respostas (respostas
  guardadas criptografadas).
- Login do cliente por **e-mail/senha e Google** (o login por Facebook foi removido).

---

## Observações

- Este documento reflete o **estado funcional atual** da plataforma; fluxos e telas podem ser
  ajustados durante desenvolvimento e testes conforme necessidade técnica e feedback das
  profissionais.
- Priorize **mobile-first** — a maioria das clientes agenda pelo celular.
- O fluxo de agendamento e o dashboard financeiro são o coração do produto.
- Preços dos planos não estão fixados aqui de propósito (definição comercial à parte).
