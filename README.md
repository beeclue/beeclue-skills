# BeeClue Skills V2 — Commerce Design Intelligence

A production-grade, multi-industry, brand-aware **Creative + Commerce Design System** by **Beeclue Tech**. Built to generate distinctive, high-converting, accessible (WCAG 2.1 AA), and blazing fast WooCommerce digital flagships.

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

## 1. What Makes V2 Different

Most AI theme generators produce the same website repeatedly: white background, 3-column card grid, generic purple gradient, and cliché phrases like *"Elevate your experience"*.

BeeClue Skills V2 introduces a rigorous **Commerce Design Intelligence Pipeline**:
1. **Quantitative Brand DNA**: Encodes every brand into a normalized 0–100 coordinate vector across Positioning, Personality, Visual Tone, and Motion.
2. **Machine-Readable Design Contract**: Emits an unambiguous YAML contract before any template code is written.
3. **Multi-Industry Knowledge**: Deep domain blueprints across 30+ industries (Fine Jewelry, Skincare, Automotive, Furniture, Industrial B2B, Boutique Hotels, Gourmet Food, SaaS).
4. **15+ Composable Archetypes**: Directional aesthetic systems (Quiet Luxury, Editorial Luxury, Architectural Minimal, Technical Premium, Neo-Industrial, Clinical Premium, etc.).
5. **5-Layer Token Architecture**: Seamlessly connects strategy to styling (Brand DNA $\rightarrow$ Primitives $\rightarrow$ Semantics $\rightarrow$ Components $\rightarrow$ Experience Tokens).
6. **Independent Design Critic**: An objective evaluation engine scoring builds on an 11-vector, 100-point rubric (<70 Reject to 95+ Exceptional).

---

## 2. Directory Hierarchy

The entire V2 system is self-contained within `skills/beeclue-woocommerce-theme/`, allowing single-folder installation without polluting your agent's global skill registry:

```
beeclue-skills/
├── README.md
├── .gitignore
├── eval/                                         # Evaluation suites & diversity tests
│   ├── scenarios/
│   │   ├── luxury-jewelry.md
│   │   ├── premium-skincare.md
│   │   ├── automotive.md
│   │   └── b2b-industrial.md
│   └── cross-industry-diversity-test.md
│
├── docs/                                         # Architecture & tool specifications
│   └── mcp-specifications/
│       ├── beeclue-design-mcp.md
│       ├── beeclue-commerce-mcp.md
│       └── beeclue-visual-mcp.md
│
├── scripts/
│   └── validate-skills.py                       # Automated verification & linting suite
│
└── skills/
    └── beeclue-woocommerce-theme/
        ├── SKILL.md                              # Master Orchestrator (25-step execution pipeline)
        └── references/
            ├── brand/
            │   ├── brand-strategy.md             # Brand DNA 0–100 quantitative model
            │   ├── positioning.md                # Luxury vs Premium vs Accessible axes
            │   └── voice.md                      # Restrained editorial tone & anti-buzzword codex
            │
            ├── intelligence/
            │   ├── industries/                   # Deep domain profiles (Jewelry, Skincare, Automotive, etc.)
            │   ├── customer-behavior.md          # Purchase psychology & information requirements
            │   └── competitive-intelligence.md   # Competitor analysis & market differentiation
            │
            ├── design/
            │   ├── archetypes-library.md         # 15+ design archetypes & composable mixtures
            │   ├── luxury-definition.md          # Beyond black & gold: restraint, typography, whitespace
            │   ├── superclass-tokens.md          # 5-layer token template (strict CSS unit formatting)
            │   ├── typography.md                 # Fluid clamp scaling & authentic Google Font pairings
            │   ├── color-systems.md              # 60-30-10 palette architecture & WCAG contrast
            │   ├── layout-grids.md               # Asymmetric editorial splits & responsive grids
            │   ├── image-direction.md            # Structured photo briefs (lighting, crop, mood)
            │   ├── motion-personality.md         # Brand-aware motion & prefers-reduced-motion
            │   └── anti-generic-linter.md        # Linter against AI design clichés
            │
            ├── commerce/
            │   ├── strategy.md                   # Conditional feature enablement (shipping, urgency)
            │   ├── ecommerce-ux-patterns.md      # PDP sticky bar, AJAX drawer, variant swatches
            │   ├── product-discovery.md          # Faceted filtering, search overlays, card ergonomics
            │   └── cart-checkout.md              # Dynamic free shipping meter & in-drawer cross-sells
            │
            ├── wordpress/
            │   ├── wp-architecture.md            # Decision tree: Core vs Theme vs Blocks vs Plugins
            │   ├── theme-engineering.md          # Modular template-parts/ & functions.php architecture
            │   └── woocommerce-api.md            # WP-CLI automation & modern WooCommerce Store API
            │
            ├── quality/
            │   ├── visual-qa.md                  # Inspection loop (render, screenshot, patch)
            │   ├── a11y-wcag.md                  # WCAG 2.1 AA focus traps & screen-reader live regions
            │   ├── performance-cwv.md            # 90+ Core Web Vitals & critical CSS inlining
            │   ├── seo-schema.md                 # Complete JSON-LD (WebSite, Org, Product, FAQPage)
            │   └── design-critic.md              # 100-point rubric (<70 reject to 95+ exceptional)
            │
            ├── content/
            │   ├── brand-copy.md                 # Editorial copy rules & component microcopy
            │   └── content-strategy.md           # 7-chapter homepage narrative hierarchy
            │
            └── examples/
                └── lumiere-reasoning.md          # Case study in design reasoning (not a template)
```

---

## 3. The 25-Step Pipeline Overview

When invoked, the skill runs an autonomous 4-stage pipeline:

1. **Discovery & Intelligence**: Identifies industry dynamics, customer purchase friction, and competitive white space.
2. **Strategy & Architecture**: Computes 0–100 Brand DNA vectors, outputs the YAML Design Contract, and generates 5-layer design tokens.
3. **Technical Implementation**: Scaffolds modular `template-parts/`, authors the single-product sticky CTA bar, accessible variant swatches, dynamic AJAX cart drawer with free shipping calculation, and inlines critical CSS.
4. **Quality & Critic Gates**: Runs the Anti-Generic Linter, verifies WCAG 2.1 AA compliance, and submits the build to the Independent Design Critic.

---

## 4. Brand DNA & Design Contract Example

```yaml
brand_dna:
  positioning:
    luxury: 85
    premium: 90
    accessible: 20
  personality:
    sophistication: 90
    minimalism: 85
    warmth: 80
  visual:
    editorial: 85
    artisanal: 90
  motion:
    elegance: 95
    intensity: 30
```

---

## 5. Automated Verification & Testing

The repository includes an automated test runner validating frontmatter, reference paths, strict CSS unit formatting, and link integrity:

```bash
python3 scripts/validate-skills.py
```

---

## 6. Installation & Usage

To equip Claude Code, Gemini CLI, or any Antigravity-compatible agent with BeeClue Commerce Design Intelligence:

```bash
# Clone or copy into your agent's skills directory
cp -r skills/beeclue-woocommerce-theme ~/.gemini/config/skills/
```

### Trigger Phrases:
- `"create woocommerce theme"`
- `"superclass theme"`
- `"build wordpress store"`
- `"beeclue theme"`
- `"commerce design intelligence"`
- `"luxury woocommerce"`
- `"new client site"`

---

Website Designed & Developed by [Beeclue Tech](https://beeclue.com/?utm_source=skills_repo&utm_medium=readme&utm_campaign=open_source).
