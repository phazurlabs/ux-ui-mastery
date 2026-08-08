# Page and Layout Transition Recipes

18 page transitions and 12 layout animations — route changes, shared-element
morphs, list reordering, and container transforms.


#### D1. crossFade
**Duration**: 300ms | **Easing**: ease-in-out
```css
.page-enter { animation: fadeIn 300ms var(--ease-out) forwards; }
.page-exit { animation: fadeOut 200ms var(--ease-in) forwards; }
```
```tsx
<AnimatePresence mode="wait">
  <motion.div key={route} initial={{ opacity: 0 }} animate={{ opacity: 1 }}
    exit={{ opacity: 0 }} transition={{ duration: 0.3 }} />
</AnimatePresence>
```

#### D2. slideTransition
**Duration**: 400ms | **Easing**: ease-in-out
```css
.page-enter { animation: slideRight 400ms var(--ease-in-out) forwards; }
.page-exit { animation: slideOutLeft 300ms var(--ease-in) forwards; }
```
```tsx
<AnimatePresence mode="wait">
  <motion.div key={route} initial={{ x: "100%" }} animate={{ x: 0 }}
    exit={{ x: "-100%" }} transition={{ duration: 0.4, ease: [0.87, 0, 0.13, 1] }} />
</AnimatePresence>
```

#### D3. sharedElement (View Transitions API)
**Duration**: 350ms | **Easing**: ease-in-out
```css
::view-transition-old(card-hero) {
  animation: fadeOut 200ms var(--ease-in) forwards;
}
::view-transition-new(card-hero) {
  animation: fadeIn 350ms var(--ease-out) forwards;
}
.card-hero { view-transition-name: card-hero; }
```
```tsx
// With Framer Motion layoutId
<motion.div layoutId="card-hero" transition={{ duration: 0.35, ease: [0.87, 0, 0.13, 1] }} />
```

#### D4. morphTransition
**Duration**: 500ms | **Easing**: ease-in-out
```tsx
<motion.div layoutId={`card-${id}`} transition={{ type: "spring", stiffness: 200, damping: 25 }}>
  {isExpanded ? <FullView /> : <CardView />}
</motion.div>
```

#### D5. scaleTransition
**Duration**: 350ms | **Easing**: ease-out
```css
.page-enter {
  animation: scaleIn 350ms var(--ease-out) forwards;
}
.page-exit {
  animation: scaleOut 250ms var(--ease-in) forwards;
}
```

#### D6. modalOverlay
**Duration**: 250ms overlay, 300ms modal | **Easing**: ease-out
```css
.overlay {
  opacity: 0; transition: opacity 250ms var(--ease-out);
  background: rgba(0,0,0,0.5); backdrop-filter: blur(4px);
}
.overlay.is-open { opacity: 1; }
.modal {
  opacity: 0; transform: scale(0.95) translateY(8px);
  transition: all 300ms var(--spring-gentle);
}
.modal.is-open { opacity: 1; transform: scale(1) translateY(0); }
```

#### D7. drawerSlide
**Duration**: 300ms | **Easing**: ease-out
```css
.drawer {
  transform: translateX(-100%);
  transition: transform 300ms var(--ease-out);
}
.drawer.is-open { transform: translateX(0); }
```

#### D8. bottomSheet
**Duration**: 350ms | **Easing**: spring-gentle
```css
.bottom-sheet {
  transform: translateY(100%);
  transition: transform 350ms var(--spring-gentle);
}
.bottom-sheet.is-open { transform: translateY(0); }
```

#### D9. stackNavigation
**Duration**: 350ms | **Easing**: ios-spring | **Use**: iOS-style push/pop
```css
.stack-enter { animation: slideLeft 350ms var(--ios-spring) forwards; }
.stack-exit { animation: fadeOut 200ms var(--ease-in) forwards; transform: scale(0.95); }
```

#### D10. tabSwitch
**Duration**: 200ms | **Easing**: ease-out
```css
.tab-panel {
  opacity: 0; transition: opacity 200ms var(--ease-out);
}
.tab-panel.is-active { opacity: 1; }
```

#### D11. zoomDrillDown
**Duration**: 400ms | **Easing**: ease-out
```css
.drill-enter { animation: zoomIn 400ms var(--ease-out) forwards; }
.drill-exit { animation: zoomOut 300ms var(--ease-in) forwards; }
```

#### D12. verticalSlide
**Duration**: 350ms | **Easing**: ease-in-out
```tsx
<AnimatePresence mode="wait">
  <motion.div key={route} initial={{ y: "100%", opacity: 0 }}
    animate={{ y: 0, opacity: 1 }} exit={{ y: "-50%", opacity: 0 }}
    transition={{ duration: 0.35 }} />
</AnimatePresence>
```

#### D13. revealFromEdge
**Duration**: 400ms | **Easing**: ease-out
```css
@keyframes revealFromLeft {
  from { clip-path: inset(0 100% 0 0); }
  to { clip-path: inset(0 0 0 0); }
}
.reveal-left { animation: revealFromLeft 400ms var(--ease-out) forwards; }
```

#### D14. flipPage
**Duration**: 500ms | **Easing**: ease-in-out
```css
@keyframes flipPage {
  from { transform: perspective(1200px) rotateY(0); }
  to { transform: perspective(1200px) rotateY(-180deg); }
}
.flip-page { animation: flipPage 500ms var(--ease-in-out) forwards; }
```

#### D15. fadeThrough
**Duration**: 350ms total | **Easing**: ease-in-out (M3 pattern)
```tsx
<AnimatePresence mode="wait">
  <motion.div key={route} initial={{ opacity: 0, scale: 0.92 }}
    animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0 }}
    transition={{ duration: 0.35 }} />
</AnimatePresence>
```

#### D16. containerTransform
**Duration**: 500ms | **Easing**: material-emphasized | **Use**: M3 container transform
```tsx
<motion.div layoutId={`container-${id}`}
  transition={{ duration: 0.5, ease: [0.2, 0, 0, 1] }}>
  {isExpanded ? <DetailView /> : <CompactView />}
</motion.div>
```

#### D17. viewTransitionAPI
**Duration**: browser-managed | **Use**: Native cross-document transitions
```js
// Same-document transition
document.startViewTransition(() => {
  updateDOM();
});

// Cross-document (Chrome 126+)
// Set in CSS:
@view-transition { navigation: auto; }
::view-transition-old(root) { animation: fadeOut 200ms ease-in; }
::view-transition-new(root) { animation: fadeIn 300ms ease-out; }
```

#### D18. parallaxTransition
**Duration**: 500ms | **Easing**: ease-out
```tsx
<AnimatePresence mode="popLayout">
  <motion.div key={route}
    initial={{ x: "100%", zIndex: 1 }}
    animate={{ x: 0, zIndex: 1 }}
    exit={{ x: "-30%", zIndex: 0 }}
    transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }} />
</AnimatePresence>
```

---


#### G1. listReorder
```tsx
<Reorder.Group values={items} onReorder={setItems}>
  {items.map(item => (
    <Reorder.Item key={item.id} value={item}
      transition={{ type: "spring", stiffness: 300, damping: 25 }}>
      {item.label}
    </Reorder.Item>
  ))}
</Reorder.Group>
```

#### G2. gridMorph (grid to list and back)
```css
.grid-container {
  display: grid;
  transition: grid-template-columns 400ms var(--ease-in-out);
}
.grid-container.is-list { grid-template-columns: 1fr; }
.grid-container.is-grid { grid-template-columns: repeat(3, 1fr); }
.grid-container > * { transition: all 400ms var(--ease-in-out); }
```

#### G3. accordionExpand
```tsx
<motion.div initial={false} animate={{ height: isOpen ? "auto" : 0 }}
  transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
  style={{ overflow: "hidden" }}>
  <div style={{ padding: "16px" }}>{content}</div>
</motion.div>
```

#### G4. tabSwitch
```tsx
<AnimatePresence mode="wait">
  <motion.div key={activeTab}
    initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -8 }}
    transition={{ duration: 0.2 }} />
</AnimatePresence>
```

#### G5. carouselSlide
```css
.carousel-track {
  display: flex; transition: transform 400ms var(--ease-out);
}
.carousel-track[data-slide="0"] { transform: translateX(0); }
.carousel-track[data-slide="1"] { transform: translateX(-100%); }
.carousel-track[data-slide="2"] { transform: translateX(-200%); }
```

#### G6. masonry
```tsx
<motion.div layout transition={{ type: "spring", stiffness: 200, damping: 25 }}>
  {items.map(item => (
    <motion.div key={item.id} layout
      initial={{ opacity: 0 }} animate={{ opacity: 1 }}
      exit={{ opacity: 0 }} transition={{ duration: 0.3 }} />
  ))}
</motion.div>
```

#### G7. listItemAdd
```tsx
<AnimatePresence>
  {items.map(item => (
    <motion.div key={item.id}
      initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: "auto" }}
      exit={{ opacity: 0, height: 0 }} transition={{ duration: 0.25 }} />
  ))}
</AnimatePresence>
```

#### G8. listItemRemove
```tsx
<motion.div exit={{ opacity: 0, x: -100, height: 0, marginBottom: 0 }}
  transition={{ duration: 0.25, ease: [0.55, 0.055, 0.675, 0.19] }} />
```

#### G9. columnResize
```css
.resizable-panel {
  transition: flex-basis 300ms var(--ease-in-out);
}
```

#### G10. cardExpandDetail
```tsx
<motion.div layoutId={`card-${id}`} onClick={() => setSelected(id)}
  transition={{ type: "spring", stiffness: 200, damping: 25 }}>
  <motion.h2 layoutId={`title-${id}`}>{title}</motion.h2>
  <AnimatePresence>
    {isSelected && <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }}>{body}</motion.p>}
  </AnimatePresence>
</motion.div>
```

#### G11. sidebarCollapse
```css
.sidebar {
  width: 240px; transition: width 250ms var(--ease-in-out);
  overflow: hidden;
}
.sidebar.is-collapsed { width: 64px; }
.sidebar-label { transition: opacity 150ms var(--ease-in); }
.sidebar.is-collapsed .sidebar-label { opacity: 0; }
```

#### G12. splitView
```css
.split-container { display: flex; }
.split-left, .split-right {
  transition: flex 300ms var(--ease-in-out);
}
.split-container.focus-left .split-left { flex: 2; }
.split-container.focus-left .split-right { flex: 1; }
```

---
