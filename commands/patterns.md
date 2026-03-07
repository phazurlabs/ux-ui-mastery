---
description: Analyze a vibe-coded app's UI patterns, benchmark against world-class products, identify sector-specific gaps, and prescribe exact pattern upgrades. The pattern intelligence engine.
phase: "1"
phase_step: "1.5"
phase_name: "DISCOVER"
step_label: "Step 5 of 5"
---

# Patterns — UI Pattern Intelligence Engine

Analyze any codebase or screenshot against a 200+ pattern taxonomy, benchmark against 50+ world-class products, and prescribe the exact pattern upgrades that will make a vibe-coded app feel professionally designed.

## Analysis Protocol

### Step 0: Gather Context

Before analyzing, collect:

1. **Input**: Code (file paths or pasted), screenshots, or both. Code is highest-fidelity — it reveals states, accessibility, and implementation quality. Screenshots reveal visual execution and layout.
2. **What the app does**: Product description, purpose, target users.
3. **Sector**: Auto-detect from code/content, or ask the user. This is critical — sector determines which patterns are expected and which are anti-patterns.
4. **Platform**: Web (React, Vue, Svelte, HTML), iOS (SwiftUI, UIKit), Android (Compose, XML), or cross-platform (React Native, Flutter).
5. **Prior Sumi outputs**: Check for `/taste` (visual direction), `/intent` (problem + constraints), `/benchmark` (competitive context). Consume if available.

If the user provides only a description with no code or screenshots, explain that pattern analysis is most powerful with real code or screenshots, but proceed with a sector-based recommendation of expected patterns.

### Step 1: IDENTIFY — Pattern Inventory

Scan the codebase or screenshot and map every component, screen, and interaction to the pattern taxonomy (`ui-pattern-intelligence` skill → `pattern-taxonomy-complete.md`).

**For code analysis**:
- Walk through each file/component
- Use the code signal → pattern mapping tables from `pattern-matching-engine.md`
- Identify: navigation system, data display patterns, input patterns, feedback patterns, layout structure, commerce patterns (if applicable), AI patterns (if applicable)
- Note patterns that are ABSENT but expected

**For screenshot analysis**:
- Scan top-to-bottom, left-to-right
- Identify layout, navigation, content patterns, visual language
- Note visible states (or lack thereof)

**Output as**:
```
## Pattern Inventory
[N] patterns detected across [M] categories

### Navigation
- [Pattern Name] ([taxonomy ID]) — found in: [location]
- [Pattern Name] ([taxonomy ID]) — MISSING (expected for [reason])

### Data Display
[continue for all 10 categories]
```

### Step 2: BENCHMARK — Score Each Pattern

For every detected pattern, score its execution quality (1-10) against the benchmark products from `designer-benchmark-dna.md`.

**Scoring dimensions** (weighted):
- States coverage (25%): default, hover, focus, active, disabled, loading, error, success, skeleton, empty
- Accessibility (20%): ARIA, keyboard, focus, contrast, screen reader
- Visual execution (20%): typography, spacing, color, hierarchy, consistency
- Responsiveness (15%): mobile, tablet, desktop adaptation
- Motion & feedback (10%): transitions, micro-interactions, state change animation
- Pattern correctness (10%): follows canonical pattern or confusing deviation

**Score each pattern individually, then compute category averages.**

**You MUST**:
- Name the specific Tier 1/2 benchmark product for each pattern
- State the exact gap between the user's implementation and the benchmark
- Be specific: "Missing hover state on cards" not "Cards could be better"

**Output as**:
```
## Benchmark Scores

| Category | Patterns | Avg Score | Worst | Best | Benchmark Target |
|----------|----------|-----------|-------|------|-----------------|
| Navigation | [N] | [X/10] | [name: score] | [name: score] | [Product] |
[continue for all categories]

**Overall Pattern Quality: [X/10]**
```

### Step 3: SECTOR-FIT — Check Against Industry Expectations

Cross-reference the pattern inventory against the sector's expected patterns from `sector-pattern-matrix.md`.

**You MUST report**:
- **Critical pattern coverage**: X of Y critical patterns present (percentage)
- **Missing critical patterns**: Patterns that users in this sector expect but are absent
- **Missing important patterns**: Patterns that would differentiate
- **Present but unexpected**: Patterns that are unusual for this sector (verify intentional)
- **Sector anti-patterns detected**: Patterns that actively hurt in this sector
- **Visual direction alignment**: Do the colors, typography, and density match sector norms?

### Step 4: PRESCRIBE — Specific Upgrade Recommendations

For every pattern scoring below 7/10 and every missing critical/important pattern, generate a specific prescription.

**Each prescription MUST include**:
1. **Pattern name and current score** → target score
2. **What's wrong**: Specific issues (not vague)
3. **What world-class looks like**: Named product + what they do specifically
4. **How to fix**: Ordered priority list of changes
5. **Effort estimate**: Quick win (< 1hr) | Medium (1-4hr) | Large (4hr+) | Strategic (days)
6. **Principle**: The cognitive/UX principle that makes this important
7. **Sumi command**: Which `/command` to run to execute the fix

**Prioritize prescriptions**:
- **P0 — Fix Now**: Anti-patterns, broken patterns, missing critical sector patterns, accessibility failures
- **P1 — High Impact**: Core patterns scoring 3-5, missing important patterns, quick wins
- **P2 — Polish**: Patterns scoring 5-7, missing states, missing motion
- **P3 — Delight**: Patterns scoring 7-8, advanced details, edge cases

### Step 5: COHERENCE — Visual Language Assessment

Assess whether the patterns form a unified visual language:

**Check**: color consistency, typography consistency, spacing/grid, border radius, shadows/elevation, icon style, motion curves, density, pattern language (do similar actions use similar patterns?)

**Score 1-10** with specific findings.

If coherence < 7, recommend `/drip` to formalize the token system and `/ship` to rebuild outlier components.

## Output Format

```
### Phase Position
> **Phase 1: DISCOVER** | Step 5 of 5 | `/patterns`
> *NNG: Pattern Analysis | Visual: Pattern Intelligence*
>
> `/benchmark` (1.3) → `/pulse` (1.4) → **`/patterns` (1.5)** → `/vibe-check` (2.1)

---

## Pattern Intelligence Report

### App Overview
- **App**: [Name/description]
- **Sector**: [Detected/specified]
- **Platform**: [Web/iOS/Android]
- **Files analyzed**: [List or count]
- **Prior Sumi context**: [What was consumed from prior commands]

---

### Pattern Inventory ([N] patterns, [M] categories)

[Categorized list of every pattern found + notable absences]

---

### Benchmark Scores

| Category | Patterns | Avg | Worst Pattern | Best Pattern | Target (Tier 1) |
|----------|----------|-----|---------------|-------------|-----------------|
| Navigation | [N] | [X] | [name: score] | [name: score] | [Product: score] |
| Data Display | [N] | [X] | [name: score] | [name: score] | [Product: score] |
| Input & Forms | [N] | [X] | [name: score] | [name: score] | [Product: score] |
| Feedback | [N] | [X] | [name: score] | [name: score] | [Product: score] |
| Layout | [N] | [X] | [name: score] | [name: score] | [Product: score] |
| [others if applicable] | | | | | |

**Overall Pattern Quality: [X/10]**

---

### Sector Fit: [Sector Name]
- **Critical pattern coverage**: [X/Y] ([Z]%)
- **Missing critical**: [List with why each matters]
- **Missing important**: [List]
- **Sector anti-patterns detected**: [List with severity]
- **Visual direction**: [Aligned/Misaligned — specifics]

---

### P0 — Fix Now
[Prescriptions for anti-patterns, broken patterns, accessibility failures]

### P1 — High Impact
[Prescriptions for weak core patterns, missing important patterns]

### P2 — Polish
[Prescriptions for functional-but-generic patterns]

### P3 — Delight
[Prescriptions for good-to-great elevation]

---

### Style Coherence: [X/10]
[Specific findings and recommendations]

---

### Pattern Upgrade Roadmap

| # | Priority | Pattern | Current | Target | Effort | Impact | Fix With |
|---|----------|---------|---------|--------|--------|--------|----------|
| 1 | P0 | [name] | [X/10] | [Y/10] | [est] | Critical | `/ship [x]` |
| 2 | P0 | [name] | [X/10] | [Y/10] | [est] | Critical | `/include` |
| 3 | P1 | [name] | [X/10] | [Y/10] | [est] | High | `/ship [x]` |
| [continue prioritized] | | | | | | | |

---

### Next Steps

1. **First**: [Highest-impact, lowest-effort action — specific]
2. **Second**: [Next action]
3. **Third**: [Next action]

**Recommended command sequence**:
→ `/drip` — Formalize your token system (fixes coherence)
→ `/ship [weakest component]` — Rebuild the worst-scoring pattern
→ `/include` — Fix accessibility gaps across all patterns
→ `/vibe-check` — Verify improvements against heuristics
→ `/patterns` — Re-run to measure improvement
```

## Quality Gates

The output MUST include:
- [ ] Pattern count and category breakdown
- [ ] Per-pattern scores with named benchmarks (not vague)
- [ ] Sector identification and critical pattern coverage percentage
- [ ] At least one prescription per priority level (P0-P3) if applicable
- [ ] Coherence score with specific findings
- [ ] Prioritized roadmap table
- [ ] Next steps with specific Sumi commands

The output MUST NOT include:
- Vague feedback ("could be better", "consider improving") — every finding must be specific
- Scores without justification — every score must cite what's present and what's missing
- Recommendations without benchmarks — every upgrade must reference a product that does it well
- Effort estimates without basis — ground estimates in the scope of change required

## Cross-References

When analyzing patterns, draw implementation knowledge from:
- `ui-pattern-intelligence` skill — pattern taxonomy, benchmarks, sector matrix, evolution, anti-patterns
- `sector-style-intelligence` skill — visual direction per sector (colors, typography, motion, tone)
- `component-patterns-code` skill — React, SwiftUI, CSS implementations for recommended patterns
- `cognitive-psychology-ux` skill — Laws of UX that ground pattern recommendations
- `nng-ux-heuristics` skill — heuristic evaluation framework for scoring
- `accessibility-inclusive-design` skill — WCAG compliance for accessibility scoring
- `design-systems-architecture` skill — token architecture for coherence assessment
- `interaction-motion-design` skill — motion patterns for animation scoring
- `performance-states-patterns` skill — loading/error/empty state patterns
- `screen-flow-patterns` skill — screen type patterns and flow patterns

## Next Step

**Next** → `/vibe-check` (2.1) — Deep heuristic audit on the patterns identified

**Alternatives**:
- `/ship [component]` — Build the highest-priority pattern upgrade immediately
- `/drip` (4.1) — Create a design token system to fix coherence
- `/include` (2.3) — Deep accessibility audit on flagged patterns
- `/taste` (1.1) — Get sector visual direction if not already done
- `/guide` — See the full journey map
