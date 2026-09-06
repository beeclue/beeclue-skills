# WCAG 2.1 AA Accessibility Standards for Next.js

An Apple-grade website is inclusive by default. We build strictly according to WCAG 2.1 AA standards, ensuring assistive technologies and keyboard-only users experience complete functional parity.

---

## 1. Keyboard Navigation & Focus Ring Standards

- **Tab Order**: Logical DOM order matching visual reading flow.
- **Visible Focus Rings**: Never remove outline styles with `outline: none` without providing an explicit replacement.
  ```css
  /* Apple-Grade Accessible Focus Style */
  :focus-visible {
    outline: 2px solid var(--primitive-blue-apple, #0071e3);
    outline-offset: 2px;
  }
  ```
- **Modal & Drawer Focus Trap**: When the mobile navigation drawer or dialog opens, focus is trapped inside the container and dismissed via the `Escape` key.

---

## 2. Touch Target Dimensions

All interactive buttons, links, toggles, and form inputs must provide a minimum clickable area of **44x44px**:

```tsx
// Good: Visual size can be compact, but tap target is padded
<button
  type="button"
  className="relative p-2.5 -m-2.5 flex items-center justify-center min-w-[44px] min-h-[44px]"
  aria-label="Close navigation"
>
  <X className="w-5 h-5" />
</button>
```

---

## 3. ARIA Semantics & Screen Reader Live Regions

- **Navigation**: `<nav aria-label="Main Navigation">`
- **Accordions**: `aria-expanded="true|false"`, `aria-controls="content-id"`
- **Live Updates**: Use `aria-live="polite"` for asynchronous search results or form submission messages.
- **Decorative SVGs**: Add `aria-hidden="true"` to purely decorative icons.
