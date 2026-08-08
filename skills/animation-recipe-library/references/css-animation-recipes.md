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
