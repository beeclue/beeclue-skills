# Shopify Theme Customization Architecture (`settings_schema.json`)

BeeClue Shopify themes provide unmatched merchant customizability through a 12-group `config/settings_schema.json` architecture. Every setting is strictly typed, grouped logically, and mapped cleanly to CSS custom properties via `snippets/css-variables.liquid`.

---

## 1. The 12-Group Customizer Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│               BeeClue 12-Group Customizer Architecture                 │
├────────────────────────────┬───────────────────────────────────────────┤
│ 1. Theme Info & Meta       │ Agency attribution, version, docs         │
│ 2. Colors (5-Layer Tokens) │ Canvas, surface, primary ink, accent      │
│ 3. Typography & Scale      │ Headings, body, editorial, uppercase track│
│ 4. Corner Radius & Shape   │ Sharp (0px), subtle (4px), smooth (12px)  │
│ 5. Buttons & Actions       │ Solid, outline, magnetic hover, pill      │
│ 6. Header & Navigation     │ Transparent, sticky on scroll, mega menu  │
│ 7. Predictive Search       │ Drawer vs modal, show vendor, show price  │
│ 8. Product Cards & Grid    │ Aspect ratio (1:1, 3:4), hover swap, badge│
│ 9. Variant Swatches        │ Color circles, size pills, image thumbs   │
│ 10. Product Detail Page    │ Media layout, sticky buy bar, size guide  │
│ 11. Cart Drawer & Shipping │ Threshold meter, GWP milestone, notes     │
│ 12. Micro-Interactions     │ Scroll physics, icon stroke-width         │
└────────────────────────────┴───────────────────────────────────────────┘
```

---

## 2. Complete `settings_schema.json` Specification

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
        "type": "header",
        "content": "Surface and canvas colors"
      },
      {
        "type": "color",
        "id": "color_canvas",
        "label": "Canvas background",
        "default": "#F7F3EE",
        "info": "The primary page canvas tone."
      },
      {
        "type": "color",
        "id": "color_surface",
        "label": "Card and surface background",
        "default": "#FFFFFF"
      },
      {
        "type": "header",
        "content": "Text and line colors"
      },
      {
        "type": "color",
        "id": "color_text_primary",
        "label": "Primary text",
        "default": "#1C1915"
      },
      {
        "type": "color",
        "id": "color_text_muted",
        "label": "Muted text",
        "default": "#70695E"
      },
      {
        "type": "color",
        "id": "color_border",
        "label": "Border color",
        "default": "rgba(28, 25, 21, 0.12)"
      },
      {
        "type": "header",
        "content": "Accent colors"
      },
      {
        "type": "color",
        "id": "color_accent",
        "label": "Accent",
        "default": "#C8602A",
        "info": "Used for checkout CTA, free shipping progress fill, and active swatches."
      },
      {
        "type": "color",
        "id": "color_accent_hover",
        "label": "Accent hover",
        "default": "#B25220"
      }
    ]
  },
  {
    "name": "Typography",
    "settings": [
      {
        "type": "font_picker",
        "id": "type_header_font",
        "label": "Heading font",
        "default": "cormorant_garamond_n5"
      },
      {
        "type": "font_picker",
        "id": "type_body_font",
        "label": "Body font",
        "default": "plus_jakarta_sans_n4"
      },
      {
        "type": "range",
        "id": "heading_scale_percent",
        "min": 80,
        "max": 140,
        "step": 5,
        "unit": "%",
        "label": "Heading scale multiplier",
        "default": 100
      },
      {
        "type": "checkbox",
        "id": "heading_uppercase",
        "label": "Uppercase section headings",
        "default": false
      },
      {
        "type": "select",
        "id": "eyebrow_letter_spacing",
        "label": "Eyebrow letter spacing",
        "options": [
          { "value": "0.05em", "label": "Subtle (0.05em)" },
          { "value": "0.15em", "label": "Editorial luxury (0.15em)" },
          { "value": "0.25em", "label": "Haute monograph (0.25em)" }
        ],
        "default": "0.15em"
      }
    ]
  },
  {
    "name": "Corner radii",
    "settings": [
      {
        "type": "select",
        "id": "corner_radius_preset",
        "label": "Corner radius preset",
        "options": [
          { "value": "0px", "label": "Sharp architectural (0px)" },
          { "value": "4px", "label": "Subtle refinement (4px)" },
          { "value": "12px", "label": "Smooth contemporary (12px)" },
          { "value": "24px", "label": "Organic soft (24px)" }
        ],
        "default": "0px"
      },
      {
        "type": "select",
        "id": "card_shadow",
        "label": "Surface elevation and shadow",
        "options": [
          { "value": "none", "label": "None" },
          { "value": "0 4px 20px rgba(0,0,0,0.04)", "label": "Subtle feather" },
          { "value": "0 12px 40px rgba(0,0,0,0.08)", "label": "Editorial floating" }
        ],
        "default": "none"
      }
    ]
  },
  {
    "name": "Buttons",
    "settings": [
      {
        "type": "select",
        "id": "btn_style",
        "label": "Primary button style",
        "options": [
          { "value": "solid", "label": "Solid" },
          { "value": "outline", "label": "Outline" },
          { "value": "magnetic", "label": "Magnetic" }
        ],
        "default": "solid"
      },
      {
        "type": "select",
        "id": "btn_border_radius",
        "label": "Button shape",
        "options": [
          { "value": "match", "label": "Match corner radius" },
          { "value": "999px", "label": "Pill (999px)" },
          { "value": "0px", "label": "Square (0px)" }
        ],
        "default": "match"
      }
    ]
  },
  {
    "name": "Header and navigation",
    "settings": [
      {
        "type": "select",
        "id": "header_sticky_mode",
        "label": "Sticky navigation behavior",
        "options": [
          { "value": "always", "label": "Always sticky" },
          { "value": "on_scroll_up", "label": "Reveal on scroll up" },
          { "value": "none", "label": "Static" }
        ],
        "default": "always"
      },
      {
        "type": "checkbox",
        "id": "header_transparent_hero",
        "label": "Show transparent header over hero",
        "default": true
      },
      {
        "type": "checkbox",
        "id": "header_glassmorphic_blur",
        "label": "Show frosted glass blur",
        "default": true
      }
    ]
  },
  {
    "name": "Predictive search",
    "settings": [
      {
        "type": "select",
        "id": "search_display_type",
        "label": "Search experience",
        "options": [
          { "value": "drawer", "label": "Drawer" },
          { "value": "modal", "label": "Modal" }
        ],
        "default": "drawer"
      },
      {
        "type": "checkbox",
        "id": "search_show_vendor",
        "label": "Show product vendor",
        "default": true
      },
      {
        "type": "checkbox",
        "id": "search_show_price",
        "label": "Show price in results",
        "default": true
      }
    ]
  },
  {
    "name": "Product cards",
    "settings": [
      {
        "type": "select",
        "id": "card_aspect_ratio",
        "label": "Card image aspect ratio",
        "options": [
          { "value": "1/1", "label": "Square (1:1)" },
          { "value": "3/4", "label": "Portrait (3:4)" },
          { "value": "2/3", "label": "Tall (2:3)" }
        ],
        "default": "3/4"
      },
      {
        "type": "checkbox",
        "id": "card_hover_secondary_image",
        "label": "Show secondary image on hover",
        "default": true
      },
      {
        "type": "select",
        "id": "card_quick_add_mode",
        "label": "Quick add trigger",
        "options": [
          { "value": "instant", "label": "Instant add to cart" },
          { "value": "quick_view", "label": "Open quick view modal" },
          { "value": "hidden", "label": "None" }
        ],
        "default": "instant"
      },
      {
        "type": "checkbox",
        "id": "card_show_color_swatches",
        "label": "Show color swatch preview",
        "default": true
      }
    ]
  },
  {
    "name": "Variant swatches",
    "settings": [
      {
        "type": "select",
        "id": "swatch_style",
        "label": "Color swatch presentation",
        "options": [
          { "value": "circle", "label": "Color circles" },
          { "value": "pill", "label": "Pill buttons" },
          { "value": "image_thumb", "label": "Variant images" }
        ],
        "default": "circle"
      },
      {
        "type": "checkbox",
        "id": "swatches_out_of_stock_cross",
        "label": "Strikethrough unavailable variants",
        "default": true
      }
    ]
  },
  {
    "name": "Product page",
    "settings": [
      {
        "type": "select",
        "id": "pdp_gallery_layout",
        "label": "Media gallery layout",
        "options": [
          { "value": "grid_2col", "label": "Two columns" },
          { "value": "stacked", "label": "Stacked" },
          { "value": "thumbnails_left", "label": "Thumbnails left" }
        ],
        "default": "grid_2col"
      },
      {
        "type": "checkbox",
        "id": "enable_sticky_atc",
        "label": "Show floating sticky buy bar",
        "default": true
      },
      {
        "type": "page",
        "id": "size_guide_page",
        "label": "Size guide page content"
      }
    ]
  },
  {
    "name": "Cart",
    "settings": [
      {
        "type": "select",
        "id": "cart_type",
        "label": "Cart type",
        "options": [
          { "value": "drawer", "label": "Drawer" },
          { "value": "page", "label": "Page" },
          { "value": "modal", "label": "Modal" }
        ],
        "default": "drawer"
      },
      {
        "type": "number",
        "id": "free_shipping_threshold",
        "label": "Free shipping threshold",
        "default": 75,
        "info": "Set to 0 to disable progress bar."
      },
      {
        "type": "collection",
        "id": "cart_cross_sell_collection",
        "label": "Cart cross-sell collection",
        "info": "Display recommended items in the cart drawer."
      },
      {
        "type": "checkbox",
        "id": "enable_cart_notes",
        "label": "Show order notes",
        "default": true
      }
    ]
  },
  {
    "name": "Animation and motion",
    "settings": [
      {
        "type": "select",
        "id": "motion_speed",
        "label": "Animation velocity",
        "options": [
          { "value": "deliberate", "label": "Deliberate (400ms)" },
          { "value": "standard", "label": "Standard (250ms)" },
          { "value": "instant", "label": "Instant" }
        ],
        "default": "standard"
      },
      {
        "type": "select",
        "id": "icon_stroke_width",
        "label": "Icon stroke width",
        "options": [
          { "value": "1.0", "label": "Fine (1.0px)" },
          { "value": "1.25", "label": "Standard (1.25px)" },
          { "value": "1.5", "label": "Bold (1.5px)" }
        ],
        "default": "1.25"
      }
    ]
  },
  {
    "name": "Social media",
    "settings": [
      {
        "type": "image_picker",
        "id": "favicon",
        "label": "Favicon"
      },
      {
        "type": "text",
        "id": "social_instagram_link",
        "label": "Instagram link"
      },
      {
        "type": "text",
        "id": "social_twitter_link",
        "label": "Twitter link"
      }
    ]
  }
]
```

---

## 3. Liquid Mapping Engine (`snippets/css-variables.liquid`)

How `settings_schema.json` transforms into CSS custom properties:

```liquid
<style>
  :root {
    /* 1. Colors */
    --color-bg: {{ settings.color_canvas }};
    --color-surface: {{ settings.color_surface }};
    --color-text-primary: {{ settings.color_text_primary }};
    --color-text-muted: {{ settings.color_text_muted }};
    --color-border-subtle: {{ settings.color_border }};
    --color-action-primary: {{ settings.color_accent }};
    --color-action-hover: {{ settings.color_accent_hover }};

    /* 2. Typography */
    --font-heading-family: {{ settings.type_header_font.family }}, {{ settings.type_header_font.fallback_families }};
    --font-heading-weight: {{ settings.type_header_font.weight }};
    --font-body-family: {{ settings.type_body_font.family }}, {{ settings.type_body_font.fallback_families }};
    --font-body-weight: {{ settings.type_body_font.weight }};
    --eyebrow-tracking: {{ settings.eyebrow_letter_spacing }};

    /* 3. Geometry & Radii */
    --radius-base: {{ settings.corner_radius_preset }};
    --radius-button: {% if settings.btn_border_radius == 'match' %}{{ settings.corner_radius_preset }}{% else %}{{ settings.btn_border_radius }}{% endif %};
    --card-shadow: {{ settings.card_shadow }};

    /* 4. Layout & Cards */
    --card-aspect-ratio: {{ settings.card_aspect_ratio }};
    --icon-stroke-width: {{ settings.icon_stroke_width }}px;

    /* 5. Motion Durations */
    --motion-duration: {% if settings.motion_speed == 'deliberate' %}400ms{% elsif settings.motion_speed == 'standard' %}250ms{% else %}0ms{% endif %};
  }
</style>
```

---

## 4. Shopify Theme Store Schema Compliance

Per [Shopify Theme Store Requirements](theme-store-requirements.md) Section 14:
1. **Sentence Case**: All category, section, preset, and setting names must be in sentence case (e.g. "Header and navigation", not "Header & Navigation").
2. **American English**: Always use American spelling (`color`, `center`, `catalog`, `dialog`, `canceled`).
3. **No Ampersands**: Never use `&` in settings labels or section names (always write "and").
4. **Official Shopify Terminology**: Use `home page` (not homepage), `top bar` (not meta-nav), `button label` (not button name), `body text` (not main text), `slideshow` (not slider), `cart type` (not Ajax cart).
5. **Declarative Tone**: Use declarative statements ("Use custom logo", never questions like "Use custom logo?").
6. **Theme Info Block**: Must include a `theme_info` section in `config/settings_schema.json` with version and support URLs.
7. **Paired Colors**: Every background color setting must be accompanied by a corresponding foreground color setting.
8. **Navigation Menus**: Settings of type `link_list` must default to `"main-menu"` in the header, or `"footer"` in the footer.
