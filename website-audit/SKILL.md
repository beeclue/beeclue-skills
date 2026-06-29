---
name: website-audit
description: >-
  Complete UX, conversion, and psychology audit for any website: static HTML,
  Next.js, WordPress, Webflow, Astro, Gatsby, or CMS-based. Given a local
  directory or live URL, it maps the full user journey including the skeptic's
  path and post-conversion experience, scores every page against conversion
  frameworks (AIDA, Fogg, Cialdini, pricing psychology), and outputs a
  prioritized revamp roadmap that turns the site into a revenue machine.
---

# Website Audit — Full Conversion & UX Revamp

Turns any website into a lead-generating, revenue-driving machine.
Audits every layer: business goals → traffic sources → user psychology →
page architecture → pricing → conversion paths → post-conversion →
re-engagement → technical performance → copy & messaging.

**Supported codebases:** Next.js (App/Pages Router), static HTML, WordPress
(theme files + plugins), Astro, Gatsby, Remix, Webflow exports, and any
JS/TS frontend. Detects the framework automatically in Phase 1.

**Trigger:** user says "audit this site", "review this web app", "/website-audit",
or points you at a local project directory or live URL.

Flags:
- `--dir <path>` — project root (required if not the current directory)
- `--url <url>` — live URL to fetch alongside codebase analysis (also works standalone without `--dir`)
- `--save [path]` — write full report to specified path, or default to `./audits/<SiteName>_Audit_<YYYY-MM-DD>.md`
- `--quick` — abbreviated run: Phases 0, 1.1, 3 (layers 1–4 only), 5, 6 (Sprint 0 only), 7. Skip live fetch, competitor analysis, deep code crawl, analytics audit.
- `--focus <area>` — run only one area: `pricing` | `hero` | `mobile` | `copy` | `analytics` | `seo` | `trust` | `post-conversion` | `framework`
- `--generate-copy` — after identifying copy issues, output 3 rewrite options for each headline/CTA found lacking
- `--benchmark` — compare against industry conversion benchmarks (adds benchmark column to scorecard)

---

## Phase 0 — Business Intelligence Interview

**Do this before touching any code.** Without business context, every recommendation
is guesswork. Ask all questions in one message. Wait for answers before proceeding.

```
BUSINESS CONTEXT
────────────────
1. What is the ONE primary goal of this website?
   (e.g. book a call, capture email, sell a product, sign up for SaaS)

2. Who is the ideal customer? One sentence, be specific.
   (e.g. "B2B SaaS founders with 10–200 employees who hate manual reporting")

3. What does the customer want most when they land here?
   (the outcome they're hiring this site to deliver — not features, outcomes)

4. What traffic sources send visitors? Rank them.
   (e.g. "60% Google SEO, 25% paid Meta ads, 15% referral")

5. Current monthly traffic and conversion rate?
   (rough is fine: "~2k/month, ~1% book a call")

6. Average deal value / LTV of one customer?

7. What do visitors say when they DON'T convert?
   (exit surveys, sales call objections, support tickets — verbatim quotes preferred)

8. Who are the top 2–3 competitors? Paste their URLs.

9. What happens immediately AFTER someone converts?
   (thank-you page URL, what email fires, what the onboarding looks like)

10. Do you have any analytics data you can share?
    (GA4, Mixpanel, Hotjar — especially drop-off pages and scroll depth)

11. What is the single biggest friction point you already know about?

12. Is there a pricing page? How is it structured (tiers, custom quote, freemium)?
```

Capture all answers. Derive:
- **Primary Conversion Event (PCE)** — the one action that equals success
- **Traffic Source Mix** — which sources need separate optimization
- **Revenue Per Visitor (RPV)** = avg deal value × conversion rate × close rate
- **Conversion Lift Value** — what a 1% conversion lift is worth monthly
- **Audit Priority Stack** — order pages by (traffic volume × drop-off severity)

---

## Phase 1 — Codebase Mapping

### 1.0 — Framework Detection

Detect the framework first. This determines which audit paths to follow.

```bash
# Check for Next.js
ls <dir>/next.config.* 2>/dev/null && echo "NEXTJS"

# Check for WordPress
ls <dir>/wp-config.php 2>/dev/null && echo "WORDPRESS"
ls <dir>/wp-content/themes/ 2>/dev/null && echo "WORDPRESS_THEME"
grep -rl "Elementor\|ElementorPro" <dir>/wp-content/plugins/ 2>/dev/null | head -3 && echo "ELEMENTOR"
grep -rl "wpbakery\|vc_row\|vc_column" <dir>/wp-content/ 2>/dev/null | head -3 && echo "WPBAKERY"

# Check for Astro
ls <dir>/astro.config.* 2>/dev/null && echo "ASTRO"

# Check for Gatsby
ls <dir>/gatsby-config.* 2>/dev/null && echo "GATSBY"

# Check for Remix
ls <dir>/remix.config.* 2>/dev/null && echo "REMIX"

# Check for Webflow export
ls <dir>/index.html 2>/dev/null && grep -l "w-webflow\|webflow" <dir>/index.html 2>/dev/null && echo "WEBFLOW"

# Check for static HTML site
find <max_depth 2> -name "*.html" 2>/dev/null | head -20 && echo "STATIC_HTML"

# Check for page builders
grep -rl "elementor\|wpbakery\|divi\|beaver\|flavor\|cornerstone" <dir>/wp-content/ 2>/dev/null | head -5 && echo "PAGE_BUILDER"

# Check package.json for frontend frameworks
cat <dir>/package.json 2>/dev/null | grep -i "react\|vue\|svelte\|angular\|solid" | head -5
```

Record detected framework. Use the appropriate mapping path below.

### 1.1 — Discover All Pages

**Next.js (App Router):**
```bash
find <dir>/app -name "page.tsx" -o -name "page.jsx" -o -name "page.ts" -o -name "page.js" | sort
find <dir>/app -name "\[*\]*" 2>/dev/null | sort  # dynamic routes
find <dir>/app/api -name "*.ts" -o -name "*.js" 2>/dev/null | sort  # API routes
```

**Next.js (Pages Router):**
```bash
find <dir>/pages -name "*.tsx" -o -name "*.jsx" -o -name "*.ts" -o -name "*.js" | grep -v "_app\|_document\|_error\|api/" | sort
find <dir>/pages -name "\[*\]*" 2>/dev/null | sort  # dynamic routes
find <dir>/pages/api -name "*.ts" -o -name "*.js" 2>/dev/null | sort  # API routes
```

**WordPress:**
```bash
# Theme template files
find <dir>/wp-content/themes/<active-theme> -name "*.php" | grep -v "inc/\|vendor/\|node_modules/" | sort

# Page templates
find <dir>/wp-content/themes/<active-theme> -name "page-*.php" -o -name "template-*.php" | sort

# Plugin-detected pages (WooCommerce, Contact Form 7, etc.)
find <dir>/wp-content/plugins -name "*.php" 2>/dev/null | grep -i "template\|page" | head -20
```

**Astro:**
```bash
find <dir>/src/pages -name "*.astro" -o -name "*.md" -o -name "*.mdx" 2>/dev/null | sort
find <dir>/src/content -name "*.md" -o -name "*.mdx" 2>/dev/null | sort
```

**Static HTML:**
```bash
find <dir> -maxdepth 3 -name "*.html" | grep -v "node_modules\|vendor\|dist\|build" | sort
```

**Webflow Export:**
```bash
find <dir> -name "*.html" -maxdepth 2 | sort
ls <dir>/css/ <dir>/js/ 2>/dev/null
```

Build a **Page Inventory Table**:

| Route | File | Funnel Stage | Est. Traffic Rank | PCE Present? | Last Modified |
|---|---|---|---|---|---|
| / | app/page.tsx | TOFU | 1 | — | — |
| /pricing | app/pricing/page.tsx | BOFU | 2 | — | — |

Classify each page:
- **TOFU** — home, blog, landing pages, comparison pages
- **MOFU** — features, how-it-works, case studies, about, integrations
- **BOFU** — pricing, contact, book-a-call, sign-up, checkout, demo request

### 1.2 — Identify Core Components

```bash
# Find all CTAs — broad pattern matching for any framework
# Matches: Button, button, btn, CTA, cta, <a> with action classes, onClick, href with action intent
grep -rn -i "button\|btn\|cta\|onClick\|on-click\|@click\|v-on:click\|href.*contact\|href.*signup\|href.*pricing\|href.*book\|href.*demo\|href.*trial" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --include="*.vue" --include="*.svelte" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|dist\|vendor\|import\|//" | head -50

# Find forms and their fields (any form library or raw HTML)
grep -rn -i "<form\|useForm\|handleSubmit\|onSubmit\|register(\|formState\|Formik\|react-hook-form\|wpforms\|gravityforms\|contact-form-7\|cf7" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --include="*.vue" --include="*.php" --include="*.html" \
  | grep -vi "node_modules\|\.next\|vendor\|import" | head -30

# Find input fields — count them (every unnecessary field kills conversion)
grep -rn -i "<input\|<Input\|<TextField\|<textarea\|<select\|form.*field\|form.*input" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -30

# Find navigation structure
grep -rn -i "nav\|header\|menu\|navbar\|navigation\|sidebar" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | grep -i "component\|class\|id\|function\|export" | head -10

# Find hero / above-fold sections — broad pattern
grep -rn -i "hero\|banner\|above.*fold\|first.*screen\|jumbotron\|masthead\|spotlight" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.html" --include="*.php" --include="*.css" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -20

# Find social proof elements
grep -rn -i "testimonial\|review\|rating\|trust\|logo.*bar\|partner\|client\|case.*study\|stat\|counter\|number\|logo.*cloud\|social.*proof\|badge\|award" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -20

# Find pricing components
grep -rn -i "pricing\|plan\|tier\|price\|billed\|subscription\|monthly\|annual\|enterprise\|freemium" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -20

# Find modals, overlays, popups (exit intent, lead capture, upsells)
grep -rn -i "modal\|overlay\|dialog\|popup\|exit.*intent\|exitIntent\|lightBox\|drawer\|slideout" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.html" --include="*.php" --include="*.js" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -20

# Find chat widgets / live support / AI chatbots
grep -rn -i "intercom\|drift\|crisp\|tawk\|livechat\|hubspot\|freshchat\|zendesk\|chatwoot\|tidio\|zendesk\|chatbot\|ai.*chat\|openai\|gpt.*widget\|chatgpt\|botpress\|voiceflow\|botpress\|manychat" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -10

# Find video components
grep -rn -i "video\|youtube\|vimeo\|iframe\|reactplayer\|wistia\|loom\|plyr\|plyr\|jwplayer\|brightcove" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -10

# Find 404 and error pages
find <dir>/app -name "not-found*" -o -name "error*" 2>/dev/null
find <dir>/pages -name "404*" -o -name "_error*" 2>/dev/null
find <dir> -maxdepth 2 -name "404*" -o -name "error*" 2>/dev/null | grep -v "node_modules\|vendor"

# Find sticky / floating elements
grep -rn -i "sticky\|fixed\|position.*fixed\|floating\|float\|bottom.*bar\|sticky.*cta\|floating.*cta" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.html" --include="*.css" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -20

# Analytics tracking (broad detection)
grep -rn -i "gtag\|ga4\|analytics\|mixpanel\|segment\|posthog\|hotjar\|clarity\|heap\|amplitude\|plausible\|fathom\|matomo\|plausible\|ackee\|pirsch\|umami" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" -l | head -10

# Conversion pixels (Facebook, Google, LinkedIn, etc.)
grep -rn -i "fbq\|_linkedin\|twq\|googleads\|adroll\|pixel\|remarketing\|google.*tag\|gtm\|google.*tag.*manager" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -20

# Cookie consent / GDPR banners
grep -rn -i "cookie.*consent\|cookie.*banner\|gdpr\|cookiebot\|onetrust\|tarteaucitron\|cookie.*notice\|consent.*manager\|complianz\|iubenda" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.ts" --include="*.js" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -10

# Speed-to-lead: response time signals
grep -rn -i "auto.*reply\|instant.*response\|we.*received\|confirmation.*email\|within.*hour\|respond.*within\|reply.*within" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.html" --include="*.php" --include="*.md" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -10
```

### 1.3 — Read Critical Files in Full

Read every file that is high-traffic or PCE-adjacent. The files differ by framework:

**Next.js:**
- Home / landing page component (`app/page.tsx`)
- Hero section component (search for Hero, Banner, Masthead)
- Primary CTA component(s)
- Pricing page + pricing card component
- Contact / book-a-call / sign-up page
- Navigation / header component
- Thank-you / confirmation page (post-PCE)
- Any modal or overlay forms
- 404 / error page
- `next.config.js` / `next.config.ts`
- `package.json`
- `tailwind.config.js` or equivalent (color system — is there a distinct CTA color defined?)
- Any `middleware.ts` (redirect logic, A/B routing, geo-targeting)
- `.env.example` (what third-party services are wired up)

**WordPress:**
- `functions.php` (theme setup, enqueued scripts, hooks)
- `style.css` header (theme metadata)
- `header.php` / `footer.php` (navigation, global elements)
- `index.php` / `front-page.php` / `home.php` (homepage template)
- `page.php` (generic page template)
- `single.php` / `post.php` (blog post template)
- `sidebar.php` (if present — is it used?)
- `404.php` (error page)
- Active theme's `template-parts/` directory (reusable components)
- Any page template: `page-*.php`, `template-*.php`
- WooCommerce templates if e-commerce: `woocommerce/single-product.php`, `woocommerce/cart/`
- `wp-config.php` (check for debug mode, installed constants — DON'T read secrets)
- Installed plugins list: `ls wp-content/plugins/`

**Astro:**
- `src/pages/index.astro` (homepage)
- `src/layouts/` (layout components)
- `src/components/` (all components)
- `astro.config.mjs` (integrations, output mode)
- `package.json`

**Static HTML:**
- `index.html` (homepage)
- All other `.html` files
- `css/` directory (stylesheets)
- `js/` directory (scripts)

**Any framework — also check:**
- `.env.example` / `.env.local.example` (third-party services)
- `robots.txt` / `sitemap.xml`
- `README.md` (project context)

---

## Phase 2 — Technical Performance Signals

Before looking at the live site, audit performance patterns that directly
affect conversion via speed, SEO, and perceived responsiveness.

### 2.0 — Real Performance Data (if `--url` provided)

Always prefer real measured data over code inference when available.

```bash
# PageSpeed Insights API (free, no key needed for basic)
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=<url>&strategy=mobile&category=PERFORMANCE&category=ACCESSIBILITY&category=SEO&category=BEST_PRACTICES" | python3 -c "
import json,sys
d=json.load(sys.stdin)
lhr=d.get('lighthouseResult',{})
cats=lhr.get('categories',{})
for k,v in cats.items():
    print(f\"{v['title']}: {int(v['score']*100)}/100\")
audits=lhr.get('audits',{})
for key in ['first-contentful-paint','largest-contentful-paint','total-blocking-time','cumulative-layout-shift','speed-index','interactive']:
    a=audits.get(key,{})
    print(f\"{a.get('title','?')}: {a.get('displayValue','?')} (score: {a.get('score','?')})\")
" 2>/dev/null

# CrUX data (real user experience from Chrome)
curl -s "https://chromeuxreport.googleapis.com/v1/records:queryRecord" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"<url>\"}" 2>/dev/null | python3 -c "
import json,sys
d=json.load(sys.stdin)
mc=d.get('record',{}).get('metrics',{})
for k,v in mc.items():
    p=v.get('percentiles',{})
    print(f\"{k}: p75={p.get('p75','?')}\")
" 2>/dev/null
```

Record: LCP, CLS, INP, FCP, TTFB, Speed Index. These are your **measured baselines** — all code-level findings must be validated against them.

### 2.1 — Rendering Strategy Audit (Next.js specific — skip for other frameworks)

```bash
# Check for 'use client' directives (client-side rendering)
grep -rn "\"use client\"" <dir>/app --include="*.tsx" | wc -l

# Check for server components (no directive = server by default in app router)
find <dir>/app -name "page.tsx" | head -20

# Check for ISR (Incremental Static Regeneration)
grep -rn "revalidate\|fetch.*revalidate\|next.*revalidate" <dir> --include="*.tsx" --include="*.ts" | head -10

# Check for static generation
grep -rn "generateStaticParams\|getStaticPaths\|getStaticProps" <dir> --include="*.tsx" | head -10

# Check for server actions (form handling)
grep -rn "\"use server\"\|useFormState\|useFormStatus\|action=" <dir>/app --include="*.tsx" | head -20
```

Evaluate:
- Are marketing pages (home, pricing, blog) statically generated or server-rendered? (They must be — dynamic = slow = lost leads)
- Are interactive components properly split with `"use client"` only where needed?
- Is ISR configured for content that updates (blog posts, testimonials)?
- Are Server Actions used for form submissions (eliminates round-trip API calls)?

### 2.1b — WordPress / CMS Performance Audit

```bash
# Check for render-blocking plugins
grep -rn "wp_enqueue_script\|wp_enqueue_style" <dir>/wp-content/themes/<theme>/functions.php 2>/dev/null | wc -l

# Check for image optimization plugins
ls <dir>/wp-content/plugins/ 2>/dev/null | grep -i "smush\|shortpixel\|imagify\|ewww\|optimole\|webp"

# Check for caching plugins
ls <dir>/wp-content/plugins/ 2>/dev/null | grep -i "w3-total\|wp-super-cache\|wp-rocket\|litespeed\|hummingbird\|autoptimize"

# Check for lazy loading
grep -rn "lazy\|loading.*lazy\|defer\|async" <dir>/wp-content/themes/<theme>/ 2>/dev/null | head -10

# Check for database optimization
ls <dir>/wp-content/plugins/ 2>/dev/null | grep -i "wp-optimize\|advanced-database\|query-monitor"
```

### 2.2 — Core Web Vitals Signals (all frameworks)

```bash
# Check for priority prop on hero/LCP image (Next.js)
grep -rn "priority" <dir>/components --include="*.tsx" 2>/dev/null | grep -i "image\|img\|hero" | head -10

# Check for next/image usage vs raw <img>
grep -rn "from 'next/image'\|from \"next/image\"" <dir> --include="*.tsx" 2>/dev/null | wc -l
grep -rn "<img " <dir> --include="*.tsx" --include="*.html" --include="*.vue" --include="*.php" 2>/dev/null \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -20

# Check for layout shift sources (missing dimensions)
grep -rn "width=\|height=" <dir> --include="*.tsx" --include="*.html" --include="*.vue" 2>/dev/null \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | grep -i "image\|img" | head -20

# Check font loading strategy
grep -rn "next/font\|@font-face\|font-display\|font-display.*swap\|preload.*font" \
  <dir> --include="*.tsx" --include="*.css" --include="*.html" --include="*.php" 2>/dev/null | head -10
grep -rn "googleapis.com/css" <dir> --include="*.tsx" --include="*.html" --include="*.php" 2>/dev/null | head -5

# Check for third-party script loading strategy
grep -rn "next/script\|<Script\|async\|defer\|loading=\"lazy\"" \
  <dir> --include="*.tsx" --include="*.html" --include="*.php" 2>/dev/null | head -20

# Check for render-blocking resources
grep -rn "<link.*rel=\"stylesheet\"\|<script.*src" <dir> --include="*.html" --include="*.php" 2>/dev/null \
  | grep -vi "async\|defer\|preload\|module" | head -10
```

Flag against targets (use measured data from 2.0 if available, otherwise infer from code):
- **LCP** < 2.5s → hero image must use `priority` prop (Next.js), correct sizing, WebP/AVIF format, lazy loading for below-fold
- **CLS** < 0.1 → all images need explicit `width`/`height`, fonts use `font-display: swap` or `next/font`
- **INP** < 200ms → heavy client components, synchronous third-party scripts are killers
- **TTFB** < 600ms → static/ISR pages achieve this; dynamic SSR may not; WordPress needs caching plugin

### 2.3 — Routing & Redirect Audit

```bash
# Check for redirect rules (Next.js)
grep -rn "redirects\|redirect(" <dir>/next.config* <dir>/middleware* 2>/dev/null | head -20

# Check for redirect rules (WordPress - .htaccess or redirect plugins)
cat <dir>/.htaccess 2>/dev/null | head -30
ls <dir>/wp-content/plugins/ 2>/dev/null | grep -i "redirection\|rank-math\|yoast\|301\|redirect"

# Check for redirect chains (A→B→C is worse than A→C)
grep -rn "redirects" <dir>/next.config* 2>/dev/null

# Check for broken internal links
grep -rn "href=" <dir> --include="*.tsx" --include="*.html" --include="*.vue" --include="*.php" 2>/dev/null \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" \
  | grep -v "http\|mailto\|tel\|#\|{" | grep "\"/" | head -30

# Check for trailing slash consistency (Next.js)
grep -rn "trailingSlash" <dir>/next.config* 2>/dev/null
```

Evaluate:
- Are there redirect chains (a visitor bounces through 2+ redirects before landing)?
- Are old URLs properly redirected (broken links = instant trust loss)?
- Is trailing slash behavior consistent? (Inconsistency causes duplicate content)
- Does middleware do anything useful for conversion (geo-routing, A/B, auth)?
- For WordPress: are there plugin-based redirects configured? Are they chains?

---

## Phase 3 — Live Site Fetch (if `--url` provided)

```bash
# Measure real performance
curl -o /dev/null -s -w \
  "DNS: %{time_namelookup}s | TCP: %{time_connect}s | TTFB: %{time_starttransfer}s | Total: %{time_total}s | Size: %{size_download}b\n" \
  "<url>"

# Check HTTP headers
curl -sI "<url>" | grep -i "cache-control\|x-powered-by\|server\|content-encoding\|vary\|x-frame-options\|strict-transport\|content-security-policy"

# Check for compression
curl -sI --compressed "<url>" | grep -i "content-encoding"

# Fetch page source for copy analysis
curl -s --max-time 20 "<url>" -o /tmp/audit_home.html 2>/dev/null

# Check for common frameworks via headers/HTML
curl -s "<url>" | grep -i "next\|gatsby\|astro\|nuxt\|remix\|wp-content\|elementor\|webflow" | head -5

# Check for third-party scripts loaded
curl -s "<url>" | grep -oP 'src="[^"]*"' | grep -v "self\|data:" | head -20
```

Use WebFetch to read the live homepage, pricing page, and any flagged pages.

Compare live output vs. source code:
- Discrepancies = runtime logic, A/B tests, personalization, or server-rendered copy worth noting
- Check if the live copy matches what the codebase says (stale deploys are common)
- Note any framework-specific rendering differences (SSR vs static)

If `--url` and competitors provided: use WebFetch to fetch competitor homepages.
Extract: H1, sub-headline, primary CTA text, trust signal above fold, pricing model, chat widget presence, social proof type.

---

## Phase 4 — The 12-Layer Conversion Audit

Score each layer 1–10. 10 = best in class. Weight by funnel stage.
Every flaw found must be quoted specifically (not paraphrased).

---

### Layer 1: Above-the-Fold Clarity (The 3-Second Test)

The visitor decides to stay or leave in **3 seconds**. Every element above the fold
must earn its place.

**H1 Audit**
- Does it state the OUTCOME the customer gets, not what the product does?
  - FAIL: "The best project management software"
  - WIN: "Ship features 2× faster without another status meeting"
- Is it under 10 words? (Longer = skimmed, not read)
- Does it name the ICP's specific pain, not a generic benefit?
- Does it pass the "Would this headline work on a competitor's site?" test?
  (If yes, it's not a value prop — it's a category description)

**Sub-headline Audit**
- Does it address HOW (the mechanism) behind the H1 promise?
- Does it pre-empt the #1 sales objection? ("without X", "even if Y", "in Z minutes")
- Is it under 20 words?

**Hero CTA Audit**
- Is there ONE primary CTA? (No competing actions above the fold)
- Does CTA copy state the outcome or the first step, not the action?
  - FAIL: "Submit" / "Sign Up" / "Learn More"
  - WIN: "Get My Free Audit" / "See It In Action" / "Start Saving Time"
- Is the CTA button color unique — does it appear nowhere else on the page?
- Is there risk-reversal micro-copy beneath the CTA?
  ("No credit card required" / "Cancel anytime" / "Free 14-day trial")
- Is there a secondary trust signal (number stat, logo, rating) directly below CTA?

**Visual Hierarchy Audit**
- Is H1 the largest text element on the page?
- Does eye flow follow: H1 → sub-headline → CTA → trust signal?
- Hero image/video: does it show the product in use or the customer outcome?
  (A person at a desk smiling is NOT a hero image. A before/after result is.)
- Is the hero fully visible without scrolling at 375px (iPhone SE)?
- Is the hero fully visible without scrolling at 1440px (desktop)?

**Video Audit** (if a video exists above or near the fold)
- Is it auto-playing with sound? (Instant trust killer — must be muted or user-initiated)
- Is it under 90 seconds? (Cold traffic drops off after 60–90s)
- Does it show the product working or a customer's result — not a talking head?
- Does it have captions? (80% of social video is watched without sound)
- Is there a clear CTA immediately after the video ends?

**Score this layer. Quote every specific flaw verbatim from the codebase.**

---

### Layer 2: Value Proposition Architecture

Apply the Value Prop Canvas + Jobs-to-be-Done:

- **Gain Creators**: What specific outcomes does the site promise? Are they measurable?
- **Pain Relievers**: What specific pains are called out by name?
- **JTBD**: Does the copy reflect the customer's job, or the product's features?

Audit questions:
- Is the value prop unique and ownable, or could any competitor claim it?
- Are benefits listed before features? (People buy outcomes, then justify with features)
- Does the site use customer language (pulled from reviews/testimonials/interviews)?
  Or internal product language (the team's words, not the market's words)?
- Is there a "Why Us vs. alternatives" section (vs. a generic competitor, not just Brand X)?
- Does the site acknowledge the customer's current alternative? ("Tired of spreadsheets?")
- Does the copy speak to ONE reader ("you") or a crowd ("our customers")?

**The "Who Is This For" Check**
Exclusion creates inclusion. Does the site clearly state who it's for AND who it's NOT for?
A site that tries to speak to everyone speaks to no one.

**Score this layer.**

---

### Layer 3: Trust & Credibility Architecture (Cialdini's 7)

Map every trust signal in the codebase to a Cialdini principle:

| Principle | Present? | Quality (1–5) | Placement | Fix Needed? |
|---|---|---|---|---|
| Social Proof | — | — | — | — |
| Authority | — | — | — | — |
| Scarcity / Urgency | — | — | — | — |
| Liking | — | — | — | — |
| Reciprocity | — | — | — | — |
| Commitment / Consistency | — | — | — | — |
| Unity | — | — | — | — |

**Social Proof Deep Audit**
- Logo bar: Are logos instantly recognizable? Are they above the fold? (Above = credibility; below = reinforcement)
- Testimonials: Do they include full name, job title, company, photo, and a **specific result with a number**?
  - FAIL: "Great product, very easy to use!" — Jane D.
  - WIN: "Cut our weekly reporting from 6 hours to 45 minutes." — Jane Doe, Head of Ops @ Acme Corp (500 employees)
- Star ratings: Displayed near the PCE? Linked to a real review platform?
- Case studies: Is there a quantified before/after? Not "improved efficiency" — "reduced churn by 34%"
- Number proof: "10,000+ customers", "$50M saved", "99.9% uptime" — present and specific?
- Review platform badges (G2, Capterra, Trustpilot, Product Hunt): present and linked?

**Authority Signals**
- Press mentions: logos visible, not just text?
- Awards, certifications, SOC2, ISO, GDPR badges: near forms and payment fields?
- Founder/team credentials: visible on About or homepage?
- Media appearances, podcasts, speaking: referenced?

**Urgency / Scarcity Audit**
- Is any urgency present? (Legitimate urgency: cohort dates, limited spots, price increases)
- Is urgency fake? (Fake countdown timers, "Only 3 left!" on digital products)
  → Flag dark patterns separately (see Layer 5)

**Chat Widget / AI Chatbot Audit**
- Is there a live chat, chatbot, or AI assistant widget?
- If yes: when does it trigger? (Immediate popup = friction; after 30s or scroll = helpful)
- Is the opening message a question (engagement) or a statement (ignored)?
  - FAIL: "Hi! Let me know if you need help."
  - WIN: "What's the #1 thing you're trying to solve today?"
- Is the chat available 24/7 or only during business hours? (If hours-limited, does it say so?)
- **AI Chatbot quality** (if present):
  - Does it qualify leads before connecting to a human?
  - Does it capture email/phone even if the user drops off?
  - Does it have a clear handoff to human support?
  - Does it answer the top 5 FAQs from Phase 0 correctly?
  - Is it trained on the product/ICP-specific knowledge, or generic?
- **Speed-to-lead audit**:
  - After form submit: how fast does the business respond? (Code may reveal auto-reply timing)
  - Is there an immediate confirmation message on the page?
  - Is there a "we'll respond within X hours" expectation set?
  - FAIL: No response time mentioned → user assumes "maybe never"
  - WIN: "We respond within 2 hours during business hours. Your audit is being generated now."
- **Personalization signals**:
  - Does the site show different copy based on traffic source? (UTM parameters)
  - Is there geo-targeted content? (location-specific copy, pricing in local currency)
  - Are there dynamic hero sections based on industry/use-case?
  - Is there A/B testing infrastructure? (Look for Optimizely, VWO, LaunchDarkly, Split.io, or custom)

**Score this layer. Map the trust deficit.**

---

### Layer 4: Conversion Path Analysis (Funnel Math)

Map every possible path from landing to PCE.

```
[Entry Source] → [Landing Page] → [Page A] → [PCE] ✅
[Entry Source] → [Landing Page] → [Blog Post] → (dead end) ⚠️
```

For each path, count:
- **Clicks to PCE** — target is ≤3 from homepage
- **Decision points** — every dropdown, tab, modal, redirect is a potential exit
- **Dead ends** — pages with no CTA, no next step, no path forward
- **Leaks** — outbound links that take users off-site before PCE

**The Rule**: Every page must have exactly ONE primary CTA pointing toward PCE,
and ONE secondary CTA that advances the visitor one step deeper.

Audit each page for:
- Zero CTAs (abandoned page)
- 3+ competing CTAs (paralysis by analysis)
- Nav that offers more escape routes than conversion paths
- Footer links that invite exit (social media links, unrelated pages)

**Sticky CTA / Scroll Trigger Audit**
- Is the primary CTA visible after the user scrolls past the hero?
- Is there a sticky nav bar that keeps the CTA visible throughout?
- Are there scroll-triggered CTAs (e.g., sidebar CTA appearing at 50% scroll depth)?
- Is there a floating CTA bar at the bottom on mobile?

**404 & Error Recovery Audit**
- What does the 404 page look like? (Read the file)
- Does it have a search bar, popular pages, and a clear CTA back to the PCE?
- Does the error page help the user or abandon them?
- A great 404 page recovers ~10% of lost sessions.

**Build a Conversion Flow Diagram:**

```
/ (Home) — PCE clicks: 1
├── Primary CTA "Get Free Audit" → /contact ✅
├── Nav: Features → /features (MOFU, has PCE CTA) ✅
├── Nav: Blog → /blog (LEAK — no return CTA) ⚠️
├── Nav: Pricing → /pricing (BOFU, good) ✅
└── Footer: Twitter link (LEAK — exits site) ⚠️

/pricing — PCE clicks: 1
├── Primary CTA "Start Free Trial" → /signup ✅
├── FAQ (informational, no CTA after) ⚠️
├── Plan comparison table (no CTA below fold) ⚠️
└── "Talk to Sales" → /contact (secondary CTA) ✅
```

**Score this layer.**

---

### Layer 5: Psychological Friction & Dark Patterns

**Behavior = Motivation × Ability × Prompt** (Fogg Behavior Model)

When conversion fails, one of these three is broken:
- **Low Motivation** — copy doesn't compel, wrong audience, wrong pain targeted
- **Low Ability** — too many steps, too slow, too confusing, too much friction
- **Missing/Weak Prompt** — no CTA, CTA buried, wrong timing

**Friction Inventory — count every instance:**

*Cognitive friction:*
- Jargon the ICP wouldn't use in a sentence
- Features listed without benefit translation
- More than 2 options presented simultaneously without a recommended choice
- Pricing with no anchoring (no "most popular", no crossed-out higher price, no "save X%")
- Unclear next step after any user action

*Emotional friction:*
- No acknowledgement of the user's pain or current frustration
- Generic stock photography (signals inauthenticity)
- No brand personality — sounds like every other company in the space
- Missing risk-reversal near high-commitment moments (form submit, checkout)
- No human element (founder face, team photo, real names)

*Process friction:*
- Form fields that are not needed at this stage (each extra field = ~11% drop in conversion)
- Multi-step process without a progress indicator
- No autofill / autocomplete support (`autocomplete="email"`, `autocomplete="tel"`)
- CAPTCHA visible before any trust has been established
- Password strength requirements shown before the user starts typing
- Validation errors only appear on submit (must be inline)
- Popup firing before 20 seconds or before first scroll
- No guest/anonymous option (forced account creation before browsing or buying)
- Phone number field required when email would suffice
- State/country dropdown not pre-filled based on IP geolocation
- No "save and continue later" for multi-step forms

**Dark Pattern Audit** (flag each one — these actively erode long-term trust)
- Fake countdown timers (resets on page refresh)
- "Only X left!" on digital/unlimited products
- Pre-checked opt-in boxes (for email list, upsells)
- Roach motel: easy to sign up, hard to cancel (audit the cancellation flow in the codebase)
- Bait-and-switch pricing (price changes at checkout)
- Misdirection (confirm-shaming: "No thanks, I don't want more leads")
- Disguised ads or paid placements presented as organic results
- Cookie consent that makes "Accept All" the obvious default with no easy "Reject All"

**Score this layer. Count total friction points and dark patterns separately.**

---

### Layer 6: Copy & Messaging Hierarchy

Read the FULL copy of every BOFU page. Evaluate:

**The 5-Second Scan Test**
Read only the H1, H2s, and H3s in sequence. Do they tell a complete, compelling story
without reading any body copy? This is how most visitors experience the page.

**Headline Hierarchy**
- H1: Outcome-led, ICP-specific, under 10 words
- H2s: Benefit-led, not feature-led ("Work less, ship more" not "Automated scheduling")
- H3s: Specifics, proof points, elaboration

**Body Copy**
- Paragraphs ≤3 lines (desktop) — longer = skimmed, not read
- Bullets for feature lists, steps, and benefits
- **Bold the key insight** in each paragraph so skimmers capture it
- Speaks to "you" (singular), not "our customers" (plural, distant)
- Uses customer's own language (pulled from reviews, sales calls, support tickets)
- Objections answered before the reader forms them

**Urgency Copy** (BOFU pages only)
- Is there urgency? (Legitimate: "Cohort starts Jan 15", "Founding member pricing ends Friday")
- Does it avoid manufactured urgency? ("Don't miss out!" with no context = ignored)

**Micro-copy** (highest leverage, lowest effort)
- Button labels: outcome-oriented, not action-oriented
  - FAIL: "Submit" / "Send" / "Go"
  - WIN: "Get My Free Audit" / "Start My Trial" / "Show Me the Pricing"
- Form placeholders: helpful hints, not redundant labels
  - FAIL: placeholder="Email" on a field labeled "Email"
  - WIN: placeholder="you@company.com — we'll send the report here"
- Error messages: human, specific, and tell the user how to fix it
  - FAIL: "Invalid input"
  - WIN: "That email doesn't look right — try name@company.com"
- Empty states: guide the user to the next action (not blank or generic "Nothing here")
- Confirmation messages: confirm the action AND tell the user exactly what happens next
  - FAIL: "Form submitted!"
  - WIN: "You're in! Check your inbox — your audit report arrives in 5 minutes. Here's what to do while you wait → [CTA]"

**Brand Voice Consistency Audit**
- Does the copy have a consistent personality across all pages?
- Does the tone shift between marketing pages and product pages? (Disconnect = untrustworthy)
- Is the reading level appropriate for the ICP? (B2B SaaS founders ≠ enterprise procurement)
- Are there pages that clearly had different writers? (Flag them — inconsistency kills subliminal trust)

If `--generate-copy` flag: for every headline/CTA failing the audit, provide 3 rewrite options.

**Score this layer.**

---

### Layer 7: Pricing Psychology Deep Audit

The pricing page is often the highest-converting page on the site.
It gets one shot to turn consideration into commitment.

**Price Architecture**
- How many tiers? (Ideal: 3 — uses decoy pricing effect. 2 = too simple. 4+ = paralysis)
- Is the middle/recommended tier highlighted as "Most Popular" or "Best Value"?
  (Decoy effect: middle tier should be designed to be chosen ~60% of the time)
- Is there a price anchor? (A crossed-out original price makes current price feel like a deal)
- Is there a "save X% with annual" toggle? (Annual subscriptions improve LTV by 3–4×)
- Is pricing shown per month or per day? (Per day feels smaller: "$1.60/day" vs "$49/month")
- Is there a "What's included" breakdown that stacks value before showing price?
- Are prices charm-priced? ($97 vs $100, $497 vs $500 — ~5% psychological gap)

**Objection Handling on Pricing Page**
- Is there an FAQ section specifically on the pricing page? (Must address top 5 objections)
- Is there a money-back guarantee? Where is it placed relative to the CTA?
  (Guarantee placed directly beneath CTA button = highest conversion position)
- Is there a comparison table (This Plan vs. That Plan vs. Competitor)?
- Is "Talk to Sales" or "Custom Quote" visible for enterprise visitors?

**Social Proof on Pricing Page**
- Are there testimonials specifically about value/ROI (not features)?
  ("We made back the annual cost in the first week" is pricing-page gold)
- Is the customer count or revenue processed visible on this page?

**The "Why Not Free" Audit**
If there's a freemium or free trial:
- Is it clearly differentiated from paid? (Free shouldn't feel like paid)
- Is there a feature gate that creates a natural upgrade moment?
- Is the upgrade prompt contextual (fires when user hits the limit) or intrusive (fires randomly)?

**Score this layer.**

---

### Layer 8: Mobile & Performance Audit

**Performance is conversion.** Every 1-second delay = ~7% conversion drop.
Mobile is typically 60%+ of traffic. The mobile experience IS the experience.

**If measured data available from Phase 2.0, use it here.** Otherwise infer from code:

```bash
# Check image optimization (Next.js)
grep -rn "from 'next/image'" <dir> --include="*.tsx" 2>/dev/null | wc -l

# Check for raw <img> tags (any framework)
grep -rn "<img " <dir> --include="*.tsx" --include="*.html" --include="*.vue" --include="*.php" 2>/dev/null \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -20

# Check for responsive design patterns
grep -rn "sm:\|md:\|lg:\|xl:\|@media\|min-width\|max-width\|breakpoint" \
  <dir> --include="*.tsx" --include="*.css" --include="*.html" --include="*.vue" 2>/dev/null | wc -l

# Check for mobile-specific components
grep -rn -i "mobile\|hamburger\|drawer\|bottom.*nav\|tab.*bar\|swipe" \
  <dir> --include="*.tsx" --include="*.jsx" --include="*.vue" --include="*.html" --include="*.php" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -10

# Check touch targets (should see min 44px)
grep -rn "min-w\|min-h\|min-width\|min-height\|padding\|p-[0-9]" \
  <dir> --include="*.tsx" --include="*.css" --include="*.html" --include="*.vue" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | grep -i "button\|btn\|cta\|link" | head -20

# Check for font-size on mobile inputs (must be >=16px to prevent iOS zoom)
grep -rn "text-xs\|text-sm\|fontSize.*1[0-4]\b\|font-size.*1[0-4]" \
  <dir> --include="*.tsx" --include="*.css" --include="*.html" --include="*.vue" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | grep -i "input\|form\|field\|email" | head -10

# Check for horizontal scroll issues
grep -rn "overflow-x\|overflow.*scroll\|white-space.*nowrap" \
  <dir> --include="*.tsx" --include="*.css" --include="*.html" --include="*.vue" \
  | grep -vi "node_modules\|\.next\|vendor\|import\|//" | head -10
```

Evaluate against conversion standards:
- Hero image optimized? (next/image with priority for Next.js, WebP/AVIF for others, explicit dimensions)
- All images have explicit `width` and `height`? (Prevents CLS)
- Fonts load without layout shift? (next/font, font-display: swap, or preload)
- Loading skeletons for dynamic content? (Reduces perceived wait)
- Third-party scripts (analytics, chat, pixels) deferred/async?
- Nav collapses cleanly on mobile with a proper hamburger?
- Touch targets ≥ 44×44px on all tappable elements?
- Form inputs have `font-size: 16px` minimum? (Below 16px triggers iOS zoom = form abandonment)
- CTAs large enough to tap with a thumb?
- Horizontal scroll: present anywhere? (Instant trust killer on mobile)
- No interstitial popups that block content on mobile? (Google penalty + UX killer)

**Score this layer.**

---

### Layer 9: Analytics & Instrumentation Audit

Without measurement, there's no improvement. Every untracked event is a blind spot.

```bash
# Installed analytics tools
grep -rn "gtag\|ga4\|mixpanel\|segment\|amplitude\|posthog\|hotjar\|clarity\|heap\|plausible\|fathom" \
  <dir> --include="*.tsx" --include="*.ts" --include="*.js" -l

# Events currently tracked
grep -rn "\.track\|gtag('event'\|logEvent\|\.capture\|analytics\.track\|sendEvent" \
  <dir> --include="*.tsx" --include="*.ts" | grep -v "//\|import\|require" | head -40

# Conversion pixels
grep -rn "fbq\|_linkedin\|twq\|googleads\|adroll\|pixel\|remarketing" \
  <dir> --include="*.tsx" --include="*.ts" | head -20

# UTM parameter handling
grep -rn "utm_\|UTM\|searchParams.*utm\|useSearchParams" <dir> --include="*.tsx" | head -20

# Error tracking
grep -rn "sentry\|bugsnag\|rollbar\|datadog\|raygun" <dir> --include="*.tsx" --include="*.ts" -l
```

Build an **Analytics Gap List**. P0 = missing event that directly blinds revenue decisions:

| Event | Required? | Present? | Priority |
|---|---|---|---|
| PCE completed (form submit / checkout / booking) | Required | — | P0 |
| PCE page view (pricing, contact, signup) | Required | — | P0 |
| Hero CTA click | Required | — | P0 |
| Form field abandonment | Required | — | P0 |
| Scroll depth (25/50/75/100%) on key pages | Required | — | P0 |
| Navigation clicks | Required | — | P1 |
| Exit intent trigger | Required | — | P1 |
| Pricing plan selected | Required | — | P0 |
| Video play / 25% / 50% / complete | If video present | — | P1 |
| Chat opened / first message sent | If chat present | — | P1 |
| Error events (validation failures, API errors) | Required | — | P1 |
| UTM source/medium captured on conversion | Required | — | P0 |
| Outbound link clicks | Recommended | — | P2 |
| Time-on-page for MOFU/BOFU pages | Recommended | — | P2 |

**Score this layer. List every missing P0 event as a critical gap.**

---

### Layer 10: SEO → UX Pipeline Audit

SEO generates TOFU traffic. UX converts it. They must be designed together.

```bash
# Page metadata
grep -rn "export.*metadata\|generateMetadata\|<title\|og:\|twitter:" \
  <dir>/app --include="*.tsx" | head -30

# Sitemap and robots
find <dir> \( -name "sitemap.ts" -o -name "sitemap.xml" -o -name "robots.ts" -o -name "robots.txt" \) 2>/dev/null

# Structured data (rich results = free SERP real estate)
grep -rn "application/ld+json\|schema.org\|\"@type\"\|FAQPage\|Product\|Review\|Organization" \
  <dir> --include="*.tsx" | head -20

# Canonical tags
grep -rn "canonical\|alternates.*canonical" <dir>/app --include="*.tsx" | head -10

# Internal linking (TOFU → MOFU → BOFU)
grep -rn "href=\"/blog\|href=\"/features\|href=\"/pricing\|href=\"/case" \
  <dir>/components --include="*.tsx" | head -20
```

Evaluate:
- Every page has a unique `<title>` and `meta description` with the ICP keyword?
- H1 on each page aligns with the page's primary search intent?
- Open Graph configured for all key pages? (Social sharing = free traffic)
- Structured data present? (FAQ schema on pricing page = FAQ rich result = more SERP space)
- Blog or content engine present to generate TOFU traffic?
- Internal links push visitors from TOFU → MOFU → BOFU?
- Comparison pages exist for "[This Product] vs [Competitor]" queries? (High buyer intent)
- Programmatic landing pages for location, industry, or use-case variations?

**Score this layer.**

---

### Layer 11: Post-Conversion Experience Audit

**Most audits stop at the lead. This is where revenue is actually made.**
The moment after conversion is the highest-trust moment in the relationship.
Wasting it leaves the most revenue on the table.

**Thank-You Page Audit** (Read the file. If it doesn't exist, flag as P0.)
The thank-you page should do 5 things:
1. **Confirm the action** — "You're in! Your [X] is on its way."
2. **Set expectations** — "Here's exactly what happens next and when."
3. **Reduce anxiety** — "You made the right call. Here's why: [micro-proof]"
4. **Deepen the relationship** — invite them to take the next micro-step (join community, follow on social, watch a video, book a call if they just signed up for trial)
5. **Create a referral moment** — "Know someone who needs this? Share → [link]"

Evaluate the thank-you page against all 5. If the page just says "Thanks, we'll be in touch" → score = 1.

**Email Sequence Audit** (if `package.json` or env reveals an email tool — Resend, Postmark, SendGrid, Mailchimp, ConvertKit, Loops, React Email,MJML)
- Is there a welcome email? Does it fire within 5 minutes of PCE?
- Does the welcome email have ONE clear next action?
- Is there a nurture sequence for leads who didn't purchase immediately?
- Does the sequence address the top objections from Phase 0 in order?
- Is the email sender name a real person or "No Reply"? (Real person = 2× open rate)
- Is there a re-engagement email at 24h, 72h, 7 days post-signup?
- For trial users: is there a "trial ending in 3 days" email? What does it say?

**Onboarding Audit** (for SaaS / sign-up flows):
- How many steps from signup to "aha moment"? (Target: ≤3)
- Is there a welcome tour / checklist / getting-started guide?
- Is the first action pre-filled or guided? (Reduce activation friction)
- Is there a progress indicator showing setup completion?
- Is there an email/ping if the user hasn't completed setup within 24h?

**The 97% Re-engagement Strategy**
97% of visitors do not convert on first visit. What happens to them?

Audit:
- Is there a retargeting pixel? (Facebook, Google, LinkedIn)
- Is there an exit-intent popup offering a lead magnet (free guide, checklist, mini-audit)?
- Is there email capture before the PCE? (Email = second chance; no email = gone forever)
- Is there a lead magnet? What is it? Is it valuable enough to trade an email for?
  - FAIL: "Subscribe to our newsletter"
  - WIN: "Download: The 5-Point Checklist We Use to Audit Every Client's Site"
- Is there a remarketing email sequence for cart abandonment or sign-up drop-off?
- Is there an in-app notification system to re-engage dormant users?
- Is there a referral program? Is it easy to find and use?

**Score this layer.**

---

### Layer 12: Brand Consistency & Visual Trust Audit

Trust is built subliminally through visual consistency. Inconsistency signals
a poorly run operation — even if the product is great.

**Visual Consistency Checks** (read component files)
- Is one primary CTA color used throughout the site and only for CTAs?
- Is the typography scale consistent (same font, same size hierarchy) across all pages?
- Do all sections use consistent spacing scale?
- Are all icons from the same family/style?
- Do all images have a consistent treatment (style, color grading, subject matter)?
- Does the homepage feel like the same site as the pricing page? The blog? The 404?

**Color Psychology Audit**
- Is the CTA button color high-contrast against its background? (Minimum 4.5:1 ratio)
- Does the CTA color create visual tension / "pops"?
- Is the overall color palette appropriate for the ICP's industry expectations?
  (Fintech: blue/white = trust. Legal: navy/gold = authority. Health: green = safety.
   If the color palette contradicts industry expectations, it creates subliminal doubt.)

**Accessibility as Conversion**
Low accessibility = real revenue loss (15% of population, plus mobile-adverse conditions):
- Form labels visible (not just placeholder text)? Labels disappear when users type
- Error states use color AND text (not color alone)
- Keyboard navigation reaches the PCE without a mouse
- CTA buttons have descriptive aria-labels (not just "button" or "click here")

**Score this layer.**

---

## Phase 5 — Competitive Gap Analysis

For each competitor URL from Phase 0, use WebFetch to read their homepage + pricing page.

### 5.1 — Direct Site Comparison

| Element | This Site | Competitor 1 | Competitor 2 | Winner |
|---|---|---|---|---|
| H1 — outcome specificity | — | — | — | — |
| Sub-headline — objection handling | — | — | — | — |
| Trust signals above fold | — | — | — | — |
| PCE clicks from homepage | — | — | — | — |
| Pricing clarity + anchoring | — | — | — | — |
| Social proof quality | — | — | — | — |
| Mobile experience | — | — | — | — |
| Thank-you page quality | — | — | — | — |
| Re-engagement / exit intent | — | — | — | — |
| Content / TOFU engine | — | — | — | — |
| AI chatbot / live chat | — | — | — | — |
| Speed-to-lead (response time) | — | — | — | — |

### 5.2 — SEO & SERP Presence

```bash
# Check competitor SERP presence
# Use WebSearch to find: site:competitor.com, competitor reviews, competitor comparisons
```

Use WebSearch to research:
- `site:<competitor.com>` — how many pages indexed? What content strategy?
- `"<competitor> vs"` — who are they compared against? What's the narrative?
- `"<competitor> review"` — what's the sentiment? What complaints surface?
- `"<competitor> pricing"` — is pricing transparent or gated?
- `"<competitor> alternative"` — are they ranking for competitor terms?

### 5.3 — Review Sentiment Mining

Use WebSearch to find competitor reviews on G2, Capterra, Trustpilot, Reddit, Twitter:
- What do their happiest customers love? (steal this positioning)
- What do their angriest customers hate? (exploit this gap)
- What feature is most requested but missing? (opportunity)
- What's the #1 complaint about their pricing? (your advantage)

### 5.4 — Ad & Messaging Intelligence

```bash
# Check Google Ads transparency
# Use WebSearch: "competitor site:adstransparency.google.com"
# Or fetch: https://adstransparency.google.com/?region=<country>
```

Research:
- What ad copy are competitors running? (Headlines, descriptions, CTAs)
- What keywords are they bidding on?
- Are they running retargeting ads? (Check with Facebook Ad Library)
- What's their landing page for paid traffic vs organic?

### 5.5 — Asymmetric Opportunity Map

Identify **3 asymmetric opportunities** — areas where competitors are weakest
and this site could dominate with targeted effort:

| Opportunity | Competitor Weakness | Our Advantage | Effort | Impact |
|---|---|---|---|---|
| — | — | — | H/M/L | H/M/L |
| — | — | — | H/M/L | H/M/L |
| — | — | — | H/M/L | H/M/L |

---

## Phase 6 — The Skeptic's Journey Map

**Most audits map the happy path. This maps the path of the most skeptical ICP visitor.**

The skeptic: highly qualified, has been burned before, actively looking for reasons NOT to trust.
They read every word. They check the fine print. They hover over testimonials.
If the site can convert the skeptic, it can convert anyone.

Map their journey:

```
Skeptic lands on homepage
│
├── Scans H1 → "Generic, seen this before" ⚠️ [specific H1 flaw]
├── Looks for "Who made this?" → No founder face, no About link in nav ⚠️
├── Checks testimonials → No surnames, no companies, no results ⚠️
├── Clicks Pricing → Finds "Contact us for pricing" ⚠️ [instant exit signal]
├── Looks for cancellation policy → Can't find it ⚠️
├── Looks for real phone number or address → Footer has none ⚠️
└── Leaves → Converts on Competitor 2 ✅ (for them)
```

For each skeptic exit point found: document the specific flaw and the fix.

**The 5 Skeptic Questions** the site must answer without the visitor having to ask:
1. "Who is behind this?" (Real people, real company, verifiable)
2. "Has this worked for people like me?" (Specific results from specific people)
3. "What happens if I don't like it?" (Risk-reversal: refund, cancel, no commitment)
4. "What does this actually cost?" (Pricing transparency — opacity = suspicion)
5. "Why should I do this now?" (Legitimate urgency or a reason to act today)

---

## Phase 7 — Scoring & Prioritization

### Master Score Card

| Layer | Score (1–10) | Weight | Weighted Score | Benchmark (Top 10%) | Business Impact (H/M/L) | Effort to Fix (H/M/L) | Priority Rank |
|---|---|---|---|---|---|---|---|
| 1. Hero / Above-the-Fold | — | 15% | — | 8+ | — | — | — |
| 2. Value Proposition | — | 12% | — | 8+ | — | — | — |
| 3. Trust & Credibility | — | 12% | — | 8+ | — | — | — |
| 4. Conversion Path | — | 12% | — | 8+ | — | — | — |
| 5. Friction & Dark Patterns | — | 10% | — | 2 or less | — | — | — |
| 6. Copy & Messaging | — | 10% | — | 8+ | — | — | — |
| 7. Pricing Psychology | — | 8% | — | 8+ | — | — | — |
| 8. Mobile & Performance | — | 8% | — | 8+ | — | — | — |
| 9. Analytics & Instrumentation | — | 5% | — | 9+ | — | — | — |
| 10. SEO → UX Pipeline | — | 3% | — | 8+ | — | — | — |
| 11. Post-Conversion & Re-engagement | — | 3% | — | 8+ | — | — | — |
| 12. Brand Consistency & Visual Trust | — | 2% | — | 8+ | — | — | — |
| **Overall Conversion Health Score** | — | 100% | — | 8+ | — | — | — |

**Weighting rationale**: Layers 1–4 directly control whether a visitor converts. Layers 5–8 remove barriers. Layers 9–12 enable optimization. Weight accordingly.

**Conversion Confidence Score**: `((Weighted Score - 3) / 7) × 100`
- 0–30%: Site will struggle to convert cold traffic
- 30–60%: Functional but leaving significant revenue on the table
- 60–80%: Competitive — targeted fixes can unlock growth
- 80–100%: Best-in-class — focus on optimization, not overhaul

**Priority Formula** = (10 − Score) × Impact Weight × (1 / Effort Weight)

Sort all issues: High Impact + Low Effort first. These are the compounding quick wins.

### Quick Win Stack (Week 1 — no dev or minimal dev)
Headline rewrites, CTA copy, risk-reversal micro-copy, trust badges, missing CTAs,
competing CTA removal, thank-you page rebuild, analytics P0 events.

### Foundation Sprint (Weeks 2–4)
Page restructures, hero rebuild, pricing page overhaul, conversion path repair,
tracking implementation, chat widget timing.

### Growth Infrastructure (Month 2+)
Exit intent + lead magnet, comparison pages, case study pages, referral mechanics,
A/B test infrastructure, content engine, retargeting pixel strategy.

---

## Phase 8 — The Revamp Roadmap

Each item must be specific enough to hand directly to a developer or copywriter.

```
## [P0/P1/P2] [Page/Component] — [What to Change]

**Current state:** "[exact current copy or description of current UI]"
**Why it fails:** [specific psychological or conversion reason — cite the principle]
**What to change:** [exact replacement — rewritten copy, layout change, component to add]
**Psychology principle:** [Fogg / Cialdini / JTBD / Hick's Law / Loss Aversion / etc.]
**Expected metric:** [which metric improves: conversion rate / scroll depth / bounce rate / etc.]
**Effort:** [X hours for a developer, Y hours for a copywriter]
**A/B hypothesis:** "Changing [X] to [Y] will increase [PCE rate / click-through / scroll depth]
  by [estimated %] because [specific psychology reason]. Test for [N] visitors to reach significance."
```

Group into sprints:

### Sprint 0 — No-Code Wins (1–3 days, no developer needed)
All copy changes, CTA relabels, meta description updates, testimonial improvements,
micro-copy additions, removing leaking nav links, thank-you page text update.

### Sprint 1 — Page-Level Restructure (1–2 weeks)
Hero section rebuild, trust section above fold, pricing page architecture,
conversion path repair, analytics P0 events, sticky CTA implementation,
chat widget reconfiguration, 404 page rebuild.

### Sprint 2 — New Conversion Infrastructure (2–4 weeks)
Exit intent capture + lead magnet, new BOFU landing pages for top traffic sources,
social proof engine (auto-pull reviews), case study pages, comparison pages,
email welcome sequence, remarketing pixel setup.

### Sprint 3 — Growth & Scale (Ongoing)
Content engine + SEO flywheel, A/B test infrastructure (first 3 hypotheses queued),
referral program, traffic source personalization, programmatic landing pages,
pricing page experimentation, customer advocacy program.

---

## Phase 9 — Revenue Impact Projection

```
CURRENT STATE
─────────────────────────────────────────
Monthly Visitors:         [X]
Traffic Source Mix:       [SEO X% / Paid X% / Direct X% / Referral X%]
Current Conversion Rate:  [Y%]
Monthly Leads/Sales:      [X × Y%]
Close Rate (if B2B):      [Z%]
Avg Deal Value / LTV:     [$W]
Current Monthly Revenue:  [leads × close rate × deal value]
Revenue Per Visitor:      [$W × Y% × Z%]


WHAT EACH SPRINT IS WORTH
─────────────────────────────────────────
Sprint 0 (copy + CTA + thank-you page):
  Projected conversion lift: +[A]%
  New monthly leads:          [X × (Y + A)%]
  Monthly revenue delta:      +$[amount]
  Implementation cost:        ~$[copywriter hours]
  Payback period:             [days]

Sprint 1 (page restructure + analytics + pricing):
  Projected conversion lift: +[B]%
  New monthly leads:          [X × (Y + A + B)%]
  Monthly revenue delta:      +$[amount]

After Full Revamp:
  Conservative (0.5× improvement on identified gaps): +$[amount]/month
  Base case (1× improvement):                         +$[amount]/month
  Best case (2× improvement):                         +$[amount]/month

Annual value of full revamp (base case): +$[amount × 12]
Estimated revamp investment:             $[dev + design + copy hours]
Break-even:                              [X weeks/months]
ROI at 12 months:                        [X×]
```

---

## Output Format

Produce a single Markdown document with sections in this order:

### Part 1 — Executive Brief (1 page max, for stakeholders)

```
┌─────────────────────────────────────────────────────────────────┐
│  EXECUTIVE BRIEF                                                │
│                                                                  │
│  Site: [Name]                Framework: [Next.js / WP / etc.]   │
│  Conversion Confidence: [X]%     Overall Score: [X]/100         │
│                                                                  │
│  THE PROBLEM (in 2 sentences):                                   │
│  [What's broken and what it's costing per month]                │
│                                                                  │
│  TOP 3 WINS (quick wins, high impact):                          │
│  1. [Change] → Expected lift: +[X]% → Worth $[X]/month         │
│  2. [Change] → Expected lift: +[X]% → Worth $[X]/month         │
│  3. [Change] → Expected lift: +[X]% → Worth $[X]/month         │
│                                                                  │
│  REVENUE AT STAKE: $[X]/month (current) → $[X]/month (after)   │
│  BREAK-EVEN: [X] weeks                                          │
│                                                                  │
│  START HERE: [One specific action to take in the next 2 hours]  │
└─────────────────────────────────────────────────────────────────┘
```

### Part 2 — Full Audit Report

1. **Business Context** — ICP, PCE, traffic mix, revenue math
2. **Site Map & Funnel Architecture** — page inventory table + conversion flow diagram
3. **Audit Findings** — all 12 layers, each scored with verbatim findings
4. **The Skeptic's Journey Map** — their path + every exit point
5. **Competitive Gap Matrix** — side-by-side + 3 asymmetric opportunities + SERP/review intelligence
6. **Master Score Card** — weighted priority matrix with benchmarks
7. **Revamp Roadmap** — all 4 sprints, full detail per item
8. **Revenue Impact Projection** — the math

### Part 3 — Before/After Mockups (top 3 changes)

For the 3 highest-impact changes, describe:

```
## Change #1: [What to change]

**BEFORE (current state):**
[Exact current copy, layout description, or component structure]

**AFTER (recommended state):**
[Exact new copy, layout change, or component to add — specific enough
for a developer or copywriter to implement without further questions]

**WHY this works:** [Cite the psychology principle — Fogg, Cialdini, JTBD, etc.]
**EXPECTED IMPACT:** [Which metric improves and by how much]
**A/B HYPOTHESIS:** "Changing [X] to [Y] will increase [metric] by [%] because [reason]."
```

If `--save`: write to specified path or default `./audits/<SiteName>_Audit_<YYYY-MM-DD>.md`

**Always end with a "START HERE TODAY" box:**

```
┌─────────────────────────────────────────────────────────┐
│  START HERE TODAY (next 2 hours, zero dev needed)       │
│                                                         │
│  1. [Specific change #1 — exact copy/fix]               │
│  2. [Specific change #2]                                │
│  3. [Specific change #3]                                │
│                                                         │
│  Estimated conversion lift from these 3 alone: +X%     │
│  Worth $[amount] per month at current traffic.         │
└─────────────────────────────────────────────────────────┘
```

---

## Key Frameworks Reference

**AIDA**: Attention → Interest → Desire → Action
Every page maps to exactly one AIDA stage. Don't try to do all four at once.

**Fogg Behavior Model**: Behavior = Motivation × Ability × Prompt
When conversion fails, one of these three is broken. Diagnose which.

**Cialdini's 7**: Social Proof · Authority · Scarcity · Liking · Reciprocity · Commitment · Unity

**Jobs-to-be-Done**: The customer isn't buying software. They're buying an outcome.
"People don't want a drill, they want a hole in the wall."

**Decoy Pricing**: 3 tiers. The middle tier is designed to be chosen ~60% of the time.
The top tier makes the middle feel reasonable. The bottom tier makes paid feel accessible.

**Hick's Law**: More choices = longer decision time = more abandonment.
Max 2 meaningful choices per decision moment.

**Miller's Law**: Working memory holds 7±2 items.
Feature lists over 7 items kill comprehension.

**Loss Aversion**: People are 2× more motivated by avoiding loss than gaining equivalent value.
"Stop losing leads every week" converts better than "Get more leads every week."

**Peak-End Rule**: People judge an experience by its peak moment and its end.
The thank-you page and the last interaction before exit are disproportionately remembered.

**IKEA Effect**: People value what they build or co-create.
Interactive tools, quizzes, and configurators increase commitment before purchase.

**Anchoring**: The first number a visitor sees frames all subsequent numbers.
Show the highest value first (enterprise price, total savings) before showing the actual price.

**Social Proof Threshold**: Below 10 reviews/testimonials, social proof can backfire.
If under 10, focus on authority signals and specific case studies instead.

**The Skeptic's Lens**: Always audit from the perspective of the most skeptical qualified visitor.
If the site can convert them, it can convert anyone.

**The $10,000 Test**: Would a conversion-rate optimizer stake $10,000 on this recommendation?
Only recommend changes you'd bet money on. No hedging.

**The 5-Second Test**: Show a visitor the page for 5 seconds, then ask "What does this site do?"
If they can't answer, the hero has failed.
