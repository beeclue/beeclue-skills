# Commerce Strategy & Conditional Feature Architecture

Not every digital storefront should feature the exact same e-commerce mechanisms. Commercial patterns must be explicitly enabled or disabled based on business model, AOV tier, and brand positioning.

---

## 1. The Strategic Feature Enablement Matrix

| Commerce Feature | Haute Luxury ($1,000+) | Modern Premium ($150–$600) | High-Velocity ($20–$100) | B2B Equipment ($2,000+) |
| :--- | :--- | :--- | :--- | :--- |
| **Free Shipping Meter** | ❌ Disabled (Destroys prestige) | ⚠️ Enabled if shipping is conditional | ✅ Crucial AOV lever (Prominent) | ❌ Disabled (Freight calculated) |
| **Sticky PDP Buy Bar** | ⚠️ Subtle pill on scroll | ✅ Full sticky conversion bar | ✅ Full sticky conversion bar | ⚠️ Sticky "Request Quote" bar |
| **Variant Swatches** | ✅ Visual color circles & sizes | ✅ Visual swatches | ✅ Visual swatches + badges | ✅ Material / Spec dropdowns |
| **One-Click Cross-Sells**| ❌ Disabled (Feels cheap) | ✅ Curated pairings (1–2 max) | ✅ High-velocity accessory add-ons | ✅ Matching accessories / tools |
| **Discount Strikethroughs**| ❌ Strictly prohibited | ⚠️ Restricted to seasonal sales | ✅ High-contrast sale badges | ⚠️ Tiered volume discounts |
| **Subscription Toggle** | ❌ N/A | ⚠️ Replenishment goods only | ✅ Crucial for recurring items | ⚠️ Maintenance contracts |
| **Sample Selectors** | ❌ Upon request | ✅ Excellent for skincare/tea | ⚠️ Cart threshold gift | ⚠️ Material swatch kit |

---

## 2. Dynamic Free Shipping Threshold Formula

When a free shipping progress bar is strategically enabled, the threshold should be computed based on the store's average basket metrics:

$$\text{Threshold} = \text{Current AOV} \times 1.25 \quad \text{to} \quad \text{Current AOV} \times 1.35$$

*Example*: If average order value is $52.00, set the free shipping threshold at **$70.00** or **$75.00** to incentivize adding a complementary second item.

---

## 3. The Bespoke PDP Strategy Rule

Before writing single product template code, determine:
1. Is this an **impulse buy** (e.g. phone case, organic socks) $\rightarrow$ Focus on rapid Add-to-Cart with immediate Apple Pay?
2. Or a **high-consideration investment** (e.g. mechanical chronograph, wool sectional sofa) $\rightarrow$ Focus on craftsmanship storytelling, dimensional schematics, and concierge consultation?
