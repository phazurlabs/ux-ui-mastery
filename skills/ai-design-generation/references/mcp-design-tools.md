# MCP Design Tools — Complete Catalog

This reference covers every MCP server relevant to AI-powered design generation. For each tool: capabilities, configuration, tool names, parameters, pricing, strengths, limitations, and best use cases.

---

## 1. Stitch MCP (Google)

### Purpose
Generate complete UI screens, multi-page sites, and design systems from text descriptions. Stitch understands design context (colors, typography, layout patterns) and produces HTML/CSS output that can be previewed, iterated, and converted to production code.

### MCP Configuration
```json
{
  "mcpServers": {
    "stitch": {
      "command": "npx",
      "args": ["-y", "@anthropic/stitch-mcp"]
    }
  }
}
```

### Available Tools

#### `extract_design_context`
Analyzes an existing design (URL, screenshot, or description) to extract design context including colors, typography, layout patterns, component styles, and spacing systems.

**Parameters:**
- `source` (string, required): URL, file path, or detailed text description of existing design
- `extract_colors` (boolean, default true): Extract color palette
- `extract_typography` (boolean, default true): Extract font families, sizes, weights
- `extract_layout` (boolean, default true): Extract grid, spacing, layout patterns
- `extract_components` (boolean, default true): Extract component patterns

**Returns:** A design context object that can be passed to `generate_screen_from_text` for style-consistent generation.

**When to use:** Before generating screens for an existing product, or when the user wants to match a reference design's style.

#### `generate_screen_from_text`
Generates a complete screen from a text description, optionally using design context for style consistency.

**Parameters:**
- `description` (string, required): Detailed description of the screen to generate
- `design_context` (object, optional): Context extracted from `extract_design_context`
- `platform` (string, optional): "web", "ios", "android" — defaults to "web"
- `theme` (string, optional): "light", "dark", "auto" — defaults to "light"
- `viewport` (object, optional): Width and height for the generated screen
- `responsive` (boolean, optional): Generate responsive variants

**Returns:** HTML/CSS output with preview URL, plus metadata about the generated design decisions.

**When to use:** Primary screen generation tool. Use for any single-screen generation task.

#### `build_site`
Generates a multi-page site from a description, maintaining design consistency across all pages.

**Parameters:**
- `description` (string, required): Overall site description
- `pages` (array, required): List of page descriptions with names and content requirements
- `design_context` (object, optional): Context for style consistency
- `navigation` (string, optional): Navigation structure description
- `theme` (string, optional): "light", "dark", "auto"

**Returns:** Multi-page HTML/CSS output with navigation, consistent styling, and preview URLs for each page.

**When to use:** When generating landing pages, marketing sites, or multi-screen app prototypes.

### Strengths
- Full screen generation from text — not just images but interactive HTML/CSS
- Design context awareness — can match existing styles
- Multi-page consistency — maintains design coherence across pages
- Layout intelligence — understands grid systems, responsive patterns
- Real content handling — works with actual content, not just placeholders
- Rapid iteration — can regenerate quickly with adjusted descriptions

### Limitations
- Output is HTML/CSS, not native code (SwiftUI, Jetpack Compose)
- Limited fine-grained style control compared to manual CSS
- Cannot generate complex interactive components (modals, drag-and-drop, charts with live data)
- May not perfectly match very specific brand guidelines without strong design context
- No SVG/vector output for icons or illustrations

### Best Use Cases
- Rapid prototyping of screen concepts
- Landing page generation
- Multi-screen app wireframes and mockups
- Design exploration (generate 3 variants, pick best)
- Converting verbal design ideas into visual screens

### Pricing
API-based, per generation. Check current rates at the Stitch documentation.

---

## 2. Fal.ai MCP

### Purpose
Access 600+ image and video generation models through a single MCP server. This is the most versatile generation MCP — it provides access to models from Google (Imagen 4, Veo 3.1), Black Forest Labs (FLUX), Stability AI (Stable Diffusion), Recraft (V3 vector), and hundreds more.

### MCP Configuration
```json
{
  "mcpServers": {
    "fal-ai": {
      "command": "npx",
      "args": ["-y", "@fal-ai/mcp"],
      "env": {
        "FAL_KEY": "your-fal-api-key"
      }
    }
  }
}
```

### Available Tools

#### `generate_image`
Generates an image using a specified model.

**Parameters:**
- `model` (string, required): Model identifier (e.g., "fal-ai/flux-pro/v1.1", "fal-ai/imagen4", "fal-ai/recraft-v3")
- `prompt` (string, required): Text description of the image to generate
- `negative_prompt` (string, optional): What to exclude from the image
- `image_size` (string, optional): Output dimensions ("landscape_16_9", "square", "portrait_4_3", etc.)
- `num_images` (integer, optional): Number of images to generate (1-4)
- `seed` (integer, optional): Reproducibility seed
- `guidance_scale` (float, optional): How closely to follow the prompt (higher = more literal)
- `style` (string, optional): Model-specific style parameter

**Returns:** Image URL(s), generation metadata, seed used.

#### `list_models`
Lists available models with filtering.

**Parameters:**
- `category` (string, optional): "image", "video", "audio", "text-to-image", "image-to-image"
- `search` (string, optional): Search term to filter models

**Returns:** List of available models with descriptions and capabilities.

#### `get_model_info`
Gets detailed information about a specific model.

**Parameters:**
- `model` (string, required): Model identifier

**Returns:** Model capabilities, supported parameters, pricing, example outputs.

### Key Models for Design Generation

#### FLUX Pro 1.1 (`fal-ai/flux-pro/v1.1`)
- **Type:** Text-to-image
- **Strength:** Best general-purpose image generation. Photorealistic output with excellent prompt following.
- **Best for:** Hero images, product photography, lifestyle imagery, UI screenshots
- **Resolution:** Up to 2048x2048
- **Speed:** ~5-10 seconds per image
- **Design use:** Generate high-quality hero images, background imagery, product shots

#### FLUX Dev (`fal-ai/flux/dev`)
- **Type:** Text-to-image
- **Strength:** Open-source variant of FLUX. Good quality, faster and cheaper than Pro.
- **Best for:** Quick iterations, concept exploration, bulk generation
- **Resolution:** Up to 1024x1024
- **Speed:** ~3-5 seconds per image
- **Design use:** Rapid exploration of visual concepts before committing to Pro quality

#### Imagen 4 (`fal-ai/imagen4`)
- **Type:** Text-to-image (Google)
- **Strength:** Highest-quality photorealistic images. Excellent text rendering within images. Best at understanding complex spatial relationships.
- **Best for:** Product photographs, images with text overlays, realistic scenes, marketing assets
- **Resolution:** Up to 2048x2048
- **Speed:** ~8-15 seconds per image
- **Design use:** Product shots for e-commerce, hero images with text, realistic lifestyle photography

#### Recraft V3 (`fal-ai/recraft-v3`)
- **Type:** Text-to-image with SVG output
- **Strength:** The ONLY model that generates true SVG/vector output. Critical for icons, logos, and scalable graphics.
- **Best for:** Icons, logos, vector illustrations, brand marks, UI icons
- **Output formats:** SVG (vector), PNG
- **Speed:** ~5-8 seconds per image
- **Design use:** Icon sets, logo concepts, vector illustrations, any asset that must scale without quality loss
- **Critical note:** This is the only path to AI-generated vector assets. All other models output raster images only.

#### Veo 3.1 (`fal-ai/veo-3.1`)
- **Type:** Text-to-video (Google)
- **Strength:** Video generation from text descriptions. Up to 8 seconds of video.
- **Best for:** Product demo concepts, motion design references, hero video backgrounds, onboarding animation concepts
- **Resolution:** Up to 1080p
- **Duration:** Up to 8 seconds
- **Speed:** ~30-60 seconds per video
- **Design use:** Motion concept exploration, product demo storyboards, background video for hero sections

#### Stable Diffusion 3.5 (`fal-ai/stable-diffusion-v35`)
- **Type:** Text-to-image
- **Strength:** Open-source, fine-tunable, large community and ecosystem
- **Best for:** Fine-tuned use cases, specialized styles, community models
- **Design use:** When you need a fine-tuned model for a specific visual style

### Strengths
- Massive model variety — 600+ models through one MCP server
- Competitive pricing — often cheaper than direct API access
- Fast inference — optimized infrastructure
- Single API key — access everything with one FAL_KEY
- Model comparison — easy to try different models for same prompt

### Limitations
- Requires FAL_KEY (API key with billing)
- Image output only (except Veo for video) — no HTML/CSS like Stitch
- Model availability can change
- Some models have queue times during peak usage
- Vector output only through Recraft V3

### Best Use Cases
- Any image generation task — route to the best model for the specific need
- Icon generation (via Recraft V3)
- Hero image and photography generation
- Video concept generation (via Veo 3.1)
- Model comparison and A/B testing

### Pricing
Per-model pricing. Generally $0.01-0.10 per image, $0.10-0.50 per video. Check fal.ai/pricing for current rates.

---

## 3. Replicate MCP

### Purpose
Run open-source AI models with support for custom fine-tuned models. Replicate hosts thousands of community models and allows users to deploy their own fine-tuned versions.

### MCP Configuration
```json
{
  "mcpServers": {
    "replicate": {
      "command": "npx",
      "args": ["-y", "replicate-mcp"],
      "env": {
        "REPLICATE_API_TOKEN": "your-replicate-token"
      }
    }
  }
}
```

### Available Tools

#### `run_model`
Runs a model on Replicate.

**Parameters:**
- `model` (string, required): Model identifier (owner/name:version)
- `input` (object, required): Model-specific input parameters

#### `list_models`
Lists and searches available models.

#### `get_model`
Gets details about a specific model.

### Key Models for Design
- FLUX variants (schnell, dev, pro)
- Stable Diffusion XL and variants
- Custom fine-tuned models (brand-specific, style-specific)
- Image upscaling models (Real-ESRGAN)
- Background removal models (RemBG)
- Style transfer models

### Strengths
- Custom fine-tuned model support — train on your brand's visual style
- Large community model ecosystem
- Pay-per-use pricing (no idle costs)
- Model versioning and reproducibility
- Image utility models (upscale, remove background, style transfer)

### Limitations
- Cold start times for less popular models
- Quality varies widely across community models
- More complex model selection (thousands of options)
- No vector/SVG output

### Best Use Cases
- Running custom fine-tuned models trained on brand assets
- Image utility operations (upscale, background removal, style transfer)
- Accessing specialized community models
- Reproducible generation with pinned model versions

### Pricing
Per-second GPU billing. Typical image generation: $0.01-0.05. Check replicate.com/pricing.

---

## 4. OpenAI GPT-Image / DALL-E MCP

### Purpose
Access OpenAI's image generation models (GPT-Image-1, DALL-E 3) through MCP. Known for strong prompt comprehension, good text rendering in images, and consistent artistic style.

### MCP Configuration
```json
{
  "mcpServers": {
    "openai-images": {
      "command": "npx",
      "args": ["-y", "openai-images-mcp"],
      "env": {
        "OPENAI_API_KEY": "your-openai-key"
      }
    }
  }
}
```

### Available Tools

#### `generate_image`
Generates an image using GPT-Image-1 or DALL-E 3.

**Parameters:**
- `prompt` (string, required): Description of the image to generate
- `model` (string, optional): "gpt-image-1" or "dall-e-3" — defaults to latest
- `size` (string, optional): "1024x1024", "1024x1792", "1792x1024"
- `quality` (string, optional): "standard", "hd"
- `style` (string, optional): "natural", "vivid"
- `n` (integer, optional): Number of images (1-4 for DALL-E 3)

#### `edit_image`
Edits an existing image based on a text description (inpainting/outpainting).

**Parameters:**
- `image` (string, required): URL or base64 of the image to edit
- `prompt` (string, required): Description of the edit to make
- `mask` (string, optional): Mask indicating areas to edit

### Strengths
- Excellent prompt comprehension — understands complex, nuanced descriptions
- Strong text rendering in images — better than most models at including readable text
- Consistent artistic quality across generations
- Image editing (inpainting) capability — modify specific regions of existing images
- Reliable and well-documented API

### Limitations
- Fewer model options than Fal.ai (only GPT-Image-1 and DALL-E 3)
- No vector/SVG output
- No video generation
- Higher pricing than some alternatives
- Content policy restrictions can block some design-related prompts

### Best Use Cases
- Illustrations for UI (empty states, onboarding, feature highlights)
- Concept art and mood board imagery
- Images that need readable text embedded
- Lifestyle photography with specific compositions
- Image editing and modification (change background, modify elements)

### Pricing
DALL-E 3: $0.040-0.080 per image depending on size and quality. GPT-Image-1: check current OpenAI pricing.

---

## 5. Figma MCP (Official)

### Purpose
Read and write Figma design files programmatically. This MCP connects to Figma's official API, enabling design extraction, component analysis, and design-to-code workflows.

### MCP Configuration
```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@anthropic/figma-mcp"],
      "env": {
        "FIGMA_ACCESS_TOKEN": "your-figma-token"
      }
    }
  }
}
```

### Available Tools

#### `get_file`
Retrieves a complete Figma file with all pages, frames, and components.

**Parameters:**
- `file_key` (string, required): Figma file key (from URL)
- `depth` (integer, optional): How deep to traverse the node tree

#### `get_file_nodes`
Retrieves specific nodes from a Figma file.

**Parameters:**
- `file_key` (string, required): Figma file key
- `ids` (array, required): Node IDs to retrieve

#### `get_images`
Exports images from Figma nodes.

**Parameters:**
- `file_key` (string, required): Figma file key
- `ids` (array, required): Node IDs to export as images
- `format` (string, optional): "png", "jpg", "svg", "pdf"
- `scale` (number, optional): Export scale (1x, 2x, 3x)

#### `post_comment`
Posts a comment on a Figma file.

**Parameters:**
- `file_key` (string, required): Figma file key
- `message` (string, required): Comment text
- `client_meta` (object, optional): Position coordinates for the comment

#### `get_file_styles`
Retrieves all styles (colors, text, effects) defined in a Figma file.

#### `get_file_components`
Retrieves all components and component sets defined in a Figma file.

### Strengths
- Direct access to design files — read actual design specifications
- Component extraction — understand design system components
- Style extraction — pull colors, typography, effects from Figma
- Image export — export any layer as PNG, JPG, SVG, or PDF
- Design-to-code bridge — extract specs needed for implementation
- Comment integration — annotate designs programmatically

### Limitations
- Read-heavy — writing back to Figma is limited compared to reading
- Requires Figma access token with appropriate permissions
- Large files can be slow to retrieve (use node-specific endpoints)
- Cannot create new files — only read and annotate existing ones
- Does not generate designs — it reads existing ones

### Best Use Cases
- Extracting design specifications for code implementation
- Analyzing existing design systems (components, styles, tokens)
- Exporting assets from Figma for use in projects
- Design audit — programmatically check design file quality
- Creating design context (from Figma) for use with Stitch generation

### Pricing
Figma API is free with a Figma account. Rate limits apply (check Figma API docs).

---

## Tool Selection Matrix

Use this matrix to route generation tasks to the best available MCP tool.

| Task | Best Tool | Fallback | Notes |
|------|-----------|----------|-------|
| Full UI screen from text | Stitch | FLUX Pro (as screenshot) | Stitch outputs HTML/CSS; FLUX outputs image only |
| Multi-page site | Stitch (build_site) | Manual | Only Stitch handles multi-page consistency |
| App icon (SVG) | Recraft V3 (via Fal.ai) | Manual SVG | Recraft is the ONLY vector-capable model |
| Icon set (batch SVG) | Recraft V3 (via Fal.ai) | Manual SVG | Generate with consistent style prompt |
| UI illustrations | GPT-Image (OpenAI) | FLUX Pro (Fal.ai) | OpenAI better for stylized illustration |
| Product photographs | Imagen 4 (via Fal.ai) | FLUX Pro (Fal.ai) | Imagen 4 is highest photorealism |
| Hero images | FLUX Pro (via Fal.ai) | Imagen 4 (Fal.ai) | FLUX Pro best general-purpose |
| Images with text | Imagen 4 or GPT-Image | — | Both handle text well |
| Video/motion concepts | Veo 3.1 (via Fal.ai) | — | Only video-capable tool |
| Design system extraction | Figma MCP | Manual | Reads Figma files directly |
| Design context extraction | Stitch (extract_design_context) | Figma MCP | Stitch analyzes any design |
| Wireframes | Stitch | Manual | Fast low-fidelity generation |
| Background removal | Replicate (RemBG) | Manual | Utility model on Replicate |
| Image upscaling | Replicate (Real-ESRGAN) | — | Utility model on Replicate |
| Custom fine-tuned style | Replicate | Fal.ai | Replicate supports custom models |
| Image editing/inpainting | GPT-Image (edit_image) | — | Only tool with edit capability |

## MCP Detection Protocol

When Sumi runs a generation command, follow this protocol:

### Step 1: Detect Available MCP Servers
Check which MCP servers are connected in the current session. The available tools will indicate which servers are active.

### Step 2: Route to Best Available Tool
Using the Tool Selection Matrix above, identify the best tool for the task. If the best tool is not available, use the fallback.

### Step 3: Handle No-MCP Gracefully
If no generation MCP servers are available, Sumi should:
1. Acknowledge that no generation tools are connected
2. Provide a complete, detailed specification that the user can use manually
3. Include the exact prompt they would use with each tool
4. Suggest which MCP server(s) to install for their use case
5. Offer to proceed with design guidance using Sumi's other skills

### Step 4: Never Fail Silently
Always tell the user:
- Which MCP tool was selected and why
- What model is being used (for Fal.ai)
- What the generation will cost (approximate)
- What the expected output quality is
- How to iterate if the result is not satisfactory

## Multi-MCP Coordination

When multiple MCP servers are available, coordinate them for richer output:

### Screen + Assets Pipeline
1. Use Stitch to generate the screen layout
2. Use Recraft V3 (Fal.ai) to generate icons referenced in the screen
3. Use FLUX Pro or Imagen 4 (Fal.ai) to generate hero images
4. Use Figma MCP to export existing brand assets if available

### Design Extraction + Generation Pipeline
1. Use Figma MCP to extract design context from existing Figma files
2. Convert Figma styles into a design context object
3. Pass that context to Stitch for style-consistent screen generation
4. Score the generated screen against the Figma original

### Iterative Refinement Pipeline
1. Generate v1 with any tool
2. Score against the 10-dimension visual framework
3. Identify weakest dimensions
4. Adjust prompt to target weak dimensions
5. Regenerate v2
6. Repeat until quality gate is passed (max 3 iterations)
