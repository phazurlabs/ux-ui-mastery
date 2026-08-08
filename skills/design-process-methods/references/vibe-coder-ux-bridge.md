# The Vibe Coder's UX Bridge — Process for Terminal Workers

A complete framework for integrating UX process into AI-assisted development workflows. Bridges the gap between "prompt and ship" and evidence-based design, specifically designed for developers who work in the terminal with AI code generation tools.

---

## The Research: Why This Matters

### arXiv:2509.10652 — Key Findings

The paper "AI-Assisted Software Development: Implications for Developer Productivity and Skill" (2025) identifies three interconnected risks in AI-assisted development that directly apply to UI/UX work:

#### Risk 1: Pseudo-Productivity

**Finding**: Developers using AI assistants report feeling 2-3x more productive, but measurable output quality (bug rate, user satisfaction, code maintainability) shows minimal improvement — and sometimes degradation.

**UX parallel**: A developer using AI to generate 10 screens in an hour feels enormously productive. But if none of the screens solve the actual user problem, the real productivity is zero. Volume of output ≠ quality of outcomes.

**Observable symptoms**:
- Many screens/components generated, few validated with users
- High feature count, low feature adoption
- Code reviews focus on "does it work?" not "should it exist?"
- Shipping frequency increases but user satisfaction plateaus or drops
- "We built 40 screens this sprint" replaces "We validated 3 hypotheses this sprint"

**Antidote**: Define success criteria before generating. The `/brief` command forces this by requiring measurable outcomes before any build activity.

#### Risk 2: Homogenization

**Finding**: AI-generated code converges on similar patterns regardless of context. Models trained on common patterns reproduce common patterns. The result is increasing sameness across products.

**UX parallel**: AI-generated UIs default to the same layouts, the same component patterns, the same information hierarchies. Every SaaS dashboard starts looking identical. Every mobile app uses the same bottom navigation. Differentiation — the quality that makes a product memorable — disappears.

**Observable symptoms**:
- Your UI looks like it could belong to any product in your category
- Users can't distinguish your product from competitors in screenshots
- The AI consistently suggests the same layout regardless of what you describe
- You've stopped questioning AI output because "it looks professional"
- Every screen has the same information density, the same spacing, the same card-based layout
- Design reviews produce feedback like "it's fine" instead of "this is distinctively ours"

**Antidote**: Run `/style` before building. Sector-specific style direction creates visual differentiation that AI generation alone doesn't provide. Add the style tokens from `/tokens` as constraints in every build prompt.

#### Risk 3: Skill Erosion

**Finding**: Developers who consistently accept AI suggestions without critical evaluation gradually lose the ability to write code independently. The effect is strongest in design-adjacent skills (layout, visual hierarchy, interaction patterns) because these skills atrophy fastest without practice.

**UX parallel**: A developer who always accepts AI-generated UI stops developing their own design eye. They lose the ability to critique layouts, spot accessibility issues, evaluate information hierarchy, or reason about user mental models. When the AI generates a bad design, they can't tell.

**Observable symptoms**:
- You can no longer explain *why* a layout works or doesn't work
- You accept AI output without modification because you're unsure what to change
- Your design vocabulary has shrunk (you say "it looks good" instead of identifying specific principles)
- You've forgotten what WCAG contrast ratios are or how to check them manually
- When the AI generates something wrong, you regenerate instead of fixing it
- You feel less confident about UI decisions than you did before using AI tools

**Antidote**: Run Sumi audit commands on every AI-generated output. Each audit forces you to evaluate output against specific principles — heuristics, cognitive laws, accessibility standards. This maintains and builds your design vocabulary and judgment.

---

## The Hall of Real Consequences

Products that shipped without adequate UX process — and what happened:

### Healthcare.gov Launch (2013)
**What happened**: Built by engineers without user testing. The sign-up flow had 76 screens. Users couldn't complete enrollment. The site crashed under load because nobody tested real usage patterns.
**Root cause**: No Empathize phase. No usability testing. No load testing against realistic user behavior.
**Cost**: $1.7 billion to fix. Congressional hearings. Massive public trust erosion.
**What 10 minutes of /intent would have revealed**: "Users who need health insurance need to compare plans and enroll because open enrollment is time-limited" → success criteria: complete enrollment in under 15 minutes → would have caught the 76-screen flow immediately.

### Snapchat Redesign (2018)
**What happened**: Completely redesigned the app without user research. Separated friends from publishers. 1.2 million users signed a petition to revert. Kylie Jenner's single tweet ("does anyone else not open Snapchat anymore?") wiped $1.3B in market cap.
**Root cause**: No Empathize phase. Redesign driven by business goals (separating social from media for advertisers), not user needs.
**Cost**: $1.3B market cap loss in one day. 3M daily active users lost in Q1 2018.
**What /ground would have revealed**: Users' core mental model is "friends and content are interleaved" — any redesign must preserve this model or introduce the new one gradually.

### Sonos App Redesign (2024)
**What happened**: Rebuilt the entire app from scratch. Removed features users depended on (alarm management, local library, queue management). Shipped without feature parity. CEO publicly apologized.
**Root cause**: No user testing before launch. Built the new app against engineering goals (modern architecture) instead of user goals (control my speakers).
**Cost**: CEO resignation. Stock price drop. Years of user trust destroyed.
**What /vibe-check would have caught**: Heuristic 7 (Flexibility and Efficiency of Use) — power users lost critical workflows. Severity 4 violation on 6+ features.

### Digg v4 (2010)
**What happened**: Redesigned to favor publishers over community-submitted content. Users couldn't recognize the product they loved. Traffic dropped 26% in one month. Users migrated to Reddit permanently.
**Root cause**: Redesign driven by monetization (publisher partnerships), not user research. No testing with the existing community.
**Cost**: Digg sold for $500K (previously valued at $200M). Reddit became the dominant platform.
**What /intent would have forced**: "Power users who curate and vote on community content need [X] because [Z]" — the problem statement would have revealed that the redesign removed the core user value.

### The Pattern

Every failure shares the same root cause: **building without understanding**. The fix is always the same: Empathize → Define → then build. This is what Phase 0 exists to prevent.

---

## The Before/While/After Framework

### BEFORE Prompting: The 2-Minute Pre-Prompt

Every build session starts with 2 minutes of structured thinking. This single habit prevents all three risks identified in arXiv:2509.10652.

#### The Pre-Prompt Checklist

```markdown
## Pre-Prompt Checklist (2 min)

### 1. WHO is the user? (30 sec)
- Name a specific persona (not "users" — a real archetype)
- What is their role/context? (developer, nurse, shopper, student)
- What accessibility needs might they have? (vision, motor, cognitive, situational)
- What device/environment? (mobile on a train, desktop in office, tablet in warehouse)

### 2. WHAT are they trying to do? (30 sec)
- State the task as verb + noun: "booking a flight," "reviewing test results," "configuring settings"
- What triggers this task? (notification, schedule, need, problem)
- What does "done" look like? (specific outcome, not "they used the feature")
- What happens if they fail? (stakes/consequences)

### 3. WHY this solution? (30 sec)
- What's their current workaround? (they're solving this somehow today)
- Why is the current solution insufficient? (too slow, too error-prone, inaccessible)
- What's your hypothesis? "We believe [X] will improve because [Y]"

### 4. HOW will you know it works? (30 sec)
- Functional success: what must it do?
- Usability success: how fast/easy must it be? (task time, error rate, learnability)
- Accessibility success: WCAG level, persona spectrum coverage
- Business success: conversion rate, adoption rate, retention impact
```

#### Example: Before Building a Settings Screen

**Without pre-prompt** (vibe coding):
```
"Generate a settings screen for a SaaS app"
```
Result: Generic settings screen with random toggle ordering, no information hierarchy, no grouping logic, no consideration of who needs what settings.

**With pre-prompt**:
```
WHO: Sarah, 35, product manager at a 50-person startup. Uses the app 8 hours/day
     on a laptop. Wears reading glasses. Often configures settings for her team.
WHAT: Configuring notification preferences so her team gets the right alerts
      without notification fatigue. Task triggered by team complaints about too
      many emails. "Done" = team members only get notifications they act on.
WHY:  Currently uses Slack to tell people "ignore that email." Insufficient
      because it doesn't scale and new team members don't know which to ignore.
HOW:  Functional: role-based notification defaults, per-channel control
      Usability: < 3 minutes to configure for a team of 10
      Accessibility: WCAG 2.2 AA, Dynamic Type support
      Business: 50% reduction in "notification settings" support tickets
```

Now the AI prompt becomes:
```
/screen settings for a SaaS project management app. Target user is a product
manager configuring notifications for a 10-person team. Must support role-based
defaults, per-channel control (email/slack/in-app/push), and batch configuration.
Success = < 3 minutes for 10 people. WCAG 2.2 AA. Reading glasses user so generous
text sizing. Group settings by: Account → Team → Notifications → Integrations → Data.
```

### WHILE Generating: Real-Time Evaluation

As AI generates output, evaluate it against these checkpoints:

#### The Generation Evaluation Checklist

```markdown
## While Generating (ongoing)

### Mental Model Check
- Does this match how the USER thinks about this task?
- Or does this match how the AI's training data structures this information?
- Would Sarah (the persona) understand this grouping/labeling/flow?

### Homogenization Check
- Would this look identical if generated for a different product?
- Is there anything distinctively "ours" about this design?
- Does this reflect the style direction from /taste?
- Are the design tokens from /drip being consumed?

### Edge Case Check
- What happens with 0 items? (empty state)
- What happens with 1 item? (singular state)
- What happens with 1,000 items? (scale state)
- What happens when the network fails? (error state)
- What happens on first use? (onboarding state)
- What happens when data is loading? (loading state)
- What happens offline? (offline state)

### Hierarchy Check
- Is the most important information most prominent?
- Is the least important information least prominent?
- Does the visual hierarchy match the task priority?
- Can the user find the primary action in < 2 seconds?

### Assumption Check
- What assumptions is the AI making about the user?
- What assumptions is the AI making about the data?
- What assumptions is the AI making about the device?
- Are any of these assumptions wrong for your specific case?
```

### AFTER Generating: The 5-Minute Post-Generation Audit

After AI generates UI, spend 5 minutes evaluating before using or shipping.

#### The 5-Minute Audit

```markdown
## Post-Generation Audit (5 min)

### Minute 1: Heuristic Spot-Check
- [ ] System status: Can the user always tell what's happening?
- [ ] Real-world match: Does the language match the user's vocabulary?
- [ ] User control: Can the user undo, go back, and escape?
- [ ] Consistency: Are similar things treated similarly?
- [ ] Error prevention: Are dangerous actions guarded?
→ Quick alternative: Run `/audit` for full evaluation

### Minute 2: Accessibility Quick-Check
- [ ] Color contrast: Do all text/background pairs meet 4.5:1 (AA)?
- [ ] Keyboard: Can every interactive element be reached and operated by keyboard?
- [ ] Screen reader: Do images have alt text? Do buttons have labels?
- [ ] Touch targets: Are all interactive elements at least 44x44px?
- [ ] Focus order: Does tab order follow visual/logical order?
→ Quick alternative: Run `/a11y` for full WCAG 2.2 audit

### Minute 3: State Completeness
- [ ] Empty state: What shows when there's no data?
- [ ] Loading state: What shows while data loads?
- [ ] Error state: What shows when something fails?
- [ ] Populated state: The "happy path" (usually what AI generates)
- [ ] Partial state: What if only some data loaded?
- [ ] Offline state: What if there's no network?
- [ ] Updating state: What if data is being saved/synced?

### Minute 4: Information Architecture
- [ ] Grouping: Are related items grouped together?
- [ ] Labeling: Are labels clear and consistent?
- [ ] Navigation: Can the user find what they need?
- [ ] Priority: Is the most important thing most prominent?
- [ ] Progressive disclosure: Is complexity hidden until needed?

### Minute 5: Persona Validation
- [ ] Does this solve the persona's actual task?
- [ ] Would the persona understand the terminology?
- [ ] Can the persona complete the task in the target time?
- [ ] Does this handle the persona's accessibility needs?
- [ ] Would the persona choose this over their current workaround?
```

---

## The 15-Minute Full UX Check

For important screens or components, invest 15 minutes for a comprehensive check. This maps directly to Sumi commands:

```markdown
## 15-Minute Full UX Check

### Block 1: Process Alignment (3 min) — Manual
- [ ] Re-read the problem statement from /intent
- [ ] Verify the generated output addresses the defined problem
- [ ] Check: does this match the success criteria?
- [ ] Check: does this serve the identified persona?
- [ ] Check: did you consider 3+ approaches before committing?

### Block 2: Heuristic Evaluation (3 min) — /vibe-check
- [ ] Run /vibe-check on the generated code/screen
- [ ] Note severity 3-4 findings (critical violations)
- [ ] Identify any heuristic scored below 3/5

### Block 3: Cognitive Audit (3 min) — /brain-scan
- [ ] Run /brain-scan on the generated code/screen
- [ ] Check cognitive load score
- [ ] Identify Hick's Law violations (too many choices)
- [ ] Identify Fitts's Law violations (target sizing/placement)

### Block 4: Accessibility Audit (3 min) — /include
- [ ] Run /include on the generated code/screen
- [ ] Fix all WCAG AA failures
- [ ] Verify keyboard navigation
- [ ] Verify screen reader experience

### Block 5: Final Integration (3 min) — Manual
- [ ] Does this integrate with the existing design system?
- [ ] Does this consume design tokens (not magic numbers)?
- [ ] Does this handle all 7 states?
- [ ] Does this respect the style direction from /taste?
- [ ] Would you ship this if you couldn't generate another version?
```

---

## Anti-Patterns: What Not to Do

### Anti-Pattern 1: Prompt-and-Pray

**What it looks like**:
```
"Make me a dashboard"
[AI generates dashboard]
"Looks good, ship it"
```

**Why it fails**: No defined user, no defined problem, no defined success criteria. The "dashboard" might look professional but solve no actual user need.

**The fix**: `/brief` → `/style` → `/screen` → `/audit` → `/a11y`

### Anti-Pattern 2: The Iteration Illusion

**What it looks like**:
```
"Make me a dashboard"
"No, more like Stripe's dashboard"
"Add more charts"
"Make it darker"
"Add a sidebar"
[15 iterations later]
"Ship it"
```

**Why it fails**: Iterating on visual preferences without testing against user needs. Each iteration moves the design closer to the developer's taste, not the user's needs. This is decoration, not design.

**The fix**: Each iteration should test a hypothesis, not a preference. "/vibe-check — did this iteration fix the severity 4 finding from the last check?"

### Anti-Pattern 3: Audit Avoidance

**What it looks like**:
```
[Generates component]
"I should run /include but I don't want to find problems"
[Ships without audit]
```

**Why it fails**: Every unaudited component ships accessibility violations, heuristic failures, and cognitive load issues. These compound. By the time someone notices, the entire product needs remediation.

**The fix**: Make audits non-negotiable. `/audit` + `/a11y` is the minimum bar. Takes 5 minutes and prevents hours of remediation.

### Anti-Pattern 4: Context-Free Building

**What it looks like**:
```
/ship button
/ship card
/ship modal
/ship form
[Has 20 components with no shared design language]
```

**Why it fails**: Each component generated in isolation uses different spacing, colors, border-radius, typography, and motion. The result is a Frankenstein UI.

**The fix**: `/style` → `/tokens` → then `/component` with token constraints. Every component consumes the same token system.

### Anti-Pattern 5: The "Vibe" Validation

**What it looks like**:
```
[Generates UI]
"This vibes"
[Ships]
```

**Why it fails**: "Vibes" is not a design validation method. The aesthetic-usability effect (Kurosu & Kashimura, 1995) means attractive interfaces are perceived as more usable — but perception ≠ reality. The prettiest interface can still be unusable.

**The fix**: Replace "vibes" with evidence. `/roast` provides structured critique across 10 dimensions. `/grade` scores across all 21 skill domains. Evidence, not feelings.

### Anti-Pattern 6: One-And-Done Auditing

**What it looks like**:
```
[Generates screen]
/vibe-check
"No critical findings!"
[Ships]
```

**Why it fails**: `/audit` checks heuristics. It doesn't check accessibility, cognitive load, content quality, dark patterns, responsive behavior, or AI trust. Each audit command covers different dimensions.

**The fix**: Minimum audit battery = `/audit` + `/a11y` + `/audit`. For important screens, add `/audit` + `/audit` + `/responsive`.

### Anti-Pattern 7: Skipping Phase 0

**What it looks like**:
```
"I know what to build, let me just start"
/ship dashboard
```

**Why it fails**: Confidence is not the same as understanding. The most experienced designers still empathize and define before building. Phase 0 takes 10 minutes and prevents days of building the wrong thing.

**The fix**: `/sumi` → `/brief` → then build. 10 minutes to ground yourself saves hours of rework.

### Anti-Pattern 8: The Perfectionism Trap

**What it looks like**:
```
/intent
/ground
/taste
/inspo
/benchmark
/pulse
[Still hasn't built anything after 3 hours]
"I need to do more research..."
```

**Why it fails**: Process exists to make building better, not to replace building. Analysis paralysis is just as harmful as no analysis. The goal is informed action, not perfect knowledge.

**The fix**: Time-box each phase. Phase 0: 10 min max. Phase 1: 30 min max. Then BUILD. You can always loop back. Ship → learn → improve beats plan → plan → plan → never ship.

---

## Mapping Sumi Audit Commands to the Test Phase

Every Sumi audit command simulates a specific type of expert evaluation. Together, they approximate the Test phase of the NNG process:

| Sumi Command | Simulates | NNG Test Method | What It Catches |
|-------------|-----------|-----------------|-----------------|
| `/audit` (2.1) | Expert heuristic evaluator | Heuristic evaluation | Usability violations, missing feedback, inconsistency |
| `/audit` (2.2) | Cognitive psychologist | Cognitive walkthrough | Mental model mismatches, cognitive overload, bias |
| `/a11y` (2.3) | Accessibility specialist | WCAG audit | Contrast, keyboard, screen reader, ARIA violations |
| `/audit` (2.4) | UX researcher | Task analysis | Drop-off points, friction, unnecessary steps |
| `/audit` (3.1) | Ethics reviewer | Ethical review | Deceptive patterns, manipulative design, regulatory risk |
| `/ai-audit` (3.2) | AI safety researcher | AI trust evaluation | AI transparency, safety, explainability gaps |
| `/audit` (3.3) | Content strategist | Content audit | Clarity, tone, inclusive language, i18n readiness |
| `/responsive` (3.4) | QA engineer | Cross-device testing | Breakpoint issues, touch targets, reflow problems |
| `/roast` (5.1) | Senior design critic | Design critique | Visual hierarchy, composition, polish, consistency |
| `/grade` (5.3) | Design director | Comprehensive review | Cross-domain quality, readiness assessment |

### Minimum Viable Audit Battery

**Quick check (2 commands, ~5 min)**:
```
/vibe-check → /include
```
Covers heuristic violations + accessibility. The highest-impact minimum.

**Standard check (4 commands, ~15 min)**:
```
/vibe-check → /brain-scan → /include → /responsive
```
Adds cognitive load and cross-device. Appropriate for most screens.

**Full check (7 commands, ~30 min)**:
```
/vibe-check → /brain-scan → /include → /flow → /dark-scan → /copy-check → /responsive
```
Comprehensive coverage. Use for critical screens (checkout, onboarding, sign-up).

**Launch check (9 commands, ~45 min)**:
```
/vibe-check → /brain-scan → /include → /flow → /dark-scan → /trust-scan → /copy-check → /responsive → /judge
```
Full audit battery. Use before shipping to production.

---

## Process Recipes for Common Scenarios

### Recipe 1: "I need to build one component quickly"

**Time**: 10 minutes
```
1. Pre-prompt (2 min): Answer WHO, WHAT, WHY, HOW
2. Build (3 min): /ship [component] with full context
3. Audit (5 min): /vibe-check + /include
4. Done — or /remix if findings are critical
```

### Recipe 2: "I need to build a full screen"

**Time**: 25 minutes
```
1. Pre-prompt (2 min): Answer WHO, WHAT, WHY, HOW
2. Direction (5 min): /taste [sector] (skip if already done)
3. Build (8 min): /screen [type] with persona + tokens
4. Audit (10 min): /vibe-check + /brain-scan + /include + /responsive
5. Fix (if needed): /remix to apply must-fix findings
```

### Recipe 3: "I need to design a new product from scratch"

**Time**: 2-3 hours
```
1. Ground (10 min): /ground → /intent
2. Discover (30 min): /taste → /inspo → /benchmark
3. Foundation (15 min): /drip (token system)
4. Build (30 min): /screen (2-3 key screens) → /ship (key components)
5. Diagnose (30 min): /vibe-check → /brain-scan → /include → /flow
6. Fortify (20 min): /dark-scan → /copy-check → /responsive
7. Launch (15 min): /roast → /remix (apply fixes) → /judge (final score)
```

### Recipe 4: "I need to audit an existing product"

**Time**: 45-60 minutes
```
1. Ground (5 min): /intent (define what the product should do)
2. Diagnose (20 min): /vibe-check → /brain-scan → /include → /flow
3. Fortify (15 min): /dark-scan → /trust-scan → /copy-check → /responsive
4. Score (10 min): /judge (comprehensive review)
5. Fix (ongoing): /remix on critical findings → /roast to verify
```

### Recipe 5: "I'm a vibe coder and want to start doing UX right"

**Time**: 15 minutes for first session, then habits
```
First session:
1. Run /ground — understand the 6-phase process
2. Run /intent on your current project — define the problem properly
3. Run /vibe-check on something you've already built — see what you've been missing
4. Run /include on the same thing — see the accessibility gaps

Ongoing habits:
- Before every build: 2-min pre-prompt checklist
- After every generation: 5-min post-generation audit
- Before every ship: /vibe-check + /include minimum
- Weekly: 15-min full UX check on your most important screen
```

### Recipe 6: "I'm building a landing page to validate an idea"

**Time**: 20 minutes
```
1. Intent (3 min): /intent — "Who is this for, what's the value prop?"
2. Direction (5 min): /taste [sector] — visual credibility for the sector
3. Build (7 min): /screen landing-page with constraint stack
4. Audit (5 min): /copy-check (is the value prop clear?) + /include
```

### Recipe 7: "I'm adding a feature to an existing product"

**Time**: 15 minutes
```
1. Intent (3 min): /intent — define who needs this feature and why
2. Context (2 min): Paste existing code/screenshot for context
3. Build (5 min): /ship [feature component] with constraint stack
4. Audit (5 min): /vibe-check + /include on the new component
                   Check: does it match existing patterns? (/responsive)
```

### Recipe 8: "I'm building a mobile app MVP"

**Time**: 1-2 hours
```
1. Ground (10 min): /ground → /intent (mobile-specific constraints)
2. Direction (10 min): /taste [sector] — mobile-first style direction
3. Foundation (10 min): /drip — token system with mobile breakpoints
4. Core screens (30 min):
   /screen onboarding — first-run experience
   /screen home — primary task screen
   /screen [key-feature] — the one thing that makes your app different
5. Audit (20 min): /vibe-check + /include + /brain-scan + /responsive
6. Polish (10 min): /roast → /remix on lowest-scoring screen
```

### Recipe 9: "I need to fix a UX problem users are complaining about"

**Time**: 20 minutes
```
1. Reframe (3 min): /intent — redefine the problem from the user's perspective
                     (not "users want dark mode" but "users who work at night
                      need reduced eye strain because bright screens cause fatigue")
2. Diagnose (7 min): Paste the problematic screen/component
                      /vibe-check + /brain-scan — find the root cause
3. Fix (5 min): /remix — apply the findings as a redesign
4. Verify (5 min): /include + /responsive — ensure the fix doesn't break anything
```

### Recipe 10: "I'm a designer reviewing a developer's implementation"

**Time**: 30 minutes
```
1. Baseline (5 min): /intent — align on what the feature should do
2. Audit battery (20 min):
   /vibe-check — heuristic compliance
   /include — accessibility compliance
   /brain-scan — cognitive load issues
   /copy-check — content quality
   /responsive — cross-device behavior
3. Report (5 min): /judge — comprehensive score with priority roadmap
```

---

## Measuring Your Process Maturity

### The 5 Levels

| Level | Name | Behavior | Process Commands Used |
|-------|------|----------|----------------------|
| 0 | **Prompt & Pray** | Generate → ship. No evaluation. | None |
| 1 | **Post-Audit** | Generate → audit → fix obvious issues | `/audit`, `/a11y` |
| 2 | **Context-Aware** | Define context → generate with constraints → audit | `/brief`, `/style`, `/tokens` + audits |
| 3 | **Process-Driven** | Full Phase 0→5 journey. Problem before solution. | All phases used |
| 4 | **Evidence-Based** | Hypothesis → build → measure → learn. User testing. Real metrics. | Full Sumi + real user data |

**Most vibe coders start at Level 0.** The goal is Level 2 minimum, Level 3 ideal. Level 4 requires real users.

### Self-Assessment Questions

```markdown
## Where Am I? (answer honestly)

- Do I define the user before prompting AI? → If no: Level 0
- Do I run any audit after generating? → If no: Level 0
- Do I run /vibe-check + /include on generated code? → If yes: Level 1
- Do I use /intent and /taste before building? → If yes: Level 2
- Do I follow the full Phase 0→5 journey? → If yes: Level 3
- Do I test with real users and measure outcomes? → If yes: Level 4
```

### Level-Up Roadmap

**Level 0 → Level 1** (1 day):
- Start running `/audit` + `/a11y` after every AI generation
- Read the findings. Understand why they're problems.
- Fix severity 3-4 findings before shipping.

**Level 1 → Level 2** (1 week):
- Before building, run `/brief` to define the problem and persona
- Before building, run `/style` to establish style direction
- Use `/tokens` tokens in every build prompt
- Start using the 2-min pre-prompt checklist

**Level 2 → Level 3** (2-4 weeks):
- Follow the full Phase 0→5 journey for at least one project
- Run the standard audit battery (4 commands) on every important screen
- Use the 5-min post-generation audit consistently
- Review and iterate using `/roast` → `/remix` → `/roast` loops

**Level 3 → Level 4** (ongoing):
- Test prototypes with real users (even 3-5 people)
- Set up metrics with `/research` and track them
- Use `/benchmark` to compare against competitors regularly
- Measure outcomes, not outputs

### Process Maturity Titles

Earn your title. Each level comes with a builder identity:

| Level | Title | Badge | You've Proven |
|-------|-------|-------|--------------|
| 0 | **Pixel Pusher** | `[PP]` | You can generate UI |
| 1 | **Quality Checker** | `[QC]` | You audit before shipping |
| 2 | **Intent Builder** | `[IB]` | You define problems before solving them |
| 3 | **Process Designer** | `[PD]` | You follow the full design thinking process |
| 4 | **Evidence Architect** | `[EA]` | You validate with real users and measure outcomes |

Add your current title to your commit messages, PR descriptions, or project README. Track your growth. Level up intentionally.

**Where most builders are today**: Level 0-1.
**Where most builders should aim**: Level 2-3.
**What separates good products from great ones**: Level 3-4.

---

## The Constraint Stack

The constraint stack is the key artifact that carries intent forward from Phase 0 into all subsequent commands. It's a structured block of text that you paste into any BUILD command to ensure the AI generates with your full context.

### Format

```markdown
## Constraint Stack (from /intent)

**Problem**: [Users who X need Y because Z]
**Persona**: [Name, role, context, accessibility needs]
**Success**: [Functional + usability + accessibility + business criteria]
**Platform**: [Device, framework, design system]
**Style**: [From /taste — sector, palette, tokens, tone]
**Anti-goals**: [What this is NOT — prevents scope creep]
```

### Example

```markdown
## Constraint Stack

**Problem**: Nurses who monitor multiple patients need real-time alerts
  because current systems require checking each patient's chart individually,
  costing 15 minutes per round.
**Persona**: Maria, ICU nurse, 42, 12-hour shifts, standing with tablet,
  needs high contrast (bright environment), large touch targets (gloved hands),
  auditory + haptic alerts (can't always see screen).
**Success**:
  - Functional: Show vitals for 6 patients simultaneously, alert within 5 sec
  - Usability: Identify critical patient in < 2 sec, acknowledge alert in 1 tap
  - Accessibility: WCAG AA, min 44x44 touch targets, works with gloves
  - Business: 50% reduction in response time to critical events
**Platform**: iPad, React Native, design system uses 8px grid, Inter font
**Style**: Healthcare/clinical, trust-first palette (blue-600 primary),
  high-contrast mode default, minimal animation, serious tone
**Anti-goals**: NOT a consumer health app, NOT a charting system,
  NOT replacing bedside monitors
```

This constraint stack pastes into any Sumi BUILD command:
```
/screen patient-monitoring dashboard

[paste constraint stack]
```

The AI now generates a screen calibrated to Maria's exact needs, environment, and success criteria — not a generic healthcare dashboard.
