# Visual Scoring Framework

> 10-dimension visual quality scoring system calibrated to Awwwards, Red Dot, and iF Design Award standards.

---

## Scoring Dimensions

### Dimension 1: Typography (Weight: 15%)

**Rubric**:
- **1-2 (Broken)**: System default fonts unstyled. No hierarchy. Single size/weight for everything. Browser-default line-height. No consideration for readability.
- **3-4 (Amateur)**: A custom font is loaded but used without a system. Random sizes. Inconsistent weights. Line-height too tight or too loose. No type scale.
- **5-6 (Functional)**: Clear hierarchy with 3+ levels. Consistent font stack. Reasonable line-height. Some type scale logic. Works but doesn't impress.
- **7-8 (Professional)**: Mathematical type scale. Proper line-height per level. Tracking adjustments for display type. Variable font usage. Baseline grid alignment. Cross-platform tested.
- **9-10 (World-class)**: Custom or perfectly selected typeface. Optical sizing. Fluid type scale with clamp(). Every text element is precisely kerned, tracked, and measured. Typographic color is even. Type IS the design.

**Benchmarks**: 3 = default WordPress theme. 5 = Tailwind UI out-of-box. 7 = Notion. 8 = Linear. 9 = Stripe docs. 10 = Apple.com.

**Top 3 Vibe-Coder Failures**:
1. Using 14px body text on mobile (too small, triggers iOS zoom on inputs)
2. No letter-spacing adjustment on large headings (looks loose and amateurish)
3. line-height: 1.5 on everything including 48px headings (way too much leading)

**Quick Diagnostic**:
- Does every text element belong to a defined type scale level?
- Is heading line-height tighter than body line-height?
- Does display type (>32px) have negative letter-spacing?

---

### Dimension 2: Color (Weight: 12%)

**Rubric**:
- **1-2 (Broken)**: Default browser colors. No palette. Random colors per element. No contrast checking. No dark mode.
- **3-4 (Amateur)**: A palette exists but is poorly applied. Too many colors. Contrast violations. Dark mode is broken or absent.
- **5-6 (Functional)**: Coherent palette with primary + semantic colors. Meets basic contrast requirements. Dark mode exists but has issues.
- **7-8 (Professional)**: Systematic palette generated from a perceptually uniform color space. Semantic color tokens. WCAG AA+ contrast throughout. Polished dark mode with surface tinting.
- **9-10 (World-class)**: oklch-based palette with full tonal range. APCA-validated contrast. Dynamic color support. Dark mode that's a first-class experience, not an afterthought. Color communicates meaning at every level.

**Benchmarks**: 3 = Bootstrap default blue + danger red. 5 = Material UI default theme. 7 = GitHub. 8 = Vercel. 9 = Stripe. 10 = Apple Dynamic Color.

**Top 3 Vibe-Coder Failures**:
1. Same colors in dark mode as light mode (saturated blue on dark gray = eye strain)
2. Color as the only differentiator for states (no icon, no text, just "it turns red")
3. Gradients with muddy midpoints (HSL interpolation between blue and yellow = gray sludge)

**Quick Diagnostic**:
- Can a colorblind user distinguish all states and categories?
- Are dark mode surfaces tinted with the brand color or just neutral gray?
- Is the contrast ratio >=4.5:1 for all body text?

---

### Dimension 3: Spacing (Weight: 12%)

**Rubric**:
- **1-2 (Broken)**: No spacing system. Arbitrary pixel values. Elements overlap or are crammed. No padding inside containers.
- **3-4 (Amateur)**: Some spacing consistency but frequent violations. Padding varies between similar components. No spacing scale.
- **5-6 (Functional)**: 8px grid mostly followed. Consistent component padding. Sections have reasonable spacing. Some violations.
- **7-8 (Professional)**: Strict spacing scale (4, 8, 12, 16, 24, 32, 48, 64, 96). All spacing uses tokens. Proximity communicates grouping. Components define their own spacing.
- **9-10 (World-class)**: Spacing creates rhythm and breathing room. Macro and micro whitespace are deliberately controlled. Density is intentional and user-adjustable. Every pixel of space serves a purpose.

**Benchmarks**: 3 = Jira (inconsistent, cramped). 5 = Gmail. 7 = Notion. 8 = Linear. 9 = Apple HIG apps. 10 = Swiss typography poster-level precision.

**Top 3 Vibe-Coder Failures**:
1. padding: 10px 15px (off-grid, asymmetric for no reason)
2. Same gap between related and unrelated elements (no proximity hierarchy)
3. Cramped layouts because "users don't like scrolling" (they don't like cramped layouts more)

**Quick Diagnostic**:
- Do all spacing values fall on the 4px/8px grid?
- Is there a clear visual difference between "within group" and "between group" spacing?
- Could you increase whitespace by 50% and improve the design?

---

### Dimension 4: Composition (Weight: 12%)

**Rubric**:
- **1-2 (Broken)**: No grid. Elements positioned seemingly at random. No alignment lines. No clear reading order.
- **3-4 (Amateur)**: A grid exists but isn't consistently followed. Mixed alignment (some centered, some left, some arbitrary). Unclear visual hierarchy.
- **5-6 (Functional)**: 12-column grid or equivalent. Consistent alignment. Clear primary/secondary areas. Responsive breakpoints work.
- **7-8 (Professional)**: Strong grid with intentional breaks for emphasis. Clear focal points. Visual weight balanced. Responsive behavior designed per breakpoint, not just reflowed.
- **9-10 (World-class)**: Compositionally sophisticated — asymmetric balance, golden ratio proportions, rule of thirds applied. Every screen is balanced yet dynamic. Responsive behavior enhances the composition at each breakpoint.

**Benchmarks**: 3 = generic WordPress site. 5 = standard SaaS dashboard. 7 = Figma. 8 = Arc browser. 9 = Airbnb. 10 = Awwwards SOTD winner.

**Top 3 Vibe-Coder Failures**:
1. Everything centered (no dynamic balance, no reading direction)
2. No clear focal point (everything has equal visual weight)
3. Desktop layout shrunk on mobile instead of reflowed

**Quick Diagnostic**:
- Does the design pass the squint test (blurred, hierarchy still visible)?
- Can you draw consistent alignment lines through the layout?
- Is there exactly ONE element that draws the eye first?

---

### Dimension 5: Imagery (Weight: 8%)

**Rubric**:
- **1-2 (Broken)**: No images, or distorted/pixelated images. Random stock photos. No consistent treatment.
- **3-4 (Amateur)**: Stock photos that don't match. Inconsistent aspect ratios. No image treatment. Generic unsplash.
- **5-6 (Functional)**: Relevant images with consistent aspect ratios. Basic treatment (rounded corners). Placeholder for missing images.
- **7-8 (Professional)**: Art-directed photography or illustration. Consistent treatment (filters, overlays, crops). Inclusive representation. Loading states (skeleton/blur-up).
- **9-10 (World-class)**: Photography/illustration that IS the brand. Custom art direction. Every image feels intentional. Responsive image loading with srcset. Blur hash previews. No generic stock.

**Benchmarks**: 3 = random Unsplash. 5 = curated Unsplash. 7 = Airbnb listing photos. 8 = Apple product shots. 9 = Stripe illustrations. 10 = custom brand photography with cohesive art direction.

**Top 3 Vibe-Coder Failures**:
1. Stock photos with watermarks or inconsistent style
2. Images without aspect-ratio constraints (layout shift on load)
3. No alt text, no loading state, no error fallback

**Quick Diagnostic**:
- Are all images the same aspect ratio within a collection?
- Do images have consistent color temperature / treatment?
- Is there a fallback for broken/missing images?

---

### Dimension 6: Iconography (Weight: 8%)

**Rubric**:
- **1-2 (Broken)**: No icons, or mixed icon sets (Material + FontAwesome + custom). Inconsistent sizes and weights.
- **3-4 (Amateur)**: One icon set but poorly applied. Wrong metaphors. Inconsistent sizing. No optical alignment.
- **5-6 (Functional)**: Consistent icon set. Correct sizes. Clear metaphors. Basic icon-text alignment.
- **7-8 (Professional)**: Single icon system with consistent stroke weight, size grid (16/20/24), and optical corrections. Icons paired with labels for clarity. Active/inactive states.
- **9-10 (World-class)**: Custom icon system that extends brand identity. Size-specific optical adjustments. Hierarchical rendering (multicolor). Animated transitions between icon states.

**Benchmarks**: 3 = mixed free icon sets. 5 = Heroicons out of box. 7 = GitHub Octicons. 8 = SF Symbols. 9 = Phosphor Icons (well-implemented). 10 = custom icon system with brand DNA.

**Top 3 Vibe-Coder Failures**:
1. Mixing outline and filled icons randomly (use outline for inactive, filled for active — or be consistent)
2. Icon-only buttons without labels or tooltips (mystery meat navigation)
3. Icons at inconsistent sizes (18px, 20px, 22px, 24px on the same page)

**Quick Diagnostic**:
- Are ALL icons from the same family/set?
- Do icons have consistent stroke weight?
- Is every standalone icon paired with a label or tooltip?

---

### Dimension 7: Motion (Weight: 8%)

**Rubric**:
- **1-2 (Broken)**: No transitions. Instant state changes. Or: everything animates excessively with no purpose.
- **3-4 (Amateur)**: Some CSS transitions but inconsistent. Random durations. Default linear easing. Motion doesn't communicate meaning.
- **5-6 (Functional)**: Consistent transition duration (150-200ms). Ease-out for enters, ease-in for exits. Page transitions exist. Hover states animate.
- **7-8 (Professional)**: Motion tokens (duration, easing curves). Choreographed sequences. Spring physics for interactive elements. Loading skeletons with shimmer. Staggered list animations.
- **9-10 (World-class)**: Motion is a design language. Shared element transitions. Gesture-driven animation. Every animation has purpose and is precisely timed. Reduced-motion alternative for every animation.

**Benchmarks**: 3 = no animation. 5 = basic CSS transitions. 7 = Notion (subtle, purposeful). 8 = Linear (fast, precise). 9 = Airbnb (Lottie, springs). 10 = Apple.com (scroll choreography).

**Top 3 Vibe-Coder Failures**:
1. animation-duration: 1s on everything (too slow for UI — use 150-300ms)
2. No prefers-reduced-motion media query (accessibility violation)
3. Entrance animations on every scroll, causing janky performance

**Quick Diagnostic**:
- Does every animated element respect prefers-reduced-motion?
- Are transition durations under 300ms for micro-interactions?
- Does motion COMMUNICATE something (state change, direction, hierarchy)?

---

### Dimension 8: Polish (Weight: 10%)

**Rubric**:
- **1-2 (Broken)**: Visible bugs. Overflow. Broken layouts. Missing states. Raw error messages.
- **3-4 (Amateur)**: Layout works but edge cases are unhandled. No loading states. No empty states. Scroll jank. No focus styles.
- **5-6 (Functional)**: All primary states covered. Loading indicators. Error messages. Focus visible. Minor edge cases may be unpolished.
- **7-8 (Professional)**: Every state designed: loading, empty, error, partial, overflow, min/max content. Skeleton screens. Smooth scrolling. Pixel-perfect alignment. Focus management for keyboard navigation.
- **9-10 (World-class)**: Sub-pixel precision. Every edge case is a design opportunity (delightful empty states, helpful errors, graceful degradation). Performance optimized. Feels inevitable — nothing is missing.

**Benchmarks**: 3 = MVP prototype. 5 = shipped v1 product. 7 = mature SaaS (Slack). 8 = Linear. 9 = Figma. 10 = iOS system apps.

**Top 3 Vibe-Coder Failures**:
1. No loading states (blank screen while data fetches)
2. No focus-visible styles (keyboard users are blind)
3. Text overflow not handled (long names break layouts)

**Quick Diagnostic**:
- What happens with 0 items? 1 item? 1000 items?
- What happens when text is 3x the expected length?
- Can you navigate the entire UI with keyboard only?

---

### Dimension 9: Coherence (Weight: 8%)

**Rubric**:
- **1-2 (Broken)**: Every page looks like a different product. No shared visual language. Mixed frameworks/component libraries.
- **3-4 (Amateur)**: Some shared elements but frequent inconsistencies. Different button styles across pages. Inconsistent spacing.
- **5-6 (Functional)**: Component library in use. Most elements are consistent. Some one-offs. Design tokens partially adopted.
- **7-8 (Professional)**: Full design token system. All components follow the same visual rules. Cross-page consistency. Theming works. New pages feel like natural extensions.
- **9-10 (World-class)**: Every pixel belongs to the same visual language. You could show any 100x100 crop and identify the product. Perfect token consumption. Zero one-off styles.

**Benchmarks**: 3 = WordPress site with 5 plugins from different authors. 5 = early-stage startup product. 7 = Notion. 8 = Linear. 9 = Stripe. 10 = Apple (cross-platform coherence from Watch to Mac).

**Top 3 Vibe-Coder Failures**:
1. Copy-pasting UI code from different sources (Tailwind examples + Material + custom = Frankenstein)
2. Using multiple component libraries in one product
3. Inconsistent border-radius (4px here, 8px there, 12px somewhere else)

**Quick Diagnostic**:
- How many unique border-radius values exist in the codebase? (Should be 3-5)
- How many unique color values? (Should be <30 for a complete system)
- Could a new page be built entirely from existing components?

---

### Dimension 10: Craft (Weight: 7%)

**Rubric**:
- **1-2 (Broken)**: No evidence of care. Feels like a homework assignment or template.
- **3-4 (Amateur)**: Basic effort visible but no signature moments. Generic feel. Could be any product.
- **5-6 (Functional)**: Some nice touches (custom empty state, smooth animations, thoughtful copy). The designer cared.
- **7-8 (Professional)**: Intentionality in every detail. Custom illustrations, considered micro-copy, delightful empty states, signature interactions. The product has personality.
- **9-10 (World-class)**: The product feels inevitable — every choice was deliberate. Surprises the user with care in unexpected places. Has at least one "how did they do that?" moment. Would win design awards.

**Benchmarks**: 3 = template. 5 = competent startup. 7 = Notion (gentle craft). 8 = Linear (precision craft). 9 = Stripe (gradient craft). 10 = the "wow" products that designers share on Twitter.

**Top 3 Vibe-Coder Failures**:
1. No personality — the product could be any product. No brand voice, no delight.
2. Error states are technical ("404", "Something went wrong") instead of helpful and human.
3. No custom touches — everything is default component library with no customization.

**Quick Diagnostic**:
- Does the product have at least one moment of genuine delight?
- Would a designer share this on Twitter/Dribbble as inspiration?
- Does it feel like a human designed it, or a template generated it?

---

## Award Calibration

### Awwwards Mapping

Awwwards uses 4 criteria, each scored 1-10:

| Awwwards Criterion | Visual Scoring Framework Dimensions | Weight |
|---|---|---|
| **Design** | Typography (30%) + Color (25%) + Spacing (20%) + Composition (25%) | 40% |
| **Usability** | Polish (40%) + Spacing (20%) + Composition (20%) + Coherence (20%) | 30% |
| **Creativity** | Craft (35%) + Motion (25%) + Imagery (20%) + Color (20%) | 15% |
| **Content** | Typography (30%) + Coherence (30%) + Imagery (20%) + Polish (20%) | 15% |

**Conversion formula** (approximate):
```
awwwards_design = 0.30 * typography + 0.25 * color + 0.20 * spacing + 0.25 * composition
awwwards_usability = 0.40 * polish + 0.20 * spacing + 0.20 * composition + 0.20 * coherence
awwwards_creativity = 0.35 * craft + 0.25 * motion + 0.20 * imagery + 0.20 * color
awwwards_content = 0.30 * typography + 0.30 * coherence + 0.20 * imagery + 0.20 * polish

awwwards_total = 0.40 * design + 0.30 * usability + 0.15 * creativity + 0.15 * content
```

SOTD threshold: Awwwards total >= 8.0. About 70% of SOTD winners score 8+ on this framework.

### Red Dot Mapping

Red Dot evaluates: Innovation, Functionality, Formal Quality, Ergonomics, Durability, Symbolic/Emotional Content, Self-explanatory quality, Ecological compatibility.

| Red Dot Criterion | Visual Scoring Framework Dimensions |
|---|---|
| Formal Quality | Typography + Color + Composition + Coherence |
| Functionality | Polish + Spacing + Coherence |
| Ergonomics | Spacing + Polish (touch targets, readability) |
| Self-explanatory | Iconography + Typography + Composition |
| Emotional Content | Craft + Color + Motion |

### iF Design Award Mapping

iF evaluates: Idea, Form, Function, Differentiation, Impact.

| iF Criterion | Visual Scoring Framework Dimensions |
|---|---|
| Form | Typography + Color + Spacing + Composition |
| Function | Polish + Coherence + Spacing |
| Differentiation | Craft + Motion + Imagery |
| Impact | Color + Composition + Craft |

---

## Overall Score Calculation

### Weighted Formula

```
overall_score = (
  typography   * 0.15 +
  color        * 0.12 +
  spacing      * 0.12 +
  composition  * 0.12 +
  imagery      * 0.08 +
  iconography  * 0.08 +
  motion       * 0.08 +
  polish       * 0.10 +
  coherence    * 0.08 +
  craft        * 0.07
)
```

### Score Interpretation

| Score Range | Level | Description | Action |
|---|---|---|---|
| **1.0-3.9** | Needs Redesign | Fundamental visual problems. Multiple broken dimensions. Users actively distrust the product. | Full redesign with design system foundation. |
| **4.0-5.4** | Amateur | Recognizable as a designed product but clearly unpolished. Vibe-coded aesthetic. | Systematic improvement: establish type scale, color tokens, spacing grid. |
| **5.5-6.9** | Competent | Functional and consistent. Doesn't offend but doesn't impress. Most SaaS products live here. | Targeted polish: improve weakest 3 dimensions. Add craft moments. |
| **7.0-8.4** | Professional | Clearly designed by someone with skill. Competes with best-in-class products. Most design-led companies (Notion, Slack, Figma) live here. | Refinement: push strongest dimensions toward 9+. Aim for award submission. |
| **8.5-10.0** | World-class | Award-winning quality. Every dimension is at least 7+. The product IS a design reference. Apple, Stripe, Linear at their best. | Maintain and innovate. Lead the industry. |

### Practical Usage

**When scoring a UI**:
1. Score each dimension independently (don't let a strong dimension inflate a weak one)
2. Note the lowest-scoring dimension — this is the bottleneck
3. Calculate overall score with the weighted formula
4. The lowest individual dimension score matters more than the overall — a product with a 9.0 average but a 3.0 in accessibility is not an 9.0 product
5. Improvement priority: always fix the lowest dimension first (diminishing returns above 8)

**Minimum viable scores for launch**:
- Consumer product: 6.0+ overall, no dimension below 5
- Enterprise product: 5.5+ overall, no dimension below 4
- Developer tool: 5.0+ overall, no dimension below 4
- Marketing site: 7.0+ overall, no dimension below 6
