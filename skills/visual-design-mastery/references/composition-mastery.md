# Composition Mastery

> Layout and composition for UI: grid systems, proportional systems, visual weight, whitespace, density, responsive patterns, hierarchy techniques, scanning patterns, and information density.

---

## Grid Systems

### Swiss/International Grid

The Swiss grid divides space mathematically into columns, gutters, and margins. Every element aligns to this structure.

**Anatomy**:
- **Columns**: Vertical divisions of content area (typically 4, 6, 8, or 12)
- **Gutters**: Space between columns (typically 16-32px)
- **Margins**: Space between content area and viewport edge (typically 16-80px)
- **Modules**: Grid cells formed by column width × row height

**Mathematical Division**:
```
Content width = Viewport - (2 × margin)
Column width = (Content width - (columns - 1) × gutter) / columns

Example (1440px viewport, 12 columns):
  Margin: 80px each side
  Content: 1440 - 160 = 1280px
  Gutter: 24px
  Column: (1280 - 11 × 24) / 12 = 84.67px ≈ 85px
```

### 8px Baseline Grid

The foundational spacing unit for digital interfaces.

**Why 8px**:
- Divisible by 2 and 4 (sub-grid for icons and fine details)
- Scales cleanly across 1x, 1.5x, 2x, 3x pixel densities
- Creates clear visual rhythm at all spacing levels
- Industry standard (Material Design, Apple HIG, most design systems)

**Application**:
```css
/* All spacing derived from 8px */
--space-1: 4px;    /* Half-unit for fine details */
--space-2: 8px;    /* Base unit */
--space-3: 12px;   /* 1.5 base */
--space-4: 16px;   /* 2 base */
--space-6: 24px;   /* 3 base */
--space-8: 32px;   /* 4 base */
--space-10: 40px;  /* 5 base */
--space-12: 48px;  /* 6 base */
--space-16: 64px;  /* 8 base */
--space-24: 96px;  /* 12 base */
--space-32: 128px; /* 16 base */

/* Element heights on the grid */
--height-button-sm: 32px;   /* 4 × 8 */
--height-button-md: 40px;   /* 5 × 8 */
--height-button-lg: 48px;   /* 6 × 8 */
--height-input: 40px;       /* 5 × 8 */
--height-list-item: 48px;   /* 6 × 8 */
--height-toolbar: 56px;     /* 7 × 8 */
--height-nav: 64px;         /* 8 × 8 */
```

### 4px Sub-Grid

For fine adjustments where 8px is too coarse:

- Icon padding within buttons: 4px
- Badge offset: 4px
- Divider spacing: 4px above and below
- Inline icon alignment nudges
- Small component internal spacing (chip padding: 4px 8px)

**Rule**: Use 4px only inside small components (<48px total height). Use 8px+ for all inter-component spacing.

### 12-Column Grid

The web standard for responsive layouts:

```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;               /* Gutter */
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 24px;         /* Mobile margin */
}

/* Responsive breakdown */
@media (max-width: 1024px) {
  .grid { grid-template-columns: repeat(8, 1fr); }
}
@media (max-width: 768px) {
  .grid { grid-template-columns: repeat(4, 1fr); }
}
@media (max-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    padding: 0 16px;
  }
}

/* Common span patterns */
.full { grid-column: span 12; }
.two-thirds { grid-column: span 8; }
.half { grid-column: span 6; }
.third { grid-column: span 4; }
.quarter { grid-column: span 3; }
.sidebar { grid-column: span 3; }
.content { grid-column: span 9; }
```

### CSS Grid vs. Flexbox

| Use Case | Recommended | Why |
|---|---|---|
| Page-level layout | CSS Grid | 2D: rows AND columns |
| Component-level layout | Flexbox | 1D: row OR column |
| Card grids with equal sizes | CSS Grid | Consistent cell sizes |
| Navigation bars | Flexbox | Single-axis alignment |
| Dashboard layout | CSS Grid | Named areas, spanning |
| Centering | Flexbox | `align-items: center; justify-content: center` |
| Auto-fill responsive grids | CSS Grid | `auto-fit` + `minmax()` |
| Unknown-count item wrapping | Flexbox | `flex-wrap: wrap` |

```css
/* Auto-responsive grid (no media queries needed) */
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}
```

---

## Golden Ratio & Proportional Systems

### Golden Ratio (1:1.618)

The ratio found in nature, art, and architecture. Creates naturally pleasing proportions.

**UI Applications**:
```css
/* Sidebar / Content split */
.layout {
  display: grid;
  grid-template-columns: 1fr 1.618fr;  /* ~38% / ~62% */
}

/* Card proportions */
.card {
  aspect-ratio: 1 / 1.618;  /* Golden rectangle */
}

/* Section padding (vertical / horizontal) */
.section {
  padding: 64px 40px;  /* 64/40 ≈ 1.6 */
}
```

**Where it works**: Hero sections, sidebar/content splits, card aspect ratios, image crops for portfolios and editorial.

**Where it doesn't**: Data-dense dashboards, forms, navigation. Use rational proportions (halves, thirds, quarters) for functional layouts.

### Rule of Thirds

Divide the viewport into a 3x3 grid. Focal points at line intersections.

```css
/* Hero image with subject at top-right intersection */
.hero-image {
  object-position: 67% 33%;  /* Top-right third intersection */
}

/* CTA placement at bottom-left intersection */
.hero-cta {
  position: absolute;
  left: 33%;
  bottom: 33%;
}
```

### Musical Ratios

Proportional systems based on musical intervals:

| Ratio | Name | Decimal | Use |
|---|---|---|---|
| 1:2 | Octave | 2.0 | Main content vs. sidebar (2:1 split) |
| 2:3 | Fifth | 1.5 | Card image-to-text ratio |
| 3:4 | Fourth | 1.333 | Image aspect ratio (4:3) |
| 4:5 | Major third | 1.25 | Comfortable column proportions |
| 5:6 | Minor third | 1.2 | Tight but harmonious proportions |

### Fibonacci Spacing Scale

Spacing values following the Fibonacci sequence, expressed as multipliers of a base unit:

```css
:root {
  --base: 4px;
  --fib-1: calc(1 * var(--base));    /* 4px */
  --fib-2: calc(2 * var(--base));    /* 8px */
  --fib-3: calc(3 * var(--base));    /* 12px */
  --fib-5: calc(5 * var(--base));    /* 20px */
  --fib-8: calc(8 * var(--base));    /* 32px */
  --fib-13: calc(13 * var(--base));  /* 52px */
  --fib-21: calc(21 * var(--base));  /* 84px */
  --fib-34: calc(34 * var(--base));  /* 136px */
}
```

**Advantage**: Non-linear scale with natural-feeling jumps. Each step is ~1.618x the previous (golden ratio).

---

## Visual Weight & Balance

### What Creates Visual Weight

| Factor | More Weight | Less Weight |
|---|---|---|
| **Size** | Larger elements | Smaller elements |
| **Color saturation** | Vivid, saturated colors | Muted, desaturated colors |
| **Color darkness** | Dark elements on light bg | Light elements on light bg |
| **Density** | Complex, detailed elements | Simple, minimal elements |
| **Isolation** | Elements with surrounding space | Crowded elements |
| **Texture** | Textured, patterned surfaces | Smooth, flat surfaces |
| **Position** | Lower-right (feels heavier) | Upper-left (feels lighter) |
| **Shape** | Irregular, complex shapes | Regular, geometric shapes |

### Balance Types

**Symmetric (Formal) Balance**:
- Equal visual weight on both sides of a central axis
- Creates stability, trust, order
- Best for: Settings pages, forms, data tables, dashboards, login screens
- Implementation: Centered layouts, equal column widths, mirrored sections
```css
.symmetric-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;  /* Equal halves */
  text-align: center;
}
```

**Asymmetric (Informal) Balance**:
- Unequal elements balanced through visual weight
- Creates dynamism, interest, movement
- Best for: Marketing pages, portfolios, storytelling, product tours
- Implementation: Large element on one side, multiple smaller elements on the other
```css
.asymmetric-layout {
  display: grid;
  grid-template-columns: 2fr 1fr;  /* Hero left, supporting right */
}
```

**Radial Balance**:
- Visual weight radiates from a central focal point
- Creates focus, attention, ceremony
- Best for: Login screens, onboarding steps, modal dialogs, empty states
- Implementation: Centered content with surrounding space
```css
.radial-layout {
  display: grid;
  place-items: center;
  min-height: 100vh;
  text-align: center;
}
```

### Balance Testing Methods

1. **Squint test**: Squint at the screen. Blur removes detail, revealing weight distribution. If one area feels heavier, rebalance.
2. **Blur test** (Figma): Apply 10px Gaussian blur. The hierarchy should still be visible. Primary element = darkest/largest blob.
3. **Grayscale test**: Remove all color (filter: grayscale(1)). If hierarchy disappears, you're relying on color alone — fix with size/weight/position.
4. **Thumbnail test**: View the design at 10% zoom. The composition should still make sense as abstract shapes.

---

## Whitespace as Design Element

### Micro Whitespace

Space inside components:

```css
/* Micro whitespace: padding within components */
--padding-button-sm: 6px 12px;
--padding-button-md: 10px 20px;
--padding-button-lg: 14px 28px;
--padding-input: 10px 14px;
--padding-card: 20px 24px;
--padding-badge: 2px 8px;
--padding-chip: 4px 12px;
--padding-tooltip: 8px 12px;
```

**Rule**: Horizontal padding is typically 1.5-2x vertical padding for most components (buttons, chips, badges). Exception: cards and modals use equal or near-equal padding.

### Macro Whitespace

Space between major sections:

```css
/* Macro whitespace: section and page-level spacing */
--section-gap-sm: 48px;    /* Between related sections */
--section-gap-md: 64px;    /* Between distinct sections */
--section-gap-lg: 96px;    /* Between major sections */
--section-gap-xl: 128px;   /* Hero-to-content gap */

--page-margin-mobile: 16px;
--page-margin-tablet: 32px;
--page-margin-desktop: 48px;
--page-margin-wide: 80px;
```

### Active vs. Passive Whitespace

**Active whitespace**: Intentionally placed to create hierarchy, guide the eye, or separate content groups. It has a purpose.
```css
/* Active: generous padding around CTA draws attention */
.cta-container {
  padding: 48px 32px;  /* Intentionally generous */
  margin: 64px auto;   /* Isolated from surrounding content */
}
```

**Passive whitespace**: Leftover space from poor layout — margins that happen by accident, gaps from content not filling its container.
```css
/* Passive: accidental whitespace from fixed-width content */
.container {
  width: 600px; /* On a 1440px viewport, 840px of passive whitespace */
}
```

**Rule**: All whitespace should be active. If you can't explain why a space exists, either increase it (make it an intentional separator) or eliminate it (close the gap).

### The "Double the Whitespace" Rule

From Refactoring UI (Wathan & Schoger): When in doubt, double the whitespace.

**Before**:
```css
.card { padding: 16px; margin-bottom: 16px; }
.section { padding: 24px 0; }
```

**After (doubled)**:
```css
.card { padding: 32px; margin-bottom: 32px; }
.section { padding: 48px 0; }
```

**Why it works**: Developers and beginner designers consistently under-space. The result looks "cramped" or "cheap." Generous whitespace is the single most impactful upgrade for amateur-to-professional transition.

---

## Density Control

### Three Density Levels

| Density | Base Unit | Row Height | Padding Scale | Best For |
|---|---|---|---|---|
| **Compact** | 4px | 32px | 4, 8, 12, 16, 24 | Data-heavy: spreadsheets, Figma panels, code editors, admin tables |
| **Comfortable** | 8px | 40-44px | 8, 12, 16, 24, 32, 48 | General: email, project management, CMS, most SaaS |
| **Spacious** | 12px | 48-56px | 12, 16, 24, 32, 48, 64 | Marketing: landing pages, editorial, onboarding, consumer apps |

### Implementing Density as Tokens

```css
/* Density as a switchable custom property */
:root {
  --density: 8px; /* comfortable default */
}

:root[data-density="compact"] { --density: 4px; }
:root[data-density="comfortable"] { --density: 8px; }
:root[data-density="spacious"] { --density: 12px; }

/* All spacing multiplied by density */
--space-1: calc(0.5 * var(--density));
--space-2: var(--density);
--space-3: calc(1.5 * var(--density));
--space-4: calc(2 * var(--density));
--space-6: calc(3 * var(--density));
--space-8: calc(4 * var(--density));

/* Component sizing tied to density */
--row-height: calc(5 * var(--density));
--button-height: calc(5 * var(--density));
--input-height: calc(5 * var(--density));
```

### When to Use Each

- **Compact**: Expert users who work in the tool 8+ hours/day. They've learned the interface and want efficiency. Figma, VS Code, Bloomberg Terminal.
- **Comfortable**: General productivity users. They use the tool daily but not all day. Gmail, Notion, Slack, Linear.
- **Spacious**: First-time users, marketing audiences, or reading-focused use cases. Airbnb, Medium, Apple.com, onboarding flows.

**Rule**: Default to comfortable. Offer compact as a user preference for power users. Use spacious for public-facing pages and onboarding.

---

## Responsive Layout Patterns

### Pattern 1: Reflow

Columns reduce as viewport narrows. Content maintains its size.

```css
/* 4 columns → 2 → 1 */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}
```

**When**: Card grids, feature sections, team grids, pricing plans.

### Pattern 2: Stack

Horizontal arrangements become vertical.

```css
/* Side-by-side → stacked */
.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
}
@media (max-width: 768px) {
  .hero { grid-template-columns: 1fr; }
}
```

**When**: Hero sections (text + image), feature descriptions, comparison layouts.

### Pattern 3: Reveal/Hide

Secondary content hidden on smaller screens, accessible via interaction.

```css
.sidebar {
  display: block;
  width: 260px;
}
@media (max-width: 1024px) {
  .sidebar {
    display: none;         /* Hidden by default */
    position: fixed;       /* Overlay when revealed */
    inset: 0;
    z-index: 50;
  }
  .sidebar[data-open="true"] { display: block; }
}
```

**When**: Navigation sidebars, filter panels, secondary info panels.

### Pattern 4: Prioritize

Content reorders by importance on smaller screens.

```css
.layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas: "sidebar content";
}
@media (max-width: 768px) {
  .layout {
    grid-template-columns: 1fr;
    grid-template-areas:
      "content"    /* Content first on mobile */
      "sidebar";   /* Sidebar second (below) */
  }
}
```

**When**: Sidebar + content layouts where content is primary on mobile.

### Pattern 5: Resize (Container Queries)

Components adapt to their container width, not viewport width.

```css
.card-container {
  container-type: inline-size;
}

.card {
  display: grid;
  grid-template-columns: 1fr;
}
@container (min-width: 400px) {
  .card {
    grid-template-columns: 120px 1fr;  /* Image + text side-by-side */
  }
}
@container (min-width: 600px) {
  .card {
    grid-template-columns: 200px 1fr;  /* Larger image */
  }
}
```

**When**: Cards, widgets, and components that appear in different-sized containers.

### Common Breakpoints

```css
/* Standard breakpoints */
--bp-sm: 640px;    /* Mobile landscape / large phone */
--bp-md: 768px;    /* Tablet portrait */
--bp-lg: 1024px;   /* Tablet landscape / small laptop */
--bp-xl: 1280px;   /* Desktop */
--bp-2xl: 1536px;  /* Wide desktop */

/* Max content width */
--max-content: 1280px;  /* Standard */
--max-prose: 720px;     /* Reading content */
--max-wide: 1536px;     /* Full-bleed sections */
```

---

## Visual Hierarchy Techniques

### The 7 Hierarchy Levers

Listed in order of effectiveness:

| # | Lever | How It Works | CSS Property |
|---|---|---|---|
| 1 | **Size** | Larger = more important | font-size, width, height |
| 2 | **Weight** | Bolder = more important | font-weight |
| 3 | **Color/Contrast** | Saturated/dark = more attention | color, background-color |
| 4 | **Position** | Top-left (LTR) = first seen | grid-area, order |
| 5 | **Spacing/Isolation** | More whitespace around = more prominent | margin, padding, gap |
| 6 | **Depth** | Elevated (shadow) = foreground | box-shadow, z-index |
| 7 | **Motion** | Moving elements attract attention | animation, transition |

### The "3 Levels Max" Rule

At any moment, the user should perceive at most 3 levels of importance:

```
Level 1 — PRIMARY: "Look here first"
  Hero heading, primary metric, main CTA
  Treatment: Largest size, boldest weight, highest contrast, most isolation

Level 2 — SECONDARY: "Look here next"
  Section headings, supporting data, secondary actions
  Treatment: Medium size, medium weight, moderate contrast

Level 3 — TERTIARY: "Look here if needed"
  Body text, metadata, tertiary actions
  Treatment: Base size, normal weight, reduced contrast
```

**Test**: Cover your screen with your hand and reveal it suddenly. The first thing your eye goes to is Level 1. The second thing is Level 2. Everything else should be Level 3.

### Hierarchy Application

```css
/* Level 1: Primary */
.primary-heading {
  font-size: var(--text-3xl);        /* 30-39px */
  font-weight: 700;
  color: var(--color-text-primary);  /* Highest contrast */
  line-height: 1.15;
  letter-spacing: -0.02em;
}

/* Level 2: Secondary */
.section-heading {
  font-size: var(--text-xl);         /* 20-25px */
  font-weight: 600;
  color: var(--color-text-primary);
  line-height: 1.25;
}

/* Level 3: Tertiary */
.body-text {
  font-size: var(--text-base);       /* 16-18px */
  font-weight: 400;
  color: var(--color-text-secondary); /* Reduced contrast */
  line-height: 1.5;
}
```

---

## Scanning Patterns

### F-Pattern

**Where it occurs**: Text-heavy pages, search results, news feeds, documentation.

**User behavior**:
1. Horizontal scan across the top (headline area)
2. Drop down, horizontal scan across a subheading
3. Vertical scan down the left edge (skimming first words of each line/heading)

**Design implications**:
- Place the most important content in the first 2 lines
- Front-load headings (first 2-3 words carry the meaning)
- Left-align all text
- Use bold/color on the first word of list items to support left-edge scanning
- Don't center long lists or body content

### Z-Pattern

**Where it occurs**: Landing pages, login screens, above-the-fold sections with minimal text.

**User behavior**:
1. Top-left → Top-right (header area)
2. Diagonal → Bottom-left
3. Bottom-left → Bottom-right (action area)

**Design implications**:
- Logo/brand: top-left
- Navigation or secondary CTA: top-right
- Key message: center-left
- Primary CTA: bottom-right or center-bottom
- Supporting info: bottom-left

### Layer Cake Pattern

**Where it occurs**: Pages with clear headings that create horizontal bands.

**User behavior**: Users scan headings as horizontal layers, reading only the heading text, then diving into the section that matches their need.

**Design implications**:
- Make headings scannable independently (each heading tells a complete micro-story)
- Visual distinction between heading and body (size, weight, spacing)
- Consistent heading rhythm (equal spacing above each heading)
- Each section should be independently understandable

### Designing for Scanning vs. Reading

**Most users scan. Design for scanning first.**

| Scanning-Friendly | Reading-Hostile |
|---|---|
| Short headings (3-5 words) | Paragraphs longer than 4 lines |
| Bullet points for lists | Dense paragraphs for lists |
| Bold key phrases | Uniform text weight throughout |
| Visual separators between sections | Wall of text with no breaks |
| Progressive disclosure | Everything visible at once |

---

## Information Density Optimization

### Dashboard Design: Data-Ink Ratio (Tufte)

Edward Tufte's principle: Maximize the ratio of data to non-data ink. Remove everything that doesn't communicate data.

**Remove**:
- Decorative borders around data (use whitespace instead)
- Redundant labels (if the axis says "Revenue ($)", don't repeat it)
- 3D effects on charts (distort perception)
- Grid lines (reduce to minimum: light, few, or none)

**Keep**:
- Data labels (when they replace axis reading)
- Direct annotation (label the important point, not all points)
- Clear titles that state the insight, not just the category

```css
/* Clean data display */
.metric-card {
  padding: 24px;
  /* No border, no shadow — whitespace creates the container */
}
.metric-value {
  font-size: 32px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}
.metric-label {
  font-size: 13px;
  color: var(--color-text-secondary);
  margin-top: 4px;
}
```

### Card Layouts

Cards are content previews. They should:
- Have consistent aspect ratios for images
- Show just enough to decide whether to click
- Have a single clear action (the entire card is clickable)
- Use hierarchy within the card: image > title > metadata > description (truncated)

```css
.card {
  display: flex;
  flex-direction: column;
  border-radius: 12px;
  overflow: hidden;
  background: var(--color-surface);
  border: 1px solid var(--color-border-default);
  transition: box-shadow 150ms ease;
}
.card:hover {
  box-shadow: 0 8px 24px oklch(0.3 0.02 250 / 0.1);
}
.card-image {
  aspect-ratio: 16 / 9;
  object-fit: cover;
  width: 100%;
}
.card-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.card-title {
  font-size: 18px;
  font-weight: 600;
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.card-meta {
  font-size: 14px;
  color: var(--color-text-secondary);
}
```

### Table Design

Tables for dense data with readability:

```css
.table {
  width: 100%;
  border-collapse: collapse;
  font-variant-numeric: tabular-nums;
}
.table th {
  text-align: left;
  font-weight: 600;
  font-size: 13px;
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 12px 16px;
  border-bottom: 2px solid var(--color-border-strong);
  position: sticky;
  top: 0;
  background: var(--color-bg);
}
.table td {
  padding: 12px 16px;
  border-bottom: 1px solid var(--color-border-default);
  font-size: 14px;
}

/* Zebra striping (subtle) */
.table tr:nth-child(even) {
  background: oklch(0 0 0 / 0.02);
}

/* Hover highlight */
.table tr:hover {
  background: oklch(0 0 0 / 0.04);
}
```

**Table priorities by breakpoint**:
- Desktop (1280px+): Full table with all columns
- Laptop (1024px): Hide lowest-priority columns
- Tablet (768px): Horizontal scroll with sticky first column
- Mobile (640px): Convert to card/list layout (each row becomes a card)

### Progressive Disclosure

Show essential first, expand for detail:

```css
/* Summary → Detail pattern */
.summary {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  cursor: pointer;
}
.detail {
  padding: 0 16px 16px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 200ms ease-out;
}
.detail[data-expanded="true"] {
  max-height: 500px;  /* Arbitrary large value */
}
```

**Progressive disclosure hierarchy**:
1. **Level 0**: Title + primary metric (visible always)
2. **Level 1**: Summary data + key actions (visible on hover/focus or one click)
3. **Level 2**: Full details + secondary actions (visible on expand/navigate)
4. **Level 3**: Configuration + advanced options (visible via settings/modal)

**Rule**: 80% of users should never need to go past Level 1. Only power users reach Level 3. If most users need Level 2, promote that content to Level 1.

---

## Composition Cheat Sheet

### Quick Audit Questions

1. **Grid**: Can I overlay a 12-column grid and see alignment? (If not: add grid)
2. **Focal point**: Is there ONE element that draws the eye first? (If not: increase its visual weight)
3. **Balance**: Does the layout feel weighted evenly? (If not: add whitespace to balance)
4. **Rhythm**: Are spacing intervals repeated consistently? (If not: standardize on spacing scale)
5. **Scanning**: Can I understand the page in 5 seconds? (If not: increase heading contrast)
6. **Density**: Is the density appropriate for the user and context? (If not: adjust spacing scale)
7. **Responsive**: Does the layout reflow gracefully? (If not: implement responsive patterns above)
8. **Whitespace**: Does removing 30% of the content make it look better? (If yes: the original was too dense)
