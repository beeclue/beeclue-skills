# Motion-Primitives Integration (`https://motion-primitives.com/`)

To achieve true Apple-grade fluidity, `beeclue-next-theme` provides native integration with **[Motion-Primitives](https://motion-primitives.com/)** (open-source motion components for React & Tailwind CSS built on `motion/react`).

---

## 1. Core Package Installation

When motion-primitives animations are requested or selected in the Design Contract, install the lightweight motion runtime:

```bash
npm install motion react-use-measure
```

*(Note: `motion` is the modern unified package for Framer Motion, supporting React 19 and Next.js 15 App Router out of the box).*

---

## 2. The 9 Essential Motion-Primitives for Apple-Grade Flagships

| Primitive | What It Does | Apple-Grade Application |
| :--- | :--- | :--- |
| **`TextShimmer`** | Subtle specular light passing across text | Hero eyebrow tags and focal value propositions (eliminates cheap gradients) |
| **`MorphingDialog`** | Card smoothly morphs into a full modal via `layoutId` | Portfolio case studies, service deep-dives, and video showreels |
| **`InfiniteSlider`** | Continuous frictionless marquee loop | Client logo trust bars, partner indices, certification strips |
| **`Spotlight`** | Radial flashlight effect following cursor on hover | Bento grid feature cards and interactive pricing containers |
| **`BorderTrail`** | Subtle luminous particle traveling along a 1px border | Highlighting active tier or mission-critical architecture cards |
| **`Magnetic`** | Button or icon magnetically pulled toward cursor | Primary CTA buttons, audio controls, and navigational action triggers |
| **`AnimatedBackground`** | Floating indicator pill sliding smoothly between items | Navigation links, category tabs, and monthly/annual pricing toggles |
| **`SlidingNumber`** | Smooth rolling odometer number transitions | KPI statistics, live telemetry, and pricing counters |
| **`ProgressiveBlur`** | Multi-stop gradient blur | Frosted glass headers and bottom viewport fade overlays |

---

## 3. Production Component Recipes

### 3.1 `TextShimmer` (`src/components/core/text-shimmer.tsx`)
Subtle specular illumination on text without ugly multi-color gradients:

```tsx
"use client";

import React, { useMemo } from "react";
import { motion } from "motion/react";
import { cn } from "@/lib/utils";

export type TextShimmerProps = {
  children: string;
  as?: React.ElementType;
  className?: string;
  duration?: number;
  spread?: number;
};

export function TextShimmer({
  children,
  as: Component = "p",
  className,
  duration = 2.5,
  spread = 2,
}: TextShimmerProps) {
  const MotionComponent = motion.create(Component);

  const dynamicSpread = useMemo(() => {
    return children.length * spread;
  }, [children, spread]);

  return (
    <MotionComponent
      className={cn(
        "relative inline-block bg-[length:250%_100%,auto] bg-clip-text text-transparent",
        "[--base-color:#71717a] [--base-gradient-color:#09090b]",
        "dark:[--base-color:#a1a1aa] dark:[--base-gradient-color:#ffffff]",
        "[background-repeat:no-repeat,padding-box]",
        "[--bg:linear-gradient(90deg,#0000_calc(50%-var(--spread)),var(--base-gradient-color),#0000_calc(50%+var(--spread)))]",
        className
      )}
      initial={{ backgroundPosition: "100% center" }}
      animate={{ backgroundPosition: "0% center" }}
      transition={{
        repeat: Infinity,
        duration,
        ease: "linear",
      }}
      style={{
        "--spread": `${dynamicSpread}px`,
        backgroundImage: "var(--bg), linear-gradient(var(--base-color), var(--base-color))",
      } as React.CSSProperties}
    >
      {children}
    </MotionComponent>
  );
}
```

### 3.2 `InfiniteSlider` (`src/components/core/infinite-slider.tsx`)
Continuous seamless logo loop for client validation strips:

```tsx
"use client";

import React, { useEffect, useState } from "react";
import { useMotionValue, animate, motion } from "motion/react";
import useMeasure from "react-use-measure";
import { cn } from "@/lib/utils";

export interface InfiniteSliderProps {
  children: React.ReactNode;
  gap?: number;
  speed?: number;
  direction?: "horizontal" | "vertical";
  reverse?: boolean;
  className?: string;
}

export function InfiniteSlider({
  children,
  gap = 32,
  speed = 40,
  direction = "horizontal",
  reverse = false,
  className,
}: InfiniteSliderProps) {
  const [ref, { width, height }] = useMeasure();
  const translation = useMotionValue(0);

  useEffect(() => {
    const size = direction === "horizontal" ? width : height;
    if (size === 0) return;
    const contentSize = size + gap;
    const from = reverse ? -contentSize / 2 : 0;
    const to = reverse ? 0 : -contentSize / 2;
    const duration = Math.abs(to - from) / speed;

    const controls = animate(translation, [from, to], {
      ease: "linear",
      duration,
      repeat: Infinity,
      repeatType: "loop",
      repeatDelay: 0,
      onRepeat: () => translation.set(from),
    });

    return () => controls.stop();
  }, [translation, width, height, gap, speed, direction, reverse]);

  return (
    <div className={cn("overflow-hidden w-full", className)}>
      <motion.div
        className="flex w-max"
        style={{
          ...(direction === "horizontal" ? { x: translation } : { y: translation }),
          gap: `${gap}px`,
        }}
        ref={ref}
      >
        {children}
        {children}
      </motion.div>
    </div>
  );
}
```

### 3.3 `Magnetic` (`src/components/core/magnetic.tsx`)
Physical cursor attraction for buttons and interactive controls:

```tsx
"use client";

import React, { useRef, useState } from "react";
import { motion } from "motion/react";

interface MagneticProps {
  children: React.ReactElement;
  intensity?: number;
  springOptions?: { bounce?: number; damping?: number; stiffness?: number };
}

export function Magnetic({
  children,
  intensity = 0.35,
  springOptions = { bounce: 0.1, damping: 15, stiffness: 150 },
}: MagneticProps) {
  const ref = useRef<HTMLDivElement>(null);
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!ref.current) return;
    const { left, top, width, height } = ref.current.getBoundingClientRect();
    const centerX = left + width / 2;
    const centerY = top + height / 2;
    setPosition({
      x: (e.clientX - centerX) * intensity,
      y: (e.clientY - centerY) * intensity,
    });
  };

  const handleMouseLeave = () => {
    setPosition({ x: 0, y: 0 });
  };

  return (
    <motion.div
      ref={ref}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      animate={{ x: position.x, y: position.y }}
      transition={{ type: "spring", ...springOptions }}
      className="inline-block"
    >
      {children}
    </motion.div>
  );
}
```

### 3.4 `Spotlight` (`src/components/core/spotlight.tsx`)
Cursor-following ambient highlight for Bento cards:

```tsx
"use client";

import React, { useRef, useState } from "react";
import { motion, useSpring } from "motion/react";
import { cn } from "@/lib/utils";

interface SpotlightProps {
  children: React.ReactNode;
  className?: string;
  size?: number;
  color?: string;
}

export function Spotlight({
  children,
  className,
  size = 350,
  color = "rgba(255, 255, 255, 0.06)",
}: SpotlightProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [isHovered, setIsHovered] = useState(false);

  const mouseX = useSpring(0, { stiffness: 300, damping: 30 });
  const mouseY = useSpring(0, { stiffness: 300, damping: 30 });

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!containerRef.current) return;
    const rect = containerRef.current.getBoundingClientRect();
    mouseX.set(e.clientX - rect.left);
    mouseY.set(e.clientY - rect.top);
  };

  return (
    <div
      ref={containerRef}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className={cn("relative overflow-hidden rounded-3xl", className)}
    >
      <motion.div
        className="pointer-events-none absolute -inset-px transition-opacity duration-300"
        style={{
          opacity: isHovered ? 1 : 0,
          background: `radial-gradient(${size}px circle at ${mouseX}px ${mouseY}px, ${color}, transparent 80%)`,
        }}
      />
      {children}
    </div>
  );
}
```

---

## 4. Performance & Core Web Vitals Guardrails

When deploying `motion-primitives`:
1. **Isolate Client Boundaries**: Never make full pages or layouts `'use client'`. Keep `page.tsx` as a Server Component and import motion-primitives inside isolated interactive client leaves (`HeroInteractive`, `LogoTicker`, `BentoSpotlightCard`).
2. **GPU Acceleration**: Primitives animate hardware-accelerated properties (`transform`, `opacity`, `filter`). Never animate `width`, `height`, or `top` directly.
3. **Reduced Motion Safety**: All components must gracefully fallback to static states when the user has enabled OS-level `prefers-reduced-motion`.
