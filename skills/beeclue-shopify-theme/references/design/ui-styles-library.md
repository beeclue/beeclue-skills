# Popular Web UI Design Styles Library (27 Styles)

Use this library during Discovery Step 7b. NEVER assume a style. ALWAYS present options, recommend top 2-3 based on industry (see `references/intelligence/industry-style-matrix.md`), then get explicit user confirmation before building.

Each style includes an **Apple-grade adaptation** note — how to execute it without looking cheap, generic, or AI-generated. All styles must still obey Human Designer Mandates: zero emojis, no decorative chip spam, razor-thin Lucide icons, asymmetry over 3-card spam.

---

## 1. Glassmorphism
- **Traits**: Translucent frosted-glass surfaces, backdrop-blur, layered depth, subtle borders.
- **Best for**: SaaS, fintech dashboards, premium tech.
- **Caution**: Low contrast risk — always pair with high-contrast text.
- **Apple adaptation**: Default Beeclue navbar + Bento cards. `backdrop-blur(20px) saturate(180%)`, 1px `rgba(0,0,0,0.06)` border.

## 2. Neumorphism
- **Traits**: Soft extruded/pressed shapes, dual light+dark shadows on same-color background.
- **Best for**: Settings panels, audio/IoT controls, tactile dashboards.
- **Caution**: Poor accessibility contrast; use sparingly for small controls only, never full pages.
- **Apple adaptation**: Restrict to toggles/cards on matte canvas; keep text outside neumorphic surfaces.

## 3. Skeuomorphism
- **Traits**: Digital UI imitates real materials (leather, metal, paper, switches).
- **Best for**: Niche luxury, watches, musical instruments, heritage brands.
- **Caution**: Dated fast; heavy assets hurt performance.
- **Apple adaptation**: Use only as micro-texture (paper grain, metal sheen) inside Minimalist layout.

## 4. Flat Design
- **Traits**: 2D shapes, solid colors, no shadows/gradients, clean iconography.
- **Best for**: SaaS, government, education, high-accessibility sites.
- **Caution**: Can feel generic without strong typography + asymmetry.
- **Apple adaptation**: Pair with Swiss grid + tight tracking headlines to avoid blandness.

## 5. Material Design (M3)
- **Traits**: Google system — surfaces, elevation levels, FABs, motion specs, tonal palettes.
- **Best for**: Android-adjacent products, data-heavy admin, B2B tools.
- **Caution**: Looks "Google-default" unless re-tokenized.
- **Apple adaptation**: Re-skin with Beeclue 5-layer tokens; keep elevation logic, replace Roboto with Geist/Inter.

## 6. Brutalism
- **Traits**: Raw layouts, system fonts, harsh contrast, exposed structure, minimal styling.
- **Best for**: Underground culture, architecture manifestos, anti-luxury statements.
- **Caution**: Alienates mainstream buyers; conversion risk for commerce/medical/finance.
- **Apple adaptation**: Keep raw grid + oversized type but fix a11y (focus states, contrast).

## 7. Neo-Brutalism
- **Traits**: Brutalist bones + modern UX: thick borders, hard shadows, bold colors, oversized type.
- **Best for**: Gen-Z DTC, creator tools, gaming, streetwear.
- **Caution**: Tires quickly; limit to marketing pages, not checkout flows.
- **Apple adaptation**: One neo-brutalist hero + clean Minimalist body to sustain conversion.

## 8. Bento Grid
- **Traits**: Modular rectangular cards of varied sizes, dashboard-like composition.
- **Best for**: SaaS features, fintech, AI platforms, portfolios.
- **Caution**: The most overused AI pattern — must use asymmetric weights, not uniform 3x3.
- **Apple adaptation**: DEFAULT. Vary spans (2x large + 3x small), one live/telemetry card, 60/40 splits.

## 9. Minimalism
- **Traits**: Whitespace, restrained type, limited palette, strong hierarchy.
- **Best for**: Luxury, medical, legal, premium SaaS — highest conversion safety.
- **Caution**: Empty ≠ premium; needs focal dominance + photography.
- **Apple adaptation**: Cupertino Clean baseline. `clamp(5rem,10vw,9rem)` section spacing.

## 10. Maximalism
- **Traits**: Dense visuals, bold color, layered type, patterns, decoration.
- **Best for**: Fashion editorials, music, festivals, Gen-Z retail.
- **Caution**: Kills performance + readability; never for clinical/finance.
- **Apple adaptation**: Contain to hero/marquee band; keep transactional sections Minimalist.

## 11. Y2K
- **Traits**: Chrome, glossy gradients, bubbly/futuristic type, playful techno-optimism.
- **Best for**: Streetwear, pop culture, beauty Gen-Z, music.
- **Caution**: Novelty fades; polarizing for B2B.
- **Apple adaptation**: Chrome accents + glossy buttons only; keep body type clean.

## 12. Cyberpunk
- **Traits**: Dark base, neon glow, terminal type, futuristic HUD elements.
- **Best for**: Cybersecurity, blockchain, gaming, AI infra.
- **Caution**: Glow overuse destroys readability.
- **Apple adaptation**: Cyber-Minimal archetype — obsidian `#050507`, single neon accent, mono metadata.

## 13. Aurora / Mesh Gradient
- **Traits**: Blurred multicolor gradient blobs as atmospheric background.
- **Best for**: SaaS heroes, AI products, wellness, fintech onboarding.
- **Caution**: BANNED as generic purple/indigo AI gradient (`#6366F1→#A855F7`). Must derive from Brand DNA.
- **Apple adaptation**: Allowed only when colors come from brand palette, at <40% opacity, behind frosted content.

## 14. Claymorphism
- **Traits**: Soft inflated 3D, thick rounded corners, pastel, double inner+outer shadows.
- **Best for**: Kids products, playful fintech, education, wellness apps.
- **Caution**: Infantilizes luxury/B2B/medical brands.
- **Apple adaptation**: Use for single CTA card or pricing highlight only.

## 15. Liquid / Fluid UI
- **Traits**: Blobs, organic morphing shapes, flowing transitions, gooey motion.
- **Best for**: Wellness, beauty, creative studios, sustainability.
- **Caution**: Motion-heavy; respect `prefers-reduced-motion`.
- **Apple adaptation**: Implement with Motion-Primitives + spring `cubic-bezier(0.16,1,0.3,1)`; static fallback required.

## 16. Retro / Vintage
- **Traits**: Print/advertising eras: serif badges, grain, muted palettes, old-web motifs.
- **Best for**: Hospitality, barbershops, craft breweries, heritage retail.
- **Caution**: Can read as low-quality if typography is sloppy.
- **Apple adaptation**: Warm Artisanal archetype — Fraunces serif + cream canvas + grain overlay.

## 17. Pixel Art
- **Traits**: Deliberate low-res pixels, 8-bit type, sprite illustrations.
- **Best for**: Gaming, dev tools with playful brand, nostalgia drops.
- **Caution**: Extremely niche; conversion poison for luxury/medical/finance.
- **Apple adaptation**: Confine to illustrations/easter eggs; body UI stays Minimalist.

## 18. Editorial Design
- **Traits**: Magazine grids, dramatic serif headlines, asymmetry, pull-quotes, large imagery.
- **Best for**: Luxury, fashion, architecture, real estate, law thought-leadership.
- **Caution**: Needs exceptional photography + copy; weak content looks empty.
- **Apple adaptation**: Neo-Editorial archetype — Cormorant/Fraunces display + sharp `0-2px` frames.

## 19. Swiss / International Style
- **Traits**: Strict grid, Helvetica/Inter, strong alignment, hairline rules, minimal decoration.
- **Best for**: Consulting, industrial, legal, data infra, enterprise.
- **Caution**: Cold without one warm accent or human photography.
- **Apple adaptation**: Swiss Precision archetype + international orange/red accent.

## 20. Organic / Natural UI
- **Traits**: Earth tones, irregular curves, grain textures, botanical motifs.
- **Best for**: Skincare, wellness, hospitality, sustainability, craft F&B.
- **Caution**: Earthy ≠ muddy — maintain contrast ratios.
- **Apple adaptation**: Warm Artisanal + cream `#FAF7F2`, sage/amber accents, full-bleed nature hero.

## 21. Hand-drawn / Doodle
- **Traits**: Imperfect lines, sketch illustrations, handwritten type, annotations.
- **Best for**: Education, SaaS onboarding illustrations, nonprofit, kids.
- **Caution**: Undermines trust in finance/medical/legal.
- **Apple adaptation**: Illustrations only; UI chrome stays razor-precise.

## 22. Memphis Design
- **Traits**: Geometric shapes, bright blocks, squiggles, playful clashing patterns.
- **Best for**: Creative agencies, events, youth brands.
- **Caution**: Chaotic at scale; use as accent band.
- **Apple adaptation**: Kinetic Creative hero band + Minimalist body.

## 23. 3D / Immersive
- **Traits**: WebGL scenes, spatial cards, parallax, interactive objects.
- **Best for**: Flagship launches, automotive, real estate tours, product configurators.
- **Caution**: Heavy JS; must hit LCP <2.5s with lazy-load + fallback image.
- **Apple adaptation**: One hero 3D moment + static poster fallback; body stays fast.

## 24. Retro-Futurism
- **Traits**: Future as seen from the past (mid-century space age, synthwave, art deco tech).
- **Best for**: Bars, automotive, watches, boutique hotels.
- **Caution**: Camp risk — commit fully or skip.
- **Apple adaptation**: Display type + chrome/detailing in hero; clean body.

## 25. Dark Mode / OLED
- **Traits**: Near-black surfaces, high-contrast accents, glow details.
- **Best for**: Dev tools, AI, fintech dashboards, media/streaming.
- **Caution**: Must still ship light mode unless brand is dark-native.
- **Apple adaptation**: Cyber-Minimal tokens; test `rgba(255,255,255,0.08)` borders on `#050507`.

## 26. Monochromatic
- **Traits**: Single hue + tonal variations, texture/type carry interest.
- **Best for**: Luxury, photography, architecture, minimal SaaS.
- **Caution**: Flat without material contrast (matte vs gloss vs blur).
- **Apple adaptation**: Slate/ink mono + single accent reserved for primary CTA.

## 27. High-Contrast Accessibility-First
- **Traits**: AAA contrast, large type, obvious focus/interaction states, reduced ambiguity.
- **Best for**: Government, healthcare, senior audiences, education, public sector.
- **Caution**: Can feel utilitarian — warm it with photography + serif display.
- **Apple adaptation**: Clinical Luxe base + `4.5:1` minimum, visible focus rings, `prefers-reduced-motion` honored.
