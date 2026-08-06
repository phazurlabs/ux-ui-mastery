---
name: ux-audit
description: Audit any UI component, screen, or codebase against NNG's 10 usability heuristics with severity ratings and actionable recommendations.
---

# UX Audit Command

Perform a comprehensive UX audit using Nielsen's 10 usability heuristics against the provided code, component, or screen description.

## Audit Protocol

1. **Identify the target**: Determine what is being audited (component, screen, flow, or full application).

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

3. **For each finding, document**:
   - **Heuristic violated**: Which of the 10 heuristics
   - **Location**: Where in the interface the issue occurs
   - **Description**: What the problem is
   - **Severity**: 0 (cosmetic) to 4 (catastrophe)
   - **Recommendation**: Specific, actionable fix
   - **Code suggestion**: When applicable, provide corrected code

4. **Generate summary**:
   - Total findings count by severity
   - Top 3 priority fixes
   - Overall usability score (1-100)
   - Strengths identified

## Output Format

```
## UX Audit Results

### Summary
- **Target**: [component/screen name]
- **Overall Score**: [X/100]
- **Findings**: [X critical, X major, X minor, X cosmetic]

### Critical & Major Findings
[Sorted by severity, then by frequency]

### Strengths
[What the design does well]

### Recommendations
[Prioritized action items with effort estimates]
```

## Cross-References
When relevant issues are found, load additional context from:
- `accessibility-inclusive-design` skill for a11y issues
- `mobile-ux-design` skill for mobile-specific issues
- `ui-visual-design-system` skill for visual design issues
- `interaction-motion-design` skill for animation/interaction issues
