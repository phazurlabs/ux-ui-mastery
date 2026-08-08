---
name: remix
description: "Redesign existing UI — fix top problems with UX reasoning for every change"
argument-hint: "[file, component, or screen to redesign]"
---

# Remix — Redesign with UX Reasoning

## Before running

This command needs a file, component, or screen to redesign.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Take an existing screen, component, or flow and redesign it with explicit UX reasoning for every single change. No change without a citation. No opinion without a principle.

This command produces runnable code — not just critique. It finds problems, proposes fixes, and ships the improved version.

## Design Memory Integration

Before redesigning, check for `.sumi/` in the user's project root:

- **`.sumi/style.json`** — If present, the redesigned code MUST use these design tokens (colors, spacing, typography, border radii). Do not invent new values. Map every CSS property to a token.
- **`.sumi/wireframe-*.json`** — If present, respect the layout structure and component map from wireframing. The remix changes implementation and visual treatment, not fundamental layout architecture (unless the layout IS the problem).
- **`.sumi/brief.json`** — If present, pull target users, constraints, and platform. Redesign for the documented audience, not a generic user.
- **`.sumi/decisions.log`** — If present, read prior design decisions. Do not contradict them without explicit justification.

After the redesign is approved, write decisions to `.sumi/decisions.log`:
```
[ISO-8601] REMIX: [component/screen name]
  Problems fixed: [count]
  Principles applied: [list]
  Tokens used: [yes/no — from .sumi/style.json]
  Changes: [summary]
```

---

## Remix Protocol

### Step 0: Accept Input

Determine what is being remixed and establish baseline context.

**Input types accepted**:
- Existing code (React/TypeScript, SwiftUI, HTML/CSS, Vue, Svelte, Angular)
- Screenshot description (user describes what they see)
- Component specification
- Wireframe description
- Live product URL description
- Figma frame description

**Required context** (ask if not provided):
1. What specifically do you want improved? (or "everything")
2. What platform? (React/TypeScript is default if not specified)
3. Are there constraints? (brand guidelines, tech stack, existing design system)
4. What is the user's primary task on this screen/component?
5. Who is the target user? (pull from `.sumi/brief.json` if available)

**Establish the tech stack**:
- Default: React + TypeScript + Tailwind CSS
- If the input is SwiftUI, output SwiftUI
- If the input is plain HTML/CSS, output HTML/CSS
- Match the input's technology unless the user requests a different stack

---

### Step 1: PROBLEM IDENTIFICATION — Top 5 UX Problems

Before touching anything, identify the top 5 UX problems. This is a diagnostic step — accurate diagnosis before treatment.

#### Problem Scanning Checklist

Scan the input systematically for these categories:

**Visual Hierarchy (Gestalt + Cognitive Load)**:
- Is there a clear visual hierarchy? Can you identify H1, H2, H3 at a glance?
- Does everything compete for attention equally? (hierarchy failure)
- Is the primary action visually dominant?
- Is there sufficient contrast between hierarchy levels?

**Cognitive Load (Miller's Law, Hick's Law)**:
- Too many choices on screen? (Hick's Law — decision time increases with options)
- Too many things to remember? (Miller's Law — 7 plus or minus 2 chunks)
- Can the user figure out what to do without instructions? (H2: Match between system and real world)
- Is the information architecture clear or muddled?

**Interaction Design (Fitts's Law, Affordance)**:
- Are interactive elements large enough? (Fitts's Law — 44px minimum touch, 24px minimum click)
- Are interactive elements recognizable as interactive? (signifiers, affordance)
- Is the click/tap target the same as the visual target? (no ghost targets)
- Are destructive actions protected from accidental activation?

**States & Feedback (H1: Visibility of System Status)**:
- Are loading states present?
- Are error states present and helpful?
- Are empty states present and actionable?
- Do actions provide immediate feedback?
- Are disabled states visually distinct and explained?

**Accessibility (WCAG 2.2)**:
- Color contrast ratio (minimum 4.5:1 for text, 3:1 for large text and UI)
- Touch target size (minimum 44x44pt iOS, 48x48dp Android, 24x24px web)
- Focus indicators visible?
- Screen reader support (aria labels, semantic HTML, heading structure)
- Keyboard navigation possible?
- Motion: can animations be disabled? (prefers-reduced-motion)

**Consistency (H4: Consistency and Standards)**:
- Are similar elements styled and behaving the same way?
- Do patterns match platform conventions? (Jakob's Law)
- Is spacing consistent?
- Are fonts/sizes consistent?
- Do buttons look and behave the same throughout?

**Dark Patterns & Ethics**:
- Shame clicks ("No thanks, I don't want to save money")
- Hidden costs or information
- Forced actions (newsletter signup to access content)
- Manipulative visual weight (making the option YOU want more prominent)
- Confirmshaming

#### Problem Documentation Format

For each of the top 5 problems:

| Field | Value |
|-------|-------|
| **Problem** | Clear, specific description of the issue |
| **Location** | Exact element or area affected (line number if from code) |
| **Severity** | Critical (blocks users) / Major (frustrates users) / Minor (suboptimal) / Cosmetic (polish) |
| **Principle Violated** | The specific heuristic, law, or criterion being broken |
| **User Impact** | What happens to the user because of this problem — behavioral consequence |
| **Evidence** | Why this is a problem, not a personal preference. Research, data, or principle citation. |

#### Principle Reference Library

Cite these by name — not vaguely ("usability issue") but specifically:

**Nielsen's 10 Heuristics**:
- H1: Visibility of System Status
- H2: Match Between System and Real World
- H3: User Control and Freedom
- H4: Consistency and Standards
- H5: Error Prevention
- H6: Recognition Rather than Recall
- H7: Flexibility and Efficiency of Use
- H8: Aesthetic and Minimalist Design
- H9: Help Users Recognize, Diagnose, and Recover from Errors
- H10: Help and Documentation

**Cognitive Laws**:
- Fitts's Law — Time to reach target = f(distance, size). Larger targets closer to cursor = faster.
- Hick's Law — Decision time = f(number of choices). Fewer options = faster decisions.
- Miller's Law — Working memory holds 7 plus or minus 2 chunks. Group information into chunks.
- Jakob's Law — Users spend most of their time on OTHER sites. They expect yours to work the same.
- Tesler's Law — Every system has irreducible complexity. The question is who bears it: user or system.
- Postel's Law — Be liberal in what you accept, conservative in what you produce.
- Doherty Threshold — Productivity soars when system responds in < 400ms.

**Perception Laws**:
- Von Restorff Effect — Isolated items are remembered better. Use for CTAs.
- Serial Position Effect — First and last items in a list are remembered best.
- Peak-End Rule — Experiences are judged by the peak moment and the ending.
- Zeigarnik Effect — Incomplete tasks are remembered better than complete ones (progress bars work).

**Gestalt Principles**:
- Proximity — Elements close together are perceived as related.
- Similarity — Elements that look alike are perceived as related.
- Continuity — The eye follows smooth paths.
- Closure — The mind fills in gaps to see complete shapes.
- Common Region — Elements within a boundary are perceived as grouped.
- Figure-Ground — Elements are perceived as either foreground or background.

**WCAG 2.2 (cite specific criteria)**:
- 1.4.3 Contrast (Minimum) — 4.5:1 for normal text
- 1.4.11 Non-text Contrast — 3:1 for UI components
- 2.4.7 Focus Visible — Visible focus indicator
- 2.5.8 Target Size (Minimum) — 24x24px CSS pixels
- 2.4.6 Headings and Labels — Descriptive headings

---

### Step 2: PROPOSE FIXES — Before/After for Each Problem

For each identified problem, propose a specific fix with before/after comparison:

#### Fix Proposal Format

**Problem [N]: [Name]**

| Aspect | Before | After |
|--------|--------|-------|
| **Visual** | [What it looks like now] | [What it will look like] |
| **Behavior** | [How it works now] | [How it will work] |
| **Code** | [Key code difference — the specific property/component change] | [New code approach] |

**Principle applied**: [Specific principle name + how it applies]
**Expected impact**: [What metric or behavior this should improve — task completion rate, time-on-task, error rate, satisfaction]

#### Fix Priority

Order fixes by impact:
1. **Critical fixes first** — things that block users or cause errors
2. **Major fixes second** — things that frustrate users or slow them down
3. **Minor fixes third** — things that are suboptimal but functional
4. **Cosmetic fixes last** — polish that improves perception but not function

---

### Step 3: OUTPUT REDESIGNED CODE

Generate the complete, production-ready redesigned code. Not a diff — the full, runnable component.

#### Code Requirements

**Completeness**:
- The output must be a complete, self-contained, runnable component
- All imports included
- All types/interfaces defined
- All states handled (default, hover, focus, active, disabled, loading, error, empty, success)
- All accessibility attributes included (aria-label, role, tabIndex, alt text)
- Responsive behavior built in (not a TODO)

**Design Token Integration**:
- If `.sumi/style.json` exists, use those tokens exclusively:
  ```tsx
  // Use tokens from .sumi/style.json
  className="bg-primary-500 text-white px-spacing-4 py-spacing-2 rounded-radius-md"

  // NOT arbitrary values
  className="bg-blue-500 text-white px-4 py-2 rounded-lg"
  ```
- If no tokens exist, use sensible Tailwind defaults but note which values should become tokens

**Annotation**:
- Every significant change must have a comment explaining WHY:
  ```tsx
  {/* Fitts's Law: Increased touch target to 48px for mobile accessibility */}
  <button className="min-h-[48px] min-w-[48px] ...">

  {/* Von Restorff Effect: Primary CTA isolated with whitespace to draw attention */}
  <div className="mt-8 mb-4">
    <Button variant="primary" size="lg">Get Started</Button>
  </div>

  {/* H1: Visibility of System Status — Loading skeleton matches content shape */}
  {isLoading && <Skeleton className="h-6 w-3/4" />}

  {/* Hick's Law: Reduced from 8 actions to 3 primary + overflow menu */}
  <ActionGroup>
    <Button>Save</Button>
    <Button>Preview</Button>
    <OverflowMenu items={secondaryActions} />
  </ActionGroup>
  ```

**State Handling**:
```tsx
// Every interactive component must handle these states:
// 1. Default — normal appearance
// 2. Hover — visual feedback on mouse over (desktop)
// 3. Focus — visible focus ring for keyboard navigation
// 4. Active — pressed state feedback
// 5. Disabled — visually distinct + not interactive + explained
// 6. Loading — skeleton or spinner with status announcement
// 7. Error — error message + recovery action
// 8. Empty — helpful message + action to populate
// 9. Success — confirmation feedback
```

**Accessibility Built-In**:
```tsx
// Semantic HTML first
<nav aria-label="Main navigation">
<main id="main-content">
<section aria-labelledby="section-heading">

// ARIA only when HTML semantics are insufficient
<div role="alert" aria-live="polite">{errorMessage}</div>

// Keyboard navigation
onKeyDown={(e) => {
  if (e.key === 'Enter' || e.key === ' ') handleAction();
  if (e.key === 'Escape') handleClose();
}}

// Focus management
useEffect(() => { if (isOpen) dialogRef.current?.focus(); }, [isOpen]);

// Reduced motion
const prefersReducedMotion = useMediaQuery('(prefers-reduced-motion: reduce)');
```

**Responsive Implementation**:
```tsx
// Mobile-first responsive classes
<div className="
  grid grid-cols-1        // Mobile: single column
  md:grid-cols-2          // Tablet: two columns
  lg:grid-cols-3          // Desktop: three columns
  gap-4 md:gap-6 lg:gap-8  // Responsive spacing
">
```

---

### Step 4: CHANGE LOG — UX Reasoning for Every Change

After the code, provide a complete change log. Every change must cite a principle.

#### Change Log Format

For each change:

**Change [N]: [Descriptive Name]**
- **What changed**: [Specific description]
- **Before**: [How it was — with code snippet if relevant]
- **After**: [How it is now — with code snippet if relevant]
- **Principle**: [Specific UX law, heuristic, or WCAG criterion]
- **Why this matters**: [User behavior impact — not aesthetic preference]
- **Expected impact**: [Predicted improvement in metric or behavior]

Example:
> **Change 3: Reduced Action Bar from 8 to 3 Buttons**
> - **Before**: 8 buttons in a horizontal row: Save, Preview, Delete, Share, Export, Print, Archive, Duplicate
> - **After**: 3 primary buttons (Save, Preview, Share) + overflow menu for 5 secondary actions
> - **Principle**: Hick's Law — decision time increases logarithmically with number of choices
> - **Why this matters**: Users reported feeling overwhelmed by the action bar. 8 equally-weighted buttons creates decision paralysis.
> - **Expected impact**: Reduced time-to-action by ~40% (from 8 choices to 3). Secondary actions remain accessible but don't compete.

---

### Step 5: BEFORE/AFTER COMPARISON

Summarize the full transformation with a scoring comparison:

| Dimension | Before (1-10) | After (1-10) | Key Change | Principle |
|-----------|---------------|--------------|------------|-----------|
| Visual Hierarchy | [score] | [score] | [what changed] | [principle] |
| Cognitive Load | [score] | [score] | [what changed] | [principle] |
| Accessibility | [score] | [score] | [what changed] | [WCAG criterion] |
| State Coverage | [score] | [score] | [what changed] | [H1] |
| Error Handling | [score] | [score] | [what changed] | [H9] |
| Interaction Quality | [score] | [score] | [what changed] | [principle] |
| Consistency | [score] | [score] | [what changed] | [H4] |
| Mobile Readiness | [score] | [score] | [what changed] | [principle] |

**Overall score**: Before [X/10] -> After [Y/10]

---

### Step 6: VALIDATION PLAN

How to verify the redesign is actually better (not just different):

**Quick validation** (< 1 hour):
- [ ] Run the component in a browser and test all states
- [ ] Tab through with keyboard only — is everything reachable?
- [ ] Run axe DevTools or Lighthouse accessibility audit
- [ ] Test on mobile viewport (320px, 375px, 428px)
- [ ] Test with browser zoom at 200%

**User validation** (1-3 days):
- [ ] A/B test before vs. after with [N] users on [metric]
- [ ] 5-second test: show the redesign for 5 seconds, ask what the page is about
- [ ] Task completion test: give users a task, measure time-on-task and error rate
- [ ] Preference test: show before and after side-by-side, ask which feels easier

**Risk assessment**:
- What could go wrong with the redesign?
- What assumptions did we make that might be wrong?
- What edge cases weren't covered?
- Does the redesign work with the existing backend/API without changes?

---

## Output Format

```
### Phase Position
> **Phase 5: VALIDATE** | Step 24 of 30 | `/remix`
>
> `/23-roast` -> **`/remix`** -> `/25-qa`

---

## Remix: [Component/Screen Name]

### Input Analysis
- **Type**: [code / screenshot / specification]
- **Platform**: [React+Tailwind / SwiftUI / HTML+CSS / Vue / etc.]
- **Tech stack**: [What the code uses]
- **Design tokens**: [From .sumi/style.json: yes/no]
- **Primary user task**: [What the user does with this component/screen]

---

### Problem Identification (Top 5)

| # | Problem | Location | Severity | Principle Violated | User Impact |
|---|---------|----------|----------|--------------------|-------------|
| 1 | [problem] | [where] | [Critical/Major/Minor/Cosmetic] | [specific principle] | [behavioral consequence] |
| 2 | [problem] | [where] | [severity] | [principle] | [impact] |
| 3 | [problem] | [where] | [severity] | [principle] | [impact] |
| 4 | [problem] | [where] | [severity] | [principle] | [impact] |
| 5 | [problem] | [where] | [severity] | [principle] | [impact] |

---

### Proposed Fixes

#### Fix 1: [Name]
| Before | After |
|--------|-------|
| [description] | [description] |
**Principle**: [citation]
**Expected impact**: [metric prediction]

[Repeated for each fix]

---

### Redesigned Code

```[language]
// Complete, runnable, production-ready code
// Every change annotated with WHY (principle citation)
// All states handled
// Accessibility built-in
// Responsive behavior included
// Design tokens used if .sumi/style.json exists
```

---

### Change Log

#### Change 1: [Name]
- **Before**: [description]
- **After**: [description]
- **Principle**: [specific citation]
- **Expected impact**: [metric prediction]

[Repeated for each change]

---

### Before/After Score

| Dimension | Before | After | Change | Principle |
|-----------|--------|-------|--------|-----------|
| Visual Hierarchy | [X] | [Y] | [what] | [why] |
| Cognitive Load | [X] | [Y] | [what] | [why] |
| Accessibility | [X] | [Y] | [what] | [why] |
| State Coverage | [X] | [Y] | [what] | [why] |
| Error Handling | [X] | [Y] | [what] | [why] |
| Interaction Quality | [X] | [Y] | [what] | [why] |
| Consistency | [X] | [Y] | [what] | [why] |
| Mobile Readiness | [X] | [Y] | [what] | [why] |

**Overall**: [X/10] -> [Y/10]

---

### Validation Plan
**Quick checks**: [list]
**User testing**: [list]
**Risks**: [list]

---

### Design Memory Updated
Remix decisions logged to `.sumi/decisions.log`.

---

### Next Steps
1. **Test it** → Copy the code, run it, verify all states work
2. **Then** → `/25-qa` — Run full quality assurance on the redesigned component
3. **Or** → `/remix` again — Iterate on a different component
4. **Or** → `/23-roast` — Get a fresh critique of the redesign

**Run `/next` to continue the journey.**
```

---

## Quality Gates

The output MUST include:
- [ ] Exactly 5 problems identified with severity, principle, and user impact
- [ ] Every problem cites a specific, named UX principle (not "usability issue" or "bad design")
- [ ] Before/after description for every proposed fix
- [ ] Complete, runnable code output (not a diff, not pseudocode, not "add X here")
- [ ] Every code change annotated with a WHY comment citing the principle
- [ ] All UI states handled in code (default, hover, focus, active, disabled, loading, error, empty)
- [ ] Accessibility built into the code (semantic HTML, ARIA, keyboard nav, focus management)
- [ ] Responsive behavior in the code (mobile-first, breakpoint-aware)
- [ ] Design tokens from `.sumi/style.json` used if available (not arbitrary values)
- [ ] Change log with principle citation for every change
- [ ] Before/after scoring across 8 dimensions
- [ ] Validation plan with quick checks and user testing recommendations

The output MUST NOT include:
- Vague problem descriptions ("the design is cluttered") without specific principle citation
- Changes justified by personal preference rather than principles
- Incomplete code ("... rest of component" or "// add your styles here")
- Missing states (no loading state, no error state, no empty state)
- Accessibility bolted on as an afterthought (should be structural)
- New design tokens invented when `.sumi/style.json` exists
- Changes that contradict prior `.sumi/decisions.log` without explicit justification

---

## Cross-References

When remixing designs, draw principles and patterns from:
- `nng-ux-heuristics` skill — heuristic evaluation framework, all 10 heuristics with examples
- `cognitive-psychology-ux` skill — cognitive laws (Fitts's, Hick's, Miller's, Jakob's), perception laws (Von Restorff, Peak-End), Gestalt principles
- `component-patterns-code` skill — production-ready implementation patterns in React, SwiftUI, and CSS
- `interaction-motion-design` skill — animation improvements, micro-interactions, transition design, haptic feedback
- `accessibility-inclusive-design` skill — WCAG 2.2 compliance, ARIA patterns, keyboard navigation, screen reader support
- `ui-visual-design-system` skill — visual hierarchy, spacing systems, typography scale, color systems
- `performance-states-patterns` skill — loading, error, empty, skeleton, optimistic update patterns
- `micro-copy-intelligence` skill — button labels, error messages, empty state copy, tooltip text
- `form-design-encyclopedia` skill — form layout, input types, validation patterns, error recovery
- `color-palette-library` skill — accessible color combinations, APCA contrast scores
- `typography-pairing-recipes` skill — type scale, font pairings, fluid typography
- `animation-recipe-library` skill — production animation recipes for micro-interactions and transitions
- `design-token-presets` skill — ready-to-deploy token systems if no `.sumi/style.json` exists

---

## Next Step

**Next** -> `/25-qa` (5.4) — Run full quality assurance on the redesigned component

**Alternatives**:
- `/23-roast` (5.2) — Get a fresh critique of the redesign to find remaining issues
- `/19-ship` (4.3) — Rebuild specific components from scratch
- `/wireframe` — Go back to layout exploration if the fundamental structure is wrong
- `/guide` — See the full journey map
