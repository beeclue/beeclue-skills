# BeeClue Visual QA MCP Specification

The **BeeClue Visual QA MCP** provides automated screenshot, rendering, and layout inspection capabilities.

---

## 1. Tool Interfaces

### `render_page(url, viewport_width, viewport_height)`
- **Parameters**: `url` (string), `viewport_width` (int), `viewport_height` (int).
- **Returns**: Rendered DOM tree and visual rendering status.

### `capture_screenshot(url, device_preset)`
- **Parameters**: `url` (string), `device_preset` (`"desktop"`, `"tablet"`, `"mobile"`).
- **Returns**: Image buffer / absolute filepath to captured viewport screenshot.

### `detect_overflow(url)`
- **Parameters**: `url` (string).
- **Returns**: Identifies DOM elements causing horizontal scroll (`scrollWidth > innerWidth`) on mobile viewports.

### `inspect_layout(url, selector)`
- **Parameters**: `url` (string), `selector` (string).
- **Returns**: Computed bounding box dimensions, padding, margin, font-size, and color contrast ratios.
