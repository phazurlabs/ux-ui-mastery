# SaaS & Productivity — Sector Style Intelligence

## Sector Overview

SaaS and productivity tools represent the purest expression of functional design. These are products people use for hours every workday — their interfaces must reduce friction to near-zero for expert users while remaining learnable for newcomers. The defining aesthetic is "professional calm" — interfaces that communicate competence and reliability through restraint, precision, and information density that respects the user's time and attention.

The modern SaaS aesthetic was largely defined by a wave of products in the 2019-2024 era: Linear, Superhuman, Raycast, and Vercel established a new visual language that broke from the cluttered enterprise dashboards of the previous generation. This language is characterized by reduced chrome, keyboard-first interaction, dark mode preference, command palette navigation, and an almost brutalist commitment to functional beauty. If fintech's defining quality is trust and wellness is warmth, SaaS's defining quality is speed — visual and interactive speed that makes the user feel like the product is an extension of their mind.

---

## Color Psychology

### What Colors Mean in SaaS

| Color | Association | Usage | Notes |
|---|---|---|---|
| **Dark Gray/Near Black** | Focus, professionalism, modern | Default dark mode backgrounds | Not pure black — #111 to #1A1A1A range |
| **White/Light Gray** | Clarity, cleanliness, document-like | Light mode, content areas | Warm off-whites (#FAFAFA) preferred |
| **Brand Purple/Blue** | Innovation, interactivity | Primary accent, selections, CTAs | Used sparingly — UI is about content, not brand |
| **Green** | Success, online, active | Status indicators, success states | Must work against both light and dark |
| **Red/Orange** | Errors, urgency, destructive | Alerts, error states, critical actions | Minimal use — most SaaS flows are non-critical |
| **Yellow/Amber** | Warning, attention | Pending states, warnings | Accessible amber, not bright yellow |

### Palettes from Leading SaaS Apps

#### Linear
```
Primary Purple:     #5E6AD2 (Distinctive muted purple)
Dark Background:    #0D0D0D (Near black — ultra minimal)
Surface:            #171717 (Subtle elevation)
Surface Elevated:   #1F1F1F
Surface Hover:      #262626
Text Primary:       #F2F2F2
Text Secondary:     #8B8B8B
Text Muted:         #5C5C5C
Border:             #2A2A2A
Accent Blue:        #4C9EEB
Priority Urgent:    #F2505D (Red — urgent)
Priority High:      #F28E3D (Orange — high)
Priority Medium:    #F2C94C (Yellow — medium)
Priority Low:       #8B8B8B (Gray — low)
Status Done:        #5E6AD2 (Purple — completed)
Status In Progress: #F2C94C (Yellow — active)
Status Todo:        #8B8B8B (Gray — waiting)
```
**Why it works:** Linear's muted purple is sophisticated without being flashy. The priority/status color system is immediately scannable in dense issue lists. The near-black background creates an immersive, focused work environment.

#### Vercel
```
Primary White:      #FFFFFF (Brand is black and white)
Dark Background:    #000000 (Pure black — bold statement)
Surface:            #111111
Surface Elevated:   #1A1A1A
Border:             #333333
Text Primary:       #EDEDED
Text Secondary:     #888888
Text Muted:         #666666
Accent Blue:        #0070F3 (Vercel blue — deployments, links)
Success Green:      #50E3C2 (Deployment success)
Error Red:          #E00
Warning Yellow:     #F5A623
Gradient Start:     #007CF0
Gradient End:       #00DFD8
Logo Triangle:      #FFFFFF on #000000
```
**Why it works:** Vercel's black-and-white palette is a statement of confidence — no brand color needed. The monochromatic aesthetic lets deployment status colors (green for success, red for error) communicate with maximum clarity against the neutral canvas.

#### Superhuman
```
Primary Purple:     #6B4FBB (Email reimagined — premium purple)
Dark Background:    #1A1625 (Warm dark — purple-tinted black)
Surface:            #231E30
Surface Hover:      #2D2740
Text Primary:       #FFFFFF
Text Secondary:     #A09BB5
Border:             #3A3450
Unread Indicator:   #6B4FBB (Purple dot)
Star Gold:          #FFD700
Calendar Blue:      #4A9BF5
Snooze Orange:      #F5A623
Sent Green:         #4FD1C5
```
**Why it works:** Superhuman's warm, purple-tinted dark theme creates a premium feel that justifies its $30/month price point. Every color has a specific semantic meaning in the email workflow.

#### Slack
```
Primary Purple:     #4A154B (Aubergine — distinctive brand)
Dark Background:    #1A1D21 (Dark mode)
Sidebar:            #19171D (Dark sidebar)
Channel Active:     #FFFFFF text on dark
Channel Inactive:   #9B9D9F text
Message Background: #222529
Text Primary:       #D1D2D3
Text Secondary:     #9B9D9F
Online Green:       #007A5A
Away Yellow:        #E8A820
DND Red:            #E01E5A
Link Blue:          #1D9BD1
Mention Yellow:     #F2C744 (Mention highlight)
Reaction Hover:     #2D2F33
Border:             #3B3C3F
```
**Why it works:** Slack's aubergine brand color is one of the most distinctive in B2B SaaS. The sidebar color system (workspace color customization) adds personality while the message area maintains neutral readability.

#### Raycast
```
Primary Red:        #FF6363 (Energetic, distinctive)
Dark Background:    #141414 (Near black)
Surface:            #1C1C1C
Surface Elevated:   #252525
Surface Active:     #2D2D2D
Text Primary:       #EEEEEE
Text Secondary:     #929292
Text Muted:         #6B6B6B
Border:             #333333
Green Success:      #30D158
Yellow Warning:     #FFD60A
Blue Info:          #0A84FF
Extension Colors:   Per-extension icon color system
```
**Why it works:** Raycast's warm red accent stands out in a sea of blue/purple SaaS tools. The near-black command palette creates an immersive launcher experience that feels native to macOS.

#### Cron (now Notion Calendar)
```
Primary Blue:       #006BFF (Clean calendar blue)
Dark Background:    #141414
Surface:            #1C1C1C
Surface Hover:      #262626
Text Primary:       #FFFFFF
Text Secondary:     #8F8F8F
Event Colors:       #006BFF, #30D158, #FF9F0A, #FF453A,
                    #BF5AF2, #64D2FF, #FFD60A, #FF6482
Border:             #2C2C2C
Today Highlight:    #006BFF (Circle indicator)
Weekend Muted:      #0D0D0D (Slightly darker)
```

### Developer Tool Palettes (Sector Overlap)

#### GitHub
```
Dark Background:    #0D1117 (GitHub dark default)
Surface:            #161B22
Surface Elevated:   #21262D
Text Primary:       #F0F6FC
Text Secondary:     #8B949E
Link Blue:          #58A6FF
Border:             #30363D
Green Merged:       #3FB950
Purple Open:        #A371F7
Red Closed:         #F85149
Diff Green:         #2EA04333 (Addition with alpha)
Diff Red:           #F8514933 (Deletion with alpha)
Syntax Highlighting: GitHub theme colors (well-established)
```

#### Supabase
```
Primary Green:      #3ECF8E (Distinctive green)
Dark Background:    #1C1C1C
Surface:            #2A2A2A
Text Primary:       #EDEDED
Text Secondary:     #8F8F8F
Brand Dark:         #181818
Accent Green Light: #C5F1DD
Border:             #333333
```

---

## Typography Norms

### Font Choices Across Leading SaaS Apps

| App | Primary Font | Mono Font | Why |
|---|---|---|---|
| **Linear** | Inter | SF Mono, JetBrains Mono | Inter's tabular figures and clean geometry at 13px |
| **Vercel** | Inter, Geist (custom) | Geist Mono | Custom font family — sans + mono pair designed together |
| **Superhuman** | SF Pro, system | SF Mono | Native feel for keyboard-intensive email client |
| **Slack** | Lato, system | Consolas, Menlo | Lato is warm yet professional; mono for code snippets |
| **Raycast** | Inter, SF Pro | SF Mono | Clean, native-feeling on macOS |
| **Cron** | Inter | Tabular numerals in Inter | Inter's time/date rendering is excellent |
| **GitHub** | -apple-system, Segoe UI | SFMono-Regular, Consolas | System fonts for performance; mono for code |
| **Supabase** | Custom (based on Inter) | Source Code Pro | Clean, consistent with developer tooling |

### SaaS Typography Rules

1. **13-14px is the standard body size.** SaaS users accept higher density than consumer app users. 13px with 1.5 line-height is perfectly readable for daily-use professional tools.

2. **Use font-weight for hierarchy, not just size.** In dense interfaces, a 13px bold label above a 13px regular value creates effective hierarchy without size variation.

3. **Monospace for data, IDs, and code.** Issue IDs (LIN-1234), deployment hashes (abc123f), and API keys should always render in monospace.

4. **Condensed type scale — fewer steps.** SaaS interfaces need fewer heading levels. Three is usually enough.

```
Page Title:     24px / 600 weight / -0.02em tracking
Section Header: 16px / 600 weight / -0.01em tracking
Subsection:     14px / 600 weight / 0 tracking
Body:           14px / 400 weight / 0 tracking
Body Small:     13px / 400 weight / 0 tracking
Label:          12px / 500 weight / 0 tracking
Caption:        11px / 400 weight / 0.02em tracking
Overline:       11px / 600 weight / 0.08em tracking / uppercase
Code/ID:        13px / 400 weight / 0 tracking / monospace
Keyboard Hint:  11px / 500 weight / monospace
```

5. **Keyboard shortcut rendering matters.** Display keyboard shortcuts in a monospace font with a subtle background badge:

```css
.kbd {
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 11px;
  font-weight: 500;
  background: #2A2A2A;
  border: 1px solid #404040;
  border-radius: 4px;
  padding: 1px 6px;
  color: #B3B3B3;
  line-height: 1;
}
```

---

## Component Conventions

### Border Radius

SaaS tools use tight, professional radii. Soft curves feel consumer-grade; sharp corners feel productive.

```
Buttons:           6px  (compact, efficient)
Cards:             8px  (subtle softening)
Input Fields:      6px  (matches buttons)
Modals:            12px (focal elements get slightly more)
Dropdowns:         8px
Context Menus:     8px
Command Palette:   12px (the hero element gets special treatment)
Tooltips:          6px
Tags/Badges:       4px  (compact, data-dense)
Avatars:           50%  (circular) or 6px (rounded square)
Toggle:            12px (pill-shaped track)
```

### Elevation & Shadow

SaaS UIs in dark mode rely on border + surface color rather than shadow for elevation.

```css
/* Dark Mode Elevation (preferred) */
/* Level 0 — Base */
background: #0D0D0D;
border: none;

/* Level 1 — Subtle surface */
background: #171717;
border: 1px solid #2A2A2A;

/* Level 2 — Panel */
background: #1F1F1F;
border: 1px solid #333333;

/* Level 3 — Popover/Dropdown */
background: #252525;
border: 1px solid #404040;
box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);

/* Level 4 — Modal/Command Palette */
background: #1F1F1F;
border: 1px solid #404040;
box-shadow: 0 16px 64px rgba(0, 0, 0, 0.6);

/* Light Mode Elevation */
/* Level 0 */
background: #FFFFFF;
border: 1px solid #E5E7EB;

/* Level 1 */
background: #FFFFFF;
box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);

/* Level 2 */
background: #FFFFFF;
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);

/* Level 3 */
background: #FFFFFF;
box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
```

### Issue/Task Row (Key SaaS Pattern)

```css
.issue-row {
  display: flex;
  align-items: center;
  padding: 8px 16px;
  border-bottom: 1px solid #2A2A2A;
  font-size: 13px;
  color: #F2F2F2;
  gap: 12px;
  transition: background 0.08s ease;
  cursor: pointer;
}
.issue-row:hover {
  background: #1A1A1A;
}
.issue-row .priority-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}
.issue-row .status-icon {
  width: 14px;
  height: 14px;
  flex-shrink: 0;
  border-radius: 50%;
  border: 2px solid #5E6AD2;
}
.issue-row .status-icon.done {
  background: #5E6AD2;
}
.issue-row .issue-id {
  font-family: 'SF Mono', monospace;
  font-size: 12px;
  color: #5C5C5C;
  flex-shrink: 0;
  min-width: 72px;
}
.issue-row .issue-title {
  flex: 1;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.issue-row .assignee-avatar {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  flex-shrink: 0;
}
.issue-row .label {
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 500;
  flex-shrink: 0;
}
```

### Command Palette (Key SaaS Pattern)

```css
.cmd-palette-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  display: flex;
  justify-content: center;
  padding-top: 15vh;
  z-index: 9999;
}
.cmd-palette {
  width: 640px;
  max-height: 480px;
  background: #1F1F1F;
  border: 1px solid #404040;
  border-radius: 12px;
  box-shadow: 0 16px 64px rgba(0, 0, 0, 0.6);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.cmd-palette-input-wrapper {
  display: flex;
  align-items: center;
  padding: 0 16px;
  border-bottom: 1px solid #333333;
  gap: 12px;
}
.cmd-palette-input-wrapper .search-icon {
  width: 20px;
  height: 20px;
  color: #666666;
  flex-shrink: 0;
}
.cmd-palette-input {
  flex: 1;
  height: 52px;
  background: transparent;
  border: none;
  color: #F2F2F2;
  font-size: 16px;
  outline: none;
}
.cmd-palette-input::placeholder {
  color: #666666;
}
.cmd-palette-group {
  padding: 8px;
}
.cmd-palette-group-label {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #666666;
  padding: 8px 8px 4px;
}
.cmd-palette-item {
  display: flex;
  align-items: center;
  padding: 8px 12px;
  border-radius: 6px;
  gap: 12px;
  font-size: 14px;
  color: #CCCCCC;
  cursor: pointer;
}
.cmd-palette-item.active {
  background: #333333;
  color: #FFFFFF;
}
.cmd-palette-item .icon {
  width: 16px;
  height: 16px;
  opacity: 0.6;
}
.cmd-palette-item .shortcut {
  margin-left: auto;
  display: flex;
  gap: 4px;
}
```

### Button Styles — SaaS

```css
/* Primary */
.btn-primary {
  background: #5E6AD2;
  color: #FFFFFF;
  border: none;
  border-radius: 6px;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 500;
  height: 36px;
  transition: background 0.1s ease;
}
.btn-primary:hover {
  background: #6E7AE2;
}

/* Secondary */
.btn-secondary {
  background: #252525;
  color: #CCCCCC;
  border: 1px solid #404040;
  border-radius: 6px;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 500;
  height: 36px;
}
.btn-secondary:hover {
  background: #2D2D2D;
  border-color: #505050;
}

/* Ghost */
.btn-ghost {
  background: transparent;
  color: #8B8B8B;
  border: none;
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 13px;
  font-weight: 500;
  height: 36px;
}
.btn-ghost:hover {
  background: #252525;
  color: #CCCCCC;
}

/* Danger */
.btn-danger {
  background: #3D1F1F;
  color: #F2505D;
  border: 1px solid #5C2A2A;
  border-radius: 6px;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 500;
  height: 36px;
}
```

### Data Table — SaaS

```css
.data-table {
  width: 100%;
  font-size: 13px;
  border-collapse: collapse;
}
.data-table thead th {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #666666;
  padding: 8px 16px;
  border-bottom: 1px solid #2A2A2A;
  text-align: left;
  position: sticky;
  top: 0;
  background: #0D0D0D;
  user-select: none;
  cursor: pointer;
}
.data-table thead th:hover {
  color: #999999;
}
.data-table tbody td {
  padding: 10px 16px;
  border-bottom: 1px solid #1A1A1A;
  color: #E0E0E0;
}
.data-table tbody tr:hover {
  background: #141414;
}
.data-table tbody td.id {
  font-family: monospace;
  color: #666666;
  font-size: 12px;
}
.data-table tbody td.status {
  display: flex;
  align-items: center;
  gap: 8px;
}
```

---

## Spacing Philosophy

SaaS apps optimize for information density while maintaining scannability. Power users want more data visible; casual users need breathing room. Solve this with density modes.

### Spacing Scale

```
2px   — Hairline (table borders, divider lines)
4px   — Micro (icon internal padding, tight groups)
6px   — Extra-tight (sidebar item padding)
8px   — Tight (button padding, between inline elements)
12px  — Default (list item gap, form field spacing)
16px  — Standard (card padding, section gap)
20px  — Comfortable (between major sections)
24px  — Spacious (panel padding, dashboard card gap)
32px  — Section (between page sections)
48px  — Page (major page divisions)
```

### Density Modes

```
Compact:
  Row height:     32px
  Cell padding:   6px 12px
  Font size:      12px
  Gap between:    4px

Default:
  Row height:     40px
  Cell padding:   8px 16px
  Font size:      13px
  Gap between:    8px

Comfortable:
  Row height:     48px
  Cell padding:   12px 16px
  Font size:      14px
  Gap between:    12px
```

### Layout Dimensions

```
Sidebar collapsed:     48px (icon-only)
Sidebar expanded:      240px
Top bar height:        48px
Detail panel width:    400-480px
Content max-width:     No max (fluid) or 1200px (content-focused)
Command palette width: 640px
Modal width:           480px (small) / 640px (medium) / 800px (large)
Page padding:          24px (mobile) / 32px (desktop)
```

---

## Motion Personality

SaaS motion is **instant, utilitarian, and invisible.** The goal is zero perceived latency. Every millisecond of animation is a millisecond the user is waiting to do their work.

### Timing

```
Hover state:          50ms  (background color change — near instant)
Button press:         80ms  (scale down, release)
Focus ring:           0ms   (instant — never animate focus)
Dropdown open:        100ms (fade + scale from 95% to 100%)
Sidebar toggle:       150ms (slide + fade)
Modal open:           200ms (fade in + scale from 97% to 100%)
Command palette:      150ms (fast open — this is the power move)
Page transition:      0ms   (instant swap — no transition)
Toast notification:   200ms slide in, 3s visible, 300ms fade out
Loading skeleton:     1.5s shimmer cycle (subtle pulse)
```

### Easing Curves

```css
/* Near-instant — hover, selection (most interactions) */
transition-timing-function: cubic-bezier(0.2, 0.0, 0.0, 1.0);

/* Quick snap — dropdowns, panels */
transition-timing-function: cubic-bezier(0.32, 0.72, 0.0, 1.0);

/* Standard ease — modal, toast */
transition-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1.0);

/* Exit — dismiss, collapse */
transition-timing-function: cubic-bezier(0.4, 0.0, 1.0, 1.0);
```

### Specific Patterns

- **Command palette open:** Scale from 97% -> 100% + opacity 0 -> 1 over 150ms with backdrop blur fading in simultaneously.
- **Sidebar collapse:** Width animates from 240px -> 48px over 150ms. Content area expands to fill. Icons remain centered.
- **Issue status change:** Status icon color-transitions over 200ms. Row may reorder with 250ms slide animation.
- **Toast notification:** Slides up from bottom-right, 200ms decelerate. Stacks if multiple. Auto-dismiss after 3-5s with 300ms fade.
- **Keyboard navigation highlight:** Active list item background changes instantly (0ms transition). No animation — speed is everything.
- **Loading states:** Subtle skeleton shimmer (background gradient animation, 1.5s cycle). Never spinners in inline content.

---

## Trust Signals

### SaaS-Specific Trust Elements

1. **Uptime status.** Link to status.yourapp.com in the footer. "All systems operational" with green indicator.
2. **Changelog visibility.** "What's new" with recent updates builds confidence the product is actively maintained.
3. **Keyboard shortcuts working perfectly.** If Cmd+K opens the command palette every single time without fail, users trust the product. Broken shortcuts destroy trust instantly.
4. **Fast load times.** A SaaS dashboard that takes 3 seconds to load feels broken. Target < 1 second for page transitions.
5. **Data integrity indicators.** "Last synced 2 seconds ago" for real-time data. "Saved" indicators for user content.
6. **SSO and security badges.** "SOC 2 Type II certified," "SSO available," "Encrypted at rest and in transit."
7. **Clear pricing.** SaaS that hides pricing until demo creates distrust. Transparent pricing is a trust signal.
8. **API documentation quality.** Well-documented APIs signal a product built by competent engineers who care about developer experience.
9. **Responsive support indicators.** "Average response time: 2 hours" is a concrete trust signal.

### Anti-Patterns — SaaS

1. **Feature bloat in primary navigation.** If the sidebar has 20+ items, the product feels overwhelming. Group features, use progressive disclosure.
2. **Mandatory onboarding tours.** Forced product tours that cannot be skipped waste expert users' time. Offer optional, dismissible guidance.
3. **Slow search.** If the command palette takes > 200ms to show results, it fails its core promise of speed.
4. **No keyboard shortcuts.** SaaS products without keyboard navigation feel dated and inefficient.
5. **Excessive loading spinners.** Full-page spinners for data that could be incrementally loaded signal poor engineering.
6. **Settings labyrinth.** Settings pages that require 5 clicks to reach basic preferences indicate poor information architecture.
7. **Notification overload.** Every team member's every action generating a notification creates noise. Smart defaults and customizable notification levels are essential.
8. **Dark mode as afterthought.** SaaS dark mode that is clearly a CSS inversion (wrong contrast, missing shadows, broken illustrations) signals lack of care.
9. **No density controls.** Power users and new users have fundamentally different density needs. One-size-fits-all fails both.
10. **Ignoring CMD+Z.** Undo must work for destructive actions (deleting items, removing team members, changing settings). If Cmd+Z does nothing, the product feels dangerous.

---

## Reference Apps — What to Learn from Each

### Linear
- **Lesson:** Opinionated simplicity. Linear deliberately limits customization to enforce a fast, consistent workflow. Study how saying "no" to features can be a design strategy.
- **Key pattern:** Keyboard-driven everything (press C to create, X to close), priority system (urgent/high/medium/low with distinct icons), cycle-based project management, and the smoothest command palette in SaaS.
- **Visual identity:** The dark, muted aesthetic with purple accent creates a premium "developer tool" feel. Every pixel feels intentional.
- **Motion:** Linear's interactions feel instant — hover states at 50ms, no page transitions, status changes animate but never block.

### Vercel
- **Lesson:** Developer experience as a design discipline. Vercel's dashboard treats deployment status as the primary information hierarchy. Study how they make complex infrastructure feel simple through visual design.
- **Key pattern:** Deployment timeline (git commit -> build -> deploy with live status), domain management cards, real-time log streaming, function invocation graphs.
- **Visual identity:** Pure black and white with deployment status colors. The monochromatic palette is both bold and functional.

### Superhuman
- **Lesson:** Speed as the primary UX metric. Superhuman was built from the ground up to be the fastest email client. Study how they optimize for < 100ms response time and how that speed affects the entire design language.
- **Key pattern:** Split-pane email (list + detail), keyboard shortcuts for every action (H to snooze, E to archive), AI triage, sender profile sidebar, "superhuman command" (Cmd+K).
- **Pricing justification:** At $30/month, the premium visual design (warm purple dark theme, smooth animations, custom iconography) justifies the price through perceived quality.

### Slack
- **Lesson:** Workplace chat as a platform. Study how Slack manages the complexity of workspaces, channels, threads, DMs, apps, and integrations through a clean channel-list paradigm.
- **Key pattern:** Sidebar channel list with sections (Channels, DMs, Apps), threaded conversations (messages fork into side threads), rich message formatting (code blocks, lists, embeds), custom emoji and reactions, Slack Connect (cross-company channels).
- **Customization:** Workspace theming (sidebar colors) gives each workspace a distinct identity.

### Raycast
- **Lesson:** The command palette as the entire product. Raycast is essentially a command palette that replaces Spotlight. Study how they organize thousands of possible actions into a discoverable, fast interface.
- **Key pattern:** Single input field -> instant results grouped by category, extension marketplace, clipboard history, snippet expansion, window management — all through one search interface.
- **Native feel:** Raycast feels like a macOS system feature because it uses native rendering, respects system appearance, and uses standard keyboard shortcuts.

### Cron (Notion Calendar)
- **Lesson:** Calendar design reimagined with modern SaaS aesthetics. Study how Cron applied the Linear/Superhuman visual language (dark mode, keyboard shortcuts, command palette) to the calendar paradigm.
- **Key pattern:** Multi-calendar overlay with distinct colors, availability sharing, keyboard navigation through time (arrow keys move by day/week), Cmd+K for quick event creation, conference link integration.
- **Integration:** The clean API integration (Zoom, Google Meet, Notion) makes joining meetings a one-click action from the calendar.

---

## W3C Design Token Starter Kit — SaaS & Productivity

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "saas-productivity": {
    "color": {
      "background": {
        "$value": "#0D0D0D",
        "$type": "color",
        "$description": "Base dark background"
      },
      "surface-1": { "$value": "#171717", "$type": "color" },
      "surface-2": { "$value": "#1F1F1F", "$type": "color" },
      "surface-3": { "$value": "#252525", "$type": "color" },
      "surface-hover": { "$value": "#2D2D2D", "$type": "color" },
      "surface-active": { "$value": "#333333", "$type": "color" },
      "text-primary": { "$value": "#F2F2F2", "$type": "color" },
      "text-secondary": { "$value": "#8B8B8B", "$type": "color" },
      "text-muted": { "$value": "#5C5C5C", "$type": "color" },
      "text-disabled": { "$value": "#404040", "$type": "color" },
      "border-default": { "$value": "#2A2A2A", "$type": "color" },
      "border-strong": { "$value": "#404040", "$type": "color" },
      "border-subtle": { "$value": "#1F1F1F", "$type": "color" },
      "accent-primary": {
        "$value": "#5E6AD2",
        "$type": "color",
        "$description": "Primary interactive — purple"
      },
      "accent-primary-hover": { "$value": "#6E7AE2", "$type": "color" },
      "accent-blue": { "$value": "#4C9EEB", "$type": "color" },
      "semantic-success": { "$value": "#30D158", "$type": "color" },
      "semantic-success-bg": { "$value": "#1A3D2A", "$type": "color" },
      "semantic-error": { "$value": "#F2505D", "$type": "color" },
      "semantic-error-bg": { "$value": "#3D1F1F", "$type": "color" },
      "semantic-warning": { "$value": "#F2C94C", "$type": "color" },
      "semantic-warning-bg": { "$value": "#3D3520", "$type": "color" },
      "semantic-info": { "$value": "#4C9EEB", "$type": "color" },
      "semantic-info-bg": { "$value": "#1F2D3D", "$type": "color" },
      "priority-urgent": { "$value": "#F2505D", "$type": "color" },
      "priority-high": { "$value": "#F28E3D", "$type": "color" },
      "priority-medium": { "$value": "#F2C94C", "$type": "color" },
      "priority-low": { "$value": "#8B8B8B", "$type": "color" },
      "light-background": {
        "$value": "#FAFAFA",
        "$type": "color",
        "$description": "Light mode base"
      },
      "light-surface": { "$value": "#FFFFFF", "$type": "color" },
      "light-text-primary": { "$value": "#111111", "$type": "color" },
      "light-text-secondary": { "$value": "#666666", "$type": "color" },
      "light-border": { "$value": "#E5E7EB", "$type": "color" }
    },
    "typography": {
      "font-family-primary": {
        "$value": "'Inter', 'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "$type": "fontFamily"
      },
      "font-family-mono": {
        "$value": "'Geist Mono', 'SF Mono', 'JetBrains Mono', 'Fira Code', monospace",
        "$type": "fontFamily"
      },
      "font-size-page-title": { "$value": "24px", "$type": "dimension" },
      "font-size-section": { "$value": "16px", "$type": "dimension" },
      "font-size-subsection": { "$value": "14px", "$type": "dimension" },
      "font-size-body": { "$value": "14px", "$type": "dimension" },
      "font-size-body-small": { "$value": "13px", "$type": "dimension" },
      "font-size-label": { "$value": "12px", "$type": "dimension" },
      "font-size-caption": { "$value": "11px", "$type": "dimension" },
      "font-size-kbd": { "$value": "11px", "$type": "dimension" },
      "font-weight-bold": { "$value": "600", "$type": "fontWeight" },
      "font-weight-medium": { "$value": "500", "$type": "fontWeight" },
      "font-weight-regular": { "$value": "400", "$type": "fontWeight" },
      "line-height-tight": { "$value": "1.3", "$type": "number" },
      "line-height-normal": { "$value": "1.5", "$type": "number" },
      "line-height-relaxed": { "$value": "1.6", "$type": "number" }
    },
    "spacing": {
      "hairline": { "$value": "2px", "$type": "dimension" },
      "micro": { "$value": "4px", "$type": "dimension" },
      "extra-tight": { "$value": "6px", "$type": "dimension" },
      "tight": { "$value": "8px", "$type": "dimension" },
      "default": { "$value": "12px", "$type": "dimension" },
      "standard": { "$value": "16px", "$type": "dimension" },
      "comfortable": { "$value": "20px", "$type": "dimension" },
      "spacious": { "$value": "24px", "$type": "dimension" },
      "section": { "$value": "32px", "$type": "dimension" },
      "page": { "$value": "48px", "$type": "dimension" }
    },
    "radius": {
      "tag": { "$value": "4px", "$type": "dimension" },
      "small": { "$value": "6px", "$type": "dimension" },
      "medium": { "$value": "8px", "$type": "dimension" },
      "large": { "$value": "12px", "$type": "dimension" },
      "full": { "$value": "9999px", "$type": "dimension" }
    },
    "shadow": {
      "popover": {
        "$value": "0 8px 30px rgba(0, 0, 0, 0.4)",
        "$type": "shadow"
      },
      "modal": {
        "$value": "0 16px 64px rgba(0, 0, 0, 0.6)",
        "$type": "shadow"
      },
      "light-popover": {
        "$value": "0 4px 12px rgba(0, 0, 0, 0.08)",
        "$type": "shadow"
      },
      "light-modal": {
        "$value": "0 12px 40px rgba(0, 0, 0, 0.12)",
        "$type": "shadow"
      }
    },
    "motion": {
      "duration-instant": { "$value": "50ms", "$type": "duration" },
      "duration-micro": { "$value": "80ms", "$type": "duration" },
      "duration-fast": { "$value": "100ms", "$type": "duration" },
      "duration-normal": { "$value": "150ms", "$type": "duration" },
      "duration-slow": { "$value": "200ms", "$type": "duration" },
      "duration-toast": { "$value": "3000ms", "$type": "duration" },
      "easing-instant": {
        "$value": "cubic-bezier(0.2, 0.0, 0.0, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-snap": {
        "$value": "cubic-bezier(0.32, 0.72, 0.0, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-standard": {
        "$value": "cubic-bezier(0.25, 0.1, 0.25, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-exit": {
        "$value": "cubic-bezier(0.4, 0.0, 1.0, 1.0)",
        "$type": "cubicBezier"
      }
    },
    "layout": {
      "sidebar-collapsed": { "$value": "48px", "$type": "dimension" },
      "sidebar-expanded": { "$value": "240px", "$type": "dimension" },
      "topbar-height": { "$value": "48px", "$type": "dimension" },
      "detail-panel-width": { "$value": "440px", "$type": "dimension" },
      "command-palette-width": { "$value": "640px", "$type": "dimension" },
      "modal-small": { "$value": "480px", "$type": "dimension" },
      "modal-medium": { "$value": "640px", "$type": "dimension" },
      "modal-large": { "$value": "800px", "$type": "dimension" }
    }
  }
}
```

---

## Inspiration Links

### Mobbin
- [SaaS dashboard screens](https://mobbin.com/browse/apps?category=productivity) — Dashboard patterns, settings, onboarding
- [Developer tool screens](https://mobbin.com/browse/apps?category=developer-tools)

### Screenlane
- [Productivity app UI](https://screenlane.com/screens/category/productivity/) — Task management, calendars, dashboards
- [SaaS dashboard patterns](https://screenlane.com/screens/category/business/)

### Additional Resources
- [Linear design blog](https://linear.app/blog) — Design process and decisions
- [Vercel design system (Geist)](https://vercel.com/geist) — Geist font and design system
- [Superhuman design](https://superhuman.com) — Study the product
- [Raycast store](https://www.raycast.com/store) — Extension design patterns
- [GitHub Primer design system](https://primer.style/) — Comprehensive open-source design system for developer tools

---

## Quick Decision Framework — SaaS

1. **Is this a daily-use tool or a periodic dashboard?** Daily: optimize for speed, keyboard shortcuts, density. Periodic: optimize for orientation, context, and discoverability.

2. **Who is the primary user?** Technical (developers, designers): higher density, command palette, keyboard-first. Non-technical (managers, sales): more visual, mouse-friendly, guided workflows.

3. **What is the data density requirement?** High (project management, analytics): compact rows, scrollable tables, filter systems. Low (note-taking, email): generous spacing, content-focused.

4. **Is dark mode the primary experience?** For developer tools and productivity apps: yes, dark mode first. For business dashboards and reporting: light mode likely default, dark mode as option.

5. **What competitive position are you targeting?** Premium (Superhuman, Linear): invest in custom typography, refined dark theme, subtle motion. Value (ClickUp, Asana): prioritize feature breadth and customization over visual refinement.

6. **How important are keyboard shortcuts?** If your power users spend 8+ hours/day in the product: keyboard shortcuts are mandatory, command palette is essential. If occasional use: keyboard shortcuts are nice-to-have.
