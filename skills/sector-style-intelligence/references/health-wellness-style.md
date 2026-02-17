# Health & Wellness — Sector Style Intelligence

## Sector Overview

Health and wellness design encompasses two distinct but overlapping domains with fundamentally different visual philosophies. **Clinical healthcare** — apps for patient portals, telehealth, medical records, and clinical decision-making — demands precision, accessibility, and regulatory awareness. HIPAA considerations influence not just data architecture but visual design: clear hierarchy, unambiguous status indicators, and error prevention are non-negotiable. **Wellness and fitness** — apps for meditation, exercise, nutrition, and mental health — prioritize warmth, motivation, and emotional safety. Users come to these products in vulnerable states, and the visual language must meet them with calm confidence rather than clinical distance.

The best products in this sector understand that health is deeply personal. Design must balance authority (users need to trust the information) with approachability (users must feel safe to engage). A medical portal that feels cold will discourage patients from checking results. A meditation app that feels clinical will fail to create the relaxation it promises. This tension — between competence and warmth — defines every design decision in health and wellness.

---

## Part 1: Clinical Healthcare

### Color Psychology — Healthcare

| Color | Association | Usage | Notes |
|---|---|---|---|
| **Blue** | Trust, calm, clinical competence | Primary brand, navigation | The dominant color in healthcare for good reason |
| **White** | Cleanliness, sterility, clarity | Backgrounds, content areas | Essential — communicates clinical environment |
| **Green** | Health, vitality, positive outcomes | Success states, healthy ranges | Avoid neon greens — use muted, medical greens |
| **Red** | Critical, urgent, abnormal | Alerts, critical values, emergencies | Must be used precisely — overuse causes alarm fatigue |
| **Yellow/Amber** | Caution, attention needed | Warnings, borderline values | Important for tricolor status systems |
| **Teal** | Modern healthcare, wellness-adjacent | Progressive healthcare brands | Bridges clinical and wellness aesthetics |

### Palettes from Leading Healthcare Apps

#### One Medical
```
Primary Blue:       #1A73E8 (Clean medical blue)
Dark Blue:          #0D47A1 (Deep navigation blue)
Light Background:   #FAFBFC (Barely-there gray)
Surface:            #FFFFFF
Text Primary:       #202124 (Near-black)
Text Secondary:     #5F6368 (Medium gray)
Success Green:      #34A853
Warning Yellow:     #FBBC04
Error Red:          #EA4335
Border:             #DADCE0
Accent Teal:        #00897B (Warmth signal)
```

#### Epic MyChart
```
Primary Blue:       #005EB8 (NHS-adjacent trust blue)
Secondary:          #003087 (Deep navy)
Light Background:   #F4F4F4
Surface:            #FFFFFF
Text Primary:       #212121
Status Green:       #2E7D32
Status Red:         #C62828
Status Yellow:      #F57F17
Border:             #E0E0E0
```

#### Zocdoc
```
Primary Green:      #00BFA5 (Teal — modern healthcare)
Dark Background:    #1B2D45
Light Background:   #F8F9FA
Surface:            #FFFFFF
Text Primary:       #1B2D45
Text Secondary:     #6B7C93
CTA Orange:         #FF6B35 (Warmth, action)
Border:             #E1E5EB
Rating Yellow:      #FFB400
```

#### Teladoc
```
Primary Purple:     #6B2D8B (Modern telehealth)
Secondary Teal:     #00A99D
Light Background:   #F5F5F5
Surface:            #FFFFFF
Text Primary:       #333333
Text Secondary:     #666666
CTA Green:          #4CAF50
Border:             #E0E0E0
```

### Typography — Healthcare

| App | Primary Font | Why |
|---|---|---|
| **One Medical** | Google Sans, Roboto | Google ecosystem consistency, excellent readability |
| **Epic MyChart** | System fonts (SF Pro, Roboto) | Performance, familiarity, accessibility |
| **Zocdoc** | Inter, system stack | Modern, clean, excellent at small sizes |
| **Teladoc** | Proxima Nova, system stack | Warm geometric sans, professional |
| **Apple Health** | SF Pro, SF Rounded | Platform-native, accessible, warm |

#### Healthcare Typography Rules

1. **Minimum body text: 16px.** Healthcare users skew older and may have visual impairments. Never go below 16px for body text on mobile.

2. **High contrast ratios are mandatory.** Target 7:1 for body text (WCAG AAA), not just 4.5:1 (AA). Medication names, dosages, and lab values demand maximum readability.

3. **Use weight, not just color, for emphasis.** Color-blind users must be able to distinguish importance. Bold weight + color, not color alone.

4. **Lab values and vitals use tabular figures.** Blood pressure 120/80, glucose 98 mg/dL — these must align cleanly.

```
Display:      36px / 700 weight / -0.01em tracking
Heading 1:    28px / 700 weight / -0.01em tracking
Heading 2:    22px / 600 weight / 0 tracking
Heading 3:    18px / 600 weight / 0 tracking
Body:         16px / 400 weight / 0 tracking
Body Strong:  16px / 600 weight / 0 tracking
Caption:      14px / 400 weight / 0.01em tracking
Label:        12px / 600 weight / 0.05em tracking / uppercase
Vital Value:  32px / 700 weight / tabular-nums
```

### Component Conventions — Healthcare

#### Border Radius
```
Buttons:         8px  (professional, accessible)
Cards:           12px (soft but not playful)
Input Fields:    8px  (clear, defined boundaries)
Modals:          16px
Status Badges:   4px  (compact, clinical precision)
Avatar/Photos:   50%  (circular)
Alert Banners:   8px  (structured, not decorative)
```

#### Status Indicators (Critical Pattern)

Healthcare apps need a robust, colorblind-safe status system:

```css
/* Normal / Healthy */
.status-normal {
  background: #E8F5E9;
  color: #2E7D32;
  border-left: 4px solid #4CAF50;
  /* Icon: checkmark circle */
}

/* Attention / Borderline */
.status-attention {
  background: #FFF8E1;
  color: #F57F17;
  border-left: 4px solid #FFC107;
  /* Icon: warning triangle */
}

/* Critical / Abnormal */
.status-critical {
  background: #FFEBEE;
  color: #C62828;
  border-left: 4px solid #EF5765;
  /* Icon: alert circle */
}

/* Pending / Unknown */
.status-pending {
  background: #F5F5F5;
  color: #616161;
  border-left: 4px solid #9E9E9E;
  /* Icon: clock */
}
```

**Key:** Always combine color + icon + text label. Never rely on color alone for health status.

#### Appointment Card
```css
.appointment-card {
  background: #FFFFFF;
  border: 1px solid #E1E5EB;
  border-radius: 12px;
  padding: 20px;
  display: flex;
  gap: 16px;
}
.appointment-card .provider-avatar {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  object-fit: cover;
}
.appointment-card .provider-name {
  font-size: 16px;
  font-weight: 600;
  color: #1B2D45;
}
.appointment-card .appointment-type {
  font-size: 14px;
  color: #6B7C93;
}
.appointment-card .appointment-time {
  font-size: 14px;
  font-weight: 600;
  color: #1A73E8;
}
```

### Spacing — Healthcare

Healthcare apps use generous spacing to reduce cognitive load during health-related decision-making.

```
4px   — Micro (icon internal padding)
8px   — Tight (related inline elements)
12px  — Compact (label-to-field, within tight groups)
16px  — Default (between form fields, list items)
20px  — Card padding (standard content container)
24px  — Section gap (between content sections)
32px  — Major sections
40px  — Page sections
56px  — Major page divisions
```

**Key principle:** Healthcare spacing errs toward generous. When in doubt, add more breathing room. Users processing health information need cognitive space.

### Trust Signals — Healthcare

1. **Provider credentials displayed prominently.** "Dr. Sarah Chen, MD, Board Certified Internal Medicine" — credentials build trust in healthcare contexts.
2. **HIPAA compliance indicators.** "Your data is protected by HIPAA" badges, lock icons near PHI.
3. **Clinical data sourcing.** "Source: UpToDate, reviewed January 2026" for health information.
4. **Verified review badges.** "Verified Patient" on provider reviews.
5. **Clear data sharing controls.** Users must feel in control of who sees their health data.
6. **Accessibility compliance.** Healthcare apps that fail WCAG AA face legal liability and user harm. Compliance is both ethical and a trust signal.
7. **Emergency fallbacks.** "If this is an emergency, call 911" must be consistently present. Its absence is a trust violation.

### Anti-Patterns — Healthcare

1. **Burying lab results behind excessive navigation.** Users checking lab results are anxious — don't make them hunt through 5 screens.
2. **Using red for all alerts.** If everything is red, nothing is urgent. Reserve red for genuinely critical values.
3. **Gamifying health metrics irresponsibly.** Step streaks are fine; gamifying medication adherence with leaderboards trivializes serious health management.
4. **Tiny text for dosage information.** Medication names and dosages in 11px text is a patient safety risk.
5. **Missing offline access for critical information.** Insurance cards, medication lists, and emergency contacts must work offline.
6. **Generic stock photography of diverse smiling people.** Healthcare imagery should feel authentic, not corporate. Illustration often works better than stock photos.
7. **Non-accessible color palettes.** Low-contrast text in healthcare apps isn't just a design flaw — it's a potential harm vector.

---

## Part 2: Wellness & Fitness

### Color Psychology — Wellness

| Color | Association | Usage | Notes |
|---|---|---|---|
| **Soft Blue** | Calm, serenity, sky | Meditation, sleep, breathing | Desaturated blues, not corporate blues |
| **Warm Peach/Coral** | Warmth, self-care, gentle energy | Accents, illustrations, progress | Organic, human warmth |
| **Sage Green** | Nature, growth, healing | Backgrounds, secondary surfaces | Muted, botanical greens |
| **Lavender** | Relaxation, mindfulness | Sleep features, evening modes | Soft purples, never saturated |
| **Sand/Cream** | Organic, natural, grounded | Backgrounds, surfaces | Warmth without energy |
| **Terracotta** | Earthy, grounded, physical | Fitness, movement | Energetic but natural |
| **Deep Navy** | Night, sleep, depth | Dark mode, sleep features | Warmer than pure black |

### Palettes from Leading Wellness Apps

#### Headspace
```
Primary Orange:     #F47D31 (Warm, approachable, distinctive)
Secondary Orange:   #FF8C4C
Dark Background:    #2B2244 (Warm dark purple — sleep mode)
Blue Sky:           #64B5F6 (Calm, optimism)
Yellow:             #FDD835 (Joy, energy)
Coral:              #EF7C8E (Warmth, self-care)
Text on Dark:       #FFFFFF
Text on Light:      #2B2244
Surface Light:      #FFF8F0 (Warm off-white)
Surface Medium:     #F0E7DB (Warm sand)
```
**Why it works:** Headspace's palette is deliberately warm and organic — no corporate blues, no clinical whites. The warm orange CTA feels inviting rather than demanding. The dark purple (not black) night mode maintains emotional warmth.

#### Calm
```
Primary Blue:       #5B86E5 (Sky blue — serenity)
Dark Background:    #1A1A2E (Deep night blue)
Gradient Start:     #36D1DC (Teal)
Gradient End:       #5B86E5 (Blue)
Nature Green:       #7BC67E (Soft, botanical)
Gold Premium:       #D4AF37 (Premium tier)
Surface Light:      #F5F7FA
Text Primary:       #1A1A2E
Text Secondary:     #6B7280
Sleep Purple:       #7C3AED
```
**Why it works:** Calm's palette evokes sky and water — primal calm associations. The blue-teal gradient is both distinctive and physiologically calming.

#### Apple Health
```
Activity Red:       #FA4C52 (Move ring)
Activity Green:     #92E544 (Exercise ring)
Activity Blue:      #00CFF8 (Stand ring)
Heart Red:          #FF2D55
Mindfulness Teal:   #64D2FF
Sleep Purple:       #BF5AF2
Respiratory Blue:   #30D158
Background:         #000000 (Dark mode default)
Surface Card:       #1C1C1E (Elevated dark)
Text Primary:       #FFFFFF
Text Secondary:     #8E8E93
```
**Why it works:** Apple Health uses vibrant, saturated colors for data categories while maintaining a dark, calm canvas. Each health category has a distinct, memorable color.

#### Peloton
```
Primary Red:        #D0021B (Energy, motivation, urgency)
Dark Background:    #181818 (Near black — immersive)
Surface Card:       #242424
White:              #FFFFFF
Text Secondary:     #A0A0A0
Metric Blue:        #5AC8FA (Performance data)
Leaderboard Gold:   #FFD700
Progress Green:     #4CD964
```
**Why it works:** Peloton's palette channels the energy of a live studio class — dark and immersive with intense red accents. The darkness keeps focus on content (instructor video) while metrics pop against the dark canvas.

#### MyFitnessPal
```
Primary Blue:       #0073E6 (Trust, systematic tracking)
Secondary Green:    #00C853 (Positive progress)
Warning Orange:     #FF9800 (Over target)
Error Red:          #F44336 (Significantly over target)
Surface:            #FFFFFF
Background:         #F5F5F5
Text Primary:       #212121
Text Secondary:     #757575
Border:             #E0E0E0
Calorie Green:      #4CAF50 (Under target — positive)
```

### Typography — Wellness

| App | Primary Font | Why |
|---|---|---|
| **Headspace** | Brandon Grotesque, custom | Friendly geometric sans — warm, approachable, slightly rounded |
| **Calm** | DIN Next, system stack | Clean, balanced, excellent readability |
| **Apple Health** | SF Pro, SF Rounded | SF Rounded adds warmth to the Apple ecosystem |
| **Peloton** | Proxima Nova, custom display | Strong, confident, athletic |
| **MyFitnessPal** | Roboto, system stack | Clean, functional, systematic |
| **Strava** | National 2 (custom), system | Athletic, editorial, confident |

#### Wellness Typography Rules

1. **Use rounded or humanist fonts.** Geometric sans-serifs with slight rounding (Brandon Grotesque, Nunito, SF Rounded) feel warmer than industrial geometrics (Helvetica, Roboto).

2. **Larger display sizes for motivational content.** "Great job!" at 36px hits differently than at 16px. Celebration moments deserve large, bold typography.

3. **Generous line height for readability during exercise.** Users reading during workouts need at least 1.6 line height. Phone-at-arm's-length viewing demands larger text.

```
Display:      40px / 700 weight / -0.02em tracking (motivational)
Heading 1:    28px / 700 weight / -0.01em tracking
Heading 2:    22px / 600 weight / 0 tracking
Heading 3:    18px / 600 weight / 0 tracking
Body:         16px / 400 weight / 0.01em tracking
Body Small:   14px / 400 weight / 0.01em tracking
Timer:        64px / 700 weight / tabular-nums / monospace
Metric:       32px / 700 weight / tabular-nums
Metric Label: 12px / 600 weight / 0.06em tracking / uppercase
```

### Component Conventions — Wellness

#### Border Radius
```
Buttons:           20px (pill-shaped or heavily rounded — approachable)
Cards:             16px (soft, organic feel)
Input Fields:      12px (softer than clinical)
Progress Rings:    50% (circular)
Avatars:           50% (circular)
Illustrations:     24px (large radius for warmth)
Bottom Sheets:     24px top corners
Chips/Tags:        20px (pill-shaped)
```

**Key difference from fintech:** Wellness uses significantly larger border radii. Rounded shapes feel safer, softer, and more organic.

#### Progress Ring (Key Wellness Pattern)

```css
.progress-ring {
  width: 200px;
  height: 200px;
  position: relative;
}
.progress-ring svg circle {
  fill: none;
  stroke-width: 12;
  stroke-linecap: round;
  transform: rotate(-90deg);
  transform-origin: center;
}
.progress-ring .track {
  stroke: #E8E8E8;
}
.progress-ring .progress {
  stroke: #FA4C52;
  stroke-dasharray: 565.48; /* 2 * PI * 90 */
  stroke-dashoffset: 141.37; /* 75% complete */
  transition: stroke-dashoffset 0.6s cubic-bezier(0.34, 1.56, 0.64, 1.0);
}
.progress-ring .value {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 48px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}
```

#### Meditation Session Card
```css
.session-card {
  background: linear-gradient(135deg, #2B2244 0%, #3D2E5C 100%);
  border-radius: 16px;
  padding: 24px;
  color: #FFFFFF;
  position: relative;
  overflow: hidden;
}
.session-card .illustration {
  position: absolute;
  right: -20px;
  bottom: -20px;
  width: 140px;
  height: 140px;
  opacity: 0.6;
}
.session-card .duration {
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 8px;
}
.session-card .title {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 4px;
}
.session-card .description {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.5;
}
```

#### Workout Metric Display
```css
.metric-cluster {
  display: flex;
  gap: 24px;
  padding: 20px;
  background: #1C1C1E;
  border-radius: 16px;
}
.metric-item {
  flex: 1;
  text-align: center;
}
.metric-item .value {
  font-size: 32px;
  font-weight: 700;
  color: #FFFFFF;
  font-variant-numeric: tabular-nums;
}
.metric-item .unit {
  font-size: 14px;
  font-weight: 500;
  color: #8E8E93;
  margin-left: 2px;
}
.metric-item .label {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #8E8E93;
  margin-top: 4px;
}
```

### Spacing — Wellness

Wellness apps use generous, breathing spacing. Whitespace itself is a design element that communicates calm.

```
4px   — Micro
8px   — Tight (within metric clusters)
12px  — Compact
16px  — Default
24px  — Standard card padding
32px  — Section gap
40px  — Major sections (breathing room)
56px  — Page sections
72px  — Major page divisions (generous calm)
```

**Key principle:** Wellness spacing is 20-30% more generous than fintech. The breathing room is intentional — it physiologically calms users.

### Motion — Wellness

Wellness motion is **slow, organic, and soothing.** Animations communicate calm and progress rather than efficiency.

#### Timing
```
Micro-interaction:    200-300ms  (button tap, checkbox)
State transition:     400-500ms  (card expand, screen change)
Page transition:      500-600ms  (navigation, significant state change)
Breathing animation:  4000-6000ms per cycle (inhale-hold-exhale)
Progress celebration: 800-1200ms (achievement unlocked)
Ring fill:            600-800ms  (progress ring completing)
```

#### Easing Curves
```css
/* Gentle ease — most interactions */
transition-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1.0);

/* Organic decelerate — entering elements, feels natural */
transition-timing-function: cubic-bezier(0.0, 0.0, 0.15, 1.0);

/* Spring bounce — celebrations, achievement moments */
transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1.0);

/* Breathing — smooth, continuous, soothing */
transition-timing-function: cubic-bezier(0.37, 0.0, 0.63, 1.0);

/* Fade — gentle opacity transitions */
transition-timing-function: ease-in-out;
```

#### Specific Patterns

- **Breathing circle:** Inhale 4s (scale 1.0 -> 1.3, ease-in-out), hold 4s, exhale 4s (scale 1.3 -> 1.0, ease-in-out). Continuous loop.
- **Progress ring fill:** Animate `stroke-dashoffset` over 600ms with spring easing. Add subtle scale pulse at completion (1.0 -> 1.05 -> 1.0, 400ms).
- **Session start:** Content fades in with 500ms ease, background gradient slowly shifts hue over 30s (almost imperceptible drift).
- **Achievement celebration:** Subtle confetti (not stock-market style), particle count 20-30, fall duration 1.5s with gentle gravity. Or: expanding ring of light, 800ms.
- **Heart rate visualization:** Continuous sinusoidal animation synced to BPM data, stroke-dashoffset animation.

### Trust Signals — Wellness

1. **Clinical advisors credited.** "Content reviewed by Dr. [Name], clinical psychologist." Wellness apps that claim health benefits must cite clinical authority.
2. **Research citations.** "Based on 47 peer-reviewed studies on mindfulness-based stress reduction."
3. **Privacy emphasis.** "Your meditation history is private by default." Health and wellness data is deeply personal.
4. **No social comparison by default.** Opt-in leaderboards, not default. Comparing health progress can be harmful.
5. **Crisis resources.** Mental health apps must include crisis hotline information (988 Suicide & Crisis Lifeline). Its absence is a liability.
6. **Progress without judgment.** "You meditated 3 times this week" not "You only meditated 3 times." Language matters enormously in wellness.
7. **Inclusive imagery.** Diverse body types, abilities, ages in illustrations and photography. Wellness is for everyone.

### Anti-Patterns — Wellness

1. **Guilt-tripping missed sessions.** "You broke your streak!" creates anxiety, not motivation. Reframe: "Welcome back. Pick up where you left off."
2. **Aggressive push notifications.** "You haven't meditated today!" at 10 PM is counterproductive. Wellness apps should offer gentle, opt-in reminders.
3. **Weight-centric metrics as primary display.** Leading with weight promotes unhealthy relationships with body metrics. Lead with activity, energy, mood.
4. **High-contrast jarring colors in sleep/meditation.** Bright white screens at bedtime or during meditation break the calming experience. Use dark mode defaults for sleep features.
5. **Competitive leaderboards by default.** Social competition in fitness can be motivating for some and harmful for others. Always opt-in.
6. **Ignoring accessibility in fitness.** Workout apps that assume full mobility exclude wheelchair users, people with chronic pain, and many others.
7. **Paywalling crisis resources.** If your app surfaces mental health content, crisis resources must always be free and accessible.

---

## Reference Apps — What to Learn from Each

### Headspace
- **Lesson:** Illustration can be a primary design language. Headspace's custom illustration style (by studio Shantell Martin, Andy Puddicombe era; later expanded) creates an instantly recognizable brand that feels warm, accessible, and non-threatening.
- **Key pattern:** Illustration-first cards, themed sessions with distinct color palettes, animated breathing guides.
- **Tone:** Friendly without being juvenile. The visual style says "meditation is approachable" without saying "meditation is trivial."

### Calm
- **Lesson:** Nature imagery as a design system. Calm uses full-screen nature photography and soundscapes as both aesthetic and functional elements. Study how environmental design creates mood.
- **Key pattern:** Full-screen background scenes with minimal UI overlay, audio-first design, bedtime stories as a feature category.
- **Night mode:** Calm's dark mode is particularly well-designed — warm purples and deep blues that feel like nighttime, not like a darkened office.

### One Medical
- **Lesson:** Healthcare can feel modern and approachable without sacrificing clinical credibility. Study how One Medical's clean, minimal interface reduces the anxiety of interacting with healthcare systems.
- **Key pattern:** Provider-centric design (real photos, credentials visible), streamlined booking flow (3 steps), integrated messaging that feels like consumer chat.

### Apple Health
- **Lesson:** Data density with category-specific color coding. Apple Health displays enormous amounts of health data through a consistent pattern: category color + metric value + trend chart. Study the card-based summary dashboard.
- **Key pattern:** Summary dashboard with scrollable metric cards, each category has a distinct color, trend sparklines provide context without detail, drill-down to daily/weekly/monthly/yearly views.

### MyFitnessPal
- **Lesson:** Tracking UX as a design problem. MyFitnessPal makes logging calories fast through barcode scanning, meal copying, and frequent-food suggestions. Study how they reduce friction in repetitive data entry.
- **Key pattern:** Pie chart macro breakdown, daily goal progress bar, meal-based organization (breakfast/lunch/dinner/snacks), barcode scanner integration.

### Peloton
- **Lesson:** Live experience design for at-home fitness. Study how Peloton translates the energy of a group fitness class into a solitary home experience through instructor presence, leaderboard, and performance metrics overlay.
- **Key pattern:** Full-screen instructor video with minimal metric overlay, heart rate zones with color coding, post-workout summary with personal records highlighted, social high-fives.

---

## W3C Design Token Starter Kit — Health & Wellness

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "health-wellness": {
    "color": {
      "healthcare": {
        "primary": {
          "$value": "#1A73E8",
          "$type": "color",
          "$description": "Clinical trust blue"
        },
        "primary-hover": { "$value": "#1565C0", "$type": "color" },
        "surface-primary": { "$value": "#FFFFFF", "$type": "color" },
        "surface-secondary": { "$value": "#FAFBFC", "$type": "color" },
        "text-primary": { "$value": "#202124", "$type": "color" },
        "text-secondary": { "$value": "#5F6368", "$type": "color" },
        "border": { "$value": "#DADCE0", "$type": "color" },
        "status-normal": { "$value": "#34A853", "$type": "color" },
        "status-normal-bg": { "$value": "#E8F5E9", "$type": "color" },
        "status-attention": { "$value": "#F57F17", "$type": "color" },
        "status-attention-bg": { "$value": "#FFF8E1", "$type": "color" },
        "status-critical": { "$value": "#EA4335", "$type": "color" },
        "status-critical-bg": { "$value": "#FFEBEE", "$type": "color" },
        "status-pending": { "$value": "#9E9E9E", "$type": "color" },
        "status-pending-bg": { "$value": "#F5F5F5", "$type": "color" }
      },
      "wellness": {
        "primary": {
          "$value": "#F47D31",
          "$type": "color",
          "$description": "Warm, approachable orange"
        },
        "primary-hover": { "$value": "#E06B20", "$type": "color" },
        "surface-light": {
          "$value": "#FFF8F0",
          "$type": "color",
          "$description": "Warm off-white"
        },
        "surface-sand": { "$value": "#F0E7DB", "$type": "color" },
        "surface-dark": {
          "$value": "#2B2244",
          "$type": "color",
          "$description": "Warm dark purple for night mode"
        },
        "text-on-dark": { "$value": "#FFFFFF", "$type": "color" },
        "text-on-light": { "$value": "#2B2244", "$type": "color" },
        "accent-blue": { "$value": "#64B5F6", "$type": "color" },
        "accent-coral": { "$value": "#EF7C8E", "$type": "color" },
        "accent-sage": { "$value": "#A8C5A0", "$type": "color" },
        "accent-lavender": { "$value": "#B39DDB", "$type": "color" },
        "accent-terracotta": { "$value": "#C17952", "$type": "color" }
      },
      "fitness": {
        "activity-move": {
          "$value": "#FA4C52",
          "$type": "color",
          "$description": "Apple Health-inspired move ring"
        },
        "activity-exercise": { "$value": "#92E544", "$type": "color" },
        "activity-stand": { "$value": "#00CFF8", "$type": "color" },
        "heart-rate": { "$value": "#FF2D55", "$type": "color" },
        "surface-dark": { "$value": "#1C1C1E", "$type": "color" },
        "surface-elevated": { "$value": "#2C2C2E", "$type": "color" }
      }
    },
    "typography": {
      "font-family-wellness": {
        "$value": "'Brandon Grotesque', 'Nunito', 'SF Pro Rounded', -apple-system, sans-serif",
        "$type": "fontFamily",
        "$description": "Warm, rounded fonts for wellness"
      },
      "font-family-healthcare": {
        "$value": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "$type": "fontFamily",
        "$description": "Clean, accessible fonts for healthcare"
      },
      "font-size-timer": { "$value": "64px", "$type": "dimension" },
      "font-size-metric": { "$value": "32px", "$type": "dimension" },
      "font-size-display": { "$value": "40px", "$type": "dimension" },
      "font-size-h1": { "$value": "28px", "$type": "dimension" },
      "font-size-h2": { "$value": "22px", "$type": "dimension" },
      "font-size-h3": { "$value": "18px", "$type": "dimension" },
      "font-size-body": { "$value": "16px", "$type": "dimension" },
      "font-size-caption": { "$value": "14px", "$type": "dimension" },
      "font-size-label": { "$value": "12px", "$type": "dimension" }
    },
    "spacing": {
      "micro": { "$value": "4px", "$type": "dimension" },
      "tight": { "$value": "8px", "$type": "dimension" },
      "compact": { "$value": "12px", "$type": "dimension" },
      "default": { "$value": "16px", "$type": "dimension" },
      "comfortable": { "$value": "24px", "$type": "dimension" },
      "spacious": { "$value": "32px", "$type": "dimension" },
      "breathing": { "$value": "40px", "$type": "dimension" },
      "section": { "$value": "56px", "$type": "dimension" },
      "page": { "$value": "72px", "$type": "dimension" }
    },
    "radius": {
      "small": { "$value": "8px", "$type": "dimension" },
      "medium": { "$value": "12px", "$type": "dimension" },
      "large": { "$value": "16px", "$type": "dimension" },
      "pill": { "$value": "20px", "$type": "dimension" },
      "xlarge": { "$value": "24px", "$type": "dimension" },
      "full": { "$value": "9999px", "$type": "dimension" }
    },
    "motion": {
      "duration-micro": { "$value": "200ms", "$type": "duration" },
      "duration-normal": { "$value": "400ms", "$type": "duration" },
      "duration-slow": { "$value": "600ms", "$type": "duration" },
      "duration-breathing": { "$value": "4000ms", "$type": "duration" },
      "duration-celebration": { "$value": "1000ms", "$type": "duration" },
      "easing-gentle": {
        "$value": "cubic-bezier(0.25, 0.1, 0.25, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-organic": {
        "$value": "cubic-bezier(0.0, 0.0, 0.15, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-breathing": {
        "$value": "cubic-bezier(0.37, 0.0, 0.63, 1.0)",
        "$type": "cubicBezier"
      },
      "easing-spring": {
        "$value": "cubic-bezier(0.34, 1.56, 0.64, 1.0)",
        "$type": "cubicBezier"
      }
    }
  }
}
```

---

## Inspiration Links

### Mobbin
- [Health & Fitness apps](https://mobbin.com/browse/apps?category=health-fitness) — Browse full app flows
- [Meditation app screens](https://mobbin.com/browse/screens?category=health-fitness&tag=meditation)
- [Workout tracking flows](https://mobbin.com/browse/flows?category=health-fitness&flow=tracking)

### Screenlane
- [Healthcare app UI](https://screenlane.com/screens/category/health/) — Clinical interfaces, patient portals
- [Fitness app UI](https://screenlane.com/screens/category/fitness/) — Workout tracking, progress displays

### Additional Resources
- [Apple Health Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/health) — HealthKit design patterns
- [Headspace design blog](https://www.headspace.com/blog) — Wellness content design approach
- [Calm design](https://www.calm.com) — Study the product directly

---

## Quick Decision Framework — Health & Wellness

1. **Is this a clinical or wellness context?** Clinical: prioritize precision, accessibility, unambiguous status. Wellness: prioritize warmth, motivation, emotional safety.

2. **What emotional state is the user in?** Anxious (lab results): be calm, clear, provide context. Motivated (starting workout): match energy, be encouraging. Vulnerable (mental health): be gentle, non-judgmental.

3. **Is this real-time or reflective?** Real-time (during workout): minimal UI, large metrics, glanceable. Reflective (reviewing progress): richer data, trends, insights.

4. **What time of day is primary usage?** Morning (workout planning): bright, energetic. Evening (meditation, sleep): dark, warm, calming. Auto-adapt with time-based theming.

5. **Does this involve clinical data?** If yes: treat as healthcare regardless of context. Lab values, medications, diagnoses require clinical precision even in a consumer wellness app.
