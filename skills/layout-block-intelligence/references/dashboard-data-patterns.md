# Dashboard & Data Patterns — 50+ Production-Ready Variants

## Dashboard Design Philosophy

Dashboards are the information cockpit of any data-driven application. Unlike marketing pages that tell a story, dashboards must answer questions: "How is my business doing?", "What needs my attention?", "What changed since yesterday?" The best dashboards achieve this in under 5 seconds of looking.

Dashboard blocks have unique constraints: they must handle live data, empty states, loading states, error states, and extreme data ranges. A pricing table always shows 3 cards — a KPI card might show $0 or $10,000,000. A testimonial carousel has 3-5 items — a data table might have 3 or 30,000 rows. This variability makes dashboard blocks the most technically demanding category.

### Dashboard Design Principles
1. **Information density**: Maximize data per pixel without overwhelming. The goal is "dense but clear."
2. **Hierarchy**: Most important metrics at the top. Details below. Actions in context.
3. **Scanability**: Key metrics should be readable in 2-3 seconds of scanning.
4. **Actionability**: Every piece of data should suggest a next action. If it doesn't, consider removing it.
5. **Consistency**: Same metric card style, same chart colors, same interaction patterns throughout.
6. **Real-time awareness**: Show when data was last updated. Indicate stale or loading data clearly.

---

## Dashboard Layout Patterns

### Full-Width Dashboard
- Top: KPI card row (full width)
- Middle: primary chart (full width or 2/3) + secondary widget (1/3)
- Bottom: data table (full width)
- Sidebar: navigation (fixed left)

### Two-Panel Dashboard
- Left panel (60-70%): charts and primary data
- Right panel (30-40%): activity feed, notifications, quick actions
- Top: KPI cards spanning full width

### Grid Dashboard
- 2x2 or 3x2 grid of equal-sized chart/widget blocks
- Each block: self-contained visualization with title
- Drag-and-drop reordering (advanced)
- Responsive: 2 cols at lg, 1 col at md

### Sidebar + Main Content
- Fixed sidebar (240-280px): navigation + filters
- Main area: scrollable dashboard content
- Top bar: fixed header with search + user menu
- Content padding: 24-32px

---

## Dashboard Spacing System

| Element | Spacing |
|---------|---------|
| Page padding | 24-32px |
| Card gap | 16-24px |
| Card padding | 20-24px |
| Chart container padding | 16-24px |
| Section gap (KPIs to charts) | 24-32px |
| Table cell padding | 12px 16px |
| Widget header to content | 16px |

---

## Variant 1: KPI Card Row

3-5 metric cards showing key performance indicators at a glance.

### Layout Specs
- Grid: 3-5 cards in a single row, equal width
- Card height: auto (content-driven), typically 100-120px
- Card padding: 20-24px
- Card border: 1px gray-200, border-radius 12px
- Card background: white
- Content: metric label (13-14px, gray-500, font-weight 500) + value (28-36px, gray-900, font-weight 700) + trend indicator (up/down arrow + percentage, 13px, green-600 or red-600)
- Optional: sparkline (32px height) or progress bar below value
- Gap: 16-24px between cards

### Responsive Behavior
- `xl`+: Single row (3-5 cards)
- `lg`: 3 cards per row (wraps to 2 rows for 5 cards)
- `md`: 2 per row
- `sm`: 1 per row or 2 per row compact

### Production Code (React/TSX)
```tsx
interface KPICard {
  label: string;
  value: string;
  change?: { value: string; positive: boolean };
  icon?: React.ReactNode;
}

export function KPICardRow({ cards }: { cards: KPICard[] }) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-6">
      {cards.map((card, i) => (
        <div key={i} className="rounded-xl bg-white p-5 ring-1 ring-gray-200">
          <div className="flex items-center justify-between">
            <span className="text-sm font-medium text-gray-500">{card.label}</span>
            {card.icon && <span className="text-gray-400">{card.icon}</span>}
          </div>
          <div className="mt-2 flex items-baseline gap-2">
            <span className="text-2xl font-bold text-gray-900">{card.value}</span>
            {card.change && (
              <span className={`text-sm font-medium ${card.change.positive ? 'text-green-600' : 'text-red-600'}`}>
                {card.change.positive ? '+' : ''}{card.change.value}
              </span>
            )}
          </div>
        </div>
      ))}
    </div>
  );
}
```

### States
- **Loading**: Skeleton pulse animation (gray-200 bg, rounded shapes matching content)
- **Error**: Card with error icon + "Failed to load" + retry link
- **Empty**: Show $0 or 0 — never hide the card
- **Stale data**: Show last-updated timestamp, slightly dimmed

---

## Variant 2: KPI Card with Sparkline

Metric card with embedded mini chart showing trend.

### Layout Specs
- Same as KPI Card Row + sparkline below value
- Sparkline: 32-40px height, full card width
- Sparkline colors: single color line (brand or gray), optional gradient fill below
- No axes, no labels on sparkline (too small)
- Data points: 7-30 (daily for month, hourly for day)

### Sparkline Implementation
```tsx
export function Sparkline({ data, color = '#3B82F6', height = 32 }: { data: number[]; color?: string; height?: number }) {
  const max = Math.max(...data);
  const min = Math.min(...data);
  const range = max - min || 1;
  const width = 100;
  const points = data.map((v, i) => `${(i / (data.length - 1)) * width},${height - ((v - min) / range) * height}`).join(' ');

  return (
    <svg viewBox={`0 0 ${width} ${height}`} className="w-full" style={{ height }} preserveAspectRatio="none">
      <polyline fill="none" stroke={color} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" points={points} />
    </svg>
  );
}
```

---

## Variant 3: Chart Container (Line Chart)

Time-series data visualization for trends over time.

### Layout Specs
- Container: white card, border-radius 12px, padding 24px
- Header: title (16-18px bold) + time range selector (buttons or dropdown)
- Chart area: 300-400px height
- X-axis: date/time labels, 12px, gray-500
- Y-axis: value labels, 12px, gray-500
- Grid lines: horizontal only, 1px gray-100
- Line: 2px, brand color, smooth curve (catmull-rom or monotone)
- Tooltip: on hover, show value + date, white card with shadow
- Legend: below chart or top-right, colored circles + labels

### Responsive Behavior
- `xl`+: Full width or 2/3 width, 400px height
- `lg`: Full width, 350px height
- `md`: Full width, 280px height, fewer x-axis labels
- `sm`: Full width, 200px height, minimal labels

### Production Code (Recharts)
```tsx
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

interface ChartData { date: string; value: number }

export function TimeSeriesChart({ data, title }: { data: ChartData[]; title: string }) {
  return (
    <div className="rounded-xl bg-white p-6 ring-1 ring-gray-200">
      <div className="flex items-center justify-between mb-6">
        <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
        <div className="flex gap-1">
          {['7D', '30D', '90D', '1Y'].map((range) => (
            <button key={range} className="px-3 py-1 text-xs font-medium rounded-md text-gray-600 hover:bg-gray-100">{range}</button>
          ))}
        </div>
      </div>
      <ResponsiveContainer width="100%" height={320}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#F3F4F6" vertical={false} />
          <XAxis dataKey="date" tick={{ fontSize: 12 }} stroke="#9CA3AF" tickLine={false} axisLine={false} />
          <YAxis tick={{ fontSize: 12 }} stroke="#9CA3AF" tickLine={false} axisLine={false} width={48} />
          <Tooltip contentStyle={{ borderRadius: 8, border: 'none', boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)' }} />
          <Line type="monotone" dataKey="value" stroke="#3B82F6" strokeWidth={2} dot={false} activeDot={{ r: 4, strokeWidth: 0 }} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
```

---

## Variant 4: Chart Container (Bar Chart)

Categorical comparison data.

### Layout Specs
- Same container as line chart
- Bars: border-radius 4px top, 24-40px width
- Colors: single color for single series, multi-color for comparison
- Horizontal variant: for long category labels
- Stacked variant: for composition data
- Grouped variant: for side-by-side comparison

---

## Variant 5: Chart Container (Pie/Donut)

Proportion display for composition data.

### Layout Specs
- Donut preferred over pie (center space for total/label)
- Donut inner radius: 60-70% of outer radius
- Center label: total value (24-32px bold) + label (14px gray-500)
- Legend: right of chart (desktop) or below (mobile)
- Segments: 3-7 (more than 7 = group into "Other")
- Colors: sequential palette (same hue, different lightness) or categorical
- Hover: segment expands slightly + tooltip

---

## Variant 6: Data Table (Simple)

Rows and columns with sortable headers.

### Layout Specs
- Container: white card or borderless
- Header row: bg-gray-50, 13px uppercase, font-weight 600, gray-500
- Data rows: 14-15px, gray-700, alternating white/gray-50 (optional)
- Row height: 48-56px
- Cell padding: 12px 16px
- Sort indicator: up/down arrow next to sorted column header
- Hover: row bg-gray-50
- Border: 1px gray-200 between rows, or border on container only

### Responsive Behavior
- `xl`+: Full table
- `lg`: Horizontal scroll with sticky first column
- `md`: Card layout (each row becomes a card with label-value pairs)

### Production Code (React/TSX)
```tsx
interface Column<T> { key: keyof T; label: string; sortable?: boolean; align?: 'left' | 'right' }

interface DataTableProps<T> {
  columns: Column<T>[];
  data: T[];
  title?: string;
}

export function DataTable<T extends Record<string, any>>({ columns, data, title }: DataTableProps<T>) {
  return (
    <div className="rounded-xl bg-white ring-1 ring-gray-200 overflow-hidden">
      {title && <div className="px-6 py-4 border-b border-gray-200"><h3 className="text-lg font-semibold text-gray-900">{title}</h3></div>}
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              {columns.map((col) => (
                <th key={String(col.key)} scope="col" className={`px-4 py-3 text-xs font-semibold uppercase tracking-wider text-gray-500 ${col.align === 'right' ? 'text-right' : 'text-left'}`}>
                  {col.label}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {data.map((row, i) => (
              <tr key={i} className="hover:bg-gray-50 transition-colors">
                {columns.map((col) => (
                  <td key={String(col.key)} className={`px-4 py-3 text-sm text-gray-700 whitespace-nowrap ${col.align === 'right' ? 'text-right' : 'text-left'}`}>
                    {String(row[col.key])}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
```

---

## Variant 7: Data Table (Advanced)

Sort + filter + search + pagination for large datasets.

### Layout Specs
- Toolbar above table: search input (left) + filter buttons (center/right) + column toggle
- Search: 40px height input with search icon
- Filters: dropdown buttons or pill toggles
- Pagination: bottom bar with "1-10 of 342" + page buttons
- Bulk actions: checkbox column + action bar on selection
- Row actions: "..." menu or inline action buttons (edit, delete)

### Pagination Specs
- Show: "Showing 1-10 of 342 results"
- Buttons: Previous, page numbers (with ellipsis), Next
- Per-page selector: "10 / 25 / 50 / 100"
- Keyboard: Left/Right arrows for page navigation

---

## Variant 8: Activity Feed

Chronological event list showing recent activity.

### Layout Specs
- Single column, max-width 640px
- Each item: avatar (32-40px) + content (14-15px) + timestamp (13px, gray-500)
- Content: bold actor name + action text + bold object name
- Example: "**Sarah** created a new **Project Alpha** report"
- Timestamp: relative ("2 hours ago") or absolute ("Mar 12, 2:30 PM")
- Connector: vertical line between items (2px, gray-200, left of avatars)
- Load more: button at bottom or infinite scroll

### Production Code
```tsx
interface Activity {
  avatar: string;
  actor: string;
  action: string;
  target: string;
  time: string;
}

export function ActivityFeed({ activities }: { activities: Activity[] }) {
  return (
    <div className="rounded-xl bg-white ring-1 ring-gray-200 p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-6">Recent Activity</h3>
      <div className="space-y-6">
        {activities.map((a, i) => (
          <div key={i} className="flex gap-3">
            <img src={a.avatar} alt={a.actor} className="h-8 w-8 rounded-full flex-shrink-0" />
            <div className="min-w-0">
              <p className="text-sm text-gray-700">
                <span className="font-semibold text-gray-900">{a.actor}</span> {a.action} <span className="font-semibold text-gray-900">{a.target}</span>
              </p>
              <p className="text-xs text-gray-500 mt-0.5">{a.time}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
```

---

## Variant 9: Kanban Board

Column-based task/status board.

### Layout Specs
- Columns: 3-6, horizontal scroll on narrow screens
- Column width: 280-320px
- Column header: status name (16px bold) + card count badge
- Cards: white, rounded-lg, shadow-sm, padding 12-16px
- Card content: title (14px semibold) + description (13px, 1-2 lines) + assignee avatar + priority indicator + due date
- Drag and drop: between columns and within columns
- Add card: "+ Add card" button at column bottom

### Column States
- Default: gray-50 background
- Drag over: blue-50 background, dashed border
- Empty: "No items" message + add button

---

## Variant 10: Calendar View

Month/week/day event display.

### Layout Specs
- Month view: 7-column grid (Sun-Sat), 5-6 rows
- Day cell: date number (14px) + event dots or mini event blocks
- Event block: colored left border (4px) + title (12-13px) + time
- Header: month/year + prev/next arrows + view toggle (month/week/day)
- Today: highlighted cell (blue bg ring or fill)
- Week view: 7 columns, hourly rows (24 or 8-20 for business hours)
- Day view: single column, hourly slots

---

## Variants 11-25: Dashboard Blocks Quick Reference

### 11. Notification List
Unread/read states. Item: icon + title + message + time + read indicator (blue dot). Actions: mark read, dismiss, click to navigate. Unread: bg-blue-50. Badge: count of unread in header.

### 12. List View (Simple)
Single-column list of items. Each row: title + metadata (date, status, author). Click: navigate to detail. Hover: bg-gray-50. Selected: bg-blue-50.

### 13. List View (Detailed)
Multi-field rows with inline data. Columns: thumbnail, title, status badge, date, amount, actions menu. More information density than a card layout, less than a full table.

### 14. Map View
Geographic data on interactive map. Markers: clustered at zoom levels. Click marker: info popup. Sidebar: list of locations with click-to-center. Tools: zoom, search, filter by type. Library: Mapbox GL or Google Maps.

### 15. File/Document Grid
Grid of document thumbnails. Card: thumbnail preview + filename + file type icon + size + date. Actions: download, share, delete (on hover). View toggle: grid / list. Drag-and-drop upload zone.

### 16. User/Member List
Avatar + name + email + role badge + status indicator. Role: colored badge (Admin, Member, Viewer). Status: green dot (online), gray (offline). Actions: edit, remove, change role. Search + role filter above.

### 17. Settings Panel
Grouped form sections. Section: heading + description + form fields. Toggle switches for boolean settings. Save button: sticky bottom or per-section. Changes indicator: "Unsaved changes" warning. Reset: "Restore defaults" link.

### 18. Status Dashboard
System health monitoring. Services: list with green/yellow/red indicators. Uptime: 99.9% with history chart. Incidents: recent incidents list. Response time: line chart. Overall status: large green "All systems operational" banner.

### 19. Progress Tracker
Multi-step with completion state. Steps: completed (green check), current (blue, in progress), upcoming (gray). Progress bar: percentage complete. ETA: estimated completion time. Used for: onboarding, project milestones, data processing.

### 20. Analytics Overview
2x2 or 3x2 grid of chart widgets. Each widget: title + chart + key metric. Time range: shared across all widgets. Export: download button for reports. Widgets: line chart, bar chart, donut, table.

### 21. Heatmap Block
Color-intensity data grid. Axes: categories (x and y). Cell color: intensity scale (light to dark). Tooltip: exact value on hover. Legend: color scale bar. Use for: correlation matrices, time-day activity, geographic density.

### 22. Funnel Chart
Conversion funnel stages. Top-wide to bottom-narrow bars. Labels: stage name + count + conversion rate. Highlight: drop-off between stages. Colors: gradient from stage to stage or single color with opacity.

### 23. Gauge/Meter Block
Single metric with threshold zones. Arc: 180-270 degrees. Zones: green (good), yellow (warning), red (danger). Needle: points to current value. Center: numeric value. Label: metric name below. Size: 160-200px diameter.

### 24. Tree Map Block
Hierarchical data as nested rectangles. Rectangle size: proportional to value. Color: by category. Label: inside rectangle if space allows. Tooltip: full details on hover. Drill-down: click to zoom into category.

### 25. Sankey Diagram Block
Flow data visualization. Nodes: categories (left to right). Links: flows between nodes with width proportional to value. Colors: by source or destination. Hover: highlight connected flows. Use for: user journeys, budget allocation, data flow.

---

## Variants 26-50: Extended Dashboard Patterns

### 26. Alert/Warning Panel
Status alerts requiring attention. Priority levels: critical (red), warning (yellow), info (blue). Each alert: icon + title + description + timestamp + action button. Dismissable. Sticky top or dedicated panel. Badge count on panel trigger.

### 27. Sidebar Widget Stack
Vertical stack of small widgets in a right sidebar (300-360px). Widgets: quick stats, recent activity, upcoming events, shortcuts. Each widget: card with title, compact content. Collapsible: click title to minimize.

### 28. Command Center
Multi-panel real-time monitoring. 4-8 panels in a grid. Each panel: dedicated metric or feed. Real-time updates: WebSocket or polling. Dark theme common. Full-screen mode. Used for: NOC, social media monitoring, trading.

### 29. Report View
Printable/exportable data layout. Header: title + date range + filters applied. Body: charts + tables + text summaries. Footer: page numbers, disclaimers. Export: PDF, CSV, PNG. Print stylesheet: clean, no interactive elements.

### 30. Comparison Dashboard
Period-over-period comparison. Two date ranges selected. Charts: overlay current vs. previous. KPIs: show both values + delta. Table: columns for each period + change column. Color: green for improvement, red for decline.

### 31. Scatter Plot Block
Correlation data display. Axes: two numeric dimensions. Dots: data points, sized by third dimension (optional). Hover: tooltip with details. Trend line: optional linear regression. Quadrants: optional grid dividing into zones.

### 32. Area Chart Block
Filled line chart for volume data. Stacked: for composition over time. Gradient fill: brand color to transparent. Axes: same as line chart. Good for: revenue over time, user growth, cumulative data.

### 33. Combined Chart Block
Multiple chart types overlaid. Example: bar chart + line chart (revenue bars + growth rate line). Two Y-axes: left for bars, right for line. Legend required to distinguish series.

### 34. Search Results Container
Results list with relevance ranking. Each result: title (link) + URL + excerpt with highlighted search terms. Sidebar: filter facets. Top: result count + sort options. Pagination: standard. Loading: skeleton cards.

### 35. Filter Bar (Horizontal)
Horizontal row of filter controls above a data view. Filters: dropdown selects, date pickers, search input, toggle buttons. Active filters: pill badges below bar with X to remove. Clear all: "Reset filters" link. Apply: button or auto-apply on change.

### 36. Empty State (Dashboard)
No data to display. Illustration: simple, relevant to context. Message: explain why empty + what to do next. CTA: "Import data", "Create your first [item]", "Connect your [source]". Don't leave screens blank.

### 37. Skeleton Loading
Placeholder shapes matching content layout. Pulse animation (gray-200 to gray-100). Shapes: rectangles for text, circles for avatars, rounded rectangles for cards. Match exact dimensions of loaded content. Duration: display until data arrives.

### 38. Error State (Dashboard Widget)
Widget showing error instead of data. Icon: warning triangle or X circle. Message: "Failed to load [data type]." Action: "Retry" button. Background: subtle red-50 or neutral gray. Don't show technical error details to users.

### 39. Real-Time Indicator
Shows data is live-updating. Green dot + "Live" label. Pulse animation on the dot. Or: "Last updated 30 seconds ago" with auto-refresh. SSE or WebSocket connection indicator.

### 40. Drag-and-Drop Dashboard Builder
User-configurable dashboard layout. Widget library: sidebar with available widgets. Drop zones: grid cells that accept widgets. Resize handles: drag to resize widget blocks. Save: persist layout to user preferences. Reset: restore default layout.

### 41-45. Chart Variants
41. **Waterfall Chart**: Cumulative positive/negative changes. Used for: financial P&L breakdown.
42. **Radar/Spider Chart**: Multi-dimensional comparison on radial axes. Used for: skill assessments, product comparisons.
43. **Bubble Chart**: Scatter with bubble size as third dimension. Used for: market analysis, portfolio mapping.
44. **Candlestick Chart**: OHLC financial data. Used for: stock/crypto trading.
45. **Histogram**: Frequency distribution bars. Used for: data distribution analysis.

### 46-50. Interactive Dashboard Elements
46. **Date Range Picker**: Calendar dropdown with preset ranges (7D, 30D, 90D, Custom). Used across all charts.
47. **Data Refresh Control**: Manual refresh button + auto-refresh toggle + interval selector.
48. **Chart Zoom**: Brush/zoom on chart area to drill into time range. Reset zoom button.
49. **Data Export Menu**: Download as CSV, Excel, PDF, PNG. Email report option.
50. **Dashboard Sharing**: Share via link, embed code, or scheduled email report.

---

## Dashboard Color System

### Chart Colors (Sequential Palette)
```css
--chart-1: #3B82F6; /* blue-500 */
--chart-2: #10B981; /* emerald-500 */
--chart-3: #F59E0B; /* amber-500 */
--chart-4: #EF4444; /* red-500 */
--chart-5: #8B5CF6; /* violet-500 */
--chart-6: #EC4899; /* pink-500 */
--chart-7: #06B6D4; /* cyan-500 */
--chart-8: #F97316; /* orange-500 */
```

### Status Colors
```css
--status-success: #10B981; /* green */
--status-warning: #F59E0B; /* amber */
--status-error: #EF4444;   /* red */
--status-info: #3B82F6;    /* blue */
--status-neutral: #6B7280; /* gray */
```

### Trend Colors
```css
--trend-up: #10B981;   /* green-500 — positive */
--trend-down: #EF4444; /* red-500 — negative */
--trend-flat: #6B7280; /* gray-500 — neutral */
```

---

## Dashboard Accessibility

1. **Color alone**: Never use color as the only indicator. Pair with icons, patterns, or text labels.
2. **Chart alternatives**: Provide data table view as alternative to every chart (screen reader accessible).
3. **Focus management**: When filtering/sorting data, announce changes to screen readers via live regions.
4. **Keyboard**: All interactive elements (sort, filter, paginate, actions) keyboard-accessible.
5. **ARIA live regions**: For real-time updates, use `aria-live="polite"` to announce data changes.
6. **Contrast**: Chart colors must meet 3:1 contrast against backgrounds. Text labels must meet 4.5:1.
7. **Reduced motion**: Respect `prefers-reduced-motion` — disable chart animations, count-up effects.
8. **Screen reader**: KPI cards should have aria-label summarizing the metric ("Revenue: $45,230, up 12% from last month").
9. **Table structure**: Use proper `<th>` with `scope`, `<caption>`, `aria-sort` for sorted columns.
10. **Chart descriptions**: Provide `aria-label` or linked description summarizing chart data trends.

---

## Dashboard Performance

1. **Virtualization**: For tables with 100+ rows, use virtual scrolling (react-window, tanstack-virtual).
2. **Lazy chart rendering**: Use Intersection Observer to render charts only when scrolled into view.
3. **Data aggregation**: Pre-aggregate data server-side for charts. Don't send raw data to client for aggregation.
4. **WebSocket vs. polling**: For real-time data, WebSocket is more efficient. Polling interval: 15-60 seconds if needed.
5. **Skeleton loading**: Show skeleton immediately, load data async. Never show a blank dashboard.
6. **Cache**: Cache frequently accessed dashboard data. Show cached data immediately, refresh in background.
7. **Responsive images**: Chart images (if using image-based charts) should be responsive SVG, not raster.
8. **Bundle size**: Recharts/D3 are large. Code-split chart libraries. Load only the chart types used.
9. **Memoization**: Memoize chart components to prevent re-renders when parent state changes.
10. **Debounce filters**: Debounce filter inputs (300ms) to prevent excessive API calls while typing.
