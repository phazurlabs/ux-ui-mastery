# Micro-Interaction Recipes

35 recipes for the small responses that make an interface feel alive: button
presses, toggles, hovers, focus, drag affordances, and state confirmations.


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
