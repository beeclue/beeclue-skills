# 5-Layer Superclass Design Token Architecture

The BeeClue token architecture organizes CSS Custom Properties into a rigorous **5-Layer Hierarchy**, bridging business strategy directly to pixel-perfect styling.

---

## 1. The 5-Layer Token Hierarchy

```
Layer 0: Brand DNA           (Normalized 0-100 strategic coordinates)
   │
   ▼
Layer 1: Primitives          (Raw hex values, base clamp scales, font families)
   │
   ▼
Layer 2: Semantics           (Role-based aliases: surface, text, action, border)
   │
   ▼
Layer 3: Components          (Scoped widget parameters: product-card, cart-drawer, sticky-bar)
   │
   ▼
Layer 4: Experience Tokens   (Macro page rhythm, section spacing, density, editorial cadence)
```

---

## 2. Production CSS Tokens Template

> [!IMPORTANT]
> **Strict CSS Formatting Rule**: All CSS units MUST be formatted without whitespace between number and unit (e.g., `2.5rem`, `16px`, `150ms`, `0.15em`). Never emit invalid syntax like `2.5 rem`, `16 px`, or `150 ms`.

```css
:root {
    /* ═════════════════════════════════════════════════════════════
       LAYER 0: BRAND DNA (Strategic Metadata Variables)
       ═════════════════════════════════════════════════════════════ */
    --brand-dna-luxury:         85;
    --brand-dna-minimalism:     80;
    --brand-dna-warmth:         75;
    --brand-dna-editorial:      85;

    /* ═════════════════════════════════════════════════════════════
       LAYER 1: PRIMITIVES (Raw Unaliased Values)
       ═════════════════════════════════════════════════════════════ */
    /* Color Palette */
    --primitive-neutral-0:      #ffffff;
    --primitive-neutral-50:     #f7f4ef; /* Warm Alabaster */
    --primitive-neutral-100:    #eeebe4;
    --primitive-neutral-200:    #e0dcd4;
    --primitive-neutral-400:    #9e9a92;
    --primitive-neutral-600:    #5c5852;
    --primitive-neutral-900:    #1b1816; /* Deep Espresso Charcoal */

    --primitive-brand-500:      #2b333a; /* Core Brand Neutral */
    --primitive-brand-700:      #1c2227;

    --primitive-accent-500:     #c8602a; /* Terracotta */
    --primitive-accent-600:     #b25220;

    /* Raw Typography */
    --primitive-font-heading:   'Cormorant Garamond', Georgia, serif;
    --primitive-font-body:      'Plus Jakarta Sans', system-ui, sans-serif;
    --primitive-font-mono:      ui-monospace, 'JetBrains Mono', monospace;

    /* ═════════════════════════════════════════════════════════════
       LAYER 2: SEMANTICS (Intent & Purpose-Driven)
       ═════════════════════════════════════════════════════════════ */
    /* Surfaces */
    --color-bg:                 var(--primitive-neutral-50);
    --color-surface-base:       var(--primitive-neutral-0);
    --color-surface-sunken:     var(--primitive-neutral-100);
    --color-surface-overlay:    rgba(27, 24, 22, 0.45);

    /* Text & Ink */
    --color-text-primary:       var(--primitive-neutral-900);
    --color-text-secondary:     var(--primitive-neutral-600);
    --color-text-tertiary:      var(--primitive-neutral-400);
    --color-text-inverse:       var(--primitive-neutral-0);

    /* Actions & Interactions */
    --color-action-primary:       var(--primitive-accent-500);
    --color-action-primary-hover: var(--primitive-accent-600);
    --color-action-secondary:     var(--primitive-brand-500);

    /* Borders */
    --color-border-subtle:      var(--primitive-neutral-200);
    --color-border-strong:      var(--primitive-neutral-400);
    --color-border-focus:       var(--primitive-accent-500);

    /* Radii & Shadows */
    --radius-sm:                4px;
    --radius-md:                8px;
    --radius-lg:                16px;
    --radius-full:              9999px;

    --shadow-subtle:            0 1px 3px rgba(0, 0, 0, 0.04);
    --shadow-card:              0 4px 16px -2px rgba(0, 0, 0, 0.06);
    --shadow-drawer:            -12px 0 32px rgba(0, 0, 0, 0.12);

    /* Fluid Typography Scales */
    --text-hero:                clamp(2.75rem, 6vw, 4.75rem);
    --text-section:             clamp(1.875rem, 3.5vw, 2.75rem);
    --text-title:               1.25rem;
    --text-body:                clamp(0.938rem, 1vw, 1.063rem);
    --text-small:               0.875rem;
    --text-eyebrow:             0.688rem;

    /* ═════════════════════════════════════════════════════════════
       LAYER 3: COMPONENTS (Scoped Widget Properties)
       ═════════════════════════════════════════════════════════════ */
    --header-height:            76px;
    --product-card-bg:          var(--color-surface-base);
    --product-card-radius:      var(--radius-sm);
    --product-card-padding:     16px;
    --cart-drawer-width:        440px;
    --cart-progress-height:     8px;
    --sticky-bar-height:        70px;
    --swatch-size:              36px;

    /* ═════════════════════════════════════════════════════════════
       LAYER 4: EXPERIENCE TOKENS (Macro Rhythm, Density & Behavior)
       ═════════════════════════════════════════════════════════════ */
    /* Section Rhythm */
    --section-spacing:          clamp(5rem, 10vw, 10rem);
    --section-spacing-sm:       clamp(3rem, 6vw, 6rem);
    --container-max-width:      1440px;
    --container-padding:        clamp(1.5rem, 4vw, 4rem);

    /* Editorial Rhythm & Motion */
    --motion-duration-fast:     150ms;
    --motion-duration-base:     250ms;
    --motion-duration-slow:     500ms;
    --motion-ease-velvet:       cubic-bezier(0.25, 1, 0.5, 1);
    --motion-ease-spring:       cubic-bezier(0.175, 0.885, 0.32, 1.275);

    /* Layout Density */
    --grid-gap-desktop:         32px;
    --grid-gap-mobile:          16px;
}
```
