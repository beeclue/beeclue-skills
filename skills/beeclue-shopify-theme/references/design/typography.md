# Typography Architecture & Fluid Scaling

Typographic hierarchy in BeeClue digital flagships is treated as the primary vehicle of art direction and brand voice.

---

## 1. Google Font Pairings by Archetype

| Archetype | Display / Heading Font | Body / Functional Font | Monospace / Spec Font | Typical Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **Quiet Luxury** | `Cormorant Garamond` (300/400) | `Plus Jakarta Sans` (400/500) | `JetBrains Mono` (400) | Headings: `-0.02em`, Caps: `+0.15em` |
| **Editorial Luxury** | `Playfair Display` (400/600) | `DM Sans` (400/500) | `ui-monospace` | Headings: `-0.01em`, Caps: `+0.12em` |
| **Architectural Minimal** | `Syne` (500/700) or `Cabinet Grotesk` | `Inter` (400/500) | `Space Mono` | Headings: `-0.03em`, Caps: `+0.08em` |
| **Technical Premium** | `Space Grotesk` (500/700) | `Plus Jakarta Sans` (400/600) | `JetBrains Mono` (500) | Headings: `-0.02em`, Caps: `+0.05em` |
| **Artisanal Craft** | `Fraunces` (300/500) or `Lora` | `DM Sans` (400) | `Courier Prime` | Headings: `0em`, Caps: `+0.1em` |
| **Clinical Premium** | `Plus Jakarta Sans` (600/700) | `Inter` (400/500) | `ui-monospace` | Headings: `-0.02em`, Caps: `+0.06em` |
| **Playful Premium** | `Outfit` (600/800) | `Plus Jakarta Sans` (400/500) | `JetBrains Mono` | Headings: `-0.01em`, Caps: `+0.04em` |

---

## 2. Fluid Clamp Typography Formulas

All major headings must use CSS `clamp()` to transition smoothly between mobile (375px) and wide desktop (1440px) without jagged media query jumps:

```css
/* Hero Display Heading (44px mobile -> 76px desktop) */
--text-hero: clamp(2.75rem, 1.8rem + 4.1vw, 4.75rem);

/* Section H2 (28px mobile -> 44px desktop) */
--text-section: clamp(1.75rem, 1.25rem + 2.1vw, 2.75rem);

/* Sub-section H3 (20px mobile -> 26px desktop) */
--text-h3: clamp(1.25rem, 1.1rem + 0.6vw, 1.625rem);

/* Body Text (15px mobile -> 17px desktop) */
--text-body: clamp(0.938rem, 0.9rem + 0.16vw, 1.063rem);

/* Eyebrow Label (11px fixed, uppercase, tracking) */
--text-eyebrow: 0.688rem;
```

---

## 3. Typographic Rules of Restraint
1. **Single H1 per Page**: The homepage hero and single PDP contain exactly one semantic `<h1>`.
2. **Line Heights**: Headings must maintain tight line heights (`1.05` to `1.2`) to prevent awkward line breaks. Body text must maintain relaxed reading line heights (`1.55` to `1.7`).
3. **Eyebrow Microcopy**: Always set `text-transform: uppercase`, `letter-spacing: 0.12em` to `0.2em`, and font weight `500` or `600`.
