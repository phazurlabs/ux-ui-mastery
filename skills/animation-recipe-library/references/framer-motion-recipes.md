# Framer Motion Recipes — 40+ React Component Patterns

Production-ready Framer Motion animation patterns for React. Each recipe is a self-contained component or pattern you can drop into any project.

Requires: `framer-motion` v11+

---

## Spring Presets

```tsx
export const springs = {
  gentle:  { type: "spring", stiffness: 120, damping: 14, mass: 1 },
  bouncy:  { type: "spring", stiffness: 180, damping: 12, mass: 1 },
  snappy:  { type: "spring", stiffness: 300, damping: 20, mass: 0.8 },
  wobbly:  { type: "spring", stiffness: 150, damping: 8, mass: 1 },
  stiff:   { type: "spring", stiffness: 400, damping: 30, mass: 1 },
  slow:    { type: "spring", stiffness: 80, damping: 20, mass: 1.2 },
  ios:     { type: "spring", stiffness: 200, damping: 22, mass: 1 },
} as const;
```

---

## Entrance Animations

### 1. FadeIn
```tsx
export const FadeIn = ({ children, delay = 0 }: { children: React.ReactNode; delay?: number }) => (
  <motion.div
    initial={{ opacity: 0 }}
    animate={{ opacity: 1 }}
    transition={{ duration: 0.2, delay }}
  >
    {children}
  </motion.div>
);
```

### 2. SlideUp
```tsx
export const SlideUp = ({ children, delay = 0 }: { children: React.ReactNode; delay?: number }) => (
  <motion.div
    initial={{ opacity: 0, y: 16 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1], delay }}
  >
    {children}
  </motion.div>
);
```

### 3. SlideDown
```tsx
export const SlideDown = ({ children }: { children: React.ReactNode }) => (
  <motion.div
    initial={{ opacity: 0, y: -16 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
  >
    {children}
  </motion.div>
);
```

### 4. ScaleIn (Spring)
```tsx
export const ScaleIn = ({ children }: { children: React.ReactNode }) => (
  <motion.div
    initial={{ opacity: 0, scale: 0.9 }}
    animate={{ opacity: 1, scale: 1 }}
    transition={{ type: "spring", stiffness: 300, damping: 20 }}
  >
    {children}
  </motion.div>
);
```

### 5. BounceIn
```tsx
export const BounceIn = ({ children }: { children: React.ReactNode }) => (
  <motion.div
    initial={{ opacity: 0, scale: 0.3 }}
    animate={{ opacity: 1, scale: 1 }}
    transition={{ type: "spring", stiffness: 180, damping: 12 }}
  >
    {children}
  </motion.div>
);
```

### 6. BlurIn
```tsx
export const BlurIn = ({ children }: { children: React.ReactNode }) => (
  <motion.div
    initial={{ opacity: 0, filter: "blur(12px)" }}
    animate={{ opacity: 1, filter: "blur(0px)" }}
    transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
  >
    {children}
  </motion.div>
);
```

### 7. ClipReveal
```tsx
export const ClipReveal = ({ children }: { children: React.ReactNode }) => (
  <motion.div
    initial={{ clipPath: "inset(0 100% 0 0)" }}
    animate={{ clipPath: "inset(0 0% 0 0)" }}
    transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
  >
    {children}
  </motion.div>
);
```

### 8. RotateIn
```tsx
export const RotateIn = ({ children }: { children: React.ReactNode }) => (
  <motion.div
    initial={{ opacity: 0, rotate: -180, scale: 0.5 }}
    animate={{ opacity: 1, rotate: 0, scale: 1 }}
    transition={{ type: "spring", stiffness: 200, damping: 15 }}
  >
    {children}
  </motion.div>
);
```

---

## Stagger Patterns

### 9. StaggerChildren
```tsx
const containerVariants = {
  hidden: {},
  visible: { transition: { staggerChildren: 0.05 } },
};

const itemVariants = {
  hidden: { opacity: 0, y: 16 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.25, ease: [0.16, 1, 0.3, 1] } },
};

export const StaggerList = ({ items }: { items: { id: string; label: string }[] }) => (
  <motion.ul initial="hidden" animate="visible" variants={containerVariants}>
    {items.map(item => (
      <motion.li key={item.id} variants={itemVariants}>
        {item.label}
      </motion.li>
    ))}
  </motion.ul>
);
```

### 10. StaggerGrid
```tsx
export const StaggerGrid = ({ items }: { items: React.ReactNode[] }) => (
  <motion.div
    initial="hidden"
    animate="visible"
    variants={{ visible: { transition: { staggerChildren: 0.06 } } }}
    style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 16 }}
  >
    {items.map((item, i) => (
      <motion.div
        key={i}
        variants={{
          hidden: { opacity: 0, y: 24, scale: 0.95 },
          visible: { opacity: 1, y: 0, scale: 1 },
        }}
        transition={{ type: "spring", stiffness: 200, damping: 20 }}
      >
        {item}
      </motion.div>
    ))}
  </motion.div>
);
```

### 11. StaggerOnScroll
```tsx
export const StaggerOnScroll = ({ children }: { children: React.ReactNode }) => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: "-10%" });
  return (
    <motion.div
      ref={ref}
      initial="hidden"
      animate={isInView ? "visible" : "hidden"}
      variants={{ visible: { transition: { staggerChildren: 0.08 } } }}
    >
      {React.Children.map(children, child => (
        <motion.div
          variants={{
            hidden: { opacity: 0, y: 24 },
            visible: { opacity: 1, y: 0 },
          }}
          transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
        >
          {child}
        </motion.div>
      ))}
    </motion.div>
  );
};
```

---

## Page Transitions

### 12. CrossFade Page
```tsx
export const PageTransition = ({ children }: { children: React.ReactNode }) => (
  <AnimatePresence mode="wait">
    <motion.div
      key={useLocation().pathname}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.3 }}
    >
      {children}
    </motion.div>
  </AnimatePresence>
);
```

### 13. Slide Page
```tsx
export const SlidePageTransition = ({ children, direction = 1 }: { children: React.ReactNode; direction?: number }) => (
  <AnimatePresence mode="wait">
    <motion.div
      key={useLocation().pathname}
      initial={{ x: `${100 * direction}%`, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      exit={{ x: `${-30 * direction}%`, opacity: 0 }}
      transition={{ duration: 0.4, ease: [0.87, 0, 0.13, 1] }}
    >
      {children}
    </motion.div>
  </AnimatePresence>
);
```

### 14. Fade Through (Material 3)
```tsx
export const FadeThrough = ({ children }: { children: React.ReactNode }) => (
  <AnimatePresence mode="wait">
    <motion.div
      key={useLocation().pathname}
      initial={{ opacity: 0, scale: 0.92 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.35, ease: [0.2, 0, 0, 1] }}
    >
      {children}
    </motion.div>
  </AnimatePresence>
);
```

### 15. Shared Element / Layout Animation
```tsx
export const SharedElementCard = ({ id, isExpanded, children, onClick }: {
  id: string; isExpanded: boolean; children: React.ReactNode; onClick: () => void;
}) => (
  <motion.div
    layoutId={`card-${id}`}
    onClick={onClick}
    transition={{ type: "spring", stiffness: 200, damping: 25 }}
    style={{ cursor: "pointer" }}
  >
    {children}
  </motion.div>
);
```

### 16. Container Transform
```tsx
export const ContainerTransform = ({ id, isOpen, compact, detail }: {
  id: string; isOpen: boolean; compact: React.ReactNode; detail: React.ReactNode;
}) => (
  <motion.div layoutId={`container-${id}`} transition={{ duration: 0.5, ease: [0.2, 0, 0, 1] }}>
    <AnimatePresence mode="wait">
      {isOpen ? (
        <motion.div key="detail" initial={{ opacity: 0 }} animate={{ opacity: 1 }}
          exit={{ opacity: 0 }} transition={{ duration: 0.15 }}>
          {detail}
        </motion.div>
      ) : (
        <motion.div key="compact" initial={{ opacity: 0 }} animate={{ opacity: 1 }}
          exit={{ opacity: 0 }} transition={{ duration: 0.15 }}>
          {compact}
        </motion.div>
      )}
    </AnimatePresence>
  </motion.div>
);
```

---

## Micro-Interactions

### 17. Button Press
```tsx
export const Button = ({ children, onClick }: { children: React.ReactNode; onClick?: () => void }) => (
  <motion.button
    whileHover={{ y: -1, boxShadow: "0 4px 12px rgba(0,0,0,0.1)" }}
    whileTap={{ scale: 0.96 }}
    transition={{ type: "spring", stiffness: 400, damping: 25 }}
    onClick={onClick}
  >
    {children}
  </motion.button>
);
```

### 18. Toggle Switch
```tsx
export const Toggle = ({ isOn, onToggle }: { isOn: boolean; onToggle: () => void }) => (
  <button onClick={onToggle} style={{ width: 48, height: 28, borderRadius: 14, padding: 2,
    background: isOn ? "#3b82f6" : "#e2e8f0", border: "none", cursor: "pointer" }}>
    <motion.div
      animate={{ x: isOn ? 20 : 0 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
      style={{ width: 24, height: 24, borderRadius: 12, background: "white" }}
    />
  </button>
);
```

### 19. Shake on Error
```tsx
export const ShakeOnError = ({ hasError, children }: { hasError: boolean; children: React.ReactNode }) => (
  <motion.div
    animate={hasError ? { x: [0, -6, 6, -4, 4, 0] } : { x: 0 }}
    transition={{ duration: 0.4 }}
  >
    {children}
  </motion.div>
);
```

### 20. Card Hover Lift
```tsx
export const HoverCard = ({ children }: { children: React.ReactNode }) => (
  <motion.div
    whileHover={{ y: -4, boxShadow: "0 12px 32px rgba(0,0,0,0.1)" }}
    transition={{ duration: 0.2, ease: [0.16, 1, 0.3, 1] }}
  >
    {children}
  </motion.div>
);
```

### 21. Badge Notification
```tsx
export const NotificationBadge = ({ count }: { count: number }) => (
  <AnimatePresence>
    {count > 0 && (
      <motion.span
        key={count}
        initial={{ scale: 0 }}
        animate={{ scale: 1 }}
        exit={{ scale: 0 }}
        transition={{ type: "spring", stiffness: 300, damping: 15 }}
        style={{ background: "#ef4444", color: "white", borderRadius: "50%",
          width: 20, height: 20, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 12 }}
      >
        {count}
      </motion.span>
    )}
  </AnimatePresence>
);
```

### 22. Checkbox with Checkmark Draw
```tsx
export const Checkbox = ({ checked, onChange }: { checked: boolean; onChange: () => void }) => (
  <motion.button onClick={onChange} style={{ width: 24, height: 24, borderRadius: 6, border: "2px solid #d1d5db" }}
    animate={{ borderColor: checked ? "#3b82f6" : "#d1d5db", backgroundColor: checked ? "#3b82f6" : "transparent" }}
    transition={{ duration: 0.15 }}>
    <svg viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth={3}>
      <motion.path d="M5 12l5 5L19 7" initial={{ pathLength: 0 }}
        animate={{ pathLength: checked ? 1 : 0 }}
        transition={{ duration: 0.2, ease: [0.16, 1, 0.3, 1] }} />
    </svg>
  </motion.button>
);
```

### 23. Tooltip
```tsx
export const Tooltip = ({ text, children }: { text: string; children: React.ReactNode }) => {
  const [isVisible, setIsVisible] = useState(false);
  return (
    <div onMouseEnter={() => setIsVisible(true)} onMouseLeave={() => setIsVisible(false)}
      style={{ position: "relative", display: "inline-block" }}>
      {children}
      <AnimatePresence>
        {isVisible && (
          <motion.div
            initial={{ opacity: 0, y: 4, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 2 }}
            transition={{ duration: 0.1 }}
            style={{ position: "absolute", bottom: "100%", left: "50%", transform: "translateX(-50%)",
              padding: "6px 10px", background: "#1e293b", color: "white", borderRadius: 6, fontSize: 13,
              whiteSpace: "nowrap", marginBottom: 6 }}
          >
            {text}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};
```

### 24. Ripple Effect
```tsx
export const RippleButton = ({ children, onClick }: { children: React.ReactNode; onClick?: () => void }) => {
  const [ripples, setRipples] = useState<{ id: number; x: number; y: number }[]>([]);
  const handleClick = (e: React.MouseEvent) => {
    const rect = e.currentTarget.getBoundingClientRect();
    setRipples(prev => [...prev, { id: Date.now(), x: e.clientX - rect.left, y: e.clientY - rect.top }]);
    onClick?.();
  };
  return (
    <button onClick={handleClick} style={{ position: "relative", overflow: "hidden" }}>
      {children}
      <AnimatePresence>
        {ripples.map(r => (
          <motion.span key={r.id} initial={{ scale: 0, opacity: 0.4 }}
            animate={{ scale: 4, opacity: 0 }} exit={{ opacity: 0 }}
            transition={{ duration: 0.4 }}
            onAnimationComplete={() => setRipples(prev => prev.filter(p => p.id !== r.id))}
            style={{ position: "absolute", left: r.x, top: r.y, width: 40, height: 40,
              borderRadius: "50%", background: "rgba(255,255,255,0.3)", transform: "translate(-50%,-50%)" }} />
        ))}
      </AnimatePresence>
    </button>
  );
};
```

---

## Layout Animations

### 25. Accordion
```tsx
export const Accordion = ({ isOpen, children }: { isOpen: boolean; children: React.ReactNode }) => (
  <motion.div
    initial={false}
    animate={{ height: isOpen ? "auto" : 0 }}
    transition={{ duration: 0.25, ease: [0.16, 1, 0.3, 1] }}
    style={{ overflow: "hidden" }}
  >
    <div style={{ padding: "16px 0" }}>{children}</div>
  </motion.div>
);
```

### 26. Tab Content Switch
```tsx
export const TabContent = ({ activeTab, children }: { activeTab: string; children: React.ReactNode }) => (
  <AnimatePresence mode="wait">
    <motion.div
      key={activeTab}
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -8 }}
      transition={{ duration: 0.2 }}
    >
      {children}
    </motion.div>
  </AnimatePresence>
);
```

### 27. List Item Add/Remove
```tsx
export const AnimatedList = ({ items }: { items: { id: string; label: string }[] }) => (
  <AnimatePresence>
    {items.map(item => (
      <motion.div
        key={item.id}
        initial={{ opacity: 0, height: 0 }}
        animate={{ opacity: 1, height: "auto" }}
        exit={{ opacity: 0, height: 0, marginBottom: 0 }}
        transition={{ duration: 0.25 }}
      >
        {item.label}
      </motion.div>
    ))}
  </AnimatePresence>
);
```

### 28. Reorder List
```tsx
export const ReorderList = ({ items, setItems }: {
  items: { id: string; label: string }[];
  setItems: (items: { id: string; label: string }[]) => void;
}) => (
  <Reorder.Group values={items} onReorder={setItems} axis="y">
    {items.map(item => (
      <Reorder.Item
        key={item.id}
        value={item}
        whileDrag={{ scale: 1.03, boxShadow: "0 8px 24px rgba(0,0,0,0.15)" }}
        transition={{ type: "spring", stiffness: 300, damping: 25 }}
      >
        {item.label}
      </Reorder.Item>
    ))}
  </Reorder.Group>
);
```

### 29. Card Expand Detail
```tsx
export const ExpandableCard = ({ id, title, body, isSelected, onClick }: {
  id: string; title: string; body: string; isSelected: boolean; onClick: () => void;
}) => (
  <motion.div
    layoutId={`card-${id}`}
    onClick={onClick}
    transition={{ type: "spring", stiffness: 200, damping: 25 }}
    style={{ cursor: "pointer", padding: 16, borderRadius: 12, background: "white" }}
  >
    <motion.h3 layoutId={`title-${id}`}>{title}</motion.h3>
    <AnimatePresence>
      {isSelected && (
        <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
          {body}
        </motion.p>
      )}
    </AnimatePresence>
  </motion.div>
);
```

### 30. Masonry Layout
```tsx
export const MasonryLayout = ({ items }: { items: { id: string; content: React.ReactNode }[] }) => (
  <motion.div layout style={{ columns: 3, gap: 16 }}>
    {items.map(item => (
      <motion.div
        key={item.id}
        layout
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        exit={{ opacity: 0, scale: 0.9 }}
        transition={{ type: "spring", stiffness: 200, damping: 25 }}
        style={{ breakInside: "avoid", marginBottom: 16 }}
      >
        {item.content}
      </motion.div>
    ))}
  </motion.div>
);
```

---

## Modal and Overlay

### 31. Modal with Backdrop
```tsx
export const Modal = ({ isOpen, onClose, children }: {
  isOpen: boolean; onClose: () => void; children: React.ReactNode;
}) => (
  <AnimatePresence>
    {isOpen && (
      <>
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          onClick={onClose}
          style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", backdropFilter: "blur(4px)" }}
        />
        <motion.div
          initial={{ opacity: 0, scale: 0.95, y: 8 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.95, y: 8 }}
          transition={{ type: "spring", stiffness: 300, damping: 25 }}
          style={{ position: "fixed", top: "50%", left: "50%", transform: "translate(-50%,-50%)",
            background: "white", borderRadius: 16, padding: 24, maxWidth: 480, width: "90%" }}
        >
          {children}
        </motion.div>
      </>
    )}
  </AnimatePresence>
);
```

### 32. Bottom Sheet
```tsx
export const BottomSheet = ({ isOpen, onClose, children }: {
  isOpen: boolean; onClose: () => void; children: React.ReactNode;
}) => (
  <AnimatePresence>
    {isOpen && (
      <>
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
          onClick={onClose} style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.3)" }} />
        <motion.div
          initial={{ y: "100%" }}
          animate={{ y: 0 }}
          exit={{ y: "100%" }}
          transition={{ type: "spring", stiffness: 300, damping: 30 }}
          drag="y" dragConstraints={{ top: 0 }} dragElastic={0.2}
          onDragEnd={(_, info) => { if (info.offset.y > 100) onClose(); }}
          style={{ position: "fixed", bottom: 0, left: 0, right: 0,
            background: "white", borderRadius: "16px 16px 0 0", padding: 24, maxHeight: "80vh" }}
        >
          <div style={{ width: 32, height: 4, background: "#d1d5db", borderRadius: 2,
            margin: "0 auto 16px" }} />
          {children}
        </motion.div>
      </>
    )}
  </AnimatePresence>
);
```

### 33. Drawer
```tsx
export const Drawer = ({ isOpen, onClose, children, side = "left" }: {
  isOpen: boolean; onClose: () => void; children: React.ReactNode; side?: "left" | "right";
}) => (
  <AnimatePresence>
    {isOpen && (
      <>
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
          onClick={onClose} style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.3)" }} />
        <motion.div
          initial={{ x: side === "left" ? "-100%" : "100%" }}
          animate={{ x: 0 }}
          exit={{ x: side === "left" ? "-100%" : "100%" }}
          transition={{ type: "spring", stiffness: 300, damping: 30 }}
          style={{ position: "fixed", top: 0, bottom: 0, [side]: 0, width: 320,
            background: "white", padding: 24 }}
        >
          {children}
        </motion.div>
      </>
    )}
  </AnimatePresence>
);
```

---

## Loading States

### 34. Skeleton Loader
```tsx
export const Skeleton = ({ width = "100%", height = 20, borderRadius = 4 }: {
  width?: string | number; height?: number; borderRadius?: number;
}) => (
  <motion.div
    animate={{ backgroundPosition: ["200% 0", "-200% 0"] }}
    transition={{ duration: 1.5, repeat: Infinity, ease: "linear" }}
    style={{
      width, height, borderRadius,
      background: "linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%)",
      backgroundSize: "200% 100%",
    }}
  />
);
```

### 35. Bouncing Dots
```tsx
export const BouncingDots = () => (
  <div style={{ display: "flex", gap: 4 }}>
    {[0, 1, 2].map(i => (
      <motion.div
        key={i}
        animate={{ scale: [0.6, 1, 0.6], opacity: [0.4, 1, 0.4] }}
        transition={{ duration: 1.2, repeat: Infinity, delay: i * 0.16 }}
        style={{ width: 8, height: 8, borderRadius: "50%", background: "#3b82f6" }}
      />
    ))}
  </div>
);
```

### 36. Progress Bar
```tsx
export const ProgressBar = ({ value }: { value: number }) => (
  <div style={{ height: 4, background: "#e2e8f0", borderRadius: 2, overflow: "hidden" }}>
    <motion.div
      animate={{ width: `${value}%` }}
      transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
      style={{ height: "100%", background: "#3b82f6", borderRadius: 2 }}
    />
  </div>
);
```

### 37. Count Up
```tsx
export const CountUp = ({ end, duration = 2 }: { end: number; duration?: number }) => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true });
  const count = useMotionValue(0);
  const rounded = useTransform(count, Math.round);

  useEffect(() => {
    if (isInView) {
      animate(count, end, { duration });
    }
  }, [isInView, end, duration, count]);

  return <motion.span ref={ref}>{rounded}</motion.span>;
};
```

---

## Gesture Interactions

### 38. Drag to Dismiss
```tsx
export const SwipeToDismiss = ({ onDismiss, children }: {
  onDismiss: () => void; children: React.ReactNode;
}) => (
  <motion.div
    drag="x"
    dragConstraints={{ left: 0, right: 0 }}
    onDragEnd={(_, info) => {
      if (Math.abs(info.offset.x) > 100) onDismiss();
    }}
    transition={{ type: "spring", stiffness: 300, damping: 25 }}
  >
    {children}
  </motion.div>
);
```

### 39. Pull to Refresh
```tsx
export const PullToRefresh = ({ onRefresh, children }: {
  onRefresh: () => void; children: React.ReactNode;
}) => {
  const y = useMotionValue(0);
  const opacity = useTransform(y, [0, 80], [0, 1]);
  const rotate = useTransform(y, [0, 80], [0, 360]);

  return (
    <motion.div
      drag="y"
      dragConstraints={{ top: 0, bottom: 0 }}
      dragElastic={0.4}
      style={{ y }}
      onDragEnd={(_, info) => { if (info.offset.y > 80) onRefresh(); }}
    >
      <motion.div style={{ opacity, rotate, textAlign: "center", padding: 16 }}>
        Refreshing...
      </motion.div>
      {children}
    </motion.div>
  );
};
```

### 40. Long Press
```tsx
export const LongPressButton = ({ onLongPress, duration = 1, children }: {
  onLongPress: () => void; duration?: number; children: React.ReactNode;
}) => {
  const [isHolding, setIsHolding] = useState(false);
  const timerRef = useRef<NodeJS.Timeout>();

  return (
    <motion.button
      onTapStart={() => {
        setIsHolding(true);
        timerRef.current = setTimeout(() => { onLongPress(); setIsHolding(false); }, duration * 1000);
      }}
      onTap={() => { clearTimeout(timerRef.current); setIsHolding(false); }}
      onTapCancel={() => { clearTimeout(timerRef.current); setIsHolding(false); }}
      whileTap={{ scale: 0.98 }}
    >
      {children}
      <motion.div
        style={{ height: 3, background: "#3b82f6", borderRadius: 2, transformOrigin: "left" }}
        animate={{ scaleX: isHolding ? 1 : 0 }}
        transition={{ duration: isHolding ? duration : 0.15 }}
      />
    </motion.button>
  );
};
```

---

## Notification / Toast

### 41. Toast Notification
```tsx
export const Toast = ({ message, isVisible, onClose }: {
  message: string; isVisible: boolean; onClose: () => void;
}) => (
  <AnimatePresence>
    {isVisible && (
      <motion.div
        initial={{ opacity: 0, y: 50, scale: 0.95 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        exit={{ opacity: 0, y: 20, scale: 0.95 }}
        transition={{ type: "spring", stiffness: 300, damping: 25 }}
        drag="x"
        dragConstraints={{ left: 0, right: 0 }}
        onDragEnd={(_, info) => { if (Math.abs(info.offset.x) > 80) onClose(); }}
        style={{ position: "fixed", bottom: 24, left: "50%", x: "-50%",
          padding: "12px 20px", background: "#1e293b", color: "white", borderRadius: 12 }}
      >
        {message}
      </motion.div>
    )}
  </AnimatePresence>
);
```

### 42. Notification Stack
```tsx
export const NotificationStack = ({ notifications, onDismiss }: {
  notifications: { id: string; message: string }[];
  onDismiss: (id: string) => void;
}) => (
  <div style={{ position: "fixed", top: 16, right: 16, display: "flex", flexDirection: "column", gap: 8 }}>
    <AnimatePresence>
      {notifications.map((notif, i) => (
        <motion.div
          key={notif.id}
          layout
          initial={{ opacity: 0, x: 100, scale: 0.95 }}
          animate={{ opacity: 1, x: 0, scale: 1 }}
          exit={{ opacity: 0, x: 100, scale: 0.95 }}
          transition={{ type: "spring", stiffness: 300, damping: 25 }}
          onClick={() => onDismiss(notif.id)}
          style={{ padding: "12px 16px", background: "white", borderRadius: 8,
            boxShadow: "0 4px 12px rgba(0,0,0,0.1)", cursor: "pointer" }}
        >
          {notif.message}
        </motion.div>
      ))}
    </AnimatePresence>
  </div>
);
```

---

## Reduced Motion

### 43. useReducedMotion Wrapper
```tsx
import { useReducedMotion } from "framer-motion";

export const MotionSafe = ({ children, animation, reducedAnimation }: {
  children: React.ReactNode;
  animation: Record<string, any>;
  reducedAnimation?: Record<string, any>;
}) => {
  const shouldReduce = useReducedMotion();
  const safeAnimation = shouldReduce ? (reducedAnimation ?? { opacity: 1 }) : animation;

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={safeAnimation}
      transition={{ duration: shouldReduce ? 0 : 0.3 }}
    >
      {children}
    </motion.div>
  );
};
```
