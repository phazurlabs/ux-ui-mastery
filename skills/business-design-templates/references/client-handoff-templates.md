# Client Handoff Templates — From Design to Production

## Handoff Philosophy

The handoff is not a moment; it is a process. The traditional "throw it over the wall" model where a designer exports a PDF and hopes for the best produces mediocre results. Modern handoff is a continuous dialogue between design and development, supported by shared tools, shared language, and shared accountability for the final output.

The goal of handoff documentation is to answer every question a developer would have before they have to ask it. Every hour a developer spends guessing, searching for information, or waiting for a designer's response is wasted. Every specification left ambiguous becomes a coin flip.

### Handoff Principles

1. **The Figma file is the source of truth.** All other documentation supplements the Figma file; it does not replace it. If there is a conflict between a spec document and the Figma file, the Figma file wins (assuming it is up to date).

2. **Design tokens are the shared contract.** Every visual value (color, spacing, type size, shadow, radius, motion duration) should reference a token, not a raw value. Tokens ensure that the developer's implementation uses the same values as the designer's Figma file, because both pull from the same token source.

3. **States are not optional.** If a component can be loading, empty, errored, disabled, focused, or hovered, those states must be designed and documented. The default state is the minimum viable design, not the complete design.

4. **Responsive is not an afterthought.** Every screen should be documented at all target breakpoints. If a design is delivered only at desktop width, the developer will make responsive decisions without design guidance.

5. **Accessibility is part of the spec, not a separate checklist.** Focus order, ARIA roles, keyboard navigation, contrast ratios, and screen reader announcements should be documented alongside visual specifications, not in a separate document that gets overlooked.

---

## 1. Figma Handoff Best Practices

### File Organization for Handoff

```
FIGMA FILE STRUCTURE FOR HANDOFF
═══════════════════════════════════════════════════════════════

Page Organization:
──────────────────
📄 Cover
   └── Project name, status, last updated, links to docs

📄 Changelog
   └── Version history with dates and descriptions of changes

📄 Design Tokens
   └── Visual reference for all tokens (auto-generated from variables)

📄 Components
   └── All components with variants displayed
   └── Component documentation (description, usage, states)

📄 Screens — [Feature/Section Name]
   └── Desktop views
   └── Tablet views
   └── Mobile views
   └── State variations (loading, empty, error)

📄 Screens — [Another Feature/Section]
   └── [Same structure]

📄 Prototype Flows
   └── Named flows with entry points documented

📄 Handoff Notes
   └── Interaction specifications
   └── Animation specifications
   └── Edge case documentation
   └── Developer Q&A log

📄 Archive
   └── Previous iterations (kept for reference, clearly labeled)

Layer Naming Convention:
────────────────────────
- Use descriptive, semantic names (not "Frame 427")
- Match component names to code component names where possible
- Use "/" for hierarchy: "Header/Navigation/DesktopNav"
- Prefix states: "State=Default", "State=Hover", "State=Error"
- Mark optional elements: "[Optional] Subtitle"
- Mark dev-only notes: "[DEV] Animation: 200ms ease-out"

Variable Setup:
───────────────
- All colors bound to semantic variables (no hex values on layers)
- All spacing bound to spacing variables
- All typography bound to type scale variables
- Modes configured: Light / Dark / High Contrast (minimum)
- Variable descriptions filled in for developer clarity

Component Descriptions:
───────────────────────
Every component should have a description in Figma's component
description field that includes:
- What it is (one sentence)
- When to use it
- Any critical behavioral notes
- Link to full documentation (Storybook/docs site)
```

### Figma Dev Mode Optimization

```
DEV MODE PREPARATION CHECKLIST
═══════════════════════════════════════════════════════════════

Before marking screens as "Ready for dev":

□ All components use Auto Layout (no absolute positioning unless
  required for overlays/badges)
□ All Auto Layout padding and gaps use spacing variables
□ All colors reference semantic tokens (check with Figma's
  selection colors panel — no "local" colors should appear)
□ All text uses type scale variables for size, weight, line-height
□ All border-radius values use radius variables
□ All shadows use elevation variables
□ Component properties match intended code API (prop names should
  match what developers will use)
□ Boolean properties named with "show" prefix: showIcon, showBadge
□ Instance swap properties named for the slot: icon, avatar, action
□ Text properties named for the content: title, description, label
□ Frames have meaningful names (not auto-generated)
□ Hidden layers removed (not just hidden — deleted or moved to archive)
□ Annotations added for non-obvious behaviors
□ Responsive variants provided for all target breakpoints
□ All interactive states designed (default, hover, active, focus,
  disabled, loading, error, empty)

After Dev Mode setup:

□ Mark sections as "Ready for dev" in Figma
□ Verify Dev Mode output matches intent (check CSS output for
  accuracy, especially for complex Auto Layout)
□ Add developer annotations for anything Dev Mode cannot express
  (animation, gesture, conditional logic)
□ Link to related documentation in the Dev Mode panel
□ Verify that component links resolve correctly in Dev Mode
```

### Figma-to-Code Mapping Guide

```
FIGMA-TO-CODE MAPPING
═══════════════════════════════════════════════════════════════

Auto Layout → CSS:
┌──────────────────────────┬──────────────────────────────────┐
│ Figma Property           │ CSS Equivalent                   │
├──────────────────────────┼──────────────────────────────────┤
│ Horizontal Auto Layout   │ display: flex; flex-direction: row│
│ Vertical Auto Layout     │ display: flex; flex-direction: column│
│ Gap                      │ gap: [value]                     │
│ Padding (all sides)      │ padding: [value]                 │
│ Padding (individual)     │ padding-top/right/bottom/left    │
│ Fill container           │ flex: 1 (or width: 100%)         │
│ Hug contents             │ width: auto (or fit-content)     │
│ Fixed width              │ width: [value]px                 │
│ Space between            │ justify-content: space-between   │
│ Align: Center            │ align-items: center              │
│ Wrap                     │ flex-wrap: wrap                  │
│ Absolute position        │ position: absolute               │
│ Clip content             │ overflow: hidden                 │
│ Min/Max width            │ min-width/max-width              │
└──────────────────────────┴──────────────────────────────────┘

Variables → CSS Custom Properties:
┌──────────────────────────┬──────────────────────────────────┐
│ Figma Variable           │ CSS Custom Property              │
├──────────────────────────┼──────────────────────────────────┤
│ color/bg/primary         │ --color-bg-primary               │
│ color/text/primary       │ --color-text-primary             │
│ spacing/4                │ --space-4                        │
│ radius/md                │ --radius-md                      │
│ shadow/md                │ --shadow-md                      │
│ font/body/size           │ --font-body-size                 │
│ font/body/line-height    │ --font-body-line-height          │
└──────────────────────────┴──────────────────────────────────┘

Component Properties → React Props:
┌──────────────────────────┬──────────────────────────────────┐
│ Figma Property           │ React Prop                       │
├──────────────────────────┼──────────────────────────────────┤
│ Variant: "Primary"       │ variant="primary"                │
│ Boolean: showIcon        │ showIcon={true}                  │
│ Text: label              │ label="Button Text"              │
│ Instance swap: icon      │ icon={<IconName />}              │
│ Variant: size "Small"    │ size="small"                     │
└──────────────────────────┴──────────────────────────────────┘

═══════════════════════════════════════════════════════════════
```

---

## 2. Developer Handoff Checklist

A comprehensive checklist for the designer to complete before declaring a design "ready for development."

```
DEVELOPER HANDOFF CHECKLIST
═══════════════════════════════════════════════════════════════

PROJECT: [Name]
FEATURE: [Name]
DESIGNER: [Name]
DATE: [YYYY-MM-DD]

─────────────────────────────────────────────────────────────

STRUCTURE & LAYOUT
□ All screens designed for all target breakpoints
  Breakpoints: □ Mobile (375) □ Tablet (768) □ Desktop (1440)
□ Grid system documented (columns, gutters, margins per breakpoint)
□ Maximum content width specified
□ Scroll behavior specified (sticky headers, parallax, etc.)
□ Page-level layout documented (sidebar vs. full-width, etc.)

COMPONENTS
□ All components exist in the design system / component library
□ New components documented with props, variants, and states
□ Component naming matches (or is mapped to) code component names
□ All component states designed:
  □ Default     □ Hover      □ Active/Pressed
  □ Focus       □ Disabled   □ Loading
  □ Error       □ Success    □ Empty
□ Edge cases handled:
  □ Long text (truncation rules specified)
  □ Missing images (placeholder specified)
  □ Missing data (empty state designed)
  □ Single item vs. many items
  □ Maximum content (1000+ items, overflow behavior)

DESIGN TOKENS
□ All visual values reference tokens (no hard-coded values)
□ Token names are finalized and match the token file
□ Color tokens cover light, dark, and high-contrast modes
□ Spacing tokens applied consistently
□ Typography tokens applied consistently
□ Elevation tokens applied where needed
□ Border radius tokens applied consistently

INTERACTIONS
□ Click/tap behaviors specified for all interactive elements
□ Hover states designed (desktop)
□ Focus states designed (keyboard navigation)
□ Transition animations specified (property, duration, easing)
□ Loading behaviors specified:
  □ Initial load (skeleton / spinner / progressive)
  □ Action load (button loading state)
  □ Data refresh (pull-to-refresh, background update)
□ Error behaviors specified:
  □ Form validation (inline, on-submit, real-time)
  □ Network errors (retry, fallback)
  □ Permission errors (access denied)
  □ Not found errors (404 page)
□ Navigation behaviors:
  □ Page transitions (if applicable)
  □ Back button behavior
  □ Deep link support
  □ Browser history management

CONTENT
□ Real content used in designs (not lorem ipsum for key screens)
□ Content length variations tested (short, medium, long)
□ Dynamic content rules specified (truncation, formatting)
□ Date/time format specified
□ Number format specified (thousands separator, decimals)
□ Currency format specified
□ Pluralization rules specified ("1 item" vs. "2 items")

ACCESSIBILITY
□ Focus order documented (tab sequence through the page)
□ Heading hierarchy specified (h1, h2, h3, etc.)
□ ARIA roles specified for custom components
□ ARIA labels specified for icon-only buttons and inputs
□ Alt text provided for all meaningful images
□ Decorative images marked as decorative (alt="")
□ Color contrast verified:
  □ Normal text: 4.5:1 minimum
  □ Large text: 3:1 minimum
  □ UI components: 3:1 minimum
  □ Focus indicator: 3:1 minimum
□ Touch target size verified: 44x44px minimum (mobile)
□ Screen reader announcements specified for dynamic content:
  □ Form errors
  □ Toast notifications
  □ Loading state changes
  □ Content updates (live regions)
□ Reduced motion alternative specified for animations
□ Content readable at 200% zoom

ASSETS
□ Icons exported as SVG (optimized, viewBox preserved)
□ Images exported at 1x and 2x (or 3x for mobile)
□ Image format specified (WebP with PNG/JPG fallback)
□ Image dimensions and aspect ratios documented
□ Favicon and app icons provided (all required sizes)
□ Open Graph images provided (if applicable)

DOCUMENTATION
□ Figma file organized and pages named clearly
□ Screen-level annotations completed
□ Interaction specification written for complex behaviors
□ Design decision records updated for new decisions
□ Edge case documentation complete
□ Known limitations or compromises documented

HANDOFF MEETING
□ Walkthrough meeting scheduled with development team
□ Figma file shared with developer access
□ Design tokens file shared / accessible
□ Questions channel established (Slack channel, etc.)
□ Design QA process agreed (who reviews, when, how)

═══════════════════════════════════════════════════════════════
```

---

## 3. Design Token Export Guide

```
DESIGN TOKEN EXPORT GUIDE
═══════════════════════════════════════════════════════════════

TOKEN ARCHITECTURE OVERVIEW

Figma Variables → Tokens Studio → JSON → Style Dictionary → Platform Code

Layer 1: Primitive Tokens (raw values)
──────────────────────────────────────
{
  "color": {
    "blue": {
      "50":  { "value": "#eff6ff" },
      "100": { "value": "#dbeafe" },
      "200": { "value": "#bfdbfe" },
      "300": { "value": "#93c5fd" },
      "400": { "value": "#60a5fa" },
      "500": { "value": "#3b82f6" },
      "600": { "value": "#2563eb" },
      "700": { "value": "#1d4ed8" },
      "800": { "value": "#1e40af" },
      "900": { "value": "#1e3a8a" },
      "950": { "value": "#172554" }
    }
  },
  "spacing": {
    "0":  { "value": "0" },
    "1":  { "value": "4px" },
    "2":  { "value": "8px" },
    "3":  { "value": "12px" },
    "4":  { "value": "16px" },
    "6":  { "value": "24px" },
    "8":  { "value": "32px" },
    "10": { "value": "40px" },
    "12": { "value": "48px" },
    "16": { "value": "64px" }
  }
}

Layer 2: Semantic Tokens (contextual meaning, mode-aware)
─────────────────────────────────────────────────────────
{
  "color": {
    "bg": {
      "primary": {
        "value": "{color.white}",
        "$dark": "{color.neutral.900}"
      },
      "secondary": {
        "value": "{color.neutral.50}",
        "$dark": "{color.neutral.800}"
      },
      "accent": {
        "value": "{color.blue.50}",
        "$dark": "{color.blue.950}"
      }
    },
    "text": {
      "primary": {
        "value": "{color.neutral.900}",
        "$dark": "{color.neutral.50}"
      },
      "secondary": {
        "value": "{color.neutral.600}",
        "$dark": "{color.neutral.400}"
      }
    },
    "action": {
      "primary": {
        "value": "{color.blue.600}",
        "$dark": "{color.blue.400}"
      },
      "primary-hover": {
        "value": "{color.blue.700}",
        "$dark": "{color.blue.300}"
      }
    }
  }
}

Layer 3: Component Tokens (component-specific)
──────────────────────────────────────────────
{
  "button": {
    "primary": {
      "bg": { "value": "{color.action.primary}" },
      "bg-hover": { "value": "{color.action.primary-hover}" },
      "text": { "value": "{color.text.on-action}" },
      "border-radius": { "value": "{radius.md}" },
      "padding-x": { "value": "{spacing.4}" },
      "padding-y": { "value": "{spacing.2}" }
    }
  }
}

EXPORT FORMATS
──────────────

CSS Custom Properties:
:root {
  --color-bg-primary: #ffffff;
  --color-text-primary: #0f172a;
  --color-action-primary: #2563eb;
  --space-4: 16px;
  --radius-md: 8px;
}

[data-theme="dark"] {
  --color-bg-primary: #0f172a;
  --color-text-primary: #f8fafc;
  --color-action-primary: #60a5fa;
}

Tailwind Configuration:
module.exports = {
  theme: {
    colors: {
      bg: {
        primary: 'var(--color-bg-primary)',
        secondary: 'var(--color-bg-secondary)',
      },
      text: {
        primary: 'var(--color-text-primary)',
        secondary: 'var(--color-text-secondary)',
      }
    }
  }
}

iOS Swift:
extension Color {
  static let bgPrimary = Color("bgPrimary")
  static let textPrimary = Color("textPrimary")
  static let actionPrimary = Color("actionPrimary")
}

Android Kotlin:
object AppColors {
  val bgPrimary = Color(0xFFFFFFFF)
  val textPrimary = Color(0xFF0F172A)
  val actionPrimary = Color(0xFF2563EB)
}

VALIDATION CHECKLIST
────────────────────
□ Token names are consistent across Figma and code
□ All semantic tokens resolve correctly in light mode
□ All semantic tokens resolve correctly in dark mode
□ All semantic tokens resolve correctly in high-contrast mode
□ No orphaned tokens (tokens defined but not used)
□ No missing tokens (values used but not tokenized)
□ Token values are accurate to Figma (spot-check 10+ values)
□ Platform-specific transforms applied correctly (px → pt for iOS)

═══════════════════════════════════════════════════════════════
```

---

## 4. Asset Export Specifications

```
ASSET EXPORT SPECIFICATIONS
═══════════════════════════════════════════════════════════════

ICONS
─────
Format: SVG (optimized)
Optimization: Run through SVGO (remove metadata, optimize paths)
ViewBox: Preserve viewBox attribute (do not use width/height on SVG)
Size: Design at 24x24 grid, export with viewBox="0 0 24 24"
Color: Use currentColor for fill/stroke (allows CSS color inheritance)
Naming: icon-[name].svg (kebab-case, descriptive)
Organization: /assets/icons/[category]/icon-[name].svg

Icon Export Checklist:
□ viewBox preserved
□ No embedded styles (use attributes)
□ Paths optimized (minimal points)
□ currentColor used for fill/stroke
□ No transforms (flatten before export)
□ No clip-paths unless absolutely necessary
□ No embedded raster images
□ File size under 2KB per icon (ideally under 1KB)

IMAGES (Raster)
───────────────
Format Priority: WebP (primary), PNG (transparency fallback),
                 JPEG (photo fallback)
Density: Export at 1x and 2x (3x for mobile-critical images)
Quality: WebP 80-85%, JPEG 80-85%, PNG lossless
Max Dimensions:
  - Hero images: 2880px wide (covers 1440px @2x)
  - Content images: 1600px wide max
  - Thumbnails: 800px wide max
  - Avatars: 400px (covers 200px @2x)
Naming: [context]-[description]-[size].[ext]
        e.g., hero-dashboard-overview-2880w.webp
Organization: /assets/images/[feature]/[name]

Image Export Checklist:
□ Exported at correct dimensions and density
□ WebP version created with quality 80-85%
□ Fallback format created (PNG for transparency, JPEG for photos)
□ File size optimized (use ImageOptim, Squoosh, or equivalent)
□ Alt text documented in the handoff spec
□ Lazy loading specified for below-the-fold images
□ Aspect ratio documented (for responsive containers)
□ Placeholder strategy specified (LQIP, blur-up, dominant color)

ILLUSTRATIONS
─────────────
Format: SVG (for simple/flat) or optimized PNG/WebP (for complex)
SVG: Same rules as icons but may be larger and more complex
Raster: Export at 2x minimum, 3x for mobile-critical
Animation: Export as Lottie JSON (from After Effects via Bodymovin)
           or define in CSS/JS (for simple transitions)
Naming: illus-[context]-[description].[ext]
Organization: /assets/illustrations/[category]/

FAVICONS AND APP ICONS
──────────────────────
favicon.ico:     16x16, 32x32 (multi-resolution ICO)
favicon.svg:     SVG (preferred for modern browsers)
apple-touch:     180x180 PNG
android-chrome:  192x192, 512x512 PNG
og-image:        1200x630 PNG (Open Graph for social sharing)
manifest icons:  48, 72, 96, 144, 168, 192, 256, 512 PNG

═══════════════════════════════════════════════════════════════
```

---

## 5. Responsive Behavior Documentation

```
RESPONSIVE BEHAVIOR DOCUMENTATION — [Screen/Feature Name]
═══════════════════════════════════════════════════════════════

BREAKPOINT DEFINITIONS
┌──────────────┬────────────┬─────────┬──────────┬──────────┐
│ Name         │ Range      │ Columns │ Gutter   │ Margin   │
├──────────────┼────────────┼─────────┼──────────┼──────────┤
│ Mobile S     │ 320-374    │ 4       │ 16px     │ 16px     │
│ Mobile       │ 375-767    │ 4       │ 16px     │ 16px     │
│ Tablet       │ 768-1023   │ 8       │ 24px     │ 32px     │
│ Desktop      │ 1024-1439  │ 12      │ 24px     │ 48px     │
│ Wide         │ 1440+      │ 12      │ 24px     │ auto     │
└──────────────┴────────────┴─────────┴──────────┴──────────┘
Max content width: 1440px (centered on wide screens)

LAYOUT BEHAVIOR BY BREAKPOINT
──────────────────────────────

Component: [Navigation]
┌──────────────┬──────────────────────────────────────────────┐
│ Breakpoint   │ Behavior                                     │
├──────────────┼──────────────────────────────────────────────┤
│ Mobile       │ Bottom tab bar (5 items max), hamburger for  │
│              │ overflow. Fixed to bottom of viewport.        │
│ Tablet       │ Collapsed sidebar (icons only, 64px width).  │
│              │ Expand on hover/click to full width (240px).  │
│ Desktop      │ Persistent sidebar (240px), always expanded.  │
│ Wide         │ Same as desktop.                              │
└──────────────┴──────────────────────────────────────────────┘

Component: [Content Grid]
┌──────────────┬──────────────────────────────────────────────┐
│ Breakpoint   │ Behavior                                     │
├──────────────┼──────────────────────────────────────────────┤
│ Mobile       │ Single column, full-width cards. Stack        │
│              │ vertically with 16px gap.                     │
│ Tablet       │ 2-column grid. Cards span 4 columns each.    │
│              │ 24px gap.                                     │
│ Desktop      │ 3-column grid. Cards span 4 columns each.    │
│              │ 24px gap.                                     │
│ Wide         │ 4-column grid. Cards span 3 columns each.    │
│              │ 24px gap.                                     │
└──────────────┴──────────────────────────────────────────────┘

Component: [Hero Section]
┌──────────────┬──────────────────────────────────────────────┐
│ Breakpoint   │ Behavior                                     │
├──────────────┼──────────────────────────────────────────────┤
│ Mobile       │ Image above text, full-width. Image height:  │
│              │ 200px (cover, center crop). Text below.       │
│ Tablet       │ Side-by-side. Image: 50%, Text: 50%.         │
│              │ Image height: auto (match text column).       │
│ Desktop      │ Side-by-side. Image: 55%, Text: 45%.         │
│              │ Max height: 480px.                            │
│ Wide         │ Same as desktop, centered in max-width.       │
└──────────────┴──────────────────────────────────────────────┘

HIDE/SHOW RULES
────────────────
┌──────────────────────────┬─────┬──────┬───────┬──────┬─────┐
│ Element                  │ MoS │ Mo   │ Tab   │ Desk │ Wide│
├──────────────────────────┼─────┼──────┼───────┼──────┼─────┤
│ Desktop navigation       │ ✗   │ ✗    │ ✓     │ ✓    │ ✓   │
│ Mobile tab bar           │ ✓   │ ✓    │ ✗     │ ✗    │ ✗   │
│ Sidebar filters          │ ✗   │ ✗    │ ✗     │ ✓    │ ✓   │
│ Filter bottom sheet      │ ✓   │ ✓    │ ✓     │ ✗    │ ✗   │
│ Secondary description    │ ✗   │ ✗    │ ✓     │ ✓    │ ✓   │
│ Compact metric cards     │ ✓   │ ✓    │ ✗     │ ✗    │ ✗   │
│ Expanded metric cards    │ ✗   │ ✗    │ ✓     │ ✓    │ ✓   │
└──────────────────────────┴─────┴──────┴───────┴──────┴─────┘

TYPOGRAPHY SCALING
──────────────────
┌──────────────────┬────────┬────────┬────────┬────────┐
│ Token            │ Mobile │ Tablet │ Desktop│ Wide   │
├──────────────────┼────────┼────────┼────────┼────────┤
│ Display Large    │ 32/40  │ 40/48  │ 48/56  │ 56/64  │
│ Display Medium   │ 28/36  │ 32/40  │ 36/44  │ 36/44  │
│ Heading 1        │ 24/32  │ 28/36  │ 28/36  │ 28/36  │
│ Body             │ 16/24  │ 16/24  │ 16/24  │ 16/24  │
│ Body Small       │ 14/20  │ 14/20  │ 14/20  │ 14/20  │
└──────────────────┴────────┴────────┴────────┴────────┘
(Format: size/line-height in px)

═══════════════════════════════════════════════════════════════
```

---

## 6. Animation Specification Format

```
ANIMATION SPECIFICATION — [Feature/Component Name]
═══════════════════════════════════════════════════════════════

ANIMATION INVENTORY
───────────────────
┌────┬────────────────────┬────────────┬──────────┬──────────┐
│ #  │ Animation          │ Trigger    │ Duration │ Priority │
├────┼────────────────────┼────────────┼──────────┼──────────┤
│ A1 │ Page transition    │ Navigation │ 300ms    │ Required │
│ A2 │ Modal enter        │ Button click│ 200ms   │ Required │
│ A3 │ Modal exit         │ Close/ESC  │ 150ms    │ Required │
│ A4 │ List item enter    │ Data load  │ 200ms    │ Nice-to-have│
│ A5 │ Button feedback    │ Click      │ 100ms    │ Required │
│ A6 │ Skeleton shimmer   │ Loading    │ 1500ms   │ Required │
│ A7 │ Toast enter        │ Event      │ 300ms    │ Required │
│ A8 │ Toast exit         │ Timer/dismiss│ 200ms  │ Required │
└────┴────────────────────┴────────────┴──────────┴──────────┘

DETAILED SPECIFICATIONS

A1: Page Transition
─────────────────
Trigger: Route change (navigation)
Enter:
  - New page: opacity 0→1, translateY 8px→0
  - Duration: 300ms
  - Easing: cubic-bezier(0.16, 1, 0.3, 1) (ease-out-expo)
  - Delay: 50ms (allow exit to begin first)
Exit:
  - Current page: opacity 1→0
  - Duration: 150ms
  - Easing: ease-in
Reduced motion alternative:
  - Simple crossfade, 150ms, no transform

A2: Modal Enter
──────────────
Trigger: Modal open action
Overlay:
  - opacity: 0→0.5
  - background: var(--color-overlay)
  - Duration: 200ms
  - Easing: ease-out
Content:
  - opacity: 0→1
  - scale: 0.95→1.0
  - Duration: 200ms
  - Easing: cubic-bezier(0.16, 1, 0.3, 1)
Focus: Move to first focusable element in modal after animation
Reduced motion: Instant appear (opacity only, 100ms)

A5: Button Feedback
──────────────────
Trigger: Click/tap on button
Active state:
  - scale: 1.0→0.97
  - Duration: 100ms
  - Easing: ease-in
Release:
  - scale: 0.97→1.0
  - Duration: 200ms
  - Easing: cubic-bezier(0.16, 1, 0.3, 1) (spring-like)
Reduced motion: Background color change only, no transform

MOTION DESIGN TOKENS
────────────────────
┌──────────────────────────┬────────────────────────────────┐
│ Token                    │ Value                          │
├──────────────────────────┼────────────────────────────────┤
│ duration-instant         │ 100ms                          │
│ duration-fast            │ 150ms                          │
│ duration-normal          │ 200ms                          │
│ duration-slow            │ 300ms                          │
│ duration-slower          │ 500ms                          │
│ easing-default           │ cubic-bezier(0.4, 0, 0.2, 1)  │
│ easing-in                │ cubic-bezier(0.4, 0, 1, 1)    │
│ easing-out               │ cubic-bezier(0, 0, 0.2, 1)    │
│ easing-spring            │ cubic-bezier(0.16, 1, 0.3, 1) │
│ easing-bounce            │ cubic-bezier(0.34, 1.56, 0.64, 1)│
└──────────────────────────┴────────────────────────────────┘

REDUCED MOTION POLICY
─────────────────────
When prefers-reduced-motion: reduce is active:
- Remove all transform-based animations (scale, translate, rotate)
- Replace with opacity-only transitions (150ms max)
- Disable infinite animations (shimmer, pulse, spin)
- Keep essential state changes (color, visibility) instantaneous
- Never remove information conveyed solely through animation
  (provide static alternative)

═══════════════════════════════════════════════════════════════
```

---

## 7. Accessibility Requirements Documentation

```
ACCESSIBILITY SPECIFICATION — [Feature/Screen Name]
═══════════════════════════════════════════════════════════════

TARGET CONFORMANCE: WCAG 2.2 Level AA

─────────────────────────────────────────────────────────────

1. FOCUS ORDER
   [Document the sequential focus order through the page]

   Focus Sequence:
   1. Skip to main content link (visually hidden until focused)
   2. Logo (link to home)
   3. Navigation items (left to right)
   4. Search input
   5. Page title (if heading is focusable / linked)
   6. Filter controls (if present)
   7. Content items (grid / list, left-right then top-bottom)
   8. Pagination controls
   9. Footer links

   Focus Traps:
   - Modal dialogs: Focus trapped within modal while open
   - Dropdown menus: Focus returns to trigger on close
   - Drawers: Focus trapped within drawer while open

   Focus Restoration:
   - When closing an overlay, return focus to the element that
     triggered it
   - When deleting an item, move focus to the next item (or
     previous if last item was deleted)

2. HEADING HIERARCHY
   h1: [Page title — one per page]
   h2: [Section titles]
   h3: [Subsection titles within each h2]
   h4: [If needed, within h3 sections]

   Rules:
   - No skipped levels (no h1 → h3)
   - One h1 per page
   - Headings are semantic, not just visual styling

3. ARIA SPECIFICATIONS
   ┌──────────────────────┬────────────────────────────────────┐
   │ Component            │ ARIA Requirements                  │
   ├──────────────────────┼────────────────────────────────────┤
   │ Navigation           │ <nav aria-label="Main navigation"> │
   │ Search               │ role="search" or <form role="search">│
   │ Breadcrumbs          │ <nav aria-label="Breadcrumb">      │
   │ Modal                │ role="dialog" aria-modal="true"     │
   │                      │ aria-labelledby="[title id]"       │
   │ Toast                │ role="status" aria-live="polite"   │
   │ Error toast          │ role="alert" aria-live="assertive" │
   │ Loading spinner      │ role="status" aria-label="Loading" │
   │ Tab set              │ role="tablist" / role="tab" /      │
   │                      │ role="tabpanel"                    │
   │ Accordion            │ aria-expanded="true/false"         │
   │ Sort button          │ aria-sort="ascending/descending/none"│
   │ Required field       │ aria-required="true"               │
   │ Invalid field        │ aria-invalid="true"                │
   │                      │ aria-describedby="[error id]"      │
   │ Icon-only button     │ aria-label="[action description]"  │
   │ Badge / count        │ aria-label="[X] notifications"     │
   │ Progress bar         │ role="progressbar" aria-valuenow   │
   │                      │ aria-valuemin aria-valuemax        │
   └──────────────────────┴────────────────────────────────────┘

4. KEYBOARD INTERACTION
   ┌──────────────────────┬────────────────────────────────────┐
   │ Component            │ Keyboard Behavior                  │
   ├──────────────────────┼────────────────────────────────────┤
   │ Button               │ Enter/Space: activate              │
   │ Link                 │ Enter: navigate                    │
   │ Checkbox             │ Space: toggle                      │
   │ Radio group          │ Arrow keys: move between options   │
   │ Select/Dropdown      │ Enter/Space: open                  │
   │                      │ Arrows: navigate options           │
   │                      │ Enter: select option               │
   │                      │ Escape: close without selecting    │
   │ Tab set              │ Arrows: switch tabs                │
   │                      │ Tab: move to tab panel content     │
   │ Modal                │ Escape: close                      │
   │                      │ Tab: cycle within modal            │
   │ Menu                 │ Arrows: navigate items             │
   │                      │ Enter: activate item               │
   │                      │ Escape: close menu                 │
   │ Data table           │ Arrows: navigate cells             │
   │ Slider               │ Arrows: adjust value               │
   │                      │ Home/End: min/max values           │
   └──────────────────────┴────────────────────────────────────┘

5. COLOR CONTRAST VERIFICATION
   ┌──────────────────────┬──────────┬──────────┬──────────────┐
   │ Element              │ FG Color │ BG Color │ Ratio        │
   ├──────────────────────┼──────────┼──────────┼──────────────┤
   │ Body text            │ #0f172a  │ #ffffff  │ 15.4:1 ✓     │
   │ Secondary text       │ #475569  │ #ffffff  │ 6.2:1 ✓      │
   │ Link text            │ #2563eb  │ #ffffff  │ 4.6:1 ✓      │
   │ Button text          │ #ffffff  │ #2563eb  │ 4.6:1 ✓      │
   │ Placeholder text     │ #94a3b8  │ #ffffff  │ 3.0:1 ✗ (fix)│
   │ Error text           │ #dc2626  │ #ffffff  │ 4.5:1 ✓      │
   │ Focus ring           │ #2563eb  │ #ffffff  │ 4.6:1 ✓      │
   │ Disabled text        │ #cbd5e1  │ #ffffff  │ 1.9:1 (exempt)│
   └──────────────────────┴──────────┴──────────┴──────────────┘

6. SCREEN READER ANNOUNCEMENTS
   ┌──────────────────────┬────────────────────────────────────┐
   │ Event                │ Announcement                       │
   ├──────────────────────┼────────────────────────────────────┤
   │ Page load            │ "[Page title] loaded"              │
   │ Form submitted       │ "Form submitted successfully"      │
   │ Form error           │ "[X] errors found. First error:    │
   │                      │  [field name], [error message]"    │
   │ Item added to cart   │ "[Item name] added to cart.        │
   │                      │  Cart total: [X] items."           │
   │ Item deleted         │ "[Item name] removed."             │
   │ Content loading      │ "Loading content"                  │
   │ Content loaded       │ "[X] results loaded"               │
   │ Sort applied         │ "Sorted by [column], [direction]"  │
   │ Filter applied       │ "[X] results for [filter criteria]"│
   │ Toast notification   │ "[Toast message text]"             │
   └──────────────────────┴────────────────────────────────────┘

═══════════════════════════════════════════════════════════════
```

---

## 8. QA Checklist for Design Handoff

```
DESIGN QA CHECKLIST — [Feature/Screen Name]
═══════════════════════════════════════════════════════════════

Reviewer: [Name]
Date: [YYYY-MM-DD]
Build/Branch: [Reference]
Compared Against: [Figma frame link]

─────────────────────────────────────────────────────────────

VISUAL ACCURACY
□ Colors match design tokens (not eyeballed — compare hex values)
□ Typography matches type scale (size, weight, line-height, color)
□ Spacing matches design tokens (margins, padding, gaps)
□ Border radius matches design tokens
□ Shadows/elevation matches design tokens
□ Icons are correct (right icon, right size, right color)
□ Images are correct resolution (not blurry on retina)
□ Layout matches grid specification (columns, gutters, margins)
□ Alignment is precise (no off-by-1px misalignment)

RESPONSIVE BEHAVIOR
□ Mobile layout matches Figma mobile frame
□ Tablet layout matches Figma tablet frame
□ Desktop layout matches Figma desktop frame
□ Breakpoint transitions are smooth (no layout jumps)
□ Text reflows correctly at all widths
□ Images resize correctly (no distortion, correct cropping)
□ Touch targets are 44x44px minimum on mobile
□ No horizontal scroll at any breakpoint

INTERACTION STATES
□ Default state matches design
□ Hover state matches design (desktop)
□ Active/pressed state matches design
□ Focus state matches design (visible focus ring)
□ Disabled state matches design
□ Loading state matches design
□ Error state matches design
□ Empty state matches design
□ Success state matches design

FUNCTIONALITY
□ All interactive elements are clickable/tappable
□ Form validation works as specified
□ Error messages display correctly
□ Loading states appear and resolve
□ Navigation works correctly
□ Back button behavior is correct
□ Scroll behavior is correct (sticky headers, scroll restoration)
□ Animations match specification (timing, easing, properties)

CONTENT
□ Real content displays correctly (not just test data)
□ Long content handled correctly (truncation, wrapping, overflow)
□ Short content handled correctly (no awkward gaps)
□ Missing content handled correctly (placeholders, empty states)
□ Date/time formats are correct
□ Number formats are correct (commas, decimals, currency)

ACCESSIBILITY
□ Keyboard navigation works through all interactive elements
□ Focus order is logical
□ Focus is visible on all interactive elements
□ Screen reader announces content correctly
□ ARIA attributes are present and correct
□ Color contrast passes (4.5:1 text, 3:1 UI components)
□ Reduced motion preference respected
□ Images have alt text

CROSS-BROWSER/DEVICE (spot check)
□ Chrome (latest)
□ Safari (latest)
□ Firefox (latest)
□ iOS Safari (latest)
□ Android Chrome (latest)

ISSUES FOUND
┌────┬────────┬────────────────────┬──────────┬──────────────┐
│ #  │ Severity│ Description        │ Location │ Screenshot   │
├────┼────────┼────────────────────┼──────────┼──────────────┤
│ 1  │ [H/M/L]│ [Description]      │ [Screen] │ [Link/Ref]   │
│ 2  │ [H/M/L]│ [Description]      │ [Screen] │ [Link/Ref]   │
└────┴────────┴────────────────────┴──────────┴──────────────┘

RESULT: □ Approved  □ Approved with minor issues  □ Revisions needed

═══════════════════════════════════════════════════════════════
```

---

## 9. Post-Launch Monitoring Setup Guide

```
POST-LAUNCH MONITORING — [Feature/Product Name]
═══════════════════════════════════════════════════════════════

Launch Date: [YYYY-MM-DD]
Monitoring Period: [X] weeks post-launch

─────────────────────────────────────────────────────────────

1. METRICS TO TRACK
   ┌──────────────────────┬────────────┬────────────┬─────────┐
   │ Metric               │ Baseline   │ Target     │ Tool    │
   ├──────────────────────┼────────────┼────────────┼─────────┤
   │ Task success rate    │ [X]%       │ [X]%       │ [Tool]  │
   │ Time on task         │ [X] sec    │ [X] sec    │ [Tool]  │
   │ Error rate           │ [X]%       │ [X]%       │ [Tool]  │
   │ Conversion rate      │ [X]%       │ [X]%       │ [Tool]  │
   │ Support tickets      │ [X]/week   │ [X]/week   │ [Tool]  │
   │ Page load time       │ [X] sec    │ < [X] sec  │ [Tool]  │
   │ Core Web Vitals      │ [Values]   │ [Targets]  │ CrUX    │
   │ User satisfaction    │ [Score]    │ [Target]   │ Survey  │
   └──────────────────────┴────────────┴────────────┴─────────┘

2. MONITORING SCHEDULE
   Day 1-3:   Daily check — critical bugs, error rates, page load
   Week 1:    Daily metric review — funnel conversion, task success
   Week 2-3:  Bi-weekly review — trend analysis, early patterns
   Week 4:    Full post-launch review — comprehensive analysis
   Month 2-3: Monthly check-in — sustained impact verification

3. ALERT THRESHOLDS
   - Error rate exceeds [X]%: Investigate immediately
   - Conversion rate drops more than [X]% vs. baseline: Alert team
   - Page load time exceeds [X] seconds: Performance investigation
   - Support ticket volume increases [X]% vs. baseline: UX review
   - Core Web Vital regression: Engineering + design review

4. FEEDBACK COLLECTION
   - In-app feedback widget (optional, for specific flows)
   - Post-task survey (triggered after key user actions)
   - Support ticket categorization (tag design-related issues)
   - Session recording review ([X] sessions per week for [X] weeks)
   - User interview recruitment (from active users post-launch)

5. POST-LAUNCH REPORT TEMPLATE
   ┌────────────────────────────────────────────────────────┐
   │ POST-LAUNCH REPORT — [Feature Name]                   │
   │ Period: [Launch Date] — [Report Date]                  │
   │                                                        │
   │ Executive Summary:                                     │
   │ [2-3 sentences: Overall performance vs. expectations]  │
   │                                                        │
   │ Key Metrics:                                           │
   │ [Table comparing baseline, target, actual]             │
   │                                                        │
   │ Issues Identified:                                     │
   │ [List with severity and status]                        │
   │                                                        │
   │ User Feedback Themes:                                  │
   │ [Top 3-5 themes from feedback data]                    │
   │                                                        │
   │ Recommendations:                                       │
   │ [Prioritized list of improvements for next iteration]  │
   │                                                        │
   │ Next Steps:                                            │
   │ [Specific actions with owners and deadlines]           │
   └────────────────────────────────────────────────────────┘

6. ITERATION TRIGGER CRITERIA
   When to iterate:
   - Metric misses target by more than [X]%
   - Recurring user feedback pattern (3+ reports of same issue)
   - New competitive pressure requiring response
   - Technical constraint discovered post-launch
   - Accessibility issue identified in production

   When NOT to iterate immediately:
   - Single user complaint (monitor for pattern first)
   - Stakeholder preference change (validate with data first)
   - Feature request that was out of scope (add to backlog)
   - Metrics within acceptable range of target

═══════════════════════════════════════════════════════════════
```
