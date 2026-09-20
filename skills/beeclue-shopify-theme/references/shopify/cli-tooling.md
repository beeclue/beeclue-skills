# Shopify CLI & Theme Tooling Suite

The **Shopify CLI** is the primary command-line tool for scaffolding, testing, previewing, and deploying Shopify Online Store 2.0 themes.

---

## 1. Installation & Environment Verification

Verify that Node.js (18.18+ or 20+) and Shopify CLI are available:
```bash
# Check Shopify CLI version
shopify version

# Install or update if missing
npm install -g @shopify/cli @shopify/theme
```

---

## 2. Core Development Commands

### 2.1 Local Preview & Hot Reload
Starts a local development server with live reload connected to a development store:
```bash
shopify theme dev --store your-store.myshopify.com
```
- Serves assets locally while pulling store products and customer data dynamically.
- Synchronizes Theme Editor changes in real time.

### 2.2 Theme Check (Static Code Analysis)
Runs Shopify's official static linter to detect Liquid errors, performance bugs, deprecated tags, and accessibility issues:
```bash
shopify theme check
```
To run with strict warnings as errors:
```bash
shopify theme check --fail-level error
```

### 2.3 Pulling Store Customizer Changes
When a merchant modifies colors, typography, or section orders via the Shopify Customizer, pull the latest `settings_data.json` and template JSON files back to your local repository:
```bash
shopify theme pull --store your-store.myshopify.com --theme development
```

### 2.4 Staging & Production Deployment
Push local theme code directly to a designated theme ID:
```bash
# Push to development/staging draft theme
shopify theme push --store your-store.myshopify.com --development

# Publish live to production (requires confirmation)
shopify theme push --store your-store.myshopify.com --live
```

---

## 3. Theme Check Configuration (`.theme-check.yml`)

Place `.theme-check.yml` in the theme root to enforce agency standards:
```yaml
extends: theme-check:recommended

# Enforce clean modern Liquid syntax
SyntaxError:
  enabled: true

AssetSizeAppBlockCSS:
  enabled: true
  threshold: 100000

RemoteAsset:
  enabled: true

DeprecateBinds:
  enabled: true

# Require accessible alt tags
ImgWidthAndHeight:
  enabled: true
```
