# Type Scale Systems — Complete Implementation Guide

> Modular scale theory, 12 complete type scale recipes with CSS custom properties, line-height rules, letter-spacing adjustments, paragraph width guidelines, and responsive scaling strategies.

---

## Type Scale Theory

### What Is a Modular Scale?

A modular scale is a sequence of numbers that relate to one another through a consistent ratio. In typography, you start with a base size (typically 16px / 1rem) and multiply or divide by the ratio to generate every size in your system.

```
size = base * ratio^n
```

Where `n` is the step number (positive for larger, negative for smaller).

### The Classic Ratios

| Ratio | Name | Value | Character | Best For |
|-------|------|-------|-----------|----------|
| 1.067 | Minor Second | 1.067 | Barely noticeable steps. Ultra-subtle. | Dense data UIs, dashboards |
| 1.125 | Major Second | 1.125 | Gentle progression. Restrained. | Admin panels, documentation |
| 1.200 | Minor Third | 1.200 | Balanced, versatile. The workhorse. | SaaS apps, general web |
| 1.250 | Major Third | 1.250 | Clear hierarchy. Confident. | Marketing sites, blogs |
| 1.333 | Perfect Fourth | 1.333 | Strong contrast. Dramatic. | Editorial, landing pages |
| 1.414 | Augmented Fourth | 1.414 | Mathematical elegance (sqrt of 2). | Design portfolios, creative |
| 1.500 | Perfect Fifth | 1.500 | Very dramatic jumps. High impact. | Hero-heavy marketing |
| 1.618 | Golden Ratio | 1.618 | Classical proportion. Maximum drama. | Art, luxury, special occasions |

### Choosing Your Ratio

**Rule of thumb**: The more content-dense your UI, the smaller your ratio should be.

- **Data-heavy dashboards**: 1.067-1.125 (minor/major second)
- **SaaS applications**: 1.125-1.200 (major second/minor third)
- **Content sites/blogs**: 1.200-1.250 (minor/major third)
- **Marketing/landing**: 1.250-1.333 (major third/perfect fourth)
- **Editorial/luxury**: 1.333-1.500 (perfect fourth/perfect fifth)
- **Hero-driven single pages**: 1.500-1.618 (perfect fifth/golden ratio)

### Scale Generation Formula

Given base = 16px and ratio = 1.250 (Major Third):

```
Step -2: 16 / 1.250^2 = 10.24px  (0.64rem)
Step -1: 16 / 1.250   = 12.80px  (0.80rem)
Step  0: 16            = 16.00px  (1.00rem)  ← base
Step  1: 16 * 1.250    = 20.00px  (1.25rem)
Step  2: 16 * 1.250^2  = 25.00px  (1.563rem)
Step  3: 16 * 1.250^3  = 31.25px  (1.953rem)
Step  4: 16 * 1.250^4  = 39.06px  (2.441rem)
Step  5: 16 * 1.250^5  = 48.83px  (3.052rem)
Step  6: 16 * 1.250^6  = 61.04px  (3.815rem)
```

---

## Complete Type Scale Recipes

### Recipe 1: Minimal App Scale (Minor Third 1.2)

Tight, restrained scale for UI-heavy applications.

```css
:root {
  /* Type Scale — Minor Third (1.200) */
  --font-size-2xs: 0.694rem;   /* 11.1px — fine print, timestamps */
  --font-size-xs: 0.833rem;    /* 13.3px — captions, labels */
  --font-size-sm: 0.875rem;    /* 14px — secondary text, metadata */
  --font-size-base: 1rem;      /* 16px — body text */
  --font-size-md: 1.2rem;      /* 19.2px — large body, card titles */
  --font-size-lg: 1.44rem;     /* 23px — section headings (h3) */
  --font-size-xl: 1.728rem;    /* 27.6px — page headings (h2) */
  --font-size-2xl: 2.074rem;   /* 33.2px — page title (h1) */

  /* Line Heights */
  --leading-tight: 1.1;
  --leading-snug: 1.3;
  --leading-normal: 1.5;
  --leading-relaxed: 1.6;

  /* Letter Spacing */
  --tracking-tighter: -0.02em;
  --tracking-tight: -0.01em;
  --tracking-normal: 0;
  --tracking-wide: 0.01em;
  --tracking-wider: 0.05em;

  /* Paragraph Width */
  --measure-narrow: 45ch;
  --measure-base: 65ch;
  --measure-wide: 80ch;
}

/* Application */
body {
  font-size: var(--font-size-base);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
}

h1 {
  font-size: var(--font-size-2xl);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tighter);
}

h2 {
  font-size: var(--font-size-xl);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
}

h3 {
  font-size: var(--font-size-lg);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
}

.caption {
  font-size: var(--font-size-xs);
  line-height: var(--leading-relaxed);
  letter-spacing: var(--tracking-wide);
}

p {
  max-width: var(--measure-base);
}
```

### Recipe 2: Marketing Page Scale (Major Third 1.25)

Confident hierarchy for marketing and content sites.

```css
:root {
  /* Type Scale — Major Third (1.250) */
  --font-size-xs: 0.8rem;      /* 12.8px — fine print */
  --font-size-sm: 0.875rem;    /* 14px — captions, labels */
  --font-size-base: 1rem;      /* 16px — body text */
  --font-size-md: 1.25rem;     /* 20px — large body, intro text */
  --font-size-lg: 1.563rem;    /* 25px — h4 */
  --font-size-xl: 1.953rem;    /* 31.3px — h3 */
  --font-size-2xl: 2.441rem;   /* 39px — h2 */
  --font-size-3xl: 3.052rem;   /* 48.8px — h1 */
  --font-size-4xl: 3.815rem;   /* 61px — hero headline */

  /* Line Heights */
  --leading-none: 1.0;
  --leading-tight: 1.1;
  --leading-snug: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 1.75;

  /* Letter Spacing */
  --tracking-tightest: -0.04em;
  --tracking-tighter: -0.02em;
  --tracking-tight: -0.01em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;

  /* Paragraph Width */
  --measure-narrow: 45ch;
  --measure-base: 65ch;
  --measure-wide: 75ch;
}

/* Heading Styles */
.hero-headline {
  font-size: var(--font-size-4xl);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-tightest);
  max-width: 20ch;
}

h1 {
  font-size: var(--font-size-3xl);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tighter);
}

h2 {
  font-size: var(--font-size-2xl);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tighter);
}

h3 {
  font-size: var(--font-size-xl);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
}

h4 {
  font-size: var(--font-size-lg);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
}

/* Body Styles */
.lead {
  font-size: var(--font-size-md);
  line-height: var(--leading-relaxed);
  max-width: var(--measure-wide);
}

body {
  font-size: var(--font-size-base);
  line-height: var(--leading-normal);
}

p {
  max-width: var(--measure-base);
}

.overline {
  font-size: var(--font-size-sm);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  font-weight: 600;
}
```

### Recipe 3: Dashboard Scale (Major Second 1.125)

Dense, efficient scale for data-heavy interfaces.

```css
:root {
  /* Type Scale — Major Second (1.125) */
  --font-size-3xs: 0.702rem;   /* 11.2px — sparkline labels */
  --font-size-2xs: 0.79rem;    /* 12.6px — table cell data */
  --font-size-xs: 0.889rem;    /* 14.2px — secondary labels */
  --font-size-sm: 0.937rem;    /* 15px — body small */
  --font-size-base: 1rem;      /* 16px — body text */
  --font-size-md: 1.125rem;    /* 18px — card titles */
  --font-size-lg: 1.266rem;    /* 20.3px — section headings */
  --font-size-xl: 1.424rem;    /* 22.8px — page headings */
  --font-size-2xl: 1.602rem;   /* 25.6px — dashboard title */
  --font-size-3xl: 1.802rem;   /* 28.8px — KPI numbers */

  /* Dense Line Heights */
  --leading-compressed: 1.0;
  --leading-tight: 1.2;
  --leading-normal: 1.4;
  --leading-relaxed: 1.5;

  /* Tabular Number Settings */
  --font-feature-tabular: "tnum" 1;
}

/* KPI / Metric Display */
.kpi-value {
  font-size: var(--font-size-3xl);
  line-height: var(--leading-compressed);
  font-feature-settings: var(--font-feature-tabular);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
  font-weight: 700;
}

.kpi-label {
  font-size: var(--font-size-xs);
  line-height: var(--leading-normal);
  letter-spacing: 0.05em;
  text-transform: uppercase;
  font-weight: 500;
  color: var(--color-text-secondary);
}

/* Table Typography */
.table-header {
  font-size: var(--font-size-xs);
  line-height: var(--leading-tight);
  letter-spacing: 0.03em;
  text-transform: uppercase;
  font-weight: 600;
}

.table-cell {
  font-size: var(--font-size-2xs);
  line-height: var(--leading-normal);
  font-variant-numeric: tabular-nums;
}

/* Dashboard Headings */
.dashboard-title {
  font-size: var(--font-size-2xl);
  line-height: var(--leading-tight);
  font-weight: 700;
}

.section-title {
  font-size: var(--font-size-lg);
  line-height: var(--leading-tight);
  font-weight: 600;
}

.card-title {
  font-size: var(--font-size-md);
  line-height: var(--leading-tight);
  font-weight: 600;
}
```

### Recipe 4: Documentation Scale (Minor Third 1.2)

Optimized for long-form reading with clear hierarchy.

```css
:root {
  /* Type Scale — Minor Third (1.200) */
  --font-size-xs: 0.833rem;    /* 13.3px — footnotes */
  --font-size-sm: 0.875rem;    /* 14px — captions, sidenotes */
  --font-size-base: 1rem;      /* 16px — body text */
  --font-size-md: 1.125rem;    /* 18px — lead paragraphs */
  --font-size-lg: 1.2rem;      /* 19.2px — h4 */
  --font-size-xl: 1.44rem;     /* 23px — h3 */
  --font-size-2xl: 1.728rem;   /* 27.6px — h2 */
  --font-size-3xl: 2.074rem;   /* 33.2px — h1 */
  --font-size-4xl: 2.488rem;   /* 39.8px — page title */

  /* Reading-Optimized Line Heights */
  --leading-code: 1.6;
  --leading-body: 1.7;
  --leading-heading: 1.25;
  --leading-title: 1.1;

  /* Reading Width */
  --measure-content: 70ch;
  --measure-code: 80ch;
  --measure-wide: 90ch;
}

/* Document Structure */
.doc-title {
  font-size: var(--font-size-4xl);
  line-height: var(--leading-title);
  letter-spacing: -0.02em;
  font-weight: 800;
  margin-bottom: 0.5em;
}

.doc-description {
  font-size: var(--font-size-md);
  line-height: var(--leading-body);
  color: var(--color-text-secondary);
  max-width: var(--measure-content);
}

article h1 {
  font-size: var(--font-size-3xl);
  line-height: var(--leading-heading);
  letter-spacing: -0.015em;
  font-weight: 700;
  margin-top: 2em;
  margin-bottom: 0.5em;
}

article h2 {
  font-size: var(--font-size-2xl);
  line-height: var(--leading-heading);
  letter-spacing: -0.01em;
  font-weight: 700;
  margin-top: 1.75em;
  margin-bottom: 0.5em;
}

article h3 {
  font-size: var(--font-size-xl);
  line-height: var(--leading-heading);
  font-weight: 600;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
}

article h4 {
  font-size: var(--font-size-lg);
  line-height: var(--leading-heading);
  font-weight: 600;
  margin-top: 1.25em;
  margin-bottom: 0.25em;
}

article p {
  font-size: var(--font-size-base);
  line-height: var(--leading-body);
  max-width: var(--measure-content);
  margin-bottom: 1.25em;
}

/* Code Blocks */
pre, code {
  font-size: 0.9em;
  line-height: var(--leading-code);
}

pre {
  max-width: var(--measure-code);
}

/* Sidebar / TOC */
.toc-item {
  font-size: var(--font-size-sm);
  line-height: 1.4;
}
```

### Recipe 5: Mobile-First Scale (Custom Progressive)

Starts small on mobile, expands on larger screens.

```css
:root {
  /* Mobile Base (320-767px) */
  --font-size-xs: 0.75rem;     /* 12px */
  --font-size-sm: 0.875rem;    /* 14px */
  --font-size-base: 1rem;      /* 16px */
  --font-size-md: 1.125rem;    /* 18px */
  --font-size-lg: 1.25rem;     /* 20px */
  --font-size-xl: 1.5rem;      /* 24px */
  --font-size-2xl: 1.875rem;   /* 30px */
  --font-size-3xl: 2.25rem;    /* 36px */
}

/* Tablet (768px+) */
@media (min-width: 48rem) {
  :root {
    --font-size-base: 1rem;      /* 16px — unchanged */
    --font-size-md: 1.25rem;     /* 20px */
    --font-size-lg: 1.5rem;      /* 24px */
    --font-size-xl: 1.875rem;    /* 30px */
    --font-size-2xl: 2.25rem;    /* 36px */
    --font-size-3xl: 3rem;       /* 48px */
  }
}

/* Desktop (1024px+) */
@media (min-width: 64rem) {
  :root {
    --font-size-md: 1.25rem;     /* 20px */
    --font-size-lg: 1.5rem;      /* 24px */
    --font-size-xl: 2rem;        /* 32px */
    --font-size-2xl: 2.5rem;     /* 40px */
    --font-size-3xl: 3.5rem;     /* 56px */
  }
}

/* Large Desktop (1440px+) */
@media (min-width: 90rem) {
  :root {
    --font-size-xl: 2.25rem;     /* 36px */
    --font-size-2xl: 3rem;       /* 48px */
    --font-size-3xl: 4rem;       /* 64px */
  }
}

/* Mobile-Specific Adjustments */
@media (max-width: 47.999rem) {
  body {
    /* Slightly increase base line-height on mobile for thumb-scrolling readability */
    line-height: 1.6;
  }

  h1, h2, h3 {
    /* Prevent orphans in narrow columns */
    text-wrap: balance;
  }

  p {
    /* Shorter measure on mobile */
    max-width: 100%;
  }
}
```

### Recipe 6: Fluid Typography Scale (clamp-based)

Zero breakpoints. Smooth scaling from mobile to desktop.

```css
:root {
  /* Fluid Type Scale — No Breakpoints
     Formula: clamp(min, preferred, max)
     Preferred uses viewport width: minSize + (maxSize - minSize) * ((100vw - minViewport) / (maxViewport - minViewport))
     Simplified to: clamp(min, calc(base + vw-factor), max)
  */

  --font-size-xs: clamp(0.75rem, 0.7rem + 0.15vw, 0.875rem);
  /* 12px → 14px */

  --font-size-sm: clamp(0.875rem, 0.83rem + 0.2vw, 1rem);
  /* 14px → 16px */

  --font-size-base: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  /* 16px → 18px */

  --font-size-md: clamp(1.125rem, 1rem + 0.5vw, 1.375rem);
  /* 18px → 22px */

  --font-size-lg: clamp(1.25rem, 1rem + 1vw, 1.75rem);
  /* 20px → 28px */

  --font-size-xl: clamp(1.5rem, 1rem + 1.5vw, 2.25rem);
  /* 24px → 36px */

  --font-size-2xl: clamp(1.875rem, 1rem + 2.5vw, 3rem);
  /* 30px → 48px */

  --font-size-3xl: clamp(2.25rem, 1rem + 3.5vw, 4rem);
  /* 36px → 64px */

  --font-size-display: clamp(2.75rem, 0.5rem + 5vw, 5.5rem);
  /* 44px → 88px */

  /* Fluid Line Heights (tighter as size grows) */
  --leading-body: 1.5;
  --leading-md: 1.4;
  --leading-lg: 1.3;
  --leading-xl: 1.2;
  --leading-2xl: 1.15;
  --leading-3xl: 1.1;
  --leading-display: 1.05;

  /* Fluid Spacing (tied to type scale) */
  --space-text-flow: clamp(1rem, 0.75rem + 0.5vw, 1.5rem);
  --space-section: clamp(2rem, 1rem + 3vw, 6rem);
}

/* Application */
body {
  font-size: var(--font-size-base);
  line-height: var(--leading-body);
}

h1 {
  font-size: var(--font-size-3xl);
  line-height: var(--leading-3xl);
  letter-spacing: -0.02em;
}

h2 {
  font-size: var(--font-size-2xl);
  line-height: var(--leading-2xl);
  letter-spacing: -0.015em;
}

h3 {
  font-size: var(--font-size-xl);
  line-height: var(--leading-xl);
  letter-spacing: -0.01em;
}

.hero-text {
  font-size: var(--font-size-display);
  line-height: var(--leading-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

p + p {
  margin-top: var(--space-text-flow);
}

section + section {
  margin-top: var(--space-section);
}
```

### Recipe 7: Editorial/Magazine Scale (Perfect Fourth 1.333)

Dramatic hierarchy for editorial content.

```css
:root {
  /* Type Scale — Perfect Fourth (1.333) */
  --font-size-xs: 0.75rem;     /* 12px — datelines */
  --font-size-sm: 0.875rem;    /* 14px — bylines, captions */
  --font-size-base: 1.0625rem; /* 17px — body (slightly larger for serifs) */
  --font-size-md: 1.333rem;    /* 21.3px — lead paragraph */
  --font-size-lg: 1.777rem;    /* 28.4px — subheading */
  --font-size-xl: 2.369rem;    /* 37.9px — section heading */
  --font-size-2xl: 3.157rem;   /* 50.5px — article headline */
  --font-size-3xl: 4.209rem;   /* 67.3px — cover headline */
  --font-size-display: 5.61rem; /* 89.8px — display headline */

  /* Serif Body Line Height */
  --leading-body: 1.65;
  --leading-heading: 1.15;
  --leading-display: 1.0;

  /* Editorial Widths */
  --measure-article: 36em;  /* ~65 characters for serif body */
  --measure-caption: 30ch;
  --measure-headline: 25ch;
}

/* Editorial Styles */
.cover-headline {
  font-size: var(--font-size-3xl);
  line-height: var(--leading-display);
  letter-spacing: -0.03em;
  font-weight: 700;
  text-wrap: balance;
  max-width: var(--measure-headline);
}

.article-headline {
  font-size: var(--font-size-2xl);
  line-height: var(--leading-heading);
  letter-spacing: -0.025em;
  font-weight: 700;
  margin-bottom: 0.3em;
}

.article-deck {
  font-size: var(--font-size-md);
  line-height: 1.4;
  font-weight: 400;
  color: var(--color-text-secondary);
  font-style: italic;
  margin-bottom: 2em;
}

.byline {
  font-size: var(--font-size-sm);
  line-height: 1.4;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  font-weight: 600;
}

.drop-cap::first-letter {
  font-size: 3.5em;
  float: left;
  line-height: 0.8;
  padding-right: 0.1em;
  font-weight: 700;
}

article p {
  font-size: var(--font-size-base);
  line-height: var(--leading-body);
  max-width: var(--measure-article);
  margin-bottom: 1.5em;
  hanging-punctuation: first last;
}

.caption {
  font-size: var(--font-size-sm);
  line-height: 1.4;
  max-width: var(--measure-caption);
  color: var(--color-text-tertiary);
}
```

### Recipe 8: Landing Page / Hero Scale (Perfect Fifth 1.5)

Maximum drama for conversion-focused pages.

```css
:root {
  /* Type Scale — Perfect Fifth (1.500) */
  --font-size-sm: 0.875rem;     /* 14px */
  --font-size-base: 1rem;       /* 16px */
  --font-size-md: 1.125rem;     /* 18px */
  --font-size-lg: 1.5rem;       /* 24px */
  --font-size-xl: 2.25rem;      /* 36px */
  --font-size-2xl: 3.375rem;    /* 54px */
  --font-size-3xl: 5.063rem;    /* 81px */
  --font-size-display: 7.594rem; /* 121.5px */

  /* Impact Line Heights */
  --leading-display: 0.95;
  --leading-hero: 1.0;
  --leading-heading: 1.1;
  --leading-body: 1.5;
}

/* Hero Section */
.hero-headline {
  font-size: var(--font-size-display);
  line-height: var(--leading-display);
  letter-spacing: -0.04em;
  font-weight: 800;
  text-wrap: balance;
}

.hero-subheadline {
  font-size: var(--font-size-xl);
  line-height: var(--leading-heading);
  letter-spacing: -0.01em;
  font-weight: 400;
  color: var(--color-text-secondary);
  max-width: 50ch;
}

/* Section Headlines */
.section-headline {
  font-size: var(--font-size-2xl);
  line-height: var(--leading-hero);
  letter-spacing: -0.03em;
  font-weight: 700;
  text-wrap: balance;
}

.section-description {
  font-size: var(--font-size-md);
  line-height: var(--leading-body);
  max-width: 65ch;
}

/* CTA */
.cta-text {
  font-size: var(--font-size-lg);
  line-height: var(--leading-heading);
  font-weight: 600;
}

/* Mobile Override — Reduce Drama */
@media (max-width: 47.999rem) {
  :root {
    --font-size-display: 3rem;
    --font-size-3xl: 2.5rem;
    --font-size-2xl: 2rem;
    --font-size-xl: 1.5rem;
  }
}
```

### Recipe 9: Design System Token Scale (Tailwind-Compatible)

Maps to Tailwind CSS naming conventions.

```css
:root {
  /* Tailwind-Compatible Type Tokens */
  --text-xs: 0.75rem;      /* 12px */
  --text-sm: 0.875rem;     /* 14px */
  --text-base: 1rem;       /* 16px */
  --text-lg: 1.125rem;     /* 18px */
  --text-xl: 1.25rem;      /* 20px */
  --text-2xl: 1.5rem;      /* 24px */
  --text-3xl: 1.875rem;    /* 30px */
  --text-4xl: 2.25rem;     /* 36px */
  --text-5xl: 3rem;        /* 48px */
  --text-6xl: 3.75rem;     /* 60px */
  --text-7xl: 4.5rem;      /* 72px */
  --text-8xl: 6rem;        /* 96px */
  --text-9xl: 8rem;        /* 128px */

  /* Matching Line Heights */
  --leading-3: 0.75rem;    /* 12px */
  --leading-4: 1rem;       /* 16px */
  --leading-5: 1.25rem;    /* 20px */
  --leading-6: 1.5rem;     /* 24px */
  --leading-7: 1.75rem;    /* 28px */
  --leading-8: 2rem;       /* 32px */
  --leading-9: 2.25rem;    /* 36px */
  --leading-10: 2.5rem;    /* 40px */
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;

  /* Matching Letter Spacing */
  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;

  /* Font Weights */
  --font-thin: 100;
  --font-extralight: 200;
  --font-light: 300;
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  --font-extrabold: 800;
  --font-black: 900;
}
```

### Recipe 10: Compact/Dense UI Scale (Minor Second 1.067)

Ultra-tight for data-dense interfaces like trading platforms or spreadsheets.

```css
:root {
  /* Type Scale — Minor Second (1.067) — Ultra Dense */
  --font-size-4xs: 0.625rem;   /* 10px — sparkline labels, badge counts */
  --font-size-3xs: 0.6875rem;  /* 11px — compact table cells */
  --font-size-2xs: 0.75rem;    /* 12px — table data, secondary labels */
  --font-size-xs: 0.8125rem;   /* 13px — form labels */
  --font-size-sm: 0.875rem;    /* 14px — primary body text (NOTE: body is 14px in dense mode) */
  --font-size-base: 0.875rem;  /* 14px — base in dense mode */
  --font-size-md: 0.9375rem;   /* 15px — emphasized text */
  --font-size-lg: 1rem;        /* 16px — card titles */
  --font-size-xl: 1.125rem;    /* 18px — section headings */
  --font-size-2xl: 1.25rem;    /* 20px — page title */
  --font-size-3xl: 1.5rem;     /* 24px — dashboard KPIs */

  /* Dense Line Heights */
  --leading-dense: 1.15;
  --leading-compact: 1.25;
  --leading-normal: 1.4;

  /* Dense Spacing */
  --space-cell-y: 0.25rem;
  --space-cell-x: 0.5rem;
}

/* Dense Table */
.dense-table th {
  font-size: var(--font-size-2xs);
  line-height: var(--leading-dense);
  letter-spacing: 0.04em;
  text-transform: uppercase;
  font-weight: 600;
  padding: var(--space-cell-y) var(--space-cell-x);
}

.dense-table td {
  font-size: var(--font-size-2xs);
  line-height: var(--leading-compact);
  font-variant-numeric: tabular-nums;
  padding: var(--space-cell-y) var(--space-cell-x);
}

/* Dense Form */
.dense-label {
  font-size: var(--font-size-xs);
  line-height: var(--leading-dense);
  font-weight: 500;
}

.dense-input {
  font-size: var(--font-size-sm);
  line-height: var(--leading-compact);
  padding: 0.25rem 0.5rem;
}
```

### Recipe 11: Presentation/Slide Scale (Golden Ratio 1.618)

For fullscreen presentations and slide-like layouts.

```css
:root {
  /* Type Scale — Golden Ratio (1.618) */
  --font-size-sm: 0.875rem;     /* 14px — footnotes */
  --font-size-base: 1rem;       /* 16px — body text */
  --font-size-md: 1.618rem;     /* 25.9px — bullet points */
  --font-size-lg: 2.618rem;     /* 41.9px — subheadings */
  --font-size-xl: 4.236rem;     /* 67.8px — slide titles */
  --font-size-2xl: 6.854rem;    /* 109.7px — hero statements */
  --font-size-display: 11.089rem; /* 177.4px — single-word impact */

  /* Presentation Line Heights */
  --leading-display: 0.9;
  --leading-title: 1.0;
  --leading-heading: 1.1;
  --leading-body: 1.4;
}

/* Slide Styles */
.slide-statement {
  font-size: var(--font-size-2xl);
  line-height: var(--leading-display);
  letter-spacing: -0.05em;
  font-weight: 900;
  text-wrap: balance;
}

.slide-title {
  font-size: var(--font-size-xl);
  line-height: var(--leading-title);
  letter-spacing: -0.03em;
  font-weight: 700;
}

.slide-bullet {
  font-size: var(--font-size-md);
  line-height: var(--leading-heading);
  font-weight: 400;
}

.slide-footnote {
  font-size: var(--font-size-sm);
  line-height: var(--leading-body);
  color: var(--color-text-tertiary);
}
```

### Recipe 12: Fluid Container Query Scale

Uses container queries for component-level responsive typography.

```css
/* Container-responsive type scale */
.card-container {
  container-type: inline-size;
  container-name: card;
}

@container card (min-width: 0px) {
  .card-title {
    font-size: 1rem;
    line-height: 1.3;
  }
  .card-body {
    font-size: 0.875rem;
    line-height: 1.5;
  }
}

@container card (min-width: 300px) {
  .card-title {
    font-size: 1.25rem;
    line-height: 1.25;
  }
  .card-body {
    font-size: 1rem;
    line-height: 1.5;
  }
}

@container card (min-width: 500px) {
  .card-title {
    font-size: 1.5rem;
    line-height: 1.2;
  }
  .card-body {
    font-size: 1.0625rem;
    line-height: 1.6;
  }
}

@container card (min-width: 700px) {
  .card-title {
    font-size: 2rem;
    line-height: 1.15;
    letter-spacing: -0.01em;
  }
  .card-body {
    font-size: 1.125rem;
    line-height: 1.6;
  }
}

/* Container Query Units (cqi = 1% of container inline size) */
.responsive-headline {
  font-size: clamp(1.25rem, 5cqi, 3rem);
  line-height: 1.1;
}

.responsive-body {
  font-size: clamp(0.875rem, 2.5cqi, 1.125rem);
  line-height: 1.5;
}
```

---

## Line-Height Rules by Size

### The Inverse Relationship

As font size increases, line-height (leading) should decrease proportionally. This is because larger text has more internal whitespace and needs less external whitespace to be readable.

| Font Size Range | Line-Height | Rationale |
|----------------|-------------|-----------|
| 10-12px | 1.6-1.7 | Tiny text needs generous leading for readability |
| 13-14px | 1.5-1.6 | Small text, captions, labels |
| 15-16px | 1.5 | Body text sweet spot (the "golden standard") |
| 17-18px | 1.45-1.5 | Large body, intro text |
| 19-22px | 1.3-1.4 | Subheadings, card titles |
| 23-28px | 1.2-1.3 | Section headings |
| 29-40px | 1.1-1.2 | Page headings |
| 41-60px | 1.05-1.1 | Display text |
| 61px+ | 0.95-1.05 | Hero text (can go below 1 for tight stacking) |

### Line-Height for Multi-line vs Single-line

- **Single-line headings**: Can use tighter line-height (1.0-1.1) safely
- **Multi-line headings**: Need looser line-height (1.15-1.25) to prevent collision
- **Body text**: Always 1.4-1.7 regardless of number of lines

### Font-Specific Adjustments

Different fonts have different built-in spacing:

| Font Style | Adjustment |
|-----------|------------|
| Serif body fonts | +0.05 to +0.1 (serifs create visual noise; needs more space) |
| Geometric sans | Standard (already has even spacing) |
| Condensed fonts | +0.05 to +0.1 (taller letterforms need more leading) |
| Rounded fonts | -0.05 (rounded terminals create more internal space) |
| Monospace | Standard to +0.1 (depends on context: code vs prose) |

---

## Letter-Spacing Adjustments

### Size-Based Rules

```css
/* Letter-spacing decreases as size increases */
.text-xs     { letter-spacing: 0.02em; }   /* Open up small text */
.text-sm     { letter-spacing: 0.01em; }   /* Slightly open */
.text-base   { letter-spacing: 0; }        /* Default — no adjustment */
.text-lg     { letter-spacing: 0; }        /* Still default */
.text-xl     { letter-spacing: -0.005em; } /* Begin tightening */
.text-2xl    { letter-spacing: -0.01em; }  /* Moderate tightening */
.text-3xl    { letter-spacing: -0.015em; } /* Noticeable tightening */
.text-4xl    { letter-spacing: -0.02em; }  /* Tight */
.text-display { letter-spacing: -0.03em; } /* Very tight */
.text-hero   { letter-spacing: -0.04em; }  /* Maximum tightening */
```

### Context-Based Rules

```css
/* All caps always need opening */
.uppercase-label {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
  font-size: 0.75em;
}

/* Small caps */
.small-caps {
  font-variant-caps: small-caps;
  letter-spacing: 0.05em;
}

/* Monospace — never adjust */
code, pre, .mono {
  letter-spacing: 0;  /* Fixed-width handles its own spacing */
}

/* Numeric displays */
.number-display {
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;  /* Tighten numbers at large sizes */
}
```

---

## Paragraph Width (Measure)

### The 45-75 Character Rule

Optimal reading line length is 45-75 characters per line, with 65 characters being the ideal. This applies to body text at comfortable reading size.

```css
/* Width Units: ch = width of the "0" character */
.measure-narrow  { max-width: 45ch; }  /* Narrow columns, sidebars */
.measure-default { max-width: 65ch; }  /* Ideal body text */
.measure-wide    { max-width: 75ch; }  /* Wide content, documentation */
.measure-ultra   { max-width: 90ch; }  /* Code blocks only */
```

### Size-Adjusted Measure

Wider fonts need fewer characters per line, narrower fonts can handle more:

| Font Style | Recommended ch | Example |
|-----------|----------------|---------|
| Wide sans (Inter, Open Sans) | 60-70ch | Standard |
| Narrow sans (Barlow, Archivo) | 65-80ch | Can be wider |
| Serif body (Lora, Merriweather) | 55-65ch | Serifs slow reading; shorter lines help |
| Monospace | 80-100ch | Code blocks have different rules |
| Large text (> 24px) | 30-45ch | Fewer characters at larger sizes |

---

## Responsive Type Scaling Strategies

### Strategy 1: Breakpoint Steps (Traditional)

Simplest approach. Change sizes at breakpoints.

**Pros**: Predictable, easy to debug, works everywhere.
**Cons**: Jarring jumps between breakpoints, many custom properties to manage.

### Strategy 2: Fluid Typography with clamp()

Smooth scaling between a minimum and maximum using viewport width.

**Pros**: No jumps, single declaration per size, modern and elegant.
**Cons**: Requires careful calculation, can be unpredictable at extreme viewport widths.

**Browser support**: 96%+ (all modern browsers).

### Strategy 3: Container Queries

Component-responsive typography based on parent container size.

**Pros**: Component-level control, works in any layout context.
**Cons**: Newer feature (2023+), slight learning curve.

**Browser support**: 91%+ (all modern browsers as of 2025).

### Strategy 4: Hybrid (Recommended)

Combine fluid type for body and headings with container queries for components.

```css
/* Global: Fluid type scale */
:root {
  --font-size-base: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  --font-size-xl: clamp(1.5rem, 1rem + 1.5vw, 2.25rem);
}

/* Component: Container query overrides */
.card {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card-title {
    font-size: var(--font-size-xl);
  }
}
```

### Strategy 5: User Preference Scaling

Respect user's preferred font size and never override it.

```css
/* NEVER do this */
html { font-size: 16px; }          /* Overrides user preference */
html { font-size: 62.5%; }         /* Overrides user preference */

/* DO this instead */
html { font-size: 100%; }          /* Respects user preference (default) */
body { font-size: 1rem; }          /* Inherits from html */

/* All sizes in rem inherit the user's preference */
h1 { font-size: 2rem; }            /* 2x user's preferred size */
```

---

## Cross-References

- **font-pairing-catalog.md** — 105+ font pairings to use with these scales
- **platform-font-stacks.md** — System fonts and loading strategies
- **design-token-presets** — Complete token systems with type scales included
- **visual-design-mastery** — Typography scoring and quality assessment
