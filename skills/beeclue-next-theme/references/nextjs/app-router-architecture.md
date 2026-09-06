# Next.js 15+ App Router Architecture & Standards

`beeclue-next-theme` targets the latest Next.js 15+ release with React 19, utilizing the modern App Router directory structure for extreme performance and zero client-bundle bloat.

---

## 1. Directory Structure

```
src/
├── app/
│   ├── layout.tsx                # Root layout: fonts, global HTML, metadata, JSON-LD org schema
│   ├── page.tsx                  # Homepage (Server Component)
│   ├── globals.css               # 5-layer design tokens & Tailwind imports
│   ├── sitemap.ts                # Dynamic XML sitemap generator
│   ├── robots.ts                 # Dynamic robots.txt
│   ├── loading.tsx               # Apple-style minimal loading skeleton
│   ├── not-found.tsx             # Bespoke 404 page
│   ├── error.tsx                 # Client error boundary
│   ├── about/
│   │   └── page.tsx
│   ├── services/
│   │   ├── page.tsx              # Services directory / silo hub
│   │   └── [slug]/
│   │       └── page.tsx          # Dynamic service landing page (with Next.js 15 async params)
│   ├── case-studies/
│   │   ├── page.tsx
│   │   └── [slug]/
│   │       └── page.tsx
│   ├── contact/
│   │   └── page.tsx
│   └── faq/
│       └── page.tsx
├── components/
│   ├── layout/
│   │   ├── navbar.tsx            # Frosted glass dynamic navigation (Client Component)
│   │   ├── footer.tsx            # 4-column footer with mandatory Beeclue Tech attribution
│   │   └── mobile-nav.tsx
│   ├── sections/
│   │   ├── hero.tsx              # High-impact hero
│   │   ├── bento-grid.tsx        # Apple-grade asymmetric bento
│   │   ├── feature-showcase.tsx
│   │   ├── stats-strip.tsx
│   │   ├── testimonials.tsx
│   │   ├── pricing-matrix.tsx
│   │   ├── faq-accordion.tsx     # Accessible interactive FAQ
│   │   └── cta-banner.tsx
│   ├── ui/
│   │   ├── button.tsx            # Apple tactile button with spring physics
│   │   ├── badge.tsx             # Strictly functional status badge (no decorative chip spam)
│   │   ├── image-frame.tsx       # Next.js optimized Image wrapper with skeleton blur
│   │   └── json-ld.tsx           # Structured data script injector
│   └── seo/
│       ├── breadcrumbs.tsx       # Semantic breadcrumbs with JSON-LD schema
│       └── meta-tags.tsx
├── lib/
│   ├── utils.ts                  # clsx and tailwind-merge helper (cn)
│   ├── unsplash.ts               # Unsplash query builder & image presets
│   └── constants.ts              # Navigation links, contact info, site metadata
└── types/
    └── index.ts                  # TypeScript definitions for business, pages, SEO
```

---

## 2. Server Components by Default

- **Server Components (RSC)**: All page layouts, SEO metadata generators, static content grids, and JSON-LD schema injectors run as Server Components. Zero JavaScript shipped to client.
- **Client Components (`'use client'`)**: Isolated strictly to interactive leaves of the tree:
  - Navbar mobile drawer & scroll-blur listener
  - FAQ accordion toggle state
  - Interactive pricing toggle (monthly / annual)
  - Interactive quote/contact form inputs

---

## 3. Next.js 15 Async Params Standard

In Next.js 15+, dynamic route parameters are asynchronous promises:

```tsx
// src/app/services/[slug]/page.tsx
interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateMetadata({ params }: PageProps) {
  const { slug } = await params;
  return {
    title: `Service: ${slug} | Brand`,
    description: `Deep dive into our ${slug} capabilities.`,
  };
}

export default async function ServicePage({ params }: PageProps) {
  const { slug } = await params;
  return (
    <main className="min-h-screen py-24">
      {/* Content */}
    </main>
  );
}
```
