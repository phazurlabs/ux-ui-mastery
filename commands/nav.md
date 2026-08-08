---
name: nav
description: "Generate responsive navigation systems — top bar, sidebar, bottom tabs, command palette, mega menu, with ARIA and dark mode."
argument-hint: "[product and navigation type]"
---

# Nav — Navigation System Builder

## Before running

This command needs a product and the kind of navigation it needs.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate complete, production-ready navigation components with responsive transformations, keyboard navigation, ARIA landmarks, and dark mode support. Output React + Tailwind code that is copy-paste ready.

## Generation Protocol

### Step 0: Gather Input

Before generating, collect:

1. **Nav pattern**: Which navigation pattern does the user need?
   - **Top Bar** — Horizontal navigation bar at the top of the page (logo, links, actions)
   - **Sidebar** — Vertical navigation panel on the left (collapsible, with groups and icons)
   - **Bottom Tabs** — Mobile tab bar fixed to the bottom (iOS/Android pattern)
   - **Command Palette** — Keyboard-triggered search overlay (Cmd+K pattern)
   - **Mega Menu** — Multi-column dropdown triggered from top bar items
   - **Hamburger** — Slide-out mobile menu triggered by hamburger icon
   - **Breadcrumbs** — Hierarchical path showing current location
   - **Tab Bar** — Horizontal content tabs (not navigation, but content switching)
   - **Combined** — Top bar for desktop + bottom tabs for mobile (common responsive pattern)
   - **Custom** — User describes their navigation requirements

2. **Navigation items**: What pages/sections appear in the nav?
   - Primary items (always visible)
   - Secondary items (overflow, "more" menu)
   - User/account actions (profile, settings, logout)
   - Call-to-action (signup, upgrade)

3. **Positioning**: How should the nav behave on scroll?
   - **Fixed/sticky** — Always visible (default for top bars and bottom tabs)
   - **Static** — Scrolls with content
   - **Auto-hide** — Hides on scroll down, shows on scroll up
   - **Sticky after threshold** — Becomes sticky after scrolling past hero

4. **Prior Sumi outputs**: Check for `/layout` (layout shell to insert nav into), `/tokens` (colors, spacing), `/taste` (brand personality for nav style). Consume if available.

If no pattern is specified, ask. Do not guess.

### Step 1: TOP BAR NAVIGATION

The most common navigation pattern. Fixed horizontal bar with logo, links, and actions.

**Desktop top bar**:
```tsx
'use client';

import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

const navigation = [
  { name: 'Dashboard', href: '/dashboard' },
  { name: 'Projects', href: '/projects' },
  { name: 'Team', href: '/team' },
  { name: 'Reports', href: '/reports' },
];

export function TopBar() {
  const pathname = usePathname();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <>
      <header className="sticky top-0 z-50 border-b border-gray-200 bg-white/95 backdrop-blur supports-[backdrop-filter]:bg-white/80 dark:border-gray-800 dark:bg-gray-950/95 dark:supports-[backdrop-filter]:bg-gray-950/80">
        <nav
          className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8"
          aria-label="Main navigation"
        >
          {/* Logo */}
          <div className="flex items-center">
            <Link href="/" className="flex items-center gap-2" aria-label="Home">
              <img src="/logo.svg" alt="" className="h-8 w-auto" />
              <span className="text-lg font-semibold text-gray-900 dark:text-white">Brand</span>
            </Link>
          </div>

          {/* Desktop navigation links */}
          <div className="hidden md:flex md:items-center md:gap-1">
            {navigation.map((item) => {
              const isActive = pathname === item.href || pathname.startsWith(item.href + '/');
              return (
                <Link
                  key={item.name}
                  href={item.href}
                  className={`rounded-md px-3 py-2 text-sm font-medium transition-colors ${
                    isActive
                      ? 'bg-gray-100 text-gray-900 dark:bg-gray-800 dark:text-white'
                      : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900 dark:text-gray-400 dark:hover:bg-gray-800/50 dark:hover:text-white'
                  }`}
                  aria-current={isActive ? 'page' : undefined}
                >
                  {item.name}
                </Link>
              );
            })}
          </div>

          {/* Right side actions */}
          <div className="flex items-center gap-3">
            {/* Search button (desktop) */}
            <button
              type="button"
              className="hidden md:flex items-center gap-2 rounded-md bg-gray-100 px-3 py-1.5 text-sm text-gray-500 hover:bg-gray-200 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700"
              aria-label="Search"
            >
              <MagnifyingGlassIcon className="h-4 w-4" />
              <span>Search</span>
              <kbd className="ml-2 rounded border border-gray-300 px-1.5 py-0.5 text-xs font-medium text-gray-400 dark:border-gray-600">
                /
              </kbd>
            </button>

            {/* Notifications */}
            <button
              type="button"
              className="relative rounded-md p-2 text-gray-500 hover:bg-gray-100 hover:text-gray-900 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-white"
              aria-label="View notifications"
            >
              <BellIcon className="h-5 w-5" />
              {/* Notification badge */}
              <span className="absolute right-1.5 top-1.5 h-2 w-2 rounded-full bg-red-500" aria-hidden="true" />
              <span className="sr-only">3 unread notifications</span>
            </button>

            {/* User menu */}
            <UserMenu />

            {/* Mobile hamburger button */}
            <button
              type="button"
              className="md:hidden rounded-md p-2 text-gray-500 hover:bg-gray-100 hover:text-gray-900 dark:text-gray-400 dark:hover:bg-gray-800"
              onClick={() => setMobileMenuOpen(true)}
              aria-expanded={mobileMenuOpen}
              aria-controls="mobile-menu"
              aria-label="Open main menu"
            >
              <Bars3Icon className="h-6 w-6" />
            </button>
          </div>
        </nav>
      </header>

      {/* Mobile menu overlay */}
      <MobileMenu
        open={mobileMenuOpen}
        onClose={() => setMobileMenuOpen(false)}
        navigation={navigation}
        currentPath={pathname}
      />

      {/* Skip link (must be first focusable element on page) */}
      {/* Place this BEFORE the header in the actual DOM */}
    </>
  );
}
```

**Skip link** (place before all other content in the page):
```tsx
<a
  href="#main-content"
  className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[100] focus:rounded-md focus:bg-white focus:px-4 focus:py-2 focus:text-sm focus:font-medium focus:text-gray-900 focus:shadow-lg focus:ring-2 focus:ring-indigo-500 dark:focus:bg-gray-900 dark:focus:text-white"
>
  Skip to main content
</a>
```

### Step 2: MOBILE MENU (Hamburger Slide-Out)

Full-screen or slide-out panel for mobile navigation.

```tsx
'use client';

import { useEffect, useRef } from 'react';
import Link from 'next/link';

interface MobileMenuProps {
  open: boolean;
  onClose: () => void;
  navigation: { name: string; href: string }[];
  currentPath: string;
}

export function MobileMenu({ open, onClose, navigation, currentPath }: MobileMenuProps) {
  const menuRef = useRef<HTMLDivElement>(null);
  const closeButtonRef = useRef<HTMLButtonElement>(null);

  // Focus trap and escape key
  useEffect(() => {
    if (!open) return;

    // Focus close button on open
    closeButtonRef.current?.focus();

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
        return;
      }

      // Focus trap
      if (e.key === 'Tab' && menuRef.current) {
        const focusableElements = menuRef.current.querySelectorAll<HTMLElement>(
          'a, button, input, textarea, select, [tabindex]:not([tabindex="-1"])'
        );
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];

        if (e.shiftKey && document.activeElement === firstElement) {
          e.preventDefault();
          lastElement.focus();
        } else if (!e.shiftKey && document.activeElement === lastElement) {
          e.preventDefault();
          firstElement.focus();
        }
      }
    };

    // Prevent body scroll when menu is open
    document.body.style.overflow = 'hidden';
    document.addEventListener('keydown', handleKeyDown);

    return () => {
      document.body.style.overflow = '';
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [open, onClose]);

  if (!open) return null;

  return (
    <div className="fixed inset-0 z-50 md:hidden" role="dialog" aria-modal="true" aria-label="Mobile navigation">
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-gray-900/50 backdrop-blur-sm"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Menu panel */}
      <div
        ref={menuRef}
        className="fixed inset-y-0 right-0 w-full max-w-sm bg-white shadow-xl dark:bg-gray-950"
      >
        {/* Header */}
        <div className="flex items-center justify-between border-b border-gray-200 px-4 py-4 dark:border-gray-800">
          <Link href="/" className="flex items-center gap-2" onClick={onClose}>
            <img src="/logo.svg" alt="" className="h-8 w-auto" />
            <span className="text-lg font-semibold text-gray-900 dark:text-white">Brand</span>
          </Link>
          <button
            ref={closeButtonRef}
            type="button"
            className="rounded-md p-2 text-gray-500 hover:bg-gray-100 hover:text-gray-900 dark:text-gray-400 dark:hover:bg-gray-800"
            onClick={onClose}
            aria-label="Close menu"
          >
            <XMarkIcon className="h-6 w-6" />
          </button>
        </div>

        {/* Navigation links */}
        <nav className="px-4 py-6" aria-label="Mobile navigation">
          <ul className="space-y-1" role="list">
            {navigation.map((item) => {
              const isActive = currentPath === item.href || currentPath.startsWith(item.href + '/');
              return (
                <li key={item.name}>
                  <Link
                    href={item.href}
                    onClick={onClose}
                    className={`block rounded-md px-3 py-3 text-base font-medium transition-colors ${
                      isActive
                        ? 'bg-gray-100 text-gray-900 dark:bg-gray-800 dark:text-white'
                        : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900 dark:text-gray-400 dark:hover:bg-gray-800/50 dark:hover:text-white'
                    }`}
                    aria-current={isActive ? 'page' : undefined}
                  >
                    {item.name}
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>

        {/* Bottom actions */}
        <div className="absolute bottom-0 left-0 right-0 border-t border-gray-200 p-4 dark:border-gray-800">
          <button className="w-full rounded-md bg-indigo-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500">
            Get Started
          </button>
        </div>
      </div>
    </div>
  );
}
```

### Step 3: SIDEBAR NAVIGATION

Vertical sidebar with groups, icons, collapsible sections, and active state tracking.

```tsx
'use client';

import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

const sidebarNavigation = [
  {
    group: 'Main',
    items: [
      { name: 'Dashboard', href: '/dashboard', icon: HomeIcon },
      { name: 'Projects', href: '/projects', icon: FolderIcon },
      { name: 'Tasks', href: '/tasks', icon: ClipboardDocumentListIcon },
      { name: 'Calendar', href: '/calendar', icon: CalendarIcon },
    ],
  },
  {
    group: 'Workspace',
    items: [
      { name: 'Team', href: '/team', icon: UsersIcon },
      { name: 'Messages', href: '/messages', icon: ChatBubbleLeftIcon, badge: 5 },
      { name: 'Documents', href: '/documents', icon: DocumentTextIcon },
    ],
  },
  {
    group: 'Account',
    items: [
      { name: 'Settings', href: '/settings', icon: CogIcon },
      { name: 'Billing', href: '/billing', icon: CreditCardIcon },
    ],
  },
];

export function Sidebar() {
  const pathname = usePathname();
  const [collapsed, setCollapsed] = useState(false);

  return (
    <aside
      className={`fixed inset-y-0 left-0 z-40 flex flex-col border-r border-gray-200 bg-white transition-[width] duration-200 dark:border-gray-800 dark:bg-gray-950 ${
        collapsed ? 'w-16' : 'w-64'
      }`}
      aria-label="Sidebar navigation"
    >
      {/* Logo area */}
      <div className="flex h-16 items-center border-b border-gray-200 px-4 dark:border-gray-800">
        <Link href="/" className="flex items-center gap-2" aria-label="Home">
          <img src="/logo.svg" alt="" className="h-8 w-8 flex-shrink-0" />
          {!collapsed && (
            <span className="text-lg font-semibold text-gray-900 dark:text-white">Brand</span>
          )}
        </Link>
      </div>

      {/* Navigation */}
      <nav className="flex-1 overflow-y-auto px-2 py-4" aria-label="Sidebar">
        {sidebarNavigation.map((group) => (
          <div key={group.group} className="mb-6">
            {/* Group label — hidden when collapsed */}
            {!collapsed && (
              <h3 className="mb-2 px-3 text-xs font-semibold uppercase tracking-wider text-gray-500 dark:text-gray-400">
                {group.group}
              </h3>
            )}

            <ul className="space-y-0.5" role="list">
              {group.items.map((item) => {
                const isActive = pathname === item.href || pathname.startsWith(item.href + '/');
                const Icon = item.icon;

                return (
                  <li key={item.name}>
                    <Link
                      href={item.href}
                      className={`group flex items-center gap-3 rounded-md px-3 py-2 text-sm font-medium transition-colors ${
                        isActive
                          ? 'bg-indigo-50 text-indigo-700 dark:bg-indigo-500/10 dark:text-indigo-400'
                          : 'text-gray-700 hover:bg-gray-100 hover:text-gray-900 dark:text-gray-300 dark:hover:bg-gray-800 dark:hover:text-white'
                      } ${collapsed ? 'justify-center px-2' : ''}`}
                      aria-current={isActive ? 'page' : undefined}
                      title={collapsed ? item.name : undefined}
                    >
                      <Icon
                        className={`h-5 w-5 flex-shrink-0 ${
                          isActive
                            ? 'text-indigo-600 dark:text-indigo-400'
                            : 'text-gray-400 group-hover:text-gray-600 dark:text-gray-500 dark:group-hover:text-gray-300'
                        }`}
                        aria-hidden="true"
                      />
                      {!collapsed && (
                        <>
                          <span className="flex-1">{item.name}</span>
                          {item.badge && (
                            <span className="rounded-full bg-indigo-100 px-2 py-0.5 text-xs font-medium text-indigo-700 dark:bg-indigo-500/20 dark:text-indigo-300">
                              {item.badge}
                            </span>
                          )}
                        </>
                      )}
                    </Link>
                  </li>
                );
              })}
            </ul>
          </div>
        ))}
      </nav>

      {/* Collapse toggle */}
      <div className="border-t border-gray-200 p-2 dark:border-gray-800">
        <button
          type="button"
          onClick={() => setCollapsed(!collapsed)}
          className="flex w-full items-center justify-center rounded-md p-2 text-gray-500 hover:bg-gray-100 hover:text-gray-900 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-white"
          aria-label={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}
        >
          {collapsed ? (
            <ChevronRightIcon className="h-5 w-5" />
          ) : (
            <ChevronLeftIcon className="h-5 w-5" />
          )}
        </button>
      </div>

      {/* User profile (bottom) */}
      <div className="border-t border-gray-200 p-3 dark:border-gray-800">
        <div className={`flex items-center gap-3 ${collapsed ? 'justify-center' : ''}`}>
          <img
            src="/avatar.jpg"
            alt=""
            className="h-8 w-8 rounded-full ring-2 ring-white dark:ring-gray-800"
          />
          {!collapsed && (
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium text-gray-900 truncate dark:text-white">Jane Doe</p>
              <p className="text-xs text-gray-500 truncate dark:text-gray-400">jane@example.com</p>
            </div>
          )}
        </div>
      </div>
    </aside>
  );
}
```

### Step 4: BOTTOM TABS (Mobile)

Fixed bottom tab bar for mobile applications.

```tsx
'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

const tabs = [
  { name: 'Home', href: '/', icon: HomeIcon },
  { name: 'Search', href: '/search', icon: MagnifyingGlassIcon },
  { name: 'Create', href: '/create', icon: PlusCircleIcon, accent: true },
  { name: 'Activity', href: '/activity', icon: BellIcon, badge: 3 },
  { name: 'Profile', href: '/profile', icon: UserCircleIcon },
];

export function BottomTabs() {
  const pathname = usePathname();

  return (
    <nav
      className="fixed bottom-0 left-0 right-0 z-50 border-t border-gray-200 bg-white/95 backdrop-blur supports-[backdrop-filter]:bg-white/80 dark:border-gray-800 dark:bg-gray-950/95 md:hidden"
      aria-label="Bottom navigation"
    >
      {/* Safe area padding for iOS (notch/home indicator) */}
      <div className="flex items-center justify-around pb-[env(safe-area-inset-bottom)]">
        {tabs.map((tab) => {
          const isActive = pathname === tab.href || (tab.href !== '/' && pathname.startsWith(tab.href));
          const Icon = tab.icon;

          return (
            <Link
              key={tab.name}
              href={tab.href}
              className={`relative flex flex-1 flex-col items-center gap-0.5 px-2 py-2.5 text-xs font-medium transition-colors ${
                tab.accent
                  ? 'text-indigo-600 dark:text-indigo-400'
                  : isActive
                  ? 'text-indigo-600 dark:text-indigo-400'
                  : 'text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white'
              }`}
              aria-current={isActive ? 'page' : undefined}
              aria-label={tab.badge ? `${tab.name}, ${tab.badge} new` : tab.name}
            >
              <span className="relative">
                <Icon
                  className={`h-6 w-6 ${
                    tab.accent
                      ? 'h-7 w-7'
                      : ''
                  }`}
                  aria-hidden="true"
                />
                {/* Badge */}
                {tab.badge && (
                  <span
                    className="absolute -right-1.5 -top-1 flex h-4 min-w-4 items-center justify-center rounded-full bg-red-500 px-1 text-[10px] font-bold text-white"
                    aria-hidden="true"
                  >
                    {tab.badge}
                  </span>
                )}
              </span>
              <span>{tab.name}</span>
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
```

Bottom tabs rules:
- Maximum 5 tabs (more requires "More" overflow)
- Touch targets: full width of each tab, minimum 48px height
- Active indicator: color change + optional dot/bar above icon
- Badge: positioned top-right of icon, red circle with count
- Safe area: `pb-[env(safe-area-inset-bottom)]` for iOS home indicator
- Hidden on desktop: `md:hidden`

### Step 5: COMMAND PALETTE

Keyboard-triggered search/action overlay (Cmd+K / Ctrl+K pattern).

```tsx
'use client';

import { useState, useEffect, useRef, useCallback } from 'react';

interface CommandItem {
  id: string;
  name: string;
  description?: string;
  icon?: React.ComponentType<{ className?: string }>;
  shortcut?: string;
  action: () => void;
  group: string;
}

export function CommandPalette({ commands }: { commands: CommandItem[] }) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [selectedIndex, setSelectedIndex] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);
  const listRef = useRef<HTMLUListElement>(null);

  // Filter commands based on query
  const filtered = query === ''
    ? commands
    : commands.filter((cmd) =>
        cmd.name.toLowerCase().includes(query.toLowerCase()) ||
        cmd.description?.toLowerCase().includes(query.toLowerCase())
      );

  // Group filtered results
  const grouped = filtered.reduce<Record<string, CommandItem[]>>((acc, cmd) => {
    (acc[cmd.group] ||= []).push(cmd);
    return acc;
  }, {});

  // Global keyboard shortcut to open
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setOpen((prev) => !prev);
      }
    };
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, []);

  // Focus input when opened
  useEffect(() => {
    if (open) {
      setQuery('');
      setSelectedIndex(0);
      // Delay to allow animation
      requestAnimationFrame(() => inputRef.current?.focus());
    }
  }, [open]);

  // Keyboard navigation within palette
  const handleKeyDown = useCallback((e: React.KeyboardEvent) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        setSelectedIndex((prev) => Math.min(prev + 1, filtered.length - 1));
        break;
      case 'ArrowUp':
        e.preventDefault();
        setSelectedIndex((prev) => Math.max(prev - 1, 0));
        break;
      case 'Enter':
        e.preventDefault();
        if (filtered[selectedIndex]) {
          filtered[selectedIndex].action();
          setOpen(false);
        }
        break;
      case 'Escape':
        setOpen(false);
        break;
    }
  }, [filtered, selectedIndex]);

  // Scroll selected item into view
  useEffect(() => {
    const selectedElement = listRef.current?.querySelector('[data-selected="true"]');
    selectedElement?.scrollIntoView({ block: 'nearest' });
  }, [selectedIndex]);

  if (!open) return null;

  return (
    <div className="fixed inset-0 z-[100] overflow-y-auto p-4 sm:p-6 md:p-20" role="dialog" aria-modal="true" aria-label="Command palette">
      {/* Backdrop */}
      <div className="fixed inset-0 bg-gray-900/50 backdrop-blur-sm" onClick={() => setOpen(false)} aria-hidden="true" />

      {/* Palette */}
      <div className="relative mx-auto max-w-xl rounded-xl bg-white shadow-2xl ring-1 ring-gray-950/5 dark:bg-gray-900 dark:ring-gray-800">
        {/* Search input */}
        <div className="flex items-center border-b border-gray-200 px-4 dark:border-gray-800">
          <MagnifyingGlassIcon className="h-5 w-5 text-gray-400" aria-hidden="true" />
          <input
            ref={inputRef}
            type="text"
            className="w-full border-0 bg-transparent px-3 py-4 text-sm text-gray-900 placeholder:text-gray-400 focus:outline-none focus:ring-0 dark:text-white"
            placeholder="Search commands..."
            value={query}
            onChange={(e) => {
              setQuery(e.target.value);
              setSelectedIndex(0);
            }}
            onKeyDown={handleKeyDown}
            role="combobox"
            aria-expanded="true"
            aria-controls="command-list"
            aria-activedescendant={filtered[selectedIndex] ? `command-${filtered[selectedIndex].id}` : undefined}
          />
          <kbd className="rounded border border-gray-300 px-1.5 py-0.5 text-xs font-medium text-gray-400 dark:border-gray-700">
            Esc
          </kbd>
        </div>

        {/* Results */}
        <ul
          ref={listRef}
          id="command-list"
          className="max-h-80 overflow-y-auto py-2"
          role="listbox"
        >
          {filtered.length === 0 ? (
            <li className="px-4 py-8 text-center text-sm text-gray-500">
              No results found for "{query}"
            </li>
          ) : (
            Object.entries(grouped).map(([group, items]) => (
              <li key={group} role="presentation">
                <h3 className="px-4 py-1.5 text-xs font-semibold uppercase tracking-wider text-gray-500 dark:text-gray-400">
                  {group}
                </h3>
                <ul role="group" aria-label={group}>
                  {items.map((item) => {
                    const flatIndex = filtered.indexOf(item);
                    const isSelected = flatIndex === selectedIndex;
                    const Icon = item.icon;

                    return (
                      <li
                        key={item.id}
                        id={`command-${item.id}`}
                        role="option"
                        aria-selected={isSelected}
                        data-selected={isSelected}
                        className={`flex cursor-pointer items-center gap-3 px-4 py-2.5 text-sm ${
                          isSelected
                            ? 'bg-indigo-600 text-white'
                            : 'text-gray-700 dark:text-gray-300'
                        }`}
                        onClick={() => {
                          item.action();
                          setOpen(false);
                        }}
                        onMouseEnter={() => setSelectedIndex(flatIndex)}
                      >
                        {Icon && (
                          <Icon
                            className={`h-5 w-5 flex-shrink-0 ${
                              isSelected ? 'text-white' : 'text-gray-400'
                            }`}
                            aria-hidden="true"
                          />
                        )}
                        <div className="flex-1 min-w-0">
                          <p className="font-medium truncate">{item.name}</p>
                          {item.description && (
                            <p className={`text-xs truncate ${isSelected ? 'text-indigo-200' : 'text-gray-500'}`}>
                              {item.description}
                            </p>
                          )}
                        </div>
                        {item.shortcut && (
                          <kbd className={`text-xs ${isSelected ? 'text-indigo-200' : 'text-gray-400'}`}>
                            {item.shortcut}
                          </kbd>
                        )}
                      </li>
                    );
                  })}
                </ul>
              </li>
            ))
          )}
        </ul>

        {/* Footer */}
        <div className="flex items-center justify-between border-t border-gray-200 px-4 py-2.5 text-xs text-gray-500 dark:border-gray-800">
          <div className="flex items-center gap-3">
            <span className="flex items-center gap-1"><kbd className="rounded border px-1">↑↓</kbd> Navigate</span>
            <span className="flex items-center gap-1"><kbd className="rounded border px-1">↵</kbd> Select</span>
            <span className="flex items-center gap-1"><kbd className="rounded border px-1">Esc</kbd> Close</span>
          </div>
        </div>
      </div>
    </div>
  );
}
```

### Step 6: BREADCRUMBS

Hierarchical path navigation showing current location.

```tsx
interface BreadcrumbItem {
  name: string;
  href?: string;
}

export function Breadcrumbs({ items }: { items: BreadcrumbItem[] }) {
  return (
    <nav aria-label="Breadcrumb" className="mb-4">
      <ol className="flex items-center gap-1.5 text-sm" role="list">
        <li>
          <Link
            href="/"
            className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
            aria-label="Home"
          >
            <HomeIcon className="h-4 w-4" />
          </Link>
        </li>

        {items.map((item, index) => {
          const isLast = index === items.length - 1;
          return (
            <li key={item.name} className="flex items-center gap-1.5">
              <ChevronRightIcon className="h-4 w-4 text-gray-400 flex-shrink-0" aria-hidden="true" />
              {isLast || !item.href ? (
                <span
                  className="font-medium text-gray-900 dark:text-white"
                  aria-current="page"
                >
                  {item.name}
                </span>
              ) : (
                <Link
                  href={item.href}
                  className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200"
                >
                  {item.name}
                </Link>
              )}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}
```

Breadcrumb rules:
- Use `<nav aria-label="Breadcrumb">` wrapper
- Use `<ol>` for ordered list semantics
- Last item: `aria-current="page"`, no link, bold text
- Separator: chevron icon with `aria-hidden="true"` (not text "/" which is read by screen readers)
- Truncate on mobile: show first + last + ellipsis for long paths

### Step 7: RESPONSIVE TRANSFORMATION

Define how navigation transforms across breakpoints.

**Common responsive patterns**:

| Desktop Pattern | Mobile Transformation | Breakpoint |
|----------------|----------------------|------------|
| Top bar with links | Hamburger slide-out | md (768px) |
| Sidebar (256px) | Hidden + hamburger overlay | lg (1024px) |
| Sidebar (256px) | Bottom tabs (5 key items) | lg (1024px) |
| Mega menu | Accordion within hamburger | md (768px) |
| Breadcrumbs (full) | Truncated (home + current) | sm (640px) |
| Tab bar (horizontal) | Horizontal scroll or dropdown | md (768px) |

**Auto-hide on scroll** (for top bars on mobile):
```tsx
'use client';

import { useState, useEffect } from 'react';

function useScrollDirection() {
  const [scrollDirection, setScrollDirection] = useState<'up' | 'down'>('up');
  const [lastScrollY, setLastScrollY] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      const currentScrollY = window.scrollY;
      const direction = currentScrollY > lastScrollY ? 'down' : 'up';

      // Only update if scrolled more than 10px (debounce jitter)
      if (Math.abs(currentScrollY - lastScrollY) > 10) {
        setScrollDirection(direction);
      }
      setLastScrollY(currentScrollY);
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, [lastScrollY]);

  return scrollDirection;
}

// Usage in header:
const scrollDirection = useScrollDirection();

<header className={`sticky top-0 z-50 transition-transform duration-300 ${
  scrollDirection === 'down' ? '-translate-y-full' : 'translate-y-0'
}`}>
```

### Step 8: DARK MODE SUPPORT

Every navigation component must support light and dark modes.

**Dark mode strategy**:
- Use Tailwind `dark:` prefix for all color classes
- Background: `bg-white dark:bg-gray-950`
- Text: `text-gray-900 dark:text-white` (primary), `text-gray-600 dark:text-gray-400` (secondary)
- Borders: `border-gray-200 dark:border-gray-800`
- Hover: `hover:bg-gray-100 dark:hover:bg-gray-800`
- Active: `bg-indigo-50 dark:bg-indigo-500/10` and `text-indigo-700 dark:text-indigo-400`
- Backdrop: `bg-white/95 dark:bg-gray-950/95` with `backdrop-blur`

**Toggle component** (if needed):
```tsx
<button
  onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
  className="rounded-md p-2 text-gray-500 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-800"
  aria-label={`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`}
>
  {theme === 'dark' ? <SunIcon className="h-5 w-5" /> : <MoonIcon className="h-5 w-5" />}
</button>
```

### Step 9: ARIA AND KEYBOARD REQUIREMENTS

Non-negotiable accessibility requirements for all navigation components:

**ARIA landmarks**:
- `<nav aria-label="Main navigation">` — primary navigation
- `<nav aria-label="Breadcrumb">` — breadcrumbs
- `<nav aria-label="Sidebar">` or `<nav aria-label="Sidebar navigation">` — sidebar
- `<nav aria-label="Bottom navigation">` — bottom tabs
- Each `<nav>` must have a unique `aria-label` if multiple navs exist on the page

**Active state**:
- `aria-current="page"` on the link matching the current URL
- Visual active indicator (background color, border, font weight) in addition to color change

**Mobile menu**:
- `role="dialog"` and `aria-modal="true"` on the overlay
- Focus trap: Tab/Shift+Tab cycles within the menu
- Escape closes the menu
- Focus returns to the hamburger button on close
- `aria-expanded` on the trigger button
- Body scroll locked when open

**Keyboard navigation**:
- All nav links reachable via Tab
- Enter/Space activates links
- Escape closes dropdowns, menus, command palette
- Arrow keys navigate within command palette results
- Skip link: first focusable element on the page, targets `#main-content`

**Touch targets**:
- All nav links: minimum 44x44px touch area
- Bottom tabs: full width of tab, minimum 48px height
- Hamburger button: at least 44x44px

## Output Format

```
## Navigation: [Pattern Name]

### Configuration
- **Pattern**: [top bar / sidebar / bottom tabs / command palette / combined]
- **Positioning**: [fixed / sticky / auto-hide / static]
- **Items**: [list of navigation items]
- **Dark mode**: Included

### Component Code

[Complete React + Tailwind code — single file per component]

### Responsive Behavior

| Breakpoint | Navigation Display |
|-----------|-------------------|
| Mobile (<768px) | [what shows] |
| Tablet (768-1023px) | [what shows] |
| Desktop (1024px+) | [what shows] |

### Keyboard Shortcuts
| Key | Action |
|-----|--------|
| Tab | Move between nav items |
| Enter/Space | Activate link |
| Escape | Close menu/palette |
| Cmd+K | Open command palette |
| Arrow keys | Navigate palette results |

### ARIA Checklist
- [ ] nav element with unique aria-label
- [ ] aria-current="page" on active link
- [ ] Skip link before all navigation
- [ ] Focus trap in mobile menu / command palette
- [ ] aria-expanded on hamburger trigger
- [ ] role="dialog" + aria-modal on overlays
```

## Quality Gates

The output MUST include:
- [ ] Complete React component with Tailwind — copy-paste ready
- [ ] Active state with aria-current="page"
- [ ] Mobile responsive transformation (hamburger, bottom tabs, or equivalent)
- [ ] Keyboard navigation (Tab, Enter, Escape)
- [ ] ARIA landmarks (nav with aria-label)
- [ ] Skip link implementation
- [ ] Dark mode support (dark: classes throughout)
- [ ] Sticky/fixed positioning with backdrop blur

The output MUST NOT include:
- Navigation with no active state indication
- Mobile menus without focus trap
- Missing aria-label on nav elements
- Links without sufficient touch target size (< 44px)
- Dropdown menus that cannot be closed with Escape
- Nav that only works with mouse (no keyboard support)

## Cross-References

When generating navigation, draw knowledge from:
- `navigation-pattern-encyclopedia` skill — every nav pattern with IA guidance
- `component-patterns-code` skill — React component patterns with code
- `accessibility-inclusive-design` skill — ARIA navigation requirements, focus management
- `interaction-motion-design` skill — nav transitions, slide-out animations
- `mobile-ux-design` skill — bottom tab conventions, safe areas, thumb zones
- `platform-visual-standards` skill — iOS tab bar, Material bottom nav, web conventions
- `cognitive-psychology-ux` skill — information scent, menu depth, Hick's Law (fewer choices = faster decisions)

## Next Step

**Next** -> `/layout` — Build the page layout shell that this navigation plugs into

**Alternatives**:
- `/form` — Build forms for pages within this navigation
- `/animate` — Add entrance/transition animations to navigation elements
- `/screen` — Generate full screens with this navigation integrated
- `/guide` — See the full journey map
