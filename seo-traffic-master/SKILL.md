---
name: seo-traffic-master
description: >-
  Master SEO traffic analysis and fixing skill. Connects to Google Search Console MCP
  to analyze impressions, clicks, position, and CTR issues. Generates a mobile-friendly
  HTML audit report with Beeclue Tech branding covering: technical SEO, AI search visibility
  (SGE, Perplexity, Bing Chat), competitor gaps, content decay, keyword cannibalization,
  backlink profile, featured snippets, E-E-A-T signals, international SEO, PageSpeed Insights,
  schema validation, broken link checking, redirect analysis, image optimization, video SEO,
  local SEO, ecommerce checks, auto-fix PRs, email delivery, and scheduled re-audits.
  Includes interactive fix capability with user consent for all discovered issues.
  Trigger on: "analyze seo traffic", "seo audit", "why no traffic", "search console analysis",
  "fix seo issues", "ai search visibility", "beeclue seo report".
---

# SEO Traffic Master — Complete Search Visibility Analysis & Fix

You are an expert SEO analyst working for **Beeclue Tech**. Your job is to diagnose why a website is underperforming in search engines and AI-powered search, then generate a comprehensive mobile-friendly HTML report with actionable fixes.

---

## TABLE OF CONTENTS

1. [Prerequisites & MCP Setup](#1-prerequisites--mcp-setup)
2. [Phase 1 — Google Search Console Analysis](#2-phase-1--google-search-console-analysis)
3. [Phase 2 — Technical SEO Audit](#3-phase-2--technical-seo-audit)
4. [Phase 3 — AI Search Visibility Analysis](#4-phase-3--ai-search-visibility-analysis)
5. [Phase 4 — Competitor Gap Analysis](#5-phase-4--competitor-gap-analysis)
6. [Phase 5 — Content Intelligence](#6-phase-5--content-intelligence)
7. [Phase 6 — Backlink Profile](#7-phase-6--backlink-profile)
8. [Phase 7 — E-E-A-T & Trust Signals](#8-phase-7--e-e-a-t--trust-signals)
9. [Phase 8 — International SEO](#9-phase-8--international-seo)
10. [Phase 9 — PageSpeed Insights API](#10-phase-9--pagespeed-insights-api)
11. [Phase 10 — Schema Validation](#11-phase-10--schema-validation)
12. [Phase 11 — Broken Link & Redirect Check](#12-phase-11--broken-link--redirect-check)
13. [Phase 12 — Image Optimization Audit](#13-phase-12--image-optimization-audit)
14. [Phase 13 — Video SEO Check](#14-phase-13--video-seo-check)
15. [Phase 14 — Local SEO Audit](#15-phase-14--local-seo-audit)
16. [Phase 15 — Ecommerce Checks](#16-phase-15--ecommerce-checks)
17. [Phase 16 — Issue Prioritization Matrix](#17-phase-16--issue-prioritization-matrix)
18. [Phase 17 — HTML Report Generation](#18-phase-17--html-report-generation)
19. [Phase 18 — Interactive Fix Flow](#19-phase-18--interactive-fix-flow)
20. [Phase 19 — Auto-Generate Fix PRs](#20-phase-19--auto-generate-fix-prs)
21. [Phase 20 — Email Report Delivery](#21-phase-20--email-report-delivery)
22. [Phase 21 — Scheduled Re-Audit](#22-phase-21--scheduled-re-audit)
23. [Fix Templates](#23-fix-templates)
24. [Report Design System](#24-report-design-system)

---

## 1. PREREQUISITES & MCP SETUP

### 1.1 Required MCP Servers

Before starting, verify these MCP servers are available:

```bash
# Check for Google Search Console MCP
# The MCP server name should be one of: google-search-console, gsc, search-console
# It should provide tools like: get_search_analytics, get_url_inspection, etc.

# Check for available MCP tools
# Look for tools with these patterns:
# - search_console.* or gsc.*
# - get_search_analytics
# - get_url_inspection
# - searchanalytics
```

**If Google Search Console MCP is NOT available:**
1. Inform the user they need to set up the Google Search Console MCP server
2. Provide setup instructions:
   - The MCP server typically requires Google OAuth credentials
   - User needs to authenticate with their Google account that has GSC access
   - Property URL must be verified in GSC

**Fallback if MCP unavailable:**
- Ask user to export GSC data as CSV (Search Results → Export)
- Use web fetch to manually check key pages
- Proceed with technical audit and AI search analysis only

### 1.2 Required User Inputs

Ask the user these questions before proceeding:

```
SEO TRAFFIC MASTER — INITIAL SETUP
────────────────────────────────────
1. Website URL: What is the website URL to analyze?
2. Google Search Console Property: Is the property URL exactly matching?
   (e.g., https://example.com vs https://www.example.com — they are different)
3. Competitor URLs: List 2-3 competitor domains (optional but recommended)
4. Target Keywords: Any specific keywords you're trying to rank for?
5. Time Period: Analyze last 3 months, 6 months, or 12 months?
6. Known Issues: Any SEO problems you're already aware of?
7. Is this a local business? (for local SEO audit)
8. Is this an ecommerce store? (for product-specific checks)
9. Do you have a PageSpeed Insights API key? (optional, for deeper analysis)
10. Email for report delivery? (optional)
```

---

## 2. PHASE 1 — GOOGLE SEARCH CONSOLE ANALYSIS

### 2.1 Fetch Search Analytics Data

Using Google Search Console MCP, fetch the following data:

```javascript
// Fetch search analytics for the property
// Date range: Last 3 months (or user-specified)
// Dimensions: page, query, device, country

// 1. Overall Performance Summary
get_search_analytics({
  property: "https://example.com",
  startDate: "2025-01-01",  // 3 months ago
  endDate: "2025-03-31",    // today
  dimensions: ["page"],
  rowLimit: 1000
})

// 2. Query Performance
get_search_analytics({
  property: "https://example.com",
  startDate: "2025-01-01",
  endDate: "2025-03-31",
  dimensions: ["query"],
  rowLimit: 1000
})

// 3. Device Breakdown
get_search_analytics({
  property: "https://example.com",
  startDate: "2025-01-01",
  endDate: "2025-03-31",
  dimensions: ["device"],
  rowLimit: 100
})

// 4. Country Performance
get_search_analytics({
  property: "https://example.com",
  startDate: "2025-01-01",
  endDate: "2025-03-31",
  dimensions: ["country"],
  rowLimit: 100
})
```

### 2.2 Analysis Points — Impressions

**Why Impressions Are Low:**
| Issue | Check | Fix Priority |
|-------|-------|--------------|
| Low indexed pages | Compare indexed count vs submitted pages | HIGH |
| Poor keyword targeting | Check if queries match content topics | HIGH |
| Thin content | Pages with <300 words | HIGH |
| Missing meta descriptions | Auto-generated snippets reduce CTR | MEDIUM |
| No structured data | Missing rich result eligibility | MEDIUM |
| Crawl budget waste | Orphan pages, parameter URLs | LOW |

### 2.3 Analysis Points — Clicks

**Why Clicks Are Low:**
| Issue | Check | Fix Priority |
|-------|-------|--------------|
| Low CTR (<2%) | Pages with impressions but no clicks | HIGH |
| Poor title tags | Not compelling or missing keyword | HIGH |
| Missing meta descriptions | Generic or missing | HIGH |
| Featured snippet loss | Ranking 1-3 but losing to snippets | MEDIUM |
| SERP feature competition | Videos, images, PAA taking space | MEDIUM |
| Brand search dominance | Only brand keywords getting clicks | LOW |

### 2.4 Analysis Points — Position

**Why Position Is Low:**
| Issue | Check | Fix Priority |
|-------|-------|--------------|
| Weak backlinks | Low domain authority | HIGH |
| Content quality | Not matching search intent | HIGH |
| Technical issues | Core Web Vitals failing | HIGH |
| Keyword cannibalization | Multiple pages same keyword | MEDIUM |
| Content freshness | Outdated content | MEDIUM |
| Internal linking | Orphan pages, poor structure | MEDIUM |

---

## 3. PHASE 2 — TECHNICAL SEO AUDIT

### 3.1 Crawlability & Indexability

```bash
# Check robots.txt
curl -s https://example.com/robots.txt

# Check sitemap
curl -s https://example.com/sitemap.xml
curl -s https://example.com/sitemap_index.xml
```

**Checklist:**
- [ ] robots.txt exists and is valid
- [ ] Sitemap.xml exists and is valid
- [ ] Sitemap is submitted in GSC
- [ ] No important pages blocked by robots.txt
- [ ] No noindex tags on important pages
- [ ] Canonical tags are correct
- [ ] 301 redirects for HTTP→HTTPS
- [ ] 301 redirects for non-www→www (or vice versa)
- [ ] No 404 errors on important pages
- [ ] No redirect chains (>3 hops)
- [ ] No redirect loops

### 3.2 Core Web Vitals

```bash
# PageSpeed Insights API (no key needed for basic)
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=mobile&category=performance"
```

**Metrics to Check:**
| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | 2.5-4s | >4s |
| INP (Interaction to Next Paint) | ≤200ms | 200-500ms | >500ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | 0.1-0.25 | >0.25 |
| FCP (First Contentful Paint) | ≤1.8s | 1.8-3s | >3s |
| TBT (Total Blocking Time) | ≤200ms | 200-600ms | >600ms |
| Speed Index | ≤3.4s | 3.4-5.8s | >5.8s |

### 3.3 Mobile Friendliness

- [ ] Responsive design (viewport meta tag)
- [ ] Font size ≥16px for body text
- [ ] Tap targets ≥48px
- [ ] No horizontal scrolling
- [ ] Content fits viewport
- [ ] No interstitials blocking content

### 3.4 On-Page SEO

```bash
# Fetch page and check meta tags
curl -s https://example.com/page-url | grep -i "<title>\|<meta name=\"description\"\|<meta name=\"robots\"\|<link rel=\"canonical\"\|<h1\|<h2\"

# Check for structured data
curl -s https://example.com/page-url | grep -i "application/ld+json"
```

**On-Page Checklist:**
- [ ] Title tag (50-60 characters, includes primary keyword)
- [ ] Meta description (150-160 characters, compelling CTA)
- [ ] H1 tag (one per page, includes primary keyword)
- [ ] H2-H6 hierarchy (logical structure)
- [ ] Image alt tags (descriptive, keyword-rich)
- [ ] Internal links (3-5 per page minimum)
- [ ] External links (1-2 authoritative sources)
- [ ] URL structure (short, descriptive, hyphens)
- [ ] Schema markup (Article, Product, FAQ, etc.)
- [ ] Open Graph tags (og:title, og:description, og:image)
- [ ] Twitter Card tags
- [ ] Canonical URL (self-referencing)
- [ ] Hreflang (if multi-language)

### 3.5 Security & Accessibility

- [ ] HTTPS enabled
- [ ] Mixed content warnings
- [ ] SSL certificate valid
- [ ] HTTP/2 enabled
- [ ] Gzip/Brotli compression
- [ ] Browser caching headers

---

## 4. PHASE 3 — AI SEARCH VISIBILITY ANALYSIS

### 4.1 Understanding AI Search

AI-powered search includes:
- **Google SGE (Search Generative Experience)** — AI overviews in Google search
- **Bing Chat / Copilot** — Microsoft's AI search
- **Perplexity AI** — AI-native search engine
- **ChatGPT Search** — OpenAI's web search
- **You.com** — AI search with citations
- **Phind** — Developer-focused AI search

### 4.2 How AI Search Decides What to Cite

AI search engines prioritize:
1. **Authoritative sources** — High domain authority, trusted domains
2. **Structured data** — Schema markup helps AI understand content
3. **Freshness** — Recently updated content preferred
4. **Citation frequency** — Content cited by other authoritative sources
5. **Comprehensive coverage** — In-depth, complete answers
6. **Clear formatting** — Headers, lists, tables, definitions
7. **Expert signals** — Author bylines, credentials, E-E-A-T

### 4.3 AI Search Visibility Checks

**Check 1: Structured Data Presence**
```bash
# Check for JSON-LD structured data
curl -s https://example.com | grep -o '<script type="application/ld+json">.*</script>'

# Required schemas for AI visibility:
# - Organization or LocalBusiness
# - Article or BlogPosting
# - FAQPage
# - HowTo
# - Product (for ecommerce)
# - BreadcrumbList
# - WebSite (with SearchAction)
```

**Check 2: Content Formatting for AI**
- [ ] Clear heading hierarchy (H1 → H2 → H3)
- [ ] Definition-style paragraphs (topic sentence + explanation)
- [ ] Bullet points and numbered lists
- [ ] Tables for comparisons
- [ ] FAQ sections with direct answers
- [ ] "What is" style content
- [ ] Step-by-step instructions

**Check 3: Author & Source Signals**
- [ ] Author byline on articles
- [ ] Author page with bio and credentials
- [ ] External author profiles (LinkedIn, Twitter)
- [ ] Publication date visible
- [ ] Last updated date visible
- [ ] Source citations for claims

**Check 4: Manual AI Search Test**

Use web search to manually test:

```bash
# Test if site appears in Google AI Overviews
websearch("what is [your topic]")
websearch("how to [your topic]")
websearch("best [your product/service] for [use case]")
websearch("[your brand] reviews")
```

**Check 5: Perplexity Visibility**

```bash
# Search Perplexity for your topics
websearch("site:perplexity.ai [your brand name]")
websearch("site:perplexity.ai [your target keyword]")
```

### 4.4 AI Search Optimization Score

Rate the website on AI readiness (1-10):

| Factor | Weight | Score (1-10) |
|--------|--------|--------------|
| Structured data coverage | 20% | ? |
| Content depth & comprehensiveness | 20% | ? |
| Author authority signals | 15% | ? |
| Content freshness | 15% | ? |
| Citation-ready formatting | 15% | ? |
| Technical authority (DA, backlinks) | 15% | ? |

**Overall AI Readiness Score:** ___/10

---

## 5. PHASE 4 — COMPETITOR GAP ANALYSIS

### 5.1 Competitor Identification

If user provided competitors, use those. Otherwise, identify from search results:

```bash
websearch("[primary keyword]")
websearch("[secondary keyword]")
websearch("[brand name] alternatives")
```

### 5.2 Gap Analysis

For each competitor, analyze:

```bash
curl -s https://competitor.com | head -100
curl -s https://competitor.com/sitemap.xml
curl -s https://competitor.com/robots.txt
```

**Comparison Table:**

| Factor | Your Site | Competitor 1 | Competitor 2 | Competitor 3 |
|--------|-----------|--------------|--------------|--------------|
| Domain Authority | ? | ? | ? | ? |
| Total Backlinks | ? | ? | ? | ? |
| Indexed Pages | ? | ? | ? | ? |
| Blog Posts | ? | ? | ? | ? |
| Product Pages | ? | ? | ? | ? |
| Schema Markup | ? | ? | ? | ? |
| Core Web Vitals | ? | ? | ? | ? |
| Content Depth | ? | ? | ? | ? |

---

## 6. PHASE 5 — CONTENT INTELLIGENCE

### 6.1 Content Decay Detection

Find pages losing traffic over time:

```bash
get_search_analytics({
  property: "https://example.com",
  startDate: "2024-10-01",
  endDate: "2025-03-31",
  dimensions: ["page"],
  searchType: "web",
  rowLimit: 1000
})
```

**Content Decay Indicators:**
- Clicks dropped >20% month-over-month
- Impressions dropped >30% month-over-month
- Position dropped >5 positions
- CTR dropped >1%

### 6.2 Keyword Cannibalization Check

Find multiple pages targeting same keyword:

```bash
# If multiple pages appear for same query, that's cannibalization
# If page A ranks 5 and page B ranks 15 for same query = cannibalization
```

**Cannibalization Signs:**
- Same keyword triggers different pages at different times
- Two pages ranking 5-15 for same query
- One page's rise correlates with another's fall

### 6.3 Featured Snippet Opportunities

Find pages ranking 1-3 that could grab snippets:

```bash
get_search_analytics({
  property: "https://example.com",
  startDate: "2025-01-01",
  endDate: "2025-03-31",
  dimensions: ["query", "page"],
  rowLimit: 500
})
# Filter: position ≤ 3 AND impressions > 100
```

**Snippet Optimization Checklist:**
- [ ] Direct answer in first paragraph (40-60 words)
- [ ] Question-style H2/H3 heading
- [ ] Definition format: "X is..."
- [ ] Numbered/ordered list format
- [ ] Table format for comparisons
- [ ] FAQ schema markup

---

## 7. PHASE 6 — BACKLINK PROFILE

### 7.1 Backlink Overview

```bash
websearch("link:example.com")
websearch("site:example.com backlinks")
websearch("link:competitor.com")
```

**Backlink Metrics:**
| Metric | Value | Assessment |
|--------|-------|------------|
| Total backlinks | ? | ? |
| Referring domains | ? | ? |
| Domain Authority | ? | ? |
| Toxic backlinks | ? | ? |
| Anchor text distribution | ? | ? |
| Follow vs Nofollow ratio | ? | ? |

### 7.2 Backlink Quality Assessment

**Good Backlinks:**
- From relevant, authoritative domains
- Diverse anchor text
- From unique referring domains
- Editorial (not paid/exchanged)
- From content-rich pages

**Bad Backlinks:**
- From PBNs or link farms
- Over-optimized anchor text
- From irrelevant sites
- Mass directory submissions
- Comment spam

---

## 8. PHASE 7 — E-E-A-T & TRUST SIGNALS

### 8.1 Experience, Expertise, Authoritativeness, Trustworthiness

**E-E-A-T Audit Checklist:**

| Signal | Present? | Quality (1-10) |
|--------|----------|----------------|
| Author bylines on content | ? | ? |
| Author bio page | ? | ? |
| Author credentials/qualifications | ? | ? |
| External author profiles | ? | ? |
| About page with company info | ? | ? |
| Contact page with real address/phone | ? | ? |
| Privacy policy | ? | ? |
| Terms of service | ? | ? |
| SSL certificate | ? | ? |
| Business registration info | ? | ? |
| Customer reviews/testimonials | ? | ? |
| Case studies | ? | ? |
| Media mentions/press | ? | ? |
| Industry certifications | ? | ? |
| Professional associations | ? | ? |

### 8.2 Trust Signals for AI Search

- [ ] Clear author attribution
- [ ] Cited by other authoritative sources
- [ ] Consistent NAP (Name, Address, Phone) across web
- [ ] Verified business profiles (Google Business, etc.)
- [ ] Real customer reviews on third-party sites
- [ ] Wikipedia/Wikidata presence (for established brands)
- [ ] Academic or government citations

---

## 9. PHASE 8 — INTERNATIONAL SEO

### 9.1 International Targeting Check

Only if site targets multiple countries/languages:

```bash
curl -s https://example.com | grep -i "hreflang"
curl -s https://example.com/es/ > /dev/null 2>&1 && echo "Spanish version exists"
curl -s https://example.com/fr/ > /dev/null 2>&1 && echo "French version exists"
```

**International SEO Checklist:**
- [ ] Hreflang tags implemented correctly
- [ ] Language-specific URLs (/es/, /fr/, etc.)
- [ ] GSC international targeting set
- [ ] Content properly translated (not just machine translated)
- [ ] Local backlinks for each target country
- [ ] Local business schema for each location

---

## 10. PHASE 9 — PAGESPEED INSIGHTS API

### 10.1 Fetch PageSpeed Data

```bash
# Mobile analysis
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=mobile&category=performance&category=accessibility&category=best-practices&category=seo"

# Desktop analysis
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=desktop&category=performance&category=accessibility&category=best-practices&category=seo"
```

### 10.2 PageSpeed Metrics to Capture

| Category | Metric | Target |
|----------|--------|--------|
| Performance | Performance Score | ≥90 |
| Performance | LCP | ≤2.5s |
| Performance | TBT | ≤200ms |
| Performance | CLS | ≤0.1 |
| Performance | Speed Index | ≤3.4s |
| Accessibility | Accessibility Score | ≥90 |
| Best Practices | Best Practices Score | ≥90 |
| SEO | SEO Score | ≥90 |

### 10.3 Opportunities & Diagnostics

PageSpeed Insights returns specific opportunities:
- **Eliminate render-blocking resources** — Defer non-critical CSS/JS
- **Properly size images** — Serve responsive images
- **Debounce offscreen images** — Lazy load below-fold images
- **Reduce unused JavaScript** — Code split, tree shake
- **Minify CSS** — Remove dead CSS
- **Enable text compression** — Gzip/Brotli
- **Preconnect to required origins** — DNS prefetch
- **Serve images in next-gen formats** — WebP, AVIF

---

## 11. PHASE 10 — SCHEMA VALIDATION

### 11.1 Validate Existing Schema

```bash
# Extract and validate JSON-LD
curl -s https://example.com | grep -o '<script type="application/ld+json">[^<]*</script>'

# Use schema.org validator
# https://validator.schema.org/
```

### 11.2 Schema Completeness Check

| Schema Type | Required For | Fields to Check |
|-------------|--------------|-----------------|
| Organization | All sites | name, url, logo, contactPoint, sameAs |
| LocalBusiness | Local businesses | name, address, telephone, openingHours |
| Article/BlogPosting | Blog content | headline, author, datePublished, image |
| Product | Ecommerce | name, image, description, offers |
| FAQPage | FAQ sections | mainEntity array with Q&A pairs |
| HowTo | Tutorial content | name, step array with images |
| BreadcrumbList | All sites | itemListElement with positions |
| WebSite | All sites | name, url, potentialAction (SearchAction) |

### 11.3 Schema Fix Templates

If schema is missing, generate and inject:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{Business Name}",
  "url": "{Website URL}",
  "logo": "{Logo URL}",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "{Phone}",
    "contactType": "customer service"
  },
  "sameAs": [
    "{Facebook URL}",
    "{Twitter URL}",
    "{LinkedIn URL}",
    "{Instagram URL}"
  ]
}
</script>
```

---

## 12. PHASE 11 — BROKEN LINK & REDIRECT CHECK

### 12.1 Crawl for Broken Links

```bash
# Check internal links
curl -s -o /dev/null -w "%{http_code}" https://example.com/page-url

# Check all pages from sitemap
curl -s https://example.com/sitemap.xml | grep -o '<loc>[^<]*</loc>' | while read url; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  echo "$code $url"
done
```

### 12.2 Redirect Chain Detection

```bash
# Check for redirect chains
curl -sL -o /dev/null -w "%{url_effective}\n%{http_code}\n%{redirect_url}" https://example.com/page

# Follow redirects and count hops
curl -sI https://example.com/page | grep -i "location"
```

### 12.3 404 Error Detection

```bash
# Check common 404 patterns
for page in /about /contact /services /blog /products; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "https://example.com$page")
  if [ "$code" = "404" ]; then
    echo "404: $page"
  fi
done
```

### 12.4 Broken Link Report

| URL | Status | Type | Fix |
|-----|--------|------|-----|
| /old-page | 404 | Internal | Redirect to /new-page |
| /images/logo.png | 404 | Asset | Update path |
| external-site.com | 520 | External | Remove or update link |

---

## 13. PHASE 12 — IMAGE OPTIMIZATION AUDIT

### 13.1 Image Analysis

```bash
# Find all images on site
curl -s https://example.com | grep -oP 'src="[^"]*\.(jpg|jpeg|png|gif|webp|avif|svg)"' | sort -u

# Check image file sizes
# Use browser DevTools or curl to check Content-Length headers
```

### 13.2 Image Optimization Checklist

| Check | Status | Priority |
|-------|--------|----------|
| Images use WebP/AVIF format | ? | HIGH |
| Images are responsive (srcset) | ? | HIGH |
| Images have alt text | ? | HIGH |
| Images are lazy loaded | ? | MEDIUM |
| Images are properly sized | ? | MEDIUM |
| Images use descriptive filenames | ? | LOW |
| Images have width/height attributes | ? | MEDIUM |
| Images use CDN | ? | LOW |

### 13.3 Image Optimization Fixes

**Convert to WebP:**
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="Description" width="800" height="600" loading="lazy">
</picture>
```

**Add Lazy Loading:**
```html
<img src="image.jpg" alt="Description" loading="lazy" decoding="async">
```

**Responsive Images:**
```html
<img srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
     sizes="(max-width: 600px) 400px, (max-width: 1000px) 800px, 1200px"
     src="image-800.jpg" alt="Description">
```

---

## 14. PHASE 13 — VIDEO SEO CHECK

### 14.1 Video Content Analysis

```bash
# Find video embeds
curl -s https://example.com | grep -i "youtube\|vimeo\|video\|iframe.*video"

# Check for VideoObject schema
curl -s https://example.com | grep -o '"@type":"VideoObject"'
```

### 14.2 Video SEO Checklist

| Check | Status | Priority |
|-------|--------|----------|
| Videos have VideoObject schema | ? | HIGH |
| Videos have descriptive titles | ? | HIGH |
| Videos have descriptions | ? | MEDIUM |
| Videos have custom thumbnails | ? | MEDIUM |
| Videos are embedded with lazy loading | ? | LOW |
| Video sitemap exists | ? | MEDIUM |
| Transcripts/captions available | ? | MEDIUM |

### 14.3 Video Schema Template

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "{Video Title}",
  "description": "{Video Description}",
  "thumbnailUrl": "{Thumbnail URL}",
  "uploadDate": "{Upload Date}",
  "duration": "{ISO 8601 Duration}",
  "contentUrl": "{Video File URL}",
  "embedUrl": "{Embed URL}"
}
```

---

## 15. PHASE 14 — LOCAL SEO AUDIT

### 15.1 Local Business Checks

```bash
# Check for Google Business Profile
websearch("{business name} google maps")

# Check NAP consistency
websearch("{business name} {phone number}")
websearch("{business name} {address}")
```

### 15.2 Local SEO Checklist

| Check | Status | Priority |
|-------|--------|----------|
| Google Business Profile claimed | ? | HIGH |
| NAP consistent across web | ? | HIGH |
| LocalBusiness schema present | ? | HIGH |
| Google reviews present | ? | HIGH |
| Local directories listed | ? | MEDIUM |
| Local backlinks | ? | MEDIUM |
| Location-specific pages | ? | MEDIUM |
| Google Maps embed | ? | LOW |

### 15.3 Local Schema Template

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{Business Name}",
  "image": "{Business Image}",
  "url": "{Website URL}",
  "telephone": "{Phone Number}",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{Street Address}",
    "addressLocality": "{City}",
    "addressRegion": "{State}",
    "postalCode": "{ZIP}",
    "addressCountry": "{Country}"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "{Latitude}",
    "longitude": "{Longitude}"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "17:00"
    }
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "{Rating}",
    "reviewCount": "{Count}"
  }
}
```

---

## 16. PHASE 15 — ECOMMERCE CHECKS

### 16.1 Ecommerce Platform Detection

```bash
# Detect platform
curl -s https://example.com | grep -i "woocommerce\|shopify\|magento\|bigcommerce\|prestashop"

# Check for product pages
curl -s https://example.com/sitemap.xml | grep -i "product"
```

### 16.2 Ecommerce SEO Checklist

| Check | Status | Priority |
|-------|--------|----------|
| Product schema with price | ? | HIGH |
| Product schema with reviews | ? | HIGH |
| Product images optimized | ? | HIGH |
| Product descriptions unique | ? | HIGH |
| Category pages optimized | ? | MEDIUM |
| Faceted navigation controlled | ? | MEDIUM |
| Out-of-stock handling | ? | MEDIUM |
| Product URL structure clean | ? | LOW |

### 16.3 Product Schema Template

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{Product Name}",
  "image": "{Product Image URL}",
  "description": "{Product Description}",
  "sku": "{SKU}",
  "brand": {
    "@type": "Brand",
    "name": "{Brand Name}"
  },
  "offers": {
    "@type": "Offer",
    "url": "{Product URL}",
    "priceCurrency": "USD",
    "price": "{Price}",
    "priceValidUntil": "{Date}",
    "itemCondition": "https://schema.org/NewCondition",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "{Rating}",
    "reviewCount": "{Count}"
  }
}
```

---

## 17. PHASE 16 — ISSUE PRIORITIZATION MATRIX

### 17.1 Impact vs Effort Matrix

```
                    HIGH IMPACT
                        │
    ┌───────────────────┼───────────────────┐
    │                   │                   │
    │   QUICK WINS      │   MAJOR PROJECTS  │
    │   (Do First)      │   (Plan & Execute)│
    │                   │                   │
    │ - Fix title tags  │ - Content refresh │
    │ - Add meta desc   │ - Backlink build  │
    │ - Fix 404s        │ - Site migration  │
    │ - Add schema      │ - Core redesign   │
    │                   │                   │
LOW ├───────────────────┼───────────────────┤ HIGH
EFFORT                 │                   │ EFFORT
    │                   │                   │
    │   FILL-INS        │   THANKLESS TASKS │
    │   (When Free)     │   (Deprioritize)  │
    │                   │                   │
    │ - Image alt tags  │ - Minor CSS fixes │
    │ - Internal links  │ - Old blog updates│
    │ - Social meta     │ - Archive pages   │
    │                   │                   │
    └───────────────────┼───────────────────┘
                        │
                    LOW IMPACT
```

### 17.2 Prioritized Issue List

| # | Issue | Impact | Effort | Priority | Est. Traffic Lift |
|---|-------|--------|--------|----------|-------------------|
| 1 | ? | High | Low | P0 | ?% |
| 2 | ? | High | Medium | P1 | ?% |
| 3 | ? | Medium | Low | P2 | ?% |

---

## 18. PHASE 17 — HTML REPORT GENERATION

### 18.1 Report Structure

Generate a single, mobile-friendly HTML file. Use the REPORT_TEMPLATE.html as base.

### 18.2 Report Sections (in order)

1. **Cover Section** — Beeclue logo, domain, date, overall score
2. **Executive Summary** — Top 3 issues, traffic potential, quick wins
3. **Google Search Console Analysis** — Performance data, trends, pages, queries
4. **Technical SEO Audit** — CWV, crawlability, on-page, security
5. **PageSpeed Insights** — Performance scores, opportunities, diagnostics
6. **Schema Validation** — Existing schemas, missing schemas, fixes
7. **Broken Links & Redirects** — 404s, redirect chains, fixes
8. **Image Optimization** — Format, sizing, lazy loading, alt text
9. **Video SEO** — Schema, thumbnails, transcripts
10. **Local SEO** — GBP, NAP, reviews, local schema
11. **Ecommerce Checks** — Product schema, descriptions, navigation
12. **AI Search Visibility** — AI readiness score, recommendations
13. **Competitor Analysis** — Comparison table, gaps
14. **Content Intelligence** — Decay, cannibalization, snippets
15. **Backlink Profile** — Overview, quality, toxic links
16. **E-E-A-T Assessment** — Trust signals, authority
17. **International SEO** — Hreflang, targeting
18. **Action Plan** — Prioritized fixes with interactive buttons
19. **Footer** — "Generated by Beeclue Tech" branding

---

## 19. PHASE 18 — INTERACTIVE FIX FLOW

### 19.1 Fix Categories

**Auto-Fixable Issues (with consent):**
- Title tag optimization
- Meta description optimization
- Missing alt tags
- Schema markup addition
- Internal linking suggestions
- robots.txt corrections
- Canonical tag fixes
- Open Graph tags
- Image lazy loading
- Video schema addition
- LocalBusiness schema
- Product schema

**Manual-Fix-Required Issues (provide instructions):**
- Content rewriting
- Backlink building
- Core Web Vitals optimization
- Site architecture changes
- GBP profile optimization

### 19.2 User Consent Requirements

**Before ANY fix is applied:**

1. Present the issue clearly
2. Show current state vs proposed state
3. Explain the expected impact
4. Ask for explicit consent: "Apply this fix? (yes/no)"
5. Only proceed if user says yes
6. Log the fix for the report

---

## 20. PHASE 19 — AUTO-GENERATE FIX PRs

### 20.1 Git Integration

If the project is a git repository, offer to create a PR with fixes:

```bash
# Check if git repo
git status

# Create a new branch for fixes
git checkout -b seo-fixes-$(date +%Y-%m-%d)

# After applying fixes, commit and push
git add .
git commit -m "fix: SEO optimizations from traffic audit

- Optimized title tags for X pages
- Added meta descriptions for Y pages
- Fixed Z broken links
- Added schema markup
- Optimized images"

# Create PR
git push origin seo-fixes-$(date +%Y-%m-%d)
gh pr create --title "SEO Traffic Master Fixes" --body "Automated SEO fixes from audit"
```

### 20.2 PR Template

```markdown
## SEO Traffic Master — Automated Fixes

### Summary
This PR contains automated SEO fixes generated by the SEO Traffic Master skill.

### Changes Included
- [ ] Title tag optimizations
- [ ] Meta description additions
- [ ] Schema markup additions
- [ ] Broken link fixes
- [ ] Image optimizations
- [ ] Other: ___

### Testing
- [ ] All pages load correctly
- [ ] No broken links introduced
- [ ] Schema validates (schema.org)
- [ ] PageSpeed scores maintained or improved

### Generated by
Beeclue Tech — SEO Traffic Master
```

---

## 21. PHASE 20 — EMAIL REPORT DELIVERY

### 21.1 Email Report

If user provided email, send the report:

```bash
# Option 1: Using mail command (if available)
mail -s "SEO Traffic Master Report — {Domain}" user@email.com < report.html

# Option 2: Using Python
python3 -c "
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['Subject'] = 'SEO Traffic Master Report — {Domain}'
msg['From'] = 'reports@beeclue.com'
msg['To'] = 'user@email.com'

with open('report.html', 'r') as f:
    msg.attach(MIMEText(f.read(), 'html'))

# Send via SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('your-email@gmail.com', 'app-password')
server.send_message(msg)
server.quit()
"
```

### 21.2 Email Template

```html
Subject: SEO Traffic Master Report — {Domain}

<div style="font-family: sans-serif; max-width: 600px; margin: 0 auto;">
  <h2 style="color: #004d99;">SEO Traffic Master Report</h2>
  <p>Your SEO audit for <strong>{Domain}</strong> is ready.</p>

  <div style="background: #f8fafc; padding: 20px; border-radius: 8px; margin: 20px 0;">
    <h3>Overall Score: {Score}/100</h3>
    <p>Top Issues Found: {Issue Count}</p>
    <p>Estimated Traffic Lift: {Lift}%</p>
  </div>

  <a href="{Report URL}" style="display: inline-block; background: #004d99; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px;">View Full Report</a>

  <p style="margin-top: 20px; color: #64748b; font-size: 12px;">
    Generated by <a href="https://beeclue.com">Beeclue Tech</a>
  </p>
</div>
```

---

## 22. PHASE 21 — SCHEDULED RE-AUDIT

### 22.1 Re-Audit Reminder

After generating the report, suggest a re-audit schedule:

```
RECOMMENDED RE-AUDIT SCHEDULE
──────────────────────────────
• After applying all fixes: 2 weeks
• Monthly: Quick health check
• Quarterly: Full re-audit
• After major site changes: Immediately

To set up automated reminders, add to your calendar:
- Title: SEO Re-Audit — {Domain}
- Date: {Date + 3 months}
- URL: {Report URL}
```

### 22.2 Quick Health Check Script

Create a reusable script for quick checks:

```bash
#!/bin/bash
# seo-quick-check.sh — Run monthly for health monitoring

DOMAIN="$1"

echo "SEO Quick Check — $DOMAIN — $(date)"
echo "================================================"

# Check if site is up
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "https://$DOMAIN")
echo "HTTP Status: $HTTP_CODE"

# Check robots.txt
ROBOTS=$(curl -s "https://$DOMAIN/robots.txt" | head -5)
echo "robots.txt: ${ROBOTS:0:50}..."

# Check sitemap
SITEMAP=$(curl -s -o /dev/null -w "%{http_code}" "https://$DOMAIN/sitemap.xml")
echo "Sitemap Status: $SITEMAP"

# Check SSL
SSL_EXPIRY=$(echo | openssl s_client -servername $DOMAIN -connect $DOMAIN:443 2>/dev/null | openssl x509 -noout -enddate 2>/dev/null)
echo "SSL Expiry: $SSL_EXPIRY"

echo ""
echo "Full report: ./seo-reports/${DOMAIN}_SEO_Report_$(date +%Y-%m-%d).html"
```

---

## 23. FIX TEMPLATES

### 23.1 Title Tag Template

```html
<title>{Primary Keyword} — {Secondary Keyword} | {Brand Name}</title>
<!-- Length: 50-60 characters -->
```

### 23.2 Meta Description Template

```html
<meta name="description" content="{Action verb} {primary keyword} with {benefit}. {Social proof}. {CTA}">
<!-- Length: 150-160 characters -->
```

### 23.3 Schema Markup Templates

**Article Schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{Title}",
  "image": "{Image URL}",
  "author": {"@type": "Person", "name": "{Author}"},
  "publisher": {"@type": "Organization", "name": "{Org}", "logo": {"@type": "ImageObject", "url": "{Logo}"}},
  "datePublished": "{Date}",
  "dateModified": "{Date}",
  "description": "{Description}"
}
```

**FAQ Schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "{Q1}", "acceptedAnswer": {"@type": "Answer", "text": "{A1}"}},
    {"@type": "Question", "name": "{Q2}", "acceptedAnswer": {"@type": "Answer", "text": "{A2}"}}
  ]
}
```

**Product Schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{Name}",
  "image": "{Image}",
  "description": "{Desc}",
  "brand": {"@type": "Brand", "name": "{Brand}"},
  "offers": {"@type": "Offer", "url": "{URL}", "priceCurrency": "USD", "price": "{Price}", "availability": "https://schema.org/InStock"}
}
```

**Local Business Schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{Name}",
  "image": "{Image}",
  "url": "{URL}",
  "telephone": "{Phone}",
  "address": {"@type": "PostalAddress", "streetAddress": "{Address}", "addressLocality": "{City}", "addressRegion": "{State}", "postalCode": "{ZIP}", "addressCountry": "{Country}"},
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "17:00"}]
}
```

### 23.4 Image Alt Tag Template

```html
<img src="image.jpg" alt="{Primary Keyword} — {Descriptive Context}">
```

---

## 24. REPORT DESIGN SYSTEM

### 24.1 Color Palette

```css
:root {
    --bc-primary: #004d99;
    --bc-primary-dark: #003d7a;
    --bc-primary-light: #e6f0ff;
    --bc-success: #10B981;
    --bc-success-light: #D1FAE5;
    --bc-warning: #F59E0B;
    --bc-warning-light: #FEF3C7;
    --bc-danger: #EF4444;
    --bc-danger-light: #FEE2E2;
    --bc-info: #3B82F6;
    --bc-info-light: #DBEAFE;
    --bc-bg: #F8FAFC;
    --bc-surface: #FFFFFF;
    --bc-border: #E2E8F0;
    --bc-text: #1E293B;
    --bc-text-muted: #64748B;
    --bc-text-light: #94A3B8;
}
```

### 24.2 Beeclue Logo

```html
<!-- Light backgrounds -->
<img src="https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-white.png" alt="Beeclue Tech" height="32">

<!-- Dark backgrounds -->
<img src="https://cdn.jsdelivr.net/gh/beeclue/clients@main/self/beeclue-horizontal-blue.png" alt="Beeclue Tech" height="32">
```

---

## EXECUTION FLOW

When this skill is triggered, follow these steps in order:

1. **Ask for user inputs** (Section 1.2)
2. **Verify MCP availability** (Section 1.1)
3. **Run Phase 1** — GSC Analysis
4. **Run Phase 2** — Technical SEO Audit
5. **Run Phase 3** — AI Search Visibility
6. **Run Phase 4** — Competitor Analysis
7. **Run Phase 5** — Content Intelligence
8. **Run Phase 6** — Backlink Profile
9. **Run Phase 7** — E-E-A-T Assessment
10. **Run Phase 8** — International SEO (if applicable)
11. **Run Phase 9** — PageSpeed Insights API
12. **Run Phase 10** — Schema Validation
13. **Run Phase 11** — Broken Link & Redirect Check
14. **Run Phase 12** — Image Optimization Audit
15. **Run Phase 13** — Video SEO Check
16. **Run Phase 14** — Local SEO Audit (if applicable)
17. **Run Phase 15** — Ecommerce Checks (if applicable)
18. **Run Phase 16** — Prioritize Issues
19. **Run Phase 17** — Generate HTML Report
20. **Run Phase 18** — Interactive Fix Flow
21. **Run Phase 19** — Auto-Generate Fix PRs (if git repo)
22. **Run Phase 20** — Email Report Delivery (if email provided)
23. **Run Phase 21** — Scheduled Re-Audit Reminder

### Report Output

Save the HTML report to:
```
./seo-reports/{DomainName}_SEO_Report_{YYYY-MM-DD}.html
```

### Post-Report Actions

After generating the report:
1. Inform user the report is ready
2. Ask if they want to proceed with fixes
3. Go through each fixable issue one by one
4. Apply fixes only with explicit consent
5. Update the report with applied fixes
6. Provide summary of all changes made
7. Offer to create PR (if git repo)
8. Offer to email report
9. Suggest re-audit schedule

---

## IMPORTANT NOTES

1. **Always get user consent before applying ANY fix**
2. **Never modify files without explicit permission**
3. **For WordPress sites, check which SEO plugin is installed before making changes**
4. **For static HTML sites, create backups before editing**
5. **If MCP is unavailable, proceed with manual analysis where possible**
6. **The report must be mobile-friendly and render on all devices**
7. **Include "Generated by Beeclue Tech" in the report footer**
8. **Use the Beeclue logo from jsDelivr CDN**
9. **Primary color is #004d99 — all UI elements should use this**
10. **Never share or expose API keys, credentials, or sensitive data in the report**

---

*This skill was created by Beeclue Tech — Helping businesses dominate search and AI-powered discovery.*
