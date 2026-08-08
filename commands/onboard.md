---
name: onboard
description: "Generate a complete onboarding flow — step sequence, progressive disclosure, permission timing, empty states, activation metrics, and production React code."
argument-hint: "[product and first-run goal]"
---

# Onboard — Onboarding Flow Builder

## Before running

This command needs a product and what its first run should achieve.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate a complete, research-backed onboarding flow for any product. From first launch to activation moment: step sequence with progressive disclosure, permission request timing, empty state design, activation metrics, and production React/TypeScript code with animations.

## Onboarding Archetypes

| Archetype | Best For | Steps | Completion Target | Key Trait |
|-----------|----------|-------|-------------------|-----------|
| **Benefits-first** | Consumer apps, low complexity | 3-4 screens | 90%+ | Show value before asking for anything |
| **Progressive** | Medium complexity, feature-rich | 5-7 screens | 75-85% | Reveal features as user needs them |
| **Setup wizard** | High complexity, requires configuration | 7-12 screens | 60-75% | Guided setup with progress tracking |
| **Contextual / inline** | Power tools, expert users | No dedicated flow | N/A | Teach in context, not upfront |
| **Hybrid** | Marketplaces, two-sided products | 4-6 screens + contextual | 70-80% | Brief intro then contextual coaching |
| **Tooltip tour** | Feature updates, secondary features | 3-5 tooltips | 85%+ | Non-blocking, dismissible, sequential |
| **Video walkthrough** | Complex workflows, creative tools | 1-2 min video + 2-3 steps | 65-75% | Visual demonstration of core loop |

## Generation Protocol

1. **Gather product context.**

   **Required inputs:**
   - **Product type**: mobile app, web app, desktop app, SaaS platform, marketplace
   - **App description**: what the product does in one sentence
   - **Onboarding style**: wizard, progressive, tooltip tour, video, or `recommend`
   - **Critical first action**: what must the user do to experience core value?

   **Contextual inputs:**
   - **Sector**: fintech, healthcare, SaaS, social, e-commerce, EdTech, creator tools, etc.
   - **Target user sophistication**: novice (hand-holding), intermediate (familiar with category), expert (fast setup)
   - **Platform**: iOS, Android, web, cross-platform
   - **Key value proposition**: the one sentence explaining why this product exists
   - **Mental model gap**: what does the user think this product is before onboarding? If the mental model differs from reality, onboarding must bridge that gap
   - **Prior Sumi outputs**: check for `/style` (visual direction), `/tokens` (design tokens), `/measure` (HEART metrics). If available, consume them. If not, use defaults and note what is missing

2. **Select archetype and generate step sequence.**

   Each step must include:
   - **Step number and title**: clear, benefit-oriented heading
   - **Screen type**: Welcome, Value Prop, Permission, Personalization, Setup, Activation, Celebration
   - **Purpose**: what this step accomplishes for the user and for the product
   - **Content**: headline, subtext, visual direction, interaction type
   - **Progressive disclosure level**: what is revealed vs. deferred
   - **Skip option**: whether this step can be skipped and the fallback experience
   - **Data captured**: what the product learns from this step
   - **Transition**: animation type to advance to next step
   - **Cognitive load audit**: count decisions (max 2 per step, Hick's Law) and working memory items (max 5, Miller's Law)

   ### Step Sequencing Rules
   1. **Welcome screen first** — establish trust and set expectations. No sign-up wall before value demonstration
   2. **Value before ask** — demonstrate a feature before requesting the permission it needs
   3. **Personalization early** — ask 2-3 questions that visibly change the experience
   4. **Peak moment in the middle** — the "aha" moment should not be the first or last step
   5. **Permission requests spaced** — never request two permissions in consecutive steps
   6. **Celebration at the end** — always end on a positive, empowering note
   7. **Never end on**: a permission request, a paywall, an error state, or a loading screen

3. **Design permission request strategy.**

   Time every permission for maximum grant rate:

   | Permission | When to Ask | Pre-Permission Copy | Denial Fallback |
   |-----------|------------|--------------------|-----------------|
   | **Notifications** | After showing a feature that benefits from alerts | "Get notified when [specific benefit]" | Allow in-app notifications only; re-prompt after 3 sessions |
   | **Camera** | When user taps a camera-dependent feature | "Take a photo to [specific action]" | Show file upload alternative |
   | **Location** | When displaying location-dependent content | "Find [things] near you" | Manual city/zip entry |
   | **Contacts** | When user initiates social feature | "Invite friends who already use [app]" | Manual invite by email/link |
   | **Health/Fitness** | After explaining health feature benefit | "Track your [metric] automatically" | Manual data entry |

   ### Pre-Permission Screen Pattern
   ```
   ┌──────────────────────────┐
   │                          │
   │     [Illustration]       │
   │                          │
   │  "Get price drop alerts" │
   │  We'll notify you when   │
   │  items on your wishlist  │
   │  go on sale.             │
   │                          │
   │  [Enable Notifications]  │
   │  [Maybe Later]           │
   │                          │
   └──────────────────────────┘
   ```
   The "Maybe Later" option is essential. Forcing a decision reduces grant rates.

4. **Design personalization questions.**

   Rules for personalization:
   - **2-4 questions maximum** — more causes drop-off
   - Each question must **visibly change** the product experience
   - Use **selection UI** (chips, cards with illustrations) — never dropdowns or text input
   - Show **immediate preview** of how the selection affects the interface
   - Always include **"I'll decide later"** escape hatch

   ### Common Personalization Patterns
   | Question Type | UI Pattern | Example |
   |--------------|-----------|---------|
   | Role/persona | Card selection with icons | "I'm a designer / developer / manager" |
   | Goal | Chip multi-select | "I want to: track habits / build routines / sleep better" |
   | Experience level | 3-option scale | "New to investing / Some experience / Experienced" |
   | Content preference | Grid of visual cards | "Topics you care about: [visual grid]" |
   | Appearance | Toggle with live preview | "Light / Dark / System" |

5. **Design empty state to first-value transition.**

   The moment after onboarding completes is critical. The user lands in an empty product. Design this transition:

   ### Empty State Design Rules
   - **Teach, don't just inform**: "No messages yet" is bad. "Start a conversation with your team" with a CTA is good
   - **Seed with data**: provide templates, samples, or suggestions to prevent blank-canvas paralysis
   - **Show one clear action**: a single prominent CTA pointing to the first valuable action
   - **Progressive scaffolding removal**: as the user creates content, gradually remove onboarding hints
   - **Celebrate first completion**: when the user completes their first real action, acknowledge it (confetti, success copy, progress update)

   ### Empty State Template
   ```
   ┌──────────────────────────┐
   │                          │
   │     [Illustration]       │
   │                          │
   │  "Your workspace is      │
   │   ready"                 │
   │                          │
   │  Start by creating your  │
   │  first [thing]. We've    │
   │  added a template to     │
   │  get you started.        │
   │                          │
   │  [Create Your First X]   │
   │                          │
   │  ─── or explore ───      │
   │  📖 Browse templates     │
   │  👋 Take a quick tour    │
   │                          │
   └──────────────────────────┘
   ```

6. **Design peak and end moments (Peak-End Rule).**

   Users judge an experience by its most intense moment (peak) and its ending — not the average (Kahneman).

   - **Identify the peak moment**: which step delivers the biggest "aha"? Design it to feel magical — instant payoff, visual delight, surprising personalization
   - **Design the celebration**: the moment after the peak action should include a micro-celebration (animation, confetti, success copy) to anchor positive memory
   - **Design the final screen**: the last onboarding screen is disproportionately important. End on empowerment — show what the user has accomplished, not what remains
   - **Anti-pattern warning**: never end on a permission request, paywall, error state, or loading screen. These create negative final impressions that bias the entire memory

7. **Generate activation metrics framework.**

   | Metric | Definition | Target | Instrumentation |
   |--------|-----------|--------|-----------------|
   | **Step completion rate** | % of users who complete each step | 90%+ for step 1, decreasing 5-8% per step | Analytics event per step transition |
   | **Overall completion rate** | % who finish the entire flow | Varies by archetype (see table above) | Event on final step completion |
   | **Time-to-value** | Seconds from app open to first value moment | < 60s for consumer, < 5min for SaaS | Timestamp diff: app_open → first_value_action |
   | **Skip rate per step** | % who skip each optional step | < 30% indicates good step design | Event on skip button click |
   | **Permission grant rate** | % who grant each permission | 60%+ with pre-permission screen | Event on system dialog result |
   | **First session depth** | Actions taken in first session after onboarding | 3+ meaningful actions | Count of key events in session 1 |
   | **Day 1 retention** | % who return the day after onboarding | 40%+ (consumer), 60%+ (SaaS) | Session tracking |
   | **Activation rate** | % who complete the critical first action | Defined per product | Event on critical action completion |

   ### Drop-Off Analysis Points
   Instrument these specific moments:
   - Between step 1 and step 2 (highest drop-off point)
   - Before and after each permission request
   - Before and after each text input field
   - At the "skip" button on personalization steps
   - At the empty state CTA

   ### A/B Test Hypotheses
   Generate 3-5 testable hypotheses per flow:
   ```
   H1: Reducing onboarding from [N] to [N-2] steps will increase completion by [X]%
   H2: Moving personalization before value demonstration will decrease completion by [X]%
   H3: Adding a progress indicator will increase completion by [X]%
   H4: Replacing text descriptions with short video clips will increase engagement by [X]%
   H5: Allowing anonymous trial before sign-up will increase activation by [X]%
   ```

8. **Generate production React/TypeScript code.**

   ### Stepper Component
   ```tsx
   'use client';
   import { useState, useCallback, useEffect, useRef } from 'react';

   interface OnboardingStep {
     id: string;
     title: string;
     component: React.ComponentType<StepProps>;
     skippable: boolean;
     analyticsEvent: string;
   }

   interface StepProps {
     onNext: (data?: Record<string, unknown>) => void;
     onSkip: () => void;
     onBack: () => void;
     isFirst: boolean;
     isLast: boolean;
   }

   interface OnboardingFlowProps {
     steps: OnboardingStep[];
     onComplete: (data: Record<string, unknown>) => void;
     onSkipAll?: () => void;
   }

   export function OnboardingFlow({ steps, onComplete, onSkipAll }: OnboardingFlowProps) {
     const [currentIndex, setCurrentIndex] = useState(0);
     const [collectedData, setCollectedData] = useState<Record<string, unknown>>({});
     const [direction, setDirection] = useState<'forward' | 'backward'>('forward');
     const announcerRef = useRef<HTMLDivElement>(null);

     const currentStep = steps[currentIndex];
     const StepComponent = currentStep.component;
     const progress = ((currentIndex + 1) / steps.length) * 100;

     // Track step view
     useEffect(() => {
       trackEvent('onboarding_step_view', {
         step: currentStep.id,
         stepIndex: currentIndex,
         totalSteps: steps.length,
       });
     }, [currentIndex, currentStep.id, steps.length]);

     // Announce step change to screen readers
     useEffect(() => {
       if (announcerRef.current) {
         announcerRef.current.textContent =
           `Step ${currentIndex + 1} of ${steps.length}: ${currentStep.title}`;
       }
     }, [currentIndex, currentStep.title, steps.length]);

     const handleNext = useCallback((data?: Record<string, unknown>) => {
       if (data) {
         setCollectedData(prev => ({ ...prev, [currentStep.id]: data }));
       }
       trackEvent(currentStep.analyticsEvent, { action: 'complete', ...data });

       if (currentIndex === steps.length - 1) {
         onComplete({ ...collectedData, [currentStep.id]: data });
       } else {
         setDirection('forward');
         setCurrentIndex(i => i + 1);
       }
     }, [currentIndex, currentStep, steps.length, collectedData, onComplete]);

     const handleSkip = useCallback(() => {
       trackEvent(currentStep.analyticsEvent, { action: 'skip' });
       setDirection('forward');
       setCurrentIndex(i => Math.min(i + 1, steps.length - 1));
     }, [currentStep, steps.length]);

     const handleBack = useCallback(() => {
       setDirection('backward');
       setCurrentIndex(i => Math.max(i - 1, 0));
     }, []);

     return (
       <div className="onboarding-container">
         {/* Screen reader announcer */}
         <div
           ref={announcerRef}
           role="status"
           aria-live="polite"
           aria-atomic="true"
           className="sr-only"
         />

         {/* Progress bar */}
         <div className="onboarding-progress" role="progressbar"
           aria-valuenow={progress} aria-valuemin={0} aria-valuemax={100}
           aria-label={`Onboarding progress: step ${currentIndex + 1} of ${steps.length}`}
         >
           <div className="onboarding-progress-fill" style={{ width: `${progress}%` }} />
         </div>

         {/* Step indicators */}
         <div className="onboarding-dots" aria-hidden="true">
           {steps.map((step, i) => (
             <div
               key={step.id}
               className={`onboarding-dot ${i === currentIndex ? 'active' : ''} ${i < currentIndex ? 'completed' : ''}`}
             />
           ))}
         </div>

         {/* Skip all (if allowed) */}
         {onSkipAll && currentIndex < steps.length - 1 && (
           <button className="onboarding-skip-all" onClick={onSkipAll}>
             Skip setup
           </button>
         )}

         {/* Step content with animation */}
         <div className={`onboarding-step-wrapper animate-${direction}`} key={currentStep.id}>
           <StepComponent
             onNext={handleNext}
             onSkip={handleSkip}
             onBack={handleBack}
             isFirst={currentIndex === 0}
             isLast={currentIndex === steps.length - 1}
           />
         </div>
       </div>
     );
   }

   // Analytics helper (replace with your analytics SDK)
   function trackEvent(name: string, data?: Record<string, unknown>) {
     if (typeof window !== 'undefined' && 'analytics' in window) {
       (window as any).analytics.track(name, data);
     }
   }
   ```

   ### Step Animation CSS
   ```css
   .onboarding-container {
     position: relative;
     width: 100%;
     max-width: 480px;
     margin: 0 auto;
     min-height: 100dvh;
     display: flex;
     flex-direction: column;
     padding: var(--space-page-inline);
   }

   .onboarding-progress {
     height: 3px;
     background: var(--color-border-subtle);
     border-radius: var(--radius-full);
     overflow: hidden;
   }

   .onboarding-progress-fill {
     height: 100%;
     background: var(--color-action-primary);
     border-radius: var(--radius-full);
     transition: width 0.3s var(--easing-ease-out);
   }

   .onboarding-dots {
     display: flex;
     justify-content: center;
     gap: 8px;
     padding: var(--space-300) 0;
   }

   .onboarding-dot {
     width: 8px;
     height: 8px;
     border-radius: 50%;
     background: var(--color-border-default);
     transition: all 0.2s ease;
   }
   .onboarding-dot.active {
     background: var(--color-action-primary);
     transform: scale(1.25);
   }
   .onboarding-dot.completed {
     background: var(--color-action-primary);
     opacity: 0.5;
   }

   .onboarding-skip-all {
     position: absolute;
     top: var(--space-300);
     right: var(--space-300);
     color: var(--color-text-secondary);
     font-size: var(--font-size-sm);
     background: none;
     border: none;
     cursor: pointer;
     padding: var(--space-100) var(--space-200);
   }

   .onboarding-step-wrapper {
     flex: 1;
     display: flex;
     flex-direction: column;
     justify-content: center;
   }

   /* Step transition animations */
   .animate-forward {
     animation: slide-in-right 0.3s var(--easing-ease-out);
   }
   .animate-backward {
     animation: slide-in-left 0.3s var(--easing-ease-out);
   }

   @keyframes slide-in-right {
     from {
       opacity: 0;
       transform: translateX(30px);
     }
     to {
       opacity: 1;
       transform: translateX(0);
     }
   }

   @keyframes slide-in-left {
     from {
       opacity: 0;
       transform: translateX(-30px);
     }
     to {
       opacity: 1;
       transform: translateX(0);
     }
   }

   @media (prefers-reduced-motion: reduce) {
     .animate-forward,
     .animate-backward {
       animation: fade-in 0.15s ease;
     }
     @keyframes fade-in {
       from { opacity: 0; }
       to { opacity: 1; }
     }
     .onboarding-progress-fill {
       transition: none;
     }
   }

   /* Responsive — tablet+ */
   @media (min-width: 768px) {
     .onboarding-container {
       max-width: 560px;
       min-height: auto;
       padding: var(--space-800) var(--space-600);
       margin-top: 10vh;
       background: var(--color-bg-surface);
       border-radius: var(--radius-xl);
       border: 1px solid var(--color-border-subtle);
       box-shadow: var(--shadow-lg);
     }
   }
   ```

   ### Example Step Component
   ```tsx
   /* Welcome Step */
   export function WelcomeStep({ onNext, isFirst }: StepProps) {
     return (
       <div className="step-content">
         <div className="step-illustration">
           {/* Illustration or Lottie animation */}
         </div>
         <h1 className="step-headline">Welcome to [App Name]</h1>
         <p className="step-subtext">
           [One sentence describing the core value proposition]
         </p>
         <button className="btn-primary btn-full" onClick={() => onNext()}>
           Get Started
         </button>
       </div>
     );
   }

   /* Personalization Step (chip selection) */
   export function GoalSelectionStep({ onNext, onSkip, onBack }: StepProps) {
     const [selected, setSelected] = useState<string[]>([]);

     const goals = [
       { id: 'goal-1', label: 'Goal One', icon: '...' },
       { id: 'goal-2', label: 'Goal Two', icon: '...' },
       { id: 'goal-3', label: 'Goal Three', icon: '...' },
       { id: 'goal-4', label: 'Goal Four', icon: '...' },
     ];

     const toggle = (id: string) => {
       setSelected(prev =>
         prev.includes(id) ? prev.filter(g => g !== id) : [...prev, id]
       );
     };

     return (
       <div className="step-content">
         <button className="btn-back" onClick={onBack} aria-label="Go back">
           ← Back
         </button>
         <h2 className="step-headline">What brings you here?</h2>
         <p className="step-subtext">Pick one or more. We'll personalize your experience.</p>
         <div className="chip-grid" role="group" aria-label="Select your goals">
           {goals.map(goal => (
             <button
               key={goal.id}
               className={`chip ${selected.includes(goal.id) ? 'chip-selected' : ''}`}
               onClick={() => toggle(goal.id)}
               aria-pressed={selected.includes(goal.id)}
             >
               <span className="chip-icon" aria-hidden="true">{goal.icon}</span>
               <span>{goal.label}</span>
             </button>
           ))}
         </div>
         <button
           className="btn-primary btn-full"
           onClick={() => onNext({ goals: selected })}
           disabled={selected.length === 0}
         >
           Continue
         </button>
         <button className="btn-text" onClick={onSkip}>
           I'll decide later
         </button>
       </div>
     );
   }

   /* Celebration / Final Step */
   export function CelebrationStep({ onNext }: StepProps) {
     return (
       <div className="step-content step-celebration">
         <div className="celebration-animation">
           {/* Confetti or success animation */}
         </div>
         <h2 className="step-headline">You're all set!</h2>
         <p className="step-subtext">
           Your personalized [app] is ready. Here's what you can do first:
         </p>
         <ul className="first-actions">
           <li>Create your first [thing]</li>
           <li>Explore templates</li>
           <li>Invite your team</li>
         </ul>
         <button className="btn-primary btn-full" onClick={() => onNext()}>
           Let's Go
         </button>
       </div>
     );
   }
   ```

   ### Heuristic Compliance Checklist
   Verify in the generated code:
   - **H1 (System Status)**: progress indicator visible on every step
   - **H3 (User Control)**: back button and skip option on every non-critical step
   - **H4 (Consistency)**: step layout, button placement, animation style consistent
   - **H5 (Error Prevention)**: inline validation on inputs; sensible defaults pre-filled
   - **H6 (Recognition > Recall)**: visual selectors (chips, cards) instead of free-text input
   - **H8 (Minimalist Design)**: each step has only essential content
   - **H10 (Help)**: contextual help text on complex steps

## Output Format

```
### Phase Position
> **Phase: BUILD** | `/onboard`
> *UX Design | Onboarding Flow*

## Onboarding Flow: [Product Name]

### Flow Parameters
- **Product type**: [type]
- **Sector**: [sector]
- **Archetype**: [selected archetype with reasoning]
- **Target user**: [sophistication level]
- **Onboarding style**: [wizard / progressive / tooltip / video / hybrid]
- **Time-to-value target**: [X seconds/minutes]
- **Total steps**: [N]

### Flow Map
[Visual step sequence]
[Branch points and skip paths marked]

### Step-by-Step Breakdown
#### Step [N]: [Title]
- **Screen type**: [Welcome / Value Prop / Permission / Personalization / Setup / Activation / Celebration]
- **Headline**: [benefit-oriented headline]
- **Subtext**: [supporting copy]
- **Interaction**: [tap to continue / select options / input / permission dialog]
- **Skip option**: [Yes/No + fallback]
- **Data captured**: [what the product learns]
- **Cognitive load**: [decisions: N/2, memory items: N/5]
[Repeated for each step]

### Permission Strategy
[Timing, pre-permission copy, and denial fallback for each permission]

### Personalization Questions
[2-4 questions with UI pattern and impact on experience]

### Empty State → First Value
[Design for the post-onboarding empty state with CTA]

### Peak and End Design
- **Peak moment**: Step [N] — [description]
- **Celebration**: [what happens after the peak]
- **Final screen**: [description and why it creates positive memory]
- **Anti-patterns avoided**: [what the flow deliberately does NOT end on]

### React/TypeScript Implementation
[OnboardingFlow component, step components, CSS, animation]

### Activation Metrics
| Metric | Target | Instrumentation |
|--------|--------|-----------------|
[Metrics table]

### Drop-Off Analysis Points
[Where to instrument for funnel analysis]

### A/B Test Hypotheses
[3-5 testable variations with predicted impact]

### Cognitive Load Audit
| Step | Decisions (max 2) | Memory Items (max 5) | New Concepts | Status |
|------|-------------------|---------------------|-------------|--------|
[Per-step audit]

### Heuristic Compliance
- [ ] H1: Progress indicator on every step
- [ ] H3: Back and skip on non-critical steps
- [ ] H4: Consistent layout and interaction patterns
- [ ] H5: Inline validation; sensible defaults
- [ ] H6: Visual selectors over free text
- [ ] H8: Only essential content per step
- [ ] H10: Help text on complex steps

### Prior Output Integration
- **`/style` consumed**: [Yes/No — what was used]
- **`/tokens` consumed**: [Yes/No — what was used]
- **`/measure` consumed**: [Yes/No — activation targets applied]
- **Missing context**: [what prior outputs would improve this flow]
```

## Cross-References

When building onboarding flows, draw from:
- `performance-states-patterns` skill for empty states, loading states, skeleton screens, onboarding transitions
- `cognitive-psychology-ux` skill for progressive disclosure, cognitive load management, peak-end rule
- `component-patterns-code` skill for React/SwiftUI/CSS stepper, carousel, form components
- `mobile-ux-design` skill for iOS and Android onboarding conventions
- `interaction-motion-design` skill for step transition animations and celebration moments
- `animation-recipe-library` skill for confetti, success, entrance animations
- `micro-copy-intelligence` skill for onboarding copy: headlines, CTAs, permission prompts, empty states
- `ux-metrics-measurement` skill for activation metrics, funnel analysis, A/B testing
- `conversion-optimization-patterns` skill for onboarding completion optimization

## Next Step

**Next** → `/screen` — Build the screens your users will see after onboarding

**Alternatives**:
- `/roast` — Stress-test the onboarding flow with a brutal critique
- `/a11y` — Audit onboarding accessibility
- `/measure` — Define HEART metrics that onboarding targets
- `/guide` — See the full journey
