# Multi-Vector Visual QA & Layout Integrity Loop

Before delivering any Next.js flagship website, execute a rigorous multi-vector visual QA check across viewports, dark/light modes, and high-density retina displays.

---

## 1. Multi-Breakpoint Responsive Matrix

Validate every page at these key viewport widths:
- **Mobile Compact (375px & 390px)**: iPhone SE / 14 / 15. Verify touch targets (`>= 44px`), no horizontal scroll leakage (`overflow-x: hidden`), readable typography.
- **Tablet Portrait (768px)**: iPad Mini / Air. Verify 2-column bento reflow, readable navigation.
- **Laptop Standard (1280px & 1440px)**: MacBook Air / Pro. Verify max-width container constraints (`max-w-7xl`).
- **Retina Ultra-Wide (1920px & 2560px)**: Studio Display / 4K. Verify background full-bleed integrity and crisp text rendering.

---

## 2. Dark / Light Mode Parity Check

If dark mode is supported:
1. **Contrast Preservation**: Ensure text does not disappear against dark surfaces.
2. **Border Luster**: Ensure card borders transition from dark subtle lines (`rgba(0,0,0,0.06)`) to luminous hairline borders (`rgba(255,255,255,0.1)`).
3. **Image Brightness**: Ensure images with pure white backgrounds are treated or framed appropriately to avoid blinding the user.

---

## 3. The 10-Second Visual Polish Checklist
- [ ] Are all icon stroke widths consistent across all components (1.25px or 1.5px)?
- [ ] Are all button labels vertically and horizontally optically centered?
- [ ] Is horizontal overflow (`overflow-x: hidden`) strictly contained?
- [ ] Are hero images displaying without layout shift (CLS = 0)?
- [ ] Are there zero emojis and zero decorative pill chips across all visible screens?
