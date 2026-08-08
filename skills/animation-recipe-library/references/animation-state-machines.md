# Animation State Machines

Modelling animation as explicit states and transitions, for anything with more
than two visual states.


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
