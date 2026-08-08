# Chart Type Encyclopedia

> 50+ chart types with complete specifications. For each chart: when to use, when NOT to use, data shape required, max data points, design specs, accessibility notes, and visual description.

---

## 1. Comparison Charts

### 1.1 Vertical Bar Chart (Column Chart)

**When to use:** Compare values across a small number of categories (3-12). The default choice for categorical comparison.
**When NOT to use:** More than 12 categories (use horizontal bar). Continuous data (use histogram). Time series with many points (use line).
**Data shape:** 1 categorical dimension + 1 quantitative measure.
**Max data points:** 12-15 bars before the chart becomes crowded.

**Design specs:**
- Bar width: 24-48px minimum, never narrower than 12px
- Bar gap: 8-16px between bars (roughly 30-50% of bar width)
- Bar fill: solid color from categorical palette, no gradients
- Bar corner radius: 4px on top two corners only (flat bottom)
- Y-axis: starts at 0, 4-6 gridlines, gridline opacity 0.1-0.15
- X-axis: category labels, horizontal text if space allows, 45-degree rotation if needed
- Value labels: optional, placed above bars in 11px font-weight 500
- Hover: bar lightens 10%, tooltip shows exact value
- Sort: by value descending (unless categories have inherent order like months)

**Accessibility:** Alt text: "Bar chart showing [metric] by [category]. [Key insight, e.g., 'Category X leads at $Y.']" Provide data table alternative.

**Visual description:** Vertical rectangles rising from a horizontal baseline, each representing a category. Heights encode values. Gap between bars distinguishes discrete categories.

---

### 1.2 Horizontal Bar Chart

**When to use:** Compare values across many categories (7-30+). Long category labels. Ranking or sorted data. Mobile-friendly alternative to column chart.
**When NOT to use:** Fewer than 5 categories with short labels (column chart is more conventional). Time series.
**Data shape:** 1 categorical dimension + 1 quantitative measure.
**Max data points:** 30+ rows are readable with horizontal bars.

**Design specs:**
- Bar height: 20-32px
- Bar gap: 4-8px between bars
- Bar fill: single categorical color, or gradient of sequential palette for ranking
- X-axis (value): starts at 0, at top or bottom, 4-6 gridlines
- Y-axis (category): left-aligned text labels, 13-14px
- Sort: by value descending (longest bar on top) unless categories have inherent order
- Value labels: placed at end of bar, inside if bar is long enough, outside if short
- Hover: bar lightens 10%, tooltip shows exact value

**Accessibility:** Alt text: "Horizontal bar chart ranking [categories] by [metric]. Top: [category] at [value]. Bottom: [category] at [value]." Provide data table.

**Visual description:** Horizontal rectangles extending rightward from a vertical axis of category labels. Lengths encode values. Easy to read long labels.

---

### 1.3 Grouped Bar Chart

**When to use:** Compare values across categories, split by a second dimension (e.g., revenue by product, grouped by quarter). 2-4 groups.
**When NOT to use:** More than 4 groups (use small multiples). Only one dimension (use simple bar).
**Data shape:** 2 categorical dimensions + 1 quantitative measure.
**Max data points:** 4 groups x 8 categories = 32 bars maximum.

**Design specs:**
- Group gap: 16-24px (visually larger than within-group gap)
- Within-group gap: 2-4px
- Each group member gets a distinct categorical color
- Legend: top-right or below chart, matching group colors
- All other specs inherit from vertical bar chart

**Accessibility:** Alt text: "Grouped bar chart comparing [metric] by [dim1] and [dim2]. [Key comparison insight.]" Color alone must not be the only differentiator; use legend and tooltips.

**Visual description:** Clusters of bars at each category position. Bars within a cluster sit side by side with minimal gap. Clusters separated by larger gaps.

---

### 1.4 Stacked Bar Chart

**When to use:** Show total plus composition. Compare totals across categories while showing how each total breaks down.
**When NOT to use:** When precise comparison of individual segments matters (middle segments are hard to compare). More than 5 stack segments.
**Data shape:** 2 categorical dimensions + 1 quantitative measure.
**Max data points:** 10 categories x 5 segments = 50 values.

**Design specs:**
- Segments stacked vertically from the baseline
- Segment colors: sequential or categorical palette (max 5 segments)
- Segment borders: 1px white divider between segments
- Total label: optional, above the full stack
- Hover: highlight one segment across all bars, dim others to 30% opacity
- Legend: matches segment colors, ordered same as stack order

**Accessibility:** Alt text: "Stacked bar chart showing [total metric] by [category], broken down by [segments]. [Key insight.]" Data table is essential here since middle segments are hard to read precisely.

**Visual description:** Vertical bars where each bar is subdivided into colored segments stacked on top of each other. Total height encodes total value. Segment heights encode parts.

---

### 1.5 100% Stacked Bar Chart

**When to use:** Compare proportions across categories (e.g., market share by region). When the absolute values matter less than the percentage breakdown.
**When NOT to use:** When absolute values matter. When there are more than 5 segments.
**Data shape:** 2 categorical dimensions + 1 quantitative measure (converted to percentage).
**Max data points:** 10 categories x 5 segments.

**Design specs:**
- All bars same height (100%)
- Y-axis: 0% to 100%, gridlines at 25% intervals
- Percentage labels inside segments (if segment is large enough, >15%)
- All other specs inherit from stacked bar chart

**Accessibility:** Alt text: "100% stacked bar chart showing the proportional breakdown of [metric] across [categories]. [Key insight about proportions.]"

**Visual description:** All bars extend to the same height (100%). Colored segments within each bar show proportional composition. Easy to compare ratios.

---

### 1.6 Lollipop Chart

**When to use:** Same use case as bar chart but with a lighter, more elegant look. Works well with many categories. Reduces visual weight compared to bars.
**When NOT to use:** When the audience expects conventional bar charts. When bars need to show stacking.
**Data shape:** 1 categorical dimension + 1 quantitative measure.
**Max data points:** 20-30.

**Design specs:**
- Stem: thin line (1.5-2px) from baseline to value
- Head: circle (radius 5-6px) at the value position
- Stem color: gray (#9ca3af) or categorical color
- Head fill: categorical color, solid
- Horizontal orientation preferred for many categories
- Sort by value descending

**Accessibility:** Alt text: "Lollipop chart showing [metric] by [category], sorted by value. [Key insight.]"

**Visual description:** Thin lines extending from an axis, each topped with a dot. Like a simplified bar chart with less visual weight.

---

### 1.7 Dot Plot (Cleveland Dot Plot)

**When to use:** Compare values across many categories with high precision. Show ranges or multiple values per category (e.g., before/after, actual vs target).
**When NOT to use:** When audience is unfamiliar with dot plots.
**Data shape:** 1 categorical + 1-3 quantitative measures.
**Max data points:** 30+ categories.

**Design specs:**
- Dots: radius 4-6px, solid fill
- Multiple measures per category: different colored dots on the same row
- Connecting line between dots (for range): 1px gray
- Grid: horizontal lines at each category for visual tracking
- Y-axis: category labels left-aligned
- X-axis: value scale

**Accessibility:** Alt text: "Dot plot comparing [metrics] across [categories]. [Key insight.]"

**Visual description:** Dots positioned along a value axis for each category. Clean, precise, high data-to-ink ratio.

---

### 1.8 Bullet Chart (Stephen Few)

**When to use:** Show a single measure against a target and qualitative ranges (poor/satisfactory/good). KPI performance display. Compact alternative to gauges.
**When NOT to use:** When there is no target or qualitative context.
**Data shape:** 1 quantitative measure + 1 target + 2-3 qualitative ranges.
**Max data points:** 1-10 bullet charts stacked vertically.

**Design specs:**
- Qualitative ranges: 3 bands of gray (light to dark) representing poor/satisfactory/good
- Featured measure: a single dark bar (narrower than the qualitative bands)
- Comparative measure (target): a vertical line marker
- Width: qualitative band full width, featured bar ~40% width, target line ~60% width
- Orientation: horizontal (preferred) or vertical
- Label: metric name to the left, value at the right

**Accessibility:** Alt text: "Bullet chart for [metric]. Current value: [X]. Target: [Y]. Performance: [qualitative assessment]."

**Visual description:** A horizontal bar layered over gray bands, with a vertical line indicating the target. Compact, information-dense.

---

### 1.9 Radar Chart (Spider Chart)

**When to use:** Compare multiple quantitative variables for one or two entities. Skill profiles, competitive analysis, feature comparison. Works with 5-8 variables.
**When NOT to use:** More than 2-3 entities overlaid (becomes unreadable). Precise comparison needed (area distorts perception). General audiences (unfamiliar).
**Data shape:** 1 entity x 5-8 quantitative variables (each on its own axis).
**Max data points:** 2-3 entities x 8 variables.

**Design specs:**
- Axes: 5-8 spokes radiating from center, equally spaced
- Grid: concentric polygons (not circles) at scale intervals
- Fill: semi-transparent (opacity 0.2-0.3) with 2px solid border
- Points: dots at each axis value (radius 4px)
- Labels: axis names at the outer end of each spoke
- Multiple entities: overlay with different colors, max 2-3
- Scale: normalize all axes to 0-100 if they have different units

**Accessibility:** Alt text: "Radar chart comparing [entity/entities] across [N] dimensions. [Key strengths and weaknesses.]" Radar charts are particularly hard for screen readers; always provide a data table.

**Visual description:** A polygon shape formed by connecting data points plotted on multiple axes radiating from a center point. Filled area creates a distinctive shape profile.

---

## 2. Trend Charts

### 2.1 Line Chart (Single Series)

**When to use:** Show trend over time for a single measure. The default for time series data.
**When NOT to use:** Categorical data (use bar). Fewer than 5 time points (use bar). Non-continuous data.
**Data shape:** 1 time dimension + 1 quantitative measure.
**Max data points:** 200+ (lines handle density well).

**Design specs:**
- Line: 2px stroke, solid, categorical color
- Data points: hidden by default, show on hover (radius 4px, expand to 6px)
- X-axis: time labels, auto-thin to prevent overlap (show every Nth label)
- Y-axis: starts at contextually appropriate value (need not be 0 for line charts), 4-6 gridlines
- Gridlines: horizontal only, opacity 0.1-0.15
- Area under line: optional light fill (opacity 0.1) to ground the line
- Tooltip: vertical crosshair line + point highlight + value display
- Null/missing data: break the line (gap), do not interpolate unless noted

**Accessibility:** Alt text: "Line chart showing [metric] from [start] to [end]. Trend: [description, e.g., 'steady increase from X to Y with a dip in Month Z']."

**Visual description:** A continuous line connecting data points over a time axis. The slope and direction of the line communicate trend.

---

### 2.2 Multi-Series Line Chart

**When to use:** Compare trends across 2-5 series over the same time period.
**When NOT to use:** More than 5 series (spaghetti chart -- use small multiples or highlight + gray). Series with vastly different scales (use dual axis or separate charts).
**Data shape:** 1 time dimension + 2-5 quantitative measures (or 1 measure x 2-5 categories).
**Max data points:** 5 series x 50 time points = 250.

**Design specs:**
- Each series: distinct categorical color, 2px stroke
- Active series: full opacity. Inactive: reduce to 0.3 opacity on hover
- Legend: top or right, clickable to toggle series visibility
- Direct labels: label the last point of each line (more effective than legend)
- Tooltip: show all series values for the hovered time point
- If series cross frequently: use small multiples instead

**Accessibility:** Alt text: "Multi-series line chart comparing [N] [entities] from [start] to [end]. [Key comparison insight.]" Ensure legend is accessible and series are distinguishable by pattern (dash, dot-dash) not just color.

**Visual description:** Multiple colored lines sharing the same time axis. Each line represents a different series, with a legend mapping colors to labels.

---

### 2.3 Area Chart

**When to use:** Show trend over time with emphasis on volume/magnitude. Single series. The filled area adds visual weight compared to a line chart.
**When NOT to use:** Multiple overlapping series (areas occlude each other). When precise values matter more than overall shape.
**Data shape:** 1 time dimension + 1 quantitative measure.
**Max data points:** 200+.

**Design specs:**
- Line: 2px stroke on top edge
- Fill: gradient from line color (opacity 0.3) at top to transparent at bottom
- Y-axis: should start at 0 (area is misleading if baseline is not 0)
- All other specs inherit from line chart

**Accessibility:** Alt text: "Area chart showing [metric] volume from [start] to [end]. [Trend description.]"

**Visual description:** A line chart with the area below the line filled with a semi-transparent color, emphasizing the magnitude of values over time.

---

### 2.4 Sparkline

**When to use:** Inline trend indicator. Embedded in a table cell, KPI card, or text. Shows shape of trend without precise values.
**When NOT to use:** When exact values matter. Standalone chart (too small for detail).
**Data shape:** 1 time dimension + 1 quantitative measure.
**Max data points:** 20-90 (past 30-90 days typical).

**Design specs:**
- Size: 60-120px wide, 20-32px tall
- Line: 1.5px stroke, single color
- No axes, no labels, no gridlines
- Optional: highlight min/max points with small dots (radius 2px)
- Optional: highlight last point with larger dot (radius 3px)
- Optional: fill area below line with very light color (opacity 0.1)
- Color: match the KPI delta color (green for positive trend, red for negative)

**Accessibility:** Alt text: "Sparkline showing [metric] trend over [period]. Direction: [up/down/flat]." Sparklines must have textual context nearby.

**Visual description:** A tiny line chart, typically 60-120px wide, embedded inline. No axes or labels -- pure shape.

---

### 2.5 Slope Chart

**When to use:** Compare two time points (before/after, this year vs last year). Show how rankings or values changed between two moments.
**When NOT to use:** More than 2 time points (use line chart). More than 10 entities (too many crossing lines).
**Data shape:** 1 entity dimension + 2 time points + 1 quantitative measure.
**Max data points:** 10 entities x 2 time points.

**Design specs:**
- Two vertical axes: left (time 1) and right (time 2)
- Lines connecting each entity's value from left to right
- Line color: categorical, or encode direction (green for increase, red for decrease)
- Labels: entity name and value at both ends
- Crossing lines: reduce opacity of non-hovered lines to 0.2

**Accessibility:** Alt text: "Slope chart comparing [entities] between [time1] and [time2]. Biggest change: [entity] from [val1] to [val2]."

**Visual description:** Two parallel vertical axes connected by diagonal lines. Each line represents an entity, with its slope indicating direction and magnitude of change.

---

### 2.6 Step Chart

**When to use:** Data that changes at discrete intervals and remains constant between changes (pricing tiers, policy changes, plan levels). Emphasizes the exact moment of change.
**When NOT to use:** Continuously changing data (use line chart).
**Data shape:** 1 time dimension + 1 quantitative measure (discrete changes).
**Max data points:** 50+.

**Design specs:**
- Line: 2px stroke, steps as right-angles (horizontal then vertical)
- Fill below: optional, same as area chart
- Change points: optional dot markers (radius 4px)
- All other specs inherit from line chart

**Accessibility:** Alt text: "Step chart showing [metric] changes over [period]. [Number] changes occurred, ranging from [min] to [max]."

**Visual description:** A line that moves in right-angle steps -- horizontal segments at constant values connected by vertical jumps when values change.

---

### 2.7 Range Area Chart

**When to use:** Show a range (min-max, confidence interval, high-low) over time. Temperature ranges, price ranges, uncertainty bands.
**When NOT to use:** Single value trend (use line or area).
**Data shape:** 1 time dimension + 2 quantitative measures (upper bound, lower bound).
**Max data points:** 200+.

**Design specs:**
- Band fill: semi-transparent color (opacity 0.2-0.3)
- Upper and lower boundary lines: 1.5px stroke
- Optional center line: 2px stroke (median or mean)
- Color: single hue for the band, darker shade for center line

**Accessibility:** Alt text: "Range area chart showing [metric] range from [start] to [end]. Range typically between [low] and [high], with [trend description]."

**Visual description:** A shaded band between two boundary lines, showing the range of values over time. Wider bands indicate more variance.

---

## 3. Part-to-Whole Charts

### 3.1 Pie Chart

**When to use:** Show parts of a whole when there are 2-5 segments and one segment dominates. Works when the story is "this one part is more than half."
**When NOT to use:** More than 5 slices. When precise comparison between slices matters. When values do not sum to a meaningful whole.
**Data shape:** 1 categorical dimension + 1 quantitative measure (summing to 100%).
**Max data points:** 5 slices (2-3 is ideal).

**Design specs:**
- Slices: solid categorical colors, no gradients, no 3D, no exploded slices
- Stroke between slices: 2px white
- Labels: percentage + category name, positioned outside with leader lines, or inside if slice is large enough (>15%)
- Start angle: 12 o'clock (top), slices proceed clockwise
- Largest slice starts at 12 o'clock
- Sort: largest to smallest, clockwise
- Hover: slight separation (2-3px outward pull) + tooltip

**Accessibility:** Alt text: "Pie chart showing [whole] broken down by [category]. Largest segment: [name] at [%]. Smallest: [name] at [%]." Always provide a data table. Pie charts are hard for colorblind users; add percentage labels.

**Visual description:** A circle divided into wedge-shaped slices. Slice angle encodes proportion. The circle represents the whole (100%).

---

### 3.2 Donut Chart

**When to use:** Same as pie chart, but with a center hole that can display a summary number. Slightly better than pie as the center removes the misleading area perception of small inner slices.
**When NOT to use:** Same restrictions as pie chart.
**Data shape:** Same as pie chart.
**Max data points:** 5 slices.

**Design specs:**
- Inner radius: 55-65% of outer radius (creates a ring, not a thin sliver)
- Center content: total value, key metric, or icon
- Center text: 24-32px bold for number, 12px muted for label
- All other specs inherit from pie chart

**Accessibility:** Same as pie chart. Center content should be described in alt text.

**Visual description:** A pie chart with a hollow center. The ring of segments surrounds a central space that often contains a summary number.

---

### 3.3 Treemap

**When to use:** Show hierarchical part-to-whole relationships. Hundreds of items with nested categories. Area encodes value, color can encode a second dimension.
**When NOT to use:** Few categories (use bar chart). When precise comparison matters (rectangles are harder to compare than bars). Non-hierarchical data.
**Data shape:** Hierarchical categories + 1 quantitative measure (size) + optional 1 quantitative measure (color).
**Max data points:** 200+ (treemaps handle many items well).

**Design specs:**
- Algorithm: squarified treemap (aspect ratio close to 1:1 for readability)
- Border between cells: 1-2px white
- Border between hierarchy levels: 3-4px white (visually thicker)
- Labels: inside each cell, truncated with ellipsis if cell is small
- Minimum cell size for label: 60px x 30px
- Color: sequential palette (one measure) or categorical (by top-level category)
- Hover: outline highlight (2px) + tooltip with full label and value
- Drill-down: click to zoom into a branch, breadcrumb for navigation back

**Accessibility:** Alt text: "Treemap showing [metric] across [N] [categories]. Largest: [name] at [value]. Hierarchy has [N] levels." Treemaps are very hard for screen readers; data table is essential.

**Visual description:** A rectangle subdivided into smaller rectangles. Each rectangle's area is proportional to its value. Nested rectangles show hierarchy.

---

### 3.4 Sunburst Chart

**When to use:** Show hierarchical part-to-whole with emphasis on the hierarchy path. Multi-level categories (e.g., department > team > individual).
**When NOT to use:** More than 3-4 hierarchy levels. When precise comparison matters. Non-hierarchical data.
**Data shape:** Hierarchical categories + 1 quantitative measure.
**Max data points:** 100+ leaves.

**Design specs:**
- Center ring: top-level categories (widest arcs)
- Outer rings: child categories (narrower arcs)
- Ring width: 30-60px per level
- Color: inherit from parent (lighter shade for children) or distinct per top-level category
- Gap between arcs: 1px white
- Hover: highlight the arc and its ancestors, dim others to 30% opacity
- Click: zoom into the selected branch

**Accessibility:** Alt text: "Sunburst chart showing [metric] hierarchy with [N] levels. [Key path description.]" Provide hierarchical data table.

**Visual description:** Concentric rings divided into arcs. The innermost ring shows top-level categories; each ring outward shows the next hierarchy level. Arc angle encodes value.

---

### 3.5 Waffle Chart

**When to use:** Show a percentage or proportion as filled squares in a 10x10 grid. Engaging alternative to pie chart for a single proportion (e.g., "73% of users...").
**When NOT to use:** Multiple simultaneous proportions to compare. Precise values (hard to count individual squares).
**Data shape:** 1 percentage value (or 2-3 if showing simple breakdown).
**Max data points:** 1-3 proportions in the same grid.

**Design specs:**
- Grid: 10x10 = 100 squares
- Square size: 12-20px per square
- Gap: 2px between squares
- Filled squares: categorical color for the "filled" portion
- Unfilled squares: light gray (#e5e7eb)
- Fill order: left-to-right, top-to-bottom (like reading order)
- Label: percentage displayed prominently (24-32px) beside or above the grid

**Accessibility:** Alt text: "Waffle chart showing [X]% of [total] are [category]." Simple and effective for screen readers.

**Visual description:** A 10x10 grid of small squares where a proportion of squares are filled with color. Each square represents 1%.

---

### 3.6 Marimekko Chart (Mekko)

**When to use:** Show part-to-whole along two dimensions simultaneously. Both width and height encode data (e.g., market size x market share).
**When NOT to use:** When audience is unfamiliar (unusual chart type). When either dimension alone would suffice.
**Data shape:** 2 categorical dimensions + 2 quantitative measures.
**Max data points:** 5-8 columns x 3-5 segments.

**Design specs:**
- Column widths: proportional to one measure (e.g., total market size)
- Segment heights within columns: proportional to another measure (e.g., share)
- Column borders: 2px white vertical dividers
- Segment borders: 1px white horizontal dividers
- Labels: inside segments (percentage), column labels at top (category + total)
- Color: categorical for segments

**Accessibility:** Alt text: "Marimekko chart showing [dim1] (column width) by [dim2] (segment height). [Key insight.]" Data table essential.

**Visual description:** Variable-width columns divided into stacked segments. Column width encodes one value; segment height encodes another. Every pixel of area maps to data.

---

## 4. Distribution Charts

### 4.1 Histogram

**When to use:** Show the distribution (frequency) of a single continuous variable. Understand shape: normal, skewed, bimodal, uniform.
**When NOT to use:** Categorical data (use bar chart -- histograms are for continuous data). Comparing distributions of multiple groups (use box plot, violin, or overlaid histograms carefully).
**Data shape:** 1 continuous quantitative variable, binned into ranges.
**Max data points:** Underlying data can be millions; typically 10-30 bins displayed.

**Design specs:**
- Bins: 10-30 bins (Sturges, Scott, or Freedman-Diaconis rule for bin count)
- Bars: NO gap between bars (continuous data -- adjacent bars touch)
- Bar fill: single color, solid
- X-axis: bin range labels or bin center points
- Y-axis: frequency count or density (probability), starts at 0
- Mean/median line: optional vertical dashed line with label

**Accessibility:** Alt text: "Histogram showing distribution of [variable]. Shape: [normal/skewed/bimodal]. Center: approximately [value]. Range: [min] to [max]."

**Visual description:** Adjacent bars (no gaps) where bar height shows frequency of values within each range. The overall shape reveals the distribution pattern.

---

### 4.2 Box Plot (Box-and-Whisker)

**When to use:** Compare distributions across categories. Show median, quartiles, and outliers compactly. Multiple groups side by side.
**When NOT to use:** When audience is unfamiliar (explain or use simpler alternative). When distribution shape details matter (use violin).
**Data shape:** 1 categorical dimension + 1 continuous quantitative measure.
**Max data points:** 15-20 categories.

**Design specs:**
- Box: Q1 to Q3 (interquartile range), width 20-40px
- Median line: bold horizontal line inside box (2px)
- Whiskers: lines extending to min/max within 1.5x IQR
- Outliers: individual dots beyond whiskers (radius 3px)
- Fill: light categorical color (opacity 0.3) with solid border (2px)
- Orientation: vertical (default) or horizontal (for many categories)
- Reference line: optional horizontal line at mean or target

**Accessibility:** Alt text: "Box plot comparing distribution of [variable] across [N] [categories]. [Category with highest median]: median [value], range [min-max]."

**Visual description:** A rectangle (box) spanning the middle 50% of values with a line at the median. Whiskers extend to extremes. Dots mark outliers.

---

### 4.3 Violin Plot

**When to use:** Compare distributions across categories with full shape detail. Shows density, not just quartiles. Reveals bimodal or unusual distributions.
**When NOT to use:** When audience is unfamiliar. Fewer than 3 categories (histogram might be clearer).
**Data shape:** 1 categorical dimension + 1 continuous quantitative measure.
**Max data points:** 10-15 categories.

**Design specs:**
- Shape: mirrored density curve (symmetric kernel density estimate)
- Width: max width 40-60px per violin
- Fill: light categorical color (opacity 0.3)
- Outline: 1.5px solid stroke
- Inner box plot: optional mini box plot inside (25% width of violin)
- Median: dot or line inside the violin

**Accessibility:** Alt text: "Violin plot showing distribution of [variable] across [categories]. [Category] shows [bimodal/normal/skewed] distribution."

**Visual description:** Symmetrical curved shapes resembling violins, where width at any point represents the density of data at that value. Wider sections mean more data points.

---

### 4.4 Density Plot

**When to use:** Show the continuous probability distribution of a variable. Overlay 2-3 distributions for comparison. Smoother than histogram.
**When NOT to use:** When exact bin counts matter (use histogram). More than 3 overlaid distributions.
**Data shape:** 1 continuous quantitative variable (per series).
**Max data points:** 2-3 overlaid distributions.

**Design specs:**
- Curve: smooth kernel density estimate, 2px stroke
- Fill: semi-transparent (opacity 0.2) below the curve
- Multiple distributions: different colors, labeled directly or via legend
- X-axis: variable values
- Y-axis: density (typically unlabeled or 0-1 scale)

**Accessibility:** Alt text: "Density plot showing distribution of [variable] for [groups]. [Group A] is centered around [value], while [Group B] is centered around [value]."

**Visual description:** Smooth curves where height represents the probability density. Like a smoothed histogram. Overlapping curves make direct comparison easy.

---

### 4.5 Strip Plot (Jitter Plot)

**When to use:** Show individual data points for small-to-medium datasets (20-200 points). Reveals distribution and individual values. Good for showing outliers.
**When NOT to use:** Large datasets (>500 points per category -- dots overlap). When summary statistics are more useful.
**Data shape:** 1 categorical dimension + 1 continuous quantitative measure.
**Max data points:** 200 per category.

**Design specs:**
- Dots: radius 3-4px, semi-transparent (opacity 0.5-0.7)
- Jitter: random horizontal offset to prevent overlap (within category width)
- Orientation: horizontal or vertical
- Dot color: single color per category, or encode a third variable
- Optional: overlay mean/median line or box plot

**Accessibility:** Alt text: "Strip plot showing individual [measure] values for [N] [categories]. [Category] has most variation, ranging from [min] to [max]."

**Visual description:** Individual dots for each data point, spread horizontally within category lanes to avoid overlap. Cluster density reveals distribution.

---

### 4.6 Bee Swarm Plot

**When to use:** Same as strip plot but arranged to avoid overlap. Each dot is nudged to prevent overplotting while staying as close to the category center as possible.
**When NOT to use:** Very large datasets (computation and rendering become expensive).
**Data shape:** Same as strip plot.
**Max data points:** 100-300 per category.

**Design specs:**
- Dots: radius 3-4px, solid fill
- Arrangement: force-directed or algorithmic packing to avoid overlap
- Width per category: expands as needed to fit all dots without overlap
- All other specs inherit from strip plot

**Accessibility:** Same as strip plot.

**Visual description:** Like a strip plot, but dots are arranged so none overlap, creating organic "swarm" shapes. The overall shape reveals the distribution.

---

## 5. Relationship Charts

### 5.1 Scatter Plot

**When to use:** Show the relationship between two continuous variables. Identify correlation, clusters, and outliers.
**When NOT to use:** Categorical data. Time series (implies sequence -- use line). Very few data points (<10).
**Data shape:** 2 continuous quantitative measures.
**Max data points:** 500-2000 (use opacity to handle overplotting).

**Design specs:**
- Dots: radius 4-6px, semi-transparent (opacity 0.5-0.7) to handle overlap
- Color: single color (default), or encode a categorical third variable
- X-axis: independent variable (if applicable)
- Y-axis: dependent variable (if applicable)
- Gridlines: both horizontal and vertical, opacity 0.1
- Trend line: optional linear regression line (dashed, 1.5px, muted color)
- Quadrants: optional reference lines dividing the plot into meaningful zones
- Hover: enlarge dot, show tooltip with both values and entity name
- Zoom: support brush-zoom for dense scatter plots

**Accessibility:** Alt text: "Scatter plot showing relationship between [X] and [Y] for [N] [entities]. Pattern: [positive correlation/negative correlation/no clear pattern/clusters]."

**Visual description:** Dots scattered across a two-axis plane, with each dot's position encoding two values. The pattern of dots reveals relationships.

---

### 5.2 Bubble Chart

**When to use:** Scatter plot with a third variable encoded as bubble size. Show relationships between three continuous variables.
**When NOT to use:** Size differences are small (hard to perceive small area differences). When precise size comparison matters.
**Data shape:** 3 continuous quantitative measures (x, y, size). Optional: categorical for color.
**Max data points:** 50-100 bubbles.

**Design specs:**
- Bubble radius: proportional to SQUARE ROOT of the value (area, not radius, should be proportional)
- Minimum radius: 4px (must be visible)
- Maximum radius: 40-60px (must not overwhelm)
- Opacity: 0.6-0.7 (bubbles overlap)
- Stroke: 1px solid border (slightly darker than fill)
- Label inside: if bubble is large enough (>24px radius)
- Legend for size: show a reference bubble with known size

**Accessibility:** Alt text: "Bubble chart showing [X] vs [Y], with bubble size representing [Z]. Largest bubble: [entity] at [Z value]. [Pattern description.]"

**Visual description:** Circles of varying sizes scattered on a two-axis plane. Position encodes X and Y values; area encodes a third value.

---

### 5.3 Correlation Matrix (Heatmap Matrix)

**When to use:** Show pairwise correlations between many variables (5-20). Identify which variables are strongly related.
**When NOT to use:** Fewer than 4 variables (just describe correlations). Non-numeric variables.
**Data shape:** N x N matrix of correlation coefficients (-1 to +1).
**Max data points:** 20 x 20 = 400 cells.

**Design specs:**
- Cell color: diverging palette (red for negative, blue for positive, white for zero)
- Cell size: uniform squares, 30-50px per cell
- Labels: variable names on both axes
- Value labels: correlation coefficient inside each cell (2 decimal places)
- Diagonal: 1.0 always (self-correlation), can be grayed out
- Triangle: optionally show only upper or lower triangle (symmetric matrix)
- Sort: cluster correlated variables together (hierarchical clustering)

**Accessibility:** Alt text: "Correlation matrix for [N] variables. Strongest positive correlation: [var1] and [var2] at [value]. Strongest negative: [var1] and [var2] at [value]."

**Visual description:** A grid of colored squares where color intensity and hue show the strength and direction of correlation between variable pairs.

---

### 5.4 Parallel Coordinates

**When to use:** Compare multiple entities across many (5-15) quantitative variables simultaneously. Find patterns, clusters, and outliers in multivariate data.
**When NOT to use:** General audiences (unfamiliar chart type). Fewer than 4 variables. When precise reading of individual values matters.
**Data shape:** N entities x 5-15 quantitative variables.
**Max data points:** 100-500 entities (use opacity to manage density).

**Design specs:**
- Axes: parallel vertical lines, equally spaced, one per variable
- Lines: one polyline per entity connecting its value on each axis
- Opacity: 0.1-0.3 (many overlapping lines)
- Color: categorical (by cluster/group) or sequential (by one variable)
- Brushing: click-drag on any axis to select a range, highlighting matching lines
- Axis reordering: allow user to drag axes to reposition (adjacent correlated axes reveal patterns)

**Accessibility:** Alt text: "Parallel coordinates chart showing [N] [entities] across [N] variables. [Key pattern or cluster description.]" Very hard for screen readers; data table essential.

**Visual description:** Parallel vertical axes, each representing a variable. Lines connect across all axes for each data point, forming patterns that reveal multivariate relationships.

---

## 6. Composition Over Time

### 6.1 Stacked Area Chart

**When to use:** Show how composition changes over time. Total and its parts, all evolving. Works with 2-5 series.
**When NOT to use:** More than 5 series (middle layers become unreadable). When individual series values need precise reading (only top and bottom series are easy to read).
**Data shape:** 1 time dimension + 2-5 quantitative measures (stacking to a total).
**Max data points:** 5 series x 100 time points = 500.

**Design specs:**
- Stacking order: largest series at bottom (most stable baseline)
- Fill: solid categorical colors (no gradients), opacity 0.8
- Series borders: 1px white between series
- Y-axis: starts at 0
- Hover: highlight one series (full opacity), dim others (opacity 0.2)
- Legend: matches series order

**Accessibility:** Alt text: "Stacked area chart showing [total metric] over [period], broken into [N] categories. [Key composition change.]"

**Visual description:** Colored areas stacked on top of each other over a time axis. The total height is the sum; each colored band shows a component's contribution.

---

### 6.2 Stream Graph (ThemeRiver)

**When to use:** Show composition over time with emphasis on aesthetic flow and overall shape. Works for many series (5-10+). More organic feel than stacked area.
**When NOT to use:** When precise values matter. When audience needs exact readings. Business dashboards (too decorative for most use cases).
**Data shape:** 1 time dimension + 5-10+ quantitative measures.
**Max data points:** 10 series x 100 time points.

**Design specs:**
- Baseline: centered (streams flow above and below a central axis)
- Streams: smooth, organic curves using cardinal spline interpolation
- Fill: categorical colors, opacity 0.8
- Labels: directly on the largest streams
- Hover: highlight one stream, dim others

**Accessibility:** Alt text: "Stream graph showing [topic] composition over [period]. Dominant themes: [list]. Trend: [description]." Data table essential.

**Visual description:** Flowing, organic streams of color that expand and contract over time, centered around a horizontal axis. Width encodes magnitude.

---

### 6.3 Alluvial Diagram

**When to use:** Show how categorical compositions change between discrete time points or stages. Flow from one state to another.
**When NOT to use:** Continuous time (use stacked area). When there is no meaningful flow between stages.
**Data shape:** 2-5 categorical stages + flow magnitudes between them.
**Max data points:** 5 stages x 8 categories.

**Design specs:**
- Nodes: vertical bars at each stage, subdivided by category
- Flows: curved bands connecting categories across stages
- Flow width: proportional to magnitude
- Color: by source category (maintain color through flow)
- Flow opacity: 0.4-0.6 (semi-transparent for overlapping flows)
- Hover: highlight one flow path from start to end

**Accessibility:** Alt text: "Alluvial diagram showing flow from [stage1] to [stageN]. [Key flow description, e.g., 'Most users flow from Free to Premium']."

**Visual description:** Vertical bars at discrete stages connected by flowing colored bands. Band width shows the magnitude of flow between categories across stages.

---

## 7. Flow Charts

### 7.1 Sankey Diagram

**When to use:** Show flow from sources to destinations with proportional width. Energy flows, user journeys, budget allocation, conversion funnels.
**When NOT to use:** Circular flows (Sankey is DAG -- directed acyclic). When there are too many small flows (noise).
**Data shape:** Source nodes + target nodes + flow magnitude.
**Max data points:** 20-40 nodes, 50-100 flows.

**Design specs:**
- Nodes: vertical rectangles, height proportional to total flow through node
- Node width: 12-20px
- Node labels: beside nodes, 13px
- Links: curved bands connecting source to target
- Link width: proportional to flow magnitude
- Link color: source color at 40-60% opacity, or gradient from source to target color
- Node gap: 8-16px vertical spacing
- Hover: highlight all flows through hovered node or link
- Layout: auto-arranged by flow direction (left to right)

**Accessibility:** Alt text: "Sankey diagram showing flows from [sources] to [destinations]. Largest flow: [source] to [destination] at [value]."

**Visual description:** Colored bands of varying width flow from left-side nodes to right-side nodes. Band width shows flow magnitude. Nodes show totals.

---

### 7.2 Chord Diagram

**When to use:** Show flows between entities in a circular layout. All entities are both sources and targets. Mutual relationships (trade between countries, communication between teams).
**When NOT to use:** One-directional flows (use Sankey). More than 10 entities (becomes unreadable). When precise flow values matter.
**Data shape:** N x N matrix of flow values.
**Max data points:** 10 x 10 = 100 flows.

**Design specs:**
- Arc segments: around the circle perimeter, one per entity, length proportional to total flow
- Chords: curved bands connecting arcs, width proportional to flow
- Color: chords colored by source entity
- Opacity: chords at 0.5-0.6
- Hover: highlight all chords connected to hovered entity, dim others
- Gap between arcs: 2-4px

**Accessibility:** Alt text: "Chord diagram showing flows between [N] [entities]. Largest connection: [entity1] to [entity2] at [value]."

**Visual description:** A circular layout with arc segments around the perimeter. Curved ribbons (chords) connect arcs, with ribbon width encoding flow magnitude.

---

### 7.3 Funnel Chart

**When to use:** Show progressive reduction through stages (sales funnel, conversion funnel, recruitment pipeline). Emphasizes drop-off at each stage.
**When NOT to use:** When stages do not represent progressive reduction. When precise comparison between stages matters more than the funnel narrative.
**Data shape:** Ordered stages + 1 quantitative measure per stage (decreasing).
**Max data points:** 3-7 stages.

**Design specs:**
- Shape: symmetrical trapezoids stacked vertically, widest at top
- Width: proportional to value at each stage
- Stage height: uniform (40-60px per stage)
- Gap between stages: 2-4px
- Labels: stage name + value + conversion rate (percentage of previous stage)
- Color: single hue gradient (darkest at top), or categorical per stage
- Hover: highlight stage, show detailed conversion metrics in tooltip

**Accessibility:** Alt text: "Funnel chart showing [process] conversion. Start: [value] at [stage1]. End: [value] at [last stage]. Overall conversion: [%]."

**Visual description:** A vertical stack of trapezoids, widest at top, narrowing toward the bottom. Each level represents a stage with decreasing values.

---

### 7.4 Network Graph (Node-Link Diagram)

**When to use:** Show relationships between entities (social networks, dependencies, knowledge graphs). Explore connections and clusters.
**When NOT to use:** More than 200 nodes (becomes hairball). When hierarchical structure is more important (use tree). When precise layout matters.
**Data shape:** Nodes + edges (connections between nodes). Optional: node size, edge weight.
**Max data points:** 50-200 nodes, 100-500 edges.

**Design specs:**
- Nodes: circles, radius 6-20px (proportional to importance/degree)
- Node color: categorical (by cluster/group)
- Node label: beside node, 11-12px, visible for important nodes, hidden for others until hover
- Edges: lines connecting nodes, 1-2px stroke
- Edge weight: line thickness (1-4px) or opacity
- Layout: force-directed (d3-force), or specific layout (circular, hierarchical)
- Hover: highlight node + connected nodes + edges, dim rest to 10% opacity
- Zoom and pan: essential for any non-trivial network

**Accessibility:** Alt text: "Network graph with [N] nodes and [N] connections. [Key structural insight: clusters, central nodes, isolated nodes.]" Very hard for screen readers; provide entity list with connection counts.

**Visual description:** Circles (nodes) connected by lines (edges) in a force-directed layout. Clusters of densely connected nodes emerge naturally.

---

## 8. Geospatial Charts

### 8.1 Choropleth Map

**When to use:** Color geographic regions (countries, states, counties, zip codes) by a quantitative value. Population density, election results, economic indicators.
**When NOT to use:** When geographic area size distorts perception (large low-value regions dominate visually). Point data (use bubble map).
**Data shape:** Geographic regions + 1 quantitative measure.
**Max data points:** Depends on map (50 states, 200 countries, etc.).

**Design specs:**
- Fill color: sequential palette (one variable) or diverging palette (above/below center)
- Border: 0.5-1px white between regions
- Legend: horizontal color scale with value labels, positioned below map
- Hover: darken region fill, show tooltip with region name and value
- No data: light gray fill with diagonal stripe pattern
- Projection: appropriate for the area (Mercator for world, Albers for US)

**Accessibility:** Alt text: "Choropleth map of [region] showing [metric] by [geography]. Highest: [region] at [value]. Lowest: [region] at [value]." Provide a ranked data table as alternative.

**Visual description:** A geographic map where each region is filled with a color from a gradient scale. Darker colors indicate higher values.

---

### 8.2 Bubble Map

**When to use:** Plot data at geographic points with size encoding magnitude. City populations, event locations, facility sizes.
**When NOT to use:** When region-level aggregation is more meaningful (use choropleth).
**Data shape:** Geographic coordinates (lat/lng) + 1 quantitative measure (size) + optional 1 categorical (color).
**Max data points:** 100-300 bubbles.

**Design specs:**
- Bubbles: radius proportional to SQUARE ROOT of value (area encodes value)
- Minimum radius: 4px
- Maximum radius: 40px
- Opacity: 0.6-0.7 (overlapping bubbles)
- Stroke: 1px white border
- Base map: muted, low-contrast tiles (light gray, no labels or minimal labels)
- Zoom: support zoom to separate overlapping bubbles

**Accessibility:** Alt text: "Bubble map showing [metric] across [N] locations. Largest: [location] at [value]. [Geographic pattern description.]"

**Visual description:** A geographic map with circles of varying sizes placed at specific locations. Circle size represents data magnitude.

---

### 8.3 Heat Map (Geographic)

**When to use:** Show density of points or events across a geographic area. Crime hotspots, traffic congestion, population density from point data.
**When NOT to use:** When individual points matter (use bubble map). When region aggregation is sufficient (use choropleth).
**Data shape:** Many geographic coordinates (hundreds to millions of points).
**Max data points:** Thousands to millions (aggregated into density).

**Design specs:**
- Color scale: sequential (typically: transparent -> yellow -> orange -> red)
- Radius: kernel density radius 20-50px (adjustable)
- Opacity: gradient from 0 (no data) to 0.8 (high density)
- Base map: dark tiles for heat map visibility
- Blur: Gaussian blur for smooth transitions

**Accessibility:** Alt text: "Geographic heat map showing density of [events] in [region]. Hotspots: [location1], [location2]." Provide summary statistics by zone.

**Visual description:** A geographic map overlaid with a smooth gradient of warm colors. Red/orange hotspots indicate areas of high concentration.

---

### 8.4 Flow Map

**When to use:** Show movement between geographic locations. Migration, trade routes, airline routes, supply chains.
**When NOT to use:** Non-geographic flows (use Sankey).
**Data shape:** Origin coordinates + destination coordinates + magnitude.
**Max data points:** 50-200 flows.

**Design specs:**
- Lines: curved arcs from origin to destination
- Line width: proportional to flow magnitude (1-6px)
- Color: single color with opacity variation, or categorical by flow type
- Arrowheads: optional, indicating direction
- Base map: muted background
- Hover: highlight one flow, show origin, destination, and magnitude

**Accessibility:** Alt text: "Flow map showing [type of movement] between [N] locations. Largest flow: [origin] to [destination] at [value]."

**Visual description:** A map with curved lines connecting locations. Line thickness indicates flow magnitude. The overall pattern shows dominant corridors of movement.

---

## 9. Hierarchical Charts

### 9.1 Circle Packing

**When to use:** Show hierarchical data with a softer, more organic aesthetic than treemaps. Nested circles show containment relationships.
**When NOT to use:** When space efficiency matters (circles waste space in corners). When precise comparison matters.
**Data shape:** Hierarchical categories + 1 quantitative measure.
**Max data points:** 100-500 nodes.

**Design specs:**
- Circles: radius proportional to square root of value
- Nesting: parent circles contain child circles
- Color: by hierarchy level (lighter for deeper levels)
- Stroke: 1px on all circles
- Labels: inside circles that are large enough, outside for small ones
- Zoom: click a circle to zoom into its children

**Accessibility:** Alt text: "Circle packing diagram showing [hierarchy]. Largest group: [name]. [N] levels of nesting."

**Visual description:** Circles nested within circles. Each circle's area represents a value, and containment represents the hierarchy.

---

### 9.2 Dendrogram (Tree Diagram)

**When to use:** Show hierarchical clustering or tree structure. Organizational charts, file systems, taxonomy, clustering results.
**When NOT to use:** When quantitative value matters (use treemap). Very deep hierarchies (>6 levels).
**Data shape:** Hierarchical tree structure (parent-child relationships).
**Max data points:** 50-200 leaf nodes.

**Design specs:**
- Layout: top-to-bottom (vertical) or left-to-right (horizontal)
- Nodes: circles (radius 4-6px) or rectangles (for labels)
- Edges: lines connecting parent to children (L-shaped or curved)
- Edge width: 1.5px
- Node color: by depth level or by cluster
- Labels: at leaf nodes, 11-12px
- Collapse: allow collapsing subtrees for large hierarchies

**Accessibility:** Alt text: "Dendrogram showing [hierarchy type] with [N] levels and [N] leaf nodes. Top level: [root]. [Key structural insight.]"

**Visual description:** A branching tree structure where nodes connect to children via lines. The layout reveals hierarchy depth and branching patterns.

---

### 9.3 Org Chart

**When to use:** Show organizational reporting structure. People, teams, departments.
**When NOT to use:** Non-hierarchical relationships (use network graph). Very large organizations (>200 people in one view).
**Data shape:** Hierarchical tree (parent-child with metadata per node).
**Max data points:** 50-200 nodes.

**Design specs:**
- Node cards: 140-200px wide, 60-80px tall, with name, title, optional avatar
- Layout: top-to-bottom, centered children under parents
- Connectors: vertical + horizontal lines (elbow connectors), 1.5px
- Level spacing: 60-80px vertical gap between levels
- Node spacing: 16-24px horizontal gap between siblings
- Collapse: allow collapsing subtrees with +/- indicator and count badge
- Hover: highlight reporting chain (ancestors + descendants)

**Accessibility:** Alt text: "Organization chart with [N] levels and [N] people. [Root person/role] at top. [Key structural notes.]"

**Visual description:** Rectangular cards arranged in a top-to-bottom tree. Lines connect managers to reports. Each card shows a person or role.

---

## 10. Specialized Charts

### 10.1 Gauge Chart

**When to use:** Show a single value's position within a defined range. Progress toward a goal. System health indicators.
**When NOT to use:** When comparison across multiple items is needed. When there is no meaningful min/max range. Multiple gauges (use bullet charts instead -- more space-efficient).
**Data shape:** 1 quantitative value + 1 min + 1 max + optional target.
**Max data points:** 1 value per gauge.

**Design specs:**
- Shape: semi-circle (180 degrees) or 270-degree arc
- Arc width: 16-24px
- Background arc: light gray
- Value arc: colored segment showing current position
- Color: semantic (green/yellow/red zones) or single accent color
- Center label: current value (24-36px bold)
- Needle: optional (adds precision but also decoration)
- Size: 120-200px diameter

**Accessibility:** Alt text: "Gauge showing [metric] at [value] out of [max]. Status: [good/warning/critical]."

**Visual description:** A semicircular arc with a colored segment indicating the current value's position between minimum and maximum.

---

### 10.2 Calendar Heatmap

**When to use:** Show daily data over months or years. Activity frequency, contribution history (GitHub-style), daily metrics.
**When NOT to use:** Non-daily time granularity. When day-of-week pattern is irrelevant.
**Data shape:** Date + 1 quantitative measure.
**Max data points:** 365+ days.

**Design specs:**
- Grid: 7 rows (days of week) x 52-53 columns (weeks of year)
- Cell size: 12-16px squares
- Cell gap: 2-3px
- Color: sequential palette (light for low, dark for high)
- Month labels: along the top, aligned with the first week of each month
- Day labels: Mon, Wed, Fri on the left (alternating to save space)
- Hover: tooltip showing date and exact value
- Legend: gradient scale with value labels

**Accessibility:** Alt text: "Calendar heatmap showing daily [metric] for [year]. Highest: [date] at [value]. Pattern: [weekday/seasonal pattern description]."

**Visual description:** A grid of small colored squares arranged in a calendar pattern. Each square represents one day, with color intensity encoding the metric value. GitHub contribution graph is the canonical example.

---

### 10.3 Timeline

**When to use:** Show events or milestones in chronological order. Project milestones, product history, historical events.
**When NOT to use:** When quantitative values are more important than events (use line chart). Dense continuous data.
**Data shape:** Events with dates + descriptions + optional categories.
**Max data points:** 10-50 events.

**Design specs:**
- Layout: horizontal (events above/below a center line) or vertical (events left/right of a center line)
- Center line: 2px, muted color
- Event markers: circles (radius 6-8px) on the timeline
- Event cards: connected to markers with thin lines, showing date + title + optional description
- Alternating: cards alternate above/below (horizontal) or left/right (vertical) to save space
- Color: by category (if events have types)
- Zoom: support for long timelines

**Accessibility:** Alt text: "Timeline showing [N] events from [start date] to [end date]. Key events: [list of 2-3 most important]."

**Visual description:** A horizontal or vertical line with event markers placed at chronological positions. Cards beside each marker provide event details.

---

### 10.4 Gantt Chart

**When to use:** Show project schedules, task duration, dependencies, and milestones. Project management visualization.
**When NOT to use:** Simple event lists (use timeline). Non-temporal data.
**Data shape:** Tasks with start date, end date, optional dependencies, optional progress percentage.
**Max data points:** 20-100 tasks.

**Design specs:**
- Y-axis: task names (left-aligned, 13-14px)
- X-axis: time scale (days, weeks, months)
- Bars: horizontal bars from start to end date, height 20-28px
- Bar fill: categorical color by phase/category, or single accent color
- Progress: filled portion of bar (darker shade) showing completion
- Dependencies: arrow lines from predecessor end to successor start
- Milestones: diamond markers on the timeline
- Today line: vertical dashed line at current date (red or accent color)
- Grid: vertical gridlines at time intervals, opacity 0.1

**Accessibility:** Alt text: "Gantt chart showing [N] tasks from [start] to [end]. Critical path: [list]. [N] tasks completed, [N] in progress."

**Visual description:** Horizontal bars along a time axis, one per task. Bar length shows task duration. Arrows show dependencies. A vertical "today" line marks current progress.

---

### 10.5 Candlestick Chart

**When to use:** Show financial price movement (open, high, low, close) over time periods. Stock prices, forex, commodities.
**When NOT to use:** Non-financial data. When only close price matters (use line chart). General audiences unfamiliar with financial charts.
**Data shape:** Date + open + high + low + close per period.
**Max data points:** 50-200 periods.

**Design specs:**
- Body: rectangle from open to close price
- Body color: green/white (close > open, bullish) or red/black (close < open, bearish)
- Wicks: thin lines (1px) from body to high (top) and body to low (bottom)
- Body width: 6-12px, gap 2-4px between candles
- Volume: optional histogram below the candlestick chart (separate y-axis)
- Moving averages: optional overlay lines (e.g., 20-day, 50-day)

**Accessibility:** Alt text: "Candlestick chart for [asset] from [start] to [end]. Trend: [bullish/bearish/sideways]. Range: [low] to [high]."

**Visual description:** Vertical rectangles (bodies) with thin lines (wicks) extending above and below. Green bodies mean price went up; red means it went down.

---

### 10.6 Progress Bar / Progress Ring

**When to use:** Show completion percentage for a single task or metric. File upload, onboarding completion, goal progress.
**When NOT to use:** Comparing multiple metrics (use bullet chart). When showing distribution.
**Data shape:** 1 percentage value (0-100%).
**Max data points:** 1.

**Design specs (bar):**
- Track: full-width rectangle, light gray fill (#e5e7eb), height 8-12px, border-radius 99px
- Fill: accent color, same height as track, border-radius 99px, width = percentage
- Label: percentage text above or beside the bar (14px, font-weight 600)
- Milestones: optional tick marks at 25%/50%/75%

**Design specs (ring):**
- Track: circle arc, 6-12px stroke width, light gray
- Fill: circle arc, same stroke width, accent color, dasharray for percentage
- Center: percentage text (24-32px bold)
- Size: 60-120px diameter

**Accessibility:** Alt text: "[metric] progress: [X]% complete." Use `role="progressbar"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax`.

**Visual description:** A horizontal bar (or circular ring) partially filled with color to show progress toward completion.

---

### 10.7 Heatmap (Data Matrix)

**When to use:** Show patterns in a matrix of values. Time x category, feature comparison, schedule visualization. Day-of-week x hour-of-day patterns.
**When NOT to use:** When the matrix is sparse. When individual cell values matter more than the pattern.
**Data shape:** 2 categorical dimensions + 1 quantitative measure.
**Max data points:** 500-5000 cells.

**Design specs:**
- Cells: uniform squares or rectangles, 20-40px
- Cell gap: 1-2px
- Color: sequential palette (low = light, high = dark) or diverging
- Row labels: left side, 11-12px
- Column labels: top, 11-12px (rotated if needed)
- Value label: optional, inside cell (if cell is >= 30px)
- Hover: cell outline + tooltip with exact value
- Legend: horizontal color scale below or beside

**Accessibility:** Alt text: "Heatmap showing [metric] by [row dimension] and [column dimension]. Hottest cell: [row] x [col] at [value]. Coldest: [row] x [col] at [value]."

**Visual description:** A grid of colored cells where color intensity represents values. Rows and columns represent two dimensions, revealing patterns at their intersections.

---

### 10.8 Waterfall Chart

**When to use:** Show how a starting value is affected by a series of positive and negative intermediate values to arrive at a final total. Financial bridge, budget build-up/breakdown.
**When NOT to use:** When there is no meaningful running total. Non-sequential contributions.
**Data shape:** Ordered categories + positive/negative values + start total + end total.
**Max data points:** 5-15 bars.

**Design specs:**
- Start and end bars: grounded to baseline (touching x-axis), dark color
- Intermediate bars: floating (connected by thin lines showing the running total)
- Positive values: green fill (#16a34a)
- Negative values: red fill (#dc2626)
- Connector lines: thin gray lines between bars (1px) showing continuity
- Value labels: above bars (positive) or below bars (negative)

**Accessibility:** Alt text: "Waterfall chart showing how [start metric] of [value] changes through [N] factors to reach [end metric] of [value]. Largest increase: [factor]. Largest decrease: [factor]."

**Visual description:** A series of floating and grounded bars. Bars step up (green) or down (red) from the previous running total, connected by thin lines. Start and end bars sit on the baseline.

---

### 10.9 Dumbbell Chart

**When to use:** Compare two values per category (e.g., male vs female, 2024 vs 2025, actual vs target). Highlights the gap between two measures.
**When NOT to use:** When there is only one value per category (use dot plot or bar). More than 2 values per category.
**Data shape:** 1 categorical + 2 quantitative measures.
**Max data points:** 15-25 categories.

**Design specs:**
- Two dots per row: one for each measure, different colors (radius 5-6px)
- Connecting line between dots: 2px, gray
- Horizontal orientation (categories on y-axis)
- Sort: by gap size or by one of the values
- Legend: identifies which dot color represents which measure

**Accessibility:** Alt text: "Dumbbell chart comparing [measure1] and [measure2] across [N] categories. Largest gap: [category] with [value1] vs [value2]."

**Visual description:** Horizontal rows with two dots connected by a line. The distance between dots shows the gap between two values for each category.

---

### 10.10 Sparkline Variants

**Bar sparkline:** Tiny bar chart in a table cell. Shows distribution or comparison inline.
**Win/loss sparkline:** Binary up/down bars (equal height). Shows sequence of wins and losses.
**Dot sparkline:** Highlights specific data points (max, min, first, last) in a tiny chart.

**All sparkline specs:**
- Width: 60-120px
- Height: 20-32px
- No axes, no labels, no gridlines
- Color: single accent color or semantic color (green/red)
- Embed in table cells, KPI cards, or inline with text

---

## Quick Reference: Chart Selection Cheat Sheet

| I want to show... | Use this chart |
|-------------------|----------------|
| Values by category | Bar chart (horizontal for >7 categories) |
| Trend over time | Line chart |
| Parts of a whole (few parts) | Donut chart |
| Parts of a whole (many parts) | Treemap |
| Distribution of one variable | Histogram |
| Distribution comparison | Box plot or Violin |
| Two-variable relationship | Scatter plot |
| Three-variable relationship | Bubble chart |
| Flow from source to target | Sankey diagram |
| Progress toward goal | Bullet chart or Progress bar |
| Performance vs target | Bullet chart |
| Single KPI with trend | KPI card + Sparkline |
| Geographic data by region | Choropleth map |
| Geographic data by point | Bubble map |
| Hierarchical breakdown | Treemap or Sunburst |
| Project schedule | Gantt chart |
| Financial price movement | Candlestick chart |
| Change from start to end | Waterfall chart |
| Before vs after comparison | Slope chart or Dumbbell chart |
| Daily activity over a year | Calendar heatmap |
| Two values across a matrix | Heatmap |
| Event chronology | Timeline |
| Multi-variable profile | Radar chart (with caution) |
