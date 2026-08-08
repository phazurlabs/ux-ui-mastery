# Motion Principles for UI

Disney's twelve principles of animation, translated from character animation
into interface motion. These are the reasoning behind the recipes: read them
when deciding whether a motion is doing a job, not when looking up a duration.

## The Twelve Principles

### Disney's 12 Principles Applied to Interface Design

The 12 principles of animation, originally codified by Frank Thomas and Ollie Johnston for Disney, translate directly into UI motion design. Each principle below maps to concrete interface behavior.

#### 1. Squash and Stretch
Objects compress on impact and elongate in motion. In UI: buttons compress slightly on press (`scaleY(0.95)`), modals stretch subtly as they spring open.
```css
.button:active {
  transform: scaleX(1.02) scaleY(0.96);
  transition: transform 80ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

#### 2. Anticipation
A small preparatory movement before the main action. In UI: a button dips slightly before launching a navigation, a card lifts before being dragged.
```css
.card-draggable:active {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  transition: all 120ms ease-out;
}
```

#### 3. Staging
Direct attention to what matters. In UI: dim the background when a modal appears, highlight the changed element after a save operation.

#### 4. Straight Ahead vs. Pose to Pose
CSS keyframes = pose-to-pose (define key states). JavaScript requestAnimationFrame = straight-ahead (frame-by-frame). For UI, pose-to-pose via keyframes is almost always correct.

#### 5. Follow Through and Overlapping Action
Elements don't all stop at the same time. In UI: when a panel slides in, its children arrive slightly after with staggered delays.
```css
.panel-child:nth-child(1) { animation-delay: 0ms; }
.panel-child:nth-child(2) { animation-delay: 50ms; }
.panel-child:nth-child(3) { animation-delay: 100ms; }
```

#### 6. Slow In and Slow Out (Ease)
Never use linear timing for UI motion. Objects accelerate and decelerate naturally.

#### 7. Arc
Natural motion follows curves, not straight lines. For UI: elements moving across screen should follow slight arcs, not rigid horizontal/vertical paths.

#### 8. Secondary Action
Supporting animations reinforce the primary action. A success checkmark draws while a green background fades in behind it.

#### 9. Timing
The single most critical principle for UI. See Duration Guidelines below.

#### 10. Exaggeration
Amplify for clarity, not realism. A notification badge bounces more than physics would dictate to ensure it's noticed.

#### 11. Solid Drawing (Solid Design)
Maintain spatial consistency. If a card expands from the top-left, it should collapse back to the top-left.

#### 12. Appeal
Animation should feel pleasant, not mechanical. Spring physics with slight overshoot feels more alive than rigid easing.

### Timing Theory

Human perception thresholds that govern animation timing:
- **0-100ms**: Perceived as instant. Use for color changes, opacity toggles, active states.
- **100-300ms**: Perceived as fast but visible. Ideal for most UI transitions.
- **300-500ms**: Perceived as deliberate. Use for large layout changes, page transitions.
- **500ms+**: Perceived as slow. Only for dramatic reveals, onboarding, hero animations.
- **1000ms+**: Feels broken unless there's a visual progress indicator.

**Jakob's Law of Animation**: Users spend most of their time on other sites. Match common animation patterns and durations. Don't be creative with timing unless you have a reason.

**Doherty Threshold**: System responses under 400ms keep users in a flow state. Your animations must finish within this window for interactive elements.

### Easing Mathematics

All easing curves are cubic Bezier functions defined by 4 control points: `cubic-bezier(x1, y1, x2, y2)` where P0=(0,0) and P3=(1,1) are fixed.

**The formula**: `B(t) = (1-t)^3*P0 + 3*(1-t)^2*t*P1 + 3*(1-t)*t^2*P2 + t^3*P3` for t in [0,1].

Spring physics use a different model: damped harmonic oscillation.
**Spring equation**: `x(t) = A * e^(-zeta * omega * t) * cos(omega_d * t + phi)`
where zeta = damping ratio, omega = natural frequency.

---
