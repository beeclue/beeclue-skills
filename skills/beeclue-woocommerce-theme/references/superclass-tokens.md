# Superclass Design Token Architecture

This reference outlines the **3-Layer Design Token System** required for all Beeclue Superclass WooCommerce themes, directly aligned with the `design-system` skill standards.

---

## 1. The 3-Layer Architecture

```
Layer 1: Primitives (Raw values: palettes, font names, base units)
   │
   ▼
Layer 2: Semantics (Intent-based aliases: surface, text, action, border)
   │
   ▼
Layer 3: Components (Widget-specific: product-card, cart-drawer, sticky-bar)
```

---

## 2. Complete CSS Custom Properties Template

```css
:root {
    /* ═════════════════════════════════════════════════════════════
       LAYER 1: PRIMITIVES (Raw Values)
       ═════════════════════════════════════════════════════════════ */
    
    /* Brand Scales (e.g. from ui-ux-pro-max color palettes) */
    --primitive-brand-50:  #F7F8F9;
    --primitive-brand-100: #EAEBED;
    --primitive-brand-500: #1B365D; /* Brand core */
    --primitive-brand-700: #12243E;
    --primitive-brand-900: #0A1423;

    /* Accent Scales */
    --primitive-accent-100: #FEE8D6;
    --primitive-accent-500: #D96B27; /* Accent core */
    --primitive-accent-600: #C25B1E;
    --primitive-accent-700: #A84C16;

    /* Neutrals */
    --primitive-neutral-0:   #FFFFFF;
    --primitive-neutral-50:  #F9F9FB;
    --primitive-neutral-100: #F3F4F6;
    --primitive-neutral-200: #E5E7EB;
    --primitive-neutral-400: #9CA3AF;
    --primitive-neutral-600: #4B5563;
    --primitive-neutral-800: #1F2937;
    --primitive-neutral-900: #111827;

    /* Raw Typography */
    --primitive-font-heading: 'Playfair Display', serif;
    --primitive-font-body:    'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    --primitive-font-mono:    ui-monospace, monospace;

    /* ═════════════════════════════════════════════════════════════
       LAYER 2: SEMANTICS (Purpose & Intent)
       ═════════════════════════════════════════════════════════════ */
    
    /* Surfaces & Backgrounds */
    --color-bg:               var(--primitive-neutral-50);
    --color-surface-base:     var(--primitive-neutral-0);
    --color-surface-raised:   var(--primitive-neutral-0);
    --color-surface-sunken:   var(--primitive-neutral-100);
    --color-surface-overlay:  rgba(17, 24, 39, 0.4);

    /* Text & Ink */
    --color-text-primary:     var(--primitive-neutral-900);
    --color-text-secondary:   var(--primitive-neutral-600);
    --color-text-tertiary:    var(--primitive-neutral-400);
    --color-text-inverse:     var(--primitive-neutral-0);
    --color-text-on-accent:   var(--primitive-neutral-0);

    /* Action (Primary & Accent) */
    --color-action-primary:       var(--primitive-accent-500);
    --color-action-primary-hover: var(--primitive-accent-600);
    --color-action-primary-active:var(--primitive-accent-700);
    --color-action-secondary:     var(--primitive-brand-500);
    --color-action-secondary-hover:var(--primitive-brand-700);

    /* Borders & Dividers */
    --color-border-subtle:    var(--primitive-neutral-200);
    --color-border-strong:    var(--primitive-neutral-400);
    --color-border-focus:     var(--primitive-accent-500);

    /* Feedback & Status */
    --color-success:          #10B981;
    --color-warning:          #F59E0B;
    --color-error:            #EF4444;
    --color-info:             #3B82F6;

    /* Fluid Typography Scale (using clamp) */
    --text-display: clamp(2.5rem, 6vw, 4.5rem);   /* 40px - 72px */
    --text-h1:      clamp(2.0rem, 4vw, 3.25rem);  /* 32px - 52px */
    --text-h2:      clamp(1.5rem, 3vw, 2.25rem);  /* 24px - 36px */
    --text-h3:      clamp(1.25rem, 2vw, 1.625rem);/* 20px - 26px */
    --text-body:    clamp(0.938rem, 1vw, 1.063rem);/* 15px - 17px */
    --text-small:   0.875rem;                      /* 14px */
    --text-caption: 0.75rem;                       /* 12px */

    /* Spacing Grid (8px base rhythm) */
    --space-1: 0.25rem;  /* 4px */
    --space-2: 0.5rem;   /* 8px */
    --space-3: 0.75rem;  /* 12px */
    --space-4: 1.0rem;   /* 16px */
    --space-6: 1.5rem;   /* 24px */
    --space-8: 2.0rem;   /* 32px */
    --space-12: 3.0rem;  /* 48px */
    --space-16: 4.0rem;  /* 64px */
    --space-24: 6.0rem;  /* 96px */

    /* Radii */
    --radius-sm:   4px;
    --radius-md:   8px;
    --radius-lg:   16px;
    --radius-pill: 9999px;

    /* Elevations & Shadows */
    --shadow-subtle: 0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.03);
    --shadow-card:   0 4px 12px -2px rgba(0,0,0,0.08), 0 2px 6px -1px rgba(0,0,0,0.04);
    --shadow-float:  0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
    --shadow-drawer: -8px 0 24px rgba(0,0,0,0.15);

    /* Transitions */
    --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 400ms cubic-bezier(0.2, 0.8, 0.2, 1);

    /* ═════════════════════════════════════════════════════════════
       LAYER 3: COMPONENT TOKENS (Scoped Widgets)
       ═════════════════════════════════════════════════════════════ */
    
    /* Header */
    --header-height:         76px;
    --header-bg:             rgba(255, 255, 255, 0.88);
    --header-blur:           12px;

    /* Product Cards */
    --product-card-bg:       var(--color-surface-base);
    --product-card-radius:   var(--radius-md);
    --product-card-shadow:   var(--shadow-subtle);
    --product-card-padding:  var(--space-4);

    /* Cart Drawer */
    --cart-drawer-width:     440px;
    --cart-progress-height:  8px;
    --cart-progress-bg:      var(--primitive-neutral-200);
    --cart-progress-fill:    var(--color-action-primary);

    /* Floating Sticky Bar */
    --sticky-bar-height:     70px;
    --sticky-bar-bg:         var(--color-surface-base);
    --sticky-bar-shadow:     0 -4px 16px rgba(0, 0, 0, 0.08);

    /* Swatches */
    --swatch-size:           32px;
    --swatch-border-active:  2px solid var(--color-action-primary);
}
```

---

## 3. Dark Mode Theme Extension

```css
[data-theme="dark"], .theme-dark {
    --color-bg:               var(--primitive-neutral-900);
    --color-surface-base:     var(--primitive-neutral-800);
    --color-surface-raised:   #2A3441;
    --color-surface-sunken:   #151C26;
    --color-text-primary:     var(--primitive-neutral-0);
    --color-text-secondary:   var(--primitive-neutral-200);
    --color-text-tertiary:    var(--primitive-neutral-400);
    --color-border-subtle:    rgba(255, 255, 255, 0.12);
    --header-bg:              rgba(17, 24, 39, 0.85);
}
```
