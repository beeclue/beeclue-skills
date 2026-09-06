# The 60-30-10 Color Architecture & Material Contrast

A hallmark of amateur AI web design is an uncontrolled explosion of colors, neon gradients, and inconsistent button hues. In `beeclue-next-theme`, color is deployed with architectural restraint.

---

## 1. The 60-30-10 Composition Principle

Every color scheme is strictly governed by proportional spatial allocation:

- **60% Dominant Canvas**: The foundational background tone. In light mode: pure white (`#FFFFFF`) or warm bone linen (`#FBF9F5`). In dark mode: deep obsidian (`#09090B`) or slate charcoal (`#0F172A`).
- **30% Secondary Structural**: Card surfaces, navigation bars, typography, borders, and footer elements. Provides visual scaffolding and hierarchy.
- **10% Intentional Accent**: Reserved **strictly** for high-priority interactive conversion elements: primary CTA buttons, active state indicators, and focal data metrics.

---

## 2. Multi-Mode Surface Elevation (Dark & Light)

Surfaces in modern web applications simulate physical light and layered depth:

| Level | Light Mode Surface | Dark Mode Surface | Typical Application |
| :--- | :--- | :--- | :--- |
| **Level 0 (Canvas)** | `#FAFAFA` / `#F8FAFC` | `#09090B` | Root page background |
| **Level 1 (Base Surface)** | `#FFFFFF` | `#121216` | Bento cards, content containers, tables |
| **Level 2 (Elevated)** | `#FFFFFF` (+ shadow) | `#1A1A22` | Sticky navigation, dropdown menus, modals |
| **Level 3 (Overlay)** | `#FFFFFF` (+ border) | `#24242F` | Tooltips, popovers, active drawer dialogs |

---

## 3. WCAG 2.1 AA Contrast Enforcement

All color combinations must pass strict contrast ratios:
- **Body Text**: Minimum **4.5:1** contrast ratio against its immediate background.
- **Large Headlines / Display**: Minimum **3.0:1** contrast ratio.
- **Interactive UI Components & Focus Rings**: Minimum **3.0:1** against adjacent colors.

Never render light gray text (`#94A3B8`) on white backgrounds for critical body copy. Always test token pairings.
