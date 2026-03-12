---
name: Screen & Flow Patterns
description: "Comprehensive taxonomy of 25+ screen types, 15+ user flow patterns, and 25+ UI element deep-dives. Mobbin-style categorization with layout patterns, component hierarchies, state matrices, accessibility requirements, and best-in-class references for every screen, flow, and element type. Use when the user mentions: screen type, screen pattern, user flow, flow pattern, login screen, signup screen, checkout flow, onboarding flow, dashboard screen, search screen, product page, settings screen, empty state, error screen, screen builder, flow builder."
---

# Screen & Flow Patterns — The Complete Taxonomy

## Why Screen & Flow Patterns Matter

Every screen type in a digital product has established patterns that users have internalized through years of interaction with hundreds of apps and websites. When a login screen places the password field above the email field, or a checkout flow asks for shipping info after payment, users experience friction not because the interface is broken, but because it violates their learned expectations. These patterns are not arbitrary conventions — they are the result of decades of iterative refinement across billions of user interactions, A/B tests, and usability studies conducted by teams at companies like Apple, Google, Shopify, Stripe, and Airbnb.

Knowing the canonical patterns for each screen type is not about copying — it is about having a baseline of "what good looks like" so that every deviation is intentional and justified. A designer who knows that the standard checkout flow is 3-5 steps with a progress indicator, address before payment, and an order summary sidebar can make an informed decision to deviate (say, a single-page checkout for digital products). A designer who does not know the pattern is guessing. The difference between innovation and ignorance is whether you know the rule you are breaking.

This skill provides a complete taxonomy: 32 screen types with layout patterns and component hierarchies, 22 user flow patterns with step sequences and branching logic, 120+ UI element deep-dives with anatomy, states, and accessibility requirements, flow diagram conventions, screen-to-screen transition models, state machines for every screen, information density guidance, and platform-specific conventions across iOS, Android, and Web.

## Coverage

- **32 screen types** with layout patterns, component hierarchies, state matrices, and accessibility requirements
- **22 user flow patterns** with step sequences, decision points, error handling, emotional arcs, and metric benchmarks
- **120+ UI element patterns** organized by function (navigation, input, display, feedback, overlay, layout)
- **6 screen-to-screen transition types** with platform-specific implementation guidance
- **5-state screen state machine** with transitions and triggers
- **3-tier information density model** per screen type
- **Platform-specific conventions** for iOS, Android, and Web
- **Curated inspiration source guide** with lookup table for 20+ common design needs

## Reference Architecture

| File | Contents | Lines |
|------|----------|-------|
| `references/screen-type-catalog.md` | 32 screen types with UX patterns, layout specs, component lists, state matrices | 800-1000+ |
| `references/user-flow-catalog.md` | 22 user flows with step sequences, branching, error handling, metrics | 700-900+ |
| `references/ui-element-deep-dive.md` | 120+ UI elements with anatomy, variants, states, accessibility | 800-1000+ |
| `references/inspiration-reference-guide.md` | Curated sources, lookup table, how to study references | 200-300 |

---

## Section 1: Screen Type Taxonomy (32 Types)

Each screen type includes: purpose, key components, canonical layout pattern, common user flows in and out, information density level, and platform variations.

### 1.1 Landing Page
- **Purpose**: Convert visitors into users or customers. First impression. Single call to action.
- **Key Components**: Hero section (headline + subhead + CTA), social proof strip, feature grid (3-4 cards), testimonials carousel, pricing teaser, final CTA block, footer.
- **Layout Pattern**: Single-column stack. Hero is full-viewport or near-full. Content alternates left-right sections. Sticky CTA on mobile.
- **Flows In**: Direct URL, ad click, search engine result, social media link, email campaign.
- **Flows Out**: Sign-up, pricing page, product tour, demo request, app store redirect.
- **Density**: Low. Generous whitespace. One idea per viewport fold.
- **Platform Notes**: Web-primary. Mobile landing pages must load under 2.5s (Core Web Vitals). iOS/Android deep links should route to equivalent native onboarding if app installed.

### 1.2 Home / Dashboard
- **Purpose**: Orient the user. Show personalized content, key metrics, recent activity, and shortcuts to primary actions.
- **Key Components**: Greeting/header, key metric cards (KPIs), recent activity feed, quick action buttons, navigation to all major sections, notification badge.
- **Layout Pattern**: Grid of cards on desktop (2-3 columns). Single-column scrolling feed on mobile. Optional sidebar for navigation on desktop. Top-level tabs or segmented control for content categories.
- **Flows In**: Login, app launch, back from any section, notification tap, deep link.
- **Flows Out**: Any primary feature, settings, notifications, profile, search.
- **Density**: Medium-High. Dashboards are information-dense by nature but must prioritize hierarchy.
- **Platform Notes**: iOS uses large title collapsing on scroll. Android uses top app bar with optional bottom nav. Web dashboards commonly use persistent left sidebar.

### 1.3 List / Feed
- **Purpose**: Browse, scan, and select from a collection of items. Supports filtering, sorting, and pagination.
- **Key Components**: List header with count, sort/filter controls, list items (thumbnail + title + metadata + action), pull-to-refresh, infinite scroll or pagination, empty state, skeleton loading.
- **Layout Pattern**: Vertical list (mobile), grid or table (desktop). Filter panel as sidebar (desktop) or bottom sheet (mobile). Sticky header with active filter chips.
- **Flows In**: Navigation tab, search results, dashboard shortcut, back from detail.
- **Flows Out**: Detail/show page, create new item, filter/sort modal, bulk actions.
- **Density**: High. Each list item is a compressed information unit. Scanability is paramount.
- **Platform Notes**: iOS uses grouped/inset list style with swipe actions. Android uses RecyclerView patterns. Web supports both list and grid toggle views.

### 1.4 Detail / Show
- **Purpose**: Present complete information about a single item. Allow primary actions on that item.
- **Key Components**: Hero image/media, title + metadata, description/body content, action buttons (primary + secondary), related items, share/bookmark, back navigation.
- **Layout Pattern**: Top media area, scrolling content below. Sticky bottom action bar on mobile. Side panel for metadata on desktop. Tabs for sections if content is deep.
- **Flows In**: List item tap, search result, deep link, notification, related item.
- **Flows Out**: Back to list, edit, delete, share, related detail, external link.
- **Density**: Medium. Balance completeness with scannability. Progressive disclosure for secondary info.
- **Platform Notes**: iOS uses large title with hero image parallax. Android uses collapsing toolbar layout. Web uses breadcrumb trail for context.

### 1.5 Profile
- **Purpose**: Display user identity, activity history, and settings access. Can be own profile or another user's.
- **Key Components**: Avatar, display name, bio/tagline, stats row (followers, posts, etc.), action buttons (edit profile / follow / message), content tabs (posts, media, likes), settings gear icon.
- **Layout Pattern**: Header card with avatar and stats, horizontal tabs below, scrolling content per tab. Sticky header on scroll (avatar shrinks).
- **Flows In**: Navigation tab, user mention tap, search result, follower list.
- **Flows Out**: Edit profile, settings, follower/following list, content detail, message.
- **Density**: Medium. Header is compact; tab content varies.
- **Platform Notes**: All platforms follow the header-tabs-content pattern. iOS uses segmented control. Android uses TabLayout. Web uses horizontal tab bar.

### 1.6 Settings
- **Purpose**: Let users configure their experience. Account, preferences, notifications, privacy, about.
- **Key Components**: Grouped sections with headers, toggle switches, drill-down rows (chevron indicator), destructive actions at bottom (delete account, log out), version info footer.
- **Layout Pattern**: Grouped table/list view. Single column. Each row is a key-value pair or toggle. Drill-down for complex settings. Search bar at top for large settings surfaces.
- **Flows In**: Profile page, gear icon, navigation menu, system prompt (e.g., notification permission).
- **Flows Out**: Sub-setting pages, external links (privacy policy, terms), logout, delete account confirmation.
- **Density**: Low-Medium. Clean rows. No clutter.
- **Platform Notes**: iOS uses UITableView grouped style. Android uses PreferenceScreen. Web uses tabbed settings panels or vertical nav.

### 1.7 Search / Results
- **Purpose**: Help users find specific content. Includes search input, suggestions, and results display.
- **Key Components**: Search bar (prominent), recent searches, trending/suggested searches, results list with relevance ranking, filter chips, no-results state, voice search button.
- **Layout Pattern**: Three states: empty (recent + trending), typing (autocomplete suggestions), results (filtered list/grid). Filters as horizontal chips or sidebar.
- **Flows In**: Search icon tap, spotlight/universal search, command palette (desktop).
- **Flows Out**: Detail page, filter refinement, clear and retry, back to previous screen.
- **Density**: Variable. Empty state is low. Results state is high.
- **Platform Notes**: iOS uses UISearchController with scope bar. Android uses SearchView in toolbar. Web uses dedicated search page or inline expandable search.

### 1.8 Checkout
- **Purpose**: Complete a purchase transaction. Minimize friction while collecting necessary information.
- **Key Components**: Order summary (items, quantities, prices), shipping address form, payment method selector, promo code input, tax/fee breakdown, place order CTA, trust signals (security badges, return policy).
- **Layout Pattern**: Multi-step wizard (3-5 steps) with progress indicator, or single-page with accordion sections. Order summary sidebar (desktop) or collapsible top section (mobile). Sticky CTA button.
- **Flows In**: Cart, buy-now button, pricing page selection.
- **Flows Out**: Confirmation/success page, back to cart, payment failure error, abandon (exit intent modal).
- **Density**: Medium. Show only what is needed per step. Progressive disclosure.
- **Platform Notes**: Web uses full-page checkout. iOS/Android use Apple Pay / Google Pay for express checkout. Native apps should support biometric payment confirmation.

### 1.9 Onboarding
- **Purpose**: Introduce new users to the product. Set up their account. Establish first value.
- **Key Components**: Welcome screen, value proposition slides (3-5 max), permission requests (notifications, location), account setup (avatar, preferences), progress dots, skip button, get-started CTA.
- **Layout Pattern**: Horizontal paged carousel with dots indicator. Full-screen each step. Final step transitions to home/dashboard. Optional vertical scrolling variant for complex setup.
- **Flows In**: First app launch, sign-up completion, invitation link.
- **Flows Out**: Home/dashboard, first key action (create first item), tutorial overlay.
- **Density**: Very Low. One concept per screen. Minimal text.
- **Platform Notes**: iOS uses UIPageViewController. Android uses ViewPager2. Web uses stepped modal or full-page carousel. All platforms: respect skip — onboarding should never trap users.

### 1.10 Login
- **Purpose**: Authenticate returning users. Fast re-entry to the product.
- **Key Components**: Email/username field, password field (with show/hide toggle), remember me checkbox, forgot password link, submit button, social login buttons (Google, Apple, GitHub), sign-up link, biometric login prompt.
- **Layout Pattern**: Centered card on desktop. Full-screen form on mobile. Logo at top. Fields stacked vertically. Social logins separated by "or" divider. Error messages inline.
- **Flows In**: App launch (session expired), logout, deep link to protected content, sign-up redirect.
- **Flows Out**: Home/dashboard, MFA challenge, forgot password, sign-up page.
- **Density**: Very Low. Single purpose. No distractions.
- **Platform Notes**: iOS supports Sign in with Apple (required if social login offered), passkeys, Face ID/Touch ID. Android supports Google One Tap, fingerprint. Web supports WebAuthn/passkeys.

### 1.11 Sign-up / Registration
- **Purpose**: Create a new account. Collect minimum viable information to activate the user.
- **Key Components**: Name field, email field, password field (with strength indicator), terms acceptance checkbox, create account CTA, social sign-up buttons, login redirect link.
- **Layout Pattern**: Similar to login. Centered card or full-screen. Minimal fields (email + password minimum). Social options prominent. Progressive profiling defers non-essential data to post-signup.
- **Flows In**: Landing page CTA, login page redirect, invitation link, pricing page selection.
- **Flows Out**: Email verification, onboarding, home/dashboard, plan selection.
- **Density**: Very Low. Reduce fields to reduce abandonment.
- **Platform Notes**: Same as login. Sign in with Apple required on iOS if any social option exists. Password autofill support on all platforms.

### 1.12 Forgot Password / Reset
- **Purpose**: Recover account access. Verify identity and set new password.
- **Key Components**: Email input, submit button, success message (check your email), reset link/code entry, new password fields, confirmation.
- **Layout Pattern**: Two-step: request (email form) then reset (new password form). Simple centered layout. Back to login link prominent.
- **Flows In**: Login page "forgot password" link.
- **Flows Out**: Login page (after reset), email app (to find reset link).
- **Density**: Minimal. Single input per step.

### 1.13 Error 404 (Not Found)
- **Purpose**: Inform user the requested page does not exist. Provide escape routes.
- **Key Components**: Error code/title, friendly explanation, illustration/graphic, search bar, link to home, link to sitemap or popular pages, report broken link option.
- **Layout Pattern**: Centered content. Single column. Illustration above text. 2-3 action links below.
- **Flows In**: Broken link, mistyped URL, deleted content, expired link.
- **Flows Out**: Home page, search, back button, suggested pages.
- **Density**: Minimal. The page itself is the message.

### 1.14 Error 500 (Server Error)
- **Purpose**: Inform user of a system failure. Reassure that the issue is being addressed.
- **Key Components**: Error title, apologetic message, illustration, retry button, status page link, support contact, auto-refresh timer (optional).
- **Layout Pattern**: Centered. Similar to 404 but with retry emphasis.
- **Flows In**: Any server failure during navigation or action.
- **Flows Out**: Retry (same page), home page, status page, support.
- **Density**: Minimal. Empathetic tone.

### 1.15 Maintenance Page
- **Purpose**: Inform user the service is temporarily down for maintenance. Set expectations for return.
- **Key Components**: Maintenance title, estimated return time, progress indicator (optional), subscribe for updates option, social media links.
- **Layout Pattern**: Centered. Single purpose. Often a static HTML page served from CDN.
- **Flows In**: Any URL during maintenance window.
- **Flows Out**: Auto-redirect to home when maintenance complete, subscribe confirmation.
- **Density**: Minimal.

### 1.16 Empty State
- **Purpose**: Guide user when a screen has no content yet. Motivate first action.
- **Key Components**: Illustration, headline, explanatory text, primary CTA (create first item / import data / invite team), optional secondary CTA.
- **Layout Pattern**: Centered vertically and horizontally in the content area. Illustration above text. CTA below. Should not look like a broken page.
- **Flows In**: First use of any list/collection/feed screen, after deleting all items, after clearing filters with no results.
- **Flows Out**: Create flow, import flow, tutorial, adjust filters.
- **Density**: Very Low. The emptiness is intentional.

### 1.17 Loading Screen / Splash
- **Purpose**: Bridge the gap while content loads. Maintain perceived performance.
- **Key Components**: Brand logo, progress indicator (determinate or indeterminate), skeleton screen, shimmer placeholders, loading tips (optional).
- **Layout Pattern**: Full-screen splash for app launch. Inline skeleton screens for content areas. Progress bar at top for page-level loading.
- **Flows In**: App launch, heavy content fetch, file upload/processing.
- **Flows Out**: Loaded content screen. Error screen if load fails.
- **Density**: None. Pure transition.
- **Platform Notes**: iOS requires a launch storyboard matching initial UI. Android uses splash screen API (Android 12+). Web uses skeleton screens (avoid full-page spinners).

### 1.18 Notifications Center
- **Purpose**: Aggregate all notifications. Allow users to review, act on, and manage alerts.
- **Key Components**: Notification list (grouped by time: today, earlier, this week), read/unread indicators, action buttons per notification, mark all read, notification preferences link, empty state.
- **Layout Pattern**: Full-screen list on mobile. Dropdown panel on desktop. Grouped by time. Swipe to dismiss on mobile. Click to navigate to relevant screen.
- **Flows In**: Bell icon tap, push notification tap, badge indicator.
- **Flows Out**: Relevant detail screen per notification, notification settings, mark as read.
- **Density**: Medium-High. Dense list but clear hierarchy.

### 1.19 Chat / Messaging
- **Purpose**: Real-time or async communication between users. Support text, media, and reactions.
- **Key Components**: Conversation list, message thread (bubbles), input bar (text field + send + attachments), typing indicator, read receipts, message status (sent/delivered/read), user presence indicator.
- **Layout Pattern**: Split view on desktop (list left, thread right). Full-screen thread on mobile with back to list. Messages anchored to bottom. Input bar sticky at bottom. Auto-scroll to newest.
- **Flows In**: Contact list, notification tap, user profile message button, deep link.
- **Flows Out**: User profile, shared content detail, file preview, call initiation.
- **Density**: High in thread. Medium in list.
- **Platform Notes**: iOS uses MessageKit patterns. Android uses conversation notifications. Web uses WebSocket for real-time updates.

### 1.20 Calendar
- **Purpose**: Display and manage time-based content. Events, schedules, availability.
- **Key Components**: Month/week/day view toggle, date grid, event indicators (dots or blocks), event detail popup, create event button, today button, navigation arrows (prev/next month).
- **Layout Pattern**: Grid-based for month view. Timeline (vertical hours) for day/week view. Side panel for event details on desktop. Bottom sheet or full screen for event detail on mobile.
- **Flows In**: Navigation tab, notification about upcoming event, deep link to specific date.
- **Flows Out**: Event detail, create event, edit event, related contact/project.
- **Density**: High. Calendars are inherently data-dense.
- **Platform Notes**: iOS uses EventKit integration. Android uses CalendarProvider. Web implementations vary (FullCalendar, custom).

### 1.21 Map View
- **Purpose**: Display location-based content. Search, browse, and interact with geospatial data.
- **Key Components**: Map canvas, location pins/markers, search bar overlay, current location button, zoom controls, bottom sheet with list view, cluster indicators, filter chips.
- **Layout Pattern**: Full-screen map with overlaid controls. Bottom sheet pulls up for list/detail. Search bar at top with filter chips below. Floating action buttons for current location and zoom.
- **Flows In**: Navigation tab, location-based search, address tap, directions request.
- **Flows Out**: Location detail, directions/navigation, list view toggle, filter adjustment.
- **Density**: Variable. Map itself is high density. Overlaid UI should be minimal.
- **Platform Notes**: iOS uses MapKit or Google Maps SDK. Android uses Google Maps SDK. Web uses Mapbox GL, Google Maps JS, or Leaflet.

### 1.22 Analytics / Reporting
- **Purpose**: Visualize data trends, KPIs, and business metrics. Support decision-making.
- **Key Components**: Date range picker, KPI summary cards, charts (line, bar, pie, area), data tables, export button, comparison toggles (vs previous period), filter controls.
- **Layout Pattern**: Top: date range + filters. Below: KPI cards row. Below: charts in grid (2-column desktop, stacked mobile). Below: detailed data table. Sticky header with controls.
- **Flows In**: Dashboard shortcut, navigation menu, report notification, scheduled report link.
- **Flows Out**: Drill-down detail, export/download, share report, configure dashboard.
- **Density**: Very High. Analytics screens are the densest screen type. Requires excellent visual hierarchy to avoid overwhelm.

### 1.23 File Manager
- **Purpose**: Browse, organize, and manage files and folders. Upload, download, move, share.
- **Key Components**: Folder tree (sidebar), file grid/list toggle, breadcrumb path, upload button, search, sort/filter, file preview, multi-select + bulk actions, context menu (right-click).
- **Layout Pattern**: Three-panel on desktop (tree + list + preview). Single list on mobile with drill-down navigation. Toolbar at top with view controls. Drag-and-drop support.
- **Flows In**: Navigation menu, file link, upload completion notification, share link.
- **Flows Out**: File preview/editor, share dialog, download, move/copy dialog.
- **Density**: High. Many items, nested structure.

### 1.24 Editor / Canvas
- **Purpose**: Create or edit content. Text editor, image editor, diagram tool, code editor.
- **Key Components**: Canvas/workspace area (maximized), toolbar (contextual tools), properties panel (sidebar), layers panel, zoom controls, undo/redo, save indicator, collaboration cursors.
- **Layout Pattern**: Full-screen workspace. Toolbar at top or left. Properties panel on right (collapsible). Layers/assets panel on left (collapsible). Minimal chrome to maximize canvas.
- **Flows In**: Create new, edit existing, template selection, duplicate item.
- **Flows Out**: Save and exit, preview, publish, share, export.
- **Density**: Variable. Toolbar and panels are dense. Canvas is user-controlled.
- **Platform Notes**: Web-primary for complex editors (Figma, Notion, VS Code). Native apps for performance-sensitive editing (Photoshop, Final Cut). Touch-optimized toolbars for iPad.

### 1.25 Wizard / Multi-Step Form
- **Purpose**: Break a complex task into manageable sequential steps. Reduce cognitive load.
- **Key Components**: Step progress indicator (stepper), step title, form fields for current step, next/back buttons, save draft option, validation per step, summary/review step before submission.
- **Layout Pattern**: Progress indicator at top. One step visible at a time. Navigation buttons at bottom (back left, next right). Summary step shows all entries for review. Confirmation after final submit.
- **Flows In**: CTA to start complex process (apply, configure, onboard).
- **Flows Out**: Completion/success page, back to dashboard, save as draft.
- **Density**: Low per step. The whole point is to chunk information.

### 1.26 Comparison
- **Purpose**: Help users evaluate options side by side. Feature comparison, plan comparison.
- **Key Components**: Column headers (options being compared), feature rows, check/cross indicators, highlight for recommended option, sticky column headers, add/remove columns.
- **Layout Pattern**: Table/grid with horizontal scroll on mobile. Sticky first column (feature names). 2-4 columns typical. Highlight recommended with badge or color. Collapse categories with expand/collapse.
- **Flows In**: Pricing page, product listing, category browse.
- **Flows Out**: Selection/purchase, detail page per option, customize option.
- **Density**: High. Dense by necessity.
- **Platform Notes**: Horizontal scroll with snap points on mobile. Full table on desktop. Consider card-based toggle view for mobile as alternative.

### 1.27 Pricing
- **Purpose**: Present plans and pricing. Drive conversion to optimal plan.
- **Key Components**: Plan cards (3-4 plans), plan name + price + billing toggle (monthly/annual), feature list per plan, CTA per plan, recommended badge, FAQ section, enterprise contact option.
- **Layout Pattern**: Horizontal card layout (3-4 columns desktop, horizontal scroll or stacked on mobile). Monthly/annual toggle at top. Recommended plan visually elevated (larger, bordered, badged). FAQ below.
- **Flows In**: Landing page, upgrade prompt, navigation menu, trial expiration.
- **Flows Out**: Checkout/payment, plan comparison detail, contact sales, FAQ anchor links.
- **Density**: Medium. Clear pricing must not feel cluttered.

### 1.28 About / Team
- **Purpose**: Build trust and human connection. Company story, mission, team members.
- **Key Components**: Company narrative section, mission/values, team member grid (photo + name + role + bio), office photos, metrics (customers served, years in business), investor logos, career link.
- **Layout Pattern**: Long-scroll single page. Narrative sections with full-width imagery. Team grid (3-4 columns). Alternating content blocks.
- **Flows In**: Footer link, navigation menu, about link from landing page.
- **Flows Out**: Careers page, contact page, specific team member profile, social links.
- **Density**: Low-Medium. Storytelling pace.

### 1.29 Contact
- **Purpose**: Provide communication channels. Collect inquiries.
- **Key Components**: Contact form (name, email, subject, message), office address + map, phone number, email address, social media links, business hours, FAQ link.
- **Layout Pattern**: Two-column on desktop (form left, contact info right). Stacked on mobile (form then info). Map embed optional.
- **Flows In**: Footer link, navigation, support redirect, about page.
- **Flows Out**: Form submission confirmation, email client open, map/directions app, FAQ page.
- **Density**: Low.

### 1.30 Blog / Article
- **Purpose**: Present long-form content. Readability and engagement.
- **Key Components**: Title, author byline + avatar + date, hero image, body content (rich text with headings, images, code blocks, quotes), table of contents (sidebar), share buttons, related articles, comments section, reading time estimate, progress bar.
- **Layout Pattern**: Single-column centered content (max-width 680-720px for readability). Optional sticky TOC sidebar on desktop. Sticky share buttons. Related articles grid at bottom.
- **Flows In**: Blog listing, search result, social media link, newsletter link, internal link.
- **Flows Out**: Related articles, author profile, category listing, share to social, comment, CTA within article.
- **Density**: Medium. Text-heavy but well-spaced.
- **Platform Notes**: Web uses semantic HTML (article, header, time). Reader mode support matters. RSS feed availability. AMP optional.

### 1.31 Product Gallery
- **Purpose**: Showcase products visually. Enable browsing, filtering, and selection.
- **Key Components**: Product cards (image + title + price + rating), grid layout, filter sidebar/bar, sort dropdown, pagination or infinite scroll, quick view modal, wishlist toggle, compare toggle.
- **Layout Pattern**: Grid (2-4 columns desktop, 2 columns mobile). Filter sidebar on desktop, filter icon + bottom sheet on mobile. Sticky sort/filter bar. Cards have consistent aspect ratio images.
- **Flows In**: Category navigation, search results, homepage featured section, ad click.
- **Flows Out**: Product detail page, quick view modal, add to cart, wishlist, comparison.
- **Density**: High. Visual scanning of many items.

### 1.32 Booking / Reservation
- **Purpose**: Schedule appointments, reserve resources, book services. Date/time selection with availability.
- **Key Components**: Service/resource selector, date picker (calendar), time slot grid, duration selector, provider/staff selector (optional), booking summary, confirm button, cancellation policy.
- **Layout Pattern**: Step-by-step (select service, select date/time, confirm details, payment). Calendar with available dates highlighted. Time slots as selectable chips. Summary panel on right (desktop) or bottom sheet (mobile).
- **Flows In**: Service page, provider profile, CTA from landing page, rebooking from confirmation.
- **Flows Out**: Confirmation/success page, calendar add prompt, payment, cancellation flow.
- **Density**: Medium. Progressive disclosure through steps.

### 1.33 Confirmation / Success
- **Purpose**: Confirm successful completion of an action. Provide next steps.
- **Key Components**: Success icon (checkmark), confirmation title, order/reference number, summary of what was completed, next steps list, primary CTA (continue shopping / go to dashboard), secondary CTA (download receipt / share), estimated timeline (if applicable).
- **Layout Pattern**: Centered content. Large success icon at top. Summary card. CTA buttons at bottom. Confetti animation optional for celebratory moments.
- **Flows In**: Checkout completion, form submission, booking confirmation, account creation.
- **Flows Out**: Home/dashboard, order tracking, related actions, share.
- **Density**: Low. Celebratory moment. Let the user breathe.

---

## Section 2: User Flow Patterns (22 Types)

Each flow pattern includes: trigger, step sequence, decision nodes, happy path, error paths, edge cases, emotional arc, and key metrics.

### 2.1 Onboarding Flow
- **Trigger**: First app launch or account creation.
- **Steps**: Welcome screen -> Value props (2-3 slides) -> Permission requests (notifications, location) -> Profile setup (avatar, name, preferences) -> First key action guidance -> Home/dashboard.
- **Decision Nodes**: Skip onboarding? Grant permissions? Complete optional profile fields?
- **Happy Path**: User completes all steps and performs first key action within session.
- **Error Path**: User skips everything -> lands on empty dashboard -> churn risk.
- **Edge Cases**: Returning user after reinstall, invited user with pre-filled data, enterprise SSO user.
- **Emotional Arc**: Excited -> Curious -> Empowered -> Ready.
- **Key Metrics**: Completion rate per step, time to first key action, Day 1 retention.

### 2.2 Authentication Flow
- **Trigger**: App launch (no session), session expiration, accessing protected resource.
- **Steps**: Login screen -> Credential entry -> (Optional: MFA challenge) -> Session creation -> Redirect to intended destination.
- **Decision Nodes**: New or returning user? Social or email login? MFA required? Biometric available?
- **Happy Path**: Biometric/passkey -> instant access. Social login -> one tap -> access.
- **Error Path**: Wrong password -> inline error -> forgot password sub-flow. Account locked -> support contact.
- **Edge Cases**: Multiple social accounts, device change, expired magic link, rate-limited login attempts.
- **Emotional Arc**: Friction -> Relief.
- **Key Metrics**: Login success rate, time to authenticate, MFA drop-off rate, password reset rate.

### 2.3 Purchase / Checkout Flow
- **Trigger**: Add to cart, buy now, plan selection.
- **Steps**: Cart review -> (Guest or login) -> Shipping address -> Shipping method -> Payment -> Order review -> Place order -> Confirmation.
- **Decision Nodes**: Guest checkout? Saved address? Saved payment? Apply promo code? Express checkout (Apple Pay/Google Pay)?
- **Happy Path**: Returning user with saved info -> review -> confirm -> 2 clicks.
- **Error Path**: Payment declined -> retry with different method. Address validation failure -> manual correction. Inventory changed during checkout -> notification.
- **Edge Cases**: Cart expiration, price change between cart and checkout, international shipping, tax calculation delays, 3D Secure challenge.
- **Emotional Arc**: Intent -> Consideration -> Commitment -> Satisfaction.
- **Key Metrics**: Cart abandonment rate, checkout completion rate, average steps to purchase, payment failure rate.

### 2.4 Search -> Filter -> Select Flow
- **Trigger**: User has a goal but needs to find the right item.
- **Steps**: Tap search -> Enter query (with autocomplete) -> View results -> Apply filters -> Refine results -> Select item -> View detail.
- **Decision Nodes**: Use suggested query? Apply filters? Change sort order? View in list or grid? Open quick view or full detail?
- **Happy Path**: Type query -> first result matches -> tap -> done.
- **Error Path**: No results -> suggest alternatives, check spelling, broaden filters. Too many results -> prompt filter usage.
- **Edge Cases**: Zero-state search (trending, recent), voice search, search within category, saved searches.
- **Emotional Arc**: Seeking -> Scanning -> Narrowing -> Found.
- **Key Metrics**: Search-to-select rate, average queries per session, filter usage rate, zero-result rate.

### 2.5 CRUD Flow (Create, Read, Update, Delete)
- **Trigger**: User manages their own content or data.
- **Steps**: List view (Read all) -> Create (form/wizard) -> Detail view (Read one) -> Edit (pre-filled form) -> Delete (confirmation dialog).
- **Decision Nodes**: Create from scratch or from template? Edit inline or in modal? Confirm delete or undo?
- **Happy Path**: Create -> save -> appears in list. Edit -> save -> updated in place. Delete -> confirm -> removed with undo toast.
- **Error Path**: Validation failure on create/edit -> inline errors. Conflict on save (another user edited) -> merge or overwrite prompt. Delete of item with dependencies -> warning.
- **Edge Cases**: Bulk operations (multi-select + bulk delete/edit), draft saving, optimistic updates, offline edits.
- **Emotional Arc**: Productive -> Accomplished (create/edit). Cautious -> Relieved (delete).
- **Key Metrics**: Create completion rate, edit frequency, delete rate, error rate per form.

### 2.6 Invite / Share Flow
- **Trigger**: User wants to add collaborators or share content.
- **Steps**: Tap share/invite -> Select method (email, link, social) -> Configure permissions (view, edit, admin) -> Send/copy -> Confirmation.
- **Decision Nodes**: Share with specific people or public link? What permission level? Add a message? Set expiration?
- **Happy Path**: Tap share -> copy link -> paste in chat. Or: invite by email -> recipient gets email -> clicks link -> joins.
- **Error Path**: Invalid email format -> inline error. Recipient already has access -> notification. Share limit reached -> upgrade prompt.
- **Edge Cases**: Sharing with non-users (creates invite), revoking access, share link expiration, shared item deletion.
- **Emotional Arc**: Collaborative -> Generous -> Connected.
- **Key Metrics**: Share rate, invite acceptance rate, viral coefficient, sharing method distribution.

### 2.7 Settings Management Flow
- **Trigger**: User needs to change a preference or configuration.
- **Steps**: Navigate to settings -> Find relevant setting (scan or search) -> Change value -> Confirm/save -> See effect.
- **Decision Nodes**: Which category? Immediate apply or save button? Confirm dangerous changes?
- **Happy Path**: Navigate -> toggle -> instant effect. No save button needed.
- **Error Path**: Invalid input -> validation error. Setting requires verification (e.g., email change -> confirm email).
- **Edge Cases**: Settings sync across devices, admin vs. user settings, setting dependencies (changing one affects another), reset to defaults.
- **Emotional Arc**: Purposeful -> Satisfied.
- **Key Metrics**: Settings page visit rate, most-changed settings, support tickets related to settings.

### 2.8 Content Creation Flow
- **Trigger**: User wants to create new content (post, document, image, etc.).
- **Steps**: Tap create (+) -> Select content type -> Editor/composer -> Add content (text, media, formatting) -> Preview (optional) -> Publish/save -> Confirmation + share prompt.
- **Decision Nodes**: Which content type? Draft or publish immediately? Add tags/categories? Set visibility? Schedule?
- **Happy Path**: Tap + -> type text -> publish -> live instantly.
- **Error Path**: Unsaved changes on exit -> save draft prompt. Upload failure -> retry. Content policy violation -> warning.
- **Edge Cases**: Long-form content with auto-save, collaborative editing, version history, content scheduling, cross-posting.
- **Emotional Arc**: Creative -> Expressive -> Proud -> Social (sharing).
- **Key Metrics**: Content creation rate, publish rate (vs. draft), time to publish, media attachment rate.

### 2.9 Communication Flow
- **Trigger**: User wants to message or contact another user.
- **Steps**: Find contact (search, contacts list, profile page) -> Open/create conversation -> Compose message -> Send -> Await response.
- **Decision Nodes**: New or existing conversation? Text, voice, or video? Add attachments? Mark as urgent?
- **Happy Path**: Tap contact -> type -> send -> delivered -> read -> reply.
- **Error Path**: Network failure -> message queued with retry. User blocked -> notification. Rate limit -> cool-down.
- **Edge Cases**: Offline messaging, message editing/deletion, reactions, threads/replies, group conversations, message forwarding.
- **Emotional Arc**: Intent -> Connected -> Awaiting -> Satisfied.
- **Key Metrics**: Messages per user per day, response time, conversation start rate, media sharing rate.

### 2.10 Notification -> Action Flow
- **Trigger**: System event generates a notification.
- **Steps**: Event occurs -> Notification created -> Delivered (push/in-app/email) -> User sees notification -> Taps -> Navigated to relevant screen -> Takes action.
- **Decision Nodes**: Which channel (push, in-app, email)? Tap or dismiss? Act now or later?
- **Happy Path**: Push notification -> tap -> relevant screen -> action completed.
- **Error Path**: Notification for deleted content -> graceful error. Stale notification -> already handled state. Notification overload -> user mutes.
- **Edge Cases**: Notification grouping/batching, do-not-disturb respect, cross-device deduplication, notification preferences per type.
- **Emotional Arc**: Alerted -> Curious -> Resolved.
- **Key Metrics**: Notification tap rate, action completion rate post-tap, opt-out rate, notification-to-engagement time.

### 2.11 Upgrade / Upsell Flow
- **Trigger**: User hits a paywall, usage limit, or encounters premium feature.
- **Steps**: Feature gate encountered -> Value proposition for upgrade -> Plan comparison -> Plan selection -> Payment -> Confirmation -> Feature unlocked.
- **Decision Nodes**: Which plan? Monthly or annual? Use existing payment method? Apply coupon?
- **Happy Path**: Hit limit -> see value -> upgrade -> instant access.
- **Error Path**: Payment failure -> retry. Price shock -> abandon -> follow-up email.
- **Edge Cases**: Mid-cycle upgrade proration, team/org billing, downgrade from upgrade page, free trial extension.
- **Emotional Arc**: Frustrated (limit) -> Intrigued (value) -> Committed (purchase) -> Empowered (access).
- **Key Metrics**: Upgrade conversion rate, paywall encounter-to-upgrade rate, average time from signup to upgrade, plan distribution.

### 2.12 Cancellation / Churn Flow
- **Trigger**: User initiates cancellation or downgrade.
- **Steps**: Navigate to subscription settings -> Tap cancel -> Retention offer (pause, downgrade, discount) -> Cancellation reason survey -> Confirm cancellation -> Confirmation + what-you-lose summary -> Follow-up email.
- **Decision Nodes**: Accept retention offer? Provide feedback reason? Confirm despite warning?
- **Happy Path (for business)**: User accepts pause or downgrade instead of canceling.
- **Error Path**: User frustrated by dark patterns -> leaves negative review. Can't find cancel button -> support complaint.
- **Edge Cases**: Cancel with time remaining, cancel with annual commitment, team owner canceling for entire team, data export before cancellation.
- **Emotional Arc**: Frustrated -> Heard (survey) -> Resolved.
- **Key Metrics**: Cancellation rate, save rate (retention offer acceptance), reason distribution, reactivation rate.

### 2.13 Error Recovery Flow
- **Trigger**: Something went wrong during a user action.
- **Steps**: Error occurs -> Error message displayed (what happened + what to do) -> User decides recovery path -> Retry / alternative action / contact support -> Resolution.
- **Decision Nodes**: Retry same action? Try alternative? Contact support? Abandon task?
- **Happy Path**: Error -> retry -> success.
- **Error Path**: Persistent error -> escalate to support. Data loss -> apologetic recovery with compensation offer.
- **Edge Cases**: Partial completion (some items saved, some failed), cascading errors, offline errors with queue.
- **Emotional Arc**: Confused -> Informed -> Resolving -> Recovered.
- **Key Metrics**: Error rate, recovery rate, support escalation rate, abandon rate after error.

### 2.14 Help / Support Flow
- **Trigger**: User is confused, stuck, or has a problem they cannot solve alone.
- **Steps**: Tap help/support -> Search knowledge base -> Browse FAQs -> (If unresolved) Start conversation (chatbot -> human) -> Describe issue -> Resolution -> Satisfaction survey.
- **Decision Nodes**: Self-serve or contact support? Chat, email, or phone? Satisfied with bot answer?
- **Happy Path**: Search help -> find article -> problem solved.
- **Error Path**: No relevant article -> chatbot fails -> long wait for human -> frustrated.
- **Edge Cases**: Urgent issues (account locked), pre-authenticated support (no re-login), support in different languages, support during off-hours.
- **Emotional Arc**: Stuck -> Seeking -> Helped -> Relieved.
- **Key Metrics**: Self-serve resolution rate, contact rate, first response time, CSAT score, ticket volume.

### 2.15 Data Import / Export Flow
- **Trigger**: User wants to bring data in from another system or export their data.
- **Steps**: Select import/export -> Choose format (CSV, JSON, API) -> Map fields (import) or select data (export) -> Preview -> Confirm -> Processing -> Completion notification.
- **Decision Nodes**: Which format? Map fields manually or auto-detect? Include all data or select?
- **Happy Path**: Upload CSV -> auto-detect fields -> preview looks correct -> import -> done.
- **Error Path**: Format error -> validation report with row-level errors. Partial import -> summary of successes and failures.
- **Key Metrics**: Import completion rate, error rate per import, export frequency.

### 2.16 Review / Rating Flow
- **Trigger**: User completes a purchase, finishes a course, ends a trip.
- **Steps**: Prompt to review (timing matters) -> Star rating -> Written review (optional) -> Photo upload (optional) -> Submit -> Thank you.
- **Decision Nodes**: Rate now or later? Add text? Add photos? Make review public?
- **Happy Path**: Prompt -> 5 stars -> short text -> submit.
- **Error Path**: Dismiss prompt -> follow-up prompt later (max 2 attempts). Inappropriate content -> moderation flag.
- **Key Metrics**: Review completion rate, average rating, text review rate, photo attachment rate.

### 2.17 Onboarding Checklist / Progressive Activation Flow
- **Trigger**: User has signed up but has not completed all activation milestones.
- **Steps**: Dashboard shows checklist -> User completes each item -> Progress updates -> All items complete -> Celebration + badge/reward.
- **Decision Nodes**: Which item to tackle next? Skip optional items?
- **Happy Path**: Complete all items in first session -> fully activated.
- **Error Path**: Abandon checklist -> incomplete activation -> lower retention.
- **Key Metrics**: Checklist completion rate per item, time to full activation, correlation between activation and retention.

### 2.18 Collaborative Editing Flow
- **Trigger**: Multiple users editing the same document or resource simultaneously.
- **Steps**: Open shared document -> See other cursors/presence -> Edit concurrently -> Changes sync in real-time -> Conflict resolution (if any) -> Version saved.
- **Decision Nodes**: Accept incoming change or keep yours? Resolve conflict manually?
- **Happy Path**: Multiple users edit different sections -> all changes merge cleanly.
- **Error Path**: Edit conflict -> conflict marker shown -> manual merge. Connection lost -> offline edits queued.
- **Key Metrics**: Concurrent editing session rate, conflict rate, sync latency.

### 2.19 Subscription / Renewal Flow
- **Trigger**: Subscription approaching renewal or payment method expiring.
- **Steps**: Reminder notification (email/in-app) -> Review subscription details -> Update payment if needed -> Confirm renewal -> Receipt.
- **Decision Nodes**: Auto-renew or manual confirm? Update payment method? Change plan at renewal?
- **Happy Path**: Auto-renew with valid payment -> receipt email -> no friction.
- **Error Path**: Payment method expired -> update prompt -> retry billing.
- **Key Metrics**: Renewal rate, voluntary vs involuntary churn, payment update rate.

### 2.20 Referral Flow
- **Trigger**: User wants to refer friends for mutual benefit.
- **Steps**: Navigate to referral page -> See reward structure -> Copy referral link or invite by email -> Friend signs up via link -> Both receive reward -> Notification of reward.
- **Decision Nodes**: Share via link, email, or social? Track status of referrals?
- **Happy Path**: Share link -> friend signs up -> both get credit -> repeat.
- **Error Path**: Friend already has account -> no reward. Referral abuse detected -> blocked.
- **Key Metrics**: Referral send rate, referral conversion rate, reward claim rate, viral coefficient.

### 2.21 Account Deletion Flow
- **Trigger**: User wants to permanently delete their account and data.
- **Steps**: Settings -> Account -> Delete account -> Data export offer -> Consequences summary -> Confirm with password/verification -> Cooling-off period notice -> Account scheduled for deletion -> Confirmation email.
- **Decision Nodes**: Export data first? Understand consequences? Confirm identity?
- **Happy Path**: User understands consequences -> exports data -> confirms -> account deleted after cooling-off.
- **Error Path**: User changes mind during cooling-off -> reactivate. User cannot verify identity -> support contact.
- **Key Metrics**: Deletion request rate, cooling-off reactivation rate, data export rate before deletion.

### 2.22 Multi-Device Handoff Flow
- **Trigger**: User switches between devices while performing a task.
- **Steps**: Start task on device A -> State synced to cloud -> Open same app on device B -> Handoff prompt or automatic resume -> Continue task.
- **Decision Nodes**: Accept handoff or start fresh? Which device is primary?
- **Happy Path**: Writing email on phone -> sit at desk -> laptop shows "Continue on Mac" -> seamless.
- **Error Path**: Sync conflict -> latest-edit-wins or manual merge. Offline device -> sync on reconnect.
- **Key Metrics**: Handoff usage rate, cross-device session rate, sync failure rate.

---

## Section 3: Flow Diagram Conventions

When documenting or communicating user flows, use these standardized conventions.

### 3.1 Node Types
- **Start / End**: Rounded rectangle (pill shape). Green for start, red for end.
- **Screen / Page**: Rectangle. Contains screen name. Color-coded by section.
- **Decision**: Diamond. Contains yes/no or conditional question.
- **Action**: Rectangle with rounded corners. User or system action.
- **Sub-flow**: Rectangle with double border. Links to separate flow diagram.
- **Wait / Delay**: Hourglass or clock icon. Async step (email verification, processing).

### 3.2 Path Types
- **Happy Path**: Solid green arrows. The primary expected journey.
- **Error Path**: Dashed red arrows. What happens when things fail.
- **Alternative Path**: Dotted blue arrows. Valid but less common routes.
- **Escape Hatch**: Gray arrows. Exit points (cancel, back, close).

### 3.3 Entry Points
- **Direct URL**: Globe icon. User arrives via typed URL or link.
- **Deep Link**: Chain icon. From push notification, email, or external app.
- **Navigation**: Menu icon. From in-app navigation.
- **System Trigger**: Gear icon. Automated redirect (session expire, maintenance).

### 3.4 Edge Case Annotations
- **Conditional**: Annotate arrows with conditions (e.g., "if cart > $50").
- **Frequency**: Label paths with expected traffic percentage (e.g., "80% of users").
- **Data Dependencies**: Note when a step requires data from a previous step.
- **Timeout**: Note time limits (e.g., "OTP expires in 10 min").

---

## Section 4: UI Element Pattern Catalog (120+ Elements)

### 4.1 Navigation Elements (20)
1. **Top Navigation Bar** — Primary nav for web. Logo left, links center or right, CTA right.
2. **Bottom Tab Bar** — Mobile primary nav. 3-5 tabs. Active state indicator. Badge support.
3. **Sidebar Navigation** — Desktop persistent nav. Collapsible. Section headers. Active indicator.
4. **Hamburger Menu** — Hidden nav behind 3-line icon. Use only when space is critically limited.
5. **Breadcrumbs** — Hierarchical location indicator. Clickable path segments. Separator character.
6. **Pagination** — Page numbers, prev/next, items-per-page selector. For finite datasets.
7. **Tab Bar (Content)** — Horizontal tabs for content sections within a page. Underline active.
8. **Segmented Control** — 2-5 mutually exclusive options. Acts as toggle. Compact.
9. **Stepper / Progress Bar** — Multi-step process indicator. Current, completed, upcoming states.
10. **Back Button** — Return to previous screen. Platform-specific position (top-left iOS, top-left Android).
11. **Close Button** — Dismiss modal or overlay. X icon. Top-right (web/Android) or top-left (iOS).
12. **Floating Action Button (FAB)** — Primary action. Android Material pattern. Bottom-right.
13. **Command Palette** — Keyboard-activated search for actions. Cmd+K pattern. Power user navigation.
14. **Mega Menu** — Large dropdown with categorized links and images. E-commerce pattern.
15. **Drawer Navigation** — Slide-in panel from edge. Temporary overlay. Mobile or secondary nav.
16. **Anchor Links / Scroll Spy** — Jump to sections within long page. Active state updates on scroll.
17. **Quick Actions Menu** — Long-press or right-click context menu. Relevant actions for item.
18. **Skip Navigation Link** — Accessibility. Hidden link to skip to main content. Visible on focus.
19. **Language / Region Selector** — Globe icon dropdown. Flag icons optional (controversial for accessibility).
20. **Notification Bell** — Badge count indicator. Dropdown or navigate to notifications center.

### 4.2 Input Elements (25)
21. **Text Input** — Single-line. Label, placeholder, helper text, error state, character count.
22. **Password Input** — Masked characters. Show/hide toggle. Strength indicator.
23. **Textarea** — Multi-line text. Auto-resize or fixed with scroll. Character/word count.
24. **Select / Dropdown** — Single selection from list. Native or custom. Search within for long lists.
25. **Multi-Select** — Multiple selections. Chips/tags display. Checkbox list or token input.
26. **Checkbox** — Binary toggle for single item. Can be grouped for multiple selections.
27. **Radio Button** — Mutually exclusive selection within a group. Always show all options.
28. **Toggle / Switch** — Binary on/off. Instant effect (no save button needed). Label describes on-state.
29. **Date Picker** — Calendar-based date selection. Min/max date constraints. Range selection variant.
30. **Time Picker** — Hour/minute selection. 12/24 hour format. Scroll wheel or dropdown.
31. **Range Slider** — Value within a range. Single handle or dual (min-max). Step increments.
32. **File Upload** — Drag-and-drop zone or button. File type/size restrictions. Progress indicator.
33. **Color Picker** — Hue/saturation/brightness selector. Hex/RGB/HSL input. Preset swatches.
34. **Search Input** — Text input with search icon. Debounced. Clear button. Autocomplete dropdown.
35. **Number Input** — Numeric value. Increment/decrement buttons. Min/max/step constraints.
36. **Phone Input** — Country code selector + number. Format validation. Auto-formatting.
37. **Email Input** — Email format validation. Suggestion for common domain typos.
38. **URL Input** — Protocol prefix. Validation. Preview/favicon fetch.
39. **Credit Card Input** — Number with Luhn validation. Auto-detect card type. Expiry + CVV.
40. **OTP / Verification Code** — 4-6 digit boxes. Auto-focus next. Paste support. Auto-submit on complete.
41. **Rich Text Editor** — Formatted text input. Toolbar with bold/italic/list/link/image.
42. **Autocomplete / Combobox** — Text input with suggestion dropdown. Fuzzy matching.
43. **Tag Input** — Add/remove tags. Autocomplete suggestions. Max tag limit.
44. **Rating Input** — Star rating (1-5). Hover preview. Half-star option.
45. **Signature Input** — Canvas for drawing signature. Clear/redo. Touch and mouse support.

### 4.3 Display Elements (25)
46. **Avatar** — User photo circle. Fallback to initials. Size variants. Status dot indicator.
47. **Badge** — Count or status indicator. Dot or number. Color-coded by type.
48. **Card** — Contained content block. Image + title + description + actions. Clickable or static.
49. **Table** — Rows and columns. Sortable headers. Row selection. Responsive collapse strategy.
50. **Data Grid** — Enhanced table with inline editing, column resize, virtual scroll, export.
51. **List Item** — Row in a list. Leading icon/avatar + text + trailing action/metadata.
52. **Chip / Tag** — Compact element for labels, filters, selections. Dismissible variant.
53. **Progress Bar** — Determinate (percentage) or indeterminate (loading). Linear.
54. **Progress Circle** — Circular progress indicator. Percentage display. Size variants.
55. **Skeleton Screen** — Placeholder shapes mimicking content layout during loading.
56. **Stat / Metric Card** — Single KPI display. Number + label + trend indicator + sparkline.
57. **Timeline** — Chronological sequence of events. Vertical line with nodes. Expandable entries.
58. **Accordion / Collapsible** — Expandable sections. Single-expand or multi-expand. Icon rotation.
59. **Carousel / Slider** — Horizontal scrolling content. Dots/arrows navigation. Auto-play optional.
60. **Image Gallery** — Grid of images. Lightbox on click. Zoom. Thumbnail strip.
61. **Video Player** — Play/pause, progress bar, volume, fullscreen, speed, captions.
62. **Audio Player** — Play/pause, progress bar, volume, speed, waveform visualization.
63. **Code Block** — Syntax-highlighted code. Copy button. Language label. Line numbers.
64. **Markdown Renderer** — Rendered markdown with heading hierarchy, lists, tables, code.
65. **Chart (Line)** — Trend over time. Multiple series. Hover tooltip. Legend.
66. **Chart (Bar)** — Comparison across categories. Horizontal or vertical. Stacked variant.
67. **Chart (Pie/Donut)** — Part-to-whole relationships. Legend. Hover tooltip. Avoid > 6 slices.
68. **Map Embed** — Interactive map with markers. Zoom/pan. Popup on marker click.
69. **Empty State Illustration** — Friendly graphic for zero-data states. Pairs with CTA.
70. **Divider / Separator** — Horizontal or vertical line. Separates content sections.

### 4.4 Feedback Elements (20)
71. **Toast / Snackbar** — Temporary message. Bottom of screen. Auto-dismiss. Optional action (undo).
72. **Alert Banner** — Persistent message at top. Info/warning/error/success variants. Dismissible.
73. **Inline Error** — Error message below form field. Red text + icon. Specific guidance.
74. **Success Message** — Green confirmation. Checkmark icon. Brief and clear.
75. **Warning Message** — Yellow/amber alert. Caution icon. Describes risk and recommended action.
76. **Loading Spinner** — Indeterminate circular indicator. Inline or overlay. With optional text.
77. **Pull-to-Refresh** — Mobile gesture. Animated indicator at top of scrollable content.
78. **Tooltip** — Hover-triggered popover with brief help text. Arrow pointing to trigger.
79. **Popover** — Click-triggered rich content popup. Can contain forms, lists, actions.
80. **Notification Badge** — Red dot or count on icon. Indicates unread/pending items.
81. **Confetti / Celebration** — Particle animation for milestone achievements. Use sparingly.
82. **Shake Animation** — Error feedback on invalid submission. Subtle horizontal shake.
83. **Haptic Feedback** — Physical vibration on mobile. Success, warning, error patterns.
84. **Sound Feedback** — Audio cue for actions. Message sent whoosh, error beep. Respects mute.
85. **Progress Toast** — Upload/download progress. Percentage + cancel option. Persists until complete.
86. **Validation Summary** — List of all form errors at top of form. Links to each field.
87. **Status Indicator** — Colored dot (green/yellow/red) for system or user status.
88. **Typing Indicator** — Three animated dots in chat. Shows when another user is composing.
89. **Read Receipt** — Check marks for sent/delivered/read message status.
90. **Connection Status** — Online/offline indicator. Banner when connection lost/restored.

### 4.5 Overlay Elements (15)
91. **Modal Dialog** — Centered overlay with backdrop. Focused task. Trap focus inside.
92. **Bottom Sheet** — Slides up from bottom. Mobile pattern. Draggable. Snap points.
93. **Side Sheet / Drawer** — Slides from edge. Detail panel. Desktop pattern.
94. **Lightbox** — Full-screen media viewer. Dark backdrop. Swipe to navigate. Close X.
95. **Full-Screen Overlay** — Takes over entire viewport. For immersive tasks (editor, video).
96. **Action Sheet** — iOS-style bottom options list. Cancel button. Destructive option in red.
97. **Alert Dialog** — System-level confirmation. Title + message + 2 buttons (cancel + confirm).
98. **Dropdown Menu** — Triggered by button click. List of actions. Positioned relative to trigger.
99. **Context Menu** — Right-click (web) or long-press (mobile) options. Contextual actions.
100. **Command Palette** — Cmd+K overlay. Search for actions, pages, settings. Power user tool.
101. **Cookie Consent Banner** — Bottom or overlay. Accept/reject/customize. GDPR/CCPA compliance.
102. **Announcement Bar** — Top of page. Promotional or system message. Dismissible.
103. **Onboarding Tooltip** — Pointed overlay highlighting a feature. Step sequence. Skip all option.
104. **Image Crop Modal** — Crop tool for uploaded images. Aspect ratio lock. Zoom.
105. **Share Sheet** — Native or custom sharing options. Copy link, social platforms, messaging.

### 4.6 Layout Elements (15+)
106. **Grid System** — 12-column (web), flexible (mobile). Gutters, margins, breakpoints.
107. **Stack (Vertical)** — Elements stacked top-to-bottom. Consistent spacing.
108. **Stack (Horizontal)** — Elements arranged left-to-right. Wrap on overflow.
109. **Split View** — Two panels side by side. Master-detail pattern. Resizable divider.
110. **Sticky Header** — Fixed at top on scroll. Compact variant after scroll threshold.
111. **Sticky Footer** — Fixed at bottom. CTA bar, action buttons, or tab bar.
112. **Scroll Container** — Scrollable area within fixed layout. Vertical or horizontal.
113. **Masonry Grid** — Pinterest-style variable-height grid. Optimal for mixed-size content.
114. **Container** — Max-width wrapper centering content. Responsive breakpoints.
115. **Spacer** — Empty spacing element. Consistent vertical rhythm.
116. **Responsive Breakpoints** — Mobile (<640px), Tablet (640-1024px), Desktop (>1024px). Content reflows.
117. **Aspect Ratio Box** — Maintains width-to-height ratio regardless of container width.
118. **Overlay Layout** — Content layered with z-index. Map + controls, video + captions.
119. **Holy Grail Layout** — Header + sidebar + main + sidebar + footer. Classic web layout.
120. **Dashboard Grid** — Draggable, resizable widget tiles. User-configurable layout.

---

## Section 5: Screen-to-Screen Transitions

### 5.1 Push Transition
- **Description**: New screen slides in from the right (LTR) while current slides left. Standard forward navigation.
- **Use When**: Navigating deeper into a hierarchy (list -> detail).
- **iOS**: UINavigationController push. Automatic back gesture (swipe from left edge).
- **Android**: Fragment transaction with slide animation. Predictive back gesture (Android 14+).
- **Web**: Route change. CSS slide animation or View Transitions API. Browser back button.

### 5.2 Modal Presentation
- **Description**: New screen slides up from bottom or fades in as an overlay. Interrupts flow for focused task.
- **Use When**: Creating new content, confirming destructive action, completing a sub-task that should not lose context.
- **iOS**: Present modally. Sheet detents (.medium, .large). Drag to dismiss. Close button top-left.
- **Android**: Bottom sheet or dialog fragment. Scrim behind. Swipe to dismiss.
- **Web**: Modal dialog with backdrop. Escape key to close. Focus trapped inside.

### 5.3 Replace / Swap
- **Description**: Current screen is replaced in-place. No back navigation to replaced screen.
- **Use When**: Post-login redirect, completing a flow (checkout -> confirmation), switching accounts.
- **iOS**: Set view controllers on navigation stack.
- **Android**: Replace fragment without adding to back stack.
- **Web**: `window.location.replace()` or router replace.

### 5.4 Tab Switch
- **Description**: Instant switch between top-level sections. No animation or cross-fade.
- **Use When**: Switching between primary app sections (home, search, profile, settings).
- **iOS**: UITabBarController. Each tab preserves its own navigation stack.
- **Android**: BottomNavigationView. Fragment per tab.
- **Web**: Tab component or route-based sections.

### 5.5 Back / Pop
- **Description**: Reverse of push. Current screen exits right, previous screen returns from left.
- **Use When**: User presses back button, swipes back, or presses hardware/software back.
- **iOS**: Pop from navigation stack. Interactive swipe-to-go-back.
- **Android**: System back button. Predictive back animation.
- **Web**: Browser back. History pop state.

### 5.6 Deep Link / Cold Start
- **Description**: App opens directly to a specific screen, bypassing normal navigation.
- **Use When**: Push notification tap, email link, QR code, universal link, app shortcut.
- **iOS**: Universal Links, URL schemes. Handle in AppDelegate / SceneDelegate.
- **Android**: Intent filters, App Links. Handle in Activity.
- **Web**: Direct URL. Server-side rendering or client-side route match.
- **Important**: Must handle authentication state. If user not logged in, queue deep link destination and redirect after login.

---

## Section 6: Screen State Machines

Every screen passes through states. Model them explicitly to ensure all states are designed.

### 6.1 The Five Core States

```
[Initial] -> [Loading] -> [Loaded / Populated]
                |               |
                v               v
            [Error]       [Empty]
                |               |
                v               v
           [Retry -> Loading]  [Action -> Loading]
```

1. **Initial**: Screen is mounted but no data request has fired yet. Often invisible (immediate transition to Loading).
2. **Loading**: Data is being fetched. Show skeleton screens (preferred), spinner, or shimmer. Never show a blank screen.
3. **Loaded / Populated**: Data received and displayed. The "happy" state. Most design time is spent here.
4. **Empty**: Data request succeeded but returned zero items. Show empty state illustration + CTA.
5. **Error**: Data request failed. Show error message + retry button. Distinguish between network error, server error, and permission error.

### 6.2 Extended States

- **Refreshing**: Pulling to refresh or background sync. Show inline indicator without replacing content.
- **Partial Load**: Some data loaded, more available. Infinite scroll loading indicator at bottom.
- **Stale**: Data is old. Show "last updated" timestamp. Background refresh in progress.
- **Offline**: No network connection. Show cached data with offline banner. Queue actions for sync.
- **Permission Required**: User has not granted necessary permission (location, camera, contacts). Show explanation + request button.

### 6.3 State Design Checklist

For every screen, verify you have designed:
- [ ] Loading state (skeleton or spinner)
- [ ] Populated state (with real data, not lorem ipsum)
- [ ] Empty state (zero items, with helpful CTA)
- [ ] Error state (with clear message and retry)
- [ ] Partial/paginated state (loading more indicator)
- [ ] Offline state (if applicable)
- [ ] Permission request state (if applicable)

---

## Section 7: Information Density Levels

### 7.1 Three Density Tiers

| Tier | Description | Target Elements per Viewport | Example Screen Types |
|------|-------------|------|------|
| **Low** | Breathing room. One idea per fold. Marketing-oriented. | 3-5 | Landing, onboarding, login, confirmation, empty state, error pages |
| **Medium** | Balanced. Content-rich but not overwhelming. Scrolling expected. | 6-12 | Profile, detail, settings, blog/article, checkout, contact |
| **High** | Data-dense. Power users. Scanning and filtering essential. | 12-25+ | Dashboard, analytics, file manager, data table, calendar, comparison |

### 7.2 Density Adjustments by Platform

- **Mobile**: Reduce density by 30-40% vs desktop. Stack columns. Collapse secondary info behind taps.
- **Tablet**: Intermediate density. Use split views to maintain context without overwhelming.
- **Desktop**: Highest density acceptable. Multi-column layouts, sidebars, persistent panels.

### 7.3 Density Controls for Users

- **Comfortable / Cozy / Compact**: Gmail-style density toggle. Adjusts row height and spacing.
- **Card / List / Table**: View mode toggle. Cards are lowest density, tables are highest.
- **Show/Hide Columns**: Let users configure which columns appear in data tables.
- **Collapse Panels**: Resizable and collapsible sidebars for user-controlled density.

---

## Section 8: Platform-Specific Screen Conventions

### 8.1 iOS Conventions
- **Navigation**: Large title that collapses on scroll. Back button with previous screen title. Tab bar at bottom (max 5).
- **Inputs**: Grouped inset list style for forms. Date picker as inline expanding calendar or bottom wheel.
- **Modals**: Sheet presentation with detents. Drag indicator at top. Close button top-left ("Cancel" or X).
- **Actions**: Trailing swipe actions on list items (delete, archive). Long-press context menu with preview.
- **System Integration**: SF Symbols for icons. Dynamic Type for text scaling. Haptic feedback on interactions. Sign in with Apple required if any social auth.
- **iOS 26 Liquid Glass**: Translucent tab bars and navigation bars. Frosted glass material. Vibrant label colors. Floating tab bar style.

### 8.2 Android Conventions
- **Navigation**: Top app bar (small, medium, or large). Bottom navigation bar (3-5 items). Navigation drawer for secondary items. Extended FAB for primary action.
- **Inputs**: Filled or outlined text fields (Material 3). Exposed dropdown menus. Chips for filters and selections.
- **Modals**: Bottom sheets (standard, modal). Dialog with title, content, actions. Full-screen dialog for complex tasks.
- **Actions**: 3-dot overflow menu in app bar. Swipe-to-dismiss on notifications. Long-press for selection mode.
- **System Integration**: Material You dynamic color. Predictive back gesture (Android 14+). Edge-to-edge content. Google One Tap sign-in.
- **Material 3 Expressive**: New emphasis on personality through shape, color, and motion. Squircle containers. Expressive type scale.

### 8.3 Web Conventions
- **Navigation**: Horizontal navbar with dropdowns. Breadcrumbs for hierarchy. Sidebar for app-type products. Footer with site map.
- **Inputs**: Native form elements (accessible by default) or custom components with full ARIA. Inline validation on blur.
- **Modals**: Dialog element (native). Focus trap. Escape to close. Scroll lock on body.
- **Actions**: Hover states on all interactive elements. Right-click context menu (custom). Keyboard shortcuts. Command palette (Cmd+K).
- **System Integration**: Responsive breakpoints (mobile-first). Prefers-color-scheme for dark mode. Prefers-reduced-motion for accessibility. View Transitions API for page animations. PWA install prompt.
- **Modern CSS (2025-2026)**: Container queries, :has() selector, subgrid, scroll-driven animations, anchor positioning, view transitions.

### 8.4 Cross-Platform Consistency Rules

1. **Same information architecture** across all platforms. Screen names and hierarchy match.
2. **Platform-native navigation patterns**. Do not put a bottom tab bar on web or a hamburger menu on iOS.
3. **Shared design tokens** for colors, typography scales, spacing. Platform-specific adjustments for density and touch targets.
4. **Feature parity by intent, not by implementation**. Swipe-to-delete on iOS, long-press menu on Android, right-click on web all achieve the same goal.
5. **Minimum touch target**: 44x44pt (iOS), 48x48dp (Android), 44x44px (Web WCAG).

---

## Cross-References

- **component-patterns-code** — React, SwiftUI, and CSS implementations for elements described here
- **performance-states-patterns** — Loading, error, and empty state patterns referenced in screen states
- **mobile-ux-design** — iOS and Android platform conventions for mobile adaptations
- **desktop-app-design** — Desktop layout patterns for sidebar, split-view, and data-dense screens
- **cognitive-psychology-ux** — Cognitive load theory behind flow design and information hierarchy
- **accessibility-inclusive-design** — WCAG 2.2 compliance details for all screen and element patterns
- **interaction-motion-design** — Transition and animation patterns between screens and states
- **ui-pattern-intelligence** — Detailed pattern implementations for elements cataloged here
- **navigation-pattern-encyclopedia** — Deep dives on every navigation pattern listed in Section 4.1
- **form-design-encyclopedia** — Deep dives on every input element listed in Section 4.2
- **platform-visual-standards** — iOS 26 Liquid Glass, M3 Expressive, and modern CSS implementation details

## Commands Powered by This Skill

| Command | Purpose |
|---------|---------|
| `/screen` | Generate a complete screen specification with layout, components, states, and accessibility |
| `/flow` | Generate a user flow with step sequences, branching, error handling, and metrics |
| `/inspo` | Get curated inspiration sources for a specific screen type, flow, or design problem |
