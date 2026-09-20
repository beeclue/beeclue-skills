# The Anti-Generic Design Linter

AI-generated websites frequently collapse into predictable visual clichés. The BeeClue Anti-Generic Linter scans designs and layouts to eliminate automated mediocrity.

---

## 1. The 12 AI Web-Design Clichés to Flag

| Cliché | Why It Appears | Why It Fails | Required Justification or Fix |
| :--- | :--- | :--- | :--- |
| **1. The AI Purple/Indigo Gradient** | Default color ramp of modern LLM training sets (`#6366F1` to `#A855F7`). | Makes every brand look like an unlaunched AI SaaS tool. | Use brand-specific palettes derived from `color-systems.md`. |
| **2. Universal Glassmorphism** | Adding `backdrop-filter: blur()` to every single card and container. | Destroys mobile GPU performance and muddies readability. | Restrict frosted glass strictly to sticky headers and overlay navs. |
| **3. "Cards Inside Cards" Syndrome** | Wrapping every headline, paragraph, and button in white bordered rounded boxes. | Creates visual clutter and claustrophobic layouts. | Use whitespace and subtle typography scale to separate hierarchy. |
| **4. Repetitive 3-Column Card Rows** | Generating 3 feature cards followed by 3 product cards followed by 3 blog cards. | Monotonous scroll cadence that induces user fatigue. | Alternate layout structures: 60/40 splits, full-bleed images, asymmetric bento grids. |
| **5. Bogus Floating Statistics** | *"99% Customer Satisfaction"*, *"10M+ Happy Users"* without sources. | Consumers instantly detect artificial social proof. | Only display verified, sourced metrics, or eliminate entirely. |
| **6. Random Floating Blobs & Waves** | Abstract SVG organic blobs floating behind hero images. | Dated 2019 Dribbble cliché with zero brand connection. | Replace with genuine photography, physical materiality, or clean negative space. |
| **7. Pill-Button Inflation** | Turning every tag, link, category, and heading into a pill capsule. | Destroys interactive hierarchy (users can't tell what is clickable). | Reserve pill shapes strictly for primary actions or verified interactive filter tags. |
| **8. Generic Stock Photo Smiles** | Business people laughing at salads or generic models staring blankly. | Destroys brand authenticity in milliseconds. | Use direct, high-detail product craftsmanship photography with natural lighting. |
| **9. The Faux-Luxury "Black & Gold"** | `#000000` background + `#D4AF37` metallic text + italic serif. | Screams "cheap perfume kiosk" rather than real heritage luxury. | Reference `luxury-definition.md` for genuine restraint, alabaster, and typography. |
| **10. Jittery Scroll Reveal Animations** | Every line of text sliding up and fading in slowly on scroll. | Frustrates buyers who just want to browse products. | Keep scroll animations instant (`< 20 lines` IntersectionObserver) or purely CSS. |
| **11. Buzzword Marketing Copy** | *"Elevate Your Life"*, *"Discover Excellence"*, *"Redefining Perfection"*. | Empty filler copy that says nothing about the product. | Reference `voice.md` for concrete, tactile product descriptions. |
| **12. Uniform Radius Everywhere** | Every element sharing an identical `border-radius: 16px`. | Lacks architectural contrast. | Balance soft cards with crisp `4px` or sharp `0px` image frames for editorial precision. |

---

## 2. The Intentional Justification Rule

A design element is never rejected solely because it appears on this list. It is rejected if it was used **without deliberate brand justification**. 

If a cyber-security brand intentionally uses dark indigo because of documented category signaling, that is valid. If a luxury ceramicist has a purple gradient hero, the linter rejects the implementation.
