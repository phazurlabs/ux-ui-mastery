---
description: Cross-device responsive audit — evaluate design at every breakpoint for layout, touch targets, typography, reflow, and input mode adaptation.
---

# Responsive — Cross-Device Responsive Audit

Audit a design or component for responsive behavior across all breakpoints, input modes, and orientations, ensuring a coherent experience from 320px mobile to 2560px ultrawide.

## Responsive Audit Protocol

1. **Evaluate at each breakpoint tier**:

   | Tier | Range | Canonical Widths | Typical Devices |
   |------|-------|-----------------|-----------------|
   | Small Mobile | 320-375px | 320px, 375px | iPhone SE, older Androids |
   | Mobile | 376-428px | 390px, 393px, 428px | iPhone 15, Pixel 8, Galaxy S24 |
   | Large Mobile / Small Tablet | 429-767px | 430px, 744px | iPhone Pro Max, iPad Mini |
   | Tablet | 768-1024px | 768px, 820px, 1024px | iPad, iPad Air, Surface Go |
   | Small Desktop | 1025-1279px | 1280px | Laptops, small monitors |
   | Desktop | 1280-1920px | 1440px, 1920px | Standard monitors |
   | Ultrawide | 2560px+ | 2560px, 3440px | Ultrawide monitors, 4K displays |

2. **Check touch target compliance per breakpoint**:
   - Mobile/Tablet: minimum 44x44px touch targets (WCAG 2.5.8 Level AA, Apple HIG)
   - Desktop with pointer: 24x24px minimum with hover affordance
   - Verify spacing between adjacent targets: minimum 8px gap to prevent mis-taps
   - Check that touch targets do not overlap or crowd near screen edges
   - Verify that clickable areas match visual boundaries (no phantom touch zones)

3. **Assess content priority and reflow strategy**:
   - Verify content priority order: does the most important content appear first on mobile?
   - Check reflow behavior: single-column mobile to multi-column desktop without content loss
   - Flag horizontal scrolling at any breakpoint (WCAG 1.4.10 failure)
   - Verify that no content is hidden-only on mobile (progressive disclosure is fine; removal is not)
   - Check image/media behavior: art direction with `<picture>`, responsive images with `srcset`, aspect ratio handling
   - Verify tables reflow appropriately (stacked cards, horizontal scroll container, or responsive table pattern)

4. **Evaluate navigation pattern adaptation**:
   - Mobile: bottom tab bar (5 items max) or hamburger menu with clear affordance
   - Tablet: sidebar navigation or expanded bottom bar
   - Desktop: top navigation bar, optional side navigation for complex apps
   - Verify navigation is consistent in information architecture across breakpoints (same items, same hierarchy)
   - Check that the active/current state is clear at every breakpoint
   - Verify that deep-linked pages have clear wayfinding at all sizes

5. **Check typography scale and fluid type**:
   - Verify fluid typography using `clamp()`: e.g., `clamp(1rem, 0.5rem + 1.5vw, 1.25rem)`
   - Check minimum body text size: 16px on mobile (prevents iOS zoom), 14px minimum on desktop
   - Verify line length: 45-75 characters per line (measure) at every breakpoint
   - Check heading scale ratio adjusts: tighter ratio on mobile (1.2), wider on desktop (1.25-1.333)
   - Verify vertical rhythm is maintained across breakpoints

6. **Assess container queries vs. media queries**:
   - Identify components that should use container queries (reusable components in varying contexts)
   - Verify media queries handle page-level layout changes
   - Check for `container-type: inline-size` on appropriate wrapper elements
   - Flag components that break when placed in narrow containers (sidebar, modal, card)

7. **Evaluate input mode adaptation**:
   - **Touch**: Large targets, swipe gestures documented, no hover-dependent interactions
   - **Pointer (mouse)**: Hover states, precise click targets, right-click context menus where appropriate
   - **Keyboard**: Full operability without mouse, visible focus indicators at all sizes, logical tab order
   - **Hybrid** (touch laptop): Both touch and pointer patterns work, no conflicts
   - Check `@media (pointer: coarse)` and `@media (hover: none)` usage for adaptive styling

8. **Check orientation handling**:
   - Verify layout works in both portrait and landscape on mobile and tablet
   - Check that no critical content or actions are cut off in landscape mode
   - Verify orientation lock is not forced unless absolutely necessary (WCAG 1.3.4)
   - Test split-view and slide-over modes on iPad

9. **Score the responsive implementation** (each 1-10):

   | Dimension | What It Measures |
   |-----------|-----------------|
   | Mobile Readiness | Does the design work excellently on small screens, not just adequately? |
   | Tablet Optimization | Is the tablet experience thoughtfully designed, not just scaled-up mobile? |
   | Desktop Density | Does the desktop version use the available space well without feeling sparse? |
   | Cross-Device Consistency | Is the experience coherent across devices without being identical? |
   | Input Mode Adaptation | Does the interface adapt to touch, pointer, and keyboard input modes? |

## Output Format

```
## Responsive Audit: [Component/Screen Name]

### Summary
- **Breakpoints tested**: [list]
- **Critical failures**: [X] (horizontal scroll, content loss, touch target violations)
- **Responsive strategy**: [mobile-first / desktop-first / adaptive / fluid]

### Dimension Scores
| Dimension | Score | Key Observation |
|-----------|-------|----------------|
| Mobile Readiness | X/10 | ... |
| Tablet Optimization | X/10 | ... |
| Desktop Density | X/10 | ... |
| Cross-Device Consistency | X/10 | ... |
| Input Mode Adaptation | X/10 | ... |

**Overall Responsive Score**: [average]/10

### Breakpoint-by-Breakpoint Findings

#### Mobile (320-428px)
- **Layout**: [findings]
- **Touch Targets**: [pass/fail with specifics]
- **Typography**: [findings]
- **Navigation**: [pattern and issues]
- **Issues**: [specific problems with fixes]

#### Tablet (768-1024px)
[Same structure]

#### Desktop (1280-1920px)
[Same structure]

#### Ultrawide (2560px+)
[Same structure]

### CSS Recommendations
[Specific CSS code for fixing issues — using modern CSS: container queries, clamp(), logical properties, subgrid]

### Reflow Strategy
[How content should reorganize across breakpoints — with visual diagram if helpful]

### Input Mode Checklist
- [ ] Touch targets ≥ 44px on touch devices
- [ ] Hover states have non-hover fallbacks
- [ ] Focus indicators visible and ≥ 3:1 contrast
- [ ] No hover-only information disclosure
- [ ] Keyboard tab order matches visual order at all breakpoints
```

## Cross-References
When auditing responsive behavior, draw evaluation criteria from:
- `mobile-ux-design` skill for iOS 26 Liquid Glass and Material 3 responsive patterns, safe area insets, and platform-specific touch guidelines
- `desktop-app-design` skill for desktop density, keyboard shortcuts, and multi-window behavior
- `component-patterns-code` skill for modern CSS techniques (container queries, subgrid, `clamp()`, logical properties, `@layer`)
- `accessibility-inclusive-design` skill for WCAG 2.5.5 (Target Size), 1.4.10 (Reflow), 1.3.4 (Orientation), and 2.5.8 (Target Size Enhanced)

## Next Steps
After running `/responsive`, consider:
- `/include` — Full accessibility audit with focus on cross-device a11y (touch a11y, zoom, reflow)
- `/ship` — Rebuild components with production-ready responsive CSS
- `/screen` — Generate a complete responsive screen from scratch
- `/vibe-check` — Heuristic audit at specific breakpoints where issues were found
- `/copy-check` — Check for text truncation and reflow issues across breakpoints
