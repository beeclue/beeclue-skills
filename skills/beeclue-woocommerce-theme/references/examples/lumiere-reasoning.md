# Case Study: Lumière — A Study in Design Reasoning

> [!IMPORTANT]
> **Lumière is a study in Design Reasoning, NOT a reusable visual template.**
> Do NOT copy Lumière's terracotta color, Cormorant Garamond font, or warm cream backgrounds for other stores unless the client's Brand DNA independently demands it.
> Learn the **thought process** that created Lumière:
> $$\text{Brand Characteristics} \longrightarrow \text{Design Decisions} \longrightarrow \text{Technical Implementation}$$

---

## 1. The Brand Brief & Brand DNA Coordinates
- **Store Name**: Lumière
- **Niche**: Artisanal home goods, hand-thrown ceramics, botanical candles
- **Positioning**: Quiet Luxury / Artisanal Craft (`luxury: 85`, `warmth: 85`, `artisanal: 90`)
- **Customer Mindset**: Seeks tactile warmth, calm living spaces, anti-fast-furniture permanence.

---

## 2. The Design Reasoning Chain

### Decision 1: Palette
- *Reasoning*: Because the brand sells terracotta ceramics and natural soy candles, cold clinical stark `#FFFFFF` would feel sterile and cheap. 
- *Output*: Warm Linen canvas (`#F7F3EE`) paired with Tuscan Terracotta (`#C8602A`) accent.

### Decision 2: Zero Border-Radius
- *Reasoning*: While many retail sites use soft `16px` rounded cards, Lumière wanted the disciplined, sharp feel of an architectural monograph or gallery catalogue.
- *Output*: Strict `0px` radius on all image frames, balanced by soft organic curves *inside* the photographed ceramics.

### Decision 3: Linen Materiality
- *Reasoning*: Pure digital flat colors feel synthetic. 
- *Output*: Placeholder and container backgrounds received a subtle repeating linear gradient texture mimicking woven natural linen.

### Decision 4: Typography Balance
- *Reasoning*: High-end ceramics require literary nuance. 
- *Output*: `Cormorant Garamond` serif for editorial storytelling, grounded by `DM Sans` for clean, legible product pricing and descriptions.

---

## 3. The Technical Production Output
- **Header**: Sticky navigation with automatic light/dark logo transition on scroll.
- **Hero**: 60/40 asymmetric split with staggered fade-up CSS keyframes.
- **Product Grid**: Hover quick-add dispatches AJAX cart drawer without page refresh.
- **Cart Drawer**: Free shipping meter incentivizes reaching the $75 threshold.
- **Agency Attribution**: Mandatory Beeclue Tech footer link preserved with UTM parameters.
