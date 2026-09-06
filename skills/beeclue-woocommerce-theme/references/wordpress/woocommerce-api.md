# WooCommerce API, Store API & WP-CLI Integration

BeeClue themes integrate with current WooCommerce architectures, avoiding deprecated templates and hooks.

---

## 1. WooCommerce Theme Support Registration

In `functions.php`:
```php
add_action('after_setup_theme', function() {
    add_theme_support('woocommerce');
    add_theme_support('wc-product-gallery-zoom');
    add_theme_support('wc-product-gallery-lightbox');
    add_theme_support('wc-product-gallery-slider');
});
```

---

## 2. WP-CLI Scaffolding Automation

When deploying or testing a store, execute these commands via WP-CLI:

```bash
# 1. Install & Activate WooCommerce
wp plugin install woocommerce --activate

# 2. Install Sample Products for Immediate Visuals
wp plugin install wordpress-importer --activate
wp import wp-content/plugins/woocommerce/sample-data/sample_products.xml --authors=create

# 3. Ensure Core Shop Pages Exist
wp wc tool run install_pages --user=1

# 4. Activate Custom Beeclue Theme
wp theme activate beeclue-{slug}-theme

# 5. Create Key Pages & Assign Templates
wp post create --post_type=page --post_title="Home" --post_status=publish --page_template=template-home.php
wp post create --post_type=page --post_title="About Us" --post_status=publish --page_template=template-about.php
wp post create --post_type=page --post_title="Contact" --post_status=publish --page_template=template-contact.php
wp post create --post_type=page --post_title="FAQ" --post_status=publish --page_template=template-faq.php

# 6. Set Static Front Page
wp option update show_on_front page
wp option update page_on_front $(wp post list --post_type=page --title="Home" --field=ID)

# 7. Build Primary Navigation Menu
wp menu create "Primary Menu"
wp menu location assign "Primary Menu" primary
wp menu item add-post "Primary Menu" $(wp post list --post_type=page --title="Home" --field=ID) --title="Home"
wp menu item add-post "Primary Menu" $(wp option get woocommerce_shop_page_id) --title="Shop"
wp menu item add-post "Primary Menu" $(wp post list --post_type=page --title="About Us" --field=ID) --title="About"
wp menu item add-post "Primary Menu" $(wp post list --post_type=page --title="Contact" --field=ID) --title="Contact"
```
