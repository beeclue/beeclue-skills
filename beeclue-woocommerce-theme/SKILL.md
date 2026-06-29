---
name: beeclue-woocommerce-theme
description: >
  Automates the creation of production-ready, high-performance WooCommerce WordPress themes.
  Generates custom designs with premium typography, animations, full SEO (JSON-LD, OG, meta),
  Unsplash imagery, AJAX cart (full-page + drawer modes), sticky headers, and Beeclue Tech
  agency branding. Targets 90+ Google PageSpeed and GTmetrix scores.
  Trigger on: "create woocommerce theme", "new wordpress theme", "build wordpress store",
  "beeclue theme", "woocommerce site", "new client site", "create store theme".
---

# Beeclue WooCommerce Theme Generator

You are an expert WordPress theme developer working for **Beeclue Tech**, a web design agency.
Your job is to generate complete, production-ready WooCommerce themes that are visually stunning,
SEO-optimized, and blazing fast. Every theme you create must feel like a $10,000+ custom build.

---

## TABLE OF CONTENTS

1. [Pre-Flight Checks](#1-pre-flight-checks)
2. [Discovery & Design System](#2-discovery--design-system)
3. [Theme Scaffolding](#3-theme-scaffolding)
4. [Core Theme Files](#4-core-theme-files)
5. [WooCommerce Integration](#5-woocommerce-integration)
6. [Page Templates & Content](#6-page-templates--content)
7. [SEO Implementation](#7-seo-implementation)
8. [Performance Optimization](#8-performance-optimization)
9. [Cart Modes (Full Page + Drawer)](#9-cart-modes)
10. [Verification Checklist](#10-verification-checklist)

---

## 1. PRE-FLIGHT CHECKS

Before starting ANY work, run these checks in order:

### 1.1 WP-CLI
```bash
# Check if wp-cli exists globally
which wp || wp --version
```
- If `wp` command exists globally → use it directly.
- If NOT found → install it globally ONE TIME:
```bash
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
chmod +x wp-cli.phar
sudo mv wp-cli.phar /usr/local/bin/wp
```
- On XAMPP environments, use: `/Applications/XAMPP/xamppfiles/bin/php /usr/local/bin/wp` or download `wp-cli.phar` into the project root and use `/Applications/XAMPP/xamppfiles/bin/php wp-cli.phar`.

### 1.2 WordPress Installation
```bash
# Check if WordPress is installed in the target directory
wp core is-installed --path=/path/to/site
```
- If WordPress is NOT installed:
  1. Download WordPress: `wp core download --path=/path/to/site`
  2. Check if a database exists. If not, create one:
     ```bash
     # For XAMPP (root, no password):
     /Applications/XAMPP/xamppfiles/bin/mysql -u root -e "CREATE DATABASE IF NOT EXISTS <db_name>;"
     ```
  3. Create `wp-config.php`:
     ```bash
     wp config create --dbname=<db_name> --dbuser=root --dbpass="" --dbhost=localhost --path=/path/to/site
     ```
  4. Run the install:
     ```bash
     wp core install --url="http://localhost/<site_folder>" --title="<Site Title>" --admin_user=admin --admin_password=<password> --admin_email=admin@example.com --path=/path/to/site
     ```
- If WordPress IS installed → proceed to theme creation.

### 1.3 WooCommerce
```bash
wp plugin is-installed woocommerce --path=/path/to/site
```
- If NOT installed:
  ```bash
  wp plugin install woocommerce --activate --path=/path/to/site
  wp plugin install wordpress-importer --activate --path=/path/to/site
  wp import wp-content/plugins/woocommerce/sample-data/sample_products.xml --authors=create --path=/path/to/site
  ```

### 1.4 Fluent Forms
```bash
wp plugin install fluentform --activate --path=/path/to/site
```

### 1.5 WordPress MCP
If a WordPress MCP adapter is available in the environment, use it to create/edit pages and manage content directly instead of manual dashboard work. Check for MCP servers named `wordpress`, `wp`, or similar. If available, prefer MCP tools over WP-CLI for content operations.

---

## 2. DISCOVERY & DESIGN SYSTEM

### 2.1 Prompt the User

Before generating any code, ASK the user the following (use the `ask_question` tool or ask directly):

**Required:**
- **Brand / Store Name**: What is the store called?
- **Industry / Niche**: What are they selling? (e.g., "luxury candles", "streetwear", "organic skincare")
- **Brand Tone**: Choose from: Minimal & Clean, Bold & Vibrant, Warm & Editorial, Dark & Luxury, Playful & Colorful
- **Color Preference**: Do you have specific brand colors, or should I choose based on the niche?

**Optional (use smart defaults if skipped):**
- Target audience
- Competitor sites for inspiration
- Specific features beyond standard

### 2.2 Generate Design Tokens

Based on user answers, generate a complete design token set. If the user says "use your own knowledge", select colors and fonts that are industry-appropriate and visually premium.

**Color Token Structure (REQUIRED — every theme must define these):**
```css
:root {
    /* Primary Palette */
    --color-bg:          /* Page background — light, warm, never pure white */
    --color-surface:     /* Cards, elevated surfaces */
    --color-ink:         /* Primary text — never pure black */
    --color-muted:       /* Secondary text, labels, metadata */
    --color-accent:      /* CTA buttons, links, highlights */
    --color-accent-hover:/* Darker shade of accent for hover states */
    --color-accent-light:/* Very light tint of accent for badges, backgrounds */
    --color-white:       #FFFFFF;

    /* Typography */
    --font-heading:      /* Display/heading font from Google Fonts — serif or display */
    --font-body:         /* Body font — clean sans-serif */

    /* Type Scale (use clamp for fluid sizing) */
    --text-hero:         clamp(48px, 8vw, 96px);
    --text-section:      clamp(28px, 5vw, 56px);
    --text-card-title:   20px;
    --text-body:         16px;
    --text-small:        14px;
    --text-eyebrow:      11px;

    /* Spacing (8px base unit) */
    --space-1: 8px;   --space-2: 16px;  --space-3: 24px;
    --space-4: 32px;  --space-6: 48px;  --space-8: 64px;
    --space-12: 96px; --space-16: 120px;

    /* Radii & Shadows */
    --radius-none: 0;
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-full: 9999px;
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
    --shadow-lg: 0 12px 24px rgba(0,0,0,0.12);
}
```

**Typography Pairing Guidelines (pick ONE pair):**
| Tone | Heading Font | Body Font |
|------|-------------|-----------|
| Minimal & Clean | `Outfit` or `Inter` | `Inter` or `DM Sans` |
| Bold & Vibrant | `Space Grotesk` or `Syne` | `DM Sans` or `Outfit` |
| Warm & Editorial | `Cormorant Garamond` or `Playfair Display` | `DM Sans` or `Source Sans 3` |
| Dark & Luxury | `Cormorant Garamond` or `Italiana` | `Montserrat` or `Outfit` |
| Playful & Colorful | `Fredoka` or `Quicksand` | `Nunito` or `DM Sans` |

---

## 3. THEME SCAFFOLDING

### 3.1 Generate Theme Name
Generate a random word for the theme name. Use simple, memorable words:
`beeclue-{randomword}-theme` (e.g., `beeclue-nova-theme`, `beeclue-ember-theme`, `beeclue-drift-theme`)

### 3.2 Create Directory Structure
```
wp-content/themes/beeclue-{name}-theme/
├── style.css                  # Theme header + design tokens + base styles
├── functions.php              # Theme setup, enqueues, customizer, WooCommerce support
├── header.php                 # Sticky nav with logo, menu, search, cart icons
├── footer.php                 # Email signup + 4-col footer + Beeclue branding
├── index.php                  # Fallback template
├── page.php                   # Default page template
├── single.php                 # Single post template
├── search.php                 # Search results template
├── 404.php                    # Custom 404 page
├── template-home.php          # Homepage (Template Name: Homepage)
├── template-about.php         # About Us (Template Name: About Us)
├── template-contact.php       # Contact (Template Name: Contact)
├── template-faq.php           # FAQ (Template Name: FAQ)
├── woocommerce.css            # WooCommerce style overrides
├── woocommerce/               # WooCommerce template overrides (if needed)
│   └── cart/
│       └── mini-cart.php      # AJAX sidebar drawer cart
├── assets/
│   ├── css/
│   │   └── critical.css       # Above-the-fold critical CSS (inlined)
│   ├── js/
│   │   ├── main.js            # Core interactions (nav scroll, marquee)
│   │   ├── cart-drawer.js     # AJAX cart drawer logic
│   │   └── animations.js     # Scroll-triggered CSS animations (IntersectionObserver)
│   └── images/
│       └── (generated assets)
└── inc/
    ├── seo.php                # JSON-LD, OG tags, meta tags
    ├── customizer.php         # Theme Customizer options (cart mode toggle, socials)
    └── performance.php        # Preload, lazy-load, defer, async optimizations
```

---

## 4. CORE THEME FILES

### 4.1 `style.css`
Must contain:
- WordPress theme header comment block
- ALL design tokens as CSS custom properties
- Google Fonts `@import` (use `<link>` in `functions.php` for performance — the `@import` here is fallback only)
- Base reset/normalize styles
- Typography system
- Component classes: `.btn`, `.btn-primary`, `.btn-secondary`, `.eyebrow`, `.container`, `.section-padding`
- Animation utility classes (`.fade-up`, `.fade-in`, `.slide-left`, etc.)
- Responsive breakpoints: `768px` (mobile), `1024px` (tablet), `1440px` (max-width)

### 4.2 `functions.php`
Must include:
```php
<?php
// Theme Setup
add_action('after_setup_theme', function() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('custom-logo');
    add_theme_support('html5', ['search-form','comment-form','comment-list','gallery','caption','style','script']);
    add_theme_support('woocommerce');
    add_theme_support('wc-product-gallery-zoom');
    add_theme_support('wc-product-gallery-lightbox');
    add_theme_support('wc-product-gallery-slider');
    register_nav_menus(['primary' => 'Primary Menu', 'footer' => 'Footer Menu']);
});

// Enqueue Styles & Scripts (with performance in mind)
add_action('wp_enqueue_scripts', function() {
    // Google Fonts — preconnect + single request
    wp_enqueue_style('theme-fonts', 'https://fonts.googleapis.com/css2?family=...&display=swap', [], null);

    // Main stylesheet
    wp_enqueue_style('theme-style', get_stylesheet_uri(), [], '1.0.0');

    // WooCommerce overrides
    if (class_exists('WooCommerce')) {
        wp_enqueue_style('theme-woo', get_template_directory_uri() . '/woocommerce.css', ['theme-style'], '1.0.0');
    }

    // JS — loaded in footer, deferred
    wp_enqueue_script('theme-main', get_template_directory_uri() . '/assets/js/main.js', [], '1.0.0', true);
    wp_enqueue_script('theme-animations', get_template_directory_uri() . '/assets/js/animations.js', [], '1.0.0', true);

    if (class_exists('WooCommerce')) {
        wp_enqueue_script('theme-cart', get_template_directory_uri() . '/assets/js/cart-drawer.js', ['jquery'], '1.0.0', true);
        wp_localize_script('theme-cart', 'themeCart', [
            'ajaxUrl' => admin_url('admin-ajax.php'),
            'nonce'   => wp_create_nonce('theme-cart-nonce'),
        ]);
    }
});

// Include modular files
require_once get_template_directory() . '/inc/seo.php';
require_once get_template_directory() . '/inc/customizer.php';
require_once get_template_directory() . '/inc/performance.php';

// AJAX Cart Handlers (for drawer mode)
// ... (see Section 9)
```

### 4.3 `header.php` — Sticky Header (REQUIRED PATTERN)
Every header MUST include:
- `<!DOCTYPE html>` with `language_attributes()`
- Preconnect hints for Google Fonts and Unsplash
- `wp_head()` hook
- Skip-to-content link for accessibility
- Sticky `<header>` element with:
  - **Left**: Site logo (custom logo or site title in heading font)
  - **Center**: `wp_nav_menu()` primary navigation
  - **Right**: Search icon (SVG) + Cart icon (SVG with live AJAX count badge) + "Shop Now" CTA button
- Opening `<main>` tag
- JavaScript for sticky shadow on scroll (in `main.js`)

```html
<!-- Cart icon with AJAX count -->
<a href="<?php echo wc_get_cart_url(); ?>" class="cart-icon" id="cart-toggle">
    <svg>...</svg>
    <span class="cart-count"><?php echo WC()->cart->get_cart_contents_count(); ?></span>
</a>
```

### 4.4 `footer.php` — MANDATORY BRANDING
Every footer MUST contain this exact line (non-negotiable):
```html
<span>Website Designed &amp; Developed by
    <a href="https://beeclue.com/?utm_source=client_site&utm_medium=footer&utm_campaign=web_design"
       target="_blank" rel="noopener noreferrer">Beeclue Tech</a>
</span>
```

Footer structure:
1. Email signup section (full-width, dark background)
2. 4-column grid: Brand info + Social icons | Shop links | Help links | Newsletter compact
3. Bottom bar with copyright + Beeclue branding (above) + legal links
4. `wp_footer()` hook

---

## 5. WOOCOMMERCE INTEGRATION

### 5.1 Style Overrides (`woocommerce.css`)
Override ALL default WooCommerce styles to match the theme's design system:
- Product grids: custom card layout with hover effects
- Single product: editorial layout with large images
- Buttons: match theme's `.btn-primary` styling
- Forms: match theme's input styling
- Cart table: clean, minimal design
- Checkout: streamlined, single-column on mobile
- Notices: styled with theme accent color

### 5.2 WooCommerce Template Overrides
Only override templates when absolutely necessary. Prefer CSS overrides and `woocommerce_*` action/filter hooks.

### 5.3 Product Display
- Product cards must have: image with hover zoom, category eyebrow, product title, short description (1 line), price, star rating
- "Quick Add" button revealed on hover
- Use `wc_get_template_part()` for consistency

---

## 6. PAGE TEMPLATES & CONTENT

### 6.1 Required Pages (create ALL of these via WP-CLI)
After theme activation, create these pages and assign templates:

```bash
# Create pages
wp post create --post_type=page --post_title="Home" --post_status=publish --page_template=template-home.php
wp post create --post_type=page --post_title="About Us" --post_status=publish --page_template=template-about.php
wp post create --post_type=page --post_title="Contact" --post_status=publish --page_template=template-contact.php
wp post create --post_type=page --post_title="FAQ" --post_status=publish --page_template=template-faq.php
wp post create --post_type=page --post_title="Privacy Policy" --post_status=publish
wp post create --post_type=page --post_title="Terms of Service" --post_status=publish

# Set homepage
wp option update show_on_front page
wp option update page_on_front $(wp post list --post_type=page --title="Home" --field=ID)
```

### 6.2 Homepage Template (`template-home.php`)
Must include these sections (in order):
1. **Hero Section** — Full-viewport, editorial headline with Unsplash background image, CTA buttons, subtle CSS animations (fade-up stagger)
2. **Trust Marquee** — Infinite CSS scroll: "Free Shipping" · "Sustainably Sourced" · "30-Day Returns" etc.
3. **Featured Products** — Dynamic WP_Query pulling 4-8 latest products from WooCommerce
4. **Editorial Split** — Image + text side-by-side brand story section
5. **Shop by Category** — Grid of product category cards with overlay text
6. **Testimonials** — 3-column review cards
7. **Newsletter CTA** — Full-width dark section with email signup (use Fluent Forms shortcode if available)

**Unsplash Images:** Use `https://source.unsplash.com/800x600/?{keyword}` format with niche-relevant keywords. Examples:
```
https://source.unsplash.com/1200x800/?{niche},lifestyle
https://source.unsplash.com/800x800/?{niche},product
https://source.unsplash.com/600x800/?{niche},detail
```

### 6.3 About Page (`template-about.php`)
- Hero with brand statement
- Team / founder section
- Brand values grid
- Timeline or milestones
- CTA to shop

### 6.4 Contact Page (`template-contact.php`)
- Contact info (address, email, phone)
- Embed Fluent Forms contact form via shortcode: `[fluentform id="1"]`
- Google Maps embed placeholder
- Social media links

### 6.5 FAQ Page (`template-faq.php`)
- Accordion-style FAQ using `<details>` / `<summary>` (native HTML, no JS needed)
- Structured data (FAQPage schema) — see SEO section

---

## 7. SEO IMPLEMENTATION (CRITICAL PRIORITY)

SEO is the #1 priority. Every page must be fully optimized.

### 7.1 Create `inc/seo.php`
This file hooks into `wp_head` and outputs:

#### Meta Tags
```php
add_action('wp_head', function() {
    // Charset & viewport (already in header.php but ensure)
    echo '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">' . "\n";

    // Canonical URL
    echo '<link rel="canonical" href="' . esc_url(get_permalink()) . '">' . "\n";

    // Dynamic meta description
    if (is_singular()) {
        $desc = get_the_excerpt() ?: wp_trim_words(get_the_content(), 30);
    } elseif (is_shop()) {
        $desc = 'Shop our curated collection of premium products. Free shipping available.';
    } else {
        $desc = get_bloginfo('description');
    }
    echo '<meta name="description" content="' . esc_attr($desc) . '">' . "\n";
});
```

#### Open Graph Tags
```php
add_action('wp_head', function() {
    echo '<meta property="og:type" content="' . (is_singular('product') ? 'product' : 'website') . '">' . "\n";
    echo '<meta property="og:title" content="' . esc_attr(wp_get_document_title()) . '">' . "\n";
    echo '<meta property="og:description" content="' . esc_attr($desc) . '">' . "\n";
    echo '<meta property="og:url" content="' . esc_url(get_permalink()) . '">' . "\n";
    echo '<meta property="og:site_name" content="' . esc_attr(get_bloginfo('name')) . '">' . "\n";

    // OG Image
    if (has_post_thumbnail()) {
        echo '<meta property="og:image" content="' . esc_url(get_the_post_thumbnail_url(null, 'large')) . '">' . "\n";
    }

    // Twitter Card
    echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
});
```

#### JSON-LD Structured Data (REQUIRED for every page type)
```php
add_action('wp_head', function() {
    $schema = [];

    // Organization (every page)
    $org = [
        '@type' => 'Organization',
        'name' => get_bloginfo('name'),
        'url' => home_url('/'),
        'logo' => esc_url(wp_get_attachment_url(get_theme_mod('custom_logo'))),
    ];

    // WebSite with SearchAction
    $schema[] = [
        '@context' => 'https://schema.org',
        '@type' => 'WebSite',
        'name' => get_bloginfo('name'),
        'url' => home_url('/'),
        'publisher' => $org,
        'potentialAction' => [
            '@type' => 'SearchAction',
            'target' => home_url('/?s={search_term_string}'),
            'query-input' => 'required name=search_term_string',
        ],
    ];

    // Product schema (single product pages)
    if (is_singular('product')) {
        global $product;
        $schema[] = [
            '@context' => 'https://schema.org',
            '@type' => 'Product',
            'name' => $product->get_name(),
            'description' => wp_strip_all_tags($product->get_short_description()),
            'image' => wp_get_attachment_url($product->get_image_id()),
            'sku' => $product->get_sku(),
            'offers' => [
                '@type' => 'Offer',
                'url' => get_permalink(),
                'priceCurrency' => get_woocommerce_currency(),
                'price' => $product->get_price(),
                'availability' => $product->is_in_stock()
                    ? 'https://schema.org/InStock'
                    : 'https://schema.org/OutOfStock',
            ],
            'aggregateRating' => $product->get_review_count() > 0 ? [
                '@type' => 'AggregateRating',
                'ratingValue' => $product->get_average_rating(),
                'reviewCount' => $product->get_review_count(),
            ] : null,
        ];
    }

    // BreadcrumbList
    if (!is_front_page()) {
        $breadcrumbs = [
            ['@type' => 'ListItem', 'position' => 1, 'name' => 'Home', 'item' => home_url('/')],
        ];
        if (is_singular()) {
            $breadcrumbs[] = ['@type' => 'ListItem', 'position' => 2, 'name' => get_the_title(), 'item' => get_permalink()];
        }
        $schema[] = [
            '@context' => 'https://schema.org',
            '@type' => 'BreadcrumbList',
            'itemListElement' => $breadcrumbs,
        ];
    }

    // FAQPage schema (for FAQ template)
    if (is_page_template('template-faq.php')) {
        // Generate from page content or hardcoded FAQ items
        // Structure: @type FAQPage with mainEntity array of Question items
    }

    // Output
    foreach ($schema as $s) {
        $s = array_filter($s); // Remove nulls
        echo '<script type="application/ld+json">' . wp_json_encode($s, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . '</script>' . "\n";
    }
});
```

### 7.2 Additional SEO Requirements
- Every page template must have exactly ONE `<h1>` tag
- Use semantic HTML: `<header>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<nav>`
- All images must have descriptive `alt` attributes
- Internal linking between pages
- Breadcrumb navigation on all non-homepage pages
- XML sitemap (WooCommerce provides this, ensure it's active)

---

## 8. PERFORMANCE OPTIMIZATION (CRITICAL — targets 90+ PageSpeed)

### 8.1 Create `inc/performance.php`

```php
<?php
// Preconnect to external origins
add_action('wp_head', function() {
    echo '<link rel="preconnect" href="https://fonts.googleapis.com">' . "\n";
    echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
}, 1);

// Preload critical font files (get URLs from Google Fonts CSS)
add_action('wp_head', function() {
    echo '<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=...">' . "\n";
}, 2);

// Remove unnecessary WordPress head bloat
remove_action('wp_head', 'rsd_link');
remove_action('wp_head', 'wlwmanifest_link');
remove_action('wp_head', 'wp_shortlink_wp_head');
remove_action('wp_head', 'wp_generator');
remove_action('wp_head', 'rest_output_link_wp_head');
remove_action('wp_head', 'wp_oembed_add_discovery_links');
remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');

// Defer non-critical JS
add_filter('script_loader_tag', function($tag, $handle) {
    $defer_handles = ['theme-main', 'theme-animations', 'theme-cart'];
    if (in_array($handle, $defer_handles)) {
        return str_replace(' src', ' defer src', $tag);
    }
    return $tag;
}, 10, 2);

// Add native lazy loading to images
add_filter('wp_get_attachment_image_attributes', function($attr) {
    $attr['loading'] = 'lazy';
    $attr['decoding'] = 'async';
    return $attr;
});

// Disable WooCommerce styles on non-WooCommerce pages
add_action('wp_enqueue_scripts', function() {
    if (function_exists('is_woocommerce') && !is_woocommerce() && !is_cart() && !is_checkout() && !is_account_page()) {
        wp_dequeue_style('woocommerce-general');
        wp_dequeue_style('woocommerce-layout');
        wp_dequeue_style('woocommerce-smallscreen');
    }
}, 99);

// Disable jQuery Migrate
add_action('wp_default_scripts', function($scripts) {
    if (!is_admin() && isset($scripts->registered['jquery'])) {
        $script = $scripts->registered['jquery'];
        if ($script->deps) {
            $script->deps = array_diff($script->deps, ['jquery-migrate']);
        }
    }
});
```

### 8.2 Critical CSS
- Extract above-the-fold CSS into `assets/css/critical.css`
- Inline it in `header.php` inside a `<style>` tag
- Load the full stylesheet with `media="print" onload="this.media='all'"`

### 8.3 Image Optimization
- Use `srcset` and `sizes` attributes on all images
- Use WebP format where possible
- Unsplash images: append `&w=800&q=80&fm=webp` for optimized delivery
- Set explicit `width` and `height` on images to prevent CLS

### 8.4 Animation Strategy (NO HEAVY JS LIBRARIES)
**DO NOT use GSAP, ScrollReveal, AOS, or similar libraries for production themes.**
Instead, use a lightweight IntersectionObserver pattern in `animations.js`:

```javascript
// animations.js — lightweight scroll reveal (~20 lines, zero dependencies)
document.addEventListener('DOMContentLoaded', () => {
    const reveals = document.querySelectorAll('.reveal');
    if (!reveals.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    reveals.forEach(el => observer.observe(el));
});
```

Corresponding CSS (in `style.css`):
```css
.reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s cubic-bezier(0.2, 0.8, 0.2, 1),
                transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.reveal.revealed {
    opacity: 1;
    transform: translateY(0);
}
.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }
.reveal-delay-3 { transition-delay: 0.3s; }
```

For CSS-only animations (hero, marquee), use `@keyframes` — no JS needed.

---

## 9. CART MODES

Both modes must ALWAYS be built. The active mode is controlled via the WordPress Customizer.

### 9.1 Customizer Option (`inc/customizer.php`)
```php
add_action('customize_register', function($wp_customize) {
    $wp_customize->add_section('theme_cart_settings', [
        'title' => 'Cart Settings',
        'priority' => 30,
    ]);

    $wp_customize->add_setting('cart_display_mode', [
        'default' => 'drawer',
        'sanitize_callback' => 'sanitize_text_field',
    ]);

    $wp_customize->add_control('cart_display_mode', [
        'label' => 'Cart Display Mode',
        'section' => 'theme_cart_settings',
        'type' => 'select',
        'choices' => [
            'drawer' => 'Sidebar Drawer (AJAX)',
            'full_page' => 'Full Page Cart',
        ],
    ]);

    // Social Media URLs
    $socials = ['instagram', 'facebook', 'twitter', 'pinterest', 'tiktok'];
    $wp_customize->add_section('theme_socials', ['title' => 'Social Media', 'priority' => 35]);
    foreach ($socials as $social) {
        $wp_customize->add_setting("social_{$social}", ['default' => '', 'sanitize_callback' => 'esc_url_raw']);
        $wp_customize->add_control("social_{$social}", [
            'label' => ucfirst($social) . ' URL',
            'section' => 'theme_socials',
            'type' => 'url',
        ]);
    }
});
```

### 9.2 Drawer Cart (`cart-drawer.js`)
- Slides in from the right side of the screen
- Triggered by clicking the cart icon in the header
- Shows product list, quantities (editable), subtotal, checkout button
- Updates via AJAX (WordPress admin-ajax.php or WC REST API)
- Close button + click-outside-to-close
- Smooth CSS transition (transform: translateX)
- Body scroll lock when open

### 9.3 Full Page Cart
- Standard WooCommerce cart page at `/cart/`
- Styled to match the theme's design tokens
- Enhanced with quantity +/- buttons
- Cross-sell products displayed below

### 9.4 Cart Toggle Logic
In `header.php`, check the customizer setting:
```php
<?php $cart_mode = get_theme_mod('cart_display_mode', 'drawer'); ?>
<?php if ($cart_mode === 'drawer') : ?>
    <!-- Include drawer HTML + cart-drawer.js -->
<?php endif; ?>
```
The cart icon links to:
- **Drawer mode**: `#` (JavaScript opens drawer)
- **Full page mode**: `<?php echo wc_get_cart_url(); ?>`

---

## 10. VERIFICATION CHECKLIST

After generating the theme, verify ALL of the following:

### Functional
- [ ] Theme activates without errors
- [ ] Homepage displays all sections
- [ ] WooCommerce shop page works
- [ ] Single product page works
- [ ] Cart (both modes) works
- [ ] Checkout page works
- [ ] All page templates render correctly
- [ ] Navigation menu works
- [ ] Search functionality works
- [ ] Mobile responsive (test at 375px, 768px, 1024px)

### SEO
- [ ] Every page has unique `<title>` tag
- [ ] Every page has `<meta name="description">`
- [ ] OG tags present on all pages
- [ ] JSON-LD schema on homepage (WebSite + Organization)
- [ ] JSON-LD schema on product pages (Product)
- [ ] JSON-LD schema on FAQ page (FAQPage)
- [ ] Breadcrumbs on all non-homepage pages
- [ ] Canonical URLs set
- [ ] Semantic HTML throughout
- [ ] Single `<h1>` per page
- [ ] All images have `alt` attributes

### Performance
- [ ] No render-blocking JS
- [ ] Google Fonts loaded with `display=swap`
- [ ] Images lazy-loaded
- [ ] No GSAP/AOS/heavy animation libraries
- [ ] WordPress head bloat removed
- [ ] jQuery Migrate disabled
- [ ] WooCommerce CSS disabled on non-WC pages

### Branding
- [ ] Beeclue Tech footer link with UTM tags present on every page
- [ ] UTM format: `?utm_source=client_site&utm_medium=footer&utm_campaign=web_design`

---

## EXECUTION ORDER

When creating a new theme, follow this exact sequence:

1. **Ask** the user for brand details (Section 2.1)
2. **Pre-flight** — check WP-CLI, WordPress, WooCommerce (Section 1)
3. **Generate** design tokens based on user input (Section 2.2)
4. **Scaffold** theme directory and ALL files (Section 3)
5. **Build** core files: style.css → functions.php → header.php → footer.php (Section 4)
6. **Build** page templates: home → about → contact → faq (Section 6)
7. **Build** SEO module: inc/seo.php (Section 7)
8. **Build** performance module: inc/performance.php (Section 8)
9. **Build** cart system: customizer + drawer + full page (Section 9)
10. **Build** WooCommerce overrides: woocommerce.css (Section 5)
11. **Activate** theme via WP-CLI
12. **Create** pages and assign templates via WP-CLI (Section 6.1)
13. **Set** homepage to static page via WP-CLI
14. **Import** WooCommerce sample products
15. **Verify** with checklist (Section 10)
