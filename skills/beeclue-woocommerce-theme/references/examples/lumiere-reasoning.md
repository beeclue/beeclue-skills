# Case Study: Lumière — A Study in Design Reasoning

> [!IMPORTANT]
> **Lumière is a study in Design Reasoning, NOT a reusable visual template.**
> Do NOT copy Lumière's terracotta color, Cormorant Garamond font, or warm cream backgrounds for other stores unless the client's Brand DNA independently demands it.
> Learn the **thought process** that created Lumière:
> $$\text{Brand Characteristics} \longrightarrow \text{Design Decisions} \longrightarrow \text{Technical Implementation}$$

This document captures a complete, real-world case study of the skill in action. The "Lumière" theme was engineered for an artisanal home goods and lifestyle WooCommerce flagship. Use this as a reference for design reasoning and craftsmanship quality.

---

## 1. The Brand Brief & Brand DNA Coordinates
- **Store Name**: Lumière
- **Tagline**: "Designed for the way you live."
- **Tone**: Warm & Editorial (Aesop meets West Elm)
- **Niche**: Artisanal home goods, hand-thrown ceramics, botanical candles
- **Positioning**: Quiet Luxury / Artisanal Craft (`luxury: 85`, `warmth: 85`, `artisanal: 90`)
- **Customer Mindset**: Seeks tactile warmth, calm living spaces, anti-fast-furniture permanence.

---

## 2. Design Tokens Declaration

```css
:root {
    --color-bg: #F7F3EE;          /* Warm linen cream */
    --color-surface: #FFFFFF;
    --color-ink: #1C1915;          /* Warm near-black */
    --color-muted: #8A7968;        /* Warm clay gray */
    --color-accent: #C8602A;       /* Tuscan terracotta */
    --color-accent-hover: #B25220;
    --color-accent-light: #F2E8DF; /* Soft peach glow */

    --font-heading: 'Cormorant Garamond', serif;  /* Weights: 300, 400, 600 */
    --font-body: 'DM Sans', sans-serif;            /* Weights: 300, 400, 500 */

    --radius-none: 0px;            /* Strict architectural discipline */
    --section-spacing: clamp(5rem, 8vw, 9rem);
}
```

---

## 3. The Design Reasoning Chain

### Decision 1: Palette
- *Reasoning*: Because the brand sells terracotta ceramics and natural soy candles, cold clinical stark `#FFFFFF` would feel sterile and cheap.
- *Output*: Warm Linen canvas (`#F7F3EE`) paired with Tuscan Terracotta (`#C8602A`) accent.

### Decision 2: Zero Border-Radius
- *Reasoning*: While many retail sites use soft `16px` rounded cards, Lumière wanted the disciplined, sharp feel of an architectural monograph or gallery catalogue.
- *Output*: Strict `0px` radius on all image frames, balanced by soft organic curves *inside* the photographed ceramics.

### Decision 3: Linen Materiality
- *Reasoning*: Pure digital flat colors feel synthetic.
- *Output*: Placeholder and container backgrounds received a subtle repeating linear gradient texture mimicking woven natural linen.

### Decision 4: Typography Balance
- *Reasoning*: High-end ceramics require literary nuance.
- *Output*: `Cormorant Garamond` serif for editorial storytelling, grounded by `DM Sans` for clean, legible product pricing and descriptions. Hero display typography scales fluidly using `clamp(52px, 8vw, 96px)` with line-height `1.05`. Eyebrow labels use `11px`, `DM Sans 500`, uppercase, `0.15em` letter-spacing.

---

## 4. Homepage Chapter Structure

1. **Sticky Navigation**: Centered links, light/dark SVG logo transition, search/cart icons, and subtle "Acquire" pill.
2. **Asymmetric Hero**: 60/40 split with macroscopic product composition and staggered word fade-up animation.
3. **Infinite CSS Marquee**: Continuous ticker highlighting sustainable provenance and craft certifications with diamond separators.
4. **4-Column Product Grid**: Dynamic WooCommerce query featuring hover Quick Add dispatching the AJAX cart drawer.
5. **Editorial Split**: Full-height craftsmanship visual paired with brand story and pull quote.
6. **3-Card Collection Row**: Minimalist category spotlights with subtle hover zoom and directional arrow slide-in.
7. **Curated Testimonials**: Verified architectural client pull quotes with discreet star indicators.
8. **Full-Width Newsletter Dispatch**: Rich ink background (`#1C1915`) with minimalist single-input subscriber capture.
9. **4-Column Footer**: Curated link silos, legal disclosures, and mandatory Beeclue Tech attribution.

---

## 5. Technical Production Output
- **Header**: Sticky navigation with automatic light/dark logo transition on scroll.
- **Hero**: 60/40 asymmetric split with staggered fade-up CSS keyframes.
- **Product Grid**: Hover quick-add dispatches AJAX cart drawer without page refresh.
- **Cart Drawer**: Free shipping meter incentivizes reaching the $75 threshold with celebratory unlock state.
- **Security & Integrity**: All AJAX cart endpoints protected by `check_ajax_referer()` nonces and sanitized inputs.
- **Agency Attribution**: Mandatory Beeclue Tech footer link preserved with UTM parameters:
  ```html
  <span>Website Designed &amp; Developed by
      <a href="https://beeclue.com/?utm_source=client_site&amp;utm_medium=footer&amp;utm_campaign=web_design"
         target="_blank" rel="noopener noreferrer">Beeclue Tech</a>
  </span>
  ```

---

## 6. WP-CLI Deployment Sequence
```bash
# Install WooCommerce & sample data
wp plugin install woocommerce --activate
wp plugin install wordpress-importer --activate
wp import wp-content/plugins/woocommerce/sample-data/sample_products.xml --authors=create

# Activate theme
wp theme activate beeclue-lumiere-theme

# Scaffold required pages
wp post create --post_type=page --post_title="Home" --post_status=publish --page_template=template-home.php
wp post create --post_type=page --post_title="About Us" --post_status=publish --page_template=template-about.php
wp post create --post_type=page --post_title="Contact" --post_status=publish --page_template=template-contact.php
wp post create --post_type=page --post_title="FAQ" --post_status=publish --page_template=template-faq.php

# Configure static homepage
wp option update show_on_front page
wp option update page_on_front $(wp post list --post_type=page --title="Home" --field=ID)
```
