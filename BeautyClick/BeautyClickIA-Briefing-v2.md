# BeautyClick IA — Briefing Funcional v2 (Visão & Direção)

> **Escopo deste documento:** direção de produto da IA de atendimento — o *quê* e o *porquê*, e o que
> a IA já faz. Itens em desenvolvimento/em teste estão descritos como prontos.
> **Não** é o estado técnico de implementação. Para o status detalhado (o que está pronto, pendente,
> pausado, com nomes de workflows/RPCs), ver `BeautyClickIA-Status.md`.
> **Atualizado:** 2026-08-05.

---

## O que é

A **BeautyClick IA** é uma atendente virtual de WhatsApp para profissionais de beleza, incluída no
plano **Elite**. Ela conversa com as clientes de forma humanizada, 24 horas por dia — tira dúvidas,
apresenta serviços, consulta horários, agenda, remarca, cancela, faz encaixe, cobra sinal, envia
lembretes, reativa clientes, resume o dia para a profissional e transfere para atendimento humano
quando necessário. A proposta é que a cliente sinta que fala com uma atendente real: linguagem
natural, educada, simpática e alinhada ao estilo da profissional.

A IA é vendida e integrada junto com a plataforma BeautyClick. Comunicação em **pt-BR / pt-PT**.

## Contexto atual

- **WhatsApp** via **WAME API**; IA orquestrada no **n8n** com **LangChain Agent + Google Gemini**.
  Entende **texto, áudios e imagens/prints**.
- **Pagamento de sinal** via **MercadoPago**.
- **Agenda**: a integração com o Google Calendar fica na **plataforma**; a IA a aciona. Reservas
  feitas/canceladas/remarcadas pela IA também **sincronizam com o Google Calendar** da profissional.
- Configurada **por profissional** (cada uma tem seu perfil de IA e seus dados).
- Conversas **são gravadas** (isoladas por profissional, retenção de **120 dias**); sem aviso de
  privacidade dentro da conversa.

---

## 1. Objetivo da IA

Ser uma atendente virtual humanizada no WhatsApp, disponível 24h, capaz de conversar com clientes,
tirar dúvidas, oferecer serviços, consultar horários, realizar agendamentos, cobrar sinal, reativar
clientes e auxiliar em pedidos de encaixe — sempre com linguagem natural e no tom da profissional.

---

## 2. Principais funções da IA

### 2.1 Atendimento inicial
- Cumprimentar a cliente de forma humanizada.
- Identificar a intenção da cliente.
- Oferecer os caminhos: ver serviços pelo site/link da profissional, agendar direto pelo WhatsApp,
  ou tirar dúvidas sobre serviços, valores, horários ou endereço.

### 2.2 Entendimento de mensagens
A IA entende: texto, **áudios**, **imagens** e **prints**, mensagens incompletas ou informais, erros
de digitação, gírias e a linguagem comum de WhatsApp. Áudios são transcritos e imagens são
interpretadas antes de a IA responder.

Exemplos: *"tem horário amanhã?"*, *"quanto tá a unha em gel?"*, *"quero fazer igual essa foto"*,
*"vc tem encaixe hj?"*, *"qual valor desse procedimento?"*.

### 2.3 Consulta de serviços
Acessa os serviços cadastrados pela profissional e responde: nome, descrição, duração, valor, se
exige sinal (e o valor do sinal) e orientações específicas. Também **sugere serviços** com base no
pedido da cliente.

> Exemplo — Cliente: *"Quero fazer cílios, mas não sei qual."*
> IA: *"Temos algumas opções. Posso te explicar a diferença entre volume brasileiro, volume russo e
> fio a fio para você escolher o ideal."*

### 2.4 Agendamento via WhatsApp
Conduz o agendamento completo dentro do WhatsApp:
1. Perguntar qual serviço a cliente deseja (um ou mais).
2. Consultar a duração total.
3. Consultar horários disponíveis na agenda da profissional.
4. Mostrar opções de data/horário e aguardar a escolha.
5. Coletar/reaproveitar dados da cliente (nome, telefone, e-mail se necessário).
6. Quando fizer sentido, **oferecer um serviço complementar (cross-sell)** — fechando tudo num único
   agendamento, no mesmo horário, somando as durações.
7. Confirmar o resumo do agendamento.
8. Se houver sinal, enviar link de pagamento; se não houver, confirmar direto.
9. Criar o evento na agenda da profissional.
10. Enviar a mensagem final de confirmação.

### 2.5 Integração com a agenda (Google Calendar)
A IA consulta horários e cria/atualiza eventos na agenda da profissional. **A integração com o Google
Calendar é feita pela plataforma BeautyClick** — a IA aciona os endpoints da plataforma, que leem e
escrevem na agenda, e a reserva feita pela IA **sincroniza com o Google Calendar** (criação,
remarcação e cancelamento). Comportamento esperado:
- Buscar horários disponíveis, considerando bloqueios, outros compromissos e a duração do serviço.
- Criar evento após a confirmação; atualizar em remarcação; cancelar quando permitido.
- Evitar conflitos de horário.

O evento contém: nome da cliente, telefone, serviço, valor, status do pagamento/sinal, observações e
o canal de origem (**WhatsApp IA**).

### 2.6 Pagamento de sinal
Quando o serviço exige sinal, a IA informa o valor, explica que o horário só é confirmado após o
pagamento, **gera e envia o link de pagamento (MercadoPago)**, aguarda a confirmação, confirma o
agendamento após aprovação e avisa a cliente e a profissional.

> Exemplo: *"Esse serviço exige um sinal de R$ 30,00 para reservar o horário. Vou te enviar o link de
> pagamento. Assim que o pagamento for confirmado, seu horário fica reservado."*

Quando o pagamento é confirmado, a cliente recebe o aviso de **"Pagamento confirmado ✅"**.

### 2.7 Pedido de encaixe
Quando a cliente pede encaixe e não há horário disponível, a IA:
1. Coleta serviço desejado, data e horário/período desejado (e urgência, se houver).
2. Envia uma mensagem para a **profissional** perguntando se aceita o encaixe.
3. A profissional **responde citando** (reply-quote) o pedido — aceitando, recusando ou sugerindo
   outro horário.
4. A IA interpreta a resposta e **retorna para a cliente**. Se aceito, agenda o encaixe (fura a grade)
   e o agendamento aparece na agenda com destaque de **"encaixe"**.

> Exemplo (para a profissional): *"Pedido de encaixe: Cliente Maria · Serviço: Manicure e pedicure ·
> Data: hoje · Período: fim da tarde. Você aceita esse encaixe?"*

---

## 3. Remarcação e cancelamento

A cliente pode, pela IA: remarcar, cancelar, confirmar presença e consultar dados do agendamento.
A IA respeita as regras da profissional: prazo mínimo para cancelamento, política de perda/reembolso
do sinal, reaproveitamento do sinal na remarcação e necessidade de aprovação manual. Cancelamentos e
estornos do sinal seguem as janelas configuradas.

---

## 4. Lembretes automáticos

A IA envia lembretes automáticos pelo WhatsApp:
- **24 horas antes** ("amanhã").
- **3 horas antes** do agendamento.

A cliente pode responder ao lembrete em texto livre (*confirmo*, *preciso remarcar* ou *quero
cancelar*) e a IA interpreta.

> Exemplo: *"Oi, Maria! Passando para lembrar do seu horário amanhã às 14h para alongamento de unhas.
> Podemos confirmar sua presença?"*

---

## 5. Captação e reativação — follow-ups proativos

A IA envia mensagens proativas para trazer a cliente de volta e recuperar conversões. Cada follow-up
é um "tipo", com mensagem própria. Todos respeitam **opt-out por cliente** e uma **janela mínima**
entre disparos (dedupe/anti-spam), para não spammar.

Catálogo de follow-ups **ativos**:

- **Manutenção** — X dias após o serviço (ciclo de cada serviço), para reagendar a próxima sessão.
- **Inativa** — cliente sumida há ~90 dias recebe um convite para voltar.
- **Primeira visita** — quem veio uma única vez e não voltou (~20–30 dias), para virar recorrente.
- **Aniversário** 🎂 — mensagem no dia com um **cupom de desconto** (a IA envia o código; a cliente
  resgata no site).
- **No-show** — quem faltou recebe uma mensagem empática para remarcar.
- **Sinal pendente** — gerou o link de pagamento mas não pagou; lembrete de que o horário ainda não
  está reservado.
- **Agendamento abandonado** — conversa com intenção clara que morreu sem agendar; empurrão para
  concluir.
- **Cross-sell** — sugestão do serviço que costuma vir depois do que a cliente fez.

> Exemplo: *"Oi, Ana! Já faz 30 dias desde sua última manutenção. Quer ver os horários disponíveis
> desta semana?"*

**Direção futura (ainda não ativa):**
- **Ritmo individual** — detectar o intervalo médio da própria cliente (ex.: vem a cada 25 dias) e
  cutucar quando ela passa do ritmo dela — reativação mais inteligente que o prazo fixo.
- **Pós-atendimento** — ver seção 6.

---

## 6. Pós-atendimento *(direção futura)*

Após o atendimento, a IA poderá enviar: agradecimento, pedido de avaliação, link para reagendamento,
sugestão de retorno e oferta de outro serviço. Fecha o funil de retenção logo após o serviço.

> Exemplo: *"Obrigada pela visita! Esperamos que tenha amado o resultado. Quer deixar uma avaliação ou
> já agendar sua próxima manutenção?"*

---

## 7. Memória de longo prazo por cliente

A IA lembra observações duráveis entre conversas. Ela guarda notas sobre a cliente (preferências,
alergias, restrições — nada efêmero ou sensível) e reinjeta essas informações nas conversas
seguintes, dando consistência real ao reconhecimento de clientes recorrentes.

---

## 8. Reconhecimento de clientes recorrentes

A IA identifica quando a cliente já tem cadastro/histórico e reaproveita dados para tornar a conversa
mais natural — evita pedir as mesmas informações de novo. Reaproveita, quando possível: nome,
telefone, histórico de serviços, preferências e últimos atendimentos (apoiado pela memória da seção 7).

> Exemplo — em vez de *"Qual seu nome?"*: *"Oi Maria! 😊 Que bom falar com você novamente. Gostaria de
> agendar outro horário?"*

---

## 9. Resumo diário para a profissional

Uma vez por dia, no horário configurado pela profissional, a IA envia um **resumo do dia** pelo
WhatsApp com: os agendamentos de **amanhã** (serviço, hora, cliente, valor, situação do sinal, combo)
e os **novos, cancelados e remarcados** do dia. Dia sem movimento não gera envio. O resumo pode ser
ligado/desligado e ter o horário ajustado.

---

## 10. Aviso de cancelamento em tempo real

Quando um agendamento **de hoje** é cancelado (pela cliente, pela IA, pelo site ou pelo painel), a IA
avisa a profissional **na hora** pelo WhatsApp, já sugerindo **candidatas a encaixe** para aquele
horário que abriu.

---

## 11. Personalização por profissional

Cada profissional configura o comportamento da IA (no onboarding e na Central da IA):
- **Nome da atendente** e **tom de voz** (formal, simpático, descontraído ou premium).
- **Mensagem de saudação**.
- Se a IA deve **enviar o link do site** da profissional.
- **Instruções extras** específicas do estúdio.
- **Telefone para transbordo humano** (para onde a IA avisa/transfere).
- **Resumo diário**: liga/desliga e horário.
- Horário de funcionamento, serviços, políticas de cancelamento/remarcação e valor de sinal vêm do
  restante da plataforma.

---

## 12. Regras importantes

A IA deve:
- **Não inventar horários** nem confirmar agendamento sem disponibilidade real.
- **Não confirmar horário com sinal pendente.**
- Não passar informações que não estejam cadastradas.
- Chamar a profissional quando não souber responder.
- Registrar o histórico da conversa.
- Avisar a profissional em casos sensíveis ou complexos.
- Ter sempre a opção de **atendimento humano**.

---

## 13. Quando a IA chama a profissional

Transferir ou notificar a profissional quando: a cliente reclamar; o caso for muito específico; a
cliente pedir encaixe; houver falha no pagamento; houver conflito de agenda; ou a IA não entender a
solicitação.

---

## 14. Central da IA (painel da profissional)

No painel da plataforma, a profissional acompanha e controla a IA numa central com 4 áreas:

- **Resultados** — métricas da IA (ver seção 15) e follow-ups por tipo.
- **Conversas** — lista de conversas recentes com **transcrição**, busca por número/nome, filtros
  (todas / pausadas / pediram humano), caixa de prioridade para quem pediu atendimento humano, e
  **opt-out de follow-up** por cliente.
- **Pendências** — pedidos de **encaixe** pendentes, **sinais** pendentes e confirmados, e clientes
  que **não finalizaram** o agendamento.
- **Configuração** — todos os campos de personalização da seção 11.

Controles de operação:
- **Liga/desliga global da IA** — interruptor mestre que silencia a IA quando desligada.
- **Pausar/reativar por conversa** — pausa a IA numa conversa específica (ou já deixa pausado um
  número que ainda não conversou), sem afetar as demais; útil quando a profissional quer assumir.

---

## 15. Métricas da IA

Indicadores que a IA registra e mostra no painel:
- Quantidade de atendimentos e de agendamentos feitos pela IA.
- Taxa de conversão de conversa → agendamento.
- Receita gerada pela IA e sinais pagos via WhatsApp.
- Faltas/cancelamentos e clientes que desistiram.
- Follow-ups enviados por tipo.

---

## 16. Confiabilidade / operação

Se algo falhar no atendimento da IA, a **dona da plataforma é avisada no WhatsApp** (com limite de
frequência para não virar spam) e todos os erros ficam registrados. Isso vale tanto para falhas de
execução quanto para ferramentas que não concluíram uma ação — para nada passar despercebido.

---

## 17. Fluxo ideal resumido

Cliente chama no WhatsApp → IA responde humanizada → IA entende a intenção → oferece link do site ou
agenda pelo WhatsApp → cliente escolhe serviço → IA consulta horários → cliente escolhe horário → IA
coleta/reaproveita dados → (quando faz sentido) oferece complemento → verifica sinal → (se houver)
envia link de pagamento e confirma após pago; (se não houver) confirma direto → IA cria o evento na
agenda (e sincroniza no Google Calendar) → cliente recebe confirmação → profissional recebe a
notificação.

---

## 18. Direção futura — uso do histórico de conversas

Ideias para evoluir a IA a partir do histórico que já é gravado (ainda não implementadas):

- **Mineração de dúvidas** — o que gera transbordo vira conteúdo de FAQ dos serviços e instruções da
  IA; a IA melhora sozinha (e é argumento de venda).
- **Demanda reprimida** — detectar serviços pedidos e não cadastrados, e horários que sempre lotam.
- **QA do agente** — varrer conversas em busca de erros (ex.: confirmou sem sinal, citou preço que não
  bate com o cadastro).

---

## Importante

Os exemplos deste documento são referências para ilustrar o comportamento esperado da IA. Durante o
desenvolvimento e os testes, fluxos, mensagens, integrações e funcionalidades podem ser ajustados
conforme necessidades técnicas, experiência do usuário e feedback das profissionais. O objetivo é
definir a **direção** do produto e o que ele faz, não engessar a implementação.
