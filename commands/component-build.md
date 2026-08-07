---
name: component-build
description: Build a production-ready UI component with full state matrix, accessibility, design tokens, and platform code (React/SwiftUI/CSS).
argument-hint: "[component name and requirements]"
---

# Component Build Command

## Before running

This command needs which component to build, the platform (React/SwiftUI/CSS), and any states it needs.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target, do not audit a hypothetical interface, and do not produce generic advice in place of the real analysis — an audit of something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.

Generate a production-ready UI component with complete state coverage, accessibility, design tokens, and platform-specific code.

## Build Protocol

1. **Identify the component**: Determine the component type and platform target.
   - Component name, purpose, and context of use
   - Platform: React/TypeScript, SwiftUI, CSS/HTML, or all three
   - Design system context (existing tokens, theme, brand)

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

3. **Build with accessibility first**:
   - Semantic HTML elements (button, input, dialog, nav)
   - ARIA attributes where semantics are insufficient
   - Keyboard interaction pattern (Tab, Enter, Space, Escape, Arrow keys)
   - Focus management (trap for modals, restore on close)
   - Color contrast (4.5:1 text, 3:1 UI components)
   - Motion respect (`prefers-reduced-motion`)
   - Screen reader announcements for dynamic state changes

4. **Apply design tokens**:
   - Use semantic token names (--color-action-primary, not --blue-500)
   - Support light/dark mode via token switching
   - Respect density and size variants through token tiers
   - Follow W3C Design Tokens specification format

5. **Generate platform code**:
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
```

## Cross-References
When building components, draw implementation patterns from:
- `component-patterns-code` skill for platform-specific cookbook patterns
- `cognitive-psychology-ux` skill for Fitts's Law (target sizing), Hick's Law (option count)
- `accessibility-inclusive-design` skill for WCAG compliance
- `design-systems-architecture` skill for token architecture
- `interaction-motion-design` skill for animation and micro-interactions
- `performance-states-patterns` skill for loading, error, and empty states
