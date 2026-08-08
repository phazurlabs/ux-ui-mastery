# Icon Implementation Recipes

Getting icons into a codebase: the React component, inline vs sprite vs font,
state transitions, animated icons, and SVG optimization.

## 6. Icon Component Implementation

### React SVG Icon Component
A production-ready icon component wraps raw SVGs with consistent props:

```tsx
import { forwardRef, SVGProps } from 'react';

interface IconProps extends SVGProps<SVGSVGElement> {
  size?: number | string;
  color?: string;
  title?: string;
  'aria-label'?: string;
}

const Icon = forwardRef<SVGSVGElement, IconProps>(
  ({ size = 24, color = 'currentColor', title, children, ...props }, ref) => {
    const isDecorative = !title && !props['aria-label'];
    return (
      <svg
        ref={ref}
        xmlns="http://www.w3.org/2000/svg"
        width={size}
        height={size}
        viewBox="0 0 24 24"
        fill="none"
        stroke={color}
        strokeWidth={2}
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden={isDecorative ? true : undefined}
        role={isDecorative ? undefined : 'img'}
        {...props}
      >
        {title && <title>{title}</title>}
        {children}
      </svg>
    );
  }
);
```

### Inline SVG vs Icon Fonts vs Sprite Sheets

| Method | Bundle Size | Styling | Accessibility | Rendering | Recommendation |
|--------|-------------|---------|---------------|-----------|----------------|
| **Inline SVG** | Small (tree-shaking) | Full CSS control | Best (aria, title) | Crisp at all sizes | Recommended |
| **SVG sprite sheet** | Single HTTP request | Limited (use/fill) | Good | Crisp | Good for large sets |
| **Icon font** | Medium (full set) | color/font-size only | Poor (pseudo-elements) | Can blur at odd sizes | Avoid for new projects |
| **img tag SVG** | Per-request or cached | No CSS control | alt text only | Crisp | External/user-uploaded only |

### SVG Sprite Sheet Implementation
```html
<!-- sprites.svg (hidden) -->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol id="icon-search" viewBox="0 0 24 24">
    <circle cx="11" cy="11" r="8" fill="none" stroke="currentColor" stroke-width="2"/>
    <line x1="21" y1="21" x2="16.65" y2="16.65" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  </symbol>
</svg>

<!-- Usage -->
<svg class="icon" width="24" height="24" aria-hidden="true">
  <use href="#icon-search" />
</svg>
```

---

## 7. Icon States

| State | Opacity | Color Token | Transform | Cursor | Additional |
|-------|---------|-------------|-----------|--------|------------|
| **Default** | 100% | `--icon-default` (gray-600) | none | default | — |
| **Hover** | 100% | `--icon-hover` (gray-900) | none | pointer | transition: color 150ms ease |
| **Active / Pressed** | 100% | `--icon-active` (primary-600) | scale(0.95) | pointer | transition: transform 100ms ease |
| **Disabled** | 38% | `--icon-disabled` (gray-400) | none | not-allowed | pointer-events: none |
| **Selected / On** | 100% | `--icon-selected` (primary-600) | none | pointer | Switch to filled variant if available |
| **Focus-visible** | 100% | `--icon-focus` (gray-900) | none | pointer | 2px focus ring offset 2px |
| **Drag** | 80% | `--icon-default` | scale(1.05) | grabbing | drop-shadow for lift effect |

### State Transition CSS
```css
.icon-button {
  color: var(--icon-default);
  transition: color 150ms ease, transform 100ms ease, opacity 150ms ease;
}
.icon-button:hover { color: var(--icon-hover); }
.icon-button:active { color: var(--icon-active); transform: scale(0.95); }
.icon-button:disabled { color: var(--icon-disabled); opacity: 0.38; pointer-events: none; }
.icon-button[aria-selected="true"] { color: var(--icon-selected); }
.icon-button:focus-visible { outline: 2px solid var(--focus-ring); outline-offset: 2px; }
```

---

## 8. Animated Icons

### Loading Spinner
```css
@keyframes spin { to { transform: rotate(360deg); } }
.icon-spinner { animation: spin 1s linear infinite; transform-origin: center; }
/* Accessible: pair with aria-live region announcing "Loading" */
```

### Toggle Transitions (Bookmark, Favorite)
```css
@keyframes pop {
  0% { transform: scale(1); }
  50% { transform: scale(1.3); }
  100% { transform: scale(1); }
}
.icon-toggle--active { animation: pop 300ms cubic-bezier(0.175, 0.885, 0.32, 1.275); }
```

### Success / Error State Icons
```css
/* Checkmark draw-on */
@keyframes draw-check {
  from { stroke-dashoffset: 24; }
  to { stroke-dashoffset: 0; }
}
.icon-success path {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
  animation: draw-check 400ms ease-out 200ms forwards;
}

/* Error shake */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-4px); }
  75% { transform: translateX(4px); }
}
.icon-error { animation: shake 400ms ease-in-out; color: var(--color-error); }
```

### Hamburger-to-Close Morph
```css
.hamburger-line {
  transition: transform 300ms ease, opacity 200ms ease;
  transform-origin: center;
}
/* Open state */
.menu-open .hamburger-line:nth-child(1) { transform: rotate(45deg) translateY(6px); }
.menu-open .hamburger-line:nth-child(2) { opacity: 0; }
.menu-open .hamburger-line:nth-child(3) { transform: rotate(-45deg) translateY(-6px); }
```

### Animation Guidelines
- Keep icon animations under 400ms — they should feel instant, not theatrical
- Use `prefers-reduced-motion: reduce` to disable all icon animations for accessibility
- Loading spinners are exempt from reduced-motion (but should slow to a gentle pulse)
- Never animate icons on page load — only on user interaction or state change

---

## 12. SVG Optimization

### SVGO Configuration
SVGO (SVG Optimizer) is the industry standard tool. Recommended configuration:

```js
// svgo.config.js
module.exports = {
  multipass: true,
  plugins: [
    'preset-default',
    'removeDimensions',        // Use viewBox instead of width/height
    'removeXMLNS',             // Remove xmlns when inlining
    { name: 'removeAttrs', params: { attrs: ['data-name', 'class'] } },
    { name: 'addAttributesToSVGElement', params: { attributes: [{ 'aria-hidden': 'true' }] } },
    { name: 'removeViewBox', active: false },  // KEEP viewBox
    { name: 'cleanupIds', params: { minify: true } },
    'convertPathData',         // Optimize path data
    'mergePaths',              // Merge adjacent paths
    'removeEmptyContainers',
    'removeUselessStrokeAndFill',
    'collapseGroups',
  ],
};
```

### Optimization Checklist
- Remove editor metadata (Illustrator, Sketch, Figma layer names)
- Remove hidden layers and unused definitions (defs, clipPaths not referenced)
- Simplify paths: reduce decimal precision to 1-2 places
- Merge paths that share the same fill/stroke attributes
- Convert shapes (rect, circle, ellipse) to path only when it reduces file size
- Remove unnecessary transforms — flatten to direct coordinates
- Remove default attribute values (fill="black" when black is default)
- Minify: remove whitespace, newlines, comments

### Size Targets
| Icon Complexity | Raw SVG | Optimized | Target |
|-----------------|---------|-----------|--------|
| Simple (arrow, X) | 400-600B | 150-250B | < 300B |
| Medium (gear, person) | 800-1200B | 300-500B | < 600B |
| Complex (illustration) | 2-10KB | 1-4KB | < 5KB |

---
