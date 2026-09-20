# Shopify Ajax Cart API & Section Rendering Architecture

The cart drawer is the highest-leverage conversion surface in a Shopify store. Combining the **Shopify Ajax API** with the **Section Rendering API** provides instant, app-like speed without reloading the page.

---

## 1. Shopify Ajax API Endpoints

All requests use native `fetch()` with JSON payloads and headers:

| Endpoint | Method | Purpose | Payload |
| :--- | :--- | :--- | :--- |
| `/cart.js` | `GET` | Retrieve complete current cart object | None |
| `/cart/add.js` | `POST` | Add one or multiple items to cart | `{ items: [{ id, quantity, properties }] }` |
| `/cart/change.js` | `POST` | Change quantity of an item by key or line | `{ id: lineItemKey, quantity: newQty }` |
| `/cart/update.js` | `POST` | Update cart notes or multiple line items | `{ note: '...', updates: { key: qty } }` |
| `/cart/clear.js` | `POST` | Empty entire cart | None |

---

## 2. Dynamic Section Rendering Workflow

Instead of re-rendering HTML in client-side JavaScript templates, request the pre-rendered Liquid HTML directly from Shopify servers using the `sections` parameter:

```javascript
async function addToCart(variantId, quantity = 1) {
  try {
    const response = await fetch('/cart/add.js', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        items: [{ id: variantId, quantity: quantity }],
        sections: ['cart-drawer', 'cart-icon-bubble']
      })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.description || 'Failed to add item to bag.');
    }

    // 1. Update Cart Drawer DOM
    const drawerContainer = document.getElementById('cart-drawer-container');
    if (drawerContainer && data.sections['cart-drawer']) {
      drawerContainer.innerHTML = data.sections['cart-drawer'];
    }

    // 2. Update Header Cart Bubble
    const bubbleContainer = document.getElementById('cart-icon-bubble');
    if (bubbleContainer && data.sections['cart-icon-bubble']) {
      bubbleContainer.innerHTML = data.sections['cart-icon-bubble'];
    }

    // 3. Open Drawer & Announce to Screen Readers
    const drawer = document.querySelector('cart-drawer');
    drawer?.open();

    const liveRegion = document.getElementById('a11y-live-region');
    if (liveRegion) {
      liveRegion.textContent = 'Item added to your bag. Subtotal updated.';
    }

  } catch (error) {
    console.error('Cart Error:', error);
    alert(error.message);
  }
}
```

---

## 3. Dynamic Free Shipping Progress Calculation

In `sections/cart-drawer.liquid`, Liquid renders the initial progress meter based on `settings.free_shipping_threshold` and `cart.total_price`. When quantities change via JavaScript, update the progress bar dynamically:

```javascript
function updateShippingMeter(subtotalInCents, thresholdInDollars) {
  const textEl = document.getElementById('cart-shipping-text');
  const fillEl = document.getElementById('cart-shipping-fill');
  const container = document.getElementById('cart-shipping-bar');
  if (!textEl || !fillEl || !container || !thresholdInDollars) return;

  const currentTotal = subtotalInCents / 100;
  const remaining = thresholdInDollars - currentTotal;
  const percentage = Math.min(100, Math.max(0, (currentTotal / thresholdInDollars) * 100));

  fillEl.style.width = `${percentage}%`;
  fillEl.parentElement?.setAttribute('aria-valuenow', Math.round(percentage));

  if (remaining <= 0) {
    textEl.innerHTML = '🎉 <strong>Unlocked!</strong> You have earned <strong>Free Shipping</strong>!';
    container.classList.add('threshold-reached');
  } else {
    textEl.innerHTML = `Add <strong>$${remaining.toFixed(2)}</strong> more to qualify for <strong>Free Shipping</strong>`;
    container.classList.remove('threshold-reached');
  }
}
```

---

## 4. Debounced Quantity Stepper

```javascript
let debounceTimer;
function onQuantityChange(lineItemKey, newQuantity) {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(async () => {
    const res = await fetch('/cart/change.js', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        id: lineItemKey,
        quantity: parseInt(newQuantity, 10),
        sections: ['cart-drawer', 'cart-icon-bubble']
      })
    });
    const data = await res.json();
    document.getElementById('cart-drawer-container').innerHTML = data.sections['cart-drawer'];
    document.getElementById('cart-icon-bubble').innerHTML = data.sections['cart-icon-bubble'];
  }, 250);
}
```
