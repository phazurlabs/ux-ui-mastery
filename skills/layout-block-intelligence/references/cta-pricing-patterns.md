# CTA & Pricing Patterns — 50+ Production-Ready Variants

## Conversion Block Psychology

CTA and pricing blocks exist at the critical juncture between interest and action. They are the highest-stakes blocks on any page — everything above them is designed to bring users to this moment. A poorly designed CTA or confusing pricing table can nullify an otherwise excellent page.

Two psychological forces dominate these blocks: motivation (the user wants what you offer) and friction (anything that makes committing harder). Great conversion blocks maximize motivation signals and minimize friction points simultaneously.

### CTA Conversion Principles
1. **Clarity over cleverness** — "Start free trial" converts better than "Unleash your potential"
2. **Single primary action** — one prominent CTA per block, never equal-weight dual CTAs
3. **Reduce perceived risk** — "No credit card required", "Cancel anytime", money-back guarantee
4. **Create urgency ethically** — limited-time offers with real deadlines, not fake countdown timers
5. **Match CTA to intent stage** — "Learn more" for awareness, "Try free" for consideration, "Buy now" for decision

### Pricing Psychology
1. **Anchor effect** — show the highest price first (right column) to make others seem reasonable
2. **Decoy effect** — the middle tier should be the best value, making it the obvious choice
3. **Price ending** — $99 vs $100 (charm pricing works, even in B2B)
4. **Annual discount framing** — "Save 20%" or "$X/month billed annually" vs monthly price
5. **Loss aversion** — "You're losing $X per month" is stronger than "Save $X per month"

---

## CTA Block Specifications

### Universal CTA Anatomy
- **Headline**: 28-40px, font-weight 700, compelling action-oriented
- **Subtext**: 16-18px, gray-600 or white/70%, supporting detail
- **Primary button**: 16-18px, padding 16px 32px, border-radius 8-12px, high contrast
- **Secondary action**: text link or ghost button, clearly subordinate
- **Trust signal**: small text — "No credit card required", "Free forever", "Cancel anytime"
- **Section padding**: 64-96px vertical, generous for breathing room

---

## CTA Variant 1: Simple CTA Banner

The most universal CTA pattern. Works everywhere.

### Layout Specs
- Centered layout, max-width 640px for text
- Headline: 32-40px, font-weight 700
- Subtext: 18px, max-width 480px
- Button: centered below text, 48px height, min-width 200px
- Background: brand color, dark gray, or gradient
- Text: white on dark/colored backgrounds
- Padding: 80-120px vertical

### Production Code (React/TSX)
```tsx
interface CTABannerProps {
  title: string;
  subtitle?: string;
  cta: { label: string; href: string };
  secondaryCta?: { label: string; href: string };
  background?: 'dark' | 'brand' | 'gradient';
}

export function CTABanner({ title, subtitle, cta, secondaryCta, background = 'dark' }: CTABannerProps) {
  const bgClasses = {
    dark: 'bg-gray-900',
    brand: 'bg-blue-600',
    gradient: 'bg-gradient-to-r from-blue-600 to-purple-600',
  };

  return (
    <section className={`${bgClasses[background]} text-white`}>
      <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-16 md:py-20 lg:py-24 text-center">
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight">{title}</h2>
        {subtitle && <p className="mt-4 text-lg text-white/70 max-w-xl mx-auto">{subtitle}</p>}
        <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
          <a href={cta.href} className="w-full sm:w-auto rounded-lg bg-white px-8 py-3.5 text-base font-semibold text-gray-900 hover:bg-gray-100 transition-colors">
            {cta.label}
          </a>
          {secondaryCta && (
            <a href={secondaryCta.href} className="text-base font-semibold text-white/80 hover:text-white transition-colors">
              {secondaryCta.label} &rarr;
            </a>
          )}
        </div>
      </div>
    </section>
  );
}
```

---

## CTA Variant 2: CTA with Email Input

Lead generation CTA with inline email capture.

### Layout Specs
- Centered or split layout
- Input + button: inline on desktop (flex row), stacked on mobile
- Input: 48-52px height, 16px font, border-radius 8px, flex-1
- Button: same height as input, min-width 140px, no flex
- Wrapper: optional white card on colored background
- Privacy note: 12px text below input ("We respect your privacy")

### Form Specifications
- Input type: email (triggers email keyboard on mobile)
- Input font-size: 16px minimum (prevents iOS zoom on focus)
- Placeholder: "Enter your email" or "you@company.com"
- Validation: HTML5 email validation + custom regex
- Error state: red border + "Please enter a valid email" below
- Success state: replace form with "Check your inbox" message
- Loading state: spinner in button, input disabled

### Production Code
```tsx
export function CTAEmailCapture({ title, subtitle, buttonText = 'Get started', privacy }: {
  title: string; subtitle?: string; buttonText?: string; privacy?: string;
}) {
  return (
    <section className="bg-blue-600">
      <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 py-16 md:py-20 lg:py-24 text-center">
        <h2 className="text-3xl sm:text-4xl font-bold text-white tracking-tight">{title}</h2>
        {subtitle && <p className="mt-4 text-lg text-blue-100 max-w-xl mx-auto">{subtitle}</p>}
        <form className="mt-8 flex flex-col sm:flex-row gap-3 max-w-md mx-auto">
          <input
            type="email"
            required
            placeholder="Enter your email"
            className="flex-1 rounded-lg px-4 py-3 text-base text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white/50"
          />
          <button type="submit" className="rounded-lg bg-gray-900 px-6 py-3 text-base font-semibold text-white hover:bg-gray-800 transition-colors whitespace-nowrap">
            {buttonText}
          </button>
        </form>
        {privacy && <p className="mt-3 text-xs text-blue-200">{privacy}</p>}
      </div>
    </section>
  );
}
```

---

## CTA Variant 3: CTA with Countdown

Urgency-driven CTA with time-limited offer.

### Layout Specs
- Countdown: 4 number boxes (days, hours, minutes, seconds)
- Number size: 36-48px, font-weight 700, monospace font
- Label below each: "Days", "Hrs", "Min", "Sec" in 12px
- Box: 64-80px square, border-radius 8px, dark or brand bg
- Position: above or beside the CTA text
- Update: JavaScript setInterval every 1 second
- Expiration: show "Offer expired" or redirect when timer hits 0

### Ethics Warning
Only use countdown timers for genuine time-limited offers. Fake urgency (evergreen timers that reset) is deceptive and damages trust. If the offer is always available, do not use a countdown timer.

### Production Code
```tsx
import { useState, useEffect } from 'react';

function useCountdown(targetDate: Date) {
  const [timeLeft, setTimeLeft] = useState({ days: 0, hours: 0, minutes: 0, seconds: 0 });

  useEffect(() => {
    const tick = () => {
      const now = new Date().getTime();
      const distance = targetDate.getTime() - now;
      if (distance <= 0) { setTimeLeft({ days: 0, hours: 0, minutes: 0, seconds: 0 }); return; }
      setTimeLeft({
        days: Math.floor(distance / (1000 * 60 * 60 * 24)),
        hours: Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        minutes: Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
        seconds: Math.floor((distance % (1000 * 60)) / 1000),
      });
    };
    tick();
    const interval = setInterval(tick, 1000);
    return () => clearInterval(interval);
  }, [targetDate]);

  return timeLeft;
}

export function CTACountdown({ title, cta, targetDate }: { title: string; cta: { label: string; href: string }; targetDate: Date }) {
  const { days, hours, minutes, seconds } = useCountdown(targetDate);

  return (
    <section className="bg-gray-900 text-white py-16 md:py-20">
      <div className="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8 text-center">
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight">{title}</h2>
        <div className="mt-8 flex items-center justify-center gap-4" aria-label={`${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds remaining`}>
          {[{ value: days, label: 'Days' }, { value: hours, label: 'Hours' }, { value: minutes, label: 'Min' }, { value: seconds, label: 'Sec' }].map(({ value, label }) => (
            <div key={label} className="flex flex-col items-center">
              <div className="w-16 h-16 sm:w-20 sm:h-20 flex items-center justify-center rounded-lg bg-white/10 text-2xl sm:text-3xl font-bold font-mono">
                {String(value).padStart(2, '0')}
              </div>
              <span className="mt-2 text-xs text-gray-400 uppercase tracking-wider">{label}</span>
            </div>
          ))}
        </div>
        <a href={cta.href} className="mt-8 inline-block rounded-lg bg-white px-8 py-3.5 text-base font-semibold text-gray-900 hover:bg-gray-100 transition-colors">
          {cta.label}
        </a>
      </div>
    </section>
  );
}
```

---

## CTA Variant 4: Sticky Bottom CTA

Fixed bar at viewport bottom for persistent conversion presence.

### Layout Specs
- Fixed position: bottom 0, full width
- Height: 64-72px (desktop), 56-64px (mobile)
- Background: white with shadow-up, or brand color
- Content: text (16px) + button (aligned right or centered)
- Z-index: high (z-40 or z-50)
- Close/dismiss button: optional X in top-right
- Trigger: appears after user scrolls past the main CTA (Intersection Observer)
- Animation: slide-up from bottom (translateY 100% to 0), 300ms ease

### Mobile Considerations
- Do not cover critical UI (respect safe area inset on iOS)
- Keep compact: single line text + button
- Ensure the close button is at least 44x44px tap target
- Consider auto-dismissing after conversion

### Production Code
```tsx
import { useState, useEffect } from 'react';

export function StickyBottomCTA({ text, cta }: { text: string; cta: { label: string; href: string } }) {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => setVisible(window.scrollY > 600);
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  if (!visible) return null;

  return (
    <div className="fixed bottom-0 inset-x-0 z-40 bg-white border-t border-gray-200 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.1)] animate-slide-up">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between gap-4">
        <p className="text-sm sm:text-base font-medium text-gray-900 truncate">{text}</p>
        <a href={cta.href} className="flex-shrink-0 rounded-lg bg-blue-600 px-6 py-2.5 text-sm font-semibold text-white hover:bg-blue-500 transition-colors">
          {cta.label}
        </a>
      </div>
    </div>
  );
}
```

---

## CTA Variants 5-25: Quick Reference

### 5. CTA with Background Image
Photo background + dark overlay (60-70% opacity) + white text + button. Image: relevant to product/audience. Overlay: gradient for text readability. Same structure as Simple CTA Banner with image background.

### 6. CTA with Gradient
Gradient background (brand primary to secondary). Text: white. Button: white bg, dark text. Popular gradient angles: 135deg, 90deg. Keep gradients subtle for readability.

### 7. Dual CTA Banner
Two equal-weight paths: "For individuals" / "For teams." Side-by-side buttons or side-by-side cards. Each path has its own heading + button. Split the decision clearly. Responsive: stacked on mobile.

### 8. CTA with Testimonial
CTA section with a testimonial quote embedded. Layout: quote left/above, CTA right/below. Or: centered CTA with quote below. Combines motivation (social proof) with action (button). Very effective pre-pricing.

### 9. CTA with Stats
"Join 10,000+ users who save 5 hours per week." Large stat number + CTA button. Stats provide evidence, CTA captures the motivated. Background: dark or brand for emphasis.

### 10. Full-Width Dark CTA
Full-width dark gray or black section. Maximum contrast. Large headline. Bright CTA button. Used as a page divider before footer. Creates visual punctuation.

### 11. Minimal CTA
Text-only link, no button styling. "Ready to get started? Create your account." Understated, no visual pressure. Effective for users who resist heavy sales tactics. Works well in content-heavy pages.

### 12. CTA with Illustration
Custom illustration + text + button. Illustration: left side or above text. Adds personality and brand identity. Works for playful brands. Responsive: illustration above text on mobile.

### 13. CTA with Screenshot
Product preview image + sign-up CTA. Shows what the user gets. Image: browser frame or clean mockup. Text: benefit-oriented headline. Button: "Start free trial" or "Get started."

### 14. CTA with Video Thumbnail
Play button over video thumbnail + CTA. Click play: opens modal video. CTA beside or below. Video demonstrates the product. Effective for complex products that benefit from visual explanation.

### 15. Floating CTA Button
Fixed position button (bottom-right corner). Always visible during scroll. Typically: "Chat with us", "Get a demo", or "Sign up." Circle or rounded-rectangle shape. Z-index: high. Shadow: lg. Mobile: adjust for thumb reach.

### 16. Exit-Intent CTA
Modal triggered when cursor moves toward browser close/back. Desktop only (no mouse tracking on mobile). Content: compelling offer, email capture, or discount. Dismiss: X button and click-outside. Rate limit: show max once per session. Cookie: don't show again for 7-30 days.

### 17. Scroll-Triggered CTA
Appears after user scrolls past 50% of page. Slide-in from bottom or side. Less aggressive than exit-intent. Content: brief text + button. Dismiss: X button. Trigger: Intersection Observer on a mid-page element.

### 18. CTA with Social Proof
"Join 10,000+ users" badge above or beside CTA button. Small avatar stack (3-4 overlapping circles) + "X people signed up today." Combines social proof with action.

### 19. CTA with Form
Multi-field form: name, email, company, message. Used for "Contact sales", "Request demo", "Get a quote." Split layout: value prop left, form right. Form card: white with shadow on colored bg. Required fields marked clearly.

### 20. CTA with App Download
App Store + Google Play badges side by side. Standard badge sizes: 135x40px. Above: phone mockup or app description. QR code option: for desktop users to scan and download. Platform detection: highlight the user's platform badge.

### 21. CTA with Free Resource
"Download the free guide" + email capture. Resource preview image (book cover, PDF thumbnail). Trust signal: "Join 5,000+ subscribers." Content marketing lead magnet approach.

### 22. CTA Split
Text left (40-50%), form/button right (50-60%). Text: headline + bullet points of benefits. Right: form card or large CTA button. More detail than banner, less than full landing page.

### 23. CTA with Feature Recap
Brief 3-4 feature bullets + CTA button. Last chance to reinforce value before asking for commitment. Bullet icons: checkmarks (green). Placed before footer as final conversion block.

### 24. CTA with Guarantee
"30-day money-back guarantee" badge + CTA. Shield icon or badge graphic. Reduces perceived risk at commitment point. Text: explicit guarantee terms. Most effective for higher-priced products.

### 25. CTA with Chat
"Questions? Chat with our team" + chat bubble icon. Triggers live chat widget. Alternative: "Schedule a call" + calendar link. Personal touch reduces conversion anxiety for complex/expensive products.

---

## Pricing Block Specifications

### Universal Pricing Anatomy
- **Section header**: "Pricing", "Simple, transparent pricing", "Choose your plan"
- **Toggle** (optional): Monthly/Annual switch
- **Pricing cards**: 2-4 side by side
- **Recommended badge**: "Most Popular" or "Best Value"
- **Feature list**: checkmarks per plan
- **CTA per card**: "Start trial", "Get started", "Contact sales"
- **FAQ below** (optional): pricing-specific questions

### Card Specs
- Width: equal (1/n of container)
- Padding: 32-40px
- Border-radius: 16-24px
- Shadow: sm for standard cards, lg for highlighted card
- Highlighted card: raised (translateY -8px), colored border (2px brand), or different bg
- Price: 48-64px, font-weight 700-800
- Price period: 16px, gray-500 ("/month", "/user/month")
- Feature list: 14-16px, checkmark icon + text, 8-12px gap

---

## Pricing Variant 1: 3-Column Pricing Table

The industry standard. Three tiers: Starter, Pro, Enterprise.

### Layout Specs
- 3 equal columns, gap 24-32px
- Middle column: highlighted (recommended)
- Highlight: scale(1.02-1.05), colored border-top 4px, "Most Popular" badge
- Badge: absolute positioned, -12px top, centered, pill shape
- Card content: plan name + price + period + description + feature list + CTA button
- Feature list: 6-10 features, checkmarks, items not included have X or gray text

### Responsive Behavior
- `xl`+: 3 columns side by side
- `lg`: 3 columns, reduced padding
- `md`: stacked vertically (highlighted card first with `order: -1`)
- `sm`: full-width stacked cards

### Production Code (React/TSX)
```tsx
interface PricingTier {
  name: string;
  price: string;
  period: string;
  description: string;
  features: Array<{ text: string; included: boolean }>;
  cta: { label: string; href: string };
  highlighted?: boolean;
}

export function PricingTable({ tiers, title, subtitle }: { tiers: PricingTier[]; title: string; subtitle?: string }) {
  return (
    <section className="bg-white py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-2xl mx-auto mb-12 lg:mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-gray-900">{title}</h2>
          {subtitle && <p className="mt-4 text-lg text-gray-600">{subtitle}</p>}
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
          {tiers.map((tier, i) => (
            <div key={i} className={`relative rounded-2xl p-8 ${tier.highlighted ? 'bg-white ring-2 ring-blue-600 shadow-lg scale-[1.02]' : 'bg-white ring-1 ring-gray-200'}`}>
              {tier.highlighted && (
                <div className="absolute -top-3 left-1/2 -translate-x-1/2">
                  <span className="rounded-full bg-blue-600 px-4 py-1 text-xs font-semibold text-white">Most Popular</span>
                </div>
              )}
              <h3 className="text-lg font-semibold text-gray-900">{tier.name}</h3>
              <div className="mt-4 flex items-baseline gap-1">
                <span className="text-4xl font-bold text-gray-900">{tier.price}</span>
                <span className="text-sm text-gray-500">{tier.period}</span>
              </div>
              <p className="mt-2 text-sm text-gray-600">{tier.description}</p>
              <a href={tier.cta.href} className={`mt-6 block w-full rounded-lg py-3 text-center text-sm font-semibold transition-colors ${tier.highlighted ? 'bg-blue-600 text-white hover:bg-blue-500' : 'bg-gray-50 text-gray-900 ring-1 ring-gray-200 hover:bg-gray-100'}`}>
                {tier.cta.label}
              </a>
              <ul className="mt-8 space-y-3">
                {tier.features.map((f, j) => (
                  <li key={j} className="flex items-start gap-3 text-sm">
                    {f.included ? (
                      <svg className="h-5 w-5 flex-shrink-0 text-blue-600" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" /></svg>
                    ) : (
                      <svg className="h-5 w-5 flex-shrink-0 text-gray-300" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" /></svg>
                    )}
                    <span className={f.included ? 'text-gray-700' : 'text-gray-400'}>{f.text}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Pricing Variant 2: Pricing with Toggle

Monthly/annual billing toggle with savings indicator.

### Layout Specs
- Toggle position: centered, above pricing cards, 32-48px below section header
- Toggle type: pill switch or segmented control
- Labels: "Monthly" / "Annual" (or "Yearly")
- Savings badge: "Save 20%" next to Annual label
- Price animation: fade or number transition on toggle (200ms)
- Default: Annual selected (higher LTV for the business)

### Toggle Specifications
- Width: 200-240px
- Height: 40-48px
- Active indicator: sliding pill or background change
- Active: brand color bg, white text
- Inactive: transparent bg, gray-600 text
- Transition: 200ms ease

### Production Code
```tsx
import { useState } from 'react';

interface PricingPlan {
  name: string;
  monthlyPrice: string;
  annualPrice: string;
  period: string;
  features: string[];
  cta: { label: string; href: string };
  highlighted?: boolean;
}

export function PricingWithToggle({ plans, title }: { plans: PricingPlan[]; title: string }) {
  const [annual, setAnnual] = useState(true);

  return (
    <section className="bg-white py-16 md:py-20 lg:py-24">
      <div className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl sm:text-4xl font-bold text-center text-gray-900 mb-8">{title}</h2>
        <div className="flex items-center justify-center gap-3 mb-12">
          <span className={`text-sm font-medium ${!annual ? 'text-gray-900' : 'text-gray-500'}`}>Monthly</span>
          <button
            onClick={() => setAnnual(!annual)}
            className="relative h-7 w-12 rounded-full bg-blue-600 transition-colors"
            role="switch"
            aria-checked={annual}
            aria-label="Toggle annual billing"
          >
            <span className={`absolute top-0.5 h-6 w-6 rounded-full bg-white shadow transition-transform ${annual ? 'translate-x-5' : 'translate-x-0.5'}`} />
          </button>
          <span className={`text-sm font-medium ${annual ? 'text-gray-900' : 'text-gray-500'}`}>
            Annual <span className="text-xs text-green-600 font-semibold ml-1">Save 20%</span>
          </span>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {plans.map((plan, i) => (
            <div key={i} className={`rounded-2xl p-8 ${plan.highlighted ? 'ring-2 ring-blue-600 shadow-lg' : 'ring-1 ring-gray-200'}`}>
              <h3 className="text-lg font-semibold text-gray-900">{plan.name}</h3>
              <div className="mt-4 flex items-baseline gap-1">
                <span className="text-4xl font-bold text-gray-900">{annual ? plan.annualPrice : plan.monthlyPrice}</span>
                <span className="text-sm text-gray-500">/month</span>
              </div>
              {annual && <p className="mt-1 text-xs text-gray-500">Billed annually</p>}
              <a href={plan.cta.href} className={`mt-6 block w-full rounded-lg py-3 text-center text-sm font-semibold ${plan.highlighted ? 'bg-blue-600 text-white hover:bg-blue-500' : 'bg-gray-50 text-gray-900 ring-1 ring-gray-200 hover:bg-gray-100'} transition-colors`}>
                {plan.cta.label}
              </a>
              <ul className="mt-8 space-y-3">
                {plan.features.map((f, j) => (
                  <li key={j} className="flex items-center gap-3 text-sm text-gray-700">
                    <svg className="h-4 w-4 text-blue-600 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" /></svg>
                    {f}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## Pricing Variant 3: Pricing with Feature Matrix

Detailed comparison grid below pricing cards.

### Layout Specs
- Pricing cards above (standard 3-column)
- Feature matrix below: table format
- Columns: plans (matching card order)
- Rows: grouped by category ("Core Features", "Advanced", "Support")
- Cells: checkmark, X, text value, or "Coming soon"
- Sticky header row: plan names visible while scrolling
- Row highlight: alternate gray-50 backgrounds

### Responsive Behavior
- `xl`+: Full table
- `lg`: Horizontal scroll with sticky first column (feature names)
- `md`: Switch to accordion per plan (click plan to see its features)

---

## Pricing Variants 4-30: Quick Reference

### 4. 2-Column Pricing
Binary choice: Free vs. Pro, or Basic vs. Premium. Simpler decision. Cards: larger, more detail per card. Good for products with one clear upgrade path.

### 5. 4-Column Pricing
Four tiers: Free, Starter, Pro, Enterprise. Use only when tiers are genuinely distinct. Risk: choice paralysis. Mitigation: clear "Most Popular" on one tier.

### 6. Pricing with Slider
Usage-based pricing. Slider input: controls quantity (users, API calls, storage). Price updates in real-time as slider moves. Display: large price number + unit breakdown. Good for: infrastructure, API products, metered services.

### 7. Pricing with Enterprise CTA
Top-tier card: no price displayed. Instead: "Let's talk" or "Contact sales." Card content: enterprise features list + "Custom pricing" + contact button. Often includes: SSO, SLA, custom integrations, dedicated support.

### 8. Pricing with Add-Ons
Base plan + optional add-on checkboxes. Each add-on: +$X/month. Total updates as add-ons are checked. Good for: modular products where features are genuinely optional.

### 9. Pricing with Calculator
Interactive cost estimator. Multiple inputs: team size, usage volume, features needed. Output: recommended plan + estimated monthly cost. Good for: complex pricing that depends on multiple variables.

### 10. Per-Seat Pricing
Number input or stepper for seat count. Price: per-user rate x seats. Volume discounts: show discount tiers. Display: total + per-seat breakdown. Common in: B2B SaaS, collaboration tools.

### 11. Pricing Comparison (vs. Competitor)
Your product vs. named competitor(s). Feature rows with check/X. Price row: your price vs. theirs. Conclusion: clear value advantage. Risk: legal issues — use publicly available pricing only.

### 12. Simple Price Card
Single product, single price. One card: product name + price + feature list + CTA. No comparison needed. For: single products, books, courses, one-time purchases.

### 13. Pricing with Trial CTA
Emphasize free trial over purchase. Primary CTA: "Start 14-day free trial." Secondary: "See pricing." Subtext: "No credit card required." Reduces commitment anxiety.

### 14. Pricing with FAQ
Pricing cards + FAQ accordion below. FAQ topics: billing, cancellation, upgrades, refunds, enterprise. Addresses objections immediately. Reduces support burden.

### 15. Pricing with Testimonial
Quote alongside pricing: "We saved 40% switching from [competitor]." Position: below cards or in sidebar. Validates the price/value proposition at the critical moment.

### 16. Pricing with Guarantee
"30-day money-back guarantee" prominently displayed. Shield/badge icon. Position: below pricing cards, centered. Text: explicit guarantee terms. Reduces purchase anxiety.

### 17. Pricing with Savings Badge
"Save 20%" pill badge on annual toggle. Or: "Save $120/year" specific amount on each card. Green color for positive (savings). Annual highlighted as default.

### 18. Horizontal Pricing
Plans side-by-side in a horizontal comparison table. Each column: plan details. Scroll horizontally on narrow screens. Good for many features, fewer plans.

### 19. Pricing Accordion
Expandable details per plan. Click plan name: reveals full feature list + pricing details. Compact initial view. Mobile-friendly. Good for mobile-first designs.

### 20. Usage-Based Table
Tiered usage with cost per unit at each tier. Table: usage range + price per unit. Example: 0-1K calls $0.01/call, 1K-10K $0.008/call. Include calculator.

### 21. Bundle Pricing
Package deals: individual product prices + bundle discount. Show: individual total vs. bundle price. Savings: prominent, usually a percentage or dollar amount.

### 22. Pricing with Currency Selector
Dropdown for currency: USD, EUR, GBP, etc. Prices update dynamically. Auto-detect user's locale for default. Use real exchange rates.

### 23. Pricing with Discount Code
Input field for promo/coupon codes. Validate in real-time. Show: original price + discounted price. Strikethrough on original. Green text on savings.

### 24-30. Specialized Pricing
24. **Pricing Timeline**: Prices change over time (early bird, regular, last-chance).
25. **Startup Pricing**: Special discounted tier for qualifying startups.
26. **Nonprofit Pricing**: Free or discounted tier for nonprofits.
27. **Education Pricing**: Academic discounts with .edu verification.
28. **Pricing with ROI**: Cost + projected return calculator.
29. **Pay-As-You-Go**: No commitment, per-usage billing.
30. **Freemium Comparison**: Detailed free vs. paid feature breakdown.

---

## Pricing Accessibility Requirements

1. **Screen reader announcement**: When toggle changes, announce new price ("Pro plan: $29 per month, billed annually")
2. **Feature list semantics**: Use `<ul>` with `<li>` elements, not just styled divs
3. **Checkmark/X meaning**: Don't rely on icon color alone — include text ("Included" / "Not included") for screen readers
4. **Card heading hierarchy**: Plan name as H3, under section H2
5. **CTA buttons**: Descriptive text ("Start free trial of Pro plan") not just "Get started"
6. **Price format**: Use `aria-label` to spell out price clearly ("twenty-nine dollars per month")
7. **Toggle**: `role="switch"` with `aria-checked` and descriptive `aria-label`
8. **Highlighted/recommended**: Not communicated through visual styling alone — include text badge

---

## Conversion Optimization Best Practices

1. **Reduce form fields** — every field reduces conversion by 5-10%. Ask for the minimum.
2. **Use social proof near CTAs** — "Join 10,000+ users" increases conversion 12-34%.
3. **Default to annual billing** — higher LTV, and the savings message reinforces value.
4. **Highlight one plan** — the paradox of choice is real. Guide the decision.
5. **Show the next step** — "Start trial" is better than "Submit" because users know what happens.
6. **Provide escape hatches** — "Cancel anytime", "No credit card required" reduce commitment anxiety.
7. **Use action-oriented button text** — "Get started free" beats "Sign up". Describe the benefit, not the action.
8. **Place trust badges near payment** — security seals, SSL badges, guarantee badges reduce payment friction.
9. **A/B test CTA copy** — even single-word changes can move conversion rates significantly.
10. **Show pricing early** — hiding pricing creates friction. Transparent pricing builds trust.
