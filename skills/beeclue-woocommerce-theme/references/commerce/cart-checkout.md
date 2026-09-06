# Cart Drawer & High-Converting Checkout Architecture

The cart drawer is the highest-leverage conversion surface in an e-commerce storefront. It transforms purchase intent into completed orders by eliminating friction, celebrating order milestones, and surfacing relevant cross-sells.

---

## 1. The Superclass Cart Drawer Blueprint

```
┌────────────────────────────────────────────────────────┐
│  Your Bag (3)                                     [✕]  │ ← Header + Accessible Close
├────────────────────────────────────────────────────────┤
│  🚚 Add $14.00 more to unlock Free Shipping!          │ ← Dynamic Progress Bar
│  ████████████████████░░░░░░░░░░░ (78%)                 │
├────────────────────────────────────────────────────────┤
│  [Thumb]  Organic Stoneware Mug               $32.00   │ ← Cart Items
│           Terracotta / 12oz                     [×]    │
│           [−] 1 [+]                                    │
│                                                        │
│  [Thumb]  Linen Kitchen Towel                 $24.00   │
│           Natural Oat / Pair                    [×]    │
│           [−] 1 [+]                                    │
├────────────────────────────────────────────────────────┤
│  Complete Your Order:                                  │ ← In-Drawer Cross-Sells
│  [Thumb]  Natural Beeswax Candle             +$18.00   │
│           [+ Add to Bag]                               │
├────────────────────────────────────────────────────────┤
│  Subtotal                                     $56.00   │ ← Footer & CTA
│  Taxes & shipping calculated at checkout               │
│  [ Proceed to Checkout → ]                             │
│  [ View Full Cart ]                                    │
└────────────────────────────────────────────────────────┘
```

---

## 2. Dynamic Free Shipping Progress Bar

### 2.1 Technical Operation
- The shipping threshold is read dynamically from the WordPress Customizer setting `free_shipping_threshold`.
- Whenever an item is added, removed, or quantity altered via AJAX:
  1. The new subtotal is calculated.
  2. Remaining balance is evaluated: `remaining = threshold - subtotal`.
  3. Percentage is updated: `percentage = Math.min(100, Math.max(0, (subtotal / threshold) * 100))`.
  4. If `remaining <= 0`, celebrate: bar adds `.threshold-reached`, progress fill expands to 100%, and text updates to: *"🎉 Congratulations! You have unlocked Free Shipping!"*

---

## 3. In-Drawer One-Click Cross-Sells

- **Curated Logic**: Cross-sells must NOT be random products. They must be low-friction impulse accessories (travel cases, care balms, cleaning brushes, mystery add-ons).
- **Price Anchor**: Cross-sell items should be priced under 35% of store AOV to facilitate frictionless addition.
- **AJAX Addition**: Clicking `+ Add` immediately dispatches an AJAX request, re-renders the cart drawer, updates the subtotal, and advances the free shipping bar without page refresh.

---

## 4. Debounced Quantity Steppers

- Prevents rapid server hammering when a user clicks `+` multiple times in succession.
- Local DOM quantity updates immediately for instant tactile response.
- Background AJAX call is debounced by 250ms to dispatch the final consolidated quantity to WooCommerce Store API or `admin-ajax.php`.
