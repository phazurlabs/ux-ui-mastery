# Color Combination Recipes — 50+ Ready-to-Use Palettes

Production-ready color combination recipes organized by type and mood. Each recipe includes 5-8 color values (oklch + hex), recommended usage for each color, contrast scores for key pairings, mood/feeling description, and complete CSS custom properties.

---

## Category 1: Monochromatic (Single Hue)

### Recipe M-01: Blue Monochrome
**Mood:** Professional, calm, focused
**Best for:** SaaS dashboards, productivity tools, documentation

```css
:root {
  --mono-bg:       oklch(98% 0.003 255);  /* #F8FAFF — page background */
  --mono-surface:  oklch(94% 0.04 255);   /* #E0ECFF — card background */
  --mono-accent:   oklch(82% 0.08 255);   /* #93C5FD — decorative, badges */
  --mono-primary:  oklch(48% 0.20 255);   /* #2563EB — buttons, links */
  --mono-hover:    oklch(40% 0.18 255);   /* #1D4ED8 — hover states */
  --mono-text:     oklch(18% 0.06 255);   /* #1E3A8A — primary text */
  --mono-muted:    oklch(50% 0.06 255);   /* #64748B — secondary text */
}
```
**Contrast:** --mono-text on --mono-bg: Lc 90. White on --mono-primary: Lc 76.

### Recipe M-02: Purple Monochrome
**Mood:** Creative, premium, innovative
**Best for:** AI products, design tools, premium tiers

```css
:root {
  --mono-bg:       oklch(98% 0.003 295);  /* #FAF8FF — page background */
  --mono-surface:  oklch(92% 0.04 295);   /* #EDE9FE — card background */
  --mono-accent:   oklch(78% 0.10 295);   /* #C4B5FD — decorative */
  --mono-primary:  oklch(48% 0.22 295);   /* #7C3AED — buttons, links */
  --mono-hover:    oklch(40% 0.20 295);   /* #6D28D9 — hover states */
  --mono-text:     oklch(15% 0.06 295);   /* #2E1065 — primary text */
  --mono-muted:    oklch(50% 0.06 295);   /* #6B6685 — secondary text */
}
```
**Contrast:** --mono-text on --mono-bg: Lc 94. White on --mono-primary: Lc 78.

### Recipe M-03: Green Monochrome
**Mood:** Growth, natural, health
**Best for:** Finance apps, health platforms, eco-brands

```css
:root {
  --mono-bg:       oklch(98% 0.004 155);  /* #F0FDF4 — page background */
  --mono-surface:  oklch(92% 0.04 155);   /* #DCFCE7 — card background */
  --mono-accent:   oklch(72% 0.10 155);   /* #86EFAC — decorative */
  --mono-primary:  oklch(48% 0.18 155);   /* #16A34A — buttons, links */
  --mono-hover:    oklch(40% 0.16 155);   /* #15803D — hover states */
  --mono-text:     oklch(16% 0.06 155);   /* #14532D — primary text */
  --mono-muted:    oklch(48% 0.05 155);   /* #5F7A6E — secondary text */
}
```
**Contrast:** --mono-text on --mono-bg: Lc 94. White on --mono-primary: Lc 72.

### Recipe M-04: Slate Monochrome
**Mood:** Sophisticated, minimal, content-first
**Best for:** Developer tools, reading apps, documentation

```css
:root {
  --mono-bg:       oklch(98% 0.003 240);  /* #F8FAFC — page background */
  --mono-surface:  oklch(94% 0.003 240);  /* #E2E8F0 — card background */
  --mono-accent:   oklch(80% 0.005 240);  /* #94A3B8 — decorative */
  --mono-primary:  oklch(30% 0.008 240);  /* #334155 — buttons */
  --mono-hover:    oklch(22% 0.006 240);  /* #1E293B — hover states */
  --mono-text:     oklch(14% 0.005 240);  /* #0F172A — primary text */
  --mono-muted:    oklch(50% 0.005 240);  /* #64748B — secondary text */
}
```
**Contrast:** --mono-text on --mono-bg: Lc 96. White on --mono-primary: Lc 84.

### Recipe M-05: Rose Monochrome
**Mood:** Warm, inviting, personal
**Best for:** Consumer social, dating, lifestyle

```css
:root {
  --mono-bg:       oklch(98% 0.004 355);  /* #FFF5F7 — page background */
  --mono-surface:  oklch(94% 0.04 355);   /* #FFE4E6 — card background */
  --mono-accent:   oklch(78% 0.10 355);   /* #FDA4AF — decorative */
  --mono-primary:  oklch(50% 0.20 355);   /* #E11D48 — buttons, links */
  --mono-hover:    oklch(42% 0.18 355);   /* #BE123C — hover states */
  --mono-text:     oklch(16% 0.06 355);   /* #4C0519 — primary text */
  --mono-muted:    oklch(52% 0.05 355);   /* #7B6B72 — secondary text */
}
```
**Contrast:** --mono-text on --mono-bg: Lc 94. White on --mono-primary: Lc 68.

---

## Category 2: Duotone (Two Complementary Colors)

### Recipe D-01: Blue + Orange
**Mood:** Dynamic, energetic, attention-grabbing
**Best for:** Marketing sites, CTAs, event platforms

```css
:root {
  --duo-bg:        oklch(99% 0.002 255);  /* #FAFBFF — background */
  --duo-surface:   oklch(100% 0 0);       /* #FFFFFF — cards */
  --duo-primary:   oklch(48% 0.20 255);   /* #2563EB — primary actions */
  --duo-accent:    oklch(65% 0.18 55);    /* #EA580C — accent CTA */
  --duo-text:      oklch(15% 0.005 265);  /* #111827 — body text */
  --duo-muted:     oklch(50% 0.005 265);  /* #6B7280 — secondary text */
  --duo-primary-subtle: oklch(94% 0.03 255); /* #EFF6FF — primary tint */
  --duo-accent-subtle:  oklch(94% 0.03 55);  /* #FFF7ED — accent tint */
}
```
**Contrast:** --duo-text on --duo-bg: Lc 96. White on --duo-primary: Lc 76. White on --duo-accent: Lc 52.

### Recipe D-02: Purple + Teal
**Mood:** Creative, balanced, modern
**Best for:** Creative tools, portfolio sites, agencies

```css
:root {
  --duo-bg:        oklch(99% 0.002 295);  /* #FAFAFF — background */
  --duo-surface:   oklch(100% 0 0);       /* #FFFFFF — cards */
  --duo-primary:   oklch(48% 0.20 295);   /* #7C3AED — primary */
  --duo-accent:    oklch(52% 0.14 195);   /* #0D9488 — accent */
  --duo-text:      oklch(15% 0.005 265);  /* #111827 — body text */
  --duo-muted:     oklch(50% 0.005 265);  /* #6B7280 — secondary text */
  --duo-primary-subtle: oklch(94% 0.03 295); /* #F5F3FF — primary tint */
  --duo-accent-subtle:  oklch(94% 0.03 195); /* #F0FDFA — accent tint */
}
```
**Contrast:** --duo-text on --duo-bg: Lc 96. White on --duo-primary: Lc 78.

### Recipe D-03: Navy + Gold
**Mood:** Premium, authoritative, trustworthy
**Best for:** Finance, law, luxury brands

```css
:root {
  --duo-bg:        oklch(98% 0.003 255);  /* #F8FAFC — background */
  --duo-surface:   oklch(100% 0 0);       /* #FFFFFF — cards */
  --duo-primary:   oklch(25% 0.10 255);   /* #1E3A5F — primary */
  --duo-accent:    oklch(70% 0.12 85);    /* #C8A951 — gold accent */
  --duo-text:      oklch(15% 0.01 255);   /* #0F172A — body text */
  --duo-muted:     oklch(50% 0.005 255);  /* #64748B — secondary text */
  --duo-primary-subtle: oklch(92% 0.03 255); /* #E2E8F0 — navy tint */
  --duo-accent-subtle:  oklch(94% 0.04 85);  /* #FEF9E7 — gold tint */
}
```
**Contrast:** White on --duo-primary: Lc 88. --duo-text on --duo-bg: Lc 96.

### Recipe D-04: Red + Black
**Mood:** Bold, powerful, high-contrast
**Best for:** Sports brands, news sites, bold statements

```css
:root {
  --duo-bg:        oklch(100% 0 0);       /* #FFFFFF — background */
  --duo-surface:   oklch(97% 0.002 265);  /* #F5F5F5 — cards */
  --duo-primary:   oklch(0% 0 0);         /* #000000 — primary */
  --duo-accent:    oklch(50% 0.22 25);    /* #DC2626 — red accent */
  --duo-text:      oklch(0% 0 0);         /* #000000 — body text */
  --duo-muted:     oklch(45% 0.003 265);  /* #666666 — secondary text */
  --duo-accent-subtle: oklch(94% 0.04 25);/* #FEE2E2 — red tint */
}
```
**Contrast:** --duo-text on --duo-bg: Lc 106. White on --duo-accent: Lc 68.

### Recipe D-05: Pink + Navy
**Mood:** Confident, modern, fashion-forward
**Best for:** Fashion brands, beauty, lifestyle editorial

```css
:root {
  --duo-bg:        oklch(99% 0.002 345);  /* #FFFAFC — background */
  --duo-surface:   oklch(100% 0 0);       /* #FFFFFF — cards */
  --duo-primary:   oklch(55% 0.20 345);   /* #DB2777 — pink primary */
  --duo-accent:    oklch(22% 0.06 255);   /* #1E293B — navy accent */
  --duo-text:      oklch(18% 0.005 255);  /* #1E293B — body text */
  --duo-muted:     oklch(50% 0.005 265);  /* #6B7280 — secondary text */
  --duo-primary-subtle: oklch(95% 0.03 345); /* #FDF2F8 — pink tint */
}
```
**Contrast:** --duo-text on --duo-bg: Lc 92. White on --duo-primary: Lc 62.

---

## Category 3: Neutral + Single Accent

### Recipe NSA-01: Gray + Blue Accent
**Mood:** Clean, professional, focused
**Best for:** Enterprise SaaS, admin panels, B2B products

```css
:root {
  --bg:        oklch(98% 0.002 265);  /* #F9FAFB — background */
  --surface:   oklch(100% 0 0);       /* #FFFFFF — cards */
  --subtle:    oklch(96% 0.002 265);  /* #F3F4F6 — subtle bg */
  --border:    oklch(88% 0.003 265);  /* #E5E7EB — borders */
  --text:      oklch(14% 0.005 265);  /* #111827 — primary text */
  --muted:     oklch(48% 0.004 265);  /* #6B7280 — secondary text */
  --accent:    oklch(50% 0.18 255);   /* #2563EB — the single accent */
  --accent-hover: oklch(42% 0.16 255);/* #1D4ED8 — accent hover */
}
```
**Contrast:** --text on --bg: Lc 96. White on --accent: Lc 72.

### Recipe NSA-02: Warm Gray + Teal Accent
**Mood:** Approachable, modern, fresh
**Best for:** Healthcare platforms, wellness apps, HR tools

```css
:root {
  --bg:        oklch(97% 0.005 75);   /* #FAF8F2 — warm background */
  --surface:   oklch(100% 0.002 75);  /* #FFFEFA — cards */
  --subtle:    oklch(94% 0.005 75);   /* #F0EDE5 — subtle bg */
  --border:    oklch(86% 0.005 75);   /* #DDD8CE — borders */
  --text:      oklch(18% 0.008 75);   /* #2C2A24 — primary text */
  --muted:     oklch(50% 0.005 75);   /* #78716C — secondary text */
  --accent:    oklch(50% 0.14 195);   /* #0D9488 — teal accent */
  --accent-hover: oklch(42% 0.12 195);/* #0F766E — accent hover */
}
```
**Contrast:** --text on --bg: Lc 92. White on --accent: Lc 66.

### Recipe NSA-03: Dark Gray + Green Accent
**Mood:** Developer, terminal, tech
**Best for:** Developer tools, CLI products, code editors

```css
:root {
  --bg:        oklch(10% 0.01 265);   /* #141414 — dark background */
  --surface:   oklch(14% 0.01 265);   /* #1E1E1E — cards */
  --subtle:    oklch(18% 0.01 265);   /* #282828 — subtle bg */
  --border:    oklch(22% 0.01 265);   /* #333333 — borders */
  --text:      oklch(90% 0.005 265);  /* #E0E0E0 — primary text */
  --muted:     oklch(58% 0.005 265);  /* #888888 — secondary text */
  --accent:    oklch(65% 0.18 155);   /* #34D399 — green accent */
  --accent-hover: oklch(72% 0.16 155);/* #6EE7B7 — accent hover */
}
```
**Contrast:** --text on --bg: Lc 88. --accent on --bg: Lc 62.

### Recipe NSA-04: Pure White + Red Accent
**Mood:** Bold, editorial, high-impact
**Best for:** News sites, media platforms, photography portfolios

```css
:root {
  --bg:        oklch(100% 0 0);       /* #FFFFFF — background */
  --surface:   oklch(97% 0.002 265);  /* #F5F5F5 — cards */
  --subtle:    oklch(95% 0.002 265);  /* #EBEBEB — subtle bg */
  --border:    oklch(88% 0.003 265);  /* #DDDDDD — borders */
  --text:      oklch(10% 0.003 265);  /* #1A1A1A — primary text */
  --muted:     oklch(48% 0.003 265);  /* #6B6B6B — secondary text */
  --accent:    oklch(52% 0.22 25);    /* #DC2626 — red accent */
  --accent-hover: oklch(44% 0.20 25); /* #B91C1C — accent hover */
}
```
**Contrast:** --text on --bg: Lc 98. White on --accent: Lc 68.

### Recipe NSA-05: Off-White + Purple Accent
**Mood:** Refined, creative, modern
**Best for:** AI products, creative SaaS, education platforms

```css
:root {
  --bg:        oklch(98% 0.003 295);  /* #FAFAFF — background */
  --surface:   oklch(100% 0 0);       /* #FFFFFF — cards */
  --subtle:    oklch(96% 0.003 295);  /* #F3F0FF — subtle bg */
  --border:    oklch(88% 0.004 295);  /* #E0DDF0 — borders */
  --text:      oklch(15% 0.01 295);   /* #1C1033 — primary text */
  --muted:     oklch(50% 0.006 295);  /* #6B6685 — secondary text */
  --accent:    oklch(48% 0.22 295);   /* #7C3AED — purple accent */
  --accent-hover: oklch(40% 0.20 295);/* #6D28D9 — accent hover */
}
```
**Contrast:** --text on --bg: Lc 94. White on --accent: Lc 78.

---

## Category 4: Neutral + Two Accents (Primary/Secondary)

### Recipe NTA-01: Gray + Blue Primary + Teal Secondary
**Mood:** Professional with depth
**Best for:** Multi-feature SaaS, project management, CRM

```css
:root {
  --bg:        oklch(98% 0.002 265);  /* #F9FAFB */
  --surface:   oklch(100% 0 0);       /* #FFFFFF */
  --border:    oklch(88% 0.003 265);  /* #E5E7EB */
  --text:      oklch(14% 0.005 265);  /* #111827 */
  --muted:     oklch(48% 0.004 265);  /* #6B7280 */
  --primary:   oklch(48% 0.20 255);   /* #2563EB — primary actions */
  --secondary: oklch(52% 0.14 195);   /* #0D9488 — secondary actions */
  --primary-subtle: oklch(94% 0.03 255); /* #EFF6FF */
  --secondary-subtle: oklch(94% 0.03 195); /* #F0FDFA */
}
```

### Recipe NTA-02: Warm Gray + Indigo Primary + Amber Secondary
**Mood:** Warm yet professional
**Best for:** Collaboration tools, team platforms, education

```css
:root {
  --bg:        oklch(97% 0.005 75);   /* #FAF8F2 */
  --surface:   oklch(100% 0.002 75);  /* #FFFEFA */
  --border:    oklch(86% 0.005 75);   /* #DDD8CE */
  --text:      oklch(18% 0.008 75);   /* #2C2A24 */
  --muted:     oklch(50% 0.005 75);   /* #78716C */
  --primary:   oklch(45% 0.20 270);   /* #4338CA — indigo actions */
  --secondary: oklch(65% 0.16 65);    /* #D97706 — amber actions */
  --primary-subtle: oklch(94% 0.03 270); /* #E0E7FF */
  --secondary-subtle: oklch(94% 0.04 65); /* #FEF3C7 */
}
```

### Recipe NTA-03: Dark + Cyan Primary + Pink Secondary
**Mood:** Modern, vibrant, consumer tech
**Best for:** Social apps, streaming, entertainment

```css
:root {
  --bg:        oklch(8% 0.01 265);    /* #0F0F0F */
  --surface:   oklch(12% 0.01 265);   /* #1A1A1A */
  --border:    oklch(20% 0.01 265);   /* #2E2E2E */
  --text:      oklch(92% 0.005 265);  /* #EDEDED */
  --muted:     oklch(55% 0.005 265);  /* #808080 */
  --primary:   oklch(68% 0.16 210);   /* #22D3EE — cyan */
  --secondary: oklch(62% 0.18 345);   /* #EC4899 — pink */
  --primary-subtle: oklch(16% 0.04 210); /* dark cyan tint */
  --secondary-subtle: oklch(16% 0.04 345); /* dark pink tint */
}
```

### Recipe NTA-04: Gray + Green Primary + Blue Secondary
**Mood:** Balanced, trustworthy, growth
**Best for:** Fintech, banking, investment platforms

```css
:root {
  --bg:        oklch(99% 0.002 265);  /* #F9FAFB */
  --surface:   oklch(100% 0 0);       /* #FFFFFF */
  --border:    oklch(88% 0.003 265);  /* #E5E7EB */
  --text:      oklch(14% 0.005 265);  /* #111827 */
  --muted:     oklch(48% 0.004 265);  /* #6B7280 */
  --primary:   oklch(48% 0.16 155);   /* #059669 — green */
  --secondary: oklch(50% 0.16 255);   /* #2563EB — blue */
  --primary-subtle: oklch(94% 0.03 155); /* #ECFDF5 */
  --secondary-subtle: oklch(94% 0.03 255); /* #EFF6FF */
}
```

### Recipe NTA-05: Warm + Rose Primary + Violet Secondary
**Mood:** Warm, expressive, premium consumer
**Best for:** Beauty, fashion, lifestyle commerce

```css
:root {
  --bg:        oklch(98% 0.005 355);  /* #FFF5F7 */
  --surface:   oklch(100% 0.002 355); /* #FFFFFF */
  --border:    oklch(88% 0.005 355);  /* #F0DDE4 */
  --text:      oklch(16% 0.008 355);  /* #2D1A24 */
  --muted:     oklch(52% 0.005 355);  /* #7B6B72 */
  --primary:   oklch(52% 0.20 355);   /* #E11D48 — rose */
  --secondary: oklch(50% 0.16 295);   /* #7C3AED — violet */
  --primary-subtle: oklch(94% 0.04 355); /* #FFF1F2 */
  --secondary-subtle: oklch(94% 0.03 295); /* #F5F3FF */
}
```

---

## Category 5: Warm Palettes

### Recipe W-01: Sunset Warm
**Mood:** Cozy, inviting, energetic

```css
:root {
  --warm-bg:      oklch(98% 0.005 50);   /* #FFF8F0 — warm white */
  --warm-surface: oklch(100% 0.003 50);  /* #FFFCF8 — cream */
  --warm-amber:   oklch(72% 0.16 65);    /* #F59E0B — highlight */
  --warm-orange:  oklch(62% 0.18 55);    /* #EA580C — primary */
  --warm-red:     oklch(52% 0.18 30);    /* #DC2626 — accent */
  --warm-text:    oklch(18% 0.01 55);    /* #3D2C1E — body */
  --warm-muted:   oklch(52% 0.006 55);   /* #8B7355 — secondary */
  --warm-border:  oklch(88% 0.006 55);   /* #E8DDD0 — borders */
}
```

### Recipe W-02: Terracotta Earth
**Mood:** Organic, grounded, artisanal

```css
:root {
  --earth-bg:      oklch(96% 0.005 65);  /* #F5EFE5 — sandstone */
  --earth-surface: oklch(98% 0.004 65);  /* #FAF6F0 — cream */
  --earth-terra:   oklch(50% 0.14 40);   /* #B45309 — terracotta */
  --earth-olive:   oklch(45% 0.08 120);  /* #5F6B4E — olive */
  --earth-sand:    oklch(82% 0.06 75);   /* #D4C5A5 — sand accent */
  --earth-text:    oklch(20% 0.008 60);  /* #3D3425 — body */
  --earth-muted:   oklch(50% 0.005 60);  /* #7A7062 — secondary */
  --earth-border:  oklch(85% 0.005 65);  /* #D4CFC5 — borders */
}
```

### Recipe W-03: Autumn Harvest
**Mood:** Rich, seasonal, comforting

```css
:root {
  --autumn-bg:      oklch(97% 0.005 55); /* #FAF2E8 — warm bg */
  --autumn-surface: oklch(100% 0.003 55);/* #FFFAF5 — cards */
  --autumn-rust:    oklch(48% 0.14 40);  /* #9A3412 — primary */
  --autumn-gold:    oklch(68% 0.12 80);  /* #B8960B — accent */
  --autumn-olive:   oklch(42% 0.08 115); /* #4D5B35 — secondary */
  --autumn-cream:   oklch(90% 0.06 75);  /* #E8D5B5 — decorative */
  --autumn-text:    oklch(18% 0.008 50); /* #3D2E1E — body */
  --autumn-muted:   oklch(50% 0.006 50); /* #7D6B55 — secondary */
}
```

### Recipe W-04: Coral Sunset
**Mood:** Playful, tropical, lifestyle

```css
:root {
  --coral-bg:      oklch(98% 0.004 30);  /* #FFF5F5 — blush bg */
  --coral-surface: oklch(100% 0 0);      /* #FFFFFF — cards */
  --coral-primary: oklch(62% 0.18 25);   /* #F87171 — coral */
  --coral-peach:   oklch(78% 0.10 40);   /* #FECACA — peach */
  --coral-amber:   oklch(72% 0.14 70);   /* #F59E0B — amber */
  --coral-text:    oklch(18% 0.01 30);   /* #2D1A1A — body */
  --coral-muted:   oklch(52% 0.005 30);  /* #7B6B6B — secondary */
  --coral-border:  oklch(90% 0.005 30);  /* #F0DDDD — borders */
}
```

### Recipe W-05: Golden Hour
**Mood:** Luxurious, warm, editorial

```css
:root {
  --gold-bg:      oklch(97% 0.006 80);   /* #FAF4E8 — parchment */
  --gold-surface: oklch(100% 0.003 80);  /* #FFFDF5 — cream */
  --gold-primary: oklch(55% 0.14 80);    /* #A16207 — deep gold */
  --gold-accent:  oklch(72% 0.12 85);    /* #C8A951 — bright gold */
  --gold-dark:    oklch(20% 0.06 80);    /* #3D3010 — near-black */
  --gold-text:    oklch(20% 0.008 80);   /* #3D3425 — body */
  --gold-muted:   oklch(52% 0.006 80);   /* #7A7055 — secondary */
  --gold-border:  oklch(86% 0.006 80);   /* #DDD2B8 — borders */
}
```

---

## Category 6: Cool Palettes

### Recipe C-01: Arctic Blue
**Mood:** Clean, precise, professional

```css
:root {
  --arctic-bg:      oklch(98% 0.004 240); /* #F0F5FA — cool white */
  --arctic-surface: oklch(100% 0 0);      /* #FFFFFF — cards */
  --arctic-sky:     oklch(65% 0.16 230);  /* #38BDF8 — sky blue */
  --arctic-navy:    oklch(30% 0.12 245);  /* #1E3A5F — deep blue */
  --arctic-ice:     oklch(88% 0.06 230);  /* #BAE6FD — ice accent */
  --arctic-text:    oklch(15% 0.01 240);  /* #0F172A — body */
  --arctic-muted:   oklch(50% 0.005 240); /* #64748B — secondary */
  --arctic-border:  oklch(88% 0.004 240); /* #CBD5E1 — borders */
}
```

### Recipe C-02: Ocean Deep
**Mood:** Immersive, calm, depth

```css
:root {
  --ocean-bg:      oklch(10% 0.02 240);  /* #0C1524 — deep ocean */
  --ocean-surface: oklch(14% 0.02 240);  /* #162032 — cards */
  --ocean-wave:    oklch(60% 0.16 220);  /* #38BDF8 — wave blue */
  --ocean-foam:    oklch(80% 0.08 210);  /* #A5F3FC — seafoam */
  --ocean-coral:   oklch(62% 0.14 195);  /* #2DD4BF — coral teal */
  --ocean-text:    oklch(90% 0.005 240); /* #E2E8F0 — body */
  --ocean-muted:   oklch(58% 0.005 240); /* #94A3B8 — secondary */
  --ocean-border:  oklch(22% 0.02 240);  /* #1E2D42 — borders */
}
```

### Recipe C-03: Frost Minimal
**Mood:** Icy, minimal, Scandinavian

```css
:root {
  --frost-bg:      oklch(97% 0.003 210); /* #F0F9FF — frost */
  --frost-surface: oklch(100% 0 0);      /* #FFFFFF — cards */
  --frost-teal:    oklch(52% 0.12 195);  /* #0F766E — primary */
  --frost-ice:     oklch(85% 0.05 210);  /* #CFFAFE — ice */
  --frost-steel:   oklch(60% 0.005 240); /* #94A3B8 — steel accent */
  --frost-text:    oklch(16% 0.005 210); /* #134E4A — body */
  --frost-muted:   oklch(50% 0.005 210); /* #5F7A7D — secondary */
  --frost-border:  oklch(88% 0.004 210); /* #CCE3E8 — borders */
}
```

### Recipe C-04: Twilight Purple
**Mood:** Mysterious, premium, night

```css
:root {
  --twi-bg:      oklch(8% 0.03 280);    /* #0A0618 — twilight */
  --twi-surface: oklch(12% 0.03 280);   /* #141028 — cards */
  --twi-violet:  oklch(55% 0.20 290);   /* #8B5CF6 — violet */
  --twi-indigo:  oklch(45% 0.18 270);   /* #4F46E5 — indigo */
  --twi-sky:     oklch(68% 0.14 240);   /* #7DD3FC — sky accent */
  --twi-text:    oklch(92% 0.005 280);  /* #EDE8F5 — body */
  --twi-muted:   oklch(55% 0.02 280);   /* #7A6B95 — secondary */
  --twi-border:  oklch(20% 0.03 280);   /* #211A38 — borders */
}
```

### Recipe C-05: Teal Calm
**Mood:** Serene, medical, trustworthy

```css
:root {
  --calm-bg:      oklch(98% 0.004 195); /* #F0FDFA — mint bg */
  --calm-surface: oklch(100% 0 0);      /* #FFFFFF — cards */
  --calm-teal:    oklch(48% 0.14 195);  /* #0D9488 — primary */
  --calm-light:   oklch(78% 0.08 195);  /* #99F6E4 — accent light */
  --calm-deep:    oklch(32% 0.10 195);  /* #115E59 — deep teal */
  --calm-text:    oklch(16% 0.01 195);  /* #134E4A — body */
  --calm-muted:   oklch(50% 0.005 195); /* #5F8A85 — secondary */
  --calm-border:  oklch(88% 0.005 195); /* #CCF2ED — borders */
}
```

---

## Category 7: Earth Tones

### Recipe E-01: Desert Sand
**Mood:** Warm, natural, minimal

```css
:root {
  --desert-bg:      oklch(95% 0.005 70); /* #F2EBE0 — sand */
  --desert-surface: oklch(98% 0.004 70); /* #FAF6F0 — light sand */
  --desert-brown:   oklch(40% 0.10 55);  /* #6D4C2E — earth brown */
  --desert-rust:    oklch(48% 0.12 45);  /* #9C4221 — rust */
  --desert-sage:    oklch(62% 0.06 140); /* #8AA886 — sage */
  --desert-text:    oklch(20% 0.008 55); /* #3C2A14 — body */
  --desert-muted:   oklch(52% 0.005 55); /* #7D6B55 — secondary */
}
```

### Recipe E-02: Forest Floor
**Mood:** Deep, organic, grounded

```css
:root {
  --forest-bg:      oklch(96% 0.005 110); /* #F0EEE5 — moss bg */
  --forest-surface: oklch(98% 0.004 110); /* #F8F6F0 — cards */
  --forest-green:   oklch(38% 0.10 140);  /* #3D5A30 — deep green */
  --forest-bark:    oklch(32% 0.08 55);   /* #5C4033 — bark brown */
  --forest-moss:    oklch(55% 0.08 130);  /* #6B8F60 — moss */
  --forest-text:    oklch(18% 0.008 100); /* #2D2B1E — body */
  --forest-muted:   oklch(50% 0.005 100); /* #7A7854 — secondary */
}
```

### Recipe E-03: Clay Studio
**Mood:** Artisanal, handmade, crafted

```css
:root {
  --clay-bg:      oklch(96% 0.006 60);   /* #F5EDE0 — clay bg */
  --clay-surface: oklch(98% 0.005 60);   /* #FAF5EC — cards */
  --clay-terra:   oklch(48% 0.14 35);    /* #A0522D — terracotta */
  --clay-sienna:  oklch(42% 0.10 45);    /* #8B4513 — burnt sienna */
  --clay-cream:   oklch(88% 0.06 70);    /* #E8D5B5 — cream accent */
  --clay-text:    oklch(18% 0.008 50);   /* #3D2E18 — body */
  --clay-muted:   oklch(52% 0.006 50);   /* #7D6B48 — secondary */
}
```

---

## Category 8: Neon / Vibrant (Dark Background)

### Recipe N-01: Cyberpunk Neon
**Mood:** Futuristic, intense, high-energy

```css
:root {
  --neon-bg:       oklch(4% 0.02 280);   /* #030310 — void */
  --neon-surface:  oklch(8% 0.02 280);   /* #0A0818 — cards */
  --neon-magenta:  oklch(60% 0.26 340);  /* #FF0088 — primary neon */
  --neon-cyan:     oklch(75% 0.18 210);  /* #00E5FF — secondary neon */
  --neon-yellow:   oklch(85% 0.20 95);   /* #FFE500 — highlight */
  --neon-text:     oklch(95% 0.005 280); /* #F0ECF5 — body */
  --neon-muted:    oklch(50% 0.02 280);  /* #6B5E80 — secondary */
  --neon-border:   oklch(16% 0.03 280);  /* #1A1530 — borders */
}
```

### Recipe N-02: Electric Gaming
**Mood:** Competitive, vivid, adrenaline

```css
:root {
  --elec-bg:       oklch(5% 0.01 265);   /* #060608 — black */
  --elec-surface:  oklch(10% 0.01 265);  /* #121214 — cards */
  --elec-green:    oklch(75% 0.24 150);  /* #00FF66 — primary */
  --elec-purple:   oklch(55% 0.24 300);  /* #9900FF — secondary */
  --elec-red:      oklch(58% 0.22 30);   /* #FF3344 — accent */
  --elec-text:     oklch(95% 0.003 265); /* #F2F2F2 — body */
  --elec-muted:    oklch(50% 0.005 265); /* #6E6E6E — secondary */
  --elec-border:   oklch(15% 0.01 265);  /* #1E1E20 — borders */
}
```

### Recipe N-03: Synthwave
**Mood:** Retro-future, 80s, nostalgia

```css
:root {
  --synth-bg:      oklch(6% 0.03 300);   /* #0C0518 — deep purple-black */
  --synth-surface: oklch(10% 0.04 300);  /* #160C28 — cards */
  --synth-pink:    oklch(60% 0.24 340);  /* #FF2288 — hot pink */
  --synth-blue:    oklch(55% 0.18 260);  /* #2266FF — electric blue */
  --synth-orange:  oklch(68% 0.20 55);   /* #FF6622 — warm accent */
  --synth-text:    oklch(92% 0.005 300); /* #E8E0F0 — body */
  --synth-muted:   oklch(55% 0.02 300);  /* #7A6890 — secondary */
  --synth-border:  oklch(18% 0.04 300);  /* #221540 — borders */
}
```

---

## Category 9: Pastel (Light, Desaturated)

### Recipe P-01: Cotton Candy
**Mood:** Soft, playful, light

```css
:root {
  --pastel-bg:      oklch(98% 0.003 340); /* #FEFAFC — whisper pink bg */
  --pastel-surface: oklch(100% 0 0);      /* #FFFFFF — cards */
  --pastel-pink:    oklch(82% 0.08 340);  /* #F9A8D4 — soft pink */
  --pastel-blue:    oklch(82% 0.08 250);  /* #93C5FD — soft blue */
  --pastel-mint:    oklch(82% 0.08 170);  /* #A7F3D0 — soft mint */
  --pastel-lilac:   oklch(82% 0.08 295);  /* #C4B5FD — soft lilac */
  --pastel-text:    oklch(20% 0.008 340); /* #2D1A24 — body */
  --pastel-muted:   oklch(55% 0.005 340); /* #8A7580 — secondary */
}
```

### Recipe P-02: Morning Fog
**Mood:** Calm, professional, gentle

```css
:root {
  --fog-bg:      oklch(97% 0.003 240);   /* #F0F5FA — fog bg */
  --fog-surface: oklch(100% 0 0);        /* #FFFFFF — cards */
  --fog-blue:    oklch(80% 0.06 240);    /* #BAD6F0 — mist blue */
  --fog-sage:    oklch(80% 0.06 155);    /* #B0D8C8 — sage green */
  --fog-warm:    oklch(85% 0.05 70);     /* #DDD0B8 — warm sand */
  --fog-primary: oklch(42% 0.10 240);    /* #3A5570 — deep blue */
  --fog-text:    oklch(18% 0.005 240);   /* #1A2535 — body */
  --fog-muted:   oklch(52% 0.005 240);   /* #6A7A8A — secondary */
}
```

### Recipe P-03: Pastel Rainbow
**Mood:** Playful, inclusive, celebration

```css
:root {
  --rainbow-bg:     oklch(99% 0.002 265); /* #FAFAFA — bg */
  --rainbow-surface:oklch(100% 0 0);      /* #FFFFFF — cards */
  --rainbow-red:    oklch(82% 0.08 25);   /* #FCA5A5 — soft red */
  --rainbow-orange: oklch(85% 0.08 55);   /* #FDBA74 — soft orange */
  --rainbow-yellow: oklch(88% 0.08 90);   /* #FDE68A — soft yellow */
  --rainbow-green:  oklch(82% 0.08 155);  /* #86EFAC — soft green */
  --rainbow-blue:   oklch(82% 0.08 250);  /* #93C5FD — soft blue */
  --rainbow-purple: oklch(80% 0.08 295);  /* #C4B5FD — soft purple */
  --rainbow-text:   oklch(18% 0.005 265); /* #1F1F1F — body */
  --rainbow-muted:  oklch(55% 0.004 265); /* #737373 — secondary */
}
```

---

## Category 10: Jewel Tones (Deep, Rich)

### Recipe J-01: Royal Jewels
**Mood:** Luxurious, opulent, premium

```css
:root {
  --jewel-bg:       oklch(8% 0.02 270);  /* #0A0818 — velvet black */
  --jewel-surface:  oklch(12% 0.02 270); /* #141025 — cards */
  --jewel-ruby:     oklch(42% 0.18 25);  /* #9B1B30 — ruby */
  --jewel-sapphire: oklch(38% 0.18 260); /* #1E3A8A — sapphire */
  --jewel-emerald:  oklch(40% 0.16 155); /* #065F46 — emerald */
  --jewel-amethyst: oklch(42% 0.18 295); /* #5B21B6 — amethyst */
  --jewel-gold:     oklch(70% 0.14 85);  /* #CA8A04 — gold */
  --jewel-text:     oklch(90% 0.005 270);/* #E0DCF0 — body */
  --jewel-muted:    oklch(55% 0.02 270); /* #7A7095 — secondary */
}
```

### Recipe J-02: Emerald Night
**Mood:** Sophisticated, nature-luxury

```css
:root {
  --emerald-bg:      oklch(6% 0.03 155); /* #041510 — deep forest */
  --emerald-surface: oklch(10% 0.03 155);/* #0A2218 — cards */
  --emerald-bright:  oklch(52% 0.18 155);/* #059669 — bright emerald */
  --emerald-light:   oklch(68% 0.14 155);/* #34D399 — light emerald */
  --emerald-gold:    oklch(70% 0.12 85); /* #C8A951 — gold accent */
  --emerald-text:    oklch(90% 0.005 155);/* #D8E8E0 — body */
  --emerald-muted:   oklch(55% 0.02 155);/* #6A8A7A — secondary */
  --emerald-border:  oklch(16% 0.03 155);/* #143024 — borders */
}
```

### Recipe J-03: Sapphire Depth
**Mood:** Deep, authoritative, premium tech

```css
:root {
  --sapph-bg:      oklch(6% 0.03 255);   /* #040A1A — midnight */
  --sapph-surface: oklch(10% 0.03 255);  /* #0C1628 — cards */
  --sapph-bright:  oklch(55% 0.20 255);  /* #3B82F6 — bright sapphire */
  --sapph-light:   oklch(68% 0.14 255);  /* #60A5FA — light sapphire */
  --sapph-silver:  oklch(80% 0.005 255); /* #B0B8C8 — silver accent */
  --sapph-text:    oklch(90% 0.005 255); /* #D8E0F0 — body */
  --sapph-muted:   oklch(55% 0.01 255);  /* #6A7A95 — secondary */
  --sapph-border:  oklch(16% 0.03 255);  /* #142040 — borders */
}
```

---

## Category 11: Split-Complementary

### Recipe SC-01: Blue + Yellow-Orange + Red-Orange
**Mood:** Dynamic but balanced, editorial

```css
:root {
  --sc-bg:       oklch(99% 0.002 255);  /* #FAFBFF */
  --sc-surface:  oklch(100% 0 0);       /* #FFFFFF */
  --sc-primary:  oklch(48% 0.20 255);   /* #2563EB — blue */
  --sc-accent1:  oklch(68% 0.16 55);    /* #F59E0B — yellow-orange */
  --sc-accent2:  oklch(55% 0.16 15);    /* #F43F5E — red-orange */
  --sc-text:     oklch(14% 0.005 265);  /* #111827 */
  --sc-muted:    oklch(48% 0.004 265);  /* #6B7280 */
}
```

### Recipe SC-02: Purple + Yellow-Green + Teal
**Mood:** Creative, balanced, nature-tech fusion

```css
:root {
  --sc-bg:       oklch(98% 0.003 295);  /* #FAF8FF */
  --sc-surface:  oklch(100% 0 0);       /* #FFFFFF */
  --sc-primary:  oklch(48% 0.20 295);   /* #7C3AED — purple */
  --sc-accent1:  oklch(62% 0.14 135);   /* #65A30D — yellow-green */
  --sc-accent2:  oklch(55% 0.14 195);   /* #0D9488 — teal */
  --sc-text:     oklch(15% 0.01 295);   /* #1C1033 */
  --sc-muted:    oklch(50% 0.005 295);  /* #6B6685 */
}
```

---

## Category 12: Gradient-Based

### Recipe G-01: Purple-to-Pink Gradient
**Mood:** Modern, social, vibrant

```css
:root {
  --grad-start:   oklch(48% 0.22 295);  /* #7C3AED — purple */
  --grad-end:     oklch(58% 0.20 345);  /* #EC4899 — pink */
  --grad-css:     linear-gradient(135deg, var(--grad-start), var(--grad-end));
  --grad-bg:      oklch(99% 0.002 310); /* #FAFAFF — bg */
  --grad-surface: oklch(100% 0 0);      /* #FFFFFF — cards */
  --grad-text:    oklch(14% 0.005 265); /* #111827 */
  --grad-muted:   oklch(48% 0.004 265); /* #6B7280 */
  --grad-on-gradient: oklch(100% 0 0);  /* White text on gradient */
}
```

### Recipe G-02: Blue-to-Teal Gradient
**Mood:** Tech, fresh, professional

```css
:root {
  --grad-start:   oklch(48% 0.20 255);  /* #2563EB — blue */
  --grad-end:     oklch(55% 0.16 195);  /* #14B8A6 — teal */
  --grad-css:     linear-gradient(135deg, var(--grad-start), var(--grad-end));
  --grad-bg:      oklch(99% 0.002 240); /* #FAFBFE — bg */
  --grad-surface: oklch(100% 0 0);      /* #FFFFFF — cards */
  --grad-text:    oklch(14% 0.005 240); /* #0F172A */
  --grad-muted:   oklch(48% 0.005 240); /* #64748B */
  --grad-on-gradient: oklch(100% 0 0);  /* White text on gradient */
}
```

### Recipe G-03: Sunset Gradient
**Mood:** Warm, emotional, marketing

```css
:root {
  --grad-start:   oklch(58% 0.22 25);   /* #F43F5E — rose */
  --grad-mid:     oklch(65% 0.20 55);   /* #FB923C — orange */
  --grad-end:     oklch(78% 0.16 85);   /* #FBBF24 — amber */
  --grad-css:     linear-gradient(135deg, var(--grad-start), var(--grad-mid), var(--grad-end));
  --grad-bg:      oklch(99% 0.003 40);  /* #FFFAF5 — bg */
  --grad-surface: oklch(100% 0 0);      /* #FFFFFF — cards */
  --grad-text:    oklch(16% 0.01 40);   /* #1C1108 */
  --grad-muted:   oklch(48% 0.005 40);  /* #7D6B55 */
  --grad-on-gradient: oklch(100% 0 0);  /* White text on gradient */
}
```

### Recipe G-04: Dark Gradient (Header)
**Mood:** Premium, immersive, hero section

```css
:root {
  --grad-start:   oklch(8% 0.03 280);   /* #0A0618 — deep purple */
  --grad-end:     oklch(12% 0.02 240);  /* #0C1628 — deep navy */
  --grad-css:     linear-gradient(180deg, var(--grad-start), var(--grad-end));
  --grad-accent1: oklch(60% 0.22 295);  /* #8B5CF6 — purple accent */
  --grad-accent2: oklch(65% 0.18 230);  /* #38BDF8 — sky accent */
  --grad-text:    oklch(95% 0.003 265); /* #F5F5F5 — body */
  --grad-muted:   oklch(65% 0.01 270);  /* #9090A0 — secondary */
}
```

---

## Usage Guide: How to Choose a Recipe

### By Mood
| Desired Mood | Recommended Categories | Top Picks |
|-------------|----------------------|-----------|
| Professional | Monochromatic, NSA, Cool | M-01, M-04, NSA-01, C-01 |
| Playful | Pastel, Warm, Duotone | P-01, P-03, W-04, D-01 |
| Premium | Jewel, Duotone, Gradient | J-01, D-03, G-04, NSA-04 |
| Minimal | Monochromatic, NSA | M-04, NSA-01, NSA-02 |
| Energetic | Neon, Warm, Duotone | N-01, N-02, W-01, D-04 |
| Calm | Cool, Pastel, Earth | C-05, P-02, E-01, C-03 |
| Bold | Neon, Duotone, Gradient | N-01, D-04, G-01, N-03 |
| Natural | Earth, Warm, Cool | E-01, E-02, E-03, W-02 |

### By Industry
| Industry | Recommended Recipes |
|----------|-------------------|
| Fintech | M-01, D-03, NSA-01, NTA-04, C-01 |
| Healthcare | C-05, P-02, NSA-02, M-03 |
| SaaS/B2B | M-01, M-04, NSA-01, NTA-01 |
| E-commerce | W-01, W-04, D-01, NSA-04 |
| Social | G-01, P-01, NTA-03, D-05 |
| Education | P-03, NTA-02, NSA-05, M-02 |
| Gaming | N-01, N-02, J-01, N-03 |
| Creative | M-02, D-02, G-01, J-03 |
| Food/Lifestyle | W-01, W-02, E-01, E-03, W-04 |
| Enterprise | NSA-01, M-04, NTA-01, C-01 |

### By Dark Mode Strategy
| Strategy | Recipes |
|----------|---------|
| Already dark | N-01, N-02, N-03, J-01, J-02, J-03, C-02, C-04, NSA-03, G-04 |
| Easy to invert | M-01 through M-05 (monochromatic inverts cleanly) |
| Needs custom dark | D-01 through D-05, NTA-01 through NTA-05, W-01 through W-05 |
| Use as-is (both modes) | NSA-03 (already dark), NSA-01 (swap gray scale) |
