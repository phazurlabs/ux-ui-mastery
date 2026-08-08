# Depth Cues and Surface Materials

Everything that communicates elevation without a shadow, and the material
treatments a surface can carry.


Shadows are one of many depth cues. A rich spatial UI combines several:

### Overlapping (Occlusion)
Elements partially covering others instantly convey layering order.
```css
.stacked-cards {
  display: grid;
  grid-template-columns: 1fr;
}
.stacked-cards > * {
  grid-area: 1 / 1;
}
.stacked-cards > :nth-child(1) { transform: rotate(-3deg); z-index: 1; }
.stacked-cards > :nth-child(2) { transform: rotate(0deg); z-index: 2; }
.stacked-cards > :nth-child(3) { transform: rotate(3deg); z-index: 3; }
```

### Scale (Size)
Larger elements feel closer. Useful for focus/zoom effects.
```css
.card-focused { transform: scale(1.05); z-index: 2; }
.card-background { transform: scale(0.95); opacity: 0.7; }
```

### Blur (Depth of Field)
Background blur simulates camera depth of field.
```css
.background-layer { filter: blur(4px); }
.foreground-layer { filter: none; }
```

### Opacity / Fog
Distant elements fade toward the background color.
```css
.depth-layer-far { opacity: 0.5; }
.depth-layer-mid { opacity: 0.8; }
.depth-layer-near { opacity: 1; }
```

### Parallax
Layers move at different speeds during scroll, creating depth.
```css
.parallax-container {
  perspective: 1000px;
  overflow-y: auto;
}
.parallax-far {
  transform: translateZ(-200px) scale(1.2);
}
.parallax-near {
  transform: translateZ(0);
}
```

### Atmospheric Perspective
Combine blur + desaturation + lightening for distant elements.
```css
.distant-element {
  filter: blur(2px) saturate(0.6) brightness(1.1);
}
```

---

## Surface Materials

### Glass

```css
.surface-glass {
  background: oklch(1 0 0 / 0.5);
  backdrop-filter: blur(16px) saturate(1.8);
  -webkit-backdrop-filter: blur(16px) saturate(1.8);
  border: 1px solid oklch(1 0 0 / 0.25);
  box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.3);
}
```

### Paper

```css
.surface-paper {
  background: oklch(0.97 0.005 80);  /* Warm off-white */
  box-shadow:
    0 1px 3px oklch(0 0 0 / 0.08),
    0 0 0 1px oklch(0 0 0 / 0.04);
  /* Optional: noise texture for paper grain */
  background-image: url("data:image/svg+xml,..."); /* inline noise SVG */
}
```

### Metal (Brushed)

```css
.surface-metal {
  background: linear-gradient(
    135deg,
    oklch(0.85 0.005 250),
    oklch(0.78 0.005 250) 30%,
    oklch(0.88 0.005 250) 50%,
    oklch(0.76 0.005 250) 70%,
    oklch(0.82 0.005 250)
  );
  border: 1px solid oklch(0.70 0.005 250);
  box-shadow:
    inset 0 1px 0 oklch(1 0 0 / 0.25),
    inset 0 -1px 0 oklch(0 0 0 / 0.1),
    0 2px 8px oklch(0 0 0 / 0.15);
}
```

### Fabric / Soft

```css
.surface-fabric {
  background: oklch(0.95 0.01 80);
  /* Subtle woven texture via repeating gradients */
  background-image:
    repeating-linear-gradient(
      0deg,
      oklch(0 0 0 / 0.02) 0px,
      oklch(0 0 0 / 0.02) 1px,
      transparent 1px,
      transparent 3px
    ),
    repeating-linear-gradient(
      90deg,
      oklch(0 0 0 / 0.02) 0px,
      oklch(0 0 0 / 0.02) 1px,
      transparent 1px,
      transparent 3px
    );
  border-radius: var(--radius-3);
  box-shadow: 0 1px 4px oklch(0 0 0 / 0.05);
}
```

---

