# The Independent Design Critic & 100-Point Scoring Rubric

The **BeeClue Design Critic** is an objective evaluation engine independent from implementation. It holds the authority to reject work that fails to meet the agency's quality bar.

---

## 1. The 11-Vector Quality Scoring Rubric

Every generated storefront is scored on a 100-point weighted scale:

| Evaluation Dimension | Weight | Critical Success Criteria |
| :--- | :--- | :--- |
| **1. Brand Fidelity** | 15% | Does the visual execution precisely match the Brand DNA coordinates? |
| **2. Visual Hierarchy** | 10% | Is the focal point immediately obvious? Does the eye glide naturally down the page? |
| **3. Typography Mastery** | 10% | Fluid clamp scaling, optical balance, letter-spacing on microcopy, tight heading line heights. |
| **4. Composition & Spacing** | 10% | Intentional negative space, asymmetric balance, zero claustrophobic crowding. |
| **5. Imagery Art Direction** | 10% | Purpose-shot composition, intentional negative space for headlines, natural lighting. |
| **6. Industry Fit** | 10% | Solves the specific buyer objections and friction points for the client's industry. |
| **7. Commerce UX & Security** | 10% | Smooth AJAX cart drawer with CSRF nonce verification (check_ajax_referer) and input sanitization, sticky single product buy bar, accessible swatches. |
| **8. Accessibility (WCAG AA)**| 8% | Focus traps in modals, screen reader `aria-live` regions, $\ge 4.5:1$ text contrast. |
| **9. Performance (CWV)** | 7% | Sub-2.5s LCP, zero-dependency animations, critical CSS inlining, CLS $< 0.05$. |
| **10. Mobile Ergonomics** | 5% | Zero horizontal overflow, min 44px tap targets, full-screen glassmorphism menu. |
| **11. Originality & Anti-Generic**| 5% | Complete absence of AI design clichés (no purple gradients, no card spam, no filler buzzwords). |

---

## 2. Decision Thresholds

- **Score $\ge 95$**: **EXCEPTIONAL** — Flawless flagship execution. Exceeds agency standards.
- **Score $90 - 94$**: **PREMIUM** — Production ready. High-end bespoke craftsmanship.
- **Score $80 - 89$**: **NEEDS POLISH** — Solid foundation, minor typography or spacing adjustments required.
- **Score $70 - 79$**: **MAJOR REVISION** — Fails key brand or UX dimensions. Mandatory architectural patch.
- **Score $< 70$**: **REJECT** — Fundamental failure of design contract or accessibility. Complete rebuild required.

---

## 3. The Creative Director's Interrogation Checklist

Before certifying any build, the critic must answer:
1. *Does this store look like a $15,000 bespoke flagship, or a $50 Shopify theme?*
2. *Does this design feel like this specific brand, or could we swap the logo and put any competitor on it?*
3. *Does anything feel AI-generated (generic purple gradients, uninspired 3-column cards, filler buzzwords like "Elevate")?*
4. *What elements are unnecessary and should be ruthlessly removed to increase focus?*
5. *Does the mobile experience preserve the art direction, or did it collapse into generic stacked blocks?*
6. *Are all interactive commerce AJAX endpoints cryptographically protected against CSRF (`check_ajax_referer`) with sanitized inputs?*
