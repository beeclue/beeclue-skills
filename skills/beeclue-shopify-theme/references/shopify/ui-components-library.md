# Shopify OS 2.0 UI Components Library

This reference provides production-ready implementations for 22 high-converting, luxury-grade Shopify Online Store 2.0 UI components. Each component is engineered using modern Liquid, lightweight native Web Components (Custom Elements), strict WCAG 2.1 AA accessibility, and zero-framework CSS.

---

## 1. Multi-Column Mega Menu with Visual Promotion Tiles

### 1.1 Liquid Implementation (`sections/header.liquid` or `snippets/mega-menu.liquid`)
```liquid
<nav class="header-nav" aria-label="{{ 'general.navigation' | t }}">
  <ul class="nav-list list-unstyled" role="menubar">
    {%- for link in section.settings.menu.links -%}
      {%- assign has_mega = false -%}
      {%- for block in section.blocks -%}
        {%- if block.type == 'mega_menu' and block.settings.menu_title == link.title -%}
          {%- assign has_mega = true -%}
          {%- assign mega_block = block -%}
        {%- endif -%}
      {%- endfor -%}

      <li class="nav-item{% if has_mega %} nav-item-has-mega{% endif %}" role="none">
        <a href="{{ link.url }}" class="nav-link" role="menuitem" {% if link.active %}aria-current="page"{% endif %}>
          {{ link.title | escape }}
          {% if link.links != blank %}<span class="nav-chevron">{% render 'icon', name: 'chevron-down' %}</span>{% endif %}
        </a>

        {%- if has_mega -%}
          <div class="mega-menu-panel" role="region" aria-label="{{ link.title | escape }} sub-menu">
            <div class="mega-menu-container">
              <div class="mega-menu-links">
                {%- for child_link in link.links -%}
                  <div class="mega-column">
                    <h4 class="mega-column-title"><a href="{{ child_link.url }}">{{ child_link.title | escape }}</a></h4>
                    {%- if child_link.links != blank -%}
                      <ul class="mega-sublist list-unstyled">
                        {%- for grandchild_link in child_link.links -%}
                          <li><a href="{{ grandchild_link.url }}" class="mega-sublink">{{ grandchild_link.title | escape }}</a></li>
                        {%- endfor -%}
                      </ul>
                    {%- endif -%}
                  </div>
                {%- endfor -%}
              </div>

              {%- if mega_block.settings.promo_image != blank -%}
                <div class="mega-promo-tile">
                  <a href="{{ mega_block.settings.promo_url }}" class="mega-promo-card">
                    {{ mega_block.settings.promo_image | image_url: width: 600 | image_tag: loading: 'lazy', class: 'mega-promo-img' }}
                    <div class="mega-promo-meta">
                      <span class="mega-promo-badge">{{ mega_block.settings.promo_badge | escape }}</span>
                      <h5 class="mega-promo-heading">{{ mega_block.settings.promo_heading | escape }}</h5>
                      <span class="mega-promo-cta">{{ mega_block.settings.promo_cta | default: 'Shop Now' }} &rarr;</span>
                    </div>
                  </a>
                </div>
              {%- endif -%}
            </div>
          </div>
        {%- endif -%}
      </li>
    {%- endfor -%}
  </ul>
</nav>
```

---

## 2. Predictive Live Search Drawer & Modal

### 2.1 Web Component Markup (`snippets/predictive-search.liquid`)
```liquid
<predictive-search class="predictive-search-drawer" id="PredictiveSearch" aria-hidden="true">
  <div class="search-drawer-overlay" tabindex="-1"></div>
  <div class="search-drawer-dialog" role="dialog" aria-modal="true" aria-label="Search Store">
    <div class="search-drawer-header">
      <form action="{{ routes.search_url }}" method="get" role="search" class="search-drawer-form">
        <span class="search-input-icon">{% render 'icon', name: 'search' %}</span>
        <input type="search" name="q" id="SearchInput" class="search-input"
               placeholder="Search collections, craftsmanship, goods..."
               autocomplete="off" spellcheck="false" role="combobox"
               aria-expanded="false" aria-owns="predictive-search-results"
               aria-controls="predictive-search-results" aria-haspopup="listbox">
        <button type="button" class="search-clear-btn visually-hidden" aria-label="Clear query">{% render 'icon', name: 'close' %}</button>
      </form>
      <button type="button" class="search-close-btn" aria-label="Close search">{% render 'icon', name: 'close' %}</button>
    </div>

    <div id="predictive-search-results" class="predictive-search-results" tabindex="-1">
      <div class="search-popular-searches">
        <span class="search-section-label">Popular Searches</span>
        <div class="search-tags-list">
          <button type="button" class="search-tag-chip" data-query="Ceramics">Ceramics</button>
          <button type="button" class="search-tag-chip" data-query="Linen">Linen</button>
          <button type="button" class="search-tag-chip" data-query="Botanical">Botanical</button>
        </div>
      </div>
      <div class="search-live-content"></div>
    </div>
  </div>
</predictive-search>
```

### 2.2 JavaScript Controller (`assets/predictive-search.js`)
```javascript
class PredictiveSearch extends HTMLElement {
  constructor() {
    super();
    this.input = this.querySelector('input[type="search"]');
    this.resultsContainer = this.querySelector('.search-live-content');
    this.closeBtn = this.querySelector('.search-close-btn');
    this.overlay = this.querySelector('.search-drawer-overlay');
    this.debounceTimer = null;
  }

  connectedCallback() {
    this.input?.addEventListener('input', () => this.onInput());
    this.closeBtn?.addEventListener('click', () => this.close());
    this.overlay?.addEventListener('click', () => this.close());
    this.querySelectorAll('.search-tag-chip').forEach(btn => {
      btn.addEventListener('click', () => {
        this.input.value = btn.dataset.query;
        this.onChange();
      });
    });
  }

  open() {
    this.classList.add('active');
    this.setAttribute('aria-hidden', 'false');
    this.input.focus();
    document.body.classList.add('overflow-hidden');
  }

  close() {
    this.classList.remove('active');
    this.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('overflow-hidden');
  }

  onInput() {
    clearTimeout(this.debounceTimer);
    const query = this.input.value.trim();
    if (query.length < 2) {
      this.resultsContainer.innerHTML = '';
      return;
    }
    this.debounceTimer = setTimeout(() => this.fetchResults(query), 200);
  }

  async fetchResults(query) {
    const url = `${window.routes?.predictive_search_url || '/search/suggest'}?q=${encodeURIComponent(query)}&resources[type]=product,collection,article&resources[limit]=4&section_id=predictive-search`;
    const res = await fetch(url);
    const text = await res.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(text, 'text/html');
    const content = doc.querySelector('#shopify-section-predictive-search')?.innerHTML;
    if (content) this.resultsContainer.innerHTML = content;
  }
}
customElements.define('predictive-search', PredictiveSearch);
```

---

## 3. Quick View Modal (Ajax PDP pop-over)

Enables instantaneous product inspection and cart addition without abandoning collection browsing:

```liquid
<quick-view-modal id="QuickViewModal" class="quick-view-modal" aria-hidden="true">
  <div class="modal-overlay" tabindex="-1"></div>
  <div class="modal-container" role="dialog" aria-modal="true" aria-label="Product Quick View">
    <button type="button" class="modal-close-btn" aria-label="Close modal">{% render 'icon', name: 'close' %}</button>
    <div class="modal-body" id="QuickViewBody">
      <div class="modal-loading-skeleton">
        <div class="skeleton-media"></div>
        <div class="skeleton-info"></div>
      </div>
    </div>
  </div>
</quick-view-modal>
```

```javascript
class QuickViewModal extends HTMLElement {
  connectedCallback() {
    this.querySelector('.modal-overlay')?.addEventListener('click', () => this.close());
    this.querySelector('.modal-close-btn')?.addEventListener('click', () => this.close());
    document.addEventListener('quick-view:open', (e) => this.open(e.detail.productHandle));
  }

  async open(handle) {
    this.classList.add('active');
    this.setAttribute('aria-hidden', 'false');
    document.body.classList.add('overflow-hidden');
    const body = this.querySelector('#QuickViewBody');
    body.innerHTML = '<div class="loader-spinner"></div>';

    const res = await fetch(`/products/${handle}?section_id=quick-view-product`);
    const html = await res.text();
    const doc = new DOMParser().parseFromString(html, 'text/html');
    body.innerHTML = doc.querySelector('.quick-view-product-container')?.innerHTML || '';
  }

  close() {
    this.classList.remove('active');
    this.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('overflow-hidden');
  }
}
customElements.define('quick-view-modal', QuickViewModal);
```

---

## 4. Shoppable Lookbook / Image Hotspots (`sections/shoppable-image.liquid`)

Allows merchants to place interactive coordinate pins on lifestyle imagery that trigger product popovers:

```liquid
<div class="shoppable-lookbook-section" style="--hotspot-aspect: {{ section.settings.aspect_ratio }};">
  <div class="lookbook-frame">
    {{ section.settings.image | image_url: width: 2400 | image_tag: loading: 'lazy', class: 'lookbook-base-img' }}

    {%- for block in section.blocks -%}
      {%- assign product = block.settings.product -%}
      {%- if product != blank -%}
        <div class="hotspot-pin" style="top: {{ block.settings.top_percent }}%; left: {{ block.settings.left_percent }}%;" {{ block.shopify_attributes }}>
          <button type="button" class="hotspot-trigger" aria-label="View {{ product.title | escape }}" aria-expanded="false">
            <span class="hotspot-pulse"></span>
            <span class="hotspot-icon">+</span>
          </button>
          <div class="hotspot-card" role="tooltip">
            <a href="{{ product.url }}" class="hotspot-product-link">
              {{ product.featured_image | image_url: width: 160 | image_tag: loading: 'lazy', class: 'hotspot-thumb' }}
              <div class="hotspot-meta">
                <span class="hotspot-title">{{ product.title | escape }}</span>
                <span class="hotspot-price">{{ product.price | money }}</span>
              </div>
            </a>
            <button type="button" class="btn btn-sm btn-primary hotspot-quick-btn" onclick="addToCart({{ product.selected_or_first_available_variant.id }})">
              Add
            </button>
          </div>
        </div>
      {%- endif -%}
    {%- endfor -%}
  </div>
</div>
```

---

## 5. Interactive Before/After Image Comparison Slider (`sections/before-after-slider.liquid`)

Critical for beauty, skincare, home decor, materials, and restoration brands:

```liquid
<before-after-slider class="before-after-slider" style="--slider-position: 50%;">
  <div class="comparison-container">
    <div class="comparison-image-before">
      {{ section.settings.image_before | image_url: width: 1800 | image_tag: loading: 'lazy', class: 'comp-img' }}
      <span class="comparison-badge badge-before">{{ section.settings.label_before | default: 'Before' }}</span>
    </div>
    <div class="comparison-image-after">
      {{ section.settings.image_after | image_url: width: 1800 | image_tag: loading: 'lazy', class: 'comp-img' }}
      <span class="comparison-badge badge-after">{{ section.settings.label_after | default: 'After' }}</span>
    </div>
    <div class="comparison-handle" aria-hidden="true">
      <span class="handle-line"></span>
      <span class="handle-thumb">{% render 'icon', name: 'arrows-horizontal' %}</span>
      <span class="handle-line"></span>
    </div>
    <input type="range" min="0" max="100" value="50" class="comparison-range" aria-label="Slide to compare before and after images">
  </div>
</before-after-slider>
```

```javascript
class BeforeAfterSlider extends HTMLElement {
  connectedCallback() {
    const range = this.querySelector('.comparison-range');
    range?.addEventListener('input', (e) => {
      this.style.setProperty('--slider-position', `${e.target.value}%`);
    });
  }
}
customElements.define('before-after-slider', BeforeAfterSlider);
```

---

## 6. Size Chart & Fit Guide Drawer (`snippets/size-guide-drawer.liquid`)

Features an accessible slide-out drawer with dual unit toggles (Centimeters vs Inches):

```liquid
<size-guide-drawer id="SizeGuideDrawer" class="size-guide-drawer" aria-hidden="true">
  <div class="drawer-overlay" tabindex="-1"></div>
  <div class="drawer-panel" role="dialog" aria-modal="true" aria-label="Size Guide">
    <div class="drawer-header">
      <h3 class="drawer-title">Size & Fit Guide</h3>
      <button type="button" class="drawer-close-btn" aria-label="Close">{% render 'icon', name: 'close' %}</button>
    </div>
    <div class="drawer-content">
      <div class="unit-toggle" role="radiogroup" aria-label="Measurement Units">
        <button type="button" class="unit-btn active" data-unit="cm" role="radio" aria-checked="true">CM</button>
        <button type="button" class="unit-btn" data-unit="in" role="radio" aria-checked="false">Inches</button>
      </div>
      <table class="size-chart-table" aria-label="Clothing sizes">
        <thead>
          <tr><th>Size</th><th>Chest (<span class="unit-label">cm</span>)</th><th>Waist (<span class="unit-label">cm</span>)</th><th>Hip (<span class="unit-label">cm</span>)</th></tr>
        </thead>
        <tbody>
          <tr data-cm="92,76,96" data-in="36,30,38"><td>Small (S)</td><td class="c1">92</td><td class="c2">76</td><td class="c3">96</td></tr>
          <tr data-cm="98,82,102" data-in="38.5,32,40"><td>Medium (M)</td><td class="c1">98</td><td class="c2">82</td><td class="c3">102</td></tr>
          <tr data-cm="104,88,108" data-in="41,34.5,42.5"><td>Large (L)</td><td class="c1">104</td><td class="c2">88</td><td class="c3">108</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</size-guide-drawer>
```

---

## 7. Frequently Bought Together & Bundle Builder (`sections/frequently-bought-together.liquid`)

Automatically calculates bundled discount pricing when checkboxes are selected:

```liquid
<bundle-builder class="frequently-bought-together" data-discount-percentage="{{ section.settings.discount_percent | default: 15 }}">
  <h3 class="fbt-heading">{{ section.settings.heading | default: 'Frequently Bought Together' }}</h3>
  <div class="fbt-grid">
    <div class="fbt-items-list">
      {%- for product in recommendations.products limit: 3 -%}
        <div class="fbt-item" data-variant-id="{{ product.selected_or_first_available_variant.id }}" data-price="{{ product.selected_or_first_available_variant.price }}">
          <input type="checkbox" id="FBT-Check-{{ product.id }}" class="fbt-checkbox" checked>
          <label for="FBT-Check-{{ product.id }}" class="fbt-label">
            {{ product.featured_image | image_url: width: 140 | image_tag: loading: 'lazy', class: 'fbt-thumb' }}
            <div class="fbt-info">
              <span class="fbt-title">{{ product.title | escape }}</span>
              <span class="fbt-price">{{ product.price | money }}</span>
            </div>
          </label>
        </div>
      {%- endfor -%}
    </div>
    <div class="fbt-summary-panel">
      <div class="fbt-price-box">
        <span class="fbt-total-label">Total for all items:</span>
        <div class="fbt-prices">
          <span class="fbt-discounted-price">$0.00</span>
          <span class="fbt-original-price">$0.00</span>
        </div>
        <span class="fbt-savings-badge">Save {{ section.settings.discount_percent | default: 15 }}%</span>
      </div>
      <button type="button" class="btn btn-primary fbt-add-all-btn">
        Add Selected to Bag
      </button>
    </div>
  </div>
</bundle-builder>
```

---

## 8. Vertical Shoppable Video Carousel (`sections/shoppable-videos.liquid`)

Reels/TikTok style vertical 9:16 video cards with synchronized product quick-purchase tags:

```liquid
<div class="shoppable-videos-section">
  <div class="section-header">
    <h2 class="section-title">{{ section.settings.title | default: 'Seen In Action' }}</h2>
    <span class="section-subtitle">{{ section.settings.subtitle | default: 'Tap to inspect featured goods' }}</span>
  </div>
  <div class="video-reels-carousel">
    {%- for block in section.blocks -%}
      {%- assign product = block.settings.product -%}
      <div class="video-reel-card" {{ block.shopify_attributes }}>
        <video class="reel-video-player" playsinline loop muted preload="none" poster="{{ block.settings.poster_image | image_url: width: 600 }}">
          <source src="{{ block.settings.video_url }}" type="video/mp4">
        </video>
        {%- if product != blank -%}
          <div class="reel-product-pill">
            <a href="{{ product.url }}" class="reel-product-meta">
              {{ product.featured_image | image_url: width: 80 | image_tag: loading: 'lazy', class: 'reel-thumb' }}
              <div>
                <span class="reel-prod-title">{{ product.title | escape }}</span>
                <span class="reel-prod-price">{{ product.price | money }}</span>
              </div>
            </a>
            <button type="button" class="btn-reel-quick-add" onclick="addToCart({{ product.selected_or_first_available_variant.id }})" aria-label="Quick add">
              +
            </button>
          </div>
        {%- endif -%}
      </div>
    {%- endfor -%}
  </div>
</div>
```

---

## 9. Countdown Drop / Limited Edition Urgency Timer (`sections/countdown-banner.liquid`)

> **Shopify Theme Store Requirement (Section 8 Anti-Deception)**: Fictitious scarcity or fake countdown timers are **strictly forbidden**. This component must only be used for authentic, merchant-scheduled product drops or promotions with legitimate deadlines.

Dignified, editorial countdown timer without flashing red discounts:

```liquid
<countdown-timer class="countdown-drop-banner" data-end-time="{{ section.settings.end_timestamp }}">
  <div class="countdown-container">
    <span class="countdown-eyebrow">{{ section.settings.eyebrow | default: 'Limited Studio Allocation' }}</span>
    <h3 class="countdown-heading">{{ section.settings.heading | default: 'The Autumn Solstice Drop' }}</h3>
    <div class="countdown-digits" role="timer" aria-live="polite">
      <div class="digit-unit"><span class="digit-num days">00</span><span class="digit-label">Days</span></div>
      <div class="digit-sep">:</div>
      <div class="digit-unit"><span class="digit-num hours">00</span><span class="digit-label">Hours</span></div>
      <div class="digit-sep">:</div>
      <div class="digit-unit"><span class="digit-num minutes">00</span><span class="digit-label">Mins</span></div>
      <div class="digit-sep">:</div>
      <div class="digit-unit"><span class="digit-num seconds">00</span><span class="digit-label">Secs</span></div>
    </div>
  </div>
</countdown-timer>
```

---

## 10. Advanced Product Media Gallery with 3D AR (`model-viewer`)

```liquid
<div class="product-media-gallery" data-layout="{{ section.settings.gallery_layout }}">
  {%- for media in product.media -%}
    <div class="product-media-item" data-media-id="{{ media.id }}">
      {%- case media.media_type -%}
        {%- when 'image' -%}
          {{ media | image_url: width: 1800 | image_tag: loading: 'lazy', class: 'zoomable-image', alt: media.alt | escape }}
        {%- when 'video' -%}
          {{ media | video_tag: controls: true, loop: true, class: 'product-video' }}
        {%- when 'model' -%}
          <div class="model-viewer-wrapper">
            {{ media | model_viewer_tag: reveal: 'interaction', toggleable: true, ar: true }}
          </div>
      {%- endcase -%}
    </div>
  {%- endfor -%}
</div>
```

---

## 11. Product Provenance Tabs & Collapsible Accordions

```liquid
<div class="product-accordions-group">
  <details class="accordion-item" open>
    <summary class="accordion-header">
      <span class="accordion-title">Craftsmanship & Materials</span>
      <span class="accordion-chevron">{% render 'icon', name: 'chevron-down' %}</span>
    </summary>
    <div class="accordion-body prose">
      {{ product.metafields.custom.craftsmanship_details | default: product.description }}
    </div>
  </details>
  <details class="accordion-item">
    <summary class="accordion-header">
      <span class="accordion-title">Complimentary Shipping & Returns</span>
      <span class="accordion-chevron">{% render 'icon', name: 'chevron-down' %}</span>
    </summary>
    <div class="accordion-body prose">
      <p>Delivered via insured white-glove courier. 30-day effortless returns on undamaged originals.</p>
    </div>
  </details>
</div>
```

---

## 12. Faceted Collection Filtering & Active Filter Chips

Native storefront filtering synced with URL parameters:

```liquid
<form id="FacetFiltersForm" class="facets-form">
  <div class="facets-active-chips">
    {%- for filter in collection.filters -%}
      {%- for value in filter.active_values -%}
        <a href="{{ value.url_to_remove }}" class="facet-chip">
          {{ value.label | escape }} &times;
        </a>
      {%- endfor -%}
    {%- endfor -%}
  </div>

  {%- for filter in collection.filters -%}
    <details class="facet-filter-group" open>
      <summary class="facet-group-summary">{{ filter.label | escape }}</summary>
      <div class="facet-group-content">
        {%- case filter.type -%}
          {%- when 'boolean', 'list' -%}
            <ul class="facet-list list-unstyled">
              {%- for value in filter.values -%}
                <li>
                  <label class="facet-checkbox-label">
                    <input type="checkbox" name="{{ value.param_name }}" value="{{ value.value }}"
                           {% if value.active %}checked{% endif %}
                           {% if value.count == 0 and value.active == false %}disabled{% endif %}>
                    {{ value.label }} ({{ value.count }})
                  </label>
                </li>
              {%- endfor -%}
            </ul>
          {%- when 'price_range' -%}
            <div class="price-range-inputs">
              <input type="number" name="{{ filter.min_value.param_name }}" placeholder="0" min="0">
              <span>to</span>
              <input type="number" name="{{ filter.max_value.param_name }}" placeholder="{{ filter.range_max | divided_by: 100 }}">
            </div>
        {%- endcase -%}
      </div>
    </details>
  {%- endfor -%}
</form>
```

---

## 13. Shopify Markets Currency & Country Selector

```liquid
{%- form 'localization', id: 'LocalizationFooterForm' -%}
  <div class="localization-selector">
    <label for="CountrySelect" class="visually-hidden">Select Country / Currency</label>
    <select name="country_code" id="CountrySelect" onchange="this.form.submit()">
      {%- for country in localization.available_countries -%}
        <option value="{{ country.iso_code }}" {% if country.iso_code == localization.country.iso_code %}selected{% endif %}>
          {{ country.name }} ({{ country.currency.iso_code }} {{ country.currency.symbol }})
        </option>
      {%- endfor -%}
    </select>
  </div>
{%- endform -%}
```

---

## 14. Tiered Volume Pricing Table (`snippets/volume-pricing.liquid`)

```liquid
{%- if product.selected_or_first_available_variant.quantity_price_breaks.size > 0 -%}
  <div class="volume-pricing-table">
    <span class="volume-pricing-title">Volume Pricing Tiers:</span>
    <div class="tiers-grid">
      {%- for price_break in product.selected_or_first_available_variant.quantity_price_breaks -%}
        <div class="tier-badge">
          <span class="tier-qty">Buy {{ price_break.minimum_quantity }}+</span>
          <span class="tier-price">{{ price_break.price | money }}/ea</span>
        </div>
      {%- endfor -%}
    </div>
  </div>
{%- endif -%}
```

---

## 15. Milestone Free Gift with Purchase (GWP) Progress Bar

```liquid
<div class="cart-gwp-meter" data-gwp-threshold="150" data-subtotal="{{ cart.total_price | divided_by: 100 }}">
  <div class="gwp-header">
    <span class="gwp-text">
      {%- if cart.total_price >= 15000 -%}
        🎁 <strong>Unlocked!</strong> Complimentary Ceramic Incense Holder added to bag!
      {%- else -%}
        Add <strong>${{ 15000 | minus: cart.total_price | money_without_currency }}</strong> more to unlock your <strong>Gift with Purchase</strong>!
      {%- endif -%}
    </span>
  </div>
  <div class="gwp-bar" role="progressbar" aria-valuenow="{{ cart.total_price | times: 100 | divided_by: 15000 | at_most: 100 }}">
    <div class="gwp-bar-fill" style="width: {{ cart.total_price | times: 100 | divided_by: 15000 | at_most: 100 }}%;"></div>
  </div>
</div>
```

---

## 16. In-Drawer Order Notes & Gift Accordion (`snippets/cart-drawer-notes.liquid`)

```liquid
<details class="cart-notes-accordion">
  <summary class="cart-notes-summary">
    <span>{% render 'icon', name: 'gift' %} Add Complimentary Gift Card Message</span>
    <span>{% render 'icon', name: 'chevron-down' %}</span>
  </summary>
  <div class="cart-notes-content">
    <textarea name="note" class="cart-note-input" placeholder="Enter personal inscription...">{{ cart.note }}</textarea>
  </div>
</details>
```

---

## 17. Delivery Date & Estimated Shipping Calculator

```liquid
<div class="delivery-estimator" data-processing-days="2" data-transit-days="3">
  <span class="delivery-icon">{% render 'icon', name: 'clock' %}</span>
  <span class="delivery-copy">
    Order within <strong id="CutoffCountdown">4 hrs 12 mins</strong> to receive by <strong id="EstimatedArrivalDate">Thursday, Oct 24</strong>.
  </span>
</div>
```

---

## 18. Testimonials & Verified Buyer Photo Carousel (`sections/testimonials-carousel.liquid`)

```liquid
<div class="testimonials-section">
  <div class="testimonials-slider">
    {%- for block in section.blocks -%}
      <div class="testimonial-card" {{ block.shopify_attributes }}>
        <div class="testimonial-stars" aria-label="5 out of 5 stars">★★★★★</div>
        <blockquote class="testimonial-quote">"{{ block.settings.quote | escape }}"</blockquote>
        <div class="testimonial-author">
          {%- if block.settings.avatar != blank -%}
            {{ block.settings.avatar | image_url: width: 80 | image_tag: loading: 'lazy', class: 'author-avatar' }}
          {%- endif -%}
          <div>
            <span class="author-name">{{ block.settings.author | escape }}</span>
            <span class="author-location">{{ block.settings.location | escape }}</span>
          </div>
        </div>
      </div>
    {%- endfor -%}
  </div>
</div>
```

---

## 19. Press & Media Logo Cloud with Quote Highlights (`sections/press-ticker.liquid`)

```liquid
<div class="press-ticker-section">
  <div class="press-quotes-container">
    {%- for block in section.blocks -%}
      <div class="press-quote-item{% if forloop.first %} active{% endif %}" data-index="{{ forloop.index0 }}">
        <p class="press-quote-text">“{{ block.settings.quote | escape }}”</p>
        <span class="press-outlet">&mdash; {{ block.settings.outlet_name | escape }}</span>
      </div>
    {%- endfor -%}
  </div>
  <div class="press-logos-row">
    {%- for block in section.blocks -%}
      <div class="press-logo-wrapper" data-index="{{ forloop.index0 }}">
        {{ block.settings.logo | image_url: width: 240 | image_tag: loading: 'lazy', class: 'press-logo-img' }}
      </div>
    {%- endfor -%}
  </div>
</div>
```

---

## 20. Accessible Breadcrumbs with Schema.org `BreadcrumbList`

```liquid
<nav class="breadcrumbs" aria-label="Breadcrumbs">
  <ol class="breadcrumb-list list-unstyled" itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a href="{{ routes.root_url }}" itemprop="item"><span itemprop="name">Home</span></a>
      <meta itemprop="position" content="1">
    </li>
    {%- if template contains 'collection' -%}
      <li class="breadcrumb-sep">&sol;</li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <a href="{{ collection.url }}" itemprop="item" aria-current="page"><span itemprop="name">{{ collection.title | escape }}</span></a>
        <meta itemprop="position" content="2">
      </li>
    {%- elsif template contains 'product' -%}
      {%- if collection -%}
        <li class="breadcrumb-sep">&sol;</li>
        <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
          <a href="{{ collection.url }}" itemprop="item"><span itemprop="name">{{ collection.title | escape }}</span></a>
          <meta itemprop="position" content="2">
        </li>
      {%- endif -%}
      <li class="breadcrumb-sep">&sol;</li>
      <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
        <span itemprop="name" aria-current="page">{{ product.title | escape }}</span>
        <meta itemprop="position" content="{% if collection %}3{% else %}2{% endif %}">
      </li>
    {%- endif -%}
  </ol>
</nav>
```

---

## 21. Exit-Intent / Scroll-Triggered Newsletter Modal (`sections/newsletter-modal.liquid`)

```liquid
<newsletter-modal class="newsletter-modal" data-delay="{{ section.settings.delay_seconds | default: 5 }}" aria-hidden="true">
  <div class="modal-overlay" tabindex="-1"></div>
  <div class="modal-card" role="dialog" aria-modal="true" aria-label="Join Private Archive">
    <button type="button" class="modal-close" aria-label="Close">{% render 'icon', name: 'close' %}</button>
    <div class="modal-split-grid">
      {%- if section.settings.image != blank -%}
        <div class="modal-img-frame">
          {{ section.settings.image | image_url: width: 800 | image_tag: loading: 'lazy', class: 'modal-feature-img' }}
        </div>
      {%- endif -%}
      <div class="modal-content-panel">
        <span class="modal-eyebrow">{{ section.settings.eyebrow | default: 'Privé Club' }}</span>
        <h3 class="modal-title">{{ section.settings.title | default: 'Receive Invitations to Private Allocations' }}</h3>
        <p class="modal-desc">{{ section.settings.description | default: 'Subscribers receive early access to studio drops and exhibition catalogues.' }}</p>
        {%- form 'customer', class: 'modal-form' -%}
          <input type="email" name="contact[email]" class="modal-email-input" placeholder="Enter your email address..." required>
          <button type="submit" class="btn btn-primary modal-submit-btn">Request Access</button>
        {%- endform -%}
      </div>
    </div>
  </div>
</newsletter-modal>
```

---

## 22. Luxury Razor-Thin SVG Icon Set (`snippets/icon.liquid`)

Standardizes all icons with a 1.25px stroke, no bloated font icon libraries:

```liquid
{%- case name -%}
  {%- when 'search' -%}
    <svg class="icon icon-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
  {%- when 'cart' -%}
    <svg class="icon icon-cart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
  {%- when 'close' -%}
    <svg class="icon icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
  {%- when 'chevron-down' -%}
    <svg class="icon icon-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
  {%- when 'gift' -%}
    <svg class="icon icon-gift" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5A4.8 8 0 0 1 12 8a4.8 8 0 0 1 4.5-5 2.5 2.5 0 0 1 0 5"/></svg>
  {%- when 'clock' -%}
    <svg class="icon icon-clock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
{%- endcase -%}
```

---

## 23. Mandatory Shopify Theme Store Core Components

Per [Shopify Theme Store Requirements](theme-store-requirements.md), every theme must natively implement these core components:

1. **Account Component**: `<shopify-account></shopify-account>` rendered in both desktop and mobile header navigation.
2. **Follow on Shop Button**: `{{ shop | login_button: action: 'follow' }}` rendered with unaltered branded styling.
3. **Pickup Availability**: Render store local pickup availability on PDP using `variant.store_availabilities`.
4. **Shop Pay Installments Banner**: `{{ form | payment_terms }}` inside the PDP product form.
5. **Accelerated Checkout Buttons**: `{{ form | payment_button }}` on PDP and `content_for_additional_checkout_buttons` on Cart page.
6. **Gift Card Recipient Form**: Inputs for `recipient[email]`, `recipient[name]`, `recipient[message]`, and `recipient[send_on]` on PDP for gift card products.
7. **Selling Plans & Subscriptions**: Subscription allocation selector on PDP and selling plan badges in Cart drawer / Cart page.
8. **Unit Pricing**: Output `variant.unit_price` and `variant.unit_price_measurement` on PDP, collection grid cards, and cart items.
