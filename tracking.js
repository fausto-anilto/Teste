/* Vitória Clima — rastreamento pré-pronto (sem dependências).
   Configuração: tracking-config.js · Guia: docs/RASTREAMENTO.md
   Com tudo vazio na configuração, este arquivo não faz nada no site. */
(function () {
  'use strict';
  var w = window, d = document;
  var C = w.VC_TRACKING || {};
  var DEBUG = !!C.DEBUG || /[?&]tracking_debug=1/.test(location.search);
  var HAS_TAGS = !!(C.GTM_ID || C.GA4_ID || C.GADS_ID || C.META_PIXEL_ID);
  var ACTIVE = HAS_TAGS || !!C.COLLECT_URL;
  var NEEDS_CONSENT = ACTIVE && C.REQUIRE_CONSENT !== false;
  var KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'gbraid', 'wbraid', 'fbclid', 'msclkid', 'ttclid'];
  var CHANNELS = { whatsapp: 1, phone: 1, map: 1, email: 1, social: 1 };

  function log() { if (DEBUG && w.console) { console.log.apply(console, ['[VC]'].concat([].slice.call(arguments))); } }

  /* ---------- armazenamento (localStorage, com proteção) ---------- */
  function get(k) { try { return JSON.parse(localStorage.getItem('vc_' + k)); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem('vc_' + k, JSON.stringify(v)); } catch (e) { /* navegação privada */ } }
  function cookie(n) { var m = d.cookie.match(new RegExp('(?:^|; )' + n + '=([^;]*)')); return m ? decodeURIComponent(m[1]) : ''; }

  function consentState() { return get('consent'); }
  function granted() { return !NEEDS_CONSENT || consentState() === 'granted'; }
  function fresh(t) {
    if (!t || !t.ts) { return null; }
    var max = (C.ATTR_DAYS || 90) * 864e5;
    return (Date.now() - t.ts) <= max ? t : null;
  }

  /* ---------- origem do visitante: UTM, click IDs e referência ---------- */
  function queryParams() {
    var out = {}, s = location.search.replace(/^\?/, '');
    if (!s) { return out; }
    s.split('&').forEach(function (p) {
      var i = p.indexOf('='), k, v;
      if (i < 0) { return; }
      try { k = decodeURIComponent(p.slice(0, i)); v = decodeURIComponent(p.slice(i + 1).replace(/\+/g, ' ')); } catch (e) { return; }
      if (KEYS.indexOf(k) > -1 && v) { out[k] = v.slice(0, 200); }
    });
    return out;
  }
  function fromReferrer() {
    var r = d.referrer, h, m;
    if (!r) { return { source: '(direct)', medium: '(none)' }; }
    try { h = new URL(r).hostname.replace(/^www\./, ''); } catch (e) { return { source: '(direct)', medium: '(none)' }; }
    if (!h || h === location.hostname.replace(/^www\./, '')) { return null; }
    m = h.match(/(google|bing|yahoo|duckduckgo|ecosia|brave)\./);
    if (m) { return { source: m[1], medium: 'organic' }; }
    if (/(instagram|facebook|fb\.com|t\.co|tiktok|youtube|linkedin|pinterest)/.test(h)) { return { source: h, medium: 'social' }; }
    return { source: h, medium: 'referral' };
  }
  function captureAttribution() {
    if (!ACTIVE || !granted()) { return; }
    var q = queryParams(), has = Object.keys(q).length > 0, t = null, ids, now = Date.now();
    if (has) {
      var ads = q.gclid || q.gbraid || q.wbraid;
      t = {
        source: q.utm_source || (ads ? 'google' : q.fbclid ? 'facebook' : q.msclkid ? 'bing' : ''),
        medium: q.utm_medium || (ads ? 'cpc' : q.fbclid ? 'paid_social' : q.msclkid ? 'cpc' : ''),
        campaign: q.utm_campaign || '', term: q.utm_term || '', content: q.utm_content || ''
      };
      ids = get('ids') || {};
      ['gclid', 'gbraid', 'wbraid', 'msclkid', 'ttclid'].forEach(function (k) { if (q[k]) { ids[k] = q[k]; ids[k + '_ts'] = now; } });
      if (q.fbclid) { ids.fbclid = q.fbclid; ids.fbc = 'fb.1.' + now + '.' + q.fbclid; ids.fbc_ts = now; }
      set('ids', ids);
    } else {
      t = fromReferrer();
    }
    if (!t) { return; }
    t.landing = location.pathname.replace(/^\//, '') || 'index.html';
    t.referrer = (d.referrer || '').slice(0, 200);
    t.ts = now;
    var direct = t.source === '(direct)';
    if (!fresh(get('ft'))) { set('ft', t); }
    if (!direct || !fresh(get('lt'))) { set('lt', t); }
    log('origem', t);
  }
  function attribution() {
    var lt = fresh(get('lt')) || {}, ft = fresh(get('ft')) || {}, ids = get('ids') || {}, max = (C.ATTR_DAYS || 90) * 864e5, o = {}, now = Date.now();
    ['gclid', 'gbraid', 'wbraid', 'msclkid', 'ttclid'].forEach(function (k) { if (ids[k] && (now - (ids[k + '_ts'] || 0)) <= max) { o[k] = ids[k]; } });
    if (ids.fbc && (now - (ids.fbc_ts || 0)) <= max) { o.fbc = ids.fbc; }
    return {
      utm_source: lt.source || '', utm_medium: lt.medium || '', utm_campaign: lt.campaign || '', utm_term: lt.term || '', utm_content: lt.content || '',
      first_source: ft.source || '', first_medium: ft.medium || '', first_campaign: ft.campaign || '', first_landing: ft.landing || '', last_referrer: lt.referrer || '',
      gclid: o.gclid || '', gbraid: o.gbraid || '', wbraid: o.wbraid || '', msclkid: o.msclkid || '', ttclid: o.ttclid || '',
      fbclid: ids.fbclid || '', fbc: o.fbc || '', fbp: cookie('_fbp')
    };
  }

  /* ---------- carregamento das tags (só se houver ID) ---------- */
  function loadScript(src) { var s = d.createElement('script'); s.async = true; s.src = src; d.head.appendChild(s); }
  function consentValues(ok) {
    var v = ok ? 'granted' : 'denied';
    return { ad_storage: v, analytics_storage: v, ad_user_data: v, ad_personalization: v };
  }
  function initTags() {
    if (!HAS_TAGS) { return; }
    w.dataLayer = w.dataLayer || [];
    w.gtag = w.gtag || function () { w.dataLayer.push(arguments); };
    if (NEEDS_CONSENT) {
      var dflt = consentValues(consentState() === 'granted'); dflt.wait_for_update = 500;
      w.gtag('consent', 'default', dflt);
    }
    if (C.GTM_ID) {
      w.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
      loadScript('https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(C.GTM_ID));
      if (C.GA4_ID || C.GADS_ID || C.META_PIXEL_ID) { log('AVISO: com GTM_ID preenchido, deixe GA4_ID/GADS_ID/META_PIXEL_ID vazios para não contar em dobro.'); }
    }
    if (C.GA4_ID || C.GADS_ID) {
      w.gtag('js', new Date());
      loadScript('https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(C.GA4_ID || C.GADS_ID));
      if (C.GA4_ID) { w.gtag('config', C.GA4_ID); }
      if (C.GADS_ID) { w.gtag('config', C.GADS_ID); }
    }
    if (C.META_PIXEL_ID) {
      if (!w.fbq) {
        var n = w.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
        if (!w._fbq) { w._fbq = n; }
        n.push = n; n.loaded = true; n.version = '2.0'; n.queue = [];
        loadScript('https://connect.facebook.net/en_US/fbevents.js');
      }
      w.fbq('consent', granted() ? 'grant' : 'revoke');
      w.fbq('init', C.META_PIXEL_ID);
      w.fbq('track', 'PageView');
    }
  }

  /* ---------- consentimento (LGPD) ---------- */
  var banner = null;
  function setConsent(state) {
    if (state !== 'granted' && state !== 'denied') { return; }
    set('consent', state);
    if (HAS_TAGS) {
      if (w.gtag) { w.gtag('consent', 'update', consentValues(state === 'granted')); }
      if (w.fbq) { w.fbq('consent', state === 'granted' ? 'grant' : 'revoke'); }
    }
    if (state === 'granted') { captureAttribution(); }
    hideBanner();
    log('consentimento', state);
  }
  function hideBanner() { if (banner && banner.parentNode) { banner.parentNode.removeChild(banner); } banner = null; }
  function showBanner() {
    if (banner) { return; }
    banner = d.createElement('div');
    banner.className = 'cc';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Preferências de cookies');
    banner.innerHTML = '<p>Usamos cookies e tecnologias semelhantes para medir resultados e melhorar nossos anúncios.' +
      (C.PRIVACY_URL ? ' <a href="' + C.PRIVACY_URL + '">Saiba mais</a>' : '') + '</p>' +
      '<div class="cc-btns"><button type="button" class="btn btn-ghost btn-sm" data-cc="denied">Recusar</button>' +
      '<button type="button" class="btn btn-teal btn-sm" data-cc="granted">Aceitar</button></div>';
    banner.addEventListener('click', function (e) {
      var b = e.target.closest('[data-cc]');
      if (b) { setConsent(b.getAttribute('data-cc')); }
    });
    d.body.appendChild(banner);
  }

  /* ---------- classificação dos cliques ---------- */
  function channelOf(a) {
    var x = a.getAttribute('data-track');
    if (x && CHANNELS[x]) { return x; }
    var h = a.getAttribute('href') || '';
    if (/^https?:\/\/(wa\.me|api\.whatsapp\.com|web\.whatsapp\.com|chat\.whatsapp\.com)/i.test(h)) { return 'whatsapp'; }
    if (/^tel:/i.test(h)) { return 'phone'; }
    if (/^mailto:/i.test(h)) { return 'email'; }
    if (/^https?:\/\/(www\.)?(google\.[a-z.]+\/maps|maps\.google\.|maps\.app\.goo\.gl|goo\.gl\/maps)/i.test(h)) { return 'map'; }
    if (/^https?:\/\/(www\.)?(instagram|facebook)\.com/i.test(h)) { return 'social'; }
    return '';
  }
  var LOCS = [
    ['.dock', 'botao_fixo'], ['.header', 'cabecalho'], ['.footer', 'rodape'],
    ['.intent-card', 'home_intencoes'], ['.hero-aside', 'hero_lateral'], ['.hero', 'home_hero'], ['.page-hero', 'hero_pagina'],
    ['.art-aside', 'artigo_lateral'], ['.inline-cta', 'artigo_meio'], ['.prose', 'artigo_corpo'],
    ['.cta', 'faixa_final'], ['.loc', 'contato'], ['.faq', 'faq'], ['.posts', 'blog_cards']
  ];
  function slug(s) { return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '').slice(0, 32); }
  function locationOf(a) {
    var el = a.closest('[data-loc]');
    if (el) { return el.getAttribute('data-loc'); }
    for (var i = 0; i < LOCS.length; i++) { if (a.closest(LOCS[i][0])) { return LOCS[i][1]; } }
    var sec = a.closest('section'), h = sec && sec.querySelector('h2');
    return h ? 'secao_' + slug(h.textContent) : 'pagina';
  }
  function labelOf(a, channel) {
    var l = a.getAttribute('data-label');
    if (l) { return l; }
    if (a.closest('.dock')) { return 'botao_fixo_' + channel; }
    var b = a.querySelector('b'), t = ((b && b.textContent) || a.textContent || '').replace(/\s+/g, ' ').trim();
    if (!t) { t = (a.getAttribute('aria-label') || '').trim(); }
    return t.slice(0, 80);
  }
  function pageType() {
    var og = d.querySelector('meta[property="og:type"]');
    if (og && og.getAttribute('content') === 'article') { return 'artigo'; }
    var p = location.pathname.replace(/^\//, '').replace(/\.html$/, '') || 'index';
    return p === 'index' ? 'home' : p;
  }
  function newRef() {
    var A = '23456789ABCDEFGHJKMNPQRSTUVWXYZ', s = '', i, r;
    for (i = 0; i < 5; i++) {
      r = (w.crypto && w.crypto.getRandomValues) ? w.crypto.getRandomValues(new Uint32Array(1))[0] : Math.floor(Math.random() * 4294967295);
      s += A.charAt(r % A.length);
    }
    return (C.WA_REF_PREFIX || 'VC') + '-' + s;
  }
  function addRefToLink(a, ref) {
    try {
      var u = new URL(a.href), txt = u.searchParams.get('text') || '';
      txt = txt.replace(/\s*\(ref\. [A-Z0-9]+-[A-Z0-9]+\)\s*$/, '');
      u.searchParams.set('text', txt + '\n\n(ref. ' + ref + ')');
      a.href = u.toString();
    } catch (e) { /* mantém o link original */ }
  }

  /* ---------- envio dos eventos ---------- */
  function dispatch(name, p, channel) {
    if (C.GTM_ID || C.GA4_ID || C.GADS_ID) {
      w.dataLayer = w.dataLayer || [];
      if (C.GTM_ID) { var o = { event: name }; for (var k in p) { o[k] = p[k]; } w.dataLayer.push(o); }
      else if (w.gtag) {
        w.gtag('event', name, p);
        if (C.GADS_LABELS && C.GADS_LABELS[channel]) { w.gtag('event', 'conversion', { send_to: C.GADS_LABELS[channel] }); }
      }
    }
    if (C.META_PIXEL_ID && w.fbq && C.META_EVENTS && C.META_EVENTS[channel]) {
      var opt = p.ref ? { eventID: p.ref } : undefined;
      w.fbq('track', C.META_EVENTS[channel], { content_name: p.label, content_category: p.location, contact_channel: channel }, opt);
    }
    if (C.COLLECT_URL && granted() && (channel === 'whatsapp' || channel === 'phone' || channel === 'map' || channel === 'email')) {
      var body = {}, kk;
      for (kk in p) { body[kk] = p[kk]; }
      body.token = C.COLLECT_TOKEN || '';
      body.ts = new Date().toISOString();
      body.fbp = cookie('_fbp');
      var json = JSON.stringify(body);
      try {
        if (!(navigator.sendBeacon && navigator.sendBeacon(C.COLLECT_URL, new Blob([json], { type: 'text/plain;charset=UTF-8' })))) { throw 0; }
      } catch (e) {
        try { fetch(C.COLLECT_URL, { method: 'POST', mode: 'no-cors', keepalive: true, headers: { 'Content-Type': 'text/plain;charset=UTF-8' }, body: json }); } catch (e2) { /* sem rede */ }
      }
    }
    log(name, p);
  }
  function payload(channel, a) {
    var p = attribution();
    if (!granted()) { for (var k in p) { p[k] = ''; } }
    p.channel = channel;
    p.location = a ? locationOf(a) : '';
    p.label = a ? labelOf(a, channel) : '';
    p.page = location.pathname.replace(/^\//, '') || 'index.html';
    p.page_type = pageType();
    p.device = /Mobi|Android|iPhone/i.test(navigator.userAgent) ? 'mobile' : 'desktop';
    p.ref = '';
    return p;
  }
  function onClick(e) {
    if (!ACTIVE) { return; }
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) { return; }
    var channel = channelOf(a);
    if (!channel) { return; }
    var p = payload(channel, a);
    if (channel === 'whatsapp' && C.WA_REF !== false && granted()) {
      p.ref = newRef();
      addRefToLink(a, p.ref);
    }
    dispatch('click_' + channel, p, channel);
  }

  /* ---------- início ---------- */
  initTags();
  captureAttribution();
  d.addEventListener('click', onClick, true);
  d.addEventListener('auxclick', function (e) { if (e.button === 1) { onClick(e); } }, true);

  function ready() {
    if (NEEDS_CONSENT) {
      if (!consentState()) { showBanner(); }
      var open = d.querySelector('[data-cc-open]');
      if (open) { open.hidden = false; open.addEventListener('click', function () { showBanner(); }); }
    }
  }
  if (d.readyState === 'loading') { d.addEventListener('DOMContentLoaded', ready); } else { ready(); }

  /* API pública: VCTrack.track('nome', {...}), VCTrack.attribution(), VCTrack.consent('granted'|'denied') */
  w.VCTrack = {
    track: function (name, params, channel) {
      var p = payload(channel || 'custom', null);
      for (var k in (params || {})) { p[k] = params[k]; }
      dispatch(name, p, channel || 'custom');
    },
    attribution: attribution,
    consent: setConsent,
    openConsent: showBanner,
    config: C
  };
})();
