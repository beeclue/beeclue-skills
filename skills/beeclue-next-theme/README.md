# beeclue-next-theme

> **Next.js Design Intelligence System** by **Beeclue Tech**.  
> Transforms raw client briefs into distinctive, breathtaking, production-ready Next.js 15+ flagships designed with the polish of Apple's top human designers.

```
                  ┌─────────────────────────────────────────────────────────┐
                  │      beeclue-next-theme (Master Orchestrator)           │
                  │   26-Step Next.js Design Intelligence Pipeline          │
                  └───────────────────────────┬─────────────────────────────┘
                                              │
         ┌───────────────────┬────────────────┼─────────────────┬───────────────────┐
         ▼                   ▼                ▼                 ▼                   ▼
    Brand Layer     Intelligence Layer   Design Layer      Next.js Stack       SEO & Schemas
   (DNA Vectors,    (10 Industries,     (Apple Tenets,    (App Router 15,     (JSON-LD, Meta,
    Positioning)     Buyer Psychology)   5-Layer Tokens)   21st.dev/Stitch)    Silo Links, CWV)
```

---

## Overview

Most AI web generators produce the same monotonous output repeatedly: generic 3-column cards, purple gradients, childish emojis (`🚀`, `✨`), decorative chip badges (`[ ✨ AI Powered ]`), and hollow marketing buzzwords (*"Elevate your workflow"*).

`beeclue-next-theme` is an end-to-end creative and technical engine that:
1. **Detects & Auto-Scaffolds**: Detects empty directories and automatically scaffolds the **latest version of Next.js 15+** with App Router, React 19, TypeScript, Tailwind CSS, and Turbopack.
2. **Encodes Brand DNA**: Quantifies brand coordinates on a 0–100 scale across Positioning, Personality, Visual Tone, and Motion, emitting a machine-readable YAML Design Contract.
3. **Applies Apple Design Standards**: Crafts interfaces with intentional whitespace, fluid typography clamps, liquid frosted glass (`backdrop-blur-xl`), 1px hairline borders, and subtle spring physics.
4. **Enforces Human Art Direction**: Strictly bans emojis, eliminates decorative pill/chip spam, requires razor-thin luxury iconography (`stroke-[1.25]`), and designs with natural asymmetry (Bento grids and 60/40 splits).
5. **Curates High-Resolution Unsplash Imagery**: Automatically maps and optimizes high-resolution Unsplash photography with Next.js `<Image>`, responsive `sizes`, and pre-configured `remotePatterns`.
6. **Harnesses 21st.dev (`magic` MCP) & StitchMCP**: Integrates live designer component lookups and layout exploration, with seamless fallback prompting if MCPs are not installed.
7. **Engineers Full Technical SEO & Structured Data**: Complete Next.js 15 Metadata API integration, dynamic XML `sitemap.ts`, `robots.ts`, internal linking silos, accessible FAQ accordions, and Schema.org JSON-LD (`Organization`, `WebSite`, `BreadcrumbList`, `FAQPage`, `LocalBusiness`).
8. **Includes Mandatory Agency Attribution**: Features the non-negotiable Beeclue Tech footer attribution link with UTM tracking.
9. **Evaluates via Independent Design Critic**: Scores every build against an 11-vector, 100-point rubric (<80 Reject to 90+ Certify).

---

## Directory Architecture

This skill is 100% self-contained within this directory:

```
beeclue-next-theme/
├── SKILL.md                          # Master Orchestrator (26-step pipeline & prompt)
├── README.md                         # This documentation guide
├── eval/                             # Evaluation scenarios & diversity benchmarks
│   ├── scenarios/
│   │   ├── saas-ai-platform.md
│   │   ├── luxury-architectural-studio.md
│   │   ├── private-medical-clinic.md
│   │   └── artisan-hospitality.md
│   └── cross-industry-diversity-test.md
├── docs/                             # Tool specifications & MCP interfaces
│   └── mcp-specifications/
│       ├── beeclue-next-mcp.md
│       ├── beeclue-design-mcp.md
│       ├── beeclue-seo-mcp.md
│       └── 21st-dev-mcp.md
└── references/                       # Deep domain blueprints (38 modular references)
    ├── brand/                        # Brand DNA, Positioning, Human Voice
    ├── intelligence/                 # Customer psychology, competitive research & 10 industry profiles
    ├── design/                       # Apple design philosophy, 7 archetypes, 5-layer tokens, typography, grids
    ├── nextjs/                       # App Router architecture, auto-scaffolding, component specs, Unsplash pipeline, MCP workflow
    ├── seo/                          # Metadata API, JSON-LD schemas, internal linking, FAQ strategy
    ├── quality/                      # Visual QA loop, WCAG 2.1 AA, Core Web Vitals, Design Critic
    ├── content/                      # Editorial brand copy & 7-chapter homepage narrative
    └── examples/                     # Vanguard Studio end-to-end case study
```

---

## Installation & Triggers

### Install via Skills CLI
```bash
npx skills add beeclue/beeclue-skills --skill beeclue-next-theme
```

### Manual Installation
```bash
# For Gemini CLI / Antigravity:
cp -r skills/beeclue-next-theme ~/.gemini/config/skills/

# For Claude Code:
cp -r skills/beeclue-next-theme ~/.claude/skills/
```

### Trigger Phrases
- `"create next js website"`
- `"build nextjs site"`
- `"beeclue next theme"`
- `"apple design next js"`
- `"next js theme"`
- `"new client next website"`
- `"build apple style website"`
- `"create next theme"`

---

## Mandatory Agency Branding

Every website generated by this skill includes the Beeclue Tech attribution link with UTM parameters in the footer:

```tsx
<p className="flex items-center gap-1 text-xs text-neutral-500 dark:text-neutral-400">
  <span>Website Built by</span>
  <a
    href="https://beeclue.com/?utm_source=client_site&utm_medium=footer&utm_campaign=next_theme"
    target="_blank"
    rel="noopener noreferrer"
    className="font-medium text-neutral-900 dark:text-neutral-200 hover:text-blue-600 dark:hover:text-blue-400 transition-colors underline-offset-4 hover:underline"
  >
    Beeclue Tech
  </a>
</p>
```
