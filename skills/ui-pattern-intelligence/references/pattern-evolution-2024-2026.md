# Pattern Evolution 2024-2026 — What's Changing, What's Dying, What's Emerging

## Why Pattern Evolution Matters

UI patterns are not static. They evolve as technology shifts (new CSS features, new platform APIs, new interaction models), as user expectations change (what felt innovative in 2020 feels dated in 2026), and as the best products push conventions forward.

When Sumi analyzes a user's app, it needs to distinguish between patterns that are stable (use them confidently), patterns that are evolving (use the modern variant), patterns that are dying (replace them), and patterns that are emerging (consider adopting). This file provides that temporal intelligence.

---

## Dying Patterns — Replace These

These patterns were once standard but are now actively declining. Using them makes an app feel dated.

### Hamburger Menu on Desktop → Command Palette + Visible Nav
**Status**: Dead on desktop. Acceptable only as a mobile fallback.
**Why it died**: Nielsen Norman Group's quantitative study (179 participants, six sites) found that hiding navigation cuts content discoverability by nearly half. Users don't explore menus they can't see. The rise of command palettes (Cmd+K) provides keyboard-first navigation that is faster than any menu. Visible top nav or sidebar is always superior on desktop.
**Replace with**: Sidebar navigation (SaaS), top nav (marketing), or command palette as primary.

### Full-Page Loading Spinners → Skeleton Screens
**Status**: Dying. Still seen in older apps and vibe-coded projects.
**Why it's dying**: Spinners provide zero information about what's loading or how much is left. Skeleton screens set spatial expectations and reduce perceived wait time by up to 30% (research from Facebook and Google). The user's brain starts processing the layout before data arrives.
**Replace with**: Per-component skeleton screens matching the layout of real content. Use `<Skeleton>` components.

### Modal-Heavy Workflows → Side Panels + Inline Editing
**Status**: Declining for data workflows. Still appropriate for confirmations.
**Why it's declining**: Modals break context. Users lose their place. Deep modal stacking (modal opening modal) is a UX nightmare. Side panels (drawers) allow users to keep the main view visible while editing details. Inline editing (Notion-style) eliminates the need for a separate editing surface entirely.
**Replace with**: Side panel/drawer for detail views. Inline editing for content. Reserve modals for confirmations and alerts only.

### Carousel/Slider Auto-Advance → Static Content or User-Controlled
**Status**: Dying for hero carousels. Still used for product image galleries (user-controlled).
**Why it's dying**: Auto-advancing carousels have terrible engagement rates. Users can't control the pace. Accessibility issues (auto-advancing content violates WCAG 2.2.2). Content in slides 2+ is seen by < 1% of users (NNG research). The "hero carousel" is one of the most debunked patterns in UX.
**Replace with**: Single hero with strong messaging. Or static bento grid of features. For product images: user-controlled gallery.

### Pagination for Feeds → Infinite Scroll (with caveats)
**Status**: Pagination dying for feeds/timelines. Still alive and correct for data tables and search results.
**Why the shift**: For content consumption (social feeds, activity streams), pagination creates unnecessary friction. Users expect continuous scrolling. But for data analysis (tables, search), pagination is superior because users need position awareness and the ability to return to specific pages.
**Keep pagination for**: Data tables, search results, admin panels.
**Use infinite scroll for**: Social feeds, activity streams, messaging.

### Flat Design (2013-era) → Depth + Elevation + Glassmorphism
**Status**: Pure flat design peaked in 2015-2018. Evolving toward subtle depth.
**Why the shift**: Pure flat design lost affordance — users couldn't tell what was clickable. The pendulum swung back toward subtle elevation (shadows), glassmorphism (iOS 26 Liquid Glass, Material 3 elevation), and layered interfaces. The goal is depth that communicates hierarchy without returning to skeuomorphism.
**Current best practice**: Subtle shadows, frosted glass for overlays, layered cards with clear z-axis hierarchy.

### Tab Bar with > 5 Items → More Tab or Reorganize
**Status**: The "More" tab (with a grid of remaining items) is itself declining.
**Why**: Apps that need > 5 bottom nav items have an architecture problem, not a UI problem. The solution is to reorganize the information architecture, not to cram more items into the tab bar.
**Replace with**: Reorganize IA to fit 4-5 primary destinations. Move secondary items to settings or profile menus.

### Cookie Consent Banners (dark pattern variants) → Transparent + Compliant
**Status**: The obnoxious "Accept All" prominent / "Reject" hidden cookie banner is dying due to enforcement.
**Why**: GDPR, ePrivacy, and CPRA enforcement is catching up. Regulators are fining for dark-pattern consent. The "Accept All" + tiny "Manage Preferences" pattern is explicitly called out by the EU.
**Replace with**: Equal-prominence "Accept" / "Reject" buttons. Genuine choice. Or better: only set essential cookies and skip the banner entirely.

---

## Evolving Patterns — Use the Modern Variant

### Search → AI-Augmented Semantic Search
**Was**: Keyword matching. Type a word, get exact matches.
**Now**: Semantic search that understands intent. "Show me invoices from last quarter" instead of searching "invoice." Typo tolerance, fuzzy matching, synonym awareness.
**Best implementations**: Algolia, Meilisearch for traditional. Embeddings-based search for AI-native products.
**What this means for users**: If your search still requires exact keywords, it feels broken. Users now expect search to understand what they mean.

### Dropdowns/Selects → Searchable Combobox
**Was**: Native `<select>` with scrollable option list.
**Now**: Custom combobox with type-to-filter, keyboard navigation, multi-select support, and option grouping. The native `<select>` is now reserved for simple cases (< 7 options) or when native mobile pickers are desired.
**Best implementations**: Radix UI, Headless UI, Cmdk.

### Forms → Progressive, Conversational, AI-Assisted
**Was**: Static form with all fields visible, submit button at bottom.
**Now**: Progressive forms that reveal fields based on prior answers. Conversational forms (Typeform) for engagement. AI-assisted autofill that pre-populates based on context. Smart defaults that reduce cognitive load.
**What this means**: A signup form that shows 10 fields at once feels antiquated. Show 1-3 at a time.

### Tooltips → Contextual Popovers with Rich Content
**Was**: Plain text tooltip on hover.
**Now**: Rich popovers with formatted content, links, and interactions — triggered on click (not hover) for better mobile and accessibility support. Hover tooltips remain for simple labels, but anything more than a sentence should be a popover.
**Best implementations**: Radix Tooltip + Popover. Floating UI.

### Card Grids → Bento Grids with Intentional Sizing
**Was**: Uniform grid of equal-sized cards. Bootstrap 12-column layouts.
**Now**: Bento grids where card size communicates importance. A feature card spanning 2 columns is more important than a 1-column card. Apple popularized this on their marketing pages.
**Caution**: Bento grids work for curated content (marketing, features). For repetitive content (products, listings), uniform grids remain better for scannability.

### Static Dashboards → Customizable Widget Layouts
**Was**: Fixed dashboard layout. Same KPIs for everyone.
**Now**: Drag-to-reorder, resize, add/remove widgets. Saved layouts per user. Default layout for new users with customization available. The dashboard reflects the user's priorities.
**Best implementations**: Notion databases. Vercel dashboard. Home Assistant.

### Tab Navigation → Segmented Controls and View Switchers
**Was**: Traditional underline tabs.
**Now**: Pill-style segmented controls (iOS native) for 2-4 options. Tab bars with count badges. Dropdown view switchers for > 5 options. The visual language is shifting from underline to pill/segment.
**Both still valid**: Underline tabs aren't dying — they're appropriate for content sections. Segments/pills are better for mode switching.

### Error Messages → Inline Guidance + Recovery Actions
**Was**: Red text below field: "Invalid email."
**Now**: Specific explanation + fix suggestion: "This doesn't look like an email. Check for typos — did you mean user@gmail.com?" Recovery-focused, not accusatory. Inline, not in an alert dialog.

---

## Emerging Patterns — Consider Adopting

### Command-K / Universal Command Bar
**Status**: Rapidly becoming table stakes for any app with > 10 features.
**What it is**: A single keyboard shortcut (Cmd+K or Ctrl+K) that opens a search + action palette. Navigate, execute commands, search content — all from one place.
**Who should adopt**: Every SaaS, productivity, and developer tool. Consumer apps with power users. Admin panels.
**Why**: It's the single biggest QoL improvement for power users. Takes < 1 day to add with libraries like cmdk (Pacifico), kbar, or ninja-keys.

### AI Copilot / Inline Assist
**Status**: Rapidly expanding beyond code editors into all content-creation tools.
**What it is**: AI suggestions that appear inline as you work — ghost text in editors, auto-complete in forms, suggested actions in context.
**Who should adopt**: Any product with text editing or content creation. Task management (suggest next actions). CRMs (suggest email responses). Design tools (suggest layouts).
**Caution**: Must be non-intrusive. Tab to accept, Escape to dismiss. Never auto-apply without consent.

### Generative UI / Dynamic Interfaces
**Status**: Early but accelerating. Vercel AI SDK v4 has native support.
**What it is**: AI generates the UI component (chart, table, form, card) dynamically based on the user's query. "Show me revenue by country" renders a bar chart. "Compare these plans" renders a comparison table.
**Who should adopt**: Analytics dashboards, AI-native products, internal tools.
**Caution**: Generated UI must be accessible. ARIA attributes must be injected. Keyboard navigation must work.

### Bottom Sheets (Mobile)
**Status**: Becoming the dominant mobile overlay pattern, replacing modals.
**What it is**: A panel that slides up from the bottom of the screen with drag-to-dismiss. Half-sheet (peeks) or full-sheet. Native on both iOS and Android.
**Why it's winning**: Thumb-friendly (within the thumb zone). Less disruptive than full-screen modals. Drag-to-dismiss feels natural. Progressive disclosure (peek → expand).
**Who should adopt**: All mobile apps. Use instead of modals for detail views, filters, and secondary actions.

### Container Queries for Responsive Components
**Status**: Now supported in all modern browsers. Adoption accelerating.
**What it is**: Components that respond to their container's width, not the viewport. A card component that rearranges its layout in a sidebar vs. main content area vs. modal — without media queries.
**Why it matters**: Enables truly reusable components. A component works everywhere without breakpoint-specific overrides.
**Who should adopt**: Everyone building reusable component libraries.

### View Transitions API
**Status**: Chrome shipped, Safari shipping. Polyfill available.
**What it is**: Native browser API for animating between views/pages. Smooth page transitions without JavaScript animation libraries. Morph animations between shared elements across routes.
**Why it matters**: Page transitions that previously required complex JavaScript now work with a few CSS properties. SPA-smooth navigation for MPA architectures.

### Passkeys → Replacing Passwords
**Status**: Supported by Apple, Google, Microsoft. Adoption growing.
**What it is**: Biometric-based authentication (Face ID, fingerprint, Windows Hello) that replaces passwords entirely. No password to type, no OTP to enter. Sign in with a glance or touch.
**Who should adopt**: Any app with authentication. Offer passkeys alongside traditional auth during transition.

### Scroll-Driven Animations
**Status**: CSS `animation-timeline: scroll()` landing in browsers.
**What it is**: Animations that progress based on scroll position, entirely in CSS. No JavaScript intersection observers or scroll listeners needed. Parallax, reveal-on-scroll, progress indicators.
**Why it matters**: Performance (GPU-accelerated, no JS). Simplicity. Works with `prefers-reduced-motion`.

### Spatial / 3D UI Elements
**Status**: Niche but growing. visionOS, 3D product viewers, AR try-on.
**What it is**: UI elements with depth — 3D product rotators, spatial layouts in AR/VR, parallax cards. visionOS window management in spatial computing.
**Who should adopt**: E-commerce (product 3D viewers), real estate (3D tours), gaming, AR apps.
**Caution**: 3D for the sake of 3D is decoration. Only use when depth adds information.

### Skeleton → Content-Aware Loading
**Status**: Early. Apple and Google are experimenting.
**What it is**: Beyond generic skeleton shapes — loading states that show a blurred or low-resolution preview of the actual content. Like progressive image loading applied to entire UI sections.

---

## Stable Patterns — Use Confidently

These patterns are mature, well-tested, and not going anywhere:

| Pattern | Status | Notes |
|---------|--------|-------|
| Sidebar Navigation | Stable | The SaaS standard. May evolve visually but structurally stable. |
| Bottom Navigation | Stable | The mobile standard. 3-5 items. Not going away. |
| Data Tables | Stable | The backbone of admin/analytics. Features evolve (virtualization, inline editing) but the pattern endures. |
| Cards | Stable | The universal content container. Layout variants (bento) evolve but cards endure. |
| Forms with Labels | Stable | Labels above inputs. Inline validation. The most-tested UI pattern. |
| Toasts | Stable | Auto-dismissing confirmations. The feedback standard. |
| Modals (for confirmation) | Stable | Declining for data workflows but permanent for confirmations. |
| Progress Indicators | Stable | Determinate bars, step indicators. Timeless. |
| Search | Stable (but evolving) | The input pattern is stable. The intelligence behind it (semantic, AI) is evolving. |
| Avatar | Stable | Circle + initials fallback. Universal identity pattern. |

---

## What Vibe Coders Get Wrong

AI-generated UI tends to produce patterns that are technically functional but stylistically generic and temporally misaligned. Common issues:

1. **Bootstrap-era patterns**: Default HTML/CSS patterns that were cutting-edge in 2015 but feel dated now (full-width hero with centered text, basic card grid, hamburger on desktop).

2. **Missing modern essentials**: No command palette, no skeleton screens, no inline editing, no dark mode, no keyboard shortcuts. These are now expected, not premium.

3. **State blindness**: Only the "happy path" default state is built. No hover, no focus, no loading, no error, no empty, no disabled. Real products have 10 states per component.

4. **Accessibility afterthought**: ARIA attributes missing. Keyboard navigation not implemented. Focus management absent. Color contrast insufficient.

5. **Motion desert**: Zero transitions, zero micro-interactions. Elements appear and disappear without animation. The app feels static and lifeless.

6. **Franken-design**: Each prompt generates a slightly different visual language. Cards from one prompt have 8px radius; cards from another have 16px. Colors drift. Typography inconsistent. No design token system.

7. **Sector blindness**: Generic patterns used regardless of sector. A fintech app with the same visual weight as a social app. A healthcare app with gaming-level color saturation.

8. **Anti-pattern adoption**: Using patterns that look good in a screenshot but fail in production — auto-advancing carousels, hamburger menus on desktop, infinite scroll for data tables, modals for everything.

The `/audit` command exists to catch all 8 of these issues and prescribe the specific upgrades that close the gap between "vibe coded" and "professionally designed."
