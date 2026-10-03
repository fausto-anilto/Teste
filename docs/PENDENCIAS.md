# Pendências — Vitória Clima

Itens que dependem de confirmação do cliente antes de publicar. Os valores provisórios ficam no topo de `gerador/build.py` (bloco `CONFIG`); depois de alterar, rode `python3 gerador/build.py`.

## Obrigatórios antes de publicar

| Item | Situação atual | Onde trocar |
|---|---|---|
| WhatsApp | número provisório `5527900000000` | `WA_NUMBER` |
| Telefone | provisório `(27) 90000-0000` | `PHONE_TEL`, `PHONE_SHOW` |
| Domínio | provisório `https://vitoriaclima.com.br` | `DOMAIN` (afeta canonical, sitemap, schema, Open Graph) |
| E-mail | não exibido | `EMAIL` (vazio = não aparece) |
| Nome da marca | "Vitória Clima" em todo o projeto (antes: "Climavitoria") | `BRAND` e `design-system/` |

## Conteúdo a validar com o cliente

- **Diferenciais.** A versão antiga citava "10 anos de experiência", "atendimento 24/7", "economia de até 40%", "garantia estendida" e "melhor preço". Nada disso foi mantido porque não há comprovação. Se forem verdadeiros, inclua de volta com dados que o cliente possa comprovar.
- **Avaliação gratuita do local.** Veio da versão antiga do site e aparece no FAQ e nos artigos. Confirmar.
- **Garantia do serviço.** Não há texto de garantia no site. Se houver prazo e condições, criar uma seção.
- **Bairros atendidos.** As listas de cada cidade são exemplos de bairros reais da região, não uma lista fornecida pelo cliente. Pedir a lista de bairros efetivamente atendidos.
- **Cidades.** Foram usadas Vitória, Vila Velha, Serra, Cariacica, Viana e Guarapari. Confirmar se atende também Fundão e outras.
- **Atendimento a comércio.** O site fala só em casas e apartamentos (a versão antiga dizia "residencial").
- **Horário de atendimento e endereço.** Não informados, por isso não aparecem. Se houver endereço fixo, adicionar ao schema `HVACBusiness` e criar a seção de mapa.
- **Fotos reais de instalações.** Não há fotos. Fotos reais do cliente valem mais que banco de imagens (sem imagem de banco no projeto).
- **Página de política de privacidade** com revisão jurídica, necessária para ligar o rastreamento (`PRIVACY_URL` em `tracking-config.js`).

## Para ranquear (fora do site)

1. Criar/ajustar o **Perfil da Empresa no Google** com categoria "Instalador de ar-condicionado", áreas de atendimento e telefone iguais aos do site.
2. Pedir **avaliações reais** de clientes atendidos.
3. Cadastrar o domínio no **Google Search Console** e enviar `sitemap.xml`.
4. Manter **nome, telefone e cidade iguais** em todos os cadastros.
5. Testar a velocidade no celular (PageSpeed Insights) depois de publicar.
6. Publicar um artigo novo por mês com o gerador.

## Observações técnicas

- Domínio com acento (IDN), se for usado: nas tags técnicas, usar a forma punycode (`xn--...`).
- `llms.txt` é inofensivo, mas não há evidência sólida de que as IAs o usem. O que move o ranking local é o conjunto acima.
- `docs/` e `gerador/` estão bloqueados no `robots.txt`, mas são arquivos públicos se o repositório for publicado na Vercel. Não coloque dados sensíveis neles.
