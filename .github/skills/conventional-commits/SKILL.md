---
name: conventional-commits
description: "Guia para escrever mensagens de commit seguindo Conventional Commits v1.0.0. Use quando: precisar escrever uma mensagem de commit com formato padronizado, validar commits ou aprender a estrutura correta."
---

# Conventional Commits — Guia Prático

Use essa skill para escrever mensagens de commit claras, estruturadas e automaticamente interpretáveis, seguindo a especificação **Conventional Commits 1.0.0**.

## Por Que Usar?

✅ **CHANGELOG automatizado** — Ferramentas geram automaticamente CHANGELOGs a partir dos commits  
✅ **Versionamento semântico automático** — Sistema determina MAJOR, MINOR, PATCH automaticamente  
✅ **Histórico legível** — Commits estruturados facilitam entender o que mudou e por quê  
✅ **Integração com CI/CD** — Pipelines podem disparar deploy/release baseado no tipo de commit  
✅ **Colaboração melhor** — Toda a equipe usa o mesmo padrão

---

## Estrutura Básica

```
<tipo>[escopo]: <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]
```

### Elementos

| Elemento | Obrigatório? | Descrição |
|----------|------------|-----------|
| **tipo** | ✅ Sim | `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore` |
| **escopo** | ❌ Não | Seção do código alterada (entre parênteses): `feat(auth): ...` |
| **`!`** | ❌ Não | Indica breaking change: `feat!: ...` ou `feat(api)!: ...` |
| **descrição** | ✅ Sim | Resumo em imperativo (máx. ~50 caracteres) |
| **corpo** | ❌ Não | Detalhes após linha em branco (várias linhas OK) |
| **rodapé** | ❌ Não | Metadados: `Refs: #123`, `BREAKING CHANGE: ...`, etc |

---

## Tipos de Commit

### 🎯 Principais

| Tipo | Uso | Semver | Exemplo |
|------|-----|--------|---------|
| **feat** | Novo recurso | MINOR ↑ | `feat(auth): adiciona autenticação OAuth 2.0` |
| **fix** | Correção de bug | PATCH ↑ | `fix(parser): corrige erro ao parsear arrays vazios` |
| **BREAKING CHANGE** | Quebra compatibilidade | MAJOR ↑ | `feat!: remove suporte para Node 6` |

### 📚 Complementares

| Tipo | Descrição | Semver |
|------|-----------|--------|
| `docs` | Alterações em documentação | — |
| `style` | Formatting, pontuação, espaços (não afeta lógica) | — |
| `refactor` | Reescreve código sem mudar comportamento | — |
| `perf` | Melhoria de performance | PATCH |
| `test` | Adiciona/altera testes | — |
| `build` | Altera sistema de build, deps, versioning | — |
| `ci` | Altera CI/CD, workflows, scripts | — |
| `chore` | Manutenção, atualizações (npm, config) | — |
| `revert` | Reverte um commit anterior | — |

---

## 📋 Checklist: Escreva Seu Commit

### Passo 1: Escolha o Tipo
```
Você está:
□ Adicionando novo recurso?          → feat
□ Corrigindo bug?                    → fix
□ Só atualizando docs?               → docs
□ Reformatando código?               → style
□ Refatorando (sem mudar função)?    → refactor
□ Melhorando performance?            → perf
□ Adicionando testes?                → test
□ Alterando build/deps?              → build ou chore
```

### Passo 2: Identifique o Escopo (Opcional)
```
Qual parte do código muda?
Exemplos: auth, parser, api, ui, database, config
Deixe em branco se não se aplica.

Seu escopo: (        )
```

### Passo 3: Escreva a Descrição
```
Regras:
✓ Use imperativo: "add", "fix", "update" (não "added", "fixed")
✓ Não capitalize a primeira letra
✓ Sem ponto final
✓ Máximo ~50 caracteres

Sua descrição: "                                                "
```

### Passo 4: Tem Breaking Change?
```
Sua mudança quebra compatibilidade? (sim/não)

Se SIM:
  □ Adicione ! após o tipo/escopo: feat(api)!: ...
  □ SEMPRE inclua no rodapé: BREAKING CHANGE: <descrição>

Se NÃO:
  □ Continue para o corpo (opcional)
```

### Passo 5: Corpo (Opcional, Mas Recomendado)
```
Contexto:
  - Qual era o problema?
  - Por que essa solução?
  - Há alternativas consideradas?

Máximo: Sem limite, mas seja conciso.
```

### Passo 6: Rodapés (Opcional)
```
Formatos comuns:

Refs: #123, #456           (referencia issues)
Reviewed-by: João Silva    (revisor)
Fixes: #789                (fecha issue)
Closes: #790               (fecha PR)
BREAKING CHANGE: <desc>    (para breaking changes)

Exemplo completo:
Refs: #123
Reviewed-by: Maria
```

---

## 🎨 Exemplos Prontos

### Exemplo 1: Feature Simples
```
feat: adiciona validação de email

Implementa regex para validar formato de email antes de enviar para o backend.
Reduz requisições inválidas em 30%.

Refs: #145
```
**Análise:** tipo=`feat`, escopo=nenhum, tem corpo e rodapé ✅

---

### Exemplo 2: Fix com Escopo
```
fix(auth): corrige timeout na renovação de token

O token expirava sem renovar quando a janela estava inativa por >5 min.
Agora verifica a expiração a cada 2 min.

Fixes: #234
```
**Análise:** tipo=`fix`, escopo=`auth`, breaking=não ✅

---

### Exemplo 3: Breaking Change
```
feat(api)!: remove endpoint POST /v1/users

Use POST /v2/users com novo schema de resposta.

BREAKING CHANGE: endpoint legado /v1/users foi removido.
Migre para /v2/users que retorna { user_id, created_at } ao invés de { id, timestamp }.

Refs: #567
```
**Análise:** tipo=`feat`, escopo=`api`, breaking=SIM (! + BREAKING CHANGE) ✅

---

### Exemplo 4: Doc
```
docs: atualiza README com passos de instalação
```
**Análise:** tipo=`docs`, simples, sem corpo ✅

---

### Exemplo 5: Refactor
```
refactor: extrai validação de email em função reutilizável

Sem mudança de comportamento. Facilita testes e reutilização.
```
**Análise:** tipo=`refactor`, objetivo claro ✅

---

## ❌ Padrões de Erro Comuns

### ❌ Erro 1: Tipo Inválido
```
ERRADO: bugfix: corrige login
CERTO:  fix: corrige erro no login
```
→ Use só tipos reconhecidos: `feat`, `fix`, `docs`, etc.

---

### ❌ Erro 2: Descrição Capitalizada com Ponto
```
ERRADO: feat: Adiciona novo filtro.
CERTO:  feat: adiciona novo filtro
```
→ Imperativo, minúsculo, sem ponto

---

### ❌ Erro 3: Breaking Change Sem Marcação
```
ERRADO: feat(db): muda schema de users
           (não sinaliza breaking change)

CERTO:  feat(db)!: muda schema de users
           BREAKING CHANGE: coluna 'email' foi renomeada para 'user_email'
```
→ Use `!` e `BREAKING CHANGE:` sempre para mudanças que quebram compatibilidade

---

### ❌ Erro 4: Escopo com Espaços
```
ERRADO: feat(user auth): novo sistema
CERTO:  feat(auth): novo sistema
```
→ Escopo é uma palavra, sem espaços. Use kebab-case se precisa: `feat(user-auth)`

---

### ❌ Erro 5: Múltiplas Mudanças em Um Commit
```
ERRADO: feat: adiciona validação E corrige bug do login E refatora parser
```
→ Faça commits separados. Um tipo de mudança por commit.

---

## ✅ Validação: Seu Commit Passou?

Responda:

1. **Formato?** `tipo[escopo]: descrição` ✓/✗
2. **Tipo válido?** Está em nossa lista? ✓/✗
3. **Descrição?** Imperativo, minúsculo, sem ponto? ✓/✗
4. **Escopo (se presente)?** Sem espaços, entre parênteses? ✓/✗
5. **Breaking change?** Se sim, tem `!` + `BREAKING CHANGE:`? ✓/✗
6. **Corpo (se presente)?** Após linha em branco? ✓/✗
7. **Rodapé (se presente)?** Formato `Token: valor`? ✓/✗
8. **Uma mudança?** Ou misturou vários tipos? ✓/✗

Se todas são **✓**, seu commit está pronto! 🎉

---

## 🔗 Recursos

- **Especificação oficial:** https://www.conventionalcommits.org/pt-br/v1.0.0/
- **SemVer (versionamento):** https://semver.org/lang/pt-BR/
- **Commitlint (validação):** https://commitlint.js.org/
- **Git Trailer Format:** https://git-scm.com/docs/git-interpret-trailers

---

## 💡 Dicas Práticas

1. **Use imperativos:** "add", "fix", "update", "remove" (como se a pessoa estivesse dando ordem ao código)
2. **Complete a frase:** "Se aplicado, este commit irá: ____" → a descrição deve encaixar
3. **Escopo = contexto:** Facilita buscar commits por áreas (ex: `git log --grep="(auth)"`)
4. **Corpo = justificativa:** Explique POR QUÊ (não O QUÊ, que já está na descrição)
5. **Breaking changes = aviso vermelho:** Sempre sinalizar com `!` no tipo/escopo
6. **Commits pequenos:** Mais fácil de revisar, entender e reverter se necessário

---

## 🤖 Próximos Passos

Depois de dominar Conventional Commits:
- Configure **commitlint** para validar automaticamente
- Configure **husky** para rejeitar commits inválidos localmente
- Configure **conventional-changelog** para gerar CHANGELOG automaticamente
- Atualize seu workflow de versioning para usar SemVer

