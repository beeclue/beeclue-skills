# Tool Specification: `beeclue-seo-mcp`

The `beeclue-seo-mcp` specification defines the tool interface for generating technical SEO metadata, XML sitemaps, robots.txt directives, and JSON-LD structured schemas for Next.js.

---

## 1. Tool Endpoints

### `generate_jsonld_schemas`
Generates syntactically validated Schema.org JSON-LD definitions based on the business category (`Organization`, `LocalBusiness`, `MedicalClinic`, `Restaurant`, `ArchitecturalFirm`, `SoftwareApplication`, `FAQPage`, `BreadcrumbList`).

### `generate_sitemap_routes`
Analyzes the page tree and dynamic route handlers to generate `src/app/sitemap.ts` and `src/app/robots.ts`.
