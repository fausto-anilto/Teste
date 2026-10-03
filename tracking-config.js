/* Vitória Clima — configuração de rastreamento
   ---------------------------------------------------------------
   Este é o ÚNICO arquivo que você edita para ligar o rastreamento.
   Deixe '' (vazio) para manter desligado: com tudo vazio o site não
   carrega nenhum script de terceiros, não grava nada e não altera os links.
   Passo a passo completo: docs/RASTREAMENTO.md
*/
window.VC_TRACKING = {

  /* ---- 1) Caminho recomendado: Google Tag Manager --------------------
     Com GTM_ID preenchido, o site só envia eventos para o dataLayer e você
     configura GA4, Google Ads e Meta dentro do GTM. Nesse caso deixe
     GA4_ID, GADS_ID e META_PIXEL_ID vazios (senão contaria em dobro). */
  GTM_ID: '',                // ex.: 'GTM-XXXXXXX'

  /* ---- 2) Caminho direto (sem GTM) ---------------------------------- */
  GA4_ID: '',                // ex.: 'G-XXXXXXXXXX'
  GADS_ID: '',               // ex.: 'AW-123456789'
  GADS_LABELS: {             // conversões do Google Ads: 'AW-123456789/AbC-D_efG'
    whatsapp: '',
    phone: '',
    map: ''
  },
  META_PIXEL_ID: '',         // ex.: '123456789012345'
  META_EVENTS: {             // evento padrão da Meta disparado em cada tipo de clique
    whatsapp: 'Lead',
    phone: 'Contact',
    email: 'Contact',
    map: 'FindLocation'
  },

  /* ---- 3) Coletor próprio (Planilha Google via Apps Script) -----------
     Guarda cada clique com UTM, gclid, fbclid e o código de referência.
     É a base das conversões offline. Veja docs/coletor-apps-script.gs */
  COLLECT_URL: '',           // URL do app da web publicado no Apps Script
  COLLECT_TOKEN: '',         // mesmo valor de TOKEN no script (evita lixo)

  /* ---- 4) WhatsApp ----------------------------------------------------
     Quando o rastreamento está ligado, acrescenta ao fim da mensagem
     pronta um código curto, ex.: "(ref. VC-7K3Q9)". É ele que liga a
     conversa do WhatsApp ao clique no anúncio. Use false para desativar. */
  WA_REF: true,
  WA_REF_PREFIX: 'VC',

  /* ---- 5) LGPD / consentimento ----------------------------------------
     true  = mostra um aviso de cookies (Aceitar/Recusar) e só grava
             identificadores e dispara pixels depois do "Aceitar".
     false = só use se a base legal estiver definida com o jurídico. */
  REQUIRE_CONSENT: true,
  PRIVACY_URL: '',           // ex.: 'privacidade.html' (página de política de privacidade)

  /* ---- 6) Outros -------------------------------------------------------- */
  ATTR_DAYS: 90,             // por quantos dias lembrar a origem do visitante
  DEBUG: false               // true (ou ?tracking_debug=1 na URL) mostra os eventos no console
};
