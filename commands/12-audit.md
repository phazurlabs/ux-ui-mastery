---
description: "[3.1] Heuristic audit — evaluate any UI against Nielsen's 10 usability heuristics with severity ratings and actionable recommendations."
phase: "3"
phase_step: "3.1"
phase_name: "AUDIT"
step_label: "Step 12 of 30"
---

# Vibe Check — UX Heuristic Audit

Perform a comprehensive UX audit using Nielsen's 10 usability heuristics against the provided code, component, or screen description.

## Audit Protocol

1. **Gather context and design intent**: Before auditing, understand what the designer intended. (Following Liz Lerman's "respect the designer" protocol — understand intent before critiquing.)
   - **What is being audited**: Component, screen, flow, or full application
   - **Design intent**: What was the designer trying to achieve? What problem does this solve?
   - **Target users**: Who uses this? What is their sophistication level and context?
   - **Sector**: What industry? Sector conventions affect what counts as a violation vs. an intentional choice
   - **Constraints**: What trade-offs were the designer working within? (timeline, technical, business)
   - **Prior Sumi outputs**: Check for `/taste`, `/inspo`, `/benchmark`, `/brain-scan` outputs. If available, use them as baseline context
   - **Specific concerns**: Does the designer have areas they already suspect are weak? Prioritize those

2. **Evaluate against each heuristic** (H1-H10):
   - H1: Visibility of System Status
   - H2: Match Between System and Real World
   - H3: User Control and Freedom
   - H4: Consistency and Standards
   - H5: Error Prevention
   - H6: Recognition Rather Than Recall
   - H7: Flexibility and Efficiency of Use
   - H8: Aesthetic and Minimalist Design
   - H9: Help Users Recognize, Diagnose, and Recover from Errors
   - H10: Help and Documentation

3. **For each finding, document with principle grounding**:
   - **Heuristic violated**: Which of the 10 heuristics
   - **Underlying cognitive principle**: Every heuristic violation has a deeper cognitive reason — cite it:
     - H1 violation → Doherty Threshold (system feels unresponsive) or Zeigarnik Effect (incomplete tasks create anxiety)
     - H2 violation → Mental Model theory (interface doesn't match user's existing understanding)
     - H5 violation → Cognitive Load Theory (user is forced to hold too much in working memory to avoid errors)
     - H6 violation → Miller's Law (interface demands recall of >7 items instead of showing them)
     - H8 violation → Signal-to-Noise Ratio (irrelevant information competes with relevant information)
   - **Location**: Where in the interface the issue occurs
   - **Description**: What the problem is
   - **Severity**: 0 (cosmetic) to 4 (catastrophe)
   - **Recommendation**: Specific, actionable fix
   - **Code suggestion**: When applicable, provide corrected code

4. **Mental model check**: Verify whether the interface communicates a clear, correct mental model to the user.
   - **Conceptual model**: Does the interface clearly communicate what this system is and how it works?
   - **Navigational model**: Can the user predict where actions will take them? Is the information architecture intuitive?
   - **Interaction model**: Do controls behave the way the user expects based on their appearance? (e.g., does something that looks clickable respond to clicks?)
   - **Model gaps**: Where does the interface's model diverge from the user's likely expectation? Flag these as **high-severity** — mental model mismatches cause the deepest usability failures
   - Reference: `cognitive-psychology-ux` skill — mental model theory (Norman, 1988)

5. **Generate summary**:
   - Total findings count by severity
   - Top 3 priority fixes
   - Overall usability score (1-100)
   - Strengths identified

## Output Format

```
### Phase Position
> **Phase 2: DIAGNOSE** | Step 1 of 4 | `/vibe-check`
> *NNG: Heuristic Evaluation | Visual: Quality Assessment*
>
> **Phase 1** `/pulse` (1.4) → **`/vibe-check` (2.1)** → `/brain-scan` (2.2)

## Vibe Check Results

### Context & Design Intent
- **Target**: [component/screen name]
- **Design intent**: [What the designer was trying to achieve]
- **Target users**: [Who, sophistication, context]
- **Sector**: [Industry and relevant conventions]
- **Constraints noted**: [Trade-offs the designer was working within]

### Summary
- **Overall Score**: [X/100]
- **Findings**: [X critical, X major, X minor, X cosmetic]
- **Mental Model**: [Clear / Gaps detected — brief summary]

### Critical & Major Findings
[Sorted by severity, then by frequency]

### Principle Grounding
| Finding | Heuristic | Cognitive Principle | Why This Matters |
|---------|-----------|-------------------|-----------------|
| [Finding 1] | H[N] | [Principle name] | [Why the cognitive principle makes this a real user problem] |
| [Finding 2] | H[N] | [Principle name] | [Why] |
| [...] | [...] | [...] | [...] |

### Mental Model Assessment
- **Conceptual model**: [Clear/Unclear — explanation]
- **Navigational model**: [Predictable/Unpredictable — explanation]
- **Interaction model**: [Consistent/Inconsistent — explanation]
- **Model gaps identified**: [List any mismatches between likely user expectation and actual behavior — these are high-severity]

### Strengths
[What the design does well]

### Recommendations
[Prioritized action items with effort estimates]

### Prior Output Integration
- **Prior audits consumed**: [List any `/brain-scan`, `/include`, `/benchmark` outputs used as context]
- **Missing context**: [List any prior outputs that would improve this audit if available]
```

## Cross-References
When relevant issues are found, load additional context from:
- `cognitive-psychology-ux` skill for mental model theory, cognitive load, Fitts's Law, Hick's Law, and perceptual principles
- `nng-ux-heuristics` skill for detailed heuristic evaluation methodology and severity rating framework
- `sector-style-intelligence` skill for sector-specific conventions that affect what counts as a violation
- `accessibility-inclusive-design` skill for a11y issues
- `mobile-ux-design` skill for mobile-specific issues
- `ui-visual-design-system` skill for visual design issues
- `interaction-motion-design` skill for animation/interaction issues

## Next Step

**Next** → `/brain-scan` (2.2) — Go deeper into cognitive load and decision architecture

**Alternatives**:
- `/include` (2.3) — Skip ahead to accessibility audit
- `/remix` (5.2) — Fix the issues found immediately
- `/guide` — See the full 20-step journey
