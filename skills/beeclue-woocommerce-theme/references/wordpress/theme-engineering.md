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

### 4.4 Submenu Dropdown CSS & Accessible Interaction (`style.css`)
WordPress automatically appends `.menu-item-has-children` to parent items and wraps nested lists in `.sub-menu`:
```css
/* Top-level menu */
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

.nav-menu-primary a {
    color: var(--color-text-primary);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.938rem;
    transition: color var(--motion-duration-fast) ease;
}

/* Multi-level nested dropdowns */
.nav-menu-primary .sub-menu {
    position: absolute;
    top: 100%;
    left: 0;
    min-width: 220px;
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

/* Deep nested submenus (Level 2+) */
.nav-menu-primary .sub-menu .sub-menu {
    top: 0;
    left: 100%;
    margin: 0 0 0 0.25rem;
}

/* Accessible reveal on :hover AND :focus-within */
.nav-menu-primary li:hover > .sub-menu,
.nav-menu-primary li:focus-within > .sub-menu {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.nav-menu-primary .sub-menu li {
    position: relative;
    padding: 0;
}

.nav-menu-primary .sub-menu a {
    display: block;
    padding: 0.5rem 1.25rem;
    font-size: 0.875rem;
    color: var(--color-text-secondary);
}

.nav-menu-primary .sub-menu a:hover,
.nav-menu-primary .sub-menu a:focus {
    color: var(--color-action-primary);
    background: var(--color-surface-sunken);
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


