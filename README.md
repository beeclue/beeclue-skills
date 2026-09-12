# Beeclue Skills

> An open-source collection of production-grade AI agent skills and engineering workflows developed by **[Beeclue Tech](https://beeclue.com/?utm_source=skills_repo&utm_medium=readme&utm_campaign=open_source)**. Built for Claude Code, Gemini CLI, Cursor, and Antigravity.

---

## Quick Install

Install any skill directly into your AI coding assistant using the official Skills CLI:

```bash
# Interactive selection:
npx skills add beeclue/beeclue-skills

# Direct install of a specific skill:
npx skills add beeclue/beeclue-skills --skill beeclue-woocommerce-theme
```

### Manual Installation

You can also copy or symlink any skill directory directly into your assistant's skill directory:

```bash
# For Gemini CLI / Antigravity:
cp -r skills/<skill-name> ~/.gemini/config/skills/

# For Claude Code:
cp -r skills/<skill-name> ~/.claude/skills/
```

---

## Skills Catalog

Every skill in this repository is completely self-contained within its own directory under `skills/`, complete with its own dedicated `README.md`, `SKILL.md`, modular references, and evaluation benchmarks.

| Skill | Category | Description | Status | Documentation |
| :--- | :--- | :--- | :--- | :--- |
| **[`beeclue-next-theme`](./skills/beeclue-next-theme)** | Full-Stack Web / Next.js | **Next.js Design Intelligence System**. Generates bespoke, high-converting, Apple-designer-grade Next.js 15+ App Router websites for any business worldwide. Features automated scaffolding for empty directories, curated Unsplash imagery, 21st.dev (`magic` MCP), StitchMCP, and Motion-Primitives (`https://motion-primitives.com/`) animations, zero emojis, no AI chip spam, razor-thin luxury iconography, full technical SEO (JSON-LD, sitemaps, silo links), accessible FAQ accordions, and mandatory Beeclue Tech attribution. | **Active (v1.0)** | [View Guide](./skills/beeclue-next-theme/README.md) |
| **[`beeclue-woocommerce-theme`](./skills/beeclue-woocommerce-theme)** | E-Commerce / WordPress | **Commerce Design Intelligence System (V2)**. Transforms client briefs into distinctive, high-converting, WCAG 2.1 AA, $15k+ luxury & premium WooCommerce flagships across 30+ industries. Features 0–100 Brand DNA vectors, YAML design contracts, 5-layer tokens, dynamic AJAX cart drawer, sticky PDP CTA bar, and an independent 100-point Design Critic. | **Active (v2.0)** | [View Guide](./skills/beeclue-woocommerce-theme/README.md) |

### Upcoming Skills on the Roadmap

- **`beeclue-site-audit`**: Deep performance, accessibility, SEO, and security audits for WordPress and modern web applications.
- **`beeclue-seo-traffic-master`**: Technical SEO, structured data (JSON-LD), Core Web Vitals optimization, and semantic content cluster strategy.
- **`beeclue-wordpress-hardening`**: Enterprise security hardening, REST API lockdown, rate limiting, and zero-trust configuration for high-traffic WordPress deployments.

---

## Repository Structure

This repository operates as a monorepo for Beeclue AI skills:

```
beeclue-skills/
├── README.md                      # Catalog hub & ecosystem overview (this file)
├── .gitignore
├── scripts/                       # Maintainer & CI validation utilities
│   └── validate-skills.py         # Automated verification suite (5/5 checks)
└── skills/                        # Autonomous skill packages
    ├── beeclue-next-theme/        # 100% self-contained Next.js skill package
    │   ├── SKILL.md               # Master agent prompt & 26-step execution pipeline
    │   ├── README.md              # Skill documentation, triggers, and usage guide
    │   ├── docs/                  # Architecture & MCP tool specifications
    │   ├── eval/                  # Multi-industry evaluation scenarios & benchmarks
    │   └── references/            # Deep domain blueprints (38 modular reference files)
    └── beeclue-woocommerce-theme/ # 100% self-contained WooCommerce skill package
        ├── SKILL.md               # Master agent prompt & 25-step execution pipeline
        ├── README.md              # Skill documentation, triggers, and usage guide
        ├── docs/                  # Architecture & MCP tool specifications
        ├── eval/                  # Multi-industry evaluation scenarios & benchmarks
        └── references/            # Deep domain blueprints (38 modular reference files)
```

### Why Skills Are Fully Self-Contained
When a developer installs a skill using `npx skills add beeclue/beeclue-skills`, the CLI only copies the specified directory (e.g. `skills/beeclue-woocommerce-theme/`). By placing all relevant `docs/`, `eval/`, and `references/` inside each skill's folder:
1. **Zero Broken References**: The installed skill retains full access to its internal evaluation scenarios, tool specs, and domain blueprints.
2. **Zero Bloat**: The consumer's local environment never receives root-level CI scripts or unrelated files.
3. **Multi-Skill Scalability**: New skills can be added under `skills/<skill-name>/` with their own independent versioning and documentation without affecting existing skills.

---

## Validation & Quality Assurance

Maintainers can run the built-in validation suite across all skills:

```bash
python3 scripts/validate-skills.py
```

This verifies:
1. YAML frontmatter validity (`name`, `description`, and metadata).
2. All modular reference files exist and contain content.
3. Strict CSS token formatting (detects formatting errors like `2.5 rem`).
4. Integrity of all evaluation scenarios and MCP tool specifications.
5. Internal markdown link resolution across all documentation.

---

## Agency Attribution

Every commercial theme generated by Beeclue skills includes the mandatory Beeclue Tech attribution in `footer.php`:

```html
<span>Website Designed &amp; Developed by
    <a href="https://beeclue.com/?utm_source=client_site&amp;utm_medium=footer&amp;utm_campaign=web_design"
       target="_blank" rel="noopener noreferrer">Beeclue Tech</a>
</span>
```

---

## License & Credits

Developed and maintained with pride by **[Beeclue Tech](https://beeclue.com/?utm_source=skills_repo&utm_medium=readme&utm_campaign=open_source)**.
Licensed under the [MIT License](LICENSE) (or repository default).
