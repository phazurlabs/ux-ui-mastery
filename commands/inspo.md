---
description: Design inspiration and pattern finder — find best-practice patterns, references, and inspiration for any screen type, UI element, or user flow.
phase: "1"
phase_step: "1.2"
phase_name: "DISCOVER"
step_label: "Step 2 of 4"
---

# Inspo — Design Inspiration & Pattern Finder

Find the right design pattern, best-in-class reference, and actionable inspiration for any screen type, UI element, or user flow. Three modes, one command.

## Usage Modes

Invoke with a mode and type:
- `/inspo screen [type]` — Screen-level inspiration
- `/inspo element [type]` — Component/element-level inspiration
- `/inspo flow [type]` — Multi-screen flow inspiration

If no mode is specified, infer the most appropriate mode from context.

## Mode 1: Screen Inspiration

### Supported Screen Types
Login, Sign Up, Home/Dashboard, Profile, Settings, Search, Search Results, Detail/Product, List/Feed, Onboarding, Empty State, Error Page, Pricing, Checkout, Cart, Order Tracking, Chat/Messaging, Notification Center, Activity Feed, Calendar, Map, Media Player, Gallery/Grid, Analytics/Stats, Form (multi-step), Confirmation, Landing Page, About, Contact

### Screen Inspiration Protocol

1. **Identify the screen type** and gather context:
   - Product sector (fintech, social, e-commerce, etc.)
   - Platform (iOS, Android, Web, Desktop)
   - Key user task on this screen
   - Content density (minimal, moderate, dense)

2. **Describe the best patterns** for this screen type:
   - **Layout structure**: Optimal information architecture for this screen
   - **Key UI regions**: What goes where and why (header, content area, actions, navigation)
   - **Content hierarchy**: What users look at first, second, third (eye-tracking informed)
   - **Interaction model**: Primary actions, secondary actions, navigation patterns
   - **State coverage**: What states this screen must handle (loading, empty, error, populated, partial)

3. **Reference 5 best-in-class implementations**:
   - App name and platform
   - What makes their version of this screen exceptional
   - Specific pattern or decision to study
   - Screenshot search terms to find it on Mobbin/Screenlane

4. **Key principles for this screen type**:
   - 3-5 principles that specifically matter for this screen (not generic UX advice)
   - Common user expectations (Jakob's Law patterns)
   - Performance considerations specific to this screen type

5. **Common mistakes to avoid**:
   - 5 frequently seen anti-patterns for this screen type
   - Why each is a problem with user impact
   - What to do instead

6. **Inspiration source links**:
   - Mobbin search URL and filter combination
   - Screenlane category link
   - Refero search terms
   - Nicelydone applicable collection

## Mode 2: Element Inspiration

### Supported Element Types
Button, Card, Modal, Dialog, Bottom Sheet, Banner, Toast, Snackbar, Tab Bar, Navigation Bar, Sidebar, Search Bar, Input Field, Text Area, Toggle, Switch, Checkbox, Radio, Chip/Tag, Avatar, Badge, Tooltip, Popover, Dropdown, Select, Accordion, Carousel, Slider, List Item, Progress Indicator, Progress Bar, Stepper, Date Picker, Time Picker, Color Picker, Rating, Empty State, Skeleton, Breadcrumb, Pagination, Data Table, Menu, Context Menu, Command Palette, Floating Action Button, Segmented Control, Divider

### Element Inspiration Protocol

1. **Identify the element** and gather context:
   - Element type from the supported list
   - Platform context (iOS, Android, Web, Desktop)
   - Design system context (if working within an existing system)
   - Use case specifics (what content, what action, what context)

2. **Best-practice anatomy and variants**:
   - **Anatomy diagram** (text description): Every part of the element labeled
   - **Required variants**: Size variants, state variants, content variants
   - **Optional variants**: Contextual adaptations that may be needed
   - **Slot model**: What content is configurable (icon, label, description, action, badge)

3. **Platform-specific conventions**:

   | Aspect | iOS (HIG) | Android (M3) | Web |
   |--------|-----------|--------------|-----|
   | Size | [convention] | [convention] | [convention] |
   | Behavior | [convention] | [convention] | [convention] |
   | Animation | [convention] | [convention] | [convention] |
   | Position | [convention] | [convention] | [convention] |

4. **Accessibility requirements**:
   - Semantic role and ARIA attributes
   - Keyboard interaction pattern (which keys do what)
   - Screen reader announcement behavior
   - Minimum touch/click target size
   - Focus management rules
   - Color and contrast requirements

5. **5 outstanding implementations to reference**:
   - App or design system name
   - What makes their implementation excellent
   - Specific detail to borrow or study

## Mode 3: Flow Inspiration

### Supported Flow Types
Authentication (login/signup/password reset), Onboarding, Checkout, Payment, Booking/Reservation, Search & Filter, Content Creation (text/photo/video), Profile Editing, Settings Management, Subscription & Upgrade, Plan Selection, Social Sharing, Messaging (1:1 and group), File Upload, Data Import/Export, Collaboration Invite, Account Deletion, Cancellation, Refund/Return, Address Entry, Identity Verification (KYC), Two-Factor Setup, Permission Granting, Feedback/Review, Bug Reporting, Support/Help Request

### Flow Inspiration Protocol

1. **Identify the flow** and gather context:
   - Flow type from the supported list
   - Product sector and platform
   - User motivation (required vs. optional, urgent vs. casual)
   - Complexity level (simple, moderate, complex)

2. **Step-by-step flow pattern**:
   - Optimal number of steps with reasoning
   - Each step: purpose, content, interaction, and success criteria
   - Linear vs. branching logic with decision points mapped
   - Progress indication strategy (stepper, progress bar, step count, none)

3. **Decision points and branching**:
   - Where the flow can branch based on user input or system state
   - Conditional steps (shown only if relevant)
   - Early exit points and their consequences

4. **Error handling across the flow**:
   - Inline validation (when to validate, what to validate)
   - Step-level errors (what happens when a step fails)
   - Flow-level errors (network failure mid-flow, session timeout)
   - Recovery patterns (retry, save progress, start over)

5. **5 best reference implementations**:
   - App name and what makes their flow exceptional
   - Specific friction-reduction technique to study
   - Estimated completion rate or time-to-complete if known

6. **Anti-patterns for this flow**:
   - Common mistakes that kill completion rates
   - Dark patterns to avoid
   - Accessibility pitfalls specific to this flow type

## Output Format

```
### Phase Position
> **Phase 1: DISCOVER** | Step 2 of 4 | `/inspo`
> *NNG: Generative Research | Visual: Pattern Research*
>
> `/taste` (1.1) → **`/inspo` (1.2)** → `/benchmark` (1.3)

## Inspo: [Mode] — [Type]

### Context
- **Platform**: [iOS / Android / Web / Desktop]
- **Sector**: [if specified]
- **Key user task**: [primary goal]

### Pattern Analysis
[Detailed pattern description based on mode]

### Best-in-Class References
| # | App/System | Platform | Study This | Search Terms |
|---|------------|----------|------------|--------------|
[5 rows with actionable references]

### Key Principles
[3-5 principles specific to this type, not generic]

### Common Mistakes
[5 anti-patterns with explanations]

### Inspiration Sources
- **Mobbin**: [search URL or filter combination]
- **Screenlane**: [category or search terms]
- **Refero**: [search terms]
- **Nicelydone**: [collection name]

### Quick Implementation Notes
[Key technical considerations for building this pattern]
```

## Cross-References
When finding inspiration and patterns, draw knowledge from:
- `mobile-ux-design` skill for iOS 26 Liquid Glass patterns and Material 3 conventions
- `desktop-app-design` skill for desktop-specific patterns, density, and keyboard interaction
- `component-patterns-code` skill for production implementation patterns in React, SwiftUI, and CSS
- `interaction-motion-design` skill for animation patterns and platform-specific motion conventions
- `accessibility-inclusive-design` skill for accessible pattern requirements per WCAG 2.2
- `cognitive-psychology-ux` skill for cognitive principles behind effective patterns
- `design-critique-case-studies` skill for product deep-dives and pattern analysis

## Next Step

**Next** → `/benchmark` (1.3) — Score your references against the competition

**Alternatives**:
- `/ship` (4.3) — Jump to BUILD with the patterns you found
- `/screen` (4.2) — Build a screen using your reference patterns
- `/guide` — See the full 20-step journey
