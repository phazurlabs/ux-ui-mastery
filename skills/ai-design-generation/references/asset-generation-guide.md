# Asset Generation Guide

This reference covers generating specific design asset types with AI tools. Each asset type has a best tool, prompt strategy, output format requirements, quality checklist, and production-readiness criteria.

---

## Icons (SVG / Vector)

### Best Tool
**Recraft V3** (via Fal.ai MCP) — the ONLY AI model that generates true SVG/vector output. All other image generation models produce raster images (PNG/JPG) that cannot scale without quality loss.

### Why Vector Matters for Icons
Icons are displayed at multiple sizes (16px in menus, 24px in toolbars, 32px in cards, 48px in feature sections). Raster icons become blurry when scaled. SVG icons remain crisp at any size. For production use, SVG is the only acceptable format for UI icons.

### Prompt Strategy

**Base template:**
```
[Style] icon depicting [subject], [grid]px grid,
[stroke]px stroke width, rounded line caps and joins.
Single color: [hex color]. Clean, minimal, geometric.
Recognizable at 16px. No fine detail that would be lost at small sizes.
Professional quality, suitable for a [sector] application.
```

**Style variants:**

Outlined (most versatile):
```
Minimal outlined icon depicting [subject]. 24x24 pixel grid,
1.5px consistent stroke width, rounded line caps and rounded joins.
Single color #0F172A. Open shapes, clean negative space.
No fills, strokes only. Recognizable at 16px.
```

Filled:
```
Solid filled icon depicting [subject]. 24x24 pixel grid.
Single color #0F172A. Geometric shapes, clean silhouette.
No stroke, filled shapes only. Recognizable at 16px.
Clear silhouette distinction from background.
```

Two-tone:
```
Two-tone icon depicting [subject]. 24x24 pixel grid.
Primary color #0F172A for outlines and key shapes.
Secondary color #E2E8F0 (20% opacity fill) for background shapes.
1.5px stroke width for outlines. Rounded caps and joins.
```

Duotone:
```
Duotone icon depicting [subject]. 24x24 pixel grid.
Primary layer: #0F172A (full shapes).
Secondary layer: #6366F1 at 30% opacity (accent fills).
Clean, modern, geometric. Professional SaaS style.
```

### Grid Specifications
| Use Case | Grid | Stroke | Padding |
|----------|------|--------|---------|
| Inline text (menus, labels) | 16x16 | 1px | 1px |
| Toolbar / nav | 20x20 | 1.25px | 1.5px |
| Default UI | 24x24 | 1.5px | 2px |
| Cards / features | 32x32 | 2px | 2px |
| Hero / large display | 48x48 | 2.5px | 3px |

### Batch Icon Generation
Generate consistent icon sets by using the same prompt prefix for every icon:

```
Style prefix (use for ALL icons in the set):
"Minimal outlined icon, 24x24 pixel grid, 1.5px stroke width,
rounded line caps and joins, single color #0F172A, clean geometric
shapes, recognizable at 16px. Icon depicts: "

Then append each icon's subject:
- "...a house (home navigation)"
- "...a magnifying glass (search)"
- "...a gear/cog (settings)"
- "...a bell (notifications)"
- "...a person silhouette (profile/account)"
- "...an envelope (messages/email)"
- "...a bar chart (analytics/dashboard)"
- "...a plus sign in a circle (add/create new)"
- "...a trash can (delete)"
- "...a pencil (edit)"
```

### Quality Checklist for Icons
- [ ] Consistent stroke width across the entire set (measure visually)
- [ ] Pixel-aligned on the target grid (no half-pixel strokes)
- [ ] Recognizable at smallest intended display size (16px test)
- [ ] Works on both light and dark backgrounds (test both)
- [ ] SVG output is clean (no unnecessary groups, transforms, or paths)
- [ ] No fine detail that creates visual noise at small sizes
- [ ] Consistent visual weight across the set (no icon looks heavier/lighter)
- [ ] Consistent corner radius (all rounded or all sharp, not mixed)
- [ ] Consistent metaphor language (same conceptual style across set)
- [ ] Optical alignment (icons appear centered even if mathematically offset)

### SVG Optimization Post-Generation
After generating SVGs with Recraft V3:
1. Run through SVGO (SVG Optimizer) to remove metadata and simplify paths
2. Ensure viewBox is set correctly (0 0 24 24 for 24px grid)
3. Remove any hardcoded width/height attributes (use viewBox for scaling)
4. Ensure fill or stroke uses currentColor for theme-ability
5. Test rendering in browser at 1x, 2x, and 3x pixel densities

### Fallback Without MCP
If Recraft V3 is not available via MCP:
1. Describe each icon in precise detail
2. Suggest existing open-source icon sets that match the style (Lucide, Phosphor, Heroicons, Tabler)
3. Provide SVG specifications for manual creation
4. Recommend Figma icon plugins for generation

---

## Illustrations

### Best Tools
- **GPT-Image (OpenAI MCP)**: Best for stylized, artistic illustrations with specific compositions
- **FLUX Pro (Fal.ai MCP)**: Best for photorealistic or highly detailed illustrations
- **Imagen 4 (Fal.ai MCP)**: Best for illustrations that include readable text

### Illustration Styles for UI

**Flat vector:**
```
Flat vector illustration of [subject]. Minimal geometric shapes,
no gradients, no shadows, no 3D. Color palette: [3-4 hex colors].
Clean edges, bold shapes. White background.
Style: modern tech company illustration (like Stripe or Notion).
No outlines unless part of the design language.
[Size/aspect ratio] suitable for use as [empty state / onboarding step / feature highlight].
```

**Isometric:**
```
Isometric illustration of [subject]. Clean geometric shapes,
consistent isometric angle (30 degrees). Color palette: [colors].
Subtle shadows for depth. Light background.
Professional, modern, technical style.
No perspective distortion, strict isometric projection.
```

**3D rendered / clay style:**
```
3D rendered illustration of [subject], clay/plastic material style.
Soft studio lighting, gentle shadows. Color palette: [colors].
Rounded shapes, smooth surfaces. Pastel or muted tones.
Modern, friendly, approachable style similar to Apple Memoji aesthetic.
White or light gradient background. No harsh shadows.
```

**Line art:**
```
Continuous line drawing illustration of [subject].
Single line weight: 2px. Color: [hex color].
Minimal, abstract, elegant. White background.
No fills, line work only. Artistic but professional.
```

**Abstract geometric:**
```
Abstract geometric composition using [shapes: circles, rectangles, triangles].
Color palette: [colors]. No representational imagery.
Modern, minimal, balanced composition. Suitable for decorative use
in [hero section / card background / section divider].
```

### Common UI Use Cases for Illustrations

| Use Case | Best Style | Size | Notes |
|----------|-----------|------|-------|
| Empty state | Flat vector or line art | 200-300px wide | Should be small, not dominate |
| Onboarding step | Flat vector or 3D clay | 300-400px wide | Should explain the step's concept |
| Feature highlight | Isometric or flat vector | 200-300px wide | Should visualize the feature |
| Error page (404, 500) | Flat vector or line art | 300-400px wide | Should be friendly, not alarming |
| About page | Any style | Varies | Match brand personality |
| Hero section | Abstract or flat vector | Full width | Should not compete with headline |
| Loading/processing | Simple line art | 100-150px | Minimal, should loop as animation reference |

### Consistency Across Illustration Sets
When generating multiple illustrations for one project:
1. Use the same style prefix for every prompt
2. Use the same color palette (exactly 3-5 colors)
3. Use the same line weight if line-based
4. Use the same level of detail/complexity
5. Generate all in one session if possible (maintains context)
6. Review the set together (not individually) for coherence

### Quality Checklist for Illustrations
- [ ] Style consistent with the app's visual language
- [ ] Colors match design token palette exactly (not approximately)
- [ ] Works at multiple sizes (responsive — test at 50% and 200%)
- [ ] Not too detailed (should not compete with UI elements for attention)
- [ ] Inclusive representation (if humans are depicted)
- [ ] No AI artifacts (extra limbs, distorted faces, impossible geometry)
- [ ] Clear concept communication (viewer understands what it represents)
- [ ] Works on the intended background color (light and dark if needed)
- [ ] File size optimized (compressed PNG/WebP, not uncompressed)
- [ ] Aspect ratio appropriate for the layout position

---

## Photographs

### Best Tools
- **Imagen 4 (Fal.ai MCP)**: Highest photorealism, excellent text rendering, best for product and lifestyle photography
- **FLUX Pro (Fal.ai MCP)**: Excellent general-purpose, good for stylized photography
- **GPT-Image (OpenAI MCP)**: Good for specific compositions, supports image editing

### Photograph Types for UI

**Product photography:**
```
Professional product photograph of [product].
Studio lighting: soft key light from upper left, fill light from right,
subtle rim light. [White / gradient / lifestyle] background.
Sharp focus on product, shallow depth of field for lifestyle shots.
4K resolution, commercial quality. Color temperature: [warm/neutral/cool].
Clean, minimal composition. [Product angle: front / three-quarter / flat lay].
```

**Lifestyle photography:**
```
Lifestyle photograph of [scene description].
Natural lighting, golden hour warmth. [Setting description].
[People: age, diversity, activity, expression].
Editorial quality, authentic feel, not stock-photo-posed.
Color palette harmony with [hex colors from design system].
Rule of thirds composition. Medium depth of field.
```

**Hero imagery:**
```
Cinematic wide-angle photograph for [website/app] hero section.
[Subject description]. [Mood: inspiring / calm / energetic / professional].
16:9 aspect ratio, suitable for full-width hero banner.
Color temperature matching design palette: [warm/cool/neutral].
Slightly desaturated for text overlay readability.
High resolution, sharp, professional quality.
```

**Avatar/profile placeholders:**
```
Professional headshot portrait of a [description] person.
Studio lighting, neutral background (#F5F5F5).
Friendly, approachable expression. Sharp focus on face.
Square aspect ratio (1:1). Diverse representation.
Clean, simple, suitable for a profile avatar at 48-128px display size.
```

### Important Considerations
- **Disclosure**: AI-generated photos may require disclosure in some jurisdictions. Consider adding metadata or disclosure text where legally required.
- **Diversity**: When generating people, explicitly request diverse representation. Generate sets that include varied ages, ethnicities, and abilities.
- **Ethical use**: Do not generate photos that could be mistaken for real individuals in contexts where this would be misleading (testimonials, team pages, reviews).
- **Consistency**: For a set of photos (like a team page), generate all with the same lighting, background, and color temperature.

### Quality Checklist for Photographs
- [ ] No AI artifacts (extra fingers, distorted faces, impossible text, weird backgrounds)
- [ ] Appropriate resolution for display size (1x minimum, 2x for retina)
- [ ] Color temperature matches the app's design palette
- [ ] Inclusive and diverse representation (if showing people)
- [ ] Ethical use verified (not misleading about real people)
- [ ] Composition supports the intended layout (hero, card, avatar, etc.)
- [ ] File format and compression optimized (WebP preferred, JPEG fallback)
- [ ] Alt text prepared for accessibility
- [ ] Works with text overlays (if hero image — sufficient contrast/blur areas)
- [ ] Consistent with other photos in the set (lighting, mood, saturation)

---

## Video / Motion

### Best Tool
**Veo 3.1** (via Fal.ai MCP) — Google's video generation model. Currently the only production-quality text-to-video model available via MCP.

### Video Types for UI

**Product demo concept:**
```
Smooth product demo video showing a [app type] application.
Screen recording style: cursor moving through the interface,
clicking buttons, scrolling content. Clean desktop background.
Professional, polished. 4-6 seconds duration.
[Platform] interface. Static camera, no zoom or pan.
```

**Hero background video:**
```
Ambient background video for a [product type] website hero section.
[Abstract / nature / technology] theme. Slow, smooth movement.
Desaturated colors compatible with text overlay.
Seamless loop potential (start and end frames should be similar).
6-8 seconds duration. No text, no UI elements.
[Color mood matching design palette].
```

**Onboarding animation concept:**
```
Animated illustration showing [concept] for an onboarding step.
[Flat / 3D / isometric] style matching the app's illustration language.
Smooth transition from [state A] to [state B].
4-5 seconds duration. White background.
Color palette: [hex colors]. Clean, simple motion.
```

**Micro-interaction reference:**
```
UI micro-interaction animation: [interaction description].
Example: button press with ripple effect, card expand animation,
toggle switch flipping, loading spinner, success checkmark animation.
Close-up view, dark background, [accent color] element.
2-3 seconds, smooth 60fps feel. For reference/inspiration only.
```

### Limitations
- Maximum 8 seconds per generation
- May not perfectly match your exact UI design
- Best used as concept/reference, not production assets
- Cannot generate interactive or conditional animations
- Quality varies — expect 2-3 generations to get a good result

### Quality Checklist for Video
- [ ] Smooth motion throughout (no jitter, no frame drops)
- [ ] Consistent style frame-to-frame (no style flickering)
- [ ] Appropriate duration for the intended use
- [ ] Color palette matches the design system
- [ ] No visual artifacts or distortions
- [ ] Compressed for web delivery (WebM primary, MP4 fallback)
- [ ] Accessible: any information conveyed by video is also available as text
- [ ] Does not autoplay with sound (or is muted by default)
- [ ] Poster frame (first frame) is visually representative
- [ ] File size acceptable for web delivery (under 5MB for hero backgrounds)

---

## Patterns and Textures

### Best Tools
- **FLUX Pro (Fal.ai MCP)**: Best for complex patterns and textures
- **Imagen 4 (Fal.ai MCP)**: Good for photorealistic textures

### Pattern Types for UI

**Seamless tileable patterns:**
```
Seamless tileable pattern: [description].
[Geometric / organic / abstract] shapes. Color palette: [colors].
Minimal, subtle. Suitable for background use at low opacity.
Must tile seamlessly in both X and Y directions.
Clean, professional, modern design aesthetic.
```

**Noise and grain overlays:**
```
Subtle noise texture overlay. Fine grain, uniform distribution.
Monochromatic (grayscale). Tileable seamlessly.
Very subtle — should be barely visible at 5-10% opacity.
Use: overlay on solid color backgrounds for warmth and depth.
512x512 pixels, high resolution.
```

**Gradient meshes:**
```
Smooth gradient mesh background. Colors: [hex colors].
Organic, flowing color transitions. No hard edges.
Abstract, ambient, modern. Full bleed, edge-to-edge color.
Suitable for hero section background or card accent.
16:9 aspect ratio for hero use, 1:1 for card use.
```

### Export and Usage
- Export as WebP for raster patterns (best compression)
- Set as CSS background-image with background-repeat: repeat for tiles
- Apply with low opacity (5-15%) over solid backgrounds for subtle texture
- Test tiling in browser to verify seamless edges
- Provide fallback solid color for slow connections

---

## Brand Assets

### Logos
- **Generation tool**: Recraft V3 for SVG vector concepts
- **Important**: AI-generated logos are starting points, not final deliverables
- **Workflow**: Generate 5-10 concepts, select best direction, refine manually in vector editor
- **Prompt**: "Modern minimalist logo mark for [brand name], a [description]. Geometric, clean, memorable. Single color #0F172A. Simple enough to work at 16px favicon size."
- **Post-generation**: Always refine manually — AI logos need human design judgment for balance, uniqueness, and trademark viability

### App Icons
- **Generation tool**: Imagen 4 or FLUX Pro for concept, then recreate in vector
- **Prompt**: "Mobile app icon for [app name], a [description]. [Style: flat / gradient / 3D]. [Color palette]. Square with rounded corners (iOS: 60px radius on 1024x1024). Simple, recognizable, no text. Single focal element."
- **Sizes needed**: 1024x1024 (source), automatically generate iOS and Android required sizes
- **Post-generation**: Recreate winning concept in vector for production

### Social Media Graphics
- **Generation tool**: FLUX Pro or Imagen 4 with brand colors
- **Sizes**: OG image (1200x630), Twitter card (1200x600), Instagram (1080x1080)
- **Prompt**: Include brand colors, font, and layout constraints for each platform
- **Consistency**: Generate all social assets in one session with same style prefix

### OG (Open Graph) Images
- **Template approach**: Generate a background pattern/image, overlay text programmatically
- **Prompt**: "Abstract background for social share image. Colors: [brand palette]. [Geometric / gradient / texture] style. Space for large text overlay in center. 1200x630 pixels. Subtle, not competing with text."
- **Text overlay**: Add programmatically with correct font, not in the AI generation

---

## Production-Readiness Checklist (All Asset Types)

Before any AI-generated asset enters production, verify:

### Format and Optimization
- [ ] Correct file format chosen (SVG for vectors, WebP for images, MP4/WebM for video)
- [ ] File size optimized (run through appropriate compression tool)
- [ ] Appropriate resolution for target display (1x minimum, 2x for retina-critical elements)
- [ ] Responsive variants generated if needed (multiple sizes or scalable format)

### Accessibility
- [ ] Alt text written (descriptive for informative images, empty for decorative)
- [ ] Decorative vs. informative classification determined
- [ ] Sufficient contrast if the asset contains meaningful visual information
- [ ] No information conveyed solely through color
- [ ] Video/motion has text alternative or captions if informative

### Theme Compatibility
- [ ] Works in light mode
- [ ] Works in dark mode (if app supports dark mode)
- [ ] Color-safe for color vision deficiency (test with simulator)
- [ ] Works on the intended background colors

### Legal and Ethical
- [ ] AI generation usage rights understood (check model's terms of service)
- [ ] Disclosure added if required by jurisdiction or platform policy
- [ ] No unintentional likeness to real individuals (for generated people)
- [ ] No copyrighted material reproduced (brand logos, characters, etc.)
- [ ] Diverse and inclusive representation (for assets depicting people)

### Performance
- [ ] Lazy loading implemented for below-fold images
- [ ] Appropriate decoding attribute set (async for non-critical images)
- [ ] srcset/sizes attributes set for responsive images
- [ ] Video set to not autoplay (or autoplay muted with controls available)
- [ ] Total page weight with all assets is within performance budget
- [ ] CDN delivery configured for production assets
