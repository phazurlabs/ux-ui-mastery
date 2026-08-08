---
name: UI Pattern Intelligence
description: "Comprehensive UI pattern taxonomy (200+ patterns across 10 categories), designer benchmark DNA (50+ world-class products analyzed), sector-specific pattern matrices (20+ industries), pattern matching engine for code and screenshot analysis, pattern evolution intelligence (2024-2026), and anti-pattern encyclopedia (100+ anti-patterns). Use when the user mentions: UI patterns, design patterns, component patterns, pattern matching, pattern analysis, pattern audit, pattern library, pattern recommendation, what pattern should I use, best practices, what does [product] do, how should this look, industry standard, anti-pattern, common mistakes, pattern quality, vibe code audit, upgrade my UI, make it look professional, match [product], pattern score, pattern benchmark."
---

# UI Pattern Intelligence

## Part 1: Pattern Intelligence Philosophy

### Patterns as Reusable Solutions

A UI pattern is a reusable solution to a recurring design problem within a given context. It is not a template. It is not a component. It is the distillation of collective design experience into a named, documented, repeatable approach that solves a specific user need. When a designer says "use a modal for this confirmation," they are invoking a pattern — a solution that thousands of products have validated, refined, and optimized over decades of interface design.

The concept originates with Christopher Alexander's "A Pattern Language" (1977), where he described 253 architectural patterns — from "Light on Two Sides of Every Room" to "Intimacy Gradient" — each one a proven solution to a human problem in the built environment. Alexander's insight was that good design is not invented from scratch each time; it is composed from patterns that have been tested against reality and found to work.

In UI design, this translates directly. Every interface you admire is an assembly of patterns. Stripe's dashboard is not beautiful because of a single brilliant idea. It is beautiful because every pattern — the sidebar navigation, the stat cards, the data tables, the empty states, the command palette — is executed at benchmark quality and composed into a coherent whole. Pattern intelligence is knowing what those patterns are, when to use them, and what world-class execution looks like.

### Pattern Languages and Vocabulary

A pattern language is a structured collection of patterns that work together to solve problems at multiple scales. Just as a spoken language has vocabulary, grammar, and rhetoric, a pattern language has:

- **Vocabulary** — The individual patterns (card, modal, toast, breadcrumb)
- **Grammar** — The rules for combining patterns (a modal should not contain another modal; a toast should not require user action)
- **Rhetoric** — The art of composing patterns into experiences that persuade, guide, and delight (progressive disclosure sequences, onboarding flows, conversion funnels)

A designer with pattern intelligence has fluency in this language. They do not need to reinvent navigation — they select from 20+ navigation patterns based on information architecture depth, platform conventions, and user mental models. They do not guess at feedback mechanisms — they choose between toasts, snackbars, banners, and inline messages based on severity, persistence needs, and interruption tolerance.

### Why This Matters for Vibe Coders

The gap between a vibe-coded app and a professionally designed product is pattern literacy. A vibe coder prompts "build me a dashboard" and gets a functional layout at 5/10 quality — missing states, no keyboard navigation, generic aesthetics, sector-blind patterns. A designer with pattern intelligence prompts the same thing and gets a 9/10 dashboard — because they specify exact patterns (stat cards with sparklines, sortable data tables, command palette, skeleton loading), cite benchmarks (Stripe, Mercury, Linear), and enforce quality standards (all 10 states handled, full ARIA compliance, responsive breakpoints).

This skill gives Sumi the pattern intelligence to close that gap. Given any codebase or screenshot, Sumi can:

1. **Identify** every pattern in use, mapped to a 200+ pattern taxonomy
2. **Benchmark** each pattern against what the world's best products ship
3. **Sector-fit** the pattern inventory against what is expected in the user's industry
4. **Prescribe** specific upgrades with references to benchmark products and cognitive science
5. **Assess coherence** — whether the patterns form a unified visual language or a Frankenstein of copied trends

---

## Part 2: Pattern Taxonomy (200+ Patterns by Category)

### A. Navigation Patterns (22)

1. **Top Navigation Bar** — Horizontal bar at viewport top. Logo left, links center or right. Best for shallow IA (under 7 top-level items). Benchmark: Apple, Stripe.
2. **Sidebar Navigation** — Vertical nav at left edge. Supports grouping, nesting, badges. Best for apps with deep IA. Benchmark: Linear, Notion, Figma.
3. **Bottom Tab Bar** — Fixed bar at screen bottom with 3-5 tabs. Mobile-first. iOS and Android standard. Benchmark: Instagram, Spotify, Cash App.
4. **Command Palette** — Keyboard-triggered search over all actions and navigation. Cmd+K / Ctrl+K convention. Benchmark: Linear, Raycast, VS Code, Superhuman.
5. **Breadcrumbs** — Horizontal trail showing location in hierarchy. Best for deep content trees. Benchmark: Shopify Admin, AWS Console.
6. **Tabs** — Horizontal or vertical tab set for switching between related views. Must not be used for sequential steps (use stepper instead). Benchmark: Google Material, Stripe Dashboard.
7. **Mega Menu** — Expanded dropdown exposing multiple columns of links, often with images. Best for e-commerce and content-heavy sites. Benchmark: Amazon, IKEA, Apple Store.
8. **Pagination** — Numbered page controls for discrete data sets. Preferred when users need to reference specific pages. Benchmark: Google Search.
9. **Infinite Scroll** — Content loads continuously as user scrolls. Best for feeds. Must include scroll position preservation. Benchmark: Twitter/X, Instagram.
10. **Back Button / Back Navigation** — System or in-app back affordance. Must preserve state. Critical for mobile flows.
11. **Deep Linking** — URL-addressable states within an app. Every meaningful view should have a unique URL. Benchmark: Figma, Notion.
12. **Search Navigation** — Global search as primary navigation mechanism. Works for large content libraries. Benchmark: Spotify, YouTube, Algolia.
13. **Hamburger Menu** — Three-line icon hiding navigation. Acceptable on mobile; anti-pattern on desktop where space permits visible navigation.
14. **Navigation Drawer** — Slide-out panel for navigation items. Android convention. Can be permanent, dismissible, or modal. Benchmark: Gmail (mobile).
15. **Navigation Rail** — Narrow vertical bar with icons only. Expands on hover or click. Best for compact layouts. Benchmark: Slack, Teams.
16. **Stepper / Wizard Navigation** — Sequential numbered steps. Best for multi-step processes (checkout, onboarding). Must show progress and allow back-navigation.
17. **Segmented Control** — Two to five options in a pill-shaped toggle. Best for filtering a single view. iOS native pattern. Benchmark: Apple Music.
18. **Skip Navigation** — Hidden link for keyboard/screen reader users to bypass repeated navigation. Accessibility requirement (WCAG 2.4.1).
19. **Anchor/Scroll Navigation** — In-page links that scroll to sections. Best for long-form content and documentation. Benchmark: MDN, Stripe Docs.
20. **Hub and Spoke** — Central hub screen with spokes to detail screens. Common in mobile apps with distinct feature areas. Benchmark: iOS Settings.
21. **Faceted Navigation** — Filter-based navigation combining multiple dimensions. Best for search results and catalogs. Benchmark: Airbnb, Amazon.
22. **Quick Actions / Shortcuts Bar** — Contextual action strip showing frequent operations. Reduces navigation depth. Benchmark: iOS Shortcuts, Raycast.

### B. Content Patterns (27)

1. **Card** — Bounded container for a unit of content. Supports image, title, description, actions. The most versatile content pattern. Benchmark: Pinterest, Airbnb.
2. **List Item** — Single row in a vertical list. Supports leading icon, primary text, secondary text, trailing action. Benchmark: iOS Settings, Gmail.
3. **Table Row** — Structured data row with aligned columns. Supports sorting, selection, inline editing. Benchmark: Airtable, Notion Database.
4. **Feed Item** — Social content unit with author, timestamp, content, engagement actions. Benchmark: Twitter/X, LinkedIn.
5. **Timeline Entry** — Chronological event marker on a vertical or horizontal axis. Benchmark: GitHub activity, Jira history.
6. **Grid Tile** — Square or rectangular unit in a grid layout. Best for visual content (photos, products). Benchmark: Unsplash, Dribbble.
7. **Carousel Slide** — Horizontally scrollable content unit. Must have manual controls; never auto-advance without pause. Benchmark: Netflix, App Store.
8. **Hero Section** — Large visual block at page top. Contains headline, subtext, CTA, and often an image or illustration. Benchmark: Stripe, Linear landing pages.
9. **Feature Block** — Content unit showcasing a product capability. Typically icon + heading + description. Benchmark: Vercel, Notion marketing.
10. **Testimonial** — User quote with attribution (name, role, photo). Builds social proof. Benchmark: Webflow, Stripe.
11. **Stat Counter** — Numeric value with label and optional trend indicator. Best for dashboards and landing pages. Benchmark: Stripe Dashboard, Plausible.
12. **Pricing Card** — Plan details with name, price, feature list, and CTA. Best in 2-4 card comparison layout. Benchmark: Tailwind, Vercel.
13. **Comparison Table** — Feature matrix comparing plans, products, or options. Must be responsive. Benchmark: Notion pricing.
14. **Accordion Item** — Expandable/collapsible content section. Best for FAQs and dense information. Only one should be open at a time (single-expand) or allow multi-expand depending on context.
15. **Tree View** — Hierarchical expandable list. Best for file systems, nested categories. Benchmark: VS Code Explorer, Figma Layers.
16. **Data Table** — Full-featured table with headers, rows, sorting, filtering, selection, pagination. The most complex content pattern. Benchmark: Airtable, Retool.
17. **Kanban Board** — Columnar card layout for workflow stages. Supports drag-and-drop. Benchmark: Trello, Linear, Notion.
18. **Calendar View** — Date-based grid showing events or data. Supports day, week, month views. Benchmark: Google Calendar, Cal.com.
19. **Map View** — Geographic visualization of location-based data. Supports markers, clusters, info windows. Benchmark: Airbnb, Google Maps.
20. **Media Gallery** — Grid or masonry layout of images/videos with lightbox expansion. Benchmark: Unsplash, Google Photos.
21. **Article / Long-form Content** — Structured reading layout with headings, paragraphs, images, pull quotes. Max 70-75 characters per line. Benchmark: Medium, Substack.
22. **Profile Card** — User identity display with avatar, name, role, stats, action buttons. Benchmark: GitHub, LinkedIn.
23. **Notification Item** — Alert unit with icon, message, timestamp, read/unread state. Benchmark: GitHub notifications, Slack.
24. **Changelog Entry** — Version-tagged update with date, category badge, and description. Benchmark: Linear changelog, Stripe changelog.
25. **Code Block** — Syntax-highlighted code display with copy button and optional line numbers. Benchmark: GitHub, Stripe Docs.
26. **Metric Dashboard Tile** — Combined stat + chart in a card. Shows current value, trend, and sparkline or small chart. Benchmark: Stripe, Datadog.
27. **Empty State Illustration** — Placeholder content shown when a view has no data. Must include explanation and action CTA. Benchmark: Linear, Notion.

### C. Input Patterns (26)

1. **Text Field** — Single-line text input. Supports label, placeholder, helper text, error state, character count. The foundational input pattern.
2. **Textarea** — Multi-line text input. Supports auto-resize. Best for comments, descriptions, messages.
3. **Select / Dropdown** — Single-value selection from a list. Native or custom. Custom should support search for lists over 7 items.
4. **Checkbox** — Binary toggle for non-exclusive options. Use for multi-select in forms. Must have visible checked/unchecked/indeterminate states.
5. **Radio Button** — Single selection from mutually exclusive options. Use when 2-5 options. All options should be visible (no scrolling).
6. **Toggle / Switch** — Binary on/off control for settings. Takes effect immediately (no submit required). Benchmark: iOS, Material.
7. **Slider** — Continuous or stepped value selection along a range. Must show current value. Best for volume, price range, opacity.
8. **Date Picker** — Calendar-based date selection. Supports single date, date range, and relative dates. Must allow keyboard input. Benchmark: Airbnb, Cal.com.
9. **Time Picker** — Hour/minute selection. Supports 12h and 24h formats. Can be scroll wheel (mobile) or dropdown (desktop).
10. **Color Picker** — Visual color selection with spectrum, swatches, and hex/RGB/HSL input. Benchmark: Figma, Notion.
11. **File Upload** — Drag-and-drop zone with click fallback. Must show progress, file type validation, and size limits. Benchmark: Dropbox, Vercel.
12. **Search Input** — Text field with search icon, debounced query, and results display. Supports recent searches and suggestions. Benchmark: Algolia, Spotlight.
13. **Autocomplete / Combobox** — Text input with filtered suggestion dropdown. Supports both free text and constrained selection. The modern evolution of the select dropdown.
14. **Tag Input / Token Field** — Multi-value input displayed as removable chips/tags. Best for categories, recipients, labels. Benchmark: Gmail compose, Notion tags.
15. **Rating Input** — Star, heart, or numeric rating selection. Typically 1-5 scale. Must support half values if needed.
16. **Rich Text Editor** — WYSIWYG or markdown editor with formatting toolbar. Supports headings, bold, lists, links, images. Benchmark: Notion, Linear.
17. **Code Editor** — Syntax-highlighted editor with line numbers, auto-indent, bracket matching. Benchmark: VS Code, CodeSandbox.
18. **Signature Pad** — Touch/mouse drawing surface for capturing signatures. Must support undo and clear.
19. **OTP / Verification Code Input** — 4-6 individual digit fields with auto-advance. Must support paste. Benchmark: Stripe, any 2FA flow.
20. **Phone Number Input** — Input with country code selector, formatting, and validation. Benchmark: Stripe, Cal.com.
21. **Address Input** — Multi-field or autocomplete address entry. Supports Google Places API integration. Benchmark: Shopify Checkout, Amazon.
22. **Password Input** — Text field with visibility toggle, strength indicator, and requirements checklist. Benchmark: 1Password, Stripe.
23. **Quantity Selector** — Minus/plus stepper with numeric input. Best for e-commerce cart items. Benchmark: Shopify, Amazon.
24. **Multi-Select Combobox** — Search-and-select multiple items from a large list. Displays selections as chips. Benchmark: GitHub labels, Jira.
25. **Inline Edit** — Click-to-edit text that toggles between display and input mode. Supports Enter to save, Escape to cancel. Benchmark: Notion, Airtable.
26. **Date Range Picker** — Dual-calendar selection for start and end dates. Must support presets (last 7 days, this month). Benchmark: Stripe, Mixpanel.

### D. Feedback Patterns (22)

1. **Toast** — Ephemeral message at screen edge. Auto-dismisses after 3-5 seconds. For non-critical confirmations ("Saved," "Copied"). Must stack when multiple appear.
2. **Snackbar** — Toast variant with optional action button ("Undo"). Material Design convention. Appears at bottom.
3. **Alert / Inline Message** — Persistent, dismissible message within page flow. Four severities: info, success, warning, error. Benchmark: Stripe, GitHub.
4. **Banner** — Full-width message at page or viewport top. For system-wide announcements. Must be dismissible. Benchmark: GitHub, Vercel.
5. **Progress Bar** — Determinate horizontal bar showing completion percentage. Must include numeric indicator for accessibility.
6. **Skeleton Screen** — Placeholder shapes mimicking content layout during loading. Reduces perceived wait time. The modern replacement for spinners. Benchmark: Facebook, LinkedIn.
7. **Spinner / Loading Indicator** — Indeterminate circular animation. Use only when skeleton is not feasible. Should appear after 200ms delay to avoid flicker.
8. **Empty State** — Meaningful content shown when a view has no data. Must explain why empty and provide action to populate. Benchmark: Linear, Notion.
9. **Error State** — Displayed when an operation fails. Must explain what happened, why, and what the user can do. Never show raw error codes.
10. **Success State** — Confirmation that an operation completed. Can be inline, full-page, or overlay. Include next-step guidance.
11. **Confirmation Dialog** — Modal asking user to confirm a destructive or irreversible action. Must clearly state the consequence. Red button for destructive actions.
12. **Tooltip** — Small text popup on hover/focus explaining an element. Must not contain essential information. Supports rich content in some systems.
13. **Badge** — Small count or status indicator overlaid on an icon or element. Shows unread count, notification count, or status.
14. **Status Indicator** — Colored dot or icon showing entity state (online/offline, active/inactive, healthy/degraded). Must use color + shape for accessibility.
15. **Notification Dot** — Minimal red dot indicating new, unseen content. No count, just presence. Benchmark: iPhone app icons.
16. **Progress Steps** — Numbered or labeled step indicators for multi-step processes. Shows current step, completed steps, and remaining steps.
17. **Validation Message** — Inline field-level feedback on input validity. Appears on blur or on change. Must use color + icon + text (never color alone).
18. **Shimmer Effect** — Animated gradient sweep over skeleton elements. Adds perceived activity during loading. Benchmark: Facebook, Stripe.
19. **Confetti / Celebration** — Particle animation for milestone achievements. Use sparingly. Benchmark: Stripe Atlas, Duolingo.
20. **Typing Indicator** — Animated dots showing another user is composing a message. Chat and messaging convention. Benchmark: iMessage, Slack.
21. **Optimistic Update** — Instant UI update before server confirmation, with rollback on failure. Reduces perceived latency. Benchmark: Twitter likes, Linear.
22. **Retry State** — Shown after a failed operation with a retry button. Must preserve user input. Include exponential backoff for automatic retries.

### E. Overlay Patterns (17)

1. **Modal Dialog** — Centered overlay with backdrop dimming. For focused tasks requiring user attention. Must trap focus and support Escape to close. Benchmark: Stripe, Linear.
2. **Confirmation Dialog** — Simplified modal with question, cancel, and confirm buttons. For destructive actions. The confirm button must describe the action ("Delete project," not "OK").
3. **Bottom Sheet** — Sheet sliding up from bottom of screen. Mobile pattern for contextual actions and content. Supports peek, half, and full heights. Benchmark: Apple Maps, Google Maps.
4. **Popover** — Small floating panel anchored to a trigger element. For contextual information or controls. Closes on outside click. Benchmark: Notion block menu, GitHub.
5. **Dropdown Menu** — Vertical list of actions anchored to a trigger button. Supports icons, keyboard navigation, dividers, and nested submenus.
6. **Context Menu** — Right-click or long-press triggered dropdown. Must mirror available actions without hiding unique functionality. Benchmark: Figma, VS Code.
7. **Command Palette** — Full-width search overlay for navigating and executing actions. The power-user pattern. Benchmark: Linear, Raycast, VS Code.
8. **Lightbox** — Full-viewport overlay for viewing images/media at full size. Must support gallery navigation and zoom. Benchmark: Unsplash, Medium.
9. **Drawer / Side Panel** — Panel sliding in from left or right edge. For secondary content, filters, or detail views. Can overlay or push content. Benchmark: Gmail, Jira.
10. **Sidebar Overlay** — Temporary sidebar that overlays rather than displaces main content. For detail views and inspector panels.
11. **Full-Screen Overlay** — Takes over entire viewport. For immersive experiences like media playback, onboarding, or focused editing. Benchmark: Medium editor.
12. **Action Sheet** — iOS-style bottom overlay with a list of actions. Includes cancel button. Used for contextual choices on mobile. Benchmark: iOS Share Sheet.
13. **Toast Stack** — Vertically stacked toast notifications at a viewport corner. Must limit visible count (3-5 max) and support queue management.
14. **Notification Panel** — Slide-out panel showing notification history. Supports mark-as-read, grouping, and filtering. Benchmark: GitHub, Figma.
15. **Cookie Consent Banner** — Overlay bar or modal for GDPR/privacy consent. Must support granular choices, not just "Accept All." Benchmark: Vercel, Linear.
16. **Spotlight / Feature Highlight** — Overlay that dims the page except for one highlighted element. For onboarding and feature discovery. Benchmark: Slack, Notion.
17. **Slide-Over Panel** — Compact panel that slides over content from the right. Common for quick editing or previewing records without navigating away. Benchmark: Salesforce, HubSpot.

### F. Layout Patterns (16)

1. **Holy Grail Layout** — Header + sidebar + main + sidebar + footer. The classic web application layout. Best achieved with CSS Grid.
2. **Sidebar + Content** — Fixed or collapsible sidebar with scrollable main area. The standard SaaS application layout. Benchmark: Linear, Notion.
3. **Dashboard Grid** — Card-based grid layout with stat tiles, charts, and tables. Supports responsive reflow. Benchmark: Stripe Dashboard, Vercel.
4. **Masonry Layout** — Variable-height items arranged in columns without row alignment. Best for visual content. Benchmark: Pinterest, Unsplash.
5. **Split View** — Two panes side by side with adjustable divider. Best for comparison, editing, and reference workflows. Benchmark: VS Code, Figma.
6. **Master-Detail** — List on left, detail on right. Selecting a list item updates the detail view. Best for email, messaging, and record management. Benchmark: Apple Mail, Outlook.
7. **Responsive Container** — Layout that adapts based on container width (not viewport) using container queries. The modern responsive approach.
8. **Sticky Header** — Header that remains fixed at viewport top during scroll. Must not consume excessive vertical space (max 64px). Includes scroll shadow on overlap.
9. **Floating Action Button (FAB)** — Circular button floating above content for the primary action. Material Design convention. Use only for the single most important creation action.
10. **Scroll-to-Top** — Button appearing after downward scroll to return to page top. Appears at bottom-right. Best for long content pages.
11. **Full-Bleed Layout** — Content extending to viewport edges without margins. Best for immersive visual experiences and media-heavy pages.
12. **Centered Content Layout** — Single column centered with max-width (typically 680-740px). Best for reading, forms, and focused tasks. Benchmark: Medium, Substack.
13. **Asymmetric Two-Column** — Content + sidebar with unequal widths (typically 2:1 or 3:1 ratio). Best for articles with supplementary info or settings with preview.
14. **F-Pattern Layout** — Content arranged for natural eye-scanning pattern. Primary content top-left, secondary in horizontal bands. Best for landing pages.
15. **Z-Pattern Layout** — Content following diagonal scanning pattern: top-left headline, top-right image, bottom-left features, bottom-right CTA. Best for simple landing pages.
16. **Bento Grid** — Mixed-size cards in a grid suggesting Apple's visual metaphor. Creates visual hierarchy through card size variation. Benchmark: Apple product pages, Linear.

### G. Social Patterns (16)

1. **Like / React** — Single-tap positive sentiment (heart, thumbs up) or multi-reaction picker. Must show count and animate on tap. Benchmark: Twitter heart, Slack emoji react.
2. **Comment** — Text input with author attribution, timestamp, and threading support. Must support edit, delete, and rich text.
3. **Share** — Action to distribute content via link copy, social platforms, or messaging. Must include native share sheet on mobile.
4. **Follow / Subscribe** — Toggle button to opt into updates from an entity (person, topic, project). Must show follower count.
5. **Mention (@)** — Inline user reference in text input. Triggers autocomplete dropdown of users. Creates notification for mentioned user. Benchmark: Slack, Notion.
6. **Avatar Group** — Overlapping circular avatars showing multiple users. Shows +N overflow indicator. Benchmark: GitHub, Figma.
7. **Activity Feed** — Chronological stream of actions by users. Groups related actions. Supports filtering by type. Benchmark: GitHub, Notion.
8. **Chat Bubble** — Message container with sender alignment (left for others, right for self). Supports text, media, reactions. Benchmark: iMessage, WhatsApp.
9. **Thread / Reply Chain** — Nested conversation branching from a parent message. Supports collapse, expand, and "View N replies." Benchmark: Slack threads, Reddit.
10. **Poll / Vote** — Multiple-choice question with real-time results display. Supports single and multi-select. Benchmark: Slack, Twitter/X polls.
11. **Bookmark / Save** — Persistent save action for content. Distinct from like (private vs. public). Benchmark: Twitter/X bookmarks, Instagram saved.
12. **Report / Flag** — Hidden action to report content or users for moderation. Must include reason selection and confirmation.
13. **Presence Indicator** — Green/gray dot showing user online status. Must respect "appear offline" preference. Benchmark: Slack, Discord.
14. **Typing Indicator** — Animated indicator showing who is currently composing. Real-time collaboration signal.
15. **Reaction Picker** — Emoji grid overlay for selecting reactions. Supports custom emoji and frequently used. Benchmark: Slack, Discord.
16. **User Mention List** — Overlay showing all users who interacted (liked, reacted, viewed). Benchmark: LinkedIn "who viewed."

### H. Commerce Patterns (18)

1. **Product Card** — Image, title, price, rating, and quick-add button. The atomic unit of e-commerce browsing. Benchmark: Shopify, Amazon.
2. **Shopping Cart** — Running list of selected items with quantity controls, subtotal, and checkout CTA. Supports mini-cart (dropdown) and full-page cart.
3. **Checkout Flow** — Multi-step or single-page purchase completion. Information, shipping, payment, review. Benchmark: Shopify Checkout, Stripe Checkout.
4. **Payment Form** — Card number, expiry, CVC with real-time formatting and validation. Must support autofill. Benchmark: Stripe Elements.
5. **Address Form** — Structured address entry with country-aware field ordering. Supports autocomplete. Benchmark: Shopify Checkout.
6. **Order Summary** — Running total with line items, taxes, shipping, discounts. Must update in real-time as cart changes.
7. **Wishlist / Saved Items** — Collection of saved products for future purchase. Supports move-to-cart and share. Benchmark: Amazon.
8. **Product Review** — Star rating + text review with verified purchase badge, helpfulness voting, and photo upload. Benchmark: Amazon, TripAdvisor.
9. **Quantity Selector** — Minus/plus stepper with direct numeric input. Must enforce min/max limits. Benchmark: Shopify, Amazon.
10. **Size / Variant Selector** — Visual selector for product variants (size, color, material). Out-of-stock variants should be visible but disabled. Benchmark: Nike, Shopify.
11. **Filter Panel** — Sidebar or drawer with faceted filters (price range, category, rating, brand). Must show active filter count and clear-all option.
12. **Sort Controls** — Dropdown or segmented control for result ordering (price, rating, newest, relevance). Benchmark: Amazon, Airbnb.
13. **Product Comparison** — Side-by-side feature matrix for 2-4 products. Must support add/remove products and highlight differences.
14. **Promo Code Input** — Expandable field for discount code entry with inline validation. Show savings after application.
15. **Shipping Method Selector** — Radio-style selection of delivery options with estimated dates and prices. Benchmark: Amazon, Shopify Checkout.
16. **Trust Signals** — Security badges, payment method logos, guarantee text, and review counts placed near conversion points.
17. **Recently Viewed** — Horizontal scroll of products the user has browsed. Supports up to 20 items. Benchmark: Amazon, ASOS.
18. **Upsell / Cross-sell Block** — "Customers also bought" or "Frequently bought together" recommendations. Benchmark: Amazon, Shopify.

---

## Part 3: Pattern Selection Decision Tree

Selecting the right pattern requires evaluating four dimensions in order:

### Step 1: User Goal
What is the user trying to accomplish?

- **Find something** → Search, faceted navigation, filters, command palette
- **Create something** → Form patterns, rich text editor, inline edit, wizard
- **Understand data** → Tables, charts, stat counters, dashboards, timelines
- **Make a decision** → Comparison tables, pricing cards, product cards, pros/cons
- **Complete a task** → Stepper, checkout flow, confirmation dialogs, progress indicators
- **Communicate** → Chat bubbles, comment, mention, thread, activity feed
- **Browse / explore** → Cards, grids, carousels, infinite scroll, feeds
- **Configure / manage** → Toggle switches, settings forms, master-detail, tree views

### Step 2: Context
What are the constraints of this interaction?

- **Data volume**: Few items (radio/checkbox) vs. many items (autocomplete/combobox) vs. unlimited (search + pagination)
- **Frequency**: One-time action (modal) vs. repeated action (inline, keyboard shortcut)
- **Reversibility**: Reversible (optimistic update) vs. irreversible (confirmation dialog)
- **Urgency**: Critical (alert banner) vs. informational (toast) vs. ambient (badge)
- **Complexity**: Simple (toggle) vs. moderate (date picker) vs. complex (rich text editor)

### Step 3: Platform
What platform conventions apply?

- **iOS**: Bottom tabs, action sheets, swipe gestures, segmented controls, Liquid Glass (iOS 26)
- **Android**: Navigation drawer/rail, bottom sheets, FAB, snackbars, Material 3 Expressive
- **Desktop Web**: Sidebar navigation, command palette, keyboard shortcuts, hover states, right-click menus
- **Mobile Web**: Simplified navigation, large touch targets (min 44px), reduced overlays

### Step 4: Pattern Recommendation
Cross-reference goal + context + platform to select the optimal pattern. When multiple patterns could work, prefer:

1. The platform-native pattern (reduces learning curve)
2. The pattern used by the sector benchmark (meets user expectations)
3. The simpler pattern (fewer states to manage, fewer edge cases)
4. The more accessible pattern (broader user support)

---

## Part 4: Product Benchmarks (50+)

### Tier 1: Pattern-Defining Products

1. **Stripe** — The benchmark for developer-facing dashboards. Stat cards with sparklines, sortable tables, purple-accent design system, skeleton loading, command palette. Every state handled.
2. **Linear** — The benchmark for productivity apps. Ultra-minimal sidebar nav, keyboard-first design, command palette as primary interaction, real-time sync, subtle motion.
3. **Notion** — The benchmark for block-based content tools. Every piece of content is a draggable block. Inline editing, slash commands, relational databases, template gallery.
4. **Airbnb** — The benchmark for marketplace search and discovery. Map + list split view, date range picker, faceted filters with instant preview counts, photo-first cards.
5. **Figma** — The benchmark for collaborative design tools. Multiplayer cursors, command palette, contextual toolbars, infinite canvas, layers panel, deep linking to frames.

### Tier 2: Category Leaders

6. **Vercel** — Best deployment dashboard. Minimal, high-contrast, real-time build logs, branch previews, domain management.
7. **Shopify** — Best e-commerce admin. Polaris design system, universal search, timeline for orders, extensible with apps.
8. **Mercury** — Best fintech dashboard. Banking with Stripe-tier aesthetics. Transaction tables, balance cards, team management.
9. **Cash App** — Best mobile fintech. Bold, brand-forward, simple navigation, one-tap payments, bitcoin integration.
10. **Superhuman** — Best email client UX. Keyboard-only navigation, split inbox, instant search, command palette, "Get Me To Zero."
11. **Arc Browser** — Best browser UX innovation. Sidebar tabs, spaces, command bar, split view, boosts for customization.
12. **Raycast** — Best launcher/productivity tool. Command palette as entire product, extensions ecosystem, clipboard history, snippets.
13. **Duolingo** — Best gamified learning. Streak mechanics, hearts, XP, leaderboards, character-driven micro-interactions, celebration animations.
14. **Slack** — Best team messaging. Threaded conversations, emoji reactions, channel organization, app integrations, search with filters.
15. **Discord** — Best community platform. Server/channel hierarchy, voice channels, role management, rich embeds, bot ecosystem.
16. **GitHub** — Best developer collaboration. Pull request review UX, issue tracking, actions CI/CD, codespaces, contribution graph.
17. **VS Code** — Best code editor UX. Command palette, extensions marketplace, integrated terminal, split editors, GitLens integration.
18. **Spotify** — Best music streaming UX. Personalized home, infinite scroll discovery, mini player, collaborative playlists, Wrapped campaign.
19. **Apple Music** — Best platform-native music UX. Spatial audio, lyrics sync, listen now intelligence, seamless device handoff.
20. **Netflix** — Best streaming content discovery. Row-based browsing, preview on hover, personalized recommendations, top 10 lists.

### Tier 3: Domain Specialists

21. **Airtable** — Best spreadsheet-database hybrid. Multiple views (grid, kanban, calendar, gallery), linked records, automations.
22. **Retool** — Best internal tool builder. Pre-built components, query builder, drag-and-drop layout, permission management.
23. **Cal.com** — Best scheduling UX. Clean availability picker, timezone handling, booking confirmation, calendar integration.
24. **Loom** — Best async video communication. One-click record, auto-chapters, comments on timeline, viewer analytics.
25. **Intercom** — Best customer messaging. Inbox management, chatbot flows, resolution bot, article suggestions, macro system.
26. **Framer** — Best no-code website builder. Canvas editing, component variants, CMS integration, responsive design tools.
27. **Webflow** — Best visual web development. CSS visual editor, interactions timeline, CMS collections, e-commerce.
28. **Tailwind UI** — Best component library. Professionally designed, accessible, responsive, copy-paste ready patterns.
29. **Planetscale** — Best database management UX. Branch-based schema changes, deploy requests, query insights.
30. **Railway** — Best one-click deployment. Service cards, environment management, real-time logs, usage dashboards.
31. **Plausible** — Best privacy-friendly analytics. Single-page dashboard, real-time counter, clean data tables, no cookie banners.
32. **Posthog** — Best product analytics. Feature flags, session recordings, funnels, retention charts, experimentation.
33. **Resend** — Best email API dashboard. Clean log viewer, domain management, API key handling, webhook configuration.
34. **Clerk** — Best auth UI components. Pre-built sign-in/sign-up flows, user profile, organization management.
35. **Supabase** — Best open-source BaaS dashboard. Table editor, SQL editor, auth management, storage browser, realtime inspector.
36. **Dub.co** — Best link management. Clean analytics, QR code generation, link builder, team workspaces.
37. **Craft** — Best native document editor. Block-based, beautifully native (macOS/iOS), markdown support, backlinks.
38. **Things 3** — Best task management design. Native macOS/iOS, headings as sections, today/upcoming/anytime/someday paradigm.
39. **Bear** — Best native notes app design. Minimal, markdown-first, tag-based organization, beautiful typography.
40. **1Password** — Best password manager UX. Vault organization, autofill, Watchtower security audit, family sharing.
41. **Wise** — Best international payment UX. Transparent pricing, multi-currency accounts, clear conversion flow.
42. **Revolut** — Best mobile banking super-app. Account switching, spending insights, crypto/stocks, card management.
43. **Monzo** — Best banking notification design. Real-time spending alerts, categorization, savings pots, salary sorter.
44. **TripAdvisor** — Best review aggregation. Review distribution charts, photo galleries, ranking methodology, traveler type filters.
45. **Zillow** — Best real estate search. Map-based search, saved searches, price history charts, mortgage calculator.
46. **Calendly** — Best mainstream scheduling. Simple booking page, availability rules, round-robin, team scheduling.
47. **Miro** — Best infinite canvas collaboration. Sticky notes, voting, timer, presentation mode, templates.
48. **Excalidraw** — Best hand-drawn diagramming. Whiteboard simplicity, collaborative, exportable, library of shapes.
49. **Pitch** — Best presentation design tool. Template-first, collaborative, version history, presentation analytics.
50. **Cron (now Notion Calendar)** — Best calendar redesign. Multi-account, side panel scheduling, keyboard navigation, elegant density.
51. **Warp** — Best terminal reimagination. Block-based output, AI command search, team sharing, modern text editing.
52. **Fig (now Amazon Q)** — Best CLI autocomplete. Context-aware suggestions, inline documentation, visual interface for CLI.

---

## Part 5: Anti-Pattern Encyclopedia (35+)

### Navigation Anti-Patterns

1. **Desktop Hamburger** — Hiding navigation behind a hamburger menu on desktop where ample screen space exists. Reduces discoverability by 21% (NNG). Use visible sidebar or top navigation instead.
2. **Mystery Navigation** — Icon-only navigation without labels. Users cannot reliably interpret icons alone. Always pair icons with text labels (especially on bottom tabs).
3. **Infinite Nesting** — Menus within menus within menus. If navigation exceeds 3 levels deep, the information architecture needs restructuring, not deeper menus.
4. **Broken Back Button** — Single-page apps that break browser back behavior. Every meaningful state must be URL-addressable and back-navigable.
5. **Surprise Redirect** — Links that navigate away from the current context without warning. External links should open in new tabs; destructive navigation should confirm.

### Content Anti-Patterns

6. **Auto-Advancing Carousel** — Carousels that rotate automatically. Users cannot read at forced speeds. Auto-advance hides content users never see. Let users control advancement.
7. **Infinite Scroll Without Position** — Infinite scroll that loses scroll position on back navigation. Users return to the top and must re-scroll. Preserve scroll position or use pagination.
8. **Truncation Without Access** — Text cut with "..." but no way to see the full content. Every truncation must have an expansion mechanism (tooltip, expand, detail view).
9. **Data Table Without Sort/Filter** — Presenting tabular data with no user control over ordering or visibility. Tables over 10 rows need sorting; over 20 rows need filtering.
10. **Wall of Text** — Dense, unformatted content blocks. Break into paragraphs, add headings, use bullet points, include visual breaks. Max 75 characters per line.

### Input Anti-Patterns

11. **Dropdowns for Known Values** — Using a dropdown for inputs the user already knows (birth year, country they live in). Use autocomplete/combobox so users can type directly.
12. **Calendar for Known Dates** — Forcing a date picker for dates users know by heart (birthday, anniversary). Allow direct text input with optional calendar.
13. **Required Fields Without Indication** — Forms where required fields are not marked. Mark all required fields (asterisk convention) or mark optional fields if most are required.
14. **Premature Validation** — Showing error messages before the user has finished typing. Validate on blur or on submit, not on every keystroke.
15. **Clearing Form on Error** — Resetting form fields after a submission error. This forces users to re-enter everything. Preserve all input on error.
16. **Ambiguous Toggle State** — Toggles where the label does not clarify whether it shows current state or the action it will perform. The label should describe the setting, not the action.

### Feedback Anti-Patterns

17. **Full-Page Spinner** — Blocking the entire page with a loading spinner. Use skeleton screens to show layout structure during loading. Only block specific regions that are loading.
18. **Silent Failure** — Operations that fail without any user notification. Every failure must produce visible, actionable feedback.
19. **Error Code Display** — Showing raw error codes or stack traces to end users. Translate technical errors into human language with recovery instructions.
20. **Undismissible Alerts** — Alert messages that cannot be closed or dismissed. All non-critical alerts must be dismissible. Critical alerts should provide a resolution path.
21. **Success Without Next Step** — Showing "Success!" with no guidance on what to do next. Always follow success states with a clear next action or return path.

### Layout Anti-Patterns

22. **Overstuffed Dashboard** — Showing every possible metric on a single screen. Prioritize 4-6 key metrics above the fold; provide progressive access to secondary data.
23. **False Floors** — Layouts where content exists below the fold but nothing indicates scrollability. Use partial element visibility, scroll indicators, or content teasers.
24. **Fixed Everything** — Sticky header + sticky sidebar + sticky footer consuming 40%+ of viewport. Only fix elements that need persistent access. Reclaim vertical space.
25. **Mobile Desktop** — Desktop layouts force-shrunk into mobile viewports. Responsive design requires layout transformation, not just scaling. Reorder, stack, and simplify.

### Commerce Anti-Patterns

26. **Surprise Costs** — Revealing shipping, tax, or fees only at checkout. Show total cost estimates as early as possible. Surprise costs cause 48% of cart abandonments (Baymard).
27. **Forced Account Creation** — Requiring registration before checkout. Always offer guest checkout. Account creation can happen post-purchase. Forced registration causes 26% abandonment.
28. **Hostile Dark Patterns** — Tricks to manipulate user choices: pre-checked add-ons, confusing unsubscribe flows, confirmshaming ("No, I don't want to save money"). These destroy trust and violate regulations.
29. **Hidden Unsubscribe** — Making it difficult to cancel subscriptions or unsubscribe from emails. Must be as easy to leave as to join.

### Accessibility Anti-Patterns

30. **Color-Only Feedback** — Using color alone to convey meaning (red for error, green for success). 8% of men are color-blind. Always pair color with icons, text, or patterns.
31. **Missing Focus Indicators** — Removing default browser focus outlines without providing custom alternatives. Keyboard users lose all orientation. Always provide visible focus styles.
32. **Tiny Touch Targets** — Interactive elements smaller than 44x44px on mobile. Causes miss-taps and frustration. Apple and Google both specify 44px minimum.
33. **Low Contrast Text** — Text that fails WCAG AA contrast ratios (4.5:1 for normal text, 3:1 for large text). Check every text color against its background.
34. **Keyboard Trap** — Modal or widget that captures keyboard focus without providing an escape mechanism. Focus must always be navigable and escapable.
35. **Auto-Playing Media** — Videos or audio that play automatically with sound. Startles users, disrupts screen readers, wastes data. Always default to muted or paused.

### AI/Modern Anti-Patterns

36. **AI Without Attribution** — AI-generated content presented without disclosure. Users deserve to know when content is machine-generated.
37. **Chatbot Dead End** — AI chat interfaces that cannot escalate to human support or alternative actions. Always provide escape hatches from AI interactions.
38. **Overpromising AI** — AI features marketed as more capable than they are. Set accurate expectations and show confidence levels.

---

## Part 6: Pattern Composition

### How Patterns Combine Into Screens

Individual patterns are like words; screens are sentences. A well-composed screen selects patterns that work together without redundancy or contradiction. The composition rules:

**Hierarchy Rule** — Every screen needs exactly one primary pattern (the main content area), supported by secondary patterns (navigation, feedback, actions). Two primary patterns compete for attention and create confusion.

**Density Rule** — Pattern density must match user expertise. Novice users need fewer, larger patterns with more whitespace. Expert users tolerate (and prefer) higher density with keyboard shortcuts.

**State Rule** — Every pattern on screen must handle all its states: empty, loading, partial, complete, error, disabled, hover, focus, active. Missing states create the uncanny valley of "almost professional."

**Consistency Rule** — Patterns that serve similar functions must look and behave identically. If cards are clickable in one view, they must be clickable in all views. If toasts appear bottom-right, they always appear bottom-right.

### Common Screen Compositions

**Dashboard** = Sidebar nav + stat cards (4-6) + primary data table + chart widgets + command palette
**Settings** = Sidebar nav + settings group list + form sections + toggles + save bar
**List/Detail** = Sidebar nav + filterable list + detail panel + action bar
**Onboarding** = Stepper + illustration + form fields + progress bar + skip option
**Checkout** = Stepper + address form + payment form + order summary + trust signals
**Feed** = Top nav or bottom tabs + infinite scroll feed items + compose FAB + pull-to-refresh
**Chat** = Sidebar contact list + message thread + chat bubbles + input bar + typing indicator
**Landing Page** = Hero + feature blocks + testimonials + pricing cards + CTA + footer

### Pattern Relationship Types

- **Contains**: A modal *contains* a form. A card *contains* a stat counter.
- **Triggers**: A button *triggers* a modal. A list item *triggers* a detail view.
- **Replaces**: A skeleton *replaces* content during loading. An empty state *replaces* a list when empty.
- **Accompanies**: A tooltip *accompanies* an icon. A badge *accompanies* a nav item.
- **Sequences**: A stepper *sequences* form steps. A wizard *sequences* configuration.

---

## Reference Architecture

| File | Contents | Use When |
|------|----------|----------|
| `references/pattern-taxonomy-complete.md` | 200+ UI patterns across 10 categories: Navigation, Data Display, Input & Forms, Feedback & Status, Layout & Composition, Commerce & Conversion, Social & Communication, Content & Media, Onboarding & Education, AI & Generative. Each pattern: anatomy, variants, when to use, when not to use, anti-patterns, accessibility requirements, benchmarks. | Identifying patterns in code/screenshots. Recommending patterns for a use case. Understanding pattern variants. |
| `references/designer-benchmark-dna.md` | What 50+ world-class products actually ship. Tier 1 (pattern-defining): Stripe, Linear, Notion, Airbnb, Figma. Tier 2 (category leaders): Vercel, Shopify, Mercury, Cash App, Superhuman, Arc, Raycast, Duolingo, and 15+ more. Per-product: signature patterns, design principles, pattern scores. Designer influence: Rasmus Andersson, Dieter Rams, Apple, Material Design. Scoring framework. | Benchmarking user patterns against world-class execution. Citing specific products as references. Understanding what "good" looks like for a specific pattern type. |
| `references/sector-pattern-matrix.md` | Which patterns matter most per industry. 12+ detailed sector profiles: Fintech, SaaS, E-commerce, Healthcare, Social, Education, Developer Tools, Real Estate, Food/Delivery, Travel, Music, Gaming. Per-sector: critical patterns, important patterns, anti-patterns, visual direction. Priority summary matrix. | Determining which patterns are expected for a user's sector. Flagging missing critical patterns. Identifying sector anti-patterns. |
| `references/pattern-matching-engine.md` | The 5-stage analysis protocol: IDENTIFY (code/screenshot to pattern taxonomy), BENCHMARK (score each pattern 1-10), SECTOR-FIT (cross-reference against sector matrix), PRESCRIBE (specific upgrade recommendations), COHERENCE (visual language unity assessment). Code signal to pattern mapping tables. Scoring dimensions and weights. Output templates. | Running the `/patterns` command. Analyzing codebases or screenshots for pattern quality. Generating pattern intelligence reports. |
| `references/pattern-evolution-2024-2026.md` | What is dying (hamburger on desktop, full-page spinners, auto-carousels), what is evolving (search to AI-semantic, dropdowns to combobox, forms to progressive), what is emerging (command palette, AI copilot, generative UI, bottom sheets, container queries, passkeys), what is stable. What vibe coders get wrong. | Ensuring recommendations are temporally current. Flagging dated patterns. Recommending modern alternatives. |
| `references/anti-pattern-encyclopedia.md` | 100+ anti-patterns across navigation, data display, forms, layout, commerce, feedback, accessibility, and AI. Each: description, why it seems reasonable, why it fails, what to use instead, cognitive science, severity. The Vibe Coder's Top 10 anti-patterns with frequency data. | Identifying anti-patterns in user code. Explaining why something is wrong. Prescribing the correct alternative. |

## Cross-References

This skill is the connective tissue that links analysis to action:

- **`sector-style-intelligence`** — Provides visual direction (colors, typography, tone) per sector. This skill provides pattern direction per sector. Together they define what a product in sector X should look like AND how it should work.
- **`screen-flow-patterns`** — Provides screen type and flow catalogs. This skill provides the broader pattern taxonomy that screen types are composed of.
- **`component-patterns-code`** — Provides React, SwiftUI, and CSS code for individual components. This skill identifies which components are needed; component-patterns-code provides the implementation.
- **`cognitive-psychology-ux`** — Provides the cognitive science (Fitts, Hick, Miller, Gestalt) that explains why patterns work or fail. This skill applies those principles to pattern evaluation.
- **`nng-ux-heuristics`** — Provides Nielsen's 10 heuristics for evaluation. This skill uses heuristics to score pattern execution.
- **`accessibility-inclusive-design`** — Provides WCAG compliance details. This skill flags accessibility gaps in pattern execution.
- **`design-systems-architecture`** — Provides token architecture. This skill assesses whether patterns consume tokens consistently (coherence).
- **`design-critique-case-studies`** — Provides deep product case studies. This skill provides broader pattern-level benchmarking.
- **`interaction-motion-design`** — Provides animation and motion patterns. This skill assesses whether patterns have appropriate motion.
- **`performance-states-patterns`** — Provides loading, error, and empty state patterns. This skill flags missing states as pattern gaps.

## Commands Powered by This Skill

| Command | How This Skill Is Used |
|---------|----------------------|
| `/patterns` | Primary command — runs the full 5-stage analysis pipeline |
| `/ship` | Consumes pattern taxonomy for component building, benchmark DNA for quality targeting |
| `/screen` | Consumes screen patterns from taxonomy, sector expectations from matrix |
| `/vibe-check` | Cross-references pattern quality during heuristic evaluation |
| `/benchmark` | Uses designer benchmark DNA for competitive comparison |
| `/inspo` | Uses pattern taxonomy and benchmark DNA for inspiration references |
| `/roast` | References anti-pattern encyclopedia during design critique |
| `/remix` | Uses prescriptions from pattern analysis to drive redesign |
| `/judge` | Pattern quality contributes to overall design score |

## How to Use This Skill

When Claude Code activates this skill, it draws from:

1. **Pattern Taxonomy** to identify and classify what is present in the user's code/screenshots
2. **Designer Benchmark DNA** to know what world-class execution looks like for each pattern
3. **Sector Pattern Matrix** to know which patterns are critical for the user's industry
4. **Pattern Matching Engine** to run the systematic 5-stage analysis pipeline
5. **Pattern Evolution** to ensure recommendations are temporally current
6. **Anti-Pattern Encyclopedia** to identify and explain what is wrong

The combination of these six reference files gives Sumi deep pattern intelligence — not by listing every possible UI, but by providing a taxonomy deep enough to classify any UI, benchmarks comprehensive enough to score any execution, and prescriptions specific enough to upgrade any pattern to world-class.
