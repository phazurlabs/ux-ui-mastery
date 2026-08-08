# Mobile Navigation Patterns — Complete Reference

> 22 mobile-specific navigation patterns with thumb zone analysis, iOS vs. Android conventions, exact specs, accessibility requirements, and production code.

---

## Mobile Navigation Fundamentals

### Thumb Zone Analysis

Steven Hoober's research on mobile device usage (2013, updated 2017) and subsequent studies show that how users hold their phone determines which screen areas are easy, stretchy, or hard to reach:

```
One-Handed Grip (49% of mobile usage):

+---------------------------+
|  HARD    |  HARD   | HARD |  Top zone: requires stretch
|          |         |      |  or hand repositioning
+----------+---------+------+
|  OK      |  EASY   |  OK  |  Middle zone: comfortable
|          |         |      |  for most interactions
+----------+---------+------+
|  EASY    |  EASY   | EASY |  Bottom zone: natural
|          |         |      |  thumb resting area
+---------------------------+

Thumb reach from bottom-right (right-handed):
- Bottom-right corner: easiest
- Bottom-center: easy
- Bottom-left: comfortable
- Middle-center: comfortable
- Top-right: stretch
- Top-left: hardest
```

### Key Mobile Navigation Principles
1. **Primary nav in the thumb zone**: Bottom tab bars, bottom sheets, FABs — all in easy reach
2. **Minimum 44x44pt touch targets** (iOS HIG) / **48x48dp** (Material Design)
3. **8px minimum spacing** between touch targets to prevent mis-taps
4. **No hover states**: Every hover interaction must have a tap equivalent
5. **System gestures are sacred**: Never override swipe-back (iOS) or system-back (Android)
6. **Provide visual feedback within 100ms** of touch to confirm the tap registered
7. **Limit navigation depth to 2-3 levels** — every level deeper increases drop-off by 10-20%

### iOS vs. Android Navigation Philosophy

| Dimension | iOS (Apple HIG) | Android (Material Design) |
|-----------|-----------------|---------------------------|
| **Primary nav** | Tab bar (bottom) | Bottom navigation bar or nav drawer |
| **Back navigation** | Left edge swipe gesture + nav bar back button | System back button/gesture |
| **Secondary nav** | Segmented control, action sheets | Tabs (top), bottom sheets |
| **Menu pattern** | Action sheet (bottom), no hamburger recommended | Navigation drawer (hamburger), bottom sheet |
| **Transitions** | Push/pop (horizontal slide) | Shared axis, container transform |
| **Tab bar items** | 2-5, always labeled with icon + text | 3-5, icon + text (labels always visible in M3) |
| **Tab bar position** | Bottom, always visible | Bottom (M3 preference) or top |
| **Modal presentation** | Sheet (slides up, swipe down to dismiss) | Bottom sheet or dialog |

---

## Pattern Index

| # | Pattern | Platform | Thumb Zone |
|---|---------|----------|-----------|
| 1 | Bottom Tab Bar (iOS) | iOS | Easy |
| 2 | Bottom Navigation Bar (Android/M3) | Android | Easy |
| 3 | Hamburger Menu (Slide-In Drawer) | Cross-platform | Hard (trigger) |
| 4 | Hamburger Menu (Full Overlay) | Cross-platform | Hard (trigger) |
| 5 | Bottom Sheet Navigation | Cross-platform | Easy |
| 6 | Tab Bar with More Menu | iOS / Cross-platform | Easy |
| 7 | Top Tab Bar (Scrollable) | Android / Cross-platform | Stretch |
| 8 | Swipe Navigation (Horizontal Paging) | Cross-platform | Easy |
| 9 | Search-First Mobile Navigation | Cross-platform | Middle |
| 10 | Floating Action Button (FAB) | Material Design | Easy |
| 11 | FAB + Speed Dial | Material Design | Easy |
| 12 | Pull-Down Navigation | iOS | Stretch |
| 13 | Stories/Carousel Navigation | Cross-platform | Easy-Middle |
| 14 | Nested Drill-Down (Push Stack) | iOS / Cross-platform | Easy (back) |
| 15 | Bottom App Bar | Material Design | Easy |
| 16 | Action Sheet Navigation | iOS | Easy |
| 17 | Contextual Bottom Bar | Cross-platform | Easy |
| 18 | Gesture-Based Navigation | Cross-platform | Easy |
| 19 | Radial/Pie Menu | Gaming / Specialized | Easy |
| 20 | Onboarding Navigation | Cross-platform | Easy |
| 21 | Mobile Breadcrumbs (Compact) | Cross-platform | Stretch |
| 22 | Split View Navigation (Tablet) | iPad / Android Tablet | Easy |

---

## 1. Bottom Tab Bar (iOS Style)

The standard iOS navigation pattern. A persistent bar at the bottom of the screen with 2-5 tab items, each consisting of an icon and a text label. Tapping a tab switches the entire view to that section.

### When to Use
- iOS apps with 2-5 top-level sections
- Apps where users switch between sections frequently
- When all sections are equally important
- Consumer-facing apps (social, commerce, content, productivity)

### When NOT to Use
- More than 5 sections (use "More" tab for overflow)
- Single-purpose utility apps (calculator, timer)
- Content-consumption apps where immersion matters (reading, video)
- When sections are hierarchically unequal (one section is clearly primary)

### iOS Human Interface Guidelines Specs
| Property | Value |
|----------|-------|
| Height | 49pt (compact), 83pt (regular, with home indicator) |
| Icon size | 25x25pt (regular), 18x18pt (compact) |
| Label font | SF Pro Text, 10pt, medium weight |
| Items | 2-5 maximum |
| Active state | Filled icon + tinted label (system blue or app tint color) |
| Inactive state | Outlined icon + gray label (#8E8E93) |
| Badge | Red circle with white number, top-right of icon |
| Background | System material (blur), adapts to light/dark mode |
| Separator | 0.5pt hairline at top edge |
| Safe area | Tab bar sits above the home indicator safe area |

### SwiftUI Implementation
```swift
struct ContentView: View {
    @State private var selectedTab = 0

    var body: some View {
        TabView(selection: $selectedTab) {
            HomeView()
                .tabItem {
                    Label("Home", systemImage: "house")
                }
                .tag(0)
                .badge(3)

            SearchView()
                .tabItem {
                    Label("Search", systemImage: "magnifyingglass")
                }
                .tag(1)

            FavoritesView()
                .tabItem {
                    Label("Favorites", systemImage: "heart")
                }
                .tag(2)

            ProfileView()
                .tabItem {
                    Label("Profile", systemImage: "person")
                }
                .tag(3)
        }
    }
}
```

### React Native Implementation
```tsx
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();

function App() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          const icons: Record<string, string> = {
            Home: focused ? 'home' : 'home-outline',
            Search: 'search',
            Favorites: focused ? 'heart' : 'heart-outline',
            Profile: focused ? 'person' : 'person-outline',
          };
          return <Icon name={icons[route.name]} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#007AFF',
        tabBarInactiveTintColor: '#8E8E93',
        tabBarStyle: {
          height: 83,
          paddingBottom: 34, // safe area
          paddingTop: 8,
        },
        tabBarLabelStyle: {
          fontSize: 10,
          fontWeight: '500',
        },
      })}
    >
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Search" component={SearchScreen} />
      <Tab.Screen name="Favorites" component={FavoritesScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
}
```

### Reference Implementations
- Instagram — 5-tab bottom bar (Home, Search, Reels, Shop, Profile)
- Apple Music — 4-tab bar (Listen Now, Browse, Radio, Library, Search)
- Safari iOS — 5-tab bottom bar (Back, Forward, Share, Bookmarks, Tabs)

---

## 2. Bottom Navigation Bar (Android / Material 3)

Material Design's bottom navigation component. Similar concept to iOS tab bar but with Material-specific styling: rounded indicator pill behind the active icon, optional label visibility control, and M3 Expressive theming.

### When to Use
- Android apps with 3-5 top-level destinations
- Cross-platform apps using Material Design
- When destinations are equally important and frequently accessed

### Material 3 Specs
| Property | Value |
|----------|-------|
| Height | 80dp |
| Icon size | 24dp |
| Active indicator | Pill shape, 64x32dp, surface-container-highest color |
| Label font | Label Medium (12sp), always visible in M3 |
| Items | 3-5 |
| Active icon | Filled variant |
| Inactive icon | Outlined variant, on-surface-variant color |
| Active label | On-surface color |
| Inactive label | On-surface-variant color |
| Badge | Small dot (6dp) or number badge (16dp height) |
| Elevation | Surface tint, level 2 |
| Ripple | State layer on touch |

### Jetpack Compose Implementation
```kotlin
@Composable
fun BottomNav(
    selectedIndex: Int,
    onSelect: (Int) -> Unit
) {
    val items = listOf(
        NavItem("Home", Icons.Filled.Home, Icons.Outlined.Home),
        NavItem("Search", Icons.Filled.Search, Icons.Outlined.Search),
        NavItem("Favorites", Icons.Filled.Favorite, Icons.Outlined.FavoriteBorder),
        NavItem("Profile", Icons.Filled.Person, Icons.Outlined.Person),
    )

    NavigationBar {
        items.forEachIndexed { index, item ->
            NavigationBarItem(
                icon = {
                    Icon(
                        imageVector = if (index == selectedIndex) item.filledIcon else item.outlinedIcon,
                        contentDescription = item.label
                    )
                },
                label = { Text(item.label) },
                selected = index == selectedIndex,
                onClick = { onSelect(index) }
            )
        }
    }
}
```

---

## 3. Hamburger Menu (Slide-In Drawer)

A three-line icon ("hamburger") that, when tapped, slides in a navigation panel from the left (or right in RTL) edge. The drawer overlays or pushes the main content.

### When to Use
- Apps with 6+ navigation destinations that cannot fit in a bottom bar
- When navigation items are not all equally important
- Secondary navigation destinations (settings, help, account)
- When screen real estate is needed for content

### When NOT to Use
- When discoverability matters (NNG found hiding navigation cuts content discoverability by nearly half)
- For primary, frequently-accessed navigation (use bottom tab bar instead)
- iOS apps (Apple discourages hamburger menus)
- Apps where users are new and need to discover features

### Discoverability Problem
NNG research consistently shows that hidden navigation (hamburger) reduces discoverability:
- Visible navigation leads to 20-50% more navigation usage
- Users are less likely to explore features hidden behind a hamburger
- Time to first interaction with hidden features is 2-3x longer

### Specs
| Property | Value |
|----------|-------|
| Trigger | 24dp hamburger icon, top-left (or top-right in RTL) |
| Drawer width | 256-320dp, or 85% of screen width (max 360dp) |
| Overlay | Semi-transparent scrim (32% black) behind drawer |
| Animation | Slide in from left, 250ms, standard easing |
| Close | Tap scrim, swipe drawer left, tap X, or system back |
| Content | User avatar/name (top), nav items, dividers, footer (settings, help) |
| Item height | 48dp minimum |
| Item padding | 16dp horizontal |
| Active item | Background tint, filled icon, primary color text |

### CSS Specs (Mobile Web)
```css
.drawer-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.32);
  z-index: 9998;
  opacity: 0;
  visibility: hidden;
  transition: opacity 250ms ease, visibility 250ms;
}

.drawer-backdrop--open {
  opacity: 1;
  visibility: visible;
}

.drawer {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 280px;
  max-width: 85vw;
  background: #ffffff;
  z-index: 9999;
  transform: translateX(-100%);
  transition: transform 250ms cubic-bezier(0.4, 0, 0.2, 1);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.drawer--open {
  transform: translateX(0);
}

.drawer__header {
  padding: 24px 16px;
  border-bottom: 1px solid #e5e7eb;
}

.drawer__item {
  display: flex;
  align-items: center;
  gap: 16px;
  height: 48px;
  padding: 0 16px;
  font-size: 14px;
  font-weight: 500;
  color: #374151;
  text-decoration: none;
}

.drawer__item:active {
  background: #f3f4f6;
}

.drawer__item[aria-current="page"] {
  background: #eff6ff;
  color: #2563eb;
}

.drawer__divider {
  height: 1px;
  background: #e5e7eb;
  margin: 8px 0;
}
```

### Accessibility
- Drawer must trap focus when open
- First focus on the close button or first nav item
- Escape key closes drawer
- `aria-hidden="true"` on main content when drawer is open
- Screen reader: announce "Navigation menu, open" when opened
- Return focus to hamburger trigger when closed

### Reference Implementations
- Gmail (Android) — Navigation drawer with account switcher
- Google Maps — Drawer for layers, settings, timeline

---

## 4. Hamburger Menu (Full Overlay)

Instead of a side-sliding drawer, the menu takes over the full screen as an overlay. Navigation items are displayed large and centered.

### When to Use
- Mobile websites (especially creative, fashion, minimal sites)
- When navigation items are few (4-8) and benefit from large display
- When the menu design is part of the brand experience

### When NOT to Use
- Apps with frequent navigation switching (too much visual disruption)
- When users need to reference content while navigating

### Specs
| Property | Value |
|----------|-------|
| Trigger | Hamburger icon or custom trigger |
| Overlay | Full viewport |
| Background | Solid color, brand color, or dark overlay |
| Font size | 24-40px for nav items (the menu IS the content) |
| Close | X icon (top-right), tap outside items, or system back |
| Animation | Fade + scale or staggered item reveal, 300-500ms |

---

## 5. Bottom Sheet Navigation

A sheet that slides up from the bottom of the screen to present navigation options, actions, or additional content. Can be a peek sheet (partial height), half sheet, or full sheet.

### When to Use
- Presenting 3-10 navigation actions in context
- Secondary navigation that does not warrant a full page
- "More options" overflow menus
- Quick selection (sort options, filter options)
- Modal-like content that should feel connected to the current context

### When NOT to Use
- Primary navigation (too ephemeral)
- Content that needs to persist while user interacts with main content
- When there are only 2-3 options (use action sheet or segmented control)

### Specs
| Property | Value |
|----------|-------|
| Peek height | 25-40% of screen |
| Half height | 50% of screen |
| Full height | 90-95% of screen (with grabber visible) |
| Grabber/handle | 36x4dp rounded bar, centered, top of sheet |
| Corner radius | 16-24dp (top corners only) |
| Backdrop | Semi-transparent scrim |
| Dismiss | Swipe down, tap scrim, or close button |
| Animation | Spring physics (iOS) or standard easing, 300ms |
| Content | List items, grid of actions, or scrollable content |

### CSS Specs (Mobile Web)
```css
.bottom-sheet-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.32);
  z-index: 9998;
}

.bottom-sheet {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  background: #ffffff;
  border-radius: 16px 16px 0 0;
  z-index: 9999;
  max-height: 90vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transform: translateY(100%);
  transition: transform 300ms cubic-bezier(0.32, 0.72, 0, 1);
}

.bottom-sheet--open {
  transform: translateY(0);
}

.bottom-sheet__handle {
  width: 36px;
  height: 4px;
  background: #d1d5db;
  border-radius: 2px;
  margin: 12px auto;
  flex-shrink: 0;
}

.bottom-sheet__content {
  overflow-y: auto;
  padding: 0 16px 24px;
  -webkit-overflow-scrolling: touch;
}

.bottom-sheet__item {
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: 52px;
  padding: 12px 0;
  font-size: 16px;
  color: #111827;
  border-bottom: 1px solid #f3f4f6;
  cursor: pointer;
}

.bottom-sheet__item:active {
  background: #f3f4f6;
}
```

### Reference Implementations
- Apple Maps — Bottom sheet for place details, directions
- Google Maps — Location details bottom sheet
- Uber — Ride options bottom sheet

---

## 6. Tab Bar with More Menu

A bottom tab bar with 4-5 visible tabs, where the last tab is a "More" item that opens a list of additional navigation destinations. iOS standard pattern for apps with 6+ sections.

### When to Use
- iOS apps with 6-10 sections where 4 are primary and the rest are secondary
- When you cannot reduce top-level sections to 5 or fewer
- When all secondary sections still need bottom-nav-level access

### When NOT to Use
- When all sections are equally important (reorganize IA instead)
- Android apps (use navigation drawer for overflow)
- When there are more than 10 sections (the "More" list becomes unwieldy)

### Specs
| Property | Value |
|----------|-------|
| Visible tabs | 4 primary + "More" (5th tab) |
| More icon | Ellipsis icon (...) or "More" text with grid/list icon |
| More screen | Table view list of remaining sections |
| Customization | iOS allows users to reorder tabs (Edit in More screen) |
| Active state on More | "More" tab highlighted when user is in any overflow section |

### SwiftUI Implementation
```swift
// iOS automatically handles More tab when > 5 items
struct ContentView: View {
    var body: some View {
        TabView {
            HomeView().tabItem { Label("Home", systemImage: "house") }
            SearchView().tabItem { Label("Search", systemImage: "magnifyingglass") }
            FavoritesView().tabItem { Label("Favorites", systemImage: "heart") }
            CartView().tabItem { Label("Cart", systemImage: "cart") }
            // These appear in "More" tab automatically:
            OrdersView().tabItem { Label("Orders", systemImage: "bag") }
            SettingsView().tabItem { Label("Settings", systemImage: "gear") }
            HelpView().tabItem { Label("Help", systemImage: "questionmark.circle") }
        }
    }
}
```

---

## 7. Top Tab Bar (Scrollable)

A horizontal tab bar at the top of the screen (below the app bar) that can scroll horizontally when there are more tabs than fit on screen. The standard Android/Material Design pattern for section navigation within a screen.

### When to Use
- Android apps with 3-8+ sections within a screen
- Content organized by category (news categories, product types)
- When tab labels vary in length
- ViewPager-style swipe navigation with tab indicators

### When NOT to Use
- iOS apps (bottom tabs are preferred)
- When tabs navigate to entirely different features (use bottom nav)
- When there are only 2 tabs (use segmented control)

### Material 3 Specs
| Property | Value |
|----------|-------|
| Height | 48dp |
| Active indicator | Primary color underline (3dp) or pill (M3) |
| Font | Title Small (14sp), medium weight |
| Scroll | Horizontal scroll with edge fade indicators |
| Swipe integration | Swipe left/right to switch tabs (ViewPager) |
| Fixed vs. scrollable | Fixed: all tabs equal width. Scrollable: auto width per tab |

---

## 8. Swipe Navigation (Horizontal Paging)

Navigate between peer-level content by swiping left or right. Often paired with a top tab bar or page indicator dots.

### When to Use
- Onboarding screens
- Image galleries and photo carousels
- News category browsing (swipe between categories)
- Tinder-style card interfaces
- Tab content that naturally flows left-to-right

### When NOT to Use
- When content does not have a natural horizontal sequence
- When swipe conflicts with horizontal scroll content (maps, wide tables)
- When users need to see content from multiple pages at once
- When there are more than 7-8 pages (disorienting)

### Specs
| Property | Value |
|----------|-------|
| Gesture | Horizontal swipe with velocity and distance thresholds |
| Snap | Snap to nearest page center (pagination snapping) |
| Indicator | Dots (for 2-7 pages) or tab bar |
| Dot size | 8dp active, 6dp inactive |
| Transition | Follow finger position (interactive), snap with spring |
| Peek | Optionally show 10-20px of adjacent page to hint swipeability |
| Velocity threshold | 500+ dp/s for a quick swipe to advance |
| Distance threshold | 50%+ of page width for a slow drag to advance |

### CSS Specs (Scroll Snap)
```css
.swipe-container {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}

.swipe-container::-webkit-scrollbar {
  display: none;
}

.swipe-page {
  flex: 0 0 100%;
  scroll-snap-align: start;
  min-height: 100vh;
}

.page-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 16px 0;
}

.page-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #d1d5db;
  transition: all 200ms ease;
}

.page-dot--active {
  width: 8px;
  height: 8px;
  background: #2563eb;
}
```

---

## 9. Search-First Mobile Navigation

A navigation pattern where the search bar is the most prominent element on the screen, positioned in or near the thumb zone, with browse-based navigation secondary.

### When to Use
- E-commerce mobile apps (Amazon, eBay)
- Food delivery (search for restaurants or dishes)
- Music/media (search for songs, artists)
- When > 50% of mobile users start with search

### When NOT to Use
- Apps with small content catalogs
- Social apps where the feed IS the content
- When users do not know what to search for

### Specs
| Property | Value |
|----------|-------|
| Search bar position | Top of screen (just below status bar) or in app bar |
| Search bar height | 44-52px |
| Tap behavior | Tap opens full-screen search with keyboard |
| Auto-suggest | Show after 1 character, optimized for mobile bandwidth |
| Recent searches | Show on focus before typing |
| Voice search | Microphone icon for voice input |

---

## 10. Floating Action Button (FAB)

A circular button floating above the content, typically in the bottom-right corner, representing the single most important action on the screen.

### When to Use
- Compose/create actions (new message, new post, new file)
- When there is one clearly primary action per screen
- Material Design applications
- When the action should be accessible regardless of scroll position

### When NOT to Use
- iOS apps (not a native iOS pattern)
- When there is no single primary action
- On screens that already have a prominent CTA
- When the FAB would obscure important content

### Material 3 Specs
| Property | Value |
|----------|-------|
| Size | 56dp (standard), 96dp (large), 40dp (small) |
| Corner radius | 16dp (standard), 28dp (large), 12dp (small) |
| Elevation | Level 3 (6dp shadow) |
| Position | 16dp from bottom edge and right edge |
| Color | Primary container with on-primary-container icon |
| Icon size | 24dp |
| Hide on scroll | Optional: hide when scrolling down, show when scrolling up |
| Extended FAB | Icon + text label, auto-width, collapses to icon on scroll |

### Compose Implementation
```kotlin
@Composable
fun MyScreen() {
    Scaffold(
        floatingActionButton = {
            FloatingActionButton(
                onClick = { /* create action */ },
                containerColor = MaterialTheme.colorScheme.primaryContainer,
                contentColor = MaterialTheme.colorScheme.onPrimaryContainer,
            ) {
                Icon(Icons.Default.Add, contentDescription = "Create new")
            }
        }
    ) { padding ->
        // Screen content
    }
}
```

---

## 11. FAB + Speed Dial

A FAB that, when pressed, fans out 3-6 smaller action buttons vertically. Each mini FAB has a text label. Used when there are multiple related creation actions.

### When to Use
- When there are 3-6 related creation actions
- Photo/camera apps (take photo, record video, upload from library)
- Note apps (new note, new checklist, new voice memo)

### When NOT to Use
- When there is only one action (use simple FAB)
- When there are more than 6 actions (use bottom sheet)
- When actions are not related to each other

### Specs
| Property | Value |
|----------|-------|
| Main FAB | 56dp, rotates icon (+ to X) on open |
| Mini FABs | 40dp each, 16dp gap between |
| Labels | Required — 13sp, left of mini FAB, surface container background |
| Scrim | Semi-transparent backdrop behind speed dial |
| Animation | Staggered entrance from bottom, 50ms delay each, 200ms duration |
| Close | Tap scrim, tap main FAB, or system back |

---

## 12. Pull-Down Navigation

A pattern where pulling down from the top of a scrolled-to-top list reveals a hidden navigation area, search bar, or filter options. Extends the pull-to-refresh pattern.

### When to Use
- Hiding search or filters that are not always needed
- Progressive disclosure of navigation options
- When top screen area is valuable and filters are secondary

### When NOT to Use
- When the hidden navigation is essential (visibility matters)
- When the pattern conflicts with pull-to-refresh
- When users will not discover the hidden area

### Specs
| Property | Value |
|----------|-------|
| Trigger | Pull down when already at top of scroll view |
| Reveal height | 48-120px depending on content |
| Threshold | 60+ px pull to commit |
| Content | Search bar, filter chips, sort options |
| Animation | Rubber-band physics, match system pull-to-refresh feel |

---

## 13. Stories/Carousel Navigation

A horizontal row of circular or rounded-rect thumbnails that represent sequential, ephemeral, or categorized content. Tapping opens a full-screen immersive experience.

### When to Use
- Social media stories (Instagram, Snapchat, LinkedIn)
- Featured content highlights
- Category browsing with visual previews
- User/creator spotlight navigation

### When NOT to Use
- Navigation to persistent, non-ephemeral content
- When there are fewer than 3 items
- When visual preview does not aid decision-making

### Specs
| Property | Value |
|----------|-------|
| Thumbnail size | 56-72dp circle or 80-100dp rounded rect |
| Row height | 80-120dp including label |
| Label | 11-12sp, below thumbnail, truncated at 1 line |
| Unread indicator | Colored ring around thumbnail (gradient for stories) |
| Scroll | Horizontal scroll, no snap |
| Position | Top of feed, below app bar |
| Peek | Show partial next item to hint scrollability |

---

## 14. Nested Drill-Down (Push Stack / UINavigationController)

A navigation pattern where tapping an item pushes a new screen onto a stack, sliding it in from the right. The back button or swipe-back gesture pops the screen, returning to the previous level. The iOS standard for hierarchical navigation.

### When to Use
- Settings screens (Settings > General > About > Legal)
- Category browsing (Categories > Electronics > Phones > iPhone)
- Any hierarchical content up to 3-4 levels deep
- Master-detail interfaces

### When NOT to Use
- Non-hierarchical navigation (peer switching)
- When the stack would go deeper than 4 levels
- When users need to see parent and child content simultaneously

### Specs
| Property | Value |
|----------|-------|
| Transition | Push: slide in from right (300ms). Pop: slide out to right (300ms) |
| Back button | Left-pointing chevron + previous screen title (iOS) |
| Swipe back | iOS: swipe from left edge. Android: system back |
| Title | Current screen title in navigation bar, center (iOS) or left (Android) |
| Large title | iOS: large title collapses to small on scroll |
| Stack depth | Recommend max 3-4 levels |

### SwiftUI Implementation
```swift
struct SettingsView: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("General") {
                    GeneralSettingsView()
                }
                NavigationLink("Notifications") {
                    NotificationSettingsView()
                }
                NavigationLink("Privacy") {
                    PrivacySettingsView()
                }
            }
            .navigationTitle("Settings")
        }
    }
}
```

### Reference Implementations
- iOS Settings app — Deep drill-down with back navigation
- Apple Mail — Mailboxes > Inbox > Message > Attachment

---

## 15. Bottom App Bar (Material Design)

A bar at the bottom of the screen that contains navigation icons and optionally a FAB. An alternative to bottom navigation when the screen needs both navigation and a primary action.

### When to Use
- Screens that need both navigation and a prominent action
- When the FAB and navigation share the bottom of the screen
- Material Design apps that want to combine navigation with actions

### Material 3 Specs
| Property | Value |
|----------|-------|
| Height | 80dp |
| Icons | 2-4 navigation/action icons on the left |
| FAB | Optional, notched or overlapping, right side |
| Background | Surface container color |
| Icon size | 24dp with 48dp touch target |

---

## 16. Action Sheet Navigation (iOS)

A modal sheet that slides up from the bottom presenting a list of actions or navigation options relevant to the current context. The standard iOS pattern for presenting choices.

### When to Use
- Presenting 2-8 contextual actions (share, copy, delete, save)
- Navigation choices within a flow
- Destructive action confirmation (with red "Delete" option)
- As an alternative to a hamburger menu on iOS

### iOS Specs
| Property | Value |
|----------|-------|
| Presentation | Slides up from bottom with spring animation |
| Actions | List of buttons, full width |
| Destructive action | Red text, at bottom of action list |
| Cancel button | Separate section at bottom, bold text |
| Dismiss | Tap Cancel, tap outside, or swipe down |
| Corner radius | 14pt (top corners) |
| Max visible actions | 6-8 before scrolling |

### SwiftUI Implementation
```swift
struct ContentView: View {
    @State private var showActionSheet = false

    var body: some View {
        Button("Options") { showActionSheet = true }
            .confirmationDialog("Choose an action", isPresented: $showActionSheet) {
                Button("Share") { /* share */ }
                Button("Duplicate") { /* duplicate */ }
                Button("Move to Folder") { /* move */ }
                Button("Delete", role: .destructive) { /* delete */ }
                Button("Cancel", role: .cancel) { }
            }
    }
}
```

---

## 17. Contextual Bottom Bar

A bar that appears at the bottom of the screen when the user enters a specific mode (editing, selecting, composing) and provides mode-specific actions. Replaces or overlays the regular bottom navigation.

### When to Use
- Text editing mode (bold, italic, link, image)
- Multi-select mode (select all, delete, move)
- Media editing (crop, filter, adjust)
- Any temporary mode with specific tooling needs

### Specs
| Property | Value |
|----------|-------|
| Height | 48-56dp |
| Position | Bottom, above safe area |
| Background | Surface or primary color to distinguish from regular bottom nav |
| Actions | 3-6 icon buttons or icon + label |
| Transition | Slide up from bottom, 200ms |
| Dismiss | Complete action, tap "Done", or swipe down |

---

## 18. Gesture-Based Navigation

Navigation driven by touch gestures rather than explicit UI elements. Gestures include swipe, pinch, long-press, and multi-finger interactions.

### When to Use
- Immersive experiences (maps, photos, games)
- Content consumption (e-reader page turn, video seek)
- Quick actions on list items (swipe to archive, swipe to delete)
- Complementing visible navigation (gesture as shortcut)

### When NOT to Use
- As the only navigation method (not discoverable)
- When gestures conflict with system gestures
- For critical or destructive actions without confirmation
- When the target user base includes low dexterity users

### Common Mobile Gestures
| Gesture | Navigation Action | Example |
|---------|------------------|---------|
| Swipe right from left edge | Go back | iOS system back |
| Swipe left on list item | Quick action (delete, archive) | Mail, Reminders |
| Swipe down from top | Pull to refresh, notification center | System pattern |
| Long press | Context menu | iOS context menu |
| Pinch out | Zoom into detail view | Photos, Maps |
| Pinch in | Zoom out / go to overview | Photos, Maps |
| Double tap | Toggle zoom | Photos |
| Two-finger swipe | Page between views | Some iPad apps |

### Discoverability Requirements
- Always provide a visible alternative for every gesture
- Show a brief tutorial or hint on first use
- Consider haptic feedback to confirm gesture recognition
- Support undo for destructive gesture actions

---

## 19. Radial/Pie Menu

A circular menu that appears around the touch point, with options arranged radially. The user slides their finger to the desired option and releases. Extremely fast for experts but has a learning curve.

### When to Use
- Gaming interfaces
- Creative tools (drawing apps, 3D modeling)
- Quick tool switching in professional apps
- When speed matters more than discoverability

### When NOT to Use
- General consumer apps
- When there are more than 8 options
- When target labels are long or complex
- When accessibility is a primary concern

### Specs
| Property | Value |
|----------|-------|
| Trigger | Long press or dedicated button |
| Radius | 80-120dp from center |
| Sectors | 4-8 equal segments |
| Labels | Along the radial direction, 12-14sp |
| Icons | 24dp in each sector |
| Selection | Slide finger to sector and release |
| Cancel | Release in center dead zone (30dp radius) |

---

## 20. Onboarding Navigation

Navigation specific to first-time user onboarding flows: typically 3-5 screens with horizontal swipe or Next/Skip buttons.

### When to Use
- First app launch experience
- Feature introduction after updates
- Account setup wizard
- Permission request flow

### When NOT to Use
- Returning users (show once, then skip)
- When onboarding content can be integrated into the main UI
- When the app is self-explanatory

### Specs
| Property | Value |
|----------|-------|
| Screens | 3-5 (more causes drop-off) |
| Navigation | Swipe + dots + Next button |
| Skip | Always provide "Skip" (top-right) |
| Last screen | "Get Started" or "Done" instead of "Next" |
| Dots | Bottom-center, 8dp active, 6dp inactive |
| Auto-advance | Optional: 5-8 second timer per screen |
| Persistence | Show only once, store completion in user defaults |

---

## 21. Mobile Breadcrumbs (Compact)

A compact breadcrumb that shows only the immediate parent as a back link, since full breadcrumb paths do not fit mobile screens well.

### When to Use
- Mobile web e-commerce where users drill into categories
- When the browser back button is unreliable (web views)
- When the parent context is not obvious from the page content

### When NOT to Use
- Native iOS apps (use system navigation bar back button)
- When there is already a clear back navigation element

### Specs
| Property | Value |
|----------|-------|
| Display | "< Category Name" (chevron + parent name) |
| Position | Top of content, below app bar |
| Font size | 13-14px |
| Touch target | Full width of text + padding (min 44px height) |
| Truncation | Truncate parent name at 20-25 characters with ellipsis |

---

## 22. Split View Navigation (Tablet)

A two-pane layout where the left pane shows a navigation list (master) and the right pane shows the selected item's content (detail). Standard pattern for iPad and Android tablets.

### When to Use
- iPad apps in landscape orientation
- Android tablets and foldables
- Email clients (inbox list + message detail)
- Chat apps (conversation list + chat)
- Settings (category list + settings detail)

### When NOT to Use
- Phone-sized screens (use push navigation instead)
- When the list and detail are unrelated
- When the detail pane needs full screen width

### iPad Specs (iPadOS)
| Property | Value |
|----------|-------|
| Master pane width | 320-380pt (compact: 260pt) |
| Detail pane | Remaining width |
| Separator | 0.5pt hairline or subtle shadow |
| Collapse behavior | Portrait: master pane becomes overlay sidebar |
| Selection highlight | System accent color background on selected row |
| Transition | Crossfade detail content on selection change |

### SwiftUI Implementation
```swift
struct MailView: View {
    @State private var selectedMessage: Message?

    var body: some View {
        NavigationSplitView {
            List(messages, selection: $selectedMessage) { message in
                NavigationLink(value: message) {
                    MessageRow(message: message)
                }
            }
            .navigationTitle("Inbox")
        } detail: {
            if let message = selectedMessage {
                MessageDetail(message: message)
            } else {
                Text("Select a message")
                    .foregroundStyle(.secondary)
            }
        }
    }
}
```

### Reference Implementations
- Apple Mail (iPad) — Split view with collapsible sidebar
- Apple Notes (iPad) — Three-column split view (folders, notes, editor)
- Gmail (tablet) — Conversation list + email detail

---

## Mobile Navigation Decision Matrix

| Scenario | iOS Recommendation | Android Recommendation |
|----------|-------------------|----------------------|
| 2-5 equal sections | Bottom tab bar | Bottom navigation bar |
| 6-10 sections | Tab bar + More | Navigation drawer |
| Single primary action | Prominent button in nav bar | FAB |
| Multiple quick actions | Action sheet | FAB + speed dial / bottom sheet |
| Deep hierarchy | NavigationStack (push/pop) | Navigation component with back |
| Contextual actions | Long-press context menu | Long-press / bottom sheet |
| Settings navigation | Push stack (drill-down) | Push stack or tabs |
| Content categories | Segmented control or tabs | Top tabs (scrollable) |
| Mode-specific tools | Toolbar at bottom | Bottom app bar |
| Onboarding flow | Horizontal paging + dots | ViewPager + dots |
| Tablet layout | NavigationSplitView | Canonical layouts (M3) |

---

## Mobile Navigation Accessibility Checklist

- [ ] All touch targets are at least 44x44pt (iOS) / 48x48dp (Android)
- [ ] 8px minimum spacing between adjacent touch targets
- [ ] Bottom tab bar items have both icon and text label
- [ ] Active tab is announced by screen reader ("Selected, Home tab, 1 of 4")
- [ ] Hamburger menu traps focus when open
- [ ] Bottom sheets are announced when they appear
- [ ] System back gesture is not overridden
- [ ] All gestures have visible UI alternatives
- [ ] VoiceOver/TalkBack can access all navigation options
- [ ] Dynamic type / font scaling does not break navigation layout
- [ ] Reduced motion is respected for all navigation transitions
- [ ] One-handed operation is possible for all primary navigation
