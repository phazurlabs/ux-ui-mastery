---
name: ai-ux-audit
description: Audit AI-powered features against agentic, trust, safety, and interaction best practices with scoring and specific fix recommendations.
argument-hint: [AI feature, file, or description]
---

# AI UX Audit Command

## Before running

This command needs the AI feature to audit — a file, a flow description, or a screenshot.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target, do not audit a hypothetical interface, and do not produce generic advice in place of the real analysis — an audit of something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.

Perform a comprehensive audit of AI-powered features against agentic AI, trust calibration, safety guardrail, and AI interaction best practices.

## Audit Protocol

1. **Identify AI Features**: Catalog all AI-powered features in the target (copilot, suggestions, generation, automation, agents, chat, search).

2. **Evaluate against four scoring dimensions**:

   **AI Trust Score (0-100)**
   - Is the AI's confidence level communicated to users?
   - Can users verify AI outputs against sources?
   - Does the system support calibrated trust (not over-trust or under-trust)?
   - Are AI limitations and error rates disclosed?
   - Is AI-generated content clearly labeled?
   - Does the system rebuild trust appropriately after errors?

   **AI Safety Score (0-100)**
   - Are guardrails implemented at appropriate risk tiers (informational/advisory/mandatory)?
   - Can users set constraints on AI autonomy?
   - Are high-risk actions gated behind explicit approval?
   - Is there undo/rollback for AI actions?
   - Are content filters and safety mechanisms in place?
   - Is sensitive data handled with appropriate privacy controls?

   **AI Usability Score (0-100)**
   - Is the AI interaction model appropriate for the task (chat vs. structured UI vs. generative)?
   - Does the prompt/input UX help users express intent effectively?
   - Are AI outputs rendered in a usable, scannable format?
   - Can users edit, refine, and iterate on AI outputs?
   - Is error recovery clear when AI fails or misunderstands?
   - Does the AI respect user preferences and learn appropriately?
   - Is the AI feature genuinely useful (not "AI slop")?

   **AI Accessibility Score (0-100)**
   - Do screen readers work with streaming AI output?
   - Are keyboard navigation patterns supported for copilot/suggestion UIs?
   - Are confidence indicators accessible (not color-only)?
   - Is AI-generated content accessible (alt text for images, structure for text)?
   - Do AI features work with assistive technology (voice control, switch access)?
   - Is focus management handled properly for dynamically generated content?

3. **For each finding, document**:
   - **Dimension**: Which scoring dimension (Trust, Safety, Usability, Accessibility)
   - **Feature**: Which AI feature is affected
   - **Issue**: Description of the problem
   - **Severity**: Critical (blocks users/causes harm), Major (significant friction), Minor (suboptimal), Enhancement (improvement opportunity)
   - **Recommendation**: Specific, actionable fix
   - **Code/design suggestion**: When applicable, provide corrected implementation

4. **Check for AI anti-patterns**:
   - AI fatigue: Are there unnecessary AI features that add complexity without value?
   - "AI slop": Is AI-generated content low quality or generic?
   - Forced AI: Are users required to use AI when direct manipulation would be faster?
   - Missing guardrails: Can the AI take high-risk actions without user approval?
   - Over-trust encouragement: Does the UI design discourage healthy skepticism?
   - Hallucination risk: Are users warned about potential AI errors in critical contexts?

## Output Format

```
## AI UX Audit Results

### Summary
- **Target**: [product/feature name]
- **AI Features Audited**: [list of AI features]
- **AI Trust Score**: [X/100]
- **AI Safety Score**: [X/100]
- **AI Usability Score**: [X/100]
- **AI Accessibility Score**: [X/100]
- **Overall AI UX Score**: [average/100]

### Critical & Major Findings
[Sorted by severity, grouped by dimension]

### AI Anti-Patterns Detected
[List of anti-patterns found with specific instances]

### Strengths
[What the AI UX does well]

### Recommendations
[Prioritized action items organized by effort and impact]

### AI Trust Improvement Roadmap
[Specific steps to improve trust calibration]
```

## Cross-References
When relevant issues are found, load additional context from:
- `agentic-ai-generative-ux` skill for agentic AI and generative UI patterns
- `accessibility-inclusive-design` skill for AI accessibility issues
- `ux-ethics-content-strategy` skill for AI content and ethical issues
- `ux-metrics-measurement` skill for measuring AI UX improvements
