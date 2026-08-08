---
name: responsive
description: "Generate responsive behavior for any screen or component — breakpoints, container queries, fluid scaling, block transformations, and touch targets."
argument-hint: "[screen, block, or component]"
---

# Responsive — Responsive Transformation Generator

## Before running

This command needs a screen, block, or component to make responsive.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate complete responsive CSS for any screen layout or component. Handles breakpoint strategy, container queries, fluid type and spacing with `clamp()`, block-level transformation rules, touch target scaling, and modern viewport units.

## Core Principles

1. **Mobile-first always.** Start with the smallest screen and layer up with `min-width` queries. Never start desktop and scale down.
2. **Content determines breakpoints, not devices.** Set breakpoints where the layout breaks, not at arbitrary device widths.
3. **Fluid over fixed.** Use `clamp()` for type and spacing so values scale smoothly between breakpoints instead of jumping.
4. **Container queries for components.** Components should respond to their container, not the viewport. Reserve viewport queries for page-level layout.
5. **Touch targets are non-negotiable.** 44px minimum on iOS, 48px minimum on Android. No exceptions.

## Generation Protocol

1. **Gather inputs.**

   **Required:**
   - What to make responsive: a specific screen layout, component, or "full page"
   - Existing code or screen type (from `/screen` output, custom code, or description)
   - Primary platform: web (responsive), native (adaptive), or both

   **Optional:**
   - Breakpoint preference: default system, custom values, or "content-first"
   - Token system reference (from `/tokens` or `.sumi/style.json`)
   - Target devices: phone, tablet, laptop, desktop, ultrawide
   - Orientation handling: portrait-only, landscape-only, or both

2. **Define breakpoint strategy.**

   ### Default Breakpoint Scale (mobile-first)
   ```css
   /* Base: 0–479px    — phone portrait */
   /* sm:  480–767px   — phone landscape / small tablet */
   /* md:  768–1023px  — tablet portrait */
   /* lg:  1024–1279px — tablet landscape / laptop */
   /* xl:  1280–1535px — desktop */
   /* 2xl: 1536px+     — large desktop / ultrawide */

   @media (min-width: 480px)  { /* sm  */ }
   @media (min-width: 768px)  { /* md  */ }
   @media (min-width: 1024px) { /* lg  */ }
   @media (min-width: 1280px) { /* xl  */ }
   @media (min-width: 1536px) { /* 2xl */ }
   ```

   ### Content-First Breakpoints
   When "content-first" is selected, do not use fixed values. Instead:
   1. Set the base layout at narrow width
   2. Increase viewport width until the layout visually breaks
   3. Set a breakpoint at that width
   4. Repeat until the widest target

   Express these as `em`-based breakpoints for zoom resilience:
   ```css
   @media (min-width: 30em)  { /* ~480px  — first break */ }
   @media (min-width: 48em)  { /* ~768px  — second break */ }
   @media (min-width: 64em)  { /* ~1024px — third break */ }
   ```

   ### Tailwind v4 Breakpoints
   ```css
   @theme {
     --breakpoint-sm: 480px;
     --breakpoint-md: 768px;
     --breakpoint-lg: 1024px;
     --breakpoint-xl: 1280px;
     --breakpoint-2xl: 1536px;
   }
   ```

3. **Generate container queries for component-level responsiveness.**

   Components should not care about viewport width. They should respond to their own container.

   ```css
   /* Define containment on the parent */
   .card-grid {
     container-type: inline-size;
     container-name: card-grid;
   }

   /* Component responds to its container width */
   .card {
     display: grid;
     grid-template-columns: 1fr;
     gap: var(--space-300);
   }

   @container card-grid (min-width: 400px) {
     .card {
       grid-template-columns: auto 1fr;
     }
   }

   @container card-grid (min-width: 700px) {
     .card {
       grid-template-columns: 200px 1fr auto;
     }
   }
   ```

   ### When to Use Container vs. Viewport Queries

   | Use Case | Query Type | Reason |
   |----------|-----------|--------|
   | Page layout (grid columns, sidebar) | `@media` (viewport) | Layout depends on total available width |
   | Navigation pattern switch | `@media` (viewport) | Nav affects the whole page |
   | Card layout within a grid | `@container` | Card might be in a sidebar or main area |
   | Table/data display | `@container` | Table may be full-width or in a panel |
   | Form field arrangement | `@container` | Form may appear in modal, sidebar, or page |
   | Component internal layout | `@container` | Always — components should be portable |

4. **Generate fluid scaling with `clamp()`.**

   ### Fluid Typography
   Instead of jumping between fixed sizes at breakpoints, use `clamp()` for smooth scaling:

   ```css
   /* Formula: clamp(min, preferred, max)
      Preferred uses viewport width for fluid scaling
      calc formula: min + (max - min) * ((100vw - minViewport) / (maxViewport - minViewport)) */

   :root {
     /* Body text: 16px at 320px → 18px at 1280px */
     --font-size-base: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);

     /* H1: 28px at 320px → 48px at 1280px */
     --font-size-display: clamp(1.75rem, 1.25rem + 2.5vw, 3rem);

     /* H2: 24px at 320px → 36px at 1280px */
     --font-size-heading-lg: clamp(1.5rem, 1.15rem + 1.75vw, 2.25rem);

     /* H3: 20px at 320px → 28px at 1280px */
     --font-size-heading-md: clamp(1.25rem, 1.05rem + 1vw, 1.75rem);

     /* Small: 14px at 320px → 14px (does not scale) */
     --font-size-sm: 0.875rem;
   }
   ```

   ### Fluid Spacing
   ```css
   :root {
     /* Section padding: 24px at 320px → 64px at 1280px */
     --space-section: clamp(1.5rem, 0.5rem + 5vw, 4rem);

     /* Page inline padding: 16px at 320px → 48px at 1280px */
     --space-page-inline: clamp(1rem, 0.25rem + 3.75vw, 3rem);

     /* Component gap: 12px at 320px → 24px at 1280px */
     --space-gap: clamp(0.75rem, 0.5rem + 1.25vw, 1.5rem);

     /* Card padding: 16px at 320px → 32px at 1280px */
     --space-card-padding: clamp(1rem, 0.5rem + 2.5vw, 2rem);
   }
   ```

   ### Fluid Spacing (Tailwind v4 Utility)
   ```css
   @utility fluid-p-* {
     padding: clamp(1rem, calc(0.5rem + value(--modifier) * 1vw), calc(value(--modifier) * 0.5rem));
   }
   ```

5. **Generate block transformation rules.**

   Each block type has specific responsive behavior:

   ### Hero Section
   ```css
   .hero {
     display: grid;
     grid-template-columns: 1fr;
     gap: var(--space-gap);
     padding: var(--space-section) var(--space-page-inline);
     text-align: center;
     min-height: 100dvh; /* dynamic viewport height */
   }

   @media (min-width: 768px) {
     .hero {
       grid-template-columns: 1fr 1fr;
       text-align: left;
       min-height: auto;
       align-items: center;
     }
   }

   @media (min-width: 1280px) {
     .hero {
       grid-template-columns: 1.2fr 0.8fr;
       max-width: 1280px;
       margin-inline: auto;
     }
   }
   ```

   ### Navigation
   ```css
   /* Mobile: bottom tab bar or hamburger */
   .nav {
     position: fixed;
     bottom: 0;
     left: 0;
     right: 0;
     display: flex;
     justify-content: space-around;
     padding: var(--space-200) var(--space-page-inline);
     background: var(--color-bg-surface);
     border-top: 1px solid var(--color-border-subtle);
     z-index: var(--z-sticky);
   }

   .nav-desktop { display: none; }

   @media (min-width: 768px) {
     .nav {
       position: static;
       border-top: none;
       border-bottom: 1px solid var(--color-border-subtle);
       justify-content: flex-start;
       gap: var(--space-400);
     }
     .nav-mobile-only { display: none; }
     .nav-desktop { display: flex; }
   }
   ```

   ### Grid Layouts
   ```css
   .feature-grid {
     display: grid;
     grid-template-columns: 1fr;
     gap: var(--space-gap);
   }

   @media (min-width: 480px) {
     .feature-grid {
       grid-template-columns: repeat(2, 1fr);
     }
   }

   @media (min-width: 1024px) {
     .feature-grid {
       grid-template-columns: repeat(3, 1fr);
     }
   }

   @media (min-width: 1280px) {
     .feature-grid {
       grid-template-columns: repeat(4, 1fr);
     }
   }
   ```

   ### Data Table
   ```css
   /* Mobile: stack rows as cards */
   @media (max-width: 767px) {
     .data-table thead { display: none; }
     .data-table tr {
       display: grid;
       grid-template-columns: 1fr 1fr;
       gap: var(--space-100);
       padding: var(--space-300);
       border-bottom: 1px solid var(--color-border-subtle);
     }
     .data-table td::before {
       content: attr(data-label);
       font-weight: 600;
       font-size: var(--font-size-sm);
       color: var(--color-text-secondary);
     }
   }

   /* Tablet+: standard table */
   @media (min-width: 768px) {
     .data-table {
       width: 100%;
       border-collapse: collapse;
     }
     .data-table th,
     .data-table td {
       padding: var(--space-200) var(--space-300);
       text-align: left;
       border-bottom: 1px solid var(--color-border-subtle);
     }
   }

   /* Desktop: add horizontal scroll only if needed */
   .data-table-wrapper {
     overflow-x: auto;
     -webkit-overflow-scrolling: touch;
   }
   ```

   ### Sidebar Layout
   ```css
   .layout-with-sidebar {
     display: grid;
     grid-template-columns: 1fr;
   }

   .sidebar {
     order: 2; /* Below main on mobile */
     padding: var(--space-card-padding);
   }

   @media (min-width: 768px) {
     .layout-with-sidebar {
       grid-template-columns: 280px 1fr;
     }
     .sidebar {
       order: 0;
       position: sticky;
       top: var(--space-400);
       align-self: start;
       max-height: calc(100dvh - var(--space-800));
       overflow-y: auto;
     }
   }

   @media (min-width: 1280px) {
     .layout-with-sidebar {
       grid-template-columns: 320px 1fr;
     }
   }
   ```

   ### Form Layout
   ```css
   .form-grid {
     display: grid;
     grid-template-columns: 1fr;
     gap: var(--space-400);
   }

   @media (min-width: 480px) {
     .form-grid {
       grid-template-columns: repeat(2, 1fr);
     }
     .form-grid .full-width {
       grid-column: 1 / -1;
     }
   }

   @media (min-width: 768px) {
     .form-grid {
       grid-template-columns: repeat(3, 1fr);
       max-width: 720px;
     }
   }
   ```

6. **Touch target scaling.**

   All interactive elements must meet minimum touch target sizes:

   ```css
   /* Minimum touch targets */
   .touch-target {
     min-width: 44px;   /* iOS HIG */
     min-height: 44px;  /* iOS HIG */
     display: inline-flex;
     align-items: center;
     justify-content: center;
   }

   /* Android: 48dp minimum */
   @media (pointer: coarse) {
     .touch-target {
       min-width: 48px;
       min-height: 48px;
     }

     /* Increase spacing between adjacent targets */
     .touch-target + .touch-target {
       margin-left: 8px;
     }

     /* Larger tap areas for inline links in text */
     a {
       padding-block: 4px;
     }
   }

   /* Fine pointer: can be smaller */
   @media (pointer: fine) {
     .touch-target-compact {
       min-width: 32px;
       min-height: 32px;
     }
   }

   /* Touch-specific: increase hit area without increasing visual size */
   .touch-expand {
     position: relative;
   }
   .touch-expand::after {
     content: '';
     position: absolute;
     inset: -8px; /* Expand by 8px in all directions */
   }
   ```

7. **Viewport units — modern approach.**

   Use dynamic viewport units for reliable height calculations:

   ```css
   /* dvh: accounts for mobile browser chrome (address bar, toolbar)
      svh: smallest possible viewport (chrome visible)
      lvh: largest possible viewport (chrome hidden) */

   /* Full-height section — use dvh for mobile, vh for desktop */
   .full-height {
     min-height: 100dvh;
   }

   /* Fallback for older browsers */
   @supports not (min-height: 100dvh) {
     .full-height {
       min-height: 100vh;
       min-height: -webkit-fill-available;
     }
   }

   /* Fixed bottom bar — account for safe areas */
   .bottom-bar {
     position: fixed;
     bottom: 0;
     left: 0;
     right: 0;
     padding-bottom: env(safe-area-inset-bottom, 0px);
   }

   /* Notch-safe horizontal padding */
   .safe-padding {
     padding-left: max(var(--space-page-inline), env(safe-area-inset-left));
     padding-right: max(var(--space-page-inline), env(safe-area-inset-right));
   }
   ```

8. **Generate complete responsive CSS for the input.**

   Combine all strategies into a single, complete stylesheet for the provided screen or component. Include:
   - All breakpoint rules
   - Fluid values
   - Container queries where appropriate
   - Touch target enforcement
   - Viewport unit handling
   - Safe area support
   - Print styles (if applicable)

   ### Print Styles (when relevant)
   ```css
   @media print {
     .no-print { display: none !important; }
     .nav, .sidebar, .bottom-bar { display: none !important; }
     body { font-size: 12pt; color: #000; background: #fff; }
     a { color: #000; text-decoration: underline; }
     a[href]::after { content: " (" attr(href) ")"; font-size: 0.8em; }
   }
   ```

## Responsive Testing Checklist

| Check | What to Verify | How to Test |
|-------|---------------|-------------|
| No horizontal scroll | Page does not scroll horizontally at any width | Drag browser from 320px to 2560px |
| Text readable at 320px | Body text minimum 16px, no overflow | Viewport at 320px |
| Touch targets met | All interactive elements 44px+ on touch devices | Chrome DevTools mobile emulation |
| Images responsive | No images overflow container, proper aspect ratios | Resize viewport |
| Fluid type smooth | Text scales smoothly without jumps | Slowly resize viewport |
| Container queries work | Components adapt to their container, not viewport | Place component in sidebar vs. full-width |
| Safe areas respected | No content hidden by notch or home indicator | iOS Safari testing |
| Landscape usable | Layout works in landscape orientation | Rotate mobile emulator |
| Zoom functional | Layout holds at 200% zoom (WCAG) | Browser zoom to 200% |
| Focus order logical | Tab order matches visual order at all breakpoints | Tab through at each breakpoint |

## Output Format

```
### Phase Position
> **Phase: BUILD** | `/responsive`
> *Responsive Design | Adaptive Transformation*

## Responsive System: [Screen/Component Name]

### Breakpoint Strategy
- **Approach**: [mobile-first / content-first]
- **Breakpoints**: [values with rationale]
- **Container queries**: [which components use them]

### Fluid Scaling
[clamp() values for type, spacing, padding]

### Block Transformations
[Per-block responsive behavior with complete CSS]

### Touch Target Audit
[Interactive elements with touch target sizes verified]

### Viewport Handling
[dvh/svh usage and safe area implementation]

### Complete CSS
[Full responsive stylesheet combining all strategies]

### Testing Checklist
[Verified checklist with pass/fail per check]
```

## Cross-References

When generating responsive behavior, draw from:
- `responsive-block-patterns` skill for cross-breakpoint transformation catalog
- `screen-flow-patterns` skill for screen type responsive conventions
- `mobile-ux-design` skill for iOS and Android responsive patterns
- `platform-visual-standards` skill for device-specific standards
- `accessibility-inclusive-design` skill for responsive accessibility (touch targets, zoom, reflow)
- `component-patterns-code` skill for responsive component implementation
- `design-systems-architecture` skill for responsive token architecture

## Next Step

**Next** → `/screen` — Build complete screen layouts with responsive behavior

**Alternatives**:
- `/tokens` — Generate the token system that responsive values reference
- `/dark` — Add dark mode to your responsive layout
- `/component` — Build responsive components directly
- `/sumi` — See the full journey
