# UI Element Deep-Dive — 26 Element Patterns

> For each element: anatomy, variants, states, platform differences, accessibility requirements, and common mistakes.

---

## 1. Button

**Anatomy:**
- Container (background shape: rectangle, rounded, pill)
- Label text (centered, sentence case)
- Optional leading icon (left of label)
- Optional trailing icon (right of label, e.g., arrow)
- Focus ring (visible on keyboard focus)

**Variants:**
- **Primary** — Filled background, brand color, highest emphasis
- **Secondary** — Outlined or muted fill, medium emphasis
- **Tertiary / Ghost** — Text only, no background, low emphasis
- **Destructive** — Red fill or outline, for delete/remove actions
- **Icon-only** — No label, icon with tooltip
- **FAB (Floating Action Button)** — Circular, elevated, primary creation action
- **Sizes:** Small (32px), Medium (40px), Large (48px)

**States:**
- **Default** — Resting appearance
- **Hover** — Slight darkening or elevation (desktop only)
- **Focus** — Visible focus ring (2px offset, contrasting color)
- **Active/Pressed** — Darker fill, slight scale-down
- **Disabled** — Reduced opacity (0.4-0.5), no pointer events, `aria-disabled`
- **Loading** — Spinner replaces or sits next to label, width preserved to prevent layout shift

**Platform differences:**
- **iOS** — System button styles (tinted, filled, plain), 44pt minimum height, SF Symbols for icons
- **Android** — Material 3 buttons (Filled, Outlined, Text, Elevated, Tonal), 48dp minimum height, ripple effect
- **Web** — Custom styling, `:focus-visible` for keyboard-only focus ring, `<button>` element (not `<div>`)

**Accessibility requirements:**
- Use `<button>` or `role="button"` (never a styled `<div>` or `<a>` for actions)
- `aria-label` for icon-only buttons ("Add to cart", not "Plus")
- Disabled buttons: `aria-disabled="true"` (not `disabled` attribute if you want screen readers to find them)
- Loading state: `aria-busy="true"` + `aria-label` update ("Saving..." instead of "Save")
- Minimum touch target: 44x44pt (iOS) / 48x48dp (Android)
- Color contrast: 4.5:1 for text on button background

**Common mistakes:**
1. Using `<a>` for actions (buttons do things, links go places)
2. Disabled button with no explanation of why it's disabled (add tooltip or helper text)
3. Button width changes between states (loading spinner makes button wider/narrower)

---

## 2. Card

**Anatomy:**
- Container (rounded corners, optional shadow/border)
- Header area (title, subtitle, action button)
- Media area (image, video, or illustration)
- Content area (body text, data, details)
- Action area (buttons, links, footer actions)

**Variants:**
- **Elevated** — Shadow for depth, interactive feel
- **Outlined** — Border, flat, often used in grids
- **Filled** — Subtle background color, no shadow
- **Interactive** — Entire card is clickable (hover state on full card)
- **Expandable** — Card expands to show more content
- **Sizes:** Compact (list item size), Standard (grid card), Featured (hero card)

**States:**
- **Default** — Resting
- **Hover** — Slight elevation increase or border highlight (for interactive cards)
- **Focus** — Focus ring around entire card (for interactive cards)
- **Selected** — Checkmark overlay or highlighted border
- **Loading** — Skeleton version of the card
- **Error** — Error message within card area

**Platform differences:**
- **iOS** — Grouped content in rounded rectangles, inset grouped style
- **Android** — Material 3 cards (Elevated, Filled, Outlined), 12dp corner radius
- **Web** — Custom, often used in grids, `<article>` or `<section>` semantically

**Accessibility requirements:**
- Interactive card: wrap in `<a>` or `<button>`, or use `role="link"` / `role="button"`
- If card has multiple interactive elements inside, avoid making the entire card a link (nested interactive elements)
- Card title should be a heading at the appropriate level
- Image in card: descriptive `alt` text
- Card group: use `<ul>` + `<li>` for lists of cards

**Common mistakes:**
1. Entire card is clickable but contains other buttons inside (nested interactives — confusing click targets)
2. No discernible border or shadow — cards blend into background
3. Inconsistent card heights in a grid (no fixed aspect ratio or content truncation)

---

## 3. Modal / Dialog

**Anatomy:**
- Overlay/backdrop (semi-transparent dark background)
- Container (centered card with max-width, rounded corners)
- Header (title + close button, top-right X)
- Body (content, form, or confirmation message)
- Footer (action buttons: primary right, cancel left)

**Variants:**
- **Alert dialog** — Simple message + confirm/cancel (destructive confirmation)
- **Form dialog** — Contains form inputs, longer content
- **Full-screen dialog** — Mobile primarily, replaces entire view
- **Side sheet** — Slides in from right (desktop, for detail panels)
- **Sizes:** Small (400px), Medium (560px), Large (720px)

**States:**
- **Opening** — Fade/scale-in animation (150-200ms)
- **Open** — Focus trapped, backdrop visible
- **Closing** — Fade/scale-out animation
- **Scrollable** — Body scrolls, header/footer fixed
- **Loading** — Skeleton or spinner within body

**Platform differences:**
- **iOS** — `.sheet` (bottom sheets), `.alert`, `.fullScreenCover` in SwiftUI, rounded 14pt corners
- **Android** — Material 3 Dialog, Full-screen dialog, bottom sheets, 28dp corner radius
- **Web** — `<dialog>` element with `showModal()`, or ARIA `role="dialog"` + `aria-modal="true"`

**Accessibility requirements:**
- Focus trapped within modal (Tab cycles through modal controls only)
- `role="dialog"` + `aria-modal="true"` + `aria-labelledby` pointing to title
- Escape key closes modal
- Focus returns to trigger element on close
- Backdrop click to close (with confirmation if form has unsaved data)
- Announce modal opening: focus moves to first focusable element or title
- Alert dialog: `role="alertdialog"` for urgent confirmations

**Common mistakes:**
1. No focus trap — user can Tab into the background
2. Focus doesn't return to trigger on close (user is lost on the page)
3. Modal over modal (stacking modals creates confusion — use one at a time)

---

## 4. Bottom Sheet

**Anatomy:**
- Handle bar (drag indicator at top center, 36x5px rounded)
- Header (optional title + close button)
- Content area (scrollable)
- Background overlay (dim behind sheet)

**Variants:**
- **Peek** — Shows partial content (30-40% height), expandable
- **Half-screen** — 50% height, common for menus and selections
- **Full-screen** — Expanded to near-full height, close button required
- **Non-modal** — No overlay, content behind remains interactive
- **Persistent** — Always visible, not dismissible (map bottom panels)

**States:**
- **Collapsed** — Peek height, drag up to expand
- **Half-expanded** — Middle detent
- **Fully expanded** — Maximum height
- **Dismissing** — Swipe down past threshold to close
- **Scrolling** — Content scrolls within sheet, sheet itself stays at detent

**Platform differences:**
- **iOS** — `UISheetPresentationController`, detents (medium/large), grabber visible
- **Android** — Material 3 `BottomSheetBehavior`, three states (collapsed, half, expanded)
- **Web** — Custom implementation, touch events for drag, CSS for transitions

**Accessibility requirements:**
- `role="dialog"` when modal, `aria-label` for sheet purpose
- Handle bar: `role="slider"` or visual-only (with button alternative to expand/collapse)
- Swipe-to-dismiss: must have close button alternative (swipe is not accessible to all)
- Focus management same as modal when sheet is modal
- Announce sheet content on open

**Common mistakes:**
1. No close button — only swipe to dismiss (not accessible)
2. Scroll conflicts: content scroll vs. sheet drag fight each other
3. No defined detents — sheet can rest at any height (feels unfinished)

---

## 5. Banner / Alert

**Anatomy:**
- Container (full-width bar at top of page/section)
- Icon (leading, type-specific: info, success, warning, error)
- Message text (concise, single line or max 2 lines)
- Action link/button (optional: "Learn more", "Dismiss", "Undo")
- Close/dismiss button (X icon, trailing)

**Variants:**
- **Informational** — Blue/neutral, general announcements
- **Success** — Green, action completed
- **Warning** — Yellow/amber, potential issue
- **Error** — Red, something went wrong
- **Promotional** — Branded color, feature announcements
- **Placement:** Top of page (global), inline within section (contextual)

**States:**
- **Visible** — Displayed with content
- **Dismissing** — Slide-up or fade-out animation
- **Dismissed** — Removed from DOM or hidden
- **Persistent** — Cannot be dismissed (critical system alerts)

**Platform differences:**
- **iOS** — Typically custom, no standard system banner component
- **Android** — Material 3 Snackbar (temporary) vs. Banner (persistent, in content)
- **Web** — Custom, often `role="alert"` or `role="status"`, positioned fixed or in-flow

**Accessibility requirements:**
- Error/warning banners: `role="alert"` (immediately announced)
- Info/success banners: `role="status"` (announced at next pause)
- Dismiss button: `aria-label="Dismiss alert"`
- Do not rely on color alone — icon + text convey type
- Ensure sufficient contrast on colored backgrounds
- Auto-dismiss: provide enough time to read (minimum 5 seconds + 1 second per 120 words)

**Common mistakes:**
1. Auto-dismissing error banners before user can read them
2. Banner pushes content down causing layout shift (use fixed position or reserve space)
3. Color-only type indication (red for error, green for success) without icon or text label

---

## 6. Toast / Snackbar

**Anatomy:**
- Container (small, rounded, elevated card at bottom of screen)
- Message text (short, 1 line max)
- Optional action button ("Undo", "View")
- Optional dismiss button or auto-dismiss timer

**Variants:**
- **Simple** — Text only ("Saved")
- **Action** — Text + action button ("Deleted. Undo")
- **Icon** — Leading icon + text ("Email sent" with checkmark)
- **Multi-line** — Two lines max (avoid if possible)

**States:**
- **Entering** — Slide up from bottom or fade in
- **Visible** — 4-8 seconds visible
- **Exiting** — Slide down or fade out
- **Queued** — Multiple toasts queue, one visible at a time (not stacked)

**Platform differences:**
- **iOS** — No standard toast; use custom or avoid in favor of inline feedback
- **Android** — Material 3 Snackbar, 48dp height, bottom-aligned, supports action
- **Web** — Custom, positioned `fixed` at bottom center or bottom left

**Accessibility requirements:**
- `role="status"` + `aria-live="polite"` (announced without interrupting)
- For critical toasts: `role="alert"` + `aria-live="assertive"`
- Action button must be keyboard accessible during toast duration
- Auto-dismiss timer must be long enough (minimum 5 seconds)
- Do not use toast for critical errors (use inline alerts instead)
- Provide alternative feedback for screen reader users who may miss timed toasts

**Common mistakes:**
1. Using toast for error messages (errors should persist until resolved, not auto-dismiss)
2. Stacking multiple toasts (confusing — queue them)
3. Toast blocks important UI elements (position carefully, especially on mobile)

---

## 7. Tab Bar

**Anatomy:**
- Container (bar at bottom of screen on mobile, top of content on desktop)
- Tab items (3-5 items, each with icon + label)
- Active indicator (filled icon, colored label, or underline/pill)
- Badge (notification count on tab icon)

**Variants:**
- **Bottom tab bar** — Mobile primary navigation (3-5 tabs)
- **Top tab bar** — Content section switching (scrollable if many)
- **Segmented control** — Toggle between 2-3 views within a section
- **Scrollable tabs** — More than 5 options, horizontally scrollable

**States per tab:**
- **Default** — Outlined icon, muted label
- **Active** — Filled icon, colored label, indicator
- **Badge** — Red dot or count on icon
- **Disabled** — Grayed out (rare for navigation tabs)

**Platform differences:**
- **iOS** — `UITabBarController`, SF Symbols, labels always visible, bottom safe area
- **Android** — Material 3 Navigation Bar, 3-5 destinations, labeled icons
- **Web** — Custom or framework component, responsive (tabs on desktop, hamburger or bottom bar on mobile)

**Accessibility requirements:**
- Container: `role="tablist"` (for content tabs) or `role="navigation"` (for navigation)
- Tab items: `role="tab"` with `aria-selected` (content) or links with `aria-current="page"` (navigation)
- `aria-label` on tablist: "Main navigation" or "Content sections"
- Badge count: `aria-label` includes count ("Notifications, 3 unread")
- Keyboard: Arrow keys to move between tabs, Enter/Space to activate

**Common mistakes:**
1. More than 5 items in a bottom tab bar (use 3-5, with "More" overflow if needed)
2. No labels on icons (icon-only tabs are ambiguous, especially for new users)
3. Active state not visually distinct enough from default

---

## 8. Navigation Bar

**Anatomy:**
- Container (top of screen, fixed position)
- Back button / hamburger menu (leading, left)
- Title text (centered on iOS, left-aligned on Android, or centered/left on web)
- Action buttons (trailing, right: search, share, more)
- Optional: large title (scrolls to inline), subtitle

**Variants:**
- **Standard** — Fixed top bar with title and actions
- **Large title** — Expanded title that collapses on scroll (iOS pattern)
- **Transparent** — Overlaid on content (hero images, maps)
- **Search-integrated** — Search bar embedded in nav bar
- **Toolbar** — Action buttons without navigation context

**States:**
- **Default** — Full visibility, large title if applicable
- **Scrolled** — Collapsed title, background becomes opaque (if transparent)
- **Search active** — Search bar expanded, title hidden
- **Hidden** — Scrolled away (auto-hide on scroll down, reveal on scroll up)

**Platform differences:**
- **iOS** — `UINavigationBar`, automatic large title, back button with previous title, system blur background
- **Android** — Material 3 Top App Bar (small, medium, large), collapsing toolbar
- **Web** — Custom, sticky position, responsive breakpoints for hamburger conversion

**Accessibility requirements:**
- `role="navigation"` or `<nav>` with `aria-label="Main"` or contextual label
- Back button: `aria-label="Back"` or `aria-label="Back to [previous page]"`
- Title: use heading element (`<h1>` for page title)
- Action buttons: `aria-label` for icon-only buttons
- Skip navigation link: hidden link before nav to jump to main content

**Common mistakes:**
1. Title truncated without full title accessible anywhere
2. Too many action buttons (max 2-3 in nav bar, overflow to "more" menu)
3. Back button and hamburger menu on the same screen (conflicting navigation models)

---

## 9. Search Bar

**Anatomy:**
- Container (rounded rectangle input)
- Search icon (leading, magnifying glass)
- Text input area
- Clear button (trailing, appears when text is present)
- Cancel button (trailing, appears on focus — mobile)
- Optional: voice input button, filter icon, scanner/camera icon

**Variants:**
- **Standalone** — Prominent, full-width search field (search-first experiences)
- **In navigation** — Integrated into top nav bar
- **Expandable** — Icon-only that expands to full field on tap
- **With filters** — Filter chips or dropdown within/below search bar

**States:**
- **Default** — Placeholder text ("Search...", or specific: "Search products...")
- **Focused** — Cursor active, keyboard open, suggestions may appear below
- **Typing** — Clear button appears, autocomplete suggestions
- **Results** — Search submitted, results displayed
- **No results** — "No results" state within results area

**Platform differences:**
- **iOS** — `UISearchBar`, system styling, cancel button on focus, pull-to-reveal in lists
- **Android** — Material 3 Search Bar (docked) and Search View (full-screen), leading icon
- **Web** — `<input type="search">`, clear button styling varies by browser, custom autocomplete

**Accessibility requirements:**
- `role="searchbox"` or `<input type="search">`
- `aria-label="Search"` or visible label
- Autocomplete dropdown: `role="listbox"` with `aria-activedescendant`
- Clear button: `aria-label="Clear search"`
- Voice input: `aria-label="Voice search"`
- Results count announced: `aria-live="polite"` on results region

**Common mistakes:**
1. Placeholder text is the only label (disappears on typing, screen readers may miss it)
2. No clear button — user has to select-all and delete
3. Search requires pressing Enter — no search-as-you-type for simple queries

---

## 10. Input Field

**Anatomy:**
- Label (above or floating within field)
- Container (border/underline)
- Input area (text entry)
- Leading icon (optional: email, phone, search)
- Trailing icon (optional: clear, toggle visibility, validation indicator)
- Helper text (below field: guidance or character count)
- Error text (replaces helper text on error, red)

**Variants:**
- **Text** — Single-line text input
- **Textarea** — Multi-line, expandable
- **Password** — Obscured with show/hide toggle
- **Number** — Numeric keyboard, stepper optional
- **Email** — Email keyboard layout
- **Phone** — Phone number with country code prefix
- **Floating label** — Label moves from placeholder position to above on focus
- **Outlined** — Container with border
- **Filled** — Container with background fill + underline

**States:**
- **Default** — Empty, resting
- **Focused** — Border highlight, label floated, cursor active
- **Filled** — Has value, label floated
- **Error** — Red border, error icon, error text below
- **Disabled** — Grayed out, no interaction
- **Read-only** — Visible but not editable, selectable for copy
- **Success** — Green checkmark (for validation like "Username available")

**Platform differences:**
- **iOS** — `UITextField`, no built-in floating label, rounded rectangle style, `.textContentType` for autofill
- **Android** — Material 3 `TextInputLayout`, filled or outlined, built-in floating label, `inputType` for keyboard
- **Web** — `<input>` with `<label>`, custom floating label animation, `autocomplete` attribute

**Accessibility requirements:**
- `<label>` associated with `<input>` via `for`/`id`
- Error: `aria-describedby` linking input to error message, `aria-invalid="true"`
- Helper text: `aria-describedby` linking input to helper text
- Required: `aria-required="true"` + visual indicator (asterisk)
- Floating label: must remain visible as a label when field is focused/filled
- Character count: accessible to screen readers via `aria-describedby`

**Common mistakes:**
1. Placeholder text as the only label (disappears on focus, not accessible)
2. Error message replaces helper text permanently (user loses the guidance)
3. No `autocomplete` attribute (browsers can not auto-fill, users type more)

---

## 11. Toggle / Switch

**Anatomy:**
- Track (horizontal bar or pill)
- Thumb (circular indicator that slides)
- Label (text describing what the toggle controls)
- Optional: on/off text, icon within thumb

**Variants:**
- **Standard** — On/off binary toggle
- **With labels** — "On"/"Off" or "Yes"/"No" text
- **With icons** — Sun/moon for light/dark mode
- **Compact** — Smaller toggle for dense interfaces

**States:**
- **Off** — Track muted, thumb left
- **On** — Track colored (green/brand), thumb right
- **Disabled off** — Grayed track, no interaction
- **Disabled on** — Grayed but in on position
- **Focused** — Focus ring around toggle
- **Transitioning** — Thumb animating between positions (150ms)

**Platform differences:**
- **iOS** — `UISwitch`, green on-state, 51x31pt, no label text on track
- **Android** — Material 3 Switch, thumb with icon option, 52x32dp
- **Web** — Custom or `role="switch"`, no native switch element in HTML

**Accessibility requirements:**
- `role="switch"` (preferred) or `role="checkbox"` with `aria-checked`
- `aria-label` or associated `<label>` describing the setting
- State change announced by screen reader ("On" / "Off")
- Keyboard: Space to toggle
- Do not use toggle for actions that require save — toggle implies immediate effect

**Common mistakes:**
1. Using toggle for settings that require a save button (confuses immediate vs. deferred save)
2. No visible label near the toggle (what does this toggle do?)
3. "On" state not visually distinct enough from "Off" (use color + position + optional text)

---

## 12. Chip / Tag

**Anatomy:**
- Container (pill shape, small)
- Label text
- Optional leading icon or avatar
- Optional trailing close/remove button (X icon)

**Variants:**
- **Input chip** — Represents user input, removable (email recipients, tags)
- **Filter chip** — Selected/unselected state for filtering (categories, options)
- **Suggestion chip** — Tappable suggestions (autocomplete options)
- **Assist chip** — Action shortcuts (smart replies)

**States:**
- **Default** — Outlined or subtle fill
- **Selected** — Filled or checkmark + fill (filter chips)
- **Hover** — Slight background change
- **Focus** — Focus ring
- **Disabled** — Muted, no interaction

**Platform differences:**
- **iOS** — No standard chip; custom pill-shaped buttons
- **Android** — Material 3 Chip (assist, filter, input, suggestion), 32dp height
- **Web** — Custom, `role="option"` (filter) or `role="button"` (action)

**Accessibility requirements:**
- Filter chips: `role="checkbox"` with `aria-checked`, or `role="option"` within `role="listbox"`
- Input chips with remove: `aria-label="Remove [value]"` on X button
- Chip group: `role="group"` with `aria-label`
- Keyboard: Enter/Space to select, Delete/Backspace to remove input chips

**Common mistakes:**
1. Chips too small to tap (minimum 32dp height for touch targets)
2. Remove button too small or too close to the label (accidental removals)
3. No visual feedback on selection state (which chips are active?)

---

## 13. Avatar

**Anatomy:**
- Container (circle or rounded square)
- Image (user photo, cropped to container)
- Fallback (initials on colored background if no image)
- Optional: status indicator (online dot), badge, border

**Variants:**
- **Sizes:** XS (24px), S (32px), M (40px), L (48px), XL (64px), XXL (96px+)
- **Shape:** Circle (most common), rounded square (workspace icons)
- **Group:** Overlapping avatars for group representation (show 3-5 + "+N")
- **With status:** Green dot = online, gray = offline, yellow = away

**States:**
- **Image loaded** — Photo displayed
- **Image loading** — Gray circle or shimmer placeholder
- **Image error** — Initials fallback
- **No image set** — Initials or generic person icon

**Platform differences:**
- **iOS** — Custom `UIImageView` with corner radius, `AsyncImage` in SwiftUI
- **Android** — `ShapeableImageView`, Material 3 does not have a standard avatar component
- **Web** — `<img>` with `border-radius: 50%`, CSS object-fit: cover

**Accessibility requirements:**
- `alt="[Person's name]"` on image avatar
- Initials fallback: `aria-label="[Person's name]"` (initials alone are not descriptive)
- Status indicator: text alternative ("Online", "Away") not just color dot
- Avatar group: `aria-label="Group: [name1], [name2], and 3 others"`
- Decorative avatars: `alt=""` if name is displayed as text nearby

**Common mistakes:**
1. No fallback for missing images (broken image icon shown)
2. Initials on clashing background color (poor contrast)
3. Status dot relies only on color (add tooltip or text label)

---

## 14. Badge

**Anatomy:**
- Container (small circle or pill)
- Count text (number) or empty (dot indicator)
- Position (overlapping the corner of parent element)

**Variants:**
- **Dot** — No count, just presence indicator (something new)
- **Count** — Shows numeric count (3, 99, 99+)
- **Label** — Text badge ("New", "Beta", "Pro")
- **Status** — Colored dot for status (green = active, red = error)

**States:**
- **Hidden** — Count is zero, badge not rendered
- **Dot** — Something new, count unknown or irrelevant
- **Low count** — Shows number (1-99)
- **High count** — "99+" for three-digit counts
- **Animated** — Brief scale animation on count change

**Platform differences:**
- **iOS** — `.badge()` modifier in SwiftUI, system red pill on tab bar icons
- **Android** — `BadgeDrawable` in Material 3, top-right corner positioning
- **Web** — CSS positioned element, `position: absolute` relative to parent

**Accessibility requirements:**
- Badge count: include in parent element's `aria-label` ("Notifications, 3 unread")
- Do not make the badge itself a separate interactive element
- Dot badge: "new content available" conveyed in parent label
- Ensure badge is visible against parent background (contrast)

**Common mistakes:**
1. Badge obscures important content behind it (position carefully)
2. No maximum count — showing "1,247" in a tiny badge
3. Badge only conveyed visually — no screen reader announcement

---

## 15. Tooltip

**Anatomy:**
- Container (small card with arrow/caret pointing to trigger)
- Text content (1-2 lines, plain text)
- Optional: close button (for interactive tooltips)

**Variants:**
- **Plain text** — Simple description, appears on hover/focus
- **Rich** — Contains formatted text, links, or actions
- **Guided** — Part of a product tour (step X of Y, with next/previous)

**States:**
- **Hidden** — Not visible
- **Appearing** — Fade in with slight delay (200-400ms hover delay to prevent flicker)
- **Visible** — Displayed, positioned relative to trigger
- **Disappearing** — Fade out on mouse leave or focus loss

**Platform differences:**
- **iOS** — No standard tooltip; use popovers or custom implementation
- **Android** — Material 3 Plain Tooltip (on long press) and Rich Tooltip (on tap or hover)
- **Web** — Custom implementation, CSS or JS positioning, or native `title` attribute (limited styling)

**Accessibility requirements:**
- `role="tooltip"` on the tooltip element
- `aria-describedby` on the trigger pointing to the tooltip
- Hover and focus both trigger tooltip (not hover-only — not accessible to keyboard/touch)
- For touch devices: long-press or tap to reveal (hover does not exist on touch)
- Rich tooltips with interactive content: `role="dialog"` instead, with focus management
- Do not put essential information in tooltips only (it must be accessible elsewhere)

**Common mistakes:**
1. Tooltip only on hover (touch and keyboard users cannot access)
2. Essential information in tooltip only (should be visible inline for important info)
3. Tooltip obscures the element it describes (poor positioning)

---

## 16. Dropdown / Select

**Anatomy:**
- Trigger button (shows current selection + chevron/arrow icon)
- Label (above trigger or floating)
- Dropdown menu (list of options below trigger)
- Options (text, optional icon, optional description)
- Selected indicator (checkmark on current option)
- Optional: search within dropdown, group headers

**Variants:**
- **Single select** — One option chosen
- **Multi-select** — Checkboxes per option, multiple chosen
- **Searchable** — Filter input at top of dropdown (for long lists)
- **Grouped** — Options organized under group headers
- **Custom rendering** — Options with icons, avatars, or descriptions

**States:**
- **Closed** — Trigger displays current value
- **Open** — Dropdown visible, options listed
- **Option hover** — Background highlight
- **Option selected** — Checkmark + highlight
- **Disabled** — Trigger grayed, not openable
- **Loading** — Spinner in dropdown while options load

**Platform differences:**
- **iOS** — `UIMenu` (contextual menus), Picker (wheel, inline, segmented), action sheets
- **Android** — Material 3 `ExposedDropdownMenu` (text field + menu), no native dropdown
- **Web** — `<select>` (native but limited styling) or custom with `role="listbox"` + `role="option"`

**Accessibility requirements:**
- Trigger: `role="combobox"` or `role="button"` with `aria-haspopup="listbox"` and `aria-expanded`
- Options: `role="option"` within `role="listbox"`
- Selected option: `aria-selected="true"`
- Keyboard: Enter/Space to open, arrow keys to navigate, Enter to select, Escape to close
- Type-ahead: typing a letter jumps to first option starting with that letter
- Group headers: `role="group"` with `aria-labelledby`

**Common mistakes:**
1. Custom dropdown not keyboard accessible (only mouse/touch)
2. Dropdown extends beyond viewport (should flip to top if no room below)
3. Using dropdown for fewer than 5 options (radio buttons are better for 2-4 options)

---

## 17. Accordion

**Anatomy:**
- Container (groups multiple accordion items)
- Item header (clickable trigger: label + expand/collapse icon)
- Item content (panel that shows/hides)
- Expand/collapse icon (chevron, plus/minus, or caret)

**Variants:**
- **Single open** — Only one item open at a time (others close when one opens)
- **Multi open** — Multiple items can be open simultaneously
- **Flush** — No container border, items separated by dividers only
- **Contained** — Each item has its own bordered container

**States per item:**
- **Collapsed** — Header visible, content hidden, icon pointing right/down
- **Expanding** — Content animating open (200-300ms)
- **Expanded** — Content visible, icon rotated
- **Collapsing** — Content animating closed
- **Disabled** — Header visible but not interactive

**Platform differences:**
- **iOS** — `DisclosureGroup` in SwiftUI, custom UIKit implementation
- **Android** — No standard Material 3 component; custom or `ExpandableListView`
- **Web** — `<details>` + `<summary>` (native) or custom with ARIA

**Accessibility requirements:**
- Header: `<button>` with `aria-expanded="true/false"` and `aria-controls="[panel-id]"`
- Content panel: `id` matching `aria-controls`, `role="region"` with `aria-labelledby="[header-id]"`
- Keyboard: Enter/Space to toggle, arrow keys to navigate between headers
- Screen reader: expanding/collapsing announced via `aria-expanded` state change

**Common mistakes:**
1. Content inside collapsed accordion not in DOM (breaks in-page search — use CSS hiding)
2. Nesting accordions inside accordions (deep nesting is confusing)
3. All items collapsed by default with no indication of content within (open the most relevant one)

---

## 18. Carousel

**Anatomy:**
- Container (fixed width, overflow hidden)
- Slides/items (content cards, images, or pages)
- Navigation arrows (previous/next, left/right)
- Pagination indicators (dots or fraction "2/5")
- Optional: auto-play control, swipe support

**Variants:**
- **Hero/banner** — Full-width, one item at a time (marketing)
- **Multi-item** — Shows multiple cards, scrolls one at a time
- **Peek** — Next item partially visible (indicates more content)
- **Full-screen** — Gallery style, one image at a time

**States:**
- **First item** — Previous button hidden or disabled
- **Middle** — Both arrows visible
- **Last item** — Next button hidden or disabled (or loops to first)
- **Auto-playing** — Timer advances slides, pauses on hover/interaction
- **Dragging/swiping** — Follows finger/cursor, snaps on release

**Platform differences:**
- **iOS** — `UICollectionView` with paging, `TabView` in SwiftUI with `.tabViewStyle(.page)`
- **Android** — `ViewPager2`, `RecyclerView` with snap helper, Material 3 Carousel
- **Web** — CSS scroll-snap, custom JS, or library (Swiper, Embla)

**Accessibility requirements:**
- Container: `role="region"` with `aria-label="Carousel"` and `aria-roledescription="carousel"`
- Slides: `role="group"` with `aria-roledescription="slide"` and `aria-label="Slide 2 of 5"`
- Navigation: buttons with `aria-label="Previous slide"` / `aria-label="Next slide"`
- Auto-play: pause button required, respects `prefers-reduced-motion`
- Keyboard: Arrow keys or Tab to navigate slides
- Pagination dots: interactive, `aria-label="Go to slide 3"`

**Common mistakes:**
1. Auto-play with no pause control (WCAG violation, annoying)
2. Content only accessible via carousel (critical content should not be hidden in slides)
3. No keyboard navigation (arrow keys or tab should work)

---

## 19. List Item

**Anatomy:**
- Leading element (avatar, icon, thumbnail, checkbox)
- Primary text (title/name)
- Secondary text (subtitle, description)
- Trailing element (metadata, action button, chevron, toggle)
- Divider (below item, optional)
- Swipe actions (hidden, revealed on swipe)

**Variants:**
- **Single-line** — Title only
- **Two-line** — Title + subtitle
- **Three-line** — Title + subtitle + description (max before using cards)
- **Interactive** — Tappable, navigates to detail
- **Selectable** — Checkbox/radio for selection
- **Swipeable** — Swipe actions (archive, delete, pin)

**States:**
- **Default** — Normal display
- **Pressed** — Background highlight (ripple on Android)
- **Selected** — Checkbox checked or highlight
- **Swiped** — Action buttons revealed behind item
- **Dragging** — Elevated, shadow, for reorder
- **Disabled** — Muted appearance

**Platform differences:**
- **iOS** — `UITableViewCell` / `List` in SwiftUI, swipe actions, leading/trailing accessories
- **Android** — Material 3 List Item, three-line max, leading/trailing elements
- **Web** — `<li>` within `<ul>` or `<ol>`, custom styling

**Accessibility requirements:**
- Semantic: `<li>` within `<ul>` or `<ol>`
- Interactive items: focusable, `role="button"` or link
- Swipe actions: must have accessible alternatives (long-press menu or visible button)
- Checkbox items: `aria-checked` state, group label for the list
- Reorderable: `aria-grabbed`, `aria-dropeffect` (or modern drag-and-drop ARIA)

**Common mistakes:**
1. Tap target too small (entire row should be tappable, not just the text)
2. No separator between items (content runs together)
3. Swipe-only actions with no alternative (not accessible)

---

## 20. Progress Indicator

**Anatomy:**
- Track (background line or circle)
- Fill (progress amount on track)
- Label (percentage, step count, or description)
- Optional: animated indeterminate state

**Variants:**
- **Linear determinate** — Horizontal bar filling left to right (file upload: 67%)
- **Linear indeterminate** — Animated bar moving back and forth (loading, unknown duration)
- **Circular determinate** — Ring filling around (timer, progress)
- **Circular indeterminate** — Spinning ring (loading spinner)
- **Step indicator** — Discrete steps filled (checkout: step 2 of 4)

**States:**
- **Empty** — 0% progress, track only
- **In progress** — Partially filled
- **Complete** — 100% filled, success color (green)
- **Error** — Progress stopped, error indicator
- **Indeterminate** — Unknown duration, animated pattern

**Platform differences:**
- **iOS** — `UIProgressView` (linear), `ProgressView` in SwiftUI (circular and linear)
- **Android** — `LinearProgressIndicator`, `CircularProgressIndicator` in Material 3
- **Web** — `<progress>` element (native) or custom with `role="progressbar"`

**Accessibility requirements:**
- `role="progressbar"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax`
- `aria-label="Uploading file, 67% complete"` or `aria-labelledby`
- Indeterminate: `aria-valuenow` omitted, `aria-label="Loading"`
- Do not rely on visual progress alone — provide text percentage or step count
- Step indicators: `aria-current="step"` on active step

**Common mistakes:**
1. No text label — just a bar with no percentage or context
2. Indeterminate spinner for tasks that should show real progress
3. Progress bar that jumps (non-smooth updates — interpolate between updates)

---

## 21. Stepper

**Anatomy:**
- Decrement button (minus icon or text)
- Value display (current number)
- Increment button (plus icon or text)
- Optional: min/max labels, input field for direct entry

**Variants:**
- **Compact** — Small buttons flanking a number (quantity in cart)
- **Input hybrid** — Buttons + editable number field (type or click)
- **Horizontal** — Buttons on left and right of value
- **Vertical** — Buttons above and below value (less common)

**States:**
- **Default** — Both buttons active
- **At minimum** — Decrement disabled
- **At maximum** — Increment disabled
- **Editing** — Value field focused for direct input
- **Disabled** — Both buttons and value inactive

**Platform differences:**
- **iOS** — `UIStepper` (compact +/- buttons), separate label for value
- **Android** — No standard stepper; custom implementation common
- **Web** — `<input type="number">` has native stepper, or custom with buttons

**Accessibility requirements:**
- `role="spinbutton"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax`
- `aria-label="Quantity"` or associated label
- Keyboard: Up/Down arrows to increment/decrement, direct number entry
- Buttons: `aria-label="Increase quantity"` and `aria-label="Decrease quantity"`
- Value changes announced to screen readers

**Common mistakes:**
1. No direct input option (user has to click 20 times to reach 20)
2. Buttons too small (tiny +/- buttons are hard to tap)
3. No min/max indication (user discovers limits by hitting them)

---

## 22. Date Picker

**Anatomy:**
- Trigger (input field or button showing selected date)
- Calendar grid (month view with day cells)
- Month/year navigation (previous/next arrows, month/year selectors)
- Day cells (numbers in 7-column grid)
- Today indicator
- Selected date indicator
- Optional: time picker, date range selection

**Variants:**
- **Calendar dropdown** — Opens calendar grid below input (web common)
- **Inline calendar** — Always visible calendar embedded in page
- **Date range** — Select start and end date (booking, reporting)
- **Wheels** — Scrolling wheel picker (iOS native)
- **Input only** — Text field with date format mask (MM/DD/YYYY)

**States:**
- **Empty** — Placeholder with format hint
- **Calendar open** — Grid displayed, today highlighted
- **Date selected** — Day cell highlighted, input value updated
- **Date range selecting** — Start selected, hovering shows potential end
- **Disabled dates** — Past dates or unavailable dates grayed/not selectable
- **Invalid input** — Error state for manually typed invalid dates

**Platform differences:**
- **iOS** — `UIDatePicker` (wheels, compact, inline), SwiftUI `DatePicker`
- **Android** — Material 3 `DatePicker`, `DateRangePicker`, modal or docked
- **Web** — `<input type="date">` (native, limited styling) or custom calendar component

**Accessibility requirements:**
- Calendar grid: `role="grid"` with `role="gridcell"` for days
- Day cells: `aria-label="Monday, January 15, 2026"` (full date, not just "15")
- Selected date: `aria-selected="true"`
- Disabled dates: `aria-disabled="true"` with reason if possible
- Keyboard: Arrow keys navigate days, Page Up/Down for months, Enter to select
- Month navigation: labeled buttons ("Previous month", "Next month")
- Input alternative: allow typing dates, not just calendar selection

**Common mistakes:**
1. Calendar-only with no text input option (typing "Jan 15" is faster for known dates)
2. Year navigation requires clicking month arrow 48 times to go back 4 years
3. No "Today" button to quickly return to current date

---

## 23. Slider

**Anatomy:**
- Track (horizontal line)
- Thumb (draggable circle on track)
- Fill (colored portion of track from min to thumb)
- Labels (min and max values at track ends)
- Value label (current value above thumb or nearby)
- Optional: tick marks for discrete values

**Variants:**
- **Continuous** — Any value between min and max
- **Discrete** — Snaps to defined values (tick marks)
- **Range** — Two thumbs for min-max range (price range filter)
- **Vertical** — Vertical track (volume, brightness — less common in UI)

**States:**
- **Default** — Thumb at current value
- **Hover** — Thumb enlarged slightly
- **Dragging** — Thumb enlarged, value label visible
- **Focus** — Focus ring on thumb
- **Disabled** — Track and thumb grayed

**Platform differences:**
- **iOS** — `UISlider`, continuous by default, custom track/thumb appearance
- **Android** — Material 3 `Slider`, continuous and discrete, tick marks for discrete
- **Web** — `<input type="range">`, limited styling, custom for rich sliders

**Accessibility requirements:**
- `role="slider"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax`, `aria-valuetext`
- `aria-label` or associated label ("Price: $50")
- `aria-valuetext` for human-readable value ("$50" instead of "50")
- Keyboard: Arrow keys for fine adjustment, Page Up/Down for larger steps
- Range slider: two separate `role="slider"` elements within a group

**Common mistakes:**
1. No visible current value (user doesn't know what they selected)
2. Thumb too small for touch (minimum 44x44pt touch target area)
3. No keyboard alternative (slider is drag-only)

---

## 24. Rating

**Anatomy:**
- Rating icons (stars, hearts, or custom icons, typically 5)
- Optional: current value text ("4.2 out of 5")
- Optional: total reviews count ("(1,234 reviews)")
- Optional: rating distribution bar chart (5-star breakdown)

**Variants:**
- **Display only** — Shows rating, not interactive
- **Interactive** — User can select rating by tapping/clicking stars
- **Half-star** — Allows 0.5 increments
- **Compact** — Single star icon with number ("4.2" next to star)

**States:**
- **Empty** — No rating given (gray stars)
- **Partial** — Some stars filled (display: half-stars for averages)
- **Full** — All stars filled
- **Hover** — Stars fill up to hovered position (interactive)
- **Selected** — Stars filled to selected position (interactive)
- **Disabled** — Gray, not interactive

**Platform differences:**
- **iOS** — Custom implementation (no standard rating component)
- **Android** — `RatingBar` component, configurable star count
- **Web** — Custom, using radio buttons (`role="radiogroup"`) or custom `role="slider"`

**Accessibility requirements:**
- Interactive rating: `role="radiogroup"` with each star as `role="radio"` and `aria-label="1 star"` etc.
- Or `role="slider"` with `aria-valuenow="4"`, `aria-valuemin="1"`, `aria-valuemax="5"`
- Display rating: text alternative "Rated 4.2 out of 5 stars"
- Review count: include in accessible label "4.2 out of 5, based on 1,234 reviews"
- Interactive: keyboard navigable (arrow keys or number keys)

**Common mistakes:**
1. Stars with no text value (screen readers can't interpret star images)
2. Interactive rating with no confirmation (accidental taps)
3. Half-star precision on interactive rating (hard to tap precisely — use full stars for input)

---

## 25. Empty State

**Anatomy:**
- Illustration or icon (contextual, relevant to the empty area)
- Headline (what would be here if not empty)
- Description (why it's empty and what to do about it)
- Primary CTA (create, add, import, connect)
- Optional: secondary CTA, example content, templates

**Variants:**
- **First-time** — User hasn't created anything yet ("Create your first project")
- **No results** — Search or filter returned nothing ("No results for 'xyz'")
- **Completed** — All items done ("All caught up!" — positive empty state)
- **Error-caused** — Content failed to load ("Couldn't load items. Try again.")
- **Permission** — User doesn't have access ("Request access to view this content")

**States:**
- **First-time** — Encouraging tone, education, quick start
- **Cleared** — Celebratory or neutral ("No unread messages")
- **Error** — Concerned tone with retry option
- **Loading** — Show skeleton before determining if empty

**Platform differences:**
- **iOS** — Custom view within collection view or table view, centered content
- **Android** — Custom layout, often within `RecyclerView.AdapterDataObserver`
- **Web** — Custom component, replaces content area, maintains page layout

**Accessibility requirements:**
- Heading at appropriate level in page hierarchy
- CTA button properly labeled
- Illustration: decorative `alt=""` unless it conveys unique information
- Must be discoverable by screen reader (not hidden or overflow-hidden)

**Common mistakes:**
1. No empty state at all (blank white space, user thinks it's broken)
2. Same generic empty state everywhere ("Nothing here") instead of contextual messaging
3. No CTA — user sees it's empty but doesn't know how to create content

---

## 26. Skeleton Loader

**Anatomy:**
- Container (matches the shape and layout of the loading content)
- Placeholder shapes (rectangles for text, circles for avatars, rounded rectangles for images)
- Shimmer animation (gradient wave moving left to right, 1.5-2s cycle)
- Background (subtle gray, #E0E0E0 or system equivalent)

**Variants:**
- **Text skeleton** — Rectangle blocks mimicking lines of text (varying widths)
- **Card skeleton** — Full card shape with image placeholder, text blocks, action area
- **List skeleton** — Repeated list item shapes (avatar + two text lines per item)
- **Table skeleton** — Grid of rectangles matching table cells
- **Profile skeleton** — Large circle (avatar) + text blocks (name, bio)

**States:**
- **Loading** — Shimmer animation active, placeholder shapes visible
- **Loaded** — Transition to real content (fade or instant replace)
- **Error** — Replace skeleton with error state (retry button)
- **Partial** — Some sections loaded (replace per section), others still skeleton

**Platform differences:**
- **iOS** — Custom implementation with gradient animation, `redacted(reason: .placeholder)` in SwiftUI
- **Android** — Shimmer library (Facebook), custom drawable animation
- **Web** — CSS gradient animation (`@keyframes shimmer`), `linear-gradient` background

**Accessibility requirements:**
- `aria-busy="true"` on loading container
- `aria-label="Loading content"` on skeleton region
- When loaded: `aria-busy="false"` and announce content with `aria-live`
- Shimmer animation: should respect `prefers-reduced-motion` (use pulse instead of shimmer)
- Screen readers should announce "Loading" once, not repeatedly

**Common mistakes:**
1. Skeleton doesn't match actual content layout (causes layout shift when content loads)
2. Shimmer animation too fast or aggressive (distracting, motion sensitivity)
3. Showing skeleton indefinitely without timeout to error state (30-60 second max, then show error)

---

## Element Pattern Quick Reference

| Element | Primary ARIA Role | Key Keyboard Pattern | Critical Accessibility |
|---------|-------------------|---------------------|----------------------|
| Button | `button` | Enter/Space to activate | `aria-label` for icon-only |
| Card | `article` or link | Enter to activate (if interactive) | Nested interactive conflict |
| Modal | `dialog` | Escape to close, focus trap | Focus return to trigger |
| Bottom Sheet | `dialog` | Escape to close | Close button required |
| Banner | `alert` / `status` | Dismiss via button | Don't auto-dismiss errors |
| Toast | `status` | Action button accessible | Timed — long enough to read |
| Tab Bar | `tablist` + `tab` | Arrow keys between tabs | `aria-selected` state |
| Nav Bar | `navigation` | Skip nav link | Back button `aria-label` |
| Search Bar | `searchbox` | Autocomplete with arrows | `aria-live` for results count |
| Input Field | native `<input>` | Standard form controls | `aria-describedby` for errors |
| Toggle | `switch` | Space to toggle | On/Off announced |
| Chip | varies by type | Enter/Space, Delete to remove | Remove button label |
| Avatar | `img` | N/A (decorative) | Alt text or `aria-label` |
| Badge | N/A (decorative) | N/A | Count in parent label |
| Tooltip | `tooltip` | Focus + hover trigger | Touch device alternative |
| Dropdown | `listbox` | Arrows, Enter, Escape | Type-ahead support |
| Accordion | `button` + `region` | Enter/Space to toggle | `aria-expanded` state |
| Carousel | `region` | Arrow keys for slides | Pause for auto-play |
| List Item | `listitem` | Enter for interactive | Swipe action alternatives |
| Progress | `progressbar` | N/A | `aria-valuenow` + text |
| Stepper | `spinbutton` | Up/Down arrows | Direct input option |
| Date Picker | `grid` | Arrows, Enter, Page Up/Down | Full date in `aria-label` |
| Slider | `slider` | Arrow keys | `aria-valuetext` |
| Rating | `radiogroup` / `slider` | Arrow keys | Text value required |
| Empty State | N/A (content) | CTA focusable | Contextual messaging |
| Skeleton | `aria-busy` | N/A | Respect reduced motion |
