# Elevation Hierarchy — Z-Index, Stacking Contexts & Surface Systems

## Z-Index Scale System

A well-defined z-index scale prevents the "z-index: 99999" anti-pattern. Every elevation level has a purpose. Arbitrary z-index values lead to unpredictable stacking and fragile CSS.

### Recommended Z-Index Scale

```css
:root {
  /* ---- Semantic z-index scale ---- */
  --z-deep:             -1;     /* Behind base content */
  --z-base:              0;     /* Default layer, page content */
  --z-raised:            1;     /* Slightly above siblings */
  --z-dropdown:        100;     /* Dropdown menus, selects */
  --z-sticky:          200;     /* Sticky headers, sidebars */
  --z-fixed:           300;     /* Fixed navigation, FABs */
  --z-drawer:          350;     /* Side drawers, off-canvas panels */
  --z-modal-backdrop:  400;     /* Modal/dialog backdrop overlay */
  --z-modal:           500;     /* Modal dialogs */
  --z-popover:         600;     /* Popovers, floating panels */
  --z-tooltip:         700;     /* Tooltips */
  --z-toast:           800;     /* Toast notifications, snackbars */
  --z-command-palette: 900;     /* Command palette, spotlight search */
  --z-dev-tools:       950;     /* Debug overlays, dev panels */
  --z-max:             999;     /* Absolute maximum — emergency only */
}
```

### Why These Values Have Gaps

The 100-point gaps between major levels allow for sub-layers without restructuring the system:

```css
/* If a sticky element needs to be above another sticky element: */
.sticky-header   { z-index: var(--z-sticky); }        /* 200 */
.sticky-toolbar  { z-index: calc(var(--z-sticky) + 1); } /* 201 */
.sticky-submenu  { z-index: calc(var(--z-sticky) + 10); } /* 210 */
```

This eliminates the need to define every possible z-index up front. The gaps accommodate edge cases without conflicting with the next semantic layer.

### Z-Index Documentation Convention

Every z-index in a codebase should reference a named token, never a raw number:

```css
/* BAD — raw z-index values create confusion */
.modal { z-index: 1000; }
.overlay { z-index: 999; }
.header { z-index: 50; }

/* GOOD — semantic tokens are self-documenting */
.modal { z-index: var(--z-modal); }
.overlay { z-index: var(--z-modal-backdrop); }
.header { z-index: var(--z-sticky); }
```

---

## Stacking Context Management

### What Creates a New Stacking Context

A stacking context is a three-dimensional conceptualization of HTML elements along the z-axis. When a new stacking context is created, all z-index values inside it are scoped to that context. This is the source of most z-index bugs.

**Properties that create new stacking contexts:**

| Property | Condition | Common Gotcha |
|----------|-----------|---------------|
| `position` + `z-index` | `position: relative/absolute/fixed/sticky` with any z-index value (including 0) | Adding z-index: 0 to "fix" something creates a new context |
| `opacity` | Any value less than 1 | `opacity: 0.99` creates a context — fading elements trap z-index |
| `transform` | Any value other than `none` | `transform: translateX(0)` creates a context |
| `filter` | Any value other than `none` | Even `filter: blur(0px)` counts |
| `backdrop-filter` | Any value other than `none` | Glassmorphism elements always create contexts |
| `perspective` | Any value other than `none` | 3D transform containers |
| `clip-path` | Any value other than `none` | Clipping creates a context |
| `mask` / `mask-image` | Any value | Masking creates a context |
| `mix-blend-mode` | Any value other than `normal` | Blend modes create contexts |
| `isolation` | `isolate` | Intentional context creation |
| `will-change` | When specifying `opacity`, `transform`, etc. | Performance hints create contexts |
| `contain` | `layout`, `paint`, or `strict` | CSS containment creates contexts |
| Flex/Grid children | When they have z-index set | Flex items with z-index create contexts |

### The Stacking Context Trap

The most common z-index bug occurs when an element needs to appear above something outside its stacking context:

```html
<!-- Problem: Tooltip inside a transformed parent -->
<div style="transform: translateX(0);"> <!-- Creates stacking context -->
  <div style="z-index: 9999;"> <!-- Trapped inside parent context -->
    This tooltip cannot escape its parent's stacking context,
    no matter how high the z-index.
  </div>
</div>

<div style="z-index: 1;"> <!-- This will still cover the tooltip -->
  I appear above the tooltip even though its z-index is 9999.
</div>
```

### Solutions to Stacking Context Problems

**1. Portals (React pattern):**
Render the floating element at the root of the DOM tree, outside any stacking contexts:
```jsx
// React portal — renders tooltip at document.body level
import { createPortal } from 'react-dom';

function Tooltip({ children, ...props }) {
  return createPortal(
    <div className="tooltip" {...props}>{children}</div>,
    document.body
  );
}
```

**2. CSS isolation property:**
Intentionally create stacking contexts where you want them, so you control the hierarchy:
```css
/* Create intentional stacking context barriers */
.layout-main {
  isolation: isolate; /* Everything inside is scoped */
}
.modal-layer {
  isolation: isolate; /* Modals get their own scope */
  z-index: var(--z-modal);
}
```

**3. Popover API (modern browsers):**
The HTML `popover` attribute renders elements in the top layer, above all stacking contexts:
```html
<button popovertarget="my-tooltip">Hover me</button>
<div id="my-tooltip" popover>
  This renders in the top layer — stacking contexts do not apply.
</div>
```

**4. The `<dialog>` element:**
Native `<dialog>` with `showModal()` renders in the top layer:
```javascript
const dialog = document.querySelector('dialog');
dialog.showModal(); // Renders above everything, ignores z-index
```

### Debugging Stacking Contexts

**Chrome DevTools approach:**
1. Open Elements panel
2. Select the problematic element
3. Look at the "Computed" tab for z-index
4. Walk up the DOM tree checking each ancestor for stacking context triggers
5. Use the "Layers" panel (3D view) to visualize the layer tree

**Mental model for debugging:**
1. Find the two elements that overlap incorrectly
2. Find the stacking context parent of each
3. Compare the z-index of those two stacking context parents
4. The fix is either: change the parent z-index, or move the element out of its context

---

## Surface Layer Architecture

### The Surface Hierarchy Model

Surfaces are the visual containers that hold content. Each surface sits at a specific elevation level, with corresponding visual treatment (shadow, color, blur) that communicates its position in the hierarchy.

```
LAYER 8: toast/snackbar      [z-800]  — Ephemeral, auto-dismissing
LAYER 7: tooltip              [z-700]  — Informational, pointer-following
LAYER 6: popover              [z-600]  — Rich interactive floating content
LAYER 5: modal/dialog         [z-500]  — Focus-trapping overlay
LAYER 4: modal-backdrop       [z-400]  — Dimming layer behind modals
LAYER 3: fixed/sticky         [z-200-300] — Persistent navigation
LAYER 2: raised               [z-1]    — Cards, panels above base
LAYER 1: surface              [z-0]    — Primary content container
LAYER 0: base/background      [z-deep] — Page background
```

### Surface Colors by Elevation

Each elevation level should have a distinct surface color. In light mode the differences are subtle. In dark mode they are the primary mechanism for communicating hierarchy.

#### Light Mode Surface Colors

```css
:root {
  --surface-base:     #ffffff;     /* Page background */
  --surface-subtle:   #fafafa;     /* Slightly recessed areas, sidebars */
  --surface-default:  #ffffff;     /* Cards, content panels */
  --surface-raised:   #ffffff;     /* Elevated cards (shadow does the work) */
  --surface-overlay:  #ffffff;     /* Dropdowns, popovers */
  --surface-modal:    #ffffff;     /* Modals and dialogs */
  --surface-tooltip:  #1a1a1a;     /* Dark tooltip (inverted) */

  --backdrop-color: rgba(0, 0, 0, 0.4);  /* Modal backdrop */
}
```

In light mode, shadows handle most of the elevation communication. Surface colors can remain the same or use very subtle tints.

#### Dark Mode Surface Colors

```css
:root[data-theme="dark"] {
  --surface-base:     #0a0a0a;     /* Deepest background */
  --surface-subtle:   #111111;     /* Sidebar, secondary panels */
  --surface-default:  #171717;     /* Cards, content panels */
  --surface-raised:   #1e1e1e;     /* Elevated cards */
  --surface-overlay:  #262626;     /* Dropdowns, popovers */
  --surface-modal:    #2a2a2a;     /* Modals and dialogs */
  --surface-tooltip:  #f5f5f5;     /* Light tooltip (inverted) */

  --backdrop-color: rgba(0, 0, 0, 0.7);  /* Darker backdrop for dark mode */
}
```

In dark mode, each elevation step lightens the surface by approximately 3-5%. This progressive lightening is the primary depth cue.

#### Material 3 Tint-Based Surface Colors

```css
:root[data-theme="dark"] {
  --primary: #6750a4;
  --primary-rgb: 103, 80, 164;

  --surface-base:     #1c1b1f;
  --surface-1:        color-mix(in srgb, #1c1b1f, var(--primary) 5%);
  --surface-2:        color-mix(in srgb, #1c1b1f, var(--primary) 8%);
  --surface-3:        color-mix(in srgb, #1c1b1f, var(--primary) 11%);
  --surface-4:        color-mix(in srgb, #1c1b1f, var(--primary) 12%);
  --surface-5:        color-mix(in srgb, #1c1b1f, var(--primary) 14%);
}
```

This creates surfaces with a subtle primary color tint that increases with elevation, giving the dark mode a cohesive, branded feel.

---

## Elevation-to-Shadow Mapping

### Complete Mapping Table

The following table maps every common UI component to its elevation level, z-index token, surface color, shadow token, and border treatment:

| Component | Elevation | Z-Index | Surface | Shadow | Border |
|-----------|-----------|---------|---------|--------|--------|
| Page background | base | z-deep | surface-base | none | none |
| Sidebar | subtle | z-base | surface-subtle | none or xs | right border |
| Card (resting) | default | z-base | surface-default | sm | optional subtle |
| Card (hovered) | raised | z-raised | surface-raised | md-lg | none |
| Table header | raised | z-raised | surface-raised | none | bottom border |
| Sticky header | sticky | z-sticky | surface-default | sm | bottom border |
| Fixed nav | fixed | z-fixed | surface-default | sm | bottom border |
| Dropdown menu | overlay | z-dropdown | surface-overlay | lg | none |
| Select options | overlay | z-dropdown | surface-overlay | lg | none |
| Context menu | overlay | z-dropdown | surface-overlay | lg | none |
| Side drawer | overlay | z-drawer | surface-overlay | xl | none |
| Bottom sheet | overlay | z-drawer | surface-overlay | xl (top) | top border |
| Backdrop | backdrop | z-modal-backdrop | backdrop-color | none | none |
| Modal / Dialog | modal | z-modal | surface-modal | 2xl | none |
| Alert dialog | modal | z-modal | surface-modal | 2xl | none |
| Popover | popover | z-popover | surface-overlay | lg | none |
| Date picker | popover | z-popover | surface-overlay | lg | none |
| Color picker | popover | z-popover | surface-overlay | lg | none |
| Tooltip | tooltip | z-tooltip | surface-tooltip | md | none |
| Toast | toast | z-toast | surface-modal | lg | none |
| Snackbar | toast | z-toast | surface-modal | lg | none |
| Command palette | command | z-command-palette | surface-modal | 2xl | none |
| Notification banner | toast | z-toast | surface-modal | md | none |

---

## When to Use Elevation

### Elevation is Appropriate When

1. **Content temporarily overlaps other content.** Dropdowns, modals, tooltips — anything that appears over existing content needs elevation to communicate its temporary nature.

2. **An element follows the user.** Sticky headers, fixed navigation, floating action buttons — persistent elements that override scroll position should be elevated.

3. **Content is interactive and benefits from hover feedback.** Cards that link somewhere, draggable items, selectable elements — elevation change on interaction provides physical affordance.

4. **You need to create visual grouping.** A slightly raised card groups its contents together, separating them from the surrounding page.

5. **You need to establish reading order.** A modal should be read before the page behind it. Elevation ensures this by making the modal visually dominant.

### Elevation is NOT Appropriate When

1. **Content is inline and part of the normal flow.** Paragraphs, lists, form fields in a form — these do not need elevation.

2. **The interface is intentionally flat.** Flat design systems communicate hierarchy through spacing, color, and typography — not shadow.

3. **Every element is elevated.** If everything has a shadow, nothing stands out. Elevation loses meaning when overused.

4. **Performance is constrained.** On low-power devices or long lists, shadows add rendering cost. Use borders or background colors instead.

5. **Shadows would cause visual noise.** Compact, data-dense UIs with many small elements become chaotic with shadows on every item.

---

## Common Z-Index Bugs and Solutions

### Bug 1: Modal Behind Header

**Symptom:** Modal opens but appears behind the sticky header.

**Cause:** The header has `z-index: var(--z-sticky)` (200) and creates a stacking context. The modal is inside a parent with a lower stacking context.

**Fix:**
```css
/* Ensure modal is rendered at the top-level stacking context */
.modal-container {
  position: fixed;
  z-index: var(--z-modal); /* 500, above sticky at 200 */
}

/* Or use the dialog element with showModal() for top-layer rendering */
```

### Bug 2: Dropdown Cut Off by Overflow

**Symptom:** Dropdown menu appears but is clipped by a parent with `overflow: hidden`.

**Cause:** `overflow: hidden` clips all children, regardless of z-index.

**Fix:**
```css
/* Option 1: Remove overflow hidden from parent */
.parent { overflow: visible; }

/* Option 2: Use position: fixed for the dropdown */
.dropdown { position: fixed; }

/* Option 3: Portal the dropdown to document.body */

/* Option 4: Use the Popover API */
<div popover>Dropdown content</div>
```

### Bug 3: Tooltip Hidden Behind Sibling

**Symptom:** Tooltip on one card appears behind the adjacent card.

**Cause:** Cards have `position: relative` and create stacking contexts. Later DOM siblings stack above earlier ones.

**Fix:**
```css
/* Option 1: Raise the hovered card's stacking context */
.card:hover { z-index: var(--z-raised); }

/* Option 2: Portal tooltips to body */

/* Option 3: Use CSS isolation on the card container */
.card-grid { isolation: isolate; }
```

### Bug 4: Backdrop Not Covering Everything

**Symptom:** Modal backdrop does not cover the sticky header or toasts.

**Cause:** Backdrop z-index is lower than the header's.

**Fix:**
```css
/* Backdrop must be above fixed/sticky elements */
.backdrop {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal-backdrop); /* 400, above fixed at 300 */
}
.modal {
  z-index: var(--z-modal); /* 500, above backdrop at 400 */
}
```

### Bug 5: New Stacking Context from Animation

**Symptom:** After adding a CSS animation or transition, z-index behavior changes.

**Cause:** CSS transforms and animations create new stacking contexts.

**Fix:**
```css
/* Be aware that will-change creates a stacking context */
.animated-element {
  will-change: transform; /* This creates a new stacking context */
  z-index: var(--z-raised); /* Must now account for the new context */
}

/* Remove will-change when animation completes */
.animated-element.animation-done {
  will-change: auto;
}
```

---

## CSS `isolation` Property

The `isolation` property creates a new stacking context without any visual side effects. It is the cleanest way to intentionally scope z-index.

```css
/* Create explicit stacking context boundaries */
.page-layout {
  isolation: isolate;
}

.modal-layer {
  isolation: isolate;
  position: fixed;
  z-index: var(--z-modal);
}

.toast-layer {
  isolation: isolate;
  position: fixed;
  z-index: var(--z-toast);
}
```

### Isolation Architecture Pattern

Structure your application into explicit isolation layers:

```html
<body>
  <!-- Base layer: all page content, isolated -->
  <div class="layer-base" style="isolation: isolate;">
    <header class="sticky-header">...</header>
    <main>
      <!-- All page content here. Z-indexes inside are scoped -->
    </main>
  </div>

  <!-- Drawer layer -->
  <div class="layer-drawer" style="isolation: isolate; z-index: 350;">
    <!-- Side drawers, off-canvas panels -->
  </div>

  <!-- Modal layer -->
  <div class="layer-modal" style="isolation: isolate; z-index: 500;">
    <!-- Modals and dialogs render here via portals -->
  </div>

  <!-- Notification layer -->
  <div class="layer-toast" style="isolation: isolate; z-index: 800;">
    <!-- Toasts and notifications render here -->
  </div>
</body>
```

This architecture guarantees that no element inside the base layer can ever overlap elements in the modal or toast layers, regardless of any z-index values used within those layers.

---

## The Top Layer (HTML spec)

Modern browsers have a concept called the "top layer" — a special rendering layer that exists above all stacking contexts in the document. Elements promoted to the top layer cannot be overlapped by any z-index value in the regular document.

### Elements that use the Top Layer

1. **`<dialog>` with `showModal()`:**
```html
<dialog id="my-dialog">
  <p>I am in the top layer. Nothing can cover me.</p>
  <button onclick="this.closest('dialog').close()">Close</button>
</dialog>
<script>
  document.getElementById('my-dialog').showModal();
</script>
```

2. **Popover API:**
```html
<button popovertarget="menu">Open Menu</button>
<div id="menu" popover>
  <p>I am in the top layer when open.</p>
</div>
```

3. **Fullscreen API:**
```javascript
document.querySelector('video').requestFullscreen();
// The video element moves to the top layer
```

### Top Layer Advantages
- No z-index management needed
- Immune to parent stacking contexts
- Immune to parent overflow clipping
- Immune to parent opacity/transform/filter stacking context creation
- Built-in `::backdrop` pseudo-element for dimming
- Proper focus trapping (for `showModal()`)
- Accessibility baked in (dialog has ARIA role automatically)

### Top Layer Limitations
- Cannot stack top-layer elements against each other with CSS (they stack in show-order)
- Not all components can use it (only dialog, popover, fullscreen)
- Limited browser support for Popover API in older browsers

---

## Elevation in Component Libraries

### React Component Elevation Pattern

```tsx
// Elevation wrapper component
type ElevationLevel = 0 | 1 | 2 | 3 | 4 | 5;

interface SurfaceProps {
  elevation?: ElevationLevel;
  children: React.ReactNode;
  className?: string;
  as?: React.ElementType;
}

const elevationStyles: Record<ElevationLevel, string> = {
  0: '',
  1: 'shadow-sm bg-surface-default',
  2: 'shadow-md bg-surface-raised',
  3: 'shadow-lg bg-surface-overlay',
  4: 'shadow-xl bg-surface-modal',
  5: 'shadow-2xl bg-surface-modal',
};

function Surface({ elevation = 0, children, className, as: Tag = 'div' }: SurfaceProps) {
  return (
    <Tag className={`${elevationStyles[elevation]} ${className ?? ''}`}>
      {children}
    </Tag>
  );
}

// Usage
<Surface elevation={1} className="rounded-lg p-4">Card content</Surface>
<Surface elevation={4} className="rounded-xl p-6">Modal content</Surface>
```

### CSS Utility Classes for Elevation

```css
/* Elevation utility classes */
.elevation-0 {
  box-shadow: none;
  background-color: var(--surface-base);
}
.elevation-1 {
  box-shadow: var(--shadow-sm);
  background-color: var(--surface-default);
}
.elevation-2 {
  box-shadow: var(--shadow-md);
  background-color: var(--surface-raised);
}
.elevation-3 {
  box-shadow: var(--shadow-lg);
  background-color: var(--surface-overlay);
}
.elevation-4 {
  box-shadow: var(--shadow-xl);
  background-color: var(--surface-modal);
}
.elevation-5 {
  box-shadow: var(--shadow-2xl);
  background-color: var(--surface-modal);
}

/* Interactive elevation transitions */
.elevation-interactive {
  transition: box-shadow 0.2s ease, transform 0.2s ease, background-color 0.2s ease;
}
.elevation-interactive:hover {
  box-shadow: var(--shadow-lg);
  background-color: var(--surface-raised);
  transform: translateY(-1px);
}
.elevation-interactive:active {
  box-shadow: var(--shadow-sm);
  transform: translateY(0);
}
```

---

## Elevation Audit Checklist

Use this checklist when reviewing an interface's elevation system:

- [ ] Every z-index in the codebase references a semantic token, not a raw number
- [ ] Z-index scale has documented gaps between levels for sub-layering
- [ ] No z-index values above 999 (indicates a z-index war)
- [ ] Stacking contexts are intentionally created with `isolation: isolate`
- [ ] Modals/dialogs use the top layer (`showModal()` or popover API) where possible
- [ ] Floating elements (tooltips, dropdowns) are portaled to escape stacking contexts
- [ ] Backdrop overlay z-index is between fixed elements and modals
- [ ] Dark mode uses surface color stepping, not just shadow darkening
- [ ] Shadow intensity matches the elevation level (higher = larger shadow)
- [ ] No elements have shadows that contradict their z-position
- [ ] Elevation transitions are performant (opacity/transform, not box-shadow animation)
- [ ] Focus rings appear above all content at the current elevation
- [ ] Overflow hidden does not clip any floating elements
- [ ] Toast/notification layer is above modals so they remain visible during dialogs
