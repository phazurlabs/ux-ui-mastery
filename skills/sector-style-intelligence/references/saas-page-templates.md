# SaaS Page Templates — Complete Implementation Guide

## Overview

This reference provides complete page-level templates for 10 essential SaaS pages. Each template includes the exact block sequence, typography choices, color application, spacing rhythm, component selection, responsive behavior, and a React/TSX page skeleton. Every page is provided in three style variants: Minimal (Linear/Vercel), Warm (Notion/Figma), and Bold (Stripe/Loom).

These templates complement the style tokens in `saas-productivity-style.md` by translating abstract style direction into concrete page-level blueprints.

---

## Template Structure Convention

Every template follows this anatomy:
1. **Block Sequence** — Ordered list of page sections from top to bottom
2. **Typography Map** — Font family, weight, size, line-height per element
3. **Color Application** — Background, text, accent, border per section
4. **Spacing Rhythm** — Vertical gaps between blocks, internal padding
5. **Component Selection** — Exact components used per block
6. **Responsive Behavior** — Breakpoint adaptations (mobile, tablet, desktop)
7. **React/TSX Skeleton** — Implementation-ready page component

---

## 1. SaaS Marketing Landing Page

### Block Sequence (all variants)
1. Navigation bar (logo + links + CTA)
2. Hero section (headline + subheadline + CTA buttons + hero visual)
3. Social proof bar (logos or metrics)
4. Feature grid (3-6 features with icons)
5. Product showcase (screenshot/video with supporting copy)
6. Testimonial section (quotes with avatars)
7. Pricing preview (3 tiers with CTA)
8. Integration logos strip
9. Final CTA section
10. Footer (links + legal)

### Variant A: Minimal (Linear/Vercel Style)

**Typography Map**
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Nav links | Inter | 400 | 14px | 20px |
| Hero headline | Inter | 600 | 56px | 64px |
| Hero subheadline | Inter | 400 | 18px | 28px |
| Section heading | Inter | 600 | 36px | 44px |
| Body text | Inter | 400 | 16px | 26px |
| Button text | Inter | 500 | 14px | 20px |
| Caption/meta | Inter | 400 | 13px | 18px |

**Color Application**
```
Page background:        #000000
Nav background:         #000000 + backdrop-blur(12px) border-bottom: 1px solid #1a1a1a
Hero background:        #000000 with radial gradient spotlight
Section backgrounds:    Alternate #000000 / #0A0A0A
Card backgrounds:       #111111 border: 1px solid #222222
Text primary:           #EDEDED
Text secondary:         #888888
CTA primary:            #FFFFFF bg, #000000 text
CTA secondary:          transparent, #EDEDED text, 1px solid #333
Accent:                 #0070F3 (links, hover states)
```

**Spacing Rhythm**
```
Section vertical padding:   120px desktop / 80px tablet / 60px mobile
Between blocks:             80px
Card grid gap:              24px
Internal card padding:      32px
Nav height:                 64px
Container max-width:        1200px
Container padding:          0 24px
```

**Component Selection**
- Nav: Sticky, transparent-to-blur on scroll, command palette shortcut badge
- Hero: Text-only or with subtle gradient mesh, no illustration
- Social proof: Monochrome logos at 40% opacity, grayscale filter
- Features: Icon + heading + description in 3-column grid, icons are 20px stroke
- Testimonials: Single quote with monochrome avatar, minimal card
- CTA: Ghost buttons with subtle hover glow

**Responsive Behavior**
- Desktop (1200px+): Full grid layouts, large typography
- Tablet (768-1199px): 2-column grids, reduce hero headline to 40px
- Mobile (<768px): Single column, hero headline 32px, stack CTAs vertically, hamburger nav

**React/TSX Skeleton**
```tsx
import { useState } from 'react';

export function SaaSLandingMinimal() {
  const [mobileNav, setMobileNav] = useState(false);

  return (
    <div className="min-h-screen bg-black text-gray-200">
      {/* Navigation */}
      <nav className="sticky top-0 z-50 border-b border-white/10 bg-black/80 backdrop-blur-xl">
        <div className="mx-auto flex h-16 max-w-[1200px] items-center justify-between px-6">
          <a href="/" className="text-sm font-semibold text-white">ProductName</a>
          <div className="hidden items-center gap-8 md:flex">
            <a href="#features" className="text-sm text-gray-400 hover:text-white transition-colors">Features</a>
            <a href="#pricing" className="text-sm text-gray-400 hover:text-white transition-colors">Pricing</a>
            <a href="#docs" className="text-sm text-gray-400 hover:text-white transition-colors">Docs</a>
            <a href="/login" className="text-sm text-gray-400 hover:text-white transition-colors">Log in</a>
            <a href="/signup" className="rounded-md bg-white px-4 py-2 text-sm font-medium text-black hover:bg-gray-200 transition-colors">
              Get Started
            </a>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="relative overflow-hidden py-[120px] md:py-[160px]">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_rgba(255,255,255,0.05)_0%,transparent_70%)]" />
        <div className="relative mx-auto max-w-[1200px] px-6 text-center">
          <h1 className="mx-auto max-w-3xl text-4xl font-semibold leading-tight text-white md:text-[56px] md:leading-[64px]">
            Build faster with fewer distractions
          </h1>
          <p className="mx-auto mt-6 max-w-xl text-lg leading-7 text-gray-400">
            The project management tool designed for speed. Keyboard-first, real-time, minimal.
          </p>
          <div className="mt-10 flex items-center justify-center gap-4">
            <a href="/signup" className="rounded-md bg-white px-6 py-3 text-sm font-medium text-black hover:bg-gray-200 transition-colors">
              Start for free
            </a>
            <a href="/demo" className="rounded-md border border-gray-700 px-6 py-3 text-sm font-medium text-gray-300 hover:border-gray-500 hover:text-white transition-colors">
              Live demo
            </a>
          </div>
        </div>
      </section>

      {/* Social Proof */}
      <section className="border-y border-white/5 py-12">
        <div className="mx-auto max-w-[1200px] px-6">
          <p className="text-center text-xs uppercase tracking-widest text-gray-600">Trusted by teams at</p>
          <div className="mt-8 flex items-center justify-center gap-12 opacity-40 grayscale">
            {['Company A', 'Company B', 'Company C', 'Company D', 'Company E'].map((co) => (
              <span key={co} className="text-sm text-gray-500">{co}</span>
            ))}
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section id="features" className="py-[120px]">
        <div className="mx-auto max-w-[1200px] px-6">
          <h2 className="text-center text-3xl font-semibold text-white md:text-4xl">
            Everything you need, nothing you don't
          </h2>
          <div className="mt-16 grid gap-6 md:grid-cols-3">
            {[1, 2, 3, 4, 5, 6].map((i) => (
              <div key={i} className="rounded-lg border border-white/10 bg-[#111] p-8">
                <div className="mb-4 h-10 w-10 rounded-md bg-white/5 flex items-center justify-center">
                  <span className="text-gray-400">icon</span>
                </div>
                <h3 className="text-lg font-semibold text-white">Feature {i}</h3>
                <p className="mt-2 text-sm leading-relaxed text-gray-400">
                  Short description of how this feature solves a real pain point.
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing Preview */}
      <section id="pricing" className="bg-[#0A0A0A] py-[120px]">
        <div className="mx-auto max-w-[1200px] px-6 text-center">
          <h2 className="text-3xl font-semibold text-white md:text-4xl">Simple pricing</h2>
          <p className="mt-4 text-gray-400">No surprises. Cancel anytime.</p>
          <div className="mt-16 grid gap-6 md:grid-cols-3">
            {['Free', 'Pro', 'Enterprise'].map((tier) => (
              <div key={tier} className="rounded-lg border border-white/10 bg-[#111] p-8 text-left">
                <h3 className="text-lg font-semibold text-white">{tier}</h3>
                <p className="mt-1 text-sm text-gray-500">
                  For {tier === 'Free' ? 'individuals' : tier === 'Pro' ? 'growing teams' : 'organizations'}
                </p>
                <p className="mt-6 text-4xl font-semibold text-white">
                  {tier === 'Free' ? '$0' : tier === 'Pro' ? '$12' : 'Custom'}
                </p>
                <p className="mt-1 text-sm text-gray-500">
                  {tier !== 'Enterprise' ? '/user/month' : 'Contact sales'}
                </p>
                <button className={`mt-8 w-full rounded-md py-2.5 text-sm font-medium transition-colors ${
                  tier === 'Pro'
                    ? 'bg-white text-black hover:bg-gray-200'
                    : 'border border-gray-700 text-gray-300 hover:border-gray-500'
                }`}>
                  {tier === 'Enterprise' ? 'Contact sales' : 'Get started'}
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/5 py-12">
        <div className="mx-auto max-w-[1200px] px-6 flex flex-col md:flex-row items-center justify-between gap-4">
          <span className="text-sm text-gray-600">2026 ProductName. All rights reserved.</span>
          <div className="flex gap-6">
            <a href="/privacy" className="text-sm text-gray-600 hover:text-gray-400">Privacy</a>
            <a href="/terms" className="text-sm text-gray-600 hover:text-gray-400">Terms</a>
          </div>
        </div>
      </footer>
    </div>
  );
}
```

### Variant B: Warm (Notion/Figma Style)

**Typography Map**
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Nav links | Inter | 400 | 14px | 20px |
| Hero headline | Georgia or serif fallback | 700 | 52px | 62px |
| Hero subheadline | Inter | 400 | 18px | 28px |
| Section heading | Georgia or serif fallback | 700 | 36px | 44px |
| Body text | Inter | 400 | 16px | 26px |
| Button text | Inter | 500 | 14px | 20px |

**Color Application**
```
Page background:        #FFFFFF
Nav background:         #FFFFFF border-bottom: 1px solid #E8E5E0
Hero background:        #FFFCF7 (warm off-white)
Alternate sections:     #F7F5F0
Card backgrounds:       #FFFFFF with subtle shadow
Text primary:           #37352F
Text secondary:         #787774
CTA primary:            #2F80ED bg, #FFFFFF text
CTA secondary:          #FFFFFF bg, #37352F text, 1px solid #E3E2DE
Accent:                 #2F80ED (Notion-style blue)
Highlight:              #FDEBCF (warm highlight)
```

**Spacing Rhythm**
```
Section vertical padding:   100px desktop / 72px tablet / 56px mobile
Between blocks:             64px
Card grid gap:              20px
Internal card padding:      28px
Nav height:                 56px
Container max-width:        1080px
```

**Component Selection**
- Nav: Clean horizontal with dropdown menus, rounded avatar, warm hover states
- Hero: Left-aligned text with illustration or product screenshot on right
- Social proof: Color logos, customer count metric
- Features: Icon + text in 2-column layout with generous descriptions
- Testimonials: Card-based carousel with colored borders
- CTA: Rounded corners (8px), filled primary, outlined secondary

**Responsive Behavior**
- Desktop: 2-column hero, 3-column features
- Tablet: Stacked hero, 2-column features
- Mobile: Single column throughout, hero illustration below text

**React/TSX Skeleton**
```tsx
export function SaaSLandingWarm() {
  return (
    <div className="min-h-screen bg-white text-[#37352F]">
      <nav className="sticky top-0 z-50 border-b border-[#E8E5E0] bg-white">
        <div className="mx-auto flex h-14 max-w-[1080px] items-center justify-between px-6">
          <a href="/" className="text-base font-semibold">ProductName</a>
          <div className="hidden items-center gap-6 md:flex">
            <a href="#" className="text-sm text-[#787774] hover:text-[#37352F]">Product</a>
            <a href="#" className="text-sm text-[#787774] hover:text-[#37352F]">Solutions</a>
            <a href="#" className="text-sm text-[#787774] hover:text-[#37352F]">Pricing</a>
            <a href="/login" className="text-sm text-[#787774] hover:text-[#37352F]">Log in</a>
            <a href="/signup" className="rounded-lg bg-[#2F80ED] px-4 py-2 text-sm font-medium text-white hover:bg-[#2672D4]">
              Get started free
            </a>
          </div>
        </div>
      </nav>

      <section className="bg-[#FFFCF7] py-24 md:py-32">
        <div className="mx-auto max-w-[1080px] px-6 md:flex md:items-center md:gap-16">
          <div className="md:w-1/2">
            <h1 className="font-serif text-4xl font-bold leading-tight md:text-[52px] md:leading-[62px]">
              Your workspace, beautifully organized
            </h1>
            <p className="mt-6 text-lg leading-7 text-[#787774]">
              Write, plan, and get organized in one tool that adapts to the way your team works.
            </p>
            <div className="mt-8 flex gap-3">
              <a href="/signup" className="rounded-lg bg-[#2F80ED] px-6 py-3 text-sm font-medium text-white">
                Get started free
              </a>
              <a href="/demo" className="rounded-lg border border-[#E3E2DE] px-6 py-3 text-sm font-medium">
                Request a demo
              </a>
            </div>
          </div>
          <div className="mt-12 md:mt-0 md:w-1/2">
            <div className="aspect-[4/3] rounded-xl bg-[#F0EDE6] shadow-lg" />
          </div>
        </div>
      </section>

      <section className="py-24">
        <div className="mx-auto max-w-[1080px] px-6">
          <h2 className="text-center font-serif text-3xl font-bold">Built for your whole team</h2>
          <div className="mt-16 grid gap-5 md:grid-cols-3">
            {[1, 2, 3].map((i) => (
              <div key={i} className="rounded-xl bg-white p-7 shadow-sm ring-1 ring-[#E8E5E0]">
                <div className="mb-4 flex h-10 w-10 items-center justify-center rounded-lg bg-[#FDEBCF]">
                  <span className="text-lg">icon</span>
                </div>
                <h3 className="text-lg font-semibold">Feature {i}</h3>
                <p className="mt-2 text-sm leading-relaxed text-[#787774]">
                  Descriptive text about how this feature helps teams work better together.
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <footer className="border-t border-[#E8E5E0] py-10">
        <div className="mx-auto max-w-[1080px] px-6 text-center text-sm text-[#787774]">
          2026 ProductName
        </div>
      </footer>
    </div>
  );
}
```

### Variant C: Bold (Stripe/Loom Style)

**Typography Map**
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Nav links | Inter or system | 500 | 15px | 22px |
| Hero headline | Inter | 700 | 64px | 72px |
| Hero subheadline | Inter | 400 | 20px | 32px |
| Section heading | Inter | 700 | 44px | 52px |
| Body text | Inter | 400 | 17px | 28px |
| Button text | Inter | 600 | 15px | 22px |

**Color Application**
```
Page background:        #0A2540 (Stripe dark blue) or gradient
Hero background:        Linear gradient from #0A2540 to #1B1B50
Section backgrounds:    #FFFFFF (alternating light sections)
Card backgrounds:       #FFFFFF with colored left border or gradient overlay
Text on dark:           #FFFFFF
Text on light:          #0A2540
Text secondary light:   #425466
CTA primary:            #635BFF bg (Stripe purple), #FFFFFF text
CTA secondary:          #FFFFFF bg, #0A2540 text
Accent gradient:        Linear gradient(135deg, #80E9FF, #635BFF, #FF80B5)
```

**Spacing Rhythm**
```
Section vertical padding:   140px desktop / 96px tablet / 72px mobile
Between blocks:             96px
Card grid gap:              32px
Internal card padding:      40px
Nav height:                 72px
Container max-width:        1280px
```

**Component Selection**
- Nav: Tall nav with mega-menu dropdowns, bold CTAs
- Hero: Large gradient background, animated mesh/globe visual, oversized headline
- Social proof: Metric counters with bold numbers
- Features: Large cards with gradient borders, product screenshots
- Testimonials: Full-width quote with large avatar and company logo
- CTA: Pill-shaped buttons with hover elevation, gradient accents

**React/TSX Skeleton**
```tsx
export function SaaSLandingBold() {
  return (
    <div className="min-h-screen">
      <nav className="sticky top-0 z-50 bg-[#0A2540]/95 backdrop-blur-xl">
        <div className="mx-auto flex h-[72px] max-w-[1280px] items-center justify-between px-8">
          <a href="/" className="text-lg font-bold text-white">ProductName</a>
          <div className="hidden items-center gap-8 lg:flex">
            <a href="#" className="text-[15px] font-medium text-white/80 hover:text-white">Products</a>
            <a href="#" className="text-[15px] font-medium text-white/80 hover:text-white">Solutions</a>
            <a href="#" className="text-[15px] font-medium text-white/80 hover:text-white">Developers</a>
            <a href="#" className="text-[15px] font-medium text-white/80 hover:text-white">Pricing</a>
            <a href="/login" className="text-[15px] font-medium text-white/80 hover:text-white">Sign in</a>
            <a href="/signup" className="rounded-full bg-[#635BFF] px-5 py-2.5 text-[15px] font-semibold text-white hover:bg-[#7A73FF] transition-colors">
              Start now
            </a>
          </div>
        </div>
      </nav>

      <section className="relative overflow-hidden bg-gradient-to-br from-[#0A2540] via-[#1B1B50] to-[#0A2540] py-32 md:py-44">
        <div className="relative mx-auto max-w-[1280px] px-8">
          <h1 className="max-w-4xl text-5xl font-bold leading-tight text-white md:text-[64px] md:leading-[72px]">
            Financial infrastructure for the internet
          </h1>
          <p className="mt-8 max-w-xl text-xl leading-8 text-white/70">
            Millions of companies use our platform to accept payments, grow revenue, and accelerate new business opportunities.
          </p>
          <div className="mt-12 flex gap-4">
            <a href="/signup" className="rounded-full bg-[#635BFF] px-8 py-4 text-[15px] font-semibold text-white shadow-lg shadow-[#635BFF]/30 hover:bg-[#7A73FF]">
              Start now
            </a>
            <a href="/contact" className="rounded-full bg-white/10 px-8 py-4 text-[15px] font-semibold text-white backdrop-blur-sm hover:bg-white/20">
              Contact sales
            </a>
          </div>
        </div>
      </section>

      <section className="bg-white py-32">
        <div className="mx-auto max-w-[1280px] px-8">
          <h2 className="text-center text-4xl font-bold text-[#0A2540] md:text-[44px]">
            A fully integrated suite of products
          </h2>
          <div className="mt-20 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
            {[1, 2, 3, 4, 5, 6].map((i) => (
              <div key={i} className="group rounded-2xl bg-gradient-to-br from-[#F6F9FC] to-white p-10 transition-shadow hover:shadow-xl">
                <div className="mb-5 flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-[#80E9FF] to-[#635BFF]">
                  <span className="text-xl text-white">icon</span>
                </div>
                <h3 className="text-xl font-bold text-[#0A2540]">Product {i}</h3>
                <p className="mt-3 text-[15px] leading-relaxed text-[#425466]">
                  Description of the product capability and its primary value proposition.
                </p>
                <a href="#" className="mt-4 inline-flex items-center gap-1 text-sm font-semibold text-[#635BFF]">
                  Learn more
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>

      <footer className="bg-[#0A2540] py-16">
        <div className="mx-auto max-w-[1280px] px-8 text-sm text-white/50">
          2026 ProductName. All rights reserved.
        </div>
      </footer>
    </div>
  );
}
```

---

## 2. SaaS Pricing Page

### Block Sequence
1. Navigation bar
2. Page header (headline + plan toggle monthly/annual)
3. Pricing tier cards (3-4 columns)
4. Feature comparison table (expandable)
5. FAQ accordion
6. Enterprise CTA banner
7. Footer

### Variant A: Minimal (Linear/Vercel Style)

**Typography Map**
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Page headline | Inter | 600 | 40px | 48px |
| Tier name | Inter | 600 | 18px | 24px |
| Price | Inter | 700 | 48px | 56px |
| Price period | Inter | 400 | 14px | 20px |
| Feature list | Inter | 400 | 14px | 28px |
| Comparison header | Inter | 500 | 13px | 18px |
| FAQ question | Inter | 500 | 15px | 22px |
| FAQ answer | Inter | 400 | 14px | 24px |

**Color Application**
```
Background:             #000000
Card background:        #111111 border: 1px solid #222
Highlighted tier:       #111111 border: 1px solid #0070F3
Toggle background:      #222222
Toggle active:          #FFFFFF bg, #000000 text
Comparison table:       #0A0A0A, rows border-b #1A1A1A
Check icon:             #0070F3
Cross icon:             #333333
FAQ border:             #1A1A1A
```

**Spacing Rhythm**
```
Header padding:         80px top, 48px bottom
Tier card gap:          16px
Tier card padding:      32px
Feature item gap:       12px
Comparison row height:  48px
FAQ item padding:       20px vertical
```

**React/TSX Skeleton**
```tsx
import { useState } from 'react';

export function PricingMinimal() {
  const [annual, setAnnual] = useState(true);

  const tiers = [
    { name: 'Free', price: { monthly: 0, annual: 0 }, desc: 'For individuals', features: ['5 projects', '1 user', 'Basic analytics'], cta: 'Get started', highlighted: false },
    { name: 'Pro', price: { monthly: 16, annual: 12 }, desc: 'For growing teams', features: ['Unlimited projects', '10 users', 'Advanced analytics', 'Priority support'], cta: 'Start free trial', highlighted: true },
    { name: 'Enterprise', price: { monthly: null, annual: null }, desc: 'For organizations', features: ['Everything in Pro', 'SSO/SAML', 'Audit logs', 'Custom contracts'], cta: 'Contact sales', highlighted: false },
  ];

  return (
    <div className="min-h-screen bg-black text-gray-200">
      <section className="pt-20 pb-12 text-center">
        <h1 className="text-4xl font-semibold text-white">Pricing</h1>
        <p className="mt-4 text-gray-500">Start free. Scale as you grow.</p>
        <div className="mt-8 inline-flex items-center rounded-full bg-[#222] p-1">
          <button onClick={() => setAnnual(false)} className={`rounded-full px-4 py-1.5 text-sm font-medium transition-colors ${!annual ? 'bg-white text-black' : 'text-gray-400'}`}>
            Monthly
          </button>
          <button onClick={() => setAnnual(true)} className={`rounded-full px-4 py-1.5 text-sm font-medium transition-colors ${annual ? 'bg-white text-black' : 'text-gray-400'}`}>
            Annual <span className="ml-1 text-xs text-green-400">-25%</span>
          </button>
        </div>
      </section>

      <section className="mx-auto max-w-[1000px] px-6 pb-20">
        <div className="grid gap-4 md:grid-cols-3">
          {tiers.map((tier) => (
            <div key={tier.name} className={`rounded-lg border p-8 ${tier.highlighted ? 'border-[#0070F3] bg-[#111]' : 'border-[#222] bg-[#111]'}`}>
              <h3 className="text-lg font-semibold text-white">{tier.name}</h3>
              <p className="mt-1 text-sm text-gray-500">{tier.desc}</p>
              <p className="mt-6 text-5xl font-bold text-white">
                {tier.price.monthly !== null ? `$${annual ? tier.price.annual : tier.price.monthly}` : 'Custom'}
              </p>
              {tier.price.monthly !== null && <p className="mt-1 text-sm text-gray-500">/user/month</p>}
              <button className={`mt-8 w-full rounded-md py-2.5 text-sm font-medium ${tier.highlighted ? 'bg-white text-black' : 'border border-[#333] text-gray-300'}`}>
                {tier.cta}
              </button>
              <ul className="mt-8 space-y-3">
                {tier.features.map((f) => (
                  <li key={f} className="flex items-center gap-3 text-sm text-gray-400">
                    <span className="text-[#0070F3]">check</span> {f}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </section>

      {/* Feature Comparison Table */}
      <section className="mx-auto max-w-[1000px] px-6 pb-20">
        <h2 className="text-xl font-semibold text-white">Compare plans</h2>
        <div className="mt-8 rounded-lg border border-[#1E1E1E] overflow-hidden">
          <table className="w-full">
            <thead>
              <tr className="border-b border-[#1A1A1A] bg-[#0A0A0A]">
                <th className="px-6 py-4 text-left text-xs font-medium uppercase tracking-wider text-gray-600">Feature</th>
                <th className="px-6 py-4 text-center text-xs font-medium uppercase tracking-wider text-gray-600">Free</th>
                <th className="px-6 py-4 text-center text-xs font-medium uppercase tracking-wider text-gray-600">Pro</th>
                <th className="px-6 py-4 text-center text-xs font-medium uppercase tracking-wider text-gray-600">Enterprise</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#1A1A1A]">
              {['Projects', 'Users', 'Analytics', 'SSO', 'Audit logs', 'Custom roles', 'API access', 'Support'].map((feat) => (
                <tr key={feat} className="hover:bg-[#0A0A0A]">
                  <td className="px-6 py-3 text-sm text-gray-300">{feat}</td>
                  <td className="px-6 py-3 text-center text-sm text-gray-500">Limited</td>
                  <td className="px-6 py-3 text-center text-sm text-[#0070F3]">Yes</td>
                  <td className="px-6 py-3 text-center text-sm text-[#0070F3]">Yes</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* FAQ */}
      <section className="mx-auto max-w-[700px] px-6 pb-20">
        <h2 className="text-2xl font-semibold text-white">Frequently asked questions</h2>
        <div className="mt-8 divide-y divide-[#1A1A1A]">
          {[
            { q: 'Can I switch plans anytime?', a: 'Yes. Upgrade or downgrade at any time. Changes take effect immediately with prorated billing.' },
            { q: 'Is there a free trial for Pro?', a: 'Yes, every Pro plan starts with a 14-day free trial. No credit card required.' },
            { q: 'What payment methods do you accept?', a: 'We accept all major credit cards, ACH transfers, and wire transfers for Enterprise.' },
            { q: 'Can I cancel anytime?', a: 'Cancel from your billing settings with one click. No cancellation fees.' },
          ].map(({ q, a }) => (
            <details key={q} className="group py-5">
              <summary className="flex cursor-pointer items-center justify-between text-[15px] font-medium text-gray-300 group-open:text-white">
                {q}
                <span className="text-gray-600 group-open:rotate-45 transition-transform">+</span>
              </summary>
              <p className="mt-3 text-sm leading-relaxed text-gray-500">{a}</p>
            </details>
          ))}
        </div>
      </section>
    </div>
  );
}
```

### Variant B: Warm (Notion/Figma Style)

**Color Application**
```
Background:             #FFFFFF
Card background:        #FFFFFF ring-1 ring-[#E8E5E0]
Highlighted tier:       #FFFFFF ring-2 ring-[#2F80ED] shadow-lg
Toggle:                 #F0EDE6 background
Toggle active:          #2F80ED bg, #FFFFFF text
Check icon:             #2F80ED
FAQ background:         Open state gets #FFFCF7
Price color:            #37352F
```

**Component Differences**
- Rounded cards (12px border-radius) with warm shadows
- Toggle uses filled style rather than background swap
- Feature list uses filled circle checks instead of text
- FAQ uses chevron icon, open state has warm background tint

### Variant C: Bold (Stripe/Loom Style)

**Color Application**
```
Background gradient:    #0A2540 at top, transitions to #FFFFFF from tier cards down
Card background:        #FFFFFF with shadow-xl
Highlighted tier:       scale(1.05) transform, 4px gradient top-border (#80E9FF to #635BFF)
CTA:                    #635BFF pill buttons with shadow
Price:                  #0A2540, 64px, font-weight 800
Comparison:             Zebra striping #F6F9FC / #FFFFFF
Enterprise banner:      Full-width gradient #0A2540 to #1B1B50
```

---

## 3. SaaS Signup/Onboarding Flow (3-4 Steps)

### Block Sequence
1. Step indicator (progress bar or step numbers)
2. Step content area (form fields or selections)
3. Navigation (back/next buttons)
4. Side panel (optional for Warm/Bold variants)

### Step Breakdown
- **Step 1: Account creation** — Email, password (or SSO), name
- **Step 2: Workspace setup** — Team name, URL slug, invite teammates
- **Step 3: Personalization** — Role, use case, goals (selection chips)
- **Step 4: First action** — Create first project, import data, or explore template

### Variant A: Minimal (Linear/Vercel Style)

**Layout**: Centered single column, 480px max-width, no side panel
**Progress**: Minimal bar segments at top

**React/TSX Skeleton**
```tsx
import { useState } from 'react';

export function OnboardingMinimal() {
  const [step, setStep] = useState(1);
  const totalSteps = 4;

  return (
    <div className="flex min-h-screen items-center justify-center bg-black">
      <div className="w-full max-w-[480px] px-6">
        <div className="mb-12 flex items-center justify-center gap-2">
          {Array.from({ length: totalSteps }).map((_, i) => (
            <div key={i} className={`h-1 w-8 rounded-full transition-colors ${i + 1 <= step ? 'bg-white' : 'bg-[#333]'}`} />
          ))}
        </div>

        {step === 1 && (
          <div>
            <h2 className="text-2xl font-semibold text-white">Create your account</h2>
            <p className="mt-2 text-sm text-gray-500">Get started in seconds.</p>
            <div className="mt-8 space-y-4">
              <button className="flex w-full items-center justify-center gap-3 rounded-md border border-[#333] py-3 text-sm font-medium text-gray-300 hover:border-gray-500">
                Continue with Google
              </button>
              <button className="flex w-full items-center justify-center gap-3 rounded-md border border-[#333] py-3 text-sm font-medium text-gray-300 hover:border-gray-500">
                Continue with GitHub
              </button>
              <div className="flex items-center gap-3">
                <div className="h-px flex-1 bg-[#222]" />
                <span className="text-xs text-gray-600">or</span>
                <div className="h-px flex-1 bg-[#222]" />
              </div>
              <input type="email" placeholder="Email address" className="w-full rounded-md border border-[#333] bg-transparent px-4 py-3 text-sm text-white placeholder:text-gray-600 focus:border-[#0070F3] focus:outline-none" />
              <input type="password" placeholder="Password" className="w-full rounded-md border border-[#333] bg-transparent px-4 py-3 text-sm text-white placeholder:text-gray-600 focus:border-[#0070F3] focus:outline-none" />
            </div>
          </div>
        )}

        {step === 2 && (
          <div>
            <h2 className="text-2xl font-semibold text-white">Set up your workspace</h2>
            <p className="mt-2 text-sm text-gray-500">This is where your team will collaborate.</p>
            <div className="mt-8 space-y-4">
              <div>
                <label className="text-xs font-medium text-gray-500">Workspace name</label>
                <input type="text" placeholder="Acme Inc" className="mt-2 w-full rounded-md border border-[#333] bg-transparent px-4 py-3 text-sm text-white placeholder:text-gray-600 focus:border-[#0070F3] focus:outline-none" />
              </div>
              <div>
                <label className="text-xs font-medium text-gray-500">Workspace URL</label>
                <div className="mt-2 flex items-center rounded-md border border-[#333] px-4 py-3">
                  <span className="text-sm text-gray-600">app.product.com/</span>
                  <input type="text" placeholder="acme" className="ml-1 flex-1 bg-transparent text-sm text-white placeholder:text-gray-600 focus:outline-none" />
                </div>
              </div>
              <div>
                <label className="text-xs font-medium text-gray-500">Invite teammates (optional)</label>
                <input type="email" placeholder="teammate@company.com" className="mt-2 w-full rounded-md border border-[#333] bg-transparent px-4 py-3 text-sm text-white placeholder:text-gray-600 focus:border-[#0070F3] focus:outline-none" />
              </div>
            </div>
          </div>
        )}

        {step === 3 && (
          <div>
            <h2 className="text-2xl font-semibold text-white">What is your role?</h2>
            <p className="mt-2 text-sm text-gray-500">We will customize your experience.</p>
            <div className="mt-8 grid grid-cols-2 gap-3">
              {['Engineering', 'Design', 'Product', 'Marketing', 'Operations', 'Founder', 'Sales', 'Other'].map((role) => (
                <button key={role} className="rounded-md border border-[#333] px-4 py-3 text-sm text-gray-300 hover:border-[#0070F3] hover:text-white transition-colors">
                  {role}
                </button>
              ))}
            </div>
          </div>
        )}

        {step === 4 && (
          <div>
            <h2 className="text-2xl font-semibold text-white">Ready to go</h2>
            <p className="mt-2 text-sm text-gray-500">Pick your starting point.</p>
            <div className="mt-8 space-y-3">
              <button className="w-full rounded-md bg-white py-3 text-sm font-medium text-black hover:bg-gray-200">
                Create blank project
              </button>
              <button className="w-full rounded-md border border-[#333] py-3 text-sm font-medium text-gray-300 hover:border-gray-500">
                Browse templates
              </button>
              <button className="w-full rounded-md border border-[#333] py-3 text-sm font-medium text-gray-300 hover:border-gray-500">
                Import from another tool
              </button>
            </div>
          </div>
        )}

        <div className="mt-10 flex items-center justify-between">
          {step > 1 ? (
            <button onClick={() => setStep(step - 1)} className="text-sm text-gray-500 hover:text-white">Back</button>
          ) : <span />}
          <button onClick={() => setStep(Math.min(step + 1, totalSteps))} className="rounded-md bg-white px-6 py-2.5 text-sm font-medium text-black">
            {step === totalSteps ? 'Launch' : 'Continue'}
          </button>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Warm (Notion/Figma Style)

**Layout**: Split panel - left 50% form on white, right 50% warm illustration/value prop on #F7F5F0
**Progress**: Numbered steps with labels connected by horizontal line
**Inputs**: White background, warm border #E3E2DE, focus: #2F80ED
**Chips**: Rounded-lg, warm hover with #FDEBCF background

### Variant C: Bold (Stripe/Loom Style)

**Layout**: Centered card (560px max-width) floating on gradient background
**Progress**: Gradient animated progress bar at card top (width transitions 25/50/75/100%)
**Card**: White, rounded-2xl, shadow-2xl on dark gradient bg
**CTA**: #635BFF rounded-full buttons with shadow

---

## 4. SaaS Dashboard (Analytics Overview)

### Block Sequence
1. Top bar (breadcrumb + date range selector + refresh)
2. Metric summary cards (4 across)
3. Primary chart (line/area chart, full width)
4. Secondary charts row (2 side by side)
5. Data table (recent activity or top items)
6. Quick actions inline

### Variant A: Minimal (Linear/Vercel Style)

**Typography Map**
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Page title | Inter | 600 | 24px | 32px |
| Metric label | Inter | 400 | 13px | 18px |
| Metric value | Inter | 600 | 28px | 36px |
| Metric delta | Inter | 500 | 12px | 16px |
| Chart axis | Inter | 400 | 11px | 14px |
| Table header | Inter | 500 | 12px | 16px |
| Table cell | Inter | 400 | 13px | 18px |

**Color Application**
```
Background:             #0A0A0A
Sidebar:                #000000 border-right: 1px solid #1A1A1A
Card backgrounds:       #111111 border: 1px solid #1E1E1E
Metric positive delta:  #22C55E
Metric negative delta:  #EF4444
Chart line:             #0070F3
Chart grid:             #1A1A1A
Chart area fill:        #0070F3 at 10% opacity
Table row hover:        #151515
Table border:           #1A1A1A
```

**React/TSX Skeleton**
```tsx
export function DashboardMinimal() {
  const metrics = [
    { label: 'Total Revenue', value: '$48,290', delta: '+12.5%', positive: true },
    { label: 'Active Users', value: '2,847', delta: '+8.2%', positive: true },
    { label: 'Churn Rate', value: '2.1%', delta: '-0.3%', positive: true },
    { label: 'MRR', value: '$12,480', delta: '+15.7%', positive: true },
  ];

  return (
    <div className="flex min-h-screen bg-[#0A0A0A]">
      <aside className="hidden w-60 border-r border-[#1A1A1A] bg-black p-4 lg:block">
        <div className="text-sm font-semibold text-white">ProductName</div>
        <nav className="mt-8 space-y-1">
          {['Dashboard', 'Projects', 'Team', 'Analytics', 'Settings'].map((item) => (
            <a key={item} href="#" className={`block rounded-md px-3 py-2 text-sm ${item === 'Dashboard' ? 'bg-[#111] text-white' : 'text-gray-500 hover:text-gray-300'}`}>
              {item}
            </a>
          ))}
        </nav>
      </aside>

      <main className="flex-1 p-8">
        <div className="flex items-center justify-between">
          <h1 className="text-2xl font-semibold text-white">Dashboard</h1>
          <div className="flex items-center gap-3">
            <select className="rounded-md border border-[#333] bg-transparent px-3 py-1.5 text-sm text-gray-400">
              <option>Last 30 days</option>
              <option>Last 7 days</option>
              <option>Last 90 days</option>
            </select>
            <button className="rounded-md border border-[#333] px-3 py-1.5 text-sm text-gray-400 hover:text-white">Refresh</button>
          </div>
        </div>

        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {metrics.map((m) => (
            <div key={m.label} className="rounded-lg border border-[#1E1E1E] bg-[#111] p-6">
              <p className="text-[13px] text-gray-500">{m.label}</p>
              <p className="mt-2 text-[28px] font-semibold text-white">{m.value}</p>
              <p className={`mt-1 text-xs font-medium ${m.positive ? 'text-green-500' : 'text-red-500'}`}>{m.delta}</p>
            </div>
          ))}
        </div>

        <div className="mt-6 rounded-lg border border-[#1E1E1E] bg-[#111] p-6">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-medium text-gray-400">Revenue over time</h3>
            <div className="flex gap-2">
              {['1W', '1M', '3M', '1Y'].map((r) => (
                <button key={r} className="rounded px-2 py-1 text-xs text-gray-500 hover:bg-[#1A1A1A] hover:text-white">{r}</button>
              ))}
            </div>
          </div>
          <div className="mt-4 h-64 rounded bg-[#0A0A0A]" />
        </div>

        <div className="mt-6 grid gap-6 lg:grid-cols-2">
          <div className="rounded-lg border border-[#1E1E1E] bg-[#111] p-6">
            <h3 className="text-sm font-medium text-gray-400">Users by plan</h3>
            <div className="mt-4 h-48 rounded bg-[#0A0A0A]" />
          </div>
          <div className="rounded-lg border border-[#1E1E1E] bg-[#111] p-6">
            <h3 className="text-sm font-medium text-gray-400">Conversion funnel</h3>
            <div className="mt-4 h-48 rounded bg-[#0A0A0A]" />
          </div>
        </div>

        <div className="mt-6 rounded-lg border border-[#1E1E1E] bg-[#111]">
          <div className="flex items-center justify-between border-b border-[#1A1A1A] px-6 py-3">
            <h3 className="text-sm font-medium text-gray-400">Recent Activity</h3>
            <a href="#" className="text-xs text-[#0070F3]">View all</a>
          </div>
          <table className="w-full">
            <thead>
              <tr className="border-b border-[#1A1A1A] text-left text-xs font-medium uppercase tracking-wider text-gray-600">
                <th className="px-6 py-3">Event</th>
                <th className="px-6 py-3">User</th>
                <th className="px-6 py-3">Time</th>
                <th className="px-6 py-3">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#1A1A1A]">
              {[1, 2, 3, 4, 5].map((i) => (
                <tr key={i} className="hover:bg-[#151515]">
                  <td className="px-6 py-3 text-[13px] text-gray-300">User signed up</td>
                  <td className="px-6 py-3 text-[13px] text-gray-500">user{i}@email.com</td>
                  <td className="px-6 py-3 text-[13px] text-gray-600">{i * 2}m ago</td>
                  <td className="px-6 py-3"><span className="rounded-full bg-green-500/10 px-2 py-0.5 text-xs text-green-500">Active</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </div>
  );
}
```

### Variant B: Warm — White bg, warm gray sidebar, colored metric borders, serif section headers, warm chart palette
### Variant C: Bold — Gradient header, 36px bold metric values, gradient chart fills, purple interactive accents

---

## 5. SaaS Settings Page

### Block Sequence
1. Settings sidebar navigation (vertical tabs)
2. Settings header (section title + description)
3. Form sections (grouped fields with dividers)
4. Action bar (save/cancel, sticky bottom or inline)

### Variant A: Minimal (Linear/Vercel Style)

**Layout**: 240px sidebar + content, max-width 640px form

**React/TSX Skeleton**
```tsx
export function SettingsMinimal() {
  const sections = ['General', 'Profile', 'Notifications', 'Security', 'API', 'Billing', 'Danger Zone'];

  return (
    <div className="flex min-h-screen bg-[#0A0A0A]">
      <aside className="w-60 border-r border-[#1A1A1A] p-6">
        <h2 className="text-sm font-semibold text-white">Settings</h2>
        <nav className="mt-6 space-y-1">
          {sections.map((s) => (
            <a key={s} href="#" className={`block rounded-md px-3 py-2 text-sm ${s === 'General' ? 'bg-[#111] text-white' : s === 'Danger Zone' ? 'text-red-400 hover:text-red-300' : 'text-gray-500 hover:text-gray-300'}`}>
              {s}
            </a>
          ))}
        </nav>
      </aside>

      <main className="flex-1 p-10">
        <div className="max-w-[640px]">
          <h1 className="text-xl font-semibold text-white">General</h1>
          <p className="mt-1 text-sm text-gray-500">Manage your workspace settings.</p>

          <div className="mt-10 space-y-8">
            <div>
              <label className="block text-sm font-medium text-gray-300">Workspace name</label>
              <input type="text" defaultValue="My Workspace" className="mt-2 w-full rounded-md border border-[#333] bg-transparent px-4 py-2.5 text-sm text-white focus:border-[#0070F3] focus:outline-none" />
              <p className="mt-1.5 text-xs text-gray-600">Displayed across your workspace.</p>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-300">Workspace URL</label>
              <div className="mt-2 flex items-center rounded-md border border-[#333] px-4 py-2.5">
                <span className="text-sm text-gray-600">app.product.com/</span>
                <input type="text" defaultValue="my-workspace" className="flex-1 bg-transparent text-sm text-white focus:outline-none" />
              </div>
            </div>
            <div className="border-t border-[#1A1A1A] pt-8">
              <label className="block text-sm font-medium text-gray-300">Timezone</label>
              <select className="mt-2 w-full rounded-md border border-[#333] bg-transparent px-4 py-2.5 text-sm text-gray-400">
                <option>Pacific Time (PT)</option>
                <option>Eastern Time (ET)</option>
                <option>UTC</option>
              </select>
            </div>
            <div className="border-t border-[#1A1A1A] pt-8">
              <label className="block text-sm font-medium text-gray-300">Language</label>
              <select className="mt-2 w-full rounded-md border border-[#333] bg-transparent px-4 py-2.5 text-sm text-gray-400">
                <option>English (US)</option>
                <option>Spanish</option>
                <option>French</option>
              </select>
            </div>
          </div>

          <div className="mt-10 flex gap-3">
            <button className="rounded-md bg-white px-4 py-2 text-sm font-medium text-black hover:bg-gray-200">Save changes</button>
            <button className="rounded-md border border-[#333] px-4 py-2 text-sm font-medium text-gray-400 hover:text-white">Cancel</button>
          </div>
        </div>
      </main>
    </div>
  );
}
```

### Variant B: Warm — White bg, warm dividers, field groups in shadow cards, serif section headers
### Variant C: Bold — Card-based sections, gradient header, colored section icons, bold save button

---

## 6. SaaS Team Management Page

### Block Sequence
1. Page header (title + invite button)
2. Search and filter bar
3. Team member table (avatar, name, email, role, status, actions)
4. Pending invitations section
5. Role management (admin only)

### Variant A: Minimal (Linear/Vercel Style)

**React/TSX Skeleton**
```tsx
export function TeamMinimal() {
  const members = [
    { name: 'Alice Chen', email: 'alice@co.com', role: 'Admin', status: 'Active', initials: 'AC' },
    { name: 'Bob Patel', email: 'bob@co.com', role: 'Member', status: 'Active', initials: 'BP' },
    { name: 'Carol Wu', email: 'carol@co.com', role: 'Member', status: 'Invited', initials: 'CW' },
    { name: 'Dave Kim', email: 'dave@co.com', role: 'Viewer', status: 'Active', initials: 'DK' },
  ];

  return (
    <div className="min-h-screen bg-[#0A0A0A] p-10">
      <div className="mx-auto max-w-[900px]">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-xl font-semibold text-white">Team</h1>
            <p className="mt-1 text-sm text-gray-500">Manage members and permissions.</p>
          </div>
          <button className="rounded-md bg-white px-4 py-2 text-sm font-medium text-black hover:bg-gray-200">Invite member</button>
        </div>

        <input type="search" placeholder="Search members..." className="mt-6 w-full rounded-md border border-[#333] bg-transparent px-4 py-2.5 text-sm text-white placeholder:text-gray-600 focus:border-[#0070F3] focus:outline-none" />

        <div className="mt-6 rounded-lg border border-[#1E1E1E] bg-[#111]">
          <table className="w-full">
            <thead>
              <tr className="border-b border-[#1A1A1A] text-left text-xs font-medium uppercase tracking-wider text-gray-600">
                <th className="px-6 py-3">Member</th>
                <th className="px-6 py-3">Role</th>
                <th className="px-6 py-3">Status</th>
                <th className="px-6 py-3" />
              </tr>
            </thead>
            <tbody className="divide-y divide-[#1A1A1A]">
              {members.map((m) => (
                <tr key={m.email} className="hover:bg-[#151515]">
                  <td className="px-6 py-4">
                    <div className="flex items-center gap-3">
                      <div className="flex h-8 w-8 items-center justify-center rounded-full bg-[#222] text-xs font-medium text-gray-400">{m.initials}</div>
                      <div>
                        <p className="text-sm font-medium text-white">{m.name}</p>
                        <p className="text-xs text-gray-500">{m.email}</p>
                      </div>
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    <span className="rounded-md bg-[#1A1A1A] px-2 py-1 text-xs text-gray-400">{m.role}</span>
                  </td>
                  <td className="px-6 py-4">
                    <span className={`inline-flex items-center gap-1.5 text-xs ${m.status === 'Active' ? 'text-green-500' : 'text-yellow-500'}`}>
                      <span className={`h-1.5 w-1.5 rounded-full ${m.status === 'Active' ? 'bg-green-500' : 'bg-yellow-500'}`} />
                      {m.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-right">
                    <button className="rounded-md px-2 py-1 text-xs text-gray-600 hover:bg-[#1A1A1A] hover:text-gray-400">...</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Warm — White table, colored avatar backgrounds, warm role badges, friendly hover states
### Variant C: Bold — Card-per-member on mobile, gradient invite button, rich role dropdowns

---

## 7. SaaS Billing Page

### Block Sequence
1. Current plan summary card
2. Usage metrics with progress bars
3. Payment method section
4. Invoice history table
5. Upgrade/downgrade CTA

### Variant A: Minimal (Linear/Vercel Style)

**React/TSX Skeleton**
```tsx
export function BillingMinimal() {
  return (
    <div className="min-h-screen bg-[#0A0A0A] p-10">
      <div className="mx-auto max-w-[720px]">
        <h1 className="text-xl font-semibold text-white">Billing</h1>
        <p className="mt-1 text-sm text-gray-500">Manage subscription and payments.</p>

        <div className="mt-8 rounded-lg border border-[#1E1E1E] bg-[#111] p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-xs uppercase tracking-wider text-gray-600">Current plan</p>
              <p className="mt-1 text-lg font-semibold text-white">Pro Plan</p>
              <p className="mt-1 text-sm text-gray-500">$12/user/month billed annually</p>
            </div>
            <button className="rounded-md border border-[#333] px-4 py-2 text-sm text-gray-300 hover:border-gray-500">Change plan</button>
          </div>
          <div className="mt-4 flex items-center gap-2">
            <span className="rounded-full bg-green-500/10 px-2 py-0.5 text-xs text-green-500">Active</span>
            <span className="text-xs text-gray-600">Next billing: Apr 1, 2026</span>
          </div>
        </div>

        <div className="mt-6 grid gap-4 sm:grid-cols-3">
          {[
            { label: 'Team members', display: '7 / 10', pct: 70 },
            { label: 'Storage', display: '4.2 GB / 10 GB', pct: 42 },
            { label: 'API calls', display: '12.4k / 50k', pct: 25 },
          ].map((u) => (
            <div key={u.label} className="rounded-lg border border-[#1E1E1E] bg-[#111] p-5">
              <p className="text-xs text-gray-600">{u.label}</p>
              <p className="mt-2 text-lg font-semibold text-white">{u.display}</p>
              <div className="mt-3 h-1.5 rounded-full bg-[#222]">
                <div className="h-full rounded-full bg-[#0070F3]" style={{ width: `${u.pct}%` }} />
              </div>
            </div>
          ))}
        </div>

        <div className="mt-6 rounded-lg border border-[#1E1E1E] bg-[#111] p-6">
          <h3 className="text-sm font-medium text-gray-400">Payment method</h3>
          <div className="mt-4 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="flex h-8 w-12 items-center justify-center rounded bg-[#222] text-xs text-gray-500">VISA</div>
              <div>
                <p className="text-sm text-white">Visa ending in 4242</p>
                <p className="text-xs text-gray-600">Expires 12/2027</p>
              </div>
            </div>
            <button className="text-sm text-gray-500 hover:text-white">Update</button>
          </div>
        </div>

        <div className="mt-6 rounded-lg border border-[#1E1E1E] bg-[#111]">
          <div className="flex items-center justify-between border-b border-[#1A1A1A] px-6 py-3">
            <h3 className="text-sm font-medium text-gray-400">Invoices</h3>
            <a href="#" className="text-xs text-[#0070F3]">View all</a>
          </div>
          <div className="divide-y divide-[#1A1A1A]">
            {['Mar 1, 2026', 'Feb 1, 2026', 'Jan 1, 2026'].map((d) => (
              <div key={d} className="flex items-center justify-between px-6 py-3">
                <div className="flex items-center gap-4">
                  <span className="text-sm text-gray-300">{d}</span>
                  <span className="rounded-full bg-green-500/10 px-2 py-0.5 text-xs text-green-500">Paid</span>
                </div>
                <div className="flex items-center gap-4">
                  <span className="text-sm text-gray-400">$84.00</span>
                  <a href="#" className="text-xs text-[#0070F3]">Download</a>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Warm — White cards, colored progress bars, warm invoice rows, friendly amounts
### Variant C: Bold — Gradient plan header, bold usage meters, pill action buttons, purple accents

---

## 8. SaaS Integration Marketplace

### Block Sequence
1. Page header (title + search)
2. Category filter pills (horizontal scroll)
3. Integration grid (icon + name + description + connect button)
4. Integration detail modal
5. Installed integrations section

### Variant A: Minimal (Linear/Vercel Style)

**React/TSX Skeleton**
```tsx
import { useState } from 'react';

export function IntegrationsMinimal() {
  const [active, setActive] = useState('All');
  const categories = ['All', 'Communication', 'Development', 'Analytics', 'Design', 'Storage'];
  const integrations = [
    { name: 'Slack', desc: 'Get notifications in channels', cat: 'Communication', installed: true },
    { name: 'GitHub', desc: 'Sync issues and PRs', cat: 'Development', installed: true },
    { name: 'Figma', desc: 'Embed designs in projects', cat: 'Design', installed: false },
    { name: 'Segment', desc: 'Track product events', cat: 'Analytics', installed: false },
    { name: 'Google Drive', desc: 'Attach Drive files', cat: 'Storage', installed: false },
    { name: 'Linear', desc: 'Two-way issue sync', cat: 'Development', installed: false },
    { name: 'Jira', desc: 'Import Jira issues', cat: 'Development', installed: false },
    { name: 'Datadog', desc: 'Monitor performance', cat: 'Analytics', installed: false },
  ];
  const filtered = active === 'All' ? integrations : integrations.filter((i) => i.cat === active);

  return (
    <div className="min-h-screen bg-[#0A0A0A] p-10">
      <div className="mx-auto max-w-[1100px]">
        <div className="flex items-center justify-between">
          <h1 className="text-xl font-semibold text-white">Integrations</h1>
          <input type="search" placeholder="Search..." className="w-64 rounded-md border border-[#333] bg-transparent px-4 py-2 text-sm text-white placeholder:text-gray-600 focus:border-[#0070F3] focus:outline-none" />
        </div>

        <div className="mt-6 flex gap-2 overflow-x-auto">
          {categories.map((c) => (
            <button key={c} onClick={() => setActive(c)} className={`flex-shrink-0 rounded-full px-4 py-1.5 text-xs font-medium ${c === active ? 'bg-white text-black' : 'bg-[#1A1A1A] text-gray-400 hover:text-white'}`}>
              {c}
            </button>
          ))}
        </div>

        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {filtered.map((i) => (
            <div key={i.name} className="flex items-start gap-4 rounded-lg border border-[#1E1E1E] bg-[#111] p-5 hover:border-[#333] transition-colors">
              <div className="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-lg bg-[#222] text-xs font-medium text-gray-500">{i.name[0]}</div>
              <div className="flex-1 min-w-0">
                <h3 className="text-sm font-semibold text-white">{i.name}</h3>
                <p className="mt-1 text-xs text-gray-500">{i.desc}</p>
                <button className={`mt-3 rounded-md px-3 py-1 text-xs font-medium ${i.installed ? 'bg-green-500/10 text-green-500' : 'border border-[#333] text-gray-400 hover:border-[#0070F3] hover:text-[#0070F3]'}`}>
                  {i.installed ? 'Connected' : 'Connect'}
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Warm — White grid, colored icons, warm connect states, modal with setup wizard
### Variant C: Bold — Large cards, gradient connect button, brand-colored integration icons

---

## 9. SaaS Changelog/Updates Page

### Block Sequence
1. Page header (title + RSS/subscribe)
2. Version timeline (vertical, newest first)
3. Each entry: date, version tag, title, description, optional screenshot
4. Load more / pagination

### Variant A: Minimal (Linear/Vercel Style)

**React/TSX Skeleton**
```tsx
export function ChangelogMinimal() {
  const entries = [
    { date: 'Mar 10, 2026', version: 'v2.4.0', tag: 'Feature', title: 'Command Palette Redesign', desc: 'Rebuilt command palette with fuzzy search, recent commands, and contextual actions.', hasImage: true },
    { date: 'Mar 3, 2026', version: 'v2.3.2', tag: 'Improvement', title: 'Performance Improvements', desc: 'Reduced initial load time by 40%. Dashboard renders in under 200ms.', hasImage: false },
    { date: 'Feb 24, 2026', version: 'v2.3.1', tag: 'Fix', title: 'Bug Fixes', desc: 'Fixed notification preferences not saving. Resolved timezone offset in reports.', hasImage: false },
    { date: 'Feb 15, 2026', version: 'v2.3.0', tag: 'Feature', title: 'Team Permissions Overhaul', desc: 'Granular RBAC with custom roles. Audit log for permission changes. Bulk role assignment.', hasImage: true },
  ];

  const tagColor: Record<string, string> = { Feature: 'text-[#0070F3]', Improvement: 'text-green-500', Fix: 'text-yellow-500' };

  return (
    <div className="min-h-screen bg-black py-20">
      <div className="mx-auto max-w-[680px] px-6">
        <div className="flex items-center justify-between">
          <h1 className="text-2xl font-semibold text-white">Changelog</h1>
          <a href="/rss" className="text-sm text-gray-600 hover:text-gray-400">Subscribe</a>
        </div>

        <div className="mt-16 space-y-20">
          {entries.map((e) => (
            <article key={e.version} className="relative border-l border-[#222] pl-8">
              <div className="absolute -left-1.5 top-1 h-3 w-3 rounded-full border-2 border-[#333] bg-black" />
              <div className="flex flex-wrap items-center gap-3">
                <time className="text-xs text-gray-600">{e.date}</time>
                <span className="rounded bg-[#1A1A1A] px-2 py-0.5 text-[11px] font-medium text-gray-500">{e.version}</span>
                <span className={`text-[11px] font-medium ${tagColor[e.tag]}`}>{e.tag}</span>
              </div>
              <h2 className="mt-3 text-xl font-semibold text-white">{e.title}</h2>
              <p className="mt-3 text-sm leading-relaxed text-gray-400">{e.desc}</p>
              {e.hasImage && <div className="mt-6 aspect-[16/9] rounded-lg border border-[#1E1E1E] bg-[#111]" />}
            </article>
          ))}
        </div>

        <div className="mt-20 text-center">
          <button className="rounded-md border border-[#333] px-6 py-2.5 text-sm text-gray-400 hover:text-white">Load more</button>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Warm — White bg, colored version badges, serif titles, warm screenshot frames
### Variant C: Bold — Card-per-entry, gradient version headers, large screenshots, animated reveals

---

## 10. SaaS Documentation / Help Center

### Block Sequence
1. Search header (prominent search bar)
2. Category grid (6-8 categories with icons and counts)
3. Popular articles list
4. Article view (sidebar TOC + content + feedback + prev/next)

### Variant A: Minimal (Linear/Vercel Style)

**React/TSX Skeleton — Index**
```tsx
export function DocsIndexMinimal() {
  const categories = [
    { name: 'Getting Started', count: 12 },
    { name: 'Account & Billing', count: 8 },
    { name: 'Integrations', count: 15 },
    { name: 'API Reference', count: 24 },
    { name: 'Security', count: 6 },
    { name: 'Troubleshooting', count: 10 },
  ];

  return (
    <div className="min-h-screen bg-black">
      <section className="border-b border-[#1A1A1A] bg-[#0A0A0A] py-20">
        <div className="mx-auto max-w-[640px] px-6 text-center">
          <h1 className="text-3xl font-semibold text-white">Help Center</h1>
          <p className="mt-3 text-sm text-gray-500">Search docs or browse categories below.</p>
          <input type="search" placeholder="Search docs..." className="mt-8 w-full rounded-lg border border-[#333] bg-[#111] px-5 py-3.5 text-sm text-white placeholder:text-gray-600 focus:border-[#0070F3] focus:outline-none" />
        </div>
      </section>

      <section className="py-16">
        <div className="mx-auto max-w-[900px] px-6">
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {categories.map((c) => (
              <a key={c.name} href="#" className="rounded-lg border border-[#1E1E1E] bg-[#111] p-6 hover:border-[#333] transition-colors">
                <h3 className="text-sm font-semibold text-white">{c.name}</h3>
                <p className="mt-1 text-xs text-gray-600">{c.count} articles</p>
              </a>
            ))}
          </div>
        </div>
      </section>

      <section className="border-t border-[#1A1A1A] py-16">
        <div className="mx-auto max-w-[900px] px-6">
          <h2 className="text-lg font-semibold text-white">Popular articles</h2>
          <div className="mt-6 space-y-1">
            {['How to invite team members', 'Setting up SSO', 'API authentication', 'Webhook config', 'Exporting data'].map((a) => (
              <a key={a} href="#" className="flex items-center justify-between rounded-md px-4 py-3 text-sm text-gray-300 hover:bg-[#111]">
                {a}
                <span className="text-gray-700">-&gt;</span>
              </a>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
```

**React/TSX Skeleton — Article**
```tsx
export function DocArticleMinimal() {
  return (
    <div className="flex min-h-screen bg-black">
      <aside className="hidden w-64 border-r border-[#1A1A1A] p-6 lg:block">
        <a href="/docs" className="text-xs text-gray-600 hover:text-gray-400">Back to Help Center</a>
        <p className="mt-6 text-xs uppercase tracking-wider text-gray-600">On this page</p>
        <nav className="mt-4 space-y-2">
          {['Overview', 'Prerequisites', 'Step 1', 'Step 2', 'Step 3', 'Troubleshooting'].map((s) => (
            <a key={s} href="#" className="block text-sm text-gray-500 hover:text-white">{s}</a>
          ))}
        </nav>
      </aside>

      <main className="flex-1 px-12 py-10">
        <div className="max-w-[680px]">
          <nav className="flex items-center gap-2 text-xs text-gray-600">
            <a href="/docs" className="hover:text-gray-400">Help Center</a>
            <span>/</span>
            <a href="#" className="hover:text-gray-400">API Reference</a>
            <span>/</span>
            <span className="text-gray-400">Authentication</span>
          </nav>

          <h1 className="mt-6 text-2xl font-semibold text-white">API Authentication Guide</h1>
          <p className="mt-2 text-sm text-gray-500">Last updated Mar 8, 2026</p>

          <div className="mt-8 space-y-6">
            <p className="text-sm leading-relaxed text-gray-400">
              Learn how to authenticate API requests using API keys or OAuth tokens.
            </p>
            <h2 className="text-lg font-semibold text-white">Prerequisites</h2>
            <ul className="list-disc pl-5 space-y-1 text-sm text-gray-400">
              <li>A ProductName account with API access</li>
              <li>Admin or developer role</li>
            </ul>
            <h2 className="text-lg font-semibold text-white">Create an API Key</h2>
            <p className="text-sm leading-relaxed text-gray-400">
              Navigate to Settings, then API, then click Create new key.
            </p>
            <div className="rounded-lg bg-[#111] p-4 font-mono text-sm text-gray-300">
              <code>curl -H "Authorization: Bearer sk_live_..." https://api.product.com/v1/users</code>
            </div>
          </div>

          <div className="mt-16 flex items-center gap-4 border-t border-[#1A1A1A] pt-8">
            <span className="text-sm text-gray-500">Was this helpful?</span>
            <button className="rounded-md border border-[#333] px-3 py-1 text-xs text-gray-400 hover:text-[#0070F3]">Yes</button>
            <button className="rounded-md border border-[#333] px-3 py-1 text-xs text-gray-400 hover:text-red-500">No</button>
          </div>

          <div className="mt-8 flex items-center justify-between border-t border-[#1A1A1A] pt-8">
            <a href="#" className="text-sm text-[#0070F3]">Previous: API Overview</a>
            <a href="#" className="text-sm text-[#0070F3]">Next: Rate Limits</a>
          </div>
        </div>
      </main>
    </div>
  );
}
```

### Variant B: Warm — White bg, warm search, illustrated categories, serif article headings
### Variant C: Bold — Gradient search header, large category cards, bold typography, purple accents

---

## Cross-Variant Summary Matrix

| Page | Minimal (Linear/Vercel) | Warm (Notion/Figma) | Bold (Stripe/Loom) |
|---|---|---|---|
| Landing | Black bg, text-only hero, ghost buttons | Off-white, serif headlines, split hero | Gradient hero, oversized type, pill CTAs |
| Pricing | Dark cards, dot toggle, comparison table | White cards, warm shadows, filled toggle | Gradient header, scaled highlight card |
| Onboarding | Centered column, bar progress | Split layout, step labels | Card on gradient, animated bar |
| Dashboard | Dark panels, monochrome charts | White, colored metrics, warm palette | Gradient header, bold metric values |
| Settings | Dark sidebar + form, minimal | Light sidebar, warm dividers | Card sections, colored headers |
| Team | Dark table, initial avatars | White table, colored role badges | Card-per-member, rich dropdowns |
| Billing | Dark cards, blue progress bars | White, colored meters | Gradient plan header, bold meters |
| Integrations | Dark grid, ghost connect | White grid, colored icons | Large cards, gradient connect |
| Changelog | Dark timeline, left border | White timeline, colored tags | Card-per-entry, gradient badges |
| Docs | Dark search, minimal grid | Warm search, illustrated cats | Gradient header, bold categories |

---

## Implementation Notes

### Responsive Breakpoints (All Variants)
```css
@media (min-width: 640px)  { /* sm: 2-column grids */ }
@media (min-width: 768px)  { /* md: tablet layouts */ }
@media (min-width: 1024px) { /* lg: sidebar layouts */ }
@media (min-width: 1280px) { /* xl: max-width containers */ }
```

### Shared Patterns
- All pages include keyboard navigation support
- All forms include proper labels, focus states, and error messages
- All tables support sorting and column resizing on desktop
- All modals trap focus and close on Escape
- All pages include loading skeletons for async content
- All interactive elements need visible focus rings

### Design Token Integration
Replace hardcoded values with tokens from `saas-productivity-style.md`:
```
bg-black          -> var(--color-surface-base)
text-white        -> var(--color-text-primary)
border-[#1E1E1E]  -> var(--color-border-default)
bg-[#0070F3]      -> var(--color-accent-primary)
```
