# Layout Grids & Visual Cadence

A superclass storefront avoids the monotonous "card grid after card grid" syndrome by orchestrating varied visual rhythms across the customer journey.

---

## 1. The 4 Structural Layout Systems

### 1.1 Asymmetric Editorial Split (60/40 or 70/30)
- Used for hero sections and brand storytelling modules.
- One dominant visual column paired with a staggered typography column.
```css
.editorial-split {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: clamp(2rem, 5vw, 6rem);
    align-items: center;
}
@media (max-width: 1024px) {
    .editorial-split { grid-template-columns: 1fr; }
}
```

### 1.2 Dynamic Product Catalog Grid
- Fluid multi-column layout adapting cleanly across screen sizes:
```css
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: var(--grid-gap-desktop, 32px);
}
@media (max-width: 768px) {
    .product-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: var(--grid-gap-mobile, 16px);
    }
}
```

### 1.3 Asymmetric Feature Breakout
- Interspersed between standard catalog grids to break scroll fatigue:
  - 1 giant full-bleed lifestyle image spanning 2 columns + 2 individual product cards stacked alongside.

### 1.4 Horizontal Swipe Carousel (Mobile Only)
- On mobile devices (`< 768px`), secondary collections or testimonials convert from stacked vertical blocks into smooth CSS scroll-snap carousels to preserve vertical page length.

---

## 2. Vertical Section Spacing & Editorial Cadence

Page pacing requires deliberate breathing room between chapters:
```css
.section-padding {
    padding-top: var(--section-spacing, clamp(5rem, 10vw, 10rem));
    padding-bottom: var(--section-spacing, clamp(5rem, 10vw, 10rem));
}
.section-padding-compact {
    padding-top: var(--section-spacing-sm, clamp(3rem, 6vw, 6rem));
    padding-bottom: var(--section-spacing-sm, clamp(3rem, 6vw, 6rem));
}
```

### Alternating Section Rhythm:
1. **Hero**: High-impact asymmetric editorial (Image + Staggered H1)
2. **Trust Bar**: Tight infinite ticker (Low height, microcopy)
3. **Curated Drop**: 4-column product grid (Commercial focus)
4. **Editorial Story**: Immersive full-width quote or split narrative (Atmospheric)
5. **Collection Bento**: 3-card asymmetric collection row (Navigation)
6. **Social Proof**: 3-card clean reviews without star overload
7. **Newsletter**: High-contrast, full-width dark section (Conversion capture)
