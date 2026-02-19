---
description: Onboarding flow builder — generate a complete onboarding sequence with progressive disclosure, activation metrics, and production React/TypeScript code.
phase: "4"
phase_step: "4.4"
phase_name: "BUILD"
step_label: "Step 4 of 5"
---

# Onboard — Onboarding Flow Builder

Generate a complete, research-backed onboarding flow for any product type and sector, from first launch to activation moment.

## Discovery Protocol

1. **Gather product context and constraints**: Determine the product parameters before generating the flow.
   - **Product type**: Mobile app, web app, desktop app, SaaS platform, marketplace, or hybrid
   - **Sector**: Fintech, Healthcare, SaaS, Social, E-commerce, EdTech, Creator Tools, etc.
   - **Target user sophistication**: Novice (needs hand-holding), Intermediate (familiar with category), Expert (wants fast setup)
   - **Key value proposition**: The single sentence that explains why this product exists
   - **Critical first action (time-to-value)**: What must the user do to experience the core value?
   - **Platform constraints**: iOS, Android, Web, or cross-platform
   - **Prior Sumi outputs**: Check for `/taste` (style direction to apply to onboarding UI), `/pulse` (HEART metrics and activation targets to inform completion goals). If available, consume them. If not, use sensible defaults and note what's missing
   - **Mental model assumption**: What does the user think this product is before they start onboarding? (e.g., "another note-taking app" vs. "a knowledge graph") — mismatches between the user's mental model and the actual product must be corrected during onboarding

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
   - **Cognitive load budget**: Each step must respect working memory limits:
     - Maximum **2 decisions** per step (Hick's Law — more choices = more drop-off)
     - Maximum **5 items** in working memory at any point (Miller's Law)
     - Count and document: how many new concepts, options, and inputs does this step introduce?

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

7. **Design peak and end moments**: Apply the Peak-End Rule (Kahneman) — users judge an experience by its most intense moment and its ending, not the average.

   - **Identify the peak moment ("aha!")**: Which step delivers the biggest value revelation? Design it to feel magical — visual delight, instant payoff, or surprising personalization
   - **Design the celebration**: The moment after the peak action should include a micro-celebration (confetti, animation, success copy) — this anchors positive memory
   - **Design the final screen**: The last onboarding screen is disproportionately important. End on a positive, empowering note — show the user what they've accomplished, not what's left
   - **Anti-pattern warning**: NEVER end onboarding on a permissions request, a paywall, or an error state. These create negative final impressions that bias the entire memory of onboarding

8. **Generate activation metrics framework**:
   - Step completion rate targets per screen
   - Time-to-value benchmark (seconds/minutes from install to first value moment)
   - Drop-off analysis points: where to instrument for funnel analysis
   - A/B test hypotheses: 3-5 testable variations with predicted impact

9. **Generate production code**: React/TypeScript component sequence.
   - Stepper/progress component with state management
   - Individual step components with enter/exit animations
   - Skip logic and conditional branching
   - Analytics event hooks at each step
   - Responsive layout (mobile-first, adapts to tablet/desktop)
   - Accessibility: screen reader announcements for step transitions, focus management
   - **Heuristic compliance** — verify each of these in the generated code:
     - H1 (System Status): Progress indicator shows current step and total
     - H3 (User Control): Back button and skip option on every non-critical step
     - H4 (Consistency): Step layout, button placement, and animation style are consistent
     - H5 (Error Prevention): Inline validation on inputs; sensible defaults pre-filled
     - H6 (Recognition > Recall): Use visual selectors (chips, cards) not free-text input
     - H8 (Minimalist Design): Each step has only what's needed — no extra UI
     - H10 (Help): Contextual help text available on complex steps

## Output Format

```
### Phase Position
> **Phase 4: BUILD** | Step 4 of 5 | `/onboard`
> *NNG: Onboarding Design | Visual: Activation Flow*
>
> `/ship` (4.3) → **`/onboard` (4.4)** → `/extract` (4.5)

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

### Peak and End Design
- **Peak moment (aha!)**: Step [N] — [description of the peak moment and why it's the highest-value revelation]
- **Celebration design**: [What happens after the peak — animation, copy, visual feedback]
- **Final screen**: [Description of the last onboarding screen and why it creates a positive final impression]
- **Anti-patterns avoided**: [What the flow deliberately does NOT end on — permissions, paywalls, etc.]

### Cognitive Load per Step
| Step | Decisions Required | Working Memory Items | New Concepts | Status |
|------|-------------------|---------------------|-------------|--------|
| 1 | [N] (max 2) | [N] (max 5) | [N] | [OK/Over] |
| 2 | [N] (max 2) | [N] (max 5) | [N] | [OK/Over] |
| [...]| [...] | [...] | [...] | [...] |

### Heuristic Compliance Checklist
- [ ] H1: Progress indicator visible on every step
- [ ] H3: Back and skip available on non-critical steps
- [ ] H4: Consistent layout and interaction patterns across steps
- [ ] H5: Inline validation; sensible defaults pre-filled
- [ ] H6: Visual selectors (chips, cards) used instead of free text where possible
- [ ] H8: Each step contains only essential content
- [ ] H10: Help text available on complex steps

### Design Decision Rationale
| Decision | Choice Made | Principle | Why |
|----------|------------|-----------|-----|
| Archetype | [choice] | [principle] | [reasoning] |
| Step count | [N] steps | Cognitive Load Theory | [reasoning] |
| [...]    | [...]      | [...]     | [...] |

### Prior Output Integration
- **`/taste` consumed**: [Yes/No — if yes, list what was used: palette, motion, tone for onboarding UI]
- **`/pulse` consumed**: [Yes/No — if yes, list activation targets and HEART metrics applied]
- **Missing context**: [List any Phase 1 outputs that would improve this flow if run]
```

## Cross-References
When building onboarding flows, draw patterns and principles from:
- `performance-states-patterns` skill for empty states, loading states, skeleton screens, and onboarding state transitions
- `cognitive-psychology-ux` skill for progressive disclosure, cognitive load management, and the peak-end rule in flow design
- `component-patterns-code` skill for React/SwiftUI/CSS implementation patterns for steppers, carousels, and form components
- `mobile-ux-design` skill for platform-specific onboarding conventions (iOS 26, Material 3)
- `interaction-motion-design` skill for step transition animations, celebration moments, and micro-interactions
- `ux-metrics-measurement` skill for activation metrics, funnel analysis, and A/B testing methodology

## Next Step

**Next** → `/extract` (4.5) — Bridge your Figma designs to production code

**Alternatives**:
- `/roast` (5.1) — Jump to LAUNCH to validate what you've built
- `/flow` (2.4) — Go back to audit the onboarding flow for friction
- `/guide` — See the full 20-step journey
