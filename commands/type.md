---
name: type
description: "Generate a complete typography system — font pairing, modular type scale with fluid clamp() values, line-height, letter-spacing, and platform stacks."
argument-hint: "[brand voice or existing fonts]"
---

# Type — Complete Typography System Generator

## Before running

This command needs a brand voice or the existing fonts to work from.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate a production-grade typography system from a style direction, platform, or font preference. Outputs font pairing with rationale, a modular type scale with fluid `clamp()` values, per-size line-height and letter-spacing, responsive scaling strategy, platform font stacks, and complete CSS/Tailwind code.

This command goes deeper than `/style` on typography alone. Use it when you need precise typographic control, want to explore pairings, or are building a type-heavy product (editorial, documentation, content platform).

---

## Input Parameters

| Parameter | Required | Default | Examples |
|-----------|----------|---------|----------|
| **Style** | No | balanced | minimal, editorial, corporate, friendly, expressive, technical, luxury |
| **Platform** | No | web | web, iOS, Android, cross-platform, desktop |
| **Sector** | No | — | fintech, SaaS, editorial, e-commerce, education |
| **Font preference** | No | — | "Inter", "serif headings", "geometric sans", "monospace-forward" |
| **Density** | No | balanced | tight, balanced, airy |
| **Scale ratio** | No | Auto-selected | 1.125, 1.200, 1.250, 1.333, 1.414, 1.500, 1.618 |
| **Base size** | No | 16px | 14px, 15px, 16px, 18px |
| **Brand tone** | No | — | "serious and precise", "warm and approachable", "bold and modern" |

If `.sumi/style.json` exists with typography data from `/style`, load it and refine rather than starting from scratch.

---

## Generation Protocol

### Step 1 — Style Analysis and Ratio Selection

Map the requested style to typographic parameters:

| Style | Scale Ratio | Weight Range | Heading Character | Body Character | Best For |
|-------|------------|-------------|-------------------|---------------|----------|
| **Minimal** | 1.200 (Minor Third) | 400-600 | Clean, understated | Neutral, high-readability | SaaS, dev tools, productivity |
| **Editorial** | 1.333 (Perfect Fourth) | 300-700 | Expressive, distinctive | Readable, comfortable | Media, blogs, magazines, content |
| **Corporate** | 1.250 (Major Third) | 400-700 | Authoritative, structured | Professional, clear | Enterprise, B2B, fintech, legal |
| **Friendly** | 1.250 (Major Third) | 400-600 | Rounded, approachable | Warm, inviting | Consumer apps, education, wellness |
| **Expressive** | 1.414 (Aug. Fourth) | 300-900 | Bold, dramatic | Balanced contrast to headings | Creative, gaming, music, fashion |
| **Technical** | 1.200 (Minor Third) | 400-500 | Monospace-influenced | Dense, precise | Dev tools, documentation, data |
| **Luxury** | 1.500 (Perfect Fifth) | 300-600 | Elegant, high contrast | Refined, generous spacing | Automotive, real estate, premium |

### Step 2 — Font Pairing Recommendation

Select specific fonts based on style, sector, and platform. Provide:

**Primary Pairing:**

| Role | Font | Category | Weights | Why This Font |
|------|------|----------|---------|--------------|
| **Headings** | [Specific font name] | [sans/serif/display] | [e.g., 600, 700] | [1-sentence personality rationale] |
| **Body** | [Specific font name] | [sans/serif] | [e.g., 400, 500] | [1-sentence readability rationale] |
| **Mono** | [Specific font name] | monospace | [e.g., 400] | [1-sentence utility rationale] |

**Why This Pairing Works:**
- **Contrast principle**: [How heading and body fonts create hierarchy through contrast — e.g., serif heading + sans body creates classic editorial contrast]
- **X-height compatibility**: [Both fonts share similar x-height proportions, preventing visual jarring when mixed]
- **Character coverage**: [Both support Latin Extended, and mono covers programming ligatures]
- **Personality match**: [How the fonts together communicate the brand tone]

**Alternative Pairing** (if the primary feels too safe):

| Role | Font | Why |
|------|------|-----|
| Headings | [Alt font] | [Brief rationale] |
| Body | [Alt font] | [Brief rationale] |

**Framework-Aware Font Loading:**

Detect the project framework and output the correct loading strategy.

**If Next.js detected** (next.config.js/ts exists):
```typescript
// app/layout.tsx — next/font self-hosts, eliminates CLS, zero external requests
import { Inter, [Heading_Font], [Mono_Font] } from 'next/font/google';

const heading = [Heading_Font]({
  subsets: ['latin'],
  weight: ['600', '700'],
  variable: '--font-heading',
  display: 'swap',
});

const body = Inter({
  subsets: ['latin'],
  weight: ['400', '500'],
  variable: '--font-body',
  display: 'swap',
});

const mono = [Mono_Font]({
  subsets: ['latin'],
  weight: ['400'],
  variable: '--font-mono',
  display: 'swap',
});

// Apply CSS variables to <html>
<html className={`${heading.variable} ${body.variable} ${mono.variable}`}>
```

**If Next.js + Tailwind v4** (detected via `@import "tailwindcss"` in CSS):
```css
/* app/globals.css */
@import "tailwindcss";

@theme {
  --font-heading: var(--font-heading), system-ui, sans-serif;
  --font-body: var(--font-body), system-ui, sans-serif;
  --font-mono: var(--font-mono), ui-monospace, monospace;
}
```

**If Remix / Vite / Astro** (no next/font available):
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=[Heading+Font]:wght@600;700&family=[Body+Font]:wght@400;500&family=[Mono+Font]&display=swap" rel="stylesheet" />
```

**Fallback (static HTML, any framework):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=[Heading+Font]:wght@600;700&family=[Body+Font]:wght@400;500&family=[Mono+Font]&display=swap" rel="stylesheet" />
```

**Detection Priority:**
1. `next.config.js/ts` → `next/font/google` (always preferred)
2. `@fontsource/*` in `package.json` → `@fontsource` imports
3. Remix/Vite/Astro config → `<link>` with preconnect
4. Fallback → `<link>` with `font-display: swap`

**Performance Rules:**
- `next/font` self-hosts fonts and applies `size-adjust` to match fallback metrics — zero layout shift
- Always `font-display: swap` — FOUT is better than FOIT
- Subset to `latin` unless CJK/Cyrillic/Arabic needed
- Load only used weights (never `100..900` range)

### Step 3 — Font Family Stacks

Complete `font-family` declarations with system fallbacks for every platform.

```css
/* --- Web (cross-platform fallbacks) --- */
--font-heading: '[Heading Font]', 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
--font-body: '[Body Font]', 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
--font-mono: '[Mono Font]', 'JetBrains Mono', 'Fira Code', 'Cascadia Code', 'SF Mono', 'Consolas', monospace;
```

**Platform-Specific System Font Stacks:**

| Platform | Sans Stack | Serif Stack | Mono Stack |
|----------|-----------|------------|-----------|
| **iOS / macOS** | 'SF Pro', -apple-system, system-ui, sans-serif | 'New York', 'Georgia', 'Times New Roman', serif | 'SF Mono', 'Menlo', monospace |
| **Android** | 'Roboto', system-ui, sans-serif | 'Noto Serif', 'Georgia', serif | 'Roboto Mono', monospace |
| **Windows** | 'Segoe UI', system-ui, sans-serif | 'Cambria', 'Georgia', serif | 'Cascadia Code', 'Consolas', monospace |
| **Linux** | 'Ubuntu', 'Cantarell', system-ui, sans-serif | 'Noto Serif', 'DejaVu Serif', serif | 'Ubuntu Mono', 'DejaVu Sans Mono', monospace |
| **Universal** | system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif | 'Georgia', 'Times New Roman', 'Noto Serif', serif | ui-monospace, 'SF Mono', 'Cascadia Code', 'Consolas', monospace |

If targeting a specific platform (iOS app, Android app, Electron), use the platform-native fonts as primary and eliminate the Google Fonts dependency.

### Step 4 — Modular Type Scale

Compute the full type scale from the chosen base size and ratio. Every value is provided in px, rem, and `clamp()`.

**Scale Parameters:**
- Base size: [X]px / [X]rem
- Scale ratio: [X] ([Name])
- Viewport range: 375px (mobile) to 1440px (desktop)
- Fluid scaling: `clamp(min, preferred, max)` using the formula `clamp([mobile]rem, [calc]rem + [vw]vw, [desktop]rem)`

**Type Scale Table:**

| Token | Step | Desktop (px) | Desktop (rem) | Mobile (px) | Mobile (rem) | Fluid `clamp()` | Line Height | Letter Spacing | Weight |
|-------|------|-------------|--------------|------------|-------------|-----------------|-------------|---------------|--------|
| text-2xs | -3 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.5 | 0.03em | 400 |
| text-xs | -2 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.5 | 0.02em | 400 |
| text-sm | -1 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.5 | 0.01em | 400 |
| text-base | 0 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.5 | 0 | 400 |
| text-lg | 1 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.4 | -0.01em | 400-500 |
| text-xl | 2 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.3 | -0.015em | 500-600 |
| text-2xl | 3 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.25 | -0.02em | 600 |
| text-3xl | 4 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.2 | -0.02em | 600-700 |
| text-4xl | 5 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.15 | -0.025em | 700 |
| text-5xl | 6 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.1 | -0.03em | 700 |
| text-6xl | 7 | [x] | [x] | [x] | [x] | clamp([x]rem, [x]rem + [x]vw, [x]rem) | 1.05 | -0.03em | 700 |

**How clamp() is computed:**
1. Define desired size at mobile breakpoint (375px) and desktop breakpoint (1440px)
2. Mobile sizes are typically 85-90% of desktop for body, 60-70% of desktop for display sizes
3. The preferred value uses `rem + vw` to create smooth interpolation:
   - `preferred = mobile_rem + ((desktop_px - mobile_px) / (1440 - 375)) * 100vw`
   - Simplified: `preferred = [base]rem + [slope]vw`

### Step 5 — Line Height Rules

Line height varies by size and purpose. Larger text needs tighter line height; smaller text needs more space.

| Size Range | Line Height | Rationale |
|-----------|------------|-----------|
| Display (4xl-6xl) | 1.05-1.15 | Large text has built-in spacing; tight leading looks intentional |
| Heading (2xl-3xl) | 1.2-1.25 | Balanced — scannable but not loose |
| Subheading (lg-xl) | 1.3-1.4 | Transitional — bridges heading and body |
| Body (base-sm) | 1.5-1.6 | Optimal readability for long-form (research-backed: 1.5 is the floor) |
| Caption (xs-2xs) | 1.5 | Small text needs generous leading for readability |
| UI labels | 1.0-1.2 | Single-line elements in buttons, tabs, badges |

**Paragraph-specific line height guidance:**
- Short paragraphs (1-3 lines): 1.5 is fine
- Long-form reading (4+ lines): 1.6-1.7 improves comprehension
- Narrow columns (< 40ch): Increase by 0.1
- Wide columns (> 70ch): Decrease by 0.05 (tighter feels better in wide measure)

### Step 6 — Letter Spacing Rules

| Size Range | Letter Spacing | Rationale |
|-----------|---------------|-----------|
| Display (4xl+) | -0.025em to -0.03em | Large optically-designed text benefits from tightening |
| Heading (2xl-3xl) | -0.02em | Moderate tightening |
| Subheading (xl) | -0.015em | Subtle tightening |
| Body (base) | 0 | Default tracking; most fonts are optimized for body at 0 |
| Small (sm-xs) | +0.01em to +0.02em | Small text benefits from slight opening |
| Tiny (2xs) | +0.03em | More opening for legibility at small sizes |
| UPPERCASE labels | +0.05em to +0.10em | All-caps always needs extra tracking |
| Monospace | 0 | Monospace fonts are pre-spaced; do not adjust |

### Step 7 — Paragraph and Measure

| Token | Value | Rationale |
|-------|-------|-----------|
| **prose-max-width** | 65ch | Optimal line length for body text (research: 50-75ch, 65ch is the sweet spot) |
| **prose-max-width-narrow** | 45ch | For captions, sidebars, card descriptions |
| **prose-max-width-wide** | 80ch | For code blocks, data tables, wide layouts |
| **paragraph-margin** | 1em (= 1 line of text) | Standard inter-paragraph spacing |
| **heading-margin-top** | 1.5em-2em | Space above headings (more than paragraph gap) |
| **heading-margin-bottom** | 0.5em | Close to the content they introduce (Gestalt proximity) |
| **list-item-gap** | 0.25em-0.5em | Tighter than paragraphs — list items are related |

### Step 8 — Responsive Scaling Strategy

Define how typography adapts across breakpoints.

**Breakpoint Typography Rules:**

| Breakpoint | Width | Base Size | Scale Behavior |
|-----------|-------|----------|---------------|
| **Mobile** | < 640px | 15-16px | Fluid via clamp(); display sizes compress significantly |
| **Tablet** | 640-1024px | 16px | Fluid interpolation continues |
| **Desktop** | 1024-1440px | 16-18px | Full scale reached |
| **Large desktop** | > 1440px | 18px max | Sizes cap — do NOT continue scaling beyond this |

**Key responsive rules:**
1. Body text stays relatively stable (15-18px range across all viewports)
2. Display/heading text compresses dramatically on mobile (a 61px desktop heading might be 32px on mobile)
3. `clamp()` handles this smoothly without media queries
4. Never go below 14px for any readable text (12px absolute minimum for legal/fine print)
5. Touch targets: Ensure tappable text elements (links, buttons) have at least 44px touch target

**Container query typography (modern CSS):**

```css
/* Scale text based on container, not viewport */
@container (min-width: 400px) {
  .card-title { font-size: var(--font-size-lg); }
}
@container (min-width: 600px) {
  .card-title { font-size: var(--font-size-xl); }
}
```

### Step 9 — Typographic Utilities

Define commonly needed text styles as composable utilities.

| Utility | Font | Size | Weight | Line Height | Letter Spacing | Usage |
|---------|------|------|--------|-------------|---------------|-------|
| .text-display | heading | 5xl-6xl | 700 | 1.05-1.1 | -0.03em | Hero sections, landing pages |
| .text-title | heading | 3xl-4xl | 700 | 1.15-1.2 | -0.025em | Page titles, section headings |
| .text-heading | heading | 2xl | 600 | 1.25 | -0.02em | Card headings, sub-sections |
| .text-subheading | heading | lg-xl | 600 | 1.3 | -0.015em | Group labels, sub-headings |
| .text-body | body | base | 400 | 1.5 | 0 | Paragraphs, descriptions |
| .text-body-strong | body | base | 500-600 | 1.5 | 0 | Emphasized body text |
| .text-caption | body | sm | 400 | 1.5 | 0.01em | Metadata, timestamps, helper text |
| .text-label | body | sm | 500 | 1.0 | 0.02em | Form labels, tab labels, nav items |
| .text-overline | body | xs | 600 | 1.0 | 0.08em | UPPERCASE category labels |
| .text-code | mono | sm | 400 | 1.6 | 0 | Inline code, code blocks |
| .text-data | mono | base | 400 | 1.4 | 0 | Numbers, financial data, stats |

### Step 10 — CSS Custom Properties Output

Complete, copy-paste-ready CSS.

```css
/* ============================================================
   Typography System — [Style] / [Platform]
   Generated by Sumi /type
   ============================================================ */

:root {
  /* --- Font Families --- */
  --font-heading: '[Heading]', [fallback stack];
  --font-body: '[Body]', [fallback stack];
  --font-mono: '[Mono]', [fallback stack];

  /* --- Font Sizes (fluid) --- */
  --text-2xs: clamp(...);
  --text-xs: clamp(...);
  --text-sm: clamp(...);
  --text-base: clamp(...);
  --text-lg: clamp(...);
  --text-xl: clamp(...);
  --text-2xl: clamp(...);
  --text-3xl: clamp(...);
  --text-4xl: clamp(...);
  --text-5xl: clamp(...);
  --text-6xl: clamp(...);

  /* --- Font Weights --- */
  --font-light: 300;
  --font-regular: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;

  /* --- Line Heights --- */
  --leading-none: 1;
  --leading-tight: 1.15;
  --leading-snug: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 1.75;

  /* --- Letter Spacing --- */
  --tracking-tighter: -0.03em;
  --tracking-tight: -0.02em;
  --tracking-slightly-tight: -0.01em;
  --tracking-normal: 0;
  --tracking-slightly-wide: 0.01em;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.10em;

  /* --- Measure (line length) --- */
  --measure-narrow: 45ch;
  --measure: 65ch;
  --measure-wide: 80ch;

  /* --- Paragraph Spacing --- */
  --paragraph-gap: 1em;
  --heading-gap-top: 1.5em;
  --heading-gap-bottom: 0.5em;
}

/* --- Typographic Utilities --- */
.text-display {
  font-family: var(--font-heading);
  font-size: var(--text-5xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tighter);
}

.text-title {
  font-family: var(--font-heading);
  font-size: var(--text-3xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
}

.text-heading {
  font-family: var(--font-heading);
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
}

.text-subheading {
  font-family: var(--font-heading);
  font-size: var(--text-lg);
  font-weight: var(--font-semibold);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-slightly-tight);
}

.text-body {
  font-family: var(--font-body);
  font-size: var(--text-base);
  font-weight: var(--font-regular);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
}

.text-body-strong {
  font-family: var(--font-body);
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
}

.text-caption {
  font-family: var(--font-body);
  font-size: var(--text-sm);
  font-weight: var(--font-regular);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-slightly-wide);
}

.text-label {
  font-family: var(--font-body);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-wide);
}

.text-overline {
  font-family: var(--font-body);
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
}

.text-code {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: var(--font-regular);
  line-height: var(--leading-relaxed);
  letter-spacing: var(--tracking-normal);
}

.text-data {
  font-family: var(--font-mono);
  font-size: var(--text-base);
  font-weight: var(--font-regular);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-normal);
  font-variant-numeric: tabular-nums;
}

/* --- Prose (long-form content) --- */
.prose {
  font-family: var(--font-body);
  font-size: var(--text-base);
  font-weight: var(--font-regular);
  line-height: var(--leading-relaxed);
  max-width: var(--measure);
  letter-spacing: var(--tracking-normal);
}

.prose h1 { font-family: var(--font-heading); font-size: var(--text-4xl); font-weight: var(--font-bold); line-height: var(--leading-tight); letter-spacing: var(--tracking-tight); margin-top: 0; margin-bottom: var(--heading-gap-bottom); }
.prose h2 { font-family: var(--font-heading); font-size: var(--text-3xl); font-weight: var(--font-bold); line-height: var(--leading-snug); letter-spacing: var(--tracking-tight); margin-top: var(--heading-gap-top); margin-bottom: var(--heading-gap-bottom); }
.prose h3 { font-family: var(--font-heading); font-size: var(--text-2xl); font-weight: var(--font-semibold); line-height: var(--leading-snug); letter-spacing: var(--tracking-tight); margin-top: var(--heading-gap-top); margin-bottom: var(--heading-gap-bottom); }
.prose h4 { font-family: var(--font-heading); font-size: var(--text-xl); font-weight: var(--font-semibold); line-height: var(--leading-snug); letter-spacing: var(--tracking-slightly-tight); margin-top: var(--heading-gap-top); margin-bottom: var(--heading-gap-bottom); }
.prose p { margin-bottom: var(--paragraph-gap); }
.prose ul, .prose ol { margin-bottom: var(--paragraph-gap); padding-left: 1.5em; }
.prose li { margin-bottom: 0.25em; }
.prose code { font-family: var(--font-mono); font-size: 0.875em; }
.prose blockquote { border-left: 3px solid currentColor; padding-left: 1em; opacity: 0.85; font-style: italic; }

/* --- Reduced motion: disable any text animation --- */
@media (prefers-reduced-motion: reduce) {
  * { text-decoration-skip-ink: auto; }
}
```

All `(...)` values are replaced with actual computed values at generation time.

### Step 11 — Tailwind Typography Config

```js
// tailwind.config.js — typography extension
// Generated by Sumi /type
const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  theme: {
    extend: {
      fontFamily: {
        heading: ['[Heading Font]', ...defaultTheme.fontFamily.sans],
        body:    ['[Body Font]', ...defaultTheme.fontFamily.sans],
        mono:    ['[Mono Font]', ...defaultTheme.fontFamily.mono],
      },
      fontSize: {
        '2xs': ['clamp(...)', { lineHeight: '1.5', letterSpacing: '0.03em' }],
        xs:    ['clamp(...)', { lineHeight: '1.5', letterSpacing: '0.02em' }],
        sm:    ['clamp(...)', { lineHeight: '1.5', letterSpacing: '0.01em' }],
        base:  ['clamp(...)', { lineHeight: '1.5', letterSpacing: '0em' }],
        lg:    ['clamp(...)', { lineHeight: '1.4', letterSpacing: '-0.01em' }],
        xl:    ['clamp(...)', { lineHeight: '1.3', letterSpacing: '-0.015em' }],
        '2xl': ['clamp(...)', { lineHeight: '1.25', letterSpacing: '-0.02em' }],
        '3xl': ['clamp(...)', { lineHeight: '1.2', letterSpacing: '-0.02em' }],
        '4xl': ['clamp(...)', { lineHeight: '1.15', letterSpacing: '-0.025em' }],
        '5xl': ['clamp(...)', { lineHeight: '1.1', letterSpacing: '-0.03em' }],
        '6xl': ['clamp(...)', { lineHeight: '1.05', letterSpacing: '-0.03em' }],
      },
      lineHeight: {
        tight:   '1.15',
        snug:    '1.25',
        normal:  '1.5',
        relaxed: '1.625',
        loose:   '1.75',
      },
      letterSpacing: {
        tighter: '-0.03em',
        tight:   '-0.02em',
        normal:  '0',
        wide:    '0.025em',
        wider:   '0.05em',
        widest:  '0.10em',
      },
      maxWidth: {
        prose:        '65ch',
        'prose-narrow': '45ch',
        'prose-wide': '80ch',
      },
    },
  },
  plugins: [
    // require('@tailwindcss/typography'), // recommended for .prose
  ],
}
```

**Tailwind v4 (`@theme` — CSS-first configuration):**

If the project uses Tailwind v4 (detected by `@import "tailwindcss"` in CSS instead of `tailwind.config.js`), output CSS-native theme configuration instead of the JS config above:

```css
/* app/globals.css — Tailwind v4 */
@import "tailwindcss";

@theme {
  /* Font Families */
  --font-heading: '[Heading Font]', system-ui, sans-serif;
  --font-body: '[Body Font]', system-ui, sans-serif;
  --font-mono: '[Mono Font]', ui-monospace, monospace;

  /* Font Sizes (fluid) */
  --text-2xs: clamp(0.625rem, 0.6rem + 0.1vw, 0.75rem);
  --text-xs: clamp(0.75rem, 0.72rem + 0.15vw, 0.875rem);
  --text-sm: clamp(0.8125rem, 0.78rem + 0.15vw, 0.875rem);
  --text-base: clamp(0.875rem, 0.85rem + 0.2vw, 1rem);
  --text-lg: clamp(1rem, 0.95rem + 0.3vw, 1.25rem);
  --text-xl: clamp(1.25rem, 1.15rem + 0.45vw, 1.5625rem);
  --text-2xl: clamp(1.5rem, 1.35rem + 0.6vw, 1.9375rem);
  --text-3xl: clamp(1.875rem, 1.65rem + 0.8vw, 2.4375rem);
  --text-4xl: clamp(2.25rem, 1.95rem + 1vw, 3.0625rem);
  --text-5xl: clamp(2.75rem, 2.3rem + 1.3vw, 3.8125rem);
  --text-6xl: clamp(3.25rem, 2.7rem + 1.6vw, 4.75rem);

  /* Line Heights */
  --leading-tight: 1.15;
  --leading-snug: 1.25;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 1.75;

  /* Letter Spacing */
  --tracking-tighter: -0.03em;
  --tracking-tight: -0.02em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.10em;
}
```

**Detection Logic:** If `tailwind.config.js` exists → output Tailwind v3 JS config. If `@import "tailwindcss"` found in CSS → output Tailwind v4 `@theme` block. If both → output v4 (newer wins).

### Step 12 — Font Loading Performance

Best practices for font loading to avoid layout shift (CLS) and invisible text (FOIT).

**Strategy: FOUT over FOIT** (Flash of Unstyled Text is better than Flash of Invisible Text)

```css
/* Font-display: swap ensures text is visible immediately with system font,
   then swaps to custom font when loaded */
@font-face {
  font-family: '[Heading Font]';
  src: url('/fonts/[heading-font].woff2') format('woff2');
  font-weight: 600 700;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

@font-face {
  font-family: '[Body Font]';
  src: url('/fonts/[body-font].woff2') format('woff2');
  font-weight: 400 500;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
```

**Size-adjust for reduced CLS:**

```css
/* Match system font metrics to custom font to minimize layout shift */
@font-face {
  font-family: '[Heading Font] Fallback';
  src: local('Arial');
  size-adjust: 100.5%;    /* adjust to match custom font metrics */
  ascent-override: 95%;
  descent-override: 22%;
  line-gap-override: 0%;
}

/* Use in stack: */
--font-heading: '[Heading Font]', '[Heading Font] Fallback', system-ui, sans-serif;
```

**Preload critical fonts:**

```html
<link rel="preload" href="/fonts/[body-font]-latin-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/[heading-font]-latin-700.woff2" as="font" type="font/woff2" crossorigin>
```

### Step 13 — Save to `.sumi/style.json`

`/type` owns `tokens.typography` and nothing else. Follow `design-memory`: load,
deep-merge your subtree, append `"/type"` to `meta.updatedBy`, write back.

Merge the family stack, the modular scale, line heights and letter-spacing into
`tokens.typography`. Leave every other subtree byte-identical.

---

## Output Format

```
## Type: [Style] — [Platform / Sector]

### Style Analysis
[Rationale for ratio, weight range, and typographic personality]

### Font Pairing
[Primary and alt pairings with Google Fonts integration code]

### Platform Font Stacks
[Complete font-family declarations per platform]

### Type Scale
[Full table: token, step, px, rem, clamp(), line-height, letter-spacing, weight]

### Line Height Rules
[Per-size and per-context rules]

### Letter Spacing Rules
[Per-size and per-context rules]

### Paragraph & Measure
[Max-width, spacing, heading gaps]

### Responsive Strategy
[Breakpoint behavior, clamp() methodology, container queries]

### Typographic Utilities
[Utility class table]

### CSS Custom Properties
[Complete copy-paste CSS block with utilities and prose styles]

### Tailwind Config
[Complete extend block]

### Font Loading
[Performance strategy: preload, font-display, size-adjust, fallback matching]

### Saved
> Typography saved to `.sumi/style.json` — available to `/style`, `/palette`, `/tokens`, `/screen`, `/component`
```

---

## Cross-References

When generating typography systems, draw knowledge from:
- `typography-pairing-recipes` skill for 100+ validated font pairings and pairing principles
- `ui-visual-design-system` skill for typographic hierarchy, scale theory, and visual rhythm
- `visual-design-mastery` skill for canonical typography rules and visual scoring
- `platform-visual-standards` skill for iOS 26, Material 3, and modern CSS typography norms
- `mobile-ux-design` skill for mobile-specific type sizing and touch target requirements
- `desktop-app-design` skill for desktop information density and type scale conventions
- `accessibility-inclusive-design` skill for minimum text sizes, contrast, and dyslexia-friendly type
- `cross-cultural-i18n-ux` skill for multilingual typography (CJK, RTL, script stacking)
- `sector-style-intelligence` skill for sector-specific typographic conventions
- `design-token-presets` skill for pre-built typography token systems
- `responsive-block-patterns` skill for fluid scaling and container query patterns
- `component-patterns-code` skill for typography implementation in React and SwiftUI

## Next Step

**Next** -> `/palette` — Generate color system to pair with this typography
**Or** -> `/style` — Full visual identity (color + type + spacing + motion + tone)
**Or** -> `/tokens` — Export typography as production W3C design tokens
**Or** -> `/screen` — Build screens using your new type system