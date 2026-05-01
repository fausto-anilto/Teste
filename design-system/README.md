# 🎨 Design System - Climavitoria

**Sistema de Design Visual Corporativo Profissional**

---

## 📋 Sumário

- [Cores](#cores)
- [Tipografia](#tipografia)
- [Componentes](#componentes)
- [Espaçamento](#espaçamento)
- [Como Usar](#como-usar)
- [Estrutura de Arquivos](#estrutura-de-arquivos)

---

## 🎨 Cores

### Paleta Primária - Azul (Ar Frio)
- **50**: `#f0f9ff` - Backgrounds claros
- **100**: `#e0f2fe` - Hover states
- **300**: `#7dd3fc` - Borders, secondary text
- **500**: `#0ea5e9` - ⭐ **COR PRINCIPAL** - CTAs, elements interativos
- **600**: `#0284c7` - Hover primary
- **700**: `#0369a1` - Active primary
- **900**: `#0c3d66` - Text escuro

### Paleta Secundária - Indigo
- **500**: `#6366f1` - Botões secundários, accents
- **700**: `#4338ca` - Hover secondary

### Status & Feedback
- **Sucesso**: `#10b981` ✅ Verde
- **Aviso**: `#f59e0b` ⚠️ Âmbar
- **Erro**: `#ef4444` ❌ Vermelho
- **Informação**: `#3b82f6` ℹ️ Azul

---

## 📝 Tipografia

### Fonte
- **Display/Headers**: Poppins (bold, semibold)
- **Body**: Inter (regular, medium, semibold)

### Tamanhos

#### Headings (Hierarquia)
```
Display Large  → 3.5rem  (56px) - Hero sections
Display Medium → 3rem    (48px) - Main headers
H1             → 2.25rem (36px) - Títulos principais
H2             → 1.875rem(30px) - Subtítulos
H3             → 1.5rem  (24px) - Seções
H4             → 1.25rem (20px) - Cards
H5             → 1.125rem(18px) - Labels
H6             → 1rem    (16px) - Small titles
```

#### Body Text
```
Large  → 1.125rem (18px) - Destaque em parágrafos
Medium → 1rem     (16px) - Texto padrão ⭐
Small  → 0.875rem (14px) - Descrições secundárias
XSmall → 0.75rem  (12px) - Hints, captions
```

#### Labels
```
Label   → 0.875rem (14px) - Inputs, buttons, tags
Caption → 0.75rem  (12px) - Helper text, timestamps
```

---

## 🔘 Componentes

### 1. Botões

#### Variantes
```html
<!-- Primary (CTA) -->
<button class="btn btn-primary">Solicitar Orçamento</button>

<!-- Secondary -->
<button class="btn btn-secondary">Saiba Mais</button>

<!-- Ghost (Outline) -->
<button class="btn btn-ghost">Contato</button>
```

#### Tamanhos
```html
<button class="btn btn-primary btn-sm">Small</button>
<button class="btn btn-primary">Medium</button>
<button class="btn btn-primary btn-lg">Large</button>
<button class="btn btn-primary btn-full">Full Width</button>
```

#### Estados
```html
<button class="btn btn-primary">Default</button>
<button class="btn btn-primary" disabled>Disabled</button>
```

### 2. Cards

#### Variantes
```html
<!-- Default -->
<div class="card">
  <div class="card-header">
    <div class="card-header-icon">❄️</div>
    <h3 class="card-title">Título</h3>
  </div>
  <div class="card-body">
    <p>Descrição do card...</p>
  </div>
  <div class="card-footer">
    <a href="#">Saiba mais →</a>
  </div>
</div>

<!-- Destaque (Gradient) -->
<div class="card card-primary">...</div>

<!-- Escuro -->
<div class="card card-dark">...</div>

<!-- Sem Sombra -->
<div class="card card-flat">...</div>
```

### 3. Formulários

#### Input
```html
<label class="block text-label font-medium text-gray-700 mb-2">
  Nome
</label>
<input 
  type="text"
  placeholder="João Silva"
  class="w-full px-4 py-3 border border-gray-300 rounded-lg 
           focus:outline-none focus:ring-2 focus:ring-primary-500"
>
```

#### Select
```html
<select class="w-full px-4 py-3 border border-gray-300 rounded-lg 
               focus:outline-none focus:ring-2 focus:ring-primary-500">
  <option>Selecione...</option>
  <option>Opção 1</option>
</select>
```

#### Textarea
```html
<textarea 
  rows="4"
  class="w-full px-4 py-3 border border-gray-300 rounded-lg 
         focus:outline-none focus:ring-2 focus:ring-primary-500"
></textarea>
```

### 4. Navegação

#### Header
```html
<header class="bg-primary-600 text-white">
  <div class="max-w-7xl mx-auto px-6 py-6 flex justify-between items-center">
    <h1 class="text-3xl font-bold">❄️ Climavitoria</h1>
    <nav class="space-x-8">
      <a href="#" class="hover:text-primary-200">Serviços</a>
      <a href="#" class="hover:text-primary-200">Sobre</a>
      <a href="#" class="hover:text-primary-200">Contato</a>
    </nav>
    <button class="btn btn-primary">Orçamento</button>
  </div>
</header>
```

#### Footer
```html
<footer class="bg-gray-900 text-white py-12">
  <div class="max-w-7xl mx-auto px-6">
    <div class="grid grid-cols-3 gap-8">
      <!-- Colunas -->
    </div>
  </div>
</footer>
```

---

## 📏 Espaçamento

### Escala (Base 4px)
```
xs   → 4px  (0.25rem)
sm   → 8px  (0.5rem)
md   → 16px (1rem)
lg   → 24px (1.5rem)
xl   → 32px (2rem)
2xl  → 40px (2.5rem)
3xl  → 48px (3rem)
```

### Uso
```html
<!-- Padding -->
<div class="p-md">Padding medium</div>
<div class="px-lg py-md">Padding customizado</div>

<!-- Margin -->
<div class="mb-xl">Margin bottom extra large</div>
<div class="space-y-lg">Espaço vertical entre filhos</div>

<!-- Gap (Flex/Grid) -->
<div class="flex gap-md">Flex gap</div>
<div class="grid grid-cols-3 gap-lg">Grid gap</div>
```

### Border Radius
```
sm   → 8px   (0.5rem)
md   → 12px  (0.75rem)
lg   → 16px  (1rem)    ⭐ Padrão para cards
xl   → 24px  (1.5rem)
full → 9999px (círculo)
```

---

## 🎯 Como Usar

### 1. Setup Inicial

```bash
# Tailwind já está configurado em tailwind.config.js
# Basta incluir o CDN ou build do Tailwind
```

### 2. Usar Cores do Design System

```html
<!-- Usando classes Tailwind customizadas -->
<div class="bg-primary-500 text-white p-md rounded-lg">
  Elemento com cor primária
</div>

<!-- Hover states -->
<button class="bg-primary-600 hover:bg-primary-700 text-white">
  Botão interativo
</button>
```

### 3. Usar Tipografia

```html
<h1 class="text-h1 font-bold">Título Principal</h1>
<h2 class="text-h2 font-bold">Subtítulo</h2>
<p class="text-body-md">Parágrafo normal</p>
<label class="text-label font-medium">Label</label>
<small class="text-caption">Texto pequeno</small>
```

### 4. Componentes Reutilizáveis

Os componentes estão em `src/components/`:

```html
<!-- Importar ou copiar os estilos -->
<link rel="stylesheet" href="../components/buttons.html">
<link rel="stylesheet" href="../components/cards.html">

<!-- Usar as classes -->
<button class="btn btn-primary">Clique</button>
<div class="card">...</div>
```

### 5. Estrutura de Layout

```html
<!-- Max-width container -->
<div class="max-w-7xl mx-auto px-6">
  <!-- Conteúdo com espaçamento responsivo -->
</div>

<!-- Grid responsivo -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-lg">
  <!-- Itens -->
</div>

<!-- Flex com gap -->
<div class="flex flex-wrap gap-md">
  <!-- Itens -->
</div>
```

---

## 📁 Estrutura de Arquivos

```
.
├── design-system/
│   └── design-system.html       # Documentação visual completa
│
├── src/
│   └── components/
│       ├── buttons.html         # Componentes de botões reutilizáveis
│       └── cards.html           # Componentes de cards reutilizáveis
│
├── tailwind.config.js           # Configuração customizada
│
└── index.html                   # Landing page (usa o Design System)
```

---

## 🔍 Checklist de Uso

Ao criar novos elementos:

- [ ] Usar cores da paleta (primary, secondary, neutral, status)
- [ ] Usar tamanhos de fonte pré-definidos (h1, h2, body-md, etc)
- [ ] Usar escala de espaçamento (p-md, mb-lg, gap-xl, etc)
- [ ] Border radius padrão para cards: `rounded-lg`
- [ ] Transições suave: `transition-colors` ou `transition-all`
- [ ] Focus states em inputs: `focus:ring-2 focus:ring-primary-500`
- [ ] Hover states nos botões e links
- [ ] Shadows para depth: `shadow-md` em cards, `shadow-lg` em hover
- [ ] Responsive design: mobile-first, usar breakpoints (md, lg)
- [ ] Contrastes acessíveis (AA mínimo)

---

## 📊 Tokens de Design

### Cores
```json
{
  "primary": "#0ea5e9",
  "secondary": "#6366f1",
  "success": "#10b981",
  "warning": "#f59e0b",
  "error": "#ef4444"
}
```

### Tipografia
```json
{
  "family-display": "Poppins",
  "family-body": "Inter",
  "size-h1": "2.25rem",
  "size-body": "1rem"
}
```

### Spacing
```json
{
  "space-unit": "4px",
  "space-sm": "8px",
  "space-md": "16px",
  "space-lg": "24px"
}
```

---

## 🚀 Próximos Passos

1. ✅ Design System criado
2. ⏳ Usar Design System na landing page
3. ⏳ Criar componentes adicionais conforme necessário (modais, tooltips, etc)
4. ⏳ Documentação de acessibilidade
5. ⏳ Guia de brand guidelines

---

## 📞 Suporte

Para dúvidas sobre o Design System:
- Consulte `design-system.html` (documentação visual)
- Veja exemplos em `src/components/`
- Revise `tailwind.config.js` para tokens disponíveis

---

**Versão**: 1.0  
**Último update**: 2024-05-01  
**Status**: ✅ Pronto para uso
