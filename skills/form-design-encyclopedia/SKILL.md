---
name: form-design-encyclopedia
description: "Complete form design system covering every input type, layout pattern, validation strategy, multi-step flow, and accessibility requirement. 200+ form patterns with production React/CSS code, mobile optimization, and conversion best practices. Use when the user mentions: form design, input field, form layout, form validation, multi-step form, form wizard, login form, signup form, checkout form, contact form, search form, filter form, settings form, form accessibility, form error, form submission, form UX, form pattern."
---

# Form Design Encyclopedia — Every Form Pattern

## 1. Form Design Philosophy

### The Fundamental Truth
Every form field is a question. Every question is friction. The best form is the one with the fewest fields that still accomplishes the goal. Forms are conversations between system and human — design them as such.

### Core Principles
1. **Reduce friction** — every field is a cost; only ask what you need right now
2. **Guide completion** — labels, placeholders, helper text, and validation work together as a system
3. **Prevent errors** — constrain input, validate inline, provide formatting guidance before the user types
4. **Recover gracefully** — explain what went wrong and how to fix it in human language
5. **Respect time** — autosave progress, remember preferences, never make users re-enter data
6. **Build trust** — explain why you need sensitive data, show security indicators, link to privacy policy
7. **Progressive disclosure** — show only what is relevant now; reveal complexity as needed

### Research Foundation
- **Matteo Penzo (UXMatters, 2006)**: Eye-tracking study proved top-aligned labels have fastest completion times. Users fixate once (label + field together) vs. left-aligned requiring two fixations (label, then field). Top-aligned labels reduce completion time by ~50% compared to left-aligned.
- **Luke Wroblewski (Web Form Design, 2008)**: Established the canonical form design principles. Key findings: (a) single-column forms outperform multi-column, (b) optional fields should be marked rather than required fields, (c) inline validation reduces errors by 22%, (d) removing even one field increases conversion measurably.
- **Baymard Institute (2012-2025)**: Checkout usability research across 100+ e-commerce sites. Average cart abandonment rate: 70%. Form-related causes: too long (18%), required account creation (24%), confusing checkout (17%).
- **Google UX Research (2016)**: Autocomplete reduces form completion time by 30% and errors by 15%.
- **NNG (2019-2024)**: Placeholder text as labels fails accessibility and usability. Floating labels are acceptable but top-aligned labels remain the gold standard.

### The Form Equation
```
Completion Rate = Motivation / (Friction x Complexity)
```
- Motivation: value proposition, progress indicators, social proof
- Friction: number of fields, cognitive load per field, error recovery cost
- Complexity: branching logic, unfamiliar concepts, format requirements

---

## 2. Label Placement Research — Complete Guide

### Top-Aligned Labels (Recommended Default)
- **Completion time**: Fastest (Penzo eye-tracking study)
- **Fixation pattern**: Single fixation — label and field read together
- **Best for**: Most forms, mobile, short-to-medium length
- **Drawback**: Increased vertical space
- **CSS**: `flex-direction: column; gap: 4px;`

### Left-Aligned Labels
- **Completion time**: Slowest — saccade between label and field
- **Fixation pattern**: Two fixations per field
- **Best for**: Dense data-entry forms used by trained operators (ERP, medical records)
- **Drawback**: Requires consistent label width; long labels wrap awkwardly
- **CSS**: `display: grid; grid-template-columns: 160px 1fr; align-items: baseline;`

### Right-Aligned Labels
- **Completion time**: Moderate — closer proximity than left-aligned
- **Best for**: Settings panels, admin forms
- **Drawback**: Ragged left edge makes scanning harder
- **CSS**: `text-align: right;` on label column

### Floating Labels (Material Design Pattern)
- **Completion time**: Moderate
- **How it works**: Placeholder animates up to become label on focus/fill
- **Best for**: Space-constrained designs, modern aesthetic
- **Drawback**: Animation can distract; limited label length; placeholder disappears
- **Accessibility**: Must use `<label>` element, not just visual animation

### Placeholder-Only Labels — NEVER USE
- Disappears on focus — users lose context
- Fails WCAG 1.3.1 (Info and Relationships)
- Low contrast in most implementations
- Screen readers may not announce them reliably
- Users with cognitive disabilities cannot reference the label while typing

---

## 3. Complete Input Type Catalog (55 Types)

### 3.1 Text Input (`<input type="text">`)
- **When to use**: Single-line free text — names, titles, generic strings
- **Anatomy**: Label, input container, optional helper text, optional character counter
- **States**: Default (border: neutral-300), Focus (border: primary-500 + ring), Filled (border: neutral-400), Error (border: error-500 + icon + message), Disabled (opacity: 0.5, cursor: not-allowed), Read-only (no border, bg: neutral-50)
- **Sizing**: Height 40px (default), 36px (compact), 48px (large/touch)
- **Platform notes**: iOS adds autocorrect by default — disable with `autoCorrect="off"` for names, codes

### 3.2 Email Input (`<input type="email">`)
- **When to use**: Email address collection
- **Anatomy**: Label, input with email icon (optional), domain suggestion dropdown
- **States**: Same as text + valid state with checkmark
- **Validation**: Browser native + regex `/^[^\s@]+@[^\s@]+\.[^\s@]+$/` + MX record check for critical flows
- **Smart features**: Suggest common domain corrections ("gmail.con" -> "Did you mean gmail.com?")
- **Mobile**: Triggers email keyboard with `@` and `.` keys
- **Autocomplete**: `autocomplete="email"`

### 3.3 Password Input (`<input type="password">`)
- **When to use**: Password entry (login, registration, change password)
- **Anatomy**: Label, masked input, show/hide toggle button, strength meter (registration), requirements checklist
- **States**: Default, Focus, Filled (dots), Error, Disabled + Strength levels (weak/fair/strong/excellent)
- **Show/hide toggle**: Eye icon; `aria-label="Show password"` / `aria-label="Hide password"`
- **Strength meter**: Check length, uppercase, lowercase, numbers, special chars, common passwords list
- **Paste**: ALWAYS allow paste — NCSC and security experts confirm blocking paste reduces security
- **Mobile**: Do not use `autocomplete="off"` — allow password managers

### 3.4 Number Input (`<input type="number">`)
- **When to use**: Numeric values with increment/decrement (quantity, age)
- **Anatomy**: Label, input, stepper buttons (optional), unit suffix
- **Caution**: Avoid for phone numbers, zip codes, credit cards, SSN — use `type="text"` with `inputmode="numeric"` instead
- **Why**: Number inputs have scroll-to-change behavior (accidental changes), strip leading zeros, and have inconsistent formatting across browsers
- **Attributes**: `min`, `max`, `step`
- **Mobile**: `inputmode="numeric"` or `inputmode="decimal"`

### 3.5 Phone Input (`<input type="tel">`)
- **When to use**: Phone number collection
- **Anatomy**: Country code selector (flag + dial code), input field, formatting mask
- **Formatting**: Auto-format as user types: `(555) 123-4567` for US
- **International**: Use libphonenumber for validation; store in E.164 format (+15551234567)
- **Mobile**: `inputmode="tel"` triggers numeric keypad with `+`, `*`, `#`
- **Autocomplete**: `autocomplete="tel"`

### 3.6 URL Input (`<input type="url">`)
- **When to use**: Website URL collection
- **Anatomy**: Label, optional protocol prefix (https://), input
- **Smart features**: Auto-prepend `https://` if user types `example.com`
- **Validation**: Check for valid URL format; optionally verify URL resolves
- **Autocomplete**: `autocomplete="url"`

### 3.7 Search Input (`<input type="search">`)
- **When to use**: Search functionality
- **Anatomy**: Search icon (left), input, clear button (x, appears when filled), optional voice input button
- **Behavior**: Native clear button in most browsers; `Escape` key clears
- **Patterns**: Instant search (debounced 300ms), search-on-submit, hybrid
- **Suggestions**: Show recent searches, popular queries, autocomplete results
- **Mobile**: Triggers search keyboard with "Search" return key

### 3.8 Date Input
- **When to use**: Single date selection
- **Options**: Native `<input type="date">` vs. custom date picker
- **Native pros**: Accessible, keyboard-navigable, mobile-optimized
- **Native cons**: Inconsistent styling across browsers, limited customization
- **Custom picker anatomy**: Calendar grid, month/year navigation, today button, clear button
- **Format**: Display in locale format; store as ISO 8601 (YYYY-MM-DD)
- **Accessibility**: Arrow key navigation, `aria-label` on each day cell
- **Platform**: iOS uses scroll wheels; Android uses Material date picker; desktop uses dropdown calendar

### 3.9 Date Range Input
- **When to use**: Start/end date selection (booking, reporting)
- **Anatomy**: Two date fields or single field with range picker, calendar with range highlighting
- **Interaction**: Click start date, click end date; hover shows preview range
- **Validation**: End date must be after start date; min/max constraints
- **Presets**: "Last 7 days", "This month", "Last quarter", "Custom"

### 3.10 Time Input (`<input type="time">`)
- **When to use**: Time selection
- **Anatomy**: Hour, minute (optional seconds), AM/PM toggle
- **Format**: 12-hour (US) vs. 24-hour (most of world) — detect from locale
- **Step**: Default 60 seconds; use `step="900"` for 15-minute intervals
- **Mobile**: Native time picker wheels

### 3.11 DateTime Input
- **When to use**: Combined date and time (event scheduling, appointments)
- **Pattern**: Separate date and time fields (preferred) or combined picker
- **Timezone**: Always show timezone; allow selection if relevant
- **Storage**: ISO 8601 with timezone: `2025-03-15T14:30:00-07:00`

### 3.12 Textarea (`<textarea>`)
- **When to use**: Multi-line text (comments, descriptions, messages, bio)
- **Anatomy**: Label, text area, character counter, optional formatting toolbar
- **Sizing**: Min-height 80px; auto-expand with content (recommended); or fixed with scroll
- **Character counter**: Show `{current}/{max}` — change color at 90%+ usage
- **Resize**: `resize: vertical` (recommended), `resize: none` for fixed, `resize: both` for flexible
- **Attributes**: `rows` for initial height; `maxlength` for limit

### 3.13 Select / Dropdown (`<select>`)
- **When to use**: Single selection from 5-15 predefined options
- **When NOT to use**: <5 options (use radio buttons), >15 options (use searchable combobox)
- **Anatomy**: Label, trigger button with current value, dropdown menu, optional placeholder
- **States**: Default, Open, Selected, Disabled, Error
- **Placeholder**: "Select..." or "Choose..." — NOT a valid selection
- **Accessibility**: Arrow keys navigate; Enter selects; Escape closes; type-ahead search
- **Mobile**: Uses native `<select>` picker (scroll wheel) — much better UX than custom

### 3.14 Combobox / Searchable Select
- **When to use**: Selection from large lists (countries, cities, products) — 15+ options
- **Anatomy**: Text input + dropdown list, filtered by typing, optional "Create new" action
- **Behavior**: Type to filter; arrow keys to navigate; Enter to select
- **ARIA**: `role="combobox"`, `aria-expanded`, `aria-controls`, `aria-activedescendant`
- **Libraries**: Downshift, Radix Select, Headless UI Combobox

### 3.15 Multi-Select
- **When to use**: Multiple selections from a list (tags, categories, permissions)
- **Patterns**: Checkbox list (< 10 items), tag input with suggestions (10-50), searchable multi-select (50+)
- **Anatomy**: Input area with selected items as chips/tags, dropdown with checkboxes, "Select all" / "Clear all"
- **Mobile**: Use full-screen modal for multi-select on mobile

### 3.16 Radio Buttons (`<input type="radio">`)
- **When to use**: Single selection from 2-5 mutually exclusive options
- **Anatomy**: Circle indicator, label, optional description per option
- **Layout**: Vertical stack (default), horizontal row (2-3 short options only)
- **Rules**: Always have one pre-selected (or explicit "None" option); never use for on/off (use toggle)
- **Card variant**: Radio cards with icon + title + description for rich options
- **ARIA**: Wrap in `<fieldset>` with `<legend>`

### 3.17 Checkbox (`<input type="checkbox">`)
- **When to use**: Binary on/off, or multiple selections from a set
- **Anatomy**: Square indicator (empty, checked, indeterminate), label
- **Indeterminate state**: For "Select all" when some children are checked
- **Single checkbox**: Consent, terms agreement, opt-in — label is the question
- **Group**: Wrap in `<fieldset>` with `<legend>` describing the group
- **Spacing**: Minimum 8px between checkboxes; 44px touch target on mobile

### 3.18 Toggle / Switch
- **When to use**: Immediate on/off effect (settings, preferences, feature flags)
- **Key difference from checkbox**: Toggle applies immediately (no submit needed); checkbox is part of a form
- **Anatomy**: Track, thumb, on/off labels (optional), status text
- **States**: Off (default), On, Disabled-off, Disabled-on, Loading (for async toggles)
- **Accessibility**: `role="switch"`, `aria-checked="true|false"`
- **Label**: Always describe the ON state: "Enable notifications" not "Notifications toggle"

### 3.19 Segmented Control
- **When to use**: Switch between 2-5 views or modes (not form data)
- **Anatomy**: Container with equal-width segments, selected indicator
- **Difference from radio**: Segmented controls switch views/modes; radios select form values
- **Platform**: iOS uses segmented control extensively; Material uses tabs
- **Accessibility**: `role="radiogroup"` with `role="radio"` children

### 3.20 Slider / Range (`<input type="range">`)
- **When to use**: Selecting a value within a continuous range where precision is not critical
- **Anatomy**: Track, thumb, optional min/max labels, optional value tooltip, optional input field for precise entry
- **Variants**: Single thumb, dual thumb (range), stepped, with marks
- **When NOT to use**: When exact number entry is needed (use number input instead)
- **Accessibility**: `aria-valuemin`, `aria-valuemax`, `aria-valuenow`, `aria-valuetext` (for human-readable value)
- **Mobile**: Large thumb (minimum 44px touch target); consider full-width track

### 3.21 Color Picker
- **When to use**: Color selection (themes, branding, design tools)
- **Patterns**: Preset swatches (simple), spectrum picker + hex input (advanced), eyedropper tool
- **Anatomy**: Color well trigger, picker popup (spectrum, hue strip, alpha), format inputs (hex, rgb, hsl, oklch)
- **States**: Default, Open, Selected with preview
- **Accessibility**: Provide text input alternative; announce selected color

### 3.22 File Upload
- **When to use**: Document, image, or media upload
- **Patterns**: Click to browse, drag-and-drop zone, paste from clipboard
- **Anatomy**: Drop zone with icon + instructions, file type restrictions, size limit, progress bar, preview, remove button
- **States**: Empty, Drag-over (highlighted), Uploading (progress), Complete (with preview), Error
- **Validation**: Check file type (`accept` attribute), file size, dimensions (images), virus scan (server)
- **Multiple files**: Show upload queue with individual progress and remove buttons
- **Mobile**: Trigger native file picker, camera, or photo library

### 3.23 Image Upload with Preview
- **When to use**: Profile photos, product images, cover photos
- **Anatomy**: Preview area (circular for avatars, rectangular for covers), upload button, crop tool, remove button
- **Crop**: Offer aspect ratio lock; provide zoom and pan controls
- **Optimization**: Client-side resize before upload to reduce bandwidth

### 3.24 Signature Pad
- **When to use**: Electronic signatures (contracts, consent forms, delivery confirmation)
- **Anatomy**: Canvas area, clear button, type-signature alternative, date stamp
- **Technology**: HTML5 Canvas or SVG path capture
- **Output**: SVG (preferred for quality) or PNG with transparent background
- **Legal**: Display legal text: "By signing, you agree to..."
- **Accessibility**: Provide "Type your name" alternative for keyboard-only users

### 3.25 OTP / Verification Code Input
- **When to use**: One-time password, 2FA codes, phone verification
- **Anatomy**: 4-6 individual digit boxes, auto-advance on entry, paste support
- **Behavior**: Auto-focus first box; advance on digit entry; backspace returns to previous; paste fills all boxes
- **Attributes**: `inputmode="numeric"`, `autocomplete="one-time-code"` (triggers SMS autofill on mobile)
- **Timer**: Show resend countdown: "Resend code in 0:45"
- **Security**: Mask after brief display; auto-clear after timeout

### 3.26 Credit Card Input
- **When to use**: Payment card details
- **Fields**: Card number (with brand detection), expiry (MM/YY), CVC, cardholder name, ZIP (optional)
- **Card number**: Format with spaces: `4242 4242 4242 4242`; detect brand from first digits (Visa: 4, MC: 5, Amex: 34/37)
- **Expiry**: Auto-insert `/` after MM; reject past dates
- **CVC**: 3 digits (4 for Amex); show card flip animation indicating CVC location
- **Autocomplete**: `autocomplete="cc-number"`, `cc-exp`, `cc-csc`, `cc-name`
- **Security**: Display card brand icon; show lock icon; PCI compliance note
- **Libraries**: Stripe Elements, Braintree Hosted Fields (handle PCI compliance)

### 3.27 Address Input
- **When to use**: Shipping/billing address
- **Pattern 1**: Single-field autocomplete (Google Places API) that expands to individual fields
- **Pattern 2**: Traditional multi-field (street, apt, city, state, zip, country)
- **Autocomplete attributes**: `address-line1`, `address-line2`, `address-level2` (city), `address-level1` (state), `postal-code`, `country`
- **International**: Country selection changes field structure (e.g., Japan: prefecture before city; UK: no state)
- **Validation**: Use postal code to auto-fill city/state; validate with address verification API

### 3.28 Rich Text Editor
- **When to use**: Formatted content (blog posts, emails, descriptions with styling)
- **Toolbar**: Bold, italic, underline, headings, lists, links, images, code blocks
- **Variants**: Minimal (bold, italic, link), Standard (+ headings, lists, images), Full (+ tables, embeds, code)
- **Libraries**: Tiptap, Lexical, Slate, Quill, ProseMirror
- **Accessibility**: All toolbar actions must be keyboard-accessible; announce formatting changes
- **Mobile**: Collapse toolbar behind "+" button; use bottom sheet for formatting options

### 3.29 Code Input / Code Editor
- **When to use**: Code snippets, API keys, configuration (developer tools)
- **Features**: Syntax highlighting, line numbers, auto-indent, bracket matching
- **Libraries**: CodeMirror, Monaco Editor
- **Monospace font**: Required — use `font-family: 'JetBrains Mono', 'Fira Code', monospace`

### 3.30 Rating Input
- **When to use**: Star ratings, satisfaction scores, NPS
- **Patterns**: Star rating (1-5), numeric scale (1-10), emoji scale, thumb up/down
- **Anatomy**: Icons (stars/emojis), optional labels per level, hover preview
- **Interaction**: Click to rate; hover shows preview; click same star to clear (or provide clear button)
- **Accessibility**: `role="radiogroup"` with `role="radio"` per star; arrow key navigation
- **Half-stars**: Only in display, not input — too fiddly for touch

### 3.31 Emoji Picker
- **When to use**: Reactions, status, message composition
- **Anatomy**: Category tabs, search, recently used, emoji grid, skin tone selector
- **Performance**: Virtualize the grid (300+ emojis); lazy-load categories
- **Accessibility**: Search is primary a11y path; grid uses `role="listbox"`

### 3.32 Tag / Chip Input
- **When to use**: Multiple freeform or suggested values (skills, interests, labels)
- **Anatomy**: Input field, tag chips (with remove X), suggestion dropdown
- **Behavior**: Type + Enter/comma to add; Backspace to remove last; click X to remove specific
- **Validation**: Max tags, min/max length per tag, duplicate prevention, allowlist/blocklist
- **Autocomplete**: Show suggestions as user types; allow freeform or restrict to suggestions only

### 3.33 Mention Input (@-mention)
- **When to use**: Referencing users, channels, or entities in text
- **Trigger**: `@` character opens suggestion popup
- **Anatomy**: Text input, popup with avatar + name + handle, highlighted mention chip in text
- **Behavior**: Continue typing to filter; arrow keys + Enter to select; Escape to dismiss

### 3.34 Command Input (Command Palette)
- **When to use**: Power-user shortcut, action search
- **Trigger**: `Cmd+K` / `Ctrl+K`
- **Anatomy**: Search input, categorized action list, keyboard shortcut hints, recent actions
- **Libraries**: cmdk (React), Ninja Keys

### 3.35 Currency Input
- **When to use**: Money amounts (pricing, payments, budgets)
- **Anatomy**: Currency symbol prefix ($), formatted number, optional currency code selector
- **Formatting**: Locale-aware thousands separator and decimal; format on blur
- **Attributes**: `inputmode="decimal"` for mobile keyboard with decimal point
- **Validation**: Must be positive (usually), max decimal places (2 for USD), min/max amount

### 3.36 Percentage Input
- **When to use**: Rates, discounts, allocations
- **Anatomy**: Number input with `%` suffix
- **Validation**: 0-100 range (or custom); decimal precision
- **Alternative**: Slider for approximate values

### 3.37 Quantity Stepper
- **When to use**: Small numeric adjustments (e-commerce cart, number of guests)
- **Anatomy**: Minus button, value display, plus button
- **States**: Min reached (minus disabled), Max reached (plus disabled)
- **Touch targets**: Each button minimum 44x44px

### 3.38 Pin / Pattern Input
- **When to use**: Mobile unlock, simple auth
- **Pin**: 4-6 digit circles that fill on entry
- **Pattern**: 3x3 dot grid with gesture connection

### 3.39 Captcha / Bot Detection
- **When to use**: Form submission protection
- **Options**: reCAPTCHA v3 (invisible, score-based — preferred), hCaptcha, Turnstile (Cloudflare)
- **UX rule**: Invisible captcha is always preferred; visual challenges are hostile UX
- **Accessibility**: Always provide audio alternative for visual captcha

### 3.40 Autocomplete / Typeahead
- **When to use**: Any field with predictable inputs (cities, companies, products)
- **Anatomy**: Text input, suggestion dropdown with highlighted match, optional categories
- **Performance**: Debounce 200-300ms; cache results; show loading indicator
- **Keyboard**: Arrow keys navigate; Enter selects; Escape dismisses
- **ARIA**: `role="combobox"`, `aria-autocomplete="list"`, live region for result count

### 3.41 Geolocation Input
- **When to use**: Location-based forms (store finder, delivery, check-in)
- **Pattern**: "Use my location" button + manual address fallback
- **Anatomy**: Location button with GPS icon, map preview, address confirmation
- **Permission**: Request geolocation only on user action, never on page load

### 3.42 Avatar / Profile Picture
- **When to use**: User profile setup
- **Anatomy**: Circular preview, camera icon overlay, upload/change button, initials fallback
- **Flow**: Click > Choose file/camera > Crop circle > Save

### 3.43 Boolean Yes/No
- **When to use**: Simple yes/no question in a form
- **Options**: Radio buttons (preferred for clarity), toggle (only if immediate effect), segmented control
- **Never**: A single checkbox for "Yes" — unclear what unchecked means

### 3.44 Likert Scale
- **When to use**: Surveys, feedback forms
- **Anatomy**: Statement text, 5 or 7-point scale, labeled endpoints (Strongly Disagree — Strongly Agree)
- **Layout**: Horizontal on desktop, vertical stack on mobile
- **Accessibility**: `role="radiogroup"` with each point as `role="radio"`

### 3.45 Matrix / Grid Question
- **When to use**: Multiple items rated on same scale (survey)
- **Anatomy**: Row headers (items), column headers (scale points), radio/checkbox intersections
- **Mobile**: Transform into stacked individual Likert scales — grids are unusable on small screens

### 3.46 Conditional / Branching Field
- **When to use**: Field visibility depends on previous answer
- **Pattern**: Show/hide with smooth animation; maintain focus management
- **Animation**: `max-height` transition or Framer Motion `AnimatePresence`
- **ARIA**: Use `aria-expanded` on trigger; manage focus to newly revealed fields

### 3.47 Inline Editable Field
- **When to use**: Profile pages, settings, data tables with editable cells
- **Pattern**: Display value as text > Click to edit > Input appears > Save/Cancel
- **Anatomy**: Text display, edit icon (pencil), input field, save (check) and cancel (x) buttons
- **Keyboard**: Enter to save, Escape to cancel

### 3.48 Masked Input
- **When to use**: Formatted data entry (SSN, phone, credit card, date)
- **Pattern**: Show mask template `___-__-____`; replace underscores as user types
- **Libraries**: react-input-mask, imask
- **Caution**: Can be confusing — always show the expected format as helper text

### 3.49 Dynamic Repeatable Fields
- **When to use**: Variable-count items (work experience, education, line items)
- **Anatomy**: Field group, "Add another" button, remove button per item, drag-to-reorder
- **Validation**: Validate each group independently; show group-level and field-level errors
- **Animation**: Animate add/remove for spatial continuity

### 3.50 Read-Only / Display Field
- **When to use**: Showing computed or locked values in form context
- **Styling**: No border or subtle border, background: neutral-50, no cursor
- **Accessibility**: Use `aria-readonly="true"` or render as plain text (not input)

### 3.51 Hidden Fields
- **When to use**: Tracking data, CSRF tokens, referral codes, UTM parameters
- **Implementation**: `<input type="hidden">` or React state — never rendered visually
- **Security**: Never put sensitive logic in hidden fields; validate server-side

### 3.52 Drag-and-Drop Ordering
- **When to use**: Prioritization, custom sort order
- **Anatomy**: Drag handle (grip dots), item content, drop zone indicator
- **Libraries**: @dnd-kit/core, react-beautiful-dnd
- **Accessibility**: Provide up/down buttons as keyboard alternative

### 3.53 Time Zone Selector
- **When to use**: Scheduling across time zones
- **Pattern**: Searchable select grouped by UTC offset; show current time in selected zone
- **Data**: Use IANA timezone database (America/Los_Angeles, not "PST")
- **Smart default**: Auto-detect from `Intl.DateTimeFormat().resolvedOptions().timeZone`

### 3.54 Language / Locale Selector
- **When to use**: i18n, localization preferences
- **Pattern**: Dropdown with flag + native language name ("Deutsch" not "German")
- **Caution**: Flags represent countries, not languages — Spanish is spoken in 20+ countries

### 3.55 Terms / Consent Checkbox
- **When to use**: Legal agreement before submission
- **Pattern**: Checkbox with linked text: "I agree to the [Terms of Service] and [Privacy Policy]"
- **Rules**: Must be unchecked by default (GDPR); link text must be distinguishable; separate checkboxes for separate consents
- **Validation**: Required with clear error: "You must agree to the terms to continue"

---

## 4. Universal Input States — Complete Reference

Every input in your design system must support these states:

| State | Visual Treatment | Trigger |
|-------|-----------------|---------|
| Default | Border: neutral-300, bg: white | No interaction |
| Hover | Border: neutral-400 | Mouse over |
| Focus | Border: primary-500, ring: primary-200 (2px) | Click or Tab |
| Filled | Border: neutral-400, value displayed | Has value, not focused |
| Error | Border: error-500, icon: error, message below | Validation failure |
| Warning | Border: warning-500, icon: warning, message below | Non-blocking issue |
| Success | Border: success-500, icon: check | Valid after error correction |
| Disabled | Opacity: 0.5, cursor: not-allowed | Field is inactive |
| Read-only | No border or dashed, bg: neutral-50 | Value cannot change |
| Loading | Spinner in field, input disabled | Async validation/data fetch |

### State Priority (highest wins)
Disabled > Error > Warning > Success > Focus > Hover > Filled > Default

---

## 5. Validation Strategy Encyclopedia

### 5.1 Validation Timing Patterns

**On Blur (Recommended Default)**
- Validate when user leaves the field
- Best balance of helpfulness and non-intrusiveness
- Shows error after user has finished typing
- Clear error on change (optimistic recovery)

**On Submit**
- Validate all fields when form is submitted
- Use summary at top + inline errors per field
- Scroll to first error and focus it
- Best for: short forms, forms with interdependent fields

**Real-Time / On Change (Debounced)**
- Validate as user types, with 300-500ms debounce
- Best for: password strength, username availability, search
- Never show errors for incomplete input — wait for minimum viable input
- Show positive feedback (green check) when valid

**On Focus (NEVER for errors)**
- Never show errors when user focuses a field — they haven't typed yet
- Acceptable: Show helper text, format hints on focus

**Hybrid (Best Practice)**
```
First interaction: Validate on blur
After first error: Validate on change (instant feedback as user fixes)
Submit: Validate all + scroll to first error
```

### 5.2 Validation Scope

**Field-Level Validation**
- Required, min/max length, pattern/format, custom rules
- Runs on individual fields independently
- Shows error directly below the field

**Form-Level Validation**
- Cross-field dependencies (password match, date range logic, either/or)
- Runs on submit or when related fields change
- Shows at top of form or between related fields

**Group-Level Validation**
- At least one in group required (phone OR email)
- Shows at group level, not individual field

### 5.3 Inline Validation Patterns

**Optimistic Validation**
- Assume valid until proven otherwise
- Clear errors as soon as user starts fixing
- Show success state briefly, then return to neutral

**Pessimistic Validation**
- Check everything on every change
- Use only for security-critical fields (password, payment)

**Debounced Async Validation**
- For server-side checks: username availability, email uniqueness, promo codes
- Show loading spinner in field during check
- Debounce 500ms to avoid excessive API calls
```jsx
const [isChecking, setIsChecking] = useState(false);
useEffect(() => {
  const timer = setTimeout(async () => {
    if (username.length >= 3) {
      setIsChecking(true);
      const available = await checkUsername(username);
      setIsChecking(false);
      setError(available ? null : 'Username is taken');
    }
  }, 500);
  return () => clearTimeout(timer);
}, [username]);
```

### 5.4 Error Prevention Strategies
- Input masks for formatted data (phone, date, credit card)
- Character counters with limit enforcement
- Dropdowns/selects instead of free text where possible
- Smart defaults (country from IP, date from context)
- Autocomplete suggestions
- Disabling impossible options (past dates for future bookings)
- Real-time formatting (add spaces in card numbers as user types)

---

## 6. Error Message Formula and Patterns

### The Formula
```
[What is wrong] + [How to fix it]
```
Never just say what is wrong. Always tell the user how to fix it.

### Error Message Principles
1. **Be specific** — "Email must include @" not "Invalid email"
2. **Be human** — Write like a helpful person, not a robot
3. **Be humble** — "We couldn't find that address" not "You entered an invalid address"
4. **Be immediate** — Show as close to the error as possible
5. **Use red** — Error color (not just icon) for instant recognition
6. **Don't blame** — "Please enter your email" not "You forgot your email"

### Complete Error Message Catalog

**Required Fields**
- "Please enter your [field name]" (NOT "This field is required")
- "Email address is required to send you a confirmation"

**Email**
- "Please include an '@' in your email address"
- "Please enter a valid email address (e.g., name@example.com)"
- "Did you mean [suggestion]@gmail.com?" (typo correction)
- "This email is already registered. [Log in instead?]"

**Password**
- "Password must be at least 8 characters"
- "Add a number or special character to strengthen your password"
- "Passwords don't match — please re-enter"
- "Incorrect password. [Forgot password?]"

**Phone**
- "Please enter a valid 10-digit phone number"
- "Please include your area code"

**Name**
- "Please enter your first name"
- "Name can only contain letters, spaces, hyphens, and apostrophes"

**Number / Amount**
- "Please enter a number between [min] and [max]"
- "Amount must be at least $1.00"
- "Maximum quantity is 99"

**Date**
- "Please select a date after today"
- "End date must be after start date"
- "Please enter a valid date (MM/DD/YYYY)"

**URL**
- "Please enter a valid URL starting with https://"

**File Upload**
- "File must be smaller than 5MB (yours is 12MB)"
- "Please upload a PNG, JPG, or PDF file"
- "Upload failed — please try again"

**Credit Card**
- "Please enter a valid card number"
- "Your card has expired. Please use a different card."
- "Your card was declined. Please try a different payment method."

**Username**
- "Username is already taken. Try: [suggestions]"
- "Username must be 3-20 characters, letters and numbers only"

**Generic Fallbacks**
- "Please check this field and try again"
- "Something went wrong. Please try again or [contact support]."

### Error Message Placement
- **Inline (below field)**: Default for individual field errors — 4px below input
- **Summary (top of form)**: For submit-time validation — scrollable link list to each error
- **Toast / Banner**: For system errors (network, server) — not field-specific
- **Tooltip**: Only for supplementary warnings, never for critical errors

---

## 7. Multi-Step Form Patterns

### When to Use Multi-Step
- 7+ fields (threshold varies by complexity)
- Fields have logical groupings
- User needs to make decisions that affect subsequent fields
- Information collection spans different topics

### 7.1 Wizard Pattern (Linear Steps)
- **Structure**: Step indicator → content → back/next buttons
- **Step indicator**: Show all steps with labels; highlight current; mark completed with checkmark
- **Navigation**: Next validates current step; Back preserves data; steps are clickable only if completed
- **Final step**: Review all entered data before submission
- **Progress**: Show fraction: "Step 2 of 4" or progress bar

### 7.2 Stepper Pattern (Material Design)
- **Structure**: Vertical or horizontal stepper with expandable sections
- **Vertical stepper**: Better for forms where steps have variable content length
- **Horizontal stepper**: Better for fixed-step flows (checkout: Shipping → Payment → Review)
- **States**: Inactive, Active, Completed, Error

### 7.3 Accordion Pattern
- **Structure**: All steps visible as collapsed panels; one expanded at a time
- **Advantage**: User can see all sections and jump between them
- **Best for**: Settings, profile editing, forms where order doesn't matter
- **Validation**: Validate section on collapse; show error badge on section header

### 7.4 Progressive Disclosure
- **Structure**: Start with minimal fields; reveal more based on answers
- **Example**: "Do you have a referral code?" → [Yes] reveals code input
- **Animation**: Smooth expand with focus management to new fields
- **Best for**: Reducing perceived complexity; forms where some fields are conditional

### 7.5 Branching Logic
- **Structure**: Next step depends on current answers
- **Example**: "Account type" → [Personal] leads to SSN step; [Business] leads to EIN step
- **Implementation**: Decision tree with step mapping; save branch state for back navigation
- **Visualization**: Don't show full step count (it changes); use "Step X" without total

### 7.6 One-Thing-Per-Page (GDS Pattern)
- **Structure**: Each screen has exactly one question or decision
- **Origin**: UK Government Digital Service — proven in large-scale public forms
- **Advantage**: Minimum cognitive load; maximum accessibility; perfect for complex forms
- **Disadvantage**: More page loads; can feel slow for simple forms

### Multi-Step Implementation Rules
1. Validate per step before allowing advance
2. Allow back navigation without data loss
3. Persist data (localStorage or state management) for recovery
4. Show review/summary step before final submission
5. Allow editing from review step (click to jump back)
6. Submit button only on final step — intermediate steps use "Continue"/"Next"
7. Never reset the form on browser back button

---

## 8. Form Layout Patterns

### 8.1 Single Column (Default — Use This)
- **Research**: Single column forms complete 15.4 seconds faster than multi-column (CXL Institute)
- **Why**: Creates clear top-to-bottom reading path; no ambiguity about field order
- **Use for**: All mobile forms, most desktop forms, checkout, registration
- **Max width**: 400-560px for the form column; center on page

### 8.2 Two Column
- **When to use**: Related short fields (First name / Last name, City / State / ZIP)
- **Rules**: Only pair fields that are logically related and similar length
- **Never**: Put unrelated fields side by side — users may skip the right column
- **Responsive**: Stack to single column on mobile (always)
```css
.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}
@media (max-width: 640px) {
  .form-row { grid-template-columns: 1fr; }
}
```

### 8.3 Inline Layout
- **When to use**: Search bars, filter rows, compact action bars
- **Structure**: Multiple fields in a horizontal row with submit button
- **Example**: Search field + Location dropdown + "Search" button
- **Responsive**: Stack vertically on mobile

### 8.4 Floating Label Layout
- **How it works**: Label starts as placeholder, animates to small text above input on focus/fill
- **Pros**: Saves vertical space; modern appearance; label always visible when filled
- **Cons**: Limits label length; animation can distract; harder to implement accessibly
- **Implementation**: Must use real `<label>` element with `for` attribute
```css
.float-label {
  position: relative;
}
.float-label label {
  position: absolute;
  left: 12px; top: 50%;
  transform: translateY(-50%);
  transition: all 0.2s ease;
  pointer-events: none;
  color: var(--neutral-500);
}
.float-label input:focus + label,
.float-label input:not(:placeholder-shown) + label {
  top: 4px;
  font-size: 0.75rem;
  color: var(--primary-600);
}
```

### 8.5 Stacked Full-Width
- **When to use**: Mobile forms, landing page forms, modal forms
- **Structure**: Every field takes full container width
- **Submit button**: Full width on mobile; right-aligned or centered on desktop

### 8.6 Sectioned Layout
- **When to use**: Long forms with logical groups (account settings, checkout)
- **Structure**: Sections with headers and optional descriptions; dividers or spacing between sections
- **Pattern**: Section heading + description + fields (repeat)

---

## 9. Mobile Form Optimization

### Input Mode Attributes (Critical for Mobile)
```html
<!-- Numeric keypad (0-9 only, no decimals) -->
<input inputmode="numeric" pattern="[0-9]*">

<!-- Decimal keypad (0-9 with decimal point) -->
<input inputmode="decimal">

<!-- Email keyboard (with @ and . keys) -->
<input inputmode="email" type="email">

<!-- Phone keypad (0-9, +, *, #) -->
<input inputmode="tel" type="tel">

<!-- URL keyboard (with / and .com) -->
<input inputmode="url" type="url">

<!-- Search keyboard (with search/go button) -->
<input inputmode="search" type="search">

<!-- No special keyboard (default) -->
<input inputmode="text">
```

### Autocomplete Attributes (Enable Autofill)
```html
<input autocomplete="given-name">      <!-- First name -->
<input autocomplete="family-name">     <!-- Last name -->
<input autocomplete="email">           <!-- Email -->
<input autocomplete="tel">             <!-- Phone -->
<input autocomplete="street-address">  <!-- Street -->
<input autocomplete="address-line1">   <!-- Address line 1 -->
<input autocomplete="address-line2">   <!-- Apt/Suite -->
<input autocomplete="address-level2">  <!-- City -->
<input autocomplete="address-level1">  <!-- State/Province -->
<input autocomplete="postal-code">     <!-- ZIP -->
<input autocomplete="country">         <!-- Country -->
<input autocomplete="cc-number">       <!-- Card number -->
<input autocomplete="cc-exp">          <!-- Expiry -->
<input autocomplete="cc-csc">          <!-- CVC -->
<input autocomplete="cc-name">         <!-- Cardholder -->
<input autocomplete="new-password">    <!-- Registration -->
<input autocomplete="current-password"> <!-- Login -->
<input autocomplete="one-time-code">   <!-- OTP / 2FA -->
<input autocomplete="username">        <!-- Username -->
```

### Touch Target Sizing
- **Minimum**: 44x44px (Apple HIG), 48x48dp (Material Design)
- **Recommended**: 48x48px with 8px spacing between targets
- **Checkbox/radio**: Entire row is tappable (label + control), not just the control

### Mobile-Specific Rules
1. Single column always — no exceptions on mobile
2. Sticky submit button for long forms (fixed bottom)
3. Use native selects on mobile — custom dropdowns are worse
4. Disable zoom on input focus: `<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">`
5. Show numeric keyboard for numeric fields (inputmode, not type="number")
6. Place labels above fields (never to the left on mobile)
7. Auto-scroll to focused field when keyboard opens
8. Avoid modals/popups for form flows on mobile — use full-screen pages
9. Support paste in all fields (especially OTP)
10. Test with thumb reach zones — primary actions in bottom half of screen

---

## 10. Accessibility — Complete Form A11Y Guide

### Foundational Requirements

**Labels (WCAG 1.3.1, 3.3.2)**
- Every input MUST have a visible `<label>` with matching `for`/`id`
- Groups use `<fieldset>` + `<legend>` (radio groups, checkbox groups, address)
- `aria-label` or `aria-labelledby` only when visible label is impossible

**Error Identification (WCAG 3.3.1)**
- Errors must be identified in text (not color/icon alone)
- Connect error to field: `aria-describedby="email-error"` on input, `id="email-error"` on message
- Error messages must be programmatically associated

**Error Suggestion (WCAG 3.3.3)**
- Provide correction suggestion when possible
- "Email format: name@example.com"

**Error Prevention (WCAG 3.3.4)**
- Reversible: allow undo or edit after submission
- Checked: provide review step before irreversible actions
- Confirmed: require confirmation for destructive actions

### ARIA Attributes for Forms
```html
<!-- Required field -->
<input aria-required="true">

<!-- Field with error -->
<input aria-invalid="true" aria-describedby="field-error">
<span id="field-error" role="alert">Error message here</span>

<!-- Field with helper text -->
<input aria-describedby="field-help">
<span id="field-help">Helper text here</span>

<!-- Field with both helper and error -->
<input aria-describedby="field-help field-error" aria-invalid="true">

<!-- Combobox / autocomplete -->
<input role="combobox" aria-expanded="true" aria-controls="listbox-id"
       aria-activedescendant="option-3-id" aria-autocomplete="list">

<!-- Switch / toggle -->
<button role="switch" aria-checked="true">Enable notifications</button>
```

### Live Regions for Dynamic Content
```html
<!-- Error summary that appears on submit -->
<div role="alert" aria-live="assertive">
  Please fix 3 errors before submitting.
</div>

<!-- Character counter that updates as user types -->
<span aria-live="polite" aria-atomic="true">
  42 of 280 characters used
</span>

<!-- Async validation result -->
<span aria-live="polite">Username is available</span>
```

### Focus Management
1. On submit with errors: focus first invalid field (or error summary)
2. On multi-step next: focus first field of new step (or step heading)
3. On field add (repeatable): focus new field
4. On field remove: focus previous field or "Add" button
5. On modal open: trap focus inside modal; return focus to trigger on close
6. Tab order: must follow visual order; use `tabindex="0"` (never positive tabindex)

### Keyboard Navigation
- `Tab` / `Shift+Tab`: Move between fields
- `Enter`: Submit form (when not in textarea)
- `Space`: Toggle checkbox, activate button
- `Arrow keys`: Navigate radio groups, sliders, date pickers
- `Escape`: Close dropdown, dismiss modal, cancel edit
- All custom components must be fully keyboard-operable

### Screen Reader Announcements
- Required fields: Include "required" in label or use `aria-required`
- Character limits: Announce at 80% and 100% via `aria-live="polite"`
- Dynamic errors: Use `role="alert"` for immediate announcement
- Password strength: Announce level changes via live region
- Loading states: `aria-busy="true"` on the field or form

### Color and Contrast
- Error state: Do not rely on color alone — use icon + text + color
- Input borders: Minimum 3:1 contrast ratio against background (WCAG 1.4.11)
- Label text: Minimum 4.5:1 contrast (WCAG 1.4.3)
- Placeholder text: Minimum 4.5:1 (often fails — another reason not to use as labels)
- Focus ring: Minimum 3:1 contrast, 2px+ thickness

---

## 11. Form Performance Patterns

### 11.1 Autosave
- **When**: Long forms, multi-step flows, content creation
- **How**: Save to localStorage on field blur or debounced on change (2s)
- **UX**: Show "Draft saved" indicator (timestamp); auto-dismiss after 3s
- **Recovery**: On page load, check for saved draft; offer "Continue where you left off?"
```jsx
// Autosave hook
function useAutosave(formId, data, delay = 2000) {
  useEffect(() => {
    const timer = setTimeout(() => {
      localStorage.setItem(`draft-${formId}`, JSON.stringify({
        data,
        savedAt: Date.now()
      }));
    }, delay);
    return () => clearTimeout(timer);
  }, [formId, data, delay]);
}
```

### 11.2 Draft Recovery
- Check for draft on mount
- Show banner: "You have an unsaved draft from [time]. [Resume] [Discard]"
- Clear draft on successful submission
- Expire drafts after reasonable period (24h-7d depending on form)

### 11.3 Optimistic Submission
- Show success state immediately while request is in-flight
- If request fails, revert to form state with error message
- Best for: non-critical updates (profile changes, settings)
- Not for: payments, legal submissions, irreversible actions

### 11.4 Debounced Search / Validation
```jsx
function useDebouncedValue(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);
  return debounced;
}
```

### 11.5 Lazy Field Loading
- For forms with conditional sections, lazy-load heavy components (rich text editor, map, file uploader)
- Use `React.lazy()` + `Suspense` with loading skeleton

### 11.6 Form Submission States
1. **Idle**: Submit button enabled, default text ("Create Account")
2. **Submitting**: Button disabled, spinner + "Creating account..."
3. **Success**: Green check + "Account created!" → redirect or reset
4. **Error**: Red banner with retry option; form remains filled
5. **Rate limited**: "Too many attempts. Please try again in X seconds."

---

## 12. Specialized Form Patterns

### 12.1 Checkout Form
- **Fields**: Email, Shipping address, Shipping method, Payment, Billing address (checkbox: "Same as shipping"), Review
- **Optimization**: Guest checkout first (account creation after); auto-fill from browser; minimal fields
- **Trust signals**: Lock icon, security badges, payment provider logos, "Your data is encrypted"
- **Express checkout**: Apple Pay, Google Pay, Shop Pay buttons above the form
- **Address**: Single-field autocomplete expanding to individual fields
- **Payment**: Use hosted payment fields (Stripe Elements) for PCI compliance
- **Mobile**: One-thing-per-page pattern; sticky order summary

### 12.2 Registration / Sign-Up Form
- **Minimum viable**: Email + password (name optional at signup)
- **Social login**: "Continue with Google/Apple/GitHub" above email form
- **Progressive profiling**: Collect additional info over time, not all at registration
- **Password**: Strength meter + requirements checklist (show which are met in real-time)
- **Username**: Real-time availability check with suggestions
- **Confirmation**: Email verification flow (link or code)
- **Never**: Require username + email + password + confirm password + name + phone at signup

### 12.3 Login Form
- **Fields**: Email/username, password, "Remember me" checkbox, "Forgot password?" link
- **Error**: "Incorrect email or password" (never reveal which one is wrong)
- **Biometric**: Offer Face ID / Touch ID / Windows Hello after first login
- **Magic link**: "Email me a login link" as alternative to password
- **Rate limiting**: Lock after 5 attempts with increasing cooldown
- **Layout**: Centered card, max-width 400px, ample whitespace

### 12.4 Search with Filters
- **Structure**: Search bar (prominent) + filter panel (sidebar or collapsible)
- **Filter types**: Checkbox groups, radio buttons, range sliders, date range
- **Behavior**: Apply filters instantly (no submit button) or with "Apply" button for complex filters
- **Active filters**: Show as removable chips above results with "Clear all"
- **Mobile**: Filters in bottom sheet or full-screen modal with "Show X results" button
- **URL sync**: Reflect filter state in URL for shareability and back button

### 12.5 Settings / Preferences Form
- **Layout**: Sectioned with sidebar navigation or accordion
- **Save pattern**: Auto-save individual toggles; "Save changes" for text fields
- **Destructive settings**: Require confirmation ("Delete account" → confirm modal)
- **Defaults**: Show "(Default)" label; offer "Reset to defaults" per section
- **Search**: Add search for large settings pages (like VS Code settings)

### 12.6 Profile Editing
- **Pattern**: Display mode → Edit mode (inline editable or edit page)
- **Avatar**: Circular with camera icon overlay; crop on upload
- **Sections**: Personal info, contact, security, preferences, connected accounts
- **Save**: Per-section save or global save with change detection

### 12.7 Survey / Quiz Form
- **Pattern**: One question per page (recommended) or scrolling form
- **Question types**: Single choice, multiple choice, Likert scale, open text, ranking, matrix
- **Progress**: Progress bar with question count
- **Branching**: Skip logic based on answers
- **Required strategy**: Allow skipping non-essential questions; save partial responses
- **Completion**: Thank-you page with results (if applicable)

### 12.8 Booking / Scheduling Form
- **Flow**: Select service → Pick date → Pick time → Enter details → Confirm
- **Calendar**: Show availability (green = available, gray = unavailable); disable past dates
- **Time slots**: Show as button grid, not dropdown; gray out unavailable
- **Duration**: Auto-calculate end time from service selection
- **Timezone**: Auto-detect with option to change; show in slot display
- **Confirmation**: Summary with calendar add button (ICS file, Google Calendar link)

### 12.9 Contact Form
- **Fields**: Name, email, subject (optional), message, optional attachment
- **Anti-spam**: Honeypot field + reCAPTCHA v3 (invisible)
- **Success**: Clear confirmation: "We'll get back to you within 24 hours"
- **Alternative**: Show email address and phone number alongside form

### 12.10 Newsletter Subscription
- **Minimal**: Email + Submit (single field + button, inline layout)
- **Social proof**: "Join 50,000+ subscribers"
- **Expectations**: "Weekly tips, no spam, unsubscribe anytime"
- **Double opt-in**: Send confirmation email (required by GDPR for EU)

---

## 13. Anti-Patterns Encyclopedia — What NOT to Do

### Critical Anti-Patterns

1. **Placeholder as Label**: Disappears on focus; fails accessibility; confuses users
2. **Reset Button**: Almost never needed; one accidental click destroys all input
3. **Confirming Email/Password by Retyping**: Allow paste; show/hide toggle instead of confirm field
4. **CAPTCHA on Every Form**: Use invisible CAPTCHA (reCAPTCHA v3); visual CAPTCHA is hostile
5. **Disabled Submit Until Valid**: Users don't know why button is disabled; use enabled button + error on submit
6. **All Fields Required**: Only ask what you actually need; mark optional fields, not required
7. **Asterisk Without Legend**: If using * for required, include legend "* Required" near the form top
8. **Phone Number for Everything**: Don't require phone unless you will call/text; explain why if needed
9. **Gender as Required**: Often unnecessary; if needed, provide inclusive options + "Prefer not to say"
10. **Birthday for Age Verification**: Just ask "Are you 18+?" unless you actually need the date

### Validation Anti-Patterns

11. **Error on Focus**: Showing error when user first clicks into a field — they haven't typed yet
12. **Clearing the Field on Error**: User has to retype everything; keep their input
13. **Only Showing One Error at a Time**: Show all errors at once so user can fix them all
14. **Vague Errors**: "Invalid input" — tell them what's wrong and how to fix it
15. **Error Without Context**: "Error in field 3" — highlight the actual field
16. **Blocking Paste in Password Fields**: Hurts password manager users; reduces security
17. **Overly Strict Validation**: Rejecting valid names with hyphens, apostrophes, spaces, or non-Latin characters
18. **Validating Incomplete Input in Real-Time**: Showing "Invalid email" after typing just "j" — wait for blur

### Layout Anti-Patterns

19. **Multi-Column Forms on Mobile**: Always single column on mobile
20. **Horizontal Radio Buttons (5+ options)**: Stack vertically beyond 3 options
21. **Hidden Labels**: Every input needs a visible label; don't hide them for "cleanliness"
22. **Inconsistent Alignment**: Mixing left-aligned and centered fields in the same form
23. **Huge Forms Without Sections**: No visual grouping makes long forms overwhelming
24. **Modal Forms for Complex Input**: Use a dedicated page; modals are for simple confirmations

### Interaction Anti-Patterns

25. **Auto-Advancing Focus Without Warning**: Unexpected focus changes disorient users
26. **Form Timeout Without Warning**: Save progress; warn before session expires
27. **No Back Button Support**: Browser back should not destroy form data
28. **Submitting on Enter in Multi-Field Forms**: Can cause accidental submission; handle deliberately
29. **Custom Dropdowns on Mobile**: Native selects are always better on touch devices
30. **Auto-Formatting That Fights the User**: Format on blur, not on keystroke (except phone/card)

---

## 14. Form Analytics — Measuring Form Performance

### Key Metrics

**Completion Rate**
- Formula: `Submissions / Form Views * 100`
- Benchmark: 20-40% (varies wildly by form type)
- Track both started and completed

**Drop-Off Rate by Field**
- Which field causes the most abandonment?
- Measure time from focus to blur per field; flag outliers
- Track last field interacted before abandonment

**Field Timing**
- Average time to complete each field
- Fields taking >30 seconds indicate confusion
- Compare against expected time for field type

**Error Rate by Field**
- Which fields generate the most errors?
- Track error type frequency (required, format, custom)
- High error rate = redesign the field

**Interaction Metrics**
- Tab vs. click navigation ratio
- Backspace/delete frequency per field (indicates confusion)
- Paste usage (especially in card/code fields)

### Analytics Implementation
```jsx
// Track field interaction events
function trackFieldEvent(fieldName, event, metadata = {}) {
  analytics.track('form_field_event', {
    form_id: formId,
    field_name: fieldName,
    event_type: event, // 'focus', 'blur', 'error', 'change', 'paste'
    timestamp: Date.now(),
    time_spent: metadata.duration,
    error_message: metadata.error,
    attempt_number: metadata.attempt
  });
}

// Track form-level events
function trackFormEvent(event, metadata = {}) {
  analytics.track('form_event', {
    form_id: formId,
    event_type: event, // 'view', 'start', 'submit', 'success', 'error', 'abandon'
    step: metadata.step,
    fields_completed: metadata.fieldsCompleted,
    total_fields: metadata.totalFields,
    duration: metadata.duration,
    error_count: metadata.errorCount
  });
}
```

### Funnel Analysis for Multi-Step Forms
- Track conversion rate between each step
- Identify the "killer step" (highest drop-off)
- A/B test step order and grouping
- Monitor review-step-to-submit conversion (should be >90%)

---

## 15. CSS / React Code Snippets for Key Patterns

### 15.1 Base Form Field Component (React + CSS)
```tsx
interface FormFieldProps {
  label: string;
  name: string;
  type?: string;
  error?: string;
  helperText?: string;
  required?: boolean;
  disabled?: boolean;
}

function FormField({
  label, name, type = 'text', error, helperText, required, disabled
}: FormFieldProps) {
  const inputId = `field-${name}`;
  const errorId = `${inputId}-error`;
  const helperId = `${inputId}-helper`;
  const describedBy = [
    error && errorId,
    helperText && helperId
  ].filter(Boolean).join(' ') || undefined;

  return (
    <div className="form-field">
      <label htmlFor={inputId} className="form-label">
        {label}
        {required && <span aria-hidden="true"> *</span>}
      </label>
      <input
        id={inputId}
        name={name}
        type={type}
        className={`form-input ${error ? 'form-input--error' : ''}`}
        aria-required={required}
        aria-invalid={!!error}
        aria-describedby={describedBy}
        disabled={disabled}
      />
      {error && (
        <span id={errorId} className="form-error" role="alert">
          {error}
        </span>
      )}
      {helperText && !error && (
        <span id={helperId} className="form-helper">
          {helperText}
        </span>
      )}
    </div>
  );
}
```

```css
.form-field {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.form-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--neutral-700);
}

.form-input {
  height: 40px;
  padding: 0 12px;
  border: 1px solid var(--neutral-300);
  border-radius: 8px;
  font-size: 1rem;
  color: var(--neutral-900);
  background: white;
  transition: border-color 0.15s, box-shadow 0.15s;
}

.form-input:hover {
  border-color: var(--neutral-400);
}

.form-input:focus {
  outline: none;
  border-color: var(--primary-500);
  box-shadow: 0 0 0 3px var(--primary-100);
}

.form-input--error {
  border-color: var(--error-500);
}

.form-input--error:focus {
  box-shadow: 0 0 0 3px var(--error-100);
}

.form-input:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  background: var(--neutral-50);
}

.form-error {
  font-size: 0.8125rem;
  color: var(--error-600);
  display: flex;
  align-items: center;
  gap: 4px;
}

.form-helper {
  font-size: 0.8125rem;
  color: var(--neutral-500);
}
```

### 15.2 Floating Label Pattern (CSS Only)
```css
.floating-field {
  position: relative;
  margin-top: 16px;
}

.floating-field input {
  width: 100%;
  height: 56px;
  padding: 24px 12px 8px;
  border: 1px solid var(--neutral-300);
  border-radius: 8px;
  font-size: 1rem;
  background: white;
}

.floating-field label {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1rem;
  color: var(--neutral-500);
  pointer-events: none;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: left top;
}

.floating-field input:focus + label,
.floating-field input:not(:placeholder-shown) + label {
  top: 8px;
  transform: translateY(0);
  font-size: 0.75rem;
  color: var(--primary-600);
}

.floating-field input:focus {
  border-color: var(--primary-500);
  outline: none;
  box-shadow: 0 0 0 3px var(--primary-100);
}
```

### 15.3 Multi-Step Form Hook (React)
```tsx
function useMultiStepForm(steps: string[]) {
  const [currentStep, setCurrentStep] = useState(0);
  const [formData, setFormData] = useState<Record<string, any>>({});
  const [completedSteps, setCompletedSteps] = useState<Set<number>>(new Set());

  const next = () => {
    setCompletedSteps(prev => new Set([...prev, currentStep]));
    setCurrentStep(prev => Math.min(prev + 1, steps.length - 1));
  };

  const back = () => setCurrentStep(prev => Math.max(prev - 1, 0));

  const goTo = (step: number) => {
    if (completedSteps.has(step) || step === currentStep) {
      setCurrentStep(step);
    }
  };

  const updateData = (stepData: Record<string, any>) => {
    setFormData(prev => ({ ...prev, ...stepData }));
  };

  return {
    currentStep,
    stepName: steps[currentStep],
    totalSteps: steps.length,
    isFirstStep: currentStep === 0,
    isLastStep: currentStep === steps.length - 1,
    completedSteps,
    formData,
    next,
    back,
    goTo,
    updateData
  };
}
```

### 15.4 Debounced Validation Hook
```tsx
function useDebouncedValidation(
  value: string,
  validate: (val: string) => Promise<string | null>,
  delay = 500
) {
  const [error, setError] = useState<string | null>(null);
  const [isValidating, setIsValidating] = useState(false);

  useEffect(() => {
    if (!value) { setError(null); return; }

    setIsValidating(true);
    const timer = setTimeout(async () => {
      const result = await validate(value);
      setError(result);
      setIsValidating(false);
    }, delay);

    return () => { clearTimeout(timer); setIsValidating(false); };
  }, [value, delay]);

  return { error, isValidating };
}
```

### 15.5 Form Error Summary Component
```tsx
function ErrorSummary({ errors }: { errors: Record<string, string> }) {
  const errorEntries = Object.entries(errors);
  if (errorEntries.length === 0) return null;

  return (
    <div role="alert" className="error-summary">
      <h2>There {errorEntries.length === 1 ? 'is 1 error' : `are ${errorEntries.length} errors`} in this form</h2>
      <ul>
        {errorEntries.map(([field, message]) => (
          <li key={field}>
            <a href={`#field-${field}`} onClick={(e) => {
              e.preventDefault();
              document.getElementById(`field-${field}`)?.focus();
            }}>
              {message}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

```css
.error-summary {
  border: 2px solid var(--error-500);
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 24px;
  background: var(--error-50);
}

.error-summary h2 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--error-700);
  margin: 0 0 8px;
}

.error-summary ul {
  margin: 0; padding: 0 0 0 20px;
}

.error-summary a {
  color: var(--error-700);
  text-decoration: underline;
}
```

### 15.6 Password Strength Meter
```tsx
function getPasswordStrength(password: string) {
  let score = 0;
  if (password.length >= 8) score++;
  if (password.length >= 12) score++;
  if (/[a-z]/.test(password) && /[A-Z]/.test(password)) score++;
  if (/\d/.test(password)) score++;
  if (/[^a-zA-Z0-9]/.test(password)) score++;

  const levels = ['', 'Weak', 'Fair', 'Good', 'Strong', 'Excellent'];
  const colors = ['', 'var(--error-500)', 'var(--warning-500)',
                  'var(--warning-400)', 'var(--success-500)', 'var(--success-600)'];
  return { score, label: levels[score], color: colors[score] };
}

function PasswordStrength({ password }: { password: string }) {
  const { score, label, color } = getPasswordStrength(password);
  if (!password) return null;

  return (
    <div aria-live="polite">
      <div className="strength-bar">
        {[1,2,3,4,5].map(i => (
          <div key={i} className="strength-segment"
            style={{ background: i <= score ? color : 'var(--neutral-200)' }} />
        ))}
      </div>
      <span className="strength-label" style={{ color }}>{label}</span>
    </div>
  );
}
```

---

## 16. Form Design Checklist

### Before Building
- [ ] Is every field necessary? Remove any you can live without
- [ ] Is the form as short as possible for the use case?
- [ ] Are fields in logical order (name before address, not interleaved)?
- [ ] Are optional fields marked (not required fields)?
- [ ] Is there a clear value proposition above the form?

### During Building
- [ ] Every field has a visible `<label>` with `for`/`id`
- [ ] Correct `type`, `inputmode`, and `autocomplete` on every field
- [ ] All states implemented (default, focus, filled, error, disabled)
- [ ] Error messages follow the formula: [what's wrong] + [how to fix]
- [ ] Tab order matches visual order
- [ ] Submit button has clear action text ("Create Account" not "Submit")

### After Building
- [ ] Test with keyboard only (no mouse)
- [ ] Test with screen reader (VoiceOver/NVDA)
- [ ] Test on mobile (real device, not just emulator)
- [ ] Test with autofill (browser and password manager)
- [ ] Test error states for every field
- [ ] Test with slow network (3G throttle)
- [ ] Test long content (long names, long emails)
- [ ] Test international input (accented characters, RTL text)
- [ ] Set up analytics tracking for completion rate and drop-off

---

## Cross-References
- component-patterns-code (React component implementations)
- micro-copy-intelligence (error messages, helper text, button labels)
- conversion-optimization-patterns (form conversion, CTA optimization)
- accessibility-inclusive-design (WCAG compliance, screen reader testing)
- mobile-ux-design (touch targets, mobile patterns)
- interaction-motion-design (form transitions, validation animations)
- performance-states-patterns (loading, empty, error states)
- navigation-pattern-encyclopedia (form navigation, multi-step flows)
