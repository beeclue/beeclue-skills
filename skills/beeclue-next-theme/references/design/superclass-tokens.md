# 5-Layer Superclass Token Architecture for Next.js & Tailwind

To guarantee architectural consistency from Brand DNA down to the smallest interactive button, all visual variables are codified across 5 strict mathematical layers.

> [!IMPORTANT]
> **Strict CSS Syntax Rule**: Always format CSS units directly without spaces (e.g., `2.5rem`, `16px`, `150ms`, `100%`). Never write `2.5 rem`, `16 px`, or `150 ms`.

---

## 1. The 5-Layer Hierarchy

```
Layer 0: Brand DNA Vectors (0-100 normalized mathematical coordinates)
  │
Layer 1: Design Primitives (Hex color values, raw font families, base scales)
  │
Layer 2: Semantics (Contextual tokens: background, surface, text, border, action)
  │
Layer 3: Component Tokens (Navbar height, card radius, button padding, drawer width)
  │
Layer 4: Experience Tokens (Section spacing, spring curves, micro-hover scales)
```

---

## 2. Production CSS Token Implementation (`src/app/globals.css`)

```css
:root {
  /* ==========================================================================
     LAYER 0: BRAND DNA VECTORS
     ========================================================================== */
  --brand-dna-luxury: 85;
  --brand-dna-minimalism: 90;
  --brand-dna-architectural: 80;

  /* ==========================================================================
     LAYER 1: PRIMITIVES
     ========================================================================== */
  --primitive-white: #ffffff;
  --primitive-black: #09090b;
  --primitive-slate-50: #f8fafc;
  --primitive-slate-100: #f1f5f9;
  --primitive-slate-200: #e2e8f0;
  --primitive-slate-800: #1e293b;
  --primitive-slate-900: #0f172a;
  --primitive-blue-apple: #0071e3;
  --primitive-blue-apple-hover: #0077ed;

  /* Raw Font Stacks */
  --primitive-font-sans: var(--font-geist-sans), -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --primitive-font-mono: var(--font-geist-mono), ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  --primitive-font-editorial: var(--font-editorial-serif), "Cormorant Garamond", Georgia, serif;

  /* ==========================================================================
     LAYER 2: SEMANTICS (LIGHT MODE)
     ========================================================================== */
  --color-canvas: var(--primitive-slate-50);
  --color-surface: var(--primitive-white);
  --color-surface-hover: #fafafa;
  --color-text-primary: var(--primitive-slate-900);
  --color-text-secondary: #64748b;
  --color-text-tertiary: #94a3b8;
  --color-border-subtle: rgba(15, 23, 42, 0.08);
  --color-border-focus: var(--primitive-blue-apple);
  --color-action-primary: var(--primitive-blue-apple);
  --color-action-primary-hover: var(--primitive-blue-apple-hover);
  --color-action-text: var(--primitive-white);

  /* Fluid Typography Clamps */
  --text-hero: clamp(2.5rem, 5vw + 1rem, 5.25rem);
  --text-section-title: clamp(2rem, 3.5vw + 0.5rem, 3.75rem);
  --text-subsection-title: clamp(1.5rem, 2vw + 0.25rem, 2.25rem);
  --text-body-large: clamp(1.125rem, 1.25vw, 1.25rem);
  --text-body: clamp(0.938rem, 1vw, 1.063rem);
  --text-caption: clamp(0.75rem, 0.8vw, 0.875rem);

  /* ==========================================================================
     LAYER 3: COMPONENT SPECIFICATIONS
     ========================================================================== */
  --nav-height: 4.25rem;
  --card-radius: 1.25rem;
  --button-radius: 9999px;
  --card-padding: clamp(1.5rem, 3vw, 2.5rem);
  --bento-gap: clamp(1rem, 2vw, 1.5rem);

  /* ==========================================================================
     LAYER 4: EXPERIENCE & MOTION TOKENS
     ========================================================================== */
  --section-padding-y: clamp(5rem, 10vw, 10rem);
  --container-max-width: 80rem;
  --spring-duration-fast: 200ms;
  --spring-duration-base: 400ms;
  --spring-ease-apple: cubic-bezier(0.16, 1, 0.3, 1);
  --shadow-apple-ambient: 0 1px 2px 0 rgba(0, 0, 0, 0.04);
  --shadow-apple-elevated: 0 12px 32px -8px rgba(0, 0, 0, 0.08);
}

/* ==========================================================================
   DARK MODE OVERRIDES (AUTOMATIC OR CLASS-BASED)
   ========================================================================== */
@media (prefers-color-scheme: dark) {
  :root {
    --color-canvas: #09090b;
    --color-surface: #121215;
    --color-surface-hover: #1a1a1f;
    --color-text-primary: #f8fafc;
    --color-text-secondary: #94a3b8;
    --color-text-tertiary: #64748b;
    --color-border-subtle: rgba(255, 255, 255, 0.08);
    --shadow-apple-ambient: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
    --shadow-apple-elevated: 0 12px 32px -8px rgba(0, 0, 0, 0.6);
  }
}
```
