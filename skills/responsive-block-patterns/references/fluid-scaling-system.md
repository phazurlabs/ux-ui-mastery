# Fluid Scaling System — Complete Fluid Design System

A comprehensive system for fluid typography, spacing, sizing, and layout that eliminates hard breakpoint jumps and creates smooth, proportional scaling across all viewport widths.

---

## The Fluid Design Philosophy

Discrete breakpoints create visual "jumps" where elements snap from one size to another. Fluid design uses continuous mathematical functions so that typography, spacing, and sizing scale smoothly as the viewport changes. The primary tool is CSS `clamp()`, supported in all modern browsers.

The goal: define a minimum value, a maximum value, and let the browser calculate everything in between proportionally.

---

## The clamp() Master Formula

```
clamp(MIN, PREFERRED, MAX)
```

The browser uses MIN if PREFERRED would be smaller, MAX if PREFERRED would be larger, and PREFERRED otherwise.

### Calculating the Preferred Value

For a linear scale between two viewport widths:

```
PREFERRED = MIN_VALUE + (MAX_VALUE - MIN_VALUE) * ((100vw - MIN_VIEWPORT) / (MAX_VIEWPORT - MIN_VIEWPORT))
```

**Example:** Scale from 1rem (16px) at 320px viewport to 1.5rem (24px) at 1440px viewport.

```
Step 1: Convert viewports to rem (assuming 16px root)
  MIN_VIEWPORT = 320px = 20rem
  MAX_VIEWPORT = 1440px = 90rem

Step 2: Calculate slope
  slope = (1.5 - 1) / (90 - 20) = 0.5 / 70 = 0.007143

Step 3: Convert slope to vw
  slope_vw = 0.007143 * 100 = 0.7143vw

Step 4: Calculate intercept
  intercept = MIN_VALUE - (slope * MIN_VIEWPORT)
  intercept = 1 - (0.007143 * 20) = 1 - 0.1429 = 0.8571rem

Step 5: Assemble
  clamp(1rem, 0.8571rem + 0.7143vw, 1.5rem)
```

### Quick Reference Formula

For the common 320px to 1440px range:

```
clamp(MIN, (MIN - 0.1429 * (MAX - MIN))rem + (0.7143 * (MAX - MIN))vw, MAX)
```

Or more simply, when working in rem with a 320-1440 range:

```
clamp(MIN_REM, INTERCEPT_REM + SLOPE_VW, MAX_REM)
where:
  SLOPE = (MAX_REM - MIN_REM) / (90 - 20) * 100
  INTERCEPT = MIN_REM - (MAX_REM - MIN_REM) / (90 - 20) * 20
```

---

## Complete Fluid Type Scale

Based on a 1.2 (minor third) ratio at 320px scaling to a 1.25 (major third) ratio at 1440px. This creates a type scale that is more compressed on mobile (less contrast between sizes) and more expressive on desktop (greater contrast between sizes).

```css
:root {
  /* ============================================
     FLUID TYPE SCALE
     Base: 16px (320px) -> 20px (1440px)
     Ratio: 1.2 (mobile) -> 1.25 (desktop)
     Range: 320px (20rem) -> 1440px (90rem)
     ============================================ */

  /* -2: Extra Small — captions, labels, fine print */
  --text-xs:    clamp(0.6944rem, 0.6553rem + 0.1953vw, 0.8rem);
  /* 11.1px -> 12.8px */

  /* -1: Small — secondary text, metadata, helper text */
  --text-sm:    clamp(0.8333rem, 0.7754rem + 0.2896vw, 1rem);
  /* 13.3px -> 16px */

  /* 0: Base — body text, default reading size */
  --text-base:  clamp(1rem, 0.9107rem + 0.4464vw, 1.25rem);
  /* 16px -> 20px */

  /* 1: Medium — lead paragraphs, emphasized body */
  --text-md:    clamp(1.2rem, 1.0625rem + 0.6875vw, 1.5625rem);
  /* 19.2px -> 25px */

  /* 2: Large — card titles, section subtitles */
  --text-lg:    clamp(1.44rem, 1.2304rem + 1.0482vw, 1.9531rem);
  /* 23px -> 31.25px */

  /* 3: Extra Large — section headings */
  --text-xl:    clamp(1.728rem, 1.4107rem + 1.5866vw, 2.4414rem);
  /* 27.6px -> 39.06px */

  /* 4: 2XL — page headings */
  --text-2xl:   clamp(2.0736rem, 1.5964rem + 2.3857vw, 3.0518rem);
  /* 33.2px -> 48.83px */

  /* 5: 3XL — hero headings */
  --text-3xl:   clamp(2.4883rem, 1.7768rem + 3.5575vw, 3.8147rem);
  /* 39.8px -> 61.04px */

  /* 6: 4XL — display headings, hero text */
  --text-4xl:   clamp(2.986rem, 1.9357rem + 5.2513vw, 4.7684rem);
  /* 47.8px -> 76.29px */

  /* 7: 5XL — extra large display (billboards, landing pages) */
  --text-5xl:   clamp(3.5832rem, 2.0571rem + 7.6304vw, 5.9605rem);
  /* 57.3px -> 95.37px */
}
```

### Usage Mapping

| Token | Use Case | HTML Element |
|-------|----------|-------------|
| `--text-xs` | Captions, fine print, badges | `<small>`, `.caption` |
| `--text-sm` | Metadata, helper text, nav items | `<label>`, `.meta` |
| `--text-base` | Body text, paragraphs | `<p>`, `<li>` |
| `--text-md` | Lead paragraphs, card descriptions | `.lead`, `.subtitle` |
| `--text-lg` | Card titles, list headings | `<h4>`, `<h5>` |
| `--text-xl` | Section subtitles | `<h3>` |
| `--text-2xl` | Section headings | `<h2>` |
| `--text-3xl` | Page titles | `<h1>` |
| `--text-4xl` | Hero headings | `.hero-title` |
| `--text-5xl` | Display / billboard text | `.display` |

---

## Complete Fluid Space Scale

16 spacing tokens that scale fluidly. The scale uses a consistent ratio so that the relationship between spaces is preserved across all viewports.

```css
:root {
  /* ============================================
     FLUID SPACE SCALE
     Each token scales from mobile to desktop
     Range: 320px (20rem) -> 1440px (90rem)
     Ratio: mobile value * 1.5 = desktop value
     ============================================ */

  /* 3xs: 2px -> 3px */
  --space-3xs: clamp(0.125rem, 0.1027rem + 0.1116vw, 0.1875rem);

  /* 2xs: 4px -> 6px */
  --space-2xs: clamp(0.25rem, 0.2054rem + 0.2232vw, 0.375rem);

  /* xs: 8px -> 12px */
  --space-xs:  clamp(0.5rem, 0.4107rem + 0.4464vw, 0.75rem);

  /* sm: 12px -> 18px */
  --space-sm:  clamp(0.75rem, 0.6161rem + 0.6696vw, 1.125rem);

  /* md: 16px -> 24px */
  --space-md:  clamp(1rem, 0.8214rem + 0.8929vw, 1.5rem);

  /* lg: 20px -> 30px */
  --space-lg:  clamp(1.25rem, 1.0268rem + 1.1161vw, 1.875rem);

  /* xl: 24px -> 36px */
  --space-xl:  clamp(1.5rem, 1.2321rem + 1.3393vw, 2.25rem);

  /* 2xl: 32px -> 48px */
  --space-2xl: clamp(2rem, 1.6429rem + 1.7857vw, 3rem);

  /* 3xl: 40px -> 60px */
  --space-3xl: clamp(2.5rem, 2.0536rem + 2.2321vw, 3.75rem);

  /* 4xl: 48px -> 72px */
  --space-4xl: clamp(3rem, 2.4643rem + 2.6786vw, 4.5rem);

  /* 5xl: 64px -> 96px */
  --space-5xl: clamp(4rem, 3.2857rem + 3.5714vw, 6rem);

  /* 6xl: 80px -> 120px */
  --space-6xl: clamp(5rem, 4.1071rem + 4.4643vw, 7.5rem);

  /* 7xl: 96px -> 144px */
  --space-7xl: clamp(6rem, 4.9286rem + 5.3571vw, 9rem);

  /* 8xl: 128px -> 192px */
  --space-8xl: clamp(8rem, 6.5714rem + 7.1429vw, 12rem);

  /* 9xl: 160px -> 240px */
  --space-9xl: clamp(10rem, 8.2143rem + 8.9286vw, 15rem);

  /* 10xl: 192px -> 288px */
  --space-10xl: clamp(12rem, 9.8571rem + 10.7143vw, 18rem);
}
```

### One-Up Space Pairs (for larger jumps)

Sometimes you want a space that jumps from one token to the next higher token across the viewport range. These "one-up" pairs are useful for section padding where you want more dramatic scaling.

```css
:root {
  /* xs -> sm: 8px -> 18px */
  --space-xs-sm:  clamp(0.5rem, 0.3214rem + 0.8929vw, 1.125rem);

  /* sm -> md: 12px -> 24px */
  --space-sm-md:  clamp(0.75rem, 0.5268rem + 1.1161vw, 1.5rem);

  /* md -> lg: 16px -> 30px */
  --space-md-lg:  clamp(1rem, 0.7375rem + 1.3125vw, 1.875rem);

  /* lg -> xl: 20px -> 36px */
  --space-lg-xl:  clamp(1.25rem, 0.9518rem + 1.4911vw, 2.25rem);

  /* xl -> 2xl: 24px -> 48px */
  --space-xl-2xl: clamp(1.5rem, 1.0536rem + 2.2321vw, 3rem);

  /* 2xl -> 3xl: 32px -> 60px */
  --space-2xl-3xl: clamp(2rem, 1.4643rem + 2.6786vw, 3.75rem);

  /* 3xl -> 4xl: 40px -> 72px */
  --space-3xl-4xl: clamp(2.5rem, 1.875rem + 3.125vw, 4.5rem);
}
```

---

## Fluid Padding and Margin Recipes

### Section Padding

```css
/* Standard section padding */
.section {
  padding-block: var(--space-4xl);
  padding-inline: var(--space-md);
}

/* Hero section — more dramatic scaling */
.section--hero {
  padding-block: var(--space-5xl);
  padding-inline: var(--space-lg);
}

/* Compact section */
.section--compact {
  padding-block: var(--space-2xl);
  padding-inline: var(--space-md);
}
```

### Card Padding

```css
.card {
  padding: var(--space-md);
}

.card--large {
  padding: var(--space-xl);
}

.card--compact {
  padding: var(--space-sm);
}
```

### Container Padding

```css
.container {
  padding-inline: var(--space-md);
  max-width: 1200px;
  margin-inline: auto;
}

@media (min-width: 768px) {
  .container {
    padding-inline: var(--space-xl);
  }
}
```

### Stack Spacing (Vertical Rhythm)

```css
/* Content stack — consistent vertical spacing between elements */
.stack > * + * {
  margin-top: var(--space-md);
}

.stack--tight > * + * {
  margin-top: var(--space-sm);
}

.stack--loose > * + * {
  margin-top: var(--space-xl);
}
```

---

## Fluid Grid Gaps

```css
/* Auto-grid with fluid gaps */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr));
  gap: var(--space-md);
}

/* Tighter grid for image galleries */
.grid--tight {
  gap: var(--space-xs);
}

/* Looser grid for card layouts */
.grid--loose {
  gap: var(--space-xl);
}

/* Asymmetric gaps (wider row gap than column gap) */
.grid--asymmetric {
  row-gap: var(--space-xl);
  column-gap: var(--space-md);
}
```

---

## Modern Viewport Units Deep Dive

### The Problem with vh

`100vh` on mobile browsers includes the area behind the browser chrome (address bar, toolbar). This causes content to be hidden behind the UI, especially on iOS Safari.

### The Three Viewport Unit Types

```css
/* svh — Small Viewport Height
   The viewport height when ALL browser chrome is visible (address bar + toolbar).
   This is the smallest possible viewport. Use for elements that must always
   be fully visible without scrolling. */
.always-visible {
  max-height: 100svh;
}

/* lvh — Large Viewport Height
   The viewport height when browser chrome is HIDDEN (after scrolling down).
   This is the largest possible viewport. Use for full-screen backgrounds
   where you want no gap when chrome hides. */
.full-background {
  min-height: 100lvh;
}

/* dvh — Dynamic Viewport Height
   The CURRENT viewport height — changes in real-time as browser chrome
   shows/hides. Use for hero sections that should fill the visible area. */
.hero {
  min-height: 100dvh;
}
```

### Viewport Unit Comparison Table

| Unit | Description | When to Use |
|------|------------|-------------|
| `vh` | Legacy, inconsistent on mobile | Avoid |
| `svh` | Smallest viewport (chrome visible) | Dialogs, sticky containers |
| `lvh` | Largest viewport (chrome hidden) | Backgrounds, decorative fills |
| `dvh` | Dynamic (real-time) | Hero sections, app shells |
| `vw` | 1% of viewport width | Fluid calculations |
| `svw` / `lvw` / `dvw` | Width equivalents | Rare; vw is usually sufficient |
| `vi` | 1% of viewport inline size | Better for writing-mode support |
| `vb` | 1% of viewport block size | Better for writing-mode support |
| `svi` / `lvi` / `dvi` | Inline equivalents | When combining with logical properties |
| `svb` / `lvb` / `dvb` | Block equivalents | When combining with logical properties |

### Practical Viewport Unit Patterns

```css
/* Hero that fills exactly the visible viewport on mobile */
.hero {
  min-height: 100dvh;
  display: flex;
  align-items: center;
}

/* Sticky header that accounts for safe area */
.header {
  position: sticky;
  top: 0;
  height: clamp(3rem, 8svh, 5rem);
  padding-top: env(safe-area-inset-top);
}

/* Bottom navigation that avoids home indicator */
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding-bottom: env(safe-area-inset-bottom);
}

/* Modal that never exceeds the visible viewport */
.modal {
  max-height: 85svh;
  overflow-y: auto;
}

/* Full-page app that fills available height exactly */
.app-shell {
  height: 100dvh;
  display: grid;
  grid-template-rows: auto 1fr auto;
}
```

---

## Fluid Aspect Ratios

```css
/* Fixed aspect ratios */
.aspect-video    { aspect-ratio: 16 / 9; }
.aspect-square   { aspect-ratio: 1 / 1; }
.aspect-portrait { aspect-ratio: 3 / 4; }
.aspect-wide     { aspect-ratio: 21 / 9; }

/* Fluid aspect ratio: more square on mobile, wider on desktop */
.hero-image {
  aspect-ratio: 4 / 3;
}

@media (min-width: 768px) {
  .hero-image {
    aspect-ratio: 16 / 9;
  }
}

@media (min-width: 1280px) {
  .hero-image {
    aspect-ratio: 21 / 9;
  }
}
```

---

## Fluid Border Radius

Border radius should scale with the element and the viewport. A card with 8px radius looks right on mobile, but that same 8px on a 600px wide card on desktop looks too tight.

```css
:root {
  --radius-sm:   clamp(0.25rem, 0.2rem + 0.25vw, 0.5rem);    /* 4px -> 8px */
  --radius-md:   clamp(0.5rem, 0.375rem + 0.625vw, 0.75rem);  /* 8px -> 12px */
  --radius-lg:   clamp(0.75rem, 0.5rem + 1.25vw, 1rem);       /* 12px -> 16px */
  --radius-xl:   clamp(1rem, 0.625rem + 1.875vw, 1.5rem);     /* 16px -> 24px */
  --radius-2xl:  clamp(1.5rem, 0.875rem + 3.125vw, 2rem);     /* 24px -> 32px */
  --radius-full: 9999px;                                        /* Pill shape */
}
```

### Element-Specific Radius

```css
/* Cards: generous radius that scales */
.card { border-radius: var(--radius-lg); }

/* Buttons: consistent pill or medium radius */
.button { border-radius: var(--radius-md); }
.button--pill { border-radius: var(--radius-full); }

/* Inputs: subtle radius */
.input { border-radius: var(--radius-sm); }

/* Modals: large radius on top (mobile bottom sheet) */
.modal {
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
}

@media (min-width: 768px) {
  .modal {
    border-radius: var(--radius-xl);
  }
}

/* Avatars: always circular */
.avatar { border-radius: var(--radius-full); }
```

---

## The Utopia Calculation Method

Utopia (utopia.fyi) popularized the systematic approach to fluid type and space. Here is the method explained for custom implementation.

### Step 1: Define Your Range

```
Viewport min: 320px (20rem)
Viewport max: 1440px (90rem)
```

### Step 2: Define Min and Max Type Sizes

```
Base font min: 16px (1rem)
Base font max: 20px (1.25rem)

Type scale min ratio: 1.2 (minor third)
Type scale max ratio: 1.25 (major third)
```

### Step 3: Generate Each Step

For step N:

```
min_size = base_min * (ratio_min ^ N)
max_size = base_max * (ratio_max ^ N)
```

Example for step 3 (text-xl):

```
min_size = 1rem * 1.2^3 = 1.728rem (27.6px)
max_size = 1.25rem * 1.25^3 = 2.4414rem (39.06px)
```

### Step 4: Calculate clamp() Values

```
slope = (max_size - min_size) / (max_viewport_rem - min_viewport_rem)
intercept = min_size - slope * min_viewport_rem
vw_value = slope * 100

Result: clamp(min_size, intercept + vw_value, max_size)
```

For text-xl:
```
slope = (2.4414 - 1.728) / (90 - 20) = 0.01019
intercept = 1.728 - 0.01019 * 20 = 1.5241
vw_value = 0.01019 * 100 = 1.019

Result: clamp(1.728rem, 1.5241rem + 1.019vw, 2.4414rem)
```

### Step 5: Apply Same Method to Spacing

Space tokens follow the same principle, typically using a simpler ratio (often 1.5x between mobile and desktop).

---

## Custom Fluid Scale Generator

A CSS-only approach to generating fluid values dynamically using custom properties and calculations.

```css
:root {
  /* Configuration */
  --fluid-min-viewport: 20;  /* 320px in rem */
  --fluid-max-viewport: 90;  /* 1440px in rem */
  --fluid-range: calc(var(--fluid-max-viewport) - var(--fluid-min-viewport));

  /* Base sizes */
  --fluid-base-min: 1;       /* 16px in rem */
  --fluid-base-max: 1.25;    /* 20px in rem */

  /* Scale ratios */
  --fluid-ratio-min: 1.2;
  --fluid-ratio-max: 1.25;
}

/* Utility: generate a single fluid value */
/* Unfortunately, CSS cannot do exponentiation natively,
   so each step must be pre-calculated or use this approximation: */

/* For a fluid value from MIN to MAX: */
/* clamp(MIN_REM, CALC_REM + CALC_VW, MAX_REM) */

/* Helper mixin (for CSS preprocessors or PostCSS): */
/*
  @define-mixin fluid($min-px, $max-px) {
    $min-rem: calc($min-px / 16);
    $max-rem: calc($max-px / 16);
    $slope: calc(($max-rem - $min-rem) / (90 - 20));
    $intercept: calc($min-rem - $slope * 20);
    $vw: calc($slope * 100);
    font-size: clamp(#{$min-rem}rem, #{$intercept}rem + #{$vw}vw, #{$max-rem}rem);
  }
*/
```

### JavaScript Fluid Value Generator

```javascript
/**
 * Generate a CSS clamp() value for fluid scaling.
 * @param {number} minPx - Minimum size in pixels
 * @param {number} maxPx - Maximum size in pixels
 * @param {number} minVw - Minimum viewport width in pixels (default 320)
 * @param {number} maxVw - Maximum viewport width in pixels (default 1440)
 * @returns {string} CSS clamp() value
 */
function fluidClamp(minPx, maxPx, minVw = 320, maxVw = 1440) {
  const minRem = minPx / 16;
  const maxRem = maxPx / 16;
  const minVwRem = minVw / 16;
  const maxVwRem = maxVw / 16;

  const slope = (maxRem - minRem) / (maxVwRem - minVwRem);
  const intercept = minRem - slope * minVwRem;
  const slopeVw = slope * 100;

  const interceptRounded = Math.round(intercept * 10000) / 10000;
  const slopeVwRounded = Math.round(slopeVw * 10000) / 10000;

  return `clamp(${minRem}rem, ${interceptRounded}rem + ${slopeVwRounded}vw, ${maxRem}rem)`;
}

// Usage:
// fluidClamp(16, 24)  => "clamp(1rem, 0.8571rem + 0.7143vw, 1.5rem)"
// fluidClamp(24, 48)  => "clamp(1.5rem, 1.0714rem + 2.1429vw, 3rem)"
// fluidClamp(8, 16)   => "clamp(0.5rem, 0.3571rem + 0.7143vw, 1rem)"
```

### Sass/SCSS Fluid Mixin

```scss
@function fluid($min-px, $max-px, $min-vw: 320px, $max-vw: 1440px) {
  $min-rem: calc($min-px / 16px) * 1rem;
  $max-rem: calc($max-px / 16px) * 1rem;
  $min-vw-rem: calc($min-vw / 16px);
  $max-vw-rem: calc($max-vw / 16px);

  $slope: calc(($max-rem - $min-rem) / ($max-vw-rem - $min-vw-rem));
  $intercept: $min-rem - $slope * $min-vw-rem * 1rem;
  $slope-vw: $slope * 100;

  @return clamp(#{$min-rem}, #{$intercept} + #{$slope-vw}vw, #{$max-rem});
}

// Usage:
// font-size: fluid(16px, 24px);
// padding: fluid(12px, 32px);
// gap: fluid(8px, 24px);
```

---

## Complete Fluid CSS Custom Property System

A production-ready set of custom properties combining fluid type, space, and sizing.

```css
:root {
  /* ============================================
     FLUID DESIGN SYSTEM
     Viewport range: 320px <-> 1440px
     ============================================ */

  /* --- Typography --- */
  --font-size-xs:    clamp(0.6944rem, 0.6553rem + 0.1953vw, 0.8rem);
  --font-size-sm:    clamp(0.8333rem, 0.7754rem + 0.2896vw, 1rem);
  --font-size-base:  clamp(1rem, 0.9107rem + 0.4464vw, 1.25rem);
  --font-size-md:    clamp(1.2rem, 1.0625rem + 0.6875vw, 1.5625rem);
  --font-size-lg:    clamp(1.44rem, 1.2304rem + 1.0482vw, 1.9531rem);
  --font-size-xl:    clamp(1.728rem, 1.4107rem + 1.5866vw, 2.4414rem);
  --font-size-2xl:   clamp(2.0736rem, 1.5964rem + 2.3857vw, 3.0518rem);
  --font-size-3xl:   clamp(2.4883rem, 1.7768rem + 3.5575vw, 3.8147rem);
  --font-size-4xl:   clamp(2.986rem, 1.9357rem + 5.2513vw, 4.7684rem);

  /* --- Line Heights (decrease as size increases) --- */
  --line-height-xs:   1.6;
  --line-height-sm:   1.55;
  --line-height-base: 1.5;
  --line-height-md:   1.4;
  --line-height-lg:   1.3;
  --line-height-xl:   1.2;
  --line-height-2xl:  1.15;
  --line-height-3xl:  1.1;
  --line-height-4xl:  1.05;

  /* --- Letter Spacing (tighten as size increases) --- */
  --tracking-xs:    0.02em;
  --tracking-sm:    0.01em;
  --tracking-base:  0em;
  --tracking-md:   -0.005em;
  --tracking-lg:   -0.01em;
  --tracking-xl:   -0.015em;
  --tracking-2xl:  -0.02em;
  --tracking-3xl:  -0.025em;
  --tracking-4xl:  -0.03em;

  /* --- Spacing --- */
  --space-3xs: clamp(0.125rem, 0.1027rem + 0.1116vw, 0.1875rem);
  --space-2xs: clamp(0.25rem, 0.2054rem + 0.2232vw, 0.375rem);
  --space-xs:  clamp(0.5rem, 0.4107rem + 0.4464vw, 0.75rem);
  --space-sm:  clamp(0.75rem, 0.6161rem + 0.6696vw, 1.125rem);
  --space-md:  clamp(1rem, 0.8214rem + 0.8929vw, 1.5rem);
  --space-lg:  clamp(1.25rem, 1.0268rem + 1.1161vw, 1.875rem);
  --space-xl:  clamp(1.5rem, 1.2321rem + 1.3393vw, 2.25rem);
  --space-2xl: clamp(2rem, 1.6429rem + 1.7857vw, 3rem);
  --space-3xl: clamp(2.5rem, 2.0536rem + 2.2321vw, 3.75rem);
  --space-4xl: clamp(3rem, 2.4643rem + 2.6786vw, 4.5rem);
  --space-5xl: clamp(4rem, 3.2857rem + 3.5714vw, 6rem);
  --space-6xl: clamp(5rem, 4.1071rem + 4.4643vw, 7.5rem);

  /* --- Border Radius --- */
  --radius-sm:   clamp(0.25rem, 0.2rem + 0.25vw, 0.5rem);
  --radius-md:   clamp(0.5rem, 0.375rem + 0.625vw, 0.75rem);
  --radius-lg:   clamp(0.75rem, 0.5rem + 1.25vw, 1rem);
  --radius-xl:   clamp(1rem, 0.625rem + 1.875vw, 1.5rem);
  --radius-full: 9999px;

  /* --- Max Widths --- */
  --max-width-prose: 65ch;
  --max-width-content: min(1200px, calc(100vw - var(--space-xl) * 2));
  --max-width-wide: min(1440px, calc(100vw - var(--space-md) * 2));
  --max-width-full: 100%;

  /* --- Content Width (readable line length) --- */
  --content-width: clamp(16rem, 60vw, 40rem);
}
```

### Using the System

```css
/* Typography */
h1 {
  font-size: var(--font-size-3xl);
  line-height: var(--line-height-3xl);
  letter-spacing: var(--tracking-3xl);
}

h2 {
  font-size: var(--font-size-2xl);
  line-height: var(--line-height-2xl);
  letter-spacing: var(--tracking-2xl);
}

p {
  font-size: var(--font-size-base);
  line-height: var(--line-height-base);
  max-width: var(--max-width-prose);
}

/* Layout */
.section {
  padding-block: var(--space-5xl);
  padding-inline: var(--space-md);
}

.section__content {
  max-width: var(--max-width-content);
  margin-inline: auto;
}

/* Components */
.card {
  padding: var(--space-md);
  border-radius: var(--radius-lg);
  gap: var(--space-sm);
}

.button {
  padding: var(--space-xs) var(--space-md);
  border-radius: var(--radius-md);
  font-size: var(--font-size-sm);
}
```

---

## Fluid Sizing Utilities

### Fluid Width Constraints

```css
/* Fluid minimum width that scales with viewport */
.sidebar {
  width: clamp(200px, 25vw, 320px);
}

/* Fluid max-width for reading content */
.prose {
  max-width: clamp(28rem, 50vw + 10rem, 40rem);
}
```

### Fluid Icon Sizing

```css
:root {
  --icon-sm: clamp(1rem, 0.875rem + 0.625vw, 1.25rem);     /* 16px -> 20px */
  --icon-md: clamp(1.25rem, 1.0625rem + 0.9375vw, 1.5rem);  /* 20px -> 24px */
  --icon-lg: clamp(1.5rem, 1.25rem + 1.25vw, 2rem);          /* 24px -> 32px */
  --icon-xl: clamp(2rem, 1.5rem + 2.5vw, 3rem);              /* 32px -> 48px */
}
```

### Fluid Touch Target Sizing

```css
/* Minimum touch target that respects platform guidelines */
.touch-target {
  min-width: clamp(44px, 5vw, 48px);
  min-height: clamp(44px, 5vw, 48px);
}
```

---

## Testing Fluid Values

### Browser DevTools Method

1. Open DevTools, toggle device toolbar
2. Set responsive mode
3. Slowly drag the viewport width from 320px to 1440px
4. Watch computed values in the Styles panel — they should change smoothly
5. Verify: no value goes below the clamp minimum or above the maximum

### Automated Visual Regression

Take screenshots at 320, 480, 768, 1024, 1280, 1440, and 1920px. Compare each pair for proportional relationships — spacing should feel "right" at every width, not just the endpoints.
