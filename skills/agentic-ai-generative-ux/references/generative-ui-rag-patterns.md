# Generative UI and RAG Interface Design Patterns

This reference covers the core design patterns, frameworks, and platform guidelines for building interfaces where AI generates, adapts, or augments the user interface in real time. Apply these patterns when designing retrieval-augmented generation experiences, agent-driven UIs, multimodal output rendering, and AI-native interaction flows.

---

## Google A2UI Framework

### Agent-to-UI Interoperability

Google's Agent-to-UI (A2UI) framework defines a structured interoperability format that enables AI agents to generate user interface components dynamically. Rather than treating AI output as raw text piped into a chat bubble, A2UI establishes a message protocol where agents declare the UI they need rendered and the host application translates those declarations into native components.

### Message Format and Component Specification

The A2UI message format uses a JSON-based schema where each agent response contains a `ui` block alongside the standard `text` content. This block declares components by type, binds data to them, and specifies layout intent.

```json
{
  "response": {
    "text": "Here are the top 3 flights matching your criteria.",
    "ui": {
      "layout": "card-list",
      "components": [
        {
          "type": "flight-card",
          "data": {
            "airline": "United",
            "departure": "SFO 8:00 AM",
            "arrival": "JFK 4:35 PM",
            "price": "$342"
          },
          "actions": [
            { "label": "Book", "action": "book_flight", "params": { "id": "UA-1234" } },
            { "label": "Details", "action": "show_details", "params": { "id": "UA-1234" } }
          ]
        }
      ]
    }
  }
}
```

### Bridging AI Output to Structured Rendering

Design the bridge layer between AI output and structured UI rendering with three responsibilities:

1. **Parse** the A2UI message and validate each component type against a registry of supported components.
2. **Map** declared component types to platform-native implementations (e.g., `flight-card` resolves to a SwiftUI `FlightCardView` on iOS, a Material `FlightCard` composable on Android).
3. **Fallback** gracefully when the agent declares a component the host does not support. Render a generic card with the raw data fields rather than failing silently.

Register every supported component type in a component registry. When the agent references an unregistered type, log a warning, render the fallback, and surface an indicator to the user that the display is simplified.

### A2UI Implementation Considerations

Treat A2UI as a contract between the agent layer and the rendering layer. Version the schema so that older host applications gracefully ignore new component types introduced in later agent versions. Include a `min_version` field in each component declaration so the renderer knows whether it can handle the component or must fall back.

Implement action handlers as a bidirectional channel. When the user clicks "Book" on a flight card, the host application sends an action event back to the agent with the action name and parameters. The agent then processes the action and may respond with a new UI declaration (e.g., a booking confirmation form). This round-trip pattern keeps the agent in control of the workflow while the host controls rendering.

Support partial updates so the agent can modify a single component within an existing layout without re-rendering the entire response. Use component IDs to target updates. This reduces flicker and preserves scroll position during multi-step interactions.

---

## Three UI Paradigms: Conversational vs Instructed vs Generative

### Conversational UI

Use conversational UI when users explore open-ended questions, need clarification, or the task is inherently ambiguous. Chat-based interfaces excel at progressive refinement where the user and AI iterate toward a goal through natural language turns.

**When to use:**
- Simple factual queries and Q&A
- Exploratory research where the user refines intent over multiple turns
- Emotional or subjective domains (therapy bots, journaling)
- Tasks where ambiguity is expected and clarification is part of the process

**Limitations:**
- Complex structured data (tables, comparisons) renders poorly in chat bubbles
- Users cannot scan or compare multiple options efficiently
- Long conversations lose context for the user even if the model retains it
- High cognitive load for tasks that require spatial reasoning or side-by-side evaluation

### Instructed UI

Instructed UI uses pre-designed, deterministic components that the AI triggers based on context. The interface is authored by designers ahead of time; the AI decides which components to show and what data to populate them with.

**When to use:**
- Known, repeatable task patterns (booking flows, form completion, dashboards)
- Domains with strict regulatory or brand requirements
- When consistency and predictability matter more than flexibility
- Structured tasks where the optimal UI is well understood

**Example:** A banking assistant that always renders a `TransactionTable` component when the user asks about recent charges. The component is pre-built; the AI supplies the data and the trigger condition.

### Generative UI

Generative UI means the AI produces the interface structure itself, assembling components, layouts, and data bindings on the fly. Evaluations of generative interfaces for language models (arXiv:2508.19227) report **preference margins reaching 72%** for generative over conversational interfaces in task-completion scenarios, particularly when the task involved variable data structures or personalization requirements.

**When to use:**
- Variable tasks where the optimal display depends on runtime data shape
- Personalization-heavy experiences where each user sees a different interface
- Rapid prototyping and internal tools where pre-designing every screen is impractical
- Scenarios where data schema varies (e.g., comparing hotels vs flights vs restaurants with different attributes)

**Risks to mitigate:**
- Constrain generation to a vetted component library (see Design System Integration below)
- Validate accessibility of every generated layout before rendering
- Provide deterministic fallbacks for critical user flows

### Decision Matrix

Use the following matrix to select the appropriate paradigm based on task complexity and task variability:

| | **Low Variability** | **Medium Variability** | **High Variability** |
|---|---|---|---|
| **Low Complexity** | Conversational UI | Conversational UI | Instructed UI |
| **Medium Complexity** | Instructed UI | Instructed UI | Generative UI |
| **High Complexity** | Instructed UI | Generative UI | Generative UI |

Apply this matrix as a starting heuristic. Override it when domain constraints (regulation, accessibility mandates, brand consistency) demand tighter control.

---

## Outcome-Oriented Design

### Designing for Outcomes, Not Layouts

Nielsen Norman Group's outcome-oriented design principle directs designers to specify the *outcome* the user needs rather than the specific layout to render. Define what the user should accomplish or understand. Let the AI system determine the optimal presentation given the user's context, device, data shape, and interaction history.

### Outcome Specification Format

Express outcomes as structured goal declarations:

```yaml
outcome:
  goal: "user_compares_options"
  data_type: "product_list"
  constraints:
    max_items: 5
    required_fields: ["name", "price", "rating", "image"]
  user_context:
    device: "mobile"
    expertise: "novice"
    time_pressure: "high"
```

### Adaptive Rendering by Context

The same outcome renders differently depending on context. Consider the outcome "user compares three health insurance plans":

| Context | Rendered UI |
|---|---|
| Desktop, expert user, low time pressure | Full comparison table with all 24 plan attributes, expandable sections, side-by-side layout |
| Mobile, novice user, high time pressure | Stacked cards showing only the 5 most-differentiating attributes, with a "Top pick" badge on the AI-recommended plan |
| Screen reader user | Structured heading hierarchy with plan names as H3, attributes as definition lists, summary recommendation read first |
| Voice-only interface | Spoken summary of the top recommendation with "Would you like to hear details on any specific plan?" |

Design the outcome abstraction layer so that the AI selects the rendering strategy. Maintain a mapping of outcome types to rendering strategies per device class and user profile.

### Outcome Types Taxonomy

Categorize outcomes into a standard taxonomy that the AI references when selecting renderings:

| Outcome Type | Description | Typical Rendering |
|---|---|---|
| `compare` | User evaluates multiple options against each other | Comparison table, side-by-side cards |
| `decide` | User must select one option from a set | Recommendation card with supporting rationale |
| `understand` | User needs to comprehend a concept or dataset | Explanatory text with supporting visualizations |
| `act` | User needs to complete a transactional step | Form, wizard, or action panel |
| `monitor` | User tracks status or metrics over time | Dashboard with KPI cards and trend charts |
| `explore` | User browses without a specific target | Filterable grid, infinite scroll, faceted search |

Map each outcome type to two or three rendering strategies per platform. Allow the AI to select among them based on data density, user expertise, and device constraints. Update the mapping as usability testing reveals which renderings perform best for each outcome-context pairing.

---

## Design System Integration with Generative UI

### Constraining AI Generation

Never allow AI to generate arbitrary HTML or unconstrained layouts. Constrain generation to a defined component registry that maps to your design system tokens, spacing scale, color palette, and typography ramp.

### Component Registry Approach

Maintain a machine-readable component registry that the AI agent references during generation:

```json
{
  "components": {
    "data-table": {
      "max_columns": 8,
      "supports_sorting": true,
      "supports_pagination": true,
      "a11y_requirements": ["caption", "scope_attributes", "keyboard_navigation"]
    },
    "metric-card": {
      "allowed_sizes": ["sm", "md", "lg"],
      "required_fields": ["label", "value"],
      "optional_fields": ["trend", "sparkline", "icon"]
    },
    "comparison-grid": {
      "max_items": 6,
      "required_fields": ["title", "attributes"],
      "layout_modes": ["side-by-side", "stacked"]
    }
  }
}
```

### Validation Pipeline

Run every generated UI through a validation pipeline before rendering:

1. **Schema validation** — Confirm the generated component tree only references registered component types and respects each component's constraints.
2. **Accessibility audit** — Verify color contrast ratios meet WCAG 2.2 AA, confirm interactive elements have accessible names, validate focus order.
3. **Brand compliance** — Check that only approved colors, fonts, and iconography are used.
4. **Performance budget** — Reject layouts that exceed a DOM node threshold or require excessive client-side computation.

### Fallback Patterns

When generation fails or produces invalid output, implement a tiered fallback strategy:

| Failure Type | Fallback Response |
|---|---|
| Component type not in registry | Render generic card with raw key-value pairs |
| Accessibility validation fails | Re-render with safe defaults (high-contrast, larger text) |
| Generation times out | Show cached version of last successful render with a "Refreshing..." indicator |
| Complete failure | Revert to conversational UI with plain-text response |

---

## RAG Interface Patterns

### Reference Panels

Place a collapsible source-documents sidebar adjacent to the AI response. Display source titles, publication dates, and relevance scores. Allow the user to click any source to expand a preview pane showing the relevant passage highlighted in context.

Design the panel to occupy no more than 30% of the viewport width on desktop. On mobile, convert it to a bottom sheet triggered by a "View sources" button.

### Inline Citation Linking

Insert numbered superscript references within the AI-generated text. Each number links to the corresponding source in the reference panel.

```
The conversion rate increased by 23% after implementing
progressive disclosure patterns [1], consistent with
earlier findings on cognitive load reduction [2][3].
```

On hover (desktop) or long-press (mobile), display a citation preview tooltip containing the source title, author, date, and the specific passage the claim is drawn from.

### Source Verification UX

Enable users to verify claims against their sources with these interaction patterns:

- **Claim highlighting:** When the user clicks a citation number, highlight the specific sentence in the AI response that the citation supports and simultaneously scroll the reference panel to the relevant passage.
- **Side-by-side mode:** Offer a split view where the AI summary appears on the left and the full source document appears on the right, with corresponding passages connected by visual indicators.
- **Disagreement flagging:** Provide a "This doesn't match" action on each citation so users can flag inaccurate attributions.

### Knowledge Freshness Indicators

Display the date of each source document prominently. Apply visual treatments to indicate freshness:

| Source Age | Visual Treatment |
|---|---|
| Less than 7 days | Green dot, "Current" label |
| 7-90 days | No special treatment |
| 90 days - 1 year | Yellow dot, "Published [date]" label |
| Over 1 year | Orange dot, "May be outdated" warning |
| Source unavailable | Red dot, "Source no longer accessible" |

### Multi-Source Synthesis Visualization

When the AI combines information from multiple sources to form a response, visualize the synthesis process. Display a flow diagram or color-coded segments showing which parts of the response derive from which sources. Use distinct background tints per source so the user can visually parse the provenance of each claim.

### Confidence Indicators

Attach per-claim confidence indicators using a three-tier system:

- **High confidence** (solid icon): Claim is directly stated in multiple corroborating sources
- **Medium confidence** (half-filled icon): Claim is supported by a single source or requires inference
- **Low confidence** (outline icon): Claim is extrapolated or sources partially conflict

### Progressive Disclosure of Sources

Default to showing only the AI summary. Place a "Show sources" toggle or expandable section that reveals the full reference panel. Track usage analytics on this toggle to determine what percentage of users verify sources and adjust the default visibility accordingly.

### RAG Error States and Edge Cases

Handle the following RAG-specific failure modes with dedicated UI patterns:

- **No sources found:** Display a clear "No supporting sources found" message. Offer the user the option to broaden the search scope or rephrase their query. Do not silently generate a response without sources if the application promises source-backed answers.
- **Conflicting sources:** When sources directly contradict each other, surface both positions with labels indicating the disagreement. Display a "Sources disagree" badge and let the user inspect each perspective.
- **Partial retrieval:** When some claims have sources and others do not, mark unsourced claims with a "No source" indicator. Never blend sourced and unsourced content without clear visual differentiation.
- **Stale retrieval index:** When the underlying knowledge base has not been updated recently, display a global banner indicating the last index refresh date. Phrase it as "Sources last updated [date]" so users calibrate their trust accordingly.

---

## Platform Design Guidelines

### Apple Liquid Glass (iOS 26)

Apple's Liquid Glass design language introduced in iOS 26 uses translucent materials, depth layering, and fluid responsive animations. Apply these principles to AI interfaces:

- **Translucency:** Render AI response containers with the Liquid Glass material so underlying content shows through, maintaining spatial context. Use `Material.ultraThinMaterial` or the new `.liquidGlass` modifier.
- **Depth:** Layer AI suggestions above the primary content using elevation and parallax. Generative UI panels should feel as though they float above the workspace.
- **Fluid responsiveness:** Animate transitions between AI states (loading, streaming, complete) with spring-based physics. Avoid hard cuts.
- **Dynamic materials:** Adapt the material tint to the underlying content color so the glass effect always feels integrated rather than overlaid.

### Apple Intelligence Framework

Design for Apple Intelligence's on-device AI capabilities:

- **Foundation Models framework:** Build on-device generative features using Apple's Foundation Models API. Respect the guided generation schema for structured output.
- **Writing Tools integration:** Implement the system Writing Tools panel for text-heavy AI features. Users expect the standard Proofread, Rewrite, and Summary actions.
- **Image Playground:** Use the Image Playground API for image generation features. Follow Apple's style categories (Animation, Illustration, Sketch) and respect content policies.
- **Genmoji:** Support custom emoji generation through the Genmoji API. Allow inline insertion in text fields where the system supports it.
- **Visual Intelligence:** Integrate with Apple's Visual Intelligence for camera-based contextual understanding. Present results in the system look-up sheet format with action suggestions derived from identified objects, text, or scenes.
- **Siri integration:** When building AI features that complement Siri, respect the App Intents framework so the system can surface your AI capabilities through Siri without requiring the user to open your app directly.

### Google Gemini Visual Language

Gemini's visual design system uses gradients, circular shapes, and purposeful motion:

- **Gradient system:** Use the Gemini blue-to-purple gradient spectrum for AI-originated content. Apply gradients to borders, backgrounds, or accent elements to signal "AI-generated."
- **Circle shape language:** Circular avatars, loading indicators, and container shapes signal the Gemini brand. Use rounded containers for AI response areas.
- **Motion patterns:** Thinking states use a pulsing radial animation. Streaming text uses a left-to-right wipe reveal. Completion uses a subtle scale-up with opacity fade.
- **Multimodal indicators:** When the AI processes images, audio, or video, display modality icons (camera, microphone, film) with the Gemini gradient treatment to indicate active multimodal reasoning.

### OpenAI Apps SDK Design System

The OpenAI Apps SDK provides structured display modes and a component library:

- **Display modes:** Choose between `inline` (embedded within the host app's content flow), `floating` (overlay panel anchored to a trigger), and `fullscreen` (modal takeover for complex interactions).
- **Component library:** Use the SDK's built-in `MessageBubble`, `CodeBlock`, `DataTable`, `ImageGrid`, and `ActionBar` components for consistency across OpenAI-powered experiences.
- **Token system:** Map the SDK's design tokens (`--oai-color-primary`, `--oai-spacing-md`, `--oai-radius-lg`) to your design system tokens for seamless integration.
- **Dark and light theming:** Support both themes using the SDK's `ThemeProvider`. Test all AI-generated content in both themes to ensure contrast compliance.
- **Conversation threading:** Use the SDK's thread management to maintain context across multi-turn interactions. Display thread history in a sidebar on desktop and a sheet on mobile. Allow the user to branch conversations by selecting a previous message and starting a new thread from that point.
- **Plugin surfaces:** When building plugins or extensions for OpenAI's platform, render plugin outputs using the SDK's `PluginCard` component, which standardizes the display of third-party content within the AI conversation. Include clear attribution and a "View in app" deep link.

---

## Image Generation UX

### Style Galleries

Present curated style galleries before image generation begins. Display 8-12 style thumbnails (photorealistic, illustration, watercolor, 3D render, pixel art, etc.) so users anchor their expectations. Allow users to select a style as a generation parameter rather than describing it in natural language.

### Iterative Refinement Patterns

Design the generation workflow as a loop, not a one-shot operation:

1. **Generate** — User submits prompt, system produces 2-4 variations
2. **Select** — User picks the closest match or describes what to change
3. **Refine** — System regenerates with adjusted parameters (style, composition, color)
4. **Edit** — User applies targeted edits (inpainting, outpainting, object removal)
5. **Finalize** — User confirms and exports

### Inpainting and Outpainting Interaction

- **Inpainting:** Provide a brush tool for the user to mask regions they want regenerated. Display the mask as a semi-transparent red overlay. Allow brush size adjustment and an eraser for mask correction.
- **Outpainting:** Show the current image centered on a larger canvas. Display the extension regions as a checkerboard pattern (the universal transparency indicator). Let the user drag the canvas boundaries to define extension direction and size.

### Prompt-to-Image Feedback Loop

After each generation, display the interpreted prompt alongside the result. Show which keywords influenced which visual elements using color-coded highlights. This teaches users how to write more effective prompts.

### Undo and History

Maintain a visual history strip showing thumbnails of every generation and edit step. Support nonlinear undo by allowing the user to click any history thumbnail to branch from that state. Display the history as a horizontal scrollable timeline at the bottom of the canvas.

### Image Generation Prompt Assistance

Provide prompt scaffolding to help users express their intent more precisely:

- **Prompt templates:** Offer fill-in-the-blank templates organized by category (portrait, landscape, product shot, abstract). Each template includes slots for subject, style, lighting, and composition.
- **Negative prompts:** Expose a secondary input field for negative prompts (elements to exclude). Label it clearly as "Exclude from image" to avoid confusion.
- **Parameter sliders:** Provide visual sliders for abstract parameters like "creativity" (mapping to temperature or guidance scale), "detail level," and "color saturation" so users can adjust without understanding the underlying model parameters.
- **Prompt history:** Save successful prompts so users can re-use and modify them. Display prompt history as chips above the input field for quick access.

---

## AI Vision Interface Patterns

### Camera-Based AI Interaction

Design camera-based AI interfaces with a clear viewfinder overlay. Display a bounding box or highlight around detected objects in real time. Show the AI's classification label adjacent to each detected object with a confidence percentage.

Provide a shutter-style button for the user to capture the current frame for deeper analysis, distinct from the continuous live preview which shows lightweight annotations.

### Screenshot Understanding UX

When the user shares a screenshot for AI analysis, display the screenshot prominently with the AI's annotations overlaid. Use numbered callout markers on the screenshot linked to corresponding explanation text below. Allow the user to tap any region of the screenshot to ask follow-up questions about that specific area.

### Visual Question Answering

Structure the VQA workflow as:

1. User uploads or captures an image
2. System displays the image with a text input field below labeled "Ask about this image"
3. AI response appears adjacent to the image, not replacing it, so the user can cross-reference
4. Highlight the relevant region of the image that corresponds to the answer

### Real-Time Visual AI

For augmented reality and live camera analysis:

- Maintain a minimum of 24 fps for overlay rendering to avoid perceptible lag
- Use semi-transparent bounding boxes with rounded corners for object detection
- Position labels outside the bounding box to avoid occluding the detected object
- Apply a subtle background blur behind label text to ensure readability over variable backgrounds
- Provide a "Pause" control so users can freeze the frame for detailed inspection

### Document and Image Analysis Patterns

When designing AI-powered document analysis (receipts, contracts, diagrams, handwriting):

- Display the original document as the primary artifact. Overlay extracted data as dismissible annotation layers rather than replacing the original.
- Structure extracted information in an editable form adjacent to the document. Pre-populate fields from AI extraction but make every field user-editable to correct errors.
- Show extraction confidence per field. Highlight low-confidence extractions in amber so the user reviews them first.
- For multi-page documents, provide a page-by-page navigation with a minimap showing which pages have been analyzed and which have pending extractions.

---

## Multimodal Output Rendering

### Rendering Mixed Outputs

AI responses frequently combine text, images, code blocks, interactive widgets, and data visualizations in a single response. Render each content type as a distinct block within a vertical flow layout. Preserve the semantic sequence the AI intended.

```
[Text block: "Here's an analysis of the dataset."]
[Chart widget: bar chart of monthly revenue]
[Text block: "The spike in March correlates with the campaign launch."]
[Code block: SQL query used for the analysis]
[Interactive widget: date range selector to re-run the query]
```

### Layout Algorithms for Dynamic Content

Apply these layout rules for dynamically composed multimodal responses:

| Content Type | Layout Rule |
|---|---|
| Text | Full width, max-width 680px for readability |
| Image (single) | Centered, max-width 100% of container, maintain aspect ratio |
| Image (gallery) | Grid layout, 2 columns on mobile, 3-4 on desktop |
| Code block | Full width with horizontal scroll, syntax highlighting, copy button |
| Data table | Full width with horizontal scroll on overflow, sticky first column |
| Chart or visualization | Full width, responsive aspect ratio (16:9 default), interactive tooltips |
| Interactive widget | Full width, prominent visual separation (card container with border) |

### Streaming Multimodal Content

Render multimodal content progressively as it streams from the AI:

1. **Text streams first** — Display text tokens as they arrive using a cursor animation.
2. **Placeholder for media** — When the stream signals an upcoming image or chart, display a skeleton placeholder with the expected dimensions.
3. **Media loads asynchronously** — Replace the skeleton with the actual media once it is ready. Use a fade-in transition.
4. **Interactive widgets render last** — Hydrate interactive components after all static content has loaded to avoid layout shift.

Implement a layout stability mechanism that reserves space for incoming content blocks so existing content does not jump as new blocks appear.

### Content Type Detection and Rendering Pipeline

Build a content-type detection layer that inspects each block in the AI response stream and routes it to the appropriate renderer:

```javascript
const renderers = {
  'text/plain':       TextBlockRenderer,
  'text/markdown':    MarkdownRenderer,
  'image/png':        ImageRenderer,
  'image/svg+xml':    SVGRenderer,
  'application/json': JSONTreeRenderer,
  'application/vnd.chart': ChartRenderer,
  'application/vnd.table': DataTableRenderer,
  'text/x-python':    CodeBlockRenderer,
  'widget/form':      FormWidgetRenderer,
};

function renderBlock(block) {
  const Renderer = renderers[block.contentType] || FallbackRenderer;
  return <Renderer data={block.data} metadata={block.metadata} />;
}
```

Register custom content types for domain-specific widgets. When the AI includes a block with an unrecognized content type, render it using the `FallbackRenderer`, which displays the raw data in a collapsible JSON tree with a "This content type is not fully supported" notice.

### Accessibility of Multimodal Output

Ensure every modality in the response is accessible:

- **Images:** Require alt text generated by the AI or a secondary vision model. If alt text is unavailable, provide a "Describe this image" button that triggers an on-demand description.
- **Charts:** Provide a data table alternative accessible via a "View as table" toggle. Announce chart summaries to screen readers (e.g., "Bar chart showing revenue by month. March is highest at $4.2M.").
- **Code blocks:** Mark up code blocks with appropriate `language` attributes for syntax highlighting. Provide a "Copy code" button with an accessible label.
- **Interactive widgets:** Ensure full keyboard navigability. Announce state changes to screen readers via ARIA live regions.
- **Audio and video:** Provide captions and transcripts. Do not autoplay audio.

Apply WCAG 2.2 AA as the minimum standard for all generated multimodal content. Run automated accessibility checks on the rendered DOM after each generation cycle and before exposing the content to the user.

---

## Summary of Key Principles

| Principle | Guidance |
|---|---|
| Constrain generation | Never allow unconstrained AI output to reach the DOM. Route all generated UI through a validated component registry. |
| Design for outcomes | Specify what the user needs to accomplish, not the specific layout. Let the AI adapt presentation to context. |
| Cite everything | In RAG interfaces, link every claim to its source. Make verification effortless. |
| Respect platform conventions | Follow Apple Liquid Glass, Gemini visual language, or OpenAI SDK patterns for the target platform. |
| Fallback gracefully | Every generative UI path must have a deterministic fallback that preserves functionality. |
| Stream progressively | Render content as it arrives. Reserve layout space to prevent content shifting. |
| Guarantee accessibility | Validate contrast, semantics, keyboard access, and screen reader compatibility for every generated component. |
| Support iteration | Image generation, prompt refinement, and generative UI all benefit from undo, history, and branching. |
