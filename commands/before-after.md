---
name: before-after
description: "Before/after comparison — show exactly how AI-generated slop transforms into production-quality UI. Visual proof of every design improvement."
argument-hint: "[file or component to compare]"
---

# Before / After — Transformation Proof

## Before running

This command needs a file or component to compare.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Visual proof that design discipline transforms AI slop into production cuisine. This command runs `/roast` scoring and `/fix` transformation silently, then presents a structured side-by-side comparison showing exactly what changed, why it changed, and how much the design quality improved.

This is the receipts command. It does not just fix — it proves the fix. Every improvement is quantified, every change is justified, and every before/after pair is shown in code.

**Accepts**: Pasted code, file paths, component/screen references, or "compare this file."

---

## Comparison Protocol

### Step 0 — Accept Input

**Accept any of these input formats:**

| Input Type | Example | How to Handle |
|-----------|---------|---------------|
| Pasted code | Raw JSX/HTML/CSS/SwiftUI in the message | Parse directly as "before" state |
| File path | `src/components/Dashboard.tsx` | Read the file as "before" state |
| Multiple files | `src/app/page.tsx` + `src/components/Card.tsx` | Process each, maintain cross-file consistency |
| Component reference | "the hero section" or "the pricing card" | Ask for code or file path |
| Post-fix comparison | "compare before and after" | Use git history or cached original if available |

**Auto-detect framework:**

| Framework | Detection Signals |
|-----------|------------------|
| React + Tailwind | `className=`, Tailwind utility classes (`bg-`, `text-`, `flex`, `p-`, `rounded-`) |
| React + CSS Modules | `styles.` or `import styles from`, `.module.css` |
| React + styled-components | `styled.div`, `` css`` `` |
| Vue | `<template>`, `<script setup>`, `:class`, `v-bind` |
| Svelte | `<script>`, `{#if}`, `{#each}`, `class:` directives |
| Vanilla HTML/CSS | `<html>`, `<style>`, no framework markers |
| SwiftUI | `struct ... View`, `VStack`, `HStack`, `.modifier()` |
| Next.js / App Router | `'use client'`, `export default function Page()`, `app/` path |

**Check for design memory:**

1. Look for `.sumi/style.json` in the project root
2. If found: load all tokens and use them as the transformation target — do NOT invent new tokens
3. If not found: check for `tailwind.config.js/ts` custom theme extensions
4. If neither: generate a minimal token set as part of the transformation

---

### Step 1 — Analyze Current State (Before)

Run the `/roast` scoring dimensions against the input **silently** — do not output this step. Capture all scores internally for the comparison table.

**Score each of the 10 dimensions (1-10):**

| # | Dimension | Evaluation Focus |
|---|-----------|-----------------|
| 1 | Clarity | Can users understand what to do without instruction? |
| 2 | Hierarchy | Is information prioritized visually and structurally? |
| 3 | Consistency | Does it follow established patterns and conventions? |
| 4 | Spacing | Is whitespace used purposefully? Breathing room appropriate? |
| 5 | Color | Is the palette harmonious, semantic, and accessible? |
| 6 | Typography | Is the type system clear, readable, and hierarchical? |
| 7 | Interaction | Do interactive elements provide clear feedback? |
| 8 | Accessibility | Does it work for users of all abilities? |
| 9 | Innovation | Does it solve problems in novel, valuable ways? |
| 10 | Polish | Is the craft quality and attention to detail high? |

**Run AI Slop Detection silently:**

Scan against all 5 slop categories (23 total flags):
- Purple Gradient Syndrome (4 flags)
- Font Monotony (4 flags)
- Layout Lottery (5 flags)
- Component Copy-Paste (5 flags)
- Accessibility Void (5 flags)

Record the total slop score and per-category breakdown.

**Calculate letter grade from total score** (same scale as `/roast`):
- A (90-100), A- (85-89), B+ (80-84), B (75-79), B- (70-74)
- C+ (65-69), C (60-64), C- (55-59), D (45-54), F (0-44)

**Identify the top 5 most impactful issues** — sorted by (severity * breadth of impact). These become the headline transformation targets.

---

### Step 2 — Generate Transformation (After)

Apply the `/fix` transformation logic **silently** — do not output this step. Produce the complete fixed code internally.

**Transformation passes (apply in order):**

1. **Typography**: Apply type scale, fluid sizing, proper tracking/leading, constrained prose width
2. **Color**: Replace AI-default palette with semantic tokens, fix contrast, add dark mode
3. **Spacing**: Snap to 4px grid, add responsive spacing, fix button padding ratios
4. **Layout**: Add responsive breakpoints, max-width containers, section rhythm
5. **Components**: Add all missing states (hover, focus-visible, active, disabled, loading, error, empty)
6. **Accessibility**: Semantic HTML, ARIA labels, focus rings, form labels, alt text, keyboard nav
7. **Code Quality**: Remove inline styles, extract tokens, fix naming, remove dead code

**Apply design memory if available:**
- `.sumi/style.json` tokens override any generated values
- `tailwind.config.js` custom theme values are preserved and extended
- Existing design system conventions are respected and reinforced

**Re-score the transformed output** across all 10 dimensions and re-run slop detection to produce the "after" scores.

---

### Step 3 — Present Side-by-Side Comparison

This is the main output. Present a structured, scannable comparison that proves every improvement.

**3.1 — Design Quality Scorecard**

Present the 10-dimension before/after table:

```
### Design Quality Score

| Dimension | Before | After | Change |
|-----------|--------|-------|--------|
| Clarity | X/10 | X/10 | +X |
| Hierarchy | X/10 | X/10 | +X |
| Consistency | X/10 | X/10 | +X |
| Spacing | X/10 | X/10 | +X |
| Color | X/10 | X/10 | +X |
| Typography | X/10 | X/10 | +X |
| Interaction | X/10 | X/10 | +X |
| Accessibility | X/10 | X/10 | +X |
| Innovation | X/10 | X/10 | +X |
| Polish | X/10 | X/10 | +X |
| **Total** | **X/100** | **X/100** | **+X** |

**Grade: [Before Letter] -> [After Letter]**
```

**3.2 — AI Slop Scorecard**

Present the slop detection before/after:

```
### AI Slop Score

| Category | Before | After |
|----------|--------|-------|
| Purple Gradient Syndrome | X/4 | X/4 |
| Font Monotony | X/4 | X/4 |
| Layout Lottery | X/5 | X/5 |
| Component Copy-Paste | X/5 | X/5 |
| Accessibility Void | X/5 | X/5 |
| **Total** | **X/23 ([Severity])** | **X/23 ([Severity])** |
```

**3.3 — Category-by-Category Transformation**

For each category where changes were made, show the specific before/after code with explanation. Present EVERY category that had fixes — do not skip any.

**Format for each category:**

```
### [Category Name]

**Before**: [One-line summary of what was wrong]
**After**: [One-line summary of what was fixed]
**Principle**: [UX/design principle that justifies the change]

// BEFORE
[exact code from the original input]

// AFTER
[exact code from the transformation]
```

**Categories to cover (in this order, skip only if no changes were needed):**

#### Typography
Show before/after for: font families, font sizes, type scale, tracking, leading, prose width, responsive sizing, font weight hierarchy.

Typical transformation:
```
// BEFORE
<h1 className="text-2xl font-bold">Dashboard</h1>
<p className="text-sm text-gray-500">Welcome back</p>

// AFTER
<h1 className="text-3xl md:text-4xl font-bold tracking-tight leading-tight">
  Dashboard
</h1>
<p className="text-base text-neutral-600 dark:text-neutral-400 leading-relaxed max-w-prose">
  Welcome back
</p>
```

#### Color
Show before/after for: primary palette, gradients, semantic tokens, contrast fixes, dark mode additions. Call out any instance of the purple gradient syndrome.

Typical transformation:
```
// BEFORE
<div className="bg-gradient-to-r from-indigo-500 to-purple-600">
<button className="bg-blue-500 text-white">

// AFTER
<div className="bg-primary-600 dark:bg-primary-500">
<button className="bg-primary-600 hover:bg-primary-700 dark:bg-primary-500 text-white">
```

#### Spacing
Show before/after for: padding normalization, gap consistency, section rhythm, button padding ratios, responsive spacing.

Typical transformation:
```
// BEFORE
<div className="p-2">
  <div className="mt-3 mb-5 gap-[11px]">

// AFTER
<div className="p-4 md:p-6">
  <div className="mt-4 mb-6 gap-3">
```

#### Layout
Show before/after for: responsive grids, max-width containers, section spacing, visual hierarchy structure.

Typical transformation:
```
// BEFORE
<div className="grid grid-cols-3 gap-4">

// AFTER
<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
```

#### Components
Show before/after for: interactive states (hover, focus, active, disabled), transitions, border-radius consistency, shadow normalization.

Typical transformation:
```
// BEFORE
<button className="bg-blue-500 text-white rounded px-4 py-2">

// AFTER
<button className="
  bg-primary-600 text-white rounded-md px-4 py-2 font-medium text-sm
  hover:bg-primary-700 focus-visible:outline-none focus-visible:ring-2
  focus-visible:ring-primary-500 focus-visible:ring-offset-2
  active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed
  transition-all duration-150 ease-out motion-reduce:transition-none
  dark:bg-primary-500 dark:hover:bg-primary-400
">
```

#### Accessibility
Show before/after for: semantic HTML replacements, ARIA labels, focus management, form labels, alt text, contrast fixes.

Typical transformation:
```
// BEFORE
<div onClick={handleClick}>Click me</div>
<img src="/hero.jpg">
<button><SearchIcon /></button>
<input placeholder="Email">

// AFTER
<button onClick={handleClick}>Click me</button>
<img src="/hero.jpg" alt="Team collaborating in a modern workspace" />
<button aria-label="Search"><SearchIcon aria-hidden="true" /></button>
<label htmlFor="email" className="sr-only">Email</label>
<input id="email" type="email" placeholder="you@example.com" />
```

#### States
Show before/after for any added loading skeletons, empty states, or error states. If these were missing entirely, show the full new component code.

Typical transformation:
```
// BEFORE — no loading state existed

// AFTER
function DashboardSkeleton() {
  return (
    <div className="animate-pulse space-y-4" role="status" aria-label="Loading">
      <div className="h-6 bg-neutral-200 dark:bg-neutral-700 rounded w-1/3" />
      <div className="h-4 bg-neutral-200 dark:bg-neutral-700 rounded w-2/3" />
      <span className="sr-only">Loading...</span>
    </div>
  );
}
```

---

### Step 4 — Full Transformed Code

Output the **COMPLETE** "after" code — the entire file, ready to copy-paste and replace the original. Not diffs, not patches. The full corrected code with every fix applied.

```
### Transformed Code — Ready to Ship

#### [filename.tsx]
```[framework]
// Complete fixed code here
// Each fix annotated with a comment citing the principle
```
```

If design tokens were generated (no `.sumi/style.json` or `tailwind.config.js` custom theme detected), include the token file:

```
#### Design Tokens (generated)
```css
:root {
  /* Tokens generated by Sumi /before-after — move to global CSS */
  ...
}
```
```

---

### Step 5 — Transformation Summary

Output a concise summary for non-designers. This section is designed to be shareable — in a PR description, a README, a Slack message, or a portfolio.

**Format:**

```
### Transformation Summary

**[N] issues fixed** across [N] categories.

| Metric | Before | After |
|--------|--------|-------|
| Design Grade | [Letter] | [Letter] |
| Slop Score | X/23 ([Severity]) | X/23 ([Severity]) |
| WCAG Contrast Violations | [N] | [N] |
| Missing Interactive States | [N] | [N] |
| Accessibility Issues | [N] | [N] |

**What changed in plain English:**
[2-3 sentence summary explaining the improvements in non-technical language.
Focus on what users will experience differently, not what code changed.
Example: "The interface went from looking like every other AI-generated dashboard
to having a distinct visual identity with proper typography, accessible color contrast,
and interactive feedback on every clickable element."]

> **Verdict**: "Transformed from [Before Grade]-grade AI slop to [After Grade] production cuisine in [N] fixes."

*This comparison is shareable — use it in your README, PR description, or portfolio.*
```

---

## Integration with Other Commands

### Post-Fix Comparison

If `/fix` was already run on this code, `/before-after` can reconstruct the comparison:

1. **Git history available**: Use `git diff` or `git show` to retrieve the original pre-fix version
2. **Cached original**: If the original was stored in `.sumi/cache/`, load it as the "before" state
3. **Manual paste**: Ask the user to paste or reference the original code

### Chaining

| Scenario | Recommended Flow |
|----------|-----------------|
| Quick transformation proof | `/before-after` (does everything in one pass) |
| Deep audit first, then fix | `/roast` -> `/fix` -> `/before-after` (compare original to fixed) |
| Multiple components | Run `/before-after` on each, compile into a transformation report |
| Portfolio piece | `/before-after` -> copy the summary section for case study |

### Sharing the Comparison

The output of `/before-after` is structured for reuse:
- **PR descriptions**: Copy the Design Quality Score table and Transformation Summary
- **README badges**: Use the letter grade change as a visual indicator
- **Portfolio case studies**: The category-by-category breakdown shows design thinking
- **Team communication**: The plain-English summary explains value to non-designers
- **Stakeholder reports**: The metrics table quantifies design quality improvement

---

## Output Format

The final output follows this structure — all sections from Steps 3-5 assembled in order:

```
## Before / After — [Component/Screen Name]

### Context
- **Framework**: [detected framework]
- **Design Memory**: [.sumi/style.json loaded | tailwind.config.js theme detected | none — tokens generated]
- **Input**: [file path or "pasted code"]

[Design Quality Score table — Step 3.1]
[AI Slop Score table — Step 3.2]
[What Changed — category-by-category code comparisons — Step 3.3]
[Transformed Code — complete file — Step 4]
[Transformation Summary with verdict — Step 5]

### Next Steps
- `/fix` — Apply the transformation to additional files
- `/roast` — Score the transformed output independently
- `/audit` — Deep comprehensive audit of the "after" state
- `/grade` — Awwwards-calibrated visual quality scoring
- `/a11y` — Accessibility deep-dive on the transformed code
- `/tokens` — Export generated tokens to W3C DTCG format
- `/style` — Generate a complete design system from the token foundation
```

---

## Quality Gates

The output MUST include:
- [ ] Before scores for all 10 dimensions with honest calibration (most AI slop scores 3-5)
- [ ] After scores for all 10 dimensions with honest calibration (most fixes reach 7-8, not 10)
- [ ] AI Slop Detection run on both before and after states
- [ ] Category-by-category code comparison with exact before/after snippets
- [ ] Principle citation for every transformation (WCAG, NNG heuristic, cognitive principle, or design rule)
- [ ] Complete transformed code — full file, ready to copy-paste
- [ ] Token file generated if no design system was detected
- [ ] Plain-English transformation summary for non-designers
- [ ] One-line shareable verdict with grade change and fix count
- [ ] All business logic and functionality preserved — design layer only
- [ ] Scores are internally consistent (after scores reflect the actual fixes applied)

The output MUST NOT include:
- Inflated "after" scores — if a dimension was not addressed, its score should not change
- Before scores lower than reality to exaggerate improvement — be honest in both directions
- Generic transformations not grounded in the actual input code
- Partial code output — the transformed code must be complete and runnable
- Commentary on business logic, architecture, or feature decisions — design layer only
- Changes that break component APIs, props, or data flow

---

## Scoring Calibration

**Before scores (typical AI-generated UI):**
- Most AI slop scores 30-50/100 total (D to C- range)
- Accessibility is usually the lowest (1-3/10) — AI consistently misses ARIA and semantic HTML
- Color scores 3-5/10 — functional but generic, often with the purple gradient
- Interaction scores 2-4/10 — AI rarely generates hover/focus/active states
- Innovation scores 4-6/10 — AI uses known patterns competently but without distinction

**After scores (post-transformation):**
- A well-executed fix typically reaches 65-80/100 (C+ to B range)
- Accessibility should jump to 7-8/10 after semantic HTML and ARIA fixes
- Color should reach 7-9/10 after semantic tokens and contrast fixes
- Interaction should reach 7-8/10 after state coverage
- Innovation rarely changes — fixing slop does not add novelty, it adds quality
- Do NOT score 9-10 on any dimension unless the transformation truly achieves exceptional quality

**Score honestly. The credibility of the comparison depends on accurate before AND after scoring.**

---

## Cross-References

When analyzing and transforming, draw knowledge from:
- `visual-design-mastery` — 10-dimension visual scoring calibration, canonical design rules
- `nng-ux-heuristics` — Heuristic violations for component and interaction evaluation
- `accessibility-inclusive-design` — WCAG 2.2 compliance for accessibility scoring and fixes
- `cognitive-psychology-ux` — Fitts's Law, Gestalt principles, Von Restorff Effect
- `ui-visual-design-system` — Color theory, type scales, visual hierarchy principles
- `design-systems-architecture` — Token architecture, naming conventions, semantic layers
- `component-patterns-code` — Production component patterns for state coverage
- `performance-states-patterns` — Loading, error, empty, skeleton state patterns
- `interaction-motion-design` — Animation curves, duration guidelines, reduced motion
- `platform-visual-standards` — iOS 26, Material 3, modern CSS conventions
- `sector-style-intelligence` — Sector-appropriate expectations for scoring calibration
- `design-token-presets` — Ready-to-deploy token systems as transformation targets
- `color-palette-library` — OKLCH palette references, APCA contrast scoring
- `typography-pairing-recipes` — Type scale recipes, font stack validation
- `shadow-elevation-density` — Shadow scales, elevation hierarchy
- `design-critique-case-studies` — Critique methodology, before/after case study benchmarks

---

## Next Steps

**After** `/before-after`:
- `/fix` — Apply the same transformation to more files
- `/roast` — Independent score of the transformed output
- `/audit` — Comprehensive audit of the "after" state
- `/grade` — Awwwards-calibrated visual quality score
- `/style` — Build a full design system from the generated tokens
