# Product Discovery, Faceted Filtering & Search

Product discovery bridges visitor curiosity to transaction without friction. Superclass stores turn catalogs into intuitive, responsive galleries.

---

## 1. Full-Screen Accessible Search Overlay

Every BeeClue theme provides a full-screen, focused search overlay rather than a cramped input field in the header.

### 1.1 Architecture
- **Trigger**: Search icon SVG in desktop navigation or mobile menu.
- **Focus**: Instant autofocus on `<input type="search">` with smooth scale-down backdrop blur.
- **Escape Key Listener**: Closes overlay immediately and restores focus to triggering icon.
- **Quick Links**: Direct pills to "Popular Searches", "New Arrivals", and primary collections.

---

## 2. Faceted Filtering Architecture

For catalogs with $> 12$ products, provide an accessible, slide-out or horizontal filter bar:

- **Filter Dimensions by Industry**:
  - *Skincare*: Skin concern (hydration, anti-aging), active ingredient (retinol, AHA), texture (cream, oil, serum).
  - *Fashion*: Size, color, fabric composition, fit, occasion.
  - *Furniture*: Room type, primary material, seating capacity, colorway.
- **Tactile Filter Pills**: Active filters appear as dismissible tags with instant count badges.
- **Zero Page Reload (AJAX)**: Filtering updates the WooCommerce product loop via AJAX, avoiding jarring full-page refreshes.

---

## 3. Product Card Ergonomics

Every card in a category grid must be an interactive micro-application:
1. **Aspect Ratio Lock**: Native CSS `aspect-ratio: 1 / 1` or `4 / 5` prevents Cumulative Layout Shift (CLS 0.00).
2. **Secondary Hover Crossfade**: Hovering the card smoothly fades in a second angle, on-model lifestyle photo, or macro texture.
3. **Hover Quick-Add**: A tactile Add-to-Cart pill slides up on card hover (`translateY(0)`), dispatching an AJAX cart addition without redirecting to the product page.
4. **Color Swatch Preview**: Display up to 5 small color dots beneath the title; hovering a dot swaps the displayed card thumbnail.
