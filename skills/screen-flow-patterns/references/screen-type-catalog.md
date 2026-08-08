# Screen Type Catalog — 27 Screen Types with UX Patterns

> For each screen type: layout pattern, key components, information hierarchy, states to handle, accessibility requirements, mobile vs. desktop adaptation, common mistakes, and 3 reference implementations.

---

## 1. Welcome / Splash

**Layout pattern:** Full-bleed centered. Single focal point (logo or hero image) with vertically stacked CTAs at the bottom third. No navigation chrome.

**Key components:**
- Brand logo or wordmark (centered, upper third)
- Hero illustration, video, or value-prop image (middle third)
- Primary CTA: "Get Started" or "Sign Up" (bottom third)
- Secondary CTA: "Log In" (text link below primary)
- Optional: social proof line ("Join 2M+ users") or app store badges

**Information hierarchy:**
1. Brand identity (who is this?)
2. Value proposition (why should I care?)
3. Primary action (what do I do?)
4. Secondary action (I already have an account)

**States to handle:**
- **First launch:** Full welcome experience with animation
- **Returning unauthenticated:** Skip animation, show CTAs immediately
- **Deep link arrival:** Brief flash then redirect to target
- **Offline:** Show brand + "No connection" message with retry
- **Loading:** Skeleton of logo + shimmer on CTA area

**Accessibility requirements:**
- Hero image must have descriptive alt text
- CTAs must be minimum 44x44pt touch targets
- Color contrast ratio 4.5:1 for all text on background image (use overlay)
- Auto-playing video must have pause control and no audio by default
- Screen reader should announce: brand name, value prop, available actions

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen, CTAs at bottom within thumb zone, logo scales down
- Desktop: Centered card (max-width 480px) or split layout (image left, CTAs right)

**Common mistakes:**
1. Auto-playing video with sound (instant bounce)
2. No "Log In" option visible (returning users stranded)
3. Value proposition is vague ("The best app for everything") instead of specific

**Reference implementations:**
- **Headspace** — Calming animation, clear "Get Started" + "Log In", value prop in 6 words
- **Notion** — Clean split layout on desktop, single CTA focus on mobile
- **Duolingo** — Character-driven illustration, playful tone, immediate language selection

---

## 2. Login

**Layout pattern:** Centered card on desktop (max-width 400px), full-width form on mobile. Vertically stacked fields with CTA below.

**Key components:**
- Email/username input field
- Password input field with show/hide toggle
- "Forgot password?" link (right-aligned below password field)
- Primary CTA: "Log In" button (full-width)
- Divider: "or continue with"
- Social login buttons (Google, Apple, etc.)
- "Don't have an account? Sign Up" link at bottom
- Optional: "Remember me" checkbox

**Information hierarchy:**
1. Form fields (the task)
2. Primary action button
3. Recovery option (forgot password)
4. Alternative login methods
5. Signup redirect

**States to handle:**
- **Default:** Empty form, primary CTA disabled or enabled
- **Filling:** Real-time validation on email format, password visibility toggle
- **Submitting:** Button shows spinner, fields disabled
- **Error — wrong credentials:** Inline error "Incorrect email or password" (never reveal which is wrong)
- **Error — account locked:** Message with unlock instructions
- **Error — network:** "Connection failed. Check your internet and try again."
- **Success:** Brief success state then redirect
- **Rate limited:** "Too many attempts. Try again in 5 minutes."
- **SSO redirect:** Loading state while redirecting to identity provider

**Accessibility requirements:**
- Labels associated with inputs via `for`/`id` or wrapping `<label>`
- Error messages linked to fields via `aria-describedby`
- `aria-live="polite"` on error message container
- Password toggle button: `aria-label="Show password"` / `aria-label="Hide password"`
- Form submittable via Enter key
- Focus moves to first error field on submission failure
- Minimum touch target 44x44pt for all interactive elements

**Mobile vs. desktop adaptation:**
- Mobile: Full-width inputs, large touch targets, keyboard type `email` for email field, biometric login option (Face ID/fingerprint) as primary
- Desktop: Centered card with subtle shadow, autofill support, tabindex order

**Common mistakes:**
1. Revealing whether email exists in the system ("No account found for this email") — security risk
2. Clearing the password field on error (forces re-entry)
3. No biometric/passkey option on mobile (friction for returning users)

**Reference implementations:**
- **Stripe** — Clean centered card, email-first flow, excellent error messages
- **Linear** — Magic link + Google SSO prominence, minimal friction
- **Apple ID** — Email-first then password, biometric integration, clear error states

---

## 3. Signup / Registration

**Layout pattern:** Centered card (desktop) or full-screen form (mobile). Progressive disclosure — single column, one field visible at a time or grouped logically. Optional split layout with benefits panel on desktop.

**Key components:**
- Email input field
- Password input with strength indicator
- Name field(s) — first/last or single "Full name"
- Terms of service + privacy policy checkbox or passive consent text
- Primary CTA: "Create Account" (full-width)
- Social signup buttons
- "Already have an account? Log In" link
- Optional: referral code field, organization name

**Information hierarchy:**
1. Form fields (minimal — only what is needed to create account)
2. Password requirements (inline, updating in real-time)
3. Primary action
4. Legal consent
5. Alternative methods
6. Login redirect

**States to handle:**
- **Default:** Empty form
- **Filling:** Real-time email format validation, password strength meter updating
- **Email taken:** "An account with this email already exists. Log in or reset password?"
- **Weak password:** Inline strength indicator + requirements checklist
- **Submitting:** Button loading state
- **Success:** Welcome message or redirect to onboarding
- **Verification required:** "Check your email for a verification link"
- **Error — server:** Generic retry message

**Accessibility requirements:**
- Password strength indicator must be conveyed non-visually (`aria-live` region describing strength level)
- Requirements checklist items should use `aria-label` with completion state
- Terms link must be keyboard accessible and open in new tab with `aria-label` indicating external link
- All form errors announced to screen readers immediately
- Do not rely on color alone for password strength (use text + icon)

**Mobile vs. desktop adaptation:**
- Mobile: One field per viewport (step-by-step) or compact single form, keyboard-appropriate types
- Desktop: Single form with optional benefits/social-proof sidebar

**Common mistakes:**
1. Asking for too much information upfront (phone, address, birthday) — defer to later
2. Password requirements only shown after failed submission instead of proactively
3. No inline validation — user fills entire form then sees multiple errors

**Reference implementations:**
- **Figma** — Email-first, then name + password, minimal fields, Google SSO prominent
- **Slack** — Email first, then magic link or continue to password, workspace context
- **Coinbase** — Step-by-step progressive disclosure, clear legal requirements

---

## 4. Password Reset

**Layout pattern:** Centered card, single input. Multi-step: (1) enter email, (2) check email confirmation, (3) enter new password, (4) success.

**Key components:**
- Step 1: Email input + "Send Reset Link" button + "Back to Login" link
- Step 2: Confirmation message + "Open email app" button + "Resend" link with cooldown timer
- Step 3: New password + confirm password + strength indicator + "Reset Password" button
- Step 4: Success message + "Go to Login" button

**Information hierarchy:**
1. Clear instruction text ("Enter your email to reset your password")
2. Input field
3. Action button
4. Navigation back to login

**States to handle:**
- **Email not found:** Do NOT reveal this — always show "If an account exists, we've sent a link" (security)
- **Rate limited:** "Reset link already sent. Check spam or try again in X minutes."
- **Link expired:** "This reset link has expired. Request a new one."
- **Password mismatch:** Inline error on confirm field
- **Success:** Clear confirmation with next action

**Accessibility requirements:**
- Progress indication for multi-step (step X of Y, announced to screen readers)
- Timer for resend cooldown must be `aria-live`
- New password field requirements conveyed proactively
- Focus management: move focus to relevant content on step transitions

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen per step, "Open email app" deep link button
- Desktop: Centered card, same content

**Common mistakes:**
1. Revealing whether email exists (security vulnerability)
2. No "Open email app" button (user has to manually switch)
3. Reset link with no expiry or too-short expiry (< 1 hour)

**Reference implementations:**
- **GitHub** — Clean multi-step, code-based verification option, clear expiry info
- **Google** — Multi-factor verification before reset, strong security
- **Shopify** — Simple flow, "Open email" button, clear timing expectations

---

## 5. Home / Dashboard

**Layout pattern:** Grid-based with information density appropriate to role. Often sidebar navigation (desktop) + content area. Cards or widgets for discrete data groups. Mobile uses bottom tab bar with scrollable content.

**Key components:**
- Greeting/context header ("Good morning, Alex" or "Dashboard")
- Key metrics / KPI cards (3-5 at top)
- Activity feed or recent items
- Quick actions (create, add, invite)
- Navigation to primary sections
- Notifications indicator
- Optional: search, date range filter, data visualization charts

**Information hierarchy:**
1. Orientation (where am I, what time context)
2. Key metrics (how are things going)
3. Recent activity (what happened)
4. Quick actions (what should I do next)
5. Navigation to deeper sections

**States to handle:**
- **First-time (empty):** Onboarding tasks, guided setup, sample data
- **Populated:** Full data with progressive loading
- **Loading:** Skeleton screens per card/widget
- **Error per widget:** Individual widget error states (don't break the whole page)
- **Stale data:** "Last updated 5 min ago" with refresh
- **Offline:** Cached data with offline indicator

**Accessibility requirements:**
- Landmark regions: `<main>`, `<nav>`, `<aside>` for sidebar
- KPI cards: use proper heading hierarchy, not just large text
- Charts must have text alternatives (data table or summary)
- Skip navigation link to main content
- Widget error states announced to screen readers

**Mobile vs. desktop adaptation:**
- Mobile: Single column, KPIs in horizontal scroll or 2-column grid, bottom nav
- Desktop: Sidebar nav + multi-column grid, data-dense layout acceptable
- Tablet: Collapsible sidebar, 2-column grid

**Common mistakes:**
1. Information overload — showing everything instead of prioritizing
2. No empty/first-time state — new users see a blank page
3. All data loads synchronously — slow initial paint

**Reference implementations:**
- **Stripe Dashboard** — Clean KPI cards, activity feed, progressive data loading
- **Linear** — Focused on "my issues," minimal but actionable
- **Shopify Admin** — Contextual insights, guided setup for new stores

---

## 6. Feed / Timeline

**Layout pattern:** Single-column, vertically scrolling, content-width constrained (max 600-680px on desktop). Infinite scroll or paginated. Reverse chronological or algorithmically sorted.

**Key components:**
- Feed items (cards with author, timestamp, content, actions)
- Compose/create button or input (top of feed or FAB)
- Filter/sort controls (Following, For You, Recent)
- Pull-to-refresh (mobile)
- New items indicator ("3 new posts" pill at top)
- Load more trigger (infinite scroll or "Load more" button)

**Information hierarchy per item:**
1. Author identity (avatar + name)
2. Content (text, image, video)
3. Engagement signals (likes, comments, shares)
4. Actions (like, comment, share, save)
5. Timestamp

**States to handle:**
- **Empty feed:** "Follow people to see posts here" with suggestions
- **Loading:** Skeleton cards (3-5 placeholder items)
- **End of feed:** "You're all caught up" message
- **New items while scrolling:** Floating pill "New posts" — tap to scroll to top
- **Error loading more:** Retry button inline
- **Offline:** Cached items + "You're offline" banner
- **Single item error:** Graceful removal or "This post is unavailable"

**Accessibility requirements:**
- Feed items as `<article>` elements within a `<feed>` role container
- `aria-setsize` and `aria-posinset` for virtual scrolling
- Images in posts require alt text (user-provided or AI-generated)
- Video autoplay must respect `prefers-reduced-motion`
- Infinite scroll must have keyboard-accessible "Load more" fallback
- Time stamps as `<time>` elements with full datetime

**Mobile vs. desktop adaptation:**
- Mobile: Full-width cards, thumb-zone actions, pull-to-refresh gesture
- Desktop: Centered column (max 680px), sidebar with trending/suggestions

**Common mistakes:**
1. No "caught up" indicator — users scroll forever wondering if there's more
2. Autoplay video with sound
3. Infinite scroll with no way to reach the footer (put footer in sidebar on desktop)

**Reference implementations:**
- **Twitter/X** — Tab-based feed switching (For You / Following), new tweets indicator
- **Instagram** — Clean card layout, stories at top, strong visual hierarchy
- **LinkedIn** — Content type variety (text, articles, polls), engagement-driven sort

---

## 7. Search & Results

**Layout pattern:** Search bar prominent at top. Results in list or grid below. Filter panel as sidebar (desktop) or bottom sheet (mobile). Zero-state with suggestions.

**Key components:**
- Search input with icon, clear button, and voice input option
- Recent searches (zero state)
- Trending/suggested searches (zero state)
- Results list/grid with result count
- Filter/sort controls
- Pagination or infinite scroll
- "No results" state with suggestions
- Optional: search-as-you-type suggestions, category tabs

**Information hierarchy:**
1. Search input (always accessible)
2. Result count + active filters
3. Results (matched content with highlighted terms)
4. Filter/sort options
5. Pagination

**States to handle:**
- **Zero state:** Recent searches, trending, categories
- **Typing:** Autocomplete suggestions dropdown (max 5-8)
- **Loading results:** Skeleton list or spinner
- **Results found:** Count + items
- **No results:** "No results for 'xyz'" + suggestions (check spelling, try broader terms, browse categories)
- **Error:** "Search failed. Try again."
- **Filtered to zero:** "No results match your filters" + "Clear all filters" button

**Accessibility requirements:**
- Search input: `role="searchbox"` or `<input type="search">`
- Autocomplete: `role="listbox"` with `aria-activedescendant` for highlighted option
- Results region: `aria-live="polite"` announcing result count on update
- Filter controls: proper `role="checkbox"` or `role="radio"` for filter options
- Highlighted search terms in results must not rely solely on color

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen search overlay on tap, filters in bottom sheet or separate screen
- Desktop: Inline search with dropdown suggestions, filter sidebar always visible

**Common mistakes:**
1. No zero-state — blank page until user types
2. No "no results" guidance — dead end with no next step
3. Filters reset when navigating back from a result

**Reference implementations:**
- **Airbnb** — Map + list split, dynamic filters, search-as-you-type with location suggestions
- **Spotify** — Category-based zero state, instant results, genre filtering
- **Amazon** — Robust filtering, result count, sponsored vs. organic clarity

---

## 8. Product Listing Page (PLP)

**Layout pattern:** Grid (2-4 columns desktop, 2 columns mobile) or list view toggle. Filter sidebar (desktop) or sticky filter bar (mobile). Sort dropdown top-right.

**Key components:**
- Product cards (image, title, price, rating, quick-add)
- Category breadcrumbs
- Filter panel (price range, category, brand, size, color, rating)
- Sort control (relevance, price low-high, price high-low, newest, rating)
- Result count
- Pagination or infinite scroll with "Load more"
- View toggle (grid/list)
- Optional: comparison checkbox, wishlist button per card

**Information hierarchy per card:**
1. Product image (primary visual hook)
2. Price (decision driver)
3. Title/name
4. Rating/reviews count
5. Quick action (add to cart / wishlist)

**States to handle:**
- **Loading:** Skeleton grid (match card aspect ratios)
- **Empty category:** "No products in this category" + related categories
- **Filtered to zero:** "No products match filters" + "Clear filters"
- **Sale/promotion:** Badge overlay on card, strikethrough original price
- **Out of stock items:** Grayed or labeled, optionally hidden via filter
- **Error:** Retry loading

**Accessibility requirements:**
- Product cards as `<article>` or list items
- Image alt text: product name + key attribute ("Blue Nike Air Max 90, size 10")
- Price changes on filter: `aria-live` region for result count
- Grid/list toggle: `aria-pressed` state
- Filter checkboxes properly labeled

**Mobile vs. desktop adaptation:**
- Mobile: 2-column grid, sticky filter/sort bar at top, horizontal scrolling filter chips
- Desktop: 3-4 column grid, filter sidebar, hover states on cards

**Common mistakes:**
1. Product images with inconsistent aspect ratios (jagged grid)
2. Too many filters visible — cognitive overload (use progressive disclosure)
3. No way to compare products side-by-side

**Reference implementations:**
- **Shopify (Dawn theme)** — Clean grid, filter sidebar, collection-based navigation
- **Nike** — Strong visual grid, filter chips, quick-add functionality
- **ASOS** — View toggle, comprehensive filters, "save for later" integration

---

## 9. Product Detail Page (PDP)

**Layout pattern:** Split layout on desktop (image gallery left 50-60%, details right 40-50%). Single column on mobile (images carousel top, details below). Sticky "Add to Cart" bar on mobile scroll.

**Key components:**
- Image gallery (zoomable, with thumbnails)
- Product title + brand
- Price (with sale/original if applicable)
- Variant selectors (size, color, material)
- Quantity selector
- "Add to Cart" primary CTA (full-width)
- "Add to Wishlist" secondary action
- Product description (expandable)
- Specifications table
- Reviews section with rating distribution
- Related/recommended products carousel
- Shipping info + return policy
- Optional: size guide, AR try-on, stock indicator

**Information hierarchy:**
1. Product images (is this what I want?)
2. Price (can I afford it?)
3. Variants (is my size/color available?)
4. Add to Cart (take action)
5. Description + specs (details for consideration)
6. Reviews (social proof)
7. Related products (alternatives)

**States to handle:**
- **In stock:** Normal state
- **Low stock:** "Only 3 left" urgency indicator
- **Out of stock:** Disable Add to Cart, show "Notify me when available" or alternative sizes
- **Variant selected:** Update images, price, stock status per variant
- **Added to cart:** Brief confirmation ("Added!") + "View Cart" mini-notification
- **Loading:** Skeleton with image placeholder, text blocks
- **Error loading reviews:** "Couldn't load reviews. Try again."

**Accessibility requirements:**
- Image gallery: keyboard navigable, alt text per image, zoom via button (not hover-only)
- Variant selectors: `role="radiogroup"` with `aria-label` per option
- Out-of-stock variants: `aria-disabled="true"` with explanation
- Price: mark up with `<ins>` (sale) and `<del>` (original) for screen readers
- Add to Cart confirmation: `aria-live` announcement

**Mobile vs. desktop adaptation:**
- Mobile: Swipeable image carousel, sticky bottom "Add to Cart" bar, collapsible sections
- Desktop: Thumbnail gallery with zoom, side-by-side layout, tabbed sections (Description/Reviews/Specs)

**Common mistakes:**
1. Only one product image (users want 4-8 angles minimum)
2. No sticky "Add to Cart" on mobile (user scrolls past and has to scroll back)
3. Variant selection not updating price/availability in real time

**Reference implementations:**
- **Apple Store** — Immersive imagery, configuration-driven layout, clean variant selection
- **Amazon** — Comprehensive detail, Q&A section, variant matrix
- **Everlane** — Clean PDP, transparent pricing, strong photography

---

## 10. Shopping Cart

**Layout pattern:** Single page with item list (left/main) and order summary sidebar (right on desktop, bottom sheet or below on mobile). Each item is a row with image, details, quantity, and price.

**Key components:**
- Cart item rows (thumbnail, name, variant, quantity stepper, line price, remove button)
- Order summary (subtotal, shipping estimate, tax, total)
- Promo code input
- "Proceed to Checkout" primary CTA
- "Continue Shopping" secondary link
- Shipping estimate calculator
- "Save for later" / "Move to wishlist" per item
- Recommended products ("You might also like")

**Information hierarchy:**
1. Cart items (what am I buying?)
2. Order total (what will I pay?)
3. Checkout CTA (take action)
4. Promo code (can I save money?)
5. Cross-sell recommendations

**States to handle:**
- **Empty cart:** Illustration + "Your cart is empty" + "Start Shopping" CTA
- **Single item:** Full layout, no confusion
- **Multiple items:** Clear item separation, running total
- **Item out of stock since added:** Warning banner on that item + "Remove" or "Save for later"
- **Price changed:** "Price updated" indicator with old vs. new
- **Promo applied:** Success message, discount shown in summary
- **Promo invalid:** Inline error below promo input
- **Loading:** Skeleton of item rows

**Accessibility requirements:**
- Quantity stepper: `role="spinbutton"` with `aria-valuemin`, `aria-valuemax`, `aria-valuenow`
- Remove button: `aria-label="Remove [product name] from cart"`
- Order summary: use `<table>` or definition list for label-value pairs
- Live region for total update when quantity changes
- Promo code success/error: `aria-live` announcement

**Mobile vs. desktop adaptation:**
- Mobile: Full-width item cards, order summary at bottom, sticky "Checkout" button
- Desktop: Two-column layout (items + summary sidebar), inline editing

**Common mistakes:**
1. No empty cart state (just a blank page)
2. Quantity changes require page reload instead of inline update
3. Promo code field hidden or hard to find

**Reference implementations:**
- **Shopify (checkout)** — Clean item list, clear summary, smooth quantity updates
- **Apple Store** — Minimal cart, excellent empty state, configuration summary
- **Target** — Save for later, store pickup option, clear price breakdown

---

## 11. Checkout

**Layout pattern:** Simplified chrome (no main navigation — reduce escape routes). Linear multi-step (2-4 steps) or single-page scrollable. Order summary persistent in sidebar (desktop) or collapsible top section (mobile). Progress indicator.

**Key components:**
- Progress indicator (steps: Information > Shipping > Payment > Review)
- Contact/email input
- Shipping address form (with autocomplete)
- Shipping method selection
- Payment method (card inputs, digital wallets)
- Order summary (collapsible on mobile)
- Place Order CTA
- Trust signals (SSL badge, money-back guarantee, payment icons)
- Express checkout buttons (Apple Pay, Google Pay, PayPal) above the fold

**Information hierarchy:**
1. Current step context (where am I in the process)
2. Form fields for this step
3. Order summary (persistent reference)
4. Continue/Place Order CTA
5. Trust signals

**States to handle:**
- **Guest vs. logged in:** Guest checkout must be available, logged in pre-fills address
- **Address validation:** Suggest corrections for ambiguous addresses
- **Payment processing:** "Processing your order..." overlay, disable all interaction
- **Payment declined:** Clear error + "Try another payment method" option
- **Field validation errors:** Inline per field, focus on first error
- **Session timeout:** Warning before expiry, save form state
- **Success:** Redirect to confirmation page

**Accessibility requirements:**
- Step indicator: `aria-current="step"` on active step, completed steps marked
- Address autocomplete: `role="listbox"` for suggestion dropdown
- Payment card inputs: proper `autocomplete` attributes (`cc-number`, `cc-exp`, `cc-csc`)
- Error summary at top of form with links to each error field
- `aria-live` for payment processing status

**Mobile vs. desktop adaptation:**
- Mobile: Single column, one step per screen, express pay prominent, sticky CTA
- Desktop: Two-column (form + order summary sidebar), accordion or multi-step

**Common mistakes:**
1. Requiring account creation before checkout (kills conversion)
2. No express checkout (Apple Pay/Google Pay) above the fold
3. Address form without autocomplete/autofill support

**Reference implementations:**
- **Shopify Checkout** — Industry standard, single-page or multi-step, express pay prominent
- **Stripe Checkout** — Hosted checkout, clean design, strong trust signals
- **Apple Store** — Express checkout, minimal steps for logged-in users

---

## 12. Order Confirmation

**Layout pattern:** Single column, centered content (max-width 680px). Celebration moment at top, then order details.

**Key components:**
- Success icon/animation (checkmark)
- "Order confirmed" headline
- Order number (prominent, copyable)
- Confirmation email notice
- Order summary (items, quantities, prices)
- Shipping address + estimated delivery
- Payment method summary (last 4 digits)
- "Track Order" CTA
- "Continue Shopping" secondary CTA
- Optional: share/social, account creation prompt for guest checkout

**Information hierarchy:**
1. Confirmation (it worked!)
2. Order number (reference for support)
3. Delivery estimate (when will I get it?)
4. Order details (what did I order?)
5. Next actions

**States to handle:**
- **Standard:** Full confirmation
- **Digital/instant delivery:** Include download link or access instructions
- **Partially fulfilled:** Note which items ship separately
- **Guest user:** Prompt to create account to track order

**Accessibility requirements:**
- Focus moves to confirmation heading on page load
- Order number should be selectable/copyable
- Success animation should respect `prefers-reduced-motion`
- All details in proper semantic structure (headings, lists, tables)

**Mobile vs. desktop adaptation:**
- Mobile: Single column, full-width, email app deep link
- Desktop: Centered card, more breathing room

**Common mistakes:**
1. No order number displayed (user has to check email)
2. No clear next step (dead end)
3. No estimated delivery date

**Reference implementations:**
- **Amazon** — Delivery estimate prominent, order tracking link, recommendations
- **Apple** — Clean confirmation, timeline of expected events
- **Uber Eats** — Real-time tracking embedded in confirmation

---

## 13. Order Tracking

**Layout pattern:** Timeline/progress bar at top showing order stages. Details below. Map integration for delivery tracking.

**Key components:**
- Order status progress bar (Confirmed > Shipped > Out for Delivery > Delivered)
- Current status with timestamp
- Estimated delivery date/time
- Tracking number (linked to carrier)
- Map with delivery driver location (if applicable)
- Order items summary
- Delivery address
- Contact support link

**Information hierarchy:**
1. Current status (where is my order?)
2. Estimated delivery (when will it arrive?)
3. Live tracking (where exactly is it now?)
4. Order details (what did I order?)
5. Support access

**States to handle:**
- **Processing:** First step active, no tracking yet
- **Shipped:** Tracking number available, carrier link
- **In transit:** Map/location updates
- **Out for delivery:** Live tracking, "X stops away"
- **Delivered:** Confirmation photo, "Leave a review" CTA
- **Delayed:** Warning banner with updated estimate
- **Exception:** Issue notification with support contact

**Accessibility requirements:**
- Progress bar steps: `aria-current="step"` plus `aria-label` describing each step status
- Map: text alternative with address and ETA
- Auto-updating content: `aria-live="polite"` for status changes
- Timestamps as `<time>` elements

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen map with bottom sheet for details, push notifications
- Desktop: Split layout (map + details sidebar)

**Common mistakes:**
1. Tracking updates lag behind carrier by hours
2. No proactive delay notification
3. Map without text-based ETA fallback

**Reference implementations:**
- **Amazon** — Step-by-step tracking, photo confirmation, map integration
- **Uber Eats** — Real-time driver tracking, stop count, live ETA
- **FedEx** — Detailed tracking timeline, multiple tracking views

---

## 14. User Profile (Own)

**Layout pattern:** Header section (cover photo + avatar + name + bio) with tabbed content below (Posts, Likes, Collections). Edit button prominent.

**Key components:**
- Cover photo / header background
- Profile avatar (with edit/change indicator)
- Display name + handle/username
- Bio/description
- Key stats (posts, followers, following)
- Edit Profile button
- Settings gear icon
- Content tabs (activity, posts, saved items, collections)
- Content grid or list below tabs

**Information hierarchy:**
1. Identity (photo, name)
2. Social proof (stats)
3. Edit action
4. Content tabs
5. Content items

**States to handle:**
- **Complete profile:** Full display
- **Incomplete profile:** Prompts to add missing info (banner: "Add a profile photo")
- **No content yet:** Empty tab states with creation prompts
- **Loading:** Skeleton header + content
- **Profile update success:** Toast "Profile updated"

**Accessibility requirements:**
- Avatar image: `alt="Profile photo of [name]"` or `alt=""` if decorative
- Stats: use proper structure, not just "34 | 1.2K | 890" — label each number
- Tabs: `role="tablist"` with `role="tab"` and `role="tabpanel"`
- Edit button: clear `aria-label="Edit profile"`

**Mobile vs. desktop adaptation:**
- Mobile: Full-width header, scrollable tabs, content below
- Desktop: Wider header, tabs with more horizontal space, content grid

**Common mistakes:**
1. Stats without labels (what does "34" mean?)
2. No prompts for incomplete profile
3. Edit button hard to find or buried in menu

**Reference implementations:**
- **Instagram** — Clean grid layout, story highlights, clear stats
- **Twitter/X** — Cover + avatar overlap, tabbed content, edit prominent
- **GitHub** — Contribution graph, pinned repos, activity feed

---

## 15. User Profile (Public)

**Layout pattern:** Same as own profile but with interaction CTAs instead of edit. Follow/connect button replaces Edit Profile.

**Key components:**
- All profile display elements (avatar, name, bio, stats)
- Follow/Connect primary CTA
- Message secondary CTA
- More options menu (report, block, share profile)
- Public content tabs
- Mutual connections indicator
- Optional: verification badge

**Information hierarchy:**
1. Identity
2. Follow/Connect action
3. Content preview
4. Mutual connections (social proof)

**States to handle:**
- **Not following:** "Follow" primary button
- **Following:** "Following" button (with unfollow on menu/long-press)
- **Follow requested (private account):** "Requested" state
- **Blocked user:** Limited/no profile visibility
- **Own profile viewed as public:** "This is how others see your profile" preview

**Accessibility requirements:**
- Follow button: state clearly communicated (`aria-pressed` or label change)
- Report/block in accessible menu with clear labels
- Same tab and stats requirements as own profile

**Mobile vs. desktop adaptation:**
- Same patterns as own profile, with action buttons in header

**Common mistakes:**
1. Unfollow too easy to trigger accidentally (no confirmation)
2. No "Message" option visible
3. No indication of mutual connections

**Reference implementations:**
- **Instagram** — Follow + Message buttons, mutual followers shown
- **LinkedIn** — Connect + Message, mutual connections prominent
- **Twitter/X** — Follow button, "Followed by people you follow"

---

## 16. Edit Profile

**Layout pattern:** Full-screen form (mobile) or centered card/modal (desktop). Grouped sections with save at bottom or per-section.

**Key components:**
- Profile photo upload/change (tap to change, crop tool)
- Cover photo upload/change
- Name field(s)
- Username/handle field (with availability check)
- Bio/description textarea (character count)
- Link/website field
- Location field
- Category/profession field (optional)
- Save button (sticky on mobile)
- Cancel/discard option
- Unsaved changes warning on navigation

**Information hierarchy:**
1. Visual identity (photos)
2. Core identity (name, username)
3. Description (bio, links)
4. Optional details
5. Save action

**States to handle:**
- **Clean (no changes):** Save button disabled
- **Dirty (changes made):** Save button enabled, warn on navigate away
- **Saving:** Button loading state
- **Username taken:** Inline error with suggestions
- **Photo uploading:** Progress indicator on avatar
- **Photo crop:** Modal overlay with crop tool
- **Validation error:** Inline per field (bio too long, invalid URL)
- **Success:** Return to profile with toast confirmation

**Accessibility requirements:**
- Photo upload: accessible button with `aria-label="Change profile photo"`
- Character count: `aria-live="polite"` or `aria-describedby` on textarea
- Username availability: announced via `aria-live`
- Unsaved changes dialog: focus trapped in confirmation dialog

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen, sections stacked, sticky save button at bottom
- Desktop: Modal or side panel, inline editing where possible

**Common mistakes:**
1. No unsaved changes warning (user loses edits by navigating away)
2. Photo crop tool that is not mobile-friendly
3. No character count on bio until limit exceeded

**Reference implementations:**
- **Instagram** — Simple form, photo tap-to-change, character limits clear
- **Twitter/X** — Modal edit, cover + avatar, bio + link fields
- **LinkedIn** — Section-based editing, comprehensive fields

---

## 17. Settings

**Layout pattern:** Grouped list of setting categories (desktop: sidebar navigation + detail panel; mobile: drill-down list). Settings organized by domain (Account, Notifications, Privacy, Appearance).

**Key components:**
- Category groups with headers
- Individual setting rows (label + current value/state + chevron or toggle)
- Toggle switches for on/off settings
- Drill-down for complex settings (notification preferences, privacy controls)
- Search within settings
- Account actions at bottom (log out, delete account — red/destructive styling)
- Breadcrumbs or back navigation for nested settings

**Information hierarchy:**
1. Category organization (find the right group)
2. Setting label + current value (understand current state)
3. Action (change the setting)
4. Destructive actions (clearly separated at bottom)

**States to handle:**
- **Default:** Current values displayed inline
- **Toggle changed:** Immediate save with brief feedback
- **Complex setting open:** Detail view/modal
- **Saving:** Per-setting loading indicator
- **Error saving:** Retry prompt per setting
- **Destructive action:** Confirmation dialog with consequences explained

**Accessibility requirements:**
- Toggles: `role="switch"` with `aria-checked`
- Group headings: proper heading hierarchy or `role="group"` with `aria-labelledby`
- Destructive actions: clearly labeled, confirmation dialog with focus trap
- Settings search: standard search box accessibility
- Current values announced with setting labels

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen list, drill-down navigation per category, back button
- Desktop: Sidebar + detail panel, settings searchable

**Common mistakes:**
1. Flat list with no grouping — overwhelming at scale
2. No search — users can not find the setting they need
3. No confirmation on destructive actions (log out, delete account)

**Reference implementations:**
- **iOS Settings** — Grouped list, drill-down, toggles, search at top
- **Slack** — Sidebar categories, detail panel, notification granularity
- **Notion** — Clean grouped settings, workspace vs. personal separation

---

## 18. Notifications

**Layout pattern:** Single-column list, reverse chronological. Grouped by time period (Today, Yesterday, This Week, Earlier). Unread indicator per item.

**Key components:**
- Notification items (icon/avatar + text + timestamp + unread dot)
- Group headers (time-based)
- "Mark all as read" action
- Filter tabs (All, Mentions, Reactions, System)
- Individual notification actions (mark read, dismiss, mute)
- Empty state ("No new notifications")
- Settings link ("Notification preferences")

**Information hierarchy per item:**
1. Unread indicator (is this new?)
2. Source (who/what generated this)
3. Action/content (what happened)
4. Timestamp (when)
5. Quick action (respond, dismiss)

**States to handle:**
- **Unread items:** Bold text, dot indicator, unread count in nav badge
- **All read:** Subtle state, "Mark all as read" hidden
- **Empty:** Friendly illustration + "No notifications yet"
- **Loading:** Skeleton list
- **Action required:** Highlighted notification (approval request, invitation)
- **Notification overflow:** Grouped ("Jane and 5 others liked your post")

**Accessibility requirements:**
- List items: `role="listitem"` or semantic list
- Unread state: conveyed via text ("unread") not just visual dot
- Timestamps: `<time>` element with full date
- "Mark all as read" button: clear `aria-label`, `aria-live` confirmation
- Dismissible notifications: dismiss button with `aria-label="Dismiss notification about [summary]"`

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen list, swipe actions (swipe to dismiss/mark read)
- Desktop: Dropdown panel from bell icon or full page

**Common mistakes:**
1. No grouping — hundreds of individual items in a flat list
2. No way to mark all as read
3. Notification text too vague ("Something happened in your project")

**Reference implementations:**
- **GitHub** — Filtered by type, unread/read sections, keyboard navigation
- **Slack** — Threaded notifications, channel grouping, mention highlighting
- **Instagram** — Social grouping ("X and Y liked your photo"), time sections

---

## 19. Chat / Messaging

**Layout pattern:** Two-panel on desktop (conversation list left 30%, chat view right 70%). Full-screen chat view on mobile with back to list. Messages in bubbles, alternating left/right alignment.

**Key components:**
- Conversation list (avatar, name, last message preview, timestamp, unread badge)
- Chat header (recipient name, avatar, status, actions)
- Message bubbles (sent right/blue, received left/gray)
- Text input + send button + attachment options
- Typing indicator ("Alex is typing...")
- Read receipts (delivered, read)
- Message timestamps (grouped by time)
- Media messages (images, files, voice notes)
- Optional: reactions, replies/threads, search in conversation

**Information hierarchy:**
1. Conversation list: who, last message, unread state
2. Active chat: messages in time order
3. Input area: compose and send
4. Message metadata: time, read status

**States to handle:**
- **Empty inbox:** "No conversations yet" + "Start a conversation" CTA
- **No messages in conversation:** "Say hello to [name]" prompt
- **Sending message:** Optimistic display with "sending" indicator
- **Message failed:** Error indicator with retry button
- **Typing indicator:** Animated dots, appears/disappears
- **New message while scrolled up:** "New messages" pill at bottom
- **Offline:** Queue messages, show offline banner
- **Media uploading:** Progress bar on media bubble

**Accessibility requirements:**
- Messages: `role="log"` container with `aria-live="polite"` for new messages
- Chat bubbles: `role="listitem"` with sender identification
- Input: `aria-label="Message [recipient name]"`
- Typing indicator: `aria-live="polite"` with text "Alex is typing"
- Media messages: alt text or file description
- Keyboard: Enter to send (or Shift+Enter for newline), documented behavior

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen conversation, swipe back to list, compact input bar
- Desktop: Side-by-side panels, rich input with formatting, drag-and-drop files

**Common mistakes:**
1. No offline message queuing (messages disappear on network loss)
2. Enter key behavior not documented (does Enter send or add newline?)
3. No way to search within conversation history

**Reference implementations:**
- **WhatsApp** — Clean bubbles, read receipts, media handling, end-to-end encryption
- **Slack** — Threaded replies, rich formatting, file sharing, search
- **iMessage** — Tapback reactions, typing indicators, seamless media

---

## 20. Activity Feed

**Layout pattern:** Single-column timeline with activity items. Each item shows who did what and when. Grouped by time period.

**Key components:**
- Activity items (avatar + action text + target + timestamp)
- Time group headers
- Activity type icons
- Filter by activity type
- "Load more" or infinite scroll
- Empty state: "No activity yet"

**Information hierarchy per item:**
1. Actor (who did this)
2. Action (what they did)
3. Object (what they acted on)
4. Timestamp (when)

**States to handle:**
- **Empty:** "No recent activity" + context about what would appear
- **Loading:** Skeleton items
- **Filtered empty:** "No [type] activity" + clear filter
- **Bulk activity:** Collapsed group ("12 team members joined")
- **Error loading:** Retry prompt

**Accessibility requirements:**
- Activity items as list items
- Timestamps as `<time>` elements
- Filter controls properly labeled
- Action text should form complete sentences readable by screen readers

**Mobile vs. desktop adaptation:**
- Mobile: Full-width, compact items
- Desktop: Constrained width (max 700px), more detailed items

**Common mistakes:**
1. Activity text is cryptic ("user_123 performed action on item_456")
2. No time grouping — hard to scan
3. No filtering — overwhelming for active projects

**Reference implementations:**
- **GitHub** — Repository activity feed, filtered by type, clear action text
- **Notion** — Page activity sidebar, who edited what
- **Asana** — Project activity, task-centric updates

---

## 21. Article / Content Detail

**Layout pattern:** Single column, reading-optimized (max-width 680px for text). Long-form with typographic hierarchy. Optional sidebar for table of contents (desktop).

**Key components:**
- Article title (H1)
- Author byline (avatar, name, date, reading time)
- Hero image with caption
- Body content (structured with H2/H3, paragraphs, images, blockquotes, code blocks)
- Social sharing buttons
- Related articles
- Comments section
- Save/bookmark button
- Reading progress indicator (subtle top bar)
- Table of contents (desktop sidebar or in-article)

**Information hierarchy:**
1. Title (what is this about)
2. Author + date + reading time (context and freshness)
3. Body content (the substance)
4. Engagement (comments, shares)
5. Related content (what to read next)

**States to handle:**
- **Loading:** Skeleton with image placeholder, text blocks
- **Full article:** Normal reading view
- **Paywalled:** Blurred/truncated content with subscription CTA
- **Offline cached:** Available offline indicator
- **Comments loading:** Separate loading state for comments section
- **Comments error:** "Couldn't load comments" with retry

**Accessibility requirements:**
- Proper heading hierarchy (H1 > H2 > H3, no skipping)
- Images with descriptive alt text
- Reading progress bar: `aria-hidden="true"` (decorative) or accessible
- Table of contents: `<nav aria-label="Table of contents">`
- Blockquotes: `<blockquote>` with `cite` attribute
- Code blocks: `<pre><code>` with language indicated

**Mobile vs. desktop adaptation:**
- Mobile: Full-width, comfortable reading typography (16-18px), bottom share bar
- Desktop: Centered column, table of contents sidebar, floating share buttons

**Common mistakes:**
1. Line length too wide (80+ characters per line — optimal is 60-75)
2. No reading time estimate
3. No "save for later" option

**Reference implementations:**
- **Medium** — Clean reading experience, progress bar, highlights, claps
- **Substack** — Long-form focused, comment section, email-first
- **Apple Newsroom** — Beautiful typography, hero images, minimal chrome

---

## 22. Media Viewer / Gallery

**Layout pattern:** Full-screen or near-full-screen modal/overlay. Dark background. Single media item with navigation arrows. Thumbnail strip below or side.

**Key components:**
- Full-size media display (image/video)
- Navigation arrows (previous/next)
- Thumbnail strip
- Close button (top-right)
- Zoom controls (pinch on mobile, scroll/buttons on desktop)
- Media info (title, description, date, camera info)
- Download button
- Share button
- Counter ("3 of 12")
- Optional: slideshow auto-play, edit button, EXIF data

**Information hierarchy:**
1. Media content (full focus)
2. Navigation (previous/next)
3. Close/exit
4. Metadata and actions

**States to handle:**
- **Loading:** Placeholder/blur-up while high-res loads
- **Zoomed in:** Pan functionality, zoom level indicator
- **Video:** Play controls, progress bar, volume, fullscreen
- **Error loading:** "Couldn't load this image" with retry
- **End of gallery:** Loop or disable navigation arrow

**Accessibility requirements:**
- `role="dialog"` or `role="img"` as appropriate
- Focus trapped within viewer when open
- All images: descriptive alt text
- Keyboard: Arrow keys for navigation, Escape to close
- Video: captions/subtitles when available
- Counter: `aria-label="Image 3 of 12"`

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen, swipe gesture navigation, pinch-to-zoom
- Desktop: Modal overlay, arrow key navigation, scroll-to-zoom

**Common mistakes:**
1. No keyboard navigation (arrow keys, escape)
2. Zoom only works on hover (not accessible on touch)
3. No loading state for large images (user sees nothing while waiting)

**Reference implementations:**
- **Google Photos** — Smooth transitions, gesture support, smart zoom
- **Unsplash** — Clean lightbox, download options, photographer info
- **Apple Photos (iOS)** — Native viewer, smooth animations, share sheet

---

## 23. Error Screen (404 / 500)

**Layout pattern:** Centered content with illustration. Minimal chrome, clear message, actionable next steps.

**Key components:**
- Error illustration or icon (branded, friendly tone)
- Error code (404 / 500) — visible but not dominant
- Human-friendly headline ("Page not found" not "HTTP 404")
- Explanation text (1-2 sentences)
- Primary CTA: "Go Home" or "Go Back"
- Search bar (for 404)
- Support/contact link
- Optional: popular links, recent pages

**Information hierarchy:**
1. What happened (headline)
2. Why (brief explanation)
3. What to do (CTAs)
4. Alternatives (search, popular pages)

**States to handle:**
- **404 (not found):** "This page doesn't exist" + search + popular pages
- **500 (server error):** "Something went wrong on our end" + retry + status page link
- **403 (forbidden):** "You don't have access" + login link or request access
- **503 (maintenance):** Estimated return time, status page link
- **Timeout:** "Taking too long" + retry button
- **Offline:** "You're offline" + cached content suggestion

**Accessibility requirements:**
- Error message as `<h1>` — most important content on page
- Navigation still accessible (header/footer remain)
- Search bar properly labeled
- Auto-focus on main content area
- Status code in `aria-label` or visible text

**Mobile vs. desktop adaptation:**
- Mobile: Simplified illustration, compact layout
- Desktop: Larger illustration, more suggested links

**Common mistakes:**
1. Generic "Error" with no explanation or next step
2. Removing all navigation (user is stranded)
3. Technical jargon ("HTTP 404 Not Found" with no plain language)

**Reference implementations:**
- **GitHub** — Branded 404 with parallax illustration, search bar
- **Slack** — Friendly animal illustrations, humor, helpful links
- **Notion** — Clean 404, search, recent pages list

---

## 24. Empty State

**Layout pattern:** Centered content within the parent container. Illustration + headline + description + CTA. Takes the place of where content would be.

**Key components:**
- Illustration or icon (contextual, not generic)
- Headline (what would be here)
- Description (why it is empty + what to do)
- Primary CTA (create first item, import, connect)
- Optional: secondary action, template/example to start from

**Information hierarchy:**
1. Visual context (illustration)
2. What this space is for
3. How to populate it
4. Action to take

**States to handle:**
- **First-time (never had content):** Educational + encouraging ("Create your first project")
- **Cleared (had content, now empty):** Acknowledge emptiness ("No items match your filters" or "All done!")
- **Error-caused empty:** "Couldn't load items" + retry (not a true empty state)
- **Permission-based empty:** "You don't have access to view items" + request access

**Accessibility requirements:**
- Illustration: `alt=""` if decorative, descriptive if meaningful
- Heading: proper heading level in context (not always H1)
- CTA: clearly labeled button
- Description should provide context that a screen reader user needs

**Mobile vs. desktop adaptation:**
- Mobile: Smaller illustration, concise text
- Desktop: Larger illustration, more detail in description

**Common mistakes:**
1. Completely blank area with no guidance (user thinks it's broken)
2. Generic illustration for every empty state (same sad-face everywhere)
3. No CTA — user sees it is empty but does not know how to fix it

**Reference implementations:**
- **Dropbox** — Contextual illustrations, drag-and-drop prompt, import options
- **Asana** — Unicorn celebration on empty inbox, project-specific empty states
- **Notion** — Template suggestions, quick-start guides

---

## 25. Onboarding Step

**Layout pattern:** Full-screen or modal overlay. Sequential steps with progress indicator. Illustration/demo + headline + description + primary CTA per step. Skippable.

**Key components:**
- Progress indicator (dots, bar, or step counter)
- Illustration, animation, or interactive demo
- Headline (benefit-oriented, not feature-oriented)
- Description (1-2 sentences)
- Primary CTA: "Next" or step-specific action
- Skip option ("Skip" text link or "Skip for now")
- Back option (previous step)
- Step counter ("2 of 5")

**Information hierarchy:**
1. Visual (illustration/demo)
2. Benefit statement (headline)
3. Supporting detail
4. Forward action
5. Skip/back options

**States to handle:**
- **First step:** No back button, prominent skip
- **Middle steps:** Back + forward + skip
- **Last step:** "Get Started" or "Done" instead of "Next"
- **Already completed:** Skip entire onboarding or show "welcome back" summary
- **Action required step:** Cannot proceed until action taken (e.g., choose interests)
- **Optional steps:** Clear "Skip" with no penalty

**Accessibility requirements:**
- Step indicator: `aria-label="Step 2 of 5: Choose your interests"`
- Illustration: decorative alt if not essential
- Keyboard: Tab through controls, Enter to proceed
- Skip link clearly labeled: `aria-label="Skip onboarding"`
- Content should make sense without illustrations (screen reader path)

**Mobile vs. desktop adaptation:**
- Mobile: Full-screen, swipe between steps, dots at bottom
- Desktop: Centered card or modal, more detailed illustrations

**Common mistakes:**
1. Cannot skip (forcing users through irrelevant setup)
2. Too many steps (5 max, ideally 3-4)
3. Feature-focused instead of benefit-focused ("Feature X does Y" vs. "Achieve Y with Feature X")

**Reference implementations:**
- **Duolingo** — Interactive onboarding, choose language, immediate mini-lesson
- **Notion** — Use-case selection, workspace setup, template recommendations
- **Slack** — Channel joining, teammate inviting, purpose-driven setup

---

## 26. Pricing / Plans

**Layout pattern:** Horizontal card layout (2-4 plans side by side on desktop, horizontal scroll or stacked on mobile). Feature comparison table below. Recommended plan highlighted.

**Key components:**
- Plan cards (plan name, price, billing period, feature list, CTA)
- Recommended/popular badge on one plan
- Billing toggle (monthly/annual with savings shown)
- Feature comparison table (checkmarks per plan)
- FAQ section
- Enterprise/custom plan CTA
- Money-back guarantee badge
- Optional: social proof, customer logos

**Information hierarchy:**
1. Plan options (what are my choices)
2. Pricing (what does each cost)
3. Key differentiators (what's different between plans)
4. CTA per plan
5. Detailed comparison (for careful evaluation)
6. Trust signals

**States to handle:**
- **Unauthenticated visitor:** Full pricing display, CTAs go to signup
- **Free user:** Current plan indicated, upgrade CTAs on others
- **Paid user:** Current plan indicated, upgrade/downgrade options
- **Annual toggle:** Prices update dynamically, savings highlighted
- **Enterprise inquiry:** Contact form or meeting scheduler

**Accessibility requirements:**
- Billing toggle: `role="switch"` or `role="radiogroup"`
- Comparison table: proper `<table>` with `<th>` headers, `scope` attributes
- Checkmarks: `aria-label="Included"` or text equivalent (not just icon)
- Recommended plan: visual highlight + `aria-label` indicating recommended
- Price changes on toggle: `aria-live` for dynamic price updates

**Mobile vs. desktop adaptation:**
- Mobile: Stacked cards or horizontal carousel, comparison table with sticky first column
- Desktop: Side-by-side cards, full comparison table visible

**Common mistakes:**
1. Feature comparison table with only checkmarks and no explanations
2. Annual savings not prominently shown
3. No indication of current plan for existing users

**Reference implementations:**
- **Stripe** — Clean pricing cards, transparent feature comparison, enterprise option
- **Notion** — Clear plan differentiation, generous free tier explained
- **Linear** — Simple two-plan layout, feature comparison, startup program mention

---

## 27. Admin / Data Table

**Layout pattern:** Full-width table with toolbar above. Sidebar navigation for admin sections. Bulk actions on selection. Responsive strategy: horizontal scroll or card view on mobile.

**Key components:**
- Data table with sortable column headers
- Search/filter bar above table
- Column visibility controls
- Bulk action toolbar (appears on selection)
- Row actions menu (edit, delete, duplicate)
- Pagination controls (rows per page, page navigation)
- Checkbox column for multi-select
- Status badges in cells
- Export button (CSV, PDF)
- "Add new" CTA
- Optional: inline editing, drag-to-reorder rows, saved views/filters

**Information hierarchy:**
1. Table content (data)
2. Search + filters (find specific data)
3. Bulk actions (act on selected)
4. Row actions (act on individual)
5. Pagination (navigate data set)

**States to handle:**
- **Loading:** Skeleton table rows (match column count)
- **Empty table:** "No [items] yet" + "Add first [item]" CTA
- **Filtered empty:** "No results match your filters" + "Clear filters"
- **Selection active:** Bulk action bar appears, selected count shown
- **Inline editing:** Cell becomes editable on click, save on blur/enter
- **Delete confirmation:** "Delete 5 items?" dialog with consequences
- **Sort active:** Column header shows sort direction indicator
- **Error loading:** Retry prompt
- **Large dataset:** Virtual scrolling or pagination

**Accessibility requirements:**
- `<table>` with `<thead>`, `<tbody>`, `<th scope="col">`
- Sortable headers: `aria-sort="ascending"`, `"descending"`, or `"none"`
- Selection checkboxes: `aria-label="Select [row identifier]"`
- Bulk action count: `aria-live` for "5 items selected"
- Row actions: accessible dropdown menu, keyboard navigable
- Pagination: `aria-label` on navigation, current page announced

**Mobile vs. desktop adaptation:**
- Mobile: Horizontal scroll with sticky first column, or card view per row, simplified columns
- Desktop: Full table, all columns visible, hover row highlighting
- Tablet: Selected important columns, expandable row for full details

**Common mistakes:**
1. No responsive strategy — table breaks on mobile
2. No keyboard navigation through cells and rows
3. Bulk delete without confirmation dialog

**Reference implementations:**
- **Airtable** — Spreadsheet-like table, inline editing, multiple views, rich filtering
- **Stripe Dashboard** — Clean data tables, search + filters, export, pagination
- **Notion Database** — Multiple views (table, board, list), inline editing, filtering

---

## Quick Reference Matrix

| Screen Type | Primary Layout | Key Pattern | Critical State |
|-------------|---------------|-------------|----------------|
| Welcome | Full-bleed centered | Value prop + dual CTA | First launch vs. returning |
| Login | Centered card | Social + email/password | Error without revealing info |
| Signup | Centered/split | Progressive disclosure | Email taken, weak password |
| Password Reset | Multi-step card | Email > confirm > reset | Security (don't reveal email existence) |
| Dashboard | Grid + sidebar | KPI cards + activity | First-time empty state |
| Feed | Single column scroll | Infinite scroll + compose | End of feed, new items indicator |
| Search | Search bar + results | Zero state + autocomplete | No results with guidance |
| PLP | Grid + filters | Product cards + sort/filter | Filtered to zero |
| PDP | Split (images + details) | Gallery + variants + CTA | Out of stock, variant switching |
| Cart | List + summary sidebar | Item rows + order total | Empty cart, price changes |
| Checkout | Simplified multi-step | Express pay + form | Payment declined |
| Confirmation | Centered celebration | Order number + ETA | Guest vs. authenticated |
| Tracking | Timeline + map | Status progress + live tracking | Delayed, exception |
| Profile (own) | Header + tabs | Avatar + stats + content | Incomplete profile |
| Profile (public) | Header + follow CTA | Follow/message + content | Follow states |
| Edit Profile | Form | Photo upload + fields | Unsaved changes warning |
| Settings | Grouped list | Categories + toggles | Destructive actions |
| Notifications | Chronological list | Unread + grouped | Empty, overflow grouping |
| Chat | Two-panel | Bubble messages + input | Offline, failed send |
| Activity Feed | Timeline list | Actor + action + object | Bulk activity grouping |
| Article | Reading column | Typography + TOC | Paywalled content |
| Media Viewer | Fullscreen overlay | Gallery + zoom | Loading large media |
| Error (404/500) | Centered | Friendly message + next steps | Different error types |
| Empty State | Centered in context | Illustration + CTA | First-time vs. cleared |
| Onboarding | Full-screen steps | Progress + benefits + skip | Required vs. optional steps |
| Pricing | Horizontal cards | Plan comparison + toggle | Current plan indication |
| Admin Table | Full-width table | Sort + filter + bulk actions | Mobile responsiveness |

---

## Screen Type Taxonomy (32 types)


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
