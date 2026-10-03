# Rastreamento do site Vitória Clima — guia de ativação

O site já vem com o caminho pronto. **Enquanto `tracking-config.js` estiver com os campos vazios, o site não carrega nada de terceiros, não grava nada no navegador e não altera nenhum link.** Para ligar, preencha o arquivo e publique.

## 1. O que já é rastreado (sem mexer no HTML)

Todo link de **WhatsApp, telefone, mapa, e-mail, Instagram e Facebook** do site (botões, cartões, menu, rodapé, botão fixo) é detectado automaticamente pelo `tracking.js`. Cada clique gera um evento com:

| Campo | O que é | Exemplo |
|---|---|---|
| `channel` | tipo do clique | `whatsapp`, `phone`, `map`, `email`, `social` |
| `location` | onde o botão está | `botao_fixo`, `cabecalho`, `home_hero`, `home_intencoes`, `hero_lateral`, `artigo_lateral`, `artigo_meio`, `artigo_corpo`, `faixa_final`, `rodape`, `contato`, ou `secao_<título da seção>` |
| `label` | texto do botão (ou título do cartão) | `Pedir orçamento` |
| `page`, `page_type` | página e tipo | `instalacao-ar-condicionado-vitoria.html`, `artigo` |
| `device` | aparelho | `mobile`, `desktop` |
| `ref` | código do clique no WhatsApp | `VC-7K3Q9` |
| `utm_*` | origem do último acesso não direto | `google / cpc / campanha` |
| `first_*` | origem do primeiro acesso | |
| `gclid`, `gbraid`, `wbraid`, `fbclid`, `fbc`, `fbp`, `msclkid` | identificadores de anúncio (guardados por 90 dias) | |

Eventos enviados: `click_whatsapp`, `click_phone`, `click_map`, `click_email`, `click_social`.
Um botão novo que você criar no futuro já é rastreado sozinho. Para dar um nome próprio, use `data-loc="nome"` no bloco ou `data-label="nome"` no link.

Para eventos de outra natureza (formulário, por exemplo): `VCTrack.track('envio_formulario', { label: 'contato' }, 'lead')`.

## 2. Ativar em 3 caminhos (escolha um para as tags)

### Caminho A (recomendado): Google Tag Manager
1. Crie o contêiner em tagmanager.google.com e copie o ID `GTM-XXXXXXX` para `GTM_ID`.
2. Deixe `GA4_ID`, `GADS_ID` e `META_PIXEL_ID` **vazios** (senão conta em dobro).
3. No GTM crie acionadores do tipo *Evento personalizado* com os nomes `click_whatsapp`, `click_phone`, `click_map`.
4. Crie as tags (GA4, conversão do Google Ads, Pixel da Meta) e ligue cada uma ao acionador. Variáveis do dataLayer disponíveis: `channel`, `location`, `label`, `ref`, `utm_source`, `utm_medium`, `utm_campaign`, `gclid`, `fbc`, etc.
5. Use o **Modo de visualização** do GTM para conferir antes de publicar.

### Caminho B: direto, sem GTM
Preencha `GA4_ID`, `GADS_ID` (+ `GADS_LABELS` com o `send_to` completo de cada conversão, ex.: `AW-123456789/AbC-D_efG`) e `META_PIXEL_ID`. Os eventos da Meta saem conforme `META_EVENTS` (padrão: WhatsApp = `Lead`, telefone = `Contact`, mapa = `FindLocation`) e já levam `eventID` igual ao `ref`, para deduplicar com a API de Conversões no futuro.

### Caminho C: só o coletor próprio
Preencha apenas `COLLECT_URL` e `COLLECT_TOKEN` (seção 4). Dá a base das conversões offline sem nenhuma tag de terceiros.

No GA4, marque `click_whatsapp` e `click_phone` como **eventos principais** (antes "conversões").

## 3. UTM: padrão para todos os links que levam ao site

Sempre: `utm_source`, `utm_medium`, `utm_campaign`. Em minúsculas, sem acento, sem espaço.

| Origem | Modelo |
|---|---|
| Google Ads (pesquisa) | `?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={creative}` (ative também o **Etiquetamento automático** para o `gclid`) |
| Meta Ads | `?utm_source=facebook&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}` |
| Perfil da empresa no Google | `?utm_source=google&utm_medium=organic&utm_campaign=perfil_empresa` |
| Bio do Instagram | `?utm_source=instagram&utm_medium=social&utm_campaign=bio` |
| Stories / posts | `?utm_source=instagram&utm_medium=social&utm_campaign=<nome_do_post>` |
| QR Code (balcão, cartão) | `?utm_source=qrcode&utm_medium=offline&utm_campaign=balcao` |
| Assinatura de e-mail / WhatsApp Business | `?utm_source=whatsapp&utm_medium=mensagem&utm_campaign=<nome>` |

Sem UTM, o site ainda classifica pelo *referrer*: busca orgânica, rede social, indicação ou direto.

## 4. Conversões offline (o caminho WhatsApp → agendamento → Google Ads / Meta)

O problema: a conversa acontece dentro do WhatsApp, fora do site. A solução:

1. **No clique**, o site acrescenta ao fim da mensagem pronta um código curto, por exemplo `(ref. VC-7K3Q9)`, e guarda a origem do visitante (UTM + gclid/fbclid) na **Planilha Google** (coletor).
2. **Quando o tutor manda a mensagem**, a recepção vê o `ref` na primeira linha. Basta procurar esse código na aba *Leads*.
3. **Na planilha**, preencha `status` (Conversando, Visita agendada, Serviço fechado, Perdido), `telefone_cliente`, `valor` e `data_conversao` quando houver.
4. **Toda semana**, menu *Vitória Clima > Exportar conversões — Google Ads* e *Exportar eventos — Meta*. Baixe a aba gerada como CSV e importe:
   - **Google Ads**: Metas > Conversões > Uploads. Crie antes uma conversão do tipo "Importar" > "Cliques" com o mesmo nome que está em `CONVERSOES` no script. Só entram linhas com `gclid`; as de iPhone (`gbraid`/`wbraid`) saem em aba separada, com outro modelo.
   - **Meta**: Gerenciador de Eventos (ou API de Conversões). O telefone sai normalizado e em SHA-256. **Confirme o modelo atual de colunas** na Meta antes de subir, pois muda com frequência.

Instalação do coletor (uma vez, 10 minutos): siga o cabeçalho de `docs/coletor-apps-script.gs`. Depois copie a URL do app da web em `COLLECT_URL` e o `TOKEN` em `COLLECT_TOKEN`.

Se não quiser o código na mensagem: `WA_REF: false`. Sem ele, o coletor ainda registra o clique, mas fica difícil ligar a conversa ao clique.

## 5. LGPD: antes de ligar qualquer pixel

- Com `REQUIRE_CONSENT: true` (padrão), aparece um aviso com **Aceitar / Recusar**. Só depois do "Aceitar" o site grava identificadores, dispara o Pixel da Meta e envia ao coletor. O Google recebe o *Consent Mode v2* (negado até aceitar). Um link "Preferências de cookies" aparece no rodapé para mudar de ideia.
- **Falta criar a página de política de privacidade** (`privacidade.html`) e preencher `PRIVACY_URL`. O texto precisa de revisão jurídica: ele deve citar os pixels usados, a finalidade e como pedir exclusão de dados.
- Cuidado com a planilha: ela passa a guardar telefone de tutores. Restrinja o acesso e evite compartilhar com pessoas de fora.

## 6. Como testar

1. Abra o site com `?tracking_debug=1` no fim do endereço. Cada evento aparece no console do navegador (F12) com o prefixo `[VC]`.
2. **GTM**: Modo de visualização. **GA4**: Admin > DebugView. **Meta**: extensão *Meta Pixel Helper*. **Google Ads**: extensão *Tag Assistant*.
3. Clique num botão de WhatsApp com `?utm_source=teste&utm_medium=teste&utm_campaign=teste&gclid=TESTE123` e confira se a mensagem do WhatsApp chega com `(ref. ...)` e se a linha aparece na planilha.
4. Teste com o aviso de cookies em **Recusar**: nada deve ser gravado nem enviado.

## 7. Arquivos

| Arquivo | Para quê |
|---|---|
| `tracking-config.js` | IDs e opções. O único que você edita. |
| `tracking.js` | lógica (cliques, origem, consentimento, envio). |
| `docs/coletor-apps-script.gs` | coletor e exportações (vai no Google Apps Script, não no site). |
| `docs/RASTREAMENTO.md` | este guia. |

A pasta `docs/` fica bloqueada para robôs de busca, mas não é secreta: não coloque senhas nem chaves nela.
