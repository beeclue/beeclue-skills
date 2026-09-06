# BeeClue Commerce MCP Specification

The **BeeClue Commerce MCP** provides tools for inspecting stores, auditing product data, and validating WooCommerce template execution.

---

## 1. Tool Interfaces

### `inspect_store()`
- **Returns**: Store active plugins, WooCommerce version, active theme, currency, and tax/shipping configurations.

### `inspect_products(limit, category)`
- **Parameters**: `limit` (int, default 10), `category` (string, optional).
- **Returns**: Product array with IDs, names, SKUs, prices, stock status, variations, and image URLs.

### `validate_product_template(template_path)`
- **Parameters**: `template_path` (string).
- **Returns**: Validates presence of sticky Add-to-Cart bar markup, variant swatches, schema tags, and WCAG accessibility attributes.

### `validate_cart()`
- **Returns**: Validates AJAX cart endpoints, free shipping threshold calculation, debounced steppers, and focus trap.

### `validate_checkout()`
- **Returns**: Evaluates checkout form field efficiency, payment gateway integrations, and order review card layout.
