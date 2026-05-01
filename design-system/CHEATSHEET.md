# 📚 Guia de Referência Rápida — Design System Climavitoria

## 🎨 Cores Principais

```html
<!-- Primária -->
bg-primary-500    #0ea5e9   (⭐ Cor principal)
bg-primary-600    #0284c7   (Hover)
bg-primary-700    #0369a1   (Active)
bg-primary-50     #f0f9ff   (Background claro)

<!-- Secundária -->
bg-secondary-500  #6366f1   (Complementar)
bg-secondary-700  #4338ca   (Hover)

<!-- Status -->
bg-green-500      #10b981   (Sucesso)
bg-amber-500      #f59e0b   (Aviso)
bg-red-500        #ef4444   (Erro)
bg-blue-500       #3b82f6   (Info)
```

## 📝 Tipografia

```html
<!-- Headings -->
<h1 class="text-h1 font-bold">2.25rem — Título Principal</h1>
<h2 class="text-h2 font-bold">1.875rem — Subtítulo</h2>
<h3 class="text-h3 font-semibold">1.5rem — Seção</h3>
<h4 class="text-h4 font-semibold">1.25rem — Card</h4>

<!-- Body -->
<p class="text-body-md">1rem — Texto Padrão</p>
<small class="text-body-sm">0.875rem — Texto Pequeno</small>
<label class="text-label font-medium">0.875rem — Label</label>
<caption class="text-caption">0.75rem — Caption</caption>

<!-- Fontes -->
font-family: 'Poppins'  → Headings (bold, semibold)
font-family: 'Inter'    → Body (regular, medium, semibold)
```

## 🔘 Botões

```html
<!-- Variantes -->
<button class="btn btn-primary">CTA Principal</button>
<button class="btn btn-secondary">Secundário</button>
<button class="btn btn-ghost">Ghost/Outline</button>

<!-- Tamanhos -->
<button class="btn btn-sm">Small</button>
<button class="btn">Medium (padrão)</button>
<button class="btn btn-lg">Large</button>
<button class="btn btn-full">Full Width</button>

<!-- Classes CSS -->
.btn-primary {
  background: #0ea5e9;
  hover: #0284c7;
  color: white;
}

.btn-secondary {
  background: #e0f2fe;
  border: 1px solid #7dd3fc;
  color: #0369a1;
}

.btn-ghost {
  border: 2px solid #0ea5e9;
  color: #0ea5e9;
  background: transparent;
}
```

## 🎁 Cards

```html
<!-- Estrutura básica -->
<div class="card">
  <div class="card-header">
    <div class="card-header-icon">❄️</div>
    <h3 class="card-title">Título</h3>
  </div>
  <div class="card-body">
    <p>Descrição...</p>
  </div>
  <div class="card-footer">
    <a href="#">Link →</a>
  </div>
</div>

<!-- Variantes -->
<div class="card">...</div>                    <!-- Default -->
<div class="card card-primary">...</div>      <!-- Gradient azul -->
<div class="card card-dark">...</div>         <!-- Escuro -->
<div class="card card-flat">...</div>         <!-- Sem sombra -->

<!-- Propriedades -->
border-radius: 1rem (16px)
padding: 1.5rem (24px)
box-shadow: md (hover: lg)
transition: all 0.3s
```

## 📋 Formulários

```html
<!-- Input Base -->
<input 
  type="text"
  class="w-full px-4 py-3 border border-gray-300 rounded-lg 
         focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
>

<!-- Select -->
<select class="w-full px-4 py-3 border border-gray-300 rounded-lg 
               focus:outline-none focus:ring-2 focus:ring-primary-500">
  <option>Opção</option>
</select>

<!-- Textarea -->
<textarea 
  class="w-full px-4 py-3 border border-gray-300 rounded-lg 
         focus:outline-none focus:ring-2 focus:ring-primary-500"
></textarea>

<!-- Checkbox -->
<input type="checkbox" class="w-5 h-5 text-primary-600 border-gray-300">

<!-- Estados -->
focus:          ring-2 ring-primary-500 border-transparent
disabled:       opacity-50 cursor-not-allowed
error:          border-red-500 ring-red-500
success:        border-green-500 ring-green-500
```

## 📏 Espaçamento

```html
<!-- Padding -->
p-xs  p-sm  p-md  p-lg  p-xl  p-2xl  p-3xl
px-md py-lg                              /* X e Y separados */

<!-- Margin -->
m-xs  m-sm  m-md  m-lg  m-xl  m-2xl
mb-lg mt-sm                             /* Vertical/Horizontal */

<!-- Gap (Flex/Grid) -->
gap-xs  gap-sm  gap-md  gap-lg  gap-xl

<!-- Space Between -->
space-y-md  space-x-lg                  /* Espaço entre filhos */

<!-- Mapa de valores -->
xs   → 4px   (0.25rem)
sm   → 8px   (0.5rem)
md   → 16px  (1rem)
lg   → 24px  (1.5rem)
xl   → 32px  (2rem)
2xl  → 40px  (2.5rem)
3xl  → 48px  (3rem)
```

## 🧭 Navegação

```html
<!-- Header -->
<header class="bg-primary-600 text-white sticky top-0">
  <div class="max-w-7xl mx-auto px-6 py-6 flex justify-between items-center">
    <h1 class="text-3xl font-bold">Logo</h1>
    <nav class="flex space-x-8">
      <a href="#" class="hover:text-primary-200">Link</a>
    </nav>
    <button class="btn btn-primary">CTA</button>
  </div>
</header>

<!-- Footer -->
<footer class="bg-gray-900 text-white py-12">
  <div class="max-w-7xl mx-auto px-6">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
      <!-- Colunas -->
    </div>
  </div>
</footer>
```

## 📐 Layout Responsivo

```html
<!-- Container -->
<div class="max-w-7xl mx-auto px-6">Conteúdo</div>

<!-- Grid Responsivo -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-lg">
  <!-- Itens: 1 coluna mobile, 2 em tablet, 3 em desktop -->
</div>

<!-- Flex com wrapping -->
<div class="flex flex-wrap gap-md">
  <!-- Itens quebram em múltiplas linhas -->
</div>

<!-- Grid com Tailwind -->
grid-cols-1, grid-cols-2, grid-cols-3, ... grid-cols-12
md:grid-cols-2, lg:grid-cols-3                /* Breakpoints -->
gap-sm, gap-md, gap-lg                         /* Gaps -->

<!-- Breakpoints -->
sm  → 640px
md  → 768px   (padrão para tablet)
lg  → 1024px  (padrão para desktop)
xl  → 1280px
2xl → 1536px
```

## 🎯 Border Radius

```html
rounded-sm    → 8px   (0.5rem)
rounded-md    → 12px  (0.75rem)
rounded-lg    → 16px  (1rem)    ⭐ Padrão para cards
rounded-xl    → 24px  (1.5rem)
rounded-full  → 9999px (círculo)
```

## ✨ Efeitos

```html
<!-- Shadows -->
shadow-sm   shadow-md   shadow-lg   shadow-xl   shadow-2xl
hover:shadow-lg                                 /* Hover effect -->

<!-- Transitions -->
transition-colors    /* Cor suave */
transition-all       /* Tudo suave */
duration-200         /* 200ms (padrão) */
ease-in-out          /* Timing function -->

<!-- Opacity -->
opacity-50  opacity-75  opacity-100
hover:opacity-80                     /* Hover state -->

<!-- Transform -->
hover:scale-105     /* Zoom on hover */
group-hover:scale-105  /* Zoom quando parent é hoverado -->
```

## 🔗 Uso em HTML

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700&display=swap');
    
    body { font-family: 'Inter', sans-serif; }
    h1, h2, h3, h4, h5, h6 { font-family: 'Poppins', sans-serif; }
  </style>
</head>
<body class="bg-gray-50">
  <!-- Seu conteúdo aqui -->
</body>
</html>
```

## 📁 Arquivos Importantes

```
design-system/
├── design-system.html     → Documentação visual completa
├── exemplo-uso.html       → Exemplo prático full page
├── README.md              → Documentação completa
└── CHEATSHEET.md          → Este arquivo

tailwind.config.js         → Configuração customizada
src/components/
├── buttons.html           → Componentes de botões
└── cards.html             → Componentes de cards
```

## ✅ Checklist ao Criar

- [ ] Usar cores da paleta (primary, secondary, status)
- [ ] Usar tamanhos de fonte pré-definidos
- [ ] Usar escala de espaçamento (não valores aleatórios)
- [ ] Border radius: rounded-lg para cards
- [ ] Transições suaves: transition-colors
- [ ] Focus states: focus:ring-2 focus:ring-primary-500
- [ ] Hover states em botões e links
- [ ] Shadows para depth: shadow-md, shadow-lg
- [ ] Responsive design: mobile-first
- [ ] Acessibilidade: contraste AA mínimo

## 🚀 Quick Start

```html
<!-- Hero Section -->
<section class="bg-gradient-to-b from-primary-50 to-white py-20">
  <div class="max-w-7xl mx-auto px-6 text-center">
    <h1 class="text-5xl font-bold text-gray-900 mb-6">Título</h1>
    <p class="text-xl text-gray-600 mb-8">Descrição</p>
    <button class="btn btn-primary">CTA</button>
  </div>
</section>

<!-- Cards Grid -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-6">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="card">...</div>
      <div class="card">...</div>
      <div class="card">...</div>
    </div>
  </div>
</section>

<!-- Contact Form -->
<form class="space-y-6 max-w-2xl">
  <div>
    <label class="block text-label font-medium mb-2">Campo</label>
    <input type="text" class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500">
  </div>
  <button type="submit" class="btn btn-primary w-full">Enviar</button>
</form>
```

---

**Versão**: 1.0  
**Status**: ✅ Pronto para usar  
**Próximo**: Veja `exemplo-uso.html` para exemplo completo
