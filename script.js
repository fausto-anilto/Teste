/* Vitória Clima — comportamento leve (sem dependências). */
(function () {
  'use strict';
  var d = document;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* menu no celular */
  var btn = d.querySelector('.menu-btn'), nav = d.getElementById('menu');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  /* revelar ao rolar */
  var items = d.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -30px 0px' });
    items.forEach(function (el, i) { el.style.transitionDelay = (i % 4) * 70 + 'ms'; io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  /* inclinação sutil nos cartões (só com mouse e sem "reduzir animações") */
  if (!reduce && window.matchMedia && matchMedia('(hover:hover) and (pointer:fine)').matches) {
    d.querySelectorAll('[data-tilt]').forEach(function (c) {
      c.addEventListener('mousemove', function (e) {
        var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        c.style.transform = 'perspective(800px) rotateY(' + (x * 5).toFixed(2) + 'deg) rotateX(' + (-y * 5).toFixed(2) + 'deg) translateY(-3px)';
      });
      c.addEventListener('mouseleave', function () { c.style.transform = ''; });
    });
  }

  /* busca no FAQ */
  var q = d.getElementById('faq-q');
  if (q) {
    var rows = d.querySelectorAll('.faq details');
    q.addEventListener('input', function () {
      var t = q.value.trim().toLowerCase();
      rows.forEach(function (r) { r.hidden = t && r.textContent.toLowerCase().indexOf(t) < 0; });
    });
  }

  /* formulário: monta a mensagem e abre o WhatsApp */
  var f = d.getElementById('form-orcamento');
  if (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = function (n) { return (f.elements[n].value || '').trim(); };
      var msg = 'Olá! Quero um orçamento de instalação de ar-condicionado.' +
        '\nNome: ' + v('nome') +
        '\nCidade/bairro: ' + v('cidade') +
        '\nImóvel: ' + v('imovel') +
        '\nQuantidade de aparelhos: ' + v('qtd') +
        (v('obs') ? '\nObservações: ' + v('obs') : '');
      var a = d.createElement('a');
      a.href = 'https://wa.me/' + f.getAttribute('data-wa') + '?text=' + encodeURIComponent(msg);
      a.target = '_blank'; a.rel = 'noopener noreferrer';
      a.setAttribute('data-label', 'Formulário de orçamento');
      d.body.appendChild(a); a.click(); d.body.removeChild(a);
    });
  }
})();
