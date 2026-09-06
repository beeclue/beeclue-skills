# BeeClue Design MCP Specification

The **BeeClue Design MCP** provides programmatic tools and resources for design intelligence, token synthesis, and automated contrast/quality evaluation.

---

## 1. Resources

- `design://archetypes`: Catalogs all 15+ design archetypes with characteristic parameters.
- `design://industries`: Returns structured profiles, customer psychology, and UX rules for 30+ industries.
- `design://tokens`: Token schema specifications for the 5-layer hierarchy.
- `design://typography`: Curated Google Font pairings, weights, and clamp formulas.
- `design://color`: Industry-verified 60-30-10 color palettes with contrast ratios.
- `design://anti-patterns`: Codex of banned generic AI design clichés and buzzwords.

---

## 2. Tool Interfaces

### `generate_design_direction(brand_dna)`
- **Parameters**: `brand_dna` (object matching the 0–100 Brand DNA schema).
- **Returns**: Recommended primary archetype, secondary hybrid, color strategy, and typography system.

### `generate_tokens(design_contract)`
- **Parameters**: `design_contract` (validated YAML/JSON design contract).
- **Returns**: Syntactically valid CSS custom properties with strict unit formatting (e.g., `2.5rem`, `16px`).

### `validate_tokens(css_content)`
- **Parameters**: `css_content` (string containing CSS custom properties).
- **Returns**: Boolean `valid`, list of formatting errors (e.g. detects spaces like `2.5 rem`), and missing semantic layers.

### `score_design(design_contract, rendered_dom)`
- **Parameters**: `design_contract`, `rendered_dom`.
- **Returns**: 100-point rubric breakdown across the 11 quality vectors.
