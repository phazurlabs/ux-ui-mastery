---
name: wireframe
description: "Generate low-fidelity ASCII wireframes with layout alternatives and interaction notes"
argument-hint: "[screen or flow to wireframe]"
---

# Wireframe — Low-Fidelity Layout Engine

## Before running

This command needs a screen or flow to wireframe.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate low-fidelity ASCII wireframes that explore layout structure, content placement, and interaction flow before committing to visual design. This is the step vibe coders skip most — jumping straight to high-fidelity code and locking in the first layout that comes to mind. Structure first, style later.

## Design Memory Integration

Before generating wireframes, check for `.sumi/` in the user's project root:

- **`.sumi/style.json`** — If present, inherit design tokens (spacing scale, border radii, grid system) to inform wireframe structure. Do not apply colors or typography — this is low-fidelity — but use the spacing rhythm and grid column count.
- **`.sumi/brief.json`** — If present, pull product description, target users, constraints, and platform from the brief. Skip re-asking these questions.
- **`.sumi/map.json`** — If present, pull sitemap, screen inventory, and content hierarchy. Use as the wireframe source-of-truth for what screens exist and what content each contains.
- **`.sumi/decisions.log`** — If present, read prior design decisions to maintain consistency across commands.

If `.sumi/` does not exist, create it after the user selects their preferred wireframe layout. Write:
```json
// .sumi/wireframe-[screen-name].json
{
  "screen": "screen-name",
  "selectedLayout": "A|B|C",
  "layoutApproach": "description of selected layout",
  "regions": ["header", "sidebar", "main", "footer"],
  "components": { "region": ["component-type"] },
  "responsive": { "mobile": "...", "tablet": "...", "desktop": "..." },
  "interactionMap": { "element": "action" },
  "states": ["default", "empty", "loading", "error"],
  "timestamp": "ISO-8601"
}
```

This ensures `/screen`, `/ship`, `/generate`, and `/remix` can read the wireframe decisions downstream.

---

## Analysis Protocol

### Step 0: Gather Context

Before wireframing, collect everything needed to make informed layout decisions:

1. **Which screens to wireframe**: From `.sumi/map.json` or `/08-map` output, or the user specifies directly. Start with the 3-5 most critical screens (the ones users will use most frequently or that have the highest business impact).

2. **Screen purpose and primary user task**: What is the user trying to accomplish on each screen? One screen = one primary task. If the screen tries to serve two equally important tasks, consider splitting it.

3. **Content requirements**: What content must appear on each screen? Pull from `.sumi/map.json` content hierarchy if available. Categorize content as:
   - **Must have** — screen fails without this content
   - **Should have** — expected by users but not critical
   - **Could have** — nice-to-have, candidate for progressive disclosure

4. **Platform**: Web, iOS, Android, or cross-platform — affects layout patterns, viewport assumptions, and interaction conventions. Pull from `.sumi/brief.json` if available.

5. **User mental models**: How do users expect this type of screen to work? What patterns do they already know from competitor products? Pull from `.sumi/brief.json` personas and `/03-research` if available.

6. **Entry and exit points**: How does the user arrive at this screen? Where do they go next? This determines what navigation and wayfinding the wireframe needs.

7. **Data volume expectations**: Will this screen show 3 items or 3,000? Data volume dramatically affects layout choice (cards vs. tables vs. lists vs. virtual scroll).

8. **Prior Sumi outputs**: Check for `/08-map` (information architecture, content hierarchy), `/02-brief` (product brief, personas, constraints), `/03-research` (user needs, mental models), `/04-taste` (visual reference, competitive landscape). Consume if available.

If the user has no prior Sumi outputs and no `/08-map`, ask:
- What screens do you need?
- What is each screen's primary purpose?
- What platform are you building for?
- What content must appear on each screen?

Do not wireframe without understanding what the screen is for.

---

### Step 1: LAYOUT EXPLORATION

For each screen, generate **2-3 genuinely different layout alternatives** using ASCII/text-based wireframe format. These are structure-only — no colors, no fonts, no styling. Gray boxes and labels.

#### ASCII Wireframe Conventions

Use these conventions consistently across all wireframes:

```
Structural elements:
  ┌─────┐  Box-drawing characters for containers
  │     │  Vertical lines for boundaries
  └─────┘  Corners for clean framing
  ├─────┤  Horizontal dividers within containers

Interactive elements:
  [Button Text]     Clickable buttons
  [Search...]       Input fields (with placeholder)
  [v Dropdown]      Select/dropdown menus
  ( ) Radio         Radio button (unselected)
  (x) Radio         Radio button (selected)
  [ ] Checkbox      Checkbox (unchecked)
  [x] Checkbox      Checkbox (checked)
  [< Back]          Navigation back
  [+ Add New]       Action with icon hint

Content placeholders:
  CAPS TEXT          Headlines / section titles
  Regular text       Body copy / descriptions
  xxx xxx xxx        Placeholder body text
  [---]              Image or media placeholder
  [/// IMG ///]      Larger image area
  [>> VIDEO <<]      Video placeholder
  ~~~~               Decorative divider
  ...                Truncated content

Status indicators:
  (i)                Info icon
  (!)                Warning icon
  (x)                Error icon
  (*)                Star/favorite
  (#)                Count badge
```

#### Layout Approach Catalog

Each alternative must explore a genuinely different structural approach. Do not produce minor variations of the same idea. Here are canonical approaches to consider:

**Navigation structure alternatives:**
- Top navigation bar (horizontal)
- Left sidebar navigation (vertical, persistent)
- Bottom tab bar (mobile-native)
- Hamburger/drawer (hidden navigation)
- Breadcrumb-only (deep hierarchy)
- Command palette (keyboard-first)

**Content layout alternatives:**
- Card grid (browseable, visual)
- List view (scannable, dense)
- Table view (comparable, sortable)
- Split pane (list + detail)
- Single-column feed (focused, scrollable)
- Dashboard panels (multi-metric overview)
- Magazine layout (editorial, mixed content sizes)
- Kanban columns (status-based)
- Timeline (chronological)
- Map + list hybrid (location-based)

**Form layout alternatives:**
- Single long form (simple, scrollable)
- Multi-step wizard (complex, guided)
- Accordion sections (progressive disclosure)
- Side-by-side comparison form
- Inline editing (edit-in-place)
- Modal/drawer form (contextual)

**Detail view alternatives:**
- Full-page detail (immersive)
- Side panel / drawer (contextual, non-navigating)
- Modal overlay (quick view)
- Expandable row (inline detail)
- Tab-organized detail (multi-section)

#### Example Wireframe: Dashboard (Layout A — Sidebar + Grid)

```
┌──────────────────────────────────────────────────────────┐
│  [Logo]              [Search...]           (!) [Avatar]  │
├────────┬─────────────────────────────────────────────────┤
│        │                                                 │
│  NAV   │  DASHBOARD                                      │
│        │  Welcome back, Sarah                            │
│  Home  │                                                 │
│  ----  │  ┌─────────────┐ ┌─────────────┐ ┌───────────┐ │
│  Tasks │  │ METRIC 1    │ │ METRIC 2    │ │ METRIC 3  │ │
│  Team  │  │ 2,456       │ │ $12.4K      │ │ 94%       │ │
│  Docs  │  │ +12% ↑      │ │ -3% ↓       │ │ +2% ↑     │ │
│  Stats │  └─────────────┘ └─────────────┘ └───────────┘ │
│        │                                                 │
│  ----  │  RECENT ACTIVITY                                │
│  Help  │  ┌─────────────────────────────────────────┐   │
│  Gear  │  │ [Avatar] Jane commented on Project X    │   │
│        │  │ 2 minutes ago                           │   │
│        │  ├─────────────────────────────────────────┤   │
│        │  │ [Avatar] Tom completed Task #142        │   │
│        │  │ 15 minutes ago                          │   │
│        │  ├─────────────────────────────────────────┤   │
│        │  │ [Avatar] You were assigned Review #89   │   │
│        │  │ 1 hour ago                              │   │
│        │  └─────────────────────────────────────────┘   │
│        │                                                 │
│        │  [View All Activity →]                          │
│        │                                                 │
└────────┴─────────────────────────────────────────────────┘
```

**Optimizes for**: Quick scanning of key metrics + persistent navigation access
**Trades off**: Less horizontal space for content on narrow screens

#### Example Wireframe: Dashboard (Layout B — Top Nav + Full-Width Panels)

```
┌──────────────────────────────────────────────────────────┐
│  [Logo]   Home  Tasks  Team  Docs  Stats    [? ] [Avtr] │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  DASHBOARD                              [+ New Task]     │
│  Welcome back, Sarah · Last login: 2h ago                │
│                                                          │
│  ┌──────────────────────────────────────────────────┐    │
│  │  2,456 tasks    $12.4K revenue    94% on-time    │    │
│  │  +12% ↑         -3% ↓             +2% ↑          │    │
│  └──────────────────────────────────────────────────┘    │
│                                                          │
│  ┌──────────────────────┐  ┌─────────────────────────┐   │
│  │ MY TASKS             │  │ TEAM UPDATES            │   │
│  │                      │  │                         │   │
│  │ [ ] Design review    │  │ Jane → commented        │   │
│  │ [ ] API integration  │  │ Tom → completed #142    │   │
│  │ [x] Write specs      │  │ You → assigned #89      │   │
│  │ [ ] User testing     │  │                         │   │
│  │                      │  │ [View All →]            │   │
│  │ [+ Add Task]         │  │                         │   │
│  └──────────────────────┘  └─────────────────────────┘   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

**Optimizes for**: Full content width, action-oriented layout with tasks prominent
**Trades off**: Navigation takes vertical space, fewer nav items visible at once

---

#### Annotation Requirements for Each Alternative

Every wireframe alternative must include these annotations:

**1. Rationale** (2-3 sentences):
- Why this structural approach was chosen
- What user behavior or need it optimizes for
- What design principle supports this choice

**2. Pros**:
- List 3-4 specific advantages
- Tie each to a user task, platform convention, or design principle
- Example: "Sidebar navigation stays visible during deep task flows (H7: Flexibility and Efficiency of Use)"

**3. Cons**:
- List 2-3 specific disadvantages
- Be honest about trade-offs — every layout trades something
- Example: "Sidebar consumes ~240px of horizontal space, reducing content area on screens < 1280px"

**4. Best suited when**:
- Describe the scenario where this layout wins
- "Best when users navigate frequently between sections"
- "Best when data density is high and comparison is needed"

---

### Step 2: CONTENT PLACEMENT & INFORMATION HIERARCHY

For each layout alternative, map content priority to visual prominence:

#### Above the Fold Analysis

**Above the fold** (visible without scrolling — approximately 600px on mobile, 800px on desktop):

- What is immediately visible?
- Is the primary task achievable without scrolling?
- Is there enough context for the user to orient themselves?
- Can the user answer "Where am I?" and "What can I do here?" within 3 seconds?

#### Information Hierarchy Levels

Annotate every element in the wireframe with its hierarchy level:

| Level | Treatment | Examples |
|-------|-----------|---------|
| **H1 — Primary** | Largest, most prominent, above the fold | Page title, primary metric, hero content |
| **H2 — Secondary** | Supporting the primary, still above fold | Subtitle, secondary metrics, key filters |
| **H3 — Tertiary** | Important but not first-glance | Data tables, list items, form fields |
| **H4 — Quaternary** | Available but not competing | Metadata, timestamps, secondary actions |
| **H5 — Hidden** | Behind progressive disclosure | Advanced settings, "show more", tooltips |

#### Content Priority Mapping

- Most important content → most prominent position (top-left for LTR layouts, largest element, highest visual weight)
- Secondary content → supporting position (below or adjacent to primary)
- Tertiary content → below the fold, in sidebar, or behind progressive disclosure
- Actions → proximity to the content they act upon

#### CTA Placement Rules

- **Primary CTA**: Prominent, thumb-reachable on mobile, above the fold, isolated with whitespace
- **Secondary CTAs**: Visually distinct from primary (outlined vs. filled, smaller, different color weight)
- **Destructive actions**: Separated from constructive actions, requiring confirmation, never primary styling
- **Contextual actions**: Near the content they affect (edit button near the item, not in a distant toolbar)

#### Whitespace Zones

- Between major sections → creates visual grouping per Gestalt proximity principle
- Around CTAs → isolation draws attention (Von Restorff Effect)
- Padding within cards/containers → breathing room for readability
- Vertical rhythm → consistent spacing creates scannable structure

---

### Step 3: INTERACTION NOTES

For each wireframe, document what happens when users interact. This transforms a static layout into a living interface specification.

#### Click/Tap Behavior Matrix

For **every** interactive element in the wireframe:

| Element | Trigger | Action | Target | Feedback |
|---------|---------|--------|--------|----------|
| [Logo] | Click | Navigate | Home/Dashboard | - |
| [Search...] | Focus | Expand | Search overlay | Input focus ring |
| [Avatar] | Click | Open | Profile dropdown | Dropdown animation |
| [Metric Card] | Click | Navigate | Detail drill-down | Card press state |
| [+ New Task] | Click | Open | Creation modal/form | Button loading state |
| List item | Click | Navigate | Item detail view | Row highlight |
| [View All] | Click | Navigate | Full list page | Link underline |

#### Navigation Flow

Document screen-to-screen transitions:

```
Screen A (Dashboard)
  │
  ├─ [Task item] ──→ Screen B (Task Detail)
  │                     │
  │                     ├─ [Edit] ──→ Screen C (Task Edit)
  │                     │               └─ [Save] ──→ Screen B (updated)
  │                     │
  │                     └─ [Back] ──→ Screen A (Dashboard)
  │
  ├─ [+ New Task] ──→ Screen D (Task Creation)
  │                     └─ [Create] ──→ Screen B (new task detail)
  │
  └─ [Nav: Team] ──→ Screen E (Team List)
```

#### State Changes (Without Navigation)

Document every in-place state change:

- **Accordion expand/collapse**: Click section header → content slides open/closed, chevron rotates
- **Tab switching**: Click tab → content panel swaps, active tab indicator moves
- **Filter application**: Select filter → list updates in place, count badge updates, "X active filters" appears
- **Toggle switches**: Click → immediate state change with animation, associated content updates
- **Inline editing**: Double-click text → converts to editable input, shows save/cancel buttons
- **Drag and drop**: Long press → item lifts, drop zones highlight, reorder animates
- **Sort**: Click column header → list reorders, sort indicator arrow appears

#### Progressive Disclosure

Document what starts hidden and what reveals it:

| Hidden Content | Trigger | Reveal Method |
|---------------|---------|---------------|
| Advanced filters | "More filters" link | Drawer slides in from right |
| Item description | "Show more" | Text expands inline, link changes to "Show less" |
| Bulk actions | Checkbox selection | Toolbar slides down from top |
| Keyboard shortcuts | `?` key | Modal overlay |
| Metadata | Hover on item | Tooltip appears after 300ms delay |

---

### Step 4: STATE VARIATIONS

Every screen exists in multiple states. Wireframe the critical states, not just the "happy path" populated state.

#### Required States

For each wireframe, document or sketch these states:

**1. Empty State** — No data yet
```
┌─────────────────────────────────┐
│                                 │
│         [/// IMG ///]           │
│                                 │
│      NO TASKS YET               │
│                                 │
│   Create your first task to     │
│   get started tracking work.    │
│                                 │
│      [+ Create First Task]      │
│                                 │
└─────────────────────────────────┘
```
Requirements:
- Explain what would normally appear here
- Provide a clear action to populate the screen
- Use illustration or icon to soften the emptiness
- Never show a blank white screen — that looks broken

**2. Loading State** — Data is being fetched
```
┌─────────────────────────────────┐
│                                 │
│  ┌─────────────────────────┐    │
│  │ ░░░░░░░░░░░░            │    │
│  │ ░░░░░░░░                │    │
│  └─────────────────────────┘    │
│  ┌─────────────────────────┐    │
│  │ ░░░░░░░░░░░░            │    │
│  │ ░░░░░░░░                │    │
│  └─────────────────────────┘    │
│  ┌─────────────────────────┐    │
│  │ ░░░░░░░░░░░░            │    │
│  │ ░░░░░░░░                │    │
│  └─────────────────────────┘    │
│                                 │
└─────────────────────────────────┘
```
Requirements:
- Skeleton screens that match the shape of the loaded content
- Not a full-page spinner — show the layout structure
- Content appears progressively (header first, then content)

**3. Error State** — Something went wrong
```
┌─────────────────────────────────┐
│                                 │
│     (!) SOMETHING WENT WRONG    │
│                                 │
│   We couldn't load your tasks.  │
│   This is usually temporary.    │
│                                 │
│   [Try Again]    [Contact Us]   │
│                                 │
└─────────────────────────────────┘
```
Requirements:
- Explain what happened in plain language (not error codes)
- Provide a recovery action (retry, go back, contact support)
- Maintain the page shell (navigation, header) so user isn't lost

**4. Populated State** — Normal usage with realistic data volume
- Show realistic amounts of data (not 3 items when users will have 300)
- Use realistic content (real names, plausible dates, authentic copy)
- Show mixed states within lists (some completed, some pending, some overdue)

**5. Edge Case States** (document which apply):
- **Overflow**: What happens with very long text, many items, or large numbers?
- **Minimal**: What if there's only 1 item?
- **Permission restricted**: What does the user see if they lack access?
- **Offline**: What is available without a network connection?
- **First-time use**: Is there an onboarding overlay or guided tour?

---

### Step 5: RESPONSIVE BEHAVIOR

Document how each layout adapts across breakpoints. This is not an afterthought — it determines whether the wireframe is viable.

#### Mobile (320-428px)

- What is the mobile layout? Design mobile first, not as a compressed desktop
- Single-column unless there's a strong reason for multi-column
- Touch targets: minimum 44x44pt (iOS) / 48x48dp (Android)
- Bottom-reachable actions (thumb zone — the bottom 40% of the screen is the comfort zone)
- Navigation: bottom tab bar or hamburger menu
- Tables transform to cards or stacked key-value pairs
- Horizontal scrolling only for intentional carousels, never for content overflow

**Mobile wireframe sketch** (provide for each alternative):
```
┌───────────────────┐
│ [≡]  Logo  [Bell] │
├───────────────────┤
│                   │
│ DASHBOARD         │
│ Welcome, Sarah    │
│                   │
│ ┌───────────────┐ │
│ │ 2,456 tasks   │ │
│ │ +12% ↑        │ │
│ └───────────────┘ │
│ ┌───────────────┐ │
│ │ $12.4K rev    │ │
│ │ -3% ↓         │ │
│ └───────────────┘ │
│                   │
│ RECENT ACTIVITY   │
│ ┌───────────────┐ │
│ │ Jane commented│ │
│ │ 2 min ago     │ │
│ └───────────────┘ │
│ ┌───────────────┐ │
│ │ Tom completed │ │
│ │ 15 min ago    │ │
│ └───────────────┘ │
│                   │
├───────────────────┤
│ [Home][Task][Team]│
└───────────────────┘
```

#### Tablet (768-1024px)

- What changes from mobile? Usually: 2-column where mobile was 1-column
- Sidebar can appear (collapsible) or split view activates
- Touch targets still apply (tablets are touch devices)
- May show navigation rail (narrow sidebar with icons only)

#### Desktop (1024px+)

- What does the wider screen add? Not just "stretched mobile"
- Multi-column layouts, persistent sidebar navigation, richer data displays
- Maximum content width (typically 1200-1440px) with centered or left-aligned
- Hover states become relevant (tooltips, previews, hover cards)
- Keyboard shortcuts become relevant
- Right-click context menus become possible

#### Responsive Transformation Rules

Document these for each wireframe:

| Element | Mobile | Tablet | Desktop |
|---------|--------|--------|---------|
| Navigation | Bottom tabs | Side rail | Full sidebar |
| Metrics | Stacked cards | 2-column grid | 3-column row |
| Activity list | Full-width cards | Full-width cards | Right panel |
| Data table | Card list | Compact table | Full table |
| Actions | Bottom sheet | Bottom sheet | Inline/toolbar |
| Search | Icon → overlay | Compact bar | Full search bar |
| Filters | Bottom sheet | Side drawer | Inline above content |

---

### Step 6: COMPONENT IDENTIFICATION

For each region in the selected wireframe, identify what component it becomes during implementation:

#### Component Map

```
┌──────────────────────────────────────────────────────┐
│  AppBar / TopNavigation                               │
│  Components: Logo, SearchInput, NotificationBell,     │
│              AvatarMenu                               │
├────────┬─────────────────────────────────────────────┤
│        │                                              │
│ SideNav│  PageHeader                                  │
│  - NavItem (x7)  Components: Title, Subtitle,        │
│  - NavDivider         ActionButton                    │
│  - NavItem (x2)                                       │
│        │  MetricCardGroup                             │
│        │  Components: MetricCard (x3)                 │
│        │    - MetricCard: value, label, trend         │
│        │                                              │
│        │  ActivityFeed                                │
│        │  Components: FeedItem (repeating)            │
│        │    - FeedItem: avatar, text, timestamp       │
│        │    - LoadMoreButton                          │
│        │                                              │
└────────┴─────────────────────────────────────────────┘
```

This component map is written to `.sumi/wireframe-[screen].json` and consumed by `/screen` and `/ship` to generate production code.

---

### Step 7: RECOMMEND

For each screen, provide a clear recommendation:

**Recommended layout**: Which alternative is strongest and why. Consider:
- Does it serve the primary user task efficiently?
- Does it follow platform conventions users already know (Jakob's Law)?
- Does it accommodate all required content without clutter?
- Does it work responsively without major restructuring?
- Does it scale? (What happens with 3 items? 30? 300? 3,000?)
- Is the information hierarchy correct? (Most important = most prominent)
- Does the interaction model feel natural for the platform?

**What to validate with users before proceeding**:
- Key layout assumptions that need testing
- Alternative approaches worth A/B testing
- Content priority assumptions to verify
- Navigation model assumptions

**Key risks**:
- What could go wrong with this layout?
- Edge cases (long text, missing data, many items, no items, slow network)
- Accessibility concerns (reading order matches visual order, focus management)
- Performance concerns (rendering 1,000 items, large images)

---

## Output Format

```
### Phase Position
> **Phase 2: SHAPE** | Step 9 of 30 | `/wireframe`
>
> `/08-map` -> **`/wireframe`** -> `/10-vision`

---

## Low-Fidelity Wireframes

### Screen: [Name]
**Purpose**: [What this screen does — one sentence]
**Primary task**: [What user is trying to accomplish]
**Content requirements**: [What must appear, from IA or user input]
**Entry points**: [How users arrive at this screen]
**Exit points**: [Where users go from this screen]
**Data volume**: [Expected number of items, records, or content density]

---

#### Layout A: [Approach name — e.g., "Sidebar + Content Grid"]

```
[ASCII wireframe — desktop view]
```

**Rationale**: [Why this approach — 2-3 sentences]
**Optimizes for**: [What this layout prioritizes]
**Trades off**: [What it sacrifices]

**Pros**:
- [Specific advantage + principle reference]
- [Specific advantage + principle reference]
- [Specific advantage + principle reference]

**Cons**:
- [Specific disadvantage + impact]
- [Specific disadvantage + impact]

**Best suited when**: [Scenario where this layout wins]

**Information Hierarchy**:
| Element | Level | Position | Justification |
|---------|-------|----------|---------------|
| [element] | H1 | [position] | [why] |
| [element] | H2 | [position] | [why] |

---

#### Layout B: [Approach name — e.g., "Full-Width Card Feed"]

```
[ASCII wireframe — desktop view]
```

[Same annotation structure as Layout A]

---

#### Layout C: [Approach name — e.g., "Split Panel Detail View"]

```
[ASCII wireframe — desktop view]
```

[Same annotation structure as Layout A]

---

#### Recommendation
**Use Layout [X]** because [specific reasons tied to user task, content requirements, platform, and scale].

---

#### Interaction Map

| Element | Trigger | Action | Target | Feedback |
|---------|---------|--------|--------|----------|
| [element] | [click/tap/hover] | [navigate/open/toggle] | [destination] | [visual feedback] |

**State changes**: [What changes without navigation]
**Progressive disclosure**: [What starts hidden, what reveals it]
**Navigation flow**: [Screen-to-screen transitions]

---

#### State Variations

**Empty state**:
```
[ASCII wireframe of empty state]
```
[What the empty state communicates and what action it offers]

**Loading state**:
```
[ASCII wireframe showing skeleton]
```
[Skeleton strategy — which elements get placeholders]

**Error state**:
```
[ASCII wireframe of error state]
```
[Error message strategy, recovery actions]

**Edge cases**: [Overflow, minimal data, permission restricted, offline]

---

#### Responsive Behavior

**Mobile (320-428px)**:
```
[ASCII wireframe — mobile view]
```

**Transformation rules**:
| Element | Mobile | Tablet | Desktop |
|---------|--------|--------|---------|
| [element] | [treatment] | [treatment] | [treatment] |

---

#### Component Map

| Region | Component | Props/Children |
|--------|-----------|----------------|
| [region] | [ComponentName] | [key props] |

---

#### Assumptions to Test
1. [Assumption that needs user validation]
2. [Another assumption]
3. [Edge case to verify]

#### Risks
1. [Risk + mitigation]
2. [Risk + mitigation]

---

[Repeat for each screen]

---

### Design Memory Written
Wireframe decisions saved to `.sumi/wireframe-[screen].json`.
Available to downstream commands: `/screen`, `/ship`, `/generate`, `/remix`.

---

### Next Steps
1. **Select a layout** → Tell me which layout (A, B, or C) for each screen
2. **Then** → `/screen` — Build the selected wireframe into a full screen specification with real components
3. **Or** → `/10-vision` — Set visual direction before building
4. **Or** → `/22-test` — Plan usability testing on wireframes before investing in code

**Run `/next` to continue the journey.**
```

---

## Quality Gates

The output MUST include:
- [ ] At least 2 layout alternatives per screen (3 preferred), each structurally distinct
- [ ] ASCII wireframes drawn with box-drawing characters (not described in prose)
- [ ] Rationale, pros, and cons for each alternative with principle references
- [ ] Information hierarchy annotation (H1-H5 levels mapped to elements)
- [ ] Content priority mapped for each layout (above/below fold, primary/secondary)
- [ ] Complete interaction map for all interactive elements (trigger, action, target, feedback)
- [ ] Navigation flow diagram showing screen-to-screen transitions
- [ ] Progressive disclosure documented (what's hidden, what reveals it)
- [ ] State variations: empty, loading, error, populated (wireframed, not just listed)
- [ ] Responsive behavior with mobile wireframe sketch and transformation rules
- [ ] Component identification for each wireframe region
- [ ] Clear recommendation with rationale tied to user task, platform, and scale
- [ ] Assumptions and risks identified for validation
- [ ] Design memory written to `.sumi/wireframe-[screen].json`

The output MUST NOT include:
- Vague descriptions instead of wireframes ("a grid of cards") — draw the wireframe
- Visual design details (colors, specific fonts, shadows, gradients, border colors)
- Only one layout option per screen (defeats the purpose of exploration)
- Wireframes without interaction notes (static pictures are not UX design)
- Missing responsive considerations (mobile is not an afterthought)
- All alternatives looking the same with minor element shuffles
- Empty/loading/error states ignored or hand-waved
- Components described but not mapped to wireframe regions

---

## Cross-References

When creating wireframes, draw knowledge from:
- `screen-flow-patterns` skill — 25+ screen type catalog with canonical layout patterns for each
- `ui-pattern-intelligence` skill — 200+ UI patterns, navigation/data display/input/feedback recommendations per screen type
- `layout-block-intelligence` skill — 500+ layout section/block patterns (hero, features, pricing, CTA, dashboard blocks)
- `page-composition-engine` skill — 100+ full-page composition recipes with block stacking order and visual rhythm
- `cognitive-psychology-ux` skill — scanning patterns (F-pattern for text-heavy, Z-pattern for marketing, Gutenberg diagram), Gestalt grouping (proximity, similarity, closure), Fitts's Law (target size and distance)
- `component-patterns-code` skill — component patterns that will implement these wireframes (feasibility check)
- `visual-design-mastery` skill — `composition-mastery.md` for grid systems, visual hierarchy, rule of thirds
- `responsive-block-patterns` skill — cross-breakpoint transformation catalog, container queries, fluid scaling
- `mobile-ux-design` skill — mobile layout conventions, thumb zones, safe areas, iOS/Android specifics
- `desktop-app-design` skill — desktop layout conventions, window management, keyboard shortcuts
- `performance-states-patterns` skill — loading, error, and empty state patterns for each screen
- `accessibility-inclusive-design` skill — reading order, focus order, touch target sizes, WCAG requirements
- `navigation-pattern-encyclopedia` skill — every nav pattern with selection guidance
- `form-design-encyclopedia` skill — form layout patterns, input types, validation strategies
- `data-visualization-mastery` skill — chart and data table patterns for data-heavy screens

---

## Next Step

**Next** -> `/10-vision` (2.3) — Set visual direction to apply to these wireframe structures

**Alternatives**:
- `/screen` (4.2) — Build selected wireframe into full screen specification with components
- `/11-anatomy` — Analyze which specific UI patterns and components fit these layouts
- `/15-flow` (3.4) — Map detailed user flows connecting these screens
- `/22-test` (5.1) — Plan usability testing on wireframes before investing in visual design
- `/guide` — See the full journey map
