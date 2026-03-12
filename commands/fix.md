---
description: "Anti-slop engine — takes AI-generated UI code and transforms it into production-quality design. Fixes typography, color, spacing, accessibility, and design consistency in one pass."
tier: "make"
---

# Fix — Anti-Slop Engine

The antidote to AI-generated UI. Takes code that *works* but *looks like a robot made it* and transforms it into production-quality design in a single pass. Detects the telltale signs of LLM-generated UI — the purple gradients, the arbitrary spacing, the missing states, the generic font stacks — and systematically replaces every slop pattern with a principled design decision.

This command does not redesign. It does not change your architecture, your business logic, or your component structure. It fixes the **design layer only** — typography, color, spacing, layout, states, accessibility, and code quality — while preserving everything else.

**Accepts**: Pasted code, file paths, or "fix this file/component/screen."

---

## Input Protocol

### Step 0 — Detect Input

**Accept any of these input formats:**

| Input Type | Example | How to Handle |
|-----------|---------|---------------|
| Pasted code | Raw JSX/HTML/CSS/SwiftUI in the message | Parse directly |
| File path | `src/components/Dashboard.tsx` | Read the file |
| Vague request | "fix this component" | Ask which file or request paste |
| Multiple files | `src/app/page.tsx` + `src/components/Card.tsx` | Process all, maintain cross-file consistency |
| Screenshot description | "the hero section looks off" | Ask for the code behind it |

**Auto-detect framework:**

| Framework | Detection Signals |
|-----------|------------------|
| React + Tailwind | `className=`, Tailwind utility classes (`bg-`, `text-`, `flex`, `p-`, `rounded-`) |
| React + CSS Modules | `styles.` or `import styles from`, `.module.css` |
| React + styled-components | `styled.div`, `css\`\`` |
| Vue | `<template>`, `<script setup>`, `:class`, `v-bind` |
| Svelte | `<script>`, `{#if}`, `{#each}`, `class:` directives |
| Vanilla HTML/CSS | `<html>`, `<style>`, no framework markers |
| SwiftUI | `struct ... View`, `VStack`, `HStack`, `.modifier()` |
| Next.js / App Router | `'use client'`, `export default function Page()`, `app/` path |

**Check for design memory:**

1. Look for `.sumi/style.json` in the project root
2. If found: load all tokens and use them as the source of truth — do NOT generate new tokens
3. If not found: check for `tailwind.config.js/ts` custom theme extensions
4. If neither: generate a minimal token set as part of the fix (Step 4)

---

## Slop Detection Protocol

### Step 1 — Slop Detection Scan

Run a systematic scan across 7 dimensions. For each dimension, check every item. Mark each finding with severity:

- **CRITICAL**: Breaks usability or accessibility. Must fix before shipping.
- **MAJOR**: Degrades perceived quality. Users notice, even if subconsciously.
- **MINOR**: Polish issue. Separates good from great.

---

#### 1.1 Typography Slop

| # | Pattern | What to Look For | Severity | Why It Matters |
|---|---------|-----------------|----------|---------------|
| T1 | Generic font stack | Just `font-sans` or `"Inter"` with no fallback strategy, no type scale | Major | Typography is 95% of web design (Oliver Reichenstein). Generic stacks signal zero design intentionality |
| T2 | Missing fluid typography | No `clamp()` values; fixed `text-sm`, `text-lg` only | Major | Fixed sizes break at viewport extremes. Fluid type scales gracefully from 320px to 2560px (WCAG 1.4.4 Resize Text) |
| T3 | No type scale hierarchy | h1-h6 sizes feel arbitrary — e.g., h1 is 36px, h2 is 24px, h3 is 20px with no ratio | Major | Without a modular ratio (1.2, 1.25, 1.333), the type hierarchy lacks visual logic. Users cannot parse information priority (NNG: Aesthetic-Usability Effect) |
| T4 | Inconsistent font weights | Random mixing of 400/500/600/700 with no pattern | Minor | Weight should have semantic meaning: 400=body, 500=emphasis, 600=subheading, 700=heading. Random weights create visual noise |
| T5 | Missing letter-spacing | Same letter-spacing at all sizes, or none set at all | Minor | Large text needs negative tracking (-0.01em to -0.03em); small text needs positive tracking (+0.01em to +0.02em). This is optical compensation, not preference |
| T6 | Wrong line heights | All text at `leading-normal` (1.5) regardless of size | Minor | Headings need tighter line-height (1.1-1.25); body needs 1.5; captions need 1.5-1.6. Uniform line-height wastes space on headings and cramps captions |
| T7 | No responsive sizing | Same text sizes across all breakpoints | Major | Mobile body at 16px is correct; desktop body at 16px is undersized. Fluid scaling is required for readability across devices |
| T8 | Too many font families | 3+ different fonts loaded | Minor | Each additional font family adds 20-100KB of load and fractures visual consistency. Maximum 2 families (heading + body), or 1 versatile family |
| T9 | Paragraph width unconstrained | Prose text stretches to full container width, no `max-w-prose` or `ch` limit | Major | Lines longer than 75 characters cause reading fatigue. Optimal: 55-75 characters (Robert Bringhurst, The Elements of Typographic Style) |

---

#### 1.2 Color Slop

| # | Pattern | What to Look For | Severity | Why It Matters |
|---|---------|-----------------|----------|---------------|
| C1 | The Purple Gradient | `bg-gradient-to-r from-indigo-500 to-purple-600` or any indigo/violet hero gradient on white | Major | This is the #1 tell of AI-generated UI. It appears in >60% of LLM outputs. It signals "a machine made this" to any designer who sees it |
| C2 | Default Tailwind palette | Using `blue-500`, `gray-100`, `red-500` straight from Tailwind defaults with zero customization | Major | Tailwind's defaults are intentionally generic. Every serious product customizes its palette. Default colors = default product |
| C3 | No semantic tokens | `bg-blue-500` for primary, `bg-red-500` for error instead of `bg-primary`, `bg-error` | Major | Raw color values create maintenance nightmares and break dark mode. Semantic tokens decouple meaning from value (Design Systems Architecture: token layers) |
| C4 | Missing dark mode | No `dark:` prefixes, no `prefers-color-scheme` media query, no theme variables | Major | 82% of smartphone users use dark mode (Android data, 2024). Missing dark mode is a feature gap, not a polish issue |
| C5 | Failing contrast ratios | Light gray text on white, or colored text on colored backgrounds without verification | Critical | WCAG 2.2 SC 1.4.3 requires 4.5:1 for normal text, 3:1 for large text and UI components. Failing contrast = inaccessible = potentially illegal |
| C6 | No color system | Random hex values scattered through code (`#3B82F6` here, `#2563EB` there, `#1D4ED8` elsewhere) | Major | A color system means a neutral scale (10 steps), a brand scale (10 steps), and semantic colors. Scattered hex values = no system |
| C7 | Semantic confusion | Same color used for success AND links, or red used for non-destructive actions | Major | Color carries meaning (NNG Heuristic 4: Consistency). When red means both "error" and "important," users cannot trust color as a signal |
| C8 | Too many accent colors | 4+ distinct bright hues competing on the same screen | Minor | The 60-30-10 rule: 60% neutral, 30% secondary, 10% accent. More than 2-3 accent hues creates visual chaos (Josef Albers, Interaction of Color) |
| C9 | Pure black text | `text-black` or `#000000` for body text | Minor | Pure black on pure white creates maximum contrast (21:1) which causes eye strain on screens. Optimal body text: `gray-900` / `neutral-900` at ~15:1 contrast |

---

#### 1.3 Spacing Slop

| # | Pattern | What to Look For | Severity | Why It Matters |
|---|---------|-----------------|----------|---------------|
| S1 | Inconsistent spacing | `p-2` next to `p-5` next to `p-3` with no logic connecting them | Major | Spacing should follow a scale (4, 8, 12, 16, 24, 32, 48, 64). Arbitrary values destroy visual rhythm (Gestalt: Proximity) |
| S2 | No spacing scale | Values like `p-[13px]`, `mt-[7px]`, `gap-[11px]` — custom values that follow no grid | Major | The 4px base grid is industry standard. Every spacing value should be a multiple of 4 (or 8 for looser systems). Off-grid values create subpixel rendering issues |
| S3 | Cramped layouts | Insufficient padding inside components; text touching borders | Major | Minimum padding: 8px for compact elements, 12-16px for standard components, 24px for cards/sections. Cramped = amateur (NNG: Aesthetic-Usability Effect) |
| S4 | No responsive spacing | Same `p-4` at 320px mobile and 1440px desktop | Minor | Spacing should scale with viewport. Mobile needs tighter spacing (small screens); desktop needs more breathing room |
| S5 | Gap inconsistency | Different gap values for similar patterns — `gap-2` for one card grid, `gap-4` for another | Minor | Same pattern = same gap. Card grids should use one gap value consistently. List items should use one gap value consistently |
| S6 | Missing section rhythm | No vertical spacing pattern between page sections | Major | Sections need consistent vertical rhythm — typically 48-96px between major sections. Random section spacing makes the page feel unstructured |
| S7 | Padding ratio wrong on buttons | Button padding like `px-2 py-2` (square) or `px-8 py-1` (extreme rectangle) | Minor | Button padding ratio should be ~2.5-3:1 (horizontal:vertical). Example: `px-4 py-2` or `px-6 py-2.5`. This follows Fitts's Law for comfortable targets |

---

#### 1.4 Layout Slop

| # | Pattern | What to Look For | Severity | Why It Matters |
|---|---------|-----------------|----------|---------------|
| L1 | Everything is a 3-column grid | All content sections use `grid-cols-3` regardless of content type | Major | AI defaults to 3 columns. Real design uses hierarchy: 1-column for focus, 2-column for comparison, 3-column for browsing, 4-column for dashboards |
| L2 | No visual hierarchy | All sections have equal visual weight — same size headings, same card sizes, same spacing | Critical | Without hierarchy, users cannot prioritize information. The most important content must be visually dominant (Von Restorff Effect, Gestalt: Figure-Ground) |
| L3 | Missing section spacing rhythm | Sections crammed together or randomly spaced | Major | Vertical rhythm should follow a pattern: section padding (64-96px), subsection gap (32-48px), element gap (16-24px). Consistent rhythm creates perceived quality |
| L4 | No responsive breakpoint strategy | Either no responsive classes or haphazard `md:` / `lg:` usage | Major | Mobile-first means: stack on mobile (1 col), expand on tablet (2 col), full layout on desktop (3-4 col). Every layout needs a breakpoint plan |
| L5 | Hardcoded widths | `w-[400px]`, `w-96`, `max-w-[1200px]` instead of semantic container classes | Minor | Use `max-w-screen-sm/md/lg/xl/2xl` or `container` with `mx-auto`. Hardcoded widths break at unexpected viewport sizes |
| L6 | No max-width on content | Prose or card sections that stretch to full viewport width on ultrawide monitors | Major | Content sections need `max-w-7xl` or similar. Prose needs `max-w-prose` (65ch). Unbounded width destroys readability on wide screens |
| L7 | Centered everything | Every section is `text-center` with centered content regardless of content type | Minor | Center alignment works for heroes and CTAs. Body text, lists, and forms should be left-aligned (for LTR languages). Center alignment reduces reading speed by 10% for body text |

---

#### 1.5 Component Slop

| # | Pattern | What to Look For | Severity | Why It Matters |
|---|---------|-----------------|----------|---------------|
| K1 | Missing interactive states | Buttons/links with no hover, focus, or active states | Critical | Interactive elements without state feedback violate NNG Heuristic 1 (Visibility of System Status). Users cannot tell if something is clickable or if their click registered |
| K2 | No focus-visible outlines | Missing `focus:` or `focus-visible:` ring on interactive elements | Critical | WCAG 2.2 SC 2.4.7 (Focus Visible) requires visible focus indicator. Missing = keyboard users cannot navigate. This is an accessibility violation |
| K3 | No loading states | No skeleton, spinner, or loading indicator anywhere in the code | Major | Any action >300ms needs a loading state (Doherty Threshold). Missing loading states make the app feel broken during async operations |
| K4 | No empty states | No handling for zero-data scenarios — just blank space or missing content | Major | Empty states are the first thing new users see. "No data" is a missed opportunity; "Get started by..." is onboarding (NNG: Help and Documentation) |
| K5 | No error states | No error handling, no error messages, no error boundaries | Critical | When things fail (and they will), users need clear, helpful error messages with recovery paths (NNG Heuristic 9: Help Users Recover from Errors) |
| K6 | No transition/animation | State changes are instant — no fade, no slide, no easing | Minor | Transitions communicate state change (cognitive continuity). 150-300ms transitions on interactive elements are expected. Their absence feels abrupt |
| K7 | Button padding wrong | Buttons with uneven or insufficient padding, or text touching the border | Minor | Buttons need minimum 44x44px touch target (WCAG 2.5.8). Padding ratio should be ~2.5:1 horizontal:vertical. `px-4 py-2` minimum for md size |
| K8 | Card elevation chaos | Cards with inconsistent `shadow-sm`, `shadow-md`, `shadow-lg` for items at the same level | Minor | Elevation = hierarchy. Cards at the same level should share the same shadow. Only elevated (modals, popovers) or interactive (hover lift) elements should differ |
| K9 | Inconsistent border-radius | `rounded-md` on one card, `rounded-lg` on another, `rounded-xl` on a button | Minor | Pick a default radius for the product and use it everywhere. Cards, buttons, inputs, modals — all should use the same base radius (or deliberate scale: sm, md, lg) |
| K10 | No disabled state | Interactive elements have no disabled variant — no `opacity`, no `cursor-not-allowed`, no `pointer-events-none` | Major | Disabled state prevents invalid actions and communicates unavailability. Missing disabled state = users try to interact with non-functional elements |

---

#### 1.6 Accessibility Slop

| # | Pattern | What to Look For | Severity | Why It Matters |
|---|---------|-----------------|----------|---------------|
| A1 | Images without alt text | `<img>` with no `alt` attribute or `alt=""` on meaningful images | Critical | WCAG 2.2 SC 1.1.1 (Non-text Content). Screen readers announce images without alt as the file path. Every meaningful image needs descriptive alt text |
| A2 | Buttons/links with no accessible name | `<button><Icon /></button>` with no `aria-label`, no visible text, no `sr-only` label | Critical | WCAG 2.2 SC 4.1.2 (Name, Role, Value). Screen readers announce "button" with no context. Every interactive element needs a perceivable name |
| A3 | Missing ARIA on dynamic content | Modals, dropdowns, toasts without `role`, `aria-expanded`, `aria-live` | Major | Dynamic content changes are invisible to screen readers without ARIA announcements. Modal without `role="dialog"` and `aria-modal="true"` = inaccessible |
| A4 | No skip-to-content link | No skip navigation link for keyboard users | Minor | WCAG 2.2 SC 2.4.1 (Bypass Blocks). Keyboard users must Tab through the entire nav on every page without a skip link |
| A5 | Color as only indicator | Status shown only by color (green=active, red=inactive) with no icon or text | Critical | WCAG 2.2 SC 1.4.1 (Use of Color). 8% of males have color vision deficiency. Color must never be the sole indicator of meaning |
| A6 | No focus management | Modal opens but focus stays behind it; route changes but focus stays at bottom of page | Major | WCAG 2.2 SC 2.4.3 (Focus Order). Focus must move to new content when it appears (modals, route changes) and return when it closes |
| A7 | Missing keyboard navigation | Interactive elements only respond to click/tap, not Enter/Space/Arrow keys | Critical | WCAG 2.2 SC 2.1.1 (Keyboard). All functionality must be operable via keyboard. Many users cannot use a mouse |
| A8 | Form inputs without labels | `<input placeholder="Email">` with no `<label>` element | Critical | WCAG 2.2 SC 1.3.1 (Info and Relationships). Placeholder disappears on focus. Screen readers need `<label>` associated via `htmlFor`/`id` |
| A9 | Missing lang attribute | `<html>` without `lang="en"` (or appropriate language) | Minor | WCAG 2.2 SC 3.1.1 (Language of Page). Screen readers use this to select the correct pronunciation engine |
| A10 | Touch targets too small | Buttons, links, or interactive elements smaller than 44x44px | Major | WCAG 2.2 SC 2.5.8 (Target Size Minimum) requires 24x24px minimum; 44x44px is the recommended target. Small targets cause mis-taps |

---

#### 1.7 Code Quality Slop

| # | Pattern | What to Look For | Severity | Why It Matters |
|---|---------|-----------------|----------|---------------|
| Q1 | Inline styles mixed with utilities | `style={{color: 'red'}}` alongside Tailwind classes | Minor | Pick one styling method. Mixing inline and utility classes creates specificity conflicts and maintenance burden |
| Q2 | Hardcoded strings | `color: '#3B82F6'` instead of CSS variables or Tailwind theme values | Major | Hardcoded values cannot be themed, cannot be dark-moded, and create duplication. Every color, spacing, and font value should reference a token |
| Q3 | Inconsistent naming | `UserCard` next to `profile_header` next to `mainCTA` — camelCase/snake_case/PascalCase mixed | Minor | Consistent naming conventions signal professional code. Components: PascalCase. Props/variables: camelCase. CSS classes: kebab-case or utility |
| Q4 | Duplicated style patterns | Same Tailwind class string repeated 5+ times across components | Minor | Extract into a CVA variant, a component, or a `@apply` directive. Duplication = divergence over time |
| Q5 | Missing responsive utilities | No `sm:`, `md:`, `lg:` breakpoint prefixes anywhere in the code | Major | If there are no responsive utilities, the layout is either accidentally responsive (flexbox/grid default behavior) or broken on mobile |
| Q6 | div with onClick | `<div onClick={...}>` instead of `<button>` for clickable elements | Critical | `<div>` is not keyboard focusable, has no implicit role, and does not respond to Enter/Space. Use `<button>` for actions and `<a>` for navigation |
| Q7 | Missing key props | List renders without `key` prop, or using array index as key | Minor | React needs stable keys for efficient reconciliation. Missing or index-based keys cause rendering bugs and performance issues |
| Q8 | Unused imports / dead code | Imported components or variables that are not used | Minor | Dead code increases bundle size and cognitive load. Clean imports signal maintained code |

---

## Fix Protocol

### Step 2 — Generate Fix Report

After running the slop scan, output a structured report. Group by category, sort by severity (Critical first).

**Report Format:**

```
### Slop Report

**Scan Summary**: [X] issues found — [N] critical, [N] major, [N] minor

| # | ID | Category | Severity | Issue | Location | Principle |
|---|----|----------|----------|-------|----------|-----------|
| 1 | A2 | Accessibility | Critical | Icon button has no accessible name | Line 45: `<button><SearchIcon /></button>` | WCAG 2.2 SC 4.1.2 |
| 2 | C5 | Color | Critical | Gray-400 text on white bg fails AA contrast | Line 12: `text-gray-400` on white | WCAG 2.2 SC 1.4.3 (requires 4.5:1) |
| 3 | K1 | Component | Critical | Primary button has no hover or focus state | Line 67: `<button className="bg-blue-500">` | NNG H1: Visibility of System Status |
| ... | | | | | | |
```

For each issue, provide:
1. **ID**: The detection code from Step 1 (e.g., T1, C3, S1, K2, A1, Q6)
2. **Category**: Typography / Color / Spacing / Layout / Component / Accessibility / Code
3. **Severity**: Critical / Major / Minor
4. **Issue**: What is wrong, specifically
5. **Location**: Exact line or element in the code
6. **Principle**: WCAG guideline, NNG heuristic, cognitive principle, or design rule that justifies the fix

---

### Step 3 — Transform the Code

Output the **COMPLETE** transformed file with ALL fixes applied. Not diffs, not patches — the full corrected code, ready to copy-paste and replace the original file.

**Transformation rules by category:**

#### 3.1 Typography Transforms

```
BEFORE (slop):
  <h1 className="text-3xl font-bold">
  <p className="text-base">

AFTER (fixed):
  <h1 className="text-3xl md:text-4xl lg:text-5xl font-bold tracking-tight leading-tight">
  {/* Type scale: 1.25 ratio, fluid sizing, tightened tracking for display text */}
  <p className="text-base md:text-lg leading-relaxed max-w-prose">
  {/* Body: 1.5+ line-height, constrained to 65ch for readability */}
```

Apply these transforms:
- Add fluid responsive sizing (`text-base md:text-lg lg:text-xl` or `clamp()` values)
- Add proper `tracking-` (letter-spacing) per size: tight for headings, normal for body, wide for caps
- Add proper `leading-` (line-height) per context: tight for headings, relaxed for body
- Constrain prose width with `max-w-prose` or equivalent
- Standardize weight usage: 400 body, 500 emphasis, 600 subheadings, 700 headings

#### 3.2 Color Transforms

```
BEFORE (slop):
  <div className="bg-gradient-to-r from-indigo-500 to-purple-600">
  <p className="text-gray-400">
  <button className="bg-blue-500">

AFTER (fixed):
  <div className="bg-primary-600 dark:bg-primary-500">
  {/* Solid brand color with dark mode variant — no AI-gradient cliche */}
  <p className="text-neutral-600 dark:text-neutral-400">
  {/* neutral-600 on white = 7.0:1 contrast ratio (WCAG AAA) */}
  <button className="bg-primary-600 hover:bg-primary-700 dark:bg-primary-500 dark:hover:bg-primary-400">
  {/* Semantic token with hover state and dark mode */}
```

Apply these transforms:
- Replace generic Tailwind colors with semantic custom theme colors
- Remove the purple/indigo gradient pattern — replace with solid brand colors or subtle, intentional gradients
- Fix contrast violations — minimum 4.5:1 for text, 3:1 for UI components
- Add `dark:` variants for every color usage
- Replace `text-black` with `text-neutral-900` (softer, less strain)
- Add CSS custom properties if no token system exists (see Step 4)

#### 3.3 Spacing Transforms

```
BEFORE (slop):
  <div className="p-2">
    <div className="mt-3 mb-5 p-4">
      <div className="gap-[11px] p-[13px]">

AFTER (fixed):
  <div className="p-4 md:p-6">
    {/* 16px mobile, 24px desktop — consistent with 4px grid */}
    <div className="mt-4 mb-6 p-4 md:p-6">
    {/* Spacing follows 4px scale: 4, 8, 12, 16, 24, 32 */}
      <div className="gap-3 p-4">
      {/* gap-3 (12px) and p-4 (16px) — on the 4px grid */}
```

Apply these transforms:
- Snap all spacing to the 4px grid (Tailwind: 1=4px, 2=8px, 3=12px, 4=16px, 6=24px, 8=32px)
- Remove arbitrary `[Npx]` values — round to nearest grid value
- Add responsive spacing (`p-4 md:p-6 lg:p-8`)
- Fix button padding ratios to ~2.5:1 horizontal:vertical
- Establish section rhythm: 16-24px between elements, 32-48px between groups, 64-96px between sections

#### 3.4 Layout Transforms

```
BEFORE (slop):
  <div className="grid grid-cols-3 gap-4">
    {items.map(item => <Card key={item.id} item={item} />)}
  </div>

AFTER (fixed):
  <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
    {/* Responsive: 1 col mobile → 2 col tablet → 3 col desktop */}
    {items.map(item => <Card key={item.id} item={item} />)}
  </div>
```

Apply these transforms:
- Add responsive column counts (`grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`)
- Wrap content sections in `max-w-7xl mx-auto px-4 md:px-6 lg:px-8`
- Add section spacing rhythm with consistent `py-16 md:py-24` between major sections
- Fix visual hierarchy — primary content should be larger/bolder than secondary
- Replace hardcoded widths with semantic max-width classes

#### 3.5 Component State Transforms

For every interactive element, add missing states:

```
BEFORE (slop):
  <button className="bg-blue-500 text-white rounded px-4 py-2">
    Save
  </button>

AFTER (fixed):
  <button
    className="
      bg-primary-600 text-white rounded-md px-4 py-2
      font-medium text-sm
      hover:bg-primary-700
      focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary-500 focus-visible:ring-offset-2
      active:scale-[0.98]
      disabled:opacity-50 disabled:cursor-not-allowed disabled:pointer-events-none
      transition-all duration-150 ease-out
      motion-reduce:transition-none motion-reduce:active:scale-100
      dark:bg-primary-500 dark:hover:bg-primary-400
      dark:focus-visible:ring-offset-neutral-900
    "
    {/* States: hover (color shift), focus-visible (ring), active (scale), disabled (dimmed) */}
    {/* Motion: 150ms transition, reduced-motion safe */}
    {/* A11y: focus ring with offset, keyboard accessible via native <button> */}
  >
    Save
  </button>
```

**Minimum state coverage per element type:**

| Element | Required States |
|---------|----------------|
| Button | hover, focus-visible, active, disabled, loading (if async) |
| Link | hover, focus-visible, visited (if applicable) |
| Input | hover, focus, disabled, error, placeholder, filled |
| Card | hover (if clickable), focus-visible (if clickable) |
| Checkbox/Toggle | checked, unchecked, hover, focus-visible, disabled |
| Select/Dropdown | open, closed, hover, focus-visible, disabled |

**Add loading skeleton if none exists:**

```typescript
// Loading skeleton for any async content
function ComponentSkeleton() {
  return (
    <div className="animate-pulse space-y-4" role="status" aria-label="Loading">
      <div className="h-4 bg-neutral-200 dark:bg-neutral-700 rounded w-3/4" />
      <div className="h-4 bg-neutral-200 dark:bg-neutral-700 rounded w-1/2" />
      <div className="h-10 bg-neutral-200 dark:bg-neutral-700 rounded" />
      <span className="sr-only">Loading...</span>
    </div>
  );
}
```

**Add empty state if none exists:**

```typescript
// Empty state for any list/grid/table
function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center py-12 px-4 text-center">
      <div className="w-12 h-12 rounded-full bg-neutral-100 dark:bg-neutral-800 flex items-center justify-center mb-4">
        {/* Icon placeholder */}
      </div>
      <h3 className="text-base font-medium text-neutral-900 dark:text-neutral-100 mb-1">
        {title}
      </h3>
      <p className="text-sm text-neutral-500 dark:text-neutral-400 max-w-sm mb-4">
        {description}
      </p>
      {action && (
        <button className="text-sm font-medium text-primary-600 hover:text-primary-700 dark:text-primary-400">
          {action.label}
        </button>
      )}
    </div>
  );
}
```

**Add error state if none exists:**

```typescript
// Error state for any async content
function ErrorState({ message, onRetry }: ErrorStateProps) {
  return (
    <div className="flex flex-col items-center justify-center py-12 px-4 text-center" role="alert">
      <div className="w-12 h-12 rounded-full bg-error-50 dark:bg-error-900/20 flex items-center justify-center mb-4">
        {/* Error icon */}
      </div>
      <h3 className="text-base font-medium text-neutral-900 dark:text-neutral-100 mb-1">
        Something went wrong
      </h3>
      <p className="text-sm text-neutral-500 dark:text-neutral-400 max-w-sm mb-4">
        {message || "We couldn't load this content. Please try again."}
      </p>
      {onRetry && (
        <button
          onClick={onRetry}
          className="text-sm font-medium text-primary-600 hover:text-primary-700 dark:text-primary-400"
        >
          Try again
        </button>
      )}
    </div>
  );
}
```

#### 3.6 Accessibility Transforms

Apply these transforms to every element:

```
BEFORE (slop):
  <div onClick={handleClick}>Click me</div>
  <img src="/hero.jpg">
  <button><SearchIcon /></button>
  <input placeholder="Enter email">

AFTER (fixed):
  <button onClick={handleClick}>Click me</button>
  {/* Semantic HTML: <button> is keyboard accessible and has implicit role */}

  <img src="/hero.jpg" alt="Team collaborating in a modern office space" />
  {/* WCAG 1.1.1: Descriptive alt text for meaningful images */}

  <button aria-label="Search">
    <SearchIcon aria-hidden="true" />
  </button>
  {/* WCAG 4.1.2: Icon buttons need aria-label; icon is decorative */}

  <div>
    <label htmlFor="email" className="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-1">
      Email address
    </label>
    <input
      id="email"
      type="email"
      placeholder="you@example.com"
      aria-describedby="email-hint"
      className="..."
    />
    <p id="email-hint" className="mt-1 text-xs text-neutral-500">
      We'll never share your email.
    </p>
  </div>
  {/* WCAG 1.3.1: Label associated via htmlFor/id; hint via aria-describedby */}
```

**Accessibility transforms checklist:**
- Replace every `<div onClick>` with `<button>` or `<a href>`
- Add `alt` text to all `<img>` elements (or `alt=""` + `aria-hidden="true"` for decorative)
- Add `aria-label` to all icon-only buttons
- Add `<label>` to all form inputs, linked via `htmlFor`/`id`
- Add `focus-visible:ring-2 focus-visible:ring-offset-2` to all interactive elements
- Add `role="alert"` to error messages
- Add `role="status"` and `aria-live="polite"` to dynamic content
- Add `aria-expanded`, `aria-haspopup` to disclosure triggers
- Add `lang` attribute to `<html>` if missing

#### 3.7 Code Quality Transforms

- Replace `style={{}}` props with Tailwind utilities or CSS custom properties
- Replace hardcoded color strings with theme tokens
- Extract repeated class strings into CVA variants or component abstractions
- Fix naming inconsistencies (enforce PascalCase for components, camelCase for props)
- Replace `<div onClick>` with semantic elements
- Add missing `key` props on list renders
- Remove unused imports

---

### Step 4 — Generate Token File (If None Exists)

If no `.sumi/style.json` exists and no design tokens are detected in the project (no `tailwind.config.js` custom theme, no CSS custom properties), generate a minimal token set.

**Output as CSS custom properties at the top of the fixed file (or as a separate token block):**

```css
/* =================================================================
   Design Tokens — Generated by Sumi /fix
   Move to your global CSS file or tailwind.config.js
   ================================================================= */

:root {
  /* --- Color: Primary --- */
  --color-primary-50:  oklch(0.97 0.01 250);
  --color-primary-100: oklch(0.93 0.03 250);
  --color-primary-200: oklch(0.86 0.06 250);
  --color-primary-300: oklch(0.75 0.10 250);
  --color-primary-400: oklch(0.65 0.14 250);
  --color-primary-500: oklch(0.55 0.17 250);  /* Hero value */
  --color-primary-600: oklch(0.47 0.16 250);  /* Default button bg */
  --color-primary-700: oklch(0.40 0.14 250);
  --color-primary-800: oklch(0.33 0.11 250);
  --color-primary-900: oklch(0.27 0.08 250);

  /* --- Color: Neutral --- */
  --color-neutral-50:  oklch(0.985 0.002 250);
  --color-neutral-100: oklch(0.965 0.002 250);
  --color-neutral-200: oklch(0.925 0.002 250);
  --color-neutral-300: oklch(0.87  0.002 250);
  --color-neutral-400: oklch(0.71  0.002 250);
  --color-neutral-500: oklch(0.55  0.002 250);
  --color-neutral-600: oklch(0.445 0.002 250);
  --color-neutral-700: oklch(0.37  0.002 250);
  --color-neutral-800: oklch(0.27  0.002 250);
  --color-neutral-900: oklch(0.205 0.002 250);

  /* --- Color: Semantic --- */
  --color-success: oklch(0.55 0.15 145);
  --color-warning: oklch(0.70 0.15 85);
  --color-error:   oklch(0.55 0.20 27);
  --color-info:    oklch(0.55 0.12 250);

  /* --- Color: Surface (Light) --- */
  --color-bg:          var(--color-neutral-50);
  --color-bg-raised:   white;
  --color-bg-overlay:  var(--color-neutral-100);
  --color-text:        var(--color-neutral-900);
  --color-text-muted:  var(--color-neutral-600);
  --color-text-faint:  var(--color-neutral-500);
  --color-border:      var(--color-neutral-200);

  /* --- Typography --- */
  --font-sans:  'Inter', ui-sans-serif, system-ui, -apple-system, sans-serif;
  --font-mono:  'JetBrains Mono', ui-monospace, monospace;

  --text-xs:    clamp(0.625rem,  0.6rem  + 0.1vw,  0.75rem);
  --text-sm:    clamp(0.75rem,   0.72rem + 0.15vw, 0.875rem);
  --text-base:  clamp(0.875rem,  0.85rem + 0.2vw,  1rem);
  --text-lg:    clamp(1rem,      0.95rem + 0.3vw,  1.25rem);
  --text-xl:    clamp(1.25rem,   1.15rem + 0.45vw, 1.5rem);
  --text-2xl:   clamp(1.5rem,    1.35rem + 0.6vw,  1.875rem);
  --text-3xl:   clamp(1.875rem,  1.65rem + 0.8vw,  2.25rem);
  --text-4xl:   clamp(2.25rem,   1.95rem + 1vw,    3rem);

  /* --- Spacing (4px grid) --- */
  --space-1:  0.25rem;   /* 4px */
  --space-2:  0.5rem;    /* 8px */
  --space-3:  0.75rem;   /* 12px */
  --space-4:  1rem;      /* 16px */
  --space-6:  1.5rem;    /* 24px */
  --space-8:  2rem;      /* 32px */
  --space-12: 3rem;      /* 48px */
  --space-16: 4rem;      /* 64px */
  --space-24: 6rem;      /* 96px */

  /* --- Border Radius --- */
  --radius-sm:   0.25rem;  /* 4px */
  --radius-md:   0.5rem;   /* 8px */
  --radius-lg:   0.75rem;  /* 12px */
  --radius-xl:   1rem;     /* 16px */
  --radius-full: 9999px;

  /* --- Shadow --- */
  --shadow-sm: 0 1px 2px 0 oklch(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px oklch(0 0 0 / 0.07), 0 2px 4px -2px oklch(0 0 0 / 0.07);
  --shadow-lg: 0 10px 15px -3px oklch(0 0 0 / 0.08), 0 4px 6px -4px oklch(0 0 0 / 0.08);

  /* --- Motion --- */
  --duration-fast:   150ms;
  --duration-normal: 250ms;
  --duration-slow:   400ms;
  --ease-out:  cubic-bezier(0.0, 0.0, 0.2, 1.0);
  --ease-in:   cubic-bezier(0.4, 0.0, 1.0, 1.0);
  --ease-move: cubic-bezier(0.4, 0.0, 0.2, 1.0);
}

/* --- Dark Mode --- */
[data-theme="dark"],
.dark,
:root:is(.dark) {
  --color-bg:          var(--color-neutral-900);
  --color-bg-raised:   var(--color-neutral-800);
  --color-bg-overlay:  var(--color-neutral-700);
  --color-text:        oklch(0.93 0.002 250);
  --color-text-muted:  var(--color-neutral-400);
  --color-text-faint:  var(--color-neutral-500);
  --color-border:      oklch(1 0 0 / 0.12);

  --shadow-sm: 0 0 0 1px oklch(1 0 0 / 0.06);
  --shadow-md: 0 0 0 1px oklch(1 0 0 / 0.08);
  --shadow-lg: 0 0 0 1px oklch(1 0 0 / 0.10);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast:   0ms;
    --duration-normal: 0ms;
    --duration-slow:   0ms;
  }
}
```

If the input code is React + Tailwind, also output the `tailwind.config.js` `extend` block that maps these tokens to Tailwind utilities.

---

### Step 5 — Before/After Summary

Output a comparison table scoring each dimension 1-10 before and after:

```
### Before/After Summary

| Dimension | Before | After | Delta | Key Changes |
|-----------|--------|-------|-------|-------------|
| Typography | 3/10 | 7/10 | +4 | Added type scale (1.25 ratio), fluid clamp() values, proper tracking/leading |
| Color | 2/10 | 8/10 | +6 | Replaced AI gradient with brand palette, added semantic tokens, dark mode, fixed contrast |
| Spacing | 4/10 | 7/10 | +3 | Snapped all values to 4px grid, added responsive spacing, fixed button padding |
| Layout | 3/10 | 7/10 | +4 | Added responsive breakpoints, max-width containers, section rhythm |
| Components | 2/10 | 7/10 | +5 | Added hover/focus/active/disabled states, loading skeleton, empty state, error state |
| Accessibility | 1/10 | 7/10 | +6 | Fixed contrast, added ARIA, keyboard nav, labels, focus rings, semantic HTML |
| Code Quality | 4/10 | 8/10 | +4 | Extracted tokens, consistent naming, removed div onClick, added responsive utilities |
| **Total** | **19/70** | **51/70** | **+32** | |

**Grade: D (before) → B (after)**
```

Scoring guidance:
- 1-3: Fundamentally broken in this dimension
- 4-5: Below average, noticeable issues
- 6-7: Solid, professional baseline
- 8-9: Excellent, above industry standard
- 10: Exceptional, reference-quality

---

## Framework-Specific Protocols

### React + Tailwind
- Output JSX with Tailwind utility classes
- Use `dark:` prefix for dark mode
- Use `motion-safe:` and `motion-reduce:` for animation
- Use `focus-visible:` (not `focus:`) for keyboard focus
- Include TypeScript types for any new components (skeleton, empty state, error state)
- Use `cn()` utility for conditional class merging if shadcn/ui patterns detected

### Vue
- Output `<template>` + `<script setup>` + `<style scoped>`
- Use `:class` binding for conditional classes
- Use CSS custom properties for theming
- Include TypeScript `defineProps` with defaults

### Svelte
- Output Svelte component syntax
- Use `class:` directives for conditional classes
- Use CSS custom properties in `<style>` block
- Include TypeScript in `<script lang="ts">`

### Vanilla HTML/CSS
- Output semantic HTML5 with CSS custom properties
- Use `@media (prefers-color-scheme: dark)` for dark mode
- Use `@media (prefers-reduced-motion: reduce)` for motion
- Use `:focus-visible` for keyboard focus
- Use modern CSS: `clamp()`, container queries, logical properties, `oklch()`

### SwiftUI
- Use semantic `Color` tokens from asset catalog or extension
- Use `@Environment(\.colorScheme)` for dark mode
- Use `.accessibilityLabel()` for icon-only elements
- Use `.dynamicTypeSize()` for text scaling
- Use `.animation(.default, value:)` with `.transaction` for reduced motion

---

## Quality Gates

The output MUST include:
- [ ] Complete slop report with every issue ID'd, categorized, and severity-rated
- [ ] Principle citation for every non-obvious fix (WCAG guideline, NNG heuristic, or cognitive principle)
- [ ] COMPLETE transformed code — full file, not patches, not diffs
- [ ] All interactive elements have hover, focus-visible, active, and disabled states
- [ ] All text meets WCAG AA contrast (4.5:1 normal, 3:1 large/UI)
- [ ] Dark mode support on every color usage
- [ ] Responsive breakpoints on layout and typography
- [ ] Semantic HTML replacing any `<div onClick>` patterns
- [ ] Token file generated if no design system detected
- [ ] Before/after scoring table with per-dimension breakdown
- [ ] All business logic and functionality preserved exactly — design layer only

The output MUST NOT include:
- Pseudocode or placeholder comments like `/* add styles here */`
- Breaking changes to component APIs, props, or data flow
- New dependencies unless absolutely necessary (prefer Tailwind built-ins over adding libraries)
- Subjective preference changes disguised as fixes — every change must cite a principle
- Generated code that is longer than necessary — fix the slop, do not over-engineer

---

## Output Format

```
## Fix: [Component/File Name]

### Context
- **Framework**: [React + Tailwind | Vue | Svelte | HTML/CSS | SwiftUI]
- **Design Memory**: [.sumi/style.json loaded | tailwind.config.js theme detected | none — tokens generated]
- **Issues Found**: [X] total — [N] critical, [N] major, [N] minor

---

### Slop Report

| # | ID | Category | Severity | Issue | Location | Principle |
|---|----|----------|----------|-------|----------|-----------|
| 1 | ... | ... | Critical | ... | ... | ... |
| ... | | | | | | |

---

### Transformed Code

#### [filename.tsx]
\`\`\`tsx
// COMPLETE fixed code here
// Every fix annotated with a comment explaining WHY
\`\`\`

#### Design Tokens (generated)
\`\`\`css
/* Only if no token system was detected */
:root { ... }
\`\`\`

---

### States Added

| Element | States Added | Code Reference |
|---------|-------------|----------------|
| Primary Button | hover, focus-visible, active, disabled, dark mode | Line N |
| Search Input | focus, error, disabled, placeholder styling | Line N |
| Card Grid | loading skeleton, empty state, responsive columns | Line N |
| ... | | |

---

### Before/After

| Dimension | Before | After | Delta | Key Changes |
|-----------|--------|-------|-------|-------------|
| Typography | X/10 | X/10 | +X | ... |
| Color | X/10 | X/10 | +X | ... |
| Spacing | X/10 | X/10 | +X | ... |
| Layout | X/10 | X/10 | +X | ... |
| Components | X/10 | X/10 | +X | ... |
| Accessibility | X/10 | X/10 | +X | ... |
| Code Quality | X/10 | X/10 | +X | ... |
| **Total** | **X/70** | **X/70** | **+X** | |

**Grade: [Letter] → [Letter]**

---

### Next Steps
- `/roast` — Score the fixed output across 10 dimensions
- `/component` — Rebuild any component from scratch with full state coverage
- `/style` — Generate a complete visual identity if you need a full design system
- `/tokens` — Export the generated tokens to W3C DTCG format
- `/a11y` — Deep accessibility audit beyond the fixes applied here
```

---

## Cross-References

When detecting and fixing slop, draw knowledge from:
- `nng-ux-heuristics` — Heuristic violations for component and interaction fixes
- `accessibility-inclusive-design` — WCAG 2.2 compliance for all accessibility transforms
- `cognitive-psychology-ux` — Fitts's Law (target sizing), Gestalt principles (spacing), Von Restorff (hierarchy)
- `ui-visual-design-system` — Color theory, type scales, visual hierarchy principles
- `visual-design-mastery` — Canonical design rules, visual scoring calibration
- `design-systems-architecture` — Token architecture, naming conventions, semantic layers
- `component-patterns-code` — Production component patterns (React, SwiftUI, CSS)
- `performance-states-patterns` — Loading, error, empty, skeleton state patterns
- `interaction-motion-design` — Animation curves, duration guidelines, reduced motion
- `platform-visual-standards` — iOS 26, Material 3, modern CSS conventions
- `sector-style-intelligence` — Sector-appropriate color, typography, density norms
- `design-token-presets` — Ready-to-deploy token systems as starting points
- `color-palette-library` — OKLCH palette references, APCA scoring
- `typography-pairing-recipes` — Type scale recipes, font stack validation
- `shadow-elevation-density` — Shadow scales, elevation hierarchy
- `form-design-encyclopedia` — Input patterns, label placement, validation strategies

---

## Next Step

**Next** -> `/roast` — Score the fixed output to verify improvement
**Or** -> `/component` — Rebuild a specific component from scratch
**Or** -> `/style` — Generate a complete design system for the project
**Or** -> `/tokens` — Export tokens to W3C DTCG format for design tool integration
