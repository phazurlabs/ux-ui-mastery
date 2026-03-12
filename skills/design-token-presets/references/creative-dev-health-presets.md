# Creative, Developer & Health Design Token Presets

Complete, production-ready CSS custom property token systems for creative portfolios, developer tools, healthcare, education, and sustainability products. Each preset is a deployable `:root {}` block following the 3-tier token architecture with oklch color space.

---

## 1. Creative Portfolio (Designer / Agency)

Expressive, editorial, dramatic. Large type, bold contrasts, gallery-ready spacing. The portfolio IS the product. Inspired by agencies like Pentagram, ueno, Locomotive.

```css
:root {
  /* ================================================================
     CREATIVE PORTFOLIO PRESET
     Expressive, editorial, dramatic, gallery-ready
     ================================================================ */

  /* --- Primitive: Neutral Scale (near-black dominant, hue 270) --- */
  --color-neutral-50:  oklch(0.98 0.003 270);
  --color-neutral-100: oklch(0.95 0.004 270);
  --color-neutral-200: oklch(0.90 0.005 270);
  --color-neutral-300: oklch(0.82 0.006 270);
  --color-neutral-400: oklch(0.68 0.006 270);
  --color-neutral-500: oklch(0.54 0.006 270);
  --color-neutral-600: oklch(0.44 0.006 270);
  --color-neutral-700: oklch(0.34 0.005 270);
  --color-neutral-800: oklch(0.24 0.005 270);
  --color-neutral-900: oklch(0.16 0.004 270);
  --color-neutral-950: oklch(0.10 0.004 270);
  --color-black:       oklch(0.05 0.003 270);

  /* --- Primitive: Accent (Vibrant Magenta) --- */
  --color-accent-50:  oklch(0.96 0.03 340);
  --color-accent-100: oklch(0.90 0.06 340);
  --color-accent-200: oklch(0.82 0.12 340);
  --color-accent-300: oklch(0.72 0.18 340);
  --color-accent-400: oklch(0.62 0.22 340);
  --color-accent-500: oklch(0.55 0.25 340);
  --color-accent-600: oklch(0.48 0.23 340);
  --color-accent-700: oklch(0.40 0.20 340);
  --color-accent-800: oklch(0.32 0.16 340);
  --color-accent-900: oklch(0.24 0.12 340);

  /* --- Primitive: Secondary (Electric Blue) --- */
  --color-electric-50:  oklch(0.96 0.02 255);
  --color-electric-100: oklch(0.90 0.06 255);
  --color-electric-400: oklch(0.62 0.20 255);
  --color-electric-500: oklch(0.55 0.22 255);
  --color-electric-600: oklch(0.48 0.22 255);

  /* --- Primitive: Gradients --- */
  --gradient-hero:      linear-gradient(135deg, oklch(0.55 0.25 340), oklch(0.55 0.22 255));
  --gradient-dark-mesh: radial-gradient(ellipse at 30% 70%, oklch(0.20 0.08 340) 0%, transparent 50%),
                        radial-gradient(ellipse at 70% 30%, oklch(0.18 0.06 255) 0%, transparent 50%),
                        oklch(0.05 0.003 270);
  --gradient-text:      linear-gradient(90deg, oklch(0.55 0.25 340), oklch(0.55 0.22 255));

  /* --- Primitive: Status --- */
  --color-green-500: oklch(0.58 0.15 150);
  --color-red-500:   oklch(0.55 0.22 25);
  --color-amber-500: oklch(0.75 0.15 80);

  /* --- Semantic: Dark Mode (default) --- */
  --color-bg:              var(--color-black);
  --color-bg-subtle:       var(--color-neutral-950);
  --color-bg-dramatic:     oklch(0.03 0.002 270);
  --color-surface:         var(--color-neutral-900);
  --color-surface-raised:  var(--color-neutral-800);
  --color-surface-overlay: oklch(0.16 0.005 270 / 0.95);
  --color-text-primary:    var(--color-neutral-50);
  --color-text-secondary:  var(--color-neutral-400);
  --color-text-tertiary:   var(--color-neutral-500);
  --color-text-muted:      var(--color-neutral-600);
  --color-primary:         var(--color-accent-500);
  --color-primary-hover:   var(--color-accent-400);
  --color-primary-subtle:  oklch(0.55 0.25 340 / 0.10);
  --color-secondary:       var(--color-electric-500);
  --color-border:          var(--color-neutral-800);
  --color-border-subtle:   var(--color-neutral-900);
  --color-border-accent:   var(--color-accent-500);
  --color-cursor:          var(--color-accent-500);
  --color-success:         var(--color-green-500);
  --color-error:           var(--color-red-500);
  --color-warning:         var(--color-amber-500);

  /* --- Semantic: Light Mode --- */
  --color-bg-light:             white;
  --color-bg-subtle-light:      var(--color-neutral-50);
  --color-surface-light:        white;
  --color-surface-raised-light: white;
  --color-text-primary-light:   var(--color-black);
  --color-text-secondary-light: var(--color-neutral-600);
  --color-border-light:         var(--color-neutral-200);

  /* --- Typography (editorial, expressive) --- */
  --font-display:  'PP Neue Montreal', 'Syne', 'Space Grotesk', sans-serif;
  --font-heading:  'PP Neue Montreal', 'Syne', sans-serif;
  --font-sans:     'Inter', 'DM Sans', system-ui, sans-serif;
  --font-serif:    'PP Editorial New', 'Playfair Display', serif;
  --font-mono:     'JetBrains Mono', 'Fira Code', monospace;
  --font-weight-light:     300;
  --font-weight-regular:   400;
  --font-weight-medium:    500;
  --font-weight-semibold:  600;
  --font-weight-bold:      700;
  --font-weight-extrabold: 800;
  --font-weight-black:     900;
  --text-xs:    0.75rem;
  --text-sm:    0.875rem;
  --text-base:  1rem;
  --text-lg:    1.125rem;
  --text-xl:    1.25rem;
  --text-2xl:   1.5rem;
  --text-3xl:   2rem;
  --text-4xl:   2.75rem;
  --text-5xl:   3.5rem;
  --text-6xl:   4.5rem;
  --text-7xl:   6rem;
  --text-8xl:   8rem;
  --text-hero:  clamp(3rem, 8vw, 10rem);
  --leading-none:    0.9;
  --leading-tight:   1.05;
  --leading-snug:    1.2;
  --leading-normal:  1.5;
  --leading-relaxed: 1.65;
  --tracking-tightest: -0.06em;
  --tracking-tighter:  -0.04em;
  --tracking-tight:    -0.02em;
  --tracking-normal:   0;
  --tracking-wide:     0.04em;
  --tracking-wider:    0.08em;
  --tracking-caps:     0.15em;

  /* --- Spacing (dramatic, generous) --- */
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
  --space-48: 192px;
  --space-64: 256px;
  --space-section: clamp(64px, 10vw, 192px);

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-2xl:  24px;
  --radius-full: 9999px;

  /* --- Shadows (dark-optimized) --- */
  --shadow-xs:  0 1px 3px oklch(0 0 0 / 0.20);
  --shadow-sm:  0 2px 6px oklch(0 0 0 / 0.25);
  --shadow-md:  0 4px 12px oklch(0 0 0 / 0.30);
  --shadow-lg:  0 8px 24px oklch(0 0 0 / 0.35);
  --shadow-xl:  0 16px 48px oklch(0 0 0 / 0.40);
  --shadow-glow: 0 0 30px oklch(0.55 0.25 340 / 0.15);
  --shadow-glow-blue: 0 0 30px oklch(0.55 0.22 255 / 0.15);

  /* --- Motion (cinematic, expressive) --- */
  --duration-instant:  50ms;
  --duration-fast:     150ms;
  --duration-normal:   300ms;
  --duration-moderate: 500ms;
  --duration-slow:     800ms;
  --duration-slower:   1200ms;
  --duration-cinematic: 1800ms;
  --ease-out:      cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in:       cubic-bezier(0.55, 0.055, 0.675, 0.19);
  --ease-in-out:   cubic-bezier(0.87, 0, 0.13, 1);
  --ease-spring:   cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-dramatic: cubic-bezier(0.76, 0, 0.24, 1);

  /* --- Breakpoints --- */
  --bp-sm:  640px;
  --bp-md:  768px;
  --bp-lg:  1024px;
  --bp-xl:  1440px;
  --bp-2xl: 1920px;

  /* --- Z-Index --- */
  --z-base:       0;
  --z-raised:     1;
  --z-dropdown:   10;
  --z-sticky:     20;
  --z-overlay:    30;
  --z-modal:      40;
  --z-popover:    50;
  --z-toast:      60;
  --z-cursor:     70;
  --z-transition: 80;
  --z-max:        9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.3;
  --opacity-muted:    0.5;
  --opacity-subtle:   0.7;
  --opacity-full:     1;
}
```

---

## 2. Developer Tools (VS Code / GitHub Style)

Monospace-heavy, dark-first, syntax highlighting tokens. Information-dense, keyboard-friendly. Inspired by VS Code, GitHub, Linear, Warp.

```css
:root {
  /* ================================================================
     DEVELOPER TOOLS PRESET
     Monospace-heavy, dark-first, syntax colors, info-dense
     ================================================================ */

  /* --- Primitive: Slate Scale (cool blue-gray, hue 225) --- */
  --color-slate-50:  oklch(0.98 0.005 225);
  --color-slate-100: oklch(0.95 0.006 225);
  --color-slate-200: oklch(0.90 0.008 225);
  --color-slate-300: oklch(0.82 0.010 225);
  --color-slate-400: oklch(0.68 0.010 225);
  --color-slate-500: oklch(0.55 0.010 225);
  --color-slate-600: oklch(0.44 0.010 225);
  --color-slate-700: oklch(0.34 0.010 225);
  --color-slate-800: oklch(0.24 0.012 225);
  --color-slate-850: oklch(0.20 0.012 225);
  --color-slate-900: oklch(0.16 0.012 225);
  --color-slate-950: oklch(0.12 0.012 225);

  /* --- Primitive: Brand (Blue) --- */
  --color-blue-50:  oklch(0.96 0.02 240);
  --color-blue-100: oklch(0.92 0.05 240);
  --color-blue-200: oklch(0.84 0.10 240);
  --color-blue-300: oklch(0.74 0.14 240);
  --color-blue-400: oklch(0.64 0.18 240);
  --color-blue-500: oklch(0.56 0.20 240);
  --color-blue-600: oklch(0.48 0.20 240);
  --color-blue-700: oklch(0.40 0.17 240);

  /* --- Primitive: Syntax Highlighting Colors --- */
  --syntax-keyword:    oklch(0.68 0.18 310);   /* purple/magenta */
  --syntax-string:     oklch(0.68 0.15 155);   /* green */
  --syntax-number:     oklch(0.70 0.15 80);    /* amber/orange */
  --syntax-function:   oklch(0.70 0.16 240);   /* blue */
  --syntax-variable:   oklch(0.78 0.10 200);   /* light cyan */
  --syntax-type:       oklch(0.68 0.14 180);   /* teal */
  --syntax-constant:   oklch(0.68 0.18 310);   /* purple */
  --syntax-comment:    oklch(0.50 0.005 225);   /* muted gray */
  --syntax-operator:   oklch(0.78 0.12 55);    /* warm yellow */
  --syntax-tag:        oklch(0.65 0.18 20);    /* red/coral */
  --syntax-attribute:  oklch(0.70 0.16 240);   /* blue */
  --syntax-property:   oklch(0.78 0.10 200);   /* light cyan */
  --syntax-punctuation: oklch(0.60 0.005 225); /* subtle gray */
  --syntax-regex:      oklch(0.65 0.18 20);    /* red */
  --syntax-class:      oklch(0.72 0.14 60);    /* gold */
  --syntax-decorator:  oklch(0.70 0.16 240);   /* blue */

  /* --- Primitive: Diff Colors --- */
  --color-diff-add-bg:    oklch(0.30 0.05 150 / 0.20);
  --color-diff-add-text:  oklch(0.70 0.14 150);
  --color-diff-del-bg:    oklch(0.30 0.05 20 / 0.20);
  --color-diff-del-text:  oklch(0.70 0.14 20);
  --color-diff-change-bg: oklch(0.30 0.05 80 / 0.15);

  /* --- Primitive: Status --- */
  --color-green-500:  oklch(0.60 0.16 150);
  --color-red-500:    oklch(0.58 0.20 25);
  --color-amber-500:  oklch(0.78 0.15 80);
  --color-cyan-500:   oklch(0.65 0.12 200);

  /* --- Semantic: Dark Mode (default) --- */
  --color-bg:              var(--color-slate-950);
  --color-bg-subtle:       oklch(0.14 0.012 225);
  --color-bg-editor:       oklch(0.13 0.012 225);
  --color-bg-sidebar:      oklch(0.11 0.012 225);
  --color-bg-panel:        oklch(0.14 0.012 225);
  --color-bg-terminal:     oklch(0.08 0.010 225);
  --color-surface:         var(--color-slate-900);
  --color-surface-raised:  var(--color-slate-850);
  --color-surface-overlay: oklch(0.20 0.012 225 / 0.95);
  --color-surface-hover:   var(--color-slate-800);
  --color-text-primary:    var(--color-slate-100);
  --color-text-secondary:  var(--color-slate-400);
  --color-text-tertiary:   var(--color-slate-500);
  --color-text-muted:      var(--color-slate-600);
  --color-primary:         var(--color-blue-500);
  --color-primary-hover:   var(--color-blue-400);
  --color-primary-subtle:  oklch(0.56 0.20 240 / 0.12);
  --color-border:          var(--color-slate-800);
  --color-border-subtle:   var(--color-slate-850);
  --color-border-strong:   var(--color-slate-700);
  --color-focus-ring:      oklch(0.56 0.20 240 / 0.5);
  --color-selection:       oklch(0.56 0.20 240 / 0.20);
  --color-line-highlight:  oklch(0.20 0.012 225 / 0.5);
  --color-success:         var(--color-green-500);
  --color-error:           var(--color-red-500);
  --color-warning:         var(--color-amber-500);
  --color-info:            var(--color-cyan-500);

  /* --- Semantic: Light Mode --- */
  --color-bg-light:             white;
  --color-bg-editor-light:      white;
  --color-bg-sidebar-light:     var(--color-slate-50);
  --color-surface-light:        white;
  --color-text-primary-light:   var(--color-slate-900);
  --color-text-secondary-light: var(--color-slate-600);
  --color-border-light:         var(--color-slate-200);

  /* --- Typography (mono-forward) --- */
  --font-mono:    'JetBrains Mono', 'Fira Code', 'SF Mono', 'Cascadia Code', monospace;
  --font-sans:    'Inter', 'SF Pro', system-ui, sans-serif;
  --font-display: 'Inter', system-ui, sans-serif;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --text-2xs:   0.625rem;   /* 10px */
  --text-xs:    0.6875rem;  /* 11px */
  --text-sm:    0.8125rem;  /* 13px — editor default */
  --text-base:  0.875rem;   /* 14px */
  --text-lg:    1rem;       /* 16px */
  --text-xl:    1.125rem;   /* 18px */
  --text-2xl:   1.25rem;    /* 20px */
  --text-3xl:   1.5rem;     /* 24px */
  --text-4xl:   2rem;       /* 32px */
  --text-code:  0.8125rem;  /* 13px — code blocks */
  --leading-tight:   1.2;
  --leading-snug:    1.35;
  --leading-normal:  1.5;
  --leading-relaxed: 1.6;
  --leading-code:    1.7;
  --tracking-tight:  -0.02em;
  --tracking-normal: 0;
  --tracking-wide:   0.02em;
  --tracking-mono:   -0.03em;

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
  --space-20: 80px;
  --space-24: 96px;

  /* --- Border Radius (minimal) --- */
  --radius-none: 0;
  --radius-sm:   3px;
  --radius-md:   6px;
  --radius-lg:   8px;
  --radius-xl:   12px;
  --radius-full: 9999px;

  /* --- Shadows (subtle, dark-optimized) --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.15);
  --shadow-sm:  0 2px 4px oklch(0 0 0 / 0.20);
  --shadow-md:  0 4px 8px oklch(0 0 0 / 0.25);
  --shadow-lg:  0 8px 16px oklch(0 0 0 / 0.30);
  --shadow-xl:  0 16px 32px oklch(0 0 0 / 0.35);
  --shadow-command: 0 16px 48px oklch(0 0 0 / 0.40);

  /* --- Motion (fast, functional) --- */
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
  --bp-xl:  1280px;
  --bp-2xl: 1536px;
  --bp-3xl: 1920px;

  /* --- Z-Index --- */
  --z-base:      0;
  --z-raised:    1;
  --z-gutter:    5;
  --z-dropdown:  10;
  --z-sticky:    20;
  --z-overlay:   30;
  --z-modal:     40;
  --z-popover:   50;
  --z-toast:     60;
  --z-command:   70;
  --z-max:       9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.35;
  --opacity-muted:    0.5;
  --opacity-subtle:   0.7;
  --opacity-full:     1;
}
```

---

## 3. Healthcare (HIPAA-Friendly)

Calming, accessible, high contrast, professional. Blues and greens for trust and calm. Large touch targets, clear hierarchy. Inspired by medical portals, Epic MyChart, Calm.

```css
:root {
  /* ================================================================
     HEALTHCARE PRESET — HIPAA-Friendly
     Calming, accessible, high contrast, professional
     ================================================================ */

  /* --- Primitive: Cool Blue-Gray Scale (hue 215) --- */
  --color-gray-50:  oklch(0.98 0.005 215);
  --color-gray-100: oklch(0.96 0.006 215);
  --color-gray-200: oklch(0.92 0.007 215);
  --color-gray-300: oklch(0.85 0.008 215);
  --color-gray-400: oklch(0.72 0.008 215);
  --color-gray-500: oklch(0.57 0.008 215);
  --color-gray-600: oklch(0.47 0.008 215);
  --color-gray-700: oklch(0.37 0.007 215);
  --color-gray-800: oklch(0.27 0.007 215);
  --color-gray-900: oklch(0.19 0.006 215);
  --color-gray-950: oklch(0.13 0.006 215);

  /* --- Primitive: Medical Blue (primary trust color) --- */
  --color-blue-50:  oklch(0.97 0.02 225);
  --color-blue-100: oklch(0.93 0.04 225);
  --color-blue-200: oklch(0.87 0.08 225);
  --color-blue-300: oklch(0.78 0.12 225);
  --color-blue-400: oklch(0.67 0.15 225);
  --color-blue-500: oklch(0.56 0.16 225);
  --color-blue-600: oklch(0.48 0.16 225);
  --color-blue-700: oklch(0.40 0.14 225);
  --color-blue-800: oklch(0.32 0.12 225);
  --color-blue-900: oklch(0.24 0.09 225);

  /* --- Primitive: Teal (wellness/calm) --- */
  --color-teal-50:  oklch(0.97 0.02 175);
  --color-teal-100: oklch(0.93 0.04 175);
  --color-teal-200: oklch(0.86 0.07 175);
  --color-teal-300: oklch(0.76 0.10 175);
  --color-teal-400: oklch(0.65 0.12 175);
  --color-teal-500: oklch(0.55 0.12 175);
  --color-teal-600: oklch(0.48 0.12 175);
  --color-teal-700: oklch(0.40 0.10 175);

  /* --- Primitive: Status Colors (high contrast for accessibility) --- */
  --color-green-50:  oklch(0.96 0.02 150);
  --color-green-100: oklch(0.92 0.04 150);
  --color-green-500: oklch(0.52 0.14 150);
  --color-green-700: oklch(0.40 0.12 150);
  --color-red-50:    oklch(0.96 0.02 25);
  --color-red-100:   oklch(0.92 0.05 25);
  --color-red-500:   oklch(0.50 0.20 25);
  --color-red-700:   oklch(0.40 0.17 25);
  --color-amber-50:  oklch(0.96 0.03 80);
  --color-amber-100: oklch(0.92 0.05 80);
  --color-amber-500: oklch(0.72 0.14 80);
  --color-amber-700: oklch(0.58 0.12 80);

  /* --- Semantic: Light Mode --- */
  --color-bg:              white;
  --color-bg-subtle:       var(--color-gray-50);
  --color-bg-calming:      var(--color-blue-50);
  --color-surface:         white;
  --color-surface-raised:  white;
  --color-surface-overlay: white;
  --color-surface-info:    var(--color-blue-50);
  --color-text-primary:    var(--color-gray-900);
  --color-text-secondary:  var(--color-gray-600);
  --color-text-tertiary:   var(--color-gray-500);
  --color-text-inverse:    white;
  --color-text-critical:   var(--color-red-700);
  --color-primary:         var(--color-blue-600);
  --color-primary-hover:   var(--color-blue-700);
  --color-primary-subtle:  var(--color-blue-50);
  --color-secondary:       var(--color-teal-500);
  --color-secondary-hover: var(--color-teal-600);
  --color-secondary-subtle: var(--color-teal-50);
  --color-border:          var(--color-gray-200);
  --color-border-subtle:   var(--color-gray-100);
  --color-border-strong:   var(--color-gray-300);
  --color-border-input:    var(--color-gray-300);
  --color-focus-ring:      oklch(0.56 0.16 225 / 0.4);
  --color-success:         var(--color-green-500);
  --color-success-subtle:  var(--color-green-50);
  --color-error:           var(--color-red-500);
  --color-error-subtle:    var(--color-red-50);
  --color-warning:         var(--color-amber-500);
  --color-warning-subtle:  var(--color-amber-50);
  --color-info:            var(--color-blue-500);
  --color-info-subtle:     var(--color-blue-50);
  --color-urgent:          var(--color-red-500);
  --color-normal:          var(--color-green-500);
  --color-elevated:        var(--color-amber-500);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             oklch(0.12 0.006 215);
  --color-bg-subtle-dark:      oklch(0.15 0.006 215);
  --color-surface-dark:        oklch(0.18 0.006 215);
  --color-surface-raised-dark: oklch(0.22 0.006 215);
  --color-text-primary-dark:   oklch(0.95 0.005 215);
  --color-text-secondary-dark: oklch(0.68 0.006 215);
  --color-border-dark:         oklch(0.27 0.006 215);

  /* --- Typography (clean, accessible, large) --- */
  --font-sans:    'Inter', 'SF Pro', system-ui, sans-serif;
  --font-display: 'Inter', system-ui, sans-serif;
  --font-mono:    'SF Mono', 'JetBrains Mono', monospace;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --text-xs:    0.75rem;    /* 12px — minimum for labels */
  --text-sm:    0.875rem;   /* 14px */
  --text-base:  1rem;       /* 16px — body minimum */
  --text-lg:    1.125rem;   /* 18px — preferred body */
  --text-xl:    1.25rem;    /* 20px */
  --text-2xl:   1.5rem;     /* 24px */
  --text-3xl:   1.875rem;   /* 30px */
  --text-4xl:   2.25rem;    /* 36px */
  --text-5xl:   3rem;       /* 48px */
  --leading-tight:   1.25;
  --leading-snug:    1.4;
  --leading-normal:  1.6;
  --leading-relaxed: 1.75;
  --leading-loose:   2;
  --tracking-tight:  -0.01em;
  --tracking-normal: 0;
  --tracking-wide:   0.02em;

  /* --- Spacing (generous for touch, base-4) --- */
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
  --touch-target-min: 44px;   /* WCAG minimum */
  --touch-target-comfortable: 48px;

  /* --- Border Radius --- */
  --radius-none: 0;
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-2xl:  20px;
  --radius-full: 9999px;

  /* --- Shadows (gentle) --- */
  --shadow-xs:  0 1px 2px oklch(0 0 0 / 0.03);
  --shadow-sm:  0 1px 3px oklch(0 0 0 / 0.05);
  --shadow-md:  0 3px 8px oklch(0 0 0 / 0.07);
  --shadow-lg:  0 8px 16px oklch(0 0 0 / 0.09);
  --shadow-xl:  0 16px 32px oklch(0 0 0 / 0.11);
  --shadow-card: 0 1px 4px oklch(0 0 0 / 0.04), 0 0 0 1px oklch(0 0 0 / 0.02);

  /* --- Motion (calm, reassuring) --- */
  --duration-instant:  50ms;
  --duration-fast:     120ms;
  --duration-normal:   200ms;
  --duration-moderate: 350ms;
  --duration-slow:     500ms;
  --ease-out:    cubic-bezier(0.25, 1, 0.5, 1);
  --ease-in:     cubic-bezier(0.5, 0, 0.75, 0);
  --ease-in-out: cubic-bezier(0.45, 0, 0.55, 1);
  --ease-gentle: cubic-bezier(0.4, 0, 0.2, 1);

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
  --z-alert:    70;
  --z-max:      9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.45;
  --opacity-muted:    0.6;
  --opacity-subtle:   0.8;
  --opacity-full:     1;
}
```

---

## 4. Education / EdTech (Friendly & Organized)

Friendly, colorful but organized. Large touch targets, clear hierarchy, joyful but professional. Inspired by Duolingo, Khan Academy, Coursera, Notion for Education.

```css
:root {
  /* ================================================================
     EDUCATION / EDTECH PRESET
     Friendly, colorful, organized, large touch targets
     ================================================================ */

  /* --- Primitive: Warm Gray Scale (hue 45) --- */
  --color-gray-50:  oklch(0.98 0.006 45);
  --color-gray-100: oklch(0.96 0.007 45);
  --color-gray-200: oklch(0.92 0.008 45);
  --color-gray-300: oklch(0.85 0.008 45);
  --color-gray-400: oklch(0.72 0.008 45);
  --color-gray-500: oklch(0.57 0.008 45);
  --color-gray-600: oklch(0.47 0.007 45);
  --color-gray-700: oklch(0.37 0.006 45);
  --color-gray-800: oklch(0.27 0.006 45);
  --color-gray-900: oklch(0.19 0.005 45);
  --color-gray-950: oklch(0.13 0.005 45);

  /* --- Primitive: Primary (Friendly Blue) --- */
  --color-blue-50:  oklch(0.96 0.03 240);
  --color-blue-100: oklch(0.92 0.06 240);
  --color-blue-200: oklch(0.84 0.10 240);
  --color-blue-300: oklch(0.74 0.15 240);
  --color-blue-400: oklch(0.64 0.18 240);
  --color-blue-500: oklch(0.55 0.18 240);
  --color-blue-600: oklch(0.48 0.18 240);
  --color-blue-700: oklch(0.40 0.15 240);
  --color-blue-800: oklch(0.32 0.12 240);

  /* --- Primitive: Subject Colors --- */
  --color-math-100:     oklch(0.93 0.04 250);
  --color-math-500:     oklch(0.55 0.18 250);
  --color-science-100:  oklch(0.93 0.04 155);
  --color-science-500:  oklch(0.55 0.15 155);
  --color-reading-100:  oklch(0.93 0.04 295);
  --color-reading-500:  oklch(0.55 0.16 295);
  --color-art-100:      oklch(0.93 0.04 340);
  --color-art-500:      oklch(0.60 0.18 340);
  --color-history-100:  oklch(0.93 0.04 55);
  --color-history-500:  oklch(0.60 0.12 55);
  --color-music-100:    oklch(0.93 0.04 190);
  --color-music-500:    oklch(0.55 0.14 190);

  /* --- Primitive: Reward / Gamification Colors --- */
  --color-gold:     oklch(0.78 0.14 80);
  --color-silver:   oklch(0.75 0.005 250);
  --color-bronze:   oklch(0.62 0.08 55);
  --color-xp-green: oklch(0.65 0.18 140);
  --color-streak:   oklch(0.68 0.18 45);

  /* --- Primitive: Status --- */
  --color-green-500:  oklch(0.58 0.16 150);
  --color-red-500:    oklch(0.55 0.18 25);
  --color-amber-500:  oklch(0.78 0.14 80);
  --color-purple-500: oklch(0.55 0.16 295);

  /* --- Semantic: Light Mode --- */
  --color-bg:             oklch(0.99 0.004 45);
  --color-bg-subtle:      var(--color-gray-50);
  --color-bg-warm:        oklch(0.98 0.010 55);
  --color-surface:        white;
  --color-surface-raised: white;
  --color-surface-overlay: white;
  --color-surface-card:   white;
  --color-text-primary:   var(--color-gray-900);
  --color-text-secondary: var(--color-gray-600);
  --color-text-tertiary:  var(--color-gray-400);
  --color-text-inverse:   white;
  --color-primary:        var(--color-blue-500);
  --color-primary-hover:  var(--color-blue-600);
  --color-primary-subtle: var(--color-blue-50);
  --color-border:         var(--color-gray-200);
  --color-border-subtle:  var(--color-gray-100);
  --color-border-strong:  var(--color-gray-300);
  --color-focus-ring:     oklch(0.55 0.18 240 / 0.35);
  --color-success:        var(--color-green-500);
  --color-error:          var(--color-red-500);
  --color-warning:        var(--color-amber-500);
  --color-correct:        var(--color-green-500);
  --color-incorrect:      var(--color-red-500);
  --color-progress:       var(--color-blue-500);
  --color-reward:         var(--color-gold);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             oklch(0.13 0.005 45);
  --color-bg-subtle-dark:      oklch(0.16 0.005 45);
  --color-surface-dark:        oklch(0.19 0.005 45);
  --color-surface-raised-dark: oklch(0.23 0.005 45);
  --color-text-primary-dark:   oklch(0.95 0.006 45);
  --color-text-secondary-dark: oklch(0.68 0.006 45);
  --color-border-dark:         oklch(0.27 0.005 45);

  /* --- Typography (friendly, readable) --- */
  --font-sans:    'Nunito', 'Nunito Sans', system-ui, sans-serif;
  --font-display: 'Nunito', 'Poppins', system-ui, sans-serif;
  --font-mono:    'Fira Code', 'JetBrains Mono', monospace;
  --font-weight-regular:  400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;
  --font-weight-extrabold: 800;
  --text-xs:    0.75rem;
  --text-sm:    0.875rem;
  --text-base:  1rem;       /* 16px — body */
  --text-lg:    1.125rem;   /* 18px — preferred reading */
  --text-xl:    1.25rem;
  --text-2xl:   1.5rem;
  --text-3xl:   1.875rem;
  --text-4xl:   2.25rem;
  --text-5xl:   3rem;
  --leading-tight:   1.2;
  --leading-snug:    1.35;
  --leading-normal:  1.6;
  --leading-relaxed: 1.75;
  --leading-loose:   2;
  --tracking-tight:  -0.01em;
  --tracking-normal: 0;
  --tracking-wide:   0.02em;

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
  --touch-target-min: 44px;
  --touch-target-comfortable: 52px;
  --touch-target-large: 60px;

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
  --shadow-lg:   0 8px 16px oklch(0 0 0 / 0.10);
  --shadow-xl:   0 16px 32px oklch(0 0 0 / 0.12);
  --shadow-card: 0 2px 8px oklch(0 0 0 / 0.06), 0 0 0 1px oklch(0 0 0 / 0.02);
  --shadow-button: 0 2px 4px oklch(0 0 0 / 0.08);

  /* --- Motion (playful, responsive) --- */
  --duration-instant:  50ms;
  --duration-fast:     100ms;
  --duration-normal:   200ms;
  --duration-moderate: 300ms;
  --duration-slow:     500ms;
  --duration-celebrate: 800ms;
  --ease-out:     cubic-bezier(0.25, 1, 0.5, 1);
  --ease-in:      cubic-bezier(0.5, 0, 0.75, 0);
  --ease-in-out:  cubic-bezier(0.45, 0, 0.55, 1);
  --ease-bounce:  cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-playful: cubic-bezier(0.68, -0.55, 0.265, 1.55);

  /* --- Breakpoints --- */
  --bp-sm:  640px;
  --bp-md:  768px;
  --bp-lg:  1024px;
  --bp-xl:  1280px;
  --bp-2xl: 1440px;

  /* --- Z-Index --- */
  --z-base:       0;
  --z-raised:     1;
  --z-dropdown:   10;
  --z-sticky:     20;
  --z-overlay:    30;
  --z-modal:      40;
  --z-popover:    50;
  --z-toast:      60;
  --z-confetti:   70;
  --z-max:        9999;

  /* --- Opacity --- */
  --opacity-disabled: 0.45;
  --opacity-muted:    0.6;
  --opacity-subtle:   0.8;
  --opacity-full:     1;
}
```

---

## 5. Sustainability / Green (Earth Tones)

Earth tones, organic feel, warm neutrals. Nature-inspired palette, soft textures, approachable. Inspired by Patagonia, Allbirds, Oatly, sustainable brands.

```css
:root {
  /* ================================================================
     SUSTAINABILITY / GREEN PRESET
     Earth tones, organic feel, warm, nature-inspired
     ================================================================ */

  /* --- Primitive: Earth Gray Scale (warm olive, hue 85) --- */
  --color-earth-50:  oklch(0.98 0.008 85);
  --color-earth-100: oklch(0.96 0.010 85);
  --color-earth-200: oklch(0.92 0.012 80);
  --color-earth-300: oklch(0.85 0.014 75);
  --color-earth-400: oklch(0.72 0.014 70);
  --color-earth-500: oklch(0.57 0.012 65);
  --color-earth-600: oklch(0.47 0.012 65);
  --color-earth-700: oklch(0.37 0.010 60);
  --color-earth-800: oklch(0.27 0.010 55);
  --color-earth-900: oklch(0.19 0.008 50);
  --color-earth-950: oklch(0.13 0.008 50);

  /* --- Primitive: Forest Green (primary brand) --- */
  --color-forest-50:  oklch(0.96 0.02 145);
  --color-forest-100: oklch(0.92 0.04 145);
  --color-forest-200: oklch(0.85 0.07 145);
  --color-forest-300: oklch(0.75 0.11 145);
  --color-forest-400: oklch(0.64 0.14 145);
  --color-forest-500: oklch(0.52 0.14 145);
  --color-forest-600: oklch(0.44 0.13 145);
  --color-forest-700: oklch(0.36 0.11 145);
  --color-forest-800: oklch(0.28 0.09 145);
  --color-forest-900: oklch(0.20 0.07 145);

  /* --- Primitive: Moss (secondary) --- */
  --color-moss-100: oklch(0.92 0.04 120);
  --color-moss-300: oklch(0.72 0.10 120);
  --color-moss-500: oklch(0.55 0.10 120);

  /* --- Primitive: Clay (warm accent) --- */
  --color-clay-50:  oklch(0.96 0.02 40);
  --color-clay-100: oklch(0.92 0.04 40);
  --color-clay-300: oklch(0.74 0.08 40);
  --color-clay-500: oklch(0.58 0.10 35);
  --color-clay-700: oklch(0.42 0.08 35);

  /* --- Primitive: Sky (tertiary) --- */
  --color-sky-100: oklch(0.93 0.03 215);
  --color-sky-500: oklch(0.60 0.10 215);

  /* --- Primitive: Sand / Parchment --- */
  --color-sand:      oklch(0.94 0.015 70);
  --color-parchment: oklch(0.96 0.012 80);
  --color-linen:     oklch(0.97 0.010 60);

  /* --- Primitive: Status --- */
  --color-green-500: oklch(0.55 0.14 150);
  --color-red-500:   oklch(0.52 0.16 25);
  --color-amber-500: oklch(0.72 0.12 75);
  --color-blue-500:  oklch(0.55 0.12 235);

  /* --- Semantic: Light Mode --- */
  --color-bg:              var(--color-linen);
  --color-bg-subtle:       var(--color-parchment);
  --color-bg-warm:         var(--color-sand);
  --color-surface:         white;
  --color-surface-raised:  white;
  --color-surface-overlay: white;
  --color-surface-natural: var(--color-earth-50);
  --color-text-primary:    var(--color-earth-900);
  --color-text-secondary:  var(--color-earth-600);
  --color-text-tertiary:   var(--color-earth-400);
  --color-text-inverse:    white;
  --color-primary:         var(--color-forest-600);
  --color-primary-hover:   var(--color-forest-700);
  --color-primary-subtle:  var(--color-forest-50);
  --color-secondary:       var(--color-clay-500);
  --color-secondary-hover: var(--color-clay-700);
  --color-secondary-subtle: var(--color-clay-50);
  --color-tertiary:        var(--color-sky-500);
  --color-border:          var(--color-earth-200);
  --color-border-subtle:   var(--color-earth-100);
  --color-border-strong:   var(--color-earth-300);
  --color-focus-ring:      oklch(0.52 0.14 145 / 0.35);
  --color-success:         var(--color-green-500);
  --color-error:           var(--color-red-500);
  --color-warning:         var(--color-amber-500);
  --color-info:            var(--color-blue-500);
  --color-eco-badge:       var(--color-forest-500);
  --color-impact-positive: var(--color-forest-500);
  --color-impact-neutral:  var(--color-earth-500);

  /* --- Semantic: Dark Mode --- */
  --color-bg-dark:             oklch(0.12 0.008 50);
  --color-bg-subtle-dark:      oklch(0.15 0.008 55);
  --color-surface-dark:        oklch(0.18 0.008 55);
  --color-surface-raised-dark: oklch(0.22 0.010 60);
  --color-text-primary-dark:   oklch(0.94 0.010 80);
  --color-text-secondary-dark: oklch(0.68 0.010 70);
  --color-border-dark:         oklch(0.27 0.010 55);

  /* --- Typography (organic, warm) --- */
  --font-display: 'Fraunces', 'Lora', 'Georgia', serif;
  --font-heading: 'Fraunces', 'Lora', serif;
  --font-sans:    'DM Sans', 'Inter', system-ui, sans-serif;
  --font-mono:    'JetBrains Mono', monospace;
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
  --leading-tight:   1.15;
  --leading-snug:    1.3;
  --leading-normal:  1.6;
  --leading-relaxed: 1.75;
  --leading-loose:   2;
  --tracking-tight:  -0.02em;
  --tracking-normal: 0;
  --tracking-wide:   0.03em;
  --tracking-wider:  0.06em;
  --tracking-caps:   0.1em;

  /* --- Spacing (generous, organic feel, base-4) --- */
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

  /* --- Border Radius (soft, organic) --- */
  --radius-none: 0;
  --radius-sm:   6px;
  --radius-md:   10px;
  --radius-lg:   16px;
  --radius-xl:   24px;
  --radius-2xl:  32px;
  --radius-organic: 40% 60% 55% 45% / 55% 40% 60% 45%;
  --radius-full: 9999px;

  /* --- Shadows (warm, soft) --- */
  --shadow-xs:  0 1px 2px oklch(0.30 0.02 55 / 0.06);
  --shadow-sm:  0 2px 4px oklch(0.30 0.02 55 / 0.08);
  --shadow-md:  0 4px 10px oklch(0.30 0.02 55 / 0.10);
  --shadow-lg:  0 8px 20px oklch(0.30 0.02 55 / 0.12);
  --shadow-xl:  0 16px 40px oklch(0.30 0.02 55 / 0.14);
  --shadow-card: 0 2px 8px oklch(0.30 0.02 55 / 0.06);

  /* --- Motion (natural, gentle) --- */
  --duration-instant:  50ms;
  --duration-fast:     120ms;
  --duration-normal:   250ms;
  --duration-moderate: 400ms;
  --duration-slow:     600ms;
  --duration-gentle:   900ms;
  --ease-out:     cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in:      cubic-bezier(0.64, 0, 0.78, 0);
  --ease-in-out:  cubic-bezier(0.45, 0, 0.55, 1);
  --ease-organic: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --ease-gentle:  cubic-bezier(0.4, 0, 0.2, 1);

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

### Syntax Highlighting Integration (Dev Tools Preset)
Apply syntax tokens to code blocks:
```css
.token-keyword  { color: var(--syntax-keyword); }
.token-string   { color: var(--syntax-string); }
.token-number   { color: var(--syntax-number); }
.token-function { color: var(--syntax-function); }
.token-comment  { color: var(--syntax-comment); font-style: italic; }
```

### Healthcare Accessibility Checklist
- All text must meet APCA Lc 60+ for body, Lc 75+ for small text
- Touch targets minimum 44px (WCAG 2.2 Level AA)
- Color must never be the only indicator of state
- Error states require icon + text + color
- Use `--leading-relaxed` for body text (1.75)

### Organic Border Radius (Sustainability Preset)
Apply the organic blob shape for hero sections:
```css
.hero-blob {
  border-radius: var(--radius-organic);
}
```

### Subject Color Mapping (Education Preset)
Assign colors per subject for consistent theming:
```css
[data-subject="math"]    { --subject-color: var(--color-math-500); --subject-bg: var(--color-math-100); }
[data-subject="science"] { --subject-color: var(--color-science-500); --subject-bg: var(--color-science-100); }
[data-subject="reading"] { --subject-color: var(--color-reading-500); --subject-bg: var(--color-reading-100); }
```

### Gamification Tokens (Education Preset)
Use reward tokens for achievement badges:
```css
.badge-gold   { background: var(--color-gold); }
.badge-silver { background: var(--color-silver); }
.badge-bronze { background: var(--color-bronze); }
.xp-bar       { background: var(--color-xp-green); }
.streak-fire  { color: var(--color-streak); }
```
