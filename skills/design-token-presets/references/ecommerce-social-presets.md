# E-Commerce & Social Design Token Presets

Complete, production-ready CSS custom property token systems for e-commerce and social platforms. Each preset is a deployable `:root {}` block following the 3-tier token architecture with oklch color space.

---

## 1. Luxury E-Commerce (Farfetch / Net-a-Porter Style)

Editorial typography, restrained palette, generous whitespace. Every pixel communicates exclusivity. Inspired by Farfetch, Net-a-Porter, Mr Porter, Ssense.

```css
:root {
  /* ================================================================
     LUXURY E-COMMERCE PRESET
     Editorial type, restrained palette, generous whitespace
     ================================================================ */

  /* --- Primitive: Warm Neutral Scale (hue 45) --- */
  --color-neutral-50:  oklch(0.98 0.006 45);
  --color-neutral-100: oklch(0.96 0.007 45);
  --color-neutral-200: oklch(0.92 0.008 45);
  --color-neutral-300: oklch(0.86 0.008 45);
  --color-neutral-400: oklch(0.74 0.008 45);
  --color-neutral-500: oklch(0.58 0.008 45);
  --color-neutral-600: oklch(0.48 0.008 45);
  --color-neutral-700: oklch(0.38 0.006 45);
  --color-neutral-800: oklch(0.28 0.006 45);
  --color-neutral-900: oklch(0.18 0.004 45);
  --color-neutral-950: oklch(0.12 0.004 45);

  /* --- Primitive: Black & Cream --- */
  --color-black:  oklch(0.08 0.003 45);
  --color-cream:  oklch(0.97 0.010 70);
  --color-ivory:  oklch(0.98 0.008 80);
  --color-sand:   oklch(0.92 0.015 65);

  /* --- Primitive: Gold Accent --- */
  --color-gold-100: oklch(0.92 0.04 85);
  --color-gold-300: oklch(0.78 0.08 80);
  --color-gold-500: oklch(0.65 0.10 75);
  --color-gold-700: oklch(0.50 0.08 70);

  /* --- Primitive: Status (muted) --- */
  --color-green-500: oklch(0.55 0.10 155);
  --color-red-500:   oklch(0.50 0.12 20);
  --color-amber-500: oklch(0.70 0.10 75);

  /* --- Semantic: Light Mode --- */
  --color-bg:              var(--color-ivory);
  --color-bg-subtle:       var(--color-cream);
  --color-bg-editorial:    var(--color-sand);
  --color-surface:         white;
  --color-surface-raised:  white;
  --color-surface-overlay: white;
  --color-text-primary:    var(--color-black);
  --color-text-secondary:  var(--color-neutral-600);
  --color-text-tertiary:   var(--color-neutral-400);
  --color-text-inverse:    white;
  --color-primary:         var(--color-black);
  --color-primary-hover:   var(--color-neutral-800);
  --color-primary-subtle:  var(--color-neutral-100);
  --color-accent:          var(--color-gold-500);
  --color-accent-subtle:   var(--color-gold-100);
  --color-border:          var(--color-neutral-200);
  --color-border-subtle:   var(--color-neutral-100);
  --color-border-strong:   var(--color-neutral-400);
  --color-divider:         var(--color-neutral-200);
  --color-success:         var(--color-green-500);
  --color-error:           var(--color-red-500);
  --color-warning:         var(--color-amber-500);
  --color-sale:            var(--color-red-500);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             var(--color-black);
  --color-bg-subtle-dark:      var(--color-neutral-950);
  --color-surface-dark:        oklch(0.14 0.004 45);
  --color-surface-raised-dark: oklch(0.18 0.004 45);
  --color-text-primary-dark:   var(--color-ivory);
  --color-text-secondary-dark: var(--color-neutral-400);
  --color-border-dark:         var(--color-neutral-800);

  /* --- Typography --- */
  --font-display: 'Playfair Display', 'Didot', 'Bodoni MT', serif;
  --font-heading: 'Playfair Display', 'Georgia', serif;
  --font-sans:    'Inter', 'Helvetica Neue', 'Arial', sans-serif;
  --font-mono:    'SF Mono', monospace;
  --font-weight-light:    300;
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
  --text-5xl:   3.25rem;
  --text-6xl:   4rem;
  --text-7xl:   5rem;
  --leading-tight:   1.1;
  --leading-snug:    1.25;
  --leading-normal:  1.5;
  --leading-relaxed: 1.75;
  --leading-loose:   2;
  --tracking-tighter: -0.04em;
  --tracking-tight:   -0.02em;
  --tracking-normal:  0;
  --tracking-wide:    0.05em;
  --tracking-wider:   0.1em;
  --tracking-caps:    0.15em;

  /* --- Spacing (generous, base-4) --- */
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
  --space-48: 192px;

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   2px;
  --radius-md:   4px;
  --radius-lg:   6px;
  --radius-xl:   8px;
  --radius-full: 9999px;

  /* --- Shadows (delicate) --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.03);
  --shadow-sm:  0 2px 4px oklch(0 0 0 / 0.04);
  --shadow-md:  0 4px 12px oklch(0 0 0 / 0.06);
  --shadow-lg:  0 8px 24px oklch(0 0 0 / 0.08);
  --shadow-xl:  0 16px 48px oklch(0 0 0 / 0.10);
  --shadow-product: 0 4px 16px oklch(0 0 0 / 0.06);

  /* --- Motion (elegant, deliberate) --- */
  --duration-instant:  50ms;
  --duration-fast:     150ms;
  --duration-normal:   300ms;
  --duration-moderate: 500ms;
  --duration-slow:     700ms;
  --duration-slower:   1000ms;
  --ease-out:      cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in:       cubic-bezier(0.64, 0, 0.78, 0);
  --ease-in-out:   cubic-bezier(0.45, 0, 0.55, 1);
  --ease-elegant:  cubic-bezier(0.25, 0.46, 0.45, 0.94);

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
  --opacity-disabled: 0.4;
  --opacity-muted:    0.6;
  --opacity-subtle:   0.8;
  --opacity-full:     1;
}
```

---

## 2. Marketplace (Airbnb / Etsy Style)

Friendly, warm, accessible. High color contrast for trust. Rounded forms for approachability. Inspired by Airbnb, Etsy, Depop.

```css
:root {
  /* ================================================================
     MARKETPLACE PRESET — Friendly & Warm
     Warm palette, rounded, accessible, trust-building
     ================================================================ */

  /* --- Primitive: Warm Gray Scale (hue 35) --- */
  --color-gray-50:  oklch(0.98 0.007 35);
  --color-gray-100: oklch(0.96 0.008 35);
  --color-gray-200: oklch(0.92 0.009 35);
  --color-gray-300: oklch(0.85 0.009 35);
  --color-gray-400: oklch(0.72 0.009 35);
  --color-gray-500: oklch(0.57 0.009 35);
  --color-gray-600: oklch(0.47 0.008 35);
  --color-gray-700: oklch(0.37 0.007 35);
  --color-gray-800: oklch(0.27 0.006 35);
  --color-gray-900: oklch(0.19 0.005 35);
  --color-gray-950: oklch(0.13 0.005 35);

  /* --- Primitive: Coral Brand Scale --- */
  --color-coral-50:  oklch(0.96 0.02 20);
  --color-coral-100: oklch(0.92 0.05 20);
  --color-coral-200: oklch(0.85 0.09 20);
  --color-coral-300: oklch(0.76 0.14 20);
  --color-coral-400: oklch(0.67 0.18 18);
  --color-coral-500: oklch(0.60 0.20 15);
  --color-coral-600: oklch(0.52 0.20 15);
  --color-coral-700: oklch(0.44 0.17 15);
  --color-coral-800: oklch(0.36 0.14 15);
  --color-coral-900: oklch(0.28 0.10 15);

  /* --- Primitive: Teal Secondary --- */
  --color-teal-50:  oklch(0.96 0.02 180);
  --color-teal-100: oklch(0.92 0.04 180);
  --color-teal-500: oklch(0.55 0.12 175);
  --color-teal-600: oklch(0.48 0.12 175);

  /* --- Primitive: Warm Accents --- */
  --color-amber-100: oklch(0.93 0.04 80);
  --color-amber-500: oklch(0.75 0.14 80);
  --color-peach-100: oklch(0.94 0.03 50);
  --color-peach-500: oklch(0.72 0.10 50);

  /* --- Primitive: Status Colors --- */
  --color-green-500:  oklch(0.58 0.15 150);
  --color-red-500:    oklch(0.52 0.20 25);
  --color-yellow-500: oklch(0.82 0.14 90);
  --color-blue-500:   oklch(0.55 0.14 245);

  /* --- Semantic: Light Mode --- */
  --color-bg:             white;
  --color-bg-subtle:      var(--color-gray-50);
  --color-bg-warm:        oklch(0.98 0.012 35);
  --color-surface:        white;
  --color-surface-raised: white;
  --color-surface-overlay: white;
  --color-surface-hover:  var(--color-gray-50);
  --color-text-primary:   var(--color-gray-900);
  --color-text-secondary: var(--color-gray-600);
  --color-text-tertiary:  var(--color-gray-400);
  --color-text-inverse:   white;
  --color-primary:        var(--color-coral-500);
  --color-primary-hover:  var(--color-coral-600);
  --color-primary-subtle: var(--color-coral-50);
  --color-secondary:      var(--color-teal-500);
  --color-secondary-hover: var(--color-teal-600);
  --color-border:         var(--color-gray-200);
  --color-border-subtle:  var(--color-gray-100);
  --color-border-strong:  var(--color-gray-300);
  --color-focus-ring:     oklch(0.60 0.20 15 / 0.3);
  --color-success:        var(--color-green-500);
  --color-error:          var(--color-red-500);
  --color-warning:        var(--color-yellow-500);
  --color-info:           var(--color-blue-500);
  --color-star:           var(--color-amber-500);
  --color-superhost:      var(--color-coral-500);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             oklch(0.12 0.005 35);
  --color-bg-subtle-dark:      oklch(0.15 0.005 35);
  --color-surface-dark:        oklch(0.18 0.005 35);
  --color-surface-raised-dark: oklch(0.22 0.005 35);
  --color-text-primary-dark:   oklch(0.95 0.007 35);
  --color-text-secondary-dark: oklch(0.68 0.007 35);
  --color-border-dark:         oklch(0.27 0.005 35);

  /* --- Typography --- */
  --font-sans:    'Nunito Sans', 'Inter', system-ui, sans-serif;
  --font-display: 'Nunito Sans', 'Inter', system-ui, sans-serif;
  --font-mono:    'SF Mono', monospace;
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
  --leading-tight:   1.2;
  --leading-snug:    1.35;
  --leading-normal:  1.5;
  --leading-relaxed: 1.65;
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

  /* --- Border Radius (rounded, friendly) --- */
  --radius-none: 0;
  --radius-sm:   6px;
  --radius-md:   10px;
  --radius-lg:   14px;
  --radius-xl:   20px;
  --radius-2xl:  28px;
  --radius-full: 9999px;

  /* --- Shadows --- */
  --shadow-xs:   0 1px 2px oklch(0 0 0 / 0.04);
  --shadow-sm:   0 2px 4px oklch(0 0 0 / 0.06);
  --shadow-md:   0 4px 8px oklch(0 0 0 / 0.08);
  --shadow-lg:   0 8px 20px oklch(0 0 0 / 0.10);
  --shadow-xl:   0 16px 40px oklch(0 0 0 / 0.12);
  --shadow-card: 0 2px 8px oklch(0 0 0 / 0.06), 0 0 0 1px oklch(0 0 0 / 0.02);
  --shadow-card-hover: 0 4px 16px oklch(0 0 0 / 0.10);

  /* --- Motion --- */
  --duration-instant:  50ms;
  --duration-fast:     100ms;
  --duration-normal:   200ms;
  --duration-moderate: 300ms;
  --duration-slow:     500ms;
  --ease-out:    cubic-bezier(0.25, 1, 0.5, 1);
  --ease-in:     cubic-bezier(0.5, 0, 0.75, 0);
  --ease-in-out: cubic-bezier(0.45, 0, 0.55, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);

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
  --opacity-disabled: 0.4;
  --opacity-muted:    0.6;
  --opacity-subtle:   0.8;
  --opacity-full:     1;
}
```

---

## 3. Fashion / Streetwear (Bold & Editorial)

High contrast, bold typography, editorial layout energy. Oversized type, dramatic black/white with one accent. Inspired by Supreme, Off-White, Grailed, END.

```css
:root {
  /* ================================================================
     FASHION / STREETWEAR PRESET
     Bold, high contrast, editorial, statement typography
     ================================================================ */

  /* --- Primitive: Pure Scale (achromatic) --- */
  --color-white:      oklch(1.00 0 0);
  --color-gray-50:    oklch(0.97 0 0);
  --color-gray-100:   oklch(0.94 0 0);
  --color-gray-200:   oklch(0.88 0 0);
  --color-gray-300:   oklch(0.80 0 0);
  --color-gray-400:   oklch(0.68 0 0);
  --color-gray-500:   oklch(0.55 0 0);
  --color-gray-600:   oklch(0.42 0 0);
  --color-gray-700:   oklch(0.32 0 0);
  --color-gray-800:   oklch(0.22 0 0);
  --color-gray-900:   oklch(0.14 0 0);
  --color-gray-950:   oklch(0.08 0 0);
  --color-black:      oklch(0.00 0 0);

  /* --- Primitive: Accent (Electric Red) --- */
  --color-accent-50:  oklch(0.95 0.03 25);
  --color-accent-100: oklch(0.88 0.08 25);
  --color-accent-300: oklch(0.70 0.18 25);
  --color-accent-500: oklch(0.55 0.25 25);
  --color-accent-700: oklch(0.40 0.20 25);
  --color-accent-900: oklch(0.28 0.14 25);

  /* --- Primitive: Alt Accents --- */
  --color-neon-green:  oklch(0.85 0.25 140);
  --color-neon-yellow: oklch(0.90 0.20 100);
  --color-electric-blue: oklch(0.60 0.22 255);

  /* --- Primitive: Status --- */
  --color-green-500: oklch(0.58 0.15 150);
  --color-red-500:   oklch(0.55 0.25 25);
  --color-amber-500: oklch(0.78 0.15 80);

  /* --- Semantic: Light Mode (white-dominant) --- */
  --color-bg:             var(--color-white);
  --color-bg-subtle:      var(--color-gray-50);
  --color-bg-contrast:    var(--color-black);
  --color-surface:        var(--color-white);
  --color-surface-raised: var(--color-white);
  --color-surface-invert: var(--color-black);
  --color-text-primary:   var(--color-black);
  --color-text-secondary: var(--color-gray-600);
  --color-text-tertiary:  var(--color-gray-400);
  --color-text-inverse:   var(--color-white);
  --color-primary:        var(--color-black);
  --color-primary-hover:  var(--color-gray-800);
  --color-primary-subtle: var(--color-gray-100);
  --color-accent:         var(--color-accent-500);
  --color-accent-hover:   var(--color-accent-700);
  --color-border:         var(--color-black);
  --color-border-subtle:  var(--color-gray-200);
  --color-focus-ring:     var(--color-accent-500);
  --color-success:        var(--color-green-500);
  --color-error:          var(--color-red-500);
  --color-warning:        var(--color-amber-500);
  --color-sale:           var(--color-accent-500);
  --color-new:            var(--color-neon-green);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             var(--color-black);
  --color-bg-subtle-dark:      var(--color-gray-950);
  --color-surface-dark:        var(--color-gray-900);
  --color-surface-raised-dark: var(--color-gray-800);
  --color-text-primary-dark:   var(--color-white);
  --color-text-secondary-dark: var(--color-gray-400);
  --color-border-dark:         var(--color-gray-700);

  /* --- Typography (oversized, statement) --- */
  --font-display:  'Oswald', 'Bebas Neue', 'Impact', sans-serif;
  --font-heading:  'Oswald', 'Bebas Neue', sans-serif;
  --font-sans:     'Inter', 'Helvetica Neue', sans-serif;
  --font-mono:     'Space Mono', 'JetBrains Mono', monospace;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-bold:     700;
  --font-weight-black:    900;
  --text-xs:    0.75rem;
  --text-sm:    0.875rem;
  --text-base:  1rem;
  --text-lg:    1.125rem;
  --text-xl:    1.25rem;
  --text-2xl:   1.5rem;
  --text-3xl:   2rem;
  --text-4xl:   2.75rem;
  --text-5xl:   3.75rem;
  --text-6xl:   5rem;
  --text-7xl:   7rem;
  --text-8xl:   10rem;
  --leading-none:    1;
  --leading-tight:   1.1;
  --leading-snug:    1.25;
  --leading-normal:  1.5;
  --leading-relaxed: 1.65;
  --tracking-tightest: -0.06em;
  --tracking-tighter:  -0.03em;
  --tracking-tight:    -0.01em;
  --tracking-normal:   0;
  --tracking-wide:     0.05em;
  --tracking-wider:    0.1em;
  --tracking-caps:     0.2em;

  /* --- Spacing (base-4) --- */
  --space-0:  0;
  --space-px: 1px;
  --space-1:  4px;
  --space-2:  8px;
  --space-3:  12px;
  --space-4:  16px;
  --space-6:  24px;
  --space-8:  32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
  --space-32: 128px;
  --space-40: 160px;

  /* --- Border Radius (sharp or pill) --- */
  --radius-none: 0;
  --radius-sm:   2px;
  --radius-md:   4px;
  --radius-lg:   6px;
  --radius-full: 9999px;

  /* --- Shadows (dramatic) --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.08);
  --shadow-sm:  0 2px 6px oklch(0 0 0 / 0.12);
  --shadow-md:  0 4px 12px oklch(0 0 0 / 0.16);
  --shadow-lg:  0 8px 24px oklch(0 0 0 / 0.20);
  --shadow-xl:  0 16px 48px oklch(0 0 0 / 0.25);
  --shadow-hard: 4px 4px 0 var(--color-black);

  /* --- Motion (punchy, fast) --- */
  --duration-instant:  30ms;
  --duration-fast:     80ms;
  --duration-normal:   150ms;
  --duration-moderate: 250ms;
  --duration-slow:     400ms;
  --ease-out:    cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in:     cubic-bezier(0.55, 0.055, 0.675, 0.19);
  --ease-in-out: cubic-bezier(0.87, 0, 0.13, 1);
  --ease-snap:   cubic-bezier(0.2, 0, 0, 1);

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
  --opacity-disabled: 0.3;
  --opacity-muted:    0.5;
  --opacity-subtle:   0.75;
  --opacity-full:     1;
}
```

---

## 4. Social Media (Feed-Based)

Content-forward, minimal chrome. The UI disappears so user content shines. Thin borders, subtle interactions. Inspired by Instagram, Twitter/X, Threads.

```css
:root {
  /* ================================================================
     SOCIAL MEDIA PRESET — Feed-Based
     Content-forward, minimal chrome, subtle interactions
     ================================================================ */

  /* --- Primitive: True Gray Scale (near-achromatic, hue 250) --- */
  --color-gray-50:  oklch(0.98 0.002 250);
  --color-gray-100: oklch(0.96 0.003 250);
  --color-gray-200: oklch(0.92 0.004 250);
  --color-gray-300: oklch(0.85 0.004 250);
  --color-gray-400: oklch(0.73 0.004 250);
  --color-gray-500: oklch(0.58 0.004 250);
  --color-gray-600: oklch(0.47 0.004 250);
  --color-gray-700: oklch(0.36 0.003 250);
  --color-gray-800: oklch(0.26 0.003 250);
  --color-gray-900: oklch(0.18 0.003 250);
  --color-gray-950: oklch(0.12 0.003 250);

  /* --- Primitive: Blue Brand --- */
  --color-blue-50:  oklch(0.96 0.02 240);
  --color-blue-100: oklch(0.92 0.05 240);
  --color-blue-200: oklch(0.84 0.09 240);
  --color-blue-300: oklch(0.74 0.14 240);
  --color-blue-400: oklch(0.64 0.18 240);
  --color-blue-500: oklch(0.55 0.20 240);
  --color-blue-600: oklch(0.48 0.20 240);
  --color-blue-700: oklch(0.40 0.18 240);

  /* --- Primitive: Engagement Colors --- */
  --color-heart:     oklch(0.55 0.25 15);
  --color-repost:    oklch(0.58 0.17 155);
  --color-bookmark:  oklch(0.55 0.20 240);
  --color-verified:  oklch(0.55 0.20 240);

  /* --- Primitive: Gradient (stories/reels) --- */
  --gradient-stories: linear-gradient(135deg,
    oklch(0.65 0.22 330),
    oklch(0.60 0.25 15),
    oklch(0.70 0.20 60));

  /* --- Primitive: Status --- */
  --color-green-500:  oklch(0.58 0.14 150);
  --color-red-500:    oklch(0.55 0.22 25);
  --color-amber-500:  oklch(0.78 0.14 80);

  /* --- Semantic: Light Mode --- */
  --color-bg:              white;
  --color-bg-subtle:       var(--color-gray-50);
  --color-bg-feed:         var(--color-gray-100);
  --color-surface:         white;
  --color-surface-raised:  white;
  --color-surface-overlay: white;
  --color-surface-hover:   var(--color-gray-50);
  --color-text-primary:    var(--color-gray-950);
  --color-text-secondary:  var(--color-gray-500);
  --color-text-tertiary:   var(--color-gray-400);
  --color-text-link:       var(--color-blue-500);
  --color-text-inverse:    white;
  --color-primary:         var(--color-blue-500);
  --color-primary-hover:   var(--color-blue-600);
  --color-primary-subtle:  var(--color-blue-50);
  --color-border:          var(--color-gray-200);
  --color-border-subtle:   var(--color-gray-100);
  --color-separator:       var(--color-gray-100);
  --color-focus-ring:      oklch(0.55 0.20 240 / 0.3);
  --color-success:         var(--color-green-500);
  --color-error:           var(--color-red-500);
  --color-warning:         var(--color-amber-500);
  --color-like:            var(--color-heart);
  --color-share:           var(--color-repost);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             oklch(0.00 0 0);
  --color-bg-subtle-dark:      oklch(0.10 0.003 250);
  --color-bg-feed-dark:        oklch(0.00 0 0);
  --color-surface-dark:        oklch(0.14 0.003 250);
  --color-surface-raised-dark: oklch(0.18 0.003 250);
  --color-text-primary-dark:   oklch(0.97 0.002 250);
  --color-text-secondary-dark: oklch(0.62 0.004 250);
  --color-border-dark:         oklch(0.22 0.003 250);
  --color-separator-dark:      oklch(0.18 0.003 250);

  /* --- Typography --- */
  --font-sans:    'SF Pro', 'Inter', system-ui, sans-serif;
  --font-mono:    'SF Mono', monospace;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --text-2xs:   0.6875rem;   /* 11px */
  --text-xs:    0.75rem;     /* 12px */
  --text-sm:    0.875rem;    /* 14px */
  --text-base:  0.9375rem;   /* 15px — social default */
  --text-lg:    1rem;        /* 16px */
  --text-xl:    1.125rem;    /* 18px */
  --text-2xl:   1.25rem;     /* 20px */
  --text-3xl:   1.5rem;      /* 24px */
  --text-4xl:   2rem;        /* 32px */
  --leading-tight:   1.2;
  --leading-snug:    1.35;
  --leading-normal:  1.5;
  --leading-relaxed: 1.6;
  --tracking-tight:  -0.01em;
  --tracking-normal: 0;
  --tracking-wide:   0.01em;

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

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-2xl:  24px;
  --radius-full: 9999px;

  /* --- Shadows (minimal) --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.03);
  --shadow-sm:  0 1px 3px oklch(0 0 0 / 0.05);
  --shadow-md:  0 3px 8px oklch(0 0 0 / 0.08);
  --shadow-lg:  0 8px 20px oklch(0 0 0 / 0.10);
  --shadow-xl:  0 16px 40px oklch(0 0 0 / 0.14);

  /* --- Motion (snappy, responsive) --- */
  --duration-instant:  30ms;
  --duration-fast:     80ms;
  --duration-normal:   150ms;
  --duration-moderate: 250ms;
  --duration-slow:     400ms;
  --ease-out:    cubic-bezier(0.25, 1, 0.5, 1);
  --ease-in:     cubic-bezier(0.5, 0, 0.75, 0);
  --ease-in-out: cubic-bezier(0.45, 0, 0.55, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);

  /* --- Breakpoints --- */
  --bp-sm:  640px;
  --bp-md:  768px;
  --bp-lg:  1024px;
  --bp-xl:  1280px;

  /* --- Z-Index --- */
  --z-base:     0;
  --z-raised:   1;
  --z-dropdown: 10;
  --z-sticky:   20;
  --z-overlay:  30;
  --z-modal:    40;
  --z-popover:  50;
  --z-toast:    60;
  --z-stories:  70;
  --z-max:      9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.35;
  --opacity-muted:    0.55;
  --opacity-subtle:   0.75;
  --opacity-full:     1;
}
```

---

## 5. Community / Forum (Readable & Compact)

Readability-first, compact density, scalable information hierarchy. Long-form content support. Inspired by Reddit, Discord, Discourse, Hacker News.

```css
:root {
  /* ================================================================
     COMMUNITY / FORUM PRESET
     Readable, compact, scalable, dark-friendly
     ================================================================ */

  /* --- Primitive: Cool Gray Scale (hue 220) --- */
  --color-gray-50:  oklch(0.98 0.004 220);
  --color-gray-100: oklch(0.96 0.005 220);
  --color-gray-200: oklch(0.92 0.006 220);
  --color-gray-300: oklch(0.85 0.007 220);
  --color-gray-400: oklch(0.72 0.007 220);
  --color-gray-500: oklch(0.57 0.007 220);
  --color-gray-600: oklch(0.47 0.007 220);
  --color-gray-700: oklch(0.37 0.006 220);
  --color-gray-800: oklch(0.27 0.006 220);
  --color-gray-850: oklch(0.22 0.007 220);
  --color-gray-900: oklch(0.17 0.007 220);
  --color-gray-950: oklch(0.12 0.007 220);

  /* --- Primitive: Brand (Indigo) --- */
  --color-brand-50:  oklch(0.96 0.02 270);
  --color-brand-100: oklch(0.92 0.04 270);
  --color-brand-200: oklch(0.84 0.08 270);
  --color-brand-300: oklch(0.74 0.13 270);
  --color-brand-400: oklch(0.63 0.17 270);
  --color-brand-500: oklch(0.53 0.19 270);
  --color-brand-600: oklch(0.46 0.19 270);
  --color-brand-700: oklch(0.38 0.16 270);

  /* --- Primitive: Community Colors (flair/badges) --- */
  --color-orange-500: oklch(0.68 0.18 50);
  --color-teal-500:   oklch(0.58 0.12 180);
  --color-pink-500:   oklch(0.62 0.18 340);
  --color-lime-500:   oklch(0.75 0.18 130);

  /* --- Primitive: Voting --- */
  --color-upvote:   oklch(0.65 0.18 50);
  --color-downvote: oklch(0.53 0.19 270);

  /* --- Primitive: Status --- */
  --color-green-500:  oklch(0.58 0.14 150);
  --color-red-500:    oklch(0.55 0.20 25);
  --color-amber-500:  oklch(0.78 0.14 80);
  --color-blue-500:   oklch(0.55 0.16 245);

  /* --- Semantic: Light Mode --- */
  --color-bg:             var(--color-gray-100);
  --color-bg-subtle:      var(--color-gray-50);
  --color-surface:        white;
  --color-surface-raised: white;
  --color-surface-nested: var(--color-gray-50);
  --color-surface-hover:  var(--color-gray-50);
  --color-text-primary:   var(--color-gray-900);
  --color-text-secondary: var(--color-gray-600);
  --color-text-tertiary:  var(--color-gray-400);
  --color-text-link:      var(--color-brand-500);
  --color-text-inverse:   white;
  --color-primary:        var(--color-brand-500);
  --color-primary-hover:  var(--color-brand-600);
  --color-primary-subtle: var(--color-brand-50);
  --color-border:         var(--color-gray-200);
  --color-border-subtle:  var(--color-gray-100);
  --color-border-thread:  var(--color-gray-200);
  --color-focus-ring:     oklch(0.53 0.19 270 / 0.3);
  --color-success:        var(--color-green-500);
  --color-error:          var(--color-red-500);
  --color-warning:        var(--color-amber-500);
  --color-info:           var(--color-blue-500);
  --color-vote-up:        var(--color-upvote);
  --color-vote-down:      var(--color-downvote);
  --color-mod:            var(--color-green-500);
  --color-admin:          var(--color-red-500);
  --color-op:             var(--color-brand-500);

  /* --- Semantic: Dark Mode (default for many forums) --- */
  --color-bg-dark:             oklch(0.10 0.007 220);
  --color-bg-subtle-dark:      oklch(0.12 0.007 220);
  --color-surface-dark:        oklch(0.15 0.007 220);
  --color-surface-raised-dark: oklch(0.18 0.007 220);
  --color-surface-nested-dark: oklch(0.13 0.007 220);
  --color-text-primary-dark:   oklch(0.93 0.004 220);
  --color-text-secondary-dark: oklch(0.65 0.005 220);
  --color-border-dark:         oklch(0.22 0.007 220);
  --color-border-thread-dark:  oklch(0.25 0.007 220);

  /* --- Typography --- */
  --font-sans:    'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', 'Fira Code', monospace;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --text-2xs:   0.6875rem;  /* 11px */
  --text-xs:    0.75rem;    /* 12px */
  --text-sm:    0.8125rem;  /* 13px — compact default */
  --text-base:  0.875rem;   /* 14px */
  --text-lg:    1rem;       /* 16px */
  --text-xl:    1.125rem;   /* 18px */
  --text-2xl:   1.25rem;    /* 20px */
  --text-3xl:   1.5rem;     /* 24px */
  --text-4xl:   2rem;       /* 32px */
  --leading-tight:   1.25;
  --leading-snug:    1.4;
  --leading-normal:  1.55;
  --leading-relaxed: 1.7;
  --tracking-tight:  -0.01em;
  --tracking-normal: 0;
  --tracking-wide:   0.02em;

  /* --- Spacing (compact, base-4) --- */
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

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-2xl:  24px;
  --radius-full: 9999px;

  /* --- Shadows --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.04);
  --shadow-sm:  0 1px 3px oklch(0 0 0 / 0.06);
  --shadow-md:  0 3px 8px oklch(0 0 0 / 0.08);
  --shadow-lg:  0 8px 16px oklch(0 0 0 / 0.10);
  --shadow-xl:  0 16px 32px oklch(0 0 0 / 0.14);

  /* --- Motion --- */
  --duration-instant:  30ms;
  --duration-fast:     80ms;
  --duration-normal:   150ms;
  --duration-moderate: 250ms;
  --duration-slow:     400ms;
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

## Usage Notes

### Product Card Shadow Pattern
For e-commerce cards with hover elevation:
```css
.product-card {
  box-shadow: var(--shadow-card);
  transition: box-shadow var(--duration-normal) var(--ease-out);
}
.product-card:hover {
  box-shadow: var(--shadow-card-hover, var(--shadow-lg));
}
```

### Feed Item Separator Pattern
For social/forum feed separators:
```css
.feed-item + .feed-item {
  border-top: 1px solid var(--color-separator, var(--color-border-subtle));
}
```

### Thread Nesting Pattern
For community threaded replies:
```css
.reply {
  border-left: 2px solid var(--color-border-thread);
  margin-left: var(--space-4);
  padding-left: var(--space-4);
}
```
