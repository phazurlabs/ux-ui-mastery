---
description: "Information architecture — sitemap, navigation model, content hierarchy, cross-linking map, URL structure, and search strategy."
tier: "plan"
---

# Map — Information Architecture

Generate complete information architecture: content inventory, sitemap, navigation model, page-level content hierarchy, cross-linking map, and search strategy. This is the step that separates apps that feel organized from apps that feel like a pile of screens.

## Protocol

### Step 0: Gather Context

Before building IA, collect:

1. **Product description**: What it does, features, content types, core value proposition
2. **User types/roles**: From `/brief` personas if available -- different users may need different navigation paths
3. **Platform**: Web (SPA, MPA, marketing site), mobile (iOS, Android), or both. Platform determines navigation conventions
4. **Scale**: How many pages/screens? A 5-screen mobile app needs a different IA than a 50-page SaaS or a 200-page content site
5. **Prior Sumi outputs**: Check for `/brief` (personas), `/research` (user mental models, card sorting), `/benchmark` (competitor navigation). Consume if available

If no prior outputs exist, ask directly. Scale is particularly important -- do not build mega-menu IA for a 5-screen app.

### Step 1: Content Inventory

List all content types the product needs.

**Categorize each item**:
- **Primary**: Core to value proposition, used every session (dashboard, main feed, project workspace)
- **Secondary**: Supporting, used regularly but not every session (settings, profile, reports)
- **Tertiary**: Infrequent access (legal pages, help docs, account management, onboarding)

**For each item, note**:
- Content type (page, screen, modal, drawer, panel)
- Expected frequency of access (every visit, weekly, rarely)
- User role(s) that need it
- Whether it contains sub-content (e.g., Settings > Profile, Billing, Notifications)

**Priority ranking**: Stack-rank by user importance, not by what the business wants to promote. Most-accessed content must be most-accessible content.

### Step 2: Sitemap / Screen Map

Generate a hierarchical tree structure.

**For web products** -- page tree with URL structure:
```
/                              Home
├── /dashboard                 Dashboard
├── /projects                  Projects List
│   ├── /projects/:id          Project Detail
│   │   ├── /projects/:id/tasks    Tasks
│   │   └── /projects/:id/settings Project Settings
│   └── /projects/new          Create Project
├── /team                      Team
│   └── /team/:id              Member Profile
├── /settings                  Settings
│   ├── /settings/profile      Profile
│   ├── /settings/billing      Billing
│   └── /settings/notifications Notifications
└── /auth
    ├── /auth/login            Login
    ├── /auth/signup           Signup
    └── /auth/forgot-password  Forgot Password
```

**For mobile products** -- screen hierarchy with navigation depth:
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
- Mobile: Maximum 3 levels (deeper = users get lost)
- Web: Maximum 4 levels (deeper = SEO suffers, users abandon)
- If you need more depth, restructure -- don't add levels

**Mark on the sitemap**:
- Primary flows (bold/highlighted)
- Secondary flows (normal)
- Auth-gated sections
- Role-specific sections

### Step 3: Navigation Model

Recommend the navigation system based on product characteristics.

**Primary navigation** (always visible or one gesture away):

| Product Type | Pattern | Examples |
|-------------|---------|----------|
| 2-5 sections, mobile | Tab bar (iOS) / Bottom nav (Android) | Instagram, Spotify |
| 6-10 sections, web | Sidebar navigation | Notion, Linear, Slack |
| 3-5 sections, web SaaS | Top navigation bar | Stripe, GitHub |
| 10+ sections, content-heavy | Mega menu or sidebar with groups | Amazon, Shopify admin |
| 2-3 sections, focused app | Segmented control or minimal nav | Calculator, Camera |

**Secondary navigation**:
- Submenus / dropdown (web)
- Section headers within scrollable views (mobile)
- Breadcrumbs (when depth > 2 levels on web)
- Tab bars within a screen (for sub-sections)

**Utility navigation** (persistent but secondary):
- Search (if >20 items of any type)
- Notifications
- User profile / avatar
- Settings gear
- Help / support

**Breadcrumb strategy**:
- Show on web products with depth > 2 levels
- Format: `Home > Section > Subsection > Current Page`
- Mobile equivalent: back button with section title
- Do NOT use breadcrumbs on flat architectures (wasted space)

### Step 4: Content Hierarchy Per Page

For each key page/screen (top 5-8), define content priority:

**Above the fold** (visible without scrolling):
- What is the #1 thing users need to see/do?
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

### Step 5: Cross-Linking Map

Map how pages/screens connect:

**Entry points** -- how users arrive at each page:
- Direct navigation (from nav menu)
- In-context links (from related content)
- Search results
- Notifications
- External links (email, shared URL)

**Exit points** -- where users go from each page:
- Primary action leads to...
- Secondary actions lead to...
- Back/cancel returns to...

**Anti-pattern detection**:
- **Dead ends**: Pages with no forward navigation (trap the user) -- flag these
- **Orphan pages**: Pages not linked from any other page (unreachable) -- flag these
- **Circular flows**: A > B > C > A with no progress -- flag these
- **Forced detours**: Must leave task to complete subtask (breaks flow) -- flag these

### Step 6: Search and Findability

**Does this product need search?**
- Yes if: >20 items of any type, content-heavy, user-generated content, e-commerce
- No if: <10 screens, simple task-focused app, no content to search

**If search is needed**:
- Search scope: global vs. sectional
- Input style: persistent in header vs. expandable vs. dedicated screen
- Results display: list with filters, grouped by type, highlighted matches
- Filters and sort strategy
- Recent searches and suggestions
- Empty state: what to show when no results match

**Findability test**:
- Can users reach any content within 3 clicks/taps?
- Are labels clear and unambiguous? (no jargon, no creative naming)
- Is most-accessed content the most-accessible content?

## Output Format

```
## Information Architecture: [Product Name]

### Content Inventory

| Content | Type | Category | Frequency | Roles | Sub-content |
|---------|------|----------|-----------|-------|-------------|
| [name] | [page/screen/modal] | [primary/secondary/tertiary] | [every visit/weekly/rarely] | [all/specific] | [yes/no] |

### Sitemap
[Tree structure with URLs/screen names]

**Depth analysis**: Max depth = [N] levels. [Assessment]

### Navigation Model

**Primary**: [pattern] -- [why]
**Secondary**: [pattern] -- [when it appears]
**Utility**: [items] -- [placement]
**Breadcrumbs**: [yes/no] -- [format if yes]

### Page Content Hierarchy

#### [Screen 1]
1. [Highest priority content]
2. [Second priority]
3. [Third priority]
- **Primary CTA**: [action] -- [placement]
- **Progressive disclosure**: [what's hidden until expanded]
- **Mobile adaptation**: [what changes]

[Continue for top 5-8 screens]

### Cross-Linking Map
[Entry/exit points for key screens]

**Anti-patterns detected**:
- Dead ends: [list or "None"]
- Orphan pages: [list or "None"]
- Circular flows: [list or "None"]

### Search & Findability

**Search needed**: [yes/no -- why]
[If yes: scope, input, results, filters, empty state]
**3-click test**: [pass/fail -- which content takes more?]

### Next Steps
1. `/wireframe` -- Create layouts based on this IA
2. `/screen` -- Build production screens
3. `/nav` -- Design the navigation system in detail
```

## Quality Gates

The output MUST include:
- [ ] Content inventory with priority ranking (primary/secondary/tertiary)
- [ ] Sitemap with maximum 3 levels (mobile) or 4 levels (web)
- [ ] Navigation model with platform-appropriate pattern and justification
- [ ] Content hierarchy for at least top 5 screens
- [ ] No dead ends or orphan pages (or flagged if found)
- [ ] Search strategy if product has >20 pages/items
- [ ] 3-click test assessment

The output MUST NOT include:
- Navigation patterns violating platform conventions (e.g., hamburger as primary nav on iOS)
- Sitemaps deeper than 4 levels without restructuring recommendation
- Jargon or ambiguous labels in the sitemap (must be user-facing language)

## Cross-References

When building IA, draw knowledge from:
- `screen-flow-patterns` skill -- screen types and flow patterns catalog
- `ui-pattern-intelligence` skill -- navigation, search, list/grid patterns
- `navigation-pattern-encyclopedia` skill -- every nav pattern with IA guide
- `cognitive-psychology-ux` skill -- Hick's Law, Miller's Law, serial position effect
- `mobile-ux-design` skill -- mobile navigation conventions (tab bar, nav drawer, bottom sheet)
- `desktop-app-design` skill -- desktop navigation (sidebar, top nav, command palette)
- `accessibility-inclusive-design` skill -- skip links, landmark regions, focus order
- `ux-research-methods` skill -- card sorting and tree testing for IA validation

## Next Step

**Next** --> `/wireframe` -- Create low-fidelity wireframes based on this IA

**Alternatives**:
- `/screen` -- Jump to production screens if IA is simple enough
- `/nav` -- Deep dive into navigation design
- `/sumi` -- See the full command map
