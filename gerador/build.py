#!/usr/bin/env python3
"""Gerador do site Vitória Clima (HTML estático, estrutura plana).

Uso:  python3 gerador/build.py
Escreve as páginas, sitemap.xml, robots.txt, llms.txt e vercel.json na raiz do projeto.
Os dados de contato e o domínio ficam em CONFIG; tudo o que precisa ser confirmado
com o cliente está marcado em PENDENTE e listado em docs/PENDENCIAS.md.
"""
import json
import os
import sys
from datetime import date
from html import escape
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TODAY = date.today().isoformat()

# ----------------------------------------------------------------------------
# CONFIG — trocar aqui quando o cliente confirmar (veja docs/PENDENCIAS.md)
# ----------------------------------------------------------------------------
BRAND = "Vitória Clima"
DOMAIN = "https://vitoriaclima.com.br"          # PENDENTE: domínio real
WA_NUMBER = "5527900000000"                     # PENDENTE: WhatsApp real (55 + DDD + número)
PHONE_TEL = "+5527900000000"                    # PENDENTE: telefone real
PHONE_SHOW = "(27) 90000-0000"                  # PENDENTE: telefone como aparece na tela
EMAIL = ""                                      # PENDENTE: e-mail real (vazio = não aparece)
PLACEHOLDERS = [WA_NUMBER, PHONE_TEL]

CITIES = [
    {
        "slug": "vitoria", "name": "Vitória",
        "h1": "Instalação de ar-condicionado em Vitória",
        "desc": "Instalação de ar-condicionado split em Vitória (ES): casas e apartamentos. Avaliação do local e orçamento pelo WhatsApp.",
        "intro": [
            "Vitória concentra muitos prédios residenciais, e é nos apartamentos que a instalação pede mais cuidado: definir onde a condensadora vai ficar, como a água do dreno será escoada sem incomodar ninguém e o que o regimento do condomínio permite na fachada.",
            "Como a cidade é cercada de água, a maresia também entra na conta. Na avaliação do local, a posição da condensadora e a escolha do aparelho levam isso em consideração, para o equipamento durar mais.",
        ],
        "bairros": ["Jardim Camburi", "Praia do Canto", "Jardim da Penha", "Santa Lúcia", "Mata da Praia", "Bento Ferreira", "Enseada do Suá", "Centro"],
        "faq": [
            ("Instalam ar-condicionado em apartamento em Vitória?", "Sim. Antes de agendar, vale consultar o síndico ou o regimento interno sobre regras de fachada e horários de obra. Na avaliação do local, definimos onde ficam a evaporadora, a condensadora e o dreno."),
            ("Atendem todos os bairros de Vitória?", "A lista de bairros desta página é um exemplo das regiões atendidas. Chame no WhatsApp com o seu bairro para confirmar o atendimento."),
        ],
    },
    {
        "slug": "vila-velha", "name": "Vila Velha",
        "h1": "Instalação de ar-condicionado em Vila Velha",
        "desc": "Instalação de ar-condicionado split em Vila Velha (ES), de casas a apartamentos na orla. Peça seu orçamento pelo WhatsApp.",
        "intro": [
            "Em Vila Velha, boa parte dos imóveis fica perto do mar. Isso pesa na hora de instalar: a condensadora fica exposta ao ar salgado, então a escolha do local e a manutenção periódica fazem diferença na vida útil do aparelho.",
            "O atendimento cobre casas e apartamentos. Na avaliação, combinamos o ponto de instalação, a passagem da tubulação e o escoamento do dreno, e você recebe o orçamento pelo WhatsApp.",
        ],
        "bairros": ["Praia da Costa", "Itapuã", "Itaparica", "Coqueiral de Itaparica", "Glória", "Centro de Vila Velha", "Jaburuna", "Ataíde"],
        "faq": [
            ("A maresia de Vila Velha danifica o ar-condicionado?", "A maresia acelera a corrosão em áreas externas, e a condensadora é a parte mais exposta. Por isso a posição de instalação e a limpeza periódica importam; leia o artigo sobre ar-condicionado e maresia para os cuidados."),
            ("Como peço orçamento em Vila Velha?", "Pelo WhatsApp: informe o bairro, o tipo de imóvel e quantos aparelhos você quer instalar. A avaliação do local define o valor final."),
        ],
    },
    {
        "slug": "serra", "name": "Serra",
        "h1": "Instalação de ar-condicionado na Serra",
        "desc": "Instalação de ar-condicionado split na Serra (ES) para casas e condomínios. Avaliação do local e orçamento pelo WhatsApp.",
        "intro": [
            "A Serra tem muitas casas e condomínios, onde a instalação costuma envolver mais de um ambiente. Vale planejar tudo de uma vez: a quantidade de aparelhos, o caminho da tubulação e a carga na instalação elétrica.",
            "Na avaliação, verificamos o ponto de instalação de cada ambiente e orientamos sobre a escolha da capacidade (BTUs), para você receber um orçamento fechado, sem surpresas no meio da obra.",
        ],
        "bairros": ["Laranjeiras", "Jardim Limoeiro", "Manguinhos", "Valparaíso", "Carapina", "Colina de Laranjeiras", "Praia de Carapebus"],
        "faq": [
            ("Dá para instalar vários aparelhos no mesmo dia na Serra?", "Depende da quantidade de aparelhos e da infraestrutura de cada ambiente. O prazo é combinado na avaliação do local."),
            ("Preciso adaptar a parte elétrica?", "Pode ser necessário, dependendo do aparelho e do que já existe no imóvel. Isso é verificado na avaliação, antes do orçamento final."),
        ],
    },
    {
        "slug": "cariacica", "name": "Cariacica",
        "h1": "Instalação de ar-condicionado em Cariacica",
        "desc": "Instalação de ar-condicionado split em Cariacica (ES), com avaliação do local e orçamento pelo WhatsApp.",
        "intro": [
            "Em Cariacica, a instalação de ar-condicionado em casas costuma pedir atenção à posição da condensadora, ao caimento do dreno e à fiação que alimenta o aparelho. Esses três pontos definem se o split vai funcionar bem por muitos anos.",
            "Para saber o que o seu imóvel precisa, o primeiro passo é uma conversa pelo WhatsApp e, em seguida, a avaliação do local. Com ela, você recebe o orçamento detalhado.",
        ],
        "bairros": ["Campo Grande", "Jardim América", "Alto Lage", "Itacibá", "Porto de Santana"],
        "faq": [
            ("Atendem Cariacica inteira?", "Os bairros listados são exemplos. Chame no WhatsApp com o seu endereço para confirmar o atendimento na sua região."),
            ("Como saber qual aparelho comprar?", "A capacidade em BTUs depende do tamanho do ambiente, da incidência de sol e do uso. Veja o artigo sobre como escolher o BTU ou peça ajuda no WhatsApp."),
        ],
    },
    {
        "slug": "viana", "name": "Viana",
        "h1": "Instalação de ar-condicionado em Viana",
        "desc": "Instalação de ar-condicionado split em Viana (ES) para residências. Peça avaliação do local e orçamento pelo WhatsApp.",
        "intro": [
            "Viana faz parte da Grande Vitória e também é atendida. Para residências, o processo é o mesmo: conversa inicial, avaliação do local, orçamento claro e instalação seguindo as orientações do fabricante do aparelho.",
            "Se você ainda não escolheu o equipamento, dá para pedir orientação antes da compra. Assim você evita comprar um aparelho com capacidade acima ou abaixo da necessidade do ambiente.",
        ],
        "bairros": ["Centro", "Marcílio de Noronha", "Areinha", "Universal", "Nova Bethânia"],
        "faq": [
            ("Posso comprar o aparelho por conta própria?", "Pode. Antes de comprar, converse pelo WhatsApp para conferir se o modelo e a capacidade fazem sentido para o ambiente."),
            ("Como funciona o orçamento em Viana?", "Você descreve o imóvel pelo WhatsApp, combinamos a avaliação do local e, depois dela, enviamos o orçamento."),
        ],
    },
    {
        "slug": "guarapari", "name": "Guarapari",
        "h1": "Instalação de ar-condicionado em Guarapari",
        "desc": "Instalação de ar-condicionado split em Guarapari (ES), com cuidados para áreas litorâneas. Orçamento pelo WhatsApp.",
        "intro": [
            "Guarapari é litorânea, então a maresia é um fator real para a condensadora. A posição de instalação e a limpeza periódica ajudam a proteger o equipamento, e vale conferir com o fabricante as condições de garantia para áreas de praia.",
            "Em imóveis usados só em parte do ano, como casas de temporada, também é importante revisar o aparelho antes de voltar a usá-lo. Pelo WhatsApp você descreve o imóvel e combinamos a avaliação.",
        ],
        "bairros": ["Centro", "Praia do Morro", "Enseada Azul", "Muquiçaba", "Meaípe", "Perocão", "Setiba"],
        "faq": [
            ("A instalação em Guarapari é diferente por causa do mar?", "O processo é o mesmo, mas a escolha do local da condensadora e a manutenção periódica ganham importância por causa da maresia."),
            ("Atendem casas de temporada?", "Sim, mande uma mensagem com o bairro e o número de aparelhos para combinarmos a avaliação do local."),
        ],
    },
]

HOME_FAQ = [
    ("Quais cidades vocês atendem?", "A Vitória Clima atende a Grande Vitória: Vitória, Vila Velha, Serra, Cariacica, Viana e Guarapari. Se o seu bairro não está nas listas, chame no WhatsApp para confirmar."),
    ("Como peço um orçamento de instalação?", "Pelo WhatsApp. Informe a cidade, o tipo de imóvel e quantos aparelhos você quer instalar. Em seguida, combinamos a avaliação do local e você recebe o orçamento."),
    ("A avaliação do local tem custo?", "A avaliação é gratuita. Ela serve para definir o ponto de instalação, o caminho da tubulação, o dreno e a parte elétrica antes do orçamento final."),
    ("Instalam em apartamento?", "Sim. Em apartamento, vale consultar antes o síndico ou o regimento interno sobre fachada e horários de obra. Veja o artigo sobre instalação em apartamento."),
    ("Posso comprar o aparelho por conta própria?", "Pode. Converse antes pelo WhatsApp para conferir se o modelo e a capacidade (BTUs) são adequados para o ambiente."),
    ("Como saber quantos BTUs preciso?", "Depende da área, da incidência de sol, do número de pessoas e dos equipamentos do ambiente. O artigo sobre BTUs explica o raciocínio, e na avaliação do local a escolha é confirmada."),
    ("Vocês fazem manutenção?", "Sim, manutenção preventiva e corretiva de ar-condicionado. Chame no WhatsApp descrevendo o problema ou o tempo desde a última limpeza."),
]

# ----------------------------------------------------------------------------
# Ícones (traços no estilo Lucide, licença ISC)
# ----------------------------------------------------------------------------
ICONS = {
    "snowflake": '<line x1="2" x2="22" y1="12" y2="12"/><line x1="12" x2="12" y1="2" y2="22"/><path d="m20 16-4-4 4-4"/><path d="m4 8 4 4-4 4"/><path d="m16 4-4 4-4-4"/><path d="m8 20 4-4 4 4"/>',
    "wind": '<path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"/><path d="M9.6 4.6A2 2 0 1 1 11 8H2"/><path d="M12.6 19.4A2 2 0 1 0 14 16H2"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "check": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "chat": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "menu": '<line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "book": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    "home": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    "building": '<rect width="16" height="20" x="4" y="2" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
    "gauge": '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
}


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def wa(text):
    return f"https://wa.me/{WA_NUMBER}?text={quote(text)}"


def url(path):
    return f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"


def page_title(t):
    full = f"{t} | {BRAND}"
    return full if len(full) <= 60 else t


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)}
                                for i, (n, p) in enumerate(trail)]}


def business_ld():
    b = {
        "@context": "https://schema.org", "@type": "HVACBusiness", "@id": url("") + "#negocio",
        "name": BRAND, "url": url(""), "image": url("og-image.jpg"),
        "telephone": PHONE_TEL,
        "description": "Instalação e manutenção de ar-condicionado split na Grande Vitória, Espírito Santo.",
        "areaServed": [{"@type": "City", "name": c["name"]} for c in CITIES],
        "address": {"@type": "PostalAddress", "addressRegion": "ES", "addressCountry": "BR"},
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Instalação de ar-condicionado split"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Manutenção preventiva e corretiva de ar-condicionado"}},
        ],
    }
    if EMAIL:
        b["email"] = EMAIL
    return b


# ----------------------------------------------------------------------------
# Peças de layout
# ----------------------------------------------------------------------------
NAV = [("Início", "index.html"), ("Serviços", "servicos.html"), ("Blog", "blog.html"),
       ("Perguntas", "faq.html"), ("Contato", "contato.html")]


def header(current):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (p, ' aria-current="page"' if p == current else "", n) for n, p in NAV)
    return f'''<a class="skip" href="#conteudo">Ir para o conteúdo</a>
<header class="header"><div class="wrap">
<a class="brand" href="index.html" aria-label="{BRAND} — página inicial">{icon("snowflake")}<span>{BRAND}</span></a>
<button class="menu-btn" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu">{icon("menu")}</button>
<nav class="nav" id="menu" aria-label="Principal">{links}
<a class="btn btn-wa btn-sm" href="{wa("Olá! Quero um orçamento de instalação de ar-condicionado.")}" target="_blank" rel="noopener noreferrer" data-label="Pedir orçamento">{icon("chat")}Pedir orçamento</a>
</nav></div></header>'''


def flow_svg():
    return ('<svg class="flow" viewBox="0 0 1200 500" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M-20 120 C 200 60, 380 190, 600 120 S 1000 60, 1220 130"/>'
            '<path d="M-20 260 C 220 200, 420 330, 640 260 S 1000 190, 1220 280"/>'
            '<path d="M-20 400 C 240 340, 400 460, 620 390 S 1000 330, 1220 410"/></svg>')


def waves_svg():
    one = ('<svg viewBox="0 0 1440 64" preserveAspectRatio="none" aria-hidden="true">'
           '<path fill="currentColor" d="M0 32 C 180 64, 360 0, 540 32 S 900 64, 1080 32 S 1320 8, 1440 32 V64 H0Z"/></svg>')
    return f'<div class="waves" aria-hidden="true"><div class="waves-track">{one}{one}</div></div>'


def dock():
    return f'''<div class="dock">
<a class="btn btn-wa" href="{wa("Olá! Quero um orçamento de instalação de ar-condicionado.")}" target="_blank" rel="noopener noreferrer">{icon("chat")}<span class="lbl">Chamar no WhatsApp</span></a>
<a class="btn btn-primary btn-phone" href="tel:{PHONE_TEL}" aria-label="Ligar para {BRAND}">{icon("phone")}<span class="lbl">Ligar</span></a>
</div>'''


def footer():
    cid = "".join(f'<li><a href="instalacao-ar-condicionado-{c["slug"]}.html">{c["name"]}</a></li>' for c in CITIES)
    pages = "".join(f'<li><a href="{p}">{n}</a></li>' for n, p in NAV)
    mail = f'<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>' if EMAIL else ""
    return f'''{waves_svg()}
<footer class="footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html">{icon("snowflake")}<span>{BRAND}</span></a>
<p>Instalação e manutenção de ar-condicionado split na Grande Vitória, Espírito Santo.</p></div>
<div><h3>Páginas</h3><ul>{pages}</ul></div>
<div><h3>Cidades atendidas</h3><ul>{cid}</ul></div>
<div><h3>Contato</h3><ul>
<li><a href="{wa("Olá! Quero um orçamento de instalação de ar-condicionado.")}" target="_blank" rel="noopener noreferrer">WhatsApp</a></li>
<li><a href="tel:{PHONE_TEL}">{PHONE_SHOW}</a></li>{mail}</ul></div>
</div>
<p class="legal">&copy; {date.today().year} {BRAND}. Todos os direitos reservados.</p>
</div></footer>'''


def cta_block(title="Peça seu orçamento de instalação", text="Conte a cidade, o tipo de imóvel e quantos aparelhos. Respondemos pelo WhatsApp."):
    return f'''<section class="cta"><div class="wrap rv">
<h2>{title}</h2><p>{text}</p>
<div class="btn-row"><a class="btn btn-wa btn-lg" href="{wa("Olá! Quero um orçamento de instalação de ar-condicionado.")}" target="_blank" rel="noopener noreferrer">{icon("chat")}Chamar no WhatsApp</a>
<a class="btn btn-ghost btn-lg" href="tel:{PHONE_TEL}">{icon("phone")}Ligar agora</a></div>
</div></section>'''


def faq_block(items, search=False):
    s = ('<label class="sr-only" for="faq-q">Buscar pergunta</label>'
         '<input class="faq-search" id="faq-q" type="search" placeholder="Buscar pergunta…" autocomplete="off">') if search else ""
    rows = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in items)
    return f'{s}<div class="faq rv">{rows}</div>'


def cities_grid():
    return '<div class="cities">' + "".join(
        f'<a href="instalacao-ar-condicionado-{c["slug"]}.html" data-label="Cidade {c["name"]}">{c["name"]}{icon("arrow")}</a>'
        for c in CITIES) + "</div>"


def marquee():
    one = "".join(f'<span>{icon("pin")}{c["name"]}</span>' for c in CITIES)
    return f'<div class="marquee" aria-hidden="true"><div class="marquee-track">{one}{one}{one}{one}</div></div>'


def post_card(a):
    return (f'<a class="post rv" href="{a["slug"]}.html"><div class="post-top">{icon(a["icon"])}</div>'
            f'<div class="post-body"><h3>{a["title"]}</h3><p>{a["desc"]}</p><small>Ler artigo · {a["read"]} min</small></div></a>')


def render(*, path, title, desc, body, current="", jsonld=(), og_type="website", noindex=False):
    assert len(title) <= 60, f"title longo ({len(title)}): {title}"
    assert len(desc) <= 160, f"description longa ({len(desc)}): {desc}"
    canon = url("" if path == "index.html" else path)
    scripts = "\n".join(ld(j) for j in jsonld)
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
{robots}<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0c3d66">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{url("og-image.jpg")}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preload" href="poppins-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="style.css">
<script>document.documentElement.classList.add("js")</script>
{scripts}
</head>
<body>
{header(current)}
<main id="conteudo">
{body}
</main>
{footer()}
{dock()}
<script src="tracking-config.js" defer></script>
<script src="tracking.js" defer></script>
<script src="script.js" defer></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(html)
    PAGES.append((path, TODAY))


PAGES = []


def page_hero(title, lead, trail, aside=""):
    cr = " › ".join(f'<a href="{p}">{n}</a>' if p else n for n, p in trail)
    aside_html = f'<aside class="hero-aside">{aside}</aside>' if aside else ""
    cls = "page-hero-grid" if aside else ""
    inner = f'<div><h1>{nb(title)}</h1><p class="lead">{lead}</p><div class="btn-row"><a class="btn btn-wa" href="{wa("Olá! Quero um orçamento de instalação de ar-condicionado.")}" target="_blank" rel="noopener noreferrer">{icon("chat")}Pedir orçamento</a></div></div>{aside_html}'
    return f'''<section class="page-hero">{flow_svg()}<div class="wrap">
<nav class="crumbs" aria-label="Você está em">{cr}</nav>
<div class="{cls}">{inner}</div></div></section>'''


def nb(s):
    return s.replace("ar-condicionado", '<span style="white-space:nowrap">ar-condicionado</span>')


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{icon('check')}<span>{t}</span></li>" for t in items) + "</ul>"


# ----------------------------------------------------------------------------
# Páginas
# ----------------------------------------------------------------------------
INTENTS = [
    ("Instalar um split novo", "Compre o aparelho e deixe a instalação com a gente.", "Olá! Quero instalar um ar-condicionado split novo."),
    ("Instalação em apartamento", "Fachada, dreno e condensadora planejados com antecedência.", "Olá! Preciso instalar ar-condicionado em apartamento."),
    ("Instalação em casa", "Do quarto à sala, vários ambientes em uma só visita.", "Olá! Quero instalar ar-condicionado na minha casa."),
    ("Quantos BTUs eu preciso?", "Ajuda para escolher a capacidade certa antes de comprar.", "Olá! Preciso de ajuda para escolher a capacidade (BTUs) do ar-condicionado."),
    ("Manutenção e limpeza", "Preventiva e corretiva, para o aparelho render mais.", "Olá! Quero agendar manutenção do meu ar-condicionado."),
    ("Orçamento rápido", "Conte o que você precisa e receba o orçamento.", "Olá! Quero um orçamento de instalação de ar-condicionado."),
]


def build_home():
    intents = "".join(
        f'<a class="intent-card rv" data-tilt href="{wa(msg)}" target="_blank" rel="noopener noreferrer"><b>{t}</b><span>{d}</span><em>WhatsApp</em></a>'
        for t, d, msg in INTENTS)
    services = f'''
<article class="card rv" data-tilt><div class="ico">{icon("wind")}</div><h3>Instalação de split</h3><p>Instalação de ar-condicionado split em casas e apartamentos, com avaliação do local antes do orçamento.</p></article>
<article class="card rv" data-tilt><div class="ico">{icon("wrench")}</div><h3>Manutenção</h3><p>Manutenção preventiva e corretiva para manter o aparelho funcionando bem e evitar problemas maiores.</p></article>
<article class="card rv" data-tilt><div class="ico">{icon("gauge")}</div><h3>Escolha do equipamento</h3><p>Orientação sobre capacidade em BTUs e tipo de aparelho (inverter ou convencional) conforme o ambiente.</p></article>'''
    steps = '''
<li class="rv"><h3>Você chama no WhatsApp</h3><p>Informe a cidade, o tipo de imóvel e quantos aparelhos quer instalar.</p></li>
<li class="rv"><h3>Avaliação do local</h3><p>Definimos o ponto de cada unidade, a tubulação, o dreno e a parte elétrica.</p></li>
<li class="rv"><h3>Orçamento claro</h3><p>Você recebe o valor com o que está incluído, para decidir com tranquilidade.</p></li>
<li class="rv"><h3>Instalação e orientação</h3><p>Instalamos conforme o manual do fabricante e explicamos o uso e a limpeza dos filtros.</p></li>'''
    why = f'''
<div class="card rv"><div class="ico">{icon("check")}</div><h3>Equipe especializada</h3><p>Instalação feita por profissionais de climatização, seguindo o manual do fabricante.</p></div>
<div class="card rv"><div class="ico">{icon("check")}</div><h3>Orçamento claro</h3><p>Avaliação do local antes do valor final, para não ter surpresa durante a obra.</p></div>
<div class="card rv"><div class="ico">{icon("check")}</div><h3>Atendimento pelo WhatsApp</h3><p>Você explica o que precisa, tira dúvidas e agenda sem burocracia.</p></div>
<div class="card rv"><div class="ico">{icon("check")}</div><h3>Foco na Grande Vitória</h3><p>Atendimento em Vitória, Vila Velha, Serra, Cariacica, Viana e Guarapari.</p></div>'''
    posts = "".join(post_card(a) for a in ARTICLES[:3])
    body = f'''
<section class="hero">{flow_svg()}<div class="wrap hero-grid">
<div class="rv in"><span class="eyebrow">Grande Vitória · Espírito Santo</span>
<h1>{nb('Instalação de ar-condicionado na Grande Vitória')}</h1>
<p class="lead">Instalamos ar-condicionado split em casas e apartamentos de Vitória, Vila Velha, Serra, Cariacica, Viana e Guarapari. Avaliação do local e orçamento pelo WhatsApp.</p>
<div class="btn-row"><a class="btn btn-wa btn-lg" href="{wa("Olá! Quero um orçamento de instalação de ar-condicionado.")}" target="_blank" rel="noopener noreferrer">{icon("chat")}Pedir orçamento</a>
<a class="btn btn-ghost btn-lg" href="tel:{PHONE_TEL}">{icon("phone")}Ligar</a></div></div>
<aside class="hero-aside"><h2>Como funciona</h2>
{ticks(["Você descreve o imóvel pelo WhatsApp", "Fazemos a avaliação do local", "Você recebe o orçamento e agenda a instalação"])}
<a class="btn btn-wa" href="{wa("Olá! Quero um orçamento de instalação de ar-condicionado.")}" target="_blank" rel="noopener noreferrer">Começar agora</a></aside>
</div></section>
{marquee()}

<section><div class="wrap"><div class="sec-head"><h2>O que você precisa hoje?</h2><p>Escolha o assunto e a conversa já abre no WhatsApp com a mensagem pronta.</p></div>
<div class="grid g3">{intents}</div></div></section>

<section class="sec-alt"><div class="wrap"><div class="sec-head"><h2>Nossos serviços</h2><p>Do planejamento à instalação, com foco em ar-condicionado split residencial.</p></div>
<div class="grid g3">{services}</div>
<p style="margin-top:1.6rem"><a class="btn btn-ghost-dark" href="servicos.html">Ver detalhes dos serviços</a></p></div></section>

<section><div class="wrap"><div class="sec-head center"><h2>Como é a instalação do início ao fim</h2><p>Quatro passos simples, sem complicação.</p></div>
<ol class="steps">{steps}</ol></div></section>

<section class="sec-alt"><div class="wrap"><div class="sec-head"><h2>Cidades atendidas na Grande Vitória</h2>
<p>Cada cidade tem uma página com as particularidades da região e os bairros atendidos.</p></div>
{cities_grid()}</div></section>

<section><div class="wrap"><div class="sec-head center"><h2>Por que escolher a {BRAND}</h2></div>
<div class="grid g4">{why}</div></div></section>

<section class="sec-alt"><div class="wrap"><div class="sec-head"><h2>Dicas para quem vai instalar</h2><p>Artigos para decidir melhor antes de comprar e instalar.</p></div>
<div class="posts">{posts}</div>
<p style="margin-top:1.6rem"><a class="btn btn-ghost-dark" href="blog.html">Ver todos os artigos</a></p></div></section>

<section><div class="wrap"><div class="sec-head center"><h2>Perguntas frequentes</h2></div>
{faq_block(HOME_FAQ)}</div></section>
{cta_block()}'''
    render(path="index.html", title="Instalação de Ar-Condicionado na Grande Vitória",
           desc="Instalação de ar-condicionado split em Vitória, Vila Velha, Serra, Cariacica, Viana e Guarapari. Avaliação do local e orçamento pelo WhatsApp.",
           body=body, current="index.html", jsonld=[business_ld(), faq_ld(HOME_FAQ)])


def build_services():
    items = [
        ("Instalação de ar-condicionado split", "wind",
         "Instalação em casas e apartamentos. A avaliação do local define o ponto da evaporadora e da condensadora, o caminho da tubulação, o dreno e a parte elétrica. A instalação segue o manual do fabricante."),
        ("Manutenção preventiva e corretiva", "wrench",
         "Limpeza e revisão para manter o desempenho e evitar mau cheiro, pingos e perda de rendimento. Quando o aparelho já apresenta defeito, a manutenção corretiva identifica e resolve a causa."),
        ("Escolha do equipamento", "gauge",
         "Ajuda para definir a capacidade em BTUs e o tipo de aparelho, inverter ou convencional, de acordo com o tamanho do ambiente, o sol e o uso."),
    ]
    blocks = "".join(
        f'<article class="card rv" data-tilt><div class="ico">{icon(i)}</div><h3>{t}</h3><p>{d}</p>'
        f'<p style="margin-top:1rem"><a class="btn btn-wa btn-sm" href="{wa("Olá! Quero saber mais sobre: " + t + ".")}" target="_blank" rel="noopener noreferrer">{icon("chat")}Pedir orçamento</a></p></article>'
        for t, i, d in items)
    body = f'''
{page_hero("Serviços de ar-condicionado na Grande Vitória", "Instalação, manutenção e orientação para escolher o aparelho certo, em casas e apartamentos.", [("Início", "index.html"), ("Serviços", "")])}
<section><div class="wrap"><h2 class="sr-only">Nossos serviços</h2><div class="grid g3">{blocks}</div></div></section>
<section class="sec-alt"><div class="wrap"><div class="sec-head"><h2>Como a instalação é conduzida</h2></div>
<ol class="steps">
<li class="rv"><h3>Conversa e avaliação</h3><p>Entendemos o ambiente e avaliamos o local da instalação.</p></li>
<li class="rv"><h3>Orçamento</h3><p>Valor claro, com o que está incluído e o que depende de infraestrutura.</p></li>
<li class="rv"><h3>Instalação</h3><p>Fixação, tubulação, dreno, ligação elétrica e teste de funcionamento.</p></li>
<li class="rv"><h3>Orientação</h3><p>Explicamos o uso do controle e a limpeza dos filtros.</p></li>
</ol></div></section>
<section><div class="wrap"><div class="sec-head"><h2>Onde atendemos</h2><p>Escolha a sua cidade para ver os bairros e as particularidades da região.</p></div>
{cities_grid()}</div></section>
{cta_block()}'''
    render(path="servicos.html", title="Serviços de Ar-Condicionado na Grande Vitória",
           desc="Instalação e manutenção de ar-condicionado split na Grande Vitória, com orientação para escolher o aparelho. Peça orçamento pelo WhatsApp.",
           body=body, current="servicos.html",
           jsonld=[crumbs_ld([("Início", "index.html"), ("Serviços", "servicos.html")])])


def build_city(c):
    path = f"instalacao-ar-condicionado-{c['slug']}.html"
    others = "".join(
        f'<li><a href="instalacao-ar-condicionado-{o["slug"]}.html">{o["name"]}</a></li>' for o in CITIES if o["slug"] != c["slug"])
    chips = "".join(f"<li>{b}</li>" for b in c["bairros"])
    msg = f"Olá! Quero um orçamento de instalação de ar-condicionado em {c['name']}."
    faq = c["faq"] + HOME_FAQ[1:3]
    body = f'''
{page_hero(c["h1"], c["desc"], [("Início", "index.html"), ("Serviços", "servicos.html"), (c["name"], "")],
           aside=f'<h2>Atendimento em {c["name"]}</h2>' + ticks(["Avaliação do local", "Orçamento pelo WhatsApp", "Casas e apartamentos"]) + f'<a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener noreferrer">Pedir orçamento</a>')}
<section><div class="wrap art-grid"><div class="prose rv">
<h2>Instalação de split em {c["name"]}</h2>
<p>{c["intro"][0]}</p><p>{c["intro"][1]}</p>
<h2>Bairros atendidos em {c["name"]}</h2>
<p>Alguns dos bairros e regiões onde fazemos instalação. Se o seu não está na lista, chame no WhatsApp para confirmar.</p>
<ul class="chips">{chips}</ul>
<div class="inline-cta"><p>Quer instalar ar-condicionado em {c["name"]}?</p><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener noreferrer">{icon("chat")}Chamar no WhatsApp</a></div>
<h2>Leia antes de instalar</h2>
<ul>{"".join(f'<li><a href="{a["slug"]}.html">{a["title"]}</a></li>' for a in ARTICLES[:4])}</ul>
<h2>Também atendemos</h2><ul class="related">{others}</ul>
</div>
<aside class="art-aside"><h2>Orçamento em {c["name"]}</h2><p>Conte o bairro, o tipo de imóvel e quantos aparelhos.</p>
<a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener noreferrer">{icon("chat")}WhatsApp</a>
<a class="btn btn-ghost-dark" href="tel:{PHONE_TEL}">{icon("phone")}Ligar</a></aside></div></section>
<section class="sec-alt"><div class="wrap"><div class="sec-head center"><h2>Perguntas sobre instalação em {c["name"]}</h2></div>{faq_block(faq)}</div></section>
{cta_block()}'''
    render(path=path, title=page_title(c["h1"]), desc=c["desc"], body=body, current="servicos.html",
           jsonld=[business_ld(), faq_ld(faq),
                   crumbs_ld([("Início", "index.html"), ("Serviços", "servicos.html"), (c["name"], path)])])


def build_blog():
    posts = "".join(post_card(a) for a in ARTICLES)
    body = f'''
{page_hero("Blog: dicas de ar-condicionado", "Guias práticos para escolher, instalar e cuidar do seu ar-condicionado na Grande Vitória.", [("Início", "index.html"), ("Blog", "")])}
<section><div class="wrap"><h2 class="sr-only">Todos os artigos</h2><div class="posts">{posts}</div></div></section>
{cta_block()}'''
    render(path="blog.html", title="Blog: Dicas de Ar-Condicionado na Grande Vitória",
           desc="Guias sobre instalação, BTUs, split inverter, maresia e manutenção de ar-condicionado para quem mora na Grande Vitória.",
           body=body, current="blog.html",
           jsonld=[crumbs_ld([("Início", "index.html"), ("Blog", "blog.html")])])


def build_article(a):
    path = f'{a["slug"]}.html'
    secs = "".join(f'<h2>{h}</h2>{t}' for h, t in a["sections"])
    rel = "".join(f'<li><a href="{r["slug"]}.html">{r["title"]}</a></li>'
                  for r in ARTICLES if r["slug"] in a["related"])
    msg = a.get("cta_msg", "Olá! Li um artigo do site e quero um orçamento de instalação de ar-condicionado.")
    body = f'''
{page_hero(a["title"], a["desc"], [("Início", "index.html"), ("Blog", "blog.html"), (a["crumb"], "")])}
<section><div class="wrap art-grid"><article class="prose">
<p class="meta" style="color:var(--n500)">Atualizado em {date.fromisoformat(TODAY).strftime("%d/%m/%Y")} · {a["read"]} min de leitura</p>
{secs}
<div class="inline-cta"><p>{a["cta_title"]}</p><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener noreferrer">{icon("chat")}Falar no WhatsApp</a></div>
<h2>Perguntas frequentes</h2>
{faq_block(a["faq"]).replace(' rv"', '"')}
<h2>Leia também</h2><ul class="related">{rel}</ul>
<div class="note">As informações deste artigo são gerais. Para o seu caso, siga o manual do fabricante do aparelho e peça uma avaliação do local.</div>
</article>
<aside class="art-aside"><h2>Precisa de instalação?</h2><p>Atendemos a Grande Vitória. Peça seu orçamento pelo WhatsApp.</p>
<a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener noreferrer">{icon("chat")}WhatsApp</a>
<a class="btn btn-ghost-dark" href="tel:{PHONE_TEL}">{icon("phone")}Ligar</a></aside></div></section>'''
    article_ld = {
        "@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
        "datePublished": TODAY, "dateModified": TODAY, "inLanguage": "pt-BR",
        "mainEntityOfPage": url(path), "image": url("og-image.jpg"),
        "author": {"@type": "Organization", "name": BRAND}, "publisher": {"@type": "Organization", "name": BRAND},
    }
    render(path=path, title=page_title(a["seo_title"]), desc=a["desc"], body=body, current="blog.html", og_type="article",
           jsonld=[article_ld, faq_ld(a["faq"]),
                   crumbs_ld([("Início", "index.html"), ("Blog", "blog.html"), (a["crumb"], path)])])


def build_faq():
    items = HOME_FAQ + [q for a in ARTICLES[:0] for q in a["faq"]]
    body = f'''
{page_hero("Perguntas frequentes sobre instalação", "Respostas rápidas sobre orçamento, avaliação do local, apartamento, BTUs e manutenção.", [("Início", "index.html"), ("Perguntas", "")])}
<section><div class="wrap">{faq_block(items, search=True)}</div></section>
{cta_block("Não achou sua dúvida?", "Pergunte direto pelo WhatsApp.")}'''
    render(path="faq.html", title="Perguntas Frequentes sobre Ar-Condicionado",
           desc="Dúvidas sobre instalação de ar-condicionado: cidades atendidas, orçamento, avaliação do local, apartamento, BTUs e manutenção.",
           body=body, current="faq.html",
           jsonld=[faq_ld(items), crumbs_ld([("Início", "index.html"), ("Perguntas", "faq.html")])])


def build_contact():
    mail = f'<li>{icon("mail")}<span><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>' if EMAIL else ""
    cities = ", ".join(c["name"] for c in CITIES)
    body = f'''
{page_hero("Contato e orçamento", "Fale com a gente pelo WhatsApp ou preencha os dados abaixo: a mensagem já abre pronta.", [("Início", "index.html"), ("Contato", "")])}
<section><div class="wrap loc"><div>
<h2>Fale com a {BRAND}</h2>
<ul class="info">
<li>{icon("chat")}<span><b>WhatsApp</b><br><a href="{wa("Olá! Quero um orçamento de instalação de ar-condicionado.")}" target="_blank" rel="noopener noreferrer">Chamar agora</a></span></li>
<li>{icon("phone")}<span><b>Telefone</b><br><a href="tel:{PHONE_TEL}">{PHONE_SHOW}</a></span></li>
<li>{icon("pin")}<span><b>Onde atendemos</b><br>{cities}.</span></li>{mail}
</ul>
<p>O orçamento é feito depois da avaliação do local, para o valor refletir o que o seu imóvel realmente precisa.</p></div>
<form class="form" id="form-orcamento" data-wa="{WA_NUMBER}">
<h2 style="font-size:1.3rem">Peça seu orçamento</h2>
<label>Seu nome<input name="nome" required autocomplete="name"></label>
<label>Cidade e bairro<input name="cidade" required placeholder="Ex.: Vila Velha, Itapuã"></label>
<label>Tipo de imóvel<select name="imovel"><option>Apartamento</option><option>Casa</option><option>Outro</option></select></label>
<label>Quantos aparelhos?<select name="qtd"><option>1</option><option>2</option><option>3</option><option>4 ou mais</option></select></label>
<label>Observações (opcional)<input name="obs"></label>
<button class="btn btn-wa btn-lg" type="submit">{icon("chat")}Enviar pelo WhatsApp</button>
<small>Ao enviar, o WhatsApp abre com a mensagem pronta. Nada é salvo neste site.</small>
</form></div></section>'''
    render(path="contato.html", title="Contato e Orçamento de Instalação de Ar-Condicionado",
           desc="Peça orçamento de instalação de ar-condicionado na Grande Vitória pelo WhatsApp ou preencha o formulário rápido.",
           body=body, current="contato.html",
           jsonld=[business_ld(), crumbs_ld([("Início", "index.html"), ("Contato", "contato.html")])])


# ----------------------------------------------------------------------------
# Arquivos técnicos
# ----------------------------------------------------------------------------
def write(name, text):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(text)


def build_tech():
    urls = "".join(
        f"<url><loc>{url('' if p == 'index.html' else p)}</loc><lastmod>{d}</lastmod></url>\n" for p, d in PAGES)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    bots = ["GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended", "Bingbot", "CCBot", "anthropic-ai", "OAI-SearchBot", "ChatGPT-User"]
    ia = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots)
    write("robots.txt", "User-agent: *\nAllow: /\nDisallow: /docs/\nDisallow: /design-system/\nDisallow: /src/\nDisallow: /gerador/\n\n" + ia + f"Sitemap: {url('sitemap.xml')}\n")
    svc = "\n".join(f"- [{c['h1']}]({url('instalacao-ar-condicionado-' + c['slug'] + '.html')})" for c in CITIES)
    art = "\n".join(f"- [{a['title']}]({url(a['slug'] + '.html')})" for a in ARTICLES)
    write("llms.txt", f"""# {BRAND}

> Instalação e manutenção de ar-condicionado split na Grande Vitória, Espírito Santo (Brasil). Atendimento em casas e apartamentos, com avaliação do local e orçamento pelo WhatsApp.

## Serviços
- Instalação de ar-condicionado split
- Manutenção preventiva e corretiva
- Orientação para escolher a capacidade (BTUs) e o tipo de aparelho

## Área de atendimento
Vitória, Vila Velha, Serra, Cariacica, Viana e Guarapari (ES).

## Contato
- WhatsApp e telefone: {PHONE_SHOW}
- Site: {url('')}

## Páginas
- [Início]({url('')})
- [Serviços]({url('servicos.html')})
- [Perguntas frequentes]({url('faq.html')})
- [Contato]({url('contato.html')})
{svc}

## Blog
{art}
""")
    write("vercel.json", json.dumps({
        "cleanUrls": False,
        "headers": [{"source": "/(.*)", "headers": [
            {"key": "X-Content-Type-Options", "value": "nosniff"},
            {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
            {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
            {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"},
            {"key": "Strict-Transport-Security", "value": "max-age=31536000; includeSubDomains"}]},
            {"source": "/(.*)\\.(woff2|css|js|svg|jpg|png|webp)", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]}],
    }, indent=2, ensure_ascii=False) + "\n")
    write("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0c3d66"/>'
          '<g transform="translate(8 8) scale(2)" fill="none" stroke="#00d9ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
          + ICONS["snowflake"] + "</g></svg>\n")


def main():
    build_home()
    build_services()
    for c in CITIES:
        build_city(c)
    build_blog()
    for a in ARTICLES:
        build_article(a)
    build_faq()
    build_contact()
    build_tech()
    print(f"{len(PAGES)} páginas geradas.")
    pend = [p for p in PLACEHOLDERS if p.endswith("00000000")]
    if pend:
        print("ATENÇÃO: número de contato ainda é provisório (veja docs/PENDENCIAS.md).")


if __name__ == "__main__":
    main()
