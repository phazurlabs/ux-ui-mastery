# Glassmorphism & Modern CSS Visual Effects — 25+ Production Recipes

## Visual Effects Philosophy

Modern UI design has moved beyond flat surfaces and basic shadows. Glassmorphism, blur effects, gradient treatments, noise textures, and blend modes create dimensional, layered interfaces that feel alive. These effects serve function — they communicate depth, focus attention, and establish visual hierarchy.

**The cardinal rule:** Effects must serve the interface. A frosted glass navbar communicates "I float above content." A gradient background creates ambient energy. Noise texture prevents banding. If an effect does not communicate or solve, it is decoration.

---

## Glassmorphism Fundamentals

Glassmorphism creates the illusion of a semi-transparent, frosted glass surface floating above background content. The three required ingredients are:

1. **Semi-transparent background:** `background: rgba(255, 255, 255, 0.6)` — the "glass" tint
2. **Backdrop blur:** `backdrop-filter: blur(12px)` — the "frosted" effect
3. **Subtle border:** `border: 1px solid rgba(255, 255, 255, 0.2)` — the edge catch-light

```css
.glass-basic {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px); /* Safari */
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
}
```

### Glassmorphism Quality Factors

- **Blur radius:** 8-24px. Lower = more visible background content. Higher = more opaque feel.
- **Background opacity:** 0.3-0.8. Lower = more transparent. Higher = more readable text.
- **Border opacity:** 0.1-0.3. Creates the light-catching edge that sells the glass illusion.
- **Background content matters:** Glassmorphism looks best over colorful, varied backgrounds. Over a solid white background, it is invisible and pointless.

---

## Recipe 1: Frosted Glass Card (Apple Style)

The signature Apple aesthetic — a clean frosted panel with soft edges.

```css
.glass-card-apple {
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border: 0.5px solid rgba(255, 255, 255, 0.4);
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.06);
  padding: 24px;
}

/* Dark mode variant */
.dark .glass-card-apple {
  background: rgba(30, 30, 30, 0.72);
  border: 0.5px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
}
```

**Key detail:** `saturate(180%)` boosts the color saturation of the blurred background content, preventing the washed-out look that pure blur creates. This is Apple's secret to vibrant frosted glass.

---

## Recipe 2: Acrylic Material (Windows / Fluent Design)

Microsoft's Fluent Design uses a noise layer on top of blur to create the "acrylic" material texture.

```css
.acrylic-material {
  position: relative;
  background: rgba(255, 255, 255, 0.65);
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

/* Noise texture overlay */
.acrylic-material::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  background-size: 256px 256px;
  pointer-events: none;
  mix-blend-mode: overlay;
}

/* Dark variant */
.dark .acrylic-material {
  background: rgba(0, 0, 0, 0.6);
}
.dark .acrylic-material::after {
  opacity: 0.06;
}
```

---

## Recipe 3: Glassmorphic Navigation Bar

A floating navbar that blurs the page content scrolling behind it.

```css
.glass-navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: var(--z-sticky);
  height: 64px;
  display: flex;
  align-items: center;
  padding: 0 24px;

  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

/* Transition: solid when at top, glass when scrolled */
.glass-navbar--top {
  background: transparent;
  backdrop-filter: none;
  -webkit-backdrop-filter: none;
  border-bottom-color: transparent;
  box-shadow: none;
}

/* Dark mode */
.dark .glass-navbar {
  background: rgba(20, 20, 20, 0.75);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}
```

**JavaScript for scroll detection:**
```javascript
const navbar = document.querySelector('.glass-navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('glass-navbar--top', window.scrollY < 10);
}, { passive: true });
```

---

## Recipe 4: Glassmorphic Modal

```css
.glass-modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  z-index: var(--z-modal-backdrop);
}

.glass-modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: var(--z-modal);
  max-width: 520px;
  width: 90%;
  padding: 32px;

  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(24px) saturate(150%);
  -webkit-backdrop-filter: blur(24px) saturate(150%);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 24px;
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.08),
    0 2px 8px rgba(0, 0, 0, 0.04);
}

/* Dark variant */
.dark .glass-modal {
  background: rgba(30, 30, 30, 0.85);
  border-color: rgba(255, 255, 255, 0.08);
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.4),
    0 0 0 1px rgba(255, 255, 255, 0.04);
}
```

---

## Recipe 5: Glassmorphic Sidebar

```css
.glass-sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 280px;
  z-index: var(--z-fixed);
  padding: 20px 12px;
  overflow-y: auto;

  background: rgba(245, 245, 245, 0.6);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-right: 1px solid rgba(0, 0, 0, 0.06);
}

.dark .glass-sidebar {
  background: rgba(20, 20, 20, 0.65);
  border-right-color: rgba(255, 255, 255, 0.06);
}
```

---

## Recipe 6: Frosted Glass Input

```css
.glass-input {
  height: 44px;
  padding: 0 16px;
  font-size: 15px;
  color: var(--color-text-primary);

  background: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 12px;
  outline: none;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

.glass-input:focus {
  border-color: rgba(var(--primary-rgb), 0.5);
  box-shadow: 0 0 0 3px rgba(var(--primary-rgb), 0.15);
}

.glass-input::placeholder {
  color: rgba(0, 0, 0, 0.35);
}

.dark .glass-input {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.1);
}
.dark .glass-input::placeholder {
  color: rgba(255, 255, 255, 0.3);
}
```

---

## Recipe 7: Gradient Mesh Background

Creates a rich, multi-colored background using layered radial gradients. Perfect behind glassmorphism elements.

```css
.mesh-background {
  background-color: #0f0c29;
  background-image:
    radial-gradient(at 20% 80%, hsla(210, 100%, 60%, 0.4) 0, transparent 50%),
    radial-gradient(at 80% 20%, hsla(280, 100%, 60%, 0.3) 0, transparent 50%),
    radial-gradient(at 40% 40%, hsla(180, 100%, 50%, 0.25) 0, transparent 50%),
    radial-gradient(at 70% 70%, hsla(340, 100%, 60%, 0.2) 0, transparent 50%);
  min-height: 100vh;
}

/* Animated variant */
.mesh-background-animated {
  background-size: 200% 200%;
  animation: mesh-shift 20s ease infinite;
}

@keyframes mesh-shift {
  0%, 100% { background-position: 0% 50%; }
  25% { background-position: 100% 0%; }
  50% { background-position: 100% 100%; }
  75% { background-position: 0% 100%; }
}
```

---

## Recipe 8: Gradient Border

A border that uses a gradient instead of a solid color. Achieved via background-clip or a pseudo-element.

```css
/* Method 1: Background-clip technique */
.gradient-border {
  position: relative;
  background: var(--surface-default);
  border-radius: 16px;
  padding: 24px;
}
.gradient-border::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px; /* Border width */
  background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
  -webkit-mask:
    linear-gradient(#fff 0 0) content-box,
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

/* Method 2: border-image (simpler, no border-radius support) */
.gradient-border-simple {
  border: 2px solid;
  border-image: linear-gradient(135deg, #667eea, #764ba2) 1;
}

/* Method 3: Background with padding (works with border-radius) */
.gradient-border-bg {
  background: linear-gradient(var(--surface-default), var(--surface-default)) padding-box,
              linear-gradient(135deg, #667eea, #764ba2, #f093fb) border-box;
  border: 1px solid transparent;
  border-radius: 16px;
}
```

---

## Recipe 9: Glow Effect (Neon)

Colored glow around an element, using box-shadow or drop-shadow.

```css
.neon-glow {
  box-shadow:
    0 0 5px rgba(var(--primary-rgb), 0.3),
    0 0 20px rgba(var(--primary-rgb), 0.2),
    0 0 40px rgba(var(--primary-rgb), 0.1);
  border: 1px solid rgba(var(--primary-rgb), 0.3);
}

/* Animated pulse glow */
.neon-glow-pulse {
  animation: glow-pulse 2s ease-in-out infinite alternate;
}
@keyframes glow-pulse {
  from {
    box-shadow:
      0 0 5px rgba(var(--primary-rgb), 0.2),
      0 0 20px rgba(var(--primary-rgb), 0.1);
  }
  to {
    box-shadow:
      0 0 10px rgba(var(--primary-rgb), 0.4),
      0 0 40px rgba(var(--primary-rgb), 0.2),
      0 0 80px rgba(var(--primary-rgb), 0.1);
  }
}

/* Text neon glow */
.neon-text {
  color: #fff;
  text-shadow:
    0 0 7px rgba(var(--primary-rgb), 0.8),
    0 0 20px rgba(var(--primary-rgb), 0.4),
    0 0 40px rgba(var(--primary-rgb), 0.2);
}
```

---

## Recipe 10: Noise / Grain Texture Overlay

Adds subtle analog texture to surfaces. Reduces color banding on gradients and adds visual warmth.

```css
/* SVG-based noise (inline, no external file) */
.noise-overlay {
  position: relative;
}
.noise-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  opacity: 0.03;
  pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
  background-size: 256px 256px;
}

/* Heavier noise for editorial/artistic effect */
.noise-overlay-heavy::after {
  opacity: 0.08;
  mix-blend-mode: overlay;
}

/* Film grain effect (animated) */
.film-grain::after {
  content: '';
  position: absolute;
  inset: -50%;
  width: 200%;
  height: 200%;
  opacity: 0.04;
  pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 512 512' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='grain'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23grain)'/%3E%3C/svg%3E");
  background-size: 256px 256px;
  animation: grain-shift 0.5s steps(5) infinite;
}
@keyframes grain-shift {
  0%, 100% { transform: translate(0, 0); }
  20% { transform: translate(-2%, 3%); }
  40% { transform: translate(3%, -1%); }
  60% { transform: translate(-3%, 2%); }
  80% { transform: translate(2%, -3%); }
}
```

---

## Recipe 11: CSS Filter Effects for UI

```css
/* Brightness on hover */
.filter-brightness:hover {
  filter: brightness(1.05);
}

/* Darken overlay effect without pseudo-element */
.filter-darken {
  filter: brightness(0.85);
}

/* Saturate on hover for image cards */
.image-card {
  filter: saturate(0.9);
  transition: filter 0.3s ease;
}
.image-card:hover {
  filter: saturate(1.1);
}

/* Grayscale to color transition */
.grayscale-hover {
  filter: grayscale(100%);
  transition: filter 0.4s ease;
}
.grayscale-hover:hover {
  filter: grayscale(0%);
}

/* Disabled state via filter */
.disabled-filter {
  filter: grayscale(100%) opacity(0.5);
  pointer-events: none;
}

/* Sepia vintage effect */
.vintage {
  filter: sepia(20%) contrast(1.05) brightness(1.02);
}
```

---

## Recipe 12: Blend Modes for Overlays

```css
/* Dark overlay with multiply */
.overlay-dark {
  position: relative;
}
.overlay-dark::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  mix-blend-mode: multiply;
  pointer-events: none;
}

/* Color tint overlay */
.overlay-tint::before {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--color-primary);
  mix-blend-mode: color;
  opacity: 0.3;
  pointer-events: none;
}

/* Screen blend for lightening */
.overlay-light::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(255,255,255,0.8), transparent);
  mix-blend-mode: screen;
  pointer-events: none;
}

/* Duotone image effect */
.duotone {
  position: relative;
  filter: grayscale(100%) contrast(1.2);
}
.duotone::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #667eea, #764ba2);
  mix-blend-mode: color;
  pointer-events: none;
}
```

---

## Recipe 13: Animated Gradient Background

```css
.gradient-animated {
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
  background-size: 400% 400%;
  animation: gradient-flow 15s ease infinite;
}

@keyframes gradient-flow {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Subtle version for backgrounds */
.gradient-animated-subtle {
  background: linear-gradient(-45deg, #f8f9fa, #e9ecef, #f1f3f5, #dee2e6);
  background-size: 400% 400%;
  animation: gradient-flow 30s ease infinite;
}
```

---

## Recipe 14: Conic Gradient Effects

```css
/* Color wheel */
.color-wheel {
  background: conic-gradient(
    hsl(0, 80%, 60%),
    hsl(60, 80%, 60%),
    hsl(120, 80%, 60%),
    hsl(180, 80%, 60%),
    hsl(240, 80%, 60%),
    hsl(300, 80%, 60%),
    hsl(360, 80%, 60%)
  );
  border-radius: 50%;
}

/* Spotlight / pie effect */
.spotlight {
  background: conic-gradient(
    from 180deg at 50% 70%,
    transparent 0deg,
    rgba(var(--primary-rgb), 0.1) 90deg,
    transparent 180deg
  );
}

/* Gauge progress indicator */
.gauge {
  --progress: 75%;
  background: conic-gradient(
    var(--color-primary) calc(var(--progress) * 3.6deg),
    var(--color-border-subtle) calc(var(--progress) * 3.6deg)
  );
  border-radius: 50%;
  position: relative;
}
.gauge::after {
  content: '';
  position: absolute;
  inset: 8px;
  background: var(--surface-default);
  border-radius: 50%;
}
```

---

## Recipe 15: Inner Glow / Light Effect

```css
/* Top inner glow (simulates overhead light reflection) */
.inner-glow-top {
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

/* Full inner glow */
.inner-glow {
  box-shadow:
    inset 0 0 20px rgba(255, 255, 255, 0.05),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

/* Radial inner glow (spotlight) */
.inner-spotlight {
  background:
    radial-gradient(ellipse at 50% 0%, rgba(255,255,255,0.15) 0%, transparent 60%),
    var(--surface-default);
}

/* Pressed / recessed surface */
.recessed {
  box-shadow:
    inset 0 2px 4px rgba(0, 0, 0, 0.1),
    inset 0 1px 2px rgba(0, 0, 0, 0.06);
  background: var(--surface-subtle);
}
```

---

## Recipe 16: Shimmer / Skeleton Loading

```css
.shimmer {
  background: linear-gradient(
    90deg,
    var(--surface-subtle) 0%,
    var(--surface-raised) 40%,
    var(--surface-subtle) 80%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
  border-radius: var(--radius-md);
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Skeleton shapes */
.skeleton-text { height: 14px; margin-bottom: 8px; }
.skeleton-title { height: 24px; width: 60%; margin-bottom: 16px; }
.skeleton-avatar { width: 40px; height: 40px; border-radius: 50%; }
.skeleton-image { width: 100%; aspect-ratio: 16/9; }
```

---

## Recipe 17: Frosted Glass Tooltip

```css
.glass-tooltip {
  padding: 8px 12px;
  font-size: 13px;
  color: #fff;
  background: rgba(15, 15, 15, 0.8);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  pointer-events: none;
  z-index: var(--z-tooltip);
}

/* Arrow */
.glass-tooltip::before {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%) rotate(45deg);
  width: 10px;
  height: 10px;
  background: rgba(15, 15, 15, 0.8);
  border-right: 1px solid rgba(255, 255, 255, 0.08);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}
```

---

## Recipe 18: Glass Command Palette / Spotlight Search

```css
.command-palette {
  position: fixed;
  top: 20%;
  left: 50%;
  transform: translateX(-50%);
  width: min(600px, 90vw);
  z-index: var(--z-command-palette);

  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(24px) saturate(150%);
  -webkit-backdrop-filter: blur(24px) saturate(150%);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 16px;
  box-shadow:
    0 16px 70px rgba(0, 0, 0, 0.12),
    0 0 0 1px rgba(0, 0, 0, 0.04);
  overflow: hidden;
}

.command-palette-input {
  width: 100%;
  padding: 16px 20px;
  font-size: 18px;
  border: none;
  background: transparent;
  outline: none;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}

.command-palette-results {
  max-height: 400px;
  overflow-y: auto;
  padding: 8px;
}

.command-palette-item {
  padding: 10px 12px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}

.command-palette-item:hover,
.command-palette-item[aria-selected="true"] {
  background: rgba(0, 0, 0, 0.04);
}

/* Dark variant */
.dark .command-palette {
  background: rgba(25, 25, 25, 0.88);
  border-color: rgba(255, 255, 255, 0.08);
  box-shadow:
    0 16px 70px rgba(0, 0, 0, 0.5),
    0 0 0 1px rgba(255, 255, 255, 0.04);
}
.dark .command-palette-input {
  border-bottom-color: rgba(255, 255, 255, 0.06);
  color: #fff;
}
.dark .command-palette-item:hover {
  background: rgba(255, 255, 255, 0.06);
}
```

---

## Recipe 19: Holographic / Iridescent Effect

```css
.holographic {
  position: relative;
  overflow: hidden;
}
.holographic::before {
  content: '';
  position: absolute;
  inset: -50%;
  background: conic-gradient(
    from 0deg,
    #ff6b6b33,
    #feca5733,
    #48dbfb33,
    #ff9ff333,
    #54a0ff33,
    #5f27cd33,
    #ff6b6b33
  );
  animation: holo-rotate 6s linear infinite;
  mix-blend-mode: overlay;
  pointer-events: none;
}

@keyframes holo-rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Static holographic gradient */
.holographic-static {
  background: linear-gradient(
    135deg,
    #667eea20 0%,
    #764ba220 25%,
    #f093fb20 50%,
    #5ee7df20 75%,
    #667eea20 100%
  );
  border: 1px solid rgba(255, 255, 255, 0.2);
}
```

---

## Recipe 20: Floating Card with Reflection

```css
.floating-card-reflect {
  padding: 24px;
  background: var(--surface-default);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  position: relative;
}

/* Reflection below card */
.floating-card-reflect::after {
  content: '';
  position: absolute;
  left: 10%;
  right: 10%;
  bottom: -12px;
  height: 12px;
  background: radial-gradient(
    ellipse at center,
    rgba(0, 0, 0, 0.08) 0%,
    transparent 70%
  );
  filter: blur(4px);
  pointer-events: none;
}
```

---

## Recipe 21: Frosted Glass Notification Badge

```css
.glass-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 24px;
  height: 24px;
  padding: 0 8px;
  font-size: 12px;
  font-weight: 600;
  color: #fff;
  background: rgba(239, 68, 68, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-radius: 9999px;
  border: 1.5px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 2px 8px rgba(239, 68, 68, 0.25);
}
```

---

## Recipe 22: Ambient Light / Orb Effect

Decorative glowing orbs that create ambient atmosphere behind glassmorphism panels.

```css
.ambient-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.5;
  pointer-events: none;
}
.ambient-orb--primary {
  width: 400px;
  height: 400px;
  background: var(--color-primary);
  top: -100px;
  right: -100px;
}
.ambient-orb--secondary {
  width: 300px;
  height: 300px;
  background: #f093fb;
  bottom: -80px;
  left: -80px;
}
.ambient-orb--accent {
  width: 250px;
  height: 250px;
  background: #5ee7df;
  top: 40%;
  left: 30%;
}

/* Animated floating orbs */
.ambient-orb--animated {
  animation: orb-float 20s ease-in-out infinite;
}
@keyframes orb-float {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33% { transform: translate(30px, -20px) scale(1.05); }
  66% { transform: translate(-20px, 15px) scale(0.95); }
}
```

---

## Recipe 23: CSS Houdini Paint Worklet Gradient (Progressive Enhancement)

```css
/* Modern browsers with Houdini support */
@supports (background: paint(something)) {
  .houdini-gradient {
    --gradient-color1: #667eea;
    --gradient-color2: #764ba2;
    --gradient-seed: 42;
    background: paint(smooth-gradient);
  }
}

/* Fallback */
@supports not (background: paint(something)) {
  .houdini-gradient {
    background: linear-gradient(135deg, #667eea, #764ba2);
  }
}
```

---

## Recipe 24: Depth Blur (Tilt-Shift)

Blurs the edges of a container to create a depth-of-field effect.

```css
.depth-blur {
  position: relative;
  overflow: hidden;
}
.depth-blur::before,
.depth-blur::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  height: 80px;
  pointer-events: none;
  z-index: 1;
}
.depth-blur::before {
  top: 0;
  background: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 0.9),
    transparent
  );
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  mask-image: linear-gradient(to bottom, black, transparent);
  -webkit-mask-image: linear-gradient(to bottom, black, transparent);
}
.depth-blur::after {
  bottom: 0;
  background: linear-gradient(
    to top,
    rgba(255, 255, 255, 0.9),
    transparent
  );
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  mask-image: linear-gradient(to top, black, transparent);
  -webkit-mask-image: linear-gradient(to top, black, transparent);
}
```

---

## Recipe 25: Glass Morphism Toggle / Switch

```css
.glass-toggle {
  position: relative;
  width: 52px;
  height: 32px;
  border-radius: 16px;
  border: none;
  cursor: pointer;
  padding: 0;

  background: rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: background 0.2s ease;
}
.glass-toggle[aria-checked="true"] {
  background: rgba(var(--primary-rgb), 0.6);
}
.glass-toggle::after {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(4px);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}
.glass-toggle[aria-checked="true"]::after {
  transform: translateX(20px);
}
```

---

## Performance Considerations for Visual Effects

### Backdrop-filter Performance

`backdrop-filter` is expensive. Each element using it:
1. Creates a new stacking context
2. Requires the browser to composite the area behind the element
3. Must re-render whenever the background content changes (e.g., scrolling)

**Performance budget:** Limit to 2-3 elements with `backdrop-filter` visible simultaneously.

**Optimization strategies:**
```css
/* Only apply blur when element is visible */
.glass-element {
  backdrop-filter: none; /* Default: off */
  will-change: backdrop-filter; /* Hint for upcoming change */
}
.glass-element.is-visible {
  backdrop-filter: blur(16px);
}

/* Reduce blur radius on mobile */
@media (max-width: 768px) {
  .glass-element {
    backdrop-filter: blur(8px); /* Lower blur = cheaper */
  }
}

/* Prefer lower blur values when many glass elements are present */
@media (prefers-reduced-motion: reduce) {
  .glass-element {
    backdrop-filter: none;
    background: rgba(255, 255, 255, 0.9); /* Opaque fallback */
  }
}
```

### Fallback Strategy

```css
/* Feature detection for backdrop-filter */
.glass {
  /* Fallback: opaque background */
  background: rgba(255, 255, 255, 0.95);
}

@supports (backdrop-filter: blur(1px)) {
  .glass {
    background: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(16px);
  }
}

/* Safari-specific fallback */
@supports (-webkit-backdrop-filter: blur(1px)) and (not (backdrop-filter: blur(1px))) {
  .glass {
    background: rgba(255, 255, 255, 0.6);
    -webkit-backdrop-filter: blur(16px);
  }
}
```

### Browser Support Summary (2025-2026)

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| `backdrop-filter` | 76+ | 103+ | 9+ (-webkit) | 79+ |
| `filter` | 53+ | 35+ | 9.1+ | 79+ |
| `mix-blend-mode` | 41+ | 32+ | 8+ | 79+ |
| CSS `color-mix()` | 111+ | 113+ | 16.2+ | 111+ |
| `@supports` | 28+ | 22+ | 9+ | 79+ |

Firefox was the last major browser to support `backdrop-filter` (version 103). As of 2025-2026, support is effectively universal for modern browsers. Always include `-webkit-backdrop-filter` for Safari compatibility.
