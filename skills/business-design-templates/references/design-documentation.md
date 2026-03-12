# Design Documentation — Specifications, Systems, and Standards

## Design Documentation Philosophy

Design documentation exists to reduce ambiguity between intent and implementation. Every pixel that a developer guesses at is a pixel that might be wrong. Every interaction behavior left unspecified becomes a developer's interpretation rather than a designer's decision. Documentation is not bureaucracy; it is the mechanism that ensures design quality survives the translation from Figma to production code.

The level of documentation should match the risk and complexity of the project. A startup prototype needs less documentation than an enterprise design system used by 50 developers. But even the leanest project benefits from explicit component specifications, interaction definitions, and design decision records.

### Documentation Principles

1. **Document decisions, not just outputs.** The "what" without the "why" creates a brittle system. When someone needs to modify a design decision later, understanding the original rationale prevents accidental regression.

2. **Machine-readable where possible.** Design tokens in JSON are more useful than design tokens in a PDF. Component APIs described in structured formats can be validated, tested, and consumed by tools.

3. **Living over static.** A Figma file with Dev Mode enabled is better than a PDF spec that was accurate on the day it was exported. A Storybook instance showing live components is better than a screenshot gallery. Prefer documentation formats that update when the source of truth changes.

4. **Layered detail.** Not everyone needs the same depth. Provide an overview for stakeholders, specifications for developers, and annotated rationale for future designers. Structure documentation so each audience can find their level without wading through content meant for others.

---

## 1. Design Spec Documentation Format

The design spec is the primary handoff document for individual screens, components, or features. It tells developers exactly what to build.

### Screen-Level Design Spec

```
DESIGN SPECIFICATION — [Screen Name]
═══════════════════════════════════════════════════════════════

Document Version: [X.X]
Last Updated: [YYYY-MM-DD]
Designer: [Name]
Figma Link: [URL to specific frame]
Status: [Draft | In Review | Approved | In Development | Shipped]

─────────────────────────────────────────────────────────────

1. SCREEN OVERVIEW
   Purpose: [What this screen does for the user in one sentence]
   Entry Points: [How the user arrives at this screen]
   Exit Points: [Where the user can go from this screen]
   User Story: As a [user type], I want to [action] so that [benefit]

2. LAYOUT SPECIFICATION
   Breakpoints:
   ┌────────────┬──────────┬────────────┬──────────────────────┐
   │ Breakpoint │ Width    │ Columns    │ Layout Changes       │
   ├────────────┼──────────┼────────────┼──────────────────────┤
   │ Mobile     │ 320-767  │ 4 col      │ [Description]        │
   │ Tablet     │ 768-1023 │ 8 col      │ [Description]        │
   │ Desktop    │ 1024-1439│ 12 col     │ [Description]        │
   │ Wide       │ 1440+    │ 12 col     │ [Max-width: 1440]    │
   └────────────┴──────────┴────────────┴──────────────────────┘

   Content Regions:
   ┌─────────────────────────────────────┐
   │ [Header / Navigation]               │ Fixed / Sticky
   ├─────────────────────────────────────┤
   │ [Hero / Page Title Region]          │ Padding: var(--space-8)
   ├───────────────────┬─────────────────┤
   │ [Main Content]    │ [Sidebar]       │ 8 col / 4 col
   │                   │                 │ Gap: var(--space-6)
   ├───────────────────┴─────────────────┤
   │ [Footer]                            │
   └─────────────────────────────────────┘

3. COMPONENT INVENTORY
   ┌──────────────────┬──────────────┬─────────────┬──────────┐
   │ Component        │ Variant      │ Props/State │ Notes    │
   ├──────────────────┼──────────────┼─────────────┼──────────┤
   │ PageHeader       │ with-breadcrumb│ title, breadcrumbs │  │
   │ SearchInput      │ with-filters │ query, filters, onSearch││
   │ ProductCard      │ grid-view    │ product, onAdd │       │
   │ Pagination       │ numbered     │ page, total, onChange │ │
   │ EmptyState       │ no-results   │ searchQuery │          │
   └──────────────────┴──────────────┴─────────────┴──────────┘

4. CONTENT SPECIFICATIONS
   ┌──────────────────┬────────────┬────────────┬─────────────┐
   │ Element          │ Content    │ Max Length  │ Truncation  │
   ├──────────────────┼────────────┼────────────┼─────────────┤
   │ Page title       │ Dynamic    │ 60 chars   │ None        │
   │ Product name     │ Dynamic    │ 80 chars   │ Ellipsis    │
   │ Description      │ Dynamic    │ 200 chars  │ "Read more" │
   │ Price            │ Dynamic    │ N/A        │ None        │
   │ CTA button       │ "Add to Cart"│ Fixed    │ None        │
   └──────────────────┴────────────┴────────────┴─────────────┘

5. STATE MATRIX
   ┌──────────────────┬──────────────────────────────────────┐
   │ State            │ Description                          │
   ├──────────────────┼──────────────────────────────────────┤
   │ Default          │ Standard view with content loaded     │
   │ Loading          │ Skeleton screens for card grid        │
   │ Empty            │ No results found — show empty state   │
   │ Error            │ API error — show retry option         │
   │ First-time       │ No previous searches — show suggestions│
   │ Filtered         │ Active filters shown with clear option│
   │ Paginated        │ Multiple pages — show pagination      │
   └──────────────────┴──────────────────────────────────────┘

6. INTERACTION NOTES
   [Numbered list of specific interaction behaviors not obvious
   from the static design]

   ① Search is debounced (300ms delay) — show loading indicator
     after 150ms if results have not returned
   ② Filter panel slides in from left on mobile (sheet pattern),
     is persistent sidebar on desktop
   ③ "Add to Cart" button shows success animation (checkmark,
     300ms) then reverts to default state
   ④ Scroll position is preserved when returning from product
     detail page (back navigation)

7. ACCESSIBILITY NOTES
   - Focus order: [Search] → [Filters] → [Sort] → [Product Grid]
     → [Pagination]
   - Product cards are announced as: "[Product Name], [Price],
     [Rating] stars. Button: Add to Cart"
   - Filter changes announce: "[X] results for [active filters]"
   - Pagination uses aria-label: "Page [X] of [Y]"
   - Search field has aria-label: "Search products"

8. RELATED SCREENS
   - Product Detail: [Figma link]
   - Cart: [Figma link]
   - Filter Panel (mobile): [Figma link]

═══════════════════════════════════════════════════════════════
```

---

## 2. Component Documentation Template

For documenting individual components in a design system or component library.

```
COMPONENT DOCUMENTATION — [Component Name]
═══════════════════════════════════════════════════════════════

Version: [X.X.X]
Last Updated: [YYYY-MM-DD]
Status: [Draft | Beta | Stable | Deprecated]
Designer: [Name]
Developer: [Name]
Figma: [URL]
Storybook: [URL]

─────────────────────────────────────────────────────────────

1. OVERVIEW
   Description: [One paragraph explaining what this component does,
   when to use it, and its role in the system]

   When to use:
   - [Use case 1]
   - [Use case 2]
   - [Use case 3]

   When NOT to use:
   - [Anti-pattern 1 — use [Alternative] instead]
   - [Anti-pattern 2 — use [Alternative] instead]

2. ANATOMY
   ┌─────────────────────────────────────┐
   │  ┌──┐ ┌──────────────┐ ┌────────┐  │
   │  │①│ │ ②            │ │  ③     │  │
   │  └──┘ └──────────────┘ └────────┘  │
   └─────────────────────────────────────┘

   ① [Element name] — [Description, required/optional]
   ② [Element name] — [Description, required/optional]
   ③ [Element name] — [Description, required/optional]

3. VARIANTS
   ┌──────────────┬─────────────────────────────────────────┐
   │ Variant      │ Description + Use Case                  │
   ├──────────────┼─────────────────────────────────────────┤
   │ Primary      │ Main action on the page. One per view.  │
   │ Secondary    │ Supporting actions. Multiple allowed.    │
   │ Ghost        │ Tertiary actions, navigation-like.      │
   │ Danger       │ Destructive actions (delete, remove).   │
   └──────────────┴─────────────────────────────────────────┘

4. SIZES
   ┌──────────────┬────────┬────────┬────────┬────────────────┐
   │ Size         │ Height │ Padding│ Font   │ Icon Size      │
   ├──────────────┼────────┼────────┼────────┼────────────────┤
   │ Small        │ 32px   │ 8/12   │ 14/20  │ 16px           │
   │ Medium       │ 40px   │ 8/16   │ 14/20  │ 20px           │
   │ Large        │ 48px   │ 12/20  │ 16/24  │ 20px           │
   └──────────────┴────────┴────────┴────────┴────────────────┘

5. STATES
   ┌──────────────┬─────────────┬────────────────────────────┐
   │ State        │ Visual      │ Behavior                   │
   ├──────────────┼─────────────┼────────────────────────────┤
   │ Default      │ [Description]│ Clickable                 │
   │ Hover        │ [Description]│ Cursor: pointer           │
   │ Active       │ [Description]│ Scale: 0.98               │
   │ Focus        │ [Description]│ Focus ring: 2px offset    │
   │ Disabled     │ [Description]│ Cursor: not-allowed       │
   │ Loading      │ [Description]│ Spinner replaces label    │
   └──────────────┴─────────────┴────────────────────────────┘

6. PROPERTIES / API
   ┌──────────────┬──────────┬──────────┬─────────┬──────────┐
   │ Property     │ Type     │ Default  │ Required│ Description│
   ├──────────────┼──────────┼──────────┼─────────┼──────────┤
   │ variant      │ enum     │ "primary"│ No      │ Visual style│
   │ size         │ enum     │ "medium" │ No      │ Size preset│
   │ label        │ string   │ —        │ Yes     │ Button text│
   │ icon         │ ReactNode│ —        │ No      │ Leading icon│
   │ iconPosition │ enum     │ "left"   │ No      │ Icon placement│
   │ disabled     │ boolean  │ false    │ No      │ Disabled state│
   │ loading      │ boolean  │ false    │ No      │ Loading state│
   │ fullWidth    │ boolean  │ false    │ No      │ Fill container│
   │ onClick      │ function │ —        │ No      │ Click handler│
   └──────────────┴──────────┴──────────┴─────────┴──────────┘

7. DESIGN TOKENS USED
   ┌────────────────────────────┬────────────────────────────┐
   │ Token                      │ Value (Light)              │
   ├────────────────────────────┼────────────────────────────┤
   │ button-primary-bg          │ color-action-primary       │
   │ button-primary-bg-hover    │ color-action-primary-hover │
   │ button-primary-text        │ color-text-on-action       │
   │ button-border-radius       │ radius-md (8px)            │
   │ button-focus-ring-color    │ color-focus-ring           │
   │ button-focus-ring-offset   │ 2px                        │
   └────────────────────────────┴────────────────────────────┘

8. ACCESSIBILITY
   - Role: button (native <button> element, not <div>)
   - Keyboard: Enter and Space activate the button
   - Focus: Visible focus ring on keyboard navigation
   - Disabled: aria-disabled="true" (not HTML disabled, to allow
     tooltip explaining why the button is disabled)
   - Loading: aria-busy="true", aria-label updated to include
     "loading" context
   - Icon-only: aria-label required (no visible label)
   - Color contrast: 4.5:1 minimum for text on all variants

9. USAGE EXAMPLES

   Do:
   - Use primary variant for the single most important action per view
   - Use consistent sizing within a button group
   - Include loading state for async operations
   - Pair with descriptive label text (verb + noun: "Save Changes")

   Don't:
   - Do not use multiple primary buttons in the same view
   - Do not use buttons for navigation (use links)
   - Do not disable without explanation (tooltip or helper text)
   - Do not use icon-only without aria-label

10. RELATED COMPONENTS
    - IconButton — for icon-only actions in toolbar contexts
    - LinkButton — for navigation that looks like a button
    - ButtonGroup — for grouping related actions
    - ToggleButton — for on/off state actions

═══════════════════════════════════════════════════════════════
```

---

## 3. Interaction Specification Format

For documenting how components and screens behave beyond static visuals.

```
INTERACTION SPECIFICATION — [Feature/Flow Name]
═══════════════════════════════════════════════════════════════

Version: [X.X]
Last Updated: [YYYY-MM-DD]
Designer: [Name]
Figma Prototype: [URL]

─────────────────────────────────────────────────────────────

1. INTERACTION OVERVIEW
   [Brief description of the interaction and its purpose]

2. TRIGGER AND RESPONSE TABLE
   ┌──────────────────┬────────────┬──────────────────────────┐
   │ Trigger          │ Condition  │ Response                 │
   ├──────────────────┼────────────┼──────────────────────────┤
   │ Click "Save"     │ Form valid │ Submit data, show toast  │
   │ Click "Save"     │ Form invalid│ Highlight errors, scroll│
   │ Click "Cancel"   │ No changes │ Navigate back            │
   │ Click "Cancel"   │ Unsaved changes│ Show discard dialog  │
   │ Press Escape     │ Modal open │ Close modal              │
   │ Press Escape     │ Dropdown open│ Close dropdown         │
   │ Scroll to bottom │ More data  │ Load next page           │
   │ Scroll to bottom │ No more data│ Show "end of list"     │
   │ Network error    │ Any submit │ Show error toast, retain │
   │                  │            │ form data                │
   │ Session timeout  │ Any action │ Show re-auth modal       │
   └──────────────────┴────────────┴──────────────────────────┘

3. ANIMATION SPECIFICATIONS
   ┌──────────────────┬────────────┬────────────┬─────────────┐
   │ Element          │ Property   │ Duration   │ Easing      │
   ├──────────────────┼────────────┼────────────┼─────────────┤
   │ Modal enter      │ opacity    │ 200ms      │ ease-out    │
   │                  │ transform  │ 200ms      │ ease-out    │
   │                  │ (scale)    │ 0.95→1.0   │             │
   │ Modal overlay    │ opacity    │ 200ms      │ ease-out    │
   │                  │            │ 0→0.5      │             │
   │ Modal exit       │ opacity    │ 150ms      │ ease-in     │
   │                  │ transform  │ 150ms      │ ease-in     │
   │                  │ (scale)    │ 1.0→0.95   │             │
   │ Toast enter      │ transform  │ 300ms      │ spring      │
   │                  │ (translateY)│ 100%→0    │ (0.5,1.5)   │
   │ Toast exit       │ opacity    │ 200ms      │ ease-in     │
   │ Skeleton shimmer │ transform  │ 1500ms     │ linear      │
   │                  │ (translateX)│ -100%→100%│ (infinite)  │
   └──────────────────┴────────────┴────────────┴─────────────┘

4. LOADING BEHAVIOR
   Initial page load:
   - Show skeleton screen matching the layout structure
   - Load above-the-fold content first
   - Progressive image loading (blur-up or LQIP)
   - Skeleton shimmer animation for 100ms minimum (avoid flash)

   Data refresh:
   - Maintain current content while fetching
   - Show subtle loading indicator (spinner in toolbar, not overlay)
   - Replace content with fade transition (150ms) when new data arrives

   Error recovery:
   - Show inline error message with retry button
   - Preserve user input (forms) and scroll position
   - Offer offline fallback if applicable

5. GESTURE SPECIFICATIONS (Mobile)
   ┌──────────────────┬────────────────────────────────────────┐
   │ Gesture          │ Behavior                               │
   ├──────────────────┼────────────────────────────────────────┤
   │ Swipe left       │ Reveal action buttons (delete, archive)│
   │ Swipe right      │ Mark as read / complete                │
   │ Long press       │ Enter selection mode                   │
   │ Pull down        │ Refresh content                        │
   │ Pinch            │ Zoom image gallery                     │
   │ Double tap       │ Like / favorite                        │
   └──────────────────┴────────────────────────────────────────┘

6. KEYBOARD SHORTCUTS
   ┌──────────────────┬────────────────────────────────────────┐
   │ Shortcut         │ Action                                 │
   ├──────────────────┼────────────────────────────────────────┤
   │ Cmd/Ctrl + S     │ Save current work                      │
   │ Cmd/Ctrl + Z     │ Undo last action                       │
   │ Cmd/Ctrl + K     │ Open command palette                   │
   │ Escape           │ Close current overlay / deselect       │
   │ Tab              │ Move focus to next element             │
   │ Shift + Tab      │ Move focus to previous element         │
   │ Enter            │ Activate focused element               │
   │ Arrow keys       │ Navigate within lists / grids          │
   └──────────────────┴────────────────────────────────────────┘

7. EDGE CASES
   ┌──────────────────┬────────────────────────────────────────┐
   │ Edge Case        │ Handling                               │
   ├──────────────────┼────────────────────────────────────────┤
   │ Very long text   │ Truncate with ellipsis at [X] chars    │
   │ Missing image    │ Show placeholder with icon             │
   │ Empty data       │ Show empty state with CTA              │
   │ Single result    │ Hide pagination, adjust grid           │
   │ 1000+ results    │ Virtualize list, show count in header  │
   │ Slow network     │ Show loading after 200ms delay         │
   │ No network       │ Show offline banner, cached data       │
   │ Concurrent edit  │ Show conflict resolution UI            │
   │ Session expired  │ Modal with re-auth, preserve state     │
   └──────────────────┴────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════
```

---

## 4. Design Decision Log (DDR — Design Decision Record)

### DDR Template

```
═══════════════════════════════════════════════════════════════
DESIGN DECISION RECORD

DDR-[NUMBER]: [DECISION TITLE]
═══════════════════════════════════════════════════════════════

Date: [YYYY-MM-DD]
Status: [Proposed | Accepted | Deprecated | Superseded by DDR-XX]
Deciders: [Names and roles]
Stakeholders Consulted: [Names and roles]

─────────────────────────────────────────────────────────────

CONTEXT

[Describe the situation, the problem, or the question that prompted
this decision. Include relevant background: user research findings,
technical constraints, business requirements, timeline pressures,
or other factors that shaped the decision space.]

[Reference specific data points: "Usability testing showed that 4 of
6 participants failed to complete the task using the current pattern
(see Research Report R-023)."]

─────────────────────────────────────────────────────────────

DECISION

[State the decision clearly and specifically. What was chosen?]

[Example: "We will implement a single-page checkout with progressive
disclosure rather than a multi-step wizard. All form fields will be
visible on the page with sections that expand/collapse, and the order
summary will remain persistently visible in a sidebar (desktop) or
sticky footer (mobile)."]

─────────────────────────────────────────────────────────────

ALTERNATIVES CONSIDERED

Alternative A: [Name]
Description: [What this option would look like]
Pros: [Advantages]
Cons: [Disadvantages]
Why rejected: [Specific reason — tie to evidence]

Alternative B: [Name]
Description: [What this option would look like]
Pros: [Advantages]
Cons: [Disadvantages]
Why rejected: [Specific reason — tie to evidence]

Alternative C: [Name]
Description: [What this option would look like]
Pros: [Advantages]
Cons: [Disadvantages]
Why rejected: [Specific reason — tie to evidence]

─────────────────────────────────────────────────────────────

RATIONALE

[Explain why the chosen option is the best fit given the constraints.
Reference design principles, research data, technical feasibility,
business priorities, or other decision criteria.]

[Example: "The single-page approach was chosen because: (1) usability
testing showed 40% faster completion times vs. the wizard, (2) the
persistent order summary addresses the #1 user complaint about hidden
costs, and (3) the technical team confirmed that progressive
disclosure can be implemented without additional API calls."]

─────────────────────────────────────────────────────────────

CONSEQUENCES

Positive:
- [Expected benefit 1]
- [Expected benefit 2]

Negative / Trade-offs:
- [Accepted trade-off 1]
- [Accepted trade-off 2]

Risks:
- [Risk 1] — Mitigation: [Plan]
- [Risk 2] — Mitigation: [Plan]

─────────────────────────────────────────────────────────────

VALIDATION PLAN

How will we know if this decision was correct?
- Metric: [What to measure]
- Target: [What success looks like]
- Timeline: [When to evaluate]
- Rollback plan: [What to do if the decision proves wrong]

─────────────────────────────────────────────────────────────

RELATED DECISIONS

- DDR-[XX]: [Related decision title]
- DDR-[YY]: [Related decision title]

═══════════════════════════════════════════════════════════════
```

### DDR Index Template

```
DESIGN DECISION LOG — [Project Name]
═══════════════════════════════════════════════════════════════

┌─────┬────────────┬──────────────────────────────┬──────────┐
│ DDR │ Date       │ Title                        │ Status   │
├─────┼────────────┼──────────────────────────────┼──────────┤
│ 001 │ 2026-01-15 │ Single-page checkout          │ Accepted │
│ 002 │ 2026-01-22 │ Guest checkout as default     │ Accepted │
│ 003 │ 2026-02-01 │ Mobile navigation pattern     │ Accepted │
│ 004 │ 2026-02-08 │ Color system token structure  │ Accepted │
│ 005 │ 2026-02-15 │ Error handling strategy       │ Proposed │
│ 006 │ 2026-03-01 │ Original sidebar nav          │ Superseded│
│     │            │                              │ by DDR-003│
└─────┴────────────┴──────────────────────────────┴──────────┘
═══════════════════════════════════════════════════════════════
```

---

## 5. Design System Documentation Structure

A comprehensive documentation structure for a design system.

```
DESIGN SYSTEM DOCUMENTATION — [System Name]
═══════════════════════════════════════════════════════════════

Site Structure:

/
├── Getting Started
│   ├── Introduction (what, why, who)
│   ├── Installation & Setup
│   ├── Quick Start Guide
│   └── FAQ
│
├── Foundations
│   ├── Design Principles
│   │   └── [X] principles with examples and counter-examples
│   ├── Color
│   │   ├── Color palette (primitive tokens)
│   │   ├── Semantic color (light, dark, high-contrast)
│   │   ├── Color usage guidelines
│   │   ├── Accessibility (contrast ratios)
│   │   └── Color in data visualization
│   ├── Typography
│   │   ├── Type scale
│   │   ├── Font families and weights
│   │   ├── Line height and letter spacing
│   │   ├── Responsive typography rules
│   │   └── Typography dos and don'ts
│   ├── Spacing
│   │   ├── Base unit and scale
│   │   ├── Component spacing
│   │   ├── Layout spacing
│   │   └── Responsive spacing rules
│   ├── Elevation
│   │   ├── Shadow system
│   │   ├── Layering model (z-index)
│   │   └── When to use elevation
│   ├── Motion
│   │   ├── Duration scale
│   │   ├── Easing curves
│   │   ├── Transition patterns
│   │   ├── Motion principles
│   │   └── Reduced motion support
│   ├── Grid & Layout
│   │   ├── Breakpoint definitions
│   │   ├── Column grid
│   │   ├── Container widths
│   │   └── Responsive patterns
│   └── Iconography
│       ├── Icon grid and sizing
│       ├── Icon style guidelines
│       ├── Icon library (searchable)
│       └── Contributing new icons
│
├── Components
│   ├── [Component Category]
│   │   └── [Component Name]
│   │       ├── Overview (description, when to use)
│   │       ├── Anatomy (labeled diagram)
│   │       ├── Variants (visual examples)
│   │       ├── States (all interactive states)
│   │       ├── Properties/API (props table)
│   │       ├── Accessibility (ARIA, keyboard)
│   │       ├── Usage guidelines (do/don't)
│   │       ├── Code examples
│   │       └── Related components
│   └── [Repeat for each component]
│
├── Patterns
│   ├── [Pattern Name]
│   │   ├── Overview (what problem this solves)
│   │   ├── Anatomy (composed components)
│   │   ├── Variants (different contexts)
│   │   ├── Behavior specification
│   │   ├── Responsive behavior
│   │   ├── Accessibility
│   │   ├── Usage examples
│   │   └── Related patterns
│   └── [Repeat for each pattern]
│
├── Content
│   ├── Voice and Tone
│   ├── Writing Guidelines
│   ├── UI Text Patterns (buttons, errors, empty states)
│   ├── Terminology Glossary
│   └── Localization Guidelines
│
├── Resources
│   ├── Figma Library (link + usage guide)
│   ├── Code Repository (link + setup guide)
│   ├── Storybook (link)
│   ├── Design Token Files (download)
│   ├── Presentation Templates
│   └── Brand Assets
│
└── Contributing
    ├── How to Propose a New Component
    ├── Component Design Checklist
    ├── Code Contribution Guidelines
    ├── Review Process
    ├── Versioning and Changelog
    └── Deprecation Policy

═══════════════════════════════════════════════════════════════
```

### Design Principles Documentation Template

```
DESIGN PRINCIPLES — [System Name]
═══════════════════════════════════════════════════════════════

PRINCIPLE 1: [Name — e.g., "Clarity Over Cleverness"]
──────────────────────────────────────────────────────

Statement:
[One sentence that captures the principle]
e.g., "When in doubt, choose the option that is most immediately
understandable, even if a more sophisticated approach exists."

Why This Matters:
[2-3 sentences explaining the rationale]

This Means:
- [Specific application 1 — e.g., "Use established UI patterns
  rather than novel interactions"]
- [Specific application 2 — e.g., "Label buttons with verbs that
  describe the action, not clever phrases"]
- [Specific application 3 — e.g., "Show content rather than hiding
  it behind hover or gesture interactions"]

This Does NOT Mean:
- [Common misinterpretation — e.g., "This does not mean designs
  should be boring. Delight is valuable when it does not come at
  the cost of comprehension."]

Example — Do:
[Specific example with visual or description]

Example — Don't:
[Counter-example with visual or description]

─────────────────────────────────────────────────────────────

[Repeat for each principle, typically 4-6 principles]

═══════════════════════════════════════════════════════════════
```

---

## 6. Brand Guidelines Template

```
BRAND GUIDELINES — [Brand Name]
═══════════════════════════════════════════════════════════════

Version: [X.X]
Last Updated: [YYYY-MM-DD]
Owner: [Brand Team / Design Lead]

─────────────────────────────────────────────────────────────

1. BRAND OVERVIEW
   Mission: [One sentence]
   Vision: [One sentence]
   Values: [3-5 core values with brief descriptions]
   Personality: [3-5 personality traits — e.g., "Confident but
   not arrogant. Warm but not casual. Expert but not elitist."]

2. LOGO
   Primary Logo:
   - Full color version [visual + download link]
   - Monochrome version [visual + download link]
   - Reversed version (for dark backgrounds) [visual + download link]

   Logo Variations:
   - Horizontal lockup [visual]
   - Stacked lockup [visual]
   - Icon only [visual]
   - Wordmark only [visual]

   Clear Space:
   - Minimum clear space: [X] times the height of the [element]
   - [Visual showing clear space measurement]

   Minimum Size:
   - Digital: [X]px width minimum
   - Print: [X]mm width minimum

   Logo Misuse:
   - Do not stretch or distort
   - Do not change colors
   - Do not add effects (shadows, outlines, gradients)
   - Do not place on busy backgrounds without contrast container
   - Do not rotate
   - [Visuals showing each misuse example]

3. COLOR
   Primary Palette:
   ┌────────────────┬─────────┬──────────────┬──────────────┐
   │ Name           │ Hex     │ RGB          │ Usage        │
   ├────────────────┼─────────┼──────────────┼──────────────┤
   │ [Primary]      │ #XXXXXX │ R, G, B      │ [When to use]│
   │ [Secondary]    │ #XXXXXX │ R, G, B      │ [When to use]│
   │ [Accent]       │ #XXXXXX │ R, G, B      │ [When to use]│
   └────────────────┴─────────┴──────────────┴──────────────┘

   Extended Palette:
   [Full color scale with 50-950 shades for each core color]

   Color Ratios:
   - Primary: [X]% of visual space
   - Secondary: [X]%
   - Accent: [X]% (highlights, CTAs only)
   - Neutral: [X]% (backgrounds, text, borders)

4. TYPOGRAPHY
   Primary Typeface: [Font Name]
   - Weights used: [List — e.g., Regular (400), Medium (500), Bold (700)]
   - License: [License type + link]
   - Fallback stack: [System font fallbacks]

   Secondary Typeface: [Font Name] (if applicable)
   - Usage: [When to use secondary vs. primary]

   Type Scale:
   ┌──────────────────┬──────┬────────┬────────┬─────────────┐
   │ Name             │ Size │ Weight │ Line H │ Usage        │
   ├──────────────────┼──────┼────────┼────────┼─────────────┤
   │ Display Large    │ 48px │ 700    │ 56px   │ Hero headings│
   │ Display Medium   │ 36px │ 700    │ 44px   │ Page titles  │
   │ Heading 1        │ 28px │ 600    │ 36px   │ Section heads│
   │ Heading 2        │ 24px │ 600    │ 32px   │ Sub-sections │
   │ Heading 3        │ 20px │ 600    │ 28px   │ Card titles  │
   │ Body Large       │ 18px │ 400    │ 28px   │ Lead text    │
   │ Body             │ 16px │ 400    │ 24px   │ Body text    │
   │ Body Small       │ 14px │ 400    │ 20px   │ Secondary    │
   │ Caption          │ 12px │ 400    │ 16px   │ Labels, meta │
   └──────────────────┴──────┴────────┴────────┴─────────────┘

5. IMAGERY
   Photography Style:
   - [Description of photographic style — lighting, subjects, mood]
   - [Examples of approved photography]
   - [Examples of photography that does not fit the brand]

   Illustration Style:
   - [Description of illustration approach]
   - [Style parameters: line weight, color palette, perspective]

   Iconography:
   - Style: [Outlined / Filled / Duotone]
   - Grid: [X]px × [X]px with [X]px padding
   - Stroke: [X]px
   - Corner radius: [X]px

6. VOICE AND TONE
   Brand Voice (Consistent):
   - [Trait 1]: [Description + example]
   - [Trait 2]: [Description + example]
   - [Trait 3]: [Description + example]

   Tone Variations (Context-Dependent):
   - Success moments: [More celebratory, encouraging]
   - Error moments: [Helpful, not blaming, solution-oriented]
   - Onboarding: [Welcoming, clear, not overwhelming]
   - Marketing: [More aspirational, benefit-focused]

   Writing Examples:
   ┌──────────────┬───────────────────┬───────────────────────┐
   │ Context      │ Do                │ Don't                 │
   ├──────────────┼───────────────────┼───────────────────────┤
   │ Button label │ "Save Changes"    │ "Submit" / "OK"       │
   │ Error msg    │ "Card declined.   │ "Error: Payment       │
   │              │ Try another card."│ processing failed."   │
   │ Empty state  │ "No projects yet. │ "Nothing to show."    │
   │              │ Create your first."│                      │
   └──────────────┴───────────────────┴───────────────────────┘

═══════════════════════════════════════════════════════════════
```

---

## 7. Content Style Guide Template

```
CONTENT STYLE GUIDE — [Product/Brand Name]
═══════════════════════════════════════════════════════════════

1. VOICE PRINCIPLES
   [3-5 principles governing all content]

2. UI TEXT PATTERNS

   Headings:
   - Page titles: Sentence case, descriptive ([noun] or [verb + noun])
   - Section heads: Sentence case, concise
   - Max length: [X] characters for page titles

   Buttons and CTAs:
   - Format: [Verb] + [Noun] (e.g., "Create Project", "Send Invite")
   - Sentence case (not Title Case, not ALL CAPS)
   - Max length: 3 words preferred, 5 words maximum

   Form Labels:
   - Sentence case
   - No colons
   - Paired with helper text for complex fields
   - Required fields: [Indicate with asterisk / "Required" label]

   Error Messages:
   - Structure: [What happened] + [How to fix it]
   - No technical jargon, no error codes visible to users
   - No blame language ("you forgot" / "invalid input")
   - Example: "Enter a valid email address, like name@example.com"

   Empty States:
   - Structure: [What this area is for] + [How to add content]
   - Include a CTA to take the first action
   - Friendly but not cutesy
   - Example: "No team members yet. Invite your first team member to
     start collaborating."

   Success Messages:
   - Brief confirmation of what happened
   - Next step if applicable
   - Example: "Project created. Share the link to invite collaborators."

   Loading States:
   - Only show text for loads exceeding 3 seconds
   - Be specific: "Loading your dashboard" not "Loading..."
   - For long processes: show progress or estimated time

3. TERMINOLOGY GLOSSARY
   ┌──────────────────┬─────────────────────────────────────────┐
   │ Term             │ Definition + Usage Notes                │
   ├──────────────────┼─────────────────────────────────────────┤
   │ [Term 1]         │ [Definition. Use when... Avoid...]     │
   │ [Term 2]         │ [Definition. Use when... Avoid...]     │
   │ [Term 3]         │ [Definition. Use when... Avoid...]     │
   └──────────────────┴─────────────────────────────────────────┘

4. FORMATTING CONVENTIONS
   - Dates: [Format — e.g., "Mar 12, 2026" not "03/12/2026"]
   - Times: [Format — e.g., "2:30 PM" or "14:30"]
   - Numbers: [Comma as thousands separator, period for decimals]
   - Currency: [Symbol before number, 2 decimal places]
   - Percentages: [X% with no space before %]
   - Lists: [Oxford comma / no Oxford comma]
   - Capitalization: [Sentence case for all UI text]

5. LOCALIZATION NOTES
   - [Design for text expansion: 30-50% for major languages]
   - [Avoid culturally specific metaphors or idioms]
   - [Date/time format must be locale-aware]
   - [Currency display must support multiple formats]
   - [RTL language support requirements]

═══════════════════════════════════════════════════════════════
```

---

## 8. Pattern Library Documentation Template

```
PATTERN DOCUMENTATION — [Pattern Name]
═══════════════════════════════════════════════════════════════

Category: [Navigation / Data Entry / Feedback / Layout / etc.]
Status: [Draft | Beta | Stable | Deprecated]
Last Updated: [YYYY-MM-DD]

─────────────────────────────────────────────────────────────

1. PROBLEM STATEMENT
   [What user problem does this pattern solve?]
   [In what context does this problem occur?]

2. SOLUTION
   [Brief description of the pattern and how it solves the problem]

3. WHEN TO USE
   - [Scenario 1]
   - [Scenario 2]
   - [Scenario 3]

4. WHEN NOT TO USE
   - [Scenario where an alternative pattern is better]
   - [Alternative: Use [Pattern X] instead when [condition]]

5. ANATOMY
   [Labeled diagram showing all elements of the pattern]

   Required elements:
   - [Element 1]: [Purpose]
   - [Element 2]: [Purpose]

   Optional elements:
   - [Element 3]: [When to include]
   - [Element 4]: [When to include]

6. BEHAVIOR
   [How the pattern responds to user interaction]

   Default flow:
   1. [Step 1]
   2. [Step 2]
   3. [Step 3]

   Error flow:
   1. [Step 1]
   2. [Step 2]

   Edge cases:
   - [Edge case 1]: [Handling]
   - [Edge case 2]: [Handling]

7. RESPONSIVE BEHAVIOR
   - Mobile: [How the pattern adapts]
   - Tablet: [How the pattern adapts]
   - Desktop: [Default presentation]

8. ACCESSIBILITY
   - [ARIA roles and properties]
   - [Keyboard interaction]
   - [Screen reader announcements]
   - [Focus management]

9. COMPONENTS USED
   - [Component 1]: [Role in this pattern]
   - [Component 2]: [Role in this pattern]
   - [Component 3]: [Role in this pattern]

10. EXAMPLES
    [Visual examples showing the pattern in different contexts]

    Example 1: [Context description]
    [Visual]

    Example 2: [Context description]
    [Visual]

11. RELATED PATTERNS
    - [Pattern A]: [How it relates]
    - [Pattern B]: [How it relates]

═══════════════════════════════════════════════════════════════
```
