# SEO Architecture & JSON-LD Structured Data

Every BeeClue digital storefront is architected for maximum organic search indexing and rich snippet visibility across Google and modern AI search engines.

---

## 1. Dynamic JSON-LD Schema Engine (`inc/seo.php`)

Output structured data automatically via `wp_head`:

```php
add_action('wp_head', function() {
    $schema = [];

    // 1. Organization Schema
    $org = [
        '@type' => 'Organization',
        'name'  => get_bloginfo('name'),
        'url'   => home_url('/'),
        'logo'  => 'https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-blue.png',
    ];

    // 2. WebSite Schema with SearchAction
    $schema[] = [
        '@context'        => 'https://schema.org',
        '@type'           => 'WebSite',
        'name'            => get_bloginfo('name'),
        'url'             => home_url('/'),
        'publisher'       => $org,
        'potentialAction' => [
            '@type'       => 'SearchAction',
            'target'      => home_url('/?s={search_term_string}'),
            'query-input' => 'required name=search_term_string',
        ],
    ];

    // 3. Product Schema on Single Product Pages
    if (is_singular('product')) {
        global $product;
        if ($product) {
            $schema[] = [
                '@context'    => 'https://schema.org',
                '@type'       => 'Product',
                'name'        => $product->get_name(),
                'description' => wp_strip_all_tags($product->get_short_description() ?: $product->get_description()),
                'image'       => wp_get_attachment_url($product->get_image_id()),
                'sku'         => $product->get_sku() ?: 'SKU-' . $product->get_id(),
                'offers'      => [
                    '@type'         => 'Offer',
                    'url'           => get_permalink(),
                    'priceCurrency' => get_woocommerce_currency(),
                    'price'         => $product->get_price(),
                    'availability'  => $product->is_in_stock() ? 'https://schema.org/InStock' : 'https://schema.org/OutOfStock',
                ],
            ];
        }
    }

    // 4. BreadcrumbList on Inner Pages
    if (!is_front_page()) {
        $schema[] = [
            '@context'        => 'https://schema.org',
            '@type'           => 'BreadcrumbList',
            'itemListElement' => [
                ['@type' => 'ListItem', 'position' => 1, 'name' => 'Home', 'item' => home_url('/')],
                ['@type' => 'ListItem', 'position' => 2, 'name' => get_the_title(), 'item' => get_permalink()],
            ],
        ];
    }

    // Output all schemas
    foreach ($schema as $item) {
        echo '<script type="application/ld+json">' . wp_json_encode($item, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . '</script>' . "\n";
    }
});
```
