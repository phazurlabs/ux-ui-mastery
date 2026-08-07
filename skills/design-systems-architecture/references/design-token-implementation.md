# Design Token Architecture and Implementation

Authoritative reference for building, scaling, and maintaining design token systems. Apply these patterns to create a single source of truth for design decisions that propagates consistently across platforms, tools, and teams.

---

## W3C Design Tokens Specification

The W3C Design Tokens Community Group specification defines a standard JSON format for representing design tokens. Adopt this format as the canonical source file for all tokens.

### File Structure

Token files use `.tokens.json` or `.tokens` extension. The top-level object contains groups and tokens.

```json
{
  "$name": "Brand Tokens",
  "$description": "Core design tokens for the product design system",
  "color": {
    "$type": "color",
    "$description": "Color palette tokens",
    "primary": {
      "$value": "#0066cc",
      "$description": "Primary brand color"
    },
    "primary-light": {
      "$value": "{color.primary}",
      "$description": "Aliased from primary, overridden per theme"
    }
  },
  "spacing": {
    "$type": "dimension",
    "sm": { "$value": "8px" },
    "md": { "$value": "16px" },
    "lg": { "$value": "24px" }
  }
}
```

### Key Format Rules

- **`$value`**: The resolved or aliased value. Required on every token.
- **`$type`**: Declares the token type. Set on groups to apply to all children, or on individual tokens.
- **`$description`**: Human-readable purpose. Always provide descriptions for semantic and component tokens.
- **Aliases**: Reference other tokens with curly-brace syntax: `"{group.token}"`. Aliases resolve at build time.
- **Groups**: Nest tokens in objects to create logical groupings. Groups are not tokens themselves unless they have a `$value`.

### Token Types Defined by the Spec

| Type | Example `$value` | Notes |
|------|-------------------|-------|
| `color` | `"#0066cc"`, `"oklch(0.55 0.2 250)"` | Any valid CSS color |
| `dimension` | `"16px"`, `"1.5rem"` | Number + unit |
| `fontFamily` | `"Inter, sans-serif"` | String or array |
| `fontWeight` | `400`, `"bold"` | Number (100-900) or named weight |
| `duration` | `"200ms"` | Time value for animations |
| `cubicBezier` | `[0.4, 0, 0.2, 1]` | Four-number array |
| `number` | `1.5` | Unitless number |
| `strokeStyle` | `"solid"`, `"dashed"` | Border style keywords |
| `border` | `{ "color": "...", "width": "...", "style": "..." }` | Composite type |
| `transition` | `{ "duration": "...", "delay": "...", "timingFunction": "..." }` | Composite type |
| `shadow` | `{ "color": "...", "offsetX": "...", "offsetY": "...", "blur": "...", "spread": "..." }` | Composite or array for stacked shadows |
| `gradient` | `[{ "color": "...", "position": 0 }, ...]` | Array of color stops |

---

## Token Naming Conventions

### Flat vs. Nested

**Flat naming** uses dot-delimited or dash-delimited strings:

```
color-bg-primary
color-text-secondary
spacing-md
```

**Nested naming** uses object hierarchy:

```json
{
  "color": {
    "bg": {
      "primary": { "$value": "..." }
    }
  }
}
```

Prefer nested naming in source files for readability and group-level `$type` inheritance. Transform to flat naming in platform outputs where needed.

### CTI (Category-Type-Item) Naming

The Category-Type-Item pattern provides consistent structure:

```
{category}-{type}-{item}-{variant}-{state}
```

Examples:
- `color-bg-surface-default`
- `color-text-primary-hover`
- `spacing-gap-md`
- `font-size-heading-lg`
- `shadow-elevation-md`
- `border-radius-sm`
- `duration-transition-fast`

### BEM-Inspired Naming

For component tokens, adapt BEM conventions:

```
{component}__{element}--{modifier}--{state}
```

Translated to token naming:
- `button__label--primary--default`
- `button__label--primary--hover`
- `input__border--error--focus`

### Naming Rules

1. Use lowercase and hyphens. Never camelCase in source token names.
2. Order specificity from general to specific: `color-bg-primary`, not `primary-bg-color`.
3. Include state as the final segment: `-hover`, `-focus`, `-active`, `-disabled`.
4. Avoid encoding platform-specific values in names (no `-px`, `-rem` suffixes).
5. Keep names under 5 segments for readability. If a name exceeds this, reconsider the nesting strategy.

---

## Token Types in Detail

### Color Tokens

Store color values in the perceptually-uniform OKLCH space in source files. Transform to hex, RGB, or HSL for platform outputs that lack OKLCH support.

```json
{
  "color": {
    "$type": "color",
    "blue-500": { "$value": "oklch(0.58 0.19 250)" },
    "neutral-100": { "$value": "oklch(0.96 0.005 250)" }
  }
}
```

### Dimension Tokens

Use `rem` for scalable values, `px` for fixed values (borders, icons). Transform units per platform.

```json
{
  "spacing": {
    "$type": "dimension",
    "xs": { "$value": "0.25rem" },
    "sm": { "$value": "0.5rem" },
    "md": { "$value": "1rem" },
    "lg": { "$value": "1.5rem" },
    "xl": { "$value": "2rem" },
    "2xl": { "$value": "3rem" }
  },
  "border-width": {
    "$type": "dimension",
    "thin": { "$value": "1px" },
    "medium": { "$value": "2px" },
    "thick": { "$value": "4px" }
  }
}
```

### Shadow Tokens

Define as composite objects. Support stacked shadows with arrays.

```json
{
  "shadow": {
    "$type": "shadow",
    "sm": {
      "$value": {
        "color": "{color.neutral-900 / 0.08}",
        "offsetX": "0px",
        "offsetY": "1px",
        "blur": "2px",
        "spread": "0px"
      }
    },
    "lg": {
      "$value": [
        { "color": "{color.neutral-900 / 0.1}", "offsetX": "0px", "offsetY": "4px", "blur": "6px", "spread": "-1px" },
        { "color": "{color.neutral-900 / 0.06}", "offsetX": "0px", "offsetY": "10px", "blur": "15px", "spread": "-3px" }
      ]
    }
  }
}
```

### Typography Composite Tokens

Group related typographic properties into composite tokens for text styles.

```json
{
  "typography": {
    "heading-lg": {
      "$value": {
        "fontFamily": "{font.family.heading}",
        "fontSize": "{font.size.2xl}",
        "fontWeight": "{font.weight.bold}",
        "lineHeight": "{line-height.tight}",
        "letterSpacing": "{letter-spacing.tight}"
      }
    },
    "body-md": {
      "$value": {
        "fontFamily": "{font.family.body}",
        "fontSize": "{font.size.md}",
        "fontWeight": "{font.weight.regular}",
        "lineHeight": "{line-height.normal}",
        "letterSpacing": "{letter-spacing.normal}"
      }
    }
  }
}
```

---

## Token Aliasing and Referencing

Build token chains from primitive to semantic to component-level, creating layers of abstraction.

### Three-Tier Token Architecture

**Tier 1 — Global (Primitive) Tokens**

Raw values with no semantic meaning. Named by their intrinsic property.

```json
{
  "blue-500": { "$value": "oklch(0.58 0.19 250)" },
  "gray-200": { "$value": "oklch(0.90 0.005 250)" },
  "space-4": { "$value": "1rem" },
  "font-size-16": { "$value": "1rem" }
}
```

**Tier 2 — Semantic (Alias) Tokens**

Map intent to primitives. These are the theming layer.

```json
{
  "color-bg-primary": { "$value": "{color.neutral.0}" },
  "color-bg-interactive": { "$value": "{color.blue.500}" },
  "color-text-primary": { "$value": "{color.neutral.900}" },
  "spacing-component-gap": { "$value": "{space.4}" },
  "font-size-body": { "$value": "{font-size.16}" }
}
```

**Tier 3 — Component Tokens**

Map component-specific needs to semantic tokens. Enable surgical overrides.

```json
{
  "button-bg": { "$value": "{color-bg-interactive}" },
  "button-text": { "$value": "{color-text-on-interactive}" },
  "button-padding-x": { "$value": "{spacing-component-gap}" },
  "button-border-radius": { "$value": "{border-radius-md}" },
  "card-bg": { "$value": "{color-bg-primary}" },
  "card-padding": { "$value": "{spacing-component-gap}" }
}
```

### Alias Resolution

Aliases form a directed acyclic graph (DAG). Build tools resolve references recursively at compile time. Circular references are build errors — enforce cycle detection in CI.

Example resolution chain:
```
button-bg → color-bg-interactive → color.blue.500 → oklch(0.58 0.19 250)
```

In dark mode, only the semantic layer changes:
```
color-bg-interactive → color.blue.300 → oklch(0.72 0.14 250)
```

The component token (`button-bg`) and global token (`color.blue.500`) remain unchanged. Only the alias mapping in Tier 2 shifts.

---

## Multi-Theme Token Architecture

### Theme File Structure

Organize tokens with a base set and theme overrides:

```
tokens/
  global/
    color.tokens.json      # All primitive color values
    spacing.tokens.json    # All spacing primitives
    typography.tokens.json # All type primitives
  semantic/
    light.tokens.json      # Semantic aliases for light theme
    dark.tokens.json       # Semantic aliases for dark theme
    high-contrast.tokens.json
  brand/
    brand-a.tokens.json    # Brand A overrides
    brand-b.tokens.json    # Brand B overrides
  component/
    button.tokens.json
    card.tokens.json
    input.tokens.json
```

### Light/Dark Themes

Define identical semantic token names in both `light.tokens.json` and `dark.tokens.json`, pointing to different global values:

```json
// light.tokens.json
{
  "color-bg-primary": { "$value": "{color.neutral.0}" },
  "color-text-primary": { "$value": "{color.neutral.900}" },
  "color-border-default": { "$value": "{color.neutral.200}" }
}

// dark.tokens.json
{
  "color-bg-primary": { "$value": "{color.neutral.900}" },
  "color-text-primary": { "$value": "{color.neutral.100}" },
  "color-border-default": { "$value": "{color.neutral.700}" }
}
```

### Brand Variants

Override the global primitive layer per brand while keeping semantic and component layers identical:

```json
// brand-a.tokens.json
{ "color.blue.500": { "$value": "oklch(0.58 0.19 250)" } }

// brand-b.tokens.json
{ "color.blue.500": { "$value": "oklch(0.55 0.22 280)" } }
```

### Density Modes

Define spacing and sizing tokens for compact, default, and comfortable densities:

```json
// density-compact.tokens.json
{ "spacing-component-gap": { "$value": "{space.2}" }, "font-size-body": { "$value": "{font-size.14}" } }

// density-default.tokens.json
{ "spacing-component-gap": { "$value": "{space.4}" }, "font-size-body": { "$value": "{font-size.16}" } }

// density-comfortable.tokens.json
{ "spacing-component-gap": { "$value": "{space.6}" }, "font-size-body": { "$value": "{font-size.18}" } }
```

### High-Contrast Mode

Increase contrast ratios by mapping text tokens to pure black/white and strengthening border visibility:

```json
// high-contrast.tokens.json
{
  "color-text-primary": { "$value": "{color.neutral.1000}" },
  "color-bg-primary": { "$value": "{color.neutral.0}" },
  "color-border-default": { "$value": "{color.neutral.800}" },
  "border-width-default": { "$value": "{border-width.medium}" }
}
```

---

## Token Transformation Pipeline

### Overview

```
tokens.json → Style Dictionary → Platform Outputs
              (transform + format)
```

Source token files are the single source of truth. Style Dictionary (or alternatives like Cobalt UI, Specify) reads these files, resolves aliases, applies transforms, and outputs platform-specific formats.

### Style Dictionary Configuration

```javascript
// config.js
module.exports = {
  source: ['tokens/**/*.tokens.json'],
  platforms: {
    css: {
      transformGroup: 'css',
      buildPath: 'dist/css/',
      files: [{
        destination: 'tokens.css',
        format: 'css/variables',
        options: { outputReferences: true }
      }]
    },
    scss: {
      transformGroup: 'scss',
      buildPath: 'dist/scss/',
      files: [{
        destination: '_tokens.scss',
        format: 'scss/variables'
      }]
    },
    ios: {
      transformGroup: 'ios-swift',
      buildPath: 'dist/ios/',
      files: [{
        destination: 'DesignTokens.swift',
        format: 'ios-swift/class.swift',
        className: 'DesignTokens'
      }]
    },
    android: {
      transformGroup: 'android',
      buildPath: 'dist/android/',
      files: [{
        destination: 'tokens.xml',
        format: 'android/resources'
      }]
    }
  }
};
```

### Transforms

Transforms modify token values or names for specific platforms:

- **name/cti/kebab**: Converts nested paths to kebab-case (`color-bg-primary`).
- **name/cti/camel**: Converts to camelCase (`colorBgPrimary`) for JavaScript/Swift.
- **color/css**: Converts color values to valid CSS strings.
- **color/UIColor**: Converts colors to Swift UIColor syntax.
- **size/rem**: Converts px dimensions to rem.
- **size/pxToSp**: Converts px to Android sp units.

### Custom Transforms

Create custom transforms for project-specific needs:

```javascript
StyleDictionary.registerTransform({
  name: 'color/oklch-to-hex',
  type: 'value',
  matcher: (token) => token.$type === 'color',
  transformer: (token) => convertOklchToHex(token.$value)
});

StyleDictionary.registerTransform({
  name: 'size/pxToRem',
  type: 'value',
  matcher: (token) => token.$type === 'dimension',
  transformer: (token) => {
    const px = parseFloat(token.$value);
    return `${px / 16}rem`;
  }
});
```

### Custom Formats

Generate entirely custom output formats:

```javascript
StyleDictionary.registerFormat({
  name: 'tailwind/config',
  formatter: ({ dictionary }) => {
    const colors = {};
    dictionary.allTokens
      .filter(t => t.$type === 'color' && t.path[0] === 'color')
      .forEach(t => {
        set(colors, t.path.slice(1).join('.'), t.value);
      });
    return `module.exports = { theme: { colors: ${JSON.stringify(colors, null, 2)} } }`;
  }
});
```

---

## Platform-Specific Outputs

### CSS Custom Properties

```css
:root {
  --color-bg-primary: #ffffff;
  --color-bg-interactive: oklch(0.58 0.19 250);
  --color-text-primary: #1a1a2e;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --font-size-body: 1rem;
  --shadow-sm: 0 1px 2px rgba(26, 26, 46, 0.08);
}

[data-theme="dark"] {
  --color-bg-primary: #1a1a2e;
  --color-text-primary: #f0f0f4;
}
```

Enable `outputReferences: true` to preserve alias chains in CSS output, making debugging easier.

### SCSS Variables

```scss
$color-bg-primary: #ffffff;
$color-text-primary: #1a1a2e;
$spacing-md: 1rem;
$font-size-body: 1rem;
```

### iOS Swift

```swift
public class DesignTokens {
    public static let colorBgPrimary = UIColor(red: 1.0, green: 1.0, blue: 1.0, alpha: 1.0)
    public static let colorTextPrimary = UIColor(red: 0.102, green: 0.102, blue: 0.180, alpha: 1.0)
    public static let spacingMd: CGFloat = 16.0
    public static let fontSizeBody: CGFloat = 16.0
}
```

### Android XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<resources>
  <color name="color_bg_primary">#FFFFFF</color>
  <color name="color_text_primary">#1A1A2E</color>
  <dimen name="spacing_md">16dp</dimen>
  <dimen name="font_size_body">16sp</dimen>
</resources>
```

### React Native

```javascript
export const DesignTokens = {
  colorBgPrimary: '#FFFFFF',
  colorTextPrimary: '#1A1A2E',
  spacingMd: 16,
  fontSizeBody: 16,
};
```

### Tailwind Config

```javascript
module.exports = {
  theme: {
    colors: {
      bg: { primary: 'var(--color-bg-primary)', interactive: 'var(--color-bg-interactive)' },
      text: { primary: 'var(--color-text-primary)', secondary: 'var(--color-text-secondary)' }
    },
    spacing: {
      xs: 'var(--spacing-xs)',
      sm: 'var(--spacing-sm)',
      md: 'var(--spacing-md)',
      lg: 'var(--spacing-lg)'
    }
  }
};
```

Reference CSS custom properties in Tailwind to enable runtime theming while retaining Tailwind's utility-class authoring model.

---

## Figma Integration

### Token Studio Setup

1. Install the Tokens Studio for Figma plugin (formerly Figma Tokens).
2. Connect to the tokens repository via GitHub, GitLab, or JSONBin sync.
3. Map token groups to Figma's native structures: colors to color styles, typography composites to text styles, spacing to auto layout variables.
4. Configure push/pull sync direction. Prefer bidirectional sync with conflict resolution rules.

### Figma Variables (Native)

Figma Variables natively support:

- **Color variables**: Map directly to color tokens.
- **Number variables**: Map to spacing, border-radius, border-width, opacity tokens.
- **String variables**: Map to font-family tokens.
- **Boolean variables**: Map to feature flags or visibility tokens.

Organize Figma variable collections to mirror the token tier structure:

- **Primitives** collection: Global palette values.
- **Semantic** collection: Aliases that reference primitives. Define modes (Light, Dark) within this collection.
- **Component** collection: Component-specific aliases referencing semantic variables.

### Sync Workflows

**Design-to-Code (Forward Sync)**

1. Designer updates tokens in Token Studio or Figma Variables.
2. Token Studio commits changes to the tokens repository.
3. CI pipeline runs Style Dictionary build.
4. Platform outputs are published as a package (npm, CocoaPods, Maven).
5. Consuming applications update the token package.

**Code-to-Design (Reverse Sync)**

1. Engineer modifies token JSON in the repository.
2. Token Studio pulls updated tokens into Figma.
3. Figma styles and variables update automatically.
4. Designers see changes in their working files.

Establish a clear rule: either design or code is the canonical source, not both. Bidirectional sync is for propagation, not dual authorship.

---

## Token Documentation

### Auto-Generating Documentation Sites

Use Style Dictionary's built-in HTML format or build a custom documentation generator:

```javascript
StyleDictionary.registerFormat({
  name: 'docs/html',
  formatter: ({ dictionary, platform }) => {
    return generateDocsSite(dictionary.allTokens, platform);
  }
});
```

Alternatively, integrate with documentation frameworks:

- **Storybook**: Use the `@storybook/addon-designs` or custom doc pages to render token swatches and values.
- **Zeroheight / Supernova**: Import tokens directly and auto-generate visual documentation.
- **Custom static site**: Build with Astro, Next.js, or Eleventy; read token JSON and render interactive swatch grids.

### Documentation Content for Each Token

- Visual preview (color swatch, type specimen, spacing box).
- Token name (all platform variants: CSS, iOS, Android).
- Current resolved value.
- Alias chain (what it references).
- Usage guidelines (when to use, when not to use).
- Accessibility notes (contrast ratios for color tokens).

---

## Token Versioning and Migration

### Semantic Versioning

Apply semver to token packages:

- **Patch (1.0.x)**: Value adjustments that do not change token names or break existing usage (e.g., adjusting a color's lightness by 2%).
- **Minor (1.x.0)**: New tokens added, no removals or renames.
- **Major (x.0.0)**: Token renames, removals, type changes, or structural reorganization.

### Handling Breaking Changes

1. **Deprecation period**: Mark tokens as deprecated with `$description` annotations at least one minor version before removal.
2. **Migration codemods**: Provide automated migration scripts (jscodeshift, sed scripts, Style Dictionary custom transforms) that rename or remap tokens in consuming codebases.
3. **Changelog**: Maintain a detailed changelog for every token change, including before/after values and migration instructions.

```json
{
  "color-bg-surface": {
    "$value": "{color.neutral.100}",
    "$description": "DEPRECATED in v2.3.0. Use color-bg-secondary instead. Will be removed in v3.0.0.",
    "$extensions": {
      "deprecated": true,
      "replacement": "color-bg-secondary"
    }
  }
}
```

### Migration Automation

Build a migration CLI that reads deprecation metadata and updates consuming files:

```bash
npx @design-system/token-migrate --from 2.x --to 3.x --path src/
```

The migration tool should:
- Find all references to deprecated tokens (CSS custom properties, SCSS variables, JS imports).
- Replace with the specified replacement token.
- Report unmigrated references that need manual review.

---

## Token Governance

### Ownership Model

- **Design system team** owns global and semantic tokens. All changes require team review.
- **Product teams** own component tokens scoped to their products. Changes are reviewed by the design system team for consistency.
- **Brand team** owns brand-variant token overrides. Coordinate with design system team for integration.

### Change Request Process

1. **Proposal**: Submit a token change request (GitHub issue, RFC document) with rationale, visual examples, and impact assessment.
2. **Impact analysis**: Run automated analysis to determine which components and products consume the affected tokens.
3. **Design review**: Design system team evaluates visual impact, accessibility implications, and cross-theme consistency.
4. **Engineering review**: Verify build compatibility, migration path, and performance impact.
5. **Approval**: Require sign-off from both design and engineering leads.
6. **Implementation**: Merge token changes and publish a new package version.
7. **Communication**: Notify consuming teams via changelog, Slack, and documentation updates.

### Review Criteria

Evaluate every token change against:

- **Consistency**: Does it follow existing naming conventions and tier structure?
- **Accessibility**: Do resulting color combinations meet WCAG AA (minimum) or AAA contrast?
- **Themability**: Does it work correctly across all theme variants (light, dark, high-contrast, brand)?
- **Scalability**: Does the naming pattern accommodate future growth without renaming?
- **Platform parity**: Is the token expressible in all target platform formats?

---

## Performance

### CSS Custom Property Performance

CSS custom properties have negligible performance overhead for static theming (hundreds of properties on `:root`). However, be aware of these patterns:

- **Inheritance cost**: Every DOM element inherits all custom properties from its ancestors. Keep the total number of global custom properties below 500 for optimal performance.
- **Recalculation on change**: Changing a custom property on `:root` triggers style recalculation for every element that uses it. Batch theme changes into a single DOM write.
- **Scoped properties**: Define component tokens on the component's root element rather than `:root` to limit recalculation scope during dynamic changes.

### Runtime vs. Build-Time Tokens

| Approach | Mechanism | Best For |
|----------|-----------|----------|
| **Build-time** | Static values compiled into CSS/platform code | Performance-critical applications, static themes |
| **Runtime CSS** | CSS custom properties swapped via class or attribute | Dynamic theme switching, user preferences |
| **Runtime JS** | JavaScript theme objects applied via CSS-in-JS | Highly dynamic themes, runtime computation |

Prefer build-time tokens for static applications. Use runtime CSS custom properties for theme switching. Resort to runtime JS only when tokens must be computed from user input or external data.

### Optimization Strategies

- Tree-shake unused tokens at build time by analyzing which tokens are actually referenced in component code.
- Split token CSS into critical (above-fold colors, type) and non-critical (shadows, motion) bundles.
- Use `content-visibility: auto` on off-screen sections to defer style resolution for token-heavy components.

---

## Token Testing

### Visual Regression Testing

Integrate visual regression tests that detect unintended changes from token modifications:

1. Maintain a token specimen page (or Storybook stories) showing every token applied in context.
2. Run visual regression (Chromatic, Percy, BackstopJS) on every token change PR.
3. Flag any visual diff larger than the expected change scope.

### Contrast Validation

Automate contrast checking in the token build pipeline:

```javascript
// In Style Dictionary build script
const contrastPairs = [
  ['color-text-primary', 'color-bg-primary'],
  ['color-text-secondary', 'color-bg-primary'],
  ['color-text-on-interactive', 'color-bg-interactive'],
];

contrastPairs.forEach(([fg, bg]) => {
  const ratio = calculateContrast(resolvedTokens[fg], resolvedTokens[bg]);
  if (ratio < 4.5) {
    throw new Error(`Contrast failure: ${fg} on ${bg} = ${ratio}:1 (requires 4.5:1)`);
  }
});
```

Run contrast validation for every theme variant. A token change that passes in light mode may fail in dark mode.

### Token Integrity Tests

Write unit tests for the token build:

- **No broken references**: Every alias resolves to a defined token.
- **No circular references**: Build fails on dependency cycles.
- **Type validation**: Every token's `$value` matches its declared `$type`.
- **Name convention compliance**: All token names match the agreed naming pattern (regex validation).
- **Completeness**: Every semantic token defined in light theme exists in dark theme (and vice versa).
- **Value range validation**: Dimensions are positive, opacity is 0-1, durations are reasonable (0-5000ms).

```javascript
describe('Token Integrity', () => {
  test('all aliases resolve', () => {
    const unresolved = findUnresolvedAliases(tokenFiles);
    expect(unresolved).toHaveLength(0);
  });

  test('light and dark themes have matching token sets', () => {
    const lightKeys = Object.keys(resolveTokens('light'));
    const darkKeys = Object.keys(resolveTokens('dark'));
    expect(lightKeys.sort()).toEqual(darkKeys.sort());
  });

  test('all color pairs meet WCAG AA', () => {
    contrastPairs.forEach(([fg, bg]) => {
      const ratio = calculateContrast(resolve(fg), resolve(bg));
      expect(ratio).toBeGreaterThanOrEqual(4.5);
    });
  });
});
```

---

## Advanced Patterns

### Responsive Tokens

Define tokens that adapt to viewport or container context using CSS custom properties and media queries:

```css
:root {
  --spacing-section: 2rem;
  --font-size-hero: 2.5rem;
}

@media (min-width: 768px) {
  :root {
    --spacing-section: 4rem;
    --font-size-hero: 4rem;
  }
}

@media (min-width: 1280px) {
  :root {
    --spacing-section: 6rem;
    --font-size-hero: 5rem;
  }
}
```

Alternatively, use `clamp()` values as token values for fluid responsive behavior:

```json
{
  "spacing-section": { "$value": "clamp(2rem, 4vw, 6rem)" },
  "font-size-hero": { "$value": "clamp(2.5rem, 5vw, 5rem)" }
}
```

Responsive tokens that use `clamp()` are more maintainable than media-query-based approaches because they produce a single token value rather than multiple overrides.

### Component-Scoped Tokens

Apply tokens at the component level for encapsulation:

```css
.card {
  --card-padding: var(--spacing-md);
  --card-radius: var(--border-radius-lg);
  --card-bg: var(--color-bg-surface);
  --card-border: var(--color-border-default);

  padding: var(--card-padding);
  border-radius: var(--card-radius);
  background: var(--card-bg);
  border: 1px solid var(--card-border);
}

/* Override for a specific context */
.sidebar .card {
  --card-padding: var(--spacing-sm);
  --card-radius: var(--border-radius-sm);
}
```

Component-scoped tokens create an API surface for each component. External code overrides the component's custom properties without modifying the component's internal CSS.

### Token Composition

Compose complex values from multiple primitive tokens:

```json
{
  "shadow-elevation-md": {
    "$value": [
      {
        "offsetX": "{shadow.offset.none}",
        "offsetY": "{shadow.offset.sm}",
        "blur": "{shadow.blur.md}",
        "spread": "{shadow.spread.none}",
        "color": "{shadow.color.ambient}"
      },
      {
        "offsetX": "{shadow.offset.none}",
        "offsetY": "{shadow.offset.md}",
        "blur": "{shadow.blur.lg}",
        "spread": "{shadow.spread.neg-sm}",
        "color": "{shadow.color.direct}"
      }
    ]
  }
}
```

Compose typography tokens from individual property tokens:

```json
{
  "typography-heading-lg": {
    "$value": {
      "fontFamily": "{font.family.heading}",
      "fontSize": "{font.size.2xl}",
      "fontWeight": "{font.weight.bold}",
      "lineHeight": "{line-height.tight}",
      "letterSpacing": "{letter-spacing.tight}"
    }
  }
}
```

### Conditional Tokens with Extensions

Use the `$extensions` field for metadata that drives conditional logic in the build pipeline:

```json
{
  "motion-duration-expand": {
    "$value": "300ms",
    "$extensions": {
      "reducedMotion": "0ms",
      "platform": {
        "ios": "250ms",
        "android": "300ms",
        "web": "300ms"
      }
    }
  }
}
```

Write custom Style Dictionary transforms that read `$extensions` and output platform-appropriate values, including reduced-motion alternatives as separate CSS custom properties or media query overrides.

### Token Dependency Graph Visualization

Generate a visual dependency graph from the token alias structure to aid debugging and governance:

```javascript
function buildDependencyGraph(tokens) {
  const graph = {};
  Object.entries(tokens).forEach(([name, token]) => {
    const refs = extractAliasReferences(token.$value);
    graph[name] = { references: refs, referencedBy: [] };
  });
  // Back-populate referencedBy
  Object.entries(graph).forEach(([name, node]) => {
    node.references.forEach(ref => {
      if (graph[ref]) graph[ref].referencedBy.push(name);
    });
  });
  return graph;
}
```

Use this graph to:
- Identify high-impact tokens (those with the most `referencedBy` entries) that require extra care during changes.
- Detect orphan tokens (no references, no referencedBy) that may be candidates for removal.
- Visualize the alias chain depth to ensure it stays manageable (3 tiers maximum recommended).

---

## Summary Checklist

Before shipping a design token system, verify:

- [ ] All tokens follow the W3C Design Tokens format with `$value`, `$type`, and `$description`.
- [ ] Naming conventions are documented and enforced via automated linting.
- [ ] Three-tier architecture (global, semantic, component) is established with clear boundaries.
- [ ] All theme variants (light, dark, high-contrast, brand) define the complete semantic token set.
- [ ] Style Dictionary (or equivalent) pipeline produces validated outputs for every target platform.
- [ ] Figma integration sync is configured and tested in both directions.
- [ ] Token documentation is auto-generated and published alongside each release.
- [ ] Versioning follows semver with deprecation periods for breaking changes.
- [ ] Governance process defines ownership, change request workflow, and review criteria.
- [ ] CI pipeline includes contrast validation, alias resolution checks, and visual regression tests.
- [ ] Performance is validated with custom property count limits and scoped property patterns.
- [ ] Migration tooling exists for automated token renames and removals.
