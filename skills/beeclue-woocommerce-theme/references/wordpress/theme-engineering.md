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

*Note: If a client explicitly requests removal of the attribution link, defer to the signed contract and scope terms (such as an agreed white-label buyout or license clause) rather than silently complying or refusing.*

---

## 3. AJAX Endpoints & CSRF Security Architecture

All custom interactive endpoints declared in `functions.php` (cart drawer updates, quantity steppers, live filters) must implement defensive CSRF nonces and input sanitization:

1. **Nonce Localization (`functions.php`)**:
   Register and localize scripts with `wp_create_nonce('beeclue_cart_nonce')` stored in the localized JS object (`beeclue_ajax.nonce`).
2. **First-Line Referer Check**:
   Every `wp_ajax_*` and `wp_ajax_nopriv_*` handler must begin with `check_ajax_referer('beeclue_cart_nonce', 'nonce');`. If the check fails, WordPress terminates execution with a `403 Forbidden`.
3. **Input Sanitization**:
   Wrap integer values with `absint()` (e.g. `$product_id`, `$quantity`) and text values with `sanitize_text_field(wp_unslash($_POST['key']))`.
4. **Structured JSON Output**:
   Always terminate responses with `wp_send_json_success($data)` or `wp_send_json_error($error)`.

