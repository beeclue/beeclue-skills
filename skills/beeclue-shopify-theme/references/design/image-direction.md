# Image Art Direction & Photographic Briefs

High-converting commerce experiences treat photography as structural architecture, not arbitrary decoration. Every image slot must fulfill a specific compositional and storytelling brief.

---

## 1. Structured Image Art Direction Schema

When specifying images for clients, photolibraries (e.g., curated Unsplash), or AI generation tools, emit structured YAML briefs:

```yaml
image_brief:
  placement: "homepage-hero"
  slot_role: "hero-split-primary"
  subject: "Ceramicist hands shaping a raw stoneware vase on an electric wheel"
  environment: "Sunlit daylight studio with concrete floors and linen backdrops"
  composition:
    rule_of_thirds: "Subject aligned to right 2/3"
    negative_space: "Left 1/3 uncluttered for headline overlay"
    focal_point: "Wet clay texture and artisan hands"
  lighting:
    type: "Diffused morning window light"
    direction: "Side lit from right (45 degrees)"
    shadows: "Soft natural gradient, no harsh flash"
  camera:
    lens: "50mm prime f/2.0"
    depth_of_field: "Shallow, soft organic background blur"
  color_grading:
    temperature: "Warm neutral (5200K)"
    palette: ["#F7F3EE", "#8A7968", "#C8602A", "#1C1915"]
  technical:
    aspect_ratio: "16:9 desktop, 4:5 mobile"
    desktop_crop: "w=1600&h=900&fit=crop"
    mobile_crop: "w=800&h=1000&fit=crop"
    format: "webp"
    loading: "eager"
```

---

## 2. Layout-Driven Negative Space Rules

- **Headline Over Image (Hero)**: Image MUST have intentional negative space or deep shadow where text sits. Never place text over high-frequency visual detail.
- **Product Cards**: Consistent aspect ratio (`1:1` square or `3:4` vertical portrait). Products photographed from identical eye-level elevation (15-degree tilt) with soft ground shadows.
- **Editorial Splits**: Portrait orientation (`4:5` ratio) showing human interaction or macro craftsmanship close-up.

---

## 3. Direct Curated Unsplash CDN Catalog

Always append explicit crop, width, height, and WebP parameters:
`https://images.unsplash.com/photo-{ID}?w={WIDTH}&h={HEIGHT}&fit=crop&auto=format&q=80`

### Niche Photo Sets:
- **Luxury Ceramics / Home**:
  - Hero: `photo-1616486338812-3dadae4b4ace`
  - Editorial: `photo-1618221195710-dd6b41faaea6`
  - Product: `photo-1567538096630-e0c55bd6374c`
- **Fine Jewelry**:
  - Hero: `photo-1515562141589-67f0d569b6c0`
  - Macro Detail: `photo-1535632066927-ab7c9ab60908`
  - Model: `photo-1603561591411-07134e71a2a9`
- **Clinical Botanical Skincare**:
  - Dropper / Texture: `photo-1596462502278-27bfdc403348`
  - Amber Bottle: `photo-1608248543803-ba4f8c70ae0b`
  - Botanical Studio: `photo-1570172619644-dfd03ed5d881`
