---
description: Sector-specific style direction generator — generate a complete visual identity direction with color, typography, motion, tone, tokens, and reference apps for any product sector.
---

# Taste — Sector-Specific Style Direction Generator

The flagship command. Given a product sector, generate a complete, opinionated visual style direction that captures the taste and conventions of the best apps in that category. This is not a generic style guide — it is a sector-aware design direction grounded in what works.

## Supported Sectors

| Sector | Key Characteristics |
|--------|-------------------|
| Fintech / Banking | Trust, precision, security, clean data display |
| Healthcare / Medical | Clinical trust, calm, HIPAA-aware information hierarchy |
| Wellness / Fitness | Energy, motivation, progress visualization, body-positive |
| Social Media | Expression, engagement, content-first, identity |
| Creator Tools | Creative expression, canvas-centric, pro-grade, flexible |
| Messaging | Speed, intimacy, presence, conversation-first |
| SaaS / Productivity | Efficiency, density, keyboard-first, professional |
| Enterprise / B2B | Data density, role-based, workflow-oriented, serious |
| Developer Tools | Monospace, dark-native, information-dense, power-user |
| E-commerce | Product-first, conversion-optimized, trust signals |
| Marketplace | Two-sided trust, discovery, comparison, social proof |
| Food & Delivery | Appetite appeal, urgency, real-time tracking, local |
| Travel & Hospitality | Aspiration, immersive imagery, booking confidence |
| Education / EdTech | Progression, encouragement, clarity, engagement |
| Gaming | Immersion, achievement, community, spectacle |
| Media / Entertainment | Content immersion, discovery, binge-friendly |
| Music / Audio | Mood, waveform aesthetics, playback-centric |
| Sports | Energy, real-time data, team identity, competition |
| Real Estate | Aspiration, space visualization, trust, locality |
| Automotive | Premium, configurator patterns, performance, safety |
| Legal / Compliance | Authority, document-centric, precision, gravity |
| Non-Profit | Impact storytelling, donation conversion, transparency |

## Style Direction Protocol

1. **Accept sector and modifiers**: Determine the style direction parameters.
   - **Sector**: One of the supported sectors above
   - **Sub-niche** (optional): e.g., "Fintech" can be neobank, investment, crypto, insurance
   - **Mood modifier** (optional): Premium, playful, minimal, bold, warm, clinical
   - **Platform**: Mobile-first, desktop-first, or responsive
   - **Audience age range** (optional): Gen Z, Millennial, Gen X, Boomer, universal

2. **Generate color direction**:
   - **Primary color**: Hex, OKLCH value, and sector rationale for why this hue works
   - **Secondary color**: Complementary or analogous, with relationship explanation
   - **Accent color**: For CTAs, highlights, and interactive elements
   - **Neutral palette**: Background, surface, border, and text colors (4-6 steps)
   - **Semantic colors**: Success, warning, error, info with sector-appropriate tones
   - **Dark mode variant**: Complete remapped palette, not just inverted
   - **Accessible pairings**: Every foreground/background combination verified for WCAG AA (4.5:1 text, 3:1 UI)
   - **Sector rationale**: Why these specific colors communicate trust/energy/creativity in this sector

3. **Generate typography direction**:
   - **Primary typeface**: Specific font recommendation (e.g., "Inter" not "sans-serif") with reasoning
   - **Secondary typeface** (if needed): For display, editorial, or data contexts
   - **Monospace** (if relevant): For code, data, or financial figures
   - **Type scale**: Base size, scale ratio, and computed sizes from caption to display
   - **Weight usage**: Which weights for which contexts (headings, body, captions, UI labels)
   - **Line heights**: Tight (headings), comfortable (body), generous (long-form)
   - **Letter spacing**: Adjustments for uppercase labels, large display text, small captions
   - **Why this pairing**: Explain the personality the fonts communicate together

4. **Generate spacing and density direction**:
   - **Density level**: Tight (data-heavy, enterprise), Balanced (most apps), Airy (consumer, content)
   - **Base unit**: 4px or 8px grid with reasoning
   - **Spacing scale**: Defined steps from the base unit (e.g., 4, 8, 12, 16, 24, 32, 48, 64)
   - **Component padding conventions**: Cards, buttons, inputs, modals, sections
   - **Information density benchmark**: How much content per viewport is appropriate for this sector

5. **Generate component personality**:
   - **Border radius**: Sharp (0-2px = professional), Medium (6-8px = balanced), Rounded (12-16px = friendly), Pill (9999px = playful) with sector reasoning
   - **Elevation style**: Flat, subtle shadow, layered shadow, or glassmorphism — with reasoning
   - **Button hierarchy**: Primary, secondary, tertiary, ghost, destructive — visual treatment for each
   - **Card treatment**: Border vs. shadow vs. filled, hover behavior, content padding
   - **Input style**: Outlined, filled, underlined — with label position (floating, stacked, inline)
   - **Icon style**: Outlined, filled, duotone, or mixed — weight and size conventions
   - **Divider and separator style**: Lines, spacing, color blocks, or none

6. **Generate motion language**:
   - **Animation personality**: Clinical (minimal, functional), Smooth (polished, fluid), Bouncy (playful, spring-based), Dramatic (cinematic, attention-grabbing)
   - **Easing curves**: Specific cubic-bezier values for enter, exit, and move transitions
   - **Duration ranges**: Micro (50-100ms), Short (150-250ms), Medium (300-500ms), Long (500ms+) with when to use each
   - **Signature interaction**: One defining motion that gives the product character
   - **Reduced motion fallback**: What every animation degrades to for `prefers-reduced-motion`
   - **Spring parameters** (if bouncy): Tension, friction, and mass values

7. **Generate tone of voice direction**:
   - **Formality level**: Formal, Professional-casual, Casual, Playful — with sector reasoning
   - **Personality traits**: 3-4 adjective descriptors (e.g., "Confident, Clear, Warm, Never condescending")
   - **Microcopy examples**:
     - CTA buttons (primary and secondary actions)
     - Error messages (validation, server, permission)
     - Empty states (first use, no results, no content)
     - Success messages (completion, achievement, confirmation)
     - Loading messages (if shown)
     - Tooltip and helper text
   - **Words to use and avoid**: Sector-specific language guidance

8. **Identify reference apps**: 5 best-in-class apps in the sector.
   - **App name and platform**
   - **What to study**: The specific design decision or pattern to learn from
   - **Key takeaway**: One sentence on what makes this app best-in-class in its area
   - **Where they could improve**: Even the best have gaps — this builds critical thinking

9. **Generate sector-specific do's and don'ts**:
   - **5 Must-have patterns**: Things users expect in this sector that you must get right
   - **5 Pitfalls to avoid**: Common mistakes that plague apps in this sector
   - Each with a concrete example and explanation

10. **Compile inspiration sources**: Curated links and search terms for ongoing reference.
    - **Mobbin**: Specific category and filter terms to find relevant screens
    - **Screenlane**: Relevant flow categories
    - **Refero**: Search terms and collections
    - **Nicelydone**: Applicable categories
    - **Dribbble/Behance**: Search terms that yield quality results, not noise
    - **Real product teardown sources**: Newsletters, YouTube channels, blogs for this sector

11. **Generate design token starter kit**: Complete W3C Design Tokens format JSON.
    - Color tokens (primitive and semantic layers)
    - Typography tokens (family, size, weight, line-height, letter-spacing)
    - Spacing tokens (scale)
    - Border radius tokens
    - Elevation/shadow tokens
    - Motion/duration tokens
    - Breakpoint tokens
    - All tokens include `$description` and `$type` fields per W3C spec

## Output Format

```
## Taste Direction: [Sector] — [Sub-niche if specified]

### Direction Summary
[2-3 sentences capturing the overall visual personality and why it works for this sector]

### Color Direction
[Full palette with hex, OKLCH, rationale, dark mode, accessible pairings]

### Typography Direction
[Font pairing, scale, weights, line heights, reasoning]

### Spacing & Density
[Base unit, scale, density level, component conventions]

### Component Personality
[Border radius, elevation, buttons, cards, inputs, icons — with reasoning]

### Motion Language
[Personality, easing, durations, signature interaction, reduced motion]

### Tone of Voice
[Formality, traits, microcopy examples across all contexts]

### Reference Apps
| App | Platform | Study This | Key Takeaway |
|-----|----------|------------|--------------|
[5 rows with specific, actionable observations]

### Do's and Don'ts
#### Must-Have Patterns
[5 patterns with examples]
#### Pitfalls to Avoid
[5 anti-patterns with examples]

### Inspiration Sources
[Curated links and search terms per platform]

### Design Token Starter Kit (W3C Format)
[Complete JSON token file]
```

## Cross-References
When generating style directions, draw sector knowledge and design system patterns from:
- `ui-visual-design-system` skill for color theory, typography scales, visual hierarchy, and design principles
- `design-systems-architecture` skill for token architecture, naming conventions, and multi-platform token strategy
- `interaction-motion-design` skill for animation curves, spring physics, duration guidelines, and platform motion conventions
- `mobile-ux-design` skill for iOS 26 Liquid Glass and Material 3 sector adaptations
- `desktop-app-design` skill for industry vertical patterns and desktop-specific density considerations
- `cross-cultural-i18n-ux` skill for culturally appropriate color and typography choices
- `ux-ethics-content-strategy` skill for tone of voice guidelines and ethical design patterns

## Next Steps
After running `/taste`, consider:
- `/inspo` — Find screen patterns and references for the sector
- `/drip` — Expand the token starter kit into a full design token system
- `/ship` — Start building components using the style direction
- `/onboard` — Build a sector-appropriate onboarding flow
- `/benchmark` — Compare against the reference apps identified
- `/vibe-check` — Audit screens built with this direction against heuristics
