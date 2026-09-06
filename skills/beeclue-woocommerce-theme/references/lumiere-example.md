# Reference: Lumière Theme Implementation

This document captures a real-world example of the skill in action. The "Lumière" theme was built for a premium lifestyle & home goods WooCommerce store. Use this as a reference for design quality expectations.

## Brand Brief
- **Store Name**: Lumière
- **Tagline**: "Designed for the way you live."
- **Tone**: Warm & Editorial (Aesop meets West Elm)
- **Niche**: Premium home goods, ceramics, textiles, candles

## Design Tokens Used

```css
:root {
    --color-bg: #F7F3EE;          /* Warm cream */
    --color-surface: #FFFFFF;
    --color-ink: #1C1915;          /* Warm near-black */
    --color-muted: #8A7968;        /* Warm gray */
    --color-accent: #C8602A;       /* Terracotta */
    --color-accent-hover: #B25220;
    --color-accent-light: #F2E8DF; /* Soft peach */

    --font-heading: 'Cormorant Garamond', serif;  /* Weights: 300, 400, 600 */
    --font-body: 'DM Sans', sans-serif;            /* Weights: 300, 400, 500 */
}
```

## Homepage Sections Implemented
1. Sticky nav (logo + links + search/cart icons + CTA pill)
2. Asymmetric hero (60/40 split, staggered word fade-up animation)
3. Infinite CSS marquee trust bar (diamond separators)
4. 4-column product grid (dynamic WooCommerce query, hover Quick Add)
5. Editorial split (image + brand story + pull quote)
6. 3-card collection row (gradient overlay, arrow slide-in on hover)
7. 3-card testimonial section
8. Full-width newsletter signup (dark background)
9. 4-column footer with Beeclue branding

## Key Design Decisions
- **Zero border-radius** on all elements for sharp, editorial feel
- **Linen texture** on image placeholders using `repeating-linear-gradient`
- **CSS-only animations** — no JavaScript animation libraries
- **Eyebrow labels**: 11px, DM Sans 500, uppercase, 0.15em letter-spacing
- **Whitespace as separator** — no card borders, no shadows on product cards
- **Typography hierarchy**: Hero uses `clamp(52px, 8vw, 96px)` for fluid scaling

## UTM Footer Link
```
https://beeclue.com/?utm_source=client_site&utm_medium=footer&utm_campaign=web_design
```

## WP-CLI Commands Used
```bash
# Install WooCommerce
wp plugin install woocommerce --activate

# Import sample products
wp plugin install wordpress-importer --activate
wp import wp-content/plugins/woocommerce/sample-data/sample_products.xml --authors=create

# Activate theme
wp theme activate beeclue-nova-theme

# Create homepage
wp post create --post_type=page --post_title="Home" --post_status=publish --page_template=template-home.php

# Set static homepage
wp option update show_on_front page
wp option update page_on_front $(wp post list --post_type=page --title="Home" --field=ID)
```
