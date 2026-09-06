# Curated Unsplash Art Direction & Photographic Standards

Images define 70% of a website's emotional impact. By default, `beeclue-next-theme` utilizes high-resolution, curated Unsplash imagery optimized through Next.js `<Image>`.

---

## 1. Photographic Criteria for Apple-Grade Realism

### 1.1 Natural Light & Authentic Materiality
- **Lighting**: Favor natural daylight, diffused overcast skies, architectural golden hour, or intentional cinematic directional lighting.
- **Avoid**: Glossy 3D CGI plastic renders, oversaturated neon flares, and flat studio flash photography.
- **Composition**: Cinematic wide framing, intentional depth of field (shallow aperture focusing on materials or human interaction), and generous negative space for text overlays.

### 1.2 Aspect Ratio Standards

| Component / Use Case | Recommended Aspect Ratio | Next.js Container Classes |
| :--- | :--- | :--- |
| **Hero Background / Split** | 16:9 or 21:9 ultra-wide | `relative aspect-[16/9] lg:aspect-[21/9] w-full` |
| **Bento Grid Primary Cell** | 4:3 or 16:10 | `relative aspect-[4/3] w-full rounded-2xl overflow-hidden` |
| **Editorial Portrait / Bio** | 4:5 or 3:4 vertical | `relative aspect-[4/5] w-full rounded-xl overflow-hidden` |
| **Product / Macro Craft** | 1:1 square or 4:3 | `relative aspect-square w-full rounded-2xl overflow-hidden` |

---

## 2. Unsplash Image URL Construction

Always append dynamic formatting and quality parameters to Unsplash URLs:

```
https://images.unsplash.com/photo-[ID]?auto=format&fit=crop&w=[WIDTH]&q=[QUALITY]
```

- **Hero Banner**: `&w=2400&q=85`
- **Bento / Feature Grid**: `&w=1200&q=80`
- **Thumbnail / Avatar**: `&w=400&q=80`

---

## 3. Accessible Alt Text Formula

Never write lazy alt text like `alt="image"` or `alt="hero"`. Follow this formula:
`[Subject] + [Action/Setting] + [Brand/Contextual Significance]`
- ❌ `alt="office"`
- ✅ `alt="Architectural models and blueprints displayed on a solid oak drafting table in morning light"`
