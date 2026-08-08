# Typography Mastery

> Typography systems for UI: classification, variable fonts, type scales, font pairing, hierarchy, line-height, rendering, responsive type, and platform stacks.

---

## Type Classification for UI

### Geometric Sans-Serif

**Examples**: Inter, Geist, SF Pro, Circular, Euclid, Outfit
**Character**: Clean, modern, precise. Letterforms built from geometric shapes (circles, straight lines).
**Best for**: Product UI, dashboards, SaaS, developer tools
**Pros**: High legibility at small sizes (especially Inter, SF Pro). Neutral personality doesn't impose brand.
**Cons**: Can feel cold or generic without careful weight/size variation.
**CSS**: `font-family: 'Inter', 'Geist', system-ui, -apple-system, sans-serif;`

### Humanist Sans-Serif

**Examples**: Source Sans 3, Nunito, Lato, Open Sans, Fira Sans
**Character**: Warm, approachable, friendly. Letterforms based on calligraphic proportions.
**Best for**: Consumer apps, education, healthcare, content-heavy products
**Pros**: Comfortable for longer reading. Feels more human than geometric sans.
**Cons**: Less precise/technical feeling. Can look soft in data-heavy contexts.
**CSS**: `font-family: 'Source Sans 3', 'Nunito', 'Segoe UI', sans-serif;`

### Neo-Grotesque

**Examples**: Helvetica, Arial, Roboto, Helvetica Neue
**Character**: Neutral, corporate, ubiquitous. Based on 19th-century grotesque designs.
**Best for**: Enterprise software, corporate products, when neutrality is paramount
**Pros**: Universally readable. No personality to clash with content.
**Cons**: Boring. Overused. Arial is the "default" look of undesigned software.
**CSS**: `font-family: 'Helvetica Neue', 'Roboto', 'Arial', sans-serif;`

### Monospace

**Examples**: JetBrains Mono, Fira Code, Berkeley Mono, Geist Mono, SF Mono
**Character**: Technical, precise, code-native. Fixed-width characters.
**Best for**: Code editors, terminals, data tables with numbers, developer tools
**Pros**: Characters align vertically. Code ligatures (→, !=, >=). Tabular numbers by default.
**Cons**: Less readable for prose (25% wider than proportional fonts). Uses more horizontal space.
**CSS**: `font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', 'Cascadia Code', monospace;`

### Serif

**Examples**: Georgia, Source Serif 4, Charter, Merriweather, Literata, New York (NY)
**Character**: Editorial, authoritative, literary. Serifs aid horizontal reading flow.
**Best for**: Long-form content, editorial products, documentation, legal/financial
**Pros**: Excellent readability for long texts. Creates instant editorial/premium feeling.
**Cons**: Can feel old-fashioned in modern app UI. Heavier rendering at small sizes on low-res screens.
**CSS**: `font-family: 'Source Serif 4', 'Charter', 'Georgia', serif;`

### When to Use Each in UI

| Context | Recommended Classification | Example Font |
|---|---|---|
| Product UI (SaaS, tools) | Geometric sans | Inter, Geist |
| Consumer app (social, lifestyle) | Humanist sans | Source Sans 3, Nunito |
| Enterprise/corporate | Neo-grotesque | Roboto, Helvetica Neue |
| Code/data display | Monospace | JetBrains Mono, Geist Mono |
| Long-form reading | Serif | Source Serif 4, Literata |
| Marketing/hero sections | Display/geometric | Clash Display, Cabinet Grotesk |
| iOS native | System | SF Pro (auto-selected) |
| Android native | System | Roboto (or Google Sans for brand) |

---

## Variable Fonts

### What Are Variable Fonts?

A single font file containing the entire design space across one or more axes. Instead of loading `Inter-Regular.woff2`, `Inter-Medium.woff2`, `Inter-SemiBold.woff2` separately, one `Inter-Variable.woff2` contains all weights.

### Standard Axes

| Axis | Tag | Range | Use |
|---|---|---|---|
| Weight | `wght` | 100-900 | Most common. Replaces separate weight files. |
| Width | `wdth` | 75-125 | Condensed to expanded. Space optimization. |
| Optical size | `opsz` | 8-144 | Adjusts letterform detail for size. Critical for quality. |
| Italic | `ital` | 0-1 | On/off italic. |
| Slant | `slnt` | -12 to 0 | Continuous slant angle. |

### CSS Usage

```css
/* Modern approach: use font-weight directly */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Variable.woff2') format('woff2');
  font-weight: 100 900;  /* Full range */
  font-display: swap;
}

body { font-weight: 400; }        /* Regular */
.label { font-weight: 500; }      /* Medium */
.heading { font-weight: 600; }    /* Semibold */

/* Optical sizing (auto-adjusts letterforms for size) */
.heading-display {
  font-size: 48px;
  font-optical-sizing: auto;  /* Browser adjusts opsz axis */
}

/* Manual axis control for advanced use */
.custom {
  font-variation-settings: 'wght' 450, 'wdth' 95;
}
```

### Performance Benefits

- **Before variable fonts**: 6 weight files × 2 (italic) = 12 files, ~360KB total
- **After variable fonts**: 1 file, ~100-160KB
- **Savings**: 55-70% file size reduction
- **Benefit**: Can use ANY weight (not just 400, 500, 600, 700 — use 450, 550, or animate between)

### Top Variable Fonts for UI

| Font | Axes | File Size | Notes |
|---|---|---|---|
| **Inter** | wght (100-900), opsz | ~300KB | The UI font. Tabular nums, slashed zero, contextual alts. |
| **Geist Sans** | wght (100-900) | ~120KB | Vercel's font. Clean, slightly narrower than Inter. |
| **Geist Mono** | wght (100-900) | ~100KB | Pairs with Geist Sans. Code ligatures. |
| **Source Sans 3** | wght (200-900), ital | ~200KB | Adobe's UI font. Humanist. Excellent i18n support. |
| **Outfit** | wght (100-900) | ~80KB | Geometric, friendly. Good for consumer apps. |
| **JetBrains Mono** | wght (100-800) | ~150KB | Best monospace for code. Ligatures, height-matched. |

### Optical Sizing: Why It Matters

At 12px, letterforms need:
- **Open counters** (bigger internal spaces in letters like 'e', 'a')
- **Wider spacing** (more tracking)
- **Thicker strokes** (thin strokes disappear at small sizes)

At 48px, letterforms need:
- **Tighter counters** (proportions look elegant)
- **Tighter spacing** (tracking can be negative)
- **Thinner strokes** (details are visible, thick strokes look crude)

Inter and SF Pro handle this automatically when `font-optical-sizing: auto` is set. Without it, small text looks cramped and large text looks loose.

---

## Type Scale Systems

### Modular Scales

| Ratio | Name | Character | Best For |
|---|---|---|---|
| 1.125 | Major second | Very tight. Many sizes. | Dense data UIs, toolbars |
| 1.200 | Minor third | Moderate. Good range. | Content-heavy products, dashboards |
| 1.250 | Major third | Balanced. Clear hierarchy. | General product UI (most common) |
| 1.333 | Perfect fourth | Dramatic. Bold hierarchy. | Marketing sites, landing pages |
| 1.500 | Perfect fifth | Very dramatic. | Editorial, headlines-first |
| 1.618 | Golden ratio | Maximum drama. | Art direction, hero typography |

### Generating a Scale

Base: 16px, Ratio: 1.25 (major third)

```
Step -2: 16 / 1.25 / 1.25 = 10.24 → 10px (caption-sm)
Step -1: 16 / 1.25 = 12.8 → 13px (caption)
Step  0: 16px (body)
Step +1: 16 × 1.25 = 20px (body-lg / h4)
Step +2: 16 × 1.25² = 25px (h3)
Step +3: 16 × 1.25³ = 31.25 → 31px (h2)
Step +4: 16 × 1.25⁴ = 39.06 → 39px (h1)
Step +5: 16 × 1.25⁵ = 48.83 → 49px (display)
Step +6: 16 × 1.25⁶ = 61.04 → 61px (display-lg)
```

### Fluid Typography with CSS clamp()

Scale type fluidly between viewport sizes without breakpoints:

```css
:root {
  /* clamp(min, preferred, max) */
  /* preferred: base + viewport-relative growth */
  --text-body:    clamp(1rem, 0.95rem + 0.25vw, 1.125rem);        /* 16-18px */
  --text-lg:      clamp(1.125rem, 1rem + 0.5vw, 1.25rem);         /* 18-20px */
  --text-h3:      clamp(1.25rem, 1rem + 1vw, 1.563rem);           /* 20-25px */
  --text-h2:      clamp(1.5rem, 1.1rem + 1.5vw, 1.953rem);       /* 24-31px */
  --text-h1:      clamp(1.875rem, 1.2rem + 2.5vw, 2.441rem);     /* 30-39px */
  --text-display:  clamp(2.25rem, 1.5rem + 3vw, 3.052rem);       /* 36-49px */
}
```

**Formula for clamp preferred value**: `(min_size / 16) + (max_size - min_size) / (max_viewport - min_viewport) * 100vw`

Where min viewport = 375px, max viewport = 1440px.

### Material 3 Type Scale

5 roles × 3 sizes = 15 type styles:

| Role | Large | Medium | Small |
|---|---|---|---|
| **Display** | 57/64 regular | 45/52 regular | 36/44 regular |
| **Headline** | 32/40 regular | 28/36 regular | 24/32 regular |
| **Title** | 22/28 medium | 16/24 medium | 14/20 medium |
| **Body** | 16/24 regular | 14/20 regular | 12/16 regular |
| **Label** | 14/20 medium | 12/16 medium | 11/16 medium |

Format: size/line-height weight. All sizes in sp (Android) ≈ px (web at 1x).

### Apple Dynamic Type (11 text styles)

| Style | Default Size | Min (accessibility) | Max (accessibility) |
|---|---|---|---|
| Large Title | 34pt | 34pt | 40pt |
| Title 1 | 28pt | 25pt | 36pt |
| Title 2 | 22pt | 19pt | 28pt |
| Title 3 | 20pt | 17pt | 26pt |
| Headline | 17pt bold | 14pt | 24pt |
| Body | 17pt | 14pt | 24pt |
| Callout | 16pt | 13pt | 22pt |
| Subhead | 15pt | 12pt | 21pt |
| Footnote | 13pt | 12pt | 19pt |
| Caption 1 | 12pt | 11pt | 18pt |
| Caption 2 | 11pt | 11pt | 17pt |

---

## Font Pairing Rules

### Strategy 1: Superfamily Pairing

Use fonts from the same family or designer that were designed to work together.

| Sans | Serif/Mono | Notes |
|---|---|---|
| Inter | Inter Display | Same family, different optical sizing |
| Geist Sans | Geist Mono | Same design language |
| Source Sans 3 | Source Serif 4 | Same designer (Paul Hunt), matched x-height |
| SF Pro | New York (NY) | Both Apple system fonts, harmonized metrics |
| IBM Plex Sans | IBM Plex Serif + Plex Mono | Complete family system |
| Noto Sans | Noto Serif + Noto Mono | Google's universal language coverage |

### Strategy 2: Contrast Pairing

Pair fonts with DIFFERENT classification but SHARED metrics (x-height, cap height).

**Rules**:
1. Different classification: sans + serif, or sans + mono
2. Similar x-height (the height of lowercase 'x')
3. Similar cap height (the height of uppercase letters)
4. Different personality (one neutral, one expressive)

| Primary (headings) | Secondary (body) | Character |
|---|---|---|
| Clash Display | Inter | Bold/editorial headings + clean body |
| Cabinet Grotesk | Source Serif 4 | Geometric headlines + readable prose |
| General Sans | Literata | Modern headlines + book-like reading |

### Strategy 3: One Font, Multiple Weights

The safest and most consistent approach for product UI.

```css
/* One font covers everything */
:root {
  --font-family: 'Inter', system-ui, sans-serif;
  --font-weight-regular: 400;   /* Body text */
  --font-weight-medium: 500;    /* Labels, UI elements */
  --font-weight-semibold: 600;  /* Headings, emphasis */
  --font-weight-bold: 700;      /* Primary headings only */
}
```

Create hierarchy through size, weight, and color — not through font family changes.

### Anti-Patterns

1. **Two similar sans-serifs** (Inter + Roboto): Too similar. Users see inconsistency, not intentional contrast.
2. **Decorative + decorative** (Playfair Display + Lobster): Competing personalities. Neither can lead.
3. **More than 3 families**: Increases file size, reduces coherence, creates visual noise.
4. **Mismatched x-heights**: If the sans x-height is visually taller than the serif, mixed-family paragraphs look bumpy.

---

## Typographic Hierarchy System

### The 6-Level System

| Level | Role | Size (desktop) | Weight | Line-height | Tracking | Color |
|---|---|---|---|---|---|---|
| **Display** | Hero headlines, marketing | 48-72px | 700-800 | 1.05-1.1 | -0.02em to -0.03em | text-primary |
| **H1** | Page titles | 32-40px | 700 | 1.15-1.2 | -0.015em | text-primary |
| **H2** | Section headings | 24-28px | 600 | 1.2-1.25 | -0.01em | text-primary |
| **H3** | Subsection headings | 20-22px | 600 | 1.25-1.3 | -0.005em | text-primary |
| **Body** | Paragraph text, UI text | 16px | 400 | 1.5-1.6 | 0 | text-primary |
| **Caption** | Helper text, metadata | 12-14px | 400-500 | 1.3-1.4 | +0.01em | text-secondary |

### Creating Distinction Without Size

When you can't increase size (space-constrained UI), use:

1. **Weight contrast**: 400 (body) vs 600 (heading) — 2 steps minimum
2. **Color contrast**: text-primary (#111827) vs text-secondary (#6B7280)
3. **Case**: UPPERCASE with letter-spacing (+0.05em) for labels — use sparingly
4. **Font family**: Mono for data, sans for labels
5. **Position**: Top = primary, inline = secondary

### Platform Conventions

**iOS (Dynamic Type)**:
- Use system text styles: .largeTitle, .title1, .body, .caption1
- Support Dynamic Type scaling (never hardcode point sizes)
- SF Pro automatically switches between Display and Text variants

**Android (Material type scale)**:
- Use MaterialTheme.typography styles: displayLarge, headlineMedium, bodyLarge
- Roboto as default, Google Sans for branded moments
- sp units scale with user font size preference

**Web (Fluid type)**:
- Use clamp() for responsive scaling
- Rem units for user font-size respect
- CSS custom properties for system consistency

---

## Line-Height & Measure

### Line-Height Rules

```css
/* Line-height decreases as font-size increases */
--lh-display: 1.05;    /* 48-72px: almost touching */
--lh-h1: 1.15;         /* 32-40px: tight */
--lh-h2: 1.2;          /* 24-28px: snug */
--lh-h3: 1.25;         /* 20-22px: comfortable-snug */
--lh-body: 1.5;        /* 14-18px: comfortable reading */
--lh-body-lg: 1.6;     /* Long-form at wide measure */
--lh-caption: 1.35;    /* 12-14px: slightly tight */
```

**Why unitless line-height**: `line-height: 1.5` multiplies by the element's own font-size. `line-height: 24px` is fixed regardless of font-size. Unitless is almost always better because it scales with the text.

### Measure (Line Length) Rules

```css
/* Optimal line length per content type */
--measure-prose: 65ch;    /* 45-75ch ideal for body text */
--measure-ui: 45ch;       /* Shorter for UI descriptions */
--measure-wide: 80ch;     /* Code blocks, data tables */
--measure-narrow: 35ch;   /* Captions, pull quotes, sidebars */
```

**Interaction**: Longer measure needs more line-height:
- 45ch measure → line-height: 1.4 is fine
- 65ch measure → line-height: 1.5-1.6 needed
- 80ch measure → line-height: 1.6-1.7 (or use columns)

---

## Text Rendering

### macOS Antialiasing

```css
/* Use antialiased rendering on macOS */
body {
  -webkit-font-smoothing: antialiased;  /* macOS: thinner, crisper text */
  -moz-osx-font-smoothing: grayscale;   /* Firefox macOS */
}
```

**When to use**: Almost always on macOS. The default (subpixel antialiasing) makes text look heavier than intended, especially on Retina displays. Apple removed subpixel antialiasing in macOS Mojave, but the CSS property still affects rendering.

**Exception**: Very small text (<12px) on non-Retina displays benefits from subpixel rendering.

### Font Display Strategies

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Variable.woff2') format('woff2');

  /* font-display options: */
  font-display: swap;      /* Show fallback immediately, swap when loaded. Best for body text. */
  font-display: optional;  /* Use if loaded within 100ms, else skip. Best for non-critical. */
  font-display: fallback;  /* Short block period, then swap. Middle ground. */
}
```

**Recommendation**: `swap` for primary body font (users see text immediately). `optional` for decorative/display fonts (no layout shift if it doesn't load).

### Web Font Loading Performance

1. **Preload** critical fonts:
   ```html
   <link rel="preload" href="/fonts/Inter-Variable.woff2" as="font" type="font/woff2" crossorigin>
   ```

2. **Subset** fonts to used character ranges:
   ```css
   @font-face {
     unicode-range: U+0000-00FF, U+0131, U+0152-0153; /* Latin */
   }
   ```

3. **Self-host** over Google Fonts for performance (eliminates DNS lookup + extra connection).

4. **Size budget**: Total web fonts <150KB for fast loading. Variable fonts help here.

### System Font Stack (Zero-Load Alternative)

```css
/* Modern system font stack — instant rendering, no download */
font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI',
  Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans',
  'Helvetica Neue', Arial, sans-serif;

/* Monospace system stack */
font-family: ui-monospace, 'Cascadia Code', 'Source Code Pro',
  Menlo, Consolas, 'DejaVu Sans Mono', monospace;
```

**Result**: SF Pro on Apple, Segoe UI on Windows, Roboto on Android. Instant rendering, zero download.

---

## Responsive Typography

### Fluid Type with clamp()

```css
/* Complete responsive type scale */
:root {
  --text-xs:     clamp(0.75rem, 0.7rem + 0.15vw, 0.8rem);     /* 12-12.8px */
  --text-sm:     clamp(0.813rem, 0.76rem + 0.2vw, 0.875rem);   /* 13-14px */
  --text-base:   clamp(1rem, 0.95rem + 0.25vw, 1.125rem);      /* 16-18px */
  --text-lg:     clamp(1.125rem, 1rem + 0.5vw, 1.25rem);       /* 18-20px */
  --text-xl:     clamp(1.25rem, 1.05rem + 0.85vw, 1.563rem);   /* 20-25px */
  --text-2xl:    clamp(1.5rem, 1.15rem + 1.35vw, 1.953rem);    /* 24-31px */
  --text-3xl:    clamp(1.875rem, 1.3rem + 2.2vw, 2.441rem);    /* 30-39px */
  --text-4xl:    clamp(2.25rem, 1.4rem + 3.3vw, 3.052rem);     /* 36-49px */
  --text-5xl:    clamp(2.5rem, 1.2rem + 5vw, 3.815rem);        /* 40-61px */
}
```

### Mobile Adjustments

On mobile (375-428px viewports):
- **Reduce display sizes**: Desktop 48px → Mobile 32px (or fluid via clamp)
- **Maintain body size**: 16px minimum (never go below on mobile)
- **Tighten heading line-height**: Mobile h1 at 1.1 (less space between lines on small screens)
- **Reduce heading weights**: Desktop H1 at 700 → Mobile at 600 (bold looks heavier on small screens)
- **Increase touch-target text**: Button text minimum 16px for comfortable reading within tap targets

### Touch vs. Pointer Adjustments

```css
/* Adjust for touch devices */
@media (pointer: coarse) {
  :root {
    --text-base: max(1rem, 16px);  /* Ensure 16px minimum */
    --lh-body: 1.6;                /* Slightly more line-height for fat-finger taps */
  }

  /* Link text needs adequate size for tapping */
  a { min-height: 44px; display: inline-flex; align-items: center; }
}
```

---

## Platform-Specific Type Stacks

### iOS

```swift
// SF Pro: auto-switches between Display (≥20pt) and Text (<20pt)
// Display variant: tighter spacing, refined details for large sizes
// Text variant: open spacing, robust details for small sizes

.font(.title)           // SF Pro 28pt
.font(.headline)        // SF Pro 17pt Semibold
.font(.body)            // SF Pro 17pt Regular
.font(.caption)         // SF Pro 12pt Regular

// SF Mono for code
.font(.system(.body, design: .monospaced))
```

### Android

```kotlin
// Material 3 type scale
MaterialTheme.typography.displayLarge   // Roboto 57/64 Regular
MaterialTheme.typography.headlineMedium // Roboto 28/36 Regular
MaterialTheme.typography.bodyLarge      // Roboto 16/24 Regular
MaterialTheme.typography.labelSmall     // Roboto 11/16 Medium
```

### Web — Inter as Universal UI Font

```css
/* Inter: the closest thing to a universal UI font */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Variable.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
  font-feature-settings: 'cv01' 1, 'cv02' 1;  /* Alt letterforms */
}

:root {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  font-feature-settings: 'liga' 1, 'calt' 1;  /* Ligatures, contextual alts */
  font-optical-sizing: auto;
}

/* Tabular numbers for data */
.data-value { font-variant-numeric: tabular-nums; }

/* Slashed zero for code-adjacent contexts */
.code-ref { font-feature-settings: 'zero' 1; }
```

**Why Inter**: Designed specifically for computer screens. Optimized for 11-16px sizes. Tabular numbers, slashed zero, contextual alternates. 2 axes (weight + optical size). Free and open source. 9 weights. Used by Linear, Figma, and hundreds of products.
