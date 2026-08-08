# Icon Library Catalog

Every major icon set compared on style, weights, coverage, licence and import
pattern, plus the platform-native conventions for SF Symbols and Material Symbols.

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
