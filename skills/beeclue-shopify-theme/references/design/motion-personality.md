# Motion Personality & Tactile Whimsy System

Animation in BeeClue digital storefronts is purposeful, performant, and brand-aware. It adds physical tactile feedback rather than decorative distraction.

---

## 1. Motion Personality Model

```yaml
motion_profile:
  intensity: 0-100       # Overall amplitude and speed
  elegance: 0-100        # Velvety deceleration and seamless fades
  playfulness: 0-100     # Elastic bounces and celebratory micro-moments
  precision: 0-100       # Mechanistic snappiness and zero-overshoot timing
  reduced_motion: "strict" # Full support for prefers-reduced-motion
```

---

## 2. Industry-Specific Motion Tuning

| Industry / Archetype | Intensity | Elegance | Playfulness | Precision | Timing & Easing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Haute / Quiet Luxury** | 30 | 95 | 10 | 90 | `500ms cubic-bezier(0.25, 1, 0.5, 1)` |
| **High-Tech / Automotive**| 65 | 70 | 15 | 98 | `180ms cubic-bezier(0, 0, 0.2, 1)` |
| **Children / Playful Goods**| 80 | 40 | 95 | 50 | `320ms cubic-bezier(0.175, 0.885, 0.32, 1.275)` |
| **Artisanal Home Goods** | 45 | 85 | 40 | 75 | `350ms cubic-bezier(0.4, 0, 0.2, 1)` |

---

## 3. Pure CSS Tactile Micro-Interactions

Zero external JavaScript animation libraries (GSAP, AOS, ScrollReveal) are permitted. All motion is authored using hardware-accelerated CSS transforms (`translate3d`, `scale`) and native `IntersectionObserver`.

### 3.1 Cart Badge Pop on Addition
```css
@keyframes cartBadgePop {
    0%   { transform: scale(1); }
    50%  { transform: scale(1.35); }
    100% { transform: scale(1); }
}
.cart-count.pop {
    animation: cartBadgePop 300ms var(--motion-ease-spring, cubic-bezier(0.175, 0.885, 0.32, 1.275));
}
```

### 3.2 Magnetic Hover Lift on CTA
```css
.btn-primary {
    transition: transform var(--motion-duration-fast, 150ms) ease,
                box-shadow var(--motion-duration-fast, 150ms) ease,
                background-color var(--motion-duration-fast, 150ms) ease;
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.15);
}
.btn-primary:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px -2px rgba(0, 0, 0, 0.1);
}
```

### 3.3 Infinite Trust Marquee (Hover-Pause)
```css
.marquee-track {
    display: flex;
    gap: 32px;
    width: max-content;
    animation: marqueeScroll 35s linear infinite;
}
.marquee-track:hover {
    animation-play-state: paused;
}
@keyframes marqueeScroll {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}
```

---

## 4. Accessibility & Reduced Motion

All motion styles MUST respect user system preferences:
```css
@media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
    .marquee-track {
        animation: none !important;
        transform: none !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
    }
}
```
