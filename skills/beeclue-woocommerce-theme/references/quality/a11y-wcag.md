# Accessibility & WCAG 2.1/2.2 AA Compliance

Accessibility in BeeClue themes is not an optional afterthought—it is a non-negotiable architectural quality standard.

---

## 1. The Core WCAG AA Verification Suite

### 1.1 Focus Trap & Keyboard Cycling
All modal overlays (Cart Drawer, Full-Screen Search, Mobile Glassmorphic Nav) MUST trap the keyboard `Tab` cycle:
- Pressing `Tab` on the last focusable element wraps back to the first.
- Pressing `Shift + Tab` on the first element wraps to the last.
- Pressing `Escape` closes the overlay and immediately restores focus to the triggering button.

```javascript
function trapFocus(modalEl) {
    const focusable = modalEl.querySelectorAll(
        'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), [tabindex]:not([tabindex="-1"])'
    );
    if (!focusable.length) return;
    const first = focusable[0];
    const last  = focusable[focusable.length - 1];

    modalEl.addEventListener('keydown', (e) => {
        if (e.key !== 'Tab') return;
        if (e.shiftKey && document.activeElement === first) {
            last.focus();
            e.preventDefault();
        } else if (!e.shiftKey && document.activeElement === last) {
            first.focus();
            e.preventDefault();
        }
    });
}
```

---

## 2. Screen Reader Live Status (`aria-live="polite"`)

Whenever an AJAX operation occurs (item added to cart, quantity updated, free shipping unlocked), an assistive technology live region must announce the state change without refreshing the page:

```html
<!-- Placed in footer.php -->
<div id="a11y-live-status" class="sr-only" aria-live="polite" aria-atomic="true"></div>
```

```javascript
function announceToScreenReader(message) {
    const region = document.getElementById('a11y-live-status');
    if (!region) return;
    region.textContent = '';
    setTimeout(() => { region.textContent = message; }, 50);
}
```

---

## 3. Physical Touch Target Standards
- Every button, quantity stepper (`+` / `−`), variant swatch, and navigation link must occupy at least **`44x44px`** of interactive hit area.

## 4. Contrast Ratios
- Standard body text: minimum **4.5:1** contrast ratio.
- Headings & interactive element borders: minimum **3.0:1** contrast ratio.
