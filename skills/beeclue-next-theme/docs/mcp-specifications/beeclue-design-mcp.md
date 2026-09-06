# Tool Specification: `beeclue-design-mcp`

The `beeclue-design-mcp` specification defines the tool interface for computing Brand DNA coordinates, synthesizing YAML design contracts, and generating 5-layer CSS tokens.

---

## 1. Tool Endpoints

### `synthesize_brand_dna`
Translates qualitative client questionnaires into a normalized 0–100 coordinate vector across Positioning, Personality, Visual Tone, and Motion.

- **Parameters**:
  - `industry` (string): Target industry or vertical.
  - `target_audience` (string): Description of primary buyer persona.
  - `aesthetic_preference` (string): Stated visual references or mood.

### `generate_design_contract`
Outputs the canonical YAML Design Contract specifying typography scales, 60-30-10 palette hex codes, card corner radii, and container dimensions.
