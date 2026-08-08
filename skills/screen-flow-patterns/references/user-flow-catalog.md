# User Flow Catalog — 15 User Flows with Step Patterns

> For each flow: step sequence, decision points, error handling per step, cognitive load management, emotional arc, metric targets, drop-off prevention, and 3 best-in-class references.

---

## 1. Authentication Flow (Login / Signup / Reset)

**Step sequence:**
1. **Entry point** — User taps "Log In" or "Sign Up" (or is redirected from a protected resource)
2. **Method selection** — Social auth buttons (Google, Apple, SSO) + email option displayed
3a. **Social auth path** — Redirect to provider > consent screen > redirect back with token
3b. **Email path — Login** — Enter email > enter password > submit > validate > redirect to app
3c. **Email path — Signup** — Enter email > enter name + password > accept terms > submit > verify email
3d. **Reset path** — Enter email > receive link > enter new password > confirm > redirect to login
4. **Post-auth** — Redirect to intended destination or home/dashboard

**Decision points and branching:**
- Does the user have an account? (Login vs. Signup — smart detection: enter email, system detects if account exists and routes accordingly)
- Social or email? (Show social options prominently — fewer steps)
- MFA required? (Branch to OTP/authenticator step after password)
- Email verified? (Branch to verification step if not)

**Error handling per step:**
- Step 2 (social auth): Provider unavailable — show error, offer email fallback
- Step 3b (login): Wrong credentials — "Incorrect email or password" (never specify which). After 5 attempts: temporary lockout with timer
- Step 3c (signup): Email taken — "Account exists. Log in or reset password?" with inline links
- Step 3c (signup): Weak password — Real-time strength meter with checklist
- Step 3d (reset): Link expired — "This link has expired. Request a new one." with one-tap action

**Cognitive load management:**
- Single-column, one task per screen
- Smart defaults (remember last-used auth method)
- Email-first flow: ask for email, determine login vs. signup automatically
- Defer optional fields (birthday, phone) to post-signup

**Emotional arc:**
- Start: Neutral/purposeful (user wants to get in)
- Middle: Slight friction (entering credentials)
- Peak tension: Waiting for validation
- Resolution: Satisfaction on successful entry
- End feeling: Relief + anticipation for what's inside

**Metric targets:**
- Login completion rate: >95%
- Signup completion rate: >70%
- Password reset completion: >60%
- Time to complete login: <15 seconds
- Time to complete signup: <45 seconds
- Social auth adoption: >40% of signups

**Drop-off prevention strategies:**
- Step 1: Show social auth (fewer fields = lower friction)
- Step 3b: Don't clear password on error
- Step 3c: Inline validation, real-time feedback, minimal fields
- Step 3d: "Open email app" deep link, resend with cooldown

**Best-in-class references:**
- **Slack** — Magic link option, workspace-aware routing, Google SSO prominence
- **Stripe** — Email-first smart routing, clean error messages, MFA support
- **Notion** — Google + Apple SSO, magic link, seamless workspace switching

---

## 2. Onboarding Flow (First-Run Experience)

**Step sequence:**
1. **Welcome** — Greeting + value proposition + "Get Started" CTA
2. **Personalization** — Select use case, role, or interests (1-3 choices)
3. **Configuration** — Set up key preferences (name workspace, invite team, choose theme)
4. **Quick win** — Guided first action (create first item, send first message, complete a mini-task)
5. **Completion** — Celebration moment + overview of what's available + "Explore" CTA

**Decision points and branching:**
- Solo user vs. team? (Skip invite step for solo)
- Use case selection determines which features to highlight
- Has data to import? (Offer import step or skip)
- Mobile vs. desktop? (Adjust step complexity)

**Error handling per step:**
- Step 2: No selection made — Allow "I'm not sure" option or "Decide later"
- Step 3: Invite emails invalid — Inline validation, allow skip
- Step 4: First action fails — Provide fallback guided path, "Try again" or "Skip for now"
- Any step: App crash — Resume from last completed step on re-launch

**Cognitive load management:**
- Maximum 3-5 steps (research shows >5 steps = significant drop-off)
- One decision per step
- Progressive disclosure — don't show everything at once
- Visual progress indicator (dots or fraction)
- Allow skipping every non-critical step

**Emotional arc:**
- Start: Excitement (new tool, new possibilities)
- Middle: Engaged (personalization feels tailored to me)
- Peak: Achievement (first quick win — "You created your first project!")
- End: Empowered (I know enough to continue on my own)

**Metric targets:**
- Onboarding completion rate: >80%
- Time to first value: <3 minutes
- Day-1 retention (completed onboarding): >60%
- Skip rate per step: <30% (if higher, step may be unnecessary)
- Activation rate (users who complete quick win): >50%

**Drop-off prevention strategies:**
- Step 1: Make the value clear, not generic
- Step 2: Limited choices (3-6 options), visual selection (cards not dropdowns)
- Step 3: Smart defaults so users can "Accept and continue" without deciding
- Step 4: Make the quick win genuinely useful, not a dummy task
- Throughout: Always show skip option, save progress

**Best-in-class references:**
- **Duolingo** — Interactive from step 1 (pick language, try a lesson), hooks you before signup
- **Notion** — Use-case selection, workspace setup, template library, quick page creation
- **Figma** — Guided tutorial with interactive canvas, team setup, first file creation

---

## 3. Checkout / Purchase Flow

**Step sequence:**
1. **Cart review** — Confirm items, quantities, remove/edit. "Proceed to Checkout."
2. **Express checkout offer** — Apple Pay / Google Pay / PayPal one-tap (above fold)
3. **Contact info** — Email (for guest) or auto-filled (for logged-in users)
4. **Shipping** — Address (with autocomplete), shipping method selection
5. **Payment** — Card details (with saved card option), billing address (same as shipping toggle)
6. **Review** — Full order summary: items + shipping + tax + total + edit links per section
7. **Confirmation** — "Place Order" > processing > success page with order number

**Decision points and branching:**
- Guest vs. logged-in? (Skip contact for logged-in, auto-fill address)
- Digital vs. physical product? (Skip shipping for digital)
- Single shipping method? (Auto-select, skip method choice)
- Express checkout? (Skip steps 3-6, go straight to confirmation)
- Promo code? (Inline in cart or checkout, not a separate step)

**Error handling per step:**
- Step 1: Item out of stock since added — Alert banner on item with "Remove" or "Save for later"
- Step 4: Address unverifiable — "Did you mean...?" suggestion with original option
- Step 5: Card declined — "Payment declined. Try another card." (never reveal why to user)
- Step 5: Card expired — "This card has expired. Update or use another."
- Step 7: Processing timeout — "Still processing... don't refresh" with timeout fallback
- Any step: Session timeout — Save cart, allow resumption

**Cognitive load management:**
- One concern per step (shipping, then payment — never combined)
- Progress indicator always visible
- Order summary always visible or easily accessible (sidebar desktop, collapsible mobile)
- Auto-fill everything possible (address, card, email)
- Minimize form fields (country auto-detect from IP, phone only if required for shipping)

**Emotional arc:**
- Start: Anticipation (I'm getting something I want)
- Cart review: Slight doubt (Is this right? Should I remove something?)
- Shipping/payment: Friction (tedious but necessary)
- Review: Confidence (everything looks correct)
- Place order: Commitment (slight tension)
- Confirmation: Delight (celebration, anticipation of delivery)

**Metric targets:**
- Cart-to-checkout rate: >60%
- Checkout completion rate: >65%
- Cart abandonment rate: <70%
- Time to complete checkout: <3 minutes
- Express checkout adoption: >20%
- Payment error rate: <5%

**Drop-off prevention strategies:**
- Step 1: Show shipping estimate in cart, no surprises at checkout
- Step 2: Express checkout reduces flow to one tap
- Step 3: Auto-detect email from browser, minimal fields
- Step 4: Address autocomplete (Google Places API), saved addresses
- Step 5: Saved payment methods, trust badges visible
- Step 6: Clear itemization, no hidden fees
- Throughout: Guest checkout always available, never require account creation

**Best-in-class references:**
- **Shopify Checkout** — Industry benchmark, optimized for conversion, express pay prominent
- **Apple Store** — Minimal steps for signed-in users, clean summary, Apple Pay integration
- **Amazon** — 1-Click ordering, saved everything, Prime integration

---

## 4. Booking / Reservation Flow

**Step sequence:**
1. **Search** — Enter destination/service, dates, guests/quantity
2. **Browse results** — List/map view with filters (price, rating, amenities)
3. **Select option** — View details, photos, reviews, availability
4. **Configure** — Select specific room/table/time, add-ons or extras
5. **Guest info** — Name, contact details, special requests
6. **Payment** — Confirm total (with breakdown), enter payment
7. **Confirmation** — Booking confirmed + calendar add + directions + cancellation policy

**Decision points and branching:**
- Flexible dates? (Show price calendar / cheapest day highlights)
- Multiple options selected for comparison? (Side-by-side view)
- Requires deposit vs. full payment? (Different payment messaging)
- Cancellation policy type? (Free vs. partial refund — shown before payment)
- Repeat booking? (Auto-fill from history)

**Error handling per step:**
- Step 1: Dates unavailable — Show nearby available dates
- Step 3: Option no longer available — "This option was just booked" + similar options
- Step 4: Time slot taken while user decides — Real-time availability update + alternatives
- Step 6: Payment fails — Clear retry, preserve all entered data
- Step 7: Double-booking detected — Immediate notification + rebooking assistance

**Cognitive load management:**
- Search: Smart defaults (tonight, 2 guests, nearby)
- Results: Map + list view, not overwhelming filter count
- Configuration: Calendar with color-coded availability
- Progressive price revelation (show total before payment step)

**Emotional arc:**
- Start: Excitement (planning something enjoyable)
- Search: Anticipation (exploring options)
- Selection: Joy (found the one!)
- Configuration: Practical (setting details)
- Payment: Brief anxiety (spending money)
- Confirmation: Relief + excitement (it's real, it's happening!)

**Metric targets:**
- Search to results: >90% (search must always return something)
- Results to selection: >30%
- Selection to booking: >50%
- Overall conversion: >10%
- Time to complete booking: <5 minutes
- Cancellation rate within 24h: <15%

**Drop-off prevention strategies:**
- Step 1: Flexible date selection, smart suggestions
- Step 2: Save/favorite options for comparison
- Step 3: "Only 2 left at this price" scarcity (if honest)
- Step 4: Show total including all fees before payment
- Step 6: Multiple payment options, split payment for groups
- Post-booking: Easy calendar integration, share with travel companions

**Best-in-class references:**
- **Airbnb** — Map + list, clear pricing, flexible dates calendar, instant book vs. request
- **OpenTable** — Quick time-slot selection, party size, real-time availability
- **Booking.com** — Price calendar, free cancellation prominence, urgency signals

---

## 5. Search & Filter Flow

**Step sequence:**
1. **Initiate search** — Tap search bar or icon, keyboard opens
2. **Type query** — Real-time suggestions appear (autocomplete, recent, trending)
3. **Submit or select suggestion** — Results page loads
4. **Scan results** — Evaluate results, adjust if needed
5. **Apply filters** — Narrow results by category, price, date, etc.
6. **Sort results** — Change order (relevance, price, date, popularity)
7. **Select result** — Navigate to detail view
8. **Return to results** — Back button preserves filters and scroll position

**Decision points and branching:**
- Autocomplete selection vs. full search? (Direct navigation vs. results page)
- No results? (Spelling suggestions, broader alternatives, category browse)
- Too many results? (Prompt filter use)
- Voice search? (Transcription > results)

**Error handling per step:**
- Step 2: No suggestions — Show recent searches + categories
- Step 3: Search timeout — "Search is taking longer than usual" + retry
- Step 4: Zero results — Spelling correction, synonym suggestions, category browse
- Step 5: Filters + query = zero results — "No matches. Remove some filters?" with clear-all
- Step 8: Results expired/changed — Refresh with maintained position

**Cognitive load management:**
- Limit autocomplete to 5-8 suggestions
- Progressive filter disclosure (most-used first, "More filters" expandable)
- Active filter count badge on filter button
- Result count updates in real-time as filters are applied
- "Clear all" always accessible

**Emotional arc:**
- Start: Intent (I know what I'm looking for)
- Typing: Anticipation (will it be here?)
- Results: Relief (found it) or frustration (didn't find it)
- Filtering: Control (narrowing to exactly what I need)
- Selection: Satisfaction (this is the one)

**Metric targets:**
- Search exit rate: <20% (users leaving search without selecting a result)
- Autocomplete usage: >50%
- Filter usage: >30%
- Zero-result rate: <5%
- Time from search to selection: <30 seconds
- Results per page viewed: <2 (users find what they need on page 1)

**Drop-off prevention strategies:**
- Step 2: Autocomplete reduces effort, recent searches reduce re-typing
- Step 4: Highlighted search terms in results
- Step 5: Filters don't require page reload (instant)
- Step 8: Preserve scroll position and filters on back navigation

**Best-in-class references:**
- **Spotify** — Instant results, category-based zero state, recent searches
- **Airbnb** — Dynamic map + list, filter chips, smart suggestions
- **Google** — Autocomplete, "Did you mean...", knowledge panel, filtered tabs

---

## 6. Content Creation Flow

**Step sequence:**
1. **Initiate** — "New" button, "+" FAB, or keyboard shortcut
2. **Choose type** — Select content type (post, document, story, photo, video)
3. **Create/compose** — Editor/composer appropriate to type (text, media, mixed)
4. **Enhance** — Add media, format text, tag people, add location, apply filters
5. **Preview** — View final output as audience will see it
6. **Configure** — Set audience/visibility, schedule, category/tags
7. **Publish** — Submit > processing > live confirmation

**Decision points and branching:**
- Content type determines editor (rich text, image, video, code)
- Draft or publish? (Save draft at any point)
- Schedule or publish now? (Date/time picker vs. immediate)
- Audience selection? (Public, private, specific group)

**Error handling per step:**
- Step 3: Auto-save failure — Retry silently, show warning icon if persistent, local storage backup
- Step 4: Media upload failure — Per-item retry button, continue composing while upload retries
- Step 5: Preview fails to render — "Preview unavailable" with "Publish anyway" option
- Step 7: Publish failure — Save as draft, show error, retry option

**Cognitive load management:**
- Start with blank canvas, progressive toolbar (basic formatting visible, advanced in menus)
- Auto-save every 30 seconds + on significant changes
- Media uploads happen in background with progress indicators
- Preview is optional, not a required step
- Publish settings have smart defaults (public, now, no tags)

**Emotional arc:**
- Start: Inspiration (I have something to share)
- Composing: Flow state (creative engagement)
- Enhancing: Crafting (making it look good)
- Preview: Evaluation (is this ready?)
- Publish: Commitment + pride (it's out there)
- Post-publish: Anticipation (will people engage?)

**Metric targets:**
- Creation started to published: >40%
- Draft save rate: >90% (auto-save must work reliably)
- Time to first publish (new users): <5 minutes
- Media upload success rate: >98%
- Average creation session length: 3-10 minutes (depends on type)

**Drop-off prevention strategies:**
- Step 1: Obvious entry point (FAB, prominent "New" button)
- Step 3: Auto-save eliminates "I forgot to save" anxiety
- Step 4: Drag-and-drop for media, paste support for images
- Step 6: Smart defaults mean users can skip configuration entirely
- Throughout: Draft accessible from anywhere (drafts list/indicator)

**Best-in-class references:**
- **Notion** — Slash commands, block-based editor, real-time collab, templates
- **Instagram** — Simple media selection > filter > caption > publish pipeline
- **Medium** — Distraction-free writing, drag media, publish settings last

---

## 7. Profile Editing Flow

**Step sequence:**
1. **Enter edit mode** — Tap "Edit Profile" from profile page
2. **Review current info** — See all editable fields with current values
3. **Update fields** — Modify desired fields (name, bio, links, location)
4. **Update photos** — Tap avatar/cover to change (camera, library, or remove)
5. **Crop/adjust** — Crop tool for photos (circle crop for avatar, banner crop for cover)
6. **Save** — Tap "Save" > validation > confirmation > return to profile

**Decision points and branching:**
- Single save or per-section save? (Single for simple profiles, per-section for complex)
- Photo source: Camera, photo library, or remove current?
- Username change: Availability check, consequences warning (old links may break)

**Error handling per step:**
- Step 3: Username taken — Inline "taken" indicator + suggestions
- Step 3: Bio exceeds character limit — Counter turns red, save blocked
- Step 4: Photo upload fails — Retry without losing text changes
- Step 5: Crop tool crash — Fall back to uncropped version
- Step 6: Save fails — Preserve all changes locally, retry option
- Navigation away: "Discard changes?" confirmation dialog

**Cognitive load management:**
- Show all editable fields on one scrollable page
- Current values pre-filled (no blank starting point)
- Character counters visible from the start, not just at the limit
- Photo crop is a focused modal (one task at a time)
- Dirty state detection: only warn on actual changes

**Emotional arc:**
- Start: Intent (I want to update my identity)
- Editing: Control (crafting my public image)
- Photo update: Self-expression (choosing how I look)
- Save: Satisfaction (profile is updated)

**Metric targets:**
- Edit initiated to saved: >80%
- Photo update rate: >30% of edit sessions
- Time to complete: <2 minutes
- Validation error rate: <10%

**Drop-off prevention strategies:**
- Pre-filled fields reduce effort to minimal changes
- Auto-save on navigate away (optional, with user preference)
- Photo crop that works on mobile (touch gestures, not mouse-only)
- Clear feedback on what has changed vs. what is saved

**Best-in-class references:**
- **Instagram** — Simple form, tap-to-change photo, inline previews
- **LinkedIn** — Section-based editing, photo cropping, rich fields
- **Twitter/X** — Modal overlay, cover + avatar update, character counters

---

## 8. Settings Management Flow

**Step sequence:**
1. **Enter settings** — Tap settings icon/menu item from profile or navigation
2. **Browse categories** — Scan grouped settings (Account, Notifications, Privacy, Appearance, etc.)
3. **Select category** — Drill into category to see individual settings
4. **Modify setting** — Toggle switch, select option, or drill deeper
5. **Confirm changes** — Auto-save on toggle, or explicit save for forms
6. **Return** — Back to category list or settings root

**Decision points and branching:**
- Simple toggle? (Immediate save, no confirmation needed)
- Complex setting? (Opens sub-page or modal with options)
- Destructive action? (Confirmation dialog required)
- Requires verification? (Password/biometric for security settings)

**Error handling per step:**
- Step 2: Settings fail to load — "Couldn't load settings. Try again." with retry
- Step 4: Toggle fails to save — Revert toggle with error message
- Step 4: Verification fails — "Incorrect password. Try again." (don't reset the setting change)
- Step 5: Save fails on form — Preserve entries, show retry

**Cognitive load management:**
- Group settings into 5-8 categories maximum
- Most-changed settings easily accessible (appearance, notifications)
- Settings search for large settings pages
- Show current value inline (not hidden behind a tap)
- Use toggles for binary choices (not checkboxes)

**Emotional arc:**
- Start: Purposeful (I need to change something specific)
- Browsing: Scanning (where is the thing I need?)
- Found it: Relief (there it is)
- Changed it: Satisfaction (setting updated)
- This is a utility flow — emotional peaks are minimal, but frustration from not finding settings is high

**Metric targets:**
- Settings search usage: >20% (indicates large settings, search is essential)
- Time to find specific setting: <20 seconds
- Settings change completion: >90%
- Support tickets about settings: <5% of all tickets

**Drop-off prevention strategies:**
- Settings search eliminates browsing friction
- Inline descriptions for ambiguous settings
- Confirmation for destructive actions (delete, logout) but not for toggles
- Undo option for toggles (brief "Undo" toast)

**Best-in-class references:**
- **iOS Settings** — Category groups, search, consistent toggle/drill-down pattern
- **Slack** — Sidebar categories, rich notification preferences, workspace separation
- **Discord** — Left sidebar categories, escape to close, per-server settings

---

## 9. Subscription / Upgrade Flow

**Step sequence:**
1. **Discover upgrade** — Feature gate, pricing page, upgrade prompt in-app
2. **Compare plans** — View plan differences, features, pricing
3. **Select plan** — Choose plan + billing cycle (monthly/annual)
4. **Payment** — Enter or confirm payment method
5. **Confirm** — Review selection + price + billing terms
6. **Activate** — Processing > success > feature unlocked celebration
7. **Post-activation** — Tour of new features, highlight what's now available

**Decision points and branching:**
- Monthly vs. annual? (Annual savings clearly shown)
- Upgrade vs. downgrade? (Different messaging and timing)
- Free trial available? (Trial > plan selection > payment at trial end)
- Team vs. individual? (Seat count + billing owner)
- Promo code? (Apply before payment)

**Error handling per step:**
- Step 3: Plan unavailable — "This plan is no longer available" + alternative
- Step 4: Payment declined — Clear message, alternative method, retry
- Step 4: Card requires 3D Secure — Redirect to bank verification, return to app
- Step 5: Price changed since viewing — Clear disclosure, option to proceed or cancel
- Step 6: Activation fails — "Payment processed, features activating shortly" + support contact

**Cognitive load management:**
- Maximum 3-4 plans to compare (not 7)
- Highlight recommended plan visually
- Annual savings shown as both percentage and absolute amount
- Feature comparison: lead with what the user gains, not what others get
- One-tap upgrade for returning users with saved payment

**Emotional arc:**
- Start: Desire/frustration (I want this feature / I hit a limit)
- Comparing: Evaluation (is it worth it?)
- Selecting: Commitment (I'm going for it)
- Payment: Slight anxiety (spending money)
- Activation: Delight (new features unlocked, celebration)
- Post-activation: Empowered (I can do more now)

**Metric targets:**
- Upgrade page to plan selection: >50%
- Plan selection to payment: >70%
- Payment to activation: >90%
- Trial-to-paid conversion: >25%
- Churn rate (monthly): <5%
- Annual plan adoption: >40%

**Drop-off prevention strategies:**
- Step 1: Feature gates show what you'd get (preview, not just a lock icon)
- Step 2: Most popular plan highlighted with social proof
- Step 3: Annual savings clearly shown (save $X per year)
- Step 4: Saved payment methods, Apple Pay / Google Pay
- Step 5: Money-back guarantee or free trial reassurance
- Post-activation: Immediate value demonstration

**Best-in-class references:**
- **Spotify** — Clear free vs. premium comparison, trial offer, family plan
- **Notion** — Generous free tier, clear feature gates, team pricing clarity
- **Linear** — Simple pricing, per-seat billing, immediate feature access

---

## 10. Social Sharing Flow

**Step sequence:**
1. **Trigger** — Tap share button/icon on content
2. **Share sheet** — OS share sheet (iOS/Android) or custom modal with sharing options
3. **Select destination** — Choose platform/method (copy link, Twitter, WhatsApp, email, etc.)
4. **Compose** — Add message/caption to shared content (pre-filled with smart defaults)
5. **Send/post** — Submit to destination platform
6. **Confirmation** — "Shared!" toast or visual feedback

**Decision points and branching:**
- Native share sheet vs. custom? (Native for broad reach, custom for curated options)
- Content type: link, image, text, or rich preview?
- Direct message vs. public post? (Different compose experience)
- Copy link fallback? (Always include as first option)

**Error handling per step:**
- Step 2: Share sheet fails to load — Fallback to "Copy link" with confirmation
- Step 3: Platform not installed — Redirect to web version or skip
- Step 5: Post fails — Save draft on destination platform, retry prompt
- Step 5: Authentication expired on destination — Re-auth prompt, then retry

**Cognitive load management:**
- Most-used sharing targets at the top (personalized over time)
- Smart pre-fill: relevant text, image, and link already composed
- One tap for "Copy link" (no compose step needed)
- Recent contacts for direct sharing

**Emotional arc:**
- Start: Enthusiasm (I want to share this!)
- Share sheet: Brief decision (where do I share?)
- Compose: Personalization (adding my take)
- Send: Satisfaction (shared with my network)

**Metric targets:**
- Share button to share complete: >40%
- Copy link usage: >30% of shares
- Share-to-engagement ratio: >5% (shared content gets engagement)
- Time to complete share: <15 seconds

**Drop-off prevention strategies:**
- Step 2: Minimize steps — one tap for copy link, two taps for platform share
- Step 4: Pre-fill with smart excerpt, user just has to tap "Post"
- Throughout: Share button in consistent, discoverable location

**Best-in-class references:**
- **iOS Share Sheet** — Native integration, AirDrop, recent contacts, copy
- **Instagram Stories** — Share to story with sticker, mention, and link overlay
- **Spotify** — Share track/playlist with rich preview card

---

## 11. Messaging / Chat Flow

**Step sequence:**
1. **Open conversations** — View conversation list (inbox)
2. **Select or start** — Tap existing conversation or "New Message"
3. **Find recipient** (new) — Search contacts/directory, select recipient(s)
4. **Compose** — Type message in input field
5. **Enhance** (optional) — Attach media, add emoji/sticker, format text
6. **Send** — Tap send button or press Enter
7. **Await response** — Typing indicator, read receipt, notification for reply

**Decision points and branching:**
- New conversation vs. existing? (Different entry point)
- 1:1 vs. group? (Group requires name, member management)
- Text vs. media? (Camera, gallery, file, voice note attachment flow)
- Reaction vs. reply? (Quick emoji reaction vs. typed response)

**Error handling per step:**
- Step 3: Recipient not found — "Invite to join" option
- Step 4: Lost connection while typing — Save draft locally, sync when online
- Step 5: Media upload fails — Show failed upload with retry per item
- Step 6: Send fails — "Not sent" indicator on message with retry tap
- Step 7: Connection lost — Queue outgoing messages, show offline banner

**Cognitive load management:**
- Conversation list sorted by recent activity
- Search across conversations and contacts in one search
- Rich media preview before sending (not after)
- Threaded replies to reduce conversation noise
- Pinned conversations for important chats

**Emotional arc:**
- Start: Social intent (I want to connect)
- Composing: Expression (crafting my message)
- Sent: Anticipation (waiting for response)
- Response received: Connection (conversation flowing)

**Metric targets:**
- Message send success rate: >99%
- Time to send first message (new user): <60 seconds
- Media attachment success rate: >95%
- Daily active messaging users: benchmark varies by app type
- Response time (p50): <5 minutes for active conversations

**Drop-off prevention strategies:**
- Optimistic sending (show message immediately, sync in background)
- Auto-save drafts
- Push notifications for replies
- Typing indicators create social obligation to wait/respond

**Best-in-class references:**
- **WhatsApp** — Reliable delivery, media handling, voice notes, end-to-end encryption
- **iMessage** — Tapback reactions, effects, seamless media, rich links
- **Slack** — Threads, channels, search, rich formatting, integrations

---

## 12. File Upload Flow

**Step sequence:**
1. **Initiate** — Click/tap upload button, or drag file over drop zone
2. **Select files** — OS file picker, camera, or drag-and-drop
3. **Preview** — Show file thumbnails/names, size, format validation
4. **Configure** — Set file options (rename, add description, choose folder/destination)
5. **Upload** — Progress bar per file, overall progress
6. **Complete** — Success confirmation, file now available in destination

**Decision points and branching:**
- Single or multiple files? (Multi-select support)
- File too large? (Compression offer or rejection with size limit shown)
- Wrong format? (Clear error + accepted formats list)
- Resume interrupted upload? (Chunked upload with resume capability)
- Cloud source? (Google Drive, Dropbox integration as alternative to local)

**Error handling per step:**
- Step 2: No file selected (cancel) — Return to previous state
- Step 3: Invalid format — Per-file error "PDF, JPG, PNG accepted" with clear icon
- Step 3: File too large — "Max 25MB. This file is 40MB." + compress option if applicable
- Step 5: Upload fails mid-way — "Upload interrupted" + resume/retry button, don't lose progress
- Step 5: Network timeout — Pause and auto-resume when connected
- Step 6: Server processing fails — "Upload complete, processing failed. We'll notify you when ready."

**Cognitive load management:**
- Drag-and-drop as primary method (visual drop zone)
- File format restrictions shown before upload, not after failure
- Background upload so user can continue working
- Per-file progress, not just overall (know which file is slow)
- Batch upload with individual retry (don't restart all on one failure)

**Emotional arc:**
- Start: Purposeful (I need to get this file somewhere)
- Selection: Brief effort (find the file)
- Upload: Waiting (progress bar — make it feel fast)
- Complete: Relief (it worked) — this is a utility flow, minimize friction, maximize reliability

**Metric targets:**
- Upload success rate: >98%
- Upload start to complete (10MB file): <30 seconds
- Format error rate: <10% (proactive format guidance reduces this)
- Resume rate after interruption: >80%
- Abandonment rate: <15%

**Drop-off prevention strategies:**
- Show accepted formats and size limits before upload
- Drag-and-drop with clear visual drop zone
- Background uploading (user doesn't have to watch)
- Resume interrupted uploads (chunked upload protocol)
- Compress option for oversized files

**Best-in-class references:**
- **Google Drive** — Drag-and-drop, background upload, progress toast, resume
- **Dropbox** — Camera upload, folder selection, conflict resolution
- **Figma** — Drag images directly to canvas, instant processing

---

## 13. Collaboration Invite Flow

**Step sequence:**
1. **Trigger** — Tap "Invite" or "Share" on workspace/project/document
2. **Enter recipients** — Email input (multi-entry), contact search, or shareable link generation
3. **Set permissions** — Choose role per invitee (Viewer, Editor, Admin)
4. **Add message** (optional) — Personal invite message
5. **Send** — Invitations sent via email/notification
6. **Confirmation** — "Invitations sent" summary with pending status

**Decision points and branching:**
- Email invite vs. shareable link? (Link = broader but less controlled)
- Existing user vs. new? (Existing get in-app notification, new get email)
- Role assignment: per-user or batch? (Default role + per-user override)
- Workspace-level vs. document-level? (Different permission scopes)

**Error handling per step:**
- Step 2: Invalid email — Inline validation "Enter a valid email address"
- Step 2: User already a member — "Already has access" indicator
- Step 3: Permission conflict — "Cannot grant Admin access. Contact workspace owner."
- Step 5: Some invites fail — "3 of 5 invitations sent. Retry 2 failed." with per-email retry
- Step 5: Rate limited — "Invite limit reached. Try again tomorrow or contact support."

**Cognitive load management:**
- Default role pre-selected (most common permission level)
- Batch email entry (paste comma-separated list)
- Recent collaborators suggested
- Permission explanation tooltips ("Editors can modify content but not manage members")

**Emotional arc:**
- Start: Generosity/purpose (inviting someone to collaborate)
- Entry: Practical (entering emails)
- Sent: Satisfaction (team is growing)
- Acceptance: Connection (collaborator joins)

**Metric targets:**
- Invite initiated to sent: >80%
- Invite acceptance rate: >50%
- Time to complete invite: <30 seconds
- Average invites per session: 2-3

**Drop-off prevention strategies:**
- Quick-invite with default permissions (reduce decisions)
- Shareable link for informal sharing
- Copy link as fallback if email is uncertain
- Suggested contacts reduce typing

**Best-in-class references:**
- **Google Docs** — Share dialog, permission levels, shareable link, real-time status
- **Figma** — Invite with role, shareable link with access control
- **Notion** — Page-level sharing, workspace invites, guest access

---

## 14. Account Deletion Flow

**Step sequence:**
1. **Find option** — Navigate to Settings > Account > Delete Account (intentionally not prominent)
2. **Consequences** — Clear disclosure of what happens (data deleted, subscription cancelled, username freed)
3. **Alternatives** — Offer alternatives (pause account, downgrade plan, export data, talk to support)
4. **Confirm identity** — Re-enter password or biometric verification
5. **Final confirmation** — Type account name or "DELETE" to confirm, checkbox for understanding consequences
6. **Processing** — Account scheduled for deletion (grace period)
7. **Grace period email** — Email sent with "Cancel deletion" link, 14-30 day window

**Decision points and branching:**
- Export data first? (Offer data export before proceeding)
- Active subscription? (Explain subscription cancellation separately)
- Team owner? (Must transfer ownership before deletion)
- Grace period: immediate deletion or delayed? (Always delayed for recovery)

**Error handling per step:**
- Step 4: Wrong password — "Incorrect password" with lockout after 5 attempts
- Step 4: MFA required — MFA step before proceeding
- Step 5: Typed confirmation wrong — "Type DELETE to confirm" (don't proceed)
- Step 6: Processing error — "Deletion could not be processed. Try again later."
- Grace period: User wants to cancel — Easy "Cancel deletion" in email + login restores account

**Cognitive load management:**
- This flow should have friction by design (preventing accidental deletion)
- Each step is a chance to reconsider
- Consequences must be specific ("Your 47 projects and 1,203 files will be permanently deleted")
- Alternatives should be genuinely helpful, not manipulative

**Emotional arc:**
- Start: Determination or frustration (user has decided to leave)
- Consequences: Doubt (is this what I want?)
- Alternatives: Consideration (maybe there's another way)
- Confirmation: Resolve (yes, I'm sure)
- Grace period: Safety net (I can still change my mind)
- Note: This flow should respect the user's agency. Do not use dark patterns (guilt-tripping, hiding the button, excessive steps). Friction should be about preventing mistakes, not retention.

**Metric targets:**
- Deletion start to completion: ~50% (some should reconsider, but not due to friction)
- Grace period recovery rate: 10-20%
- Data export rate before deletion: >30%
- Time to complete: 2-5 minutes (intentional deliberation time)

**Drop-off prevention strategies:**
- Step 2: Specific data counts make consequences tangible
- Step 3: Genuinely useful alternatives (not "Are you really sure?" x5)
- Step 7: Grace period email with one-tap recovery
- Important: Do not use dark patterns. This is about respect, not retention.

**Best-in-class references:**
- **Google** — Clear data deletion timeline, data export (Takeout), service-by-service option
- **Slack** — Workspace owner transfer requirement, clear data policy
- **Instagram** — 30-day grace period, temporarily disable as alternative, data download

---

## 15. Error Recovery Flow

**Step sequence:**
1. **Error occurs** — Something goes wrong (network, server, validation, permission)
2. **Detection** — System detects the error type and severity
3. **Communication** — Show user-friendly error message explaining what happened
4. **Guidance** — Provide specific next steps (retry, alternative action, contact support)
5. **Recovery action** — User takes suggested action
6. **Resolution** — Success state reached, or escalation to support

**Decision points and branching:**
- Error type determines UX response:
  - **Transient (network/timeout)** — Auto-retry with exponential backoff, then manual retry button
  - **Validation (user input)** — Inline field errors with correction guidance
  - **Permission (access denied)** — Explain why + how to get access
  - **Not found (404)** — Redirect options (search, home, back)
  - **Server error (500)** — Apology + status page link + retry later
  - **Conflict (version/duplicate)** — Show both versions, let user choose

**Error handling per step (meta — how to handle errors in the error recovery flow):**
- Step 3: Error message itself fails to display — Fall back to generic toast
- Step 5: Retry fails again — Escalate messaging ("Still having trouble. Contact support.")
- Step 5: Recovery action creates new error — Don't stack errors, show the most actionable one

**Cognitive load management:**
- One error message at a time (not a list of 5 problems)
- Error message formula: What happened + Why + What to do next
- Preserve user's work (never lose form data on error)
- Auto-recovery for transient errors (user may not even notice)
- Error severity indicated visually (red = blocking, yellow = warning, blue = info)

**Emotional arc:**
- Error: Frustration or anxiety (something broke!)
- Communication: Understanding (ok, I see what happened)
- Guidance: Empowerment (I know what to do)
- Recovery: Relief (it's working again)
- Key insight: The faster you move users from frustration to empowerment, the more they trust your product

**Metric targets:**
- Auto-recovery success rate: >80% (for transient errors)
- Manual retry success rate: >60%
- Error-to-resolution time: <30 seconds (for recoverable errors)
- Error abandonment rate: <20% (users leaving after an error)
- Support ticket rate from errors: <5%

**Drop-off prevention strategies:**
- Never show raw error codes or stack traces
- Always provide at least one action (retry, go back, contact support)
- Preserve form data / user state across errors
- Auto-retry transient errors before showing user an error
- Offline mode: queue actions for later, show offline-capable features

**Best-in-class references:**
- **Stripe** — Excellent error messages in API and dashboard, specific guidance
- **GitHub** — Friendly error pages, status page integration, clear recovery paths
- **Google Docs** — Auto-save prevents data loss, offline mode, conflict resolution

---

## Flow Pattern Cross-Reference Matrix

| Flow | Key Emotion | Critical Metric | Biggest Risk |
|------|-------------|----------------|--------------|
| Authentication | Purposeful > Relief | Login completion >95% | Wrong credentials handling |
| Onboarding | Excitement > Empowered | Completion >80% | Too many steps |
| Checkout | Anticipation > Delight | Cart abandonment <70% | Hidden fees at checkout |
| Booking | Excitement > Anticipation | Search-to-book >10% | Availability changes mid-flow |
| Search & Filter | Intent > Satisfaction | Zero-result rate <5% | No results guidance |
| Content Creation | Inspiration > Pride | Create-to-publish >40% | Auto-save failure |
| Profile Editing | Control > Satisfaction | Edit-to-save >80% | Unsaved changes lost |
| Settings | Purposeful > Done | Find setting <20s | Can't find the setting |
| Subscription | Desire > Empowered | Trial-to-paid >25% | Payment friction |
| Social Sharing | Enthusiasm > Satisfaction | Share completion >40% | Too many steps to share |
| Messaging | Social > Connection | Send success >99% | Message delivery failure |
| File Upload | Purposeful > Relief | Upload success >98% | Network interruption |
| Collaboration Invite | Generosity > Connection | Invite acceptance >50% | Invalid email handling |
| Account Deletion | Determination > Closure | Grace period recovery 10-20% | Dark patterns (don't do it) |
| Error Recovery | Frustration > Relief | Auto-recovery >80% | Generic unhelpful error messages |

---

## Universal Flow Design Principles

1. **Preserve user state** — Never lose user input on error, navigation, or timeout
2. **One decision per step** — Each step should have a single primary decision
3. **Progress visibility** — Users should always know where they are and how much is left
4. **Easy reversal** — Back buttons, undo, cancel, and grace periods at every step
5. **Smart defaults** — Pre-fill, auto-detect, and suggest to reduce decisions
6. **Error prevention over error handling** — Inline validation, constraints, and confirmations
7. **Emotional design** — Celebrate completions, empathize with errors, reduce anxiety at payment
8. **Accessibility throughout** — Every step must be keyboard navigable, screen reader compatible, and respect motion preferences

---

## User Flow Patterns (22 types)


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
