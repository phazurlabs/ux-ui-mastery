---
name: image-media-patterns
description: "Image, video, and media UI patterns: hero and product imagery, galleries, carousels, video and audio players, avatars, thumbnails, aspect ratios, cropping, lazy loading, responsive images, and media accessibility. Use when placing media on a page or building a gallery or player."
---

# Image & Media Patterns — Complete Visual Media System

A comprehensive reference for every image, video, audio, and media UI pattern used in modern product design. Covers fundamentals, responsive strategies, performance optimization, gallery/carousel patterns, media players, avatars, upload flows, accessibility, and CSS techniques.

---

## 1. Image Fundamentals: Aspect Ratios

### Standard Aspect Ratios

| Ratio | Decimal | Primary Use Cases | CSS | Common Resolutions |
|-------|---------|-------------------|-----|--------------------|
| 1:1 | 1.0 | Avatar, social post, thumbnail, album art | `aspect-ratio: 1` | 150x150, 300x300, 600x600, 1080x1080 |
| 4:3 | 1.33 | Card thumbnail, classic photo, presentation | `aspect-ratio: 4/3` | 640x480, 800x600, 1024x768, 1600x1200 |
| 3:2 | 1.5 | Photography, editorial card, DSLR native | `aspect-ratio: 3/2` | 720x480, 1080x720, 1440x960, 2160x1440 |
| 16:9 | 1.78 | Video, hero banner, YouTube, widescreen | `aspect-ratio: 16/9` | 1280x720, 1920x1080, 2560x1440, 3840x2160 |
| 21:9 | 2.33 | Cinematic hero, ultra-wide monitor, film | `aspect-ratio: 21/9` | 2560x1080, 3440x1440, 5120x2160 |
| 9:16 | 0.56 | Stories, Reels, TikTok, mobile-first vertical | `aspect-ratio: 9/16` | 1080x1920, 720x1280 |
| 2:3 | 0.67 | Portrait photography, Pinterest pin, book cover | `aspect-ratio: 2/3` | 800x1200, 1000x1500 |
| 5:4 | 1.25 | Large format photography, Instagram landscape | `aspect-ratio: 5/4` | 1080x864, 1350x1080 |
| 4:5 | 0.8 | Instagram portrait, product photo | `aspect-ratio: 4/5` | 1080x1350 |

### When to Use Each Ratio

- **1:1** — Best for avatars, product thumbnails in grids, social media posts (Instagram square). Creates visual uniformity in grid layouts. Use when you need perfect symmetry.
- **4:3** — Traditional screen ratio. Good for card images, dashboards, thumbnail grids. Slightly taller than 3:2, giving more vertical space for subjects.
- **3:2** — The "golden ratio" of photography. Native to most DSLR sensors. Ideal for editorial content, photo galleries, hero cards. Feels natural and balanced.
- **16:9** — Standard widescreen. Required for video content. Use for hero banners, featured content sections, video thumbnails. The default for YouTube, Vimeo, streaming platforms.
- **21:9** — Cinematic ultra-wide. Use sparingly for dramatic hero sections, landing page headers, film-related content. Creates strong horizontal emphasis.
- **9:16** — Vertical mobile-first format. Essential for Stories (Instagram, Snapchat), Reels, TikTok, mobile fullscreen experiences. Dominant in short-form social video.
- **4:5** — Instagram's preferred portrait format. Occupies maximum screen real estate on mobile feeds. Great for product photography.

### Platform-Specific Conventions

| Platform | Feed Image | Story/Reel | Profile Photo | Cover/Banner |
|----------|-----------|------------|---------------|-------------|
| Instagram | 1:1, 4:5 | 9:16 | 1:1 (320px) | N/A |
| TikTok | 9:16 | 9:16 | 1:1 | N/A |
| YouTube | 16:9 | 9:16 (Shorts) | 1:1 (800px) | 16:9 (2560x1440) |
| Twitter/X | 16:9, 2:1 | N/A | 1:1 (400px) | 3:1 (1500x500) |
| LinkedIn | 1.91:1 | N/A | 1:1 (400px) | 4:1 (1584x396) |
| Facebook | 1.91:1, 1:1 | 9:16 | 1:1 (170px) | 2.63:1 (820x312) |
| Pinterest | 2:3 | 9:16 (Idea Pin) | 1:1 | N/A |
| Open Graph | 1.91:1 (1200x630) | N/A | N/A | N/A |

---

## 2. Image Display Patterns (18 Patterns)

### 2.1 Object-Fit Modes

| Mode | Behavior | Use Case |
|------|----------|----------|
| `cover` | Fill container, crop excess, maintain ratio | Hero images, card thumbnails, backgrounds |
| `contain` | Fit inside container, show all content, may letterbox | Product images, logos, diagrams |
| `fill` | Stretch to fill, ignores ratio | Rare — background textures only |
| `scale-down` | Like `contain` but never enlarges | User-uploaded images of unknown size |
| `none` | Natural size, may overflow | Sprites, pixel-art |

### 2.2 Hero Image

Full-width image spanning the viewport or content area. Typically the first visual element on a page.

- **Full-bleed hero**: Edge-to-edge, no margins. Use `width: 100vw` with negative margin or grid breakout.
- **Contained hero**: Within max-width container (1200-1440px). Safer for text overlay readability.
- **Split hero**: Image on one side, text on the other. 50/50 or 60/40 split.
- **Gradient overlay hero**: Image with linear-gradient overlay for text contrast. `linear-gradient(to top, rgba(0,0,0,0.7) 0%, transparent 60%)`.
- **Video hero**: Autoplay muted looping video replacing static image. See Video Patterns section.
- **Parallax hero**: Background-attachment: fixed or JS-driven parallax scroll effect.

Design specs: Min height 50vh (mobile) to 70vh (desktop). Text overlay needs minimum 4.5:1 contrast. Always provide a solid color fallback behind the image.

### 2.3 Card Thumbnail

Image at the top or side of a card component.

- **Top image card**: Image fills card width, fixed aspect ratio (3:2 or 16:9), content below.
- **Side image card**: Image on left (120-200px wide), content on right. Good for list views.
- **Background image card**: Image fills entire card, text overlaid with gradient scrim.
- **Inset image card**: Image with padding inside card, rounded corners. Softer feel.

Always use `object-fit: cover` with a fixed aspect-ratio container. Never let card images distort.

### 2.4 Avatar

Circular or rounded-square image representing a user. See dedicated Avatar Patterns section below for full spec.

### 2.5 Profile Banner / Cover Photo

Wide rectangular image behind profile information.

- Typical ratio: 3:1 to 4:1 (very wide and short).
- Avatar overlaps banner bottom edge by 30-50%.
- Mobile: banner crops center; provide focal-point metadata if possible.
- Upload guidelines: minimum 1500px wide, suggest 1500x500 or 1584x396.

### 2.6 Product Image

Primary e-commerce image pattern.

- **Main image**: Large, zoomable, white/neutral background, 1:1 or 4:5 ratio.
- **Thumbnail strip**: 4-8 small thumbnails below/beside main image. Click to swap main. Active thumbnail gets border highlight.
- **Zoom on hover**: CSS transform scale or lens-style magnifier showing 2-3x zoom.
- **360-degree view**: Sequence of images rotated by drag. 24-72 frames for smooth rotation.
- **Model/lifestyle shot**: Product in context. Alternate with white-background shots.

### 2.7 Before/After Comparison

Two images shown side by side with a draggable divider.

- Slider handle: vertical line with drag affordance (arrows or grip dots).
- Both images must be identical dimensions and alignment.
- Use `clip-path: inset(0 50% 0 0)` or `overflow: hidden` with variable width.
- Accessible: provide text descriptions of both states. Keyboard arrow keys should move slider.

### 2.8 Image Comparison (Side by Side)

Two or more images displayed adjacent for visual comparison without a slider.

- Use matching aspect ratios and identical container sizes.
- Label each image clearly (A/B, Before/After, Option 1/2).
- On mobile: stack vertically rather than side-by-side.

### 2.9 Zoomed Crop / Detail View

Close-up crop of a larger image to highlight detail.

- Show outline on the source image indicating the crop region.
- Display zoomed version in a separate panel or overlay.
- Common in e-commerce (fabric texture), medical imaging, maps.

### 2.10 Tilt / Parallax Image

Image that responds to scroll position or mouse/device movement.

- **Scroll parallax**: `background-attachment: fixed` (CSS only, limited mobile support) or JS-calculated `transform: translateY()` based on scroll offset.
- **Mouse parallax**: Track cursor position, apply `transform: translate3d()` with dampened values.
- **Device tilt**: Use `DeviceOrientationEvent` for mobile gyroscope-driven parallax.
- Performance: Use `will-change: transform`. Avoid parallax on elements that trigger layout shifts.

### 2.11 Ken Burns Effect

Slow zoom and pan animation on a static image, creating cinematic movement.

```css
@keyframes ken-burns {
  0% { transform: scale(1) translate(0, 0); }
  100% { transform: scale(1.15) translate(-2%, -1%); }
}
.ken-burns-image {
  animation: ken-burns 20s ease-in-out infinite alternate;
  object-fit: cover;
  width: 100%;
  height: 100%;
}
```

Use for hero sections, storytelling pages, memorial/tribute content. Always respect `prefers-reduced-motion`.

### 2.12 Image with Hotspots

Interactive image with clickable/tappable markers revealing tooltips or details.

- Markers: numbered dots, plus icons, or pulsing circles.
- Position markers with percentage-based absolute positioning.
- On click/tap: show popover with text, link, or nested image.
- Use case: product feature callouts, interactive infographics, floor plans.

### 2.13 Full-Bleed / Edge-to-Edge

Image spanning the full viewport width, breaking out of content container.

```css
.full-bleed {
  width: 100vw;
  margin-left: calc(50% - 50vw);
}
```

### 2.14 Image with Caption

Image paired with descriptive text below or overlaid.

- Use `<figure>` and `<figcaption>` for semantic markup.
- Caption text: 12-14px, secondary color, max-width matching image.
- Attribution line: photographer credit, source link.

### 2.15 Rounded / Shaped Image

Images cropped to non-rectangular shapes.

- **Circle**: `border-radius: 50%` (requires 1:1 aspect ratio container).
- **Rounded rectangle**: `border-radius: 8-24px` with `overflow: hidden`.
- **Blob/organic shape**: `clip-path: polygon(...)` or SVG mask.
- **Diagonal cut**: `clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%)`.

### 2.16 Image Stack / Collage

Multiple overlapping images creating a layered composition.

- Rotate each image 2-5 degrees with `transform: rotate()`.
- Apply box-shadow for depth: `box-shadow: 0 4px 12px rgba(0,0,0,0.15)`.
- Commonly 3-5 images. Polaroid-style borders optional.

### 2.17 Skeleton / Placeholder Image

Visual placeholder shown while the real image loads.

- **Solid color**: Dominant color extracted from image (server-side).
- **Blur-up (LQIP)**: Tiny (20-40px wide) blurred version, crossfade to full image.
- **BlurHash/ThumbHash**: Compact hash string decoded client-side to gradient placeholder.
- **Skeleton shimmer**: Animated gradient sweep over gray rectangle.
- Always match placeholder dimensions to final image to prevent CLS.

### 2.18 Background Image with Text Overlay

Full or partial background image with readable text on top.

Contrast techniques:
1. Semi-transparent overlay: `background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5))`.
2. Text shadow: `text-shadow: 0 2px 4px rgba(0,0,0,0.5)`.
3. Frosted glass: `backdrop-filter: blur(12px)` on a semi-transparent panel.
4. Scrim gradient: Gradient only where text appears.

Minimum contrast: 4.5:1 for body text, 3:1 for large text (WCAG AA).

---

## 3. Responsive Images

### 3.1 Resolution Switching with srcset

Serve different image sizes based on viewport width or device pixel ratio.

```html
<!-- Width-based srcset (most common) -->
<img
  srcset="photo-480.webp 480w,
          photo-768.webp 768w,
          photo-1200.webp 1200w,
          photo-1920.webp 1920w"
  sizes="(max-width: 600px) 100vw,
         (max-width: 1024px) 50vw,
         33vw"
  src="photo-1200.webp"
  alt="Mountain landscape at sunset"
  loading="lazy"
  width="1200" height="800"
  decoding="async"
>

<!-- DPR-based srcset (for fixed-size images like logos) -->
<img
  srcset="logo.png 1x, logo@2x.png 2x, logo@3x.png 3x"
  src="logo.png"
  alt="Company logo"
  width="200" height="60"
>
```

### 3.2 Art Direction with picture Element

Serve entirely different image crops or compositions at different breakpoints.

```html
<picture>
  <!-- Mobile: tight portrait crop -->
  <source media="(max-width: 639px)" srcset="hero-mobile.avif" type="image/avif">
  <source media="(max-width: 639px)" srcset="hero-mobile.webp" type="image/webp">

  <!-- Tablet: medium crop -->
  <source media="(max-width: 1023px)" srcset="hero-tablet.avif" type="image/avif">
  <source media="(max-width: 1023px)" srcset="hero-tablet.webp" type="image/webp">

  <!-- Desktop: full wide composition -->
  <source srcset="hero-desktop.avif" type="image/avif">
  <source srcset="hero-desktop.webp" type="image/webp">

  <!-- Fallback -->
  <img src="hero-desktop.jpg" alt="Team collaborating in modern office" width="1920" height="800">
</picture>
```

### 3.3 Responsive Image Decision Tree

1. Same image, different sizes? Use `srcset` + `sizes`.
2. Different crops/compositions per breakpoint? Use `<picture>` with `media` queries.
3. Different formats (AVIF/WebP/JPEG fallback)? Use `<picture>` with `type` attribute.
4. Fixed-size image on retina? Use `srcset` with `1x, 2x, 3x`.

---

## 4. Image Formats

### Format Comparison

| Format | Best For | Transparency | Animation | Compression | Browser Support |
|--------|----------|-------------|-----------|-------------|-----------------|
| AVIF | Photos, illustrations | Yes | Yes | Best (30-50% smaller than WebP) | Chrome, Firefox, Safari 16.4+ |
| WebP | Photos, illustrations | Yes | Yes | Great (25-35% smaller than JPEG) | All modern browsers |
| JPEG | Photos (legacy fallback) | No | No | Good | Universal |
| PNG | Screenshots, transparency needed | Yes | No (APNG exists) | Lossless, large files | Universal |
| SVG | Icons, logos, illustrations | Yes | Yes (SMIL/CSS) | Vector, tiny at any size | Universal |
| GIF | Simple animations (legacy) | 1-bit only | Yes | Poor, large files | Universal |
| JPEG XL | Future — photos, lossless | Yes | Yes | Best theoretical | Chrome (behind flag), Safari |

### Quality Settings

| Format | Quality Range | Recommended | Notes |
|--------|--------------|-------------|-------|
| AVIF | 1-100 | 50-65 | Lower numbers are fine, excellent at low quality |
| WebP | 1-100 | 75-85 | Good balance at 80 |
| JPEG | 1-100 | 75-85 | Below 70 shows artifacts on gradients |
| PNG | Lossless | N/A | Use pngquant for lossy compression (60-80%) |

### Format Selection Rule

```
If vector (icon/logo/illustration): SVG
If photo/complex image:
  Serve AVIF (primary) → WebP (fallback) → JPEG (legacy)
If needs transparency + raster:
  WebP or AVIF (prefer over PNG for smaller size)
If simple animation:
  WebP animated or AVIF animated (avoid GIF)
If complex animation:
  Use <video> with MP4/WebM instead
```

---

## 5. Lazy Loading & Placeholders

### 5.1 Native Lazy Loading

```html
<!-- Below-fold images: lazy load -->
<img src="photo.webp" loading="lazy" alt="..." width="800" height="600" decoding="async">

<!-- Above-fold LCP image: eager load with high priority -->
<img src="hero.webp" loading="eager" fetchpriority="high" alt="..." width="1920" height="800">
```

Rules:
- Never lazy-load the LCP (Largest Contentful Paint) image.
- Apply `loading="lazy"` to all images below the initial viewport fold.
- Always pair with explicit `width` and `height` to prevent layout shift.
- Add `decoding="async"` for non-critical images.

### 5.2 Intersection Observer (Custom Lazy Loading)

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      if (img.dataset.srcset) img.srcset = img.dataset.srcset;
      img.classList.add('loaded');
      observer.unobserve(img);
    }
  });
}, { rootMargin: '200px' }); // Start loading 200px before viewport

document.querySelectorAll('img[data-src]').forEach(img => observer.observe(img));
```

### 5.3 Blur-Up / LQIP (Low Quality Image Placeholder)

Technique: Load a tiny (20-40px wide) version of the image, display it blurred and scaled up, then crossfade to the full-resolution image when loaded.

```css
.image-wrapper {
  position: relative;
  overflow: hidden;
}
.lqip {
  filter: blur(20px);
  transform: scale(1.1); /* hide blur edges */
  transition: opacity 0.5s ease;
  position: absolute;
  inset: 0;
  object-fit: cover;
  width: 100%;
  height: 100%;
}
.lqip.loaded { opacity: 0; pointer-events: none; }
```

### 5.4 Dominant Color Placeholder

Extract the dominant color server-side and use it as background while the image loads.

```html
<div style="background-color: #3a7bd5; aspect-ratio: 16/9;">
  <img src="photo.webp" loading="lazy" alt="..." onload="this.style.opacity=1"
       style="opacity: 0; transition: opacity 0.3s; width: 100%; height: 100%; object-fit: cover;">
</div>
```

### 5.5 BlurHash & ThumbHash

- **BlurHash**: Encodes image as a short string (e.g., `LKN]Rv%2Tw=w]~RBVZRi`). Decodes to a blurred gradient. ~20-30 bytes.
- **ThumbHash**: Successor to BlurHash. Preserves more detail, supports transparency. ~28 bytes.
- Both decode client-side to a `<canvas>` element used as placeholder.
- Integrate with image processing pipeline: generate hash at upload, store in database alongside image URL.

---

## 6. Gallery Patterns (12 Patterns)

### 6.1 Masonry Grid

Variable-height items arranged in columns with no row alignment. Items fill vertical space efficiently.

```css
/* CSS Columns approach */
.masonry {
  columns: 3;
  column-gap: 16px;
}
.masonry-item {
  break-inside: avoid;
  margin-bottom: 16px;
}

/* CSS Grid approach (limited masonry — use with caution) */
.masonry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  grid-auto-rows: 10px;
  gap: 16px;
}
/* Each item needs JS-calculated grid-row-end: span N */
```

Responsive breakpoints: 1 column mobile, 2 columns tablet, 3-4 columns desktop.

### 6.2 Justified Grid (Flickr-Style)

All rows have equal width. Image widths vary to fill each row exactly. Heights are uniform per row.

- Requires JS calculation (libraries: justified-layout, react-photo-album).
- Row target height: 200-300px.
- Last row: left-align (don't stretch few images to full width).

### 6.3 Uniform Grid

All images forced to identical dimensions via `object-fit: cover`.

```css
.uniform-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 8px;
}
.uniform-grid img {
  aspect-ratio: 1;
  object-fit: cover;
  width: 100%;
  border-radius: 8px;
}
```

### 6.4 Lightbox

Full-screen overlay showing a single image at maximum size with navigation.

Components: backdrop (black ~90% opacity), image (max-width/max-height constrained), close button (top-right), prev/next arrows, counter ("3 of 12"), caption area.

Accessibility requirements:
- Trap focus within lightbox when open.
- Close on Escape key.
- Navigate with left/right arrow keys.
- `role="dialog"` with `aria-label`.
- Return focus to trigger element on close.

### 6.5 Filmstrip / Thumbnail Strip

Horizontal row of small thumbnails, scrollable. Clicking a thumbnail updates a large main image above.

- Thumbnail size: 60-80px square.
- Active thumbnail: border highlight (2-3px solid primary color).
- Horizontal scroll: CSS `overflow-x: auto`, `scroll-snap-type: x mandatory`.
- Show left/right scroll arrows on desktop if content overflows.

### 6.6 Carousel / Slider

See dedicated Carousel/Slider Patterns section below.

### 6.7 Infinite Scroll Gallery

Images load progressively as user scrolls down. No pagination controls.

- Use Intersection Observer on a sentinel element near the bottom.
- Show loading spinner or skeleton placeholders during fetch.
- Provide "Back to top" button after significant scrolling.
- Preserve scroll position on browser back navigation.
- Accessibility: announce new content loaded via `aria-live="polite"`.

### 6.8 Pinterest-Style Grid

Masonry layout with card-like items containing image + text metadata below.

- Cards: rounded corners (12-16px), subtle shadow on hover.
- Text below image: title (1 line, truncated), source/author.
- Click opens detail view or navigates to source.
- "Save" button overlay on hover (top-right corner of image).

### 6.9 Portfolio Grid

Curated gallery for showcasing work. Often features mixed aspect ratios with intentional layout.

- Featured items span 2 columns or 2 rows.
- Hover effect: overlay with project title, category, and "View" CTA.
- Filter bar above: category pills (All, Branding, Web, Mobile, etc.).
- Animation: stagger fade-in on initial load, layout animation on filter change.

### 6.10 Comparison Slider

Two images overlapping with a draggable vertical divider.

- Handle: vertical line + central drag icon (grip dots or left-right arrows).
- Drag, touch-drag, and keyboard (arrow keys) support.
- Labels: "Before" (left) and "After" (right) text overlays.
- Implementation: two images absolutely positioned, left image clipped with `clip-path` or container width.

### 6.11 Mosaic Grid

Predetermined grid pattern with mixed-size tiles (e.g., one large + four small).

```css
.mosaic {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(2, 200px);
  gap: 8px;
}
.mosaic-featured {
  grid-column: span 2;
  grid-row: span 2;
}
```

### 6.12 Story-Style Gallery

Full-screen vertical slides, one image per "page," swipe/scroll to advance.

- Progress bar at top showing position.
- Tap left/right sides to navigate (mobile).
- Auto-advance timer (5-7 seconds) with pause on hold.
- Used by Instagram Stories, Google AMP Stories.

---

## 7. Carousel / Slider Patterns

### 7.1 Types

| Type | Content | Slides Visible | Use Case |
|------|---------|---------------|----------|
| Image carousel | Photos only | 1 | Hero showcase, product images |
| Content carousel | Cards with text + image | 2-4 | Featured articles, product rows |
| Testimonial carousel | Quote + avatar | 1 | Social proof section |
| Logo carousel | Brand logos | 4-8 | Partner/client logos |
| Story carousel | Full-screen vertical media | 1 | Stories, onboarding |

### 7.2 Navigation Patterns

- **Dots (pagination indicators)**: Show position and total count. Max 7-8 dots before switching to progress bar or "1/12" counter.
- **Arrows (prev/next)**: Left and right arrows at horizontal center of slide. Hide left arrow on first slide (or loop). Minimum tap target: 44x44px.
- **Swipe gestures**: Primary navigation on mobile/touch. Detect horizontal swipe with threshold (30px minimum distance). Add momentum/snap physics.
- **Thumbnail navigation**: Small thumbnails below carousel for direct slide access.
- **Progress bar**: Thin bar showing continuous progress. Good for auto-advancing carousels.

### 7.3 Autoplay Rules

- Default to OFF. Autoplay is an accessibility concern.
- If autoplay is used: provide visible pause/play button.
- Pause on hover (desktop) and on focus (keyboard).
- Pause when page is not visible (`document.hidden`).
- Interval: 5-7 seconds minimum per slide. Never less than 3 seconds.
- Stop autoplay after user manually interacts with navigation.
- Respect `prefers-reduced-motion: reduce` — disable autoplay entirely.

### 7.4 Accessibility Requirements

- Container: `role="region"` with `aria-label="Image carousel"` or descriptive label.
- Each slide: `role="group"` with `aria-roledescription="slide"` and `aria-label="Slide 1 of 5"`.
- Dots/arrows: proper `aria-label` ("Go to slide 3", "Next slide", "Previous slide").
- Keyboard: Tab to reach controls, Enter/Space to activate, arrow keys for slide navigation.
- Live region: `aria-live="polite"` on slide container to announce changes.
- Pause button: Must be keyboard-accessible and have clear label ("Pause slideshow").
- Hidden slides: Use `aria-hidden="true"` and `tabindex="-1"` on non-visible slides.

### 7.5 Mobile Behavior

- Swipe is primary navigation (arrows optional, dots visible).
- Peek next slide: show 10-20px of the next slide edge to hint at scrollability.
- Snap scrolling: `scroll-snap-type: x mandatory` for native-feeling behavior.
- Reduce to 1 visible slide on mobile from 3-4 on desktop.
- Full-width slides on mobile (<640px viewport).

### 7.6 CSS Scroll Snap Carousel

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none; /* Firefox */
}
.carousel::-webkit-scrollbar { display: none; }
.carousel-slide {
  flex: 0 0 100%;
  scroll-snap-align: start;
}
/* Peek variant: show edge of next slide */
.carousel-slide.peek {
  flex: 0 0 calc(100% - 48px);
  margin-right: 8px;
}
```

---

## 8. Avatar Patterns

### 8.1 Size Scale

| Token | Size (px) | Use Case |
|-------|-----------|----------|
| `xs` | 24 | Inline mentions, dense lists, breadcrumbs |
| `sm` | 32 | Comment threads, compact lists, tags |
| `md` | 40 | Standard lists, table rows, chat messages |
| `lg` | 48 | Card headers, detailed lists |
| `xl` | 64 | Profile cards, settings, detailed views |
| `2xl` | 80 | Profile headers, user spotlight |
| `3xl` | 128 | Profile page hero, edit profile, onboarding |

### 8.2 Shapes

- **Circle**: Default for user avatars. `border-radius: 50%`. Requires 1:1 container.
- **Rounded square**: Used by Slack, Discord. `border-radius: 20-25%`. Good for workspace/team avatars.
- **Squircle**: iOS-style superellipse. Use SVG clip-path for true squircle (CSS border-radius is not a real squircle).
- **Square**: Rare. Used for app icons or organization logos only.

### 8.3 Fallback Hierarchy

When no user photo is available:

1. **User-uploaded photo** (primary).
2. **Initials**: First + Last initial on colored background. Generate color from user ID hash for consistency. Font size: ~40% of avatar diameter. Font weight: 600.
3. **Generic icon**: Default person silhouette. Use when name is unavailable (anonymous users).
4. **Gravatar/external service**: MD5 hash of email to check Gravatar.

Initial color generation:
```javascript
const colors = ['#FF6B6B','#4ECDC4','#45B7D1','#96CEB4','#FFEAA7','#DDA0DD','#98D8C8','#F7DC6F'];
const colorIndex = userId.charCodeAt(0) % colors.length;
```

### 8.4 Status Indicators

Small colored dot on the avatar border, typically bottom-right.

| Status | Color | Label |
|--------|-------|-------|
| Online | Green (#22C55E) | "Online" |
| Away/Idle | Yellow (#EAB308) | "Away" |
| Busy/DND | Red (#EF4444) | "Do not disturb" |
| Offline | Gray (#9CA3AF) | "Offline" |

- Dot size: 25-30% of avatar diameter. Min 8px.
- White border (2px) around dot for separation from avatar.
- Position: `bottom: 0; right: 0` with slight offset.

### 8.5 Avatar Groups / Stacks

Multiple avatars overlapping horizontally.

- Overlap: 25-33% of avatar width (e.g., 32px avatars with -8px margin-left).
- Stack order: first avatar on top (highest z-index) or last on top (both conventions exist).
- Overflow indicator: "+5" circle at the end when more than shown limit.
- Max visible: 3-5 avatars before overflow.
- Ring: 2px white border on each avatar for visual separation.

```css
.avatar-group {
  display: flex;
  flex-direction: row-reverse; /* last item on top */
}
.avatar-group > * {
  margin-left: -8px;
  border: 2px solid white;
  border-radius: 50%;
}
.avatar-group > *:last-child { margin-left: 0; }
```

---

## 9. Video Patterns

### 9.1 Inline Autoplay (Muted)

Short looping video replacing an animated image. Must be muted for browser autoplay policy.

```html
<video autoplay muted loop playsinline preload="metadata" poster="thumb.webp">
  <source src="clip.mp4" type="video/mp4">
</video>
```

- `playsinline`: Required for iOS to prevent fullscreen hijack.
- `poster`: Static image shown before video loads.
- Max duration: 10-30 seconds for ambient/background use.
- File size: Keep under 5MB. Use H.265/HEVC or VP9 for better compression.

### 9.2 Click-to-Play

Video with visible thumbnail and play button overlay. User initiates playback.

- Large centered play button: 64-80px circle, semi-transparent background.
- Duration badge: bottom-right corner of thumbnail.
- On click: hide overlay, start video, show controls.
- Preferred for: content videos, tutorials, product demos.

### 9.3 Hero Video / Background Video

Full-viewport video replacing a static hero image.

- Always muted, looping, no controls visible.
- Overlay with gradient or semi-transparent color for text readability.
- Provide pause button (accessibility requirement).
- Fallback: poster image for slow connections or `prefers-reduced-motion`.
- Performance: Use lower resolution (720p often sufficient for background), high compression.

### 9.4 Video Player Controls

Custom player UI elements:

| Control | Behavior | Keyboard |
|---------|----------|----------|
| Play/Pause | Toggle playback | Space or K |
| Seek bar | Drag or click to jump | Left/Right arrows (5s), J/L (10s) |
| Volume | Slider 0-100% | Up/Down arrows, M to mute |
| Fullscreen | Toggle fullscreen | F |
| Captions | Toggle subtitles | C |
| Speed | 0.5x, 1x, 1.25x, 1.5x, 2x | < / > |
| Picture-in-Picture | Float video over other content | P |
| Skip intro | Jump ahead N seconds | Button |
| Chapters | Markers on seek bar | N/A |

### 9.5 Picture-in-Picture (PiP)

Floating mini-player that persists while scrolling away from the video.

- Trigger: scroll video out of viewport, or user clicks PiP button.
- Position: fixed bottom-right corner, 300-400px wide.
- Controls: play/pause, close, expand back.
- Z-index: high enough to float above content but below modals.
- Close: X button returns to inline player or dismisses.
- Use native `requestPictureInPicture()` API when supported.

### 9.6 Video Thumbnails / Preview

Hover-to-preview: scrubbing through video frames on mouseover.

- Generate thumbnail sprite sheet (e.g., one frame every 5 seconds).
- On hover: cycle through frames showing preview of content.
- Progress bar preview: show frame thumbnail above seek bar on hover.
- YouTube-style: 3x3 thumbnail grid in search results.

---

## 10. Audio Patterns

### 10.1 Waveform Display

Visual representation of audio amplitude over time.

- Generate waveform data server-side (peaks array, 100-500 data points).
- Render with SVG or Canvas.
- Show played portion in primary color, unplayed in muted gray.
- Scrub by clicking/dragging on waveform.
- Used by: SoundCloud, voice messages (WhatsApp), podcast players.

### 10.2 Mini Player

Compact audio player for inline use (chat messages, article embeds).

- Single row: play button + waveform/progress bar + duration.
- Height: 40-48px. Width: flexible (min 200px).
- No volume control (use device volume).
- Playback speed toggle (1x, 1.5x, 2x) for voice messages.

### 10.3 Full Player

Dedicated audio player with complete controls.

Components: album art (large, 200-300px), track title, artist name, progress bar with timestamps (elapsed / total), play/pause + skip forward/back, shuffle + repeat toggles, volume slider, queue/playlist access.

### 10.4 Podcast Player

Specialized audio player for long-form spoken content.

- Chapter markers on progress bar.
- Skip forward/back buttons (15s or 30s).
- Playback speed: 0.5x to 3x in 0.1x increments.
- Sleep timer.
- Show notes / transcript toggle.
- Episode list/queue.
- Download for offline button.

### 10.5 Voice Message

Inline audio recording found in messaging apps.

- Compressed waveform visualization.
- Duration displayed.
- Play at 1x or 2x speed.
- Unplayed indicator (blue dot or bold styling).
- Recording UI: hold-to-record with waveform animation, slide-to-cancel, release-to-send.

---

## 11. Media Player UI Specifications

### Universal Player Controls

```
[Play/Pause] [|< Prev] [>| Next] [Progress Bar ====o----] 2:34 / 5:12 [Vol] [CC] [⛶ FS]
```

### Progress Bar

- Height: 4px (expand to 8px on hover for easier targeting).
- Played portion: primary brand color.
- Buffered portion: lighter shade or semi-transparent.
- Remaining: neutral gray.
- Thumb/scrubber: 12-16px circle, visible on hover/focus.
- Tooltip: show timestamp on hover above progress bar.

### Volume Control

- Icon changes: muted (x), low (one wave), medium (two waves), high (three waves).
- Slider: vertical (traditional) or horizontal (modern).
- Click icon to toggle mute.
- Range: 0 to 100%.

### Captions/Subtitles

- Toggle button in controls bar.
- Settings: font size (50-200%), font color, background color/opacity.
- Position: bottom of video, above controls when visible.
- Format support: VTT (preferred), SRT.

### Playback Speed

- Display current speed in controls.
- Options: 0.25x, 0.5x, 0.75x, 1x (normal), 1.25x, 1.5x, 1.75x, 2x.
- Keyboard shortcut: Shift+< (slower), Shift+> (faster).

---

## 12. Image Editing UI Patterns

### 12.1 Crop

- Preset ratios: Free, 1:1, 4:3, 16:9, 3:2, custom.
- Draggable crop handles at corners and edges.
- Rule-of-thirds grid overlay (optional toggle).
- Dimmed area outside crop region.
- Flip horizontal/vertical buttons.

### 12.2 Rotate

- Free rotation: drag to rotate with degree readout.
- Quick rotate: 90-degree CW/CCW buttons.
- Straighten slider: -45 to +45 degrees with grid overlay.
- Auto-straighten: detect horizon line.

### 12.3 Filters / Presets

- Thumbnail previews of each filter applied to current image.
- Horizontal scrollable strip of filter options.
- Filter intensity slider (0-100%) after selecting.
- Common filters: Original, B&W, Sepia, Vivid, Warm, Cool, Fade, Dramatic.

### 12.4 Adjustments

Individual parameter sliders:

| Adjustment | Range | Default |
|-----------|-------|---------|
| Brightness | -100 to +100 | 0 |
| Contrast | -100 to +100 | 0 |
| Saturation | -100 to +100 | 0 |
| Temperature | -100 (cool) to +100 (warm) | 0 |
| Highlights | -100 to +100 | 0 |
| Shadows | -100 to +100 | 0 |
| Sharpness | 0 to +100 | 0 |
| Vignette | 0 to +100 | 0 |

### 12.5 Zoom / Pan

- Pinch-to-zoom on touch devices.
- Scroll wheel zoom on desktop.
- Zoom slider or +/- buttons.
- Fit-to-screen / 100% / fill toggle.
- Pan by drag when zoomed in. Change cursor to grab/grabbing.
- Mini-map overview showing current viewport position on the full image.

---

## 13. Upload Patterns

### 13.1 Drag-and-Drop Zone

```
+------------------------------------------+
|                                          |
|     [Cloud Upload Icon]                  |
|     Drag and drop files here             |
|     or click to browse                   |
|                                          |
|     Supported: JPG, PNG, WebP (max 10MB) |
+------------------------------------------+
```

States:
- **Default**: Dashed border, muted colors, upload icon.
- **Drag over**: Highlighted border (primary color), background tint, "Drop files here" text.
- **Uploading**: Progress bar or percentage, file name, cancel button.
- **Complete**: Thumbnail preview, file name, size, remove/replace button.
- **Error**: Red border, error message ("File too large", "Unsupported format").

### 13.2 File Picker Button

Simple button that opens native file dialog.

- Button text: "Upload Photo", "Choose File", "Add Image".
- Show accepted types: `accept="image/jpeg,image/png,image/webp"`.
- Multiple files: `multiple` attribute.
- After selection: show thumbnail preview + filename + "Change" link.

### 13.3 Camera Capture

Mobile-specific: open device camera directly.

```html
<input type="file" accept="image/*" capture="environment"> <!-- rear camera -->
<input type="file" accept="image/*" capture="user">        <!-- front camera -->
```

### 13.4 Paste from Clipboard

Listen for paste events to accept images from clipboard.

```javascript
document.addEventListener('paste', (e) => {
  const items = e.clipboardData?.items;
  for (const item of items) {
    if (item.type.startsWith('image/')) {
      const file = item.getAsFile();
      handleUpload(file);
    }
  }
});
```

### 13.5 Bulk Upload

Multiple file upload with batch progress.

- Grid of thumbnail previews for all queued files.
- Individual progress bar per file.
- Overall progress bar.
- Remove individual files before upload.
- Reorder via drag-and-drop.
- Status per file: queued, uploading, complete, failed.
- Retry button on failed uploads.

### 13.6 Progress Indication

| Method | Use Case |
|--------|----------|
| Determinate progress bar | Known file size, shows percentage |
| Indeterminate spinner | Unknown progress (processing server-side) |
| Percentage text | "Uploading... 67%" |
| Stepped progress | "Uploading → Processing → Complete" |
| Thumbnail blur-to-clear | Blurred thumbnail that sharpens as upload progresses |

---

## 14. Accessibility for Media

### 14.1 Alt Text Guidelines

- **Descriptive**: Describe the image content and function. "Golden retriever puppy sitting on a red blanket" not "dog".
- **Functional**: For images that are links/buttons, describe the action. "Go to homepage" not "company logo".
- **Decorative**: Use `alt=""` (empty string, not absent) for purely decorative images. Screen readers will skip them.
- **Complex**: For charts/infographics, provide brief alt + detailed `aria-describedby` linking to a text description.
- **Max length**: 125 characters recommended. Use `longdesc` or linked description for more detail.
- **Never**: "Image of...", "Picture of..." — screen readers already announce "image".

### 14.2 Captions & Transcripts

- All pre-recorded video must have captions (WCAG 1.2.2 Level A).
- Live video should have captions (WCAG 1.2.4 Level AA).
- Provide transcript for audio-only content (podcasts, voice messages).
- Audio description track for video with important visual information not conveyed by audio.

### 14.3 Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Disable Ken Burns, parallax, autoplay carousel */
  .ken-burns-image { animation: none; }
  .parallax { background-attachment: scroll; }
  .carousel { scroll-behavior: auto; }
  video[autoplay] { /* show poster frame instead */ }

  /* Replace animations with instant state changes */
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 14.4 Focus Management for Media

- All interactive media controls must be keyboard-focusable.
- Custom video players: ensure Tab order through controls is logical.
- Lightbox: trap focus, return focus on close.
- Carousel: expose all slides to assistive technology or properly hide inactive ones.

---

## 15. Performance Optimization

### 15.1 Image CDN & Transformation

Services: Cloudinary, imgix, Vercel Image Optimization, Cloudflare Images.

On-the-fly capabilities:
- Resize: `?w=800&h=600`
- Format conversion: `?f=avif` (auto-negotiate with `f_auto`)
- Quality: `?q=80`
- Crop: `?fit=crop&gravity=face` (face detection)
- Blur: `?blur=500` (for LQIP)
- DPR: `?dpr=2`

### 15.2 Compression Guidelines

| Content Type | Target File Size | Strategy |
|-------------|-----------------|----------|
| Hero image (1920px) | 100-200KB | AVIF q50 or WebP q80 |
| Card thumbnail (400px) | 20-40KB | WebP q75 |
| Avatar (128px) | 5-15KB | WebP q80 |
| Product image (800px) | 40-80KB | WebP q85 (preserve detail) |
| Icon/logo | 1-5KB | SVG (vector) |
| Background video (720p) | 2-5MB | H.265, 30fps, low bitrate |

### 15.3 Core Web Vitals

**LCP (Largest Contentful Paint)**:
- Hero image is usually the LCP element.
- Preload LCP image: `<link rel="preload" as="image" href="hero.webp">`.
- Use `fetchpriority="high"` on the LCP `<img>`.
- Never lazy-load the LCP image.
- Serve from CDN with proper caching headers.

**CLS (Cumulative Layout Shift)**:
- Always specify `width` and `height` attributes on `<img>`.
- Use CSS `aspect-ratio` on image containers.
- Reserve space with placeholder (skeleton, blur-up, dominant color).
- Avoid inserting images above existing content dynamically.

```css
/* Prevent CLS with aspect-ratio container */
.image-container {
  aspect-ratio: 16 / 9;
  overflow: hidden;
}
.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

---

## 16. CSS Techniques for Media

### 16.1 Object-Fit & Object-Position

```css
img {
  object-fit: cover;           /* fill container, crop */
  object-position: center 20%; /* focal point: center horizontal, 20% from top */
}
```

Common focal points: `center` (default), `top` (face portraits), `center 30%` (landscapes with sky).

### 16.2 Aspect-Ratio

```css
.video-container { aspect-ratio: 16 / 9; }
.square-thumb   { aspect-ratio: 1; }
.portrait       { aspect-ratio: 3 / 4; }
```

Replaces the old padding-bottom hack: `padding-bottom: 56.25%` for 16:9.

### 16.3 Clip-Path

```css
/* Circle */
.circle { clip-path: circle(50%); }

/* Diagonal cut */
.diagonal { clip-path: polygon(0 0, 100% 0, 100% 85%, 0 100%); }

/* Hexagon */
.hex { clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%); }

/* Animated reveal */
.reveal { clip-path: inset(0 100% 0 0); transition: clip-path 0.6s ease; }
.reveal.visible { clip-path: inset(0 0 0 0); }
```

### 16.4 Mask-Image

```css
/* Gradient fade */
.fade-bottom {
  mask-image: linear-gradient(to bottom, black 60%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 60%, transparent 100%);
}

/* SVG shape mask */
.custom-shape {
  mask-image: url('mask.svg');
  mask-size: cover;
}
```

### 16.5 Filter & Backdrop-Filter

```css
/* Image filters */
img.grayscale { filter: grayscale(100%); }
img.sepia     { filter: sepia(80%); }
img.blur      { filter: blur(8px); }
img.bright    { filter: brightness(1.2) contrast(1.1); }

/* Frosted glass overlay */
.glass-panel {
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  background: rgba(255, 255, 255, 0.7);
}
```

### 16.6 Mix-Blend-Mode

```css
/* Duotone effect */
.duotone {
  position: relative;
  background-color: #0066ff; /* brand color */
}
.duotone img {
  mix-blend-mode: luminosity;
  filter: grayscale(100%) contrast(1.2);
}
```

---

## 17. Dark Mode for Media

### 17.1 Image Brightness/Contrast Adjustments

Reduce eye strain by dimming images in dark mode.

```css
@media (prefers-color-scheme: dark) {
  img:not([src$=".svg"]) {
    filter: brightness(0.85) contrast(1.05);
  }
  /* Exception: avatars keep full brightness */
  .avatar img { filter: none; }
}
```

### 17.2 Dark Image Variants

Serve alternate versions optimized for dark backgrounds.

```html
<picture>
  <source srcset="logo-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="logo-light.svg" alt="Company Logo">
</picture>
```

### 17.3 SVG Color Adaptation

```css
@media (prefers-color-scheme: dark) {
  .icon svg { fill: #e0e0e0; }              /* invert icon fill */
  img[src$=".svg"] { filter: invert(0.85); } /* approximate inversion */
}
```

### 17.4 Video & Background Adjustments

- Reduce ambient video brightness: `filter: brightness(0.7)` on background videos.
- Adjust poster images: same brightness filter as photos.
- Player controls: ensure contrast against dark chrome.
- Waveform colors: switch from dark-on-light to light-on-dark palette.

---

## Cross-References

- **layout-block-intelligence** — Hero sections, feature blocks containing images
- **component-patterns-code** — React/SwiftUI/CSS implementations of image components
- **accessibility-inclusive-design** — WCAG media requirements, screen reader patterns
- **performance-states-patterns** — Loading skeletons, error states, empty states
- **responsive-block-patterns** — Container queries, breakpoint transformations
- **animation-recipe-library** — Entrance animations, Ken Burns, parallax recipes
- **form-design-encyclopedia** — File upload form patterns
- **platform-visual-standards** — iOS/Android/web image handling conventions
- **design-systems-architecture** — Token-driven image component APIs
