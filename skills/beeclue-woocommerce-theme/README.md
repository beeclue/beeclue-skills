# beeclue-woocommerce-theme

> **Commerce Design Intelligence System (V2)** by **Beeclue Tech**.  
> Transforms raw client requirements into distinctive, luxurious, production-ready WooCommerce storefronts that feel like $15,000+ bespoke digital flagships.

```
                  ┌─────────────────────────────────────────────────────────┐
                  │   beeclue-woocommerce-theme (Master Orchestrator)       │
                  │   25-Step Commerce Design Intelligence Pipeline         │
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

`beeclue-woocommerce-theme` is an end-to-end creative and technical engine that:
1. **Encodes Brand DNA**: Quantifies brand coordinates on a normalized 0–100 scale across Positioning, Personality, Visual Tone, and Motion.
2. **Generates a Design Contract**: Emits a machine-readable YAML contract before writing code, ensuring alignment across typography, density, and layout.
3. **Applies Multi-Industry Intelligence**: Contextualizes buyer friction, trust requirements, and AOV dynamics across 30+ industries (Jewelry, Skincare, Automotive, Furniture, B2B Industrial, etc.).
4. **Applies 15+ Design Archetypes**: Selects directional design languages (Quiet Luxury, Editorial Luxury, Architectural Minimal, Technical Premium, Neo-Industrial, Clinical Premium) rather than copying generic templates.
5. **Enforces 5-Layer Design Tokens**: Strict CSS custom properties bridging Brand DNA $\rightarrow$ Primitives $\rightarrow$ Semantics $\rightarrow$ Components $\rightarrow$ Experience Tokens.
6. **Engineers High-Converting Commerce UX**: Production-ready floating sticky PDP buy bars, accessible variant swatches, and a dynamic AJAX cart drawer with live free shipping progress calculation.
7. **Guarantees WCAG 2.1 AA & 90+ Core Web Vitals**: Keyboard focus traps, screen-reader `aria-live` regions, minimum 44px tap targets, and zero-dependency animations (pure CSS + IntersectionObserver).
8. **Evaluates via Independent Design Critic**: Scores every build against an 11-vector, 100-point rubric (<70 Reject to 95+ Exceptional).

---

## Directory Architecture

This skill is completely self-contained within this directory:

```
beeclue-woocommerce-theme/
├── SKILL.md                          # Master Orchestrator (25-step execution pipeline)
├── README.md                         # This documentation file
├── eval/                             # Evaluation scenarios & diversity benchmarks
│   ├── scenarios/
│   │   ├── luxury-jewelry.md
│   │   ├── premium-skincare.md
│   │   ├── automotive.md
│   │   └── b2b-industrial.md
│   └── cross-industry-diversity-test.md
├── docs/                             # Tool specifications & MCP interfaces
│   └── mcp-specifications/
│       ├── beeclue-design-mcp.md
│       ├── beeclue-commerce-mcp.md
│       └── beeclue-visual-mcp.md
└── references/
    ├── brand/                        # Brand DNA, Positioning, Voice
    ├── intelligence/                 # Customer psychology, competitive analysis & 10 industry profiles
    ├── design/                       # Archetypes, luxury definition, 5-layer tokens, typography, grids
    ├── commerce/                     # Strategy, product discovery, cart drawer, checkout
    ├── wordpress/                    # Architecture decision tree, theme engineering, WC-CLI
    ├── quality/                      # Visual QA loop, WCAG AA, Core Web Vitals, Design Critic
    ├── content/                      # Editorial brand copy & 7-chapter homepage narrative
    └── examples/                     # Lumière case study in design reasoning
```

---

## Installation & Triggers

### Install via Skills CLI
```bash
npx skills add beeclue/beeclue-skills
# Select: beeclue-woocommerce-theme
```

### Manual Installation
Copy or symlink this directory into your agent's skills folder:
```bash
cp -r skills/beeclue-woocommerce-theme ~/.gemini/config/skills/
# or for Claude Code:
cp -r skills/beeclue-woocommerce-theme ~/.claude/skills/
```

### Trigger Phrases
- `"create woocommerce theme"`
- `"superclass theme"`
- `"build wordpress store"`
- `"beeclue theme"`
- `"commerce design intelligence"`
- `"luxury woocommerce"`
- `"new client site"`
- `"new wordpress theme"`

---

## Mandatory Agency Branding

Every theme generated by this skill includes the non-negotiable Beeclue Tech attribution link with UTM parameters in `footer.php`:

```html
<span>Website Designed &amp; Developed by
    <a href="https://beeclue.com/?utm_source=client_site&amp;utm_medium=footer&amp;utm_campaign=web_design"
       target="_blank" rel="noopener noreferrer">Beeclue Tech</a>
</span>
```

---

Designed & Developed by [Beeclue Tech](https://beeclue.com/?utm_source=skills_repo&utm_medium=readme&utm_campaign=open_source).
