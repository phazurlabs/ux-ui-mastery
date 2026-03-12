# Data Visualization Code Patterns

> Production-ready React code for the top 20 chart types using Recharts. Includes chart wrapper component with loading/error/empty states, design tokens, responsive containers, theme integration, tooltip customization, legend design, and print styles.

---

## 1. Design Tokens (CSS Custom Properties)

```css
:root {
  /* Categorical Colors */
  --chart-color-1: #4e79a7;
  --chart-color-2: #f28e2b;
  --chart-color-3: #e15759;
  --chart-color-4: #76b7b2;
  --chart-color-5: #59a14f;
  --chart-color-6: #edc948;
  --chart-color-7: #b07aa1;
  --chart-color-8: #ff9da7;

  /* Sequential Colors (Blue) */
  --chart-seq-1: #f7fbff;
  --chart-seq-2: #deebf7;
  --chart-seq-3: #c6dbef;
  --chart-seq-4: #9ecae1;
  --chart-seq-5: #6baed6;
  --chart-seq-6: #4292c6;
  --chart-seq-7: #2171b5;
  --chart-seq-8: #084594;

  /* Semantic Colors */
  --chart-positive: #16a34a;
  --chart-negative: #dc2626;
  --chart-warning: #d97706;
  --chart-neutral: #6b7280;

  /* Structure */
  --chart-grid: #e5e7eb;
  --chart-grid-opacity: 0.15;
  --chart-axis: #9ca3af;
  --chart-text: #374151;
  --chart-text-muted: #9ca3af;
  --chart-bg: #ffffff;

  /* Tooltip */
  --chart-tooltip-bg: #1f2937;
  --chart-tooltip-text: #f9fafb;
  --chart-tooltip-border: none;
  --chart-tooltip-radius: 6px;
  --chart-tooltip-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);

  /* Typography */
  --chart-font: 'Inter', system-ui, -apple-system, sans-serif;
  --chart-font-mono: 'JetBrains Mono', 'SF Mono', ui-monospace, monospace;

  /* Sizing */
  --chart-min-height: 240px;
  --chart-padding: 20px;
}

/* Dark mode */
[data-theme="dark"] {
  --chart-color-1: #6ba3d6;
  --chart-color-2: #f5a855;
  --chart-color-3: #e87b7d;
  --chart-color-4: #93cec9;
  --chart-color-5: #7dbd72;
  --chart-color-6: #f0d56e;
  --chart-color-7: #c499b8;
  --chart-color-8: #ffb4bc;

  --chart-grid: #374151;
  --chart-axis: #6b7280;
  --chart-text: #e5e7eb;
  --chart-text-muted: #6b7280;
  --chart-bg: #1e293b;

  --chart-tooltip-bg: #f9fafb;
  --chart-tooltip-text: #1f2937;
}
```

### Token Arrays for Recharts

```tsx
// chart-tokens.ts
export const CHART_COLORS = {
  categorical: [
    '#4e79a7', '#f28e2b', '#e15759', '#76b7b2',
    '#59a14f', '#edc948', '#b07aa1', '#ff9da7',
  ],
  categoricalDark: [
    '#6ba3d6', '#f5a855', '#e87b7d', '#93cec9',
    '#7dbd72', '#f0d56e', '#c499b8', '#ffb4bc',
  ],
  sequential: [
    '#f7fbff', '#deebf7', '#c6dbef', '#9ecae1',
    '#6baed6', '#4292c6', '#2171b5', '#084594',
  ],
  diverging: {
    negative: ['#b2182b', '#d6604d', '#f4a582', '#fddbc7'],
    neutral: '#f7f7f7',
    positive: ['#d1e5f0', '#92c5de', '#4393c3', '#2166ac'],
  },
  semantic: {
    positive: '#16a34a',
    negative: '#dc2626',
    warning: '#d97706',
    neutral: '#6b7280',
  },
} as const;

export const CHART_THEME = {
  grid: { stroke: '#e5e7eb', strokeOpacity: 0.15, strokeDasharray: '3 3' },
  axis: { stroke: '#9ca3af', fontSize: 11, fontFamily: 'Inter, system-ui, sans-serif' },
  tooltip: {
    bg: '#1f2937',
    text: '#f9fafb',
    borderRadius: 6,
    boxShadow: '0 4px 12px rgba(0,0,0,0.15)',
  },
  line: { strokeWidth: 2 },
  bar: { radius: [4, 4, 0, 0] as [number, number, number, number] },
  dot: { r: 4, strokeWidth: 2 },
  animation: { duration: 300, easing: 'ease-in-out' },
} as const;
```

---

## 2. Chart Wrapper Component

A universal wrapper that handles loading, error, empty, and responsive states for any chart.

```tsx
// ChartWrapper.tsx
import React, { useRef, useState, useEffect } from 'react';

interface ChartWrapperProps {
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  empty?: boolean;
  emptyMessage?: string;
  onRetry?: () => void;
  height?: number;
  children: React.ReactNode;
  actions?: React.ReactNode;
  className?: string;
}

export function ChartWrapper({
  title,
  subtitle,
  loading = false,
  error,
  empty = false,
  emptyMessage = 'No data available',
  onRetry,
  height = 320,
  children,
  actions,
  className = '',
}: ChartWrapperProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const [containerWidth, setContainerWidth] = useState(0);

  useEffect(() => {
    if (!containerRef.current) return;
    const observer = new ResizeObserver((entries) => {
      for (const entry of entries) {
        setContainerWidth(entry.contentRect.width);
      }
    });
    observer.observe(containerRef.current);
    return () => observer.disconnect();
  }, []);

  return (
    <div
      ref={containerRef}
      className={`chart-card ${className}`}
      role="figure"
      aria-label={title}
      style={{ minHeight: height }}
    >
      {/* Header */}
      <div className="chart-card-header">
        <div>
          <h3 className="chart-card-title">{title}</h3>
          {subtitle && <p className="chart-card-subtitle">{subtitle}</p>}
        </div>
        {actions && <div className="chart-card-actions">{actions}</div>}
      </div>

      {/* Body */}
      <div className="chart-card-body" style={{ height: height - 60 }}>
        {loading && <ChartSkeleton />}
        {error && <ChartError message={error} onRetry={onRetry} />}
        {!loading && !error && empty && (
          <ChartEmpty message={emptyMessage} />
        )}
        {!loading && !error && !empty && children}
      </div>
    </div>
  );
}

function ChartSkeleton() {
  return (
    <div className="chart-skeleton" aria-label="Loading chart data">
      <div className="chart-skeleton-bar" style={{ height: '60%' }} />
      <div className="chart-skeleton-bar" style={{ height: '80%' }} />
      <div className="chart-skeleton-bar" style={{ height: '45%' }} />
      <div className="chart-skeleton-bar" style={{ height: '70%' }} />
      <div className="chart-skeleton-bar" style={{ height: '55%' }} />
    </div>
  );
}

function ChartError({
  message,
  onRetry,
}: {
  message: string;
  onRetry?: () => void;
}) {
  return (
    <div className="chart-error" role="alert">
      <p className="chart-error-title">Unable to load chart</p>
      <p className="chart-error-description">{message}</p>
      {onRetry && (
        <button className="chart-error-retry" onClick={onRetry}>
          Try again
        </button>
      )}
    </div>
  );
}

function ChartEmpty({ message }: { message: string }) {
  return (
    <div className="chart-empty">
      <svg
        className="chart-empty-icon"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth={1.5}
      >
        <path d="M3 3v18h18" />
        <path d="M7 16l4-4 4 4 6-6" />
      </svg>
      <p className="chart-empty-title">No data</p>
      <p className="chart-empty-description">{message}</p>
    </div>
  );
}
```

### Chart Wrapper CSS

```css
.chart-card {
  background: var(--chart-bg, white);
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  overflow: hidden;
}

.chart-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 16px 20px 0;
}

.chart-card-title {
  font-size: 16px;
  font-weight: 600;
  color: var(--chart-text, #111827);
  margin: 0;
}

.chart-card-subtitle {
  font-size: 13px;
  color: var(--chart-text-muted, #6b7280);
  margin: 2px 0 0;
}

.chart-card-actions {
  display: flex;
  gap: 8px;
}

.chart-card-body {
  padding: 12px 20px 20px;
  position: relative;
}

/* Skeleton */
.chart-skeleton {
  display: flex;
  align-items: flex-end;
  gap: 8px;
  height: 100%;
  padding: 20px 0;
}

.chart-skeleton-bar {
  flex: 1;
  border-radius: 4px 4px 0 0;
  background: linear-gradient(90deg, #f3f4f6 25%, #e5e7eb 50%, #f3f4f6 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
}

@keyframes shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Error */
.chart-error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
  padding: 24px;
}

.chart-error-title {
  font-size: 15px;
  font-weight: 600;
  color: #991b1b;
  margin: 0 0 4px;
}

.chart-error-description {
  font-size: 13px;
  color: #b91c1c;
  margin: 0 0 16px;
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

/* Empty */
.chart-empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
  padding: 24px;
}

.chart-empty-icon {
  width: 48px;
  height: 48px;
  color: #d1d5db;
  margin-bottom: 12px;
}

.chart-empty-title {
  font-size: 15px;
  font-weight: 600;
  color: #374151;
  margin: 0 0 4px;
}

.chart-empty-description {
  font-size: 13px;
  color: #9ca3af;
  margin: 0;
  max-width: 240px;
}
```

---

## 3. Custom Tooltip Component

```tsx
// ChartTooltip.tsx
import React from 'react';

interface TooltipPayload {
  name: string;
  value: number;
  color: string;
  dataKey: string;
}

interface ChartTooltipProps {
  active?: boolean;
  payload?: TooltipPayload[];
  label?: string;
  formatter?: (value: number, name: string) => string;
  labelFormatter?: (label: string) => string;
}

export function ChartTooltip({
  active,
  payload,
  label,
  formatter,
  labelFormatter,
}: ChartTooltipProps) {
  if (!active || !payload?.length) return null;

  const displayLabel = labelFormatter ? labelFormatter(String(label)) : label;

  return (
    <div className="chart-tooltip" role="tooltip">
      {displayLabel && (
        <p className="chart-tooltip-label">{displayLabel}</p>
      )}
      <div className="chart-tooltip-items">
        {payload.map((entry, index) => (
          <div key={index} className="chart-tooltip-item">
            <span
              className="chart-tooltip-dot"
              style={{ backgroundColor: entry.color }}
            />
            <span className="chart-tooltip-name">{entry.name}</span>
            <span className="chart-tooltip-value">
              {formatter
                ? formatter(entry.value, entry.name)
                : entry.value.toLocaleString()}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
```

### Tooltip CSS

```css
.chart-tooltip {
  background: var(--chart-tooltip-bg, #1f2937);
  color: var(--chart-tooltip-text, #f9fafb);
  border-radius: var(--chart-tooltip-radius, 6px);
  padding: 8px 12px;
  box-shadow: var(--chart-tooltip-shadow, 0 4px 12px rgba(0,0,0,0.15));
  font-family: var(--chart-font, 'Inter', system-ui, sans-serif);
  font-size: 13px;
  line-height: 1.4;
  max-width: 240px;
  pointer-events: none;
}

.chart-tooltip-label {
  font-weight: 600;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.7);
  margin: 0 0 6px;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.chart-tooltip-items {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.chart-tooltip-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.chart-tooltip-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.chart-tooltip-name {
  flex: 1;
  color: rgba(255, 255, 255, 0.8);
}

.chart-tooltip-value {
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  color: white;
}
```

---

## 4. Custom Legend Component

```tsx
// ChartLegend.tsx
import React from 'react';

interface LegendItem {
  value: string;
  color: string;
  inactive?: boolean;
}

interface ChartLegendProps {
  payload?: LegendItem[];
  onClick?: (item: LegendItem) => void;
  align?: 'left' | 'center' | 'right';
}

export function ChartLegend({
  payload = [],
  onClick,
  align = 'center',
}: ChartLegendProps) {
  return (
    <div className={`chart-legend chart-legend-${align}`} role="list">
      {payload.map((entry, index) => (
        <button
          key={index}
          className={`chart-legend-item ${entry.inactive ? 'inactive' : ''}`}
          onClick={() => onClick?.(entry)}
          role="listitem"
          aria-label={`${entry.value}${entry.inactive ? ' (hidden)' : ''}`}
        >
          <span
            className="chart-legend-dot"
            style={{ backgroundColor: entry.inactive ? '#d1d5db' : entry.color }}
          />
          <span className="chart-legend-label">{entry.value}</span>
        </button>
      ))}
    </div>
  );
}
```

### Legend CSS

```css
.chart-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  padding: 8px 0 0;
}

.chart-legend-center { justify-content: center; }
.chart-legend-left   { justify-content: flex-start; }
.chart-legend-right  { justify-content: flex-end; }

.chart-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 2px 4px;
  font-size: 12px;
  font-weight: 500;
  color: var(--chart-text, #374151);
  background: none;
  border: none;
  cursor: pointer;
  border-radius: 4px;
  transition: opacity 150ms ease;
}

.chart-legend-item:hover {
  background: #f3f4f6;
}

.chart-legend-item.inactive {
  opacity: 0.4;
  text-decoration: line-through;
}

.chart-legend-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.chart-legend-label {
  white-space: nowrap;
}
```

---

## 5. Responsive Chart Container

```tsx
// ResponsiveChart.tsx
import React from 'react';
import { ResponsiveContainer } from 'recharts';

interface ResponsiveChartProps {
  children: React.ReactElement;
  height?: number;
  minWidth?: number;
  aspect?: number;
}

export function ResponsiveChart({
  children,
  height = 300,
  minWidth,
  aspect,
}: ResponsiveChartProps) {
  return (
    <div
      className="responsive-chart"
      style={{ minWidth, width: '100%', height: aspect ? undefined : height }}
    >
      <ResponsiveContainer width="100%" height="100%" aspect={aspect}>
        {children}
      </ResponsiveContainer>
    </div>
  );
}
```

```css
.responsive-chart {
  width: 100%;
  font-family: var(--chart-font, 'Inter', system-ui, sans-serif);
}

/* Reduce motion */
@media (prefers-reduced-motion: reduce) {
  .responsive-chart .recharts-animate-enter,
  .responsive-chart .recharts-animate {
    animation: none !important;
    transition: none !important;
  }
}
```

---

## 6. Chart Type Implementations

### 6.1 Line Chart

```tsx
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid,
  Tooltip, Legend, ResponsiveContainer,
} from 'recharts';
import { CHART_COLORS, CHART_THEME } from './chart-tokens';
import { ChartTooltip } from './ChartTooltip';
import { ChartWrapper } from './ChartWrapper';

interface LineChartProps {
  data: Array<Record<string, number | string>>;
  xKey: string;
  yKeys: string[];
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
  formatValue?: (value: number) => string;
  formatLabel?: (label: string) => string;
}

export function AppLineChart({
  data,
  xKey,
  yKeys,
  title,
  subtitle,
  loading,
  error,
  height = 320,
  formatValue,
  formatLabel,
}: LineChartProps) {
  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height}
    >
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data} margin={{ top: 8, right: 8, left: 0, bottom: 0 }}>
          <CartesianGrid
            strokeDasharray="3 3"
            stroke={CHART_THEME.grid.stroke}
            strokeOpacity={CHART_THEME.grid.strokeOpacity}
            vertical={false}
          />
          <XAxis
            dataKey={xKey}
            axisLine={{ stroke: CHART_THEME.axis.stroke }}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatLabel}
            dy={8}
          />
          <YAxis
            axisLine={false}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatValue}
            dx={-8}
          />
          <Tooltip
            content={
              <ChartTooltip
                formatter={(val, name) =>
                  formatValue ? formatValue(val) : val.toLocaleString()
                }
                labelFormatter={formatLabel}
              />
            }
          />
          {yKeys.map((key, i) => (
            <Line
              key={key}
              type="monotone"
              dataKey={key}
              stroke={CHART_COLORS.categorical[i % 8]}
              strokeWidth={CHART_THEME.line.strokeWidth}
              dot={false}
              activeDot={{ r: 6, strokeWidth: 2, fill: 'white' }}
              animationDuration={CHART_THEME.animation.duration}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

### 6.2 Bar Chart (Vertical)

```tsx
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, Cell,
} from 'recharts';
import { CHART_COLORS, CHART_THEME } from './chart-tokens';
import { ChartTooltip } from './ChartTooltip';
import { ChartWrapper } from './ChartWrapper';

interface BarChartProps {
  data: Array<Record<string, number | string>>;
  xKey: string;
  yKey: string;
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
  color?: string;
  highlightIndex?: number;
  formatValue?: (value: number) => string;
}

export function AppBarChart({
  data,
  xKey,
  yKey,
  title,
  subtitle,
  loading,
  error,
  height = 320,
  color = CHART_COLORS.categorical[0],
  highlightIndex,
  formatValue,
}: BarChartProps) {
  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height}
    >
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data} margin={{ top: 8, right: 8, left: 0, bottom: 0 }}>
          <CartesianGrid
            strokeDasharray="3 3"
            stroke={CHART_THEME.grid.stroke}
            strokeOpacity={CHART_THEME.grid.strokeOpacity}
            vertical={false}
          />
          <XAxis
            dataKey={xKey}
            axisLine={{ stroke: CHART_THEME.axis.stroke }}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            dy={8}
          />
          <YAxis
            axisLine={false}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatValue}
            dx={-8}
          />
          <Tooltip
            content={
              <ChartTooltip
                formatter={(val) =>
                  formatValue ? formatValue(val) : val.toLocaleString()
                }
              />
            }
          />
          <Bar
            dataKey={yKey}
            radius={CHART_THEME.bar.radius}
            animationDuration={CHART_THEME.animation.duration}
          >
            {data.map((_, index) => (
              <Cell
                key={index}
                fill={
                  highlightIndex !== undefined
                    ? index === highlightIndex
                      ? color
                      : '#e5e7eb'
                    : color
                }
              />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

### 6.3 Horizontal Bar Chart

```tsx
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer,
} from 'recharts';

export function AppHorizontalBarChart({
  data,
  categoryKey,
  valueKey,
  title,
  subtitle,
  loading,
  error,
  height,
  color = CHART_COLORS.categorical[0],
  formatValue,
}: {
  data: Array<Record<string, number | string>>;
  categoryKey: string;
  valueKey: string;
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
  color?: string;
  formatValue?: (value: number) => string;
}) {
  const dynamicHeight = Math.max(240, data.length * 36 + 40);

  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height || dynamicHeight}
    >
      <ResponsiveContainer width="100%" height="100%">
        <BarChart
          data={data}
          layout="vertical"
          margin={{ top: 4, right: 24, left: 100, bottom: 4 }}
        >
          <CartesianGrid
            strokeDasharray="3 3"
            stroke={CHART_THEME.grid.stroke}
            strokeOpacity={CHART_THEME.grid.strokeOpacity}
            horizontal={false}
          />
          <XAxis
            type="number"
            axisLine={false}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatValue}
          />
          <YAxis
            type="category"
            dataKey={categoryKey}
            axisLine={false}
            tickLine={false}
            tick={{ fontSize: 13, fill: '#374151' }}
            width={96}
          />
          <Tooltip
            content={
              <ChartTooltip
                formatter={(val) =>
                  formatValue ? formatValue(val) : val.toLocaleString()
                }
              />
            }
          />
          <Bar
            dataKey={valueKey}
            fill={color}
            radius={[0, 4, 4, 0]}
            barSize={20}
            animationDuration={CHART_THEME.animation.duration}
          />
        </BarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

### 6.4 Area Chart

```tsx
import {
  AreaChart, Area, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer,
} from 'recharts';

export function AppAreaChart({
  data,
  xKey,
  yKey,
  title,
  subtitle,
  loading,
  error,
  height = 320,
  color = CHART_COLORS.categorical[0],
  formatValue,
  formatLabel,
}: {
  data: Array<Record<string, number | string>>;
  xKey: string;
  yKey: string;
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
  color?: string;
  formatValue?: (value: number) => string;
  formatLabel?: (label: string) => string;
}) {
  const gradientId = `area-gradient-${yKey}`;

  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height}
    >
      <ResponsiveContainer width="100%" height="100%">
        <AreaChart data={data} margin={{ top: 8, right: 8, left: 0, bottom: 0 }}>
          <defs>
            <linearGradient id={gradientId} x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor={color} stopOpacity={0.3} />
              <stop offset="100%" stopColor={color} stopOpacity={0} />
            </linearGradient>
          </defs>
          <CartesianGrid
            strokeDasharray="3 3"
            stroke={CHART_THEME.grid.stroke}
            strokeOpacity={CHART_THEME.grid.strokeOpacity}
            vertical={false}
          />
          <XAxis
            dataKey={xKey}
            axisLine={{ stroke: CHART_THEME.axis.stroke }}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatLabel}
          />
          <YAxis
            axisLine={false}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatValue}
          />
          <Tooltip
            content={
              <ChartTooltip
                formatter={(val) =>
                  formatValue ? formatValue(val) : val.toLocaleString()
                }
                labelFormatter={formatLabel}
              />
            }
          />
          <Area
            type="monotone"
            dataKey={yKey}
            stroke={color}
            strokeWidth={2}
            fill={`url(#${gradientId})`}
            dot={false}
            activeDot={{ r: 6, strokeWidth: 2, fill: 'white' }}
            animationDuration={CHART_THEME.animation.duration}
          />
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

### 6.5 Pie / Donut Chart

```tsx
import {
  PieChart, Pie, Cell, Tooltip, ResponsiveContainer,
} from 'recharts';

interface PieChartDataItem {
  name: string;
  value: number;
}

export function AppPieChart({
  data,
  title,
  subtitle,
  loading,
  error,
  height = 320,
  donut = false,
  centerLabel,
  centerValue,
  formatValue,
}: {
  data: PieChartDataItem[];
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
  donut?: boolean;
  centerLabel?: string;
  centerValue?: string;
  formatValue?: (value: number) => string;
}) {
  const innerRadius = donut ? '55%' : 0;

  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height}
    >
      <ResponsiveContainer width="100%" height="100%">
        <PieChart>
          <Pie
            data={data}
            cx="50%"
            cy="50%"
            innerRadius={innerRadius}
            outerRadius="80%"
            paddingAngle={2}
            dataKey="value"
            stroke="white"
            strokeWidth={2}
            animationDuration={CHART_THEME.animation.duration}
            label={({ name, percent }) =>
              `${name} ${(percent * 100).toFixed(0)}%`
            }
            labelLine={{ stroke: '#9ca3af', strokeWidth: 1 }}
          >
            {data.map((_, index) => (
              <Cell
                key={index}
                fill={CHART_COLORS.categorical[index % 8]}
              />
            ))}
          </Pie>
          <Tooltip
            content={
              <ChartTooltip
                formatter={(val) =>
                  formatValue ? formatValue(val) : val.toLocaleString()
                }
              />
            }
          />
          {/* Center label for donut */}
          {donut && centerValue && (
            <text
              x="50%"
              y="50%"
              textAnchor="middle"
              dominantBaseline="central"
            >
              <tspan
                x="50%"
                dy="-8"
                fontSize="28"
                fontWeight="700"
                fill="#111827"
              >
                {centerValue}
              </tspan>
              {centerLabel && (
                <tspan
                  x="50%"
                  dy="22"
                  fontSize="12"
                  fill="#6b7280"
                >
                  {centerLabel}
                </tspan>
              )}
            </text>
          )}
        </PieChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

### 6.6 Scatter Plot

```tsx
import {
  ScatterChart, Scatter, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, ZAxis,
} from 'recharts';

export function AppScatterChart({
  data,
  xKey,
  yKey,
  zKey,
  title,
  subtitle,
  loading,
  error,
  height = 320,
  color = CHART_COLORS.categorical[0],
  formatX,
  formatY,
}: {
  data: Array<Record<string, number>>;
  xKey: string;
  yKey: string;
  zKey?: string;
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
  color?: string;
  formatX?: (value: number) => string;
  formatY?: (value: number) => string;
}) {
  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height}
    >
      <ResponsiveContainer width="100%" height="100%">
        <ScatterChart margin={{ top: 8, right: 8, left: 0, bottom: 0 }}>
          <CartesianGrid
            strokeDasharray="3 3"
            stroke={CHART_THEME.grid.stroke}
            strokeOpacity={CHART_THEME.grid.strokeOpacity}
          />
          <XAxis
            dataKey={xKey}
            type="number"
            axisLine={{ stroke: CHART_THEME.axis.stroke }}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatX}
            name={xKey}
          />
          <YAxis
            dataKey={yKey}
            type="number"
            axisLine={false}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatY}
            name={yKey}
          />
          {zKey && (
            <ZAxis
              dataKey={zKey}
              type="number"
              range={[40, 400]}
              name={zKey}
            />
          )}
          <Tooltip content={<ChartTooltip />} />
          <Scatter
            data={data}
            fill={color}
            fillOpacity={0.6}
            stroke={color}
            strokeWidth={1}
            animationDuration={CHART_THEME.animation.duration}
          />
        </ScatterChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

### 6.7 Stacked Area Chart

```tsx
import {
  AreaChart, Area, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer,
} from 'recharts';

export function AppStackedAreaChart({
  data,
  xKey,
  yKeys,
  title,
  subtitle,
  loading,
  error,
  height = 320,
  formatValue,
  formatLabel,
}: {
  data: Array<Record<string, number | string>>;
  xKey: string;
  yKeys: string[];
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
  formatValue?: (value: number) => string;
  formatLabel?: (label: string) => string;
}) {
  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height}
    >
      <ResponsiveContainer width="100%" height="100%">
        <AreaChart data={data} margin={{ top: 8, right: 8, left: 0, bottom: 0 }}>
          <CartesianGrid
            strokeDasharray="3 3"
            stroke={CHART_THEME.grid.stroke}
            strokeOpacity={CHART_THEME.grid.strokeOpacity}
            vertical={false}
          />
          <XAxis
            dataKey={xKey}
            axisLine={{ stroke: CHART_THEME.axis.stroke }}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatLabel}
          />
          <YAxis
            axisLine={false}
            tickLine={false}
            tick={{ fontSize: 11, fill: '#9ca3af' }}
            tickFormatter={formatValue}
          />
          <Tooltip
            content={
              <ChartTooltip
                formatter={(val) =>
                  formatValue ? formatValue(val) : val.toLocaleString()
                }
                labelFormatter={formatLabel}
              />
            }
          />
          {yKeys.map((key, i) => (
            <Area
              key={key}
              type="monotone"
              dataKey={key}
              stackId="1"
              stroke={CHART_COLORS.categorical[i % 8]}
              fill={CHART_COLORS.categorical[i % 8]}
              fillOpacity={0.8}
              animationDuration={CHART_THEME.animation.duration}
            />
          ))}
        </AreaChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

### 6.8 Radar Chart

```tsx
import {
  RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis,
  Radar, Tooltip, ResponsiveContainer, Legend,
} from 'recharts';

export function AppRadarChart({
  data,
  dataKeys,
  angleKey,
  title,
  subtitle,
  loading,
  error,
  height = 360,
}: {
  data: Array<Record<string, number | string>>;
  dataKeys: string[];
  angleKey: string;
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
}) {
  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height}
    >
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart data={data} cx="50%" cy="50%" outerRadius="75%">
          <PolarGrid stroke="#e5e7eb" strokeOpacity={0.3} />
          <PolarAngleAxis
            dataKey={angleKey}
            tick={{ fontSize: 11, fill: '#6b7280' }}
          />
          <PolarRadiusAxis
            tick={{ fontSize: 10, fill: '#9ca3af' }}
            axisLine={false}
          />
          {dataKeys.map((key, i) => (
            <Radar
              key={key}
              name={key}
              dataKey={key}
              stroke={CHART_COLORS.categorical[i % 8]}
              fill={CHART_COLORS.categorical[i % 8]}
              fillOpacity={0.2}
              strokeWidth={2}
              animationDuration={CHART_THEME.animation.duration}
            />
          ))}
          <Tooltip content={<ChartTooltip />} />
          <Legend />
        </RadarChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

### 6.9 Treemap

```tsx
import {
  Treemap as RechartsTreemap, ResponsiveContainer, Tooltip,
} from 'recharts';

interface TreemapDataItem {
  name: string;
  size: number;
  children?: TreemapDataItem[];
}

function TreemapContent({
  x, y, width, height, name, size, depth,
}: {
  x: number; y: number; width: number; height: number;
  name: string; size: number; depth: number;
}) {
  if (width < 50 || height < 30) return null;

  return (
    <g>
      <rect
        x={x}
        y={y}
        width={width}
        height={height}
        rx={2}
        fill={CHART_COLORS.categorical[depth % 8]}
        fillOpacity={0.85}
        stroke="white"
        strokeWidth={2}
      />
      {width > 60 && height > 40 && (
        <>
          <text
            x={x + 8}
            y={y + 18}
            fontSize={12}
            fontWeight={600}
            fill="white"
          >
            {name.length > width / 8 ? name.slice(0, Math.floor(width / 8)) + '...' : name}
          </text>
          <text
            x={x + 8}
            y={y + 34}
            fontSize={11}
            fill="rgba(255,255,255,0.8)"
          >
            {size.toLocaleString()}
          </text>
        </>
      )}
    </g>
  );
}

export function AppTreemap({
  data,
  title,
  subtitle,
  loading,
  error,
  height = 400,
}: {
  data: TreemapDataItem[];
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
}) {
  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height}
    >
      <ResponsiveContainer width="100%" height="100%">
        <RechartsTreemap
          data={data}
          dataKey="size"
          aspectRatio={4 / 3}
          stroke="white"
          content={<TreemapContent x={0} y={0} width={0} height={0} name="" size={0} depth={0} />}
          animationDuration={CHART_THEME.animation.duration}
        />
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

### 6.10 Funnel Chart

```tsx
import {
  FunnelChart, Funnel, Cell, Tooltip,
  LabelList, ResponsiveContainer,
} from 'recharts';

interface FunnelDataItem {
  name: string;
  value: number;
  fill?: string;
}

export function AppFunnelChart({
  data,
  title,
  subtitle,
  loading,
  error,
  height = 360,
  formatValue,
}: {
  data: FunnelDataItem[];
  title: string;
  subtitle?: string;
  loading?: boolean;
  error?: string;
  height?: number;
  formatValue?: (value: number) => string;
}) {
  return (
    <ChartWrapper
      title={title}
      subtitle={subtitle}
      loading={loading}
      error={error}
      empty={!data?.length}
      height={height}
    >
      <ResponsiveContainer width="100%" height="100%">
        <FunnelChart>
          <Tooltip
            content={
              <ChartTooltip
                formatter={(val) =>
                  formatValue ? formatValue(val) : val.toLocaleString()
                }
              />
            }
          />
          <Funnel
            data={data}
            dataKey="value"
            animationDuration={CHART_THEME.animation.duration}
          >
            {data.map((entry, index) => (
              <Cell
                key={index}
                fill={entry.fill || CHART_COLORS.categorical[index % 8]}
              />
            ))}
            <LabelList
              position="right"
              dataKey="name"
              fill="#374151"
              fontSize={13}
              fontWeight={500}
            />
          </Funnel>
        </FunnelChart>
      </ResponsiveContainer>
    </ChartWrapper>
  );
}
```

---

## 7. KPI Card Component

```tsx
// KPICard.tsx
interface KPICardProps {
  label: string;
  value: string;
  delta?: {
    value: string;
    direction: 'up' | 'down' | 'flat';
    sentiment: 'positive' | 'negative' | 'neutral';
  };
  sparklineData?: number[];
  context?: string;
  loading?: boolean;
}

export function KPICard({
  label,
  value,
  delta,
  sparklineData,
  context,
  loading,
}: KPICardProps) {
  if (loading) {
    return (
      <div className="kpi-card kpi-card-loading">
        <div className="skeleton" style={{ width: '60%', height: 14 }} />
        <div className="skeleton" style={{ width: '40%', height: 32, marginTop: 8 }} />
        <div className="skeleton" style={{ width: '50%', height: 14, marginTop: 8 }} />
      </div>
    );
  }

  const deltaColor =
    delta?.sentiment === 'positive' ? 'var(--chart-positive)' :
    delta?.sentiment === 'negative' ? 'var(--chart-negative)' :
    'var(--chart-neutral)';

  const deltaArrow =
    delta?.direction === 'up' ? '\u2191' :
    delta?.direction === 'down' ? '\u2193' :
    '\u2014';

  return (
    <div className="kpi-card" role="group" aria-label={label}>
      <span className="kpi-label">{label}</span>
      <span className="kpi-value">{value}</span>
      {delta && (
        <span className="kpi-delta" style={{ color: deltaColor }}>
          {deltaArrow} {delta.value}
        </span>
      )}
      {sparklineData && (
        <div className="kpi-sparkline" aria-hidden="true">
          <svg viewBox={`0 0 ${sparklineData.length * 4} 24`} preserveAspectRatio="none">
            <polyline
              fill="none"
              stroke={deltaColor}
              strokeWidth="1.5"
              points={sparklineData
                .map((v, i) => {
                  const min = Math.min(...sparklineData);
                  const max = Math.max(...sparklineData);
                  const range = max - min || 1;
                  const y = 22 - ((v - min) / range) * 20;
                  return `${i * 4},${y}`;
                })
                .join(' ')}
            />
          </svg>
        </div>
      )}
      {context && <span className="kpi-context">{context}</span>}
    </div>
  );
}
```

### KPI Card CSS

```css
.kpi-card {
  background: var(--chart-bg, white);
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 16px 20px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.kpi-label {
  font-size: 12px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--chart-text-muted, #6b7280);
}

.kpi-value {
  font-size: 32px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: var(--chart-text, #111827);
  line-height: 1.1;
}

.kpi-delta {
  font-size: 14px;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
}

.kpi-sparkline {
  height: 24px;
  margin: 4px 0;
}

.kpi-sparkline svg {
  width: 100%;
  height: 100%;
}

.kpi-context {
  font-size: 12px;
  color: var(--chart-text-muted, #9ca3af);
}
```

---

## 8. Utility Functions

### 8.1 Number Formatting

```tsx
// format.ts
export function formatCurrency(value: number, compact = false): string {
  if (compact) {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      notation: 'compact',
      maximumFractionDigits: 1,
    }).format(value);
  }
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(value);
}

export function formatNumber(value: number, compact = false): string {
  if (compact) {
    return new Intl.NumberFormat('en-US', {
      notation: 'compact',
      maximumFractionDigits: 1,
    }).format(value);
  }
  return new Intl.NumberFormat('en-US').format(value);
}

export function formatPercent(value: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'percent',
    minimumFractionDigits: 1,
    maximumFractionDigits: 1,
  }).format(value / 100);
}

export function formatDate(date: Date, style: 'short' | 'medium' | 'relative' = 'medium'): string {
  if (style === 'relative') {
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffHours = diffMs / (1000 * 60 * 60);
    const diffDays = diffMs / (1000 * 60 * 60 * 24);

    if (diffHours < 1) return 'Just now';
    if (diffHours < 24) return `${Math.floor(diffHours)}h ago`;
    if (diffDays < 2) return 'Yesterday';
    if (diffDays < 7) return `${Math.floor(diffDays)}d ago`;
  }

  if (style === 'short') {
    return new Intl.DateTimeFormat('en-US', {
      month: 'short',
      day: 'numeric',
    }).format(date);
  }

  return new Intl.DateTimeFormat('en-US', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  }).format(date);
}
```

### 8.2 Color Utilities

```tsx
// color-utils.ts
import { CHART_COLORS } from './chart-tokens';

export function getCategoricalColor(index: number): string {
  return CHART_COLORS.categorical[index % CHART_COLORS.categorical.length];
}

export function getSequentialColor(
  value: number,
  min: number,
  max: number,
): string {
  const normalizedIndex = Math.round(
    ((value - min) / (max - min)) * (CHART_COLORS.sequential.length - 1)
  );
  return CHART_COLORS.sequential[
    Math.max(0, Math.min(normalizedIndex, CHART_COLORS.sequential.length - 1))
  ];
}

export function getDeltaColor(
  value: number,
  invertSentiment = false,
): string {
  if (value === 0) return CHART_COLORS.semantic.neutral;
  const isPositive = value > 0;
  const isGood = invertSentiment ? !isPositive : isPositive;
  return isGood ? CHART_COLORS.semantic.positive : CHART_COLORS.semantic.negative;
}
```

---

## 9. Print Styles

```css
@media print {
  /* Hide interactive elements */
  .chart-tooltip,
  .chart-legend-item,
  .chart-card-actions,
  .filter-bar,
  .pagination,
  .bulk-actions-bar {
    display: none !important;
  }

  /* Force white backgrounds */
  .chart-card,
  .kpi-card,
  .dashboard-card {
    background: white !important;
    box-shadow: none !important;
    border: 1px solid #d1d5db !important;
  }

  /* Prevent page breaks inside charts */
  .chart-card,
  .kpi-card {
    break-inside: avoid;
    page-break-inside: avoid;
  }

  /* Ensure colors print */
  .recharts-surface,
  .chart-bar,
  .chart-line,
  .chart-area {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* Show legend as static text for print */
  .chart-legend-print {
    display: flex !important;
    gap: 16px;
    padding: 8px 0;
    font-size: 11px;
  }

  /* Increase text contrast */
  .chart-axis-label,
  .chart-tick-label {
    fill: #111827 !important;
    color: #111827 !important;
  }

  /* Increase gridline visibility */
  .recharts-cartesian-grid line {
    stroke-opacity: 0.3 !important;
  }
}
```

---

## 10. Responsive Chart Sizing Reference

```css
/* Container query-based chart sizing */
.chart-container {
  container-type: inline-size;
}

/* Compact: reduce padding, font sizes */
@container (max-width: 400px) {
  .chart-card-title { font-size: 14px; }
  .chart-card-body { padding: 8px 12px 12px; }
  .chart-legend { gap: 8px; }
  .chart-legend-item { font-size: 11px; }
}

/* Very compact: hide secondary elements */
@container (max-width: 280px) {
  .chart-card-subtitle { display: none; }
  .chart-legend { display: none; }
  .chart-card-actions { display: none; }
}

/* Tall enough for chart */
@container (min-height: 200px) {
  .chart-card-body { min-height: 160px; }
}
```

---

## 11. Testing Patterns

### 11.1 Chart Rendering Test

```tsx
// AppBarChart.test.tsx
import { render, screen } from '@testing-library/react';
import { AppBarChart } from './AppBarChart';

describe('AppBarChart', () => {
  const mockData = [
    { category: 'A', value: 100 },
    { category: 'B', value: 200 },
    { category: 'C', value: 150 },
  ];

  it('renders loading state', () => {
    render(
      <AppBarChart
        data={[]}
        xKey="category"
        yKey="value"
        title="Test Chart"
        loading
      />
    );
    expect(screen.getByLabelText('Loading chart data')).toBeInTheDocument();
  });

  it('renders empty state', () => {
    render(
      <AppBarChart
        data={[]}
        xKey="category"
        yKey="value"
        title="Test Chart"
      />
    );
    expect(screen.getByText('No data')).toBeInTheDocument();
  });

  it('renders error state', () => {
    render(
      <AppBarChart
        data={[]}
        xKey="category"
        yKey="value"
        title="Test Chart"
        error="Failed to load"
      />
    );
    expect(screen.getByText('Unable to load chart')).toBeInTheDocument();
    expect(screen.getByText('Failed to load')).toBeInTheDocument();
  });

  it('renders chart with data', () => {
    render(
      <AppBarChart
        data={mockData}
        xKey="category"
        yKey="value"
        title="Test Chart"
      />
    );
    expect(screen.getByText('Test Chart')).toBeInTheDocument();
    expect(screen.getByRole('figure')).toHaveAttribute('aria-label', 'Test Chart');
  });
});
```

### 11.2 Accessibility Test

```tsx
import { axe } from 'jest-axe';
import { render } from '@testing-library/react';

it('passes accessibility audit', async () => {
  const { container } = render(
    <AppBarChart
      data={mockData}
      xKey="category"
      yKey="value"
      title="Revenue by Region"
    />
  );
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```
