# UI Pattern Taxonomy — The Complete Classification

## How This Taxonomy Works

Every UI pattern in digital product design belongs to one of 10 categories. Each pattern has a canonical form (the version users have internalized through billions of interactions), variants (legitimate adaptations), anti-patterns (what looks similar but fails), and accessibility requirements (non-negotiable).

Patterns are not opinions. They are empirically validated solutions to recurring design problems. When Shopify, Stripe, Linear, Airbnb, and Apple converge on the same solution independently, that convergence is a pattern. When a designer deviates from a pattern, the burden of proof is on the deviation.

This taxonomy covers 200+ patterns across 10 categories. Each entry is structured for pattern matching: given a piece of code or a screenshot, Claude can identify which pattern is being attempted, score how well it is executed, and recommend the canonical or best-in-class version.

---

## Category 1: Navigation Patterns (28 patterns)

Navigation is the skeleton of any product. Users form a spatial mental model of your app within the first 30 seconds. Poor navigation is the single most common reason products feel "off" — not because any one screen is bad, but because moving between screens is confusing, inconsistent, or unpredictable.

### 1.1 Top Navigation Bar

**What it is**: Horizontal bar at the top of the viewport containing primary navigation links, logo, and key actions. The most universal navigation pattern on the web.

**Anatomy**: Logo/brand mark (left) | Primary nav links (center or left-aligned after logo) | Utility actions (right: search, notifications, avatar/account).

**Variants**:
- **Transparent overlay**: Nav floats over hero content, shifts to solid on scroll. Used by marketing sites (Apple, Stripe). Requires careful contrast management — text must be readable over any background it overlaps.
- **Sticky/fixed**: Remains visible on scroll. Standard for SaaS dashboards (Linear, Notion). Must not consume more than 64px vertical space on desktop, 56px on mobile.
- **Shrinking**: Full height on load, compresses to compact on scroll. Balances brand presence with content space. Apple.com pioneered this.
- **Mega menu**: Hover/click reveals a full-width dropdown with categorized links, featured content, and sometimes imagery. Used by e-commerce (Amazon, Shopify stores) and enterprise sites. Must be keyboard navigable — most implementations fail here.
- **Contextual**: Content changes based on current section. GitHub does this — repo nav shows Code/Issues/PRs/Actions only within a repo context.

**When to use**: Web applications, marketing sites, multi-section products. Default choice for desktop-first experiences.

**When NOT to use**: Mobile-primary apps (use bottom nav instead). Single-page applications with minimal navigation needs. Immersive/full-screen experiences (video, gaming, creative tools).

**Anti-patterns**:
- Hamburger menu on desktop (hides primary nav behind a click — kills discoverability)
- More than 7 top-level items (violates Miller's Law — chunk or use mega menu)
- Logo that is not a home link (violates Jakob's Law — every user expects this)
- Dropdown menus that require precise hover targeting (violates Fitts's Law)
- Nav that disappears on scroll with no way to get it back without scrolling to top

**Accessibility**:
- `<nav>` landmark with `aria-label="Main navigation"`
- Skip link as first focusable element: "Skip to main content"
- Keyboard: Tab through items, Enter to activate, Escape to close dropdowns
- `aria-current="page"` on active link
- Dropdown menus: `aria-expanded`, `aria-haspopup="true"`, arrow key navigation within

**Benchmark**: Linear's top nav — minimal, contextual, never more than 5 items visible. Stripe's marketing nav — mega menu with smooth animation, keyboard accessible, clear hierarchy.

### 1.2 Bottom Navigation Bar

**What it is**: Fixed bar at the bottom of the mobile viewport with 3-5 icon+label destinations. The dominant mobile navigation pattern since iOS and Android standardized it.

**Anatomy**: 3-5 tab items, each with icon + text label. Active state visually distinct. Optional badge for notifications. Fixed to viewport bottom, above safe area on notched devices.

**Variants**:
- **Standard (iOS/Android)**: 5 items max. iOS uses thin line icons (SF Symbols), Material uses filled icons with indicator pill. Labels always visible.
- **Floating**: Detached from screen edge with rounded corners and shadow. Emerging trend (Cash App, some fintech). Looks premium but reduces touch target reliability — the floating element can feel less anchored.
- **Morphing**: Center item transforms into an action (FAB-style). Common in creation-focused apps. The center action should be the app's primary creation gesture.
- **Contextual hide**: Scrolls away on downward scroll, reappears on upward scroll. Maximizes content area. Must reappear on any upward scroll, not just scroll-to-top.
- **Expandable**: Tapping active tab reveals sub-navigation. Instagram's profile tab doing this for saved/tagged/posts is the canonical example.

**When to use**: Mobile apps with 3-5 primary destinations. The default choice for consumer mobile products.

**When NOT to use**: Apps with only 1-2 destinations (use a simpler structure). Apps with 6+ destinations (use a sidebar or tab bar with "More"). Desktop applications. Content-reading apps where full-screen immersion matters.

**Anti-patterns**:
- More than 5 items (overcrowded, tiny targets)
- Icons without labels (recognition requires both — Google's own research proved this)
- Labels that truncate on small screens (test on 320px width)
- No active state indicator (user can't tell where they are — H1 violation)
- Placing a hamburger menu icon in the bottom nav (defeats the purpose of bottom nav)
- Bottom nav + top tab bar simultaneously (two horizontal nav bars = spatial confusion)

**Accessibility**:
- `role="tablist"` with `role="tab"` for each item
- `aria-selected="true"` on active tab
- Minimum 48x48dp touch target (Material guideline), 44x44pt (iOS guideline)
- Badge count announced: `aria-label="Notifications, 3 new"`
- Tab order follows visual order left-to-right

**Benchmark**: Apple's tab bar — always labeled, clear active state, consistent across all Apple apps. Cash App's floating nav — bold, minimal, only 4 items.

### 1.3 Sidebar Navigation

**What it is**: Vertical panel on the left (or right in RTL) containing navigation links, often with collapsible sections. The dominant pattern for SaaS, dashboards, and productivity tools.

**Anatomy**: App logo/name (top) | Primary navigation items with icons | Collapsible section groups | User account (bottom) | Collapse/expand toggle.

**Variants**:
- **Fixed full**: Always visible, fixed width (200-280px). Standard for desktop SaaS (Notion, Linear, Slack). Best for frequent navigation.
- **Collapsible to icons**: Shrinks to icon-only rail (~56-72px) to maximize content area. Figma, VS Code. Icon-only mode must have tooltips.
- **Collapsible to hidden**: Fully hides behind a toggle. Used when content needs maximum width. Must be accessible via keyboard shortcut.
- **Multi-level/nested**: Tree-style hierarchy for deep information architecture. File managers, documentation sites. Notion's sidebar is the gold standard — infinite nesting with smooth expand/collapse.
- **Dual sidebar**: Two panels — narrow icon rail + expanded detail panel on selection. Slack's redesign uses this. Powerful for apps with both workspace-level and context-level navigation.
- **Resizable**: User can drag the sidebar edge to resize. Figma, VS Code. Store the preference. Respect a minimum width (~160px) and maximum (~400px).

**When to use**: Desktop SaaS, dashboards, productivity tools, admin panels, documentation sites. Any application with 6+ navigation destinations or deep hierarchy.

**When NOT to use**: Mobile (use bottom nav or hamburger). Marketing/landing pages. Simple consumer apps with few destinations.

**Anti-patterns**:
- Sidebar wider than 300px by default (steals too much content space)
- No collapse option on screens < 1280px
- Horizontal scrolling within the sidebar
- Icons without tooltips in collapsed state
- Nesting deeper than 3 levels without visual indentation or breadcrumbs
- Sidebar that resets scroll position when navigating between pages
- "Active" state that is too subtle to see at a glance

**Accessibility**:
- `<nav>` landmark with `aria-label="Sidebar navigation"`
- Expandable sections: `aria-expanded` on toggle, `aria-controls` pointing to section
- Tree pattern: `role="tree"`, `role="treeitem"`, `aria-level` for depth
- Collapse toggle: descriptive `aria-label` ("Collapse sidebar" / "Expand sidebar")
- Keyboard: Arrow keys for tree navigation, Enter to expand/select

**Benchmark**: Linear's sidebar — clean grouping, keyboard shortcuts shown inline, smooth collapse. Notion's sidebar — infinite hierarchy, drag-to-reorder, quick-add at every level. Raycast's sidebar — minimal, fast, instant search integration.

### 1.4 Breadcrumbs

**What it is**: Horizontal trail showing the user's location within a hierarchy. Answers "Where am I?" and "How did I get here?"

**Anatomy**: Home link > Parent category > Current page. Separator between items (typically "/" or ">"). Current page is plain text (not a link).

**Variants**:
- **Hierarchy-based**: Reflects the site structure. Most common. E-commerce category paths.
- **Path-based**: Shows the user's actual navigation history. Less common, more confusing — browsers already have Back.
- **Attribute-based**: Shows filters/facets applied. E-commerce after filtering: "Shoes > Running > Men's > Under $100."
- **Truncated/collapsed**: Middle items collapse into "..." when the path is long. Click to expand. Google Drive does this.

**When to use**: E-commerce product pages, documentation, file systems, admin panels, any hierarchical content deeper than 2 levels.

**When NOT to use**: Flat navigation structures. Single-level apps. Mobile (usually too cramped — use a back button instead).

**Anti-patterns**:
- Making the current page a clickable link (it should be plain text)
- Using breadcrumbs as the only navigation (they supplement, not replace)
- More than 5 visible levels without truncation
- Breadcrumbs that don't match the actual hierarchy (misleading mental model)

**Accessibility**:
- `<nav aria-label="Breadcrumb">` wrapping an `<ol>`
- `aria-current="page"` on the last item
- Separator characters as decorative (`aria-hidden="true"`) or use CSS `::before`

**Benchmark**: Shopify admin — clean, always accurate to hierarchy. AWS Console — essential for deep hierarchies, always shows full context.

### 1.5 Tab Navigation

**What it is**: Horizontal row of labeled tabs that switch between views within the same context. The content below changes; the URL may or may not change.

**Anatomy**: Tab list container | Individual tabs with labels | Active indicator (underline, background, or pill) | Tab panels below.

**Variants**:
- **Underline tabs**: Active tab indicated by bottom border. Clean, minimal. GitHub, Stripe.
- **Pill/segment tabs**: Active tab has a filled background. Feels more like a toggle. iOS segmented controls.
- **Scrollable tabs**: Horizontal scroll when tabs exceed viewport width. Material Design standard for mobile. Must show scroll affordance (partial next tab visible or fade).
- **Vertical tabs**: Stacked vertically, typically on the left of content. Used for settings pages with many sections. AWS, Azure.
- **Icon tabs**: Icons with optional labels. Used when tab count is high and labels would be too long.
- **Closable tabs**: Tabs with close (x) buttons. Browser-style. Used in code editors, multi-document interfaces.

**When to use**: Multiple views of the same data or context. Settings pages. Profile sections. Dashboard views. Any time the user needs to switch between related content without leaving the page.

**When NOT to use**: Sequential/wizard flows (use stepper instead). Unrelated content areas (use separate pages). More than 7 tabs without scrolling mechanism.

**Anti-patterns**:
- Tabs that trigger navigation to a new page (tabs should be in-page view switches)
- Tabs that look like buttons (ambiguous affordance)
- No visible active indicator
- Tab content that is wildly different heights causing layout shift
- Nested tabs (tabs within tabs — cognitive load nightmare)

**Accessibility**:
- `role="tablist"` on container, `role="tab"` on each tab, `role="tabpanel"` on content
- `aria-selected="true"` on active tab
- `aria-controls` linking tab to its panel, `aria-labelledby` linking panel to its tab
- Keyboard: Arrow keys to move between tabs, Enter/Space to activate, Home/End for first/last
- Only active tab panel in tab order; inactive panels have `tabindex="-1"`

**Benchmark**: Stripe Dashboard tabs — clear underline indicator, smooth transitions, keyboard perfect. GitHub's repo tabs — contextual, never more than needed.

### 1.6 Command Palette / Spotlight

**What it is**: A keyboard-triggered search overlay that provides instant access to any action, page, or content in the application. The fastest-growing navigation pattern of 2023-2026. Replaces traditional menus for power users.

**Anatomy**: Trigger (Cmd+K / Ctrl+K) | Search input with placeholder | Categorized results list | Keyboard navigation hints | Recent/suggested items when empty.

**Variants**:
- **Navigation-focused**: Primarily finds pages/views. Notion, Linear.
- **Action-focused**: Executes commands (change theme, create item, toggle feature). VS Code, Raycast.
- **Hybrid**: Both navigation and actions in one palette. The modern standard. Raycast, Linear, Vercel.
- **Contextual**: Results change based on current view (e.g., different commands available in settings vs. editor). VS Code does this masterfully.
- **AI-enhanced**: Natural language queries that map to actions. "Show me revenue for last quarter" → navigates to analytics with filters applied. Emerging pattern, Notion AI approaches this.

**When to use**: Any application with 10+ possible destinations or actions. SaaS, productivity tools, developer tools, admin panels. Power users expect this. Increasingly expected in consumer apps too.

**When NOT to use**: Simple apps with < 5 destinations. First-time user experience (supplement, don't replace visible navigation). Purely content-consumption apps (readers, video players).

**Anti-patterns**:
- No keyboard shortcut (the whole point is keyboard speed)
- Slow search (> 100ms for local results)
- Results not keyboard-navigable
- No categorization of results (actions vs. pages vs. content)
- Not dismissable with Escape
- Stealing browser's Cmd+K (address bar) without allowing override

**Accessibility**:
- `role="combobox"` on input, `role="listbox"` on results
- `aria-activedescendant` tracks keyboard-focused result
- `aria-label="Command palette"` on the dialog
- Results announced as user arrows through them
- Escape closes palette, focus returns to trigger element

**Benchmark**: Raycast — the gold standard. Sub-50ms results, beautiful categorization, extensible. Linear — clean, fast, perfectly scoped to project management context. VS Code — the original mainstream command palette, deeply contextual.

### 1.7 Hamburger Menu

**What it is**: Three horizontal lines (the "hamburger") that toggle a hidden navigation panel. Originally designed for mobile, now overused on desktop.

**Anatomy**: Hamburger icon (top-left or top-right) | Overlay or slide-in panel with navigation links | Close mechanism (X, tap outside, swipe).

**Variants**:
- **Slide-in drawer**: Panel slides from left/right. Standard mobile pattern.
- **Full-screen overlay**: Panel covers entire viewport. Used for dramatic effect on marketing sites.
- **Dropdown**: Panel drops down from the header. Less common, can feel disorienting.

**When to use**: Mobile as a secondary navigation holder (when bottom nav handles primary destinations but you need more options). Responsive breakpoints where sidebar needs to collapse.

**When NOT to use**: Desktop — almost never. If you have room to show the nav, show it. Nielsen Norman Group found that hiding navigation cuts content discoverability by nearly half (179 participants, six sites). As the primary mobile navigation when you have 3-5 destinations (use bottom nav instead).

**Anti-patterns**:
- Hamburger as the only navigation on desktop (discoverability killer)
- Hamburger + bottom nav + sidebar all on the same screen
- Navigation panel with no close mechanism other than the hamburger icon
- Important actions hidden inside the hamburger (users don't explore menus they can't see)
- Animated hamburger-to-X transition that takes > 300ms (feels sluggish)

**Accessibility**:
- Button with `aria-label="Open menu"` / `"Close menu"` (toggled)
- `aria-expanded="true/false"` on the button
- `aria-controls` pointing to the nav panel
- Focus trap when menu is open
- Escape closes menu, focus returns to hamburger button

**Benchmark**: Airbnb mobile — hamburger for secondary items, primary nav is bottom bar and contextual. Apple.com mobile — clean slide-down, well-categorized.

### 1.8 Pagination

**What it is**: Controls for navigating through pages of content. The classic solution for large data sets.

**Anatomy**: Previous/Next buttons | Page number links | Current page indicator | Optional: first/last, items-per-page selector, total count.

**Variants**:
- **Numbered**: Shows page numbers. Best for search results where users may want to jump to a specific page.
- **Previous/Next only**: Minimal. Good for article sequences, blog archives.
- **Load more button**: Single button at the bottom of content. Hybrid between pagination and infinite scroll. Instagram web uses this.
- **Cursor-based**: API-driven, uses cursor tokens instead of page numbers. Better for real-time data. Shows "Load more" or auto-loads.

**When to use**: Search results, data tables, product listings, any discrete content set where users need to know their position and total.

**When NOT to use**: Feeds/timelines (use infinite scroll). Content that benefits from continuous flow. Mobile-first experiences where tap-to-load-more feels more natural.

**Anti-patterns**:
- Showing all page numbers for hundreds of pages (truncate with ellipsis)
- No current page indicator
- Page links too small for touch (< 44px)
- Pagination that reloads the entire page instead of updating content
- No items-per-page option on data-heavy tables

**Accessibility**:
- `<nav aria-label="Pagination">`
- `aria-current="page"` on active page
- Previous/Next buttons with clear labels (not just arrows)
- Disabled state for Previous on first page, Next on last page: `aria-disabled="true"`

**Benchmark**: Google Search — the canonical pagination. Shopify admin tables — clean, with items-per-page.

### 1.9 Infinite Scroll / Virtualized List

**What it is**: Content loads continuously as the user scrolls. No explicit "next page" action required.

**Anatomy**: Content feed | Loading indicator at bottom | Optional: scroll-to-top button | Optional: "You're all caught up" terminus.

**Variants**:
- **True infinite**: No end. Social feeds (Twitter/X, Instagram, TikTok). Designed for engagement.
- **Bounded infinite**: Loads until content exhausted, then shows terminus. E-commerce search, email inboxes.
- **Windowed/virtualized**: Only renders visible items plus a buffer. Essential for lists > 1000 items. react-window, react-virtuoso, TanStack Virtual.
- **Bidirectional**: Loads content above and below current position. Chat interfaces, email threads.

**When to use**: Social feeds, messaging, email, activity logs. Content where sequential consumption is natural and position doesn't matter.

**When NOT to use**: Search results where users need to find a specific item (they can't bookmark a position). Content where users need to reach the footer (infinite scroll blocks it). E-commerce where users want to compare specific items across pages.

**Anti-patterns**:
- No loading indicator (user doesn't know more content is coming)
- Blocking the footer (user can never reach it — put critical footer links elsewhere)
- No way to return to a previous position after navigating away
- Loading content that pushes the scrollbar position (janky scroll)
- Not virtualizing large lists (rendering 10K DOM nodes destroys performance)

**Accessibility**:
- New content announced via `aria-live="polite"` region
- Loading state: `aria-busy="true"` on the container
- Provide an alternative: pagination or "Load more" button for users who can't scroll
- Focus management: new content should not steal focus
- Virtual lists must maintain correct tab order and not skip focusable items

**Benchmark**: Twitter/X — smooth bidirectional scroll, "New posts" indicator, scroll position preservation. Linear — virtualized issue lists handle thousands of items.

### 1.10 Stepper / Wizard Navigation

**What it is**: A numbered or labeled sequence of steps that guides users through a multi-step process. The step indicator shows progress and remaining steps.

**Anatomy**: Step indicators (numbers or icons) | Step labels | Connector lines between steps | Current/completed/upcoming visual states | Next/Back navigation buttons.

**Variants**:
- **Horizontal stepper**: Steps displayed left to right. Standard for desktop forms with 3-7 steps.
- **Vertical stepper**: Steps stacked vertically with content inline. Good for long forms on mobile or when each step has variable content length.
- **Progress bar stepper**: Steps shown as segments of a progress bar. Simpler visual, less precise. Typeform uses this approach.
- **Non-linear stepper**: Users can click any step to jump to it (if previous steps are valid). Used for configuration wizards where order doesn't matter.
- **Micro-stepper**: Dots or dashes showing position in a carousel or short sequence. Onboarding screens.

**When to use**: Checkout flows, account setup, onboarding, multi-page forms, configuration wizards. Any process with 3-7 distinct steps.

**When NOT to use**: Single-page forms (overkill). Processes with variable/conditional paths that would make the step count misleading. More than 7 steps (reconsider the architecture — chunk into sub-flows).

**Anti-patterns**:
- Steps without labels (just numbers — user doesn't know what's ahead)
- No back button (trapping the user — H3 violation)
- Losing data when user navigates back (destructive)
- Step indicator that doesn't show total steps (user doesn't know how much is left)
- Step labels that change after the user has passed them (breaks mental model)

**Accessibility**:
- `aria-label="Progress"` on the step container
- Current step: `aria-current="step"`
- Completed steps: visually distinct + screen reader text "Completed"
- `role="list"` with `role="listitem"` for step indicators
- Step navigation buttons: clear labels ("Continue to Payment", not just "Next")

**Benchmark**: Stripe Checkout — 3 steps, clear labels, back navigation, step indicator with completion state. Shopify checkout — clean stepper, mobile-optimized.

### 1.11-1.28 Additional Navigation Patterns

**1.11 Anchor/Section Navigation**: In-page links that scroll to sections. Common on long-form pages, documentation, and landing pages. Sticky sidebar or top bar variant. Must update URL hash for shareability.

**1.12 Back Button / Return Navigation**: System back vs. contextual back. Mobile: swipe gesture (iOS) or system back (Android). Web: browser back vs. in-app back link. Never override browser back behavior.

**1.13 Search Navigation**: Search-first navigation where search is the primary way to find content. Algolia-style instant search. Google, Spotify, Amazon. Must handle zero results gracefully.

**1.14 Card Navigation**: Grid of cards acting as navigation targets. Dashboards, home screens, category selectors. Each card is a link. Must have clear hover/focus states.

**1.15 Dropdown Navigation**: Select-style dropdown for switching between contexts (workspaces, accounts, projects). Not a form input — a navigation control. GitHub repo selector, Slack workspace switcher.

**1.16 Floating Action Button (FAB)**: Android Material pattern. Single prominent action floating above content. The primary creation action. Only one FAB per screen. Extended FAB includes a label. Avoid on iOS — not a platform convention.

**1.17 Quick Actions / Speed Dial**: FAB that expands into multiple actions on tap. Material Design pattern. Use sparingly — more than 6 options defeats the purpose.

**1.18 Contextual Toolbar**: Appears when user selects content or enters a mode. Text formatting bars, multi-select action bars, image editing tools. Must be dismissable.

**1.19 Navigation Rail**: Narrow vertical bar with icon + label navigation items. Material Design pattern for tablets and medium screens. The desktop equivalent of bottom nav.

**1.20 Gesture Navigation**: Swipe to navigate between views/tabs. iOS standard (swipe back, swipe between tabs). Must have visible affordances — users can't discover invisible gestures.

**1.21 Notification/Activity Navigation**: Bell icon leading to a feed of updates. The notification center pattern. Badge count for unread. Dropdown panel or separate page.

**1.22 Avatar/Account Menu**: Profile picture/initials triggering a dropdown with account settings, preferences, and sign out. Universal pattern. Always includes sign out.

**1.23 Timeline Navigation**: Navigating content by time axis. Horizontal or vertical. Calendar views, history, changelogs. Time scrubber pattern for video/audio.

**1.24 Map Navigation**: Spatial navigation on a map. Zoom, pan, tap markers, search on map. Airbnb, Google Maps, Uber. Unique accessibility challenges.

**1.25 Keyboard Shortcut System**: Not visual navigation but a navigation layer. "?" to show shortcut list. Common in productivity apps. Must be discoverable, overridable, and not conflict with browser/OS shortcuts.

**1.26 Progressive Navigation**: Navigation options that reveal progressively as user scrolls or interacts. "As you read more, more options appear." Used in article/content apps. Medium's contextual toolbar.

**1.27 A-Z / Index Navigation**: Alphabetical index for jumping through a sorted list. Contact lists, glossaries. The scrubber on the right of iOS contact lists. Touch target must be generous.

**1.28 Multi-Level Drill-Down**: Hierarchical navigation where tapping an item reveals its children, pushing the current view offscreen. iOS Settings app. File managers. Each level must have a clear back path.

---

## Category 2: Data Display Patterns (32 patterns)

How you display data determines whether users understand it. The same data presented in a table, a card, a chart, or a list tells a completely different story and enables completely different actions. Choosing the wrong display pattern is one of the most expensive UX mistakes — it makes your app feel "hard to use" even when all the data is technically there.

### 2.1 Data Table

**What it is**: Rows and columns displaying structured data. The most information-dense display pattern. The backbone of every admin panel, CRM, and analytics tool.

**Anatomy**: Column headers (sortable) | Data rows | Optional: row selection, row actions, inline editing, pagination/infinite scroll, column resizing, row expansion.

**Variants**:
- **Basic/static**: Read-only display. Reports, invoices, logs.
- **Interactive**: Sortable, filterable, searchable. Standard for admin panels.
- **Editable**: Inline editing on click/double-click. Spreadsheet-like. Airtable, Notion tables.
- **Expandable rows**: Click a row to reveal detail panel below. Complex data that doesn't fit columns.
- **Sticky header/first column**: Headers stay visible on scroll. Essential for wide tables.
- **Responsive/stacked**: Columns stack vertically on narrow viewports. Each row becomes a card-like block.
- **Virtualized**: Only renders visible rows. Required for 1000+ rows. TanStack Table, AG Grid.
- **Tree table**: Hierarchical rows with expand/collapse. File system views, org charts.

**When to use**: Structured data with 3+ attributes that users need to scan, sort, filter, or compare. Admin panels, analytics, CRMs, inventory, financial data.

**When NOT to use**: Fewer than 3 columns or 5 rows (overkill — use a list). Non-tabular data. Mobile-first experiences (tables are inherently wide). Content that users browse rather than analyze.

**Anti-patterns**:
- No sorting on any column (users expect to sort)
- Horizontal scroll without a sticky first column (context lost)
- Row actions hidden in a menu when there are only 1-2 actions (just show them)
- No empty state when filters produce zero results
- Alternating row colors with insufficient contrast
- Column headers that truncate without tooltips
- Editable cells with no visual edit affordance

**Accessibility**:
- Semantic `<table>`, `<thead>`, `<tbody>`, `<th>`, `<td>`
- `scope="col"` on column headers
- Sortable headers: `aria-sort="ascending"` / `"descending"` / `"none"`
- Row selection: `aria-selected="true"`, announced count
- Inline editing: `role="gridcell"` when editable, clear focus states
- Responsive stacked view: maintain data association (label + value pairs)

**Benchmark**: Stripe Dashboard tables — sortable, filterable, clean density, excellent empty states. Airtable — the pinnacle of editable tables. Linear — minimal, focused, fast.

### 2.2 Card / Content Card

**What it is**: A contained unit of content and actions presented as a distinct visual block. Cards are the atoms of modern UI — flexible, composable, and universally understood.

**Anatomy**: Container (border/shadow/background) | Header area (title, subtitle, metadata) | Media area (image, video, chart) | Body content | Action area (buttons, links).

**Variants**:
- **Basic content card**: Title + description + CTA. Blog post previews, feature lists.
- **Media card**: Prominent image/video + minimal text. E-commerce products, portfolios, social posts.
- **Stat card**: Single prominent metric + trend indicator + label. Dashboard KPIs. Mercury, Ramp.
- **Action card**: Card that is itself a button/link. Navigation cards, selection cards. Entire card is clickable.
- **Profile card**: Avatar + name + role + contact actions. Team directories, user mentions.
- **Pricing card**: Plan name + price + feature list + CTA. Pricing pages. The most A/B tested UI pattern in existence.
- **Interactive card**: Expandable, draggable, or with inline editing. Trello/Kanban cards.
- **Horizontal card**: Image left, content right. Compact layout for lists. Search results.
- **Bento card/grid**: Asymmetric grid of cards with varying sizes. Apple's marketing trend. Visual impact but harder to scan systematically.

**When to use**: Collections of similar items that need visual separation. Product listings, dashboards, galleries, team directories, any "grid of things."

**When NOT to use**: Homogeneous data that should be a table (cards waste space for tabular data). Single items (a card around one thing adds unnecessary visual noise). Deeply nested content (cards within cards within cards = matryoshka syndrome).

**Anti-patterns**:
- Cards with inconsistent heights in a grid (jagged layout)
- Clickable cards with clickable elements inside (nested interaction — confusing click targets)
- Too many actions per card (> 3 — the card becomes a miniature page)
- Cards without clear boundaries (floating content — is this one item or two?)
- Card shadows so heavy they compete with the content

**Accessibility**:
- If the entire card is a link: single `<a>` wrapper or `<article>` with a heading link
- Multiple actions in a card: each must be individually focusable and labeled
- Card images: meaningful `alt` text or `alt=""` for decorative
- Card grids: use CSS Grid with logical source order matching visual order
- `<article>` element for self-contained cards with headings

**Benchmark**: Airbnb listing cards — perfect hierarchy (image > price > title > metadata > rating). Stripe's dashboard stat cards — clean metric + trend + context.

### 2.3 List / Feed

**What it is**: Vertical sequence of items, each containing key information and optional actions. The most natural display for sequential or chronological content.

**Anatomy**: List items (consistent structure) | Dividers or spacing between items | Optional: avatars/icons, timestamps, status indicators, swipe actions.

**Variants**:
- **Simple list**: Text-only items. Settings pages, menus, selection lists.
- **Rich list**: Multi-line items with avatar, title, subtitle, metadata, and trailing action. Email, messaging, contact lists.
- **Interactive list**: Swipeable items (iOS mail), long-press for context menu, drag to reorder. Task lists, playlists.
- **Grouped list**: Items grouped by category with section headers. iOS Settings style. Alphabet-grouped contacts.
- **Timeline/activity list**: Chronological items with timestamps and a connecting line. Activity feeds, changelogs, order history.
- **Virtualized list**: Windowed rendering for large datasets. 10K+ items. react-window, iOS UITableView reuse.

**When to use**: Sequential content, chronological data, user-generated content feeds, settings, any list of homogeneous items where vertical scanning is natural.

**When NOT to use**: Data with many attributes to compare side-by-side (use a table). Visual content where images dominate (use a grid of cards). Small collections where a grid layout would be more scannable.

**Anti-patterns**:
- Lists without any visual divider or spacing (wall of text)
- List items with inconsistent structure (some have icons, some don't)
- No empty state for lists with zero items
- Swipe actions with no visual hint that they exist (undiscoverable)
- Long lists without any virtualization (performance death)
- List items that don't respond to tap/click in any way (feels broken)

**Accessibility**:
- Semantic `<ul>` or `<ol>` (or `role="list"`)
- Interactive items: focusable with clear focus indicator
- Grouped lists: `role="group"` with `aria-labelledby` pointing to section header
- Swipe actions: must have a visible alternative (long-press menu or visible button)
- Drag-to-reorder: keyboard alternative (grab with Space, move with arrows, drop with Space)

**Benchmark**: Apple Mail — rich list with swipe actions and grouped by date. Linear issues list — clean, dense, keyboard-first. Notion's page list — flexible, drag-to-reorder.

### 2.4 Chart / Data Visualization

**What it is**: Graphical representation of data using visual encoding (position, length, angle, color, area) to reveal patterns, trends, and outliers.

**Anatomy**: Chart area | Axes with labels and scales | Data marks (bars, lines, points, areas) | Legend | Tooltip on hover | Optional: annotations, reference lines, interactive filters.

**Variants**:
- **Line chart**: Trends over time. Revenue, users, performance. The most common dashboard chart.
- **Bar chart**: Comparison between categories. Horizontal for long labels, vertical for time-based.
- **Pie/donut chart**: Part-of-whole composition. Use sparingly — humans are bad at comparing angles. Max 5-7 segments.
- **Area chart**: Like line chart but filled. Good for showing volume/magnitude over time. Stacked area for composition.
- **Scatter plot**: Relationship between two variables. Correlation analysis. Less common in product UI.
- **Sparkline**: Tiny chart without axes, embedded inline in a table or card. Shows trend at a glance. Stripe, Robinhood.
- **Heatmap**: Color-coded matrix. Activity calendars (GitHub), time-based usage, geographic data.
- **Gauge/radial**: Single metric as percentage of a whole. Health scores, progress, capacity. Use for single-metric dashboards.
- **Funnel chart**: Sequential stages with drop-off. Conversion analysis. Sales pipelines.
- **Sankey diagram**: Flow and proportions between categories. User flow analysis, budget allocation.

**When to use**: Quantitative data where visual pattern recognition is more efficient than reading numbers. Dashboards, analytics, reports, financial data.

**When NOT to use**: Exact values needed (use a table). Fewer than 3 data points (use a stat card with a number). When the visual encoding makes the data harder to interpret, not easier.

**Anti-patterns**:
- Pie charts with more than 7 segments
- Y-axis not starting at zero for bar charts (exaggerates differences)
- 3D charts (distort perception — always use 2D)
- No tooltip on data points (user can't get exact values)
- Color as the only encoding (inaccessible to color-blind users)
- Chart without a title explaining what it shows
- Dual y-axes (confusing — use two separate charts)

**Accessibility**:
- `role="img"` with descriptive `aria-label` summarizing the chart's key insight
- Data table alternative: provide a "View as table" toggle for all charts
- Color: use patterns/shapes in addition to color (stripe, dot, dash for lines)
- Keyboard: interactive charts must support Tab to data series, arrows between points
- Announce significant changes: `aria-live` region for real-time updating charts

**Benchmark**: Stripe Dashboard charts — clean, interactive, consistent. Observable — the gold standard for data visualization. Robinhood — sparklines that tell a story at a glance.

### 2.5 Badge / Tag / Chip

**What it is**: Small UI element that communicates status, category, count, or attribute. One of the most versatile micro-patterns.

**Anatomy**: Container (pill or rectangle) | Label text | Optional: icon, count, dismiss button, avatar.

**Variants**:
- **Status badge**: Color-coded indicator (green/red/yellow/blue). "Active", "Pending", "Failed". Used in tables, lists, cards.
- **Notification badge**: Small dot or count overlay on an icon. Unread count. Red is conventional.
- **Tag/label**: Categorization chip. "Feature", "Bug", "Enhancement" in issue trackers. Often color-coded.
- **Filter chip**: Toggleable filter. Material Design pattern. Selected state = filled.
- **Input chip**: Represents a selected value that can be removed. Email "To" field recipients, tag inputs.
- **Action chip**: Chip that triggers an action. "Share", "Save", "Rate" in Material Design.

**When to use**: Status indication, categorization, filtering, selected values, notification counts. Everywhere — badges are universal.

**When NOT to use**: Long text content (badges should be 1-3 words). Primary actions (use buttons). Critical error messages (use alerts, not badges).

**Anti-patterns**:
- Color as the only differentiator (inaccessible)
- Too many badge types on one screen (visual noise)
- Badge text that truncates (keep it short)
- Notification badges with no way to clear them
- Red badges for non-critical information (red = urgent)

**Accessibility**:
- Status badges: screen reader text must convey meaning, not just color ("Status: Active")
- Notification count: `aria-label="3 unread notifications"` on the icon
- Dismissible chips: dismiss button with `aria-label="Remove [tag name]"`
- Color + icon + text: triple encoding for status (never color alone)

**Benchmark**: Linear's status chips — color + icon + label, always accessible. GitHub labels — rich color system with good contrast. Slack's notification badges — subtle but clear.

### 2.6 Avatar / Profile Image

**What it is**: Circular or rounded-square image representing a user, team, or entity. The visual anchor for identity throughout a product.

**Anatomy**: Image container (circle or rounded square) | Fallback: initials on colored background | Optional: presence indicator (green dot), badge overlay, size variants.

**Variants**:
- **Single avatar**: One user/entity. Profile headers, comment authors, assignees.
- **Avatar group/stack**: Overlapping row showing multiple users. "3 people are editing." Figma, Google Docs.
- **Avatar with status**: Online/offline/busy/away indicator. Slack, Teams. Green dot = online is universal.
- **Avatar with badge**: Notification count or role badge overlaid. Admin crown, verified checkmark.

**When to use**: Anywhere a user or entity needs visual identification. User menus, comment threads, assignee fields, team lists, chat.

**Anti-patterns**:
- No fallback for missing images (broken image icon)
- Initials fallback with poor contrast against background
- Avatar group showing 10+ overlapping (unreadable — show 3-5 + "+N")
- Square avatars in a product that otherwise uses circles (consistency)

**Accessibility**:
- `alt="[User name]"` on image, or `alt=""` if name is shown adjacent
- Presence indicator: not just color — include `aria-label="Online"` text
- Avatar group: `aria-label="Assigned to: Alice, Bob, and 3 others"`

**Benchmark**: Slack's avatars — presence indicator, status emoji, consistent. GitHub's avatars — clean fallback, hover reveals full profile.

### 2.7 Stat / Metric Display

**What it is**: A prominent number with label and context. The building block of every dashboard.

**Anatomy**: Metric value (large, prominent) | Label/description | Trend indicator (arrow + percentage) | Comparison context (vs. last period) | Optional: sparkline.

**Variants**:
- **Simple stat**: Number + label. "2,847 Users".
- **Stat with trend**: Number + label + up/down arrow + percentage. "Revenue $42.5K (+12.3%)".
- **Stat with sparkline**: Number + tiny chart showing recent trend. Stripe, Mercury.
- **Stat with comparison**: Current vs. previous period side by side.
- **Goal stat**: Progress toward a target. Progress bar or ring + current/target numbers.
- **Live stat**: Animating/counting up in real-time. Real-time dashboards, launch counters.

**When to use**: Dashboard KPIs, analytics overview, report headers. Any time a single number is the primary information.

**When NOT to use**: When the trend matters more than the number (use a chart instead). When comparing many metrics against each other (use a table).

**Anti-patterns**:
- Number without label (what does "2,847" mean?)
- Trend without time context ("+12.3%" — compared to what?)
- Green/red for trend without secondary encoding (add arrows too)
- Too many stats competing for attention (no hierarchy — everything is "important")
- Decimal precision that implies false accuracy ("$42,518.37" when the real margin of error is thousands)

**Accessibility**:
- `aria-label` on stat group: "Revenue: $42,500, up 12.3% from last month"
- Trend colors + icons (not color alone)
- Live updating stats: `aria-live="polite"` or "off" if updates are frequent

**Benchmark**: Stripe Dashboard — stat cards with sparklines, clean hierarchy. Mercury — bold numbers, subtle trends, grouped logically. Plausible Analytics — minimal, honest metrics.

### 2.8-2.32 Additional Data Display Patterns

**2.8 Accordion / Expandable Section**: Header + collapsible content. FAQs, settings sections, grouped content. `<details>/<summary>` in HTML. `aria-expanded` on trigger.

**2.9 Tooltip**: Hover/focus-triggered information popup. Definitions, truncated text, context. Must not contain interactive elements (use popover). Delay 300-500ms on hover. `role="tooltip"`, `aria-describedby`.

**2.10 Popover / Info Card**: Click-triggered floating panel with rich content. Profile previews, contextual details. Unlike tooltips, can contain interactive elements. `aria-haspopup`, focus trap.

**2.11 Modal / Dialog**: Overlay that blocks background interaction. Confirmations, forms, important messages. Must have focus trap, Escape to close, focus return. `role="dialog"`, `aria-modal="true"`.

**2.12 Drawer / Sheet**: Panel that slides in from an edge. Detail views, filters, settings. Bottom sheet on mobile (iOS/Android native). Less disruptive than modals for secondary content.

**2.13 Carousel / Slider**: Horizontal sequence of content panels with navigation. Product images, testimonials, feature highlights. Auto-advance is an anti-pattern (users can't control pace). Must be keyboard navigable with arrow keys. `role="region"`, `aria-roledescription="carousel"`.

**2.14 Gallery / Image Grid**: Grid of images with optional lightbox on click. Products, portfolios, photo libraries. Pinterest-style masonry variant. Lazy loading essential.

**2.15 Tree View**: Hierarchical expandable list. File explorers, org charts, nested categories. `role="tree"`, `role="treeitem"`, `aria-level`, `aria-expanded`. Keyboard: arrows for navigation, Enter for expand/collapse.

**2.16 Kanban Board**: Columns representing stages, cards that can be dragged between them. Trello, Linear, Notion boards. Drag-and-drop with keyboard alternative. Column = `role="group"`, cards within.

**2.17 Calendar View**: Date grid with events/data. Month, week, day, agenda views. Google Calendar, Cal.com. Complex accessibility — `role="grid"`, arrow key navigation between days.

**2.18 Map Display**: Geographic visualization with markers, clusters, and info windows. Airbnb, Uber, Google Maps. Must have non-map alternative for accessibility. `role="application"` with keyboard controls.

**2.19 Timeline / History**: Vertical or horizontal sequence of dated events connected by a line. Activity logs, order tracking, changelogs. Each event is a node on the line.

**2.20 Empty State**: What's shown when there is no data to display. The most neglected pattern. Must include: explanation, illustration (optional), primary action to populate. Never show a blank screen.

**2.21 Error State**: What's shown when something fails. Error code/message, explanation in human language, recovery action. Never show raw error messages or stack traces. Always offer a path forward.

**2.22 Skeleton Screen**: Placeholder shapes mimicking the layout of real content during loading. Pulse animation. Better than spinner because it sets spatial expectations. Facebook pioneered, now universal.

**2.23 Loading Spinner / Progress**: Indeterminate (spinner) vs. determinate (progress bar). Use determinate when you know the percentage. Spinner only when duration is unknown and < 10 seconds. > 10 seconds: show progress or skeleton.

**2.24 Notification / Alert Banner**: Full-width or inline banner for system messages. Info, warning, error, success types. Dismissible or persistent based on severity. `role="alert"` for urgent, `role="status"` for informational.

**2.25 Toast / Snackbar**: Temporary notification that auto-dismisses. Action confirmations, non-critical updates. Bottom or top of screen. 3-5 second duration. Must have dismiss button. `role="status"`, `aria-live="polite"`.

**2.26 Progress Bar / Steps Indicator**: Linear or segmented bar showing completion progress. Profile completeness, upload, multi-step forms. Determinate with percentage or step count.

**2.27 Divider / Separator**: Horizontal or vertical line separating content sections. Subtle but essential for grouping (Gestalt). `<hr>` or `role="separator"`. Can be decorative (`role="none"`).

**2.28 Overflow Menu / More Actions**: "..." or "kebab" icon revealing additional actions in a dropdown. Used when space is limited. Maximum 7 items (Hick's Law). Destructive actions at the bottom, visually distinct.

**2.29 Ribbon / Highlight Label**: Diagonal or horizontal label overlaying a card corner. "New", "Sale", "Popular". E-commerce, product cards. Use sparingly — more than 2 per page dilutes impact.

**2.30 Count / Counter**: Animated number that increments/decrements. Social proof ("1,234 people viewing"), real-time metrics, gamification points.

**2.31 Comparison Table**: Side-by-side feature comparison. Pricing pages, product specs. Sticky header row, checkmarks for features, highlighted recommended column. Responsive: stack or scroll.

**2.32 Code Block / Syntax Display**: Formatted code with syntax highlighting, copy button, language label. Developer tools, documentation, API references. Use monospace font, line numbers optional.

---

## Category 3: Input & Form Patterns (27 patterns)

Forms are where value is exchanged. Every form field is a question, and every question has a cognitive cost. The patterns here determine whether users complete the form or abandon it.

### 3.1 Text Input

**What it is**: Single-line text entry field. The most fundamental input pattern.

**Anatomy**: Label (above or floating) | Input field | Placeholder text (optional, controversial) | Helper text (below) | Error message (below, replaces helper) | Optional: icon (leading/trailing), character count, clear button.

**Variants**:
- **Standard**: Label above, input below. The most accessible and scannable layout.
- **Floating label**: Label starts as placeholder, floats above on focus. Material Design popularized this. Saves space but has accessibility concerns (the label becomes smaller and lighter when floated).
- **Inline/borderless**: No visible border until focus. Clean aesthetic for forms embedded in content. Notion's inline editing. Must have clear focus state.
- **With icon**: Leading icon for context (search icon, email icon). Trailing icon for action (clear, toggle visibility).
- **With prefix/suffix**: Static text before/after input. "https://", ".com", "$", "kg". Use `<span>` not placeholder.

**When to use**: Any text data entry. Names, emails, search, URLs, short answers.

**When NOT to use**: Long-form text (use textarea). Selection from known options (use select/radio/checkbox). Dates, times, numbers with specific formats (use dedicated inputs).

**Anti-patterns**:
- Placeholder as the only label (disappears on input — user forgets what the field is for)
- No visible label (WCAG failure)
- Red border without error message (color alone is insufficient)
- Error message that appears while user is still typing (premature validation)
- Autocomplete disabled for standard fields (browsers know best — let them autofill)
- Input field width that doesn't hint at expected content length (a zip code field shouldn't be 400px wide)

**Accessibility**:
- `<label>` explicitly associated with `<input>` via `for`/`id`
- Error state: `aria-invalid="true"`, `aria-describedby` pointing to error message
- Required: `aria-required="true"` or `required` attribute
- Helper text: `aria-describedby` pointing to the helper element
- Autocomplete: appropriate `autocomplete` attribute (name, email, tel, etc.)
- Minimum contrast: 4.5:1 for input text, 3:1 for placeholder, 3:1 for border

**Benchmark**: Stripe's form inputs — clear labels, excellent error states, smart autofill. Linear — minimal, focused, keyboard-first.

### 3.2 Search Input

**What it is**: Specialized text input for querying content. Distinguished from standard text input by its behavior: typically triggers results as-you-type, includes search icon, and has clear/cancel functionality.

**Anatomy**: Search icon (leading) | Input field | Clear/cancel button (trailing, appears when non-empty) | Keyboard shortcut hint (e.g., "/" or "Cmd+K") | Dropdown results panel.

**Variants**:
- **Inline search**: Search box embedded in the page. Persistent, always visible. Header search bars.
- **Expandable search**: Icon that expands to full input on click. Saves space. Appropriate when search is secondary.
- **Command palette search**: Full-screen or overlay search (see 1.6 Command Palette). The power-user variant.
- **Scoped search**: Dropdown to select search scope before typing. "Search in Projects" vs. "Search everywhere." GitHub code search.
- **Faceted search**: Search with filter chips/sidebar for refining results. E-commerce, job boards, property listings.

**When to use**: Any app with > 20 items of content. Search should be as prominent as the content it searches.

**When NOT to use**: Apps with < 10 items (just show them all). When filtering is sufficient (checkbox filters may be better than free-text search).

**Anti-patterns**:
- No instant results (requiring Enter to search feels broken in 2025)
- Search icon that is not clickable (users will click it)
- No recent searches or suggestions when input is empty
- Results that don't highlight the matching text
- Search that requires exact matches (fuzzy search is expected)

**Accessibility**:
- `role="search"` on the form or container
- `role="combobox"` when search shows results dropdown
- `aria-activedescendant` for keyboard-navigated results
- Clear button: `aria-label="Clear search"`
- Results count announced: "5 results for [query]"

**Benchmark**: Algolia — the gold standard for search UX. Raycast — instant, categorized. Spotify — search with scoped tabs (Songs, Artists, Playlists).

### 3.3 Select / Dropdown

**What it is**: Input that presents a list of predefined options for the user to choose from.

**Anatomy**: Trigger (button/input showing current selection) | Dropdown panel with options | Optional: search/filter within dropdown, group headers, selected indicator.

**Variants**:
- **Native select**: Browser `<select>` element. Minimal control over styling but perfect accessibility and mobile behavior. Use for simple cases.
- **Custom select**: Styled dropdown matching design system. Full visual control. Requires manual accessibility implementation.
- **Searchable select**: Includes a filter input in the dropdown. Essential when options > 10. react-select pattern.
- **Multi-select**: Multiple selections allowed. Selected items shown as chips. Tag selectors, permission pickers.
- **Combobox**: Combines free-text input with suggestion dropdown. User can type a new value or select existing. Autocomplete variant.
- **Grouped select**: Options organized under category headers. Countries grouped by continent. Permissions grouped by role.

**When to use**: 4-15 predefined options where only one (or a few) can be selected. When the options are too numerous for radio buttons.

**When NOT to use**: 2-3 options (use radio buttons — all options visible). Yes/no (use toggle/checkbox). Very long lists without search (use searchable select or combobox).

**Anti-patterns**:
- Dropdown with 100+ unsearchable options (country lists without search)
- Native select on desktop when design requires custom styling (but then reimplementing all a11y)
- Dropdown that opens upward and clips off screen
- No keyboard support for custom selects (the #1 custom select failure)
- Placeholder as label ("Select an option..." that disappears)

**Accessibility**:
- Native: `<select>` with `<label>` — inherently accessible
- Custom: `role="listbox"`, `role="option"`, `aria-selected`, `aria-expanded`
- Keyboard: Space/Enter to open, Arrow keys to navigate, Enter to select, Escape to close
- Type-ahead: typing a letter jumps to matching option
- Multi-select: announce selected count

**Benchmark**: Radix UI Select — accessible, customizable, composable. Headless UI Listbox — minimal, correct. GitHub's selectors — clean, fast, well-scoped.

### 3.4 Checkbox

**What it is**: A toggleable square control for binary (on/off) or multiple selection.

**Anatomy**: Square box (checked/unchecked/indeterminate) | Label text (clickable) | Optional: description text below label.

**Variants**:
- **Single checkbox**: Accept terms, opt-in. Binary choice.
- **Checkbox group**: Multiple checkboxes for multi-select. Toppings, features, permissions.
- **Indeterminate/mixed**: Parent checkbox partially checked when some children are. Tree-selection UI.
- **Switch/toggle variant**: When the checkbox represents an immediate setting change (not a form submission), prefer a toggle switch.

**When to use**: Binary yes/no for single checkbox. Multiple selections from a group of options. Opt-in/consent patterns.

**When NOT to use**: Mutually exclusive choices (use radio buttons). Immediate on/off settings (use toggle). Single binary in a form context where the action is ambiguous without reading the label carefully.

**Anti-patterns**:
- Pre-checked marketing consent checkboxes (dark pattern — user must opt-out)
- Label not clickable (only the tiny box is the target)
- Checkboxes that look like radio buttons (or vice versa)
- Required checkbox with no indication it's required until form submission fails

**Accessibility**:
- `<input type="checkbox">` with associated `<label>`
- Indeterminate: `aria-checked="mixed"` (set via JavaScript)
- Group: wrap in `<fieldset>` with `<legend>`
- Error: `aria-invalid="true"`, `aria-describedby` for error message

**Benchmark**: Radix UI Checkbox — clean, animated check, indeterminate support. Apple's iOS checkmarks — minimal, clear.

### 3.5 Radio Button

**What it is**: A group of mutually exclusive options where selecting one deselects all others.

**Anatomy**: Circle indicator (filled when selected) | Label text (clickable) | Optional: description below each option. Group label above the set.

**Variants**:
- **Standard radio group**: Vertical stack of options. 2-5 choices.
- **Card radio**: Each option is a card with radio indicator. Richer visual, good for plans/pricing.
- **Segmented control**: Horizontal pill-shaped buttons where selecting one deselects others. iOS standard. Used for 2-4 options.
- **Icon radio**: Each option is represented by an icon (e.g., layout options, theme selection).

**When to use**: 2-5 mutually exclusive options where all should be visible simultaneously. The user needs to compare options before choosing.

**When NOT to use**: More than 7 options (use a select dropdown). Non-exclusive choices (use checkboxes). Binary toggle (use switch for on/off).

**Anti-patterns**:
- No default selection in a radio group (force the user to choose — or make it clear none is selected)
- Radio buttons that allow deselection (violates radio button contract — use checkboxes if deselection needed)
- Radio group without a group label (what is the question?)
- Options that are too similar to differentiate (rewrite the options)

**Accessibility**:
- Wrap in `<fieldset>` with `<legend>` as the group label
- `<input type="radio">` with same `name` attribute within group
- Keyboard: Arrow keys to move between options (auto-select), Tab to enter/exit group
- Each `<input>` associated with `<label>` via `for`/`id`

**Benchmark**: Stripe Checkout's payment method radios — card-style, clear selection, visual feedback.

### 3.6 Toggle / Switch

**What it is**: A binary control that immediately toggles a setting between on and off states.

**Anatomy**: Track (background) | Thumb (sliding indicator) | On/off labels (optional but recommended) | State change is immediate (no submit button needed).

**Variants**:
- **Standard toggle**: Simple on/off. Settings pages.
- **Toggle with label**: On/off state described in adjacent text. "Dark mode: On".
- **Toggle with confirmation**: Requires confirmation for destructive toggles. "Disable notifications? This will..."
- **Toggle group**: Multiple toggles with related settings. Notification preferences.

**When to use**: Immediate binary settings. "Enable/disable", "on/off". When the change takes effect immediately without a form submission.

**When NOT to use**: Form submissions (use checkbox — user expects to "Save" to apply). When the two states aren't clearly opposite. When more than two options exist.

**Anti-patterns**:
- Toggle without visible state label (is it on or off? The slider position is ambiguous for some users)
- Toggle change without feedback (did it save? Confirm with a toast or inline message)
- Destructive toggle without confirmation (toggling off account protection should confirm)
- Toggle that requires a separate "Save" button (contradicts the toggle mental model)

**Accessibility**:
- `role="switch"` with `aria-checked="true/false"`
- Visible text label: always describe what the toggle controls
- State change announced by screen reader automatically with `role="switch"`
- Sufficient track/thumb contrast in both states

**Benchmark**: iOS Settings toggles — universally understood, clear green/gray states. Linear's notification toggles — clean, immediate, with subtle animation.

### 3.7 Date Picker

**What it is**: A specialized input for selecting dates (and optionally times). One of the most complex form patterns.

**Anatomy**: Input field showing selected date | Calendar popup | Month/year navigation | Day grid | Optional: time selector, range selection, presets ("Today", "Last 7 days").

**Variants**:
- **Single date**: Calendar popup for one date. Birthdays, appointments.
- **Date range**: Two dates (start/end) with visual range on calendar. Hotel bookings, report periods. Airbnb date picker is the benchmark.
- **Date + time**: Calendar plus time input. Event creation, scheduling.
- **Relative date presets**: Quick buttons for "Today", "Yesterday", "Last 7 days", "This month". Analytics date filters. Often combined with custom range.
- **Inline calendar**: Always-visible calendar, no popup. Scheduling interfaces, availability views.
- **Native date input**: `<input type="date">`. Limited styling but good mobile experience (native date picker).

**When to use**: Any date entry. Always prefer a picker over asking users to type dates in a specific format.

**When NOT to use**: When the date is "today" or "now" (just use a button/toggle, don't make users pick today from a calendar). When a relative time is more natural ("2 hours from now").

**Anti-patterns**:
- Requiring a specific date format in a text field with no picker
- Calendar that defaults to January 1, 1970 for birthdate entry (default to a reasonable date)
- Year selection that requires clicking through months (for birthdates, provide year dropdown or scrollable year)
- No keyboard navigation within the calendar grid
- Date range picker with no visual indication of the selected range on the calendar

**Accessibility**:
- Calendar grid: `role="grid"`, `role="row"`, `role="gridcell"`
- Arrow keys for day navigation, PageUp/PageDown for month, Home/End for week start/end
- Selected date: `aria-selected="true"`
- Today: `aria-current="date"`
- Input: `aria-label` describing expected format

**Benchmark**: Airbnb's date range picker — smooth, visual range, excellent mobile experience. Cal.com — clean, accessible, good keyboard support.

### 3.8 File Upload

**What it is**: Controls for selecting and uploading files from the user's device.

**Anatomy**: Drop zone (drag-and-drop area) | File browser button | Accepted formats text | Upload progress | File list with preview, name, size, remove action.

**Variants**:
- **Simple button**: Click to open file browser. Minimal footprint.
- **Drag-and-drop zone**: Dashed border area that accepts dropped files. Visual feedback on drag-over.
- **Drag-and-drop + button**: Combined. The standard for modern upload patterns.
- **Inline/avatar upload**: Click on an avatar or image to replace it. Camera icon overlay.
- **Multi-file**: Supports multiple selections. Progress per file. Reorder capability.
- **Chunked/resumable**: Large file upload with resume on failure. Uses tus or similar protocol.

**When to use**: Any file input scenario. Profile pictures, document submissions, media uploads.

**When NOT to use**: When the data can be entered via forms instead (don't make users create and upload a file for data that could be typed).

**Anti-patterns**:
- No file type validation until after upload (validate on selection)
- No progress indicator for uploads > 1 second
- No preview for image uploads
- Maximum file size not communicated before upload fails
- Upload that resets the form on failure

**Accessibility**:
- `<input type="file">` as the base (visually hidden if custom UI, but still present)
- Drop zone: `role="button"` or `role="region"` with `aria-label="Drop files here or click to upload"`
- Upload progress: `role="progressbar"`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax`
- File list: each file with name, size, and remove button (`aria-label="Remove [filename]"`)

**Benchmark**: Dropbox upload — smooth, clear progress, preview. Vercel's deployment drop zone — clean, informative.

### 3.9-3.27 Additional Input & Form Patterns

**3.9 Textarea / Rich Text Editor**: Multi-line text input. Basic: `<textarea>` with character count. Rich: toolbar with formatting (bold, italic, links). Markdown editors. Notion's block editor is the modern gold standard. TipTap, ProseMirror, Slate for React.

**3.10 Number Input**: Stepper (+/-) buttons or plain input with type="number". Currency, quantity, age. Input constraints (min, max, step). Don't use for phone numbers, zip codes, or credit cards (use text input with formatting).

**3.11 Slider / Range Input**: Draggable handle on a track for selecting a value within a range. Price filters, volume, brightness. Must show current value. Dual-thumb for ranges. `role="slider"`, arrow key increments. Touch target: at least 44px for the thumb.

**3.12 Color Picker**: Hue/saturation/lightness picker. Design tools, theme customizers, branding. Predefined palette + custom input. Hex/RGB/HSL format toggle. Accessibility: must be keyboard operable with arrow keys.

**3.13 Tag / Token Input**: Text input that converts typed values into removable chips/tags. Email recipients, category tagging. Autocomplete suggestions. Backspace to remove last tag. `aria-describedby` for instructions.

**3.14 Autocomplete / Typeahead**: Input with suggestion dropdown populated as user types. Address fields, mention systems, search. Debounce input (200-300ms). Highlight matching text in suggestions. `role="combobox"`, `aria-autocomplete`.

**3.15 Password Input**: Text input with masked characters and visibility toggle. Strength indicator. Requirements checklist. "Show password" button with `aria-label`. Never disable paste. Never impose arbitrary length maximums.

**3.16 OTP / Verification Code Input**: 4-6 individual digit boxes for one-time passwords. Auto-advance on input. Paste support for the full code. `autocomplete="one-time-code"`. Mobile: `inputmode="numeric"`.

**3.17 Phone Number Input**: Country code selector + formatted phone number input. `autocomplete="tel"`. Use libphonenumber for validation. Country flag + code dropdown. International format support.

**3.18 Address Input**: Structured multi-field or single-field with autocomplete (Google Places, Mapbox). Country selector affects field layout (states vs. provinces vs. prefectures). `autocomplete` attributes: street-address, address-level1, postal-code, country.

**3.19 Credit Card Input**: Card number (with brand detection), expiry, CVC. Stripe Elements is the benchmark. Format as-you-type (4-4-4-4). Card brand icon updates dynamically. `autocomplete="cc-number"`, `cc-exp`, `cc-csc`.

**3.20 Rating Input**: Star/heart/emoji selection for feedback. 5-point scale is standard. Click or hover to select. Must be keyboard accessible (arrow keys). `role="radiogroup"` with `role="radio"` per star.

**3.21 Emoji Picker**: Grid of emoji with category tabs and search. Messaging, reactions, status. Virtual scroll for performance. Skin tone selection. `role="grid"` with keyboard navigation.

**3.22 Signature Input**: Canvas-based signature drawing or typed signature option. Legal documents, approvals. Touch and mouse support. Clear button. Export as image.

**3.23 Captcha / Bot Detection**: Challenge to verify human user. reCAPTCHA, hCaptcha, Turnstile. Invisible variant preferred (no user interaction unless suspicious). Accessibility: audio alternative, always.

**3.24 Multi-Step Form / Wizard**: Form broken into sequential steps. (See also 1.10 Stepper.) Save progress between steps. Validate on step completion, not just final submit. Summary/review step before submission.

**3.25 Inline Editing**: Click-to-edit pattern. Text transforms from display to input on interaction. Notion, Airtable. Double-click or pencil icon trigger. Enter to save, Escape to cancel. Focus management critical.

**3.26 Form Validation Pattern**: When and how to show validation errors. Best practice: validate on blur (not on keystroke), show errors inline below the field, summarize at the top for screen readers. Never clear the form on validation failure.

**3.27 Consent / Permission Pattern**: Cookie consent, notification permission, data sharing. Progressive: ask when needed, not all at once. Explain the benefit. Never pre-check opt-in. GDPR-compliant patterns.

---

## Category 4: Feedback & Status Patterns (18 patterns)

### 4.1 Toast / Snackbar
Non-blocking, auto-dismissing notification for action confirmations. 3-5 seconds visible. Bottom-left or bottom-center placement. Must have dismiss button. Optional undo action. Queue multiple toasts, don't stack more than 3. `role="status"`, `aria-live="polite"`.

### 4.2 Alert / Banner
Persistent or dismissible full-width message. Info, warning, error, success variants. Page-level at the top. Inline near the relevant content for contextual alerts. `role="alert"` for urgent (screen reader will interrupt). `role="status"` for informational.

### 4.3 Notification Center
Bell icon + badge → dropdown or page with notification list. Read/unread states. Grouped by time or type. Mark all as read. Click to navigate to relevant content. Real-time updates via WebSocket or polling.

### 4.4 Progress Indicator
Determinate (known percentage) vs. indeterminate (unknown duration). Linear bar or circular ring. Always use determinate when you can estimate progress. Show percentage or step label. `role="progressbar"` with `aria-valuenow`.

### 4.5 Loading Skeleton
Placeholder shapes mimicking real content layout. Pulse animation. Per-component, not full-page. The modern replacement for spinners. Shows instantly, replaced when data arrives. No ARIA needed — it's visual-only.

### 4.6 Spinner
Rotating indicator for indeterminate loading. Use only when loading will be < 5 seconds and layout is unknown. For > 5 seconds, use progress bar or skeleton. `role="status"`, `aria-label="Loading"`. Centered in the loading area, not full-page.

### 4.7 Pull-to-Refresh
Mobile pattern: pull down on a scrollable list to refresh content. iOS and Android native. Visual indicator (spinner or arrow) appears during pull. Haptic feedback at trigger point. Web: use carefully, can conflict with browser behavior.

### 4.8 Confirmation Dialog
Modal asking user to confirm a destructive or important action. "Delete this project?" with Cancel (primary) and Delete (destructive, secondary). Destructive button should be visually distinct (red) and not pre-focused. Focus the cancel button by default.

### 4.9 Inline Validation Feedback
Real-time feedback on form input validity. Green checkmark for valid, red X for invalid. Show on blur (after user finishes the field), not on every keystroke. Password strength meters. Email format validation. `aria-invalid="true"` + `aria-describedby`.

### 4.10 Status Indicator / Dot
Small colored circle indicating state. Green (active/online), yellow (warning/away), red (error/offline), gray (inactive/unknown). Always pair with text or `aria-label` — never color alone. System status pages, user presence, server health.

### 4.11 Coaching / Hotspot
Pulsing dot or highlight drawing attention to a new or important feature. Part of onboarding or feature discovery. Click to see explanation tooltip/popover. Dismiss permanently after interaction. Max 1 per screen at a time.

### 4.12 Confetti / Celebration
Animation triggered on achievement or completion. Onboarding complete, first sale, milestone reached. Use sparingly — impact diminishes with frequency. Respect `prefers-reduced-motion`. Lottie or CSS animation.

### 4.13 Undo / Redo Feedback
After a destructive action (archive, delete, move), show toast with "Undo" action for 5-10 seconds. Gmail's "Message sent — Undo" is the gold standard. Better than confirmation dialogs because it doesn't interrupt flow.

### 4.14 Connection Status
Online/offline indicator. Appears when connection is lost, hides when restored. "You're offline — changes will sync when you're back online." `aria-live="assertive"` for connection loss.

### 4.15 Rate Limiting / Throttle Feedback
When user hits a rate limit or is being throttled: explain what happened, when they can retry, and why the limit exists. Show countdown timer if applicable. Never silently swallow requests.

### 4.16 Permission Request
System permission dialog (camera, microphone, location, notifications). Always explain WHY before triggering the system dialog. Show context: "We need your location to show nearby restaurants." Never request on page load — wait for a user action that needs the permission.

### 4.17 Maintenance / Downtime Screen
Full-page screen shown during scheduled or unscheduled downtime. Estimated time of restoration. Status page link. Friendly tone, not technical. Optional: email notification signup for when service is back.

### 4.18 Empty Search Results
What's shown when a search returns zero results. Never just "No results." Show: the query with suggestion to modify, spelling suggestions, popular/recommended content, help link. The most underdesigned screen in most products.

---

## Category 5: Layout & Composition Patterns (20 patterns)

### 5.1 Single Column Layout
Content stacked vertically in one column, typically 600-800px max-width centered. Blog posts, articles, signup flows, mobile. The simplest and most readable layout. Optimal line length: 45-75 characters.

### 5.2 Two Column Layout
Content area + sidebar. The classic web layout. Content typically 2/3, sidebar 1/3. Sidebar for navigation, filters, related content, or ads. Collapses to single column on mobile.

### 5.3 Three Column Layout
Left sidebar + content + right sidebar. Dashboards, social media (Facebook-style). Left for navigation, center for content, right for supplementary info. Complex — only justified when all three columns serve distinct purposes.

### 5.4 Grid / Card Grid
CSS Grid of uniformly-sized cards. Product listings, galleries, dashboards. Auto-fill/auto-fit for responsive behavior. Gap consistency is critical. Minimum card width ~280px.

### 5.5 Bento Grid
Asymmetric grid with cards of varying sizes. Apple marketing trend. High visual impact. Best for feature showcases, not repetitive content. Each card size should be intentional — larger = more important. CSS Grid `grid-template-areas` for implementation.

### 5.6 Masonry Layout
Cards of varying heights arranged to minimize vertical gaps. Pinterest, image galleries. CSS Columns, or Masonry.js. Source order vs. visual order mismatch is an accessibility concern.

### 5.7 Split Screen
Two equal (or near-equal) panels side by side. Login/signup pages (illustration + form), comparison views, master-detail. Powerful for storytelling. Collapses to stacked on mobile.

### 5.8 Full Bleed / Edge-to-Edge
Content spans the full viewport width with no container padding. Hero images, feature sections, immersive media. Alternates with contained sections for rhythm.

### 5.9 Holy Grail Layout
Header + footer + 3 columns (nav + content + aside). The classic web layout problem, now solved by CSS Grid. `grid-template-rows: auto 1fr auto; grid-template-columns: 200px 1fr 200px;`

### 5.10 Sticky Header + Scrollable Content
Fixed header/toolbar with independently scrollable content area below. Dashboards, email clients, chat apps. `position: sticky` or fixed positioning. Content area: `overflow-y: auto`.

### 5.11 Fixed Sidebar + Scrollable Content
Sidebar stays fixed while main content scrolls. SaaS standard (Slack, Notion, Linear). Sidebar has its own scroll when content exceeds height. Main content area fills remaining width.

### 5.12 Master-Detail
Left panel shows a list, right panel shows the selected item's details. Email clients (Outlook), file managers, CRMs. List width ~300-400px, detail fills remainder. Mobile: list and detail are separate views with navigation between them.

### 5.13 Dashboard Grid
Configurable grid of widgets/cards. Analytics dashboards, home screens. Drag-to-reorder, resize. Fixed breakpoints or fluid. Each widget is self-contained with its own loading/error states.

### 5.14 Responsive Container
Content adapts based on its container width, not the viewport. CSS Container Queries (`@container`). Components that work in sidebars, modals, and full-width without separate responsive logic.

### 5.15 Z-Pattern / F-Pattern Layout
Layout that follows natural eye scanning patterns. F-pattern: users scan the top horizontal line, then a shorter horizontal line below, then scan vertically down the left side. Z-pattern: diagonal eye movement for simpler pages. Place primary CTAs along these scan paths.

### 5.16 Card + Detail Overlay
Clicking a card opens a detail view as a modal, drawer, or expanded inline panel. Product quick-view, post detail on social media. URL should update for deep linking. Smooth transition from card to detail.

### 5.17 Dock / Toolbar Layout
Floating toolbar (horizontal or vertical) for frequently used actions. Design tools (Figma), photo editors, presentation tools. Draggable, collapsible. macOS Dock is the archetype.

### 5.18 Focus Mode / Zen Mode
Stripped-down layout that removes all secondary UI to focus on primary content. Writing mode (iA Writer), reading mode (Safari Reader), presentation mode. Toggle to enter/exit. Keyboard shortcut.

### 5.19 Responsive Breakpoint System
Mobile (<768px) → Tablet (768-1024px) → Desktop (1024-1440px) → Wide (1440px+). Container queries replacing viewport queries. Key transitions: bottom nav ↔ sidebar, stack ↔ side-by-side, collapse ↔ expand.

### 5.20 Content + Floating Elements
Main content with floating elements overlaid: FABs, chat widgets, cookie banners, help buttons. Z-index management. Must not obscure critical content or CTAs. Maximum 2 floating elements per screen.

---

## Category 6: Commerce & Conversion Patterns (15 patterns)

### 6.1 Product Card
Image + name + price + rating + CTA. E-commerce fundamental. Quick-view on hover. Wishlist button. Sale price with strikethrough original. Badge: "New", "Sale", "-20%".

### 6.2 Product Detail Page
Hero image gallery + product info + add to cart + description tabs + reviews + related products. The most A/B tested page type in existence. Image gallery: zoom, thumbnails, video. Sticky add-to-cart on scroll.

### 6.3 Shopping Cart
Line items with image, name, quantity adjuster, price, remove. Subtotal, taxes, shipping estimate, total. Promo code input. Continue shopping + checkout CTAs. Mini-cart variant (dropdown from cart icon).

### 6.4 Checkout Flow
Shipping → Payment → Review → Confirmation. Guest checkout option. Express checkout (Apple Pay, Google Pay) above the fold. Order summary sidebar (desktop) or collapsible (mobile). Trust badges near payment.

### 6.5 Pricing Page
Tiered pricing cards (3-4 tiers). Highlighted recommended tier. Monthly/annual toggle (annual shows savings). Feature comparison table below cards. FAQ section. Enterprise "Contact us" CTA.

### 6.6 Social Proof
Testimonials, reviews, ratings, customer logos, usage stats. "Trusted by 10,000+ teams." Star ratings with count. Video testimonials are highest-converting. Place near CTAs and pricing.

### 6.7 CTA (Call to Action)
Primary button that drives the main conversion action. One primary CTA per viewport. Contrasting color. Action-oriented label ("Start free trial", not "Submit"). Above the fold. Sticky on mobile.

### 6.8 Lead Capture Form
Email input + submit button. The simplest conversion form. Minimal fields (name + email maximum). Value proposition above the form. Privacy note below. Success state with confirmation.

### 6.9 Trial / Freemium Gate
Paywall or feature gate for premium content. Show what's behind the gate (blurred, truncated). Clear upgrade path. Frictionless trial start (no credit card required converts better).

### 6.10 Upsell / Cross-sell
"Customers also bought", "Upgrade for X", "Complete the look". Product recommendations, plan upgrades, add-ons during checkout. Ethical: must be genuinely useful, not dark-pattern bloat.

### 6.11 Urgency / Scarcity (Ethical)
"3 left in stock", countdown timer for sales, "Last booked 5 minutes ago." Only ethical when real. False scarcity is a dark pattern and increasingly illegal (FTC, EU DSA). Real inventory counts are fine.

### 6.12 Trust Signals
SSL badge, secure payment icons, money-back guarantee badge, customer count, press logos, certifications (SOC 2, HIPAA). Place near form fields and payment. Fintech and healthcare need elevated trust signals.

### 6.13 Onboarding Paywall
Paywall shown during onboarding, typically after demonstrating value. "Your report is ready — subscribe to view it." Effective when the user has invested effort. Must offer a way to cancel/go back.

### 6.14 Subscription Management
Current plan display + upgrade/downgrade options + billing history + cancel flow. Cancel must be as easy as subscribe (FTC requirement). Retention offer on cancellation attempt (ethical: discount, not dark pattern maze).

### 6.15 Referral / Invite System
Share link/code + reward display + invite tracking. "Give $10, get $10." Simple copy-to-clipboard link. Social share buttons. Status tracking for pending/completed referrals.

---

## Category 7: Social & Communication Patterns (15 patterns)

### 7.1 Chat / Messaging Interface
Message list (reverse chronological) + input bar + send button. Real-time updates. Read receipts. Typing indicator. Thread/reply support. File/image attachment. Emoji reactions. Bubble layout (user right, other left) or aligned (Slack-style).

### 7.2 Comment Thread
Nested comments with reply chains. Author avatar + name + timestamp + content + actions (reply, like, edit, delete). Collapsible threads for deep nesting. @mentions with autocomplete. Markdown or rich text.

### 7.3 Activity Feed
Chronological stream of events. "Alice commented on...", "Bob merged PR #123." Actor + action + object + timestamp. Grouped by time (Today, Yesterday). Read/unread state. Filter by type.

### 7.4 Reaction / Emoji Response
Quick emotional response to content. Like, love, laugh, etc. Click to add, click again to remove. Reaction count display. Facebook reactions, Slack emoji reactions, GitHub PR reactions.

### 7.5 Mention / Tag System
@username inline in text. Autocomplete dropdown triggered by "@". Links to profile. Notification to mentioned user. Display differently from regular text (bold, colored).

### 7.6 Share / Social Sharing
Share button → modal/sheet with options. Copy link, social platform buttons, email, QR code. Short URL generation. Preview card (Open Graph) showing what the shared link looks like.

### 7.7 User Profile Page
Avatar + name + bio + stats (followers, posts, etc.) + content tabs (posts, media, likes). Edit profile button (own profile). Follow/message buttons (other profiles). Cover image.

### 7.8 Follow / Subscribe / Connect
Relationship action button. States: Follow, Following, Unfollow (on hover). Confirmation for unfollow. Follower/following counts. Feed implications explained.

### 7.9 Direct Message / Inbox
Conversation list + message detail. Unread indicators. Search conversations. New message composer. Online/offline status. Group DMs. Similar to email inbox pattern but real-time.

### 7.10 Presence / Online Status
Green dot (online), yellow (away), red (busy/DND), gray (offline). Custom status with emoji + text. Slack pioneered this. Must have screen reader text — never color alone.

### 7.11 Video / Audio Call Interface
Camera and mic controls + participant grid + screen share + chat sidebar + leave/end button. Gallery vs. speaker view. Self-view mirror. Hand raise, reactions. Caption/transcript toggle.

### 7.12 Collaborative Editing Indicators
Multi-cursor with user colors/names. "3 people editing." Selection highlighting per user. Presence sidebar showing who's viewing. Figma, Google Docs, Notion.

### 7.13 Content Creation / Post Composer
Rich text input + media attachment + audience selector + post button. Character count for limited platforms. Draft saving. Preview before posting. Schedule for later.

### 7.14 Group / Community
Member list + roles/permissions + settings + activity. Join/leave, invite. Admin tools. Moderation controls. Channels or topics for organization within the group.

### 7.15 Notification Preferences
Per-channel (email, push, in-app, SMS) toggle grid. Per-type (mentions, replies, follows, marketing) controls. Global mute. Quiet hours. The settings page most products get wrong by making it too complex or too simple.

---

## Category 8: Content & Media Patterns (15 patterns)

### 8.1 Article / Long-form Content
Title + author + date + body + table of contents (sidebar or top). Optimal line length: 45-75 characters. Responsive images. Pull quotes. Related articles at bottom. Reading time estimate.

### 8.2 Media Player (Video)
Video container + play/pause + progress bar + volume + fullscreen + captions toggle. Hover to show controls. Autoplay: muted only. Progress bar: scrubble with preview thumbnails. Captions on by default for accessibility.

### 8.3 Media Player (Audio)
Waveform or progress bar + play/pause + current time/duration + speed control + volume. Podcast players, music players, voice messages. Minimizable to persistent mini-player.

### 8.4 Image Viewer / Lightbox
Full-screen or large overlay for viewing images. Zoom, pan, swipe between images. Counter (3/12). Download/share/info buttons. Escape or click outside to close. Background dim.

### 8.5 Document Viewer
PDF, DOC, or rich text display within the app. Pagination or scroll. Zoom controls. Search within document. Annotation/highlighting tools. Download option.

### 8.6 Markdown Renderer
Formatted display of markdown content. Code blocks with syntax highlighting and copy. Tables, images, headings, lists, blockquotes. GitHub Flavored Markdown as the standard. Anchor links on headings.

### 8.7 Story / Reel Format
Full-screen, swipeable, auto-advancing content units. Instagram Stories, YouTube Shorts, TikTok. Progress bar at top. Tap left/right to navigate. Hold to pause. Vertical video format.

### 8.8 Hero Section / Banner
Full-width section at top of page. Large headline + subheading + CTA + background image/video/gradient. The first impression of any marketing page. Above-the-fold content must convey the core value proposition.

### 8.9 Feature Section
Section showcasing a product feature. Icon/image + heading + description + CTA. Grid of features (3-4 per row) or alternating left-right layout. Each feature: benefit-first headline, not feature-first.

### 8.10 Testimonial / Quote Block
Customer testimonial with photo, name, role, company, and quote. Star rating optional. Carousel for multiple. Video testimonials are highest-trust. Attribution must be real.

### 8.11 FAQ / Accordion Content
Questions as accordion headers, answers as expandable content. Search for long FAQ lists. Categories/sections. Schema markup for SEO (FAQ page schema). `<details>/<summary>` HTML implementation.

### 8.12 Pricing / Plan Display
See 6.5 (Commerce). Cross-referenced here because pricing is also a content pattern — it communicates value, not just collects payment.

### 8.13 Changelog / What's New
Chronological list of product updates. Date + version + title + description + type badge (New, Improved, Fixed). Group by release. Images/GIFs for visual changes. RSS feed option.

### 8.14 Knowledge Base / Help Center
Searchable article repository. Categories with article counts. Popular articles. Breadcrumb navigation. In-article feedback ("Was this helpful?"). Contact support CTA when self-service fails.

### 8.15 Onboarding Slides / Walkthrough
Full-screen or modal sequence introducing key features. Dots/progress indicator. Skip button always visible. 3-5 slides maximum. Benefit-oriented (not feature-oriented). Show, don't just tell.

---

## Category 9: Onboarding & Education Patterns (12 patterns)

### 9.1 Welcome Screen
First screen after signup. Personalize: "Welcome, [Name]." Clear next step. Option to take a tour or skip. Show what the user can accomplish, not just what the app has. "Let's set up your first project" > "Here are all our features."

### 9.2 Setup Wizard
Multi-step configuration after signup. Name, preferences, integrations, team invites. Progress indicator. Skip individual steps where possible. Reasonable defaults for everything. Notion, Linear, Slack.

### 9.3 Progressive Disclosure Onboarding
Features revealed as the user demonstrates readiness. Day 1: core features. Day 3: intermediate features. Day 7: power features. Trigger-based, not time-based ("You've created 5 projects — try templates").

### 9.4 Feature Tour / Coach Marks
Overlay highlighting UI elements with explanatory tooltips. Step-by-step, one element at a time. Must be dismissable and skippable. Never block the primary action. Spotlights with dark overlay. Max 5 steps.

### 9.5 Interactive Tutorial
Guided task completion with real data. "Create your first task" with hand-holding. More effective than passive tours because user builds muscle memory. Duolingo-style learning-by-doing.

### 9.6 Template / Quick Start
Pre-built templates that give users a populated starting point. "Start with Marketing template" vs. blank state. Templates should be deletable/modifiable. Show outcome before selection.

### 9.7 Checklist / Progress Tracker
"Get started" checklist showing setup completion. "Complete your profile (3/5 steps done)." Persistent, collapsible widget. Celebrate completion. Linear onboarding, Notion onboarding.

### 9.8 Empty State with Action
When a section has no content, show what could be there and how to get started. Illustration + explanation + primary CTA. "No projects yet — Create your first project." Never show a blank screen.

### 9.9 Contextual Help / Inline Education
Help text, tooltips, and info icons placed next to complex features. "What is this?" links. Learn more in context, not in documentation. Dismissable, not persistent.

### 9.10 Gamification / Achievement System
Points, badges, streaks, levels for engagement. Duolingo is the benchmark. Must be optional, not coercive. Celebrate genuine progress, not manufactured addiction loops. Ethical guardrails essential.

### 9.11 Sample Data / Demo Mode
Pre-populated data so users can explore the product before committing their own data. "Explore with sample data" toggle. Clearly marked as sample. Easy to clear and start fresh.

### 9.12 Changelog Notification
In-app notification for new features. "What's new" badge on menu item. Modal or slide-in panel with recent updates. Per-update "dismiss" so user isn't re-shown. Show, don't just tell — include screenshots.

---

## Category 10: AI & Generative Patterns (12 patterns)

### 10.1 AI Chat Interface
Conversational AI in a chat-like UI. User message + AI response + streaming text. Suggestion chips for follow-ups. Copy, regenerate, thumbs up/down per response. Citation/source links. ChatGPT, Claude, Gemini.

### 10.2 AI Copilot / Inline Assist
AI suggestions appearing inline in the user's workflow. Code completion (GitHub Copilot), writing suggestions (Notion AI), design suggestions. Tab to accept, Escape to dismiss. Ghost text preview. Non-blocking.

### 10.3 AI Command Bar
Natural language input that maps to application actions. "Create a new project called X" → executes action. Different from search — it acts, not navigates. Confidence indicator for uncertain interpretations. Confirmation for destructive actions.

### 10.4 AI-Generated Content Preview
Show AI output before applying. "Here's what the AI wrote — Edit or Accept." Diff view against original (for rewrites). Regenerate option. Never auto-apply without user confirmation for consequential content.

### 10.5 AI Loading / Thinking State
What to show while AI processes. Streaming text (word by word) is best — shows progress and reduces perceived wait. Typing indicator (dots). "Thinking..." with elapsed time for long operations. Never a blank screen.

### 10.6 AI Confidence / Uncertainty Display
Visual indication of how confident the AI is. Highlight uncertain sections. "I'm not sure about this" disclaimers. Source citations for factual claims. Hallucination guardrails.

### 10.7 AI Feedback Loop
Thumbs up/down, "Was this helpful?", corrections, custom feedback. Per-response rating. Improves model over time. Must be lightweight (one click). Detailed feedback optional.

### 10.8 AI Permission / Scope Control
What the AI can access and do. Read-only vs. read-write. Per-tool permissions. "Allow AI to access your calendar?" Granular, revocable, transparent. Audit log of AI actions.

### 10.9 Prompt Input / Instruction
Text area for telling the AI what to do. Examples/templates for common tasks. Character limit display. Context indicator ("AI can see this page"). Clear "Send" or "Generate" CTA.

### 10.10 AI-Powered Search / Semantic Search
Search that understands meaning, not just keywords. Natural language queries. "Show me all invoices from last quarter over $5000." Results ranked by semantic relevance, not just keyword match. Explanation of why each result matched.

### 10.11 Generative UI / Dynamic Interface
UI components generated on-the-fly by AI based on context. Vercel's AI SDK Generative UI. Charts, forms, cards rendered in response to queries. The AI decides the best display pattern. Must be accessible — generated UI needs ARIA.

### 10.12 Multi-Agent / Orchestration Display
UI showing multiple AI agents collaborating. Status per agent. Pipeline visualization. Progress per stage. Which agent is currently active. Human-in-the-loop checkpoints. Trust and transparency critical.

---

## Pattern Cross-Reference Index

When analyzing code or screenshots, use this index to quickly identify which category a pattern belongs to:

| If you see... | It's likely... | Category |
|---------------|---------------|----------|
| Horizontal links at top | Top Nav Bar (1.1) | Navigation |
| Icons at bottom of mobile screen | Bottom Nav (1.2) | Navigation |
| Vertical panel with links on left | Sidebar (1.3) | Navigation |
| Rows and columns of data | Data Table (2.1) | Data Display |
| Rectangular containers with content | Cards (2.2) | Data Display |
| Vertical sequence of items | List/Feed (2.3) | Data Display |
| Visual graph or chart | Chart (2.4) | Data Display |
| Input field with label | Text Input (3.1) | Input |
| Dropdown selection | Select (3.3) | Input |
| Grid of selectable dates | Date Picker (3.7) | Input |
| Temporary bottom message | Toast (4.1) | Feedback |
| Animated placeholder shapes | Skeleton (4.5) | Feedback |
| Two panels side by side | Split Screen (5.7) | Layout |
| Full-width top section with CTA | Hero (8.8) | Content |
| Chat-like AI conversation | AI Chat (10.1) | AI |
| Inline text suggestions | AI Copilot (10.2) | AI |

This index enables rapid pattern identification during code analysis. When examining a user's codebase, walk through every component and screen, match each to this taxonomy, and assess execution quality against the benchmarks described in each pattern entry.
