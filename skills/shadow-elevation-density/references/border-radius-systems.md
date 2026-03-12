# Border-Radius Systems — 5 Complete Radius Systems with Tokens & Conventions

## Border-Radius Philosophy

Border-radius is one of the strongest subconscious signals of brand personality in UI design. It is perceived before typography, before color, before layout. Sharp corners communicate precision and authority. Rounded corners communicate warmth and approachability. This single property shapes how users feel about an entire product within milliseconds.

The radius system must be:
- **Consistent:** All components in a family share a coordinated radius logic
- **Scalable:** Larger components use proportionally larger radii
- **Nested-aware:** Inner elements account for padding when nested inside rounded parents
- **Platform-conscious:** iOS, Android, and web each have default radius conventions

---

## The Radius Scale

A universal scale that all five systems below are built upon:

| Token | Value | Usage |
|-------|-------|-------|
| `none` | 0px | Sharp corners, dividers, full-bleed elements |
| `xs` | 2px | Subtle softening, inline badges, code blocks |
| `sm` | 4px | Small interactive elements, chips, tags |
| `md` | 8px | Standard components: buttons, inputs, cards |
| `lg` | 12px | Prominent cards, dropdown menus, panels |
| `xl` | 16px | Large panels, featured cards, sheets |
| `2xl` | 24px | Hero cards, modals, large containers |
| `3xl` | 32px | Extra-large containers, sections |
| `full` | 9999px | Pills, circles, fully rounded elements |

---

## The Nested Radius Rule (Critical)

When a rounded element contains another rounded element with padding between them, the inner element must use a smaller radius to maintain visual consistency:

```
inner-radius = max(0, outer-radius - padding)
```

### Visual demonstration:

```
WRONG (same radius, uneven gap):
╭────────────────────────╮
│  ╭──────────────────╮  │
│  │   Inner content   │  │
│  ╰──────────────────╯  │
╰────────────────────────╯
  ^ Gap is thicker at corners

CORRECT (reduced inner radius):
╭────────────────────────╮
│  ╭──────────────────╮  │
│  │   Inner content   │  │
│  ╰──────────────────╯  │
╰────────────────────────╯
  ^ Gap is visually uniform
```

### CSS Implementation:

```css
.card {
  --card-radius: 16px;
  --card-padding: 8px;
  border-radius: var(--card-radius);
  padding: var(--card-padding);
}

.card-inner {
  /* Nested radius rule */
  border-radius: calc(var(--card-radius) - var(--card-padding));
  /* Result: 16px - 8px = 8px */
}

/* If padding exceeds the outer radius, inner radius is 0 */
.card-inner-flat {
  border-radius: max(0px, calc(var(--card-radius) - var(--card-padding)));
}
```

### Common nested scenarios:

| Outer Radius | Padding | Inner Radius |
|-------------|---------|-------------|
| 16px | 4px | 12px |
| 16px | 8px | 8px |
| 16px | 12px | 4px |
| 16px | 16px+ | 0px |
| 12px | 4px | 8px |
| 12px | 8px | 4px |
| 8px | 4px | 4px |
| 8px | 8px+ | 0px |
| 24px | 8px | 16px |
| 24px | 12px | 12px |

---

## Component Radius Conventions

### Universal component-to-radius mapping

| Component | Typical Radius | Notes |
|-----------|---------------|-------|
| Button (standard) | md (8px) | Match the system personality |
| Button (pill) | full (9999px) | For CTAs, tags, pill-style |
| Button (icon only) | full or md | Circles for FABs, rounded-square for toolbars |
| Input / Text field | md (8px) | Must match button radius for visual alignment |
| Select / Dropdown trigger | md (8px) | Same as input |
| Dropdown menu | lg (12px) | Slightly larger than trigger |
| Card | lg (12px) | Prominent but not playful |
| Modal / Dialog | xl-2xl (16-24px) | Large, prominent, floating |
| Toast / Snackbar | md-lg (8-12px) | Visible but not dominant |
| Tooltip | sm-md (4-8px) | Small and utilitarian |
| Badge / Tag | sm-full (4px-9999px) | Depends on pill vs. rectangular style |
| Avatar | full (9999px) | Always circular (or squircle on iOS) |
| Chip | full (9999px) | Pill-shaped by convention |
| Switch / Toggle track | full (9999px) | Always pill-shaped |
| Checkbox | xs-sm (2-4px) | Slightly rounded square |
| Tab | md-lg (8-12px) top only | Rounded top, flat bottom |
| Sidebar | none (0px) | Full-height panels are not rounded |
| Image thumbnail | sm-md (4-8px) | Subtle softening |
| Code block | md (8px) | Distinct from regular content |
| Alert / Banner | md (8px) | Functional, not decorative |
| Progress bar | full (9999px) | Rounded ends by convention |
| Skeleton placeholder | matches target | Must match the component it replaces |

---

## System 1: Sharp (Corporate / Technical)

**Personality:** Precise, authoritative, professional, no-nonsense. Communicates technical competence and institutional trust.

**Used by:** Bloomberg, Reuters, enterprise admin panels, code editors, terminal UIs, legal/finance software.

### Token Scale

```css
:root {
  --radius-none: 0px;
  --radius-xs: 1px;
  --radius-sm: 2px;
  --radius-md: 3px;
  --radius-lg: 4px;
  --radius-xl: 6px;
  --radius-2xl: 8px;
  --radius-3xl: 8px;
  --radius-full: 9999px;
}
```

### Design Tokens (JSON)

```json
{
  "radius": {
    "sharp": {
      "none": { "value": "0px" },
      "xs":   { "value": "1px" },
      "sm":   { "value": "2px" },
      "md":   { "value": "3px" },
      "lg":   { "value": "4px" },
      "xl":   { "value": "6px" },
      "2xl":  { "value": "8px" },
      "3xl":  { "value": "8px" },
      "full": { "value": "9999px" }
    }
  }
}
```

### Component Mapping

| Component | Token | Value |
|-----------|-------|-------|
| Button | sm | 2px |
| Input | sm | 2px |
| Card | md | 3px |
| Dropdown | md | 3px |
| Modal | lg | 4px |
| Toast | md | 3px |
| Tooltip | sm | 2px |
| Badge | xs | 1px |
| Avatar | full | circle |
| Tab | sm (top) | 2px |
| Checkbox | xs | 1px |
| Code block | sm | 2px |

### Characteristics
- Maximum radius caps at 8px even for the largest elements
- Most elements use 2-3px radius
- Borders are more important than shadows for separation
- Often paired with monospace or technical sans-serif typography
- Flat color fills with sharp edges dominate the visual language

---

## System 2: Balanced (Modern Web Standard)

**Personality:** Professional yet approachable. Modern without being trendy. Trustworthy without being cold.

**Used by:** Notion, Linear, Stripe, GitHub, Vercel, most modern SaaS products.

### Token Scale

```css
:root {
  --radius-none: 0px;
  --radius-xs: 2px;
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-2xl: 16px;
  --radius-3xl: 20px;
  --radius-full: 9999px;
}
```

### Design Tokens (JSON)

```json
{
  "radius": {
    "balanced": {
      "none": { "value": "0px" },
      "xs":   { "value": "2px" },
      "sm":   { "value": "4px" },
      "md":   { "value": "6px" },
      "lg":   { "value": "8px" },
      "xl":   { "value": "12px" },
      "2xl":  { "value": "16px" },
      "3xl":  { "value": "20px" },
      "full": { "value": "9999px" }
    }
  }
}
```

### Component Mapping

| Component | Token | Value |
|-----------|-------|-------|
| Button | md | 6px |
| Input | md | 6px |
| Card | lg | 8px |
| Dropdown | lg | 8px |
| Modal | xl-2xl | 12-16px |
| Toast | lg | 8px |
| Tooltip | md | 6px |
| Badge / Tag | sm-full | 4px or pill |
| Avatar | full | circle |
| Tab | md (top) | 6px |
| Checkbox | sm | 4px |
| Code block | md | 6px |
| Popover | lg | 8px |
| Bottom sheet | xl (top) | 12px |

### Characteristics
- Sweet spot between sharp and soft
- md (6px) is the workhorse radius for most interactive elements
- lg (8px) for container elements
- Consistent use of 6-8px throughout creates calm, clean feel
- The most "neutral" and versatile system — works for almost any product category

---

## System 3: Soft (Friendly / Consumer)

**Personality:** Warm, friendly, inviting, approachable. Communicates care, safety, and human-centeredness.

**Used by:** Airbnb, Slack, Spotify, Instagram, Figma, most consumer-facing apps.

### Token Scale

```css
:root {
  --radius-none: 0px;
  --radius-xs: 4px;
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-2xl: 20px;
  --radius-3xl: 28px;
  --radius-full: 9999px;
}
```

### Design Tokens (JSON)

```json
{
  "radius": {
    "soft": {
      "none": { "value": "0px" },
      "xs":   { "value": "4px" },
      "sm":   { "value": "6px" },
      "md":   { "value": "8px" },
      "lg":   { "value": "12px" },
      "xl":   { "value": "16px" },
      "2xl":  { "value": "20px" },
      "3xl":  { "value": "28px" },
      "full": { "value": "9999px" }
    }
  }
}
```

### Component Mapping

| Component | Token | Value |
|-----------|-------|-------|
| Button | lg | 12px |
| Input | lg | 12px |
| Card | xl | 16px |
| Dropdown | xl | 16px |
| Modal | 2xl-3xl | 20-28px |
| Toast | xl | 16px |
| Tooltip | md | 8px |
| Badge / Tag | full | pill |
| Avatar | full | circle |
| Chip | full | pill |
| Tab | lg (top) | 12px |
| Checkbox | sm | 6px |
| Code block | lg | 12px |
| Image card | xl | 16px |

### Characteristics
- Noticeably rounded — corners are a design feature, not just a softening
- 12-16px is the dominant range
- Pill shapes (full radius) used liberally for badges, chips, tags
- Creates the "bubbly" feel associated with consumer apps
- Works well with soft shadows and pastel color palettes

---

## System 4: Rounded (Highly Rounded / Playful)

**Personality:** Playful, friendly, casual, youthful. Communicates fun, creativity, and approachability. Borders on "cute" territory.

**Used by:** Duolingo, kids' apps, wellness apps, social platforms, creative tools, casual games.

### Token Scale

```css
:root {
  --radius-none: 0px;
  --radius-xs: 6px;
  --radius-sm: 10px;
  --radius-md: 14px;
  --radius-lg: 18px;
  --radius-xl: 24px;
  --radius-2xl: 32px;
  --radius-3xl: 40px;
  --radius-full: 9999px;
}
```

### Design Tokens (JSON)

```json
{
  "radius": {
    "rounded": {
      "none": { "value": "0px" },
      "xs":   { "value": "6px" },
      "sm":   { "value": "10px" },
      "md":   { "value": "14px" },
      "lg":   { "value": "18px" },
      "xl":   { "value": "24px" },
      "2xl":  { "value": "32px" },
      "3xl":  { "value": "40px" },
      "full": { "value": "9999px" }
    }
  }
}
```

### Component Mapping

| Component | Token | Value |
|-----------|-------|-------|
| Button | xl | 24px (or full for pill) |
| Input | lg | 18px |
| Card | 2xl | 32px |
| Dropdown | xl | 24px |
| Modal | 3xl | 40px |
| Toast | xl | 24px |
| Tooltip | md | 14px |
| Badge | full | pill |
| Avatar | full | circle |
| Chip | full | pill |
| Checkbox | sm | 10px |
| Image card | xl | 24px |
| Progress bar | full | fully rounded |

### Characteristics
- Even the smallest elements have visible rounding
- Cards at 32px and modals at 40px are unmistakably playful
- Almost everything that can be pill-shaped is pill-shaped
- Requires careful nested radius management (large outer radii amplify nesting issues)
- Best paired with bold colors, playful illustrations, and rounded typography

---

## System 5: Pill-Centric (Bold / Modern)

**Personality:** Bold, confident, modern, distinctive. Makes a strong visual statement. Every interactive element is fully rounded.

**Used by:** Some banking apps (Revolut), modern fintech, design-forward SaaS, crypto platforms.

### Token Scale

```css
:root {
  --radius-none: 0px;
  --radius-xs: 4px;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 9999px;  /* Everything lg and up is fully rounded */
  --radius-xl: 9999px;
  --radius-2xl: 9999px;
  --radius-3xl: 9999px;
  --radius-full: 9999px;
}
```

### Design Tokens (JSON)

```json
{
  "radius": {
    "pill": {
      "none": { "value": "0px" },
      "xs":   { "value": "4px" },
      "sm":   { "value": "8px" },
      "md":   { "value": "12px" },
      "lg":   { "value": "9999px" },
      "xl":   { "value": "9999px" },
      "2xl":  { "value": "9999px" },
      "3xl":  { "value": "9999px" },
      "full": { "value": "9999px" }
    }
  }
}
```

### Component Mapping

| Component | Token | Value |
|-----------|-------|-------|
| Button | full | pill |
| Input | full | pill |
| Card | md | 12px (cards are not pills) |
| Dropdown | md | 12px |
| Modal | md | 12px |
| Search bar | full | pill |
| Tab bar | full | pill track + pill indicator |
| Tag / Chip | full | pill |
| Badge | full | pill |
| Avatar | full | circle |
| Toggle | full | pill |
| Segmented control | full | pill track + pill segments |
| Code block | sm | 8px |

### Characteristics
- Strong distinction: interactive elements are pills, containers are moderately rounded
- Creates a clear interactive affordance — if it's a pill, you can tap it
- Requires careful height/width balance (pills look bad when too tall or too narrow)
- Best when combined with a limited color palette and bold typography
- The pill search bar is the signature element of this system

---

## Platform Radius Conventions

### iOS / Apple (Continuous Corners)

Apple uses "continuous corners" (superellipse/squircle) rather than standard circular arcs. The mathematical formula produces smoother transitions between straight edges and curves.

**iOS default radii:**

| Element | Radius |
|---------|--------|
| App icon | 60/4 = ~13.3pt (superellipse) |
| Card | 10-16pt |
| Sheet | 10pt (top corners) |
| Alert | 14pt |
| Button (filled) | typically height/2 for pill |
| Text field | 10pt |
| Toggle | height/2 (pill) |

**SwiftUI continuous corners:**
```swift
RoundedRectangle(cornerRadius: 16, style: .continuous) // Squircle
RoundedRectangle(cornerRadius: 16, style: .circular)   // Standard
```

**CSS approximation of continuous corners:**
```css
/* No native CSS support for continuous corners */
/* Approximation using SVG clip-path */
.ios-rounded {
  clip-path: url(#squircle);
  /* or use a sufficiently large border-radius which approximates it on small sizes */
  border-radius: 16px;
}
```

### Android / Material Design (Shape Scale)

Material 3 defines a shape scale with specific corner treatments:

| Shape | Corner Size | Usage |
|-------|------------|-------|
| None | 0dp | n/a |
| Extra Small | 4dp | Small components |
| Small | 8dp | Standard components |
| Medium | 12dp | Cards, dialogs |
| Large | 16dp | Large sheets |
| Extra Large | 28dp | FAB, large containers |
| Full | 50% | Circles, pills |

Material also supports different corner types:
- **Rounded:** Standard circular arc (default)
- **Cut:** Diagonal cut corner
- **Asymmetric:** Different radii per corner

### Web Defaults

Browsers render `border-radius: 0` by default. There is no OS-level convention for the web, which is why establishing a design system radius is essential.

**Common web framework defaults:**
- Tailwind: 0.25rem (4px) for `rounded`, 0.5rem (8px) for `rounded-lg`
- Bootstrap: 0.375rem (6px) for `border-radius`
- Chakra UI: 0.375rem (6px) default
- Ant Design: 6px default
- shadcn/ui: 0.5rem (8px) via `--radius` variable

---

## Squircle (Superellipse) Implementation

### What is a Squircle?

A standard CSS `border-radius` creates a circular arc. The transition between the straight edge and the curve is abrupt at a mathematical level, creating a subtle "pinch" point. A squircle (superellipse) uses a different mathematical formula that creates a smoother, more organic transition.

The difference is subtle but perceivable, especially at larger radii (16px+). Apple's entire design language is built on continuous corner curves.

### CSS + SVG Squircle

```html
<svg width="0" height="0">
  <defs>
    <clipPath id="squircle-16" clipPathUnits="objectBoundingBox">
      <path d="M 0.5,0 C 0.832,0 1,0.168 1,0.5 C 1,0.832 0.832,1 0.5,1 C 0.168,1 0,0.832 0,0.5 C 0,0.168 0.168,0 0.5,0 Z" />
    </clipPath>
  </defs>
</svg>

<style>
.squircle {
  clip-path: url(#squircle-16);
  /* Fallback for browsers that don't support SVG clip-path */
  border-radius: 16px;
}
</style>
```

### JavaScript Squircle Path Generator

```javascript
/**
 * Generate a squircle (superellipse) SVG path
 * @param {number} width - Element width
 * @param {number} height - Element height
 * @param {number} radius - Corner radius
 * @param {number} smoothing - Smoothing factor (0 = circle, 1 = max squircle)
 * @returns {string} SVG path data
 */
function generateSquirclePath(width, height, radius, smoothing = 0.6) {
  const r = Math.min(radius, width / 2, height / 2);
  const s = r * smoothing;

  return `
    M ${r},0
    L ${width - r},0
    C ${width - s},0 ${width},${s} ${width},${r}
    L ${width},${height - r}
    C ${width},${height - s} ${width - s},${height} ${width - r},${height}
    L ${r},${height}
    C ${s},${height} 0,${height - s} 0,${height - r}
    L 0,${r}
    C 0,${s} ${s},0 ${r},0
    Z
  `.trim();
}
```

### React Squircle Component

```tsx
function Squircle({
  width,
  height,
  radius = 16,
  smoothing = 0.6,
  children,
  className,
  style,
}: {
  width: number;
  height: number;
  radius?: number;
  smoothing?: number;
  children: React.ReactNode;
  className?: string;
  style?: React.CSSProperties;
}) {
  const id = `squircle-${radius}-${smoothing}`;
  const path = generateSquirclePath(width, height, radius, smoothing);

  return (
    <>
      <svg width="0" height="0" style={{ position: 'absolute' }}>
        <defs>
          <clipPath id={id} clipPathUnits="objectBoundingBox">
            <path d={normalizePathToObjectBoundingBox(path, width, height)} />
          </clipPath>
        </defs>
      </svg>
      <div
        className={className}
        style={{
          width,
          height,
          clipPath: `url(#${id})`,
          ...style,
        }}
      >
        {children}
      </div>
    </>
  );
}
```

---

## Border-Radius and Overflow Clipping

### The Overflow Problem

`border-radius` clips content visually, but without `overflow: hidden`, child elements can escape the rounded corners:

```css
/* BROKEN: child image extends beyond rounded corners */
.card {
  border-radius: 16px;
  /* Child img bleeds past corners */
}

/* FIXED: overflow clips children to the rounded shape */
.card {
  border-radius: 16px;
  overflow: hidden;
}
```

**Caution:** `overflow: hidden` has side effects:
- Clips scrollbar if content overflows
- Can clip box-shadows (which render outside the element)
- Can clip absolutely-positioned children (dropdowns, tooltips)
- Creates a new stacking context

### Solutions for overflow + border-radius conflicts:

```css
/* Solution 1: Clip only the image, not the card */
.card {
  border-radius: 16px;
  /* Do NOT set overflow: hidden here */
}
.card-image {
  border-radius: 16px 16px 0 0; /* Match card top corners */
  overflow: hidden; /* Clip image only */
}

/* Solution 2: Use clip-path instead of overflow */
.card {
  clip-path: inset(0 round 16px);
  /* Clips to rounded rect without affecting overflow behavior */
}

/* Solution 3: Isolate the clipping to a wrapper */
.card {
  border-radius: 16px;
  position: relative;
}
.card-clip-layer {
  position: absolute;
  inset: 0;
  border-radius: inherit;
  overflow: hidden;
  pointer-events: none;
}
```

---

## Radius Tokens in Major Frameworks

### Tailwind CSS

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    borderRadius: {
      'none': '0px',
      'xs': '2px',
      'sm': '4px',
      DEFAULT: '6px',    // class="rounded"
      'md': '8px',
      'lg': '12px',
      'xl': '16px',
      '2xl': '24px',
      '3xl': '32px',
      'full': '9999px',
    },
  },
}
```

**Usage:**
```html
<button class="rounded-md">Balanced button</button>
<button class="rounded-full">Pill button</button>
<div class="rounded-lg">Card</div>
<dialog class="rounded-2xl">Modal</dialog>
```

### CSS Custom Properties

```css
:root {
  /* Choose one system and apply its values */
  --radius-none: 0px;
  --radius-xs: 2px;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-2xl: 24px;
  --radius-3xl: 32px;
  --radius-full: 9999px;

  /* Semantic aliases */
  --radius-button: var(--radius-md);
  --radius-input: var(--radius-md);
  --radius-card: var(--radius-lg);
  --radius-modal: var(--radius-2xl);
  --radius-tooltip: var(--radius-sm);
  --radius-dropdown: var(--radius-lg);
  --radius-badge: var(--radius-full);
  --radius-avatar: var(--radius-full);
}
```

### Style Dictionary Token Format

```json
{
  "radius": {
    "none": { "value": "0", "type": "borderRadius" },
    "xs":   { "value": "2", "type": "borderRadius" },
    "sm":   { "value": "4", "type": "borderRadius" },
    "md":   { "value": "8", "type": "borderRadius" },
    "lg":   { "value": "12", "type": "borderRadius" },
    "xl":   { "value": "16", "type": "borderRadius" },
    "2xl":  { "value": "24", "type": "borderRadius" },
    "3xl":  { "value": "32", "type": "borderRadius" },
    "full": { "value": "9999", "type": "borderRadius" }
  },
  "radius-semantic": {
    "button":   { "value": "{radius.md}", "type": "borderRadius" },
    "input":    { "value": "{radius.md}", "type": "borderRadius" },
    "card":     { "value": "{radius.lg}", "type": "borderRadius" },
    "modal":    { "value": "{radius.2xl}", "type": "borderRadius" },
    "tooltip":  { "value": "{radius.sm}", "type": "borderRadius" },
    "dropdown": { "value": "{radius.lg}", "type": "borderRadius" },
    "badge":    { "value": "{radius.full}", "type": "borderRadius" },
    "avatar":   { "value": "{radius.full}", "type": "borderRadius" }
  }
}
```

### Figma Variables

In Figma, create a radius variable collection:
- Mode: "Sharp", "Balanced", "Soft", "Rounded", "Pill"
- Each mode maps the same variable names to different values
- Components reference variables, and switching modes updates the entire file

---

## Responsive Radius

On very small screens, large border-radii can look disproportionate. Consider scaling radius with viewport:

```css
/* Scale radius down on small screens */
@media (max-width: 480px) {
  :root {
    --radius-lg: 8px;   /* Was 12px */
    --radius-xl: 12px;  /* Was 16px */
    --radius-2xl: 16px; /* Was 24px */
    --radius-3xl: 20px; /* Was 32px */
  }
}

/* Full-bleed cards on mobile should lose corner rounding */
@media (max-width: 640px) {
  .card-full-bleed {
    border-radius: 0;
    margin-left: -16px;
    margin-right: -16px;
  }
}
```

---

## Asymmetric Border-Radius

CSS allows different radii per corner. This is useful for:

### Tab-like elements (rounded top, flat bottom):
```css
.tab {
  border-radius: var(--radius-md) var(--radius-md) 0 0;
}
```

### Bottom sheet (rounded top, flat bottom):
```css
.bottom-sheet {
  border-radius: var(--radius-2xl) var(--radius-2xl) 0 0;
}
```

### Sidebar items (rounded right, flat left):
```css
.sidebar-item.active {
  border-radius: 0 var(--radius-md) var(--radius-md) 0;
}
```

### Chat bubbles (asymmetric corners):
```css
.chat-bubble-sent {
  border-radius: var(--radius-xl) var(--radius-xl) var(--radius-xs) var(--radius-xl);
}
.chat-bubble-received {
  border-radius: var(--radius-xl) var(--radius-xl) var(--radius-xl) var(--radius-xs);
}
```

### Notification grouped list (first/last rounding):
```css
.grouped-list-item {
  border-radius: 0;
}
.grouped-list-item:first-child {
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
}
.grouped-list-item:last-child {
  border-radius: 0 0 var(--radius-lg) var(--radius-lg);
}
.grouped-list-item:only-child {
  border-radius: var(--radius-lg);
}
```

---

## Advanced: 8-Value Border-Radius (Elliptical Corners)

CSS `border-radius` can take 8 values, creating elliptical (non-circular) corners:

```css
/* Syntax: horizontal-radii / vertical-radii */
.organic-shape {
  border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
}

/* Blob/organic shape for decorative elements */
.blob {
  border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
  animation: blob-morph 8s ease-in-out infinite;
}

@keyframes blob-morph {
  0%, 100% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; }
  25%      { border-radius: 50% 50% 30% 70% / 60% 40% 50% 50%; }
  50%      { border-radius: 60% 40% 50% 50% / 30% 70% 40% 60%; }
  75%      { border-radius: 30% 70% 60% 40% / 50% 50% 70% 30%; }
}
```

This is primarily for decorative/artistic elements, not UI components. UI components should use uniform circular corners.

---

## Border-Radius Audit Checklist

- [ ] A single radius system is chosen and documented for the project
- [ ] All components use token-based radius values, not hardcoded pixels
- [ ] Button and input radii match (they appear side-by-side in forms)
- [ ] Nested radius rule is applied wherever rounded elements contain rounded children
- [ ] Cards, modals, and dropdowns use proportionally larger radii than buttons
- [ ] Avatars and badges use `border-radius: 9999px` for circles/pills
- [ ] `overflow: hidden` is applied where needed to clip children to rounded corners
- [ ] Images inside rounded containers are properly clipped
- [ ] Radius values are reasonable on small screens (not comically large)
- [ ] Full-bleed mobile elements correctly use 0 radius
- [ ] Radius is consistent within component families (all buttons same, all cards same)
- [ ] Asymmetric radius (tabs, sheets, chat bubbles) is intentional and consistent
- [ ] Focus rings adapt to the border-radius of their target element
- [ ] Skeleton/placeholder shapes match the radius of the components they stand in for
- [ ] Platform conventions are considered (iOS squircle, Material shape scale)
