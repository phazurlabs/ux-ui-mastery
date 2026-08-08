---
name: navigation-pattern-encyclopedia
description: "Every navigation pattern with specs, trade-offs, and production code: top bars, sidebars, bottom tabs, mega menus, breadcrumbs, command palettes, and contextual and mobile navigation. Use when choosing a nav model, fixing discoverability, or structuring information architecture."
---

# Navigation Pattern Encyclopedia — Every Nav Pattern

---

## Part 1: Navigation Philosophy

### The Three Questions Every Navigation Must Answer
1. **Where am I?** — current location clearly indicated (active state, breadcrumb, page title)
2. **Where can I go?** — available destinations visible or discoverable
3. **How do I get there?** — interaction path obvious (click, tap, keyboard shortcut)

### Wayfinding Principles
Wayfinding in digital products mirrors physical navigation. Users build mental models of information spaces the same way they learn building layouts.

- **Landmarks** — persistent visual anchors (logo, primary nav bar, footer) that orient users
- **Paths** — clear routes between destinations (links, buttons, breadcrumbs)
- **Regions** — visually distinct zones that group related content (sidebar, main content, utility bar)
- **Edges** — boundaries between sections (dividers, background shifts, elevation changes)
- **Signs** — labels and icons that communicate destination or action

### Information Scent (Pirolli & Card, 1999)
Users follow "information scent" — the perceived likelihood that a navigation path leads to desired content. Strong scent = clear labels, recognizable icons, descriptive link text. Weak scent = vague labels ("Resources"), icon-only navigation without tooltips, buried content.

**Scent Strength Checklist:**
- Label uses the user's vocabulary (not internal jargon)
- Icon is universally recognizable or paired with text
- Hover/focus state previews destination content
- Active state confirms the user's current location
- Breadcrumb trail shows path taken

### Progressive Disclosure in Navigation
Reveal complexity gradually. Show primary navigation always; reveal secondary navigation on interaction; surface contextual navigation in-context.

**Hierarchy of Disclosure:**
1. Always visible: 3-7 primary destinations
2. Revealed on hover/click: sub-sections, mega menu panels
3. On-demand: command palette, search, contextual menus
4. Deep: settings, admin tools, rarely used features

### Fitts's Law Applied to Navigation
- Larger targets = faster to reach. Minimum touch target: 44x44pt (iOS), 48x48dp (Android)
- Edge/corner targets are effectively infinite size (pin nav to screen edges)
- Distance matters: place frequent actions close to resting cursor/thumb position
- Bottom navigation on mobile exploits the thumb zone (easy reach)

### Hick's Law Applied to Navigation
- More choices = longer decision time. Keep primary nav to 5-7 items
- Group items into categories to reduce cognitive load
- Use progressive disclosure to stage choices

---

## Part 2: Navigation Levels

### Level 1 — Global Navigation
Persistent across all pages/screens. Contains top-level destinations.
- **Location:** top bar, sidebar, or bottom tab bar
- **Item count:** 5-8 maximum
- **Must include:** logo/home link, primary destinations, utility actions (search, account)

### Level 2 — Local Navigation
Within a section or feature area. Shows sub-sections of the current context.
- **Location:** sub-nav bar, sidebar sub-menu, horizontal tabs
- **Item count:** 3-8 items
- **Relationship:** child of currently active global nav item

### Level 3 — Contextual Navigation
Embedded within content. Provides related links, in-page anchors, and inline actions.
- **Location:** within the content area — breadcrumbs, inline links, related items, TOC
- **Item count:** varies by content
- **Purpose:** cross-linking, deeper exploration, supplementary paths

### Level 4 — Utility Navigation
Account management, settings, help, notifications. Always secondary to content navigation.
- **Location:** top-right corner (web), profile menu, settings gear
- **Item count:** 3-6 items
- **Convention:** universally placed top-right on web; profile tab or settings in mobile

---

## Part 3: Primary Navigation Patterns

### TOP-01: Horizontal Top Navigation Bar

**When to Use:** Marketing sites, content sites, e-commerce, SaaS landing pages. Best when there are 3-7 top-level destinations.

**When to Avoid:** Complex apps with 10+ sections, deeply nested IA, mobile-first apps.

**Anatomy (ASCII):**
```
+------------------------------------------------------------------+
| [Logo]   Home   Products   Pricing   Docs   Blog   |  [Search] [Avatar] |
+------------------------------------------------------------------+
```

**Sizing Specs:**
- Height: 56-64px (web), 44px (iOS compact), 56px (Android)
- Logo area: 120-200px width
- Nav item padding: 12-16px horizontal, full height clickable area
- Font size: 14-16px, medium weight (500-600)
- Active indicator: 2-3px bottom border or background highlight
- Z-index: 1000+ (always above content)

**States:**
- Default: text color at 70-80% opacity
- Hover: text color at 100%, subtle background (4-8% opacity)
- Active/Current: full opacity, bottom border accent, `aria-current="page"`
- Focus: visible focus ring (2px outline, 2px offset)

**Responsive Behavior:**
- Desktop (1024px+): full horizontal layout
- Tablet (768-1023px): collapse least-important items into overflow "More" menu
- Mobile (<768px): collapse to hamburger menu or switch to bottom tab bar

**Accessibility:**
- Wrap in `<nav aria-label="Main navigation">`
- Use `<ul>/<li>` semantic list structure
- `aria-current="page"` on active item
- All items keyboard-reachable via Tab
- Skip navigation link before nav

**React + CSS Implementation:**
```tsx
function TopNav({ items, currentPath }) {
  return (
    <nav aria-label="Main navigation" className="top-nav">
      <a href="/" className="top-nav__logo" aria-label="Home">
        <Logo />
      </a>
      <ul className="top-nav__list" role="list">
        {items.map(item => (
          <li key={item.href}>
            <a
              href={item.href}
              className="top-nav__link"
              aria-current={item.href === currentPath ? 'page' : undefined}
            >
              {item.label}
            </a>
          </li>
        ))}
      </ul>
      <div className="top-nav__utility">
        <SearchButton />
        <UserMenu />
      </div>
    </nav>
  );
}
```

```css
.top-nav {
  display: flex;
  align-items: center;
  height: 64px;
  padding: 0 24px;
  background: var(--surface-primary);
  border-bottom: 1px solid var(--border-subtle);
  position: sticky;
  top: 0;
  z-index: 1000;
}
.top-nav__list {
  display: flex;
  gap: 4px;
  list-style: none;
  margin: 0;
  padding: 0;
}
.top-nav__link {
  display: flex;
  align-items: center;
  padding: 8px 16px;
  height: 40px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-secondary);
  text-decoration: none;
  transition: background 150ms, color 150ms;
}
.top-nav__link:hover {
  background: var(--surface-hover);
  color: var(--text-primary);
}
.top-nav__link[aria-current='page'] {
  color: var(--text-primary);
  background: var(--surface-active);
  font-weight: 600;
}
```

---

### TOP-02: Mega Menu

**When to Use:** E-commerce with many categories, enterprise sites with deep IA, sites with 20+ destinations to expose.

**When to Avoid:** Simple sites, mobile (use hierarchical drill-down instead), apps with flat IA.

**Anatomy (ASCII):**
```
+------------------------------------------------------------------+
| [Logo]   Shop v   Solutions v   Resources v   Pricing            |
+==================================================================+
| Category 1       | Category 2       | Category 3    | [Promo]   |
|  - Sub-item      |  - Sub-item      |  - Sub-item   | [Image]   |
|  - Sub-item      |  - Sub-item      |  - Sub-item   | [CTA]     |
|  - Sub-item      |  - Sub-item      |  - Sub-item   |           |
|  - View All ->   |  - View All ->   |  - View All   |           |
+------------------------------------------------------------------+
```

**Sizing Specs:**
- Full viewport width or constrained to max-width (1200-1440px)
- Column width: 200-280px each
- 3-5 columns of links + 1 optional promo/featured column
- Padding: 32-48px vertical, 24-32px horizontal
- Category heading: 13-14px, uppercase, bold, muted color
- Sub-item links: 14-15px, regular weight
- Vertical gap between items: 8-12px

**Interaction:**
- Opens on hover (desktop) with 200-300ms delay to prevent accidental triggers
- Opens on click/tap (mobile/tablet)
- Closes on mouse leave (with 300ms grace period) or Escape key
- Diagonal movement tolerance: use "aim triangle" pattern (Amazon-style) to prevent premature close when moving cursor diagonally to submenu

**Accessibility:**
- `aria-expanded="true/false"` on trigger button
- `aria-haspopup="true"` on trigger
- Panel has `role="region"` or `role="menu"` with `aria-labelledby` pointing to trigger
- Escape closes and returns focus to trigger
- Arrow keys navigate between items within the panel

---

### SIDE-01: Sidebar Navigation (Always Visible)

**When to Use:** SaaS dashboards, admin panels, tools with 8-20+ sections, apps where users frequently switch between sections.

**When to Avoid:** Content-heavy sites (sidebar steals reading width), marketing sites, mobile-primary apps.

**Anatomy (ASCII):**
```
+--------+--------------------------------------------+
| [Logo] |                                            |
|--------|            Main Content Area               |
| * Home |                                            |
|   Inbox|                                            |
|   Tasks|--------------------------------------------+
|   Proj |                                            |
|--------|                                            |
| TEAM   |                                            |
|   Memb |                                            |
|   Sett |                                            |
|--------|                                            |
| [Ava]  |                                            |
| [Coll] |                                            |
+--------+--------------------------------------------+
```

**Sizing Specs:**
- Expanded width: 240-280px (standard), up to 320px (complex apps)
- Collapsed/rail width: 56-72px (icons only)
- Mini rail: 48px (icon only, no labels)
- Nav item height: 36-44px
- Icon size: 20-24px
- Text: 14px, medium weight
- Section heading: 11-12px, uppercase, muted, extra-bold
- Vertical padding between items: 2-4px
- Section gap: 16-24px
- Background: slightly darker or lighter than content area (3-5% contrast shift)

**Collapsed Sidebar (Rail):**
```
+----+--------------------------------------------+
| Ic |                                            |
|----|            Main Content Area               |
| Ic |                                            |
| Ic |                                            |
| Ic |                                            |
| Ic |                                            |
|----|                                            |
| Ic |                                            |
| Ic |                                            |
|----|                                            |
| Av |                                            |
| << |                                            |
+----+--------------------------------------------+
```
- Tooltip on hover showing label (200ms delay)
- Toggle button at bottom or top to expand/collapse
- Persist collapsed state in localStorage
- Transition: width 200ms ease-out

**Nested Sidebar (Multi-Level):**
- Indent sub-items 16-24px from parent
- Expand/collapse icon (chevron) on parent items
- `aria-expanded="true/false"` on expandable items
- Maximum nesting depth: 3 levels (deeper = use breadcrumbs or separate view)

**Accessibility:**
- `<nav aria-label="Sidebar navigation">`
- `aria-current="page"` on active item
- Arrow Up/Down to move between items
- Enter/Space to activate
- Arrow Right to expand, Arrow Left to collapse sub-menus
- Home/End to jump to first/last item

**React Implementation:**
```tsx
function Sidebar({ items, currentPath, collapsed, onToggle }) {
  return (
    <nav
      aria-label="Sidebar navigation"
      className={`sidebar ${collapsed ? 'sidebar--collapsed' : ''}`}
      style={{ width: collapsed ? 64 : 256 }}
    >
      <div className="sidebar__header">
        <Logo collapsed={collapsed} />
      </div>
      <ul className="sidebar__list" role="list">
        {items.map(section => (
          <li key={section.label} className="sidebar__section">
            {!collapsed && (
              <span className="sidebar__section-label">{section.label}</span>
            )}
            <ul role="list">
              {section.items.map(item => (
                <li key={item.href}>
                  <a
                    href={item.href}
                    className="sidebar__item"
                    aria-current={item.href === currentPath ? 'page' : undefined}
                    title={collapsed ? item.label : undefined}
                  >
                    <item.icon className="sidebar__icon" />
                    {!collapsed && <span>{item.label}</span>}
                    {!collapsed && item.badge && (
                      <span className="sidebar__badge">{item.badge}</span>
                    )}
                  </a>
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
      <button
        className="sidebar__toggle"
        onClick={onToggle}
        aria-label={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}
      >
        {collapsed ? <ChevronRight /> : <ChevronLeft />}
      </button>
    </nav>
  );
}
```

```css
.sidebar {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: var(--surface-sidebar);
  border-right: 1px solid var(--border-subtle);
  transition: width 200ms ease-out;
  overflow-y: auto;
  overflow-x: hidden;
  position: fixed;
  left: 0;
  top: 0;
}
.sidebar__section-label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  padding: 24px 16px 8px;
}
.sidebar__item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 16px;
  height: 40px;
  border-radius: 8px;
  margin: 0 8px;
  font-size: 14px;
  color: var(--text-secondary);
  text-decoration: none;
  transition: background 120ms;
}
.sidebar__item:hover { background: var(--surface-hover); }
.sidebar__item[aria-current='page'] {
  background: var(--surface-active);
  color: var(--text-primary);
  font-weight: 600;
}
.sidebar--collapsed .sidebar__item {
  justify-content: center;
  padding: 8px;
}
```

---

### MOB-01: Bottom Tab Bar

**When to Use:** Mobile apps with 2-5 primary destinations. The dominant mobile navigation pattern for iOS and Android.

**When to Avoid:** More than 5 items (use "More" tab or different pattern), desktop apps, web content sites.

**Anatomy (ASCII):**
```
+------------------------------------------------------------------+
|                                                                    |
|                      Main Content                                  |
|                                                                    |
+------------------------------------------------------------------+
| [ic]      [ic]      [ic]      [ic]      [ic]                     |
| Home     Search    Create    Inbox    Profile                     |
+------------------------------------------------------------------+
```

**Platform Specs:**

| Property | iOS (HIG) | Android (M3) |
|---|---|---|
| Height | 49pt (compact) / 83pt (with safe area) | 80dp |
| Icon size | 24-28pt | 24dp |
| Label font | 10pt SF Pro | 12sp Roboto |
| Active color | System blue / app tint | Primary color |
| Inactive color | Gray (secondary label) | On-surface-variant |
| Max items | 5 | 5 |
| Min items | 2 | 3 |
| Touch target | 44x44pt minimum | 48x48dp minimum |
| Badge position | Top-right of icon | Top-right of icon |
| Safe area | Extends behind home indicator | Extends behind gesture bar |

**iOS 26 Liquid Glass Tab Bar:**
- Translucent material background with vibrancy
- Active item uses filled icon variant
- Inactive items use outline icon variant
- No explicit divider line — relies on material blur
- Tab bar hides on scroll in certain contexts (scrollEdgeAppearance)

**Android Material 3 Navigation Bar:**
- Active item gets indicator pill (64x32dp, primary-container color)
- Active icon is filled, inactive is outlined
- 12dp vertical padding above icons
- Label always visible (M3 recommendation; unlike M2 which hid inactive labels)

**Overflow (More Than 5):**
- 5th tab becomes "More" with ellipsis icon
- "More" opens a list view of additional destinations
- Allow users to customize/reorder tabs (long-press to rearrange)
- Alternative: use 4 tabs + FAB for primary action

**Accessibility:**
- `role="tablist"` on container (or `role="navigation"` — both valid approaches)
- Each tab: `role="tab"` with `aria-selected="true/false"`
- Labels required — never icon-only without `aria-label`
- Badge: `aria-label="Inbox, 3 new messages"` (announce count)
- Minimum contrast: 3:1 for inactive icons against background

---

### CMD-01: Command Palette (Cmd+K / Ctrl+K)

**When to Use:** Power user tools, developer tools, complex apps with many features, as supplementary navigation alongside primary nav.

**When to Avoid:** As the sole navigation method, for non-technical audiences without other nav options.

**Anatomy (ASCII):**
```
+-----------------------------------------------+
| [>] Type a command or search...           [Esc]|
|-----------------------------------------------|
|  Recently Used                                 |
|    > Go to Dashboard                     Cmd+D |
|    > Create New Project                  Cmd+N |
|-----------------------------------------------|
|  Navigation                                    |
|    > Go to Settings                            |
|    > Go to Team Members                        |
|    > Go to Billing                             |
|-----------------------------------------------|
|  Actions                                       |
|    > Toggle Dark Mode                          |
|    > Export Data as CSV                        |
|    > Invite Team Member                        |
+-----------------------------------------------+
```

**Sizing Specs:**
- Width: 560-640px (centered), max 90vw on mobile
- Max height: 400-480px with scroll
- Top offset: 20-25% from top of viewport
- Input height: 48-56px
- Result item height: 40-44px
- Border radius: 12-16px
- Shadow: large elevation (0 24px 48px rgba(0,0,0,0.2))
- Overlay backdrop: rgba(0,0,0,0.5) with backdrop-filter blur(4px)
- Animation: scale(0.95) + opacity 0 -> scale(1) + opacity 1, 150ms ease-out

**Behavior:**
- Trigger: Cmd+K (Mac), Ctrl+K (Windows/Linux)
- Focus immediately in search input on open
- Fuzzy search across all commands, pages, and actions
- Categorize results (Navigation, Actions, Recent, Settings)
- Show keyboard shortcuts alongside results
- Arrow Up/Down to navigate results
- Enter to execute selected result
- Escape to close (return focus to previous element)
- Typing filters results in real-time (<50ms perceived latency)

**Accessibility:**
- `role="combobox"` on input
- `role="listbox"` on results list
- `role="option"` on each result
- `aria-activedescendant` tracks highlighted result
- `aria-expanded="true"` when open
- Announce result count to screen readers: "5 results"

**React Implementation:**
```tsx
function CommandPalette({ commands, onSelect, onClose }) {
  const [query, setQuery] = useState('');
  const [activeIndex, setActiveIndex] = useState(0);
  const filtered = useMemo(() => fuzzySearch(commands, query), [commands, query]);

  useEffect(() => {
    const handler = (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        // toggle open
      }
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, []);

  return (
    <div className="cmd-palette-overlay" onClick={onClose}>
      <div className="cmd-palette" role="dialog" aria-label="Command palette"
           onClick={e => e.stopPropagation()}>
        <input
          type="text"
          role="combobox"
          aria-expanded="true"
          aria-controls="cmd-results"
          aria-activedescendant={`cmd-item-${activeIndex}`}
          placeholder="Type a command or search..."
          value={query}
          onChange={e => { setQuery(e.target.value); setActiveIndex(0); }}
          onKeyDown={e => {
            if (e.key === 'ArrowDown') setActiveIndex(i => Math.min(i + 1, filtered.length - 1));
            if (e.key === 'ArrowUp') setActiveIndex(i => Math.max(i - 1, 0));
            if (e.key === 'Enter') onSelect(filtered[activeIndex]);
            if (e.key === 'Escape') onClose();
          }}
          autoFocus
        />
        <ul id="cmd-results" role="listbox">
          {filtered.map((cmd, i) => (
            <li key={cmd.id} id={`cmd-item-${i}`} role="option"
                aria-selected={i === activeIndex}
                className={i === activeIndex ? 'active' : ''}
                onClick={() => onSelect(cmd)}>
              <cmd.icon />
              <span>{cmd.label}</span>
              {cmd.shortcut && <kbd>{cmd.shortcut}</kbd>}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
```

---

### MOB-02: Hamburger Menu

**When to Use:** As a last resort when other patterns do not fit, for secondary navigation on mobile, for sites with many top-level pages that cannot be reduced.

**When to Avoid:** When you can use bottom tabs or visible navigation instead. Hamburger menus reduce discoverability by 50%+ (NNG research). Never use as sole navigation for key features.

**Anatomy (ASCII):**
```
+----------------------------------+
| [=]  Page Title          [Search]|    <- Header with hamburger icon
+----------------------------------+

Slide-over variant (opens from left):
+-------------------+
| [X] Navigation    |+--------------+
|                   ||              |
| * Home            ||   Dimmed     |
|   Products        ||   Content    |
|   About           ||   Behind     |
|   Contact         ||              |
|                   ||              |
| ----              ||              |
| Settings          ||              |
| Help              ||              |
+-------------------++--------------+

Full-overlay variant:
+----------------------------------+
| [X]                       [Logo] |
|                                  |
|         Home                     |
|         Products                 |
|         About                    |
|         Contact                  |
|                                  |
|         Settings                 |
|         Help                     |
+----------------------------------+
```

**Specs:**
- Hamburger icon: 24x24px, three horizontal lines (2px thick, 18px wide, 6px gap)
- Slide-over panel width: 280-320px or 80% of viewport
- Full overlay: 100% viewport
- Animation: slide-in 250ms ease-out (slide-over), fade 200ms (overlay)
- Backdrop: rgba(0,0,0,0.5)
- Close mechanisms: X button, tap backdrop, swipe left, Escape key

**Accessibility:**
- Toggle button: `aria-expanded="true/false"`, `aria-controls="nav-panel"`
- Panel: `role="dialog"` or `role="navigation"`, `aria-label="Main menu"`
- Focus trap when open (Tab cycles within panel)
- Return focus to hamburger button on close
- Escape key closes menu

---

## Part 4: Secondary Navigation Patterns

### SEC-01: Breadcrumbs

**When to Use:** Sites with 3+ levels of hierarchy (e-commerce, documentation, file systems).

**When to Avoid:** Flat sites with 1-2 levels, mobile apps (use back button instead), single-page apps with no hierarchy.

**Anatomy:**
```
Home  >  Products  >  Electronics  >  Headphones
[link]   [link]       [link]          [current, not a link]
```

**Specs:**
- Font size: 13-14px
- Separator: ">" or "/" or chevron icon (8-12px)
- Gap between items: 4-8px
- Current page: not a link, text color at 100% opacity
- Ancestor links: text color at 60-70% opacity
- Truncation: on mobile, show "... > Parent > Current" (collapse middle levels)

**Accessibility:**
- `<nav aria-label="Breadcrumb">`
- `<ol>` ordered list
- Current page: `aria-current="page"`
- Separators: CSS-generated (not in DOM) or `aria-hidden="true"`

---

### SEC-02: Horizontal Tabs

**When to Use:** 2-6 parallel content views within the same page context (profile tabs, settings sections, data views).

**When to Avoid:** More than 6 tabs (use scrollable tabs or different pattern), for sequential steps (use stepper instead).

**Anatomy:**
```
+-------------------------------------------------------------------+
| [ Overview ]  [ Activity ]  [ Settings ]  [ Members ]             |
|====================================================================
|                                                                    |
|                    Tab Panel Content                               |
|                                                                    |
+-------------------------------------------------------------------+
```

**Specs:**
- Tab height: 40-48px
- Tab padding: 12-20px horizontal
- Active indicator: 2-3px bottom border (accent color)
- Font: 14px, medium weight; active = bold or semibold
- Gap between tabs: 0-4px
- Scrollable variant: add horizontal scroll with fade indicators at edges

**Accessibility:**
- `role="tablist"` on container
- `role="tab"` on each tab, `aria-selected="true/false"`
- `role="tabpanel"` on content, `aria-labelledby` pointing to tab
- Arrow Left/Right to move between tabs
- Home/End to jump to first/last tab
- Tab key moves focus from tab to panel content

---

### SEC-03: Segmented Control

**When to Use:** 2-5 mutually exclusive options that filter or switch a view (list/grid, day/week/month, map/satellite).

**When to Avoid:** More than 5 options, actions (use buttons), navigation between separate pages.

**Anatomy:**
```
+------------------------------------------+
| [ List ][= Grid =][ Map ]               |
+------------------------------------------+
```

**Specs:**
- Height: 32-40px
- Segment min-width: 80px
- Border-radius: 8-10px (container), 6-8px (active pill)
- Active segment: filled background (primary or surface)
- Background: subtle fill (gray-100 or surface-secondary)
- Animation: slide active indicator 200ms ease-out
- iOS: UISegmentedControl — 32pt height, system blue tint
- Android: M3 SegmentedButton — 40dp height, secondary-container fill

---

### SEC-04: Pagination

**When to Use:** Long lists of results (search results, product listings, data tables). When the total count matters to the user.

**When to Avoid:** Social feeds (use infinite scroll), short lists under 20 items, real-time data.

**Anatomy:**
```
[< Prev]  1  2  [3]  4  5  ...  42  [Next >]
```

**Specs:**
- Button size: 36-40px square
- Font: 14px
- Active page: filled background (accent color), white text
- Hover: subtle background
- Disabled state: 40% opacity, no pointer
- Gap: 4-8px between items
- Truncation: show first page, last page, 2 pages around current, ellipsis for gaps
- Show "Showing 21-40 of 420 results" text

---

### SEC-05: Stepper / Progress Navigation

**When to Use:** Multi-step processes (checkout, onboarding, form wizards). When the user needs to know progress and remaining steps.

**Anatomy:**
```
(1)-----(2)-----(3)-----(4)
Done    Active  To do   To do
Account Profile Payment Review
```

**Specs:**
- Step circle: 32-40px diameter
- Completed: filled accent + checkmark icon
- Active: filled accent + step number
- Upcoming: outlined border + step number, muted color
- Connector line: 2px, accent for completed, muted for upcoming
- Label: 12-14px below circle
- Horizontal layout on desktop, vertical on mobile

---

## Part 5: Contextual Navigation

### CTX-01: Context Menu (Right-Click)

**When to Use:** Desktop apps and web apps where items have multiple actions (file managers, design tools, code editors, data tables).

**Specs:**
- Width: 200-280px
- Item height: 32-36px
- Padding: 4px vertical (container)
- Separator: 1px line with 8px vertical margin
- Border-radius: 8px
- Shadow: medium elevation
- Sub-menu: opens to the right (or left if constrained), indicated by chevron icon
- Keyboard: Arrow Up/Down to navigate, Enter to select, Right to open sub-menu, Left to close sub-menu, Escape to dismiss

### CTX-02: Action Sheet (Mobile)

**When to Use:** Mobile — presenting a set of actions related to the current context (sharing, editing, deleting).

**iOS Specs:**
- Slides up from bottom
- Rounded corners: 14pt
- Cancel button: separate card below
- Destructive action: red text
- Max visible actions before scroll: 6-8

**Android Specs (Bottom Sheet):**
- Rounded top corners: 28dp
- Drag handle: 32x4dp, centered, gray
- Can be half-screen or full-screen modal

### CTX-03: Popover

**When to Use:** Revealing additional options or information without leaving context (filter options, color picker, date picker).

**Specs:**
- Width: 200-400px
- Arrow/caret pointing to trigger element
- Border-radius: 12px
- Shadow: medium elevation
- Dismiss: click outside, Escape, or explicit close button
- Position: automatically flip if near viewport edge (top/bottom/left/right)

### CTX-04: Tooltip Navigation

**When to Use:** Providing supplementary navigation hints on icon-only interfaces, collapsed sidebars, or toolbar icons.

**Specs:**
- Appear on hover (500-800ms delay) and focus
- Position: above, below, left, or right of trigger
- Max width: 200-300px
- Font: 12-13px
- Background: dark (inverted) or surface with border
- Duration: persist while hovering, dismiss 200ms after mouse leave
- `role="tooltip"`, linked via `aria-describedby`

---

## Part 6: Search Navigation

### Search Bar Placement

**Option A — Header Search (most common):**
```
+------------------------------------------------------------------+
| [Logo]   Nav Items...                    [Search Icon] [Avatar]   |
+------------------------------------------------------------------+
```
- Search icon that expands to input on click
- Width when expanded: 300-480px

**Option B — Prominent Search (search-driven apps):**
```
+------------------------------------------------------------------+
| [Logo]   [     Search products, articles, help...      ] [Avatar]|
+------------------------------------------------------------------+
```
- Persistent search input in header
- Width: 400-600px, centered or left-aligned

**Option C — Hero Search (search-primary sites):**
```
+------------------------------------------------------------------+
|                                                                    |
|                    What are you looking for?                       |
|              [                                          ] [Go]    |
|              Popular: shoes, electronics, deals                   |
|                                                                    |
+------------------------------------------------------------------+
```

### Autocomplete / Search Suggestions

**Specs:**
- Dropdown appears after 1-2 characters typed
- Debounce: 150-300ms
- Max suggestions: 6-10
- Categories: Recent searches, suggested terms, matching products/pages
- Highlight matching text in bold
- Keyboard: Arrow Up/Down to navigate, Enter to select, Escape to close
- `role="combobox"` + `role="listbox"` + `role="option"`

### Faceted Search / Filters

**Anatomy:**
```
+----------+-----------------------------------------------+
| Filters  |  Results (142)                   [Sort: v]    |
|          |                                               |
| Category |  [Result 1]                                   |
| [x] Elec |  [Result 2]                                   |
| [ ] Cloth|  [Result 3]                                   |
|          |  [Result 4]                                   |
| Price    |                                               |
| [--o--]  |  [ 1 ] [ 2 ] [ 3 ] ... [15] [Next>]         |
|          |                                               |
| Rating   |                                               |
| 4+ stars |                                               |
+----------+-----------------------------------------------+
```

**Specs:**
- Filter panel width: 240-280px (desktop sidebar)
- Mobile: filter button opens bottom sheet or full-screen overlay
- Active filters shown as removable chips/tags above results
- Show result count that updates dynamically
- "Clear all filters" action when filters are active

---

## Part 7: Information Architecture

### Card Sorting
- **Open card sort:** users group items and name the groups (discovery phase)
- **Closed card sort:** users place items into predefined groups (validation phase)
- **Hybrid:** some predefined groups, users can create new ones
- Sample size: 15-30 participants for reliable results
- Tools: Optimal Workshop, UserZoom, Maze

### Tree Testing
- Test your IA hierarchy without visual design influence
- Give users tasks: "Find the return policy"
- Measure: success rate, directness (first click correct), time to complete
- Sample size: 50+ participants for statistical significance

### IA Structures

**Hierarchical (Tree):** Most common. Parent-child relationships. Good for large sites.
```
        Home
       / | \
    Products  About  Support
    /  |  \
  Cat1 Cat2 Cat3
```

**Sequential (Linear):** Steps in order. Good for wizards, onboarding, checkout.
```
Step 1 -> Step 2 -> Step 3 -> Step 4 -> Done
```

**Matrix (Cross-Reference):** Multiple ways to reach the same content. Good for e-commerce (by category, by brand, by price).
```
By Category: Electronics > Headphones > Sony WH-1000XM5
By Brand:    Sony > Headphones > Sony WH-1000XM5
By Feature:  Noise Cancelling > Sony WH-1000XM5
```

**Hub-and-Spoke:** Central hub with spokes to features. Good for mobile apps (home screen to features, always return home).
```
       Feature A
          |
Feature D-HOME-Feature B
          |
       Feature C
```

### User Flow Mapping
- Map entry points, decision points, and exit points
- Identify dead ends (pages with no next action)
- Ensure every page answers "what should I do next?"
- Maximum clicks to any content: 3 (three-click rule is a myth, but depth should feel shallow)

---

## Part 8: Navigation by App Type

### SaaS Dashboard
- **Primary:** Sidebar (collapsible, 240px expanded, 64px collapsed)
- **Secondary:** Horizontal tabs within each section
- **Utility:** Top-right — search, notifications, user menu
- **Supplementary:** Command palette (Cmd+K)
- **Example:** Notion, Linear, Figma admin

### E-Commerce
- **Primary:** Top nav with mega menu for categories
- **Secondary:** Breadcrumbs, faceted search sidebar
- **Utility:** Cart icon (with count badge), account, wishlist
- **Mobile:** Bottom tab bar (Home, Categories, Search, Cart, Account)
- **Example:** Amazon, Shopify stores

### Content / Publishing Site
- **Primary:** Horizontal top nav (3-6 sections)
- **Secondary:** Breadcrumbs, in-article TOC, related articles
- **Utility:** Search (prominent), newsletter, social sharing
- **Mobile:** Hamburger for nav, sticky header with search
- **Example:** Medium, NYT, documentation sites

### Social / Community App
- **Primary:** Bottom tab bar (Feed, Search/Discover, Create, Notifications, Profile)
- **Secondary:** Horizontal scrollable tabs within feed (For You, Following, Trending)
- **Utility:** Direct messages icon in header
- **Mobile-first:** Bottom tabs are primary, top bar is contextual
- **Example:** Instagram, Twitter/X, TikTok

### Admin Panel / Back-Office
- **Primary:** Sidebar (always visible, with sections)
- **Secondary:** Breadcrumbs + horizontal tabs within entity views
- **Utility:** Global search, notification bell, user menu
- **Special:** Bulk action bars that appear on selection
- **Example:** Shopify admin, WordPress admin, Django admin

### Mobile-First Utility App
- **Primary:** Bottom tab bar (3-5 tabs)
- **Secondary:** Stack navigation (push/pop screens)
- **Utility:** Settings accessible from profile/more tab
- **Pattern:** Hub-and-spoke IA with bottom tabs as hubs
- **Example:** Banking apps, weather apps, fitness apps

---

## Part 9: Responsive Navigation Transformations

### Breakpoint Strategy
| Breakpoint | Width | Navigation Approach |
|---|---|---|
| Mobile | 0-767px | Bottom tabs or hamburger, stack navigation |
| Tablet | 768-1023px | Collapsed sidebar (rail) or top nav with overflow |
| Desktop | 1024-1439px | Full sidebar or top nav with dropdowns |
| Wide | 1440px+ | Full sidebar + secondary sidebar, or top nav + mega menu |

### Top Nav Transformation
```
Desktop:  [Logo]  Home  Products  Pricing  Docs  Blog  [Search] [User]
Tablet:   [Logo]  Home  Products  Pricing  [More v]    [Search] [User]
Mobile:   [=]  [Logo]                                   [Search]
```
- Items collapse into "More" dropdown from right to left based on priority
- On mobile, entire nav collapses into hamburger
- Priority+ pattern: mark items with priority levels, hide lowest first

### Sidebar Transformation
```
Desktop (1200px+):   [240px sidebar + content]
Tablet (768-1199px): [64px rail + content]
Mobile (<768px):     [full-width content] + [hamburger opens overlay sidebar]
```

### Bottom Tab Transformation
```
Mobile:   [Tab1] [Tab2] [Tab3] [Tab4] [Tab5]  (bottom bar)
Tablet:   [Sidebar rail with same items]
Desktop:  [Full sidebar with labels]
```

---

## Part 10: Navigation Accessibility

### Skip Links
First focusable element on the page. Invisible until focused.
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```
```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 8px;
  z-index: 10000;
  padding: 8px 16px;
  background: var(--surface-primary);
  color: var(--text-primary);
  border-radius: 4px;
  font-size: 14px;
}
.skip-link:focus {
  top: 8px;
}
```

### ARIA Landmarks
```html
<header role="banner">         <!-- site header -->
<nav aria-label="Main">        <!-- primary nav -->
<nav aria-label="Breadcrumb">  <!-- breadcrumb nav -->
<main role="main" id="main-content"> <!-- main content -->
<aside role="complementary">   <!-- sidebar content -->
<footer role="contentinfo">    <!-- site footer -->
```
- Multiple `<nav>` elements must have distinct `aria-label` values
- Screen readers list landmarks for quick navigation

### Focus Management
- **Page navigation (SPA):** Move focus to page heading or main content on route change
- **Modal/dialog open:** Move focus to first interactive element inside
- **Modal/dialog close:** Return focus to trigger element
- **Dropdown open:** Move focus to first menu item
- **Delete item from list:** Move focus to next item (or previous if last)

### Keyboard Patterns by Component
| Component | Keys | Behavior |
|---|---|---|
| Menu bar | Left/Right | Move between top-level items |
| Menu bar | Down/Enter | Open submenu |
| Menu | Up/Down | Move between items |
| Menu | Escape | Close, return focus to trigger |
| Tabs | Left/Right | Switch tabs (activate or focus based on implementation) |
| Tabs | Home/End | First/last tab |
| Tree view | Up/Down | Move between visible nodes |
| Tree view | Right | Expand node / move to first child |
| Tree view | Left | Collapse node / move to parent |
| Accordion | Enter/Space | Toggle section |

### ARIA Roles Reference
| Pattern | Container Role | Item Role | Key ARIA Properties |
|---|---|---|---|
| Nav bar | `navigation` | — | `aria-label`, `aria-current` |
| Tab bar | `tablist` | `tab` | `aria-selected`, `aria-controls` |
| Menu | `menu` | `menuitem` | `aria-expanded`, `aria-haspopup` |
| Tree | `tree` | `treeitem` | `aria-expanded`, `aria-level` |
| Breadcrumb | `navigation` | — | `aria-current`, `aria-label="Breadcrumb"` |
| Command palette | `combobox` + `listbox` | `option` | `aria-activedescendant`, `aria-expanded` |

---

## Part 11: Navigation Anti-Patterns

### ANTI-01: Icon-Only Navigation Without Labels
**Problem:** Users cannot identify destinations. Recognition requires recall.
**Fix:** Always pair icons with text labels. If space-constrained, use tooltips on hover/focus and ensure `aria-label` is present.

### ANTI-02: Hamburger Menu as Primary Navigation
**Problem:** Hides all navigation behind a tap. NNG research shows 50%+ reduction in discoverability.
**Fix:** Use visible navigation (bottom tabs, sidebar, horizontal nav) for primary destinations. Reserve hamburger for secondary items.

### ANTI-03: Too Many Top-Level Items (8+)
**Problem:** Violates Hick's Law. Users take longer to decide and may miss important items.
**Fix:** Group items into 5-7 categories. Use mega menus for sub-items. Conduct card sorting to validate groupings.

### ANTI-04: Creative/Non-Standard Placement
**Problem:** Navigation in unexpected locations (center of page, right side, below content) breaks learned conventions.
**Fix:** Follow platform conventions. Left sidebar or top bar for web. Bottom tabs for mobile. Users should not have to learn your navigation.

### ANTI-05: No Active State Indicator
**Problem:** Users cannot answer "Where am I?" without a visible active/current state.
**Fix:** Always show clear active state — filled background, bottom border, bold text, or color change. Use `aria-current="page"`.

### ANTI-06: Disappearing Navigation on Scroll
**Problem:** Auto-hiding nav frustrates users who want to navigate mid-page.
**Fix:** If you hide nav on scroll-down, show it on any scroll-up. Better: keep nav persistent. If hiding, ensure there is another way to navigate (footer nav, breadcrumbs, back-to-top).

### ANTI-07: Deep Nesting Without Breadcrumbs
**Problem:** Users get lost in 4+ level hierarchies with no way to understand their location.
**Fix:** Add breadcrumbs at 3+ levels. Consider flattening IA if nesting exceeds 4 levels.

### ANTI-08: Inconsistent Navigation Across Pages
**Problem:** Navigation items change, reorder, or disappear on different pages. Destroys spatial memory.
**Fix:** Keep global navigation consistent on every page. Only local/contextual navigation should change.

### ANTI-09: Non-Descriptive Labels
**Problem:** Labels like "Solutions", "Resources", "Platform" have weak information scent.
**Fix:** Use specific, action-oriented labels: "Pricing", "Documentation", "API Reference", "Templates". Test labels with users.

### ANTI-10: Dropdown on Hover Without Click Support
**Problem:** Hover-only dropdowns are inaccessible on touch devices and frustrating with trackpads.
**Fix:** Support both hover (desktop) and click/tap to open. Ensure keyboard Enter/Space also opens the dropdown.

---

## Part 12: Platform-Specific Navigation

### iOS (Human Interface Guidelines)
- **Tab bar:** bottom, 49pt height, 2-5 tabs, SF Symbols for icons
- **Navigation bar:** top, 44pt height, back button (left), title (center), action (right)
- **Large title:** 34pt, scrolls to inline 17pt on scroll
- **iOS 26 Liquid Glass:** translucent tab bar with vibrancy, floating tab bar style
- **Back navigation:** system back gesture (swipe from left edge), always support it
- **Search:** UISearchController integrates into navigation bar, pulls down to reveal

### Android (Material 3)
- **Navigation bar (bottom):** 80dp height, 3-5 destinations, active indicator pill
- **Navigation rail (tablet):** 80dp width, vertical icon+label, 3-7 destinations
- **Navigation drawer:** 360dp width, full-height, modal or persistent
- **Top app bar:** 64dp height, collapsing variants (small, medium, large)
- **Back navigation:** system back gesture or top-left back arrow
- **Search:** SearchBar or SearchView, expanding from top app bar

### Web Conventions
- **Logo:** top-left, links to home
- **Primary nav:** horizontal top bar (marketing) or left sidebar (apps)
- **Utility nav:** top-right (search, notifications, account)
- **Footer nav:** comprehensive sitemap-style links
- **Breadcrumbs:** below header, above content
- **Sticky header:** fixes on scroll, optionally shrinks (64px -> 48px)

---

## Part 13: Navigation Decision Framework

### Choosing the Right Pattern

```
How many primary destinations?
|
+-- 2-5 items
|   +-- Mobile-first? --> Bottom Tab Bar (MOB-01)
|   +-- Desktop SaaS? --> Top Nav (TOP-01) or Sidebar (SIDE-01)
|   +-- Marketing site? --> Top Nav (TOP-01)
|
+-- 6-12 items
|   +-- Groupable into 3-5 categories? --> Top Nav + Mega Menu (TOP-02)
|   +-- Flat list? --> Sidebar (SIDE-01)
|   +-- Mobile? --> Bottom Tabs (4) + "More" tab
|
+-- 13+ items
    +-- Always Sidebar (SIDE-01) with sections
    +-- Add Command Palette (CMD-01) as supplement
    +-- Mobile: Hamburger with categorized list
```

### Navigation Audit Checklist
- [ ] All primary destinations reachable in 1 click/tap
- [ ] Active state visible on current page/section
- [ ] Keyboard navigable (Tab, Arrow keys, Enter, Escape)
- [ ] Screen reader announces navigation landmarks and current page
- [ ] Skip link present as first focusable element
- [ ] Mobile navigation does not rely solely on hamburger for primary features
- [ ] Labels use user vocabulary (validated via card sorting or user testing)
- [ ] Navigation is consistent across all pages
- [ ] Touch targets meet minimum size (44pt iOS, 48dp Android)
- [ ] Breadcrumbs present at 3+ levels of hierarchy
- [ ] Search accessible from any page
- [ ] Navigation adapts appropriately across breakpoints

---

## Cross-References
- **mobile-ux-design** — iOS and Android navigation deep dives
- **desktop-app-design** — Desktop navigation conventions
- **layout-block-intelligence** — Header/nav block patterns and layout integration
- **accessibility-inclusive-design** — Full WCAG navigation requirements
- **screen-flow-patterns** — User flow patterns that connect to navigation
- **component-patterns-code** — Production code for nav components
- **interaction-motion-design** — Navigation transition animations
- **responsive-block-patterns** — Responsive transformation specs
