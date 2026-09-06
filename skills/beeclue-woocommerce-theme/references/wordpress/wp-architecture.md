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

---

## 3. The Anti-Bloat Rules
1. **Never Bundle Heavy External JS Libraries**: No GSAP, no AOS, no full jQuery UI libraries. Use pure CSS `@keyframes` and native browser `IntersectionObserver`.
2. **Never Hardcode Domain URLs**: Always use `home_url('/')`, `wc_get_cart_url()`, and `get_template_directory_uri()`.
3. **Never Output Unescaped Variables**: Always wrap dynamic output in `esc_html()`, `esc_attr()`, `esc_url()`, or `wp_kses_post()`.
