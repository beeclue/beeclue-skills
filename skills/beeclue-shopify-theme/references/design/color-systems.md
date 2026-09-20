# Color Systems & 60-30-10 Architecture

BeeClue color systems prevent the "cluttered rainbow" effect by enforcing strict proportional color hierarchy and verified accessibility contrast ratios.

---

## 1. The 60-30-10 Color Distribution Principle

Every superclass storefront allocates its visual surface area according to the classical 60-30-10 rule:

- **60% Dominant Canvas (`--color-bg`, `--color-surface-base`)**:
  - The backdrop and primary card containers. Typically warm off-white, raw alabaster, limestone, or deep obsidian.
- **30% Structural Secondary (`--color-text-primary`, `--color-text-secondary`, `--color-border-subtle`)**:
  - Headings, body copy, subtle divider borders, footer backgrounds, and product card outlines.
- **10% Intentional Accent (`--color-action-primary`, hover rings, notification badges)**:
  - Reserved strictly for conversion-driving interactive touchpoints: "Add to Bag", active filter pills, cart checkout buttons, free shipping progress bar.

---

## 2. WCAG 2.1 AA Contrast Standards

All text and essential interactive components must satisfy mathematical contrast thresholds:

- **Body Text (`< 18pt` or `< 14pt bold`)**: Contrast ratio $\ge 4.5:1$ against background.
- **Large Headings (`\ge 18pt` or `\ge 14pt bold`)**: Contrast ratio $\ge 3.0:1$ against background.
- **Interactive UI Components & Borders**: Contrast ratio $\ge 3.0:1$ for focus rings, form inputs, and active button outlines.

---

## 3. Curated Niche Color Palettes

### 3.1 Warm Editorial (Ceramics, Home Goods, Fashion)
- **60% Canvas**: `#F7F3EE` (Warm Linen)
- **30% Structure**: `#1C1915` (Charcoal Ink) / `#8A7968` (Warm Taupe)
- **10% Accent**: `#C8602A` (Terracotta)

### 3.2 Clinical Botanical (Dermatology, Skincare)
- **60% Canvas**: `#FBF9F5` (Hydrated Cream)
- **30% Structure**: `#23282B` (Mineral Slate) / `#E2E6E2` (Subtle Sage Border)
- **10% Accent**: `#436652` (Deep Forest Sage)

### 3.3 Aerospace Precision (Electronics, Automotive)
- **60% Canvas**: `#0E1114` (Carbon Matte)
- **30% Structure**: `#E8EAEB` (Titanium Light) / `#2A2F35` (Milled Metal Border)
- **10% Accent**: `#FF5500` (Signal Orange) or `#0070F3` (Electric Blue)

---

## 4. Dark Mode Semantic Inversion

Dark mode must NOT be a naive inverted color filter. It requires mapped semantic re-assignment:
```css
[data-theme="dark"], .theme-dark {
    --color-bg:               #111315;
    --color-surface-base:     #1a1d21;
    --color-surface-sunken:   #0a0b0d;
    --color-text-primary:     #f4f5f6;
    --color-text-secondary:   #9ea3aa;
    --color-border-subtle:    rgba(255, 255, 255, 0.08);
    --header-bg:              rgba(17, 19, 21, 0.85);
}
```
