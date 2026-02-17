---
name: Screen & Flow Patterns
description: "Comprehensive taxonomy of 25+ screen types, 15+ user flow patterns, and 25+ UI element deep-dives. Mobbin-style categorization with layout patterns, component hierarchies, state matrices, accessibility requirements, and best-in-class references for every screen, flow, and element type. Use when the user mentions: screen type, screen pattern, user flow, flow pattern, login screen, signup screen, checkout flow, onboarding flow, dashboard screen, search screen, product page, settings screen, empty state, error screen, screen builder, flow builder."
---

# Screen & Flow Patterns — The Complete Taxonomy

## Why Screen & Flow Patterns Matter

Every screen type in a digital product has established patterns that users have internalized through years of interaction with hundreds of apps and websites. When a login screen places the password field above the email field, or a checkout flow asks for shipping info after payment, users experience friction not because the interface is broken, but because it violates their learned expectations. These patterns are not arbitrary conventions — they are the result of decades of iterative refinement across billions of user interactions, A/B tests, and usability studies conducted by teams at companies like Apple, Google, Shopify, Stripe, and Airbnb.

Knowing the canonical patterns for each screen type is not about copying — it is about having a baseline of "what good looks like" so that every deviation is intentional and justified. A designer who knows that the standard checkout flow is 3-5 steps with a progress indicator, address before payment, and an order summary sidebar can make an informed decision to deviate (say, a single-page checkout for digital products). A designer who does not know the pattern is guessing. The difference between innovation and ignorance is whether you know the rule you are breaking.

This skill provides a complete taxonomy: 27 screen types with layout patterns and component hierarchies, 15 user flow patterns with step sequences and branching logic, and 26 UI element deep-dives with anatomy, states, and accessibility requirements. Each entry includes real-world reference implementations, common mistakes to avoid, and specific accessibility requirements. Use this as your pattern library when designing, auditing, or critiquing any digital product.

## Coverage

- **27 screen types** with layout patterns, component hierarchies, state matrices, and accessibility requirements
- **15 user flow patterns** with step sequences, decision points, error handling, emotional arcs, and metric benchmarks
- **26 UI element deep-dives** with anatomy, variants, states, platform differences, and ARIA requirements
- **Curated inspiration source guide** with lookup table for 20+ common design needs

## Reference Architecture

| File | Contents | Lines |
|------|----------|-------|
| `references/screen-type-catalog.md` | 27 screen types with UX patterns, layout specs, component lists, state matrices | 600-800+ |
| `references/user-flow-catalog.md` | 15 user flows with step sequences, branching, error handling, metrics | 500-700+ |
| `references/ui-element-deep-dive.md` | 26 UI elements with anatomy, variants, states, accessibility | 500-700+ |
| `references/inspiration-reference-guide.md` | Curated sources, lookup table, how to study references | 200-300 |

## Cross-References

- **component-patterns-code** — React, SwiftUI, and CSS implementations for elements described here
- **performance-states-patterns** — Loading, error, and empty state patterns referenced in screen states
- **mobile-ux-design** — iOS and Android platform conventions for mobile adaptations
- **desktop-app-design** — Desktop layout patterns for sidebar, split-view, and data-dense screens
- **cognitive-psychology-ux** — Cognitive load theory behind flow design and information hierarchy
- **accessibility-inclusive-design** — WCAG 2.2 compliance details for all screen and element patterns
- **interaction-motion-design** — Transition and animation patterns between screens and states

## Commands Powered by This Skill

| Command | Purpose |
|---------|---------|
| `/screen` | Generate a complete screen specification with layout, components, states, and accessibility |
| `/flow` | Generate a user flow with step sequences, branching, error handling, and metrics |
| `/inspo` | Get curated inspiration sources for a specific screen type, flow, or design problem |
