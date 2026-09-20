# Superclass Shopify OS 2.0 UX & Conversion Patterns

This reference provides production-ready implementations for the high-converting e-commerce patterns that define a **Superclass Shopify Theme**.

---

## 1. Dynamic Free Shipping Progress Bar

### 1.1 Liquid Markup (inside `sections/cart-drawer.liquid`)
```liquid
{%- assign threshold = settings.free_shipping_threshold | default: 75 -%}
{%- assign current_subtotal = cart.total_price | divided_by: 100.00 -%}
{%- assign remaining = threshold | minus: current_subtotal -%}
{%- assign percent = current_subtotal | times: 100.00 | divided_by: threshold | at_most: 100 -%}

<div class="cart-shipping-threshold{% if remaining <= 0 %} threshold-reached{% endif %}" id="cart-shipping-threshold" data-threshold="{{ threshold }}">
  <div class="shipping-message">
    <span class="shipping-icon">🚚</span>
    <span class="shipping-text" id="shipping-progress-text">
      {%- if remaining <= 0 -%}
        🎉 <strong>Unlocked!</strong> You have earned <strong>Free Shipping</strong>!
      {%- else -%}
        Add <strong>${{ remaining | times: 100 | money_without_currency }}</strong> more to unlock <strong>Free Shipping</strong>!
      {%- endif -%}
    </span>
  </div>
  <div class="shipping-progress-bar" role="progressbar" aria-valuenow="{{ percent | round }}" aria-valuemin="0" aria-valuemax="100">
    <div class="shipping-progress-fill" id="shipping-progress-fill" style="width: {{ percent }}%;"></div>
  </div>
</div>
```

### 1.2 JavaScript Calculation & Dynamic Updates
```javascript
function updateShippingThreshold(cartSubtotalInCents, thresholdAmountInDollars = 75) {
  const textEl = document.getElementById('shipping-progress-text');
  const fillEl = document.getElementById('shipping-progress-fill');
  const barEl  = document.getElementById('cart-shipping-threshold');
  if (!textEl || !fillEl || !barEl || !thresholdAmountInDollars) return;

  const currentSubtotal = cartSubtotalInCents / 100;
  const remaining = thresholdAmountInDollars - currentSubtotal;
  const percentage = Math.min(100, Math.max(0, (currentSubtotal / thresholdAmountInDollars) * 100));

  fillEl.style.width = `${percentage}%`;
  fillEl.parentElement.setAttribute('aria-valuenow', Math.round(percentage));

  if (remaining <= 0) {
    textEl.innerHTML = '🎉 <strong>Unlocked!</strong> You have earned <strong>Free Shipping</strong>!';
    barEl.classList.add('threshold-reached');
  } else {
    textEl.innerHTML = `Add <strong>$${remaining.toFixed(2)}</strong> more for <strong>Free Shipping</strong>`;
    barEl.classList.remove('threshold-reached');
  }
}
```

---

## 2. In-Drawer One-Click Cross-Sells

Display 1 to 3 curated impulse-buy accessories (e.g., travel cases, care kits, mystery add-ons) directly inside the drawer cart:

```liquid
{%- if settings.cart_cross_sell_collection != blank -%}
  <div class="cart-drawer-cross-sells">
    <h4 class="cross-sells-title">Complete Your Order</h4>
    <div class="cross-sell-items">
      {%- for product in collections[settings.cart_cross_sell_collection].products limit: 3 -%}
        <div class="cross-sell-card" data-product-id="{{ product.id }}">
          {{ product.featured_image | image_url: width: 96 | image_tag: loading: 'lazy', class: 'cross-sell-thumb' }}
          <div class="cross-sell-info">
            <span class="cross-sell-name">{{ product.title | escape }}</span>
            <span class="cross-sell-price">{{ product.price | money }}</span>
          </div>
          <button type="button" class="btn-cross-sell-add" onclick="addToCart({{ product.selected_or_first_available_variant.id }})" aria-label="Add {{ product.title | escape }} to bag">
            + Add
          </button>
        </div>
      {%- endfor -%}
    </div>
  </div>
{%- endif -%}
```

---

## 3. Floating Sticky Add-to-Cart Bar (Single Product)

### 3.1 Liquid Markup (`sections/product-sticky-bar.liquid`)
```liquid
<div class="product-sticky-bar" id="product-sticky-bar" aria-hidden="true">
  <div class="sticky-bar-container">
    <div class="sticky-bar-product">
      {{ product.featured_image | image_url: width: 100 | image_tag: loading: 'lazy', class: 'sticky-bar-thumb' }}
      <div class="sticky-bar-meta">
        <h4 class="sticky-bar-title">{{ product.title | escape }}</h4>
        <span class="sticky-bar-price">{{ product.selected_or_first_available_variant.price | money }}</span>
      </div>
    </div>
    <div class="sticky-bar-action">
      <button type="button" class="btn btn-primary sticky-bar-btn" id="sticky-bar-buy-btn">
        {{ 'products.product.add_to_cart' | t | default: 'Add to Bag' }}
      </button>
    </div>
  </div>
</div>
```

### 3.2 Sticky Bar Observer (`assets/product-form.js`)
```javascript
document.addEventListener('DOMContentLoaded', () => {
  const stickyBar = document.getElementById('product-sticky-bar');
  const mainCta   = document.querySelector('.product-form-submit') || document.querySelector('[name="add"]');
  const buyBtn    = document.getElementById('sticky-bar-buy-btn');

  if (!stickyBar || !mainCta) return;

  const observer = new IntersectionObserver(([entry]) => {
    // Show sticky bar when main add-to-cart button scrolls out of view
    const isHidden = entry.isIntersecting;
    stickyBar.classList.toggle('active', !isHidden);
    stickyBar.setAttribute('aria-hidden', isHidden ? 'true' : 'false');
  }, { threshold: 0, rootMargin: '-80px 0px 0px 0px' });

  observer.observe(mainCta);

  buyBtn?.addEventListener('click', () => {
    mainCta.click(); // Trigger native product form submission or AJAX handler
  });
});
```

---

## 4. Visual Variant Swatches (Color & Size Pills)

Replaces native `<select>` dropdowns with accessible, visual swatch buttons:

```liquid
<div class="swatch-group" role="radiogroup" aria-label="{{ option.name | escape }}">
  {%- for value in option.values -%}
    <input type="radio" id="Option-{{ option.position }}-{{ forloop.index }}"
           name="{{ option.name | escape }}" value="{{ value | escape }}"
           {% if option.selected_value == value %}checked{% endif %} class="swatch-input visually-hidden">
    <label for="Option-{{ option.position }}-{{ forloop.index }}" class="swatch-pill swatch-{{ option.name | handle }}">
      {{ value }}
    </label>
  {%- endfor -%}
</div>
```

---

## 5. WCAG 2.1 AA Focus Trap & Live Region

```javascript
/**
 * Accessible Focus Trap for Drawers & Modals
 */
function trapFocus(element) {
  const focusableEls = element.querySelectorAll('a[href], button:not([disabled]), textarea:not([disabled]), input[type="text"]:not([disabled]), input[type="radio"]:not([disabled]), input[type="checkbox"]:not([disabled]), [tabindex]:not([tabindex="-1"])');
  const firstFocusable = focusableEls[0];
  const lastFocusable  = focusableEls[focusableEls.length - 1];

  element.addEventListener('keydown', (e) => {
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

  firstFocusable?.focus();
}

/**
 * Screen Reader Live Status Announcement
 */
function announceToScreenReader(message) {
  let liveRegion = document.getElementById('a11y-live-status');
  if (!liveRegion) {
    liveRegion = document.createElement('div');
    liveRegion.id = 'a11y-live-status';
    liveRegion.className = 'sr-only';
    liveRegion.setAttribute('aria-live', 'polite');
    liveRegion.setAttribute('aria-atomic', 'true');
    document.body.appendChild(liveRegion);
  }
  liveRegion.textContent = '';
  setTimeout(() => {
    liveRegion.textContent = message;
  }, 50);
}
```
