# Tool Specification: `beeclue-next-mcp`

The `beeclue-next-mcp` specification defines the tool interface for autonomous Next.js project detection, scaffolding, and App Router configuration.

---

## 1. Tool Endpoints

### `scaffold_next_project`
Detects if the target directory is empty or lacks a Next.js setup, determines the latest available version of Next.js from npm, and runs `create-next-app` with App Router, TypeScript, and Tailwind CSS.

- **Parameters**:
  - `target_dir` (string): Directory path to initialize.
  - `package_manager` (enum: `npm` | `pnpm` | `yarn` | `bun`): Default `npm`.
  - `install_core_utilities` (boolean): Default `true` (`lucide-react`, `clsx`, `tailwind-merge`).

### `configure_unsplash_remote_patterns`
Injects or updates `next.config.ts` to allow high-resolution image rendering from `images.unsplash.com`.

- **Parameters**:
  - `project_path` (string): Absolute path to project root.
