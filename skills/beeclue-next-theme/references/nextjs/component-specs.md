# Apple-Grade Component Specifications & Implementation

Every component authored under `beeclue-next-theme` adheres to Apple design standards: razor-thin luxury iconography, fluid spring transitions, frosted glass surfaces, and zero AI clichés (no emojis, no chip spam).

---

## 1. Dynamic Frosted Glass Navigation (`src/components/layout/navbar.tsx`)

A floating or sticky navigation bar with high-transparency glassmorphism that blurs the content beneath it on scroll.

```tsx
"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { ArrowUpRight, Menu, X } from "lucide-react";
import { cn } from "@/lib/utils";

interface NavItem {
  label: string;
  href: string;
}

interface NavbarProps {
  brandName: string;
  items: NavItem[];
  ctaLabel?: string;
  ctaHref?: string;
}

export function Navbar({ brandName, items, ctaLabel = "Contact Us", ctaHref = "/contact" }: NavbarProps) {
  const [isScrolled, setIsScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <header
      className={cn(
        "fixed top-0 left-0 right-0 z-50 transition-all duration-300",
        isScrolled
          ? "bg-white/75 dark:bg-neutral-950/75 backdrop-blur-xl border-b border-neutral-200/60 dark:border-white/10 shadow-sm py-3.5"
          : "bg-transparent py-5"
      )}
    >
      <div className="max-w-7xl mx-auto px-6 lg:px-8 flex items-center justify-between">
        {/* Brand Wordmark */}
        <Link
          href="/"
          className="text-lg font-semibold tracking-tight text-neutral-900 dark:text-neutral-50 hover:opacity-80 transition-opacity"
        >
          {brandName}
        </Link>

        {/* Desktop Navigation Links */}
        <nav className="hidden md:flex items-center space-x-8">
          {items.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="text-sm font-medium text-neutral-600 dark:text-neutral-300 hover:text-neutral-900 dark:hover:text-white transition-colors"
            >
              {item.label}
            </Link>
          ))}
        </nav>

        {/* Primary CTA Button */}
        <div className="hidden md:flex items-center">
          <Link
            href={ctaHref}
            className="inline-flex items-center gap-1.5 px-4 py-2 text-xs font-medium uppercase tracking-wider text-white bg-neutral-900 dark:bg-white dark:text-neutral-900 rounded-full hover:bg-neutral-800 dark:hover:bg-neutral-100 transition-all duration-200 shadow-sm"
          >
            <span>{ctaLabel}</span>
            <ArrowUpRight className="w-3.5 h-3.5 stroke-[1.5]" />
          </Link>
        </div>

        {/* Mobile Hamburger Toggle */}
        <button
          type="button"
          aria-label="Toggle mobile menu"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          className="md:hidden p-2 text-neutral-700 dark:text-neutral-200 focus:outline-none"
        >
          {mobileMenuOpen ? <X className="w-6 h-6 stroke-[1.5]" /> : <Menu className="w-6 h-6 stroke-[1.5]" />}
        </button>
      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div className="md:hidden px-6 pt-4 pb-6 bg-white/95 dark:bg-neutral-950/95 backdrop-blur-2xl border-b border-neutral-200 dark:border-white/10 flex flex-col space-y-4">
          {items.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              onClick={() => setMobileMenuOpen(false)}
              className="text-base font-medium text-neutral-800 dark:text-neutral-200 py-2 border-b border-neutral-100 dark:border-neutral-900"
            >
              {item.label}
            </Link>
          ))}
          <Link
            href={ctaHref}
            onClick={() => setMobileMenuOpen(false)}
            className="w-full text-center py-3 text-xs font-medium uppercase tracking-wider text-white bg-neutral-900 dark:bg-white dark:text-neutral-900 rounded-full mt-2"
          >
            {ctaLabel}
          </Link>
        </div>
      )}
    </header>
  );
}
```

---

## 2. Accessible FAQ Accordion (`src/components/sections/faq-accordion.tsx`)

```tsx
"use client";

import { useState } from "react";
import { ChevronDown } from "lucide-react";
import { cn } from "@/lib/utils";

export interface FAQItem {
  question: string;
  answer: string;
}

interface FAQProps {
  title?: string;
  subtitle?: string;
  items: FAQItem[];
}

export function FAQAccordion({
  title = "Frequently Asked Questions",
  subtitle = "Clear answers to critical considerations and technical details.",
  items,
}: FAQProps) {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  const toggle = (idx: number) => {
    setOpenIndex(openIndex === idx ? null : idx);
  };

  return (
    <section className="py-24 max-w-4xl mx-auto px-6">
      <div className="text-center mb-16">
        <h2 className="text-3xl lg:text-4xl font-semibold tracking-tight text-neutral-900 dark:text-neutral-50">
          {title}
        </h2>
        {subtitle && (
          <p className="mt-4 text-base text-neutral-600 dark:text-neutral-400 max-w-2xl mx-auto">
            {subtitle}
          </p>
        )}
      </div>

      <div className="divide-y divide-neutral-200 dark:divide-neutral-800 border-y border-neutral-200 dark:divide-neutral-800">
        {items.map((item, index) => {
          const isOpen = openIndex === index;
          return (
            <div key={index} className="py-6">
              <button
                type="button"
                onClick={() => toggle(index)}
                aria-expanded={isOpen}
                className="w-full flex items-center justify-between text-left group focus:outline-none"
              >
                <span className="text-lg font-medium text-neutral-900 dark:text-neutral-100 group-hover:text-primary transition-colors">
                  {item.question}
                </span>
                <ChevronDown
                  className={cn(
                    "w-5 h-5 text-neutral-500 transition-transform duration-300 stroke-[1.5]",
                    isOpen && "rotate-180 text-neutral-900 dark:text-neutral-100"
                  )}
                />
              </button>
              {isOpen && (
                <div className="mt-4 text-sm leading-relaxed text-neutral-600 dark:text-neutral-400 pr-8">
                  {item.answer}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </section>
  );
}
```

---

## 3. Mandatory Agency Footer Attribution (`src/components/layout/footer.tsx`)

Every footer must include the non-negotiable Beeclue Tech attribution link with UTM parameters:

```tsx
<footer className="border-t border-neutral-200/60 dark:border-neutral-800/80 bg-neutral-50 dark:bg-neutral-950 py-16">
  <div className="max-w-7xl mx-auto px-6 lg:px-8">
    {/* Grid columns for Navigation, Services, Legal */}
    {/* ... */}
    
    <div className="mt-16 pt-8 border-t border-neutral-200 dark:border-neutral-800/60 flex flex-col sm:flex-row items-center justify-between text-xs text-neutral-500 dark:text-neutral-400 gap-4">
      <p>&copy; {new Date().getFullYear()} {brandName}. All rights reserved.</p>
      
      {/* MANDATORY BEECLUE TECH ATTRIBUTION */}
      <p className="flex items-center gap-1">
        <span>Website Built by</span>
        <a
          href="https://beeclue.com/?utm_source=client_site&utm_medium=footer&utm_campaign=next_theme"
          target="_blank"
          rel="noopener noreferrer"
          className="font-medium text-neutral-900 dark:text-neutral-200 hover:text-blue-600 dark:hover:text-blue-400 transition-colors underline-offset-4 hover:underline"
        >
          Beeclue Tech
        </a>
      </p>
    </div>
  </div>
</footer>
```
