# Responsive Image Recipes — srcset, picture, LQIP & Lazy Loading

Production-ready code patterns for responsive images, format fallbacks, lazy loading, and placeholder techniques.

---

## 1. Width-Based srcset (Most Common Pattern)

The browser selects the best image based on viewport width and device pixel ratio.

```html
<img
  srcset="
    photo-320.webp   320w,
    photo-480.webp   480w,
    photo-640.webp   640w,
    photo-768.webp   768w,
    photo-1024.webp 1024w,
    photo-1200.webp 1200w,
    photo-1920.webp 1920w"
  sizes="
    (max-width: 480px) 100vw,
    (max-width: 768px) 100vw,
    (max-width: 1024px) 50vw,
    33.33vw"
  src="photo-1024.webp"
  alt="Descriptive alt text"
  loading="lazy"
  decoding="async"
  width="1920"
  height="1280"
>
```

### How `sizes` Works

The `sizes` attribute tells the browser how wide the image will display at each breakpoint, **before** downloading. The browser then picks the smallest `srcset` candidate that satisfies the display width at the device's pixel ratio.

| Viewport | `sizes` Value | Display Width | On 2x Device | Image Selected |
|----------|--------------|---------------|---------------|----------------|
| 375px | 100vw | 375px | 750px | photo-768.webp |
| 768px | 100vw | 768px | 1536px | photo-1920.webp |
| 1024px | 50vw | 512px | 1024px | photo-1024.webp |
| 1440px | 33.33vw | 480px | 960px | photo-1024.webp |

### Common `sizes` Recipes

```html
<!-- Full-width hero -->
sizes="100vw"

<!-- Full-width with max-width container (1200px) -->
sizes="(max-width: 1200px) 100vw, 1200px"

<!-- Two-column layout on desktop, full on mobile -->
sizes="(max-width: 768px) 100vw, 50vw"

<!-- Three-column grid with gap -->
sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, calc(33.33vw - 32px)"

<!-- Sidebar layout (content takes 66%) -->
sizes="(max-width: 768px) 100vw, 66vw"

<!-- Fixed-width card image (always 300px display) -->
sizes="300px"
```

---

## 2. DPR-Based srcset (Fixed-Size Images)

For images that are always the same display size (logos, avatars, icons).

```html
<!-- Logo: always 200px wide -->
<img
  srcset="logo.png 1x, logo@2x.png 2x, logo@3x.png 3x"
  src="logo.png"
  alt="Acme Corp"
  width="200"
  height="60"
>

<!-- Avatar: always 48px -->
<img
  srcset="avatar-48.webp 1x, avatar-96.webp 2x, avatar-144.webp 3x"
  src="avatar-48.webp"
  alt="Jane Smith"
  width="48"
  height="48"
  class="avatar"
>
```

---

## 3. Art Direction with `<picture>`

Serve different crops or compositions at different breakpoints.

### Hero Image — Different Crops

```html
<picture>
  <!-- Mobile: tight vertical crop, subject centered -->
  <source
    media="(max-width: 639px)"
    srcset="hero-mobile-640.avif 640w, hero-mobile-960.avif 960w"
    sizes="100vw"
    type="image/avif"
  >
  <source
    media="(max-width: 639px)"
    srcset="hero-mobile-640.webp 640w, hero-mobile-960.webp 960w"
    sizes="100vw"
    type="image/webp"
  >

  <!-- Tablet: medium crop -->
  <source
    media="(max-width: 1023px)"
    srcset="hero-tablet-1024.avif 1024w, hero-tablet-1536.avif 1536w"
    sizes="100vw"
    type="image/avif"
  >
  <source
    media="(max-width: 1023px)"
    srcset="hero-tablet-1024.webp 1024w, hero-tablet-1536.webp 1536w"
    sizes="100vw"
    type="image/webp"
  >

  <!-- Desktop: full wide composition -->
  <source
    srcset="hero-desktop-1920.avif 1920w, hero-desktop-2560.avif 2560w"
    sizes="100vw"
    type="image/avif"
  >
  <source
    srcset="hero-desktop-1920.webp 1920w, hero-desktop-2560.webp 2560w"
    sizes="100vw"
    type="image/webp"
  >

  <!-- Ultimate fallback: JPEG, no srcset -->
  <img
    src="hero-desktop-1920.jpg"
    alt="Team collaborating in a bright modern office with floor-to-ceiling windows"
    width="1920"
    height="800"
    fetchpriority="high"
  >
</picture>
```

### Format Fallback Only (Same Crop)

```html
<picture>
  <source srcset="photo.avif" type="image/avif">
  <source srcset="photo.webp" type="image/webp">
  <img src="photo.jpg" alt="Sunset over the ocean" width="800" height="533" loading="lazy">
</picture>
```

### Dark Mode Image Variant

```html
<picture>
  <source srcset="logo-dark.svg" media="(prefers-color-scheme: dark)">
  <source srcset="logo-light.svg" media="(prefers-color-scheme: light)">
  <img src="logo-light.svg" alt="Company logo" width="200" height="60">
</picture>
```

---

## 4. Native Lazy Loading

### Basic Usage

```html
<!-- Below the fold: lazy load -->
<img src="photo.webp" loading="lazy" width="800" height="600" alt="...">

<!-- Above the fold (LCP candidate): eager + high priority -->
<img src="hero.webp" loading="eager" fetchpriority="high" width="1920" height="800" alt="...">

<!-- Preload the LCP image in <head> -->
<link rel="preload" as="image" href="hero.webp" type="image/webp">

<!-- Preload with srcset -->
<link
  rel="preload"
  as="image"
  href="hero-1920.webp"
  imagesrcset="hero-640.webp 640w, hero-1024.webp 1024w, hero-1920.webp 1920w"
  imagesizes="100vw"
>
```

### Rules for Lazy Loading

1. Never lazy-load the LCP image (typically the hero or first visible image).
2. Always pair `loading="lazy"` with explicit `width` and `height` to prevent CLS.
3. Add `decoding="async"` for non-critical images.
4. The browser's internal threshold varies (~1250-2500px below viewport in Chrome).
5. Use `fetchpriority="high"` on the single most important image, `fetchpriority="low"` on background/decorative images.

---

## 5. Intersection Observer Lazy Loading

For cases where native `loading="lazy"` is insufficient (e.g., background images, video, iframes).

```html
<img
  class="lazy"
  data-src="photo-full.webp"
  data-srcset="photo-480.webp 480w, photo-768.webp 768w, photo-1200.webp 1200w"
  data-sizes="(max-width: 768px) 100vw, 50vw"
  src="placeholder-blur.webp"
  alt="Mountain landscape"
  width="1200"
  height="800"
>
```

```javascript
// Lazy loading with Intersection Observer
function initLazyLoading() {
  const images = document.querySelectorAll('img.lazy');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;

          // Swap data attributes to real attributes
          if (img.dataset.srcset) img.srcset = img.dataset.srcset;
          if (img.dataset.sizes) img.sizes = img.dataset.sizes;
          img.src = img.dataset.src;

          // Fade in when loaded
          img.addEventListener('load', () => {
            img.classList.add('loaded');
          });

          img.classList.remove('lazy');
          observer.unobserve(img);
        }
      });
    }, {
      rootMargin: '200px 0px', // start loading 200px before entering viewport
      threshold: 0.01
    });

    images.forEach(img => observer.observe(img));
  } else {
    // Fallback: load all images immediately
    images.forEach(img => {
      img.src = img.dataset.src;
      if (img.dataset.srcset) img.srcset = img.dataset.srcset;
      if (img.dataset.sizes) img.sizes = img.dataset.sizes;
    });
  }
}

document.addEventListener('DOMContentLoaded', initLazyLoading);
```

```css
img.lazy {
  opacity: 0;
  transition: opacity 0.4s ease;
}
img.lazy.loaded, img.loaded {
  opacity: 1;
}
```

---

## 6. LQIP (Low Quality Image Placeholder) — Blur-Up

### HTML Structure

```html
<div class="image-wrapper" style="aspect-ratio: 3/2;">
  <!-- Tiny placeholder (inline base64 or tiny URL) -->
  <img
    class="lqip"
    src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
    alt=""
    aria-hidden="true"
  >
  <!-- Full resolution image -->
  <img
    class="full-image lazy"
    data-src="photo-1200.webp"
    data-srcset="photo-480.webp 480w, photo-768.webp 768w, photo-1200.webp 1200w"
    data-sizes="(max-width: 768px) 100vw, 50vw"
    alt="Golden hour landscape with rolling hills"
    width="1200"
    height="800"
  >
</div>
```

### CSS

```css
.image-wrapper {
  position: relative;
  overflow: hidden;
  background-color: #e5e7eb; /* fallback gray */
}

.lqip {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: blur(20px);
  transform: scale(1.1); /* prevent blur edges from showing */
  transition: opacity 0.6s ease;
  z-index: 1;
}

.full-image {
  position: relative;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 0.6s ease;
  z-index: 2;
}

.full-image.loaded {
  opacity: 1;
}

.full-image.loaded + .lqip,
.full-image.loaded ~ .lqip {
  /* When using adjacent sibling, reverse the DOM order */
}

/* Alternative: hide LQIP when full image loads */
.image-wrapper.revealed .lqip {
  opacity: 0;
  pointer-events: none;
}
```

### JavaScript

```javascript
function initBlurUp() {
  const wrappers = document.querySelectorAll('.image-wrapper');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const wrapper = entry.target;
        const fullImage = wrapper.querySelector('.full-image');

        if (fullImage.dataset.srcset) fullImage.srcset = fullImage.dataset.srcset;
        if (fullImage.dataset.sizes) fullImage.sizes = fullImage.dataset.sizes;

        fullImage.addEventListener('load', () => {
          fullImage.classList.add('loaded');
          wrapper.classList.add('revealed');
        });

        fullImage.src = fullImage.dataset.src;
        observer.unobserve(wrapper);
      }
    });
  }, { rootMargin: '300px' });

  wrappers.forEach(w => observer.observe(w));
}

initBlurUp();
```

### Generating LQIP Server-Side

```bash
# Using sharp (Node.js)
sharp input.jpg
  .resize(32)           # tiny width
  .jpeg({ quality: 20 }) # heavy compression
  .toBuffer()            # get base64 for inline use

# Using ImageMagick
convert input.jpg -resize 32x -quality 20 lqip.jpg

# Using sqip (SVG-based LQIP — produces artistic SVG placeholder)
npx sqip -i input.jpg -o placeholder.svg -n 16
```

---

## 7. BlurHash Implementation

### Server: Generate BlurHash

```javascript
// Node.js with sharp + blurhash
import { encode } from 'blurhash';
import sharp from 'sharp';

async function generateBlurHash(imagePath) {
  const { data, info } = await sharp(imagePath)
    .raw()
    .ensureAlpha()
    .resize(32, 32, { fit: 'inside' })
    .toBuffer({ resolveWithObject: true });

  const hash = encode(
    new Uint8ClampedArray(data),
    info.width,
    info.height,
    4, // componentX (4 is good default)
    3  // componentY
  );

  return hash; // e.g., "LKN]Rv%2Tw=w]~RBVZRi"
}
```

### Client: Decode and Display

```javascript
import { decode } from 'blurhash';

function blurHashToCanvas(hash, width = 32, height = 32) {
  const pixels = decode(hash, width, height);
  const canvas = document.createElement('canvas');
  canvas.width = width;
  canvas.height = height;
  const ctx = canvas.getContext('2d');
  const imageData = ctx.createImageData(width, height);
  imageData.data.set(pixels);
  ctx.putImageData(imageData, 0, 0);
  return canvas;
}

// Usage
const canvas = blurHashToCanvas('LKN]Rv%2Tw=w]~RBVZRi', 32, 32);
canvas.style.width = '100%';
canvas.style.height = '100%';
document.querySelector('.placeholder').appendChild(canvas);
```

### React Component

```jsx
import { Blurhash } from 'react-blurhash';

function ImageWithBlurHash({ src, hash, alt, width, height }) {
  const [loaded, setLoaded] = useState(false);

  return (
    <div style={{ position: 'relative', aspectRatio: `${width}/${height}` }}>
      {!loaded && (
        <Blurhash
          hash={hash}
          width="100%"
          height="100%"
          resolutionX={32}
          resolutionY={32}
          punch={1}
          style={{ position: 'absolute', inset: 0 }}
        />
      )}
      <img
        src={src}
        alt={alt}
        width={width}
        height={height}
        onLoad={() => setLoaded(true)}
        style={{
          opacity: loaded ? 1 : 0,
          transition: 'opacity 0.4s ease',
          width: '100%',
          height: '100%',
          objectFit: 'cover',
        }}
      />
    </div>
  );
}
```

---

## 8. ThumbHash Implementation

ThumbHash is a successor to BlurHash with better detail preservation and transparency support.

```javascript
// Server: generate ThumbHash
import { rgbaToThumbHash } from 'thumbhash';
import sharp from 'sharp';

async function generateThumbHash(imagePath) {
  const { data, info } = await sharp(imagePath)
    .resize(100, 100, { fit: 'inside' })
    .ensureAlpha()
    .raw()
    .toBuffer({ resolveWithObject: true });

  const hash = rgbaToThumbHash(info.width, info.height, data);
  return Buffer.from(hash).toString('base64'); // ~28 bytes
}

// Client: decode ThumbHash to data URL
import { thumbHashToDataURL } from 'thumbhash';

function decodeThumbHash(base64Hash) {
  const hash = Uint8Array.from(atob(base64Hash), c => c.charCodeAt(0));
  return thumbHashToDataURL(hash); // returns data:image/png;base64,...
}
```

---

## 9. Dominant Color Placeholder

### Extract Dominant Color Server-Side

```javascript
// Node.js with sharp
import sharp from 'sharp';

async function getDominantColor(imagePath) {
  const { dominant } = await sharp(imagePath).stats();
  return `rgb(${dominant.r}, ${dominant.g}, ${dominant.b})`;
}

// Returns e.g., "rgb(58, 123, 213)"
```

### Usage in HTML

```html
<!-- Server renders the color inline -->
<div class="image-container" style="background-color: rgb(58, 123, 213); aspect-ratio: 16/9;">
  <img
    src="photo.webp"
    alt="Blue sky over mountains"
    loading="lazy"
    width="1200"
    height="675"
    style="opacity: 0; transition: opacity 0.3s ease;"
    onload="this.style.opacity=1"
  >
</div>
```

---

## 10. Image CDN URL Patterns

### Cloudinary

```html
<!-- Auto format, auto quality, resize to 800px width -->
<img src="https://res.cloudinary.com/demo/image/upload/f_auto,q_auto,w_800/sample.jpg" alt="...">

<!-- With srcset -->
<img
  srcset="
    https://res.cloudinary.com/demo/image/upload/f_auto,q_auto,w_400/sample.jpg 400w,
    https://res.cloudinary.com/demo/image/upload/f_auto,q_auto,w_800/sample.jpg 800w,
    https://res.cloudinary.com/demo/image/upload/f_auto,q_auto,w_1200/sample.jpg 1200w"
  sizes="(max-width: 768px) 100vw, 50vw"
  src="https://res.cloudinary.com/demo/image/upload/f_auto,q_auto,w_800/sample.jpg"
  alt="..."
>

<!-- LQIP: tiny blurred version -->
<img src="https://res.cloudinary.com/demo/image/upload/f_auto,q_10,w_32,e_blur:1000/sample.jpg" alt="">
```

### imgix

```html
<img
  srcset="
    https://example.imgix.net/photo.jpg?auto=format&w=400 400w,
    https://example.imgix.net/photo.jpg?auto=format&w=800 800w,
    https://example.imgix.net/photo.jpg?auto=format&w=1200 1200w"
  sizes="(max-width: 768px) 100vw, 50vw"
  src="https://example.imgix.net/photo.jpg?auto=format&w=800"
  alt="..."
>
```

### Vercel/Next.js Image

```jsx
import Image from 'next/image';

<Image
  src="/photo.jpg"
  alt="Description"
  width={1200}
  height={800}
  sizes="(max-width: 768px) 100vw, 50vw"
  placeholder="blur"
  blurDataURL="data:image/jpeg;base64,..."
  priority={false}  // true for LCP image
/>
```

---

## 11. CLS Prevention Checklist

1. Always set `width` and `height` attributes on `<img>` tags.
2. Use CSS `aspect-ratio` on containers wrapping images.
3. Use a placeholder strategy (dominant color, BlurHash, skeleton).
4. Never insert images dynamically above existing visible content.
5. For responsive images, `sizes` should accurately reflect displayed width.
6. For ads/embeds, reserve explicit space with min-height.
7. Font-display: swap does not cause image CLS but be aware of text-shift interaction.

```css
/* Universal CLS prevention for images */
img {
  max-width: 100%;
  height: auto;
}

/* Container-based approach */
.responsive-image-container {
  position: relative;
  overflow: hidden;
  aspect-ratio: var(--img-ratio, 16/9);
}
.responsive-image-container img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```
