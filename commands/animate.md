---
name: animate
description: "Generate production animations — CSS keyframes, Framer Motion, scroll-driven, micro-interactions, with reduced motion fallbacks."
argument-hint: "[element or interaction to animate]"
---

# Animate — Animation Recipe Generator

## Before running

This command needs an element or interaction to animate.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate production-ready animation code for UI interactions, page transitions, loading states, and scroll-driven effects. Output CSS @keyframes with Tailwind classes OR Framer Motion React components, always with reduced motion fallbacks and performance guardrails.

## Generation Protocol

### Step 0: Gather Input

Before generating, collect:

1. **Animation type**: What kind of animation does the user need?
   - **Entrance** — Elements appearing on screen (fade in, slide up, scale in, reveal)
   - **Exit** — Elements leaving the screen (fade out, slide away, collapse, shrink)
   - **Micro-interaction** — Small feedback animations (button press, toggle, checkbox, like)
   - **Page transition** — Navigating between pages/views (crossfade, slide, shared element)
   - **Loading** — Skeleton screens, spinners, progress bars, shimmer effects
   - **Scroll-driven** — Parallax, reveal-on-scroll, progress indicator, sticky transformations
   - **Gesture** — Drag, swipe, pinch, pull-to-refresh responses
   - **Hover** — Hover effects for cards, buttons, links, images
   - **State change** — Expanding/collapsing, accordion, tab switch, modal open/close
   - **Stagger** — Sequential animation of list items, grid cards, menu items

2. **Specific recipe** (optional, more targeted):
   - "button hover effect"
   - "modal entrance and exit"
   - "skeleton loading shimmer"
   - "parallax scroll hero"
   - "card hover lift"
   - "toast notification slide in"
   - "accordion expand/collapse"
   - "page route transition"
   - "list item stagger entrance"
   - "floating action button press"

3. **Tech preference**:
   - **CSS only** (default) — @keyframes + Tailwind utility classes
   - **Framer Motion** — React component with motion primitives
   - **Both** — CSS version + Framer Motion version

4. **Prior Sumi outputs**: Check for `/tokens` (duration scale, easing curves), `/style` or `/taste` (motion personality — minimal, playful, dramatic). Consume if available.

If no animation type is specified, ask. Do not guess.

### Step 1: TIMING AND EASING FUNDAMENTALS

Every animation must use intentional timing. Never use arbitrary values.

**Duration scale** (research-backed):
```css
/* Micro — instant feedback, imperceptible delay */
--duration-instant:  50ms    /* Checkbox tick, toggle snap */
--duration-micro:    100ms   /* Button active state, focus ring */
--duration-fast:     150ms   /* Tooltip show, dropdown open, small hover effects */
--duration-normal:   200ms   /* Most UI transitions (Doherty Threshold sweet spot) */
--duration-moderate: 300ms   /* Modal open, slide transitions, accordion expand */
--duration-slow:     400ms   /* Page transitions, large element movements */
--duration-slower:   500ms   /* Complex entrance animations, orchestrated sequences */
--duration-slowest:  700ms   /* Hero animations, dramatic reveals (use sparingly) */
```

**Duration rules**:
- Feedback animations (hover, press, toggle): 100-200ms
- UI transitions (modal, dropdown, accordion): 200-350ms
- Entrance animations (page load, scroll reveal): 300-500ms
- Exit animations: 20-30% shorter than entrance (feels more responsive)
- Never exceed 700ms for any single animation (users perceive delays > 400ms as sluggish per Doherty Threshold)
- Stagger delay between items: 50-100ms

**Easing curves**:
```css
/* Standard easings */
--ease-in:       cubic-bezier(0.4, 0, 1, 0.2);    /* Accelerate — for exits */
--ease-out:      cubic-bezier(0, 0, 0.2, 1);      /* Decelerate — for entrances */
--ease-in-out:   cubic-bezier(0.4, 0, 0.2, 1);    /* Standard — for state changes */

/* Expressive easings */
--ease-bounce:   cubic-bezier(0.34, 1.56, 0.64, 1);  /* Overshoot — playful, attention-grabbing */
--ease-spring:   cubic-bezier(0.22, 1, 0.36, 1);     /* Spring-like — natural, organic feel */
--ease-snap:     cubic-bezier(0.5, 0, 0, 1);         /* Quick start, gentle land — decisive */

/* Material Design 3 Expressive */
--ease-emphasized:     cubic-bezier(0.2, 0, 0, 1);
--ease-emphasized-acc: cubic-bezier(0.3, 0, 0.8, 0.15);
--ease-emphasized-dec: cubic-bezier(0.05, 0.7, 0.1, 1);
```

**Easing rules**:
- Elements entering the screen: ease-out (decelerate into view)
- Elements leaving the screen: ease-in (accelerate away)
- Elements moving on screen: ease-in-out (smooth state change)
- Playful/delightful interactions: ease-bounce or ease-spring
- Never use `linear` for UI animations (feels mechanical and unnatural)
- Exception: progress bars and loading indicators can use linear

### Step 2: ENTRANCE ANIMATIONS

Elements appearing on screen for the first time.

**Fade in**:
```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.animate-fade-in {
  animation: fadeIn 300ms var(--ease-out) both;
}
```

**Slide up + fade** (most common entrance):
```css
@keyframes slideUpFade {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-slide-up {
  animation: slideUpFade 400ms var(--ease-out) both;
}
```

**Scale in** (modals, popovers):
```css
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
.animate-scale-in {
  animation: scaleIn 200ms var(--ease-out) both;
}
```

**Slide from edge** (sidebars, drawers, sheets):
```css
@keyframes slideInFromRight {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
.animate-slide-in-right {
  animation: slideInFromRight 300ms var(--ease-out) both;
}

@keyframes slideInFromBottom {
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
}
.animate-slide-in-bottom {
  animation: slideInFromBottom 300ms var(--ease-out) both;
}
```

**Framer Motion entrance equivalents**:
```tsx
import { motion } from 'framer-motion';

// Fade in
<motion.div
  initial={{ opacity: 0 }}
  animate={{ opacity: 1 }}
  transition={{ duration: 0.3, ease: [0, 0, 0.2, 1] }}
>
  Content
</motion.div>

// Slide up + fade
<motion.div
  initial={{ opacity: 0, y: 16 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.4, ease: [0, 0, 0.2, 1] }}
>
  Content
</motion.div>

// Scale in (modal)
<motion.div
  initial={{ opacity: 0, scale: 0.95 }}
  animate={{ opacity: 1, scale: 1 }}
  transition={{ duration: 0.2, ease: [0, 0, 0.2, 1] }}
>
  Modal content
</motion.div>
```

### Step 3: EXIT ANIMATIONS

Elements leaving the screen. Exits should be faster than entrances.

**Fade out**:
```css
@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}
.animate-fade-out {
  animation: fadeOut 200ms var(--ease-in) both;
}
```

**Slide down + fade** (dismissal):
```css
@keyframes slideDownFade {
  from {
    opacity: 1;
    transform: translateY(0);
  }
  to {
    opacity: 0;
    transform: translateY(8px);
  }
}
.animate-slide-down-out {
  animation: slideDownFade 200ms var(--ease-in) both;
}
```

**Scale out** (modal close):
```css
@keyframes scaleOut {
  from {
    opacity: 1;
    transform: scale(1);
  }
  to {
    opacity: 0;
    transform: scale(0.95);
  }
}
.animate-scale-out {
  animation: scaleOut 150ms var(--ease-in) both;
}
```

**Framer Motion exit** (with AnimatePresence):
```tsx
import { AnimatePresence, motion } from 'framer-motion';

<AnimatePresence>
  {isVisible && (
    <motion.div
      key="modal"
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.95 }}
      transition={{ duration: 0.2 }}
    >
      Modal content
    </motion.div>
  )}
</AnimatePresence>
```

### Step 4: MICRO-INTERACTIONS

Small feedback animations that make the UI feel alive.

**Button press**:
```css
.btn-press {
  transition: transform 100ms var(--ease-in-out), box-shadow 100ms var(--ease-in-out);
}
.btn-press:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
.btn-press:active {
  transform: translateY(0) scale(0.98);
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
}
```

**Card hover lift**:
```css
.card-hover {
  transition: transform 200ms var(--ease-out), box-shadow 200ms var(--ease-out);
}
.card-hover:hover {
  transform: translateY(-4px);
  box-shadow:
    0 12px 24px -4px rgba(0, 0, 0, 0.08),
    0 4px 8px -2px rgba(0, 0, 0, 0.04);
}
```

**Toggle switch**:
```css
.toggle-track {
  transition: background-color 200ms var(--ease-in-out);
}
.toggle-thumb {
  transition: transform 200ms var(--ease-spring);
}
.toggle-track[aria-checked="true"] .toggle-thumb {
  transform: translateX(20px);
}
```

**Checkbox tick** (SVG path animation):
```css
@keyframes checkmark {
  from {
    stroke-dashoffset: 24;
  }
  to {
    stroke-dashoffset: 0;
  }
}
.checkbox-tick {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
}
.checkbox-checked .checkbox-tick {
  animation: checkmark 200ms var(--ease-out) forwards;
}
```

**Like/heart animation** (scale bounce):
```css
@keyframes heartBounce {
  0% { transform: scale(1); }
  25% { transform: scale(1.3); }
  50% { transform: scale(0.95); }
  100% { transform: scale(1); }
}
.heart-active {
  animation: heartBounce 400ms var(--ease-spring);
  color: #ef4444;
}
```

**Framer Motion micro-interactions**:
```tsx
// Button with press animation
<motion.button
  whileHover={{ y: -1, boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}
  whileTap={{ y: 0, scale: 0.98 }}
  transition={{ duration: 0.1 }}
>
  Click me
</motion.button>

// Like button with spring
<motion.button
  whileTap={{ scale: 0.85 }}
  onClick={() => setLiked(!liked)}
>
  <motion.svg
    animate={liked ? { scale: [1, 1.3, 0.95, 1] } : { scale: 1 }}
    transition={{ duration: 0.4, ease: 'easeOut' }}
  >
    <HeartIcon />
  </motion.svg>
</motion.button>

// Number counter
<motion.span
  key={count}
  initial={{ y: -10, opacity: 0 }}
  animate={{ y: 0, opacity: 1 }}
  exit={{ y: 10, opacity: 0 }}
  transition={{ duration: 0.15 }}
>
  {count}
</motion.span>
```

### Step 5: LOADING ANIMATIONS

Skeleton screens, shimmer effects, spinners, and progress indicators.

**Skeleton shimmer** (placeholder while content loads):
```css
@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}
.skeleton {
  background: linear-gradient(
    90deg,
    #f0f0f0 25%,
    #e0e0e0 37%,
    #f0f0f0 63%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
  border-radius: 4px;
}

/* Dark mode skeleton */
.dark .skeleton {
  background: linear-gradient(
    90deg,
    #1f2937 25%,
    #374151 37%,
    #1f2937 63%
  );
  background-size: 200% 100%;
}
```

**Skeleton component** (React):
```tsx
function Skeleton({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={`animate-pulse rounded-md bg-gray-200 dark:bg-gray-800 ${className}`}
      {...props}
      aria-hidden="true"
    />
  );
}

// Usage: card skeleton
function CardSkeleton() {
  return (
    <div className="rounded-lg border border-gray-200 p-4 dark:border-gray-800" aria-busy="true" aria-label="Loading content">
      <Skeleton className="h-40 w-full rounded-lg" />
      <Skeleton className="mt-4 h-5 w-3/4" />
      <Skeleton className="mt-2 h-4 w-1/2" />
      <div className="mt-4 flex gap-2">
        <Skeleton className="h-8 w-20 rounded-full" />
        <Skeleton className="h-8 w-20 rounded-full" />
      </div>
    </div>
  );
}
```

**Spinner**:
```css
@keyframes spin {
  to { transform: rotate(360deg); }
}
.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid #e5e7eb;
  border-top-color: #6366f1;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}
```

**Spinner component** (accessible):
```tsx
function Spinner({ size = 'md', className }: { size?: 'sm' | 'md' | 'lg'; className?: string }) {
  const sizes = { sm: 'h-4 w-4', md: 'h-5 w-5', lg: 'h-8 w-8' };
  return (
    <svg
      className={`animate-spin ${sizes[size]} ${className}`}
      viewBox="0 0 24 24"
      fill="none"
      aria-hidden="true"
    >
      <circle
        className="opacity-25"
        cx="12" cy="12" r="10"
        stroke="currentColor"
        strokeWidth="4"
      />
      <path
        className="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
      />
    </svg>
  );
}
```

**Progress bar** (determinate):
```tsx
function ProgressBar({ value, max = 100 }: { value: number; max?: number }) {
  const percentage = Math.min(100, Math.max(0, (value / max) * 100));

  return (
    <div
      role="progressbar"
      aria-valuenow={value}
      aria-valuemin={0}
      aria-valuemax={max}
      aria-label={`Progress: ${Math.round(percentage)}%`}
      className="h-2 w-full overflow-hidden rounded-full bg-gray-200 dark:bg-gray-800"
    >
      <div
        className="h-full rounded-full bg-indigo-600 transition-[width] duration-300 ease-out"
        style={{ width: `${percentage}%` }}
      />
    </div>
  );
}
```

**Indeterminate progress bar**:
```css
@keyframes indeterminate {
  0% {
    transform: translateX(-100%);
    width: 40%;
  }
  50% {
    width: 60%;
  }
  100% {
    transform: translateX(250%);
    width: 40%;
  }
}
.progress-indeterminate {
  animation: indeterminate 1.5s cubic-bezier(0.65, 0, 0.35, 1) infinite;
}
```

### Step 6: SCROLL-DRIVEN ANIMATIONS

Animations triggered or controlled by scroll position.

**Reveal on scroll** (Intersection Observer):
```tsx
'use client';

import { useEffect, useRef, useState } from 'react';

function useScrollReveal(options?: IntersectionObserverInit) {
  const ref = useRef<HTMLDivElement>(null);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const element = ref.current;
    if (!element) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          observer.unobserve(element); // Only animate once
        }
      },
      { threshold: 0.1, rootMargin: '0px 0px -50px 0px', ...options }
    );

    observer.observe(element);
    return () => observer.disconnect();
  }, []);

  return { ref, isVisible };
}

// Usage
function RevealSection({ children }: { children: React.ReactNode }) {
  const { ref, isVisible } = useScrollReveal();

  return (
    <div
      ref={ref}
      className={`transition-all duration-500 ease-out ${
        isVisible
          ? 'opacity-100 translate-y-0'
          : 'opacity-0 translate-y-8'
      }`}
    >
      {children}
    </div>
  );
}
```

**Framer Motion scroll reveal** (with useInView):
```tsx
import { motion, useInView } from 'framer-motion';
import { useRef } from 'react';

function ScrollReveal({ children, delay = 0 }: { children: React.ReactNode; delay?: number }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-50px' });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 24 }}
      animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 24 }}
      transition={{ duration: 0.5, delay, ease: [0, 0, 0.2, 1] }}
    >
      {children}
    </motion.div>
  );
}
```

**CSS scroll-driven animations** (Chrome 115+, progressive enhancement):
```css
/* Scroll progress indicator (top of page) */
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(to right, #6366f1, #8b5cf6);
  transform-origin: left;
  animation: scrollProgress linear;
  animation-timeline: scroll();
}

@keyframes scrollProgress {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}

/* Parallax effect */
.parallax-slow {
  animation: parallax linear;
  animation-timeline: scroll();
}

@keyframes parallax {
  from { transform: translateY(0); }
  to { transform: translateY(-100px); }
}
```

**Stagger reveal on scroll** (list items appearing sequentially):
```tsx
// Framer Motion stagger
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.08,
      delayChildren: 0.1,
    },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 16 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.4, ease: [0, 0, 0.2, 1] },
  },
};

function StaggerList({ items }: { items: string[] }) {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-50px' });

  return (
    <motion.ul
      ref={ref}
      variants={containerVariants}
      initial="hidden"
      animate={isInView ? 'visible' : 'hidden'}
      className="space-y-4"
    >
      {items.map((item, index) => (
        <motion.li key={index} variants={itemVariants}>
          {item}
        </motion.li>
      ))}
    </motion.ul>
  );
}
```

**CSS stagger without JS** (using nth-child delays):
```css
.stagger-list > * {
  opacity: 0;
  transform: translateY(16px);
  animation: slideUpFade 400ms var(--ease-out) both;
}
.stagger-list > *:nth-child(1) { animation-delay: 0ms; }
.stagger-list > *:nth-child(2) { animation-delay: 60ms; }
.stagger-list > *:nth-child(3) { animation-delay: 120ms; }
.stagger-list > *:nth-child(4) { animation-delay: 180ms; }
.stagger-list > *:nth-child(5) { animation-delay: 240ms; }
.stagger-list > *:nth-child(6) { animation-delay: 300ms; }
.stagger-list > *:nth-child(7) { animation-delay: 360ms; }
.stagger-list > *:nth-child(8) { animation-delay: 420ms; }
/* Cap at 8 items — beyond this, stagger becomes too slow */
.stagger-list > *:nth-child(n+9) { animation-delay: 480ms; }
```

### Step 7: PAGE TRANSITIONS

Smooth transitions between pages/views.

**Framer Motion page transition** (with Next.js App Router):
```tsx
// app/template.tsx — wraps every page with transition
'use client';

import { motion } from 'framer-motion';

export default function Template({ children }: { children: React.ReactNode }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -8 }}
      transition={{ duration: 0.3, ease: [0, 0, 0.2, 1] }}
    >
      {children}
    </motion.div>
  );
}
```

**View Transitions API** (Chrome 111+, progressive enhancement):
```tsx
// Using the View Transitions API for page navigation
function navigateWithTransition(href: string) {
  if (!document.startViewTransition) {
    // Fallback: regular navigation
    window.location.href = href;
    return;
  }

  document.startViewTransition(() => {
    // Update the DOM (e.g., via router)
    router.push(href);
  });
}
```

```css
/* View transition CSS */
::view-transition-old(root) {
  animation: fadeOut 200ms ease-in both;
}
::view-transition-new(root) {
  animation: fadeIn 300ms ease-out both;
}

/* Shared element transitions */
.hero-image {
  view-transition-name: hero;
}
::view-transition-old(hero),
::view-transition-new(hero) {
  animation-duration: 400ms;
  animation-timing-function: cubic-bezier(0.22, 1, 0.36, 1);
}
```

### Step 8: REDUCED MOTION FALLBACK

Every animation MUST have a reduced motion fallback. This is a non-negotiable accessibility requirement.

**CSS approach** (global reset):
```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

**Targeted CSS approach** (preferred — preserves essential animations):
```css
@media (prefers-reduced-motion: reduce) {
  /* Remove decorative animations */
  .animate-slide-up,
  .animate-fade-in,
  .animate-scale-in {
    animation: none;
    opacity: 1;
    transform: none;
  }

  /* Keep essential state changes, just make them instant */
  .toggle-thumb {
    transition-duration: 0.01ms;
  }

  /* Keep loading indicators but simplify */
  .skeleton {
    animation: none;
    background: #e5e7eb;
  }

  .spinner {
    /* Keep spinner — it communicates loading state */
    animation-duration: 1.5s; /* Slow it down */
  }
}
```

**Framer Motion reduced motion**:
```tsx
import { useReducedMotion } from 'framer-motion';

function AnimatedCard({ children }: { children: React.ReactNode }) {
  const shouldReduceMotion = useReducedMotion();

  return (
    <motion.div
      initial={shouldReduceMotion ? false : { opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={shouldReduceMotion ? { duration: 0 } : { duration: 0.4 }}
    >
      {children}
    </motion.div>
  );
}
```

**React hook for reduced motion**:
```tsx
function usePrefersReducedMotion() {
  const [prefersReduced, setPrefersReduced] = useState(false);

  useEffect(() => {
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReduced(mq.matches);

    const handler = (event: MediaQueryListEvent) => {
      setPrefersReduced(event.matches);
    };
    mq.addEventListener('change', handler);
    return () => mq.removeEventListener('change', handler);
  }, []);

  return prefersReduced;
}
```

**What to do for reduced motion users**:
- Decorative animations (entrance fades, hover lifts, parallax): remove entirely
- State change animations (toggle, accordion): make instant (0ms duration)
- Loading indicators (spinner, progress): keep but slow down
- Error/success feedback: keep (essential for communication)
- Scroll-driven animations: disable (no parallax, no reveal)
- Page transitions: instant cut (no fade/slide)

### Step 9: PERFORMANCE GUIDELINES

Every animation output must include performance notes.

**Transform-only rule**:
- ONLY animate `transform` and `opacity` — these are GPU-composited and do not trigger layout or paint
- NEVER animate: `width`, `height`, `top`, `left`, `margin`, `padding`, `border`, `font-size`, `background-color` (these trigger layout/paint and cause jank)
- Exception: `background-color` and `color` transitions are acceptable for hover states (paint-only, no layout)

**will-change usage**:
```css
/* Apply will-change only to elements that WILL animate */
.will-animate {
  will-change: transform, opacity;
}

/* Remove will-change after animation completes (if one-shot) */
.animation-complete {
  will-change: auto;
}
```

**will-change rules**:
- Apply to elements that will animate within the next 200ms
- Never apply to more than 5 elements at a time (excessive GPU memory)
- Remove after animation completes for one-shot animations
- Never use `will-change: transform` on static elements "just in case"

**Composite layers**:
- Use `transform: translateZ(0)` or `will-change: transform` to promote to own layer
- But limit to 5-10 promoted layers per page (too many = excessive memory)

**Animation frame budget**:
- Target: 16.67ms per frame (60fps)
- Each animation should add < 2ms to frame time
- Test on low-end devices (throttle CPU 4x in DevTools)

**Performance checklist for every animation**:
```
[ ] Uses only transform and/or opacity
[ ] will-change applied only where needed, removed after
[ ] No layout thrashing (no width/height/margin/padding animations)
[ ] Tested with DevTools Performance panel (no dropped frames)
[ ] Works on 4x CPU throttle (low-end device simulation)
[ ] Total animated elements < 20 at any time
```

### Step 10: COMPLETE ANIMATION OUTPUT

Combine the requested animations into a single, complete, copy-paste-ready file.

**CSS output file structure**:
```css
/* ============================================
   Animation Recipes — [Type]
   Generated by Sumi /animate
   ============================================ */

/* 1. Custom Properties (timing, easing) */
/* 2. @keyframes definitions */
/* 3. Animation utility classes */
/* 4. Reduced motion fallbacks */
/* 5. Performance notes (comments) */
```

**Framer Motion output file structure**:
```tsx
// Animation Recipes — [Type]
// Generated by Sumi /animate

// 1. Animation variants (reusable)
// 2. React components with motion
// 3. Custom hooks (useScrollReveal, usePrefersReducedMotion)
// 4. Reduced motion handling
// 5. Usage examples
```

## Output Format

```
## Animation: [Type/Recipe Name]

### Configuration
- **Type**: [entrance / micro-interaction / loading / scroll-driven / etc.]
- **Tech**: [CSS / Framer Motion / Both]
- **Duration**: [timing values used]
- **Easing**: [curves used and why]

### Animation Code

[Complete CSS or React code — copy-paste ready]

### Timing Reference

| Animation | Duration | Easing | When |
|-----------|----------|--------|------|
| [name] | [ms] | [curve name] | [trigger condition] |

### Reduced Motion Fallback

[Code showing what happens when prefers-reduced-motion is enabled]

### Performance Notes
- **Properties animated**: [transform, opacity — or note if paint properties used]
- **will-change**: [where applied, when removed]
- **Layer count**: [how many composite layers created]
- **Frame budget**: [estimated ms per frame for this animation]

### Integration Notes
- **With `/component`**: Apply these animation classes to generated components
- **With `/nav`**: Use entrance animations for mobile menu, exit for closing
- **With `/form`**: Apply micro-interactions to form validation feedback
- **With `/tokens`**: Map duration/easing values to design token system
```

## Quality Gates

The output MUST include:
- [ ] Complete animation code (CSS @keyframes or Framer Motion) — copy-paste ready
- [ ] Explicit duration and easing values with rationale
- [ ] Reduced motion fallback (@media prefers-reduced-motion or useReducedMotion)
- [ ] Performance guardrails (transform-only, will-change guidance)
- [ ] Stagger orchestration for list/grid animations
- [ ] Both entrance and exit animations for elements that appear and disappear

The output MUST NOT include:
- Animations with no reduced motion fallback
- Animations on layout properties (width, height, margin, padding, top, left)
- Durations exceeding 700ms for any single UI animation
- Linear easing on UI transitions (except progress bars)
- will-change applied globally or to static elements
- Animations with no explicit timing values ("use whatever feels right")

## Cross-References

When generating animations, draw knowledge from:
- `animation-recipe-library` skill — 200+ production animation recipes
- `interaction-motion-design` skill — motion principles, haptics, timing theory
- `platform-visual-standards` skill — iOS spring animations, Material motion, CSS best practices
- `performance-states-patterns` skill — loading states, skeleton patterns, transition states
- `accessibility-inclusive-design` skill — prefers-reduced-motion, vestibular disorders, WCAG 2.3.3
- `cognitive-psychology-ux` skill — perceived performance, Doherty Threshold, animation attention

## Next Step

**Next** -> `/screen` — Build full screens using these animations for entrance, transitions, and interactions

**Alternatives**:
- `/form` — Apply micro-interactions to form validation and submission
- `/nav` — Add entrance/exit animations to navigation menus
- `/component` — Animate individual UI components
- `/guide` — See the full journey map
