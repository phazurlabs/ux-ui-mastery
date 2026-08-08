# Media Formats and Performance

Choosing a format, and everything that keeps media from wrecking Core Web Vitals.

## Image Formats

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

## Performance Optimization

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
