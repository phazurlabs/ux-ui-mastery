# Screen Transitions and Platform Conventions

How screens move between each other, and what each platform expects.


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
