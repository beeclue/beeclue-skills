# The Anti-Generic Design Linter for Next.js

AI-generated websites have become infamous for predictable visual patterns that look automated and generic. The Beeclue Anti-Generic Linter enforces human designer standards across every layout and component.

---

## 1. The 14 Deadly Sins of AI Web Design

| AI Cliché | Why It Appears | Why It Fails | Strict Human Replacement Rule |
| :--- | :--- | :--- | :--- |
| **1. The AI Purple/Indigo Gradient** | Default color ramp of modern LLM training sets (`#6366F1` to `#A855F7`). | Makes every brand look like an unlaunched AI wrapper. | Derive bespoke 60-30-10 palettes from client Brand DNA. |
| **2. Decorative "Chip / Pill" Inflation** | AI slaps pill badges above every heading (`[ ✨ AI Powered ]`, `[ 🚀 Next-Gen ]`). | Clutters visual hierarchy; screams template automation. | **Banned.** Only allow chips for verifiable system status (e.g. `Operational`). Otherwise eliminate completely. |
| **3. Emojis in Professional UI** | AI uses emojis (`🚀`, `✨`, `🔥`, `💡`, `🎉`) as icons or bullet markers. | Instantly destroys enterprise credibility; looks childish. | **Strictly Forbidden.** Zero emojis. Use bespoke, razor-thin luxury SVG or Lucide icons (`stroke-[1.25]`). |
| **4. Universal Frosted Glass On Everything** | Applying `backdrop-blur` to every card, button, and footer container. | Destroys mobile GPU performance and muddies readability. | Restrict frosted glass strictly to sticky headers and overlay drawers. |
| **5. "Cards Inside Cards" Claustrophobia** | Wrapping headlines, paragraphs, and buttons in nested bordered boxes. | Monotonous, boxed-in layout that induces visual fatigue. | Use intentional whitespace and subtle typographic scale for separation. |
| **6. Monotonous 3-Column Card Spam** | 3 feature cards followed by 3 testimonial cards followed by 3 blog cards. | Predictable scroll cadence that loses user engagement. | Alternate layouts: asymmetric Bento grids, 60/40 splits, full-bleed focal points. |
| **7. Fabricated Social Proof** | *"99% Satisfaction"*, *"10M+ Happy Users"* without sources. | Savvy buyers immediately detect fake numbers. | Only display verified, sourced metrics with context, or omit entirely. |
| **8. Generic Stock Photo Smiles** | Corporate models laughing at salads or staring blankly at laptops. | Destroys brand authenticity in milliseconds. | Curate authentic, contextual Unsplash photography with cinematic lighting. |
| **9. Faux-Luxury "Black & Gold"** | Pure `#000000` + metallic gold `#D4AF37` text + italic serif. | Looks like a cheap fragrance kiosk rather than authentic luxury. | Use understated palettes: warm alabaster, charcoal ink, travertine stone. |
| **10. Jittery Scroll Reveal Staggering** | Every word or line sliding up with slow delays on scroll. | Frustrates visitors who want to browse quickly. | Keep motion fast, subtle, or instant (Apple spring curves under 300ms). |
| **11. Buzzword Marketing Copy** | *"Elevate your workflow"*, *"Unleash your potential"*, *"Seamless synergy"*. | Empty filler copy that communicates zero product value. | Ground every sentence in concrete facts, numbers, and physical nouns. |
| **12. Uniform Radius Everywhere** | Every element sharing an identical `border-radius: 16px`. | Lacks architectural tension and typographic contrast. | Balance soft container corners with crisp, sharp 1px borders and frames. |
| **13. Missing Human Asymmetry** | Everything perfectly centered in sterile identical blocks. | Feels machine-generated, rigid, and soulless. | Introduce deliberate asymmetry, editorial pull-quotes, and focal dominance. |
| **14. Cartoonish / Bloated Icons** | Thick, colorful, rounded icons that look like mobile game assets. | Incompatible with professional or luxury brand stature. | Use razor-thin 1.25px–1.5px luxury line icons with optical padding. |

---

## 2. The Human Designer Verification Gate

Before any generated page is certified, ask these 3 core questions:
1. *Could this page have been designed by a senior designer at Apple, Pentagram, or Stripe?*
2. *Are there any emojis or decorative pill chips anywhere on the screen?* (If yes, fail immediately).
3. *Does the layout possess natural human breathing room, asymmetric tension, and authentic industry copy?*
