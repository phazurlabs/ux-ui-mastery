---
description: "[0.2] Design brief — define problem statement, persona, How Might We questions, success criteria, and constraint stack."
phase: "0"
phase_step: "0.2"
phase_name: "GROUND"
step_label: "Step 2 of 30"
---

# Intent — Problem Definition & Constraint Stack Generator

The most important 5 minutes of any build session. `/intent` transforms a vague idea into a structured design intent that makes every subsequent Sumi command dramatically more precise.

## Why This Exists

The #1 cause of "good-looking but useless" AI-generated UI is building without defining the problem. `/intent` forces the definition that makes the difference between:

- **Without intent**: "Generate a settings screen" → Generic, undifferentiated, solves no specific problem
- **With intent**: "Users who manage 10-person teams need role-based notification controls because current all-or-nothing settings cause alert fatigue" → Specific, testable, purpose-built

## Quick Intent (2 Minutes)

Short on time? Skip the full protocol. Answer three questions and get a usable Constraint Stack:

1. **Who + What**: "[Name] is a [role] who needs to [task] on [device]"
2. **Why**: "Because their current workaround is [X] and it fails because [Y]"
3. **Success**: "We'll know it works when [one measurable thing]"

That's enough. Sumi will generate the full output (persona, HMW questions, success criteria, Constraint Stack) from these three lines.

**Example — Quick Intent for an indie SaaS:**
```
1. Marcus is a freelance developer who needs to track project hours on his laptop
2. Because his current workaround is a spreadsheet and it fails because he forgets to log time
3. We'll know it works when 80% of hours are logged within 5 minutes of completing work
```

**Example — Quick Intent for a mobile app:**
```
1. Priya is a new mom who needs to track her baby's feeding schedule on her phone
2. Because her current workaround is Apple Notes and it fails because she can't see patterns
3. We'll know it works when she can identify feeding patterns in under 10 seconds
```

**Example — Quick Intent for a portfolio site:**
```
1. Jake is a hiring manager who needs to evaluate a designer's work on desktop
2. Because his current experience is clicking through 20 Dribbble shots and it fails because he can't assess process
3. We'll know it works when he can decide "interview or skip" in under 60 seconds
```

## Intent Protocol

1. **Gather raw intent from user**:

   Accept intent in any form — a sentence, a paragraph, a feature request, a bug report, a vague idea. The user doesn't need to know UX terminology. Examples of valid input:

   - "I want to build a dashboard"
   - "Our checkout flow has a 40% drop-off"
   - "Users keep asking for dark mode"
   - "I need a settings page for my SaaS app"
   - "We're building a health tracking app for seniors"
   - A pasted screenshot or component code
   - A Figma link or design spec

   If the user provides no specific intent, ask: "What are you building, and who is it for?"

2. **Challenge and refine the problem statement**:

   Transform raw intent into the structured format: **"Users who [X] need [Y] because [Z]"**

   **Challenge questions** (ask only the ones needed — don't interrogate):
   - "Who specifically will use this?" (push past "users" to a real archetype)
   - "What are they trying to accomplish?" (task, not feature)
   - "Why can't they do this today?" (current workaround reveals the real gap)
   - "What happens if they fail?" (stakes reveal priority)
   - "What does success look like for them?" (measurable outcome, not completion)

   **Refinement process**:
   - Start with the user's words
   - Identify the implied user, need, and reason
   - Draft the problem statement
   - Read it back and ask: "Does this capture what you're solving?"
   - Iterate once if needed

   **Example refinement**:
   ```
   Raw: "I want to build a dashboard"
   Challenge: "Who will use this dashboard, and what decisions will it help them make?"
   User: "Product managers tracking feature adoption"
   Challenge: "How do they track this today?"
   User: "They check 3 different analytics tools and make a spreadsheet"

   → Problem statement: "Product managers who track feature adoption need
     a unified metrics view because switching between 3 analytics tools and
     maintaining a manual spreadsheet costs 2 hours/week and delays decisions."
   ```

   **Alternative format — Jobs to Be Done (JTBD)**:

   If the "Users who X need Y because Z" format doesn't click, try JTBD:

   > "When [situation], I want to [motivation], so I can [expected outcome]."

   **Example**: "When I'm reviewing my team's pull requests at 6am before standup, I want to see which ones need my attention first, so I can unblock my team before the meeting starts."

   JTBD captures the *context* (when), the *desire* (want), and the *value* (so I can). Either format works — pick the one that feels more natural.

3. **Build lightweight persona**:

   Generate a concise persona based on the problem statement. Not a demographic profile — a behavioral archetype.

   ```
   ### Persona: [Name]
   **Role**: [What they do]
   **Context**: [Where and when they use this]
   **Goal**: [What they're trying to accomplish]
   **Frustration**: [What blocks them today]
   **Tech comfort**: [Novice / Intermediate / Power user]
   **Accessibility**: [Any known needs — vision, motor, cognitive, situational]
   **Device**: [Primary device and environment]
   ```

   **Guidelines**:
   - Use a realistic name (not "User A")
   - Focus on behavior, not demographics (age/gender matter only when they affect interaction patterns — e.g., vision needs for older users, thumb zones for younger mobile users)
   - Include situational accessibility (e.g., "uses app in bright sunlight," "often multitasking," "wears gloves")
   - One persona is enough for intent definition. More can come later in research.

4. **Generate 3-5 "How Might We" questions**:

   HMW questions reframe the problem as design opportunities. Each opens a different solution direction.

   **Rules for good HMW questions**:
   - Broad enough to allow multiple solutions
   - Narrow enough to be actionable
   - User-focused, not technology-focused
   - Start with "How might we..." (not "How can we..." — "might" implies possibility, not certainty)

   **Example** (for the dashboard problem):
   ```
   1. HMW consolidate 3 analytics tools into a single view without losing granularity?
   2. HMW help PMs identify underperforming features in under 30 seconds?
   3. HMW make adoption trends visible at a glance without requiring spreadsheet creation?
   4. HMW enable PMs to share adoption insights with stakeholders without exporting data?
   5. HMW surface actionable recommendations, not just data, from adoption metrics?
   ```

5. **Define success criteria**:

   Four categories of success, each with measurable criteria:

   **Functional success** — What must it do?
   - Core capabilities required
   - Data it must display/capture
   - Integrations required
   - Performance requirements (load time, refresh rate)

   **Usability success** — How fast and easy must it be?
   - Task completion time target
   - Error rate target
   - Learnability: time to first successful use
   - Efficiency: time for expert repeated use

   **Accessibility success** — Who must be able to use it?
   - WCAG level (AA minimum, AAA for specific criteria)
   - Persona Spectrum coverage (permanent, temporary, situational)
   - Input method support (mouse, keyboard, touch, voice, switch)
   - Minimum contrast, touch target, and text size requirements

   **Business success** — What outcome does this drive?
   - Adoption metric (% of target users who engage)
   - Retention metric (return usage rate)
   - Efficiency metric (time saved, errors reduced, tasks completed)
   - Revenue metric (if applicable — conversion, upsell, churn reduction)

6. **Generate the Constraint Stack**:

   The constraint stack is the key output — a structured block the user pastes into any subsequent Sumi BUILD command to carry intent forward.

   ```markdown
   ## Constraint Stack

   **Problem**: [Users who X need Y because Z]
   **Persona**: [Name, role, context, device, accessibility needs]
   **Success**:
     - Functional: [what it must do]
     - Usability: [how fast/easy — with metrics]
     - Accessibility: [WCAG level, persona spectrum, input methods]
     - Business: [adoption, retention, efficiency, revenue targets]
   **Platform**: [device, framework, design system constraints]
   **Style**: [sector, mood — or "run /taste to establish"]
   **Anti-goals**: [what this is NOT — 2-3 explicit exclusions]
   ```

   **Anti-goals are critical**: They prevent scope creep and keep AI generation focused. Examples:
   - "NOT a replacement for the existing analytics tools"
   - "NOT a real-time monitoring dashboard"
   - "NOT for external stakeholder consumption"

7. **Show how to use the Constraint Stack**:

   The Constraint Stack is only valuable if the user actually pastes it forward. Show them exactly how:

   ```
   ## How to Use Your Constraint Stack

   Copy the block above. Paste it into ANY Sumi BUILD command:

   /taste fintech
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
### Phase Position
> **Phase 0: GROUND** | Step 2 of 2 | `/intent`
> *NNG: Understand (Empathize + Define) | Problem Definition*
>
> `/ground` (0.1) → **`/intent` (0.2)** → `/taste` (1.1)

## Design Intent: [Short Title]

### Problem Statement
> Users who [X] need [Y] because [Z].

### Persona: [Name]
[Behavioral persona — role, context, goal, frustration, accessibility, device]

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
[Ready-to-paste block for BUILD commands]

### Recommended Next Steps
[Personalized roadmap based on intent]
```

## Cross-References

When defining intent, draw knowledge from:
- `ux-process-workflow` skill for NNG Empathize + Define methodology
- `ux-research-methods` skill for persona construction and problem framing techniques
- `cognitive-psychology-ux` skill for understanding user mental models and cognitive constraints
- `ux-metrics-measurement` skill for success criteria frameworks (HEART, SUS, task-based metrics)
- `accessibility-inclusive-design` skill for Persona Spectrum and inclusive success criteria
- `ux-ethics-content-strategy` skill for ethical framing of the problem space
- `sector-style-intelligence` skill for sector-specific user expectations and conventions

## Next Step

**Next** → `/taste` (1.1) — Establish your visual style direction for the sector

**Alternatives**:
- `/inspo` (1.2) — Find patterns for the screen type you're building
- `/drip` (4.1) — Jump to token system if you already have a style direction
- `/ship` (4.3) — Jump to BUILD if time-critical (paste your Constraint Stack into the prompt)
- `/guide` — See the full 22-step journey across all 6 phases

**Remember**: The Constraint Stack is your superpower. It's the difference between "generate a settings screen" (generic) and "generate a settings screen for Maria, a product manager who configures team notifications on her laptop, success = under 3 minutes for 10 people, WCAG AA, not a replacement for Slack preferences" (fire). Paste it everywhere.
