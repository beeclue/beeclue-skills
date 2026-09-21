# Modern Liquid Best Practices & Performance Optimization

Modern Shopify themes must achieve 90+ Core Web Vitals and meet strict Shopify Theme Store quality standards. Writing performant, idiomatic Liquid is essential.

---

## 1. Native Responsive Image Tagging

Never write static, unoptimized `<img>` tags. Always use Shopify's native `image_url` and `image_tag` filters with responsive `srcset` generation:

```liquid
{%- comment -%}
  High-Performance Responsive Image Helper
{%- endcomment -%}
{%- if image != blank -%}
  {{
    image
    | image_url: width: 1500
    | image_tag:
      loading: 'lazy',
      decoding: 'async',
      sizes: '(min-width: 1200px) 600px, (min-width: 768px) 50vw, 100vw',
      widths: '375, 550, 750, 1100, 1500, 1780',
      alt: image.alt | default: product.title | escape,
      class: 'product-card-image'
  }}
{%- endif -%}
```

### 1.1 Above-The-Fold Hero Image Optimization (LCP)
For the primary hero banner, bypass lazy loading to maximize Largest Contentful Paint (LCP):
```liquid
{{
  section.settings.image
  | image_url: width: 2400
  | image_tag:
    loading: 'eager',
    fetchpriority: 'high',
    decoding: 'sync',
    sizes: '100vw',
    widths: '750, 1100, 1500, 1780, 2000, 2400',
    alt: section.settings.image.alt | default: shop.name | escape,
    class: 'hero-banner-image'
}}
```

---

## 2. Escaping & Sanitization Standards

Prevent XSS vulnerabilities and invalid JSON encoding:
- **HTML Attributes**: Always escape text inside attributes: `<input value="{{ customer.first_name | escape }}">`.
- **Headings & Body Copy**: Use `{{ page_description | escape }}` and `{{ product.description }}` (which is already sanitized rich text).
- **JavaScript Objects**: When passing Liquid data to JavaScript, always use the `json` filter:
  ```html
  <script type="application/json" id="ProductData-{{ product.id }}">
    {{ product | json }}
  </script>
  ```

---

## 3. Currency Formatting Standards

Always format prices using store settings rather than hardcoding dollar signs:
```liquid
<span class="price-regular">{{ product.price | money }}</span>
{%- if product.compare_at_price > product.price -%}
  <span class="price-compare">{{ product.compare_at_price | money }}</span>
{%- endif -%}
```

---

## 4. Avoiding Liquid Antipatterns

1. **No Nested Loops**: Avoid iterating over all products inside a collection loop to find matching tags or vendors. This causes $O(N^2)$ execution times that slow down server response.
2. **Paginate Early**: Always wrap product and article loops with `{% paginate %}`:
   ```liquid
   {% paginate collection.products by 24 %}
     {% for product in collection.products %}
       {% render 'product-card', product: product %}
     {% endfor %}
     {{ paginate | default_pagination }}
   {% endpaginate %}
   ```
3. **Use Snippet Parameters**: Explicitly pass objects to snippets instead of relying on global scope:
   - ✅ `{% render 'product-card', product: item, aspect_ratio: '3/4' %}`
   - ❌ `{% include 'product-card' %}` (Deprecated and leaks variables).

---

## 5. Section Schema Best Practices

- Always declare `"presets"` in modular sections so merchants can insert them anywhere on JSON templates:
```json
{% schema %}
{
  "name": "Featured Collection",
  "tag": "section",
  "class": "section-featured-collection",
  "settings": [
    {
      "type": "text",
      "id": "title",
      "label": "Heading",
      "default": "Featured Works"
    }
  ],
  "presets": [
    {
      "name": "Featured Collection"
    }
  ]
}
{% endschema %}
```

---

## 6. Shopify Theme Store Liquid & Storefront Requirements

Per [Shopify Theme Store Requirements](theme-store-requirements.md), every theme must adhere to these Liquid rules:

### 6.1 Dynamic Storefront URLs (`routes` Object)
Never hardcode URLs like `href="/"`, `href="/cart"`, or `href="/search"`. Always use the `routes` object to support multiple languages and custom Shopify routing:
- `{{ routes.root_url }}` (Home page)
- `{{ routes.cart_url }}` (Cart page)
- `{{ routes.cart_add_url }}` (Cart add endpoint)
- `{{ routes.cart_change_url }}` (Cart change endpoint)
- `{{ routes.search_url }}` (Search template)
- `{{ routes.predictive_search_url }}` (Predictive search endpoint)
- `{{ routes.all_products_collection_url }}` (All products collection)

### 6.2 Taxes Included & Unit Pricing
- **Taxes Included**: Always indicate when taxes are included in price:
  ```liquid
  {%- if cart.taxes_included -%}
    <span class="tax-note">{{ 'sections.cart.taxes_included' | t }}</span>
  {%- endif -%}
  ```
- **Unit Pricing**: Output unit price on PDP, collection cards, and cart:
  ```liquid
  {%- if variant.unit_price_measurement -%}
    <span class="unit-price">
      {{ variant.unit_price | money }} /
      {%- if variant.unit_price_measurement.reference_value != 1 -%}
        {{ variant.unit_price_measurement.reference_value }}
      {%- endif -%}
      {{ variant.unit_price_measurement.reference_unit }}
    </span>
  {%- endif -%}
  ```

### 6.3 Full-Color Payment Icons
Output payment icons using Shopify's official SVG filter (must be rendered in full color):
```liquid
{%- for type in shop.enabled_payment_types -%}
  {{ type | payment_type_svg_tag: class: 'payment-icon' }}
{%- endfor -%}
```

### 6.4 Font Loading with `font_modify`
Shopify font pickers require bold, italic, and bold-italic variants to be loaded dynamically:
```liquid
{% style %}
  {{ settings.heading_font | font_face: font_display: 'swap' }}
  {{ settings.heading_font | font_modify: 'weight', 'bold' | font_face: font_display: 'swap' }}
  {{ settings.heading_font | font_modify: 'style', 'italic' | font_face: font_display: 'swap' }}
  {{ settings.body_font | font_face: font_display: 'swap' }}
  {{ settings.body_font | font_modify: 'weight', 'bold' | font_face: font_display: 'swap' }}
  {{ settings.body_font | font_modify: 'style', 'italic' | font_face: font_display: 'swap' }}
{% endstyle %}
```

### 6.5 Account Component & Follow on Shop
- Render `<shopify-account></shopify-account>` in both desktop and mobile headers.
- Render `{{ shop | login_button: action: 'follow' }}` without modifying branded button colors.
