# Pattern Quick-Lookup Index — 300+ UI Patterns

## How to Use This Index

This is the fastest way to look up any UI pattern. Organized alphabetically within categories. Each entry gives you instant context: what it is, when to use it, what it pairs with, and when to avoid it. For deeper analysis, cross-reference with `pattern-taxonomy-complete.md` for full anatomy and accessibility requirements, or `designer-benchmark-dna.md` for world-class examples.

Jump to category: [Navigation](#navigation-patterns) | [Content Display](#content-display-patterns) | [Data Entry](#data-entry-patterns) | [Feedback & Status](#feedback--status-patterns) | [Social & Communication](#social--communication-patterns) | [Commerce & Conversion](#commerce--conversion-patterns) | [Search & Filter](#search--filter-patterns) | [Onboarding & Education](#onboarding--education-patterns) | [Settings & Preferences](#settings--preferences-patterns) | [Dashboard & Analytics](#dashboard--analytics-patterns) | [Media & Content](#media--content-patterns) | [AI & Intelligent](#ai--intelligent-patterns) | [Mobile-Specific](#mobile-specific-patterns) | [Collaboration](#collaboration-patterns)

---

## Navigation Patterns

### Anchor Navigation
**Category:** Navigation
**When to use:** Long single-page content with distinct sections (docs, landing pages, legal pages).
**Key components:** Fixed side or top link list, scroll-spy highlighting, smooth scroll behavior.
**Best example:** Stripe Docs
**Avoid when:** Page sections are short or content is highly dynamic.
**See also:** Table of Contents, Sticky Header

### Back Button / Back Navigation
**Category:** Navigation
**When to use:** Any multi-level navigation where users drill into detail views.
**Key components:** Left-arrow icon, label showing parent context, swipe-back gesture on mobile.
**Best example:** iOS system back, Linear issue detail
**Avoid when:** You have persistent sidebar navigation that already shows hierarchy.
**See also:** Breadcrumbs, Drill-Down Navigation

### Bottom Navigation Bar
**Category:** Navigation
**When to use:** Mobile apps with 3-5 primary destinations.
**Key components:** 3-5 icon+label tabs, active indicator, optional badge counts, safe area padding.
**Best example:** Instagram, Spotify
**Avoid when:** Desktop apps, more than 5 destinations, single-purpose apps.
**See also:** Tab Bar, Floating Tab Bar

### Breadcrumbs
**Category:** Navigation
**When to use:** Deep hierarchical content (e-commerce categories, file systems, admin panels).
**Key components:** Ancestor links separated by "/" or ">", current page as plain text, truncation for deep paths.
**Best example:** Shopify Admin, AWS Console
**Avoid when:** Flat navigation with no hierarchy, mobile apps with limited space.
**See also:** Back Button, Anchor Navigation

### Carousel Navigation
**Category:** Navigation
**When to use:** Browsing related content horizontally (product images, featured items).
**Key components:** Prev/next arrows, dot indicators, swipe support, peek of adjacent items.
**Best example:** Airbnb listing photos
**Avoid when:** Hero content (auto-advance kills engagement), critical information (users miss slides 2+).
**See also:** Horizontal Scroll, Gallery View

### Command Palette
**Category:** Navigation
**When to use:** Power-user apps, developer tools, any product with many actions or pages.
**Key components:** Cmd+K trigger, fuzzy search input, categorized results, keyboard shortcut hints, recent actions.
**Best example:** Linear, Raycast, VS Code
**Avoid when:** Simple consumer apps with few actions, non-technical audiences unfamiliar with the pattern.
**See also:** Spotlight Search, Quick Actions Menu

### Contextual Menu
**Category:** Navigation
**When to use:** Secondary actions on specific items (right-click menus, long-press menus).
**Key components:** Action list, keyboard shortcuts, dividers for grouping, destructive action styling.
**Best example:** Figma right-click menu, macOS context menu
**Avoid when:** Primary actions that should be visible by default.
**See also:** Dropdown Menu, Action Sheet

### Deep Link Navigation
**Category:** Navigation
**When to use:** Sharing specific app states via URL, push notification targets, cross-app linking.
**Key components:** URL scheme, universal links, state restoration, fallback handling.
**Best example:** Slack message links, Notion page links
**Avoid when:** Content that requires authentication context that cannot be restored.
**See also:** URL Routing, Magic Links

### Dock / App Launcher
**Category:** Navigation
**When to use:** Desktop OS interfaces, multi-app dashboards, workspace tools.
**Key components:** Icon grid or row, labels on hover, drag-to-reorder, app switching.
**Best example:** macOS Dock, Windows Taskbar
**Avoid when:** Single-purpose applications, mobile web.
**See also:** Bottom Navigation Bar, Sidebar Navigation

### Drawer Navigation
**Category:** Navigation
**When to use:** Mobile apps needing more than 5 destinations, secondary navigation on any platform.
**Key components:** Slide-in panel (left or right), overlay backdrop, grouped menu items, close on outside tap.
**Best example:** Google apps (Gmail, Maps), Material Design drawer
**Avoid when:** Desktop apps (use sidebar instead), apps with 3-5 destinations (use bottom nav).
**See also:** Sidebar Navigation, Hamburger Menu

### Drill-Down Navigation
**Category:** Navigation
**When to use:** Hierarchical content exploration (settings trees, file browsers, category browsing).
**Key components:** List view pushing to detail, back button chain, breadcrumb trail, animated transitions.
**Best example:** iOS Settings, Finder column view
**Avoid when:** Flat content with no parent-child relationships.
**See also:** Breadcrumbs, Miller Columns

### Expandable Navigation
**Category:** Navigation
**When to use:** Sidebar navigation with nested sections (docs, admin panels, file trees).
**Key components:** Collapsible sections, chevron icons, indentation levels, persistent expand state.
**Best example:** Notion sidebar, GitHub file tree
**Avoid when:** Flat navigation with no nesting, mobile where space is critical.
**See also:** Tree View, Accordion Navigation

### Floating Action Button (FAB)
**Category:** Navigation
**When to use:** Mobile apps with a single primary creation action (compose, add, create).
**Key components:** Circular button, elevation shadow, fixed bottom-right position, optional speed dial.
**Best example:** Gmail compose, Google Maps
**Avoid when:** Multiple primary actions, desktop apps, when it obscures content.
**See also:** Bottom Navigation Bar, Quick Actions Menu

### Footer Navigation
**Category:** Navigation
**When to use:** Marketing sites, e-commerce for secondary links (legal, sitemap, social links).
**Key components:** Multi-column link groups, legal links, newsletter signup, social icons.
**Best example:** Stripe footer, Apple footer
**Avoid when:** Web apps (use sidebar), mobile apps (use bottom nav).
**See also:** Top Navigation Bar, Sitemap

### Gesture Navigation
**Category:** Navigation
**When to use:** Mobile apps requiring swipe-based interactions (swipe to go back, swipe between tabs).
**Key components:** Swipe gestures, edge gestures, visual affordance hints, haptic feedback.
**Best example:** iOS gesture navigation, Tinder swipe
**Avoid when:** Desktop-first experiences, accessibility-critical contexts without alternatives.
**See also:** Bottom Navigation Bar, Carousel Navigation

### Hamburger Menu
**Category:** Navigation
**When to use:** Mobile only, as a secondary navigation container when bottom nav handles primary destinations.
**Key components:** Three-line icon, slide-out panel, overlay backdrop, grouped links.
**Best example:** Acceptable on mobile Gmail; avoid on desktop
**Avoid when:** Desktop (kills discoverability), when you have fewer than 6 nav items on mobile.
**See also:** Drawer Navigation, Bottom Navigation Bar

### Hub-and-Spoke Navigation
**Category:** Navigation
**When to use:** Apps where users always return to a central hub (home screen) between tasks.
**Key components:** Central home/dashboard, task-specific sub-screens, return-to-hub action.
**Best example:** Apple Watch home, smart TV interfaces
**Avoid when:** Workflows requiring cross-task navigation without returning to hub.
**See also:** Dashboard Layout, Bottom Navigation Bar

### Mega Menu
**Category:** Navigation
**When to use:** E-commerce and enterprise sites with many categories (50+ links to expose).
**Key components:** Full-width dropdown, categorized columns, featured content/images, keyboard navigable.
**Best example:** Amazon, IKEA, Microsoft
**Avoid when:** Simple sites with few pages, SaaS apps (use sidebar).
**See also:** Top Navigation Bar, Dropdown Menu

### Miller Columns
**Category:** Navigation
**When to use:** Deep hierarchical browsing where users need to see multiple levels simultaneously.
**Key components:** Side-by-side columns, each selection populates next column, horizontal scroll.
**Best example:** macOS Finder column view, Spotify desktop browse
**Avoid when:** Mobile (insufficient width), shallow hierarchies.
**See also:** Drill-Down Navigation, Tree View

### Pagination
**Category:** Navigation
**When to use:** Data tables, search results, admin panels where position awareness matters.
**Key components:** Page numbers, prev/next, items-per-page selector, total count display.
**Best example:** Stripe Dashboard tables, Google Search
**Avoid when:** Social feeds, messaging, content consumption flows.
**See also:** Infinite Scroll, Load More Button

### Quick Actions Menu
**Category:** Navigation
**When to use:** Exposing frequent actions without navigating (3D Touch, long-press shortcuts).
**Key components:** Action list overlay, icon + label per action, contextual to trigger location.
**Best example:** iOS home screen quick actions, Notion slash menu
**Avoid when:** Actions that need confirmation or complex input.
**See also:** Command Palette, Contextual Menu

### Radial Menu
**Category:** Navigation
**When to use:** Creative tools, gaming interfaces, spatial computing where directional selection is natural.
**Key components:** Circular arrangement of options, center trigger, directional selection, visual sectors.
**Best example:** Procreate, some gaming interfaces
**Avoid when:** Standard business apps, accessibility-critical contexts, many options (>8).
**See also:** Contextual Menu, Quick Actions Menu

### Segmented Control
**Category:** Navigation
**When to use:** Switching between 2-4 related views of the same content (list/grid, day/week/month).
**Key components:** Horizontal pill group, active indicator, 2-4 options maximum, immediate switching.
**Best example:** iOS Maps (Map/Transit/Satellite), Linear views
**Avoid when:** More than 4 options (use tabs), unrelated content sections.
**See also:** Tab Navigation, Toggle Group

### Sidebar Navigation
**Category:** Navigation
**When to use:** SaaS apps, dashboards, admin panels, any desktop app with 5+ destinations.
**Key components:** Vertical link list, grouped sections, collapsible, active state highlight, icon + label.
**Best example:** Linear, Notion, Slack
**Avoid when:** Mobile (use bottom nav/drawer), marketing sites (use top nav).
**See also:** Expandable Navigation, Drawer Navigation

### Spotlight / Global Search
**Category:** Navigation
**When to use:** Any app where users need to find content across the entire product quickly.
**Key components:** Keyboard shortcut trigger, centered overlay input, categorized results, recent searches.
**Best example:** macOS Spotlight, Slack search, Notion search
**Avoid when:** Very simple apps with minimal searchable content.
**See also:** Command Palette, Search Input

### Stepper / Wizard
**Category:** Navigation
**When to use:** Multi-step processes (checkout, onboarding, form wizards) with 3-7 steps.
**Key components:** Step indicators, progress bar, back/next buttons, step validation, save progress.
**Best example:** Shopify checkout, Stripe onboarding
**Avoid when:** Fewer than 3 steps (use single page), more than 7 steps (reorganize).
**See also:** Progress Bar, Pagination

### Sticky Header
**Category:** Navigation
**When to use:** Long scrolling pages where persistent access to navigation or context is needed.
**Key components:** Fixed top bar, scroll-triggered appearance/shrink, shadow on scroll, z-index management.
**Best example:** Apple.com shrinking nav, GitHub repo header
**Avoid when:** Short pages, immersive content experiences, mobile where vertical space is precious.
**See also:** Top Navigation Bar, Anchor Navigation

### Tab Navigation
**Category:** Navigation
**When to use:** Switching between 3-7 peer-level content sections within a view.
**Key components:** Horizontal tab row, active indicator (underline or pill), content panel, keyboard arrow navigation.
**Best example:** GitHub repo tabs, Chrome browser tabs
**Avoid when:** More than 7 tabs (use sidebar or dropdown), unrelated content.
**See also:** Segmented Control, Bottom Navigation Bar

### Top Navigation Bar
**Category:** Navigation
**When to use:** Marketing sites, web apps, multi-section products on desktop.
**Key components:** Logo (left), primary links (center/left), utility actions (right: search, avatar, CTA).
**Best example:** Stripe marketing, Linear
**Avoid when:** Mobile-first apps, single-page apps, immersive experiences.
**See also:** Mega Menu, Sticky Header

### Tree View
**Category:** Navigation
**When to use:** File systems, nested settings, organizational hierarchies, code editors.
**Key components:** Expandable/collapsible nodes, indentation, connecting lines, leaf/branch icons.
**Best example:** VS Code file explorer, Windows Explorer
**Avoid when:** Flat data, mobile interfaces, non-technical users.
**See also:** Expandable Navigation, Miller Columns

---

## Content Display Patterns

### Accordion
**Category:** Content Display
**When to use:** FAQ sections, settings groups, collapsible content sections where showing all at once overwhelms.
**Key components:** Header + chevron trigger, expandable content panel, single or multi-expand modes.
**Best example:** Stripe FAQ, iOS Settings groups
**Avoid when:** Content users need to compare across sections, very short content.
**See also:** Expandable Navigation, Disclosure

### Alert Banner
**Category:** Content Display
**When to use:** System-wide messages (maintenance, new features, critical warnings) that affect all users.
**Key components:** Full-width bar, icon + message + optional CTA, dismiss button, color-coded severity.
**Best example:** GitHub incident banner, Vercel deployment notice
**Avoid when:** User-specific feedback (use toast), non-urgent information.
**See also:** Toast, Notification Badge

### Avatar
**Category:** Content Display
**When to use:** Representing users or entities anywhere in the UI (comments, lists, profiles, chat).
**Key components:** Circular image, fallback initials, size variants (24-64px), optional status dot, group stacking.
**Best example:** Slack, GitHub, Linear
**Avoid when:** Non-human entities that need distinct iconography.
**See also:** Avatar Group, Profile Card

### Avatar Group
**Category:** Content Display
**When to use:** Showing multiple participants (assignees, collaborators, attendees) in compact space.
**Key components:** Overlapping circular avatars, "+N more" overflow, size-consistent, tooltip on hover.
**Best example:** GitHub PR reviewers, Linear assignees, Figma collaborators
**Avoid when:** Need to show detailed user info (use a list).
**See also:** Avatar, Presence Indicator

### Badge / Tag
**Category:** Content Display
**When to use:** Status labels, category tags, notification counts, feature labels (new, beta).
**Key components:** Small pill shape, color-coded, text or count, removable variant for filters.
**Best example:** Linear status badges, Notion tags, App Store notification badges
**Avoid when:** Long text content, primary actions.
**See also:** Chip, Status Indicator

### Bento Grid
**Category:** Content Display
**When to use:** Feature showcases, dashboard overviews, marketing sections with varied content types.
**Key components:** CSS Grid with varied cell sizes, visual hierarchy through size, mixed media types.
**Best example:** Apple product pages, Vercel feature grid
**Avoid when:** Uniform data that should be in a table or card grid.
**See also:** Card Grid, Masonry Layout

### Calendar View
**Category:** Content Display
**When to use:** Date-based events, scheduling, availability, time-bound data visualization.
**Key components:** Month/week/day grid, event blocks, drag-to-create, date navigation, today highlight.
**Best example:** Google Calendar, Notion Calendar, Cron
**Avoid when:** Non-date-based data, mobile where space is limited (use agenda/list view).
**See also:** Timeline, Date Picker

### Card
**Category:** Content Display
**When to use:** Browsable collections of similar items (products, articles, projects, users).
**Key components:** Container with border/shadow, image, title, description, metadata, CTA.
**Best example:** Airbnb listings, Dribbble shots, App Store
**Avoid when:** Dense data needing comparison (use table), sequential content (use list).
**See also:** Card Grid, List Item, Bento Grid

### Card Grid
**Category:** Content Display
**When to use:** Displaying a collection of cards in a responsive grid layout.
**Key components:** Equal-sized cards, responsive columns (1-4), gap spacing, consistent card height.
**Best example:** Dribbble, Unsplash, App Store
**Avoid when:** Items that vary wildly in content length (consider masonry).
**See also:** Card, Bento Grid, Masonry Layout

### Carousel / Slider
**Category:** Content Display
**When to use:** Product image galleries (user-controlled), testimonials, related items.
**Key components:** Horizontal scroll, prev/next arrows, pagination dots, swipe support, peek.
**Best example:** Airbnb listing photos (user-controlled)
**Avoid when:** Hero content (auto-advance is an anti-pattern), critical information.
**See also:** Horizontal Scroll, Gallery View

### Chart (Bar)
**Category:** Content Display
**When to use:** Comparing discrete categories, showing distribution, ranking data.
**Key components:** Labeled axes, value labels, hover tooltips, color coding, responsive sizing.
**Best example:** Stripe analytics, Vercel usage
**Avoid when:** Continuous data over time (use line chart), parts of a whole (use pie/donut).
**See also:** Chart (Line), Chart (Pie), Stat Display

### Chart (Line)
**Category:** Content Display
**When to use:** Trends over time, continuous data, multiple series comparison.
**Key components:** Time axis, value axis, data points, hover crosshair, legend, zoom/pan.
**Best example:** Stripe revenue chart, Vercel analytics
**Avoid when:** Categorical data (use bar), single data points (use stat display).
**See also:** Chart (Bar), Sparkline, Chart (Area)

### Chart (Pie / Donut)
**Category:** Content Display
**When to use:** Parts of a whole, percentage breakdowns, budget allocation (max 5-7 segments).
**Key components:** Segments with labels, percentage values, legend, hover highlight, center stat for donut.
**Best example:** Mercury account breakdown
**Avoid when:** More than 7 segments (use bar chart), precise value comparison.
**See also:** Chart (Bar), Stat Display

### Chart (Area)
**Category:** Content Display
**When to use:** Volume over time, stacked comparisons, emphasizing magnitude of trends.
**Key components:** Filled area under line, opacity layering for stacks, gradient fills.
**Best example:** Vercel bandwidth usage, Stripe volume charts
**Avoid when:** Precise value reading needed (overlapping areas obscure values).
**See also:** Chart (Line), Chart (Bar)

### Chip
**Category:** Content Display
**When to use:** Compact interactive elements for selections, filters, or input tags.
**Key components:** Pill shape, optional icon/avatar, optional remove button, selected state.
**Best example:** Gmail labels, Material Design chips, Notion tags
**Avoid when:** Non-interactive labels (use badge), long text content.
**See also:** Badge / Tag, Filter Chip

### Code Block
**Category:** Content Display
**When to use:** Displaying code snippets, API responses, configuration examples.
**Key components:** Monospace font, syntax highlighting, copy button, language label, line numbers.
**Best example:** Stripe Docs, GitHub, Vercel
**Avoid when:** Non-code text content.
**See also:** Terminal Display, Diff View

### Collapsible Section
**Category:** Content Display
**When to use:** Progressive disclosure of secondary content within a page.
**Key components:** Toggle header, smooth expand/collapse animation, chevron rotation, content panel.
**Best example:** GitHub PR file changes, Notion toggle blocks
**Avoid when:** Primary content that most users need to see.
**See also:** Accordion, Disclosure

### Data Table
**Category:** Content Display
**When to use:** Structured data requiring sorting, filtering, comparison across rows and columns.
**Key components:** Header row, sortable columns, row selection, pagination, column resizing, sticky header.
**Best example:** Stripe Dashboard, Airtable, Notion tables
**Avoid when:** Fewer than 3 rows (use cards), mobile-first (tables are hard on small screens).
**See also:** List / Feed, Card Grid, Virtual Table

### Diff View
**Category:** Content Display
**When to use:** Comparing two versions of text, code, or configuration.
**Key components:** Side-by-side or unified view, added/removed highlighting, line numbers, collapse unchanged.
**Best example:** GitHub Pull Requests, VS Code diff
**Avoid when:** Non-text comparison, real-time editing.
**See also:** Code Block, Version History

### Divider / Separator
**Category:** Content Display
**When to use:** Visually separating content sections within a view.
**Key components:** Horizontal line (or vertical), optional label, consistent spacing.
**Best example:** iOS grouped list separators
**Avoid when:** Sufficient whitespace already provides separation (over-using dividers adds noise).
**See also:** Card, Section Header

### Drawer / Sheet
**Category:** Content Display
**When to use:** Detail views, secondary panels, mobile action menus, filters on mobile.
**Key components:** Slide from edge (bottom on mobile, right on desktop), backdrop overlay, drag handle, close button.
**Best example:** Apple Maps bottom sheet, Notion side panel
**Avoid when:** Primary content that needs full screen.
**See also:** Modal, Side Panel

### Empty State
**Category:** Content Display
**When to use:** When a view has no data yet (first use, empty search, cleared filters).
**Key components:** Illustration or icon, descriptive headline, action-oriented body text, primary CTA.
**Best example:** Linear empty project, Notion empty page
**Avoid when:** Never skip this — every list, table, and feed needs an empty state.
**See also:** Error State, Onboarding

### Error State
**Category:** Content Display
**When to use:** When something goes wrong (API failure, 404, permission denied, network offline).
**Key components:** Error icon/illustration, clear message, suggested fix, retry button, error code for debugging.
**Best example:** GitHub 404 octocat, Stripe error pages
**Avoid when:** Expected empty states (use empty state pattern instead).
**See also:** Empty State, Alert Banner, Toast

### Gallery View
**Category:** Content Display
**When to use:** Image-heavy browsing (photo albums, portfolios, product photos).
**Key components:** Grid of thumbnails, lightbox on click, zoom, fullscreen, swipe between images.
**Best example:** Unsplash, Google Photos, Airbnb
**Avoid when:** Non-visual content, single images.
**See also:** Card Grid, Masonry Layout, Lightbox

### Kanban Board
**Category:** Content Display
**When to use:** Workflow management with distinct stages (to-do / in-progress / done), project tracking.
**Key components:** Columns representing stages, draggable cards, column headers with counts, add card.
**Best example:** Linear board view, Trello, Notion board
**Avoid when:** Non-stage-based data, read-only views, mobile (hard to drag across columns).
**See also:** Data Table, List / Feed, Timeline

### Lightbox
**Category:** Content Display
**When to use:** Focused image/media viewing from a grid or gallery context.
**Key components:** Dark overlay, centered media, close button, prev/next navigation, zoom controls.
**Best example:** Unsplash image view, Instagram post expand
**Avoid when:** Non-media content, when context of surrounding content is needed.
**See also:** Gallery View, Modal

### List / Feed
**Category:** Content Display
**When to use:** Sequential content (activity feeds, messages, notifications, search results).
**Key components:** Consistent list items, metadata, timestamps, actions, dividers or spacing, virtualization.
**Best example:** Linear issue list, Slack message list, Twitter/X feed
**Avoid when:** Visual content needing image prominence (use cards), tabular data (use table).
**See also:** Data Table, Card, Virtual List

### Masonry Layout
**Category:** Content Display
**When to use:** Mixed-height visual content (photos, pins, design shots) in a space-efficient grid.
**Key components:** Variable-height items in columns, no row gaps, responsive column count.
**Best example:** Pinterest, Dribbble
**Avoid when:** Uniform content (use card grid), data tables, text-heavy content.
**See also:** Card Grid, Gallery View

### Modal / Dialog
**Category:** Content Display
**When to use:** Confirmations, alerts, focused tasks requiring user decision before proceeding.
**Key components:** Overlay backdrop, centered panel, title, content, action buttons, close/escape, focus trap.
**Best example:** Stripe confirmation modals, Linear create issue
**Avoid when:** Data workflows (use side panel), content viewing (use drawer), anything non-blocking.
**See also:** Drawer / Sheet, Alert Banner, Confirmation Dialog

### Notification Badge
**Category:** Content Display
**When to use:** Indicating unread items, pending actions, or new content on navigation elements.
**Key components:** Small red dot or count badge, positioned on icon corner, announced to screen readers.
**Best example:** iOS app badges, Slack unread indicators
**Avoid when:** Decorative purposes, non-actionable information.
**See also:** Badge / Tag, Alert Banner

### Popover
**Category:** Content Display
**When to use:** Rich contextual information or actions triggered by a specific element.
**Key components:** Floating panel, arrow pointing to trigger, click/hover trigger, positioned intelligently.
**Best example:** GitHub user hover cards, Notion block menus
**Avoid when:** Simple text (use tooltip), complex workflows (use drawer/modal).
**See also:** Tooltip, Dropdown Menu, Contextual Menu

### Profile Card
**Category:** Content Display
**When to use:** Showing user details on hover or tap (social profiles, team members, contacts).
**Key components:** Avatar, name, role/bio, stats, action buttons (follow, message).
**Best example:** GitHub hover cards, LinkedIn profile
**Avoid when:** Non-user entities, simple avatar-only needs.
**See also:** Avatar, Card, Popover

### Progress Bar
**Category:** Content Display
**When to use:** Showing completion progress for uploads, multi-step processes, loading states.
**Key components:** Track bar, fill indicator, percentage label, color-coded stages, animation.
**Best example:** GitHub PR checks, file upload progress, Notion import
**Avoid when:** Indeterminate waits (use spinner), instant actions.
**See also:** Stepper / Wizard, Loading Spinner, Progress Ring

### Progress Ring
**Category:** Content Display
**When to use:** Compact circular progress (storage usage, completion %, timer countdowns).
**Key components:** Circular track, fill arc, center value, size variants.
**Best example:** Apple Activity Rings, storage usage indicators
**Avoid when:** Linear processes with steps (use progress bar).
**See also:** Progress Bar, Stat Display

### Section Header
**Category:** Content Display
**When to use:** Labeling groups of content within a scrolling view.
**Key components:** Title text, optional subtitle, optional action link, sticky variant for long lists.
**Best example:** iOS grouped list headers, Notion sections
**Avoid when:** Single-section views, already-labeled card containers.
**See also:** Divider, Collapsible Section

### Skeleton Screen
**Category:** Content Display
**When to use:** Loading states for content-heavy views (replaces full-page spinners).
**Key components:** Gray placeholder shapes matching real content layout, pulse/shimmer animation.
**Best example:** Facebook, LinkedIn, Notion
**Avoid when:** Instant-loading content, error states, empty states.
**See also:** Loading Spinner, Progress Bar

### Sparkline
**Category:** Content Display
**When to use:** Inline trend visualization within tables, stat cards, or list items.
**Key components:** Tiny line chart (no axes), trend direction, color-coded (green up, red down).
**Best example:** Stripe stat cards, stock tickers
**Avoid when:** Need precise values (use full chart), no temporal data.
**See also:** Chart (Line), Stat Display

### Stat Display / KPI Card
**Category:** Content Display
**When to use:** Highlighting key metrics on dashboards (revenue, users, conversion rate).
**Key components:** Large number, label, trend arrow, percentage change, optional sparkline, comparison period.
**Best example:** Stripe Dashboard, Vercel analytics, Mercury
**Avoid when:** More than 6-8 stats (prioritize), detailed data (use table/chart).
**See also:** Sparkline, Chart (Line), Dashboard Layout

### Status Indicator
**Category:** Content Display
**When to use:** Showing current state of items (online/offline, active/inactive, build status).
**Key components:** Colored dot or icon, label text, consistent color coding (green/yellow/red).
**Best example:** Linear issue status, GitHub Actions, Vercel deployment status
**Avoid when:** Binary states only (use toggle/switch).
**See also:** Badge / Tag, Progress Bar

### Table of Contents
**Category:** Content Display
**When to use:** Long-form content (documentation, articles, legal pages) with multiple sections.
**Key components:** Section links, scroll-spy active highlight, sticky sidebar placement, nested levels.
**Best example:** Stripe Docs, MDN, Notion
**Avoid when:** Short content, dynamically changing sections.
**See also:** Anchor Navigation, Sidebar Navigation

### Timeline
**Category:** Content Display
**When to use:** Chronological event sequences (activity logs, version history, project milestones).
**Key components:** Vertical or horizontal line, event nodes, timestamps, event details, branching.
**Best example:** GitHub activity, Vercel deployment timeline, Git history
**Avoid when:** Non-chronological data, real-time streams (use feed).
**See also:** List / Feed, Calendar View, Version History

### Toast / Snackbar
**Category:** Content Display
**When to use:** Brief, non-blocking feedback after user actions (saved, copied, sent, deleted).
**Key components:** Auto-dismiss (3-5s), message text, optional undo action, stacking, position (bottom or top).
**Best example:** Notion, Linear, Vercel
**Avoid when:** Critical errors (use alert banner), information requiring user decision (use modal).
**See also:** Alert Banner, Notification Badge

### Tooltip
**Category:** Content Display
**When to use:** Brief label text for icon-only buttons or truncated content.
**Key components:** Small floating text, triggered on hover/focus, arrow pointing to trigger, delay (200-500ms).
**Best example:** GitHub icon buttons, Figma toolbar
**Avoid when:** Rich content (use popover), mobile (no hover — use long press or tap).
**See also:** Popover, Help Text

### Version History
**Category:** Content Display
**When to use:** Showing document or entity change history with restore capability.
**Key components:** Version list with timestamps/authors, diff view, restore button, auto-save indicators.
**Best example:** Notion page history, Google Docs version history, Figma
**Avoid when:** Non-versioned data, real-time-only content.
**See also:** Timeline, Diff View

### Virtual / Windowed List
**Category:** Content Display
**When to use:** Lists with 100+ items where rendering all DOM nodes would kill performance.
**Key components:** Only renders visible items + buffer, maintains scroll position, dynamic row heights.
**Best example:** Linear issue list (thousands of issues), Slack messages
**Avoid when:** Short lists (<50 items), SEO-critical content (virtual lists are not crawlable).
**See also:** List / Feed, Infinite Scroll, Data Table

---

## Data Entry Patterns

### Autocomplete Input
**Category:** Data Entry
**When to use:** Inputs with known suggestion sets (addresses, tags, usernames, cities).
**Key components:** Text input, dropdown suggestion list, keyboard navigation, highlight matching text.
**Best example:** Google search suggestions, GitHub mention autocomplete
**Avoid when:** Free-form text with no predictable values.
**See also:** Combobox, Search Input

### Checkbox
**Category:** Data Entry
**When to use:** Binary choices or multi-select from a short list (2-7 options).
**Key components:** Square indicator, label, checked/unchecked/indeterminate states, group label.
**Best example:** Notion property checkboxes, Todoist tasks
**Avoid when:** Single on/off setting (use toggle), mutually exclusive options (use radio).
**See also:** Toggle / Switch, Radio Button, Checkbox Group

### Checkbox Group
**Category:** Data Entry
**When to use:** Selecting multiple options from a list where all options should be visible.
**Key components:** Group label, individual checkboxes with labels, select all option, validation.
**Best example:** GitHub label picker, settings preferences
**Avoid when:** More than 10 options (use searchable multi-select), mutually exclusive choices.
**See also:** Checkbox, Multi-Select, Chip Group

### Chip Input / Tag Input
**Category:** Data Entry
**When to use:** Entering multiple values as discrete tokens (tags, email recipients, labels).
**Key components:** Input field, chips for entered values, remove button on chips, autocomplete suggestions.
**Best example:** Gmail recipients, Notion tags, Linear labels
**Avoid when:** Single value selection, free-form text.
**See also:** Autocomplete Input, Multi-Select, Combobox

### Color Picker
**Category:** Data Entry
**When to use:** Selecting colors for customization (themes, labels, tags, branding).
**Key components:** Color spectrum/wheel, preset swatches, hex/RGB input, opacity slider, recently used.
**Best example:** Figma color picker, Notion cover colors
**Avoid when:** Predefined color options only (use swatches).
**See also:** Swatch Selector, Range Slider

### Combobox / Searchable Select
**Category:** Data Entry
**When to use:** Selecting from large option lists (7+ items) where type-to-filter is essential.
**Key components:** Text input, filterable dropdown, keyboard navigation, option grouping, create new option.
**Best example:** cmdk, Radix Combobox, Linear assignee picker
**Avoid when:** Fewer than 7 options (use native select or radio group).
**See also:** Select / Dropdown, Autocomplete Input, Multi-Select

### Date Picker
**Category:** Data Entry
**When to use:** Selecting dates or date ranges (booking, scheduling, filtering by date).
**Key components:** Calendar grid, month/year navigation, today highlight, range selection, time addition.
**Best example:** Airbnb date picker, Notion date property
**Avoid when:** Distant past dates (use direct input), time only (use time picker).
**See also:** Date Range Picker, Time Picker, Calendar View

### Date Range Picker
**Category:** Data Entry
**When to use:** Selecting start and end dates for filtering or booking periods.
**Key components:** Two calendar panels, start/end highlight, range shading, preset ranges (last 7 days, etc.).
**Best example:** Airbnb check-in/out, Stripe analytics range, Vercel
**Avoid when:** Single date selection, non-date ranges.
**See also:** Date Picker, Segmented Control (for presets)

### Drag and Drop
**Category:** Data Entry
**When to use:** Reordering items, moving between lists/columns, file upload, layout customization.
**Key components:** Drag handle, ghost/shadow preview, drop zone highlight, keyboard alternative.
**Best example:** Trello/Linear kanban, Notion block reordering, Figma layers
**Avoid when:** Simple sequential ordering (use up/down buttons), accessibility-only contexts.
**See also:** Kanban Board, File Upload, Sortable List

### File Upload
**Category:** Data Entry
**When to use:** Accepting file input from users (documents, images, videos, data imports).
**Key components:** Drop zone, file browser button, progress bar, file type validation, preview, cancel.
**Best example:** Notion file blocks, Figma import, Vercel deployment
**Avoid when:** Text-only input, camera-only capture on mobile.
**See also:** Drag and Drop, Image Upload, Progress Bar

### Form (Multi-Step)
**Category:** Data Entry
**When to use:** Complex data collection with 7+ fields that benefit from chunking into steps.
**Key components:** Step indicator, field groups per step, back/next/submit, validation per step, save progress.
**Best example:** Shopify checkout, Stripe onboarding, Typeform
**Avoid when:** Fewer than 7 fields (use single-page form), non-sequential fields.
**See also:** Stepper / Wizard, Form (Single Page), Progressive Disclosure

### Form (Single Page)
**Category:** Data Entry
**When to use:** Data collection with 2-6 fields that users can complete in one view.
**Key components:** Labeled inputs, validation, submit button, error summary, field grouping.
**Best example:** Stripe payment form, login forms
**Avoid when:** More than 7 fields (break into steps or sections), mobile with many fields.
**See also:** Form (Multi-Step), Input Group

### Image Upload
**Category:** Data Entry
**When to use:** Profile photos, product images, cover images, document scans.
**Key components:** Preview, crop/resize, drag-and-drop, file type/size validation, camera option on mobile.
**Best example:** Notion cover images, Figma asset import
**Avoid when:** Non-image files (use generic file upload).
**See also:** File Upload, Avatar, Drag and Drop

### Inline Editing
**Category:** Data Entry
**When to use:** Quick edits without navigating away (names, descriptions, prices, labels).
**Key components:** Click-to-edit text, input replaces display, save on blur/Enter, cancel on Escape.
**Best example:** Notion page titles, Airtable cells, Linear issue titles
**Avoid when:** Complex multi-field editing (use form/modal), sensitive data.
**See also:** Form (Single Page), Data Table

### Input Group
**Category:** Data Entry
**When to use:** Related inputs that form a logical unit (first + last name, address fields, date + time).
**Key components:** Grouped container, shared label, consistent styling, combined validation.
**Best example:** Stripe card input (number + expiry + CVC), address forms
**Avoid when:** Unrelated fields that happen to be near each other.
**See also:** Form (Single Page), Form (Multi-Step)

### Multi-Select
**Category:** Data Entry
**When to use:** Choosing multiple options from a large set with search and chip display.
**Key components:** Search input, checkbox list, selected chips, remove individual, clear all.
**Best example:** Notion multi-select property, Linear label picker
**Avoid when:** Binary choices (use checkbox), small option sets (<7, use checkbox group).
**See also:** Combobox, Checkbox Group, Chip Input

### Number Input / Stepper
**Category:** Data Entry
**When to use:** Numeric values with increment/decrement (quantity, age, order amounts).
**Key components:** Numeric input, +/- buttons, min/max bounds, step size, keyboard input.
**Best example:** E-commerce quantity selectors, Figma dimension inputs
**Avoid when:** Large ranges (use slider), currency (use formatted text input).
**See also:** Range Slider, Text Input

### OTP / Verification Input
**Category:** Data Entry
**When to use:** 2FA codes, email verification, phone verification (4-6 digit codes).
**Key components:** Individual digit boxes, auto-advance, paste support, auto-submit on complete, resend timer.
**Best example:** Stripe Radar, most auth flows
**Avoid when:** Long codes or non-numeric verification.
**See also:** Password Input, Pin Input

### Password Input
**Category:** Data Entry
**When to use:** Password entry for login, registration, or settings changes.
**Key components:** Masked input, show/hide toggle, strength meter for registration, requirements list.
**Best example:** 1Password, Stripe login
**Avoid when:** Non-sensitive text input.
**See also:** OTP Input, Text Input

### Phone Input
**Category:** Data Entry
**When to use:** International phone number entry with country code selection.
**Key components:** Country code dropdown with flags, number formatting, validation, auto-detect country.
**Best example:** Stripe phone verification, Twilio
**Avoid when:** Domestic-only apps where country code is unnecessary.
**See also:** Text Input, Select / Dropdown

### Pin Input
**Category:** Data Entry
**When to use:** Secure numeric codes (ATM pins, app lock, device pairing).
**Key components:** Masked dots, individual digit boxes, numeric keyboard on mobile, error shake.
**Best example:** iOS passcode entry, banking apps
**Avoid when:** Non-numeric codes (use regular input).
**See also:** OTP Input, Password Input

### Radio Button Group
**Category:** Data Entry
**When to use:** Mutually exclusive single selection from 2-5 visible options.
**Key components:** Circular indicators, labels, group label, one selected by default, vertical or horizontal layout.
**Best example:** Stripe pricing tier selection, survey forms
**Avoid when:** More than 5 options (use select/combobox), multi-select (use checkboxes).
**See also:** Segmented Control, Select / Dropdown, Checkbox

### Range Slider
**Category:** Data Entry
**When to use:** Selecting a value or range within a continuous spectrum (price, distance, volume).
**Key components:** Track, thumb(s), value label, min/max labels, step increments, dual thumbs for ranges.
**Best example:** Airbnb price filter, Spotify volume
**Avoid when:** Precise numeric input needed (use number input), very large ranges.
**See also:** Number Input, Date Range Picker

### Rich Text Editor
**Category:** Data Entry
**When to use:** Formatted content creation (documents, emails, descriptions, blog posts).
**Key components:** Formatting toolbar, keyboard shortcuts, markdown support, embeds, slash commands.
**Best example:** Notion, Linear descriptions, Slack message composer
**Avoid when:** Plain text only (use textarea), short inputs (use text input).
**See also:** Block Editor, Markdown Editor, Textarea

### Select / Dropdown
**Category:** Data Entry
**When to use:** Single selection from a short list (3-7 options) where native behavior is acceptable.
**Key components:** Trigger button with current value, options list, keyboard navigation, placeholder.
**Best example:** Native form selects, Stripe country picker (simple cases)
**Avoid when:** More than 7 options (use combobox), multi-select, custom option rendering needed.
**See also:** Combobox, Radio Button Group

### Signature Input
**Category:** Data Entry
**When to use:** Electronic signatures for contracts, agreements, delivery confirmation.
**Key components:** Canvas drawing area, clear button, type-to-sign alternative, touch support.
**Best example:** DocuSign, HelloSign
**Avoid when:** Simple agreement (use checkbox).
**See also:** File Upload, Canvas Drawing

### Text Input
**Category:** Data Entry
**When to use:** Single-line free-form text (names, emails, URLs, short answers).
**Key components:** Label, placeholder, validation, error message, helper text, character count, prefix/suffix.
**Best example:** Stripe forms (floating labels), Linear
**Avoid when:** Long text (use textarea), structured data (use specialized input).
**See also:** Textarea, Search Input, Password Input

### Textarea
**Category:** Data Entry
**When to use:** Multi-line free-form text (descriptions, comments, bio, notes).
**Key components:** Resizable area, character count, auto-grow, placeholder, min/max height.
**Best example:** GitHub issue body, Notion simple text blocks
**Avoid when:** Formatted text (use rich text editor), single-line input.
**See also:** Rich Text Editor, Text Input

### Time Picker
**Category:** Data Entry
**When to use:** Selecting specific times for scheduling, alarms, time entries.
**Key components:** Hour/minute selectors, AM/PM toggle, scrolling wheels on mobile, keyboard input.
**Best example:** iOS time picker, Google Calendar event time
**Avoid when:** Date+time together (use combined date-time picker), durations (use duration input).
**See also:** Date Picker, Select / Dropdown

### Toggle / Switch
**Category:** Data Entry
**When to use:** Binary on/off settings that take effect immediately without a save action.
**Key components:** Track, thumb, on/off states, optional label, immediate feedback.
**Best example:** iOS Settings toggles, Notion property toggles
**Avoid when:** Choices that need a save/submit action (use checkbox), multiple related options.
**See also:** Checkbox, Segmented Control

### Transfer List
**Category:** Data Entry
**When to use:** Moving items between two lists (assigning users, selecting permissions, configuring columns).
**Key components:** Source list, target list, add/remove buttons, search/filter, bulk select.
**Best example:** AWS security group rules, admin permission panels
**Avoid when:** Simple multi-select suffices, mobile (too space-intensive).
**See also:** Multi-Select, Drag and Drop

---

## Feedback & Status Patterns

### Confirmation Dialog
**Category:** Feedback & Status
**When to use:** Destructive or irreversible actions (delete, cancel subscription, remove team member).
**Key components:** Warning message, consequence description, confirm/cancel buttons, destructive button styling.
**Best example:** GitHub "Delete repository" (type name to confirm), Stripe cancellation
**Avoid when:** Reversible actions (use undo toast instead), non-destructive confirmations.
**See also:** Modal / Dialog, Toast with Undo

### Error Message (Field-Level)
**Category:** Feedback & Status
**When to use:** Validation errors on specific form fields.
**Key components:** Red text below field, error icon, specific message (not generic), triggered on blur or submit.
**Best example:** Stripe inline validation
**Avoid when:** Success feedback (use checkmark), warnings (use yellow).
**See also:** Error State, Form Validation Summary

### Error Page (Full)
**Category:** Feedback & Status
**When to use:** Unrecoverable errors (404, 500, permission denied, offline).
**Key components:** Error illustration, clear headline, helpful description, CTA (go home, retry, contact support).
**Best example:** GitHub 404 octocat, Notion offline page
**Avoid when:** Recoverable inline errors (handle in-place).
**See also:** Error State, Empty State

### Form Validation Summary
**Category:** Feedback & Status
**When to use:** Multiple form errors that need to be shown together after submission.
**Key components:** Error count, list of errors linking to fields, red banner at top, auto-scroll to first error.
**Best example:** Gov.uk form validation pattern
**Avoid when:** Single-field validation (use field-level), real-time validation.
**See also:** Error Message (Field-Level), Alert Banner

### Loading Spinner
**Category:** Feedback & Status
**When to use:** Short indeterminate waits (<2s) for button actions, inline operations.
**Key components:** Animated circle/dots, optional label, size variants, reduced-motion alternative.
**Best example:** Button loading states, Notion block loading
**Avoid when:** Page-level loading (use skeleton), determinate progress (use progress bar).
**See also:** Skeleton Screen, Progress Bar

### Notification Center
**Category:** Feedback & Status
**When to use:** Aggregated in-app notifications with read/unread states and history.
**Key components:** Bell icon trigger, notification list, read/unread states, mark all read, notification types.
**Best example:** GitHub notifications, Slack activity, Linear inbox
**Avoid when:** Real-time messaging (use chat), single notifications (use toast).
**See also:** Notification Badge, Toast, Alert Banner

### Offline Indicator
**Category:** Feedback & Status
**When to use:** When the app detects network loss and needs to inform the user.
**Key components:** Banner or badge, offline/online status, syncing indicator, queued actions count.
**Best example:** Slack offline bar, Google Docs offline mode
**Avoid when:** Apps with no offline implications.
**See also:** Alert Banner, Status Indicator

### Optimistic Update Feedback
**Category:** Feedback & Status
**When to use:** Actions that appear instant by updating UI before server confirmation.
**Key components:** Immediate UI update, background sync, error rollback, subtle sync indicator.
**Best example:** Linear (all mutations), Notion, Slack messages
**Avoid when:** Financial transactions, destructive actions, compliance-critical operations.
**See also:** Toast, Loading Spinner

### Permission Request
**Category:** Feedback & Status
**When to use:** Requesting device or data permissions (camera, location, notifications, contacts).
**Key components:** Pre-permission explanation, benefit statement, system prompt trigger, denied state handling.
**Best example:** iOS permission pattern (pre-prompt + system prompt)
**Avoid when:** Permissions not needed for current action (request just-in-time).
**See also:** Onboarding, Confirmation Dialog

### Progress Indicator (Determinate)
**Category:** Feedback & Status
**When to use:** File uploads, downloads, multi-step processes with known total.
**Key components:** Bar or ring, percentage, estimated time remaining, cancel option.
**Best example:** File upload progress, Vercel build progress
**Avoid when:** Unknown duration (use indeterminate spinner).
**See also:** Progress Bar, Progress Ring, Loading Spinner

### Pull-to-Refresh
**Category:** Feedback & Status
**When to use:** Mobile feeds and lists that may have new content since last load.
**Key components:** Overscroll gesture, spinner animation, content reload, haptic feedback.
**Best example:** Twitter/X, Instagram, most iOS apps
**Avoid when:** Desktop apps, real-time feeds that auto-update, non-list views.
**See also:** Loading Spinner, Infinite Scroll

### Rate Limit / Throttle Feedback
**Category:** Feedback & Status
**When to use:** When user hits action limits (API rate limits, message frequency, submission caps).
**Key components:** Clear message, cooldown timer, retry-after indicator, escalation path.
**Best example:** Slack message rate limit, API rate limit pages
**Avoid when:** Silently throttling without informing the user.
**See also:** Error Message, Toast

### Save Indicator
**Category:** Feedback & Status
**When to use:** Auto-save confirmation, showing when content was last saved.
**Key components:** "Saving..." / "Saved" text, cloud icon, timestamp of last save, error state.
**Best example:** Notion "Saved", Google Docs "All changes saved", Figma
**Avoid when:** Manual save workflows (use save button with confirmation).
**See also:** Optimistic Update, Status Indicator

### Session Timeout Warning
**Category:** Feedback & Status
**When to use:** Before automatically logging out inactive users (banking, healthcare, admin).
**Key components:** Countdown timer, extend session button, save work warning, auto-redirect.
**Best example:** Banking apps, healthcare portals
**Avoid when:** Apps without security-sensitive sessions.
**See also:** Confirmation Dialog, Modal

### Skeleton Loading
**Category:** Feedback & Status
**When to use:** Initial page/component load, data fetching states.
**Key components:** Gray shapes matching real content dimensions, shimmer animation, per-component.
**Best example:** Facebook, LinkedIn, Stripe Dashboard
**Avoid when:** Already loaded content refreshing, error states.
**See also:** Loading Spinner, Progress Bar

### Success State
**Category:** Feedback & Status
**When to use:** Confirming completed actions (order placed, payment processed, account created).
**Key components:** Checkmark animation, success message, next-step CTA, confetti for celebrations.
**Best example:** Stripe Checkout success, Duolingo lesson complete
**Avoid when:** Routine saves (use subtle toast), background processes.
**See also:** Toast, Confirmation Dialog

### Toast with Undo
**Category:** Feedback & Status
**When to use:** Reversible actions where immediate undo is valuable (archive, delete, move).
**Key components:** Action confirmation text, undo button, auto-dismiss timer (5-8s with undo), queued undo.
**Best example:** Gmail "Message archived — Undo", Notion block delete
**Avoid when:** Irreversible actions (use confirmation dialog first).
**See also:** Toast, Confirmation Dialog

### Typing Indicator
**Category:** Feedback & Status
**When to use:** Real-time messaging to show someone is composing a message.
**Key components:** Animated dots, user attribution, debounced display, timeout.
**Best example:** Slack, iMessage, WhatsApp
**Avoid when:** Non-real-time communication (email, comments).
**See also:** Presence Indicator, Chat Interface

---

## Social & Communication Patterns

### Activity Feed
**Category:** Social & Communication
**When to use:** Showing chronological user or system actions (team activity, project updates, audit logs).
**Key components:** Timestamped entries, actor avatars, action descriptions, grouping, filters.
**Best example:** GitHub activity, Linear activity, Notion page activity
**Avoid when:** Real-time messaging (use chat), analytics (use dashboard).
**See also:** Timeline, Notification Center, List / Feed

### Chat Interface
**Category:** Social & Communication
**When to use:** Real-time messaging between users or with AI assistants.
**Key components:** Message list, input composer, message bubbles, timestamps, read receipts, typing indicator.
**Best example:** Slack, iMessage, WhatsApp, ChatGPT
**Avoid when:** Async discussions (use comments), broadcast communication (use feed).
**See also:** Message Composer, Thread, AI Chat

### Comment Thread
**Category:** Social & Communication
**When to use:** Contextual discussion on specific content (documents, code, designs, issues).
**Key components:** Comment list, reply threading, @mentions, reactions, resolve/archive, edit/delete.
**Best example:** Figma comments, GitHub PR reviews, Notion comments
**Avoid when:** Real-time conversation (use chat), feedback without context.
**See also:** Thread, Activity Feed, Annotation

### Contact Card
**Category:** Social & Communication
**When to use:** Displaying contact information with communication actions.
**Key components:** Name, avatar, role, contact methods (email, phone, chat), quick action buttons.
**Best example:** iOS Contacts, LinkedIn profile cards
**Avoid when:** Non-person entities.
**See also:** Profile Card, Avatar

### Direct Message List
**Category:** Social & Communication
**When to use:** Inbox of 1:1 or group conversations.
**Key components:** Conversation previews, unread indicators, last message timestamp, search, online status.
**Best example:** Slack DMs, Instagram DMs, WhatsApp chats
**Avoid when:** Public/channel-based communication.
**See also:** Chat Interface, Notification Center

### Emoji Reaction
**Category:** Social & Communication
**When to use:** Quick emotional responses to messages or content without typing.
**Key components:** Emoji picker, reaction display under content, count aggregation, hover to see reactors.
**Best example:** Slack reactions, GitHub comment reactions, Notion
**Avoid when:** Formal contexts, structured feedback needs.
**See also:** Like / Vote Button, Comment Thread

### Follow / Subscribe Button
**Category:** Social & Communication
**When to use:** Opting into updates from a user, channel, topic, or entity.
**Key components:** Toggle button, follower count, confirmation, unfollow with confirmation.
**Best example:** Twitter/X follow, YouTube subscribe, GitHub watch
**Avoid when:** Mandatory relationships, one-time notifications.
**See also:** Notification Preferences, Like / Vote Button

### Group / Channel List
**Category:** Social & Communication
**When to use:** Browsing and selecting communication channels or groups.
**Key components:** Channel names with icons, unread badges, muted state, search, create new.
**Best example:** Slack channel list, Discord servers/channels
**Avoid when:** Single-channel apps, DM-only communication.
**See also:** Sidebar Navigation, Direct Message List

### Like / Vote Button
**Category:** Social & Communication
**When to use:** Simple binary or numeric feedback on content (likes, upvotes, hearts).
**Key components:** Icon button, animation on tap, count display, togglable state.
**Best example:** Instagram heart, Twitter/X like, Product Hunt upvote
**Avoid when:** Nuanced feedback needed (use rating), anonymous contexts.
**See also:** Emoji Reaction, Rating Input, Follow / Subscribe

### Mention / @-Mention
**Category:** Social & Communication
**When to use:** Referencing specific users or entities within text input.
**Key components:** @-trigger, autocomplete user list, linked mention display, notification to mentioned user.
**Best example:** Slack @mentions, GitHub @mentions, Notion @person
**Avoid when:** No user system, non-collaborative contexts.
**See also:** Autocomplete Input, Comment Thread

### Message Composer
**Category:** Social & Communication
**When to use:** Creating messages with rich features (attachments, formatting, mentions, emoji).
**Key components:** Text input, formatting toolbar, attachment button, emoji picker, send button, draft save.
**Best example:** Slack composer, Gmail compose, Linear comment
**Avoid when:** Simple single-line inputs.
**See also:** Rich Text Editor, Chat Interface

### Notification Preferences
**Category:** Social & Communication
**When to use:** Letting users control which notifications they receive and how.
**Key components:** Channel toggles (email, push, in-app), per-type settings, global mute, schedule.
**Best example:** Slack notification preferences, GitHub notification settings
**Avoid when:** Apps with minimal notification types.
**See also:** Settings Page, Toggle / Switch

### Presence Indicator
**Category:** Social & Communication
**When to use:** Showing user online/offline/away status in collaborative apps.
**Key components:** Colored dot on avatar (green/yellow/gray), status text, auto-detect idle.
**Best example:** Slack presence, Figma collaborators, Discord
**Avoid when:** Non-collaborative apps, privacy-sensitive contexts.
**See also:** Avatar, Typing Indicator, Avatar Group

### Profile Page
**Category:** Social & Communication
**When to use:** Dedicated user profile with activity, settings, and social information.
**Key components:** Avatar, name, bio, stats, activity feed, edit profile, content tabs.
**Best example:** GitHub profile, Twitter/X profile, LinkedIn
**Avoid when:** Non-social apps where profiles are settings-only.
**See also:** Profile Card, Settings Page

### Quote / Repost
**Category:** Social & Communication
**When to use:** Sharing or referencing others' content with attribution.
**Key components:** Embedded original content, quote author attribution, added commentary, share action.
**Best example:** Twitter/X retweet/quote, Slack message sharing
**Avoid when:** Original content creation only.
**See also:** Comment Thread, Share Sheet

### Share Sheet / Share Modal
**Category:** Social & Communication
**When to use:** Distributing content via multiple channels (link copy, social platforms, email, messaging).
**Key components:** Copy link button, platform icons, QR code, embed code, permission settings.
**Best example:** iOS share sheet, Notion share, Figma share
**Avoid when:** Private-only content with no sharing.
**See also:** Link Preview, Share Button

### Social Proof Display
**Category:** Social & Communication
**When to use:** Showing usage stats, testimonials, or social validation to build trust.
**Key components:** User counts, avatar stacks, testimonial cards, star ratings, trust badges.
**Best example:** Notion "Used by X teams", Product Hunt votes
**Avoid when:** B2B enterprise (use case studies instead), when numbers are low.
**See also:** Avatar Group, Stat Display, Testimonial

### Thread / Nested Replies
**Category:** Social & Communication
**When to use:** Organizing conversations into sub-discussions within a main feed or channel.
**Key components:** Reply indentation, thread view, reply count, thread summary in main feed.
**Best example:** Slack threads, Reddit comment threads, Discord threads
**Avoid when:** Linear conversation without branching needs.
**See also:** Comment Thread, Chat Interface

### User Directory
**Category:** Social & Communication
**When to use:** Browsing and searching team members or platform users.
**Key components:** Search, filters (role, team, location), user cards/list, contact actions.
**Best example:** Slack member directory, company intranets
**Avoid when:** Small teams where everyone is known.
**See also:** Data Table, Card Grid, Search & Filter

### Video Call Interface
**Category:** Social & Communication
**When to use:** Real-time video communication with multiple participants.
**Key components:** Video grid, self-view, mute/camera toggles, screen share, chat sidebar, participant list.
**Best example:** Zoom, Google Meet, FaceTime
**Avoid when:** Audio-only communication (simplify the UI).
**See also:** Chat Interface, Screen Share, Presence Indicator

---

## Commerce & Conversion Patterns

### Add-to-Cart Button
**Category:** Commerce & Conversion
**When to use:** E-commerce product pages, marketplace listings.
**Key components:** Primary CTA button, quantity selector, variant selection, cart badge update, animation.
**Best example:** Shopify stores, Amazon
**Avoid when:** Non-commerce products, free items (use "Get" or "Download").
**See also:** Buy Now Button, Cart, Product Card

### Buy Now / Express Checkout
**Category:** Commerce & Conversion
**When to use:** Reducing checkout friction for single-item or repeat purchases.
**Key components:** Single-click button, Apple Pay / Google Pay integration, saved payment methods.
**Best example:** Amazon Buy Now, Shopify Buy It Now, Apple Pay
**Avoid when:** Multi-item shopping where users need cart review.
**See also:** Add-to-Cart Button, Checkout Flow

### Cart / Bag
**Category:** Commerce & Conversion
**When to use:** Holding selected items before checkout in e-commerce.
**Key components:** Item list, quantity controls, remove, subtotal, promo code input, checkout CTA.
**Best example:** Shopify cart, Amazon cart
**Avoid when:** Single-item purchase flows, subscription-only products.
**See also:** Add-to-Cart Button, Checkout Flow, Cart Drawer

### Cart Drawer / Mini Cart
**Category:** Commerce & Conversion
**When to use:** Quick cart review without leaving the current page.
**Key components:** Slide-in drawer, cart items preview, quantity adjust, subtotal, proceed to checkout.
**Best example:** Shopify stores (modern themes), Nike
**Avoid when:** Complex cart needing full-page layout.
**See also:** Cart, Drawer / Sheet

### Checkout Flow
**Category:** Commerce & Conversion
**When to use:** Completing a purchase with shipping, payment, and confirmation.
**Key components:** Step indicator, shipping form, payment form, order summary, place order CTA.
**Best example:** Shopify Checkout, Stripe Checkout
**Avoid when:** Free products, subscription-only (use subscribe flow).
**See also:** Form (Multi-Step), Stepper / Wizard, Payment Form

### Comparison Table
**Category:** Commerce & Conversion
**When to use:** Helping users compare products, plans, or features side-by-side.
**Key components:** Feature rows, product/plan columns, checkmarks/values, sticky header, highlight recommended.
**Best example:** Stripe pricing, Apple product comparison
**Avoid when:** Fewer than 2 items to compare, simple products.
**See also:** Data Table, Pricing Table

### Coupon / Promo Code Input
**Category:** Commerce & Conversion
**When to use:** Applying discount codes during checkout.
**Key components:** Text input, apply button, success/error feedback, discount display, remove applied.
**Best example:** Shopify checkout, Amazon
**Avoid when:** No promo system, fully discounted products.
**See also:** Checkout Flow, Input Group

### Delivery Tracking
**Category:** Commerce & Conversion
**When to use:** Showing order fulfillment progress to customers.
**Key components:** Status timeline, current step highlight, estimated delivery, map view, carrier info.
**Best example:** Amazon tracking, Shopify order status page
**Avoid when:** Digital-only products.
**See also:** Timeline, Progress Bar, Map View

### Inventory / Stock Indicator
**Category:** Commerce & Conversion
**When to use:** Showing product availability (in stock, low stock, out of stock).
**Key components:** Color-coded label, quantity (optional), waitlist option for out-of-stock, urgency messaging.
**Best example:** Amazon "Only 3 left", Shopify stock indicators
**Avoid when:** Unlimited digital products.
**See also:** Badge / Tag, Status Indicator

### Order Summary
**Category:** Commerce & Conversion
**When to use:** Reviewing order details before purchase confirmation.
**Key components:** Item list with images, pricing breakdown, taxes, shipping, total, edit links.
**Best example:** Shopify checkout summary, Amazon order review
**Avoid when:** Single simple item (inline the details).
**See also:** Cart, Checkout Flow, Receipt

### Payment Form
**Category:** Commerce & Conversion
**When to use:** Collecting payment information for transactions.
**Key components:** Card number, expiry, CVC, billing address, card brand detection, Apple Pay/Google Pay.
**Best example:** Stripe Elements (the industry standard)
**Avoid when:** Free products, invoice-based billing.
**See also:** Checkout Flow, Form (Single Page)

### Paywall / Upgrade Prompt
**Category:** Commerce & Conversion
**When to use:** Converting free users to paid plans at feature boundaries.
**Key components:** Feature preview, plan benefits, pricing, CTA, dismiss option, current plan indicator.
**Best example:** Notion paywall, Spotify premium prompts
**Avoid when:** Free-only products, already-subscribed users.
**See also:** Pricing Table, Modal, Feature Gate

### Pricing Table
**Category:** Commerce & Conversion
**When to use:** Displaying plan options with features and pricing for SaaS products.
**Key components:** Plan columns, feature rows, pricing, billing toggle (monthly/annual), CTA per plan, recommended highlight.
**Best example:** Stripe pricing, Vercel pricing, Linear pricing
**Avoid when:** Single plan, custom enterprise pricing only.
**See also:** Comparison Table, Paywall

### Product Card
**Category:** Commerce & Conversion
**When to use:** E-commerce product listings in grid or list views.
**Key components:** Product image, name, price, rating, quick-add, wishlist, variant preview.
**Best example:** Shopify stores, Amazon listings
**Avoid when:** Non-product content (use generic card).
**See also:** Card, Card Grid, Product Page

### Product Gallery
**Category:** Commerce & Conversion
**When to use:** Showcasing product images on a product detail page.
**Key components:** Main image, thumbnail strip, zoom on hover, swipe on mobile, 360-view option.
**Best example:** Apple product pages, Shopify product images
**Avoid when:** Products without visual variety.
**See also:** Gallery View, Lightbox, Carousel

### Product Page
**Category:** Commerce & Conversion
**When to use:** Full product detail view for purchase consideration.
**Key components:** Gallery, title, price, variants, description, add-to-cart, reviews, related products.
**Best example:** Apple product pages, Shopify PDPs
**Avoid when:** Non-product detail pages.
**See also:** Product Gallery, Product Card, Reviews

### Receipt / Confirmation
**Category:** Commerce & Conversion
**When to use:** Post-purchase confirmation with order details.
**Key components:** Order number, item summary, payment method, shipping details, estimated delivery, support link.
**Best example:** Stripe receipts, Shopify order confirmation
**Avoid when:** Pre-purchase (use order summary).
**See also:** Success State, Order Summary

### Reviews / Ratings Display
**Category:** Commerce & Conversion
**When to use:** Showing customer feedback on products or services.
**Key components:** Star average, rating distribution bar, individual reviews, verified badge, helpful vote.
**Best example:** Amazon reviews, App Store ratings
**Avoid when:** Products without review system, B2B contexts where case studies are better.
**See also:** Rating Input, Social Proof, Testimonial

### Wishlist / Saved Items
**Category:** Commerce & Conversion
**When to use:** Saving products for later purchase consideration.
**Key components:** Heart/bookmark icon, saved items page, move-to-cart, share wishlist.
**Best example:** Amazon wishlist, Airbnb saved, Pinterest boards
**Avoid when:** Low-consideration impulse purchases.
**See also:** Like / Vote Button, Cart, Product Card

---

## Search & Filter Patterns

### Active Filter Display
**Category:** Search & Filter
**When to use:** Showing currently applied filters with clear/modify options.
**Key components:** Filter chips, remove individual, clear all, filter count, result count update.
**Best example:** Airbnb applied filters, Shopify admin filters
**Avoid when:** No active filters, single permanent filter.
**See also:** Filter Chip, Filter Bar, Faceted Search

### Command Bar Search
**Category:** Search & Filter
**When to use:** Search integrated into a command palette for power users.
**Key components:** Cmd+K trigger, type-ahead, mixed results (pages + actions + content), keyboard navigation.
**Best example:** Linear, Raycast, Vercel
**Avoid when:** Simple content search (use search input), non-technical users.
**See also:** Command Palette, Spotlight Search

### Date Filter
**Category:** Search & Filter
**When to use:** Filtering content by time period or date range.
**Key components:** Preset ranges (today, week, month, quarter), custom range picker, relative options.
**Best example:** Stripe analytics date filter, Google Analytics
**Avoid when:** Non-temporal data.
**See also:** Date Range Picker, Filter Bar

### Faceted Search / Filter
**Category:** Search & Filter
**When to use:** E-commerce and data-heavy apps with multiple filterable dimensions.
**Key components:** Filter groups (sidebar or modal), checkbox/range filters, result count, URL sync.
**Best example:** Amazon filters, Airbnb filters, Algolia
**Avoid when:** Simple content with one or two filter dimensions.
**See also:** Filter Bar, Active Filter Display, Search Input

### Filter Bar
**Category:** Search & Filter
**When to use:** Compact horizontal filter controls above a list or table.
**Key components:** Dropdown filters, active filter indicators, clear all, result count.
**Best example:** Linear issue filters, Stripe table filters
**Avoid when:** More than 5 filter dimensions (use faceted sidebar).
**See also:** Faceted Search, Active Filter Display, Segmented Control

### Filter Chip
**Category:** Search & Filter
**When to use:** Toggleable filter options displayed as a horizontal chip row.
**Key components:** Chip pills, single or multi-select, scrollable on mobile, active state styling.
**Best example:** Google Maps category chips, YouTube filter chips
**Avoid when:** Complex filters with ranges or dates (use faceted search).
**See also:** Chip, Active Filter Display, Segmented Control

### Filter Drawer (Mobile)
**Category:** Search & Filter
**When to use:** Complex filtering on mobile where screen space is limited.
**Key components:** Bottom sheet or full-screen modal, all filter groups, apply/clear buttons, result count preview.
**Best example:** Airbnb mobile filters, Shopify mobile
**Avoid when:** Desktop (use sidebar or filter bar), 1-2 simple filters.
**See also:** Drawer / Sheet, Faceted Search, Filter Bar

### Global Search
**Category:** Search & Filter
**When to use:** Searching across all content types in the application.
**Key components:** Search input, categorized results, recent searches, suggested queries, result previews.
**Best example:** Slack search, Notion search, Spotify search
**Avoid when:** Single content type (use contextual search).
**See also:** Command Bar Search, Spotlight Search

### Instant Search / Search-as-You-Type
**Category:** Search & Filter
**When to use:** Real-time results while the user types (< 200ms response).
**Key components:** Debounced input, live result list, loading indicator, highlight matching text.
**Best example:** Algolia InstantSearch, VS Code file search, Raycast
**Avoid when:** Heavy server queries (use submit-based search), privacy-sensitive contexts.
**See also:** Autocomplete Input, Search Input

### Recent / Saved Searches
**Category:** Search & Filter
**When to use:** Helping users quickly repeat previous searches.
**Key components:** History list, clear individual/all, save/pin searches, search suggestions.
**Best example:** Amazon search history, Google recent searches
**Avoid when:** Privacy-first apps where search history is sensitive.
**See also:** Search Input, Global Search

### Result Sorting
**Category:** Search & Filter
**When to use:** Letting users reorder search/list results by different criteria.
**Key components:** Sort dropdown (relevance, date, price, rating), ascending/descending toggle.
**Best example:** Amazon sort options, Airbnb sort
**Avoid when:** Fixed ordering that should not be changed (editorial content).
**See also:** Data Table (sortable columns), Filter Bar

### Saved Filters / Views
**Category:** Search & Filter
**When to use:** Letting users save complex filter combinations for reuse.
**Key components:** Save current filter state, name the view, quick-switch between views, share views.
**Best example:** Linear custom views, Airtable views, Notion database views
**Avoid when:** Simple filtering that does not need persistence.
**See also:** Faceted Search, Filter Bar, Tab Navigation

### Scope Selector
**Category:** Search & Filter
**When to use:** Narrowing search to a specific content type or section before searching.
**Key components:** Segmented control or dropdown, scope options (All, Files, People, Messages).
**Best example:** Slack search scope, macOS Spotlight categories
**Avoid when:** Single content type.
**See also:** Segmented Control, Search Input

### Search Input
**Category:** Search & Filter
**When to use:** Any searchable content area (lists, tables, pages, products).
**Key components:** Search icon, text input, clear button, loading indicator, keyboard shortcut hint.
**Best example:** Stripe search, GitHub search
**Avoid when:** Non-searchable content, fewer than 10 items.
**See also:** Global Search, Instant Search, Filter Bar

### Search Results Page
**Category:** Search & Filter
**When to use:** Displaying search results with metadata, filters, and pagination.
**Key components:** Result cards, match highlighting, filter sidebar, pagination, result count, sort.
**Best example:** Google Search, Algolia, Amazon
**Avoid when:** Instant search with inline results (use dropdown).
**See also:** Search Input, Faceted Search, Pagination

### Smart Suggestions
**Category:** Search & Filter
**When to use:** Proactively suggesting searches, filters, or content based on context or history.
**Key components:** Suggestion chips, personalized recommendations, trending searches, "Did you mean?"
**Best example:** Google "People also ask", Amazon suggested searches
**Avoid when:** Privacy-first contexts, simple exact-match search.
**See also:** Autocomplete Input, Recent Searches

### Toggle View (List/Grid)
**Category:** Search & Filter
**When to use:** Letting users switch between list and grid display of the same content.
**Key components:** View toggle icons (list/grid), persist preference, smooth transition.
**Best example:** macOS Finder views, Airbnb map/list toggle
**Avoid when:** Content that only works in one format.
**See also:** Segmented Control, Card Grid, List / Feed

### Type-Ahead / Predictive Search
**Category:** Search & Filter
**When to use:** Completing user queries with predicted terms as they type.
**Key components:** Input with prediction overlay, tab/right-arrow to accept, multiple suggestions.
**Best example:** Google Search autocomplete, GitHub Copilot
**Avoid when:** Exact-match-only search.
**See also:** Autocomplete Input, Instant Search

---

## Onboarding & Education Patterns

### Benefit-Oriented Welcome Screen
**Category:** Onboarding & Education
**When to use:** First screen after app install/signup, communicating core value proposition.
**Key components:** Hero illustration/animation, benefit statements, CTA (Get Started), skip option.
**Best example:** Duolingo welcome, Headspace, Notion
**Avoid when:** Returning users, power-user tools where users come with intent.
**See also:** Onboarding Carousel, Empty State

### Checklist Onboarding
**Category:** Onboarding & Education
**When to use:** Guiding new users through setup tasks that unlock product value.
**Key components:** Task list, completion checkmarks, progress bar, reward/celebration, skip option.
**Best example:** Notion "Getting Started", Linear onboarding, Stripe activation
**Avoid when:** Simple products with no setup, expert users.
**See also:** Stepper / Wizard, Progress Bar, Empty State

### Coach Mark / Spotlight
**Category:** Onboarding & Education
**When to use:** Highlighting a specific UI element to teach first-time users.
**Key components:** Dimmed overlay, spotlight on target element, tooltip with explanation, next/dismiss.
**Best example:** iOS new feature highlights, Slack tour
**Avoid when:** More than 3-5 steps (use interactive tutorial), expert users.
**See also:** Tooltip Tour, Feature Announcement

### Contextual Help / Inline Help
**Category:** Onboarding & Education
**When to use:** Providing help exactly where and when users need it, near relevant features.
**Key components:** Help icon (?) trigger, popover explanation, link to docs, dismissable.
**Best example:** Stripe Dashboard help popovers, GitHub documentation links
**Avoid when:** Self-explanatory interfaces, inline labels are sufficient.
**See also:** Tooltip, Popover, Help Center

### Empty State Onboarding
**Category:** Onboarding & Education
**When to use:** Using empty views as an opportunity to guide users toward first actions.
**Key components:** Illustration, instructional text, primary CTA to create first item, sample data option.
**Best example:** Linear empty project, Notion empty workspace
**Avoid when:** Views that are never empty (dashboards with defaults).
**See also:** Empty State, Checklist Onboarding

### Feature Announcement
**Category:** Onboarding & Education
**When to use:** Introducing new features to existing users.
**Key components:** Banner or modal, feature description, visual preview, try it CTA, dismiss.
**Best example:** Notion "What's New", Linear changelog, Figma feature popover
**Avoid when:** Minor bug fixes, features users will naturally discover.
**See also:** Changelog, Alert Banner, Coach Mark

### Feature Gate / Upsell
**Category:** Onboarding & Education
**When to use:** Showing locked features with upgrade prompts.
**Key components:** Disabled feature preview, lock icon, plan comparison, upgrade CTA.
**Best example:** Notion AI upsell, Spotify premium features
**Avoid when:** Already-subscribed users, free features.
**See also:** Paywall, Pricing Table

### Interactive Tutorial
**Category:** Onboarding & Education
**When to use:** Teaching complex features through guided hands-on practice.
**Key components:** Step-by-step instructions, highlighted UI targets, validation of user actions, skip option.
**Best example:** Figma onboarding tutorial, Duolingo lessons
**Avoid when:** Simple features, users who explicitly skip onboarding.
**See also:** Coach Mark, Checklist Onboarding, Tooltip Tour

### Onboarding Carousel
**Category:** Onboarding & Education
**When to use:** Mobile app first launch, 3-5 screens explaining key features and benefits.
**Key components:** Swipeable screens, page dots, skip button, get started on final screen.
**Best example:** Duolingo, Headspace, Cash App
**Avoid when:** Desktop apps, complex products needing interactive onboarding.
**See also:** Benefit-Oriented Welcome Screen, Stepper / Wizard

### Personalization Setup
**Category:** Onboarding & Education
**When to use:** Tailoring the product experience based on user preferences during onboarding.
**Key components:** Preference questions, selection UI (chips, toggles), preview of customized result.
**Best example:** Spotify genre selection, Notion workspace setup, TikTok interests
**Avoid when:** One-size-fits-all products, post-onboarding (move to settings).
**See also:** Form (Multi-Step), Checklist Onboarding

### Progress-Gated Onboarding
**Category:** Onboarding & Education
**When to use:** Unlocking features progressively as users demonstrate competency.
**Key components:** Level/milestone system, unlock notifications, feature preview, achievement badges.
**Best example:** Duolingo skill tree, gaming tutorials
**Avoid when:** Professional tools where all features should be immediately available.
**See also:** Checklist Onboarding, Feature Gate

### Sample Data / Template Gallery
**Category:** Onboarding & Education
**When to use:** Reducing cold-start by providing pre-built examples or templates.
**Key components:** Template cards, preview, one-click create from template, category filters.
**Best example:** Notion templates, Figma community, Vercel templates
**Avoid when:** Products where templates would mislead about functionality.
**See also:** Empty State Onboarding, Card Grid

### Tooltip Tour
**Category:** Onboarding & Education
**When to use:** Sequential walkthrough of 3-5 key features using positioned tooltips.
**Key components:** Numbered tooltips, next/back/skip, progress dots, element highlighting.
**Best example:** Slack workspace tour, Figma first-time tips
**Avoid when:** More than 5 stops (fatigue), mobile (tooltips are hard to position).
**See also:** Coach Mark, Interactive Tutorial

### Video Walkthrough
**Category:** Onboarding & Education
**When to use:** Complex features best explained visually, especially for non-technical users.
**Key components:** Embedded video, autoplay (muted), captions, skip option, chapter markers.
**Best example:** Loom product tours, Notion help videos
**Avoid when:** Simple features, users on slow connections (provide text alternative).
**See also:** Interactive Tutorial, Feature Announcement

### What's New / Changelog
**Category:** Onboarding & Education
**When to use:** Keeping users informed about product updates and improvements.
**Key components:** Version entries, date, feature descriptions, screenshots, categorized (new, improved, fixed).
**Best example:** Linear changelog, Notion "What's New", Arc release notes
**Avoid when:** Internal tools with verbal communication channels.
**See also:** Feature Announcement, Notification Center

---

## Settings & Preferences Patterns

### Account Settings
**Category:** Settings & Preferences
**When to use:** Managing user account details (name, email, password, profile photo).
**Key components:** Form fields, save button, email change verification, password change flow, delete account.
**Best example:** GitHub account settings, Stripe account
**Avoid when:** Anonymous/guest users.
**See also:** Profile Page, Security Settings

### API Key Management
**Category:** Settings & Preferences
**When to use:** Developer-facing products with API access.
**Key components:** Key list, create key, copy button, reveal/hide, revoke, scopes/permissions, last used.
**Best example:** Stripe API keys, Vercel tokens, OpenAI API keys
**Avoid when:** Non-developer products.
**See also:** Security Settings, Data Table

### Billing / Subscription Management
**Category:** Settings & Preferences
**When to use:** Managing payment methods, viewing invoices, changing plans.
**Key components:** Current plan display, change plan CTA, payment method, invoice history, cancel flow.
**Best example:** Stripe customer portal, Vercel billing
**Avoid when:** Free-only products.
**See also:** Pricing Table, Payment Form

### Dark Mode Toggle
**Category:** Settings & Preferences
**When to use:** System appearance preference (light, dark, system auto).
**Key components:** Three-way toggle (light/dark/system), instant preview, persistent preference.
**Best example:** Linear, Notion, GitHub
**Avoid when:** Brand-critical products that require a specific theme.
**See also:** Toggle / Switch, Segmented Control

### Data Export / Import
**Category:** Settings & Preferences
**When to use:** Portability features for downloading or uploading user data.
**Key components:** Export format selection (CSV, JSON, PDF), progress indicator, download link, import wizard.
**Best example:** Notion export, Google Takeout
**Avoid when:** No portable data.
**See also:** File Upload, Progress Bar

### Grouped Settings
**Category:** Settings & Preferences
**When to use:** Organizing many settings into logical sections.
**Key components:** Section headers, descriptions, toggle/input groups, save per section or global.
**Best example:** iOS Settings groups, GitHub notification settings
**Avoid when:** Fewer than 5 settings (use simple list).
**See also:** Accordion, Drill-Down Navigation

### Integration / Connected Apps
**Category:** Settings & Preferences
**When to use:** Managing third-party service connections.
**Key components:** Integration cards, connect/disconnect, OAuth flow, permission display, status indicator.
**Best example:** Notion integrations, Slack app directory, Zapier
**Avoid when:** No third-party integrations.
**See also:** Card Grid, Settings Page

### Language / Locale Selector
**Category:** Settings & Preferences
**When to use:** Multi-language products, international users.
**Key components:** Language dropdown/combobox, flag icons (optional, controversial), instant or save-required.
**Best example:** Google account language, Airbnb language
**Avoid when:** Single-language products.
**See also:** Combobox, Select / Dropdown

### Notification Settings
**Category:** Settings & Preferences
**When to use:** Controlling notification delivery channels and types.
**Key components:** Per-type toggles, channel selection (email, push, in-app), batch settings, quiet hours.
**Best example:** Slack notification preferences, GitHub, Linear
**Avoid when:** Apps with no notifications.
**See also:** Notification Preferences, Toggle / Switch, Grouped Settings

### Permission / Role Management
**Category:** Settings & Preferences
**When to use:** Team/organization settings for access control.
**Key components:** Role list, permission matrix, invite members, role assignment, audit log.
**Best example:** Notion workspace settings, GitHub org permissions, Vercel teams
**Avoid when:** Single-user apps.
**See also:** Data Table, Transfer List

### Privacy Settings
**Category:** Settings & Preferences
**When to use:** User control over data visibility, sharing, and tracking.
**Key components:** Visibility toggles, data sharing options, cookie preferences, data deletion request.
**Best example:** iOS Privacy settings, Google privacy dashboard
**Avoid when:** Apps collecting no personal data.
**See also:** Grouped Settings, Toggle / Switch

### Security Settings
**Category:** Settings & Preferences
**When to use:** Password management, 2FA setup, session management, security logs.
**Key components:** Password change, 2FA enable/disable, active sessions list, security log, recovery codes.
**Best example:** GitHub security settings, Stripe two-factor
**Avoid when:** Non-authenticated apps.
**See also:** Account Settings, OTP Input

### Settings Page Layout
**Category:** Settings & Preferences
**When to use:** The overall structure for a settings/preferences area.
**Key components:** Sidebar navigation (desktop) or drill-down (mobile), grouped sections, save confirmation.
**Best example:** iOS Settings, GitHub Settings, Linear Settings
**Avoid when:** Products with 1-2 settings (inline them).
**See also:** Sidebar Navigation, Drill-Down Navigation, Grouped Settings

### Team / Workspace Settings
**Category:** Settings & Preferences
**When to use:** Managing shared workspace configuration, members, and billing.
**Key components:** Team name/avatar, member list with roles, invite flow, billing section, danger zone.
**Best example:** Notion workspace settings, Linear team settings, Vercel
**Avoid when:** Single-user products.
**See also:** Permission Management, Account Settings

### Theme / Appearance Customization
**Category:** Settings & Preferences
**When to use:** User customization beyond dark mode (accent colors, density, font size).
**Key components:** Color palette selector, density toggle (compact/comfortable), font size slider, preview.
**Best example:** Arc Browser boost, Notion accent colors, Slack themes
**Avoid when:** Products with strict brand guidelines.
**See also:** Dark Mode Toggle, Range Slider

---

## Dashboard & Analytics Patterns

### Activity Heatmap
**Category:** Dashboard & Analytics
**When to use:** Showing activity distribution over time (contribution graphs, usage heat).
**Key components:** Grid of time periods, color intensity for activity level, tooltip details, legend.
**Best example:** GitHub contribution graph, Stripe activity heatmap
**Avoid when:** Non-temporal data, precise values needed.
**See also:** Chart (Area), Calendar View

### Alert / Threshold Indicator
**Category:** Dashboard & Analytics
**When to use:** Highlighting metrics that have crossed defined thresholds.
**Key components:** Color-coded severity (green/yellow/red), threshold lines on charts, notification trigger.
**Best example:** Vercel error rate alerts, monitoring dashboards
**Avoid when:** Informational-only dashboards with no actionable thresholds.
**See also:** Status Indicator, Alert Banner, Stat Display

### Comparison Dashboard
**Category:** Dashboard & Analytics
**When to use:** Side-by-side analysis of metrics across periods, segments, or entities.
**Key components:** Period selectors, comparison charts, delta indicators, percentage change.
**Best example:** Google Analytics comparison, Stripe period comparison
**Avoid when:** Single-metric views, real-time-only dashboards.
**See also:** Stat Display, Chart (Line), Date Range Picker

### Customizable Dashboard
**Category:** Dashboard & Analytics
**When to use:** Power users who need to configure their own metric layouts.
**Key components:** Widget library, drag-to-arrange, resize, save layouts, share dashboards.
**Best example:** Grafana, Datadog, Mixpanel
**Avoid when:** Simple dashboards with fixed KPIs, non-technical users.
**See also:** Bento Grid, Drag and Drop, Card Grid

### Dashboard Layout
**Category:** Dashboard & Analytics
**When to use:** Overview screens showing key metrics, charts, and status at a glance.
**Key components:** KPI cards row, primary chart, secondary charts/tables, date range selector, refresh.
**Best example:** Stripe Dashboard, Vercel analytics, Mercury
**Avoid when:** Single-purpose screens, content-focused pages.
**See also:** Stat Display, Chart (Line), Bento Grid

### Data Visualization Widget
**Category:** Dashboard & Analytics
**When to use:** Embedding individual chart/metric widgets within dashboards.
**Key components:** Widget container, title, chart/stat content, time range, expand to full, export.
**Best example:** Grafana panels, Stripe chart cards
**Avoid when:** Single full-page charts (just use the chart directly).
**See also:** Chart (Line), Stat Display, Card

### Drill-Down Analytics
**Category:** Dashboard & Analytics
**When to use:** Exploring data from summary to detail (click metric card to see breakdown).
**Key components:** Clickable summary metrics, detail view, breadcrumb trail, back navigation.
**Best example:** Stripe revenue → by product → by customer
**Avoid when:** Flat data with no hierarchy.
**See also:** Drill-Down Navigation, Dashboard Layout

### Funnel Visualization
**Category:** Dashboard & Analytics
**When to use:** Showing conversion rates through multi-step processes.
**Key components:** Stage bars with decreasing width, conversion rates between stages, drop-off highlights.
**Best example:** Mixpanel funnels, Google Analytics
**Avoid when:** Non-sequential processes, binary conversion (use single metric).
**See also:** Chart (Bar), Progress Bar, Timeline

### Geographic Map / Choropleth
**Category:** Dashboard & Analytics
**When to use:** Showing data distribution across geographic regions.
**Key components:** Map visualization, color-coded regions, tooltips, zoom/pan, legend.
**Best example:** Stripe global coverage, Google Analytics geo reports
**Avoid when:** Non-geographic data, precise values needed.
**See also:** Activity Heatmap, Chart (Bar)

### Leaderboard
**Category:** Dashboard & Analytics
**When to use:** Ranking entities by performance metrics (sales reps, products, regions).
**Key components:** Ranked list, position numbers, metric values, avatars/icons, trend arrows.
**Best example:** Salesforce leaderboards, gaming rankings
**Avoid when:** Non-competitive contexts, sensitive individual performance data.
**See also:** Data Table, List / Feed

### Live / Real-Time Dashboard
**Category:** Dashboard & Analytics
**When to use:** Monitoring real-time metrics (server status, live users, streaming analytics).
**Key components:** Auto-refreshing metrics, websocket/SSE updates, live charts, connection status, pause.
**Best example:** Vercel real-time logs, Datadog, Cloudflare
**Avoid when:** Historical-only analytics, batch-updated data.
**See also:** Dashboard Layout, Status Indicator, Sparkline

### Metric Breakdown Table
**Category:** Dashboard & Analytics
**When to use:** Detailed tabular breakdown of dashboard summary metrics.
**Key components:** Sortable columns, metric values, percentage of total, sparklines per row, export.
**Best example:** Stripe payments table, Google Analytics pages report
**Avoid when:** Visual trend analysis (use charts instead).
**See also:** Data Table, Dashboard Layout, Stat Display

### Report Builder
**Category:** Dashboard & Analytics
**When to use:** Custom report creation with flexible metrics, dimensions, and visualizations.
**Key components:** Metric selector, dimension picker, visualization type, filter builder, save/share/export.
**Best example:** Google Analytics custom reports, Mixpanel
**Avoid when:** Fixed reporting needs, non-analytical users.
**See also:** Customizable Dashboard, Faceted Search

### Scorecard
**Category:** Dashboard & Analytics
**When to use:** Executive summary of health metrics with status coloring.
**Key components:** Metric grid, green/yellow/red status, target vs. actual, trend arrows.
**Best example:** Executive dashboards, OKR tracking tools
**Avoid when:** Detailed analysis (supplement with drill-down).
**See also:** Stat Display, Dashboard Layout, Alert / Threshold

### Sparkline Grid
**Category:** Dashboard & Analytics
**When to use:** Compact overview of many metrics with trends in a dense layout.
**Key components:** Grid of metric + sparkline pairs, consistent sizing, color coding, hover detail.
**Best example:** Stripe overview, financial dashboards
**Avoid when:** Detailed chart analysis needed.
**See also:** Sparkline, Stat Display, Dashboard Layout

### Status Board
**Category:** Dashboard & Analytics
**When to use:** Monitoring operational health across multiple services or systems.
**Key components:** Service list, status indicators (operational/degraded/down), uptime bars, incident history.
**Best example:** Vercel status page, GitHub status, AWS health dashboard
**Avoid when:** Non-operational contexts.
**See also:** Status Indicator, Timeline, Alert / Threshold

### Time Series Chart
**Category:** Dashboard & Analytics
**When to use:** Primary data visualization for trends over time in analytics dashboards.
**Key components:** X-axis time, Y-axis metric, hover crosshair, multi-series, zoom, date range selector.
**Best example:** Stripe analytics, Vercel analytics, Grafana
**Avoid when:** Non-temporal data (use bar/pie).
**See also:** Chart (Line), Chart (Area), Sparkline

### Tree Map
**Category:** Dashboard & Analytics
**When to use:** Showing hierarchical data as proportional nested rectangles (storage, budgets, categories).
**Key components:** Nested rectangles, size by value, color by category, labels, hover detail.
**Best example:** Disk usage visualizers, portfolio allocation
**Avoid when:** Small data sets, precise value comparison.
**See also:** Chart (Pie / Donut), Bento Grid

### Usage Meter
**Category:** Dashboard & Analytics
**When to use:** Showing consumption against a quota or limit (storage, API calls, bandwidth).
**Key components:** Progress bar/ring, used/total values, threshold warning, upgrade CTA at limits.
**Best example:** Vercel usage, GitHub Actions minutes, Notion AI credits
**Avoid when:** Unlimited resources.
**See also:** Progress Bar, Progress Ring, Alert / Threshold

---

## Media & Content Patterns

### Audio Player
**Category:** Media & Content
**When to use:** Playing audio content (music, podcasts, voice messages).
**Key components:** Play/pause, progress bar, time display, volume, speed control, skip forward/back.
**Best example:** Spotify player, Apple Podcasts, Overcast
**Avoid when:** Video content (use video player), short sound effects.
**See also:** Video Player, Mini Player, Progress Bar

### Block Editor
**Category:** Media & Content
**When to use:** Structured content creation with different block types (text, images, embeds, code).
**Key components:** Block types, slash command menu, drag-to-reorder, block actions, nesting.
**Best example:** Notion, Craft, WordPress Gutenberg
**Avoid when:** Simple text input, structured forms (use form patterns).
**See also:** Rich Text Editor, Markdown Editor

### Code Editor
**Category:** Media & Content
**When to use:** Writing and editing code with syntax highlighting and developer features.
**Key components:** Syntax highlighting, line numbers, auto-indent, auto-complete, minimap, error gutter.
**Best example:** VS Code, CodeMirror, Monaco
**Avoid when:** Non-code text editing.
**See also:** Code Block, Rich Text Editor

### Content Feed
**Category:** Media & Content
**When to use:** Scrollable stream of mixed-type content (social posts, articles, updates).
**Key components:** Content cards, author attribution, timestamps, engagement actions, infinite scroll.
**Best example:** Twitter/X timeline, Instagram feed, LinkedIn feed
**Avoid when:** Structured data (use table), single content type with search needs.
**See also:** List / Feed, Activity Feed, Infinite Scroll

### Document Viewer
**Category:** Media & Content
**When to use:** Viewing documents (PDF, DOCX) within the application.
**Key components:** Page rendering, zoom, page navigation, search, download, annotation tools.
**Best example:** Google Docs viewer, Notion embedded PDFs
**Avoid when:** Editable documents (use document editor).
**See also:** Block Editor, Code Block

### Embed / Rich Preview
**Category:** Media & Content
**When to use:** Displaying previews of linked content (URLs, tweets, videos, maps).
**Key components:** Open Graph preview card, thumbnail, title, description, source domain.
**Best example:** Slack link unfurling, Notion embeds, Twitter card previews
**Avoid when:** Simple text links where preview adds no value.
**See also:** Link Preview, Card, Content Feed

### Image Gallery
**Category:** Media & Content
**When to use:** Browsing and viewing collections of images.
**Key components:** Grid/masonry layout, lightbox viewing, zoom, download, EXIF data, lazy loading.
**Best example:** Google Photos, Unsplash, Flickr
**Avoid when:** Single images, non-visual content.
**See also:** Gallery View, Masonry Layout, Lightbox

### Infinite Canvas
**Category:** Media & Content
**When to use:** Freeform spatial content arrangement (whiteboards, mind maps, design tools).
**Key components:** Pan/zoom, freeform placement, connections/arrows, minimap, collaboration cursors.
**Best example:** Figma canvas, Miro, tldraw, Excalidraw
**Avoid when:** Linear content, structured data.
**See also:** Block Editor, Kanban Board

### Markdown Editor
**Category:** Media & Content
**When to use:** Writing with markdown syntax, often with live preview.
**Key components:** Markdown input, preview pane (split or toggle), syntax shortcuts, toolbar for formatting.
**Best example:** GitHub issue editor, Obsidian, Bear
**Avoid when:** Non-technical users (use block editor), rich formatting needs beyond markdown.
**See also:** Rich Text Editor, Block Editor, Code Editor

### Media Grid
**Category:** Media & Content
**When to use:** Displaying mixed media thumbnails (images, videos) in a uniform grid.
**Key components:** Uniform thumbnail grid, play indicator for videos, selection mode, lazy loading.
**Best example:** Instagram profile grid, Google Photos
**Avoid when:** Text-heavy content, single media items.
**See also:** Card Grid, Gallery View, Masonry Layout

### Mini Player / Persistent Player
**Category:** Media & Content
**When to use:** Keeping media playback accessible while navigating the app.
**Key components:** Compact fixed bar, play/pause, track info, progress, tap to expand to full player.
**Best example:** Spotify mini player, Apple Music, YouTube mini player
**Avoid when:** Non-media apps, single-screen media consumption.
**See also:** Audio Player, Video Player

### PDF Viewer
**Category:** Media & Content
**When to use:** Viewing PDF documents in-app without downloading.
**Key components:** Page rendering, zoom, page navigation, text search, annotation, download.
**Best example:** Google Drive PDF viewer, Notion embedded PDFs
**Avoid when:** Editable content (convert to native format).
**See also:** Document Viewer, Image Gallery

### Podcast / Episode List
**Category:** Media & Content
**When to use:** Browsing audio/video episodes in a series.
**Key components:** Episode cards, play button, duration, description, download, progress indicator.
**Best example:** Apple Podcasts, Spotify podcasts, Overcast
**Avoid when:** Single audio files, non-episodic content.
**See also:** List / Feed, Audio Player, Content Feed

### Reading Mode / Focus Mode
**Category:** Media & Content
**When to use:** Distraction-free content consumption (articles, documentation, ebooks).
**Key components:** Simplified layout, hidden navigation, typography optimization, progress indicator.
**Best example:** Safari Reader, Medium, Notion full-width
**Avoid when:** Interactive content requiring navigation access.
**See also:** Document Viewer, Content Feed

### Slideshow / Presentation
**Category:** Media & Content
**When to use:** Sequential full-screen content presentation.
**Key components:** Full-screen slides, navigation (arrows/keys), slide thumbnails, presenter notes.
**Best example:** Google Slides, Keynote, Pitch
**Avoid when:** Non-sequential content, reference material.
**See also:** Carousel, Lightbox

### Story / Ephemeral Content
**Category:** Media & Content
**When to use:** Time-limited vertical media content (social stories, product highlights).
**Key components:** Full-screen vertical, auto-advance timer, tap to pause/skip, progress bars, reply.
**Best example:** Instagram Stories, Snapchat, WhatsApp Status
**Avoid when:** Permanent content, desktop-first experiences.
**See also:** Carousel, Content Feed

### Text-to-Speech Player
**Category:** Media & Content
**When to use:** Audio version of text content for accessibility or multitasking.
**Key components:** Play/pause, speed control, highlight current text, voice selection.
**Best example:** Speechify, Pocket, Medium audio
**Avoid when:** Short text, interactive content.
**See also:** Audio Player, Reading Mode

### Video Player
**Category:** Media & Content
**When to use:** Playing video content with standard controls.
**Key components:** Play/pause, progress bar, volume, fullscreen, quality selector, captions, speed.
**Best example:** YouTube, Vimeo, Loom
**Avoid when:** Audio-only content, GIFs/short loops.
**See also:** Audio Player, Mini Player, Video Gallery

### Video Thumbnail / Preview
**Category:** Media & Content
**When to use:** Preview of video content in lists and grids before playing.
**Key components:** Thumbnail image, play button overlay, duration badge, hover preview (animated).
**Best example:** YouTube thumbnails, Loom previews
**Avoid when:** Non-video content.
**See also:** Card, Media Grid, Video Player

### WYSIWYG Editor
**Category:** Media & Content
**When to use:** Visual editing where output matches what users see while editing.
**Key components:** Formatting toolbar, inline styling, media insertion, live preview matches output.
**Best example:** Webflow, Framer, Squarespace
**Avoid when:** Code editing (use code editor), structured data (use forms).
**See also:** Rich Text Editor, Block Editor

---

## AI & Intelligent Patterns

### AI Agent Task Card
**Category:** AI & Intelligent
**When to use:** Showing autonomous AI agent progress on multi-step tasks.
**Key components:** Task description, step list with status, progress indicator, logs, pause/cancel, result.
**Best example:** Claude Code task execution, Devin, GitHub Copilot Workspace
**Avoid when:** Simple single-step AI operations.
**See also:** Progress Bar, Timeline, Checklist

### AI Chat Interface
**Category:** AI & Intelligent
**When to use:** Conversational AI interactions (chatbots, assistants, copilots).
**Key components:** Message thread, user/AI bubbles, typing indicator, suggested prompts, code blocks, copy.
**Best example:** ChatGPT, Claude, Notion AI, GitHub Copilot Chat
**Avoid when:** Non-conversational AI (use inline suggestions), simple commands.
**See also:** Chat Interface, AI Sidebar

### AI Command Bar
**Category:** AI & Intelligent
**When to use:** Natural language actions integrated into command palette (AI + traditional commands).
**Key components:** Text input, AI interpretation indicator, action preview, confidence display, execute/edit.
**Best example:** Raycast AI, Notion AI command, Linear AI
**Avoid when:** Traditional exact-match command palettes are sufficient.
**See also:** Command Palette, AI Chat Interface

### AI Confidence Indicator
**Category:** AI & Intelligent
**When to use:** Showing reliability of AI-generated content or predictions.
**Key components:** Confidence score/bar, explanation of uncertainty, source attribution, verify prompt.
**Best example:** AI diagnostic tools, code review suggestions
**Avoid when:** Deterministic operations, non-AI features.
**See also:** Status Indicator, Progress Bar

### AI Content Suggestions
**Category:** AI & Intelligent
**When to use:** Inline AI-powered writing assistance (autocomplete, rephrase, expand).
**Key components:** Ghost text preview, tab to accept, alternative suggestions, dismiss, undo.
**Best example:** GitHub Copilot, Notion AI, Gmail Smart Compose
**Avoid when:** Users who prefer manual control, sensitive/legal content.
**See also:** Autocomplete Input, Rich Text Editor

### AI Feedback Loop
**Category:** AI & Intelligent
**When to use:** Collecting user feedback to improve AI outputs (thumbs up/down, corrections).
**Key components:** Rating buttons, correction input, regenerate, copy, flag inappropriate.
**Best example:** ChatGPT thumbs up/down, Claude feedback
**Avoid when:** Non-AI-generated content.
**See also:** Like / Vote Button, Emoji Reaction

### AI Generated UI
**Category:** AI & Intelligent
**When to use:** Dynamically rendering UI components based on AI interpretation of user intent.
**Key components:** Intent parser, component renderer, layout engine, fallback UI, edit generated result.
**Best example:** v0 by Vercel, Claude Artifacts, Galileo AI
**Avoid when:** Static known interfaces, compliance-critical UIs.
**See also:** AI Chat Interface, Block Editor

### AI Image Generation Inline
**Category:** AI & Intelligent
**When to use:** Creating images from text prompts within the product workflow.
**Key components:** Prompt input, generation progress, result gallery, variations, edit/refine, insert into content.
**Best example:** Midjourney, DALL-E in ChatGPT, Notion AI images
**Avoid when:** Pre-existing image libraries suffice, brand-controlled imagery.
**See also:** Image Upload, Gallery View, AI Chat Interface

### AI Model Selector
**Category:** AI & Intelligent
**When to use:** Letting users choose between AI models with different capabilities/costs.
**Key components:** Model list with descriptions, capability comparison, cost indicator, speed indicator.
**Best example:** ChatGPT model picker, Vercel AI SDK model routing
**Avoid when:** Single-model products, auto-routing is sufficient.
**See also:** Select / Dropdown, Comparison Table

### AI Prompt Templates
**Category:** AI & Intelligent
**When to use:** Pre-built prompts that guide users toward effective AI interactions.
**Key components:** Template cards, category filters, variable placeholders, one-click use, custom save.
**Best example:** ChatGPT prompt library, Notion AI templates
**Avoid when:** Expert users who write custom prompts.
**See also:** Sample Data / Template Gallery, AI Chat Interface

### AI Sidebar / Copilot Panel
**Category:** AI & Intelligent
**When to use:** Persistent AI assistant panel alongside the main workspace.
**Key components:** Side panel, chat interface, context awareness, suggested actions, collapse/expand.
**Best example:** GitHub Copilot sidebar, Notion AI, Microsoft Copilot
**Avoid when:** Full-screen AI experiences, simple inline suggestions.
**See also:** AI Chat Interface, Drawer / Sheet, Side Panel

### AI Source Attribution
**Category:** AI & Intelligent
**When to use:** Showing where AI-generated information comes from for trust and verification.
**Key components:** Inline citations, source links, confidence per source, expandable references.
**Best example:** Perplexity AI citations, Google AI Overviews
**Avoid when:** Creative generation where sources are not applicable.
**See also:** AI Confidence Indicator, Footnote

### AI Streaming Response
**Category:** AI & Intelligent
**When to use:** Displaying AI-generated text as it streams token by token.
**Key components:** Token-by-token rendering, cursor indicator, stop generation button, copy after complete.
**Best example:** ChatGPT, Claude, Notion AI
**Avoid when:** Short responses that load instantly, batch processing.
**See also:** AI Chat Interface, Loading Spinner, Typing Indicator

### AI Summarization
**Category:** AI & Intelligent
**When to use:** Condensing long content into key points using AI.
**Key components:** Summary card, expand to full content, key points, regenerate, adjust length.
**Best example:** Notion AI summarize, Slack thread summary, Arc Browse
**Avoid when:** Short content, content where nuance matters and summarization could mislead.
**See also:** Collapsible Section, AI Content Suggestions

### AI Tool Use / Function Calling Display
**Category:** AI & Intelligent
**When to use:** Showing when AI is using tools or calling functions during a conversation.
**Key components:** Tool invocation label, parameters shown, result preview, execution status, error handling.
**Best example:** ChatGPT plugins, Claude tool use, Anthropic function calling
**Avoid when:** Background tool use where user visibility is not needed.
**See also:** AI Agent Task Card, Timeline, Code Block

### AI Voice Interface
**Category:** AI & Intelligent
**When to use:** Voice-based AI interactions (voice assistants, voice commands).
**Key components:** Microphone button, waveform visualization, transcript display, voice feedback.
**Best example:** Siri, Google Assistant, Alexa, ChatGPT voice
**Avoid when:** Text-only contexts, noisy environments, accessibility-only audio.
**See also:** AI Chat Interface, Voice Command Overlay

### Contextual AI Assist
**Category:** AI & Intelligent
**When to use:** AI help triggered by user context (hovering over complex data, selecting text).
**Key components:** Context detection, assist popover, explain/simplify/translate actions, dismiss.
**Best example:** Notion AI on selection, Google Translate on select
**Avoid when:** Simple self-explanatory content, privacy-sensitive data.
**See also:** AI Content Suggestions, Popover, Tooltip

### Intelligent Autocomplete
**Category:** AI & Intelligent
**When to use:** AI-powered predictions that go beyond simple string matching.
**Key components:** Multi-token suggestions, ghost text, context-aware, learning from user patterns.
**Best example:** GitHub Copilot, TabNine, Gmail Smart Compose
**Avoid when:** Exact-match autocomplete is sufficient, low-trust environments.
**See also:** Autocomplete Input, AI Content Suggestions

### Prompt Input
**Category:** AI & Intelligent
**When to use:** Dedicated input for AI prompts with enhanced features.
**Key components:** Expandable textarea, attachment support, model selector, submit button, history.
**Best example:** ChatGPT prompt input, Claude input, Midjourney prompt
**Avoid when:** Non-AI text input.
**See also:** Textarea, AI Chat Interface, Message Composer

### Semantic Search
**Category:** AI & Intelligent
**When to use:** AI-powered search understanding intent rather than just keywords.
**Key components:** Natural language input, intent parsing, relevance scoring, related results, "Did you mean?"
**Best example:** Algolia NeuralSearch, Perplexity, Notion AI search
**Avoid when:** Exact keyword matching is required, simple small datasets.
**See also:** Global Search, AI Command Bar, Instant Search

---

## Mobile-Specific Patterns

### Action Sheet
**Category:** Mobile-Specific
**When to use:** Presenting a set of actions from the bottom of the screen on mobile.
**Key components:** Bottom sheet, action list, cancel button, destructive action styling, swipe to dismiss.
**Best example:** iOS action sheets, Google Photos share
**Avoid when:** Desktop (use dropdown/context menu), fewer than 2 actions.
**See also:** Drawer / Sheet, Contextual Menu

### App Clip / Instant App
**Category:** Mobile-Specific
**When to use:** Lightweight app experiences without full installation.
**Key components:** NFC/QR trigger, focused single-task UI, sign in with Apple/Google, upgrade prompt.
**Best example:** iOS App Clips, Android Instant Apps
**Avoid when:** Full app experiences, complex multi-screen flows.
**See also:** Deep Link Navigation, Onboarding

### Bottom Sheet
**Category:** Mobile-Specific
**When to use:** Contextual content or actions sliding up from the bottom on mobile.
**Key components:** Drag handle, snap points (partial/full), backdrop, swipe to dismiss, content scroll.
**Best example:** Apple Maps, Google Maps, iOS share sheet
**Avoid when:** Desktop (use side panel/modal), full-page content.
**See also:** Drawer / Sheet, Action Sheet, Modal

### Compact Mode / Dense Layout
**Category:** Mobile-Specific
**When to use:** Maximizing information density on small screens for power users.
**Key components:** Reduced spacing, smaller text, abbreviated labels, toggle to comfortable mode.
**Best example:** Gmail compact view, Linear mobile
**Avoid when:** First-time users, accessibility-critical contexts.
**See also:** Settings toggle, List / Feed

### Edge Swipe Gesture
**Category:** Mobile-Specific
**When to use:** Navigation via swipe from screen edges (back, forward, drawer reveal).
**Key components:** Edge detection, gesture animation, haptic feedback, conflict avoidance with content swipe.
**Best example:** iOS swipe-to-go-back, Android gesture navigation
**Avoid when:** Desktop, web apps where browser gestures conflict.
**See also:** Gesture Navigation, Bottom Navigation Bar

### Floating Action Button (Mobile)
**Category:** Mobile-Specific
**When to use:** Primary creation action on mobile screens.
**Key components:** Circular elevated button, bottom-right position, speed dial expansion, scroll-hide optional.
**Best example:** Gmail mobile compose, Google Maps layers
**Avoid when:** Multiple primary actions, screens without creation context.
**See also:** FAB, Bottom Navigation Bar

### Full-Screen Modal (Mobile)
**Category:** Mobile-Specific
**When to use:** Focused tasks on mobile that need the full screen (compose, create, edit).
**Key components:** Full-screen takeover, close/cancel top-left, save/done top-right, back gesture support.
**Best example:** Instagram create post, iOS compose email
**Avoid when:** Quick actions (use bottom sheet), information display (use pushed screen).
**See also:** Modal, Bottom Sheet, Drawer

### Haptic Feedback Pattern
**Category:** Mobile-Specific
**When to use:** Confirming actions through tactile response on mobile.
**Key components:** Impact feedback (light/medium/heavy), selection feedback, notification feedback.
**Best example:** iOS haptics throughout, Cash App payment confirmation
**Avoid when:** Web apps (limited support), accessibility-off contexts.
**See also:** Toggle / Switch, Pull-to-Refresh

### Long-Press Menu
**Category:** Mobile-Specific
**When to use:** Revealing secondary actions on mobile via long-press gesture.
**Key components:** Press-and-hold trigger, haptic feedback, context menu, preview (iOS), blur background.
**Best example:** iOS context menus, Instagram post options
**Avoid when:** Primary actions (should be visible), web apps (limited support).
**See also:** Action Sheet, Contextual Menu

### Mobile Form Optimization
**Category:** Mobile-Specific
**When to use:** Any form on mobile that needs to account for soft keyboard and thumb reach.
**Key components:** Large touch targets (44pt), input type for keyboard (email, tel, number), sticky submit.
**Best example:** Shopify mobile checkout, Stripe mobile forms
**Avoid when:** Desktop-only forms.
**See also:** Form (Single Page), Form (Multi-Step)

### Peek and Pop / Preview
**Category:** Mobile-Specific
**When to use:** Previewing content without fully navigating to it.
**Key components:** Long-press preview, quick actions, full open on deeper press, haptic feedback.
**Best example:** iOS link previews, 3D Touch previews
**Avoid when:** Web apps, Android (limited support), simple content.
**See also:** Long-Press Menu, Popover

### Pull-Down Quick Settings
**Category:** Mobile-Specific
**When to use:** Quick access to common toggles and settings from any screen.
**Key components:** Pull-down gesture, toggle grid, brightness/volume sliders, quick access icons.
**Best example:** iOS Control Center, Android Quick Settings
**Avoid when:** In-app contexts (use settings page), web apps.
**See also:** Settings Page, Action Sheet

### Reachability / One-Handed Use
**Category:** Mobile-Specific
**When to use:** Designing for thumb-zone ergonomics on large phones.
**Key components:** Bottom-positioned primary actions, pull-down reachability, avoid top-corner targets.
**Best example:** iOS Reachability, Arc Browser mobile, modern app bottom-focused layouts
**Avoid when:** Desktop, tablet in landscape.
**See also:** Bottom Navigation Bar, Bottom Sheet, FAB

### Swipe Actions on List Items
**Category:** Mobile-Specific
**When to use:** Quick actions on list items via horizontal swipe (archive, delete, pin).
**Key components:** Left/right swipe reveals, action icons with labels, color coding, haptic feedback.
**Best example:** iOS Mail swipe actions, Slack swipe, Todoist
**Avoid when:** Desktop (use hover actions), complex multi-action needs.
**See also:** List / Feed, Action Sheet, Gesture Navigation

### Thumb-Zone Optimized Layout
**Category:** Mobile-Specific
**When to use:** Any mobile interface prioritizing easy thumb reach on modern large phones.
**Key components:** Primary actions in bottom third, avoid top corners for frequent actions, large targets.
**Best example:** Modern iOS app layouts, Arc Browser mobile
**Avoid when:** Desktop/tablet layouts.
**See also:** Bottom Navigation Bar, Bottom Sheet, Reachability

---

## Collaboration Patterns

### Annotation / Comment Pinning
**Category:** Collaboration
**When to use:** Placing comments at specific locations on visual content (designs, documents, code).
**Key components:** Pin placement, comment thread at pin, resolved/open states, pin visibility toggle.
**Best example:** Figma comments, Google Docs suggestions, InVision
**Avoid when:** Non-visual, non-spatial content (use inline comments).
**See also:** Comment Thread, Multiplayer Cursors

### Branching / Versioning
**Category:** Collaboration
**When to use:** Working on variations without affecting the main version.
**Key components:** Branch creation, branch list, merge/conflict resolution, branch comparison.
**Best example:** Figma branching, Git branches, Notion
**Avoid when:** Simple single-version content, real-time-only collaboration.
**See also:** Version History, Diff View

### Collaborative Editing
**Category:** Collaboration
**When to use:** Multiple users editing the same content simultaneously.
**Key components:** Real-time sync, conflict resolution (CRDT/OT), cursor positions, change attribution.
**Best example:** Google Docs, Notion, Figma
**Avoid when:** Single-user tools, offline-only workflows.
**See also:** Multiplayer Cursors, Presence Indicator

### File Sharing / Handoff
**Category:** Collaboration
**When to use:** Sharing files or design assets between team members.
**Key components:** Share link generation, permission levels, download, preview, version tracking.
**Best example:** Figma share, Google Drive, Notion export
**Avoid when:** Internal-only systems with direct file access.
**See also:** Share Sheet, Permission Management

### Guest / External Access
**Category:** Collaboration
**When to use:** Giving limited access to non-team members (clients, contractors, reviewers).
**Key components:** Guest invite, scoped permissions, expiring access, guest indicator, audit trail.
**Best example:** Notion guest access, Figma viewer links, Slack Connect
**Avoid when:** Public content (no access control needed).
**See also:** Permission Management, Share Sheet

### Inline Suggestions / Track Changes
**Category:** Collaboration
**When to use:** Proposing edits that the content owner can accept or reject.
**Key components:** Suggested text with highlighting, accept/reject buttons, comment on suggestion, author.
**Best example:** Google Docs suggestions, GitHub PR reviews
**Avoid when:** Real-time co-editing where changes are immediately applied.
**See also:** Diff View, Comment Thread

### Live Presence Bar
**Category:** Collaboration
**When to use:** Showing who is currently viewing the same page or document.
**Key components:** Avatar stack, online indicator, click to follow, "N viewing" count.
**Best example:** Figma top bar, Notion presence, Google Docs
**Avoid when:** Single-user apps, non-collaborative views.
**See also:** Presence Indicator, Avatar Group

### Multiplayer Cursors
**Category:** Collaboration
**When to use:** Showing other users' cursor positions in real-time collaborative editing.
**Key components:** Colored cursor per user, name label, smooth movement, selection highlighting.
**Best example:** Figma, Google Docs, Notion (beta), tldraw
**Avoid when:** Non-spatial content, single-user tools.
**See also:** Presence Indicator, Collaborative Editing

### Notification / Mention in Context
**Category:** Collaboration
**When to use:** Alerting specific team members about relevant content.
**Key components:** @mention in comments/content, notification delivery, deep link to context.
**Best example:** Slack @mentions, Notion @person, GitHub @mentions
**Avoid when:** Broadcast notifications (use announcement), non-targeted alerts.
**See also:** Mention / @-Mention, Comment Thread

### Permission Indicator
**Category:** Collaboration
**When to use:** Showing the user's access level for the current content.
**Key components:** Role badge (Owner, Editor, Viewer), edit/view-only indicator, request access button.
**Best example:** Google Docs "Viewing" badge, Notion permission display
**Avoid when:** Single-user content, uniform access.
**See also:** Permission Management, Badge / Tag

### Real-Time Activity Log
**Category:** Collaboration
**When to use:** Showing live changes happening to shared content.
**Key components:** Timestamped actions, actor attribution, action descriptions, auto-scroll, filters.
**Best example:** Notion page activity, Figma activity, Google Docs activity
**Avoid when:** Non-collaborative tools, historical-only logs.
**See also:** Activity Feed, Timeline

### Resolution Workflow
**Category:** Collaboration
**When to use:** Managing review feedback through open/resolved states.
**Key components:** Open comments list, resolve button, resolved section, reopen, bulk resolve.
**Best example:** Figma resolved comments, GitHub PR review threads
**Avoid when:** Non-review contexts, single-author content.
**See also:** Comment Thread, Kanban Board

### Shared Workspace
**Category:** Collaboration
**When to use:** Team-level content organization with shared access.
**Key components:** Workspace name, member management, shared content, personal vs. shared areas.
**Best example:** Notion teamspaces, Figma teams, Slack workspaces
**Avoid when:** Individual-only tools.
**See also:** Team / Workspace Settings, Permission Management

### Task Assignment
**Category:** Collaboration
**When to use:** Assigning work items to specific team members.
**Key components:** Assignee selector, avatar display, due date, status, notification on assignment.
**Best example:** Linear assignees, Notion task assignment, Asana
**Avoid when:** Non-task content, single-user tools.
**See also:** Kanban Board, Avatar, Mention

### Watch / Follow Item
**Category:** Collaboration
**When to use:** Subscribing to updates on specific items without being assigned.
**Key components:** Watch toggle, subscriber list, notification on changes, unwatch option.
**Best example:** GitHub issue watch, Jira watchers, Linear subscribers
**Avoid when:** Auto-subscribed content (assigned tasks).
**See also:** Follow / Subscribe Button, Notification Preferences

---

## Quick Pattern Selection by Use Case

| I need to... | Start with | Consider also |
|---|---|---|
| Show a list of things | List / Feed, Data Table | Card Grid, Virtual List |
| Let users navigate | Sidebar (desktop), Bottom Nav (mobile) | Command Palette, Breadcrumbs |
| Collect user input | Text Input, Select, Combobox | Form (Multi-Step), Inline Editing |
| Show feedback | Toast (success), Alert Banner (system) | Confirmation Dialog (destructive) |
| Display metrics | Stat Display, Dashboard Layout | Chart (Line), Sparkline Grid |
| Enable search | Search Input, Global Search | Command Bar, Faceted Search |
| Onboard new users | Checklist, Empty State | Tooltip Tour, Welcome Screen |
| Build with AI | AI Chat Interface, AI Sidebar | AI Command Bar, AI Suggestions |
| Collaborate | Multiplayer Cursors, Comments | Presence, Real-Time Activity |
| Sell products | Product Card, Cart, Checkout | Pricing Table, Paywall |
