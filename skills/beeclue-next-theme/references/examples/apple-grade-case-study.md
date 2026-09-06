# End-to-End Case Study: Vanguard Studio Next.js 15 Flagship

This case study traces how the `beeclue-next-theme` pipeline transforms a raw architectural client brief into a production Next.js 15 App Router website with Apple-grade polish.

---

## 1. Client Brief & Questionnaire Discovery

- **Business Name**: Vanguard Studio
- **Industry**: Contemporary Sustainable Architecture & Bespoke Estates
- **Target Audience**: High-net-worth individuals, institutional art trusts, boutique hospitality founders
- **Primary Conversion**: Schedule Private Architectural Consultation
- **Aesthetic Direction**: Cupertino Clean meets Neo-Editorial (warm limestone canvas, razor-thin lines, spatial photography, zero emojis, zero chip spam)

---

## 2. Quantitative Brand DNA (0–100 Scale)

```yaml
brand_dna:
  positioning:
    luxury: 95
    premium: 95
    accessible: 10
    innovative: 85
    heritage: 50
  personality:
    sophistication: 95
    warmth: 60
    minimalism: 90
    boldness: 80
    technicality: 75
  visual:
    editorial: 90
    architectural: 95
    retina_precision: 95
    materiality: 85
    cinematic: 90
  motion:
    spring_physics: 85
    unhurried_grace: 90
    micro_tactility: 90
    prefers_reduced: 100
```

---

## 3. Emitted Design Contract (YAML)

```yaml
design_contract:
  brand:
    name: "Vanguard Studio"
    industry: "Architecture & Spatial Design"
    archetype: "Cupertino Clean + Neo-Editorial"
  typography:
    display_font: "Geist Sans"
    editorial_font: "Cormorant Garamond"
    body_font: "Geist Sans"
    mono_font: "Geist Mono"
    hero_scale: "clamp(2.75rem, 6vw, 5rem)"
  colors:
    canvas_light: "#FAF8F5"       # Warm architectural limestone
    surface_light: "#FFFFFF"
    text_primary_light: "#181716" # Charcoal ink
    text_secondary_light: "#6E6B68"
    accent: "#B85D36"             # Terracotta / corten steel accent
    border_subtle: "rgba(24, 23, 22, 0.08)"
  layout:
    section_spacing: "clamp(5rem, 10vw, 9rem)"
    card_radius: "1.5rem"
    container_max_width: "80rem"
  imagery:
    primary_unsplash_id: "1600585154340-be6161a56a0c"
    secondary_unsplash_id: "1600596542815-ffad4c1539a9"
```

---

## 4. Production Code Excerpts

### 4.1 Frosted Glass Navigation (`src/components/layout/navbar.tsx`)
Features a 20px blur backdrop, hairline border, luxury stroke icons, and accessible mobile drawer.

### 4.2 Bento Architecture Grid (`src/components/sections/bento-grid.tsx`)
Showcases three core disciplines: Passive Solar Engineering, Monolithic Concrete Craft, and Master Planning.

### 4.3 Structured Data (`src/app/layout.tsx`)
Injects `Organization` and `WebSite` JSON-LD schemas alongside `FAQPage` on the FAQ route.

### 4.4 Mandatory Agency Footer Attribution
```tsx
<p className="text-xs text-neutral-500">
  <span>Website Built by </span>
  <a
    href="https://beeclue.com/?utm_source=client_site&utm_medium=footer&utm_campaign=next_theme"
    target="_blank"
    rel="noopener noreferrer"
    className="font-medium text-neutral-900 underline-offset-4 hover:underline"
  >
    Beeclue Tech
  </a>
</p>
```
