# Pattern Decision Engine — Choose the Right Pattern Every Time

## How to Use This File

When a user says "I need to display a list" or "how should my navigation work," this file provides decision trees that narrow from a vague need to a specific pattern recommendation. Each tree starts with the user's goal and asks 3-5 branching questions about their context to arrive at the right pattern with rationale.

The decision trees are not theoretical. They encode the same decisions that senior product designers make intuitively after years of experience. The goal is to give that intuition to anyone — especially vibe coders who know what they want to build but not which pattern to use.

Cross-reference pattern recommendations with:
- `pattern-taxonomy-complete.md` for full pattern specs
- `pattern-quick-lookup.md` for quick pattern summaries
- `designer-benchmark-dna.md` for world-class examples
- `emerging-patterns-2025-2026.md` for cutting-edge alternatives

---

## Decision Tree 1: "I need to display a list of items"

Start here when the user needs to show a collection of things — products, users, messages, tasks, files, anything.

### Q1: How many items will be displayed?

**A: Fewer than 10 items**
→ Go to Q2a

**B: 10-100 items**
→ Go to Q2b

**C: 100-1000+ items**
→ Go to Q2c

---

### Q2a (Fewer than 10 items): What kind of content are the items?

**Visual content (images are primary — products, photos, designs):**
→ **Card Grid** (2-3 columns)
- Rationale: Small collections with visual content benefit from image prominence. Cards give each item visual weight.
- Benchmark: Dribbble shots grid, App Store featured.

**Text-heavy data (structured fields — emails, tasks, records):**
→ Go to Q3a

**Mixed content with varying importance:**
→ **Bento Grid**
- Rationale: When items have different importance levels, a bento layout lets you give visual weight to the most important items.
- Benchmark: Apple feature pages, Vercel dashboard.

### Q3a: Do users need to compare items across multiple attributes?

**Yes, need to compare (sorting, filtering across columns):**
→ **Data Table**
- Rationale: Tables make cross-row comparison effortless. Even with few rows, columns enable scanning.
- Benchmark: Stripe payments table.

**No, items are read sequentially or acted on individually:**
→ **Simple List**
- Rationale: Lists are the most compact and scannable format for sequential content.
- Benchmark: Linear issue list, Slack channels.

---

### Q2b (10-100 items): Are items primarily visual or data-driven?

**Visual (images, thumbnails are primary):**
→ Go to Q3b_visual

**Data-driven (text, numbers, status):**
→ Go to Q3b_data

**Mixed (some visual, some data):**
→ **Card Grid with toggle** (offer list and grid views)
- Rationale: When content is mixed, let users choose their preferred density. Grid for browsing, list for scanning.
- Benchmark: macOS Finder view toggle, Airbnb list/map toggle.

### Q3b_visual: Are all items the same height?

**Yes (uniform thumbnails — products, avatars, album art):**
→ **Card Grid** (responsive 2-4 columns)
- Rationale: Uniform grid is the most efficient layout for similarly-sized visual content.
- Benchmark: Unsplash, Shopify product grid.

**No (variable height — photos, pins, articles with different image ratios):**
→ **Masonry Layout**
- Rationale: Masonry eliminates row gaps, making variable-height content visually cohesive.
- Benchmark: Pinterest, Dribbble.

### Q3b_data: Do users need to sort, filter, or select multiple items?

**Yes:**
→ **Data Table** (sortable, filterable, with row selection)
- Rationale: Tables are the gold standard for interactive structured data. Sorting and filtering are built into the pattern.
- Benchmark: Stripe Dashboard, Airtable.

**No, just scan and click into detail:**
→ **List / Feed**
- Rationale: Lists are faster to scan than tables when users do not need to compare across columns.
- Benchmark: Linear issue list, Gmail inbox.

---

### Q2c (100-1000+ items): Is the list the primary content or a sidebar/picker?

**Primary content (the list IS the screen):**
→ Go to Q3c_primary

**Sidebar or picker (selecting from a large set):**
→ **Virtual List with search** (combobox or searchable list)
- Rationale: Users cannot browse 100+ items in a picker — they need to search. Virtualization prevents DOM bloat.
- Benchmark: Linear assignee picker (cmdk), GitHub repo picker.

### Q3c_primary: Is it a continuous feed or structured data?

**Continuous feed (social, activity, messaging):**
→ **Virtual List + Infinite Scroll**
- Rationale: Feeds are consumed continuously. Pagination would interrupt the flow. Virtualization keeps performance smooth.
- Benchmark: Twitter/X timeline, Slack messages.

**Structured data (records, transactions, admin data):**
→ **Data Table + Pagination + Server-Side Filtering**
- Rationale: For large structured data, users need position awareness (page 3 of 50), server-side pagination, and the ability to return to specific pages.
- Benchmark: Stripe payments table (handles millions of records).

**Visual content (image library, product catalog):**
→ **Virtualized Card Grid + Infinite Scroll + Faceted Filters**
- Rationale: Large visual catalogs need the visual appeal of cards with the performance of virtualization and the findability of filters.
- Benchmark: Unsplash, Shopify product admin, Pinterest.

---

## Decision Tree 2: "I need a navigation system"

Start here when designing the navigation structure for a product or feature.

### Q1: What platform is primary?

**A: Mobile (phone-first)**
→ Go to Q2_mobile

**B: Desktop (web app or desktop app)**
→ Go to Q2_desktop

**C: Both equally (responsive)**
→ Go to Q2_responsive

---

### Q2_mobile: How many primary destinations?

**2-3 destinations:**
→ Go to Q3_mobile_few

**4-5 destinations:**
→ **Bottom Navigation Bar**
- Rationale: The dominant mobile navigation pattern. 4-5 tabs with icons + labels gives users a persistent mental model of the app structure.
- Benchmark: Instagram (5), Spotify (5), Cash App (5).

**6+ destinations:**
→ **Bottom Navigation Bar (top 4-5) + Drawer/Hamburger for rest**
- Rationale: Prioritize the top 4-5 destinations in the bottom nav. Move secondary destinations to a drawer. Do not use a "More" tab — reorganize instead.
- Benchmark: Gmail mobile (5 bottom tabs, drawer for labels/settings).

### Q3_mobile_few: What type of app?

**Content consumption (reading, browsing, media):**
→ **Bottom Navigation Bar** (even with 2-3 items, it anchors the experience)
- Rationale: Bottom nav provides consistent wayfinding even with few destinations.
- Benchmark: Apple Music (3 main destinations).

**Task-focused (single primary workflow):**
→ **Hub-and-Spoke** (home screen → task → return to home)
- Rationale: When there is one main workflow, navigation complexity distracts. A central hub with task screens keeps things simple.
- Benchmark: Calculator apps, Camera apps, Apple Watch.

**Communication (chat, messaging):**
→ **Tab bar + conversation list pattern**
- Rationale: Communication apps need a conversation list as the primary view with tabs for different message types (DMs, channels, activity).
- Benchmark: Slack mobile, WhatsApp, iMessage.

---

### Q2_desktop: How many sections does the product have?

**1-4 sections:**
→ Go to Q3_desktop_few

**5-15 sections:**
→ **Sidebar Navigation**
- Rationale: Sidebars are the standard for SaaS products with multiple sections. They persist, can be collapsed, and support grouping and nesting.
- Benchmark: Linear, Notion, Slack, Figma.

**15+ sections:**
→ **Sidebar Navigation + Command Palette**
- Rationale: Beyond 15 sections, even a good sidebar becomes overwhelming. A command palette (Cmd+K) lets power users navigate faster than any menu. The sidebar handles browsing; the command palette handles jumping.
- Benchmark: Notion (many pages, Cmd+K essential), VS Code (many files + Cmd+P).

### Q3_desktop_few: What type of product?

**Marketing site or content site:**
→ **Top Navigation Bar**
- Rationale: Top nav is the web standard for content-focused sites. Users expect it and it keeps the content area clean.
- Benchmark: Stripe marketing, Apple.com, Vercel.

**SaaS product / web app:**
→ **Sidebar Navigation** (even with few sections, it scales)
- Rationale: Start with a sidebar even if you have only 4 sections. It scales as the product grows. Switching from top nav to sidebar later is a major UX disruption.
- Benchmark: Linear started with few sections, sidebar scaled.

**Developer tool / technical product:**
→ **Sidebar Navigation + Command Palette (from day one)**
- Rationale: Developer users expect keyboard-first navigation. A command palette is not optional — it is expected.
- Benchmark: Vercel, Stripe Dashboard, GitHub.

**Single-purpose tool (editor, viewer, player):**
→ **Minimal nav — top toolbar + contextual panels**
- Rationale: When the product IS the content (editor, player), navigation should be minimal. Toolbars and context panels serve dual duty.
- Benchmark: Figma (toolbar + panels), VS Code, Google Docs.

---

### Q2_responsive: What is the core user journey?

**Browse and discover (e-commerce, media, social):**
→ Desktop: **Top Nav + Mega Menu** | Mobile: **Bottom Nav + Hamburger for secondary**
- Rationale: Browsing needs discoverability on both platforms. Mega menus expose categories on desktop; bottom nav provides the mobile foundation.
- Benchmark: Airbnb (top nav desktop, bottom nav mobile).

**Work and create (SaaS, productivity, tools):**
→ Desktop: **Sidebar Navigation** | Mobile: **Bottom Nav (simplified) + Drawer for sidebar items**
- Rationale: The desktop sidebar maps to a simplified mobile bottom nav. Not all sidebar items need mobile presence — prioritize.
- Benchmark: Notion (sidebar desktop, simplified mobile nav).

**Read and consume (news, blogs, documentation):**
→ Desktop: **Top Nav + Table of Contents sidebar** | Mobile: **Hamburger (for nav) + Bottom action bar (for reading controls)**
- Rationale: Reading experiences need minimal chrome. ToC sidebar aids long-form navigation on desktop; mobile can hide nav behind hamburger.
- Benchmark: MDN, Stripe Docs.

---

## Decision Tree 3: "I need to collect user input"

Start here when designing forms, inputs, or any data collection.

### Q1: How many fields do you need?

**A: 1-3 fields**
→ Go to Q2_few

**B: 4-7 fields**
→ Go to Q2_medium

**C: 8+ fields**
→ Go to Q2_many

---

### Q2_few (1-3 fields): What is the context?

**Inline within content (renaming, quick edit, adding a tag):**
→ **Inline Editing**
- Rationale: For 1-2 field edits, navigating to a form is overkill. Click-to-edit keeps users in context.
- Benchmark: Notion page titles, Airtable cell editing, Linear issue names.

**Standalone action (login, search, subscribe, single input):**
→ **Single-Page Form** (compact, single column)
- Rationale: A clean single-column form with 1-3 fields is the fastest path to completion.
- Benchmark: Stripe login, newsletter signups.

**Part of a larger workflow (add comment, quick create):**
→ **Popover or Bottom Sheet Form**
- Rationale: A lightweight popover or sheet keeps the user in the current context while collecting quick input.
- Benchmark: Linear quick-create (Cmd+I), Notion comment box.

---

### Q2_medium (4-7 fields): Is this mobile or desktop?

**Desktop:**
→ Go to Q3_medium_desktop

**Mobile:**
→ Go to Q3_medium_mobile

### Q3_medium_desktop: Do fields have logical groups?

**Yes (e.g., personal info + address + preferences):**
→ **Single-Page Form with grouped sections**
- Rationale: Group related fields visually. Section headers reduce perceived complexity. 4-7 fields is manageable on one page when grouped.
- Benchmark: Stripe account setup, GitHub settings.

**No (independent fields):**
→ **Single-Page Form** (single column, top-to-bottom)
- Rationale: A straightforward vertical form. Do not overthink it — 4-7 fields is not enough to warrant multi-step.
- Benchmark: Standard signup forms, contact forms.

### Q3_medium_mobile: How engaged is the user at this point?

**Highly motivated (checkout, onboarding they chose to start):**
→ **Single-Page Form with floating save button**
- Rationale: Motivated users will scroll through 4-7 fields on mobile. A floating save button ensures they can always submit.
- Benchmark: Shopify mobile checkout (simplified).

**Low motivation (optional profile fields, preferences):**
→ **Multi-Step Form (2-3 steps, 2-3 fields each)**
- Rationale: Lower motivation requires lower perceived effort. Breaking 6 fields into 2 steps of 3 fields each makes each step feel trivial.
- Benchmark: Duolingo setup, TikTok interests.

---

### Q2_many (8+ fields): What type of data?

**Structured application form (job application, insurance, government):**
→ **Multi-Step Form (Wizard)**
- Rationale: Long structured forms must be chunked. Show progress. Validate per step. Save progress for return visits. This is the only humane way to handle 8+ fields.
- Benchmark: Stripe onboarding (multi-step, contextual), government form patterns (Gov.uk).

**Configuration/settings (many toggles, preferences, options):**
→ **Grouped Settings Page**
- Rationale: Settings are not submitted as a batch — they are browsed and adjusted individually. Group by category with section headers. Save per-section or auto-save.
- Benchmark: iOS Settings, GitHub notification settings, Linear settings.

**Data entry (spreadsheet-like, repetitive records):**
→ **Editable Data Table / Spreadsheet**
- Rationale: When entering many similar records, a table-based input (like Airtable or Excel) is vastly more efficient than forms.
- Benchmark: Airtable, Notion table, Google Sheets.

**Creative content (document, post, page):**
→ **Block Editor**
- Rationale: Creative content needs flexible structure, not rigid fields. A block editor lets users compose freely.
- Benchmark: Notion, WordPress Gutenberg.

---

## Decision Tree 4: "I need to show feedback to the user"

Start here when deciding how to communicate status, errors, success, or information to users.

### Q1: What is the urgency/importance?

**A: Critical — requires immediate attention or action**
→ Go to Q2_critical

**B: Important — user should know, but can continue working**
→ Go to Q2_important

**C: Informational — nice to know, not urgent**
→ Go to Q2_info

---

### Q2_critical: Does the user need to take an action?

**Yes — must decide (confirm deletion, choose option, fix error):**
→ **Confirmation Dialog / Modal**
- Rationale: Modals force focus. For destructive or irreversible actions, the user must pause and confirm. No auto-dismiss.
- Benchmark: GitHub "Delete repository" (type name to confirm), Stripe "Cancel subscription."

**Yes — must fix something (form error, validation failure):**
→ **Inline Error Messages + Error Summary (scroll to first error)**
- Rationale: Show errors exactly where they occur (field-level) plus a summary at the top. Auto-scroll to the first error.
- Benchmark: Stripe form validation (inline + field highlight), Gov.uk error pattern.

**No — system is down or broken (500, offline, maintenance):**
→ **Full Error Page**
- Rationale: When the entire experience is broken, a full error page with clear messaging, suggested actions, and support links is appropriate.
- Benchmark: GitHub 404 (octocat), Notion offline page, Vercel error.

---

### Q2_important: Is it related to a user action or a system event?

**User action result (saved, sent, deleted, copied):**
→ Go to Q3_action

**System event (new version available, maintenance coming, feature update):**
→ **Alert Banner** (dismissable, page-level)
- Rationale: System events affect all users. A persistent (but dismissable) banner at the top of the page communicates without interrupting.
- Benchmark: GitHub incident banner, Vercel deployment banner, Notion update notice.

### Q3_action: Is the action reversible?

**Yes (archive, move, soft-delete):**
→ **Toast with Undo** (auto-dismiss in 5-8 seconds)
- Rationale: For reversible actions, show confirmation with an undo option. The undo window gives users confidence to act quickly.
- Benchmark: Gmail "Message archived — Undo", Notion block delete.

**No (sent message, published post, charged payment):**
→ **Success Toast** (auto-dismiss in 3-5 seconds) — but for high-stakes irreversible actions, use a **pre-action Confirmation Dialog** instead of a post-action toast.
- Rationale: If the action cannot be undone, the confirmation should happen before the action, not after.
- Benchmark: Stripe payment confirmation (pre-action), then success toast.

---

### Q2_info: How long should the user see this?

**Briefly — one-time acknowledgment (copied to clipboard, preference saved):**
→ **Toast / Snackbar** (auto-dismiss in 3 seconds, no action needed)
- Rationale: Minimal, non-blocking, auto-dismissing. Just enough to confirm the action without demanding attention.
- Benchmark: Notion "Copied to clipboard", Linear preference saved.

**Persistently — ongoing status (syncing, online/offline, background task):**
→ **Status Indicator** (inline text/icon, not a notification)
- Rationale: Ongoing states should not keep re-notifying. A persistent but subtle indicator shows the current state at a glance.
- Benchmark: Notion "Saving..." / "Saved", Figma "Synced to cloud", Slack "Connecting..."

**Contextually — related to specific content (feature tip, data explanation):**
→ **Popover or Contextual Help** (triggered by hover/click on an info icon)
- Rationale: Content-specific information should be discoverable at the point of need, not pushed as a notification.
- Benchmark: Stripe Dashboard help popovers, GitHub explanation tooltips.

---

## Decision Tree 5: "I need to display data/metrics"

Start here when building dashboards, analytics, or data-heavy views.

### Q1: Who is the audience?

**A: Executives / non-technical stakeholders**
→ Go to Q2_exec

**B: Analysts / data-savvy users**
→ Go to Q2_analyst

**C: All users (mixed technical levels)**
→ Go to Q2_mixed

---

### Q2_exec: How many metrics need to be visible at once?

**1-4 KPIs (headline numbers):**
→ **Stat Display Cards** (large numbers, trend arrows, sparklines)
- Rationale: Executives need the answer, not the data. Big numbers with trends tell the story instantly.
- Benchmark: Stripe Dashboard top row, Mercury overview.

**5-8 metrics with trends:**
→ **Stat Cards Row + Primary Time Series Chart**
- Rationale: KPI cards for the headlines, one primary chart for the most important trend. Do not overload — pick the chart that tells the story.
- Benchmark: Vercel analytics, Shopify admin dashboard.

**Full performance overview:**
→ **Scorecard / Dashboard Layout**
- Rationale: A structured dashboard with stat cards, 2-3 charts, and a key table. Use color coding (green/yellow/red) for at-a-glance health assessment.
- Benchmark: Executive dashboards, OKR tools.

---

### Q2_analyst: What kind of analysis do they need?

**Trend analysis (how is metric X changing over time?):**
→ **Time Series Chart** (line or area, with date range selector, zoom, and comparison)
- Rationale: Time series is the foundation of trend analysis. Multi-series support for comparison. Zoom for detail.
- Benchmark: Stripe analytics, Grafana.

**Comparison (how does segment A compare to segment B?):**
→ **Grouped Bar Chart + Data Table**
- Rationale: Bar charts make discrete comparisons visual. Paired with a table for exact values.
- Benchmark: Google Analytics, Mixpanel.

**Distribution (what is the breakdown of category X?):**
→ **Donut Chart (< 7 segments) or Horizontal Bar Chart (7+ segments) + Breakdown Table**
- Rationale: Donuts for parts-of-whole with few segments. Horizontal bars for many segments (sorted by value). Always pair with a table for precision.
- Benchmark: Mercury account breakdown, Stripe revenue by product.

**Exploration (let me slice data my way):**
→ **Report Builder / Custom Dashboard**
- Rationale: Analysts need to build their own views. Provide metric selectors, dimension pickers, and flexible chart types.
- Benchmark: Mixpanel, Google Analytics, Grafana.

**Funnel / conversion (where do users drop off?):**
→ **Funnel Visualization + Step-Level Metrics**
- Rationale: Funnels make drop-off points visually obvious. Show conversion rate between each step.
- Benchmark: Mixpanel funnels, Amplitude funnels.

---

### Q2_mixed: What is the primary use case?

**Monitoring health (is everything OK?):**
→ **Status Board + KPI Cards**
- Rationale: Mixed audiences need a quick health check. Status indicators (green/yellow/red) with KPI cards communicate state without requiring data literacy.
- Benchmark: Vercel status page, GitHub status.

**Tracking progress (are we on track?):**
→ **Progress Indicators + Milestone Timeline + Stat Cards**
- Rationale: Progress views work for everyone. Show percentage complete, milestone dates, and key numbers.
- Benchmark: Linear cycle progress, OKR tools.

**Understanding performance (how are we doing?):**
→ **Dashboard Layout** (stat cards + primary chart + secondary table, with date range selector)
- Rationale: The standard dashboard layout serves mixed audiences by providing headline numbers (for executives), charts (for visual thinkers), and tables (for detail seekers).
- Benchmark: Stripe Dashboard — works for both CEOs and engineers.

---

## Decision Tree 6: "I need to onboard users"

Start here when designing the new user experience.

### Q1: How complex is your product?

**A: Simple (1-2 core features, self-explanatory)**
→ Go to Q2_simple

**B: Moderate (5-10 features, some learning curve)**
→ Go to Q2_moderate

**C: Complex (many features, significant learning curve)**
→ Go to Q2_complex

---

### Q2_simple: Is the value proposition immediately clear?

**Yes (users know exactly what the app does before they sign up):**
→ **Empty State Onboarding** (guide first action from the empty state)
- Rationale: Skip the onboarding tour. Let users start using the product immediately. The empty state guides the first action.
- Benchmark: Notion empty page ("Press Enter to start writing"), Todoist empty inbox.

**No (users need to understand the value):**
→ **Benefit-Oriented Welcome Screen + Empty State**
- Rationale: One screen explaining the value proposition, then drop users into the product with guided empty states.
- Benchmark: Duolingo welcome, Headspace intro.

---

### Q2_moderate: Is the product mobile or desktop?

**Mobile:**
→ **Onboarding Carousel (3-4 screens) + Checklist**
- Rationale: Mobile onboarding carousels are a proven pattern for communicating 3-4 key benefits before entering the app. Follow with a checklist for setup tasks.
- Benchmark: Duolingo, Headspace, Cash App.

**Desktop:**
→ **Checklist Onboarding + Contextual Tooltips**
- Rationale: Desktop users prefer to learn by doing. A visible checklist (5-7 items) guides setup tasks. Contextual tooltips explain features as users encounter them.
- Benchmark: Notion "Getting Started" checklist, Linear onboarding, Stripe activation checklist.

---

### Q2_complex: What is the user's technical level?

**Technical (developers, designers, analysts):**
→ **Quick Setup Wizard (3-5 steps) + Comprehensive Documentation + Command Palette**
- Rationale: Technical users want to get going fast. A brief setup wizard, then let them explore. Excellent documentation and a command palette let them discover features on their own terms.
- Benchmark: Vercel project setup, Stripe API onboarding, GitHub new repo.

**Non-technical (business users, general consumers):**
→ **Guided Interactive Tutorial + Checklist + Sample Data**
- Rationale: Non-technical users need hand-holding. An interactive tutorial that walks through the core workflow, a visible checklist for ongoing setup, and sample data so the product does not feel empty.
- Benchmark: Figma onboarding tutorial, Canva first design, Airtable templates.

**Mixed:**
→ **Personalization Setup ("What do you want to do?") + Role-Based Onboarding**
- Rationale: Ask users their role or goal during onboarding, then tailor the experience. Developers get API docs; business users get guided setup.
- Benchmark: Notion workspace setup, Slack "What is your role?", HubSpot onboarding.

---

## Decision Tree 7: "I need to design a settings page"

Start here when building settings, preferences, or configuration views.

### Q1: How many settings exist?

**A: 1-5 settings**
→ Go to Q2_few

**B: 6-20 settings**
→ Go to Q2_medium

**C: 20+ settings**
→ Go to Q2_many

---

### Q2_few: Are settings frequently changed?

**Yes (theme toggle, notification mute, view preference):**
→ **Inline Settings** (within the view they affect, not a separate page)
- Rationale: Frequently changed settings should be accessible where they are used. A dark mode toggle in the sidebar, not buried in settings.
- Benchmark: Linear dark mode toggle (inline), Notion view options.

**No (one-time setup, rarely changed):**
→ **Simple Settings Section** (within profile or account page)
- Rationale: Few rarely-changed settings do not justify a dedicated settings area. Nest them in an existing section.
- Benchmark: Simple SaaS account pages.

---

### Q2_medium: Do settings have natural groupings?

**Yes (account, notifications, appearance, integrations):**
→ **Grouped Settings Page** (section headers, grouped controls)
- Rationale: Group related settings with clear section headers. Users scan headers to find what they need.
- Benchmark: iOS Settings groups, GitHub settings.

**No (flat list of independent preferences):**
→ **Single Scrolling Settings Page** (alphabetical or priority-ordered)
- Rationale: Without natural groups, a clean scrolling list ordered by importance (most-changed first) is simplest.
- Benchmark: Simple SaaS preference pages.

---

### Q2_many: Is this desktop or mobile?

**Desktop:**
→ **Settings Page with Sidebar Navigation**
- Rationale: A left sidebar listing setting categories, right panel showing the selected category. This is the gold standard for settings-heavy desktop apps.
- Benchmark: VS Code settings, GitHub Settings, Notion Settings, Linear Settings.

**Mobile:**
→ **Drill-Down Settings** (list → category → individual settings)
- Rationale: iOS Settings pattern — tap into a category, see settings for that category, back button to return. Natural and proven.
- Benchmark: iOS Settings (the canonical mobile settings pattern).

**Both:**
→ Desktop: **Sidebar settings** | Mobile: **Drill-down settings** (same data, different navigation)
- Rationale: Use the platform-native settings pattern for each. Map sidebar categories to drill-down list items.
- Benchmark: Notion (sidebar on desktop, drill-down on mobile).

---

## Decision Tree 8: "I need search functionality"

Start here when adding search to a product.

### Q1: What is being searched?

**A: A single content type (products, users, files, issues)**
→ Go to Q2_single

**B: Multiple content types (pages, people, actions, messages)**
→ Go to Q2_multi

---

### Q2_single: How many searchable items?

**Under 50 items:**
→ **Client-Side Filter** (filter bar or search input with instant filtering)
- Rationale: With under 50 items, client-side filtering is instant and does not need a server round trip. A simple search input that filters the visible list.
- Benchmark: Simple filter inputs on small lists.

**50-10,000 items:**
→ **Search Input with Instant Results** (search-as-you-type, debounced)
- Rationale: Type-ahead with a results dropdown provides the fastest search experience. Debounce at 200-300ms. Highlight matching text.
- Benchmark: Algolia InstantSearch, GitHub repo search, Raycast.

**10,000+ items:**
→ **Search Input + Results Page with Faceted Filters**
- Rationale: Large catalogs need server-side search with pagination and filters. Faceted search lets users narrow results across multiple dimensions.
- Benchmark: Amazon product search, Shopify admin, Algolia.

### Q2_multi: Is this a power-user or general-user product?

**Power-user (developer tools, productivity, SaaS):**
→ **Command Palette with Search** (Cmd+K)
- Rationale: Power users expect Cmd+K. Combine search across content types with actions (navigation, commands). Categorize results.
- Benchmark: Linear, Raycast, VS Code, Notion.

**General-user (consumer, e-commerce, content):**
→ Go to Q3_general

### Q3_general: How important is search to the product's core use case?

**Critical (search IS the product — Google, marketplace, library):**
→ **Prominent Search Bar + Search Results Page + Advanced Filters**
- Rationale: When search is the primary interaction, it gets prime screen real estate. Full results page with sorting, filtering, and rich result cards.
- Benchmark: Google Search, Airbnb, Amazon, Spotify.

**Important but not primary (search supplements browsing):**
→ **Search Input (header) + Instant Results Dropdown**
- Rationale: Search lives in the header, accessible from any page. Results appear in a dropdown — most users find what they need without a full results page.
- Benchmark: Stripe Dashboard search, Notion search, Slack search.

**Minor (search is a convenience, not core):**
→ **Search Input within the relevant section** (not global)
- Rationale: Scope search to where it is used (e.g., search within settings, search within a specific list). Do not build global search if it is not needed.
- Benchmark: Settings search in VS Code, iOS Settings search.

---

## Decision Tree 9: "I need to design for AI features"

Start here when integrating AI capabilities into a product.

### Q1: What type of AI interaction?

**A: Chat / conversation (user talks to AI)**
→ Go to Q2_chat

**B: Generation (AI creates content — text, image, code)**
→ Go to Q2_generation

**C: Suggestion / assistance (AI helps with user's task)**
→ Go to Q2_suggestion

**D: Agent / autonomous (AI performs multi-step tasks)**
→ Go to Q2_agent

---

### Q2_chat: Is AI the primary product or a feature within a product?

**Primary (AI chatbot product — ChatGPT, Claude, Perplexity):**
→ **Full-Screen Chat Interface**
- Rationale: When AI conversation IS the product, give it the full screen. Message list, rich input with attachments, conversation history sidebar.
- Benchmark: ChatGPT, Claude, Perplexity.

**Feature within product (AI assistant for existing workflows):**
→ **AI Sidebar / Copilot Panel**
- Rationale: The AI lives alongside the main workspace. It reads context from the current view and can insert results back into the user's work. Togglable, not always visible.
- Benchmark: GitHub Copilot Chat, Notion AI sidebar, Cursor.

---

### Q2_generation: What is being generated?

**Text (writing, summaries, translations):**
→ **Inline AI with Streaming Output**
- Rationale: Text generation should appear where the text will live — inline in the document/input. Stream token-by-token for perceived responsiveness.
- Benchmark: Notion AI (inline in document), Gmail Smart Compose.

**Images:**
→ **AI Image Generation Modal/Panel**
- Rationale: Image generation needs a prompt input, generation progress, result gallery (2-4 options), and insert action. A modal or panel keeps it focused.
- Benchmark: ChatGPT DALL-E, Canva Magic Media, Midjourney.

**Code:**
→ **AI Code Completion (ghost text) + AI Chat for complex generation**
- Rationale: Routine code completion as ghost text (tab to accept). Complex generation (build a component, refactor) via chat sidebar.
- Benchmark: GitHub Copilot (ghost text + chat), Cursor.

**UI / layouts:**
→ **AI Generated UI with Preview + Edit**
- Rationale: Show the generated UI in a preview, let the user edit/adjust, then apply. Emerging pattern with no canonical form yet.
- Benchmark: v0 by Vercel, Claude Artifacts.

---

### Q2_suggestion: How confident are the suggestions?

**High confidence (spelling, grammar, formatting — AI is usually right):**
→ **Auto-Apply with Undo**
- Rationale: When AI is right 95%+ of the time, auto-apply and provide undo. Asking for confirmation every time creates friction.
- Benchmark: Grammarly auto-corrections, Superhuman auto-triage.

**Medium confidence (categorization, priority, smart defaults):**
→ **Suggestion Badge with Accept/Dismiss**
- Rationale: Show the suggestion as a visible but non-blocking badge. User can accept in one click or dismiss. Show reasoning on hover.
- Benchmark: Linear AI priority suggestions, Gmail priority inbox.

**Low confidence (complex recommendations, creative suggestions):**
→ **Suggestion Panel with Options + Reasoning**
- Rationale: When AI is uncertain, present multiple options with explanations. Let the user choose or ignore entirely.
- Benchmark: AI writing assistants showing 3 alternatives, design tool layout suggestions.

---

### Q2_agent: How long does the task take?

**Seconds (quick AI actions — summarize, translate, format):**
→ **Loading State → Result Inline**
- Rationale: Quick actions just need a brief loading indicator, then show the result where the user expects it.
- Benchmark: Notion AI summarize, ChatGPT quick responses.

**Minutes (multi-step tasks — research, code generation, analysis):**
→ **AI Agent Task Card** (step-by-step progress, expandable logs)
- Rationale: Users need visibility into what the agent is doing. Show steps, progress, and intermediate results. Allow pause/cancel.
- Benchmark: Claude Code task execution, Devin, GitHub Copilot Workspace.

**Hours/days (background jobs — training, large-scale processing):**
→ **Background Task with Notification on Complete**
- Rationale: Users cannot watch a progress bar for hours. Start the task, show it in a task queue, and notify when done.
- Benchmark: ML model training dashboards, large data exports, CI/CD builds.

---

## Decision Tree 10: "I need to handle empty/error states"

Start here when designing for when things go wrong or nothing is there yet.

### Q1: What state are you handling?

**A: Empty state (no data yet)**
→ Go to Q2_empty

**B: Error state (something went wrong)**
→ Go to Q2_error

**C: Loading state (data is coming)**
→ Go to Q2_loading

**D: No results (search or filter returned nothing)**
→ Go to Q2_noresults

---

### Q2_empty: Is this the user's first time seeing this view?

**Yes (first-run, no data has ever existed here):**
→ **Onboarding Empty State** (illustration + instructional text + primary CTA to create first item)
- Rationale: The empty state IS your onboarding opportunity. Guide the user to create their first item. Optionally offer templates or sample data.
- Benchmark: Notion empty page, Linear empty project, Figma empty file.

**No (data was cleared, or all items were completed/deleted):**
→ **Completion Empty State** (celebratory or neutral + next action suggestion)
- Rationale: If the user cleared their inbox or completed all tasks, celebrate it. If they deleted everything, suggest next steps.
- Benchmark: Superhuman "You're done!" (inbox zero), Todoist completed all tasks.

---

### Q2_error: What went wrong?

**Network error (offline, timeout, API failure):**
→ Go to Q3_network

**User error (invalid input, unauthorized action):**
→ **Inline Error** (field-level validation, contextual message)
- Rationale: Show the error exactly where the user went wrong, with a clear message and how to fix it.
- Benchmark: Stripe form validation.

**System error (500, unexpected failure, bug):**
→ **Error State with Retry + Report**
- Rationale: System errors should be honest ("Something went wrong"), offer retry, and provide a way to report the issue. Include an error ID for debugging.
- Benchmark: GitHub 500 page, Notion error page.

**Permission error (403, unauthorized, expired session):**
→ **Permission Error with CTA** (request access, log in, upgrade plan)
- Rationale: Tell the user exactly what they lack access to and give them a clear path to get access (request, login, upgrade).
- Benchmark: Google Docs "You need permission" page, Notion locked page.

### Q3_network: Is offline functionality available?

**Yes (app works offline):**
→ **Offline Banner + Continue Working** (show cached data, queue actions)
- Rationale: If the app supports offline, show a subtle banner indicating offline status but let users continue with cached data. Sync when reconnected.
- Benchmark: Notion offline mode, Google Docs offline.

**No (app requires network):**
→ **Offline Error Page** (friendly illustration + "No connection" message + auto-retry indicator)
- Rationale: Show a clear offline state with auto-retry. Do not show a blank screen or a cryptic error.
- Benchmark: Chrome dinosaur game (the gold standard of offline pages), Slack "Connecting..."

---

### Q2_loading: What is loading?

**Full page (initial page load, navigation):**
→ **Skeleton Screen** (shapes matching the real content layout)
- Rationale: Skeleton screens reduce perceived wait time by 30%. They set spatial expectations so the brain starts processing the layout before data arrives.
- Benchmark: Facebook, LinkedIn, Stripe Dashboard.

**Single component (a chart loading, a table refreshing):**
→ **Component-Level Skeleton or Spinner**
- Rationale: Only show loading state for the component that is loading. Keep the rest of the page interactive.
- Benchmark: Stripe chart loading, Vercel analytics.

**User-initiated action (button click, form submit):**
→ **Button Loading State** (spinner inside button, button disabled)
- Rationale: The loading indicator lives inside the button that was clicked. This provides direct cause-effect feedback.
- Benchmark: Stripe submit button, Vercel deploy button.

**Background process (sync, upload, AI generation):**
→ **Progress Bar or Status Text** (non-blocking, informational)
- Rationale: Background processes should inform without blocking. A progress bar or subtle status text lets users continue working.
- Benchmark: Notion "Saving...", Figma "Syncing", Vercel build progress.

---

### Q2_noresults: Did the user search or filter?

**Searched (typed a query, no matches):**
→ **No Results State** (search query acknowledgment + suggestions: check spelling, try broader terms, browse categories)
- Rationale: Acknowledge what was searched, explain why nothing was found, and offer alternatives. Never show a completely blank state.
- Benchmark: Google "No results found — Suggestions:", Amazon "Did you mean...?"

**Filtered (applied filters that exclude everything):**
→ **No Results with Filter Reset** (message + "Clear filters" button + show current filters)
- Rationale: Show which filters caused the empty result and offer one-click filter reset. Make it easy to back out.
- Benchmark: Airbnb "No exact matches — Try changing your filters", Shopify admin.

---

## Quick Reference: Decision Cheat Sheet

| Situation | Default Recommendation | When to Deviate |
|---|---|---|
| Show a list | List / Feed | Visual content → Card Grid; structured → Data Table |
| Mobile nav | Bottom Navigation Bar (4-5 items) | 2-3 items → Hub-and-spoke; 6+ → Drawer |
| Desktop nav | Sidebar Navigation | Marketing → Top Nav; 15+ sections → add Command Palette |
| Simple form (1-3 fields) | Single-Page Form | Inline edit if within content |
| Complex form (8+ fields) | Multi-Step Wizard | Settings → Grouped page; Data entry → Editable table |
| User feedback | Toast (3-5s auto-dismiss) | Destructive → Confirmation Dialog; reversible → Toast+Undo |
| Dashboard | Stat Cards + Primary Chart + Table | Executive → Scorecard; Analyst → Report Builder |
| Onboarding | Checklist + Empty States | Simple → Empty state only; Complex → Interactive tutorial |
| Settings (20+) | Sidebar settings (desktop) / Drill-down (mobile) | Few settings → Inline in context |
| Search | Search Input + Instant Results | Power user → Command Palette; Large catalog → Faceted |
| AI chat | Sidebar Copilot (feature) / Full-screen (product) | Generation → Inline streaming; Agent → Task cards |
| Empty state | Illustration + CTA to create first item | Completion → Celebrate; Error → Retry + Report |
| Loading | Skeleton Screen (page) / Spinner (component) | Button → Inline spinner; Background → Progress bar |
| Error | Inline + contextual message | System → Error page + retry; Offline → Banner + auto-retry |
