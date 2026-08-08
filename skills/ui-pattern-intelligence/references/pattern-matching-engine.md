# Pattern Matching Engine — Analysis Protocol

## How Pattern Matching Works

When a user runs `/audit` on their codebase or provides a screenshot, Sumi performs a systematic analysis pipeline. This file defines the exact methodology for each stage.

The pipeline has 5 stages: IDENTIFY → BENCHMARK → SECTOR-FIT → PRESCRIBE → COHERENCE.

---

## Stage 1: IDENTIFY — Map Code/Screenshots to Patterns

### Code Analysis Heuristics

When analyzing source code (React, SwiftUI, HTML/CSS, Vue, Svelte, or any component-based framework), use these heuristics to identify which patterns are present.

#### Navigation Pattern Detection

| Code Signal | Pattern Identified |
|------------|-------------------|
| `<nav>` with horizontal `<ul>` or flex row at top of page | Top Navigation Bar (1.1) |
| Fixed/sticky bottom bar with 3-5 icon+label items | Bottom Navigation Bar (1.2) |
| Vertical `<nav>` or `<aside>` with links, typically left-positioned | Sidebar Navigation (1.3) |
| Ordered list with ">" or "/" separators, ancestor links | Breadcrumbs (1.4) |
| `role="tablist"` or horizontal toggle group switching content | Tab Navigation (1.5) |
| Dialog/overlay triggered by Cmd+K or Ctrl+K with search input | Command Palette (1.6) |
| Hamburger icon (3 lines) toggling a hidden nav panel | Hamburger Menu (1.7) |
| "Previous"/"Next" buttons with page numbers | Pagination (1.8) |
| Intersection Observer or scroll event loading more content | Infinite Scroll (1.9) |
| Numbered/labeled sequential steps with Next/Back buttons | Stepper/Wizard (1.10) |

#### Data Display Pattern Detection

| Code Signal | Pattern Identified |
|------------|-------------------|
| `<table>` with `<thead>`, `<tbody>`, sortable columns | Data Table (2.1) |
| Repeated container components with image + text + CTA | Card (2.2) |
| `<ul>` or `<ol>` with consistent multi-element list items | List/Feed (2.3) |
| Chart library imports (recharts, d3, chart.js, visx, victory) | Chart (2.4) |
| Small pill/rounded element with status text or count | Badge/Tag (2.5) |
| Circular image with fallback initials | Avatar (2.6) |
| Large prominent number with label and trend indicator | Stat Display (2.7) |
| `<details>/<summary>` or collapsible sections | Accordion (2.8) |
| `role="tooltip"` or hover-triggered floating text | Tooltip (2.9) |
| `role="dialog"` or `aria-modal="true"` overlay | Modal (2.11) |
| Panel sliding from screen edge | Drawer/Sheet (2.12) |
| Horizontal scroll with dots/arrows for content panels | Carousel (2.13) |
| Columns with draggable cards between them | Kanban Board (2.16) |
| Date grid with events | Calendar View (2.17) |
| Animated placeholder shapes (pulse/wave) | Skeleton Screen (2.22) |
| Rotating/spinning indicator | Loading Spinner (2.23) |
| Full-width colored banner with icon and message | Alert Banner (2.24) |
| Temporary auto-dismissing message at bottom/top | Toast (2.25) |

#### Input Pattern Detection

| Code Signal | Pattern Identified |
|------------|-------------------|
| `<input type="text">` with `<label>` | Text Input (3.1) |
| Input with search icon, `role="search"`, instant results | Search Input (3.2) |
| `<select>` or custom dropdown with options list | Select/Dropdown (3.3) |
| `<input type="checkbox">` | Checkbox (3.4) |
| `<input type="radio">` with same `name` group | Radio Button (3.5) |
| `role="switch"` or sliding toggle control | Toggle/Switch (3.6) |
| Calendar popup triggered by date input | Date Picker (3.7) |
| Drop zone with drag-over states, `<input type="file">` | File Upload (3.8) |
| `<textarea>` or rich text editor (TipTap, ProseMirror, Slate) | Textarea/Rich Text (3.9) |
| Input with `type="password"` and visibility toggle | Password Input (3.15) |
| 4-6 individual digit input boxes | OTP Input (3.16) |
| Star/heart selection for rating | Rating Input (3.20) |
| Click-to-edit text that transforms between display and input | Inline Editing (3.25) |

#### Layout Pattern Detection

| Code Signal | Pattern Identified |
|------------|-------------------|
| Single centered column, max-width 600-800px | Single Column (5.1) |
| CSS Grid or flex with content + sidebar | Two Column (5.2) |
| Grid of equal-sized card containers | Card Grid (5.4) |
| Grid with varying card sizes (grid-template-areas) | Bento Grid (5.5) |
| Two equal halves (50/50 split) | Split Screen (5.7) |
| `position: sticky` header + scrollable main | Sticky Header (5.10) |
| Fixed sidebar + flex-grow main content | Fixed Sidebar (5.11) |
| List panel + detail panel side by side | Master-Detail (5.12) |

#### Commerce Pattern Detection

| Code Signal | Pattern Identified |
|------------|-------------------|
| Product image + name + price + add-to-cart | Product Card (6.1) |
| Image gallery + product info + purchase button | Product Detail Page (6.2) |
| Line items with quantities + totals | Shopping Cart (6.3) |
| Multi-step: shipping → payment → confirmation | Checkout Flow (6.4) |
| Tiered plan cards with monthly/annual toggle | Pricing Page (6.5) |
| Testimonials, review counts, customer logos | Social Proof (6.6) |

#### AI Pattern Detection

| Code Signal | Pattern Identified |
|------------|-------------------|
| Chat-like interface with user/assistant messages, streaming text | AI Chat (10.1) |
| Ghost text suggestions appearing inline | AI Copilot (10.2) |
| Natural language input that triggers app actions | AI Command Bar (10.3) |
| "Accept/Edit/Regenerate" buttons on AI-generated content | AI Content Preview (10.4) |
| Thumbs up/down on AI responses | AI Feedback Loop (10.7) |

### Screenshot Analysis Protocol

When analyzing screenshots (rather than code), use visual pattern recognition:

1. **Scan top-to-bottom, left-to-right** — identify the primary layout (single column, sidebar, split, dashboard grid)
2. **Identify the navigation system** — top bar? sidebar? bottom bar? hamburger? tabs?
3. **Identify the primary content pattern** — cards? table? list? chart? form?
4. **Catalog every distinct UI element** — buttons, inputs, badges, avatars, icons, dividers
5. **Note the visual language** — colors, typography weight, spacing density, border radius, shadows
6. **Identify states visible** — are there loading states? empty states? error states? hover states?
7. **Check for patterns absent** — no search? no breadcrumbs? no status indicators? Absence is a finding.

### Output: Pattern Inventory

After identification, produce a structured inventory:

```
Pattern Inventory for [App Name]
Detected: [N] patterns across [M] categories

Navigation:
  - Top Nav Bar (1.1) — found in: Header.tsx
  - Sidebar (1.3) — found in: Sidebar.tsx
  - Breadcrumbs (1.4) — NOT FOUND (expected for this app type)

Data Display:
  - Cards (2.2) — found in: ProjectCard.tsx, TaskCard.tsx
  - Data Table (2.1) — found in: UserTable.tsx
  - Skeleton (2.22) — NOT FOUND (loading states missing)

[...continue for all 10 categories]
```

---

## Stage 2: BENCHMARK — Score Each Pattern

For every pattern identified in Stage 1, score its execution quality against the benchmark products from `designer-benchmark-dna.md`.

### Scoring Dimensions (per pattern)

| Dimension | Weight | What to Evaluate |
|-----------|--------|-----------------|
| **States coverage** | 25% | Does the pattern handle all applicable states? (default, hover, focus, active, disabled, loading, error, success, skeleton, empty) |
| **Accessibility** | 20% | ARIA attributes, keyboard navigation, focus management, screen reader support, color contrast |
| **Visual execution** | 20% | Typography, spacing, color, hierarchy, consistency with the rest of the app |
| **Responsiveness** | 15% | Does it adapt to mobile, tablet, desktop? Touch targets on mobile? |
| **Motion & feedback** | 10% | Transitions, micro-interactions, loading feedback, state change animations |
| **Pattern correctness** | 10% | Does it follow the canonical pattern or deviate in confusing ways? |

### Scoring Scale

| Score | Label | Characteristics |
|-------|-------|----------------|
| 1-2 | Broken | Missing critical functionality. Anti-pattern territory. Would confuse or block users. |
| 3-4 | Weak | Pattern recognizable but significant issues. Missing states, no accessibility, inconsistent styling. |
| 5-6 | Functional | Works but generic. Default framework output. No polish, no states beyond default, basic or no accessibility. This is where most vibe-coded apps land. |
| 7-8 | Good | Well-executed. Multiple states, keyboard accessible, visually polished, responsive. Minor gaps. |
| 9-10 | World-class | Benchmark-quality. All states. Full accessibility. Refined motion. Responsive. Delightful details. |

### Scoring Protocol

For each detected pattern:

1. **Identify the benchmark**: Which Tier 1/2 product sets the standard for this pattern? (Use `designer-benchmark-dna.md`)
2. **Check states**: Count how many of the applicable states are implemented vs. expected
3. **Check accessibility**: Are ARIA attributes present? Is keyboard navigation working? Is focus managed?
4. **Check visual quality**: Is the typography, spacing, and color consistent and intentional?
5. **Check responsiveness**: Does it work across breakpoints?
6. **Check motion**: Are there transitions? Loading feedback? State change animations?
7. **Calculate weighted score**: Apply dimension weights
8. **Generate gap analysis**: What specific changes would increase the score?

### Output: Benchmark Scorecard

```
Pattern Benchmark Scores

| Pattern | Score | Benchmark Target | Gap |
|---------|-------|-----------------|-----|
| Top Nav (1.1) | 6/10 | Linear 9/10 | Missing: keyboard shortcuts, active state, responsive collapse |
| Cards (2.2) | 5/10 | Airbnb 10/10 | Missing: hover state, loading skeleton, consistent heights |
| Data Table (2.1) | 7/10 | Stripe 10/10 | Missing: empty state, column resize, sticky header |
| Search (3.2) | 4/10 | Algolia 10/10 | Missing: instant results, recent searches, keyboard navigation |

Overall Pattern Quality: 5.5/10
Patterns at benchmark: 0/[N]
Patterns needing work: [N]
Anti-patterns detected: [N]
```

---

## Stage 3: SECTOR-FIT — Cross-Reference Against Sector Expectations

Using the `sector-pattern-matrix.md`, evaluate whether the app has the right patterns for its sector.

### Analysis Protocol

1. **Identify the sector** (from user input or auto-detected from code/content):
   - Look for domain-specific terms, data models, or imports
   - Payment/banking terms → Fintech
   - Product/cart/checkout terms → E-commerce
   - Patient/health/medical terms → Healthcare
   - Lesson/course/quiz terms → Education
   - Post/feed/follow terms → Social
   - If ambiguous, ask the user

2. **Pull the sector's critical pattern list** from the sector matrix

3. **Cross-reference**:
   - **Present + Critical**: Good — verify execution quality
   - **Present + Not Expected**: Investigate — is this a deliberate choice or accidental?
   - **Missing + Critical**: Flag as HIGH priority — this is expected for the sector
   - **Missing + Important**: Flag as MEDIUM priority — would improve the product
   - **Anti-pattern for sector**: Flag as URGENT — this actively hurts in this sector

4. **Sector visual alignment**: Does the visual direction (colors, typography, density, motion) match sector expectations?

### Output: Sector Fit Report

```
Sector: [Detected/Specified]
Critical Pattern Coverage: [X/Y] (Z%)

MISSING CRITICAL:
  - Trust Signals (6.12) — Expected for fintech, not found
  - Error Handling (2.21) — Financial apps must have clear error states

MISSING IMPORTANT:
  - Sparkline Charts (2.4) — Expected for financial dashboards

PRESENT BUT UNEXPECTED:
  - Gamification (9.10) — Unusual for fintech, verify this is intentional

SECTOR ANTI-PATTERNS DETECTED:
  - Infinite scroll on transaction list (fintech anti-pattern — use pagination)

VISUAL DIRECTION ALIGNMENT:
  - Colors: [Aligned / Misaligned — details]
  - Typography: [Aligned / Misaligned — details]
  - Density: [Aligned / Misaligned — details]
```

---

## Stage 4: PRESCRIBE — Specific Upgrade Recommendations

For every pattern scored below 7/10, and every missing critical/important pattern, generate a specific upgrade prescription.

### Prescription Format

For each finding:

```
UPGRADE: [Pattern Name] ([Current Score] → [Target Score])

WHAT'S WRONG:
  [Specific issues identified in the current implementation]

WHAT WORLD-CLASS LOOKS LIKE:
  [Reference product] does it this way: [specific description]
  [Why it works]: [Cognitive/UX principle]

HOW TO FIX:
  Priority 1: [Most impactful change — describe specifically]
  Priority 2: [Second change]
  Priority 3: [Third change]

EFFORT ESTIMATE:
  [Quick win: < 1hr | Medium: 1-4hr | Large: 4hr+ | Strategic: days]

PRINCIPLES APPLIED:
  - [Law/Heuristic]: [How it applies]
  - [Law/Heuristic]: [How it applies]
```

### Prescription Prioritization

Rank all prescriptions by impact × effort:

| Priority | Criteria |
|----------|----------|
| **P0 — Fix Now** | Anti-patterns or broken patterns that actively hurt usability. Missing critical sector patterns. Accessibility failures. |
| **P1 — High Impact** | Patterns scoring 3-5 that are core to the product. Missing important patterns. Quick wins that dramatically improve quality. |
| **P2 — Polish** | Patterns scoring 5-7 that could be elevated to good. Missing motion, missing states. |
| **P3 — Delight** | Patterns scoring 7-8 that could reach world-class. Advanced animation, micro-interactions, edge case handling. |

### Linking to Sumi Commands

Every prescription should link to the Sumi command that can execute the fix:

| Fix Type | Command |
|----------|---------|
| Build a new component | `/ship [component]` |
| Build a new screen | `/screen [screen type]` |
| Create design tokens | `/tokens` |
| Fix accessibility issues | `/a11y` |
| Improve content/copy | `/audit` |
| Redesign a pattern | `/remix` |
| Verify the fix | `/roast` or `/audit` |

---

## Stage 5: COHERENCE — Visual Language Assessment

The final check: do all the patterns used form a coherent visual language, or does the app feel like a Frankenstein of copied patterns from different sources?

### Coherence Dimensions

| Dimension | What to Check |
|-----------|--------------|
| **Color consistency** | Is the same palette used throughout? Are semantic colors (success, error, warning) consistent? |
| **Typography consistency** | Same typeface family? Consistent scale? Consistent weight usage? |
| **Spacing consistency** | Same base grid (4px, 8px)? Consistent padding within similar elements? |
| **Border radius consistency** | Same radius values across cards, inputs, buttons, badges? |
| **Shadow/elevation consistency** | Same shadow system? Consistent elevation levels? |
| **Icon style consistency** | Same icon set? Same stroke weight? Same fill style? |
| **Motion consistency** | Same easing curves? Same duration ranges? Same interaction patterns? |
| **Density consistency** | Same information density across screens? Or jarring shifts between dense and sparse? |
| **Pattern language consistency** | Do similar actions use similar patterns? (e.g., all destructive actions are red buttons, all navigation is in the sidebar) |

### Coherence Scoring

| Score | Label | Description |
|-------|-------|-------------|
| 1-3 | **Incoherent** | Frankenstein UI. Multiple design systems mixed. No consistent visual language. Common in vibe-coded apps that pull from multiple prompts or templates. |
| 4-5 | **Fragmented** | Some consistency but notable breaks. Maybe the dashboard uses one style and settings uses another. Or cards and tables have different spacing systems. |
| 6-7 | **Mostly coherent** | Clear visual language with occasional breaks. Perhaps one component was added later and doesn't match, or dark mode has inconsistencies. |
| 8-9 | **Unified** | Strong design system. Consistent across all screens. Minor edge cases might deviate. |
| 10 | **Systematic** | Design token-driven. Every value traces to a token. Every pattern follows the system. Design system maturity level 4-5. |

### Coherence Fix Protocol

If coherence < 7:

1. **Identify the dominant style** — which screens/components represent the "intended" design language?
2. **Identify outliers** — which components break from the dominant style?
3. **Recommend token extraction** → `/tokens` to formalize the visual language into W3C design tokens
4. **Recommend component rebuilding** → `/component` to rebuild outlier components using the token system
5. **Recommend audit** → `/grade` to verify coherence after fixes

---

## Full Pipeline Output Template

```
# Pattern Intelligence Report

## App Overview
- **App**: [Name/description]
- **Sector**: [Detected/specified]
- **Platform**: [Web/iOS/Android/Cross-platform]
- **Code analyzed**: [Files/components/screens]

## Pattern Inventory
[N] patterns detected across [M] categories
[Table of all detected patterns with file locations]

## Benchmark Scores
| Category | Patterns | Avg Score | Best Pattern | Worst Pattern | Tier 1 Benchmark |
|----------|----------|-----------|-------------|---------------|-----------------|
| Navigation | [N] | [X/10] | [Name: score] | [Name: score] | [Product: score] |
| Data Display | [N] | [X/10] | [Name: score] | [Name: score] | [Product: score] |
| Input & Forms | [N] | [X/10] | [Name: score] | [Name: score] | [Product: score] |
| [continue...] | | | | | |

**Overall Pattern Quality: [X/10]**

## Sector Fit
- Critical pattern coverage: [X/Y] ([Z]%)
- Missing critical: [list]
- Missing important: [list]
- Sector anti-patterns: [list]

## Critical Upgrades (P0)
[Prescriptions for anti-patterns and missing critical patterns]

## High-Impact Upgrades (P1)
[Prescriptions for weak core patterns]

## Polish Upgrades (P2)
[Prescriptions for functional-but-generic patterns]

## Delight Upgrades (P3)
[Prescriptions for good-to-great patterns]

## Style Coherence: [X/10]
[Assessment and fix recommendations]

## Pattern Upgrade Roadmap
| Priority | Pattern | Current | Target | Effort | Impact | Fix Command |
|----------|---------|---------|--------|--------|--------|-------------|
| P0 | [name] | [X/10] | [Y/10] | [effort] | [impact] | `/ship [x]` |
| P1 | [name] | [X/10] | [Y/10] | [effort] | [impact] | `/remix` |
| [continue...] | | | | | | |

## Next Steps
1. [First action — highest impact, lowest effort]
2. [Second action]
3. [Third action]

→ Run `/ship [component]` to build upgraded patterns
→ Run `/tokens` to formalize your design token system
→ Run `/audit` after fixes to verify improvement
```
