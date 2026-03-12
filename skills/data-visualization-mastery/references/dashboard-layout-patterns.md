# Dashboard Layout Patterns

> 30+ dashboard layout patterns with CSS grid definitions, spacing specs, component hierarchy, and responsive collapse strategies. Every pattern is production-ready.

---

## 1. Foundation: Dashboard Anatomy

Every dashboard is composed from these building blocks:

| Block | Purpose | Typical Position |
|-------|---------|-----------------|
| **Header bar** | Title, date range picker, global filters, export button | Top, full width |
| **KPI row** | 3-5 key performance indicators | Below header |
| **Chart grid** | Primary data visualizations | Main content area |
| **Filter panel** | Dimension filters, search | Sidebar or top bar |
| **Detail panel** | Drill-down content, data tables | Below charts or side panel |
| **Footer** | Data source, last updated, help links | Bottom |

### Base Grid CSS

```css
.dashboard {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  gap: 16px;
  max-width: 1440px;
  margin: 0 auto;
  padding: 24px;
}

.dashboard-header  { grid-column: 1 / -1; }
.dashboard-kpi-row { grid-column: 1 / -1; }
.dashboard-main    { grid-column: 1 / -1; }
.dashboard-footer  { grid-column: 1 / -1; }

/* Card base */
.dashboard-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
```

---

## 2. KPI Row Patterns

### 2.1 Basic KPI Row (3-5 cards)

```css
.kpi-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}
```

**Layout:** Equal-width cards in a single row. 3 cards for executive, 4-5 for operational dashboards.
**Responsive:** Wraps to 2 per row on tablet, 1 per row on mobile.

### 2.2 Hero KPI + Supporting KPIs

```css
.kpi-row-hero {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 16px;
}
```

**Layout:** One large KPI card (2x width) with hero styling, followed by 3 smaller supporting KPIs. The hero card has a larger number (48px), sparkline, and richer context.
**Responsive:** Hero goes full width, supporting KPIs stack below in a row of 3, then wrap to single column on mobile.

### 2.3 KPI Row with Mini Charts

```css
.kpi-row-charts {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.kpi-card-with-chart {
  min-height: 160px;
}

.kpi-card-with-chart .kpi-value { font-size: 28px; }
.kpi-card-with-chart .kpi-chart { height: 60px; margin-top: 12px; }
```

**Layout:** Each KPI card contains a sparkline, mini bar chart, or mini area chart below the hero number. Taller cards (160px vs 120px standard).
**Responsive:** 2 per row on tablet, 1 per row on mobile.

### 2.4 KPI Strip (Compact Horizontal)

```css
.kpi-strip {
  display: flex;
  gap: 0;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  overflow: hidden;
}

.kpi-strip-item {
  flex: 1;
  padding: 16px 20px;
  border-right: 1px solid #e5e7eb;
  text-align: center;
}

.kpi-strip-item:last-child { border-right: none; }
```

**Layout:** A single unified bar with KPIs separated by dividers (not individual cards). More compact, less visual weight.
**Responsive:** Wraps to 2-row grid on tablet, vertical stack on mobile.

---

## 3. Chart Grid Patterns

### 3.1 Equal 2-Column Grid

```css
.chart-grid-2col {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.chart-grid-2col .dashboard-card {
  min-height: 320px;
}
```

**Layout:** Two charts side by side, equal width. Simple, balanced.
**Use for:** Comparing two related metrics. Before/after views.
**Responsive:** Single column stack below 768px.

### 3.2 Equal 3-Column Grid

```css
.chart-grid-3col {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.chart-grid-3col .dashboard-card {
  min-height: 280px;
}
```

**Layout:** Three charts in a row. Good for trios of related metrics.
**Responsive:** 2-column + 1-column on tablet, single column on mobile.

### 3.3 2/3 + 1/3 Split

```css
.chart-grid-split {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 16px;
}
```

**Layout:** Large primary chart (66%) + smaller secondary chart or data panel (33%). The primary chart tells the main story; the sidebar provides context or breakdown.
**Use for:** Main trend chart + category breakdown. Map + data list.
**Responsive:** Stack to full width on tablet and mobile.

### 3.4 1/3 + 2/3 Split

```css
.chart-grid-split-reverse {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 16px;
}
```

**Layout:** Filter panel or KPI sidebar (33%) + main chart area (66%).
**Use for:** Filter-driven analysis. Sidebar navigation + chart.
**Responsive:** Sidebar collapses to top filter bar, main chart goes full width.

### 3.5 Mixed Grid (2 + 3 pattern)

```css
.chart-grid-mixed {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 16px;
}

.chart-grid-mixed .card-half  { grid-column: span 3; min-height: 320px; }
.chart-grid-mixed .card-third { grid-column: span 2; min-height: 280px; }
```

**Layout:** Row 1: two half-width charts. Row 2: three third-width charts. Creates visual rhythm and hierarchy -- the top row has the primary story, the bottom row has supporting details.
**Responsive:** Half-width cards stack to full width, third-width cards stack to full width on mobile.

### 3.6 Featured Chart + Grid

```css
.chart-grid-featured {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.chart-featured  { grid-column: 1 / -1; min-height: 400px; }
.chart-secondary { grid-column: span 2; min-height: 280px; }
```

**Layout:** One large featured chart spanning full width, followed by 2-4 smaller charts in a grid below. The featured chart is the hero story of the dashboard.
**Responsive:** All cards go full width, stacked vertically.

### 3.7 Magazine Layout (Asymmetric)

```css
.chart-grid-magazine {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  gap: 16px;
}

.card-wide-left   { grid-column: 1 / 8; grid-row: 1; min-height: 400px; }
.card-narrow-right-top { grid-column: 8 / 13; grid-row: 1; min-height: 190px; }
.card-narrow-right-bot { grid-column: 8 / 13; grid-row: 2; min-height: 190px; }
.card-bottom-left  { grid-column: 1 / 5; min-height: 280px; }
.card-bottom-mid   { grid-column: 5 / 9; min-height: 280px; }
.card-bottom-right  { grid-column: 9 / 13; min-height: 280px; }
```

**Layout:** Asymmetric editorial layout with a large chart on the left, two stacked smaller charts on the right, and three equal charts below. Creates a clear visual hierarchy.
**Responsive:** Collapse to 2-column on tablet, single column on mobile.

---

## 4. Filter Patterns

### 4.1 Top Filter Bar

```css
.filter-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  flex-wrap: wrap;
}

.filter-bar .filter-group {
  display: flex;
  align-items: center;
  gap: 8px;
}

.filter-bar .filter-label {
  font-size: 12px;
  font-weight: 500;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.filter-bar .filter-divider {
  width: 1px;
  height: 24px;
  background: #e5e7eb;
}
```

**Layout:** Horizontal bar above the chart grid. Contains date range picker, dropdowns for dimensions, search, and a reset button.
**Responsive:** Wraps naturally. On mobile, convert to a "Filters" button that opens a bottom sheet.

### 4.2 Sidebar Filters

```css
.dashboard-with-sidebar {
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 16px;
}

.filter-sidebar {
  position: sticky;
  top: 24px;
  max-height: calc(100vh - 48px);
  overflow-y: auto;
  padding: 20px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
}

.filter-sidebar .filter-section {
  margin-bottom: 24px;
}

.filter-sidebar .filter-section-title {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #6b7280;
  margin-bottom: 8px;
}
```

**Layout:** Fixed-width sidebar (240-280px) on the left with stacked filter groups. Main content fills the remaining space.
**Responsive:** Sidebar becomes a collapsible drawer (slide from left) on tablet, or a bottom sheet on mobile.

### 4.3 Segmented Control Tabs

```css
.segment-tabs {
  display: inline-flex;
  background: #f3f4f6;
  border-radius: 8px;
  padding: 4px;
}

.segment-tab {
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 500;
  color: #6b7280;
  border-radius: 6px;
  cursor: pointer;
  transition: all 150ms ease;
}

.segment-tab.active {
  background: white;
  color: #111827;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}
```

**Layout:** Inline segmented control for switching between dashboard views or data slices (Daily / Weekly / Monthly, or by category).
**Responsive:** Scrollable horizontally on mobile if too many tabs.

### 4.4 Chip Filters (Tag-based)

```css
.filter-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.filter-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  font-size: 13px;
  font-weight: 500;
  background: #f3f4f6;
  border-radius: 99px;
  color: #374151;
  cursor: pointer;
}

.filter-chip.active {
  background: #dbeafe;
  color: #1d4ed8;
}

.filter-chip .chip-remove {
  width: 14px;
  height: 14px;
  opacity: 0.5;
}
```

**Layout:** Horizontal row of toggle-able chips. Active chips are highlighted. Each can be toggled on/off or removed.
**Responsive:** Wraps naturally. On mobile, horizontally scrollable or collapsible to "+N more".

---

## 5. Dashboard Type Patterns

### 5.1 Executive Summary Dashboard

**Audience:** C-suite, board, executives.
**Principle:** Glanceable. Single screen. No interaction required.

```
+----------------------------------------------+
|  Header: Company Dashboard  |  Q1 2026  | Export |
+----------------------------------------------+
|  KPI  |  KPI  |  KPI  |  KPI  |  KPI  |
+----------------------------------------------+
|  Revenue Trend (Line)      |  Revenue by     |
|  Full year, monthly        |  Segment (Donut)|
+----------------------------------------------+
|  Top Products (Horiz Bar)  |  Geo Map        |
+----------------------------------------------+
|  Footer: Source, Updated                      |
+----------------------------------------------+
```

**Grid:** KPI row (5 cards) + 2x2 chart grid.
**Charts used:** Line chart, Donut chart, Horizontal bar chart, Choropleth map.
**Data density:** Low (glanceable). 5 KPIs + 4 charts.
**Color:** Minimal -- one accent color, gray for context.
**Responsive:** KPIs wrap to 2 rows, charts stack single column.

### 5.2 Operational Dashboard

**Audience:** Team leads, managers, operations staff.
**Principle:** Real-time or near-real-time. Actionable. Status-oriented.

```
+----------------------------------------------+
|  Header: Operations Monitor  |  Live  | Refresh |
+----------------------------------------------+
|  Active  |  Queue  |  Error   |  Uptime  |
|  Users   |  Size   |  Rate    |  99.97%  |
+----------------------------------------------+
|  Request Volume (Area, 24h)                   |
+----------------------------------------------+
|  Error Log       |  Response Time   |  Status |
|  (Table, latest) |  (Line, 1h)      |  (Grid) |
+----------------------------------------------+
```

**Grid:** KPI strip + featured chart + 3-column grid.
**Charts used:** Area chart (real-time), Line chart, Data table, Status grid.
**Data density:** Medium-high. Auto-refreshing data.
**Special features:** Live indicator, auto-refresh interval, alert badges on KPIs.
**Responsive:** Featured chart stays full width, bottom row stacks.

### 5.3 Analytical Dashboard

**Audience:** Analysts, data scientists, power users.
**Principle:** Interactive exploration. Filter, drill down, compare.

```
+---+------------------------------------------+
| F |  Header + Date Range + Segment Picker     |
| i +------------------------------------------+
| l |  KPI  |  KPI  |  KPI  |  KPI  |         |
| t +------------------------------------------+
| e |  Main Trend (Line, interactive)           |
| r +------------------------------------------+
| s |  Breakdown (Stacked Bar) | Distribution   |
|   |                          | (Histogram)    |
+---+------------------------------------------+
|  Detail Data Table (full width, sortable)     |
+----------------------------------------------+
```

**Grid:** Sidebar filters + KPI row + featured chart + 2-column grid + full-width data table.
**Charts used:** Interactive line chart (brush selection), Stacked bar, Histogram, Data table.
**Data density:** High. Cross-filtering between charts.
**Special features:** Click a bar segment to filter the line chart. Brush-select a time range. Data table updates with filters.
**Responsive:** Sidebar becomes filter button + bottom sheet. Charts stack.

### 5.4 Comparison Dashboard

**Audience:** Analysts comparing entities (products, regions, time periods).
**Principle:** Side-by-side comparison with synchronized axes.

```
+----------------------------------------------+
|  Header  |  Compare: [A] vs [B] vs [C]       |
+----------------------------------------------+
|  Metric 1: Small Multiples (3 line charts)    |
+----------------------------------------------+
|  Metric 2: Grouped Bar Chart                  |
+----------------------------------------------+
|  Metric 3: Radar Chart    |  Summary Table    |
+----------------------------------------------+
```

**Grid:** Full-width small multiples + full-width grouped bar + 2-column bottom row.
**Charts used:** Small multiples (same chart repeated per entity), Grouped bar chart, Radar chart, Summary table.
**Key rule:** All charts share the same scales so comparison is fair.
**Responsive:** Small multiples stack vertically. Grouped bar stays. Bottom row stacks.

### 5.5 Detail / Drill-Down Dashboard

**Audience:** Users who clicked through from a summary dashboard.
**Principle:** Context from parent + deep detail.

```
+----------------------------------------------+
|  <- Back to Summary  |  [Entity Name]         |
+----------------------------------------------+
|  KPI  |  KPI  |  KPI  |  KPI  |              |
+----------------------------------------------+
|  Primary Metric Trend (Line, 12 months)       |
+----------------------------------------------+
|  Breakdown by     |  Breakdown by    |  Map   |
|  Category (Bar)   |  Time (Heatmap)  |        |
+----------------------------------------------+
|  Transaction Detail Table                     |
+----------------------------------------------+
```

**Grid:** Back navigation + KPI row + featured chart + 3-column grid + full-width table.
**Special features:** Breadcrumb or back button. Entity name in header. Table shows individual records.
**Responsive:** Standard collapse behavior.

### 5.6 Real-Time Monitoring Dashboard

**Audience:** NOC, DevOps, security operations.
**Principle:** Always-on display. Dark theme. Status at a glance.

```
+----------------------------------------------+
|  System Status: ALL GREEN  |  Last 4 hours    |
+----------------------------------------------+
|  CPU %  |  Memory  |  Disk  |  Network  |    |
|  Gauge  |  Gauge   |  Gauge |  Gauge    |    |
+----------------------------------------------+
|  Request Rate (Line, streaming)               |
+----------------------------------------------+
|  Error Rate  |  Latency P50/P95  |  Alerts   |
|  (Area)      |  (Line, dual)     |  (List)   |
+----------------------------------------------+
```

**Theme:** Dark background (#111827), bright data colors for visibility at distance.
**Grid:** Status banner + gauge row + streaming chart + 3-column grid.
**Charts used:** Gauges, Streaming line chart, Area chart, Dual-line chart, Alert list.
**Special features:** Auto-refresh every 5-15 seconds. WebSocket for real-time. Alert badges. Sound notifications for critical alerts.
**Responsive:** This dashboard is typically designed for large displays (TV/monitor). Mobile version shows only critical KPIs + alert list.

### 5.7 Financial Dashboard

**Audience:** Finance team, CFO.
**Principle:** Period-over-period comparison. Budget vs actual.

```
+----------------------------------------------+
|  Financial Overview  |  FY2026  |  Q1  | MTD  |
+----------------------------------------------+
|  Revenue |  COGS   |  Gross   |  Net    |    |
|  $12.4M  |  $4.2M  |  Margin  |  Income |    |
|  +8.2%   |  +3.1%  |  66.1%   |  $2.1M  |    |
+----------------------------------------------+
|  Revenue vs Budget (Grouped Bar, monthly)     |
+----------------------------------------------+
|  P&L Waterfall    |  Revenue by Segment       |
|  (Waterfall)      |  (Treemap)                |
+----------------------------------------------+
|  Budget Variance Table (sortable)             |
+----------------------------------------------+
```

**Grid:** Period selector + KPI row + featured grouped bar + 2-column row + table.
**Charts used:** Grouped bar (actual vs budget), Waterfall (P&L build), Treemap (segment breakdown), Variance table.
**Color:** Green for favorable variance, red for unfavorable. Gray for budget line.
**Responsive:** Standard collapse.

### 5.8 Marketing Dashboard

**Audience:** Marketing team, CMO.
**Principle:** Funnel performance. Channel attribution.

```
+----------------------------------------------+
|  Marketing Performance  |  Last 30 days       |
+----------------------------------------------+
|  Visitors |  Leads  |  MQLs  |  Customers    |
|  45.2K    |  3.8K   |  890   |  142          |
+----------------------------------------------+
|  Funnel (Funnel chart, full width)            |
+----------------------------------------------+
|  Channel Performance  |  Campaign            |
|  (Horiz Bar)          |  Performance (Table) |
+----------------------------------------------+
|  Traffic Trend (Stacked Area, by channel)     |
+----------------------------------------------+
```

**Grid:** KPI row (funnel metrics) + funnel chart + 2-column + full-width trend.
**Charts used:** Funnel chart, Horizontal bar (by channel), Table (campaigns), Stacked area (traffic by channel).
**Responsive:** Standard collapse.

### 5.9 Product Analytics Dashboard

**Audience:** Product managers, growth team.
**Principle:** User behavior. Feature adoption. Retention.

```
+----------------------------------------------+
|  Product Analytics  |  Last 7 days  | Segment |
+----------------------------------------------+
|  DAU    |  WAU    |  Retention |  NPS         |
|  12.4K  |  45.2K  |  42%       |  67          |
+----------------------------------------------+
|  User Activity Trend (Line, DAU/WAU/MAU)      |
+----------------------------------------------+
|  Feature Adoption  |  Retention Cohort        |
|  (Horiz Bar)       |  (Heatmap)              |
+----------------------------------------------+
|  User Flow (Sankey: Signup -> Activation)     |
+----------------------------------------------+
```

**Grid:** KPI row + trend line + 2-column + full-width Sankey.
**Charts used:** Multi-series line, Horizontal bar (feature adoption), Cohort heatmap, Sankey (user flow).
**Responsive:** Standard collapse.

### 5.10 Mobile Dashboard (Card Stack)

**Audience:** Any user on mobile.
**Principle:** Vertical scroll. One chart per card. Touch-friendly.

```css
.dashboard-mobile {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 12px;
}

.dashboard-mobile .dashboard-card {
  width: 100%;
  border-radius: 12px;
  padding: 16px;
}

.dashboard-mobile .kpi-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.dashboard-mobile .chart-card {
  min-height: 240px;
}
```

**Layout:** Single column. KPIs in a 2-column grid at the top. Each chart in its own full-width card. Vertical scroll to see all.
**Charts:** Simplified versions. Horizontal bar instead of column. Fewer axis labels. Larger touch targets.
**Interaction:** Tap to expand chart full-screen. Swipe between time periods.

---

## 6. Component Patterns

### 6.1 Chart Card with Header

```css
.chart-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  overflow: hidden;
}

.chart-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px 0;
}

.chart-card-title {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
}

.chart-card-actions {
  display: flex;
  gap: 8px;
}

.chart-card-body {
  padding: 12px 20px 20px;
}
```

**Anatomy:** Title (left) + action buttons (right, e.g., expand, download, more options) + chart body.

### 6.2 Chart Card with Subtitle and Legend

```css
.chart-card-subtitle {
  font-size: 13px;
  color: #6b7280;
  margin-top: 2px;
}

.chart-card-legend {
  display: flex;
  gap: 16px;
  padding: 0 20px;
  margin-top: -4px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: #6b7280;
  cursor: pointer;
}

.legend-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.legend-item.inactive {
  opacity: 0.4;
  text-decoration: line-through;
}
```

### 6.3 Date Range Picker

```css
.date-range-picker {
  display: inline-flex;
  align-items: center;
  gap: 0;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  overflow: hidden;
}

.date-preset {
  padding: 8px 12px;
  font-size: 13px;
  font-weight: 500;
  color: #6b7280;
  background: white;
  border: none;
  cursor: pointer;
  border-right: 1px solid #e5e7eb;
}

.date-preset.active {
  background: #eff6ff;
  color: #1d4ed8;
}

.date-preset:last-child { border-right: none; }
```

**Presets:** 7D, 30D, 90D, YTD, 1Y, Custom.

### 6.4 Metric Comparison Strip

```css
.metric-comparison {
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.metric-primary {
  font-size: 28px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: #111827;
}

.metric-delta {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 14px;
  font-weight: 500;
}

.metric-delta.positive { color: #16a34a; }
.metric-delta.negative { color: #dc2626; }
.metric-delta.neutral  { color: #6b7280; }

.metric-context {
  font-size: 12px;
  color: #9ca3af;
}
```

### 6.5 Empty State for Charts

```css
.chart-empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 240px;
  text-align: center;
  padding: 40px;
}

.chart-empty-icon {
  width: 48px;
  height: 48px;
  color: #d1d5db;
  margin-bottom: 16px;
}

.chart-empty-title {
  font-size: 15px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 4px;
}

.chart-empty-description {
  font-size: 13px;
  color: #9ca3af;
  max-width: 280px;
}
```

**Content:** Icon (chart outline) + "No data available" + "Try adjusting your filters or date range."

### 6.6 Loading State for Charts

```css
.chart-loading {
  min-height: 240px;
  border-radius: 8px;
  background: linear-gradient(90deg, #f3f4f6 25%, #e5e7eb 50%, #f3f4f6 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
}

@keyframes shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

### 6.7 Error State for Charts

```css
.chart-error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 240px;
  text-align: center;
  padding: 40px;
  background: #fef2f2;
  border-radius: 8px;
}

.chart-error-title {
  font-size: 15px;
  font-weight: 600;
  color: #991b1b;
  margin-bottom: 4px;
}

.chart-error-description {
  font-size: 13px;
  color: #b91c1c;
  margin-bottom: 16px;
}

.chart-error-retry {
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 500;
  background: white;
  border: 1px solid #fca5a5;
  border-radius: 6px;
  color: #991b1b;
  cursor: pointer;
}
```

---

## 7. Advanced Layout Patterns

### 7.1 Tabs for Dashboard Sections

```css
.dashboard-tabs {
  display: flex;
  gap: 0;
  border-bottom: 1px solid #e5e7eb;
  margin-bottom: 16px;
}

.dashboard-tab {
  padding: 12px 20px;
  font-size: 14px;
  font-weight: 500;
  color: #6b7280;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  transition: all 150ms ease;
}

.dashboard-tab.active {
  color: #111827;
  border-bottom-color: #2563eb;
}

.dashboard-tab-panel {
  display: none;
}

.dashboard-tab-panel.active {
  display: block;
}
```

**Layout:** Tab bar below the header. Each tab shows a different dashboard view (Overview, Sales, Marketing, Operations). Only the active tab's content is rendered.
**Responsive:** Tabs become a dropdown selector on mobile.

### 7.2 Summary-to-Detail Drill-Down

**Level 1 (Summary):** KPI row + chart grid showing aggregates.
**Level 2 (Category):** Click a KPI or chart segment to navigate to a category-specific view with its own KPIs and charts.
**Level 3 (Detail):** Click a data point to see individual records in a data table.

**Navigation:** Breadcrumb trail at top: "Dashboard > Sales > North America > Q1 2026"
**Animation:** Slide-left transition when drilling down, slide-right when going back.

### 7.3 Split View (Table + Chart)

```css
.split-view {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  min-height: 500px;
}

.split-view-table {
  overflow-y: auto;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
}

.split-view-chart {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 20px;
}
```

**Layout:** Data table on the left, chart on the right. Selecting a row in the table updates the chart. Or: table shows the data behind the chart, synchronized with chart selection.
**Responsive:** Stack vertically, chart first then table (chart provides context for table).

### 7.4 Master-Detail (List + Detail Panel)

```css
.master-detail {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 0;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  overflow: hidden;
  min-height: 600px;
}

.master-list {
  border-right: 1px solid #e5e7eb;
  overflow-y: auto;
}

.master-list-item {
  padding: 12px 16px;
  border-bottom: 1px solid #f3f4f6;
  cursor: pointer;
}

.master-list-item.selected {
  background: #eff6ff;
  border-left: 3px solid #2563eb;
}

.detail-panel {
  padding: 24px;
  overflow-y: auto;
}
```

**Layout:** Scrollable list of entities (left) + detail view with charts and data for the selected entity (right).
**Responsive:** List collapses to a dropdown or modal selector. Detail view goes full width.

### 7.5 Full-Screen Single Chart (Presentation Mode)

```css
.chart-fullscreen {
  position: fixed;
  inset: 0;
  z-index: 100;
  background: white;
  padding: 24px;
  display: flex;
  flex-direction: column;
}

.chart-fullscreen-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.chart-fullscreen-body {
  flex: 1;
  min-height: 0;
}

.chart-fullscreen-close {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  background: #f3f4f6;
  cursor: pointer;
}
```

**Layout:** Any chart can be expanded to full screen for presentations or detailed analysis. Close button in top-right. ESC key to exit.

### 7.6 Scrollable Chart Carousel (Mobile)

```css
.chart-carousel {
  display: flex;
  gap: 12px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  padding: 0 12px 12px;
}

.chart-carousel::-webkit-scrollbar { display: none; }

.chart-carousel .dashboard-card {
  flex: 0 0 calc(100vw - 48px);
  scroll-snap-align: center;
}

.carousel-dots {
  display: flex;
  justify-content: center;
  gap: 6px;
  margin-top: 8px;
}

.carousel-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #d1d5db;
}

.carousel-dot.active { background: #2563eb; }
```

**Layout:** Horizontal scroll of chart cards with snap points. Dot indicators below. Swipe to navigate.

---

## 8. Responsive Collapse Strategies

### 8.1 Standard Collapse Order

```
Desktop (>1024px):  Full grid layout as designed
Tablet (768-1024px):
  - KPI row: 3 per row (wraps to 2 rows if 5 KPIs)
  - Charts: 2-column grid maximum
  - Sidebar filters: collapse to top filter bar
  - Data tables: hide low-priority columns

Mobile (<768px):
  - KPI row: 2 per row
  - Charts: single column, full width
  - Filters: bottom sheet or modal
  - Data tables: card view or horizontal scroll
  - Legend: below chart, horizontally scrollable
  - Tabs: dropdown selector
```

### 8.2 Priority-Based Hiding

```css
/* Show on all sizes */
.priority-critical { display: block; }

/* Hide on mobile */
@media (max-width: 767px) {
  .priority-high   { display: none; }
}

/* Hide on tablet and mobile */
@media (max-width: 1023px) {
  .priority-medium { display: none; }
}

/* Hide on smaller desktops */
@media (max-width: 1279px) {
  .priority-low    { display: none; }
}
```

Assign priority to each dashboard card. On smaller screens, lower-priority cards are hidden (with a "Show more" link to reveal them).

### 8.3 Container Queries for Charts

```css
.chart-container {
  container-type: inline-size;
}

@container (max-width: 400px) {
  .chart-legend { flex-direction: column; }
  .chart-axis-label { font-size: 10px; }
  .chart-title { font-size: 14px; }
}

@container (max-width: 300px) {
  .chart-legend { display: none; }
  .chart-y-axis-label { display: none; }
}
```

Container queries allow chart components to adapt based on their own size, not the viewport. This means the same chart component works in a wide card and a narrow card without viewport-level media queries.

---

## 9. Spacing and Visual Rhythm Reference

### 9.1 Spacing Scale

```
4px   - Minimum internal gap (between bar chart bars within a group)
8px   - Tight gap (between related elements)
12px  - Small gap (card gap on mobile, filter control gap)
16px  - Base gap (card gap on desktop, standard spacing)
20px  - Card padding (internal content padding)
24px  - Large gap (between dashboard sections)
32px  - Section separator (between major dashboard areas)
48px  - Major section gap (rarely used, between top-level dashboard sections)
```

### 9.2 Height Reference

```
KPI card:           100-120px
KPI card with chart: 140-160px
Small chart card:    240-280px
Medium chart card:   320-400px
Large chart card:    400-500px
Data table card:     400-600px (scrollable)
Full-screen chart:   100vh - 80px (header + padding)
```

### 9.3 Card Elevation Levels

```css
.card-flat {
  border: 1px solid #e5e7eb;
  box-shadow: none;
}

.card-raised {
  border: 1px solid #e5e7eb;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.card-elevated {
  border: 1px solid #e5e7eb;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.card-floating {
  border: none;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}
```

Use flat or raised for most cards. Elevated for modals or popovers. Floating for tooltips and dropdowns.

---

## 10. Dashboard Dark Theme

```css
[data-theme="dark"] .dashboard {
  background: #0f172a;
  color: #f1f5f9;
}

[data-theme="dark"] .dashboard-card {
  background: #1e293b;
  border-color: #334155;
}

[data-theme="dark"] .chart-card-title {
  color: #f1f5f9;
}

[data-theme="dark"] .kpi-label {
  color: #94a3b8;
}

[data-theme="dark"] .filter-bar {
  background: #1e293b;
  border-color: #334155;
}

[data-theme="dark"] .chart-gridline {
  stroke: #334155;
  opacity: 0.2;
}

[data-theme="dark"] .chart-axis-label {
  fill: #94a3b8;
}
```

**Dark theme rules for dashboards:**
- Background: very dark blue-gray (#0f172a), not pure black
- Cards: dark blue-gray (#1e293b)
- Text: light gray (#f1f5f9), not pure white
- Muted text: medium gray (#94a3b8)
- Borders: dark gray (#334155)
- Gridlines: slightly visible (#334155, opacity 0.2)
- Chart colors: slightly lighter/more saturated than light theme (see dataviz token dark overrides)
