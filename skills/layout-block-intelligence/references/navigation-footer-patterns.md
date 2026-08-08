# Navigation & Footer Patterns — 40+ Production-Ready Variants

## Navigation Design Philosophy

Navigation is the skeleton of any digital product. It answers three questions simultaneously: "Where am I?", "Where can I go?", and "How do I get back?" Poor navigation is the single most common usability failure — Nielsen Norman Group consistently ranks navigation problems as the top source of user frustration.

Navigation blocks differ from other section types because they are persistent (visible on every page), interactive (state changes constantly), and structurally critical (they define the information architecture). Getting navigation wrong affects every page; getting it right makes every page better.

### Navigation Principles
1. **Visibility**: Primary navigation must be immediately visible, never hidden behind interactions on desktop
2. **Consistency**: Same navigation structure on every page (position, items, behavior)
3. **Clarity**: Labels must be unambiguous — "Products" not "Solutions", "Pricing" not "Plans"
4. **Efficiency**: Maximum 7 primary navigation items (Miller's Law)
5. **Feedback**: Active page indicator, hover states, loading states
6. **Accessibility**: Keyboard navigable, skip links, ARIA landmarks, focus management

---

## Navigation Specifications

### Universal Nav Specs
- Height: 64-80px desktop, 56-64px mobile
- Background: white (default), transparent (over hero), dark (apps)
- Z-index: 40-50 (above content, below modals)
- Logo: 28-40px height, linked to homepage
- Links: 14-16px, font-weight 500, gap 24-32px
- CTA button: 14px, padding 10px 20px, border-radius 6-8px
- Transition: background-color 200ms ease on scroll
- Shadow (sticky): 0 1px 3px rgba(0,0,0,0.1) when scrolled

---

## Variant 1: Standard Top Nav

Logo left, navigation links center, CTA button right. The default pattern for 80%+ of marketing sites.

### Layout Specs
- Container: max-width 1200-1400px, centered, padding 0 24-48px
- Logo zone: left, flex-shrink-0
- Links zone: center (flex-1, justify-center) or right of logo
- Action zone: right, flex-shrink-0 (login link + CTA button)
- Item count: 4-7 primary links
- Active indicator: underline (2px, brand color, 4px below text) or font-weight change

### Responsive Behavior
- `xl`+: Full nav visible, all links shown
- `lg`: Condense spacing, may hide 1-2 low-priority links
- `md`: Switch to hamburger menu (mobile nav)
- `sm`: Hamburger menu, logo may reduce size

### Production Code (React/TSX)
```tsx
import { useState } from 'react';

interface NavItem { label: string; href: string; active?: boolean }

interface TopNavProps {
  logo: { src: string; alt: string; href: string };
  items: NavItem[];
  cta?: { label: string; href: string };
  loginHref?: string;
}

export function TopNav({ logo, items, cta, loginHref }: TopNavProps) {
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-sm border-b border-gray-100">
      <nav className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8" aria-label="Main navigation">
        <div className="flex h-16 items-center justify-between">
          <a href={logo.href} className="flex-shrink-0">
            <img src={logo.src} alt={logo.alt} className="h-8 w-auto" />
          </a>

          {/* Desktop links */}
          <div className="hidden lg:flex items-center gap-8">
            {items.map((item) => (
              <a
                key={item.href}
                href={item.href}
                className={`text-sm font-medium transition-colors ${item.active ? 'text-blue-600' : 'text-gray-700 hover:text-gray-900'}`}
                aria-current={item.active ? 'page' : undefined}
              >
                {item.label}
              </a>
            ))}
          </div>

          {/* Desktop actions */}
          <div className="hidden lg:flex items-center gap-4">
            {loginHref && <a href={loginHref} className="text-sm font-medium text-gray-700 hover:text-gray-900">Log in</a>}
            {cta && <a href={cta.href} className="rounded-lg bg-blue-600 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-500 transition-colors">{cta.label}</a>}
          </div>

          {/* Mobile hamburger */}
          <button
            className="lg:hidden p-2 -mr-2 text-gray-600"
            onClick={() => setMobileOpen(!mobileOpen)}
            aria-expanded={mobileOpen}
            aria-label="Toggle navigation menu"
          >
            <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              {mobileOpen ? (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>

        {/* Mobile menu */}
        {mobileOpen && (
          <div className="lg:hidden py-4 border-t border-gray-100">
            <div className="space-y-1">
              {items.map((item) => (
                <a key={item.href} href={item.href} className={`block px-3 py-2 rounded-lg text-base font-medium ${item.active ? 'bg-blue-50 text-blue-600' : 'text-gray-700 hover:bg-gray-50'}`}>
                  {item.label}
                </a>
              ))}
            </div>
            <div className="mt-4 pt-4 border-t border-gray-100 space-y-3 px-3">
              {loginHref && <a href={loginHref} className="block text-base font-medium text-gray-700">Log in</a>}
              {cta && <a href={cta.href} className="block w-full rounded-lg bg-blue-600 px-4 py-2.5 text-center text-base font-semibold text-white">{cta.label}</a>}
            </div>
          </div>
        )}
      </nav>
    </header>
  );
}
```

### Accessibility Requirements
- `<nav>` with `aria-label="Main navigation"`
- Active page: `aria-current="page"` on current link
- Mobile toggle: `aria-expanded`, `aria-label`
- Skip link: invisible `<a href="#main-content">Skip to content</a>` before nav
- Focus trap: when mobile menu open, Tab cycles within menu
- Escape: closes mobile menu
- Keyboard: Tab through links, Enter/Space to activate

---

## Variant 2: Mega Menu Nav

Full-width dropdown revealing categorized content, images, and featured items.

### Layout Specs
- Trigger: hover (desktop) or click (mobile/keyboard) on parent link
- Dropdown: full viewport width, max-height 480px
- Content: 3-5 columns of links, optional featured card with image
- Column: heading (14px, font-weight 600, uppercase, gray-500) + 4-8 links (15px, gray-700)
- Background: white, shadow-xl, border-top 1px gray-100
- Close: click outside, Escape key, or move mouse away (300ms delay)

### Responsive Behavior
- `xl`+: Full mega menu on hover
- `lg`: Simplified dropdown (single column)
- `md`: Accordion within mobile menu drawer

### Accessibility
- Trigger: `aria-haspopup="true"`, `aria-expanded`
- Dropdown: `role="menu"`, items `role="menuitem"`
- Arrow keys: navigate within menu
- Escape: close menu, return focus to trigger

---

## Variant 3: Transparent Overlay Nav

No background initially, overlays the hero section, transitions to solid on scroll.

### Layout Specs
- Initial state: background transparent, text white or light
- Scrolled state: background white (or dark), text dark, shadow
- Transition trigger: scroll past 50-100px (or past hero section)
- Logo: may swap between light and dark versions

### Production Code (scroll detection)
```tsx
import { useState, useEffect } from 'react';

function useScrolled(threshold = 50) {
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    const handle = () => setScrolled(window.scrollY > threshold);
    window.addEventListener('scroll', handle, { passive: true });
    handle();
    return () => window.removeEventListener('scroll', handle);
  }, [threshold]);
  return scrolled;
}

export function TransparentNav({ items, logo, cta }: TopNavProps) {
  const scrolled = useScrolled();

  return (
    <header className={`fixed top-0 inset-x-0 z-50 transition-all duration-300 ${scrolled ? 'bg-white/95 backdrop-blur-sm shadow-sm' : 'bg-transparent'}`}>
      <nav className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 lg:h-20 items-center justify-between">
          {/* Logo and links with dynamic text color */}
          <a href={logo.href}>
            <img src={logo.src} alt={logo.alt} className={`h-8 w-auto transition-opacity ${scrolled ? '' : 'brightness-0 invert'}`} />
          </a>
          <div className="hidden lg:flex items-center gap-8">
            {items.map((item) => (
              <a key={item.href} href={item.href} className={`text-sm font-medium transition-colors ${scrolled ? 'text-gray-700 hover:text-gray-900' : 'text-white/90 hover:text-white'}`}>
                {item.label}
              </a>
            ))}
          </div>
          {cta && (
            <a href={cta.href} className={`hidden lg:inline-flex rounded-lg px-4 py-2 text-sm font-semibold transition-colors ${scrolled ? 'bg-blue-600 text-white' : 'bg-white text-gray-900'}`}>
              {cta.label}
            </a>
          )}
        </div>
      </nav>
    </header>
  );
}
```

---

## Variant 4: Sticky Shrinking Nav

Full height at page top, reduces height on scroll for more content visibility.

### Layout Specs
- Initial height: 80px
- Scrolled height: 56-64px
- Logo: scales down slightly (h-10 to h-8)
- Links: may reduce font-size or spacing
- Transition: height and padding over 200-300ms
- Shadow: appears when scrolled

---

## Variant 5: Sidebar Navigation (Expanded)

Persistent left sidebar with icon + label. Standard for dashboard apps.

### Layout Specs
- Width: 240-280px
- Background: white or gray-50 (light theme), gray-900 (dark theme)
- Position: fixed left, full height
- Logo: top of sidebar, 16-24px from top
- Nav items: icon (20-24px) + label (14-15px), vertical stack
- Item height: 40-44px
- Item padding: 12px 16px
- Active: bg-blue-50 text-blue-600 (light) or bg-white/10 (dark)
- Hover: bg-gray-100 (light) or bg-white/5 (dark)
- Dividers: 1px line or 16px gap between groups
- Bottom: user avatar/menu or settings link

### Responsive Behavior
- `xl`+: Expanded sidebar (240px)
- `lg`: Collapsed sidebar (64px, icons only)
- `md`: Off-screen, hamburger trigger, slide-in overlay

### Production Code
```tsx
interface SidebarItem { icon: React.ReactNode; label: string; href: string; active?: boolean }

export function Sidebar({ items, logo }: { items: SidebarItem[]; logo: React.ReactNode }) {
  return (
    <aside className="fixed inset-y-0 left-0 z-30 w-64 bg-gray-900 text-white flex flex-col" aria-label="Sidebar navigation">
      <div className="flex h-16 items-center px-6 border-b border-white/10">
        {logo}
      </div>
      <nav className="flex-1 overflow-y-auto py-4 px-3">
        <ul className="space-y-1">
          {items.map((item) => (
            <li key={item.href}>
              <a href={item.href} className={`flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors ${item.active ? 'bg-white/10 text-white' : 'text-gray-400 hover:bg-white/5 hover:text-white'}`} aria-current={item.active ? 'page' : undefined}>
                <span className="flex-shrink-0 w-5 h-5">{item.icon}</span>
                {item.label}
              </a>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
}
```

---

## Variant 6: Mobile Bottom Tab Bar

Fixed bottom bar with icon tabs. Standard for mobile apps, increasingly used in mobile web.

### Layout Specs
- Position: fixed bottom, full width
- Height: 56-64px + safe area inset (iOS)
- Background: white, border-top 1px gray-200
- Items: 4-5 tabs maximum
- Item: icon (24px) + label (10-11px) centered vertically
- Active: brand color icon + label, or filled icon
- Inactive: gray-400 icon + label
- Tap target: full tab width, minimum 44px height

### Production Code
```tsx
interface TabItem { icon: React.ReactNode; activeIcon: React.ReactNode; label: string; href: string; active?: boolean }

export function BottomTabBar({ tabs }: { tabs: TabItem[] }) {
  return (
    <nav className="fixed bottom-0 inset-x-0 z-40 bg-white border-t border-gray-200 pb-[env(safe-area-inset-bottom)]" aria-label="Tab navigation">
      <div className="flex items-stretch h-14">
        {tabs.map((tab) => (
          <a key={tab.href} href={tab.href} className={`flex-1 flex flex-col items-center justify-center gap-0.5 ${tab.active ? 'text-blue-600' : 'text-gray-400'}`} aria-current={tab.active ? 'page' : undefined}>
            <span className="w-6 h-6">{tab.active ? tab.activeIcon : tab.icon}</span>
            <span className="text-[10px] font-medium">{tab.label}</span>
          </a>
        ))}
      </div>
    </nav>
  );
}
```

### Accessibility
- `<nav>` with `aria-label="Tab navigation"`
- Active tab: `aria-current="page"`
- Labels are required (icon-only tabs fail accessibility)
- Keyboard: Tab moves between tabs, Enter activates

---

## Variant 7: Breadcrumb Navigation

Path trail showing the user's location in the site hierarchy.

### Layout Specs
- Position: below main nav, above page content
- Height: 40-48px
- Items: page path separated by chevrons or slashes
- Text: 13-14px, gray-500 (links), gray-900 (current page)
- Separator: chevron icon (12px) or "/" character
- Current page: not linked, font-weight 500
- Truncation: ellipsis for long paths, show first and last 2 items

### Production Code
```tsx
interface BreadcrumbItem { label: string; href?: string }

export function Breadcrumb({ items }: { items: BreadcrumbItem[] }) {
  return (
    <nav aria-label="Breadcrumb" className="py-3">
      <ol className="flex items-center gap-2 text-sm">
        {items.map((item, i) => (
          <li key={i} className="flex items-center gap-2">
            {i > 0 && <svg className="h-4 w-4 text-gray-400 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fillRule="evenodd" d="M7.21 14.77a.75.75 0 01.02-1.06L11.168 10 7.23 6.29a.75.75 0 111.04-1.08l4.5 4.25a.75.75 0 010 1.08l-4.5 4.25a.75.75 0 01-1.06-.02z" clipRule="evenodd" /></svg>}
            {item.href ? (
              <a href={item.href} className="text-gray-500 hover:text-gray-700 transition-colors">{item.label}</a>
            ) : (
              <span className="text-gray-900 font-medium" aria-current="page">{item.label}</span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}
```

---

## Variants 8-25: Navigation Quick Reference

### 8. Command Palette (Cmd+K)
Modal overlay triggered by Cmd+K (or Ctrl+K). Search input at top, results below. Keyboard-navigable: arrow keys, Enter. Categories: pages, actions, settings. Instant results as user types. Close: Escape or click outside. Z-index: 50+ (above everything).

### 9. Progress Nav (Multi-Step)
Horizontal steps: circles connected by lines. States: completed (green check), current (brand color, filled), upcoming (gray, outlined). Labels below circles. Responsive: horizontal on desktop, vertical on mobile. Used for: checkout, onboarding, multi-step forms.

### 10. Double Bar Nav
Top bar: utility links (contact, language, social). 32px height, 12px text, gray bg. Main bar: standard nav below. Total height: 100-112px. Mobile: utility bar hidden, main bar becomes hamburger.

### 11. Floating Nav
Detached from top edge, positioned 16-24px below. Pill or rounded-rectangle shape. Backdrop-blur background. Max-width: 800px, centered. Shadow: lg. Modern, distinctive. Popular with creative and tech brands.

### 12. Secondary Tab Nav
Horizontal tabs below main nav for sub-sections. Tab height: 48px. Active: border-bottom 2px brand. Used for: product sub-pages, settings sections, documentation categories. Scrollable on mobile.

### 13. Vertical Tab Nav
Left-side tabs for settings or dashboard panels. Width: 200-240px. Items: text only or icon + text. Active: bg highlight or left border. Used for: settings pages, account management.

### 14. Contextual Action Bar
Appears when items are selected (batch operations). Fixed top or replaces main nav. Content: selection count + action buttons (delete, move, export). Dismiss: deselect all or X button.

### 15. App Header Bar
Dashboard-style top bar. Logo left, breadcrumb center, user menu + actions right. Height: 56-64px. Background: white with bottom border. Actions: notifications bell, settings gear, user avatar dropdown.

### 16-20. Mobile Navigation Variants
16. **Hamburger Slide-In**: Full-height panel from right, overlay backdrop. Width: 80% or 320px max.
17. **Hamburger Full-Screen**: 100% viewport overlay with large links. Background: dark or brand color.
18. **Bottom Sheet Nav**: Slides up from bottom. Drag handle to dismiss. Native mobile feel.
19. **Tab + More**: 4 visible tabs + "More" tab that reveals additional items in a sheet.
20. **Gesture Nav**: Swipe from edge to reveal nav. Edge indicator (thin vertical line). Native app pattern.

### 21-25. Specialized Navigation
21. **Pagination Nav**: Page numbers + prev/next arrows. For paginated content (search results, blog lists).
22. **Infinite Scroll Indicator**: Loading spinner at bottom of content. "Load more" button fallback.
23. **Table of Contents Nav**: Sticky sidebar with section anchors. Active section highlighted on scroll. For long-form content.
24. **Wizard Step Nav**: Steps with labels, connected. Shows completion state. For onboarding and checkout.
25. **Language/Region Nav**: Dropdown or modal for locale selection. Flag icons + language names. Auto-detect user locale.

---

## Footer Design Philosophy

Footers serve as the "safety net" of navigation. They catch users who scrolled past everything without finding what they need. They also fulfill legal requirements (privacy policy, terms) and provide secondary navigation paths. A good footer is comprehensive without being overwhelming.

### Footer Principles
1. **Completeness**: Include all major site sections — the footer IS your sitemap
2. **Legal compliance**: Privacy policy, terms of service, cookie policy, accessibility statement
3. **Contact info**: At minimum, a way to reach the company
4. **Social presence**: Links to social media profiles
5. **Brand closure**: Logo and brief description or tagline
6. **No orphans**: Every link in the footer should lead to a real, maintained page

---

## Footer Specifications

### Universal Footer Specs
- Background: gray-900 (dark, most common), gray-50 (light), or white
- Max-width: same as page (1200-1400px), or full-width background with contained content
- Padding: 48-80px top, 24-40px bottom
- Link text: 14px, gray-400 (on dark) or gray-600 (on light), hover: white or gray-900
- Column heading: 14px, font-weight 600, uppercase, tracking-wider, white or gray-900
- Copyright: 13px, gray-500, bottom of footer with top border or separator

---

## Footer Variant 1: 4-Column Footer

The industry standard. Logo + 4 categorized link columns.

### Layout Specs
- Row 1: Logo column (wider) + 4 link columns (equal width)
- Logo column: logo + brief description (14px, 2-3 lines) + social icons
- Link columns: heading + 5-8 links each
- Categories: Product, Company, Resources, Legal
- Row 2: bottom bar with copyright + optional links
- Separator: 1px border between main content and bottom bar

### Responsive Behavior
- `xl`+: 5 columns (logo + 4)
- `lg`: Logo full-width above, 4 link columns below (2x2 grid)
- `md`: Logo full-width, link columns 2x2
- `sm`: Everything stacked single column

### Production Code (React/TSX)
```tsx
interface FooterColumn { heading: string; links: Array<{ label: string; href: string }> }

interface FooterProps {
  logo: React.ReactNode;
  description: string;
  columns: FooterColumn[];
  social: Array<{ icon: React.ReactNode; href: string; label: string }>;
  legal: Array<{ label: string; href: string }>;
  copyright: string;
}

export function Footer({ logo, description, columns, social, legal, copyright }: FooterProps) {
  return (
    <footer className="bg-gray-900 text-gray-400" aria-label="Site footer">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
        <div className="lg:grid lg:grid-cols-6 lg:gap-8">
          {/* Brand column */}
          <div className="lg:col-span-2 mb-8 lg:mb-0">
            {logo}
            <p className="mt-4 text-sm leading-relaxed max-w-xs">{description}</p>
            <div className="mt-6 flex gap-4">
              {social.map((s) => (
                <a key={s.label} href={s.href} className="text-gray-500 hover:text-gray-300 transition-colors" aria-label={s.label}>
                  {s.icon}
                </a>
              ))}
            </div>
          </div>
          {/* Link columns */}
          <div className="grid grid-cols-2 gap-8 lg:col-span-4 lg:grid-cols-4">
            {columns.map((col) => (
              <div key={col.heading}>
                <h3 className="text-xs font-semibold uppercase tracking-wider text-white mb-4">{col.heading}</h3>
                <ul className="space-y-3">
                  {col.links.map((link) => (
                    <li key={link.href}>
                      <a href={link.href} className="text-sm hover:text-white transition-colors">{link.label}</a>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
        {/* Bottom bar */}
        <div className="mt-12 pt-8 border-t border-gray-800 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="text-xs">{copyright}</p>
          <div className="flex gap-6">
            {legal.map((link) => (
              <a key={link.href} href={link.href} className="text-xs hover:text-white transition-colors">{link.label}</a>
            ))}
          </div>
        </div>
      </div>
    </footer>
  );
}
```

---

## Footer Variant 2: Simple Footer

Minimal one-row footer for simple sites.

### Layout Specs
- Single row: logo/brand left, links center, social right
- Or: centered — copyright + links in one line
- Height: 64-80px
- Background: white with top border, or gray-50
- Text: 13-14px, gray-500

---

## Footer Variant 3: Fat Footer

Maximum-density footer with everything: sitemap, newsletter, social, trust badges, and legal.

### Layout Specs
- Section 1: Newsletter signup (email input + heading) — full width or left column
- Section 2: 4-6 link columns (full sitemap)
- Section 3: Trust badges / certification logos row
- Section 4: Bottom bar (copyright + legal links + social icons + language selector)
- Total height: 400-600px on desktop
- Background: dark (gray-900)

---

## Footer Variant 4: Footer with Newsletter

Footer with prominent email signup section above link columns.

### Layout Specs
- Newsletter zone: heading (24-28px) + subtext (16px) + email input + button
- Newsletter zone: full-width or left 50% of footer
- Below newsletter: standard link columns
- Input + button: inline (flex-row), same height
- Success state: replace form with "Thanks! Check your inbox."

---

## Variants 5-20: Footer Quick Reference

### 5. Footer with Social Links
Standard footer + social icon row. Icons: 20-24px, grayscale, hover: brand colors. Position: in brand column or bottom bar. Platforms: Twitter/X, LinkedIn, GitHub, Instagram, YouTube.

### 6. Footer with App Badges
App Store + Google Play download badges in footer. Badge size: standard (135x40px). Position: brand column or dedicated row. Link: to respective app store listing.

### 7. Footer with Contact Info
Address + phone + email displayed prominently. Map pin icon + address. Phone icon + number (tel: link). Email icon + address (mailto: link). Position: dedicated column or above link columns.

### 8. Minimal Footer
Single line: copyright + 2-3 essential links (Privacy, Terms). Height: 48-56px. Background: transparent or gray-50. Used for: single-page apps, minimal sites, dashboards.

### 9. Footer with Map
Embedded Google Maps / Mapbox showing office location. Map: 200-300px height, full-width or 50%. Muted/custom map style. Pin: office location. Below map: address text.

### 10. Footer with Trust Badges
Security/compliance badges in footer: SOC 2, GDPR, HIPAA, PCI DSS, ISO 27001. Badge height: 40-56px. Position: above bottom bar or in dedicated row. Grayscale or low-contrast styling.

### 11. Footer with Language Selector
Dropdown or link list for locale switching. Globe icon + current language. Options: language name in native script. Position: bottom bar, left or right side.

### 12. Footer with Dark Theme
Dark background (gray-900) regardless of page theme. White/gray text. The most common footer pattern — dark footer on light page creates visual closure.

### 13. Footer with CTA
Final CTA banner above footer columns. Heading + button. "Ready to get started?" + "Sign up free." Background: brand color or gradient. Creates one last conversion opportunity.

### 14. Footer with Recent Posts
3-4 recent blog post thumbnails in footer. Small image (64x64) + title + date. Links to blog posts. Keeps footer dynamic and encourages content exploration.

### 15. Footer with Testimonial
One featured customer quote in footer. Subtle, not the primary social proof location. Quote: 16px italic + name + role. Reinforces trust at the very end of the page.

### 16. Legal-Heavy Footer
For regulated industries: extensive legal links. GDPR compliance notice. Cookie policy link. Accessibility statement. Terms of service. Privacy policy. CCPA notice. Regulatory disclosures.

### 17. Multi-Brand Footer
Parent company logo + sub-brand logos. Links organized by brand/product. Used by: companies with multiple products or acquisitions.

### 18. Footer with Brand Story
Logo + 2-3 sentence brand mission/story. More personal than a simple description. "We started in 2015 with a mission to..." Used by: startups, purpose-driven brands.

### 19. Footer with Status Page Link
System status indicator (green dot + "All systems operational"). Links to status page. Important for: SaaS, infrastructure, API products.

### 20. Sticky Footer CTA Bar
Fixed bar above the actual footer: CTA text + button. Appears when user reaches bottom of page. Different from sticky bottom CTA — this lives at the content bottom, not viewport bottom.

---

## Footer Accessibility Requirements

1. **Landmark**: `<footer>` element with `aria-label="Site footer"`
2. **Heading hierarchy**: Use H2 or H3 for column headings (hidden visually if needed)
3. **Link text**: Descriptive, not "Click here" — "Privacy Policy" not "Policy"
4. **Social links**: `aria-label` on each (icons have no visible text)
5. **Newsletter form**: `<label>` for email input, form validation messages
6. **Language selector**: `aria-label="Select language"`, current language indicated
7. **External links**: Consider indicating external links (opens in new tab)
8. **Contrast**: Text meets WCAG AA on dark backgrounds (gray-400 on gray-900 = 5.5:1)
9. **Skip links**: Footer is last in DOM — no skip link needed, but ensure Tab order is logical

---

## Navigation + Footer Performance

1. **Render-blocking**: Navigation CSS should be inlined or in critical CSS path
2. **Font loading**: Nav text should use system fonts or preloaded web fonts to prevent FOUT
3. **Logo**: Use SVG for crisp rendering at any size, inline for critical above-fold nav
4. **Mega menu**: Lazy-load mega menu content on hover intent (100ms delay before fetch)
5. **Mobile menu**: Menu HTML can be conditionally rendered (not just hidden) to reduce DOM size
6. **Footer**: Below fold — can use `content-visibility: auto` for rendering optimization
7. **Social icons**: Use inline SVGs, not icon font libraries (smaller, more reliable)
8. **Analytics**: Track nav link clicks to understand navigation patterns and optimize IA
