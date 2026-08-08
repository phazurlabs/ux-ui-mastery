# Anti-Pattern Encyclopedia — What NOT to Ship

## What Makes Something an Anti-Pattern

An anti-pattern is not just "bad design." It is a pattern that appears to solve a problem but actually creates worse problems. Anti-patterns are dangerous precisely because they look reasonable — a dropdown with 200 countries seems like it solves "select your country," but it creates a 30-second interaction for a 2-second task. The correct pattern is a searchable combobox.

This encyclopedia catalogs 100+ anti-patterns organized by category, each with: what it looks like, why it seems reasonable, why it actually fails, what to use instead, and the cognitive science behind the failure.

---

## Navigation Anti-Patterns

### N1. Desktop Hamburger Menu
**What it looks like**: Three-line icon hiding the primary navigation on desktop (1024px+).
**Why it seems reasonable**: "Clean" design. Minimalist. More space for content.
**Why it fails**: Nielsen Norman Group's quantitative study (179 participants, six sites) found that hiding navigation cuts content discoverability by nearly half. Navigation hidden behind a click is navigation users don't use. Desktop screens have plenty of room for visible navigation.
**Use instead**: Sidebar navigation, top navigation bar, or command palette.
**Cognitive principle**: Recognition over recall (Nielsen H6). Users cannot recall what they cannot see.
**Severity**: High — directly reduces feature discovery and task completion.

### N2. Infinite Navigation Depth Without Breadcrumbs
**What it looks like**: Clicking into nested content (Category → Subcategory → Item → Detail → Sub-detail) with no breadcrumb trail or back path other than the browser back button.
**Why it fails**: Users lose their sense of position. The navigational mental model collapses. "Where am I?" anxiety increases with every level.
**Use instead**: Breadcrumbs at every level deeper than 2. Or flatten the hierarchy.
**Cognitive principle**: Spatial memory + wayfinding. Users need landmarks.
**Severity**: High — users get lost and abandon tasks.

### N3. Mystery Navigation Icons
**What it looks like**: Icon-only navigation without labels. A gear icon, a person icon, a chart icon — no text.
**Why it fails**: Icons are ambiguous. A gear could mean Settings, Preferences, Configuration, or Tools. Google's own research showed that adding text labels to icons increased usage by 40%. Icons are recognition aids, not replacements for labels.
**Use instead**: Icons WITH labels. Always. The only exception is universally understood icons (home, search, close) in space-constrained contexts.
**Cognitive principle**: Recognition over recall. Ambiguous icons force guessing.
**Severity**: Medium — reduces efficiency, increases cognitive load.

### N4. Hijacking the Back Button
**What it looks like**: The browser back button does something unexpected — opens a modal, redirects to a different page, or does nothing.
**Why it fails**: The back button is the most used browser control. Users have a deeply ingrained mental model: "Back takes me to the previous page." Violating this causes confusion and frustration.
**Use instead**: Respect browser history. If your app manages state, use `history.pushState` correctly so back navigates logically.
**Cognitive principle**: Jakob's Law. Users expect your app to work like every other app they use.
**Severity**: Critical — violates one of the most fundamental web conventions.

### N5. Scroll-Jacking
**What it looks like**: Custom JavaScript overriding native scroll behavior — slower scroll, horizontal scroll when user scrolls vertically, scroll "sections" that lock to positions, parallax that makes scroll distance unpredictable.
**Why it fails**: Users have proprioceptive expectations for scroll. Their thumb/finger movement maps to a predictable content shift. Scroll-jacking breaks this mapping, causing motion sickness, disorientation, and frustration.
**Use instead**: Native scroll. CSS scroll-snap for sectioned content if needed. Never override scroll speed or direction.
**Cognitive principle**: Motor memory + expectation violation. The physical-to-visual mapping must be predictable.
**Severity**: High — users physically feel this violation.

### N6. Nav That Disappears on Scroll (No Return)
**What it looks like**: Navigation hides on scroll-down (fine) but doesn't reappear on scroll-up (not fine). User must scroll all the way to the top to access nav.
**Why it fails**: Users expect scroll-down = hide (content focus), scroll-up = show (navigation intent). Requiring scroll-to-top is a Fitts's Law violation — the target is maximally far from the user's position.
**Use instead**: Hide on scroll-down, show on any scroll-up. Or keep nav permanently visible.
**Severity**: Medium — frustrating for long pages.

### N7. Bottom Nav + Top Tabs + Hamburger
**What it looks like**: Three navigation systems simultaneously — bottom bar for primary nav, top tabs for section nav, and a hamburger for overflow.
**Why it fails**: Three levels of navigation creates spatial confusion. Users don't know which navigation to use for which purpose. Mental model overload.
**Use instead**: One primary navigation system. If you need secondary navigation, make the hierarchy clear (e.g., bottom nav for app-level, tabs for page-level).
**Severity**: Medium — confusing, cluttered, amateur.

---

## Data Display Anti-Patterns

### D1. Data Table on Mobile Without Adaptation
**What it looks like**: A multi-column table displayed on a 375px screen with horizontal scroll.
**Why it fails**: Tables are inherently wide. On mobile, horizontal scrolling is disorienting and hides columns. Users miss critical data in off-screen columns.
**Use instead**: Responsive stacked layout (each row becomes a card), collapsible row details, or a list view with key information and tap-to-expand.
**Severity**: High — makes the primary data view unusable on mobile.

### D2. Chart Without Tooltip or Data Access
**What it looks like**: A bar chart or line chart with no way to see exact values. Mouse-over shows nothing.
**Why it fails**: Charts show trends; tooltips show precision. Without tooltips, users must estimate values from axis positions — inaccurate and frustrating for data-driven decisions.
**Use instead**: Always add tooltips on hover/touch. Include a "View as table" alternative.
**Severity**: Medium — reduces data utility.

### D3. Pie Chart With 12 Segments
**What it looks like**: A pie chart with many small slices, some barely visible, some overlapping in the legend.
**Why it fails**: Humans are poor at comparing angles. Beyond 5-7 segments, pie charts become unreadable. Small slices (< 5%) are indistinguishable.
**Use instead**: Horizontal bar chart for comparison. Donut chart for max 5 segments. Table for exact values.
**Cognitive principle**: Perceptual accuracy. Length (bar charts) is decoded ~5x more accurately than angle (pie charts).
**Severity**: Medium — misleading data presentation.

### D4. Blank Empty State
**What it looks like**: A white screen or an empty container when there's no data. Maybe the text "No items" and nothing else.
**Why it fails**: Empty states are the #1 opportunity to guide users, and the most commonly wasted moment. A blank screen tells the user nothing — not what this section is for, not how to populate it, not what it would look like with data.
**Use instead**: Illustration + explanation + primary action CTA. "No projects yet — Start by creating your first project."
**Cognitive principle**: Progressive disclosure + onboarding. The empty state IS onboarding for that feature.
**Severity**: High — lost opportunity at the highest-impact moment.

### D5. Auto-Advancing Carousel on Homepage
**What it looks like**: Hero section with 3-5 slides auto-advancing every 3-5 seconds.
**Why it fails**: < 1% of users interact with slides beyond the first (NNG data). Auto-advance violates user control (H3). Accessibility failure (WCAG 2.2.2 requires pause/stop control). Content in later slides is effectively hidden.
**Use instead**: Single hero with strong messaging. Or a static grid/bento layout.
**Severity**: High — wastes prime real estate, accessibility failure, false sense of content coverage.

### D6. Skeleton Screen That Doesn't Match Content Layout
**What it looks like**: Generic skeleton shapes (random rectangles and circles) that don't correspond to the actual content that will appear.
**Why it fails**: The entire point of skeleton screens is to set spatial expectations. If the skeleton doesn't match the real layout, it creates a jarring shift when content loads — worse than a simple spinner.
**Use instead**: Skeleton shapes that precisely match the layout of real content. Same widths, heights, and positions.
**Severity**: Low-medium — better than a spinner but wasted potential.

### D7. Notification Badge Overload
**What it looks like**: Red badges on every navigation item. Notification count showing "99+." Multiple competing badges.
**Why it fails**: When everything screams for attention, nothing gets attention. Badge blindness sets in. Users stop trusting the badges and ignore them all — including legitimately important ones.
**Use instead**: Badge only on items that genuinely need attention. Clear badges after viewing. Group notifications. Use subtle dots instead of counts for low-priority items.
**Cognitive principle**: Signal-to-noise ratio. Alarm fatigue.
**Severity**: Medium — reduces effectiveness of all notifications.

---

## Input & Form Anti-Patterns

### F1. Placeholder-Only Labels
**What it looks like**: Input fields with placeholder text as the only label. When the user clicks and starts typing, the label disappears.
**Why it fails**: User forgets what the field is for mid-entry. Can't review the form because labels are gone for filled fields. Accessibility failure: screen readers may not announce placeholders consistently. Violates WCAG 3.3.2 (Labels or Instructions).
**Use instead**: Visible label above the field (always). Placeholder as supplementary hint only.
**Severity**: Critical — accessibility failure, usability failure.

### F2. Password Restrictions Theater
**What it looks like**: "Password must contain 1 uppercase, 1 lowercase, 1 number, 1 special character, be 8-16 characters, not contain your username, not be a previously used password."
**Why it fails**: Complex requirements don't improve security (NIST SP 800-63B deprecated them). They increase friction, increase password-reset rate, and encourage users to write passwords down or use patterns like "Password1!". Length matters more than complexity.
**Use instead**: Minimum 8 characters, no maximum, strength indicator, support for password managers, never disable paste.
**Severity**: Medium — friction without security benefit.

### F3. Captcha Before Any Suspicious Behavior
**What it looks like**: Every user must solve a captcha before signing up, logging in, or submitting a form.
**Why it fails**: Captchas punish all users for the potential actions of bots. They're annoying, accessibility-problematic (image captchas exclude blind users), and increasingly solvable by bots anyway.
**Use instead**: Invisible captcha (Cloudflare Turnstile, reCAPTCHA v3) that only challenges suspicious behavior. Honeypot fields. Rate limiting.
**Severity**: Medium — friction and accessibility concern.

### F4. Select Dropdown With 200+ Unsearchable Options
**What it looks like**: A `<select>` for country, state, or timezone with a long scrollable list and no search/filter.
**Why it fails**: Scrolling through 200 countries to find "United States" takes 30+ seconds. Users in the US expect it near the top; users elsewhere are punished with a long scroll.
**Use instead**: Searchable combobox. Type "United" → see "United States, United Kingdom." Or detect via IP and pre-select.
**Cognitive principle**: Hick's Law. Decision time increases with number of options. Search reduces effective options to ~1-3.
**Severity**: High — massive friction for a simple selection.

### F5. Form That Clears on Validation Error
**What it looks like**: User fills out a long form, hits submit, gets a validation error, and the form is reset — all input lost.
**Why it fails**: The user just invested cognitive effort filling 10+ fields. Losing that work is one of the most frustrating UX failures possible. Users may abandon entirely.
**Use instead**: Preserve all input on validation failure. Highlight the specific field(s) with errors. Scroll to the first error.
**Severity**: Critical — data loss, user rage, abandonment.

### F6. Premature Validation (Validate on Keystroke)
**What it looks like**: Error message appears while the user is still typing. "Invalid email" shows after typing "j" — the user hasn't finished yet.
**Why it fails**: The system is judging an incomplete action. It creates anxiety and distrust. The user knows they're not done — the error message is noise.
**Use instead**: Validate on blur (when the user leaves the field). Or on submit. For password strength, real-time feedback is acceptable because it's assistive, not punitive.
**Severity**: Medium — annoying, erodes trust.

### F7. Disabled Submit Button Without Explanation
**What it looks like**: Submit button is grayed out/disabled with no indication of what's missing.
**Why it fails**: User sees the button but can't use it. They don't know why. They fill in more fields, but the button stays disabled. No feedback loop.
**Use instead**: Either enable the button and show validation errors on click, OR show a tooltip/message on the disabled button explaining what's needed: "Complete all required fields to continue."
**Severity**: Medium — confusing, blocks task completion.

### F8. Date Entry as Text Field Without Picker
**What it looks like**: "Enter date (MM/DD/YYYY)" with a plain text input.
**Why it fails**: Users in different locales have different date formats. "01/02/2025" is January 2 in the US and February 1 in Europe. Text input invites format errors. No calendar context (day of week, weekends).
**Use instead**: Date picker (calendar popup). Native `<input type="date">` as minimum. Format shown as example, not just placeholder.
**Severity**: High — error-prone, locale confusion.

---

## Layout Anti-Patterns

### L1. Fixed-Width Layout on Modern Screens
**What it looks like**: Content locked to 960px or 1200px centered on a 2560px monitor, with vast empty margins.
**Why it fails**: Wastes 40-60% of screen real estate on wide monitors. Users with large screens bought them to see more, not more whitespace.
**Use instead**: Fluid layout with max-width for readability + grid that utilizes available space. Dashboard widgets can expand. Sidebars can show more detail.
**Severity**: Low-medium — functional but wasteful.

### L2. Z-Index Wars
**What it looks like**: Overlapping elements competing for z-index. Tooltips behind modals. Modals behind drawers. Dropdowns behind sticky headers.
**Why it fails**: Z-index without a system creates unpredictable layering. Elements appear and disappear randomly. Often caused by libraries with conflicting z-index values.
**Use instead**: A defined z-index scale: base (0), dropdowns (100), sticky headers (200), overlays/drawers (300), modals (400), toasts (500), tooltips (600). Enforce through design tokens.
**Severity**: Medium — unpredictable, hard to debug.

### L3. Cards Within Cards Within Cards
**What it looks like**: A card containing a card containing another card. Triple nesting of bordered containers.
**Why it fails**: Visual nesting creates confusion about relationships and boundaries. Which card do I click? Where does one thing end and another begin? "Matryoshka syndrome."
**Use instead**: Flat layout with spacing and dividers to create hierarchy. Use one level of card containment maximum. For nested data, use accordion or tree view.
**Severity**: Medium — visual confusion, cognitive load.

### L4. Content That Can't Be Reached (Floating Element Blocking)
**What it looks like**: A cookie banner, chat widget, and floating CTA button all stacked at the bottom of the screen, covering the last 150px of content.
**Why it fails**: Critical content (footer links, form submit buttons, last items in a list) is permanently hidden behind floating elements. Users have no way to reach it.
**Use instead**: Maximum 1 floating element. Ensure content has padding-bottom equal to the floating element height. Or use non-floating alternatives.
**Severity**: High — blocks content access, potential legal issue (if footer contains legal links).

---

## Commerce Anti-Patterns

### C1. Hidden Costs Until Checkout
**What it looks like**: Product shows $29.99. Cart shows $29.99. Checkout reveals: + $8.99 shipping + $3.50 handling + $2.40 tax = $44.88.
**Why it fails**: The #2 cause of cart abandonment (after requiring account creation). Users feel deceived. Trust is destroyed at the moment you need it most.
**Use instead**: Show total estimated cost as early as possible. Shipping estimates on product page. "Free shipping over $X" messaging. Tax shown before final step.
**Severity**: Critical — revenue killer, trust destroyer.

### C2. Forced Account Creation to Purchase
**What it looks like**: "Create an account to continue checkout." No guest checkout option.
**Why it fails**: The #1 cause of cart abandonment (Baymard Institute). Users with purchase intent are blocked by an irrelevant task. They came to buy, not to create a relationship.
**Use instead**: Guest checkout with optional account creation post-purchase. "Save your info for next time?" after order is placed.
**Severity**: Critical — directly measurable revenue loss.

### C3. False Scarcity / Fake Urgency
**What it looks like**: "Only 2 left!" when there are actually 200. Countdown timer that resets when it reaches zero. "5 people are viewing this right now" with a made-up number.
**Why it fails**: Users are increasingly aware of these tactics. When discovered, trust is permanently destroyed. Increasingly illegal under EU Digital Services Act and FTC enforcement.
**Use instead**: Real inventory counts if genuinely low. Real-time actual viewer counts. No countdown timers unless tied to a real deadline.
**Severity**: Critical — ethical violation, legal risk, trust destruction.

### C4. Dark Pattern Subscription Cancellation
**What it looks like**: Subscribe with one click. Cancel requires: Settings → Account → Billing → Subscription → Cancel → "Are you sure?" → "Here's a discount" → "Tell us why" → "Are you REALLY sure?" → "Processing..." → "Your cancellation will take effect..."
**Why it fails**: FTC's "Click-to-Cancel" rule (2024) requires cancellation to be as easy as subscription. This is now a legal liability. Beyond legality, it breeds resentment and negative reviews.
**Use instead**: Cancel in the same place you subscribe. One confirmation step maximum. Retention offer is OK (one screen, one offer), but must include a clear "Cancel anyway" button.
**Severity**: Critical — legal violation, brand damage.

---

## Feedback Anti-Patterns

### FB1. Error Message: "An Error Occurred"
**What it looks like**: Generic error with no specifics. "Something went wrong. Please try again." No error code, no explanation, no next step.
**Why it fails**: The user doesn't know what happened, whether it was their fault, whether their data was saved, or what to do next. Anxiety and helplessness.
**Use instead**: Specific error + explanation + recovery action. "Payment failed: your card was declined. Try a different payment method or contact your bank."
**Severity**: High — abandonment, support tickets, user frustration.

### FB2. Success State With No Confirmation
**What it looks like**: User clicks "Save" and... nothing visible happens. No toast, no color change, no message. Did it save?
**Why it fails**: Violates H1 (Visibility of System Status). The user doesn't know if their action succeeded. They may click again (duplicate action) or navigate away (losing unsaved changes).
**Use instead**: Toast ("Settings saved"), inline confirmation (checkmark), button text change ("Saved!"), or subtle animation.
**Severity**: Medium — uncertainty, potential duplicate actions.

### FB3. Alert/Notification for Non-Critical Events
**What it looks like**: `alert()` dialog or modal for "Your preferences have been updated." Blocking the user for a non-critical informational message.
**Why it fails**: Modals demand attention and require action (clicking OK). Using them for routine confirmations trains users to dismiss all modals reflexively — including important ones. Alert fatigue.
**Use instead**: Toast/snackbar for non-critical confirmations. Reserve modals for actions requiring a decision.
**Severity**: Medium — alert fatigue, interrupted flow.

### FB4. Loading With No Feedback (Blank Screen)
**What it looks like**: User clicks a link or button. The screen goes blank for 2-5 seconds before content appears. No spinner, no skeleton, no progress indicator.
**Why it fails**: After 1 second of no feedback, users assume something is broken. After 3 seconds, they click again (duplicate request) or navigate away. The Doherty Threshold demands feedback within 400ms.
**Use instead**: Instant skeleton screen (< 100ms). Or spinner if layout is unknown. Or optimistic UI (show the result immediately, sync in background).
**Severity**: High — user thinks app is broken.

---

## Accessibility Anti-Patterns

### A1. Color as the Only Indicator
**What it looks like**: Red text for errors, green for success, yellow for warnings — with no icon, no bold, no other visual differentiation.
**Why it fails**: ~8% of men and ~0.5% of women have color vision deficiency. Red/green colorblindness is the most common type. Using color alone means these users cannot distinguish error from success.
**Use instead**: Color + icon + text. Triple encoding: red color + X icon + "Error: [message]". Green color + checkmark icon + "Success: [message]".
**Severity**: Critical — accessibility failure, affects ~300M people globally.

### A2. No Visible Focus Indicator
**What it looks like**: Keyboard tab navigation shows no visual indicator of which element is focused. CSS `outline: none` or `outline: 0` with no replacement.
**Why it fails**: Keyboard users (including screen reader users, motor-impaired users, and power users) cannot see where they are on the page. They're navigating blind. WCAG 2.4.7 failure.
**Use instead**: `outline: 2px solid [focus-color]` with `outline-offset: 2px`. Or use `:focus-visible` for keyboard-only focus rings that don't appear on mouse click.
**Severity**: Critical — blocks keyboard navigation entirely.

### A3. Click Target < 44px
**What it looks like**: Small icon buttons, tiny close (x) buttons, tight link spacing, checkbox/radio buttons at default browser size (13px).
**Why it fails**: Touch targets below 44×44pt (iOS) or 48×48dp (Android) cause tap errors, especially for users with motor impairments, large fingers, or in mobile contexts. WCAG 2.5.8 (Target Size minimum).
**Use instead**: Minimum 44×44px for all interactive elements. Generous padding. Spacing between targets to prevent accidental taps.
**Severity**: High — usability failure on touch devices, accessibility violation.

### A4. Auto-Playing Video/Audio With Sound
**What it looks like**: Video or audio that plays automatically with sound when the page loads.
**Why it fails**: Startles users. Disrupts screen reader audio. Inaccessible to deaf users if captions aren't shown. WCAG 1.4.2 (Audio Control) failure. Most browsers now block this, but workarounds still appear.
**Use instead**: Autoplay muted only. User-initiated play for audio. Captions on by default.
**Severity**: High — accessibility failure, user hostility.

### A5. Keyboard Trap
**What it looks like**: User tabs into a component (modal, widget, embed) and cannot tab out. Focus is trapped with no escape mechanism.
**Why it fails**: The user is stuck. They cannot navigate forward or backward. The only option is to close the tab or use a mouse.
**Use instead**: Focus trap only for modals (with Escape to close). All other components: Tab moves focus to the next element normally.
**Severity**: Critical — completely blocks keyboard users.

---

## AI-Specific Anti-Patterns

### AI1. AI Output Without Attribution or Uncertainty
**What it looks like**: AI-generated content presented as fact with no source, no confidence indicator, no disclaimer.
**Why it fails**: AI hallucinates. Presenting AI output as authoritative truth is dangerous for any domain with factual stakes (medical, legal, financial). Users who trust unattributed AI output can make harmful decisions.
**Use instead**: Source citations. Confidence indicators. "AI-generated" label. "Verify this information" disclaimer for factual claims.
**Severity**: High — trust and safety issue.

### AI2. AI That Acts Without Confirmation
**What it looks like**: AI assistant that executes actions (sends emails, deletes files, publishes content) without asking "Are you sure?"
**Why it fails**: AI misinterprets intent. A misunderstood command that sends an email to the wrong person, deletes the wrong file, or publishes a draft is hard to undo and potentially catastrophic.
**Use instead**: Preview before execution for all consequential actions. "I'll send this email to alice@company.com. Confirm?" Undo for reversible actions.
**Severity**: Critical — irreversible harm potential.

### AI3. Infinite Loading Without Streaming
**What it looks like**: User sends a prompt to AI. Spinner for 10-30 seconds. Then the full response appears at once.
**Why it fails**: 10+ seconds of spinner with no feedback feels broken. The user doesn't know if the AI is working, stuck, or errored. They may retry (duplicate request) or abandon.
**Use instead**: Stream the response token-by-token. Show "Thinking..." with elapsed time. Show intermediate steps if applicable.
**Severity**: Medium — perceived performance issue.

### AI4. AI Settings With No Granularity
**What it looks like**: AI is either ON or OFF. No control over what it can access, what it can do, or when it activates.
**Why it fails**: Users have varying comfort levels with AI. Some want AI to read their documents but not send messages. Some want AI suggestions in writing but not in code. Binary control forces an all-or-nothing choice.
**Use instead**: Per-feature AI toggles. Read vs. write permissions. Per-workspace settings. Clear data access indicators.
**Severity**: Medium — trust and control issue.

---

## The Vibe Coder's Top 10 Anti-Patterns

The most common anti-patterns in AI-generated/vibe-coded applications, ranked by frequency:

| Rank | Anti-Pattern | Frequency | Fix |
|------|-------------|-----------|-----|
| 1 | Missing states (only default state built) | ~90% of vibe-coded apps | Build all 10 states for every component |
| 2 | No loading states (blank screen while fetching) | ~85% | Add skeleton screens |
| 3 | Placeholder-only labels on forms | ~70% | Add visible labels above every input |
| 4 | No empty states (blank when no data) | ~70% | Add illustration + explanation + CTA |
| 5 | Generic error messages | ~65% | Write specific, helpful error messages |
| 6 | No keyboard navigation | ~60% | Add focus styles, ARIA, tab order |
| 7 | Inconsistent visual language | ~55% | Extract design tokens with `/tokens` |
| 8 | No mobile responsiveness | ~50% | Add responsive breakpoints |
| 9 | No command palette or keyboard shortcuts | ~50% | Add Cmd+K with cmdk library |
| 10 | Color-only status indicators | ~45% | Add icons and text to all status colors |

These 10 anti-patterns, if fixed, would elevate most vibe-coded apps from a 5/10 to a 7-8/10 pattern quality score.
