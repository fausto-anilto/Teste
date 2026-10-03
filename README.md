# Vitória Clima

Site institucional estático para ranqueamento local (SEO, AEO e GEO) de **instalação de ar-condicionado na Grande Vitória (ES)**. HTML, CSS e JS puros, estrutura plana, sem build de front-end.

## Nomes padronizados

| Uso | Nome |
|---|---|
| Marca (texto na tela, schema, títulos) | **Vitória Clima** |
| Identificador técnico (prefixo do rastreamento, código de referência) | `vc` / `VC` (ex.: `VC_TRACKING`, `ref. VC-7K3Q9`) |
| Páginas de cidade | `instalacao-ar-condicionado-<cidade>.html` |
| Artigos | `<assunto-em-minusculas-com-hifens>.html` |
| Gerador | `gerador/build.py` (layout e páginas) e `gerador/articles.py` (artigos) |

A marca antiga "Climavitoria" foi substituída em todo o projeto, inclusive no design system.

## Estrutura

```
index.html, servicos.html, faq.html, contato.html, blog.html
instalacao-ar-condicionado-{vitoria,vila-velha,serra,cariacica,viana,guarapari}.html
<8 artigos>.html
style.css, script.js, *.woff2        # visual, comportamento e fontes locais
tracking.js, tracking-config.js      # rastreamento pronto e DESLIGADO
robots.txt, sitemap.xml, llms.txt, vercel.json, favicon.svg, og-image.jpg
gerador/                             # build.py + articles.py
docs/                                # PENDENCIAS.md, RASTREAMENTO.md, coletor-apps-script.gs
design-system/, src/, tailwind.config.js   # documentação visual (tokens usados no style.css)
```

## Como atualizar

1. Edite os dados de contato e o domínio no bloco `CONFIG` de `gerador/build.py`, ou o conteúdo em `gerador/articles.py`.
2. Rode `python3 gerador/build.py`. Ele reescreve todas as páginas, `sitemap.xml`, `robots.txt`, `llms.txt` e `vercel.json`.
3. Confira `docs/PENDENCIAS.md` antes de publicar.

Não edite os `.html` gerados à mão: a próxima execução do gerador sobrescreve.

## Efeitos visuais e bibliotecas

Tudo em CSS/JS próprio, sem bibliotecas externas e sem CDN (melhor para velocidade e SEO): fundo animado no hero, linhas de fluxo de ar em SVG, faixa de cidades em movimento contínuo, ondas no rodapé, revelar ao rolar, inclinação leve nos cartões. Com "reduzir animações" ativo no sistema, o que é brusco é desligado e o fundo continua lento.

## Rastreamento

Pronto e desligado. Para ligar, preencha só `tracking-config.js`. Passo a passo em `docs/RASTREAMENTO.md`.
