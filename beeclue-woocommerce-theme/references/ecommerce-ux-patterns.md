# Superclass WooCommerce UX & Conversion Patterns

This reference provides production-ready implementations for the high-converting e-commerce patterns that define a **Superclass WooCommerce Theme**.

---

## 1. Dynamic Free Shipping Progress Bar

### 1.1 HTML Structure (inside Cart Drawer)
```html
<div class="cart-shipping-threshold" id="cart-shipping-threshold" data-threshold="75">
    <div class="shipping-message">
        <span class="shipping-icon">🚚</span>
        <span class="shipping-text" id="shipping-progress-text">Add $25.00 more to unlock Free Shipping!</span>
    </div>
    <div class="shipping-progress-bar" role="progressbar" aria-valuenow="66" aria-valuemin="0" aria-valuemax="100">
        <div class="shipping-progress-fill" id="shipping-progress-fill" style="width: 66.6%;"></div>
    </div>
</div>
```

### 1.2 JavaScript Calculation & Celebration Logic
```javascript
function updateShippingThreshold(cartSubtotal, thresholdAmount = 75) {
    const textEl = document.getElementById('shipping-progress-text');
    const fillEl = document.getElementById('shipping-progress-fill');
    const barEl  = document.getElementById('cart-shipping-threshold');
    if (!textEl || !fillEl || !barEl) return;

    const remaining = thresholdAmount - cartSubtotal;
    const percentage = Math.min(100, Math.max(0, (cartSubtotal / thresholdAmount) * 100));

    fillEl.style.width = `${percentage}%`;
    fillEl.parentElement.setAttribute('aria-valuenow', Math.round(percentage));

    if (remaining <= 0) {
        textEl.innerHTML = '🎉 <strong>Congratulations!</strong> You have unlocked Free Shipping!';
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

```html
<div class="cart-drawer-cross-sells" id="cart-drawer-cross-sells">
    <h4 class="cross-sells-title">Complete Your Order</h4>
    <div class="cross-sell-items">
        <div class="cross-sell-card" data-product-id="123">
            <img src="/path/to/thumb.jpg" alt="Organic Cotton Tote" width="48" height="48" loading="lazy">
            <div class="cross-sell-info">
                <span class="cross-sell-name">Organic Cotton Tote</span>
                <span class="cross-sell-price">$12.00</span>
            </div>
            <button class="btn-cross-sell-add" data-product-id="123" aria-label="Add Organic Cotton Tote to cart">
                + Add
            </button>
        </div>
    </div>
</div>
```

---

## 3. Floating Sticky Add-to-Cart Bar (Single Product)

### 3.1 HTML Markup (placed in `single-product.php` or `template-parts/product/sticky-bar.php`)
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
                <h4 class="sticky-bar-title"><?php echo esc_html($product->get_name()); ?></h4>
                <span class="sticky-bar-price"><?php echo $product->get_price_html(); ?></span>
            </div>
        </div>
        <div class="sticky-bar-action">
            <button type="button" class="btn btn-primary sticky-bar-btn" id="sticky-bar-buy-btn">
                Add to Cart
            </button>
        </div>
    </div>
</div>
```

### 3.2 Sticky Bar Observer (JS)
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const stickyBar = document.getElementById('product-sticky-bar');
    const mainCta   = document.querySelector('.single_add_to_cart_button');
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
        mainCta.click(); // Trigger native WooCommerce form submission or AJAX handler
    });
});
```

---

## 4. Visual Variant Swatches (Color & Size Pills)

Replaces native `<select>` dropdowns with accessible, visual swatch buttons:

```html
<div class="swatch-group" role="radiogroup" aria-label="Color">
    <button type="button" class="swatch-item swatch-color active" style="--swatch-hex: #1B365D;" data-value="navy" role="radio" aria-checked="true" aria-label="Navy"></button>
    <button type="button" class="swatch-item swatch-color" style="--swatch-hex: #C8602A;" data-value="terracotta" role="radio" aria-checked="false" aria-label="Terracotta"></button>
    <button type="button" class="swatch-item swatch-color" style="--swatch-hex: #F7F3EE;" data-value="cream" role="radio" aria-checked="false" aria-label="Cream"></button>
</div>

<div class="swatch-group" role="radiogroup" aria-label="Size">
    <button type="button" class="swatch-item swatch-pill" data-value="s" role="radio" aria-checked="false">S</button>
    <button type="button" class="swatch-item swatch-pill active" data-value="m" role="radio" aria-checked="true">M</button>
    <button type="button" class="swatch-item swatch-pill" data-value="l" role="radio" aria-checked="false">L</button>
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
