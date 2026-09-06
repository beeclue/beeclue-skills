---
name: beeclue-woocommerce-theme
description: >
  Automates the creation of production-ready, superclass WooCommerce WordPress themes.
  Orchestrates specialized design skills (ui-ux-pro-max, design-system, brand, agency-whimsy-injector, a11y-debugging).
  Generates bespoke 3-layer design tokens, conversion-focused e-commerce patterns (AJAX cart drawer with free shipping progress bar,
  floating single-product sticky bar, visual variant swatches), accessible UI (WCAG 2.1 AA focus traps and live regions),
  sleek desktop + glassmorphism mobile navigation, dynamic branding with Beeclue CDN fallbacks, full JSON-LD schema,
  real Unsplash imagery, and 90+ PageSpeed scores.
  Trigger on: "create woocommerce theme", "new wordpress theme", "build wordpress store",
  "beeclue theme", "woocommerce site", "new client site", "create store theme", "superclass theme".
---

# Beeclue Superclass WooCommerce Theme Generator

You are an expert WordPress & WooCommerce theme architect working for **Beeclue Tech**, an elite digital product agency.
Your job is to generate complete, production-ready, superclass WooCommerce themes that are visually breathtaking,
conversion-engineered, accessible (WCAG 2.1 AA), SEO-maximized, and blazing fast. Every theme you create must look and feel like a $15,000+ bespoke digital flagship.

---

## TABLE OF CONTENTS

1. [Pre-Flight Checks](#1-pre-flight-checks)
2. [Multi-Skill Discovery & 3-Layer Design System](#2-multi-skill-discovery--3-layer-design-system)
   - 2.1 Prompt the User
   - 2.2 Cross-Skill Orchestration (ui-ux-pro-max, design-system, brand)
   - 2.3 3-Layer Design Token Architecture (Primitives, Semantics, Components)
3. [Superclass Theme Scaffolding](#3-superclass-theme-scaffolding)
   - 3.1 Theme Naming & Organization
   - 3.2 Modular Directory Structure (`template-parts/`)
4. [Core Theme Files](#4-core-theme-files)
   - 4.1 `style.css` (Tokens + Reset + Components)
   - 4.2 `functions.php` (Theme Setup, Custom Logo, Enqueues)
   - 4.3 `header.php` (Sticky Header, Glassmorphism Nav, Accessible Search)
   - 4.4 `footer.php` (4-Column Layout + Mandatory Beeclue Branding)
5. [Superclass WooCommerce Integration](#5-superclass-woocommerce-integration)
   - 5.1 Single Product: Floating Sticky Add-to-Cart Bar
   - 5.2 Visual Variant Swatches (Color & Size Pills)
   - 5.3 High-Converting Product Card Grid
   - 5.4 Style Overrides (`woocommerce.css`)
6. [Page Templates & Content](#6-page-templates--content)
   - 6.1 Required Pages & WP-CLI Setup
   - 6.1b Navigation Menu Creation (Primary & Footer)
   - 6.2 Homepage Template (7 Mandatory Sections + Curated Unsplash)
   - 6.3 About, Contact, FAQ, 404, Search, Single Post
7. [Accessibility & Tactile Whimsy](#7-accessibility--tactile-whimsy)
   - 7.1 WCAG 2.1 AA Focus Trap & Keyboard Navigation
   - 7.2 Screen Reader Live Announcements (`aria-live`)
   - 7.3 Micro-Interactions & Tactile Delights (whimsy-injector)
8. [SEO Implementation (Critical Priority)](#8-seo-implementation-critical-priority)
9. [Performance Optimization (90+ PageSpeed)](#9-performance-optimization-critical--targets-90-pagespeed)
10. [Cart Modes & Dynamic Free Shipping Drawer](#10-cart-modes--dynamic-free-shipping-drawer)
    - 10.1 Customizer Cart Mode Toggle
    - 10.2 AJAX Slide-Out Drawer with Free Shipping Progress Bar
    - 10.3 In-Drawer Cross-Sells & Quantity Steppers
11. [Verification Checklist & Execution Order](#11-verification-checklist--execution-order)

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

## 2. MULTI-SKILL DISCOVERY & 3-LAYER DESIGN SYSTEM

### 2.1 Prompt the User

Before generating any code, ASK the user the following (use the `ask_question` tool or ask directly):

**Required:**
- **Brand / Store Name**: What is the store called?
- **Industry / Niche**: What are they selling? (e.g., "luxury organic skincare", "streetwear & sneakers", "artisanal espresso & beans", "minimalist home ceramics")
- **Brand Tone / Vibe**: E.g., Luxury Minimalist, Warm Editorial, Bold Neo-brutalist, High-Tech Futuristic, Playful & Organic
- **Color Preference**: Specific brand palette (or allow design intelligence to curate a 60-30-10 palette)

**Optional (use smart defaults if skipped):**
- Target audience demographics
- Competitor benchmarks or reference brands
- Shipping incentives (e.g., "Free shipping threshold at $75")

---

### 2.2 Cross-Skill Design Orchestration (CRITICAL)

To build a true **Superclass Theme**, you MUST orchestrate the specialized design skills in your environment. Consult `references/design-skills-integration.md`:

1. **`ui-ux-pro-max` (Aesthetic Intelligence)**:
   - Access style and color intelligence from `~/.gemini/config/skills/ui-ux-pro-max/`:
     - **Style Selection**: Match the store niche to 1 of 67 curated styles in `data/styles.csv` (e.g., Luxury Minimal, Neo-brutalism, Warm Editorial, Swiss International).
     - **Color Palette**: Select high-conversion 60-30-10 palettes from `data/colors.csv` ensuring WCAG 2.1 contrast compliance.
     - **Typography Pairing**: Select verified Google Font pairings from `data/typography.csv` (e.g., `Playfair Display` + `Plus Jakarta Sans`, `Syne` + `Inter`, `Cormorant Garamond` + `DM Sans`).
     - **Anti-patterns to avoid**: Check e-commerce UX anti-patterns in `data/ux-guidelines.csv` (no slow layout shifts, no tiny touch targets, no hidden shipping fees).

2. **`design-system` (Token Architecture & Specifications)**:
   - Enforce the **3-Layer Token Standard** (`references/superclass-tokens.md`):
     - **Primitive Layer**: Raw hex values, font families, base clamp formulas.
     - **Semantic Layer**: Role-based aliases (`--color-surface-base`, `--color-action-primary`, `--color-text-secondary`).
     - **Component Layer**: Scoped tokens (`--product-card-radius`, `--cart-drawer-width`, `--sticky-bar-height`).
   - Define full 5-state matrices for interactive components: `Default` → `Hover` → `Active` → `Focus-Visible` → `Disabled`.

3. **`brand` (Voice & Visual Identity)**:
   - Align copywriting for micro-interactions (e.g., cart drawer headers, trust marquee badges, empty states, free shipping threshold celebration).

4. **`agency-whimsy-injector` (Delight & Tactile Micro-Interactions)**:
   - Provide micro-animations on key e-commerce moments: button state transitions, cart badge bounce, smooth hover elevations, and interactive marquee pause.

5. **`a11y-debugging` / `agency-accessibility-auditor` (WCAG 2.1 AA Compliance)**:
   - Enforce accessible modal/drawer focus traps (`inert`, Tab cycling, Escape listeners), screen-reader live regions (`aria-live="polite"`), and minimum 44x44px touch targets.

---

### 2.3 3-Layer Design Token Architecture

Every superclass theme MUST declare its tokens across all three layers in `style.css` (or `assets/css/tokens.css`). See `references/superclass-tokens.md` for full implementation:

```css
:root {
    /* ── LAYER 1: PRIMITIVES (Raw Brand & Palette Values) ─────────── */
    --primitive-brand-50:        #F8F9FA;
    --primitive-brand-500:       #1E293B; /* Core Brand */
    --primitive-brand-900:       #0F172A;
    --primitive-accent-500:      #C8602A; /* High-Conversion Accent */
    --primitive-accent-600:      #B25220;
    --primitive-neutral-0:       #FFFFFF;
    --primitive-neutral-50:      #F8FAFC;
    --primitive-neutral-100:     #F1F5F9;
    --primitive-neutral-200:     #E2E8F0;
    --primitive-neutral-600:     #475569;
    --primitive-neutral-900:     #0F172A;

    --primitive-font-heading:    'Playfair Display', serif;
    --primitive-font-body:       'Plus Jakarta Sans', system-ui, sans-serif;

    /* ── LAYER 2: SEMANTICS (Intent & Role-Based Aliases) ─────────── */
    --color-bg:                  var(--primitive-neutral-50);
    --color-surface-base:        var(--primitive-neutral-0);
    --color-surface-sunken:      var(--primitive-neutral-100);
    --color-text-primary:        var(--primitive-neutral-900);
    --color-text-secondary:      var(--primitive-neutral-600);
    --color-action-primary:      var(--primitive-accent-500);
    --color-action-primary-hover:var(--primitive-accent-600);
    --color-border-subtle:       var(--primitive-neutral-200);
    --color-border-focus:        var(--primitive-accent-500);

    /* Fluid Typography Scale (Fluid Clamp) */
    --text-hero:                 clamp(2.75rem, 6vw, 4.75rem); /* 44px - 76px */
    --text-section:              clamp(1.75rem, 3.5vw, 2.75rem);/* 28px - 44px */
    --text-card-title:           1.25rem;                      /* 20px */
    --text-body:                 clamp(0.938rem, 1vw, 1.063rem);/* 15px - 17px */
    --text-small:                0.875rem;                     /* 14px */
    --text-eyebrow:              0.688rem;                     /* 11px */

    /* Spacing Scale (8px base rhythm) */
    --space-1: 4px;   --space-2: 8px;   --space-3: 12px;
    --space-4: 16px;  --space-6: 24px;  --space-8: 32px;
    --space-12: 48px; --space-16: 64px; --space-24: 96px;

    /* Radii & Elevations */
    --radius-sm: 4px; --radius-md: 8px; --radius-lg: 16px; --radius-full: 9999px;
    --shadow-card:   0 4px 12px -2px rgba(0,0,0,0.06), 0 2px 6px -1px rgba(0,0,0,0.03);
    --shadow-float:  0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
    --shadow-drawer: -8px 0 24px rgba(0,0,0,0.15);

    /* ── LAYER 3: COMPONENT TOKENS (Scoped Widgets) ───────────────── */
    --header-height:             76px;
    --product-card-radius:       var(--radius-md);
    --product-card-shadow:       var(--shadow-card);
    --cart-drawer-width:         440px;
    --sticky-bar-height:         70px;
}
```

---

## 3. SUPERCLASS THEME SCAFFOLDING

### 3.1 Generate Theme Name
Generate a distinctive name for the theme:
`beeclue-{randomword}-theme` (e.g., `beeclue-lumiere-theme`, `beeclue-apex-theme`, `beeclue-zenith-theme`)

### 3.2 Modular Directory Structure (`template-parts/`)
A superclass theme separates markup into clean, reusable template parts rather than monolithic files:

```
wp-content/themes/beeclue-{name}-theme/
├── style.css                      # Theme header + 3-layer design tokens + base styles
├── functions.php                  # Theme setup, custom-logo, enqueues, WC hooks
├── header.php                     # Sticky header container + template part loaders
├── footer.php                     # 4-col footer + mandatory Beeclue agency branding
├── index.php                      # Fallback template
├── page.php                       # Default page template
├── single.php                     # Single post template
├── search.php                     # Accessible search results template
├── 404.php                        # Custom 404 with search & popular collections
├── template-home.php              # Homepage (Template Name: Homepage)
├── template-about.php             # About Us (Template Name: About Us)
├── template-contact.php           # Contact (Template Name: Contact)
├── template-faq.php               # FAQ (Template Name: FAQ + Schema parser)
├── woocommerce.css                # Superclass WooCommerce style overrides
├── template-parts/                # MODULAR COMPONENT PARTIALS
│   ├── header/
│   │   ├── nav-desktop.php        # Centered links, dropdowns, SVG icons
│   │   ├── nav-mobile.php         # Full-page glassmorphism overlay + a11y trap
│   │   └── search-overlay.php     # Full-screen accessible search dialog
│   ├── product/
│   │   ├── card.php               # Card with swatches, hover quick-add, badges
│   │   └── sticky-bar.php         # Floating PDP Add-to-Cart bar
│   ├── cart/
│   │   ├── drawer.php             # AJAX slide-out cart drawer
│   │   └── shipping-bar.php       # Dynamic free shipping progress meter
│   └── ui/
│       ├── trust-marquee.php      # Infinite CSS scroll trust bar
│       └── live-region.php        # Screen reader accessibility announcement region
├── assets/
│   ├── css/
│   │   └── critical.css           # Above-the-fold critical CSS (inlined)
│   └── js/
│       ├── main.js                # Sticky nav, search modal, a11y focus traps
│       ├── cart-drawer.js         # AJAX cart, shipping bar calculation, cross-sells
│       ├── single-product.js      # Sticky add-to-cart bar, variant swatches
│       └── animations.js          # IntersectionObserver lightweight scroll reveal
└── inc/
    ├── customizer.php             # Cart mode (drawer vs full), free shipping threshold, socials
    ├── seo.php                    # JSON-LD (WebSite, Org, Product, FAQPage, Breadcrumbs)
    └── performance.php            # Preload, font preconnect, script defer, emoji cleanup
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

### 4.3 `header.php` — Sticky Header + Navigation (REQUIRED — CRITICAL)

The navigation is the most important UI element after the hero. It must be pixel-perfect on desktop and mobile.

#### Logo System (Native `custom_logo` + jsDelivr CDN Fallback)

Superclass themes support the WordPress Customizer native logo while maintaining the automatic Beeclue CDN default for rapid prototyping.

**Logo URLs (Fallback defaults):**
- **Light backgrounds** (cream, white, light sections): `https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-blue.png`
- **Dark backgrounds** (dark sections, footer, dark hero): `https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-white.png`

**Logo implementation in `header.php`:**
```php
<div class="header-logo-wrap">
    <?php if (has_custom_logo()) : ?>
        <?php the_custom_logo(); ?>
    <?php else : ?>
        <a href="<?php echo home_url('/'); ?>" class="site-logo" aria-label="<?php bloginfo('name'); ?>">
            <img src="https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-blue.png"
                 alt="<?php bloginfo('name'); ?>"
                 class="logo-logo logo-light"
                 width="160" height="40" loading="eager" decoding="async">
            <img src="https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-white.png"
                 alt="<?php bloginfo('name'); ?>"
                 class="logo-logo logo-dark"
                 width="160" height="40" loading="eager" decoding="async">
        </a>
    <?php endif; ?>
</div>
```

**Logo CSS (in style.css):**
```css
.site-logo { display: flex; align-items: center; }
.logo-logo { height: 32px; width: auto; transition: opacity 0.3s ease; }
.logo-dark { display: none; }

/* When header has .scrolled or .dark-bg class, swap logos */
.header-scrolled .logo-light,
.site-header.dark-bg .logo-light { display: none; }
.header-scrolled .logo-dark,
.site-header.dark-bg .logo-dark { display: block; }

/* Sticky header on dark sections: show white logo by default */
.site-header.on-dark .logo-light { display: none; }
.site-header.on-dark .logo-dark { display: block; }
.site-header.on-dark.header-scrolled .logo-dark { display: none; }
.site-header.on-dark.header-scrolled .logo-light { display: block; }
```

**Logo JS (in main.js):**
```javascript
// Swap logo based on scroll position (when header passes dark sections)
document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('.site-header');
    if (!header) return;

    const observer = new IntersectionObserver(([entry]) => {
        header.classList.toggle('header-scrolled', !entry.isIntersecting);
    }, { threshold: 0, rootMargin: '-1px 0px 0px 0px' });

    const hero = document.querySelector('.hero, .hero-section, [class*="hero"]');
    if (hero) observer.observe(hero);
});
```

#### Desktop Navigation (>1024px)

The desktop nav must feel premium, spacious, and intentional. NOT a generic WordPress menu dump.

**Structure:**
```
┌──────────────────────────────────────────────────────────────────────────┐
│ [Logo]          Shop ▾   Collections ▾   About   Contact    [🔍] [🛒] [Shop Now] │
└──────────────────────────────────────────────────────────────────────────┘
```

**Desktop Nav Requirements:**
- Sticky on scroll with subtle backdrop-blur + shadow transition
- Logo left, nav links center, icons + CTA right
- Max-width: 1440px, centered, with generous horizontal padding (48px左右)
- Nav links: 15px, font-body, 500 weight, letter-spacing 0.02em
- Hover state: underline slide-in animation (CSS-only, `transform: scaleX`)
- Dropdown menus (if any): mega-menu style with 2-4 columns, smooth fade-in + slide-down
- CTA button: `.btn-primary` pill style, rightmost element
- Cart icon: SVG with AJAX count badge (red dot, top-right)
- Search icon: SVG, opens a full-screen or slide-down search overlay

**Desktop Nav CSS:**
```css
.site-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    padding: 0 clamp(24px, 4vw, 48px);
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid transparent;
    transition: all 0.3s ease;
}

.site-header.scrolled {
    background: rgba(255, 255, 255, 0.95);
    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
    box-shadow: 0 1px 8px rgba(0, 0, 0, 0.04);
}

.nav-links {
    display: flex;
    gap: 32px;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-links a {
    font-size: 15px;
    font-weight: 500;
    color: var(--color-ink);
    text-decoration: none;
    position: relative;
    padding: 4px 0;
    transition: color 0.2s;
}

.nav-links a::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 1.5px;
    background: var(--color-accent);
    transform: scaleX(0);
    transform-origin: right;
    transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.nav-links a:hover::after {
    transform: scaleX(1);
    transform-origin: left;
}

.nav-icons {
    display: flex;
    align-items: center;
    gap: 20px;
}

.nav-icons svg {
    width: 20px;
    height: 20px;
    stroke: var(--color-ink);
    stroke-width: 1.5;
    fill: none;
    cursor: pointer;
    transition: stroke 0.2s;
}

.nav-icons svg:hover { stroke: var(--color-accent); }

.cart-count {
    position: absolute;
    top: -6px;
    right: -8px;
    background: var(--color-accent);
    color: white;
    font-size: 10px;
    font-weight: 600;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    line-height: 1;
}
```

#### Mobile Navigation (<1024px) — FULL PAGE GLASSMORPHISM OVERLAY

The mobile menu is a full-screen overlay with glassmorphism (frosted glass effect). It slides down from the top with a staggered fade-in animation. This is NOT a hamburger drawer from the side — it's a premium full-page takeover.

**Mobile Menu Structure:**
```
┌──────────────────────────────────────┐
│ [Logo]                        [✕]   │  ← Fixed top bar
├──────────────────────────────────────┤
│                                      │
│  Shop                          →    │  ← Large nav links, staggered fade-in
│  Collections                  →    │
│  About                         →    │
│  Contact                       →    │
│                                      │
│  ─────────────────────────────────  │
│                                      │
│  🔍 Search                          │  ← Secondary actions
│  🛒 Cart (3)                        │
│                                      │
│  ─────────────────────────────────  │
│                                      │
│  [ Instagram ]  [ Facebook ]        │  ← Social links
│  [ TikTok ]     [ Pinterest ]       │
│                                      │
│  ─────────────────────────────────  │
│                                      │
│  📍 Store Location                  │  ← Contact info
│  📧 hello@store.com                 │
│                                      │
└──────────────────────────────────────┘
```

**Mobile Menu HTML (in header.php, hidden by default):**
```html
<!-- Mobile Navigation Overlay -->
<div class="mobile-nav" id="mobile-nav" aria-hidden="true" role="dialog" aria-label="Mobile navigation">
    <div class="mobile-nav-backdrop"></div>
    <div class="mobile-nav-panel">
        <div class="mobile-nav-header">
            <a href="<?php echo home_url('/'); ?>" class="site-logo" aria-label="Home">
                <img src="https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-blue.png"
                     alt="<?php bloginfo('name'); ?>" class="logo-logo" width="140" height="35" loading="eager">
            </a>
            <button class="mobile-nav-close" id="mobile-nav-close" aria-label="Close menu">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                    <path d="M18 6L6 18M6 6l12 12"/>
                </svg>
            </button>
        </div>

        <nav class="mobile-nav-links" role="navigation">
            <?php
            wp_nav_menu([
                'theme_location' => 'primary',
                'container'      => false,
                'menu_class'     => 'mobile-menu-list',
                'fallback_cb'    => false,
                'depth'          => 2,
            ]);
            ?>
        </nav>

        <div class="mobile-nav-actions">
            <a href="<?php echo home_url('/search/'); ?>" class="mobile-nav-action">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
                Search
            </a>
            <a href="<?php echo wc_get_cart_url(); ?>" class="mobile-nav-action">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18"/><path d="M16 10a4 4 0 01-8 0"/></svg>
                Cart (<?php echo WC()->cart->get_cart_contents_count(); ?>)
            </a>
        </div>

        <div class="mobile-nav-social">
            <?php
            $socials = [
                'instagram' => 'Instagram',
                'facebook'  => 'Facebook',
                'tiktok'    => 'TikTok',
                'pinterest' => 'Pinterest',
            ];
            foreach ($socials as $key => $label) :
                $url = get_theme_mod("social_{$key}", '');
                if ($url) :
            ?>
                <a href="<?php echo esc_url($url); ?>" target="_blank" rel="noopener noreferrer" aria-label="<?php echo $label; ?>">
                    <?php echo $label; ?>
                </a>
            <?php
                endif;
            endforeach;
            ?>
        </div>

        <div class="mobile-nav-contact">
            <a href="mailto:<?php echo antispambot(get_option('admin_email')); ?>"><?php echo antispambot(get_option('admin_email')); ?></a>
        </div>
    </div>
</div>
```

**Mobile Menu CSS (in style.css):**
```css
/* Hamburger button */
.mobile-nav-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
    z-index: 1001;
}

.mobile-nav-toggle span {
    display: block;
    width: 22px;
    height: 1.5px;
    background: var(--color-ink);
    margin: 5px 0;
    transition: all 0.3s ease;
    transform-origin: center;
}

/* Hamburger → X animation */
.mobile-nav-toggle.active span:nth-child(1) { transform: rotate(45deg) translate(4px, 5px); }
.mobile-nav-toggle.active span:nth-child(2) { opacity: 0; }
.mobile-nav-toggle.active span:nth-child(3) { transform: rotate(-45deg) translate(4px, -5px); }

@media (max-width: 1024px) {
    .mobile-nav-toggle { display: block; }
    .nav-links, .nav-icons .nav-cta { display: none; }
}

/* Full-page glassmorphism overlay */
.mobile-nav {
    position: fixed;
    inset: 0;
    z-index: 2000;
    visibility: hidden;
    opacity: 0;
    transition: visibility 0s 0.4s, opacity 0.3s ease;
}

.mobile-nav.active {
    visibility: visible;
    opacity: 1;
    transition-delay: 0s;
}

/* Frosted glass backdrop */
.mobile-nav-backdrop {
    position: absolute;
    inset: 0;
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
}

/* Slide-down panel */
.mobile-nav-panel {
    position: relative;
    height: 100%;
    overflow-y: auto;
    padding: 0 clamp(24px, 6vw, 48px);
    padding-top: 80px;
    transform: translateY(-20px);
    transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.mobile-nav.active .mobile-nav-panel {
    transform: translateY(0);
}

/* Mobile nav header (logo + close) */
.mobile-nav-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 72px;
    padding: 0 clamp(24px, 6vw, 48px);
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    z-index: 1;
}

.mobile-nav-close {
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
    color: var(--color-ink);
    transition: transform 0.2s;
}
.mobile-nav-close:hover { transform: rotate(90deg); }

/* Nav links — large, spaced */
.mobile-menu-list {
    list-style: none;
    padding: 0;
    margin: 0 0 32px;
}

.mobile-menu-list li {
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    opacity: 0;
    transform: translateY(12px);
    transition: opacity 0.3s ease, transform 0.3s ease;
}

.mobile-nav.active .mobile-menu-list li {
    opacity: 1;
    transform: translateY(0);
}

/* Staggered fade-in */
.mobile-nav.active .mobile-menu-list li:nth-child(1) { transition-delay: 0.1s; }
.mobile-nav.active .mobile-menu-list li:nth-child(2) { transition-delay: 0.15s; }
.mobile-nav.active .mobile-menu-list li:nth-child(3) { transition-delay: 0.2s; }
.mobile-nav.active .mobile-menu-list li:nth-child(4) { transition-delay: 0.25s; }
.mobile-nav.active .mobile-menu-list li:nth-child(5) { transition-delay: 0.3s; }
.mobile-nav.active .mobile-menu-list li:nth-child(6) { transition-delay: 0.35s; }

.mobile-menu-list a {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 0;
    font-size: 28px;
    font-weight: 500;
    color: var(--color-ink);
    text-decoration: none;
    font-family: var(--font-heading);
    letter-spacing: -0.01em;
    transition: color 0.2s, padding-left 0.2s;
}

.mobile-menu-list a:hover {
    color: var(--color-accent);
    padding-left: 8px;
}

/* Sub-menu (dropdown) */
.mobile-menu-list .sub-menu {
    list-style: none;
    padding: 0 0 12px 16px;
    margin: 0;
}

.mobile-menu-list .sub-menu a {
    font-size: 18px;
    font-family: var(--font-body);
    font-weight: 400;
    padding: 10px 0;
    opacity: 0.7;
}

/* Actions row (search + cart) */
.mobile-nav-actions {
    display: flex;
    gap: 24px;
    padding: 24px 0;
    border-top: 1px solid rgba(0, 0, 0, 0.05);
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    opacity: 0;
    transform: translateY(12px);
    transition: opacity 0.3s ease 0.3s, transform 0.3s ease 0.3s;
}

.mobile-nav.active .mobile-nav-actions {
    opacity: 1;
    transform: translateY(0);
}

.mobile-nav-action {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 15px;
    font-weight: 500;
    color: var(--color-ink);
    text-decoration: none;
    transition: color 0.2s;
}
.mobile-nav-action:hover { color: var(--color-accent); }

/* Social links */
.mobile-nav-social {
    display: flex;
    gap: 16px;
    padding: 24px 0;
    opacity: 0;
    transform: translateY(12px);
    transition: opacity 0.3s ease 0.35s, transform 0.3s ease 0.35s;
}

.mobile-nav.active .mobile-nav-social {
    opacity: 1;
    transform: translateY(0);
}

.mobile-nav-social a {
    font-size: 13px;
    font-weight: 500;
    color: var(--color-muted);
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    transition: color 0.2s;
}
.mobile-nav-social a:hover { color: var(--color-accent); }

/* Contact info */
.mobile-nav-contact {
    padding: 24px 0;
    opacity: 0;
    transform: translateY(12px);
    transition: opacity 0.3s ease 0.4s, transform 0.3s ease 0.4s;
}

.mobile-nav.active .mobile-nav-contact {
    opacity: 1;
    transform: translateY(0);
}

.mobile-nav-contact a {
    font-size: 14px;
    color: var(--color-muted);
    text-decoration: none;
}

/* Body scroll lock when menu open */
body.mobile-nav-open {
    overflow: hidden;
}
```

**Mobile Menu JS (in main.js):**
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('.mobile-nav-toggle');
    const nav = document.getElementById('mobile-nav');
    const closeBtn = document.getElementById('mobile-nav-close');
    const backdrop = nav?.querySelector('.mobile-nav-backdrop');

    if (!toggle || !nav) return;

    const openMenu = () => {
        nav.classList.add('active');
        nav.setAttribute('aria-hidden', 'false');
        toggle.classList.add('active');
        document.body.classList.add('mobile-nav-open');
    };

    const closeMenu = () => {
        nav.classList.remove('active');
        nav.setAttribute('aria-hidden', 'true');
        toggle.classList.remove('active');
        document.body.classList.remove('mobile-nav-open');
    };

    toggle.addEventListener('click', openMenu);
    closeBtn?.addEventListener('click', closeMenu);
    backdrop?.addEventListener('click', closeMenu);

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && nav.classList.contains('active')) closeMenu();
    });

    // Close on link click (for SPA-like behavior)
    nav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', closeMenu);
    });
});
```

**Hamburger button (in header.php, before mobile-nav div):**
```html
<button class="mobile-nav-toggle" id="mobile-nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">
    <span></span>
    <span></span>
    <span></span>
</button>
```

#### Full header.php structure:
```php
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://images.unsplash.com">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<a href="#main-content" class="skip-to-content">Skip to content</a>

<header class="site-header" id="site-header">
    <div class="header-inner">
        <!-- Logo (auto-switches light/dark) -->
        <a href="<?php echo home_url('/'); ?>" class="site-logo" aria-label="<?php bloginfo('name'); ?>">
            <img src="https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-blue.png"
                 alt="<?php bloginfo('name'); ?>" class="logo-logo logo-light" width="160" height="40" loading="eager" decoding="async">
            <img src="https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-white.png"
                 alt="<?php bloginfo('name'); ?>" class="logo-logo logo-dark" width="160" height="40" loading="eager" decoding="async">
        </a>

        <!-- Desktop Navigation -->
        <nav class="nav-desktop" aria-label="Main navigation">
            <?php
            wp_nav_menu([
                'theme_location' => 'primary',
                'container'      => false,
                'menu_class'     => 'nav-links',
                'fallback_cb'    => false,
                'depth'          => 2,
            ]);
            ?>
        </nav>

        <!-- Desktop Icons + CTA -->
        <div class="nav-icons">
            <a href="<?php echo home_url('/search/'); ?>" aria-label="Search">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
            </a>
            <a href="<?php echo wc_get_cart_url(); ?>" class="cart-icon" id="cart-toggle" aria-label="Cart">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18"/><path d="M16 10a4 4 0 01-8 0"/></svg>
                <span class="cart-count"><?php echo WC()->cart->get_cart_contents_count(); ?></span>
            </a>
            <a href="<?php echo wc_get_page_permalink('shop'); ?>" class="btn btn-primary nav-cta">Shop Now</a>
        </div>

        <!-- Mobile Hamburger -->
        <button class="mobile-nav-toggle" id="mobile-nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">
            <span></span><span></span><span></span>
        </button>
    </div>
</header>

<!-- Mobile Navigation Overlay (glassmorphism) -->
<div class="mobile-nav" id="mobile-nav" aria-hidden="true" role="dialog" aria-label="Mobile navigation">
    <div class="mobile-nav-backdrop"></div>
    <div class="mobile-nav-panel">
        <!-- ... (mobile nav content from above) ... -->
    </div>
</div>

<main id="main-content">
```

#### Search Overlay

Every theme MUST include a full-screen search overlay triggered by the search icon in the header.

**Search overlay HTML (in `header.php`, after mobile-nav div):**
```html
<!-- Search Overlay -->
<div class="search-overlay" id="search-overlay" aria-hidden="true" role="search" aria-label="Search">
    <div class="search-overlay-backdrop"></div>
    <div class="search-overlay-panel">
        <div class="search-overlay-header">
            <h2>Search</h2>
            <button class="search-overlay-close" id="search-overlay-close" aria-label="Close search">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M18 6L6 18M6 6l12 12"/></svg>
            </button>
        </div>
        <form class="search-overlay-form" action="<?php echo esc_url(home_url('/')); ?>" method="get" role="search">
            <div class="search-overlay-input-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
                <input type="search" name="s" class="search-overlay-input" placeholder="What are you looking for?" autocomplete="off" autofocus>
                <button type="submit" class="search-overlay-submit">Search</button>
            </div>
        </form>
        <div class="search-overlay-links">
            <span class="search-overlay-label">Popular:</span>
            <a href="<?php echo wc_get_page_permalink('shop'); ?>">Shop All</a>
            <a href="<?php echo home_url('/new-arrivals/'); ?>">New Arrivals</a>
            <a href="<?php echo home_url('/sale/'); ?>">Sale</a>
        </div>
    </div>
</div>
```

**Search overlay CSS:**
```css
.search-overlay {
    position: fixed;
    inset: 0;
    z-index: 2500;
    visibility: hidden;
    opacity: 0;
    transition: visibility 0s 0.3s, opacity 0.3s ease;
}
.search-overlay.open {
    visibility: visible;
    opacity: 1;
    transition-delay: 0s;
}
.search-overlay-backdrop {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(8px);
}
.search-overlay-panel {
    position: relative;
    max-width: 680px;
    margin: 0 auto;
    padding: 80px 24px 40px;
    transform: translateY(-30px);
    transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.search-overlay.open .search-overlay-panel { transform: translateY(0); }
.search-overlay-header {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 32px;
}
.search-overlay-header h2 { color: white; font-size: 14px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.1em; margin: 0; }
.search-overlay-close { background: none; border: none; cursor: pointer; color: white; padding: 4px; }
.search-overlay-form { margin-bottom: 24px; }
.search-overlay-input-wrap {
    display: flex; align-items: center; gap: 12px;
    border-bottom: 2px solid rgba(255,255,255,0.3);
    padding-bottom: 12px;
}
.search-overlay-input-wrap svg { color: white; flex-shrink: 0; }
.search-overlay-input {
    flex: 1; background: none; border: none; outline: none;
    color: white; font-size: 32px; font-family: var(--font-heading);
    font-weight: 400;
}
.search-overlay-input::placeholder { color: rgba(255,255,255,0.5); }
.search-overlay-submit {
    background: var(--color-accent); color: white; border: none; padding: 10px 24px;
    border-radius: var(--radius-full); font-size: 14px; font-weight: 600;
    cursor: pointer; transition: background 0.2s;
}
.search-overlay-submit:hover { background: var(--color-accent-hover); }
.search-overlay-links { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.search-overlay-label { color: rgba(255,255,255,0.5); font-size: 13px; }
.search-overlay-links a {
    color: rgba(255,255,255,0.8); font-size: 13px; text-decoration: none;
    padding: 4px 12px; border: 1px solid rgba(255,255,255,0.2); border-radius: var(--radius-full);
    transition: all 0.2s;
}
.search-overlay-links a:hover { background: rgba(255,255,255,0.1); color: white; }
```

**Search overlay JS (in `main.js`):**
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const searchToggle = document.querySelector('.nav-icons [aria-label="Search"], [href*="search"]');
    const overlay       = document.getElementById('search-overlay');
    const closeBtn      = document.getElementById('search-overlay-close');
    const backdrop      = overlay?.querySelector('.search-overlay-backdrop');
    const input         = overlay?.querySelector('.search-overlay-input');

    if (!searchToggle || !overlay) return;

    const openSearch = () => {
        overlay.classList.add('open');
        overlay.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        setTimeout(() => input?.focus(), 100);
    };

    const closeSearch = () => {
        overlay.classList.remove('open');
        overlay.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    };

    searchToggle.addEventListener('click', (e) => { e.preventDefault(); openSearch(); });
    closeBtn?.addEventListener('click', closeSearch);
    backdrop?.addEventListener('click', closeSearch);
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && overlay.classList.contains('open')) closeSearch();
    });
});
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

---

## 5. SUPERCLASS WOOCOMMERCE INTEGRATION

Every Beeclue superclass theme transforms the default WooCommerce experience into a high-converting, modern storefront. See `references/ecommerce-ux-patterns.md` for full implementation code.

---

### 5.1 Single Product: Floating Sticky Add-to-Cart Bar

On single product pages, when a user scrolls past the primary Add-to-Cart button, a sleek sticky bar slides in at the bottom of the viewport (or top on mobile) to maintain maximum conversion momentum.

**Template Part (`template-parts/product/sticky-bar.php`):**
```php
<?php
global $product;
if (!$product) return;
?>
<div class="product-sticky-bar" id="product-sticky-bar" aria-hidden="true">
    <div class="sticky-bar-container">
        <div class="sticky-bar-product">
            <?php echo $product->get_image('thumbnail', ['class' => 'sticky-bar-thumb', 'loading' => 'lazy']); ?>
            <div class="sticky-bar-meta">
                <span class="sticky-bar-title"><?php echo esc_html($product->get_name()); ?></span>
                <span class="sticky-bar-price"><?php echo $product->get_price_html(); ?></span>
            </div>
        </div>
        <div class="sticky-bar-action">
            <?php if ($product->is_type('simple')) : ?>
                <button type="button" class="btn btn-primary sticky-bar-btn" id="sticky-bar-buy-btn">
                    Add to Cart
                </button>
            <?php else : ?>
                <a href="#product-options" class="btn btn-primary sticky-bar-btn">
                    Select Options
                </a>
            <?php endif; ?>
        </div>
    </div>
</div>
```

**JavaScript Observer (`assets/js/single-product.js`):**
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const stickyBar = document.getElementById('product-sticky-bar');
    const mainCta   = document.querySelector('.single_add_to_cart_button');
    const buyBtn    = document.getElementById('sticky-bar-buy-btn');

    if (!stickyBar || !mainCta) return;

    const observer = new IntersectionObserver(([entry]) => {
        const isVisible = entry.isIntersecting;
        stickyBar.classList.toggle('active', !isVisible);
        stickyBar.setAttribute('aria-hidden', isVisible ? 'true' : 'false');
    }, { threshold: 0, rootMargin: '-60px 0px 0px 0px' });

    observer.observe(mainCta);

    buyBtn?.addEventListener('click', () => {
        mainCta.click();
    });
});
```

---

### 5.2 Visual Variant Swatches (Color & Size Pills)

Default HTML `<select>` elements destroy mobile conversion. Superclass themes replace them with interactive swatch buttons:

- **Color Swatches**: Circular buttons (`36x36px`) displaying the product's color code, with active focus rings and tooltip labels.
- **Size Pills**: Rounded rectangular buttons (`44px` height) with instant active state toggle.
- **Accessibility**: Grouped with `role="radiogroup"` and individual buttons using `role="radio"` and `aria-checked="true|false"`.

---

### 5.3 High-Converting Product Card Grid (`template-parts/product/card.php`)

Every product card in shop catalogs, category archives, and homepage grids must feature:
1. **Aspect Ratio Container**: Consistent `1:1` or `4:5` ratio preventing layout shift (CLS 0.00).
2. **Secondary Hover Image**: Smooth cross-fade to lifestyle or detail shot on hover.
3. **Badges**: Floating badges for `Sale (-20%)`, `New Arrival`, or `Low Stock (< 5 left)`.
4. **Eyebrow & Title**: Category eyebrow label (11px uppercase) + product title (16px, 500 weight).
5. **Rating & Price**: Star rating snippets + clean currency formatting.
6. **Tactile Quick-Add**: A hover-revealed pill button that dispatches AJAX add-to-cart without redirecting to the cart page.

---

### 5.4 Superclass Style Overrides (`woocommerce.css`)

Ensure `woocommerce.css` completely strips legacy WooCommerce styles in favor of your 3-layer design tokens:
- Clean, borderless checkout form with float-label inputs.
- High-contrast coupon code bar with accordion toggle.
- Clean order review summary card with rounded corners and subtle elevation.
- Custom WooCommerce notice alerts (success, error, info) styled to match brand feedback tokens.

---

## 6. PAGE TEMPLATES & CONTENT

### 6.1 Required Pages (create ALL of these via WP-CLI)
After theme activation, create these pages and assign templates:

```bash
# Create pages
wp post create --post_type=page --post_title="Home" --post_status=publish --page_template=template-home.php --path=/path/to/site
wp post create --post_type=page --post_title="About Us" --post_status=publish --page_template=template-about.php --path=/path/to/site
wp post create --post_type=page --post_title="Contact" --post_status=publish --page_template=template-contact.php --path=/path/to/site
wp post create --post_type=page --post_title="FAQ" --post_status=publish --page_template=template-faq.php --path=/path/to/site
wp post create --post_type=page --post_title="Privacy Policy" --post_status=publish --path=/path/to/site
wp post create --post_type=page --post_title="Terms of Service" --post_status=publish --path=/path/to/site

# WooCommerce creates a "Shop" page on activation. Verify it exists; if not, create it:
SHOP_PAGE_ID=$(wp option get woocommerce_shop_page_id --path=/path/to/site 2>/dev/null)
if [ -z "$SHOP_PAGE_ID" ] || [ "$SHOP_PAGE_ID" = "0" ]; then
    SHOP_PAGE_ID=$(wp post create --post_type=page --post_title="Shop" --post_status=publish --path=/path/to/site --field=ID)
    wp option update woocommerce_shop_page_id $SHOP_PAGE_ID --path=/path/to/site
    echo "Created Shop page with ID: $SHOP_PAGE_ID"
else
    echo "Shop page already exists with ID: $SHOP_PAGE_ID"
fi

# Set homepage
wp option update show_on_front page --path=/path/to/site
wp option update page_on_front $(wp post list --post_type=page --title="Home" --field=ID --path=/path/to/site) --path=/path/to/site

# Set up WooCommerce basic pages (cart, checkout, my account) if not present
wp wc tool run install_pages --user=1 --path=/path/to/site 2>/dev/null || true
```

### 6.1b Navigation Menu (REQUIRED — CRITICAL)

**The navigation menu MUST be created and populated via WP-CLI.** The theme registers the menu location in `functions.php` but the menu items themselves must be created. Without this step, the nav will be EMPTY.

```bash
# Create the primary navigation menu
wp menu create "Primary Menu" --path=/path/to/site

# Assign menu to the theme location registered in functions.php
wp menu location assign "Primary Menu" primary --path=/path/to/site

# Add menu items — use the actual page IDs from the pages created above
# First, get the page IDs:
HOME_ID=$(wp post list --post_type=page --title="Home" --field=ID --path=/path/to/site)
SHOP_ID=$(wp post list --post_type=page --title="Shop" --field=ID --path=/path/to/site 2>/dev/null || echo "")
ABOUT_ID=$(wp post list --post_type=page --title="About Us" --field=ID --path=/path/to/site)
CONTACT_ID=$(wp post list --post_type=page --title="Contact" --field=ID --path=/path/to/site)
FAQ_ID=$(wp post list --post_type=page --title="FAQ" --field=ID --path=/path/to/site)

# Add menu items (page type)
wp menu item add-post "Primary Menu" $HOME_ID --title="Home" --path=/path/to/site

# Add Shop link (WooCommerce shop page — if it exists)
if [ -n "$SHOP_ID" ]; then
    wp menu item add-post "Primary Menu" $SHOP_ID --title="Shop" --path=/path/to/site
else
    wp menu item add-custom "Primary Menu" "Shop" "$(wp option get woocommerce_shop_page_id --path=/path/to/site 2>/dev/null && echo "/?page_id=$(wp option get woocommerce_shop_page_id --path=/path/to/site)" || echo "/shop/")" --path=/path/to/site
fi

# Add other pages
wp menu item add-post "Primary Menu" $ABOUT_ID --title="About" --path=/path/to/site
wp menu item add-post "Primary Menu" $CONTACT_ID --title="Contact" --path=/path/to/site

# Add WooCommerce product categories as sub-menu items (optional but recommended)
# List product categories and add them under "Shop"
wp wc product_cat list --user=1 --path=/path/to/site --format=ids 2>/dev/null | tr ' ' '\n' | while read CAT_ID; do
    CAT_NAME=$(wp wc product_cat get $CAT_ID --user=1 --path=/path/to/site --field=name 2>/dev/null)
    CAT_SLUG=$(wp wc product_cat get $CAT_ID --user=1 --path=/path/to/site --field=slug 2>/dev/null)
    if [ -n "$CAT_NAME" ]; then
        wp menu item add-custom "Primary Menu" "$CAT_NAME" "/product-category/$CAT_SLUG/" --path=/path/to/site
    fi
done

# Add a custom "Sale" link pointing to the sale products page
wp menu item add-custom "Primary Menu" "Sale" "/product-tag/sale/" --path=/path/to/site

# Verify the menu structure
wp menu list "Primary Menu" --path=/path/to/site

# Optional: Create footer menu
wp menu create "Footer Menu" --path=/path/to/site
wp menu location assign "Footer Menu" footer --path=/path/to/site
wp menu item add-post "Footer Menu" $ABOUT_ID --title="About Us" --path=/path/to/site
wp menu item add-post "Footer Menu" $CONTACT_ID --title="Contact" --path=/path/to/site
wp menu item add-post "Footer Menu" $FAQ_ID --title="FAQ" --path=/path/to/site
wp menu item add-custom "Footer Menu" "Privacy Policy" "/privacy-policy/" --path=/path/to/site
wp menu item add-custom "Footer Menu" "Terms of Service" "/terms-of-service/" --path=/path/to/site
```

**Menu structure to create (minimum required):**
```
Primary Menu (location: primary)
├── Home           → / (page: Home)
├── Shop           → /shop/ (WooCommerce shop page)
│   ├── [Category 1] → /product-category/[slug]/
│   ├── [Category 2] → /product-category/[slug]/
│   └── Sale        → /product-tag/sale/
├── About          → /about-us/ (page: About Us)
└── Contact        → /contact/ (page: Contact)
```

**Footer Menu (location: footer):**
```
Footer Menu (location: footer)
├── About Us        → /about-us/
├── Contact         → /contact/
├── FAQ             → /faq/
├── Privacy Policy  → /privacy-policy/
└── Terms of Service → /terms-of-service/
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

**Unsplash Images:** The old `source.unsplash.com` random endpoint is DEPRECATED and returns 404s. ALWAYS use specific Unsplash photo URLs via the direct image URL format. Here are curated, high-quality photos by niche. Pick the relevant set.

**Image URL format (REQUIRED):**
```
https://images.unsplash.com/photo-{ID}?w={WIDTH}&h={HEIGHT}&fit=crop&auto=format&q=80
```

**Curated Image Sets by Niche:**

*Fashion / Apparel:*
```
Hero:       https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=1600&h=900&fit=crop&auto=format&q=80
Editorial:  https://images.unsplash.com/photo-1558171813-4c088753af8f?w=800&h=1000&fit=crop&auto=format&q=80
Product:    https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=600&h=600&fit=crop&auto=format&q=80
Category:   https://images.unsplash.com/photo-1483985988355-763728e1935b?w=600&h=400&fit=crop&auto=format&q=80
Lifestyle:  https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=800&h=600&fit=crop&auto=format&q=80
```

*Home Goods / Interiors:*
```
Hero:       https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=1600&h=900&fit=crop&auto=format&q=80
Editorial:  https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=800&h=1000&fit=crop&auto=format&q=80
Product:    https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=600&h=600&fit=crop&auto=format&q=80
Category:   https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&h=400&fit=crop&auto=format&q=80
Lifestyle:  https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=800&h=600&fit=crop&auto=format&q=80
```

*Beauty / Skincare:*
```
Hero:       https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=1600&h=900&fit=crop&auto=format&q=80
Editorial:  https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=800&h=1000&fit=crop&auto=format&q=80
Product:    https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=600&h=600&fit=crop&auto=format&q=80
Category:   https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=600&h=400&fit=crop&auto=format&q=80
Lifestyle:  https://images.unsplash.com/photo-1512496015851-a90fb3edba7b?w=800&h=600&fit=crop&auto=format&q=80
```

*Food / Gourmet:*
```
Hero:       https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=1600&h=900&fit=crop&auto=format&q=80
Editorial:  https://images.unsplash.com/photo-1476224203421-9ac39bcb3327?w=800&h=1000&fit=crop&auto=format&q=80
Product:    https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600&h=600&fit=crop&auto=format&q=80
Category:   https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600&h=400&fit=crop&auto=format&q=80
Lifestyle:  https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=800&h=600&fit=crop&auto=format&q=80
```

*Jewelry / Accessories:*
```
Hero:       https://images.unsplash.com/photo-1515562141589-67f0d569b6c0?w=1600&h=900&fit=crop&auto=format&q=80
Editorial:  https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=800&h=1000&fit=crop&auto=format&q=80
Product:    https://images.unsplash.com/photo-1603561591411-07134e71a2a9?w=600&h=600&fit=crop&auto=format&q=80
Category:   https://images.unsplash.com/photo-1611652022419-a9419f74343d?w=600&h=400&fit=crop&auto=format&q=80
Lifestyle:  https://images.unsplash.com/photo-1617038260897-41a1f14a8ca0?w=800&h=600&fit=crop&auto=format&q=80
```

*Generic / Default (any niche):*
```
Hero:       https://images.unsplash.com/photo-1441984904996-e0b6ba687e04?w=1600&h=900&fit=crop&auto=format&q=80
Editorial:  https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&h=1000&fit=crop&auto=format&q=80
Product:    https://images.unsplash.com/photo-1472289065668-ce650ac443d2?w=600&h=600&fit=crop&auto=format&q=80
Category:   https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=600&h=400&fit=crop&auto=format&q=80
Lifestyle:  https://images.unsplash.com/photo-1556742393-d75f468bfcb0?w=800&h=600&fit=crop&auto=format&q=80
```

**How to use in templates:**
```php
<!-- Hero background -->
<section class="hero" style="background-image: url('https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=1600&h=900&fit=crop&auto=format&q=80');">

<!-- Editorial split image -->
<img src="https://images.unsplash.com/photo-1558171813-4c088753af8f?w=800&h=1000&fit=crop&auto=format&q=80"
     alt="Brand story" width="800" height="1000" loading="lazy" decoding="async">

<!-- Category card -->
<img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=600&h=400&fit=crop&auto=format&q=80"
     alt="Shop collection" width="600" height="400" loading="lazy" decoding="async">
```

**Image rules:**
- ALWAYS add `w=`, `h=`, `fit=crop`, `auto=format`, `q=80` parameters
- ALWAYS add explicit `width` and `height` attributes (prevents CLS)
- ALWAYS add `loading="lazy"` on below-fold images (hero uses `loading="eager"`)
- ALWAYS add descriptive `alt` text
- NEVER use the old `source.unsplash.com/random` endpoint (deprecated, returns 404)

### 6.3 About Page (`template-about.php`)
- Hero with brand statement
- Team / founder section
- Brand values grid
- Timeline or milestones
- CTA to shop

**Images for About page:**
```
Hero:       https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1600&h=600&fit=crop&auto=format&q=80
Team:       https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&h=600&fit=crop&auto=format&q=80
Values:     https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&h=400&fit=crop&auto=format&q=80
```

### 6.4 Contact Page (`template-contact.php`)
- Contact info (address, email, phone)
- Embed Fluent Forms contact form via shortcode: `[fluentform id="1"]`
- Google Maps embed placeholder
- Social media links

### 6.5 FAQ Page (`template-faq.php`)
- Accordion-style FAQ using `<details>` / `<summary>` (native HTML, no JS needed)
- Structured data (FAQPage schema) — see SEO section

### 6.6 404 Page (`404.php`)
The 404 page must recover lost visitors. Never show a bare "Page not found."

**Required elements:**
1. **H1**: "Page not found" or "Oops — that page doesn't exist"
2. **Subtext**: "The page you're looking for may have been moved or no longer exists."
3. **Search bar**: Reuse the search overlay or include an inline search form
4. **Popular links**: 3–4 links to highest-traffic pages (Shop, Best Sellers, New Arrivals, Contact)
5. **CTA button**: "Back to Shop" linking to the WooCommerce shop page
6. **Optional**: Product recommendations (recent or featured products via `wc_get_products()`)

```php
<?php get_header(); ?>
<main id="main-content" class="page-404">
    <div class="container section-padding" style="text-align: center; min-height: 60vh; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <span class="eyebrow">Error 404</span>
        <h1 style="font-family: var(--font-heading); font-size: var(--text-section); margin: 16px 0;">Page not found</h1>
        <p style="color: var(--color-muted); max-width: 420px; margin-bottom: 32px;">The page you're looking for may have been moved or no longer exists. Let's get you back on track.</p>
        <form role="search" action="<?php echo esc_url(home_url('/')); ?>" method="get" style="display: flex; gap: 8px; margin-bottom: 24px;">
            <input type="search" name="s" placeholder="Search our store..." style="padding: 12px 16px; border: 1px solid rgba(0,0,0,0.1); border-radius: var(--radius-full); font-size: 15px; width: 280px;">
            <button type="submit" class="btn btn-primary">Search</button>
        </form>
        <a href="<?php echo wc_get_page_permalink('shop'); ?>" class="btn btn-primary" style="margin-bottom: 32px;">Back to Shop</a>
        <div style="display: flex; gap: 24px; flex-wrap: wrap; justify-content: center;">
            <a href="<?php echo wc_get_page_permalink('shop'); ?>" style="color: var(--color-muted); text-decoration: underline;">Shop All</a>
            <a href="<?php echo home_url('/new-arrivals/'); ?>" style="color: var(--color-muted); text-decoration: underline;">New Arrivals</a>
            <a href="<?php echo home_url('/contact/'); ?>" style="color: var(--color-muted); text-decoration: underline;">Contact Us</a>
        </div>
    </div>
</main>
<?php get_footer(); ?>
```

### 6.7 Search Results Page (`search.php`)
Display search results in a clean, scannable grid.

**Required elements:**
1. **H1**: Dynamic — "Results for: {search query}"
2. **Result count**: "Showing X results"
3. **Results grid**: Product cards if WooCommerce results, post cards otherwise
4. **Empty state**: If no results — "No results found for '{query}'. Try a different search or browse our shop."
5. **Pagination**: Standard WordPress pagination

```php
<?php get_header(); ?>
<main id="main-content" class="page-search">
    <div class="container section-padding">
        <h1 style="font-family: var(--font-heading); font-size: var(--text-section);">Results for: "<?php echo esc_html(get_search_query()); ?>"</h1>
        <p style="color: var(--color-muted); margin-bottom: 48px;"><?php echo $wp_query->found_posts; ?> result<?php echo $wp_query->found_posts !== 1 ? 's' : ''; ?></p>

        <?php if (have_posts()) : ?>
            <div class="product-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px;">
                <?php while (have_posts()) : the_post(); ?>
                    <?php wc_get_template_part('content', 'product'); ?>
                <?php endwhile; ?>
            </div>
            <div style="margin-top: 48px; text-align: center;">
                <?php the_posts_pagination(); ?>
            </div>
        <?php else : ?>
            <div style="text-align: center; padding: 80px 0;">
                <p style="color: var(--color-muted); font-size: 18px; margin-bottom: 24px;">No results found. Try a different search or browse our shop.</p>
                <a href="<?php echo wc_get_page_permalink('shop'); ?>" class="btn btn-primary">Browse Shop</a>
            </div>
        <?php endif; ?>
    </div>
</main>
<?php get_footer(); ?>
```

### 6.8 Single Post Page (`single.php`)
Blog posts (if the blog is used for content marketing / TOFU traffic).

**Required elements:**
1. **Featured image**: Full-width, above the fold
2. **Post meta**: Author, date, category, reading time estimate
3. **H1**: Post title
4. **Content**: The post body with styled typography
5. **Share buttons**: Twitter, Facebook, LinkedIn, Pinterest
6. **Related posts**: 3 recent posts from the same category
7. **CTA**: Newsletter signup or "Shop Now" at the end

---

## 7. ACCESSIBILITY & TACTILE WHIMSY

A superclass theme is both universally accessible (WCAG 2.1 AA) and delightful to use. Integrate guidance from `a11y-debugging` and `agency-whimsy-injector`.

---

### 7.1 WCAG 2.1 AA Focus Trap & Keyboard Navigation

Every overlay (Cart Drawer, Mobile Navigation, Search Overlay) MUST implement an accessible focus trap and escape key listener.

**Focus Trap Function (in `assets/js/main.js`):**
```javascript
function trapFocus(modalElement) {
    const focusableEls = modalElement.querySelectorAll(
        'a[href], button:not([disabled]), textarea:not([disabled]), input[type="text"]:not([disabled]), input[type="search"]:not([disabled]), [tabindex]:not([tabindex="-1"])'
    );
    if (!focusableEls.length) return;
    const firstFocusable = focusableEls[0];
    const lastFocusable  = focusableEls[focusableEls.length - 1];

    modalElement.addEventListener('keydown', (e) => {
        if (e.key !== 'Tab') return;
        if (e.shiftKey) { // Shift + Tab
            if (document.activeElement === firstFocusable) {
                lastFocusable.focus();
                e.preventDefault();
            }
        } else { // Tab
            if (document.activeElement === lastFocusable) {
                firstFocusable.focus();
                e.preventDefault();
            }
        }
    });
}
```

---

### 7.2 Screen Reader Live Announcements (`aria-live`)

When products are added or removed from the cart via AJAX, assistive technologies must be notified without a page reload.

**Markup (`template-parts/ui/live-region.php` included in `footer.php`):**
```html
<div id="a11y-live-status" class="sr-only" aria-live="polite" aria-atomic="true"></div>
```

**JavaScript Announcer:**
```javascript
function announceToScreenReader(message) {
    const region = document.getElementById('a11y-live-status');
    if (!region) return;
    region.textContent = '';
    setTimeout(() => { region.textContent = message; }, 50);
}
```

---

### 7.3 Tactile Whimsy & Micro-Interactions (`agency-whimsy-injector`)

Subtle, high-performance CSS micro-interactions elevate the user's emotional connection to the brand:

1. **Cart Counter Pulse**:
```css
@keyframes cartBadgePop {
    0% { transform: scale(1); }
    50% { transform: scale(1.35); }
    100% { transform: scale(1); }
}
.cart-count.pop {
    animation: cartBadgePop 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
```

2. **Magnetic Button Hover Lift**:
```css
.btn-primary, .btn-secondary {
    transition: transform var(--transition-fast), box-shadow var(--transition-fast), background-color var(--transition-fast);
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px -4px rgba(0, 0, 0, 0.18);
}
.btn-primary:active {
    transform: translateY(0);
    box-shadow: 0 2px 6px -1px rgba(0, 0, 0, 0.12);
}
```

3. **Interactive Marquee Pause**:
```css
.trust-marquee-track:hover {
    animation-play-state: paused;
}
```

---

## 8. SEO IMPLEMENTATION (CRITICAL PRIORITY)

SEO is a fundamental priority. Every page must be fully optimized.

### 8.1 Create `inc/seo.php`
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
        'logo' => 'https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-blue.png',
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
        $faq_items = [];
        // Parse <details> / <summary> pairs from page content
        $content = get_the_content();
        preg_match_all('/<details[^>]*>.*?<summary[^>]*>(.*?)<\/summary>(.*?)<\/details>/s', $content, $matches, PREG_SET_ORDER);
        foreach ($matches as $match) {
            $question = wp_strip_all_tags($match[1]);
            $answer   = wp_strip_all_tags($match[2]);
            if ($question && $answer) {
                $faq_items[] = [
                    '@type' => 'Question',
                    'name'  => $question,
                    'acceptedAnswer' => [
                        '@type' => 'Answer',
                        'text'  => wp_trim_words($answer, 50),
                    ],
                ];
            }
        }
        if (!empty($faq_items)) {
            $schema[] = [
                '@context' => 'https://schema.org',
                '@type' => 'FAQPage',
                'mainEntity' => $faq_items,
            ];
        }
    }

    // Output
    foreach ($schema as $s) {
        $s = array_filter($s); // Remove nulls
        echo '<script type="application/ld+json">' . wp_json_encode($s, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . '</script>' . "\n";
    }
});
```

### 8.2 Additional SEO Requirements
- Every page template must have exactly ONE `<h1>` tag
- Use semantic HTML: `<header>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<nav>`
- All images must have descriptive `alt` attributes
- Internal linking between pages
- Breadcrumb navigation on all non-homepage pages
- XML sitemap (WooCommerce provides this, ensure it's active)

---

## 9. PERFORMANCE OPTIMIZATION (CRITICAL — targets 90+ PageSpeed)

### 9.1 Create `inc/performance.php`

```php
<?php
// Preconnect to external origins
add_action('wp_head', function() {
    echo '<link rel="preconnect" href="https://fonts.googleapis.com">' . "\n";
    echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
    echo '<link rel="preconnect" href="https://images.unsplash.com">' . "\n";
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

### 9.2 Critical CSS
- Extract above-the-fold CSS into `assets/css/critical.css`
- Inline it in `header.php` inside a `<style>` tag
- Load the full stylesheet with `media="print" onload="this.media='all'"`

### 9.3 Image Optimization
- Use `srcset` and `sizes` attributes on all images
- Use WebP format where possible
- Unsplash images: append `&w=800&q=80&fm=webp` for optimized delivery
- Set explicit `width` and `height` on images to prevent CLS

### 9.4 Animation Strategy (NO HEAVY JS LIBRARIES)
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
## 10. CART MODES & DYNAMIC FREE SHIPPING DRAWER

Both modes must ALWAYS be built. The active mode is controlled via the WordPress Customizer.

### 10.1 Customizer Option (`inc/customizer.php`)
```php
add_action('customize_register', function($wp_customize) {
    $wp_customize->add_section('theme_cart_settings', [
        'title' => 'Cart & Checkout Settings',
        'priority' => 30,
    ]);

    // Cart Mode Toggle
    $wp_customize->add_setting('cart_display_mode', [
        'default' => 'drawer',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('cart_display_mode', [
        'label' => 'Cart Display Mode',
        'section' => 'theme_cart_settings',
        'type' => 'select',
        'choices' => [
            'drawer' => 'Sidebar Drawer (High-Converting AJAX)',
            'full_page' => 'Full Page Cart',
        ],
    ]);

    // Free Shipping Threshold
    $wp_customize->add_setting('free_shipping_threshold', [
        'default' => 75,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('free_shipping_threshold', [
        'label' => 'Free Shipping Threshold ($)',
        'section' => 'theme_cart_settings',
        'type' => 'number',
        'description' => 'Enter the dollar amount required for free shipping (0 to disable).',
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

---

### 10.2 Dynamic AJAX Drawer Cart with Free Shipping Progress Bar

The superclass drawer slides in smoothly from the right, locks body scroll, traps keyboard focus, and updates shipping thresholds in real time.

**Full `cart-drawer.js` implementation (`assets/js/cart-drawer.js`):**

```javascript
/**
 * Beeclue Superclass Theme — AJAX Cart Drawer
 * Features: Free Shipping Meter, Accessible Focus Trap, Debounced Steppers, Screen-Reader Alerts
 */
document.addEventListener('DOMContentLoaded', () => {
    const drawer     = document.getElementById('cart-drawer');
    const toggle     = document.getElementById('cart-toggle');
    const closeBtn   = document.getElementById('cart-drawer-close');
    const backdrop   = drawer?.querySelector('.cart-drawer-backdrop');
    const list       = document.getElementById('cart-drawer-items');
    const subtotal   = document.getElementById('cart-drawer-subtotal');
    const count      = document.querySelector('.cart-count');
    const shipText   = document.getElementById('shipping-progress-text');
    const shipFill   = document.getElementById('shipping-progress-fill');
    const shipWrap   = document.getElementById('cart-shipping-threshold');

    if (!drawer || !toggle) return;

    /* ── Open / Close with Focus Trap & Body Lock ── */
    const open = () => {
        drawer.classList.add('open');
        drawer.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        if (typeof trapFocus === 'function') trapFocus(drawer);
        loadCart();
    };

    const close = () => {
        drawer.classList.remove('open');
        drawer.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        toggle.focus(); // Restore focus to trigger
    };

    toggle.addEventListener('click', (e) => {
        e.preventDefault();
        drawer.classList.contains('open') ? close() : open();
    });

    closeBtn?.addEventListener('click', close);
    backdrop?.addEventListener('click', close);
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && drawer.classList.contains('open')) close();
    });

    /* ── Load Cart via AJAX ───────────────────────── */
    function loadCart() {
        fetch(themeCart.ajaxUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: `action=theme_get_cart&nonce=${themeCart.nonce}`,
        })
        .then(r => r.json())
        .then(data => {
            if (!data.success) return;
            if (list) list.innerHTML = data.data.html;
            if (subtotal) subtotal.innerHTML = data.data.subtotal;
            if (count) count.textContent = data.data.count;

            updateShippingMeter(data.data.subtotal_raw, data.data.threshold);
            bindQuantityEvents();
        });
    }

    /* ── Dynamic Shipping Threshold Meter ────────── */
    function updateShippingMeter(cartSubtotal, threshold) {
        if (!shipText || !shipFill || !threshold || threshold <= 0) {
            if (shipWrap) shipWrap.style.display = 'none';
            return;
        }
        if (shipWrap) shipWrap.style.display = 'block';

        const remaining = threshold - cartSubtotal;
        const percentage = Math.min(100, Math.max(0, (cartSubtotal / threshold) * 100));

        shipFill.style.width = `${percentage}%`;
        shipFill.parentElement?.setAttribute('aria-valuenow', Math.round(percentage));

        if (remaining <= 0) {
            shipText.innerHTML = '🎉 <strong>Unlocked!</strong> You have earned <strong>Free Shipping</strong>!';
            shipWrap.classList.add('threshold-reached');
        } else {
            shipText.innerHTML = `Add <strong>$${remaining.toFixed(2)}</strong> more to qualify for <strong>Free Shipping</strong>`;
            shipWrap.classList.remove('threshold-reached');
        }
    }

    /* ── Add to Cart (Intercept Button Clicks) ─────── */
    document.addEventListener('click', (e) => {
        const btn = e.target.closest('.ajax_add_to_cart, .single_add_to_cart_button, [data-product_id]');
        if (!btn || btn.closest('.cart-drawer-qty')) return;

        e.preventDefault();
        const productId = btn.dataset.product_id || btn.value;
        const qtyInput  = document.querySelector('.quantity input, input[name="quantity"]');
        const qty       = qtyInput ? parseInt(qtyInput.value, 10) : 1;

        btn.classList.add('loading');
        btn.disabled = true;

        fetch(themeCart.ajaxUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: `action=theme_add_to_cart&product_id=${productId}&quantity=${qty}&nonce=${themeCart.nonce}`,
        })
        .then(r => r.json())
        .then(data => {
            btn.classList.remove('loading');
            btn.disabled = false;
            if (data.success) {
                if (count) {
                    count.textContent = data.data.count;
                    count.classList.remove('pop');
                    void count.offsetWidth; // trigger reflow
                    count.classList.add('pop');
                }
                if (typeof announceToScreenReader === 'function') {
                    announceToScreenReader('Item successfully added to cart.');
                }
                open();
            }
        });
    });

    /* ── Debounced Quantity Steppers ──────────────── */
    function bindQuantityEvents() {
        list?.querySelectorAll('.cart-drawer-qty-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const input   = btn.closest('.cart-drawer-qty')?.querySelector('input');
                const cartKey = input?.dataset.cartKey;
                const val     = parseInt(input.value, 10);
                const delta   = btn.dataset.action === 'plus' ? 1 : -1;
                const newVal  = Math.max(1, val + delta);

                input.value = newVal;
                updateItem(cartKey, newVal);
            });
        });

        list?.querySelectorAll('.cart-drawer-qty input').forEach(input => {
            input.addEventListener('change', () => {
                updateItem(input.dataset.cartKey, Math.max(1, parseInt(input.value, 10) || 1));
            });
        });
    }

    function updateItem(cartKey, qty) {
        fetch(themeCart.ajaxUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: `action=theme_update_cart_item&cart_key=${cartKey}&quantity=${qty}&nonce=${themeCart.nonce}`,
        })
        .then(r => r.json())
        .then(data => {
            if (data.success) loadCart();
        });
    }

    /* ── Remove Item ──────────────────────────────── */
    list?.addEventListener('click', (e) => {
        const removeBtn = e.target.closest('.cart-drawer-remove');
        if (!removeBtn) return;
        updateItem(removeBtn.dataset.cartKey, 0);
    });

    /* ── Initial Count on Load ────────────────────── */
    fetch(themeCart.ajaxUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `action=theme_get_cart_count&nonce=${themeCart.nonce}`,
    })
    .then(r => r.json())
    .then(data => {
        if (data.success && count) count.textContent = data.data.count;
    });
});
```

**Required PHP AJAX Handlers in `functions.php`:**

```php
// Cart Drawer AJAX Handlers
add_action('wp_ajax_theme_get_cart',             'theme_ajax_get_cart');
add_action('wp_ajax_nopriv_theme_get_cart',      'theme_ajax_get_cart');
add_action('wp_ajax_theme_add_to_cart',         'theme_ajax_add_to_cart');
add_action('wp_ajax_nopriv_theme_add_to_cart',  'theme_ajax_add_to_cart');
add_action('wp_ajax_theme_update_cart_item',     'theme_ajax_update_cart_item');
add_action('wp_ajax_nopriv_theme_update_cart_item','theme_ajax_update_cart_item');
add_action('wp_ajax_theme_get_cart_count',      'theme_ajax_get_cart_count');
add_action('wp_ajax_nopriv_theme_get_cart_count','theme_ajax_get_cart_count');

function theme_ajax_get_cart() {
    check_ajax_referer('theme-cart-nonce', 'nonce');
    $cart       = WC()->cart;
    $items      = $cart->get_cart();
    $subtotal   = (float) $cart->get_subtotal();
    $threshold  = (float) get_theme_mod('free_shipping_threshold', 75);
    $html       = '';

    foreach ($items as $key => $item) {
        $product = $item['data'];
        $html   .= '<div class="cart-drawer-item" data-key="' . esc_attr($key) . '">';
        $html   .= '<img src="' . wp_get_attachment_url($product->get_image_id()) . '" alt="' . esc_attr($product->get_name()) . '" width="64" height="64" loading="lazy">';
        $html   .= '<div class="cart-drawer-item-info">';
        $html   .= '<span class="cart-drawer-item-name">' . esc_html($product->get_name()) . '</span>';
        $html   .= '<div class="cart-drawer-qty">';
        $html   .= '<button type="button" class="cart-drawer-qty-btn" data-action="minus" aria-label="Decrease quantity">−</button>';
        $html   .= '<input type="number" value="' . esc_attr($item['quantity']) . '" min="1" data-cart-key="' . esc_attr($key) . '" aria-label="Quantity">';
        $html   .= '<button type="button" class="cart-drawer-qty-btn" data-action="plus" aria-label="Increase quantity">+</button>';
        $html   .= '</div>';
        $html   .= '</div>';
        $html   .= '<span class="cart-drawer-item-price">' . wp_kses_post(WC()->cart->get_product_subtotal($product, $item['quantity'])) . '</span>';
        $html   .= '<button type="button" class="cart-drawer-remove" data-cart-key="' . esc_attr($key) . '" aria-label="Remove item">×</button>';
        $html   .= '</div>';
    }

    wp_send_json_success([
        'html'         => $html ?: '<div class="cart-drawer-empty"><p>Your shopping bag is empty.</p><a href="' . wc_get_page_permalink('shop') . '" class="btn btn-secondary">Explore Products</a></div>',
        'subtotal'     => wp_kses_post($cart->get_cart_subtotal()),
        'subtotal_raw' => $subtotal,
        'threshold'    => $threshold,
        'count'        => $cart->get_cart_contents_count(),
    ]);
}

function theme_ajax_add_to_cart() {
    check_ajax_referer('theme-cart-nonce', 'nonce');
    $product_id = absint($_POST['product_id'] ?? 0);
    $quantity   = absint($_POST['quantity'] ?? 1);
    if ($product_id) {
        WC()->cart->add_to_cart($product_id, $quantity);
        WC()->cart->calculate_totals();
    }
    wp_send_json_success(['count' => WC()->cart->get_cart_contents_count()]);
}

function theme_ajax_update_cart_item() {
    check_ajax_referer('theme-cart-nonce', 'nonce');
    $cart_key = sanitize_text_field($_POST['cart_key'] ?? '');
    $quantity = absint($_POST['quantity'] ?? 1);
    if ($quantity > 0) {
        WC()->cart->set_quantity($cart_key, $quantity);
    } else {
        WC()->cart->remove_cart_item($cart_key);
    }
    WC()->cart->calculate_totals();
    wp_send_json_success(['count' => WC()->cart->get_cart_contents_count()]);
}

function theme_ajax_get_cart_count() {
    check_ajax_referer('theme-cart-nonce', 'nonce');
    wp_send_json_success(['count' => WC()->cart->get_cart_contents_count()]);
}
```

**Template Part (`template-parts/cart/drawer.php`):**

```html
<div class="cart-drawer" id="cart-drawer" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Shopping Cart">
    <div class="cart-drawer-backdrop"></div>
    <div class="cart-drawer-panel">
        <div class="cart-drawer-header">
            <h3>Your Bag (<span class="cart-count">0</span>)</h3>
            <button class="cart-drawer-close" id="cart-drawer-close" aria-label="Close cart">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M18 6L6 18M6 6l12 12"/></svg>
            </button>
        </div>

        <!-- Free Shipping Progress Bar -->
        <div class="cart-shipping-threshold" id="cart-shipping-threshold">
            <div class="shipping-message">
                <span class="shipping-text" id="shipping-progress-text">Calculating shipping reward...</span>
            </div>
            <div class="shipping-progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
                <div class="shipping-progress-fill" id="shipping-progress-fill"></div>
            </div>
        </div>

        <div class="cart-drawer-items" id="cart-drawer-items"></div>

        <div class="cart-drawer-footer">
            <div class="cart-drawer-subtotal">
                <span>Subtotal</span>
                <span id="cart-drawer-subtotal">$0.00</span>
            </div>
            <a href="<?php echo wc_get_checkout_url(); ?>" class="btn btn-primary cart-drawer-checkout">Proceed to Checkout</a>
            <a href="<?php echo wc_get_cart_url(); ?>" class="cart-drawer-view-cart">View Full Cart</a>
        </div>
    </div>
</div>
```

---

### 10.3 Full Page Cart
- Standard WooCommerce cart page at `/cart/`
- Fully customized via `woocommerce.css` with 3-layer design tokens
- Features responsive 2-column layout on desktop, streamlined 1-column on mobile

---

### 10.4 Cart Toggle Logic
In `header.php`:
```php
<?php $cart_mode = get_theme_mod('cart_display_mode', 'drawer'); ?>
<a href="<?php echo ($cart_mode === 'drawer') ? '#' : wc_get_cart_url(); ?>"
   class="nav-icon-link cart-icon-wrap"
   id="cart-toggle"
   aria-label="View Shopping Cart">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18"/>
        <path d="M16 10a4 4 0 01-8 0"/>
    </svg>
    <span class="cart-count"><?php echo WC()->cart->get_cart_contents_count(); ?></span>
</a>
```

---

## 11. VERIFICATION CHECKLIST & EXECUTION ORDER

### Multi-Skill Verification Checklist

#### Functional & E-Commerce
- [ ] Theme activates without PHP errors or warnings
- [ ] Single product floating sticky add-to-cart bar triggers correctly on scroll
- [ ] Cart drawer opens/closes with backdrop-blur, updates via AJAX without page reload
- [ ] Free shipping progress bar animates accurately based on cart subtotal
- [ ] Quantity +/- steppers update subtotal and count dynamically
- [ ] Checkout page loads with streamlined form styling
- [ ] All page templates render correctly (home, about, contact, faq, 404, search, single)

#### Multi-Skill Design & Tokens (`ui-ux-pro-max` + `design-system` + `brand`)
- [ ] 3-layer CSS custom properties declared in `style.css` (primitives, semantics, components)
- [ ] Color palette sourced from verified industry harmonies with 60-30-10 ratio
- [ ] Google Fonts paired authentically according to niche guidelines
- [ ] Fluid typography clamp scales functioning seamlessly across viewport widths

#### Accessibility (`a11y-debugging` / `agency-accessibility-auditor`)
- [ ] Keyboard focus trapped inside Cart Drawer, Mobile Nav, and Search Overlay when active
- [ ] `Escape` key closes active overlays and returns focus to triggering element
- [ ] Screen-reader live region (`#a11y-live-status`) announces AJAX cart operations
- [ ] Text contrast meets WCAG 2.1 AA (4.5:1 for body text, 3:1 for headings/borders)
- [ ] Interactive touch targets are minimum 44x44px

#### Tactile Whimsy (`agency-whimsy-injector`)
- [ ] Cart badge displays tactile pop animation on addition
- [ ] CTA buttons have subtle hover lift (`translateY(-2px)`) and soft shadow expansion
- [ ] Infinite trust marquee pauses cleanly on mouse hover

#### Performance & SEO
- [ ] Google Fonts loaded with `display=swap` and preconnected
- [ ] Above-the-fold critical CSS inlined
- [ ] WordPress head bloat and jQuery Migrate removed
- [ ] Complete JSON-LD Schema on all pages (WebSite, Organization, Product, FAQPage, BreadcrumbList)
- [ ] Single `<h1>` per page and all images possess descriptive `alt` tags

#### Agency Branding
- [ ] Beeclue Tech attribution link with UTM parameters in footer (non-negotiable):
  `https://beeclue.com/?utm_source=client_site&utm_medium=footer&utm_campaign=web_design`

---

## EXECUTION ORDER

When creating a new theme, follow this exact sequence:

1. **User Discovery & Niche Alignment**: Prompt user for brand name, niche, vibe, and color preferences (Section 2.1).
2. **Pre-flight System Checks**: Check WP-CLI, WordPress core installation, and WooCommerce availability (Section 1).
3. **Multi-Skill Design Intelligence**:
   - Query `ui-ux-pro-max` for curated style, 60-30-10 palette, and typography pairing (Section 2.2).
   - Generate complete 3-layer design tokens (`references/superclass-tokens.md`).
4. **Theme Scaffolding**: Create theme directory, `template-parts/`, `assets/`, and `inc/` (Section 3).
5. **Core Files**: Construct `style.css`, `functions.php`, `header.php`, and `footer.php` with custom logo fallback (Section 4).
6. **Superclass WooCommerce Components**:
   - Build `template-parts/product/sticky-bar.php` and `single-product.js` (Section 5.1).
   - Style variant swatches, urgency badges, and product cards (Section 5.2 - 5.3).
   - Write WooCommerce style overrides in `woocommerce.css` (Section 5.4).
7. **Page Templates**: Build `template-home.php` (with 7 sections and curated Unsplash photography), `template-about.php`, `template-contact.php`, `template-faq.php` (Section 6).
8. **Accessibility & Whimsy Layer**: Implement focus traps, screen-reader live region, and micro-interactions (Section 7).
9. **SEO & Performance Modules**: Implement `inc/seo.php` (JSON-LD structured data) and `inc/performance.php` (critical CSS, preconnect) (Sections 8 & 9).
10. **Cart System**: Build Customizer options, `template-parts/cart/drawer.php`, and `cart-drawer.js` with Free Shipping threshold progress bar (Section 10).
11. **WP-CLI Deployment**:
    - Activate theme via `wp theme activate <theme-slug>`.
    - Create required pages, assign templates, and set static front page.
    - Create Primary and Footer navigation menus and assign locations (`wp menu`).
    - Import WooCommerce sample products if needed.
12. **Multi-Skill Verification**: Run through the full verification checklist (Section 11).
