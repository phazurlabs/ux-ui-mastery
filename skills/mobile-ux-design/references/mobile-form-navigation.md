# Mobile Forms and Navigation — Comprehensive Design Reference

## Mobile Form Design Philosophy

Every form on mobile is a negotiation between the information the system needs and the patience the user has. On desktop, users tolerate longer forms because they have a full keyboard, a large screen, and often a more committed mindset. On mobile, every additional field increases abandonment. The discipline of mobile form design is the discipline of asking for the absolute minimum at the exact right moment, using every available platform capability to reduce friction.

Luke Wroblewski's research established the foundational principle: mobile forms must respect the constraint of the small screen and the context of mobile use (interrupted, one-handed, distracted). Apply progressive disclosure aggressively — collect only what is necessary for the current step and defer everything else.

---

## Complete Mobile Form Design System

### Text Input Fields

**Single-line text input:**
- Use floating labels (Material Design pattern) or top-aligned labels. Floating labels transition from placeholder position to a small label above the field on focus, saving vertical space while maintaining context.
- Placeholder text is not a substitute for labels. Placeholders disappear on input, causing users to forget what the field requests.
- Provide clear error states: red border, error icon, and descriptive error message below the field. Never rely on color alone (accessibility).
- Success states (green checkmark) provide positive reinforcement during multi-field forms.
- Character counters appear below the field when a maximum length exists. Show "0/280" format.

**Multi-line text input (textarea):**
- Auto-expand the field height as the user types, up to a reasonable maximum (3-5 visible lines), then enable scrolling within the field.
- Show a character counter for length-limited inputs (comments, descriptions, bios).
- Place multi-line fields at the bottom of forms to prevent the expanded keyboard from obscuring other fields.

### Selection Fields

**Dropdown / Picker:**
- On iOS, use the native picker wheel or a menu-style picker for short lists (under 15 items). For longer lists, use a searchable full-screen selector.
- On Android, use an exposed dropdown menu (Material 3) for moderate lists or a full-screen dialog with search for long lists.
- Never use a raw HTML `<select>` element on mobile web without testing — native rendering varies dramatically across browsers and OS versions.

**Radio buttons / Single select:**
- Display all options visibly when there are 2-5 choices. Avoid hiding options inside a dropdown when screen space allows displaying them.
- Use radio buttons (Material) or a selection list with checkmarks (iOS) for mutually exclusive choices within a visible group.

**Checkboxes / Multi-select:**
- Use checkboxes for independent boolean choices. Group related checkboxes under a section header.
- On iOS, use toggle switches for individual on/off settings. Reserve checkboxes for multi-select lists.
- On Android, checkboxes and switches serve distinct roles: checkboxes for selection from a set, switches for toggling a state.

**Toggle / Switch:**
- Use for binary settings with immediate effect (no "Save" button needed). The toggle itself is the commit action.
- Place the label to the left and the toggle to the right, aligned to the trailing edge of the container.
- Provide clear on/off visual states. Do not rely on position alone — include color change and, on iOS, the "I/O" markings inside the switch track.

**Slider:**
- Use for continuous ranges where precise values are less important than relative positioning (volume, brightness, price range).
- Always show the current value. Display min and max labels at the ends.
- Provide an alternative text input for scenarios where a precise value is needed (price filter: slider + text field).

**Stepper / Quantity selector:**
- Minus and plus buttons flanking a numeric value. Use for small integer ranges (1-20).
- Disable the minus button at minimum value and the plus button at maximum value. Provide haptic feedback on each tap.

### Date and Time Fields

- Never require manual text entry for dates. Always use the platform date picker.
- iOS: compact date picker (tap to expand calendar), wheel picker for time selection.
- Android: Material date picker (calendar grid with month navigation), Material time picker (clock face or text input).
- For date ranges (check-in/check-out, start/end), use a range picker component that enforces logical constraints (end date must be after start date).
- Display the selected date in the user's locale format. Never hardcode MM/DD/YYYY — respect regional conventions.

---

## Input Types and Keyboard Optimization

Specifying the correct input type is one of the highest-impact, lowest-effort optimizations available. The right keyboard reduces errors and increases speed.

**Email:**
- HTML: `<input type="email" autocomplete="email" inputmode="email">`
- Shows a keyboard with `@` and `.` readily accessible. Disables autocapitalize on the first character.
- Validate with a permissive regex on the client and a verification email on the server. Do not reject valid email formats with overly strict patterns.

**Phone number:**
- HTML: `<input type="tel" autocomplete="tel" inputmode="tel">`
- Shows the numeric phone keypad. Include a country code selector with auto-detection from the device locale.
- Use `libphonenumber` (or equivalent) for validation and formatting. Format as the user types with appropriate grouping for their region.

**Number:**
- HTML: `<input inputmode="numeric" pattern="[0-9]*">` (prefer `inputmode="numeric"` over `type="number"` to avoid browser-specific spinner controls and accessibility issues).
- For decimal numbers: `inputmode="decimal"` shows a numeric keypad with a decimal point.

**Date:**
- HTML: `<input type="date">` invokes the native date picker on mobile browsers. This is often sufficient for mobile web.
- For greater control, use a custom date picker component that still launches the native picker on mobile platforms.

**Password:**
- HTML: `<input type="password" autocomplete="current-password">` (for login) or `autocomplete="new-password"` (for registration).
- Include a visibility toggle button (eye icon). Default to hidden.
- For new passwords, show strength requirements as a checklist that updates in real time. Use green checkmarks for met requirements.

**Credit card number:**
- HTML: `<input inputmode="numeric" autocomplete="cc-number">`
- Format in groups of 4 as the user types. Detect card network (Visa, Mastercard, Amex) from the first digits and display the corresponding logo.
- Auto-advance to expiry field after the card number is complete.

**Address:**
- Use multiple fields: street address line 1, line 2 (optional, collapsed by default), city, state/province, postal code, country.
- `autocomplete` attributes: `address-line1`, `address-line2`, `address-level2` (city), `address-level1` (state), `postal-code`, `country`.
- Pre-fill country from device locale. Auto-suggest city/state from postal code where the postal system supports it.

---

## Autofill and Autocomplete Implementation

**HTML autocomplete attributes:**
- Use standard `autocomplete` values: `name`, `given-name`, `family-name`, `email`, `tel`, `organization`, `street-address`, `postal-code`, `country`, `cc-name`, `cc-number`, `cc-exp`, `cc-csc`, `username`, `current-password`, `new-password`, `one-time-code`.
- Group related fields inside a `<form>` element with a clear `action`. Autofill engines use form structure to identify field groups.
- Use `<label>` elements properly associated with inputs (via `for` attribute or nesting). Autofill systems use labels to identify field purposes.

**iOS Autofill:**
- iOS autofill reads `autocomplete` attributes and uses heuristics to fill fields from the Keychain, Contacts, and payment information.
- Password autofill integrates with the QuickType bar above the keyboard. Properly tagged password fields trigger the autofill suggestion.
- One-time code autofill: SMS codes are detected automatically and offered in the QuickType bar. Use `autocomplete="one-time-code"` to enable this.
- For native apps, use `textContentType` on UITextField: `.emailAddress`, `.telephoneNumber`, `.creditCardNumber`, `.oneTimeCode`, `.password`, `.newPassword`.

**Android Autofill:**
- Android Autofill Framework (API 26+) provides a system-level autofill service. Apps opt in by setting `importantForAutofill="yes"` on relevant views.
- Use `autofillHints` on EditText: `AUTOFILL_HINT_EMAIL_ADDRESS`, `AUTOFILL_HINT_USERNAME`, `AUTOFILL_HINT_PASSWORD`, `AUTOFILL_HINT_CREDIT_CARD_NUMBER`, etc.
- For Jetpack Compose, use `Modifier.autofill()` with the appropriate autofill types.
- Third-party password managers (1Password, Bitwarden, etc.) integrate via the Autofill Framework — proper hint annotations ensure compatibility.

---

## Multi-Step Form Wizard Patterns

### When to Use Multi-Step Forms

- Total form fields exceed 7-8 items — chunking into steps reduces cognitive load.
- The form collects logically distinct categories of information (personal info, payment, confirmation).
- Earlier steps influence later steps (conditional logic based on selections).
- The form requires a review/confirmation step before submission.

### Progress Indicators

**Step indicators (numbered dots or labels):**
- Show the current step, total steps, and allow navigation to completed previous steps.
- Horizontal stepper at the top of the form area. Label each step concisely ("Account," "Address," "Payment," "Review").
- On mobile, abbreviated step labels or numbered dots work better than full labels when space is constrained.

**Progress bar:**
- A continuous bar showing percentage completion. Better for forms where the number of steps is variable or less meaningful.
- Combine with a text label: "Step 2 of 4" or "50% complete."

### Step Transition Design

- Animate step transitions with a horizontal slide (forward for next, backward for previous) to reinforce linear progression.
- Preserve all entered data when navigating backward. Never lose user input on back navigation.
- Validate the current step before allowing progression. Disable the "Next" button until all required fields in the current step are valid, or validate on tap and scroll to the first error.
- Provide a "Save and continue later" option for long forms. Use local storage or server-side draft persistence.

### Summary and Confirmation

- The final step displays a read-only summary of all entered information, organized by step.
- Each section includes an "Edit" link that navigates directly to the corresponding step.
- The primary action button changes to "Submit" / "Place Order" / "Confirm" on the final step.

---

## Address Input Patterns

**Autocomplete with Google Places / Mapbox / Apple Maps:**
- A single text field with predictive suggestions from a geocoding API dramatically reduces input effort and errors.
- As the user types, display a dropdown of matching addresses. Selecting a suggestion auto-fills all address sub-fields.
- Fall back to manual entry fields if the user's address is not found in the autocomplete suggestions.

**Geolocation pre-fill:**
- Offer a "Use current location" button that requests location permission and reverse-geocodes the device location into an address.
- Display the detected address for user confirmation before proceeding. Never assume the device location is the user's desired address (delivery address may differ from current location).

**International formats:**
- Address field ordering varies by country (Japan: postal code first; UK: no state field; US: state + zip). Adapt the form dynamically based on the selected country.
- Postal code format and validation differ globally. Use locale-aware validation libraries.
- Support non-Latin scripts. Test with RTL (right-to-left) addresses for Arabic and Hebrew locales.

---

## Payment Form Design

**Credit/Debit Card:**
- Display a single form with: card number, expiry date (MM/YY), CVC/CVV, and cardholder name (optional if billing address is collected).
- Show card network detection (Visa, Mastercard, Amex, Discover) dynamically as the user enters the card number. Display the appropriate card logo.
- Format the card number in groups of 4 (Amex: 4-6-5) as the user types using an input mask.
- The CVC field should show a card illustration indicating where the code is located (back of card, or front for Amex).
- Security indicators (lock icon, "Secure payment" text, PCI compliance badge) reduce anxiety.

**Digital Wallets:**
- Apple Pay, Google Pay, and Samsung Pay should be the primary payment option, displayed above the manual card entry form.
- A single tap on the wallet button authenticates with biometrics and completes payment. This eliminates the entire card entry form.
- Display the wallet button using the official branding guidelines from each platform. Apple and Google have strict requirements for button styling, sizing, and placement.
- Fall back to card entry only if the wallet is not available or the user explicitly requests it.

**Buy Now, Pay Later (BNPL):**
- Present BNPL options (Klarna, Affirm, Afterpay) alongside traditional payment methods.
- Clearly display the payment schedule (4 installments of $X, no interest) before the user commits.
- BNPL flows typically redirect to the provider's app or embedded WebView for approval. Design a seamless return flow to the app after approval or rejection.
- Show eligibility status early in the checkout process. Do not present BNPL as an option only to reject the user at the final step.

---

## Authentication Flows

### Login

- Email/username + password is the baseline. Place biometric/wallet login above the form as the primary option.
- Show the password field on the same screen as the email field (single-screen login) for simplicity. Two-step login (email first, then password) is appropriate only when different authentication methods depend on the email domain (SSO detection).
- Social login options (Sign in with Apple, Sign in with Google) appear below the primary login method. Use platform-standard button styling.
- "Remember me" toggle and "Forgot password?" link sit below the password field.

### Registration / Sign Up

- Minimize fields: email + password is the minimum viable registration. Collect name, phone, and other details after the account exists.
- Password strength indicator updates in real time. Show requirements as a checklist, marking each as met or unmet.
- Inline validation on blur for email (format check + availability check via API).
- Offer social registration (Sign in with Apple, Google) as an alternative that eliminates the form entirely.

### Password Reset

- Single field: email address. Display a confirmation message regardless of whether the email exists in the system (security best practice: do not confirm or deny email existence).
- The reset link opens the app directly via deep link / universal link and presents a new password form.
- New password form: new password field + confirmation field (or a single field with visibility toggle to reduce errors).
- Auto-log in the user after successful password reset. Do not force them to go through the login form again.

### Two-Factor Authentication (2FA)

- Present a 6-digit code entry field that auto-advances between digits (or a single field with `autocomplete="one-time-code"` that captures SMS autofill).
- Support TOTP (authenticator app), SMS, and email as 2FA methods. Allow the user to choose their preferred method.
- Countdown timer shows when a new code can be requested. "Resend code" link activates after the timer expires.
- Backup codes / recovery methods must be accessible for account recovery when the 2FA device is unavailable.

### Biometric Authentication

- Face ID (iOS), Touch ID (iOS), fingerprint (Android), and face unlock (Android) should be offered as the primary authentication method for returning users.
- The biometric prompt is system-managed. Design the app to request biometric authentication immediately on launch or when accessing sensitive features.
- Provide a fallback to passcode/password if biometric authentication fails (wet fingers, face coverings, changed appearance).
- Store authentication tokens in the platform's secure enclave (iOS Keychain, Android Keystore). Never store passwords locally.

### Passkeys (FIDO2 / WebAuthn)

- Passkeys replace passwords entirely. The user authenticates with biometrics (Face ID, fingerprint) or a device PIN, and a cryptographic credential handles the authentication.
- On registration, offer "Create a passkey" as the primary option. The system dialog handles key generation and storage.
- On login, the passkey prompt appears automatically if a credential exists for the domain. The user authenticates with a single biometric scan.
- Cross-device authentication allows signing in on a new device by scanning a QR code with the device that holds the passkey.
- Implement the Web Authentication API (WebAuthn) for mobile web or platform-specific APIs for native apps (AuthenticationServices on iOS, FIDO2 API on Android).

---

## Mobile Navigation Architecture

### Flat Navigation

- All primary destinations are accessible from a single navigation level (tab bar or bottom navigation).
- Best for apps with 3-5 coequal sections where no single section dominates (social apps, utility apps).
- Users can switch between sections without traversing a hierarchy.

### Hierarchical Navigation

- A tree structure where users drill down from general to specific: category > subcategory > item > detail.
- Best for content-heavy apps (e-commerce, news, file management).
- Maintain a clear breadcrumb trail via the navigation bar back button. Show the parent title as the back label (iOS) or a back arrow (Android).

### Hub-and-Spoke

- A central hub screen (home/dashboard) connects to independent spoke experiences. Each spoke completes a task and returns the user to the hub.
- Best for apps with distinct, self-contained workflows (banking: check balance, transfer, pay bills).
- The hub should surface summary information from each spoke so users can assess status without entering each one.

### Choosing the Right Architecture

- Map the information architecture before choosing the navigation structure. Card sorting and tree testing with users validate the hierarchy.
- Most apps combine patterns: a flat tab bar for top-level navigation, hierarchical navigation within each tab, and hub-and-spoke for task-oriented sections.
- Keep the total navigation depth under 4 levels. If deeper, restructure the IA or provide cross-cutting shortcuts (search, deep links).

---

## Tab Bar Design

### Icon and Label Requirements

- Always pair icons with labels. Both Nielsen Norman Group and Baymard Institute testing find that unlabeled icons are inconsistently interpreted: users do not agree on what abstract icons mean, and icon-only controls also degrade screen reader access. Text labels resolve both problems.
- Use filled icons for the active state and outlined icons for inactive states (Material 3 convention). iOS uses filled/outline distinction within SF Symbols.
- Labels should be a single word (two words maximum). Truncation with ellipsis is never acceptable for navigation labels.

### Badge Indicators

- Numeric badges indicate a specific count (unread messages: "3"). Display the number directly on the tab icon.
- Dot badges indicate the presence of new content without specifying a count. Use when the exact number is less important than the presence of something new.
- Cap numeric badges at a reasonable maximum ("99+") to prevent display issues.
- Clear badges when the user visits the corresponding tab and views the new content.

### State Management

- Each tab maintains its own scroll position and navigation state. Switching between tabs should not reset the user's position.
- Tapping the currently active tab scrolls to the top and pops to the root view (iOS convention). Implement this on Android for consistency.
- Preserve tab state across app backgrounding and resuming. Users expect to return exactly where they left.

---

## Hamburger Menu vs Tab Bar

### Research Findings on Discoverability

- Nielsen Norman Group's quantitative study (179 participants, six sites) found that hiding navigation cuts content discoverability by nearly half, increases time on task, and raises perceived task difficulty, on both mobile and desktop.
- The hamburger icon is recognized as a menu trigger, but users must make a conscious decision to open it — many do not.
- Visible navigation (tab bar, bottom navigation) makes destinations discoverable at a glance. Users explore more sections and complete more tasks.

### When the Hamburger Menu is Appropriate

- When there are more than 5 top-level destinations and a tab bar cannot accommodate them all.
- For infrequently accessed secondary navigation (settings, help, about, legal).
- For authenticated/role-based navigation where the menu items change significantly by user state.
- On tablets and larger screens where a persistent navigation drawer (always-visible sidebar) replaces the hamburger.

### The Recommended Approach

- Use a bottom tab bar or bottom navigation for the 4-5 most important destinations.
- Place less important items in a "More" tab (iOS) or navigation drawer (Android) accessible from the tab bar.
- Never hide the most important navigation items. The hamburger menu is a supplement, not a replacement for visible navigation.

---

## Search-Driven Navigation

### When Search Becomes Primary Navigation

- Content-heavy apps with large catalogs (e-commerce, media streaming, reference apps) benefit from search-first navigation.
- The search field occupies a prominent position: a persistent search bar at the top or the first element in the home screen.

### Search Experience Design

- Display recent searches immediately on search activation. Show 5-10 recent queries.
- Provide autocomplete suggestions as the user types. Suggestions can include query completions, category shortcuts, and specific items.
- Show trending or popular searches for new or undecided users.
- Support voice input with a microphone icon in the search field. This is especially valuable for hands-busy contexts.
- Search results must load progressively. Show skeleton content while results are fetched. Never display an empty screen during the search.

### Filtered and Faceted Search

- Filters appear as horizontally scrollable chips below the search field. Active filters display prominently.
- Full filter panels open as a bottom sheet or full-screen overlay for complex filtering (price range, category, rating, color, size).
- Show the result count that will be returned for each filter option before the user applies it.
- Provide a "Clear all filters" action and the ability to remove individual filters by tapping their chip.

---

## Pull-to-Refresh

### Implementation

- The pull-to-refresh gesture is now universally understood on mobile. A downward pull on a scrollable list triggers a content refresh.
- Display a loading indicator (spinner) that appears as the user pulls down. The indicator should animate proportionally to the pull distance before triggering.
- Provide haptic feedback at the trigger threshold (the point where releasing will initiate the refresh).
- The refresh should complete within 2-3 seconds. For longer operations, transition to a progress indicator or background refresh notification.

### Alternatives and Supplements

- Auto-refresh on return: refresh content when the user returns to the screen after a set time interval.
- Real-time updates via WebSocket or push notifications eliminate the need for manual refresh entirely.
- A "New content available" banner at the top of the list allows users to tap to load new items without resetting their scroll position.

---

## Infinite Scroll vs Pagination

### Infinite Scroll

- Content loads automatically as the user scrolls near the bottom. Eliminates the friction of tapping "Next page."
- Ideal for feed-based content (social media, news, image galleries) where there is no logical endpoint.
- Show a loading indicator at the bottom of the list during content fetch. Skeleton rows maintain visual continuity.
- Preserve scroll position on back navigation. Losing position in an infinite list is the most common usability complaint with this pattern.
- Provide a "Back to top" floating button that appears after the user has scrolled significantly.

### Pagination

- Content loads in discrete pages with explicit "Load more" or numbered page controls.
- Prefer "Load more" button over traditional numbered pagination on mobile. Numbered pagination requires precise tap targets and adds complexity.
- Appropriate when the total number of results matters (search results: "Showing 1-20 of 342"), when the user needs to reference specific items by position, or when content is not time-ordered.
- Combine with infinite scroll by loading the next page automatically but providing a page indicator for orientation.

### Hybrid Approach

- Load the first 2-3 pages automatically (infinite scroll behavior), then show a "Load more" button. This prevents accidental over-scrolling and runaway data consumption.
- Display a count of remaining items: "Load 20 more (302 remaining)."

---

## Bottom Sheet as Navigation and Action Container

### Navigation Bottom Sheets

- Bottom sheets serve as secondary navigation layers. A map application shows a half-height bottom sheet with location details while the map remains visible above.
- The sheet has discrete states: collapsed (peek height showing a summary), half-expanded (showing details), and expanded (full content).
- Content in the bottom sheet scrolls within the expanded state. Scrolling up beyond the content collapses the sheet.

### Action Bottom Sheets

- Present contextual actions without leaving the current screen. The sheet contains a list of actions with icons and labels.
- Action sheets dismiss after an action is selected. Destructive actions should require a confirmation step.
- Group actions into sections with dividers or headers. Place the most common action first.

### Design Rules for Bottom Sheets

- Include a drag handle at the top for clear affordance.
- Limit peek height content to 1-2 lines of essential information. The user should understand the context at a glance.
- Respect safe areas at the bottom (home indicator on iOS, gesture nav bar on Android).
- Animate state transitions smoothly. Match the platform's standard sheet animation curve and duration.

---

## Deep Linking and Universal Links

### iOS Universal Links

- Universal links use the app's associated domain to open specific content directly in the app. If the app is not installed, the link falls back to Safari.
- Configure the `apple-app-site-association` (AASA) file on the web server to define which URL paths the app handles.
- Inside the app, handle the incoming URL in `application(_:continue:restorationHandler:)` and navigate to the correct content.
- Construct the correct navigation stack so back navigation from a deep-linked destination makes sense (the user should not be stranded with no back button).

### Android App Links

- App Links are verified deep links that open directly in the app without a disambiguation dialog. Verification requires a `assetlinks.json` file on the web server.
- Handle incoming intents in the target Activity. Parse the URI to determine the destination and navigate accordingly.
- Use the Navigation component's deep link support to automatically construct the correct back stack.
- Test deep links thoroughly: with the app installed, not installed (fallback to Play Store or web), and from various entry points (notifications, messages, QR codes, email).

### Navigation Stack Construction

- A deep link into a detail screen must build the intermediate navigation stack: Home > Category > Subcategory > Item Detail. The back button should walk up this constructed stack, not exit the app immediately.
- On iOS, push the full stack onto the navigation controller. On Android, use `NavDeepLinkBuilder` or TaskStackBuilder to construct the synthetic back stack.
- Handle invalid or expired deep links gracefully: display an error message and navigate to the closest valid parent destination.

---

## Mobile-Specific Accessibility

### VoiceOver (iOS) Gestures and Patterns

- VoiceOver reads each focusable element aloud as the user swipes right (next element) or left (previous element).
- Group related elements using `accessibilityElements` ordering or `isAccessibilityElement = false` on containers to present a logical reading order.
- Custom actions reduce swipe fatigue: instead of making every button individually focusable, add custom actions to the parent element (e.g., a list row with "Delete" and "Archive" as custom actions accessed via swipe up/down).
- Every image must have an `accessibilityLabel`. Decorative images set `isAccessibilityElement = false`.
- Form fields must associate labels with inputs. VoiceOver reads the label when the field receives focus.
- Modal presentations must trap focus within the modal. VoiceOver should not be able to navigate to background content while a sheet or alert is presented.

### TalkBack (Android) Navigation

- TalkBack navigation mirrors VoiceOver: swipe right/left to move between elements, double-tap to activate.
- Use `contentDescription` on all meaningful non-text elements. Set `importantForAccessibility="no"` on decorative elements.
- Android's accessibility heading hierarchy supports `accessibilityHeading = true` on section headers, enabling TalkBack users to navigate between headings (swipe up/down with heading navigation mode).
- Live regions (`accessibilityLiveRegion`) announce dynamic content changes (loading states, error messages, counters) without requiring the user to navigate to the changed element.
- Ensure touch targets meet the 48x48dp minimum. TalkBack exposes elements smaller than this threshold with a warning.

### Switch Access and Alternative Input

- Switch access allows users with motor impairments to navigate using one or two physical switches (or on-screen switches).
- Every interactive element must be focusable and activatable without requiring precise touch gestures. Swipe gestures, long press, and multi-finger gestures are inaccessible to switch users.
- Provide alternatives for all gesture-based interactions: swipe-to-delete must have a visible delete button or an accessible action.
- Focus order must be logical and predictable. Switch users traverse elements sequentially — an illogical order makes navigation painfully slow.

### General Mobile Accessibility Requirements

**Text and typography:**
- Support Dynamic Type (iOS) and system font scaling (Android) on all text. Test at the largest text size to ensure layouts accommodate without truncation or overlap.
- Minimum contrast ratio: 4.5:1 for body text, 3:1 for large text (18pt or 14pt bold). Use platform tools to verify contrast under dynamic theming conditions.
- Avoid conveying meaning through color alone. Pair color with icons, text, or patterns.

**Motion and animation:**
- Respect `prefers-reduced-motion` (web) / `UIAccessibility.isReduceMotionEnabled` (iOS) / `Settings.Global.ANIMATOR_DURATION_SCALE` (Android). Disable non-essential animations when these settings are active.
- Essential animations (page transitions, loading indicators) can remain but should be simplified.
- Parallax effects, auto-playing carousels, and flashing content must be disabled or reducible.

**Touch and interaction:**
- Ensure all interactive elements have touch targets of at least 44x44pt (iOS) / 48x48dp (Android).
- Provide visible focus indicators for keyboard and switch access navigation.
- Time-limited interactions (auto-dismissing toasts, disappearing buttons) must either extend their duration or offer manual control. WCAG 2.2 requires that users can extend or disable time limits.
- Drag-and-drop interfaces must provide an accessible alternative (move-to button, sort menu).

**Testing protocol:**
- Test every screen with VoiceOver (iOS) and TalkBack (Android) at minimum. Navigate the entire user flow using only the screen reader.
- Test with the largest system text size enabled on both platforms.
- Test with switch access on at least one platform.
- Use the Accessibility Inspector (Xcode) and Layout Inspector (Android Studio) to audit focus order, labels, and contrast.
- Automated tools (axe for mobile web, Accessibility Scanner for Android) catch common issues but do not replace manual screen reader testing.

---

## Cross-Referencing

- For platform-specific component differences, reference `ios-android-patterns.md` in this skill's references.
- For visual design and typography systems, reference `ui-visual-design-system`.
- For motion and transition design, reference `interaction-motion-design`.
- For comprehensive accessibility guidance, reference `accessibility-inclusive-design`.
- For design system component architecture, reference `design-systems-architecture`.

---

## Key Sources

- Wroblewski, L. (2011). "Mobile First"
- Wroblewski, L. (2008). "Web Form Design: Filling in the Blanks"
- Baymard Institute — Mobile Form Usability research (ongoing)
- Apple Human Interface Guidelines — Forms, Navigation, Accessibility (2025)
- Google Material Design 3 — Text Fields, Navigation, Accessibility (2025)
- W3C — Web Content Accessibility Guidelines (WCAG) 2.2
- FIDO Alliance — Passkey implementation guidelines
- NNG Group — Mobile Navigation, Hamburger Menu, Search Pattern studies
- Hoober, S. (2017). "Design for Fingers, Touch, and People"
