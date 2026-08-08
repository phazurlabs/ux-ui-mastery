---
name: icon
description: "Generate an icon system — library selection, sizing tokens, React wrapper component, animated recipes, SVG optimization, and accessibility."
argument-hint: "[icon set or product context]"
---

# Icon — Icon System Builder

## Before running

This command needs the product context the icon system serves.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate a complete icon implementation system: library selection with rationale, sizing scale tied to design tokens, a production React wrapper component, animated icon recipes, SVG optimization config, and accessibility patterns.

## Generation Protocol

1. **Gather inputs.**

   **Required:**
   - Icon set preference: `lucide`, `heroicons`, `phosphor`, `material`, `sf-symbols`, or `recommend`
   - Project context: web app, mobile app, marketing site, dashboard, etc.
   - Design personality: minimal, playful, corporate, premium, technical

   **Optional:**
   - Token system reference (from `/tokens` or `.sumi/style.json`)
   - Existing icon usage to match
   - Stroke vs. fill preference
   - Custom icons needed alongside the library

2. **Select or recommend icon library.**

   If input is `recommend`, evaluate based on project context:

   | Library | Style | Stroke Weight | Count | Best For | License |
   |---------|-------|--------------|-------|----------|---------|
   | **Lucide** | Clean, geometric | 1.5px-2px (adjustable) | 1500+ | SaaS, dashboards, developer tools | ISC |
   | **Heroicons** | Tailwind-aligned | 1.5px (outline) / fill | 300+ | Tailwind projects, marketing sites | MIT |
   | **Phosphor** | Flexible, 6 weights | Thin to Fill | 1200+ x 6 | Versatile, multi-weight needs | MIT |
   | **Material Symbols** | Google MD3 | Optical sizes, fill, weight, grade | 2500+ | Material Design projects, Android-first | Apache 2.0 |
   | **SF Symbols** | Apple native | 9 weights x 3 scales | 5000+ | iOS/macOS native apps only | Apple EULA |

   ### Recommendation Matrix

   | Project Type | Recommended | Reasoning |
   |-------------|-------------|-----------|
   | SaaS dashboard | Lucide or Phosphor | Clean at small sizes, large catalog for data UI |
   | Marketing site | Heroicons | Pairs with Tailwind, curated set prevents bloat |
   | Multi-platform app | Phosphor | 6 weights match any brand personality |
   | Data-heavy interface | Material Symbols | Variable font approach, optical sizing |
   | iOS native | SF Symbols | Required for platform consistency |
   | Playful consumer app | Phosphor (duotone) | Duotone weight adds personality |
   | Corporate enterprise | Lucide or Material | Neutral, professional feel |
   | Developer tools | Lucide | Popular in dev community, Radix/shadcn ecosystem |

3. **Define icon sizing scale.**

   Tie icon sizes to the design token system:

   ```json
   {
     "icon": {
       "size": {
         "xs": { "$value": "12px", "$type": "dimension", "$description": "Inline with small text, badges" },
         "sm": { "$value": "16px", "$type": "dimension", "$description": "Inline with body text, form labels" },
         "md": { "$value": "20px", "$type": "dimension", "$description": "Default — buttons, nav items, list icons" },
         "lg": { "$value": "24px", "$type": "dimension", "$description": "Section headers, prominent actions" },
         "xl": { "$value": "32px", "$type": "dimension", "$description": "Feature icons, empty states" },
         "2xl": { "$value": "48px", "$type": "dimension", "$description": "Hero illustrations, onboarding" }
       },
       "strokeWidth": {
         "light": { "$value": "1px", "$description": "Thin weight — decorative, large sizes" },
         "default": { "$value": "1.5px", "$description": "Standard weight — most use cases" },
         "bold": { "$value": "2px", "$description": "Heavy weight — emphasis, small sizes" }
       },
       "color": {
         "default": { "$value": "currentColor", "$description": "Inherits from parent text color" },
         "muted": { "$value": "{color.text.secondary}", "$description": "De-emphasized icons" },
         "brand": { "$value": "{color.action.primary.default}", "$description": "Brand-colored icons" },
         "success": { "$value": "{color.feedback.success.icon}", "$description": "Success state" },
         "warning": { "$value": "{color.feedback.warning.icon}", "$description": "Warning state" },
         "error": { "$value": "{color.feedback.error.icon}", "$description": "Error state" },
         "info": { "$value": "{color.feedback.info.icon}", "$description": "Info state" }
       }
     }
   }
   ```

   ### Optical Sizing Rules
   - At `xs` (12px) and `sm` (16px): use `bold` stroke weight — thin strokes disappear at small sizes
   - At `md` (20px): use `default` stroke weight
   - At `lg` (24px) and above: can use `light` stroke weight for elegance
   - At `2xl` (48px)+: consider filled variants instead of outlined

4. **Generate React icon wrapper component.**

   ```tsx
   import { forwardRef, type SVGProps, type ComponentType } from 'react';
   import { clsx } from 'clsx';

   /* ─── Types ─── */
   export type IconSize = 'xs' | 'sm' | 'md' | 'lg' | 'xl' | '2xl';
   export type IconColor = 'default' | 'muted' | 'brand' | 'success' | 'warning' | 'error' | 'info';

   export interface IconProps extends Omit<SVGProps<SVGSVGElement>, 'color'> {
     /** The icon component from your icon library (e.g., Lucide, Heroicons) */
     icon: ComponentType<SVGProps<SVGSVGElement>>;
     /** Size token — maps to design token scale */
     size?: IconSize;
     /** Color variant */
     color?: IconColor;
     /** Accessible label — if provided, icon is meaningful (img role). If omitted, icon is decorative (hidden). */
     label?: string;
     /** Additional CSS class */
     className?: string;
   }

   /* ─── Size map (px values from tokens) ─── */
   const sizeMap: Record<IconSize, number> = {
     xs: 12,
     sm: 16,
     md: 20,
     lg: 24,
     xl: 32,
     '2xl': 48,
   };

   /* ─── Stroke width by size (optical sizing) ─── */
   const strokeMap: Record<IconSize, number> = {
     xs: 2,
     sm: 2,
     md: 1.5,
     lg: 1.5,
     xl: 1.5,
     '2xl': 1,
   };

   /* ─── Color map (CSS custom property references) ─── */
   const colorMap: Record<IconColor, string> = {
     default: 'currentColor',
     muted: 'var(--color-text-secondary)',
     brand: 'var(--color-action-primary)',
     success: 'var(--color-feedback-success-icon)',
     warning: 'var(--color-feedback-warning-icon)',
     error: 'var(--color-feedback-error-icon)',
     info: 'var(--color-feedback-info-icon)',
   };

   /* ─── Component ─── */
   export const Icon = forwardRef<SVGSVGElement, IconProps>(
     ({ icon: IconComponent, size = 'md', color = 'default', label, className, style, ...rest }, ref) => {
       const pxSize = sizeMap[size];
       const strokeWidth = strokeMap[size];
       const colorValue = colorMap[color];

       const isDecorative = !label;

       return (
         <IconComponent
           ref={ref}
           width={pxSize}
           height={pxSize}
           strokeWidth={strokeWidth}
           className={clsx('icon', `icon-${size}`, `icon-${color}`, className)}
           style={{ color: colorValue, flexShrink: 0, ...style }}
           role={isDecorative ? 'presentation' : 'img'}
           aria-hidden={isDecorative ? true : undefined}
           aria-label={isDecorative ? undefined : label}
           focusable="false"
           {...rest}
         />
       );
     }
   );

   Icon.displayName = 'Icon';
   ```

   ### Usage Examples
   ```tsx
   import { Icon } from '@/components/ui/icon';
   import { Search, Check, AlertTriangle, Loader2 } from 'lucide-react';

   /* Decorative icon in a button (text provides meaning) */
   <button>
     <Icon icon={Search} size="sm" />
     <span>Search</span>
   </button>

   /* Meaningful icon (no adjacent text) */
   <Icon icon={Check} size="md" color="success" label="Completed" />

   /* Muted icon in a list */
   <li>
     <Icon icon={AlertTriangle} size="sm" color="warning" />
     <span>3 issues found</span>
   </li>
   ```

5. **Define icon usage guidelines by component type.**

   | Component | Icon Size | Color | Position | Notes |
   |-----------|----------|-------|----------|-------|
   | Button (with text) | `sm` (16px) | `default` | Left of text | 8px gap to text |
   | Button (icon-only) | `md` (20px) | `default` | Centered | Must have `label` for a11y |
   | Navigation item | `md` (20px) | `default` / `brand` (active) | Left of label | Active state uses brand color |
   | Form input prefix | `sm` (16px) | `muted` | Inside input, left | Decorative — `aria-hidden` |
   | Form validation | `sm` (16px) | `error` / `success` | Right of input | Paired with text message |
   | Table header sort | `xs` (12px) | `muted` | Right of header text | Shows sort direction |
   | Toast/alert | `md` (20px) | Matches alert type | Left of message | Decorative if icon matches text |
   | Empty state | `2xl` (48px) | `muted` | Above heading | Illustrative, decorative |
   | Badge | `xs` (12px) | Inherits badge color | Left of badge text | Tight spacing, 4px gap |
   | Breadcrumb separator | `xs` (12px) | `muted` | Between items | ChevronRight, decorative |
   | Dropdown trigger | `sm` (16px) | `muted` | Right of text | ChevronDown, decorative |
   | Modal close | `md` (20px) | `muted` | Top-right corner | Must have `label="Close"` |
   | Sidebar nav | `md` (20px) | `default` | Left of label | Collapsed: icon-only with tooltip |

6. **Generate animated icon recipes.**

   ### Spinner (loading)
   ```tsx
   export function Spinner({ size = 'md' }: { size?: IconSize }) {
     return (
       <Icon
         icon={Loader2}
         size={size}
         color="muted"
         label="Loading"
         className="animate-spin"
       />
     );
   }
   ```
   ```css
   .animate-spin {
     animation: spin 1s linear infinite;
   }
   @keyframes spin {
     to { transform: rotate(360deg); }
   }
   ```

   ### Toggle (hamburger to X)
   ```tsx
   export function MenuToggle({ isOpen }: { isOpen: boolean }) {
     return (
       <Icon
         icon={isOpen ? X : Menu}
         size="md"
         label={isOpen ? 'Close menu' : 'Open menu'}
         className="transition-transform duration-200"
         style={{ transform: isOpen ? 'rotate(90deg)' : 'rotate(0deg)' }}
       />
     );
   }
   ```

   ### Success Check (animated draw)
   ```css
   .icon-check-animated {
     stroke-dasharray: 24;
     stroke-dashoffset: 24;
     animation: draw-check 0.4s ease-out 0.1s forwards;
   }
   @keyframes draw-check {
     to { stroke-dashoffset: 0; }
   }
   ```
   ```tsx
   export function SuccessCheck({ size = 'lg' }: { size?: IconSize }) {
     return (
       <Icon
         icon={Check}
         size={size}
         color="success"
         label="Success"
         className="icon-check-animated"
       />
     );
   }
   ```

   ### Notification Bell (attention pulse)
   ```css
   .icon-bell-pulse {
     animation: bell-ring 0.5s ease-in-out;
     transform-origin: top center;
   }
   @keyframes bell-ring {
     0%, 100% { transform: rotate(0deg); }
     20% { transform: rotate(12deg); }
     40% { transform: rotate(-10deg); }
     60% { transform: rotate(6deg); }
     80% { transform: rotate(-4deg); }
   }
   ```

   ### Heart (like toggle)
   ```css
   .icon-heart-pop {
     animation: heart-pop 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
   }
   @keyframes heart-pop {
     0% { transform: scale(1); }
     50% { transform: scale(1.3); }
     100% { transform: scale(1); }
   }
   ```

   ### Copy Confirmation (icon swap)
   ```tsx
   export function CopyButton({ text }: { text: string }) {
     const [copied, setCopied] = useState(false);

     const handleCopy = async () => {
       await navigator.clipboard.writeText(text);
       setCopied(true);
       setTimeout(() => setCopied(false), 2000);
     };

     return (
       <button onClick={handleCopy} aria-label={copied ? 'Copied' : 'Copy to clipboard'}>
         <Icon
           icon={copied ? Check : Copy}
           size="sm"
           color={copied ? 'success' : 'muted'}
           className="transition-all duration-200"
         />
       </button>
     );
   }
   ```

7. **SVG optimization config (SVGO).**

   For custom SVG icons, optimize with SVGO before inclusion:

   ```js
   // svgo.config.js
   module.exports = {
     multipass: true,
     plugins: [
       'preset-default',
       'removeDimensions',          // Use viewBox instead of width/height
       'removeXMLNS',               // Not needed for inline SVGs
       'sortAttrs',                 // Consistent attribute order
       'removeTitle',               // Title handled by aria-label
       {
         name: 'removeAttrs',
         params: {
           attrs: ['data-name', 'class']  // Remove editor artifacts
         }
       },
       {
         name: 'addAttributesToSVGElement',
         params: {
           attributes: [
             { fill: 'none' },
             { stroke: 'currentColor' },
             { 'stroke-width': '1.5' },
             { 'stroke-linecap': 'round' },
             { 'stroke-linejoin': 'round' }
           ]
         }
       },
       {
         name: 'convertPathData',
         params: {
           floatPrecision: 2         // Reduce file size
         }
       }
     ]
   };
   ```

   ### Build Integration
   ```json
   {
     "scripts": {
       "icons:optimize": "svgo --config svgo.config.js -f src/icons/raw -o src/icons/optimized",
       "icons:build": "npm run icons:optimize && node scripts/generate-icon-exports.js"
     }
   }
   ```

   ### Custom Icon Template
   For adding custom icons alongside the library:
   ```tsx
   // src/icons/custom/CustomIcon.tsx
   import type { SVGProps } from 'react';

   export function CustomIcon(props: SVGProps<SVGSVGElement>) {
     return (
       <svg
         viewBox="0 0 24 24"
         fill="none"
         stroke="currentColor"
         strokeWidth={1.5}
         strokeLinecap="round"
         strokeLinejoin="round"
         {...props}
       >
         {/* paths here */}
       </svg>
     );
   }
   ```

8. **Accessibility rules.**

   ### Decision Tree
   ```
   Is the icon purely decorative (adjacent text conveys meaning)?
   ├─ YES → aria-hidden="true", role="presentation", no label
   └─ NO → Is there a visible text label nearby?
       ├─ YES → aria-hidden="true" (text provides the accessible name)
       └─ NO → MUST have aria-label="[description]" and role="img"
   ```

   ### Rules
   - **Icon-only buttons** must always have an accessible label (`aria-label` on button or `label` prop on Icon)
   - **Decorative icons** next to text: always `aria-hidden="true"`
   - **Status icons** (success check, error X): if no adjacent text, add `aria-label`
   - **Animated icons**: if animation conveys meaning (loading), add `aria-label`. If decorative, `aria-hidden`
   - **focusable="false"**: always set on `<svg>` elements to prevent IE/Edge focus trap (legacy but harmless)
   - **Color is never the only indicator**: pair colored icons with text labels or shape differences (WCAG 1.4.1)
   - **Reduced motion**: wrap animations in `prefers-reduced-motion` check
     ```css
     @media (prefers-reduced-motion: reduce) {
       .animate-spin { animation: none; }
       .icon-bell-pulse { animation: none; }
       .icon-heart-pop { animation: none; }
       .icon-check-animated {
         stroke-dashoffset: 0;
         animation: none;
       }
     }
     ```

## Output Format

```
### Phase Position
> **Phase: BUILD** | `/icon`
> *Design Systems | Icon System*

## Icon System: [Project Name]

### Library Selection
- **Library**: [selected library]
- **Reasoning**: [why this library fits the project]
- **Style**: [outline / fill / duotone]
- **Stroke weight**: [default weight]

### Sizing Scale
[Token-based sizing scale with optical sizing rules]

### React Icon Component
[Complete Icon component with TypeScript]

### Usage Guidelines
[Per-component icon usage table]

### Animated Recipes
[Spinner, toggle, success, notification, like animations with CSS + React]

### SVG Optimization
[SVGO config and build script]

### Accessibility
[Decision tree, rules, reduced motion handling]

### Custom Icon Template
[Template for adding project-specific icons]
```

## Cross-References

When building the icon system, draw from:
- `icon-illustration-systems` skill for icon design principles, library comparisons, and illustration systems
- `design-systems-architecture` skill for icon tokens within the design system
- `component-patterns-code` skill for React component patterns
- `accessibility-inclusive-design` skill for icon accessibility (WCAG 1.1.1, 1.4.1)
- `interaction-motion-design` skill for icon animation principles
- `animation-recipe-library` skill for production animation recipes
- `platform-visual-standards` skill for SF Symbols and Material Symbols platform conventions

## Next Step

**Next** → `/ship` — Build components using your icon system

**Alternatives**:
- `/tokens` — Generate the token system that icon sizes reference
- `/screen` — Build screens with icons integrated
- `/access` — Audit icon accessibility
- `/guide` — See the full journey
