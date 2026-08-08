# Supplementary Patterns

Entries that had no home in the other reference files when this skill was
converted to a router. Kept here rather than dropped.

### 2.13 Full-Bleed / Edge-to-Edge

Image spanning the full viewport width, breaking out of content container.

```css
.full-bleed {
  width: 100vw;
  margin-left: calc(50% - 50vw);
}
```

### 8.2 Shapes

- **Circle**: Default for user avatars. `border-radius: 50%`. Requires 1:1 container.
- **Rounded square**: Used by Slack, Discord. `border-radius: 20-25%`. Good for workspace/team avatars.
- **Squircle**: iOS-style superellipse. Use SVG clip-path for true squircle (CSS border-radius is not a real squircle).
- **Square**: Rare. Used for app icons or organization logos only.

### 8.5 Avatar Groups / Stacks

Multiple avatars overlapping horizontally.

- Overlap: 25-33% of avatar width (e.g., 32px avatars with -8px margin-left).
- Stack order: first avatar on top (highest z-index) or last on top (both conventions exist).
- Overflow indicator: "+5" circle at the end when more than shown limit.
- Max visible: 3-5 avatars before overflow.
- Ring: 2px white border on each avatar for visual separation.

```css
.avatar-group {
  display: flex;
  flex-direction: row-reverse; /* last item on top */
}
.avatar-group > * {
  margin-left: -8px;
  border: 2px solid white;
  border-radius: 50%;
}
.avatar-group > *:last-child { margin-left: 0; }
```

---

## 9. Video Patterns

### 9.2 Click-to-Play

Video with visible thumbnail and play button overlay. User initiates playback.

- Large centered play button: 64-80px circle, semi-transparent background.
- Duration badge: bottom-right corner of thumbnail.
- On click: hide overlay, start video, show controls.
- Preferred for: content videos, tutorials, product demos.

### 12.2 Rotate

- Free rotation: drag to rotate with degree readout.
- Quick rotate: 90-degree CW/CCW buttons.
- Straighten slider: -45 to +45 degrees with grid overlay.
- Auto-straighten: detect horizon line.

### 12.3 Filters / Presets

- Thumbnail previews of each filter applied to current image.
- Horizontal scrollable strip of filter options.
- Filter intensity slider (0-100%) after selecting.
- Common filters: Original, B&W, Sepia, Vivid, Warm, Cool, Fade, Dramatic.

### 12.4 Adjustments

Individual parameter sliders:

| Adjustment | Range | Default |
|-----------|-------|---------|
| Brightness | -100 to +100 | 0 |
| Contrast | -100 to +100 | 0 |
| Saturation | -100 to +100 | 0 |
| Temperature | -100 (cool) to +100 (warm) | 0 |
| Highlights | -100 to +100 | 0 |
| Shadows | -100 to +100 | 0 |
| Sharpness | 0 to +100 | 0 |
| Vignette | 0 to +100 | 0 |

### 12.5 Zoom / Pan

- Pinch-to-zoom on touch devices.
- Scroll wheel zoom on desktop.
- Zoom slider or +/- buttons.
- Fit-to-screen / 100% / fill toggle.
- Pan by drag when zoomed in. Change cursor to grab/grabbing.
- Mini-map overview showing current viewport position on the full image.

---

## 13. Upload Patterns

### 16.4 Mask-Image

```css
/* Gradient fade */
.fade-bottom {
  mask-image: linear-gradient(to bottom, black 60%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 60%, transparent 100%);
}

/* SVG shape mask */
.custom-shape {
  mask-image: url('mask.svg');
  mask-size: cover;
}
```

### 16.6 Mix-Blend-Mode

```css
/* Duotone effect */
.duotone {
  position: relative;
  background-color: #0066ff; /* brand color */
}
.duotone img {
  mix-blend-mode: luminosity;
  filter: grayscale(100%) contrast(1.2);
}
```

---

## 17. Dark Mode for Media

### 17.1 Image Brightness/Contrast Adjustments

Reduce eye strain by dimming images in dark mode.

```css
@media (prefers-color-scheme: dark) {
  img:not([src$=".svg"]) {
    filter: brightness(0.85) contrast(1.05);
  }
  /* Exception: avatars keep full brightness */
  .avatar img { filter: none; }
}
```
