# Data Visualization Accessibility

> Alt text patterns for every chart type, data table alternatives, 8 colorblind-safe palettes with hex codes, pattern fills, high contrast mode, screen reader announcements, keyboard navigation, sonification, and WCAG success criteria mapping.

---

## 1. WCAG Success Criteria for Data Visualization

### Critical Criteria

| Criterion | Level | Requirement for Dataviz |
|-----------|-------|------------------------|
| **1.1.1 Non-text Content** | A | Every chart must have a text alternative (alt text or data table) |
| **1.3.1 Info and Relationships** | A | Data relationships conveyed visually must also be conveyed programmatically |
| **1.4.1 Use of Color** | A | Color must not be the only means of conveying information |
| **1.4.3 Contrast (Minimum)** | AA | Text in charts must have 4.5:1 contrast (3:1 for large text) |
| **1.4.11 Non-text Contrast** | AA | Chart elements (bars, lines, points) must have 3:1 contrast against background |
| **2.1.1 Keyboard** | A | All interactive chart functionality must be operable via keyboard |
| **2.4.3 Focus Order** | A | Keyboard focus order must be logical |
| **4.1.2 Name, Role, Value** | A | Interactive chart elements must have accessible names and roles |

### Enhanced Criteria

| Criterion | Level | Requirement for Dataviz |
|-----------|-------|------------------------|
| **1.3.2 Meaningful Sequence** | A | Reading order of chart elements must make sense |
| **1.4.6 Contrast (Enhanced)** | AAA | 7:1 contrast for text, 4.5:1 for large text |
| **2.1.3 Keyboard (No Exception)** | AAA | No keyboard traps in interactive charts |
| **2.4.7 Focus Visible** | AA | Focus indicator visible when navigating charts by keyboard |

---

## 2. Alt Text Patterns by Chart Type

### 2.1 General Alt Text Formula

```
[Chart type] showing [what is measured] by [dimensions].
[Key insight or trend in 1-2 sentences].
[Extremes: highest and lowest values if relevant].
```

**Rules:**
- Describe the INSIGHT, not just the structure ("Revenue grew 23% year over year" not "A bar chart with bars")
- Keep alt text under 150 words for simple charts
- For complex charts, use a brief alt text + link to a data table
- Never start with "Image of..." or "Chart showing..." -- start with the chart type directly

### 2.2 Patterns by Chart Type

**Bar Chart:**
```
Bar chart comparing [metric] across [N] [categories].
[Category] leads at [value], followed by [category] at [value].
[Optional: notable gap or pattern].
```
Example: "Bar chart comparing quarterly revenue across 4 regions. North America leads at $4.2M, followed by Europe at $2.8M, Asia at $1.9M, and South America at $0.8M."

**Line Chart:**
```
Line chart showing [metric] from [start date] to [end date].
Trend: [description of overall direction and notable changes].
Range: [minimum value] to [maximum value].
```
Example: "Line chart showing daily active users from January to December 2025. Trend: steady growth from 12K to 28K with a sharp spike to 45K in November during the product launch. Range: 11.2K to 45.1K."

**Pie/Donut Chart:**
```
[Pie/Donut] chart showing the breakdown of [whole] by [category].
Largest segment: [name] at [percentage].
Other segments: [list remaining with percentages].
```
Example: "Donut chart showing revenue breakdown by product line. Largest segment: Enterprise at 45%. Other segments: Pro at 28%, Starter at 18%, Free at 9%."

**Scatter Plot:**
```
Scatter plot showing the relationship between [X variable] and [Y variable]
for [N] [entities]. Pattern: [positive/negative/no correlation].
[Notable outliers or clusters if any].
```
Example: "Scatter plot showing the relationship between marketing spend and customer acquisition for 48 campaigns. Pattern: moderate positive correlation. Two outliers show high acquisition despite low spend, suggesting viral campaigns."

**Treemap:**
```
Treemap showing [metric] across [N] [categories] with [N] hierarchy levels.
Largest: [name] at [value] ([percentage] of total).
[Key structural insight].
```
Example: "Treemap showing global app revenue across 120 apps in 8 categories. Largest: Social category at $12.4B (34% of total). Gaming is second at $8.9B. Within Social, three apps account for 78% of the category."

**Heatmap:**
```
Heatmap showing [metric] by [row dimension] and [column dimension].
Highest: [row] x [column] at [value].
Lowest: [row] x [column] at [value].
[Pattern description].
```
Example: "Heatmap showing website traffic by day of week and hour. Highest: Tuesday at 2pm with 12,400 visitors. Lowest: Sunday at 4am with 230 visitors. Weekday afternoons consistently show the highest traffic."

**Stacked Area Chart:**
```
Stacked area chart showing [total metric] from [start] to [end],
broken into [N] components: [list].
Total grew from [start value] to [end value].
[Key composition change].
```

**Sankey Diagram:**
```
Sankey diagram showing flow from [source description] to [destination description].
[N] source categories flow into [N] destination categories.
Largest flow: [source] to [destination] at [value].
[Key flow pattern].
```

**Funnel Chart:**
```
Funnel chart showing [process] conversion through [N] stages.
Start: [value] at [first stage].
End: [value] at [last stage].
Overall conversion rate: [percentage].
Biggest drop-off: [stage to stage] at [percentage] loss.
```

**Box Plot:**
```
Box plot comparing distribution of [metric] across [N] [categories].
[Category] has highest median at [value] (range: [min]-[max]).
[Category] shows most variability (IQR: [value]).
```

**Radar Chart:**
```
Radar chart comparing [entity/entities] across [N] dimensions: [list].
[Entity] scores highest in [dimension] and lowest in [dimension].
[Comparison insight if multiple entities].
```

**Gauge:**
```
Gauge showing [metric] at [current value] out of [maximum].
Status: [qualitative assessment]. Target: [target value].
```

**Calendar Heatmap:**
```
Calendar heatmap showing daily [metric] for [time period].
Highest day: [date] at [value].
[Weekly/seasonal pattern description].
Average: [value] per day.
```

**KPI Card:**
```
[Metric name]: [current value].
Change: [delta] compared to [comparison period].
Trend: [direction based on sparkline].
```

---

## 3. Data Table Alternatives

Every chart should have a data table alternative accessible to screen readers. Two approaches:

### 3.1 Visually Hidden Data Table

```html
<figure role="figure" aria-label="Revenue by region chart">
  <!-- The visible chart -->
  <div class="chart" role="img" aria-describedby="chart-data-1">
    <!-- Chart SVG/Canvas -->
  </div>

  <!-- Visually hidden but accessible data table -->
  <table id="chart-data-1" class="sr-only">
    <caption>Revenue by region, Q1 2026</caption>
    <thead>
      <tr>
        <th scope="col">Region</th>
        <th scope="col">Revenue</th>
        <th scope="col">Change vs Prior Quarter</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>North America</td><td>$4,200,000</td><td>+12.3%</td></tr>
      <tr><td>Europe</td><td>$2,800,000</td><td>+8.1%</td></tr>
      <tr><td>Asia</td><td>$1,900,000</td><td>+15.7%</td></tr>
      <tr><td>South America</td><td>$800,000</td><td>-2.4%</td></tr>
    </tbody>
  </table>
</figure>
```

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

### 3.2 Expandable Data Table

```html
<div class="chart-with-table">
  <div class="chart"><!-- Chart here --></div>
  <button class="show-data-button"
          aria-expanded="false"
          aria-controls="chart-data-table">
    View data table
  </button>
  <div id="chart-data-table" class="chart-data-panel" hidden>
    <table><!-- Full data table --></table>
  </div>
</div>
```

**Behavior:** "View data table" link below the chart. Toggles a visible data table. Useful for sighted users who want exact values too.

### 3.3 Summary Text + Table

For complex charts (Sankey, treemap, network), provide:
1. A brief text summary (2-3 sentences) as `aria-label`
2. A complete data table as the accessible alternative
3. Both the summary and table linked via `aria-describedby`

---

## 4. Colorblind-Safe Palettes

### 4.1 Palette 1: Tableau 10 (Categorical, 8 colors)

Tested against protanopia, deuteranopia, and tritanopia. Most widely validated categorical palette.

```
#4e79a7  Blue (Steel)
#f28e2b  Orange
#e15759  Red (Muted)
#76b7b2  Teal
#59a14f  Green
#edc948  Yellow
#b07aa1  Purple
#ff9da7  Pink
```

### 4.2 Palette 2: IBM Carbon (Categorical, 8 colors)

Designed by IBM for accessibility. High contrast between adjacent colors.

```
#6929c4  Purple
#1192e8  Cyan
#005d5d  Teal (Dark)
#9f1853  Magenta
#fa4d56  Red
#570408  Maroon
#198038  Green
#002d9c  Blue (Dark)
```

### 4.3 Palette 3: ColorBrewer Set2 (Categorical, 8 colors)

Designed by Cynthia Brewer for cartography. Soft, pastel tones with good distinguishability.

```
#66c2a5  Teal
#fc8d62  Salmon
#8da0cb  Periwinkle
#e78ac3  Pink
#a6d854  Lime
#ffd92f  Yellow
#e5c494  Tan
#b3b3b3  Gray
```

### 4.4 Palette 4: Wong (Categorical, 8 colors)

Proposed by Bang Wong (Nature Methods). Optimized for all three types of color vision deficiency.

```
#000000  Black
#e69f00  Orange
#56b4e9  Sky Blue
#009e73  Bluish Green
#f0e442  Yellow
#0072b2  Blue
#d55e00  Vermillion
#cc79a7  Reddish Purple
```

### 4.5 Palette 5: Okabe-Ito (Categorical, 8 colors)

Designed by Masataka Okabe and Kei Ito. Universally distinguishable.

```
#e69f00  Orange
#56b4e9  Sky Blue
#009e73  Bluish Green
#f0e442  Yellow
#0072b2  Blue
#d55e00  Vermillion
#cc79a7  Reddish Purple
#999999  Gray
```

### 4.6 Palette 6: Viridis (Sequential, 8 steps)

Perceptually uniform sequential palette. Works in grayscale. Colorblind-safe.

```
#440154  Dark Purple
#46327e  Purple
#365c8d  Blue
#277f8e  Teal
#1fa187  Green-Teal
#4ac16d  Green
#9fda3a  Yellow-Green
#fde725  Yellow
```

### 4.7 Palette 7: Cividis (Sequential, 8 steps)

Designed specifically for color vision deficiency. Perceptually uniform. Blue-to-yellow.

```
#00204d  Dark Navy
#00336e  Navy
#39486b  Blue-Gray
#5f5f65  Gray
#868055  Olive
#b3a136  Gold
#d6c73b  Yellow
#fde725  Bright Yellow
```

### 4.8 Palette 8: RdBu Diverging (Diverging, 9 steps)

Red-to-Blue diverging palette. Safe for protanopia and deuteranopia because it relies on lightness difference, not just hue.

```
#b2182b  Dark Red
#d6604d  Red
#f4a582  Light Red
#fddbc7  Very Light Red
#f7f7f7  White (neutral)
#d1e5f0  Very Light Blue
#92c5de  Light Blue
#4393c3  Blue
#2166ac  Dark Blue
```

---

## 5. Pattern Fills for Color Alternatives

When color alone is insufficient, add patterns to chart fills:

### 5.1 SVG Pattern Definitions

```svg
<defs>
  <!-- Diagonal lines (right) -->
  <pattern id="pattern-diagonal-right" patternUnits="userSpaceOnUse"
           width="8" height="8" patternTransform="rotate(45)">
    <line x1="0" y1="0" x2="0" y2="8" stroke="currentColor"
          stroke-width="2" opacity="0.4"/>
  </pattern>

  <!-- Diagonal lines (left) -->
  <pattern id="pattern-diagonal-left" patternUnits="userSpaceOnUse"
           width="8" height="8" patternTransform="rotate(-45)">
    <line x1="0" y1="0" x2="0" y2="8" stroke="currentColor"
          stroke-width="2" opacity="0.4"/>
  </pattern>

  <!-- Dots -->
  <pattern id="pattern-dots" patternUnits="userSpaceOnUse"
           width="8" height="8">
    <circle cx="4" cy="4" r="1.5" fill="currentColor" opacity="0.4"/>
  </pattern>

  <!-- Horizontal lines -->
  <pattern id="pattern-horizontal" patternUnits="userSpaceOnUse"
           width="8" height="8">
    <line x1="0" y1="4" x2="8" y2="4" stroke="currentColor"
          stroke-width="2" opacity="0.4"/>
  </pattern>

  <!-- Vertical lines -->
  <pattern id="pattern-vertical" patternUnits="userSpaceOnUse"
           width="8" height="8">
    <line x1="4" y1="0" x2="4" y2="8" stroke="currentColor"
          stroke-width="2" opacity="0.4"/>
  </pattern>

  <!-- Cross-hatch -->
  <pattern id="pattern-crosshatch" patternUnits="userSpaceOnUse"
           width="8" height="8">
    <line x1="0" y1="4" x2="8" y2="4" stroke="currentColor"
          stroke-width="1.5" opacity="0.4"/>
    <line x1="4" y1="0" x2="4" y2="8" stroke="currentColor"
          stroke-width="1.5" opacity="0.4"/>
  </pattern>

  <!-- Zigzag -->
  <pattern id="pattern-zigzag" patternUnits="userSpaceOnUse"
           width="12" height="8">
    <polyline points="0,8 3,0 6,8 9,0 12,8" fill="none"
              stroke="currentColor" stroke-width="1.5" opacity="0.4"/>
  </pattern>

  <!-- Waves -->
  <pattern id="pattern-waves" patternUnits="userSpaceOnUse"
           width="12" height="8">
    <path d="M0,4 Q3,0 6,4 Q9,8 12,4" fill="none"
          stroke="currentColor" stroke-width="1.5" opacity="0.4"/>
  </pattern>
</defs>
```

### 5.2 Applying Patterns

```css
/* Apply pattern as secondary fill on top of color */
.bar-series-1 { fill: #4e79a7; }
.bar-series-1.with-pattern { fill: url(#pattern-diagonal-right); }

.bar-series-2 { fill: #f28e2b; }
.bar-series-2.with-pattern { fill: url(#pattern-dots); }
```

**Rules:**
- Use patterns IN ADDITION to color, not instead of color
- 8 distinct patterns are enough to match 8 categorical colors
- Patterns should be subtle (low opacity) -- they supplement, not replace
- Offer a toggle: "Show patterns" for users who need them
- In print mode, always show patterns (printer may not reproduce color accurately)

---

## 6. High Contrast Mode

### 6.1 Windows High Contrast Detection

```css
@media (forced-colors: active) {
  .chart-bar,
  .chart-line,
  .chart-point {
    forced-color-adjust: none;
  }

  .chart-gridline {
    stroke: CanvasText;
    opacity: 0.2;
  }

  .chart-axis-label {
    fill: CanvasText;
  }

  .chart-bar {
    stroke: CanvasText;
    stroke-width: 1px;
  }

  .chart-tooltip {
    background: Canvas;
    color: CanvasText;
    border: 2px solid CanvasText;
  }
}
```

### 6.2 Custom High Contrast Theme

```css
[data-contrast="high"] {
  --dataviz-categorical-1: #0000ff;
  --dataviz-categorical-2: #ff0000;
  --dataviz-categorical-3: #008000;
  --dataviz-categorical-4: #ff00ff;
  --dataviz-categorical-5: #000000;
  --dataviz-categorical-6: #ff8c00;
  --dataviz-categorical-7: #00ced1;
  --dataviz-categorical-8: #8b4513;

  --dataviz-grid-color: #000000;
  --dataviz-grid-opacity: 0.3;
  --dataviz-axis-color: #000000;
  --dataviz-line-width: 3px;
  --dataviz-point-radius: 6px;
  --dataviz-bar-radius: 0;
}
```

**Rules:**
- Increase line thickness from 2px to 3px
- Increase point radius from 4px to 6px
- Use maximum saturation colors
- Add solid borders to all chart elements (bars, areas)
- Increase gridline opacity from 0.15 to 0.3
- Remove decorative elements (rounded corners, shadows)

---

## 7. Screen Reader Announcements

### 7.1 Chart Region

```html
<div role="figure" aria-label="Revenue trend chart showing monthly revenue from January to December 2025, growing from $1.2M to $2.4M">
  <div role="img" aria-describedby="chart-description chart-data-table">
    <!-- SVG/Canvas chart rendering -->
  </div>
  <div id="chart-description" class="sr-only">
    Monthly revenue trend showing consistent growth with a year-over-year increase of 100%.
    Peak month: November at $2.6M. Lowest month: February at $1.1M.
  </div>
</div>
```

### 7.2 Interactive Chart Announcements

When users interact with chart elements, announce changes via ARIA live regions:

```html
<div aria-live="polite" aria-atomic="true" class="sr-only" id="chart-announcer">
  <!-- JavaScript updates this content on interaction -->
</div>
```

```javascript
// When user hovers/focuses a data point
function announceDataPoint(point) {
  const announcer = document.getElementById('chart-announcer');
  announcer.textContent = `${point.label}: ${point.value}. ${point.context}`;
}

// Examples of announcements:
// "January: $1.2M revenue. 12% above target."
// "North America: $4.2M. Largest region, 43% of total."
// "Error rate spiked to 5.2% on March 15th. Normal range is 0.5-1.5%."
```

### 7.3 Chart Type Announcements

```javascript
// Announce chart structure when user focuses the chart
function announceChartStructure(chart) {
  const announcer = document.getElementById('chart-announcer');

  switch (chart.type) {
    case 'bar':
      announcer.textContent =
        `Bar chart with ${chart.dataPoints} bars. ` +
        `Use arrow keys to navigate between bars. ` +
        `Press Enter for details.`;
      break;
    case 'line':
      announcer.textContent =
        `Line chart with ${chart.series} series and ${chart.dataPoints} data points. ` +
        `Use left and right arrows to move between points. ` +
        `Use up and down arrows to switch series.`;
      break;
    case 'pie':
      announcer.textContent =
        `Pie chart with ${chart.slices} slices. ` +
        `Use arrow keys to navigate between slices.`;
      break;
  }
}
```

---

## 8. Keyboard Navigation in Charts

### 8.1 Navigation Patterns

**Bar Chart:**
- Left/Right: move between bars
- Up/Down: (grouped bar) switch between groups
- Enter: drill down or show details
- Escape: return to chart level

**Line Chart:**
- Left/Right: move between data points along the line
- Up/Down: switch between series (multi-series)
- Home/End: first/last data point

**Pie/Donut Chart:**
- Left/Right: move between slices (clockwise/counter-clockwise)
- Enter: drill down into slice

**Scatter Plot:**
- Arrow keys: move to nearest data point in that direction
- Tab: move to next notable point (outlier, cluster center)
- Enter: show details for current point

**Treemap:**
- Arrow keys: navigate between cells
- Enter: drill into cell (zoom to children)
- Escape: zoom back out

### 8.2 Focus Indicators

```css
/* High-visibility focus ring for chart elements */
.chart-element:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 2px;
}

/* For SVG elements that cannot use outline */
.chart-element-svg:focus-visible {
  stroke: #2563eb;
  stroke-width: 3px;
  stroke-dasharray: none;
}

/* Animated focus pulse for visibility */
@keyframes focus-pulse {
  0%, 100% { outline-color: #2563eb; }
  50% { outline-color: #93c5fd; }
}

.chart-element:focus-visible {
  animation: focus-pulse 1.5s ease-in-out infinite;
}
```

### 8.3 Implementation Pattern

```html
<svg role="img" aria-label="Bar chart of revenue by region">
  <g role="list" aria-label="Data bars">
    <rect role="listitem"
          tabindex="0"
          aria-label="North America: $4.2M, 43% of total"
          x="10" y="20" width="40" height="180"
          class="chart-bar" />
    <rect role="listitem"
          tabindex="-1"
          aria-label="Europe: $2.8M, 29% of total"
          x="60" y="80" width="40" height="120"
          class="chart-bar" />
    <!-- More bars -->
  </g>
</svg>
```

**Roving tabindex:** Only the currently focused element has `tabindex="0"`. All others have `tabindex="-1"`. Arrow keys move `tabindex="0"` to the next element.

---

## 9. Sonification (Audio Data Representation)

### 9.1 What is Sonification?

Sonification maps data values to audio properties (pitch, volume, tempo, timbre). It enables blind and low-vision users to perceive data patterns through sound.

### 9.2 Mapping Strategies

| Data Property | Audio Property | Example |
|--------------|----------------|---------|
| Value (magnitude) | Pitch | Higher values = higher pitch |
| Time | Left-to-right playback | Play notes in chronological order |
| Category | Instrument/timbre | Different sounds for different series |
| Threshold crossing | Alert tone | Beep when value exceeds target |
| Missing data | Silence | Gap in the audio sequence |

### 9.3 Implementation Approach

```javascript
// Using the Web Audio API for basic sonification
function sonifyLineChart(dataPoints, options = {}) {
  const audioCtx = new AudioContext();
  const {
    duration = 3000,        // Total playback time in ms
    minFreq = 200,          // Frequency for minimum value
    maxFreq = 800,          // Frequency for maximum value
    waveType = 'sine',      // Oscillator type
  } = options;

  const minVal = Math.min(...dataPoints.map(d => d.value));
  const maxVal = Math.max(...dataPoints.map(d => d.value));
  const timeStep = duration / dataPoints.length / 1000;

  dataPoints.forEach((point, index) => {
    const oscillator = audioCtx.createOscillator();
    const gainNode = audioCtx.createGain();

    // Map value to frequency
    const normalizedValue = (point.value - minVal) / (maxVal - minVal);
    const frequency = minFreq + normalizedValue * (maxFreq - minFreq);

    oscillator.type = waveType;
    oscillator.frequency.value = frequency;

    gainNode.gain.value = 0.1; // Low volume

    oscillator.connect(gainNode);
    gainNode.connect(audioCtx.destination);

    const startTime = audioCtx.currentTime + index * timeStep;
    oscillator.start(startTime);
    oscillator.stop(startTime + timeStep * 0.9);
  });
}
```

### 9.4 Sonification Best Practices

1. **Provide a play button** -- never auto-play sonification
2. **Allow speed control** -- slower for detail, faster for overview
3. **Announce the mapping** before playing: "Higher pitch means higher revenue"
4. **Provide stop/pause controls** -- users must be able to halt playback
5. **Combine with announcements** -- "Playing 12 months of revenue data. Trend: ascending."
6. **Use for trend perception** -- sonification excels at overall shape (up, down, flat, volatile)
7. **Not a replacement for data tables** -- sonification supplements, does not replace text alternatives

---

## 10. Reduced Motion

### 10.1 Respecting prefers-reduced-motion

```css
@media (prefers-reduced-motion: reduce) {
  /* Disable chart animations */
  .chart-bar,
  .chart-line,
  .chart-area,
  .chart-point,
  .chart-slice {
    animation: none !important;
    transition: none !important;
  }

  /* Keep essential state changes instantaneous */
  .chart-tooltip {
    transition: opacity 0ms !important;
  }

  /* Disable loading shimmer */
  .chart-loading {
    animation: none !important;
    background: #f3f4f6 !important;
  }

  /* Disable auto-scrolling carousels */
  .chart-carousel {
    scroll-behavior: auto !important;
  }
}
```

### 10.2 What to Keep vs Remove

**Remove:** Entry animations (bars growing, lines drawing), spinning loaders, bouncing elements, auto-playing transitions.
**Keep:** Instant state changes (hover highlight on/off), opacity changes (as long as they are instant), color changes (no transition needed).

---

## 11. Text Sizing and Zoom

### 11.1 Supporting 200% Zoom

```css
/* Use relative units for chart text */
.chart-title       { font-size: 1rem; }
.chart-axis-label  { font-size: 0.75rem; }
.chart-tooltip     { font-size: 0.875rem; }
.chart-data-label  { font-size: 0.6875rem; }

/* Ensure chart containers respond to zoom */
.chart-container {
  min-height: 15rem; /* Scales with zoom */
  width: 100%;
}
```

**Rules:**
- Text in charts must remain readable at 200% browser zoom
- Charts should reflow or resize, not just clip or overflow
- Test with browser zoom at 200% and 400%
- Container queries help charts adapt to their available space

---

## 12. Focus Management for Dashboard Navigation

### 12.1 Dashboard Landmark Structure

```html
<main aria-label="Analytics dashboard">
  <section aria-label="Key performance indicators">
    <!-- KPI cards -->
  </section>

  <section aria-label="Revenue charts">
    <!-- Chart cards -->
  </section>

  <section aria-label="Data tables">
    <!-- Tables -->
  </section>
</main>
```

### 12.2 Chart Card Focus Order

```
1. Chart card (focusable container)
2. Chart title link (if clickable)
3. Chart action buttons (expand, download, options)
4. Chart interactive area (enter to navigate data points)
5. Legend items (if toggleable)
6. "View data table" link
7. Next chart card
```

### 12.3 Skip Links

```html
<a href="#main-charts" class="skip-link">Skip to charts</a>
<a href="#data-table" class="skip-link">Skip to data table</a>
```

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  padding: 8px 16px;
  background: #2563eb;
  color: white;
  z-index: 100;
  transition: top 150ms ease;
}

.skip-link:focus {
  top: 0;
}
```

---

## 13. Testing Checklist

### Automated Testing
- [ ] aXe or Lighthouse audit on every dashboard page
- [ ] All images and figures have alt text
- [ ] All interactive elements have accessible names
- [ ] Color contrast ratios meet WCAG AA minimums
- [ ] No ARIA misuse detected

### Manual Screen Reader Testing
- [ ] Chart alt text accurately describes the insight
- [ ] Data table alternative is discoverable and readable
- [ ] Interactive chart elements are navigable
- [ ] Announcements are timely and informative (not noisy)
- [ ] Focus order makes logical sense

### Keyboard Testing
- [ ] Tab reaches the chart area
- [ ] Arrow keys navigate between data points
- [ ] Enter activates drill-down or detail view
- [ ] Escape returns to chart level
- [ ] No keyboard traps
- [ ] Focus indicator is always visible

### Visual Testing
- [ ] Test with Sim Daltonism (macOS) or Color Oracle
- [ ] Protanopia simulation: all series distinguishable
- [ ] Deuteranopia simulation: all series distinguishable
- [ ] Tritanopia simulation: all series distinguishable
- [ ] Grayscale: all series distinguishable by lightness
- [ ] High contrast mode: all elements visible and labeled
- [ ] 200% browser zoom: all text readable, no clipping

### Reduced Motion Testing
- [ ] Enable prefers-reduced-motion
- [ ] Verify no animations play
- [ ] Verify chart is still fully functional
- [ ] Verify tooltips appear instantly (no transition delay)

---

## 14. Common Accessibility Failures and Fixes

| Failure | Impact | Fix |
|---------|--------|-----|
| Chart is a flat image with no alt text | Screen reader users get no information | Add descriptive alt text + hidden data table |
| Color is the only differentiator between series | Colorblind users cannot distinguish series | Add patterns, labels, or shape markers |
| No keyboard access to interactive elements | Keyboard users cannot explore data | Add tabindex, arrow key navigation, focus ring |
| Tooltip only appears on mouse hover | Touch and keyboard users miss information | Show tooltip on focus, long-press on mobile |
| Chart text is too small at 200% zoom | Low vision users cannot read labels | Use relative units (rem), test at 200% |
| Animations distract or cause vertigo | Users with vestibular disorders are affected | Respect prefers-reduced-motion |
| Data table alternative is missing | Screen reader users have no way to access data | Add hidden or expandable data table |
| Auto-playing sonification | Startles users, interferes with screen reader | Require user to press play |
| Poor focus order in dashboard | Keyboard users get lost | Use semantic landmarks and logical tab order |
| Missing aria-sort on table headers | Screen reader users do not know sort state | Add aria-sort attribute, update on sort change |
