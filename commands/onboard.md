---
name: onboard
description: Onboarding flow builder — generate a complete onboarding sequence with progressive disclosure, activation metrics, and production React/TypeScript code.
user_invocable: true
---

# Onboard — Onboarding Flow Builder

Generate a complete, research-backed onboarding flow for any product type and sector, from first launch to activation moment.

## Discovery Protocol

1. **Gather product context**: Determine the product parameters before generating the flow.
   - **Product type**: Mobile app, web app, desktop app, SaaS platform, marketplace, or hybrid
   - **Sector**: Fintech, Healthcare, SaaS, Social, E-commerce, EdTech, Creator Tools, etc.
   - **Target user sophistication**: Novice (needs hand-holding), Intermediate (familiar with category), Expert (wants fast setup)
   - **Key value proposition**: The single sentence that explains why this product exists
   - **Critical first action (time-to-value)**: What must the user do to experience the core value?
   - **Platform constraints**: iOS, Android, Web, or cross-platform

2. **Determine onboarding archetype**: Select the optimal pattern based on product complexity and user sophistication.

   | Archetype | Best For | Steps | Completion Target |
   |-----------|----------|-------|-------------------|
   | Benefits-first | Consumer apps, low complexity | 3-4 screens | 90%+ |
   | Progressive | Medium complexity, feature-rich | 5-7 screens | 75-85% |
   | Setup wizard | High complexity, requires configuration | 7-12 screens | 60-75% |
   | Contextual | Power tools, expert users | Inline, no dedicated flow | N/A |
   | Hybrid | Marketplace, two-sided products | 4-6 screens + contextual | 70-80% |

3. **Generate step sequence**: Each step must include:
   - **Step number and title**: Clear, benefit-oriented heading
   - **Purpose**: What this step accomplishes for the user and for the product
   - **Content**: Headline, subtext, visual direction, and interaction type
   - **Progressive disclosure level**: What information is revealed vs. deferred
   - **Skip/defer option**: Whether this step can be skipped and the fallback experience
   - **Data captured**: What the product learns from this step
   - **Transition**: Animation and logic to advance to next step

4. **Permission request strategy**: Time every permission request for maximum grant rate.
   - Request only after demonstrating the feature that needs the permission
   - Pre-permission screen: explain the benefit before the system dialog
   - Fallback for denial: graceful degradation path, re-ask strategy (not immediately)
   - Permission copy: benefit-first language ("To send you price alerts" not "Allow notifications")

5. **Personalization questions**: Identify 2-4 questions that meaningfully customize the experience.
   - Each question must change the product experience in a visible way
   - Use selection UI (chips, cards, illustrations) not dropdowns or text input
   - Show immediate preview of how the selection affects the interface
   - Always include an "I'll decide later" escape hatch

6. **Empty state to first-value transition**: Design the critical moment between onboarding completion and first real content.
   - Empty state must teach, not just inform ("No messages yet" is bad; "Start a conversation with your team" with a CTA is good)
   - Seed with sample data, templates, or suggestions when appropriate
   - Celebrate the first completed action (confetti, success screen, progress update)
   - Remove onboarding scaffolding progressively as user gains competence

7. **Generate activation metrics framework**:
   - Step completion rate targets per screen
   - Time-to-value benchmark (seconds/minutes from install to first value moment)
   - Drop-off analysis points: where to instrument for funnel analysis
   - A/B test hypotheses: 3-5 testable variations with predicted impact

8. **Generate production code**: React/TypeScript component sequence.
   - Stepper/progress component with state management
   - Individual step components with enter/exit animations
   - Skip logic and conditional branching
   - Analytics event hooks at each step
   - Responsive layout (mobile-first, adapts to tablet/desktop)
   - Accessibility: screen reader announcements for step transitions, focus management

## Output Format

```
## Onboarding Flow: [Product Name]

### Flow Parameters
- **Product type**: [type]
- **Sector**: [sector]
- **Archetype**: [selected archetype with reasoning]
- **Target user**: [sophistication level]
- **Time-to-value target**: [X seconds/minutes]
- **Total steps**: [N]

### Flow Map
[Visual step sequence: Step 1 -> Step 2 -> ... -> Activation]
[Branch points and skip paths marked]

### Step-by-Step Breakdown
#### Step [N]: [Title]
- **Screen type**: [Welcome / Value Prop / Permission / Personalization / Setup / Activation]
- **Headline**: [benefit-oriented headline]
- **Subtext**: [supporting copy]
- **Interaction**: [tap to continue / select options / input field / permission dialog]
- **Skip option**: [Yes/No + fallback behavior]
- **Data captured**: [what the product learns]
- **Success criteria**: [what "completing" this step means]

[Repeated for each step]

### Permission Strategy
[Timing, copy, and fallback for each permission request]

### Empty State -> First Value
[Design for the moment after onboarding completes]

### React/TypeScript Implementation
[Complete component code with stepper, individual steps, state management, analytics hooks]

### Activation Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
[Completion rates, time-to-value, drop-off points]

### A/B Test Suggestions
[3-5 testable hypotheses with predicted impact]
```

## Cross-References
When building onboarding flows, draw patterns and principles from:
- `performance-states-patterns` skill for empty states, loading states, skeleton screens, and onboarding state transitions
- `cognitive-psychology-ux` skill for progressive disclosure, cognitive load management, and the peak-end rule in flow design
- `component-patterns-code` skill for React/SwiftUI/CSS implementation patterns for steppers, carousels, and form components
- `mobile-ux-design` skill for platform-specific onboarding conventions (iOS 26, Material 3)
- `interaction-motion-design` skill for step transition animations, celebration moments, and micro-interactions
- `ux-metrics-measurement` skill for activation metrics, funnel analysis, and A/B testing methodology

## Next Steps
After running `/onboard`, consider:
- `/flow` — Audit the generated onboarding flow for friction points and drop-off risks
- `/vibe-check` — Audit each individual onboarding screen against usability heuristics
- `/pulse` — Set up the activation metrics dashboard and measurement plan
- `/ship` — Build individual components (stepper, permission dialogs, celebration screens)
- `/include` — Verify the onboarding flow is accessible to all users
- `/brain-scan` — Check cognitive load across the flow to prevent overwhelm
