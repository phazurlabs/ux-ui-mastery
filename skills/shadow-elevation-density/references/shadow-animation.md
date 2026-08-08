# Shadow Animation

Animating elevation: what to transition, what it costs, and the
compositor-friendly alternatives to animating box-shadow directly.


### Hover Lift
The most common elevation change. Card rises from Level 1 to Level 2 on hover.

```css
.card {
  box-shadow: var(--shadow-1);
  transition: box-shadow 200ms cubic-bezier(0.4, 0, 0.2, 1),
              transform 200ms cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover {
  box-shadow: var(--shadow-2);
  transform: translateY(-2px);
}
```

### Press / Active State
Element compresses — drops from current elevation toward surface.

```css
.card:active {
  box-shadow: var(--shadow-1);
  transform: translateY(0px) scale(0.98);
  transition: box-shadow 100ms cubic-bezier(0.4, 0, 0.2, 1),
              transform 100ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

### Drag State
Element lifts dramatically when grabbed, then settles on drop.

```css
.draggable {
  box-shadow: var(--shadow-1);
  transition: box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1),
              transform 300ms cubic-bezier(0.4, 0, 0.2, 1);
}

.draggable.is-dragging {
  box-shadow: var(--shadow-4-drag);
  transform: scale(1.03) rotate(1deg);
  transition: box-shadow 150ms cubic-bezier(0, 0, 0.2, 1),
              transform 150ms cubic-bezier(0, 0, 0.2, 1);
  z-index: 9999;
}

.draggable.is-dropping {
  box-shadow: var(--shadow-1);
  transform: scale(1) rotate(0deg);
  transition: box-shadow 400ms cubic-bezier(0.4, 0, 0.2, 1),
              transform 400ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

### Focus Ring + Shadow
Combine focus-visible with elevation for interactive elements.

```css
.interactive:focus-visible {
  box-shadow:
    var(--shadow-2),
    0 0 0 3px oklch(0.55 0.2 255 / 0.40);
  outline: none;
}
```

### Transition Timing Reference

| State change | Duration | Easing | Notes |
|-------------|----------|--------|-------|
| Rest to hover | 200ms | ease-out (0.4, 0, 0.2, 1) | Standard Material easing |
| Hover to rest | 150ms | ease-in (0.4, 0, 1, 1) | Slightly faster return |
| Rest to active/press | 100ms | ease-out | Immediate feedback |
| Pick up (drag start) | 150ms | decelerate (0, 0, 0.2, 1) | Quick lift |
| Drop (drag end) | 400ms | standard (0.4, 0, 0.2, 1) | Gentle settle |
| Modal enter | 300ms | decelerate | Scale + shadow together |
| Modal exit | 200ms | accelerate (0.4, 0, 1, 1) | Fast dismiss |

---

