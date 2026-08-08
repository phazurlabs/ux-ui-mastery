---
description: "Problem definition — persona, How Might We questions, constraints, success criteria, and a ready-to-paste Constraint Stack."
tier: "plan"
---

# Brief — Problem Definition & Constraint Stack

The most important 5 minutes of any build session. `/brief` transforms a vague idea into a structured design intent that makes every subsequent Sumi command dramatically more precise.

## Why This Matters

The difference between generic output and great output:

- **Without brief**: "Generate a settings screen" -- Generic, undifferentiated, solves no specific problem
- **With brief**: "Users who manage 10-person teams need role-based notification controls because current all-or-nothing settings cause alert fatigue" -- Specific, testable, purpose-built

## Quick Brief (2 Minutes)

Short on time? Answer three questions:

1. **Who + What**: "[Name] is a [role] who needs to [task] on [device]"
2. **Why**: "Because their current workaround is [X] and it fails because [Y]"
3. **Success**: "We'll know it works when [one measurable thing]"

Sumi generates the full output (persona, HMW questions, success criteria, Constraint Stack) from these three lines.

**Example -- indie SaaS:**
```
1. Marcus is a freelance developer who needs to track project hours on his laptop
2. Because his current workaround is a spreadsheet and it fails because he forgets to log time
3. We'll know it works when 80% of hours are logged within 5 minutes of completing work
```

**Example -- mobile app:**
```
1. Priya is a new mom who needs to track her baby's feeding schedule on her phone
2. Because her current workaround is Apple Notes and it fails because she can't see patterns
3. We'll know it works when she can identify feeding patterns in under 10 seconds
```

**Example -- portfolio site:**
```
1. Jake is a hiring manager who needs to evaluate a designer's work on desktop
2. Because his current experience is clicking through 20 Dribbble shots and it fails because he can't assess process
3. We'll know it works when he can decide "interview or skip" in under 60 seconds
```

## Full Brief Protocol

### Step 1: Gather Raw Intent

Accept intent in any form -- a sentence, a paragraph, a feature request, a bug report, a vague idea. Examples of valid input:

- "I want to build a dashboard"
- "Our checkout flow has a 40% drop-off"
- "Users keep asking for dark mode"
- "I need a settings page for my SaaS app"
- "We're building a health tracking app for seniors"
- A pasted screenshot or component code
- A Figma link or design spec

If no specific intent is provided, ask: "What are you building, and who is it for?"

### Step 2: Refine the Problem Statement

Transform raw intent into: **"Users who [X] need [Y] because [Z]"**

**Ask only what's needed** (do not interrogate):
- "Who specifically will use this?" (push past "users" to a real archetype)
- "What are they trying to accomplish?" (task, not feature)
- "Why can't they do this today?" (current workaround reveals the real gap)
- "What happens if they fail?" (stakes reveal priority)
- "What does success look like for them?" (measurable outcome, not completion)

**Example refinement**:
```
Raw: "I want to build a dashboard"
Challenge: "Who will use this dashboard, and what decisions will it help them make?"
User: "Product managers tracking feature adoption"
Challenge: "How do they track this today?"
User: "They check 3 different analytics tools and make a spreadsheet"

Problem statement: "Product managers who track feature adoption need
  a unified metrics view because switching between 3 analytics tools and
  maintaining a manual spreadsheet costs 2 hours/week and delays decisions."
```

**Alternative format -- Jobs to Be Done (JTBD)**:

If "Users who X need Y because Z" doesn't click, try:

> "When [situation], I want to [motivation], so I can [expected outcome]."

Example: "When I'm reviewing my team's pull requests at 6am before standup, I want to see which ones need my attention first, so I can unblock my team before the meeting starts."

Either format works -- pick the one that feels more natural.

### Step 3: Build Persona

Generate a concise behavioral persona. Not demographics -- behavior.

```
### Persona: [Name]
**Role**: [What they do]
**Context**: [Where and when they use this]
**Goal**: [What they're trying to accomplish]
**Frustration**: [What blocks them today]
**Tech comfort**: [Novice / Intermediate / Power user]
**Accessibility**: [Any known needs -- vision, motor, cognitive, situational]
**Device**: [Primary device and environment]
```

Guidelines:
- Use a realistic name (not "User A")
- Focus on behavior, not demographics
- Include situational accessibility (e.g., "uses app in bright sunlight," "often multitasking")
- One persona is enough for this step

### Step 4: Generate How Might We Questions (3-5)

HMW questions reframe the problem as design opportunities. Each opens a different solution direction.

Rules:
- Broad enough to allow multiple solutions
- Narrow enough to be actionable
- User-focused, not technology-focused
- Start with "How might we..." (not "How can we..." -- "might" implies possibility)

**Example** (for the dashboard problem):
```
1. HMW consolidate 3 analytics tools into a single view without losing granularity?
2. HMW help PMs identify underperforming features in under 30 seconds?
3. HMW make adoption trends visible at a glance without requiring spreadsheet creation?
4. HMW enable PMs to share adoption insights with stakeholders without exporting data?
5. HMW surface actionable recommendations, not just data, from adoption metrics?
```

### Step 5: Define Success Criteria

Four categories, each with measurable targets:

**Functional** -- What must it do?
- Core capabilities required
- Data it must display/capture
- Integrations required
- Performance requirements

**Usability** -- How fast and easy must it be?
- Task completion time target
- Error rate target
- Learnability: time to first successful use
- Efficiency: time for expert repeated use

**Accessibility** -- Who must be able to use it?
- WCAG level (AA minimum, AAA for specific criteria)
- Persona Spectrum coverage (permanent, temporary, situational)
- Input method support (mouse, keyboard, touch, voice, switch)
- Minimum contrast, touch target, and text size requirements

**Business** -- What outcome does this drive?
- Adoption metric (% of target users who engage)
- Retention metric (return usage rate)
- Efficiency metric (time saved, errors reduced)
- Revenue metric (if applicable -- conversion, upsell, churn reduction)

### Step 6: Generate the Constraint Stack

The key output -- a structured block the user pastes into any subsequent Sumi command.

```markdown
## Constraint Stack

**Problem**: [Users who X need Y because Z]
**Persona**: [Name, role, context, device, accessibility needs]
**Success**:
  - Functional: [what it must do]
  - Usability: [how fast/easy -- with metrics]
  - Accessibility: [WCAG level, persona spectrum, input methods]
  - Business: [adoption, retention, efficiency, revenue targets]
**Platform**: [device, framework, design system constraints]
**Style**: [sector, mood -- or "run /style to establish"]
**Anti-goals**: [what this is NOT -- 2-3 explicit exclusions]
```

**Anti-goals are critical**: They prevent scope creep and keep generation focused. Examples:
- "NOT a replacement for the existing analytics tools"
- "NOT a real-time monitoring dashboard"
- "NOT for external stakeholder consumption"

### Step 7: Show How to Use It

```
## How to Use Your Constraint Stack

Copy the block above. Paste it into ANY Sumi command:

/style fintech
[paste constraint stack]

/screen dashboard
[paste constraint stack]

/ship notification-card
[paste constraint stack]

Every command becomes 10x more precise when it knows your
problem, persona, success criteria, and anti-goals.

Pro tip: Save the Constraint Stack as a comment at the top
of your project's main file. Reference it every build session.
```

## Output Format

```
## Design Brief: [Short Title]

### Problem Statement
> Users who [X] need [Y] because [Z].

### Persona: [Name]
[Behavioral persona -- role, context, goal, frustration, accessibility, device]

### How Might We...
1. HMW [opportunity question]?
2. HMW [opportunity question]?
3. HMW [opportunity question]?
4. HMW [opportunity question]?
5. HMW [opportunity question]?

### Success Criteria

| Category | Criterion | Target |
|----------|-----------|--------|
| Functional | [capability] | [measurable target] |
| Usability | [task time / error rate / learnability] | [measurable target] |
| Accessibility | [WCAG level / input methods] | [measurable target] |
| Business | [adoption / retention / efficiency] | [measurable target] |

### Constraint Stack
[Ready-to-paste block]

### How to Use Your Constraint Stack
[Usage instructions with examples]

### Recommended Next Steps
- `/style [sector]` -- Establish visual direction
- `/benchmark` -- Study your competition
- `/map` -- Plan your information architecture
```

## Quality Gates

The output MUST include:
- [ ] Problem statement in "Users who X need Y because Z" or JTBD format
- [ ] Behavioral persona with role, context, goal, frustration, device
- [ ] 3-5 HMW questions that open different solution directions
- [ ] Success criteria across all four categories with measurable targets
- [ ] Complete Constraint Stack ready to paste into other commands
- [ ] Anti-goals (2-3 explicit exclusions)
- [ ] Usage instructions showing how to carry the Constraint Stack forward

The output MUST NOT include:
- Demographic-only personas without behavioral detail
- Yes/no success criteria (everything must be measurable)
- Generic HMW questions not tailored to the specific problem
- Missing anti-goals (scope creep is the enemy)

## Cross-References

When defining the brief, draw knowledge from:
- `ux-process-workflow` skill for problem framing methodology
- `ux-research-methods` skill for persona construction techniques
- `cognitive-psychology-ux` skill for understanding user mental models
- `ux-metrics-measurement` skill for success criteria frameworks (HEART, SUS)
- `accessibility-inclusive-design` skill for Persona Spectrum and inclusive criteria
- `sector-style-intelligence` skill for sector-specific user expectations

## Next Step

**Next** --> `/style` -- Establish your visual direction for the sector

**Alternatives**:
- `/research` -- Plan user research to validate your assumptions
- `/benchmark` -- Study your competition
- `/screen [type]` -- Jump straight to building if time is critical (paste your Constraint Stack)
- `/sumi` -- See the full command map
