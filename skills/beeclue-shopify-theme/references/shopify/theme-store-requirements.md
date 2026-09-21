# Shopify Theme Store Requirements Specification

> Source: [Shopify Theme Store Requirements](https://shopify.dev/docs/storefronts/themes/store/requirements)  
> Standard: Official Shopify Theme Review & Certification Guidelines

This document details the mandatory requirements that every Shopify theme developed by agents must fulfill to guarantee complete compliance with the Shopify Theme Store standards.

---

## 1. Theme Store Exclusivity & Attribution Standards

Themes intended for the Shopify Theme Store must adhere to strict exclusivity and attribution rules:

- **Exclusivity**: Themes submitted to the Shopify Theme Store can only be distributed through the Shopify Theme Store (not distributed on ThemeForest, Creative Market, or other third-party marketplaces).
- **Prohibition of Designer Credits**: Themes submitted to the Shopify Theme Store **CANNOT contain designer credits** (such as a link to a theme developer's website) or affiliate links in the theme files.
- **Unaltered `powered_by_link`**: The `{{ powered_by_link }}` object in `sections/footer.liquid` must not be altered, stripped, or hardcoded. It must output exactly `{{ powered_by_link }}`.
- **Dual-Mode Operating Model**:
  1. **Theme Store Submission Mode** (`submission_mode: true`):
     - Zero external agency links or designer credits in footer or anywhere in the code.
     - Pure `{{ powered_by_link }}`.
     - Zero affiliate parameters or third-party marketing tags.
  2. **Agency Client Mode** (Custom bespoke merchant builds):
     - Configurable setting in `settings_schema.json` allowing the merchant or agency to toggle agency attribution:
     ```liquid
     {%- if settings.show_agency_credit -%}
       <span class="site-footer__credit">Website Designed & Developed by <a href="https://beeclue.com/?utm_source=client_site&utm_medium=footer&utm_campaign=shopify_theme_credit" target="_blank" rel="noopener noreferrer">Beeclue Tech</a></span>
     {%- else -%}
       <span class="site-footer__powered">{{ powered_by_link }}</span>
     {%- endif -%}
     ```

---

## 2. Uniqueness from Other Themes

- **Original Architecture**: Themes must be built with fully original code or based on [Shopify's Skeleton Theme](https://github.com/shopify/skeleton-theme). New submissions built on or derived from Dawn or Horizon are **not eligible** for the Shopify Theme Store.
- **Structural Differentiation**: Distinct header, navigation drawer, product card systems, media treatments, and layout grids. Superficial tweaks (color changes, font swaps, minor spacing tweaks) do not qualify as unique.

---

## 3. Theme Design & UX Requirements

- **Visual Art Direction**: Unique, intentional design targeting a specific merchant industry or catalog size. Professional visuals, no blurry/clipart imagery.
- **Complementary Color Palette**: Minimum 4 colors. Every background color setting must have a paired foreground color setting.
- **Organized Page Structure**: Clear visual hierarchy, deliberate spacing scales, flexible layouts that do not break when titles, descriptions, or media quantities vary.
- **Typography Pairing**: Clean font pairing using Shopify's native `font_picker` (no custom `@font-face` external files).
- **Frictionless Shopping**: Clear navigation from home page to collection, product discovery, PDP, cart drawer/page, and checkout.

---

## 4. Mandatory Storefront Features

All themes must natively support the following features:

### 4.1 Sections Everywhere (OS 2.0)
- All templates (except checkout, gift card, customer account) must be JSON templates (`templates/*.json`).

### 4.2 Discounts Display
- Display discount amounts for individual items (`line_item.original_price` vs `line_item.final_price`, `line_item.discount_allocations`) and entire cart orders (`cart.total_discount`, `cart.cart_level_discount_applications`) on Cart page and Cart drawer.

### 4.3 Accelerated Checkout Buttons
- Render `{{ form | payment_button }}` inside the product form on PDP.
- Support accelerated checkout buttons on Cart page (`content_for_additional_checkout_buttons`).
- **CRITICAL**: Branded dynamic checkout button styles and colors must **NOT** be overridden or styled with custom CSS.

### 4.4 Faceted Collection & Search Filtering
- Support native Storefront Filtering on `collection.json` and `search.json` using `collection.filters` / `search.filters`.
- Support filtering by availability, price range, product type, vendor, and variant options.
- Render active filter chips with individual clear links and a "Clear all" action.

### 4.5 Gift Card Page & Recipient Form
- Provide `templates/gift_card.liquid`.
- Support Apple Wallet pass (`gift_card.pass_url`).
- Display gift card code and QR code (minimum 120px × 120px).
- Include logo or `shop.name`.
- On PDP for gift card products, include the recipient form:
  ```liquid
  {%- if product.gift_card? -%}
    {%- render 'gift-card-recipient-form', product: product, form: form -%}
  {%- endif -%}
  ```
  Supporting fields: `form.email`, `form.name`, `form.message`, and `send_on`.

### 4.6 Image Focal Points & Social Sharing
- Support image focal points in image tags:
  ```liquid
  {{ image | image_url: width: 1200 | image_tag:
    loading: 'lazy',
    sizes: '100vw',
    widths: '375, 550, 750, 1100, 1500, 2000',
    style: image.presentation.focal_point ? 'object-position: ' | append: image.presentation.focal_point : nil
  }}
  ```
- Include `page_image` for Open Graph and Twitter Card tags in `snippets/social-meta-tags.liquid`.

### 4.7 Country & Language Selectors (Shopify Markets)
- Include localized country/region and currency selector using `localization.available_countries` inside a form using `routes.root_url`.
- Include language selector using `localization.available_languages`.
- Follow official Shopify country/language UX guidelines (visible disclosure modal/drawer).

### 4.8 Multi-Level Menus
- Support nested navigation (`link.links` and `childlink.links`) up to 3 levels in header mega-menus and mobile navigation drawers.

### 4.9 Newsletter Forms
- Native customer signup form:
  ```liquid
  {% form 'customer', class: 'newsletter-form' %}
    <input type="hidden" name="contact[tags]" value="newsletter">
    <input type="email" name="contact[email]" id="NewsletterEmail-{{ section.id }}" required ...>
    <label for="NewsletterEmail-{{ section.id }}">Email address</label>
    <button type="submit">Subscribe</button>
  {% endform %}
  ```

### 4.10 Local Pickup Availability
- Include the `pickup-availability` block/snippet on PDP:
  ```liquid
  {%- assign pick_up_availabilities = product.selected_or_first_available_variant.store_availabilities | where: 'pick_up_enabled', true -%}
  ```
  Renders pickup status without requiring the customer to add the item to cart.

### 4.11 Product Recommendations
- Dynamic related recommendations section using `routes.product_recommendations_url` (`recommendations.products`).
- Complementary product recommendations block/section using `recommendations.intent == 'complementary'`.

### 4.12 Rich Product Media
- Handle `model` (3D AR with `<model-viewer>`), `video`, `external_video` (YouTube/Vimeo), and `image` using `{{ media | media_tag }}` or custom wrappers on PDP and Quick View.

### 4.13 Search & Predictive Search
- Include `templates/search.json`.
- Implement live predictive search using the Shopify Predictive Search API (`/search/suggest.json` or section rendering query).
- Return products, articles, and pages with `item.object_type`.

### 4.14 Selling Plans & Subscriptions
- Display subscription selling plan selector on PDP (`variant.selling_plan_allocations`).
- Display selected selling plan in cart line items (`item.selling_plan_allocation`).

### 4.15 Shop Pay Installments
- Include Shop Pay Installments banner on PDP inside the product form:
  ```liquid
  {{ form | payment_terms }}
  ```

### 4.16 Unit Pricing
- Display unit price (`variant.unit_price` and `variant.unit_price_measurement`) when present on:
  1. Product page (PDP)
  2. Collection page (product card)
  3. Cart page and Cart drawer

### 4.17 Variant Swatches
- Support native Shopify Swatches using `option_value.swatch.image` and `option_value.swatch.color`.
- Fall back gracefully to hex colors or text pills.

### 4.18 Follow on Shop
- Render the Follow on Shop button using the `login_button` Liquid filter:
  ```liquid
  {{ shop | login_button: action: 'follow' }}
  ```
- Unaltered branded button colors.

### 4.19 Account Component
- Include the `<shopify-account>` Web Component in both the **desktop** and **mobile** header for instant sign-in and account access:
  ```html
  <shopify-account></shopify-account>
  ```

---

## 5. Templates, Sections, & Blocks Architecture

### 5.1 Mandatory Template Inventory
Every theme must include the following files:
```text
layout/
  └── theme.liquid
templates/
  ├── 404.json
  ├── article.json
  ├── blog.json
  ├── cart.json
  ├── collection.json
  ├── gift_card.liquid
  ├── index.json
  ├── list-collections.json
  ├── page.contact.json
  ├── page.json
  ├── password.json
  ├── product.json
  └── search.json
config/
  ├── settings_data.json
  └── settings_schema.json
```
*Note: Never include `config/markets.json` when submitting a theme.*

### 5.2 Section Groups
Header and footer must use OS 2.0 Section Groups:
- `sections/header-group.json`
- `sections/footer-group.json`

Rendered in `layout/theme.liquid`:
```liquid
{% sections 'header-group' %}
<main id="MainContent" role="main">
  {{ content_for_layout }}
</main>
{% sections 'footer-group' %}
```

### 5.3 Custom Liquid Section & Block
- Must include a `sections/custom-liquid.liquid` section with a setting of `type: "liquid"`, available on all JSON templates.
- Must include a Custom Liquid block (`type: "liquid"`) in `sections/main-product.liquid` and `sections/featured-product.liquid`.

### 5.4 App Blocks (`@app`)
- The main product section (`sections/main-product.liquid`) and featured product section (`sections/featured-product.liquid`) must declare and render `@app` blocks:
```liquid
{%- when '@app' -%}
  {% render block %}
```

### 5.5 Granular Modular Product Blocks
All elements in `sections/main-product.liquid` must be individual blocks in schema:
- `title`
- `price`
- `vendor`
- `description`
- `variant_picker`
- `buy_buttons`
- `share`
- `collapsible_tab`
- `pickup_availability`
- `custom_liquid`
- `@app`

---

## 6. Lighthouse Performance & Accessibility Standards

- **Lighthouse Performance Score**: Minimum average **60+** across PDP, Collection, and Home Page (Desktop and Mobile) using standard benchmark datasets.
- **Lighthouse Accessibility Score**: Minimum average **90+** across PDP, Collection, and Home Page (Desktop and Mobile).
- **Zero Empty Testing Sections**: Sections must contain realistic imagery and content when audited.

---

## 7. Page-Specific Requirements

### 7.1 Layout (`theme.liquid`)
- Dynamic language attribute: `<html lang="{{ request.locale.iso_code }}">`.
- Dynamic URLs via `routes` object only:
  - `{{ routes.root_url }}` (never `href="/"`)
  - `{{ routes.cart_url }}`
  - `{{ routes.search_url }}`
  - `{{ routes.all_products_collection_url }}`
  - `{{ routes.predictive_search_url }}`
- Never parse or modify `content_for_header`.
- Payment icons in full color via `shop.enabled_payment_types | payment_type_svg_tag`.

### 7.2 Product Page (PDP)
- Full `product.title` (untruncated).
- Price, compare-at price, unit price.
- Full description, option names and values.
- Taxes included indicator (`cart.taxes_included`).
- First available variant loaded on page (`product.selected_or_first_available_variant`).
- Quantity selector, Add to Cart button, dynamic accelerated checkout buttons.
- Client-side variant change callback updating price, compare-at price, URL, and availability.

### 7.3 Collection Page
- `collection.title` (untruncated), `collection.description`, `collection.image`.
- Product grid with untruncated titles, prices, unit prices, at least 1 piece of media.
- Layout must not break when images have varying aspect ratios.
- Sale badge when `product.compare_at_price_max > product.price`.
- Variable price indicator (`product.price_varies`).
- Sort by selector (`collection.sort_by`).
- Empty collection state message.
- Pagination or infinite scroll via `{% paginate collection.products by ... %}`.

### 7.4 Collection List Page (`list-collections.json`)
- `collection.title` (untruncated).
- `collection.featured_image` with fallback to first product's featured image.
- Pagination enabled.

### 7.5 Cart Page & Cart Drawer
- Line item details: title, unit price, featured image, final price, quantity, options with values, line-level discount allocations.
- Visible `cart.total_price`.
- Indication when taxes are included (`cart.taxes_included`).
- Cart note textarea (`cart.note`).
- Empty cart state message with link to products (`routes.all_products_collection_url`).
- Quantity increment, decrement, and removal with dynamic AJAX refresh.

### 7.6 Blog & Article Pages
- `blog.title`, `article.title` (untruncated, links to `article.url`), `article.image`.
- `article.excerpt_or_content` (not just `article.content`).
- `article.published_at` (never `article.created_at`).
- Paginated comments workflow without moderation blocking.

### 7.7 404 & Password Pages
- 404: clear message, search bar, link to home (`routes.root_url`).
- Password: store logo or `shop.name`, `shop.password_message`, storefront password entry form (`form 'storefront_password'`).

---

## 8. Theme Settings, Schema & Style Rules

### 8.1 Sentence Case & American English
All section names, preset names, setting categories, and setting labels must use **sentence case** and **American English**:
- `color` (never `colour`)
- `center`, `centered` (never `centre`)
- `catalog` (never `catalogue`)
- `customize` (never `customise`)
- `canceled` (never `cancelled`)
- `gray` (never `grey`)

### 8.2 Shopify Terminology Table
Strictly enforce official terminology in all schemas and UI:

| Use This Term | Prohibited Term |
|---|---|
| **home page** | homepage |
| **top bar** | meta-nav, search bar |
| **bottom bar** | below footer, legal |
| **slideshow** | slider |
| **checkout** | check out |
| **heading** | title |
| **subheading** | sub-heading |
| **body text** | main text |
| **signup** | sign-up, sign up |
| **favicon** | shortcut icon, website icon |
| **sidebar** | side bar |
| **button label** | button name, CTA label |
| **social media icons** | social buttons, social links |
| **navigation** | menus, menu |
| **main menu** | navigation, primary menu |
| **footer menu** | footer links |
| **cart type** | Ajax cart, Ajaxify |
| **.png** | PNG, png, .PNG |
| **use** | (for actionable options involving file upload) |
| **show** | (for show/hide visibility toggles) |
| **enable** | (for apps, plugins, or layout-modifying features) |

- **No Ampersands**: Never use `&` in settings labels or section names (use "and").
- **Declarative Statements**: Use declarative statements ("Use custom logo", not "Use custom logo?").
- **Link Lists**: Settings of type `link_list` must have `default: "main-menu"` in the header, or `default: "footer"` in the footer.
- **Theme Info**: `config/settings_schema.json` must contain a `theme_info` section:
  ```json
  {
    "name": "theme_info",
    "theme_name": "ThemeName",
    "theme_version": "1.0.0",
    "theme_author": "DeveloperName",
    "theme_documentation_url": "https://...",
    "theme_support_url": "https://..."
  }
  ```

---

## 9. Typography & Font Picker Standards

- All fonts must use `type: "font_picker"` in `settings_schema.json`.
- Must specify a valid default font from Shopify's font library:
  ```json
  {
    "type": "font_picker",
    "id": "heading_font",
    "label": "Heading font",
    "default": "assistant_n4"
  }
  ```
- CSS stylesheets must load bold, italic, and bold-italic variants using the `font_modify` filter:
  ```liquid
  {%- assign heading_font_bold = settings.heading_font | font_modify: 'weight', 'bold' -%}
  {%- assign heading_font_italic = settings.heading_font | font_modify: 'style', 'italic' -%}
  ```
- Custom font files uploaded via `@font-face` are **prohibited** for Theme Store submissions.

---

## 10. Technical Assets & Code Standards

- **No Sass**: Files with `.scss` or `.scss.liquid` are **strictly forbidden**. Only native modern CSS or `.css.liquid`.
- **No Minified Code in Source**: Unminified `.css` and `.js` files in `/assets`. Shopify CDN performs automatic minification.
- **No `robots.txt.liquid`**: Custom robots template is forbidden by Theme Store rules.
- **No Deceptive Tactics**: No fake stock counters, no fictitious countdown timers, no artificial viewer activity claims. Real event countdowns are permitted.
- **Shopify Domain Links**: Any hyperlink pointing to a `*.shopify.com` domain must include `rel="nofollow"`.
- **Protocol-Relative URLs**: External asset links must use protocol-relative syntax (`//cdn...`).
- **Touch Target Minimum**: Pointer elements must be at least 24px × 24px.
- **Color Contrast**: 4.5:1 for body text; 3:1 for large text (18pt+) and graphic elements.
