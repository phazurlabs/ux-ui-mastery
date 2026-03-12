---
description: "Comprehensive design audit — heuristic, cognitive, flow, fortification, cognitive load analysis, and summary scoring in one command. Run all lenses or pick specific sections."
tier: "review"
---

# Audit — Comprehensive Design Audit

Run every diagnostic lens against a design in a single pass. This is the master audit command — it evaluates heuristics, cognitive load, user flows, dark patterns, responsive edge cases, content quality, cognitive load analysis (Laws of UX, Gestalt, attention mapping, decision architecture), and produces a unified score with a priority roadmap.

**Accepts**: Code (file paths or pasted), screenshot description, URL description, or Figma reference.

**Section targeting**: Run the full audit or request specific sections:
- `/audit` — Full audit (all 6 sections)
- `/audit heuristic` or `/audit section-a` — Heuristic only
- `/audit cognitive` or `/audit section-b` — Cognitive only
- `/audit flow` or `/audit section-c` — Flow only
- `/audit fortify` or `/audit section-d` — Fortification only
- `/audit slop` or `/audit section-d6` — AI Slop Analysis only
- `/audit cogload` or `/audit section-e` — Cognitive Load Analysis only
- `/audit score` or `/audit section-f` — Summary score only (requires prior sections)
- `/audit a11y` — Redirects to `/a11y` (standalone accessibility audit)

---

## Pre-Audit: Context Gathering

Before running any section, establish the baseline:

1. **What is being audited**: Component, screen, flow, or full application
2. **Design intent**: What was the designer trying to achieve? What problem does this solve?
3. **Target users**: Who uses this? Sophistication level, context, accessibility needs
4. **Sector**: Industry determines what counts as a violation vs. an intentional convention
5. **Platform**: Web, iOS, Android, cross-platform, responsive targets
6. **Constraints**: Timeline, technical, business trade-offs the designer operated within
7. **Prior Sumi outputs**: Check for `/taste`, `/benchmark`, `/vision`, `/tokens`, `/screen` outputs. Consume them as baseline context if available
8. **Specific concerns**: Does the designer suspect weak areas? Prioritize those

If the user provides limited context, proceed with what is available and flag assumptions. Do not block on missing information.

---

## Section A: Heuristic Audit

Evaluate against Nielsen's 10 usability heuristics with cognitive principle grounding for every finding.

### A.1 — Heuristic Evaluation (H1-H10)

For each heuristic, evaluate whether the design complies, partially complies, or violates:

| ID | Heuristic | Core Question |
|----|-----------|---------------|
| H1 | Visibility of System Status | Does the system always tell the user what is happening, within reasonable time? |
| H2 | Match Between System and Real World | Does the system use the user's language, follow real-world conventions, and present information in a natural order? |
| H3 | User Control and Freedom | Can users undo, redo, and exit unwanted states without penalty? |
| H4 | Consistency and Standards | Do similar elements behave the same way? Are platform conventions followed? |
| H5 | Error Prevention | Does the design prevent errors before they happen through constraints, confirmations, and defaults? |
| H6 | Recognition Rather Than Recall | Is all necessary information visible or easily retrievable without memorization? |
| H7 | Flexibility and Efficiency of Use | Does the interface serve both novice and expert users with shortcuts and customization? |
| H8 | Aesthetic and Minimalist Design | Does every element serve a purpose? Is signal-to-noise ratio optimized? |
| H9 | Help Users Recognize, Diagnose, and Recover from Errors | Are error messages expressed in plain language, indicating the problem and suggesting a solution? |
| H10 | Help and Documentation | Is help available, searchable, focused on the user's task, and concise? |

### A.2 — Finding Documentation

For EACH finding, document:

- **Heuristic violated**: H1-H10 identifier
- **Underlying cognitive principle**: Every heuristic violation has a deeper cognitive reason. Cite it:
  - H1 violation -> Doherty Threshold (system feels unresponsive) or Zeigarnik Effect (incomplete tasks create anxiety)
  - H2 violation -> Mental Model theory (interface doesn't match user's existing understanding)
  - H3 violation -> Learned Helplessness (user loses sense of control)
  - H4 violation -> Jakob's Law (users transfer expectations from other products)
  - H5 violation -> Cognitive Load Theory (user is forced to hold too much in working memory to avoid errors)
  - H6 violation -> Miller's Law (interface demands recall of >7 items instead of showing them)
  - H7 violation -> Power Law of Practice (experts need accelerators to maintain engagement)
  - H8 violation -> Signal-to-Noise Ratio (irrelevant information competes with relevant)
  - H9 violation -> Error Recovery Theory (users cannot self-correct without actionable guidance)
  - H10 violation -> Situated Cognition (help must be contextual to be useful)
- **Location**: Exact element, component, or screen where the issue occurs
- **Description**: Clear explanation of the problem
- **Severity**: Use the Nielsen severity scale:
  - **0 — Cosmetic**: Not a usability problem unless extra time is available
  - **1 — Minor**: Cosmetic problem that doesn't affect task completion
  - **2 — Moderate**: Users can work around it, but it causes delay or frustration
  - **3 — Major**: Significant usability problem that causes task failure for some users
  - **4 — Catastrophe**: Must be fixed before release. Blocks task completion or causes data loss
- **Recommendation**: Specific, actionable fix
- **Code fix**: When code is provided, include corrected code

### A.3 — Mental Model Assessment

Verify whether the interface communicates a clear, correct mental model:

- **Conceptual model**: Does the interface clearly communicate what this system is and how it works?
- **Navigational model**: Can the user predict where actions will take them? Is the information architecture intuitive?
- **Interaction model**: Do controls behave the way the user expects based on their appearance? (e.g., does something that looks clickable respond to clicks?)
- **Model gaps**: Where does the interface's model diverge from the user's likely expectation? Flag these as HIGH SEVERITY — mental model mismatches cause the deepest usability failures

Reference: Norman's Gulf of Execution and Gulf of Evaluation (1988).

---

## Section B: Cognitive Audit

Audit against cognitive psychology principles — Laws of UX, Gestalt principles, cognitive biases, attention science, and memory constraints.

### B.1 — Laws of UX Evaluation

| Law | What to Check |
|-----|---------------|
| **Hick's Law** | How many choices are presented simultaneously? Are options progressively disclosed? Is decision time proportional to importance? |
| **Fitts's Law** | Are primary actions large enough and positioned near focus? Are destructive actions distant from constructive ones? Mobile tap targets >= 44pt? |
| **Miller's Law** | Are more than 4-7 items presented without chunking? Is information grouped into meaningful clusters? |
| **Jakob's Law** | Does the interface follow platform/industry conventions? Where does it deviate, and is the deviation justified? |
| **Doherty Threshold** | Do interactions respond within 400ms? Are delays masked with feedback (progress, skeleton, optimistic UI)? |
| **Peak-End Rule** | What is the emotional peak of the experience? What is the final moment? Are both deliberately designed? |
| **Von Restorff Effect** | Does the most important element visually stand out? Is distinctiveness used strategically (not everywhere)? |
| **Serial Position Effect** | Are the most important items placed first and last in lists/menus? |
| **Aesthetic-Usability Effect** | Is visual polish potentially masking usability problems? |
| **Tesler's Law** | Has complexity been reduced as far as possible without removing essential functionality? |
| **Postel's Law** | Is the interface liberal in what it accepts from users (flexible input parsing, forgiving formatting)? |
| **Zeigarnik Effect** | Are incomplete tasks creating productive engagement or anxiety? |

### B.2 — Gestalt Principles Evaluation

- **Proximity**: Are related elements close together? Are unrelated elements sufficiently separated?
- **Similarity**: Do similar elements share consistent visual treatment?
- **Closure**: Can users complete partial patterns mentally? Are shapes and regions implied effectively?
- **Continuity**: Do visual flows guide the eye in the intended direction?
- **Common Region**: Are groups enclosed or backgrounded to show relationship?
- **Figure-Ground**: Is the primary content clearly distinguished from background?
- **Common Fate**: Do elements that function together animate or move together?

### B.3 — Cognitive Load Analysis

- **Intrinsic load**: Is task complexity managed through decomposition (wizard, progressive form)?
- **Extraneous load**: What unnecessary cognitive demands does the design impose? (confusing labels, hidden controls, inconsistent patterns, visual noise)
- **Germane load**: Does the design build reusable mental schemas through consistency?
- **Working memory demand**: At any single step, how many items must the user hold in working memory? Flag if > 4

### B.4 — Cognitive Bias Scan

Scan for bias exploitation or risk:

| Bias | Check |
|------|-------|
| Anchoring | Are reference points fair or manipulative? |
| Default bias | Do defaults serve users or the business? |
| Confirmation bias | Does the interface surface disconfirming information? |
| Framing effect | Is information framed neutrally or manipulatively? |
| Choice overload | Are there too many options without curation? |
| Sunk cost framing | Does the design leverage past investment to trap users? |
| FOMO/scarcity | Are urgency signals real or fabricated? |
| Social proof | Is social proof genuine or manufactured? |

### B.5 — Cognitive Domain Scoring

Score each domain 1-10:

| Domain | Score Criteria |
|--------|---------------|
| Decision Architecture | Choice count, defaults, progressive disclosure |
| Visual Cognition | Gestalt compliance, hierarchy clarity, figure-ground |
| Memory Load | Working memory demand, recognition vs. recall, chunking |
| Attention Management | Focus direction, interruption protection, sustained attention support |
| Bias Ethics | Fair defaults, neutral framing, no dark patterns |

**Cognitive Health Score**: Average of 5 domains (X/10)

---

## Section C: Flow Audit

Audit a complete user journey across multiple screens or steps, identifying friction, drop-off risks, and emotional arc quality.

### C.1 — Flow Classification

- **Flow type**: Onboarding, signup, checkout, settings change, content creation, search-to-action, account recovery, upgrade/upsell, or custom
- **Criticality**: Revenue-critical, retention-critical, trust-critical, or utility
- **Entry point**: Where users come from
- **Success state**: What "done" looks like
- **Platform context**: Mobile, desktop, cross-device, embedded

### C.2 — Step Mapping

Enumerate every distinct screen, modal, or interaction step from entry to completion:

For each step document:
- Screen name and purpose
- Primary action (the ONE thing the user should do)
- Secondary actions available
- Data collected or displayed
- Decisions the user must make
- Branching paths (conditional steps, error branches, optional steps)
- System-initiated steps (loading, processing, verification emails, SMS codes)

Calculate:
- Total step count vs. recommended step count for this flow type
- Estimated time-to-completion

### C.3 — Per-Step Cognitive Load

For each step:
- Count decisions (Hick's Law — each decision adds friction)
- Count input fields (Miller's Law — keep chunks to 4 +/- 1)
- Assess visual complexity (information density, competing CTAs, distractions)
- Track cumulative cognitive load across the flow (load should not monotonically increase)
- Flag steps where load spikes unexpectedly

### C.4 — Drop-Off Risk Assessment

Rate each step 1-5 for drop-off risk based on:
- Effort required
- Value unclear to user
- Trust barrier present
- Technical friction (slow loading, complex input)
- Interruption likelihood

Identify the "valley of death" — the step with highest drop-off risk.

Check:
- Is value demonstrated before effort is demanded? (Reciprocity Principle)
- Does progress indication exist and is it accurate?
- Can users save progress and return later?

### C.5 — Emotional Arc Analysis (Peak-End Rule)

Map emotional valence per step:

```
Step 1: ████████░░ Curiosity (positive)
Step 2: ██████░░░░ Effort (neutral)
Step 3: ████░░░░░░ Friction (negative)  <- Valley of Death
Step 4: ████████░░ Relief (positive)    <- Designed Peak
Step 5: ██████████ Accomplishment       <- Strong End
```

Verify:
- At least one designed peak moment (positive surprise, social proof, personalization)
- End state is emotionally positive (confirmation, celebration, immediate value delivery)
- No negative emotional clusters (consecutive friction steps without relief)

### C.6 — Error Recovery Mid-Flow

- What happens if the user makes an error at step 3 of 7? Do they lose progress?
- Is back-navigation safe (no data loss)?
- Can users save progress and return later?
- Are error messages contextual and recovery-oriented?

### C.7 — Flow Dimension Scoring

Score each dimension 1-10:

| Dimension | What It Measures |
|-----------|-----------------|
| Flow Efficiency | Ratio of necessary to total steps — can steps be cut or merged? |
| Cognitive Progression | Does cognitive load distribute well or spike dangerously? |
| Emotional Arc | Is the Peak-End Rule satisfied? Delight and strong closure? |
| Error Recovery | Can users recover from mistakes without restarting? |
| Completion Likelihood | Given all factors, what percentage of users will finish? |

**Overall Flow Score**: Average of 5 dimensions (X/10)

---

## Section D: Fortification

Scan for defensive design issues — dark patterns, responsive edge cases, content/tone, and error recovery.

### D.1 — Dark Pattern Scan

Scan for 20+ deceptive design categories:

**Coercion patterns**:
- Confirmshaming — guilt-tripping the user into opting in
- Forced continuity — free trial converts to paid without clear warning
- Roach motel — easy to sign up, impossible to cancel
- Forced action — requiring account creation or social sharing to proceed

**Sneaking patterns**:
- Hidden costs — fees revealed only at checkout
- Sneak into basket — items added without explicit consent
- Bait and switch — advertising one thing, delivering another
- Hidden subscription — recurring charge buried in terms

**Interface manipulation**:
- Trick questions — double negatives or confusing opt-in/opt-out toggles
- Misdirection — visual design draws attention away from important information
- Disguised ads — ads styled to look like content or navigation
- False hierarchy — making the company-preferred option visually dominant

**Privacy violations**:
- Privacy zuckering — confusing privacy settings defaulting to maximum data sharing
- Address book leeching — requesting contacts without clear purpose
- Surveillance indicators — excessive data collection for the service provided

**Urgency/scarcity**:
- Fake urgency — countdown timers with no real deadline
- Fake scarcity — "Only 2 left!" without real inventory limits
- Fake social proof — fabricated reviews or user counts

**Obstruction**:
- Hard to cancel — cancellation flow harder than signup
- Hidden settings — important controls buried deep
- Comparison prevention — making plan comparison deliberately difficult

For each detected pattern, document:
- **Pattern name and category**
- **Location**: Specific component, screen, or flow
- **Severity**: Illegal (violates FTC/GDPR/DSA), Deceptive, Manipulative, or Questionable
- **Regulatory risk**: Specific laws/regulations that apply
- **Ethical redesign**: How to achieve the business goal without the dark pattern

If clean: "No dark patterns detected across 20+ categories scanned."

### D.2 — AI Trust Audit

**Skip if no AI features are present.** Output "N/A — no AI features detected."

If AI features exist, audit:

| Dimension | Score (1-10) | Questions |
|-----------|-------------|-----------|
| Transparency | | Does the user know when AI is deciding? Are outputs labeled? Are limitations disclosed? |
| Control | | Can the user override AI? Opt out? Provide feedback? Escalate to human? |
| Safety | | What happens when AI is wrong? Guardrails against harm? Bias monitoring? |
| Usability | | Does AI enhance or complicate UX? Is confidence communicated? |

**AI Trust Score**: Average of 4 dimensions (X/10)

### D.3 — Content & Tone Review

**Clarity**:
- Is every label, button, and message unambiguous?
- Can the user predict what will happen before they act?
- Flag jargon, unexplained acronyms, or insider language

**Tone consistency**:
- Does voice match throughout the product?
- Does tone match brand and sector expectations?
- Is tone appropriate for context? (playful error messages for banking = mismatch)

**Inclusive language**:
- No gendered assumptions
- No ableist language ("see below" vs. "refer to")
- No cultural bias or untranslatable idioms
- No age-related assumptions

**Error messages**:
- Helpful and specific? (not "Something went wrong")
- Tell the user what happened AND what to do next?
- Friendly tone without blame?
- Provide a recovery path (retry button, support link, alternative action)?

**CTAs**:
- Action-oriented with clear outcome? ("Create Account" not "Submit")
- Consistent verb patterns?
- Button text matches the result? ("Delete Account" not "Continue" for destructive actions)

**Readability**:
- Flesch-Kincaid grade level appropriate for audience
- Sentence length reasonable (avg <20 words)
- Paragraph length manageable (max 3-4 sentences in UI)

**i18n readiness**:
- Text externalized from code (not hardcoded strings)?
- Date/number formatting locale-aware?
- Text expansion room (German/French can be 30% longer)?
- No text embedded in images?
- RTL layout considerations if applicable?

Format rewrites as: "Current: [X] -> Recommended: [Y] -- Reason: [Z]"

### D.4 — Responsive & Cross-Device Edge Cases

Check at 5 breakpoints:

| Breakpoint | Key Checks |
|-----------|------------|
| **Mobile (375px)** | Single column? Touch targets >= 44px? Line length <= 75 chars? Mobile nav pattern? No horizontal scroll? |
| **Tablet (768px)** | 2-column adaptation? Touch + pointer both work? Modal sizing appropriate? Split view patterns? |
| **Laptop (1024px)** | Multi-column + sidebar? Hover states present? Keyboard nav functional? |
| **Desktop (1280px)** | Full layout as designed? Max-width container? Comfortable density? |
| **Wide (1536px+)** | Content constrained to readable width? No awkward stretching? Grid fills proportionally? |

**Cross-cutting checks**:
- No horizontal scrolling at any breakpoint
- Print stylesheet if content is printable
- Orientation changes handled (portrait to landscape)
- Input mode transitions (touch to keyboard to mouse)

### D.5 — Microcopy & Error Recovery Deep-Dive

- Every form field: label, placeholder, helper text, error message — all present and clear?
- Empty states: Do they explain what to do, not just say "No items"?
- Loading states: Skeleton screens, progress indicators, or optimistic UI?
- Success states: Confirmation with next action?
- Destructive action confirmations: Clear consequences stated?
- Undo availability: Can the user reverse the last action?

### D.6 — AI Slop Analysis

A thorough scan for AI-generated UI patterns that indicate the design was output by an AI with little or no human design refinement. This goes deeper than a surface check — it evaluates systemic design quality gaps that AI tools consistently produce.

#### D.6.1 — Visual Homogeneity Scan

- **Default palette detection**: Does the design use only Tailwind defaults without customization? Check for the "purple gradient epidemic" — default indigo/violet palette (bg-indigo-500, bg-purple-600, bg-violet-500, from-indigo-500 to-purple-600). Flag white/near-white backgrounds with purple accents as the #1 AI-generated look
- **Component homogeneity**: Do all components follow the same generic card + rounded-lg + shadow-md pattern? Are there any components with unique visual treatments?
- **Hero section analysis**: Flag hero sections with centered text on gradient backgrounds — the most common AI layout pattern
- **Color palette origin**: Is the palette a stock Tailwind palette, a stock theme palette, or a custom/intentional palette? Evidence: custom CSS properties, extended theme config, or raw Tailwind utility classes
- **Visual monotony score**: Rate 1-10 how visually homogeneous the design is (1 = rich variety, 10 = every section looks identical)

#### D.6.2 — Design System Gap Analysis

For each category, determine whether the design has an intentional system or is using arbitrary values:

| Category | Has System? | Evidence |
|----------|-------------|----------|
| **Design tokens** | Yes/No | Are there CSS custom properties, theme config, or hardcoded values? |
| **Type scale** | Yes/No | Do font sizes follow a consistent ratio (1.2, 1.25, 1.333, 1.5, 1.618) or are sizes arbitrary? |
| **Spacing system** | Yes/No | Is there a consistent spacing scale (4, 8, 12, 16, 24, 32, 48, 64) or arbitrary padding/margin values? |
| **Border-radius scale** | Yes/No | Is there a consistent radius scale or mixed values (rounded-md here, rounded-lg there, rounded-xl elsewhere)? |
| **Elevation/shadow system** | Yes/No | Is there a deliberate shadow hierarchy (sm, md, lg mapped to elevation levels) or random shadow usage? |
| **Semantic colors** | Yes/No | Are semantic colors used (primary, error, success, warning) or raw color values (bg-red-500, bg-green-400)? |
| **Font pairing** | Yes/No | Is there an intentional heading/body font pairing, or a single font with no typographic contrast? |

**Design System Score**: Count of "Yes" answers out of 7. Below 3 = strong indicator of AI-generated output.

#### D.6.3 — State Coverage Audit

For each interactive component found in the design, check whether these states are implemented:

| State | Description | What to Look For |
|-------|-------------|------------------|
| **Default** | Resting state | Component renders correctly at rest |
| **Hover** | Mouse over | Visual change on hover (color shift, underline, shadow lift) |
| **Focus** | Keyboard focus | focus-visible ring or equivalent indicator |
| **Active/Pressed** | Click/tap down | Visual compression, color darken, or scale reduction |
| **Disabled** | Not interactive | Reduced opacity, cursor-not-allowed, aria-disabled |
| **Loading** | Async operation in progress | Spinner, skeleton, shimmer, or progress indicator |
| **Error** | Invalid or failed | Red border, error message, recovery action |
| **Empty** | No data | Illustration or message explaining what to do |
| **Success** | Completed | Confirmation message, checkmark, green indicator |

Document findings per component:

| Component | Default | Hover | Focus | Active | Disabled | Loading | Error | Empty | Success | Coverage |
|-----------|---------|-------|-------|--------|----------|---------|-------|-------|---------|----------|
| [name] | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | X/9 |

**State Coverage Score**: Average coverage across all interactive components. Below 4/9 = strong indicator of AI-generated output.

#### D.6.4 — AI Slop Severity Rating

Based on findings from D.6.1, D.6.2, and D.6.3, assign an overall AI Slop severity:

| Rating | Criteria | Action |
|--------|----------|--------|
| **None** | Custom palette, intentional type system, full state coverage, visual variety | No action needed |
| **Mild** | 1-2 default patterns detected, mostly custom design, minor state gaps | Note in findings, low priority |
| **Moderate** | Stock palette with minimal customization, weak type system, several missing states | Recommend `/fix` pass to customize defaults and add missing states |
| **Severe** | Default Tailwind palette, no type scale, most states missing, generic card layouts everywhere | Strongly recommend `/fix` — design needs significant human refinement |
| **Critical** | Full default palette, no design system, minimal states, cookie-cutter AI layout, purple gradient syndrome | This is raw AI output. Run `/fix` immediately before any other work |

For the assigned rating, provide:
- **Rating**: [None / Mild / Moderate / Severe / Critical]
- **Evidence**: List the specific findings that justify the rating (cite D.6.1, D.6.2, D.6.3 findings)
- **Recommended action**: If Moderate or above, recommend `/fix` with specific areas to address

---

## Section E: Cognitive Load Analysis

Evaluate the design through the lens of cognitive psychology. Score how well the interface respects human cognitive limitations and leverages perceptual principles.

### E.1 — Laws of UX Evaluation

Evaluate compliance with key Laws of UX:

| Law | What to Check | Violation Example |
|-----|--------------|-------------------|
| **Hick's Law** | Decision time increases logarithmically with number of choices. Count choices per viewport. | Navigation with 15+ top-level items. Settings page with 30 uncategorized toggles. Dropdown with 50+ unsearchable options. |
| **Miller's Law** | Working memory holds 7±2 items. Count information chunks per section. | Dashboard showing 12 ungrouped metrics. Form with 15 fields on one step. Tab bar with 8 items. |
| **Fitts's Law** | Time to target depends on distance and size. Check CTA sizes and positions. | Tiny "Submit" button far from form. Close button as small X in corner. Important action requires precision click. |
| **Jakob's Law** | Users spend most time on other sites — they expect yours to work like those. Check convention compliance. | Logo in the center instead of top-left. Cart icon on the left side. Search that doesn't use a magnifying glass icon. |
| **Law of Proximity** | Elements close together are perceived as related. Check grouping logic. | Unrelated elements grouped tightly. Related elements separated by whitespace. Form labels far from their inputs. |
| **Law of Similarity** | Similar-looking elements are perceived as related. Check visual consistency. | Different button styles for the same action type. Inconsistent card treatments for same-category items. |
| **Law of Common Region** | Elements within a boundary are perceived as grouped. Check container usage. | No visual boundaries between content sections. Borders/backgrounds that group unrelated items. |
| **Aesthetic-Usability Effect** | Users perceive attractive designs as more usable. Rate overall aesthetic quality. | Functional but visually unpolished interface creates perception of poor usability. |
| **Doherty Threshold** | System response must be <400ms for flow state. Check perceived performance. | No loading indicators. Slow transitions. No optimistic UI for common actions. |
| **Peak-End Rule** | Users judge experience by its peak moment and end. Check critical and final moments. | No success celebration on completion. Error states that feel harsh. Abrupt endings. |
| **Von Restorff Effect** | Distinctive items are more memorable. Check if CTAs stand out. | Primary CTA doesn't visually differentiate from secondary actions. Everything is the same visual weight. |
| **Zeigarnik Effect** | People remember uncompleted tasks. Check progress indication. | Multi-step form with no progress bar. Task list with no completion states. Onboarding with no progress indicator. |

For each law, rate:
- **Compliant** (actively applied)
- **Neutral** (not applicable or no violation)
- **Violation** (law is violated with negative UX impact)

### E.2 — Gestalt Principles Audit

Evaluate how the layout uses (or violates) Gestalt principles:

| Principle | What to Check |
|-----------|--------------|
| **Figure/Ground** | Is it clear what is foreground content vs. background? Do overlapping elements have sufficient contrast? |
| **Closure** | Are incomplete shapes/patterns interpretable? Do icon metaphors rely on user completing the visual? |
| **Continuity** | Do elements create clear visual lines the eye can follow? Is the reading flow smooth? |
| **Symmetry** | Are layouts balanced? Does asymmetry feel intentional or accidental? |
| **Common Fate** | Do elements that belong together move/animate together? |
| **Focal Point** | Is there a single clear entry point per viewport? Where does the eye land first? |

### E.3 — Attention Mapping

Analyze where user attention flows:

1. **Entry Point**: Where does the eye land first on each screen? Is this the most important element?
2. **Scanning Pattern**: Does the layout support natural scanning (F-pattern for text, Z-pattern for marketing)?
3. **Visual Hierarchy Score**: Rank elements by visual weight (size, color, contrast, position). Does this ranking match the information priority?
4. **Distraction Audit**: Identify elements that compete for attention when they shouldn't (animations, bright colors on non-priority elements, decorative elements that distract from content)
5. **Progressive Disclosure**: Is information revealed at the right time, or is everything shown at once?

### E.4 — Decision Architecture

Evaluate how the interface structures user decisions:

- **Choice Architecture**: Are default options set appropriately? Are destructive actions guarded?
- **Cognitive Friction**: Where does the interface create unnecessary mental effort? (Unclear labels, ambiguous icons, missing context)
- **Error Prevention**: Does the design prevent errors before they happen? (Disabled invalid options, confirmation for destructive actions, undo capability)
- **Mental Model Alignment**: Does the interface's conceptual model match how users think about the task?
- **Information Scent**: Can users predict what they'll find behind links/buttons from the label alone?

### E.5 — Cognitive Load Score

Calculate a composite cognitive load score:

| Dimension | Weight | Score (0-10) | Criteria |
|-----------|--------|-------------|----------|
| Information Density | 20% | — | 10: Right amount of info per viewport. 1: Overwhelming or barren |
| Decision Complexity | 20% | — | 10: Guided decisions, clear defaults. 1: Too many choices, no guidance |
| Visual Noise | 15% | — | 10: Clean, focused. 1: Cluttered, competing elements |
| Consistency | 15% | — | 10: Predictable patterns. 1: Every screen is different |
| Memory Load | 15% | — | 10: Recognition over recall, persistent context. 1: Must remember previous steps |
| Learning Curve | 15% | — | 10: Immediately intuitive. 1: Requires instruction manual |

**Cognitive Load Rating:**
- 8-10: Effortless — interface disappears, users focus on tasks
- 6-7: Manageable — minor cognitive friction in specific areas
- 4-5: Taxing — users must think about the interface, not their task
- 1-3: Overwhelming — interface creates anxiety, confusion, or decision paralysis

### E.6 — Findings Format

For each cognitive issue found:

```
#### [CogN]: [Issue Title]
**Law/Principle**: [Which cognitive principle is violated]
**Severity**: Critical / Major / Minor
**Location**: [Where in the UI]
**Current**: [What the design does now]
**Impact**: [How this affects users cognitively]
**Fix**: [Specific design recommendation]
**Code**: [If applicable, show the code change]
```

---

## Section F: Summary Score & Priority Roadmap

### F.1 — Composite Score Calculation

Compute the overall audit score (0-100):

| Section | Weight | Score Source | Raw Score |
|---------|--------|-------------|-----------|
| A: Heuristic | 20% | Usability score from A (1-100) | |
| B: Cognitive | 15% | Cognitive Health Score (1-10, scaled to 100) | |
| C: Flow | 15% | Flow Score (1-10, scaled to 100) | |
| D: Fortification | 15% | Weighted from D.1-D.5 (1-10, scaled to 100) | |
| E: Cognitive Load | 20% | Cognitive Load Score (0-10, scaled to 100) | |
| F: Consistency | 15% | Cross-section coherence (do findings align?) | |

**Overall Design Health Score: X/100**

Score interpretation:
- **90-100**: Ship-ready. Exceptional design with minor polish opportunities
- **75-89**: Strong. Ready to ship with targeted improvements
- **60-74**: Competent. Needs work on specific weak areas before shipping
- **40-59**: Needs significant work. Multiple critical issues across sections
- **0-39**: Redesign recommended. Fundamental problems in most areas

### F.2 — Priority Roadmap

Consolidate ALL findings from sections A-E into three tiers:

**Must-Fix (before ship)**:
- Severity 3-4 heuristic violations
- Critical cognitive load issues
- Dark patterns classified as Illegal or Deceptive
- Valley of Death steps with no recovery
- Missing error states on critical flows
- WCAG AA failures (redirect to `/a11y` for detailed fixes)

**Should-Fix (current sprint)**:
- Severity 2 heuristic violations
- Moderate cognitive load spikes
- Manipulative or Questionable dark patterns
- High drop-off risk steps
- Tone inconsistencies in critical flows
- Responsive breakpoint degradations

**Could-Improve (backlog)**:
- Severity 0-1 heuristic findings
- Cognitive optimization opportunities
- Content clarity improvements
- i18n readiness gaps
- Delight opportunities (Peak-End Rule improvements)
- Polish-level responsive adjustments

For EACH item in the roadmap:
- Finding summary (one line)
- Section source (A/B/C/D/E)
- Severity level
- Location in the interface
- Specific fix recommendation
- UX principle cited
- Effort estimate (quick win / half-day / multi-day / strategic)

### F.3 — Cross-Section Pattern Analysis

Identify themes that appear across multiple sections:
- If the same component fails in heuristic audit AND cognitive audit AND flow audit, it is a systemic problem
- If dark patterns and tone issues overlap, there may be an organizational culture issue
- If responsive and flow issues overlap, the mobile experience likely needs dedicated attention

Call out the top 3 systemic patterns with recommendations.

---

## Output Format

```
## Design Audit: [Target Name]

### Context
- **Target**: [component/screen/flow name]
- **Design intent**: [what the designer was trying to achieve]
- **Target users**: [who, sophistication, context]
- **Sector**: [industry and relevant conventions]
- **Platform**: [web/iOS/Android/cross-platform]
- **Constraints noted**: [trade-offs]
- **Prior Sumi context consumed**: [list or "none"]

---

### Overall Design Health Score: [X/100] — [Tier Label]

| Section | Score | Critical Findings | Total Findings |
|---------|-------|-------------------|----------------|
| A: Heuristic | [X/100] | [N] | [N] |
| B: Cognitive | [X/10 -> X/100] | [N] | [N] |
| C: Flow | [X/10 -> X/100] | [N] | [N] |
| D: Fortification | [X/10 -> X/100] | [N] | [N] |
| E: Cognitive Load | [X/10 -> X/100] | [N] | [N] |
| F: Consistency | [X/100] | — | — |

---

### Section A: Heuristic Audit

#### Findings (sorted by severity)

| # | Heuristic | Severity | Location | Issue | Cognitive Principle | Fix |
|---|-----------|----------|----------|-------|--------------------|----|
| 1 | H[N] | [0-4] | [where] | [what] | [principle] | [fix] |

#### Mental Model Assessment
- **Conceptual model**: [Clear/Unclear — explanation]
- **Navigational model**: [Predictable/Unpredictable — explanation]
- **Interaction model**: [Consistent/Inconsistent — explanation]
- **Model gaps**: [list mismatches — these are HIGH SEVERITY]

---

### Section B: Cognitive Audit

#### Domain Scores
| Domain | Score | Key Finding |
|--------|-------|-------------|
| Decision Architecture | X/10 | [one-line] |
| Visual Cognition | X/10 | [one-line] |
| Memory Load | X/10 | [one-line] |
| Attention Management | X/10 | [one-line] |
| Bias Ethics | X/10 | [one-line] |

**Cognitive Health Score**: [X/10]

#### Laws of UX Findings
[Each violated law with location, evidence, and fix]

#### Gestalt Findings
[Principle violations with visual description and correction]

#### Cognitive Load Analysis
[Intrinsic, extraneous, germane load breakdown with reduction strategies]

#### Bias Audit
[Biases exploited or at risk, with ethical alternatives]

---

### Section C: Flow Audit

#### Flow Overview
- **Type**: [flow type]
- **Criticality**: [revenue/retention/trust/utility]
- **Total Steps**: [X] (recommended: [Y])
- **Estimated Time**: [X minutes]

#### Flow Diagram
[Entry] -> [Step 1] -> [Step 2] -> ... -> [Success State]

#### Per-Step Analysis
| Step | Screen | Cognitive Load (1-5) | Drop-off Risk (1-5) | Emotion | Issues |
|------|--------|---------------------|---------------------|---------|--------|

#### Emotional Arc
[Visual bar chart of emotional valence per step]

#### Flow Scores
| Dimension | Score | Observation |
|-----------|-------|------------|
| Flow Efficiency | X/10 | ... |
| Cognitive Progression | X/10 | ... |
| Emotional Arc | X/10 | ... |
| Error Recovery | X/10 | ... |
| Completion Likelihood | X/10 | ... |

**Overall Flow Score**: [X/10]

#### Optimization Recommendations
- **Steps to cut**: [eliminate zero-value steps]
- **Steps to merge**: [combine without overloading]
- **Steps to add**: [missing reassurance, trust, or progress moments]
- **Friction fixes**: [specific before/after for high-friction steps]

---

### Section D: Fortification

#### Dark Pattern Scan
[Findings or "Clean — no dark patterns detected across 20+ categories scanned."]

#### AI Trust Audit
[Findings or "N/A — no AI features detected."]

#### Content & Tone
[Findings with specific rewrites: "Current: [X] -> Recommended: [Y]"]

#### Responsive Edge Cases
[Per-breakpoint findings]

#### Microcopy & Error Recovery
[Findings with specific rewrites]

#### Fortification Score
| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| Ethics | 30% | X/10 | [why] |
| Trust | 20% | X/10 or N/A | [why] |
| Content | 25% | X/10 | [why] |
| Devices | 25% | X/10 | [why] |

**Fortification Score**: [X/10]

---

### Section D.6: AI Slop Analysis

#### Visual Homogeneity Scan
- **Palette**: [Stock Tailwind / Custom — evidence]
- **Purple Gradient Syndrome**: [Detected / Not detected — evidence]
- **Component Homogeneity**: [High / Medium / Low — evidence]
- **Hero Pattern**: [AI-generic / Intentional — evidence]
- **Visual Monotony Score**: [X/10]

#### Design System Gap Analysis
| Category | Has System? | Evidence |
|----------|-------------|----------|
| Design tokens | Y/N | [details] |
| Type scale | Y/N | [details] |
| Spacing system | Y/N | [details] |
| Border-radius scale | Y/N | [details] |
| Elevation/shadow system | Y/N | [details] |
| Semantic colors | Y/N | [details] |
| Font pairing | Y/N | [details] |

**Design System Score**: [X/7]

#### State Coverage Audit
| Component | Default | Hover | Focus | Active | Disabled | Loading | Error | Empty | Success | Coverage |
|-----------|---------|-------|-------|--------|----------|---------|-------|-------|---------|----------|
| [name] | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | Y/N | X/9 |

**State Coverage Score**: [X/9 average]

#### AI Slop Severity Rating
- **Rating**: [None / Mild / Moderate / Severe / Critical]
- **Evidence**: [specific findings from D.6.1-D.6.3]
- **Recommended action**: [next step or "No action needed"]

---

### Section E: Cognitive Load Analysis

#### Laws of UX Evaluation
| Law | Rating | Location | Evidence |
|-----|--------|----------|----------|
| [Law Name] | Compliant/Neutral/Violation | [where] | [evidence] |

#### Gestalt Principles Audit
| Principle | Rating | Evidence |
|-----------|--------|----------|
| [Principle] | Strong/Adequate/Weak | [evidence] |

#### Attention Mapping
- **Entry Point**: [analysis]
- **Scanning Pattern**: [F-pattern/Z-pattern compliance]
- **Visual Hierarchy Score**: [alignment assessment]
- **Distraction Audit**: [findings]
- **Progressive Disclosure**: [assessment]

#### Decision Architecture
- **Choice Architecture**: [assessment]
- **Cognitive Friction**: [findings]
- **Error Prevention**: [assessment]
- **Mental Model Alignment**: [assessment]
- **Information Scent**: [assessment]

#### Cognitive Load Score
| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| Information Density | 20% | X/10 | [why] |
| Decision Complexity | 20% | X/10 | [why] |
| Visual Noise | 15% | X/10 | [why] |
| Consistency | 15% | X/10 | [why] |
| Memory Load | 15% | X/10 | [why] |
| Learning Curve | 15% | X/10 | [why] |

**Cognitive Load Rating**: [X/10] — [Effortless/Manageable/Taxing/Overwhelming]

#### Cognitive Findings
[Each finding using CogN format with law/principle, severity, location, impact, fix]

---

### Section F: Priority Roadmap

#### Must-Fix (before ship)
| # | Finding | Section | Severity | Location | Fix | Principle | Effort |
|---|---------|---------|----------|----------|-----|-----------|--------|

#### Should-Fix (current sprint)
| # | Finding | Section | Severity | Location | Fix | Principle | Effort |
|---|---------|---------|----------|----------|-----|-----------|--------|

#### Could-Improve (backlog)
| # | Finding | Section | Severity | Location | Fix | Principle | Effort |
|---|---------|---------|----------|----------|-----|-----------|--------|

#### Systemic Patterns
1. [Pattern]: Appears in sections [X, Y, Z]. Root cause: [hypothesis]. Fix: [systemic recommendation]
2. [Pattern]: ...
3. [Pattern]: ...

---

### Next Steps
1. **Fix** must-fix items before shipping
2. **Run** `/a11y` for detailed accessibility audit with code fixes
3. **Run** `/roast` for quick opinionated critique
4. **Run** `/qa` to verify fixes match spec
5. **Run** `/grade` for visual quality scoring
```

---

## Quality Gates

The output MUST include:
- [ ] All 6 sections completed (or targeted section if user specified)
- [ ] Every finding has severity, location, fix recommendation, and UX principle cited
- [ ] Heuristic findings grounded in cognitive principles (not just "violates H4")
- [ ] Cognitive scores justified with specific observations
- [ ] Flow diagram with per-step cognitive load and drop-off risk
- [ ] Emotional arc visualization
- [ ] Dark pattern scan covering 20+ categories
- [ ] Content review with specific rewrites for every failing text
- [ ] Responsive check at 5 breakpoints
- [ ] Composite score computed with visible weights
- [ ] Priority roadmap with three tiers and effort estimates
- [ ] Systemic pattern analysis across sections
- [ ] Code fixes included when code input is provided
- [ ] AI Slop Analysis completed (D.6) with visual homogeneity scan, design system gap analysis, state coverage audit, and severity rating
- [ ] Cognitive Load Analysis completed (E) with Laws of UX evaluation, Gestalt audit, attention mapping, decision architecture, and composite cognitive load score

The output MUST NOT include:
- Vague findings ("could be better", "needs work") — every issue must be specific and actionable
- Scores without justification — every score must explain what earned or lost points
- Recommendations without grounding — every fix must cite a UX principle
- Dark pattern scan checking fewer than 20 categories
- AI trust audit on products without AI features (skip cleanly)
- Responsive findings without specific breakpoint data
- Missing roadmap — every finding must route to a tier with a fix

---

## Cross-References

When running the audit, draw knowledge from these skills:

- `nng-ux-heuristics` — Heuristic evaluation methodology, severity rating framework
- `cognitive-psychology-ux` — Laws of UX, Gestalt, cognitive load, mental models, biases
- `ux-ethics-content-strategy` — Dark pattern taxonomy, ethical design, content strategy, tone
- `ai-spatial-voice-ux` — AI transparency, trust patterns
- `agentic-ai-generative-ux` — AI safety guardrails, generative UI ethics
- `platform-visual-standards` — Responsive standards per device type, platform conventions
- `accessibility-inclusive-design` — Inclusive language, WCAG compliance, universal design
- `cross-cultural-i18n-ux` — i18n readiness, cultural sensitivity
- `ui-pattern-intelligence` -> `anti-pattern-encyclopedia.md` — Dark pattern reference
- `ux-metrics-measurement` — Funnel metrics, drop-off benchmarks, conversion optimization
- `performance-states-patterns` — Loading states, skeleton screens, progress indicators
- `sector-style-intelligence` — Sector-specific conventions
- `micro-copy-intelligence` — Microcopy best practices for rewrites
- `design-critique-case-studies` — Critique methodology grounding

---

## Next Steps

After `/audit`, recommended paths:

- `/a11y` — Deep accessibility audit with WCAG 2.2 AA checklist and code fixes
- `/roast` — Quick opinionated design critique (10 dimensions, letter grade)
- `/grade` — Visual quality scoring (Awwwards-calibrated)
- `/qa` — Design QA (spec vs. implementation verification)
- `/remix` — Fix the issues found immediately
- `/ship` — Rebuild flagged components