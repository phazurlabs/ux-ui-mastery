# Creator Tools & Social Media — Sector Style Intelligence

## Sector Overview

Creator tools and social media platforms represent two sides of the same coin: creation and distribution. Creator tools (Notion, Figma, Arc, Framer, Obsidian) optimize for focused production — minimal chrome, powerful features accessible through keyboard shortcuts, and interfaces that get out of the way of the creative process. Social media platforms (TikTok, Discord, Threads, BeReal) optimize for consumption and interaction — content-first design, engagement mechanics, and social dynamics that drive network effects.

Despite their differences, these sectors share critical DNA. Both prioritize speed (fast load times, instant feedback, responsive interactions). Both trend toward dark mode as default or strong preference. Both serve users who spend hours daily in the product, making ergonomic design decisions (reduced eye strain, efficient navigation) essential rather than nice-to-have. And both are increasingly converging — creator tools add social features (Figma's multiplayer, Notion's shared workspaces) while social platforms add creation tools (TikTok's editor, Discord's bots).

---

## Part 1: Social Media

### Color Psychology — Social Media

| Color | Association | Usage | Notes |
|---|---|---|---|
| **Black/Dark Gray** | Immersion, content focus, nightlife | Backgrounds, dark mode (often default) | Dark backgrounds make content POP |
| **White** | Cleanliness, content contrast | Light mode, content backgrounds | Less common as default — dark mode dominates |
| **Vibrant Accent** | Brand identity, CTAs, engagement | Unique per platform — recognition | Each platform owns a color |
| **Red** | Notifications, urgency, engagement | Notification badges, hearts, alerts | The universal attention magnet |
| **Blue** | Links, verification, trust | Verified badges, links, interactive elements | Meta blue, Twitter/X blue |
| **Green** | Online status, success, sent | Activity indicators, message status | Universal "online" signal |

### Palettes from Leading Social Apps

#### TikTok
```
Brand Cyan:         #25F4EE (Distinctive teal-cyan)
Brand Red:          #FE2C55 (Energetic red-pink)
Dark Background:    #000000 (Pure black — OLED optimized)
Surface Card:       #1A1A1A
Surface Elevated:   #2C2C2C
White:              #FFFFFF
Text Primary:       #FFFFFF (dark mode) / #161823 (light mode)
Text Secondary:     #8A8B91
Like Red:           #FE2C55
Comment:            #FFFFFF
Share:              #FFFFFF
Icon Default:       #FFFFFF
```
**Why it works:** TikTok's black background makes video content fill the entire viewport with zero distraction. The cyan-red brand duo creates visual tension that mirrors the platform's energy. These colors also create a distinctive "3D shadow" effect in the logo.

#### Discord
```
Blurple:            #5865F2 (Distinctive purple-blue — "blurple")
Dark Background:    #313338 (Not pure black — easier on eyes)
Sidebar Dark:       #2B2D31
Channel Background: #313338
Chat Background:    #313338
Input Background:   #383A40
Mention Highlight:  #3C4270 (Blurple tinted)
Green Online:       #23A559
Yellow Idle:        #F0B232
Red DND:            #F23F43
Gray Offline:       #80848E
Text Primary:       #F2F3F5
Text Secondary:     #B5BAC1
Text Muted:         #6D6F78
Nitro Pink:         #FF73FA
Boost Purple:       #FF73FA
```
**Why it works:** Discord's "blurple" is one of the most distinctive brand colors in tech — instantly recognizable. The dark gray (not pure black) background reduces eye strain during marathon gaming/chat sessions. The status color system (green/yellow/red/gray) is immediately intuitive.

#### Threads (Meta)
```
Primary Black:      #000000 (Dark mode default)
White:              #FFFFFF (Light mode)
Light Background:   #FAFAFA
Text Primary:       #000000 (light) / #FFFFFF (dark)
Text Secondary:     #999999
Link Blue:          #0095F6 (Instagram blue heritage)
Like Red:           #FF3040
Verified Blue:      #0095F6
Surface Dark:       #181818
Border Light:       #DBDBDB
Border Dark:        #2A2A2A
```
**Why it works:** Threads deliberately adopted a minimal, text-forward aesthetic that differentiates from image-centric Instagram. The near-monochrome palette puts content (text) front and center.

#### Mastodon
```
Primary Purple:     #6364FF (Fediverse purple)
Dark Background:    #191B22
Column Background:  #282C37
Header:             #1F232B
Text Primary:       #FFFFFF
Text Secondary:     #9BAEC8
Link Blue:          #2B90D9
Boost Green:        #2B90D9
Favorite Gold:      #CA8F04
CW Orange:          #E87839
```

### Typography — Social Media

| App | Primary Font | Why |
|---|---|---|
| **TikTok** | Proxima Nova, TikTok Sans (custom) | Clean, modern, excellent at small sizes on mobile |
| **Discord** | gg sans (custom), Whitney | Custom font with personality — friendly but readable at small sizes |
| **Threads** | System fonts (SF Pro, Roboto) | Speed and familiarity — text-first platform needs invisible typography |
| **Mastodon** | System fonts, Roboto | Performance — federated servers benefit from system fonts |
| **BeReal** | System fonts | Authenticity — custom fonts would feel too "designed" for the brand |

#### Social Media Typography Rules

1. **Username/handle hierarchy is critical.** Display name (16px, 600 weight) above @handle (14px, 400 weight, muted color). This is a universal social pattern.

2. **Post content uses standard body size.** 15-16px for post text. Never smaller — posts are the content.

3. **Timestamps are secondary.** 12-13px, muted gray, relative time ("2h" not "Feb 16, 2026 at 2:34 PM").

4. **Engagement counts use compact formatting.** "12.5K" not "12,500" — saves space and scans faster.

```
Display Name:    16px / 600 weight
Handle:          14px / 400 weight / muted color
Post Body:       15px / 400 weight / 1.5 line-height
Timestamp:       13px / 400 weight / muted
Engagement:      13px / 600 weight / tabular-nums
Tab Label:       12px / 600 weight
Notification:    14px / 400 weight
```

### Component Conventions — Social Media

#### Feed Post Card (Universal Pattern)

```css
.post-card {
  padding: 16px;
  border-bottom: 1px solid #2A2A2A; /* dark mode */
  /* No border-radius — full-width cards */
}
.post-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}
.post-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.post-username {
  font-size: 16px;
  font-weight: 600;
}
.post-handle {
  font-size: 14px;
  color: #8E8E93;
}
.post-timestamp {
  font-size: 13px;
  color: #8E8E93;
  margin-left: auto;
}
.post-content {
  font-size: 15px;
  line-height: 1.5;
  margin-bottom: 12px;
}
.post-actions {
  display: flex;
  gap: 40px;
  padding-top: 8px;
}
.post-action {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #8E8E93;
}
.post-action.liked {
  color: #FF3040;
}
```

#### Notification Badge
```css
.notification-badge {
  position: absolute;
  top: -4px;
  right: -4px;
  min-width: 18px;
  height: 18px;
  border-radius: 9px;
  background: #FF3040;
  color: #FFFFFF;
  font-size: 11px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 5px;
  border: 2px solid #000000; /* matches parent background */
}
```

#### Story/Status Ring
```css
.story-ring {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  background: linear-gradient(135deg, #FF8C00, #FF0080, #7928CA);
  padding: 3px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.story-ring .avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border: 3px solid #000000;
  object-fit: cover;
}
.story-ring.seen {
  background: #333333; /* Dimmed ring for viewed stories */
}
```

### Spacing — Social Media

Social media prioritizes content density — more posts visible = more engagement.

```
4px   — Micro (icon gaps, badge offsets)
8px   — Tight (inline engagement counts)
12px  — Standard (post internal spacing)
16px  — Card padding (post container)
20px  — Section headers
24px  — Between major sections
32px  — Page-level divisions
```

**Key principle:** Social feeds are deliberately dense. Whitespace between posts is minimal (1px border or 8px gap) to encourage continuous scrolling.

### Motion — Social Media

Social media motion is **fast, playful, and responsive.** Animations reward engagement and provide instant feedback.

#### Timing
```
Like animation:      300ms (heart pop + scale)
Double-tap heart:    400ms (expand from center, fade, confetti)
Pull to refresh:     200ms snap-back
Feed item load:      150ms fade-in with 30ms stagger
Story transition:    250ms (horizontal slide, cube effect)
Tab switch:          200ms (cross-fade or slide)
Swipe delete:        250ms (slide out + collapse)
Notification pop:    250ms (spring scale from 0 to 1)
```

#### Easing Curves
```css
/* Bouncy — like button, reactions */
transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1.0);

/* Quick snap — navigation, tab switches */
transition-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1.0);

/* Content slide — feed scrolling, story progression */
transition-timing-function: cubic-bezier(0.22, 1.0, 0.36, 1.0);

/* Dismiss — swipe away, delete */
transition-timing-function: cubic-bezier(0.4, 0.0, 1.0, 1.0);
```

#### Specific Patterns

- **Like heart:** Scale from 1.0 -> 1.3 -> 1.0 with 300ms spring ease. Color changes from gray to red simultaneously. Optional: particle burst of small hearts.
- **Double-tap like (Instagram pattern):** Large white heart appears at tap point, scales from 0 -> 1.2 -> 0 over 800ms. Semi-transparent, fades at end.
- **Swipe between stories:** Horizontal cube rotation, 250ms. Each story auto-advances with a top progress bar (linear fill over 5-15 seconds).
- **Pull to refresh:** Custom spinner (brand-colored), appears after 60px pull, snaps to loading position at 80px.
- **New post indicator:** Floating chip slides down from top, 300ms decelerate, stays for 3s, then slides up to dismiss.

### Trust Signals — Social Media

1. **Verification badges.** Blue checkmark, organization badge, government labels. Verification is a core trust mechanism.
2. **Content moderation visibility.** "This content may be sensitive" interstitials show the platform takes moderation seriously.
3. **Privacy controls.** "Who can reply," account privacy toggles, block/mute functionality — visible privacy controls signal user empowerment.
4. **Transparent algorithmic signals.** "Because you follow @user" or "Popular in your area" — explaining why content appears builds trust in the feed algorithm.
5. **Report mechanisms.** Easy-to-find report buttons (three-dot menu -> Report) signal accountability.

### Anti-Patterns — Social Media

1. **Infinite scroll with no orientation.** Users lose their place and feel trapped. Provide scroll position indicators, "Back to top" buttons, or save-for-later functionality.
2. **Dark patterns for engagement.** Designing notification systems to maximize dopamine hits rather than user value is ethically problematic and increasingly regulated.
3. **Hiding unfollow/mute.** If users cannot easily control their feed, they feel powerless. Unfollow must be as accessible as follow.
4. **Algorithmic opacity.** Users distrust feeds they cannot understand or control. Provide "Why am I seeing this?" and feed customization.
5. **Notification spam defaults.** Defaulting all notifications to ON is a dark pattern. Let users choose their notification level during onboarding.
6. **Follower count emphasis for non-celebrities.** Showing exact follower counts for all users promotes vanity metrics. Consider hiding counts below a threshold.

---

## Part 2: Creator Tools

### Color Psychology — Creator Tools

| Color | Association | Usage | Notes |
|---|---|---|---|
| **Dark Gray/Black** | Focus, canvas, minimal distraction | App background, canvas | Content is the star, not the UI |
| **White** | Canvas, clean workspace | Document background, editing area | The default canvas color |
| **Brand Accent** | Recognition, interactive elements | Primary CTA, selected states | Minimal use — the product is about user content |
| **Muted Colors** | Reduced distraction, peripheral | Secondary UI, toolbar backgrounds | UI elements should recede |
| **Syntax Colors** | Code highlighting, semantic meaning | In editors and code tools | Established by theme conventions |

### Palettes from Leading Creator Tools

#### Notion
```
Brand Black:        #000000 (Text-first brand)
Background:         #FFFFFF (Light mode canvas)
Dark Background:    #191919 (Dark mode)
Sidebar:            #F7F6F3 (Warm off-white — slight warmth)
Hover:              #EFEFEF
Text Primary:       #37352F (Warm near-black — NOT pure black)
Text Secondary:     #787774
Text Placeholder:   #C3C2BF
Accent Red:         #E03E3E
Accent Orange:      #D9730D
Accent Yellow:      #DFAB01
Accent Green:       #0F7B6C
Accent Blue:        #0068C9
Accent Purple:      #6940A5
Accent Pink:        #AD1A72
Border:             #E9E9E7
```
**Why it works:** Notion's palette is deliberately muted and warm. The warm near-black text (#37352F instead of #000000) and warm sidebar (#F7F6F3 instead of #F5F5F5) create a subtly more comfortable reading experience during long sessions. The multi-color accent system allows user categorization without competing with content.

#### Figma
```
Primary Blue:       #0D99FF (Figma blue — selection, interactive)
Dark Canvas:        #1E1E1E (Design canvas background)
Panel Background:   #2C2C2C (Side panels)
Surface:            #383838 (Elevated surfaces)
Text Primary:       #FFFFFF
Text Secondary:     #B3B3B3
Selection Blue:     #0D99FF (Consistent with primary)
Green Online:       #1BC47D (Multiplayer cursors, presence)
Cursor Colors:      #F24822, #14AE5C, #0D99FF, #9747FF, #FFCD29
                    (Distinct per collaborator)
Error Red:          #F24822
Warning Yellow:     #FFCD29
```
**Why it works:** Figma's UI is intentionally recessive — dark panels that disappear so the design canvas is the focus. The bright blue selection color is the most prominent UI element, directing attention to what the user is actively working on. Multiplayer cursor colors are the most vibrant elements in the interface.

#### Arc Browser
```
Primary:            User-chosen (Arc lets users pick their theme)
Default Sidebar:    #1A1A1A (Dark, minimal)
Default Tab Bar:    #2A2A2A
Surface:            #333333
Text Primary:       #FFFFFF
Text Secondary:     #999999
Space Colors:       User-configurable gradient system
                    Each space gets a distinct gradient
Active Tab:         Brighter, elevated from background
Boost Purple:       #7B61FF (Arc Boost features)
```
**Why it works:** Arc's radical personalization approach makes the browser feel like the user's own. The customizable color system per "space" (context) is both functional (visual context switching) and emotional (personal ownership).

#### Framer
```
Primary Blue:       #0099FF (Bright, creative blue)
Dark Background:    #111111 (Near black canvas)
Panel:              #1A1A1A
Surface:            #252525
Text Primary:       #FFFFFF
Text Secondary:     #808080
Accent Pink:        #FF0080 (Creative energy)
Accent Green:       #00FF87 (Success, publish)
Border:             #333333
Selection:          #0099FF
```

#### Obsidian
```
Background:         #1E1E1E (Default dark theme)
Editor Background:  #1E1E1E
Sidebar:            #1E1E1E (Unified with editor)
Text Primary:       #DCDDDE
Text Secondary:     #999999
Accent Purple:      #7F6DF2 (Default accent)
Link Blue:          #7F6DF2
Heading:            #DCDDDE (Same as body — markdown renders hierarchy)
Code Background:    #2D2D2D
Border:             #333333
Tag:                #8B6CEF
```

#### Substack
```
Primary Orange:     #FF6719 (Substack orange — writing energy)
Background:         #FFFFFF (Clean writing canvas)
Text Primary:       #000000
Text Secondary:     #6B6B6B
Surface:            #F7F7F7
Border:             #E5E5E5
Link:               #FF6719
Button Primary:     #FF6719
Button Text:        #FFFFFF
Card Background:    #FFFFFF
```

### Typography — Creator Tools

| App | Primary Font | Why |
|---|---|---|
| **Notion** | Inter (UI), Serif for content option | Inter for UI elements; users can choose serif/sans/mono for content |
| **Figma** | Inter | Clean, neutral, won't conflict with design content |
| **Arc** | System fonts (SF Pro) | Native feel, performance |
| **Framer** | Inter, custom display | UI consistency, custom fonts for marketing |
| **Obsidian** | User-configurable, default monospace | Writers and developers prefer monospace; full customization |
| **Substack** | Charter (serif for content), system for UI | Serif for reading content echoes publishing tradition |

#### Creator Tool Typography Rules

1. **Content typography must be user-configurable.** Creator tools are opinionated about UI fonts but flexible about content fonts. Users need serif, sans-serif, and monospace options.

2. **Small UI text is acceptable.** Creator tool users are typically younger, tech-savvy, and on high-resolution displays. 12-13px is acceptable for toolbar labels, panel headers, and metadata.

3. **Markdown rendering must be beautiful.** Heading hierarchy (H1-H6), code blocks, blockquotes, and lists must be visually distinct and aesthetically pleasing.

4. **Monospace for code contexts.** When displaying code, file names, or technical identifiers, switch to monospace. Common choices: JetBrains Mono, Fira Code, SF Mono.

```
UI Label:        12px / 500 weight / 0.02em tracking
UI Body:         13px / 400 weight
Panel Header:    11px / 600 weight / 0.06em tracking / uppercase
Content H1:      40px / 700 weight / -0.02em tracking
Content H2:      30px / 700 weight / -0.01em tracking
Content H3:      24px / 600 weight
Content Body:    16px / 400 weight / 1.6 line-height
Content Code:    14px / 400 weight / monospace / 1.5 line-height
Toolbar Icon:    20px (icon size)
Breadcrumb:      13px / 400 weight
```

### Component Conventions — Creator Tools

#### Border Radius
```
Buttons:           6px  (compact, professional)
Cards/Panels:      8px  (subtle softening)
Input Fields:      6px  (matches buttons)
Modals:            12px
Tooltips:          6px
Dropdowns:         8px
Context Menus:     8px
Command Palette:   12px (prominent, focal element)
Avatar:            4px or 50% (square with rounding OR circular)
Tags/Chips:        4px  (compact, information-dense)
```

**Key difference from social:** Creator tools use smaller radii — the interface is a professional tool, not a social experience.

#### Command Palette (Key Creator Pattern)

```css
.command-palette-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  padding-top: 20vh;
  z-index: 1000;
}
.command-palette {
  width: 560px;
  max-height: 420px;
  background: #2C2C2C;
  border: 1px solid #404040;
  border-radius: 12px;
  box-shadow: 0 16px 64px rgba(0, 0, 0, 0.4);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.command-palette-input {
  padding: 16px 20px;
  background: transparent;
  border: none;
  border-bottom: 1px solid #404040;
  color: #FFFFFF;
  font-size: 16px;
  outline: none;
}
.command-palette-input::placeholder {
  color: #808080;
}
.command-palette-results {
  overflow-y: auto;
  flex: 1;
  padding: 8px;
}
.command-palette-item {
  padding: 10px 12px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  color: #E0E0E0;
  font-size: 14px;
}
.command-palette-item.selected {
  background: #404040;
}
.command-palette-item .shortcut {
  margin-left: auto;
  font-size: 12px;
  color: #808080;
  font-family: monospace;
}
```

#### Sidebar Navigation (Creator Pattern)

```css
.sidebar {
  width: 240px;
  background: #1E1E1E;
  border-right: 1px solid #333333;
  display: flex;
  flex-direction: column;
  padding: 12px 8px;
  font-size: 13px;
}
.sidebar-section-header {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #808080;
  padding: 8px 12px;
  margin-top: 16px;
}
.sidebar-item {
  padding: 6px 12px;
  border-radius: 6px;
  color: #B3B3B3;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: background 0.1s ease;
}
.sidebar-item:hover {
  background: #2A2A2A;
  color: #FFFFFF;
}
.sidebar-item.active {
  background: #333333;
  color: #FFFFFF;
}
.sidebar-item .icon {
  width: 16px;
  height: 16px;
  opacity: 0.6;
}
.sidebar-item.active .icon {
  opacity: 1.0;
}
```

#### Multiplayer Cursor (Figma Pattern)

```css
.multiplayer-cursor {
  position: absolute;
  pointer-events: none;
  z-index: 999;
  transition: transform 0.1s linear;
}
.multiplayer-cursor .cursor-icon {
  width: 16px;
  height: 22px;
  /* SVG cursor shape, filled with user color */
}
.multiplayer-cursor .cursor-label {
  position: absolute;
  top: 20px;
  left: 12px;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  color: #FFFFFF;
  white-space: nowrap;
  /* Background color matches cursor color */
}
```

### Spacing — Creator Tools

Creator tools balance maximum workspace with usable UI elements.

```
2px   — Hairline (dividers between toolbar items)
4px   — Micro (icon padding, tight button groups)
6px   — Extra-tight (sidebar item vertical padding)
8px   — Tight (panel padding, between related items)
12px  — Default (between form elements, list items)
16px  — Standard (panel sections, card padding)
20px  — Comfortable (between major panel sections)
24px  — Section (between distinct areas)
32px  — Major (page-level divisions)
```

**Key principle:** Creator tool spacing is tight by default but must offer density controls. Power users want compact; new users need breathing room.

### Motion — Creator Tools

Creator tool motion is **instant, precise, and non-disruptive.** Animations must never slow down a power user's workflow.

#### Timing
```
Hover feedback:      50-80ms   (highlight, cursor change)
Click feedback:      80-120ms  (press state, selection)
Panel toggle:        150-200ms (sidebar show/hide)
Context menu:        100ms     (instant appearance)
Command palette:     150ms     (fast open, zero delay)
Canvas zoom:         200ms     (smooth zoom with easing)
Multi-select:        0ms       (instant — no animation)
Drag and drop:       Frame-locked (follows cursor, no lag)
Save indicator:      200ms fade-in, 2s visible, 300ms fade-out
```

#### Easing Curves
```css
/* Instant — toolbar interactions, no perceptible animation */
transition-timing-function: cubic-bezier(0.2, 0.0, 0.0, 1.0);

/* Quick ease — panel toggles, modal open */
transition-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1.0);

/* Smooth — canvas operations, zoom */
transition-timing-function: cubic-bezier(0.0, 0.0, 0.2, 1.0);
```

### Trust Signals — Creator Tools

1. **Auto-save indicators.** "All changes saved" with a subtle checkmark. Creator tools must never lose user work.
2. **Version history.** Visible "Last edited 2 minutes ago" with version history access signals data safety.
3. **Sync status.** Cloud sync indicators (synced/syncing/offline) build confidence in data persistence.
4. **Open-source or extensible.** Plugin ecosystems, API access, and open file formats signal that the tool respects user agency.
5. **Keyboard shortcut discoverability.** Showing shortcuts in menus and tooltips signals a professional tool designed for power users.
6. **Import/export.** "Your data is yours" — easy export to standard formats builds trust.

### Anti-Patterns — Creator Tools

1. **Animating everything.** A 300ms sidebar animation is 300ms of wasted time multiplied by hundreds of daily interactions. Creator tools should feel instant.
2. **Hiding keyboard shortcuts.** If users cannot discover shortcuts organically (through menus, tooltips, command palette), they never become power users.
3. **Lock-in through proprietary formats.** If users cannot export their work to standard formats, they feel trapped and will eventually leave.
4. **Feature bloat in the UI.** Every visible feature competes with the user's content for attention. Progressive disclosure is essential.
5. **Notifications during focus time.** Creator tools should suppress non-critical notifications during active editing sessions.
6. **Poor undo/redo.** If Cmd+Z does not work perfectly and consistently, the tool feels fundamentally untrustworthy.

---

## Reference Apps — What to Learn from Each

### TikTok
- **Lesson:** Full-screen, content-first design eliminates chrome entirely during consumption. Study how TikTok reduces the interface to content + minimal overlay controls.
- **Key pattern:** Full-screen vertical video with gesture-based navigation (swipe up = next), right-side action buttons (floating, semi-transparent), bottom navigation only visible on home/profile.
- **Engagement:** The For You page algorithm removes ALL navigation friction — users never need to search or browse. Content finds the user.

### Discord
- **Lesson:** Complex multi-panel layout that serves both casual and power users. Study how Discord manages server > channel > thread hierarchy without overwhelming new users.
- **Key pattern:** Three-panel layout (server list > channel list > chat), role-based color coding for usernames, thread expansion, voice channel presence indicators.
- **Community:** Discord's design enables different interaction modes (text, voice, video, screen share, stage) within a consistent spatial metaphor.

### Notion
- **Lesson:** The "/" command paradigm as a design system. Notion made block-based editing accessible by making everything accessible through typing "/". Study how command-driven UI can be more discoverable than menus.
- **Key pattern:** Block-based content (every paragraph, image, table is a "block"), slash commands for insertion, drag handles for reordering, database views (table, board, calendar, gallery).
- **Flexibility:** Notion's design system is built for maximum flexibility — the same data can be viewed as a table, kanban board, calendar, or gallery with one click.

### Figma
- **Lesson:** Multiplayer-first design in a creative tool. Study how Figma makes real-time collaboration feel natural — multiplayer cursors, comment threads on canvas, shared component libraries.
- **Key pattern:** Infinite canvas with spatial organization, left panel (layers/assets) + right panel (properties/design), component system with auto-layout, multiplayer cursors with user colors.
- **Collaboration:** The "Can view" / "Can edit" permission model and commenting system make design review a first-class feature.

### Substack
- **Lesson:** Writing tool that feels like writing, not like using a tool. Study Substack's minimal editor — it borrows from Medium's clean writing experience while adding newsletter-specific features (subscribe, paywall, discussion).
- **Key pattern:** Medium-inspired WYSIWYG editor, clean serif typography for published posts, inline image/embed insertion, subscriber management as simple dashboard.

### Arc Browser
- **Lesson:** Radical rethinking of established product paradigms. Arc reimagined the browser with spatial tab management, customizable theming per context, and built-in tools (notes, easel, split views). Study how to challenge deeply entrenched UX patterns.
- **Key pattern:** Sidebar-based tab management, spaces with distinct themes, auto-archiving of old tabs, command bar as primary navigation, boosts for customizing websites.

---

## W3C Design Token Starter Kit — Creator & Social

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "creator-social": {
    "color": {
      "social": {
        "background-dark": {
          "$value": "#000000",
          "$type": "color",
          "$description": "Pure black for OLED — content-first"
        },
        "surface-card": { "$value": "#1A1A1A", "$type": "color" },
        "surface-elevated": { "$value": "#2C2C2C", "$type": "color" },
        "text-primary": { "$value": "#FFFFFF", "$type": "color" },
        "text-secondary": { "$value": "#8A8B91", "$type": "color" },
        "text-muted": { "$value": "#6D6F78", "$type": "color" },
        "like-red": { "$value": "#FF3040", "$type": "color" },
        "notification-red": { "$value": "#FF3040", "$type": "color" },
        "link-blue": { "$value": "#0095F6", "$type": "color" },
        "online-green": { "$value": "#23A559", "$type": "color" },
        "border": { "$value": "#2A2A2A", "$type": "color" }
      },
      "creator": {
        "background": {
          "$value": "#1E1E1E",
          "$type": "color",
          "$description": "Dark canvas — not pure black, easier on eyes"
        },
        "surface-panel": { "$value": "#2C2C2C", "$type": "color" },
        "surface-elevated": { "$value": "#383838", "$type": "color" },
        "surface-hover": { "$value": "#404040", "$type": "color" },
        "canvas": { "$value": "#FFFFFF", "$type": "color" },
        "text-primary": { "$value": "#FFFFFF", "$type": "color" },
        "text-secondary": { "$value": "#B3B3B3", "$type": "color" },
        "text-muted": { "$value": "#808080", "$type": "color" },
        "accent-blue": {
          "$value": "#0D99FF",
          "$type": "color",
          "$description": "Selection and interactive elements"
        },
        "accent-green": { "$value": "#1BC47D", "$type": "color" },
        "border": { "$value": "#333333", "$type": "color" },
        "border-subtle": { "$value": "#2A2A2A", "$type": "color" }
      }
    },
    "typography": {
      "font-family-ui": {
        "$value": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "$type": "fontFamily"
      },
      "font-family-content": {
        "$value": "'Charter', 'Georgia', 'Times New Roman', serif",
        "$type": "fontFamily",
        "$description": "Serif for long-form reading content"
      },
      "font-family-mono": {
        "$value": "'JetBrains Mono', 'Fira Code', 'SF Mono', monospace",
        "$type": "fontFamily"
      },
      "font-size-ui-label": { "$value": "12px", "$type": "dimension" },
      "font-size-ui-body": { "$value": "13px", "$type": "dimension" },
      "font-size-ui-panel-header": { "$value": "11px", "$type": "dimension" },
      "font-size-content-h1": { "$value": "40px", "$type": "dimension" },
      "font-size-content-h2": { "$value": "30px", "$type": "dimension" },
      "font-size-content-h3": { "$value": "24px", "$type": "dimension" },
      "font-size-content-body": { "$value": "16px", "$type": "dimension" },
      "font-size-content-code": { "$value": "14px", "$type": "dimension" },
      "font-size-post-body": { "$value": "15px", "$type": "dimension" },
      "font-size-post-meta": { "$value": "13px", "$type": "dimension" }
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
      "section": { "$value": "32px", "$type": "dimension" }
    },
    "radius": {
      "tight": { "$value": "4px", "$type": "dimension" },
      "small": { "$value": "6px", "$type": "dimension" },
      "medium": { "$value": "8px", "$type": "dimension" },
      "large": { "$value": "12px", "$type": "dimension" },
      "full": { "$value": "9999px", "$type": "dimension" }
    },
    "motion": {
      "duration-instant": { "$value": "50ms", "$type": "duration" },
      "duration-micro": { "$value": "100ms", "$type": "duration" },
      "duration-fast": { "$value": "150ms", "$type": "duration" },
      "duration-normal": { "$value": "200ms", "$type": "duration" },
      "duration-engagement": { "$value": "300ms", "$type": "duration" },
      "easing-instant": {
        "$value": "cubic-bezier(0.2, 0.0, 0.0, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-standard": {
        "$value": "cubic-bezier(0.25, 0.1, 0.25, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-bouncy": {
        "$value": "cubic-bezier(0.34, 1.56, 0.64, 1.0)",
        "$type": "cubicBezier"
      }
    }
  }
}
```

---

## Inspiration Links

### Mobbin
- [Social media app screens](https://mobbin.com/browse/apps?category=social) — Feed patterns, profiles, messaging
- [Productivity tool screens](https://mobbin.com/browse/apps?category=productivity) — Editor UIs, dashboards

### Screenlane
- [Social app UI](https://screenlane.com/screens/category/social/) — Feeds, stories, messaging
- [Productivity app UI](https://screenlane.com/screens/category/productivity/) — Editors, command palettes, settings

### Additional Resources
- [Figma design system](https://www.figma.com/community/file/928108847914589057/Figma-UI-Kit) — Figma's own design system
- [Notion design inspiration](https://www.notion.so) — Study the product
- [Discord brand guidelines](https://discord.com/branding) — Color and typography reference
- [TikTok design team](https://tiktok.design) — Design case studies and process
