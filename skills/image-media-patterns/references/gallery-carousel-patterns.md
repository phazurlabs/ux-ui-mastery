# Gallery & Carousel Patterns — Grids, Lightbox & Carousel Accessibility

Production-ready patterns for gallery layouts, lightbox overlays, and accessible carousel implementations.

---

## 1. Masonry Grid — CSS Columns

The simplest masonry approach. Works without JavaScript.

```css
.masonry {
  columns: 3;
  column-gap: 16px;
  padding: 16px;
}

.masonry-item {
  break-inside: avoid;
  margin-bottom: 16px;
  border-radius: 12px;
  overflow: hidden;
}

.masonry-item img {
  width: 100%;
  height: auto;
  display: block;
}

/* Responsive */
@media (max-width: 1024px) { .masonry { columns: 2; } }
@media (max-width: 640px)  { .masonry { columns: 1; } }
```

Limitation: items flow top-to-bottom per column, not left-to-right. Source order and visual order can diverge.

---

## 2. Masonry Grid — CSS Grid with JS Row Span

True masonry feel with CSS Grid, but requires JS to calculate each item's row span.

```css
.masonry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  grid-auto-rows: 8px; /* small row unit */
  gap: 0 16px;
}

.masonry-grid-item {
  /* grid-row-end is set dynamically via JS */
  padding-bottom: 16px;
}

.masonry-grid-item img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 12px;
}
```

```javascript
function setMasonryRowSpans() {
  const grid = document.querySelector('.masonry-grid');
  const rowGap = parseInt(getComputedStyle(grid).gridAutoRows);
  const items = grid.querySelectorAll('.masonry-grid-item');

  items.forEach(item => {
    const content = item.querySelector('img');
    const contentHeight = content.getBoundingClientRect().height + 16; // + gap
    const rowSpan = Math.ceil(contentHeight / rowGap);
    item.style.gridRowEnd = `span ${rowSpan}`;
  });
}

// Run after images load
window.addEventListener('load', setMasonryRowSpans);
window.addEventListener('resize', setMasonryRowSpans);
```

---

## 3. Justified Grid (Flickr-Style)

All rows fill the full width. Image widths vary to maintain aspect ratios with uniform row height.

```javascript
// Using justified-layout (by Flickr)
import justifiedLayout from 'justified-layout';

const photos = [
  { width: 4000, height: 3000 },
  { width: 2000, height: 3000 },
  { width: 3000, height: 2000 },
  // ...
];

const geometry = justifiedLayout(photos.map(p => p.width / p.height), {
  containerWidth: containerElement.offsetWidth,
  targetRowHeight: 240,
  boxSpacing: 8,
});

// geometry.boxes contains { width, height, top, left } for each photo
geometry.boxes.forEach((box, i) => {
  const el = photoElements[i];
  el.style.position = 'absolute';
  el.style.width = `${box.width}px`;
  el.style.height = `${box.height}px`;
  el.style.top = `${box.top}px`;
  el.style.left = `${box.left}px`;
});

// Set container height
container.style.height = `${geometry.containerHeight}px`;
```

---

## 4. Uniform Grid

All images forced to identical dimensions. Simplest and most predictable layout.

```css
.uniform-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 8px;
  padding: 8px;
}

.uniform-grid-item {
  aspect-ratio: 1; /* square */
  overflow: hidden;
  border-radius: 8px;
  cursor: pointer;
  position: relative;
}

.uniform-grid-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.uniform-grid-item:hover img {
  transform: scale(1.05);
}

/* Hover overlay */
.uniform-grid-item::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0);
  transition: background 0.3s ease;
}

.uniform-grid-item:hover::after {
  background: rgba(0, 0, 0, 0.15);
}
```

### Ratio Variants

```css
/* 4:3 cards */
.grid-4-3 .uniform-grid-item { aspect-ratio: 4/3; }

/* 16:9 widescreen */
.grid-16-9 .uniform-grid-item { aspect-ratio: 16/9; }

/* 3:2 photography */
.grid-3-2 .uniform-grid-item { aspect-ratio: 3/2; }
```

---

## 5. Mosaic / Feature Grid

Predetermined layout with one large featured item and smaller supporting items.

```css
.mosaic-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(2, 200px);
  gap: 8px;
}

/* Featured: spans 2 cols + 2 rows */
.mosaic-grid .featured {
  grid-column: 1 / 3;
  grid-row: 1 / 3;
}

.mosaic-grid .item {
  overflow: hidden;
  border-radius: 12px;
}

.mosaic-grid .item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 5-photo Instagram-style layout */
.mosaic-5 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, 200px);
  gap: 4px;
}
.mosaic-5 .item:first-child {
  grid-column: 1 / 3;
  grid-row: 1 / 3;
}
```

### Responsive Mosaic

```css
@media (max-width: 768px) {
  .mosaic-grid {
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(3, 150px);
  }
  .mosaic-grid .featured {
    grid-column: 1 / 3;
    grid-row: 1 / 2;
  }
}

@media (max-width: 480px) {
  .mosaic-grid {
    grid-template-columns: 1fr;
    grid-template-rows: auto;
  }
  .mosaic-grid .featured {
    grid-column: 1;
    grid-row: auto;
  }
  .mosaic-grid .item { aspect-ratio: 16/9; }
}
```

---

## 6. Lightbox — Full Implementation

### HTML

```html
<!-- Trigger: gallery items -->
<div class="gallery" role="list">
  <button class="gallery-item" role="listitem" data-index="0"
          data-full-src="photo1-full.webp" data-alt="Mountain at sunrise"
          aria-label="View Mountain at sunrise, image 1 of 12">
    <img src="photo1-thumb.webp" alt="" width="300" height="200">
  </button>
  <!-- Repeat for each item -->
</div>

<!-- Lightbox overlay (hidden by default) -->
<div class="lightbox" role="dialog" aria-label="Image viewer" aria-modal="true"
     hidden id="lightbox">
  <div class="lightbox-backdrop"></div>

  <button class="lightbox-close" aria-label="Close image viewer">
    <svg><!-- X icon --></svg>
  </button>

  <button class="lightbox-prev" aria-label="Previous image">
    <svg><!-- Left arrow --></svg>
  </button>

  <button class="lightbox-next" aria-label="Next image">
    <svg><!-- Right arrow --></svg>
  </button>

  <div class="lightbox-content">
    <img class="lightbox-image" src="" alt="" />
  </div>

  <div class="lightbox-caption" aria-live="polite">
    <p class="lightbox-alt-text"></p>
    <p class="lightbox-counter">1 of 12</p>
  </div>
</div>
```

### CSS

```css
.lightbox {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox[hidden] { display: none; }

.lightbox-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.92);
}

.lightbox-content {
  position: relative;
  max-width: 90vw;
  max-height: 85vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-image {
  max-width: 100%;
  max-height: 85vh;
  object-fit: contain;
  border-radius: 4px;
  user-select: none;
}

.lightbox-close {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 10;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  cursor: pointer;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.lightbox-close:hover { background: rgba(255, 255, 255, 0.2); }

.lightbox-prev,
.lightbox-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  cursor: pointer;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.lightbox-prev { left: 16px; }
.lightbox-next { right: 16px; }
.lightbox-prev:hover,
.lightbox-next:hover { background: rgba(255, 255, 255, 0.2); }

.lightbox-caption {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  color: rgba(255, 255, 255, 0.85);
  font-size: 14px;
}

.lightbox-counter {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
  margin-top: 4px;
}
```

### JavaScript (Accessible)

```javascript
class Lightbox {
  constructor(gallerySelector) {
    this.gallery = document.querySelector(gallerySelector);
    this.lightbox = document.getElementById('lightbox');
    this.image = this.lightbox.querySelector('.lightbox-image');
    this.altText = this.lightbox.querySelector('.lightbox-alt-text');
    this.counter = this.lightbox.querySelector('.lightbox-counter');
    this.items = [...this.gallery.querySelectorAll('.gallery-item')];
    this.currentIndex = 0;
    this.triggerElement = null;
    this.previouslyFocused = null;

    this.bindEvents();
  }

  bindEvents() {
    // Open on gallery item click
    this.items.forEach((item, index) => {
      item.addEventListener('click', () => this.open(index));
    });

    // Close
    this.lightbox.querySelector('.lightbox-close').addEventListener('click', () => this.close());
    this.lightbox.querySelector('.lightbox-backdrop').addEventListener('click', () => this.close());

    // Navigate
    this.lightbox.querySelector('.lightbox-prev').addEventListener('click', () => this.prev());
    this.lightbox.querySelector('.lightbox-next').addEventListener('click', () => this.next());

    // Keyboard
    this.lightbox.addEventListener('keydown', (e) => this.handleKeydown(e));
  }

  open(index) {
    this.previouslyFocused = document.activeElement;
    this.currentIndex = index;
    this.updateImage();
    this.lightbox.hidden = false;
    document.body.style.overflow = 'hidden';

    // Focus trap: focus the close button
    this.lightbox.querySelector('.lightbox-close').focus();

    // Trap focus within lightbox
    this.trapFocus();
  }

  close() {
    this.lightbox.hidden = true;
    document.body.style.overflow = '';

    // Return focus to trigger element
    if (this.previouslyFocused) {
      this.previouslyFocused.focus();
    }
  }

  prev() {
    this.currentIndex = (this.currentIndex - 1 + this.items.length) % this.items.length;
    this.updateImage();
  }

  next() {
    this.currentIndex = (this.currentIndex + 1) % this.items.length;
    this.updateImage();
  }

  updateImage() {
    const item = this.items[this.currentIndex];
    this.image.src = item.dataset.fullSrc;
    this.image.alt = item.dataset.alt;
    this.altText.textContent = item.dataset.alt;
    this.counter.textContent = `${this.currentIndex + 1} of ${this.items.length}`;
  }

  handleKeydown(e) {
    switch (e.key) {
      case 'Escape':
        this.close();
        break;
      case 'ArrowLeft':
        e.preventDefault();
        this.prev();
        break;
      case 'ArrowRight':
        e.preventDefault();
        this.next();
        break;
    }
  }

  trapFocus() {
    const focusable = this.lightbox.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    this.lightbox.addEventListener('keydown', (e) => {
      if (e.key !== 'Tab') return;

      if (e.shiftKey) {
        if (document.activeElement === first) {
          e.preventDefault();
          last.focus();
        }
      } else {
        if (document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    });
  }
}

// Initialize
new Lightbox('.gallery');
```

---

## 7. Carousel — CSS Scroll Snap

Native-feeling carousel with no JS framework dependency.

### HTML

```html
<div class="carousel-container" role="region" aria-label="Featured products" aria-roledescription="carousel">
  <div class="carousel-track" role="list">
    <div class="carousel-slide" role="group" aria-roledescription="slide" aria-label="Slide 1 of 5">
      <img src="slide1.webp" alt="Product A" width="800" height="450">
    </div>
    <div class="carousel-slide" role="group" aria-roledescription="slide" aria-label="Slide 2 of 5">
      <img src="slide2.webp" alt="Product B" width="800" height="450">
    </div>
    <!-- ... more slides ... -->
  </div>

  <div class="carousel-controls">
    <button class="carousel-prev" aria-label="Previous slide" aria-controls="carousel-track">
      <svg width="24" height="24"><path d="M15 18l-6-6 6-6" stroke="currentColor" stroke-width="2" fill="none"/></svg>
    </button>
    <button class="carousel-next" aria-label="Next slide" aria-controls="carousel-track">
      <svg width="24" height="24"><path d="M9 6l6 6-6 6" stroke="currentColor" stroke-width="2" fill="none"/></svg>
    </button>
  </div>

  <div class="carousel-dots" role="tablist" aria-label="Slide navigation">
    <button role="tab" aria-selected="true" aria-label="Go to slide 1" class="dot active"></button>
    <button role="tab" aria-selected="false" aria-label="Go to slide 2" class="dot"></button>
    <button role="tab" aria-selected="false" aria-label="Go to slide 3" class="dot"></button>
    <button role="tab" aria-selected="false" aria-label="Go to slide 4" class="dot"></button>
    <button role="tab" aria-selected="false" aria-label="Go to slide 5" class="dot"></button>
  </div>
</div>
```

### CSS

```css
.carousel-container {
  position: relative;
  overflow: hidden;
}

.carousel-track {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}

.carousel-track::-webkit-scrollbar { display: none; }

.carousel-slide {
  flex: 0 0 100%;
  scroll-snap-align: start;
}

.carousel-slide img {
  width: 100%;
  height: auto;
  display: block;
}

/* Peek variant: show 10% of next slide */
.carousel-track.peek .carousel-slide {
  flex: 0 0 calc(100% - 48px);
  margin-right: 8px;
}

/* Multi-item carousel */
.carousel-track.multi .carousel-slide {
  flex: 0 0 calc(33.333% - 11px); /* 3 visible, accounting for gaps */
  margin-right: 16px;
}

@media (max-width: 1024px) {
  .carousel-track.multi .carousel-slide {
    flex: 0 0 calc(50% - 8px);
  }
}

@media (max-width: 640px) {
  .carousel-track.multi .carousel-slide {
    flex: 0 0 calc(100% - 32px); /* peek at next */
  }
}

/* Arrow buttons */
.carousel-prev, .carousel-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 2;
  background: white;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 50%;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.2s, background 0.2s;
}

.carousel-prev:hover, .carousel-next:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.carousel-prev { left: 12px; }
.carousel-next { right: 12px; }

/* Hide arrows on touch devices */
@media (pointer: coarse) {
  .carousel-prev, .carousel-next { display: none; }
}

/* Dots */
.carousel-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 12px 0;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  border: none;
  background: rgba(0, 0, 0, 0.2);
  cursor: pointer;
  padding: 0;
  transition: background 0.2s, transform 0.2s;
}

.dot.active {
  background: rgba(0, 0, 0, 0.8);
  transform: scale(1.25);
}

.dot:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}
```

### JavaScript (Scroll-Based)

```javascript
class ScrollSnapCarousel {
  constructor(container) {
    this.container = container;
    this.track = container.querySelector('.carousel-track');
    this.slides = [...container.querySelectorAll('.carousel-slide')];
    this.dots = [...container.querySelectorAll('.dot')];
    this.prevBtn = container.querySelector('.carousel-prev');
    this.nextBtn = container.querySelector('.carousel-next');
    this.currentIndex = 0;

    this.bindEvents();
    this.updateAriaStates();
  }

  bindEvents() {
    // Arrow buttons
    this.prevBtn?.addEventListener('click', () => this.goTo(this.currentIndex - 1));
    this.nextBtn?.addEventListener('click', () => this.goTo(this.currentIndex + 1));

    // Dot buttons
    this.dots.forEach((dot, i) => {
      dot.addEventListener('click', () => this.goTo(i));
    });

    // Detect scroll position to update active dot
    let scrollTimeout;
    this.track.addEventListener('scroll', () => {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => this.onScrollEnd(), 100);
    });

    // Keyboard navigation
    this.container.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') { e.preventDefault(); this.goTo(this.currentIndex - 1); }
      if (e.key === 'ArrowRight') { e.preventDefault(); this.goTo(this.currentIndex + 1); }
    });
  }

  goTo(index) {
    const clamped = Math.max(0, Math.min(index, this.slides.length - 1));
    this.slides[clamped].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
    this.currentIndex = clamped;
    this.updateAriaStates();
  }

  onScrollEnd() {
    const trackRect = this.track.getBoundingClientRect();
    const center = trackRect.left + trackRect.width / 2;

    let closest = 0;
    let minDist = Infinity;
    this.slides.forEach((slide, i) => {
      const rect = slide.getBoundingClientRect();
      const slideCtr = rect.left + rect.width / 2;
      const dist = Math.abs(slideCtr - center);
      if (dist < minDist) { minDist = dist; closest = i; }
    });

    this.currentIndex = closest;
    this.updateAriaStates();
  }

  updateAriaStates() {
    // Update dots
    this.dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === this.currentIndex);
      dot.setAttribute('aria-selected', i === this.currentIndex ? 'true' : 'false');
    });

    // Update slides
    this.slides.forEach((slide, i) => {
      const isActive = i === this.currentIndex;
      slide.setAttribute('aria-hidden', isActive ? 'false' : 'true');
      slide.querySelectorAll('a, button, input').forEach(el => {
        el.setAttribute('tabindex', isActive ? '0' : '-1');
      });
    });

    // Update arrows
    if (this.prevBtn) this.prevBtn.disabled = this.currentIndex === 0;
    if (this.nextBtn) this.nextBtn.disabled = this.currentIndex === this.slides.length - 1;
  }
}

// Initialize all carousels on page
document.querySelectorAll('.carousel-container').forEach(el => new ScrollSnapCarousel(el));
```

---

## 8. Autoplay Carousel — Accessibility-Compliant

```javascript
class AutoplayCarousel extends ScrollSnapCarousel {
  constructor(container, interval = 5000) {
    super(container);
    this.interval = interval;
    this.timer = null;
    this.isPaused = false;

    this.pauseBtn = container.querySelector('.carousel-pause');
    this.setupAutoplay();
  }

  setupAutoplay() {
    // Respect reduced motion preference
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    this.startAutoplay();

    // Pause on hover
    this.container.addEventListener('mouseenter', () => this.pauseAutoplay());
    this.container.addEventListener('mouseleave', () => {
      if (!this.isPaused) this.startAutoplay();
    });

    // Pause on focus within
    this.container.addEventListener('focusin', () => this.pauseAutoplay());
    this.container.addEventListener('focusout', (e) => {
      if (!this.container.contains(e.relatedTarget) && !this.isPaused) {
        this.startAutoplay();
      }
    });

    // Pause on page hidden
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) this.pauseAutoplay();
      else if (!this.isPaused) this.startAutoplay();
    });

    // Pause/play button
    this.pauseBtn?.addEventListener('click', () => this.togglePause());

    // Stop autoplay on manual interaction
    this.container.querySelectorAll('.carousel-prev, .carousel-next, .dot').forEach(btn => {
      btn.addEventListener('click', () => {
        this.isPaused = true;
        this.pauseAutoplay();
        this.updatePauseButton();
      });
    });
  }

  startAutoplay() {
    this.pauseAutoplay(); // clear existing
    this.timer = setInterval(() => {
      const next = (this.currentIndex + 1) % this.slides.length;
      this.goTo(next);
    }, this.interval);
  }

  pauseAutoplay() {
    clearInterval(this.timer);
    this.timer = null;
  }

  togglePause() {
    this.isPaused = !this.isPaused;
    if (this.isPaused) this.pauseAutoplay();
    else this.startAutoplay();
    this.updatePauseButton();
  }

  updatePauseButton() {
    if (!this.pauseBtn) return;
    this.pauseBtn.setAttribute('aria-label', this.isPaused ? 'Play slideshow' : 'Pause slideshow');
    this.pauseBtn.textContent = this.isPaused ? 'Play' : 'Pause';
  }
}
```

---

## 9. Filmstrip / Thumbnail Navigation

Horizontal thumbnail strip that controls a main image viewer.

```html
<div class="filmstrip-viewer">
  <div class="filmstrip-main">
    <img id="main-image" src="photo1-large.webp" alt="Photo 1" width="800" height="533">
  </div>

  <div class="filmstrip-strip" role="tablist" aria-label="Photo thumbnails">
    <button role="tab" aria-selected="true" class="filmstrip-thumb active" data-full="photo1-large.webp" data-alt="Photo 1">
      <img src="photo1-thumb.webp" alt="" width="80" height="80">
    </button>
    <button role="tab" aria-selected="false" class="filmstrip-thumb" data-full="photo2-large.webp" data-alt="Photo 2">
      <img src="photo2-thumb.webp" alt="" width="80" height="80">
    </button>
    <!-- more thumbnails -->
  </div>
</div>
```

```css
.filmstrip-main {
  width: 100%;
  aspect-ratio: 3/2;
  overflow: hidden;
  border-radius: 12px;
  margin-bottom: 12px;
}

.filmstrip-main img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 0.3s ease;
}

.filmstrip-strip {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
  padding: 4px 0;
}

.filmstrip-strip::-webkit-scrollbar { display: none; }

.filmstrip-thumb {
  flex: 0 0 72px;
  height: 72px;
  scroll-snap-align: start;
  border: 2px solid transparent;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  background: none;
  padding: 0;
  transition: border-color 0.2s;
}

.filmstrip-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.filmstrip-thumb.active {
  border-color: #2563eb;
}

.filmstrip-thumb:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}
```

---

## 10. Infinite Scroll Gallery

```javascript
class InfiniteGallery {
  constructor(container, fetchFn) {
    this.container = container;
    this.fetchFn = fetchFn;
    this.page = 1;
    this.loading = false;
    this.hasMore = true;

    this.sentinel = document.createElement('div');
    this.sentinel.className = 'gallery-sentinel';
    this.sentinel.setAttribute('aria-hidden', 'true');
    this.container.appendChild(this.sentinel);

    this.liveRegion = document.createElement('div');
    this.liveRegion.setAttribute('aria-live', 'polite');
    this.liveRegion.setAttribute('aria-atomic', 'true');
    this.liveRegion.className = 'sr-only';
    this.container.appendChild(this.liveRegion);

    this.setupObserver();
  }

  setupObserver() {
    this.observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && !this.loading && this.hasMore) {
          this.loadMore();
        }
      },
      { rootMargin: '400px' }
    );
    this.observer.observe(this.sentinel);
  }

  async loadMore() {
    this.loading = true;
    this.showSpinner();

    try {
      const { items, hasMore } = await this.fetchFn(this.page);
      this.hasMore = hasMore;
      this.page++;

      const fragment = document.createDocumentFragment();
      items.forEach(item => {
        const el = this.createItemElement(item);
        fragment.appendChild(el);
      });

      this.container.insertBefore(fragment, this.sentinel);
      this.liveRegion.textContent = `Loaded ${items.length} more images`;

    } catch (error) {
      this.showError();
    } finally {
      this.loading = false;
      this.hideSpinner();
    }
  }

  createItemElement(item) {
    const div = document.createElement('div');
    div.className = 'gallery-item';
    div.innerHTML = `<img src="${item.src}" alt="${item.alt}" loading="lazy" width="${item.width}" height="${item.height}">`;
    return div;
  }

  showSpinner() { /* show loading indicator */ }
  hideSpinner() { /* hide loading indicator */ }
  showError() { /* show retry button */ }
}
```

---

## 11. Comparison Slider

Two overlapping images with a draggable divider.

```html
<div class="compare-slider" role="img" aria-label="Before and after comparison">
  <div class="compare-before">
    <img src="before.webp" alt="Before renovation" width="800" height="600">
    <span class="compare-label">Before</span>
  </div>
  <div class="compare-after">
    <img src="after.webp" alt="After renovation" width="800" height="600">
    <span class="compare-label">After</span>
  </div>
  <div class="compare-handle" role="slider" aria-label="Comparison slider" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50" tabindex="0">
    <div class="compare-handle-line"></div>
    <div class="compare-handle-grip">
      <svg width="24" height="24"><path d="M8 5l-5 7 5 7M16 5l5 7-5 7" stroke="white" stroke-width="2" fill="none"/></svg>
    </div>
  </div>
</div>
```

```css
.compare-slider {
  position: relative;
  overflow: hidden;
  cursor: col-resize;
  border-radius: 12px;
}

.compare-before, .compare-after {
  position: absolute;
  inset: 0;
}

.compare-after { z-index: 1; }
.compare-before { z-index: 2; clip-path: inset(0 50% 0 0); }

.compare-before img, .compare-after img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.compare-label {
  position: absolute;
  top: 16px;
  padding: 4px 12px;
  background: rgba(0, 0, 0, 0.6);
  color: white;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
}

.compare-before .compare-label { left: 16px; }
.compare-after .compare-label { right: 16px; }

.compare-handle {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  z-index: 3;
  width: 4px;
  transform: translateX(-50%);
}

.compare-handle-line {
  width: 2px;
  height: 100%;
  background: white;
  margin: 0 auto;
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.3);
}

.compare-handle-grip {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 44px;
  height: 44px;
  background: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.compare-handle:focus-visible .compare-handle-grip {
  outline: 3px solid #2563eb;
}
```

```javascript
class CompareSlider {
  constructor(el) {
    this.el = el;
    this.before = el.querySelector('.compare-before');
    this.handle = el.querySelector('.compare-handle');
    this.position = 50;

    // Pointer events
    this.el.addEventListener('pointerdown', (e) => this.onStart(e));

    // Keyboard
    this.handle.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') { e.preventDefault(); this.setPosition(this.position - 2); }
      if (e.key === 'ArrowRight') { e.preventDefault(); this.setPosition(this.position + 2); }
    });
  }

  onStart(e) {
    e.preventDefault();
    this.el.setPointerCapture(e.pointerId);
    this.onMove(e);

    const onMove = (e) => this.onMove(e);
    const onEnd = () => {
      this.el.removeEventListener('pointermove', onMove);
      this.el.removeEventListener('pointerup', onEnd);
    };

    this.el.addEventListener('pointermove', onMove);
    this.el.addEventListener('pointerup', onEnd);
  }

  onMove(e) {
    const rect = this.el.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const pct = (x / rect.width) * 100;
    this.setPosition(pct);
  }

  setPosition(pct) {
    this.position = Math.max(0, Math.min(100, pct));
    this.before.style.clipPath = `inset(0 ${100 - this.position}% 0 0)`;
    this.handle.style.left = `${this.position}%`;
    this.handle.setAttribute('aria-valuenow', Math.round(this.position));
  }
}

document.querySelectorAll('.compare-slider').forEach(el => new CompareSlider(el));
```

---

## 12. Gallery Filter Animation

Animated filtering with layout transitions.

```css
.filter-bar {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 8px 16px;
  border: 1px solid #d1d5db;
  border-radius: 999px;
  background: white;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.filter-btn.active {
  background: #111827;
  color: white;
  border-color: #111827;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
}

.gallery-grid-item {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.gallery-grid-item.hidden {
  opacity: 0;
  transform: scale(0.9);
  position: absolute;
  pointer-events: none;
}
```

```javascript
class FilterGallery {
  constructor(container) {
    this.buttons = container.querySelectorAll('.filter-btn');
    this.items = container.querySelectorAll('.gallery-grid-item');

    this.buttons.forEach(btn => {
      btn.addEventListener('click', () => this.filter(btn.dataset.category, btn));
    });
  }

  filter(category, activeBtn) {
    // Update buttons
    this.buttons.forEach(b => b.classList.remove('active'));
    activeBtn.classList.add('active');

    // Filter items
    this.items.forEach(item => {
      const show = category === 'all' || item.dataset.category === category;
      item.classList.toggle('hidden', !show);
    });
  }
}
```

---

## 13. Carousel Accessibility Checklist

| Requirement | Implementation |
|-------------|---------------|
| Container role | `role="region"` + `aria-roledescription="carousel"` + `aria-label` |
| Each slide | `role="group"` + `aria-roledescription="slide"` + `aria-label="Slide N of M"` |
| Hidden slides | `aria-hidden="true"` + `tabindex="-1"` on focusable children |
| Dots | `role="tablist"` wrapper, each dot `role="tab"` + `aria-selected` + `aria-label` |
| Arrows | `aria-label="Previous slide"` / `"Next slide"` + disabled state |
| Keyboard nav | Arrow keys, Enter/Space on controls, Tab through visible content |
| Autoplay | Pause button, pause on hover/focus, respect `prefers-reduced-motion` |
| Live region | `aria-live="polite"` to announce slide changes |
| Focus management | Never auto-advance away from focused content |
| Touch | Swipe support with scroll-snap, no swipe-trapping entire page |
