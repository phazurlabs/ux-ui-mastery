# Sector Pattern Matrix — Which Patterns Matter Most by Industry

## How This Matrix Works

Not every pattern matters equally in every sector. A fintech app without trust signals is dead on arrival. A social app without a feed is not a social app. An e-commerce store without product cards has nothing to sell.

This matrix maps each sector to its **critical patterns** (must have — users expect them), **important patterns** (should have — differentiators), **nice-to-have patterns** (add polish but aren't expected), and **anti-patterns** (patterns that actively hurt in this sector).

When Sumi analyzes a user's app and identifies their sector, this matrix determines: what patterns are missing that should be there, what patterns are present that shouldn't be, and what the priority order is for upgrades.

---

## Fintech / Banking / Payments

**Users expect**: Absolute reliability, transparency, and security. Every dollar shown must be accurate. Every action must feel safe. Trust is earned per-pixel.

### Critical Patterns (must have)
| Pattern | Why It's Critical | Benchmark |
|---------|------------------|-----------|
| Data Table (2.1) | Transaction history, statements, account activity — this is the product | Stripe, Mercury |
| Stat/Metric Display (2.7) | Account balances, spending summaries, portfolio performance — the dashboard IS stat cards | Mercury, Ramp |
| Trust Signals (6.12) | SSL badges, security messaging, encryption indicators — without trust, no one enters their bank details | Stripe, Plaid |
| Form Inputs (3.1) | Account numbers, transfer amounts, payment details — must be precise, validated, and smart-filled | Stripe Elements |
| Credit Card Input (3.19) | Brand detection, formatting, CVC — specialized financial input | Stripe Elements |
| Confirmation Dialog (4.8) | "Transfer $5,000?" — every financial action must confirm with amount and recipient | Cash App, Wise |
| Loading/Progress (4.4) | "Processing payment..." — financial operations MUST show progress, never leave user uncertain | Stripe |
| Toast/Status (4.1) | "Transfer complete" — immediate, unambiguous feedback for every financial action | Mercury |
| Error Handling (2.21) | "Insufficient funds" — financial errors must be clear, specific, and suggest next steps | Stripe |
| Stepper/Wizard (1.10) | Onboarding: KYC, identity verification, account setup. Must feel professional and secure | Ramp, Mercury |

### Important Patterns (should have)
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Sparkline Charts (2.4) | Spending trends, portfolio performance, balance over time | Mercury, Robinhood |
| Search (3.2) | Find transactions by merchant, amount, date | Mercury |
| Date Range Picker (3.7) | Statement periods, report generation, tax date ranges | Stripe |
| Sidebar Navigation (1.3) | Accounts, cards, transfers, settings — organized by financial function | Mercury |
| Badge/Status (2.5) | Transaction status: Pending, Completed, Failed, Refunded | Stripe |
| Notification Center (4.3) | Large transactions, suspicious activity, payment received | Cash App |
| Export/Download | CSV, PDF statement generation | Mercury |
| Multi-Factor Auth (3.16) | OTP input for sensitive operations | All fintech |

### Anti-Patterns for Fintech
- Infinite scroll for transactions (users need pagination to find specific items)
- Gamification of spending (making money feel like a game is ethically questionable)
- Auto-advancing carousels showing financial data (user must control the pace)
- Rounded/approximate numbers (show exact cents for financial data)
- Hidden fees revealed late in checkout (trust destroyer — show all fees upfront)
- Aggressive upsell during financial operations (user is in a trust-critical mental state)
- Dark mode without sufficient contrast for financial numbers
- Motion/animation that delays showing account balances

### Visual Direction
- **Colors**: Blues, navys, whites. Green for positive (gains), red for negative (losses). Avoid loud colors.
- **Typography**: Clean, professional. Inter, SF Pro, or a humanist sans-serif. Monospace for numbers (tabular figures essential).
- **Density**: Medium-high. Financial users want information density but not clutter.
- **Motion**: Minimal and purposeful. No decorative animation. Quick, confident transitions.

---

## SaaS / Productivity / Project Management

**Users expect**: Speed, keyboard shortcuts, customizable workflows, and the ability to handle their specific complex workflow without fighting the tool.

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Sidebar Navigation (1.3) | Workspaces, projects, views — the organizational spine | Linear, Notion |
| Command Palette (1.6) | Power users expect Cmd+K. It's table stakes for 2025+ SaaS | Linear, Raycast |
| Data Table (2.1) | Lists of issues, tasks, users, records — the primary data view | Linear, Airtable |
| List/Feed (2.3) | Activity feeds, task lists, notification streams | Linear, Notion |
| Search (3.2) | Global search across all content types | Notion, Slack |
| Keyboard Shortcuts (1.25) | Every primary action must have a keyboard shortcut | Linear, Superhuman |
| Tab Navigation (1.5) | Switching between views of the same data | GitHub, Stripe |
| Toast (4.1) | Action confirmations, save success, status changes | Linear |
| Empty State (2.20) | First-run experience for every section | Notion |
| Inline Editing (3.25) | Click-to-edit for titles, descriptions, properties | Notion, Linear |

### Important Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Kanban Board (2.16) | Visual workflow management | Trello, Linear |
| Drag-and-Drop | Reordering, prioritization, assignment | Notion, Linear |
| Filter/Sort System | Complex filtering with multiple conditions | Linear, Airtable |
| Breadcrumbs (1.4) | Navigation context in deep hierarchies | Notion |
| Stat Cards (2.7) | Dashboard metrics, project health | Linear |
| Comments (7.2) | Discussion on tasks, documents, records | Linear, Notion |
| Template System | Quick start, repeatable workflows | Notion |
| Integration/Webhook UI | Connect to other tools | Zapier, Linear |

### Anti-Patterns for SaaS
- No keyboard shortcuts (forces mouse dependency — power users will leave)
- No command palette (feels dated in 2025+)
- Modal-heavy workflows (modals interrupt flow — use inline editing and side panels)
- No dark mode (developers and power users expect it)
- Saving requires clicking "Save" (auto-save is expected for document-like products)
- No undo (destructive actions without undo are unacceptable)
- Cluttered sidebar with no collapse (visual noise)
- Slow search (> 200ms for local, > 500ms for remote)

### Visual Direction
- **Colors**: Neutral bases (gray, slate) with a single brand accent. Dark mode is primary or equal.
- **Typography**: Inter, system fonts, or a clean sans-serif. Monospace for code/technical content.
- **Density**: High. SaaS power users want maximum information density. Compact modes.
- **Motion**: Fast, functional. < 150ms transitions. Spring animations for drags. No decorative animation.

---

## E-Commerce / Marketplace

**Users expect**: Beautiful product imagery, clear pricing, easy comparison, fast checkout, and transparent shipping/return policies.

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Product Card (6.1) | The fundamental unit of e-commerce — image, name, price, rating | Airbnb, Shopify |
| Product Detail Page (6.2) | Image gallery, variants, add-to-cart, reviews — the conversion page | Amazon, Shopify |
| Shopping Cart (6.3) | Cart management, quantity adjusters, subtotal | Shopify |
| Checkout Flow (6.4) | Shipping → Payment → Confirmation — the revenue moment | Stripe, Shopify |
| Search (3.2) + Faceted Filtering | Product discovery is search + category + filter | Algolia, Amazon |
| Card Grid (5.4) | Product listing layout — responsive grid of product cards | Shopify, Airbnb |
| Image Gallery (2.14) | Product photos with zoom, carousel, full-screen lightbox | Airbnb, Amazon |
| Rating/Review (3.20 + 7.4) | Star ratings, written reviews, photo reviews | Amazon, Airbnb |
| Breadcrumbs (1.4) | Category > Subcategory > Product — navigation context | Amazon, Shopify |
| Trust Signals (6.12) | Secure checkout, return policy, shipping info | All e-commerce |

### Important Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Wishlist/Save (6.15) | Bookmark for later, share lists | Airbnb, Amazon |
| Social Proof (6.6) | "2,847 people bought this", "Trending" | Amazon, Booking.com |
| Comparison Table (2.31) | Feature comparison for similar products | Amazon, Best Buy |
| Pricing with Strikethrough | Original price crossed out, sale price prominent | All e-commerce |
| Recently Viewed | Product card row of recently browsed items | Amazon |
| Upsell/Cross-sell (6.10) | "Customers also bought", "Complete the look" | Amazon, Shopify |
| Size/Variant Selector | Visual size/color/material selection with availability | Nike, Shopify |
| Shipping Estimator | Delivery date estimation in cart/product page | Amazon |

### Anti-Patterns for E-Commerce
- No guest checkout (requiring account creation to buy is the #1 cart abandonment cause)
- Hidden shipping costs revealed at checkout (the #2 abandonment cause)
- Product images that can't be zoomed
- No reviews or ratings (trust gap — buyers rely on social proof)
- Forced upsells that block checkout completion (dark pattern)
- "Continue Shopping" button more prominent than "Checkout" (friction)
- Cart that requires a page reload to update quantities
- False scarcity/urgency (fake countdown timers, fake "only 1 left")

### Visual Direction
- **Colors**: White/light backgrounds for products to pop. Accent color for CTAs (high contrast).
- **Typography**: Clean, commercial. System fonts or a geometric sans. Price styling is critical — bold, large.
- **Density**: Medium. Enough whitespace for products to breathe, but efficient use of grid space.
- **Motion**: Smooth image transitions. Add-to-cart animation. Subtle hover effects on product cards.

---

## Healthcare / Wellness / Medical

**Users expect**: Clarity, accuracy, empathy, and privacy. Medical information must be unambiguous. Wellness apps must feel calm and supportive.

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Stat/Metric Display (2.7) | Vital signs, health scores, medication dosage — numbers are life-critical | Apple Health |
| Chart/Data Visualization (2.4) | Health trends over time, lab results, activity tracking | Apple Health, Oura |
| Progress Tracking (4.4) | Treatment progress, fitness goals, medication adherence | Headspace, Oura |
| Notification System (4.3) | Medication reminders, appointment alerts, critical lab results | MyChart |
| Form Inputs (3.1) | Patient intake, symptom checkers, health questionnaires — clear, gentle, validated | Epic, Zocdoc |
| Calendar/Scheduling (2.17) | Appointment booking, medication schedules | Zocdoc, Cal.com |
| Trust Signals (6.12) | HIPAA compliance, data encryption, provider credentials | All healthcare |
| Error Prevention (form validation) | Medical data entry errors can be dangerous — validate everything | Epic |
| Accessibility (all patterns) | Healthcare must serve ALL users including elderly, disabled, cognitively impaired | WCAG AAA target |
| Empty State (2.20) | "No medications recorded" — must be supportive, not alarming | Apple Health |

### Important Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Timeline (2.19) | Medical history, treatment timeline, visit history | Epic, MyChart |
| Document Viewer (8.5) | Lab results, imaging, medical records | MyChart |
| Stepper/Wizard (1.10) | Multi-step health questionnaires, patient onboarding | Zocdoc |
| Chat/Messaging (7.1) | Patient-provider messaging, telehealth | Teladoc |
| Video Call (7.11) | Telehealth appointments | Teladoc, Doxy.me |
| Search (3.2) | Find providers, medications, conditions | Zocdoc, WebMD |

### Anti-Patterns for Healthcare
- Gamification of health metrics (can cause unhealthy obsession)
- Bright red for all warnings (anxious patients don't need more alarm)
- Small text for critical medical information (legibility is safety)
- Auto-advancing through medical questionnaires (users need time to think)
- Social features exposing health data (privacy violation)
- Complex navigation for elderly users (simplify ruthlessly)
- Jargon without plain-language alternatives
- Notification overload (alarm fatigue is a clinical safety issue)

### Visual Direction
- **Colors**: Calming blues, greens, whites. Muted palette. Red only for critical alerts. Pastel accents.
- **Typography**: Large, readable. 16px minimum body text. High contrast (AAA preferred). Simple typeface.
- **Density**: Low-medium. Generous spacing. Large touch targets (elderly users, motor impairments).
- **Motion**: Gentle, slow. Breathing animations for wellness. No sudden movements. Respect reduced motion.

---

## Social / Community / Creator

**Users expect**: Engagement, self-expression, discovery, and real-time interaction. The feed is the product.

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Feed/List (2.3) | The infinite-scroll content feed IS the product | Instagram, Twitter/X |
| Profile Page (7.7) | User identity — avatar, bio, stats, content tabs | Instagram, Twitter/X |
| Reaction/Emoji (7.4) | Quick emotional response to content — likes, hearts, reactions | Instagram, Slack |
| Comment Thread (7.2) | Discussion under posts — threading, replies, mentions | Reddit, Instagram |
| Share (7.6) | Sharing content to other platforms, DMs, or external | All social |
| Bottom Navigation (1.2) | Home, Search, Create, Notifications, Profile — the social app skeleton | Instagram, TikTok |
| Content Creation (7.13) | Post composer — text, media, audience, publish | Instagram, Twitter/X |
| Notification Center (4.3) | Likes, follows, mentions, replies — the engagement engine | All social |
| Search/Discover (3.2) | Find people, content, hashtags, topics | Instagram Explore, TikTok |
| Follow/Subscribe (7.8) | Relationship building — follow, unfollow, follower counts | All social |

### Important Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Direct Messaging (7.9) | Private conversations — real-time, media support | Instagram DMs, Discord |
| Story/Reel Format (8.7) | Ephemeral, full-screen, swipeable content | Instagram, TikTok |
| Pull-to-Refresh (4.7) | Refresh the feed for new content | All mobile social |
| Image/Video Gallery (2.14) | Media grids on profiles and in content | Instagram |
| Mention/Tag (7.5) | @mentions in posts and comments | All social |
| Avatar with Status (2.6) | Online/offline, activity indicators | Discord, Slack |
| Infinite Scroll (1.9) | Continuous content consumption | All feed-based social |
| Gesture Navigation (1.20) | Swipe between stories, swipe to like (TikTok), swipe to delete | Instagram, TikTok |

### Anti-Patterns for Social
- No content moderation tools (unsafe community)
- Infinite scroll with no "You're caught up" terminus (exploitative engagement)
- Dark patterns pushing engagement over user wellbeing (addictive design)
- No way to control who sees your content (privacy violation)
- Notifications for everything with no granular control (noise)
- Auto-playing video with sound (disruptive)
- No block/mute/report functionality (safety failure)
- Exposing precise follower counts (social comparison anxiety — some platforms are hiding these)

### Visual Direction
- **Colors**: Bold, expressive. Platform identity color (Instagram gradients, Twitter blue). Dark mode essential.
- **Typography**: System fonts for performance. Bold for names, regular for content. Efficient line height.
- **Density**: Content-first. Minimal chrome. Maximum media size. Full-bleed images/videos.
- **Motion**: Expressive. Heart animation, pull-to-refresh animation, swipe physics. Personality in motion.

---

## Education / EdTech / Learning

**Users expect**: Clear progression, encouragement, adaptive difficulty, and the feeling of making progress.

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Progress Tracking (4.4 + 9.7) | Lesson completion, course progress, skill levels — learning demands visible progress | Duolingo, Khan Academy |
| Stepper/Lesson Flow (1.10) | Sequential lesson progression with clear structure | Duolingo, Brilliant |
| Celebration/Feedback (4.12) | Completion confetti, streak celebrations, achievement unlocks | Duolingo |
| Card Navigation (1.14) | Lesson/course/topic selection as card grid | Khan Academy, Coursera |
| Empty State as Onboarding (2.20) | "Start your first lesson" — empty states are invitations | Duolingo |
| Quiz/Assessment (3.5 radio + 3.4 checkbox) | Multiple choice, true/false, matching — assessment is core | Duolingo, Brilliant |
| Gamification (9.10) | Points, streaks, leaderboards, badges — motivation system | Duolingo |
| Video Player (8.2) | Lecture videos with chaptering, speed control, captions | Khan Academy, Coursera |
| Profile/Dashboard (7.7) | Learning stats, achievements, enrolled courses | All edtech |
| Notification (4.3 + push) | Streak reminders, new lesson available, achievement earned | Duolingo |

### Anti-Patterns for Education
- Punitive error feedback ("Wrong!" without explanation)
- No way to skip ahead (forced linear progression when user already knows material)
- Gamification that rewards time-spent over learning-achieved
- Paywalls on core learning content without free tier
- Complex navigation for young learners (simplify radically for K-12)
- No offline support for learning content
- Timed assessments without accommodation options (accessibility)
- Social comparison that discourages struggling learners

### Visual Direction
- **Colors**: Bright, friendly, encouraging. Warm palette. Greens for completion. Gold for achievement. Avoid institutional gray.
- **Typography**: Rounded, friendly. Large for younger audiences. Clean for professional education.
- **Density**: Low-medium. Generous spacing. Focus on one concept at a time.
- **Motion**: Celebratory. Bounce, confetti, scaling. Character animations. High personality.

---

## Developer Tools / DevOps / API Products

**Users expect**: Speed, precision, respect for their technical expertise, and excellent documentation.

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Command Palette (1.6) | Developers expect keyboard-first interaction | VS Code, Raycast |
| Code Block (2.32) | Syntax-highlighted code with copy button — the primary content type | Stripe Docs, Vercel |
| Documentation Layout (8.1 + 5.2) | Two-column: content + code examples. Side-by-side request/response | Stripe Docs |
| Status Indicator (4.10) | Build status, deployment status, API health — green/red/yellow | Vercel, GitHub |
| Terminal/Log Output | Streaming build logs, deployment logs, error traces | Vercel, Netlify |
| API Key Management | Create, revoke, copy, scope permissions — secure and clear | Stripe, Resend |
| Search (3.2) | Docs search, API reference search, global search | Algolia-powered docs |
| Tab Navigation (1.5) | Language switcher (JavaScript/Python/Go/cURL) in docs | Stripe, Twilio |
| Data Table (2.1) | Webhook logs, API calls, error rates | Stripe, Vercel |
| Toast (4.1) | "Copied to clipboard", "Deployment started" | Vercel |

### Anti-Patterns for Developer Tools
- No dark mode (developers live in dark mode)
- Copy buttons that don't work reliably
- Documentation search that requires exact keyword matches
- No keyboard shortcuts
- Requiring GUI clicks for tasks that should be CLI-able
- Token/key management without revocation ability
- Patronizing UX copy (developers don't need hand-holding)
- Slow dashboard (developers measure in milliseconds)

### Visual Direction
- **Colors**: Dark mode primary. Monochrome with syntax-highlighting accents. Terminal green/amber aesthetic optional.
- **Typography**: Monospace for code (JetBrains Mono, Berkeley Mono, Fira Code). Sans-serif for UI (Inter, system).
- **Density**: High. Developers want information density. Compact tables, dense logs.
- **Motion**: Minimal. Fast transitions. No decorative animation. Streaming text is the "motion."

---

## Real Estate / Property / Rental

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Map + List Split View | Location-based browsing is the primary interaction | Airbnb, Zillow |
| Listing/Property Card | Photo + price + beds/baths + location | Zillow, Realtor.com |
| Photo Gallery (2.14) | Large, zoomable property photos — 20+ per listing standard | Airbnb, Zillow |
| Faceted Search/Filters | Price range, beds, baths, area, property type, amenities | Zillow, Redfin |
| Date Picker (3.7) | Move-in date, lease terms, viewing appointments | Airbnb, Zillow |
| Comparison | Side-by-side property comparison | Zillow, Redfin |

### Visual Direction
- **Colors**: Clean, trustworthy. Blue/green/white base. Professional.
- **Density**: Medium. Photos dominate. Information is structured but not overwhelming.

---

## Food / Restaurant / Delivery

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Card Grid (menu items) | Photo + name + price + description | DoorDash, Uber Eats |
| Cart/Checkout (6.3-6.4) | Item list, customization, delivery address, payment, tip | DoorDash |
| Map/Tracking | Real-time delivery tracking on a map | Uber Eats, DoorDash |
| Search + Category Filters | Cuisine type, dietary, price range, rating | All delivery apps |
| Rating/Review (for restaurants) | Star rating, delivery time, photo reviews | DoorDash, Yelp |
| Estimated Time Display | "25-35 min" prominently on listing cards | All delivery apps |

---

## Travel / Hospitality

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Date Range Picker (3.7) | Check-in/out dates — the first interaction | Airbnb, Booking.com |
| Search + Filters | Destination, dates, guests, price, amenities | Airbnb, Booking.com |
| Map + Listings | Location-based browsing | Airbnb, Google Hotels |
| Booking/Checkout Flow (6.4) | Reservation with transparent pricing | Airbnb, Booking.com |
| Photo Gallery (2.14) | Property/room photos — the selling tool | Airbnb |
| Review System | Trust through guest reviews | Airbnb, TripAdvisor |
| Calendar Availability | Which dates are available/booked | Airbnb, Cal.com |

---

## Music / Audio / Streaming

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Audio Player (8.3) | Persistent mini-player + full player | Spotify, Apple Music |
| Playlist/Queue | Song list with drag-to-reorder, remove, shuffle | Spotify |
| Search + Browse | Artist, song, album, genre, mood discovery | Spotify |
| Library/Collection | Saved songs, playlists, albums, podcasts | Spotify, Apple Music |
| Album/Artist Page (variant of 7.7) | Cover art, tracklist, bio, related artists | Spotify |
| Bottom Navigation (1.2) | Home, Search, Library — the audio app skeleton | Spotify |
| Card Grid (album/playlist cards) | Cover art + title + artist | Spotify |
| Now Playing Bar | Persistent bottom bar showing current track | Spotify |

---

## Gaming / Entertainment

### Critical Patterns
| Pattern | Why | Benchmark |
|---------|-----|-----------|
| Immersive Full-Screen | Content-first, chrome-free viewing | Netflix, Steam |
| Horizontal Scroll Rows | Category-based content discovery | Netflix |
| Hero Banner (8.8) | Featured content spotlight | Netflix, Steam |
| Continue Watching/Playing | Resume exactly where user left off | Netflix |
| Profile Switching | Multiple user profiles per account | Netflix |
| Rating/Recommendation | "Because you watched X" — personalized suggestions | Netflix, Spotify |

---

## Sector Pattern Priority Summary

For rapid reference during analysis:

| Sector | #1 Priority Pattern | #2 | #3 |
|--------|---------------------|-----|-----|
| Fintech | Trust Signals + Data Tables | Stat Display | Secure Forms |
| SaaS | Command Palette + Sidebar | Keyboard Shortcuts | Search |
| E-Commerce | Product Cards + Checkout | Search + Filters | Reviews |
| Healthcare | Accessibility + Clarity | Progress Tracking | Calm Aesthetics |
| Social | Feed + Notifications | Profile + Reactions | Creation Tools |
| Education | Progress + Gamification | Lesson Flow | Celebration |
| Dev Tools | Docs + Code Blocks | Command Palette | Status Indicators |
| Real Estate | Map + List + Photos | Filters | Comparison |
| Food/Delivery | Menu Cards + Cart | Tracking Map | Estimated Time |
| Travel | Date Picker + Search | Map + Listings | Reviews |
| Music | Audio Player + Library | Search/Browse | Playlists |
| Gaming | Immersive View + Recommendations | Continue Playing | Profiles |
