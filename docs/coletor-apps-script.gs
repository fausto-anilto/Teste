/**
 * Vitória Clima — coletor de cliques (Planilha Google + Apps Script)
 *
 * O QUE FAZ
 *  1. Recebe cada clique em WhatsApp / telefone / mapa / e-mail enviado pelo site
 *     (tracking.js) e grava uma linha na aba "Leads", com UTM, gclid, fbclid,
 *     fbc/fbp e o código de referência (ex.: VC-7K3Q9).
 *  2. A equipe preenche as colunas de status quando o contato vira agendamento
 *     ou serviço fechado.
 *  3. O menu "Vitória Clima" gera os arquivos de conversão offline para o Google Ads
 *     e para a Meta.
 *
 * COMO INSTALAR (10 minutos) — veja também docs/RASTREAMENTO.md
 *  1. Crie uma Planilha Google vazia. Menu Extensões > Apps Script.
 *  2. Cole este arquivo inteiro, troque o TOKEN abaixo e salve.
 *  3. Implantar > Nova implantação > tipo "App da Web":
 *       Executar como: Eu  ·  Quem pode acessar: Qualquer pessoa.
 *  4. Copie a URL do app da web para COLLECT_URL em tracking-config.js
 *     e o mesmo TOKEN para COLLECT_TOKEN.
 *  5. Rode uma vez a função "preparar" (autorize) para criar as abas.
 */

var TOKEN = 'TROQUE-ESTE-TOKEN';          // qualquer texto; o mesmo vai em COLLECT_TOKEN
var FUSO = 'America/Sao_Paulo';
var MOEDA = 'BRL';

/* Nome da conversão (como está criada no Google Ads / Meta) para cada status da planilha. */
var CONVERSOES = {
  'Visita agendada': { nome: 'WhatsApp - Visita agendada', evento: 'Schedule' },
  'Serviço fechado': { nome: 'Instalação fechada',        evento: 'Purchase' }
};

var COLUNAS = [
  'recebido_em', 'ref', 'canal', 'local_no_site', 'rotulo', 'pagina', 'tipo_pagina', 'dispositivo',
  'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
  'gclid', 'gbraid', 'wbraid', 'fbclid', 'fbc', 'fbp', 'msclkid',
  'primeira_origem', 'primeira_midia', 'primeira_campanha', 'primeira_pagina', 'referrer',
  // preenchidas pela recepção:
  'status', 'telefone_cliente', 'valor', 'data_conversao', 'observacoes'
];

function preparar() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName('Leads') || ss.insertSheet('Leads');
  if (sh.getLastRow() === 0) {
    sh.appendRow(COLUNAS);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, COLUNAS.length).setFontWeight('bold').setBackground('#F6E1E3');
  }
  var col = COLUNAS.indexOf('status') + 1;
  var regra = SpreadsheetApp.newDataValidation().requireValueInList(['Novo', 'Conversando', 'Visita agendada', 'Serviço fechado', 'Perdido'], true).build();
  sh.getRange(2, col, 2000, 1).setDataValidation(regra);
}

function doGet() { return ContentService.createTextOutput('coletor ativo'); }

function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);
    if (d.token !== TOKEN) { return ContentService.createTextOutput('negado'); }
    var sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Leads');
    var linha = [
      new Date(d.ts || new Date()), d.ref || '', d.channel || '', d.location || '', d.label || '', d.page || '', d.page_type || '', d.device || '',
      d.utm_source || '', d.utm_medium || '', d.utm_campaign || '', d.utm_term || '', d.utm_content || '',
      d.gclid || '', d.gbraid || '', d.wbraid || '', d.fbclid || '', d.fbc || '', d.fbp || '', d.msclkid || '',
      d.first_source || '', d.first_medium || '', d.first_campaign || '', d.first_landing || '', d.last_referrer || '',
      'Novo', '', '', '', ''
    ];
    sh.appendRow(linha);
    return ContentService.createTextOutput('ok');
  } catch (err) {
    return ContentService.createTextOutput('erro');
  }
}

/* ---------- menu ---------- */
function onOpen() {
  SpreadsheetApp.getUi().createMenu('Vitória Clima')
    .addItem('Exportar conversões — Google Ads', 'exportarGoogleAds')
    .addItem('Exportar eventos — Meta', 'exportarMeta')
    .addToUi();
}

function linhasConvertidas_() {
  var sh = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Leads');
  var v = sh.getDataRange().getValues(), h = v.shift(), idx = {};
  h.forEach(function (n, i) { idx[n] = i; });
  return v.filter(function (r) { return CONVERSOES[r[idx.status]]; }).map(function (r) {
    var o = {}; h.forEach(function (n, i) { o[n] = r[i]; }); return o;
  });
}

function dataConversao_(o) { return o.data_conversao ? new Date(o.data_conversao) : new Date(o.recebido_em); }

function escreverAba_(nome, cabecalho, linhas) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(nome) || ss.insertSheet(nome);
  sh.clear();
  sh.getRange(1, 1, 1, cabecalho.length).setValues([cabecalho]).setFontWeight('bold');
  if (linhas.length) { sh.getRange(2, 1, linhas.length, cabecalho.length).setValues(linhas); }
  ss.setActiveSheet(sh);
  return linhas.length;
}

/**
 * Google Ads: importação de conversões por clique (gclid).
 * Em Metas > Conversões > Uploads, baixe o modelo e confirme as colunas antes de importar.
 * Linhas com gbraid/wbraid (iOS) usam outro modelo: saem na aba "GoogleAds_gbraid_wbraid".
 */
function exportarGoogleAds() {
  var todas = linhasConvertidas_(), gc = [], outros = [];
  todas.forEach(function (o) {
    var c = CONVERSOES[o.status], quando = Utilities.formatDate(dataConversao_(o), FUSO, "yyyy-MM-dd HH:mm:ssXXX");
    var valor = o.valor === '' ? '' : Number(o.valor);
    if (o.gclid) { gc.push([o.gclid, c.nome, quando, valor, valor === '' ? '' : MOEDA]); }
    else if (o.gbraid || o.wbraid) { outros.push([o.gbraid || '', o.wbraid || '', c.nome, quando, valor, valor === '' ? '' : MOEDA]); }
  });
  var n = escreverAba_('GoogleAds_gclid', ['Google Click ID', 'Conversion Name', 'Conversion Time', 'Conversion Value', 'Conversion Currency'], gc);
  escreverAba_('GoogleAds_gbraid_wbraid', ['GBRAID', 'WBRAID', 'Conversion Name', 'Conversion Time', 'Conversion Value', 'Conversion Currency'], outros);
  SpreadsheetApp.getUi().alert(n + ' conversões com gclid prontas na aba GoogleAds_gclid.\nBaixe a aba como CSV (Arquivo > Fazer download > CSV).');
}

/**
 * Meta: eventos offline. O telefone do cliente é normalizado (só dígitos, com 55) e
 * enviado em SHA-256, como a Meta exige. Confirme o modelo atual no Gerenciador de Eventos
 * (ou use a API de Conversões) antes de subir: os nomes de colunas podem mudar.
 */
function exportarMeta() {
  var todas = linhasConvertidas_(), out = [];
  todas.forEach(function (o) {
    var c = CONVERSOES[o.status], fone = String(o.telefone_cliente || '').replace(/\D/g, '');
    if (fone && fone.indexOf('55') !== 0) { fone = '55' + fone; }
    var hash = fone ? sha256_(fone) : '';
    if (!hash && !o.fbc) { return; }
    var t = Math.floor(dataConversao_(o).getTime() / 1000);
    out.push([hash, o.fbc || '', o.fbp || '', c.evento, t, o.valor === '' ? '' : Number(o.valor), o.valor === '' ? '' : MOEDA, o.ref || '']);
  });
  var n = escreverAba_('Meta_eventos', ['ph', 'fbc', 'fbp', 'event_name', 'event_time', 'value', 'currency', 'event_id'], out);
  SpreadsheetApp.getUi().alert(n + ' eventos prontos na aba Meta_eventos (linhas sem telefone e sem fbc foram ignoradas).');
}

function sha256_(txt) {
  var b = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, txt, Utilities.Charset.UTF_8);
  return b.map(function (x) { var h = (x < 0 ? x + 256 : x).toString(16); return h.length === 1 ? '0' + h : h; }).join('');
}
