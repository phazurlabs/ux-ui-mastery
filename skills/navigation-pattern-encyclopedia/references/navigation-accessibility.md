# Navigation Accessibility — Complete Reference

> Complete navigation accessibility guide covering ARIA landmarks, keyboard navigation, screen reader patterns, focus management, mobile accessibility, and production-ready accessible component code.

---

## Why Navigation Accessibility Is Non-Negotiable

Navigation is the single most critical component for accessibility. If a user cannot navigate your product, they cannot use it — period. The impact is not hypothetical:

- **15-20% of the global population** has some form of disability (WHO, 2023)
- **8% of men** have color vision deficiency (cannot rely on color alone for active states)
- **Keyboard-only users** include power users, people with motor disabilities, and screen reader users
- **Legal exposure**: Navigation failures are among the top 5 most-cited issues in ADA/Section 508 lawsuits
- **SEO impact**: Accessible navigation with proper semantics improves search engine crawlability

Navigation accessibility is not a separate concern bolted on after design — it is a structural requirement that must be designed from the start.

---

## ARIA Landmarks for Navigation

ARIA landmarks create a page structure that screen reader users can navigate between using shortcut keys (e.g., D key in NVDA to jump between landmarks, VO+U in VoiceOver to list landmarks).

### Landmark Elements and Roles

| HTML Element | ARIA Role | Purpose | Usage |
|-------------|-----------|---------|-------|
| `<header>` | `banner` | Site header | One per page (top-level only) |
| `<nav>` | `navigation` | Navigation region | Multiple allowed, each needs `aria-label` |
| `<main>` | `main` | Primary content | One per page |
| `<aside>` | `complementary` | Secondary content | Sidebars, related links |
| `<footer>` | `contentinfo` | Site footer | One per page (top-level only) |
| `<section>` | `region` | Named section | Only when it has an `aria-label` |
| `<form>` | `form` | Form region | Only when it has an `aria-label` |
| `<search>` | `search` | Search region | New HTML element (2023+) |

### Multiple Navigation Regions

When a page has multiple `<nav>` elements, each must have a unique `aria-label` to distinguish them:

```html
<nav aria-label="Main">
  <!-- Primary navigation links -->
</nav>

<nav aria-label="Breadcrumb">
  <!-- Breadcrumb trail -->
</nav>

<nav aria-label="Account">
  <!-- Account/utility navigation -->
</nav>

<nav aria-label="Related articles">
  <!-- Related content links -->
</nav>

<nav aria-label="Pagination">
  <!-- Page navigation controls -->
</nav>
```

Screen reader announcement: "Main navigation landmark", "Breadcrumb navigation landmark", etc.

### Complete Page Landmark Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Page Title - Site Name</title>
</head>
<body>
  <!-- Skip link: first focusable element -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Site header with utility nav -->
  <header>
    <a href="/" aria-label="Home - Site Name">
      <img src="/logo.svg" alt="Site Name" />
    </a>

    <!-- Primary navigation -->
    <nav aria-label="Main">
      <ul>
        <li><a href="/products" aria-current="page">Products</a></li>
        <li><a href="/pricing">Pricing</a></li>
        <li><a href="/docs">Documentation</a></li>
        <li><a href="/blog">Blog</a></li>
      </ul>
    </nav>

    <!-- Utility navigation -->
    <nav aria-label="Account">
      <ul>
        <li><a href="/search" aria-label="Search">Search</a></li>
        <li><a href="/account">Account</a></li>
        <li><a href="/cart" aria-label="Cart, 3 items">Cart (3)</a></li>
      </ul>
    </nav>
  </header>

  <!-- Breadcrumb navigation -->
  <nav aria-label="Breadcrumb">
    <ol>
      <li><a href="/">Home</a></li>
      <li><a href="/products">Products</a></li>
      <li><span aria-current="page">Running Shoes</span></li>
    </ol>
  </nav>

  <!-- Main content -->
  <main id="main-content">
    <h1>Running Shoes</h1>
    <!-- Page content -->

    <!-- In-page table of contents -->
    <nav aria-label="On this page">
      <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#reviews">Reviews</a></li>
      </ul>
    </nav>
  </main>

  <!-- Sidebar -->
  <aside aria-label="Related products">
    <!-- Related content -->
  </aside>

  <!-- Footer navigation -->
  <footer>
    <nav aria-label="Footer">
      <ul>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/privacy">Privacy Policy</a></li>
        <li><a href="/terms">Terms of Service</a></li>
      </ul>
    </nav>
  </footer>
</body>
</html>
```

---

## Skip Navigation

### Why Skip Links Matter

Screen reader and keyboard users must Tab through every navigation item to reach the main content. On a site with 20 nav items, that means 20 Tab presses before reaching the content — on every single page load. Skip links solve this by providing a shortcut.

### Implementation

```html
<!-- First element inside <body> -->
<a href="#main-content" class="skip-link">Skip to main content</a>

<!-- Additional skip links for complex layouts -->
<a href="#main-content" class="skip-link">Skip to main content</a>
<a href="#primary-nav" class="skip-link">Skip to navigation</a>
<a href="#search" class="skip-link">Skip to search</a>
```

### CSS (Visible on Focus Only)

```css
.skip-link {
  /* Visually hidden by default */
  position: absolute;
  top: -100%;
  left: 16px;
  z-index: 100000; /* Above everything */

  /* Styling when visible */
  padding: 12px 24px;
  background: #111827;
  color: #ffffff;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  border-radius: 0 0 8px 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);

  /* Smooth appearance */
  transition: top 150ms ease;
}

.skip-link:focus {
  top: 0;
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}
```

### Common Mistakes
1. **Skip link target does not exist**: The `#main-content` ID must exist on a container element
2. **Target element not focusable**: Add `tabindex="-1"` to the target if it is a `<div>` or `<main>` (native `<main>` is focusable in most browsers)
3. **Skip link hidden with `display: none`**: This removes it from the tab order. Use positioning instead
4. **Multiple skip links without distinction**: Label each clearly ("Skip to content", "Skip to search")
5. **Skip link not the first focusable element**: It must be first in DOM order

```html
<!-- Target element -->
<main id="main-content" tabindex="-1">
  <!-- tabindex="-1" makes it focusable via link but not via Tab -->
```

---

## Current Page Indication

### aria-current="page"

The `aria-current` attribute tells screen readers which link represents the current page. Without it, a screen reader user must compare each link's URL to the browser address bar.

```html
<!-- Correct: aria-current on the current page link -->
<nav aria-label="Main">
  <ul>
    <li><a href="/dashboard" aria-current="page">Dashboard</a></li>
    <li><a href="/projects">Projects</a></li>
    <li><a href="/settings">Settings</a></li>
  </ul>
</nav>
```

Screen reader announces: "Dashboard, current page, link"

### Visual Current Page Indicators

The visual indicator must NOT rely solely on color. Use at least two of:
1. **Color change** (e.g., blue text)
2. **Weight change** (e.g., bold/semibold)
3. **Border/underline** (e.g., bottom border)
4. **Background change** (e.g., subtle highlight)
5. **Icon change** (e.g., filled vs. outlined icon)

```css
/* Good: uses color + border + weight */
.nav-link[aria-current="page"] {
  color: #2563eb;
  font-weight: 600;
  border-bottom: 2px solid #2563eb;
}

/* Bad: color only */
.nav-link.active {
  color: #2563eb;
}
```

### aria-current Values
| Value | Use Case |
|-------|----------|
| `page` | Current page in navigation |
| `step` | Current step in a stepper/wizard |
| `location` | Current location in a breadcrumb |
| `date` | Current date in a calendar |
| `true` | Generic current item |

---

## Expanded/Collapsed State

### aria-expanded

Any element that toggles visibility of another element must communicate its state:

```html
<!-- Collapsed state -->
<button aria-expanded="false" aria-controls="submenu-products">
  Products
  <svg aria-hidden="true"><!-- chevron icon --></svg>
</button>
<ul id="submenu-products" hidden>
  <li><a href="/products/web">Web Platform</a></li>
  <li><a href="/products/mobile">Mobile SDK</a></li>
  <li><a href="/products/api">API</a></li>
</ul>

<!-- Expanded state -->
<button aria-expanded="true" aria-controls="submenu-products">
  Products
  <svg aria-hidden="true"><!-- chevron icon --></svg>
</button>
<ul id="submenu-products">
  <li><a href="/products/web">Web Platform</a></li>
  <li><a href="/products/mobile">Mobile SDK</a></li>
  <li><a href="/products/api">API</a></li>
</ul>
```

### Key Requirements
- `aria-expanded` must toggle between `"true"` and `"false"` (strings, not boolean)
- `aria-controls` must reference the ID of the controlled element
- The controlled element should use the `hidden` attribute when collapsed
- The trigger must be a `<button>` (not a `<div>` or `<span>`)
- The chevron/arrow icon must have `aria-hidden="true"` (it is decorative)

### Screen Reader Announcement
- Collapsed: "Products, collapsed, button"
- Expanded: "Products, expanded, button"
- User presses Enter: "Products, expanded, button" + submenu items become navigable

---

## Keyboard Navigation Patterns

### Standard Keyboard Interactions

#### Navigation Bar (Simple Links)
| Key | Action |
|-----|--------|
| Tab | Move to next link in the nav |
| Shift+Tab | Move to previous link |
| Enter | Activate the focused link |

Navigation bars with simple links should use standard Tab navigation. Each link is a separate Tab stop.

#### Menu Bar (role="menubar")
| Key | Action |
|-----|--------|
| Left/Right Arrow | Move between top-level menu items |
| Down Arrow | Open submenu of focused item |
| Up Arrow | Move to previous submenu item, or close submenu |
| Enter | Activate the focused item |
| Escape | Close current submenu, return focus to parent |
| Home | Move to first item in current menu level |
| End | Move to last item in current menu level |
| Character key | Move to next item starting with that character |

**Important**: `role="menubar"` is for application-style menus (like desktop app menus), NOT for website navigation. Standard website navigation should use `<nav>` with `<ul>` and links, navigated with Tab.

#### When to Use role="menubar" vs. Simple Links
- **Simple links in `<nav>`**: For website navigation (marketing sites, blogs, e-commerce). Users Tab between items.
- **role="menubar"**: For application menus with submenus (like the menu bar in VS Code or Google Docs). Users Arrow between items. Only one item in the bar is tabbable (roving tabindex).

### Roving Tabindex Pattern

For menu bars and tab lists, only one item is in the Tab order at a time. Arrow keys move focus between items (roving tabindex):

```tsx
function MenuBar({ items }: { items: MenuItem[] }) {
  const [focusIndex, setFocusIndex] = useState(0);
  const itemRefs = useRef<(HTMLButtonElement | null)[]>([]);

  useEffect(() => {
    itemRefs.current[focusIndex]?.focus();
  }, [focusIndex]);

  const handleKeyDown = (e: React.KeyboardEvent, index: number) => {
    switch (e.key) {
      case 'ArrowRight':
        e.preventDefault();
        setFocusIndex((index + 1) % items.length);
        break;
      case 'ArrowLeft':
        e.preventDefault();
        setFocusIndex((index - 1 + items.length) % items.length);
        break;
      case 'Home':
        e.preventDefault();
        setFocusIndex(0);
        break;
      case 'End':
        e.preventDefault();
        setFocusIndex(items.length - 1);
        break;
    }
  };

  return (
    <nav aria-label="Main">
      <ul role="menubar">
        {items.map((item, i) => (
          <li key={item.id} role="none">
            <button
              ref={el => itemRefs.current[i] = el}
              role="menuitem"
              tabIndex={i === focusIndex ? 0 : -1}
              onKeyDown={(e) => handleKeyDown(e, i)}
            >
              {item.label}
            </button>
          </li>
        ))}
      </ul>
    </nav>
  );
}
```

### Tab List Pattern (role="tablist")

```html
<div role="tablist" aria-label="Content sections">
  <button role="tab" id="tab-1" aria-selected="true" aria-controls="panel-1" tabindex="0">
    Overview
  </button>
  <button role="tab" id="tab-2" aria-selected="false" aria-controls="panel-2" tabindex="-1">
    Features
  </button>
  <button role="tab" id="tab-3" aria-selected="false" aria-controls="panel-3" tabindex="-1">
    Reviews
  </button>
</div>

<div role="tabpanel" id="panel-1" aria-labelledby="tab-1" tabindex="0">
  <!-- Overview content -->
</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" tabindex="0" hidden>
  <!-- Features content -->
</div>
<div role="tabpanel" id="panel-3" aria-labelledby="tab-3" tabindex="0" hidden>
  <!-- Reviews content -->
</div>
```

**Key rules for tabs:**
- Only the selected tab has `tabindex="0"`; others have `tabindex="-1"`
- `aria-selected="true"` only on the active tab
- Arrow keys move between tabs (Left/Right for horizontal, Up/Down for vertical)
- Tab key moves focus from the tab to the tab panel content
- Hidden panels use the `hidden` attribute

---

## Focus Management

### Focus Trapping in Modal Navigation (Mobile Menus, Overlays)

When a mobile menu opens, focus must be "trapped" inside the menu — Tab should cycle through menu items and not escape to the content behind.

```tsx
function useFocusTrap(containerRef: React.RefObject<HTMLElement>, isOpen: boolean) {
  useEffect(() => {
    if (!isOpen || !containerRef.current) return;

    const container = containerRef.current;
    const focusableElements = container.querySelectorAll<HTMLElement>(
      'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
    );

    const firstFocusable = focusableElements[0];
    const lastFocusable = focusableElements[focusableElements.length - 1];

    // Focus the first element when menu opens
    firstFocusable?.focus();

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key !== 'Tab') return;

      if (e.shiftKey) {
        // Shift+Tab: if on first element, wrap to last
        if (document.activeElement === firstFocusable) {
          e.preventDefault();
          lastFocusable?.focus();
        }
      } else {
        // Tab: if on last element, wrap to first
        if (document.activeElement === lastFocusable) {
          e.preventDefault();
          firstFocusable?.focus();
        }
      }
    };

    container.addEventListener('keydown', handleKeyDown);
    return () => container.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, containerRef]);
}
```

### Focus Restoration on Menu Close

When a modal menu closes, focus must return to the element that triggered the menu:

```tsx
function useMenuFocus(isOpen: boolean) {
  const triggerRef = useRef<HTMLElement | null>(null);

  // Save the trigger element when menu opens
  useEffect(() => {
    if (isOpen) {
      triggerRef.current = document.activeElement as HTMLElement;
    }
  }, [isOpen]);

  // Restore focus when menu closes
  useEffect(() => {
    if (!isOpen && triggerRef.current) {
      triggerRef.current.focus();
      triggerRef.current = null;
    }
  }, [isOpen]);
}
```

### Focus Visible Indicator

All interactive navigation elements must have a visible focus indicator that meets WCAG 2.2 Level AA requirements:

```css
/* Default browser focus (not sufficient for WCAG 2.2) */
:focus {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}

/* Enhanced focus visible (only show for keyboard users) */
:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
  border-radius: 4px;
}

/* Remove focus ring for mouse users */
:focus:not(:focus-visible) {
  outline: none;
}

/* WCAG 2.2 requirements for focus appearance:
   - Focus indicator must have >= 3:1 contrast with adjacent colors
   - Focus indicator area >= 2px thick outline or equivalent
   - Focus indicator must not be entirely hidden by other content
*/

/* High contrast mode support */
@media (forced-colors: active) {
  :focus-visible {
    outline: 2px solid CanvasText;
  }
}
```

### Managing Focus After Route Changes (SPA)

Single-page applications must manage focus when the route changes. Without management, focus stays on the clicked link (which may no longer be visible) and screen readers do not announce the new page.

```tsx
// React Router focus management
function FocusOnRouteChange() {
  const location = useLocation();
  const mainRef = useRef<HTMLElement>(null);

  useEffect(() => {
    // Move focus to main content on route change
    if (mainRef.current) {
      mainRef.current.focus();
    }

    // Announce the new page to screen readers
    const title = document.title;
    const announcement = document.getElementById('route-announcement');
    if (announcement) {
      announcement.textContent = `Navigated to ${title}`;
    }
  }, [location.pathname]);

  return (
    <>
      <div
        id="route-announcement"
        role="status"
        aria-live="polite"
        aria-atomic="true"
        className="sr-only"
      />
      <main ref={mainRef} id="main-content" tabIndex={-1}>
        {/* Route content */}
      </main>
    </>
  );
}
```

---

## Screen Reader Navigation Patterns

### How Screen Reader Users Navigate

Screen reader users do not read pages linearly. They use shortcuts to jump between elements:

| Action | VoiceOver (Mac) | NVDA (Windows) | JAWS (Windows) |
|--------|----------------|----------------|-----------------|
| List landmarks | VO+U (Landmarks rotor) | D / Shift+D | R / Shift+R |
| Next heading | VO+Cmd+H | H | H |
| Next link | VO+Cmd+L | K | Tab |
| List all links | VO+U (Links rotor) | Insert+F7 | Insert+F7 |
| Next list | - | L | L |
| Next form field | VO+Cmd+J | F | F |
| Navigate table | VO+Arrow keys | Ctrl+Alt+Arrows | Ctrl+Alt+Arrows |

### What Screen Readers Announce for Navigation

For each navigation element, the screen reader announces:

**Link**: "[Link text], link" or "[Link text], visited link"
```html
<a href="/products">Products</a>
<!-- Announces: "Products, link" -->
```

**Current page link**: "[Link text], current page, link"
```html
<a href="/products" aria-current="page">Products</a>
<!-- Announces: "Products, current page, link" -->
```

**Button with expanded menu**: "[Button text], expanded, button" or "[Button text], collapsed, button"
```html
<button aria-expanded="true" aria-controls="submenu">Products</button>
<!-- Announces: "Products, expanded, button" -->
```

**Navigation landmark**: "Main, navigation" (when entering the landmark)
```html
<nav aria-label="Main">
<!-- Announces: "Main, navigation" -->
```

**Badge count**: Include count in accessible name
```html
<a href="/notifications" aria-label="Notifications, 5 unread">
  <span>Notifications</span>
  <span aria-hidden="true" class="badge">5</span>
</a>
<!-- Announces: "Notifications, 5 unread, link" -->
```

### Common Screen Reader Issues with Navigation

| Issue | Cause | Fix |
|-------|-------|-----|
| "Link, link, link" (no text) | Icon-only links without labels | Add `aria-label` or visually hidden text |
| Menu state not announced | Missing `aria-expanded` | Add `aria-expanded="true/false"` to trigger |
| Cannot distinguish navs | Multiple `<nav>` without labels | Add unique `aria-label` to each `<nav>` |
| Current page not announced | Missing `aria-current` | Add `aria-current="page"` to active link |
| Focus lost after menu close | No focus restoration | Return focus to trigger on close |
| New content not announced | Dynamic content loaded silently | Use `aria-live="polite"` for announcements |
| Trapped in menu | No Escape key handler | Add Escape to close menu and restore focus |
| Badge count not read | Badge is decorative `<span>` only | Include count in `aria-label` of parent link |
| Submenu items not reachable | Submenu rendered but hidden from AT | Use `hidden` attribute or `aria-hidden="true"` |
| Duplicate announcements | Both `aria-label` and visible text | Use `aria-label` only when it differs from visible text; otherwise rely on text content |

---

## Accessible Navigation Component: Complete Example

### Responsive Navigation with Hamburger Menu

```tsx
import { useState, useRef, useEffect, useCallback } from 'react';

interface NavLink {
  label: string;
  href: string;
}

interface AccessibleNavProps {
  logo: React.ReactNode;
  links: NavLink[];
  currentPath: string;
}

function AccessibleNav({ logo, links, currentPath }: AccessibleNavProps) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);
  const triggerRef = useRef<HTMLButtonElement>(null);

  // Close on Escape
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && mobileMenuOpen) {
        setMobileMenuOpen(false);
        triggerRef.current?.focus();
      }
    };
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [mobileMenuOpen]);

  // Focus trap
  useEffect(() => {
    if (!mobileMenuOpen || !menuRef.current) return;

    const focusable = menuRef.current.querySelectorAll<HTMLElement>(
      'a[href], button:not([disabled])'
    );
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    first?.focus();

    const handleTab = (e: KeyboardEvent) => {
      if (e.key !== 'Tab') return;
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last?.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first?.focus();
      }
    };

    menuRef.current.addEventListener('keydown', handleTab);
    const currentMenu = menuRef.current;
    return () => currentMenu.removeEventListener('keydown', handleTab);
  }, [mobileMenuOpen]);

  // Prevent body scroll when menu is open
  useEffect(() => {
    if (mobileMenuOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => { document.body.style.overflow = ''; };
  }, [mobileMenuOpen]);

  return (
    <header className="site-header">
      {/* Skip link */}
      <a href="#main-content" className="skip-link">
        Skip to main content
      </a>

      {/* Logo */}
      <a href="/" aria-label="Home">
        {logo}
      </a>

      {/* Desktop navigation */}
      <nav aria-label="Main" className="desktop-nav">
        <ul>
          {links.map(link => (
            <li key={link.href}>
              <a
                href={link.href}
                aria-current={currentPath === link.href ? 'page' : undefined}
              >
                {link.label}
              </a>
            </li>
          ))}
        </ul>
      </nav>

      {/* Mobile menu trigger */}
      <button
        ref={triggerRef}
        className="mobile-menu-trigger"
        aria-expanded={mobileMenuOpen}
        aria-controls="mobile-menu"
        aria-label={mobileMenuOpen ? 'Close menu' : 'Open menu'}
        onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
      >
        {mobileMenuOpen ? (
          <XIcon aria-hidden="true" />
        ) : (
          <MenuIcon aria-hidden="true" />
        )}
      </button>

      {/* Mobile menu */}
      {mobileMenuOpen && (
        <>
          <div
            className="mobile-menu-backdrop"
            onClick={() => {
              setMobileMenuOpen(false);
              triggerRef.current?.focus();
            }}
            aria-hidden="true"
          />
          <div
            ref={menuRef}
            id="mobile-menu"
            className="mobile-menu"
            role="dialog"
            aria-label="Navigation menu"
            aria-modal="true"
          >
            <button
              className="mobile-menu-close"
              onClick={() => {
                setMobileMenuOpen(false);
                triggerRef.current?.focus();
              }}
              aria-label="Close menu"
            >
              <XIcon aria-hidden="true" />
            </button>
            <nav aria-label="Main">
              <ul>
                {links.map(link => (
                  <li key={link.href}>
                    <a
                      href={link.href}
                      aria-current={currentPath === link.href ? 'page' : undefined}
                      onClick={() => setMobileMenuOpen(false)}
                    >
                      {link.label}
                    </a>
                  </li>
                ))}
              </ul>
            </nav>
          </div>
        </>
      )}
    </header>
  );
}
```

---

## Accessible Dropdown Menu Component

```tsx
interface DropdownItem {
  label: string;
  href: string;
}

interface DropdownProps {
  label: string;
  items: DropdownItem[];
  currentPath: string;
}

function AccessibleDropdown({ label, items, currentPath }: DropdownProps) {
  const [open, setOpen] = useState(false);
  const [focusIndex, setFocusIndex] = useState(-1);
  const triggerRef = useRef<HTMLButtonElement>(null);
  const listRef = useRef<HTMLUListElement>(null);

  useEffect(() => {
    if (open && focusIndex >= 0) {
      const items = listRef.current?.querySelectorAll<HTMLAnchorElement>('a');
      items?.[focusIndex]?.focus();
    }
  }, [focusIndex, open]);

  const handleTriggerKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      setOpen(true);
      setFocusIndex(0);
    }
  };

  const handleItemKeyDown = (e: React.KeyboardEvent, index: number) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        setFocusIndex(Math.min(index + 1, items.length - 1));
        break;
      case 'ArrowUp':
        e.preventDefault();
        if (index === 0) {
          setOpen(false);
          setFocusIndex(-1);
          triggerRef.current?.focus();
        } else {
          setFocusIndex(index - 1);
        }
        break;
      case 'Escape':
        e.preventDefault();
        setOpen(false);
        setFocusIndex(-1);
        triggerRef.current?.focus();
        break;
      case 'Home':
        e.preventDefault();
        setFocusIndex(0);
        break;
      case 'End':
        e.preventDefault();
        setFocusIndex(items.length - 1);
        break;
    }
  };

  return (
    <div className="dropdown" onBlur={(e) => {
      if (!e.currentTarget.contains(e.relatedTarget)) {
        setOpen(false);
        setFocusIndex(-1);
      }
    }}>
      <button
        ref={triggerRef}
        aria-expanded={open}
        aria-haspopup="true"
        aria-controls="dropdown-menu"
        onKeyDown={handleTriggerKeyDown}
        onClick={() => {
          setOpen(!open);
          if (!open) setFocusIndex(0);
        }}
      >
        {label}
        <ChevronDown aria-hidden="true" />
      </button>

      {open && (
        <ul ref={listRef} id="dropdown-menu" role="menu">
          {items.map((item, i) => (
            <li key={item.href} role="none">
              <a
                href={item.href}
                role="menuitem"
                tabIndex={i === focusIndex ? 0 : -1}
                aria-current={currentPath === item.href ? 'page' : undefined}
                onKeyDown={(e) => handleItemKeyDown(e, i)}
              >
                {item.label}
              </a>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

---

## Mobile Navigation Accessibility

### iOS VoiceOver

- Tab bar items: VoiceOver reads "Tab, [Label], [Position] of [Total], [Selected status]"
  - Example: "Home tab, 1 of 4, selected"
- Swipe left/right to move between tab items
- Double-tap to activate
- Hamburger menu: must announce "Menu, button" and state change when toggled

### Android TalkBack

- Bottom nav items: TalkBack reads "[Label], tab, [Position] of [Total], [selected]"
- Swipe right to move to next item
- Double-tap to activate
- Navigation drawer: announce "Navigation menu, showing" when opened

### Touch Target Sizing

| Platform | Minimum Target | Recommended Target | Spacing |
|----------|---------------|-------------------|---------|
| WCAG 2.2 Level AA | 24x24 CSS px | 44x44 CSS px | 8px |
| Apple HIG | 44x44 pt | 44x44 pt | 8pt |
| Material Design | 48x48 dp | 48x48 dp | 8dp |

```css
/* Ensure touch targets meet minimum size */
.nav-item {
  min-width: 44px;
  min-height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Use padding to increase touch target without increasing visual size */
.nav-link {
  padding: 12px 16px; /* Creates a 44px+ touch target */
  margin: -12px -16px; /* Visual alignment unchanged */
}
```

---

## WCAG Navigation Requirements Summary

| Criterion | Level | Requirement |
|-----------|-------|-------------|
| 1.3.1 Info and Relationships | A | Navigation structure conveyed through proper HTML/ARIA |
| 1.3.6 Identify Purpose | AAA | Input purpose identifiable (landmark roles) |
| 2.1.1 Keyboard | A | All navigation operable via keyboard |
| 2.1.2 No Keyboard Trap | A | Focus can move away from any element |
| 2.4.1 Bypass Blocks | A | Skip navigation link provided |
| 2.4.3 Focus Order | A | Focus order matches visual/logical order |
| 2.4.4 Link Purpose (In Context) | A | Link purpose determinable from link text or context |
| 2.4.5 Multiple Ways | AA | Multiple ways to find pages (nav, search, sitemap) |
| 2.4.7 Focus Visible | AA | Keyboard focus indicator is visible |
| 2.4.8 Location | AAA | User's location within site is identifiable |
| 2.4.11 Focus Not Obscured | AA | Focused element is not fully hidden by other content |
| 2.4.12 Focus Not Obscured (Enhanced) | AAA | No part of focused element is hidden |
| 2.4.13 Focus Appearance | AAA | Focus indicator has sufficient size and contrast |
| 3.2.3 Consistent Navigation | AA | Navigation order consistent across pages |
| 3.2.4 Consistent Identification | AA | Components with same function identified consistently |
| 4.1.2 Name, Role, Value | A | All UI components have accessible name, role, and state |

---

## Navigation Accessibility Testing Checklist

### Automated Testing (Run First)
- [ ] axe-core or Lighthouse audit shows no navigation-related violations
- [ ] All images in navigation have alt text
- [ ] All links have discernible text (no empty links)
- [ ] All ARIA attributes are valid and properly used
- [ ] Color contrast ratios meet 4.5:1 for text, 3:1 for large text
- [ ] Focus indicators meet 3:1 contrast ratio

### Keyboard Testing (Manual)
- [ ] Tab through entire navigation — every item is reachable
- [ ] Shift+Tab moves backwards through navigation
- [ ] Enter activates links and buttons
- [ ] Escape closes any open menus/dropdowns
- [ ] Arrow keys work within menu bars and tab lists
- [ ] Focus never gets trapped (except intentionally in modals)
- [ ] Focus order matches visual order
- [ ] Skip link works and skips to main content
- [ ] Focus returns to trigger when menus close

### Screen Reader Testing (Manual)
- [ ] All navigation landmarks are announced with labels
- [ ] Current page is announced ("current page" for active nav item)
- [ ] Menu open/close state is announced ("expanded"/"collapsed")
- [ ] Badge counts are announced with parent link
- [ ] Links have meaningful text (no "click here" or "read more")
- [ ] Decorative icons are hidden from screen readers (aria-hidden)
- [ ] Dynamic navigation changes are announced (aria-live)

### Mobile Accessibility Testing
- [ ] VoiceOver (iOS) can navigate all menu items
- [ ] TalkBack (Android) can navigate all menu items
- [ ] Touch targets are at least 44x44pt / 48x48dp
- [ ] No gesture is the only way to navigate (always provide visible alternative)
- [ ] Screen reader users can open and close mobile menus
- [ ] Focus is managed when mobile menus open and close

### Zoom and Reflow Testing
- [ ] Navigation is usable at 200% browser zoom
- [ ] Navigation reflows at 400% zoom (WCAG 1.4.10 Reflow)
- [ ] No horizontal scrollbar at 320px viewport width (WCAG 1.4.10)
- [ ] Text in navigation scales with user font size preferences
