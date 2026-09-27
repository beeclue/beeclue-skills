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

## 2. Responsibility Separation Matrix

| Requirement | Target Location | Rationale |
| :--- | :--- | :--- |
| **Custom Post Types (e.g. Portfolio, Showrooms)** | Must-Use Plugin (`wp-content/mu-plugins/`) | Data must remain intact if the user switches themes. |
| **Theme Design Tokens & Colors** | `style.css` + `theme.json` | Presentation layer directly bound to theme styling. |
| **Taxonomies & Custom Fields** | Plugin or ACF Pro | Data architecture belongs in persistent storage. |
| **Cart Drawer Markup & Scripts** | Theme (`template-parts/cart/drawer.php`) | Frontend UX presentation layer. |
| **Payment Gateways & Shipping Calculators** | Dedicated WooCommerce Plugins | Security, webhook handling, and compliance. |
| **Customizer Settings (Shipping Threshold)** | Theme (`inc/customizer.php`) | Theme-specific configuration options. |
| **Navigation Menus (Header, Mobile, Footers)** | WordPress Core (`Appearance > Menus`) | User independence to create, edit, nest, and rearrange menus. |
| **Blog & Article Content** | WordPress Core (`home.php`, `single.php`) | Dynamic publishing engine, categories, comments, and archives. |
| **Sidebars & Footer Widget Blocks** | WordPress Core (`Appearance > Widgets`) | Flexible content blocks managed without touching theme code. |

---

## 3. The Core WordPress Principles & Anti-Bloat Rules

1. **Never Hardcode Navigation Links or Assume Single Menus**: Navigation MUST be dynamically driven by `register_nav_menus()` and rendered via `wp_nav_menu()` with multi-level submenu dropdown support (`depth => 3`). Never assume a fixed structure; give the user 100% independence to manage menus, categories, and custom links in `wp-admin > Appearance > Menus`.
2. **Embrace Native WordPress Publishing (Blogs & Archives)**: A flagship theme is not a rigid brochure. It must support full editorial storytelling by implementing `index.php`, `home.php`, `single.php`, `archive.php`, `comments.php`, and `sidebar.php` with native pagination (`the_posts_pagination()`).
3. **Never Bundle Heavy External JS Libraries**: No GSAP, no AOS, no full jQuery UI libraries. Use pure CSS `@keyframes` and native browser `IntersectionObserver`.
4. **Never Hardcode Domain URLs**: Always use `home_url('/')`, `wc_get_cart_url()`, and `get_template_directory_uri()`.
5. **Never Output Unescaped Variables**: Always wrap dynamic output in `esc_html()`, `esc_attr()`, `esc_url()`, or `wp_kses_post()`.
6. **Support Standard Theme Capabilities**: Always declare `add_theme_support()` for `title-tag`, `post-thumbnails`, `custom-logo`, `html5`, and WooCommerce gallery tools.
