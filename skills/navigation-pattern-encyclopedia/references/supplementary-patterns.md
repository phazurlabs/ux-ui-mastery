# Supplementary Patterns

Entries that had no home in the other reference files when this skill was
converted to a router. Kept here rather than dropped.

### Wayfinding Principles
Wayfinding in digital products mirrors physical navigation. Users build mental models of information spaces the same way they learn building layouts.

- **Landmarks** — persistent visual anchors (logo, primary nav bar, footer) that orient users
- **Paths** — clear routes between destinations (links, buttons, breadcrumbs)
- **Regions** — visually distinct zones that group related content (sidebar, main content, utility bar)
- **Edges** — boundaries between sections (dividers, background shifts, elevation changes)
- **Signs** — labels and icons that communicate destination or action

### Fitts's Law Applied to Navigation
- Larger targets = faster to reach. Minimum touch target: 44x44pt (iOS), 48x48dp (Android)
- Edge/corner targets are effectively infinite size (pin nav to screen edges)
- Distance matters: place frequent actions close to resting cursor/thumb position
- Bottom navigation on mobile exploits the thumb zone (easy reach)

### CTX-03: Popover

**When to Use:** Revealing additional options or information without leaving context (filter options, color picker, date picker).

**Specs:**
- Width: 200-400px
- Arrow/caret pointing to trigger element
- Border-radius: 12px
- Shadow: medium elevation
- Dismiss: click outside, Escape, or explicit close button
- Position: automatically flip if near viewport edge (top/bottom/left/right)

### ANTI-09: Non-Descriptive Labels
**Problem:** Labels like "Solutions", "Resources", "Platform" have weak information scent.
**Fix:** Use specific, action-oriented labels: "Pricing", "Documentation", "API Reference", "Templates". Test labels with users.
