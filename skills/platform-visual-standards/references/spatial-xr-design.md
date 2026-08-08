# Spatial and XR Design Standards

## The Spatial Computing Landscape

Spatial computing encompasses any interface that extends into three dimensions — augmented reality (AR), virtual reality (VR), mixed reality (MR), and the broader category of extended reality (XR). As of 2025-2026, the major platforms are Apple's visionOS, Meta's Horizon OS, and the open WebXR standard. Each has distinct design conventions, interaction models, and constraints.

---

## visionOS Design System

### Three Content Types

visionOS organizes all content into three spatial modes, each with increasing immersion:

**Windows**
- Flat 2D panels floating in the user's physical space
- Default size: 1280 x 720 points (~0.94m x 0.53m at default distance)
- Can be repositioned, resized (within limits), and multiple windows can coexist
- Glass material chrome (system-provided translucent background)
- This is where most apps live — treat as a floating iPad-like surface
- Respect the window's corner radius (system-provided, ~46pt)

**Volumes**
- 3D bounded containers for objects that need depth
- Fixed size defined by the app (e.g., 500 x 500 x 500 points)
- Cannot be freely resized by the user
- Good for: 3D model viewers, globes, game objects, data visualizations
- Rendered within the user's space alongside other apps
- Objects should fit within the volume boundary — no clipping

**Spaces**
- Full immersive environments controlled entirely by the app
- Two sub-types:
  - **Shared Space**: app coexists with other apps and the passthrough view
  - **Full Space**: app takes over the entire visual field (exclusive)
- Full spaces are for immersive experiences: games, VR videos, meditation environments
- User can always exit via Digital Crown press

### Dynamic Scaling

Windows automatically enlarge as the user pushes them farther away and shrink as they pull them closer. This maintains consistent angular size — text remains readable regardless of distance. Designers do not need to account for this; the system handles it.

### Glass Material in visionOS

- System-standard window chrome uses a glass material similar to Liquid Glass on iOS 26
- Provides translucency that lets the physical environment show through
- Adapts to lighting conditions in the room
- In visionOS 26, updated to match the iOS 26 Liquid Glass aesthetic
- Do NOT use custom opaque backgrounds for window chrome — use the system glass

### Ornaments

Ornaments are floating UI elements attached to a window's edge:
- Typically toolbars, control panels, or secondary navigation
- Positioned outside the window boundary (e.g., bottom edge, leading edge)
- Maintain connection to their parent window when repositioned
- Use for controls that should not consume content space

```swift
// SwiftUI ornament
.ornament(attachmentAnchor: .scene(.bottom)) {
    HStack {
        Button("Play", systemImage: "play.fill") { }
        Button("Pause", systemImage: "pause.fill") { }
    }
    .padding()
    .glassBackgroundEffect()
}
```

---

## visionOS Interaction Model

### Eye Tracking + Hand Pinch (Indirect Interaction)

The primary interaction model in visionOS:

1. **Look**: the user's eyes target an interactive element (the system highlights it with a subtle hover effect)
2. **Pinch**: thumb and index finger come together to select
3. **Drag**: pinch and move the hand to drag content
4. **Zoom**: two-handed pinch and spread

This is the default and most comfortable interaction mode. Users' hands rest in their laps — no arm fatigue.

### Direct Touch

Users can reach out and physically touch virtual UI elements:
- Only for objects within arm's reach (~0.5m)
- Provides a more tangible, immediate feel
- Causes more arm fatigue than indirect interaction
- Use for: spatial 3D objects, immersive game elements, precision tasks
- Touch targets must be larger than indirect targets (fingertip is ~10mm)

### Voice (Siri)

Full Siri integration for voice commands, dictation, and app control. Particularly useful when hands are occupied or for accessibility.

### Keyboard and Trackpad

visionOS supports physical keyboards and trackpads:
- Bluetooth keyboards for text-heavy tasks
- Trackpad for cursor-based interaction (pointer appears in space)
- Essential for productivity apps

### Hover Effects

Every interactive element must have a visible hover state triggered by eye gaze:
- Subtle scale (1.02-1.05x) and/or highlight
- System-provided hover effects for standard components
- Custom hover effects for custom elements
- Hover is the ONLY way users know something is interactive — without it, they cannot use the app

---

## visionOS Interaction Design Rules

### Minimum Interactive Area

- **60 points minimum** for all interactive elements
- Eye tracking + hand pinch is less precise than direct touch on a screen
- This is larger than iOS's 44pt minimum — do not use mobile touch targets in visionOS
- **16 points minimum spacing** between interactive elements to prevent mis-targeting

### Placement Principles

- **Center of field of view**: place essential information and primary actions at eye level, directly ahead
- **Horizontal preference**: wider layouts are more comfortable than tall ones (horizontal head movement is easier than vertical)
- **Avoid extremes**: do not place UI too high (neck strain), too low (uncomfortable downward gaze), or too far to the sides (excessive head turning)
- **Comfortable viewing zone**: approximately 40 degrees horizontal, 30 degrees vertical from center
- **Default distance**: windows appear ~1.5m from the user

### Content Ergonomics

- Avoid forcing the user to turn their head for primary content
- Secondary content can be placed to the sides
- Never place content behind the user
- Keep the most important information at the center
- Use progressive disclosure for dense information

---

## visionOS Typography

### Weight Adjustments for Spatial

Text in spatial environments needs slightly heavier weights than on flat screens because:
- Varying distances affect perceived weight
- Glass materials behind text reduce contrast
- Environmental lighting can wash out thin strokes

| Flat Screen Weight | Spatial Equivalent |
|-------------------|-------------------|
| Regular | Medium |
| Medium | Semibold |
| Semibold | Bold |
| Bold | Heavy |

### Extra Large Title Styles

visionOS introduces extra-large title styles for spatial editorial layouts where windows float at varying distances. These display-size styles ensure headlines remain impactful in 3D space.

### Font: SF Pro (Same as iOS)

SF Pro is the system font. Do not use custom fonts for system chrome. Custom fonts are acceptable for content areas.

---

## Depth Design Principles

### Z-Axis Hierarchy

Depth conveys importance and interactivity:
- **Near (closer to user)**: interactive controls, popovers, alerts — things that demand attention
- **Mid (default window plane)**: primary content
- **Far (behind window plane)**: decorative elements, backgrounds, environment
- Closer = more important, more interactive
- Farther = less important, more ambient

### Shadows and Lighting

- visionOS simulates environmental lighting — shadows shift based on the user's real-world light sources
- Windows cast subtle shadows on surfaces behind them
- Elevated elements (popovers, sheets) cast shadows on the window below
- Do NOT bake shadows into assets — let the system compute them

### Z-Fighting Prevention

When two surfaces occupy the same depth plane, they flicker (z-fighting). Prevention:
- Maintain at least 2-4 points of depth separation between overlapping layers
- Use the system's elevation system rather than manual z-positioning
- Test with head movement — z-fighting is more visible during parallax

### Depth Zones

| Zone | Distance from Window | Content Type |
|------|---------------------|-------------|
| Background | -50 to -200pt | Environment, decorative |
| Base | 0pt | Window content |
| Elevated | +10 to +30pt | Cards, containers |
| Popover | +50 to +100pt | Menus, popovers, tooltips |
| Alert | +150pt+ | Alerts, system dialogs |

---

## visionOS Accessibility

- **Pointer Control**: navigate with head movement, wrist, or index finger tracking
- **Dwell Control**: select by holding gaze on a target for a configurable duration
- **Voice Control**: full voice-based navigation and interaction
- **Switch Control**: external switch devices for users with motor impairments
- **Head Tracking**: use head position as a pointer
- **VoiceOver**: full screen reader support with spatial audio cues indicating element position
- **Reduce Motion**: critical — some users experience discomfort with spatial motion effects
- **Increase Contrast**: thicker borders, more opaque backgrounds, higher text contrast

---

## Meta Quest / Horizon OS

### Overview

Meta Quest (Quest 3, Quest 3S, Quest Pro) runs Horizon OS, which supports both 2D panel interfaces and fully immersive 3D experiences.

### 2D Panel Design

- Default viewport: approximately 1000 x 625 pixels (resizable by user)
- Panels float in the user's space similar to visionOS windows
- System toolbar at bottom of panel for navigation
- Dark themes recommended (reduces VR eye strain)
- Font sizes: minimum 16px at default viewing distance, 20px+ recommended for body text

### Horizon OS UI Kit

- 70+ pages of VR/MR design components available as a Figma community file
- Components include: buttons, toggles, sliders, text fields, scrollable panels, dialogs, tooltips, menus, cards, tabs, navigation bars
- Follows Horizon Design System conventions
- Quarterly updates align with OS releases

### Interaction Model

- **Hand tracking**: pinch, grab, poke (direct touch)
- **Controllers**: pointer ray + trigger for selection, thumbstick for scrolling
- **Eye tracking** (Quest Pro, Quest 3): gaze-aware interfaces
- **Voice**: Meta AI voice commands

### Key Differences from visionOS

| Aspect | visionOS | Horizon OS |
|--------|----------|------------|
| Primary input | Eye + hand pinch | Hand tracking or controllers |
| Window system | System-managed glass | App-managed panels |
| Passthrough | Full-color, high quality | Color, varies by hardware |
| App coexistence | Multiple apps in Shared Space | Limited multitasking |
| Design kit | Apple Design Resources | Horizon OS UI Kit (Figma) |

---

## WebXR

### Progressive Enhancement Strategy

WebXR allows a single codebase to serve 2D, AR, and VR experiences:

1. **2D baseline**: standard web page, accessible everywhere
2. **AR enhancement**: overlay 3D content on camera feed (mobile AR, Quest passthrough)
3. **VR immersion**: full 3D environment (headset)

```javascript
// Check for XR support
if (navigator.xr) {
    const isVRSupported = await navigator.xr.isSessionSupported('immersive-vr');
    const isARSupported = await navigator.xr.isSessionSupported('immersive-ar');
}
```

### Frameworks

**A-Frame (Declarative)**
```html
<a-scene>
    <a-box position="0 1 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
    <a-sphere position="0 1.25 -5" radius="1.25" color="#EF2D5E"></a-sphere>
    <a-sky color="#ECECEC"></a-sky>
</a-scene>
```
- HTML-like syntax for 3D scenes
- Entity-component architecture
- Large ecosystem of community components
- Good for prototyping and simple experiences

**Three.js (Programmatic)**
- Full 3D rendering control
- WebXR integration via `renderer.xr.enabled = true`
- Physics engines (Cannon.js, Rapier)
- Best for complex, performance-critical experiences

### WebXR Design Considerations

- Target 72fps minimum (90fps preferred) to prevent motion sickness
- Provide a 2D fallback for non-XR browsers
- Keep file sizes small — headset browsers have limited memory
- Test on multiple devices — controller layouts differ across headsets
- Respect the user's physical space — do not place objects too close (<0.5m)

---

## AR Overlay Design

### Core Principles

AR overlays digital information onto the physical world. The cardinal rule: **enhance reality, do not overwhelm it**.

### Visual Design for AR

**Transparency and Opacity**
- Ambient information: 20-30% opacity — visible but unobtrusive
- Interactive elements: 60-80% opacity — clearly present but not blocking reality
- Critical alerts: 90-100% opacity — demands attention
- Always allow the physical world to remain the dominant visual

**Anchoring**
- Digital content should be anchored to real-world objects or surfaces
- Floating, unanchored UI feels disconnected and disorienting
- Use plane detection to place content on tables, walls, floors
- Maintain consistent position relative to the anchor as the user moves

**Lightweight Visuals**
- Thin strokes over filled shapes where possible
- Avoid large opaque surfaces that block the real world
- Use outline-style icons rather than filled
- Wire-frame or semi-transparent 3D objects

**Readability**
- Background plates behind text for legibility against varied real-world backgrounds
- High-contrast text (white on dark plate, or dark on light plate)
- Avoid small text — AR is viewed at varying distances
- Minimum 16pt equivalent at expected viewing distance

### Environmental Testing

AR experiences must be tested in diverse conditions:
- **Bright sunlight**: screens dim, colors wash out
- **Low light**: tracking accuracy decreases
- **Complex backgrounds**: busy environments make overlay readability challenging
- **Movement**: user may be walking — stability is critical
- **Mixed surfaces**: reflective and transparent surfaces confuse tracking

### Privacy Considerations

- Camera-based AR requires explicit user permission
- Avoid capturing or processing identifiable faces without consent
- Do not overlay information on people without their knowledge
- Provide clear indicators when the camera is active
- Respect visual privacy zones (private spaces, screens, documents)

---

## Spatial Design Anti-Patterns

These patterns should be actively avoided in spatial/XR design:

### Placing UI Behind the User
Users cannot see what is behind them. Never require turning around to find controls or content. All primary UI should be within the forward 180-degree arc, ideally within 90 degrees.

### Spatial Clutter
Too many floating windows, panels, or 3D objects create visual chaos. Spatial UI should be minimal — fewer elements than a screen-based interface, not more.

### Text-Heavy Interfaces at Distance
Long paragraphs in spatial windows are difficult to read. Use short labels, icons, data visualizations, and progressive disclosure. Save long-form text for close-range windows.

### Ignoring Physical Comfort
- Neck strain from UI placed too high (above 15 degrees from eye level)
- Eye strain from UI placed too close (<0.5m) for extended periods
- Arm fatigue from extended direct manipulation
- Motion sickness from unexpected movement or low frame rates

### Unchanged 2D Patterns
Flat UI patterns do not automatically work in 3D:
- Dropdown menus become awkward in space (what direction do they open?)
- Tooltips need spatial positioning logic
- Scrolling behavior needs adjustment (no scroll wheel — use gaze or gesture)
- Hover states require eye-tracking awareness

### Overusing Depth
More depth layers do not mean better hierarchy. Excessive z-axis variation creates visual noise. Use 3-4 depth levels maximum. Most content should live on the same plane.

### Ignoring Reduce Motion
Some users experience vestibular discomfort from spatial motion effects. Always respect the Reduce Motion accessibility setting. Provide static alternatives for all animated transitions.

---

## Spatial Design Checklist

When designing any spatial/XR experience, validate against these criteria:

- [ ] Primary UI is within comfortable field of view (40 degrees H, 30 degrees V)
- [ ] Interactive elements are at least 60pt (visionOS) or equivalent
- [ ] Minimum 16pt spacing between interactive targets
- [ ] Hover states are visible for all interactive elements
- [ ] Glass/translucent materials used for window chrome (not opaque)
- [ ] Text weights increased by one step for spatial legibility
- [ ] Depth hierarchy limited to 3-4 levels
- [ ] No content placed behind the user
- [ ] Reduce Motion setting respected
- [ ] Frame rate maintains 90fps (visionOS) or 72fps (Quest) minimum
- [ ] 2D fallback available for non-spatial contexts
- [ ] Tested with eye tracking, hand tracking, and accessibility modes
- [ ] Environmental diversity tested (lighting, backgrounds, movement)
