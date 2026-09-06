# Apple-Grade Typographic System for Next.js

Typography is the single most defining element that separates amateur AI websites from world-class human-designed digital products. In Next.js, we leverage `next/font` for zero layout shift (CLS) and automatic self-hosting.

---

## 1. Curated Font Pairing Strategies

| Brand Personality | Display / Headline Font | Body Font | Monospace / Data | Character & Mood |
| :--- | :--- | :--- | :--- | :--- |
| **Apple Minimal / Tech** | `Geist` (or SF Pro system) | `Geist Sans` | `Geist Mono` | Ultra-clean, mathematical, optical balance |
| **Editorial Luxury** | `Cormorant Garamond` | `Plus Jakarta Sans` | `Space Mono` | Haute couture, literary depth, prestige |
| **Swiss Modernism** | `Inter` (tight tracking) | `Inter` | `JetBrains Mono` | Objective, neutral, architectural discipline |
| **Warm Contemporary** | `Fraunces` | `Plus Jakarta Sans` | `Geist Mono` | Tactile, artisanal warmth, approachable craft |
| **High-Precision B2B** | `Plus Jakarta Sans` | `Inter` | `JetBrains Mono` | Corporate clarity, executive authority |

---

## 2. Next.js App Router Integration (`src/app/layout.tsx`)

```tsx
import { Geist, Geist_Mono, Cormorant_Garamond, Plus_Jakarta_Sans } from "next/font/google";

export const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
  display: "swap",
});

export const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
  display: "swap",
});

export const cormorant = Cormorant_Garamond({
  variable: "--font-editorial-serif",
  subsets: ["latin"],
  weight: ["300", "400", "500", "600"],
  display: "swap",
});
```

---

## 3. Typographic Rules of Human Craft

### 3.1 Tight Tracking on Large Display Headlines
When rendering large font sizes (`>= 2.5rem`), default web letter-spacing looks sparse and unconsidered. Always apply tight negative tracking:
- Hero Headlines (`4rem`+): `tracking-[-0.035em]`
- Section Titles (`2.5rem`–`3.5rem`): `tracking-[-0.025em]`
- Subsection Headers (`1.5rem`–`2rem`): `tracking-[-0.015em]`
- Body Text (`1rem`): `tracking-normal`
- Small Caps / Category Labels (`0.75rem`): `tracking-[0.08em] uppercase font-mono`

### 3.2 Maximum Line Length (The 65-Character Measure)
Never stretch body text across the entire width of a 1200px screen. Restrict prose containers to `max-w-prose` or `max-w-2xl` (~65 to 75 characters per line). This eliminates reader eye strain.

### 3.3 Optical Margin Alignment
When pairing headlines with kicker tags or icons, align them optically rather than relying on raw bounding boxes.
