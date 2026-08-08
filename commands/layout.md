---
description: "Generate responsive page layouts — CSS Grid, Flexbox, container queries, spacing rhythm, breakpoint transformations."
tier: "make"
---

# Layout — Responsive Page Layout Generator

Generate production-ready responsive page layouts using CSS Grid, Flexbox, and modern CSS techniques. Output complete Tailwind CSS code with container strategies, breakpoint transformations, and spacing rhythm systems.

## Generation Protocol

### Step 0: Gather Input

Before generating, collect:

1. **Layout pattern**: Which pattern does the user need?
   - **Sidebar + Content** — Fixed or collapsible sidebar with main content area
   - **Dashboard Grid** — Multi-panel grid with cards, charts, and data widgets
   - **Holy Grail** — Header, footer, sidebar(s), main content (classic three-column)
   - **Split View** — Two equal or weighted panels side by side
   - **Masonry** — Pinterest-style variable-height card grid
   - **Centered Content** — Single-column centered reading layout (blog, article, docs)
   - **Full-Bleed Hero** — Edge-to-edge hero section with contained content below
   - **Asymmetric** — Intentionally unequal columns for visual tension (portfolio, editorial)
   - **F-Pattern** — Optimized for scanning: top bar, left-weighted content blocks
   - **Card Grid** — Uniform card grid with responsive column count
   - **Stacked Sections** — Full-width alternating sections (landing page pattern)
   - **Custom** — User describes their own layout requirements

2. **Content type**: What goes inside this layout?
   - Dashboard with data widgets
   - Content/editorial (long text, images)
   - Product listing / catalog
   - Settings / admin panel
   - Marketing / landing page
   - Application shell (app chrome + workspace)

3. **Platform and viewport priorities**: Where will this layout live?
   - Mobile-first web (default)
   - Desktop-first (admin/dashboard)
   - Responsive web (all breakpoints)
   - Specific viewport (e.g., "only desktop 1440px")

4. **Prior Sumi outputs**: Check for `/wireframe` (layout structure), `/tokens` (spacing scale, breakpoints), `/taste` (density preferences). Consume if available.

If no pattern is specified, ask the user. Do not guess.

### Step 1: CONTAINER STRATEGY

Define the outermost containment rules before any internal layout.

**Container width system**:
```
/* Container scale — pick one based on content type */
--container-xs:   480px   /* Narrow forms, login, modals */
--container-sm:   640px   /* Centered text content, blog */
--container-md:   768px   /* Documentation, settings */
--container-lg:   1024px  /* Standard app layouts */
--container-xl:   1280px  /* Wide dashboards, catalogs */
--container-2xl:  1536px  /* Full-width data tables */
--container-full: 100%    /* Edge-to-edge (hero, full-bleed) */
```

**Container padding scale** (gutter between edge and content):
```
Mobile:   16px (px-4)
Tablet:   24px (px-6)
Desktop:  32px (px-8)
Wide:     48px (px-12) or auto-centering
```

**Container query zones** — use container queries when child components need to respond to their own container width rather than the viewport:
```css
.dashboard-panel {
  container-type: inline-size;
  container-name: panel;
}

@container panel (min-width: 400px) {
  .panel-content { grid-template-columns: 1fr 1fr; }
}

@container panel (max-width: 399px) {
  .panel-content { grid-template-columns: 1fr; }
}
```

**Output for this step**: Container wrapper class with max-width, padding, and centering. Tailwind example:
```html
<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
  <!-- Content -->
</div>
```

### Step 2: GRID STRUCTURE

Generate the primary grid or flex layout for the chosen pattern.

**Pattern: Sidebar + Content**
```html
<!-- Collapsible sidebar layout -->
<div class="flex min-h-screen">
  <!-- Sidebar -->
  <aside class="hidden lg:flex lg:w-64 lg:flex-col lg:fixed lg:inset-y-0">
    <div class="flex flex-col flex-grow border-r border-gray-200 bg-white pt-5 pb-4 overflow-y-auto">
      <!-- Sidebar content -->
    </div>
  </aside>

  <!-- Main content area — offset by sidebar width on desktop -->
  <main class="flex-1 lg:pl-64">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-6 sm:py-8 lg:py-10">
      <!-- Page content -->
    </div>
  </main>
</div>
```

Grid rules for sidebar pattern:
- Sidebar: fixed width (w-64 = 256px default), full height, scrollable independently
- Main: flex-1 to fill remaining width
- Mobile: sidebar hidden, revealed via hamburger overlay or sheet
- Tablet: optional mini sidebar (w-16 = 64px, icons only)
- Desktop: full sidebar with labels

**Pattern: Dashboard Grid**
```html
<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-6">
  <!-- Dashboard grid -->
  <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4 lg:gap-6">
    <!-- Stat cards — span 1 column each -->
    <div class="rounded-lg bg-white p-4 shadow-sm ring-1 ring-gray-950/5">
      <!-- Stat card content -->
    </div>
    <!-- Repeat for each stat -->
  </div>

  <!-- Main content grid — below stats -->
  <div class="mt-6 grid grid-cols-1 gap-6 lg:grid-cols-3">
    <!-- Primary content — spans 2 columns on desktop -->
    <div class="lg:col-span-2 rounded-lg bg-white p-6 shadow-sm ring-1 ring-gray-950/5">
      <!-- Chart, table, or primary content -->
    </div>

    <!-- Secondary content — spans 1 column -->
    <div class="rounded-lg bg-white p-6 shadow-sm ring-1 ring-gray-950/5">
      <!-- Activity feed, quick actions, etc. -->
    </div>
  </div>
</div>
```

Grid rules for dashboard pattern:
- Top row: 1 col mobile, 2 col tablet, 4 col desktop for stat cards
- Content area: 1 col mobile, stacked; 3-col desktop with 2:1 split
- Gap: 16px mobile (gap-4), 24px desktop (gap-6)
- Each panel uses container queries for internal layout

**Pattern: Holy Grail**
```html
<div class="min-h-screen flex flex-col">
  <!-- Header -->
  <header class="sticky top-0 z-40 border-b border-gray-200 bg-white">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 h-16 flex items-center">
      <!-- Header content -->
    </div>
  </header>

  <!-- Body: sidebars + main -->
  <div class="flex-1 flex">
    <!-- Left sidebar -->
    <aside class="hidden lg:block lg:w-64 border-r border-gray-200 bg-gray-50 overflow-y-auto">
      <!-- Left nav -->
    </aside>

    <!-- Main content -->
    <main class="flex-1 overflow-y-auto">
      <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-8">
        <!-- Content -->
      </div>
    </main>

    <!-- Right sidebar (optional) -->
    <aside class="hidden xl:block xl:w-72 border-l border-gray-200 bg-gray-50 overflow-y-auto">
      <!-- Right sidebar: TOC, related, etc. -->
    </aside>
  </div>

  <!-- Footer -->
  <footer class="border-t border-gray-200 bg-white">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-6">
      <!-- Footer content -->
    </div>
  </footer>
</div>
```

**Pattern: Split View**
```html
<div class="flex min-h-screen">
  <!-- Left panel (list/nav) -->
  <div class="w-full sm:w-80 lg:w-96 border-r border-gray-200 bg-white overflow-y-auto flex-shrink-0">
    <!-- List or navigation panel -->
  </div>

  <!-- Right panel (detail/content) -->
  <div class="hidden sm:flex sm:flex-1 overflow-y-auto">
    <div class="flex-1 p-6 lg:p-8">
      <!-- Detail content -->
    </div>
  </div>
</div>
```

Split view rules:
- Mobile: only left panel visible; right panel shown via navigation (not side-by-side)
- Tablet: both panels, left panel fixed width (320px)
- Desktop: both panels, left panel wider (384px), content fills remaining
- Draggable divider (optional enhancement)

**Pattern: Masonry**
```html
<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
  <!-- CSS Columns masonry (most reliable cross-browser) -->
  <div class="columns-1 sm:columns-2 lg:columns-3 xl:columns-4 gap-4 space-y-4">
    <div class="break-inside-avoid rounded-lg bg-white p-4 shadow-sm ring-1 ring-gray-950/5">
      <!-- Card with variable height -->
    </div>
    <!-- Repeat -->
  </div>
</div>

<!-- Alternative: CSS Grid masonry (Chrome 128+, Firefox 128+) -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4"
     style="grid-template-rows: masonry;">
  <!-- Cards -->
</div>
```

**Pattern: Centered Content**
```html
<div class="min-h-screen bg-white">
  <!-- Narrow centered container for reading -->
  <article class="mx-auto max-w-2xl px-4 sm:px-6 py-12 sm:py-16 lg:py-20">
    <!-- Prose content -->
    <div class="prose prose-lg prose-gray max-w-none">
      <!-- Headings, paragraphs, images, code blocks -->
    </div>
  </article>
</div>
```

Centered content rules:
- Max-width: 672px (max-w-2xl) for optimal 60-75 character line length
- Generous vertical padding that scales with viewport
- Images can break out: negative margins or full-bleed within the centered column
- Use `prose` utility for typographic rhythm

**Pattern: Full-Bleed Hero**
```html
<div class="min-h-screen">
  <!-- Full-bleed hero — no container constraint -->
  <section class="relative isolate overflow-hidden bg-gray-900 px-6 py-24 sm:py-32 lg:px-8">
    <!-- Background image or gradient -->
    <div class="absolute inset-0 -z-10">
      <img src="..." alt="" class="h-full w-full object-cover opacity-20" />
    </div>
    <!-- Centered hero content -->
    <div class="mx-auto max-w-2xl text-center">
      <h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">
        <!-- Headline -->
      </h1>
      <p class="mt-6 text-lg leading-8 text-gray-300">
        <!-- Subheadline -->
      </p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <!-- CTA buttons -->
      </div>
    </div>
  </section>

  <!-- Contained content below hero -->
  <section class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-16 sm:py-24">
    <!-- Regular contained content -->
  </section>
</div>
```

**Pattern: Asymmetric**
```html
<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-12">
  <!-- Asymmetric grid: 5/7 or 4/8 split -->
  <div class="grid grid-cols-1 gap-8 lg:grid-cols-12 lg:gap-12">
    <!-- Narrow column — 5 of 12 -->
    <div class="lg:col-span-5">
      <!-- Sticky text, description, or navigation -->
      <div class="lg:sticky lg:top-8">
        <!-- Content that stays visible while right column scrolls -->
      </div>
    </div>

    <!-- Wide column — 7 of 12 -->
    <div class="lg:col-span-7">
      <!-- Images, portfolio pieces, or primary content -->
    </div>
  </div>
</div>
```

### Step 3: RESPONSIVE TRANSFORMATION RULES

Define exactly what happens at each breakpoint. Do not leave responsive behavior as an afterthought.

**Breakpoint system** (Tailwind defaults):
```
sm:   640px   — Large phones / small tablets
md:   768px   — Tablets portrait
lg:   1024px  — Tablets landscape / small laptops
xl:   1280px  — Laptops / desktops
2xl:  1536px  — Large desktops
```

**Transformation rules per pattern**:

| Pattern | Mobile (<640px) | Tablet (640-1023px) | Desktop (1024px+) |
|---------|----------------|--------------------|--------------------|
| Sidebar + Content | Sidebar hidden, hamburger trigger, full-width content | Mini sidebar (64px, icons only) + content | Full sidebar (256px) + content |
| Dashboard Grid | Single column, stat cards stack, panels stack | 2-column stat grid, panels stack | 4-col stats, 3-col content (2+1 split) |
| Holy Grail | No sidebars, single column | Left sidebar visible, no right sidebar | Both sidebars visible |
| Split View | Single panel with navigation between panels | Both panels, fixed left (320px) | Both panels, wider left (384px) |
| Masonry | 1 column | 2 columns | 3-4 columns |
| Centered Content | Full width with 16px padding | Same with 24px padding | Max-width 672px centered |
| Full-Bleed Hero | Reduced padding, smaller text | Medium padding, medium text | Full padding, large text |
| Asymmetric | Stacked (narrow on top, wide below) | Stacked or light asymmetry | Full asymmetric grid |

**Common responsive patterns to apply**:

1. **Stack on mobile**: Multi-column layouts become single-column
   ```html
   <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
   ```

2. **Hide on mobile, show on desktop**:
   ```html
   <div class="hidden lg:block"><!-- Desktop only --></div>
   <div class="lg:hidden"><!-- Mobile only --></div>
   ```

3. **Reduce spacing on mobile**:
   ```html
   <div class="p-4 sm:p-6 lg:p-8">
   <div class="gap-4 lg:gap-6">
   <div class="py-12 sm:py-16 lg:py-24">
   ```

4. **Scale typography**:
   ```html
   <h1 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl">
   ```

5. **Reorder on mobile** (put important content first):
   ```html
   <div class="order-2 lg:order-1"><!-- Secondary on mobile --></div>
   <div class="order-1 lg:order-2"><!-- Primary on mobile (shows first) --></div>
   ```

### Step 4: CONTAINER QUERIES

Use container queries when components need to respond to their container size, not the viewport. This is critical for dashboard panels, sidebar content, and reusable card components.

**When to use container queries vs. media queries**:
- **Media queries**: Page-level layout (grid columns, sidebar visibility)
- **Container queries**: Component-level layout (card internals, widget arrangement)

**Implementation pattern**:
```html
<!-- Parent: declare as container -->
<div class="@container">
  <!-- Child: respond to container width -->
  <div class="flex flex-col @sm:flex-row @sm:items-center gap-4">
    <img class="w-full @sm:w-24 @sm:h-24 rounded-lg object-cover" />
    <div class="flex-1">
      <h3 class="font-semibold">Title</h3>
      <p class="text-sm text-gray-600">Description</p>
    </div>
    <button class="@sm:ml-auto">Action</button>
  </div>
</div>
```

**Tailwind container query breakpoints** (with `@tailwindcss/container-queries`):
```
@xs:   20rem (320px)
@sm:   24rem (384px)
@md:   28rem (448px)
@lg:   32rem (512px)
@xl:   36rem (576px)
@2xl:  42rem (672px)
@3xl:  48rem (768px)
```

**Dashboard panel example with container queries**:
```html
<div class="@container rounded-lg bg-white p-4 shadow-sm ring-1 ring-gray-950/5">
  <!-- Stat card: vertical on narrow, horizontal on wide -->
  <div class="flex flex-col @md:flex-row @md:items-center @md:justify-between gap-2">
    <div>
      <p class="text-sm text-gray-500">Total Revenue</p>
      <p class="text-2xl @lg:text-3xl font-bold text-gray-900">$48,290</p>
    </div>
    <div class="hidden @md:block">
      <!-- Sparkline chart — only shows when panel is wide enough -->
    </div>
  </div>
</div>
```

### Step 5: SPACING RHYTHM SYSTEM

Define the vertical spacing between major page sections for visual rhythm and hierarchy.

**Section spacing scale** (vertical padding between page sections):
```
/* Tight (data-dense dashboards, admin) */
--section-xs:   py-6  sm:py-8              /* 24px → 32px */
--section-sm:   py-8  sm:py-10             /* 32px → 40px */
--section-md:   py-10 sm:py-12             /* 40px → 48px */

/* Standard (most applications) */
--section-sm:   py-8  sm:py-12             /* 32px → 48px */
--section-md:   py-12 sm:py-16             /* 48px → 64px */
--section-lg:   py-16 sm:py-20 lg:py-24   /* 64px → 80px → 96px */

/* Generous (marketing, editorial, portfolio) */
--section-md:   py-16 sm:py-20             /* 64px → 80px */
--section-lg:   py-20 sm:py-24 lg:py-32   /* 80px → 96px → 128px */
--section-xl:   py-24 sm:py-32 lg:py-40   /* 96px → 128px → 160px */
```

**Vertical rhythm rules**:
1. **Hero sections**: Largest spacing (section-lg or section-xl)
2. **Content sections**: Medium spacing (section-md)
3. **Related/grouped sections**: Tight spacing (section-sm) — Gestalt proximity signals they belong together
4. **Section dividers**: Use either spacing alone OR a border, not both
5. **Consistent direction**: Increase spacing as you move down the page (creates visual deceleration)

**Internal component spacing**:
```
/* Stack spacing — vertical gap between sibling elements */
space-y-1   (4px)    — Tight: label + input, icon + text
space-y-2   (8px)    — Related: list items, form fields
space-y-4   (16px)   — Grouped: card sections, form groups
space-y-6   (24px)   — Separated: distinct content blocks
space-y-8   (32px)   — Major: page sections within a container
space-y-12  (48px)   — Hero: major landmark divisions
```

### Step 6: GRID OVERLAY VISUALIZATION

Describe the grid structure so the developer can verify alignment:

**Grid overlay description format**:
```
GRID OVERLAY — [Pattern Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Viewport: 1280px (xl breakpoint)
Container: 1280px max-width, 32px side padding = 1216px content area
Columns: 12
Gutter: 24px (gap-6)
Column width: (1216 - 11 * 24) / 12 = 79.3px

Layout mapping:
  Sidebar:     cols 1-3   (256px fixed, outside grid)
  Main:        cols 1-8   (of remaining 12)
  Right panel: cols 9-12  (of remaining 12)

Vertical grid:
  Header:      64px fixed
  Content:     flex-1 (fills remaining viewport height)
  Footer:      auto (content-driven)

Alignment checkpoints:
  ✓ All text left edges align to column starts
  ✓ Cards span full columns (no partial-column cards)
  ✓ Gutters are consistent (24px everywhere)
  ✓ Section padding follows the spacing rhythm scale
```

### Step 7: COMPLETE LAYOUT OUTPUT

Combine all steps into a single, complete, copy-paste-ready layout.

**Output requirements**:
- Full HTML structure with Tailwind classes
- Every responsive breakpoint accounted for
- Container queries where appropriate (dashboard panels, reusable cards)
- Spacing rhythm applied consistently
- Comments explaining responsive transformations
- Semantic HTML landmarks (header, main, nav, aside, footer)
- Grid overlay description for verification

## Output Format

```
## Page Layout: [Pattern Name]

### Configuration
- **Pattern**: [sidebar+content / dashboard grid / holy grail / etc.]
- **Content type**: [dashboard / editorial / catalog / etc.]
- **Container**: [max-width, padding strategy]
- **Breakpoints**: [which breakpoints trigger changes]

### Complete Layout Code

[Full HTML + Tailwind code with all responsive classes, container queries, and spacing]

### Responsive Transformation Table

| Element | Mobile | Tablet | Desktop |
|---------|--------|--------|---------|
| [element] | [behavior] | [behavior] | [behavior] |

### Grid Overlay

[ASCII grid description showing column structure, gutters, and alignment points]

### Spacing Rhythm

| Section | Vertical Padding | Rationale |
|---------|-----------------|-----------|
| [section] | [classes] | [why this spacing] |

### Container Query Components

[Any components using container queries, with the @container setup]

### Integration Notes
- **With `/tokens`**: Map spacing scale to your design token values
- **With `/nav`**: Drop navigation component into the header/sidebar slots
- **With `/form`**: Forms use the centered content container (max-w-2xl)
- **With `/screen`**: This layout becomes the shell for screen generation
```

## Quality Gates

The output MUST include:
- [ ] Complete HTML structure with Tailwind classes — copy-paste ready
- [ ] Container strategy defined (max-width, padding, centering)
- [ ] Responsive behavior at all relevant breakpoints (not just "stacks on mobile")
- [ ] Container queries used where components need container-aware sizing
- [ ] Spacing rhythm documented and consistent
- [ ] Semantic HTML landmarks (header, main, nav, aside, footer)
- [ ] Grid overlay description for developer verification
- [ ] Mobile layout designed intentionally (not a degraded desktop)

The output MUST NOT include:
- Layouts with no responsive behavior
- Vague descriptions instead of code ("use a grid here")
- Fixed pixel widths that break on different viewports
- Missing mobile layout (desktop-only code)
- Inconsistent spacing (random padding values with no system)

## Cross-References

When generating layouts, draw knowledge from:
- `responsive-block-patterns` skill — cross-breakpoint transformation catalog, container queries, fluid scaling
- `page-composition-engine` skill — full-page composition recipes with block stacking order
- `layout-block-intelligence` skill — 500+ layout section/block patterns
- `screen-flow-patterns` skill — screen type catalog with canonical layouts
- `visual-design-mastery` skill — composition rules, grid systems, rule of thirds
- `platform-visual-standards` skill — platform-specific layout conventions
- `cognitive-psychology-ux` skill — scanning patterns (F-pattern, Z-pattern), Gestalt proximity

## Next Step

**Next** -> `/nav` — Generate the navigation component to place inside this layout shell

**Alternatives**:
- `/form` — Build forms that live inside this layout
- `/screen` — Generate full screens using this layout as the structural foundation
- `/tokens` — Generate design tokens to power the spacing and sizing values
- `/guide` — See the full journey map
