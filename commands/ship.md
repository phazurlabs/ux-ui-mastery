---
description: Build a production-ready UI component with full state matrix, accessibility, design tokens, and platform code (React/SwiftUI/CSS). Copy-paste ready.
---

# Ship — Production Component Builder

Generate a production-ready UI component with complete state coverage, accessibility, design tokens, and platform-specific code.

## Build Protocol

1. **Gather context and constraints**: Before generating anything, understand the full picture.
   - Component name, purpose, and context of use
   - Platform: React/TypeScript, SwiftUI, CSS/HTML, or all three
   - Design system context (existing tokens, theme, brand)
   - **Sector**: What industry is this for? (fintech, healthcare, e-commerce, SaaS, etc.) — determines trust signals, density, and interaction conventions
   - **User sophistication**: Novice, intermediate, or expert — determines label verbosity, tooltip density, progressive disclosure level
   - **Interaction frequency**: Daily-use vs. occasional — daily-use components favor efficiency (keyboard shortcuts, density); occasional favors discoverability (labels, guidance)
   - **Cognitive context**: What is the user's mental state when encountering this component? (focused task, browsing, stressed/urgent, relaxed) — informs error tolerance and feedback intensity
   - **Prior Sumi outputs**: Check for `/taste` (style direction), `/inspo` (reference patterns), `/benchmark` (competitive gaps). If available, consume them. If not, use neutral defaults and note what's missing

2. **Generate the State Matrix**: Every component must account for all applicable states:

   | State | Description | Visual Treatment |
   |-------|-------------|-----------------|
   | Default | Resting state | Base styling |
   | Hover | Cursor over (pointer devices) | Subtle elevation or color shift |
   | Focus | Keyboard focus | Visible focus ring (2px+ offset) |
   | Active/Pressed | Being activated | Pressed/depressed feedback |
   | Disabled | Not interactive | Reduced opacity (0.38-0.5), no pointer events |
   | Loading | Awaiting response | Spinner or skeleton, aria-busy="true" |
   | Error | Validation failure | Error color, icon, message, aria-invalid="true" |
   | Success | Action completed | Success color, confirmation, aria-live announcement |
   | Skeleton | Content loading | Animated placeholder shapes |
   | Empty | No content available | Helpful message with action prompt |

3. **Apply design principles**: For every design decision, cite the specific law or heuristic that justifies it. No decision without a reason.

   | Decision Area | Principle | How to Apply |
   |---------------|-----------|-------------|
   | CTA size and padding | Fitts's Law | Larger targets for primary actions; minimum 44×44px touch, 48×48px recommended for frequent actions |
   | Number of options shown | Hick's Law | Limit visible choices to reduce decision time; group if >5 options; use progressive disclosure |
   | Visual hierarchy | Von Restorff Effect | The most important element must be visually distinct — size, color, or position isolation |
   | Element grouping | Gestalt Proximity | Related controls are close together; unrelated controls have clear spatial separation |
   | Labels and patterns | Jakob's Law | Use conventions users already know from similar products; match the user's existing mental model |
   | Error prevention | H5 + Cognitive Load Theory | Constrain inputs, use sensible defaults, confirm destructive actions — prevent errors rather than just reporting them |
   | Default values | H5 (Error Prevention) | Pre-fill with the most common/safest choice; reduce required decisions |
   | Feedback timing | Doherty Threshold (<400ms) | System response must feel instant; use optimistic UI or skeleton states for anything slower |

   If sector context is available (from `/taste` or user input), also apply `sector-style-intelligence` — e.g., fintech requires elevated trust signals (locks, badges, explicit security copy), healthcare requires high-contrast + simple language.

4. **Build with accessibility first**:
   - Semantic HTML elements (button, input, dialog, nav)
   - ARIA attributes where semantics are insufficient
   - Keyboard interaction pattern (Tab, Enter, Space, Escape, Arrow keys)
   - Focus management (trap for modals, restore on close)
   - Color contrast (4.5:1 text, 3:1 UI components)
   - Motion respect (`prefers-reduced-motion`)
   - Screen reader announcements for dynamic state changes

5. **Apply design tokens**:
   - Use semantic token names (--color-action-primary, not --blue-500)
   - Support light/dark mode via token switching
   - Respect density and size variants through token tiers
   - Follow W3C Design Tokens specification format

6. **Generate platform code**:
   - **React/TypeScript**: Functional component, typed props interface, forwardRef, compound patterns where applicable
   - **SwiftUI**: Native view with ViewModifier, environment integration, iOS 26 Liquid Glass when appropriate
   - **CSS**: Custom properties, container query responsive, logical properties for RTL

## Output Format

```
## Component: [Name]

### State Matrix
[Table of all applicable states with visual treatment]

### React/TypeScript Implementation
[Complete TSX with props interface, all states, ARIA, keyboard handling]

### SwiftUI Implementation (if requested)
[Complete SwiftUI view with modifiers and accessibility]

### CSS/HTML Implementation (if requested)
[Semantic HTML + modern CSS with custom properties]

### Accessibility Checklist
- [ ] Keyboard navigation works for all interactions
- [ ] Screen reader announces state changes
- [ ] Focus indicator visible (WCAG 2.4.7)
- [ ] Color contrast meets WCAG AA
- [ ] Motion respects prefers-reduced-motion
- [ ] Touch target >= 44x44pt (mobile)

### Test Skeleton
[Jest/Testing Library or XCTest structure for key interactions]

### Design Token Dependencies
[List of tokens the component consumes]

### Design Decision Rationale
| Decision | Choice Made | Principle | Why |
|----------|------------|-----------|-----|
| CTA size | 48×48px min | Fitts's Law | Primary action in high-frequency component needs generous target |
| Option display | Max 5 visible | Hick's Law | Reduces decision time for [context] |
| [...]    | [...]      | [...]     | [...] |

### Prior Output Integration
- **`/taste` consumed**: [Yes/No — if yes, list what was used: palette, type scale, motion personality]
- **`/inspo` consumed**: [Yes/No — if yes, list reference patterns applied]
- **`/benchmark` consumed**: [Yes/No — if yes, list competitive gaps addressed]
- **Missing context**: [List any Phase 1 outputs that would improve this component if run]
```

## Cross-References
When building components, draw implementation patterns from:
- `component-patterns-code` skill for platform-specific cookbook patterns
- `cognitive-psychology-ux` skill for Fitts's Law (target sizing), Hick's Law (option count)
- `accessibility-inclusive-design` skill for WCAG compliance
- `design-systems-architecture` skill for token architecture
- `interaction-motion-design` skill for animation and micro-interactions
- `performance-states-patterns` skill for loading, error, and empty states
- `sector-style-intelligence` skill for sector-specific conventions, trust signals, and density norms
- `nng-ux-heuristics` skill for heuristic grounding of design decisions

## Next Steps
After running `/ship`, consider:
- `/vibe-check` — Audit the component you just built
- `/include` — Deep accessibility check on the generated code
- `/roast` — Get a design critique of the component
- `/drip` — Generate the token system if you don't have one yet
