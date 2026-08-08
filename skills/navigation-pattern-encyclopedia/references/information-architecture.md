# Information Architecture — Complete Reference

> IA methods, structures, validation techniques, URL design, labeling, faceted navigation, and documentation templates for building navigation systems grounded in research.

---

## What Is Information Architecture

Information architecture (IA) is the structural design of shared information environments. It is the art and science of organizing and labeling content so that people can find and use it. IA is the invisible structure that navigation makes visible.

The relationship between IA and navigation:
- **IA** = the taxonomy, hierarchy, and relationships between content
- **Navigation** = the UI that expresses IA and enables movement through it
- **Good IA + bad navigation** = users can find things with effort (fixable with better UI)
- **Bad IA + good navigation** = users cannot find things no matter how polished the UI is (requires structural redesign)

### The Three Circles of IA (Rosenfeld & Morville)

1. **Users**: Their needs, tasks, mental models, information-seeking behaviors, and vocabulary
2. **Content**: Volume, structure, format, existing organization, metadata, and growth rate
3. **Context**: Business goals, constraints, culture, technology, and resources

IA lives at the intersection of these three circles. If you only consider content structure without understanding how users think about it, you will build a taxonomy that makes sense to your team but not to your users.

---

## IA Research Methods

### 1. Open Card Sorting

Participants organize content items into groups of their own creation and name each group. Reveals how users naturally categorize your content.

**When to Use**:
- Starting a new IA from scratch
- Redesigning an existing IA that has usability problems
- When you do not know how users think about your content
- When content does not have an obvious single organization scheme

**Process**:
1. Prepare 30-60 content items (too few = insufficient data, too many = fatigue)
2. Write each item on a physical card or use digital tool (Optimal Workshop, UserZoom)
3. Recruit 15-20 participants from your target audience
4. Ask each participant to sort cards into groups that make sense to them
5. Ask them to name each group
6. Analyze results using a similarity matrix and dendrogram

**Deliverable**: Similarity matrix showing which items are most frequently grouped together, plus common group names.

**Analysis Metrics**:
| Metric | Good Result |
|--------|-------------|
| Agreement on groupings | > 70% of participants group the same items together |
| Number of groups | 5-9 for top-level categories |
| Group naming consistency | > 60% of participants use the same or synonymous labels |
| Outlier items | < 10% of items placed inconsistently across participants |

```
Example Similarity Matrix (simplified):

                    Pricing  Plans  Billing  Invoices  FAQ
Pricing              —       85%    72%     68%       12%
Plans               85%      —      78%     65%       15%
Billing             72%     78%     —       88%       8%
Invoices            68%     65%     88%     —         5%
FAQ                 12%     15%     8%      5%        —

Interpretation: Pricing/Plans are frequently grouped (85%).
Billing/Invoices are even more strongly grouped (88%).
FAQ is rarely grouped with any of these items.
```

### 2. Closed Card Sorting

Participants organize content items into predefined categories. Validates whether an existing or proposed IA structure makes sense to users.

**When to Use**:
- Validating a proposed IA structure before implementation
- Testing whether your category labels are understood
- When you have an existing IA and want to verify or improve it
- After open card sorting, to validate the categories that emerged

**Process**:
1. Define 5-9 top-level categories with clear labels
2. Prepare 30-60 content items
3. Recruit 15-20 participants
4. Ask participants to place each item into the most appropriate category
5. Analyze placement accuracy per category

**Analysis Metrics**:
| Metric | Good Result |
|--------|-------------|
| Correct placement rate | > 80% per item |
| Category confusion | < 20% of items placed in unexpected categories |
| Abandoned items | < 5% of items that participants cannot categorize |
| Category load balance | No category has > 40% of all items |

### 3. Tree Testing (Reverse Card Sorting)

Participants navigate a text-only representation of your site hierarchy to find specific items. Tests findability without the influence of visual design or navigation UI.

**When to Use**:
- Validating IA before investing in UI design
- Comparing two or more proposed IA structures
- Identifying where users get lost in the hierarchy
- After card sorting, to validate the resulting structure

**Process**:
1. Create a text-only tree of your proposed IA (3-4 levels deep)
2. Write 8-12 tasks: "Where would you find [item]?"
3. Recruit 50+ participants (tree tests need higher N for statistical significance)
4. Use a tool (Treejack by Optimal Workshop, UserZoom) to run the test
5. Analyze success rate, directness, and time per task

**Analysis Metrics**:
| Metric | Target | Red Flag |
|--------|--------|----------|
| **Overall success** | > 80% | < 60% |
| **Directness** | > 60% | < 40% |
| **Time to find** | < 30s (primary tasks) | > 60s |
| **First click correct** | > 70% | < 50% |

**Interpreting Results**:
- **High success + high directness**: Users know where to go and go there directly. IA works.
- **High success + low directness**: Users find it eventually but wander first. Labels or groupings may be confusing.
- **Low success + users try multiple paths**: The item is in an unexpected location. Consider moving it.
- **Low success + most users try the same wrong path**: The category label is misleading. Rename it.

**Pietree Visualization**:
Tree test tools generate "pietree" visualizations showing the proportion of users who selected each path at each level. Look for:
- The correct path having the largest slice at each level
- No alternative path having > 30% of users (indicates category confusion)

### 4. First-Click Testing

Users are shown a wireframe or screenshot and asked "Where would you first click to [task]?" Measures whether the first interaction aligns with the correct path.

**When to Use**:
- Validating the visual hierarchy of navigation
- Testing whether prominent elements draw the right first clicks
- Comparing design variations for navigation layouts
- Quick validation before full usability testing

**Key Finding**: Research by Bob Bailey (2006) showed that if users' first click is correct, they have an 87% chance of completing the task. If the first click is wrong, the success rate drops to 46%. First clicks matter enormously.

**Process**:
1. Create a wireframe or screenshot of the navigation
2. Write 5-8 task scenarios
3. Recruit 20-30 participants
4. For each task, show the design and ask "Where would you click first?"
5. Generate a click heatmap and measure % correct first clicks

**Analysis**:
| Metric | Target |
|--------|--------|
| Correct first click | > 70% |
| Click concentration | > 60% of clicks on the correct element |
| Time to first click | < 10 seconds |

### 5. Content Inventory

A comprehensive catalog of every piece of content on a site or in a product. The foundation for IA work on existing products.

**Process**:
1. Crawl the site (Screaming Frog, Sitebulb) or manually catalog
2. Record for each page: URL, title, content type, author, date, word count, status
3. Identify: duplicate content, outdated content, orphaned pages, content gaps
4. Categorize content by type, topic, audience, and lifecycle stage

**Spreadsheet Template**:
| URL | Page Title | Content Type | Section | Author | Last Updated | Status | Word Count | Notes |
|-----|-----------|-------------|---------|--------|-------------|--------|-----------|-------|
| /about | About Us | Landing page | Company | Marketing | 2025-11-15 | Current | 450 | Needs refresh |
| /blog/post-1 | How to Start | Blog post | Blog | J. Smith | 2024-03-20 | Outdated | 1200 | Review for accuracy |
| /products/old | Legacy Product | Product page | Products | Product | 2023-01-10 | Deprecated | 800 | Redirect to new product |

### 6. Content Audit

A qualitative evaluation of content quality, accuracy, relevance, and effectiveness. Goes beyond inventory to assess whether content serves its purpose.

**Audit Criteria**:
| Criterion | Questions |
|-----------|-----------|
| **Accuracy** | Is the information correct and current? |
| **Completeness** | Does it cover the topic adequately? |
| **Relevance** | Does the target audience need this? |
| **Clarity** | Is it understandable by the target audience? |
| **Findability** | Can users navigate to this content easily? |
| **SEO** | Does it have proper metadata, headings, keywords? |
| **Actionability** | Does it have a clear CTA or next step? |
| **Brand alignment** | Does it match brand voice and guidelines? |

**Action Categories**:
- **Keep as-is**: Content is accurate, relevant, and well-structured
- **Update**: Content is relevant but outdated or inaccurate
- **Consolidate**: Multiple pages cover the same topic; merge them
- **Remove**: Content is no longer relevant, accurate, or needed
- **Create**: Gap identified — new content needed
- **Restructure**: Content is good but in the wrong location

---

## IA Structures

### 1. Hierarchical (Tree Structure)

The most common IA structure. Content organized in parent-child relationships, forming a tree from broad categories to specific items.

```
Home
  Products
    Category A
      Product 1
      Product 2
    Category B
      Product 3
  About
    Team
    History
    Careers
  Blog
    Post 1
    Post 2
```

**Best for**: E-commerce, corporate sites, documentation, government sites
**Navigation patterns**: Sidebar with nesting, mega menus, breadcrumbs
**Limits**: Max 3-4 levels deep before users get lost

### 2. Flat (Database) Structure

All content exists at the same level, connected through metadata, tags, and search rather than hierarchy. No parent-child relationships.

```
[Item 1] --tagged--> Tech, Tutorial, Beginner
[Item 2] --tagged--> Design, Case Study, Advanced
[Item 3] --tagged--> Tech, Case Study, Intermediate
```

**Best for**: Blogs, knowledge bases, wikis, social media feeds
**Navigation patterns**: Search, tags, filters, faceted navigation
**Limits**: Requires good metadata and search; browsing without search is difficult

### 3. Sequential (Linear) Structure

Content is organized in a specific order that users follow step by step.

```
Step 1: Account Setup --> Step 2: Profile --> Step 3: Preferences --> Step 4: Complete
```

**Best for**: Onboarding, tutorials, checkout flows, courses, wizards
**Navigation patterns**: Stepper, prev/next, progress bar
**Limits**: Does not support non-linear exploration

### 4. Matrix Structure

Content is organized along multiple dimensions simultaneously. Users can navigate by any dimension.

```
       Beginner    Intermediate    Advanced
Tech   [items]     [items]         [items]
Design [items]     [items]         [items]
Biz    [items]     [items]         [items]
```

**Best for**: Educational content, product catalogs with multiple attributes, comparison tools
**Navigation patterns**: Faceted navigation, filter combinations, pivot tables
**Limits**: Complex to implement and can overwhelm users with choices

### 5. Hub-and-Spoke Structure

A central hub connects to independent sections (spokes) that do not connect to each other. Users return to the hub to switch between sections.

```
        Spoke A
          |
Spoke D --Hub-- Spoke B
          |
        Spoke C
```

**Best for**: Mobile apps with distinct features, dashboards, kiosk interfaces
**Navigation patterns**: Home screen with cards, bottom tab bar, icon grid
**Limits**: Cross-section navigation requires returning to hub

### 6. Network (Web) Structure

Content is interconnected with no strict hierarchy. Any item can link to any other item. The web itself is a network structure.

```
[A] <--> [B] <--> [C]
 ^        |        ^
 |        v        |
 [D] <--> [E] <--> [F]
```

**Best for**: Wikis, knowledge graphs, social networks, reference materials
**Navigation patterns**: Inline links, related content, search, breadcrumbs (showing one path)
**Limits**: Users can easily get lost; requires strong "you are here" indicators

---

## Labeling and Taxonomy

### Labeling Principles

1. **Use user vocabulary, not internal vocabulary**: "Pricing" not "Commercial Plans". "Help" not "Knowledge Base". Test labels with real users.

2. **Be specific**: "Running Shoes" not "Products". "API Documentation" not "Resources". "Contact Sales" not "Get in Touch".

3. **Be consistent**: If you call it "Settings" in the nav, call it "Settings" everywhere — not "Preferences" on one page and "Options" on another.

4. **Be concise**: 1-3 words per nav item. "Sign In" not "Sign In to Your Account". "Docs" not "Documentation and References".

5. **Front-load keywords**: Users scan the first 2-3 characters. "Pricing Plans" not "Our Pricing Plans". "Account Settings" not "Manage Your Account Settings".

6. **Avoid jargon and ambiguity**: The worst offenders in navigation labeling:

| Ambiguous Label | What Users Think | Better Label |
|----------------|-----------------|-------------|
| Solutions | "Marketing speak, I'll skip it" | [Specific product name] |
| Resources | "Could be anything" | Blog, Docs, Templates, Guides |
| Platform | "Vague tech term" | [Feature name] or Products |
| Services | "Consulting? Features? Support?" | [Specific service: "Consulting", "Training"] |
| Explore | "Explore what?" | Browse [Category] |
| Insights | "Blog posts? Analytics? Reports?" | Blog, Analytics, Reports |
| More | "More of what?" | Show all [items] |

### Taxonomy Design

A taxonomy is a classification system for your content. Good taxonomy = good IA = good navigation.

**Types of Taxonomy**:
| Type | Description | Example |
|------|-------------|---------|
| **Topic** | Organized by subject matter | Blog: "Engineering", "Design", "Product" |
| **Task** | Organized by what users want to do | Banking: "Send Money", "Pay Bills", "Invest" |
| **Audience** | Organized by user type | SaaS: "For Startups", "For Enterprise", "For Developers" |
| **Format** | Organized by content type | Media: "Articles", "Videos", "Podcasts" |
| **Lifecycle** | Organized by stage | Support: "Getting Started", "Using Features", "Troubleshooting" |

**Taxonomy Rules**:
1. Categories must be mutually exclusive (an item belongs to one category)
2. Categories must be collectively exhaustive (every item has a home)
3. Categories should be balanced in size (no category with 80% of items)
4. Depth should be consistent (not 1 level in some branches, 5 in others)
5. Labels should be parallel in grammatical form (all nouns, or all verb phrases)

---

## Site Map Design

### Site Map as IA Deliverable

A site map is a visual diagram of the IA structure. It shows every page in the product and how they relate hierarchically.

**Site Map Notation**:
```
[Page]         = Standard page
{Conditional}  = Page shown conditionally (auth, role, etc.)
(External)     = Link to external site
[Repeated ×N]  = Dynamic page repeated for N items
---            = Section divider
```

**Example Site Map**:
```
Home
|
+-- Products
|   +-- Category Landing [Repeated per category]
|   |   +-- Product Detail [Repeated per product]
|   |       +-- Reviews Tab
|   |       +-- Specs Tab
|   +-- Compare Products
|   +-- Sale/Promotions
|
+-- Pricing
|   +-- Plans Comparison
|   +-- {Enterprise Contact Form}
|
+-- Documentation
|   +-- Getting Started
|   |   +-- Installation
|   |   +-- Quick Start
|   +-- API Reference [Repeated per endpoint]
|   +-- Guides [Repeated per guide]
|   +-- Changelog
|
+-- Blog
|   +-- Blog Index (paginated)
|   +-- Blog Post [Repeated per post]
|   +-- Category Archive [Repeated per category]
|
+-- Company
|   +-- About
|   +-- Team
|   +-- Careers
|   |   +-- Job Listing [Repeated per job]
|   +-- Press
|   +-- Contact
|
+-- Legal
|   +-- Privacy Policy
|   +-- Terms of Service
|   +-- Cookie Policy
|
+-- Account {Authenticated}
|   +-- Dashboard
|   +-- Settings
|   |   +-- Profile
|   |   +-- Billing
|   |   +-- Notifications
|   |   +-- Security
|   +-- Team Management {Admin role}
|
+-- Auth
    +-- Sign In
    +-- Sign Up
    +-- Reset Password
    +-- Verify Email
```

### Site Map Review Checklist
- [ ] Every page in the product is represented
- [ ] No page is more than 3-4 clicks from the home page
- [ ] Every page has a clear parent (except home)
- [ ] Categories have 5-9 items each (not 1-2 or 20+)
- [ ] Depth is balanced across branches
- [ ] Dynamic/repeated pages are noted
- [ ] Auth-gated pages are marked
- [ ] Role-restricted pages are marked
- [ ] External links are distinguished

---

## URL Structure Design

URLs are a critical part of IA. They are visible to users, shared in communications, used by search engines, and must remain stable over time.

### URL Design Principles

1. **Readable**: URLs should be human-readable and guessable
   - Good: `/products/running-shoes/nike-air-max-90`
   - Bad: `/p/cat-12/item-384729`

2. **Hierarchical**: URL structure should mirror IA hierarchy
   - Good: `/docs/api/authentication/oauth2`
   - Bad: `/docs/oauth2` (loses hierarchy context)

3. **Stable**: URLs should not change. When they must, redirect (301) the old URL.
   - A URL is a promise. Breaking it breaks bookmarks, links, and SEO.

4. **Lowercase**: Always lowercase, with hyphens for word separation
   - Good: `/blog/ux-design-patterns`
   - Bad: `/Blog/UX_Design_Patterns`

5. **No trailing slashes** (or always trailing slashes — be consistent)
   - Pick one and redirect the other

6. **No file extensions**: URLs are resources, not files
   - Good: `/about`
   - Bad: `/about.html`

7. **Query params for filtering, not structure**:
   - Category page: `/products/shoes` (not `/products?category=shoes`)
   - Filtered view: `/products/shoes?color=red&size=10`
   - Search: `/search?q=running+shoes`

### URL Template by Content Type
| Content Type | URL Pattern | Example |
|-------------|-------------|---------|
| Home page | `/` | `example.com/` |
| Category | `/[section]/[category]` | `/products/shoes` |
| Item/detail | `/[section]/[category]/[slug]` | `/products/shoes/nike-air-max` |
| Blog post | `/blog/[slug]` | `/blog/navigation-patterns` |
| Blog category | `/blog/category/[slug]` | `/blog/category/ux-design` |
| Documentation | `/docs/[section]/[page]` | `/docs/api/authentication` |
| User profile | `/[username]` or `/users/[username]` | `/@johndoe` or `/users/johndoe` |
| Search | `/search?q=[query]` | `/search?q=navigation` |
| Settings | `/settings/[section]` | `/settings/notifications` |
| API | `/api/v[n]/[resource]` | `/api/v2/users` |

### URL Pitfalls
| Pitfall | Example | Fix |
|---------|---------|-----|
| IDs in URLs | `/products/38472` | Use slugs: `/products/nike-air-max` |
| Deep nesting | `/a/b/c/d/e/f/item` | Flatten: max 3-4 segments |
| Encoded characters | `/products/running%20shoes` | Use hyphens: `/products/running-shoes` |
| Session IDs | `/page?sid=abc123` | Remove session from URL |
| Technology in URL | `/products.aspx` | Remove extensions |
| Versioning content | `/v2/products` | Version API, not content |

---

## Search vs. Browse Behavior

### When Users Search vs. Browse

Research by Jared Spool (UIE) and NNG shows two primary information-seeking behaviors:

**Known-item seeking** (Search): User knows what they want and wants to find it fast.
- Behavior: Go directly to search, type a specific query
- Example: "I need the React Router documentation"
- Nav solution: Prominent search bar, command palette, auto-complete

**Exploratory browsing** (Browse): User has a general goal but does not know exactly what they want.
- Behavior: Scan categories, click into interesting items, compare options
- Nav solution: Clear categories, filters, visual navigation, related items

**The 50/50 principle**: On most sites, approximately half of users start with search and half with browse. Your navigation must support both behaviors well. Never sacrifice one for the other.

### Search UX Best Practices
| Aspect | Best Practice |
|--------|--------------|
| Placement | Visible on every page (header or command palette) |
| Scope | Search everything by default; allow scope narrowing |
| Auto-suggest | Show after 1-2 characters; max 6-8 suggestions |
| Recent searches | Show on focus before typing |
| No results | Suggest alternatives, show popular items, check spelling |
| Filters | Post-search filters for refining results (faceted search) |
| Results | Show snippet, highlight matched terms, group by type |
| Mobile | Full-screen search overlay with auto-focus on keyboard |

---

## Faceted Navigation Design

Faceted navigation allows users to filter content by multiple dimensions (facets) simultaneously. Common in e-commerce, job boards, and search interfaces.

### Facet Types
| Type | Display | Example |
|------|---------|---------|
| **Checkbox list** | Multiple selection | Colors: Red, Blue, Green (select many) |
| **Radio list** | Single selection | Sort: Price low-high, Price high-low |
| **Range slider** | Continuous range | Price: $10 — $200 |
| **Toggle** | On/off | In stock only: Yes/No |
| **Color swatches** | Visual selection | Color: [red] [blue] [green] circles |
| **Star rating** | Minimum threshold | Rating: 4 stars and up |
| **Date range** | Temporal filtering | Posted: Last 7 days, Last 30 days |

### Faceted Navigation UX Rules

1. **Show active filters prominently**: Display selected filters as removable chips/tags above results
2. **Show result counts**: Each filter option shows how many results it will return: "Red (23)"
3. **Disable zero-result options**: Gray out options that would return 0 results (do not remove them)
4. **Apply filters immediately**: Do not require a separate "Apply" button (mobile exception: batch apply can be OK)
5. **URL-encode filters**: `?color=red&size=10&sort=price-asc` — every filter state is shareable
6. **Position**: Left sidebar on desktop, full-screen overlay or bottom sheet on mobile
7. **Order**: Most-used facets at the top, show 5-7 options per facet, "Show more" for the rest
8. **Clear all**: Prominent "Clear all filters" when any filter is active
9. **Mobile**: Filters behind a "Filter" button, opens full-screen or bottom sheet with all facets

### Filter Chip Pattern (Active Filters)
```css
.filter-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 12px 0;
}

.filter-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  background: #eff6ff;
  color: #2563eb;
  border: 1px solid #bfdbfe;
  border-radius: 16px;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
}

.filter-chip__remove {
  width: 16px;
  height: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: #2563eb;
  cursor: pointer;
  border-radius: 50%;
}

.filter-chip__remove:hover {
  background: #dbeafe;
}

.clear-all-filters {
  font-size: 13px;
  color: #6b7280;
  background: none;
  border: none;
  cursor: pointer;
  text-decoration: underline;
}
```

---

## IA Validation Methods

### Quantitative Validation

| Method | What It Measures | Sample Size | Tool |
|--------|-----------------|-------------|------|
| Tree test | Findability in the hierarchy | 50-100 | Treejack, UserZoom |
| First-click test | Correct initial navigation choice | 20-50 | Chalkmark, UsabilityHub |
| A/B test | Conversion impact of IA changes | 1000+ per variant | Optimizely, VWO |
| Analytics | Actual navigation behavior | Passive (existing traffic) | GA4, Mixpanel, Amplitude |
| Search logs | What users search for (IA gaps) | Passive | Search platform analytics |

### Qualitative Validation

| Method | What It Reveals | Participants | Duration |
|--------|----------------|-------------|----------|
| Usability test | Where users struggle to navigate | 5-8 | 30-60 min each |
| Think-aloud | User's reasoning about navigation choices | 5-8 | 30-60 min each |
| Card sort | How users group content | 15-20 | 15-30 min each |
| Contextual inquiry | How users navigate in their real environment | 5-8 | 60-120 min each |
| Diary study | Long-term navigation patterns and pain points | 10-15 | 1-4 weeks |

### Key Metrics from Analytics

| Metric | What It Indicates | Healthy Range |
|--------|------------------|---------------|
| **Bounce rate on nav pages** | Users arriving but not engaging | < 40% |
| **Exit rate by page** | Where users leave | Identify pages with > 50% exit rate |
| **Search-to-nav ratio** | Whether browse navigation is sufficient | < 30% search-first (except search-heavy products) |
| **Zero-result searches** | Content gaps in IA | < 5% of total searches |
| **Pogo-sticking** | Clicking a result, immediately going back, clicking another | Indicates bad labels or wrong content in a category |
| **Average clicks to task completion** | Navigation efficiency | 2-4 clicks for primary tasks |
| **Navigation path diversity** | Multiple paths to same content | Ideal: 1-2 dominant paths per task |

---

## IA Documentation Template

### IA Specification Document

```markdown
# Information Architecture Specification
## [Product Name] — Version [X.Y]
## Date: [YYYY-MM-DD]
## Author: [Name]

---

### 1. Research Summary
- **Users**: [Summary of target users and their mental models]
- **Content volume**: [Number of pages/items, growth rate]
- **Key findings from card sorting**: [Top groupings and labels]
- **Key findings from tree testing**: [Success rates, problem areas]

### 2. IA Principles
1. [Principle 1, e.g., "Task-based organization for daily users"]
2. [Principle 2, e.g., "Max 3 levels of hierarchy"]
3. [Principle 3, e.g., "Every page reachable within 3 clicks"]

### 3. Site Map
[Visual diagram or text tree showing all pages and hierarchy]

### 4. Navigation Specification
| Level | Pattern | Items | Behavior |
|-------|---------|-------|----------|
| Global | [e.g., Top nav bar] | [Items listed] | [Responsive behavior] |
| Local | [e.g., Sub-nav tabs] | [Items listed] | [Context-dependent] |
| Contextual | [e.g., Related links] | [Dynamic] | [Algorithm or editorial] |
| Utility | [e.g., Top-right cluster] | [Items listed] | [Always visible] |

### 5. URL Structure
| Section | URL Pattern | Example |
|---------|------------|---------|
| [Section name] | [Pattern] | [Example URL] |

### 6. Taxonomy / Labeling
| Internal Term | User-Facing Label | Rationale |
|--------------|-------------------|-----------|
| [Internal term] | [User label] | [Why this label was chosen] |

### 7. Search Specification
- Searchable content: [What is indexed]
- Auto-suggest: [Source and behavior]
- Facets/filters: [List of available filters]
- No-results strategy: [What happens when search fails]

### 8. Validation Results
| Test | Date | Key Result | Action Taken |
|------|------|------------|-------------|
| Open card sort | [Date] | [Result] | [Action] |
| Tree test v1 | [Date] | [Result] | [Action] |
| Tree test v2 | [Date] | [Result] | [Action] |
| Usability test | [Date] | [Result] | [Action] |

### 9. Governance
- **Content owners**: [Who owns each section]
- **Review cadence**: [How often IA is reviewed]
- **Change process**: [How IA changes are proposed and validated]
```

---

## IA Tools Reference

| Tool | Purpose | Type | Price |
|------|---------|------|-------|
| **Optimal Workshop** | Card sorting, tree testing, first-click | Research platform | Paid |
| **Treejack** | Tree testing | Part of Optimal Workshop | Paid |
| **UserZoom** | Full UX research including IA methods | Enterprise research | Paid |
| **UsabilityHub (Lyssna)** | First-click, preference, five-second tests | Quick testing | Freemium |
| **CardSort.io** | Simple card sorting | Standalone | Free/Paid |
| **Miro / FigJam** | Collaborative site map creation | Whiteboard | Freemium |
| **Screaming Frog** | Site crawling for content inventory | SEO tool | Freemium |
| **Sitebulb** | Visual site crawling and IA analysis | SEO tool | Paid |
| **Google Analytics** | Navigation behavior, search logs | Analytics | Free |
| **Hotjar / FullStory** | Click heatmaps, navigation recordings | Behavior analytics | Freemium |
| **Algolia / Elasticsearch** | Search implementation with analytics | Search platform | Freemium |
| **Airtable / Notion** | Content inventory management | Database | Freemium |
| **OmniGraffle / draw.io** | Site map diagramming | Diagramming | Freemium |
| **Whimsical** | Flowcharts, mind maps, site maps | Diagramming | Freemium |
| **XMind / MindNode** | Mind mapping for brainstorming IA | Mind mapping | Freemium |

---

## IA Patterns by Product Type

### E-Commerce IA
```
Home
  Categories (hierarchical, 3-7 top-level)
    Subcategories (2-3 levels max)
      Product listing (filterable, sortable)
        Product detail
  Account (Orders, Addresses, Payment, Wishlist)
  Cart --> Checkout (3-5 steps)
  Help / FAQ
  Store locator (if physical stores)
```
Key decisions:
- Category structure from card sorting, not merchandising team assumptions
- Product pages accessible from multiple category paths (product belongs to running shoes AND Nike)
- Search with category-scoped and global options

### SaaS Application IA
```
Dashboard (home)
  Feature Area 1 (list --> detail --> sub-views)
  Feature Area 2
  Feature Area 3
  Integrations / API
  Settings (grouped: Profile, Team, Billing, Security, Notifications)
  Help / Docs (external link or embedded)
  Admin (role-restricted: Users, Roles, Audit log)
```
Key decisions:
- Dashboard as home vs. most-used feature as home
- Settings: one flat list vs. grouped categories
- Admin vs. Settings separation (admin = organization, settings = personal)

### Content / Media IA
```
Home / Feed (algorithmic or chronological)
  Browse by Category / Topic
  Browse by Format (articles, videos, podcasts)
  Individual Content Item
  Search (with faceted results)
  Saved / Bookmarked
  User Profile
  Settings
```
Key decisions:
- Algorithmic vs. chronological home feed
- Category discovery: grid, carousel, or sidebar
- Content detail page: inline navigation to next/related content

### Documentation Site IA
```
Home (getting started guide)
  Section 1: Getting Started
    Installation
    Quick Start
    Configuration
  Section 2: Guides
    Guide 1
    Guide 2
  Section 3: API Reference
    Endpoint Group 1
      Endpoint 1
      Endpoint 2
    Endpoint Group 2
  Section 4: Examples
  Changelog
  Community / Support
```
Key decisions:
- Getting started must be the entry point, not the API reference
- Sidebar with deep nesting vs. search-first approach
- Version selector for multi-version documentation

### Enterprise / Internal Tool IA
```
Home / Dashboard
  Module 1 (role-based visibility)
    Sub-feature 1
    Sub-feature 2
  Module 2
  Reports / Analytics
  Admin
    User management
    Role management
    Audit log
    System settings
  My Account
    Profile
    Preferences
    Notifications
```
Key decisions:
- Role-based navigation: show only what each role can access
- Module-based sidebar that changes per module
- Admin separation from daily-use features

---

## IA Governance

### Content Lifecycle Management

| Stage | IA Action |
|-------|----------|
| **Create** | New content placed in correct category, URL assigned, nav updated if needed |
| **Publish** | Content appears in navigation, search index, sitemap |
| **Update** | Content updated in place; URL unchanged; last-updated date refreshed |
| **Archive** | Content removed from navigation but URL still works (with "archived" notice) |
| **Redirect** | Old URL 301-redirected to new location; sitemap updated |
| **Delete** | URL returns 410 Gone; removed from search index and sitemap |

### IA Review Schedule

| Review Type | Frequency | Trigger |
|-------------|-----------|---------|
| **Analytics review** | Monthly | Check nav usage, search logs, bounce rates |
| **Content audit** | Quarterly | Review accuracy, relevance, completeness |
| **Tree test** | Biannually or after major changes | Validate findability after IA changes |
| **Full IA review** | Annually or with major redesign | Card sorting, tree testing, site map update |
| **Competitive IA review** | Annually | Compare IA with competitors' structures |

### Change Management for IA

1. **Propose**: Document the proposed change and rationale
2. **Validate**: Tree test or first-click test the proposed change
3. **Redirect**: Set up 301 redirects for any URL changes
4. **Communicate**: Notify team and users of navigation changes
5. **Monitor**: Track analytics for 30 days post-change to verify improvement
6. **Rollback plan**: Have a plan to revert if metrics decline
