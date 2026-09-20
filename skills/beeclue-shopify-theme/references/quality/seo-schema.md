# SEO Architecture & JSON-LD Structured Data

Every BeeClue Shopify storefront is architected for maximum organic search indexing and rich snippet visibility across Google and modern AI search engines.

---

## 1. Dynamic JSON-LD Schema Snippet (`snippets/json-ld.liquid`)

Rendered in `layout/theme.liquid` via `{% render 'json-ld' %}`:

```liquid
{%- comment -%}
  Dynamic JSON-LD Structured Data Engine
{%- endcomment -%}

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": {{ shop.name | json }},
  "url": {{ shop.url | append: page.url | json }},
  {% if settings.logo != blank %}
    "logo": {{ settings.logo | image_url: width: 500 | prepend: 'https:' | json }},
  {% endif %}
  "sameAs": [
    {{ settings.social_instagram_link | json }},
    {{ settings.social_facebook_link | json }},
    {{ settings.social_twitter_link | json }}
  ]
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": {{ shop.name | json }},
  "url": {{ shop.url | json }},
  "potentialAction": {
    "@type": "SearchAction",
    "target": {{ shop.url | append: routes.search_url | append: '?q={search_term_string}' | json }},
    "query-input": "required name=search_term_string"
  }
}
</script>

{%- if request.page_type == 'product' -%}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": {{ product.title | json }},
  "description": {{ product.description | strip_html | truncatewords: 60 | json }},
  "image": [
    {{ product.featured_image | image_url: width: 1200 | prepend: 'https:' | json }}
  ],
  "sku": {{ product.selected_or_first_available_variant.sku | default: product.id | json }},
  "brand": {
    "@type": "Brand",
    "name": {{ product.vendor | default: shop.name | json }}
  },
  "offers": [
    {%- for variant in product.variants -%}
      {
        "@type": "Offer",
        "name": {{ variant.title | json }},
        "price": {{ variant.price | divided_by: 100.00 | json }},
        "priceCurrency": {{ cart.currency.iso_code | json }},
        "availability": "{% if variant.available %}https://schema.org/InStock{% else %}https://schema.org/OutOfStock{% endif %}",
        "url": {{ shop.url | append: variant.url | json }},
        "sku": {{ variant.sku | default: variant.id | json }}
      }{%- unless forloop.last -%},{%- endunless -%}
    {%- endfor -%}
  ]
}
</script>
{%- endif -%}

{%- if request.page_type == 'article' -%}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {{ article.title | json }},
  "image": [
    {{ article.image | image_url: width: 1200 | prepend: 'https:' | json }}
  ],
  "datePublished": {{ article.published_at | date: '%Y-%m-%dT%H:%M:%SZ' | json }},
  "dateModified": {{ article.updated_at | default: article.published_at | date: '%Y-%m-%dT%H:%M:%SZ' | json }},
  "author": {
    "@type": "Person",
    "name": {{ article.author | json }}
  },
  "publisher": {
    "@type": "Organization",
    "name": {{ shop.name | json }}
  }
}
</script>
{%- endif -%}
```
