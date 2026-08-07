---
name: figma-to-code
description: Generate production code from a Figma design specification using the MCP-powered design-to-code flywheel. Extracts tokens, components, and layout to produce platform-ready code.
argument-hint: "[Figma URL or design spec] [target platform]"
---

# Figma to Code Command

## Before running

This command needs a Figma URL or design spec, and the target platform.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target, do not audit a hypothetical interface, and do not produce generic advice in place of the real analysis — an audit of something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.

Transform a Figma design specification into production-ready code using the design-to-code flywheel. This command bridges the gap between design intent and engineering implementation.

## Pipeline Protocol

1. **Ingest the design specification**: Accept Figma design input in any available form.
   - Figma file URL or frame/component link
   - Figma MCP server data (if MCP connection available)
   - Pasted design spec (dimensions, colors, typography, spacing, assets)
   - Screenshot with design annotations
   - Exported Figma Dev Mode properties

2. **Extract design tokens**: Parse the design into structured tokens.
   - **Color**: Map fills, strokes, and effects to semantic color tokens
   - **Typography**: Extract font family, size, weight, line-height, letter-spacing into type scale tokens
   - **Spacing**: Identify padding, margin, and gap values; map to spacing scale
   - **Elevation**: Parse shadows into elevation tier tokens
   - **Border radius**: Extract corner radius values into shape tokens
   - **Layout**: Identify auto-layout direction, gap, padding, alignment
   - Output tokens in W3C Design Tokens format (JSON) and platform-specific formats

3. **Identify component structure**: Decompose the design into a component tree.
   - Map Figma layers to semantic HTML elements
   - Identify reusable components vs. one-off layouts
   - Detect component variants (size, state, type) from Figma component properties
   - Map Figma auto-layout to CSS Flexbox/Grid or SwiftUI stacks
   - Identify interactive states from Figma component sets

4. **Generate platform code**: Produce implementation for the target platform.

   **React/TypeScript (default)**:
   - Functional components with typed props
   - CSS Modules, Tailwind, or styled-components (match project convention)
   - Responsive layout using container queries where beneficial
   - Design token consumption via CSS custom properties

   **SwiftUI**:
   - Native SwiftUI views with proper stack composition
   - Dynamic Type support
   - iOS 26 Liquid Glass materials where the design uses translucency
   - Color assets for light/dark mode

   **HTML/CSS**:
   - Semantic HTML structure
   - Modern CSS with custom properties, logical properties, and grid/flexbox
   - Responsive breakpoints or container queries

5. **Validate accessibility**: Check generated code against WCAG requirements.
   - Semantic element selection (not div soup)
   - ARIA attributes for non-standard patterns
   - Color contrast verification against extracted tokens
   - Focus order matching visual layout
   - Touch target sizing (44x44pt minimum)

6. **Generate handoff documentation**: Produce specification notes.
   - Token mapping table (Figma layer -> token name -> CSS property)
   - Responsive behavior notes
   - Interaction specifications (hover, focus, active states)
   - Animation specifications if applicable
   - Known deviations from design with rationale

## Output Format

```
## Figma to Code: [Component/Screen Name]

### Design Token Extraction
[W3C format JSON tokens extracted from the design]

### Component Tree
[Hierarchical breakdown of components identified]

### Generated Code

#### React/TypeScript
[Complete component code with tokens]

#### CSS
[Stylesheet with custom properties]

### Accessibility Validation
- [ ] Semantic HTML elements used
- [ ] ARIA attributes applied where needed
- [ ] Color contrast passes AA (4.5:1 text, 3:1 UI)
- [ ] Focus indicators visible
- [ ] Touch targets >= 44x44pt

### Handoff Notes
[Token mapping, responsive behavior, interaction specs, deviations]

### Design-Code Fidelity Checklist
- [ ] Colors match design tokens (within 1% tolerance)
- [ ] Typography matches type scale
- [ ] Spacing matches spatial system
- [ ] Layout matches auto-layout spec
- [ ] Border radius matches shape tokens
- [ ] Elevation/shadow matches design
```

## Cross-References
When generating code from design, draw patterns from:
- `figma-design-tool-workflows` skill for Figma MCP integration, Code Connect, and Dev Mode
- `component-patterns-code` skill for platform-specific component patterns
- `design-systems-architecture` skill for token architecture and Style Dictionary pipeline
- `accessibility-inclusive-design` skill for WCAG validation
- `ui-visual-design-system` skill for visual system integrity
- `cross-cultural-i18n-ux` skill for RTL/i18n layout considerations
