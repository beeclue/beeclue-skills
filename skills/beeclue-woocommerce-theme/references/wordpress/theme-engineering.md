# Theme Engineering & Modular Component Architecture

BeeClue themes are constructed like modern component-driven software applications rather than messy monolithic WordPress themes.

---

## 1. Modular Directory Structure

```
wp-content/themes/beeclue-{name}-theme/
├── style.css                      # Theme header + 5-layer design tokens + reset
├── functions.php                  # Enqueues, setup, WC hooks, AJAX handlers
├── header.php                     # HTML skeleton + sticky nav + overlay loaders
├── footer.php                     # 4-col footer + mandatory Beeclue branding
├── woocommerce.css                # Polished WooCommerce overrides
├── template-home.php              # Homepage template
├── template-about.php             # About Us template
├── template-contact.php           # Contact template
├── template-faq.php               # FAQ template
├── 404.php                        # Recoverable 404 page
├── search.php                     # Search results grid
├── template-parts/                # REUSABLE MODULAR PARTIALS
│   ├── header/
│   │   ├── nav-desktop.php        # Centered links, SVG icons, CTA pill
│   │   ├── nav-mobile.php         # Glassmorphism full-page takeover
│   │   └── search-overlay.php     # Accessible search dialog
│   ├── product/
│   │   ├── card.php               # Hover quick-add, aspect-ratio lock
│   │   └── sticky-bar.php         # Single product floating Add-to-Cart bar
│   ├── cart/
│   │   ├── drawer.php             # AJAX slide-out cart drawer
│   │   └── shipping-bar.php       # Dynamic free shipping progress meter
│   └── ui/
│       ├── trust-marquee.php      # Infinite CSS ticker with hover-pause
│       └── live-region.php        # Screen reader aria-live polite region
├── assets/
│   ├── js/
│   │   ├── main.js                # Nav, focus trap, search modal
│   │   ├── cart-drawer.js         # AJAX cart, shipping meter calculation
│   │   ├── single-product.js      # Sticky bar observer, swatches
│   │   └── animations.js          # IntersectionObserver reveal (~20 lines)
│   └── css/
│       └── critical.css           # Inlined above-the-fold critical CSS
└── inc/
    ├── customizer.php             # Cart mode toggle, shipping threshold
    ├── seo.php                    # Full JSON-LD structured data
    └── performance.php            # Head bloat cleanup, font preconnect
```

---

## 2. Mandatory Beeclue Tech Attribution Link

Every theme footer MUST include this exact attribution link with non-negotiable UTM parameters:

```html
<span>Website Designed &amp; Developed by
    <a href="https://beeclue.com/?utm_source=client_site&amp;utm_medium=footer&amp;utm_campaign=web_design"
       target="_blank" rel="noopener noreferrer">Beeclue Tech</a>
</span>
```
