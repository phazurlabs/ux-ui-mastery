# Spacing Rhythm System

Complete spacing, rhythm, and layout systems for page composition. Defines the vertical and horizontal spacing rules that create visual rhythm, readability, and hierarchy across all page types.

---

## Section Spacing Scale

A 6-step scale for vertical space between major page sections. Based on an 8px base unit with contextual naming.

| Token   | Value  | Use Case                                                          |
|---------|--------|-------------------------------------------------------------------|
| `xs`    | 32px   | Tight coupling: filter bar to content, label to field group       |
| `sm`    | 48px   | Related sections: social proof below hero, sub-sections           |
| `md`    | 64px   | Default between standard sections on content-dense pages          |
| `lg`    | 96px   | Primary section separation on marketing pages                     |
| `xl`    | 128px  | Breathing room after dense content, before CTA sections           |
| `2xl`   | 160px  | Maximum separation: hero bottom padding, dramatic pauses          |

### When to Use Each Level

**xs (32px) — "Tight bond"**
Use when two elements are semantically part of the same group:
- Filter bar above a list of results
- Section subtitle beneath section title
- Form field groups within a form section
- Breadcrumb above page content
- Active filter chips below filter bar

**sm (48px) — "Related siblings"**
Use when elements are clearly related but need visual distinction:
- Social proof bar directly below hero (trust enhances hero promise)
- Stats row below a testimonial section
- "Powered by" or trust badges below a form
- Sub-sections within a larger section group
- Mobile section spacing (replacing lg)

**md (64px) — "Standard rhythm"**
The default spacing for app pages and content-dense layouts:
- Between card groups on dashboards
- Between form sections on settings pages
- Between content blocks in documentation
- Tablet section spacing (replacing lg)
- Between secondary content blocks on marketing pages

**lg (96px) — "Clear separation"**
The workhorse spacing for marketing pages:
- Between hero and first content section
- Between any two primary marketing sections (features, testimonials, pricing)
- Between main content sections on landing pages
- Between FAQ and footer
- Desktop default for most section transitions

**xl (128px) — "Breathing room"**
Use after visually dense sections or before high-importance sections:
- After a complex feature grid, before a simple CTA
- Before the pricing section (give users space to process)
- Before the final CTA section
- After a data-heavy comparison table
- Between major thematic shifts on a page

**2xl (160px) — "Dramatic pause"**
Use sparingly for maximum visual impact:
- Hero section internal padding (top and bottom)
- Full-viewport hero spacing
- Before the "grand reveal" section
- Agency/portfolio testimonial sections with single large quote
- Contact CTA sections that need maximum visual weight

---

## Block Stacking Rhythm Rules

### The Alternation Principle

Never stack two visually identical blocks back-to-back. Alternate between:
- Dense ↔ Light
- Dark background ↔ Light background
- Text-heavy ↔ Visual-heavy
- Wide (full-bleed) ↔ Narrow (contained)

### Visual Weight Mapping

Assign weight to each section type to plan rhythm:

| Section Type          | Visual Weight | Density    |
|-----------------------|---------------|------------|
| Hero (text + image)   | Heavy         | Medium     |
| Social proof bar      | Light         | Low        |
| Feature grid (3-col)  | Heavy         | High       |
| Alternating rows      | Medium        | Medium     |
| Stats/metrics row     | Light         | Low        |
| Testimonial cards     | Medium        | Medium     |
| Single large quote    | Light         | Low        |
| Pricing table         | Heavy         | High       |
| FAQ accordion         | Medium        | Medium     |
| CTA banner            | Light         | Low        |
| Image gallery         | Heavy         | High       |
| Video embed           | Medium        | Medium     |
| Team grid             | Medium        | Medium     |
| Footer                | Medium        | High       |

### Ideal Weight Sequence

Follow a **Heavy → Light → Heavy → Light** pattern:
```
HERO (heavy) → Social Proof (light) → Features (heavy) → Stats (light) → Testimonials (medium) → CTA (light) → Pricing (heavy) → FAQ (medium) → CTA (light) → Footer
```

### Background Color Rhythm

Use background alternation to reinforce section boundaries:

**Marketing page pattern:**
```
Section 1:  white          (hero)
Section 2:  gray-50        (social proof)
Section 3:  white          (features)
Section 4:  gray-50        (how it works)
Section 5:  white          (testimonials)
Section 6:  primary-950    (stats/CTA — dark accent)
Section 7:  white          (pricing)
Section 8:  gray-50        (FAQ)
Section 9:  primary-900    (final CTA — dark)
Section 10: gray-950       (footer — darkest)
```

**Rules for background alternation:**
1. Never use the same background for 3+ consecutive sections
2. Dark sections (primary-900/950) appear 1-2 times max per page
3. Dark sections are reserved for CTA/conversion moments or stats
4. gray-50 is the neutral separator — use it for supporting content
5. The footer is always the darkest section on the page
6. White sections carry the primary content (features, pricing, testimonials)

---

## Visual Rhythm Patterns

Named patterns for the vertical pacing of a page, inspired by musical rhythm.

### AABA Pattern — "Verse-Chorus"

The most common marketing page rhythm. Three standard sections followed by a contrasting accent.

```
A: Standard section (white bg, lg spacing)
A: Standard section (gray-50 bg, lg spacing)
B: Accent section (dark bg, different density)
A: Standard section (white bg, lg spacing)
```

**Example applied:**
```
A: Features grid (white, lg)
A: How It Works (gray-50, lg)
B: Stats/metrics (primary-950, md) ← visual break
A: Testimonials (white, lg)
```

Use when: You need to break monotony every 3-4 sections. The B section refreshes attention and serves as a visual landmark.

### ABAB Pattern — "Steady Alternation"

Consistent back-and-forth between two styles. Creates predictable, easy-to-scan rhythm.

```
A: Content section (white bg)
B: Supporting section (gray-50 bg)
A: Content section (white bg)
B: Supporting section (gray-50 bg)
```

**Example applied:**
```
A: Hero (white)
B: Social proof (gray-50)
A: Features (white)
B: Testimonials (gray-50)
A: Pricing (white)
B: FAQ (gray-50)
```

Use when: Content is uniform in density and importance. Works well for documentation, help centers, and straightforward marketing pages.

### Crescendo Pattern — "Building to Climax"

Sections increase in visual weight and urgency toward the page's climax (usually pricing or CTA).

```
Light → Light → Medium → Medium → Heavy → PEAK
```

**Spacing progression:**
```
Section 1:  lg spacing (96px)      — gentle start
Section 2:  lg spacing (96px)      — building
Section 3:  md spacing (64px)      — tightening
Section 4:  md spacing (64px)      — momentum
Section 5:  sm spacing (48px)      — urgency
Section 6:  PEAK (dark bg, xl top padding for drama)
```

**Example applied:**
```
Hero (light, lg)
Social proof (light, lg)
Features overview (medium, md)
Detailed features (medium, md)
Testimonials (medium, sm)
PRICING + CTA (heavy, peak moment)
```

Use when: The page has a clear conversion goal and you want to build psychological momentum toward it.

### Decrescendo Pattern — "Wind Down"

After a peak moment, sections gradually become lighter and less urgent. Used for the back half of long pages.

```
PEAK → Heavy → Medium → Light → Light
```

**Example applied (post-pricing):**
```
Pricing (peak) → FAQ (medium) → Blog/Resources (light) → Newsletter signup (light) → Footer
```

Use when: The main conversion moment is in the middle of the page, and remaining content is supplementary.

### Sandwich Pattern — "Bookend"

Strong opening, lighter middle, strong close. The most conversion-optimized pattern.

```
STRONG (hero + proof) → light → medium → light → medium → STRONG (CTA)
```

Use when: You want maximum impact at both the start and end of the scroll journey. The middle sections are evidence-building.

---

## Responsive Spacing Reduction Formula

Section spacing must decrease on smaller screens to prevent excessive scrolling while maintaining rhythm.

### Reduction Table

| Breakpoint       | Width         | Reduction | Resulting Scale                    |
|------------------|---------------|-----------|------------------------------------|
| Desktop (XL)     | 1440px+       | 0%        | xs:32 sm:48 md:64 lg:96 xl:128 2xl:160 |
| Desktop (L)      | 1280-1439px   | 0%        | Same as XL                         |
| Desktop (M)      | 1024-1279px   | ~12%      | xs:28 sm:40 md:56 lg:84 xl:112 2xl:140 |
| Tablet           | 768-1023px    | ~25%      | xs:24 sm:36 md:48 lg:72 xl:96 2xl:120  |
| Mobile (L)       | 430-767px     | ~40%      | xs:20 sm:32 md:40 lg:56 xl:72 2xl:96   |
| Mobile (S)       | 375-429px     | ~50%      | xs:16 sm:24 md:32 lg:48 xl:64 2xl:80   |
| Mobile (XS)      | < 375px       | ~55%      | xs:16 sm:24 md:28 lg:40 xl:56 2xl:72   |

### CSS Implementation

```css
:root {
  /* Desktop defaults */
  --section-xs:  32px;
  --section-sm:  48px;
  --section-md:  64px;
  --section-lg:  96px;
  --section-xl:  128px;
  --section-2xl: 160px;
}

@media (max-width: 1023px) {
  :root {
    --section-xs:  24px;
    --section-sm:  36px;
    --section-md:  48px;
    --section-lg:  72px;
    --section-xl:  96px;
    --section-2xl: 120px;
  }
}

@media (max-width: 767px) {
  :root {
    --section-xs:  20px;
    --section-sm:  32px;
    --section-md:  40px;
    --section-lg:  56px;
    --section-xl:  72px;
    --section-2xl: 96px;
  }
}

@media (max-width: 429px) {
  :root {
    --section-xs:  16px;
    --section-sm:  24px;
    --section-md:  32px;
    --section-lg:  48px;
    --section-xl:  64px;
    --section-2xl: 80px;
  }
}
```

### Fluid Spacing (Modern CSS)

For smooth scaling without breakpoint jumps:
```css
:root {
  --section-lg: clamp(48px, 4vw + 24px, 96px);
  --section-xl: clamp(64px, 5.5vw + 24px, 128px);
  --section-2xl: clamp(80px, 7vw + 24px, 160px);
}
```

### Rules for Responsive Spacing
1. Never reduce spacing below 16px between sections (minimum readable separation)
2. Reduce spacing proportionally — don't collapse all levels to the same value
3. On mobile, the difference between `md` and `lg` may be only 8-16px — this is acceptable
4. Internal card/component padding reduces less aggressively than section spacing
5. Hero sections keep proportionally more space than utility sections

---

## Container Width Strategy

### Container Types

| Container     | Max-Width | Use Case                                           |
|---------------|-----------|-----------------------------------------------------|
| Full-bleed    | 100%      | Hero backgrounds, dark sections, image galleries    |
| Wide          | 1440px    | Dashboard layouts, wide content areas               |
| Standard      | 1280px    | Most marketing page content                         |
| Content       | 1120px    | Feature grids, pricing tables                       |
| Narrow        | 720-800px | Blog posts, FAQ, forms, text-heavy content          |
| Ultra-narrow  | 480-560px | Auth forms, single-column settings, email capture   |

### Nesting Pattern

Sections use full-bleed backgrounds with contained content:
```
<section style="background: gray-50; padding: 96px 0;">
  <!-- Full-bleed background -->
  <div style="max-width: 1280px; margin: 0 auto; padding: 0 24px;">
    <!-- Contained content -->
  </div>
</section>
```

### Container Padding (Horizontal)

| Breakpoint   | Container Side Padding |
|--------------|------------------------|
| Desktop      | 24-32px                |
| Tablet       | 24px                   |
| Mobile (L)   | 20px                   |
| Mobile (S)   | 16px                   |

### Mixed Container Widths on One Page

Different sections can use different container widths for variety:
```
Hero:            Standard (1280px) — balanced
Social proof:    Wide (1440px) — logos spread out
Features:        Content (1120px) — focused reading
Testimonials:    Narrow (800px) — intimate, centered quotes
Pricing:         Content (1120px) — table needs width
FAQ:             Narrow (720px) — single column reading
CTA:             Standard (1280px) — matches hero
```

This width variation creates natural rhythm and prevents the page from feeling like a uniform column.

---

## Grid Systems for Page Composition

### 12-Column Grid

The standard grid for most web layouts.

```
Desktop (1280px container):
  Column width: ~85px
  Gutter: 24px (or 32px for spacious layouts)
  Total gutters: 11 × 24px = 264px
  Total columns: 12 × 85px = 1016px
  Total: 1280px

Common column spans:
  Full width:     12 columns (1280px)
  Two-thirds:     8 columns  (~853px)
  Half:           6 columns  (~640px)
  Third:          4 columns  (~427px)
  Quarter:        3 columns  (~320px)
  Sidebar:        3-4 columns (320-427px)
  Main content:   8-9 columns (853-960px)
```

### CSS Grid Implementation

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 24px;
}

/* Common layouts */
.span-full    { grid-column: span 12; }
.span-half    { grid-column: span 6; }
.span-third   { grid-column: span 4; }
.span-quarter { grid-column: span 3; }
.span-two-thirds { grid-column: span 8; }

/* Responsive */
@media (max-width: 1023px) {
  .grid-container { grid-template-columns: repeat(8, 1fr); }
  .span-third { grid-column: span 4; } /* becomes half */
}

@media (max-width: 767px) {
  .grid-container { grid-template-columns: repeat(4, 1fr); gap: 16px; }
  .span-half, .span-third, .span-quarter { grid-column: span 4; } /* full width */
}
```

### Responsive Grid Collapse

| Layout        | Desktop (12-col) | Tablet (8-col) | Mobile (4-col) |
|---------------|-------------------|----------------|----------------|
| 4-col cards   | 3+3+3+3           | 4+4 (2-col)    | 4 (1-col)      |
| 3-col cards   | 4+4+4             | 4+4+8 (2+1)    | 4 (1-col)      |
| 2-col split   | 6+6               | 4+4 (equal)    | 4 (stacked)    |
| Main+sidebar  | 8+4               | 5+3            | 4 (stacked)    |
| Narrow content| 3+6+3 (centered)  | 1+6+1          | 4 (full)       |

### Asymmetric Grids

For more dynamic, editorial layouts:

**Golden ratio split (61.8% / 38.2%):**
```css
.golden-split {
  display: grid;
  grid-template-columns: 1fr 0.618fr;
  gap: 48px;
}
```
Use for: hero sections, detail page main+sidebar

**Rule of thirds (33% / 67%):**
```css
.thirds-split {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 32px;
}
```
Use for: settings page nav+content, documentation sidebar+content

**Offset grid (for editorial/creative pages):**
```css
.offset-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 2fr;
  gap: 16px;
}
```
Use for: portfolio/agency work grids, magazine-style content

---

## Z-Pattern and F-Pattern Layouts

### F-Pattern Layout

Users scan content-heavy pages in an F-shape: strong horizontal scan at top, weaker scan in middle, vertical scan down the left side.

**Optimized block placement for F-pattern:**
```
┌─────────────────────────────────────────┐
│ ██████████████████████████████████████  │ ← Strong horizontal: Hero headline
│ ████████████████████                    │ ← Second scan: Subheading
│ ██████                                  │ ← Vertical scan begins
│ ██████                                  │
│ ██ Feature 1 title   [image]            │ ← Titles on left, images on right
│ ██ Feature 2 title   [image]            │
│ ██ Feature 3 title   [image]            │
│ ██████████████                          │ ← CTA catches descending eye
└─────────────────────────────────────────┘
```

**Rules for F-pattern pages:**
1. Most important content in the first two horizontal scan lines (hero)
2. Start each section with a strong left-aligned heading
3. Place key information at the start of each line (left side)
4. Use bold text, bullets, and short paragraphs to catch the vertical scan
5. Break the F-pattern with a full-width element every 3-4 sections to reset scanning

**Best for:** Text-heavy pages (blog, documentation, FAQ, feature lists, settings)

### Z-Pattern Layout

Users scan visual/sparse pages in a Z-shape: top-left → top-right → diagonal down → bottom-left → bottom-right.

**Optimized block placement for Z-pattern:**
```
┌─────────────────────────────────────────┐
│ [Logo]              [Nav]    [CTA btn]  │ ← Top scan: brand → navigation → action
│                                         │
│                                         │
│    Headline text           [Hero image] │ ← Z diagonal: text → visual
│    Subheading                           │
│    [Primary CTA]                        │
│                                         │
│                ↘                        │ ← Diagonal eye movement
│                                         │
│ [Feature 1]    [Feature 2]   [Feature 3]│ ← Bottom scan: left to right
│                                         │
│ [Social proof across full width]        │ ← Restart Z
│                                         │
│    Testimonial text        [Photo]      │ ← Second Z: text → visual
│    [Secondary CTA]                      │
│                                         │
│ [Trust badges]            [Final CTA]   │ ← Z end: trust → action
└─────────────────────────────────────────┘
```

**Rules for Z-pattern pages:**
1. Top-left: logo/brand (first fixation point)
2. Top-right: primary CTA or navigation endpoint
3. Center: hero content (catches the diagonal)
4. Bottom-left: supporting content start
5. Bottom-right: conversion point (CTA button)
6. Each "Z" resets with a full-width element (social proof bar, stats row)

**Best for:** Landing pages, marketing pages, sparse layouts with clear visual hierarchy

### Combined Pattern Strategy

Most pages use BOTH patterns at different scales:
- **Page level:** Z-pattern (hero → features → CTA)
- **Section level:** F-pattern (heading → body text → details)

```
PAGE LEVEL (Z-pattern):
  Z1: Hero section (logo TL → CTA TR → headline center → proof BL → action BR)
  Z2: Features section (title TL → features across → CTA BR)
  Z3: Social proof → Pricing → Final CTA

SECTION LEVEL (F-pattern within each Z zone):
  Feature section:
    F: Section title (strong first line)
    F: Feature 1 description (second line)
    |  Feature 2 description (vertical scan)
    |  Feature 3 description
```

---

## Spacing Cheat Sheet

Quick reference for common spacing decisions.

### Marketing Page Defaults
```
Nav height:              64px
Hero padding:            96-160px vertical
Between sections:        96px (lg)
Social proof padding:    48px (sm)
CTA section padding:     96-128px
Footer padding:          64px top, 32px bottom
Container max-width:     1280px
Container side padding:  24-32px
```

### App Page Defaults
```
Top bar height:          56-64px
Sidebar width:           256px (collapsed: 64px)
Page padding:            24px (16px mobile)
Between card groups:     24px
Card internal padding:   24px (20px compact)
Card border-radius:      12px
Card gap:                16-24px
Form field gap:          20-24px
```

### Typography Spacing
```
H1 margin-bottom:       24px
H2 margin-bottom:       20px
H3 margin-bottom:       16px
Paragraph margin-bottom: 16px
List item gap:           8px
Section title to content: 32-48px
```

### Interactive Element Spacing
```
Button height:           40px (default), 48px (large), 32px (small)
Button padding:          12px 24px
Button gap (side by side): 12px
Input height:            40px (default), 48px (large)
Input padding:           12px 16px
Checkbox/radio gap:      12px between options
Form section gap:        32px
```

---

## Rhythm Diagnostics

### Signs of Poor Spacing Rhythm

1. **Wall of sameness:** Every section has identical padding — no breathing room variation
2. **Cramped transitions:** Sections feel like they collide — missing background alternation
3. **Desert gaps:** Excessive spacing making content feel disconnected
4. **Mobile scroll fatigue:** Desktop spacing values on mobile create endless scrolling
5. **Orphaned elements:** Small elements (badges, labels) floating in too much space
6. **Collision zones:** Two dense sections back-to-back without a light separator

### How to Fix Each Problem

**Wall of sameness:** Introduce the AABA pattern. Insert one dark/accent section every 3-4 blocks.

**Cramped transitions:** Add background alternation (white → gray-50 → white). Even without spacing changes, color shifts create separation.

**Desert gaps:** Reduce 2xl spacing to xl. Group related sections with sm spacing instead of treating every block as independent.

**Mobile scroll fatigue:** Apply the responsive reduction formula. Use fluid spacing with clamp(). Audit total page height on mobile.

**Orphaned elements:** Group small elements with their parent section using xs spacing. Trust badges belong WITH the CTA, not as their own section.

**Collision zones:** Insert a light block (stats row, single quote, CTA banner) between two dense blocks (feature grid followed by pricing table).
