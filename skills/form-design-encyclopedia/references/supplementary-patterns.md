# Supplementary Patterns

Entries that had no home in the other reference files when this skill was
converted to a router. Kept here rather than dropped.

### 3.33 Mention Input (@-mention)
- **When to use**: Referencing users, channels, or entities in text
- **Trigger**: `@` character opens suggestion popup
- **Anatomy**: Text input, popup with avatar + name + handle, highlighted mention chip in text
- **Behavior**: Continue typing to filter; arrow keys + Enter to select; Escape to dismiss

### 11.1 Autosave
- **When**: Long forms, multi-step flows, content creation
- **How**: Save to localStorage on field blur or debounced on change (2s)
- **UX**: Show "Draft saved" indicator (timestamp); auto-dismiss after 3s
- **Recovery**: On page load, check for saved draft; offer "Continue where you left off?"
```jsx
// Autosave hook
function useAutosave(formId, data, delay = 2000) {
  useEffect(() => {
    const timer = setTimeout(() => {
      localStorage.setItem(`draft-${formId}`, JSON.stringify({
        data,
        savedAt: Date.now()
      }));
    }, delay);
    return () => clearTimeout(timer);
  }, [formId, data, delay]);
}
```

### 12.2 Registration / Sign-Up Form
- **Minimum viable**: Email + password (name optional at signup)
- **Social login**: "Continue with Google/Apple/GitHub" above email form
- **Progressive profiling**: Collect additional info over time, not all at registration
- **Password**: Strength meter + requirements checklist (show which are met in real-time)
- **Username**: Real-time availability check with suggestions
- **Confirmation**: Email verification flow (link or code)
- **Never**: Require username + email + password + confirm password + name + phone at signup
