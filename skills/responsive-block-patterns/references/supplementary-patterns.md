# Supplementary Patterns

Entries that had no home in the other reference files when this skill was
converted to a router. Kept here rather than dropped.

### Pattern 8: Dense Auto-Placement

```css
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-flow: dense;
  gap: 0.5rem;
}
.gallery-grid .featured {
  grid-column: span 2;
  grid-row: span 2;
}
```

### has() for Responsive-Aware Styling

```css
/* Adjust grid when sidebar is present */
.layout:has(.sidebar) {
  grid-template-columns: 280px 1fr;
}
.layout:not(:has(.sidebar)) {
  grid-template-columns: 1fr;
}

/* Form row that adjusts based on content */
.form-row:has(> :nth-child(2)) {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}
```

---

## 12. Responsive Testing
