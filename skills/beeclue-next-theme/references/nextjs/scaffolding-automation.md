# Automated Scaffolding & Empty Directory Detection

When a user invokes `beeclue-next-theme` in an empty or new project directory, the skill automatically detects the environment and scaffolds the latest version of Next.js 15+ without manual friction.

---

## 1. Pre-Flight Directory Detection Workflow

Before creating theme files, the agent executes this detection logic:

```bash
# 1. Check if directory is empty or missing package.json
if [ ! -f "package.json" ]; then
    echo "Empty directory detected. Initializing latest Next.js flagship..."
    
    # 2. Check latest Next.js version on npm registry
    npm view next version
    
    # 3. Scaffold Next.js latest with App Router, TypeScript, Tailwind CSS, Turbopack
    npx create-next-app@latest . \
      --typescript \
      --tailwind \
      --eslint \
      --app \
      --src-dir \
      --import-alias "@/*" \
      --use-npm \
      --turbopack \
      --yes
fi
```

---

## 2. Installing Core Utility Packages

Next, install essential utilities for Apple-grade micro-interactions, icons, and class management:

```bash
npm install lucide-react clsx tailwind-merge
```

*(Note: Never install heavy bloated UI libraries that introduce unnecessary runtime overhead. Keep packages clean, fast, and tree-shakeable).*

---

## 3. Configuring `next.config.ts` for Unsplash Images

Next.js requires external image hostnames to be configured under `images.remotePatterns`. The agent automatically writes or updates `next.config.ts`:

```typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    formats: ["image/avif", "image/webp"],
    remotePatterns: [
      {
        protocol: "https",
        hostname: "images.unsplash.com",
        port: "",
        pathname: "/**",
      },
    ],
  },
};

export default nextConfig;
```

---

## 4. Setting Up Class Utilities (`src/lib/utils.ts`)

```typescript
import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```
