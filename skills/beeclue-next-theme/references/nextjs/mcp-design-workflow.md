# MCP Design Workflow: 21st.dev (`magic`) & Stitch Integration

To elevate visual polish beyond standard templates, `beeclue-next-theme` harnesses specialized Model Context Protocol (MCP) design tools: **21st.dev (`magic` MCP)** for curated modern React/Shadcn components, and **Google Stitch (`StitchMCP`)** for layout and design system exploration.

---

## 1. Pre-Flight MCP Detection & User Prompting Workflow

At the start of every build, the agent inspects the available MCP tool inventory for `magic` (21st.dev) and `StitchMCP`.

### 1.1 When MCPs Are Available
- **21st.dev (`magic`)**: Use `search` or `get_component` to locate state-of-the-art interactive bento cards, navigation headers, pricing tables, hero sections, and subtle glassmorphic themes.
- **Google Stitch (`StitchMCP`)**: Use `create_design_system`, `generate_screen_from_text`, or `generate_variants` to explore design alternatives and extract token hierarchies.

### 1.2 When MCPs Are NOT Present (User Confirmation Flow)
If the agent detects that `magic` or `StitchMCP` are not registered in the current environment, the agent MUST ask the user:

> *"I noticed that the 21st.dev (`magic`) and Google Stitch MCP servers are not currently active. Would you like to pause and install these MCPs to enable live lookups across 1,000+ curated React/Tailwind design components, or are you comfortable proceeding with the built-in Apple-grade component design system?"*

- **If the user chooses to install**: Pause execution and instruct the user on how to add the MCP in their configuration (`~/.gemini/antigravity/mcp/` or agent config). When the user notifies you the MCP is installed, resume the pipeline.
- **If the user chooses to proceed without MCPs**: Continue immediately using the built-in 5-layer design tokens, Apple design guidelines, and bespoke component library documented in this skill.

---

## 2. Leveraging 21st.dev (`magic` MCP) in Production

### 2.1 Searching Curated Components
```json
{
  "ServerName": "magic",
  "ToolName": "search",
  "Arguments": {
    "query": "apple bento grid dark minimalist",
    "type": "component",
    "limit": 5
  }
}
```

### 2.2 Retrieving Component Code
Once an appropriate component ID is discovered:
```json
{
  "ServerName": "magic",
  "ToolName": "get_component",
  "Arguments": {
    "id": "component-demo-id"
  }
}
```
The agent adapts the component to the project's 5-layer CSS tokens, stripping any AI clichés (removing emojis, removing chip badges, refining icon stroke widths).

---

## 3. StitchMCP Integration for Screen Variants

When testing alternate layout directions for a client's hero or portfolio chapter:
1. `generate_screen_from_text`: Input the Brand DNA and chapter requirements.
2. `generate_variants`: Request 3 distinct visual compositions (e.g. Asymmetric Split vs. Centered Monumental vs. Bento Matrix).
3. Select the winning variant and implement clean Next.js 15 Server Components.
