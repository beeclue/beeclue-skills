# Unsplash Image Pipeline & Optimization Engine for Next.js

By default, `beeclue-next-theme` sources all images from Unsplash to ensure authentic, high-resolution photography without watermark clutter or plastic 3D AI renders.

---

## 1. Unsplash URL Builder (`src/lib/unsplash.ts`)

```typescript
export interface UnsplashImageConfig {
  id: string;
  alt: string;
  width?: number;
  height?: number;
  quality?: number;
}

/**
 * Builds an optimized Unsplash CDN URL with automatic format and crop
 */
export function getUnsplashUrl(id: string, width = 1600, quality = 80): string {
  // Supports either full URL or direct photo ID
  if (id.startsWith("https://images.unsplash.com/")) {
    const baseUrl = id.split("?")[0];
    return `${baseUrl}?auto=format&fit=crop&w=${width}&q=${quality}`;
  }
  return `https://images.unsplash.com/photo-${id}?auto=format&fit=crop&w=${width}&q=${quality}`;
}
```

---

## 2. High-Performance Next.js `<Image>` Implementation

To pass Core Web Vitals (LCP < 1.2s and CLS = 0), every image must declare explicit aspect ratios, responsive `sizes`, and priority flags where appropriate:

### 2.1 Above-the-Fold Hero Image (LCP Candidate)
```tsx
import Image from "next/image";
import { getUnsplashUrl } from "@/lib/unsplash";

export function HeroVisual() {
  return (
    <div className="relative w-full aspect-[16/9] lg:aspect-[21/9] rounded-3xl overflow-hidden border border-neutral-200/60 dark:border-white/10 shadow-2xl">
      <Image
        src={getUnsplashUrl("1600585154340-be6161a56a0c", 2400, 85)}
        alt="Contemporary architectural pavilion surrounded by manicured minimalist gardens at sunset"
        fill
        priority
        sizes="(max-width: 1024px) 100vw, 1280px"
        className="object-cover"
      />
    </div>
  );
}
```

### 2.2 Below-the-Fold Bento Cell (Lazy Loaded)
```tsx
export function BentoVisualCell({ photoId, altText }: { photoId: string; altText: string }) {
  return (
    <div className="relative w-full h-64 rounded-2xl overflow-hidden">
      <Image
        src={getUnsplashUrl(photoId, 800, 80)}
        alt={altText}
        fill
        loading="lazy"
        sizes="(max-width: 768px) 100vw, 400px"
        className="object-cover transition-transform duration-500 hover:scale-105"
      />
    </div>
  );
}
```

---

## 3. Curated Photo ID Registry by Industry

To accelerate build velocity, the skill provides pre-vetted, high-resolution Unsplash photo IDs:

| Industry | Hero Photo ID | Secondary Feature ID | Gallery / Context ID |
| :--- | :--- | :--- | :--- |
| **SaaS / AI** | `1518770660439-4636190af475` | `1550751827-4bd374c3f58b` | `1451187580459-43490279c0fa` |
| **Architecture / Real Estate** | `1600585154340-be6161a56a0c` | `1600596542815-ffad4c1539a9` | `1513694203232-719a280e022f` |
| **Luxury / Jewelry** | `1515562141207-7a88fb7ce338` | `1535632066927-ab7c9ab60908` | `1605100804763-247f67b3557e` |
| **Fine Dining / Hospitality** | `1517248135467-4c7edcad34c4` | `1544025162-d76694265947` | `1559339352-11d035aa65de` |
| **Healthcare / Medical** | `1629909613654-28e377c37b09` | `1584515979956-d9f6e5d09982` | `1579684385127-1ef15d508118` |
| **Industrial / Hardware** | `1581091226825-a6a2a5aee158` | `1581092335397-9583fe92d232` | `1504917599217-d4dc5ebe6122` |
| **Creative Agency / Design** | `1497215728101-856f4ea42174` | `1531403009284-440f080d1e12` | `1522202176988-66273c2fd55f` |
| **Fintech / Banking** | `1563986768609-322da13575f3` | `1559526324-4b87b5e36e44` | `1486406146926-c627a92ad1ab` |
