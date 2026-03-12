# Brand Color Systems — 30+ World-Class References

This reference catalogs 30+ world-class brand color systems used by leading digital products. Each entry includes: primary colors in oklch + hex, a full 10-step scale, semantic color mapping, dark mode variant, and a design analysis of what makes the system work.

Use this reference when building a new brand color system, benchmarking against leaders, or understanding the design reasoning behind successful palettes.

---

## 1. Stripe

**Category:** Fintech / Developer Tools
**Signature:** Indigo-to-teal gradient system with rich, saturated accents

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Primary (Blurple) | oklch(50% 0.22 270) | #635BFF | Brand identity, CTAs, links |
| Secondary (Teal) | oklch(62% 0.14 195) | #11C6A7 | Success states, accents |
| Accent (Cyan) | oklch(72% 0.12 210) | #80E9FF | Illustrations, gradients |
| Dark (Midnight) | oklch(18% 0.04 270) | #1A1F36 | Dark surfaces, text |
| Light (Mist) | oklch(97% 0.01 270) | #F6F9FC | Page backgrounds |

### 10-Step Blurple Scale
```
--stripe-50:  oklch(96% 0.02 270);  /* #F0EEFF */
--stripe-100: oklch(92% 0.04 270);  /* #DEDCFF */
--stripe-200: oklch(84% 0.08 270);  /* #BFBAFF */
--stripe-300: oklch(74% 0.14 270);  /* #9B94FF */
--stripe-400: oklch(62% 0.18 270);  /* #7A73FF */
--stripe-500: oklch(50% 0.22 270);  /* #635BFF */
--stripe-600: oklch(42% 0.20 270);  /* #4F48CC */
--stripe-700: oklch(34% 0.17 270);  /* #3D3699 */
--stripe-800: oklch(25% 0.14 270);  /* #2B2566 */
--stripe-900: oklch(18% 0.10 270);  /* #1A1744 */
--stripe-950: oklch(12% 0.07 270);  /* #0F0E2B */
```

### Semantic Mapping
```css
--stripe-surface: var(--stripe-50);
--stripe-text: var(--stripe-900);
--stripe-primary: var(--stripe-500);
--stripe-primary-hover: var(--stripe-600);
--stripe-subtle: var(--stripe-100);
```

### Dark Mode Variant
```css
--stripe-surface: oklch(13% 0.03 270);       /* #0A0B1E */
--stripe-text: oklch(92% 0.01 270);           /* #E3E5ED */
--stripe-primary: oklch(62% 0.18 270);        /* Lightened blurple */
--stripe-primary-hover: oklch(68% 0.16 270);
--stripe-subtle: oklch(18% 0.06 270);
```

### Why It Works
Stripe's blurple is distinctive because it sits between blue (trust) and purple (premium) — perfect for a financial product targeting developers and businesses. The teal secondary creates energy without competing with the primary. The gradient system (blurple -> teal -> cyan) feels kinetic and modern. The dark mode uses extremely low-lightness backgrounds with a purple tint that maintains brand personality.

---

## 2. Linear

**Category:** SaaS / Productivity
**Signature:** Neutral-dominant system with precisely deployed violet accents

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Primary (Violet) | oklch(55% 0.22 295) | #5E6AD2 | Brand, interactive |
| Neutral (Graphite) | oklch(55% 0.01 265) | #6B6F76 | Body text |
| Dark BG | oklch(13% 0.01 265) | #1B1C1E | App background |
| Surface | oklch(17% 0.01 265) | #222326 | Cards, panels |
| Border | oklch(24% 0.01 265) | #33353A | Dividers |

### 10-Step Violet Scale
```
--linear-50:  oklch(96% 0.02 295);  /* #F0F0FF */
--linear-100: oklch(92% 0.04 295);  /* #DEDEFF */
--linear-200: oklch(84% 0.08 295);  /* #BEBEFC */
--linear-300: oklch(74% 0.14 295);  /* #9B9BF0 */
--linear-400: oklch(64% 0.18 295);  /* #7C7CE2 */
--linear-500: oklch(55% 0.22 295);  /* #5E6AD2 */
--linear-600: oklch(46% 0.20 295);  /* #4B54A8 */
--linear-700: oklch(37% 0.17 295);  /* #3A407E */
--linear-800: oklch(27% 0.14 295);  /* #2A2D5C */
--linear-900: oklch(19% 0.10 295);  /* #1C1E3E */
--linear-950: oklch(13% 0.07 295);  /* #121328 */
```

### Why It Works
Linear is a dark-mode-first product. The neutral dominance lets content breathe — issues, projects, and roadmaps are the stars, not the chrome. The violet accent is used sparingly (selected states, active tabs, CTAs) which makes it feel precious and intentional. The extremely low-chroma neutrals prevent the dark interface from feeling cold — there is just enough warmth in the gray to feel sophisticated rather than clinical.

---

## 3. Vercel

**Category:** Developer Tools / Platform
**Signature:** Black/white binary with surgical gray precision

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Primary (Black) | oklch(0% 0 0) | #000000 | Brand, text, buttons |
| Background (White) | oklch(100% 0 0) | #FFFFFF | Page bg |
| Gray 100 | oklch(96% 0.003 265) | #F3F3F3 | Subtle bg |
| Gray 400 | oklch(70% 0.005 265) | #999999 | Secondary text |
| Gray 700 | oklch(40% 0.005 265) | #555555 | Borders |
| Blue (Link) | oklch(60% 0.18 255) | #0070F3 | Links, accents |
| Error (Red) | oklch(55% 0.20 30) | #EE0000 | Errors |
| Success (Green) | oklch(58% 0.16 150) | #0CAA34 | Success states |
| Warning (Amber) | oklch(72% 0.16 85) | #F5A623 | Warnings |

### 10-Step Gray Scale
```
--vercel-50:  oklch(98% 0.002 265);  /* #FAFAFA */
--vercel-100: oklch(96% 0.003 265);  /* #F3F3F3 */
--vercel-200: oklch(90% 0.004 265);  /* #EBEBEB */
--vercel-300: oklch(82% 0.004 265);  /* #CCCCCC */
--vercel-400: oklch(70% 0.005 265);  /* #999999 */
--vercel-500: oklch(58% 0.005 265);  /* #777777 */
--vercel-600: oklch(47% 0.005 265);  /* #666666 */
--vercel-700: oklch(40% 0.005 265);  /* #555555 */
--vercel-800: oklch(30% 0.005 265);  /* #333333 */
--vercel-900: oklch(20% 0.003 265);  /* #222222 */
--vercel-950: oklch(10% 0.002 265);  /* #111111 */
```

### Dark Mode Variant
Vercel inverts cleanly because its system is near-achromatic. Background becomes #000, text becomes #FAFAFA, and the gray scale reverses. The blue link and status colors remain largely unchanged.

### Why It Works
Vercel's brand IS the absence of color. By stripping everything to black, white, and carefully graduated grays, they communicate: "We are infrastructure — invisible, reliable, fast." The near-zero chroma grays (C: 0.002-0.005) prevent any warm/cool bias. The single accent blue is used only for links and interactive focus. This system is the ultimate content-first palette — it works for any product deployed on the platform.

---

## 4. Notion

**Category:** SaaS / Productivity / Knowledge
**Signature:** Warm off-white with soft, pastel accents

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Background | oklch(99% 0.005 85) | #FFFFFF | Page bg |
| Warm Neutral | oklch(97% 0.008 85) | #FBFBFA | Sidebar |
| Text Primary | oklch(23% 0.01 85) | #37352F | Body text |
| Text Secondary | oklch(55% 0.01 85) | #9B9A97 | Muted text |
| Brown | oklch(52% 0.08 55) | #64473A | Tags, callouts |
| Orange | oklch(65% 0.14 65) | #D9730D | Highlights |
| Yellow | oklch(82% 0.12 92) | #DFAB01 | Highlights |
| Green | oklch(55% 0.12 155) | #0F7B6C | Tags |
| Blue | oklch(55% 0.14 255) | #0B6E99 | Links |
| Purple | oklch(50% 0.14 300) | #6940A5 | Tags |
| Pink | oklch(55% 0.14 350) | #AD1A72 | Tags |
| Red | oklch(55% 0.16 25) | #E03E3E | Tags |

### Why It Works
Notion feels like a physical notebook because of its warm-tinted neutrals (hue 85 = warm yellow undertone). The text color is not pure black but a warm near-black (#37352F) that reduces harshness. The accent colors are deliberately muted — lower chroma than typical SaaS products — which keeps the focus on user content. Each accent color works as both text and background tint, creating a versatile system from minimal inputs.

---

## 5. Figma

**Category:** Design Tools
**Signature:** Purple-red gradient with a rainbow of category colors

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Primary (Purple) | oklch(48% 0.22 310) | #A259FF | Brand, design mode |
| Secondary (Coral) | oklch(62% 0.18 25) | #FF7262 | Dev mode |
| Green | oklch(60% 0.16 155) | #0ACF83 | Prototype mode |
| Blue | oklch(58% 0.18 260) | #1ABCFE | Inspect |
| Orange | oklch(68% 0.16 68) | #F24E1E | Logo, FigJam |
| Dark | oklch(17% 0.01 265) | #1E1E1E | Canvas bg |
| Light | oklch(97% 0.005 265) | #F5F5F5 | Panel bg |

### Why It Works
Figma uses color as product architecture. Each mode (Design, Dev, Prototype) has its own hue, making navigation intuitive at a glance. The primary purple is high-chroma and distinctive in the design tool space. The dark canvas background (#1E1E1E) is not pure black — it has enough lightness to show design work without eye strain. The rainbow secondary palette mirrors Figma's philosophy: design should be colorful, collaborative, and playful.

---

## 6. Shopify

**Category:** E-commerce / Platform
**Signature:** Green ecosystem with warm, approachable tones

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Primary (Green) | oklch(58% 0.18 155) | #008060 | Brand, CTAs |
| Secondary (Dark Green) | oklch(35% 0.14 155) | #004C3F | Hover states |
| Surface | oklch(98% 0.005 155) | #F6F6F7 | Page bg |
| Text | oklch(22% 0.01 265) | #202223 | Body text |
| Highlight (Yellow) | oklch(92% 0.10 95) | #FFF8DB | Alerts, badges |
| Critical (Red) | oklch(55% 0.18 25) | #D82C0D | Errors, destructive |
| Success (Green) | oklch(62% 0.14 155) | #008060 | Confirmations |
| Warning (Orange) | oklch(72% 0.14 70) | #FFC453 | Caution states |
| Info (Teal) | oklch(60% 0.12 200) | #2C6ECB | Informational |

### Polaris Design System Scale (Green)
```
--shopify-50:  oklch(96% 0.02 155);  /* #F1F8F5 */
--shopify-100: oklch(92% 0.04 155);  /* #D4EDDF */
--shopify-200: oklch(84% 0.08 155);  /* #A3D9BF */
--shopify-300: oklch(74% 0.12 155);  /* #6DC09C */
--shopify-400: oklch(66% 0.15 155);  /* #3DA87D */
--shopify-500: oklch(58% 0.18 155);  /* #008060 */
--shopify-600: oklch(48% 0.16 155);  /* #006B4F */
--shopify-700: oklch(38% 0.14 155);  /* #005540 */
--shopify-800: oklch(28% 0.11 155);  /* #003F30 */
--shopify-900: oklch(20% 0.08 155);  /* #002B21 */
--shopify-950: oklch(14% 0.06 155);  /* #001B15 */
```

### Why It Works
Shopify's green communicates growth, money, and success — all aligned with its merchant platform mission. The Polaris system is remarkably well-documented with clear token mapping. The warm neutrals prevent the green from feeling clinical (a risk with green-dominant palettes). The status colors are carefully chosen to be distinguishable from the brand green: red (destructive) has maximum hue distance, and info blue provides complementary contrast.

---

## 7. GitHub

**Category:** Developer Platform
**Signature:** Dark-first with syntax-inspired palette

### Primary Palette (Dark Default)
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Canvas Default | oklch(14% 0.01 265) | #0D1117 | Page bg |
| Canvas Subtle | oklch(18% 0.01 265) | #161B22 | Secondary bg |
| Canvas Inset | oklch(11% 0.01 265) | #010409 | Inset areas |
| Text Primary | oklch(88% 0.01 265) | #E6EDF3 | Body text |
| Text Secondary | oklch(62% 0.01 265) | #8B949E | Muted text |
| Accent (Blue) | oklch(62% 0.16 255) | #58A6FF | Links, selected |
| Success (Green) | oklch(62% 0.14 155) | #3FB950 | Merged, added |
| Danger (Red) | oklch(58% 0.16 25) | #F85149 | Deleted, error |
| Warning (Yellow) | oklch(70% 0.14 90) | #D29922 | Pending, caution |
| Accent (Purple) | oklch(60% 0.14 295) | #BC8CFF | Reviewed |

### Why It Works
GitHub's palette is designed for code. The dark canvas (#0D1117) is specifically chosen to reduce eye strain during long coding sessions while maintaining enough contrast for syntax highlighting. Each accent color maps to a git concept (green=added, red=deleted, yellow=modified, purple=reviewed). The text primary (#E6EDF3) is desaturated and slightly warm — pure white would be too harsh on dark backgrounds at the scale GitHub is used.

---

## 8. Apple (System Colors)

**Category:** Platform / Operating System
**Signature:** Dynamic, context-aware system colors that adapt to light/dark/contrast modes

### System Colors (iOS/macOS Light)
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| System Blue | oklch(55% 0.22 260) | #007AFF | Primary actions, links |
| System Green | oklch(58% 0.18 150) | #34C759 | Success, positive |
| System Indigo | oklch(48% 0.20 280) | #5856D6 | Accent, branding |
| System Orange | oklch(68% 0.18 65) | #FF9500 | Warnings |
| System Pink | oklch(58% 0.20 355) | #FF2D55 | Featured, health |
| System Purple | oklch(52% 0.18 305) | #AF52DE | Creative, premium |
| System Red | oklch(55% 0.22 30) | #FF3B30 | Destructive, error |
| System Teal | oklch(60% 0.12 200) | #5AC8FA | Info |
| System Yellow | oklch(82% 0.15 95) | #FFCC00 | Highlights |

### Dynamic Color Adaptation
Apple's system colors automatically adjust across 6 contexts:
1. Light mode (default — full saturation)
2. Dark mode (slightly lighter, reduced chroma)
3. Elevated dark mode (sheets, popovers — even lighter)
4. High contrast light (darker, increased saturation)
5. High contrast dark (lighter, increased saturation)
6. Accessibility tint (user-defined system accent)

### Why It Works
Apple does not define a single palette — it defines color BEHAVIOR. Each system color has 6+ variants that the OS selects automatically based on context. This ensures contrast compliance across every appearance mode without manual mapping. The hue choices are optimized for P3 wide-gamut displays (default on Apple devices since 2016), meaning they appear more vivid than their sRGB hex values suggest.

---

## 9. Google Material Design (Material 3)

**Category:** Design System / Platform
**Signature:** HCT tonal palettes generated algorithmically from user wallpaper

### Baseline Palette (Purple)
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Primary | oklch(48% 0.20 295) | #6750A4 | FAB, key buttons |
| On Primary | oklch(100% 0 0) | #FFFFFF | Text on primary |
| Primary Container | oklch(88% 0.08 295) | #EADDFF | Chips, cards |
| On Primary Container | oklch(22% 0.14 295) | #21005D | Text on container |
| Secondary | oklch(45% 0.06 295) | #625B71 | Secondary buttons |
| Tertiary | oklch(47% 0.10 345) | #7D5260 | Tertiary accent |
| Surface | oklch(98% 0.01 295) | #FFFBFE | Page bg |
| On Surface | oklch(15% 0.02 295) | #1C1B1F | Body text |
| Error | oklch(48% 0.20 25) | #B3261E | Errors |

### HCT Tonal Palette (Primary)
Material 3 generates tonal palettes using HCT (Hue, Chroma, Tone) with 13 tone steps:
```
Tone 0:   oklch(0% 0 295);      /* #000000 */
Tone 10:  oklch(15% 0.10 295);  /* #21005D */
Tone 20:  oklch(22% 0.14 295);  /* #381E72 */
Tone 30:  oklch(30% 0.18 295);  /* #4F378B */
Tone 40:  oklch(38% 0.20 295);  /* #6750A4 */
Tone 50:  oklch(48% 0.20 295);  /* #7F67BE */
Tone 60:  oklch(58% 0.18 295);  /* #9A82DB */
Tone 70:  oklch(68% 0.14 295);  /* #B69DF8 */
Tone 80:  oklch(78% 0.10 295);  /* #D0BCFF */
Tone 90:  oklch(88% 0.06 295);  /* #EADDFF */
Tone 95:  oklch(94% 0.03 295);  /* #F6EDFF */
Tone 99:  oklch(98% 0.01 295);  /* #FFFBFE */
Tone 100: oklch(100% 0 0);      /* #FFFFFF */
```

### Why It Works
Material 3 introduced Dynamic Color — the palette is generated FROM the user's wallpaper using the HCT color space. This means every Android device has a personalized color system. The tonal palette approach ensures accessibility because color roles are mapped to specific tone values (primary = tone 40 in light, tone 80 in dark), guaranteeing contrast ratios by construction rather than manual checking.

---

## 10. Spotify

**Category:** Music / Entertainment
**Signature:** Iconic green + dark UI with album-art-driven dynamic color

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Brand Green | oklch(68% 0.22 155) | #1DB954 | Brand mark, shuffle |
| Dark BG | oklch(10% 0.01 265) | #121212 | App bg |
| Surface | oklch(14% 0.01 265) | #181818 | Cards |
| Surface Light | oklch(20% 0.01 265) | #282828 | Hover states |
| Text Primary | oklch(100% 0 0) | #FFFFFF | Headlines |
| Text Secondary | oklch(70% 0.01 265) | #B3B3B3 | Body text |
| Text Tertiary | oklch(50% 0.01 265) | #727272 | Muted text |

### Why It Works
Spotify is a dark-mode-only product — the dark background reduces eye strain during extended listening sessions and makes album artwork pop (the REAL color in the app). The green is used surgically: only for the brand mark and the most important interactive elements (play, shuffle). Everything else is gray. This creates extreme focus on the one green element on screen, making it a powerful affordance signal. The dynamic gradient headers extracted from album art bring life to an otherwise austere palette.

---

## 11. Slack

**Category:** Communication / Collaboration
**Signature:** Aubergine brand + user-customizable sidebar themes

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Aubergine | oklch(22% 0.08 320) | #4A154B | Sidebar default |
| Brand Purple | oklch(48% 0.16 310) | #611F69 | Brand mark |
| Blue | oklch(55% 0.16 255) | #1264A3 | Links, selected |
| Green | oklch(60% 0.16 155) | #2BAC76 | Online, success |
| Yellow | oklch(80% 0.14 95) | #ECB22E | Away, warnings |
| Red | oklch(55% 0.18 25) | #E01E5A | Notifications, error |
| Surface | oklch(98% 0 0) | #FFFFFF | Message area |
| Text | oklch(18% 0.01 265) | #1D1C1D | Message text |

### Why It Works
Slack's genius is making the sidebar user-customizable (theme colors change the sidebar) while keeping the message area consistent (always white/near-white). The aubergine default is distinctive in the blue-dominated collaboration space. The four accent colors (blue, green, yellow, red) map directly to user states (active, online, away, DND) — color IS information in Slack.

---

## 12. Twitter/X

**Category:** Social Media
**Signature:** Blue identity with high-contrast dark mode options

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Brand Blue | oklch(58% 0.18 245) | #1D9BF0 | Links, brand |
| Black | oklch(0% 0 0) | #000000 | Lights Out bg |
| Dim BG | oklch(16% 0.02 255) | #15202B | Dim mode bg |
| Surface | oklch(100% 0 0) | #FFFFFF | Default bg |
| Text Primary | oklch(10% 0.01 265) | #0F1419 | Body text |
| Text Secondary | oklch(50% 0.01 265) | #536471 | Muted text |
| Like (Pink) | oklch(58% 0.20 350) | #F91880 | Heart icon |
| Retweet (Green) | oklch(60% 0.16 155) | #00BA7C | Repost icon |

### Why It Works
Twitter's blue is the most recognizable social media color in the world. The three theme options (Default/Dim/Lights Out) give users control over luminance while maintaining the same semantic color roles. The like-pink and retweet-green create instant action recognition — users identify the interaction type from color alone, even at small icon sizes.

---

## 13. Airbnb

**Category:** Marketplace / Travel
**Signature:** Rausch red (named after their founding street) + warm neutrals

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Rausch (Red-Pink) | oklch(56% 0.20 15) | #FF5A5F | Brand, CTAs, love |
| Babu (Teal) | oklch(55% 0.10 195) | #00A699 | Secondary accent |
| Arches (Peach) | oklch(78% 0.10 55) | #FC642D | Illustrations |
| Hof (Dark) | oklch(25% 0.01 265) | #484848 | Text |
| Foggy (Gray) | oklch(72% 0.005 265) | #767676 | Secondary text |
| Beach (Light) | oklch(98% 0.005 55) | #FFFFFF | Backgrounds |

### Why It Works
Airbnb's Rausch red sits between red and pink, evoking warmth, belonging, and love — aligning with their "belong anywhere" mission. It is NOT a typical corporate red. The warm neutral text (#484848 instead of pure black) makes the interface feel domestic and welcoming. The secondary teal provides enough contrast for interactive elements without competing with the emotional warmth of the primary.

---

## 14. Mercury

**Category:** Fintech / Banking
**Signature:** Navy + clean, high-trust minimal system

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Navy | oklch(30% 0.10 260) | #1C3149 | Brand, headings |
| Blue Accent | oklch(55% 0.16 255) | #3B6CF5 | Links, buttons |
| Surface | oklch(99% 0.003 260) | #FAFBFD | Page bg |
| Card | oklch(100% 0 0) | #FFFFFF | Card bg |
| Text Primary | oklch(20% 0.02 260) | #1A2233 | Body text |
| Text Secondary | oklch(52% 0.01 260) | #6B7280 | Muted text |
| Success | oklch(58% 0.14 155) | #0D9B5C | Positive amounts |
| Critical | oklch(52% 0.18 25) | #DC3545 | Negative, errors |

### Why It Works
Mercury targets startup founders who want a "serious bank." The navy + blue system communicates trust and stability while the clean, spacious layout with generous white space signals modernity and premium. The near-white background (#FAFBFD) has the slightest cool blue tint that reinforces the banking metaphor without feeling cold.

---

## 15. Cash App

**Category:** Fintech / Payments
**Signature:** High-contrast green + black — unmistakable brand identity

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Cash Green | oklch(72% 0.24 155) | #00D632 | Brand, money flow |
| Black | oklch(8% 0.01 265) | #0C0C0C | App bg |
| Dark Surface | oklch(14% 0.01 265) | #1A1A1A | Cards |
| White | oklch(100% 0 0) | #FFFFFF | Text on dark |
| Gray | oklch(55% 0.01 265) | #7C7C7C | Secondary text |

### Why It Works
Cash App's palette is brutally simple: green = money, black = premium. The high-chroma green on near-black background creates a "money is flowing" sensation. There are no secondary accents — the entire emotional and informational hierarchy is managed through one green, one white, and shades of gray. This extreme restraint makes the brand instantly recognizable even from across a room.

---

## 16. Supabase

**Category:** Developer Tools / Backend-as-a-Service
**Signature:** Vibrant green with dark developer-focused UI

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Brand Green | oklch(68% 0.20 160) | #3ECF8E | Brand, CTAs |
| Dark BG | oklch(12% 0.02 265) | #1C1C1C | Dashboard bg |
| Surface | oklch(16% 0.02 265) | #232323 | Cards, panels |
| Border | oklch(22% 0.01 265) | #2E2E2E | Dividers |
| Text Primary | oklch(90% 0.01 265) | #EDEDED | Body text |
| Text Secondary | oklch(60% 0.01 265) | #8F8F8F | Muted text |

### Why It Works
Supabase positions itself as the open-source Firebase alternative. The green communicates "go, build, ship" while differentiating from Firebase's orange/yellow. The dark UI signals developer tool while the warm-green (hue 160, leaning teal) feels more sophisticated than a pure green. The high chroma against dark backgrounds creates energy without overwhelming.

---

## 17. Railway

**Category:** Developer Tools / Deployment
**Signature:** Purple-pink gradient with dark, immersive UI

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Brand Purple | oklch(50% 0.22 310) | #9F4AE8 | Brand, CTAs |
| Accent Pink | oklch(60% 0.18 345) | #E84ACA | Gradient end |
| Dark BG | oklch(10% 0.02 290) | #13111C | App bg |
| Surface | oklch(14% 0.02 290) | #1C1929 | Cards |
| Text Primary | oklch(92% 0.01 265) | #E8E8ED | Body text |
| Text Secondary | oklch(58% 0.02 290) | #8A849D | Muted text |

### Why It Works
Railway's purple-to-pink gradient makes deployment feel exciting rather than anxiety-inducing. The slight purple tint in the dark backgrounds maintains brand cohesion even in the darkest areas. This is "developer tool as experience" rather than "developer tool as utility."

---

## 18. Resend

**Category:** Developer Tools / Email
**Signature:** Stark black/white with a single obsessive brand element

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Black | oklch(0% 0 0) | #000000 | Brand, buttons |
| White | oklch(100% 0 0) | #FFFFFF | Background |
| Gray 100 | oklch(96% 0.002 265) | #F4F4F5 | Subtle bg |
| Gray 500 | oklch(58% 0.005 265) | #71717A | Secondary text |
| Gray 900 | oklch(18% 0.003 265) | #18181B | Primary text |

### Why It Works
Resend follows the Vercel school of radical simplicity. Black and white only. The product speaks through its content, not its chrome. This is maximum content-first design — there are no accent colors to distract from the email metrics and logs that users came to see.

---

## 19. Craft

**Category:** Productivity / Documents
**Signature:** Warm, paper-like surfaces with ink-toned accents

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Blue Accent | oklch(55% 0.16 255) | #3081D0 | Links, selected |
| Background | oklch(98% 0.006 75) | #F9F8F6 | Canvas bg |
| Card | oklch(100% 0.002 75) | #FFFFFF | Block bg |
| Text Primary | oklch(20% 0.01 75) | #2C2B28 | Body text |
| Text Secondary | oklch(52% 0.008 75) | #7D7B77 | Muted text |
| Border | oklch(88% 0.006 75) | #E4E3DF | Dividers |

### Why It Works
Craft emulates the warmth of paper and ink. The background (#F9F8F6) has a yellow-brown tint (hue 75) that feels like premium stationery. The text (#2C2B28) is a warm near-black that matches. This warmth differentiates Craft from the clinical blue-gray of most productivity apps (Notion, Google Docs) and positions it as a premium, tactile writing experience.

---

## 20. Arc Browser

**Category:** Browser / Productivity
**Signature:** Gradient-driven, user-customizable color identity

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Default Blue | oklch(55% 0.18 258) | #4285F4 | Default accent |
| Default Red | oklch(58% 0.20 30) | #EA4335 | Second accent |
| Sidebar | oklch(95% 0.005 265) | #EEEEF0 | Sidebar bg |
| Background | oklch(98% 0.003 265) | #FAFAFA | Content bg |
| Text | oklch(18% 0.01 265) | #1F1F1F | Body text |

### Why It Works
Arc's signature move is letting users choose their own gradient. The sidebar color becomes the user's personal expression — their browser, their color. This personalization strategy means Arc has no single brand palette, but every user's Arc is instantly recognizable as theirs. The structural neutrals are intentionally bland to make user-chosen gradients shine.

---

## 21. Raycast

**Category:** Productivity / Launcher
**Signature:** Dark-mode-first with vibrant multi-hue extensions

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Background | oklch(13% 0.01 265) | #1A1A1A | Launcher bg |
| Surface | oklch(17% 0.01 265) | #232323 | Result rows |
| Active | oklch(20% 0.01 265) | #2C2C2C | Selected row |
| Text Primary | oklch(92% 0.01 265) | #EBEBEB | Command text |
| Text Secondary | oklch(58% 0.01 265) | #858585 | Subtitle text |
| Red | oklch(60% 0.20 25) | #FF6363 | Extension accent |
| Purple | oklch(55% 0.20 295) | #B87AFF | Extension accent |
| Blue | oklch(60% 0.18 255) | #56B6FF | Extension accent |
| Green | oklch(62% 0.16 155) | #56D88C | Extension accent |
| Orange | oklch(68% 0.18 65) | #FF9A3E | Extension accent |

### Why It Works
Raycast uses color to differentiate extensions (each has its own accent) while maintaining a consistent dark shell. This means the launcher never competes with the colored extension icons and text — the dark background is a stage for the colorful cast of tools.

---

## 22. Framer

**Category:** Design / Website Builder
**Signature:** Blue-dominant with motion-forward, saturated palette

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Brand Blue | oklch(55% 0.22 260) | #0099FF | Brand, CTAs |
| Dark BG | oklch(8% 0.01 265) | #0D0D0D | Site bg |
| Purple | oklch(52% 0.20 300) | #8855FF | Accent |
| Pink | oklch(60% 0.18 345) | #FF44CC | Accent |
| Surface | oklch(100% 0 0) | #FFFFFF | Content areas |
| Text Primary | oklch(15% 0.01 265) | #171717 | Body text |

### Why It Works
Framer's saturated blue communicates "creative and fast" — it is brighter and more energetic than corporate blues. The secondary purple and pink create a triadic accent system used in gradients that suggest motion and creativity. The near-black backgrounds on the marketing site create dramatic contrast with the vivid accents.

---

## 23. Lemon Squeezy

**Category:** E-commerce / Payments
**Signature:** Yellow-green energy with playful, approachable personality

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Lemon (Yellow) | oklch(88% 0.18 100) | #FFC233 | Brand, highlights |
| Leaf (Green) | oklch(62% 0.16 155) | #2FC06E | CTAs, success |
| Dark | oklch(15% 0.02 265) | #1A1A2E | Dark surfaces |
| Surface | oklch(98% 0.005 95) | #FFFDF5 | Page bg |
| Text | oklch(20% 0.01 265) | #1A1A2E | Body text |

### Why It Works
Lemon Squeezy sells digital products, so the brand needs to feel accessible, fun, and NOT intimidating like Stripe. The yellow communicates optimism and approachability. The warm-tinted surface (#FFFDF5) ties the whole palette together. The green CTA against yellow branding creates a natural visual hierarchy (green = action, yellow = identity).

---

## 24. Cal.com

**Category:** Scheduling / SaaS
**Signature:** Neutral-first with minimal black accent

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Brand (Gray-Black) | oklch(15% 0.01 265) | #111827 | Brand, buttons |
| Background | oklch(98% 0.003 265) | #F9FAFB | Page bg |
| Surface | oklch(100% 0 0) | #FFFFFF | Cards |
| Text Primary | oklch(15% 0.01 265) | #111827 | Body text |
| Text Secondary | oklch(48% 0.005 265) | #6B7280 | Muted text |
| Border | oklch(88% 0.004 265) | #E5E7EB | Dividers |
| Accent | oklch(50% 0.16 265) | #2563EB | Links, selected dates |

### Why It Works
Cal.com is a scheduling tool — the calendar is the product. The achromatic palette ensures that date/time information is the visual priority. The single blue accent highlights selected dates and times, making the most important interaction (choosing a slot) immediately obvious. This is radical simplicity in service of a single user task.

---

## 25. Clerk

**Category:** Developer Tools / Authentication
**Signature:** Purple-dominant with high-trust polish

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Brand Purple | oklch(45% 0.22 285) | #6C47FF | Brand, CTAs |
| Dark Purple | oklch(18% 0.08 285) | #1F0E44 | Dark surfaces |
| Light Purple | oklch(94% 0.04 285) | #F1EDFF | Subtle bg |
| Surface | oklch(99% 0.002 285) | #FAFAFF | Page bg |
| Text Primary | oklch(15% 0.02 285) | #131316 | Body text |
| Text Secondary | oklch(50% 0.01 265) | #6C6C89 | Muted text |

### Why It Works
Clerk handles authentication — the most security-sensitive part of any app. The deep purple communicates trust and premium without the coldness of blue. The purple tint in surfaces and backgrounds creates a cohesive branded experience even in otherwise neutral areas. The dark mode variant uses deep purple-blacks that feel distinctly Clerk, not generic dark.

---

## 26. PlanetScale

**Category:** Developer Tools / Database
**Signature:** Black + neon teal in developer-terminal aesthetic

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Neon Teal | oklch(72% 0.18 190) | #00E5BF | Brand, CTAs |
| Black | oklch(6% 0.01 265) | #0A0A0A | Background |
| Surface | oklch(10% 0.01 265) | #141414 | Cards |
| Text Primary | oklch(95% 0.005 265) | #F0F0F0 | Body text |
| Text Secondary | oklch(55% 0.01 265) | #7A7A7A | Muted text |
| Orange | oklch(70% 0.18 65) | #FF8800 | Warnings |

### Why It Works
PlanetScale's neon teal on black evokes a terminal aesthetic that resonates with database developers. The single vivid accent on dark background creates a striking brand identity with minimal elements. The orange warning color provides clear differentiation from the teal for destructive operations.

---

## 27. Tailwind CSS

**Category:** Developer Tools / CSS Framework
**Signature:** Sky blue with a comprehensive utility-first color system

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Brand Sky | oklch(62% 0.18 230) | #38BDF8 | Brand |
| Brand Blue | oklch(55% 0.20 255) | #3B82F6 | Links |
| Dark | oklch(15% 0.02 240) | #0F172A | Docs bg |
| Surface | oklch(98% 0.003 265) | #F8FAFC | Page bg |
| Text Primary | oklch(15% 0.02 240) | #0F172A | Body text |
| Teal | oklch(60% 0.14 190) | #14B8A6 | Accent |

### Why It Works
Tailwind's color system IS its product — the framework ships 22 color families (slate, gray, zinc, neutral, stone, red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose) each with 11 shades. The sky blue brand color differentiates from the blue of the utility palette. The documentation uses a dark slate (#0F172A) that feels technical without being harsh.

---

## 28. Radix (by WorkOS)

**Category:** Design System / Component Library
**Signature:** Scale-based neutral + accent system with 12 steps per color

### Radix Scale Architecture (12 steps per color)
```
Step 1:  App background
Step 2:  Subtle background
Step 3:  UI element background
Step 4:  Hovered UI element background
Step 5:  Active/selected UI element background
Step 6:  Subtle borders and separators
Step 7:  UI element border and focus rings
Step 8:  Hovered UI element border
Step 9:  Solid backgrounds (buttons, badges)
Step 10: Hovered solid backgrounds
Step 11: Low-contrast text
Step 12: High-contrast text
```

### Why It Works
Radix's innovation is giving each step a SEMANTIC PURPOSE rather than just a lightness value. Step 9 is ALWAYS the solid background (button), Step 12 is ALWAYS high-contrast text. This means you can swap any Radix color (blue, red, green, etc.) and the semantic mapping is preserved. It is the most systematic approach to color scales in any open-source design system.

---

## 29. shadcn/ui

**Category:** Component Library / Design System
**Signature:** CSS custom property architecture with light/dark HSL tokens

### Default Palette (Zinc Neutral)
| Role | CSS Variable | Light | Dark |
|------|-------------|-------|------|
| Background | --background | oklch(100% 0 0) | oklch(9% 0.005 265) |
| Foreground | --foreground | oklch(7% 0.005 265) | oklch(98% 0.003 265) |
| Card | --card | oklch(100% 0 0) | oklch(9% 0.005 265) |
| Primary | --primary | oklch(14% 0.004 265) | oklch(98% 0.003 265) |
| Primary FG | --primary-foreground | oklch(98% 0.003 265) | oklch(14% 0.004 265) |
| Secondary | --secondary | oklch(96% 0.003 265) | oklch(17% 0.005 265) |
| Muted | --muted | oklch(96% 0.003 265) | oklch(17% 0.005 265) |
| Accent | --accent | oklch(96% 0.003 265) | oklch(17% 0.005 265) |
| Destructive | --destructive | oklch(55% 0.22 28) | oklch(60% 0.20 25) |
| Border | --border | oklch(90% 0.004 265) | oklch(17% 0.005 265) |
| Ring | --ring | oklch(14% 0.004 265) | oklch(83% 0.005 265) |

### Why It Works
shadcn/ui pioneered the "copy-paste component" model where the color system lives in your project's CSS, not a dependency. The variable architecture makes theming trivial — swap the HSL values in your global CSS and every component updates. The neutral-by-default approach (zinc gray) means the components work with ANY brand color layered on top.

---

## 30. Pitch

**Category:** Presentation / SaaS
**Signature:** Vibrant multi-color with strong brand purple

### Primary Palette
| Role | oklch | Hex | Usage |
|------|-------|-----|-------|
| Brand Purple | oklch(48% 0.24 295) | #7B3FE4 | Brand, CTAs |
| Coral | oklch(65% 0.18 25) | #FF6B6B | Accents |
| Teal | oklch(60% 0.14 190) | #23C4AD | Success |
| Yellow | oklch(85% 0.16 95) | #FFCB47 | Highlights |
| Dark | oklch(15% 0.02 265) | #1B1B23 | Dark surfaces |
| Surface | oklch(98% 0.003 265) | #F8F8FA | Page bg |

### Why It Works
Pitch competes with Google Slides and Keynote by being MORE colorful. The multi-hue palette signals "creativity and self-expression" while the deep purple primary maintains authority. Each accent color maps to a presentation template category, helping users navigate a large template library through color coding.

---

## Pattern Analysis: What Makes Brand Color Systems Work

### Common Patterns Across All 30 Systems

1. **One dominant hue, restrained secondaries.** Every successful brand system has ONE color that IS the brand. Secondary colors support but never compete.

2. **Neutrals do the heavy lifting.** In every system, 80-90% of the visible interface is neutral (gray, off-white, dark surface). The brand color appears in perhaps 5-10% of the total surface area.

3. **Dark mode is NOT inversion.** No brand in this catalog simply flips light to dark. Each has carefully adjusted chroma, lightness, and sometimes even hue for dark backgrounds.

4. **Warm vs. cool neutrals are intentional.** Notion uses warm (hue 85). Vercel uses cool (hue 265). Linear uses near-neutral (hue 265, near-zero chroma). The neutral temperature sets the emotional tone more than the accent color.

5. **Status colors are universal.** Green = success, red = error, yellow/amber = warning, blue = info. No brand deviates from this convention — it is too deeply learned by users.

6. **Contrast drives hierarchy.** The highest-contrast element on any screen is the most important one. Brand colors are used at full saturation only for the primary action.

7. **Developer tools skew dark.** GitHub, Linear, Raycast, Railway, PlanetScale, Supabase — developer-facing products default to dark mode because their users spend extended hours in the interface.

8. **Consumer products use warmth.** Airbnb, Notion, Craft, Lemon Squeezy — consumer-facing products use warm-tinted neutrals to feel approachable and human.

### The Brand Color Decision Framework

When building a new brand color system, answer these questions:

1. **What emotion must the brand evoke?** (Trust -> blue, Energy -> red/orange, Premium -> purple, Growth -> green)
2. **Dark-first or light-first?** (Developer tools -> dark, Consumer -> light, Both -> design both from day one)
3. **Warm or cool neutrals?** (Approachable -> warm, Professional -> cool, Content-first -> near-zero chroma)
4. **How many accent colors?** (Focused tool -> 1-2, Platform with categories -> 3-5, Design/creative -> rainbow)
5. **What industry norms exist?** (Fintech -> blue/green, Health -> blue/teal, Social -> multicolor)
