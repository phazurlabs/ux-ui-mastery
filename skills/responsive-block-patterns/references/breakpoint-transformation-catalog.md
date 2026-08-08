# Breakpoint Transformation Catalog — 100+ Component Transformations

A comprehensive catalog documenting exactly how every common UI component transforms across breakpoints. For each component: what changes at each breakpoint and which transformation type applies.

## Transformation Types Key

| Code | Type | Description |
|------|------|-------------|
| RF | Reflow | Content rearranges spatial direction |
| RV | Reveal | Hidden content becomes visible |
| CL | Collapse | Expanded content becomes compact |
| PR | Prioritize | Content reorders by importance |
| SC | Scale | Elements change size proportionally |
| RL | Relocate | Element moves to different position |
| RS | Restructure | Internal structure fundamentally changes |

---

## Navigation Components (1-12)

### 1. Top Navigation Bar

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Hamburger icon + logo | Logo + primary links | Logo + all links + CTA | Full links + search + CTA + user menu | CL/RV |
| Height | 56px | 56px | 64px | 64px | SC |
| Links | Hidden in overlay | 4-5 visible | All visible | All visible + dropdowns | RV |
| Search | Hidden / icon only | Icon only | Visible inline | Expanded with suggestions | RV |
| CTA button | Hidden or in overlay | Visible, compact | Visible, standard | Visible, prominent | RV |
| User menu | Avatar only | Avatar + dropdown | Avatar + name + dropdown | Full user panel | RV |

### 2. Sidebar Navigation

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Visibility | Hidden (bottom sheet/drawer) | Icon-only rail (56px) | Expanded (240px) | Expanded (280px) | RV/SC |
| Items | Full labels in drawer | Icons only + tooltip | Icon + label | Icon + label + badge counts | RV |
| Sections | Flat list | Collapsed groups | Expanded groups | Expanded groups with headers | RV |
| Position | Fixed bottom sheet | Fixed left rail | Fixed left sidebar | Fixed left sidebar | RL |
| Nesting | Flat, no nesting | 1 level | 2 levels | 3 levels | RV |

### 3. Bottom Tab Bar

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Visibility | Visible, fixed bottom | Visible (optional) | Hidden | Hidden | CL |
| Items | 3-5 tabs with icons | 5-7 tabs | N/A | N/A | CL |
| Labels | Below icon (xs text) | Below icon (sm text) | N/A | N/A | SC |
| Height | 56-64px | 56px | N/A | N/A | SC |
| Safe area | env(safe-area-inset-bottom) | Standard | N/A | N/A | -- |

### 4. Breadcrumbs

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Items shown | First + last + ellipsis | First 2 + last 2 | All items | All items with icons | CL/RV |
| Separator | Chevron | Chevron | Slash or chevron | Slash or chevron | -- |
| Overflow | Ellipsis menu | Ellipsis for middle | None | None | CL |
| Font size | text-xs | text-sm | text-sm | text-sm | SC |

### 5. Pagination

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Display | Prev/Next + "Page X of Y" | Prev/Next + 3-5 pages | Full page numbers | Full + per-page selector | CL/RV |
| Button size | 40px touch target | 36px | 32px | 32px | SC |
| Position | Centered | Centered | Right-aligned | Right-aligned + results count | RL |

### 6. Tabs

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Horizontal scroll | Horizontal scroll | Full width, distributed | Full width, distributed | RF |
| Overflow | Scroll with fade hint | Scroll (optional) | None | None | CL |
| Indicator | Bottom border | Bottom border | Bottom border | Bottom border | -- |
| Content swap | Full-width panel | Full-width panel | Inline panel | Inline panel | -- |

### 7. Mega Menu

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Trigger | Hamburger > nested list | Hamburger > nested list | Hover/click dropdown | Hover/click dropdown | RS |
| Layout | Full-screen overlay, stacked | Full-screen, 2-column | Dropdown, 3-4 columns | Dropdown, 4+ columns + featured | RS/RV |
| Images | Hidden | Thumbnails | Medium images | Large featured images | RV |
| Close | Back button / X | Back button / X | Click outside / escape | Click outside / escape | RS |

### 8. Command Palette / Search

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Full-screen overlay | Full-screen overlay | Centered floating panel | Centered floating panel (wider) | RS |
| Width | 100% | 100% | 560px | 640px | SC |
| Results | Full-height scroll | Full-height scroll | Max 60vh | Max 60vh | SC |
| Sections | Sequential list | Sequential list | Grouped with headers | Grouped + preview pane | RV |

### 9. Stepper / Wizard Navigation

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Orientation | Vertical, left-aligned | Horizontal, top | Horizontal, top | Horizontal, top with labels | RF |
| Labels | Full text | Abbreviated | Full text | Full text + description | SC/RV |
| Connector | Vertical line | Horizontal line | Horizontal line | Horizontal line | RF |
| Step indicator | Number | Number | Number + icon | Number + icon + status | RV |

### 10. Toolbar / Action Bar

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Actions shown | 2-3 + overflow menu | 4-5 + overflow | All actions | All actions + labels | CL/RV |
| Button style | Icon-only | Icon-only | Icon + label | Icon + label | RV |
| Position | Fixed bottom or top | Fixed top | Inline or sticky | Inline or sticky | RL |
| Grouping | Flat | Flat | Grouped with dividers | Grouped with dividers + tooltips | RV |

### 11. Dropdown Menu

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Presentation | Bottom sheet (full-width) | Bottom sheet or dropdown | Dropdown anchored | Dropdown anchored | RS |
| Width | 100vw | 100vw or auto | 200-320px | 200-320px | SC |
| Item height | 48px (touch) | 44px | 36px | 36px | SC |
| Nested menus | Sequential screens | Sequential screens | Flyout to right | Flyout to right | RS |

### 12. Segmented Control

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Full-width, equal | Full-width | Auto-width | Auto-width | SC |
| Labels | Short labels only | Short labels | Full labels | Full labels + counts | CL/RV |
| Icon | Icon-only if > 3 segments | Icon + label | Icon + label | Icon + label + badge | CL/RV |
| Size | 40px height | 36px | 32px | 32px | SC |

---

## Content Components (13-36)

### 13. Hero Section

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Stacked (text above image) | Stacked or split | Split 50/50 | Split 40/60 | RF |
| Title size | text-2xl | text-3xl | text-4xl | text-4xl | SC |
| Buttons | Stacked, full-width | Side by side | Side by side | Side by side, larger | RF/SC |
| Image | Below text, full-width | Below or beside text | Beside text, 50% | Beside text, 60% | RF/SC |
| Min height | Auto | 70vh | 80vh | 80vh | SC |
| Alignment | Center | Center or left | Left | Left | PR |

### 14. Feature Grid

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Columns | 1 | 2 | 3 | 4 | RF |
| Icon size | 32px | 40px | 48px | 48px | SC |
| Description | Full text | Full text | Full text | Full text | -- |
| Card style | Simple stack | Card with border | Card with border | Card with hover effect | RV |

### 15. Pricing Table

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Stacked cards, vertical scroll | 2 visible + scroll | 3 side-by-side | 3-4 with comparison table | RF/RS |
| Features | Top 5 features | All features, compact | All features | All features + comparison grid | CL/RV |
| Recommended | Badge on card | Badge + subtle highlight | Elevated card + border | Elevated + highlighted column | SC |
| CTA | Full-width buttons | Full-width | Contained buttons | Contained + secondary CTA | SC |

### 16. Testimonial Section

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Horizontal scroll carousel | 2-column grid | 3-column grid | 3-column masonry | RF/RS |
| Photo | Small circle (40px) | Medium circle (48px) | Medium circle (56px) | Large circle (64px) | SC |
| Quote length | Truncated (3 lines) | Full text | Full text | Full text + context | CL/RV |
| Navigation | Dots or swipe | None (grid) | None (grid) | None (grid) | CL |

### 17. Card (Generic)

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Direction | Vertical (image top) | Vertical | Horizontal (image left) | Horizontal | RF |
| Image ratio | 16:9 | 16:9 | Auto (40% width) | Auto (35% width) | RS |
| Padding | 16px | 20px | 24px | 24px | SC |
| Actions | Below content | Below content | Right-aligned | Right-aligned + secondary | RL |
| Metadata | Hidden or minimal | Visible | Visible | Full metadata | RV |

### 18. Data Table

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Card list (stacked) | Horizontal scroll table | Full table | Full table + sticky columns | RS |
| Columns | 2-3 key fields per card | 4-5 columns visible | All columns | All columns + extra detail | CL/RV |
| Row height | Auto (card) | 48px | 40px | 36px | SC |
| Sorting | Dropdown selector | Column header tap | Column header click | Click + multi-sort | RS |
| Selection | Long-press / checkbox | Checkbox | Checkbox + shift-select | Checkbox + shift + keyboard | RV |
| Actions | Bottom action bar | Row-level menu | Row hover actions | Inline actions | RL |

### 19. Form Layout

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Columns | Single column | Single or 2-col | 2-column | 2-3 column | RF |
| Label position | Above input | Above input | Left of input (optional) | Left of input | RL |
| Input width | Full-width | Full-width | Max 400px | Max 400px | SC |
| Button alignment | Full-width, stacked | Full-width or right | Right-aligned | Right-aligned + cancel | RF/RL |
| Sections | Stacked | Stacked | Card sections | Card sections with sidebar summary | RS |

### 20. Modal / Dialog

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Size | Full-screen | Full-screen or centered | Centered (480-560px) | Centered (560-640px) | SC |
| Position | Bottom-aligned sliding up | Center | Center | Center | RL |
| Close | X button top-right + back swipe | X button | X button + Escape key | X + Escape + click outside | RV |
| Border radius | Top corners only | Top corners or all | All corners | All corners | SC |
| Scroll | Full-page scroll | Constrained body scroll | Constrained body scroll | Constrained body scroll | -- |

### 21. Drawer / Panel

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Position | Bottom sheet | Bottom sheet or right side | Right side (380px) | Right side (420-480px) | RL |
| Interaction | Drag handle + swipe to close | Drag or click scrim | Click scrim or X | Click scrim, X, or Escape | RS |
| Height/Width | 85% viewport height | 85vh or 380px width | 380px width | 420-480px width | SC |
| Overlay | Scrim + drag handle | Scrim | Scrim | Scrim (optional, can push content) | -- |

### 22. Tooltip

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Trigger | Long-press or tap | Long-press or tap | Hover | Hover + focus | RS |
| Position | Centered bottom of screen | Near trigger | Adjacent to trigger | Adjacent with arrow | RL |
| Dismiss | Tap anywhere | Tap anywhere | Mouse leave | Mouse leave or Escape | RS |
| Width | 90% viewport, centered | Auto (max 320px) | Auto (max 280px) | Auto (max 320px) | SC |

### 23. Toast / Notification

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Position | Bottom center, full-width | Bottom center | Bottom-right | Bottom-right or top-right | RL |
| Width | 100% - 32px | Auto (max 400px) | Auto (max 400px) | Auto (max 480px) | SC |
| Actions | Below message | Inline right | Inline right | Inline right + dismiss | RF |
| Stack | Replace previous | Stack (max 3) | Stack (max 3) | Stack (max 5) | RV |

### 24. Accordion

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Full-width, single column | Full-width | 2-column grid (optional) | 2-column + all expanded | RF/RS |
| Behavior | One open at a time | One open at a time | Multiple open | All always open | RS |
| Header | Title + chevron | Title + chevron + subtitle | Title + subtitle + chevron | Full detail | RV |
| Padding | 16px | 20px | 24px | 24px | SC |

### 25. Carousel / Slider

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Visible items | 1 (full-width) + peek | 2 + peek | 3 | 4 | RF |
| Navigation | Swipe + dots | Swipe + dots + arrows | Arrows + dots | Arrows + dots + keyboard | RV |
| Controls | Dots below | Dots below + side arrows | Side arrows + dots | Side arrows + dots + counter | RV |
| Gap | 12px | 16px | 20px | 24px | SC |

### 26. Gallery / Image Grid

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Columns | 1-2 | 2-3 | 3-4 | 4-5 | RF |
| Gap | 4px | 8px | 12px | 12-16px | SC |
| Aspect ratio | 1:1 | 1:1 | Mixed (masonry) | Mixed (masonry) | RS |
| Lightbox | Full-screen swipe | Full-screen swipe | Centered overlay + arrows | Overlay + arrows + filmstrip | RS |
| Caption | Below image | Below image | Overlay on hover | Overlay on hover + sidebar | RL/RV |

### 27. Chart / Data Visualization

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Full-width, stacked | Full-width | Side by side (2) | Side by side (2-3) | RF |
| Legend | Below chart | Below chart | Side of chart | Side of chart with interaction | RL |
| Axis labels | Rotated / abbreviated | Abbreviated | Full labels | Full labels + gridlines | CL/RV |
| Interaction | Tap to see value | Tap/hover | Hover + crosshair | Hover + crosshair + detail panel | RV |
| Annotations | Hidden | Hidden | Visible | Visible + callouts | RV |

### 28. Calendar

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Default view | Day list or agenda | Week view | Month grid | Month grid + sidebar detail | RS |
| Day cell | Date number only | Date + dot indicators | Date + 2-3 event previews | Date + 3-4 event previews | RV |
| Header | Month + nav arrows | Week range + nav | Month + weekday headers | Month + weekday headers + filters | RV |
| Event detail | Full-screen overlay | Bottom sheet | Side panel | Side panel or inline expansion | RS |

### 29. List (Generic)

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Item height | 56-72px | 48-56px | 40-48px | 36-44px | SC |
| Columns | 1 | 1 | 1-2 | 1-2 | RF |
| Secondary text | Below primary | Below primary | Inline right | Inline right | RL |
| Actions | Swipe to reveal | Swipe or long-press | Hover actions | Inline actions | RS |
| Dividers | Full-width | Full-width | Inset | Inset or none | SC |

### 30. Search Results

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | List | List | List + filter sidebar | List + filter sidebar + preview | RV |
| Filters | Bottom sheet toggle | Top horizontal scroll | Left sidebar | Left sidebar (sticky) | RL |
| Result card | Compact, key info | Compact + thumbnail | Full details + image | Full details + image + metadata | RV |
| Sort controls | Dropdown | Dropdown | Inline buttons | Inline buttons + view toggle | RV |

### 31. Blog / Article Content

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Max width | 100% | 100% | 720px centered | 720px + sidebar TOC | SC |
| Images | Full-width | Full-width | Inline or breakout | Inline, breakout, or float | SC |
| TOC | Hidden (hamburger) | Hidden (hamburger) | Sticky right sidebar | Sticky right sidebar | RV |
| Pull quotes | Inline, full-width | Inline, full-width | Float or centered | Float with offset | RL |
| Code blocks | Horizontal scroll | Horizontal scroll | Contained (wrap optional) | Contained + line numbers | CL/RV |

### 32. Footer

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Link columns | Accordion / stacked | 2 columns | 4 columns | 4 columns + newsletter | RF/RV |
| Logo | Centered above links | Left-aligned, full-width row | Left column (larger) | Left column (larger) | RL |
| Bottom bar | Stacked, centered | Horizontal, centered | Horizontal, space-between | Horizontal, space-between | RF |
| Social links | Centered row | Left or center | Right-aligned | Right-aligned | RL |

### 33. Empty State

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Illustration | Small (120px) | Medium (200px) | Large (280px) | Large (320px) | SC |
| Text alignment | Center | Center | Center | Center or left with illustration right | RF |
| CTA | Full-width button | Auto-width button | Auto-width button | Auto-width + secondary | SC |
| Description | Short (2 lines) | Medium (3 lines) | Full description | Full description + tips | CL/RV |

### 34. Error / 404 Page

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Stacked, centered | Stacked, centered | Split (illustration + text) | Split | RF |
| Illustration | Small | Medium | Large, beside text | Large, beside text | SC |
| Suggestions | 2-3 links | 3-4 links | 4-6 links + search | 6+ links + search + popular | RV |

### 35. Profile / User Page

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Cover image | Full-width, short (120px) | Full-width (200px) | Full-width (280px) | Full-width (320px) | SC |
| Avatar | 64px, centered | 80px | 96px, offset from cover | 120px, offset | SC |
| Stats | Horizontal row | Horizontal row | Right-aligned or sidebar | Sidebar | RL |
| Content tabs | Scrollable tabs | Full-width tabs | Full-width tabs | Tabs + preview sidebar | RF/RV |

### 36. Notification Center

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Container | Full-screen page | Full-screen or panel | Right panel (380px) | Right panel (420px) | RS |
| Item layout | Compact row | Compact row | Row with actions | Row + preview + actions | RV |
| Grouping | Flat list | By date | By date + category tabs | By date + category + filters | RV |
| Actions | Swipe to dismiss | Swipe + buttons | Hover buttons | Inline buttons | RS |

---

## Input Components (37-52)

### 37. Text Input

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Width | Full-width (100%) | Full-width | Max 400px | Max 400px | SC |
| Height | 48px (touch) | 44px | 40px | 36px | SC |
| Label | Above | Above | Above or left | Left (inline form) | RL |
| Helper text | Below input | Below input | Below input | Below or tooltip | -- |
| Font size | 16px (prevents zoom on iOS) | 16px | 14px | 14px | SC |

### 38. Select / Dropdown

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Opened state | Bottom sheet (full options) | Bottom sheet or dropdown | Dropdown below | Dropdown below | RS |
| Option height | 48px | 44px | 36px | 36px | SC |
| Search | Always visible if > 10 items | If > 10 items | If > 10 items | Always | RV |
| Multi-select | Checkboxes in sheet | Checkboxes | Checkboxes + chips | Chips + search | RS |

### 39. Date Picker

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Calendar | Full-screen overlay | Bottom sheet | Dropdown panel | Dropdown panel + presets | RS |
| Range | Sequential months | Sequential | Side-by-side months | Side-by-side + presets sidebar | RF/RV |
| Input | Tap to open picker | Tap to open | Type or pick | Type or pick + shortcuts | RV |
| Day size | 44px min | 40px | 36px | 36px | SC |

### 40. File Upload

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Drop zone | Button only ("Choose file") | Small drop zone | Large drop zone + drag | Large drop zone + preview grid | RS |
| Preview | List below button | Grid (2-col) | Grid (3-col) | Grid (4-col) + detail panel | RF |
| Progress | Inline bar per file | Inline bar | Inline bar + overall | Inline + overall + cancel/retry | RV |

### 41. Slider / Range Input

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Track height | 4px, thumb 28px | 4px, thumb 24px | 4px, thumb 20px | 4px, thumb 20px | SC |
| Value display | Above thumb | Above thumb | Tooltip on hover | Inline beside slider | RL |
| Width | Full-width | Full-width | Max 400px | Max 400px | SC |
| Tick marks | None | Major ticks | All ticks | All ticks + labels | RV |

### 42. Toggle / Switch

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Size | 52x32px | 48x28px | 44x24px | 40x22px | SC |
| Label | Right of toggle | Right | Right | Right + description below | RV |
| Touch target | 48px total | 44px | 36px | 32px | SC |

### 43. Checkbox / Radio

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Size | 24px with 48px touch | 20px with 40px touch | 18px | 16px | SC |
| Label gap | 12px | 10px | 8px | 8px | SC |
| Group layout | Vertical stack | Vertical or 2-col | 2-3 column | 3-4 column or horizontal | RF |

### 44. Search Input

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Behavior | Expands on focus (full-width overlay) | Inline expanding | Inline, fixed width | Inline, wider + suggestions | RS |
| Suggestions | Full-screen list | Below input | Below input | Below + category grouping | RS |
| Filters | Hidden until results | Horizontal chips | Sidebar | Sidebar + advanced | RV |
| Clear button | Always visible when filled | Always | Always | Always + keyboard shortcut hint | -- |

### 45. Rich Text Editor

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Toolbar | Minimal (bold, italic, list) | Single row, scrollable | Single row, full | Multi-row or contextual | CL/RV |
| Toolbar position | Fixed bottom | Fixed bottom or top | Top sticky | Top sticky | RL |
| Formatting | Bottom sheet menus | Bottom sheet | Dropdown menus | Dropdowns + keyboard shortcuts | RS |

### 46. Color Picker

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Full-screen overlay | Bottom sheet | Dropdown panel | Dropdown + palette sidebar | RS |
| Spectrum | Simplified (swatches) | Spectrum + swatches | Full spectrum + inputs | Spectrum + inputs + swatches | RV |
| Input | Hex only | Hex + RGB | Hex + RGB + HSL | All formats + eyedropper | RV |

### 47. Tag / Chip Input

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Tags wrap, scroll if many | Tags wrap | Single row + "+N more" | Single row, all visible | CL |
| Remove | X button on each | X button | X button + backspace key | X + backspace + select-all | RV |
| Suggestions | Full-width below | Below input | Below input | Below + categories | RF |

### 48. OTP / Verification Input

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Box size | 44px | 48px | 48px | 48px | SC |
| Gap | 8px | 12px | 12px | 16px | SC |
| Auto-fill | SMS autofill | SMS autofill | Paste support | Paste + auto-advance | -- |

### 49. Address / Multi-Field Input

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | All fields stacked | City/State/Zip in row | Street full, City/State/Zip in row | Two-column with map | RF |
| Autocomplete | Full-screen suggestions | Below input | Below input | Inline suggestions | RS |

### 50. Quantity Selector

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Button size | 48px | 40px | 36px | 32px | SC |
| Layout | - [value] + | - [value] + | - [value] + | - [input] + | -- |
| Input | Read-only display | Read-only | Editable input | Editable + keyboard shortcuts | RV |

### 51. Star Rating Input

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Star size | 32px with 48px touch | 28px | 24px | 24px | SC |
| Gap | 8px | 6px | 4px | 4px | SC |
| Half stars | No (full only) | Optional | Yes | Yes | RV |
| Hover preview | No (touch) | No | Yes | Yes + tooltip | RV |

### 52. Password Input

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Toggle visibility | Eye icon (always visible) | Eye icon | Eye icon | Eye icon + keyboard shortcut | -- |
| Strength meter | Below input, simplified | Below input | Below input + requirements | Below + requirements + suggestions | RV |
| Width | Full-width | Full-width | Max 400px | Max 400px | SC |

---

## Layout Components (53-68)

### 53. Sidebar + Main Content

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Sidebar | Hidden (drawer) | Icon rail (56px) | Expanded (240px) | Expanded (280px) | RV |
| Main padding | 16px | 20px | 24px 32px | 32px 48px | SC |
| Sidebar toggle | Hamburger button | Rail click to expand | Persistent | Persistent | RS |

### 54. Dashboard Layout

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Grid | 1 column | 2 columns | 3-4 columns | 4-6 columns | RF |
| Widget sizing | Full-width | Half or full | Quarter, half, full | Flexible grid areas | RF |
| Summary bar | Horizontal scroll | 2x2 grid | Single row | Single row + trend sparklines | RF/RV |

### 55. Split Pane

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Stacked (toggle view) | Stacked or 40/60 | 40/60 with resize | 30/70 with resize | RF |
| Resize handle | None | None or toggle button | Drag handle | Drag handle + double-click reset | RV |
| Collapse | Full screen one pane | Toggle button | Collapse button | Collapse + keyboard shortcut | CL |

### 56. Masonry Grid

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Columns | 1 | 2 | 3 | 4-5 | RF |
| Gap | 8px | 12px | 16px | 16px | SC |
| Item width | 100% | ~50% | ~33% | ~25% | SC |
| Load more | Button | Button | Infinite scroll | Infinite scroll | RS |

### 57. Kanban Board

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Columns | 1 visible (swipe) | 2 visible (scroll) | 3-4 visible | All visible | RF |
| Column width | 100% | 300px | 280px | Flexible (min 250px) | SC |
| Card detail | Full-screen overlay | Bottom sheet | Side panel | Side panel | RS |
| Drag and drop | Long-press + move | Drag | Drag | Drag + keyboard | RV |

### 58. Infinite Scroll Container

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Trigger | 200px before bottom | 300px | 400px | 500px | SC |
| Skeleton | 2 items | 4 items | 6 items | 8 items | SC |
| Back to top | FAB after 3 screens | FAB after 3 screens | Fixed button | Fixed button | -- |
| Column count | 1 | 2 | 3 | 4 | RF |

### 59. Grid / List View Toggle

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Default view | List | Grid (2-col) | Grid (3-col) | Grid (4-col) | RF |
| Toggle position | Top-right | Top-right | Top-right with sort | Top-right with sort + density | -- |
| List item | Compact row | Standard row | Detailed row | Detailed + thumbnail | RV |
| Grid card | Small card | Medium card | Standard card | Large card | SC |

### 60. Chat Layout

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Thread list | Full screen (separate view) | Left panel (320px) | Left panel (320px) | Left panel (360px) | RF |
| Message area | Full screen | Right panel | Right panel | Center panel | RF |
| Detail panel | Bottom sheet | Bottom sheet | Hidden (toggle) | Right panel (320px) | RV/RL |
| Input | Fixed bottom | Fixed bottom | Fixed bottom | Fixed bottom + toolbar | -- |

### 61. Settings Page

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Nav | Horizontal scroll tabs | Horizontal tabs | Left sidebar | Left sidebar | RL |
| Content | Full-width | Full-width | Centered (max 720px) | Centered + description sidebar | SC |
| Sections | Flat stack | Flat stack | Card groups | Card groups | -- |

### 62. Checkout Flow

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Single column + stepper | Single column | 2-column (form + summary) | 2-column (wider form) | RF |
| Summary | Expandable top section | Expandable | Sticky right sidebar | Sticky right sidebar | RL |
| Stepper | Compact top bar | Top bar | Top bar or breadcrumb | Breadcrumb with labels | RS |

### 63. E-commerce Product Grid

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Columns | 2 | 3 | 4 | 5-6 | RF |
| Card content | Image + title + price | + rating | + quick-add button | + color swatches + save | RV |
| Image ratio | 1:1 | 1:1 | 3:4 | 3:4 | -- |
| Filters | Toggle bottom sheet | Top horizontal + sheet | Left sidebar + top sort | Left sidebar + top sort + chips | RL/RV |

### 64. Email / Inbox Layout

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| List | Full screen | Left panel (40%) | Left panel (360px) | Left panel (400px) | RF |
| Message | Full screen (push) | Right panel (60%) | Right panel | Right panel + actions | RF |
| Actions | Bottom toolbar | Top toolbar | Top toolbar + hover row actions | Inline + toolbar | RL |
| Compose | Full screen | Bottom sheet | Modal (600px) | Modal or side panel | RS |

### 65. Documentation / Docs Layout

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Nav | Hamburger drawer | Hamburger drawer | Left sidebar (240px) | Left sidebar (260px) | RV |
| Content | Full-width | Full-width (max 720px) | Center column | Center column | SC |
| TOC | Hidden | Hidden | Right sidebar (200px) | Right sidebar (220px) | RV |
| Code blocks | Full-width scroll | Full-width | Contained | Contained + copy button | CL/RV |

### 66. Media Player Page

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Video | Full-width, 16:9 | Full-width, 16:9 | Left 70%, 16:9 | Left 70% + theater mode | SC |
| Controls | Overlay on tap | Overlay | Below video | Below + keyboard shortcuts | RL |
| Related | Below video, horizontal scroll | Below, 2-col grid | Right sidebar list | Right sidebar | RL |
| Comments | Below, full-width | Below | Below video, left column | Below + threaded | RF |

### 67. Map + List Layout

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Layout | Toggle between map/list | Split (map top, list bottom) | Split (list left, map right) | Split (list left, map right) | RS |
| Map size | Full-screen when active | 50% height | 60% width | 65% width | SC |
| List items | Compact cards | Compact cards | Detailed cards | Detailed + hover highlight on map | RV |
| Detail | Bottom sheet over map | Bottom sheet | Side panel over list | Expanded card in list | RS |

### 68. Wizard / Multi-Step Form

| Property | Mobile (320-480) | Tablet (768) | Desktop (1024) | Wide (1440+) | Type |
|----------|-----------------|-------------|----------------|-------------|------|
| Progress | Compact bar (step X of Y) | Step dots | Step labels + dots | Step labels + descriptions | RV |
| Content | Full-width | Full-width (max 600px) | Centered (max 640px) | Centered + summary sidebar | SC |
| Navigation | Full-width buttons | Full-width | Right-aligned | Right-aligned + back | RL |
| Review | Stacked sections | Stacked | 2-column | 2-column + edit links | RF |

---

## Specialized Components (69-100+)

### 69-75: Social & Communication

| # | Component | Mobile | Tablet | Desktop | Wide | Primary Type |
|---|-----------|--------|--------|---------|------|-------------|
| 69 | Social feed post | Full-width card | Max 600px centered | Max 600px | Max 600px + sidebar | SC |
| 70 | Comment thread | Flat + indent | Flat + indent | Threaded + collapse | Threaded + votes | RS |
| 71 | User avatar group | 3 shown + "+N" | 5 shown + "+N" | 8 shown | All shown | RV |
| 72 | Reaction picker | Bottom sheet grid | Bottom sheet | Popover | Popover + search | RS |
| 73 | Share sheet | Native OS sheet | Bottom sheet | Dropdown | Dropdown + preview | RS |
| 74 | Activity feed | Compact timeline | Timeline + icons | Timeline + previews | Timeline + previews + filters | RV |
| 75 | Mention autocomplete | Full-width below | Below input | Below input | Below + recent | RS |

### 76-82: E-commerce

| # | Component | Mobile | Tablet | Desktop | Wide | Primary Type |
|---|-----------|--------|--------|---------|------|-------------|
| 76 | Product image zoom | Pinch to zoom | Pinch or tap | Hover magnify | Hover magnify + lightbox | RS |
| 77 | Size/variant selector | Grid of buttons | Grid | Grid | Grid + availability | -- |
| 78 | Shopping cart | Full page | Full page | Side drawer (380px) | Side drawer (420px) | RS |
| 79 | Mini cart | Icon + count badge | Icon + badge | Icon + dropdown preview | Dropdown + thumbnail | RV |
| 80 | Product comparison | Horizontal scroll | 2 visible | 3-4 visible | 4+ with sticky header | RF |
| 81 | Reviews section | Stacked | Stacked + photos grid | 2-column (summary + list) | 2-column + photo gallery | RF/RV |
| 82 | Shipping tracker | Vertical stepper | Vertical stepper | Horizontal stepper | Stepper + map | RF/RV |

### 83-89: Productivity

| # | Component | Mobile | Tablet | Desktop | Wide | Primary Type |
|---|-----------|--------|--------|---------|------|-------------|
| 83 | File manager grid | 2-col grid | 3-col | 4-5 col + detail sidebar | 5-6 col + detail | RF/RV |
| 84 | Task card | Compact | Standard | Standard + sub-tasks | Full with timeline | RV |
| 85 | Gantt chart | List view only | Simplified | Full Gantt | Gantt + resource view | RS |
| 86 | Spreadsheet view | 3-4 cols scroll | 5-6 cols | Full sheet | Full + formula bar + panels | RV |
| 87 | Code editor | Full-screen | Full + file tabs | Split pane + file tree | Multi-pane + terminal | RV |
| 88 | Whiteboard / Canvas | Full-screen, pinch zoom | Full-screen | Full + left tool panel | Full + panels + minimap | RV |
| 89 | Audio waveform | Full-width minimal | Full + time markers | Full + markers + controls | Full + multi-track | RV |

### 90-96: Marketing & Content

| # | Component | Mobile | Tablet | Desktop | Wide | Primary Type |
|---|-----------|--------|--------|---------|------|-------------|
| 90 | Newsletter signup | Stacked (input + button) | Inline (input + button) | Inline + benefit text | Inline + benefit + social proof | RF/RV |
| 91 | Cookie consent | Bottom bar, stacked | Bottom bar, inline | Bottom bar, inline | Bottom corner toast | RL |
| 92 | Banner / Announcement | Full-width, 2 lines | Full-width, 1 line | Full-width, 1 line + CTA | Full + CTA + dismiss | SC/RV |
| 93 | Feature comparison | Vertical cards | 2-col table | Full table | Table + visual indicators | RS |
| 94 | Team / People grid | 1-2 columns | 3 columns | 4 columns | 4-5 columns + bio expand | RF |
| 95 | Logo cloud | 2x2 grid | 3x2 | Single row scroll | Single row, all visible | RF |
| 96 | Video embed | Full-width 16:9 | Full-width | Max 800px centered | Max 960px + transcript | SC |

### 97-104: Utility & System

| # | Component | Mobile | Tablet | Desktop | Wide | Primary Type |
|---|-----------|--------|--------|---------|------|-------------|
| 97 | Loading skeleton | Matches component | Matches | Matches | Matches | -- |
| 98 | Progress bar | Full-width | Full-width | Max 400px | Max 400px + percentage | SC |
| 99 | Badge / Counter | Dot or number | Number | Number + label | Label + number | RV |
| 100 | Divider | Full-width | Full-width | Inset | Inset or none | SC |
| 101 | Scroll indicator | Dots or line | Line | None (scrollbar) | Custom scrollbar | RS |
| 102 | Drag handle | 24px vertical dots | 20px | 16px | 16px + tooltip | SC |
| 103 | Keyboard shortcut hint | Hidden | Hidden | Shown in tooltips | Shown inline | RV |
| 104 | Context menu | Bottom sheet | Bottom sheet | Right-click popup | Right-click + sub-menus | RS |
