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
    "name": "1. Brand Colors & 5-Layer Tokens",
    "settings": [
      {
        "type": "header",
        "content": "Surface & Canvas Colors"
      },
      {
        "type": "color",
        "id": "color_canvas",
        "label": "Canvas Background",
        "default": "#F7F3EE",
        "info": "The primary page canvas tone."
      },
      {
        "type": "color",
        "id": "color_surface",
        "label": "Surface / Card Background",
        "default": "#FFFFFF"
      },
      {
        "type": "header",
        "content": "Text & Line Colors"
      },
      {
        "type": "color",
        "id": "color_text_primary",
        "label": "Primary Text & Ink",
        "default": "#1C1915"
      },
      {
        "type": "color",
        "id": "color_text_muted",
        "label": "Muted / Secondary Text",
        "default": "#70695E"
      },
      {
        "type": "color",
        "id": "color_border",
        "label": "Subtle Hairline Borders",
        "default": "rgba(28, 25, 21, 0.12)"
      },
      {
        "type": "header",
        "content": "Action & Conversion Accent"
      },
      {
        "type": "color",
        "id": "color_accent",
        "label": "Primary Conversion Accent",
        "default": "#C8602A",
        "info": "Used for checkout CTA, free shipping progress fill, and active swatches."
      },
      {
        "type": "color",
        "id": "color_accent_hover",
        "label": "Accent Hover State",
        "default": "#B25220"
      }
    ]
  },
  {
    "name": "2. Typography & Fluid Scale",
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
      },
      {
        "type": "range",
        "id": "heading_scale_percent",
        "min": 80,
        "max": 140,
        "step": 5,
        "unit": "%",
        "label": "Heading Scale Multiplier",
        "default": 100
      },
      {
        "type": "checkbox",
        "id": "heading_uppercase",
        "label": "Uppercase Section Titles",
        "default": false
      },
      {
        "type": "select",
        "id": "eyebrow_letter_spacing",
        "label": "Eyebrow Tracking",
        "options": [
          { "value": "0.05em", "label": "Subtle (0.05em)" },
          { "value": "0.15em", "label": "Editorial Luxury (0.15em)" },
          { "value": "0.25em", "label": "Haute Monograph (0.25em)" }
        ],
        "default": "0.15em"
      }
    ]
  },
  {
    "name": "3. Geometry & Corner Radii",
    "settings": [
      {
        "type": "select",
        "id": "corner_radius_preset",
        "label": "Corner Radius Preset",
        "options": [
          { "value": "0px", "label": "Sharp Architectural (0px)" },
          { "value": "4px", "label": "Subtle Refinement (4px)" },
          { "value": "12px", "label": "Smooth Contemporary (12px)" },
          { "value": "24px", "label": "Organic Soft (24px)" }
        ],
        "default": "0px"
      },
      {
        "type": "select",
        "id": "card_shadow",
        "label": "Surface Elevation / Shadow",
        "options": [
          { "value": "none", "label": "None (Flat Hairline)" },
          { "value": "0 4px 20px rgba(0,0,0,0.04)", "label": "Subtle Feather" },
          { "value": "0 12px 40px rgba(0,0,0,0.08)", "label": "Editorial Floating" }
        ],
        "default": "none"
      }
    ]
  },
  {
    "name": "4. Buttons & Interactions",
    "settings": [
      {
        "type": "select",
        "id": "btn_style",
        "label": "Primary Button Style",
        "options": [
          { "value": "solid", "label": "Filled Solid" },
          { "value": "outline", "label": "Hairline Outline" },
          { "value": "magnetic", "label": "Magnetic Cursor Follow" }
        ],
        "default": "solid"
      },
      {
        "type": "select",
        "id": "btn_border_radius",
        "label": "Button Shape",
        "options": [
          { "value": "match", "label": "Match Corner Radius Preset" },
          { "value": "999px", "label": "Pill Contour (999px)" },
          { "value": "0px", "label": "Square (0px)" }
        ],
        "default": "match"
      }
    ]
  },
  {
    "name": "5. Header & Navigation",
    "settings": [
      {
        "type": "select",
        "id": "header_sticky_mode",
        "label": "Sticky Navigation Behavior",
        "options": [
          { "value": "always", "label": "Always Sticky" },
          { "value": "on_scroll_up", "label": "Reveal on Scroll Up" },
          { "value": "none", "label": "Static (No Stick)" }
        ],
        "default": "always"
      },
      {
        "type": "checkbox",
        "id": "header_transparent_hero",
        "label": "Enable Transparent Header over Hero",
        "default": true
      },
      {
        "type": "checkbox",
        "id": "header_glassmorphic_blur",
        "label": "Enable Frosted Glass Blur",
        "default": true
      }
    ]
  },
  {
    "name": "6. Predictive Search & Discovery",
    "settings": [
      {
        "type": "select",
        "id": "search_display_type",
        "label": "Search Experience",
        "options": [
          { "value": "drawer", "label": "Slide-out Search Drawer" },
          { "value": "modal", "label": "Full-screen Overlay Modal" }
        ],
        "default": "drawer"
      },
      {
        "type": "checkbox",
        "id": "search_show_vendor",
        "label": "Show Product Brand/Vendor",
        "default": true
      },
      {
        "type": "checkbox",
        "id": "search_show_price",
        "label": "Show Pricing in Results",
        "default": true
      }
    ]
  },
  {
    "name": "7. Product Cards & Catalog",
    "settings": [
      {
        "type": "select",
        "id": "card_aspect_ratio",
        "label": "Card Image Aspect Ratio",
        "options": [
          { "value": "1/1", "label": "Square (1:1)" },
          { "value": "3/4", "label": "Editorial Portrait (3:4)" },
          { "value": "2/3", "label": "Tall Portrait (2:3)" }
        ],
        "default": "3/4"
      },
      {
        "type": "checkbox",
        "id": "card_hover_secondary_image",
        "label": "Show Secondary Image on Hover",
        "default": true
      },
      {
        "type": "select",
        "id": "card_quick_add_mode",
        "label": "Quick Add Trigger",
        "options": [
          { "value": "instant", "label": "Instant Add to Cart" },
          { "value": "quick_view", "label": "Open Quick View Modal" },
          { "value": "hidden", "label": "None (Navigate to PDP)" }
        ],
        "default": "instant"
      },
      {
        "type": "checkbox",
        "id": "card_show_color_swatches",
        "label": "Show Color Swatch Preview",
        "default": true
      }
    ]
  },
  {
    "name": "8. Variant Swatches & Selectors",
    "settings": [
      {
        "type": "select",
        "id": "swatch_style",
        "label": "Color Swatch Presentation",
        "options": [
          { "value": "circle", "label": "Minimalist Color Circles" },
          { "value": "pill", "label": "Textured Pill Buttons" },
          { "value": "image_thumb", "label": "Variant Thumbnail Images" }
        ],
        "default": "circle"
      },
      {
        "type": "checkbox",
        "id": "swatches_out_of_stock_cross",
        "label": "Strikethrough Out-of-Stock Variants",
        "default": true
      }
    ]
  },
  {
    "name": "9. Product Details Page (PDP)",
    "settings": [
      {
        "type": "select",
        "id": "pdp_gallery_layout",
        "label": "Media Gallery Layout",
        "options": [
          { "value": "grid_2col", "label": "Asymmetric 2-Column Grid" },
          { "value": "stacked", "label": "Full-Width Stacked" },
          { "value": "thumbnails_left", "label": "Thumbnails Strip (Left)" }
        ],
        "default": "grid_2col"
      },
      {
        "type": "checkbox",
        "id": "enable_sticky_atc",
        "label": "Enable Floating Sticky Buy Bar",
        "default": true
      },
      {
        "type": "page",
        "id": "size_guide_page",
        "label": "Global Size Guide Page Content"
      }
    ]
  },
  {
    "name": "10. Cart Drawer & Shipping Milestones",
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
        "label": "Free Shipping Threshold ($)",
        "default": 75,
        "info": "Set to 0 to disable progress bar."
      },
      {
        "type": "collection",
        "id": "cart_cross_sell_collection",
        "label": "In-Drawer Cross-Sell Collection",
        "info": "Display 2-3 impulse accessories at the bottom of the drawer."
      },
      {
        "type": "checkbox",
        "id": "enable_cart_notes",
        "label": "Enable Order Inscription / Gift Note",
        "default": true
      }
    ]
  },
  {
    "name": "11. Luxury Micro-Interactions & Motion",
    "settings": [
      {
        "type": "select",
        "id": "motion_speed",
        "label": "Animation Velocity",
        "options": [
          { "value": "deliberate", "label": "Deliberate & Velvety (400ms)" },
          { "value": "standard", "label": "Crisp Responsive (250ms)" },
          { "value": "instant", "label": "Reduced Motion / Instant" }
        ],
        "default": "standard"
      },
      {
        "type": "select",
        "id": "icon_stroke_width",
        "label": "Icon Stroke Width",
        "options": [
          { "value": "1.0", "label": "Ultra-Fine Hairline (1.0px)" },
          { "value": "1.25", "label": "Luxury Standard (1.25px)" },
          { "value": "1.5", "label": "Modern Bold (1.5px)" }
        ],
        "default": "1.25"
      }
    ]
  },
  {
    "name": "12. Social Accounts & Favicon",
    "settings": [
      {
        "type": "image_picker",
        "id": "favicon",
        "label": "Favicon Image (32x32 PNG)"
      },
      {
        "type": "text",
        "id": "social_instagram_link",
        "label": "Instagram URL"
      },
      {
        "type": "text",
        "id": "social_twitter_link",
        "label": "X / Twitter URL"
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
