# Apple Spring Physics & Micro-Interactions

Motion in Apple interfaces is never decorative fluff; it communicates physical mass, state transitions, and spatial reality.

---

## 1. Apple Spring Physics Curves

Avoid default browser linear or generic `ease-in-out` transitions. Use high-friction spring deceleration:

```css
/* Core Apple Motion Variables */
:root {
  --ease-apple-spring: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-apple-smooth: cubic-bezier(0.25, 1, 0.5, 1);
  --duration-hover: 200ms;
  --duration-modal: 400ms;
  --duration-page: 600ms;
}
```

---

## 2. Tactile Micro-Interactions

### 2.1 Magnetic Lift on Buttons & Cards
Interactive elements should feel tactile when hovered:
```css
.apple-card-interactive {
  transition: transform 300ms var(--ease-apple-spring), box-shadow 300ms var(--ease-apple-spring), border-color 300ms ease;
}

.apple-card-interactive:hover {
  transform: translateY(-3px);
  box-shadow: 0 16px 36px -12px rgba(0, 0, 0, 0.08);
  border-color: rgba(0, 0, 0, 0.12);
}

.apple-card-interactive:active {
  transform: translateY(-1px) scale(0.99);
}
```

### 2.2 Specular Border Highlight
On dark theme surfaces, create a subtle radial shine on hover that tracks cursor movement or gives depth to the edge.

---

## 3. Strict Accessibility: `prefers-reduced-motion`

Respect user OS accessibility preferences without breaking layout functionality:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## 4. Motion-Primitives Component Library (`https://motion-primitives.com/`)

For advanced physics-based micro-interactions, consult `references/nextjs/motion-primitives.md`:
- **Hero Typography**: `TextShimmer` for subtle specular light across keywords.
- **Brand Proof**: `InfiniteSlider` for frictionless continuous logo marquees.
- **Conversion Triggers**: `Magnetic` for cursor-attracted action buttons.
- **Card Materiality**: `Spotlight` and `BorderTrail` for luminous Bento grid depth.
- **Modals & Expanders**: `MorphingDialog` for seamless card-to-modal expansion.
