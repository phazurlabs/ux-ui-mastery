---
name: qa
description: "Design QA — verify implementation matches design spec. Token compliance, state coverage, responsive fidelity, accessibility, pixel-level issues."
argument-hint: "[implementation and design spec to compare]"
---

# QA — Design-to-Code Fidelity Verification

## Before running

This command needs an implementation and the design spec to compare it against.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Compare what was designed against what was built. Pixel-level design QA auditing implementation code against design tokens, visual specs, state coverage, responsive behavior, and accessibility requirements. The difference between "shipped" and "polished" lives in this command.

**Accepts**: Implementation code (file paths or pasted) as the primary input. Design spec (Figma, `/style` output, `/tokens` output, or screenshot) as the source of truth. If no spec is provided, audit against best practices and the token system detected in the code.

---

## QA Protocol

### Step 0: Gather Context

1. **Implementation code**: The built artifact to verify
2. **Design spec**: Figma file, `/style` output, `/tokens` output, or screenshot of intended design. This is the source of truth
3. **Platform**: Web (CSS/Tailwind/styled-components), iOS (SwiftUI/UIKit), Android (Compose/XML)
4. **Prior Sumi outputs**: Consume `/tokens` (design tokens), `/style` (visual direction), `/screen` (screen specs), `/component` (component specs) if available

### Step 1: Token Consumption Audit

Compare every value in the implementation against the design token system.

**Colors**:
- Are semantic token values used? (e.g., `--color-primary`, `--color-surface`)
- Flag every hardcoded hex/rgb/hsl value that should reference a token
- Check semantic usage correctness (primary for actions, destructive for delete, surface for backgrounds)
- Verify dark mode tokens if applicable

**Typography**:
- Correct font family from the type scale?
- Font size matches token? (e.g., `--font-size-body` not `14px`)
- Font weight matches spec?
- Line-height matches token?
- Letter-spacing matches token?

**Spacing**:
- Following the spacing scale? (4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px)
- Flag arbitrary values (13px, 7px, 22px) that break the scale
- Padding and margin consistency within similar components

**Border radius**:
- Using token values? (e.g., `--radius-sm`, `--radius-md`, `--radius-lg`)
- Consistent across similar component types

**Shadows/Elevation**:
- Using elevation token values?
- Correct hierarchy (cards < modals < popovers)

**Output**: Table of every hardcoded value with the correct token reference.

### Step 2: Visual Fidelity Check

For each component and screen:

**Layout alignment**:
- Everything on the grid system?
- Consistent alignment (left-aligned elements share the same left edge)
- Proper use of flex/grid (no float hacks or absolute positioning for layout)

**Spacing consistency**:
- Same spacing between similar elements? (all card gaps equal, all section padding equal)
- Vertical rhythm maintained?
- Content density appropriate for platform?

**Typography fidelity**:
- Correct hierarchy applied? (display > heading > subheading > body > caption)
- No skipped heading levels
- Text truncation handled (ellipsis, line-clamp, or wrapping)
- Maximum line length <= 75 characters for readability

**Color fidelity**:
- Correct semantic colors applied? (primary for CTAs, destructive for delete)
- Consistent surface/background colors
- No rogue colors outside the palette

**Icons**:
- Correct size (matches text or touch target requirements)?
- Aligned to text baseline or center?
- Correct color (inherits from text or uses semantic color)?
- Consistent icon set (not mixing Lucide with Material with Font Awesome)

**Images**:
- Correct aspect ratio maintained?
- Proper sizing (not stretched or pixelated)
- Alt text present
- Loading behavior (lazy loading, placeholder/blur-up)

### Step 3: State Coverage Audit

Check every interactive element for required states:

**Buttons**:
- [ ] Default, hover, focus, active, disabled — all implemented?
- [ ] Loading state (spinner or label change during async action)?
- [ ] Icon + text alignment correct in all states?

**Inputs/Forms**:
- [ ] Default, focus, filled, error, disabled, read-only?
- [ ] Validation messages appear on blur or submit?
- [ ] Error styling (border, error text, icon)?
- [ ] Success/valid state indicator?
- [ ] Placeholder text present and appropriate?
- [ ] Required field indicators?

**Cards/List items**:
- [ ] Default, hover, selected/active?
- [ ] Loading skeleton state?
- [ ] Empty state (when no data)?

**Modals/Dialogs**:
- [ ] Open/close transitions?
- [ ] Backdrop/overlay present?
- [ ] Focus trapped inside modal?
- [ ] Close on Escape key?
- [ ] Close on backdrop click?

**Navigation**:
- [ ] Active/current state indicator?
- [ ] Hover states on all links?
- [ ] Mobile menu open/close states?

**Data displays**:
- [ ] Loading state (skeleton or spinner)?
- [ ] Empty state (no data message + CTA)?
- [ ] Error state (failed to load + retry)?
- [ ] Pagination/infinite scroll states?

**Severity for missing states**:
- **Critical**: Missing error or loading states (user gets no feedback)
- **Major**: Missing hover/focus states (interaction feels broken)
- **Minor**: Missing transitions or micro-interactions (feels unpolished)

### Step 4: Responsive Fidelity

Check at 4 key breakpoints:

**Mobile (375px)**:
- Layout stacks to single column?
- Touch targets >= 44px?
- Navigation converts to mobile pattern (hamburger, tab bar)?
- Text readable without zooming?
- No horizontal scroll?
- Bottom-sheet or full-screen for modals?

**Tablet (768px)**:
- Layout adapts (2-column or adjusted spacing)?
- Touch targets still adequate?
- Sidebar behavior (collapsible or hidden)?
- Split view patterns where appropriate?

**Desktop (1280px)**:
- Full layout as designed?
- Max-width container preventing ultra-wide stretch?
- Hover states all present?
- Keyboard navigation functional?

**Wide (1536px+)**:
- Content doesn't stretch to full width?
- Comfortable reading line lengths?
- No awkward empty space?
- Grid fills appropriately?

Flag any breakpoint where the experience degrades.

### Step 5: Accessibility Fidelity

Quick accessibility audit on the implementation:

**Focus management**:
- Focus indicators visible on all interactive elements?
- Focus indicators have sufficient contrast?
- Custom focus styles (not just browser default outline)?

**Tab order**:
- Logical tab sequence (follows visual layout)?
- No focus traps (except intentional ones in modals)?
- Skip-to-content link present?

**Color contrast**:
- Text meets WCAG AA (4.5:1 for normal text, 3:1 for large text)?
- UI components meet 3:1 against background?
- Information not conveyed by color alone?

**ARIA and semantics**:
- Interactive elements have accessible names (aria-label, aria-labelledby)?
- Live regions for dynamic content updates?
- Correct landmark roles (header, nav, main, footer)?
- Form inputs associated with labels?

**Screen reader basics**:
- Meaningful alt text on images?
- Decorative images have empty alt or aria-hidden?
- Dynamic content changes announced?
- Error messages associated with inputs (aria-describedby)?

Note: For a full accessibility audit, use `/a11y`.

### Step 6: Cross-Browser Notes

Flag any code patterns that may cause cross-browser issues:
- CSS features without fallbacks (container queries, :has(), subgrid)
- Vendor-specific properties without standards equivalents
- JavaScript APIs with limited support
- Font rendering differences (antialiasing, weight rendering)

### Step 7: QA Report Generation

Generate a prioritized punch list with four severity tiers:

- **Critical**: Breaks functionality, blocks task completion, or fails accessibility requirements. Must fix before ship
- **Major**: Noticeable visual discrepancy from design, missing important states. Fix in current sprint
- **Minor**: Subtle misalignment, inconsistent spacing, missing transitions. Fix in next sprint
- **Polish**: Perfectionist-level details — sub-pixel alignment, advanced motion, edge-case states. Nice-to-have

Each item includes: what is wrong, where it is, expected value, actual value, and the specific fix.

---

## Output Format

```
## Design QA Report: [Target Name]

### Context
- **Implementation**: [files/components examined]
- **Design spec**: [source of truth used]
- **Platform**: [web/iOS/Android]
- **Prior Sumi context**: [consumed or "none"]

---

### Fidelity Summary

| Category | Issues | Critical | Major | Minor | Polish |
|----------|--------|----------|-------|-------|--------|
| Token Consumption | [N] | [N] | [N] | [N] | [N] |
| Visual Fidelity | [N] | [N] | [N] | [N] | [N] |
| State Coverage | [N] | [N] | [N] | [N] | [N] |
| Responsive | [N] | [N] | [N] | [N] | [N] |
| Accessibility | [N] | [N] | [N] | [N] | [N] |
| Cross-Browser | [N] | [N] | [N] | [N] | [N] |
| **Total** | **[N]** | **[N]** | **[N]** | **[N]** | **[N]** |

**Ship Readiness**: [Ready / Needs Critical Fixes / Needs Major Fixes / Not Ready]

---

### Token Consumption Audit

| # | Property | Component | Actual Value | Expected Token | Severity |
|---|----------|-----------|-------------|----------------|----------|
| 1 | color | .btn-primary | #2563eb | --color-primary | Minor |
| 2 | padding | .card | 13px | --spacing-3 (12px) | Minor |
[complete list]

---

### Visual Fidelity

#### [Component/Screen Name]
| # | Issue | Expected | Actual | Severity |
|---|-------|----------|--------|----------|
[per-component findings with specific values]

---

### State Coverage

| Component | Default | Hover | Focus | Active | Disabled | Loading | Error | Empty |
|-----------|---------|-------|-------|--------|----------|---------|-------|-------|
| Button | Yes | Yes | No | Yes | No | No | N/A | N/A |
| Input | Yes | N/A | Yes | N/A | No | N/A | No | N/A |
[complete matrix]

**Missing states by severity**:
- **Critical**: [list]
- **Major**: [list]
- **Minor**: [list]

---

### Responsive Fidelity

#### Mobile (375px)
[Findings with specific values]

#### Tablet (768px)
[Findings]

#### Desktop (1280px)
[Findings]

#### Wide (1536px+)
[Findings]

---

### Accessibility Fidelity

| # | Issue | Element | WCAG Criterion | Severity | Fix |
|---|-------|---------|---------------|----------|-----|
[findings with specific fixes]

---

### Cross-Browser Notes
[Flagged patterns with fallback recommendations]

---

### QA Punch List (Prioritized)

| # | Severity | Category | Component | Issue | Expected | Actual | Fix |
|---|----------|----------|-----------|-------|----------|--------|-----|
| 1 | Critical | A11y | nav-link | No focus indicator | 2px outline | none | Add focus-visible style |
| 2 | Critical | States | submit-btn | No loading state | Spinner | Static | Add loading prop |
| 3 | Major | Tokens | card | Hardcoded shadow | --shadow-md | 0 2px 8px | Replace with token |
[complete prioritized list]

---

### Next Steps
1. **Fix** critical and major issues
2. **Run** `/a11y` for full accessibility audit
3. **Run** `/grade` to score visual quality after fixes
4. **Run** `/audit` if systemic issues suggest deeper problems
```

---

## Quality Gates

The output MUST include:
- [ ] Every hardcoded value that should be a token is flagged with the correct token reference
- [ ] Visual fidelity checked with specific values ("padding is 10px, should be 12px"), not vague
- [ ] State coverage for all interactive elements with a component-by-state matrix
- [ ] Responsive check at 4+ breakpoints with specific findings
- [ ] Accessibility quick check covering focus, contrast, ARIA, and screen reader basics
- [ ] Cross-browser notes for any risky CSS/JS patterns
- [ ] Summary table with issue counts by category and severity
- [ ] Ship readiness verdict
- [ ] Prioritized punch list with severity ratings and specific fix instructions

The output MUST NOT include:
- Vague findings ("spacing seems off") — every issue must have exact expected vs. actual values
- Missing fix instructions — every item must say how to fix it
- Skipped categories — all audit dimensions must be covered even if clean
- Accessibility audit depth that replaces `/a11y` — keep it focused on implementation fidelity

---

## Cross-References

When performing design QA, draw knowledge from:
- `design-systems-architecture` — Token architecture, naming conventions, consumption patterns
- `visual-design-mastery` — Visual quality standards, alignment, hierarchy, consistency
- `accessibility-inclusive-design` — WCAG 2.2 compliance criteria, focus management, contrast ratios
- `platform-visual-standards` — Platform-specific conventions (iOS HIG, Material 3, CSS standards)
- `component-patterns-code` — Component implementation standards, state management, prop APIs
- `performance-states-patterns` — Loading, error, empty, and skeleton state requirements
- `interaction-motion-design` — Transition and animation standards

---

## Next Steps

After `/qa`:
- `/a11y` — Full accessibility audit with WCAG 2.2 AA checklist
- `/grade` — Visual quality scoring after fixes
- `/audit` — Comprehensive design audit if systemic issues found
- `/component [name]` — Rebuild flagged components from scratch
- `/tokens` — Revisit token system if consumption issues are systemic

---

## Project-Wide Consistency Audit

When the user runs `/qa project` or `/qa codebase` or `/qa all`, scan the entire project for design consistency issues across all components and screens.

### Scan Protocol

**Step 1: Discover UI Files**
Scan the project for all UI-related files:
- `**/*.tsx`, `**/*.jsx` — React components
- `**/*.vue` — Vue components
- `**/*.svelte` — Svelte components
- `**/*.css`, `**/*.scss` — Stylesheets
- `**/*.swift` — SwiftUI views
- `**/tailwind.config.*` — Tailwind configuration
- `.sumi/style.json` — Sumi design memory

**Step 2: Extract Design Values**

From every UI file, extract and catalog:

| Category | What to Extract | How to Detect |
|----------|----------------|---------------|
| Colors | Every color value used | Hex (#xxx), rgb(), oklch(), Tailwind color classes (text-blue-500, bg-gray-100), CSS variables (var(--color-*)) |
| Font sizes | Every font size | text-xs through text-9xl, font-size values, clamp() values |
| Font families | Every font used | font-family declarations, Tailwind font-* classes |
| Font weights | Every weight used | font-light through font-black, font-weight values |
| Spacing | Every spacing value | p-*, m-*, gap-*, space-*, padding/margin CSS values |
| Border radius | Every radius value | rounded-*, border-radius values |
| Shadows | Every shadow value | shadow-*, box-shadow values |
| Z-index | Every z-index value | z-*, z-index values |
| Breakpoints | Every responsive breakpoint | sm:, md:, lg:, xl:, @media queries |
| Transitions | Every transition/animation | transition-*, animation-*, @keyframes |

**Step 3: Consistency Analysis**

For each category, analyze:

**Color Consistency:**
- Total unique colors used across the project
- Colors that appear only once (orphans — likely errors)
- Colors that are very similar but not identical (e.g., #333 and #343434 — should be same token)
- Semantic usage: Is the same blue used for links AND errors? (violation)
- Dark mode coverage: Do all colors have dark mode equivalents?
- Token compliance: What percentage of colors reference tokens vs hardcoded values?

**Typography Consistency:**
- Total unique font sizes — should follow a scale (not random values)
- Font families used — should be 2-3 max
- Weight distribution — should be intentional (400 body, 600 heading, etc.)
- Line height consistency — should correspond to font size
- Orphan sizes — sizes used only once (likely arbitrary)

**Spacing Consistency:**
- Values used — do they follow a scale (4, 8, 12, 16, 24, 32, 48, 64)?
- Off-grid values — spacing values that don't fit the base grid
- Inconsistent padding patterns — same component type with different padding
- Section gap consistency — are page section gaps uniform?

**Component Pattern Consistency:**
- Button styles — how many button variants exist? Are they consistent?
- Card patterns — same shadow/radius/padding across all cards?
- Input styles — consistent border, focus ring, error state across all inputs?
- Modal/dialog patterns — consistent overlay, animation, close behavior?

**Step 4: Drift Report**

Output a structured drift report:

```
## Design Consistency Report — [Project Name]

### Overview
| Metric | Value | Health |
|--------|-------|--------|
| Total UI files scanned | [N] | — |
| Unique colors | [N] | 🟢 Good (<20) / 🟡 Warning (20-40) / 🔴 Critical (40+) |
| Unique font sizes | [N] | 🟢 Good (<10) / 🟡 Warning (10-15) / 🔴 Critical (15+) |
| Unique spacing values | [N] | 🟢 Good (<12) / 🟡 Warning (12-20) / 🔴 Critical (20+) |
| Token compliance | [N]% | 🟢 Good (>80%) / 🟡 Warning (50-80%) / 🔴 Critical (<50%) |
| Design system coverage | [N]% | — |

### Color Drift
| Color Value | Occurrences | Likely Intent | Suggested Token |
|-------------|-------------|---------------|-----------------|
| #2563eb | 23 | Primary action | var(--color-primary) |
| #2461e8 | 3 | Primary action (drift!) | var(--color-primary) — merge with #2563eb |
| #ef4444 | 12 | Error/destructive | var(--color-error) |
| #ff0000 | 1 | Error (orphan!) | var(--color-error) — merge with #ef4444 |

### Typography Drift
| Size | Occurrences | Likely Role | On Scale? |
|------|-------------|-------------|-----------|
| text-2xl (1.5rem) | 15 | Section heading | ✅ |
| text-[22px] | 2 | Section heading (drift!) | ❌ → use text-2xl |

### Spacing Drift
[Similar table for spacing values]

### Component Pattern Drift
| Pattern | Variants Found | Should Be | Files |
|---------|---------------|-----------|-------|
| Button padding | px-4 py-2, px-3 py-1.5, px-6 py-3 | 3 sizes (sm/md/lg) | [list] |
| Card radius | rounded-lg (12), rounded-xl (3), rounded-2xl (1) | Pick one: rounded-lg | [list] |
| Input border | border-gray-300 (8), border-gray-200 (3), border-slate-300 (2) | Standardize to one | [list] |

### Priority Fixes
Top 10 consistency issues ranked by frequency × severity:
1. [Most impactful fix]
2. [Second most impactful]
...

### Token Generation
If design tokens don't exist, generate a token file that standardizes all the values found:
- Map the most-used color values to semantic tokens
- Map font sizes to a type scale
- Map spacing to a grid scale
- Output as CSS custom properties and/or tailwind.config.js theme extension
```

### Integration with Other Commands
- `/qa project` can recommend running `/fix` on specific files with the most drift
- `/qa project` should reference `.sumi/style.json` if it exists and check compliance against those tokens
- After `/qa project`, suggest running `/tokens` to generate a standardized token file