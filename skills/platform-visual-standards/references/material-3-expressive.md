# Material 3 Expressive Design Standards

## What Changed: M3 to M3 Expressive

Material 3 Expressive is the most significant Material Design update since the Material 2 to Material 3 transition. Announced in 2025, it fundamentally shifts Material Design from a neutral, systematic framework to an emotionally expressive design system that encourages personality and brand differentiation while maintaining usability.

### Core Philosophy

"Emotional expression through systematic design." M3 Expressive recognizes that purely functional design can feel sterile. The update gives designers tools to inject warmth, playfulness, and brand identity without sacrificing accessibility or consistency.

### Three Pillars of Expressiveness

1. **Shape**: 35-shape library replaces fixed corner radii — components can morph between shapes
2. **Motion**: Spring-physics animations replace duration-based transitions — interactions feel physical
3. **Color**: Enhanced HCT color system with more vibrant defaults and richer Dynamic Color

---

## 35-Shape Library

M3 Expressive replaces the simple corner radius system (small, medium, large, extra-large, full) with a library of 35 distinct shapes that can be applied to any component.

### Shape Categories

**Round (Circular Corners)**
- Classic rounded rectangles with varying radii
- Convey approachability and softness
- Default for most components

**Squircle (Continuous Corners)**
- Superellipse curves (like iOS)
- Smoother than circular corners
- Premium, polished feel

**Cut (Chamfered Corners)**
- Straight diagonal cuts at corners
- Convey precision, seriousness, technical
- Good for finance, enterprise, productivity

**Arch**
- Rounded top with flat bottom (or vice versa)
- Architectural, structured
- Good for headers, hero cards

**Pill**
- Full-round ends (stadium shape)
- Strong action signal
- Default for buttons and chips

**Clover**
- Four-lobed organic shape
- Playful, nature-inspired
- Good for wellness, children's apps

**Scallop**
- Wavy, shell-like edges
- Decorative, artisanal
- Good for food, craft, creative apps

**Hexagon**
- Six-sided geometric shape
- Technical, structured, modular
- Good for data visualization, tech, gaming

**Diamond**
- Four-pointed rotated square
- Premium, luxury, distinctive
- Good for fashion, jewelry, premium tiers

**Custom Morphing Shapes**
- Define start and end shapes for transitions
- Components morph between shapes based on state
- Example: FAB morphs from circle to rounded rectangle on scroll

### Shape Tokens

```kotlin
// Shape token scale
MaterialTheme.shapes.extraSmall    // 4dp radius
MaterialTheme.shapes.small         // 8dp radius
MaterialTheme.shapes.medium        // 12dp radius
MaterialTheme.shapes.large         // 16dp radius
MaterialTheme.shapes.extraLarge    // 28dp radius
MaterialTheme.shapes.full          // 50% (pill/circle)
```

### Morphing Shapes in Practice

```kotlin
// FAB that morphs on scroll
val fabShape by animateShapeAsState(
    targetShape = if (isScrolling)
        RoundedCornerShape(16.dp)  // Rounded rectangle
    else
        CircleShape  // Circle
)

FloatingActionButton(
    shape = fabShape,
    onClick = { /* ... */ }
) {
    Icon(Icons.Default.Add, contentDescription = "Add")
}
```

### How Shapes Convey Meaning

| Shape | Emotional Association | Recommended For |
|-------|----------------------|-----------------|
| Round | Friendly, approachable | Consumer apps, social |
| Squircle | Premium, polished | Design tools, premium tiers |
| Cut | Serious, precise | Finance, enterprise |
| Pill | Action, urgency | CTAs, buttons, tags |
| Clover | Playful, organic | Wellness, children |
| Hexagon | Technical, structured | Dev tools, data, gaming |
| Diamond | Luxury, exclusive | Fashion, premium |
| Arch | Architectural, stable | Real estate, institutional |
| Scallop | Artisanal, warm | Food, craft, creative |

---

## Spring-Physics Motion

M3 Expressive replaces all duration-based animations (200ms ease-in-out) with spring physics. Springs are physically modeled — they have mass, stiffness, and damping — which makes motion feel natural and interruptible.

### Why Springs

- **Interruptible**: A spring animation can be redirected mid-flight without jarring stops
- **Natural**: Physical objects don't move with cubic beziers — they accelerate and decelerate organically
- **Responsive**: Springs react to velocity — a fast fling creates a different animation than a slow drag
- **Consistent**: The same spring parameters produce the same feel regardless of distance

### Spring Parameters

- **Mass**: How heavy the element feels (default: 1.0). Higher mass = slower, more deliberate movement.
- **Stiffness**: How quickly the spring pulls toward the target (default: varies). Higher stiffness = faster snap.
- **Damping**: How quickly oscillation settles (default: varies). Lower damping = more bounce.
- **Damping ratio**: 0 = infinite oscillation, 1 = critically damped (no bounce), >1 = overdamped (sluggish)

### Spring Presets

**Bouncy**
- Stiffness: 200, Damping: 10
- Damping ratio: ~0.35
- Use: Playful interactions, like/favorite animations, success states
- Visible overshoot and 1-2 bounces before settling

**Smooth**
- Stiffness: 400, Damping: 20
- Damping ratio: ~0.5
- Use: Most UI transitions — sheets, page changes, reveals
- Minimal overshoot, settles quickly

**Stiff**
- Stiffness: 800, Damping: 30
- Damping ratio: ~0.53
- Use: Small, precise movements — toggles, checkboxes, focus indicators
- Almost no overshoot, snappy response

**Gentle**
- Stiffness: 100, Damping: 14
- Damping ratio: ~0.7
- Use: Large-area transitions — full-screen reveals, background shifts
- Slow, graceful movement

### Compose Implementation

```kotlin
// Spring animation for a float value
val offset by animateFloatAsState(
    targetValue = if (expanded) 200f else 0f,
    animationSpec = spring(
        dampingRatio = Spring.DampingRatioMediumBouncy,
        stiffness = Spring.StiffnessMedium
    )
)

// Spring constants provided by Material
Spring.DampingRatioNoBouncy        // 1.0
Spring.DampingRatioLowBouncy       // 0.75
Spring.DampingRatioMediumBouncy    // 0.5
Spring.DampingRatioHighBouncy      // 0.2

Spring.StiffnessHigh               // 10000
Spring.StiffnessMedium             // 1500
Spring.StiffnessMediumLow          // 400
Spring.StiffnessLow                // 200
Spring.StiffnessVeryLow            // 50
```

### Container Transforms

Shared element transitions use spring curves for seamless morphing between screens:

```kotlin
// Shared element transition (Compose)
SharedTransitionLayout {
    AnimatedContent(targetState = showDetail) { isDetail ->
        if (isDetail) {
            DetailScreen(
                modifier = Modifier.sharedElement(
                    rememberSharedContentState(key = "card-$id"),
                    animatedVisibilityScope = this
                )
            )
        } else {
            ListScreen(/* ... */)
        }
    }
}
```

---

## HCT Color Space (Hue, Chroma, Tone)

HCT is Google's perceptually accurate color space developed specifically for Material Design. It combines the best attributes of CAM16 (hue, chroma) and L* from CIELAB (tone/lightness).

### HCT Components

**Hue (0-360)**
- The color identity: red, orange, yellow, green, blue, purple
- 0/360 = red, 60 = yellow, 120 = green, 240 = blue
- Mapped from CAM16 for perceptual accuracy

**Chroma (0-~150)**
- Color vividness/saturation
- 0 = completely gray (achromatic)
- Higher values = more vivid
- Maximum chroma varies by hue (yellow can reach ~110, blue can reach ~130)
- Unlike HSL saturation, equal chroma changes look equally vivid across all hues

**Tone (0-100)**
- Lightness on a perceptually uniform scale
- 0 = pure black
- 50 = medium (perceptual midpoint)
- 100 = pure white
- A tone difference of 40+ between foreground and background guarantees WCAG AA contrast (4.5:1)
- A tone difference of 50+ guarantees WCAG AAA contrast (7:1)

### Why HCT Over HSL

HSL has severe perceptual non-uniformity: a yellow at 50% lightness looks much lighter than a blue at 50% lightness. HCT corrects this — Tone 50 looks equally light regardless of hue. This makes it possible to generate accessible color palettes algorithmically.

### Tonal Palettes

Each key color generates a 13-tone palette:

| Tone | Use |
|------|-----|
| 0 | Black |
| 10 | Darkest surface in dark mode |
| 20 | Dark mode container fills |
| 30 | Dark mode primary/secondary colors |
| 40 | Light mode primary/secondary colors |
| 50 | Medium contrast elements |
| 60 | Light mode decorative elements |
| 70 | Light secondary containers |
| 80 | Light mode container fills |
| 90 | Light mode surface containers |
| 95 | Lightest surface in light mode |
| 99 | Near-white surface |
| 100 | White |

---

## Dynamic Color (Material You)

### Algorithm

1. **Extract**: Identify dominant colors from the user's wallpaper using quantization (Wu's algorithm or similar)
2. **Map to HCT**: Convert extracted colors to HCT color space
3. **Generate 5 key colors**: Primary, Secondary, Tertiary, Neutral, Neutral Variant
4. **Create tonal palettes**: Generate 13-tone palette for each key color
5. **Assign color roles**: Map tonal palette values to 29 semantic color tokens
6. **Generate schemes**: Create both light and dark theme variants

### 5 Key Colors

| Key Color | Source | Purpose |
|-----------|--------|---------|
| Primary | Dominant wallpaper color | Brand, key actions, active states |
| Secondary | Complementary wallpaper color | Less prominent components |
| Tertiary | Analogous or triadic color | Accent, contrast, visual interest |
| Neutral | Desaturated primary (low chroma) | Surfaces, backgrounds |
| Neutral Variant | Slightly chromatic neutral | Outline, surface variant |

### 29 Color Roles

```
primary, onPrimary, primaryContainer, onPrimaryContainer,
secondary, onSecondary, secondaryContainer, onSecondaryContainer,
tertiary, onTertiary, tertiaryContainer, onTertiaryContainer,
error, onError, errorContainer, onErrorContainer,
background, onBackground,
surface, onSurface, surfaceVariant, onSurfaceVariant,
outline, outlineVariant,
inverseSurface, inverseOnSurface, inversePrimary,
shadow, scrim
```

### Custom Colors (Brand Extension)

```kotlin
// Extend dynamic color with a brand color
val customColor = CustomColor(
    name = "Brand Orange",
    color = Color(0xFFFF6B00),
    harmonize = true  // Blend with dynamic palette
)
```

When `harmonize = true`, the brand color is shifted slightly toward the dynamic palette's primary hue, creating harmony without losing brand identity.

### Compose Implementation

```kotlin
// Dynamic color scheme (Android 12+)
val colorScheme = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
    if (darkTheme) dynamicDarkColorScheme(context)
    else dynamicLightColorScheme(context)
} else {
    if (darkTheme) darkColorScheme() else lightColorScheme()
}

MaterialTheme(
    colorScheme = colorScheme,
    typography = Typography,
    shapes = Shapes
) {
    // App content
}
```

---

## M3 Component Gallery

### Buttons

| Type | Use | Visual |
|------|-----|--------|
| Filled | Primary CTA | Solid primary color, white text |
| Outlined | Secondary action | Border only, no fill |
| Tonal | Medium emphasis | Primary container color fill |
| Elevated | Needs separation from surface | Shadow + surface tint |
| Text | Lowest emphasis | No border, no fill |

All buttons support leading/trailing icons, loading states, and disabled states.

```kotlin
Button(onClick = { }) { Text("Filled") }
OutlinedButton(onClick = { }) { Text("Outlined") }
FilledTonalButton(onClick = { }) { Text("Tonal") }
ElevatedButton(onClick = { }) { Text("Elevated") }
TextButton(onClick = { }) { Text("Text") }
```

### Cards

- **Elevated**: shadow + surface tint — default card style
- **Filled**: surface container fill — grouped content
- **Outlined**: border + no fill — content that needs clear boundary

### Chips

- **Assist**: suggest an action (e.g., "Open in Maps")
- **Filter**: toggle filtering criteria (multi-select)
- **Input**: represent user input (e.g., email recipients)
- **Suggestion**: dynamically generated suggestions

### FAB (Floating Action Button)

- **Regular**: 56dp, primary container color
- **Small**: 40dp, for compact layouts
- **Large**: 96dp, for primary screen actions
- **Extended**: pill with icon + label, for clarity
- **Shape morphing**: FAB can morph shape on scroll/expand

### Navigation

- **Bottom Bar**: 3-5 destinations, active indicator pill, icons + labels
- **Navigation Rail**: vertical strip for medium/expanded screens, 3-7 destinations
- **Navigation Drawer**: full destination list for expanded screens
- **Active indicator**: pill-shaped highlight behind active icon (M3 signature element)

### Text Fields

- **Filled**: bottom border + filled container — default
- **Outlined**: full border — more prominent
- Both support: label, supporting text, error text, leading icon, trailing icon, character counter

### Dialogs

- **Basic**: title + text + actions (2 buttons maximum)
- **Full-screen**: for complex tasks on mobile (takes entire screen, has top app bar)

### Other Components

- **Snackbar**: temporary message at bottom, optional action button
- **Bottom Sheet**: standard (partial) or modal (full with scrim)
- **Date Picker**: docked, modal, or date range
- **Time Picker**: dial or input
- **Menu**: dropdown or exposed dropdown
- **Progress**: linear or circular, determinate or indeterminate
- **Slider**: continuous or discrete, with optional label
- **Switch**: with optional icon inside track
- **Divider**: horizontal separator, full-width or inset

---

## Typography (M3 Type Scale)

### 15 Text Styles

| Role | Size | Large | Medium | Small |
|------|------|-------|--------|-------|
| Display | For hero/splash | 57sp / 64 lh | 45sp / 52 lh | 36sp / 44 lh |
| Headline | For sections | 32sp / 40 lh | 28sp / 36 lh | 24sp / 32 lh |
| Title | For subsections | 22sp / 28 lh | 16sp / 24 lh / medium weight | 14sp / 20 lh / medium weight |
| Body | For paragraphs | 16sp / 24 lh | 14sp / 20 lh | 12sp / 16 lh |
| Label | For buttons/chips | 14sp / 20 lh / medium weight | 12sp / 16 lh / medium weight | 11sp / 16 lh / medium weight |

(sp = scaleable pixels, lh = line height)

### Default Typeface

Roboto remains the default. For brand differentiation, use Google Fonts variable fonts. M3 Expressive encourages expressive typeface choices — serif for editorial, rounded sans for playful, geometric for technical.

### Responsive Typography

- **Compact** (<600dp): use Body and Label sizes predominantly
- **Medium** (600-840dp): introduce Headline and Title
- **Expanded** (>840dp): use Display sizes for hero content

---

## Canonical Layouts (Tablet and Foldable)

### Window Size Classes

| Class | Width | Examples |
|-------|-------|---------|
| Compact | < 600dp | Phone portrait, small foldable |
| Medium | 600-840dp | Tablet portrait, large foldable, phone landscape |
| Expanded | > 840dp | Tablet landscape, desktop, foldable open |

### Layout Patterns

**List-Detail**
- Compact: full-screen list, navigate to full-screen detail
- Medium: list pane (1/3) + detail pane (2/3)
- Expanded: list pane (1/3) + detail pane (2/3) with more content

**Supporting Pane**
- Main content area + supporting information panel
- Supporting pane appears alongside on medium/expanded, as bottom sheet on compact

**Feed**
- Full-width content stream
- Compact: single column
- Medium: single column with wider margins
- Expanded: multi-column grid or single column with max-width constraint

### Navigation Adaptation

| Size Class | Primary Navigation |
|------------|-------------------|
| Compact | Bottom navigation bar |
| Medium | Navigation rail (left edge) |
| Expanded | Navigation drawer (persistent) |

```kotlin
// Adaptive navigation in Compose
NavigationSuiteScaffold(
    navigationSuiteItems = {
        items.forEach { item ->
            item(
                selected = item == currentItem,
                onClick = { currentItem = item },
                icon = { Icon(item.icon, contentDescription = null) },
                label = { Text(item.label) }
            )
        }
    }
) {
    // Content area
}
```

---

## Jetpack Compose Quick Reference

### Theme Setup

```kotlin
@Composable
fun AppTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context)
            else dynamicLightColorScheme(context)
        }
        darkTheme -> darkColorScheme()
        else -> lightColorScheme()
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        shapes = Shapes,
        content = content
    )
}
```

### Scaffold

```kotlin
Scaffold(
    topBar = {
        TopAppBar(title = { Text("Title") })
    },
    bottomBar = {
        NavigationBar { /* navigation items */ }
    },
    floatingActionButton = {
        FloatingActionButton(onClick = { }) {
            Icon(Icons.Default.Add, contentDescription = "Add")
        }
    },
    snackbarHost = { SnackbarHost(snackbarHostState) }
) { innerPadding ->
    Content(modifier = Modifier.padding(innerPadding))
}
```

### Lists

```kotlin
LazyColumn(
    contentPadding = PaddingValues(16.dp),
    verticalArrangement = Arrangement.spacedBy(8.dp)
) {
    items(data) { item ->
        ListItem(
            headlineContent = { Text(item.title) },
            supportingContent = { Text(item.subtitle) },
            leadingContent = { Icon(item.icon, contentDescription = null) }
        )
    }
}
```

### Key Dimensions

| Element | Size |
|---------|------|
| Touch target minimum | 48 x 48 dp |
| Icon size (standard) | 24 x 24 dp |
| Bottom nav bar height | 80 dp |
| Top app bar height | 64 dp |
| FAB size | 56 dp |
| Small FAB | 40 dp |
| Large FAB | 96 dp |
| Standard margin | 16 dp |
| Card elevation | 1-6 dp |
| Bottom sheet peek | 56 dp |
