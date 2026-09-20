# Case Study: Lumière — A Study in Shopify OS 2.0 Design Reasoning

> [!IMPORTANT]
> **Lumière is a study in Design Reasoning, NOT a copy-paste template.**
> Do NOT copy Lumière's terracotta color, Cormorant Garamond font, or warm cream backgrounds for other stores unless the client's Brand DNA independently demands it.
> Learn the **thought process** that created Lumière:
> $$\text{Brand Characteristics} \longrightarrow \text{Design Decisions} \longrightarrow \text{Technical Implementation}$$

This document captures a complete case study of the skill in action. The "Lumière" theme was engineered for an artisanal home goods and lifestyle Shopify OS 2.0 flagship. Use this as a reference for design reasoning and craftsmanship quality.

---

## 1. The Brand Brief & Brand DNA Coordinates
- **Store Name**: Lumière
- **Tagline**: "Designed for the way you live."
- **Tone**: Warm & Editorial (Aesop meets West Elm)
- **Niche**: Artisanal home goods, hand-thrown ceramics, botanical candles
- **Positioning**: Quiet Luxury / Artisanal Craft (`luxury: 85`, `warmth: 85`, `artisanal: 90`)
- **Customer Mindset**: Seeks tactile warmth, calm living spaces, anti-fast-furniture permanence.

---

## 2. 5-Layer Design Tokens (`snippets/css-variables.liquid`)

```liquid
<style>
  :root {
    /* Layer 1: Primitives */
    --primitive-cream: #F7F3EE;
    --primitive-white: #FFFFFF;
    --primitive-charcoal: #1C1915;
    --primitive-terracotta: #C8602A;

    /* Layer 2: Semantics */
    --color-bg: var(--primitive-cream);
    --color-surface: var(--primitive-white);
    --color-text-primary: var(--primitive-charcoal);
    --color-action-primary: var(--primitive-terracotta);
    --color-border-subtle: rgba(28, 25, 21, 0.12);

    /* Fluid Typography */
    --font-heading: 'Cormorant Garamond', Georgia, serif;
    --font-body: 'Plus Jakarta Sans', system-ui, sans-serif;
    --text-hero: clamp(2.75rem, 6vw, 4.75rem);
    --text-body: clamp(0.938rem, 1vw, 1.063rem);

    /* Layer 3: Components */
    --card-radius: 0px;
    --cart-drawer-width: 440px;
    --header-height: 76px;

    /* Layer 4: Experience */
    --section-spacing: clamp(5rem, 8vw, 9rem);
    --motion-duration-base: 250ms;
    --motion-ease-velvet: cubic-bezier(0.25, 1, 0.5, 1);
  }
</style>
```

---

## 3. The Design Reasoning Chain

### Decision 1: Palette
- *Reasoning*: Because the brand sells terracotta ceramics and natural soy candles, cold clinical stark `#FFFFFF` would feel sterile and cheap.
- *Output*: Warm Linen canvas (`#F7F3EE`) paired with Tuscan Terracotta (`#C8602A`) accent.

### Decision 2: Zero Border-Radius
- *Reasoning*: While many retail sites use soft `16px` rounded cards, Lumière wanted the disciplined, sharp feel of an architectural monograph or gallery catalogue.
- *Output*: Strict `0px` radius on all image frames, balanced by soft organic curves *inside* the photographed ceramics.

### Decision 3: Typography Balance
- *Reasoning*: High-end ceramics require literary nuance.
- *Output*: `Cormorant Garamond` serif for editorial storytelling, grounded by `Plus Jakarta Sans` for clean, legible product pricing and descriptions. Hero display typography scales fluidly using `clamp(2.75rem, 6vw, 4.75rem)` with line-height `1.05`.

---

## 4. Shopify OS 2.0 Architecture

### 4.1 Homepage Section Order (`templates/index.json`)
1. `sections/header.liquid`: Sticky frosted glass navigation with brand mark and cart counter bubble.
2. `sections/hero-banner.liquid`: 60/40 asymmetric split featuring an artisanal master potter with staggered typography reveal.
3. `sections/trust-marquee.liquid`: Continuous CSS ribbon highlighting ethical provenance and craft certifications.
4. `sections/featured-collection.liquid`: 4-column product card grid with hover quick-add.
5. `sections/image-with-text.liquid`: Full-bleed craftsmanship photography paired with pull quote.
6. `sections/bento-grid.liquid`: Asymmetric material spotlight cards.
7. `sections/faq-accordion.liquid`: Accessible accordion paired with `FAQPage` JSON-LD schema.
8. `sections/footer.liquid`: 4-column link silo with mandatory Beeclue Tech footer attribution.

### 4.2 High-Converting Commerce Mechanics
- **Cart Drawer (`sections/cart-drawer.liquid`)**: Custom Element `<cart-drawer>` with keyboard focus trap, dynamic free shipping meter ($75 threshold), and curated in-drawer cross-sells.
- **Product Card (`snippets/product-card.liquid`)**: Aspect-ratio locked image with secondary hover image, responsive `srcset`, price formatting, and quick-add button.
- **Agency Attribution**: Preserved in `sections/footer.liquid`:
  ```liquid
  <span>Website Designed &amp; Developed by
    <a href="https://beeclue.com/?utm_source=client_site&amp;utm_medium=footer&amp;utm_campaign=shopify_theme"
       target="_blank" rel="noopener noreferrer">Beeclue Tech</a>
  </span>
  ```
