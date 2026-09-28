# Automated Codebase Reconnaissance & Inspection Tooling

Use these battle-tested terminal commands to perform non-invasive, read-only reconnaissance across any web project during the audit phase.

---

## 1. Framework & Engine Detection

```bash
# Detect project type, package manager, and build tools
ls -la package.json pnpm-lock.yaml yarn.lock package-lock.json bun.lockb composer.json Gemfile 2>/dev/null

# Detect Frontend Framework
grep -E '"(next|react|vue|nuxt|svelte|@sveltejs/kit|astro|remix|gatsby|@angular/core)"' package.json 2>/dev/null

# Detect CMS & Backend
ls -la wp-config.php app/Http/Kernel.php config/routes.rb 2>/dev/null
```

---

## 2. Complete Route Inventory Discovery

### Next.js (App Router)
```bash
find app src/app -name "page.tsx" -o -name "page.jsx" -o -name "page.js" -o -name "route.ts" 2>/dev/null | sort
```

### Next.js (Pages Router)
```bash
find pages src/pages -name "*.tsx" -o -name "*.jsx" -o -name "*.js" 2>/dev/null | grep -Ev "(_app|_document|_error|api/)" | sort
```

### Astro & SvelteKit
```bash
find src/pages src/routes -name "*.astro" -o -name "+page.svelte" 2>/dev/null | sort
```

### Nuxt.js
```bash
find pages -name "*.vue" 2>/dev/null | sort
```

### WordPress (Theme Templates)
```bash
find wp-content/themes -name "*.php" 2>/dev/null | grep -Ev "(vendor/|node_modules/|inc/)" | sort
```

### Static HTML / Multi-Page Apps
```bash
find . -maxdepth 3 -name "*.html" 2>/dev/null | grep -Ev "(node_modules|\.git|dist|build|\.next)" | sort
```

---

## 3. Lead Capture & Form Extraction

Find every form element, submission handler, and input field across the codebase:

```bash
# Locate all form elements and hook integrations
grep -rn -E "(<form|useForm|handleSubmit|onSubmit|register\(|Formik|react-hook-form|Netlify|action=)" \
  --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --include="*.php" . \
  | grep -Ev "(node_modules|\.next|dist|vendor)" | head -40

# Count input elements per file to locate high-friction forms
grep -rn -E "(<input|<Input|<TextField|<textarea|<select)" \
  --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --include="*.php" . \
  | grep -Ev "(node_modules|\.next|dist|vendor)" | cut -d: -f1 | sort | uniq -c | sort -nr | head -20
```

---

## 4. CTA & Button Inventory Extraction

Extract button and CTA anchor texts and their target destinations:

```bash
# Find high-intent button and link CTAs
grep -rn -E "(<button|<Button|<a.*href=|<Link.*href=)" \
  --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" --include="*.html" --include="*.php" . \
  | grep -iE "(contact|demo|trial|start|schedule|book|buy|quote|pricing|join|register|download|audit)" \
  | grep -Ev "(node_modules|\.next|dist|vendor)" | head -40
```

---

## 5. Analytics, Tracking & CRM Tag Audit

Inspect the codebase for analytics tracking scripts, pixels, and tag managers:

```bash
grep -rn -E "(gtag|GTM-|analytics\.js|fbq\(|linkedin_data_partner_id|posthog|segment|clarity|hotjar|plausible|mixpanel|fathom|heap|hubspot)" \
  --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --include="*.html" --include="*.php" . \
  | grep -Ev "(node_modules|\.next|dist|vendor)" | head -30
```

---

## 6. SEO & Metadata Verification

Check for metadata tags, OpenGraph, dynamic sitemaps, and robots configuration:

```bash
# Check Next.js App Router metadata definitions
grep -rn -E "(export const metadata|generateMetadata)" \
  --include="*.tsx" --include="*.ts" --include="*.jsx" . 2>/dev/null

# Check HTML title and meta descriptions
grep -rn -E "(<title|<meta name=\"description\"|og:title|og:description|robots\.txt|sitemap\.xml)" \
  --include="*.html" --include="*.php" --include="*.tsx" . 2>/dev/null | grep -Ev "(node_modules|\.next)" | head -25

# Check Schema.org JSON-LD structured data
grep -rn "application/ld+json" --include="*.tsx" --include="*.jsx" --include="*.html" --include="*.php" . 2>/dev/null
```

---

## 7. Performance & Image Asset Audit

Detect heavy, unoptimized assets and layout-shift triggers:

```bash
# Find oversized images (>500KB) in public directory
find public assets static -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.gif" \) -size +500k 2>/dev/null

# Check for non-standard image tags (raw <img> without Next/Image or lazy loading)
grep -rn "<img" --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.svelte" . \
  | grep -Ev "(node_modules|\.next|dist)" | head -25
```
