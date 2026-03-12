# SaaS & Fintech Design Token Presets

Complete, production-ready CSS custom property token systems for SaaS and fintech products. Each preset is a deployable `:root {}` block following the 3-tier token architecture (primitive, semantic, component) with oklch color space for perceptual uniformity.

---

## 1. Linear-Style (Minimal SaaS)

Precision tool aesthetic. Monochromatic neutrals with a single violet accent. Cool, disciplined, keyboard-first. Inspired by Linear, Raycast, Arc.

```css
:root {
  /* ================================================================
     LINEAR-STYLE PRESET — Minimal SaaS
     Cool monochromatic + violet accent
     ================================================================ */

  /* --- Primitive: Gray Scale (Cool, hue 280) --- */
  --color-gray-50:  oklch(0.98 0.005 280);
  --color-gray-100: oklch(0.95 0.005 280);
  --color-gray-200: oklch(0.90 0.008 280);
  --color-gray-300: oklch(0.82 0.010 280);
  --color-gray-400: oklch(0.70 0.012 280);
  --color-gray-500: oklch(0.55 0.015 280);
  --color-gray-600: oklch(0.45 0.015 280);
  --color-gray-700: oklch(0.35 0.012 280);
  --color-gray-800: oklch(0.25 0.010 280);
  --color-gray-900: oklch(0.18 0.008 280);
  --color-gray-950: oklch(0.12 0.008 280);

  /* --- Primitive: Violet Scale --- */
  --color-violet-50:  oklch(0.97 0.02 290);
  --color-violet-100: oklch(0.93 0.04 290);
  --color-violet-200: oklch(0.87 0.08 290);
  --color-violet-300: oklch(0.78 0.13 290);
  --color-violet-400: oklch(0.67 0.17 290);
  --color-violet-500: oklch(0.55 0.20 290);
  --color-violet-600: oklch(0.48 0.20 290);
  --color-violet-700: oklch(0.40 0.18 290);
  --color-violet-800: oklch(0.33 0.15 290);
  --color-violet-900: oklch(0.25 0.12 290);
  --color-violet-950: oklch(0.18 0.10 290);

  /* --- Primitive: Status Colors --- */
  --color-green-500:  oklch(0.60 0.17 145);
  --color-red-500:    oklch(0.55 0.20 25);
  --color-amber-500:  oklch(0.75 0.15 75);
  --color-blue-500:   oklch(0.55 0.18 250);

  /* --- Semantic: Light Mode --- */
  --color-bg:             var(--color-gray-50);
  --color-bg-subtle:      oklch(0.96 0.003 280);
  --color-surface:        white;
  --color-surface-raised: white;
  --color-surface-overlay: white;
  --color-text-primary:   var(--color-gray-900);
  --color-text-secondary: var(--color-gray-500);
  --color-text-tertiary:  var(--color-gray-400);
  --color-text-inverse:   white;
  --color-primary:        var(--color-violet-500);
  --color-primary-hover:  var(--color-violet-600);
  --color-primary-subtle: var(--color-violet-100);
  --color-border:         var(--color-gray-200);
  --color-border-subtle:  var(--color-gray-100);
  --color-success:        var(--color-green-500);
  --color-error:          var(--color-red-500);
  --color-warning:        var(--color-amber-500);
  --color-info:           var(--color-blue-500);

  /* --- Semantic: Dark Mode (override via .dark or [data-theme="dark"]) --- */
  --color-bg-dark:             var(--color-gray-950);
  --color-bg-subtle-dark:      oklch(0.14 0.008 280);
  --color-surface-dark:        var(--color-gray-900);
  --color-surface-raised-dark: var(--color-gray-800);
  --color-text-primary-dark:   var(--color-gray-50);
  --color-text-secondary-dark: var(--color-gray-400);
  --color-border-dark:         var(--color-gray-700);

  /* --- Typography --- */
  --font-sans:  'Inter', 'SF Pro', system-ui, -apple-system, sans-serif;
  --font-mono:  'JetBrains Mono', 'SF Mono', 'Fira Code', monospace;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --text-xs:    0.75rem;    /* 12px */
  --text-sm:    0.8125rem;  /* 13px */
  --text-base:  0.875rem;   /* 14px — compact default */
  --text-lg:    1rem;       /* 16px */
  --text-xl:    1.125rem;   /* 18px */
  --text-2xl:   1.25rem;    /* 20px */
  --text-3xl:   1.5rem;     /* 24px */
  --text-4xl:   2rem;       /* 32px */
  --text-5xl:   2.5rem;     /* 40px */
  --leading-tight:  1.2;
  --leading-snug:   1.35;
  --leading-normal: 1.5;
  --leading-relaxed: 1.65;
  --tracking-tight:  -0.02em;
  --tracking-normal: 0;
  --tracking-wide:   0.025em;

  /* --- Spacing (base-4) --- */
  --space-0:  0;
  --space-px: 1px;
  --space-0-5: 2px;
  --space-1:  4px;
  --space-1-5: 6px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  20px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   4px;
  --radius-md:   6px;
  --radius-lg:   8px;
  --radius-xl:   12px;
  --radius-2xl:  16px;
  --radius-full: 9999px;

  /* --- Shadows --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.04);
  --shadow-sm:  0 1px 3px oklch(0 0 0 / 0.06), 0 1px 2px oklch(0 0 0 / 0.04);
  --shadow-md:  0 4px 6px oklch(0 0 0 / 0.07), 0 2px 4px oklch(0 0 0 / 0.04);
  --shadow-lg:  0 10px 15px oklch(0 0 0 / 0.08), 0 4px 6px oklch(0 0 0 / 0.04);
  --shadow-xl:  0 20px 25px oklch(0 0 0 / 0.10), 0 8px 10px oklch(0 0 0 / 0.04);
  --shadow-2xl: 0 25px 50px oklch(0 0 0 / 0.15);
  --shadow-inner: inset 0 2px 4px oklch(0 0 0 / 0.05);

  /* --- Motion --- */
  --duration-instant: 50ms;
  --duration-fast:    100ms;
  --duration-normal:  150ms;
  --duration-moderate: 250ms;
  --duration-slow:    400ms;
  --duration-slower:  600ms;
  --ease-out:     cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in:      cubic-bezier(0.55, 0.055, 0.675, 0.19);
  --ease-in-out:  cubic-bezier(0.87, 0, 0.13, 1);
  --ease-spring:  cubic-bezier(0.34, 1.56, 0.64, 1);

  /* --- Breakpoints --- */
  --bp-xs:  480px;
  --bp-sm:  640px;
  --bp-md:  768px;
  --bp-lg:  1024px;
  --bp-xl:  1280px;
  --bp-2xl: 1536px;

  /* --- Z-Index --- */
  --z-base:     0;
  --z-raised:   1;
  --z-dropdown: 10;
  --z-sticky:   20;
  --z-overlay:  30;
  --z-modal:    40;
  --z-popover:  50;
  --z-toast:    60;
  --z-max:      9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.4;
  --opacity-muted:    0.6;
  --opacity-subtle:   0.8;
  --opacity-full:     1;
}
```

---

## 2. Stripe-Style (Developer SaaS)

Premium developer-facing aesthetic. Blue-to-purple gradient accents, generous whitespace, high-trust polish. Inspired by Stripe, Vercel, Clerk.

```css
:root {
  /* ================================================================
     STRIPE-STYLE PRESET — Developer SaaS
     Blue-purple gradient, premium polish, high-trust
     ================================================================ */

  /* --- Primitive: Gray Scale (Neutral-cool, hue 260) --- */
  --color-gray-50:  oklch(0.98 0.004 260);
  --color-gray-100: oklch(0.95 0.005 260);
  --color-gray-200: oklch(0.91 0.007 260);
  --color-gray-300: oklch(0.83 0.009 260);
  --color-gray-400: oklch(0.71 0.011 260);
  --color-gray-500: oklch(0.56 0.013 260);
  --color-gray-600: oklch(0.46 0.013 260);
  --color-gray-700: oklch(0.36 0.011 260);
  --color-gray-800: oklch(0.26 0.009 260);
  --color-gray-900: oklch(0.19 0.007 260);
  --color-gray-950: oklch(0.13 0.007 260);

  /* --- Primitive: Indigo Scale --- */
  --color-indigo-50:  oklch(0.97 0.02 265);
  --color-indigo-100: oklch(0.93 0.05 265);
  --color-indigo-200: oklch(0.86 0.10 265);
  --color-indigo-300: oklch(0.76 0.15 265);
  --color-indigo-400: oklch(0.65 0.19 265);
  --color-indigo-500: oklch(0.53 0.22 265);
  --color-indigo-600: oklch(0.46 0.22 265);
  --color-indigo-700: oklch(0.38 0.19 265);
  --color-indigo-800: oklch(0.31 0.16 265);
  --color-indigo-900: oklch(0.24 0.12 265);
  --color-indigo-950: oklch(0.17 0.10 265);

  /* --- Primitive: Cyan Scale (secondary) --- */
  --color-cyan-50:  oklch(0.97 0.02 200);
  --color-cyan-100: oklch(0.93 0.05 200);
  --color-cyan-200: oklch(0.86 0.09 200);
  --color-cyan-300: oklch(0.76 0.13 200);
  --color-cyan-400: oklch(0.65 0.15 200);
  --color-cyan-500: oklch(0.55 0.15 200);

  /* --- Primitive: Gradient Tokens --- */
  --gradient-brand:   linear-gradient(135deg, oklch(0.55 0.20 250), oklch(0.50 0.22 290));
  --gradient-surface: linear-gradient(180deg, oklch(0.98 0.004 260), oklch(0.96 0.006 260));
  --gradient-cta:     linear-gradient(135deg, oklch(0.53 0.22 265), oklch(0.48 0.20 290));
  --gradient-mesh:    radial-gradient(ellipse at 20% 80%, oklch(0.93 0.05 265) 0%, transparent 50%),
                      radial-gradient(ellipse at 80% 20%, oklch(0.93 0.04 200) 0%, transparent 50%);

  /* --- Primitive: Status Colors --- */
  --color-green-500:  oklch(0.62 0.17 150);
  --color-red-500:    oklch(0.55 0.22 25);
  --color-amber-500:  oklch(0.78 0.16 75);
  --color-blue-500:   oklch(0.56 0.18 250);

  /* --- Semantic: Light Mode --- */
  --color-bg:             oklch(0.99 0.002 260);
  --color-bg-subtle:      var(--color-gray-50);
  --color-surface:        white;
  --color-surface-raised: white;
  --color-surface-overlay: white;
  --color-text-primary:   var(--color-gray-900);
  --color-text-secondary: var(--color-gray-600);
  --color-text-tertiary:  var(--color-gray-400);
  --color-text-inverse:   white;
  --color-primary:        var(--color-indigo-500);
  --color-primary-hover:  var(--color-indigo-600);
  --color-primary-subtle: var(--color-indigo-50);
  --color-secondary:      var(--color-cyan-500);
  --color-border:         var(--color-gray-200);
  --color-border-subtle:  var(--color-gray-100);
  --color-focus-ring:     oklch(0.53 0.22 265 / 0.4);
  --color-success:        var(--color-green-500);
  --color-error:          var(--color-red-500);
  --color-warning:        var(--color-amber-500);
  --color-info:           var(--color-blue-500);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             oklch(0.10 0.008 260);
  --color-bg-subtle-dark:      oklch(0.13 0.008 260);
  --color-surface-dark:        oklch(0.16 0.009 260);
  --color-surface-raised-dark: oklch(0.19 0.009 260);
  --color-text-primary-dark:   oklch(0.95 0.005 260);
  --color-text-secondary-dark: oklch(0.70 0.010 260);
  --color-border-dark:         oklch(0.25 0.010 260);

  /* --- Typography --- */
  --font-sans:   'Inter', 'SF Pro Display', system-ui, sans-serif;
  --font-mono:   'SF Mono', 'JetBrains Mono', 'Fira Code', monospace;
  --font-display: 'Inter', 'SF Pro Display', system-ui, sans-serif;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --font-weight-extrabold: 800;
  --text-xs:    0.75rem;
  --text-sm:    0.875rem;
  --text-base:  1rem;
  --text-lg:    1.125rem;
  --text-xl:    1.25rem;
  --text-2xl:   1.5rem;
  --text-3xl:   1.875rem;
  --text-4xl:   2.25rem;
  --text-5xl:   3rem;
  --text-6xl:   3.75rem;
  --leading-tight:   1.15;
  --leading-snug:    1.3;
  --leading-normal:  1.5;
  --leading-relaxed: 1.625;
  --tracking-tighter: -0.03em;
  --tracking-tight:   -0.015em;
  --tracking-normal:  0;
  --tracking-wide:    0.025em;

  /* --- Spacing (base-4) --- */
  --space-0:  0;
  --space-px: 1px;
  --space-0-5: 2px;
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  20px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
  --space-32: 128px;

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-2xl:  24px;
  --radius-full: 9999px;

  /* --- Shadows --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.05);
  --shadow-sm:  0 2px 4px oklch(0 0 0 / 0.06), 0 1px 2px oklch(0 0 0 / 0.04);
  --shadow-md:  0 4px 8px oklch(0 0 0 / 0.08), 0 2px 4px oklch(0 0 0 / 0.04);
  --shadow-lg:  0 12px 24px oklch(0 0 0 / 0.10), 0 4px 8px oklch(0 0 0 / 0.04);
  --shadow-xl:  0 24px 48px oklch(0 0 0 / 0.12), 0 8px 16px oklch(0 0 0 / 0.04);
  --shadow-2xl: 0 32px 64px oklch(0 0 0 / 0.16);
  --shadow-glow: 0 0 20px oklch(0.53 0.22 265 / 0.15);

  /* --- Motion --- */
  --duration-instant:  50ms;
  --duration-fast:     100ms;
  --duration-normal:   200ms;
  --duration-moderate: 300ms;
  --duration-slow:     500ms;
  --ease-out:    cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in:     cubic-bezier(0.55, 0.055, 0.675, 0.19);
  --ease-in-out: cubic-bezier(0.87, 0, 0.13, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);

  /* --- Breakpoints --- */
  --bp-sm:  640px;
  --bp-md:  768px;
  --bp-lg:  1024px;
  --bp-xl:  1280px;
  --bp-2xl: 1536px;

  /* --- Z-Index --- */
  --z-base:     0;
  --z-raised:   1;
  --z-dropdown: 10;
  --z-sticky:   20;
  --z-overlay:  30;
  --z-modal:    40;
  --z-popover:  50;
  --z-toast:    60;
  --z-max:      9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.38;
  --opacity-muted:    0.6;
  --opacity-subtle:   0.8;
  --opacity-full:     1;
}
```

---

## 3. Notion-Style (Productivity SaaS)

Warm, readable, content-first. Muted accents let the user's content be the hero. Inspired by Notion, Craft, Coda.

```css
:root {
  /* ================================================================
     NOTION-STYLE PRESET — Productivity SaaS
     Warm neutrals, muted accents, content-first
     ================================================================ */

  /* --- Primitive: Warm Gray Scale (hue 55) --- */
  --color-gray-50:  oklch(0.98 0.008 55);
  --color-gray-100: oklch(0.95 0.008 55);
  --color-gray-200: oklch(0.91 0.010 55);
  --color-gray-300: oklch(0.84 0.010 55);
  --color-gray-400: oklch(0.72 0.010 55);
  --color-gray-500: oklch(0.57 0.010 55);
  --color-gray-600: oklch(0.47 0.010 55);
  --color-gray-700: oklch(0.37 0.008 55);
  --color-gray-800: oklch(0.27 0.008 55);
  --color-gray-900: oklch(0.20 0.006 55);
  --color-gray-950: oklch(0.14 0.006 55);

  /* --- Primitive: Muted Accent Colors --- */
  --color-brown-100: oklch(0.92 0.02 60);
  --color-brown-500: oklch(0.52 0.06 55);
  --color-orange-100: oklch(0.93 0.03 65);
  --color-orange-500: oklch(0.65 0.14 55);
  --color-yellow-100: oklch(0.95 0.04 95);
  --color-yellow-500: oklch(0.80 0.15 90);
  --color-green-100: oklch(0.94 0.03 155);
  --color-green-500: oklch(0.60 0.12 155);
  --color-blue-100: oklch(0.94 0.03 245);
  --color-blue-500: oklch(0.57 0.12 245);
  --color-purple-100: oklch(0.93 0.03 295);
  --color-purple-500: oklch(0.55 0.12 295);
  --color-pink-100: oklch(0.94 0.03 350);
  --color-pink-500: oklch(0.60 0.12 350);
  --color-red-100: oklch(0.93 0.03 25);
  --color-red-500: oklch(0.58 0.15 25);

  /* --- Semantic: Light Mode --- */
  --color-bg:             oklch(0.99 0.006 55);
  --color-bg-subtle:      var(--color-gray-50);
  --color-surface:        white;
  --color-surface-raised: white;
  --color-surface-hover:  var(--color-gray-50);
  --color-text-primary:   var(--color-gray-900);
  --color-text-secondary: var(--color-gray-500);
  --color-text-tertiary:  var(--color-gray-400);
  --color-text-inverse:   white;
  --color-primary:        var(--color-blue-500);
  --color-primary-hover:  oklch(0.50 0.14 245);
  --color-primary-subtle: var(--color-blue-100);
  --color-border:         var(--color-gray-200);
  --color-border-subtle:  var(--color-gray-100);
  --color-selection:      oklch(0.85 0.06 245 / 0.3);
  --color-highlight:      var(--color-yellow-100);
  --color-success:        var(--color-green-500);
  --color-error:          var(--color-red-500);
  --color-warning:        var(--color-orange-500);
  --color-info:           var(--color-blue-500);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             oklch(0.13 0.006 55);
  --color-bg-subtle-dark:      oklch(0.16 0.006 55);
  --color-surface-dark:        oklch(0.18 0.006 55);
  --color-surface-raised-dark: oklch(0.22 0.006 55);
  --color-text-primary-dark:   oklch(0.93 0.008 55);
  --color-text-secondary-dark: oklch(0.65 0.008 55);
  --color-border-dark:         oklch(0.28 0.006 55);

  /* --- Typography --- */
  --font-sans:  'Inter', 'SF Pro Text', system-ui, sans-serif;
  --font-serif: 'Georgia', 'Times New Roman', serif;
  --font-mono:  'SFMono-Regular', 'Menlo', 'Consolas', monospace;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --text-xs:    0.75rem;
  --text-sm:    0.875rem;
  --text-base:  1rem;       /* 16px — readability default */
  --text-lg:    1.125rem;
  --text-xl:    1.25rem;
  --text-2xl:   1.5rem;
  --text-3xl:   1.875rem;
  --text-4xl:   2.25rem;
  --text-5xl:   3rem;
  --leading-tight:   1.25;
  --leading-snug:    1.4;
  --leading-normal:  1.6;
  --leading-relaxed: 1.75;
  --tracking-tight:  -0.01em;
  --tracking-normal: 0;
  --tracking-wide:   0.02em;

  /* --- Spacing (base-4) --- */
  --space-0:  0;
  --space-px: 1px;
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  20px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   3px;
  --radius-md:   6px;
  --radius-lg:   8px;
  --radius-xl:   12px;
  --radius-full: 9999px;

  /* --- Shadows --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.04);
  --shadow-sm:  0 1px 3px oklch(0 0 0 / 0.05);
  --shadow-md:  0 3px 8px oklch(0 0 0 / 0.08);
  --shadow-lg:  0 8px 16px oklch(0 0 0 / 0.10);
  --shadow-xl:  0 16px 32px oklch(0 0 0 / 0.12);
  --shadow-inner: inset 0 1px 3px oklch(0 0 0 / 0.06);

  /* --- Motion --- */
  --duration-instant: 50ms;
  --duration-fast:    100ms;
  --duration-normal:  200ms;
  --duration-slow:    350ms;
  --ease-out:    cubic-bezier(0.25, 1, 0.5, 1);
  --ease-in:     cubic-bezier(0.5, 0, 0.75, 0);
  --ease-in-out: cubic-bezier(0.45, 0, 0.55, 1);

  /* --- Breakpoints --- */
  --bp-sm:  640px;
  --bp-md:  768px;
  --bp-lg:  1024px;
  --bp-xl:  1280px;
  --bp-2xl: 1440px;

  /* --- Z-Index --- */
  --z-base:     0;
  --z-raised:   1;
  --z-dropdown: 10;
  --z-sticky:   20;
  --z-overlay:  30;
  --z-modal:    40;
  --z-popover:  50;
  --z-toast:    60;
  --z-max:      9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.4;
  --opacity-muted:    0.6;
  --opacity-subtle:   0.8;
  --opacity-full:     1;
}
```

---

## 4. Banking / Fintech (Trust-Focused)

Conservative, high-trust, institution-grade. Navy palette with serif/sans pairing. Formal spacing, restrained color. Inspired by Mercury, Brex, Wise.

```css
:root {
  /* ================================================================
     BANKING / FINTECH PRESET — Trust-Focused
     Navy palette, serif+sans pairing, conservative, formal
     ================================================================ */

  /* --- Primitive: Navy Gray Scale (hue 230) --- */
  --color-gray-50:  oklch(0.98 0.006 230);
  --color-gray-100: oklch(0.96 0.007 230);
  --color-gray-200: oklch(0.92 0.009 230);
  --color-gray-300: oklch(0.85 0.010 230);
  --color-gray-400: oklch(0.73 0.011 230);
  --color-gray-500: oklch(0.58 0.012 230);
  --color-gray-600: oklch(0.48 0.012 230);
  --color-gray-700: oklch(0.38 0.010 230);
  --color-gray-800: oklch(0.28 0.010 230);
  --color-gray-900: oklch(0.20 0.010 230);
  --color-gray-950: oklch(0.14 0.010 230);

  /* --- Primitive: Navy Brand Scale --- */
  --color-navy-50:  oklch(0.96 0.02 240);
  --color-navy-100: oklch(0.92 0.04 240);
  --color-navy-200: oklch(0.85 0.07 240);
  --color-navy-300: oklch(0.74 0.11 240);
  --color-navy-400: oklch(0.62 0.14 240);
  --color-navy-500: oklch(0.50 0.14 240);
  --color-navy-600: oklch(0.42 0.13 240);
  --color-navy-700: oklch(0.34 0.12 240);
  --color-navy-800: oklch(0.26 0.10 240);
  --color-navy-900: oklch(0.18 0.08 240);
  --color-navy-950: oklch(0.12 0.07 240);

  /* --- Primitive: Teal Accent (secondary) --- */
  --color-teal-50:  oklch(0.96 0.02 180);
  --color-teal-100: oklch(0.92 0.04 180);
  --color-teal-500: oklch(0.55 0.12 180);
  --color-teal-600: oklch(0.48 0.12 180);

  /* --- Primitive: Status Colors --- */
  --color-green-500:  oklch(0.58 0.14 150);
  --color-red-500:    oklch(0.52 0.18 25);
  --color-amber-500:  oklch(0.75 0.14 75);
  --color-blue-500:   oklch(0.54 0.14 245);

  /* --- Semantic: Light Mode --- */
  --color-bg:             white;
  --color-bg-subtle:      var(--color-gray-50);
  --color-surface:        white;
  --color-surface-raised: white;
  --color-surface-overlay: white;
  --color-surface-muted:  var(--color-gray-100);
  --color-text-primary:   var(--color-navy-950);
  --color-text-secondary: var(--color-gray-600);
  --color-text-tertiary:  var(--color-gray-400);
  --color-text-inverse:   white;
  --color-primary:        var(--color-navy-700);
  --color-primary-hover:  var(--color-navy-800);
  --color-primary-subtle: var(--color-navy-50);
  --color-secondary:      var(--color-teal-500);
  --color-secondary-hover: var(--color-teal-600);
  --color-border:         var(--color-gray-200);
  --color-border-subtle:  var(--color-gray-100);
  --color-border-strong:  var(--color-gray-300);
  --color-focus-ring:     oklch(0.50 0.14 240 / 0.3);
  --color-success:        var(--color-green-500);
  --color-error:          var(--color-red-500);
  --color-warning:        var(--color-amber-500);
  --color-info:           var(--color-blue-500);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             oklch(0.11 0.010 230);
  --color-bg-subtle-dark:      oklch(0.14 0.010 230);
  --color-surface-dark:        oklch(0.17 0.010 230);
  --color-surface-raised-dark: oklch(0.20 0.010 230);
  --color-text-primary-dark:   oklch(0.95 0.006 230);
  --color-text-secondary-dark: oklch(0.68 0.008 230);
  --color-border-dark:         oklch(0.26 0.010 230);

  /* --- Typography --- */
  --font-display: 'Fraunces', 'Playfair Display', 'Georgia', serif;
  --font-sans:    'Inter', 'SF Pro', system-ui, sans-serif;
  --font-mono:    'SF Mono', 'JetBrains Mono', monospace;
  --font-numbers: 'Inter', 'Tabular Nums', system-ui, sans-serif;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --text-xs:    0.75rem;
  --text-sm:    0.875rem;
  --text-base:  1rem;
  --text-lg:    1.125rem;
  --text-xl:    1.25rem;
  --text-2xl:   1.5rem;
  --text-3xl:   2rem;
  --text-4xl:   2.5rem;
  --text-5xl:   3rem;
  --text-6xl:   3.75rem;
  --leading-tight:   1.2;
  --leading-snug:    1.35;
  --leading-normal:  1.55;
  --leading-relaxed: 1.7;
  --tracking-tight:  -0.02em;
  --tracking-normal: 0;
  --tracking-wide:   0.04em;
  --tracking-caps:   0.08em;

  /* --- Spacing (base-4, generous) --- */
  --space-0:  0;
  --space-px: 1px;
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  20px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
  --space-32: 128px;
  --space-40: 160px;

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   4px;
  --radius-md:   6px;
  --radius-lg:   8px;
  --radius-xl:   12px;
  --radius-2xl:  16px;
  --radius-full: 9999px;

  /* --- Shadows (subtle, restrained) --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.03);
  --shadow-sm:  0 1px 3px oklch(0 0 0 / 0.04), 0 1px 2px oklch(0 0 0 / 0.03);
  --shadow-md:  0 4px 8px oklch(0 0 0 / 0.06), 0 2px 4px oklch(0 0 0 / 0.03);
  --shadow-lg:  0 8px 16px oklch(0 0 0 / 0.08), 0 4px 8px oklch(0 0 0 / 0.03);
  --shadow-xl:  0 16px 32px oklch(0 0 0 / 0.10);
  --shadow-card: 0 1px 3px oklch(0 0 0 / 0.04), 0 0 0 1px oklch(0 0 0 / 0.02);

  /* --- Motion (deliberate, professional) --- */
  --duration-instant:  50ms;
  --duration-fast:     120ms;
  --duration-normal:   200ms;
  --duration-moderate: 300ms;
  --duration-slow:     500ms;
  --ease-out:    cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in:     cubic-bezier(0.64, 0, 0.78, 0);
  --ease-in-out: cubic-bezier(0.45, 0, 0.55, 1);

  /* --- Breakpoints --- */
  --bp-sm:  640px;
  --bp-md:  768px;
  --bp-lg:  1024px;
  --bp-xl:  1280px;
  --bp-2xl: 1440px;

  /* --- Z-Index --- */
  --z-base:     0;
  --z-raised:   1;
  --z-dropdown: 10;
  --z-sticky:   20;
  --z-overlay:  30;
  --z-modal:    40;
  --z-popover:  50;
  --z-toast:    60;
  --z-max:      9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.4;
  --opacity-muted:    0.55;
  --opacity-subtle:   0.75;
  --opacity-full:     1;
}
```

---

## 5. Trading / Crypto (Data-Dense)

Dark-first, data-dense, action-oriented. Green/red for up/down. Monospace numbers. High information density. Inspired by Robinhood, Binance, Bloomberg Terminal.

```css
:root {
  /* ================================================================
     TRADING / CRYPTO PRESET — Data-Dense
     Dark-first, green/red up/down, monospace numbers
     ================================================================ */

  /* --- Primitive: Dark Gray Scale (pure neutral, hue 0) --- */
  --color-gray-50:  oklch(0.95 0.000 0);
  --color-gray-100: oklch(0.90 0.000 0);
  --color-gray-200: oklch(0.82 0.000 0);
  --color-gray-300: oklch(0.70 0.000 0);
  --color-gray-400: oklch(0.58 0.000 0);
  --color-gray-500: oklch(0.48 0.000 0);
  --color-gray-600: oklch(0.38 0.000 0);
  --color-gray-700: oklch(0.28 0.000 0);
  --color-gray-800: oklch(0.20 0.000 0);
  --color-gray-850: oklch(0.17 0.000 0);
  --color-gray-900: oklch(0.14 0.000 0);
  --color-gray-950: oklch(0.10 0.000 0);
  --color-black:    oklch(0.07 0.000 0);

  /* --- Primitive: Gain / Up (Green) --- */
  --color-gain-50:  oklch(0.95 0.03 150);
  --color-gain-100: oklch(0.90 0.06 150);
  --color-gain-200: oklch(0.82 0.10 150);
  --color-gain-300: oklch(0.72 0.14 150);
  --color-gain-400: oklch(0.65 0.18 150);
  --color-gain-500: oklch(0.60 0.20 150);
  --color-gain-600: oklch(0.52 0.18 150);
  --color-gain-700: oklch(0.44 0.15 150);

  /* --- Primitive: Loss / Down (Red) --- */
  --color-loss-50:  oklch(0.95 0.03 25);
  --color-loss-100: oklch(0.90 0.06 25);
  --color-loss-200: oklch(0.82 0.10 25);
  --color-loss-300: oklch(0.72 0.15 25);
  --color-loss-400: oklch(0.62 0.19 25);
  --color-loss-500: oklch(0.55 0.22 25);
  --color-loss-600: oklch(0.48 0.20 25);
  --color-loss-700: oklch(0.40 0.17 25);

  /* --- Primitive: Accent (Electric Blue) --- */
  --color-accent-50:  oklch(0.95 0.03 250);
  --color-accent-100: oklch(0.90 0.06 250);
  --color-accent-400: oklch(0.65 0.18 250);
  --color-accent-500: oklch(0.58 0.20 250);
  --color-accent-600: oklch(0.50 0.20 250);

  /* --- Primitive: Amber (Pending/Neutral) --- */
  --color-amber-400: oklch(0.78 0.15 80);
  --color-amber-500: oklch(0.72 0.15 80);

  /* --- Semantic: Dark Mode (default) --- */
  --color-bg:              var(--color-black);
  --color-bg-subtle:       var(--color-gray-950);
  --color-surface:         var(--color-gray-900);
  --color-surface-raised:  var(--color-gray-850);
  --color-surface-overlay: var(--color-gray-800);
  --color-surface-hover:   var(--color-gray-800);
  --color-text-primary:    var(--color-gray-50);
  --color-text-secondary:  var(--color-gray-400);
  --color-text-tertiary:   var(--color-gray-500);
  --color-text-muted:      var(--color-gray-600);
  --color-primary:         var(--color-accent-500);
  --color-primary-hover:   var(--color-accent-400);
  --color-primary-subtle:  oklch(0.58 0.20 250 / 0.12);
  --color-border:          var(--color-gray-800);
  --color-border-subtle:   var(--color-gray-850);
  --color-border-strong:   var(--color-gray-700);
  --color-up:              var(--color-gain-500);
  --color-up-bg:           oklch(0.60 0.20 150 / 0.10);
  --color-up-text:         var(--color-gain-400);
  --color-down:            var(--color-loss-500);
  --color-down-bg:         oklch(0.55 0.22 25 / 0.10);
  --color-down-text:       var(--color-loss-400);
  --color-neutral:         var(--color-amber-500);
  --color-success:         var(--color-gain-500);
  --color-error:           var(--color-loss-500);
  --color-warning:         var(--color-amber-500);
  --color-info:            var(--color-accent-500);

  /* --- Semantic: Light Mode (alt) --- */
  --color-bg-light:             white;
  --color-surface-light:        var(--color-gray-50);
  --color-text-primary-light:   var(--color-gray-900);
  --color-text-secondary-light: var(--color-gray-600);
  --color-border-light:         var(--color-gray-200);

  /* --- Typography --- */
  --font-sans:    'Inter', 'SF Pro', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'SF Mono', 'Fira Code', monospace;
  --font-numbers: 'JetBrains Mono', 'SF Mono', 'Tabular Nums', monospace;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --text-2xs:   0.625rem;   /* 10px — dense data */
  --text-xs:    0.75rem;    /* 12px */
  --text-sm:    0.8125rem;  /* 13px — default for data */
  --text-base:  0.875rem;   /* 14px */
  --text-lg:    1rem;       /* 16px */
  --text-xl:    1.125rem;   /* 18px */
  --text-2xl:   1.375rem;   /* 22px */
  --text-3xl:   1.75rem;    /* 28px */
  --text-4xl:   2.25rem;    /* 36px */
  --leading-tight:   1.15;
  --leading-snug:    1.3;
  --leading-normal:  1.45;
  --leading-relaxed: 1.6;
  --tracking-tight:  -0.02em;
  --tracking-normal: 0;
  --tracking-wide:   0.03em;
  --tracking-mono:   -0.03em;

  /* --- Spacing (base-4, compact) --- */
  --space-0:  0;
  --space-px: 1px;
  --space-0-5: 2px;
  --space-1:  4px;
  --space-1-5: 6px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-5:  20px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   2px;
  --radius-md:   4px;
  --radius-lg:   6px;
  --radius-xl:   8px;
  --radius-2xl:  12px;
  --radius-full: 9999px;

  /* --- Shadows (subtle for dark UI) --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.20);
  --shadow-sm:  0 2px 4px oklch(0 0 0 / 0.25);
  --shadow-md:  0 4px 8px oklch(0 0 0 / 0.30);
  --shadow-lg:  0 8px 16px oklch(0 0 0 / 0.35);
  --shadow-xl:  0 16px 32px oklch(0 0 0 / 0.40);
  --shadow-glow-gain: 0 0 12px oklch(0.60 0.20 150 / 0.20);
  --shadow-glow-loss: 0 0 12px oklch(0.55 0.22 25 / 0.20);

  /* --- Motion (fast, responsive) --- */
  --duration-instant:  30ms;
  --duration-fast:     80ms;
  --duration-normal:   120ms;
  --duration-moderate: 200ms;
  --duration-slow:     350ms;
  --ease-out:    cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in:     cubic-bezier(0.55, 0.055, 0.675, 0.19);
  --ease-in-out: cubic-bezier(0.87, 0, 0.13, 1);
  --ease-snap:   cubic-bezier(0.2, 0, 0, 1);

  /* --- Breakpoints --- */
  --bp-sm:  640px;
  --bp-md:  768px;
  --bp-lg:  1024px;
  --bp-xl:  1440px;
  --bp-2xl: 1920px;
  --bp-3xl: 2560px;

  /* --- Z-Index --- */
  --z-base:     0;
  --z-raised:   1;
  --z-chart:    5;
  --z-dropdown: 10;
  --z-sticky:   20;
  --z-overlay:  30;
  --z-modal:    40;
  --z-popover:  50;
  --z-toast:    60;
  --z-ticker:   70;
  --z-max:      9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.35;
  --opacity-muted:    0.5;
  --opacity-subtle:   0.7;
  --opacity-full:     1;

  /* --- Data Visualization --- */
  --chart-line-gain:   var(--color-gain-500);
  --chart-line-loss:   var(--color-loss-500);
  --chart-area-gain:   oklch(0.60 0.20 150 / 0.08);
  --chart-area-loss:   oklch(0.55 0.22 25 / 0.08);
  --chart-grid:        var(--color-gray-850);
  --chart-crosshair:   var(--color-gray-500);
  --chart-volume:      var(--color-gray-700);
  --chart-candle-up:   var(--color-gain-500);
  --chart-candle-down: var(--color-loss-500);
}
```

---

## Usage Notes

### Applying Dark Mode
Use a CSS class or `data-theme` attribute:
```css
[data-theme="dark"] {
  --color-bg: var(--color-bg-dark);
  --color-surface: var(--color-surface-dark);
  --color-text-primary: var(--color-text-primary-dark);
  /* ... map all dark tokens */
}
```

### Customizing a Preset
1. Copy the `:root {}` block into your project
2. Change primitive hue values to match your brand
3. Semantic tokens auto-update via `var()` references
4. Validate contrast with APCA calculator

### Font Loading
All presets use system font fallbacks. Load web fonts via:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Token Naming Convention
- `--color-{hue}-{step}` for primitives (gray-500, violet-300)
- `--color-{role}` for semantics (primary, border, bg)
- `--{category}-{variant}` for system tokens (shadow-md, radius-lg)
