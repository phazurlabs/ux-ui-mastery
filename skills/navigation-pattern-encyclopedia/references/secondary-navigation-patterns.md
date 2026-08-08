# Secondary & Contextual Navigation Patterns — Complete Reference

> 22 secondary and contextual navigation patterns with exact specs, accessibility requirements, production code, and decision criteria.

---

## What Makes Navigation "Secondary"

Secondary navigation operates within the context established by primary navigation. If primary navigation answers "what section am I in?", secondary navigation answers "where am I within this section?" and "what related content exists?". Secondary navigation is always visually subordinate to primary navigation — smaller, lighter, positioned below or beside it — and often changes based on the current section or page.

The critical design rule: secondary navigation must never compete with primary navigation for attention. If a user's eye is drawn to secondary nav before primary nav, your visual hierarchy has failed.

---

## Pattern Index

| # | Pattern | Best For | Typical Position |
|---|---------|----------|-----------------|
| 1 | Simple Breadcrumbs | Hierarchical sites, e-commerce | Top of content area |
| 2 | Breadcrumbs with Dropdown | Deep hierarchies needing sibling access | Top of content area |
| 3 | Truncated Breadcrumbs | Very deep paths (5+ levels) | Top of content area |
| 4 | Sub-Navigation Bar | Section-level navigation | Below primary nav |
| 5 | Contextual Sidebar (In-Page) | Long-form content sections | Left or right of content |
| 6 | Anchor Navigation (Scroll-to-Section) | Long single-page content | Sticky sidebar or top |
| 7 | Sticky Anchor Bar | Documentation, article sections | Sticks below primary nav |
| 8 | Numbered Pagination | Search results, product listings | Bottom of list |
| 9 | Prev/Next Pagination | Sequential content (articles, tutorials) | Bottom of content |
| 10 | Load More Button | Social feeds, product grids | Below loaded items |
| 11 | Infinite Scroll | Social feeds, image galleries | Automatic on scroll |
| 12 | Cursor-Based Pagination | API-driven lists, real-time data | Bottom with directional controls |
| 13 | Stepper Navigation (Form Wizard) | Multi-step forms, onboarding | Top of form area |
| 14 | Segmented Control | View switching (2-5 options) | Inline with content |
| 15 | Filter Tabs | Content filtering by type/status | Above content list |
| 16 | Back Button / Back Link | Return to previous context | Top-left of content |
| 17 | Related Content Links | Content discovery | Bottom or sidebar |
| 18 | Floating Action Menu (FAB + Speed Dial) | Quick contextual actions | Bottom-right corner |
| 19 | Table of Contents | Long documents | Sidebar or top |
| 20 | In-Page Section Tabs | Content organization within a page | Inline with content |
| 21 | Quick Links / Jump Bar | Alphabetical or categorical quick access | Top of list/directory |
| 22 | Contextual Action Bar | Bulk actions, selection-dependent actions | Top of content area |

---

## 1. Simple Breadcrumbs

A horizontal trail showing the user's path from the root to the current page. Each level is a clickable link except the current page (which is text only or aria-current="page").

### When to Use
- E-commerce category hierarchies (Home > Shoes > Running > Nike Air Max)
- Documentation sites with clear hierarchy
- Any site with 3+ levels of depth where users may land deep via search
- Content management systems

### When NOT to Use
- Flat sites with no hierarchy (breadcrumbs would just show Home > Current)
- Mobile apps (use back button instead)
- Single-page applications with no meaningful hierarchy
- When the path to a page is not linear (e.g., a page reachable from multiple parents)

### Specs
| Property | Value |
|----------|-------|
| Separator | `>` or `/` or chevron icon (`) |
| Font size | 13-14px |
| Color | Muted gray for links, darker for current page |
| Current page | Not a link. Use `aria-current="page"` |
| Max visible | 4-5 levels before truncation |
| Position | Below primary nav, above page title, 16-24px margin |
| Interaction | Hover underline on links, no hover effect on current page |
| Wrapper | `<nav aria-label="Breadcrumb">` with `<ol>` |

### CSS Specs
```css
.breadcrumbs {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 4px;
  font-size: 13px;
  padding: 12px 0;
}

.breadcrumbs__item {
  display: flex;
  align-items: center;
  gap: 4px;
}

.breadcrumbs__link {
  color: #6b7280;
  text-decoration: none;
}

.breadcrumbs__link:hover {
  color: #2563eb;
  text-decoration: underline;
}

.breadcrumbs__separator {
  color: #d1d5db;
  font-size: 12px;
  user-select: none;
}

.breadcrumbs__current {
  color: #111827;
  font-weight: 500;
}
```

### React Component (Accessible)
```tsx
interface BreadcrumbItem {
  label: string;
  href?: string;
}

function Breadcrumbs({ items }: { items: BreadcrumbItem[] }) {
  return (
    <nav aria-label="Breadcrumb">
      <ol className="breadcrumbs">
        {items.map((item, i) => (
          <li key={i} className="breadcrumbs__item">
            {i > 0 && (
              <span className="breadcrumbs__separator" aria-hidden="true">
                /
              </span>
            )}
            {item.href ? (
              <a href={item.href} className="breadcrumbs__link">
                {item.label}
              </a>
            ) : (
              <span className="breadcrumbs__current" aria-current="page">
                {item.label}
              </span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}
```

### Structured Data (SEO)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com" },
    { "@type": "ListItem", "position": 2, "name": "Shoes", "item": "https://example.com/shoes" },
    { "@type": "ListItem", "position": 3, "name": "Running", "item": "https://example.com/shoes/running" }
  ]
}
</script>
```

### Reference Implementations
- Amazon.com — Category breadcrumbs with click-through
- Google Search Results — Breadcrumb display in search snippets

---

## 2. Breadcrumbs with Dropdown

Each breadcrumb level includes a small dropdown that shows sibling pages at that level, allowing users to navigate laterally without going back up the tree.

### When to Use
- When users frequently need to switch between siblings at the same level
- Deep product hierarchies where browsing siblings is common
- File managers showing directory structure

### When NOT to Use
- When sibling pages number more than 15-20 (dropdown becomes unwieldy)
- Simple hierarchies where lateral navigation is rare
- Mobile interfaces (dropdowns are hard to use on touch)

### Specs
| Property | Value |
|----------|-------|
| Dropdown trigger | Chevron icon next to breadcrumb text, or click breadcrumb itself |
| Dropdown width | Auto (min 160px, max 300px) |
| Dropdown max items | 10-15 visible, scroll for more |
| Position | Below the breadcrumb item, left-aligned |
| Current sibling | Highlighted or checked in dropdown |

### CSS Specs
```css
.breadcrumb-dropdown {
  position: relative;
}

.breadcrumb-dropdown__trigger {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  cursor: pointer;
  padding: 2px 4px;
  border-radius: 4px;
}

.breadcrumb-dropdown__trigger:hover {
  background: #f3f4f6;
}

.breadcrumb-dropdown__menu {
  position: absolute;
  top: 100%;
  left: 0;
  min-width: 180px;
  max-height: 320px;
  overflow-y: auto;
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 4px;
  z-index: 100;
}

.breadcrumb-dropdown__item {
  display: block;
  padding: 8px 12px;
  font-size: 13px;
  color: #374151;
  text-decoration: none;
  border-radius: 4px;
}

.breadcrumb-dropdown__item:hover {
  background: #f3f4f6;
}

.breadcrumb-dropdown__item[aria-current="page"] {
  background: #eff6ff;
  color: #2563eb;
  font-weight: 500;
}
```

---

## 3. Truncated Breadcrumbs

When the breadcrumb path exceeds 4-5 levels, middle levels are collapsed into an ellipsis (...) that expands on click to reveal hidden levels. Always shows the first level (Home/root) and the last 2-3 levels.

### When to Use
- Very deep hierarchies (5+ levels)
- When horizontal space is limited
- File system paths or deeply nested categories

### Specs
| Property | Value |
|----------|-------|
| Truncation threshold | 4-5 visible items |
| Always visible | First item + last 2-3 items |
| Ellipsis | "..." button that expands to show hidden items |
| Expanded state | All items visible, or dropdown with hidden items |

### CSS Specs
```css
.breadcrumbs--truncated .breadcrumbs__ellipsis {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 24px;
  border-radius: 4px;
  background: none;
  border: none;
  color: #6b7280;
  cursor: pointer;
  font-size: 14px;
  letter-spacing: 2px;
}

.breadcrumbs--truncated .breadcrumbs__ellipsis:hover {
  background: #f3f4f6;
}
```

---

## 4. Sub-Navigation Bar

A horizontal bar positioned below the primary navigation, containing links specific to the current section. Changes content based on which primary nav section is active.

### When to Use
- Marketing sites with sections that have 3-7 subsections
- Product pages with tabs-like secondary categories
- Documentation sites showing major topic areas within a section
- News sites with sub-categories (Sports > Football, Basketball, Baseball)

### When NOT to Use
- When subsections exceed 7-8 items (use sidebar instead)
- When sub-nav content is the same across all primary sections
- Mobile layouts (stacks awkwardly; use tabs or accordion instead)

### Specs
| Property | Value |
|----------|-------|
| Height | 40-48px |
| Position | Directly below primary nav, no gap or 1px border |
| Background | Slightly different shade from primary nav, or same with border |
| Font size | 13-14px |
| Active indicator | Bottom border (2px), background highlight, or bold |
| Max items | 5-8 |
| Scroll behavior | Horizontal scroll on overflow (with scroll indicators) |

### CSS Specs
```css
.sub-nav {
  display: flex;
  align-items: center;
  height: 44px;
  padding: 0 24px;
  background: #f9fafb;
  border-bottom: 1px solid #e5e7eb;
  overflow-x: auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.sub-nav::-webkit-scrollbar {
  display: none;
}

.sub-nav__link {
  white-space: nowrap;
  padding: 10px 16px;
  font-size: 14px;
  font-weight: 500;
  color: #6b7280;
  text-decoration: none;
  border-bottom: 2px solid transparent;
  transition: color 150ms ease, border-color 150ms ease;
}

.sub-nav__link:hover {
  color: #374151;
}

.sub-nav__link[aria-current="page"] {
  color: #2563eb;
  border-bottom-color: #2563eb;
}
```

### Reference Implementations
- GitHub.com — Repository sub-nav (Code, Issues, Pull Requests, Actions...)
- Medium.com — Publication sub-categories

---

## 5. Contextual Sidebar (In-Page Sections)

A sidebar within the content area (not the global sidebar) that provides navigation for sections within the current page. Typically shows a list of page sections or related subpages.

### When to Use
- Long documentation pages with many sections
- Product detail pages with multiple info areas
- Settings pages with grouped preferences
- Any page where inline section navigation aids scanning

### When NOT to Use
- Short pages with little content
- Mobile layouts (move to sticky top anchor bar instead)
- When the sidebar would duplicate the global sidebar content

### Specs
| Property | Value |
|----------|-------|
| Width | 200-260px |
| Position | Left or right of main content, within the content grid |
| Sticky behavior | `position: sticky; top: 80px` (below fixed nav) |
| Active detection | Highlight current section based on scroll position (Intersection Observer) |
| Font size | 13-14px |
| Indent | 12-16px for nested items |

### CSS Specs
```css
.page-sidebar {
  width: 220px;
  position: sticky;
  top: 80px;
  max-height: calc(100vh - 100px);
  overflow-y: auto;
  flex-shrink: 0;
}

.page-sidebar__title {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #9ca3af;
  margin-bottom: 12px;
}

.page-sidebar__link {
  display: block;
  padding: 6px 12px;
  font-size: 13px;
  color: #6b7280;
  text-decoration: none;
  border-left: 2px solid transparent;
  transition: color 150ms ease, border-color 150ms ease;
}

.page-sidebar__link:hover {
  color: #111827;
}

.page-sidebar__link--active {
  color: #2563eb;
  border-left-color: #2563eb;
  font-weight: 500;
}

.page-sidebar__link--nested {
  padding-left: 28px;
  font-size: 12px;
}
```

### Scroll Spy Implementation
```tsx
function useScrollSpy(sectionIds: string[]) {
  const [activeId, setActiveId] = useState(sectionIds[0]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter(entry => entry.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);

        if (visible.length > 0) {
          setActiveId(visible[0].target.id);
        }
      },
      { rootMargin: '-80px 0px -60% 0px', threshold: 0 }
    );

    sectionIds.forEach(id => {
      const el = document.getElementById(id);
      if (el) observer.observe(el);
    });

    return () => observer.disconnect();
  }, [sectionIds]);

  return activeId;
}
```

### Reference Implementations
- MDN Web Docs — In-page section sidebar
- Stripe Docs — Sticky table of contents sidebar
- Tailwind CSS Docs — Right sidebar with scroll spy

---

## 6. Anchor Navigation (Scroll-to-Section)

A set of links that smooth-scroll to specific sections within the same page. Can be positioned as a sidebar, a horizontal bar, or integrated into the page header.

### When to Use
- Single-page marketing or landing pages
- Long-form articles with clear sections
- FAQ pages
- Product pages with Description / Specs / Reviews sections

### When NOT to Use
- Multi-page content (these are real page links, not anchors)
- Very short pages where all content is visible without scrolling
- When sections are dynamically loaded (scroll targets may not exist yet)

### Specs
| Property | Value |
|----------|-------|
| Scroll behavior | `scroll-behavior: smooth` or JS with easing |
| Scroll offset | Account for fixed/sticky nav height (e.g., `scroll-margin-top: 80px`) |
| URL update | Update hash fragment (`#section-name`) on scroll |
| Active state | Highlight current section link based on scroll position |
| Animation duration | 300-500ms, ease-out |

### CSS Specs
```css
/* Smooth scrolling with offset for fixed nav */
html {
  scroll-behavior: smooth;
}

[id] {
  scroll-margin-top: 80px; /* height of fixed nav */
}

.anchor-nav {
  display: flex;
  gap: 24px;
  padding: 12px 0;
  border-bottom: 1px solid #e5e7eb;
}

.anchor-nav__link {
  font-size: 14px;
  font-weight: 500;
  color: #6b7280;
  text-decoration: none;
  padding-bottom: 12px;
  border-bottom: 2px solid transparent;
  margin-bottom: -13px;
}

.anchor-nav__link--active {
  color: #2563eb;
  border-bottom-color: #2563eb;
}
```

---

## 7. Sticky Anchor Bar

An anchor navigation bar that becomes sticky (fixed to the top, below the primary nav) once the user scrolls past its natural position. Provides persistent section navigation for long pages.

### When to Use
- Product detail pages (Apple product pages pattern)
- Long comparison pages
- Documentation pages with multiple major sections
- Any long-scroll page where section access is needed throughout

### Specs
| Property | Value |
|----------|-------|
| Position | `position: sticky; top: [nav-height]` |
| Height | 44-52px |
| Background | Solid with slight shadow when stuck |
| Z-index | 999 (below primary nav) |
| Stuck detection | Use Intersection Observer to add shadow when stuck |

### CSS Specs
```css
.sticky-anchor-bar {
  position: sticky;
  top: 64px; /* height of primary nav */
  z-index: 999;
  background: #ffffff;
  border-bottom: 1px solid #e5e7eb;
  transition: box-shadow 200ms ease;
}

.sticky-anchor-bar--stuck {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}
```

---

## 8. Numbered Pagination

Classic page navigation with numbered page links, used for large datasets split across multiple pages. Shows first page, last page, current page with neighbors, and ellipsis for gaps.

### When to Use
- Search results pages
- Product listing pages (e-commerce)
- Blog archives or article lists
- Any paginated data where users may want to jump to specific pages

### When NOT to Use
- Real-time or frequently updating content (items shift between pages)
- When total count is unknown (use cursor-based pagination)
- Social feeds or timelines (use infinite scroll or load more)
- Very small datasets (< 2 pages)

### Specs
| Property | Value |
|----------|-------|
| Visible page numbers | Current +/- 2 neighbors, first page, last page |
| Ellipsis | Between gaps in page sequence |
| Button size | 36-44px square or min-width |
| Active page | Solid background, different color |
| Disabled state | Prev disabled on page 1, Next disabled on last page |
| Position | Centered, below the list, 24-32px margin |
| Items per page | Typically 10, 20, 25, 50 — optionally user-selectable |

### CSS Specs
```css
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 24px 0;
}

.pagination__button {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 40px;
  height: 40px;
  padding: 0 12px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  background: #ffffff;
  font-size: 14px;
  color: #374151;
  cursor: pointer;
  text-decoration: none;
  transition: background 150ms ease, border-color 150ms ease;
}

.pagination__button:hover {
  background: #f3f4f6;
  border-color: #9ca3af;
}

.pagination__button[aria-current="page"] {
  background: #2563eb;
  border-color: #2563eb;
  color: #ffffff;
}

.pagination__button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination__ellipsis {
  min-width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #9ca3af;
}
```

### React Component (Accessible)
```tsx
function Pagination({ currentPage, totalPages, onPageChange }: PaginationProps) {
  const getPages = () => {
    const pages: (number | 'ellipsis')[] = [];
    const delta = 2;
    const left = Math.max(2, currentPage - delta);
    const right = Math.min(totalPages - 1, currentPage + delta);

    pages.push(1);
    if (left > 2) pages.push('ellipsis');
    for (let i = left; i <= right; i++) pages.push(i);
    if (right < totalPages - 1) pages.push('ellipsis');
    if (totalPages > 1) pages.push(totalPages);

    return pages;
  };

  return (
    <nav aria-label="Pagination">
      <ul className="pagination">
        <li>
          <button
            className="pagination__button"
            disabled={currentPage === 1}
            onClick={() => onPageChange(currentPage - 1)}
            aria-label="Previous page"
          >
            Previous
          </button>
        </li>
        {getPages().map((page, i) =>
          page === 'ellipsis' ? (
            <li key={`ellipsis-${i}`}>
              <span className="pagination__ellipsis" aria-hidden="true">...</span>
            </li>
          ) : (
            <li key={page}>
              <button
                className="pagination__button"
                aria-current={page === currentPage ? 'page' : undefined}
                aria-label={`Page ${page}`}
                onClick={() => onPageChange(page)}
              >
                {page}
              </button>
            </li>
          )
        )}
        <li>
          <button
            className="pagination__button"
            disabled={currentPage === totalPages}
            onClick={() => onPageChange(currentPage + 1)}
            aria-label="Next page"
          >
            Next
          </button>
        </li>
      </ul>
    </nav>
  );
}
```

---

## 9. Prev/Next Pagination

Sequential navigation showing only "Previous" and "Next" buttons, optionally with titles of the adjacent items. Used for linear content where users read sequentially.

### When to Use
- Blog articles in a series
- Documentation pages with a reading order
- Multi-page tutorials or guides
- Book chapters or course lessons

### When NOT to Use
- Non-sequential content (use numbered pagination)
- When users need to jump to specific pages
- Search results (users want to know page numbers)

### Specs
| Property | Value |
|----------|-------|
| Layout | Full-width, Prev on left, Next on right |
| Content | Direction label + item title (optional) |
| Button height | 56-72px |
| Keyboard shortcut | Optional: left/right arrow keys for page navigation |

### CSS Specs
```css
.prev-next {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  padding: 32px 0;
  border-top: 1px solid #e5e7eb;
}

.prev-next__link {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 16px 20px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  text-decoration: none;
  max-width: 50%;
  transition: border-color 150ms ease;
}

.prev-next__link:hover {
  border-color: #2563eb;
}

.prev-next__label {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  color: #6b7280;
}

.prev-next__title {
  font-size: 15px;
  font-weight: 500;
  color: #111827;
}

.prev-next__link--next {
  text-align: right;
  margin-left: auto;
}
```

---

## 10. Load More Button

A button at the bottom of a content list that loads the next batch of items when clicked. A middle ground between traditional pagination and infinite scroll.

### When to Use
- Product grids where users browse but may want to stop
- Social feeds where user control over loading is desired
- Search results on mobile (better than tiny pagination buttons)
- When you want to preserve scroll position and footer access

### When NOT to Use
- When the total dataset is very large (users never reach the end)
- When users need to jump to specific sections of the list
- Real-time data where new items appear at the top

### Specs
| Property | Value |
|----------|-------|
| Button width | 200-320px, centered |
| Button height | 44-48px |
| Label | "Load more", "Show more results", or "Load 20 more" |
| Loading state | Show spinner or skeleton placeholders |
| Count | Optionally show "Showing 20 of 156 results" |
| Batch size | Same as initial load (typically 10-20 items) |

---

## 11. Infinite Scroll

Content automatically loads as the user scrolls near the bottom of the list. No explicit trigger needed — new items appear seamlessly.

### When to Use
- Social media feeds (Twitter/X, Instagram, TikTok)
- Image galleries and Pinterest-style layouts
- Content discovery interfaces where browsing is the activity
- When the list is the entire purpose of the page

### When NOT to Use
- E-commerce product listings (users need to reach footer, compare options)
- Content with a meaningful footer (infinite scroll buries the footer)
- When users need to find a specific item (use search + pagination)
- When back-button behavior is important (scroll position is lost)

### Specs
| Property | Value |
|----------|-------|
| Trigger distance | 200-500px before bottom (IntersectionObserver threshold) |
| Loading indicator | Spinner or skeleton cards below existing content |
| End state | "You've reached the end" message |
| Scroll restoration | Must preserve position on back navigation (complex to implement) |
| Performance | Virtualize off-screen items for lists > 100 items |

### Implementation Concerns
1. **Footer inaccessibility**: The footer can never be reached. Move footer content to a sidebar or top nav.
2. **Scroll position loss**: When navigating away and back, the scroll position and loaded items must be restored.
3. **Memory**: Loading thousands of DOM nodes will crash mobile browsers. Use virtualization (react-window, tanstack-virtual).
4. **Analytics**: Traditional pageview tracking does not work. Use scroll-depth events.
5. **Accessibility**: Announce new content with `aria-live="polite"`.

---

## 12. Cursor-Based Pagination

A pagination approach using opaque cursors (tokens) instead of page numbers. The API returns a "next cursor" that the client uses to fetch the next batch. No page numbers are shown — only "Load more" or "Next" buttons.

### When to Use
- Real-time or frequently changing datasets (items added/removed between requests)
- Very large datasets where calculating total count is expensive
- API-driven lists (GraphQL cursor connections)
- When data ordering is guaranteed (chronological, by ID)

### When NOT to Use
- When users need to jump to arbitrary pages
- When total count and page numbers are useful context
- Small static datasets

---

## 13. Stepper Navigation (Form Wizard)

A progress-based navigation for multi-step forms or workflows. Shows all steps, the current step, completed steps, and optionally allows navigation to completed steps.

### When to Use
- Checkout flows (Cart > Shipping > Payment > Confirmation)
- Registration or onboarding flows
- Application forms (insurance, mortgage, job application)
- Configuration wizards (setup, customize, review, deploy)

### When NOT to Use
- Processes with only 1-2 steps
- Non-linear workflows where step order is flexible
- When steps vary dramatically in length (some steps take seconds, others minutes)

### Specs
| Property | Value |
|----------|-------|
| Step count | 3-7 steps (ideal: 3-5) |
| Step indicator | Circle with number or checkmark |
| Step label | Below or beside indicator, 12-14px |
| Connector | Horizontal line between steps |
| Connector states | Filled/colored for completed, gray for upcoming |
| Active step | Larger circle, primary color, possibly pulsing subtle animation |
| Clickable | Only completed steps and current step are clickable |
| Mobile | Compact: show current step number and total ("Step 2 of 4") |

### CSS Specs
```css
.stepper {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px 0;
}

.stepper__step {
  display: flex;
  align-items: center;
  gap: 8px;
}

.stepper__indicator {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 600;
  border: 2px solid #d1d5db;
  color: #6b7280;
  background: #ffffff;
  transition: all 200ms ease;
}

.stepper__indicator--active {
  border-color: #2563eb;
  background: #2563eb;
  color: #ffffff;
}

.stepper__indicator--completed {
  border-color: #16a34a;
  background: #16a34a;
  color: #ffffff;
}

.stepper__label {
  font-size: 13px;
  font-weight: 500;
  color: #6b7280;
}

.stepper__label--active {
  color: #111827;
}

.stepper__connector {
  flex: 1;
  height: 2px;
  background: #d1d5db;
  margin: 0 12px;
  min-width: 40px;
}

.stepper__connector--completed {
  background: #16a34a;
}
```

### Reference Implementations
- Shopify Checkout — Clean 3-step stepper
- TurboTax — Multi-step tax filing wizard
- Stripe Connect onboarding — Progressive step flow

---

## 14. Segmented Control

A set of 2-5 mutually exclusive options that switch the view or filter displayed content. Visually resembles a button group where one option is always selected. Unlike tabs, segmented controls typically change the presentation of the same data rather than switching between different data.

### When to Use
- Switching between view modes (Grid / List, Map / Satellite)
- Toggling between time periods (Day / Week / Month)
- Choosing between 2-4 related options
- When all options are equally weighted (no hierarchy)

### When NOT to Use
- More than 5 options (use tabs or dropdown)
- When options navigate to different pages (use tabs or links)
- When options are not mutually exclusive (use checkboxes)

### Specs
| Property | Value |
|----------|-------|
| Options | 2-5, all visible at once |
| Height | 32-40px |
| Selected state | Filled background (white on dark, or colored) |
| Animation | Background pill slides to selected option, 150-200ms |
| Border | 1px solid, rounded corners (6-8px), contained within a group |
| ARIA | `role="radiogroup"` with `role="radio"` for each option |

### CSS Specs
```css
.segmented-control {
  display: inline-flex;
  background: #f3f4f6;
  border-radius: 8px;
  padding: 3px;
  gap: 2px;
}

.segmented-control__option {
  padding: 6px 16px;
  font-size: 13px;
  font-weight: 500;
  color: #6b7280;
  background: transparent;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: color 150ms ease, background 150ms ease;
}

.segmented-control__option:hover {
  color: #374151;
}

.segmented-control__option[aria-checked="true"] {
  background: #ffffff;
  color: #111827;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
```

---

## 15. Filter Tabs

Horizontal tabs that filter a content list by type, status, or category. Unlike regular tabs that swap entire content panels, filter tabs narrow down a shared content list.

### When to Use
- Filtering items by status (All / Active / Archived / Drafts)
- Filtering by type (All / Images / Videos / Documents)
- Email categories (Primary / Social / Promotions)
- Task boards (All / To Do / In Progress / Done)

### When NOT to Use
- When filters are complex or multi-dimensional (use a filter panel)
- When there are more than 7-8 categories
- When categories overlap (items belong to multiple categories)

### Specs
| Property | Value |
|----------|-------|
| Max tabs | 5-8 |
| Count badge | Show item count per tab: "Active (24)" |
| Active indicator | Bottom border or background highlight |
| Loading | Show skeleton content while filtering |
| URL integration | Reflect active filter in URL query param |

---

## 16. Back Button / Back Link

An explicit "Back" or "Go back" link that returns the user to the previous context. Distinct from the browser back button — this is an in-app navigation element.

### When to Use
- Detail views that were opened from a list (Back to search results)
- Multi-step processes (Back to previous step)
- Modal-like pages that feel like they should have a "close" action
- Mobile web views that do not have a reliable browser back button

### When NOT to Use
- As a substitute for breadcrumbs (back link shows only one level)
- When the "previous" context is ambiguous (user could have come from multiple places)
- In tandem with breadcrumbs (redundant)

### Specs
| Property | Value |
|----------|-------|
| Position | Top-left, above the page title |
| Icon | Left-pointing arrow or chevron |
| Label | "Back", "Back to [context]", or contextual: "All projects" |
| Font size | 13-14px |
| Behavior | Navigate to the logical parent, not browser history |

### CSS Specs
```css
.back-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 500;
  color: #6b7280;
  text-decoration: none;
  padding: 4px 0;
  margin-bottom: 12px;
}

.back-link:hover {
  color: #2563eb;
}

.back-link__icon {
  width: 16px;
  height: 16px;
}
```

---

## 17. Related Content Links

A section showing editorially or algorithmically curated links to related content. Appears at the bottom or side of an article, product, or page to encourage further exploration.

### When to Use
- Blog posts and articles ("Related articles", "You might also like")
- E-commerce product pages ("Customers also bought", "Similar products")
- Documentation pages ("See also", "Related topics")
- Video platforms ("Up next", "Recommended for you")

### When NOT to Use
- When there is no genuinely related content
- When it distracts from a primary CTA (e.g., checkout page)
- When the algorithm produces irrelevant recommendations

### Specs
| Property | Value |
|----------|-------|
| Position | Bottom of content (most common) or sidebar |
| Number of items | 3-6 (grid) or 4-8 (list) |
| Layout | Card grid (2-3 columns) or horizontal scroll |
| Content per item | Image + title + date/category + excerpt (optional) |
| Heading | "Related articles", "You might also like", "More from [category]" |

---

## 18. Floating Action Menu (FAB + Speed Dial)

A floating action button that, when activated, expands to reveal 3-6 related quick actions. The actions fan out vertically or radially from the FAB. Primarily a Material Design mobile pattern.

### When to Use
- Mobile apps with a primary creation action plus related actions
- When there are 3-6 contextual actions that are frequently needed
- Apps following Material Design guidelines

### When NOT to Use
- Desktop applications (use toolbar or command palette instead)
- When there is only one primary action (use a single FAB without expansion)
- When there are more than 6 actions (use a bottom sheet or menu)
- iOS apps (FAB is not a native iOS pattern; use action sheets instead)

### Specs
| Property | Value |
|----------|-------|
| FAB size | 56dp (standard) or 40dp (mini) |
| Speed dial items | 3-6 items |
| Item size | 40dp mini FABs |
| Item spacing | 16dp vertical gap |
| Labels | Required — show text label to the left of each mini FAB |
| Backdrop | Semi-transparent scrim behind expanded menu |
| Animation | Staggered entrance: 50ms delay between each item, 200ms total |
| Close | Tap scrim, tap FAB again, or Escape key |
| Position | 16dp from bottom and right edges |

---

## 19. Table of Contents

A structured outline of a page's sections, typically displayed as a sidebar or collapsible panel, allowing users to jump to specific sections.

### When to Use
- Long-form articles (3000+ words)
- Documentation pages with multiple sections
- Legal documents, terms of service, privacy policies
- Academic papers or reports

### When NOT to Use
- Short content that fits on one screen
- Pages with fewer than 3 sections
- Highly visual pages where section headings are not meaningful

### Specs
| Property | Value |
|----------|-------|
| Generated from | H2 and H3 headings in the content |
| Position | Right sidebar (desktop) or collapsible top panel (mobile) |
| Sticky | Yes, below primary nav |
| Active highlighting | Current section highlighted via scroll spy |
| Nesting | Show H2 as top-level, H3 as indented children |
| Collapse | Mobile: collapsed by default with "On this page" toggle |

### Reference Implementations
- Notion.com — Auto-generated table of contents block
- GitHub — README table of contents
- Docusaurus — Right sidebar TOC with scroll spy

---

## 20. In-Page Section Tabs

Tabs that switch between content sections within a larger page, rather than at the page level. Often used within cards, panels, or specific sections of a page.

### When to Use
- Product detail pages (Description | Specs | Reviews)
- Dashboard widgets (Chart | Table | Raw Data)
- User profiles (Posts | Followers | Following)
- Settings within a settings category (General | Advanced | Integrations)

### Specs
Same as primary horizontal tabs but scoped to a section of the page rather than the full page. Ensure these are visually distinct from any page-level tab navigation to avoid confusion.

---

## 21. Quick Links / Jump Bar

An alphabetical or categorical bar that allows users to jump directly to a section of a long alphabetical or categorized list. Common in contact lists, glossaries, and directory pages.

### When to Use
- Contact lists (jump to letter)
- Glossaries or dictionaries
- Country/state selection lists
- Any long alphabetical or categorized directory

### Specs
| Property | Value |
|----------|-------|
| Layout | Horizontal bar (A B C ... Z) or vertical strip (mobile contact list) |
| Active state | Highlight current letter/section |
| Disabled state | Gray out letters with no entries |
| Touch target | 28-36px per letter (horizontal), 20-24px (vertical strip) |
| Scroll behavior | Instant jump (no smooth scroll for alphabetical lists) |

---

## 22. Contextual Action Bar

A bar that appears when one or more items are selected in a list, replacing or overlaying the normal header/toolbar. Shows actions relevant to the selection (delete, move, archive, export).

### When to Use
- Email clients (select messages, then bulk actions)
- File managers (select files, then copy/move/delete)
- Data tables with row selection
- Photo galleries with multi-select

### When NOT to Use
- Single-item actions (use an action menu on the item)
- When selection mode is not supported
- When there is only one possible action (just show a button on each item)

### Specs
| Property | Value |
|----------|-------|
| Trigger | Appears when 1+ items are selected |
| Position | Replaces or overlays the list header/toolbar |
| Content | Selection count + action buttons (Delete, Archive, Move, etc.) |
| Close | Deselect all (X button) or complete an action |
| Background | Distinct color (often primary/accent) to indicate mode change |
| Animation | Slide down from top or fade in, 200ms |
| Mobile | Full-width bar at bottom (thumb zone) |

### CSS Specs
```css
.action-bar {
  display: flex;
  align-items: center;
  gap: 16px;
  height: 56px;
  padding: 0 24px;
  background: #2563eb;
  color: #ffffff;
  border-radius: 8px;
  animation: slideDown 200ms ease-out;
}

@keyframes slideDown {
  from {
    transform: translateY(-100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.action-bar__count {
  font-size: 14px;
  font-weight: 600;
}

.action-bar__actions {
  display: flex;
  gap: 8px;
  margin-left: auto;
}

.action-bar__button {
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 500;
  background: rgba(255, 255, 255, 0.15);
  border: none;
  border-radius: 6px;
  color: #ffffff;
  cursor: pointer;
}

.action-bar__button:hover {
  background: rgba(255, 255, 255, 0.25);
}

.action-bar__close {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
  border-radius: 50%;
}

.action-bar__close:hover {
  background: rgba(255, 255, 255, 0.15);
}
```

### Reference Implementations
- Gmail — Select messages, action bar appears
- Google Drive — File selection action bar
- Notion — Multi-block selection toolbar

---

## Pattern Selection Guide: Secondary Navigation

| Scenario | Recommended Pattern |
|----------|-------------------|
| User needs to see their position in hierarchy | Breadcrumbs |
| Section has 3-7 subsections | Sub-navigation bar |
| Long page with multiple sections | Anchor nav + scroll spy |
| Sequential content reading | Prev/Next pagination |
| Large dataset with known page count | Numbered pagination |
| Browsable content feed | Load more or infinite scroll |
| Multi-step form or process | Stepper navigation |
| Switching view modes (2-4 options) | Segmented control |
| Filtering list by category | Filter tabs |
| Detail page opened from list | Back link |
| Article with related content | Related content links |
| Mobile quick actions (3-6) | FAB + speed dial |
| Long document with sections | Table of contents |
| Alphabetical directory | Quick links / jump bar |
| Bulk operations on selected items | Contextual action bar |
