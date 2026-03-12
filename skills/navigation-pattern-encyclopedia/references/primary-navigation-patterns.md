# Primary Navigation Patterns — Complete Reference

> 27 primary navigation patterns with exact specs, responsive behavior, accessibility requirements, production code, and decision criteria.

---

## Pattern Index

| # | Pattern | Best For | Max Items |
|---|---------|----------|-----------|
| 1 | Top Horizontal Nav Bar | Marketing sites, content sites, e-commerce | 5-7 |
| 2 | Top Nav with Mega Menu | Large e-commerce, enterprise portals | 5-8 categories |
| 3 | Top Nav with Centered Logo | Brand-focused sites, fashion, luxury | 4-6 |
| 4 | Top Nav with Search Bar | Search-heavy apps, e-commerce, docs | 5-7 + search |
| 5 | Top Nav with Utility Bar | Complex sites needing dual-row nav | 5-7 + 3-6 utility |
| 6 | Sticky/Fixed Top Nav | Long-scroll pages, content sites | 5-7 |
| 7 | Transparent/Hero Top Nav | Landing pages, portfolio sites | 4-6 |
| 8 | Sidebar Navigation (Always Visible) | Admin panels, dashboards, SaaS tools | 8-15 |
| 9 | Collapsible Sidebar (Icon to Expanded) | Complex tools needing screen space | 8-15 |
| 10 | Left Sidebar with Nested Groups | Deep hierarchies, documentation sites | 5-8 groups |
| 11 | Right Sidebar Navigation | Property panels, inspector tools | 5-10 |
| 12 | Top Nav + Left Sidebar Combination | Enterprise apps, complex SaaS | 5-7 top + 8-15 side |
| 13 | Full-Screen Overlay Menu | Creative agencies, minimal sites | 5-10 |
| 14 | Tabbed Navigation (Horizontal) | Content with parallel sections | 3-7 |
| 15 | Vertical Tab Navigation | Settings pages, configuration panels | 5-12 |
| 16 | Hub-and-Spoke | Mobile apps, home screen patterns | 6-12 |
| 17 | Dashboard Navigation | Analytics, monitoring, admin | sidebar + widgets |
| 18 | Command Palette (Cmd+K) | Developer tools, power-user apps | unlimited (search) |
| 19 | Ribbon Navigation | Office-style productivity tools | 5-10 tabs |
| 20 | Tree View Navigation | File systems, nested data, docs | unlimited (virtual) |
| 21 | Card-Based Navigation | Content discovery, dashboards | 6-16 cards |
| 22 | Icon Grid Navigation | Mobile home screens, app launchers | 8-24 |
| 23 | Wizard/Stepper Primary Nav | Onboarding, multi-step workflows | 3-7 steps |
| 24 | Search-First Navigation | Large catalogs, knowledge bases | 0 visible + search |
| 25 | Split Navigation | Two distinct user goals (browse vs. create) | 3-4 left + 2-3 right |
| 26 | Dropdown Navigation Bar | Compact header, many sections | 5-8 dropdowns |
| 27 | Progressive Disclosure Nav | Complex tools, learning curves | 3-5 visible + more |

---

## 1. Top Horizontal Nav Bar

The most common navigation pattern on the web. A single horizontal bar at the top of the page containing the logo, primary navigation links, and utility actions (search, account, CTA).

### When to Use
- Marketing websites with 3-7 main sections
- Content-heavy websites (blogs, news, media)
- E-commerce with clear product categories
- SaaS marketing/landing pages

### When NOT to Use
- Applications with 8+ top-level sections (use sidebar instead)
- Deep hierarchical content (3+ levels deep)
- Mobile-first applications (use bottom tab bar)
- Complex admin interfaces

### Specs
| Property | Value |
|----------|-------|
| Height | 56-80px (desktop), 48-56px (mobile) |
| Max items | 5-7 visible links |
| Logo position | Left (LTR) or center |
| CTA position | Far right |
| Font size | 14-16px, medium weight (500-600) |
| Item spacing | 24-40px between items |
| Active indicator | Bottom border (2-3px), background highlight, or bold text |
| Background | Solid color, or transparent with blur on scroll |
| Z-index | 1000+ (above page content) |
| Position | `sticky` or `fixed` at top |

### Responsive Behavior
- **> 1024px**: All items visible horizontally
- **768-1024px**: Reduce spacing, possibly hide least important items
- **< 768px**: Collapse to hamburger menu (top-right) + logo (top-left)

### CSS Specs
```css
.top-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  padding: 0 24px;
  background: #ffffff;
  border-bottom: 1px solid #e5e7eb;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.top-nav__logo {
  flex-shrink: 0;
  height: 32px;
}

.top-nav__links {
  display: flex;
  align-items: center;
  gap: 32px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.top-nav__link {
  font-size: 15px;
  font-weight: 500;
  color: #374151;
  text-decoration: none;
  padding: 8px 0;
  border-bottom: 2px solid transparent;
  transition: color 150ms ease, border-color 150ms ease;
}

.top-nav__link:hover {
  color: #111827;
}

.top-nav__link[aria-current="page"] {
  color: #2563eb;
  border-bottom-color: #2563eb;
}

.top-nav__actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

@media (max-width: 768px) {
  .top-nav__links {
    display: none;
  }
  .top-nav__hamburger {
    display: block;
  }
}
```

### React Component
```tsx
interface TopNavProps {
  logo: React.ReactNode;
  links: { label: string; href: string }[];
  currentPath: string;
  actions?: React.ReactNode;
}

function TopNav({ logo, links, currentPath, actions }: TopNavProps) {
  return (
    <header className="top-nav">
      <a href="/" aria-label="Home">{logo}</a>
      <nav aria-label="Main">
        <ul className="top-nav__links">
          {links.map(link => (
            <li key={link.href}>
              <a
                href={link.href}
                className="top-nav__link"
                aria-current={currentPath === link.href ? 'page' : undefined}
              >
                {link.label}
              </a>
            </li>
          ))}
        </ul>
      </nav>
      {actions && <div className="top-nav__actions">{actions}</div>}
    </header>
  );
}
```

### Reference Implementations
- Stripe.com — Clean top nav with subtle active state
- Linear.app — Minimal top nav with strong CTA
- Apple.com — Compact top nav with search integration

---

## 2. Top Nav with Mega Menu

A top horizontal nav where hovering or clicking a category reveals a large, multi-column dropdown panel. Used when each top-level category contains many subcategories that benefit from spatial organization.

### When to Use
- Large e-commerce sites with extensive product categories
- Enterprise portals with many features organized by department
- University or government websites with deep content trees
- Any site where users need to see the full scope of a section before navigating

### When NOT to Use
- Sites with fewer than 5 subcategories per section (simple dropdown suffices)
- Mobile-primary audiences (mega menus do not translate to mobile)
- Applications where users navigate by search primarily
- Content that changes frequently (mega menu structure is typically hard-coded)

### Specs
| Property | Value |
|----------|-------|
| Trigger | Hover (desktop) with 150-300ms delay, Click (mobile) |
| Panel width | Full viewport width or max-width: 1200px centered |
| Columns | 2-5 columns depending on content |
| Column width | 200-280px each |
| Panel max-height | 70vh (with scroll if needed) |
| Open animation | Fade in + slight slide down, 200ms ease-out |
| Close delay | 300ms (prevent accidental close when moving to panel) |
| Backdrop | Optional semi-transparent overlay behind panel |
| Arrow/caret | Downward-pointing chevron next to trigger text |

### Responsive Behavior
- **> 1024px**: Full mega menu with columns
- **768-1024px**: Reduce columns, possibly stack to 2 columns
- **< 768px**: Convert to accordion within mobile menu (hamburger)

### CSS Specs
```css
.mega-menu-trigger {
  position: relative;
  cursor: pointer;
}

.mega-menu-panel {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: #ffffff;
  border-top: 1px solid #e5e7eb;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  padding: 32px 48px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(-8px);
  transition: opacity 200ms ease-out, transform 200ms ease-out, visibility 200ms;
}

.mega-menu-trigger:hover .mega-menu-panel,
.mega-menu-trigger:focus-within .mega-menu-panel {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.mega-menu-column__title {
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #6b7280;
  margin-bottom: 16px;
}

.mega-menu-column__link {
  display: block;
  padding: 8px 0;
  font-size: 14px;
  color: #374151;
  text-decoration: none;
}

.mega-menu-column__link:hover {
  color: #2563eb;
}
```

### Accessibility Requirements
- Trigger must be a `button` element with `aria-expanded` and `aria-controls`
- Panel must have `role="menu"` or be a simple `div` with links (not role=menu if links are standard anchors)
- Arrow keys navigate within the panel
- Escape closes the panel and returns focus to trigger
- The 300ms close delay prevents frustration for users with motor difficulties

### React Component
```tsx
function MegaMenu({ categories }: { categories: Category[] }) {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  return (
    <nav aria-label="Main">
      <ul className="mega-menu-bar">
        {categories.map((cat, i) => (
          <li key={cat.id} className="mega-menu-trigger"
              onMouseEnter={() => setOpenIndex(i)}
              onMouseLeave={() => setOpenIndex(null)}>
            <button
              aria-expanded={openIndex === i}
              aria-controls={`mega-panel-${cat.id}`}
              onClick={() => setOpenIndex(openIndex === i ? null : i)}
            >
              {cat.label}
              <ChevronDown aria-hidden="true" />
            </button>
            {openIndex === i && (
              <div id={`mega-panel-${cat.id}`} className="mega-menu-panel">
                {cat.columns.map(col => (
                  <div key={col.title} className="mega-menu-column">
                    <h3 className="mega-menu-column__title">{col.title}</h3>
                    <ul>
                      {col.links.map(link => (
                        <li key={link.href}>
                          <a href={link.href} className="mega-menu-column__link">
                            {link.label}
                          </a>
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
            )}
          </li>
        ))}
      </ul>
    </nav>
  );
}
```

### Reference Implementations
- Amazon.com — Category mega menu with images
- Target.com — Clean grid mega menu
- Microsoft.com — Feature-organized mega menu with icons

---

## 3. Top Nav with Centered Logo

Logo centered in the nav bar with links distributed equally on either side. Common in fashion, luxury, and brand-focused websites where the brand mark is the visual anchor.

### When to Use
- Fashion, luxury, beauty, lifestyle brands
- Portfolio or creative agency websites
- Any brand where the logo is the primary visual identity element
- Sites with an even number of nav items (distributes well)

### When NOT to Use
- SaaS applications or admin tools (logo is not the focus)
- Sites with odd numbers of nav items (unbalanced split)
- Content-heavy sites where navigation needs more emphasis than branding
- Sites with long nav labels that need horizontal space

### Specs
| Property | Value |
|----------|-------|
| Height | 64-96px (often taller to accommodate centered logo) |
| Logo size | 80-200px wide, centered absolutely or with flexbox |
| Left links | 2-4 items, right-aligned toward center |
| Right links | 2-4 items, left-aligned from center |
| Item spacing | 24-40px |
| Font | Often lighter weight (400) or uppercase small caps |

### CSS Specs
```css
.centered-nav {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  height: 80px;
  padding: 0 48px;
}

.centered-nav__left {
  display: flex;
  justify-content: flex-end;
  gap: 32px;
}

.centered-nav__logo {
  display: flex;
  justify-content: center;
  padding: 0 24px;
}

.centered-nav__right {
  display: flex;
  justify-content: flex-start;
  gap: 32px;
}
```

### Reference Implementations
- Chanel.com — Classic centered logo nav
- Aesop.com — Minimalist centered layout
- Squarespace templates — Multiple centered logo options

---

## 4. Top Nav with Integrated Search Bar

A top navigation bar where the search input is a prominent, always-visible element rather than hidden behind a search icon. The search bar typically occupies 30-50% of the nav bar width.

### When to Use
- E-commerce (Amazon, eBay, Etsy pattern)
- Documentation sites (search is the primary navigation method)
- Knowledge bases and wikis
- Any product where > 40% of users start their journey with search

### When NOT to Use
- Marketing sites with small content volume
- Apps where browsing is the primary discovery method
- Sites with fewer than 50 pages (search is overkill)

### Specs
| Property | Value |
|----------|-------|
| Search bar width | 30-50% of nav bar, min 300px |
| Search bar height | 36-44px |
| Placeholder text | Specific: "Search products..." not generic "Search" |
| Auto-suggest | Show after 2-3 characters, max 8 suggestions |
| Results dropdown | 400-600px wide, max 60vh height |
| Keyboard shortcut | `/` or `Ctrl+K` to focus search |

### CSS Specs
```css
.search-nav {
  display: flex;
  align-items: center;
  gap: 24px;
  height: 64px;
  padding: 0 24px;
}

.search-nav__bar {
  flex: 1;
  max-width: 600px;
  position: relative;
}

.search-nav__input {
  width: 100%;
  height: 40px;
  padding: 0 16px 0 40px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 14px;
  background: #f9fafb;
  transition: border-color 150ms ease, box-shadow 150ms ease;
}

.search-nav__input:focus {
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
  background: #ffffff;
  outline: none;
}

.search-nav__icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #9ca3af;
  pointer-events: none;
}
```

### Reference Implementations
- Amazon.com — Category-scoped search bar
- YouTube.com — Central search bar with voice search
- Algolia DocSearch — Documentation-focused search nav

---

## 5. Top Nav with Utility Bar

A two-row header: a thin utility bar on top (language, account, help, store locator) and the main navigation below. Common on large corporate or e-commerce sites that need to separate system-level navigation from content navigation.

### When to Use
- Large e-commerce sites with global utility needs (language, currency, store finder)
- Enterprise websites serving multiple audiences (investors, press, careers)
- Sites where utility links would clutter the main nav

### When NOT to Use
- Mobile-first products (takes too much vertical space)
- Simple marketing sites
- Apps where vertical space is at a premium

### Specs
| Property | Value |
|----------|-------|
| Utility bar height | 32-40px |
| Utility bar font size | 12-13px |
| Utility bar background | Slightly different shade from main nav |
| Main nav height | 56-72px |
| Total header height | 88-112px |
| Responsive | Utility bar hidden on mobile, items moved to hamburger menu footer |

### CSS Specs
```css
.site-header {
  display: flex;
  flex-direction: column;
}

.utility-bar {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 24px;
  height: 36px;
  padding: 0 24px;
  background: #1f2937;
  color: #d1d5db;
  font-size: 12px;
}

.utility-bar a {
  color: #d1d5db;
  text-decoration: none;
}

.utility-bar a:hover {
  color: #ffffff;
}

.main-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  padding: 0 24px;
  background: #ffffff;
  border-bottom: 1px solid #e5e7eb;
}
```

---

## 6. Sticky/Fixed Top Nav

A top navigation bar that remains visible as the user scrolls down the page. Can be always-fixed or can appear/disappear based on scroll direction (show on scroll up, hide on scroll down).

### When to Use
- Long-form content pages (articles, documentation)
- E-commerce product listing pages
- Any page where users need persistent access to navigation while scrolling

### When NOT to Use
- Short pages that do not scroll much
- Mobile screens where vertical space is critical (consider show-on-scroll-up variant)
- Pages with important hero sections that the nav would obscure

### Specs
| Property | Value |
|----------|-------|
| Position | `position: sticky; top: 0` or `position: fixed; top: 0` |
| Scroll behavior | Always visible, or hide on scroll-down / show on scroll-up |
| Background on scroll | Add shadow or change opacity when scrolled past hero |
| Transition | Background/shadow transitions: 200ms ease |
| Z-index | 1000+ |

### Scroll-Direction Detection (Show on Scroll Up)
```tsx
function useStickyNav() {
  const [visible, setVisible] = useState(true);
  const [scrolled, setScrolled] = useState(false);
  const lastScroll = useRef(0);

  useEffect(() => {
    const handleScroll = () => {
      const current = window.scrollY;
      setScrolled(current > 10);
      setVisible(current < lastScroll.current || current < 100);
      lastScroll.current = current;
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return { visible, scrolled };
}
```

```css
.sticky-nav {
  position: sticky;
  top: 0;
  z-index: 1000;
  transform: translateY(0);
  transition: transform 300ms ease, box-shadow 200ms ease;
}

.sticky-nav--hidden {
  transform: translateY(-100%);
}

.sticky-nav--scrolled {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
```

---

## 7. Transparent/Hero Top Nav

Navigation bar that starts transparent over a hero image or video, then transitions to a solid background as the user scrolls past the hero section. Common on landing pages and portfolio sites.

### When to Use
- Landing pages with full-width hero images/videos
- Portfolio sites
- Travel, hospitality, real estate sites with visual heroes
- Marketing pages where immersion matters

### When NOT to Use
- Pages without a hero section
- When hero image has poor contrast with nav text
- Content-first pages where navigation clarity is paramount

### Specs
| Property | Value |
|----------|-------|
| Initial background | `transparent` or `rgba(0,0,0,0.1)` |
| Scrolled background | Solid color with shadow |
| Text color initial | White (on dark heroes) or dark (on light heroes) |
| Text color scrolled | Standard nav colors |
| Transition | 300ms ease for background and color |
| Scroll threshold | When hero section leaves viewport |

### CSS Specs
```css
.hero-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  height: 72px;
  padding: 0 32px;
  display: flex;
  align-items: center;
  background: transparent;
  color: #ffffff;
  transition: background 300ms ease, color 300ms ease, box-shadow 300ms ease;
}

.hero-nav--solid {
  background: #ffffff;
  color: #111827;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.hero-nav__link {
  color: inherit;
  transition: opacity 150ms ease;
}

.hero-nav__link:hover {
  opacity: 0.8;
}
```

---

## 8. Sidebar Navigation (Always Visible)

A vertical navigation panel on the left side of the viewport, always visible, containing the application's primary navigation. The standard pattern for admin panels, dashboards, and SaaS tools.

### When to Use
- Admin panels and dashboards
- SaaS applications with 6+ sections
- Documentation sites with deep content hierarchies
- Any app where users need constant awareness of available sections

### When NOT to Use
- Marketing or content websites (sidebar is an "app" pattern)
- Mobile-primary products (sidebar takes too much horizontal space)
- Simple tools with 3-4 sections (top nav suffices)

### Specs
| Property | Value |
|----------|-------|
| Width | 240-280px (expanded), 64-72px (collapsed/icon-only) |
| Background | White, very light gray (#f9fafb), or dark (#111827) |
| Item height | 40-48px |
| Item padding | 12px 16px |
| Icon size | 20-24px |
| Font size | 14px, medium weight (500) |
| Active indicator | Background highlight, left border (3-4px), or bold text |
| Separator | 1px line or 16-24px gap between groups |
| Group label | 11-12px uppercase, muted color |
| Scroll | Sidebar scrolls independently if content overflows |
| Position | Fixed to left edge, main content offset by sidebar width |

### CSS Specs
```css
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 256px;
  background: #ffffff;
  border-right: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  z-index: 900;
}

.sidebar__logo {
  height: 64px;
  display: flex;
  align-items: center;
  padding: 0 20px;
  border-bottom: 1px solid #e5e7eb;
  flex-shrink: 0;
}

.sidebar__group-label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #9ca3af;
  padding: 24px 20px 8px;
}

.sidebar__link {
  display: flex;
  align-items: center;
  gap: 12px;
  height: 40px;
  padding: 0 20px;
  font-size: 14px;
  font-weight: 500;
  color: #4b5563;
  text-decoration: none;
  border-radius: 6px;
  margin: 2px 8px;
  transition: background 150ms ease, color 150ms ease;
}

.sidebar__link:hover {
  background: #f3f4f6;
  color: #111827;
}

.sidebar__link[aria-current="page"] {
  background: #eff6ff;
  color: #2563eb;
}

.sidebar__link-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

.sidebar__footer {
  margin-top: auto;
  padding: 16px;
  border-top: 1px solid #e5e7eb;
}

.main-content {
  margin-left: 256px;
  min-height: 100vh;
}
```

### React Component
```tsx
interface SidebarItem {
  icon: React.ReactNode;
  label: string;
  href: string;
  badge?: number;
}

interface SidebarGroup {
  label?: string;
  items: SidebarItem[];
}

function Sidebar({ groups, currentPath, footer }: {
  groups: SidebarGroup[];
  currentPath: string;
  footer?: React.ReactNode;
}) {
  return (
    <aside className="sidebar" aria-label="Main navigation">
      <div className="sidebar__logo">
        <a href="/">Logo</a>
      </div>
      <nav>
        {groups.map((group, gi) => (
          <div key={gi}>
            {group.label && (
              <div className="sidebar__group-label">{group.label}</div>
            )}
            <ul>
              {group.items.map(item => (
                <li key={item.href}>
                  <a
                    href={item.href}
                    className="sidebar__link"
                    aria-current={currentPath.startsWith(item.href) ? 'page' : undefined}
                  >
                    <span className="sidebar__link-icon">{item.icon}</span>
                    <span>{item.label}</span>
                    {item.badge != null && item.badge > 0 && (
                      <span className="sidebar__badge">{item.badge}</span>
                    )}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </nav>
      {footer && <div className="sidebar__footer">{footer}</div>}
    </aside>
  );
}
```

### Reference Implementations
- Linear.app — Clean dark sidebar with keyboard shortcuts
- Notion.so — Sidebar with nested pages and drag-drop
- Stripe Dashboard — Light sidebar with grouped sections

---

## 9. Collapsible Sidebar (Icon-Only to Expanded)

A sidebar that can toggle between a narrow icon-only state (64-72px) and a full expanded state (240-280px). Allows users to reclaim horizontal space while maintaining navigation access.

### When to Use
- Complex applications where users need both nav access and maximum workspace
- Applications with 10+ nav items where icon recognition is strong
- Tools where different users have different screen sizes
- Applications that support both mouse and touch input

### When NOT to Use
- When nav labels are essential for comprehension (new users, uncommon labels)
- Applications with fewer than 6 items (full sidebar is fine)
- When icons are ambiguous or not universally understood

### Specs
| Property | Value |
|----------|-------|
| Collapsed width | 64-72px |
| Expanded width | 240-280px |
| Toggle trigger | Button at bottom of sidebar, or hover, or keyboard shortcut |
| Transition | Width: 200ms ease, content fade: 150ms |
| Tooltip on collapsed | Show label tooltip on hover when collapsed |
| Persistence | Save collapsed state to localStorage |

### CSS Specs
```css
.collapsible-sidebar {
  width: 256px;
  transition: width 200ms ease;
  overflow: hidden;
}

.collapsible-sidebar--collapsed {
  width: 68px;
}

.collapsible-sidebar--collapsed .sidebar__link-label,
.collapsible-sidebar--collapsed .sidebar__group-label,
.collapsible-sidebar--collapsed .sidebar__badge {
  opacity: 0;
  visibility: hidden;
  transition: opacity 100ms ease;
}

.collapsible-sidebar .sidebar__link-label {
  opacity: 1;
  visibility: visible;
  transition: opacity 150ms ease 50ms;
  white-space: nowrap;
}

.collapsible-sidebar__toggle {
  position: absolute;
  bottom: 16px;
  left: 50%;
  transform: translateX(-50%);
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 1px solid #e5e7eb;
  background: #ffffff;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

### Reference Implementations
- VS Code — Collapsible activity bar + sidebar
- Figma — Collapsible layers/assets panels
- Jira — Collapsible project sidebar

---

## 10. Left Sidebar with Nested Groups

A sidebar navigation that organizes items into collapsible groups (sections), each with a group header and child items. Used for deep hierarchies where items belong to clear parent categories.

### When to Use
- Documentation sites (API docs, guides, tutorials)
- Admin panels with feature areas (Users > List, Roles, Permissions)
- Settings pages with many categories
- File management interfaces

### When NOT to Use
- When hierarchy is flat (no meaningful grouping)
- When there are fewer than 3 groups
- When nesting goes deeper than 3 levels (use tree view instead)

### Specs
| Property | Value |
|----------|-------|
| Group header | Clickable to expand/collapse, with chevron icon |
| Indent per level | 16-20px |
| Max nesting depth | 3 levels recommended, 4 maximum |
| Expand/collapse animation | 150-200ms height transition |
| Default state | Top-level groups expanded, nested groups collapsed |
| Active section | Auto-expand parent group of active page |

### CSS Specs
```css
.nested-sidebar__group-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 600;
  color: #374151;
  cursor: pointer;
  user-select: none;
}

.nested-sidebar__group-header:hover {
  background: #f3f4f6;
}

.nested-sidebar__chevron {
  width: 16px;
  height: 16px;
  transition: transform 150ms ease;
}

.nested-sidebar__chevron--expanded {
  transform: rotate(90deg);
}

.nested-sidebar__children {
  overflow: hidden;
  transition: max-height 200ms ease;
}

.nested-sidebar__children--collapsed {
  max-height: 0;
}

.nested-sidebar__child-link {
  padding: 6px 16px 6px 36px; /* indent */
  font-size: 13px;
  color: #6b7280;
  display: block;
  text-decoration: none;
}

.nested-sidebar__child-link:hover {
  color: #111827;
  background: #f9fafb;
}

.nested-sidebar__child-link[aria-current="page"] {
  color: #2563eb;
  font-weight: 500;
  background: #eff6ff;
}

/* Level 3 indent */
.nested-sidebar__child-link--level-3 {
  padding-left: 52px;
}
```

### Reference Implementations
- Stripe Docs — Nested sidebar with auto-expand
- MDN Web Docs — Multi-level documentation sidebar
- AWS Console — Deep nested service navigation

---

## 11. Right Sidebar Navigation

A vertical panel on the right side used for property inspection, contextual controls, or secondary navigation related to the selected content. Not a primary navigation pattern but common in tools and editors.

### When to Use
- Design tools (property inspector)
- Code editors (file outline, minimap)
- Content management (metadata, settings for selected item)
- Email clients (reading pane)

### When NOT to Use
- Primary navigation (users expect primary nav on the left or top)
- Content websites
- Mobile interfaces

### Specs
| Property | Value |
|----------|-------|
| Width | 240-360px |
| Position | Fixed to right edge or within a layout grid |
| Content | Properties, metadata, contextual actions for selected item |
| Scroll | Independent scroll from main content |
| Collapse | Optional collapse to reclaim space |

---

## 12. Top Nav + Left Sidebar Combination

A dual-navigation pattern combining a top horizontal bar (for global/utility navigation) with a left sidebar (for section-specific navigation). The most common pattern in enterprise SaaS applications.

### When to Use
- Enterprise applications with workspace/organization switching
- SaaS tools where the top bar handles account-level nav and sidebar handles feature nav
- Applications where different modules have different sidebar items
- Complex tools with both global context (which project/team) and local navigation (features within that context)

### When NOT to Use
- Simple consumer applications (over-engineered)
- Content or marketing websites
- Mobile-primary products

### Specs
| Property | Value |
|----------|-------|
| Top bar height | 48-56px (thinner than standalone top nav) |
| Top bar content | Logo, workspace switcher, search, notifications, profile |
| Sidebar width | 220-260px |
| Sidebar top | Aligned below top bar |
| Main content | Offset by both top bar height and sidebar width |
| Responsive | Sidebar collapses to hamburger on mobile, top bar stays |

### Layout CSS
```css
.app-layout {
  display: grid;
  grid-template-areas:
    "topbar topbar"
    "sidebar main";
  grid-template-columns: 256px 1fr;
  grid-template-rows: 56px 1fr;
  height: 100vh;
}

.app-topbar {
  grid-area: topbar;
  position: sticky;
  top: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  padding: 0 16px;
  background: #111827;
  color: #ffffff;
}

.app-sidebar {
  grid-area: sidebar;
  overflow-y: auto;
  background: #ffffff;
  border-right: 1px solid #e5e7eb;
}

.app-main {
  grid-area: main;
  overflow-y: auto;
  padding: 24px;
}
```

### Reference Implementations
- GitHub.com — Top bar (user/org) + sidebar (repo sections)
- Slack — Top bar (workspace) + sidebar (channels)
- Jira — Top bar (project) + sidebar (boards, backlog, reports)

---

## 13. Full-Screen Overlay Menu

Clicking a menu trigger (usually a hamburger or custom icon) opens a full-viewport overlay containing the navigation. Content behind is hidden or dimmed. Common on creative, minimal, or experimental websites.

### When to Use
- Creative agency or portfolio sites where the menu is a design statement
- Sites with minimal navigation (3-7 items)
- When you want to focus user attention entirely on navigation choices
- Experimental or editorial websites

### When NOT to Use
- Applications where users navigate frequently (too slow)
- E-commerce (browsing efficiency matters)
- Content sites where navigation is utilitarian
- Any site where opening a menu to see options is a friction

### Specs
| Property | Value |
|----------|-------|
| Trigger | Hamburger icon or custom animation trigger |
| Overlay | Full viewport, solid background or semi-transparent |
| Animation | Fade, slide, or morph (300-500ms for dramatic effect) |
| Font size | Large (24-64px) — the navigation IS the content |
| Item layout | Centered vertically, stacked, with generous spacing |
| Close | X button (top-right), Escape key, click outside |
| Focus trap | Yes — focus must be trapped inside overlay |

### CSS Specs
```css
.overlay-menu {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: #111827;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 400ms ease, visibility 400ms;
}

.overlay-menu--open {
  opacity: 1;
  visibility: visible;
}

.overlay-menu__close {
  position: absolute;
  top: 24px;
  right: 24px;
  width: 48px;
  height: 48px;
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
}

.overlay-menu__list {
  list-style: none;
  text-align: center;
}

.overlay-menu__link {
  display: block;
  font-size: 48px;
  font-weight: 300;
  color: #ffffff;
  text-decoration: none;
  padding: 16px 0;
  opacity: 0.7;
  transition: opacity 200ms ease;
}

.overlay-menu__link:hover,
.overlay-menu__link:focus {
  opacity: 1;
}
```

---

## 14. Tabbed Navigation (Horizontal)

Horizontal tabs that switch between parallel content views within the same page context. Tabs do not navigate to new pages — they toggle visible content panels.

### When to Use
- Switching between related data views (e.g., Table / Chart / Map)
- Content with clear parallel categories (e.g., Description / Reviews / Specs)
- Settings pages with grouped preferences
- Code viewing (different files or output tabs)

### When NOT to Use
- More than 7 tabs (use sidebar or dropdown instead)
- When tab content is very different in structure (use separate pages)
- When tabs would be confused with page-level navigation
- When content in each tab is very long (anchored sections may be better)

### Specs
| Property | Value |
|----------|-------|
| Max tabs | 3-7 visible, overflow with scroll or "More" |
| Tab height | 40-48px |
| Active indicator | Bottom border (2-3px solid), background change, or both |
| Font size | 13-15px, medium weight |
| Tab spacing | 0 (touching) or 4-8px gap |
| Panel transition | Instant (recommended) or fade (150ms) |
| ARIA | `role="tablist"`, `role="tab"`, `role="tabpanel"` |

### CSS Specs
```css
.tabs {
  display: flex;
  border-bottom: 1px solid #e5e7eb;
  gap: 0;
}

.tab {
  padding: 12px 20px;
  font-size: 14px;
  font-weight: 500;
  color: #6b7280;
  background: none;
  border: none;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  transition: color 150ms ease, border-color 150ms ease;
  white-space: nowrap;
}

.tab:hover {
  color: #374151;
}

.tab[aria-selected="true"] {
  color: #2563eb;
  border-bottom-color: #2563eb;
}

.tab:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: -2px;
}

.tab-panel {
  padding: 24px 0;
}

.tab-panel[hidden] {
  display: none;
}
```

### React Component (Accessible)
```tsx
function Tabs({ tabs }: { tabs: { label: string; content: React.ReactNode }[] }) {
  const [activeIndex, setActiveIndex] = useState(0);

  const handleKeyDown = (e: React.KeyboardEvent, index: number) => {
    if (e.key === 'ArrowRight') setActiveIndex((index + 1) % tabs.length);
    if (e.key === 'ArrowLeft') setActiveIndex((index - 1 + tabs.length) % tabs.length);
    if (e.key === 'Home') setActiveIndex(0);
    if (e.key === 'End') setActiveIndex(tabs.length - 1);
  };

  return (
    <div>
      <div role="tablist" className="tabs">
        {tabs.map((tab, i) => (
          <button
            key={i}
            role="tab"
            id={`tab-${i}`}
            className="tab"
            aria-selected={i === activeIndex}
            aria-controls={`panel-${i}`}
            tabIndex={i === activeIndex ? 0 : -1}
            onClick={() => setActiveIndex(i)}
            onKeyDown={(e) => handleKeyDown(e, i)}
          >
            {tab.label}
          </button>
        ))}
      </div>
      {tabs.map((tab, i) => (
        <div
          key={i}
          role="tabpanel"
          id={`panel-${i}`}
          aria-labelledby={`tab-${i}`}
          className="tab-panel"
          hidden={i !== activeIndex}
          tabIndex={0}
        >
          {tab.content}
        </div>
      ))}
    </div>
  );
}
```

---

## 15. Vertical Tab Navigation

Tabs arranged vertically, typically on the left side, with the tab panel content to the right. Common in settings pages and configuration interfaces.

### When to Use
- Settings or preferences pages with many categories
- Configuration panels (5-12 sections)
- When tab labels are long and would not fit horizontally
- Desktop interfaces with sufficient horizontal space

### Specs
| Property | Value |
|----------|-------|
| Tab list width | 180-240px |
| Tab height | 36-44px per tab |
| Active indicator | Left border (3px), background highlight |
| Layout | Side-by-side: tab list (left) + panel (right) |
| ARIA | Same as horizontal tabs: `role="tablist"` with `aria-orientation="vertical"` |

---

## 16. Hub-and-Spoke Navigation

A central "hub" screen (typically a home screen or dashboard) from which users navigate to individual "spoke" screens. Each spoke is a self-contained feature or section. Users return to the hub to switch spokes.

### When to Use
- Mobile apps with distinct feature areas (e.g., banking: accounts, transfer, pay bills, investments)
- Smart TV interfaces
- Kiosk applications
- Applications where features are independent and do not require cross-navigation

### When NOT to Use
- When users frequently switch between spokes (too many return trips to hub)
- Web applications (feels like an app launcher, not natural on web)
- Content-heavy products where browsing across categories is important

### Specs
| Property | Value |
|----------|-------|
| Hub layout | Grid of cards, large touch targets |
| Card size | 120-180px, square or 4:3 ratio |
| Max spokes | 6-12 visible on hub screen |
| Navigation to spoke | Tap card, full-screen transition |
| Return to hub | Back button/gesture or home button |

---

## 17. Dashboard Navigation (Sidebar + Top Bar)

A specialized combination of sidebar navigation with a top utility bar, optimized for analytics, monitoring, and data-heavy interfaces. The sidebar organizes features while the top bar provides global context and actions.

### When to Use
- Analytics dashboards (Google Analytics, Mixpanel)
- Admin control panels
- Monitoring and observability tools
- CRM and ERP interfaces

### Specs
Combines specs from Pattern 12 (Top Nav + Left Sidebar) with additions:
| Property | Value |
|----------|-------|
| Top bar | Date range picker, global filters, refresh, export |
| Sidebar | Feature sections with notification badges |
| Main area | Responsive grid of data widgets |
| Widget nav | Drill-down within widgets (click chart element to filter) |

---

## 18. Command Palette (Cmd+K / Ctrl+K)

A search-driven navigation overlay triggered by a keyboard shortcut. Users type to find and navigate to any page, feature, or action in the application. The power-user navigation pattern.

### When to Use
- Developer tools and code editors
- Complex SaaS applications with many features
- Any application where power users want keyboard-driven navigation
- As a secondary navigation layer complementing visual nav

### When NOT to Use
- As the only navigation (new users need visual nav)
- Consumer mobile apps (no keyboard)
- Simple sites with few pages

### Specs
| Property | Value |
|----------|-------|
| Trigger | `Cmd+K` (Mac), `Ctrl+K` (Windows/Linux), or click search icon |
| Panel width | 560-640px, centered horizontally |
| Panel max-height | 400-500px |
| Position | Centered, 20-30% from top of viewport |
| Backdrop | Semi-transparent dark overlay |
| Input | Auto-focused, with placeholder "Search or type a command..." |
| Results | Grouped by type (Pages, Actions, Recent, Settings) |
| Result limit | 8-12 visible, scroll for more |
| Keyboard nav | Arrow up/down to select, Enter to go, Escape to close |
| Fuzzy matching | Match partial terms, acronyms, abbreviations |
| Response time | Results update within 50-100ms of typing |

### CSS Specs
```css
.command-palette-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 9999;
  display: flex;
  justify-content: center;
  padding-top: 20vh;
}

.command-palette {
  width: 600px;
  max-height: 460px;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.25);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.command-palette__input-wrapper {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  border-bottom: 1px solid #e5e7eb;
}

.command-palette__input {
  flex: 1;
  border: none;
  outline: none;
  font-size: 16px;
  padding: 4px 8px;
}

.command-palette__results {
  overflow-y: auto;
  flex: 1;
}

.command-palette__group-label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: #9ca3af;
  padding: 12px 16px 4px;
}

.command-palette__result {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  cursor: pointer;
  font-size: 14px;
}

.command-palette__result:hover,
.command-palette__result--active {
  background: #f3f4f6;
}

.command-palette__result-icon {
  width: 20px;
  height: 20px;
  color: #6b7280;
}

.command-palette__shortcut {
  margin-left: auto;
  font-size: 12px;
  color: #9ca3af;
}
```

### React Component
```tsx
function CommandPalette({ commands, onSelect, onClose }: CommandPaletteProps) {
  const [query, setQuery] = useState('');
  const [activeIndex, setActiveIndex] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);

  const filtered = useMemo(() =>
    commands.filter(cmd =>
      cmd.label.toLowerCase().includes(query.toLowerCase()) ||
      cmd.keywords?.some(k => k.toLowerCase().includes(query.toLowerCase()))
    ).slice(0, 12),
    [commands, query]
  );

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  useEffect(() => {
    setActiveIndex(0);
  }, [query]);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setActiveIndex(i => Math.min(i + 1, filtered.length - 1));
    }
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      setActiveIndex(i => Math.max(i - 1, 0));
    }
    if (e.key === 'Enter' && filtered[activeIndex]) {
      onSelect(filtered[activeIndex]);
    }
    if (e.key === 'Escape') {
      onClose();
    }
  };

  return (
    <div className="command-palette-backdrop" onClick={onClose}>
      <div className="command-palette" onClick={e => e.stopPropagation()}
           role="dialog" aria-label="Command palette">
        <div className="command-palette__input-wrapper">
          <SearchIcon aria-hidden="true" />
          <input
            ref={inputRef}
            className="command-palette__input"
            placeholder="Search or type a command..."
            value={query}
            onChange={e => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            role="combobox"
            aria-expanded="true"
            aria-controls="command-results"
            aria-activedescendant={`result-${activeIndex}`}
          />
        </div>
        <ul id="command-results" className="command-palette__results" role="listbox">
          {filtered.map((cmd, i) => (
            <li
              key={cmd.id}
              id={`result-${i}`}
              className={`command-palette__result ${i === activeIndex ? 'command-palette__result--active' : ''}`}
              role="option"
              aria-selected={i === activeIndex}
              onClick={() => onSelect(cmd)}
            >
              {cmd.icon && <span className="command-palette__result-icon">{cmd.icon}</span>}
              <span>{cmd.label}</span>
              {cmd.shortcut && <kbd className="command-palette__shortcut">{cmd.shortcut}</kbd>}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
```

### Reference Implementations
- Linear.app — Command palette with actions and navigation
- VS Code — Command palette with file, command, and setting search
- Raycast — System-wide command palette pattern
- Vercel Dashboard — Cmd+K with scoped search

---

## 19. Ribbon Navigation

A wide toolbar organized into tab-grouped panels, each containing categorized action buttons and controls. Pioneered by Microsoft Office 2007.

### When to Use
- Productivity applications with many tools (document editors, spreadsheets)
- Creative tools (image editors, design software)
- Applications where users need rapid access to many categorized actions

### When NOT to Use
- Web applications (too complex for most web UIs)
- Mobile applications (no space)
- Simple CRUD applications

### Specs
| Property | Value |
|----------|-------|
| Ribbon height | 100-130px |
| Tab bar height | 28-32px |
| Panel sections | Divided by vertical separators with section labels |
| Button sizes | Large (32-48px icon + label below) and small (16-20px icon + label right) |
| Collapse | Minimize ribbon to show only tabs |

---

## 20. Tree View Navigation

A hierarchical, expandable/collapsible tree structure showing nested parent-child relationships. Each node can expand to reveal children, creating a visual hierarchy of arbitrary depth.

### When to Use
- File system browsers
- Documentation with deep nesting
- Project structures (folders, files, components)
- Any hierarchical data (org charts, category trees)

### When NOT to Use
- Flat content structures
- When nesting exceeds 5-6 levels (becomes unusable)
- Mobile interfaces (tree views need horizontal space)

### Specs
| Property | Value |
|----------|-------|
| Indent per level | 16-24px |
| Node height | 28-36px |
| Expand/collapse | Click chevron or double-click node |
| Icons | Folder/file icons, or custom per node type |
| Selection | Single or multi-select with Ctrl/Cmd+click |
| Keyboard | Arrow keys navigate, Left collapses, Right expands |
| ARIA | `role="tree"`, `role="treeitem"`, `aria-expanded` |
| Virtualization | Required for 500+ nodes (react-window or similar) |

---

## 21. Card-Based Navigation

Navigation presented as a grid of cards, each representing a destination or content category. Cards provide visual previews and descriptions beyond what a simple text link offers.

### When to Use
- Content discovery and exploration (Netflix, Pinterest)
- Home screens with distinct feature areas
- Portfolio or gallery navigation
- When visual preview helps decision-making

### When NOT to Use
- Utilitarian task-completion interfaces
- When there are more than 16 cards (overwhelming)
- When all items are equally weighted (use a list)

### Specs
| Property | Value |
|----------|-------|
| Card size | 200-320px wide, aspect ratio 3:4 or 16:9 |
| Grid | CSS Grid with `auto-fill, minmax(240px, 1fr)` |
| Gap | 16-24px |
| Card content | Image/icon + title + description (optional) |
| Hover | Subtle lift (translateY -2px) + shadow increase |
| Touch target | Entire card is clickable |

---

## 22. Icon Grid Navigation

A grid of icons with labels, used as a home screen or launcher-style navigation. Each icon represents a top-level destination or feature.

### When to Use
- Mobile app home screens
- App launchers within larger platforms
- Intranet or internal tool directories
- When you have 8-24 destinations of relatively equal importance

### When NOT to Use
- When items have complex descriptions needed for decision-making
- When there are fewer than 6 items (a simple list is better)
- Web applications (feels like a mobile pattern on desktop)

### Specs
| Property | Value |
|----------|-------|
| Icon size | 48-64px (mobile), 40-56px (web) |
| Label | Below icon, 12-14px, max 2 lines |
| Grid columns | 3-4 (mobile), 4-6 (tablet), 6-8 (desktop) |
| Gap | 16-24px vertical, 8-16px horizontal |
| Touch target | 72-88px square minimum |

---

## 23. Wizard/Stepper as Primary Navigation

A sequential navigation pattern where users progress through ordered steps to complete a task. The stepper is the primary navigation, showing progress and allowing navigation to completed steps.

### When to Use
- Multi-step forms (checkout, registration, application)
- Onboarding flows
- Configuration wizards
- Any process with a clear sequential order

### When NOT to Use
- Non-linear tasks where step order does not matter
- Processes with only 1-2 steps (overkill)
- Tasks where users need to compare information across steps

### Specs
| Property | Value |
|----------|-------|
| Step indicator | Number in circle, checkmark when complete |
| Step label | Below or beside the indicator |
| Connector line | Between steps, filled for completed, unfilled for upcoming |
| Clickable steps | Only completed steps and current step are interactive |
| Progress | Visual progress bar or step count (Step 2 of 5) |
| Navigation buttons | "Back" (left, secondary) and "Next" (right, primary) |

---

## 24. Search-First Navigation

Navigation architecture where search is the primary (and sometimes only) way to find content. The traditional browse-based menu is minimized or removed in favor of a prominent search interface.

### When to Use
- Very large content catalogs (millions of items)
- Knowledge bases where users know what they want
- Documentation sites with expert users
- When content does not fit into clean categories

### When NOT to Use
- When users do not know what to search for (need browsing)
- New user experiences (search requires knowing terminology)
- Small content volumes (fewer than 100 items)

### Specs
| Property | Value |
|----------|-------|
| Search prominence | Center of page, large input (48-56px height) |
| Auto-complete | Show suggestions after 1-2 characters |
| Filters | Faceted filters alongside results |
| No-results | Suggest alternatives, show popular items |
| Recent searches | Show recent and popular searches on focus |

---

## 25. Split Navigation

Navigation divided into two separate groups on opposite sides of the nav bar. Typically, content navigation is on the left and action/utility navigation is on the right.

### When to Use
- Applications with distinct browse and create modes
- Sites where primary nav and utility nav need visual separation
- When you want to highlight a CTA (sign up, create, buy) separately from content nav

### When NOT to Use
- When there is no logical split between nav groups
- Mobile (everything should be in one nav pattern)

### Specs
| Property | Value |
|----------|-------|
| Left group | Logo + 3-5 content/browse links |
| Right group | 2-3 action/utility items (search, profile, CTA button) |
| Layout | `display: flex; justify-content: space-between` |
| CTA | Visually distinct (filled button vs. text links) |

---

## 26. Dropdown Navigation Bar

A horizontal navigation bar where each top-level item opens a simple single-column dropdown menu on hover or click. Simpler than a mega menu but supports one level of nesting.

### When to Use
- Medium-complexity websites with 2-6 subcategories per section
- Corporate or institutional websites
- When mega menu is overkill but flat nav is insufficient

### When NOT to Use
- When subcategories exceed 8-10 per dropdown (use mega menu)
- When there are no subcategories (use flat top nav)
- Mobile (convert to accordion in hamburger menu)

### Specs
| Property | Value |
|----------|-------|
| Dropdown width | Min 180px, auto-sized to longest item |
| Dropdown max items | 8-10 visible, scroll if more |
| Trigger | Hover with 100-200ms delay (desktop), tap (mobile) |
| Animation | Fade in + slight Y translate, 150ms |
| Close | Mouse leave with 200ms delay, or click elsewhere |
| Separator | 1px line between groups within dropdown |
| Arrow indicator | Small downward chevron next to trigger label |

---

## 27. Progressive Disclosure Navigation

Navigation that starts with a minimal set of visible items and progressively reveals more options as the user demonstrates need (through exploration, account maturity, or explicit request). Prevents overwhelming new users while supporting power users.

### When to Use
- Complex applications with learning curves
- Freemium products where features unlock with plan upgrades
- Enterprise tools that serve novice and expert users
- When the full navigation has 15+ items

### When NOT to Use
- When all navigation items are equally important from day one
- When hiding items causes findability problems
- Consumer products where simplicity is already achieved

### Specs
| Property | Value |
|----------|-------|
| Initial visible items | 3-5 most common features |
| "More" trigger | "More" link, ellipsis icon, or "Show all features" |
| Reveal animation | Expand/slide, 200ms |
| Persistence | Remember revealed state per user |
| Onboarding | Progressively add nav items as user completes tasks |

### Strategies
1. **Feature-gated**: Hide nav items for features the user has not unlocked
2. **Usage-based**: Promote frequently used items to top, demote rarely used
3. **Role-based**: Show items relevant to user's role
4. **Experience-based**: Show basic nav for new users, full nav for experienced

---

## Pattern Comparison Matrix

| Pattern | Items | Depth | Mobile | Desktop | Accessibility | Complexity |
|---------|-------|-------|--------|---------|--------------|------------|
| Top Horizontal Nav | 5-7 | 1 | Hamburger | Native | Simple | Low |
| Mega Menu | 5-8 x many | 2 | Accordion | Native | Complex | High |
| Sidebar | 8-15 | 2-3 | Overlay | Native | Medium | Medium |
| Collapsible Sidebar | 8-15 | 2-3 | Overlay | Native | Complex | High |
| Bottom Tab Bar | 3-5 | 1 | Native | N/A | Simple | Low |
| Command Palette | Unlimited | Flat | N/A | Native | Complex | High |
| Hub-and-Spoke | 6-12 | 1 | Native | Cards | Simple | Low |
| Tabs | 3-7 | 1 | Scroll | Native | Medium | Medium |
| Full-Screen Overlay | 5-10 | 1 | Native | Native | Medium | Medium |
| Tree View | Unlimited | Unlimited | N/A | Native | Complex | High |
| Stepper | 3-7 | Sequential | Native | Native | Medium | Medium |
| Search-First | Unlimited | Flat | Native | Native | Medium | High |
