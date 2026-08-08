---
name: tokens
description: "Generate a complete W3C DTCG design token system — primitives, semantics, component tokens, multi-theme, with CSS/Tailwind/Style Dictionary output."
argument-hint: "[brand requirements or existing palette]"
---

# Tokens — Design Token System Generator

## Before running

This command needs brand requirements or an existing palette.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate a production-ready design token system following the W3C Design Tokens Community Group (DTCG) JSON specification. Outputs a 3-tier token architecture with multi-theme support, CSS custom properties, Tailwind config, and Style Dictionary configuration.

## Token Architecture

```
┌─────────────────────────────────────────────────────┐
│  TIER 3: Component Tokens                           │
│  button.primary.background → {color.action.primary} │
│  card.surface → {color.surface.elevated}            │
├─────────────────────────────────────────────────────┤
│  TIER 2: Semantic / Alias Tokens                    │
│  color.action.primary → {color.brand.500}           │
│  color.surface.elevated → {color.neutral.50}        │
├─────────────────────────────────────────────────────┤
│  TIER 1: Primitive / Global Tokens                  │
│  color.brand.500 → oklch(0.55 0.15 250)            │
│  space.400 → 16px                                   │
└─────────────────────────────────────────────────────┘
```

Tier 1 is raw values. Tier 2 assigns meaning. Tier 3 binds to components. Themes swap at Tier 2 — primitives and component references stay stable.

## Generation Protocol

1. **Gather context and constraints** before generating any tokens.

   **Required inputs:**
   - Brand colors (primary, secondary, accent) — or generate from brand name/description
   - Typography preferences (font families, scale ratio)
   - Spacing system (base-4 or base-8)
   - Platform targets (web CSS, iOS, Android, React Native)
   - Theme requirements (light, dark, high contrast)

   **Contextual inputs:**
   - Brand personality (minimal, playful, corporate, premium)
   - Sector (fintech, healthcare, e-commerce, SaaS, etc.) — determines color psychology, density norms, trust signals
   - Accessibility level: AA (default) or AAA (7:1 contrast ratios)
   - Prior Sumi outputs: check for `/style`, `/palette`, `/type` output. If available, consume palette, type scale, spacing, motion personality, tone direction. If not, use neutral defaults and note what is missing

   **OKLCH mandate:** All color scales must be generated in OKLCH color space. Raw hex or HSL scales are not acceptable. OKLCH ensures perceptually uniform lightness steps across the entire scale.

2. **Apply perceptual and accessibility principles.** Every token category has a research-backed justification.

   | Token Category | Principle | Application |
   |---------------|-----------|-------------|
   | Color scales | WCAG 2.2 + OKLCH perceptual uniformity | Generate in OKLCH; verify every fg/bg pairing meets contrast ratio; lightness steps must be perceptually even |
   | Semantic colors | Color psychology + sector conventions | Red=danger, green=success, amber=warning — sector may override (healthcare: blue=trust, fintech: green=money) |
   | Type scale | Modular scale theory (Major Third 1.25, Perfect Fourth 1.333) | Smaller ratio for dense UI, larger for editorial |
   | Spacing scale | Gestalt Proximity + sector density norms | Tighter for data-dense sectors (fintech, SaaS); generous for consumer/lifestyle |
   | Border radius | Jakob's Law + sector personality | Fintech/enterprise = subtle radius, consumer = generous radius |
   | Elevation/shadow | Depth perception + layering hierarchy | Consistent light source; limit to 5 levels |
   | Motion/duration | Doherty Threshold (<400ms for feedback) | Micro: 100-200ms; transitions: 200-400ms; entrance: 300-500ms |

3. **Generate Tier 1 — Primitive Tokens.**

   ### Color Primitives
   Generate 11-step scales (0, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950) for:
   - **Brand primary** — the hero color
   - **Brand secondary** — supporting color
   - **Brand accent** — highlight/CTA color
   - **Neutral** — gray scale for text, borders, surfaces
   - **Semantic: success** — green family
   - **Semantic: warning** — amber family
   - **Semantic: error** — red family
   - **Semantic: info** — blue family

   Each step must define:
   ```json
   {
     "color": {
       "brand": {
         "500": {
           "$value": "oklch(0.55 0.15 250)",
           "$type": "color",
           "$description": "Brand primary midpoint"
         }
       }
     }
   }
   ```

   ### Typography Primitives
   - **Font families:** primary (headings), secondary (body), mono (code)
   - **Font sizes:** Use modular scale. Generate 10+ steps: xs, sm, base, md, lg, xl, 2xl, 3xl, 4xl, 5xl, 6xl
   - **Font weights:** thin (100), light (300), regular (400), medium (500), semibold (600), bold (700), extrabold (800)
   - **Line heights:** tight (1.15), snug (1.25), normal (1.5), relaxed (1.625), loose (1.75)
   - **Letter spacing:** tighter (-0.03em), tight (-0.015em), normal (0), wide (0.025em), wider (0.05em)
   - **Paragraph spacing:** sm (0.5em), md (0.75em), lg (1em)

   ```json
   {
     "typography": {
       "fontSize": {
         "base": {
           "$value": "1rem",
           "$type": "dimension",
           "$description": "Base font size — 16px equivalent"
         },
         "lg": {
           "$value": "1.25rem",
           "$type": "dimension",
           "$description": "Large text — Major Third step up from base"
         }
       },
       "fontFamily": {
         "primary": {
           "$value": "Inter, system-ui, sans-serif",
           "$type": "fontFamily"
         }
       }
     }
   }
   ```

   ### Spacing Primitives
   Generate from base unit (4px or 8px):
   - **space.0** — 0px
   - **space.25** — 1px (hairline)
   - **space.50** — 2px
   - **space.100** — 4px
   - **space.150** — 6px
   - **space.200** — 8px
   - **space.300** — 12px
   - **space.400** — 16px
   - **space.500** — 20px
   - **space.600** — 24px
   - **space.800** — 32px
   - **space.1000** — 40px
   - **space.1200** — 48px
   - **space.1600** — 64px
   - **space.2000** — 80px
   - **space.2400** — 96px
   - **space.3200** — 128px

   ### Border Radius Primitives
   - **radius.none** — 0px
   - **radius.xs** — 2px
   - **radius.sm** — 4px
   - **radius.md** — 8px
   - **radius.lg** — 12px
   - **radius.xl** — 16px
   - **radius.2xl** — 24px
   - **radius.full** — 9999px

   ### Shadow / Elevation Primitives
   5-level system with consistent top-left light source:
   - **shadow.xs** — subtle card lift
   - **shadow.sm** — raised element
   - **shadow.md** — dropdown/popover
   - **shadow.lg** — modal/dialog
   - **shadow.xl** — toast/notification overlay

   Each shadow value uses layered box-shadow for realism:
   ```json
   {
     "shadow": {
       "md": {
         "$value": [
           { "offsetX": "0px", "offsetY": "4px", "blur": "6px", "spread": "-1px", "color": "oklch(0 0 0 / 0.1)" },
           { "offsetX": "0px", "offsetY": "2px", "blur": "4px", "spread": "-2px", "color": "oklch(0 0 0 / 0.1)" }
         ],
         "$type": "shadow"
       }
     }
   }
   ```

   ### Motion / Duration Primitives
   - **duration.instant** — 0ms (state change, no animation)
   - **duration.fast** — 100ms (micro-feedback: button press)
   - **duration.normal** — 200ms (transitions: hover, focus)
   - **duration.moderate** — 300ms (reveals: dropdown, accordion)
   - **duration.slow** — 400ms (entrance: modal, page transition)
   - **duration.slower** — 500ms (complex: multi-step animation)

   ### Easing Primitives
   - **easing.linear** — linear
   - **easing.ease-in** — cubic-bezier(0.4, 0, 1, 0.5)
   - **easing.ease-out** — cubic-bezier(0, 0, 0.2, 1)
   - **easing.ease-in-out** — cubic-bezier(0.4, 0, 0.2, 1)
   - **easing.spring** — cubic-bezier(0.34, 1.56, 0.64, 1)
   - **easing.bounce** — cubic-bezier(0.34, 1.8, 0.64, 1)

   ### Z-Index Scale
   - **z.base** — 0
   - **z.dropdown** — 100
   - **z.sticky** — 200
   - **z.overlay** — 300
   - **z.modal** — 400
   - **z.popover** — 500
   - **z.toast** — 600
   - **z.tooltip** — 700
   - **z.max** — 9999

4. **Generate Tier 2 — Semantic Tokens.**

   Semantic tokens reference primitives and carry meaning. These are what themes swap.

   ### Color Semantics
   **Backgrounds:**
   - `color.bg.primary` → page background
   - `color.bg.secondary` → section/card background
   - `color.bg.tertiary` → nested/inset background
   - `color.bg.inverse` → dark on light / light on dark
   - `color.bg.brand` → brand-tinted background
   - `color.bg.surface` → elevated surface (card, modal)
   - `color.bg.surface.raised` → higher elevation surface
   - `color.bg.overlay` → scrim/backdrop

   **Text:**
   - `color.text.primary` → main body text
   - `color.text.secondary` → supporting text, labels
   - `color.text.tertiary` → captions, metadata
   - `color.text.disabled` → inactive text
   - `color.text.inverse` → text on inverse background
   - `color.text.link` → hyperlink text
   - `color.text.link.hover` → hyperlink hover
   - `color.text.brand` → brand-colored text
   - `color.text.on-brand` → text on brand background (contrast-safe)

   **Borders:**
   - `color.border.default` → standard borders
   - `color.border.strong` → emphasized borders
   - `color.border.subtle` → light dividers
   - `color.border.brand` → brand-colored borders
   - `color.border.error` → error state border
   - `color.border.success` → success state border
   - `color.border.focus` → focus ring color

   **Actions:**
   - `color.action.primary.default` / `.hover` / `.active` / `.disabled`
   - `color.action.primary.text` → text on primary action
   - `color.action.secondary.default` / `.hover` / `.active` / `.disabled`
   - `color.action.secondary.text`
   - `color.action.destructive.default` / `.hover` / `.active` / `.disabled`
   - `color.action.destructive.text`
   - `color.action.ghost.hover` / `.active`

   **Feedback:**
   For each of success, warning, error, info:
   - `.bg` — background tint
   - `.text` — message text color
   - `.border` — border color
   - `.icon` — icon color
   - `.bg.strong` — bold/badge background

   **Focus:**
   - `focus.ring.color` → focus ring color
   - `focus.ring.width` → 2px default
   - `focus.ring.offset` → 2px default

   ### Typography Semantics
   - `type.heading.xl` → composite: family, size, weight, line-height, letter-spacing
   - `type.heading.lg`
   - `type.heading.md`
   - `type.heading.sm`
   - `type.body.lg`
   - `type.body.md`
   - `type.body.sm`
   - `type.label.lg`
   - `type.label.md`
   - `type.label.sm`
   - `type.caption`
   - `type.overline`
   - `type.code`

   Use W3C DTCG `$type: "typography"` composite format:
   ```json
   {
     "type": {
       "heading": {
         "lg": {
           "$value": {
             "fontFamily": "{typography.fontFamily.primary}",
             "fontSize": "{typography.fontSize.3xl}",
             "fontWeight": "{typography.fontWeight.bold}",
             "lineHeight": "{typography.lineHeight.tight}",
             "letterSpacing": "{typography.letterSpacing.tight}"
           },
           "$type": "typography"
         }
       }
     }
   }
   ```

   ### Spacing Semantics
   - `space.page.inline` → horizontal page padding
   - `space.page.block` → vertical page padding
   - `space.section.gap` → between major sections
   - `space.card.padding` → internal card padding
   - `space.stack.sm` / `.md` / `.lg` → vertical rhythm between elements
   - `space.inline.sm` / `.md` / `.lg` → horizontal spacing between inline elements
   - `space.input.padding.x` / `.y` → form input padding

5. **Generate Tier 3 — Component Tokens.**

   Component tokens bind semantic tokens to specific UI elements.

   ### Button
   ```json
   {
     "button": {
       "primary": {
         "bg": { "$value": "{color.action.primary.default}" },
         "text": { "$value": "{color.action.primary.text}" },
         "border": { "$value": "transparent" },
         "bg-hover": { "$value": "{color.action.primary.hover}" },
         "bg-active": { "$value": "{color.action.primary.active}" },
         "bg-disabled": { "$value": "{color.action.primary.disabled}" },
         "radius": { "$value": "{radius.md}" },
         "padding-x": { "$value": "{space.400}" },
         "padding-y": { "$value": "{space.200}" },
         "font": { "$value": "{type.label.md}" },
         "shadow": { "$value": "{shadow.xs}" }
       },
       "secondary": { "...same structure..." },
       "ghost": { "...same structure..." },
       "destructive": { "...same structure..." }
     }
   }
   ```

   ### Input
   - `input.bg`, `input.text`, `input.border`, `input.placeholder`
   - `input.border.focus`, `input.border.error`, `input.border.success`
   - `input.bg.disabled`, `input.text.disabled`
   - `input.radius`, `input.padding.x`, `input.padding.y`
   - `input.font`, `input.label.font`, `input.helper.font`

   ### Card
   - `card.bg`, `card.border`, `card.shadow`, `card.radius`, `card.padding`
   - `card.header.font`, `card.body.font`

   ### Badge
   - `badge.[variant].bg`, `badge.[variant].text`, `badge.[variant].border`
   - Variants: default, brand, success, warning, error, info

   ### Avatar
   - `avatar.size.sm` / `.md` / `.lg` / `.xl`
   - `avatar.radius`, `avatar.border`, `avatar.fallback.bg`, `avatar.fallback.text`

   ### Navigation
   - `nav.bg`, `nav.border`, `nav.item.text`, `nav.item.text.active`
   - `nav.item.bg.hover`, `nav.item.bg.active`, `nav.item.indicator`

6. **Generate Theme Variants.**

   ### Light Theme (default)
   Map semantic tokens to light-appropriate primitives:
   - `color.bg.primary` → white or near-white
   - `color.text.primary` → dark neutral (900)
   - Shadows use rgba black with low opacity

   ### Dark Theme
   Map semantic tokens to dark-appropriate primitives:
   - `color.bg.primary` → very dark neutral (not pure black — use 925 or 950)
   - `color.text.primary` → light neutral (100)
   - Shadows replaced with subtle borders or luminous glows
   - Brand colors shift: reduce lightness slightly, increase chroma for vibrancy on dark surfaces
   - Surface elevation: higher surfaces are lighter (Material Design 3 tonal elevation)

   ### High Contrast Theme
   - All text meets 7:1 contrast ratio minimum (WCAG AAA)
   - Borders are visible and strong (2px, high-contrast color)
   - Focus rings are extra prominent (3px, high-contrast)
   - No color-only indicators — always paired with shape/icon/text

7. **Generate output formats.**

   ### CSS Custom Properties
   ```css
   :root {
     /* Primitives */
     --color-brand-500: oklch(0.55 0.15 250);
     --space-400: 1rem;
     --radius-md: 0.5rem;

     /* Semantic — Light Theme */
     --color-bg-primary: var(--color-neutral-0);
     --color-text-primary: var(--color-neutral-900);
     --color-action-primary: var(--color-brand-500);
   }

   .dark,
   [data-theme="dark"] {
     --color-bg-primary: var(--color-neutral-950);
     --color-text-primary: var(--color-neutral-100);
     --color-action-primary: var(--color-brand-400);
   }

   .high-contrast,
   [data-theme="high-contrast"] {
     --color-bg-primary: #000000;
     --color-text-primary: #ffffff;
     --color-border-default: #ffffff;
   }

   @media (prefers-color-scheme: dark) {
     :root:not([data-theme]) {
       --color-bg-primary: var(--color-neutral-950);
       --color-text-primary: var(--color-neutral-100);
     }
   }

   @media (prefers-contrast: more) {
     :root:not([data-theme]) {
       --color-text-primary: #000000;
       --color-border-default: #000000;
     }
   }
   ```

   ### Tailwind v4 Config
   ```js
   // tailwind.config.js (v4 CSS-first approach)
   // Tokens are consumed directly from CSS custom properties
   // Add to your CSS:
   @theme {
     --color-brand-50: oklch(0.97 0.02 250);
     --color-brand-100: oklch(0.93 0.04 250);
     --color-brand-500: oklch(0.55 0.15 250);
     --color-brand-900: oklch(0.25 0.08 250);

     --color-bg-primary: var(--color-neutral-0);
     --color-bg-secondary: var(--color-neutral-50);
     --color-text-primary: var(--color-neutral-900);
     --color-text-secondary: var(--color-neutral-600);

     --spacing-xs: 0.25rem;
     --spacing-sm: 0.5rem;
     --spacing-md: 1rem;
     --spacing-lg: 1.5rem;
     --spacing-xl: 2rem;

     --radius-sm: 0.25rem;
     --radius-md: 0.5rem;
     --radius-lg: 0.75rem;

     --shadow-sm: 0 1px 2px 0 oklch(0 0 0 / 0.05);
     --shadow-md: 0 4px 6px -1px oklch(0 0 0 / 0.1), 0 2px 4px -2px oklch(0 0 0 / 0.1);

     --font-family-primary: "Inter", system-ui, sans-serif;
     --font-family-mono: "JetBrains Mono", ui-monospace, monospace;

     --text-xs: 0.75rem;
     --text-sm: 0.875rem;
     --text-base: 1rem;
     --text-lg: 1.25rem;
     --text-xl: 1.5rem;
     --text-2xl: 1.875rem;
     --text-3xl: 2.25rem;
   }
   ```

   ### Tailwind v3 Config (legacy)
   ```js
   /** @type {import('tailwindcss').Config} */
   module.exports = {
     theme: {
       extend: {
         colors: {
           brand: {
             50: 'var(--color-brand-50)',
             100: 'var(--color-brand-100)',
             // ... full scale
             900: 'var(--color-brand-900)',
           },
           bg: {
             primary: 'var(--color-bg-primary)',
             secondary: 'var(--color-bg-secondary)',
             surface: 'var(--color-bg-surface)',
           },
           text: {
             primary: 'var(--color-text-primary)',
             secondary: 'var(--color-text-secondary)',
           },
         },
         spacing: {
           // Map token names to CSS vars
         },
         borderRadius: {
           // Map token names to CSS vars
         },
         boxShadow: {
           // Map token names to CSS vars
         },
       },
     },
   };
   ```

   ### Style Dictionary Config
   ```json
   {
     "source": [".sumi/style.json"],
     "platforms": {
       "css": {
         "transformGroup": "css",
         "buildPath": "build/css/",
         "files": [{
           "destination": "tokens.css",
           "format": "css/variables",
           "options": {
             "outputReferences": true
           }
         }]
       },
       "js": {
         "transformGroup": "js",
         "buildPath": "build/js/",
         "files": [{
           "destination": "tokens.js",
           "format": "javascript/es6"
         }]
       },
       "ios": {
         "transformGroup": "ios-swift-separate",
         "buildPath": "build/ios/",
         "files": [{
           "destination": "Tokens.swift",
           "format": "ios-swift/class.swift",
           "className": "DesignTokens"
         }]
       },
       "android": {
         "transformGroup": "android",
         "buildPath": "build/android/",
         "files": [{
           "destination": "tokens.xml",
           "format": "android/resources"
         }]
       }
     }
   }
   ```

   ### TypeScript Type Definitions
   ```ts
   // Generated from .sumi/style.json
   export interface DesignTokens {
     color: {
       brand: Record<'0' | '50' | '100' | '200' | '300' | '400' | '500' | '600' | '700' | '800' | '900' | '950', string>;
       neutral: Record<'0' | '50' | '100' | '200' | '300' | '400' | '500' | '600' | '700' | '800' | '900' | '950', string>;
       success: Record<string, string>;
       warning: Record<string, string>;
       error: Record<string, string>;
       info: Record<string, string>;
       bg: {
         primary: string;
         secondary: string;
         tertiary: string;
         inverse: string;
         brand: string;
         surface: string;
         overlay: string;
       };
       text: {
         primary: string;
         secondary: string;
         tertiary: string;
         disabled: string;
         inverse: string;
         link: string;
         brand: string;
       };
       border: {
         default: string;
         strong: string;
         subtle: string;
         brand: string;
         error: string;
         success: string;
         focus: string;
       };
       action: {
         primary: ActionTokenSet;
         secondary: ActionTokenSet;
         destructive: ActionTokenSet;
       };
       feedback: {
         success: FeedbackTokenSet;
         warning: FeedbackTokenSet;
         error: FeedbackTokenSet;
         info: FeedbackTokenSet;
       };
     };
     typography: {
       fontFamily: { primary: string; secondary: string; mono: string };
       fontSize: Record<string, string>;
       fontWeight: Record<string, number>;
       lineHeight: Record<string, string>;
       letterSpacing: Record<string, string>;
     };
     space: Record<string, string>;
     radius: Record<string, string>;
     shadow: Record<string, string>;
     duration: Record<string, string>;
     easing: Record<string, string>;
     z: Record<string, number>;
   }

   interface ActionTokenSet {
     default: string;
     hover: string;
     active: string;
     disabled: string;
     text: string;
   }

   interface FeedbackTokenSet {
     bg: string;
     text: string;
     border: string;
     icon: string;
     bgStrong: string;
   }
   ```

   ### Figma Variables Mapping Guide

   Map W3C DTCG tokens to Figma's variable system:

   | DTCG Token Path | Figma Collection | Figma Variable Name | Mode Mapping |
   |----------------|-----------------|--------------------|--------------|
   | `color.brand.*` | Primitives | brand/50 ... brand/950 | Single mode |
   | `color.bg.*` | Semantic | bg/primary, bg/secondary | Light, Dark, High Contrast |
   | `color.text.*` | Semantic | text/primary, text/secondary | Light, Dark, High Contrast |
   | `color.action.*` | Semantic | action/primary/default | Light, Dark, High Contrast |
   | `typography.fontSize.*` | Primitives | font-size/base, font-size/lg | Single mode |
   | `space.*` | Primitives | space/100, space/200 | Single mode |
   | `radius.*` | Primitives | radius/sm, radius/md | Single mode |
   | `button.primary.*` | Component | button/primary/bg | Resolves from Semantic |

   **Figma setup steps:**
   1. Create three variable collections: Primitives, Semantic, Component
   2. In Primitives: define all raw values (colors, sizes, spacing)
   3. In Semantic: create Light, Dark, High Contrast modes — alias to Primitives
   4. In Component: alias to Semantic variables
   5. Apply Component variables to your design components
   6. Switch modes at the frame level to preview themes

8. **Save to `.sumi/style.json`.**

   The complete token file is saved in W3C DTCG format at `.sumi/style.json`. This file is consumed by:
   - `/dark` — reads light tokens and generates dark mode counterparts
   - `/screen` — applies tokens when building screen layouts
   - `/ship` — applies tokens when generating component code
   - `/responsive` — references spacing and type tokens for fluid scaling
   - Style Dictionary — transforms to any platform output

   File structure:
   ```json
   {
     "$schema": "https://design-tokens.github.io/community-group/format/",
     "color": {
       "brand": { "...primitive scales..." },
       "neutral": { "...primitive scales..." },
       "success": { "..." },
       "warning": { "..." },
       "error": { "..." },
       "info": { "..." },
       "bg": { "...semantic backgrounds..." },
       "text": { "...semantic text colors..." },
       "border": { "...semantic borders..." },
       "action": { "...semantic actions..." },
       "feedback": { "...semantic feedback..." }
     },
     "typography": { "..." },
     "space": { "..." },
     "radius": { "..." },
     "shadow": { "..." },
     "duration": { "..." },
     "easing": { "..." },
     "z": { "..." },
     "type": { "...composite typography semantics..." },
     "button": { "...component tokens..." },
     "input": { "...component tokens..." },
     "card": { "...component tokens..." },
     "badge": { "...component tokens..." },
     "nav": { "...component tokens..." },
     "$themes": {
       "light": { "...semantic overrides..." },
       "dark": { "...semantic overrides..." },
       "high-contrast": { "...semantic overrides..." }
     }
   }
   ```

## Output Format

```
### Phase Position
> **Phase: BUILD** | `/tokens`
> *Design Systems Architecture | Token Foundation*

## Design Token System: [Project Name]

### Configuration
- **Brand**: [name/colors provided]
- **Scale**: [base-4 / base-8]
- **Type ratio**: [ratio name and value]
- **Themes**: [light, dark, high-contrast]
- **Platforms**: [web, iOS, Android]
- **Accessibility**: [AA / AAA]
- **Sector**: [sector]

### Tier 1 — Primitive Tokens
[Complete primitive token JSON in W3C DTCG format]

### Tier 2 — Semantic Tokens
[Complete semantic token JSON with theme mappings]

### Tier 3 — Component Tokens
[Complete component token JSON]

### CSS Custom Properties
[Full CSS output for all themes]

### Tailwind Configuration
[Tailwind v4 @theme block or v3 config object]

### Style Dictionary Config
[Ready-to-use config.json]

### TypeScript Definitions
[Type definitions for consuming tokens in code]

### Figma Variables Setup
[Step-by-step Figma variable mapping]

### Token Rationale
| Token | Value | Principle | Reasoning |
|-------|-------|-----------|-----------|
| --color-brand-500 | oklch(...) | OKLCH + sector color psychology | [why] |
| --font-size-scale | [ratio] | Modular scale theory | [why] |
| --space-base | [value] | Gestalt Proximity | [why] |
| ... | ... | ... | ... |

### Accessibility Verification
| Foreground Token | Background Token | Contrast Ratio | WCAG Level | Status |
|-----------------|-----------------|---------------|------------|--------|
| color.text.primary | color.bg.primary | [X.X:1] | AA (4.5:1) | [Pass/Fail] |
| color.text.secondary | color.bg.primary | [X.X:1] | AA (4.5:1) | [Pass/Fail] |
| color.action.primary.text | color.action.primary.default | [X.X:1] | AA (4.5:1) | [Pass/Fail] |
| ... | ... | ... | ... | ... |

### Prior Output Integration
- **`/style` consumed**: [Yes/No — what was used]
- **`/palette` consumed**: [Yes/No — what was used]
- **`/type` consumed**: [Yes/No — what was used]
- **Missing context**: [What prior outputs would improve these tokens]

### Saved
> Tokens saved to `.sumi/style.json`
```

## Cross-References

When generating tokens, draw from:
- `design-systems-architecture` skill for W3C DTCG specification and token architecture
- `ui-visual-design-system` skill for color theory and typography systems
- `design-token-presets` skill for industry-specific preset token systems
- `color-palette-library` skill for curated palettes with oklch values and APCA scores
- `typography-pairing-recipes` skill for font pairings and type scale recipes
- `shadow-elevation-density` skill for shadow scales and elevation hierarchy
- `sector-style-intelligence` skill for sector-specific token recommendations
- `accessibility-inclusive-design` skill for WCAG contrast and high-contrast theme generation
- `cognitive-psychology-ux` skill for perceptual principles (color psychology, Gestalt proximity)

## Next Step

**Next** → `/screen` — Build screens using your new token system

**Alternatives**:
- `/dark` — Generate a complete dark mode system from these tokens
- `/ship` — Skip screens, build components directly with tokens
- `/responsive` — Add responsive behavior to your token-based layouts
- `/style` — Go back to DISCOVER for style direction if tokens feel generic
- `/guide` — See the full journey

---

## Team Design System Sync

Share design tokens across a team so every developer's Chef Sumi output is consistent. One person establishes the design system, everyone inherits it.

### Setup Protocol

**Step 1: Establish the Source of Truth**

One team member runs `/style` and `/tokens` to generate the design system. This creates:
- `.sumi/style.json` — visual identity decisions
- `.sumi/context.json` — project context

**Step 2: Commit to Repository**

Add `.sumi/` to version control:
```bash
git add .sumi/
git commit -m "Add Chef Sumi design system tokens"
```

Every team member who clones or pulls the repo now has the same design tokens.

**Step 3: Automatic Inheritance**

When any team member runs a Chef Sumi command (`/screen`, `/component`, `/form`, `/fix`, etc.), the command automatically:
1. Checks for `.sumi/style.json` in the project root
2. Loads all tokens (colors, typography, spacing, motion, radii, shadows)
3. Uses those tokens in all generated code
4. Ensures consistency without manual token copying

### Updating Tokens

When the design system evolves:
1. One person runs `/style` or `/tokens` with updated parameters
2. `.sumi/style.json` is regenerated
3. Commit and push the updated file
4. All team members pull and get the updated system
5. Future commands automatically use the new tokens

### Conflict Resolution

If multiple team members modify `.sumi/style.json`:
- Treat it as a JSON file — standard git merge applies
- If conflicts occur, the design lead should resolve and re-run `/tokens` to ensure consistency
- Recommend designating one person as the "design system owner" who manages `.sumi/`

### Multi-Brand / Multi-Theme Support

For projects with multiple brands or themes:
```
.sumi/
  style.json           ← default/primary brand
  style.dark.json      ← dark theme overrides
  style.brand-b.json   ← second brand tokens
  context.json         ← shared project context
```

Commands accept a theme parameter:
- `/screen dashboard --theme dark` → uses `style.dark.json`
- `/component card --brand brand-b` → uses `style.brand-b.json`

If no theme is specified, use `style.json` (the default).

### CI/CD Integration

Use Chef Sumi's Design Quality Score in CI/CD pipelines:

**GitHub Action** (add to `.github/workflows/design-qa.yml`):
```yaml
name: Design QA
on: [pull_request]

jobs:
  design-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code
      - name: Run Design QA
        run: |
          claude -p "Run /qa project on this codebase. Output the Design Quality Score. If any file scores below 60, list it."
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

**Pre-commit Hook** (add to `.husky/pre-commit` or `.git/hooks/pre-commit`):
```bash
#!/bin/sh
# Run Chef Sumi design QA on changed UI files
changed_ui_files=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(tsx|jsx|vue|svelte|css)$')
if [ -n "$changed_ui_files" ]; then
  echo "Running Chef Sumi design check on changed UI files..."
  claude -p "Run /qa on these files: $changed_ui_files. Report any design quality issues."
fi
```

### Token Export Formats

`/tokens` can export to multiple formats for integration with existing tooling:

| Format | Command | Output |
|--------|---------|--------|
| CSS Custom Properties | `/tokens css` | `:root { --color-primary: ... }` |
| Tailwind Config | `/tokens tailwind` | `theme: { extend: { colors: ... } }` |
| W3C DTCG JSON | `/tokens json` | Standard design token JSON |
| Style Dictionary | `/tokens style-dictionary` | Style Dictionary config + tokens |
| Figma Variables | `/tokens figma` | Figma-importable variable structure |
| SwiftUI Extensions | `/tokens swift` | Color/Font Swift extensions |
| Compose Theme | `/tokens compose` | MaterialTheme Kotlin objects |
