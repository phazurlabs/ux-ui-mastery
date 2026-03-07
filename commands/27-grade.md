---
description: "[6.2] Visual quality score — score any UI across 10 visual dimensions calibrated to Awwwards and international design award standards."
phase: "6"
phase_step: "6.2"
phase_name: "LAUNCH"
step_label: "Step 27 of 30"
---

# Visual Score — Visual Design Quality Assessment

Score any UI's visual design quality across 10 weighted dimensions, calibrated to Awwwards and international design award standards. Every score is justified with specific observations, benchmarked against named world-class products, and paired with actionable prescriptions.

## Analysis Protocol

### Step 0: Gather Context

Before scoring, collect:

1. **Input**: Screenshot, URL, code files, or Figma link. Code + screenshot together gives highest-fidelity scoring. Screenshots reveal visual execution; code reveals states, accessibility, and implementation quality.
2. **What the app does**: Product description, purpose, target users.
3. **Sector**: Auto-detect from content/code, or ask the user. Sector determines what "good" looks like — a fintech app and a children's game have different visual quality benchmarks.
4. **Platform**: Web, iOS, Android, or cross-platform.
5. **Prior Sumi outputs**: Especially `/vision` (visual direction — score against the intended direction), `/patterns` (pattern inventory), `/vibe-check` (heuristic findings). Consume if available.

If the user provides only a description with no visual input, explain that scoring requires visual evidence (screenshot, code, or URL) and ask for input. Do not score hypothetically.

### Step 1: SCAN — Visual Inventory

Catalog every visual element present in the input:

**Colors**: List every distinct color observed. Note the apparent palette structure (or lack thereof). Count unique colors. Identify primary, secondary, semantic usage.

**Typography**: List every font observed (or inferred from code). Note size variations, weight usage, hierarchy levels. Count distinct type styles.

**Spacing**: Note spacing consistency or inconsistency. Identify apparent base unit (or lack of one). Note density.

**Shapes**: Border radii observed, shape consistency across components, icon style.

**Imagery**: Photos, illustrations, decorative elements — quality, treatment consistency.

**Icons**: Style (outlined/filled/mixed), consistency, grid adherence.

**Motion** (if code available): Transitions, animations, easing curves, durations.

**Elevation**: Shadow usage, depth layering, consistency.

**Visual language assessment**: Is there a coherent visual language? Is it consistent? Does it feel intentional or ad hoc?

### Step 2: SCORE — 10-Dimension Assessment

Using `visual-scoring-framework.md` from the `visual-design-mastery` skill, score each dimension 1-10.

**For EACH of the 10 dimensions, provide ALL of the following**:

1. **Score** (1-10): Whole numbers only. Be honest — most production apps score 5-7. Scores of 8+ are rare and reserved for genuinely exceptional work. Scores below 4 indicate fundamental problems.

2. **What's working**: Specific positive observations. Name exact elements, components, or choices that are well-executed. Minimum 2 observations.

3. **What's failing**: Specific negative observations. Name exact elements, components, or choices that are weak. Minimum 2 observations (unless score is 9+).

4. **Benchmark gap**: Name a specific product that scores 9/10 in this dimension. Describe what they do that this UI does not. This is the target.

5. **Priority fix**: The single most impactful improvement for this dimension. Specific enough to act on immediately.

**The 10 dimensions**:

1. **Typography** (15% weight) — Hierarchy clarity, readability, vertical rhythm, font selection quality, weight usage discipline, line-height consistency, letter-spacing craft, fluid scaling, platform convention adherence.

2. **Color** (12% weight) — Palette harmony, contrast ratios, semantic color usage, palette cohesion across components, dark mode quality (if applicable), color blindness consideration, surface/background relationship, accent restraint.

3. **Spacing** (12% weight) — Consistency of spacing tokens, breathing room, density appropriateness for sector, vertical rhythm, component internal padding, section margins, grid alignment, responsive spacing adaptation.

4. **Composition** (12% weight) — Grid alignment, visual weight distribution, balance (symmetrical or asymmetrical), focal point hierarchy, whitespace usage, content grouping (Gestalt proximity), alignment consistency, responsive reflow quality.

5. **Imagery** (8% weight) — Photo/illustration quality, relevance to content, treatment consistency (filters, crops, aspect ratios), art direction, placeholder quality, responsive image handling, loading treatment.

6. **Iconography** (8% weight) — Style consistency (all outlined OR all filled, not mixed), clarity of meaning, size consistency, grid adherence, stroke width consistency, optical alignment, icon-to-label relationship.

7. **Motion** (8% weight) — Purpose (does animation communicate or decorate?), timing appropriateness, easing curve quality, choreography (do related elements animate together?), restraint (not over-animated), reduced motion support, state transition smoothness.

8. **Polish** (10% weight) — Pixel perfection, state coverage (hover, focus, active, disabled, loading, error, empty, skeleton), edge case handling, detail work (dividers, borders, shadows done well), consistent interactive feedback, no visual glitches.

9. **Coherence** (8% weight) — Visual language unity across all screens/components, design token consumption consistency, pattern language consistency (similar actions use similar UI), brand expression consistency, no "franken-design" (mixing different design systems).

10. **Craft** (7% weight) — Overall feeling of intentionality, care, and mastery. Does this feel like a designer cared about every pixel? Is there evidence of deliberate design decisions? Does the whole exceed the sum of parts? Would this earn respect from design peers?

### Step 3: COMPUTE — Weighted Overall Score

**Apply weights to dimension scores**:
```
Overall = (Typography * 0.15) + (Color * 0.12) + (Spacing * 0.12) +
          (Composition * 0.12) + (Imagery * 0.08) + (Iconography * 0.08) +
          (Motion * 0.08) + (Polish * 0.10) + (Coherence * 0.08) +
          (Craft * 0.07)
```

**Map to quality tier**:
- < 4.0: Needs Redesign — fundamental visual problems, not shippable
- 4.0 - 5.4: Amateur — functional but visually weak, typical of undesigned vibe-coded apps
- 5.5 - 6.9: Competent — acceptable but generic, no visual distinction
- 7.0 - 8.4: Professional — solid visual quality, competitive with good SaaS products
- 8.5 - 10.0: World-Class — exceptional craft, award-worthy, top 1% of products

**Awwwards equivalent estimate**:
- Map the overall score to Awwwards' 4-criteria system (Design, Usability, Creativity, Content — each 1-10)
- Estimate total Awwwards score (out of 40, then averaged to 10)
- Note: Awwwards skews toward marketing sites; adjust for product/app context

### Step 4: DIAGNOSE — Top Visual Issues

Rank ALL identified issues by impact (how much it hurts visual quality) multiplied by effort (how hard it is to fix):

**P0 — Critical** (makes the design look amateur):
- Issues that immediately signal "not designed by a designer"
- Mixed icon styles, broken typography hierarchy, clashing colors, inconsistent spacing
- These destroy credibility on first impression

**P1 — High Impact** (prevents professional quality):
- Issues that cap the design at "competent" level
- Missing states, weak color contrast, no motion, poor density control
- Fixing these moves the score from 5-6 range to 7-8 range

**P2 — Polish** (prevents world-class quality):
- Issues that separate good from great
- Imperfect easing curves, slightly off spacing, good-but-not-great typography
- Fixing these moves the score from 7-8 range to 8.5+ range

**P3 — Delight** (opportunities for exceptional craft):
- Not problems but opportunities
- Micro-interactions, Easter eggs, exceptional empty states, crafted transitions
- These are what make designers screenshot your app and share it

### Step 5: PRESCRIBE — Visual Upgrade Path

For each issue identified (P0 through P2 minimum), provide ALL of the following:

1. **What's wrong**: Specific observation with exact location/component.
2. **What world-class looks like**: Named product that does this exceptionally. Describe what they do specifically.
3. **How to fix**: Specific values — exact colors (hex), exact sizes (px), exact spacing, exact timing (ms). Not "make it bigger" but "increase to 18px with 28px line-height".
4. **Which canonical rule applies**: Citation from `canonical-design-rules.md` (e.g., "Rule 12: The 60-30-10 color distribution").
5. **Which designer would solve this differently**: Reference from `designer-pattern-library.md` (e.g., "Tobias van Schneider would use a monochromatic palette with one high-contrast accent").
6. **Effort estimate**: Quick win (< 1hr) | Medium (1-4hr) | Large (4hr+) | Strategic (days).
7. **Sumi command to execute the fix**: Which `/command` addresses this issue directly.

## Output Format

```
### Phase Position
> **Phase 5: LAUNCH** | Step 4 of 4 | `/visual-score`
> *NNG: Visual Quality Assessment | Visual: Design Scoring*
>
> `/judge` (5.3) -> **`/visual-score` (5.4)**

---

## Visual Design Score Report

### App Overview
- **App**: [Name/description]
- **Sector**: [Detected/specified]
- **Platform**: [Platform]
- **Input analyzed**: [Screenshots/code/URL — list what was examined]
- **Prior Sumi context**: [What was consumed from prior commands]

---

### Visual Inventory

**Colors**: [N] unique colors detected — [list key colors with hex]
**Typography**: [N] type styles — [fonts, sizes observed]
**Spacing**: [Base unit detected or "inconsistent"] — [density assessment]
**Shapes**: [Radius values observed] — [consistency assessment]
**Imagery**: [Type and quality assessment]
**Icons**: [Style, consistency assessment]
**Motion**: [Present/absent, quality if present]
**Elevation**: [Shadow usage assessment]
**Visual Language**: [Coherent/fragmented — brief assessment]

---

### 10-Dimension Scores

| # | Dimension | Weight | Score | Tier | Top Issue |
|---|-----------|--------|-------|------|-----------|
| 1 | Typography | 15% | [X/10] | [tier] | [single top issue] |
| 2 | Color | 12% | [X/10] | [tier] | [single top issue] |
| 3 | Spacing | 12% | [X/10] | [tier] | [single top issue] |
| 4 | Composition | 12% | [X/10] | [tier] | [single top issue] |
| 5 | Imagery | 8% | [X/10] | [tier] | [single top issue] |
| 6 | Iconography | 8% | [X/10] | [tier] | [single top issue] |
| 7 | Motion | 8% | [X/10] | [tier] | [single top issue] |
| 8 | Polish | 10% | [X/10] | [tier] | [single top issue] |
| 9 | Coherence | 8% | [X/10] | [tier] | [single top issue] |
| 10 | Craft | 7% | [X/10] | [tier] | [single top issue] |

**Overall Visual Score: [X.X/10] — [Quality Tier]**
**Awwwards Equivalent: ~[X.X]/10**

---

### Dimension Deep-Dives

#### 1. Typography — [X/10]
**Working**: [specific positives]
**Failing**: [specific negatives]
**Benchmark**: [Product] scores 9/10 because [specific reason]
**Priority fix**: [single most impactful improvement]

#### 2. Color — [X/10]
[same structure]

[continue for all 10 dimensions]

---

### P0 — Critical Visual Issues
[Issues that make it look amateur — each with location and specific observation]

### P1 — High Impact
[Issues preventing professional quality]

### P2 — Polish
[Issues preventing world-class quality]

### P3 — Delight Opportunities
[Opportunities for exceptional craft]

---

### Visual Upgrade Roadmap

| # | Priority | Dimension | Issue | Fix | Canonical Rule | Effort | Impact | Command |
|---|----------|-----------|-------|-----|---------------|--------|--------|---------|
| 1 | P0 | [dim] | [specific issue] | [specific fix with values] | [rule #] | [est] | Critical | [/cmd] |
| 2 | P0 | [dim] | [specific issue] | [specific fix with values] | [rule #] | [est] | Critical | [/cmd] |
| 3 | P1 | [dim] | [specific issue] | [specific fix with values] | [rule #] | [est] | High | [/cmd] |
[continue prioritized — all P0 and P1 minimum, P2 if applicable]

---

### Score Projection

If all P0 fixes are applied: **[X.X/10]** (from [current])
If all P0 + P1 fixes are applied: **[X.X/10]**
If all P0 + P1 + P2 fixes are applied: **[X.X/10]**

---

### Next Steps
1. **First**: [Highest-impact visual fix — specific]
2. **Second**: [Next fix — specific]
3. **Third**: [Next fix — specific]

**Recommended command sequence**:
-> `/vision` — Generate/update visual direction (if not done or if direction needs revision)
-> `/drip` — Formalize tokens to fix coherence issues
-> `/ship [component]` — Rebuild the weakest-scoring components
-> `/visual-score` — Re-run to measure improvement
```

## Quality Gates

The output MUST include:
- [ ] All 10 dimensions scored with specific observations (not vague)
- [ ] Every score justified with what's working AND what's failing (minimum 2 each)
- [ ] Named benchmark product for every dimension (specific product, specific quality)
- [ ] Weighted overall score computed correctly using the formula
- [ ] Quality tier label applied correctly
- [ ] Awwwards equivalent estimated
- [ ] Priority-ranked issues across all four levels (P0-P3)
- [ ] Every prescription includes specific values (colors, sizes, spacing, timing — not "make it better")
- [ ] Canonical design rule citation for every P0 and P1 prescription
- [ ] Designer reference for P0 prescriptions (from designer-pattern-library.md)
- [ ] Effort estimate for every prescription
- [ ] Sumi command for every prescription
- [ ] Upgrade roadmap table sorted by priority then impact
- [ ] Score projection showing expected score after each priority tier is addressed

The output MUST NOT include:
- Vague feedback ("could be better", "consider improving", "needs work") — every finding must be specific and actionable
- Scores without justification — every score must cite what's present and what's missing
- Recommendations without benchmarks — every upgrade must reference a product that does it well
- Effort estimates without basis — ground estimates in the scope of change required
- Inflated scores — most production apps score 5-7. Be honest. A score of 8+ must be earned.
- Prescriptions without specific values — "increase contrast" is not acceptable; "change text from #999 to #666 on #fff background (ratio: 5.74:1)" is

## Cross-References

When scoring visual design, draw knowledge from:
- `visual-design-mastery` skill -> `visual-scoring-framework.md` — the scoring rubric and dimension definitions
- `visual-design-mastery` skill -> `designer-pattern-library.md` — designer references for prescriptions and benchmark comparisons
- `visual-design-mastery` skill -> `canonical-design-rules.md` — rule citations for every prescription
- `visual-design-mastery` skill -> `color-mastery.md` — color harmony evaluation, contrast verification
- `visual-design-mastery` skill -> `typography-mastery.md` — type scale evaluation, readability assessment
- `visual-design-mastery` skill -> `composition-mastery.md` — layout and spacing evaluation
- `ui-pattern-intelligence` skill — pattern quality assessment and benchmark products
- `sector-style-intelligence` skill — sector-specific visual expectations and norms
- `accessibility-inclusive-design` skill — WCAG contrast and motion requirements
- `interaction-motion-design` skill — motion quality evaluation
- `cognitive-psychology-ux` skill — perception science grounding for visual judgments

## Next Step

**Next** -> This is the final step in Phase 5. The journey cycles back to address findings.

**Alternatives**:
- `/vision` (1.6) — Generate or revise the visual direction based on scoring findings
- `/drip` (4.1) — Formalize design tokens to fix coherence and consistency issues
- `/ship [component]` (4.3) — Rebuild the lowest-scoring component with proper visual craft
- `/patterns` (1.5) — Re-run pattern analysis after visual improvements
- `/vibe-check` (2.1) — Heuristic audit to complement the visual score
- `/guide` — See the full journey map
