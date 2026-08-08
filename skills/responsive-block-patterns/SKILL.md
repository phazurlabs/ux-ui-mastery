---
name: responsive-block-patterns
description: "How every block and component transforms across breakpoints: container queries, fluid scaling, breakpoint transformation catalogs, responsive grids, and mobile-first CSS with production code. Use when a layout must survive small screens, or when specifying responsive behavior for handoff."
---

# Responsive Block Patterns — Cross-Breakpoint Design Intelligence

## 1. Responsive Design Philosophy

### Mobile-First
Start from the smallest screen. Layer complexity upward. The base CSS is for mobile; media queries add layout for larger viewports. This guarantees that every device gets a functional experience, and larger screens get enhanced layout rather than degraded desktop views.

### Content-Out
The content determines breakpoints, not device widths. If a paragraph becomes too wide to read comfortably, that is your breakpoint. If a card grid looks awkward, that is your breakpoint. Device widths are reference points, not gospel.

### Fluid by Default
Between breakpoints, everything should scale smoothly. Use relative units (rem, em, %, vw, vh), clamp(), and container query units (cqi, cqw) so that layouts breathe between breakpoints rather than snapping at arbitrary widths.

### Breakpoints as Needed
Add a breakpoint only when the layout breaks. A simple marketing page may need 3 breakpoints. A complex dashboard may need 6. Do not force every project into the same breakpoint set. The system below is a reference framework, not a mandate.

### Core Principles
- **Progressive enhancement** — Base experience works everywhere; advanced features layer on
- **Intrinsic design** — Let CSS do the work with auto-fill, minmax, clamp, flex-wrap
- **Reduce, do not hide** — Prefer simplifying content over display:none where possible
- **Performance is responsive** — Serve appropriately sized images; do not send desktop assets to mobile
- **Touch and pointer coexistence** — Design for both input modes simultaneously

---

## 2. Breakpoint Strategy

### Reference Breakpoint System

| Token | Range | Min-width query | Typical devices |
|-------|-------|-----------------|-----------------|
| xs | 0 - 479px | (default / no query) | iPhone SE, Galaxy S series, small Android |
| sm | 480 - 767px | `min-width: 480px` | iPhone Plus/Max, Pixel Pro, large phones landscape |
| md | 768 - 1023px | `min-width: 768px` | iPad Mini, iPad Air portrait, Surface Go, small tablets |
| lg | 1024 - 1279px | `min-width: 1024px` | iPad Pro portrait, iPad landscape, small laptops, Surface Pro |
| xl | 1280 - 1535px | `min-width: 1280px` | MacBook Air 13", standard laptops, desktop 720p monitors |
| 2xl | 1536px+ | `min-width: 1536px` | MacBook Pro 16", 1080p+ monitors, iMac, ultrawide |

### CSS Custom Properties for Breakpoints

```css
:root {
  --bp-sm: 480px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
  --bp-2xl: 1536px;
}
```

Note: CSS custom properties cannot be used directly inside @media queries. These are reference values for documentation and JavaScript. In media queries, use the literal pixel values.

### Mobile-First Media Query Scaffold

```css
/* xs: 0-479px — base styles, no query needed */
.component { /* mobile styles */ }

/* sm: 480-767px */
@media (min-width: 480px) { .component { /* large phone */ } }

/* md: 768-1023px */
@media (min-width: 768px) { .component { /* tablet */ } }

/* lg: 1024-1279px */
@media (min-width: 1024px) { .component { /* small desktop */ } }

/* xl: 1280-1535px */
@media (min-width: 1280px) { .component { /* desktop */ } }

/* 2xl: 1536px+ */
@media (min-width: 1536px) { .component { /* large desktop */ } }
```

### Device Mapping Reference

| Device | Screen width | Breakpoint | Pixel ratio |
|--------|-------------|------------|-------------|
| iPhone SE (3rd gen) | 375px | xs | 2x |
| iPhone 15 | 393px | xs | 3x |
| iPhone 15 Pro Max | 430px | xs | 3x |
| Pixel 8 | 412px | xs | 2.625x |
| Samsung Galaxy S24 Ultra | 480px | sm | 3x |
| iPad Mini (6th gen) | 744px | sm | 2x |
| iPad Air (5th gen) | 820px | md | 2x |
| iPad Pro 11" | 834px | md | 2x |
| iPad Pro 12.9" | 1024px | lg | 2x |
| MacBook Air 13" | 1280px | xl | 2x |
| MacBook Pro 14" | 1512px | xl | 2x |
| MacBook Pro 16" | 1728px | 2xl | 2x |
| iMac 24" | 2048px (scaled) | 2xl | 2x |
| 1080p monitor | 1920px | 2xl | 1x |

---

## 3. CSS Grid Responsive Patterns

### Pattern 1: Auto-Fill Equal Columns

```css
.grid-auto-fill {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}
```

Columns automatically wrap based on available space. No media queries needed. The 280px minimum determines the natural breakpoint.

### Pattern 2: Auto-Fit with Stretch

```css
.grid-auto-fit {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}
```

Difference from auto-fill: auto-fit collapses empty tracks, so fewer items stretch to fill the row. Use auto-fit for content grids, auto-fill for uniform card grids.

### Pattern 3: Responsive Grid with Explicit Breakpoints

```css
.grid-explicit {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}
@media (min-width: 768px) {
  .grid-explicit { grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }
}
@media (min-width: 1280px) {
  .grid-explicit { grid-template-columns: repeat(3, 1fr); gap: 2rem; }
}
```

### Pattern 4: Grid Template Areas Rearrangement

```css
.page-layout {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "sidebar"
    "footer";
  grid-template-columns: 1fr;
}
@media (min-width: 768px) {
  .page-layout {
    grid-template-areas:
      "header  header"
      "main    sidebar"
      "footer  footer";
    grid-template-columns: 2fr 1fr;
  }
}
@media (min-width: 1280px) {
  .page-layout {
    grid-template-areas:
      "header  header  header"
      "sidebar main    aside"
      "footer  footer  footer";
    grid-template-columns: 240px 1fr 300px;
  }
}
```

### Pattern 5: Asymmetric Grid

```css
.asymmetric {
  display: grid;
  grid-template-columns: 1fr;
}
@media (min-width: 768px) {
  .asymmetric { grid-template-columns: 1fr 2fr; }
}
@media (min-width: 1280px) {
  .asymmetric { grid-template-columns: 1fr 3fr 1fr; }
}
```

### Pattern 6: Named Grid Lines

```css
.named-grid {
  display: grid;
  grid-template-columns:
    [full-start] 1fr
    [content-start] min(65ch, 100%) [content-end]
    1fr [full-end];
}
.named-grid > .full-bleed {
  grid-column: full-start / full-end;
}
.named-grid > .content {
  grid-column: content-start / content-end;
}
```

### Pattern 7: Subgrid for Aligned Cards

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}
.card {
  display: grid;
  grid-template-rows: subgrid;
  grid-row: span 3; /* image, content, footer */
}
```

Subgrid ensures card internals (image, title, description, CTA) align across the row even when content lengths differ.

### Pattern 8: Dense Auto-Placement

```css
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-flow: dense;
  gap: 0.5rem;
}
.gallery-grid .featured {
  grid-column: span 2;
  grid-row: span 2;
}
```

### Pattern 9: Responsive Sidebar with minmax

```css
.sidebar-layout {
  display: grid;
  grid-template-columns: 1fr;
}
@media (min-width: 768px) {
  .sidebar-layout {
    grid-template-columns: minmax(200px, 280px) 1fr;
  }
}
```

### Pattern 10: Full-Bleed Layout

```css
.full-bleed-layout {
  display: grid;
  grid-template-columns:
    1fr
    min(var(--content-width, 1200px), 100% - 2rem)
    1fr;
}
.full-bleed-layout > * {
  grid-column: 2;
}
.full-bleed-layout > .bleed {
  grid-column: 1 / -1;
}
```

### Pattern 11: Responsive Dashboard Grid

```css
.dashboard {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}
@media (min-width: 768px) {
  .dashboard {
    grid-template-columns: repeat(2, 1fr);
  }
  .dashboard .widget-wide { grid-column: span 2; }
}
@media (min-width: 1280px) {
  .dashboard {
    grid-template-columns: repeat(4, 1fr);
  }
  .dashboard .widget-wide { grid-column: span 2; }
  .dashboard .widget-full { grid-column: span 4; }
}
```

### Pattern 12: Pancake Stack (Full-Height)

```css
.pancake {
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100dvh;
}
```

Header and footer take their natural height; main content fills remaining space.

### Pattern 13: RAM (Repeat, Auto, Minmax) with Clamped Columns

```css
.ram-grid {
  display: grid;
  grid-template-columns: repeat(
    auto-fit,
    minmax(clamp(200px, 30%, 350px), 1fr)
  );
  gap: clamp(1rem, 2vw, 2rem);
}
```

### Pattern 14: Responsive Masonry (CSS Grid)

```css
.masonry {
  columns: 1;
  column-gap: 1rem;
}
@media (min-width: 480px) { .masonry { columns: 2; } }
@media (min-width: 1024px) { .masonry { columns: 3; } }
@media (min-width: 1536px) { .masonry { columns: 4; } }
.masonry > * {
  break-inside: avoid;
  margin-bottom: 1rem;
}
```

### Pattern 15: Holy Grail Layout

```css
.holy-grail {
  display: grid;
  grid-template: auto 1fr auto / 1fr;
  min-height: 100dvh;
}
@media (min-width: 768px) {
  .holy-grail {
    grid-template:
      "header header header" auto
      "nav    main   aside" 1fr
      "footer footer footer" auto
      / 200px 1fr 200px;
  }
}
```

---

## 4. Flexbox Responsive Patterns

### Pattern 1: Flex Wrap with Minimum Width

```css
.flex-wrap-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}
.flex-wrap-cards > * {
  flex: 1 1 300px; /* grow, shrink, min 300px basis */
}
```

### Pattern 2: Flex Direction Swap

```css
.hero-split {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
@media (min-width: 768px) {
  .hero-split {
    flex-direction: row;
    align-items: center;
  }
  .hero-split > * { flex: 1; }
}
```

### Pattern 3: Flex Order Reordering

```css
.content-sidebar {
  display: flex;
  flex-direction: column;
}
.content-sidebar .sidebar { order: 2; }
.content-sidebar .main { order: 1; }

@media (min-width: 1024px) {
  .content-sidebar {
    flex-direction: row;
  }
  .content-sidebar .sidebar { order: -1; flex: 0 0 280px; }
  .content-sidebar .main { order: 0; flex: 1; }
}
```

### Pattern 4: Flex Basis Breakpoints

```css
.feature-row > * {
  flex: 1 1 100%; /* stack on mobile */
}
@media (min-width: 768px) {
  .feature-row > * { flex: 1 1 calc(50% - 1rem); }
}
@media (min-width: 1280px) {
  .feature-row > * { flex: 1 1 calc(33.333% - 1rem); }
}
```

### Pattern 5: Inline Flex with Wrap for Tag Lists

```css
.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.tag-list > .tag {
  flex: 0 0 auto;
  padding: 0.25rem 0.75rem;
}
```

### Pattern 6: Flex Gap for Responsive Spacing

```css
.button-group {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(0.5rem, 1vw, 1rem);
}
```

### Pattern 7: Centering with Flex (Responsive)

```css
.centered-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100dvh;
  padding: clamp(1rem, 5vw, 4rem);
  text-align: center;
}
@media (min-width: 768px) {
  .centered-content { text-align: left; align-items: flex-start; }
}
```

### Pattern 8: Flex Grow Distribution

```css
.toolbar {
  display: flex;
  gap: 0.5rem;
}
.toolbar .search { flex: 1; } /* takes remaining space */
.toolbar .actions { flex: 0 0 auto; } /* fixed size */
```

### Pattern 9: Responsive Nav with Flex

```css
.nav {
  display: flex;
  flex-direction: column;
  gap: 0;
}
@media (min-width: 768px) {
  .nav {
    flex-direction: row;
    align-items: center;
    gap: 1.5rem;
  }
}
```

### Pattern 10: Sticky Footer with Flex

```css
.page {
  display: flex;
  flex-direction: column;
  min-height: 100dvh;
}
.page > main { flex: 1; }
.page > header, .page > footer { flex-shrink: 0; }
```

---

## 5. Container Queries

### Syntax and Setup

```css
/* Define a containment context */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Query the container */
@container card (min-width: 400px) {
  .card { flex-direction: row; }
}
@container card (max-width: 399px) {
  .card { flex-direction: column; }
}
```

### container-type Values

| Value | Behavior |
|-------|----------|
| `inline-size` | Enable queries on inline axis (width in horizontal writing). Most common. |
| `size` | Enable queries on both axes (width and height). Use sparingly. |
| `normal` | No containment. Default. |

### container-name

Name your containers to avoid ambiguity when nesting:

```css
.sidebar { container-type: inline-size; container-name: sidebar; }
.main    { container-type: inline-size; container-name: main-content; }

@container sidebar (min-width: 250px) { /* sidebar-specific */ }
@container main-content (min-width: 600px) { /* main-specific */ }
```

### When Container Queries vs. Media Queries

| Use container queries when... | Use media queries when... |
|-------------------------------|--------------------------|
| Component appears in multiple contexts (sidebar, main, modal) | Layout depends on overall viewport |
| Building design system components | Setting global typography/spacing |
| Card/widget needs self-aware responsiveness | Changing navigation patterns |
| Component will be used in unknown parent contexts | Applying print or prefers-* queries |

### Practical Example: Responsive Card

```css
.card-wrapper {
  container-type: inline-size;
  container-name: card-container;
}

.card {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.card .image { aspect-ratio: 16/9; width: 100%; }
.card .meta { font-size: 0.875rem; }

@container card-container (min-width: 500px) {
  .card {
    flex-direction: row;
    align-items: flex-start;
  }
  .card .image {
    flex: 0 0 200px;
    aspect-ratio: 1;
  }
  .card .body { flex: 1; }
}

@container card-container (min-width: 700px) {
  .card .meta { font-size: 1rem; }
  .card .actions { display: flex; gap: 0.5rem; }
}
```

### Practical Example: Sidebar Navigation

```css
.sidebar {
  container-type: inline-size;
  container-name: sidebar-nav;
}

.nav-item .label { display: none; }
.nav-item .icon { display: block; }

@container sidebar-nav (min-width: 180px) {
  .nav-item .label { display: inline; }
  .nav-item { display: flex; gap: 0.75rem; align-items: center; }
}

@container sidebar-nav (min-width: 260px) {
  .nav-item .badge { display: flex; }
  .nav-item .description { display: block; font-size: 0.75rem; }
}
```

### Practical Example: Dashboard Widget

```css
.widget-container {
  container-type: inline-size;
  container-name: widget;
}

.widget { padding: 1rem; }
.widget .chart { height: 150px; }
.widget .stats { display: none; }

@container widget (min-width: 350px) {
  .widget .stats { display: grid; grid-template-columns: repeat(2, 1fr); }
  .widget .chart { height: 200px; }
}

@container widget (min-width: 500px) {
  .widget .stats { grid-template-columns: repeat(4, 1fr); }
  .widget .chart { height: 280px; }
}
```

### Container Query Units

| Unit | Meaning |
|------|---------|
| cqw | 1% of container width |
| cqh | 1% of container height |
| cqi | 1% of container inline size |
| cqb | 1% of container block size |
| cqmin | Smaller of cqi/cqb |
| cqmax | Larger of cqi/cqb |

```css
@container (min-width: 300px) {
  .card-title { font-size: clamp(1rem, 4cqi, 1.5rem); }
}
```

---

## 6. Fluid Scaling with clamp()

### The Formula

```
clamp(minimum, preferred, maximum)
```

The preferred value is typically viewport-relative. The formula for calculating a preferred linear interpolation between two viewport widths:

```
preferred = (maxVal - minVal) / (maxVw - minVw) * 100vw + intercept
```

For practical use, this simplifies to patterns like `0.5rem + 2vw`.

### Common Recipes

```css
:root {
  /* Typography */
  --text-xs:      clamp(0.75rem,  0.7rem  + 0.25vw, 0.875rem);
  --text-sm:      clamp(0.875rem, 0.8rem  + 0.375vw, 1rem);
  --text-base:    clamp(1rem,     0.9rem  + 0.5vw,  1.125rem);
  --text-lg:      clamp(1.125rem, 1rem    + 0.625vw, 1.375rem);
  --text-xl:      clamp(1.25rem,  1rem    + 1.25vw, 1.75rem);
  --text-2xl:     clamp(1.5rem,   1rem    + 2vw,   2.25rem);
  --text-3xl:     clamp(1.875rem, 1rem    + 3vw,   3rem);
  --text-display: clamp(2.25rem,  1rem    + 5vw,   4.5rem);

  /* Spacing */
  --space-xs:      clamp(0.25rem, 0.5vw,   0.5rem);
  --space-sm:      clamp(0.5rem,  1vw,     0.75rem);
  --space-md:      clamp(0.75rem, 1.5vw,   1.25rem);
  --space-lg:      clamp(1rem,    2vw,     2rem);
  --space-xl:      clamp(1.5rem,  3vw,     3rem);
  --space-2xl:     clamp(2rem,    4vw,     4rem);
  --space-section: clamp(3rem,    5vw + 1rem, 8rem);

  /* Layout */
  --gap-cards:    clamp(1rem,    2vw,    2rem);
  --gap-grid:     clamp(1.5rem,  2.5vw,  3rem);
  --padding-page: clamp(1rem,    5vw,    4rem);
  --width-content: clamp(20rem,  90vw,   75rem);
}
```

### Fluid Padding Example

```css
.section {
  padding-block: clamp(3rem, 8vw, 8rem);
  padding-inline: clamp(1rem, 5vw, 4rem);
}
```

### Fluid Gap Example

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: clamp(1rem, 2vw, 2rem);
}
```

---

## 7. Breakpoint Transformation Catalog

### Navigation

| Breakpoint | xs (0-479) | sm (480-767) | md (768-1023) | lg (1024-1279) | xl+ (1280+) |
|------------|-----------|-------------|--------------|---------------|-------------|
| Top nav | Hamburger icon only | Hamburger + brand | Condensed links (4-5 items) | Full links + CTA | Full links + mega menu + CTA |
| Sidebar | Bottom sheet overlay | Bottom sheet overlay | Collapsed icons (56px wide) | Expanded (240px) | Expanded (280px) + sections |
| Bottom tabs | 5 icons visible | 5 icons + labels | Hidden | Hidden | Hidden |
| Breadcrumbs | Hidden or "< Back" | Truncated (first + last) | Last 3 levels | Full path | Full path |

```css
/* Navigation transformation */
.nav-links { display: none; }
.hamburger { display: flex; }
.bottom-tabs { display: flex; }

@media (min-width: 768px) {
  .nav-links { display: flex; }
  .hamburger { display: none; }
  .bottom-tabs { display: none; }
}
```

### Hero Section

| Breakpoint | xs | sm | md | lg+ |
|------------|----|----|----|----|
| Layout | Stacked: image top, text below | Stacked: image top, text below | Side-by-side 50/50 | Side-by-side 40/60 (text/image) |
| Heading | 2rem (clamp) | 2.5rem | 3rem | 4rem |
| CTA buttons | Full-width stack | Full-width stack | Inline row | Inline row + secondary |
| Background image | Cropped, dark overlay, text centered | Art-directed mobile crop | Full image | Full image, parallax optional |

### Feature Grid

| Breakpoint | xs | sm | md | lg | xl+ |
|------------|----|----|----|----|-----|
| Columns | 1 | 1 | 2 | 3 | 3-4 |
| Icon size | 32px | 40px | 48px | 48px | 56px |
| Description | 2 lines, truncated | Full | Full | Full | Full |

```css
.features {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(1.5rem, 3vw, 2.5rem);
}
@media (min-width: 768px) { .features { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .features { grid-template-columns: repeat(3, 1fr); } }
```

### Pricing Table

| Breakpoint | xs | sm | md | lg+ |
|------------|----|----|----|----|
| Layout | Stacked cards, vertical | Stacked cards | Horizontal scroll (snap) | Side-by-side columns |
| Featured plan | Badge only | Badge + border highlight | Badge + scale(1.02) | Badge + scale(1.05) + shadow |
| Feature comparison | Hidden, "See all features" link | Collapsed accordion | Visible scroll | Full table |

```css
.pricing {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
@media (min-width: 768px) {
  .pricing {
    flex-direction: row;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
  }
  .pricing > .plan {
    flex: 0 0 300px;
    scroll-snap-align: center;
  }
}
@media (min-width: 1280px) {
  .pricing {
    overflow-x: visible;
  }
  .pricing > .plan { flex: 1; }
}
```

### Testimonials

| Breakpoint | xs | sm | md | lg+ |
|------------|----|----|----|----|
| Layout | Vertical stack (1 visible) | Carousel (swipe) | 2-column grid | 3-column grid or masonry |
| Quote length | Truncated (3 lines) | Truncated (4 lines) | Full | Full |
| Avatar | 40px circle | 48px circle | 56px circle | 64px circle |

### Data Tables

| Breakpoint | xs | sm | md | lg+ |
|------------|----|----|----|----|
| Layout | Card stack (each row = card) | Card stack | Horizontal scroll with sticky first column | Full table |
| Columns visible | Key 2-3 fields only | Key 3-4 fields | All, scrollable | All |
| Sort/filter | Dropdown above | Dropdown above | Inline header sort | Inline header sort + filter row |

```css
/* Mobile: cards. Desktop: table */
.data-table { display: block; }
.data-table thead { display: none; }
.data-table tr {
  display: block;
  padding: 1rem;
  margin-bottom: 0.75rem;
  border: 1px solid var(--border);
  border-radius: 0.5rem;
}
.data-table td {
  display: flex;
  justify-content: space-between;
  padding: 0.25rem 0;
}
.data-table td::before {
  content: attr(data-label);
  font-weight: 600;
}

@media (min-width: 1024px) {
  .data-table { display: table; width: 100%; }
  .data-table thead { display: table-header-group; }
  .data-table tr { display: table-row; margin: 0; border: none; border-radius: 0; }
  .data-table td { display: table-cell; }
  .data-table td::before { display: none; }
}
```

### Sidebar Layout

| Breakpoint | xs | sm | md | lg+ |
|------------|----|----|----|----|
| Layout | Stacked sections (sidebar below main) | Stacked sections | Tab bar above content (sidebar content in tabs) | Side-by-side (sidebar + content) |
| Sidebar width | 100% | 100% | N/A (tabs) | 240-300px fixed |

### Dashboard

| Breakpoint | xs | sm | md | lg | xl+ |
|------------|----|----|----|----|-----|
| Grid | 1 column | 1 column | 2 columns | 3 columns | 4 columns |
| Priority | Critical metrics only, stacked | All metrics, stacked | Grouped widgets | Full dashboard | Full + ancillary data |
| Charts | Simplified / sparklines | Small charts | Medium charts | Full charts | Full + comparison overlays |
| Widget reorder | Priority-sorted (critical first) | Priority-sorted | Semi-arranged | Designed layout | Designed layout |

### Footer

| Breakpoint | xs | sm | md | lg+ |
|------------|----|----|----|----|
| Layout | Accordion sections | Accordion sections | 2-column grid | 4-column grid |
| Newsletter form | Full-width, stacked | Full-width, stacked | Inline (input + button) | Inline in its own column |
| Social icons | Centered row | Centered row | Left-aligned row | In designated column |

### Image Gallery

| Breakpoint | xs | sm | md | lg+ |
|------------|----|----|----|----|
| Layout | Vertical scroll (1-col) | 2-col grid | 3-col grid | Masonry (3-4 cols) |
| Lightbox | Full-screen | Full-screen with nav | Centered modal with nav | Centered modal + thumbnails |

### Forms

| Breakpoint | xs | sm | md | lg+ |
|------------|----|----|----|----|
| Layout | Single column, full width | Single column, max-width 480px | 2-column for related fields (name + surname) | 2-3 column groups, 600px max-width form |
| Labels | Above input | Above input | Above or beside (optional) | Beside input (optional) |
| Buttons | Full-width, stacked | Full-width | Inline, right-aligned | Inline, right-aligned |

### Stats / Metrics Row

| Breakpoint | xs | sm | md | lg+ |
|------------|----|----|----|----|
| Layout | Vertical stack | 2x2 grid | Horizontal row | Horizontal row with dividers |
| Number size | 1.5rem | 1.75rem | 2rem | 2.5rem |

```css
.stats {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}
@media (min-width: 480px) { .stats { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .stats { grid-template-columns: repeat(4, 1fr); } }
```

---

## 8. Responsive Typography

### Fluid Type Scale

```css
:root {
  --step--2: clamp(0.6944rem, 0.6576rem + 0.1836vw, 0.8rem);
  --step--1: clamp(0.8333rem, 0.7754rem + 0.2899vw, 1rem);
  --step-0:  clamp(1rem,      0.913rem  + 0.4348vw, 1.25rem);
  --step-1:  clamp(1.2rem,    1.0739rem + 0.6304vw, 1.5625rem);
  --step-2:  clamp(1.44rem,   1.2615rem + 0.8924vw, 1.9531rem);
  --step-3:  clamp(1.728rem,  1.4799rem + 1.2407vw, 2.4414rem);
  --step-4:  clamp(2.0736rem, 1.7334rem + 1.7012vw, 3.0518rem);
  --step-5:  clamp(2.4883rem, 2.027rem  + 2.3065vw, 3.8147rem);
}
```

### Responsive Line Length

Optimal reading: 45-75 characters per line. Target ~66ch.

```css
.prose {
  max-width: 65ch;
  margin-inline: auto;
  padding-inline: clamp(1rem, 5vw, 2rem);
}

/* Wider content blocks can go to 90ch */
.wide-content { max-width: 90ch; }

/* Full-bleed sections have no max-width on the outer container */
```

### Heading Scaling

```css
h1 { font-size: var(--step-5); line-height: 1.1; letter-spacing: -0.02em; }
h2 { font-size: var(--step-4); line-height: 1.15; letter-spacing: -0.015em; }
h3 { font-size: var(--step-3); line-height: 1.2; }
h4 { font-size: var(--step-2); line-height: 1.25; }
h5 { font-size: var(--step-1); line-height: 1.3; }
h6 { font-size: var(--step-0); line-height: 1.4; }
p  { font-size: var(--step-0); line-height: 1.6; }
```

---

## 9. Touch Target Scaling

### Minimum Sizes by Platform

| Platform | Minimum | Recommended |
|----------|---------|-------------|
| iOS (Apple HIG) | 44 x 44px | 44 x 44px |
| Android (Material 3) | 48 x 48dp | 48 x 48dp |
| WCAG 2.2 Level AA | 24 x 24px | 44 x 44px (AAA) |

### Implementation

```css
/* Ensure touch targets on mobile */
.btn, .nav-link, .form-control {
  min-height: 44px;
  min-width: 44px;
}

/* Increase spacing between interactive elements on touch */
@media (pointer: coarse) {
  .btn { min-height: 48px; padding: 0.75rem 1.25rem; }
  .nav-link { padding: 0.75rem 1rem; }
  .list-item-interactive { padding-block: 0.875rem; }
  .icon-btn { min-width: 48px; min-height: 48px; }
}

/* Tighter targets for precise pointer (mouse) */
@media (pointer: fine) {
  .btn { min-height: 36px; padding: 0.5rem 1rem; }
  .nav-link { padding: 0.375rem 0.75rem; }
}
```

### Spacing Between Touch Targets

Maintain at least 8px between adjacent interactive elements on touch devices to prevent mis-taps.

---

## 10. Responsive Images

### srcset for Resolution Switching

```html
<img
  src="image-800.jpg"
  srcset="image-400.jpg 400w,
          image-800.jpg 800w,
          image-1200.jpg 1200w,
          image-1600.jpg 1600w"
  sizes="(min-width: 1280px) 33vw,
         (min-width: 768px) 50vw,
         100vw"
  alt="Description"
  loading="lazy"
  decoding="async"
>
```

### Art Direction with picture

```html
<picture>
  <!-- Desktop: wide landscape crop -->
  <source media="(min-width: 1024px)" srcset="hero-wide.avif" type="image/avif">
  <source media="(min-width: 1024px)" srcset="hero-wide.webp" type="image/webp">

  <!-- Tablet: medium crop -->
  <source media="(min-width: 768px)" srcset="hero-medium.avif" type="image/avif">
  <source media="(min-width: 768px)" srcset="hero-medium.webp" type="image/webp">

  <!-- Mobile: portrait/square crop, different composition -->
  <source srcset="hero-mobile.avif" type="image/avif">
  <source srcset="hero-mobile.webp" type="image/webp">

  <img src="hero-fallback.jpg" alt="Hero image" loading="eager">
</picture>
```

### Aspect Ratio Preservation

```css
.responsive-image {
  width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  border-radius: 0.5rem;
}

/* Different aspect ratios per breakpoint */
.hero-image {
  aspect-ratio: 1 / 1;
}
@media (min-width: 768px) {
  .hero-image { aspect-ratio: 4 / 3; }
}
@media (min-width: 1280px) {
  .hero-image { aspect-ratio: 16 / 9; }
}
```

---

## 11. Modern CSS Techniques for Responsive Design

### Viewport Units

| Unit | Meaning | Use case |
|------|---------|----------|
| vw / vh | 1% of viewport width / height | General sizing |
| dvw / dvh | 1% of dynamic viewport (accounts for mobile browser chrome) | Mobile full-screen sections |
| svw / svh | 1% of small viewport (browser chrome visible) | Minimum guaranteed space |
| lvw / lvh | 1% of large viewport (browser chrome hidden) | Maximum available space |

```css
.hero {
  min-height: 100dvh; /* accounts for iOS Safari address bar */
  display: grid;
  place-items: center;
}
```

### Scroll Snap

```css
.carousel {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding-inline: 1rem;
  -webkit-overflow-scrolling: touch;
}
.carousel > .slide {
  flex: 0 0 min(85vw, 400px);
  scroll-snap-align: center;
}

/* Hide scrollbar but keep functionality */
.carousel {
  scrollbar-width: none;
}
.carousel::-webkit-scrollbar {
  display: none;
}
```

### Overscroll Behavior

```css
/* Prevent scroll chaining on modals and drawers */
.modal-body {
  overscroll-behavior: contain;
}

/* Prevent pull-to-refresh interference */
.app-shell {
  overscroll-behavior-y: none;
}
```

### Logical Properties for Responsive i18n

```css
.card {
  margin-inline: auto;
  padding-block: 1.5rem;
  padding-inline: 1rem;
  border-inline-start: 3px solid var(--accent);
}
```

### has() for Responsive-Aware Styling

```css
/* Adjust grid when sidebar is present */
.layout:has(.sidebar) {
  grid-template-columns: 280px 1fr;
}
.layout:not(:has(.sidebar)) {
  grid-template-columns: 1fr;
}

/* Form row that adjusts based on content */
.form-row:has(> :nth-child(2)) {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}
```

---

## 12. Responsive Testing

### Device Lab Essentials

Test on real devices for accurate touch, performance, and rendering:
- **Small phone**: iPhone SE or equivalent (375px)
- **Standard phone**: iPhone 15 / Pixel 8 (393-412px)
- **Large phone**: iPhone 15 Pro Max (430px)
- **Tablet portrait**: iPad Air (820px)
- **Tablet landscape**: iPad Air (1180px)
- **Laptop**: 1280-1440px
- **Desktop**: 1920px+

### Chrome DevTools Device Mode

1. Open DevTools (Cmd+Opt+I / F12)
2. Toggle device toolbar (Cmd+Shift+M)
3. Select device or enter custom dimensions
4. Test at each breakpoint boundary (479, 480, 767, 768, 1023, 1024, 1279, 1280, 1535, 1536)
5. Throttle network and CPU for realistic mobile performance
6. Test both portrait and landscape orientations

### Responsive Testing Checklist

**Layout**
- [ ] No horizontal scroll on any breakpoint (except intentional carousels)
- [ ] Content is readable without zooming on mobile
- [ ] Grid columns collapse correctly at each breakpoint
- [ ] No content overflow or clipping at breakpoint boundaries
- [ ] Spacing scales proportionally between breakpoints

**Typography**
- [ ] Body text is 16px minimum on mobile (prevents iOS zoom on focus)
- [ ] Line length stays within 45-75ch on all screen sizes
- [ ] Headings do not overflow their containers
- [ ] Fluid type scales smoothly, no sudden jumps

**Navigation**
- [ ] Mobile menu opens/closes reliably
- [ ] Active state is visible on touch devices
- [ ] No hover-dependent interactions on touch devices
- [ ] Bottom tab bar does not overlap content
- [ ] Breadcrumbs truncate gracefully

**Touch**
- [ ] All interactive elements meet 44px minimum target size
- [ ] Adequate spacing between touch targets (8px+)
- [ ] No double-tap-to-zoom issues
- [ ] Swipe gestures do not conflict with browser gestures

**Images and Media**
- [ ] Images load appropriate sizes per viewport (check Network tab)
- [ ] No layout shift from images loading (aspect-ratio set)
- [ ] Videos are responsive (width:100%, height:auto)
- [ ] Art direction changes look intentional at each breakpoint

**Forms**
- [ ] Input fields are full-width on mobile
- [ ] Keyboard does not obscure active input
- [ ] Select dropdowns work on all platforms
- [ ] Form labels are visible (not placeholder-only)

**Performance**
- [ ] Largest Contentful Paint under 2.5s on 4G
- [ ] Cumulative Layout Shift under 0.1
- [ ] No unnecessary assets loaded on mobile
- [ ] Fonts load without visible flash on mobile

---

## The 7 Transformation Strategies

A mental model for how any block can adapt across breakpoints:

1. **Reflow** — Multi-column to fewer columns (3-col grid to 2-col to 1-col)
2. **Reveal/Hide** — Show or hide elements by breakpoint (desktop mega menu vs mobile hamburger)
3. **Collapse** — Expand/collapse sections (tabs become accordion on mobile)
4. **Scale** — Proportional size changes using fluid values (headings: 60px to 48px to 36px)
5. **Relocate** — Move elements to different positions (sidebar becomes bottom sheet)
6. **Restructure** — Fundamentally change the layout pattern (table becomes card list)
7. **Prioritize** — Reorder by importance (most critical content first on small screens)

Every block transformation in Section 7 uses one or more of these strategies. When designing a new responsive block, run through this list to determine which strategies apply.

---

## Cross-References

- layout-block-intelligence, component-patterns-code, mobile-ux-design, page-composition-engine
- platform-visual-standards (iOS 26, Material 3 breakpoint conventions)
- form-design-encyclopedia (responsive form patterns)
- navigation-pattern-encyclopedia (responsive nav transformations)
- typography-pairing-recipes (fluid type scales)
- data-visualization-mastery (responsive chart patterns)
