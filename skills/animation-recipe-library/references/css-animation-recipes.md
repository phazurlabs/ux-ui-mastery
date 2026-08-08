# CSS Animation Recipes — 40+ Complete @keyframes

Production-ready CSS animations. Copy-paste into any project. All recipes include the keyframe definition, a utility class, duration, easing, and usage notes.

---

## Entrance Animations

### 1. Fade In
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.anim-fade-in {
  animation: fadeIn 200ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 2. Fade In Up
```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}
.anim-fade-in-up {
  animation: fadeInUp 250ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 3. Fade In Down
```css
@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-16px); }
  to { opacity: 1; transform: translateY(0); }
}
.anim-fade-in-down {
  animation: fadeInDown 250ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 4. Fade In Left
```css
@keyframes fadeInLeft {
  from { opacity: 0; transform: translateX(-24px); }
  to { opacity: 1; transform: translateX(0); }
}
.anim-fade-in-left {
  animation: fadeInLeft 250ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 5. Fade In Right
```css
@keyframes fadeInRight {
  from { opacity: 0; transform: translateX(24px); }
  to { opacity: 1; transform: translateX(0); }
}
.anim-fade-in-right {
  animation: fadeInRight 250ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 6. Scale In
```css
@keyframes scaleIn {
  from { opacity: 0; transform: scale(0.9); }
  to { opacity: 1; transform: scale(1); }
}
.anim-scale-in {
  animation: scaleIn 200ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
```

### 7. Scale In Bounce
```css
@keyframes scaleInBounce {
  0% { opacity: 0; transform: scale(0.3); }
  50% { opacity: 1; transform: scale(1.08); }
  70% { transform: scale(0.96); }
  100% { transform: scale(1); }
}
.anim-scale-in-bounce {
  animation: scaleInBounce 500ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 8. Slide In From Bottom
```css
@keyframes slideInBottom {
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
}
.anim-slide-in-bottom {
  animation: slideInBottom 300ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 9. Slide In From Top
```css
@keyframes slideInTop {
  from { transform: translateY(-100%); }
  to { transform: translateY(0); }
}
.anim-slide-in-top {
  animation: slideInTop 300ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 10. Slide In From Left
```css
@keyframes slideInLeft {
  from { transform: translateX(-100%); }
  to { transform: translateX(0); }
}
.anim-slide-in-left {
  animation: slideInLeft 300ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 11. Slide In From Right
```css
@keyframes slideInRight {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
.anim-slide-in-right {
  animation: slideInRight 300ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 12. Blur In
```css
@keyframes blurIn {
  from { opacity: 0; filter: blur(12px); }
  to { opacity: 1; filter: blur(0); }
}
.anim-blur-in {
  animation: blurIn 300ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 13. Clip Circle Reveal
```css
@keyframes clipCircleReveal {
  from { clip-path: circle(0% at 50% 50%); }
  to { clip-path: circle(100% at 50% 50%); }
}
.anim-clip-circle {
  animation: clipCircleReveal 400ms cubic-bezier(0.17, 0.84, 0.44, 1) forwards;
}
```

### 14. Clip Inset Reveal
```css
@keyframes clipInsetReveal {
  from { clip-path: inset(0 100% 0 0); }
  to { clip-path: inset(0 0 0 0); }
}
.anim-clip-inset {
  animation: clipInsetReveal 400ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 15. Flip In Y
```css
@keyframes flipInY {
  from { opacity: 0; transform: perspective(800px) rotateY(-90deg); }
  to { opacity: 1; transform: perspective(800px) rotateY(0); }
}
.anim-flip-in-y {
  animation: flipInY 400ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 16. Flip In X
```css
@keyframes flipInX {
  from { opacity: 0; transform: perspective(800px) rotateX(-90deg); }
  to { opacity: 1; transform: perspective(800px) rotateX(0); }
}
.anim-flip-in-x {
  animation: flipInX 400ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 17. Rotate In
```css
@keyframes rotateIn {
  from { opacity: 0; transform: rotate(-180deg) scale(0.5); }
  to { opacity: 1; transform: rotate(0) scale(1); }
}
.anim-rotate-in {
  animation: rotateIn 300ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
```

### 18. Drop In
```css
@keyframes dropIn {
  from { opacity: 0; transform: translateY(-40px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
.anim-drop-in {
  animation: dropIn 350ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
```

### 19. Wipe In Left to Right
```css
@keyframes wipeInLTR {
  from { clip-path: polygon(0 0, 0 0, 0 100%, 0 100%); }
  to { clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); }
}
.anim-wipe-in {
  animation: wipeInLTR 450ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 20. Curtain Open
```css
@keyframes curtainOpen {
  from { clip-path: inset(0 50% 0 50%); }
  to { clip-path: inset(0 0 0 0); }
}
.anim-curtain {
  animation: curtainOpen 500ms cubic-bezier(0.87, 0, 0.13, 1) forwards;
}
```

---

## Exit Animations

### 21. Fade Out
```css
@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}
.anim-fade-out {
  animation: fadeOut 150ms cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards;
}
```

### 22. Fade Out Down
```css
@keyframes fadeOutDown {
  from { opacity: 1; transform: translateY(0); }
  to { opacity: 0; transform: translateY(16px); }
}
.anim-fade-out-down {
  animation: fadeOutDown 200ms cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards;
}
```

### 23. Fade Out Up
```css
@keyframes fadeOutUp {
  from { opacity: 1; transform: translateY(0); }
  to { opacity: 0; transform: translateY(-16px); }
}
.anim-fade-out-up {
  animation: fadeOutUp 200ms cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards;
}
```

### 24. Scale Out
```css
@keyframes scaleOut {
  from { opacity: 1; transform: scale(1); }
  to { opacity: 0; transform: scale(0.9); }
}
.anim-scale-out {
  animation: scaleOut 150ms cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards;
}
```

### 25. Slide Out Right
```css
@keyframes slideOutRight {
  from { transform: translateX(0); opacity: 1; }
  to { transform: translateX(100%); opacity: 0; }
}
.anim-slide-out-right {
  animation: slideOutRight 250ms cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards;
}
```

### 26. Blur Out
```css
@keyframes blurOut {
  from { opacity: 1; filter: blur(0); }
  to { opacity: 0; filter: blur(8px); }
}
.anim-blur-out {
  animation: blurOut 200ms cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards;
}
```

---

## Micro-Interactions

### 27. Shake (Error)
```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-6px); }
  40% { transform: translateX(6px); }
  60% { transform: translateX(-4px); }
  80% { transform: translateX(4px); }
}
.anim-shake {
  animation: shake 400ms cubic-bezier(0.16, 1, 0.3, 1);
}
```

### 28. Wiggle
```css
@keyframes wiggle {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(-5deg); }
  50% { transform: rotate(5deg); }
  75% { transform: rotate(-3deg); }
}
.anim-wiggle {
  animation: wiggle 300ms ease-out;
}
```

### 29. Pulse
```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
.anim-pulse {
  animation: pulse 1500ms cubic-bezier(0.45, 0, 0.55, 1) infinite;
}
```

### 30. Heartbeat
```css
@keyframes heartbeat {
  0%, 100% { transform: scale(1); }
  14% { transform: scale(1.15); }
  28% { transform: scale(1); }
  42% { transform: scale(1.08); }
  56% { transform: scale(1); }
}
.anim-heartbeat {
  animation: heartbeat 1200ms ease-in-out infinite;
}
```

### 31. Bounce
```css
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  40% { transform: translateY(-12px); }
  60% { transform: translateY(-6px); }
}
.anim-bounce {
  animation: bounce 600ms cubic-bezier(0.16, 1, 0.3, 1);
}
```

### 32. Ripple
```css
@keyframes ripple {
  from { transform: scale(0); opacity: 0.5; }
  to { transform: scale(4); opacity: 0; }
}
.anim-ripple {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  animation: ripple 400ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
```

### 33. Checkmark Draw
```css
@keyframes checkDraw {
  from { stroke-dashoffset: 24; }
  to { stroke-dashoffset: 0; }
}
.anim-check path {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
  animation: checkDraw 250ms cubic-bezier(0.16, 1, 0.3, 1) 100ms forwards;
}
```

---

## Loading Animations

### 34. Spinner
```css
@keyframes spin {
  to { transform: rotate(360deg); }
}
.anim-spinner {
  width: 24px; height: 24px;
  border: 2.5px solid #e2e8f0;
  border-top-color: #3b82f6;
  border-radius: 50%;
  animation: spin 800ms linear infinite;
}
```

### 35. Skeleton Shimmer
```css
@keyframes shimmer {
  from { background-position: -200% 0; }
  to { background-position: 200% 0; }
}
.anim-skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  border-radius: 4px;
  animation: shimmer 1500ms linear infinite;
}
```

### 36. Bouncing Dots
```css
@keyframes dotBounce {
  0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
  40% { transform: scale(1); opacity: 1; }
}
.anim-dots .dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: #3b82f6;
  display: inline-block;
  animation: dotBounce 1200ms ease-in-out infinite;
}
.anim-dots .dot:nth-child(2) { animation-delay: 160ms; }
.anim-dots .dot:nth-child(3) { animation-delay: 320ms; }
```

### 37. Indeterminate Progress Bar
```css
@keyframes indeterminate {
  0% { transform: translateX(-100%) scaleX(0.3); }
  50% { transform: translateX(0%) scaleX(0.5); }
  100% { transform: translateX(100%) scaleX(0.3); }
}
.anim-indeterminate {
  height: 3px;
  background: #3b82f6;
  animation: indeterminate 2000ms cubic-bezier(0.45, 0, 0.55, 1) infinite;
}
```

### 38. Bar Loader
```css
@keyframes barGrow {
  0%, 100% { transform: scaleY(0.4); }
  50% { transform: scaleY(1); }
}
.anim-bars .bar {
  width: 4px; height: 24px;
  background: #3b82f6;
  display: inline-block;
  animation: barGrow 1000ms ease-in-out infinite;
}
.anim-bars .bar:nth-child(2) { animation-delay: 100ms; }
.anim-bars .bar:nth-child(3) { animation-delay: 200ms; }
.anim-bars .bar:nth-child(4) { animation-delay: 300ms; }
```

### 39. Typing Indicator
```css
@keyframes typingDot {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-6px); }
}
.anim-typing .dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: #94a3b8;
  display: inline-block;
  animation: typingDot 1400ms ease-in-out infinite;
}
.anim-typing .dot:nth-child(2) { animation-delay: 200ms; }
.anim-typing .dot:nth-child(3) { animation-delay: 400ms; }
```

### 40. Circular Progress (SVG)
```css
@keyframes circularDash {
  0% { stroke-dashoffset: 280; transform: rotate(0deg); }
  50% { stroke-dashoffset: 75; }
  100% { stroke-dashoffset: 280; transform: rotate(360deg); }
}
.anim-circular circle {
  fill: none;
  stroke: #3b82f6;
  stroke-width: 3;
  stroke-dasharray: 280;
  stroke-linecap: round;
  transform-origin: center;
  animation: circularDash 1400ms linear infinite;
}
```

---

## Page Transitions

### 41. Cross Fade Pages
```css
@keyframes pageFadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
@keyframes pageFadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}
.page-enter { animation: pageFadeIn 300ms cubic-bezier(0.16, 1, 0.3, 1) forwards; }
.page-exit { animation: pageFadeOut 200ms cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards; }
```

### 42. Slide Page Left
```css
@keyframes pageSlideInLeft {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
@keyframes pageSlideOutLeft {
  from { transform: translateX(0); }
  to { transform: translateX(-30%); opacity: 0.5; }
}
.page-slide-enter { animation: pageSlideInLeft 400ms cubic-bezier(0.87, 0, 0.13, 1) forwards; }
.page-slide-exit { animation: pageSlideOutLeft 400ms cubic-bezier(0.87, 0, 0.13, 1) forwards; }
```

### 43. View Transition API Styles
```css
::view-transition-old(root) {
  animation: fadeOut 200ms cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards;
}
::view-transition-new(root) {
  animation: fadeInUp 300ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

/* Shared element transition */
.hero-image { view-transition-name: hero; }
::view-transition-group(hero) {
  animation-duration: 350ms;
  animation-timing-function: cubic-bezier(0.87, 0, 0.13, 1);
}
```

### 44. Zoom Drill-Down
```css
@keyframes zoomDrillIn {
  from { opacity: 0; transform: scale(0.85); }
  to { opacity: 1; transform: scale(1); }
}
@keyframes zoomDrillOut {
  from { opacity: 1; transform: scale(1); }
  to { opacity: 0; transform: scale(1.1); }
}
.drill-enter { animation: zoomDrillIn 350ms cubic-bezier(0.16, 1, 0.3, 1) forwards; }
.drill-exit { animation: zoomDrillOut 250ms cubic-bezier(0.55, 0.055, 0.675, 0.19) forwards; }
```

---

## Utility: Stagger System

```css
/* Apply to parent: data-stagger on children auto-staggers */
[data-stagger] > * {
  opacity: 0;
  animation: fadeInUp 250ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
[data-stagger] > *:nth-child(1) { animation-delay: 0ms; }
[data-stagger] > *:nth-child(2) { animation-delay: 50ms; }
[data-stagger] > *:nth-child(3) { animation-delay: 100ms; }
[data-stagger] > *:nth-child(4) { animation-delay: 150ms; }
[data-stagger] > *:nth-child(5) { animation-delay: 200ms; }
[data-stagger] > *:nth-child(6) { animation-delay: 250ms; }
[data-stagger] > *:nth-child(7) { animation-delay: 300ms; }
[data-stagger] > *:nth-child(8) { animation-delay: 350ms; }
[data-stagger] > *:nth-child(n+9) { animation-delay: 400ms; }
```

## Utility: Reduced Motion Override

```css
@media (prefers-reduced-motion: reduce) {
  [class^="anim-"],
  [data-stagger] > * {
    animation-duration: 0.01ms !important;
    animation-delay: 0ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Utility: Animation Custom Properties

```css
:root {
  --anim-duration-instant: 100ms;
  --anim-duration-fast: 200ms;
  --anim-duration-normal: 300ms;
  --anim-duration-slow: 500ms;
  --anim-ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --anim-ease-in: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  --anim-ease-in-out: cubic-bezier(0.87, 0, 0.13, 1);
  --anim-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

---

## Entrance Animations (25 recipes)


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

---

## Exit Animations (18 recipes)


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

---

## Loading Animations (16 recipes)


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
