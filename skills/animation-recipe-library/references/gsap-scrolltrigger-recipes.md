# GSAP + ScrollTrigger Production Recipes

25 complete, copy-paste-ready GSAP recipes for React/Next.js. Every recipe uses the `useGSAP()` hook from `@gsap/react`, includes `prefers-reduced-motion` handling, and is TypeScript-typed.

---

## Recipe 0: GSAP Core Setup + useGSAP Hook

**What it does:** Registers GSAP plugins and establishes the foundational hook pattern used by every recipe in this file.

**When to use:** First step in any GSAP project.

**Dependencies:** `npm install gsap @gsap/react`

```tsx
// lib/gsap.ts — Plugin registration (import once in layout)
"use client";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger, SplitText);

export { gsap, ScrollTrigger, SplitText, useGSAP };
```

```tsx
// components/FadeInSection.tsx — Basic useGSAP pattern
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

export function FadeInSection({ children }: { children: React.ReactNode }) {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      // All GSAP code inside useGSAP is auto-cleaned on unmount
      gsap.from(".fade-item", {
        opacity: 0,
        y: 40,
        stagger: 0.1,
        duration: 0.8,
        ease: "power2.out",
        scrollTrigger: {
          trigger: container.current,
          start: "top 80%",
          toggleActions: "play none none none",
        },
      });
    },
    { scope: container } // Scopes all selectors to this ref
  );

  return (
    <section ref={container}>
      {children}
    </section>
  );
}
```

**Reduced motion:**
```tsx
useGSAP(() => {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (prefersReducedMotion) {
    gsap.set(".fade-item", { opacity: 1, y: 0 }); // Instant, no animation
    return;
  }
  // ... full animation code
}, { scope: container });
```

**TypeScript types:**
```typescript
// GSAP types are built-in. Key types:
import type { GSAPTween, GSAPTimeline } from "gsap";

// ScrollTrigger config type
type ScrollTriggerConfig = ScrollTrigger.Vars;
```

---

## Recipe 1: Lenis Smooth Scroll Integration

**What it does:** Replaces native browser scroll with buttery-smooth inertia scrolling that syncs with GSAP ScrollTrigger.

**When to use:** Portfolio sites, marketing pages, any site where scroll feel matters.

**Dependencies:** `npm install gsap @gsap/react lenis`

```tsx
// providers/SmoothScrollProvider.tsx
"use client";
import { createContext, useContext, useEffect, useRef, useState } from "react";
import Lenis from "lenis";
import { gsap } from "@/lib/gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

interface SmoothScrollContextType {
  lenis: Lenis | null;
}

const SmoothScrollContext = createContext<SmoothScrollContextType>({ lenis: null });

export function useSmoothScroll() {
  return useContext(SmoothScrollContext);
}

export function SmoothScrollProvider({ children }: { children: React.ReactNode }) {
  const [lenis, setLenis] = useState<Lenis | null>(null);
  const reqIdRef = useRef<number>(0);

  useEffect(() => {
    const prefersReducedMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches;

    if (prefersReducedMotion) return; // No smooth scroll for reduced motion

    const lenisInstance = new Lenis({
      duration: 1.2,
      easing: (t: number) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: "vertical",
      smoothWheel: true,
    });

    // Sync Lenis scroll position with GSAP ScrollTrigger
    lenisInstance.on("scroll", ScrollTrigger.update);

    // Use GSAP ticker instead of rAF for frame-perfect sync
    gsap.ticker.add((time) => {
      lenisInstance.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);

    setLenis(lenisInstance);

    return () => {
      lenisInstance.destroy();
      gsap.ticker.remove(lenisInstance.raf);
    };
  }, []);

  return (
    <SmoothScrollContext.Provider value={{ lenis }}>
      {children}
    </SmoothScrollContext.Provider>
  );
}
```

```tsx
// app/layout.tsx — usage
import { SmoothScrollProvider } from "@/providers/SmoothScrollProvider";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <SmoothScrollProvider>{children}</SmoothScrollProvider>
      </body>
    </html>
  );
}
```

**Reduced motion:** Provider checks `prefers-reduced-motion` and skips Lenis entirely — native scroll is used.

---

## Recipe 2: Pin-and-Scrub Section

**What it does:** Pins a section in place while the user scrolls, with content animating in sync with scroll progress.

**When to use:** Feature showcases, step-by-step reveals, storytelling sections.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP, ScrollTrigger } from "@/lib/gsap";

interface Step {
  title: string;
  description: string;
  image: string;
}

export function PinAndScrubSection({ steps }: { steps: Step[] }) {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: container.current,
          start: "top top",
          end: `+=${steps.length * 100}%`,
          pin: true,
          scrub: 1, // 1 second smoothing
          snap: 1 / (steps.length - 1), // Snap to each step
        },
      });

      steps.forEach((_, i) => {
        if (i === 0) return;
        tl.fromTo(
          `.step-${i}`,
          { opacity: 0, y: 60 },
          { opacity: 1, y: 0, duration: 1 },
          i
        );
        if (i > 0) {
          tl.to(`.step-${i - 1}`, { opacity: 0, y: -40, duration: 0.5 }, i);
        }
      });
    },
    { scope: container }
  );

  return (
    <div ref={container} className="relative h-screen overflow-hidden">
      {steps.map((step, i) => (
        <div
          key={i}
          className={`step-${i} absolute inset-0 flex items-center justify-center gap-16 px-8 ${
            i === 0 ? "" : "opacity-0"
          }`}
        >
          <div className="max-w-md">
            <h3 className="text-3xl font-bold mb-4">{step.title}</h3>
            <p className="text-lg text-gray-600 dark:text-gray-400">{step.description}</p>
          </div>
          <img
            src={step.image}
            alt={step.title}
            className="w-96 h-72 object-cover rounded-2xl"
          />
        </div>
      ))}
    </div>
  );
}
```

**Reduced motion:** The `if` check exits early — all steps are visible statically without pinning.

---

## Recipe 3: Horizontal Scroll Gallery

**What it does:** Vertical scrolling translates into horizontal movement — a horizontal image gallery driven by vertical scroll.

**When to use:** Portfolio galleries, product showcases, image-heavy sections.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP, ScrollTrigger } from "@/lib/gsap";

interface GalleryItem {
  src: string;
  alt: string;
  title: string;
}

export function HorizontalScrollGallery({ items }: { items: GalleryItem[] }) {
  const container = useRef<HTMLDivElement>(null);
  const track = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const trackEl = track.current!;
      const scrollWidth = trackEl.scrollWidth - window.innerWidth;

      gsap.to(trackEl, {
        x: -scrollWidth,
        ease: "none",
        scrollTrigger: {
          trigger: container.current,
          start: "top top",
          end: `+=${scrollWidth}`,
          pin: true,
          scrub: 0.5,
          invalidateOnRefresh: true,
        },
      });
    },
    { scope: container }
  );

  return (
    <section ref={container} className="overflow-hidden">
      <div ref={track} className="flex gap-8 px-8 will-change-transform">
        {items.map((item, i) => (
          <div key={i} className="flex-shrink-0 w-[80vw] md:w-[50vw] lg:w-[40vw]">
            <img
              src={item.src}
              alt={item.alt}
              className="w-full h-[60vh] object-cover rounded-2xl"
              loading="lazy"
            />
            <p className="mt-4 text-lg font-medium">{item.title}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
```

**Reduced motion:** Renders as a standard horizontal scrollable container.

**Performance:** `will-change-transform` on the track promotes to compositor layer. Use `loading="lazy"` on images.

---

## Recipe 4: Parallax Layers

**What it does:** Multiple visual layers move at different speeds during scroll, creating depth.

**When to use:** Hero sections, background effects, immersive landing pages.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

interface ParallaxLayer {
  content: React.ReactNode;
  speed: number; // -1 to 1: negative = slower, positive = faster
  className?: string;
}

export function ParallaxSection({ layers }: { layers: ParallaxLayer[] }) {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      layers.forEach((layer, i) => {
        gsap.to(`.parallax-layer-${i}`, {
          yPercent: layer.speed * 30,
          ease: "none",
          scrollTrigger: {
            trigger: container.current,
            start: "top bottom",
            end: "bottom top",
            scrub: true,
          },
        });
      });
    },
    { scope: container }
  );

  return (
    <section ref={container} className="relative h-[80vh] overflow-hidden">
      {layers.map((layer, i) => (
        <div
          key={i}
          className={`parallax-layer-${i} absolute inset-0 will-change-transform ${
            layer.className ?? ""
          }`}
        >
          {layer.content}
        </div>
      ))}
    </section>
  );
}
```

**Usage:**
```tsx
<ParallaxSection
  layers={[
    { content: <img src="/bg.jpg" alt="" className="w-full h-full object-cover" />, speed: -0.5 },
    { content: <div className="flex items-center justify-center h-full"><h1 className="text-6xl font-bold text-white">Title</h1></div>, speed: 0.2 },
    { content: <img src="/foreground.png" alt="" className="w-full h-full object-contain" />, speed: 0.5 },
  ]}
/>
```

---

## Recipe 5: Scale-to-Full Hero

**What it does:** A small element scales up to fill the entire viewport as the user scrolls, with text fading in after scale completes.

**When to use:** Product reveals, app screenshots, dramatic hero entrances.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

export function ScaleToFullHero({
  imageSrc,
  imageAlt,
  headline,
  subline,
}: {
  imageSrc: string;
  imageAlt: string;
  headline: string;
  subline: string;
}) {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        gsap.set(".scale-image", { scale: 1, borderRadius: 0 });
        gsap.set(".hero-text", { opacity: 1, y: 0 });
        return;
      }

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: container.current,
          start: "top top",
          end: "+=150%",
          pin: true,
          scrub: 1,
        },
      });

      tl.fromTo(
        ".scale-image",
        { scale: 0.4, borderRadius: "24px" },
        { scale: 1, borderRadius: "0px", duration: 1, ease: "power2.inOut" }
      ).fromTo(
        ".hero-text",
        { opacity: 0, y: 40 },
        { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" },
        0.7
      );
    },
    { scope: container }
  );

  return (
    <div ref={container} className="relative h-screen flex items-center justify-center overflow-hidden">
      <img
        src={imageSrc}
        alt={imageAlt}
        className="scale-image absolute inset-0 w-full h-full object-cover will-change-transform"
      />
      <div className="hero-text relative z-10 text-center text-white opacity-0">
        <h1 className="text-5xl md:text-7xl font-bold mb-4">{headline}</h1>
        <p className="text-xl md:text-2xl text-white/80">{subline}</p>
      </div>
    </div>
  );
}
```

---

## Recipe 6: Scroll-Snap Sections

**What it does:** Full-viewport sections with CSS scroll snap, GSAP entrance animations triggered per section.

**When to use:** Storytelling flows, product tours, presentation-style pages.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

export function ScrollSnapSections({ sections }: { sections: React.ReactNode[] }) {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      sections.forEach((_, i) => {
        gsap.from(`.snap-section-${i} .section-content`, {
          opacity: 0,
          y: 60,
          duration: 0.8,
          ease: "power2.out",
          scrollTrigger: {
            trigger: `.snap-section-${i}`,
            start: "top 60%",
            toggleActions: "play none none reverse",
          },
        });
      });
    },
    { scope: container }
  );

  return (
    <div
      ref={container}
      className="h-screen overflow-y-auto snap-y snap-mandatory"
    >
      {sections.map((content, i) => (
        <section
          key={i}
          className={`snap-section-${i} h-screen snap-start flex items-center justify-center px-8`}
        >
          <div className="section-content max-w-4xl">{content}</div>
        </section>
      ))}
    </div>
  );
}
```

---

## Recipe 7: Sticky Header Transform

**What it does:** Full-size header shrinks to compact on scroll — logo resizes, background appears, shadow adds depth.

**When to use:** Every marketing site and SaaS product.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

export function StickyHeader({ children }: { children: React.ReactNode }) {
  const header = useRef<HTMLElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      gsap.to(header.current, {
        scrollTrigger: {
          trigger: document.body,
          start: "80px top",
          end: "81px top",
          toggleActions: "play none none reverse",
        },
        backgroundColor: "rgba(255, 255, 255, 0.95)",
        backdropFilter: "blur(12px)",
        boxShadow: "0 1px 3px rgba(0,0,0,0.08)",
        height: 56,
        duration: 0.3,
        ease: "power2.out",
      });

      gsap.to(".header-logo", {
        scrollTrigger: {
          trigger: document.body,
          start: "80px top",
          end: "81px top",
          toggleActions: "play none none reverse",
        },
        scale: 0.85,
        duration: 0.3,
        ease: "power2.out",
      });
    },
    { scope: header }
  );

  return (
    <header
      ref={header}
      className="fixed top-0 left-0 right-0 z-50 h-20 flex items-center px-6 transition-none"
    >
      {children}
    </header>
  );
}
```

---

## Recipe 8: Progress-Linked Color Change

**What it does:** Background color smoothly transitions between section themes as the user scrolls.

**When to use:** Landing pages with distinct themed sections, storytelling.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

interface ColorSection {
  bg: string;
  text: string;
  content: React.ReactNode;
}

export function ColorShiftSections({ sections }: { sections: ColorSection[] }) {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      sections.forEach((section, i) => {
        gsap.to(container.current, {
          backgroundColor: section.bg,
          color: section.text,
          scrollTrigger: {
            trigger: `.color-section-${i}`,
            start: "top 60%",
            end: "top 30%",
            scrub: true,
          },
        });
      });
    },
    { scope: container }
  );

  return (
    <div ref={container} style={{ backgroundColor: sections[0]?.bg, color: sections[0]?.text }}>
      {sections.map((section, i) => (
        <section
          key={i}
          className={`color-section-${i} min-h-screen flex items-center justify-center px-8`}
        >
          <div className="max-w-4xl">{section.content}</div>
        </section>
      ))}
    </div>
  );
}
```

---

## Recipe 9: Image Clip-Path Reveal

**What it does:** Images are revealed through animated clip-path as they scroll into view — circle, inset, or polygon.

**When to use:** Portfolio items, feature images, editorial sections.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

type RevealShape = "circle" | "inset" | "polygon";

export function ClipPathReveal({
  src,
  alt,
  shape = "inset",
}: {
  src: string;
  alt: string;
  shape?: RevealShape;
}) {
  const imageRef = useRef<HTMLDivElement>(null);

  const clipPaths: Record<RevealShape, { from: string; to: string }> = {
    circle: {
      from: "circle(0% at 50% 50%)",
      to: "circle(75% at 50% 50%)",
    },
    inset: {
      from: "inset(50% 50% 50% 50%)",
      to: "inset(0% 0% 0% 0%)",
    },
    polygon: {
      from: "polygon(50% 50%, 50% 50%, 50% 50%, 50% 50%)",
      to: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)",
    },
  };

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        gsap.set(imageRef.current, { clipPath: clipPaths[shape].to });
        return;
      }

      gsap.fromTo(
        imageRef.current,
        { clipPath: clipPaths[shape].from },
        {
          clipPath: clipPaths[shape].to,
          duration: 1.2,
          ease: "power3.inOut",
          scrollTrigger: {
            trigger: imageRef.current,
            start: "top 75%",
            toggleActions: "play none none none",
          },
        }
      );
    },
    { scope: imageRef }
  );

  return (
    <div ref={imageRef} className="overflow-hidden">
      <img src={src} alt={alt} className="w-full h-auto" loading="lazy" />
    </div>
  );
}
```

---

## Recipe 10: Before/After Slider (Scroll-Driven)

**What it does:** Two overlapping images with a divider controlled by scroll position.

**When to use:** Design comparisons, before/after showcases, product transformations.

```tsx
"use client";
import { useRef, useState } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

export function BeforeAfterSlider({
  beforeSrc,
  afterSrc,
  beforeAlt,
  afterAlt,
}: {
  beforeSrc: string;
  afterSrc: string;
  beforeAlt: string;
  afterAlt: string;
}) {
  const container = useRef<HTMLDivElement>(null);
  const [clipPercent, setClipPercent] = useState(50);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const proxy = { value: 0 };
      gsap.fromTo(
        proxy,
        { value: 0 },
        {
          value: 100,
          ease: "none",
          scrollTrigger: {
            trigger: container.current,
            start: "top center",
            end: "bottom center",
            scrub: true,
            onUpdate: () => setClipPercent(proxy.value),
          },
        }
      );
    },
    { scope: container }
  );

  return (
    <div ref={container} className="relative w-full h-[70vh] overflow-hidden select-none">
      {/* After image (full, behind) */}
      <img src={afterSrc} alt={afterAlt} className="absolute inset-0 w-full h-full object-cover" />

      {/* Before image (clipped) */}
      <img
        src={beforeSrc}
        alt={beforeAlt}
        className="absolute inset-0 w-full h-full object-cover"
        style={{ clipPath: `inset(0 ${100 - clipPercent}% 0 0)` }}
      />

      {/* Divider line */}
      <div
        className="absolute top-0 bottom-0 w-0.5 bg-white shadow-lg z-10"
        style={{ left: `${clipPercent}%` }}
      >
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 bg-white rounded-full shadow-md flex items-center justify-center">
          <span className="text-gray-600 text-sm">↔</span>
        </div>
      </div>
    </div>
  );
}
```

---

## Recipe 11: SplitText Character Stagger

**What it does:** Splits text into individual characters and staggers their entrance animation.

**When to use:** Hero headlines, section titles, dramatic text reveals.

**Dependencies:** GSAP SplitText plugin (Club GSAP or self-hosted)

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP, SplitText } from "@/lib/gsap";

type StaggerPattern = "start" | "center" | "end" | "edges" | "random";

export function CharStagger({
  text,
  as: Tag = "h1",
  pattern = "start",
  className = "",
}: {
  text: string;
  as?: "h1" | "h2" | "h3" | "p" | "span";
  pattern?: StaggerPattern;
  className?: string;
}) {
  const textRef = useRef<HTMLElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const split = new SplitText(textRef.current, { type: "chars" });

      gsap.from(split.chars, {
        opacity: 0,
        y: 30,
        rotateX: -40,
        stagger: {
          each: 0.03,
          from: pattern,
        },
        duration: 0.6,
        ease: "back.out(1.7)",
        scrollTrigger: {
          trigger: textRef.current,
          start: "top 80%",
          toggleActions: "play none none none",
        },
      });

      // Cleanup: revert split on unmount (handled by useGSAP)
      return () => split.revert();
    },
    { scope: textRef }
  );

  return <Tag ref={textRef as any} className={className}>{text}</Tag>;
}
```

**Usage:**
```tsx
<CharStagger text="Build something beautiful" as="h1" pattern="center" className="text-6xl font-bold" />
```

---

## Recipe 12: SplitText Line-by-Line Reveal

**What it does:** Splits text into lines, each slides up from behind a mask.

**When to use:** Paragraphs, descriptions, body text entrance.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP, SplitText } from "@/lib/gsap";

export function LineReveal({
  text,
  className = "",
}: {
  text: string;
  className?: string;
}) {
  const textRef = useRef<HTMLParagraphElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const split = new SplitText(textRef.current, {
        type: "lines",
        linesClass: "split-line",
      });

      // Wrap each line in a clip container
      split.lines.forEach((line) => {
        const wrapper = document.createElement("div");
        wrapper.style.overflow = "hidden";
        line.parentNode?.insertBefore(wrapper, line);
        wrapper.appendChild(line);
      });

      gsap.from(split.lines, {
        yPercent: 110,
        opacity: 0,
        stagger: 0.08,
        duration: 0.7,
        ease: "power3.out",
        scrollTrigger: {
          trigger: textRef.current,
          start: "top 85%",
          toggleActions: "play none none none",
        },
      });

      return () => split.revert();
    },
    { scope: textRef }
  );

  return <p ref={textRef} className={className}>{text}</p>;
}
```

**Responsive:** SplitText recalculates line breaks on resize. Add `ScrollTrigger.addEventListener("refreshInit", () => split.revert())` then re-split for robust resize handling.

---

## Recipe 13: SplitText Word Scramble

**What it does:** Words animate in with rotation, scale, and blur, then settle into position.

**When to use:** Playful headlines, creative portfolios, gaming.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP, SplitText } from "@/lib/gsap";

export function WordScramble({
  text,
  className = "",
}: {
  text: string;
  className?: string;
}) {
  const textRef = useRef<HTMLHeadingElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const split = new SplitText(textRef.current, { type: "words" });

      gsap.from(split.words, {
        opacity: 0,
        scale: 0.5,
        rotation: () => gsap.utils.random(-15, 15),
        filter: "blur(8px)",
        stagger: {
          each: 0.05,
          from: "random",
        },
        duration: 0.8,
        ease: "elastic.out(1, 0.5)",
        scrollTrigger: {
          trigger: textRef.current,
          start: "top 80%",
          toggleActions: "play none none none",
        },
      });

      return () => split.revert();
    },
    { scope: textRef }
  );

  return <h2 ref={textRef} className={className}>{text}</h2>;
}
```

---

## Recipe 14: Text Mask Reveal

**What it does:** Text is hidden behind a gradient mask that slides away on scroll, revealing the text progressively.

**When to use:** Editorial, long-form content, cinematic reveals.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

export function TextMaskReveal({
  children,
  className = "",
}: {
  children: React.ReactNode;
  className?: string;
}) {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        gsap.set(".mask-overlay", { xPercent: 100 });
        return;
      }

      gsap.to(".mask-overlay", {
        xPercent: 100,
        ease: "power2.inOut",
        scrollTrigger: {
          trigger: container.current,
          start: "top 70%",
          end: "top 30%",
          scrub: true,
        },
      });
    },
    { scope: container }
  );

  return (
    <div ref={container} className={`relative overflow-hidden ${className}`}>
      {children}
      <div
        className="mask-overlay absolute inset-0 bg-white dark:bg-gray-950 z-10"
        aria-hidden="true"
      />
    </div>
  );
}
```

---

## Recipe 15: Counter/Number Animation

**What it does:** Animates a number from 0 to a target value, with formatting options.

**When to use:** Stats sections, dashboards, metric displays.

```tsx
"use client";
import { useRef, useState } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

type Format = "number" | "currency" | "percent";

export function AnimatedCounter({
  target,
  format = "number",
  prefix = "",
  suffix = "",
  decimals = 0,
  duration = 2,
  className = "",
}: {
  target: number;
  format?: Format;
  prefix?: string;
  suffix?: string;
  decimals?: number;
  duration?: number;
  className?: string;
}) {
  const [display, setDisplay] = useState("0");
  const container = useRef<HTMLSpanElement>(null);

  const formatNumber = (val: number): string => {
    switch (format) {
      case "currency":
        return new Intl.NumberFormat("en-US", {
          style: "currency",
          currency: "USD",
          maximumFractionDigits: decimals,
        }).format(val);
      case "percent":
        return `${val.toFixed(decimals)}%`;
      default:
        return val.toLocaleString("en-US", {
          maximumFractionDigits: decimals,
        });
    }
  };

  useGSAP(
    () => {
      const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (prefersReduced) {
        setDisplay(formatNumber(target));
        return;
      }

      const proxy = { value: 0 };
      gsap.to(proxy, {
        value: target,
        duration,
        ease: "power2.out",
        snap: { value: decimals === 0 ? 1 : 1 / Math.pow(10, decimals) },
        scrollTrigger: {
          trigger: container.current,
          start: "top 80%",
          toggleActions: "play none none none",
        },
        onUpdate: () => setDisplay(formatNumber(proxy.value)),
      });
    },
    { scope: container }
  );

  return (
    <span ref={container} className={className} aria-label={`${prefix}${formatNumber(target)}${suffix}`}>
      {prefix}{display}{suffix}
    </span>
  );
}
```

**Usage:**
```tsx
<AnimatedCounter target={10000} prefix="" suffix="+" className="text-5xl font-bold tabular-nums" />
<AnimatedCounter target={99.9} format="percent" decimals={1} />
<AnimatedCounter target={2500000} format="currency" />
```

---

## Recipe 16: Timeline Sequences

**What it does:** Chains multiple animations into a coordinated sequence with play/pause/reverse controls.

**When to use:** Onboarding flows, feature tours, complex choreography.

```tsx
"use client";
import { useRef, useState } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

export function TimelineSequence() {
  const container = useRef<HTMLDivElement>(null);
  const tl = useRef<gsap.core.Timeline | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      tl.current = gsap.timeline({ paused: true });

      tl.current
        .from(".step-1", { opacity: 0, x: -60, duration: 0.5, ease: "power2.out" })
        .from(".step-2", { opacity: 0, y: 40, duration: 0.5, ease: "power2.out" }, "-=0.2")
        .from(".step-3", { opacity: 0, scale: 0.8, duration: 0.6, ease: "back.out(1.7)" }, "-=0.1")
        .from(".step-4", { opacity: 0, rotation: -10, duration: 0.4, ease: "power2.out" })
        .to(".highlight", { backgroundColor: "oklch(0.55 0.20 260)", color: "white", duration: 0.3 }, "<");
    },
    { scope: container }
  );

  const play = () => { tl.current?.play(); setIsPlaying(true); };
  const pause = () => { tl.current?.pause(); setIsPlaying(false); };
  const reverse = () => { tl.current?.reverse(); setIsPlaying(false); };
  const restart = () => { tl.current?.restart(); setIsPlaying(true); };

  return (
    <div ref={container}>
      <div className="flex gap-3 mb-8">
        <button onClick={play} className="px-4 py-2 bg-gray-900 text-white rounded-lg text-sm">Play</button>
        <button onClick={pause} className="px-4 py-2 bg-gray-200 rounded-lg text-sm">Pause</button>
        <button onClick={reverse} className="px-4 py-2 bg-gray-200 rounded-lg text-sm">Reverse</button>
        <button onClick={restart} className="px-4 py-2 bg-gray-200 rounded-lg text-sm">Restart</button>
      </div>
      <div className="space-y-4">
        <div className="step-1 p-4 bg-gray-100 dark:bg-gray-800 rounded-lg">Step 1</div>
        <div className="step-2 p-4 bg-gray-100 dark:bg-gray-800 rounded-lg">Step 2</div>
        <div className="step-3 p-4 bg-gray-100 dark:bg-gray-800 rounded-lg">Step 3</div>
        <div className="step-4 p-4 bg-gray-100 dark:bg-gray-800 rounded-lg">
          <span className="highlight px-2 py-1 rounded">Step 4 with highlight</span>
        </div>
      </div>
    </div>
  );
}
```

---

## Recipe 17: Card Stack Reveal

**What it does:** Cards stacked on top of each other are revealed one by one as the user scrolls, with 3D rotation and translation.

**When to use:** Feature lists, testimonials, portfolio items.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

interface CardData {
  title: string;
  description: string;
}

export function CardStackReveal({ cards }: { cards: CardData[] }) {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: container.current,
          start: "top top",
          end: `+=${cards.length * 80}%`,
          pin: true,
          scrub: 1,
        },
      });

      cards.forEach((_, i) => {
        if (i === 0) return;
        tl.fromTo(
          `.stack-card-${i}`,
          { y: 300, rotateX: -15, scale: 0.9, opacity: 0 },
          { y: 0, rotateX: 0, scale: 1, opacity: 1, duration: 1, ease: "power2.out" },
          i * 0.8
        );
        // Push previous cards up slightly
        tl.to(
          `.stack-card-${i - 1}`,
          { y: -(i * 20), scale: 1 - i * 0.03, filter: `brightness(${1 - i * 0.1})`, duration: 1 },
          i * 0.8
        );
      });
    },
    { scope: container }
  );

  return (
    <div ref={container} className="relative h-screen flex items-center justify-center" style={{ perspective: "1200px" }}>
      <div className="relative w-full max-w-lg">
        {cards.map((card, i) => (
          <div
            key={i}
            className={`stack-card-${i} ${
              i === 0 ? "" : "absolute inset-0 opacity-0"
            } bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-xl`}
          >
            <h3 className="text-2xl font-bold mb-3">{card.title}</h3>
            <p className="text-gray-600 dark:text-gray-400">{card.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

---

## Recipe 18: Stagger Grid Entrance

**What it does:** Grid items animate in with configurable stagger patterns — row-by-row, center-out, or random.

**When to use:** Feature grids, card layouts, gallery entrances.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP, ScrollTrigger } from "@/lib/gsap";

type StaggerFrom = "start" | "center" | "edges" | "random";

export function StaggerGrid({
  children,
  staggerFrom = "start",
  columns = 3,
  className = "",
}: {
  children: React.ReactNode;
  staggerFrom?: StaggerFrom;
  columns?: number;
  className?: string;
}) {
  const grid = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      // Use ScrollTrigger.batch for performance with many items
      ScrollTrigger.batch(".grid-item", {
        onEnter: (elements) => {
          gsap.from(elements, {
            opacity: 0,
            y: 40,
            scale: 0.95,
            stagger: {
              each: 0.06,
              from: staggerFrom,
              grid: [Math.ceil((elements.length) / columns), columns],
            },
            duration: 0.6,
            ease: "power2.out",
          });
        },
        start: "top 85%",
        once: true,
      });
    },
    { scope: grid }
  );

  return (
    <div
      ref={grid}
      className={`grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-${columns} gap-6 ${className}`}
    >
      {Array.isArray(children)
        ? children.map((child, i) => (
            <div key={i} className="grid-item">
              {child}
            </div>
          ))
        : children}
    </div>
  );
}
```

**Performance:** `ScrollTrigger.batch` is much more efficient than individual ScrollTriggers for large grids (100+ items).

---

## Recipe 19: Marquee / Infinite Ticker

**What it does:** Continuously scrolling horizontal ticker that pauses on hover, loops seamlessly.

**When to use:** Logo clouds, announcements, testimonials, social proof.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

export function Marquee({
  children,
  speed = 40,
  direction = "left",
  pauseOnHover = true,
  className = "",
}: {
  children: React.ReactNode;
  speed?: number;
  direction?: "left" | "right";
  pauseOnHover?: boolean;
  className?: string;
}) {
  const container = useRef<HTMLDivElement>(null);
  const tweenRef = useRef<gsap.core.Tween | null>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const track = container.current!.querySelector(".marquee-track") as HTMLElement;
      const totalWidth = track.scrollWidth / 2; // Content is duplicated

      tweenRef.current = gsap.to(track, {
        x: direction === "left" ? -totalWidth : totalWidth,
        duration: totalWidth / speed,
        ease: "none",
        repeat: -1,
        modifiers: {
          x: gsap.utils.unitize((x) => {
            const val = parseFloat(x);
            return direction === "left"
              ? ((val % totalWidth) + totalWidth) % totalWidth - totalWidth
              : val % totalWidth;
          }),
        },
      });
    },
    { scope: container }
  );

  const handleMouseEnter = () => {
    if (pauseOnHover) tweenRef.current?.pause();
  };
  const handleMouseLeave = () => {
    if (pauseOnHover) tweenRef.current?.resume();
  };

  return (
    <div
      ref={container}
      className={`overflow-hidden ${className}`}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      <div className="marquee-track flex will-change-transform">
        <div className="flex shrink-0 gap-8 items-center">{children}</div>
        <div className="flex shrink-0 gap-8 items-center" aria-hidden="true">{children}</div>
      </div>
    </div>
  );
}
```

**Usage:**
```tsx
<Marquee speed={30} pauseOnHover>
  <img src="/logo1.svg" alt="Company 1" className="h-8" />
  <img src="/logo2.svg" alt="Company 2" className="h-8" />
  <img src="/logo3.svg" alt="Company 3" className="h-8" />
</Marquee>
```

---

## Recipe 20: Magnetic Button

**What it does:** Button subtly follows the cursor when within a magnetic radius, snapping back with spring physics on leave.

**When to use:** CTAs, hero buttons, interactive highlights.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

export function MagneticButton({
  children,
  strength = 0.3,
  className = "",
}: {
  children: React.ReactNode;
  strength?: number;
  className?: string;
}) {
  const button = useRef<HTMLButtonElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const el = button.current!;

      const handleMouseMove = (e: MouseEvent) => {
        const rect = el.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        gsap.to(el, {
          x: x * strength,
          y: y * strength,
          duration: 0.3,
          ease: "power2.out",
        });
      };

      const handleMouseLeave = () => {
        gsap.to(el, {
          x: 0,
          y: 0,
          duration: 0.5,
          ease: "elastic.out(1, 0.3)",
        });
      };

      el.addEventListener("mousemove", handleMouseMove);
      el.addEventListener("mouseleave", handleMouseLeave);

      return () => {
        el.removeEventListener("mousemove", handleMouseMove);
        el.removeEventListener("mouseleave", handleMouseLeave);
      };
    },
    { scope: button }
  );

  return (
    <button ref={button} className={`will-change-transform ${className}`}>
      {children}
    </button>
  );
}
```

---

## Recipe 21: SVG Morph

**What it does:** Smoothly morphs between two SVG paths using GSAP MorphSVGPlugin.

**When to use:** Icon transitions, decorative shape morphs, interactive illustrations.

**Dependencies:** GSAP MorphSVGPlugin (Club GSAP)

```tsx
"use client";
import { useRef, useState } from "react";
import { gsap, useGSAP } from "@/lib/gsap";
// import { MorphSVGPlugin } from "gsap/MorphSVGPlugin";
// gsap.registerPlugin(MorphSVGPlugin);

const shapes = {
  circle: "M50,10 A40,40 0 1,1 49.99,10 Z",
  square: "M10,10 L90,10 L90,90 L10,90 Z",
  star: "M50,5 L61,35 L95,35 L68,57 L79,91 L50,70 L21,91 L32,57 L5,35 L39,35 Z",
  heart: "M50,88 C25,68 5,50 5,30 A20,20 0 0,1 50,20 A20,20 0 0,1 95,30 C95,50 75,68 50,88 Z",
};

type ShapeName = keyof typeof shapes;

export function SvgMorph({ className = "" }: { className?: string }) {
  const svgRef = useRef<SVGSVGElement>(null);
  const [current, setCurrent] = useState<ShapeName>("circle");

  const morphTo = (shape: ShapeName) => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      gsap.set("#morph-path", { attr: { d: shapes[shape] } });
      setCurrent(shape);
      return;
    }

    gsap.to("#morph-path", {
      morphSVG: shapes[shape],
      duration: 0.6,
      ease: "power2.inOut",
    });
    setCurrent(shape);
  };

  return (
    <div className={className}>
      <svg ref={svgRef} viewBox="0 0 100 100" className="w-48 h-48">
        <path
          id="morph-path"
          d={shapes.circle}
          fill="oklch(0.55 0.20 260)"
        />
      </svg>
      <div className="flex gap-2 mt-4">
        {(Object.keys(shapes) as ShapeName[]).map((shape) => (
          <button
            key={shape}
            onClick={() => morphTo(shape)}
            className={`px-3 py-1.5 rounded-md text-sm capitalize ${
              current === shape
                ? "bg-gray-900 text-white dark:bg-white dark:text-gray-900"
                : "bg-gray-100 dark:bg-gray-800"
            }`}
          >
            {shape}
          </button>
        ))}
      </div>
    </div>
  );
}
```

---

## Recipe 22: Scroll-Linked Camera (2D)

**What it does:** Simulates camera zoom and pan on a large canvas as the user scrolls — like a 2D "dolly shot."

**When to use:** Product tours, infographic exploration, map-style interfaces.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP } from "@/lib/gsap";

interface CameraShot {
  x: number; // Translate X in %
  y: number; // Translate Y in %
  scale: number;
  duration: number;
}

export function ScrollCamera({
  shots,
  children,
}: {
  shots: CameraShot[];
  children: React.ReactNode;
}) {
  const viewport = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: viewport.current,
          start: "top top",
          end: `+=${shots.length * 100}%`,
          pin: true,
          scrub: 1,
        },
      });

      shots.forEach((shot, i) => {
        tl.to(".camera-canvas", {
          xPercent: -shot.x,
          yPercent: -shot.y,
          scale: shot.scale,
          duration: shot.duration,
          ease: "power2.inOut",
        });
      });
    },
    { scope: viewport }
  );

  return (
    <div ref={viewport} className="h-screen overflow-hidden">
      <div className="camera-canvas w-[300vw] h-[300vh] will-change-transform origin-top-left">
        {children}
      </div>
    </div>
  );
}
```

---

## Recipe 23: gsap.matchMedia() for Responsive

**What it does:** Different animations for different breakpoints and reduced motion, with automatic cleanup per context.

**When to use:** Any animation that should differ between mobile and desktop.

```tsx
"use client";
import { useRef } from "react";
import { gsap, useGSAP, ScrollTrigger } from "@/lib/gsap";

export function ResponsiveAnimation({ children }: { children: React.ReactNode }) {
  const container = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      const mm = gsap.matchMedia();

      mm.add(
        {
          isDesktop: "(min-width: 1024px)",
          isMobile: "(max-width: 1023px)",
          reduceMotion: "(prefers-reduced-motion: reduce)",
        },
        (context) => {
          const { isDesktop, isMobile, reduceMotion } = context.conditions!;

          if (reduceMotion) {
            gsap.set(".animate-item", { opacity: 1, y: 0, x: 0 });
            return;
          }

          if (isDesktop) {
            // Desktop: items slide in from left with stagger
            gsap.from(".animate-item", {
              opacity: 0,
              x: -60,
              stagger: 0.1,
              duration: 0.8,
              ease: "power2.out",
              scrollTrigger: {
                trigger: container.current,
                start: "top 70%",
              },
            });
          }

          if (isMobile) {
            // Mobile: items fade in from below, simpler
            gsap.from(".animate-item", {
              opacity: 0,
              y: 30,
              stagger: 0.05,
              duration: 0.5,
              ease: "power2.out",
              scrollTrigger: {
                trigger: container.current,
                start: "top 85%",
              },
            });
          }
        }
      );
    },
    { scope: container }
  );

  return <div ref={container}>{children}</div>;
}
```

---

## Recipe 24: Next.js App Router Integration

**What it does:** Proper GSAP setup for Next.js App Router with dynamic imports, client boundaries, and route change cleanup.

**When to use:** Every Next.js project using GSAP.

```tsx
// lib/gsap.ts — Dynamic registration for App Router
"use client";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

if (typeof window !== "undefined") {
  gsap.registerPlugin(ScrollTrigger);
}

export { gsap, ScrollTrigger, useGSAP };
```

```tsx
// components/AnimatedPage.tsx — Per-page animation wrapper
"use client";
import { useRef } from "react";
import { gsap, useGSAP, ScrollTrigger } from "@/lib/gsap";

export function AnimatedPage({ children }: { children: React.ReactNode }) {
  const page = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      // Refresh ScrollTrigger after page renders (images, lazy content)
      const timer = setTimeout(() => ScrollTrigger.refresh(), 100);

      // Page entrance
      if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        gsap.from(page.current, {
          opacity: 0,
          y: 20,
          duration: 0.5,
          ease: "power2.out",
        });
      }

      return () => {
        clearTimeout(timer);
        // Kill all ScrollTriggers on this page on unmount
        ScrollTrigger.getAll().forEach((st) => st.kill());
      };
    },
    { scope: page }
  );

  return (
    <div ref={page} className="min-h-screen">
      {children}
    </div>
  );
}
```

```tsx
// app/page.tsx — Usage in App Router page
import { AnimatedPage } from "@/components/AnimatedPage";
import { FadeInSection } from "@/components/FadeInSection";

export default function HomePage() {
  return (
    <AnimatedPage>
      <FadeInSection>
        <h1 className="text-6xl font-bold">Welcome</h1>
      </FadeInSection>
    </AnimatedPage>
  );
}
```

**Key rules:**
- Always add `"use client"` to files importing GSAP
- Use `useGSAP` instead of `useEffect` + `useRef` — it handles cleanup automatically
- Call `ScrollTrigger.refresh()` after dynamic content loads
- Kill ScrollTriggers on page unmount to prevent memory leaks

---

## Recipe 25: Performance Guide

### will-change Best Practices

```css
/* Only add will-change on elements that are about to animate */
.will-animate {
  will-change: transform;
}
/* Remove after animation completes to free compositor memory */
```

In GSAP: `gsap.set(el, { willChange: "transform" })` before animation, `gsap.set(el, { willChange: "auto" })` after.

### force3D and Rotation Trick

```javascript
// GSAP defaults: force3D is true — promotes to GPU layer
gsap.defaults({ force3D: true });

// For elements that flicker on sub-pixel rendering:
gsap.set(el, { rotation: 0.01 }); // Forces GPU compositing without visible effect
```

### ScrollTrigger.batch() for Many Elements

```javascript
// Instead of 100 individual ScrollTriggers:
ScrollTrigger.batch(".grid-item", {
  onEnter: (batch) => gsap.to(batch, { opacity: 1, y: 0, stagger: 0.03 }),
  start: "top 85%",
  once: true,
});
// One observer instead of 100
```

### Lazy Plugin Registration

```javascript
// Don't register plugins you're not using on the current page
// Instead, dynamically import heavy plugins
async function initSplitText() {
  const { SplitText } = await import("gsap/SplitText");
  gsap.registerPlugin(SplitText);
}
```

### Memory Leak Prevention

```javascript
// useGSAP handles this automatically, but if using useEffect:
useEffect(() => {
  const ctx = gsap.context(() => {
    // all GSAP code here
  }, containerRef);

  return () => ctx.revert(); // Kills all GSAP instances in this context
}, []);
```

### 60fps Monitoring

```javascript
// Development only: log frame drops
if (process.env.NODE_ENV === "development") {
  gsap.ticker.add(() => {
    if (gsap.ticker.deltaRatio() > 1.5) {
      console.warn("Frame drop detected:", gsap.ticker.deltaRatio());
    }
  });
}
```

---

## Quick Reference: Easing Cheat Sheet

| Name | GSAP String | Feel | Best For |
|------|------------|------|----------|
| Smooth deceleration | `"power2.out"` | Natural stop | Entrances, reveals |
| Smooth acceleration | `"power2.in"` | Natural start | Exits, dismissals |
| Smooth both | `"power2.inOut"` | Elegant | Morphs, transforms |
| Sharp deceleration | `"power4.out"` | Snappy | Quick reveals |
| Bounce back | `"back.out(1.7)"` | Overshoot | Playful entrances |
| Elastic | `"elastic.out(1, 0.3)"` | Springy | Attention, emphasis |
| Bounce | `"bounce.out"` | Bouncy | Playful, gaming |
| Linear | `"none"` | Constant speed | Scroll-linked, tickers |

## Quick Reference: ScrollTrigger Positions

| Value | Meaning |
|-------|---------|
| `"top top"` | Element's top hits viewport's top |
| `"top 80%"` | Element's top hits 80% from viewport top |
| `"center center"` | Element center hits viewport center |
| `"bottom bottom"` | Element's bottom hits viewport's bottom |
| `"top bottom"` | Element's top enters viewport from below |

## Quick Reference: toggleActions

Format: `"onEnter onLeave onEnterBack onLeaveBack"`

| Preset | Value | Use Case |
|--------|-------|----------|
| Play once | `"play none none none"` | Most common — animate in, done |
| Play/reverse | `"play none none reverse"` | Animate in, undo when scrolling back |
| Restart each time | `"restart none none none"` | Re-trigger on every scroll down |
| Play/reset | `"play none none reset"` | Snap back to start when scrolling back |
