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

---

## 5. Selectable Checkout Architecture & Theming

The checkout page is the ultimate conversion bottleneck. Rather than locking the store into a single rigid flow, BeeClue themes empower store owners to select from **3 proven checkout styles** directly in **Theme Settings (`inc/customizer.php`)**, plus an optional **Distraction-Free Enclosed Chrome** mode.

```
                    ┌───────────────────────────────────────────────┐
                    │  Appearance > Customize > Checkout Experience │
                    └───────────────────────┬───────────────────────┘
                                            │
               ┌────────────────────────────┼───────────────────────────┐
               ▼                            ▼                           ▼
   [1. Split-Screen Single]      [2. Multi-Step Wizard]      [3. Progressive Accordion]
   • 2-column desktop            • 3 sequential steps        • Collapsible panels
   • Left: All form inputs       • 1. Details → 2. Shipping  • Validated steps collapse
   • Right: Sticky order card    • 3. Payment & Review       • into summary with [Edit]
   • Fastest for repeat buyers   • Best for luxury / high AOV• Zero mobile scroll fatigue
```

### 5.1 The 3 Checkout Styles

| Style Option (`beeclue_checkout_style`) | Layout & User Experience | Conversion Psychology & Best Use Case |
|---|---|---|
| **`split_single` (Split-Screen Single-Page)** | 2-column desktop split (`58% / 42%`). Left column displays Express Checkout (Apple/Google Pay), Customer Contact, Billing/Shipping address fields, and Payment Gateways. Right column displays a sticky order summary with product thumbnails, item variants, collapsible coupon input, tax breakdown, and trust badges. | **Frictionless Velocity**: Eliminates step navigation and back-and-forth clicking. Best for fashion, consumer goods, apparel, and stores with high repeat customer rates. |
| **`wizard` (Multi-Step Wizard)** | 3 sequential screens with an animated visual step indicator (`Step 1: Contact & Address` &rarr; `Step 2: Shipping Method` &rarr; `Step 3: Payment & Place Order`). Forward buttons validate current step inputs before advancing; previous steps can be revisited via breadcrumb pills. | **Cognitive Relief**: Prevents form intimidation by breaking complex orders into manageable micro-commitments. Ideal for luxury goods, high-ticket jewelry, custom orders, or cross-border purchases with multiple shipping options. |
| **`accordion` (Progressive Collapsible Accordion)** | All 3 steps exist on a single page in stacked accordion cards. Step 1 is open by default. Upon completion, Step 1 collapses into a neat 1-line verified summary card (`✓ John Doe • 123 Luxury Ave • [Edit]`), and Step 2 automatically slides open. | **Mobile Perfection**: Eliminates endless scrolling on small viewports. Keeps the customer oriented with immediate visual feedback while preserving full page context. |

### 5.2 Distraction-Free Enclosed Checkout Mode
When enabled via Customizer (`beeclue_checkout_distraction_free = true`):
- Strips out the primary header navigation menu, search bar, promotional banner, and mega-menu links.
- Replaces standard header with a clean, centered brand logo, an SSL 256-bit encrypted checkout lock badge, and a customer support hotline/chat link.
- Replaces multi-column footer with a minimalist single line showing copyright and essential legal links (Privacy Policy, Terms of Service, Return Policy).
- **Result**: Eliminates accidental exit clicks when customer intent is at its peak.

---

## 6. Checkout Accessibility & Keyboard Navigation (WCAG 2.1 AA)

- **Step Indicator Semantics**: In `wizard` mode, the step progress bar is marked as `<nav aria-label="Checkout Progress">` with `<ol>` and list items marked with `aria-current="step"` on the active step.
- **Accordion ARIA States**: In `accordion` mode, headers use `<button aria-expanded="true/false" aria-controls="step-panel-id">`.
- **Live Form Validation**: Inline error messages are linked to inputs via `aria-describedby` and alert regions use `aria-live="polite"`.
- **Order Review Focus**: Screen reader users are announced when line-item totals or shipping methods dynamically recalculate via WooCommerce checkout AJAX fragments.
