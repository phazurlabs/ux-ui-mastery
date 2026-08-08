# Icon Geometry and Color

The grid an icon is drawn on, and how it takes colour across themes.

## 2. Icon Grid Systems

### The 24x24 Base Grid
The industry standard base grid is 24x24 pixels. All icon design begins here. The grid provides:
- **Live area**: 20x20px centered within the 24x24 frame (2px padding on each side)
- **Trim area**: The full 24x24 frame, ensuring consistent bounding boxes across the set
- **Pixel grid**: Every anchor point, stroke endpoint, and corner snaps to full or half pixels to prevent anti-aliasing blur at 1x resolution

### Pixel Grid Alignment
Icons rendered at small sizes (16-24px) must align to the pixel grid:
- Horizontal and vertical strokes land on full pixel boundaries
- 2px strokes span from pixel N to pixel N+2 (not N+0.5 to N+2.5)
- Diagonal lines and curves are exempt but should use even-number stroke widths
- At 1x resolution, a misaligned stroke renders as two blurry 1px lines instead of one crisp 2px line

### Keyline Shapes
Every icon fits within one of four keyline templates to ensure optical consistency:

| Keyline Shape | Dimensions (in 24px grid) | Use Cases |
|---------------|---------------------------|-----------|
| Circle | 20px diameter | People, globes, record, radio buttons |
| Square | 18x18px | Stops, settings, generic containers |
| Portrait rectangle | 16x20px (tall) | Documents, phones, bottles, person |
| Landscape rectangle | 20x16px (wide) | Laptops, landscapes, cards, video |
| Diagonal | 20x20px rotated 45deg | Warning, diamond, rotate |

### Safe Zones and Optical Sizing
- **2px safe zone** on all sides of the 24px frame — no visual content should enter this zone
- **Optical sizing**: A circle must be slightly larger than a square to appear the same size. A 20px circle appears smaller than an 18px square to the human eye. Compensate by allowing circular icons to extend 1px beyond the keyline
- **Vertical elements** (arrows pointing up) appear shorter than horizontal elements of the same pixel height — extend by 1-2px

---

## 14. Icon Color

### currentColor for Theming
The single most important technique for themeable icons: use `currentColor` as the stroke or fill value.

```css
/* The icon inherits color from its parent */
.nav-link { color: var(--text-secondary); }
.nav-link:hover { color: var(--text-primary); }
.nav-link svg { stroke: currentColor; } /* Automatically updates on hover */
```

### Multi-Color Icons
Some icons require two or more colors (e.g., a warning triangle with yellow fill and dark exclamation):
- Use CSS custom properties for each color channel
- Phosphor's Duotone weight uses `opacity: 0.2` on secondary elements
- For themed multi-color: `--icon-primary: currentColor; --icon-secondary: currentColor / 0.3;`

```css
.icon-duotone .primary { fill: var(--icon-primary, currentColor); }
.icon-duotone .secondary { fill: var(--icon-secondary, currentColor); opacity: 0.2; }
```

### Dark Mode Adaptation
| Element | Light Mode | Dark Mode | Rule |
|---------|------------|-----------|------|
| UI icons (stroke) | gray-600 (#525252) | gray-400 (#a3a3a3) | Reduce contrast slightly |
| Filled icons | gray-700 (#404040) | gray-300 (#d4d4d4) | Ensure 3:1 contrast ratio vs background |
| Accent icons | primary-600 | primary-400 | Shift to lighter shade |
| Disabled icons | gray-400 @ 38% | gray-500 @ 38% | Same opacity, shifted base |
| Illustration fills | Full saturation | 80% saturation | Reduce saturation to prevent glowing |
| Illustration strokes | gray-900 | gray-100 | Invert stroke color |

---
