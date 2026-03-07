---
description: "[2.1] Information architecture — generate sitemap, navigation model, content hierarchy, page relationships, URL structure, and breadcrumb strategy for your product."
phase: "2"
phase_step: "2.1"
phase_name: "SHAPE"
step_label: "Step 8 of 30"
---

# Map — Information Architecture Engine

Generate complete information architecture: content inventory, sitemap, navigation model, page-level content hierarchy, cross-linking map, and search strategy. This is the #1 most-skipped step by vibe coders — and the reason their apps feel disorganized even when they look good.

## Analysis Protocol

### Step 0: Gather Context

Before building IA, collect:

1. **Product description**: What it does, features, content types, core value proposition.
2. **User types/roles**: From `/02-brief` personas if available — different users may need different navigation paths.
3. **Platform**: Web (SPA, MPA, marketing site), mobile (iOS, Android), or both. Platform determines navigation conventions.
4. **Scale**: How many pages/screens? A 5-screen mobile app needs a different IA approach than a 50-page SaaS platform or a 200-page content site.
5. **Prior Sumi outputs**: Check for `/02-brief` (product brief, personas), `/03-research` (user mental models, card sorting results), `/05-benchmark` (competitor navigation patterns). Consume if available.

If the user has no prior Sumi outputs, ask these questions directly. Scale is particularly important — do not build a mega-menu IA for a 5-screen app.

### Step 1: CONTENT INVENTORY

List all content types the product needs:

**Categorize each item**:
- **Primary**: Core to value proposition, used in every session (e.g., dashboard, main feed, project workspace)
- **Secondary**: Supporting content, used regularly but not every session (e.g., settings, profile, reports)
- **Tertiary**: Infrequent access (e.g., legal pages, help docs, account management, onboarding)

**For each content item, note**:
- Content type (page, screen, modal, drawer, panel)
- Expected frequency of access (every visit, weekly, rarely)
- User role(s) that need it
- Whether it contains sub-content (e.g., Settings contains Profile, Billing, Notifications)

**Priority ranking**: Stack-rank by user importance, not by what the business wants to promote. The most-accessed content must be the most-accessible content.

### Step 2: SITEMAP / SCREEN MAP

Generate a hierarchical tree structure of all pages/screens.

**For web products** — page tree with URL structure:
```
/                              Home
├── /dashboard                 Dashboard
├── /projects                  Projects List
│   ├── /projects/:id          Project Detail
│   │   ├── /projects/:id/tasks    Tasks
│   │   └── /projects/:id/settings Project Settings
│   └── /projects/new          Create Project
├── /team                      Team
│   └── /team/:id              Team Member Profile
├── /settings                  Settings
│   ├── /settings/profile      Profile
│   ├── /settings/billing      Billing
│   └── /settings/notifications Notifications
└── /auth
    ├── /auth/login            Login
    ├── /auth/signup           Signup
    └── /auth/forgot-password  Forgot Password
```

**For mobile products** — screen hierarchy with navigation depth:
```
Tab Bar
├── [Tab 1] Home
│   └── Detail Screen
├── [Tab 2] Search
│   ├── Results
│   └── Detail Screen
├── [Tab 3] Create (+)
├── [Tab 4] Activity
│   └── Detail Screen
└── [Tab 5] Profile
    └── Settings
        ├── Account
        ├── Notifications
        └── Privacy
```

**Depth rules**:
- Mobile: Maximum 3 levels (deeper = users get lost, can't find back)
- Web: Maximum 4 levels (deeper = SEO suffers, users abandon)
- If you need more depth, your IA needs restructuring, not more levels

**Mark on the sitemap**:
- Primary flows (bold or highlighted)
- Secondary flows (normal)
- Auth-gated sections
- Role-specific sections

### Step 3: NAVIGATION MODEL

Recommend the navigation system based on product characteristics:

**Primary navigation** (always visible or one gesture away):

| Product Characteristic | Recommended Pattern | Examples |
|----------------------|-------------------|----------|
| 2-5 top-level sections, mobile | Tab bar (iOS) / Bottom nav (Android) | Instagram, Spotify |
| 6-10 top-level sections, web | Sidebar navigation | Notion, Linear, Slack |
| 3-5 sections, web SaaS | Top navigation bar | Stripe, GitHub |
| 10+ sections, content-heavy web | Mega menu or sidebar with groups | Amazon, Shopify admin |
| 2-3 sections, focused app | Segmented control or minimal nav | Calculator, Camera |

**Secondary navigation**:
- Submenus / dropdown (web)
- Section headers within scrollable views (mobile)
- Breadcrumbs (when depth > 2 levels on web)
- Tab bars within a screen (for sub-sections of a page)

**Utility navigation** (persistent but secondary):
- Search (if product has >20 items of any type)
- Notifications
- User profile / avatar
- Settings gear
- Help / support

**Breadcrumb strategy**:
- When to show: web products with depth > 2 levels
- Format: `Home > Section > Subsection > Current Page`
- Mobile equivalent: back button with section title
- Do NOT use breadcrumbs on flat architectures (wasted space)

### Step 4: CONTENT HIERARCHY PER PAGE

For each key page/screen (top 5-8 screens), define content priority:

**Above the fold** (visible without scrolling):
- What is the #1 thing users need to see/do on this page?
- What is the primary CTA?
- What context/orientation info is needed? (page title, breadcrumb, status)

**Below the fold** (requires scrolling):
- Secondary content in order of importance
- Progressive disclosure: what starts collapsed/hidden?
- Related content / cross-links

**For each screen, specify**:
- Content blocks in priority order (1st, 2nd, 3rd...)
- CTA placement and prominence (primary, secondary, tertiary)
- What can be removed on mobile without losing core value

### Step 5: CROSS-LINKING MAP

Map how pages/screens connect to each other:

**Entry points**: How do users arrive at each page?
- Direct navigation (from nav menu)
- In-context links (from related content)
- Search results
- Notifications
- External links (email, shared URL)

**Exit points**: Where do users go from each page?
- Primary action leads to...
- Secondary actions lead to...
- Back/cancel returns to...

**Anti-pattern detection**:
- **Dead ends**: Pages with no forward navigation (trap the user) — flag these
- **Orphan pages**: Pages not linked from any other page (unreachable) — flag these
- **Circular flows**: A → B → C → A with no progress (user spinning) — flag these
- **Forced detours**: User must leave their task to complete a subtask (breaks flow) — flag these

### Step 6: SEARCH AND FINDABILITY

**Does this product need search?**
- Yes if: >20 items of any type, content-heavy, user-generated content, e-commerce
- No if: <10 screens, simple task-focused app, no content to search

**If search is needed**:
- Search scope: Global (searches everything) vs. sectional (searches within current area)
- Search input: persistent in header vs. expandable vs. dedicated search screen
- Results display: list with filters, grouped by type, highlighted matches
- Filter and sort strategy for list views (what filters matter, what default sort)
- Recent searches and suggestions
- Empty state: what to show when no results match

**Findability beyond search**:
- Can users find any content within 3 clicks/taps? (3-click rule)
- Are labels clear and unambiguous? (no jargon, no creative naming)
- Is the most-accessed content the most-accessible content?

## Output Format

```
### Phase Position
> **Phase 2: SHAPE** | Step 8 of 30 | `/08-map`
>
> `/07-inspo` → **`/08-map`** → `/09-wireframe`

---

## Information Architecture

### Content Inventory

| Content | Type | Category | Frequency | Roles | Has Sub-content |
|---------|------|----------|-----------|-------|----------------|
| [name] | [page/screen/modal] | [primary/secondary/tertiary] | [every visit/weekly/rarely] | [all/specific] | [yes/no] |

### Sitemap

[Tree structure with URLs/screen names — see Step 2 format]

**Depth analysis**: Max depth = [N] levels. [Assessment of whether this is appropriate.]

### Navigation Model

**Primary navigation**: [pattern] — [why]
**Secondary navigation**: [pattern] — [when it appears]
**Utility navigation**: [items] — [placement]
**Breadcrumbs**: [yes/no] — [format if yes]

[Navigation diagram or description]

### Page Content Hierarchy

#### [Screen 1 — Name]
1. [Highest priority content]
2. [Second priority]
3. [Third priority]
- **Primary CTA**: [action] — [placement]
- **Progressive disclosure**: [what's hidden until expanded]
- **Mobile adaptation**: [what changes]

#### [Screen 2 — Name]
[Same structure]

[Continue for top 5-8 screens]

### Cross-Linking Map

[How screens connect — entry/exit points for key screens]

**Anti-patterns detected**:
- Dead ends: [list or "None"]
- Orphan pages: [list or "None"]
- Circular flows: [list or "None"]

### Search and Findability

**Search needed**: [yes/no — why]
[If yes: scope, input style, results display, filters, empty state]
**3-click test**: [pass/fail — which content takes more than 3 clicks?]

---

### Next Steps
1. **First** → `/09-wireframe` — Create low-fidelity layouts based on this IA
2. **Or** → `/10-vision` — Set visual direction before wireframing
3. **Or** → `/12-audit` — If you have an existing app, audit it against this IA

**Run `/next` to continue the journey.**
```

## Quality Gates

The output MUST include:
- [ ] Complete content inventory with priority ranking (primary/secondary/tertiary)
- [ ] Sitemap with maximum 3 levels (mobile) or 4 levels (web) of depth
- [ ] Navigation model with platform-appropriate pattern and justification
- [ ] Content hierarchy for at least the top 5 screens
- [ ] No dead ends or orphan pages in the cross-linking map (or flagged if found)
- [ ] Search strategy if product has >20 pages/items
- [ ] 3-click test assessment

The output MUST NOT include:
- Navigation patterns that violate platform conventions (e.g., hamburger menu as primary nav on iOS)
- Sitemaps deeper than 4 levels without restructuring recommendation
- Content hierarchy without clear priority ranking
- Jargon or ambiguous labels in the sitemap (labels must be user-facing language)

## Cross-References

When building information architecture, draw knowledge from:
- `screen-flow-patterns` skill — screen types and flow patterns catalog
- `ui-pattern-intelligence` skill — navigation patterns, search patterns, list/grid patterns
- `cognitive-psychology-ux` skill — Hick's Law (fewer choices = faster decisions), Miller's Law (chunking 7+/-2), serial position effect (first and last items remembered)
- `mobile-ux-design` skill — mobile navigation conventions (tab bar, nav drawer, bottom sheet)
- `desktop-app-design` skill — desktop navigation patterns (sidebar, top nav, command palette)
- `accessibility-inclusive-design` skill — navigation accessibility (skip links, landmark regions, focus order)
- `ux-research-methods` skill — card sorting and tree testing for IA validation

## Next Step

**Next** → `/09-wireframe` (2.2) — Create low-fidelity wireframes based on the IA defined here

**Alternatives**:
- `/10-vision` — Set visual direction before wireframing
- `/12-audit` — Audit an existing app against this IA
- `/flow` (2.4) — Map detailed user flows through this IA
- `/guide` — See the full journey map
