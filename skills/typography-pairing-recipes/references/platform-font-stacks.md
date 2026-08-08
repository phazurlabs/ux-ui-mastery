# Platform Font Stacks — System Fonts, Variable Fonts, and Loading Strategies

> System font stacks for every platform, web-safe fallback chains, variable font technology, font loading strategies, and performance optimization.

---

## System Font Stacks by Platform

### macOS / iOS

```css
/* San Francisco (SF Pro) — Default since macOS 10.11 / iOS 9 */
font-family: -apple-system, BlinkMacSystemFont, system-ui, sans-serif;

/* SF Pro has two optical sizes, auto-selected by the OS: */
/* SF Pro Text: optimized for sizes below 20pt */
/* SF Pro Display: optimized for sizes 20pt and above */

/* SF Mono — System monospace */
font-family: 'SF Mono', ui-monospace, monospace;

/* New York — System serif (since macOS Catalina / iOS 13) */
font-family: ui-serif, 'New York', Georgia, serif;

/* iOS 26 Liquid Glass Note:
   Liquid Glass overlays may alter text rendering.
   Use semantic system fonts for native feel. */
```

**Available weights**: SF Pro supports 100-900 (Ultralight to Black).
**Variable font**: SF Pro is a variable font with `wght` and `opsz` axes.
**Rounded variant**: SF Pro Rounded available for friendly UI contexts.

### Windows

```css
/* Segoe UI — Default since Windows 7 */
font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;

/* Segoe UI Variable — Windows 11 variable font */
font-family: 'Segoe UI Variable', 'Segoe UI', system-ui, sans-serif;

/* Consolas / Cascadia — System monospace */
font-family: 'Cascadia Code', 'Cascadia Mono', 'Consolas', ui-monospace, monospace;

/* Segoe UI Emoji — Emoji rendering (Windows 10+) */
/* Include after main sans-serif for proper emoji fallback */

/* Windows 11 additions: */
/* Segoe Fluent Icons — icon font */
/* Segoe UI Variable — replaces fixed Segoe UI */
```

**Available weights**: Segoe UI: Light (300), Semilight (350), Regular (400), Semibold (600), Bold (700).
**Segoe UI Variable**: Full 100-900 range on Windows 11.

### Linux

```css
/* No single default — varies by distro */
/* Ubuntu */
font-family: 'Ubuntu Sans', 'Ubuntu', system-ui, sans-serif;

/* Fedora / RHEL */
font-family: 'Red Hat Text', 'Cantarell', system-ui, sans-serif;

/* GNOME default */
font-family: 'Cantarell', system-ui, sans-serif;

/* KDE default */
font-family: 'Noto Sans', system-ui, sans-serif;

/* Universal Linux fallback */
font-family: system-ui, 'Noto Sans', 'Liberation Sans', 'DejaVu Sans', sans-serif;

/* Linux monospace */
font-family: 'Ubuntu Mono', 'Liberation Mono', 'DejaVu Sans Mono', ui-monospace, monospace;
```

### Android

```css
/* Roboto — Default since Android 4.0 */
font-family: 'Roboto', system-ui, sans-serif;

/* Roboto Flex — Variable font on Android 12+ */
/* Supports: wght, wdth, opsz, GRAD, XTRA, YOPQ, YTAS, YTDE, YTFI, YTLC, YTUC */

/* Noto Sans — Fallback for non-Latin scripts */
font-family: 'Roboto', 'Noto Sans', system-ui, sans-serif;

/* Android monospace */
font-family: 'Roboto Mono', 'Droid Sans Mono', ui-monospace, monospace;

/* Material 3 Expressive (2025):
   Uses Roboto Flex with emphasis curves for M3 Expressive components.
   Axis: wght 100-1000, wdth 25-151, opsz 8-144 */
```

### Cross-Platform Universal Stack

```css
/* The modern system font stack — works everywhere */
font-family:
  system-ui,                   /* Modern browsers: OS default */
  -apple-system,               /* Safari on macOS/iOS */
  BlinkMacSystemFont,          /* Chrome on macOS */
  'Segoe UI',                  /* Windows */
  'Roboto',                    /* Android */
  'Noto Sans',                 /* Linux / CJK fallback */
  'Ubuntu',                    /* Ubuntu */
  'Cantarell',                 /* GNOME */
  'Helvetica Neue',            /* Older macOS */
  'Arial',                     /* Universal fallback */
  sans-serif;                  /* Generic family */

/* Cross-platform monospace */
font-family:
  ui-monospace,                /* Modern system mono */
  'SF Mono',                   /* macOS */
  'Cascadia Code',             /* Windows 11 */
  'Consolas',                  /* Windows */
  'JetBrains Mono',            /* Commonly installed by devs */
  'Fira Code',                 /* Commonly installed */
  'Ubuntu Mono',               /* Ubuntu */
  'Liberation Mono',           /* Linux */
  'DejaVu Sans Mono',          /* Linux fallback */
  'Courier New',               /* Universal */
  monospace;                   /* Generic family */

/* Cross-platform serif */
font-family:
  ui-serif,                    /* Modern system serif */
  'New York',                  /* macOS Catalina+ */
  'Georgia',                   /* Universal, screen-optimized */
  'Cambria',                   /* Windows */
  'Noto Serif',                /* Linux / CJK */
  'Times New Roman',           /* Universal fallback */
  serif;                       /* Generic family */
```

---

## Web-Safe Fallback Chains

### Sans-Serif Fallbacks

```css
/* Tier 1: Maximum compatibility (99%+ coverage) */
font-family: Arial, Helvetica, sans-serif;

/* Tier 2: Modern cross-platform */
font-family: -apple-system, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;

/* Tier 3: Specific Google Font with fallbacks */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
```

### Serif Fallbacks

```css
/* Tier 1: Maximum compatibility */
font-family: Georgia, 'Times New Roman', Times, serif;

/* Tier 2: Modern */
font-family: 'Charter', 'Bitstream Charter', Georgia, 'Times New Roman', serif;

/* Tier 3: Google Font with metric-compatible fallback */
font-family: 'Lora', 'Georgia', 'Cambria', serif;
```

### Monospace Fallbacks

```css
/* Tier 1: Maximum compatibility */
font-family: 'Courier New', Courier, monospace;

/* Tier 2: Modern */
font-family: 'Consolas', 'Monaco', 'Andale Mono', monospace;

/* Tier 3: Developer-oriented */
font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', 'Consolas', monospace;
```

### Metric-Compatible Fallback Fonts

To minimize layout shift (CLS) when web fonts load, use metric-compatible fallbacks:

| Web Font | Metric-Compatible System Font | Notes |
|----------|------------------------------|-------|
| Inter | Roboto, Arial | Similar metrics, slightly wider |
| Roboto | Arial, Helvetica | Very close metrics |
| Open Sans | Arial | Slightly wider; adjust letter-spacing |
| Lato | Arial | Similar x-height |
| Playfair Display | Georgia | Taller x-height; adjust |
| Source Sans 3 | Arial, Helvetica | Close metrics |
| Merriweather | Georgia | Wider; adjust line length |
| Lora | Georgia | Good match |
| Source Serif 4 | Georgia, Charter | Close metrics |

---

## Variable Font Technology

### What Are Variable Fonts?

A single font file that contains an entire family across multiple axes of variation (weight, width, slant, etc.). Instead of loading `font-regular.woff2`, `font-bold.woff2`, `font-italic.woff2` as separate files, one variable font file handles all variations.

### Standard Axes (Registered)

| Axis Tag | Name | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `wght` | Weight | 1-999 | 400 | Thin to Black |
| `wdth` | Width | 50-200 | 100 | Condensed to Expanded (%) |
| `slnt` | Slant | -90-90 | 0 | Oblique angle in degrees |
| `ital` | Italic | 0-1 | 0 | Off (0) or On (1) |
| `opsz` | Optical Size | varies | varies | Auto-adjusts for display vs text |

### Custom Axes (Font-Specific)

| Axis Tag | Font | Description |
|----------|------|-------------|
| `SOFT` | Fraunces | Softness of terminals (0-100) |
| `WONK` | Fraunces | Wonky/quirky alternate forms (0-1) |
| `MONO` | Recursive | Sans to mono interpolation (0-1) |
| `CASL` | Recursive | Casual style (0-1) |
| `CRSV` | Recursive | Cursive italics (0-1) |
| `GRAD` | Roboto Flex | Grade / thickening without width change |
| `XTRA` | Roboto Flex | Extra width for counters |
| `YOPQ` | Roboto Flex | Y-axis opacity (thin/thick strokes) |
| `FILL` | Material Symbols | Icon fill (0-1) |

### Variable Font Implementation

```css
/* 1. Load the variable font */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Variable.woff2') format('woff2-variations');
  font-weight: 100 900;        /* Declare full weight range */
  font-display: swap;
  font-style: normal;
}

/* Italic variant (separate file for most variable fonts) */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Variable-Italic.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-display: swap;
  font-style: italic;
}

/* 2. Use standard axes with CSS properties */
body {
  font-family: 'Inter', sans-serif;
  font-weight: 400;             /* Standard CSS property for wght */
}

h1 {
  font-weight: 750;             /* Any value 100-900, not just multiples of 100 */
}

/* 3. Use any axis with font-variation-settings */
.expressive-heading {
  font-variation-settings:
    'wght' 800,
    'wdth' 110,
    'slnt' -5;
}

/* 4. Optical size (auto-adjusts in supporting browsers) */
.auto-optical {
  font-optical-sizing: auto;    /* Browser selects opsz based on font-size */
}

.manual-optical {
  font-optical-sizing: none;
  font-variation-settings: 'opsz' 48;  /* Force display optical size */
}

/* 5. Animate variable fonts */
@keyframes weight-pulse {
  0%   { font-weight: 400; }
  50%  { font-weight: 700; }
  100% { font-weight: 400; }
}

.animated-text {
  animation: weight-pulse 2s ease-in-out infinite;
}

/* 6. Responsive weight with viewport */
h1 {
  font-weight: clamp(600, 500 + 0.5vw, 800);
  /* Note: font-weight animation with clamp requires browser interpolation support */
}
```

### Benefits of Variable Fonts

| Benefit | Detail |
|---------|--------|
| **File size** | 1 variable font file < 4+ static font files (typically 30-60% savings) |
| **Flexibility** | Any weight/width value, not limited to predefined steps |
| **Animation** | Smooth transitions between any axis values |
| **Responsive** | Weight/width can adapt to viewport or container |
| **Optical sizing** | Auto-optimization for different display sizes |
| **Fewer requests** | 1-2 HTTP requests vs 4-8 for static fonts |

### Popular Variable Fonts

| Font | Axes | Source |
|------|------|--------|
| Inter | wght (100-900) | Google Fonts |
| Roboto Flex | wght, wdth, opsz, GRAD, XTRA, YOPQ + more | Google Fonts |
| Source Sans 3 | wght (200-900) | Google Fonts |
| Fraunces | wght, opsz, SOFT, WONK | Google Fonts |
| Recursive | wght, CASL, MONO, slnt, CRSV | Google Fonts |
| Newsreader | wght, opsz | Google Fonts |
| Literata | wght, opsz | Google Fonts |
| Commissioner | wght (100-900) | Google Fonts |
| Bricolage Grotesque | wght, opsz, wdth | Google Fonts |
| Anybody | wght, wdth | Google Fonts |
| Geist Sans | wght (100-900) | Vercel (self-host) |

---

## Font Loading Strategies

### font-display Values

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter.woff2') format('woff2');
  font-display: swap;  /* Choose your strategy */
}
```

| Value | Behavior | Block Period | Swap Period | Best For |
|-------|----------|-------------|-------------|----------|
| `auto` | Browser decides | ~3s | Infinite | Default (avoid using) |
| `block` | Invisible text, then swap | 3s | Infinite | Icon fonts, where FOUT is worse than FOIT |
| `swap` | Fallback immediately, swap when ready | 0 | Infinite | Body text (recommended default) |
| `fallback` | Brief invisible, swap if fast | 100ms | 3s | Headings (balances FOIT/FOUT) |
| `optional` | Brief invisible, may not swap | 100ms | 0 | Non-critical fonts, slow connections |

**Recommendation**: Use `swap` for body text and `fallback` or `optional` for decorative/display fonts.

### Preloading Critical Fonts

```html
<!-- Preload your most critical font (usually body text) -->
<link
  rel="preload"
  href="/fonts/Inter-Variable.woff2"
  as="font"
  type="font/woff2"
  crossorigin="anonymous"
>

<!-- Only preload 1-2 fonts maximum. More defeats the purpose. -->

<!-- For Google Fonts: preconnect to the CDN -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

**Rules for preloading**:
1. Only preload fonts used above the fold.
2. Maximum 1-2 preloaded fonts (preloading everything helps nothing).
3. Always include `crossorigin="anonymous"` (even for same-origin fonts).
4. Always specify `type="font/woff2"` to avoid double downloads.

### FOUT/FOIT Prevention

**FOUT** (Flash of Unstyled Text): Fallback font shows, then swaps to web font (layout shift).
**FOIT** (Flash of Invisible Text): No text shows until web font loads (content delay).

```css
/* Strategy 1: Size-adjusted fallback (eliminates CLS from FOUT) */
@font-face {
  font-family: 'Inter Fallback';
  src: local('Arial');
  size-adjust: 107%;           /* Adjust to match Inter's metrics */
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}

body {
  font-family: 'Inter', 'Inter Fallback', sans-serif;
}

/* Strategy 2: Use @font-face descriptors for metric matching */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter.woff2') format('woff2');
  font-display: swap;
  /* These override metrics to match system fallback */
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}

/* Strategy 3: Font Loading API for fine-grained control */
```

```js
// JavaScript Font Loading API
async function loadFonts() {
  const inter = new FontFace('Inter', 'url(/fonts/Inter.woff2)', {
    weight: '100 900',
    display: 'swap',
  });

  try {
    const loaded = await inter.load();
    document.fonts.add(loaded);
    document.documentElement.classList.add('fonts-loaded');
  } catch (err) {
    console.warn('Font loading failed:', err);
    // Fallback fonts continue to work
  }
}

// Only load fonts if not already cached
if (!document.fonts.check('400 1em Inter')) {
  loadFonts();
}
```

```css
/* Progressive enhancement with .fonts-loaded class */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.fonts-loaded body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}
```

---

## Performance Optimization

### Font Subsetting

Remove unused glyphs to reduce file size dramatically.

```css
/* Unicode-range subsetting: browser only downloads needed files */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-latin.woff2') format('woff2');
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
  /* Latin subset */
}

@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-latin-ext.woff2') format('woff2');
  font-display: swap;
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
  /* Latin Extended subset — only downloaded if page uses these characters */
}

@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-cyrillic.woff2') format('woff2');
  font-display: swap;
  unicode-range: U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
  /* Cyrillic subset — only downloaded for Russian/Ukrainian/etc content */
}
```

**Subsetting tools**:
- **Google Fonts**: Auto-subsets by unicode-range (handled automatically).
- **glyphhanger**: CLI tool for custom subsetting: `glyphhanger --whitelist="US_ASCII" --subset=Inter.woff2`
- **pyftsubset** (fonttools): `pyftsubset Inter.ttf --unicodes="U+0000-00FF" --flavor=woff2`
- **Fontsquirrel Generator**: Web-based subsetting with GUI.

### File Size Comparison

| Format | Typical Size (Inter Regular) | Browser Support |
|--------|------------------------------|-----------------|
| TTF | 320 KB | 99%+ (legacy) |
| WOFF | 180 KB | 99%+ |
| WOFF2 | 100 KB | 97%+ (use this) |
| Variable WOFF2 | 280 KB (replaces 4-6 static files) | 96%+ |

**Always use WOFF2**. There is no reason to serve TTF or WOFF in 2025+.

### Self-Hosting vs CDN

| Factor | Self-Hosting | Google Fonts CDN |
|--------|-------------|------------------|
| **Performance** | Faster (same origin, no DNS lookup) | Extra DNS + connection (2 origins) |
| **Caching** | Your cache policy | Shared cache removed in Chrome 86+ |
| **Privacy** | No third-party requests | Sends user IP to Google |
| **GDPR** | Compliant by default | Requires consent in EU (case law) |
| **Reliability** | Your uptime | Google's uptime (99.99%) |
| **File size** | You control subsetting | Auto-optimized by Google |
| **HTTP/3** | If your server supports it | Google supports it |

**Recommendation**: Self-host for production. Use Google Fonts CDN only for prototyping.

### Self-Hosting Setup

```bash
# 1. Download from Google Fonts (use google-webfonts-helper or fontsource)
npm install @fontsource-variable/inter

# 2. Or download WOFF2 files directly and place in /public/fonts/
```

```css
/* 3. Define @font-face with local() check first */
@font-face {
  font-family: 'Inter';
  src:
    local('Inter'),                               /* Check if already installed */
    url('/fonts/Inter-Variable.woff2') format('woff2-variations'),
    url('/fonts/Inter-Variable.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6,
    U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122,
    U+FEFF, U+FFFD;
}
```

### Performance Budget

| Metric | Target | Why |
|--------|--------|-----|
| Total font payload | < 150 KB | Keeps FCP/LCP fast |
| Number of font files | 1-3 | Fewer HTTP requests |
| Number of font families | 1-2 | Cognitive simplicity + performance |
| Time to first text | < 100ms | Use system fallback with font-display: swap |
| CLS from font swap | < 0.05 | Use size-adjust and metric overrides |

### Font Loading Performance Checklist

```
[ ] Using WOFF2 format exclusively
[ ] Preloading 1-2 critical fonts with <link rel="preload">
[ ] Using font-display: swap (or fallback/optional)
[ ] Subsetting to only needed unicode ranges
[ ] Self-hosting fonts (not using Google Fonts CDN in production)
[ ] Using size-adjust on fallback font to prevent CLS
[ ] Variable font for families needing 3+ weights
[ ] Preconnecting to font CDN if using external fonts
[ ] Total font payload under 150 KB
[ ] No render-blocking font CSS in <head> (async load non-critical fonts)
[ ] Font files served with Cache-Control: max-age=31536000 (1 year)
[ ] Using local() in @font-face src to skip download if installed
```

---

## Quick Reference: Font Format Support (2025)

| Format | Extension | Support | Use Case |
|--------|-----------|---------|----------|
| WOFF2 | .woff2 | 97%+ | Primary format. Always use. |
| WOFF | .woff | 99%+ | Fallback only if needed for IE11 |
| Variable WOFF2 | .woff2 | 96%+ | Use for families with 3+ weights |
| TTF/OTF | .ttf/.otf | 99%+ | Development/design tools only |
| SVG Font | .svg | Deprecated | Never use |
| EOT | .eot | IE only | Never use in 2025+ |

---

## Cross-References

- **font-pairing-catalog.md** — 105+ font pairings with CSS stacks
- **type-scale-systems.md** — Complete type scale recipes
- **platform-visual-standards** — iOS 26, Material 3, platform-specific guidance
- **design-token-presets** — Typography tokens in complete token systems
- **accessibility-inclusive-design** — Font size minimums, dyslexia-friendly fonts
