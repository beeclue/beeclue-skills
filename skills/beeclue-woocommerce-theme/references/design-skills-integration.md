# Multi-Skill Design Orchestration Guide for Beeclue Themes

This reference defines how the **Beeclue WooCommerce Theme Generator** coordinates with other specialized design skills available in the environment to produce **Superclass Themes**.

---

## 1. Skill Integration Map

When building a high-end WooCommerce theme, do not guess design tokens or rely on generic presets. Delegate to and consult these skills:

```
                  ┌─────────────────────────────────────────────────┐
                  │    beeclue-woocommerce-theme (Orchestrator)     │
                  └───────────────────────┬─────────────────────────┘
                                          │
    ┌───────────────────┬─────────────────┼─────────────────┬───────────────────┐
    ▼                   ▼                 ▼                 ▼                   ▼
ui-ux-pro-max      design-system        brand         whimsy-injector      a11y-auditor
(Style, Color,     (3-Layer Tokens,  (Voice, Tone,   (Micro-delights,    (WCAG AA, Focus
 Typography, UX)    Component Specs)  Guidelines)     Tactile Feedback)   Trap, Screen-Reader)
```

---

## 2. Phase-by-Phase Skill Execution

### Phase 1: Niche Discovery & Intelligence (`ui-ux-pro-max` + `brand`)

**Goal**: Extract the precise aesthetic direction, color harmonies, and typography pairings tailored to the client's industry.

1. **Query `ui-ux-pro-max`**:
   - Inspect or search `~/.gemini/config/skills/ui-ux-pro-max/data/`:
     - `styles.csv`: Select 1 of 67 curated styles (e.g., Luxury Minimal, Neo-brutalism, Warm Editorial, Organic Craft, Soft Neo-morphic).
     - `colors.csv`: Pull industry-specific 60-30-10 palettes (dominant, secondary, accent) with contrast ratios.
     - `typography.csv`: Select authentic Google Font pairings with appropriate weights and letter-spacing.
     - `ux-guidelines.csv`: Identify critical UX dos & don'ts for e-commerce checkouts and product discovery.
2. **Consult `brand`**:
   - Establish brand personality (e.g., "Refined & Artisanal", "Playful & Disruptive").
   - Align copywriting tone for micro-copy (e.g., cart empty state, free shipping milestones, newsletter CTA).

---

### Phase 2: Token Architecture & Component Specs (`design-system`)

**Goal**: Build a scalable, maintainable 3-layer CSS custom property architecture rather than a flat variable dump.

1. **Load `design-system` standards**:
   - Reference `~/.gemini/config/skills/design-system/references/token-architecture.md`.
2. **Implement the 3 Layers**:
   - **Layer 1: Primitives** — Raw hex values, absolute spacing, raw clamp values.
   - **Layer 2: Semantics** — Intent-driven tokens (`--surface-base`, `--text-primary`, `--action-primary`).
   - **Layer 3: Components** — Specific widget tokens (`--product-card-radius`, `--cart-drawer-width`, `--sticky-bar-height`).
3. **Define Component State Matrix**:
   - Ensure every button, swatch, and card has explicit styles for:
     `Default` $\rightarrow$ `Hover` $\rightarrow$ `Active` $\rightarrow$ `Focus-Visible` $\rightarrow$ `Disabled`.

---

### Phase 3: Tactile Whimsy & Micro-Interactions (`agency-whimsy-injector`)

**Goal**: Elevate the theme from a corporate template to an unforgettable boutique shopping experience.

1. **Cart Add Milestone**:
   - When a user clicks "Quick Add" or "Add to Cart", trigger a micro-animation:
     - Button label transforms to "Added ✓" with a gentle bounce.
     - Header cart counter badge pops with a subtle scale pulse (`scale(1.3) -> scale(1)`).
     - Slide-out drawer opens smoothly with a staggered slide of cart items.
2. **Free Shipping Meter Celebration**:
   - When the cart total crosses the threshold, the progress bar turns accent color and triggers a subtle celebratory pulse or confetti sparkle.
3. **Interactive Marquee**:
   - Infinite trust ticker pauses smoothly on `:hover` to allow reading.
4. **Button Magnetic Feel**:
   - Pill buttons have subtle hover lifts (`transform: translateY(-2px)`) with realistic soft shadow expansion.

---

### Phase 4: Accessibility & Robustness (`a11y-debugging` / `agency-accessibility-auditor`)

**Goal**: Guarantee full compliance with WCAG 2.1/2.2 AA standards.

1. **Focus Trap in Modals & Drawers**:
   - When the Cart Drawer, Mobile Navigation, or Search Overlay is open:
     - Trap Tab key within the container.
     - Add `aria-modal="true"` and appropriate `role="dialog"`.
     - Close on `Escape` and restore focus back to the triggering button.
2. **Screen Reader Live Announcements**:
   - Add `<div id="cart-live-region" class="sr-only" aria-live="polite" aria-atomic="true"></div>`.
   - On item added or removed, update message (e.g., *"Item added to cart. Subtotal: $45.00"*).
3. **Accessible Color Contrast**:
   - Ensure text-to-background contrast ratio is $\ge 4.5:1$ for body text and $\ge 3:1$ for large headings and interactive borders.
4. **Touch Targets**:
   - All interactive controls (hamburger, cart icon, quantity buttons, swatches) must be at least `44x44px`.
