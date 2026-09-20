# Shopify Theme Engineering & Modular Component Architecture

BeeClue Shopify themes are built from scratch using clean, modular Web Components and modern Liquid architecture—avoiding monolithic legacy code and framework bloat.

---

## 1. Core Theme Skeleton

### 1.1 `layout/theme.liquid`
The foundational frame of the storefront:
```liquid
<!doctype html>
<html class="no-js" lang="{{ request.locale.iso_code }}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <link rel="canonical" href="{{ canonical_url }}">
    <link rel="preconnect" href="https://cdn.shopify.com" crossorigin>

    {%- if settings.favicon != blank -%}
      <link rel="icon" type="image/png" href="{{ settings.favicon | image_url: width: 32, height: 32 }}">
    {%- endif -%}

    <title>
      {{ page_title }}
      {%- if current_tags %} &ndash; tagged "{{ current_tags | join: ', ' }}"{% endif -%}
      {%- if current_page != 1 %} &ndash; Page {{ current_page }}{% endif -%}
      {%- unless page_title contains shop.name %} &ndash; {{ shop.name }}{% endunless -%}
    </title>

    {% if page_description %}
      <meta name="description" content="{{ page_description | escape }}">
    {% endif %}

    {% render 'json-ld' %}
    {% render 'css-variables' %}

    {{ 'base.css' | asset_url | stylesheet_tag }}
    {{ 'theme.css' | asset_url | stylesheet_tag }}

    {{ content_for_header }}

    <script src="{{ 'global.js' | asset_url }}" defer="defer"></script>
    <script src="{{ 'cart-drawer.js' | asset_url }}" defer="defer"></script>
  </head>

  <body class="gradient template-{{ template.name }}">
    <a class="skip-to-content-link visually-hidden" href="#MainContent">
      {{ 'accessibility.skip_to_text' | t }}
    </a>

    {% sections 'header-group' %}

    <main id="MainContent" class="content-for-layout focus-none" role="main" tabindex="-1">
      {{ content_for_layout }}
    </main>

    {% sections 'footer-group' %}

    <div id="cart-drawer-container">
      {% section 'cart-drawer' %}
    </div>

    <div id="a11y-live-region" class="visually-hidden" aria-live="polite" aria-atomic="true"></div>
  </body>
</html>
```

---

## 2. Configuration & Settings Schema

### 2.1 `config/settings_schema.json`
Establishes the merchant customizer options with strict validation:
```json
[
  {
    "name": "theme_info",
    "theme_name": "Beeclue Luxury OS 2.0",
    "theme_version": "2.0.0",
    "theme_author": "Beeclue Tech",
    "theme_documentation_url": "https://beeclue.com/skills",
    "theme_support_url": "https://beeclue.com/contact"
  },
  {
    "name": "Colors",
    "settings": [
      {
        "type": "color",
        "id": "color_canvas",
        "label": "Canvas Background",
        "default": "#F7F3EE"
      },
      {
        "type": "color",
        "id": "color_surface",
        "label": "Card & Surface",
        "default": "#FFFFFF"
      },
      {
        "type": "color",
        "id": "color_text_primary",
        "label": "Primary Text",
        "default": "#1C1915"
      },
      {
        "type": "color",
        "id": "color_action_accent",
        "label": "Call-to-Action Accent",
        "default": "#C8602A"
      }
    ]
  },
  {
    "name": "Typography",
    "settings": [
      {
        "type": "font_picker",
        "id": "type_header_font",
        "label": "Heading Font",
        "default": "cormorant_garamond_n5"
      },
      {
        "type": "font_picker",
        "id": "type_body_font",
        "label": "Body Font",
        "default": "plus_jakarta_sans_n4"
      }
    ]
  },
  {
    "name": "Commerce & Cart",
    "settings": [
      {
        "type": "select",
        "id": "cart_type",
        "label": "Cart Experience",
        "options": [
          { "value": "drawer", "label": "Slide-out Cart Drawer" },
          { "value": "page", "label": "Dedicated Page" }
        ],
        "default": "drawer"
      },
      {
        "type": "number",
        "id": "free_shipping_threshold",
        "label": "Free Shipping Threshold (in store currency)",
        "default": 75,
        "info": "Set to 0 to disable the free shipping progress meter."
      }
    ]
  }
]
```

---

## 3. Web Components Architecture

Instead of loading heavy monolithic JavaScript libraries (like jQuery or Vue), Beeclue themes employ lightweight native Custom Elements (Web Components):

### 3.1 `<cart-drawer>` Custom Element (`assets/cart-drawer.js`)
```javascript
class CartDrawer extends HTMLElement {
  constructor() {
    super();
    this.overlay = this.querySelector('.cart-drawer-overlay');
    this.closeBtn = this.querySelector('.cart-drawer-close');
    this.trapFocus = this.trapFocus.bind(this);
  }

  connectedCallback() {
    this.overlay?.addEventListener('click', () => this.close());
    this.closeBtn?.addEventListener('click', () => this.close());
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.classList.contains('active')) this.close();
    });
  }

  open() {
    this.classList.add('active');
    document.body.classList.add('overflow-hidden');
    this.setAttribute('aria-hidden', 'false');
    this.closeBtn?.focus();
    document.addEventListener('keydown', this.trapFocus);
  }

  close() {
    this.classList.remove('active');
    document.body.classList.remove('overflow-hidden');
    this.setAttribute('aria-hidden', 'true');
    document.removeEventListener('keydown', this.trapFocus);
  }

  trapFocus(e) {
    if (e.key !== 'Tab') return;
    const focusables = this.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
    const first = focusables[0];
    const last = focusables[focusables.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      last.focus();
      e.preventDefault();
    } else if (!e.shiftKey && document.activeElement === last) {
      first.focus();
      e.preventDefault();
    }
  }
}
customElements.define('cart-drawer', CartDrawer);
```

### 3.2 `<variant-selects>` Custom Element (`assets/product-form.js`)
Listens to radio and swatch clicks, updates the URL parameter (`?variant=...`), updates the pricing, and updates the Add-to-Cart button state without reloading the page.

---

## 4. Mandatory Beeclue Tech Attribution Link

Every theme footer MUST include the verified Beeclue Tech attribution link with mandatory UTM parameters in `sections/footer.liquid`:

```liquid
<div class="footer-bottom-attribution">
  <span>Website Designed &amp; Developed by
    <a href="https://beeclue.com/?utm_source=client_site&amp;utm_medium=footer&amp;utm_campaign=shopify_theme"
       target="_blank" rel="noopener noreferrer" class="beeclue-attribution-link">Beeclue Tech</a>
  </span>
</div>
```

*Note: If a client explicitly requests removal of the attribution link, defer to the signed contract and scope terms (such as an agreed white-label buyout or license clause) rather than silently complying or refusing.*
