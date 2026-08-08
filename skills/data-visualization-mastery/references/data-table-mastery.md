# Data Table Mastery

> Complete data table design system: anatomy, 15+ column types, sorting, filtering, pagination, selection, expansion, fixed headers, inline editing, cell formatting, empty/loading states, responsive strategies, density modes, accessibility spec, and production React/TypeScript code.

---

## 1. Table Anatomy

```
+------------------------------------------------------------------------+
|  [x] Select All  |  Name ^v  |  Status  |  Revenue ^  |  Actions     | <- Header row
+------------------------------------------------------------------------+
|  [ ]  Acme Corp  |  Active   |  $1.2M   |  ...  Edit  |              | <- Data row
|  [ ]  Beta Inc   |  Pending  |  $890K   |  ...  Edit  |              |
|  [x]  Gamma LLC  |  Active   |  $2.1M   |  ...  Edit  |              | <- Selected row
+------------------------------------------------------------------------+
|  Showing 1-25 of 342  |   < 1 2 3 ... 14 >  |  25 / page |           | <- Footer / Pagination
+------------------------------------------------------------------------+
```

### Structural Elements

| Element | Purpose | HTML Role |
|---------|---------|-----------|
| **Table container** | Scrollable wrapper | `<div role="grid">` or `<table>` |
| **Header row** | Column labels, sort controls | `<thead>` / `role="columnheader"` |
| **Data row** | One record per row | `<tr>` / `role="row"` |
| **Cell** | Individual data point | `<td>` / `role="gridcell"` |
| **Footer row** | Pagination, summary, bulk actions | `<tfoot>` or separate div |
| **Toolbar** | Search, filters, export, bulk actions | Above the table |

---

## 2. Column Types

### 2.1 Text Column

```css
.col-text {
  text-align: left;
  font-size: 14px;
  color: #111827;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 240px;
}
```

**Rules:** Left-aligned. Truncate with ellipsis at max-width. Show full text on hover (tooltip). Primary text column (e.g., Name) is bold (font-weight 600) and may be a clickable link.

### 2.2 Number Column

```css
.col-number {
  text-align: right;
  font-variant-numeric: tabular-nums;
  font-feature-settings: "tnum" 1;
  font-size: 14px;
  color: #111827;
}

.col-number-header {
  text-align: right;
}
```

**Rules:** Right-aligned (both header and cells). Tabular figures always. Comma-separate thousands. Use abbreviations for large numbers (1.2M) or full format ($1,234,567) based on column width.

### 2.3 Currency Column

```css
.col-currency {
  text-align: right;
  font-variant-numeric: tabular-nums;
  font-feature-settings: "tnum" 1;
}

.col-currency-negative {
  color: #dc2626;
}
```

**Rules:** Right-aligned. Currency symbol + formatted number. Negative values in red or parentheses. Consistent decimal places within a column (all 2 decimals, or all abbreviated).

### 2.4 Percentage Column

```css
.col-percentage {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
```

**Rules:** Right-aligned. 1 decimal max. % symbol after number. Optional: inline micro-bar showing the percentage visually.

### 2.5 Date Column

```css
.col-date {
  text-align: left;
  font-variant-numeric: tabular-nums;
  color: #6b7280;
  font-size: 13px;
}
```

**Rules:** Consistent format throughout the table. Use relative dates for recent items ("2 hours ago", "Yesterday") and absolute dates for older items (Mar 12, 2026). Sort by actual date value, not display string.

### 2.6 Status/Badge Column

```css
.col-status {
  text-align: left;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 2px 10px;
  font-size: 12px;
  font-weight: 500;
  border-radius: 99px;
}

.status-active   { background: #dcfce7; color: #166534; }
.status-pending  { background: #fef3c7; color: #92400e; }
.status-inactive { background: #f3f4f6; color: #6b7280; }
.status-error    { background: #fef2f2; color: #991b1b; }
```

**Rules:** Colored pill badges. Dot indicator (8px circle) before text. Color coding with text label (never color alone). Max 5-6 distinct statuses.

### 2.7 Avatar + Name Column

```css
.col-user {
  display: flex;
  align-items: center;
  gap: 10px;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  flex-shrink: 0;
  object-fit: cover;
}

.avatar-fallback {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #dbeafe;
  color: #1d4ed8;
  font-size: 13px;
  font-weight: 600;
}

.user-name {
  font-weight: 500;
  color: #111827;
}

.user-email {
  font-size: 12px;
  color: #6b7280;
}
```

**Rules:** 32px circular avatar + name + optional secondary text (email, role). Fallback: initials on colored background.

### 2.8 Checkbox Column (Selection)

```css
.col-checkbox {
  width: 44px;
  text-align: center;
  padding: 0 12px;
}

.col-checkbox input[type="checkbox"] {
  width: 16px;
  height: 16px;
  accent-color: #2563eb;
  cursor: pointer;
}
```

**Rules:** First column, fixed width (44px). Header checkbox: select all / deselect all. Indeterminate state when some rows selected. Selected row gets highlighted background (#eff6ff).

### 2.9 Action Column

```css
.col-actions {
  text-align: right;
  white-space: nowrap;
}

.action-button {
  padding: 6px 10px;
  font-size: 13px;
  font-weight: 500;
  color: #2563eb;
  background: transparent;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.action-button:hover {
  background: #eff6ff;
}

.action-menu-trigger {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  color: #6b7280;
}

.action-menu-trigger:hover {
  background: #f3f4f6;
  color: #111827;
}
```

**Rules:** Last column, right-aligned. 1-2 inline action buttons (Edit, View) + overflow menu (three dots) for more actions. On mobile, show only the overflow menu.

### 2.10 Link Column

```css
.col-link a {
  color: #2563eb;
  text-decoration: none;
  font-weight: 500;
}

.col-link a:hover {
  text-decoration: underline;
}
```

**Rules:** Blue text, underline on hover. Opens in same tab (internal) or new tab (external, with icon indicator).

### 2.11 Progress Column

```css
.col-progress {
  min-width: 120px;
}

.progress-bar-track {
  height: 6px;
  background: #e5e7eb;
  border-radius: 99px;
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  border-radius: 99px;
  transition: width 300ms ease;
}

.progress-label {
  font-size: 12px;
  color: #6b7280;
  margin-top: 2px;
}
```

**Rules:** Mini progress bar + percentage label. Color: blue (in progress), green (complete), gray (not started), red (behind schedule).

### 2.12 Sparkline Column

```css
.col-sparkline {
  width: 100px;
  height: 24px;
}

.col-sparkline svg {
  width: 100%;
  height: 100%;
}
```

**Rules:** Tiny inline chart showing 7-30 day trend. No axes or labels. Single color line. Hover: tooltip with value and date.

### 2.13 Tag Column (Multi-value)

```css
.col-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 4px;
}

.tag {
  display: inline-block;
  padding: 2px 8px;
  font-size: 11px;
  font-weight: 500;
  background: #f3f4f6;
  color: #374151;
  border-radius: 4px;
}
```

**Rules:** Multiple tags per cell. Show first 2-3, then "+N more" chip. Full list on hover or expand.

### 2.14 Boolean/Toggle Column

```css
.col-toggle {
  text-align: center;
  width: 60px;
}
```

**Rules:** Toggle switch or checkmark icon. Green checkmark for true, empty or gray dash for false. If editable: toggle switch inline.

### 2.15 Rating Column

```css
.col-rating {
  display: flex;
  gap: 2px;
}

.rating-star {
  width: 14px;
  height: 14px;
  color: #f59e0b;
}

.rating-star.empty {
  color: #d1d5db;
}
```

**Rules:** Star icons (filled/empty). 5-star scale. Show numeric value beside stars for accessibility.

---

## 3. Sorting

### 3.1 Single Column Sort

```css
.sort-trigger {
  cursor: pointer;
  user-select: none;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.sort-icon {
  width: 12px;
  height: 12px;
  color: #9ca3af;
  transition: transform 150ms ease;
}

.sort-icon.asc  { color: #111827; }
.sort-icon.desc { color: #111827; transform: rotate(180deg); }
```

**Behavior:**
1. Click header: sort ascending
2. Click again: sort descending
3. Click again: remove sort (return to default order)
4. Only one column sorted at a time (unless multi-sort)

**Visual:** Arrow icon in header. Gray when unsorted, dark when active. Up arrow = ascending, down arrow = descending.

### 3.2 Multi-Column Sort

**Behavior:** Hold Shift + click to add secondary sort. Show sort priority numbers (1, 2, 3) in header badges.
**Use when:** Analyst-facing tables where complex sorting is needed.

### 3.3 Default Sort

- **Names:** Alphabetical ascending
- **Dates:** Most recent first (descending)
- **Numbers/Currency:** Highest first (descending)
- **Status:** Custom order (Active > Pending > Inactive > Error)

---

## 4. Filtering

### 4.1 Global Search

```css
.table-search {
  position: relative;
  width: 280px;
}

.table-search input {
  width: 100%;
  padding: 8px 12px 8px 36px;
  font-size: 14px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  background: white;
}

.table-search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  color: #9ca3af;
}
```

**Behavior:** Search across all text columns. Debounce 300ms. Highlight matching text in cells. Show "No results" empty state.

### 4.2 Column Filters

**Types:**
- **Text column:** Contains / starts with / equals text input
- **Number column:** Greater than / less than / between range inputs
- **Date column:** Date range picker (from/to)
- **Status column:** Multi-select checkboxes
- **Boolean column:** True / False / All toggle

**Trigger:** Filter icon in each column header. Click to open filter popover below the header.

### 4.3 Faceted Filters (Sidebar)

```css
.table-filters-sidebar {
  width: 240px;
  padding: 16px;
  border-right: 1px solid #e5e7eb;
}

.filter-section {
  margin-bottom: 20px;
}

.filter-section-title {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #6b7280;
  margin-bottom: 8px;
}
```

**Layout:** Left sidebar with stacked filter sections. Checkbox lists for categories, range sliders for numbers, date pickers for dates. Show count of matching items per option.

### 4.4 Active Filter Display

```css
.active-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 8px 0;
}

.active-filter-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  font-size: 13px;
  background: #eff6ff;
  color: #1d4ed8;
  border-radius: 6px;
}

.active-filter-remove {
  width: 14px;
  height: 14px;
  cursor: pointer;
  opacity: 0.6;
}

.active-filter-remove:hover {
  opacity: 1;
}

.active-filters-clear {
  font-size: 13px;
  color: #6b7280;
  cursor: pointer;
  text-decoration: underline;
}
```

**Layout:** Row of chips above the table showing active filters. Each chip shows the filter column + value + remove button. "Clear all" link at the end.

---

## 5. Pagination

### 5.1 Numbered Pagination

```css
.pagination {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 0;
}

.pagination-info {
  font-size: 13px;
  color: #6b7280;
}

.pagination-controls {
  display: flex;
  align-items: center;
  gap: 4px;
}

.pagination-button {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 500;
  color: #374151;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  background: white;
  cursor: pointer;
}

.pagination-button.active {
  background: #2563eb;
  color: white;
  border-color: #2563eb;
}

.pagination-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-page-size {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: #6b7280;
}
```

**Layout:** Left: "Showing 1-25 of 342 results". Center: page number buttons (1, 2, 3, ..., 14) with prev/next arrows. Right: page size selector (10, 25, 50, 100).
**Pattern:** Show first, last, current, and 1-2 pages around current. Ellipsis (...) for gaps.

### 5.2 Load More Button

```css
.load-more {
  display: flex;
  justify-content: center;
  padding: 16px 0;
}

.load-more-button {
  padding: 8px 24px;
  font-size: 14px;
  font-weight: 500;
  color: #2563eb;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  cursor: pointer;
}
```

**Layout:** "Load more" button below the table. Shows count: "Load 25 more (showing 50 of 342)".
**Use when:** Casual browsing, less formal than numbered pagination.

### 5.3 Infinite Scroll

**Behavior:** Automatically load more rows as the user scrolls near the bottom of the table. Show a loading spinner at the bottom while fetching.
**Use when:** Feeds, activity logs, chat-like lists. NOT for data analysis (users lose position).

### 5.4 Cursor-Based Pagination

**Use when:** Large datasets with real-time updates. API returns a cursor token, not page numbers.
**UI:** Simpler prev/next buttons without page numbers. "Load newer" / "Load older" semantics.

---

## 6. Row Selection

### 6.1 Single Selection

```css
.row-selectable {
  cursor: pointer;
}

.row-selectable:hover {
  background: #f9fafb;
}

.row-selected {
  background: #eff6ff;
}
```

**Behavior:** Click a row to select it (highlights). Only one row selected at a time. Useful for master-detail views (selecting a row updates a detail panel).

### 6.2 Multi-Selection

**Behavior:**
- Click checkbox: toggle individual row
- Click header checkbox: select/deselect all visible rows
- Shift + click: range select (from last clicked to current)
- Header checkbox shows indeterminate state when some rows selected

### 6.3 Bulk Actions Toolbar

```css
.bulk-actions-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 16px;
  background: #eff6ff;
  border-radius: 8px;
  margin-bottom: 8px;
  animation: slideDown 150ms ease;
}

.bulk-actions-count {
  font-size: 14px;
  font-weight: 600;
  color: #1d4ed8;
}

.bulk-action-button {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: 500;
  border: 1px solid #93c5fd;
  border-radius: 6px;
  background: white;
  color: #1d4ed8;
  cursor: pointer;
}

.bulk-action-button.destructive {
  color: #dc2626;
  border-color: #fca5a5;
}
```

**Layout:** Appears above the table when rows are selected. Shows: "[N] selected" + action buttons (Export, Delete, Archive, Assign). Disappears when selection is cleared.

---

## 7. Row Expansion

### 7.1 Expandable Detail Row

```css
.expand-trigger {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-radius: 4px;
}

.expand-trigger:hover {
  background: #f3f4f6;
}

.expand-icon {
  width: 16px;
  height: 16px;
  transition: transform 150ms ease;
}

.expand-icon.expanded {
  transform: rotate(90deg);
}

.row-detail {
  background: #f9fafb;
  padding: 16px 20px 16px 60px;
  border-bottom: 1px solid #e5e7eb;
}
```

**Behavior:** Chevron in first column. Click to expand a detail row below the main row. Detail row spans full table width and shows additional information (sub-table, description, metadata).

### 7.2 Nested Table

**Layout:** Expanded row contains a child table (sub-rows). E.g., order row expands to show line items. Indent child table 40-60px from left.

---

## 8. Fixed Headers and Columns

### 8.1 Sticky Header

```css
.table-container {
  max-height: 600px;
  overflow-y: auto;
}

.table-header {
  position: sticky;
  top: 0;
  z-index: 10;
  background: white;
  border-bottom: 2px solid #e5e7eb;
}
```

**Rules:** Header stays visible when scrolling vertically. Shadow appears on header when scrolled to indicate scrollable content.

### 8.2 Sticky First Column

```css
.col-sticky {
  position: sticky;
  left: 0;
  z-index: 5;
  background: white;
  border-right: 1px solid #e5e7eb;
}

.col-sticky::after {
  content: '';
  position: absolute;
  top: 0;
  right: -8px;
  bottom: 0;
  width: 8px;
  background: linear-gradient(90deg, rgba(0,0,0,0.06), transparent);
  pointer-events: none;
}
```

**Rules:** First column (usually checkbox + name) stays visible when scrolling horizontally. Shadow on the right edge of the sticky column.

---

## 9. Column Resizing and Reordering

### 9.1 Column Resizing

```css
.resize-handle {
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  cursor: col-resize;
  background: transparent;
}

.resize-handle:hover,
.resize-handle.active {
  background: #2563eb;
}
```

**Behavior:** Drag the right edge of a column header to resize. Minimum column width: 60px. Double-click resize handle: auto-fit to content width.

### 9.2 Column Reordering

**Behavior:** Drag column header to reorder. Ghost preview shows where the column will land. Drop zone indicators between columns.

### 9.3 Column Visibility Toggle

**UI:** Menu (accessed via a "Columns" button in the toolbar) with checkboxes for each column. Toggle columns on/off. Persist user preferences.

---

## 10. Inline Editing

```css
.cell-editable:hover {
  outline: 1px dashed #d1d5db;
  outline-offset: -1px;
  cursor: text;
}

.cell-editing {
  outline: 2px solid #2563eb;
  outline-offset: -2px;
  background: white;
}

.cell-editing input {
  width: 100%;
  padding: 4px 8px;
  font-size: inherit;
  border: none;
  outline: none;
  background: transparent;
}
```

**Behavior:**
1. Click a cell to enter edit mode
2. Cell becomes an input field
3. Tab to move to next editable cell
4. Enter to confirm, Escape to cancel
5. Show unsaved indicator (colored dot) until saved
6. Validate on blur

**Rules:** Not all columns should be editable. Primary key columns (ID, name) may be read-only. Show edit icon on hover for editable cells.

---

## 11. Cell Formatting

### 11.1 Number Formatting

```typescript
function formatNumber(value: number, type: string): string {
  switch (type) {
    case 'currency':
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0,
      }).format(value);
    case 'currency-precise':
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
      }).format(value);
    case 'compact':
      return new Intl.NumberFormat('en-US', {
        notation: 'compact',
        maximumFractionDigits: 1,
      }).format(value);
    case 'percent':
      return new Intl.NumberFormat('en-US', {
        style: 'percent',
        minimumFractionDigits: 1,
        maximumFractionDigits: 1,
      }).format(value / 100);
    default:
      return new Intl.NumberFormat('en-US').format(value);
  }
}
```

### 11.2 Date Formatting

```typescript
function formatDate(date: Date, style: string): string {
  const now = new Date();
  const diffMs = now.getTime() - date.getTime();
  const diffHours = diffMs / (1000 * 60 * 60);
  const diffDays = diffMs / (1000 * 60 * 60 * 24);

  if (style === 'relative') {
    if (diffHours < 1) return 'Just now';
    if (diffHours < 24) return `${Math.floor(diffHours)}h ago`;
    if (diffDays < 2) return 'Yesterday';
    if (diffDays < 7) return `${Math.floor(diffDays)}d ago`;
  }

  return new Intl.DateTimeFormat('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  }).format(date);
}
```

### 11.3 Text Truncation

```css
.cell-truncate {
  max-width: 200px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Tooltip on hover showing full text */
.cell-truncate[title] {
  cursor: help;
}
```

---

## 12. Empty and Loading States

### 12.1 Table Loading (Skeleton)

```css
.table-skeleton-row {
  display: grid;
  grid-template-columns: 44px 2fr 1fr 1fr 1fr 80px;
  gap: 16px;
  padding: 12px 16px;
  border-bottom: 1px solid #f3f4f6;
}

.skeleton-cell {
  height: 16px;
  border-radius: 4px;
  background: linear-gradient(90deg, #f3f4f6 25%, #e5e7eb 50%, #f3f4f6 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
}

@keyframes shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

**Behavior:** Show 5-10 skeleton rows matching the table column layout. Keep the header visible (not skeleton). Skeleton cells vary in width to look natural.

### 12.2 Table Empty State

```css
.table-empty {
  text-align: center;
  padding: 60px 40px;
}

.table-empty-icon {
  width: 48px;
  height: 48px;
  color: #d1d5db;
  margin: 0 auto 16px;
}

.table-empty-title {
  font-size: 16px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 4px;
}

.table-empty-description {
  font-size: 14px;
  color: #9ca3af;
  margin-bottom: 16px;
  max-width: 320px;
  margin-left: auto;
  margin-right: auto;
}

.table-empty-action {
  padding: 8px 16px;
  font-size: 14px;
  font-weight: 500;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
```

**Content variations:**
- No data at all: "No [items] yet. Create your first [item]." + CTA button
- No results for filters: "No results match your filters. Try adjusting your search or filters." + "Clear filters" button
- No results for search: "No results for '[query]'. Try a different search term."

### 12.3 Table Error State

**Content:** "Unable to load data. Please try again." + "Retry" button. Red-tinted background.

---

## 13. Responsive Table Strategies

### 13.1 Horizontal Scroll

```css
.table-scroll-container {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.table-scroll-container table {
  min-width: 800px;
}
```

**When to use:** Tables with many columns that cannot be hidden. Power user tools.
**Enhancement:** Fade gradient on the right edge to indicate scrollable content. Sticky first column.

### 13.2 Column Priority Hiding

```css
@media (max-width: 1024px) {
  .col-priority-low { display: none; }
}

@media (max-width: 768px) {
  .col-priority-medium { display: none; }
}
```

**When to use:** Standard approach. Assign priority (critical, high, medium, low) to each column. Hide lowest priority columns first as viewport narrows.

### 13.3 Card View (Mobile)

```css
@media (max-width: 640px) {
  .table-responsive table,
  .table-responsive thead,
  .table-responsive tbody,
  .table-responsive tr,
  .table-responsive td {
    display: block;
  }

  .table-responsive thead { display: none; }

  .table-responsive tr {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 8px;
  }

  .table-responsive td {
    display: flex;
    justify-content: space-between;
    padding: 4px 0;
    border: none;
  }

  .table-responsive td::before {
    content: attr(data-label);
    font-weight: 600;
    font-size: 12px;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }
}
```

**When to use:** Mobile views where each row becomes a card. Each cell shows its label (from `data-label` attribute) on the left and value on the right.

### 13.4 Stacked Layout

**Layout:** On mobile, key columns remain as the "card header" and secondary columns stack below in a key-value pair format.

---

## 14. Density Modes

```css
/* Compact -- for data-dense views, power users */
.table-compact td {
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.3;
}

.table-compact .avatar { width: 24px; height: 24px; }

/* Comfortable -- default */
.table-comfortable td {
  padding: 10px 16px;
  font-size: 14px;
  line-height: 1.5;
}

.table-comfortable .avatar { width: 32px; height: 32px; }

/* Spacious -- for casual browsing, less data */
.table-spacious td {
  padding: 14px 16px;
  font-size: 14px;
  line-height: 1.6;
}

.table-spacious .avatar { width: 40px; height: 40px; }
```

**Density selector:** Three-button toggle in the toolbar (compact / comfortable / spacious icons).

| Mode | Row Height | Font Size | Use For |
|------|-----------|-----------|---------|
| Compact | ~36px | 13px | Power users, trading, monitoring, many rows |
| Comfortable | ~48px | 14px | Default, most applications |
| Spacious | ~56px | 14px | Casual browsing, content-focused tables |

---

## 15. Accessibility

### 15.1 Semantic HTML

```html
<div role="grid" aria-label="Customer data table" aria-rowcount="342">
  <div role="row" aria-rowindex="1">
    <div role="columnheader" aria-sort="ascending">Name</div>
    <div role="columnheader" aria-sort="none">Status</div>
    <div role="columnheader" aria-sort="none">Revenue</div>
  </div>
  <div role="row" aria-rowindex="2" aria-selected="false">
    <div role="gridcell">Acme Corp</div>
    <div role="gridcell">Active</div>
    <div role="gridcell">$1,200,000</div>
  </div>
</div>
```

### 15.2 ARIA Attributes

| Attribute | Where | Purpose |
|-----------|-------|---------|
| `role="grid"` | Table container | Identifies as interactive grid |
| `role="row"` | Each row | Identifies row |
| `role="columnheader"` | Header cells | Identifies column header |
| `role="gridcell"` | Data cells | Identifies data cell |
| `aria-sort="ascending"` | Sorted header | Announces sort direction |
| `aria-sort="descending"` | Sorted header | Announces sort direction |
| `aria-sort="none"` | Unsorted header | Announces no sort |
| `aria-rowcount` | Grid | Total row count (including off-screen) |
| `aria-rowindex` | Each row | Row position in full dataset |
| `aria-selected` | Selectable rows | Selection state |
| `aria-label` | Grid | Table purpose description |
| `aria-describedby` | Grid | ID of description element |

### 15.3 Keyboard Navigation

| Key | Action |
|-----|--------|
| **Tab** | Move focus to the table, then to next focusable element after table |
| **Arrow keys** | Navigate between cells (up, down, left, right) |
| **Home** | Move to first cell in current row |
| **End** | Move to last cell in current row |
| **Ctrl+Home** | Move to first cell in first row |
| **Ctrl+End** | Move to last cell in last row |
| **Space** | Toggle selection of current row (if selectable) |
| **Enter** | Activate link or button in current cell, or enter edit mode |
| **Escape** | Exit edit mode, cancel current action |
| **Page Up/Down** | Scroll one page of rows |

### 15.4 Focus Management

```css
.table-cell:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: -2px;
  border-radius: 2px;
}

.table-row:focus-within {
  background: #f9fafb;
}
```

**Rules:** Single tab stop for the entire table (roving tabindex). Arrow keys navigate between cells. Focus ring visible on the active cell. Screen reader announces cell content, column header, and row context.

---

## 16. Production React Component

```tsx
interface Column<T> {
  key: keyof T;
  header: string;
  type: 'text' | 'number' | 'currency' | 'date' | 'status' | 'actions';
  align?: 'left' | 'center' | 'right';
  width?: string;
  sortable?: boolean;
  priority?: 'critical' | 'high' | 'medium' | 'low';
  render?: (value: T[keyof T], row: T) => React.ReactNode;
}

interface DataTableProps<T> {
  columns: Column<T>[];
  data: T[];
  loading?: boolean;
  error?: string;
  emptyTitle?: string;
  emptyDescription?: string;
  sortColumn?: keyof T;
  sortDirection?: 'asc' | 'desc';
  onSort?: (column: keyof T) => void;
  selectable?: boolean;
  selectedRows?: Set<string>;
  onSelectionChange?: (selected: Set<string>) => void;
  getRowId: (row: T) => string;
  pagination?: {
    page: number;
    pageSize: number;
    total: number;
    onPageChange: (page: number) => void;
    onPageSizeChange: (size: number) => void;
  };
  density?: 'compact' | 'comfortable' | 'spacious';
}
```

This interface defines a production-ready data table component. Implementation should include:
1. Virtualized rendering for large datasets (react-virtual or tanstack/react-table)
2. Keyboard navigation (roving tabindex pattern)
3. Column resize handles
4. Sticky header and optional sticky first column
5. Responsive behavior (column hiding at breakpoints)
6. Loading skeleton, empty state, and error state
7. Sort, filter, and pagination controlled by parent component
8. Selection management with bulk actions
9. Cell formatting using Intl APIs
10. Print stylesheet that removes interactive elements

---

## 17. Table Design Checklist

### Visual
- [ ] Header row visually distinct from data rows (bold, uppercase, separator)
- [ ] Alternating row stripes OR horizontal dividers (not both)
- [ ] Numbers right-aligned with tabular figures
- [ ] Text left-aligned
- [ ] Consistent column widths (no random sizing)
- [ ] Adequate cell padding (not cramped, not wasteful)
- [ ] Truncated text has tooltip
- [ ] Status badges use color + text (not color alone)

### Interaction
- [ ] Sortable columns have clear affordance (icon)
- [ ] Active sort direction is visible
- [ ] Search debounce >= 300ms
- [ ] Active filters shown as chips with remove option
- [ ] Pagination shows total count and current range
- [ ] Selected rows are visually highlighted
- [ ] Bulk actions appear when rows are selected
- [ ] Expandable rows have clear expand/collapse affordance

### Accessibility
- [ ] Proper `role="grid"` with `aria-label`
- [ ] `aria-sort` on sortable column headers
- [ ] Keyboard navigation works (arrow keys between cells)
- [ ] Focus ring visible on active cell
- [ ] Screen reader announces column header with cell content
- [ ] Selection state announced via `aria-selected`

### States
- [ ] Loading: skeleton matching table structure
- [ ] Empty: clear message + CTA
- [ ] Error: message + retry button
- [ ] No search results: suggestion to modify search
- [ ] Partial loading: spinner in footer during pagination

### Responsive
- [ ] Columns hide by priority on narrow viewports
- [ ] Or: horizontal scroll with sticky first column
- [ ] Or: card view on mobile
- [ ] Touch targets >= 44px for interactive elements
- [ ] Action buttons accessible on mobile (not hidden behind hover)
