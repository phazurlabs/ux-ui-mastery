---
name: animation-recipe-library
description: "200+ production-ready animation recipes with exact CSS/Framer Motion/GSAP code. Covers entrance/exit animations, micro-interactions, page transitions, loading states, scroll-driven animations, spring physics, and reduced motion alternatives. Every recipe includes timing, easing, and copy-paste code. Use when the user mentions: animation, transition, motion, micro-interaction, page transition, entrance animation, exit animation, loading animation, skeleton animation, scroll animation, spring animation, easing, keyframe, framer motion, CSS animation, hover effect, click animation, motion design, GSAP, ScrollTrigger, SplitText, Lenis, smooth scroll, pin and scrub, parallax, horizontal scroll, cursor effect, magnetic button, custom cursor, cursor follower, text animation, typewriter, gradient text, 3D, card tilt, card flip, floating, glassmorphism, noise grain, particle, React Three Fiber, R3F, three.js, counter animation, marquee, ticker, SVG morph, stagger, spotlight."
---

# Animation Recipe Library — 200+ Production Recipes

## Part 1: Animation Principles for UI

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

## Part 2: Duration Guidelines

### Micro Animations (100-200ms)
| Animation | Duration | Use Case |
|-----------|----------|----------|
| Button hover | 120ms | Background color shift |
| Active press | 80ms | Scale down feedback |
| Toggle switch | 150ms | Slide knob position |
| Checkbox check | 150ms | Draw checkmark |
| Radio select | 120ms | Fill indicator |
| Input focus | 150ms | Border color + label float |
| Tooltip show | 100ms | Fade in near cursor |
| Ripple start | 150ms | Material ripple expand |
| Color change | 100ms | Any color transition |
| Opacity toggle | 100ms | Show/hide without motion |
| Icon swap | 120ms | Hamburger to X morph |
| Badge pulse | 150ms | Notification attention |
| Switch label | 100ms | Text swap in toggle |
| Cursor change | 0ms | Instant, never animate cursors |
| Link underline | 150ms | Underline slide in |

### Standard Animations (200-400ms)
| Animation | Duration | Use Case |
|-----------|----------|----------|
| Modal open | 250ms | Scale + fade from center |
| Dropdown expand | 200ms | Menu list reveal |
| Card expand | 300ms | Detail view expansion |
| Toast appear | 250ms | Slide in from edge |
| Sidebar toggle | 250ms | Slide panel in/out |
| Tab content switch | 200ms | Cross-fade tab panels |
| Accordion expand | 250ms | Height reveal |
| FAB action | 200ms | Speed dial expand |
| Snackbar enter | 250ms | Slide up from bottom |
| Drawer open | 300ms | Full-height side panel |
| Chip add/remove | 200ms | Scale + fade |
| Menu item hover | 200ms | Background highlight slide |
| Avatar group expand | 300ms | Spread stacked avatars |
| Card flip | 350ms | 3D rotation reveal |
| Popover | 200ms | Positioned overlay appear |

### Complex Animations (400-700ms)
| Animation | Duration | Use Case |
|-----------|----------|----------|
| Page transition | 400ms | Route change crossfade |
| Shared element | 500ms | Element morph between pages |
| Hero section reveal | 600ms | Landing page first paint |
| List stagger (full) | 400-600ms total | N items with stagger delay |
| Dashboard widget load | 500ms | Chart + card entrance |
| Onboarding step | 500ms | Guided tour transitions |
| Image gallery open | 400ms | Lightbox zoom from thumb |
| Morphing layout | 500ms | Grid to list view change |
| Skeleton to content | 400ms | Loading state resolution |
| Full-screen overlay | 450ms | Immersive view enter |

### Dramatic Animations (700ms+)
| Animation | Duration | Use Case |
|-----------|----------|----------|
| Splash screen | 800-1200ms | App launch branding |
| Success celebration | 800ms | Confetti, checkmark draw |
| Onboarding carousel | 700ms | Slide between intro screens |
| Data visualization | 1000ms | Chart draw-in, count-up |
| Parallax hero | continuous | Scroll-linked background |
| Logo animation | 1000-2000ms | Brand reveal on load |
| Progress completion | 800ms | Circular progress fill to 100% |
| Typewriter text | 50ms/char | Sequential character reveal |

---

## Part 3: Easing Library

### Production Easing Custom Properties

```css
:root {
  /* === Core Easings === */
  --ease-out:          cubic-bezier(0.16, 1, 0.3, 1);         /* Decelerate — entrances */
  --ease-out-soft:     cubic-bezier(0.33, 1, 0.68, 1);        /* Gentle decelerate */
  --ease-out-quad:     cubic-bezier(0.25, 0.46, 0.45, 0.94);  /* Quadratic decelerate */
  --ease-out-cubic:    cubic-bezier(0.22, 0.61, 0.36, 1);     /* Cubic decelerate */
  --ease-out-quart:    cubic-bezier(0.17, 0.84, 0.44, 1);     /* Quartic decelerate */
  --ease-out-quint:    cubic-bezier(0.23, 1, 0.32, 1);        /* Quintic decelerate */
  --ease-out-expo:     cubic-bezier(0.16, 1, 0.3, 1);         /* Exponential decelerate */
  --ease-out-circ:     cubic-bezier(0.08, 0.82, 0.17, 1);     /* Circular decelerate */
  --ease-out-back:     cubic-bezier(0.34, 1.56, 0.64, 1);     /* Overshoot decelerate */

  --ease-in:           cubic-bezier(0.55, 0.055, 0.675, 0.19);/* Accelerate — exits */
  --ease-in-soft:      cubic-bezier(0.32, 0, 0.67, 0);        /* Gentle accelerate */
  --ease-in-quad:      cubic-bezier(0.55, 0.085, 0.68, 0.53); /* Quadratic accelerate */
  --ease-in-cubic:     cubic-bezier(0.55, 0.055, 0.675, 0.19);/* Cubic accelerate */
  --ease-in-quart:     cubic-bezier(0.9, 0.03, 0.69, 0.22);   /* Quartic accelerate */
  --ease-in-expo:      cubic-bezier(0.7, 0, 0.84, 0);         /* Exponential accelerate */
  --ease-in-back:      cubic-bezier(0.36, 0, 0.66, -0.56);    /* Pull-back accelerate */

  --ease-in-out:       cubic-bezier(0.87, 0, 0.13, 1);        /* Symmetric — movement */
  --ease-in-out-soft:  cubic-bezier(0.45, 0, 0.55, 1);        /* Gentle symmetric */
  --ease-in-out-quad:  cubic-bezier(0.46, 0.03, 0.52, 0.96);  /* Quadratic symmetric */
  --ease-in-out-cubic: cubic-bezier(0.65, 0, 0.35, 1);        /* Cubic symmetric */
  --ease-in-out-back:  cubic-bezier(0.68, -0.6, 0.32, 1.6);   /* Overshoot symmetric */

  /* === Spring Physics (CSS approximations) === */
  --spring-gentle:     cubic-bezier(0.34, 1.56, 0.64, 1);     /* stiffness:120 damping:14 */
  --spring-bouncy:     cubic-bezier(0.68, -0.55, 0.27, 1.55); /* stiffness:180 damping:12 */
  --spring-snappy:     cubic-bezier(0.25, 1.5, 0.5, 1);       /* stiffness:300 damping:20 */
  --spring-wobbly:     cubic-bezier(0.36, 1.7, 0.5, 0.9);     /* stiffness:150 damping:8 */
  --spring-stiff:      cubic-bezier(0.12, 1.2, 0.4, 1);       /* stiffness:400 damping:30 */
  --spring-slow:       cubic-bezier(0.34, 1.3, 0.64, 1);      /* stiffness:80 damping:20 */

  /* === Bounce === */
  --bounce:            cubic-bezier(0.34, 1.56, 0.64, 1);     /* Single overshoot bounce */
  --bounce-heavy:      cubic-bezier(0.68, -0.55, 0.27, 1.55); /* Double overshoot */

  /* === Elastic (requires @keyframes for true elastic) === */
  --elastic-out:       cubic-bezier(0.36, 1.7, 0.5, 0.85);    /* Approximation of elastic */

  /* === Emphasis === */
  --emphasis-dramatic:  cubic-bezier(0.04, 0.62, 0.23, 0.98);
  --emphasis-energetic: cubic-bezier(0.22, 0.68, 0, 1.71);

  /* === Platform-Specific === */
  --ios-spring:        cubic-bezier(0.25, 0.8, 0.25, 1);      /* iOS default animation */
  --material-standard: cubic-bezier(0.2, 0, 0, 1);            /* M3 standard easing */
  --material-decel:    cubic-bezier(0, 0, 0, 1);              /* M3 decelerate */
  --material-accel:    cubic-bezier(0.3, 0, 1, 1);            /* M3 accelerate */
  --material-emphasized: cubic-bezier(0.2, 0, 0, 1);          /* M3 emphasized */
}
```

### Framer Motion Spring Presets

```tsx
// Gentle — modals, overlays, panels
const springGentle = { type: "spring", stiffness: 120, damping: 14, mass: 1 };

// Bouncy — playful UI, notifications, FABs
const springBouncy = { type: "spring", stiffness: 180, damping: 12, mass: 1 };

// Snappy — toggles, switches, small elements
const springSnappy = { type: "spring", stiffness: 300, damping: 20, mass: 0.8 };

// Wobbly — emphasis, celebrations, attention-grab
const springWobbly = { type: "spring", stiffness: 150, damping: 8, mass: 1 };

// Stiff — precise, utility, no-nonsense
const springStiff = { type: "spring", stiffness: 400, damping: 30, mass: 1 };

// Slow — large-area reveals, page transitions
const springSlow = { type: "spring", stiffness: 80, damping: 20, mass: 1.2 };

// iOS-like — platform-matching for hybrid apps
const springIOS = { type: "spring", stiffness: 200, damping: 22, mass: 1 };

// Material-like — for M3 matching
const springMaterial = { type: "spring", stiffness: 250, damping: 25, mass: 1 };
```

### When to Use Each Easing

| Easing | Use For | Avoid For |
|--------|---------|-----------|
| ease-out | Entrances, appearing elements | Exits, disappearing elements |
| ease-in | Exits, disappearing elements | Entrances (feels sluggish) |
| ease-in-out | Position changes, slides between states | Quick micro-interactions |
| ease-out-back | Playful entrances, bouncing buttons | Serious/enterprise UI |
| spring (gentle) | Modals, sheets, overlays | Rapid repeated actions |
| spring (snappy) | Toggles, switches, small controls | Large page transitions |
| spring (bouncy) | Notifications, celebrations | Data-heavy interfaces |
| linear | Progress bars, continuous rotation only | Everything else |

---

## Part 4: Animation Recipes by Category

### A. Entrance Animations (25 recipes)

#### A1. fadeIn
**Duration**: 200ms | **Easing**: ease-out | **Use**: Default entrance for any element
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.fade-in { animation: fadeIn 200ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.2 }} />
```

#### A2. slideUp
**Duration**: 250ms | **Easing**: ease-out | **Use**: Toasts, bottom sheets, list items
```css
@keyframes slideUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}
.slide-up { animation: slideUp 250ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }} />
```

#### A3. slideDown
**Duration**: 250ms | **Easing**: ease-out | **Use**: Dropdowns, notification bars
```css
@keyframes slideDown {
  from { opacity: 0; transform: translateY(-16px); }
  to { opacity: 1; transform: translateY(0); }
}
.slide-down { animation: slideDown 250ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, y: -16 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }} />
```

#### A4. slideLeft
**Duration**: 250ms | **Easing**: ease-out | **Use**: Side panels, drawer content
```css
@keyframes slideLeft {
  from { opacity: 0; transform: translateX(24px); }
  to { opacity: 1; transform: translateX(0); }
}
.slide-left { animation: slideLeft 250ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, x: 24 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }} />
```

#### A5. slideRight
**Duration**: 250ms | **Easing**: ease-out | **Use**: Back navigation, returning panels
```css
@keyframes slideRight {
  from { opacity: 0; transform: translateX(-24px); }
  to { opacity: 1; transform: translateX(0); }
}
.slide-right { animation: slideRight 250ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, x: -24 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }} />
```

#### A6. scaleIn
**Duration**: 200ms | **Easing**: spring-gentle | **Use**: Modals, popovers, tooltips
```css
@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}
.scale-in { animation: scaleIn 200ms var(--spring-gentle) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} transition={{ type: "spring", stiffness: 300, damping: 20 }} />
```

#### A7. expandIn
**Duration**: 300ms | **Easing**: ease-out | **Use**: Accordion content, expanding cards
```css
@keyframes expandIn {
  from { opacity: 0; max-height: 0; overflow: hidden; }
  to { opacity: 1; max-height: 500px; overflow: hidden; }
}
.expand-in { animation: expandIn 300ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: "auto" }} transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }} />
```

#### A8. revealText
**Duration**: 400ms | **Easing**: ease-out | **Use**: Hero headlines, section titles
```css
@keyframes revealText {
  from { clip-path: inset(0 100% 0 0); opacity: 0; }
  to { clip-path: inset(0 0% 0 0); opacity: 1; }
}
.reveal-text { animation: revealText 400ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ clipPath: "inset(0 100% 0 0)", opacity: 0 }} animate={{ clipPath: "inset(0 0% 0 0)", opacity: 1 }} transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }} />
```

#### A9. typewriter
**Duration**: 50ms/char | **Easing**: steps | **Use**: AI chat responses, terminal-style text
```css
.typewriter {
  overflow: hidden;
  white-space: nowrap;
  border-right: 2px solid;
  width: 0;
  animation: typing 2s steps(30) forwards, blink 0.7s step-end infinite;
}
@keyframes typing { to { width: 100%; } }
@keyframes blink { 50% { border-color: transparent; } }
```
```tsx
// Use framer-motion with a custom character-by-character approach
const TypeWriter = ({ text }: { text: string }) => {
  return (
    <motion.span>
      {text.split("").map((char, i) => (
        <motion.span key={i} initial={{ opacity: 0 }} animate={{ opacity: 1 }}
          transition={{ delay: i * 0.05 }}>{char}</motion.span>
      ))}
    </motion.span>
  );
};
```

#### A10. staggerChildren
**Duration**: 200ms each, 50ms stagger | **Easing**: ease-out | **Use**: Lists, grids, navigation items
```css
.stagger-parent > * {
  opacity: 0; animation: slideUp 200ms var(--ease-out) forwards;
}
.stagger-parent > *:nth-child(1) { animation-delay: 0ms; }
.stagger-parent > *:nth-child(2) { animation-delay: 50ms; }
.stagger-parent > *:nth-child(3) { animation-delay: 100ms; }
.stagger-parent > *:nth-child(4) { animation-delay: 150ms; }
.stagger-parent > *:nth-child(5) { animation-delay: 200ms; }
```
```tsx
<motion.ul initial="hidden" animate="visible"
  variants={{ visible: { transition: { staggerChildren: 0.05 } } }}>
  {items.map(item => (
    <motion.li key={item.id}
      variants={{ hidden: { opacity: 0, y: 16 }, visible: { opacity: 1, y: 0 } }}
      transition={{ duration: 0.2, ease: [0.16, 1, 0.3, 1] }} />
  ))}
</motion.ul>
```

#### A11. flipIn
**Duration**: 400ms | **Easing**: ease-out | **Use**: Card reveals, game elements
```css
@keyframes flipIn {
  from { opacity: 0; transform: perspective(800px) rotateY(-90deg); }
  to { opacity: 1; transform: perspective(800px) rotateY(0deg); }
}
.flip-in { animation: flipIn 400ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, rotateY: -90 }} animate={{ opacity: 1, rotateY: 0 }}
  style={{ perspective: 800 }} transition={{ duration: 0.4 }} />
```

#### A12. rotateIn
**Duration**: 300ms | **Easing**: ease-out-back | **Use**: Icons, badges, notification dots
```css
@keyframes rotateIn {
  from { opacity: 0; transform: rotate(-180deg) scale(0.5); }
  to { opacity: 1; transform: rotate(0deg) scale(1); }
}
.rotate-in { animation: rotateIn 300ms var(--ease-out-back) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, rotate: -180, scale: 0.5 }} animate={{ opacity: 1, rotate: 0, scale: 1 }}
  transition={{ type: "spring", stiffness: 200, damping: 15 }} />
```

#### A13. bounceIn
**Duration**: 500ms | **Easing**: spring-bouncy | **Use**: Celebration states, achievements
```css
@keyframes bounceIn {
  0% { opacity: 0; transform: scale(0.3); }
  50% { opacity: 1; transform: scale(1.1); }
  70% { transform: scale(0.95); }
  100% { transform: scale(1); }
}
.bounce-in { animation: bounceIn 500ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, scale: 0.3 }} animate={{ opacity: 1, scale: 1 }}
  transition={{ type: "spring", stiffness: 180, damping: 12 }} />
```

#### A14. blurIn
**Duration**: 300ms | **Easing**: ease-out | **Use**: Background content, image loads
```css
@keyframes blurIn {
  from { opacity: 0; filter: blur(12px); }
  to { opacity: 1; filter: blur(0px); }
}
.blur-in { animation: blurIn 300ms var(--ease-out) forwards; }
```
```tsx
<motion.div initial={{ opacity: 0, filter: "blur(12px)" }} animate={{ opacity: 1, filter: "blur(0px)" }}
  transition={{ duration: 0.3 }} />
```

#### A15. clipReveal
**Duration**: 400ms | **Easing**: ease-out-quart | **Use**: Hero images, section reveals
```css
@keyframes clipReveal {
  from { clip-path: circle(0% at 50% 50%); }
  to { clip-path: circle(100% at 50% 50%); }
}
.clip-reveal { animation: clipReveal 400ms var(--ease-out-quart) forwards; }
```
```tsx
<motion.div initial={{ clipPath: "circle(0% at 50% 50%)" }} animate={{ clipPath: "circle(100% at 50% 50%)" }}
  transition={{ duration: 0.4, ease: [0.17, 0.84, 0.44, 1] }} />
```

#### A16. slideUpFade
**Duration**: 300ms | **Easing**: ease-out | **Use**: Cards, content sections, list items
```css
@keyframes slideUpFade {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}
.slide-up-fade { animation: slideUpFade 300ms var(--ease-out) forwards; }
```

#### A17. growFromCenter
**Duration**: 250ms | **Easing**: spring-snappy | **Use**: Tooltips, context menus
```css
@keyframes growFromCenter {
  from { opacity: 0; transform: scale(0.8) translateY(4px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}
.grow-center { animation: growFromCenter 250ms var(--spring-snappy) forwards; }
```

#### A18. dropIn
**Duration**: 350ms | **Easing**: ease-out-back | **Use**: Modals dropping from top
```css
@keyframes dropIn {
  from { opacity: 0; transform: translateY(-40px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
.drop-in { animation: dropIn 350ms var(--ease-out-back) forwards; }
```

#### A19. zoomIn
**Duration**: 300ms | **Easing**: ease-out | **Use**: Image lightbox, detail views
```css
@keyframes zoomIn {
  from { opacity: 0; transform: scale(0.5); }
  to { opacity: 1; transform: scale(1); }
}
.zoom-in { animation: zoomIn 300ms var(--ease-out) forwards; }
```

#### A20. curtainReveal
**Duration**: 500ms | **Easing**: ease-in-out | **Use**: Full-screen reveals, hero sections
```css
@keyframes curtainReveal {
  from { clip-path: inset(0 50% 0 50%); }
  to { clip-path: inset(0 0% 0 0%); }
}
.curtain-reveal { animation: curtainReveal 500ms var(--ease-in-out) forwards; }
```

#### A21. unfoldDown
**Duration**: 350ms | **Easing**: ease-out | **Use**: Accordion, expandable sections
```css
@keyframes unfoldDown {
  from { opacity: 0; transform: scaleY(0); transform-origin: top; }
  to { opacity: 1; transform: scaleY(1); transform-origin: top; }
}
.unfold-down { animation: unfoldDown 350ms var(--ease-out) forwards; }
```

#### A22. swingIn
**Duration**: 400ms | **Easing**: ease-out-back | **Use**: Notification bells, playful icons
```css
@keyframes swingIn {
  0% { opacity: 0; transform: rotate(-30deg); transform-origin: top center; }
  60% { transform: rotate(10deg); }
  80% { transform: rotate(-5deg); }
  100% { opacity: 1; transform: rotate(0deg); }
}
.swing-in { animation: swingIn 400ms var(--ease-out) forwards; }
```

#### A23. elasticIn
**Duration**: 600ms | **Easing**: custom | **Use**: Playful UI, gamification elements
```css
@keyframes elasticIn {
  0% { opacity: 0; transform: scale(0.5); }
  60% { transform: scale(1.15); }
  75% { transform: scale(0.95); }
  90% { transform: scale(1.03); }
  100% { opacity: 1; transform: scale(1); }
}
.elastic-in { animation: elasticIn 600ms ease-out forwards; }
```

#### A24. morphIn
**Duration**: 400ms | **Easing**: ease-out | **Use**: Shape transitions, icon morphing
```css
@keyframes morphIn {
  from { opacity: 0; border-radius: 50%; transform: scale(0.6); }
  to { opacity: 1; border-radius: 8px; transform: scale(1); }
}
.morph-in { animation: morphIn 400ms var(--ease-out) forwards; }
```

#### A25. wipeIn
**Duration**: 450ms | **Easing**: ease-out | **Use**: Image reveals, section transitions
```css
@keyframes wipeIn {
  from { clip-path: polygon(0 0, 0 0, 0 100%, 0 100%); }
  to { clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); }
}
.wipe-in { animation: wipeIn 450ms var(--ease-out) forwards; }
```

---

### B. Exit Animations (18 recipes)

#### B1. fadeOut
**Duration**: 150ms | **Easing**: ease-in | **Use**: Default exit for any element
```css
@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}
.fade-out { animation: fadeOut 150ms var(--ease-in) forwards; }
```
```tsx
<motion.div exit={{ opacity: 0 }} transition={{ duration: 0.15 }} />
```

#### B2. slideOutDown
**Duration**: 200ms | **Easing**: ease-in | **Use**: Dismissing toasts, bottom sheets
```css
@keyframes slideOutDown {
  from { opacity: 1; transform: translateY(0); }
  to { opacity: 0; transform: translateY(16px); }
}
.slide-out-down { animation: slideOutDown 200ms var(--ease-in) forwards; }
```

#### B3. slideOutUp
**Duration**: 200ms | **Easing**: ease-in | **Use**: Dismissing notifications upward
```css
@keyframes slideOutUp {
  from { opacity: 1; transform: translateY(0); }
  to { opacity: 0; transform: translateY(-16px); }
}
.slide-out-up { animation: slideOutUp 200ms var(--ease-in) forwards; }
```

#### B4. slideOutLeft
**Duration**: 200ms | **Easing**: ease-in | **Use**: Swipe-to-dismiss, forward navigation
```css
@keyframes slideOutLeft {
  from { opacity: 1; transform: translateX(0); }
  to { opacity: 0; transform: translateX(-24px); }
}
.slide-out-left { animation: slideOutLeft 200ms var(--ease-in) forwards; }
```

#### B5. slideOutRight
**Duration**: 200ms | **Easing**: ease-in | **Use**: Back navigation, drawer close
```css
@keyframes slideOutRight {
  from { opacity: 1; transform: translateX(0); }
  to { opacity: 0; transform: translateX(24px); }
}
.slide-out-right { animation: slideOutRight 200ms var(--ease-in) forwards; }
```

#### B6. scaleOut
**Duration**: 150ms | **Easing**: ease-in | **Use**: Modal dismiss, popover close
```css
@keyframes scaleOut {
  from { opacity: 1; transform: scale(1); }
  to { opacity: 0; transform: scale(0.9); }
}
.scale-out { animation: scaleOut 150ms var(--ease-in) forwards; }
```

#### B7. collapseOut
**Duration**: 250ms | **Easing**: ease-in | **Use**: Accordion close, collapsible sections
```css
@keyframes collapseOut {
  from { opacity: 1; max-height: 500px; overflow: hidden; }
  to { opacity: 0; max-height: 0; overflow: hidden; }
}
.collapse-out { animation: collapseOut 250ms var(--ease-in) forwards; }
```

#### B8. dissolve
**Duration**: 200ms | **Easing**: ease-in | **Use**: Transitioning between states
```css
@keyframes dissolve {
  from { opacity: 1; filter: blur(0px); }
  to { opacity: 0; filter: blur(4px); }
}
.dissolve { animation: dissolve 200ms var(--ease-in) forwards; }
```

#### B9. shrinkOut
**Duration**: 200ms | **Easing**: ease-in | **Use**: Removing tags, chips, badges
```css
@keyframes shrinkOut {
  from { opacity: 1; transform: scale(1); }
  to { opacity: 0; transform: scale(0.5); }
}
.shrink-out { animation: shrinkOut 200ms var(--ease-in) forwards; }
```

#### B10. flipOut
**Duration**: 300ms | **Easing**: ease-in | **Use**: Card flip away
```css
@keyframes flipOut {
  from { opacity: 1; transform: perspective(800px) rotateY(0); }
  to { opacity: 0; transform: perspective(800px) rotateY(90deg); }
}
.flip-out { animation: flipOut 300ms var(--ease-in) forwards; }
```

#### B11. zoomOut
**Duration**: 200ms | **Easing**: ease-in | **Use**: Closing lightbox, image zoom
```css
@keyframes zoomOut {
  from { opacity: 1; transform: scale(1); }
  to { opacity: 0; transform: scale(0.5); }
}
.zoom-out { animation: zoomOut 200ms var(--ease-in) forwards; }
```

#### B12. dropOut
**Duration**: 200ms | **Easing**: ease-in | **Use**: Items falling off screen
```css
@keyframes dropOut {
  from { opacity: 1; transform: translateY(0); }
  to { opacity: 0; transform: translateY(40px); }
}
.drop-out { animation: dropOut 200ms var(--ease-in) forwards; }
```

#### B13. clipOut
**Duration**: 300ms | **Easing**: ease-in | **Use**: Section hide, reveal reverse
```css
@keyframes clipOut {
  from { clip-path: circle(100% at 50% 50%); }
  to { clip-path: circle(0% at 50% 50%); }
}
.clip-out { animation: clipOut 300ms var(--ease-in) forwards; }
```

#### B14. wipeOut
**Duration**: 350ms | **Easing**: ease-in | **Use**: Page exits, full-section dismissals
```css
@keyframes wipeOut {
  from { clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); }
  to { clip-path: polygon(100% 0, 100% 0, 100% 100%, 100% 100%); }
}
.wipe-out { animation: wipeOut 350ms var(--ease-in) forwards; }
```

#### B15. rotateOut
**Duration**: 250ms | **Easing**: ease-in | **Use**: Icon transitions, playful dismiss
```css
@keyframes rotateOut {
  from { opacity: 1; transform: rotate(0deg); }
  to { opacity: 0; transform: rotate(90deg) scale(0.7); }
}
.rotate-out { animation: rotateOut 250ms var(--ease-in) forwards; }
```

#### B16. blurOut
**Duration**: 200ms | **Easing**: ease-in | **Use**: Background dismiss, defocus
```css
@keyframes blurOut {
  from { opacity: 1; filter: blur(0); }
  to { opacity: 0; filter: blur(8px); }
}
.blur-out { animation: blurOut 200ms var(--ease-in) forwards; }
```

#### B17. sinkOut
**Duration**: 250ms | **Easing**: ease-in | **Use**: Cards being archived/deleted
```css
@keyframes sinkOut {
  from { opacity: 1; transform: translateY(0) scale(1); }
  to { opacity: 0; transform: translateY(20px) scale(0.9); }
}
.sink-out { animation: sinkOut 250ms var(--ease-in) forwards; }
```

#### B18. foldOut
**Duration**: 300ms | **Easing**: ease-in | **Use**: Collapsible panels closing
```css
@keyframes foldOut {
  from { opacity: 1; transform: scaleY(1); transform-origin: top; }
  to { opacity: 0; transform: scaleY(0); transform-origin: top; }
}
.fold-out { animation: foldOut 300ms var(--ease-in) forwards; }
```

---

### C. Micro-Interaction Recipes (35 recipes)

#### C1. buttonPress
**Duration**: 80ms down, 120ms up | **Easing**: ease-out
```css
.btn { transition: transform 120ms var(--ease-out); }
.btn:active { transform: scale(0.96); transition-duration: 80ms; }
```
```tsx
<motion.button whileTap={{ scale: 0.96 }} transition={{ type: "spring", stiffness: 400, damping: 25 }} />
```

#### C2. buttonHover
**Duration**: 150ms | **Easing**: ease-out
```css
.btn { transition: all 150ms var(--ease-out); }
.btn:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
```
```tsx
<motion.button whileHover={{ y: -1, boxShadow: "0 4px 12px rgba(0,0,0,0.1)" }}
  transition={{ duration: 0.15 }} />
```

#### C3. toggleSwitch
**Duration**: 150ms | **Easing**: spring-snappy
```css
.toggle-knob {
  transition: transform 150ms var(--spring-snappy);
}
.toggle-input:checked + .toggle-knob {
  transform: translateX(20px);
}
```
```tsx
<motion.div animate={{ x: isOn ? 20 : 0 }}
  transition={{ type: "spring", stiffness: 300, damping: 20 }} />
```

#### C4. checkboxCheck
**Duration**: 150ms | **Easing**: ease-out
```css
@keyframes checkDraw {
  from { stroke-dashoffset: 24; }
  to { stroke-dashoffset: 0; }
}
.checkbox-check {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
  animation: checkDraw 150ms var(--ease-out) forwards;
}
```

#### C5. radioSelect
**Duration**: 120ms | **Easing**: spring-snappy
```css
.radio-dot {
  transform: scale(0);
  transition: transform 120ms var(--spring-snappy);
}
.radio-input:checked + .radio-dot {
  transform: scale(1);
}
```

#### C6. inputFocus
**Duration**: 150ms | **Easing**: ease-out
```css
.input {
  border: 2px solid #e2e8f0;
  transition: border-color 150ms var(--ease-out), box-shadow 150ms var(--ease-out);
}
.input:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
}
```

#### C7. ripple
**Duration**: 400ms | **Easing**: ease-out
```css
@keyframes ripple {
  from { transform: scale(0); opacity: 0.5; }
  to { transform: scale(4); opacity: 0; }
}
.ripple-effect {
  position: absolute; border-radius: 50%; background: rgba(255,255,255,0.3);
  animation: ripple 400ms var(--ease-out) forwards;
}
```

#### C8. heartbeat
**Duration**: 300ms | **Easing**: ease-in-out
```css
@keyframes heartbeat {
  0%, 100% { transform: scale(1); }
  25% { transform: scale(1.15); }
  50% { transform: scale(1); }
  75% { transform: scale(1.08); }
}
.heartbeat { animation: heartbeat 300ms var(--ease-in-out); }
```

#### C9. shake
**Duration**: 400ms | **Easing**: ease-out | **Use**: Error states, invalid input
```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-6px); }
  40% { transform: translateX(6px); }
  60% { transform: translateX(-4px); }
  80% { transform: translateX(4px); }
}
.shake { animation: shake 400ms var(--ease-out); }
```
```tsx
<motion.div animate={hasError ? { x: [0, -6, 6, -4, 4, 0] } : { x: 0 }}
  transition={{ duration: 0.4 }} />
```

#### C10. wiggle
**Duration**: 300ms | **Easing**: ease-out | **Use**: Attention grab, playful nudge
```css
@keyframes wiggle {
  0%, 100% { transform: rotate(0); }
  25% { transform: rotate(-5deg); }
  50% { transform: rotate(5deg); }
  75% { transform: rotate(-3deg); }
}
.wiggle { animation: wiggle 300ms var(--ease-out); }
```

#### C11. pulse
**Duration**: 1500ms | **Easing**: ease-in-out | **Use**: Live indicators, loading dots
```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
.pulse { animation: pulse 1500ms var(--ease-in-out) infinite; }
```

#### C12. spin
**Duration**: 800ms | **Easing**: linear | **Use**: Loading spinners only
```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.spin { animation: spin 800ms linear infinite; }
```

#### C13. thumbUp
**Duration**: 400ms | **Easing**: spring-bouncy | **Use**: Like/reaction feedback
```css
@keyframes thumbUp {
  0% { transform: scale(1); }
  30% { transform: scale(1.3) rotate(-10deg); }
  60% { transform: scale(0.95); }
  100% { transform: scale(1); }
}
.thumb-up { animation: thumbUp 400ms var(--ease-out); }
```

#### C14. cardHoverLift
**Duration**: 200ms | **Easing**: ease-out
```css
.card {
  transition: transform 200ms var(--ease-out), box-shadow 200ms var(--ease-out);
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.1);
}
```

#### C15. linkUnderlineSlide
**Duration**: 200ms | **Easing**: ease-out
```css
.link { position: relative; text-decoration: none; }
.link::after {
  content: ''; position: absolute; bottom: -2px; left: 0;
  width: 0; height: 2px; background: currentColor;
  transition: width 200ms var(--ease-out);
}
.link:hover::after { width: 100%; }
```

#### C16. iconMorphHamburger
**Duration**: 250ms | **Easing**: ease-in-out
```css
.hamburger-line {
  transition: transform 250ms var(--ease-in-out), opacity 150ms var(--ease-in-out);
}
.is-open .hamburger-line:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
.is-open .hamburger-line:nth-child(2) { opacity: 0; }
.is-open .hamburger-line:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }
```

#### C17. switchLabel
**Duration**: 100ms | **Easing**: ease-out
```css
.switch-label { transition: opacity 100ms var(--ease-out), color 100ms var(--ease-out); }
```

#### C18. chipAdd
**Duration**: 200ms | **Easing**: spring-gentle
```css
@keyframes chipAdd {
  from { opacity: 0; transform: scale(0.7); }
  to { opacity: 1; transform: scale(1); }
}
.chip-add { animation: chipAdd 200ms var(--spring-gentle) forwards; }
```

#### C19. counterFlip
**Duration**: 300ms | **Easing**: ease-out
```css
@keyframes counterFlip {
  from { opacity: 0; transform: translateY(-100%); }
  to { opacity: 1; transform: translateY(0); }
}
.counter-digit { animation: counterFlip 300ms var(--ease-out) forwards; }
```

#### C20. tooltipAppear
**Duration**: 100ms | **Easing**: ease-out
```css
.tooltip {
  opacity: 0; transform: translateY(4px) scale(0.98);
  transition: all 100ms var(--ease-out);
}
.trigger:hover + .tooltip { opacity: 1; transform: translateY(0) scale(1); }
```

#### C21. dropdownExpand
**Duration**: 200ms | **Easing**: ease-out
```css
.dropdown {
  opacity: 0; transform: translateY(-8px) scaleY(0.95);
  transform-origin: top; transition: all 200ms var(--ease-out);
}
.dropdown.is-open { opacity: 1; transform: translateY(0) scaleY(1); }
```

#### C22. fabExpand
**Duration**: 200ms | **Easing**: spring-gentle
```css
@keyframes fabExpand {
  from { opacity: 0; transform: scale(0) rotate(-45deg); }
  to { opacity: 1; transform: scale(1) rotate(0deg); }
}
.fab-action { animation: fabExpand 200ms var(--spring-gentle) forwards; }
```

#### C23. slideLikeDelete
**Duration**: 250ms | **Easing**: ease-in
```css
@keyframes slideDelete {
  from { transform: translateX(0); opacity: 1; max-height: 60px; }
  50% { transform: translateX(-100%); opacity: 0; max-height: 60px; }
  to { max-height: 0; padding: 0; margin: 0; }
}
.slide-delete { animation: slideDelete 250ms var(--ease-in) forwards; }
```

#### C24. badgeBounce
**Duration**: 400ms | **Easing**: spring-bouncy
```css
@keyframes badgeBounce {
  0% { transform: scale(0); }
  60% { transform: scale(1.2); }
  80% { transform: scale(0.9); }
  100% { transform: scale(1); }
}
.badge-bounce { animation: badgeBounce 400ms var(--ease-out) forwards; }
```

#### C25. progressFill
**Duration**: 600ms | **Easing**: ease-out
```css
.progress-bar {
  width: 0; transition: width 600ms var(--ease-out);
}
.progress-bar[data-value="100"] { width: 100%; }
```

#### C26. skeletonShimmer
**Duration**: 1500ms | **Easing**: linear | **Use**: Loading placeholders
```css
@keyframes shimmer {
  from { background-position: -200% 0; }
  to { background-position: 200% 0; }
}
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1500ms linear infinite;
}
```

#### C27. inputLabelFloat
**Duration**: 150ms | **Easing**: ease-out
```css
.float-label {
  position: absolute; top: 16px; left: 12px;
  transition: all 150ms var(--ease-out);
  font-size: 16px; color: #94a3b8;
}
.input:focus ~ .float-label, .input:not(:placeholder-shown) ~ .float-label {
  top: 4px; font-size: 12px; color: #3b82f6;
}
```

#### C28. notificationSlideIn
**Duration**: 250ms | **Easing**: spring-gentle
```css
@keyframes notifSlide {
  from { opacity: 0; transform: translateX(100%); }
  to { opacity: 1; transform: translateX(0); }
}
.notification { animation: notifSlide 250ms var(--spring-gentle) forwards; }
```

#### C29. menuItemHighlight
**Duration**: 150ms | **Easing**: ease-out
```css
.menu-item { position: relative; }
.menu-item::before {
  content: ''; position: absolute; inset: 0;
  background: rgba(0,0,0,0.05); border-radius: 6px;
  opacity: 0; transition: opacity 150ms var(--ease-out);
}
.menu-item:hover::before { opacity: 1; }
```

#### C30. starRating
**Duration**: 200ms staggered | **Easing**: spring-bouncy
```css
.star {
  transition: transform 200ms var(--spring-bouncy), color 100ms var(--ease-out);
}
.star.active { transform: scale(1.2); color: #f59e0b; }
.star:nth-child(1) { transition-delay: 0ms; }
.star:nth-child(2) { transition-delay: 30ms; }
.star:nth-child(3) { transition-delay: 60ms; }
```

#### C31. searchExpand
**Duration**: 300ms | **Easing**: ease-out
```css
.search-input {
  width: 40px; transition: width 300ms var(--ease-out);
}
.search-input:focus { width: 240px; }
```

#### C32. avatarStack
**Duration**: 200ms | **Easing**: ease-out
```css
.avatar-stack .avatar {
  transition: transform 200ms var(--ease-out), margin 200ms var(--ease-out);
}
.avatar-stack:hover .avatar { margin-left: 4px; }
.avatar-stack .avatar:hover { transform: translateY(-4px) scale(1.1); z-index: 1; }
```

#### C33. tabIndicatorSlide
**Duration**: 250ms | **Easing**: spring-snappy
```css
.tab-indicator {
  position: absolute; bottom: 0; height: 2px; background: #3b82f6;
  transition: left 250ms var(--spring-snappy), width 250ms var(--spring-snappy);
}
```

#### C34. switchTheme
**Duration**: 300ms | **Easing**: ease-in-out
```css
.theme-transition * {
  transition: background-color 300ms var(--ease-in-out), color 300ms var(--ease-in-out),
              border-color 300ms var(--ease-in-out), box-shadow 300ms var(--ease-in-out);
}
```

#### C35. dragFeedback
**Duration**: instant grab, 200ms release | **Easing**: spring-gentle
```css
.draggable { transition: transform 200ms var(--spring-gentle), box-shadow 200ms ease-out; }
.draggable.is-dragging {
  transform: scale(1.03) rotate(1deg);
  box-shadow: 0 16px 40px rgba(0,0,0,0.15);
  transition: none;
}
```

---

### D. Page Transitions (18 recipes)

#### D1. crossFade
**Duration**: 300ms | **Easing**: ease-in-out
```css
.page-enter { animation: fadeIn 300ms var(--ease-out) forwards; }
.page-exit { animation: fadeOut 200ms var(--ease-in) forwards; }
```
```tsx
<AnimatePresence mode="wait">
  <motion.div key={route} initial={{ opacity: 0 }} animate={{ opacity: 1 }}
    exit={{ opacity: 0 }} transition={{ duration: 0.3 }} />
</AnimatePresence>
```

#### D2. slideTransition
**Duration**: 400ms | **Easing**: ease-in-out
```css
.page-enter { animation: slideRight 400ms var(--ease-in-out) forwards; }
.page-exit { animation: slideOutLeft 300ms var(--ease-in) forwards; }
```
```tsx
<AnimatePresence mode="wait">
  <motion.div key={route} initial={{ x: "100%" }} animate={{ x: 0 }}
    exit={{ x: "-100%" }} transition={{ duration: 0.4, ease: [0.87, 0, 0.13, 1] }} />
</AnimatePresence>
```

#### D3. sharedElement (View Transitions API)
**Duration**: 350ms | **Easing**: ease-in-out
```css
::view-transition-old(card-hero) {
  animation: fadeOut 200ms var(--ease-in) forwards;
}
::view-transition-new(card-hero) {
  animation: fadeIn 350ms var(--ease-out) forwards;
}
.card-hero { view-transition-name: card-hero; }
```
```tsx
// With Framer Motion layoutId
<motion.div layoutId="card-hero" transition={{ duration: 0.35, ease: [0.87, 0, 0.13, 1] }} />
```

#### D4. morphTransition
**Duration**: 500ms | **Easing**: ease-in-out
```tsx
<motion.div layoutId={`card-${id}`} transition={{ type: "spring", stiffness: 200, damping: 25 }}>
  {isExpanded ? <FullView /> : <CardView />}
</motion.div>
```

#### D5. scaleTransition
**Duration**: 350ms | **Easing**: ease-out
```css
.page-enter {
  animation: scaleIn 350ms var(--ease-out) forwards;
}
.page-exit {
  animation: scaleOut 250ms var(--ease-in) forwards;
}
```

#### D6. modalOverlay
**Duration**: 250ms overlay, 300ms modal | **Easing**: ease-out
```css
.overlay {
  opacity: 0; transition: opacity 250ms var(--ease-out);
  background: rgba(0,0,0,0.5); backdrop-filter: blur(4px);
}
.overlay.is-open { opacity: 1; }
.modal {
  opacity: 0; transform: scale(0.95) translateY(8px);
  transition: all 300ms var(--spring-gentle);
}
.modal.is-open { opacity: 1; transform: scale(1) translateY(0); }
```

#### D7. drawerSlide
**Duration**: 300ms | **Easing**: ease-out
```css
.drawer {
  transform: translateX(-100%);
  transition: transform 300ms var(--ease-out);
}
.drawer.is-open { transform: translateX(0); }
```

#### D8. bottomSheet
**Duration**: 350ms | **Easing**: spring-gentle
```css
.bottom-sheet {
  transform: translateY(100%);
  transition: transform 350ms var(--spring-gentle);
}
.bottom-sheet.is-open { transform: translateY(0); }
```

#### D9. stackNavigation
**Duration**: 350ms | **Easing**: ios-spring | **Use**: iOS-style push/pop
```css
.stack-enter { animation: slideLeft 350ms var(--ios-spring) forwards; }
.stack-exit { animation: fadeOut 200ms var(--ease-in) forwards; transform: scale(0.95); }
```

#### D10. tabSwitch
**Duration**: 200ms | **Easing**: ease-out
```css
.tab-panel {
  opacity: 0; transition: opacity 200ms var(--ease-out);
}
.tab-panel.is-active { opacity: 1; }
```

#### D11. zoomDrillDown
**Duration**: 400ms | **Easing**: ease-out
```css
.drill-enter { animation: zoomIn 400ms var(--ease-out) forwards; }
.drill-exit { animation: zoomOut 300ms var(--ease-in) forwards; }
```

#### D12. verticalSlide
**Duration**: 350ms | **Easing**: ease-in-out
```tsx
<AnimatePresence mode="wait">
  <motion.div key={route} initial={{ y: "100%", opacity: 0 }}
    animate={{ y: 0, opacity: 1 }} exit={{ y: "-50%", opacity: 0 }}
    transition={{ duration: 0.35 }} />
</AnimatePresence>
```

#### D13. revealFromEdge
**Duration**: 400ms | **Easing**: ease-out
```css
@keyframes revealFromLeft {
  from { clip-path: inset(0 100% 0 0); }
  to { clip-path: inset(0 0 0 0); }
}
.reveal-left { animation: revealFromLeft 400ms var(--ease-out) forwards; }
```

#### D14. flipPage
**Duration**: 500ms | **Easing**: ease-in-out
```css
@keyframes flipPage {
  from { transform: perspective(1200px) rotateY(0); }
  to { transform: perspective(1200px) rotateY(-180deg); }
}
.flip-page { animation: flipPage 500ms var(--ease-in-out) forwards; }
```

#### D15. fadeThrough
**Duration**: 350ms total | **Easing**: ease-in-out (M3 pattern)
```tsx
<AnimatePresence mode="wait">
  <motion.div key={route} initial={{ opacity: 0, scale: 0.92 }}
    animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0 }}
    transition={{ duration: 0.35 }} />
</AnimatePresence>
```

#### D16. containerTransform
**Duration**: 500ms | **Easing**: material-emphasized | **Use**: M3 container transform
```tsx
<motion.div layoutId={`container-${id}`}
  transition={{ duration: 0.5, ease: [0.2, 0, 0, 1] }}>
  {isExpanded ? <DetailView /> : <CompactView />}
</motion.div>
```

#### D17. viewTransitionAPI
**Duration**: browser-managed | **Use**: Native cross-document transitions
```js
// Same-document transition
document.startViewTransition(() => {
  updateDOM();
});

// Cross-document (Chrome 126+)
// Set in CSS:
@view-transition { navigation: auto; }
::view-transition-old(root) { animation: fadeOut 200ms ease-in; }
::view-transition-new(root) { animation: fadeIn 300ms ease-out; }
```

#### D18. parallaxTransition
**Duration**: 500ms | **Easing**: ease-out
```tsx
<AnimatePresence mode="popLayout">
  <motion.div key={route}
    initial={{ x: "100%", zIndex: 1 }}
    animate={{ x: 0, zIndex: 1 }}
    exit={{ x: "-30%", zIndex: 0 }}
    transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }} />
</AnimatePresence>
```

---

### E. Loading Animations (16 recipes)

#### E1. spinner
**Duration**: 800ms | **Easing**: linear
```css
@keyframes spin { to { transform: rotate(360deg); } }
.spinner {
  width: 24px; height: 24px;
  border: 2.5px solid #e2e8f0; border-top-color: #3b82f6;
  border-radius: 50%; animation: spin 800ms linear infinite;
}
```

#### E2. skeleton
**Duration**: 1500ms | **Easing**: linear
```css
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1500ms linear infinite;
  border-radius: 4px;
}
```

#### E3. shimmerOverlay
**Duration**: 1800ms | **Easing**: linear
```css
@keyframes shimmerOverlay {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}
.shimmer-overlay::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
  animation: shimmerOverlay 1800ms linear infinite;
}
```

#### E4. progressBar
**Duration**: variable | **Easing**: ease-out
```css
.progress-track { height: 4px; background: #e2e8f0; border-radius: 2px; overflow: hidden; }
.progress-fill {
  height: 100%; background: #3b82f6; border-radius: 2px;
  transition: width 400ms var(--ease-out);
}
```

#### E5. bouncingDots
**Duration**: 1200ms | **Easing**: ease-in-out
```css
@keyframes dotBounce {
  0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
  40% { transform: scale(1); opacity: 1; }
}
.dot { animation: dotBounce 1200ms var(--ease-in-out) infinite; }
.dot:nth-child(1) { animation-delay: 0ms; }
.dot:nth-child(2) { animation-delay: 160ms; }
.dot:nth-child(3) { animation-delay: 320ms; }
```

#### E6. indeterminateBar
**Duration**: 2000ms | **Easing**: ease-in-out
```css
@keyframes indeterminate {
  0% { transform: translateX(-100%) scaleX(0.3); }
  50% { transform: translateX(0%) scaleX(0.5); }
  100% { transform: translateX(100%) scaleX(0.3); }
}
.indeterminate { animation: indeterminate 2000ms var(--ease-in-out) infinite; }
```

#### E7. circularProgress
**Duration**: 1400ms | **Easing**: linear
```css
@keyframes circularSpin {
  0% { stroke-dashoffset: 280; transform: rotate(0deg); }
  50% { stroke-dashoffset: 75; }
  100% { stroke-dashoffset: 280; transform: rotate(360deg); }
}
.circular-progress circle {
  stroke-dasharray: 280; animation: circularSpin 1400ms linear infinite;
}
```

#### E8. pulseLoader
**Duration**: 1200ms | **Easing**: ease-in-out
```css
@keyframes pulseLoad {
  0%, 100% { transform: scale(0.8); opacity: 0.5; }
  50% { transform: scale(1); opacity: 1; }
}
.pulse-loader { animation: pulseLoad 1200ms var(--ease-in-out) infinite; }
```

#### E9. barLoader
**Duration**: 1000ms per bar | **Easing**: ease-in-out
```css
@keyframes barGrow {
  0%, 100% { transform: scaleY(0.4); }
  50% { transform: scaleY(1); }
}
.bar { width: 4px; height: 24px; animation: barGrow 1000ms var(--ease-in-out) infinite; }
.bar:nth-child(1) { animation-delay: 0ms; }
.bar:nth-child(2) { animation-delay: 100ms; }
.bar:nth-child(3) { animation-delay: 200ms; }
.bar:nth-child(4) { animation-delay: 300ms; }
```

#### E10. fadingText
**Duration**: 2000ms | **Easing**: ease-in-out
```css
@keyframes fadingText {
  0%, 100% { opacity: 0; }
  20%, 80% { opacity: 1; }
}
.loading-text span { animation: fadingText 2000ms var(--ease-in-out) infinite; }
```

#### E11. orbitDots
**Duration**: 1600ms | **Easing**: linear
```css
@keyframes orbit {
  from { transform: rotate(0deg) translateX(16px) rotate(0deg); }
  to { transform: rotate(360deg) translateX(16px) rotate(-360deg); }
}
.orbit-dot { animation: orbit 1600ms linear infinite; }
.orbit-dot:nth-child(2) { animation-delay: -400ms; }
.orbit-dot:nth-child(3) { animation-delay: -800ms; }
```

#### E12. typingIndicator
**Duration**: 1400ms | **Easing**: ease-in-out
```css
@keyframes typingDot {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-6px); }
}
.typing-dot { animation: typingDot 1400ms var(--ease-in-out) infinite; }
.typing-dot:nth-child(1) { animation-delay: 0ms; }
.typing-dot:nth-child(2) { animation-delay: 200ms; }
.typing-dot:nth-child(3) { animation-delay: 400ms; }
```

#### E13. skeletonToContent
**Duration**: 400ms | **Easing**: ease-out
```css
@keyframes skeletonReveal {
  from { opacity: 0; filter: blur(4px); }
  to { opacity: 1; filter: blur(0px); }
}
.content-loaded { animation: skeletonReveal 400ms var(--ease-out) forwards; }
```

#### E14. percentageCounter
**Duration**: variable | **Use**: Numeric loading progress
```tsx
const Counter = ({ target }: { target: number }) => {
  const count = useMotionValue(0);
  const rounded = useTransform(count, Math.round);
  useEffect(() => { animate(count, target, { duration: 1.5 }); }, [target]);
  return <motion.span>{rounded}</motion.span>;
};
```

#### E15. stepProgress
**Duration**: 300ms per step | **Easing**: spring-snappy
```css
.step-dot {
  transition: all 300ms var(--spring-snappy);
}
.step-dot.completed { background: #3b82f6; transform: scale(1.1); }
.step-connector {
  transition: background 300ms var(--ease-out);
}
.step-connector.completed { background: #3b82f6; }
```

#### E16. optimisticUI
**Duration**: instant show, 200ms confirm | **Use**: Show result before server confirms
```css
.optimistic { opacity: 0.7; transition: opacity 200ms var(--ease-out); }
.optimistic.confirmed { opacity: 1; }
.optimistic.failed { animation: shake 400ms var(--ease-out); opacity: 1; }
```

---

### F. Scroll-Driven Animations (16 recipes)

#### F1. parallax
**CSS Scroll-Driven (modern)**:
```css
.parallax-bg {
  animation: parallaxMove linear;
  animation-timeline: scroll();
  animation-range: 0% 100%;
}
@keyframes parallaxMove {
  from { transform: translateY(0); }
  to { transform: translateY(-30%); }
}
```

#### F2. fadeOnScroll (Intersection Observer)
```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
    }
  });
}, { threshold: 0.15 });
document.querySelectorAll('.scroll-reveal').forEach(el => observer.observe(el));
```
```css
.scroll-reveal { opacity: 0; transform: translateY(20px); transition: all 500ms var(--ease-out); }
.scroll-reveal.is-visible { opacity: 1; transform: translateY(0); }
```

#### F3. stickyReveal
```css
.sticky-header {
  position: sticky; top: 0;
  transition: all 300ms var(--ease-out);
}
.sticky-header.is-scrolled {
  backdrop-filter: blur(12px);
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  padding-block: 8px;
}
```

#### F4. countUp
```tsx
const CountUp = ({ end, duration = 2 }: { end: number; duration?: number }) => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true });
  const count = useMotionValue(0);
  const rounded = useTransform(count, Math.round);
  useEffect(() => {
    if (isInView) animate(count, end, { duration });
  }, [isInView]);
  return <motion.span ref={ref}>{rounded}</motion.span>;
};
```

#### F5. progressIndicator (scroll progress bar)
```css
.scroll-progress {
  position: fixed; top: 0; left: 0; height: 3px;
  background: #3b82f6; transform-origin: left;
  animation: scaleProgress linear;
  animation-timeline: scroll();
}
@keyframes scaleProgress {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

#### F6. scrollRevealStagger
```tsx
const StaggerOnScroll = ({ children }: { children: React.ReactNode }) => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-10%" });
  return (
    <motion.div ref={ref} initial="hidden" animate={isInView ? "visible" : "hidden"}
      variants={{ visible: { transition: { staggerChildren: 0.08 } } }}>
      {React.Children.map(children, child => (
        <motion.div variants={{ hidden: { opacity: 0, y: 24 }, visible: { opacity: 1, y: 0 } }}
          transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}>{child}</motion.div>
      ))}
    </motion.div>
  );
};
```

#### F7. horizontalScrollSnap
```css
.scroll-container {
  display: flex; overflow-x: auto; scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
}
.scroll-item { scroll-snap-align: start; flex: 0 0 80%; }
```

#### F8. scrollLinkedOpacity
```css
.scroll-fade {
  animation: scrollFade linear;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}
@keyframes scrollFade {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}
```

#### F9. scrollLinkedScale
```css
.scroll-scale {
  animation: scrollScale linear;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}
@keyframes scrollScale {
  from { transform: scale(0.8); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}
```

#### F10. scrollVideoPlayback
```js
const video = document.querySelector('video');
window.addEventListener('scroll', () => {
  const scrollFraction = window.scrollY / (document.body.scrollHeight - window.innerHeight);
  video.currentTime = scrollFraction * video.duration;
});
```

#### F11. pinnedScrollSection
```css
.pinned-section {
  position: sticky; top: 0; height: 100vh;
}
.pinned-content {
  animation: pinnedReveal linear;
  animation-timeline: scroll(nearest);
}
```

#### F12. scrollColorShift
```css
.color-section {
  animation: colorShift linear;
  animation-timeline: scroll();
}
@keyframes colorShift {
  0% { background-color: #1e293b; color: white; }
  50% { background-color: #f8fafc; color: #1e293b; }
  100% { background-color: #1e293b; color: white; }
}
```

#### F13. scrollTextHighlight
```css
.highlight-text {
  background: linear-gradient(90deg, #fbbf24, #fbbf24) no-repeat;
  background-size: 0% 100%;
  animation: highlightDraw linear;
  animation-timeline: view();
  animation-range: entry 50% cover 50%;
}
@keyframes highlightDraw {
  to { background-size: 100% 100%; }
}
```

#### F14. scrollRotate
```css
.scroll-rotate {
  animation: scrollRotate linear;
  animation-timeline: scroll();
}
@keyframes scrollRotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

#### F15. scrollBlur
```css
.scroll-blur {
  animation: scrollBlur linear;
  animation-timeline: view();
  animation-range: exit 0% exit 100%;
}
@keyframes scrollBlur {
  from { filter: blur(0); opacity: 1; }
  to { filter: blur(8px); opacity: 0; }
}
```

#### F16. scrollCounter
```js
const animateCounter = (el, target) => {
  const observer = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      let current = 0;
      const step = target / 60;
      const timer = setInterval(() => {
        current += step;
        if (current >= target) { el.textContent = target; clearInterval(timer); }
        else { el.textContent = Math.round(current); }
      }, 16);
      observer.disconnect();
    }
  }, { threshold: 0.5 });
  observer.observe(el);
};
```

---

### G. Layout Animations (12 recipes)

#### G1. listReorder
```tsx
<Reorder.Group values={items} onReorder={setItems}>
  {items.map(item => (
    <Reorder.Item key={item.id} value={item}
      transition={{ type: "spring", stiffness: 300, damping: 25 }}>
      {item.label}
    </Reorder.Item>
  ))}
</Reorder.Group>
```

#### G2. gridMorph (grid to list and back)
```css
.grid-container {
  display: grid;
  transition: grid-template-columns 400ms var(--ease-in-out);
}
.grid-container.is-list { grid-template-columns: 1fr; }
.grid-container.is-grid { grid-template-columns: repeat(3, 1fr); }
.grid-container > * { transition: all 400ms var(--ease-in-out); }
```

#### G3. accordionExpand
```tsx
<motion.div initial={false} animate={{ height: isOpen ? "auto" : 0 }}
  transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
  style={{ overflow: "hidden" }}>
  <div style={{ padding: "16px" }}>{content}</div>
</motion.div>
```

#### G4. tabSwitch
```tsx
<AnimatePresence mode="wait">
  <motion.div key={activeTab}
    initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -8 }}
    transition={{ duration: 0.2 }} />
</AnimatePresence>
```

#### G5. carouselSlide
```css
.carousel-track {
  display: flex; transition: transform 400ms var(--ease-out);
}
.carousel-track[data-slide="0"] { transform: translateX(0); }
.carousel-track[data-slide="1"] { transform: translateX(-100%); }
.carousel-track[data-slide="2"] { transform: translateX(-200%); }
```

#### G6. masonry
```tsx
<motion.div layout transition={{ type: "spring", stiffness: 200, damping: 25 }}>
  {items.map(item => (
    <motion.div key={item.id} layout
      initial={{ opacity: 0 }} animate={{ opacity: 1 }}
      exit={{ opacity: 0 }} transition={{ duration: 0.3 }} />
  ))}
</motion.div>
```

#### G7. listItemAdd
```tsx
<AnimatePresence>
  {items.map(item => (
    <motion.div key={item.id}
      initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: "auto" }}
      exit={{ opacity: 0, height: 0 }} transition={{ duration: 0.25 }} />
  ))}
</AnimatePresence>
```

#### G8. listItemRemove
```tsx
<motion.div exit={{ opacity: 0, x: -100, height: 0, marginBottom: 0 }}
  transition={{ duration: 0.25, ease: [0.55, 0.055, 0.675, 0.19] }} />
```

#### G9. columnResize
```css
.resizable-panel {
  transition: flex-basis 300ms var(--ease-in-out);
}
```

#### G10. cardExpandDetail
```tsx
<motion.div layoutId={`card-${id}`} onClick={() => setSelected(id)}
  transition={{ type: "spring", stiffness: 200, damping: 25 }}>
  <motion.h2 layoutId={`title-${id}`}>{title}</motion.h2>
  <AnimatePresence>
    {isSelected && <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }}>{body}</motion.p>}
  </AnimatePresence>
</motion.div>
```

#### G11. sidebarCollapse
```css
.sidebar {
  width: 240px; transition: width 250ms var(--ease-in-out);
  overflow: hidden;
}
.sidebar.is-collapsed { width: 64px; }
.sidebar-label { transition: opacity 150ms var(--ease-in); }
.sidebar.is-collapsed .sidebar-label { opacity: 0; }
```

#### G12. splitView
```css
.split-container { display: flex; }
.split-left, .split-right {
  transition: flex 300ms var(--ease-in-out);
}
.split-container.focus-left .split-left { flex: 2; }
.split-container.focus-left .split-right { flex: 1; }
```

---

### H. Gesture Animations (12 recipes)

#### H1. drag
```tsx
<motion.div drag dragConstraints={{ left: -100, right: 100, top: -100, bottom: 100 }}
  dragElastic={0.1} whileDrag={{ scale: 1.05, cursor: "grabbing" }}
  transition={{ type: "spring", stiffness: 300, damping: 25 }} />
```

#### H2. swipeToDismiss
```tsx
const SwipeDismiss = ({ onDismiss, children }) => (
  <motion.div drag="x" dragConstraints={{ left: 0, right: 0 }}
    onDragEnd={(_, info) => { if (Math.abs(info.offset.x) > 100) onDismiss(); }}
    animate={{ x: 0 }} exit={{ x: info.offset.x > 0 ? 300 : -300, opacity: 0 }}
    transition={{ type: "spring", stiffness: 300, damping: 25 }}>
    {children}
  </motion.div>
);
```

#### H3. swipeCard (Tinder-style)
```tsx
<motion.div drag="x" dragConstraints={{ left: 0, right: 0 }}
  style={{ rotate, x }} whileDrag={{ scale: 1.02 }}
  onDragEnd={(_, info) => {
    if (info.offset.x > 150) handleLike();
    else if (info.offset.x < -150) handlePass();
  }}
  transition={{ type: "spring", stiffness: 300, damping: 20 }} />
```

#### H4. pinchZoom
```tsx
const [scale, setScale] = useState(1);
// Use touch events
<div onTouchMove={handlePinch} style={{ transform: `scale(${scale})`, transition: "transform 100ms ease-out" }} />
```

#### H5. longPress
```tsx
<motion.button onTapStart={() => startTimer()} onTap={() => cancelTimer()} onTapCancel={() => cancelTimer()}
  whileTap={{ scale: 0.98 }}>
  <motion.div className="progress-ring"
    animate={isHolding ? { pathLength: 1 } : { pathLength: 0 }}
    transition={{ duration: 1.5 }} />
</motion.button>
```

#### H6. pullToRefresh
```tsx
const PullToRefresh = ({ onRefresh, children }) => {
  const y = useMotionValue(0);
  const opacity = useTransform(y, [0, 80], [0, 1]);
  return (
    <motion.div drag="y" dragConstraints={{ top: 0, bottom: 0 }}
      dragElastic={0.4} style={{ y }}
      onDragEnd={(_, info) => { if (info.offset.y > 80) onRefresh(); }}>
      <motion.div style={{ opacity }} className="refresh-indicator">
        <Spinner />
      </motion.div>
      {children}
    </motion.div>
  );
};
```

#### H7. dragToReorder
```tsx
<Reorder.Group axis="y" values={items} onReorder={setItems}>
  {items.map(item => (
    <Reorder.Item key={item.id} value={item}
      whileDrag={{ scale: 1.03, boxShadow: "0 8px 24px rgba(0,0,0,0.15)" }}
      transition={{ type: "spring", stiffness: 300, damping: 25 }} />
  ))}
</Reorder.Group>
```

#### H8. rubberBand (overscroll)
```css
.scrollable {
  overscroll-behavior: contain;
}
/* Custom rubber band effect */
.rubber-band { transition: transform 300ms var(--spring-bouncy); }
.rubber-band.is-overpulled { transform: scaleY(1.03); }
```

#### H9. gestureRotate
```tsx
<motion.div drag dragMomentum={false}
  onDrag={(_, info) => {
    const angle = Math.atan2(info.point.y - center.y, info.point.x - center.x);
    setRotation(angle * (180 / Math.PI));
  }}
  style={{ rotate: rotation }} />
```

#### H10. snapToGrid
```tsx
<motion.div drag dragSnapToOrigin={false}
  dragConstraints={containerRef}
  onDragEnd={(_, info) => {
    const snappedX = Math.round(info.point.x / gridSize) * gridSize;
    const snappedY = Math.round(info.point.y / gridSize) * gridSize;
    // animate to snapped position
  }}
  transition={{ type: "spring", stiffness: 400, damping: 30 }} />
```

#### H11. swipeNavigation
```tsx
<motion.div drag="x" dragConstraints={{ left: 0, right: 0 }}
  onDragEnd={(_, info) => {
    if (info.velocity.x < -500) goNext();
    else if (info.velocity.x > 500) goPrev();
  }} />
```

#### H12. doubleTapZoom
```tsx
const [zoomed, setZoomed] = useState(false);
<motion.div onDoubleClick={() => setZoomed(!zoomed)}
  animate={{ scale: zoomed ? 2 : 1 }}
  transition={{ type: "spring", stiffness: 300, damping: 25 }} />
```

---

## Part 5: Reduced Motion

### The prefers-reduced-motion Contract

Users who enable "Reduce Motion" in their OS settings may experience motion sickness (vestibular disorders), seizures, or attention difficulties. Respecting this preference is both an accessibility requirement (WCAG 2.1 SC 2.3.3) and a legal obligation in many jurisdictions.

### Global Reduced Motion Reset
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### What to Keep vs. Remove

| Keep (non-motion alternatives) | Remove |
|-------------------------------|--------|
| Opacity fades (subtle, < 200ms) | Slides, translations, transforms |
| Color changes | Parallax scrolling |
| Instant state changes | Bouncing, spring physics |
| Static indicators | Auto-playing animations |
| Focus outlines | Scroll-driven movement |

### Framer Motion Reduced Motion
```tsx
import { useReducedMotion } from "framer-motion";

const Component = () => {
  const shouldReduce = useReducedMotion();
  return (
    <motion.div
      initial={{ opacity: 0, y: shouldReduce ? 0 : 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: shouldReduce ? 0 : 0.3 }}
    />
  );
};
```

### Per-Animation Override Pattern
```css
.slide-up {
  animation: slideUp 250ms var(--ease-out) forwards;
}
@media (prefers-reduced-motion: reduce) {
  .slide-up {
    animation: fadeIn 0.01ms forwards; /* Fade only, no spatial motion */
  }
}
```

---

## Part 6: Performance

### The Compositing Model

Browsers render in 3 phases: **Layout** -> **Paint** -> **Composite**. For smooth 60fps animation, stay in the Composite layer.

#### Composite-only properties (GPU-accelerated, jank-free):
- `transform` (translate, scale, rotate)
- `opacity`
- `filter` (with will-change)

#### Paint properties (avoid animating):
- `background-color`, `color`, `box-shadow`, `border-color`

#### Layout properties (never animate):
- `width`, `height`, `padding`, `margin`, `top`, `left`, `font-size`

### will-change

```css
/* DO: Declare before animation starts, remove after */
.card { will-change: transform; }
.card.animation-done { will-change: auto; }

/* DON'T: Apply to everything */
* { will-change: transform; } /* Memory disaster */
```

### Performance Rules

1. **Use `transform` and `opacity` only** for animations whenever possible
2. **Avoid animating `box-shadow`** — use `::after` pseudo-element with opacity instead:
```css
.card { position: relative; }
.card::after {
  content: ''; position: absolute; inset: 0; border-radius: inherit;
  box-shadow: 0 12px 32px rgba(0,0,0,0.15);
  opacity: 0; transition: opacity 200ms ease-out;
}
.card:hover::after { opacity: 1; }
```
3. **Use `contain: layout`** on animated containers to prevent layout thrash
4. **Avoid animating `height`** — use `max-height`, `scaleY`, or `grid-template-rows: 0fr/1fr`
5. **Batch DOM reads and writes** — don't interleave `getBoundingClientRect()` with style changes
6. **Use `requestAnimationFrame`** for JS animations, never `setTimeout`
7. **Test on low-end devices** — Chrome DevTools > Performance > CPU 4x slowdown

### CSS `content-visibility` for Scroll Performance
```css
.offscreen-section {
  content-visibility: auto;
  contain-intrinsic-size: 0 500px;
}
```

---

## Part 7: Orchestration

### Stagger Patterns

#### Linear Stagger
Each child enters sequentially with a fixed delay.
```tsx
variants={{ visible: { transition: { staggerChildren: 0.05 } } }}
```
**Best for**: Lists, navigation items, grid cards.

#### Cascade Stagger
Delay increases per item (accelerating or decelerating).
```css
.item:nth-child(1) { animation-delay: 0ms; }
.item:nth-child(2) { animation-delay: 60ms; }
.item:nth-child(3) { animation-delay: 130ms; }
.item:nth-child(4) { animation-delay: 210ms; }
/* Increasing gaps: 60, 70, 80... */
```

#### Center-Out Stagger
Items animate from the center outward.
```tsx
const getDelay = (index: number, total: number) => {
  const center = Math.floor(total / 2);
  return Math.abs(index - center) * 0.05;
};
```

#### Random Stagger
Subtle random delays for organic feel.
```tsx
transition={{ delay: Math.random() * 0.3 }}
```

### Choreography Patterns

**Sequential**: A finishes, then B starts, then C starts. For dependent actions.
```tsx
<motion.div animate={controls}>
  {/* Trigger B after A */}
  await controlsA.start({ opacity: 1 });
  await controlsB.start({ x: 0 });
  await controlsC.start({ scale: 1 });
</motion.div>
```

**Parallel**: A, B, C all start together. For independent elements.
```tsx
initial={{ opacity: 0, y: 20, scale: 0.9 }}
animate={{ opacity: 1, y: 0, scale: 1 }}
/* All properties animate simultaneously */
```

**Overlapping**: B starts before A finishes. For fluid choreography.
```tsx
variants={{
  visible: {
    transition: { staggerChildren: 0.05, delayChildren: 0.1 }
  }
}}
```

### Orchestration with useAnimation
```tsx
const controls = useAnimation();
const sequence = async () => {
  await controls.start("step1");
  await controls.start("step2");
  await controls.start("step3");
};
```

---

## Part 8: State Machines for Animation

### Animation State Model

Every animation follows a state machine: `idle -> animating -> done`

More complex UI animations use expanded states:

```
idle -> entering -> entered -> exiting -> exited
```

### Implementation with Framer Motion + React state

```tsx
type AnimState = "idle" | "entering" | "entered" | "exiting" | "exited";
const [state, setState] = useState<AnimState>("idle");

<motion.div
  animate={
    state === "entering" ? { opacity: 1, y: 0 } :
    state === "exiting" ? { opacity: 0, y: -16 } :
    state === "idle" ? { opacity: 0, y: 16 } :
    { opacity: 1, y: 0 }
  }
  onAnimationComplete={() => {
    if (state === "entering") setState("entered");
    if (state === "exiting") setState("exited");
  }}
/>
```

### Interruptible Animations

Animations must handle interruption gracefully. If a user hovers then immediately un-hovers, the exit animation should start from the current interpolated value, not snap to the end of the entrance.

Framer Motion handles this automatically. For CSS, use `transition` (not `animation`) so the browser interpolates from the current value:
```css
.element {
  transform: translateY(0); opacity: 1;
  transition: all 200ms var(--ease-out);
}
.element.is-hidden {
  transform: translateY(16px); opacity: 0;
}
/* Switching classes mid-animation interpolates correctly */
```

### Multi-Stage Animation Pattern
```tsx
const variants = {
  initial: { opacity: 0, scale: 0.8, y: 40 },
  enter: {
    opacity: 1, scale: 1, y: 0,
    transition: {
      duration: 0.4,
      opacity: { duration: 0.25 },
      scale: { type: "spring", stiffness: 200, damping: 20 },
      y: { type: "spring", stiffness: 150, damping: 18 }
    }
  },
  exit: {
    opacity: 0, scale: 0.95,
    transition: { duration: 0.2 }
  }
};
```

---

## Cross-References

- **interaction-motion-design** — Motion principles, haptics, platform conventions
- **component-patterns-code** — React/SwiftUI/CSS component implementations
- **performance-states-patterns** — Loading, error, empty, skeleton states
- **platform-visual-standards** — iOS Liquid Glass, M3 Expressive motion specs
- **accessibility-inclusive-design** — WCAG motion requirements, vestibular triggers
- **visual-design-mastery** — Timing as a design dimension, motion in visual hierarchy

## Reference Files

Detailed code recipes are available in the `references/` directory:
- `css-animation-recipes.md` — 40+ complete CSS @keyframes recipes
- `framer-motion-recipes.md` — 40+ Framer Motion React component recipes
- `scroll-gesture-recipes.md` — Scroll-driven and gesture animation code
- `gsap-scrolltrigger-recipes.md` — 25 GSAP + ScrollTrigger production recipes: useGSAP() hook, Lenis smooth scroll, pin-and-scrub, horizontal scroll gallery, SplitText character/line/word animation, parallax layers, scale-to-full hero, counter animation, timeline sequences, marquee/ticker, magnetic button, SVG morph, stagger grid entrance, Next.js App Router integration, gsap.matchMedia() responsive, performance guide
- `cursor-text-3d-effects.md` — 20 "wow factor" recipes: custom cursor follower (GSAP quickTo), magnetic elements, cursor state changes, cursor trail, spotlight/flashlight effect, CSS animation-timeline text reveal, Framer Motion char stagger, typewriter, gradient text animation, text blur reveal, word carousel, 3D card tilt (mousemove), 3D card flip, floating elements, noise/grain overlay, glassmorphism mouse-follow, reveal-on-hover image, particle background (Canvas), React Three Fiber basics, R3F scroll-linked camera
