# Hero Section Patterns — 50+ Production-Ready Variants

## Hero Design Philosophy

The hero is the most important block on any page. It occupies 100% of the above-the-fold viewport on first load, making it the single most viewed element of any website. Research shows users form an opinion about a site within 50 milliseconds — and the hero is what they see. A hero must accomplish three things simultaneously: communicate the value proposition (what), establish visual credibility (trust), and present a clear next action (CTA).

Hero blocks have the highest design variance of any section type because they carry the brand's first impression. Unlike feature grids or pricing tables that follow structural conventions, heroes demand creative differentiation while still respecting usability principles.

---

## Hero Anatomy — Universal Structure

Every hero, regardless of variant, contains these zones:

### Pre-Header Zone (optional)
- Announcement banner or pill badge above the headline
- Size: 14px, font-weight 500, often colored background pill
- Example: "New: AI-powered analytics now available"
- Spacing: 16-24px below nav, 16-20px above headline

### Headline Zone
- Primary heading: H1, only one per page
- Desktop: 48-72px, font-weight 700-800, line-height 1.05-1.15
- Letter-spacing: -0.02 to -0.04em (tighter for large text)
- Max-width: 12-18ch for short punchy headlines, up to 28ch for descriptive
- Color: high contrast against background (WCAG AAA preferred for heroes)

### Subheadline Zone
- Supporting text explaining the value proposition
- Desktop: 18-24px, font-weight 400, line-height 1.5-1.6
- Color: 60-70% opacity or gray-600 on light backgrounds
- Max-width: 50-60ch for optimal readability
- Spacing: 16-24px below headline

### CTA Zone
- Primary button: 16-18px, padding 16px 32px, border-radius 8-12px
- Secondary action: text link or ghost button beside primary
- Spacing: 24-32px below subheadline
- On mobile: buttons stack vertically, full-width

### Visual Zone
- Image, video, illustration, or interactive element
- Position varies by variant (right, left, background, below)
- Always optimized: WebP/AVIF, responsive srcset, priority loading (no lazy)

### Social Proof Zone (optional)
- Logo bar, customer count, or trust badges below CTA
- Spacing: 40-64px below CTA zone
- Logos: grayscale, 32-40px height, 24-32px gap between

---

## Breakpoint Specifications

All hero variants follow these breakpoint rules unless noted otherwise:

| Property | 2xl (1440+) | xl (1024-1439) | lg (768-1023) | md (480-767) | sm (320-479) |
|----------|-------------|----------------|---------------|--------------|--------------|
| H1 size | 64-72px | 56-64px | 44-52px | 36-40px | 32-36px |
| Subhead size | 20-24px | 18-22px | 18-20px | 16-18px | 16px |
| Section height | 90-100vh | 85-95vh | auto | auto | auto |
| Horizontal pad | 80px | 48-64px | 32px | 24px | 16px |
| Top padding | 120-160px | 100-140px | 80-100px | 64-80px | 56-64px |
| Bottom padding | 80-120px | 64-96px | 64-80px | 48-64px | 40-48px |
| Max content width | 1200-1400px | 1024-1200px | 100% | 100% | 100% |
| Image size | 50% of row | 45% of row | 100% width | 100% width | 100% width |

---

## Variant 1: Centered Hero

The most versatile and safest hero pattern. Works for any product, any audience.

### Layout Specs
- All content centered horizontally
- Headline max-width: 680px (centered)
- Subheadline max-width: 540px (centered)
- CTA buttons: centered, inline on desktop, stacked on mobile
- Optional image below text: full-width or contained in device frame
- Background: solid color, subtle gradient, or pattern

### Spacing
- Top padding: 140px (below nav)
- Headline to subheadline: 20px
- Subheadline to CTA: 32px
- CTA to optional image: 64px
- CTA to social proof bar: 48px
- Total section height: 90-100vh or auto with min-height 600px

### Responsive Behavior
- All breakpoints maintain centered alignment
- Headline shrinks per type scale
- CTA buttons: inline at `lg`+, stacked full-width at `md` and below
- Optional image: maintains aspect ratio, width scales to container
- Social proof logos: wrap to second row at `md`, hide labels at `sm`

### Production Code (React/TSX)
```tsx
interface CenteredHeroProps {
  badge?: string;
  title: string;
  subtitle: string;
  primaryCta: { label: string; href: string };
  secondaryCta?: { label: string; href: string };
  trustedBy?: { logos: Array<{ src: string; alt: string }> };
  image?: { src: string; alt: string };
}

export function CenteredHero({
  badge,
  title,
  subtitle,
  primaryCta,
  secondaryCta,
  trustedBy,
  image,
}: CenteredHeroProps) {
  return (
    <section className="relative overflow-hidden bg-white">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 pt-24 sm:pt-32 lg:pt-40 pb-16 sm:pb-20 lg:pb-24">
        <div className="text-center">
          {badge && (
            <div className="mb-6 inline-flex items-center rounded-full bg-blue-50 px-4 py-1.5 text-sm font-medium text-blue-700 ring-1 ring-inset ring-blue-600/20">
              {badge}
            </div>
          )}
          <h1 className="mx-auto max-w-3xl text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-gray-900 leading-[1.1]">
            {title}
          </h1>
          <p className="mx-auto mt-6 max-w-xl text-lg sm:text-xl text-gray-600 leading-relaxed">
            {subtitle}
          </p>
          <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
            <a
              href={primaryCta.href}
              className="w-full sm:w-auto rounded-lg bg-blue-600 px-8 py-3.5 text-base font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 transition-colors"
            >
              {primaryCta.label}
            </a>
            {secondaryCta && (
              <a
                href={secondaryCta.href}
                className="w-full sm:w-auto text-base font-semibold text-gray-700 hover:text-gray-900 transition-colors"
              >
                {secondaryCta.label} <span aria-hidden="true">&rarr;</span>
              </a>
            )}
          </div>
          {trustedBy && (
            <div className="mt-16">
              <p className="text-sm font-medium text-gray-500 mb-6">
                Trusted by leading companies
              </p>
              <div className="flex flex-wrap items-center justify-center gap-x-8 gap-y-4">
                {trustedBy.logos.map((logo) => (
                  <img
                    key={logo.alt}
                    src={logo.src}
                    alt={logo.alt}
                    className="h-8 w-auto opacity-60 grayscale hover:opacity-100 hover:grayscale-0 transition-all"
                  />
                ))}
              </div>
            </div>
          )}
        </div>
        {image && (
          <div className="mt-16 sm:mt-20">
            <img
              src={image.src}
              alt={image.alt}
              className="w-full rounded-xl shadow-2xl ring-1 ring-gray-900/10"
              loading="eager"
              fetchPriority="high"
            />
          </div>
        )}
      </div>
    </section>
  );
}
```

### Accessibility Notes
- H1 is the first heading on the page; verify heading hierarchy
- CTA links have descriptive text (avoid "Click here")
- Badge uses sufficient color contrast (4.5:1 minimum)
- Images have meaningful alt text describing the content
- Focus-visible outlines on all interactive elements

---

## Variant 2: Split Hero (Text Left / Image Right)

The workhorse SaaS hero. 60% of top SaaS landing pages use this pattern.

### Layout Specs
- Two-column layout: text 50-55% width, image 45-50% width
- Text column: left-aligned, vertically centered
- Image column: can overflow section bounds (bleeding right)
- Gap between columns: 48-80px
- Headline max-width: none (constrained by column width)

### Spacing
- Top padding: 120-160px (below nav)
- Bottom padding: 80-120px
- Internal text spacing: same as centered hero
- Image may extend below section bottom for overlap effect

### Responsive Behavior
- `2xl`-`xl`: Side-by-side, 55/45 split
- `lg`: Side-by-side, 50/50 split, reduce gap to 32px
- `md`: Stack — image below text, both full-width
- `sm`: Stack — image below text, reduced padding

### Production Code (React/TSX)
```tsx
interface SplitHeroProps {
  badge?: string;
  title: string;
  subtitle: string;
  primaryCta: { label: string; href: string };
  secondaryCta?: { label: string; href: string };
  image: { src: string; alt: string };
  imagePosition?: 'right' | 'left';
}

export function SplitHero({
  badge,
  title,
  subtitle,
  primaryCta,
  secondaryCta,
  image,
  imagePosition = 'right',
}: SplitHeroProps) {
  return (
    <section className="relative overflow-hidden bg-white">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 pt-20 sm:pt-28 lg:pt-36 pb-16 sm:pb-20 lg:pb-28">
        <div className={`lg:grid lg:grid-cols-12 lg:gap-x-12 xl:gap-x-16 items-center ${imagePosition === 'left' ? 'lg:flex-row-reverse' : ''}`}>
          <div className={`lg:col-span-6 ${imagePosition === 'left' ? 'lg:col-start-7' : ''}`}>
            {badge && (
              <div className="mb-6 inline-flex items-center rounded-full bg-blue-50 px-4 py-1.5 text-sm font-medium text-blue-700 ring-1 ring-inset ring-blue-600/20">
                {badge}
              </div>
            )}
            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-gray-900 leading-[1.1]">
              {title}
            </h1>
            <p className="mt-6 text-lg sm:text-xl text-gray-600 leading-relaxed max-w-xl">
              {subtitle}
            </p>
            <div className="mt-8 flex flex-col sm:flex-row gap-4">
              <a
                href={primaryCta.href}
                className="rounded-lg bg-blue-600 px-8 py-3.5 text-base font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 transition-colors text-center"
              >
                {primaryCta.label}
              </a>
              {secondaryCta && (
                <a
                  href={secondaryCta.href}
                  className="text-base font-semibold text-gray-700 hover:text-gray-900 transition-colors flex items-center justify-center sm:justify-start"
                >
                  {secondaryCta.label} <span aria-hidden="true" className="ml-1">&rarr;</span>
                </a>
              )}
            </div>
          </div>
          <div className={`mt-12 lg:mt-0 lg:col-span-6 ${imagePosition === 'left' ? 'lg:col-start-1 lg:row-start-1' : ''}`}>
            <img
              src={image.src}
              alt={image.alt}
              className="w-full rounded-xl shadow-2xl ring-1 ring-gray-900/10"
              loading="eager"
              fetchPriority="high"
            />
          </div>
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 3: Video Background Hero

High-impact, cinematic. Use for brands, agencies, and premium products.

### Layout Specs
- Full-viewport video background (100vw x 100vh or min-height 700px)
- Dark overlay: 50-70% opacity black or brand-dark gradient
- Content centered over video
- Headline: white text, large (56-80px), text-shadow for legibility
- Subheadline: white at 80% opacity
- Video: autoplay, muted, loop, no controls
- Fallback: poster image for slow connections

### Technical Requirements
- Video format: MP4 (H.264) for compatibility, WebM for quality
- Video resolution: 1920x1080 minimum, 2560x1440 for retina
- Video file size: target under 5MB for fast load (use compression)
- Poster image: display immediately while video loads
- `prefers-reduced-motion`: pause video, show poster image only

### Responsive Behavior
- `xl`+: Full video visible, object-fit: cover
- `lg`: Video still visible, may crop more aggressively
- `md`-`sm`: Replace video with poster image (save bandwidth), or use shorter clip

### Production Code (React/TSX)
```tsx
interface VideoHeroProps {
  title: string;
  subtitle: string;
  primaryCta: { label: string; href: string };
  videoSrc: string;
  posterSrc: string;
  overlayOpacity?: number;
}

export function VideoHero({
  title,
  subtitle,
  primaryCta,
  videoSrc,
  posterSrc,
  overlayOpacity = 0.6,
}: VideoHeroProps) {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      <video
        autoPlay
        muted
        loop
        playsInline
        poster={posterSrc}
        className="absolute inset-0 w-full h-full object-cover"
        aria-hidden="true"
      >
        <source src={videoSrc} type="video/mp4" />
      </video>
      <div
        className="absolute inset-0 bg-black"
        style={{ opacity: overlayOpacity }}
        aria-hidden="true"
      />
      <div className="relative z-10 mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center py-24">
        <h1 className="text-4xl sm:text-5xl lg:text-7xl font-bold text-white tracking-tight leading-[1.1]">
          {title}
        </h1>
        <p className="mt-6 text-lg sm:text-xl text-white/80 max-w-2xl mx-auto leading-relaxed">
          {subtitle}
        </p>
        <div className="mt-10">
          <a
            href={primaryCta.href}
            className="rounded-lg bg-white px-8 py-4 text-base font-semibold text-gray-900 shadow-lg hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white transition-colors"
          >
            {primaryCta.label}
          </a>
        </div>
      </div>
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
        <svg className="w-6 h-6 text-white/60" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
        </svg>
      </div>
    </section>
  );
}
```

### CSS for reduced motion
```css
@media (prefers-reduced-motion: reduce) {
  video {
    display: none;
  }
  .video-hero {
    background-image: var(--poster-image);
    background-size: cover;
    background-position: center;
  }
  .animate-bounce {
    animation: none;
  }
}
```

---

## Variant 4: Product Screenshot Hero

Best for SaaS, showing the actual product UI as the primary visual.

### Layout Specs
- Text section: centered above screenshot, or left-aligned with screenshot right
- Screenshot: browser chrome frame or clean rounded container
- Screenshot angle: 0deg (flat) for clarity, or 2-5deg perspective tilt for depth
- Shadow: large diffused shadow (0 25px 50px -12px rgba(0,0,0,0.25))
- Screenshot max-width: 1100px, border-radius: 12px
- Optional: floating UI element cards around the screenshot for feature callouts

### Responsive Behavior
- `xl`+: Full screenshot visible with generous padding
- `lg`: Screenshot scales down, maintains aspect ratio
- `md`: Screenshot full-width, may crop sides or scroll horizontally
- `sm`: Screenshot full-width, consider showing mobile version of the product

### Production Code (React/TSX)
```tsx
interface ScreenshotHeroProps {
  badge?: string;
  title: string;
  subtitle: string;
  primaryCta: { label: string; href: string };
  secondaryCta?: { label: string; href: string };
  screenshot: { src: string; alt: string };
  showBrowserChrome?: boolean;
}

export function ScreenshotHero({
  badge,
  title,
  subtitle,
  primaryCta,
  secondaryCta,
  screenshot,
  showBrowserChrome = true,
}: ScreenshotHeroProps) {
  return (
    <section className="bg-gradient-to-b from-white to-gray-50 overflow-hidden">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 pt-24 sm:pt-32 lg:pt-40 pb-0">
        <div className="text-center">
          {badge && (
            <div className="mb-6 inline-flex items-center rounded-full bg-blue-50 px-4 py-1.5 text-sm font-medium text-blue-700 ring-1 ring-inset ring-blue-600/20">
              {badge}
            </div>
          )}
          <h1 className="mx-auto max-w-4xl text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-gray-900 leading-[1.1]">
            {title}
          </h1>
          <p className="mx-auto mt-6 max-w-2xl text-lg sm:text-xl text-gray-600 leading-relaxed">
            {subtitle}
          </p>
          <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
            <a href={primaryCta.href} className="w-full sm:w-auto rounded-lg bg-blue-600 px-8 py-3.5 text-base font-semibold text-white shadow-sm hover:bg-blue-500 transition-colors">
              {primaryCta.label}
            </a>
            {secondaryCta && (
              <a href={secondaryCta.href} className="text-base font-semibold text-gray-700 hover:text-gray-900 transition-colors">
                {secondaryCta.label} &rarr;
              </a>
            )}
          </div>
        </div>
        <div className="mt-16 sm:mt-20">
          {showBrowserChrome ? (
            <div className="rounded-t-xl bg-gray-800 p-2 shadow-2xl ring-1 ring-white/10">
              <div className="flex items-center gap-1.5 px-2 pb-2">
                <span className="h-3 w-3 rounded-full bg-red-500/80" />
                <span className="h-3 w-3 rounded-full bg-yellow-500/80" />
                <span className="h-3 w-3 rounded-full bg-green-500/80" />
                <span className="ml-4 flex-1 rounded-md bg-gray-700 h-6" />
              </div>
              <img src={screenshot.src} alt={screenshot.alt} className="w-full rounded-b-lg" loading="eager" fetchPriority="high" />
            </div>
          ) : (
            <img src={screenshot.src} alt={screenshot.alt} className="w-full rounded-xl shadow-2xl ring-1 ring-gray-900/10" loading="eager" fetchPriority="high" />
          )}
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 5: Dark Mode Hero

Premium feel, high contrast, perfect for developer tools and creative products.

### Layout Specs
- Background: gray-900 (#111827), gray-950 (#030712), or pure black (#000000)
- Text: white for headlines, white/70-80% for body text
- CTA button: white bg with dark text (inverted), or brand-colored
- Accent colors: more vivid on dark backgrounds (blue-400 instead of blue-600)
- Optional: subtle dot grid, gradient mesh, or noise texture overlay

### Color System for Dark Heroes
- Background: `#0A0A0B` to `#1A1A2E`
- Headline: `#FFFFFF` (100% white)
- Body text: `rgba(255,255,255,0.7)` or `#A1A1AA`
- Primary CTA: `#FFFFFF` bg, `#0A0A0B` text
- Secondary CTA: `rgba(255,255,255,0.8)` text with underline
- Links: `#60A5FA` (blue-400) or brand accent
- Borders: `rgba(255,255,255,0.1)`

### Production Code (React/TSX)
```tsx
export function DarkHero({ title, subtitle, primaryCta, secondaryCta, badge }: CenteredHeroProps) {
  return (
    <section className="relative bg-gray-950 overflow-hidden">
      {/* Gradient background effect */}
      <div className="absolute inset-0" aria-hidden="true">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl" />
        <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl" />
      </div>
      <div className="relative mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 pt-24 sm:pt-32 lg:pt-40 pb-16 sm:pb-20 lg:pb-24">
        <div className="text-center">
          {badge && (
            <div className="mb-6 inline-flex items-center rounded-full bg-white/10 px-4 py-1.5 text-sm font-medium text-blue-300 ring-1 ring-inset ring-white/10">
              {badge}
            </div>
          )}
          <h1 className="mx-auto max-w-3xl text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-white leading-[1.1]">
            {title}
          </h1>
          <p className="mx-auto mt-6 max-w-xl text-lg sm:text-xl text-gray-400 leading-relaxed">
            {subtitle}
          </p>
          <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
            <a href={primaryCta.href} className="w-full sm:w-auto rounded-lg bg-white px-8 py-3.5 text-base font-semibold text-gray-900 hover:bg-gray-100 transition-colors">
              {primaryCta.label}
            </a>
            {secondaryCta && (
              <a href={secondaryCta.href} className="text-base font-semibold text-gray-300 hover:text-white transition-colors">
                {secondaryCta.label} &rarr;
              </a>
            )}
          </div>
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 6: SaaS Sign-Up Hero

Conversion-optimized hero with an inline form for immediate sign-up or demo request.

### Layout Specs
- Split layout: text left (55%), form right (45%)
- Or centered: text above, form below
- Form: email input + submit button (minimal), or name + email + company + submit (lead gen)
- Form card: white card with shadow on colored/gray background, or borderless on white bg
- Social login buttons optional below form

### Form Specifications
- Input height: 48-52px
- Input font-size: 16px (prevents iOS zoom)
- Input border-radius: 8px
- Input border: 1px solid gray-300, focus: 2px solid blue-500
- Submit button: full-width of form, same height as inputs
- Error states: red border + message below input
- Loading state: spinner in submit button, disabled state

### Production Code (React/TSX)
```tsx
export function SaaSSignUpHero({ title, subtitle }: { title: string; subtitle: string }) {
  return (
    <section className="bg-gradient-to-br from-blue-50 to-indigo-50">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 pt-20 sm:pt-28 lg:pt-36 pb-16 sm:pb-20 lg:pb-28">
        <div className="lg:grid lg:grid-cols-2 lg:gap-x-16 items-center">
          <div>
            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-gray-900 leading-[1.1]">
              {title}
            </h1>
            <p className="mt-6 text-lg text-gray-600 leading-relaxed max-w-lg">{subtitle}</p>
            <div className="mt-8 flex items-center gap-4 text-sm text-gray-500">
              <span className="flex items-center gap-1.5">
                <svg className="h-4 w-4 text-green-500" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" /></svg>
                Free 14-day trial
              </span>
              <span className="flex items-center gap-1.5">
                <svg className="h-4 w-4 text-green-500" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" /></svg>
                No credit card required
              </span>
            </div>
          </div>
          <div className="mt-12 lg:mt-0">
            <div className="rounded-2xl bg-white p-8 shadow-xl ring-1 ring-gray-900/5">
              <h2 className="text-xl font-semibold text-gray-900 mb-6">Start your free trial</h2>
              <form className="space-y-4">
                <div>
                  <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">Full name</label>
                  <input id="name" type="text" className="w-full rounded-lg border border-gray-300 px-4 py-3 text-base focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 outline-none transition" />
                </div>
                <div>
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">Work email</label>
                  <input id="email" type="email" className="w-full rounded-lg border border-gray-300 px-4 py-3 text-base focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 outline-none transition" />
                </div>
                <div>
                  <label htmlFor="company" className="block text-sm font-medium text-gray-700 mb-1">Company</label>
                  <input id="company" type="text" className="w-full rounded-lg border border-gray-300 px-4 py-3 text-base focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 outline-none transition" />
                </div>
                <button type="submit" className="w-full rounded-lg bg-blue-600 px-8 py-3.5 text-base font-semibold text-white hover:bg-blue-500 transition-colors">
                  Start free trial
                </button>
              </form>
              <p className="mt-4 text-xs text-gray-500 text-center">
                By signing up, you agree to our Terms of Service and Privacy Policy.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
```

---

## Variant 7: App Store Hero (Mobile Preview)

Optimized for mobile apps with device mockups and download badges.

### Layout Specs
- Split layout: text left, phone mockup right
- Or centered: text above, phone mockup below (centered)
- Phone mockup: realistic iPhone/Android frame, or flat device outline
- App screenshots: inside device frame, 9:19.5 aspect ratio (iPhone)
- Download badges: App Store + Google Play, standard badge sizes (135x40px)
- Star rating: optional, above badges

### Phone Mockup Specifications
- iPhone frame: 375x812px viewport, device frame adds ~20px border
- Display size on desktop: 280-320px wide
- Shadow: 0 20px 40px rgba(0,0,0,0.15)
- Rotation: 0deg (straight) or slight 5deg tilt
- Can show multiple phones for different screens

### Responsive Behavior
- `xl`+: Side-by-side, phone at natural size
- `lg`: Side-by-side, phone scaled to 240px wide
- `md`: Stacked, phone centered, max 280px wide
- `sm`: Stacked, phone 220px wide

---

## Variant 8: Hero with Animated Text

Dynamic hero with rotating or typing headline animation.

### Layout Specs
- Same as Centered Hero structure
- Animated word/phrase within the headline: different color or underline decoration
- Animation types: typewriter, word rotation (fade or slide), morphing text
- Animation timing: 2-4 seconds per word, smooth easing
- Fallback: static text for prefers-reduced-motion

### Animation Specifications
- Typewriter: monospace or variable font, blinking cursor, 50-80ms per character
- Word rotation: 3-5 words cycling, 3s per word, 500ms transition
- Fade: opacity 0→1 with slight translateY(8px→0)
- Slide: translateY(100%→0) with overflow hidden on container

### Production Code (React/TSX)
```tsx
import { useState, useEffect } from 'react';

interface AnimatedHeroProps {
  titlePrefix: string;
  rotatingWords: string[];
  titleSuffix?: string;
  subtitle: string;
  primaryCta: { label: string; href: string };
}

export function AnimatedTextHero({ titlePrefix, rotatingWords, titleSuffix, subtitle, primaryCta }: AnimatedHeroProps) {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % rotatingWords.length);
    }, 3000);
    return () => clearInterval(interval);
  }, [rotatingWords.length]);

  return (
    <section className="bg-white">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 pt-24 sm:pt-32 lg:pt-40 pb-16 sm:pb-20 lg:pb-24 text-center">
        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-gray-900 leading-[1.1]">
          {titlePrefix}{' '}
          <span className="relative inline-block">
            <span
              key={currentIndex}
              className="text-blue-600 inline-block motion-safe:animate-fade-in-up"
            >
              {rotatingWords[currentIndex]}
            </span>
          </span>
          {titleSuffix && ` ${titleSuffix}`}
        </h1>
        <p className="mx-auto mt-6 max-w-xl text-lg sm:text-xl text-gray-600 leading-relaxed">{subtitle}</p>
        <div className="mt-8">
          <a href={primaryCta.href} className="rounded-lg bg-blue-600 px-8 py-3.5 text-base font-semibold text-white hover:bg-blue-500 transition-colors">
            {primaryCta.label}
          </a>
        </div>
      </div>
    </section>
  );
}
```

```css
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in-up { animation: fade-in-up 0.5s ease-out; }

@media (prefers-reduced-motion: reduce) {
  .motion-safe\:animate-fade-in-up { animation: none; }
}
```

---

## Variant 9: Gradient Mesh Hero

Visually striking with complex multi-color gradient backgrounds.

### Layout Specs
- Background: CSS mesh gradient or multiple radial gradients layered
- Content: centered text with high-contrast white or dark text
- No image needed — the gradient IS the visual
- Optional: subtle grain/noise texture overlay for depth

### Gradient Recipes
```css
/* Sunset Mesh */
background: #1a1a2e;
background-image:
  radial-gradient(at 40% 20%, hsla(28, 100%, 74%, 0.3) 0px, transparent 50%),
  radial-gradient(at 80% 0%, hsla(189, 100%, 56%, 0.2) 0px, transparent 50%),
  radial-gradient(at 0% 50%, hsla(355, 100%, 93%, 0.2) 0px, transparent 50%),
  radial-gradient(at 80% 50%, hsla(340, 100%, 76%, 0.2) 0px, transparent 50%),
  radial-gradient(at 0% 100%, hsla(22, 100%, 77%, 0.3) 0px, transparent 50%);

/* Aurora Mesh */
background: #0f172a;
background-image:
  radial-gradient(at 27% 37%, hsla(215, 98%, 61%, 0.15) 0px, transparent 50%),
  radial-gradient(at 97% 21%, hsla(125, 98%, 72%, 0.15) 0px, transparent 50%),
  radial-gradient(at 52% 99%, hsla(354, 98%, 61%, 0.15) 0px, transparent 50%),
  radial-gradient(at 10% 29%, hsla(256, 96%, 67%, 0.15) 0px, transparent 50%);

/* Ocean Mesh */
background: #020617;
background-image:
  radial-gradient(at 0% 0%, hsla(212, 98%, 50%, 0.2) 0px, transparent 50%),
  radial-gradient(at 100% 0%, hsla(180, 98%, 50%, 0.15) 0px, transparent 50%),
  radial-gradient(at 50% 100%, hsla(240, 98%, 50%, 0.15) 0px, transparent 50%);
```

---

## Variant 10: Minimal Text-Only Hero

For brands confident enough to let typography carry the message.

### Layout Specs
- No images, no illustrations, no visual gimmicks
- Headline: oversized (72-120px desktop), bold or black weight
- Subheadline: moderate size, generous max-width
- Background: solid white or solid dark
- CTA: understated, text link or minimal button
- Spacing: extra generous — let the type breathe

### Typography Specifications
- Headline: 80-120px desktop, 48-64px mobile
- Line-height: 0.95-1.05 (very tight for large display type)
- Letter-spacing: -0.04em (very tight tracking)
- Font: display or serif for editorial feel, sans-serif for tech
- Consider variable font weight animation on hover

---

## Variant 11-15: Quick Reference Specs

### 11. Hero with Social Proof Bar
Same as Centered Hero + logo row positioned 48-64px below CTA. Logos: grayscale, 32px height, 24-32px gap. Label: "Trusted by" in 13px gray-500 above logos.

### 12. Hero with Feature Highlights
Same as Centered Hero + 3 icon-text blocks below CTA (48-64px spacing). Icons: 24x24px in colored circles (40x40px). Text: 14px bold + 14px regular. Grid: 3-col inline, 1-col stacked on mobile.

### 13. E-Commerce Product Hero
Split layout: image gallery left (60%), product info right (40%). Gallery: main image + thumbnail row. Info: title, price, color/size selectors, add-to-cart button, shipping info.

### 14. Hero with Floating Cards
Centered text with 3-5 small cards positioned absolutely around the text area. Cards: 120-180px wide, slight rotation (2-5deg), drop shadow. Cards hide on mobile (layout-shift risk).

### 15. Full-Screen Hero
Height: 100vh with scroll indicator (bouncing arrow or "scroll" text). Content vertically and horizontally centered. Scroll indicator: positioned 32px from bottom, animated bounce (1s ease-in-out infinite).

---

## Variant 16-25: SaaS & Tech Heroes

### 16. Hero with Terminal
Split or centered layout with animated terminal block. Terminal: dark bg (#1E1E1E), rounded-lg, monospace font (14-16px), colored syntax. Animation: line-by-line typing with cursor. Border: 1px white/10.

### 17. Hero with Code Block
Same as terminal but with syntax-highlighted code. Language selector tabs optional. Copy button in top-right. Popular with developer tool companies.

### 18. Dashboard Preview Hero
Centered text above an angled dashboard screenshot. Angle: CSS perspective transform (rotateX(2deg) rotateY(-5deg)). Shadow: multi-layered for depth. Optional: floating metric cards around screenshot.

### 19. Hero with Announcement Banner
Slim banner above the headline: pill-shaped, colored background, "New" badge + text + arrow link. Height: 32-40px. Position: immediately above H1, centered. Click: links to announcement page.

### 20. Hero with Dual CTA
Primary button + secondary button side by side. Primary: filled, high contrast. Secondary: outlined/ghost or text link. Gap: 16px. On mobile: stack vertically, both full-width. Secondary should be clearly less prominent.

### 21. Glassmorphism Hero
Colorful background (gradient or image) with frosted glass content card overlaid. Card: background rgba(255,255,255,0.1), backdrop-filter: blur(16px), border: 1px solid rgba(255,255,255,0.2), border-radius: 24px, padding: 48px. Text: white.

### 22. Hero with Countdown
Event/launch countdown timer below headline. Timer: 4 boxes (days, hours, minutes, seconds), monospace font, 48-64px numbers. Labels below each box. Update: JavaScript setInterval every 1 second. Fallback: static "Coming Soon" if JS disabled.

### 23. Hero with Video Thumbnail
Centered or split layout with video thumbnail (16:9) and centered play button (64px circle). Click: opens modal with YouTube/Vimeo embed. Play button: white with 50% black bg circle, hover scale(1.1). Thumbnail: screenshot from video.

### 24. Magazine Hero
Editorial layout with large featured image (60-70% width), overlaid text block at bottom-left. Text block: white bg card with padding, or dark overlay strip. Subtitle: category tag above headline. Used by media, editorial, and blog sites.

### 25. AI Product Hero
Centered text with animated AI visual (particles, neural network viz, or pulsing orb). Optional: interactive prompt input field in hero. Input mimics chat interface. Background: dark with subtle animated gradient or particle system.

---

## Variant 26-35: Industry-Specific Heroes

### 26. Portfolio Hero
Name in large type (72-96px), role/title below (24px), brief intro (18px). Minimal, lots of whitespace. Optional: subtle background animation or gradient. CTA: "View my work" scroll link. Background: clean white or off-black.

### 27. Agency Hero
Bold statement headline (3-5 words maximum, 80-120px). Showreel video link or autoplay. Navigation integrated into hero. Full-bleed design. Dark or high-contrast. CTA: "Start a project" or "View our work."

### 28. Blog Post Hero
Title (H1, 40-56px) + meta info (author avatar, name, date, read time) + featured image. Meta: 14px, gray-600, inline with dividers. Featured image: full-width below text, 16:9 or 3:2 ratio, rounded-lg. Category tag above title.

### 29. Event Hero
Event name (H1), date + time + location, register CTA. Optional: countdown timer, speaker avatars, venue image background. Date: prominent, 24-32px. Location: with map pin icon. CTA: high contrast "Register Now" button.

### 30. Landing Page A/B Split Hero
Two variants ready for testing. Variant A: benefit-focused headline. Variant B: feature-focused headline. Same structure, different copy. Track: CTA click rate per variant.

### 31-35. Additional Variants
31. **Startup Pitch Hero** — Big problem statement headline + solution subhead + demo CTA
32. **Open Source Hero** — Project name + GitHub stars badge + "Get Started" + installation code block
33. **API Documentation Hero** — API name + version badge + "Explore Docs" + quickstart code
34. **Marketplace Hero** — Search bar prominent + category chips + trending items
35. **Community/Forum Hero** — Welcome message + member count + "Join" CTA + recent activity

---

## Variant 36-50: Specialized & Advanced Heroes

### 36. Parallax Hero
Background image moves at different scroll speed than content. Parallax factor: 0.3-0.5 (subtle). Implementation: CSS transform with scroll event or Intersection Observer. Disable on mobile (performance). Fallback: fixed background-attachment.

### 37. Split-Screen Hero
50/50 split with distinct colors/images on each side. Left: dark bg + text. Right: image or contrasting color + text. Each side has its own CTA. Used for dual-audience sites (e.g., "For buyers" / "For sellers").

### 38. Sticky Hero
Hero remains visible (sticky top) while subsequent content scrolls over it. Creates a "peek-through" or "reveal" effect. Implementation: position: sticky on hero, z-index lower than next section. Works well with dark hero + white next section.

### 39. Scroll-Activated Hero
Content animates in on scroll. Headline fades/slides in first, then subheadline, then CTA. Uses Intersection Observer or scroll-triggered animations. Subtle: 200-400ms stagger, 30-50px translate distance.

### 40. Interactive Hero
User interaction changes the visual. Examples: mouse-following gradient, draggable 3D object, hover-reactive particles, cursor-trailing effects. Implementation: requestAnimationFrame + mouse event listeners. Disable complex effects on mobile.

### 41. Map Hero
Full-width map background (Mapbox/Google Maps) with overlaid content card. Used by location-based services, real estate, travel. Map: muted/custom style, no UI clutter. Content card: white, shadowed, positioned bottom-left or center.

### 42. Image Carousel Hero
Multiple hero images cycling automatically or with dots/arrows. Each slide has its own headline + CTA. Transition: fade (preferred for heroes) or slide. Timing: 5-7 seconds per slide. Pause on hover. A11y: announce slide changes to screen readers.

### 43. Gradient Text Hero
Headline text with gradient fill instead of solid color. CSS: background-clip: text with gradient background. High impact, modern feel. Ensure gradient provides sufficient contrast against the background. Fallback: solid color for older browsers.

### 44. Outline Text Hero
Headline with outlined (stroked) text instead of filled. CSS: -webkit-text-stroke: 2px currentColor with transparent color. Or SVG text with stroke and no fill. Fill on hover for interactive effect.

### 45. Asymmetric Hero
Non-standard layout breaking the grid. Image bleeds off one edge, text positioned unconventionally. Creates visual tension and memorability. Requires careful responsive handling — simplify to standard layout on mobile.

### 46. Hero with Sidebar
Hero content with a persistent sidebar visible (dashboard context). Hero area: reduced width (calc(100% - sidebar-width)). Content: left-aligned, same patterns as other heroes but narrower. Common in app marketing pages viewed within the app.

### 47. Hero with Breadcrumb
For interior pages: breadcrumb trail above H1. Breadcrumb: 14px, gray-500, chevron separators. Background: subtle (gray-50 or light gradient). Shorter than homepage hero (300-400px). Used for category, product, and sub-pages.

### 48. Segmented Hero
Hero divided into 2-4 segments/cards, each linking to a different section or product. Cards: equal width, full hero height, hover effect (scale or overlay). Used by multi-product companies or portfolio sites.

### 49. Personalized Hero
Dynamic content based on user segment, referral source, or previous visits. Implementation: server-side rendering or client-side based on cookies/URL params. Default: generic hero for new visitors. Track: conversion rate per personalization variant.

### 50. Micro-Interaction Hero
Every element has a subtle interaction: buttons scale on hover, text has cursor-following highlight, background responds to scroll position, icons animate on view. Cumulative effect creates a "living" hero. Performance budget: keep under 16ms per frame.

---

## Hero Performance Best Practices

1. **LCP (Largest Contentful Paint)**: The hero image/video is usually the LCP element. Load it with `fetchPriority="high"` and `loading="eager"`. Never lazy-load the hero image.
2. **CLS (Cumulative Layout Shift)**: Set explicit width/height or aspect-ratio on hero images. Reserve vertical space for fonts loading (font-display: swap + size-adjust).
3. **FID/INP**: Avoid heavy JavaScript in the hero. Animations should use CSS transforms (GPU-accelerated), not JavaScript-driven layout changes.
4. **Image formats**: Use AVIF with WebP fallback and JPEG fallback. Use `<picture>` with `srcset` for responsive images.
5. **Video**: Load poster image immediately. Defer video load until after LCP. Use `preload="none"` or `preload="metadata"` on mobile.
6. **Fonts**: Preload the hero headline font. Use `font-display: swap` or `font-display: optional`. Provide accurate `size-adjust` to prevent layout shift.
7. **Above the fold**: Inline critical CSS for the hero block. Defer all non-critical CSS and JavaScript.
