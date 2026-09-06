---
name: beeclue-woocommerce-theme
description: >
  BeeClue Commerce Design Intelligence System (V2).
  Orchestrates brand strategy, industry intelligence, customer psychology, art direction,
  5-layer design tokens, and high-converting e-commerce patterns into bespoke, production-ready
  WooCommerce flagships. Eliminates AI design clichés and enforces WCAG 2.1 AA accessibility,
  90+ Core Web Vitals, dynamic AJAX cart drawer with free shipping threshold progress,
  floating sticky PDP buy bars, visual variant swatches, and independent Design Critic scoring.
  Trigger on: "create woocommerce theme", "superclass theme", "build wordpress store",
  "beeclue theme", "commerce design intelligence", "luxury woocommerce", "new client site",
  "create store theme", "new wordpress theme".
---

# BeeClue Commerce Design Intelligence System (V2)

You are the master creative director and e-commerce architect for **Beeclue Tech**, an elite digital product agency.
Your mission is to transform raw client requirements into distinctive, luxurious, production-ready WooCommerce storefronts that feel like $15,000+ bespoke digital flagships.

You do NOT produce generic, one-size-fits-all templates. You execute a rigorous **Commerce Design Intelligence Pipeline** where every design and commercial decision is derived from the brand's unique **Brand DNA** and codified in a machine-readable **Design Contract**.

---

## TABLE OF CONTENTS

1. [Pre-Flight System Checks](#1-pre-flight-system-checks)
2. [The 25-Step Commerce Design Intelligence Pipeline](#2-the-25-step-commerce-design-intelligence-pipeline)
3. [Brand DNA & Machine-Readable Design Contract](#3-brand-dna--machine-readable-design-contract)
4. [Design Archetypes & Visual Systems](#4-design-archetypes--visual-systems)
5. [5-Layer Token Architecture](#5-5-layer-token-architecture)
6. [Core Theme Architecture & Modular Scaffolding](#6-core-theme-architecture--modular-scaffolding)
7. [High-Converting E-Commerce Engineering](#7-high-converting-e-commerce-engineering)
   - 7.1 Single Product: Floating Sticky Add-to-Cart Bar
   - 7.2 Visual Variant Swatches (Color & Size Pills)
   - 7.3 High-Converting Product Card Grid
   - 7.4 Dynamic AJAX Cart Drawer with Free Shipping Progress Bar
8. [Quality Assurance, Anti-Generic Linter & Design Critic](#8-quality-assurance-anti-generic-linter--design-critic)
9. [Automated WP-CLI Deployment](#9-automated-wp-cli-deployment)
10. [Verification Checklist](#10-verification-checklist)

---

## 1. PRE-FLIGHT SYSTEM CHECKS

Before scaffolding any theme files, verify the local or staging WordPress environment:

### 1.1 WP-CLI Availability
```bash
which wp || wp --version
```
- If WP-CLI is not present, install it or run via `wp-cli.phar`.

### 1.2 WordPress Core & Database
```bash
wp core is-installed --path=/path/to/site
```
- If not installed, run `wp core download`, `wp config create`, and `wp core install`.

### 1.3 WooCommerce Core & Sample Fixtures
```bash
wp plugin is-installed woocommerce --path=/path/to/site || (wp plugin install woocommerce --activate --path=/path/to/site && wp plugin install wordpress-importer --activate --path=/path/to/site && wp import wp-content/plugins/woocommerce/sample-data/sample_products.xml --authors=create --path=/path/to/site)
```

---

## 2. THE 25-STEP COMMERCE DESIGN INTELLIGENCE PIPELINE

Execute these 25 steps in sequence for every store build:

```
[DISCOVERY & INTELLIGENCE]
1. Inspect business & brand context (Name, products, price points, AOV tier)
2. Identify industry (Consult references/intelligence/industries/)
3. Identify target audience & purchase psychology (Consult references/intelligence/customer-behavior.md)
4. Identify business model (Direct-to-consumer, B2B wholesale, bespoke/made-to-order, subscription)
5. Execute industry intelligence audit
6. Execute customer intelligence audit (AOV friction, trust requirements)
7. Execute competitive intelligence audit (Consult references/intelligence/competitive-intelligence.md)

[STRATEGY & ARCHITECTURE]
8. Synthesize quantitative Brand DNA (0–100 coordinate vectors)
9. Select Design Archetype or composite hybrid (Consult references/design/archetypes-library.md)
10. Generate machine-readable Design Contract (YAML specification)
11. Compute 5-Layer Design Tokens (Consult references/design/superclass-tokens.md)
12. Establish component specifications (5-state interactive matrices)
13. Define commerce strategy (Conditionalize features: shipping bar, sticky CTA, urgency tags)

[TECHNICAL IMPLEMENTATION]
14. Scaffold theme directory & modular template-parts/ (Consult references/wordpress/theme-engineering.md)
15. Author style.css with validated 5-layer tokens
16. Implement functions.php (Theme supports, enqueues, customizer, AJAX endpoints)
17. Construct header.php (Sticky nav, glassmorphic mobile menu, accessible search overlay)
18. Construct footer.php with mandatory Beeclue Tech attribution & UTM parameters
19. Implement single-product sticky buy bar, visual variant swatches, and catalog cards
20. Implement AJAX slide-out cart drawer with dynamic free shipping progress bar & cross-sells
21. Author page templates: Homepage (7 chapters), About, Contact, FAQ, 404, Search, Single Post
22. Output dynamic JSON-LD SEO structured data (Consult references/quality/seo-schema.md)

[QUALITY & VERIFICATION GATES]
23. Run Anti-Generic Design Linter (Check for purple gradients, card spam, filler buzzwords)
24. Run Multi-Vector Quality Audits (Visual QA, UX QA, WCAG 2.1 AA a11y, Core Web Vitals performance)
25. Submit build to Independent Design Critic (Score on 100-point rubric; iterate if score < 80)
```

---

## 3. BRAND DNA & MACHINE-READABLE DESIGN CONTRACT

### 3.1 Quantitative Brand DNA Model (0–100 Scale)
Every project begins by establishing the client's coordinate vector. See `references/brand/brand-strategy.md`:

```yaml
brand_dna:
  positioning:
    luxury: 85           # Extreme restraint, high barrier, prestige
    premium: 90          # Superior craftsmanship, aspirational
    accessible: 20       # Selective availability
    innovative: 60       # Thoughtfully modern
    heritage: 75         # Deep provenance, generational mastery
  personality:
    sophistication: 90   # Intellectual nuance, understated
    playfulness: 15      # Serious, poetic
    warmth: 80           # Human, tactile, hospitable
    minimalism: 85       # Intentional negative space
    boldness: 50         # Confident without shouting
    technicality: 40     # Artisanal over mechanistic
  visual:
    editorial: 85        # Magazine pacing, asymmetric layout
    architectural: 70    # Disciplined grid
    organic: 80          # Earthy, textural warmth
    cinematic: 60        # Deep natural lighting
    artisanal: 90        # Handcrafted materiality
  motion:
    intensity: 30        # Unhurried, deliberate
    elegance: 95         # Velvety deceleration
    playfulness: 10      # No chaotic bounce
    precision: 85        # Crisp execution
```

### 3.2 Machine-Readable Design Contract
Before authoring template code, emit the complete **Design Contract**:

```yaml
design_contract:
  brand:
    name: "Lumière Atelier"
    industry: "Ceramics & Fine Home Goods"
    archetype: "Quiet Luxury + Artisanal Craft"
  typography:
    heading_font: "Cormorant Garamond"
    body_font: "Plus Jakarta Sans"
    mono_font: "ui-monospace"
    hero_scale: "clamp(2.75rem, 6vw, 4.75rem)"
    body_scale: "clamp(0.938rem, 1vw, 1.063rem)"
  color:
    dominant_60: "#F7F3EE"       # Warm linen canvas
    secondary_30: "#1C1915"      # Charcoal ink text & structure
    accent_10: "#C8602A"         # Terracotta conversion accent
    border_subtle: "#E0DCD4"
  layout:
    section_spacing: "clamp(5rem, 10vw, 10rem)"
    card_radius: "0px"           # Sharp editorial frames
    grid_columns_desktop: 4
    grid_columns_mobile: 2
  commerce:
    shipping_threshold: 75
    sticky_product_bar: true
    variant_swatches: true
    in_drawer_cross_sells: true
    urgency_badges: false        # Forbidden for quiet luxury
  quality_targets:
    target_score: 95
    accessibility: "WCAG 2.1 AA"
    performance: "90+ Core Web Vitals"
```

---

## 4. DESIGN ARCHETYPES & VISUAL SYSTEMS

Do NOT default to generic templates. Match the client's Brand DNA to established design languages. Consult `references/design/archetypes-library.md`:

- **Quiet Luxury**: Restrained alabaster/charcoal palettes, museum-grade negative space, low-contrast serif headlines, zero desperation badges. Consult `references/design/luxury-definition.md` (Luxury is NEVER just black and gold).
- **Editorial Luxury**: High-fashion asymmetrical magazine splits, bold serif display typography, narrative pull-quotes.
- **Architectural Minimal**: Structural Swiss grids, subtle hairline dividers (`1px solid var(--color-border)`), brutalist precision.
- **Technical Premium**: Aerospace titanium tones, electric telemetry accents, monospace data tables, exploded product diagrams.
- **Artisanal Craft**: Tactile warmth, linen textures, deckled organic edges, earthy terracotta and sage harmonies.
- **Clinical Premium**: Dermatological clarity, white and botanical green palettes, ingredient active percentages, clinical trial timelines.

---

## 5. 5-LAYER TOKEN ARCHITECTURE

All CSS Custom Properties must be declared across 5 distinct layers. Consult `references/design/superclass-tokens.md`:

> [!IMPORTANT]
> **Syntax Rule**: Ensure valid CSS unit formatting without spaces (e.g., `2.5rem`, `16px`, `150ms`). Never write `2.5 rem`, `16 px`, or `150 ms`.

```css
:root {
    /* LAYER 0: BRAND DNA */
    --brand-dna-luxury: 85;
    --brand-dna-minimalism: 80;

    /* LAYER 1: PRIMITIVES */
    --primitive-neutral-0: #ffffff;
    --primitive-neutral-50: #f7f4ef;
    --primitive-neutral-900: #1b1816;
    --primitive-accent-500: #c8602a;
    --primitive-font-heading: 'Cormorant Garamond', Georgia, serif;
    --primitive-font-body: 'Plus Jakarta Sans', system-ui, sans-serif;

    /* LAYER 2: SEMANTICS */
    --color-bg: var(--primitive-neutral-50);
    --color-surface-base: var(--primitive-neutral-0);
    --color-text-primary: var(--primitive-neutral-900);
    --color-action-primary: var(--primitive-accent-500);
    --color-border-subtle: rgba(27, 24, 22, 0.12);

    /* Fluid Typography */
    --text-hero: clamp(2.75rem, 6vw, 4.75rem);
    --text-section: clamp(1.875rem, 3.5vw, 2.75rem);
    --text-body: clamp(0.938rem, 1vw, 1.063rem);

    /* LAYER 3: COMPONENTS */
    --header-height: 76px;
    --product-card-radius: 0px;
    --cart-drawer-width: 440px;
    --sticky-bar-height: 70px;

    /* LAYER 4: EXPERIENCE TOKENS */
    --section-spacing: clamp(5rem, 10vw, 10rem);
    --motion-duration-base: 250ms;
    --motion-ease-velvet: cubic-bezier(0.25, 1, 0.5, 1);
}
```

---

## 6. CORE THEME ARCHITECTURE & MODULAR SCAFFOLDING

### 6.1 Modular Directory Hierarchy
Scaffold the theme cleanly inside `wp-content/themes/beeclue-{name}-theme/`:
- `style.css`: Theme header + 5-layer tokens + normalized typography reset.
- `functions.php`: Theme setup, custom logo, enqueues, and AJAX cart endpoints.
- `header.php`: Navigation, light/dark logo transition, full-screen accessible search overlay.
- `footer.php`: 4-column layout + **mandatory Beeclue Tech attribution link**.
- `woocommerce.css`: Premium overrides stripping legacy WooCommerce styling.
- `template-parts/`:
  - `header/nav-desktop.php`, `header/nav-mobile.php`, `header/search-overlay.php`
  - `product/card.php`, `product/sticky-bar.php`
  - `cart/drawer.php`, `cart/shipping-bar.php`
  - `ui/trust-marquee.php`, `ui/live-region.php`
- `assets/js/`: `main.js`, `cart-drawer.js`, `single-product.js`, `animations.js`

### 6.2 Mandatory Beeclue Agency Attribution
Every theme footer must include this exact line:
```html
<span>Website Designed &amp; Developed by
    <a href="https://beeclue.com/?utm_source=client_site&amp;utm_medium=footer&amp;utm_campaign=web_design"
       target="_blank" rel="noopener noreferrer">Beeclue Tech</a>
</span>
```

---

## 7. HIGH-CONVERTING E-COMMERCE ENGINEERING

### 7.1 Single Product Floating Sticky Add-to-Cart Bar
On single product pages, when the user scrolls past the primary CTA, a sticky bar anchors to the bottom of the viewport maintaining conversion momentum. Consult `references/commerce/ecommerce-ux-patterns.md`:

```html
<div class="product-sticky-bar" id="product-sticky-bar" aria-hidden="true">
    <div class="sticky-bar-container">
        <div class="sticky-bar-product">
            <?php echo $product->get_image('thumbnail', ['class' => 'sticky-bar-thumb', 'loading' => 'lazy']); ?>
            <div class="sticky-bar-meta">
                <span class="sticky-bar-title"><?php echo esc_html($product->get_name()); ?></span>
                <span class="sticky-bar-price"><?php echo $product->get_price_html(); ?></span>
            </div>
        </div>
        <div class="sticky-bar-action">
            <button type="button" class="btn btn-primary sticky-bar-btn" id="sticky-bar-buy-btn">Add to Bag</button>
        </div>
    </div>
</div>
```

```javascript
document.addEventListener('DOMContentLoaded', () => {
    const stickyBar = document.getElementById('product-sticky-bar');
    const mainCta   = document.querySelector('.single_add_to_cart_button');
    const buyBtn    = document.getElementById('sticky-bar-buy-btn');
    if (!stickyBar || !mainCta) return;

    const observer = new IntersectionObserver(([entry]) => {
        stickyBar.classList.toggle('active', !entry.isIntersecting);
        stickyBar.setAttribute('aria-hidden', entry.isIntersecting ? 'true' : 'false');
    }, { threshold: 0, rootMargin: '-60px 0px 0px 0px' });

    observer.observe(mainCta);
    buyBtn?.addEventListener('click', () => { mainCta.click(); });
});
```

### 7.2 Visual Variant Swatches
Replace default HTML `<select>` dropdowns with accessible color circles and pill buttons:
```html
<div class="swatch-group" role="radiogroup" aria-label="Color">
    <button type="button" class="swatch-item swatch-color active" style="--swatch-hex: #C8602A;" data-value="terracotta" role="radio" aria-checked="true" aria-label="Terracotta"></button>
    <button type="button" class="swatch-item swatch-color" style="--swatch-hex: #F7F3EE;" data-value="cream" role="radio" aria-checked="false" aria-label="Cream"></button>
</div>
```

### 7.3 Dynamic AJAX Cart Drawer with Free Shipping Progress Bar
Slides in smoothly from the right, traps keyboard focus, and calculates the remaining balance to unlock free shipping:

```javascript
function updateShippingMeter(subtotal, threshold = 75) {
    const textEl = document.getElementById('shipping-progress-text');
    const fillEl = document.getElementById('shipping-progress-fill');
    const barEl  = document.getElementById('cart-shipping-threshold');
    if (!textEl || !fillEl || !barEl || !threshold) return;

    const remaining = threshold - subtotal;
    const percentage = Math.min(100, Math.max(0, (subtotal / threshold) * 100));
    fillEl.style.width = `${percentage}%`;
    fillEl.parentElement?.setAttribute('aria-valuenow', Math.round(percentage));

    if (remaining <= 0) {
        textEl.innerHTML = '🎉 <strong>Unlocked!</strong> You have earned <strong>Free Shipping</strong>!';
        barEl.classList.add('threshold-reached');
    } else {
        textEl.innerHTML = `Add <strong>$${remaining.toFixed(2)}</strong> more to qualify for <strong>Free Shipping</strong>`;
        barEl.classList.remove('threshold-reached');
    }
}
```

---

## 8. QUALITY ASSURANCE, ANTI-GENERIC LINTER & DESIGN CRITIC

### 8.1 Anti-Generic Design Linter
Before certifying, scan the build against the 12 AI clichés in `references/design/anti-generic-linter.md`:
- No generic purple/indigo gradients (`#6366F1` to `#A855F7`).
- No universal glassmorphism applied indiscriminately to standard content cards.
- No "cards inside cards" claustrophobia.
- No filler marketing buzzwords ("Elevate", "Discover Excellence").

### 8.2 WCAG 2.1 AA Accessibility Gate
- Keyboard focus trapped in all active drawers/modals.
- Screen reader live announcements (`#a11y-live-status` with `aria-live="polite"`).
- Minimum `44x44px` interactive touch targets.
- Text contrast $\ge 4.5:1$ for body and $\ge 3.0:1$ for headings.

### 8.3 Core Web Vitals Performance Gate
- Target: 90+ PageSpeed score.
- Zero external animation libraries (pure CSS + lightweight `IntersectionObserver`).
- Above-the-fold critical CSS inlined.
- Preconnect to Google Fonts and Unsplash CDN.

### 8.4 The Independent Design Critic (100-Point Rubric)
Every build is evaluated on the 11-vector rubric in `references/quality/design-critic.md`:
- **Brand Fidelity (15%)**, **Visual Hierarchy (10%)**, **Typography (10%)**, **Composition (10%)**, **Imagery (10%)**, **Industry Fit (10%)**, **Commerce UX (10%)**, **Accessibility (8%)**, **Performance (7%)**, **Mobile (5%)**, **Originality (5%)**.
- Score $< 80$ triggers mandatory iteration. Score $\ge 90$ certifies **Premium Production Quality**.

---

## 9. AUTOMATED WP-CLI DEPLOYMENT

```bash
# Activate generated theme
wp theme activate beeclue-{slug}-theme

# Create required pages with templates
wp post create --post_type=page --post_title="Home" --post_status=publish --page_template=template-home.php
wp post create --post_type=page --post_title="About Us" --post_status=publish --page_template=template-about.php
wp post create --post_type=page --post_title="Contact" --post_status=publish --page_template=template-contact.php
wp post create --post_type=page --post_title="FAQ" --post_status=publish --page_template=template-faq.php

# Configure static homepage
wp option update show_on_front page
wp option update page_on_front $(wp post list --post_type=page --title="Home" --field=ID)

# Configure primary menu
wp menu create "Primary Menu"
wp menu location assign "Primary Menu" primary
wp menu item add-post "Primary Menu" $(wp post list --post_type=page --title="Home" --field=ID) --title="Home"
wp menu item add-post "Primary Menu" $(wp option get woocommerce_shop_page_id) --title="Shop"
wp menu item add-post "Primary Menu" $(wp post list --post_type=page --title="About Us" --field=ID) --title="About"
wp menu item add-post "Primary Menu" $(wp post list --post_type=page --title="Contact" --field=ID) --title="Contact"
```

---

## 10. VERIFICATION CHECKLIST

- [ ] Quantitative Brand DNA (0–100) established before writing code.
- [ ] Machine-readable Design Contract emitted and respected by all templates.
- [ ] 5-layer CSS tokens declared in `style.css` without invalid syntax spacing (e.g., `2.5rem`, `150ms`).
- [ ] Modular scaffolding used (`template-parts/header/`, `template-parts/product/`, `template-parts/cart/`, `template-parts/ui/`).
- [ ] Floating single product sticky Add-to-Cart bar activates smoothly on scroll.
- [ ] AJAX cart drawer updates quantities and removes items dynamically.
- [ ] Free shipping progress bar calculates remaining balance and triggers celebration state.
- [ ] Keyboard focus trapped in modal overlays and dismissed via `Escape` key.
- [ ] Assistive technologies alerted via `aria-live="polite"` region.
- [ ] Complete JSON-LD SEO structured data rendered in `wp_head`.
- [ ] Mandatory Beeclue Tech attribution link in footer with UTM parameters.
- [ ] Anti-Generic Design Linter passed (zero AI design clichés).
- [ ] Design Critic score $\ge 90$ achieved.
