# Performance Optimization & Core Web Vitals (90+ CWV)

BeeClue themes are engineered from the ground up for instantaneous response times, targeting consistent 90+ Google PageSpeed and Lighthouse scores.

---

## 1. The Core Web Vitals Benchmarks

- **Largest Contentful Paint (LCP)**: $\le 2.5\text{s}$ (Hero image preloaded, fonts preconnected)
- **Cumulative Layout Shift (CLS)**: $\le 0.05$ (Strict aspect ratio containers, explicit dimensions)
- **Interaction to Next Paint (INP)**: $\le 200\text{ms}$ (Zero main-thread blocking JavaScript)

---

## 2. Zero-Dependency Animation Philosophy

Under NO circumstances may heavy external animation runtimes (GSAP, AOS, ScrollReveal, Framer Motion) be enqueued in production themes.

### The Lightweight Scroll Reveal Engine (`~20 lines` JS):
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const reveals = document.querySelectorAll('.reveal');
    if (!reveals.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    reveals.forEach(el => observer.observe(el));
});
```

---

## 3. WordPress Head Optimization (`inc/performance.php`)

```php
// Remove WordPress legacy head bloat
remove_action('wp_head', 'rsd_link');
remove_action('wp_head', 'wlwmanifest_link');
remove_action('wp_head', 'wp_generator');
remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('wp_print_styles', 'print_emoji_styles');

// Defer non-critical theme scripts
add_filter('script_loader_tag', function($tag, $handle) {
    if (in_array($handle, ['theme-main', 'theme-cart', 'theme-animations'])) {
        return str_replace(' src', ' defer src', $tag);
    }
    return $tag;
}, 10, 2);

// Preconnect to Google Fonts and Unsplash CDN
add_action('wp_head', function() {
    echo '<link rel="preconnect" href="https://fonts.googleapis.com">' . "\n";
    echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
    echo '<link rel="preconnect" href="https://images.unsplash.com">' . "\n";
}, 1);
```
