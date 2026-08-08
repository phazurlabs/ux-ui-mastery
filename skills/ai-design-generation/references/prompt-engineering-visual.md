# Prompt Engineering for Visual Design Generation

This reference covers how to write effective prompts for AI-powered design generation. Prompt quality is the single biggest factor in generation quality — a well-structured prompt with design intelligence produces dramatically better output than a vague description.

---

## Universal Prompt Anatomy for UI Generation

Every generation prompt should include these sections, adapted for the specific tool:

```
[SUBJECT]:      What screen/component to generate
[PLATFORM]:     Target platform (iOS 26, Android/Material 3, web)
[STYLE]:        Visual style description (mood, references, aesthetic)
[TOKENS]:       Specific design token values (colors, fonts, spacing)
[CONTENT]:      Real or realistic content (never lorem ipsum)
[STATES]:       Which states to show (default, hover, error, loading, empty)
[CONSTRAINTS]:  What NOT to include (negative prompt)
[QUALITY]:      Fidelity level (wireframe, mockup, high-fidelity, production)
[REFERENCE]:    Products to reference style from ("in the style of Linear")
```

Not every section is required for every prompt, but including more sections produces more accurate output. The minimum viable prompt includes SUBJECT, PLATFORM, and STYLE.

---

## Platform-Specific Prompt Strategies

### iOS (iOS 26 / Liquid Glass)

When generating for iOS, include these platform signals:

**Must-include keywords:**
- "iOS 26 Liquid Glass design language" (for modern apps)
- "SF Pro font family" (San Francisco is the system font)
- "SF Symbols for icons" (Apple's icon system)
- "44pt minimum touch targets" (Apple HIG requirement)
- "Dynamic Island safe area" (top of screen)
- "Tab bar navigation at bottom" (standard iOS nav pattern)
- "Large title navigation bar" (standard iOS header pattern)

**Example iOS prompt prefix:**
```
iOS 26 mobile app screen, Liquid Glass design language.
SF Pro font family. SF Symbols for all icons.
Standard iOS navigation with large title header and tab bar.
44pt minimum touch targets. Safe areas respected for Dynamic Island
and home indicator. Light mode with system background colors.
```

**Common iOS screen conventions to specify:**
- Navigation: large title collapsing to small title on scroll
- Lists: grouped inset style with rounded corners
- Actions: trailing swipe actions, context menus on long press
- Modals: sheet presentation (half-sheet, full-sheet)
- Colors: system colors that adapt to light/dark mode

### Android (Material 3 Expressive)

**Must-include keywords:**
- "Material 3 Expressive design" (latest Material version)
- "Roboto or Google Sans font" (system fonts)
- "Material Symbols for icons" (Google's icon system)
- "48dp minimum touch targets" (Material guideline)
- "Dynamic Color / Material You" (color system)
- "Canonical layouts" (for tablets and foldables)

**Example Android prompt prefix:**
```
Android app screen, Material 3 Expressive design language.
Google Sans font family. Material Symbols outlined icons.
48dp minimum touch targets. Material You Dynamic Color with
primary seed color #6366F1. Navigation bar at bottom with
3-5 destinations. Top app bar with centered title.
Light theme with surface container hierarchy.
```

**Common Android conventions to specify:**
- Navigation: bottom navigation bar (3-5 items), navigation rail (tablets)
- FAB: floating action button for primary action
- Cards: elevated or filled cards with rounded corners (16dp radius)
- Sheets: bottom sheet for secondary content
- Chips: filter chips, input chips, suggestion chips

### Web (Responsive)

**Must-include keywords:**
- Viewport widths: "desktop 1440px", "tablet 768px", "mobile 375px"
- Layout: "CSS Grid", "12-column grid", "max-width 1200px centered"
- Navigation: "sticky header", "hamburger menu on mobile"
- Hover states: "hover effects on interactive elements" (web-only)
- Typography: specific font stack with fallbacks

**Example web prompt prefix:**
```
Responsive web application, desktop view at 1440px viewport width.
12-column CSS Grid layout, max-width 1200px centered, 24px gutters.
Inter font family (400, 500, 600, 700 weights).
Sticky header navigation with logo left, nav links center,
user menu right. Hover states on all interactive elements.
8px base spacing grid. Light theme with subtle shadows for depth.
```

**Web-specific considerations:**
- Specify breakpoint behavior (what changes at tablet/mobile)
- Include cursor states (pointer on clickable, text on inputs)
- Specify scroll behavior (sticky elements, infinite scroll vs. pagination)
- Include focus states for keyboard navigation
- Specify link styles (underline, color, hover effect)

---

## Stitch-Specific Prompting

Stitch generates HTML/CSS from text descriptions. Its prompts benefit from explicit structural detail.

### Design Context First
Always extract or provide design context before generating:
```
Design context:
- Primary color: #6366F1 (indigo)
- Secondary color: #EC4899 (pink)
- Surface color: #FFFFFF
- Surface elevated: #F8FAFC
- Text primary: #0F172A
- Text secondary: #64748B
- Font: Inter, system-ui fallback
- Border radius: 8px (small), 12px (medium), 16px (large)
- Spacing: 8px grid (8, 16, 24, 32, 48)
- Shadows: 0 1px 3px rgba(0,0,0,0.1) (sm), 0 4px 6px rgba(0,0,0,0.1) (md)
```

### Structural Specification
Be explicit about layout structure:
```
Layout:
- Full-width header, 64px height, white background, bottom border 1px #E2E8F0
- Left sidebar, 256px width, white background, right border
- Main content area, remaining width, #F8FAFC background
- Content padded 32px on all sides
- Cards in 3-column grid, 24px gap
```

### Complete Stitch Prompt Example — Fintech Dashboard
```
Generate a fintech dashboard screen for a personal banking app.

Platform: Web, responsive, dark theme.
Style: Clean, data-dense, professional. In the style of Mercury bank.

Layout:
- 12-column grid, max-width 1440px
- Left sidebar navigation, 240px width, dark surface #111318
- Main content area, remaining width, surface #0C0D12
- Content padding: 32px

Header:
- Inside main content area, not full-width
- Greeting: "Good morning, Sarah" with current date
- Right side: notification bell icon, user avatar (SM, circle)

Sidebar navigation:
- Logo at top (32px height placeholder)
- Navigation items: Dashboard (active), Accounts, Transfers, Cards, Investments, Settings
- Each item: icon left, label right, 48px height, 16px padding
- Active item: #6366F1 background with white text
- Inactive: #9CA3AF text

Main content:
- Account balance card: large number $12,847.32, "Personal Checking" subtitle, "+2.4% from last month" in green
- Quick actions row: Send, Request, Pay Bills, More — circular icon buttons with labels
- Recent transactions list: 5 items, each with merchant icon, merchant name, category tag, date, amount
  - Spotify: -$9.99, Entertainment, Mar 6
  - Whole Foods: -$67.43, Groceries, Mar 5
  - Transfer from John: +$250.00, Income, Mar 5
  - Amazon: -$34.99, Shopping, Mar 4
  - Electric bill: -$142.00, Utilities, Mar 3
- Spending breakdown: horizontal bar chart showing category spending

Colors:
- Primary: #6366F1 (indigo)
- Success: #10B981 (green, for positive amounts)
- Danger: #EF4444 (red, for alerts only)
- Surface: #0C0D12
- Surface elevated: #111318
- Text primary: #E2E8F0
- Text secondary: #94A3B8

Typography:
- Inter font family
- Balance amount: 36px, 700 weight
- Section headings: 18px, 600 weight
- Body text: 14px, 400 weight, 1.5 line-height
- Small text: 12px, 400 weight

Spacing: 8px base grid. 16px component padding. 24px between sections. 32px content margins.

Include: Loading skeleton state for the balance card.
Exclude: No carousels, no hero images, no decorative illustrations, no gradients.
```

---

## Image Generator Prompting (FLUX, Imagen, DALL-E)

Image generators produce raster images (PNG/JPG), not interactive HTML. Prompt strategy differs significantly from Stitch.

### For UI Screenshots
```
High-fidelity UI screenshot of a [app type] [platform] application.
[Style description]. [Color palette]. [Layout description].
Clean, sharp, pixel-perfect rendering. Professional UI design.
No watermarks, no device frames, no shadows around the UI.
```

### For Illustrations
```
[Style] illustration of [subject].
Color palette: [specific colors].
[Mood/tone description].
Flat design, clean edges, minimal detail.
Suitable for use as a [empty state / onboarding / feature highlight] illustration.
White/transparent background.
No text, no UI elements, no frames.
```

### For Icons (Recraft V3 only for SVG)
```
Minimal [outline/filled/duotone] icon depicting [subject].
[Grid size] pixel grid, [stroke width] stroke width, rounded line caps.
Single color: [hex color].
Consistent with a professional icon set.
Simple, recognizable at 16px. No detail that would be lost at small sizes.
```

### For Product Photography
```
Professional product photograph of [subject].
[Lighting description]: studio lighting / natural light / dramatic.
[Background]: white background / lifestyle setting / gradient.
[Composition]: centered / rule-of-thirds / flat lay.
[Mood]: clean and minimal / warm and inviting / bold and modern.
4K resolution, sharp focus, commercial quality.
```

### Negative Prompting
Negative prompts tell the model what to exclude. Critical for clean design output.

**Universal negative prompt for UI generation:**
```
no watermarks, no text overlays, no logos, no device frames, no drop shadows
around the UI, no 3D effects, no gradients unless specified, no stock photo
aesthetic, no clip art, no comic style, no anime style, blurry, low quality,
distorted, deformed, extra fingers, extra limbs
```

**For clean illustration negative prompts:**
```
no photorealistic elements, no complex backgrounds, no text, no UI chrome,
no device frames, no shadows, no noise, no grain, no texture
```

---

## Style Transfer Techniques

Use reference products to anchor visual style. This is one of the most effective prompting techniques.

### Single-Reference Transfer
```
"In the visual style of [Product]"
```
Examples:
- "In the visual style of Linear" — minimal, keyboard-first, subtle animations
- "In the visual style of Stripe" — clean, trustworthy, excellent typography
- "In the visual style of Notion" — content-focused, flexible, light
- "In the visual style of Vercel" — dark, developer-focused, sharp
- "In the visual style of Airbnb" — warm, photography-forward, rounded

### Multi-Reference Blending
Combine aspects from different products:
```
"A healthcare dashboard with the visual polish of Stripe,
the information density of Figma, and the color warmth of Airbnb"
```

### Aspect-Specific Reference
Reference specific aspects rather than whole products:
- "Color palette inspired by Spotify" (dark with vibrant accents)
- "Typography system similar to Medium" (serif for reading, sans for UI)
- "Spacing density of Notion" (comfortable, not cramped)
- "Icon style of Phosphor Icons" (consistent, geometric, friendly)
- "Animation approach of Linear" (subtle, fast, purposeful)
- "Card design from Apple Music" (blur, depth, rounded corners)

### Reference Strength Modifiers
- "Exactly like [Product]" — very strong match (almost clone)
- "In the style of [Product]" — strong style match
- "Inspired by [Product]" — loose influence
- "With the polish of [Product]" — quality benchmark only

---

## Design Token Injection

Convert W3C design tokens into prompt-ready descriptions.

### Token-to-Prompt Mapping

**Color tokens:**
```json
{ "color": { "primary": { "value": "#6366F1" } } }
```
Becomes: "Primary color #6366F1 (indigo), used for buttons, links, and active states"

**Typography tokens:**
```json
{ "font": { "family": { "value": "Inter" }, "size": { "body": { "value": "16px" } } } }
```
Becomes: "Inter font family, body text 16px with 1.5 line-height"

**Spacing tokens:**
```json
{ "spacing": { "base": { "value": "8px" } } }
```
Becomes: "8px base spacing grid: 8px (xs), 16px (sm), 24px (md), 32px (lg), 48px (xl)"

**Shadow tokens:**
```json
{ "shadow": { "sm": { "value": "0 1px 3px rgba(0,0,0,0.1)" } } }
```
Becomes: "Subtle shadows for elevation: small (0 1px 3px rgba(0,0,0,0.1))"

**Border radius tokens:**
```json
{ "radius": { "md": { "value": "8px" } } }
```
Becomes: "Rounded corners: 4px (small elements), 8px (cards, inputs), 16px (large containers)"

### Full Token Block for Prompts
```
Design Tokens:
- Colors: primary #6366F1, secondary #EC4899, surface #FFFFFF, surface-elevated #F8FAFC, text-primary #0F172A, text-secondary #64748B, border #E2E8F0, success #10B981, warning #F59E0B, error #EF4444
- Typography: Inter (400, 500, 600, 700), body 16px/1.5, small 14px/1.5, heading-1 32px/1.2 700, heading-2 24px/1.3 600, heading-3 18px/1.3 600
- Spacing: base 8px grid — 4px (2xs), 8px (xs), 12px (sm), 16px (md), 24px (lg), 32px (xl), 48px (2xl)
- Radius: 4px (small), 8px (medium), 12px (large), 9999px (pill)
- Shadows: sm "0 1px 2px rgba(0,0,0,0.05)", md "0 4px 6px rgba(0,0,0,0.07)", lg "0 10px 15px rgba(0,0,0,0.1)"
```

---

## Sector-Aware Prompting

Include sector keywords that trigger appropriate visual patterns and tone.

### Fintech / Banking
```
Trustworthy, precise, data-rich, numerical clarity. Clean data visualization.
Monospaced or tabular numbers for financial figures. Green for positive,
red for negative (with secondary indicators for accessibility).
Security-conscious visual language. Professional, not flashy.
```

### Healthcare / Medical
```
Clean, clinical, calming, highly accessible. Soft blues and greens.
Large text, high contrast. Generous whitespace. Clear information hierarchy.
HIPAA-compliant UI patterns (no sensitive data visible in screenshots).
Calm, trustworthy, empathetic. Medical iconography.
```

### Social / Communication
```
Vibrant, warm, content-first, engagement-focused. Avatar-heavy.
Rich media support. Real-time indicators (online status, typing).
Conversation-centric layouts. Notification patterns.
Warm colors, friendly rounded shapes, expressive.
```

### SaaS / Productivity
```
Productive, focused, keyboard-friendly, information-dense.
Sidebar navigation, command palette, keyboard shortcuts visible.
Data tables, filters, search. Neutral color palette with
accent for primary actions. Efficient, not decorative.
Dense but organized. Multi-panel layouts.
```

### E-Commerce
```
Conversion-optimized, product-forward, cart-aware.
Product photography as hero content. Clear pricing,
prominent add-to-cart buttons. Trust signals (reviews, ratings, badges).
Filterable product grids. Checkout flow optimized.
Warm, inviting, urgent without being aggressive.
```

### Education / EdTech
```
Approachable, structured, progress-oriented. Learning pathways.
Progress bars, achievement badges, streak indicators.
Content-rich but not overwhelming. Supportive, encouraging tone.
Accessible for diverse learners. Clear navigation between lessons.
```

---

## Prompt Templates for Common Screen Types

### 1. Landing Page
```
Generate a landing page for [product name], a [product description].

Sections (top to bottom):
1. Hero: headline "[headline text]", subheadline "[subheadline]", primary CTA button "[CTA text]", secondary link "[link text]". Hero image/illustration on right.
2. Social proof: logo bar of 5-6 company logos, "Trusted by [X]+ teams"
3. Features: 3-column grid, each with icon, heading, description. Features: [feature 1], [feature 2], [feature 3]
4. How it works: 3-step numbered process with illustrations
5. Testimonial: quote from [name, title, company] with headshot
6. Pricing: [pricing tiers with features]
7. CTA: repeat primary CTA with different headline
8. Footer: links organized in 4 columns, copyright, social icons

[Design tokens block]
[Platform: web, 1440px viewport]
[Style reference]
```

### 2. Dashboard
```
Generate a dashboard for [product type], showing [user role]'s key metrics.

Layout: sidebar navigation (left, 240px) + main content area.
Sidebar: logo, nav items [list items], user menu at bottom.
Main content:
- Header row: page title "Dashboard", date range picker, export button
- Metric cards row: [4 KPI cards with labels, values, trend indicators]
- Chart section: [chart type] showing [data description]
- Table section: [data table with columns: col1, col2, col3, col4]
- Activity feed: recent [activity type] items

[Design tokens block]
[Platform and style]
```

### 3. Settings Page
```
Generate a settings page for [product type].

Layout: sidebar sub-navigation (left, 200px) + settings content (right).
Sub-nav items: Profile, Account, Notifications, Billing, Security, Integrations.
Active section: [section name].

Settings content:
- Section heading: "[Section Name]"
- Form groups (each with label, input, help text):
  [List each setting with type: text input, toggle, select, radio, etc.]
- Save button at bottom (primary), Cancel button (secondary)

[Design tokens block]
[Platform and style]
```

### 4. Login / Signup
```
Generate a [login/signup] screen for [product name].

Layout: split screen — left side branding/illustration (50%), right side form (50%).
Left side: [brand color] background, product logo, tagline, abstract illustration.
Right side: white background, centered form (max-width 400px).

Form fields:
- [Login: email, password, "Remember me" checkbox, "Forgot password?" link]
- [Signup: full name, email, password, confirm password, terms checkbox]
- Primary button: "[Login/Create Account]"
- Divider: "or continue with"
- Social login buttons: Google, GitHub, Apple
- Bottom text: "[Don't have an account? Sign up / Already have an account? Log in]"

[Design tokens block]
[Platform and style]
```

### 5. Profile Page
```
Generate a user profile page for [product type].

Layout: single column, max-width 800px, centered.
Header section:
- Cover photo (full width, 200px height, gradient placeholder)
- Avatar (80px circle, overlapping cover by 40px)
- Name, title/bio, location, joined date
- Edit Profile button (if own profile) or Follow button (if other user)

Content tabs: Posts, Projects, Activity, About
Active tab: [tab name]

Tab content: [describe content for active tab]

[Design tokens block]
[Platform and style]
```

### 6. Product Detail (E-Commerce)
```
Generate a product detail page for an e-commerce [product category].

Layout: two-column on desktop — image gallery (left, 55%), product info (right, 45%).

Image gallery:
- Main image (large, 1:1 aspect ratio)
- Thumbnail strip below (4-5 thumbnails)

Product info:
- Breadcrumb: Home > [Category] > [Subcategory]
- Product name: "[Product Name]"
- Rating: [X] stars ([N] reviews)
- Price: $[price] (if sale: strikethrough original, sale price in red)
- Short description: [2-3 sentences]
- Variant selectors: [Color swatches / Size buttons / Quantity stepper]
- Add to Cart button (primary, full width)
- Buy Now button (secondary, full width)
- Shipping info: "Free shipping over $50" with truck icon
- Accordion sections: Description, Specifications, Reviews ([N])

[Design tokens block]
[Platform and style]
```

### 7. Chat / Messaging
```
Generate a messaging screen for [product type].

Layout: three-panel — conversation list (left, 300px), active chat (center), detail panel (right, 280px, collapsible).

Conversation list:
- Search bar at top
- Conversation items: avatar, name, last message preview, timestamp, unread badge
- Active conversation highlighted

Active chat:
- Header: avatar, name, online status, action buttons (call, video, info)
- Message area: alternating sent/received bubbles with timestamps
- Include: text messages, image message, link preview, emoji reaction
- Input area: text field, attachment button, emoji button, send button

Detail panel: contact info, shared media thumbnails, shared files

[Design tokens block]
[Platform and style]
```

### 8. Data Table
```
Generate a data table view for [data type] management in [product type].

Layout: full-width content area with header controls and table.

Header:
- Page title: "[Data Type]"
- Search bar (left)
- Filter button with active filter count badge
- Column visibility toggle
- Export button (CSV, PDF)
- Primary action button: "Add [Item]"

Table:
- Columns: [checkbox], [list each column with data type]
- Sample rows: [5-7 rows with realistic data]
- Row actions: overflow menu (Edit, Duplicate, Archive, Delete)
- Selected state: checkbox checked, row highlighted

Pagination: "Showing 1-25 of 142 results", page size selector, page navigation

[Design tokens block]
[Platform and style]
```

### 9. Onboarding Flow
```
Generate step [N] of [total] in an onboarding flow for [product type].

Layout: centered content, max-width 600px, progress indicator at top.

Progress: step [N] of [total], progress bar or step dots.

Content:
- Illustration at top (relevant to this step's topic)
- Heading: "[Step heading]"
- Description: "[Step description]"
- [Step-specific input: selection cards / form fields / toggle preferences]

Navigation:
- Back button (text, left)
- Skip link (text, right)
- Continue button (primary, centered or right, full width on mobile)

[Design tokens block]
[Platform and style]
```

### 10. Empty / Error State
```
Generate an [empty/error] state for [context] in [product type].

Layout: centered content, max-width 400px, vertically centered in available space.

Content:
- Illustration: [relevant illustration description, 200px max height]
- Heading: "[State heading, e.g., 'No projects yet' or 'Something went wrong']"
- Description: "[Helpful, empathetic description explaining the state and what to do]"
- Primary action: "[Button text, e.g., 'Create your first project' or 'Try again']"
- Secondary action: "[Link text, e.g., 'Learn more' or 'Go back home']"

Tone: [empathetic and helpful, not blame-placing. Guiding, not blocking.]

[Design tokens block]
[Platform and style]
```
