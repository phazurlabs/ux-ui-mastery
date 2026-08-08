# Scroll-Driven and Gesture Animation Recipes

Production-ready scroll and gesture animation patterns. Covers CSS Scroll-Driven Animations API, Intersection Observer, Framer Motion scroll utilities, and touch/pointer gesture code.

---

## Part 1: CSS Scroll-Driven Animations API (2024+)

The CSS Scroll-Driven Animations API (`animation-timeline: scroll()` and `animation-timeline: view()`) enables performant, declarative scroll-linked animations without JavaScript.

### Browser Support
- Chrome 115+, Edge 115+, Opera 101+
- Firefox: behind flag (`layout.css.scroll-driven-animations.enabled`)
- Safari: not yet supported (use Intersection Observer fallback)

### scroll() vs view()

- `scroll()`: Ties animation progress to the scroll position of a scroll container. 0% = top, 100% = fully scrolled.
- `view()`: Ties animation progress to an element's visibility within a scroll container. Animates as the element enters and exits the viewport.

---

### Recipe 1: Scroll Progress Bar
```css
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: #3b82f6;
  transform-origin: left;
  animation: scaleX linear;
  animation-timeline: scroll();
  z-index: 9999;
}

@keyframes scaleX {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

### Recipe 2: Fade In on Scroll (view timeline)
```css
.scroll-fade-in {
  animation: fadeInUp linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### Recipe 3: Scale on Scroll
```css
.scroll-scale {
  animation: scrollScale linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}

@keyframes scrollScale {
  from { transform: scale(0.8); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}
```

### Recipe 4: Parallax Background
```css
.parallax-section {
  position: relative;
  overflow: hidden;
}

.parallax-bg {
  position: absolute;
  inset: -30% 0;
  animation: parallaxShift linear;
  animation-timeline: scroll(nearest);
}

@keyframes parallaxShift {
  from { transform: translateY(0); }
  to { transform: translateY(-20%); }
}
```

### Recipe 5: Horizontal Scroll Progress
```css
.horizontal-progress {
  position: sticky;
  top: 0;
  height: 2px;
  background: linear-gradient(to right, #3b82f6 var(--progress), transparent var(--progress));
  animation: trackProgress linear;
  animation-timeline: scroll(x nearest);
}

@keyframes trackProgress {
  from { --progress: 0%; }
  to { --progress: 100%; }
}
```

### Recipe 6: Text Highlight on Scroll
```css
.scroll-highlight {
  background: linear-gradient(90deg, #fbbf24, #fbbf24) no-repeat;
  background-size: 0% 100%;
  -webkit-background-clip: text;
  animation: highlightFill linear;
  animation-timeline: view();
  animation-range: entry 50% cover 50%;
}

@keyframes highlightFill {
  to { background-size: 100% 100%; }
}
```

### Recipe 7: Rotate on Scroll
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

### Recipe 8: Color Shift on Scroll
```css
.scroll-color {
  animation: colorShift linear;
  animation-timeline: scroll();
}

@keyframes colorShift {
  0% { background-color: #1e293b; color: #f8fafc; }
  50% { background-color: #f8fafc; color: #1e293b; }
  100% { background-color: #1e293b; color: #f8fafc; }
}
```

### Recipe 9: Blur on Exit
```css
.scroll-blur-exit {
  animation: blurExit linear;
  animation-timeline: view();
  animation-range: exit 0% exit 100%;
}

@keyframes blurExit {
  from { filter: blur(0); opacity: 1; }
  to { filter: blur(8px); opacity: 0; }
}
```

### Recipe 10: Sticky Section Reveal
```css
.sticky-reveal {
  position: sticky;
  top: 0;
  height: 100vh;
}

.sticky-reveal-content {
  animation: revealContent linear;
  animation-timeline: scroll(nearest);
}

@keyframes revealContent {
  0% { opacity: 0; transform: translateY(40px); }
  30% { opacity: 1; transform: translateY(0); }
  70% { opacity: 1; transform: translateY(0); }
  100% { opacity: 0; transform: translateY(-40px); }
}
```

### Recipe 11: Counter on Scroll (CSS only with @property)
```css
@property --num {
  syntax: "<integer>";
  initial-value: 0;
  inherits: false;
}

.scroll-counter {
  animation: countUp linear;
  animation-timeline: view();
  animation-range: entry 25% cover 75%;
  counter-reset: num var(--num);
}

.scroll-counter::after {
  content: counter(num);
}

@keyframes countUp {
  from { --num: 0; }
  to { --num: 100; }
}
```

### Recipe 12: Image Reveal Clip on Scroll
```css
.scroll-image-reveal {
  animation: clipReveal linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 50%;
}

@keyframes clipReveal {
  from { clip-path: inset(0 100% 0 0); }
  to { clip-path: inset(0 0 0 0); }
}
```

---

## Part 2: Intersection Observer Patterns

For broader browser support, Intersection Observer provides scroll-triggered animations that work everywhere.

### Recipe 13: Basic Scroll Reveal
```js
const createScrollReveal = (selector, options = {}) => {
  const defaults = { threshold: 0.15, rootMargin: "0px 0px -10% 0px" };
  const config = { ...defaults, ...options };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        if (!config.repeat) observer.unobserve(entry.target);
      } else if (config.repeat) {
        entry.target.classList.remove("is-visible");
      }
    });
  }, { threshold: config.threshold, rootMargin: config.rootMargin });

  document.querySelectorAll(selector).forEach(el => observer.observe(el));
  return observer;
};

// Usage
createScrollReveal("[data-scroll-reveal]");
```

```css
[data-scroll-reveal] {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 500ms cubic-bezier(0.16, 1, 0.3, 1),
              transform 500ms cubic-bezier(0.16, 1, 0.3, 1);
}

[data-scroll-reveal].is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Recipe 14: Staggered Scroll Reveal
```js
const createStaggerReveal = (parentSelector) => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const children = entry.target.querySelectorAll("[data-stagger-item]");
        children.forEach((child, index) => {
          child.style.transitionDelay = `${index * 60}ms`;
          child.classList.add("is-visible");
        });
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll(parentSelector).forEach(el => observer.observe(el));
};
```

```css
[data-stagger-item] {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 400ms cubic-bezier(0.16, 1, 0.3, 1),
              transform 400ms cubic-bezier(0.16, 1, 0.3, 1);
}

[data-stagger-item].is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Recipe 15: Scroll-Triggered Counter
```js
const animateCounters = () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.dataset.target, 10);
        const duration = parseInt(el.dataset.duration || "2000", 10);
        const start = performance.now();

        const update = (now) => {
          const progress = Math.min((now - start) / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
          el.textContent = Math.round(eased * target).toLocaleString();
          if (progress < 1) requestAnimationFrame(update);
        };

        requestAnimationFrame(update);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll("[data-count-target]").forEach(el => {
    el.dataset.target = el.textContent;
    el.textContent = "0";
    observer.observe(el);
  });
};
```

### Recipe 16: Lazy Image Fade-In
```js
const lazyImages = () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.onload = () => img.classList.add("is-loaded");
        observer.unobserve(img);
      }
    });
  }, { rootMargin: "200px" });

  document.querySelectorAll("img[data-src]").forEach(img => observer.observe(img));
};
```

```css
img[data-src] {
  opacity: 0;
  filter: blur(8px);
  transition: opacity 400ms ease-out, filter 400ms ease-out;
}

img.is-loaded {
  opacity: 1;
  filter: blur(0);
}
```

### Recipe 17: Sticky Header on Scroll
```js
const stickyHeader = () => {
  const sentinel = document.createElement("div");
  sentinel.style.height = "1px";
  document.body.prepend(sentinel);

  const observer = new IntersectionObserver(([entry]) => {
    document.querySelector(".header").classList.toggle("is-sticky", !entry.isIntersecting);
  });

  observer.observe(sentinel);
};
```

```css
.header {
  transition: padding 300ms cubic-bezier(0.16, 1, 0.3, 1),
              backdrop-filter 300ms ease-out,
              box-shadow 300ms ease-out;
}

.header.is-sticky {
  padding-block: 8px;
  backdrop-filter: blur(12px);
  background: rgba(255, 255, 255, 0.85);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}
```

### Recipe 18: Scroll Progress with JS (fallback)
```js
const scrollProgress = () => {
  const bar = document.querySelector(".scroll-progress-bar");
  const update = () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? scrollTop / docHeight : 0;
    bar.style.transform = `scaleX(${progress})`;
  };

  window.addEventListener("scroll", update, { passive: true });
  update();
};
```

```css
.scroll-progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: #3b82f6;
  transform-origin: left;
  transform: scaleX(0);
  z-index: 9999;
}
```

---

## Part 3: Framer Motion Scroll Utilities

### Recipe 19: useScroll Progress Bar
```tsx
import { motion, useScroll, useSpring } from "framer-motion";

export const ScrollProgressBar = () => {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 100, damping: 30, restDelta: 0.001 });

  return (
    <motion.div
      style={{
        position: "fixed", top: 0, left: 0, right: 0, height: 3,
        background: "#3b82f6", transformOrigin: "left", scaleX, zIndex: 9999,
      }}
    />
  );
};
```

### Recipe 20: useInView Fade In
```tsx
import { motion, useInView } from "framer-motion";

export const ScrollFadeIn = ({ children }: { children: React.ReactNode }) => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-10%" });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 24 }}
      animate={isInView ? { opacity: 1, y: 0 } : { opacity: 0, y: 24 }}
      transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
    >
      {children}
    </motion.div>
  );
};
```

### Recipe 21: Parallax with useScroll
```tsx
import { motion, useScroll, useTransform } from "framer-motion";

export const Parallax = ({ children, speed = 0.3 }: { children: React.ReactNode; speed?: number }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "end start"] });
  const y = useTransform(scrollYProgress, [0, 1], [`-${speed * 100}%`, `${speed * 100}%`]);

  return (
    <div ref={ref} style={{ overflow: "hidden", position: "relative" }}>
      <motion.div style={{ y }}>{children}</motion.div>
    </div>
  );
};
```

### Recipe 22: Scroll-Linked Opacity
```tsx
export const ScrollOpacity = ({ children }: { children: React.ReactNode }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "center center"] });
  const opacity = useTransform(scrollYProgress, [0, 1], [0, 1]);

  return (
    <motion.div ref={ref} style={{ opacity }}>
      {children}
    </motion.div>
  );
};
```

### Recipe 23: Scroll-Linked Scale
```tsx
export const ScrollScale = ({ children }: { children: React.ReactNode }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "center center"] });
  const scale = useTransform(scrollYProgress, [0, 1], [0.8, 1]);
  const opacity = useTransform(scrollYProgress, [0, 0.3], [0, 1]);

  return (
    <motion.div ref={ref} style={{ scale, opacity }}>
      {children}
    </motion.div>
  );
};
```

### Recipe 24: Horizontal Scroll Section
```tsx
export const HorizontalScroll = ({ children }: { children: React.ReactNode }) => {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({ target: containerRef });
  const x = useTransform(scrollYProgress, [0, 1], ["0%", "-75%"]);

  return (
    <section ref={containerRef} style={{ height: "300vh" }}>
      <div style={{ position: "sticky", top: 0, height: "100vh", overflow: "hidden", display: "flex", alignItems: "center" }}>
        <motion.div style={{ x, display: "flex", gap: 24 }}>
          {children}
        </motion.div>
      </div>
    </section>
  );
};
```

### Recipe 25: Scroll-Triggered Stagger
```tsx
export const ScrollStagger = ({ children }: { children: React.ReactNode }) => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-15%" });

  return (
    <motion.div
      ref={ref}
      initial="hidden"
      animate={isInView ? "visible" : "hidden"}
      variants={{
        hidden: {},
        visible: { transition: { staggerChildren: 0.08, delayChildren: 0.1 } },
      }}
    >
      {React.Children.map(children, child => (
        <motion.div
          variants={{
            hidden: { opacity: 0, y: 30, scale: 0.95 },
            visible: { opacity: 1, y: 0, scale: 1 },
          }}
          transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
        >
          {child}
        </motion.div>
      ))}
    </motion.div>
  );
};
```

### Recipe 26: Scroll-Linked Rotation
```tsx
export const ScrollRotate = ({ children }: { children: React.ReactNode }) => {
  const { scrollYProgress } = useScroll();
  const rotate = useTransform(scrollYProgress, [0, 1], [0, 360]);

  return <motion.div style={{ rotate }}>{children}</motion.div>;
};
```

---

## Part 4: Gesture Animation Recipes

### Recipe 27: Drag with Constraints
```tsx
export const DragBox = () => {
  const constraintsRef = useRef(null);
  return (
    <div ref={constraintsRef} style={{ width: 400, height: 400, background: "#f1f5f9", borderRadius: 12 }}>
      <motion.div
        drag
        dragConstraints={constraintsRef}
        dragElastic={0.1}
        dragMomentum={true}
        whileDrag={{ scale: 1.05, boxShadow: "0 16px 40px rgba(0,0,0,0.15)" }}
        transition={{ type: "spring", stiffness: 300, damping: 25 }}
        style={{ width: 80, height: 80, background: "#3b82f6", borderRadius: 12, cursor: "grab" }}
      />
    </div>
  );
};
```

### Recipe 28: Swipe Card Stack (Tinder-style)
```tsx
export const SwipeCard = ({ onSwipeLeft, onSwipeRight, children }: {
  onSwipeLeft: () => void; onSwipeRight: () => void; children: React.ReactNode;
}) => {
  const x = useMotionValue(0);
  const rotate = useTransform(x, [-200, 200], [-15, 15]);
  const opacity = useTransform(x, [-200, -100, 0, 100, 200], [0.5, 1, 1, 1, 0.5]);

  return (
    <motion.div
      drag="x"
      dragConstraints={{ left: 0, right: 0 }}
      style={{ x, rotate, opacity, cursor: "grab" }}
      whileDrag={{ cursor: "grabbing", scale: 1.02 }}
      onDragEnd={(_, info) => {
        if (info.offset.x > 150) onSwipeRight();
        else if (info.offset.x < -150) onSwipeLeft();
      }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
    >
      {children}
    </motion.div>
  );
};
```

### Recipe 29: Drag to Reorder List
```tsx
export const DragReorderList = ({ items, setItems }: {
  items: { id: string; label: string }[];
  setItems: (items: { id: string; label: string }[]) => void;
}) => (
  <Reorder.Group axis="y" values={items} onReorder={setItems}
    style={{ listStyle: "none", padding: 0 }}>
    {items.map(item => (
      <Reorder.Item
        key={item.id}
        value={item}
        whileDrag={{
          scale: 1.03,
          boxShadow: "0 8px 24px rgba(0,0,0,0.12)",
          background: "white",
          zIndex: 1,
        }}
        transition={{ type: "spring", stiffness: 300, damping: 25 }}
        style={{ padding: "12px 16px", background: "white", borderRadius: 8,
          marginBottom: 8, cursor: "grab" }}
      >
        {item.label}
      </Reorder.Item>
    ))}
  </Reorder.Group>
);
```

### Recipe 30: Pull-to-Refresh
```tsx
export const PullToRefresh = ({ onRefresh, isRefreshing, children }: {
  onRefresh: () => void; isRefreshing: boolean; children: React.ReactNode;
}) => {
  const y = useMotionValue(0);
  const pullProgress = useTransform(y, [0, 80], [0, 1]);
  const spinnerRotate = useTransform(y, [0, 80], [0, 360]);
  const spinnerOpacity = useTransform(y, [0, 40, 80], [0, 0.5, 1]);

  return (
    <motion.div
      drag="y"
      dragConstraints={{ top: 0, bottom: 0 }}
      dragElastic={0.4}
      style={{ y }}
      onDragEnd={(_, info) => {
        if (info.offset.y > 80 && !isRefreshing) onRefresh();
      }}
    >
      <motion.div
        style={{ rotate: spinnerRotate, opacity: spinnerOpacity,
          display: "flex", justifyContent: "center", padding: 16 }}
      >
        <svg width="24" height="24" viewBox="0 0 24 24">
          <path d="M12 2v4m0 12v4M4.93 4.93l2.83 2.83m8.48 8.48l2.83 2.83M2 12h4m12 0h4M4.93 19.07l2.83-2.83m8.48-8.48l2.83-2.83"
            stroke="#3b82f6" strokeWidth="2" strokeLinecap="round" />
        </svg>
      </motion.div>
      {children}
    </motion.div>
  );
};
```

### Recipe 31: Pinch to Zoom (touch)
```tsx
export const PinchZoom = ({ children }: { children: React.ReactNode }) => {
  const [scale, setScale] = useState(1);
  const [origin, setOrigin] = useState({ x: 0, y: 0 });
  const initialDistance = useRef(0);
  const initialScale = useRef(1);

  const getDistance = (touches: TouchList) => {
    const [a, b] = [touches[0], touches[1]];
    return Math.hypot(b.clientX - a.clientX, b.clientY - a.clientY);
  };

  return (
    <motion.div
      onTouchStart={(e) => {
        if (e.touches.length === 2) {
          initialDistance.current = getDistance(e.touches);
          initialScale.current = scale;
          const midX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
          const midY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
          setOrigin({ x: midX, y: midY });
        }
      }}
      onTouchMove={(e) => {
        if (e.touches.length === 2) {
          const newDist = getDistance(e.touches);
          const newScale = Math.max(0.5, Math.min(4, initialScale.current * (newDist / initialDistance.current)));
          setScale(newScale);
        }
      }}
      animate={{ scale }}
      transition={{ type: "spring", stiffness: 300, damping: 25 }}
      style={{ transformOrigin: `${origin.x}px ${origin.y}px`, touchAction: "none" }}
    >
      {children}
    </motion.div>
  );
};
```

### Recipe 32: Double-Tap to Zoom
```tsx
export const DoubleTapZoom = ({ children }: { children: React.ReactNode }) => {
  const [zoomed, setZoomed] = useState(false);
  const lastTap = useRef(0);

  const handleTap = () => {
    const now = Date.now();
    if (now - lastTap.current < 300) {
      setZoomed(!zoomed);
    }
    lastTap.current = now;
  };

  return (
    <motion.div
      onClick={handleTap}
      animate={{ scale: zoomed ? 2 : 1 }}
      transition={{ type: "spring", stiffness: 300, damping: 25 }}
      style={{ cursor: "zoom-in" }}
    >
      {children}
    </motion.div>
  );
};
```

### Recipe 33: Swipe Navigation (carousel)
```tsx
export const SwipeCarousel = ({ slides }: { slides: React.ReactNode[] }) => {
  const [current, setCurrent] = useState(0);
  const x = useMotionValue(0);

  return (
    <div style={{ overflow: "hidden" }}>
      <motion.div
        drag="x"
        dragConstraints={{ left: 0, right: 0 }}
        style={{ x, display: "flex" }}
        animate={{ x: -current * 100 + "%" }}
        onDragEnd={(_, info) => {
          if (info.velocity.x < -500 && current < slides.length - 1) setCurrent(current + 1);
          else if (info.velocity.x > 500 && current > 0) setCurrent(current - 1);
          else {
            const threshold = window.innerWidth * 0.3;
            if (info.offset.x < -threshold && current < slides.length - 1) setCurrent(current + 1);
            else if (info.offset.x > threshold && current > 0) setCurrent(current - 1);
          }
        }}
        transition={{ type: "spring", stiffness: 300, damping: 30 }}
      >
        {slides.map((slide, i) => (
          <div key={i} style={{ flex: "0 0 100%", minWidth: "100%" }}>{slide}</div>
        ))}
      </motion.div>
    </div>
  );
};
```

### Recipe 34: Drag Handle with Snap Points
```tsx
export const SnapDrawer = ({ snapPoints = [0, 50, 100] }: { snapPoints?: number[] }) => {
  const y = useMotionValue(0);

  const findClosestSnap = (offset: number) => {
    const vh = window.innerHeight;
    const snapPositions = snapPoints.map(p => (p / 100) * vh);
    return snapPositions.reduce((prev, curr) =>
      Math.abs(curr - offset) < Math.abs(prev - offset) ? curr : prev
    );
  };

  return (
    <motion.div
      drag="y"
      dragConstraints={{ top: 0, bottom: window.innerHeight }}
      dragElastic={0.2}
      style={{ y }}
      onDragEnd={(_, info) => {
        const snap = findClosestSnap(info.point.y);
        y.set(snap); // In practice, use animate()
      }}
      transition={{ type: "spring", stiffness: 300, damping: 30 }}
    >
      <div style={{ width: 32, height: 4, background: "#d1d5db", borderRadius: 2,
        margin: "8px auto" }} />
    </motion.div>
  );
};
```

---

## Part 5: Scroll Snap Patterns (CSS)

### Recipe 35: Vertical Full-Page Scroll Snap
```css
.snap-container {
  height: 100vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
  -webkit-overflow-scrolling: touch;
}

.snap-section {
  height: 100vh;
  scroll-snap-align: start;
  scroll-snap-stop: always;
}
```

### Recipe 36: Horizontal Card Carousel Snap
```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 16px;
  padding: 16px;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}

.carousel::-webkit-scrollbar { display: none; }

.carousel-card {
  scroll-snap-align: center;
  flex: 0 0 calc(80% - 16px);
  border-radius: 12px;
}

@media (min-width: 768px) {
  .carousel-card {
    flex: 0 0 calc(33.333% - 16px);
  }
}
```

### Recipe 37: Gallery with Snap and Indicators
```css
.gallery {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
}

.gallery-slide {
  scroll-snap-align: start;
  flex: 0 0 100%;
}

/* JS tracks scroll position for indicators */
```

```js
const gallery = document.querySelector('.gallery');
const dots = document.querySelectorAll('.gallery-dot');

gallery.addEventListener('scroll', () => {
  const index = Math.round(gallery.scrollLeft / gallery.offsetWidth);
  dots.forEach((dot, i) => dot.classList.toggle('is-active', i === index));
}, { passive: true });
```

---

## Part 6: Performance Tips for Scroll Animations

### Use `will-change` Sparingly
```css
/* Only on elements about to animate */
.will-animate { will-change: transform, opacity; }
.done-animating { will-change: auto; }
```

### Use `content-visibility` for Long Pages
```css
.offscreen-section {
  content-visibility: auto;
  contain-intrinsic-size: 0 600px;
}
```

### Passive Event Listeners
```js
// Always use passive for scroll events
window.addEventListener("scroll", handler, { passive: true });
```

### Throttle with requestAnimationFrame
```js
let ticking = false;
window.addEventListener("scroll", () => {
  if (!ticking) {
    requestAnimationFrame(() => {
      updateAnimation();
      ticking = false;
    });
    ticking = true;
  }
}, { passive: true });
```

### Prefer CSS Scroll-Driven Over JS
CSS scroll-driven animations run on the compositor thread and cannot cause jank. Always prefer them when browser support allows, with Intersection Observer as a fallback.
