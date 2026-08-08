# Emerging Patterns 2025-2026 — The Cutting Edge

## How to Use This File

This file catalogs 50+ patterns that are emerging, growing, or reaching mainstream adoption in 2025-2026. Unlike the stable patterns in `pattern-taxonomy-complete.md`, these patterns are in flux — their canonical form is still being established. When Sumi recommends emerging patterns, it should note the adoption status and implementation complexity so users can make informed decisions about whether to adopt early.

Each entry includes: what it is, adoption status, implementation complexity, reference apps, and basic specs.

Adoption status levels:
- **Emerging** — Pioneered by 1-3 products, not yet widely adopted. High risk, high differentiation.
- **Growing** — Adopted by 10+ notable products, patterns solidifying. Moderate risk, good differentiation.
- **Mainstream** — Widely adopted, canonical form established. Low risk, expected by users.

Implementation complexity:
- **Low** — Can be built with standard UI libraries and components.
- **Medium** — Requires specialized libraries, custom components, or non-trivial architecture.
- **High** — Requires significant infrastructure (real-time sync, ML models, spatial computing SDKs).

---

## AI-Native Patterns

### AI Chat Sidebar / Copilot Panel
**What it is:** A persistent or togglable AI assistant panel that lives alongside the main workspace, aware of the user's current context (selected text, current page, active file). Unlike a standalone chatbot, the copilot panel can read and write into the main workspace.

**Adoption status:** Mainstream (2025-2026)
**Implementation complexity:** Medium-High
**Reference apps:** GitHub Copilot Chat, Notion AI sidebar, Cursor AI, Claude sidebar in VS Code, Microsoft Copilot in Office
**Basic specs:**
- Panel width: 320-400px, collapsible
- Context injection: Pass current selection, file, or page as context to AI
- Actions: Insert into document, replace selection, copy to clipboard, create new item
- Conversation history: Per-context or global, with clear/reset
- Streaming responses with stop button
- Keyboard shortcut to toggle (Cmd+Shift+I or similar)
- Suggested prompts based on current context
- Must work alongside existing sidebar navigation (tabbed panels or overlay)

---

### AI Command Bar / Natural Language Actions
**What it is:** An evolution of the command palette (Cmd+K) that accepts natural language alongside traditional commands. Users can type "assign this to Sarah and set priority to high" instead of navigating menus. The AI interprets intent, maps to available actions, and either executes or previews the result.

**Adoption status:** Growing
**Implementation complexity:** Medium-High
**Reference apps:** Raycast AI, Linear (AI actions), Notion AI, Arc Browser
**Basic specs:**
- Same Cmd+K trigger as traditional command palette
- AI interpretation indicator (sparkle icon or "AI" badge on results)
- Preview of intended action before execution
- Confidence indicator for ambiguous commands
- Fallback to traditional exact-match search
- Action confirmation for destructive operations
- History of natural language commands with "run again"
- Latency target: < 500ms for action mapping, < 100ms for traditional search
- Clear distinction between AI-interpreted results and exact-match results

---

### AI-Generated UI / Dynamic Interfaces
**What it is:** UI components that are generated on-the-fly by AI based on user intent or data shape, rather than pre-designed. The AI selects appropriate components, populates them with data, and renders a usable interface. This is distinct from code generation — the UI renders in real time within the product.

**Adoption status:** Emerging
**Implementation complexity:** High
**Reference apps:** v0 by Vercel (code generation), Claude Artifacts, Galileo AI, Vercel AI SDK generative UI
**Basic specs:**
- Intent parser: Natural language or data → component selection
- Component registry: Available components the AI can compose
- Layout engine: Responsive arrangement of generated components
- Fallback UI: What to show if generation fails or is low-confidence
- Edit mode: User can adjust the generated layout (move, resize, remove components)
- Regenerate: "Try a different layout" option
- Persistence: Save generated views for reuse
- Safety: Sanitize all AI outputs before rendering (XSS prevention)
- Progressive enhancement: Start with a basic layout, refine with AI

---

### AI Content Suggestions / Smart Compose
**What it is:** Inline AI-powered writing assistance that appears as ghost text ahead of the cursor. Goes beyond autocomplete — suggests full sentences, paragraph completions, or alternative phrasings based on context and writing style.

**Adoption status:** Mainstream (in email and code; growing in general writing)
**Implementation complexity:** Medium
**Reference apps:** Gmail Smart Compose, GitHub Copilot, Notion AI, Superhuman AI compose
**Basic specs:**
- Ghost text rendering: 40-50% opacity ahead of cursor
- Accept: Tab key or right-arrow
- Dismiss: Continue typing (ghost text updates), Escape to clear
- Alternative suggestions: Cycle with Ctrl+] or similar
- Debounce: 300-500ms after last keystroke before suggesting
- Context window: Current paragraph + document title + recent edits
- Opt-out: Easy toggle in settings, remembered per user
- Privacy: Clear indication that content is processed by AI
- Reduced motion: Suggestions appear instantly without animation when preferred

---

### AI Image Generation Inline
**What it is:** Text-to-image generation embedded directly in the content creation workflow (not a separate tool). Users type a prompt, the image generates, and it inserts directly into their document, design, or product listing.

**Adoption status:** Growing
**Implementation complexity:** High (requires GPU inference or API integration)
**Reference apps:** Notion AI images, Canva Magic Media, ChatGPT DALL-E, Midjourney
**Basic specs:**
- Prompt input: Inline or modal, with style/aspect ratio options
- Generation time: 5-30 seconds with progress indicator
- Result gallery: 2-4 variations, click to select
- Refinement: "Make it more X" follow-up prompts, inpainting, outpainting
- Insert: Direct placement in content at cursor position
- Aspect ratios: 1:1, 4:3, 16:9, 3:4, 9:16 presets
- Style presets: Photo, illustration, 3D render, sketch, watercolor
- Attribution: Clear "AI-generated" metadata
- Moderation: Content safety filtering on both input and output
- Cost display: Token/credit usage indicator

---

### AI Summarization Widget
**What it is:** A component that condenses long content (threads, documents, meeting transcripts, email chains) into key points. Can appear as a persistent card at the top of long content or as an on-demand action.

**Adoption status:** Growing (mainstream in enterprise)
**Implementation complexity:** Medium
**Reference apps:** Slack thread summaries, Notion AI summarize, Arc Browse for Me, Otter.ai
**Basic specs:**
- Summary display: Bullet points (3-5), expandable to full content
- Trigger: Automatic for long content (>500 words) or manual button
- Length options: Brief (1-2 sentences), standard (3-5 bullets), detailed (paragraph)
- Source linking: Each summary point links to the original section
- Regenerate: Reshuffle with different emphasis
- Update: Re-summarize when content changes
- Copy: Summary as standalone text
- Confidence: "AI summary — may not capture all nuances" disclaimer
- Language: Match summary language to user preference

---

### AI Agent Task Cards
**What it is:** Cards displaying the status and progress of autonomous AI agents working on multi-step tasks. Unlike simple loading states, these show what the agent is doing, what it has completed, and what is remaining — providing transparency into AI reasoning and execution.

**Adoption status:** Growing
**Implementation complexity:** High
**Reference apps:** Claude Code (terminal output), Devin (task execution), GitHub Copilot Workspace, Anthropic workbench
**Basic specs:**
- Task title and description
- Step list with status icons: pending, running (with spinner), complete (checkmark), failed (x)
- Expandable step details (logs, intermediate results)
- Progress bar (determinate when steps are known, indeterminate for open-ended)
- Elapsed time and estimated remaining
- Pause/resume, cancel with confirmation
- Result summary on completion
- Error recovery: Retry failed step, modify and retry, abort
- Collapsible to compact card when backgrounded
- Real-time streaming of step updates via SSE/WebSocket

---

### AI Triage / Priority Suggestions
**What it is:** AI-powered suggestion system that recommends priority, categorization, or routing for incoming items (emails, support tickets, issues, tasks). Shows reasoning alongside the suggestion for user trust and override capability.

**Adoption status:** Growing
**Implementation complexity:** Medium
**Reference apps:** Superhuman AI triage, Linear auto-priority, Gmail priority inbox, Zendesk AI
**Basic specs:**
- Suggestion badge on items with AI-recommended priority/category
- Reasoning tooltip: "Marked urgent because customer mentioned SLA breach"
- Accept/override in one click
- Batch triage: AI suggests priorities for a queue, user reviews
- Learning: User overrides feed back into model
- Confidence display: High/medium/low certainty
- Opt-out: Per-item or globally
- Audit trail: Record AI suggestion vs. final human decision

---

## Spatial / AR Patterns

### Spatial Widgets
**What it is:** UI widgets that exist in 3D space, overlaid on the physical world through AR glasses or phone cameras. Unlike flat mobile widgets, spatial widgets have depth, respond to spatial gestures (pinch, grab, move), and can be anchored to surfaces or positions in the environment.

**Adoption status:** Emerging
**Implementation complexity:** High (requires ARKit/ARCore or visionOS)
**Reference apps:** Apple Vision Pro apps, Spatial computing prototypes, Meta Quest home
**Basic specs:**
- Widget sizes: Small (like a sticky note), medium (like a tablet), large (like a poster)
- Anchoring: World-locked (stays in physical position), head-locked (follows gaze), hand-anchored
- Interaction: Eye gaze + pinch (visionOS), hand gestures, controller input
- Depth: Widget has 3D volume, subtle parallax on head movement
- Passthrough: See real world behind/around widgets
- Typography: Minimum 12pt at 1m distance, high contrast for mixed-light environments
- Snapping: Widgets snap to surfaces, align to each other
- Persistence: Widget positions saved across sessions
- Fallback: Flat 2D representation for non-spatial devices

---

### 3D Product Viewer
**What it is:** An interactive 3D model viewer embedded in product pages, allowing users to rotate, zoom, and inspect products from any angle. Replaces or supplements static product photography.

**Adoption status:** Growing (mainstream in auto, furniture, sneakers)
**Implementation complexity:** Medium-High
**Reference apps:** Apple product pages (AirPods), IKEA Place, Nike SNKRS, Shopify AR
**Basic specs:**
- Model format: glTF/GLB (web standard), USDZ (iOS AR Quick Look)
- Interaction: Drag to rotate, pinch to zoom, swipe for predefined angles
- Loading: Progressive model loading with low-res placeholder
- Performance: 60fps on mid-range devices, LOD (level of detail) management
- AR mode: "View in your space" button using AR Quick Look (iOS) or Scene Viewer (Android)
- Annotations: Hotspots on model pointing to features
- Fallback: Static image gallery for unsupported devices
- File size target: < 5MB for web, < 15MB for AR
- Lighting: Consistent studio lighting, optional environment map

---

### AR Try-On
**What it is:** Augmented reality feature allowing users to virtually try products on themselves (eyewear, makeup, clothing) or in their space (furniture, art, home decor) using the device camera.

**Adoption status:** Growing (mainstream in beauty and eyewear, growing in fashion)
**Implementation complexity:** High (requires face/body tracking, 3D rendering)
**Reference apps:** Warby Parker, IKEA Place, Sephora Virtual Artist, Nike Fit, Amazon virtual try-on
**Basic specs:**
- Camera access with clear permission prompt explaining why
- Real-time rendering on face/body mesh (30fps minimum)
- Product switching: Browse alternatives while in AR view
- Capture: Screenshot/video of try-on for sharing
- Sizing: Body measurement estimation for fit recommendations
- Lighting adaptation: Virtual product matches ambient lighting
- Performance: Must run smoothly on 2-year-old devices
- Fallback: Static model/image overlay for devices without AR
- Privacy: Camera feed processed locally, not uploaded

---

### Spatial Navigation
**What it is:** Navigation paradigms designed for 3D/spatial computing where traditional flat menus do not apply. Includes gaze-based selection, hand gesture menus, spatial app launchers, and room-scale navigation.

**Adoption status:** Emerging
**Implementation complexity:** High
**Reference apps:** Apple Vision Pro (visionOS), Meta Quest, Magic Leap
**Basic specs:**
- Gaze + pinch as primary selection (visionOS pattern)
- Menu panels appear at comfortable arm distance (0.5-1.5m)
- Tab bars and toolbars float at bottom of field of view
- Spatial audio cues for navigation feedback
- Comfortable viewing zones: 20-degree cone for primary content
- Avoid forcing head movement for frequent actions
- Z-depth hierarchy: Active content closer, context further
- Transition animations: Spatial movement (not just fades)
- Fallback: Traditional 2D navigation for flat-screen viewing

---

### Immersive Media Viewer
**What it is:** 360-degree and volumetric media viewing for photos, videos, and spatial captures. Users can look around within captured environments.

**Adoption status:** Growing (mainstream for virtual tours, emerging for spatial video)
**Implementation complexity:** Medium-High
**Reference apps:** Google Street View, Matterport, Apple Spatial Video, Meta 360 video
**Basic specs:**
- 360 viewer: Drag/gyroscope to look around, zoom, hotspot navigation
- Spatial video: Stereoscopic rendering on compatible displays
- Controls: Play/pause, navigation arrows for multi-room, fullscreen
- Loading: Progressive quality (low-res immediate, high-res streaming)
- Performance: Texture streaming, level-of-detail management
- Accessibility: Alternative flat view, audio descriptions
- Embed: iframe-embeddable for web
- Mobile: Gyroscope-based look-around on phone

---

## Voice + Multimodal Patterns

### Voice Command Overlay
**What it is:** A visual overlay triggered by voice activation showing the system is listening, displaying real-time transcription, and confirming the interpreted command before execution.

**Adoption status:** Growing (mainstream in assistants, growing in apps)
**Implementation complexity:** Medium-High
**Reference apps:** Siri, Google Assistant, Alexa, ChatGPT voice mode
**Basic specs:**
- Activation: Wake word, button press, or keyboard shortcut
- Visual indicator: Animated waveform or pulsing orb showing listening state
- Transcription: Real-time text display of recognized speech
- Confirmation: Show interpreted command before executing, option to edit
- Error recovery: "I didn't understand" with suggestions
- Cancel: Tap anywhere or say "cancel"
- Multimodal: Voice + screen context ("delete that" referring to selected item)
- Privacy indicator: Clear recording status, local vs. cloud processing badge
- Accessibility: Visual-only alternative always available
- Latency: < 200ms from end of speech to command interpretation display

---

### Voice + Visual Hybrid Interface
**What it is:** Interfaces that combine voice input with visual display, where voice controls actions and the screen shows results. The screen is not just a passive display — it responds to voice commands with visual feedback.

**Adoption status:** Growing
**Implementation complexity:** High
**Reference apps:** Amazon Echo Show, Google Nest Hub, Apple HomePod + Apple TV, automotive infotainment
**Basic specs:**
- Visual feedback: Screen updates immediately on voice command
- Touch fallback: Every voice action also accessible via touch
- Disambiguation: When voice command is ambiguous, show visual options to select
- Glanceable results: Large text, images, clear hierarchy for distance viewing
- Continuous listening mode vs. push-to-talk toggle
- Context retention: "Show me that again" refers to previous visual result
- Multi-turn: Visual cards persist while conversation continues
- Automotive: Simplified visual + voice-primary for safety
- Smart display: Weather, calendar, photos as ambient content between interactions

---

### Multimodal Input Pattern
**What it is:** Input methods that accept multiple modalities simultaneously or interchangeably — text, voice, image, camera, file, drawing — within a single input field or interaction context.

**Adoption status:** Growing (mainstream in AI chat, growing in general apps)
**Implementation complexity:** Medium-High
**Reference apps:** ChatGPT (text + image + voice + file), Google Lens, Arc Search
**Basic specs:**
- Input bar with multiple input mode buttons: text, voice, camera, attach
- Mode switching: Seamless transition between typing and voice
- Image input: Camera capture, file upload, paste from clipboard, drag-and-drop
- Combined input: "What is this?" + attached photo
- Preview: Show attached media before sending
- Accessibility: Every modality has a text alternative
- Error handling: "Voice not available" falls back to text with explanation
- Mobile: Camera as first-class input alongside keyboard
- Size limits: Clear display of file size/type restrictions

---

### Voice Feedback / Audio UI
**What it is:** Using audio/speech output as a UI element — spoken confirmations, audio notifications, and voice-guided workflows where the display is secondary or unavailable.

**Adoption status:** Emerging (in automotive, wearables, accessibility)
**Implementation complexity:** Medium
**Reference apps:** Siri, Google Assistant, AirPods interactions, automotive interfaces
**Basic specs:**
- Earcon design: Distinct sounds for success, error, notification, warning
- Spoken confirmation: "Message sent to Sarah" with appropriate TTS voice
- Volume awareness: Adjust output based on ambient noise
- Priority: Urgent audio interrupts, normal audio queues
- Mute respect: Honor system mute/DND settings
- Accessibility: Audio output always supplemented with visual/haptic
- Voice selection: User preference for TTS voice, speed, language
- Latency: < 100ms for earcons, < 500ms for spoken output

---

## Collaborative Patterns

### Multiplayer Cursors / Live Pointers
**What it is:** Showing other users' cursor positions in real-time on a shared canvas or document, each with a unique color and name label. Creates awareness of where collaborators are working without explicit communication.

**Adoption status:** Mainstream (in design tools, growing in documents and code)
**Implementation complexity:** High (requires real-time sync infrastructure)
**Reference apps:** Figma, Google Docs, Notion (beta), tldraw, Miro, Liveblocks-powered apps
**Basic specs:**
- Colored cursor with name label per user (max 20 visible, overflow as "+N")
- Smooth interpolation of cursor movement (not raw position updates)
- Update frequency: 50-100ms position updates via WebSocket
- Selection highlighting: Show what each user has selected (colored highlight)
- Idle timeout: Fade cursor after 30 seconds of inactivity
- Viewport awareness: Only show cursors in visible area
- Performance: Must not degrade main application performance
- Libraries: Liveblocks, Yjs, PartyKit for implementation
- Fallback: Hide cursors on slow connections, show presence list instead

---

### Live Presence Indicators
**What it is:** Beyond simple online/offline dots, rich presence showing what collaborators are currently doing — which page they are viewing, what they are editing, their focus state. Enables awareness without interrupting.

**Adoption status:** Growing
**Implementation complexity:** Medium-High
**Reference apps:** Figma (page-level presence), Notion (page viewers), Linear (issue viewers), Slack (typing in channel)
**Basic specs:**
- Presence levels: Online (active), Idle (inactive 5min), Viewing (specific page/item), Editing (specific field/block)
- Avatar stack on pages/items showing who is currently there
- "N viewing this page" indicator
- Click to follow: Jump to where a collaborator is working
- Privacy: Option to go invisible / hide presence
- Latency: Presence updates within 1-2 seconds
- Scalability: Handle 50+ concurrent users without flooding the UI
- Stale cleanup: Remove presence after disconnect/timeout (30-60 seconds)

---

### Real-Time Co-Editing
**What it is:** Multiple users editing the same content simultaneously with instant synchronization, conflict-free merges, and per-character attribution. The standard is now sub-100ms sync with CRDT or OT.

**Adoption status:** Mainstream (in documents), Growing (in structured data, code)
**Implementation complexity:** High (requires CRDT/OT infrastructure)
**Reference apps:** Google Docs, Notion, Figma, VS Code Live Share, tldraw
**Basic specs:**
- Sync engine: CRDT (Yjs, Automerge) or OT (Google Docs approach)
- Conflict resolution: Automatic, deterministic, no user intervention needed
- Attribution: Color-coded per-user changes, visible in history
- Offline support: Queue local changes, merge on reconnect
- Cursor/selection sync: See where others are editing
- Undo: Per-user undo stack (my undo does not undo your changes)
- Performance: < 100ms sync latency for local network, < 500ms for global
- Bandwidth: Delta compression, only transmit changes (not full document)
- Fallback: Lock-based editing if real-time sync fails

---

### Collaborative Comments / Review Threads
**What it is:** Contextual commenting system where comments are anchored to specific content, support threading, resolution, and @mentions, with real-time updates visible to all collaborators.

**Adoption status:** Mainstream
**Implementation complexity:** Medium
**Reference apps:** Figma pinned comments, Google Docs suggestions, GitHub PR review, Notion comments
**Basic specs:**
- Anchor to: Specific text range, canvas coordinate, code line, table cell
- Threading: Reply to comments, nested up to 2 levels
- Resolution: Open/resolved states, filter by state
- @mentions: Autocomplete user list, triggers notification
- Reactions: Emoji reactions on comments (quick acknowledge)
- Editing: Edit own comments (show edited indicator), delete with confirmation
- Real-time: New comments appear without refresh
- Notifications: Email + in-app for mentions, configurable for all comments
- Export: Comments included in export/print

---

### Async Video Comments (Loom-Style)
**What it is:** Short video recordings embedded as comments, replacing or supplementing text feedback. Users record themselves (with optional screen share) and the video is inserted inline in the conversation or review thread.

**Adoption status:** Growing
**Implementation complexity:** Medium-High
**Reference apps:** Loom, Vimeo Record, Screen Studio, Figma (Loom integration)
**Basic specs:**
- Record button in comment/feedback area
- Recording: Webcam, screen, or both (PiP)
- Duration limit: Configurable (default 5 minutes for comments)
- Auto-transcription: Searchable, accessible, timestamped
- Playback: Inline video player in comment thread
- Reactions: Emoji at specific timestamps
- Viewer analytics: Who watched, completion rate
- Storage: Video hosted and CDN-delivered
- Fallback: Text transcript for accessibility and slow connections

---

## Ambient / Calm Patterns

### Ambient Dashboard
**What it is:** A dashboard designed for passive monitoring — always visible on a wall display, secondary screen, or glanceable widget. Prioritizes trends and anomalies over precise data. Uses color, motion, and spatial hierarchy so critical changes are noticeable from across a room.

**Adoption status:** Growing
**Implementation complexity:** Medium
**Reference apps:** Geckoboard, Datadog TV mode, Shopify Retail display, Grafana TV mode
**Basic specs:**
- Full-screen, auto-rotating between metric sets
- Large typography readable from 3+ meters
- Color-coded status: Calm (cool colors) → Alert (warm colors) → Critical (red/pulse)
- Animation: Subtle data transitions, attention-grabbing for anomalies
- Auto-refresh: 15-60 second data refresh
- No interaction required (but touch-to-explore optional)
- Dark mode default (for wall displays, reduced eye strain)
- Time-of-day adaptation: Show different metrics for morning vs. evening
- Screensaver mode: Dim after hours, wake on data change

---

### Glanceable Widgets
**What it is:** Minimal-information widgets designed for sub-second comprehension on watch faces, phone lock screens, home screens, or secondary displays. One metric, one status, or one action per widget.

**Adoption status:** Mainstream
**Implementation complexity:** Low-Medium
**Reference apps:** iOS Widgets (WidgetKit), watchOS Complications, Android Widgets, Windows Widgets
**Basic specs:**
- Sizes: Small (2x2 grid unit), medium (4x2), large (4x4)
- Content: Single metric with trend, status indicator, or single action shortcut
- Typography: Maximum 2 text elements (value + label)
- Update frequency: 15 minutes minimum (platform-limited), push for critical
- Tap: Deep link into full app view
- Data freshness indicator: Timestamp or "Updated X minutes ago"
- Accessibility: VoiceOver reads widget content as a single labeled value
- Platform: WidgetKit (iOS/macOS), Glance (watchOS), AppWidgetProvider (Android)
- Design: Match system aesthetics (vibrancy on iOS, Material You on Android)

---

### Ambient Notifications / Gentle Alerts
**What it is:** Non-intrusive notification patterns that inform without demanding attention. Subtle visual changes (badge dots, color shifts, peripheral animations) that a user notices when they glance, rather than interrupting their focus.

**Adoption status:** Growing
**Implementation complexity:** Low-Medium
**Reference apps:** macOS notification center, iOS Dynamic Island passive state, Slack sidebar unread indicators
**Basic specs:**
- Visual weight hierarchy: Dot (lowest) → Count badge → Banner → Full modal (highest)
- Peripheral notification: Change in sidebar, status bar, or page title (tab title "*(1) App Name*")
- Sound: Optional, short, pleasant tone (not jarring)
- Haptic: Gentle tap (not buzz) on mobile
- Grouping: Batch similar notifications, "3 new messages" instead of 3 separate alerts
- Decay: Auto-dismiss after time or acknowledge by viewing the relevant area
- DND: Respect system and app-level Do Not Disturb
- Scheduling: Non-urgent notifications batched to quiet moments
- Accessibility: Announce politely via `aria-live="polite"` (not `assertive`)

---

### Focus Mode / Zen Mode
**What it is:** A reduced-UI mode that strips away non-essential interface elements to help users focus on their primary task. Goes beyond "distraction-free writing" to any workflow.

**Adoption status:** Growing
**Implementation complexity:** Low
**Reference apps:** Notion focus mode, iA Writer, Superhuman focus, VS Code Zen Mode, macOS Stage Manager
**Basic specs:**
- Toggle: Keyboard shortcut (Cmd+Shift+F or similar), menu option
- Hidden elements: Sidebar, toolbar, notifications, activity indicators
- Visible: Current content, minimal save/exit controls
- Timer option: Pomodoro-style focus timer with break prompts
- Notification suppression: Hold non-urgent notifications until exit
- Transition: Smooth animation to/from focus mode
- Escape: Escape key or gesture to exit, always accessible
- Persistence: Remember focus mode preference per workspace or globally
- Dark mode pairing: Optional auto-switch to dark mode for focus sessions

---

### Passive Data Collection / Ambient Sensing
**What it is:** UI patterns for displaying and acting on data collected passively (health sensors, location, usage patterns) without explicit user input. The challenge is showing value from passive data without feeling creepy.

**Adoption status:** Growing (mainstream in health, emerging in productivity)
**Implementation complexity:** Medium-High
**Reference apps:** Apple Health, Google Fit, Screen Time, RescueTime
**Basic specs:**
- Data display: Summary cards with trend arrows, not raw data streams
- Insights: "You walked 20% more this week" — human-readable, not just numbers
- Control: Clear display of what is being collected, easy opt-out per data type
- Privacy: Data processed locally when possible, clear privacy policy
- Anomaly detection: Alert only when patterns change significantly
- Historical view: Trends over time, not just current state
- Export: User can export all their data
- Transparency: "How we calculate this" explanation accessible

---

## Progressive Web App Patterns

### Install Prompt (PWA)
**What it is:** The prompt encouraging users to install a progressive web app to their home screen, transforming a web experience into an app-like one. The challenge is timing the prompt for maximum conversion without annoyance.

**Adoption status:** Growing
**Implementation complexity:** Low-Medium
**Reference apps:** Twitter/X PWA, Starbucks PWA, Pinterest PWA, Spotify web
**Basic specs:**
- Trigger timing: After 2+ visits, or after meaningful engagement (not on first visit)
- Custom prompt: App-specific banner before browser's native prompt
- Benefits: List 2-3 benefits ("Works offline", "Faster load", "Notifications")
- Dismiss: Respect dismissal for 30+ days, do not re-prompt immediately
- Snackbar/banner style: Non-modal, bottom-positioned, clear close button
- A2HS button: In settings/menu as a persistent option for users who dismissed
- Platform detection: Show only on supporting platforms/browsers
- Post-install: Thank user, explain any new capabilities

---

### Offline-First Interface
**What it is:** UI patterns that work seamlessly without network connectivity, syncing data when connection is restored. The interface never shows a broken state — it degrades gracefully and communicates sync status transparently.

**Adoption status:** Growing
**Implementation complexity:** High (requires service workers, IndexedDB, sync logic)
**Reference apps:** Notion (partial), Google Docs offline, Figma offline, Obsidian
**Basic specs:**
- Connectivity indicator: Subtle banner or icon showing online/offline status
- Queued actions: Show pending changes with "will sync when online"
- Conflict resolution: When offline changes conflict with server, show diff and let user choose
- Cache strategy: Service worker caching for shell + recent content
- Storage: IndexedDB for structured data, Cache API for assets
- Sync indicator: "Syncing..." → "All changes saved" → "Offline — changes will sync"
- Data freshness: Timestamp on cached data, "Last updated X ago"
- Graceful degradation: Features requiring network show "Available when online" (not errors)
- Background sync: Sync pending changes when connection is restored (Background Sync API)

---

### App-Like Navigation (PWA)
**What it is:** Navigation patterns that make PWAs feel like native apps rather than websites — standalone display mode, custom back button handling, gesture navigation support, and smooth view transitions.

**Adoption status:** Growing
**Implementation complexity:** Medium
**Reference apps:** Twitter/X PWA, Instagram PWA, Financial Times PWA
**Basic specs:**
- Display mode: `standalone` in manifest for no browser chrome
- Back button: Custom handling (not browser back, which exits the app)
- View Transitions API: Smooth page transitions matching native app feel
- Navigation stack: Push/pop semantics with animated transitions
- Safe areas: Respect notch and home indicator on iOS
- Pull-to-refresh: Custom implementation (not browser default)
- Scroll restoration: Return to scroll position on back navigation
- Tab bar: Persistent bottom navigation mimicking native tab bar
- Performance: Instant page transitions via preloading/prefetching

---

## New Interaction Patterns

### Command Palettes Everywhere
**What it is:** The command palette pattern (Cmd+K) spreading beyond developer tools into consumer apps, e-commerce, banking, and enterprise. Every app with more than 10 actions benefits from a command palette.

**Adoption status:** Mainstream (dev tools), Growing (consumer/enterprise)
**Implementation complexity:** Low-Medium
**Reference apps:** Linear, Notion, Vercel, Raycast, Arc, Superhuman, Figma, Mercury
**Basic specs:**
- Trigger: Cmd+K (Mac), Ctrl+K (Windows)
- Sections: Pages, Actions, Recent, Settings (categorized)
- Fuzzy search: Match on any part of command name
- Keyboard shortcuts: Shown inline next to each result
- Recent: Last 5-10 commands at the top when empty
- Libraries: cmdk (React), Ninja Keys (web component), kbar (React)
- Appearance: Centered modal, 480-600px wide, max 8 visible results
- Animation: Spring-in appearance, smooth result transitions
- Accessibility: `role="combobox"`, arrow key navigation, screen reader announcements

---

### Radial / Pie Menus
**What it is:** Circular menus where options are arranged around a center point, selected by directional gesture. Faster than linear menus for frequent actions because selection is direction-based (Fitts's Law advantage).

**Adoption status:** Emerging (niche: creative tools, gaming, spatial)
**Implementation complexity:** Medium
**Reference apps:** Procreate, Blender, some games, spatial computing prototypes
**Basic specs:**
- Trigger: Long-press, right-click, or dedicated button
- Items: 4-8 options (more reduces accuracy)
- Selection: Move in direction of desired option, release to select
- Visual: Sectors or icons around a center point, active sector highlighted
- Haptic: Feedback when crossing sector boundaries
- Cancellation: Return to center and release
- Fallback: Traditional linear menu for accessibility
- Animation: Quick appearance (< 100ms), smooth sector highlighting
- Use case fit: Creative tools, spatial computing, gaming — not standard business apps

---

### Gesture Shortcuts / Custom Gestures
**What it is:** User-definable or app-specific gestures that trigger actions (two-finger swipe to undo, pinch to dismiss, draw a shape to select a tool). Going beyond platform-standard gestures to app-specific shortcuts.

**Adoption status:** Emerging
**Implementation complexity:** Medium
**Reference apps:** Procreate gestures, iOS Shortcuts gestures, Arc Browser
**Basic specs:**
- Discoverability: Gesture reference sheet accessible from help/settings
- Customization: Let users remap gestures to preferred actions
- Conflict avoidance: Do not override system gestures (edge swipes, pinch to zoom)
- Visual feedback: Show what gesture was detected and what action it triggered
- Undo: Every gesture action should be undoable
- Onboarding: Introduce gestures progressively, not all at once
- Accessibility: Every gesture must have a non-gesture alternative
- Tolerance: Forgiving gesture recognition (do not require pixel-perfect execution)

---

### Keyboard-First Workflows
**What it is:** Interfaces designed primarily for keyboard interaction, where every action is reachable via keyboard shortcut and mouse is optional. Users never need to lift hands from the keyboard for core workflows.

**Adoption status:** Growing (mainstream in dev tools, growing in productivity)
**Implementation complexity:** Medium
**Reference apps:** Linear, Superhuman, Vim/Neovim, Raycast, Obsidian, Arc
**Basic specs:**
- Shortcut system: Consistent modifiers (Cmd for actions, Cmd+Shift for variations)
- Shortcut display: Shown inline in menus, tooltips, and command palette
- Shortcut sheet: Cmd+/ or ? to show all shortcuts, searchable
- Focus management: Clear focus indicators, logical tab order, skip nav
- Vim-like modes: Optional for power users (normal/insert mode)
- Shortcut conflicts: No conflicts with browser/OS shortcuts
- Customization: User-remappable shortcuts with conflict detection
- Progressive disclosure: Basic shortcuts first, advanced shortcuts revealed over time
- No shortcut more than 3 keys (Cmd+Shift+letter is the max comfortable)

---

### Drag-to-Rearrange Everything
**What it is:** The extension of drag-and-drop from kanban boards to all list content — sidebar items, dashboard widgets, table columns, navigation order, content blocks. Users expect to rearrange anything by dragging.

**Adoption status:** Growing
**Implementation complexity:** Medium
**Reference apps:** Notion (blocks, sidebar), Linear (sidebar), Figma (layers), Framer, Todoist
**Basic specs:**
- Drag handle: Visible on hover or persistent (6-dot grip icon)
- Ghost element: Semi-transparent clone follows cursor during drag
- Drop indicators: Clear line/highlight showing where item will land
- Keyboard alternative: Select + Cmd+Arrow to move items
- Cross-container: Drag between lists, columns, or sections
- Libraries: dnd-kit (React), SortableJS, Pragmatic Drag and Drop (Atlassian)
- Animation: Items animate to new positions (spring animation, 200-300ms)
- Persistence: New order saved immediately (optimistic update)
- Touch support: Long-press to initiate drag on mobile
- Accessibility: Screen reader announcements for position changes

---

## Modern Commerce Patterns

### Social Commerce / Shoppable Content
**What it is:** Commerce integrated directly into social feeds, stories, and content — tap a product in a photo or video to view details and purchase without leaving the content experience.

**Adoption status:** Growing (mainstream in Asia, growing in West)
**Implementation complexity:** Medium-High
**Reference apps:** Instagram Shopping, TikTok Shop, Pinterest buyable pins, YouTube Shopping
**Basic specs:**
- Product tags: Tappable indicators on images/video at product locations
- Product card: Overlay showing name, price, quick-add, "View details"
- Checkout: In-app or redirect to merchant (in-app preferred)
- Creator attribution: Commission tracking for influencer commerce
- Live shopping: Real-time product pins during live streams
- Wishlist: Save tagged products for later
- Reviews: Inline ratings on product tags
- Analytics: Tap-through rate, conversion from content to purchase
- Content types: Photo, video, story, reel, live stream

---

### Live Shopping / Livestream Commerce
**What it is:** Real-time video shopping where a host demonstrates products and viewers can purchase instantly with in-stream buy buttons. Combines entertainment with commerce.

**Adoption status:** Growing (mainstream in China/Asia, emerging in West)
**Implementation complexity:** High (requires live streaming + real-time commerce)
**Reference apps:** TikTok LIVE Shopping, Amazon Live, Taobao Live, YouTube Live Shopping
**Basic specs:**
- Live video player with product sidebar or overlay
- Product cards: Appear when host pins a product, show price + buy button
- Flash deals: Time-limited prices during stream
- Chat: Live viewer comments/questions
- Reaction: Live emoji reactions floating up
- Cart: Add products during stream, checkout after or during
- Replay: Stream recording with product timestamps for later shopping
- Viewer count: Live viewer metric for social proof
- Host tools: Product queue, pin/unpin, price override, viewer analytics

---

### AR Commerce / Virtual Try-Before-You-Buy
**What it is:** Using augmented reality to let customers visualize products in their space or on themselves before purchasing, reducing return rates and increasing purchase confidence.

**Adoption status:** Growing
**Implementation complexity:** High
**Reference apps:** IKEA Place, Warby Parker, Amazon AR View, Shopify AR
**Basic specs:**
- "View in AR" button on product page
- Room placement: Tap to place furniture/decor at accurate scale
- Body placement: Face/body tracking for wearables
- Size accuracy: Real-world scale maintained (measure with device sensors)
- Multi-product: Place multiple items to see how they work together
- Save/share: Screenshot AR view, share with others for opinions
- Purchase flow: Direct "Add to Cart" from AR view
- Performance: 30fps minimum, graceful degradation on older devices
- Return rate data: Track reduction in returns for AR-viewed products

---

### Crypto / Web3 Payment Pattern
**What it is:** Payment flows that accept cryptocurrency alongside traditional payment methods, including wallet connection, token selection, network fee display, and transaction confirmation.

**Adoption status:** Emerging (niche, growing in web3-native products)
**Implementation complexity:** Medium-High
**Reference apps:** Coinbase Commerce, OpenSea, Uniswap, ENS
**Basic specs:**
- Wallet connect: WalletConnect, MetaMask, Coinbase Wallet integration
- Token selector: Choose payment token from wallet balance
- Network fee: Display gas fee estimate, allow speed selection
- Transaction preview: Show exact amount leaving wallet before confirmation
- Confirmation: Wait for blockchain confirmation, show pending/confirmed status
- Receipt: Transaction hash link to block explorer
- Error handling: Insufficient balance, rejected transaction, network congestion
- Fiat conversion: Show USD/EUR equivalent alongside crypto amount
- Fallback: Traditional card payment always available as alternative

---

## Content Patterns

### Infinite Canvas
**What it is:** A zoomable, pannable 2D space with no edges where users can place, arrange, and connect content freely. Used for whiteboarding, mind mapping, design, and spatial note-taking.

**Adoption status:** Growing
**Implementation complexity:** High (requires custom rendering, spatial indexing, collaboration)
**Reference apps:** Figma, Miro, tldraw, Excalidraw, FigJam, Apple Freeform
**Basic specs:**
- Pan: Click-drag on empty space, middle-mouse, or Space+drag
- Zoom: Scroll wheel, pinch, zoom controls, Cmd+/- keyboard
- Minimap: Small overview showing viewport position in total canvas
- Performance: Render only visible area + buffer, spatial indexing for object lookup
- Collaboration: Multi-cursor, real-time sync (see Multiplayer Cursors pattern)
- Content types: Sticky notes, shapes, text, images, embedded content, connections
- Snapping: Grid snapping, alignment guides, smart distribute
- Undo: Full undo/redo stack with keyboard shortcuts
- Export: PNG, SVG, PDF of visible area or full canvas
- Infinite: No edges — canvas extends in all directions

---

### Block Editor / Structured Content
**What it is:** Content editing where the document is a sequence of typed blocks (paragraph, heading, image, code, embed, table) rather than a single rich text stream. Each block has its own type, properties, and behavior.

**Adoption status:** Mainstream
**Implementation complexity:** Medium-High
**Reference apps:** Notion, WordPress Gutenberg, Craft, GitBook, Sanity.io
**Basic specs:**
- Slash command menu: Type "/" to see available block types
- Block types: Paragraph, H1-H3, bullet list, numbered list, toggle, quote, code, image, embed, table, divider, callout
- Drag handle: Reorder blocks by dragging (6-dot handle on hover)
- Block actions: Delete, duplicate, move, turn into (convert type), color
- Nesting: Indent blocks for hierarchy (toggle lists, nested lists)
- Markdown shortcuts: Type "## " for H2, "- " for bullet, etc.
- Selection: Click block, Shift+click for multi-select, Cmd+A for all
- Collaboration: Per-block locking or concurrent editing
- Data model: Portable JSON/AST (not HTML string)
- Libraries: BlockNote, Editor.js, Tiptap Block, Lexical

---

### Rich Embeds / oEmbed Content
**What it is:** Pasting a URL and having it render as a rich preview or interactive embed — showing the linked content inline rather than as a plain link.

**Adoption status:** Mainstream
**Implementation complexity:** Medium
**Reference apps:** Notion embeds, Slack link unfurling, Discord embeds, Twitter cards
**Basic specs:**
- URL detection: Auto-detect pasted URLs, show embed option
- Preview card: Title, description, image from Open Graph/oEmbed metadata
- Interactive embeds: YouTube player, Figma frame, CodeSandbox, Loom video
- Fallback: If embed fails, show link preview card (not broken iframe)
- Supported services: YouTube, Vimeo, Twitter, GitHub, Figma, CodePen, Spotify, Maps
- Size: Responsive, contained within content width, no horizontal scroll
- Loading: Lazy-load embeds below the fold
- Security: Sandboxed iframes, CSP headers, no script injection
- Privacy: Show embed consent prompt for third-party content (GDPR)

---

### Interactive / Executable Content
**What it is:** Content that includes runnable code, interactive widgets, data visualizations, or manipulable elements — going beyond static text and images to content that responds to user input.

**Adoption status:** Growing (mainstream in docs/education, emerging in general content)
**Implementation complexity:** Medium-High
**Reference apps:** Observable notebooks, Jupyter, MDX, Stripe Docs (runnable code), Khan Academy
**Basic specs:**
- Runnable code blocks: Execute in browser sandbox, show output inline
- Interactive charts: Hover, zoom, filter directly on embedded visualizations
- Sliders/inputs: Adjust parameters that update content in real-time
- Sandbox: Secure execution environment (no access to user data or DOM outside widget)
- Fallback: Static output for environments that cannot run interactive content
- Performance: Lazy-load interactive elements, do not block page render
- Mobile: Touch-friendly interactions, simplified controls if needed
- Persistence: Save user's parameter choices, shareable state via URL
- Accessibility: All interactions keyboard accessible, screen reader compatible

---

## Quick Reference: Adoption Timeline

| Pattern | 2024 | 2025 | 2026 (projected) |
|---------|------|------|-------------------|
| AI Chat Sidebar | Growing | Mainstream | Mainstream |
| AI Command Bar | Emerging | Growing | Growing-Mainstream |
| AI Generated UI | Emerging | Emerging | Growing |
| AI Content Suggestions | Growing | Mainstream | Mainstream |
| AI Image Generation Inline | Emerging | Growing | Growing |
| AI Summarization | Growing | Growing | Mainstream |
| AI Agent Task Cards | Emerging | Growing | Growing |
| Spatial Widgets | Emerging | Emerging | Emerging-Growing |
| 3D Product Viewer | Growing | Growing | Mainstream |
| AR Try-On | Growing | Growing | Growing-Mainstream |
| Multiplayer Cursors | Growing | Mainstream | Mainstream |
| Real-Time Co-Editing | Growing | Mainstream | Mainstream |
| Command Palette (consumer) | Emerging | Growing | Mainstream |
| Keyboard-First Workflows | Growing | Growing | Mainstream |
| Offline-First Interface | Emerging | Growing | Growing |
| Block Editor | Growing | Mainstream | Mainstream |
| Infinite Canvas | Growing | Growing | Mainstream |
| Live Shopping | Growing (Asia) | Growing | Growing-Mainstream |
| Social Commerce | Growing | Growing | Mainstream |
| Ambient Dashboard | Emerging | Growing | Growing |
| Glanceable Widgets | Growing | Mainstream | Mainstream |
| Voice Command Overlay | Growing | Growing | Growing-Mainstream |
| Multimodal Input | Emerging | Growing | Growing |
| Focus Mode / Zen Mode | Growing | Growing | Mainstream |

---

## Implementation Priority Matrix

For teams deciding which emerging patterns to adopt:

**Adopt Now (low risk, high value):**
- Command palette (proven pattern, easy to add)
- Skeleton loading (replaces spinners, trivial swap)
- Block editor (Notion proved the model, libraries available)
- Keyboard shortcuts (incremental, always beneficial)
- AI content suggestions (APIs available, clear value)

**Adopt Soon (moderate risk, high value):**
- AI Chat Sidebar (well-understood pattern, API costs are the main barrier)
- Multiplayer cursors (libraries like Liveblocks make it accessible)
- Offline-first (investment pays off in reliability and UX)
- Glanceable widgets (platform APIs are mature)

**Watch and Evaluate (high risk/investment, high potential):**
- AI Generated UI (early, no canonical form yet)
- Spatial widgets (hardware dependency, small user base)
- Live shopping (market-dependent, high infrastructure cost)
- AR try-on (impressive but expensive to implement well)
- Crypto payments (volatile adoption, regulatory complexity)

**Experimental Only (cutting edge, niche):**
- Radial menus (spatial computing only, niche desktop)
- Custom gestures (discoverability challenge)
- Voice-only interfaces (accuracy still inconsistent)
- Spatial navigation (hardware-dependent)
