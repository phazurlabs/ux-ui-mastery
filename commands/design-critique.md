---
name: design-critique
description: Conduct a structured design critique using the Liz Lerman Critical Response Process, scoring across 10 dimensions with heuristic-grounded feedback.
---

# Design Critique Command

Perform a structured design critique using proven critique methodology, scoring the design across multiple dimensions and generating actionable, evidence-based feedback.

## Critique Protocol

1. **Establish context**: Identify what is being critiqued and its design goals.
   - Design artifact type (wireframe, mockup, prototype, live product, code)
   - Target audience and user context
   - Design goals and constraints stated by the designer
   - Stage of design process (exploration, refinement, final review)

2. **Apply the Liz Lerman Critical Response Process**:

   **Step 1 — Statements of Meaning**: What is working well? What stands out positively? Begin with genuine strengths before addressing problems. This is not flattery — it identifies what to protect during iteration.

   **Step 2 — Designer's Questions**: If the designer has specific questions or areas of concern, address those first. Respect the designer's agency in directing the critique.

   **Step 3 — Neutral Questions**: Ask clarifying questions about design intent before making judgments. "I notice the navigation uses icons without labels — what informed that decision?" not "The icons need labels."

   **Step 4 — Permissioned Opinions**: Frame feedback as observations tied to evidence, not personal preference. Ground every opinion in heuristics, cognitive principles, or user evidence.

3. **Score across 10 dimensions** (each 1-10):

   | Dimension | What It Measures |
   |-----------|-----------------|
   | Clarity | Can users understand what to do without instruction? |
   | Consistency | Does it follow established patterns and conventions? |
   | Hierarchy | Is information prioritized visually and structurally? |
   | Efficiency | Can users accomplish goals with minimal friction? |
   | Accessibility | Does it work for users of all abilities? |
   | Emotional Design | Does it create appropriate emotional resonance? |
   | Error Resilience | Does it prevent errors and support recovery? |
   | Cognitive Load | Does it stay within working memory limits? |
   | Innovation | Does it solve problems in novel, valuable ways? |
   | Polish | Is the craft quality and attention to detail high? |

4. **Ground findings in evidence**:
   - Reference specific heuristics (H1-H10) when applicable
   - Cite cognitive psychology principles (Hick's Law, Fitts's Law, Gestalt)
   - Connect to user research findings when available
   - Identify dark patterns or ethical concerns if present

5. **Classify feedback by type**:
   - **Must-fix**: Issues that will cause user failure, accessibility violations, or ethical concerns
   - **Should-fix**: Issues that significantly degrade experience but don't block users
   - **Could-improve**: Opportunities to elevate from good to excellent
   - **Explore**: Open questions worth investigating through research or iteration

## Output Format

```
## Design Critique: [Design Name]

### Context
- **Artifact**: [type and description]
- **Stage**: [exploration / refinement / final]
- **Goals**: [stated design goals]

### Statements of Meaning (Strengths)
[3-5 specific strengths with reasoning]

### Dimension Scores
| Dimension | Score | Key Observation |
|-----------|-------|----------------|
[10 rows with scores and one-line observations]

**Overall Score**: [average]/10

### Findings

#### Must-Fix
[Issues with heuristic/principle grounding and specific recommendations]

#### Should-Fix
[Issues with evidence and recommendations]

#### Could-Improve
[Opportunities with rationale]

#### Explore
[Open questions for research or iteration]

### Recommended Next Steps
[Prioritized 3-5 action items with effort/impact classification]
```

## Cross-References
When critiquing designs, draw evaluation criteria from:
- `design-critique-case-studies` skill for critique methodology and case study benchmarks
- `nng-ux-heuristics` skill for heuristic violation identification
- `cognitive-psychology-ux` skill for cognitive load and bias analysis
- `accessibility-inclusive-design` skill for accessibility scoring
- `ux-ethics-content-strategy` skill for ethical design evaluation
- `ui-visual-design-system` skill for visual design quality assessment
