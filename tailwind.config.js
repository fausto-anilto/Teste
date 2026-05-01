/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{html,js}",
    "./design-system/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors: {
        // Paleta Primária - Azul + Cyan (Ar Frio)
        primary: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#0ea5e9', // Cor principal
          600: '#0284c7',
          700: '#0369a1',
          800: '#075985',
          900: '#0c3d66',
        },
        
        // Paleta Secundária - Cyan (Complementar)
        secondary: {
          50: '#ecf0ff',
          100: '#e0e7ff',
          200: '#c7d2fe',
          300: '#a5b4fc',
          400: '#818cf8',
          500: '#6366f1', // Secundária
          600: '#4f46e5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
        },

        // Paleta Neutra - Tons de Cinza
        neutral: {
          50: '#f9fafb',
          100: '#f3f4f6',
          200: '#e5e7eb',
          300: '#d1d5db',
          400: '#9ca3af',
          500: '#6b7280',
          600: '#4b5563',
          700: '#374151',
          800: '#1f2937',
          900: '#111827',
        },

        // Paleta de Status
        success: '#10b981',  // Verde
        warning: '#f59e0b',  // Âmbar
        error: '#ef4444',    // Vermelho
        info: '#3b82f6',     // Azul informativo

        // Cores Climavitoria
        brand: {
          light: '#e0f2fe',    // Azul claro (backgrounds)
          main: '#0ea5e9',     // Azul principal
          dark: '#0369a1',     // Azul escuro (hover/active)
          accent: '#00d9ff',   // Cyan vibrante
        },
      },

      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        display: ['Poppins', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },

      fontSize: {
        // Display / Headings
        'display-lg': ['3.5rem', { lineHeight: '1.1', fontWeight: '700' }],
        'display-md': ['3rem', { lineHeight: '1.1', fontWeight: '700' }],
        'display-sm': ['2.5rem', { lineHeight: '1.2', fontWeight: '700' }],

        // Headings
        'h1': ['2.25rem', { lineHeight: '1.2', fontWeight: '700' }],
        'h2': ['1.875rem', { lineHeight: '1.3', fontWeight: '700' }],
        'h3': ['1.5rem', { lineHeight: '1.4', fontWeight: '600' }],
        'h4': ['1.25rem', { lineHeight: '1.5', fontWeight: '600' }],
        'h5': ['1.125rem', { lineHeight: '1.5', fontWeight: '600' }],
        'h6': ['1rem', { lineHeight: '1.5', fontWeight: '600' }],

        // Body
        'body-lg': ['1.125rem', { lineHeight: '1.75' }],
        'body-md': ['1rem', { lineHeight: '1.5' }],
        'body-sm': ['0.875rem', { lineHeight: '1.5' }],
        'body-xs': ['0.75rem', { lineHeight: '1.5' }],

        // Labels & Captions
        'label': ['0.875rem', { lineHeight: '1.5', fontWeight: '500' }],
        'caption': ['0.75rem', { lineHeight: '1.5', fontWeight: '500' }],
      },

      spacing: {
        // Grid 4px
        'xs': '0.25rem',   // 4px
        'sm': '0.5rem',    // 8px
        'md': '1rem',      // 16px
        'lg': '1.5rem',    // 24px
        'xl': '2rem',      // 32px
        '2xl': '2.5rem',   // 40px
        '3xl': '3rem',     // 48px
        '4xl': '3.5rem',   // 56px
        '5xl': '4rem',     // 64px
      },

      borderRadius: {
        'none': '0px',
        'xs': '0.25rem',   // 4px
        'sm': '0.5rem',    // 8px
        'md': '0.75rem',   // 12px
        'lg': '1rem',      // 16px
        'xl': '1.5rem',    // 24px
        'full': '9999px',
      },

      boxShadow: {
        'xs': '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
        'sm': '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
        'md': '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        'lg': '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'xl': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
        '2xl': '0 25px 50px -12px rgba(0, 0, 0, 0.25)',
        'inset': 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
      },

      transitionDuration: {
        'fast': '100ms',
        'base': '200ms',
        'slow': '300ms',
        'slower': '500ms',
      },
    },
  },
  plugins: [],
}
