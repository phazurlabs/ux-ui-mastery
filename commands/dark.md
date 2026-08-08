---
name: dark
description: "Generate a complete dark mode system — oklch luminance mapping, surface elevation, accent adjustments, shadows, toggle component, and dark tokens."
argument-hint: "[existing palette or token file]"
---

# Dark — Dark Mode System Generator

## Before running

This command needs an existing palette or token file to map.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate a complete, perceptually correct dark mode system. Not a naive color inversion — a proper oklch luminance remapping with surface elevation, text weight compensation, accent chroma shifts, and shadow replacement.

## Why Not Inversion

Color inversion fails because:
- Inverted brand colors lose identity (a blue brand becomes orange)
- Shadows become highlights, breaking spatial hierarchy
- Images become negative, destroying content
- Contrast ratios break unpredictably
- Saturation appears different at high vs. low lightness

Proper dark mode requires independent semantic remapping at the token level.

## Generation Protocol

1. **Gather inputs and existing tokens.**

   **Required:**
   - Existing light token system (from `/tokens` or `.sumi/style.json`)
   - If no tokens exist, prompt user to run `/tokens` first or provide brand colors

   **Optional:**
   - Dark mode strategy: `class` (`.dark`), `media` (`prefers-color-scheme`), or `both` (default: both)
   - Pure black or dark gray base (OLED vs. LCD optimization)
   - Sector (affects dark mode conventions — fintech dashboards expect dark; healthcare expects light default)

2. **Remap surface colors using oklch luminance mapping.**

   The core principle: in dark mode, the lightness axis flips but chroma and hue stay anchored.

   ### Surface Elevation System
   In light mode, elevation uses shadows. In dark mode, elevation uses surface lightness — higher surfaces are lighter.

   | Elevation Level | Light Mode | Dark Mode | Use Case |
   |----------------|-----------|-----------|----------|
   | Level 0 (base) | `oklch(1.0 0 0)` white | `oklch(0.13 0.005 260)` near-black | Page background |
   | Level 1 | `oklch(0.985 0 0)` off-white | `oklch(0.17 0.005 260)` dark gray | Card, sidebar |
   | Level 2 | `oklch(0.97 0 0)` light gray | `oklch(0.21 0.005 260)` | Raised card, dropdown |
   | Level 3 | `oklch(0.95 0 0)` | `oklch(0.25 0.005 260)` | Modal, dialog |
   | Level 4 | `oklch(0.93 0 0)` | `oklch(0.29 0.005 260)` | Popover, tooltip |
   | Level 5 | `oklch(0.90 0 0)` | `oklch(0.33 0.005 260)` | Toast, overlay |

   Note the slight chroma (0.005) and hue (260, blue-ish) in dark surfaces — pure gray surfaces feel dead. A tiny blue tint adds perceived depth.

   ### Luminance Mapping Formula
   For any light-mode color with lightness `L`:
   ```
   L_dark = 1.0 - L + 0.05  (clamped to 0.08–0.95)
   ```
   This is approximate. Fine-tune per token for optimal contrast.

3. **Remap text colors with weight compensation.**

   Light text on dark backgrounds appears thinner than dark text on light backgrounds (irradiation illusion). Compensate:

   | Text Role | Light Mode | Dark Mode | Compensation |
   |-----------|-----------|-----------|--------------|
   | Primary | `oklch(0.15 0 0)` 900-weight | `oklch(0.93 0 0)` slightly thicker | Bump font-weight by 1 step or use -webkit-font-smoothing: antialiased |
   | Secondary | `oklch(0.40 0 0)` 600-weight | `oklch(0.75 0 0)` | Same compensation |
   | Tertiary | `oklch(0.55 0 0)` | `oklch(0.60 0 0)` | Minimum contrast 4.5:1 |
   | Disabled | `oklch(0.65 0 0)` | `oklch(0.45 0 0)` | Still readable, 3:1 minimum |
   | Link | Brand color at L=0.45 | Brand color at L=0.70 | Higher lightness for visibility |

   **Anti-aliasing adjustment:**
   ```css
   .dark {
     -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
   }
   ```
   This prevents light-on-dark text from appearing too bold on macOS/iOS.

4. **Adjust accent and brand colors for dark backgrounds.**

   Brand and accent colors need modification for dark mode:

   ### Chroma and Lightness Shifts
   ```
   For brand color oklch(L C H):
     Dark mode: oklch(L + 0.10, C + 0.02, H)
   ```
   - Increase lightness by ~0.10 to maintain visibility
   - Slightly increase chroma to counteract dark background absorption
   - Hue stays constant (brand identity)

   ### Semantic Color Adjustments
   | Color | Light Mode | Dark Mode | Reason |
   |-------|-----------|-----------|--------|
   | Success green | `oklch(0.50 0.15 145)` | `oklch(0.65 0.17 145)` | Lighter, slightly more vivid |
   | Warning amber | `oklch(0.55 0.15 85)` | `oklch(0.70 0.17 85)` | Same shift |
   | Error red | `oklch(0.55 0.20 25)` | `oklch(0.65 0.22 25)` | Careful — red is already attention-grabbing |
   | Info blue | `oklch(0.55 0.15 250)` | `oklch(0.65 0.17 250)` | Standard shift |

   ### Feedback Background Tints
   In light mode, feedback backgrounds are light tints (green-50, red-50). In dark mode, use low-opacity overlays:
   ```css
   .dark .alert-success {
     background: oklch(0.65 0.17 145 / 0.12);
     border-color: oklch(0.65 0.17 145 / 0.30);
   }
   ```
   This keeps feedback colors visible without overwhelming the dark surface.

5. **Replace shadows with borders or glow.**

   Shadows are invisible or ugly on dark backgrounds. Replace the shadow system:

   | Light Mode Shadow | Dark Mode Replacement | CSS |
   |------------------|-----------------------|-----|
   | `shadow.xs` (subtle lift) | 1px border at 8% white | `border: 1px solid oklch(1 0 0 / 0.08)` |
   | `shadow.sm` (raised) | 1px border at 10% white | `border: 1px solid oklch(1 0 0 / 0.10)` |
   | `shadow.md` (dropdown) | 1px border at 12% white + subtle glow | `border: 1px solid oklch(1 0 0 / 0.12); box-shadow: 0 4px 16px oklch(0 0 0 / 0.4)` |
   | `shadow.lg` (modal) | 2px border at 12% white + ambient glow | `border: 1px solid oklch(1 0 0 / 0.12); box-shadow: 0 8px 32px oklch(0 0 0 / 0.5)` |
   | `shadow.xl` (toast) | 1px border at 15% white + strong glow | `border: 1px solid oklch(1 0 0 / 0.15); box-shadow: 0 12px 48px oklch(0 0 0 / 0.6)` |

   The key insight: dark mode relies on borders (light edges) instead of shadows (dark underneath) to communicate elevation.

6. **Image and media treatment.**

   Images and media need CSS adjustments in dark mode:

   ```css
   /* Reduce brightness and boost contrast slightly */
   .dark img:not([data-dark-safe]) {
     filter: brightness(0.90) contrast(1.05);
   }

   /* Transparent PNGs with dark content may need inversion */
   .dark img[data-invert-dark] {
     filter: invert(1) hue-rotate(180deg);
   }

   /* SVG illustrations — prefer currentColor or CSS-controlled fills */
   .dark svg.illustration {
     opacity: 0.85;
   }

   /* Video — reduce brightness */
   .dark video {
     filter: brightness(0.92);
   }

   /* Decorative backgrounds — darken */
   .dark [data-decorative-bg] {
     opacity: 0.6;
   }
   ```

   **Best practice:** Use `<picture>` with separate dark-mode assets for hero images:
   ```html
   <picture>
     <source srcset="hero-dark.webp" media="(prefers-color-scheme: dark)">
     <img src="hero-light.webp" alt="Hero">
   </picture>
   ```

7. **Generate CSS implementation.**

   ### Strategy: Class + Media Query (recommended)
   ```css
   /* ============================================
      DARK MODE TOKENS
      Strategy: .dark class + prefers-color-scheme
      ============================================ */

   /* --- Light theme (default) --- */
   :root {
     --color-bg-primary: oklch(1.0 0 0);
     --color-bg-secondary: oklch(0.985 0 0);
     --color-bg-surface: oklch(1.0 0 0);
     --color-bg-surface-raised: oklch(0.985 0 0);
     --color-bg-overlay: oklch(0 0 0 / 0.5);

     --color-text-primary: oklch(0.15 0 0);
     --color-text-secondary: oklch(0.40 0 0);
     --color-text-tertiary: oklch(0.55 0 0);
     --color-text-disabled: oklch(0.65 0 0);

     --color-border-default: oklch(0.85 0 0);
     --color-border-strong: oklch(0.70 0 0);
     --color-border-subtle: oklch(0.92 0 0);

     --shadow-xs: 0 1px 2px oklch(0 0 0 / 0.05);
     --shadow-sm: 0 1px 3px oklch(0 0 0 / 0.1), 0 1px 2px oklch(0 0 0 / 0.06);
     --shadow-md: 0 4px 6px -1px oklch(0 0 0 / 0.1), 0 2px 4px -2px oklch(0 0 0 / 0.1);
     --shadow-lg: 0 10px 15px -3px oklch(0 0 0 / 0.1), 0 4px 6px -4px oklch(0 0 0 / 0.1);

     --font-smoothing: auto;
     --img-brightness: 1;
     --img-contrast: 1;
   }

   /* --- Dark theme via class --- */
   .dark,
   [data-theme="dark"] {
     color-scheme: dark;

     --color-bg-primary: oklch(0.13 0.005 260);
     --color-bg-secondary: oklch(0.17 0.005 260);
     --color-bg-surface: oklch(0.17 0.005 260);
     --color-bg-surface-raised: oklch(0.21 0.005 260);
     --color-bg-overlay: oklch(0 0 0 / 0.7);

     --color-text-primary: oklch(0.93 0 0);
     --color-text-secondary: oklch(0.75 0 0);
     --color-text-tertiary: oklch(0.60 0 0);
     --color-text-disabled: oklch(0.45 0 0);

     --color-border-default: oklch(1 0 0 / 0.10);
     --color-border-strong: oklch(1 0 0 / 0.20);
     --color-border-subtle: oklch(1 0 0 / 0.06);

     --shadow-xs: none;
     --shadow-sm: none;
     --shadow-md: 0 4px 16px oklch(0 0 0 / 0.4);
     --shadow-lg: 0 8px 32px oklch(0 0 0 / 0.5);

     --font-smoothing: antialiased;
     --img-brightness: 0.90;
     --img-contrast: 1.05;
   }

   /* --- Dark theme via OS preference --- */
   @media (prefers-color-scheme: dark) {
     :root:not([data-theme="light"]):not(.light) {
       color-scheme: dark;
       /* Same values as .dark above */
       --color-bg-primary: oklch(0.13 0.005 260);
       --color-bg-secondary: oklch(0.17 0.005 260);
       --color-bg-surface: oklch(0.17 0.005 260);
       --color-bg-surface-raised: oklch(0.21 0.005 260);
       --color-bg-overlay: oklch(0 0 0 / 0.7);

       --color-text-primary: oklch(0.93 0 0);
       --color-text-secondary: oklch(0.75 0 0);
       --color-text-tertiary: oklch(0.60 0 0);
       --color-text-disabled: oklch(0.45 0 0);

       --color-border-default: oklch(1 0 0 / 0.10);
       --color-border-strong: oklch(1 0 0 / 0.20);
       --color-border-subtle: oklch(1 0 0 / 0.06);

       --shadow-xs: none;
       --shadow-sm: none;
       --shadow-md: 0 4px 16px oklch(0 0 0 / 0.4);
       --shadow-lg: 0 8px 32px oklch(0 0 0 / 0.5);

       --font-smoothing: antialiased;
       --img-brightness: 0.90;
       --img-contrast: 1.05;
     }
   }

   /* --- Apply font smoothing --- */
   body {
     -webkit-font-smoothing: var(--font-smoothing);
     -moz-osx-font-smoothing: var(--font-smoothing);
   }

   /* --- Image treatment --- */
   .dark img:not([data-dark-safe]),
   [data-theme="dark"] img:not([data-dark-safe]) {
     filter: brightness(var(--img-brightness)) contrast(var(--img-contrast));
   }
   ```

8. **Generate dark mode toggle component (React).**

   ```tsx
   'use client';
   import { useEffect, useState } from 'react';

   type Theme = 'light' | 'dark' | 'system';

   function getSystemTheme(): 'light' | 'dark' {
     if (typeof window === 'undefined') return 'light';
     return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
   }

   function applyTheme(theme: Theme) {
     const root = document.documentElement;
     const resolved = theme === 'system' ? getSystemTheme() : theme;

     root.classList.remove('light', 'dark');
     root.classList.add(resolved);
     root.setAttribute('data-theme', resolved);
     root.style.colorScheme = resolved;
   }

   export function ThemeProvider({ children }: { children: React.ReactNode }) {
     const [theme, setTheme] = useState<Theme>('system');

     useEffect(() => {
       const stored = localStorage.getItem('theme') as Theme | null;
       const initial = stored ?? 'system';
       setTheme(initial);
       applyTheme(initial);
     }, []);

     useEffect(() => {
       const mq = window.matchMedia('(prefers-color-scheme: dark)');
       const handler = () => { if (theme === 'system') applyTheme('system'); };
       mq.addEventListener('change', handler);
       return () => mq.removeEventListener('change', handler);
     }, [theme]);

     const setAndPersist = (next: Theme) => {
       setTheme(next);
       localStorage.setItem('theme', next);
       applyTheme(next);
     };

     return (
       <ThemeContext.Provider value={{ theme, setTheme: setAndPersist }}>
         {children}
       </ThemeContext.Provider>
     );
   }

   /* --- Inline script to prevent flash of wrong theme --- */
   export const ThemeScript = () => (
     <script
       dangerouslySetInnerHTML={{
         __html: `
           (function() {
             try {
               var t = localStorage.getItem('theme') || 'system';
               var r = t === 'system'
                 ? (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
                 : t;
               document.documentElement.classList.add(r);
               document.documentElement.setAttribute('data-theme', r);
               document.documentElement.style.colorScheme = r;
             } catch(e) {}
           })();
         `,
       }}
     />
   );

   /* --- Toggle Button --- */
   export function ThemeToggle() {
     const { theme, setTheme } = useTheme();

     const cycle = () => {
       const order: Theme[] = ['light', 'dark', 'system'];
       const next = order[(order.indexOf(theme) + 1) % order.length];
       setTheme(next);
     };

     const icon = theme === 'dark' ? '🌙' : theme === 'light' ? '☀️' : '💻';
     const label = theme === 'dark' ? 'Dark' : theme === 'light' ? 'Light' : 'System';

     return (
       <button
         onClick={cycle}
         aria-label={`Current theme: ${label}. Click to change.`}
         className="theme-toggle"
       >
         <span aria-hidden="true">{icon}</span>
         <span className="sr-only">{label} theme</span>
       </button>
     );
   }

   /* Context (internal) */
   import { createContext, useContext } from 'react';
   const ThemeContext = createContext<{
     theme: Theme;
     setTheme: (t: Theme) => void;
   }>({ theme: 'system', setTheme: () => {} });
   export const useTheme = () => useContext(ThemeContext);
   ```

9. **Save dark tokens to `.sumi/style.json`.**

   Merge dark theme tokens into the existing token file under `$themes.dark`:
   ```json
   {
     "$themes": {
       "dark": {
         "color": {
           "bg": {
             "primary": { "$value": "oklch(0.13 0.005 260)" },
             "secondary": { "$value": "oklch(0.17 0.005 260)" },
             "surface": { "$value": "oklch(0.17 0.005 260)" },
             "surface-raised": { "$value": "oklch(0.21 0.005 260)" }
           },
           "text": {
             "primary": { "$value": "oklch(0.93 0 0)" },
             "secondary": { "$value": "oklch(0.75 0 0)" }
           },
           "border": {
             "default": { "$value": "oklch(1 0 0 / 0.10)" },
             "strong": { "$value": "oklch(1 0 0 / 0.20)" }
           }
         },
         "shadow": {
           "xs": { "$value": "none" },
           "sm": { "$value": "none" },
           "md": { "$value": "0 4px 16px oklch(0 0 0 / 0.4)" },
           "lg": { "$value": "0 8px 32px oklch(0 0 0 / 0.5)" }
         }
       }
     }
   }
   ```

## Dark Mode Checklist

Before shipping, verify:

| Check | What to Verify | How |
|-------|---------------|-----|
| No pure black backgrounds | Base surface is `oklch(0.13 ...)` not `oklch(0 0 0)` | Visual inspection |
| No pure white text | Primary text is `oklch(0.93 ...)` not `oklch(1 0 0)` | Visual inspection |
| Surface elevation visible | Cards are lighter than page background | Side-by-side comparison |
| Brand color visible | Brand color has sufficient contrast on dark surfaces | Contrast checker (4.5:1 min) |
| Shadows replaced | No dark shadows on dark backgrounds | Visual inspection |
| Images not harsh | Filter applied to non-dark-safe images | Toggle between modes |
| Font smoothing active | antialiased rendering on dark mode | macOS zoom test |
| Focus rings visible | Focus indicators contrast against dark surface | Tab through all interactive elements |
| Feedback colors adjusted | Success/error/warning visible on dark surfaces | Trigger all states |
| Form inputs readable | Input backgrounds distinguish from page background | Fill out forms in dark mode |
| Scrollbar styled | Native scrollbar not jarring (if custom scrollbar used) | Scroll long pages |
| Toggle no flash | Page does not flash white on load when dark is stored | Hard refresh test |
| Third-party embeds | iframes and embeds are not blindingly white | Check all embedded content |

## Output Format

```
### Phase Position
> **Phase: BUILD** | `/dark`
> *Visual Design | Dark Mode System*

## Dark Mode System: [Project Name]

### Configuration
- **Strategy**: [class / media / both]
- **Base surface**: [near-black / pure black (OLED)]
- **Surface tint**: [hue value for surface warmth/coolness]
- **Source tokens**: [.sumi/style.json or manually provided]

### Surface Elevation Map
[Table showing light → dark mapping for all 6 elevation levels]

### Color Remapping
[Complete token remapping table: light value → dark value with oklch notation]

### Text Adjustments
[Text color remapping with weight compensation notes]

### Accent & Semantic Color Shifts
[Brand, success, warning, error, info adjustments with oklch values]

### Shadow Replacement
[Shadow → border/glow replacement table]

### Image Treatment
[CSS filters and <picture> strategy]

### CSS Implementation
[Complete CSS with :root, .dark, and @media blocks]

### React Toggle Component
[ThemeProvider, ThemeScript, ThemeToggle components]

### Dark Mode Checklist
[Verified checklist with pass/fail for each item]

### Saved
> Dark tokens merged into `.sumi/style.json` under `$themes.dark`
```

## Cross-References

When generating dark mode, draw from:
- `ui-visual-design-system` skill for color theory and perceptual principles
- `color-palette-library` skill for oklch dark mode mapping
- `shadow-elevation-density` skill for elevation hierarchy and dark mode shadow replacement
- `accessibility-inclusive-design` skill for dark mode contrast verification
- `platform-visual-standards` skill for iOS dark mode and Material 3 dark theme conventions
- `component-patterns-code` skill for toggle component implementation

## Next Step

**Next** → `/screen` — Build dark-mode-ready screens

**Alternatives**:
- `/tokens` — Generate the base token system if not done yet
- `/responsive` — Add responsive behavior to dark mode layouts
- `/access` — Audit dark mode for accessibility compliance
- `/guide` — See the full journey
