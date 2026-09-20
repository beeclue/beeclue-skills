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
