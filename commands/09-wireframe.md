---
description: "[2.2] Low-fidelity wireframes — explore layout structure, content placement, and interaction flow before committing to visual design. Structure first, style later."
phase: "2"
phase_step: "2.2"
phase_name: "SHAPE"
step_label: "Step 9 of 30"
---

# Wireframe — Low-Fidelity Layout Engine

Generate low-fidelity wireframes that explore layout structure, content placement, and interaction flow before committing to visual design. This is the step vibe coders skip most — jumping straight to high-fidelity code and locking in the first layout that comes to mind. Structure first, style later.

## Analysis Protocol

### Step 0: Gather Context

Before wireframing, collect:

1. **Which screens to wireframe**: From `/08-map` sitemap, or the user specifies. Start with the 3-5 most critical screens (the ones users will use most).
2. **Screen purpose and primary user task**: What is the user trying to accomplish on each screen? One screen = one primary task.
3. **Content requirements**: What content must appear on each screen? From `/08-map` content hierarchy if available.
4. **Platform**: Web, iOS, Android, or cross-platform — affects layout patterns, viewport assumptions, and interaction conventions.
5. **Prior Sumi outputs**: Check for `/08-map` (information architecture, content hierarchy), `/02-brief` (product brief, personas, constraints), `/03-research` (user needs, mental models). Consume if available.

If the user has no prior Sumi outputs and no `/08-map`, ask what screens they need and what each screen's primary purpose is. Do not wireframe without understanding what the screen is for.

### Step 1: LAYOUT EXPLORATION

For each screen, generate 2-3 layout alternatives using ASCII/text-based wireframe format. These are structure-only — no colors, no fonts, no styling. Gray boxes and labels.

**ASCII wireframe conventions**:
- Use box-drawing characters for structure
- Use `[brackets]` for interactive elements (buttons, links, inputs)
- Use `CAPS` for headlines
- Use `x` or placeholder text for body copy
- Use `[---]` for images/media placeholders
- Use `( )` for radio buttons, `[ ]` for checkboxes
- Use `[v]` for dropdowns

**Example format**:
```
┌─────────────────────────────────────────┐
│ [Logo]         [Search...]      [Avatar]│
├─────────────────────────────────────────┤
│                                         │
│  PAGE TITLE                             │
│  Description text goes here             │
│                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐│
│  │ [---]    │ │ [---]    │ │ [---]    ││
│  │ Title    │ │ Title    │ │ Title    ││
│  │ Desc...  │ │ Desc...  │ │ Desc...  ││
│  │ [Action] │ │ [Action] │ │ [Action] ││
│  └──────────┘ └──────────┘ └──────────┘│
│                                         │
│  [Primary Action Button]                │
│                                         │
└─────────────────────────────────────────┘
```

**Each alternative must**:
- Explore a genuinely different layout approach (not minor variations)
- Examples of different approaches:
  - Sidebar navigation vs. top navigation
  - Card grid vs. list view vs. table
  - Single-column vs. multi-column
  - Content-first vs. action-first
  - Wizard/stepper vs. single long form
- Annotate: what this layout optimizes for, what it trades off

**Do NOT**:
- Create vague descriptions ("a card layout with some content") — draw the wireframe
- Make all alternatives look the same with minor shuffles
- Add visual design details (colors, specific fonts, shadows)

### Step 2: CONTENT PLACEMENT

For each layout alternative, map content priority to visual prominence:

**Above the fold** (visible without scrolling — approximately 600px on mobile, 800px on desktop):
- What is immediately visible?
- Is the primary task achievable without scrolling?
- Is there enough context for the user to orient themselves?

**Content priority mapping**:
- Most important content → most prominent position (top-left for LTR, largest element, highest contrast)
- Secondary content → supporting position
- Tertiary content → below the fold, in sidebar, or behind progressive disclosure

**CTA placement**:
- Primary CTA: prominent, thumb-reachable on mobile, above the fold
- Secondary CTAs: visually distinct from primary (not competing)
- Destructive actions: separated, requiring confirmation

**Whitespace zones**:
- Between major sections (creates visual grouping per Gestalt proximity)
- Around CTAs (isolation draws attention)
- Padding within cards/containers

### Step 3: INTERACTION NOTES

For each wireframe, document what happens when users interact:

**Click/tap behavior** — for every interactive element:
- Buttons: what action does this trigger? (navigate, submit, expand, delete)
- Cards: tap goes where? (detail page, modal, inline expand)
- Links: navigate to what? (same page section, new page, external)
- Form inputs: validation behavior, auto-complete, masks

**Navigation flow between screens**:
- "Clicking [X] navigates to [Screen Y]"
- "Back button returns to [Screen Z]"
- Use arrows to show flow: Screen A → Screen B → Screen C

**State changes** (what changes without navigating away):
- Accordions expanding/collapsing
- Tabs switching content
- Filters updating a list
- Toggle switches changing state
- Inline editing

**Progressive disclosure**:
- What starts hidden? What trigger reveals it?
- "Show more" / "See all" patterns
- Expandable sections
- Tooltips and popovers

**Error scenarios**:
- Where can things go wrong on this screen?
- Form validation errors: where do error messages appear?
- Empty states: what shows when there's no data?
- Loading: what shows while data loads?
- Failure: what shows when a request fails?

### Step 4: RESPONSIVE NOTES

Document how each layout adapts across breakpoints:

**Mobile (320-428px)**:
- What is the mobile layout? (This should be designed first, not an afterthought)
- Single-column unless there's a strong reason for multi-column
- Touch targets: minimum 44x44pt (iOS) / 48x48dp (Android)
- Bottom-reachable actions (thumb zone)

**Tablet (768-1024px)**:
- What changes from mobile? (Usually: 2-column where mobile was 1-column)
- Sidebar appears? Split view?

**Desktop (1024px+)**:
- What does the wider screen add? (Not just "stretched mobile")
- Multi-column layouts, sidebar navigation, richer data displays
- Maximum content width (typically 1200-1440px) with centered or left-aligned

**Responsive rules**:
- What stacks (multi-column → single-column)
- What hides (secondary content removed on mobile)
- What reorders (CTAs move to bottom on mobile for thumb reach)
- What transforms (table → card list on mobile, horizontal tabs → dropdown)

### Step 5: RECOMMEND

For each screen:

**Recommended layout**: Which alternative is strongest and why. Consider:
- Does it serve the primary user task efficiently?
- Does it follow platform conventions?
- Does it accommodate all required content without clutter?
- Does it work responsively without major restructuring?
- Does it scale (what happens with 3 items? 30? 300?)

**What to validate with users before proceeding**:
- Key layout assumptions that need testing
- Alternative approaches worth A/B testing
- Content priority assumptions to verify

**Key risks**:
- What could go wrong with this layout?
- Edge cases (long text, missing data, many items, no items)
- Accessibility concerns

## Output Format

```
### Phase Position
> **Phase 2: SHAPE** | Step 9 of 30 | `/09-wireframe`
>
> `/08-map` → **`/09-wireframe`** → `/10-vision`

---

## Low-Fidelity Wireframes

### Screen: [Name]
**Purpose**: [What this screen does]
**Primary task**: [What user is trying to accomplish]
**Content requirements**: [What must appear, from IA]

---

#### Layout A: [Approach name — e.g., "Sidebar + Content Grid"]

```
[ASCII wireframe]
```

**Optimizes for**: [What this layout prioritizes — e.g., "Quick scanning of many items"]
**Trades off**: [What it sacrifices — e.g., "Less space for item detail"]

---

#### Layout B: [Approach name — e.g., "Full-Width List View"]

```
[ASCII wireframe]
```

**Optimizes for**: [What this layout prioritizes]
**Trades off**: [What it sacrifices]

---

#### Layout C: [Approach name — e.g., "Dashboard with Panels"]

```
[ASCII wireframe]
```

**Optimizes for**: [What this layout prioritizes]
**Trades off**: [What it sacrifices]

---

#### Recommendation
**Use Layout [X]** because [specific reasons tied to user task, content requirements, and platform].

#### Interaction Notes
| Element | Action | Result |
|---------|--------|--------|
| [element] | [click/tap/hover] | [what happens] |

**State changes**: [what changes without navigation]
**Error scenarios**: [where things can go wrong, what shows]
**Empty state**: [what shows when there's no data]

#### Responsive Behavior
| Breakpoint | Adaptation |
|-----------|------------|
| Mobile (320-428px) | [what changes] |
| Tablet (768-1024px) | [what changes] |
| Desktop (1024px+) | [full layout as wireframed above] |

#### Assumptions to Test
1. [Assumption that needs user validation]
2. [Another assumption]
3. [Edge case to verify]

---

[Repeat for each screen]

---

### Next Steps
1. **First** → `/10-vision` — Set visual direction to apply to these wireframes
2. **Or** → `/11-anatomy` — Analyze which UI patterns fit these layouts
3. **Or** → `/22-test` — Plan usability testing on wireframes before building

**Run `/next` to continue the journey.**
```

## Quality Gates

The output MUST include:
- [ ] At least 2 layout alternatives per screen (3 preferred)
- [ ] ASCII wireframes with clear structure (drawn, not described)
- [ ] Content priority mapped for each layout (above/below fold, primary/secondary)
- [ ] Interaction notes for all interactive elements (what happens on click/tap)
- [ ] Responsive behavior noted for at least mobile and desktop breakpoints
- [ ] Clear recommendation with rationale tied to user task and platform
- [ ] Assumptions identified that need user testing before proceeding
- [ ] Error and empty states addressed for each screen

The output MUST NOT include:
- Vague descriptions instead of wireframes ("a grid of cards") — draw the wireframe
- Visual design details (colors, specific fonts, shadows, gradients)
- Only one layout option per screen (defeats the purpose of exploration)
- Wireframes without interaction notes (static pictures are not UX design)
- Missing responsive considerations (mobile is not an afterthought)

## Cross-References

When creating wireframes, draw knowledge from:
- `screen-flow-patterns` skill — screen types catalog (25+ screen types with canonical layout patterns)
- `ui-pattern-intelligence` skill — pattern recommendations for each screen type (navigation, data display, input, feedback)
- `cognitive-psychology-ux` skill — scanning patterns (F-pattern for text-heavy, Z-pattern for marketing, Gutenberg diagram for balanced), Gestalt grouping (proximity, similarity, closure), Fitts's Law (larger targets = faster acquisition)
- `component-patterns-code` skill — component patterns that will implement these wireframes (informs feasibility)
- `visual-design-mastery` skill — `composition-mastery.md` for grid systems, visual hierarchy, rule of thirds
- `mobile-ux-design` skill — mobile layout conventions, thumb zones, safe areas
- `desktop-app-design` skill — desktop layout conventions, window management, keyboard shortcuts
- `performance-states-patterns` skill — loading, error, and empty state patterns for each screen
- `accessibility-inclusive-design` skill — reading order, focus order, touch target sizes

## Next Step

**Next** → `/10-vision` (2.3) — Set visual direction to apply to these wireframe structures

**Alternatives**:
- `/11-anatomy` — Analyze which specific UI patterns and components fit these layouts
- `/flow` (2.4) — Map detailed user flows connecting these screens
- `/22-test` — Plan usability testing on wireframes before investing in visual design
- `/guide` — See the full journey map
