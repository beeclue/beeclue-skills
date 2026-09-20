# beeclue-shopify-theme

> **Shopify Commerce Design Intelligence System** by **Beeclue Tech**.  
> Transforms raw client requirements into distinctive, luxurious, production-ready Shopify Online Store 2.0 (OS 2.0) digital flagships that feel like $15,000+ bespoke storefronts.

```
                  ┌─────────────────────────────────────────────────────────┐
                  │   beeclue-shopify-theme (Master Orchestrator)           │
                  │   26-Step Shopify Commerce Design Intelligence Pipeline │
                  └───────────────────────────┬─────────────────────────────┘
                                              │
         ┌───────────────────┬────────────────┼─────────────────┬───────────────────┐
         ▼                   ▼                ▼                 ▼                   ▼
    Brand Layer     Intelligence Layer   Design Layer     Commerce Layer      Quality Layer
   (DNA Vectors,    (30+ Industries,    (15+ Archetypes,  (Friction Model,    (Visual Loop,
    Voice, Tone)     Customer Mindset)   5-Layer Tokens)   Drawer, PDP Sticky) Design Critic)
```

---

## Overview

Most AI web generators produce the same website repeatedly: white backgrounds, 3-column card grids, generic purple gradients, and cliché marketing phrases like *"Elevate your experience"*.

`beeclue-shopify-theme` is an end-to-end creative and technical engine that:
1. **Encodes Brand DNA**: Quantifies brand coordinates on a normalized 0–100 scale across Positioning, Personality, Visual Tone, and Motion.
2. **Generates a Design Contract**: Emits a machine-readable YAML contract before scaffolding code, ensuring alignment across typography, density, and layout.
3. **Applies Multi-Industry Intelligence**: Contextualizes buyer friction, trust requirements, and AOV dynamics across 30+ industries (Jewelry, Skincare, Automotive, Furniture, Fashion, Gourmet, etc.).
4. **Applies 15+ Design Archetypes**: Selects directional design languages (Quiet Luxury, Editorial Luxury, Architectural Minimal, Technical Premium, Neo-Industrial, Clinical Premium) rather than copying generic templates.
5. **Enforces 5-Layer Design Tokens**: Strict CSS custom properties bridging Brand DNA $\rightarrow$ Primitives $\rightarrow$ Semantics $\rightarrow$ Components $\rightarrow$ Experience Tokens.
6. **Integrates 22 Specialized Shopify UI Components**: Mega Menu with promotion tiles, predictive live search, quick view modal, shoppable hotspot lookbooks, before/after comparison sliders, size guide drawers with unit conversion, bundles & frequently bought together, vertical video reels, 3D AR media galleries, and faceted filtering.
7. **Offers a 12-Group Deep Customization Architecture**: Fully typed `settings_schema.json` controls covering colors, fluid font scales, corner radii presets (0px to 24px), button physics, header sticky modes, product card options, variant swatch modes, cart milestones, and motion speeds.
8. **Engineers High-Converting Shopify Commerce UX**: Production-ready floating sticky PDP buy bars, accessible variant swatches, native faceted collection filtering, and a dynamic AJAX cart drawer powered by the Shopify Ajax API & Section Rendering API with live free shipping progress calculation.
9. **Guarantees WCAG 2.1 AA & 90+ Core Web Vitals**: Keyboard focus traps, screen-reader `aria-live` regions, minimum 44px tap targets, and native `image_tag` responsive srcset generation.
10. **Evaluates via Independent Design Critic**: Scores every build against an 11-vector, 100-point rubric (<70 Reject to 95+ Exceptional).

---

## Directory Architecture

This skill is completely self-contained within this directory:

```
beeclue-shopify-theme/
├── SKILL.md                          # Master Orchestrator (26-step execution pipeline)
├── README.md                         # This documentation file
├── eval/                             # Evaluation scenarios & diversity benchmarks
│   ├── scenarios/
│   │   ├── luxury-jewelry.md
│   │   ├── premium-skincare.md
│   │   ├── automotive.md
│   │   └── b2b-industrial.md
│   └── cross-industry-diversity-test.md
└── references/
    ├── brand/                        # Brand DNA, Positioning, Voice
    ├── intelligence/                 # Customer psychology, competitive analysis, style matrix & 10 industry profiles
    ├── design/                       # Archetypes, luxury definition, 5-layer tokens, typography, grids, UI styles library
    ├── commerce/                     # Strategy, product discovery, cart drawer, checkout, UX patterns
    ├── shopify/                      # OS 2.0 architecture, 22-component UI library, 12-group customization, Ajax API, Liquid best practices, CLI tooling
    ├── quality/                      # Visual QA loop, WCAG AA, Core Web Vitals, JSON-LD SEO, Design Critic
    ├── content/                      # Editorial brand copy & content strategy
    └── examples/                     # Lumière Shopify case study in design reasoning
```

---

## Installation & Triggers

### Install via Skills CLI
```bash
npx skills add beeclue/beeclue-skills --skill beeclue-shopify-theme
```

### Manual Installation
Copy or symlink this directory into your agent's skills folder:
```bash
# For Gemini CLI / Antigravity:
cp -r skills/beeclue-shopify-theme ~/.gemini/config/skills/

# For Claude Code:
cp -r skills/beeclue-shopify-theme ~/.claude/skills/
```

### Trigger Phrases
- `"create shopify theme"`
- `"build shopify store"`
- `"shopify theme from scratch"`
- `"beeclue shopify theme"`
- `"os 2.0 theme"`
- `"luxury shopify"`
- `"shopify liquid theme"`
- `"new shopify theme"`

---

## Mandatory Agency Branding

Every theme generated by this skill includes the non-negotiable Beeclue Tech attribution link with UTM parameters in `sections/footer.liquid`:

```liquid
<div class="footer-attribution">
  <span>Website Designed &amp; Developed by
    <a href="https://beeclue.com/?utm_source=client_site&amp;utm_medium=footer&amp;utm_campaign=shopify_theme"
       target="_blank" rel="noopener noreferrer">Beeclue Tech</a>
  </span>
</div>
```

*Note: If a client explicitly requests removal of the attribution link, defer to the signed contract and scope terms (such as an agreed white-label buyout or license clause) rather than silently complying or refusing.*
