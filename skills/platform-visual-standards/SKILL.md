---
name: Platform Visual Standards
description: "Current visual design standards for every major platform and device type — iOS 26 Liquid Glass (materials, vibrancy, SF Symbols 7), Material 3 Expressive (35-shape library, spring physics, HCT color, Dynamic Color), modern web CSS 2025-2026 (container queries, view transitions, scroll-driven animations, oklch(), anchor positioning), watchOS/tvOS/automotive (complications, 10-foot UI, CarPlay), spatial/XR (visionOS, Meta Quest, WebXR), and cross-platform design harmony (one design system, 9 form factors). Use when the user mentions: iOS design, Android design, Material Design, Liquid Glass, SwiftUI, Jetpack Compose, responsive design, platform guidelines, HIG, device-specific, watch app, TV app, car app, spatial design, AR, VR, visionOS, cross-platform, web design, CSS, breakpoints, form factors."
---

# Platform Visual Standards

## Why Platform Visual Standards Matter

Every platform has a visual language — materials, motion curves, typography rules, spacing systems, and interaction idioms. A professional app respects these conventions because users have muscle memory and visual expectations formed by their OS. Ignoring platform standards makes an app feel alien. This skill ensures Sumi knows the current visual standards for every major platform so recommendations are platform-native, not platform-generic.

## Reference Architecture

| File | Contents | Use When |
|------|----------|----------|
| `references/ios-26-liquid-glass.md` | iOS 26/iPadOS 26 Liquid Glass design system: material tiers, vibrancy levels, SF Symbols 7 (rendering modes, variable color, animations), Dynamic Island, StandBy mode, Live Activities, SwiftUI implementation patterns, Safe Areas, Dynamic Type. | Designing for iPhone, iPad. Recommending iOS-native patterns. Implementing Liquid Glass correctly. |
| `references/material-3-expressive.md` | Material Design 3 Expressive: 35-shape library (morphing shapes), spring-physics motion (mass, stiffness, damping), HCT color space, Dynamic Color (wallpaper extraction), M3 component gallery, Jetpack Compose patterns, canonical layouts for tablets/foldables. | Designing for Android, Wear OS. Recommending Material-native patterns. Implementing Dynamic Color. |
| `references/web-css-2025-2026.md` | Modern CSS capabilities: container queries (@container), view transitions API, scroll-driven animations, oklch()/lch() color functions, anchor positioning, CSS nesting, :has() selector, subgrid, @layer cascade layers, @scope, CSS mixins (2026), Figma Sites/new products. | Building web interfaces. Recommending modern CSS patterns. Avoiding outdated approaches. |
| `references/watchos-tvos-automotive.md` | Watch design (Apple Watch, Wear OS): complications, glanceability, Digital Crown. TV design (tvOS, Android TV, Fire TV): 10-foot UI, D-pad navigation, focus system, overscan. Automotive (CarPlay, Android Auto): glanceability, driver safety, touch targets. | Designing for non-phone/tablet devices. Understanding unique constraints of each form factor. |
| `references/spatial-xr-design.md` | Spatial computing: visionOS (windows, volumes, spaces, Liquid Glass), Meta Quest (Horizon OS, 2D panels, immersive), WebXR, AR overlay patterns. Depth, gaze, gesture interaction models. | Designing for AR/VR/MR. Understanding spatial UI constraints. visionOS app design. |
| `references/cross-platform-harmony.md` | How to maintain one design system across 9 form factors: phone, tablet, desktop, TV, watch, spatial, automotive, kiosk, e-ink. Token architecture for multi-platform. Platform adaptation patterns. When to diverge vs. converge. | Building cross-platform design systems. Deciding platform-specific vs. shared patterns. Multi-device strategy. |

## Cross-References

- **`visual-design-mastery`** — Visual principles that apply across all platforms. This skill adapts those principles to platform-specific conventions.
- **`mobile-ux-design`** — Mobile UX patterns. This skill provides the current visual standards those patterns render within.
- **`desktop-app-design`** — Desktop patterns. This skill provides web/macOS/Windows visual standards.
- **`component-patterns-code`** — Code implementations. This skill ensures code targets the right platform APIs.
- **`design-systems-architecture`** — Token architecture. This skill defines platform-specific token overrides.
- **`interaction-motion-design`** — Motion patterns. This skill provides platform-specific animation curves and APIs.
- **`accessibility-inclusive-design`** — Platform-specific accessibility APIs (VoiceOver, TalkBack, ARIA).

## Commands Powered by This Skill

| Command | How This Skill Is Used |
|---------|----------------------|
| `/vision` | Adapts visual direction to target platform conventions |
| `/ship` | Generates platform-native component code |
| `/screen` | Uses platform-specific screen patterns and safe areas |
| `/responsive` | Cross-device adaptation using platform breakpoints |
| `/generate` | Informs AI generation prompts with platform constraints |
| `/assets` | Generates assets at platform-correct sizes and formats |
