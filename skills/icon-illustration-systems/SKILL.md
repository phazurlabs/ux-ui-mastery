---
name: icon-illustration-systems
description: "Complete icon design systems, illustration style guides, and SVG implementation patterns. Covers icon grid systems, icon sizing, icon libraries (Lucide, Heroicons, Phosphor, SF Symbols, Material Symbols), illustration styles, SVG optimization, and accessible iconography. Use when the user mentions: icon, illustration, SVG, icon library, icon system, Lucide, Heroicons, Phosphor, SF Symbols, Material Icons, icon grid, icon size, icon design, illustration style, spot illustration, empty state illustration, svg optimization, icon accessibility, icon component."
---

# Icon & Illustration Systems

## 1. Icon Philosophy

### Icons Supplement Text
Icons are visual shorthand. They accelerate recognition but must never be the sole carrier of meaning for critical actions. The cardinal rule: icons supplement text, they do not replace it. Always pair icons with visible text labels for primary navigation, toolbar actions, and settings. Icons may stand alone only when they represent universally understood metaphors.

### Universal vs Learned Metaphors
Not all icons are equal in recognizability. Distinguish between two categories:

**Universal metaphors** (safe to use without labels):
- Magnifying glass = Search
- X / Cross = Close / Dismiss
- Left arrow / Chevron = Back / Navigate back
- House = Home
- Plus = Add / Create
- Trash can = Delete
- Gear / Cog = Settings (borderline — test with users)

**Learned metaphors** (require labels or onboarding):
- Hamburger menu (three lines) — widely known but still ambiguous to some demographics
- Heart = Like / Favorite (context-dependent: could mean health in medical apps)
- Bell = Notifications (learned convention, not innate)
- Share icon — varies across platforms (iOS share vs Android share vs web share)
- Bookmark / Flag — ambiguous without context
- Filter / Funnel — not universally recognized
- Cloud = Cloud storage / Upload (requires context)

**Rule of thumb**: If you need to debate whether an icon is self-explanatory, add a label.

### Consistency Principles
1. **Stylistic unity** — Every icon in a set must share the same stroke weight, corner radius, and visual density. Mixing outline and solid icons in the same context creates cognitive dissonance.
2. **Metaphor consistency** — If a trash can means "delete" in one part of the app, it must mean "delete" everywhere. Never reuse an icon glyph for a different action.
3. **Sizing consistency** — Icons at the same hierarchy level must be the same size. Do not mix 20px and 24px icons in the same toolbar.
4. **Color consistency** — Interactive icons use the same color token. Decorative icons use a muted variant. Selected/active icons use the accent color.
5. **Density consistency** — All icons should have similar visual weight. An icon that appears heavier or lighter than its neighbors disrupts scanning.

---

## 2. Icon Grid Systems

### The 24x24 Base Grid
The industry standard base grid is 24x24 pixels. All icon design begins here. The grid provides:
- **Live area**: 20x20px centered within the 24x24 frame (2px padding on each side)
- **Trim area**: The full 24x24 frame, ensuring consistent bounding boxes across the set
- **Pixel grid**: Every anchor point, stroke endpoint, and corner snaps to full or half pixels to prevent anti-aliasing blur at 1x resolution

### Pixel Grid Alignment
Icons rendered at small sizes (16-24px) must align to the pixel grid:
- Horizontal and vertical strokes land on full pixel boundaries
- 2px strokes span from pixel N to pixel N+2 (not N+0.5 to N+2.5)
- Diagonal lines and curves are exempt but should use even-number stroke widths
- At 1x resolution, a misaligned stroke renders as two blurry 1px lines instead of one crisp 2px line

### Keyline Shapes
Every icon fits within one of four keyline templates to ensure optical consistency:

| Keyline Shape | Dimensions (in 24px grid) | Use Cases |
|---------------|---------------------------|-----------|
| Circle | 20px diameter | People, globes, record, radio buttons |
| Square | 18x18px | Stops, settings, generic containers |
| Portrait rectangle | 16x20px (tall) | Documents, phones, bottles, person |
| Landscape rectangle | 20x16px (wide) | Laptops, landscapes, cards, video |
| Diagonal | 20x20px rotated 45deg | Warning, diamond, rotate |

### Safe Zones and Optical Sizing
- **2px safe zone** on all sides of the 24px frame — no visual content should enter this zone
- **Optical sizing**: A circle must be slightly larger than a square to appear the same size. A 20px circle appears smaller than an 18px square to the human eye. Compensate by allowing circular icons to extend 1px beyond the keyline
- **Vertical elements** (arrows pointing up) appear shorter than horizontal elements of the same pixel height — extend by 1-2px

---

## 3. Icon Sizing Scale

| Token | Size | Line Height | Use Cases | Touch Target |
|-------|------|-------------|-----------|--------------|
| `icon-xs` | 12px | 12px | Status dots, inline indicators, badge counts, color swatches | N/A (not interactive) |
| `icon-sm` | 16px | 16px | Inline with small text (12-13px), table row icons, tag icons, breadcrumb separators | 24x24px min |
| `icon-md` | 20px | 20px | Default size — nav items, buttons, form field icons, list item icons, dropdown arrows | 32x32px min |
| `icon-lg` | 24px | 24px | Prominent actions, card header icons, section markers, tab bar icons (mobile) | 44x44px min (mobile) |
| `icon-xl` | 32px | 32px | Feature icons, section headers, sidebar category icons, dialog icons | 44x44px min |
| `icon-2xl` | 40px | 40px | Hero feature icons, onboarding step icons, empty state accents | N/A (usually decorative) |
| `icon-3xl` | 48px | 48px | Large empty state illustrations, marketing feature blocks, landing page icons | N/A (usually decorative) |

### Sizing Rules
- Icons below 16px should use simplified glyphs (fewer details, thicker relative strokes)
- Icons at 12px may need to be redesigned as filled shapes rather than stroked outlines
- At 32px+, icons can support more detail (inner strokes, secondary elements)
- Never scale a 24px icon down to 12px by setting width/height — use a dedicated small variant
- Design at 24px, then create size-specific variants for 16px and 12px

---

## 4. Icon Design Rules

### Stroke Specifications
- **Stroke width**: 2px at 24px base size (scales proportionally: 1.5px at 16px, 1px at 12px)
- **Stroke caps**: Round (not butt or square) — creates softer, friendlier appearance
- **Stroke joins**: Round (not miter or bevel) — prevents sharp spikes at acute angles
- **Consistent weight**: Every stroke in every icon in the set must be the same width. No mixing 1.5px and 2px strokes within one icon
- **Terminal consistency**: Open endpoints should all use the same cap style. Do not mix round and flat terminals

### Optical Alignment
Mathematical centering often looks visually wrong. Apply optical corrections:
- **Play button triangle**: Shift 1-2px right from mathematical center (visual center of mass is left of geometric center)
- **Arrows**: The head of a right-pointing arrow should extend slightly beyond the mathematical right edge
- **Asymmetric icons**: Center based on visual weight, not bounding box
- **Icons in circles**: Enclosed icons need ~1px additional padding vs the keyline to avoid feeling cramped

### Metaphor Consistency
- Choose one metaphor per concept and use it everywhere (e.g., decide between a pencil or a pen for "edit" — then use it consistently)
- Avoid cultural bias: a mailbox icon varies by country; an envelope is more universal
- Test metaphors: run a quick icon recognition test with 5+ people before committing

### Geometry Rules
- Prefer geometric shapes over organic forms for UI icons
- Use consistent corner radii (typically 1-2px at 24px size)
- Minimize the number of anchor points — simpler paths render faster and scale better
- Avoid strokes thinner than 1px at any rendered size
- Counter spaces (holes in letters, gaps in shapes) should be at least 2px wide at rendered size

---

## 5. Icon Libraries Deep Dive

### Lucide (1,400+ icons)
**Style**: Clean outline, 24x24 grid, 2px stroke, round caps/joins
**Weights**: Single weight (outline only)
**License**: ISC (permissive, commercial OK)
**Best for**: General-purpose web apps, React/Next.js projects, replacing Feather Icons
**Pros**:
- Spiritual successor to Feather Icons with active maintenance
- Excellent React/Vue/Svelte/Angular packages with tree-shaking
- Consistent 2px stroke weight across entire set
- Community-driven with regular additions
- Small bundle size (~250 bytes per icon with tree-shaking)
**Cons**:
- Outline only — no filled variants for selected states
- Smaller set than Phosphor or Material
- Some niche categories (finance, medical) are sparse
**Import pattern (React)**:
```jsx
import { Search, ChevronRight, Settings } from 'lucide-react';
<Search size={20} strokeWidth={2} className="text-gray-600" />
```

### Heroicons (300+ icons)
**Style**: Clean outline and solid, 24x24 grid, 1.5px stroke
**Weights**: Three variants — Outline (24px), Solid (24px), Mini (20px)
**License**: MIT (permissive, commercial OK)
**Best for**: Tailwind CSS projects, applications needing both outline and solid variants
**Pros**:
- Designed by the Tailwind CSS team — seamless integration
- Three clear variants: outline for default, solid for active/selected, mini for compact UI
- High-quality curation — every icon is well-crafted
- Pairs naturally with Tailwind utility classes
**Cons**:
- Smallest set (~300 icons) — may need supplementing for complex apps
- Limited to three variants (no thin/light options)
- Slower addition of new icons compared to community-driven sets
**Import pattern (React)**:
```jsx
import { MagnifyingGlassIcon } from '@heroicons/react/24/outline';
import { MagnifyingGlassIcon as MagnifyingGlassSolid } from '@heroicons/react/24/solid';
import { MagnifyingGlassIcon as MagnifyingGlassMini } from '@heroicons/react/20/solid';
```

### Phosphor Icons (7,000+ icons)
**Style**: Clean geometric, 24x24 grid (256x256 design grid)
**Weights**: Six weights — Thin, Light, Regular, Bold, Fill, Duotone
**License**: MIT (permissive, commercial OK)
**Best for**: Projects requiring maximum icon variety and weight flexibility
**Pros**:
- Largest curated open-source set (7,000+ icons across 6 weights = 42,000+ variants)
- Six weights enable nuanced hierarchy without changing icon identity
- Duotone weight provides two-tone styling unique among free libraries
- Excellent React/Vue/Svelte/Flutter/Figma support
- Active maintenance with regular additions
**Cons**:
- Large set can cause decision paralysis
- Duotone rendering requires additional CSS for second color
- Some icons feel less refined than hand-curated smaller sets
**Import pattern (React)**:
```jsx
import { MagnifyingGlass, House, Gear } from '@phosphor-icons/react';
<MagnifyingGlass size={24} weight="regular" color="currentColor" />
<House size={24} weight="fill" />
<Gear size={24} weight="duotone" />
```

### Material Symbols (2,500+ icons)
**Style**: Google Material Design 3, variable font with 4 axes
**Weights**: Continuous via variable font — wght (100-700), FILL (0-1), GRAD (-25 to 200), opsz (20-48)
**License**: Apache 2.0 (permissive, commercial OK)
**Best for**: Google/Android ecosystem, projects wanting variable font approach, Material Design 3 apps
**Pros**:
- Variable font technology: one font file, infinite weight/fill/grade/optical-size combinations
- FILL axis enables smooth outline-to-solid transitions (animatable)
- Optical size axis automatically adjusts detail level for different sizes
- Official Google support with strong documentation
- Available as both variable font and static SVGs
**Cons**:
- Variable font file is large (~5MB for full set) — subsetting required
- Naming conventions differ from other libraries
- Aesthetic is distinctly "Google" — may not suit all brand identities
- Complex setup for variable font axes
**Import pattern (CSS variable font)**:
```css
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');
.icon { font-family: 'Material Symbols Outlined'; font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
.icon--filled { font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
```

### SF Symbols (5,000+ icons)
**Style**: Apple Human Interface Guidelines, 9 weights x 3 scales
**Weights**: Nine weights (Ultralight to Black) x three scales (Small, Medium, Large)
**Rendering modes**: Monochrome, Hierarchical, Palette, Multicolor
**License**: Apple-proprietary (iOS/macOS/watchOS/tvOS/visionOS only)
**Best for**: Native Apple platform development (SwiftUI, UIKit)
**Pros**:
- Deepest integration with Apple platforms — auto-adapts to Dynamic Type
- Four rendering modes enable rich color expression
- Automatic weight matching with adjacent SF Pro text
- Variable color for progress/level indicators
- Consistent with every native Apple app — users already recognize them
- 5,000+ symbols covering virtually every use case
**Cons**:
- Apple platforms only — cannot legally use on web or Android
- Requires Xcode/SF Symbols app for browsing
- Custom symbols must follow strict template guidelines
- Not available as standalone SVGs for web use
**Import pattern (SwiftUI)**:
```swift
Image(systemName: "magnifyingglass")
    .symbolRenderingMode(.hierarchical)
    .foregroundStyle(.secondary)
    .font(.system(size: 20, weight: .medium))
```

### Tabler Icons (4,800+ icons)
**Style**: Clean outline, 24x24 grid, 1.5px stroke (thinner than Lucide)
**Weights**: Single weight (outline), with filled variants for many icons
**License**: MIT (permissive, commercial OK)
**Best for**: Dashboard/admin interfaces, projects wanting a slightly lighter stroke weight
**Pros**:
- Very large set (4,800+) with excellent category coverage
- 1.5px stroke creates a lighter, more refined feel than 2px sets
- Filled variants available for selected states
- React/Vue/Svelte/Angular/Preact packages
- Active community with frequent additions
- Comprehensive Figma library
**Cons**:
- 1.5px stroke can appear blurry at 1x resolution on non-retina displays
- Mixing with 2px-stroke libraries creates visible inconsistency
- Some icons lack the geometric precision of Lucide or Heroicons
**Import pattern (React)**:
```jsx
import { IconSearch, IconSettings, IconUser } from '@tabler/icons-react';
<IconSearch size={20} stroke={1.5} className="text-gray-600" />
```

### Library Selection Criteria
| Criterion | Weight | Evaluation Method |
|-----------|--------|-------------------|
| Icon count and category coverage | High | Does it cover your app's domain? |
| Style match with brand | Critical | Does the stroke weight/style match your design system? |
| Weight variants | Medium | Do you need outline+solid, or is outline enough? |
| Framework support | High | Official React/Vue/Svelte package available? |
| Bundle size / tree-shaking | High | Can you import individual icons? |
| License | Critical | Compatible with your distribution model? |
| Maintenance / community | Medium | Regular updates? Active issue resolution? |
| Figma library | Medium | Available for design handoff? |

---

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

## 9. Illustration Styles

### Style Catalog (15+)

**1. Flat / Minimal (Notion, Linear, Slack)**
- Solid color fills, no gradients, no shadows
- Limited palette (3-5 colors + tints)
- Geometric shapes, clean edges
- Best for: SaaS dashboards, productivity tools, developer platforms

**2. Isometric (Stripe, Webflow)**
- 30-degree angle projection, no vanishing point
- Creates 3D depth without perspective distortion
- Precise geometric construction
- Best for: Fintech, infrastructure, technical products

**3. Hand-Drawn / Organic (Dropbox, Mailchimp)**
- Irregular lines, visible brush strokes, imperfect shapes
- Warm, human, approachable feeling
- Often paired with bright, playful color palettes
- Best for: Creative tools, education, community platforms

**4. Abstract Geometric (Vercel, Stripe Docs)**
- Pure geometric shapes: circles, triangles, rectangles
- No representational imagery — relies on color and composition
- Minimalist, sophisticated, modern
- Best for: Developer tools, AI products, design platforms

**5. 3D Rendered (Apple, Microsoft)**
- Realistic materials, lighting, and shadows
- High production cost but premium feel
- Often rendered in Cinema 4D, Blender, or Spline
- Best for: Consumer electronics, premium SaaS, gaming

**6. Line Art / Continuous Line**
- Single stroke weight, often a single continuous path
- Elegant, minimalist, pairs well with whitespace
- Works at any size without losing clarity
- Best for: Luxury brands, portfolios, editorial

**7. Character Illustration (Duolingo, Headspace)**
- Recurring characters/mascots with personality
- Creates emotional connection and brand recognition
- Requires character design system (poses, expressions, guidelines)
- Best for: Education, health/wellness, consumer apps, onboarding

**8. Spot Illustration**
- Small, focused illustrations for specific UI moments
- Typically 120-200px, used inline with content
- Quick to produce, easy to maintain
- Best for: Empty states, feature explanations, tooltips, onboarding steps

**9. Scene / Full Illustration**
- Large, complex compositions with multiple elements
- Hero sections, landing pages, marketing materials
- High production cost, strong storytelling
- Best for: Landing pages, marketing, editorial

**10. Data Illustration**
- Blends data visualization with illustration
- Infographic-style: charts decorated with contextual imagery
- Makes complex data approachable
- Best for: Analytics dashboards, reports, finance

**11. Photography + Illustration Hybrid**
- Real photos with illustrated overlays, annotations, or frames
- Creates unique, memorable aesthetic
- Requires careful balance to avoid looking disjointed
- Best for: Social platforms, lifestyle brands, portfolios

**12. Gradient / Aurora**
- Soft, flowing gradients as primary visual element
- Often mesh gradients or aurora-style color blends
- Modern, premium, somewhat abstract
- Best for: AI products, creative tools, music/entertainment

**13. Paper Cut / Layered**
- Simulates cut paper with shadows between layers
- Physical, tactile quality
- Distinct depth effect without 3D rendering
- Best for: Education, children's products, craft/creative

**14. Low-Poly**
- Faceted 3D surfaces with flat-shaded triangles
- Geometric, modern, slightly retro
- Easy to generate algorithmically
- Best for: Gaming, tech, data visualization

**15. Retro / Vintage**
- References specific historical design eras (70s, 80s, pixel art)
- Strong nostalgic appeal, distinctive personality
- Must be intentional — accidental retro looks dated, not charming
- Best for: Entertainment, indie products, food/beverage

**16. Claymation / Soft 3D**
- Rounded, soft 3D renders with matte materials
- Friendly, tactile, approachable
- Popular in 2024-2026 product design
- Best for: Consumer apps, fintech (friendly finance), health

---

## 10. Empty State Illustrations

### Guidelines
Empty states are critical UX moments. The user sees nothing — the illustration must carry the experience.

**Sizing**: 160-240px wide, centered in the empty container. Never larger than 50% of the viewport width on desktop or 70% on mobile.

**Placement**: Vertically centered in the available space (or upper-third for long scrollable areas). Always above the CTA text and action button.

**Messaging pattern** (illustration + text + action):
1. **Illustration** — conveys the emotional tone (friendly, professional, playful)
2. **Headline** — describes the state clearly ("No projects yet")
3. **Description** — explains what will appear here or why it is empty ("Create your first project to get started")
4. **CTA button** — primary action to resolve the empty state ("Create Project")

### Empty State Types
| Type | Tone | Example Headline | Illustration Style |
|------|------|------------------|--------------------|
| First use | Encouraging, excited | "Welcome! Let's get started" | Character waving, open door |
| No results | Helpful | "No results for 'xyz'" | Empty magnifying glass, desert |
| No data | Neutral, instructive | "No activity yet" | Empty chart, blank page |
| Error | Empathetic | "Something went wrong" | Broken robot, tangled wires |
| No permission | Clear, respectful | "You don't have access" | Locked door, shield |
| Completed | Celebratory | "All caught up!" | Checkmark, confetti, sunrise |
| Offline | Patient | "You're offline" | Cloud with X, disconnected plug |

### Color Treatment
- Empty state illustrations should use muted, desaturated colors — they should not compete with the eventual content
- Use 2-3 colors from the brand palette at 50-70% saturation
- Dark mode: reduce illustration opacity to 80% or use a dedicated dark variant

---

## 11. Spot Illustrations

### Hero Sections
- 280-400px tall, full-width or contained within a max-width
- Illustration should complement, not overwhelm, the headline
- Place illustration to the right of text on desktop, below text on mobile
- Use illustration to create visual entry point that guides the eye to the CTA

### Feature Blocks
- 80-120px spot illustrations, one per feature
- Maintain consistent style, size, and alignment across all feature blocks
- Use a grid layout: 2-3 columns on desktop, 1 column on mobile
- Illustrations should be distinct from each other but clearly part of the same family

### Onboarding Flows
- One illustration per step, 160-200px
- Progressive disclosure: illustrations should evolve or build across steps
- Use character illustrations to create narrative continuity
- Keep illustrations lightweight — onboarding must feel fast

### Error Pages
- 404: Lost/wandering theme (astronaut in space, wrong turn on a trail)
- 500: Broken/fixing theme (wrench, hard hat, under construction)
- 403: Access/permission theme (locked gate, bouncer, velvet rope)
- Size: 200-300px, centered, with a generous amount of white space
- Tone: empathetic and slightly humorous — never blame the user

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

## 13. Icon Accessibility

### Meaningful vs Decorative Icons
Every icon is either **meaningful** (conveys information) or **decorative** (visual embellishment). The treatment differs completely:

**Meaningful icons** (icon is the only way to understand the action):
```html
<!-- Method 1: aria-label on the button -->
<button aria-label="Search">
  <svg aria-hidden="true"><!-- icon --></svg>
</button>

<!-- Method 2: title element inside SVG -->
<svg role="img" aria-labelledby="search-title">
  <title id="search-title">Search</title>
  <!-- icon paths -->
</svg>

<!-- Method 3: Visually hidden text -->
<button>
  <svg aria-hidden="true"><!-- icon --></svg>
  <span class="sr-only">Search</span>
</button>
```

**Decorative icons** (icon accompanies visible text):
```html
<button>
  <svg aria-hidden="true" focusable="false"><!-- icon --></svg>
  <span>Search</span>
</button>
```

### Accessibility Rules
1. **Every icon** must have either `aria-hidden="true"` (decorative) or an accessible name (meaningful)
2. Add `focusable="false"` to inline SVGs in IE/Edge legacy to prevent tab-stop issues
3. Use `role="img"` when the SVG is meaningful and uses `<title>` for its label
4. Toggle icons must announce their state: `aria-pressed="true/false"` or `aria-expanded`
5. Icon-only buttons require a minimum 44x44px touch target (WCAG 2.5.8)
6. Color alone must not be the only indicator — pair colored icons with shape changes (e.g., filled vs outline for selected)
7. Animated icons must respect `prefers-reduced-motion` (WCAG 2.3.3)

---

## 14. Icon Color

### currentColor for Theming
The single most important technique for themeable icons: use `currentColor` as the stroke or fill value.

```css
/* The icon inherits color from its parent */
.nav-link { color: var(--text-secondary); }
.nav-link:hover { color: var(--text-primary); }
.nav-link svg { stroke: currentColor; } /* Automatically updates on hover */
```

### Multi-Color Icons
Some icons require two or more colors (e.g., a warning triangle with yellow fill and dark exclamation):
- Use CSS custom properties for each color channel
- Phosphor's Duotone weight uses `opacity: 0.2` on secondary elements
- For themed multi-color: `--icon-primary: currentColor; --icon-secondary: currentColor / 0.3;`

```css
.icon-duotone .primary { fill: var(--icon-primary, currentColor); }
.icon-duotone .secondary { fill: var(--icon-secondary, currentColor); opacity: 0.2; }
```

### Dark Mode Adaptation
| Element | Light Mode | Dark Mode | Rule |
|---------|------------|-----------|------|
| UI icons (stroke) | gray-600 (#525252) | gray-400 (#a3a3a3) | Reduce contrast slightly |
| Filled icons | gray-700 (#404040) | gray-300 (#d4d4d4) | Ensure 3:1 contrast ratio vs background |
| Accent icons | primary-600 | primary-400 | Shift to lighter shade |
| Disabled icons | gray-400 @ 38% | gray-500 @ 38% | Same opacity, shifted base |
| Illustration fills | Full saturation | 80% saturation | Reduce saturation to prevent glowing |
| Illustration strokes | gray-900 | gray-100 | Invert stroke color |

---

## 15. Platform-Specific Conventions

### SF Symbols Rendering Modes (Apple)

**Monochrome**: Single color, inherits from tint/foreground. Default mode. Use for standard UI icons.
```swift
Image(systemName: "heart.fill")
    .symbolRenderingMode(.monochrome)
    .foregroundStyle(.red)
```

**Hierarchical**: Single color with automatic opacity layers for depth. Adds visual hierarchy without extra configuration.
```swift
Image(systemName: "wifi")
    .symbolRenderingMode(.hierarchical)
    .foregroundStyle(.blue)
// Primary layer: 100% opacity, secondary: 50%, tertiary: 25%
```

**Palette**: Explicit multi-color using 2-3 specified colors. Full control over each layer.
```swift
Image(systemName: "person.crop.circle.badge.plus")
    .symbolRenderingMode(.palette)
    .foregroundStyle(.white, .blue, .green)
```

**Multicolor**: Fixed, built-in colors (like the actual Weather icons or Finder icon). Not customizable.
```swift
Image(systemName: "cloud.sun.rain.fill")
    .symbolRenderingMode(.multicolor)
// Colors are fixed by Apple — cannot override
```

**Variable Color**: Animatable 0-1 value that progressively highlights layers. Ideal for signal strength, progress.
```swift
Image(systemName: "wifi", variableValue: 0.5)
// At 0.5: bottom wave on, top wave off
```

### Material Symbols Optical Size Axis (Google)

The `opsz` axis adjusts icon detail for different rendered sizes:

| Optical Size | Rendered At | Effect |
|--------------|-------------|--------|
| 20 | 16-20px | Thicker strokes, simplified details, larger counters |
| 24 | 20-28px | Default balance of detail and weight |
| 40 | 32-44px | Finer strokes, more internal detail |
| 48 | 44px+ | Finest strokes, maximum detail, decorative use |

```css
/* Auto-adjust optical size based on font-size */
.icon-sm { font-size: 20px; font-variation-settings: 'opsz' 20; }
.icon-md { font-size: 24px; font-variation-settings: 'opsz' 24; }
.icon-lg { font-size: 40px; font-variation-settings: 'opsz' 40; }
.icon-xl { font-size: 48px; font-variation-settings: 'opsz' 48; }
```

### FILL Axis Animation
```css
/* Animate from outline to filled on hover/select */
.icon-toggle {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
  transition: font-variation-settings 200ms ease;
}
.icon-toggle:hover { font-variation-settings: 'FILL' 0.5, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
.icon-toggle[aria-selected="true"] { font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
```

### Platform Icon Convention Summary
| Convention | Apple (SF Symbols) | Google (Material Symbols) | Web (Lucide/Phosphor) |
|------------|-------------------|--------------------------|----------------------|
| Tab bar style | Outline default, fill on select | Outline default, fill on select | Outline default, fill or color on select |
| Minimum touch target | 44x44pt | 48x48dp | 44x44px (WCAG) |
| Icon sizing | Scales with Dynamic Type | Fixed dp sizes + opsz | Fixed px with rem scaling |
| Color theming | symbolRenderingMode | Variable font axes | currentColor CSS |
| Animation | symbolEffect API | CSS font-variation-settings | CSS/Framer Motion |
| Naming convention | dot.notation (heart.fill) | snake_case (favorite) | PascalCase component (Heart) |

---

## Cross-References
- component-patterns-code — Icon component implementation patterns
- ui-visual-design-system — Icon integration in design systems
- accessibility-inclusive-design — WCAG icon accessibility requirements
- ai-design-generation — AI-generated illustration workflows
- interaction-motion-design — Icon animation specifications
- platform-visual-standards — SF Symbols and Material Symbols platform details
- color-palette-library — Icon color token systems
- animation-recipe-library — Icon animation CSS/Framer Motion recipes
