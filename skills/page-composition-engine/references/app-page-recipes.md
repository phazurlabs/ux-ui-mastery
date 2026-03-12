# App Page Composition Recipes

Complete block-by-block composition recipes for authenticated application pages. Each recipe specifies exact block order, spacing, layout structure, responsive behavior, and UX notes for product interfaces.

---

## Recipe APP-01: Dashboard Home Page

The primary view after login. Surfaces key metrics, recent activity, and quick actions. The most visited page in any SaaS product.

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ SIDEBAR NAV (persistent, 256px wide)                         │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TOP BAR                                                  │ │
│ │ Page title: "Dashboard" + search + notifications + avatar│ │
│ │ Height: 56-64px                                          │ │
│ │ Background: white, border-bottom                         │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ KPI CARD ROW                                             │ │
│ │ 4 cards in a row, equal width                            │ │
│ │   Each card: metric label (14px gray) +                  │ │
│ │   value (28-32px bold) + trend indicator (+5.2%)         │ │
│ │   Sparkline optional                                     │ │
│ │ Card height: 120px                                       │ │
│ │ Gap: 16-24px between cards                               │ │
│ │ Background: white cards on gray-50 page bg               │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ PRIMARY CHART                                            │ │
│ │ Full-width area or line chart                            │ │
│ │ Chart header: title + date range picker + view toggle    │ │
│ │ Height: 320-400px                                        │ │
│ │ Background: white card                                   │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ SECONDARY CHARTS ROW — 2 Charts Side by Side            │ │
│ │ Left (60%): Bar chart or stacked chart                   │ │
│ │ Right (40%): Donut/pie chart or small table              │ │
│ │ Height: 280px each                                       │ │
│ │ Gap: 24px                                                │ │
│ │ Background: white cards                                  │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ BOTTOM ROW — Activity Feed + Quick Actions              │ │
│ │ Left (65%): Activity feed                                │ │
│ │   10 items: avatar + action text + timestamp             │ │
│ │   "View All" link at bottom                              │ │
│ │ Right (35%): Quick actions card                          │ │
│ │   4-6 action buttons (icon + label)                      │ │
│ │   OR upcoming tasks / notifications                      │ │
│ │ Height: auto (content-driven)                            │ │
│ │ Gap: 24px                                                │ │
│ │ Background: white cards                                  │ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### Page Background
```
gray-50 (page) with white card surfaces
All cards: 1px border gray-200 or shadow-sm, border-radius 12px
```

### Spacing System
```
Page padding:      24px (all sides within main content area)
Between sections:  24px vertical
Card internal:     24px padding
Card gap:          16-24px (use consistent value throughout)
```

### Responsive Adjustments

**Tablet (sidebar collapsed):**
- Sidebar: collapsed to icon-only (64px) or hidden
- KPI cards: 2x2 grid
- Secondary charts: stacked vertically
- Bottom row: stacked (activity on top, quick actions below)

**Mobile (no sidebar):**
- Sidebar: bottom tab bar or hamburger menu
- KPI cards: horizontal scroll (show 2, swipe for more)
- All charts: full-width, stacked
- Chart heights: reduce to 240px
- Activity feed: last 5 items with "View All"
- Page padding: 16px

### UX Notes
- KPI cards load first (skeleton → data) — they set context
- Charts should have loading skeletons, not spinners
- Date range picker affects all charts simultaneously
- Quick actions should be the 4-6 most frequent user tasks
- Activity feed shows team activity, not just the user's

---

## Recipe APP-02: Settings Page

Organized configuration page with grouped form sections. Users visit infrequently but need to find things quickly.

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ SIDEBAR NAV (Settings active)                                │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TOP BAR                                                  │ │
│ │ "Settings" title + breadcrumb if nested                  │ │
│ │ Height: 56-64px                                          │ │
│ ├──────────────────────────────────────────────────────────┤ │
│ │ ┌──────────┬────────────────────────────────────────────┐│ │
│ │ │ SETTINGS │ SETTINGS CONTENT                           ││ │
│ │ │ SUB-NAV  │                                            ││ │
│ │ │          │ SECTION 1: General                         ││ │
│ │ │ General  │ ┌────────────────────────────────────────┐ ││ │
│ │ │ Account● │ │ Workspace name    [____________]       │ ││ │
│ │ │ Billing  │ │ Workspace URL     [____________]       │ ││ │
│ │ │ Team     │ │ Timezone          [Dropdown    ▼]      │ ││ │
│ │ │ Notifs   │ │ Language          [Dropdown    ▼]      │ ││ │
│ │ │ Security │ │                                        │ ││ │
│ │ │ API      │ │              [Save Changes]            │ ││ │
│ │ │ Integs   │ └────────────────────────────────────────┘ ││ │
│ │ │          │                                            ││ │
│ │ │ 200px    │ SECTION 2: Appearance                     ││ │
│ │ │          │ ┌────────────────────────────────────────┐ ││ │
│ │ │          │ │ Theme           ○ Light ○ Dark ○ Auto  │ ││ │
│ │ │          │ │ Accent color    [Color picker]         │ ││ │
│ │ │          │ │ Density         ○ Comfy ○ Compact      │ ││ │
│ │ │          │ │                                        │ ││ │
│ │ │          │ │              [Save Changes]            │ ││ │
│ │ │          │ └────────────────────────────────────────┘ ││ │
│ │ │          │                                            ││ │
│ │ │          │ SECTION 3: Danger Zone                    ││ │
│ │ │          │ ┌────────────────────────────────────────┐ ││ │
│ │ │          │ │ Delete workspace [Delete] (red/ghost)  │ ││ │
│ │ │          │ └────────────────────────────────────────┘ ││ │
│ │ └──────────┴────────────────────────────────────────────┘│ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### Layout Structure
```
Settings sub-nav:   200-240px wide, sticky, left side
Content area:       remaining width, max-width 720px
Section cards:      white background, 24px padding, 16px border-radius
Between sections:   32px vertical gap
Form field spacing: 20-24px between fields
```

### Responsive Adjustments

**Tablet:**
- Settings sub-nav: collapsible or horizontal tabs above content
- Content max-width: fill available space

**Mobile:**
- Settings sub-nav: horizontal scrollable tabs at top, or list view that drills into sections
- Each section: full-width card
- Page padding: 16px
- Save button: sticky bottom bar

### UX Notes
- Each section has its own Save button (not one global save)
- Danger zone at the bottom with red border and confirmation dialog
- Settings sub-nav highlights current section and scrolls content into view
- Unsaved changes: show warning dot on section and confirm on navigation away
- Group related settings — never present a flat list of 30+ toggles
- Search within settings for power users (optional but valuable)

---

## Recipe APP-03: Profile Page

User profile with identity, stats, and tabbed content. Can be own profile (editable) or another user's profile (view-only).

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ SIDEBAR NAV                                                  │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TOP BAR (page title hidden — profile header IS the title)│ │
│ ├──────────────────────────────────────────────────────────┤ │
│ │ COVER IMAGE                                              │ │
│ │ Full-width banner, 200-280px height                      │ │
│ │ Gradient or user-uploaded image                          │ │
│ │ Edit button (camera icon) if own profile                 │ │
│ ├── overlap: avatar extends 50% below cover ──────────────┤ │
│ │ PROFILE HEADER                                           │ │
│ │ ┌────────────────────────────────────────────────────┐   │ │
│ │ │ [Avatar 96px]                                      │   │ │
│ │ │ Name (24px bold) + @username (16px gray)           │   │ │
│ │ │ Bio text (16px, max 2 lines)                       │   │ │
│ │ │ Location + Link + Joined date (14px gray)          │   │ │
│ │ │ [Edit Profile] or [Follow] + [Message] buttons     │   │ │
│ │ └────────────────────────────────────────────────────┘   │ │
│ │ Padding: 24px sides, 48px top (to clear avatar overlap) │ │
│ ├── spacing: 16px ─────────────────────────────────────────┤ │
│ │ STATS BAR                                                │ │
│ │ 3-5 metrics inline: Posts (142) · Followers (3.2K) ·    │ │
│ │ Following (891) · Projects (24)                          │ │
│ │ Each clickable to view list                              │ │
│ │ Padding: 16px, border-bottom                             │ │
│ ├── spacing: 0px ──────────────────────────────────────────┤ │
│ │ PROFILE TABS                                             │ │
│ │ [Posts] [Projects] [Activity] [About]                    │ │
│ │ Underline active tab, sticky below top bar               │ │
│ │ Height: 48px                                             │ │
│ ├── spacing: 16px ─────────────────────────────────────────┤ │
│ │ TAB CONTENT                                              │ │
│ │                                                          │ │
│ │ Posts tab: Card grid (2-3 columns)                       │ │
│ │   Each: thumbnail + title + date + metrics               │ │
│ │                                                          │ │
│ │ Projects tab: Project cards with status badges           │ │
│ │                                                          │ │
│ │ Activity tab: Timeline list                              │ │
│ │   avatar + action + target + timestamp                   │ │
│ │                                                          │ │
│ │ About tab: Extended bio, skills, links, organizations    │ │
│ │                                                          │ │
│ │ Min-height: 400px (avoid layout shift on tab switch)     │ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### Responsive Adjustments

**Tablet:**
- Cover image: 160px height
- Content grid: 2 columns
- Stats bar: maintain inline

**Mobile:**
- Cover image: 120px height
- Avatar: 72px, centered
- Profile header: center-aligned text
- Stats bar: full-width with equal distribution
- Tabs: horizontal scroll if more than 4
- Content grid: single column
- Follow/Message buttons: full-width, stacked

### UX Notes
- Avatar overlaps the cover image — creates depth and visual interest
- "Edit Profile" only shows on own profile; "Follow" + "Message" on others
- Tab content preserves scroll position when switching tabs
- Empty states for tabs with no content yet
- Profile completeness indicator for own profile (encourages filling in bio, etc.)

---

## Recipe APP-04: List / Feed Page

The workhorse page for browsing collections of items. Used for contacts, projects, posts, products, tickets, and any list-based content.

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ SIDEBAR NAV                                                  │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TOP BAR                                                  │ │
│ │ Page title + "New Item" primary button                   │ │
│ ├── spacing: 0px ──────────────────────────────────────────┤ │
│ │ FILTER BAR                                               │ │
│ │ ┌────────────────────────────────────────────────────┐   │ │
│ │ │ [🔍 Search...     ] [Status ▼] [Type ▼] [Date ▼] │   │ │
│ │ │ [Sort: Newest ▼]        [≡ List] [⊞ Grid] [◫ Board]│  │ │
│ │ └────────────────────────────────────────────────────┘   │ │
│ │ Height: 56-64px                                          │ │
│ │ Background: white, border-bottom                         │ │
│ │ Sticky below top bar                                     │ │
│ ├── spacing: 0px (tight — filters relate to content) ──────┤ │
│ │ ACTIVE FILTERS CHIPS (conditional)                       │ │
│ │ [Status: Active ✕] [Type: Bug ✕] [Clear All]           │ │
│ │ Padding: 8px 16px, only shows when filters active        │ │
│ ├── spacing: 0px ──────────────────────────────────────────┤ │
│ │ RESULTS COUNT + BULK ACTIONS                             │ │
│ │ "247 results" + [☐ Select All] bulk action bar           │ │
│ │ Height: 40px                                             │ │
│ ├── spacing: 0px ──────────────────────────────────────────┤ │
│ │ LIST ITEMS                                               │ │
│ │ ┌────────────────────────────────────────────────────┐   │ │
│ │ │ [☐] [Avatar] Title          Status   Date    [···]│   │ │
│ │ │ [☐] [Avatar] Title          Status   Date    [···]│   │ │
│ │ │ [☐] [Avatar] Title          Status   Date    [···]│   │ │
│ │ │ [☐] [Avatar] Title          Status   Date    [···]│   │ │
│ │ │ [☐] [Avatar] Title          Status   Date    [···]│   │ │
│ │ │ ... (10-25 items per page)                         │   │ │
│ │ └────────────────────────────────────────────────────┘   │ │
│ │ Row height: 56-64px                                      │ │
│ │ Hover: gray-50 background                                │ │
│ │ Click: navigates to detail page                          │ │
│ ├── spacing: 0px ──────────────────────────────────────────┤ │
│ │ PAGINATION                                               │ │
│ │ [← Prev] [1] [2] [3] ... [12] [Next →]                 │ │
│ │ OR: infinite scroll with loading indicator               │ │
│ │ OR: "Load More" button                                   │ │
│ │ Padding: 16px, border-top                                │ │
│ ├── spacing: 0px ──────────────────────────────────────────┤ │
│ │ EMPTY STATE (when no results)                            │ │
│ │ Illustration + "No items found" + "Create First Item"   │ │
│ │ OR "Try adjusting your filters"                          │ │
│ │ Centered, min-height 300px                               │ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### View Variants

**List View (default):**
- Table-like rows with columns
- Checkbox + content columns + actions
- Column headers with sort indicators

**Grid View:**
- Cards in 3-4 column grid, 16px gap
- Card: thumbnail + title + metadata + status badge
- Card height: uniform (240-280px) or auto

**Board View (Kanban):**
- Columns by status: To Do | In Progress | Done
- Cards draggable between columns
- Column header: status + count

### Responsive Adjustments

**Tablet:**
- Grid view: 2 columns
- Board view: horizontal scroll
- Filter bar: search full-width, filters in dropdown

**Mobile:**
- List view: simplified rows (title + status only, swipe for actions)
- Grid view: 1-2 columns
- Board view: single column with tab switching between statuses
- Filter bar: collapsed into single "Filter" button that opens bottom sheet
- Pagination: infinite scroll preferred
- Bulk actions: hidden until selection mode activated

### UX Notes
- Search should be instant (debounced 300ms) with keyboard shortcut (Cmd+K)
- Filter state persists in URL (shareable filtered views)
- Empty state differs: no items ever vs. no results for current filters
- Skeleton loading: show 5-10 skeleton rows while loading
- Selection state: checkbox appears on hover (desktop) or long-press (mobile)
- View preference persists per user per list

---

## Recipe APP-05: Detail / Show Page

Individual item view with full information, related content, and actions. The destination from list pages.

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ SIDEBAR NAV                                                  │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TOP BAR + BREADCRUMB                                     │ │
│ │ ← Back / Items > Category > Item Name                    │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ ITEM HEADER                                              │ │
│ │ ┌────────────────────────────────────────────────────┐   │ │
│ │ │ Title (24-28px bold)                               │   │ │
│ │ │ Status badge + Created date + Author               │   │ │
│ │ │ [Edit] [Share] [Archive] [···More]                 │   │ │
│ │ └────────────────────────────────────────────────────┘   │ │
│ │ Padding-bottom: 24px, border-bottom                      │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ ┌─────────────────────────┬──────────────────────────┐   │ │
│ │ │ MAIN CONTENT (65-70%)   │ SIDEBAR (30-35%)         │   │ │
│ │ │                         │                          │   │ │
│ │ │ Content body:           │ Details card:            │   │ │
│ │ │ Rich text, images,      │  Assignee: [avatar]      │   │ │
│ │ │ embeds, code blocks     │  Priority: High          │   │ │
│ │ │                         │  Due date: Mar 15        │   │ │
│ │ │ Max-width: 720px        │  Labels: [tag] [tag]     │   │ │
│ │ │                         │  Project: Acme           │   │ │
│ │ │                         │                          │   │ │
│ │ │                         │ Related items card:      │   │ │
│ │ │                         │  - Related item 1        │   │ │
│ │ │                         │  - Related item 2        │   │ │
│ │ │                         │  + Add relation          │   │ │
│ │ │                         │                          │   │ │
│ │ │                         │ Attachments card:        │   │ │
│ │ │                         │  file.pdf (2.3MB)        │   │ │
│ │ │                         │  + Add attachment        │   │ │
│ │ ├─────────────────────────┼──────────────────────────┤   │ │
│ │ │ ACTIVITY / COMMENTS     │                          │   │ │
│ │ │ Tab: Comments | History │                          │   │ │
│ │ │                         │                          │   │ │
│ │ │ [Avatar] User comment   │                          │   │ │
│ │ │ [Avatar] User comment   │                          │   │ │
│ │ │                         │                          │   │ │
│ │ │ [Add comment input]     │                          │   │ │
│ │ └─────────────────────────┴──────────────────────────┘   │ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### Responsive Adjustments

**Tablet:**
- Sidebar: collapses below main content
- Main content takes full width

**Mobile:**
- All stacked: header → content → details → related → comments
- Details card: horizontal key-value pairs
- Actions: bottom action bar (sticky)
- Back button prominent in top bar
- Comments: last 3 shown with "View All"

### UX Notes
- Breadcrumb provides context and quick navigation back
- Header actions prioritized: most common action first, overflow in "More" menu
- Sidebar details are editable inline (click to change assignee, etc.)
- Comments load separately (don't block main content)
- Activity/History tab shows audit trail (who changed what, when)
- Keyboard shortcuts: E for edit, Cmd+Enter to comment

---

## Recipe APP-06: Editor / Canvas Page

Full-screen creative workspace for building, writing, or designing. Maximizes workspace area.

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ EDITOR TOP BAR (full width — no sidebar)                     │
│ ← Back  |  Document Title (editable)  |  [Undo][Redo]      │
│ [Share] [Export] [Save] | Avatar                             │
│ Height: 48px, border-bottom                                  │
├──────────────────────────────────────────────────────────────┤
│ TOOLBAR                                                      │
│ Formatting tools, insert options, mode toggles               │
│ Height: 40-48px, border-bottom                               │
│ Contextual: changes based on selection                       │
├──────────────────────────────────────────────────────────────┤
│ ┌──────────┬─────────────────────────┬───────────┐          │
│ │ LAYERS / │ CANVAS / EDITOR         │ PROPERTIES│          │
│ │ OUTLINE  │                         │ PANEL     │          │
│ │          │ The main workspace      │           │          │
│ │ Tree     │ area where content      │ Selection │          │
│ │ view of  │ is created and          │ properties│          │
│ │ document │ manipulated.            │ Fill, size│          │
│ │ layers   │                         │ position, │          │
│ │ or       │ Background: white,      │ style     │          │
│ │ sections │ checkered (for canvas), │ controls  │          │
│ │          │ or editor bg            │           │          │
│ │ Width:   │                         │ Width:    │          │
│ │ 240px    │ Flex: 1 (fills space)   │ 280-320px │          │
│ │          │                         │           │          │
│ │ Toggle-  │ Zoom controls at bottom │ Toggle-   │          │
│ │ able     │ left: [−] 100% [+] Fit  │ able      │          │
│ └──────────┴─────────────────────────┴───────────┘          │
├──────────────────────────────────────────────────────────────┤
│ STATUS BAR (optional)                                        │
│ Word count | Cursor position | Zoom level | Connection       │
│ Height: 28px                                                 │
└──────────────────────────────────────────────────────────────┘
```

### Responsive Adjustments

**Tablet:**
- Layers panel: hidden by default, toggle overlay
- Properties panel: hidden by default, toggle overlay or bottom sheet
- Toolbar: simplified, overflow into "More" menu

**Mobile:**
- Top bar: minimal (back + title + save)
- Toolbar: bottom toolbar (thumb-reachable)
- No side panels — tap selection opens bottom sheet for properties
- Canvas: pinch-to-zoom, pan with two fingers
- Status bar: hidden

### UX Notes
- Sidebar nav HIDDEN — editors are full-screen focused experiences
- Auto-save with "Saved" indicator in top bar (or "Saving..." / "Offline")
- Keyboard shortcuts are critical: Cmd+S, Cmd+Z, Cmd+Shift+Z
- Selection drives context: toolbar and properties panel change based on selection
- Panels are resizable (drag border) and collapsible (double-click border)
- Collaboration indicators: other users' cursors, presence avatars in top bar

---

## Recipe APP-07: Chat / Messaging Page

Real-time messaging interface. Can be standalone (Slack-like) or embedded (in-app support chat).

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ ┌───────────┬─────────────────────────┬──────────────┐      │
│ │ THREAD    │ MESSAGE STREAM          │ THREAD DETAIL│      │
│ │ LIST      │                         │ (optional)   │      │
│ │           │ CONVERSATION HEADER     │              │      │
│ │ Search    │ [Avatar] Channel Name   │ Shows when   │      │
│ │ [______]  │ 3 members · Active      │ a thread is  │      │
│ │           │ [Pin] [Search] [···]    │ opened from  │      │
│ │ Channels: │ ─────────────────────── │ the main     │      │
│ │ # general │                         │ stream       │      │
│ │ # design  │ [Avatar] User  10:32 AM │              │      │
│ │ # dev     │ Message text here with  │ Width:       │      │
│ │           │ formatting support.     │ 320-400px    │      │
│ │ DMs:      │                         │              │      │
│ │ ○ Alice   │ [Avatar] User  10:45 AM │ Toggle-      │      │
│ │ ○ Bob     │ Message with an         │ able         │      │
│ │ ● Carol(2)│ [image attachment]      │              │      │
│ │           │                         │              │      │
│ │ Width:    │ [Avatar] User  11:02 AM │              │      │
│ │ 260-280px │ Message text continued  │              │      │
│ │           │ with a code block:      │              │      │
│ │ Unread    │ ```code here```         │              │      │
│ │ badges on │                         │              │      │
│ │ channels  │ ─── Today ────────────  │              │      │
│ │           │                         │              │      │
│ │           │ [Avatar] User  9:15 AM  │              │      │
│ │           │ Latest message here     │              │      │
│ │           │                         │              │      │
│ │           │ ─────────────────────── │              │      │
│ │           │ MESSAGE INPUT           │              │      │
│ │           │ [+] [B I ~ S] Type msg  │              │      │
│ │           │ [📎 Attach] [Send →]    │              │      │
│ │           │ Height: 48px min,       │              │      │
│ │           │ grows with content      │              │      │
│ └───────────┴─────────────────────────┴──────────────┘      │
└──────────────────────────────────────────────────────────────┘
```

### Responsive Adjustments

**Tablet:**
- Thread detail panel: overlay or hidden
- Thread list: narrower (200px)

**Mobile:**
- Three-screen navigation: Thread list → Message stream → Thread detail
- Thread list: full screen
- Tap channel: slides to message stream (full screen)
- Back button returns to thread list
- Input: sticky at bottom with safe area inset
- Swipe right on message for thread/reactions

### UX Notes
- Message stream scrolls from bottom (newest at bottom)
- New message indicator when scrolled up: "↓ New messages"
- Typing indicator: "Alice is typing..."
- Message grouping: consecutive messages from same user collapse avatar
- Date separators between day boundaries
- Reactions: emoji picker on hover/long-press
- File drops anywhere in the message area
- Cmd+Enter to send (or just Enter, configurable)

---

## Recipe APP-08: Calendar Page

Event management with multiple view modes. Dense information display with strong time orientation.

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ SIDEBAR NAV                                                  │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TOP BAR                                                  │ │
│ │ "Calendar" + [Today] [< >] March 2026                    │ │
│ │ [Day] [Week] [Month] view toggle                         │ │
│ │ [+ New Event] button                                     │ │
│ ├──────────────────────────────────────────────────────────┤ │
│ │ ┌──────────┬─────────────────────────────────────────┐   │ │
│ │ │ MINI     │ CALENDAR GRID                           │   │ │
│ │ │ CALENDAR │                                         │   │ │
│ │ │          │ MONTH VIEW:                             │   │ │
│ │ │ March    │ Mon Tue Wed Thu Fri Sat Sun             │   │ │
│ │ │ [mini    │ ┌───┬───┬───┬───┬───┬───┬───┐          │   │ │
│ │ │ month    │ │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │          │   │ │
│ │ │ grid]    │ │   │evt│   │evt│   │   │   │          │   │ │
│ │ │          │ ├───┼───┼───┼───┼───┼───┼───┤          │   │ │
│ │ │ ──────── │ │ 8 │ 9 │10 │11 │12 │13 │14 │          │   │ │
│ │ │          │ │evt│   │   │evt│evt│   │   │          │   │ │
│ │ │ Calendars│ ├───┼───┼───┼───┼───┼───┼───┤          │   │ │
│ │ │ ☑ Work   │ │   │   │   │   │   │   │   │          │   │ │
│ │ │ ☑ Personal│ └───┴───┴───┴───┴───┴───┴───┘          │   │ │
│ │ │ ☐ Holidays│                                         │   │ │
│ │ │          │ WEEK VIEW:                              │   │ │
│ │ │ Width:   │ Time column (60px) + 7 day columns      │   │ │
│ │ │ 240px    │ Events as positioned blocks              │   │ │
│ │ │          │ All-day events in top row                │   │ │
│ │ │          │                                         │   │ │
│ │ │          │ DAY VIEW:                               │   │ │
│ │ │          │ Time column + single day + event details │   │ │
│ │ └──────────┴─────────────────────────────────────────┘   │ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### Event Detail (Popover / Side Panel)
```
Click event → popover or right panel slides in:
  Event title (20px bold)
  Date + time
  Location
  Description
  Attendees (avatars)
  [Edit] [Delete] [Close]
Panel width: 320-400px
```

### Responsive Adjustments

**Tablet:**
- Mini calendar sidebar: hidden, accessible via toggle
- Week view: show 5 days (workweek)
- Month view: truncate event text

**Mobile:**
- Default to day or agenda (list) view
- Month view: dots indicating events, tap to see day
- Mini calendar: top sheet/dropdown
- Calendar toggles: bottom sheet
- New event: full-screen modal
- Swipe left/right to change day/week

### UX Notes
- Click empty time slot to create event at that time
- Drag event to reschedule (desktop only)
- Drag event edge to resize duration (desktop only)
- Color-coded by calendar source
- Current time indicator: red horizontal line in week/day view
- Keyboard navigation: arrow keys to move between days

---

## Recipe APP-09: Analytics Page

Data-rich reporting page with configurable date ranges and multiple visualization types.

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ SIDEBAR NAV                                                  │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TOP BAR                                                  │ │
│ │ "Analytics" + [Date Range Picker] + [Compare ▼]          │ │
│ │ [Export ↓] [Schedule Report]                             │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ KPI SUMMARY ROW                                          │ │
│ │ 5-6 metrics: Visitors, Conversions, Revenue, etc.        │ │
│ │ Each: value + change vs. previous period (+12.5%)        │ │
│ │ Conditional colors: green for up, red for down           │ │
│ │ Card height: 100px, gap: 16px                            │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ PRIMARY CHART                                            │ │
│ │ Line/area chart with comparison overlay                   │ │
│ │ Metric selector tabs above chart                         │ │
│ │ Tooltip on hover showing exact values                    │ │
│ │ Height: 360px                                            │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ CHART GRID — 2x2                                         │ │
│ │ ┌──────────────────┬──────────────────┐                  │ │
│ │ │ Traffic Sources   │ Top Pages        │                  │ │
│ │ │ (Donut chart)     │ (Horizontal bar) │                  │ │
│ │ │ Height: 280px     │ Height: 280px    │                  │ │
│ │ ├──────────────────┼──────────────────┤                  │ │
│ │ │ Geo Distribution  │ Device Types     │                  │ │
│ │ │ (Map or bar)      │ (Donut + list)   │                  │ │
│ │ │ Height: 280px     │ Height: 280px    │                  │ │
│ │ └──────────────────┴──────────────────┘                  │ │
│ │ Gap: 24px                                                │ │
│ ├── spacing: 24px ─────────────────────────────────────────┤ │
│ │ DATA TABLE                                               │ │
│ │ Sortable columns: Page, Views, Unique, Bounce, Duration  │ │
│ │ Search + filter within table                             │ │
│ │ Pagination: 25/50/100 per page                           │ │
│ │ Export: CSV, PDF                                          │ │
│ ├── spacing: 16px ─────────────────────────────────────────┤ │
│ │ EXPORT / ACTIONS BAR                                     │ │
│ │ [Download CSV] [Download PDF] [Share Dashboard Link]     │ │
│ │ Padding: 16px, border-top                                │ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### Responsive Adjustments

**Tablet:**
- KPI row: 3+3 (two rows of 3) or horizontal scroll
- Chart grid: single column stack
- Data table: horizontal scroll

**Mobile:**
- KPI row: horizontal scroll
- All charts: full-width, stacked
- Chart height: reduce to 240px
- Data table: card view (each row becomes a card)
- Date range picker: full-screen modal
- Export: share sheet

### UX Notes
- Date range picker is the global control — everything responds to it
- Comparison period (vs. previous month/year) shown as dotted line on charts
- All charts should have loading skeletons, not spinners
- Hover/tap chart data points for exact values
- Drag-to-select time range on primary chart for drill-down
- Empty states for new accounts: "Start tracking to see data here"

---

## Recipe APP-10: File Manager Page

File browsing and management interface. Supports grid and list views with preview capabilities.

### Block Stack

```
┌──────────────────────────────────────────────────────────────┐
│ SIDEBAR NAV                                                  │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ TOP BAR                                                  │ │
│ │ "Files" + [🔍 Search] + [Upload ↑] + [New Folder +]     │ │
│ ├── spacing: 0px ──────────────────────────────────────────┤ │
│ │ BREADCRUMB PATH                                          │ │
│ │ Home > Projects > Design > Assets                        │ │
│ │ Clickable segments, dropdown on each for siblings        │ │
│ │ Height: 40px, border-bottom                              │ │
│ ├── spacing: 0px ──────────────────────────────────────────┤ │
│ │ VIEW CONTROLS                                            │ │
│ │ [≡ List] [⊞ Grid] | Sort: [Name ▼] | [Select]          │ │
│ │ Height: 40px                                             │ │
│ ├── spacing: 0px ──────────────────────────────────────────┤ │
│ │ ┌─────────────────────────────────┬──────────────────┐   │ │
│ │ │ FILE GRID / LIST                │ PREVIEW PANE     │   │ │
│ │ │                                 │ (toggle-able)    │   │ │
│ │ │ GRID VIEW:                      │                  │   │ │
│ │ │ 4-5 columns, 160px thumbnails   │ File preview:    │   │ │
│ │ │ File name below, type icon      │ Image/PDF/video  │   │ │
│ │ │ overlay on non-image files      │ preview           │   │ │
│ │ │                                 │                  │   │ │
│ │ │ LIST VIEW:                      │ File details:    │   │ │
│ │ │ Icon + Name + Size + Modified + │ Name, type, size │   │ │
│ │ │ Owner columns                   │ modified, owner  │   │ │
│ │ │ Sortable column headers         │ path, tags       │   │ │
│ │ │                                 │                  │   │ │
│ │ │ Folders first, then files       │ Actions:         │   │ │
│ │ │ Multi-select with Shift/Cmd     │ [Download]       │   │ │
│ │ │                                 │ [Share]          │   │ │
│ │ │ Drop zone: drag files to upload │ [Move]           │   │ │
│ │ │                                 │ [Delete]         │   │ │
│ │ │                                 │                  │   │ │
│ │ │                                 │ Width: 320px     │   │ │
│ │ └─────────────────────────────────┴──────────────────┘   │ │
│ │ STORAGE BAR (bottom)                                     │ │
│ │ [████████░░░░░░░░] 7.2 GB of 15 GB used                 │ │
│ │ Height: 32px, border-top                                 │ │
│ └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

### Responsive Adjustments

**Tablet:**
- Preview pane: hidden by default, shown on selection
- Grid: 3 columns
- List: fewer columns (hide owner, show on tap)

**Mobile:**
- Grid: 2 columns, larger touch targets
- List: simplified (icon + name + size)
- Preview pane: full-screen overlay on tap
- Breadcrumb: truncated with "..." for deep paths
- Upload: bottom sheet with camera/files/photos options
- Multi-select: long-press to enter selection mode
- Storage bar: accessible from settings, not always visible

### UX Notes
- Drag and drop for upload (desktop) with progress indicator
- Right-click context menu on files (desktop)
- Double-click folder to open, double-click file to preview/download
- Keyboard: arrow keys to navigate, Enter to open, Delete to trash
- Search should search file names AND content (if indexed)
- Starred/favorited files accessible from sidebar
- Recent files section at top (optional, collapsible)

---

## Cross-Cutting App Page Patterns

### Consistent Chrome

Every app page shares these chrome elements:
```
SIDEBAR NAV:     256px wide, collapsible to 64px
TOP BAR:         56-64px height, sticky
PAGE PADDING:    24px desktop, 16px mobile
PAGE BACKGROUND: gray-50 (content on white cards)
```

### Card System

All content containers within app pages follow the card pattern:
```
Background:      white
Border:          1px solid gray-200 (or shadow-sm)
Border-radius:   12px
Padding:         24px (20px on smaller cards)
Gap between:     16-24px
```

### Loading States

Every app page recipe should implement:
```
1. Skeleton loading (not spinners) for initial load
2. Inline loading for data refresh (keep stale content visible)
3. Optimistic updates for user actions
4. Error states with retry actions
5. Empty states with helpful CTAs
```

### Keyboard Navigation

All app pages should support:
```
Tab:           Move focus through interactive elements
Escape:        Close modals, deselect, cancel
Cmd+K:         Global search / command palette
Cmd+S:         Save (where applicable)
Cmd+Z:         Undo (where applicable)
Arrow keys:    Navigate lists, grids, calendar
```

### Transition Between Pages

Navigation between app pages should feel instant:
```
Route change:       Instant content swap (no full page reload)
Loading state:       Skeleton of destination page, not blank
Back navigation:     Restore scroll position
Page title:          Update document title for browser tab
URL:                 Reflect current state (deep-linkable)
```
