---
description: Redesign and improve — take any existing screen or component and generate a UX-grounded redesign with before/after reasoning for every change.
phase: "5"
phase_step: "5.2"
phase_name: "LAUNCH"
step_label: "Step 2 of 3"
---

# Remix — Redesign & Improve

Take an existing screen, component, or flow and redesign it with explicit UX reasoning for every single change. No change without a citation.

## Remix Protocol

1. **Accept the input**: Determine what is being remixed and establish baseline context.
   - **Input types accepted**: Existing code (React/SwiftUI/CSS/HTML), screenshot description, component specification, wireframe description, or live product URL description
   - **Identify the component/screen scope**: What exactly is being redesigned
   - **Gather context**: What does the user want improved? Are there specific pain points? What are the constraints (brand, platform, tech stack)?
   - **Establish the platform**: React/TypeScript, SwiftUI, CSS/HTML, or specify

2. **Step 1 — Quick Roast**: Identify the top 5 UX problems before touching anything.

   For each problem found, document:
   - **Problem**: Clear description of the issue
   - **Location**: Exact element or area affected
   - **Severity**: Critical (blocks users) / Major (frustrates users) / Minor (suboptimal) / Cosmetic (polish)
   - **Principle violated**: The specific heuristic, law, or principle being broken
   - **User impact**: What happens to the user because of this problem
   - **Evidence**: Why this is a problem, not a preference

   Common problems to scan for:
   - Unclear hierarchy (no visual priority, everything competes for attention)
   - Missing states (no loading, error, empty, or disabled states)
   - Accessibility failures (contrast, touch targets, keyboard, screen reader)
   - Cognitive overload (too many choices, too much information, unclear next action)
   - Inconsistent patterns (mixed interaction models, mismatched styling)
   - Dark patterns or manipulative design (shame clicks, hidden costs, forced actions)
   - Performance UX gaps (no skeleton loading, no optimistic updates, blocking spinners)

3. **Step 2 — Redesign**: Generate the improved version addressing every identified problem.
   - Solve each of the 5 problems explicitly — no problem left behind
   - Maintain the original design intent and brand character
   - Introduce no new problems while fixing existing ones
   - Apply progressive enhancement: the redesign should work at every fidelity level
   - Include all relevant states (default, hover, focus, active, disabled, loading, error, success, empty)
   - Build with accessibility from the ground up, not bolted on

4. **Step 3 — Change Log with UX Reasoning**: For every change made, explain why.

   Format each change as:
   - **Change**: [What was changed]
   - **Before**: [How it was]
   - **After**: [How it is now]
   - **Principle**: [The UX law, heuristic, or research that justifies this change]
   - **Expected impact**: [What metric or behavior this should improve]

   Principles to cite (use specific names, not vague references):
   - Nielsen's Heuristics (H1-H10)
   - Fitts's Law (target size and distance)
   - Hick's Law (decision time vs. number of choices)
   - Jakob's Law (users prefer familiar patterns)
   - Miller's Law (7 plus or minus 2 chunks)
   - Von Restorff Effect (isolation makes items memorable)
   - Serial Position Effect (primacy and recency)
   - Gestalt Principles (proximity, similarity, continuity, closure, common region)
   - WCAG 2.2 Success Criteria (specific criterion numbers)
   - Peak-End Rule (experience judged by peak moment and ending)

5. **Step 4 — Before/After Comparison**: Summarize the full transformation.
   - Side-by-side structural comparison
   - Predicted metric improvements with reasoning
   - Risk assessment: what could go wrong with the redesign
   - Validation recommendations: how to test that the remix is actually better

## Output Format

```
### Phase Position
> **Phase 5: LAUNCH** | Step 2 of 3 | `/remix`
> *NNG: Iterative Design | Visual: Redesign & Polish*
>
> `/roast` (5.1) → **`/remix` (5.2)** → `/judge` (5.3)

## Remix: [Component/Screen Name]

### Input Analysis
- **Type**: [code / screenshot / specification]
- **Platform**: [React / SwiftUI / CSS / Web]
- **Current state**: [brief description of what was provided]

### Quick Roast (Top 5 Problems)

| # | Problem | Severity | Principle Violated |
|---|---------|----------|--------------------|
| 1 | [problem] | [Critical/Major/Minor/Cosmetic] | [principle] |
| 2 | [problem] | [severity] | [principle] |
| 3 | [problem] | [severity] | [principle] |
| 4 | [problem] | [severity] | [principle] |
| 5 | [problem] | [severity] | [principle] |

### Redesigned Code
[Complete production-ready code with all states, accessibility, and tokens]

### Change Log

#### Change 1: [Name]
- **Before**: [description]
- **After**: [description]
- **Principle**: [specific citation]
- **Expected impact**: [metric prediction]

[Repeated for each change]

### Before/After Summary
| Dimension | Before | After | Predicted Improvement |
|-----------|--------|-------|-----------------------|
| Clarity | [score] | [score] | [reasoning] |
| Accessibility | [score] | [score] | [reasoning] |
| Efficiency | [score] | [score] | [reasoning] |
| Error handling | [score] | [score] | [reasoning] |
| Visual polish | [score] | [score] | [reasoning] |

### Validation Plan
[How to test that the remix is actually an improvement]
```

## Cross-References
When remixing designs, draw principles and patterns from:
- `nng-ux-heuristics` skill for heuristic evaluation and violation identification
- `cognitive-psychology-ux` skill for cognitive load analysis, bias identification, and decision architecture
- `component-patterns-code` skill for production-ready implementation patterns in React, SwiftUI, and CSS
- `interaction-motion-design` skill for animation improvements, micro-interactions, and transition design
- `accessibility-inclusive-design` skill for WCAG compliance fixes and inclusive design improvements
- `ui-visual-design-system` skill for visual hierarchy, spacing, typography, and color improvements
- `performance-states-patterns` skill for loading, error, empty, and skeleton state additions

## Next Step

**Next** → `/judge` (5.3) — Run the final comprehensive review

**Alternatives**:
- `/roast` (5.1) — Loop back for another critique of the redesign
- `/ship` (4.3) — Go back to BUILD to rebuild specific components
- `/guide` — See the full 20-step journey
