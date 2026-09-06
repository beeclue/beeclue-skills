# Tool Specification: 21st.dev (`magic` MCP) & Stitch Integration

The 21st.dev (`magic`) MCP and Google Stitch (`StitchMCP`) tools empower agents to look up high-polish React/Shadcn components, theme colors, and layout variants directly from curated designer libraries.

---

## 1. 21st.dev (`magic` MCP) Interface

### `search`
Search across React/Shadcn components, themes, and templates on 21st.dev.
- `query` (string): Search query (e.g. `"bento grid minimalist dark"`, `"pricing table apple"`).
- `type` (enum: `component` | `theme` | `template` | `all`): Type filter.

### `get_component`
Fetches the complete JSX/TSX and Tailwind implementation code for a discovered component ID.
- `id` (string): Component demo identifier.

---

## 2. Google Stitch (`StitchMCP`) Interface

### `generate_screen_from_text`
Generates initial UI layouts and screen representations from client prompts.

### `generate_variants`
Explores visual permutations of a screen (e.g., contrasting hero alignments, color palettes).
