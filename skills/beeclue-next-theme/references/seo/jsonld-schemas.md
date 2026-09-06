# Dynamic JSON-LD Structured Data Schemas for Next.js

JSON-LD structured data provides explicit semantic clues about the meaning of a page to Google and AI recommendation engines, enabling rich search snippets and citation authority.

---

## 1. Reusable JSON-LD Component (`src/components/ui/json-ld.tsx`)

```tsx
interface JsonLdProps {
  data: Record<string, unknown> | Array<Record<string, unknown>>;
}

export function JsonLd({ data }: JsonLdProps) {
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data) }}
    />
  );
}
```

---

## 2. Global Organization & WebSite Schemas (`src/app/layout.tsx`)

```tsx
const organizationSchema = {
  "@context": "https://schema.org",
  "@type": "Organization",
  name: "Vanguard Studio",
  url: "https://clientdomain.com",
  logo: "https://clientdomain.com/logo.png",
  sameAs: [
    "https://twitter.com/vanguardstudio",
    "https://linkedin.com/company/vanguardstudio",
    "https://instagram.com/vanguardstudio",
  ],
  contactPoint: {
    "@type": "ContactPoint",
    telephone: "+1-555-019-2834",
    contactType: "customer service",
    availableLanguage: ["English"],
  },
};

const websiteSchema = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  name: "Vanguard Studio",
  url: "https://clientdomain.com",
  potentialAction: {
    "@type": "SearchAction",
    target: "https://clientdomain.com/search?q={search_term_string}",
    "query-input": "required name=search_term_string",
  },
};
```

---

## 3. Dynamic FAQPage Schema (`src/app/faq/page.tsx` or FAQ Sections)

```tsx
export function generateFaqSchema(faqs: Array<{ question: string; answer: string }>) {
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faqs.map((faq) => ({
      "@type": "Question",
      name: faq.question,
      acceptedAnswer: {
        "@type": "Answer",
        text: faq.answer,
      },
    })),
  };
}
```

---

## 4. BreadcrumbList Schema for Inner Pages

```tsx
export function generateBreadcrumbSchema(items: Array<{ name: string; url: string }>) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      name: item.name,
      item: item.url,
    })),
  };
}
```

---

## 5. LocalBusiness Schema for Physical Practices

For medical clinics, architectural offices, restaurants, and law firms, output `LocalBusiness` / `MedicalClinic` / `Restaurant`:

```json
{
  "@context": "https://schema.org",
  "@type": "ArchitecturalFirm",
  "name": "Vanguard Studio",
  "image": "https://clientdomain.com/office.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "450 Sutter Street, Suite 1400",
    "addressLocality": "San Francisco",
    "addressRegion": "CA",
    "postalCode": "94108",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 37.7897,
    "longitude": -122.4082
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "09:00",
    "closes": "18:00"
  }
}
```
