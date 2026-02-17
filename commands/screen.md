---
description: Screen type builder — generate production-ready code for any standard screen type (25+) with all states, accessibility, responsive breakpoints, and design token consumption.
---

# Screen — Screen Type Builder

Generate a complete, production-ready screen for any standard screen type, including semantic HTML, component hierarchy, all states, responsive behavior, accessibility, and design token usage.

## Supported Screen Types

| Category | Screen Types |
|----------|-------------|
| Onboarding | Welcome, Get Started, Permissions, Tutorial, Value Prop |
| Auth | Login, Signup, Password Reset, MFA/2FA, Account Recovery |
| Core | Home, Dashboard, Feed, Search Results, Notifications |
| Profile | My Account, Edit Profile, Settings, Preferences, Privacy |
| Commerce | Product Listing (PLP), Product Detail (PDP), Cart, Checkout, Order Confirmation, Order Tracking |
| Content | Article/Detail, Media Viewer, Gallery, Comments, Editor |
| Social | Chat/Messaging, Activity Feed, User Profile (public), Contacts |
| Utility | Error (404/500), Empty State, Loading, Offline, Maintenance |

## Builder Protocol

1. **Accept inputs and resolve context**:
   - Required: screen type (e.g., "checkout," "login," "dashboard")
   - Optional: sector (e.g., fintech, healthcare, e-commerce, SaaS, media, education)
   - Optional: platform (web, iOS, Android — defaults to web/React)
   - Optional: design system (uses neutral tokens if not specified)
   - Resolve conventions: a fintech checkout differs from a food-delivery checkout in trust signals, data requirements, and regulatory constraints

2. **Research: "What makes a great [screen type]"**:
   - Identify 3 reference applications known for excellent implementations of this screen type
   - Extract 3-5 key design principles specific to this screen type
   - Note common pitfalls and anti-patterns for this screen type
   - Document the must-have elements (e.g., a checkout screen must have: order summary, trust signals, progress indicator, payment method selector, error recovery)

3. **Define the component hierarchy**:
   - Map the screen into a tree of components: page > sections > components > elements
   - For each component: name, purpose, data requirements, interactive behavior
   - Identify shared/reusable components vs. screen-specific components
   - Define the data flow: what props does each component receive, what events does it emit

4. **Generate the state matrix**:
   - Every screen must handle these states explicitly:

   | State | Description | What to Show |
   |-------|------------|-------------|
   | Empty | No data yet (first run, no results) | Illustration + explanation + CTA to populate |
   | Loading | Data is being fetched | Skeleton screens matching the populated layout |
   | Populated | Normal state with data | Full component rendering |
   | Error | Something went wrong | Contextual error with recovery action |
   | Partial | Some data loaded, some failed | Graceful degradation, load what you can |
   | Offline | No network connection | Cached data if available + offline indicator |
   | Updating | User action is processing | Optimistic UI or inline loading indicator |

5. **Build the semantic HTML structure**:
   - Use proper landmark regions: `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>`
   - Ensure heading hierarchy is logical and complete (h1 for page title, h2 for sections, h3 for subsections)
   - Use semantic elements: `<article>`, `<section>`, `<figure>`, `<time>`, `<address>`
   - Include ARIA attributes only where native semantics are insufficient
   - Add `role`, `aria-label`, `aria-live`, `aria-busy`, `aria-describedby` where needed

6. **Implement responsive layout**:
   - Mobile-first CSS using modern layout: CSS Grid for page structure, Flexbox for component internals
   - Define breakpoints: 375px (mobile), 768px (tablet), 1280px (desktop), 1920px (large desktop)
   - Use `clamp()` for fluid typography and spacing
   - Use container queries for reusable components that may appear in varying contexts
   - Include logical properties (`inline`, `block`) for RTL readiness

7. **Apply design tokens**:
   - Use semantic token names, not raw values: `--color-surface-primary`, not `#ffffff`
   - Token categories: color, typography, spacing, elevation, radius, motion, breakpoints
   - Show which tokens each component consumes
   - Include dark mode token mapping if applicable

8. **Add interaction and motion design**:
   - Define transitions for state changes (empty-to-populated, loading-to-error)
   - Respect `prefers-reduced-motion` for all animations
   - Include micro-interactions: button press feedback, input focus transitions, success confirmations
   - Define scroll behavior: sticky headers, infinite scroll or pagination, scroll restoration

9. **Generate the code**:
   - React + TypeScript for component logic
   - CSS Modules or styled approach for styling
   - Include TypeScript interfaces for all props and state
   - Add JSDoc comments explaining design decisions
   - Include unit test outline for critical interactions

## Output Format

```
## Screen Build: [Screen Type] — [Sector if specified]

### What Makes a Great [Screen Type]
**Reference Apps**: [App 1], [App 2], [App 3]
**Key Principles**:
1. [Principle with explanation]
2. [Principle with explanation]
3. [Principle with explanation]

**Common Pitfalls**: [What to avoid]

### Component Hierarchy
[Screen Name]
├── Header (sticky)
│   ├── BackButton
│   ├── PageTitle
│   └── ActionMenu
├── Main Content
│   ├── [Section Component]
│   │   ├── [Child Component]
│   │   └── [Child Component]
│   └── [Section Component]
└── Footer / Bottom Action Bar
    └── PrimaryCTA

### State Matrix
| State | Trigger | Visual Treatment | User Action Available |
|-------|---------|-----------------|---------------------|
| Empty | No data | [description] | [CTA] |
| Loading | Fetching | [description] | Wait / Cancel |
| ...   | ...     | ...             | ...                 |

### Code

#### TypeScript Interfaces
[Props, state, and data type definitions]

#### React Component
[Full component code with all states handled]

#### Styles
[CSS with responsive breakpoints, fluid type, dark mode, reduced motion]

#### Design Tokens Consumed
| Token | Usage | Value (Light) | Value (Dark) |
|-------|-------|--------------|-------------|
| --color-surface-primary | Page background | ... | ... |

### Accessibility Checklist
- [ ] Heading hierarchy: h1 → h2 → h3 (no skips)
- [ ] All interactive elements keyboard-accessible
- [ ] Focus management on state transitions
- [ ] ARIA live regions for dynamic content updates
- [ ] Color contrast ≥ 4.5:1 (text), ≥ 3:1 (UI components)
- [ ] Touch targets ≥ 44x44px on mobile
- [ ] Screen reader announcement for state changes

### Interaction Notes
[Scroll behavior, transitions, gestures, keyboard shortcuts]
```

## Cross-References
When building screens, draw patterns and best practices from:
- `component-patterns-code` skill for React/TypeScript component patterns, CSS modern layout, and accessible component implementations
- `performance-states-patterns` skill for skeleton screens, optimistic UI, error boundaries, loading strategies, and offline-first patterns
- `mobile-ux-design` skill for iOS 26 Liquid Glass components, safe area insets, and Material 3 adaptive patterns
- `desktop-app-design` skill for desktop-density layouts, keyboard navigation, and multi-panel architectures
- `ui-visual-design-system` skill for design token architecture, color systems, and typography scales
- `accessibility-inclusive-design` skill for ARIA patterns, focus management, and screen reader considerations

## Next Steps
After running `/screen`, consider:
- `/vibe-check` — Audit the generated screen against Nielsen's heuristics
- `/responsive` — Verify responsive behavior at all breakpoints
- `/include` — Deep accessibility audit on the generated code
- `/roast` — Full design critique with dimensional scoring
- `/flow` — Place the screen in a broader user flow for journey-level analysis
- `/copy-check` — Audit all text content in the generated screen
