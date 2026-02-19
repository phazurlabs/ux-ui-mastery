---
description: Comprehensive design review scoring a UI across all 21 skill domains with detailed feedback and improvement roadmap.
phase: "5"
phase_step: "5.3"
phase_name: "LAUNCH"
step_label: "Step 3 of 3"
---

# Judge — Full Design Review

Perform a comprehensive design review evaluating the provided UI across all UX/UI skill domains.

## Review Protocol

1. **Identify the target**: Determine the component, screen, flow, or application to review.

2. **Score each domain** (1-10 scale):

| Domain | What to Evaluate |
|--------|-----------------|
| Heuristic Compliance | Nielsen's 10 heuristics adherence |
| Research Foundation | Evidence of user-centered design decisions |
| Mobile Experience | Touch targets, responsive behavior, mobile patterns |
| Desktop Experience | Information density, keyboard support, workflow efficiency |
| Visual Design | Typography, color, spacing, hierarchy, consistency |
| Accessibility | WCAG compliance, keyboard nav, screen reader support |
| Interaction Design | Micro-interactions, transitions, feedback, loading states |
| Future-Readiness | AI integration, spatial awareness, multimodal support |
| System Architecture | Design tokens, component reusability, theming |
| Ethics & Content | Dark pattern avoidance, content quality, inclusive language |

3. **For each domain, provide**:
   - Score (1-10) with brief justification
   - Top strength in this domain
   - Top improvement opportunity
   - Specific recommendation with implementation guidance

4. **Generate overall assessment**:
   - Weighted overall score
   - Radar chart data (for visualization)
   - Priority improvement roadmap (Quick wins -> Medium effort -> Strategic)

## Output Format

```
### Phase Position
> **Phase 5: LAUNCH** | Step 3 of 3 | `/judge`
> *NNG: Summative Evaluation | Visual: Launch Certification*
>
> `/remix` (5.2) → **`/judge` (5.3)** → **COMPLETE** or loop → `/drip` (4.1)

## Design Review Results

### Overall Score: [X/100]

### Domain Scores
[Table with all 10 domains, scores, and one-line summaries]

### Top 3 Strengths
[What the design excels at]

### Priority Improvements

#### Quick Wins (< 1 day effort)
[List with specific actions]

#### Medium Effort (1-5 days)
[List with specific actions]

#### Strategic (1+ weeks)
[List with specific actions]

### Detailed Domain Analysis
[Expandable sections for each domain]
```

## Next Step

**Phase 5: LAUNCH complete.** All 21 domains scored. You have a launch readiness assessment.

**If all scores 7+ and no must-fix findings** → Ship it.

**If scores need work** → Loop back to **Phase 4: BUILD** — Start with `/drip` (4.1) or `/ship` (4.3)

**Quality loop**: `/roast` (5.1) → `/remix` (5.2) → `/ship` (4.3) → `/roast` (5.1) — repeat until quality bar met.

- `/guide` — See the full 20-step journey
