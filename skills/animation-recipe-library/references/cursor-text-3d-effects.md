# Cursor, Text Animation & 3D Effect Recipes

20 production-ready "wow factor" recipes for React/Next.js. These are the effects that separate an Awwwards-level site from a generic one. Every recipe includes TypeScript, `prefers-reduced-motion` handling, and accessibility notes.

---

## Cursor Effects

### Recipe 1: Custom Cursor Follower (GSAP)

**What it does:** Replaces the default cursor with a custom dot + ring that smoothly follows the mouse using GSAP's `quickTo` for buttery 60fps tracking.

**When to use:** Portfolio sites, agency pages, creative projects.

**Dependencies:** `npm install gsap @gsap/react`

```tsx
"use client";
import { useRef, useEffect, createContext, useContext, useState, useCallback } from "react";
import { gsap } from "gsap";

type CursorVariant = "default" | "text" | "link" | "media" | "drag" | "none";

interface CursorContextType {
  setCursorVariant: (variant: CursorVariant) => void;
}

const CursorContext = createContext<CursorContextType>({ setCursorVariant: () => {} });

export function useCursor() {
  return useContext(CursorContext);
}

export function CustomCursorProvider({ children }: { children: React.ReactNode }) {
  const dot = useRef<HTMLDivElement>(null);
  const ring = useRef<HTMLDivElement>(null);
  const [variant, setVariant] = useState<CursorVariant>("default");
  const [isTouch, setIsTouch] = useState(false);

  useEffect(() => {
    // Detect touch device
    const isTouchDevice = "ontouchstart" in window || navigator.maxTouchPoints > 0;
    setIsTouch(isTouchDevice);
    if (isTouchDevice) return;

    const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReduced) return;

    // GSAP quickTo for smooth following (lerp built-in)
    const xDot = gsap.quickTo(dot.current, "x", { duration: 0.15, ease: "power2.out" });
    const yDot = gsap.quickTo(dot.current, "y", { duration: 0.15, ease: "power2.out" });
    const xRing = gsap.quickTo(ring.current, "x", { duration: 0.35, ease: "power2.out" });
    const yRing = gsap.quickTo(ring.current, "y", { duration: 0.35, ease: "power2.out" });

    const handleMouseMove = (e: MouseEvent) => {
      xDot(e.clientX);
      yDot(e.clientY);
      xRing(e.clientX);
      yRing(e.clientY);
    };

    window.addEventListener("mousemove", handleMouseMove);
    document.body.style.cursor = "none";

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      document.body.style.cursor = "";
    };
  }, []);

  const variantStyles: Record<CursorVariant, { dotScale: number; ringScale: number; ringOpacity: number; mixBlend: string }> = {
    default: { dotScale: 1, ringScale: 1, ringOpacity: 1, mixBlend: "difference" },
    text: { dotScale: 3, ringScale: 0, ringOpacity: 0, mixBlend: "difference" },
    link: { dotScale: 1.5, ringScale: 1.5, ringOpacity: 0.5, mixBlend: "difference" },
    media: { dotScale: 4, ringScale: 0, ringOpacity: 0, mixBlend: "normal" },
    drag: { dotScale: 2, ringScale: 2, ringOpacity: 0.3, mixBlend: "difference" },
    none: { dotScale: 0, ringScale: 0, ringOpacity: 0, mixBlend: "difference" },
  };

  useEffect(() => {
    if (isTouch) return;
    const s = variantStyles[variant];
    gsap.to(dot.current, { scale: s.dotScale, duration: 0.3, ease: "back.out(1.7)" });
    gsap.to(ring.current, { scale: s.ringScale, opacity: s.ringOpacity, duration: 0.3 });
    if (dot.current) dot.current.style.mixBlendMode = s.mixBlend;
  }, [variant, isTouch]);

  const setCursorVariant = useCallback((v: CursorVariant) => setVariant(v), []);

  if (isTouch) return <CursorContext.Provider value={{ setCursorVariant }}>{children}</CursorContext.Provider>;

  return (
    <CursorContext.Provider value={{ setCursorVariant }}>
      {children}
      <div
        ref={dot}
        className="pointer-events-none fixed top-0 left-0 z-[9999] -translate-x-1/2 -translate-y-1/2 will-change-transform"
        aria-hidden="true"
      >
        <div className="w-3 h-3 rounded-full bg-white" />
      </div>
      <div
        ref={ring}
        className="pointer-events-none fixed top-0 left-0 z-[9998] -translate-x-1/2 -translate-y-1/2 will-change-transform"
        aria-hidden="true"
      >
        <div className="w-10 h-10 rounded-full border border-white/50" />
      </div>
    </CursorContext.Provider>
  );
}
```

**Usage:**
```tsx
function InteractiveLink({ href, children }: { href: string; children: React.ReactNode }) {
  const { setCursorVariant } = useCursor();
  return (
    <a
      href={href}
      onMouseEnter={() => setCursorVariant("link")}
      onMouseLeave={() => setCursorVariant("default")}
    >
      {children}
    </a>
  );
}
```

**Reduced motion:** Effect is completely skipped — default system cursor is used.

**Accessibility:** `aria-hidden="true"` on cursor elements. Interactive elements remain focusable via keyboard with standard focus rings.

---

### Recipe 2: Magnetic Elements

**What it does:** Elements attract toward the cursor when within a configurable radius, with spring-back on leave.

**When to use:** Buttons, links, navigation items.

```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";

export function Magnetic({
  children,
  strength = 0.35,
  radius = 150,
  className = "",
}: {
  children: React.ReactNode;
  strength?: number;
  radius?: number;
  className?: string;
}) {
  const el = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    if ("ontouchstart" in window) return;

    const node = el.current!;

    const handleMouseMove = (e: MouseEvent) => {
      const rect = node.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dx = e.clientX - cx;
      const dy = e.clientY - cy;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < radius) {
        const pull = (1 - dist / radius) * strength;
        gsap.to(node, { x: dx * pull, y: dy * pull, duration: 0.3, ease: "power2.out" });
      }
    };

    const handleMouseLeave = () => {
      gsap.to(node, { x: 0, y: 0, duration: 0.5, ease: "elastic.out(1, 0.3)" });
    };

    node.addEventListener("mousemove", handleMouseMove);
    node.addEventListener("mouseleave", handleMouseLeave);

    return () => {
      node.removeEventListener("mousemove", handleMouseMove);
      node.removeEventListener("mouseleave", handleMouseLeave);
    };
  }, [strength, radius]);

  return (
    <div ref={el} className={`inline-block will-change-transform ${className}`}>
      {children}
    </div>
  );
}
```

---

### Recipe 3: Cursor Trail

**What it does:** Multiple trailing dots follow the cursor with decreasing size and opacity.

**When to use:** Creative/experimental pages, interactive installations.

```tsx
"use client";
import { useEffect, useRef } from "react";

export function CursorTrail({ count = 12, color = "oklch(0.6 0.2 260)" }: { count?: number; color?: string }) {
  const dots = useRef<HTMLDivElement[]>([]);
  const mouse = useRef({ x: 0, y: 0 });
  const positions = useRef<{ x: number; y: number }[]>(Array.from({ length: count }, () => ({ x: 0, y: 0 })));

  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    if ("ontouchstart" in window) return;

    const handleMouseMove = (e: MouseEvent) => {
      mouse.current = { x: e.clientX, y: e.clientY };
    };
    window.addEventListener("mousemove", handleMouseMove);

    let raf: number;
    const animate = () => {
      positions.current.forEach((pos, i) => {
        const target = i === 0 ? mouse.current : positions.current[i - 1];
        pos.x += (target.x - pos.x) * 0.3;
        pos.y += (target.y - pos.y) * 0.3;
        const dot = dots.current[i];
        if (dot) {
          dot.style.transform = `translate(${pos.x}px, ${pos.y}px) translate(-50%, -50%)`;
        }
      });
      raf = requestAnimationFrame(animate);
    };
    raf = requestAnimationFrame(animate);

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      cancelAnimationFrame(raf);
    };
  }, [count]);

  return (
    <>
      {Array.from({ length: count }, (_, i) => (
        <div
          key={i}
          ref={(el) => { if (el) dots.current[i] = el; }}
          className="pointer-events-none fixed top-0 left-0 z-[9999] rounded-full will-change-transform"
          style={{
            width: `${Math.max(4, 16 - i * 1.2)}px`,
            height: `${Math.max(4, 16 - i * 1.2)}px`,
            backgroundColor: color,
            opacity: 1 - i * (0.8 / count),
          }}
          aria-hidden="true"
        />
      ))}
    </>
  );
}
```

---

### Recipe 4: Spotlight / Flashlight Effect

**What it does:** Dark overlay covers the page. The cursor reveals content beneath through a radial spotlight.

**When to use:** Dramatic reveals, interactive exploration, mystery/gaming.

```tsx
"use client";
import { useRef, useEffect } from "react";

export function SpotlightOverlay({
  size = 200,
  children,
}: {
  size?: number;
  children: React.ReactNode;
}) {
  const overlay = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      if (overlay.current) overlay.current.style.display = "none";
      return;
    }

    const handleMouseMove = (e: MouseEvent) => {
      if (!overlay.current) return;
      overlay.current.style.setProperty("--mx", `${e.clientX}px`);
      overlay.current.style.setProperty("--my", `${e.clientY}px`);
    };

    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, [size]);

  return (
    <div className="relative">
      {children}
      <div
        ref={overlay}
        className="pointer-events-none fixed inset-0 z-50"
        style={{
          background: `radial-gradient(circle ${size}px at var(--mx, 50%) var(--my, 50%), transparent 0%, rgba(0,0,0,0.85) 100%)`,
        }}
        aria-hidden="true"
      />
    </div>
  );
}
```

---

## Text Animations

### Recipe 5: CSS-Only Text Reveal (animation-timeline: view())

**What it does:** Pure CSS scroll-driven text reveal — no JavaScript required.

**When to use:** Body text, quotes, progressive disclosure.

```html
<p class="scroll-reveal-text">
  This text reveals as you scroll it into view.
  Each word becomes visible progressively.
</p>
```

```css
.scroll-reveal-text {
  font-size: 2rem;
  line-height: 1.4;
  background: linear-gradient(to right, oklch(0.2 0 0) 50%, oklch(0.75 0 0) 50%);
  background-size: 200% 100%;
  background-position: 100% 0;
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  animation: text-reveal linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 50%;
}

@keyframes text-reveal {
  to {
    background-position: 0 0;
  }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  .scroll-reveal-text {
    background: linear-gradient(to right, oklch(0.95 0 0) 50%, oklch(0.4 0 0) 50%);
    background-size: 200% 100%;
    background-position: 100% 0;
    background-clip: text;
    -webkit-background-clip: text;
  }
}

/* Reduced motion: show immediately */
@media (prefers-reduced-motion: reduce) {
  .scroll-reveal-text {
    animation: none;
    background-position: 0 0;
  }
}
```

**Browser support:** Chrome 115+, Safari 18+, Firefox 132+. Fallback: text is fully visible (just no animation).

---

### Recipe 6: Framer Motion Character Stagger

**What it does:** Splits text into characters and animates each with configurable variants — fade, slide, scale, rotate.

**When to use:** Headlines, hero text, emphasis text.

**Dependencies:** `npm install framer-motion`

```tsx
"use client";
import { motion, type Variants } from "framer-motion";

type AnimationVariant = "fade" | "slide" | "scale" | "rotate";

const charVariants: Record<AnimationVariant, Variants> = {
  fade: {
    hidden: { opacity: 0 },
    visible: { opacity: 1 },
  },
  slide: {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0 },
  },
  scale: {
    hidden: { opacity: 0, scale: 0.5 },
    visible: { opacity: 1, scale: 1 },
  },
  rotate: {
    hidden: { opacity: 0, rotateX: -90 },
    visible: { opacity: 1, rotateX: 0 },
  },
};

export function CharStagger({
  text,
  variant = "slide",
  staggerDelay = 0.03,
  className = "",
}: {
  text: string;
  variant?: AnimationVariant;
  staggerDelay?: number;
  className?: string;
}) {
  const chars = text.split("");

  return (
    <motion.span
      className={`inline-block ${className}`}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: "-10%" }}
      transition={{ staggerChildren: staggerDelay }}
      aria-label={text}
    >
      {chars.map((char, i) => (
        <motion.span
          key={i}
          className="inline-block motion-reduce:!opacity-100 motion-reduce:!transform-none"
          variants={charVariants[variant]}
          transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
          aria-hidden="true"
        >
          {char === " " ? "\u00A0" : char}
        </motion.span>
      ))}
    </motion.span>
  );
}
```

**Usage:**
```tsx
<h1 className="text-6xl font-bold">
  <CharStagger text="Build something" variant="slide" />
  <br />
  <CharStagger text="incredible." variant="scale" staggerDelay={0.05} />
</h1>
```

**Accessibility:** `aria-label` on the container provides the full text to screen readers. Individual chars are `aria-hidden`.

---

### Recipe 7: Typewriter Effect

**What it does:** Characters appear one by one with a blinking cursor. Supports multiple strings with delete-and-retype.

**When to use:** Hero sections, terminal-style UI, chatbot introductions.

```tsx
"use client";
import { useState, useEffect, useCallback, useRef } from "react";

export function Typewriter({
  strings,
  typingSpeed = 50,
  deletingSpeed = 30,
  pauseDelay = 2000,
  loop = true,
  className = "",
}: {
  strings: string[];
  typingSpeed?: number;
  deletingSpeed?: number;
  pauseDelay?: number;
  loop?: boolean;
  className?: string;
}) {
  const [display, setDisplay] = useState("");
  const [isDeleting, setIsDeleting] = useState(false);
  const [stringIndex, setStringIndex] = useState(0);
  const fullText = useRef(strings[0]);

  useEffect(() => {
    const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReduced) {
      setDisplay(strings[0]);
      return;
    }

    fullText.current = strings[stringIndex];

    const timeout = setTimeout(
      () => {
        if (!isDeleting) {
          setDisplay((prev) => fullText.current.slice(0, prev.length + 1));
          if (display === fullText.current) {
            if (!loop && stringIndex === strings.length - 1) return;
            setTimeout(() => setIsDeleting(true), pauseDelay);
          }
        } else {
          setDisplay((prev) => prev.slice(0, -1));
          if (display === "") {
            setIsDeleting(false);
            setStringIndex((prev) => (prev + 1) % strings.length);
          }
        }
      },
      isDeleting ? deletingSpeed : typingSpeed
    );

    return () => clearTimeout(timeout);
  }, [display, isDeleting, stringIndex, strings, typingSpeed, deletingSpeed, pauseDelay, loop]);

  return (
    <span className={className} aria-label={strings.join(", ")} role="text">
      <span aria-hidden="true">{display}</span>
      <span
        className="inline-block w-[2px] h-[1em] bg-current ml-0.5 animate-[blink_1s_step-end_infinite] motion-reduce:animate-none"
        aria-hidden="true"
      />
      <style>{`@keyframes blink { 50% { opacity: 0; } }`}</style>
    </span>
  );
}
```

**Usage:**
```tsx
<h1 className="text-5xl font-bold">
  We build{" "}
  <Typewriter
    strings={["websites", "apps", "experiences", "the future"]}
    className="text-blue-500"
  />
</h1>
```

---

### Recipe 8: Gradient Text Animation

**What it does:** Animated gradient that flows across text using `background-clip: text`.

**When to use:** Hero headlines, CTAs, accent text.

```tsx
"use client";

export function GradientText({
  text,
  gradient = "from-blue-500 via-purple-500 to-pink-500",
  animate = true,
  className = "",
}: {
  text: string;
  gradient?: string;
  animate?: boolean;
  className?: string;
}) {
  return (
    <span
      className={`
        bg-gradient-to-r ${gradient}
        bg-clip-text text-transparent
        ${animate ? "bg-[length:200%_auto] motion-safe:animate-[gradient-shift_3s_ease-in-out_infinite]" : ""}
        ${className}
      `}
    >
      {text}
      {animate && (
        <style>{`
          @keyframes gradient-shift {
            0%, 100% { background-position: 0% center; }
            50% { background-position: 100% center; }
          }
        `}</style>
      )}
    </span>
  );
}
```

**Dark mode:** Gradients work on both light and dark backgrounds. For dark mode, use lighter gradient stops:
```tsx
<GradientText
  text="Hello"
  gradient="from-blue-400 via-purple-400 to-pink-400 dark:from-blue-300 dark:via-purple-300 dark:to-pink-300"
/>
```

---

### Recipe 9: Rotating Text (Word Carousel)

**What it does:** Words rotate through a single position with configurable animations — slide up, fade, flip.

**When to use:** Hero sections with multiple value propositions, taglines.

**Dependencies:** `npm install framer-motion`

```tsx
"use client";
import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

type Transition = "slide" | "fade" | "flip";

const transitions: Record<Transition, { initial: object; animate: object; exit: object }> = {
  slide: {
    initial: { y: "100%", opacity: 0 },
    animate: { y: 0, opacity: 1 },
    exit: { y: "-100%", opacity: 0 },
  },
  fade: {
    initial: { opacity: 0, filter: "blur(8px)" },
    animate: { opacity: 1, filter: "blur(0px)" },
    exit: { opacity: 0, filter: "blur(8px)" },
  },
  flip: {
    initial: { rotateX: 90, opacity: 0 },
    animate: { rotateX: 0, opacity: 1 },
    exit: { rotateX: -90, opacity: 0 },
  },
};

export function RotatingText({
  words,
  interval = 2500,
  transition = "slide",
  className = "",
}: {
  words: string[];
  interval?: number;
  transition?: Transition;
  className?: string;
}) {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setIndex((prev) => (prev + 1) % words.length);
    }, interval);
    return () => clearInterval(timer);
  }, [words.length, interval]);

  const t = transitions[transition];

  return (
    <span className={`inline-block overflow-hidden relative ${className}`} style={{ height: "1.2em" }}>
      <AnimatePresence mode="wait">
        <motion.span
          key={words[index]}
          className="inline-block motion-reduce:!opacity-100 motion-reduce:!transform-none"
          initial={t.initial}
          animate={t.animate}
          exit={t.exit}
          transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
        >
          {words[index]}
        </motion.span>
      </AnimatePresence>
      <span className="sr-only">{words.join(", ")}</span>
    </span>
  );
}
```

**Usage:**
```tsx
<h1 className="text-5xl font-bold">
  The platform for{" "}
  <RotatingText
    words={["developers", "designers", "creators", "teams"]}
    transition="slide"
    className="text-blue-500"
  />
</h1>
```

---

## 3D Effects

### Recipe 10: 3D Card Tilt (Mouse-Tracking)

**What it does:** Card tilts toward the cursor position with a glare/shine overlay, creating a premium 3D hover effect.

**When to use:** Product cards, testimonials, feature highlights.

```tsx
"use client";
import { useRef, useState } from "react";

export function TiltCard({
  children,
  maxTilt = 15,
  glare = true,
  className = "",
}: {
  children: React.ReactNode;
  maxTilt?: number;
  glare?: boolean;
  className?: string;
}) {
  const card = useRef<HTMLDivElement>(null);
  const [style, setStyle] = useState({ transform: "", glarePos: "50% 50%" });

  const handleMouseMove = (e: React.MouseEvent) => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const rect = card.current!.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width;
    const y = (e.clientY - rect.top) / rect.height;
    const tiltX = (0.5 - y) * maxTilt;
    const tiltY = (x - 0.5) * maxTilt;

    setStyle({
      transform: `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(1.02, 1.02, 1.02)`,
      glarePos: `${x * 100}% ${y * 100}%`,
    });
  };

  const handleMouseLeave = () => {
    setStyle({ transform: "", glarePos: "50% 50%" });
  };

  return (
    <div
      ref={card}
      className={`relative overflow-hidden transition-transform duration-300 ease-out motion-reduce:!transform-none ${className}`}
      style={{ transform: style.transform, transformStyle: "preserve-3d" }}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
    >
      {children}
      {glare && (
        <div
          className="pointer-events-none absolute inset-0 opacity-0 transition-opacity duration-300 group-hover:opacity-100"
          style={{
            background: `radial-gradient(circle at ${style.glarePos}, rgba(255,255,255,0.15) 0%, transparent 60%)`,
            opacity: style.transform ? 1 : 0,
          }}
          aria-hidden="true"
        />
      )}
    </div>
  );
}
```

---

### Recipe 11: 3D Card Flip

**What it does:** Card with front and back faces, flips on click or hover.

**When to use:** Pricing plans (features on back), team bios, interactive cards.

```tsx
"use client";
import { useState } from "react";

export function FlipCard({
  front,
  back,
  trigger = "click",
  className = "",
}: {
  front: React.ReactNode;
  back: React.ReactNode;
  trigger?: "click" | "hover";
  className?: string;
}) {
  const [flipped, setFlipped] = useState(false);

  const handlers = trigger === "click"
    ? { onClick: () => setFlipped(!flipped) }
    : { onMouseEnter: () => setFlipped(true), onMouseLeave: () => setFlipped(false) };

  return (
    <div
      className={`relative ${className}`}
      style={{ perspective: "1200px" }}
      {...handlers}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => { if (e.key === "Enter" || e.key === " ") setFlipped(!flipped); }}
      aria-label={flipped ? "Showing back of card. Press to flip." : "Showing front of card. Press to flip."}
    >
      <div
        className="relative w-full h-full motion-safe:transition-transform motion-safe:duration-500 motion-reduce:transition-none"
        style={{
          transformStyle: "preserve-3d",
          transform: flipped ? "rotateY(180deg)" : "rotateY(0deg)",
        }}
      >
        {/* Front */}
        <div className="absolute inset-0" style={{ backfaceVisibility: "hidden" }}>
          {front}
        </div>
        {/* Back */}
        <div
          className="absolute inset-0"
          style={{ backfaceVisibility: "hidden", transform: "rotateY(180deg)" }}
        >
          {back}
        </div>
      </div>
    </div>
  );
}
```

---

### Recipe 12: Floating Elements

**What it does:** Elements float with gentle, organic animation at different speeds and amplitudes.

**When to use:** Background decoration, hero sections, ambient effects.

```tsx
"use client";

export function FloatingElement({
  children,
  duration = 6,
  distance = 20,
  delay = 0,
  className = "",
}: {
  children: React.ReactNode;
  duration?: number;
  distance?: number;
  delay?: number;
  className?: string;
}) {
  const animationStyle = {
    animation: `float-${distance} ${duration}s ease-in-out ${delay}s infinite`,
  };

  return (
    <>
      <div
        className={`motion-safe:will-change-transform motion-reduce:!animate-none ${className}`}
        style={animationStyle}
      >
        {children}
      </div>
      <style>{`
        @keyframes float-${distance} {
          0%, 100% { transform: translateY(0px) rotate(0deg); }
          25% { transform: translateY(-${distance}px) rotate(1deg); }
          50% { transform: translateY(-${distance * 0.5}px) rotate(-1deg); }
          75% { transform: translateY(-${distance * 0.8}px) rotate(0.5deg); }
        }
      `}</style>
    </>
  );
}
```

**Usage:**
```tsx
<div className="relative h-screen">
  <FloatingElement duration={8} distance={30} className="absolute top-20 left-10">
    <div className="w-16 h-16 rounded-full bg-blue-200/50" />
  </FloatingElement>
  <FloatingElement duration={6} distance={20} delay={1} className="absolute top-40 right-20">
    <div className="w-12 h-12 rounded-xl bg-purple-200/50" />
  </FloatingElement>
  <FloatingElement duration={10} distance={15} delay={2} className="absolute bottom-20 left-1/3">
    <div className="w-20 h-20 rounded-full bg-pink-200/50" />
  </FloatingElement>
</div>
```

---

### Recipe 13: Noise/Grain SVG Overlay

**What it does:** Adds a subtle film grain texture using an animated SVG filter.

**When to use:** Creative portfolios, editorial sites, vintage aesthetics.

```tsx
"use client";

export function GrainOverlay({
  opacity = 0.05,
  animate = true,
}: {
  opacity?: number;
  animate?: boolean;
}) {
  return (
    <div
      className="pointer-events-none fixed inset-0 z-[100] motion-reduce:hidden"
      style={{ opacity }}
      aria-hidden="true"
    >
      <svg className="w-full h-full">
        <filter id="grain-filter">
          <feTurbulence
            type="fractalNoise"
            baseFrequency="0.65"
            numOctaves="3"
            stitchTiles="stitch"
          >
            {animate && (
              <animate
                attributeName="seed"
                from="0"
                to="100"
                dur="1s"
                repeatCount="indefinite"
              />
            )}
          </feTurbulence>
          <feColorMatrix type="saturate" values="0" />
        </filter>
        <rect width="100%" height="100%" filter="url(#grain-filter)" />
      </svg>
    </div>
  );
}
```

**Performance:** The SVG filter runs on the GPU. The `animate` element cycles the `seed` attribute for subtle movement. Set `animate={false}` for a static grain (better for low-power devices).

---

### Recipe 14: Glassmorphism Mouse-Follow

**What it does:** A glass card with a light refraction effect that follows the cursor position.

**When to use:** Feature cards, CTAs, premium UI elements.

```tsx
"use client";
import { useRef, useState } from "react";

export function GlassCard({
  children,
  className = "",
}: {
  children: React.ReactNode;
  className?: string;
}) {
  const card = useRef<HTMLDivElement>(null);
  const [mousePos, setMousePos] = useState({ x: 50, y: 50 });

  const handleMouseMove = (e: React.MouseEvent) => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const rect = card.current!.getBoundingClientRect();
    setMousePos({
      x: ((e.clientX - rect.left) / rect.width) * 100,
      y: ((e.clientY - rect.top) / rect.height) * 100,
    });
  };

  return (
    <div
      ref={card}
      className={`
        relative overflow-hidden rounded-2xl
        bg-white/10 dark:bg-white/5
        backdrop-blur-xl
        border border-white/20 dark:border-white/10
        ${className}
      `}
      onMouseMove={handleMouseMove}
    >
      {children}
      {/* Light refraction gradient follows cursor */}
      <div
        className="pointer-events-none absolute inset-0 motion-reduce:hidden"
        style={{
          background: `radial-gradient(circle at ${mousePos.x}% ${mousePos.y}%, rgba(255,255,255,0.15) 0%, transparent 50%)`,
        }}
        aria-hidden="true"
      />
      {/* Border light effect */}
      <div
        className="pointer-events-none absolute inset-0 rounded-2xl motion-reduce:hidden"
        style={{
          background: `radial-gradient(circle at ${mousePos.x}% ${mousePos.y}%, rgba(255,255,255,0.3) 0%, transparent 40%)`,
          mask: "linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0)",
          maskComposite: "xor",
          WebkitMaskComposite: "xor",
          padding: "1px",
          borderRadius: "inherit",
        }}
        aria-hidden="true"
      />
    </div>
  );
}
```

---

### Recipe 15: Reveal-on-Hover Image

**What it does:** Image hidden behind a colored overlay, revealed with a directional clip-path on hover.

**When to use:** Portfolio grids, team photos, image galleries.

```tsx
"use client";
import { useState } from "react";

type RevealDirection = "left" | "right" | "top" | "bottom" | "center";

const clipPaths: Record<RevealDirection, { hidden: string; visible: string }> = {
  left: { hidden: "inset(0 100% 0 0)", visible: "inset(0 0 0 0)" },
  right: { hidden: "inset(0 0 0 100%)", visible: "inset(0 0 0 0)" },
  top: { hidden: "inset(0 0 100% 0)", visible: "inset(0 0 0 0)" },
  bottom: { hidden: "inset(100% 0 0 0)", visible: "inset(0 0 0 0)" },
  center: { hidden: "circle(0% at 50% 50%)", visible: "circle(75% at 50% 50%)" },
};

export function HoverRevealImage({
  src,
  alt,
  direction = "left",
  overlayColor = "oklch(0.2 0 0)",
  className = "",
}: {
  src: string;
  alt: string;
  direction?: RevealDirection;
  overlayColor?: string;
  className?: string;
}) {
  const [hovered, setHovered] = useState(false);
  const clip = clipPaths[direction];

  return (
    <div
      className={`relative overflow-hidden cursor-pointer ${className}`}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
    >
      {/* Color overlay (visible by default) */}
      <div
        className="absolute inset-0 z-10 motion-safe:transition-[clip-path] motion-safe:duration-500 motion-safe:ease-[cubic-bezier(0.16,1,0.3,1)]"
        style={{
          backgroundColor: overlayColor,
          clipPath: hovered ? clip.hidden : "inset(0 0 0 0)",
        }}
      />
      {/* Image (revealed on hover) */}
      <img
        src={src}
        alt={alt}
        className="w-full h-full object-cover motion-safe:transition-transform motion-safe:duration-700 motion-safe:ease-out"
        style={{ transform: hovered ? "scale(1.05)" : "scale(1)" }}
        loading="lazy"
      />
    </div>
  );
}
```

---

### Recipe 16: Particle Background (Canvas)

**What it does:** Canvas-based particle system with connecting lines and mouse interaction.

**When to use:** Hero backgrounds, ambient decoration, tech-themed pages.

```tsx
"use client";
import { useRef, useEffect } from "react";

interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  size: number;
}

export function ParticleBackground({
  count = 60,
  color = "150, 150, 150",
  connectionDistance = 120,
  mouseRadius = 150,
  className = "",
}: {
  count?: number;
  color?: string;
  connectionDistance?: number;
  mouseRadius?: number;
  className?: string;
}) {
  const canvas = useRef<HTMLCanvasElement>(null);
  const mouse = useRef({ x: -1000, y: -1000 });

  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    const cvs = canvas.current!;
    const ctx = cvs.getContext("2d")!;
    let raf: number;

    const resize = () => {
      cvs.width = cvs.offsetWidth * devicePixelRatio;
      cvs.height = cvs.offsetHeight * devicePixelRatio;
      ctx.scale(devicePixelRatio, devicePixelRatio);
    };
    resize();
    window.addEventListener("resize", resize);

    const w = () => cvs.offsetWidth;
    const h = () => cvs.offsetHeight;

    const particles: Particle[] = Array.from({ length: count }, () => ({
      x: Math.random() * w(),
      y: Math.random() * h(),
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      size: Math.random() * 2 + 1,
    }));

    const handleMouseMove = (e: MouseEvent) => {
      const rect = cvs.getBoundingClientRect();
      mouse.current = { x: e.clientX - rect.left, y: e.clientY - rect.top };
    };
    cvs.addEventListener("mousemove", handleMouseMove);

    const animate = () => {
      ctx.clearRect(0, 0, w(), h());

      particles.forEach((p) => {
        // Mouse repulsion
        const dx = p.x - mouse.current.x;
        const dy = p.y - mouse.current.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouseRadius) {
          const force = (mouseRadius - dist) / mouseRadius;
          p.vx += (dx / dist) * force * 0.5;
          p.vy += (dy / dist) * force * 0.5;
        }

        // Apply velocity with damping
        p.x += p.vx;
        p.y += p.vy;
        p.vx *= 0.99;
        p.vy *= 0.99;

        // Wrap edges
        if (p.x < 0) p.x = w();
        if (p.x > w()) p.x = 0;
        if (p.y < 0) p.y = h();
        if (p.y > h()) p.y = 0;

        // Draw particle
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${color}, 0.6)`;
        ctx.fill();
      });

      // Draw connections
      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const dx = particles[i].x - particles[j].x;
          const dy = particles[i].y - particles[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < connectionDistance) {
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.strokeStyle = `rgba(${color}, ${0.2 * (1 - dist / connectionDistance)})`;
            ctx.lineWidth = 0.5;
            ctx.stroke();
          }
        }
      }

      raf = requestAnimationFrame(animate);
    };
    raf = requestAnimationFrame(animate);

    return () => {
      cancelAnimationFrame(raf);
      window.removeEventListener("resize", resize);
      cvs.removeEventListener("mousemove", handleMouseMove);
    };
  }, [count, color, connectionDistance, mouseRadius]);

  return (
    <canvas
      ref={canvas}
      className={`w-full h-full ${className}`}
      aria-hidden="true"
    />
  );
}
```

**Reduced motion:** Canvas is completely empty — no animation loop runs. Use a static decorative element as alternative.

---

## React Three Fiber (3D)

### Recipe 17: R3F Basics — Canvas + Mesh + useFrame

**What it does:** Basic React Three Fiber scene with an animated mesh, lighting, and orbit controls.

**When to use:** 3D hero elements, product configurators, interactive backgrounds.

**Dependencies:** `npm install @react-three/fiber @react-three/drei three`

```tsx
"use client";
import { useRef, Suspense } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls, Environment } from "@react-three/drei";
import type { Mesh } from "three";

function AnimatedMesh() {
  const mesh = useRef<Mesh>(null);

  useFrame((state, delta) => {
    if (!mesh.current) return;
    mesh.current.rotation.x += delta * 0.2;
    mesh.current.rotation.y += delta * 0.3;
    mesh.current.position.y = Math.sin(state.clock.elapsedTime) * 0.3;
  });

  return (
    <mesh ref={mesh}>
      <torusKnotGeometry args={[1, 0.3, 128, 32]} />
      <meshStandardMaterial
        color="oklch(0.6 0.2 260)"
        roughness={0.2}
        metalness={0.8}
      />
    </mesh>
  );
}

export function ThreeScene({ className = "" }: { className?: string }) {
  const prefersReduced = typeof window !== "undefined" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (prefersReduced) {
    return (
      <div className={`bg-gray-100 dark:bg-gray-900 rounded-2xl flex items-center justify-center ${className}`}>
        <div className="w-32 h-32 rounded-full bg-gradient-to-br from-blue-500 to-purple-500" />
      </div>
    );
  }

  return (
    <div className={className}>
      <Canvas
        camera={{ position: [0, 0, 5], fov: 45 }}
        dpr={[1, 2]}
        gl={{ antialias: true }}
      >
        <Suspense fallback={null}>
          <ambientLight intensity={0.5} />
          <directionalLight position={[5, 5, 5]} intensity={1} />
          <AnimatedMesh />
          <OrbitControls enableZoom={false} autoRotate autoRotateSpeed={0.5} />
          <Environment preset="city" />
        </Suspense>
      </Canvas>
    </div>
  );
}
```

**Accessibility:** 3D canvas is decorative — not interactive content. If used as a product viewer, add ARIA labels and keyboard controls.

---

### Recipe 18: R3F Scroll-Linked Scene

**What it does:** 3D scene responds to scroll position — objects move, rotate, and transform as the user scrolls.

**When to use:** Landing page hero with 3D elements, product reveal sequences.

**Dependencies:** `npm install @react-three/fiber @react-three/drei three`

```tsx
"use client";
import { useRef, Suspense } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { ScrollControls, useScroll, Html, Float } from "@react-three/drei";
import type { Group } from "three";

function ScrollScene() {
  const group = useRef<Group>(null);
  const scroll = useScroll();

  useFrame(() => {
    if (!group.current) return;
    const offset = scroll.offset; // 0 to 1

    group.current.rotation.y = offset * Math.PI * 2;
    group.current.position.y = Math.sin(offset * Math.PI) * 2;
    group.current.scale.setScalar(1 + offset * 0.5);
  });

  return (
    <group ref={group}>
      <Float speed={2} rotationIntensity={0.5} floatIntensity={0.5}>
        <mesh>
          <icosahedronGeometry args={[1, 1]} />
          <meshStandardMaterial
            color="oklch(0.55 0.2 260)"
            wireframe
          />
        </mesh>
      </Float>

      {/* HTML overlay inside 3D space */}
      <Html position={[2.5, 0, 0]} center>
        <div className="bg-white/90 dark:bg-gray-900/90 backdrop-blur-sm p-6 rounded-xl shadow-xl w-64">
          <h3 className="text-lg font-bold mb-2">Scroll to explore</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            The 3D object responds to your scroll position.
          </p>
        </div>
      </Html>
    </group>
  );
}

export function ScrollLinked3D({ className = "" }: { className?: string }) {
  const prefersReduced = typeof window !== "undefined" &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (prefersReduced) {
    return (
      <div className={`bg-gray-100 dark:bg-gray-900 ${className}`}>
        <div className="h-screen flex items-center justify-center">
          <p className="text-xl">3D content (reduced motion mode)</p>
        </div>
      </div>
    );
  }

  return (
    <div className={`h-screen ${className}`}>
      <Canvas camera={{ position: [0, 0, 6], fov: 45 }} dpr={[1, 2]}>
        <Suspense fallback={null}>
          <ambientLight intensity={0.5} />
          <directionalLight position={[5, 5, 5]} intensity={1} />
          <ScrollControls pages={3} damping={0.25}>
            <ScrollScene />
          </ScrollControls>
        </Suspense>
      </Canvas>
    </div>
  );
}
```

---

## Design Quality Checklist

For every effect in this file, verify:

- [ ] `prefers-reduced-motion: reduce` is respected — effect is disabled or simplified
- [ ] Touch devices are handled — no cursor effects on mobile
- [ ] `aria-hidden="true"` on decorative elements
- [ ] `will-change` is used only during animation, not permanently
- [ ] Dark mode works — colors, gradients, and overlays adapt
- [ ] No layout shift — effects don't move interactive elements
- [ ] SSR safe — no `window` access at module scope
- [ ] Cleanup on unmount — event listeners removed, rAF cancelled
