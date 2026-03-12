# Creative & Developer Page Templates — Complete Implementation Guide

## Overview

This reference provides complete page-level templates for 5 creative/portfolio pages and 5 developer tool pages. Each template includes block sequence, typography, color application, spacing rhythm, component selection, responsive behavior, and React/TSX skeletons.

Creative pages emphasize visual storytelling, editorial typography, and portfolio presentation. Developer pages emphasize technical clarity, code-first aesthetics, and monospace typography.

---

## PART 1: CREATIVE / PORTFOLIO TEMPLATES

### Creative Design Principles
1. **Visual storytelling** — The portfolio itself is the product. Design quality proves competence
2. **Editorial typography** — Serif/display fonts for personality, generous whitespace
3. **Project-centric** — Projects are the hero, not the chrome
4. **Personality** — The design should feel handcrafted, not templated
5. **Performance** — Fast loading despite heavy imagery

### Typography Direction
Creative portfolios use typography as a primary design element:
- Display fonts for headlines (often serif or distinctive sans)
- Body text in clean sans-serif for readability
- Generous line-heights and letter-spacing for editorial feel
- Type scale creates dramatic hierarchy

---

## 1. Portfolio Landing Page

### Block Sequence
1. Hero section (name/title + brief tagline + scroll indicator)
2. Selected work grid (3-6 featured projects with hover effects)
3. Brief about section (photo + 2-3 sentence bio)
4. Client logos or recognition strip
5. Contact CTA
6. Minimal footer

### Typography Map
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Hero name | Editorial New / Playfair Display | 400 | 72px | 80px |
| Hero tagline | Inter / Neue Haas | 300 | 20px | 32px |
| Project title | Editorial New / Playfair Display | 400 | 28px | 36px |
| Project category | Inter | 400 | 13px | 18px |
| About heading | Editorial New / Playfair Display | 400 | 40px | 48px |
| Body text | Inter | 400 | 16px | 28px |
| Nav links | Inter | 400 | 14px | 20px |

### Color Application
```
Background:             #FAFAF8 (warm off-white)
Text primary:           #1A1A1A
Text secondary:         #666666
Text muted:             #999999
Accent:                 #000000 (or personal brand color)
Project card bg:        #F0F0EE
Project card hover:     Scale 1.02 + shadow
Link underline:         #1A1A1A, 1px
Border:                 #E5E5E3
Selection bg:           #D4D4D0
```

### Spacing Rhythm
```
Hero section:           100vh (full viewport)
Section padding:        120px desktop / 80px mobile
Project grid gap:       24px desktop / 16px mobile
Container max-width:    1200px
Container padding:      0 48px desktop / 0 24px mobile
Footer padding:         48px vertical
```

### React/TSX Skeleton
```tsx
export function PortfolioLanding() {
  const projects = [
    { title: 'Brand Identity for Aura', category: 'Branding', year: '2026', color: '#F0EBE3' },
    { title: 'Fintech App Redesign', category: 'Product Design', year: '2025', color: '#E3ECF0' },
    { title: 'Editorial Website', category: 'Web Design', year: '2025', color: '#E8F0E3' },
    { title: 'Packaging System', category: 'Visual Design', year: '2025', color: '#F0E3E8' },
  ];

  return (
    <div className="min-h-screen bg-[#FAFAF8] text-[#1A1A1A]">
      {/* Nav */}
      <nav className="fixed top-0 left-0 right-0 z-50 bg-[#FAFAF8]/90 backdrop-blur-sm">
        <div className="mx-auto flex h-16 max-w-[1200px] items-center justify-between px-12">
          <a href="/" className="text-sm font-medium">Alex Designer</a>
          <div className="flex items-center gap-8">
            <a href="#work" className="text-sm text-[#666] hover:text-[#1A1A1A] transition-colors">Work</a>
            <a href="#about" className="text-sm text-[#666] hover:text-[#1A1A1A] transition-colors">About</a>
            <a href="#contact" className="text-sm text-[#666] hover:text-[#1A1A1A] transition-colors">Contact</a>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="flex min-h-screen flex-col items-center justify-center px-12">
        <div className="max-w-[800px] text-center">
          <h1 className="font-serif text-[72px] font-normal leading-[80px] tracking-[-0.02em]">
            Alex Designer
          </h1>
          <p className="mt-6 text-xl font-light leading-8 text-[#666]">
            Product designer crafting thoughtful digital experiences for startups and studios.
          </p>
        </div>
        <div className="absolute bottom-12 animate-bounce">
          <span className="text-sm text-[#999]">scroll</span>
        </div>
      </section>

      {/* Selected Work */}
      <section id="work" className="py-[120px]">
        <div className="mx-auto max-w-[1200px] px-12">
          <h2 className="font-serif text-[40px] font-normal">Selected Work</h2>
          <div className="mt-16 grid gap-6 md:grid-cols-2">
            {projects.map((p) => (
              <a key={p.title} href="#" className="group relative overflow-hidden rounded-2xl transition-transform hover:scale-[1.02]">
                <div className="aspect-[4/3] w-full" style={{ backgroundColor: p.color }}>
                  <div className="flex h-full items-center justify-center">
                    <span className="text-[#999] opacity-0 group-hover:opacity-100 transition-opacity">View Project</span>
                  </div>
                </div>
                <div className="mt-4">
                  <div className="flex items-center justify-between">
                    <h3 className="font-serif text-[22px]">{p.title}</h3>
                    <span className="text-sm text-[#999]">{p.year}</span>
                  </div>
                  <p className="mt-1 text-sm text-[#666]">{p.category}</p>
                </div>
              </a>
            ))}
          </div>
        </div>
      </section>

      {/* About */}
      <section id="about" className="bg-[#F0F0EE] py-[120px]">
        <div className="mx-auto max-w-[1200px] px-12 md:flex md:items-center md:gap-20">
          <div className="md:w-1/3">
            <div className="aspect-[3/4] rounded-2xl bg-[#E5E5E3]" />
          </div>
          <div className="mt-10 md:mt-0 md:w-2/3">
            <h2 className="font-serif text-[40px] font-normal">About</h2>
            <p className="mt-6 text-lg leading-8 text-[#666]">
              I am a product designer with 8 years of experience creating digital products for companies like Stripe, Figma, and Vercel. I believe in design that serves people first.
            </p>
            <p className="mt-4 text-lg leading-8 text-[#666]">
              Currently available for freelance projects and consulting.
            </p>
            <div className="mt-8 flex gap-6">
              <a href="#" className="text-sm text-[#1A1A1A] underline underline-offset-4">Resume</a>
              <a href="#" className="text-sm text-[#1A1A1A] underline underline-offset-4">LinkedIn</a>
              <a href="#" className="text-sm text-[#1A1A1A] underline underline-offset-4">Dribbble</a>
            </div>
          </div>
        </div>
      </section>

      {/* Contact */}
      <section id="contact" className="py-[120px]">
        <div className="mx-auto max-w-[1200px] px-12 text-center">
          <h2 className="font-serif text-[48px] font-normal">Let's work together</h2>
          <p className="mt-4 text-lg text-[#666]">Have a project in mind? I would love to hear about it.</p>
          <a href="mailto:hello@alexdesigner.com" className="mt-8 inline-block rounded-full bg-[#1A1A1A] px-8 py-4 text-sm font-medium text-white hover:bg-black transition-colors">
            hello@alexdesigner.com
          </a>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-[#E5E5E3] py-12">
        <div className="mx-auto max-w-[1200px] px-12 flex items-center justify-between">
          <span className="text-sm text-[#999]">2026 Alex Designer</span>
          <div className="flex gap-6">
            <a href="#" className="text-sm text-[#999] hover:text-[#1A1A1A]">Twitter</a>
            <a href="#" className="text-sm text-[#999] hover:text-[#1A1A1A]">Instagram</a>
          </div>
        </div>
      </footer>
    </div>
  );
}
```

---

## 2. Project Case Study Page

### Block Sequence
1. Hero (project title + category + hero image, full-width)
2. Project overview (role, timeline, team, tools)
3. Problem statement
4. Research and discovery
5. Design process (with process images)
6. Solution showcase (full-width screenshots/mockups)
7. Results and impact (metrics)
8. Next project link

### Typography Map
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Project title | Editorial New / Playfair | 400 | 56px | 64px |
| Section heading | Editorial New / Playfair | 400 | 32px | 40px |
| Body paragraph | Inter | 400 | 17px | 30px |
| Meta label | Inter | 500 | 12px | 16px |
| Meta value | Inter | 400 | 15px | 22px |
| Pull quote | Editorial New / Playfair | 400 italic | 28px | 40px |
| Caption | Inter | 400 | 13px | 20px |

### React/TSX Skeleton
```tsx
export function CaseStudy() {
  return (
    <div className="min-h-screen bg-[#FAFAF8] text-[#1A1A1A]">
      {/* Hero */}
      <section className="pt-24">
        <div className="mx-auto max-w-[900px] px-6">
          <p className="text-sm text-[#999]">Branding / 2026</p>
          <h1 className="mt-4 font-serif text-[56px] font-normal leading-[64px] tracking-[-0.02em]">
            Brand Identity for Aura
          </h1>
          <p className="mt-6 text-lg leading-8 text-[#666]">
            A complete brand system for a wellness technology startup, from strategy through implementation.
          </p>
        </div>
        <div className="mt-12 aspect-[21/9] w-full bg-[#F0EBE3]" />
      </section>

      {/* Overview */}
      <section className="py-20">
        <div className="mx-auto max-w-[900px] px-6">
          <div className="grid grid-cols-2 gap-8 sm:grid-cols-4">
            {[
              { label: 'Role', value: 'Lead Designer' },
              { label: 'Timeline', value: '8 weeks' },
              { label: 'Team', value: '3 designers' },
              { label: 'Tools', value: 'Figma, After Effects' },
            ].map((meta) => (
              <div key={meta.label}>
                <p className="text-xs font-medium uppercase tracking-wider text-[#999]">{meta.label}</p>
                <p className="mt-2 text-[15px] text-[#1A1A1A]">{meta.value}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Problem */}
      <section className="py-12">
        <div className="mx-auto max-w-[900px] px-6">
          <h2 className="font-serif text-[32px] font-normal">The Challenge</h2>
          <p className="mt-6 text-[17px] leading-[30px] text-[#666]">
            Aura needed a brand identity that would position them at the intersection of technology and wellness. The existing identity felt clinical and cold, failing to communicate the warm, human-centered approach that defined their product philosophy.
          </p>
        </div>
      </section>

      {/* Process Images */}
      <section className="py-12">
        <div className="mx-auto max-w-[1200px] px-6 grid gap-4 md:grid-cols-2">
          <div className="aspect-[4/3] rounded-xl bg-[#F0F0EE]" />
          <div className="aspect-[4/3] rounded-xl bg-[#F0F0EE]" />
        </div>
        <div className="mx-auto max-w-[900px] px-6">
          <p className="mt-4 text-sm text-[#999]">Early explorations: moodboard and initial concepts</p>
        </div>
      </section>

      {/* Solution */}
      <section className="py-12">
        <div className="mx-auto max-w-[900px] px-6">
          <h2 className="font-serif text-[32px] font-normal">The Solution</h2>
          <p className="mt-6 text-[17px] leading-[30px] text-[#666]">
            We developed a brand system rooted in organic geometry and a warm, muted color palette. The logomark combines a breathing circle motif with the letter A, symbolizing both the company name and the act of mindful breathing that is central to their product.
          </p>
        </div>
        <div className="mx-auto mt-12 max-w-[1200px] px-6">
          <div className="aspect-[16/9] rounded-xl bg-[#E3ECF0]" />
        </div>
      </section>

      {/* Pull Quote */}
      <section className="py-16">
        <div className="mx-auto max-w-[900px] px-6">
          <blockquote className="border-l-2 border-[#1A1A1A] pl-8">
            <p className="font-serif text-[28px] font-normal italic leading-[40px] text-[#1A1A1A]">
              "The new brand perfectly captures who we are — warm, precise, and deeply human."
            </p>
            <cite className="mt-4 block text-sm not-italic text-[#999]">— Maya Chen, CEO of Aura</cite>
          </blockquote>
        </div>
      </section>

      {/* Results */}
      <section className="bg-[#F0F0EE] py-20">
        <div className="mx-auto max-w-[900px] px-6">
          <h2 className="font-serif text-[32px] font-normal">Impact</h2>
          <div className="mt-10 grid gap-8 sm:grid-cols-3">
            {[
              { metric: '340%', label: 'Increase in brand recognition' },
              { metric: '2.5x', label: 'Improvement in conversion' },
              { metric: '96%', label: 'Positive stakeholder feedback' },
            ].map((r) => (
              <div key={r.label}>
                <p className="font-serif text-[48px] font-normal text-[#1A1A1A]">{r.metric}</p>
                <p className="mt-2 text-sm text-[#666]">{r.label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Next Project */}
      <section className="py-20">
        <div className="mx-auto max-w-[900px] px-6 text-center">
          <p className="text-sm text-[#999]">Next Project</p>
          <a href="#" className="mt-2 inline-block font-serif text-[32px] text-[#1A1A1A] hover:text-[#666] transition-colors">
            Fintech App Redesign
          </a>
        </div>
      </section>
    </div>
  );
}
```

---

## 3. About / Bio Page

### Block Sequence
1. Hero (large name + portrait photo)
2. Extended bio (2-3 paragraphs)
3. Experience timeline
4. Skills/expertise tags
5. Awards/recognition
6. Personal interests
7. Contact CTA

### Key Design: Large portrait, editorial typography, generous whitespace, personal warmth

---

## 4. Contact Page

### Block Sequence
1. Heading (brief, inviting copy)
2. Contact form (name, email, project type, message)
3. Alternative contact methods (email, social links)
4. Availability status
5. Location/timezone

```tsx
export function ContactPage() {
  return (
    <div className="min-h-screen bg-[#FAFAF8] text-[#1A1A1A]">
      <div className="mx-auto max-w-[900px] px-12 py-24 md:flex md:gap-20">
        <div className="md:w-1/2">
          <h1 className="font-serif text-[48px] font-normal leading-[56px]">Get in touch</h1>
          <p className="mt-6 text-lg leading-8 text-[#666]">
            Currently accepting new projects for Q2 2026. Tell me about your project and I will get back to you within 24 hours.
          </p>
          <div className="mt-10 space-y-4">
            <div>
              <p className="text-xs font-medium uppercase tracking-wider text-[#999]">Email</p>
              <a href="mailto:hello@alexdesigner.com" className="mt-1 text-[15px] text-[#1A1A1A] underline underline-offset-4">hello@alexdesigner.com</a>
            </div>
            <div>
              <p className="text-xs font-medium uppercase tracking-wider text-[#999]">Social</p>
              <div className="mt-1 flex gap-4">
                <a href="#" className="text-[15px] text-[#1A1A1A] underline underline-offset-4">Twitter</a>
                <a href="#" className="text-[15px] text-[#1A1A1A] underline underline-offset-4">LinkedIn</a>
                <a href="#" className="text-[15px] text-[#1A1A1A] underline underline-offset-4">Dribbble</a>
              </div>
            </div>
            <div>
              <p className="text-xs font-medium uppercase tracking-wider text-[#999]">Availability</p>
              <p className="mt-1 flex items-center gap-2 text-[15px]">
                <span className="h-2 w-2 rounded-full bg-green-500"></span>
                Available for projects
              </p>
            </div>
            <div>
              <p className="text-xs font-medium uppercase tracking-wider text-[#999]">Location</p>
              <p className="mt-1 text-[15px] text-[#666]">San Francisco, CA (PST)</p>
            </div>
          </div>
        </div>

        <div className="mt-12 md:mt-0 md:w-1/2">
          <form className="space-y-5">
            <div>
              <label className="text-sm font-medium text-[#1A1A1A]">Name</label>
              <input type="text" className="mt-2 w-full rounded-lg border border-[#E5E5E3] bg-white px-4 py-3 text-[15px] focus:border-[#1A1A1A] focus:outline-none" />
            </div>
            <div>
              <label className="text-sm font-medium text-[#1A1A1A]">Email</label>
              <input type="email" className="mt-2 w-full rounded-lg border border-[#E5E5E3] bg-white px-4 py-3 text-[15px] focus:border-[#1A1A1A] focus:outline-none" />
            </div>
            <div>
              <label className="text-sm font-medium text-[#1A1A1A]">Project type</label>
              <select className="mt-2 w-full rounded-lg border border-[#E5E5E3] bg-white px-4 py-3 text-[15px] text-[#666] focus:border-[#1A1A1A] focus:outline-none">
                <option>Select a type</option>
                <option>Brand Identity</option>
                <option>Product Design</option>
                <option>Web Design</option>
                <option>Consulting</option>
                <option>Other</option>
              </select>
            </div>
            <div>
              <label className="text-sm font-medium text-[#1A1A1A]">Tell me about your project</label>
              <textarea rows={5} className="mt-2 w-full rounded-lg border border-[#E5E5E3] bg-white px-4 py-3 text-[15px] focus:border-[#1A1A1A] focus:outline-none resize-none" />
            </div>
            <button type="submit" className="w-full rounded-lg bg-[#1A1A1A] py-3.5 text-sm font-medium text-white hover:bg-black transition-colors">
              Send message
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
```

---

## 5. Blog / Journal Page

### Block Sequence
1. Page header (title + optional tagline)
2. Featured post (large hero card)
3. Post grid (cards with image, title, excerpt, date)
4. Category/tag filter
5. Newsletter signup
6. Pagination

### Typography: Editorial, generous line-heights, pull quotes in posts, code blocks for technical content

```tsx
export function BlogPage() {
  const posts = [
    { title: 'On the Craft of Interface Design', excerpt: 'Reflections on what makes digital products feel genuinely well-made.', date: 'Mar 8, 2026', category: 'Design', featured: true },
    { title: 'Building a Design System from Scratch', excerpt: 'Lessons learned creating a component library for a growing startup.', date: 'Feb 22, 2026', category: 'Systems', featured: false },
    { title: 'The Typography of Trust', excerpt: 'How typeface choices subconsciously communicate credibility.', date: 'Feb 10, 2026', category: 'Typography', featured: false },
    { title: 'Color in Context', excerpt: 'Why the same color means different things in different industries.', date: 'Jan 28, 2026', category: 'Color', featured: false },
  ];

  return (
    <div className="min-h-screen bg-[#FAFAF8] text-[#1A1A1A]">
      <div className="mx-auto max-w-[900px] px-12 py-24">
        <h1 className="font-serif text-[40px] font-normal">Journal</h1>
        <p className="mt-3 text-lg text-[#666]">Thoughts on design, technology, and craft.</p>

        {/* Featured Post */}
        <a href="#" className="mt-12 block group">
          <div className="aspect-[21/9] rounded-2xl bg-[#F0F0EE] overflow-hidden" />
          <div className="mt-6">
            <p className="text-sm text-[#999]">{posts[0].date} / {posts[0].category}</p>
            <h2 className="mt-2 font-serif text-[32px] font-normal group-hover:text-[#666] transition-colors">{posts[0].title}</h2>
            <p className="mt-3 text-[17px] leading-7 text-[#666]">{posts[0].excerpt}</p>
          </div>
        </a>

        {/* Post Grid */}
        <div className="mt-16 grid gap-10 md:grid-cols-2">
          {posts.slice(1).map((post) => (
            <a key={post.title} href="#" className="group">
              <div className="aspect-[16/9] rounded-xl bg-[#F0F0EE]" />
              <div className="mt-4">
                <p className="text-sm text-[#999]">{post.date} / {post.category}</p>
                <h3 className="mt-2 font-serif text-xl font-normal group-hover:text-[#666] transition-colors">{post.title}</h3>
                <p className="mt-2 text-sm leading-6 text-[#666]">{post.excerpt}</p>
              </div>
            </a>
          ))}
        </div>

        {/* Newsletter */}
        <div className="mt-20 rounded-2xl bg-[#F0F0EE] p-10 text-center">
          <h3 className="font-serif text-2xl font-normal">Subscribe to the newsletter</h3>
          <p className="mt-2 text-sm text-[#666]">Monthly thoughts on design and craft. No spam.</p>
          <div className="mx-auto mt-6 flex max-w-[400px] gap-3">
            <input type="email" placeholder="your@email.com" className="flex-1 rounded-lg border border-[#E5E5E3] bg-white px-4 py-2.5 text-sm focus:border-[#1A1A1A] focus:outline-none" />
            <button className="rounded-lg bg-[#1A1A1A] px-5 py-2.5 text-sm font-medium text-white hover:bg-black">Subscribe</button>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## PART 2: DEVELOPER TOOL TEMPLATES

### Developer Design Principles
1. **Code-first** — Monospace typography, syntax highlighting, terminal aesthetics
2. **Information density** — Developers want high density, not excessive whitespace
3. **Dark mode preference** — Most developer tools default to dark
4. **Copy-paste friendly** — Code blocks with copy buttons
5. **Fast navigation** — Command palettes, keyboard shortcuts, deep linking

### Typography Direction
Developer tools use a dual-font strategy:
- **Monospace** for code, API endpoints, CLI commands, terminal output
- **Sans-serif** for documentation prose, headings, UI labels
- Strict monospace for anything a developer might copy

---

## 6. Developer Documentation Page

### Block Sequence
1. Documentation nav (sidebar with nested sections)
2. Page header (title + last updated + edit link)
3. Content area (prose + code blocks + callouts)
4. Table of contents (right sidebar, scroll-spy)
5. Navigation (prev/next)
6. Feedback widget

### Typography Map
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Sidebar nav | Inter | 400 | 14px | 28px |
| Page title | Inter | 700 | 32px | 40px |
| Section heading (h2) | Inter | 600 | 24px | 32px |
| Section heading (h3) | Inter | 600 | 18px | 28px |
| Body text | Inter | 400 | 15px | 26px |
| Code inline | JetBrains Mono / Fira Code | 400 | 14px | 20px |
| Code block | JetBrains Mono / Fira Code | 400 | 13px | 22px |
| Callout text | Inter | 400 | 14px | 22px |
| TOC link | Inter | 400 | 13px | 24px |

### Color Application
```
Background:             #0A0A0A
Sidebar bg:             #000000 border-right: 1px solid #1A1A1A
Content bg:             #0A0A0A
Code block bg:          #111111 border: 1px solid #1E1E1E
Code text:              #E4E4E7
Inline code bg:         #1A1A1A
Inline code text:       #E4E4E7
Syntax keyword:         #C084FC (purple)
Syntax string:          #86EFAC (green)
Syntax comment:         #6B7280 (gray)
Syntax function:        #93C5FD (blue)
Syntax number:          #FDE68A (yellow)
Callout info bg:        #0C4A6E/20 border-left: 3px solid #0EA5E9
Callout warning bg:     #713F12/20 border-left: 3px solid #F59E0B
Callout error bg:       #7F1D1D/20 border-left: 3px solid #EF4444
Link:                   #0EA5E9
Text primary:           #E4E4E7
Text secondary:         #A1A1AA
TOC active:             #FFFFFF
TOC inactive:           #71717A
```

### React/TSX Skeleton
```tsx
export function DevDocs() {
  return (
    <div className="flex min-h-screen bg-[#0A0A0A]">
      {/* Sidebar */}
      <aside className="hidden w-64 overflow-y-auto border-r border-[#1A1A1A] bg-black p-5 lg:block">
        <a href="/" className="text-sm font-bold text-white">DevTool</a>
        <div className="mt-2 text-xs text-[#71717A]">v2.4.0</div>

        <div className="mt-6">
          <input type="search" placeholder="Search docs..." className="w-full rounded-md border border-[#1A1A1A] bg-[#111] px-3 py-2 text-xs text-white placeholder:text-[#52525B] focus:border-[#0EA5E9] focus:outline-none" />
        </div>

        <nav className="mt-6 space-y-1">
          {[
            { section: 'Getting Started', items: ['Introduction', 'Installation', 'Quick Start'] },
            { section: 'Core Concepts', items: ['Configuration', 'Authentication', 'Error Handling'] },
            { section: 'API Reference', items: ['REST API', 'GraphQL', 'Webhooks', 'SDK'] },
            { section: 'Guides', items: ['Deployment', 'Testing', 'Migration'] },
          ].map((group) => (
            <div key={group.section} className="mt-4">
              <p className="text-xs font-semibold uppercase tracking-wider text-[#52525B]">{group.section}</p>
              <div className="mt-2 space-y-0.5">
                {group.items.map((item) => (
                  <a key={item} href="#" className={`block rounded-md px-3 py-1.5 text-sm ${
                    item === 'Installation' ? 'bg-[#0EA5E9]/10 text-[#0EA5E9]' : 'text-[#A1A1AA] hover:text-white'
                  }`}>
                    {item}
                  </a>
                ))}
              </div>
            </div>
          ))}
        </nav>
      </aside>

      {/* Content */}
      <main className="flex-1 overflow-y-auto px-12 py-10">
        <div className="mx-auto max-w-[720px]">
          <div className="flex items-center gap-3 text-xs text-[#71717A]">
            <span>Getting Started</span>
            <span>/</span>
            <span className="text-[#A1A1AA]">Installation</span>
          </div>

          <h1 className="mt-4 text-[32px] font-bold text-white">Installation</h1>
          <p className="mt-2 text-sm text-[#71717A]">Last updated Mar 10, 2026</p>

          <div className="mt-8 space-y-6">
            <p className="text-[15px] leading-[26px] text-[#A1A1AA]">
              Install DevTool using your preferred package manager. The package works with Node.js 18+ and supports both ESM and CommonJS.
            </p>

            {/* Code Block */}
            <div className="rounded-lg border border-[#1E1E1E] bg-[#111]">
              <div className="flex items-center justify-between border-b border-[#1E1E1E] px-4 py-2">
                <div className="flex gap-4">
                  {['npm', 'yarn', 'pnpm'].map((pm, i) => (
                    <button key={pm} className={`text-xs font-medium ${i === 0 ? 'text-white' : 'text-[#52525B]'}`}>{pm}</button>
                  ))}
                </div>
                <button className="text-xs text-[#52525B] hover:text-white">Copy</button>
              </div>
              <pre className="overflow-x-auto p-4">
                <code className="font-mono text-[13px] leading-[22px]">
                  <span className="text-[#86EFAC]">npm install</span> <span className="text-[#E4E4E7]">@devtool/core</span>
                </code>
              </pre>
            </div>

            <h2 className="text-2xl font-semibold text-white">Configuration</h2>
            <p className="text-[15px] leading-[26px] text-[#A1A1AA]">
              Create a configuration file in your project root:
            </p>

            {/* Code Block with Syntax */}
            <div className="rounded-lg border border-[#1E1E1E] bg-[#111]">
              <div className="flex items-center justify-between border-b border-[#1E1E1E] px-4 py-2">
                <span className="text-xs text-[#52525B]">devtool.config.ts</span>
                <button className="text-xs text-[#52525B] hover:text-white">Copy</button>
              </div>
              <pre className="overflow-x-auto p-4">
                <code className="font-mono text-[13px] leading-[22px]">
{`import { defineConfig } from '@devtool/core'

export default defineConfig({
  apiKey: process.env.DEVTOOL_API_KEY,
  project: 'my-project',
  environment: 'production',
})`}
                </code>
              </pre>
            </div>

            {/* Info Callout */}
            <div className="rounded-lg border-l-[3px] border-[#0EA5E9] bg-[#0C4A6E]/20 p-4">
              <p className="text-xs font-semibold text-[#0EA5E9]">Note</p>
              <p className="mt-1 text-sm text-[#A1A1AA]">
                Never commit your API key to version control. Use environment variables or a secrets manager.
              </p>
            </div>

            {/* Warning Callout */}
            <div className="rounded-lg border-l-[3px] border-[#F59E0B] bg-[#713F12]/20 p-4">
              <p className="text-xs font-semibold text-[#F59E0B]">Warning</p>
              <p className="mt-1 text-sm text-[#A1A1AA]">
                Version 2.x introduces breaking changes from 1.x. See the migration guide before upgrading.
              </p>
            </div>
          </div>

          {/* Navigation */}
          <div className="mt-12 flex items-center justify-between border-t border-[#1A1A1A] pt-8">
            <a href="#" className="text-sm text-[#0EA5E9] hover:underline">Previous: Introduction</a>
            <a href="#" className="text-sm text-[#0EA5E9] hover:underline">Next: Quick Start</a>
          </div>

          {/* Feedback */}
          <div className="mt-8 flex items-center gap-4 border-t border-[#1A1A1A] pt-8">
            <span className="text-sm text-[#71717A]">Was this helpful?</span>
            <button className="rounded-md border border-[#1A1A1A] px-3 py-1 text-xs text-[#71717A] hover:text-white">Yes</button>
            <button className="rounded-md border border-[#1A1A1A] px-3 py-1 text-xs text-[#71717A] hover:text-white">No</button>
          </div>
        </div>
      </main>

      {/* TOC */}
      <aside className="hidden w-48 overflow-y-auto p-6 xl:block">
        <p className="text-xs font-semibold uppercase tracking-wider text-[#52525B]">On this page</p>
        <nav className="mt-4 space-y-2">
          {['Installation', 'Configuration', 'Environment Variables', 'Verification', 'Troubleshooting'].map((item, i) => (
            <a key={item} href="#" className={`block text-[13px] ${i === 0 ? 'text-white font-medium' : 'text-[#71717A] hover:text-white'}`}>
              {item}
            </a>
          ))}
        </nav>
      </aside>
    </div>
  );
}
```

---

## 7. API Reference Page

### Block Sequence
1. Endpoint header (method badge + path + description)
2. Parameters table (name, type, required, description)
3. Request example (with language tabs)
4. Response example (JSON with syntax highlighting)
5. Error codes table
6. Try it (interactive API explorer, optional)

```tsx
export function APIReference() {
  return (
    <div className="min-h-screen bg-[#0A0A0A] px-12 py-10">
      <div className="mx-auto max-w-[900px]">
        {/* Endpoint Header */}
        <div className="flex items-center gap-3">
          <span className="rounded-md bg-[#15803D] px-2.5 py-1 font-mono text-xs font-bold text-white">GET</span>
          <code className="font-mono text-lg text-white">/v1/users/:id</code>
        </div>
        <p className="mt-3 text-[15px] text-[#A1A1AA]">Retrieve a user by their unique identifier.</p>

        {/* Authentication */}
        <div className="mt-6 rounded-lg bg-[#111] p-4 border border-[#1E1E1E]">
          <p className="text-xs font-semibold text-[#A1A1AA]">Authentication</p>
          <p className="mt-1 text-sm text-[#71717A]">
            Requires <code className="rounded bg-[#1A1A1A] px-1.5 py-0.5 font-mono text-xs text-[#E4E4E7]">Bearer token</code> in the Authorization header.
          </p>
        </div>

        {/* Parameters */}
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-white">Path Parameters</h2>
          <div className="mt-4 rounded-lg border border-[#1E1E1E] overflow-hidden">
            <table className="w-full">
              <thead>
                <tr className="border-b border-[#1E1E1E] bg-[#111]">
                  <th className="px-4 py-3 text-left text-xs font-medium text-[#71717A]">Name</th>
                  <th className="px-4 py-3 text-left text-xs font-medium text-[#71717A]">Type</th>
                  <th className="px-4 py-3 text-left text-xs font-medium text-[#71717A]">Required</th>
                  <th className="px-4 py-3 text-left text-xs font-medium text-[#71717A]">Description</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="px-4 py-3 font-mono text-sm text-[#E4E4E7]">id</td>
                  <td className="px-4 py-3 text-sm text-[#FDE68A]">string</td>
                  <td className="px-4 py-3 text-sm text-[#86EFAC]">Yes</td>
                  <td className="px-4 py-3 text-sm text-[#A1A1AA]">The unique user identifier</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        {/* Request Example */}
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-white">Request</h2>
          <div className="mt-4 rounded-lg border border-[#1E1E1E] bg-[#111]">
            <div className="flex items-center justify-between border-b border-[#1E1E1E] px-4 py-2">
              <div className="flex gap-4">
                {['cURL', 'JavaScript', 'Python', 'Go'].map((lang, i) => (
                  <button key={lang} className={`text-xs font-medium ${i === 0 ? 'text-white' : 'text-[#52525B]'}`}>{lang}</button>
                ))}
              </div>
              <button className="text-xs text-[#52525B] hover:text-white">Copy</button>
            </div>
            <pre className="overflow-x-auto p-4 font-mono text-[13px] leading-[22px] text-[#E4E4E7]">
{`curl https://api.devtool.com/v1/users/usr_123 \\
  -H "Authorization: Bearer sk_live_..."
  -H "Content-Type: application/json"`}
            </pre>
          </div>
        </div>

        {/* Response Example */}
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-white">Response</h2>
          <div className="mt-4 flex items-center gap-2">
            <span className="rounded bg-[#15803D]/20 px-2 py-0.5 text-xs font-medium text-[#86EFAC]">200 OK</span>
          </div>
          <div className="mt-3 rounded-lg border border-[#1E1E1E] bg-[#111]">
            <div className="flex items-center justify-between border-b border-[#1E1E1E] px-4 py-2">
              <span className="text-xs text-[#52525B]">application/json</span>
              <button className="text-xs text-[#52525B] hover:text-white">Copy</button>
            </div>
            <pre className="overflow-x-auto p-4 font-mono text-[13px] leading-[22px]">
{`{
  "id": "usr_123",
  "email": "user@example.com",
  "name": "Alex Developer",
  "created_at": "2026-01-15T09:30:00Z",
  "plan": "pro",
  "usage": {
    "api_calls": 12400,
    "storage_mb": 4200
  }
}`}
            </pre>
          </div>
        </div>

        {/* Error Codes */}
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-white">Error Codes</h2>
          <div className="mt-4 rounded-lg border border-[#1E1E1E] overflow-hidden">
            <table className="w-full">
              <thead>
                <tr className="border-b border-[#1E1E1E] bg-[#111]">
                  <th className="px-4 py-3 text-left text-xs font-medium text-[#71717A]">Code</th>
                  <th className="px-4 py-3 text-left text-xs font-medium text-[#71717A]">Description</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#1E1E1E]">
                {[
                  { code: '401', desc: 'Invalid or missing authentication token' },
                  { code: '404', desc: 'User not found' },
                  { code: '429', desc: 'Rate limit exceeded. Retry after the Retry-After header value.' },
                  { code: '500', desc: 'Internal server error. Contact support if persistent.' },
                ].map((err) => (
                  <tr key={err.code}>
                    <td className="px-4 py-3 font-mono text-sm text-[#FCA5A5]">{err.code}</td>
                    <td className="px-4 py-3 text-sm text-[#A1A1AA]">{err.desc}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## 8. CLI Tool Landing Page

### Block Sequence
1. Hero (product name + tagline + install command + terminal demo)
2. Feature highlights (3-4 key features)
3. Usage examples (terminal screenshots or animated demos)
4. Comparison table (vs alternatives)
5. Installation section (multiple methods)
6. Community / GitHub link
7. Footer

```tsx
export function CLILanding() {
  return (
    <div className="min-h-screen bg-[#0A0A0A] text-[#E4E4E7]">
      <nav className="border-b border-[#1A1A1A]">
        <div className="mx-auto flex h-16 max-w-[1200px] items-center justify-between px-6">
          <span className="font-mono text-sm font-bold text-white">devtool</span>
          <div className="flex items-center gap-6">
            <a href="#" className="text-sm text-[#A1A1AA] hover:text-white">Docs</a>
            <a href="#" className="text-sm text-[#A1A1AA] hover:text-white">Blog</a>
            <a href="#" className="flex items-center gap-2 text-sm text-[#A1A1AA] hover:text-white">
              GitHub <span className="rounded bg-[#1A1A1A] px-1.5 py-0.5 text-xs">12.4k</span>
            </a>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="py-24">
        <div className="mx-auto max-w-[800px] px-6 text-center">
          <h1 className="text-5xl font-bold text-white">Ship faster from the terminal</h1>
          <p className="mt-6 text-xl text-[#A1A1AA]">
            A blazing-fast CLI for building, testing, and deploying your applications.
          </p>

          {/* Install command */}
          <div className="mx-auto mt-10 max-w-[400px] rounded-lg border border-[#1E1E1E] bg-[#111] p-4">
            <div className="flex items-center justify-between">
              <code className="font-mono text-sm text-[#86EFAC]">
                <span className="text-[#71717A]">$</span> npm install -g @devtool/cli
              </code>
              <button className="text-xs text-[#52525B] hover:text-white">Copy</button>
            </div>
          </div>

          <div className="mt-6 flex items-center justify-center gap-4">
            <a href="#" className="rounded-lg bg-white px-6 py-3 text-sm font-medium text-black hover:bg-gray-200">Get Started</a>
            <a href="#" className="rounded-lg border border-[#333] px-6 py-3 text-sm font-medium text-[#A1A1AA] hover:text-white">View on GitHub</a>
          </div>
        </div>
      </section>

      {/* Terminal Demo */}
      <section className="pb-24">
        <div className="mx-auto max-w-[700px] px-6">
          <div className="rounded-xl border border-[#1E1E1E] bg-[#111] overflow-hidden shadow-2xl">
            <div className="flex items-center gap-2 border-b border-[#1E1E1E] px-4 py-3">
              <div className="h-3 w-3 rounded-full bg-[#EF4444]" />
              <div className="h-3 w-3 rounded-full bg-[#F59E0B]" />
              <div className="h-3 w-3 rounded-full bg-[#22C55E]" />
              <span className="ml-2 text-xs text-[#52525B]">terminal</span>
            </div>
            <pre className="p-6 font-mono text-[13px] leading-[22px]">
{`$ devtool init my-project
Creating project structure...
Installing dependencies...
Configuring environment...

Done! Your project is ready.

$ cd my-project
$ devtool dev
Starting development server...
Ready at http://localhost:3000`}
            </pre>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="border-t border-[#1A1A1A] py-24">
        <div className="mx-auto max-w-[1000px] px-6">
          <h2 className="text-center text-3xl font-bold text-white">Why developers love it</h2>
          <div className="mt-16 grid gap-8 md:grid-cols-3">
            {[
              { title: 'Lightning fast', desc: 'Written in Rust. Builds complete in milliseconds, not minutes.' },
              { title: 'Zero config', desc: 'Sensible defaults out of the box. Override only what you need.' },
              { title: 'Plugin ecosystem', desc: '200+ community plugins. Extend to fit any workflow.' },
            ].map((f) => (
              <div key={f.title} className="rounded-xl border border-[#1E1E1E] bg-[#111] p-8">
                <h3 className="text-lg font-semibold text-white">{f.title}</h3>
                <p className="mt-3 text-sm leading-relaxed text-[#A1A1AA]">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
```

---

## 9. Changelog Page (Developer Tool)

### Block Sequence
1. Header (title + RSS + GitHub releases link)
2. Version entries (newest first): version tag, date, category badges, description, code examples
3. Breaking changes callout
4. Migration links

```tsx
export function DevChangelog() {
  const releases = [
    {
      version: 'v2.4.0', date: 'Mar 10, 2026', tags: ['Feature'],
      title: 'Parallel builds and watch mode',
      changes: [
        'Added --parallel flag for concurrent builds across workspaces',
        'New watch mode with incremental rebuilds (50ms average)',
        'Plugin API v2 with lifecycle hooks',
      ],
      code: 'devtool build --parallel --watch',
      breaking: false,
    },
    {
      version: 'v2.3.0', date: 'Feb 24, 2026', tags: ['Feature', 'Breaking'],
      title: 'Configuration file format change',
      changes: [
        'Migrated from JSON to TypeScript configuration',
        'New defineConfig helper with full type safety',
        'Deprecated devtool.json (will be removed in v3)',
      ],
      code: null,
      breaking: true,
    },
  ];

  const tagColor: Record<string, string> = {
    Feature: 'bg-[#0EA5E9]/10 text-[#0EA5E9]',
    Fix: 'bg-[#F59E0B]/10 text-[#F59E0B]',
    Breaking: 'bg-[#EF4444]/10 text-[#EF4444]',
    Performance: 'bg-[#22C55E]/10 text-[#22C55E]',
  };

  return (
    <div className="min-h-screen bg-[#0A0A0A] py-20">
      <div className="mx-auto max-w-[700px] px-6">
        <div className="flex items-center justify-between">
          <h1 className="text-2xl font-bold text-white">Changelog</h1>
          <div className="flex items-center gap-4">
            <a href="/rss" className="text-sm text-[#71717A] hover:text-white">RSS</a>
            <a href="#" className="text-sm text-[#71717A] hover:text-white">GitHub Releases</a>
          </div>
        </div>

        <div className="mt-12 space-y-16">
          {releases.map((r) => (
            <article key={r.version}>
              <div className="flex flex-wrap items-center gap-3">
                <span className="rounded-md bg-[#1A1A1A] px-2.5 py-1 font-mono text-sm font-medium text-white">{r.version}</span>
                <time className="text-sm text-[#71717A]">{r.date}</time>
                {r.tags.map((tag) => (
                  <span key={tag} className={`rounded-full px-2 py-0.5 text-xs font-medium ${tagColor[tag]}`}>{tag}</span>
                ))}
              </div>
              <h2 className="mt-4 text-xl font-semibold text-white">{r.title}</h2>

              {r.breaking && (
                <div className="mt-4 rounded-lg border-l-[3px] border-[#EF4444] bg-[#7F1D1D]/20 p-4">
                  <p className="text-xs font-semibold text-[#EF4444]">Breaking Change</p>
                  <p className="mt-1 text-sm text-[#A1A1AA]">
                    This version includes breaking changes. See the <a href="#" className="text-[#0EA5E9] underline">migration guide</a>.
                  </p>
                </div>
              )}

              <ul className="mt-4 space-y-2">
                {r.changes.map((change) => (
                  <li key={change} className="flex items-start gap-2 text-sm text-[#A1A1AA]">
                    <span className="mt-1.5 h-1.5 w-1.5 flex-shrink-0 rounded-full bg-[#52525B]" />
                    {change}
                  </li>
                ))}
              </ul>

              {r.code && (
                <div className="mt-4 rounded-lg border border-[#1E1E1E] bg-[#111] px-4 py-3">
                  <code className="font-mono text-sm text-[#86EFAC]">$ {r.code}</code>
                </div>
              )}
            </article>
          ))}
        </div>
      </div>
    </div>
  );
}
```

---

## 10. Status / Monitoring Page

### Block Sequence
1. Overall status banner (all systems operational / degraded / outage)
2. System component list (API, dashboard, webhooks, CDN — each with status)
3. Uptime chart (90-day bar chart)
4. Active incidents (if any)
5. Incident history (past 30 days)
6. Subscribe to updates

```tsx
export function StatusPage() {
  const systems = [
    { name: 'API', status: 'operational', uptime: '99.99%' },
    { name: 'Dashboard', status: 'operational', uptime: '99.97%' },
    { name: 'Webhooks', status: 'degraded', uptime: '99.85%' },
    { name: 'CDN', status: 'operational', uptime: '100%' },
    { name: 'Database', status: 'operational', uptime: '99.99%' },
  ];

  const statusColor: Record<string, string> = {
    operational: 'bg-[#22C55E]',
    degraded: 'bg-[#F59E0B]',
    outage: 'bg-[#EF4444]',
  };

  const statusText: Record<string, string> = {
    operational: 'text-[#22C55E]',
    degraded: 'text-[#F59E0B]',
    outage: 'text-[#EF4444]',
  };

  const allOperational = systems.every((s) => s.status === 'operational');

  return (
    <div className="min-h-screen bg-[#0A0A0A]">
      <nav className="border-b border-[#1A1A1A]">
        <div className="mx-auto flex h-14 max-w-[800px] items-center justify-between px-6">
          <span className="font-mono text-sm font-bold text-white">DevTool Status</span>
          <a href="#subscribe" className="text-sm text-[#0EA5E9] hover:underline">Subscribe to updates</a>
        </div>
      </nav>

      <div className="mx-auto max-w-[800px] px-6 py-10">
        {/* Overall Status */}
        <div className={`rounded-xl p-6 ${allOperational ? 'bg-[#22C55E]/10 border border-[#22C55E]/20' : 'bg-[#F59E0B]/10 border border-[#F59E0B]/20'}`}>
          <div className="flex items-center gap-3">
            <div className={`h-3 w-3 rounded-full ${allOperational ? 'bg-[#22C55E]' : 'bg-[#F59E0B]'}`} />
            <h1 className={`text-lg font-semibold ${allOperational ? 'text-[#22C55E]' : 'text-[#F59E0B]'}`}>
              {allOperational ? 'All Systems Operational' : 'Partial System Degradation'}
            </h1>
          </div>
          <p className="mt-2 text-sm text-[#A1A1AA]">
            Last checked: {new Date().toLocaleString()}
          </p>
        </div>

        {/* Systems */}
        <div className="mt-8 rounded-xl border border-[#1E1E1E] bg-[#111]">
          <div className="divide-y divide-[#1E1E1E]">
            {systems.map((sys) => (
              <div key={sys.name} className="flex items-center justify-between px-6 py-4">
                <div className="flex items-center gap-3">
                  <div className={`h-2.5 w-2.5 rounded-full ${statusColor[sys.status]}`} />
                  <span className="text-sm font-medium text-white">{sys.name}</span>
                </div>
                <div className="flex items-center gap-4">
                  <span className="text-xs text-[#71717A]">{sys.uptime} uptime</span>
                  <span className={`text-xs font-medium capitalize ${statusText[sys.status]}`}>{sys.status}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Uptime Chart */}
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-white">90-day uptime</h2>
          <div className="mt-4 flex gap-[2px]">
            {Array.from({ length: 90 }, (_, i) => (
              <div key={i} className={`h-8 flex-1 rounded-sm ${
                i === 67 ? 'bg-[#F59E0B]' : i === 45 ? 'bg-[#EF4444]' : 'bg-[#22C55E]'
              }`} title={`Day ${90 - i}`} />
            ))}
          </div>
          <div className="mt-2 flex items-center justify-between text-xs text-[#52525B]">
            <span>90 days ago</span>
            <span>Today</span>
          </div>
        </div>

        {/* Active Incidents */}
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-white">Active Incidents</h2>
          <div className="mt-4 rounded-xl border border-[#F59E0B]/30 bg-[#F59E0B]/5 p-5">
            <div className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-[#F59E0B]" />
              <h3 className="text-sm font-semibold text-[#F59E0B]">Webhook delivery delays</h3>
            </div>
            <p className="mt-2 text-sm text-[#A1A1AA]">
              We are investigating increased latency in webhook delivery. Events are being queued and will be delivered once the issue is resolved.
            </p>
            <p className="mt-2 text-xs text-[#71717A]">Started Mar 12, 2026 at 10:42 AM UTC</p>
            <div className="mt-3 space-y-2">
              <div className="flex items-start gap-2">
                <span className="text-xs text-[#71717A] w-14 flex-shrink-0">11:15</span>
                <p className="text-xs text-[#A1A1AA]">Root cause identified. Deploying fix.</p>
              </div>
              <div className="flex items-start gap-2">
                <span className="text-xs text-[#71717A] w-14 flex-shrink-0">10:42</span>
                <p className="text-xs text-[#A1A1AA]">Investigating reports of delayed webhook delivery.</p>
              </div>
            </div>
          </div>
        </div>

        {/* Past Incidents */}
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-white">Past Incidents</h2>
          <div className="mt-4 space-y-4">
            {[
              { date: 'Mar 5, 2026', title: 'API latency spike', duration: '23 minutes', resolved: true },
              { date: 'Feb 18, 2026', title: 'Dashboard downtime', duration: '12 minutes', resolved: true },
            ].map((inc) => (
              <div key={inc.date} className="rounded-lg border border-[#1E1E1E] p-4">
                <div className="flex items-center justify-between">
                  <div>
                    <h3 className="text-sm font-medium text-white">{inc.title}</h3>
                    <p className="mt-1 text-xs text-[#71717A]">{inc.date} - Duration: {inc.duration}</p>
                  </div>
                  <span className="rounded-full bg-[#22C55E]/10 px-2.5 py-0.5 text-xs font-medium text-[#22C55E]">Resolved</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Subscribe */}
        <div id="subscribe" className="mt-12 rounded-xl border border-[#1E1E1E] bg-[#111] p-6 text-center">
          <h2 className="text-base font-semibold text-white">Subscribe to updates</h2>
          <p className="mt-2 text-sm text-[#71717A]">Get notified when we have incidents or maintenance.</p>
          <div className="mx-auto mt-4 flex max-w-[400px] gap-2">
            <input type="email" placeholder="email@example.com" className="flex-1 rounded-md border border-[#1E1E1E] bg-[#0A0A0A] px-3 py-2 text-sm text-white placeholder:text-[#52525B] focus:border-[#0EA5E9] focus:outline-none" />
            <button className="rounded-md bg-white px-4 py-2 text-sm font-medium text-black hover:bg-gray-200">Subscribe</button>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## Cross-Template Summary

### Creative Pages
| Page | Typography | Layout | Key Pattern |
|---|---|---|---|
| Portfolio Landing | Serif headlines, generous spacing | Full-viewport hero, 2-col grid | Hover reveals, editorial feel |
| Case Study | Serif + sans, pull quotes | Narrow content + full-bleed images | Metrics section, next project link |
| About | Serif headlines, warm tone | Photo + text split | Experience timeline, personal warmth |
| Contact | Serif headline, form | Two-column: info + form | Availability badge, timezone |
| Blog | Serif titles, editorial | Featured + grid | Newsletter CTA, category filters |

### Developer Pages
| Page | Typography | Layout | Key Pattern |
|---|---|---|---|
| Documentation | Sans + monospace code | 3-column: nav + content + TOC | Code blocks, callouts, copy buttons |
| API Reference | Monospace-heavy | Single column, endpoint sections | Method badges, language tabs, error table |
| CLI Landing | Monospace hero | Centered, terminal demo | Install command, terminal animation |
| Changelog | Monospace versions | Single column timeline | Breaking change callouts, code examples |
| Status Page | Sans + monospace | Single column, system list | Uptime bars, incident timeline, subscribe |

---

## Implementation Notes

### Creative Portfolio Performance
```css
/* Lazy load portfolio images */
img[loading="lazy"] {
  opacity: 0;
  transition: opacity 0.3s ease;
}
img[loading="lazy"].loaded {
  opacity: 1;
}
```

### Developer Code Blocks
- Always include a "Copy" button on code blocks
- Support multiple language tabs (cURL, JS, Python, Go minimum)
- Use consistent syntax highlighting theme across all code
- Code blocks should be horizontally scrollable, never wrap

### Font Loading Strategy
```html
<!-- Creative: Preload serif display font -->
<link rel="preload" href="/fonts/editorial-new.woff2" as="font" type="font/woff2" crossorigin>

<!-- Developer: Preload monospace font -->
<link rel="preload" href="/fonts/jetbrains-mono.woff2" as="font" type="font/woff2" crossorigin>
```

### Design Token Integration
Replace hardcoded values with tokens from `creator-social-style.md` (creative) and `saas-productivity-style.md` (developer) for production use.
