# Marketing Page Composition Recipes

Complete block-by-block composition recipes for every common marketing page type. Each recipe specifies exact block order, spacing rhythm, background alternation, responsive adjustments, and conversion optimization notes.

---

## Recipe M-01: SaaS Landing Page

The most common B2B SaaS marketing page. Optimized for signups and demo requests.

### Block Stack

```
┌─────────────────────────────────────────────────┐
│ 1. TOP NAV                                      │
│    Logo left, nav links center, CTA right        │
│    Height: 64px desktop / 56px mobile            │
│    Background: white, border-bottom: gray-100    │
│    Sticky on scroll                              │
├── spacing: 0px (hero touches nav) ──────────────┤
│ 2. HERO — Split Layout                          │
│    Left: H1 headline (48-64px) + subhead (20px) │
│         + CTA button + secondary link            │
│    Right: Product screenshot or illustration     │
│    Section padding: 96px top / 96px bottom       │
│    Background: white or subtle gradient          │
│    Max-width container: 1280px                   │
├── spacing: 0px ─────────────────────────────────┤
│ 3. SOCIAL PROOF BAR                             │
│    "Trusted by 10,000+ teams" + 5-7 logos       │
│    Section padding: 48px top / 48px bottom       │
│    Background: gray-50                           │
│    Logos: grayscale, 40px height, 48px gap       │
├── spacing: 0px ─────────────────────────────────┤
│ 4. FEATURES GRID — 3 Columns                    │
│    Icon (48px) + title (20px bold) + body (16px) │
│    3 cards in a row, 32px gap                    │
│    Section padding: 96px top / 96px bottom       │
│    Background: white                             │
│    Max-width container: 1120px                   │
├── spacing: 0px ─────────────────────────────────┤
│ 5. HOW IT WORKS — 3 Steps                       │
│    Step number + icon + title + description      │
│    Connected with line or arrow between steps    │
│    Section padding: 96px top / 96px bottom       │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 6. FEATURE SHOWCASE — Alternating Rows          │
│    Row 1: Text left, image right                 │
│    Row 2: Image left, text right                 │
│    Row 3: Text left, image right                 │
│    Each row: 64px vertical gap between rows      │
│    Section padding: 96px top / 96px bottom       │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 7. TESTIMONIALS — 3 Cards                       │
│    Quote text + avatar + name + role + company   │
│    Star rating optional                          │
│    Section padding: 96px top / 96px bottom       │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 8. PRICING TABLE — 3 Tiers                      │
│    Free / Pro / Enterprise columns               │
│    Popular tier highlighted with border + badge  │
│    Section padding: 96px top / 96px bottom       │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 9. FAQ ACCORDION                                │
│    8-12 questions, single-column, 720px max      │
│    Section padding: 96px top / 96px bottom       │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 10. FINAL CTA BANNER                            │
│    H2 headline + subtext + primary CTA button    │
│    Section padding: 96px top / 96px bottom       │
│    Background: primary-950 (dark) or gradient    │
│    Text: white                                   │
├── spacing: 0px ─────────────────────────────────┤
│ 11. FOOTER — 4 Columns                          │
│    Col 1: Logo + tagline                         │
│    Col 2-4: Link groups (Product, Company, Legal)│
│    Bottom bar: copyright + social icons          │
│    Section padding: 64px top / 32px bottom       │
│    Background: gray-950                          │
│    Text: gray-400                                │
└─────────────────────────────────────────────────┘
```

### Background Rhythm
```
white → gray-50 → white → gray-50 → white → gray-50 → white → gray-50 → primary-950 → gray-950
```

### Spacing Rhythm (Desktop)
```
Nav:           0px gap to hero
Hero:          96px / 96px
Social Proof:  48px / 48px  (tight — supporting block)
Features:      96px / 96px
How It Works:  96px / 96px
Showcase:      96px / 96px
Testimonials:  96px / 96px
Pricing:       96px / 96px
FAQ:           96px / 96px
Final CTA:     96px / 96px
Footer:        64px / 32px
```

### Responsive Adjustments

**Tablet (768-1024px):**
- Hero: stack to single column, image below text
- Features grid: 2 columns (third wraps)
- Pricing: horizontal scroll or 2+1 layout
- Section padding: reduce to 72px
- H1: reduce to 40px

**Mobile (< 768px):**
- Hero: single column, CTA full-width
- Features: single column, stacked
- How It Works: vertical timeline instead of horizontal
- Testimonials: single card with swipe/carousel
- Pricing: accordion or vertical stack
- Section padding: reduce to 48px
- H1: reduce to 32px
- Social proof logos: 2 rows of 3 or horizontal scroll

### Conversion Optimization Notes
- Hero CTA above the fold with social proof visible on scroll hint
- Repeat CTA after testimonials and as final section
- Pricing section gets anchor link from hero CTA
- FAQ reduces support load and addresses objections before CTA
- Social proof immediately after hero builds trust before features
- Dark final CTA creates contrast urgency

---

## Recipe M-02: Mobile App Landing Page

Single-page marketing site for a mobile application. Emphasizes device mockups and app store conversion.

### Block Stack

```
┌─────────────────────────────────────────────────┐
│ 1. TOP NAV                                      │
│    Logo left, minimal links, "Download" CTA      │
│    Height: 64px / 56px mobile                    │
│    Background: white, sticky                     │
├── spacing: 0px ─────────────────────────────────┤
│ 2. HERO — Centered with Device Mockup           │
│    H1 (48-56px centered) + subheading            │
│    App Store + Google Play badges (side by side) │
│    Phone mockup below or right (floating)        │
│    Section padding: 80px top / 120px bottom      │
│    Background: gradient or subtle pattern        │
├── spacing: 0px ─────────────────────────────────┤
│ 3. SOCIAL PROOF BAR                             │
│    "Featured in" + press logos (TechCrunch, etc) │
│    OR "4.8 stars from 50K+ reviews"              │
│    Section padding: 40px / 40px                  │
│    Background: white, border-y                   │
├── spacing: 0px ─────────────────────────────────┤
│ 4. FEATURE SHOWCASE — Phone + Text              │
│    3 features, each:                             │
│      Phone screenshot on one side                │
│      Feature title + description on other side   │
│      Alternating left/right placement            │
│    64px gap between each feature pair            │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 5. SCREENSHOTS CAROUSEL                         │
│    5-7 app screenshots in horizontal scroll      │
│    Phone frame around each screenshot            │
│    Dot pagination below                          │
│    Section padding: 64px / 64px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 6. STATS ROW                                    │
│    4 metrics: "1M+ downloads", "4.8 rating", etc│
│    Large numbers (48px) + labels (14px)          │
│    Section padding: 64px / 64px                  │
│    Background: primary-600 or dark               │
│    Text: white                                   │
├── spacing: 0px ─────────────────────────────────┤
│ 7. USER REVIEWS                                 │
│    3 app store-style review cards                │
│    Stars + username + date + review text         │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 8. HOW IT WORKS — 3 Steps                       │
│    Step 1: Download → Step 2: Setup → Step 3: Go│
│    Icons or mini screenshots for each step       │
│    Section padding: 96px / 96px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 9. DOWNLOAD CTA                                 │
│    H2 + subtext + App Store badges + QR code     │
│    Phone mockup as visual anchor                 │
│    Section padding: 96px / 96px                  │
│    Background: gradient matching hero            │
├── spacing: 0px ─────────────────────────────────┤
│ 10. FOOTER — Minimal                            │
│    Logo + links + social + legal                 │
│    Section padding: 48px / 32px                  │
│    Background: gray-950                          │
└─────────────────────────────────────────────────┘
```

### Background Rhythm
```
gradient → white/border → white → gray-50 → primary-600 → white → gray-50 → gradient → gray-950
```

### Responsive Adjustments

**Tablet:**
- Hero device mockup scales to 70%
- Feature showcase: maintain side-by-side but narrower mockup
- Screenshots carousel: show 3 at a time instead of 5

**Mobile:**
- Hero: stack vertically, mockup below badges
- Feature showcase: stack vertically, mockup above text
- Screenshots: single screenshot with swipe
- Stats: 2x2 grid
- App store badges: stack vertically or keep side by side at smaller size

### Conversion Optimization Notes
- App store badges appear 3 times: hero, after reviews, final CTA
- QR code in final CTA for desktop-to-mobile conversion
- Press logos and rating build credibility before feature deep dive
- Screenshots carousel lets curious users explore before committing
- Dark stats section creates visual break and emphasizes traction

---

## Recipe M-03: Startup / Launch Page

Bold, energetic page for a startup launching a new product. Focuses on vision, traction, and team credibility.

### Block Stack

```
┌─────────────────────────────────────────────────┐
│ 1. MINIMAL NAV                                  │
│    Logo left, "Join Waitlist" CTA right          │
│    No nav links (reduce distraction)             │
│    Height: 56px                                  │
│    Background: transparent over hero             │
├── spacing: 0px ─────────────────────────────────┤
│ 2. HERO — Full-Viewport Bold Statement          │
│    H1: Large (56-72px) bold headline             │
│    Subheading: 1-2 sentences (20-24px)           │
│    Primary CTA: "Join Waitlist" or "Get Early    │
│    Access" + email input                         │
│    Background: dark gradient or video            │
│    Min-height: 90vh                              │
│    Text: white                                   │
├── spacing: 0px ─────────────────────────────────┤
│ 3. PROBLEM STATEMENT                            │
│    H2: "The problem" or "{Industry} is broken"   │
│    3 pain point cards or single narrative block  │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 4. SOLUTION                                     │
│    H2: "Meet {Product}"                          │
│    Product screenshot or demo video (autoplay)   │
│    3 key differentiators below                   │
│    Section padding: 96px / 96px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 5. DEMO / VIDEO                                 │
│    Embedded video player or animated demo        │
│    16:9 ratio, max-width 960px, centered         │
│    Play button overlay                           │
│    Section padding: 64px / 64px                  │
│    Background: gray-950 (dark for video focus)   │
├── spacing: 0px ─────────────────────────────────┤
│ 6. TRACTION / SOCIAL PROOF                      │
│    Metrics: users, revenue, growth rate          │
│    Investor logos or "Backed by" section         │
│    Press mentions                                │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 7. TEAM SECTION                                 │
│    Founder photos + names + roles + links        │
│    2-4 people, centered grid                     │
│    Section padding: 96px / 96px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 8. FINAL CTA                                    │
│    H2: "Ready to {benefit}?"                     │
│    Email input + CTA button                      │
│    Waitlist count: "Join 12,000+ on the waitlist"│
│    Section padding: 120px / 120px                │
│    Background: matches hero gradient             │
│    Text: white                                   │
├── spacing: 0px ─────────────────────────────────┤
│ 9. MINIMAL FOOTER                               │
│    Logo + copyright + social links               │
│    Single row                                    │
│    Section padding: 32px / 32px                  │
│    Background: gray-950                          │
└─────────────────────────────────────────────────┘
```

### Background Rhythm
```
dark-gradient → white → gray-50 → gray-950 → white → gray-50 → dark-gradient → gray-950
```

### Responsive Adjustments

**Tablet:**
- Hero H1: reduce to 48px
- Demo video: maintain 16:9, reduce max-width
- Team: 2x2 grid

**Mobile:**
- Hero: min-height 80vh, H1 at 36-40px
- Problem cards: single column stack
- Demo video: full-width with rounded corners
- Team: single column, horizontal card layout
- Final CTA: email + button stacked vertically
- Section padding: 64px throughout

### Conversion Optimization Notes
- Single focus: everything drives toward the waitlist signup
- No pricing — this is pre-launch, build demand
- Video in dark section creates cinema-like focus
- Traction section (if available) builds FOMO
- Team section builds personal credibility for early adopters
- Waitlist counter uses social proof psychology
- Minimal nav removes distraction from conversion goal

---

## Recipe M-04: Enterprise B2B Page

Professional, trust-heavy page for enterprise software. Multiple CTAs for different buyer stages (learn more, book demo, contact sales).

### Block Stack

```
┌─────────────────────────────────────────────────┐
│ 1. TOP NAV WITH MEGA MENU                       │
│    Logo + Products dropdown + Solutions dropdown │
│    Resources + Pricing + "Contact Sales" CTA     │
│    Height: 72px                                  │
│    Background: white, border-bottom, sticky      │
├── spacing: 0px ─────────────────────────────────┤
│ 2. HERO — Professional Split                    │
│    Left: H1 (40-48px) + subheading (18px)       │
│    Two CTAs: "Book a Demo" (primary) +           │
│    "Watch Overview" (secondary/ghost)            │
│    Right: Product screenshot (high-quality)      │
│    Section padding: 80px / 80px                  │
│    Background: white or very subtle gradient     │
├── spacing: 0px ─────────────────────────────────┤
│ 3. CLIENT LOGOS BAR                             │
│    "Trusted by Fortune 500 companies"            │
│    8-12 enterprise logos, grayscale              │
│    Section padding: 48px / 48px                  │
│    Background: gray-50, border-y                 │
├── spacing: 0px ─────────────────────────────────┤
│ 4. TRUST BADGES ROW                             │
│    SOC 2 Type II + HIPAA + GDPR + ISO 27001     │
│    Badge icons in a row with labels              │
│    Section padding: 32px / 32px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 5. CAPABILITIES — Alternating Rows              │
│    4-6 features, each:                           │
│      H3 title + paragraph + bullet points        │
│      Product screenshot on alternating side       │
│    64px gap between rows                         │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 6. CASE STUDIES — 3 Cards                       │
│    Company logo + challenge + result + metric    │
│    "Read Case Study" link on each                │
│    Section padding: 96px / 96px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 7. ROI / IMPACT METRICS                         │
│    4 large numbers with descriptions             │
│    "3x faster deployment", "60% cost reduction"  │
│    Section padding: 80px / 80px                  │
│    Background: primary-950 (dark)                │
│    Text: white                                   │
├── spacing: 0px ─────────────────────────────────┤
│ 8. INTEGRATION GRID                             │
│    "Integrates with your stack"                  │
│    Logo grid of 12-20 integrations               │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 9. ENTERPRISE TESTIMONIALS                      │
│    2-3 quotes from C-suite / VP level            │
│    Company logo + name + title + photo           │
│    Section padding: 96px / 96px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 10. CTA — DUAL ACTION                           │
│    "Ready to transform your {domain}?"           │
│    "Book a Demo" + "Contact Sales"               │
│    Optional: "Or call us at..." phone number     │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 11. FAQ ACCORDION                               │
│    Enterprise-focused: security, compliance,     │
│    implementation, SLAs, support tiers           │
│    Section padding: 96px / 96px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 12. FOOTER — 5 Columns with Compliance          │
│    Products, Solutions, Resources, Company, Legal│
│    Bottom: compliance badges + certifications    │
│    Section padding: 64px / 32px                  │
│    Background: gray-950                          │
└─────────────────────────────────────────────────┘
```

### Background Rhythm
```
white → gray-50 → white → white → gray-50 → primary-950 → white → gray-50 → white → gray-50 → gray-950
```

### Responsive Adjustments

**Tablet:**
- Mega menu collapses to hamburger
- Hero: maintain split if space allows, otherwise stack
- Case studies: 2 columns + 1 (or horizontal scroll)
- Integration grid: reduce to 3 columns
- Section padding: 72px

**Mobile:**
- Hero: stacked, screenshot below CTAs
- Client logos: horizontal scroll
- Trust badges: 2x2 grid
- Capabilities: stacked, images above text
- Case studies: vertical stack with cards
- Integration grid: 4x3 or scrollable
- Section padding: 48px

### Conversion Optimization Notes
- Multiple CTA types for different buyer stages
- Trust badges early — enterprise buyers need security assurance first
- Case studies with metrics (not just quotes) — enterprise buyers need proof
- ROI section in dark background creates focal point for decision-makers
- Phone number option in CTA — enterprise buyers often want to talk
- FAQ addresses enterprise-specific objections (implementation time, SLAs)
- Integration grid reduces "will it work with our stack" objection

---

## Recipe M-05: E-commerce Product Page

Product detail page for e-commerce. Optimized for add-to-cart conversion and information completeness.

### Block Stack

```
┌─────────────────────────────────────────────────┐
│ 1. E-COMMERCE NAV                               │
│    Logo + search bar + account + wishlist + cart │
│    Category mega menu below                      │
│    Height: 120px (2 rows) / 56px mobile          │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 2. BREADCRUMB                                   │
│    Home > Category > Subcategory > Product       │
│    Padding: 12px / 12px                          │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 3. PRODUCT HERO — 2 Column                      │
│    Left (55%): Image gallery                     │
│      Main image (zoomable) + thumbnail strip     │
│      Video thumbnail if available                │
│    Right (45%): Product info                     │
│      Product title (24-28px)                     │
│      Star rating + review count link             │
│      Price (32px bold) + compare-at price        │
│      Variant selectors (color, size)             │
│      Quantity selector                           │
│      "Add to Cart" button (full-width, 56px h)  │
│      "Buy Now" secondary button                  │
│      Shipping info + return policy               │
│    Section padding: 32px / 48px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 4. PRODUCT DETAILS TABS                         │
│    Tab 1: Description (rich text + specs table)  │
│    Tab 2: Specifications                         │
│    Tab 3: Shipping & Returns                     │
│    Section padding: 48px / 48px                  │
│    Background: white, border-top                 │
├── spacing: 0px ─────────────────────────────────┤
│ 5. CUSTOMER REVIEWS                             │
│    Summary: average rating + distribution bars   │
│    Filter by rating                              │
│    Review cards: stars + text + photos + helpful │
│    "Write a Review" CTA                          │
│    Section padding: 64px / 64px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 6. RELATED PRODUCTS                             │
│    "You might also like" — 4-product carousel   │
│    Product card: image + title + price + rating  │
│    Section padding: 64px / 64px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 7. RECENTLY VIEWED                              │
│    Horizontal scroll of recently viewed products │
│    Section padding: 48px / 48px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 8. FOOTER — E-commerce                          │
│    Newsletter signup                             │
│    4 columns: Shop, Help, About, Connect         │
│    Payment icons + trust badges                  │
│    Section padding: 64px / 32px                  │
│    Background: gray-950                          │
└─────────────────────────────────────────────────┘
```

### Background Rhythm
```
white → gray-50 → white → white → gray-50 → white → gray-50 → gray-950
```

### Responsive Adjustments

**Tablet:**
- Product hero: maintain 2-column but 50/50 split
- Image gallery: smaller thumbnails
- Related products: 3 visible

**Mobile:**
- Product hero: single column, gallery on top (swipeable), info below
- Add to Cart: sticky bottom bar (always visible)
- Tabs: accordion instead of tabs
- Reviews: collapsed, show 2 with "View All"
- Related products: horizontal scroll, 2 visible
- Recently viewed: horizontal scroll

### Conversion Optimization Notes
- Add to Cart button always visible (sticky on mobile)
- Star rating near price — social proof at decision point
- Variant selectors ABOVE the Add to Cart button
- Shipping info visible without clicking — reduces uncertainty
- Review photos increase trust significantly
- Related products capture visitors who aren't sold on this item
- Breadcrumbs allow easy category navigation (reduce bounce)

---

## Recipe M-06: Agency / Portfolio Page

Creative agency or freelancer portfolio. Visual-first with work samples as the primary content.

### Block Stack

```
┌─────────────────────────────────────────────────┐
│ 1. MINIMAL NAV                                  │
│    Logo left + Work / Services / About / Contact│
│    Height: 64px, transparent over hero           │
│    Text: white (over dark hero)                  │
├── spacing: 0px ─────────────────────────────────┤
│ 2. HERO — Showreel or Statement                 │
│    Option A: Autoplay video reel (muted)         │
│    Option B: Bold typography statement           │
│      "We design products people love"            │
│      H1: 64-80px, centered                       │
│    Full-viewport height (100vh)                  │
│    Background: dark overlay on video or dark bg  │
│    Scroll indicator at bottom                    │
├── spacing: 0px ─────────────────────────────────┤
│ 3. SELECTED WORK GRID                           │
│    6-12 project thumbnails                       │
│    Masonry or asymmetric grid layout             │
│    Hover: project name + category overlay        │
│    Click: opens case study                       │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 4. SERVICES                                     │
│    4-6 service categories                        │
│    Title + brief description + arrow link        │
│    Horizontal layout or stacked list             │
│    Section padding: 96px / 96px                  │
│    Background: gray-950 (dark)                   │
│    Text: white                                   │
├── spacing: 0px ─────────────────────────────────┤
│ 5. PROCESS — 4 Steps                            │
│    Discovery → Design → Build → Launch           │
│    Step number + title + short description       │
│    Horizontal with connecting line               │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 6. CLIENTS / LOGOS                              │
│    "Clients we've worked with"                   │
│    12-16 logos in a grid                         │
│    Section padding: 64px / 64px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 7. TESTIMONIALS                                 │
│    2-3 large quotes with client photos           │
│    Full-width, one at a time (carousel optional) │
│    Section padding: 120px / 120px                │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 8. CONTACT CTA                                  │
│    "Let's build something great"                 │
│    Email link (large) + contact form or          │
│    "Start a Project" button                      │
│    Section padding: 120px / 120px                │
│    Background: primary or brand accent color     │
│    Text: white                                   │
├── spacing: 0px ─────────────────────────────────┤
│ 9. FOOTER — Minimal Creative                    │
│    Studio info + social links + legal            │
│    Section padding: 48px / 32px                  │
│    Background: gray-950                          │
└─────────────────────────────────────────────────┘
```

### Background Rhythm
```
dark(hero) → white → gray-950 → white → gray-50 → white → brand-color → gray-950
```

### Responsive Adjustments

**Tablet:**
- Work grid: 2-column masonry
- Services: 2x2 grid
- Process: 2x2 grid or vertical timeline

**Mobile:**
- Hero: reduce to 80vh, smaller type (40-48px)
- Work grid: single column, large thumbnails
- Services: stacked list
- Process: vertical timeline
- Testimonials: single quote, swipeable
- Section padding: 64px

### Conversion Optimization Notes
- Work speaks loudest — put it immediately after hero
- Services section uses dark background to create visual separation from portfolio
- Process section reduces "what's it like to work with you" objection
- Large testimonials with real photos build trust
- Contact CTA uses emotional language, not transactional
- Minimal UI chrome — let the work be the design

---

## Recipe M-07: Event / Conference Page

Event marketing page with registration focus. Time-sensitive with speakers and schedule as key content.

### Block Stack

```
┌─────────────────────────────────────────────────┐
│ 1. EVENT NAV                                    │
│    Event logo + Speakers / Schedule / Venue /   │
│    Sponsors + "Register" CTA                     │
│    Height: 64px, sticky                          │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 2. HERO — Event Announcement                    │
│    Event name (48-64px)                          │
│    Date + Location prominently displayed         │
│    Countdown timer (days/hours/min/sec)          │
│    "Register Now" CTA + price or "Free"          │
│    Background: event brand gradient or image     │
│    Min-height: 80vh                              │
│    Text: white                                   │
├── spacing: 0px ─────────────────────────────────┤
│ 3. EVENT HIGHLIGHTS                             │
│    3-4 key selling points                        │
│    "200+ Speakers" / "3 Days" / "50 Workshops"  │
│    Icon + number + label format                  │
│    Section padding: 48px / 48px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 4. FEATURED SPEAKERS                            │
│    6-12 speaker cards                            │
│    Photo (circle) + name + title + company       │
│    3-4 per row                                   │
│    "View All Speakers" link                      │
│    Section padding: 96px / 96px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 5. SCHEDULE / AGENDA                            │
│    Day tabs (Day 1, Day 2, Day 3)               │
│    Time + Session title + Speaker + Track tag    │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 6. VENUE                                        │
│    Venue photo + name + address                  │
│    Embedded map                                  │
│    Travel/hotel info links                       │
│    Section padding: 96px / 96px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 7. TICKET PRICING                               │
│    2-3 ticket tiers (Early Bird / Regular / VIP) │
│    Each: price + what's included list            │
│    Early bird with countdown or "X left"         │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 8. SPONSORS                                     │
│    Tier rows: Platinum → Gold → Silver           │
│    Logo size decreases with tier                 │
│    "Become a Sponsor" link                       │
│    Section padding: 64px / 64px                  │
│    Background: gray-50                           │
├── spacing: 0px ─────────────────────────────────┤
│ 9. FAQ                                          │
│    Event logistics: refunds, dress code,         │
│    parking, accessibility, COVID policy           │
│    Section padding: 96px / 96px                  │
│    Background: white                             │
├── spacing: 0px ─────────────────────────────────┤
│ 10. REGISTER CTA                                │
│    "Don't miss out" + countdown timer            │
│    "Register Now" large CTA button               │
│    Section padding: 120px / 120px                │
│    Background: event brand gradient              │
│    Text: white                                   │
├── spacing: 0px ─────────────────────────────────┤
│ 11. FOOTER                                      │
│    Event organizer info + contact + social       │
│    Past event links                              │
│    Section padding: 48px / 32px                  │
│    Background: gray-950                          │
└─────────────────────────────────────────────────┘
```

### Background Rhythm
```
brand-gradient → white → gray-50 → white → gray-50 → white → gray-50 → white → brand-gradient → gray-950
```

### Responsive Adjustments

**Tablet:**
- Speaker grid: 3 per row
- Schedule: simplified view with expandable sessions
- Ticket tiers: horizontal scroll or stacked

**Mobile:**
- Hero: reduce to 70vh, countdown timer smaller
- Speakers: 2 per row or horizontal scroll
- Schedule: single column, grouped by time slot
- Venue: map below info
- Ticket pricing: stacked cards
- Sponsors: smaller logos, more compact tiers
- Section padding: 48px

### Conversion Optimization Notes
- Countdown timer creates urgency in hero AND final CTA
- Speaker lineup is the #1 draw — feature it prominently
- Schedule proves content depth and helps attendees plan
- Tiered pricing with "Early Bird" drives early registrations
- "X spots left" or "Early bird ends in..." creates scarcity
- Register CTA repeats: hero + after pricing + final section
- Sticky nav with "Register" always accessible
