# Theme Engineering & Modular Component Architecture

BeeClue themes are constructed like modern component-driven software applications rather than messy monolithic WordPress themes.

---

## 1. Modular Directory Structure

```
wp-content/themes/beeclue-{name}-theme/
├── style.css                      # Theme header + 5-layer design tokens + reset
├── functions.php                  # Enqueues, setup, WC hooks, nav menus, sidebars, AJAX handlers
├── header.php                     # HTML skeleton + dynamic wp_nav_menu + overlay loaders
├── footer.php                     # 4-col footer + dynamic footer menus + mandatory Beeclue branding
├── woocommerce.css                # Polished WooCommerce overrides
├── index.php                      # Core WordPress universal fallback loop
├── home.php                       # Blog posts index / editorial magazine layout
├── single.php                     # Single post article layout with comments & author bio
├── archive.php                    # Taxonomy archive (categories, tags, dates, authors)
├── page.php                       # Default page template for custom user pages
├── comments.php                   # Accessible, styled native comment thread & form
├── sidebar.php                    # Dynamic widgetized sidebar (register_sidebar)
├── template-home.php              # Homepage flagship template (7 chapters)
├── template-about.php             # About Us template
├── template-contact.php           # Contact template
├── template-faq.php               # FAQ template
├── 404.php                        # Recoverable 404 page
├── search.php                     # Search results grid
├── template-parts/                # REUSABLE MODULAR PARTIALS
│   ├── header/
│   │   ├── nav-desktop.php        # Dynamic wp_nav_menu with multi-level dropdowns
│   │   ├── nav-mobile.php         # Dynamic wp_nav_menu with mobile accordion submenus
│   │   └── search-overlay.php     # Accessible search dialog
│   ├── product/
│   │   ├── card.php               # Hover quick-add, aspect-ratio lock
│   │   └── sticky-bar.php         # Single product floating Add-to-Cart bar
│   ├── post/
│   │   ├── card.php               # Blog card: thumbnail, category pill, reading time
│   │   └── author-bio.php         # Author avatar, biographical note, social links
│   ├── cart/
│   │   ├── drawer.php             # AJAX slide-out cart drawer
│   │   └── shipping-bar.php       # Dynamic free shipping progress meter
│   └── ui/
│       ├── trust-marquee.php      # Infinite CSS ticker with hover-pause
│       └── live-region.php        # Screen reader aria-live polite region
├── assets/
│   ├── js/
│   │   ├── main.js                # Nav, dropdown keyboard traps, search modal
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

---

## 4. Dynamic WordPress Navigation & Multi-Level Submenus

Never hardcode navigation links. The theme must grant the user complete sovereignty to construct, edit, reorder, and nest navigation hierarchies from **wp-admin > Appearance > Menus**.

### 4.1 Registering Multiple Menu Locations (`functions.php`)
```php
function beeclue_register_navigation_menus() {
    register_nav_menus([
        'primary'   => esc_html__('Primary Header Navigation (Multi-Level Dropdowns)', 'beeclue'),
        'mobile'    => esc_html__('Mobile Navigation Drawer (Accordion Submenus)', 'beeclue'),
        'footer_1'  => esc_html__('Footer Column 1 (Explore / Shop)', 'beeclue'),
        'footer_2'  => esc_html__('Footer Column 2 (Company / Editorial)', 'beeclue'),
        'secondary' => esc_html__('Utility / Top Bar Navigation', 'beeclue'),
    ]);
}
add_action('after_setup_theme', 'beeclue_register_navigation_menus');
```

### 4.2 Dynamic Rendering via `wp_nav_menu()` (`template-parts/header/nav-desktop.php`)
```php
<nav class="site-nav-desktop" id="site-navigation" aria-label="<?php esc_attr_e('Primary Navigation', 'beeclue'); ?>">
    <?php
    wp_nav_menu([
        'theme_location' => 'primary',
        'container'      => false,
        'menu_class'     => 'nav-menu-primary',
        'fallback_cb'    => 'beeclue_nav_fallback',
        'depth'          => 3, // Enable deep nested submenu hierarchies
    ]);
    ?>
</nav>
```

### 4.3 Clean Fallback Callback (`functions.php`)
When no menu is assigned in `wp-admin`, provide a clean fallback that lists published pages rather than breaking:
```php
function beeclue_nav_fallback() {
    echo '<ul class="nav-menu-primary nav-menu-fallback">';
    wp_list_pages([
        'title_li' => '',
        'depth'    => 2,
        'number'   => 5,
    ]);
    echo '</ul>';
}
```

### 4.4 Bespoke Custom Styling for Submenus & Sub-Submenus (`style.css`)

> [!IMPORTANT]
> **Data Source vs. Styling Separation**:
> - **Source of Truth**: 100% WordPress Core (`wp_nav_menu()` populated by the client in `wp-admin > Appearance > Menus`). Users can add, delete, rename, reorder, and nest menu items at will.
> - **Styling & Interaction**: 100% Bespoke Custom CSS & JS. WordPress outputs standard semantic HTML (`<ul>`, `<li>`, `.sub-menu`). The theme styles all tiers (Top Level, Level 1 Submenu, Level 2 Sub-Submenu Flyout, and Mobile Drawer Accordions) using the 5-layer design tokens.

WordPress automatically attaches `.menu-item-has-children` to any item with children and renders child items inside `<ul class="sub-menu">`. The custom CSS handles all tiers with luxury elevation, micro-interactions, and accessible keyboard navigation:

```css
/* ─────────────────────────────────────────────────────────────
   TIER 0: TOP-LEVEL NAVIGATION BAR
   ───────────────────────────────────────────────────────────── */
.nav-menu-primary {
    display: flex;
    align-items: center;
    gap: 2rem;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-menu-primary > li {
    position: relative;
}

.nav-menu-primary > li > a {
    color: var(--color-text-primary);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.938rem;
    letter-spacing: -0.01em;
    padding: 0.75rem 0;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    transition: color var(--motion-duration-fast) ease;
}

/* Custom Chevron Indicator on Top-Level Parents */
.nav-menu-primary > li.menu-item-has-children > a::after {
    content: '';
    display: inline-block;
    width: 6px;
    height: 6px;
    border-right: 1.5px solid currentColor;
    border-bottom: 1.5px solid currentColor;
    transform: rotate(45deg) translateY(-2px);
    transition: transform var(--motion-duration-fast) ease;
}

.nav-menu-primary > li.menu-item-has-children:hover > a::after,
.nav-menu-primary > li.menu-item-has-children:focus-within > a::after {
    transform: rotate(225deg) translateY(-2px);
}

/* ─────────────────────────────────────────────────────────────
   TIER 1: SUBMENU (LEVEL 1 DROPDOWN)
   ───────────────────────────────────────────────────────────── */
.nav-menu-primary .sub-menu {
    position: absolute;
    top: 100%;
    left: 0;
    min-width: 230px;
    background: var(--color-surface-base);
    border: 1px solid var(--color-border-subtle);
    border-radius: var(--radius-sm);
    box-shadow: var(--shadow-card);
    list-style: none;
    padding: 0.5rem 0;
    margin: 0.5rem 0 0 0;
    opacity: 0;
    visibility: hidden;
    transform: translateY(8px);
    transition: opacity var(--motion-duration-fast) ease,
                transform var(--motion-duration-fast) ease,
                visibility var(--motion-duration-fast);
    z-index: 100;
}

.nav-menu-primary .sub-menu li {
    position: relative;
    padding: 0;
    margin: 0;
}

.nav-menu-primary .sub-menu a {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.625rem 1.25rem;
    font-size: 0.875rem;
    color: var(--color-text-secondary);
    text-decoration: none;
    transition: all var(--motion-duration-fast) ease;
}

.nav-menu-primary .sub-menu a:hover,
.nav-menu-primary .sub-menu a:focus {
    color: var(--color-action-primary);
    background: var(--color-surface-sunken);
}

/* ─────────────────────────────────────────────────────────────
   TIER 2: SUB-SUBMENU (LEVEL 2 TERTIARY FLYOUT)
   ───────────────────────────────────────────────────────────── */
.nav-menu-primary .sub-menu .sub-menu {
    top: -0.5rem;
    left: 100%;
    margin: 0 0 0 0.35rem;
    box-shadow: var(--shadow-drawer);
}

/* Custom Horizontal Flyout Arrow for Submenu Parents */
.nav-menu-primary .sub-menu li.menu-item-has-children > a::after {
    content: '';
    display: inline-block;
    width: 5px;
    height: 5px;
    border-right: 1.5px solid currentColor;
    border-top: 1.5px solid currentColor;
    transform: rotate(45deg);
    margin-left: auto;
}

/* Accessible reveal on :hover AND :focus-within across all tiers */
.nav-menu-primary li:hover > .sub-menu,
.nav-menu-primary li:focus-within > .sub-menu {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

/* Reverse flyout if nearing right viewport edge */
.nav-menu-primary li.flyout-left > .sub-menu {
    left: auto;
    right: 100%;
    margin: 0 0.35rem 0 0;
}
```

### 4.5 Mobile Drawer Accordion Submenu Toggles (`assets/js/main.js`)
On mobile screens, submenus must not hover-reveal. Add accessible chevron toggle buttons dynamically:
```javascript
// Enhance mobile menu items with children with accordion toggle buttons
document.querySelectorAll('.site-nav-mobile .menu-item-has-children').forEach((item) => {
    const toggleBtn = document.createElement('button');
    toggleBtn.setAttribute('type', 'button');
    toggleBtn.className = 'submenu-toggle-btn';
    toggleBtn.setAttribute('aria-expanded', 'false');
    toggleBtn.setAttribute('aria-label', 'Toggle sub-menu');
    toggleBtn.innerHTML = '<svg width="12" height="12" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" stroke="currentColor" fill="none" stroke-width="1.5"/></svg>';
    
    item.insertBefore(toggleBtn, item.querySelector('.sub-menu'));
    
    toggleBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const expanded = toggleBtn.getAttribute('aria-expanded') === 'true';
        toggleBtn.setAttribute('aria-expanded', !expanded);
        item.classList.toggle('submenu-open', !expanded);
    });
});
```

---

## 5. Native WordPress Publishing Engine: Blog, Pagination & Widgets

Never treat the store as a static brochure. The theme must integrate the full WordPress blogging, magazine, and archive capability:

### 5.1 Blog Posts Archive (`home.php` / `index.php`)
```php
<?php get_header(); ?>
<main id="primary" class="site-main site-blog-archive">
    <header class="blog-header section-spacing-sm">
        <div class="container">
            <span class="eyebrow"><?php esc_html_e('Editorial Journal', 'beeclue'); ?></span>
            <h1 class="page-title"><?php single_post_title(); ?></h1>
        </div>
    </header>

    <div class="container">
        <?php if (have_posts()) : ?>
            <div class="blog-post-grid">
                <?php while (have_posts()) : the_post(); ?>
                    <?php get_template_part('template-parts/post/card'); ?>
                <?php endwhile; ?>
            </div>

            <nav class="pagination-wrapper" aria-label="<?php esc_attr_e('Posts Navigation', 'beeclue'); ?>">
                <?php
                the_posts_pagination([
                    'mid_size'  => 2,
                    'prev_text' => '&larr; ' . esc_html__('Previous', 'beeclue'),
                    'next_text' => esc_html__('Next', 'beeclue') . ' &rarr;',
                ]);
                ?>
            </nav>
        <?php else : ?>
            <p><?php esc_html_e('No editorial dispatches found.', 'beeclue'); ?></p>
        <?php endif; ?>
    </div>
</main>
<?php get_footer(); ?>
```

### 5.2 Single Editorial Post (`single.php`)
```php
<?php get_header(); ?>
<main id="primary" class="site-main single-post-main">
    <?php while (have_posts()) : the_post(); ?>
        <article id="post-<?php the_ID(); ?>" <?php post_class('editorial-article container'); ?>>
            <header class="entry-header">
                <div class="entry-meta">
                    <span class="entry-category"><?php the_category(', '); ?></span>
                    <span class="entry-date"><?php echo esc_html(get_the_date()); ?></span>
                </div>
                <h1 class="entry-title"><?php the_title(); ?></h1>
            </header>

            <?php if (has_post_thumbnail()) : ?>
                <div class="entry-featured-image">
                    <?php the_post_thumbnail('full', ['loading' => 'eager']); ?>
                </div>
            <?php endif; ?>

            <div class="entry-content">
                <?php the_content(); ?>
            </div>

            <footer class="entry-footer">
                <?php get_template_part('template-parts/post/author-bio'); ?>
                <?php the_post_navigation(); ?>
            </footer>

            <?php
            if (comments_open() || get_comments_number()) :
                comments_template();
            endif;
            ?>
        </article>
    <?php endwhile; ?>
</main>
<?php get_footer(); ?>
```

### 5.3 Widgetized Dynamic Sidebars & Footer Areas (`functions.php`)
```php
function beeclue_widgets_init() {
    register_sidebar([
        'name'          => esc_html__('Blog Sidebar', 'beeclue'),
        'id'            => 'sidebar-blog',
        'description'   => esc_html__('Add widgets here to appear in the editorial journal sidebar.', 'beeclue'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ]);
}
add_action('widgets_init', 'beeclue_widgets_init');
```

---

## 6. Dynamic WordPress Data Architecture & Pure UI Separation

> [!IMPORTANT]
> **The Core Mandate**:
> - **WordPress & WooCommerce Core = 100% of Data**: All taxonomy terms, category titles, category thumbnail images, editorial descriptions, subcategories, product attributes, prices, gallery images, menu trees, and customizer options must be managed natively in `wp-admin`. Templates must NEVER hardcode mock text, static images, or preset category lists.
> - **Theme = 100% Pure UI, Layout & Interaction**: The theme's exclusive role is crafting high-fidelity layouts, 5-layer design token styling, fluid typography, responsive grids, micro-interactions, and accessible UI around native WordPress data objects.

### 6.1 Product Category & Taxonomy Architecture (`taxonomy-product_cat.php` / `archive-product.php`)

When a visitor navigates to a product category (e.g. `/product-category/tableware/ceramics/`), the theme dynamically extracts the category name, thumbnail image, description, and nested child terms directly from WordPress term meta:

```php
<?php
/**
 * Product Category & Taxonomy Archive Template
 * Location: taxonomy-product_cat.php or woocommerce/archive-product.php
 *
 * SOURCING: 100% WordPress / WooCommerce Term Data
 * STYLING:  100% Bespoke Theme UI & 5-Layer Design Tokens
 */

get_header('shop');

$current_term   = get_queried_object();
$term_id        = $current_term->term_id ?? 0;
$term_name      = single_term_title('', false);
$term_desc      = term_description();
$thumbnail_id   = get_term_meta($term_id, 'thumbnail_id', true);
$has_hero_image = !empty($thumbnail_id);

// Query immediate subcategories/child terms dynamically
$child_categories = get_terms([
    'taxonomy'   => 'product_cat',
    'parent'     => $term_id,
    'hide_empty' => false,
]);
?>

<main id="primary" class="site-main product-category-archive">

    <!-- 1. PURE UI: Bespoke Category Hero Banner -->
    <header class="category-hero <?php echo $has_hero_image ? 'has-bg-image' : 'has-solid-surface'; ?>">
        <?php if ($has_hero_image) : ?>
            <div class="category-hero-media">
                <?php echo wp_get_attachment_image($thumbnail_id, 'full', false, [
                    'class'   => 'category-hero-img',
                    'loading' => 'eager',
                    'alt'     => esc_attr($term_name),
                ]); ?>
                <div class="category-hero-overlay" aria-hidden="true"></div>
            </div>
        <?php endif; ?>

        <div class="container category-hero-content">
            <!-- Dynamic WordPress Breadcrumbs -->
            <div class="category-breadcrumbs">
                <?php woocommerce_breadcrumb([
                    'delimiter'   => '<span class="crumb-separator" aria-hidden="true">/</span>',
                    'wrap_before' => '<nav class="woocommerce-breadcrumb" aria-label="' . esc_attr__('Breadcrumb', 'beeclue') . '">',
                    'wrap_after'  => '</nav>',
                ]); ?>
            </div>

            <!-- Dynamic Category Name from WP Term -->
            <h1 class="category-title"><?php echo esc_html($term_name); ?></h1>

            <!-- Dynamic Category Description from WP Term (Supports rich text / Gutenberg) -->
            <?php if (!empty($term_desc)) : ?>
                <div class="category-description-card">
                    <div class="category-description-text">
                        <?php echo wp_kses_post($term_desc); ?>
                    </div>
                </div>
            <?php endif; ?>

            <!-- Dynamic Subcategories / Child Category Pills (If Any Exist) -->
            <?php if (!empty($child_categories) && !is_wp_error($child_categories)) : ?>
                <nav class="subcategory-pills" aria-label="<?php esc_attr_e('Subcategories', 'beeclue'); ?>">
                    <span class="subcategory-label"><?php esc_html_e('Explore Sub-Collections:', 'beeclue'); ?></span>
                    <ul class="subcategory-list">
                        <?php foreach ($child_categories as $child_cat) :
                            $child_link  = get_term_link($child_cat, 'product_cat');
                            $child_thumb = get_term_meta($child_cat->term_id, 'thumbnail_id', true);
                        ?>
                            <li class="subcategory-pill-item">
                                <a href="<?php echo esc_url($child_link); ?>" class="subcategory-pill-link">
                                    <?php if ($child_thumb) : ?>
                                        <?php echo wp_get_attachment_image($child_thumb, 'thumbnail', false, ['class' => 'subcategory-pill-thumb']); ?>
                                    <?php endif; ?>
                                    <span class="subcategory-pill-title"><?php echo esc_html($child_cat->name); ?></span>
                                    <span class="subcategory-pill-count">(<?php echo esc_html($child_cat->count); ?>)</span>
                                </a>
                            </li>
                        <?php endforeach; ?>
                    </ul>
                </nav>
            <?php endif; ?>
        </div>
    </header>

    <!-- 2. PURE UI: Catalog Filter & Sort Bar -->
    <div class="catalog-toolbar-wrapper">
        <div class="container catalog-toolbar">
            <div class="catalog-toolbar-count">
                <?php woocommerce_result_count(); ?>
            </div>
            <div class="catalog-toolbar-ordering">
                <?php woocommerce_catalog_ordering(); ?>
            </div>
        </div>
    </div>

    <!-- 3. Dynamic WooCommerce Product Loop -->
    <div class="container product-grid-container">
        <?php if (woocommerce_product_loop()) : ?>
            <?php woocommerce_product_loop_start(); ?>
                <?php while (have_posts()) : the_post(); ?>
                    <?php wc_get_template_part('content', 'product'); ?>
                <?php endwhile; ?>
            <?php woocommerce_product_loop_end(); ?>

            <!-- Dynamic Pagination -->
            <div class="catalog-pagination">
                <?php woocommerce_pagination(); ?>
            </div>
        <?php else : ?>
            <?php do_action('woocommerce_no_products_found'); ?>
        <?php endif; ?>
    </div>

</main>

<?php get_footer('shop'); ?>
```

### 6.2 Bespoke Category Hero & Subcategory CSS (`style.css`)
```css
/* ─────────────────────────────────────────────────────────────
   PRODUCT CATEGORY ARCHIVE: BESPOKE HERO & SUB-COLLECTION UI
   ───────────────────────────────────────────────────────────── */
.category-hero {
    position: relative;
    padding: clamp(3rem, 6vw, 6rem) 0;
    background: var(--color-surface-base);
    border-bottom: 1px solid var(--color-border-subtle);
    overflow: hidden;
}

.category-hero.has-bg-image {
    min-height: clamp(280px, 40vh, 480px);
    display: flex;
    align-items: center;
    color: var(--color-surface-base);
}

.category-hero-media {
    position: absolute;
    inset: 0;
    z-index: 0;
}

.category-hero-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
}

.category-hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        180deg,
        rgba(0, 0, 0, 0.25) 0%,
        rgba(0, 0, 0, 0.70) 100%
    );
}

.category-hero-content {
    position: relative;
    z-index: 1;
    max-width: 840px;
}

.category-title {
    font-family: var(--font-heading);
    font-size: clamp(2.25rem, 5vw, 3.75rem);
    font-weight: 400;
    line-height: 1.1;
    margin: 0.5rem 0 1rem 0;
    letter-spacing: -0.02em;
}

.category-description-card {
    margin-top: 1rem;
    font-size: clamp(0.938rem, 1.2vw, 1.063rem);
    line-height: 1.6;
    color: inherit;
    opacity: 0.9;
}

/* Dynamic Subcategory Pills */
.subcategory-pills {
    margin-top: 2rem;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.75rem;
}

.subcategory-label {
    font-size: 0.813rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
    opacity: 0.8;
}

.subcategory-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    list-style: none;
    padding: 0;
    margin: 0;
}

.subcategory-pill-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.35rem 0.85rem;
    border-radius: var(--radius-full, 9999px);
    border: 1px solid var(--color-border-subtle);
    background: var(--color-surface-base);
    color: var(--color-text-primary);
    text-decoration: none;
    font-size: 0.813rem;
    font-weight: 500;
    transition: all var(--motion-duration-fast) ease;
}

.subcategory-pill-link:hover {
    border-color: var(--color-action-primary);
    color: var(--color-action-primary);
    transform: translateY(-1px);
}

.subcategory-pill-thumb {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    object-fit: cover;
}

.subcategory-pill-count {
    opacity: 0.6;
    font-size: 0.75rem;
}
```

### 6.3 Single Product Data Binding (`content-single-product.php`)
Every element rendered on the single product page binds directly to WooCommerce object methods:
- **Title**: `$product->get_name()`
- **Pricing**: `$product->get_price_html()`
- **SKU**: `$product->get_sku()`
- **Stock Status**: `$product->get_stock_status()` and `$product->is_in_stock()`
- **Gallery Images**: `$product->get_gallery_image_ids()`
- **Short Description**: `$product->get_short_description()`
- **Product Tabs**: `woocommerce_default_product_tabs()` (Description, Additional Information, Reviews)
- **Upsells / Cross-sells**: `$product->get_upsell_ids()` and `$product->get_cross_sell_ids()`

The theme wraps these standard methods with responsive gallery sliders, zoom overlays, pill swatches, and the floating sticky Add-to-Cart bar.

---

## 7. Granular UI Component Toggles via Theme Settings (`inc/customizer.php`)

> [!IMPORTANT]
> **Complete UI Control for Store Owners**:
> Every visual UI component across catalog grids, product details, cart drawers, headers, and blog templates must have an independent toggle in **Appearance > Customize > Theme Settings**.
> **Example**: A store owner must be able to turn OFF reviews on the catalog product grid while keeping reviews fully visible on the single product details page. Templates must NEVER hardcode UI elements without wrapping them in `get_theme_mod()`.

### 7.1 Customizer Settings Registration (`inc/customizer.php`)
```php
<?php
/**
 * Theme Customizer: Granular UI Component Visibility Controls
 * Location: inc/customizer.php
 */

function beeclue_customize_register($wp_customize) {

    // ─────────────────────────────────────────────────────────────
    // PANEL: THEME SETTINGS & UI CONTROLS
    // ─────────────────────────────────────────────────────────────
    $wp_customize->add_panel('beeclue_theme_settings_panel', [
        'title'       => esc_html__('BeeClue Theme Settings', 'beeclue'),
        'description' => esc_html__('Enable or disable individual UI elements across all store templates.', 'beeclue'),
        'priority'    => 30,
    ]);

    // ─────────────────────────────────────────────────────────────
    // SECTION 1: PRODUCT CATALOG & GRID UI
    // ─────────────────────────────────────────────────────────────
    $wp_customize->add_section('beeclue_catalog_section', [
        'title' => esc_html__('Product Catalog & Grid', 'beeclue'),
        'panel' => 'beeclue_theme_settings_panel',
    ]);

    // Toggle: Reviews / Star Rating on Grid (Default: false for clean minimal grids)
    $wp_customize->add_setting('beeclue_catalog_show_rating', [
        'default'           => false,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
        'transport'         => 'refresh',
    ]);
    $wp_customize->add_control('beeclue_catalog_show_rating', [
        'label'       => esc_html__('Show Star Ratings on Product Grid', 'beeclue'),
        'description' => esc_html__('Toggle customer review stars on archive cards without affecting single product details.', 'beeclue'),
        'section'     => 'beeclue_catalog_section',
        'type'        => 'checkbox',
    ]);

    // Toggle: Secondary Hover Image
    $wp_customize->add_setting('beeclue_catalog_show_secondary_image', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_catalog_show_secondary_image', [
        'label'   => esc_html__('Show Secondary Image on Hover', 'beeclue'),
        'section' => 'beeclue_catalog_section',
        'type'    => 'checkbox',
    ]);

    // Toggle: Quick Add-to-Cart Button
    $wp_customize->add_setting('beeclue_catalog_show_quick_add', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_catalog_show_quick_add', [
        'label'   => esc_html__('Show Quick Add-to-Cart Button on Cards', 'beeclue'),
        'section' => 'beeclue_catalog_section',
        'type'    => 'checkbox',
    ]);

    // Toggle: Category Label above Product Title
    $wp_customize->add_setting('beeclue_catalog_show_category', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_catalog_show_category', [
        'label'   => esc_html__('Show Category Eyebrow above Title', 'beeclue'),
        'section' => 'beeclue_catalog_section',
        'type'    => 'checkbox',
    ]);

    // Toggle: Sale / Stock Badges on Cards
    $wp_customize->add_setting('beeclue_catalog_show_badges', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_catalog_show_badges', [
        'label'   => esc_html__('Show Sale & Stock Badges on Grid', 'beeclue'),
        'section' => 'beeclue_catalog_section',
        'type'    => 'checkbox',
    ]);

    // ─────────────────────────────────────────────────────────────
    // SECTION 2: SINGLE PRODUCT DETAILS UI
    // ─────────────────────────────────────────────────────────────
    $wp_customize->add_section('beeclue_single_product_section', [
        'title' => esc_html__('Single Product Details', 'beeclue'),
        'panel' => 'beeclue_theme_settings_panel',
    ]);

    // Toggle: Reviews on Single Product (Default: true)
    $wp_customize->add_setting('beeclue_single_show_reviews', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
        'transport'         => 'refresh',
    ]);
    $wp_customize->add_control('beeclue_single_show_reviews', [
        'label'       => esc_html__('Show Customer Reviews & Rating on Product Page', 'beeclue'),
        'description' => esc_html__('Display the full rating summary and review tab on product details.', 'beeclue'),
        'section'     => 'beeclue_single_product_section',
        'type'        => 'checkbox',
    ]);

    // Toggle: Floating Sticky Add-to-Cart Bar
    $wp_customize->add_setting('beeclue_single_show_sticky_bar', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_single_show_sticky_bar', [
        'label'   => esc_html__('Enable Floating Sticky Add-to-Cart Bar', 'beeclue'),
        'section' => 'beeclue_single_product_section',
        'type'    => 'checkbox',
    ]);

    // Toggle: SKU & Meta Details
    $wp_customize->add_setting('beeclue_single_show_sku', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_single_show_sku', [
        'label'   => esc_html__('Show SKU and Product Metadata', 'beeclue'),
        'section' => 'beeclue_single_product_section',
        'type'    => 'checkbox',
    ]);

    // Toggle: Related & Upsell Products
    $wp_customize->add_setting('beeclue_single_show_related', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_single_show_related', [
        'label'   => esc_html__('Show Related & Cross-Sell Products', 'beeclue'),
        'section' => 'beeclue_single_product_section',
        'type'    => 'checkbox',
    ]);

    // ─────────────────────────────────────────────────────────────
    // SECTION 3: CART DRAWER UI
    // ─────────────────────────────────────────────────────────────
    $wp_customize->add_section('beeclue_cart_section', [
        'title' => esc_html__('Cart Drawer', 'beeclue'),
        'panel' => 'beeclue_theme_settings_panel',
    ]);

    // Toggle: Free Shipping Progress Meter
    $wp_customize->add_setting('beeclue_cart_show_shipping_meter', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_cart_show_shipping_meter', [
        'label'   => esc_html__('Show Free Shipping Progress Bar', 'beeclue'),
        'section' => 'beeclue_cart_section',
        'type'    => 'checkbox',
    ]);

    // Toggle: In-Drawer Upsells / Cross-Sells
    $wp_customize->add_setting('beeclue_cart_show_cross_sells', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_cart_show_cross_sells', [
        'label'   => esc_html__('Show In-Drawer Recommended Add-ons', 'beeclue'),
        'section' => 'beeclue_cart_section',
        'type'    => 'checkbox',
    ]);

    // ─────────────────────────────────────────────────────────────
    // SECTION 4: HEADER & ANNOUNCEMENT BAR
    // ─────────────────────────────────────────────────────────────
    $wp_customize->add_section('beeclue_header_section', [
        'title' => esc_html__('Header & Announcement', 'beeclue'),
        'panel' => 'beeclue_theme_settings_panel',
    ]);

    // Toggle: Announcement Ticker Bar
    $wp_customize->add_setting('beeclue_header_show_announcement', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_header_show_announcement', [
        'label'   => esc_html__('Show Announcement Bar', 'beeclue'),
        'section' => 'beeclue_header_section',
        'type'    => 'checkbox',
    ]);

    // Toggle: Search Icon / Trigger in Header
    $wp_customize->add_setting('beeclue_header_show_search', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_header_show_search', [
        'label'   => esc_html__('Show Search Icon in Header', 'beeclue'),
        'section' => 'beeclue_header_section',
        'type'    => 'checkbox',
    ]);

    // ─────────────────────────────────────────────────────────────
    // SECTION 5: BLOG & EDITORIAL UI
    // ─────────────────────────────────────────────────────────────
    $wp_customize->add_section('beeclue_blog_section', [
        'title' => esc_html__('Blog & Editorial Journal', 'beeclue'),
        'panel' => 'beeclue_theme_settings_panel',
    ]);

    // Toggle: Post Author Bio Card
    $wp_customize->add_setting('beeclue_blog_show_author', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_blog_show_author', [
        'label'   => esc_html__('Show Author Bio Card on Single Articles', 'beeclue'),
        'section' => 'beeclue_blog_section',
        'type'    => 'checkbox',
    ]);

    // Toggle: Reading Time
    $wp_customize->add_setting('beeclue_blog_show_reading_time', [
        'default'           => true,
        'sanitize_callback' => 'beeclue_sanitize_checkbox',
    ]);
    $wp_customize->add_control('beeclue_blog_show_reading_time', [
        'label'   => esc_html__('Show Estimated Reading Time', 'beeclue'),
        'section' => 'beeclue_blog_section',
        'type'    => 'checkbox',
    ]);
}
add_action('customize_register', 'beeclue_customize_register');

/**
 * Sanitization helper for Customizer checkbox settings
 */
function beeclue_sanitize_checkbox($checked) {
    return (isset($checked) && true === (bool) $checked);
}
```

### 7.2 Template Implementation: Conditional UI Wrappers

#### Product Card on Grid (`woocommerce/content-product.php`):
Notice how reviews are wrapped in `beeclue_catalog_show_rating`:
```php
<li <?php wc_product_class('product-card', $product); ?>>
    <div class="product-card-media">
        <?php echo $product->get_image('woocommerce_thumbnail'); ?>

        <?php if (get_theme_mod('beeclue_catalog_show_badges', true) && $product->is_on_sale()) : ?>
            <span class="product-badge badge-sale"><?php esc_html_e('Sale', 'beeclue'); ?></span>
        <?php endif; ?>
    </div>

    <div class="product-card-body">
        <?php if (get_theme_mod('beeclue_catalog_show_category', true)) : ?>
            <span class="product-card-eyebrow"><?php echo esc_html(wc_get_product_category_list($product->get_id(), ', ')); ?></span>
        <?php endif; ?>

        <h3 class="product-card-title">
            <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
        </h3>

        <!-- Review stars only show if enabled in Theme Settings for catalog grid -->
        <?php if (get_theme_mod('beeclue_catalog_show_rating', false)) : ?>
            <div class="product-card-rating">
                <?php woocommerce_template_loop_rating(); ?>
            </div>
        <?php endif; ?>

        <div class="product-card-price">
            <?php woocommerce_template_loop_price(); ?>
        </div>

        <?php if (get_theme_mod('beeclue_catalog_show_quick_add', true)) : ?>
            <div class="product-card-actions">
                <?php woocommerce_template_loop_add_to_cart(); ?>
            </div>
        <?php endif; ?>
    </div>
</li>
```

#### Single Product Details (`woocommerce/single-product/rating.php` or `content-single-product.php`):
Reviews on details page are governed by their own independent setting:
```php
<?php
// On single product page: Independent setting allows reviews here even if disabled on grid
if (get_theme_mod('beeclue_single_show_reviews', true) && comments_open()) :
    woocommerce_template_single_rating();
endif;
?>

<?php if (get_theme_mod('beeclue_single_show_sticky_bar', true)) : ?>
    <?php get_template_part('template-parts/product/sticky-bar'); ?>
<?php endif; ?>
```




