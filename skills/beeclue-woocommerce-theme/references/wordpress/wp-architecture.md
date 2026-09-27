# WordPress & WooCommerce Architectural Decision Matrix

Before writing any custom PHP or JavaScript, every technical requirement must pass through the **BeeClue Architectural Decision Hierarchy**. Avoid reinventing capabilities that WordPress or WooCommerce natively provide.

---

## 1. The Architectural Decision Tree

```
Does the feature require persistent data that must survive a theme switch?
  ├── YES → Plugin Architecture (Custom Plugin, Must-Use Plugin, or CPT plugin)
  └── NO  ↓
Can WordPress Core or Block Architecture handle it natively?
  ├── YES → Core block pattern or theme.json configuration
  └── NO  ↓
Does WooCommerce Core provide standard hooks or Store API endpoints?
  ├── YES → WooCommerce filter/action hook or Store API client
  └── NO  ↓
Is it purely presentational, layout, or micro-interaction?
  └── YES → Theme template-parts/ or CSS Custom Properties
```

---

## 2. Responsibility Separation Matrix: Data Sovereignty vs. Pure Theme UI

The architecture enforces a strict divide: **WordPress / WooCommerce Core is the sole source of truth for all data**, while the **Theme is a pure UI, layout, and micro-interaction engine**. Store owners must be able to edit any text, image, category, menu, or setting in `wp-admin` and see the frontend update immediately without code changes.

| Domain | Data Source (WordPress / WC Core) | Theme UI & Presentation Responsibility |
| :--- | :--- | :--- |
| **Product Categories (`taxonomy-product_cat.php`)** | `wp-admin > Products > Categories`: Name (`single_term_title()`), Category Hero Image (`get_term_meta(..., 'thumbnail_id')`), Description (`term_description()`), Subcategories (`get_terms(parent)`). | Editorial hero banner layout, responsive image container, glassmorphic description card, child term pill navigation, catalog sorting bar. |
| **Single Product (`single-product.php`)** | `wp-admin > Products`: `WC_Product` object (Title, SKU, Price, Gallery IDs, Short/Full Description, Attributes, Stock Status, Upsells). | Bespoke gallery layout / slider, visual swatch radiogroups, sticky buy bar with scroll observer, accordion tab styling. |
| **Navigation Menus** | `wp-admin > Appearance > Menus`: `wp_nav_menu(['theme_location' => 'primary', 'depth' => 3])`. | Multi-tier typography, custom CSS rotating chevrons, elevated submenu dropdowns, sub-submenu horizontal flyouts, mobile drawer accordions. |
| **Editorial Blog & Journal** | `wp-admin > Posts`: `the_title()`, `the_post_thumbnail()`, `the_content()`, `the_category()`, `the_author_meta()`, `comments_template()`. | Asymmetric magazine split layouts, reading progress bar, drop-cap typography, custom comment list formatting, pagination. |
| **Theme Settings & UI Toggles (`inc/customizer.php`)** | `wp-admin > Appearance > Customize`: `get_theme_mod('beeclue_catalog_show_rating')`, `get_theme_mod('beeclue_single_show_reviews')`, etc. | Granular control to toggle UI components (e.g. disable reviews on grid while showing on details, toggle sticky bar, swatches, shipping bar). |
| **Footer Newsletter Module** | EmailOctopus or Mailchimp Plugins / Webhooks (`wp-admin > Settings` or Customizer) | List synchronization, double opt-in, API security. Theme provides 100% bespoke token styling, fluid input layouts, and Customizer visibility toggles. |
| **Site Chrome & Identity** | `wp-admin > Appearance > Customize`: `get_custom_logo()`, `get_bloginfo('name')`, `get_theme_mod('announcement_text')`. | Header positioning, responsive mobile drawer triggers, announcement ticker layout, sticky header blur effects. |
| **Cart Drawer & Checkout** | `WC()->cart`: Items, quantities, prices, cart subtotal, free shipping threshold calculation. | Off-canvas drawer sliding animation, progress bar fill calculation, focus trapping, swipe-to-dismiss gestures. |
| **Custom Post Types** | Must-Use Plugin (`wp-content/mu-plugins/`): CPT registration and custom taxonomy definitions. | Bespoke portfolio/showroom archive and single card template parts (`template-parts/cpt/`). |

---

## 3. The Core WordPress Principles & Anti-Bloat Rules

1. **Pure UI Architecture — Every Data Source Must Originate from WordPress / WooCommerce Core**:
   Templates must NEVER hardcode mock text, category names, category hero images, descriptions, or URLs. Every piece of visible content must originate dynamically from WordPress Core APIs, template tags, or WooCommerce object methods. When a store owner updates a category name, uploads a new category image, or writes an editorial category description in `wp-admin > Products > Categories`, the theme's bespoke UI must automatically render it.
2. **Granular UI Component Toggles via Theme Settings**:
   Every visual UI component must have an independent toggle in Theme Customizer (`inc/customizer.php`) and be wrapped in `get_theme_mod('setting_key', default)` before rendering markup. Store owners must have the freedom to enable/disable UI elements per screen (e.g. hide star rating reviews on product grid cards while displaying reviews on the single product details page).
3. **Never Hardcode Navigation Links or Assume Single Menus**:
   Navigation MUST be dynamically driven by `register_nav_menus()` and rendered via `wp_nav_menu()` with multi-level submenu dropdown support (`depth => 3`). Never assume a fixed structure; give the user 100% independence to manage menus, categories, and custom links in `wp-admin > Appearance > Menus`.
4. **Embrace Native WordPress Publishing (Blogs & Archives)**:
   A flagship theme is not a rigid brochure. It must support full editorial storytelling by implementing `index.php`, `home.php`, `single.php`, `archive.php`, `comments.php`, and `sidebar.php` with native pagination (`the_posts_pagination()`).
5. **Never Bundle Heavy External JS Libraries**:
   No GSAP, no AOS, no full jQuery UI libraries. Use pure CSS `@keyframes` and native browser `IntersectionObserver`.
6. **Never Hardcode Domain URLs**:
   Always use `home_url('/')`, `wc_get_cart_url()`, and `get_template_directory_uri()`.
7. **Never Output Unescaped Variables**:
   Always wrap dynamic output in `esc_html()`, `esc_attr()`, `esc_url()`, or `wp_kses_post()`.
8. **Support Standard Theme Capabilities**:
   Always declare `add_theme_support()` for `title-tag`, `post-thumbnails`, `custom-logo`, `html5`, and WooCommerce gallery tools.
