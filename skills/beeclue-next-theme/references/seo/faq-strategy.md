# High-Conversion FAQ Strategy & Schema Pairing

A strategic FAQ section is one of the highest-leverage components on a business website: it overcomes buyer objections, reduces customer support friction, and captures Google rich snippets through `FAQPage` schema.

---

## 1. The 5 Essential FAQ Objection Archetypes

Every business website must include 5 to 8 targeted FAQs answering these specific customer hesitations:

1. **Pricing & Engagement Model**: How is the service billed? Are retainers, fixed scopes, or milestone payments used?
2. **Timeline & Velocity**: What is the standard onboarding time or project turnaround?
3. **Migration / Switch Friction**: How difficult is it to transition from a legacy vendor or internal system?
4. **Security, Compliance & Intellectual Property**: Who owns the work? What NDAs, SOC 2, or HIPAA safeguards exist?
5. **Post-Launch Support & Warranty**: What happens after deployment? How are bugs, maintenance, or iterations handled?

---

## 2. Pairing UI Accordion with Dynamic JSON-LD Schema

To avoid schema drift where visible text diverges from structured data, always generate the JSON-LD schema dynamically from the exact same TypeScript data array:

```tsx
// src/data/faqs.ts
export const architecturalFaqs = [
  {
    question: "What is the typical timeline for a bespoke residential architectural commission?",
    answer: "A complete bespoke residential project typically spans 12 to 18 months, encompassing schematic concept design, municipal permitting, contractor tendering, and on-site construction administration.",
  },
  {
    question: "Do you manage municipal zoning approvals and coastal permits?",
    answer: "Yes. Our team leads all environmental impact assessments, coastal commission filings, and municipal variance hearings directly with local authorities.",
  },
  {
    question: "How do you integrate passive sustainable engineering into your designs?",
    answer: "Every residence is calibrated to its micro-climate using computational solar orientation modeling, high-thermal-mass rammed earth or concrete walls, and cross-ventilation corridors.",
  },
];
```

Render both the accessible accordion and the JSON-LD schema in the same Server Component:

```tsx
import { FAQAccordion } from "@/components/sections/faq-accordion";
import { JsonLd } from "@/components/ui/json-ld";
import { generateFaqSchema } from "@/references/seo/jsonld-schemas";
import { architecturalFaqs } from "@/data/faqs";

export default function FAQSection() {
  return (
    <>
      <JsonLd data={generateFaqSchema(architecturalFaqs)} />
      <FAQAccordion items={architecturalFaqs} />
    </>
  );
}
```
