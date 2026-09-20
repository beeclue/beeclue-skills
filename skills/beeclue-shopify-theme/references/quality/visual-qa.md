# Visual QA & Autonomous Inspection Loop

Visual quality assurance guarantees that designs render with pixel-perfect alignment, proper responsive typography, and zero layout overflow across desktop, tablet, and mobile viewports.

---

## 1. The Autonomous Visual QA Loop

When browser automation or screenshot tools are available, execute this systematic loop:

```
BUILD Theme Files
   │
   ▼
RENDER Page in Browser
   │
   ▼
CAPTURE Multi-Viewport Screenshots (Desktop: 1440px, Tablet: 768px, Mobile: 375px)
   │
   ▼
ANALYZE Visual Artifacts (Alignment, Typography Rhythm, Spacing Consistency)
   │
   ▼
CRITIQUE Against Design Contract
   │
   ├── Issues Detected → PATCH Code → Re-render
   └── No Defects → CERTIFY Visual Integrity
```

---

## 2. Multi-Viewport Inspection Checklist

### 2.1 Desktop Inspection (1440px)
- [ ] Header logo, centered navigation, and cart/search icons align on a single baseline.
- [ ] Maximum content container does not stretch beyond `1440px` on ultra-wide screens.
- [ ] Asymmetric editorial splits maintain proper proportion (e.g. 60/40) without image distortion.
- [ ] Product card grid maintains equal-height cards and consistent image aspect ratios.

### 2.2 Tablet Inspection (768px - 1024px)
- [ ] Navigation cleanly transitions from desktop menu links to mobile hamburger button.
- [ ] Product cards adapt from 4 columns to 2 or 3 columns without cramped text.
- [ ] Touch targets on filters, swatches, and cart drawer close button expand to minimum `44x44px`.

### 2.3 Mobile Inspection (375px)
- [ ] Horizontal scroll check: `document.documentElement.scrollWidth === window.innerWidth` (no horizontal overflow).
- [ ] Full-screen glassmorphism mobile overlay slides down cleanly with staggered link fade-in.
- [ ] Single product sticky buy bar anchors smoothly to viewport bottom without covering navigation controls.
- [ ] Typography scale: H1 display headings scale down via fluid clamp to avoid multi-line awkward wraps.
