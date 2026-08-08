# Watch, TV, Automotive, Kiosk, and E-Ink Design Standards

---

## WATCH DESIGN

### Apple Watch (watchOS)

#### Screen Dimensions

| Model | Resolution (px) | Points |
|-------|-----------------|--------|
| Series 10 (42mm) | 374 x 446 | 187 x 223 @2x |
| Series 10 (46mm) | 416 x 496 | 208 x 248 @2x |
| Ultra 3 (49mm) | 422 x 514 | 211 x 257 @2x |

#### Always-On Display

Design for TWO states:
- **Full brightness**: normal interactive state — full color, all details visible
- **Dimmed state**: always-on resting state — reduced brightness, simplified layout, fewer colors
- In dimmed state: hide seconds in clocks, reduce animation to static, drop non-essential elements
- Use `.isLuminanceReduced` environment value to detect dimmed state

#### System Font

- **SF Compact**: default system font, optimized for small screens with wider letter spacing
- **SF Compact Rounded**: used for complications and glanceable data — friendlier appearance
- Minimum readable size: ~17pt system text (below this, legibility degrades significantly)
- Prefer 18-20pt for body text

#### OLED Considerations

- True blacks (#000000) save battery — OLED pixels are physically off for pure black
- Use pure black backgrounds as default
- Colored UI elements pop against black with high contrast
- Avoid large areas of white — they draw significant power
- System backgrounds are black by default

#### Digital Crown Interactions

- **Scroll**: rotate crown to scroll vertically through content
- **Zoom**: rotate crown to zoom in/out on maps, photos
- **Adjust values**: rotate to increment/decrement numeric values (time, volume)
- **Haptic feedback**: the crown provides haptic detents as you scroll
- Design scroll lists with clear item boundaries that align with haptic clicks

#### Double-Tap Gesture (Series 9+)

- Pinch thumb and index finger together to trigger the primary action
- The system assigns this to the most contextually appropriate action
- Typically: answer/end call, pause/play music, dismiss alarm, start/stop timer
- Only ONE action can be the double-tap target at any time
- Use `.handGestureShortcut(.primaryAction)` in SwiftUI

#### Navigation Patterns

**Hierarchical (Push/Pop)**
- NavigationStack: push detail views, swipe back
- Best for apps with clear parent-child content relationships
- Digital Crown scrolls within each view

**Page-Based (Horizontal Swipe)**
- TabView with .tabViewStyle(.page): swipe left/right between pages
- Best for apps with parallel, equally important views
- Maximum 5-7 pages (more becomes tedious to navigate)

#### Complications

Complications display glanceable data on watch faces:

| Type | Shape | Content |
|------|-------|---------|
| Circular | Round | Small icon + short value |
| Rectangular | Wide rectangle | Rich data, small chart |
| Corner | Quarter-circle arc | Gauge-style data |
| Inline | Single text line | Short text string |

- Use WidgetKit (same framework as iOS widgets)
- Refresh cadence: system-managed, typically every 15 minutes minimum
- Data must be meaningful at a glance — no paragraphs, no complex charts
- Tap a complication to launch the app

#### watchOS SwiftUI Patterns

```swift
// Basic watch app structure
NavigationStack {
    List {
        ForEach(items) { item in
            NavigationLink(item.title) {
                DetailView(item: item)
            }
        }
    }
    .navigationTitle("Items")
}

// Date display
Text(Date.now, style: .timer)  // Live-updating timer
Text(Date.now, style: .relative)  // "2 min ago"
```

---

### Wear OS (Material 3 Expressive)

#### Round Screen Challenges

- Round screens have ~22% less usable area than equivalent square screens
- Content at the four corners is clipped — do NOT place important content there
- Center the most critical information
- Use the round shape to your advantage: circular progress indicators, radial menus

#### Screen Size Breakpoint

- **225dp** is the key breakpoint separating smaller and larger Wear OS watches
- Below 225dp: reduce padding, use compact layouts
- Above 225dp: standard padding and spacing

#### Tile Layout (3-Slot)

Wear OS Tiles use a standard 3-slot layout:
1. **Title slot**: top area, brief title text
2. **Main content slot**: center area, primary information or action
3. **Bottom slot**: secondary action or supplementary info

#### Edge-Hugging Buttons

On round screens, buttons placed at the screen edges follow the curve:
- Curved button shapes complement the circular form factor
- Bottom-of-screen buttons curve along the bottom edge
- System-provided curved layouts handle this automatically

#### Typography

- **Variable fonts** recommended for dynamic sizing across screen sizes
- Minimum text: 16px (18-20px preferred for primary content)
- Roboto is the system font
- Avoid more than 2 type sizes per screen

#### Rotating Crown / Bezel

- Similar to Apple's Digital Crown: scroll, adjust values, navigate
- Samsung Galaxy Watch: physical rotating bezel (tactile)
- Haptic feedback on detents
- Scrollable lists should respect crown/bezel rotation

#### Tiles (Swipeable Information Cards)

- Horizontal swipe from the watch face to access tiles
- Each tile: one screen of glanceable information
- Tap tile to launch full app
- Maximum complexity: one primary data point + one action per tile

---

### Watch Design Principles (Cross-Platform)

**Glanceability**
- Information must be readable in 2-3 seconds — the user's wrist is raised, and they will lower it quickly
- If it takes more than 3 seconds to comprehend, redesign it

**Information Density**
- Maximum 3-4 pieces of information visible at any time
- One primary piece of info should dominate the screen
- Supporting data should be visually subordinate

**Full-Screen Pages**
- No split views, ever — the screen is too small
- One page = one purpose
- Vertical scrolling for overflow, but keep it short (3-4 screens maximum)

**Prioritization**
- Ask: what is the ONE thing the user needs right now?
- Surface that one thing prominently
- Everything else is secondary — accessible but not in the way

**Visual Design**
- Bold accent colors on black backgrounds for hierarchy
- High contrast is mandatory — watches are viewed in direct sunlight
- Large, bold numerals for data
- Minimal chrome — every pixel is precious

---

## TV DESIGN (10-FOOT UI)

### General TV Principles

#### Viewing Context

- **Viewing distance**: 8-12 feet (2.4-3.6 meters)
- **Lean-back posture**: relaxed, passive consumption
- **Shared screen**: multiple viewers may watch simultaneously
- **Dim environment**: TVs are typically in dimly lit rooms
- **Limited input**: remote control with D-pad, not a mouse or touch

#### Safe Zones

- **5% margin from all edges** (overscan safe zone)
- Some TVs crop the outer pixels — never place critical content at the very edge
- Title-safe zone: 10% margin for text
- For a 1920x1080 screen: 96px inset on each side (5%), 192px for titles (10%)

#### Visual Design

- **Content-first**: large imagery, hero content — TV is a visual medium
- **Dark themes default**: reduce eye strain in dim rooms, save energy on OLED TVs
- **Avoid pure white (#FFFFFF)**: use off-whites (e.g., #E0E0E0) or work on dark backgrounds — pure white causes bloom on TVs and is uncomfortable
- **Background darkness**: #121212 to #1E1E1E for surfaces (not pure black #000000 on LCD — too flat)
- **On OLED TVs**: pure black is acceptable and saves power

#### Typography

- **Minimum body text**: 24px (at 1080p, viewed from 8-12 feet)
- **Recommended body text**: 28-32px
- **Titles**: 40-60px
- **Bold and medium weights only**: thin/light weights become illegible at distance
- **Small type scale**: 5-6 sizes maximum — keep it simple
- **Line length**: 40-60 characters maximum per line
- **Sans-serif fonts only**: serifs blur at TV resolution and distance

---

### Focus-Based Navigation

#### D-Pad Navigation

TV remotes use directional input: up, down, left, right, select (OK/Enter), back.

**Grid Design for Focus**
- Every screen must be designed as a logical grid for predictable focus movement
- Focus should move in the direction the user presses — no unexpected jumps
- Test: can a user reach every interactive element with only D-pad presses?

**Focus Movement Rules**
- Pressing right from the last item in a row: do NOT wrap to the next row (confusing)
- Pressing down from a row: focus should land on the nearest item in the row below
- Focus memory: when returning to a previously visited row, restore the last focused position

#### Focus Indicators (4 States)

Every interactive element needs four distinct visual states:

| State | Visual Treatment |
|-------|-----------------|
| **Idle** | Default appearance, no emphasis |
| **Focused** | Scale up (1.1x-1.2x), add glow/shadow, brightness shift, or subtle animation |
| **Pressed** | Slight scale down (0.95x), color change, or opacity shift |
| **Loading** | Skeleton or spinner overlay |

- Focus indicators must be visible from 10+ feet away
- Scale is the most universally recognizable focus indicator
- Combine scale with a shadow or glow for added clarity
- No hover states (there is no cursor)

---

### tvOS Specific

#### Parallax Effect

tvOS's signature visual effect:
- Images are composed of 2-5 separate layers
- When an item receives focus, layers shift independently based on remote movement
- Creates a sense of depth and physicality
- Create layered images in the Apple TV Parallax Previewer app
- Use LSR (Layered Source) image format

#### Siri Remote

- Touch surface: swipe for scrolling and browsing, press for selection
- Menu button: back navigation
- TV button: return to TV app / home screen
- Siri button: voice search and commands
- Clickpad: press edges for directional input, center for select

#### Top Shelf

- Premium content showcase area visible from the Apple TV home screen
- Full-width, large imagery
- Two styles: sectioned content (scrollable row) or full-screen poster
- Use this space for the most compelling, current content

#### tvOS Focus Engine

- Automatic focus management — the system determines which element receives focus
- `focusable()` modifier to control focusability
- `@FocusState` for programmatic focus management
- `focusSection()` to group related elements for predictable navigation

---

### Android TV / Google TV

#### Leanback Library

- Android's TV-specific UI framework
- BrowseFragment: the Netflix-style rows of cards pattern
- DetailFragment: hero image + metadata + action buttons
- SearchFragment: voice-activated search results
- PlaybackFragment: media playback controls

#### Layout Pattern

- Horizontal rows of content cards
- Vertical scrolling between rows (categories)
- Each row: a content category with horizontally scrollable items
- Focused card scales up (1.12x) with shadow

#### Predictive Back Gesture

- System back animation shows a preview of the previous screen
- Support `onBackPressedDispatcher` for proper back navigation
- Predictive back provides visual continuity when navigating backward

#### Voice Actions (Google Assistant)

- "Play [content]" — deep link to media playback
- "Show [category]" — navigate to a content section
- "Search for [query]" — launch search results
- Implement MediaSession for voice-controlled playback

---

### Fire TV (Amazon)

#### Design Guidelines

- Overscan safe zone: 5% from all edges (same as general TV)
- Dark theme: #232F3E (Amazon dark blue) or custom dark palette
- Focus ring: 4px solid highlight, high contrast against background
- Card dimensions: 228x128dp (landscape), 138x200dp (portrait)

#### Alexa Voice Integration

- Voice is a primary navigation method
- "Alexa, open [app]" — launch
- "Alexa, play [content]" — media playback
- Implement Alexa voice capabilities for natural interaction

#### Navigation Pattern

- Hub and spoke: main menu (hub) with sub-sections (spokes)
- Left-side navigation rail for top-level categories
- Content area to the right
- Focus starts on the content area, rail accessible by pressing left

---

## AUTOMOTIVE DESIGN

### CarPlay / CarPlay Ultra

#### Screen Sizes and Context

- Screen sizes range from 6.5" to 15"+ (vehicle-dependent, specified by car manufacturer)
- CarPlay Ultra spans the full dashboard including instrument cluster
- Driver is operating a moving vehicle — SAFETY IS THE ABSOLUTE PRIORITY
- All design decisions must minimize distraction

#### Template-Based Design

CarPlay uses predefined templates — custom layouts are extremely limited:
- **List template**: scrollable list of items (messages, contacts, playlists)
- **Grid template**: grid of icons (app launcher style)
- **Information template**: metadata display (now playing)
- **Point of interest template**: map with markers
- **Tab bar template**: tabbed navigation between sections
- Custom drawing is NOT available — you work within Apple's template constraints

#### Visual Rules

- Dark themes are standard (reduce nighttime glare)
- System font only (SF Pro) — no custom typefaces
- Limited color palette — primary tint color + system colors
- Minimal imagery — icons and album art only, no decorative graphics

#### Safety Standards (NHTSA)

- **Glance time**: < 2 seconds per individual glance at the screen
- **Total task time**: < 12 seconds for any complete task
- **Maximum number of steps**: 6 for any task (fewer is better)
- Eyes-off-road time must be minimized

#### Restricted Categories

CarPlay only permits apps in these categories:
- Media (music, podcasts, audiobooks)
- Navigation (maps, directions)
- Messaging (send/receive with Siri)
- Point of Interest (parking, fuel, charging, food)
- IoT (home automation, car accessories)

---

### Android Auto / AAOS (Android Automotive OS)

#### Design Specifications

| Element | Specification |
|---------|--------------|
| Minimum font size | 24sp |
| Minimum touch target | 76 x 76dp |
| Minimum spacing between targets | 23dp |
| Contrast ratio | 4.5:1 minimum for ALL items |
| Maximum list items visible | 6 (scrolling limited) |

#### Why Larger Targets

- Driving vibration reduces touch precision
- The screen is not at a stable distance (arm extended to dashboard)
- Users cannot look at the screen for extended periods
- Width can be sacrificed for increased height (vertical targets are easier to hit while driving)

#### Day/Night Modes

- Automatic switching based on ambient light sensor or headlight status
- Day mode: higher contrast, brighter colors
- Night mode: significantly reduced brightness, limited color palette, no white backgrounds
- Both modes must meet 4.5:1 contrast ratio

#### Voice-First Design

- **Voice is the primary interaction while driving** — touch is secondary
- Design every task to be completable entirely by voice
- Google Assistant integration for commands
- Minimize required screen touches
- Provide voice confirmations for actions

---

### Automotive Design Principles (Cross-Platform)

**Safety FIRST**
- Never, under any circumstance, design an interaction that distracts the driver
- When in doubt, remove the feature or make it voice-only
- The driver's eyes belong on the road

**Glanceable**
- All displayed information must be comprehensible in under 2 seconds
- One primary piece of information per screen (song title, next turn, message sender)
- Icons over text where possible

**Large Touch Targets**
- 76dp minimum (Android Auto) / template-enforced (CarPlay)
- Generous spacing prevents mis-taps
- Physical vibration of the vehicle makes small targets unreachable

**High Contrast**
- Variable ambient lighting: direct sunlight to pitch darkness
- 4.5:1 contrast ratio as absolute minimum
- Test in both bright sunlight and complete darkness

**Voice-First**
- Every task should be completable by voice alone
- Screen interactions should be confirmations, not data entry
- Pre-compose message replies, not free-text input

**Restrict Complexity**
- 4-5 steps maximum per task
- 6 list items maximum visible at once
- No scrolling while driving (systems may lock scrolling when in motion)
- No video playback while driving (blocked by system)

---

## KIOSK DESIGN

### Screen Sizes and Contexts

- **Small kiosks**: 15-22" (self-checkout, check-in, ticketing)
- **Medium kiosks**: 22-32" (wayfinding, information, retail)
- **Large kiosks**: 32-55" (digital signage with touch, interactive displays)

### Interaction Design

**Linear Workflows**
- 4-5 steps maximum from start to completion
- Clear progress indicators (step 1 of 4)
- Always-visible cancel/start-over button
- No dead ends — every screen has a clear next action

**Touch Targets**
- 44px minimum, 1cm x 1cm (10mm) recommended for general public
- 15mm targets for elderly-focused kiosks
- Generous spacing between targets (8mm minimum)
- Large primary action buttons (full-width or prominent placement)

### Accessibility (ADA Compliance)

- **Accessible height**: interactive elements between 15" and 48" from floor
- **Wheelchair reach**: forward reach maximum 48", side reach maximum 54"
- **Voice guidance**: text-to-speech for all screen content
- **Adjustable fonts**: user-selectable text size
- **High contrast mode**: user-activatable
- **Timeout extensions**: allow users to request more time
- **Physical braille**: on hardware buttons if present

### Environmental Considerations

**Outdoor Kiosks**
- Screen brightness: 2,500-5,000 nits (vs ~500 nits for indoor)
- Anti-reflective coatings on screen
- Sunlight-readable designs: high contrast, bold colors
- Weatherproof touch (works with gloves, rain on screen)

**Indoor Kiosks**
- Standard brightness: 300-500 nits
- Consider ambient lighting (retail stores vary widely)
- Glare from overhead lights — angle screen slightly

### Session Management

- **Idle timeout**: 30-60 seconds of inactivity → attract screen
- **Attract screen**: motion graphics or clear "Touch to start" prompt
- **Privacy**: clear all personal data on session end
- **Error recovery**: automatic reset after extended error state
- **Receipt/confirmation**: provide before ending session

---

## E-INK DESIGN

### Display Characteristics

**Monochrome First**
- Standard E Ink: black, white, and 16 levels of gray
- Design primarily for monochrome — it is the most common E Ink type
- Gray levels are visible but lack the precision of LCD grayscale

**Color E Ink (Kaleido 3, Gallery 3)**
- Kaleido: color filter over monochrome — colors appear ~40% less vivid than LCD
- Gallery: native color E Ink — better but still muted
- Never rely on color alone to convey meaning — it may be invisible on monochrome devices
- Desaturated color palettes work best — vivid colors look muddy

### Refresh Behavior

- **Full refresh**: 100-300ms, flashes black before redrawing — best quality, most disruptive
- **Partial refresh**: faster, updates only changed regions — may leave ghosting artifacts
- **Fast/A2 mode**: near-instant updates, lowest quality, significant ghosting
- **Regal waveform**: optimized for mixed content, balances speed and quality

Design implications:
- NO animations — each frame requires a refresh cycle
- Minimize full-screen redraws (they flash the entire screen black/white)
- Design state changes as page transitions, not smooth animations
- Progress indicators: use discrete steps, not smooth bars

### Typography for E-Ink

- Fonts with open counters and healthy x-height reproduce best
- Recommended: Literata, Bookerly, Charter, Georgia
- Pure black (#000000) on pure white (#FFFFFF) for body text — no subtle grays for text
- Minimum body text: 12pt (16pt preferred for extended reading)
- Line spacing: 1.4-1.6x for comfortable reading
- Avoid thin/light weights — they render poorly on E Ink

### Layout Principles

**Page-Based, Not Scroll-Based**
- E Ink devices are optimized for page turns, not smooth scrolling
- Each page should be a complete, self-contained unit of content
- Pagination over infinite scroll

**Minimize Redraws**
- Every pixel change costs energy and time
- Group related updates into single redraws
- Avoid idle animations, blinking cursors, or live clocks with seconds

**Battery Considerations**
- E Ink displays consume power only when changing the image
- A static page consumes zero display power
- This enables weeks of battery life — design to take advantage of it
- Avoid frequent automatic refreshes

**Contrast and Readability**
- Pure black on white for text (no anti-aliased gray text — it looks fuzzy on E Ink)
- Borders and dividers: use solid 1-2px black lines, not subtle grays
- Icons: solid, filled styles work better than outline styles
- Images: convert to high-contrast, dithered versions for best results

### Common E-Ink Devices

| Device | Screen | Color | Interaction |
|--------|--------|-------|-------------|
| Kindle | 6-10.2" | Monochrome | Touch + buttons |
| Kobo | 6-10.3" | Mono / Kaleido | Touch |
| reMarkable | 10.3" | Monochrome | Pen + touch |
| Boox | 6-13.3" | Mono / Kaleido | Pen + touch (Android) |
| Daylight | 10.5" | Monochrome | Touch (backlit) |

### E-Ink Design Checklist

- [ ] All text is pure black on white (no gray text)
- [ ] No animations or smooth transitions
- [ ] Page-based navigation, not scroll-based
- [ ] Icons are solid/filled, not outline
- [ ] Color is not the sole indicator of meaning
- [ ] Large touch targets (E Ink response is slower than LCD)
- [ ] Minimal full-screen redraws
- [ ] Tested at actual E Ink refresh rates
- [ ] Font has open counters and healthy x-height
- [ ] Layout works in both portrait and landscape
