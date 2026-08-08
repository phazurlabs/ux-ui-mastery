# Input Field Catalog — 50+ Input Types with Full Specs, States, ARIA, and Code

## How to Use This Catalog

Every input field in this catalog includes: semantic HTML, ARIA attributes for accessibility, all visual states (default, hover, focus, filled, error, disabled, readonly), validation rules, the correct mobile keyboard type (`inputmode`), and production React + CSS code. When building any form, look up the specific input type here for the complete implementation spec.

---

## Field State Reference (Applies to All Fields)

Every input field must support these states:

| State | Border | Background | Text Color | Label Color | Ring |
|-------|--------|------------|------------|-------------|------|
| **Default** | 1px #D1D5DB | #FFFFFF | #111827 | #374151 | none |
| **Hover** | 1px #9CA3AF | #FFFFFF | #111827 | #374151 | none |
| **Focus** | 1px #2563EB | #FFFFFF | #111827 | #2563EB | 2px #2563EB/20% |
| **Filled** | 1px #D1D5DB | #FFFFFF | #111827 | #374151 | none |
| **Error** | 1px #DC2626 | #FEF2F2 | #111827 | #DC2626 | none |
| **Error + Focus** | 1px #DC2626 | #FFFFFF | #111827 | #DC2626 | 2px #DC2626/20% |
| **Disabled** | 1px #E5E7EB | #F9FAFB | #9CA3AF | #9CA3AF | none |
| **Readonly** | 1px #E5E7EB | #F9FAFB | #374151 | #374151 | none |
| **Success** | 1px #059669 | #FFFFFF | #111827 | #374151 | none |

---

## 1. Text Input — Standard

**HTML:** `<input type="text">`
**Use for:** Names, titles, generic short text (under 100 characters)
**inputmode:** `text` (default)
**autocomplete:** `name`, `given-name`, `family-name`, `organization`, `street-address`, etc.

```tsx
function TextInput({ label, name, required, error, ...props }: InputProps) {
  const id = `field-${name}`;
  const errorId = `error-${name}`;
  return (
    <div className="form-field">
      <label htmlFor={id} className="form-label">
        {label}
        {required && <span className="form-required" aria-hidden="true"> *</span>}
      </label>
      <input
        id={id}
        name={name}
        type="text"
        required={required}
        aria-required={required}
        aria-invalid={!!error}
        aria-errormessage={error ? errorId : undefined}
        className={`form-input ${error ? 'form-input--error' : ''}`}
        {...props}
      />
      {error && <p id={errorId} className="form-error" role="alert">{error}</p>}
    </div>
  );
}
```

---

## 2. Text Input — With Leading Icon

**Use for:** Search, URL, email, or any field where an icon provides context.
**Specifications:** Icon 20px, positioned absolutely at left: 14px, input padding-left: 44px.

```tsx
function IconInput({ label, name, icon, ...props }: InputProps & { icon: React.ReactNode }) {
  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <div className="input-icon-wrapper">
        <span className="input-icon-left" aria-hidden="true">{icon}</span>
        <input id={`field-${name}`} name={name} className="form-input input-with-icon-left" {...props} />
      </div>
    </div>
  );
}
```

```css
.input-icon-wrapper {
  position: relative;
}

.input-icon-left {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: #9CA3AF;
  display: flex;
  pointer-events: none;
}

.input-with-icon-left {
  padding-left: 44px;
}
```

---

## 3. Text Input — With Action Button

**Use for:** Copy-to-clipboard fields, URL fields with "Visit" button, coupon code with "Apply".
**Specifications:** Button inside input, right side, height matches input minus 8px (nested button), or flush right.

```css
.input-action-wrapper {
  position: relative;
}

.input-with-action {
  padding-right: 100px;
}

.input-action-button {
  position: absolute;
  right: 4px;
  top: 50%;
  transform: translateY(-50%);
  height: 36px;
  padding: 0 16px;
  font-size: 13px;
  font-weight: 500;
  color: #2563EB;
  background: #EFF6FF;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
```

---

## 4. Text Input — With Character Count

**Use for:** Bios, titles, descriptions, tweets — any field with a maximum length.
**Specifications:** Character count below input, right-aligned, font-size 12px, color #9CA3AF. Turns #DC2626 when approaching limit (90%+). Uses `aria-describedby` to announce count to screen readers.

```tsx
function CharCountInput({ label, name, maxLength = 280 }: { label: string; name: string; maxLength?: number }) {
  const [value, setValue] = useState('');
  const remaining = maxLength - value.length;
  const isNearLimit = remaining <= Math.ceil(maxLength * 0.1);
  const isOver = remaining < 0;

  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <input
        id={`field-${name}`}
        name={name}
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        maxLength={maxLength}
        aria-describedby={`charcount-${name}`}
        className="form-input"
      />
      <p id={`charcount-${name}`}
        className={`char-count ${isNearLimit ? 'char-count--warning' : ''} ${isOver ? 'char-count--over' : ''}`}
        aria-live="polite"
      >
        {remaining} characters remaining
      </p>
    </div>
  );
}
```

```css
.char-count {
  font-size: 12px;
  color: #9CA3AF;
  text-align: right;
  margin: 2px 0 0;
}

.char-count--warning {
  color: #D97706;
}

.char-count--over {
  color: #DC2626;
  font-weight: 500;
}
```

---

## 5. Email Input

**HTML:** `<input type="email">`
**inputmode:** `email`
**autocomplete:** `email`
**Validation:** Must contain `@` and a domain. Regex: `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`
**Enhancement:** Suggest common domain corrections — "Did you mean @gmail.com?" when user types @gmal.com.
**Mobile keyboard:** Shows `@` and `.` keys prominently.

```tsx
function EmailInput({ label, name, error, onBlur }: InputProps) {
  const commonDomains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com'];
  const [suggestion, setSuggestion] = useState('');

  const handleBlur = (e: React.FocusEvent<HTMLInputElement>) => {
    const value = e.target.value;
    const atIndex = value.indexOf('@');
    if (atIndex > 0) {
      const domain = value.slice(atIndex + 1).toLowerCase();
      const match = commonDomains.find(d =>
        d !== domain && levenshteinDistance(d, domain) <= 2
      );
      if (match) setSuggestion(`${value.slice(0, atIndex + 1)}${match}`);
      else setSuggestion('');
    }
    onBlur?.(e);
  };

  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <input
        id={`field-${name}`}
        name={name}
        type="email"
        inputMode="email"
        autoComplete="email"
        onBlur={handleBlur}
        aria-invalid={!!error}
        className={`form-input ${error ? 'form-input--error' : ''}`}
      />
      {suggestion && (
        <p className="form-suggestion">
          Did you mean <button type="button" onClick={() => { /* set value */ setSuggestion(''); }}
            className="form-suggestion-link">{suggestion}</button>?
        </p>
      )}
      {error && <p className="form-error" role="alert">{error}</p>}
    </div>
  );
}
```

---

## 6. Password Input — With Show/Hide Toggle

**HTML:** `<input type="password">`
**autocomplete:** `current-password` (login) or `new-password` (signup/change)
**Enhancement:** Show/hide toggle button, password strength meter for new passwords.
**Accessibility:** Toggle button uses `aria-label` that updates: "Show password" / "Hide password".

```tsx
function PasswordInput({ label, name, isNew = false, error }: InputProps & { isNew?: boolean }) {
  const [visible, setVisible] = useState(false);

  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <div className="input-action-wrapper">
        <input
          id={`field-${name}`}
          name={name}
          type={visible ? 'text' : 'password'}
          autoComplete={isNew ? 'new-password' : 'current-password'}
          aria-invalid={!!error}
          className={`form-input input-with-action-icon ${error ? 'form-input--error' : ''}`}
        />
        <button
          type="button"
          className="input-toggle-visibility"
          onClick={() => setVisible(!visible)}
          aria-label={visible ? 'Hide password' : 'Show password'}
        >
          {visible ? 'Hide' : 'Show'}
        </button>
      </div>
      {error && <p className="form-error" role="alert">{error}</p>}
    </div>
  );
}
```

```css
.input-with-action-icon {
  padding-right: 64px;
}

.input-toggle-visibility {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 13px;
  font-weight: 500;
  color: #6B7280;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}

.input-toggle-visibility:hover {
  color: #111827;
}
```

---

## 7. Password Strength Meter

**Use for:** Signup and password change forms only (not login).
**Specifications:** 4-segment bar below password field. Segments fill and change color as strength increases: Weak (#DC2626), Fair (#D97706), Good (#059669), Strong (#059669 all segments).
**Logic:** Check length (8+), uppercase, lowercase, number, special character.

```tsx
function PasswordStrengthMeter({ password }: { password: string }) {
  const checks = [
    password.length >= 8,
    /[A-Z]/.test(password),
    /[a-z]/.test(password),
    /[0-9]/.test(password),
    /[^A-Za-z0-9]/.test(password),
  ];
  const score = checks.filter(Boolean).length;
  const labels = ['', 'Weak', 'Fair', 'Good', 'Strong', 'Very strong'];
  const colors = ['', '#DC2626', '#D97706', '#D97706', '#059669', '#059669'];

  return (
    <div className="password-strength" aria-label={`Password strength: ${labels[score]}`}>
      <div className="password-strength-bars">
        {[1, 2, 3, 4].map((i) => (
          <div key={i} className="password-strength-segment"
            style={{ background: i <= score ? colors[score] : '#E5E7EB' }} />
        ))}
      </div>
      {password.length > 0 && (
        <span className="password-strength-label" style={{ color: colors[score] }}>
          {labels[score]}
        </span>
      )}
    </div>
  );
}
```

```css
.password-strength {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 6px;
}

.password-strength-bars {
  display: flex;
  gap: 4px;
  flex: 1;
}

.password-strength-segment {
  height: 4px;
  flex: 1;
  border-radius: 2px;
  transition: background-color 200ms ease;
}

.password-strength-label {
  font-size: 12px;
  font-weight: 500;
  white-space: nowrap;
}
```

---

## 8. Number Input — With Stepper

**HTML:** `<input type="text" inputmode="numeric">`
**Note:** Avoid `type="number"` — it has scroll-to-change behavior and inconsistent browser UX. Use `type="text"` with `inputmode="numeric"` and `pattern="[0-9]*"`.
**Specifications:** Stepper buttons on right side (+ and -), 32x32px, border-left separator.

```tsx
function NumberStepper({ label, name, min = 0, max = 99, value, onChange }: NumberStepperProps) {
  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <div className="number-stepper">
        <button type="button" className="stepper-button stepper-minus"
          onClick={() => onChange(Math.max(min, value - 1))}
          aria-label={`Decrease ${label}`}
          disabled={value <= min}>
          &minus;
        </button>
        <input id={`field-${name}`} name={name} type="text" inputMode="numeric"
          pattern="[0-9]*" value={value} readOnly
          className="form-input stepper-input" aria-live="polite" />
        <button type="button" className="stepper-button stepper-plus"
          onClick={() => onChange(Math.min(max, value + 1))}
          aria-label={`Increase ${label}`}
          disabled={value >= max}>
          +
        </button>
      </div>
    </div>
  );
}
```

```css
.number-stepper {
  display: flex;
  align-items: center;
  border: 1px solid #D1D5DB;
  border-radius: 8px;
  overflow: hidden;
  width: fit-content;
}

.stepper-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  color: #374151;
  background: #F9FAFB;
  border: none;
  cursor: pointer;
}

.stepper-button:hover:not(:disabled) {
  background: #F3F4F6;
}

.stepper-button:disabled {
  color: #D1D5DB;
  cursor: not-allowed;
}

.stepper-input {
  width: 64px;
  height: 44px;
  text-align: center;
  border: none;
  border-left: 1px solid #D1D5DB;
  border-right: 1px solid #D1D5DB;
  border-radius: 0;
  font-size: 16px;
  font-weight: 500;
}
```

---

## 9. Phone Input — With Country Code Selector

**HTML:** `<input type="tel">`
**inputmode:** `tel`
**autocomplete:** `tel`
**Specifications:** Country flag + dial code dropdown on left, phone number input on right. Auto-format based on selected country.

```tsx
function PhoneInput({ label, name, error }: InputProps) {
  const [country, setCountry] = useState({ code: 'US', dial: '+1', flag: 'US flag' });

  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <div className="phone-wrapper">
        <button type="button" className="phone-country-trigger"
          aria-label={`Country code: ${country.dial}`}>
          <span className="phone-flag">{country.flag}</span>
          <span className="phone-dial">{country.dial}</span>
          <svg width="12" height="12" viewBox="0 0 12 12" fill="currentColor" aria-hidden="true">
            <path d="M3 4.5l3 3 3-3" stroke="currentColor" strokeWidth="1.5" fill="none" />
          </svg>
        </button>
        <input id={`field-${name}`} name={name} type="tel" inputMode="tel"
          autoComplete="tel" placeholder="(555) 123-4567"
          aria-invalid={!!error}
          className={`form-input phone-input ${error ? 'form-input--error' : ''}`} />
      </div>
      {error && <p className="form-error" role="alert">{error}</p>}
    </div>
  );
}
```

```css
.phone-wrapper {
  display: flex;
  border: 1px solid #D1D5DB;
  border-radius: 8px;
  overflow: hidden;
}

.phone-country-trigger {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 0 12px;
  background: #F9FAFB;
  border: none;
  border-right: 1px solid #D1D5DB;
  cursor: pointer;
  flex-shrink: 0;
  font-size: 14px;
  color: #374151;
}

.phone-input {
  border: none;
  border-radius: 0;
  flex: 1;
}

.phone-input:focus {
  box-shadow: none;
}

.phone-wrapper:focus-within {
  border-color: #2563EB;
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
}
```

---

## 10. URL Input

**HTML:** `<input type="url">`
**inputmode:** `url`
**autocomplete:** `url`
**Enhancement:** Show "https://" prefix as a static element inside the input.

```css
.url-wrapper {
  display: flex;
  align-items: center;
  border: 1px solid #D1D5DB;
  border-radius: 8px;
  overflow: hidden;
}

.url-prefix {
  padding: 0 0 0 14px;
  font-size: 14px;
  color: #9CA3AF;
  white-space: nowrap;
  user-select: none;
}

.url-input {
  border: none;
  border-radius: 0;
  padding-left: 4px;
  flex: 1;
}
```

---

## 11. Search Input — With Suggestions

**HTML:** `<input type="search">`
**inputmode:** `search`
**ARIA:** Use `role="combobox"`, `aria-expanded`, `aria-controls` pointing to suggestion list, `aria-activedescendant` for keyboard navigation.

```tsx
function SearchWithSuggestions({ suggestions }: { suggestions: string[] }) {
  const [query, setQuery] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const [activeIndex, setActiveIndex] = useState(-1);
  const listId = 'search-suggestions';

  return (
    <div className="search-combobox" role="combobox" aria-expanded={isOpen} aria-haspopup="listbox" aria-owns={listId}>
      <input
        type="search"
        value={query}
        onChange={(e) => { setQuery(e.target.value); setIsOpen(true); }}
        onFocus={() => setIsOpen(true)}
        aria-autocomplete="list"
        aria-controls={listId}
        aria-activedescendant={activeIndex >= 0 ? `suggestion-${activeIndex}` : undefined}
        className="form-input search-input"
        placeholder="Search..."
        aria-label="Search"
      />
      {isOpen && suggestions.length > 0 && (
        <ul id={listId} role="listbox" className="search-suggestions-list">
          {suggestions.map((item, i) => (
            <li key={item} id={`suggestion-${i}`} role="option"
              aria-selected={i === activeIndex}
              className={`search-suggestion ${i === activeIndex ? 'search-suggestion--active' : ''}`}
              onClick={() => { setQuery(item); setIsOpen(false); }}>
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

```css
.search-combobox {
  position: relative;
  max-width: 600px;
}

.search-suggestions-list {
  position: absolute;
  top: calc(100% + 4px);
  left: 0;
  right: 0;
  background: #FFFFFF;
  border: 1px solid #E5E7EB;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  list-style: none;
  padding: 4px;
  margin: 0;
  max-height: 300px;
  overflow-y: auto;
  z-index: 10;
}

.search-suggestion {
  padding: 10px 12px;
  font-size: 14px;
  color: #374151;
  border-radius: 6px;
  cursor: pointer;
}

.search-suggestion:hover,
.search-suggestion--active {
  background: #F3F4F6;
}
```

---

## 12. Textarea — Auto-Resize

**HTML:** `<textarea>`
**Use for:** Messages, descriptions, comments, bios — any multi-line text.
**Enhancement:** Auto-resize to fit content as user types. Set min-height and max-height.
**Specifications:** min-height 80px, max-height 300px, resize vertical allowed, scrollbar after max-height.

```tsx
function AutoResizeTextarea({ label, name, maxLength, error }: InputProps & { maxLength?: number }) {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [value, setValue] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setValue(e.target.value);
    const el = e.target;
    el.style.height = 'auto';
    el.style.height = `${Math.min(el.scrollHeight, 300)}px`;
  };

  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <textarea
        ref={textareaRef}
        id={`field-${name}`}
        name={name}
        value={value}
        onChange={handleChange}
        maxLength={maxLength}
        aria-invalid={!!error}
        className={`form-input form-textarea ${error ? 'form-input--error' : ''}`}
        rows={3}
      />
      {maxLength && (
        <p className="char-count" aria-live="polite">
          {maxLength - value.length} characters remaining
        </p>
      )}
      {error && <p className="form-error" role="alert">{error}</p>}
    </div>
  );
}
```

```css
.form-textarea {
  height: auto;
  min-height: 80px;
  max-height: 300px;
  resize: vertical;
  padding: 12px 16px;
  line-height: 1.5;
  overflow-y: auto;
}
```

---

## 13. Select / Dropdown — Single

**HTML:** `<select>`
**Accessibility:** Requires a visible `<label>`. Use `<optgroup>` for grouped options. Native `<select>` is the most accessible option — only use custom dropdowns if you need features native select cannot provide.

```tsx
function SelectField({ label, name, options, placeholder, required, error }: SelectProps) {
  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <div className="select-wrapper">
        <select id={`field-${name}`} name={name} required={required}
          aria-required={required} aria-invalid={!!error}
          className={`form-input form-select ${error ? 'form-input--error' : ''}`}>
          {placeholder && <option value="">{placeholder}</option>}
          {options.map(opt => (
            <option key={opt.value} value={opt.value}>{opt.label}</option>
          ))}
        </select>
      </div>
      {error && <p className="form-error" role="alert">{error}</p>}
    </div>
  );
}
```

```css
.select-wrapper {
  position: relative;
}

.form-select {
  appearance: none;
  padding-right: 40px;
  background-image: url("data:image/svg+xml,%3Csvg width='12' height='8' viewBox='0 0 12 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1.5L6 6.5L11 1.5' stroke='%236B7280' stroke-width='1.5' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  cursor: pointer;
}
```

---

## 14. Select / Dropdown — Multi-Select

**Use for:** Selecting multiple options from a list (tags, categories, permissions).
**ARIA:** Use `role="listbox"` with `aria-multiselectable="true"`, or a custom multi-select with checkboxes.
**Pattern:** Selected items shown as removable chips/tags above or inside the input.

---

## 15. Select / Dropdown — Searchable (Combobox)

**ARIA:** `role="combobox"`, `aria-autocomplete="list"`, `aria-expanded`, `aria-controls`, `aria-activedescendant`.
**Use for:** Long option lists (countries, cities, products). Type-to-filter behavior.

---

## 16. Combobox — With Create New Option

**Use for:** Tag input where users can select existing options OR create new ones.
**Enhancement:** "Create [user input]" option appears at bottom of filtered list when no exact match.

---

## 17. Date Picker — Single Date

**HTML:** `<input type="date">` for native, or custom calendar component.
**autocomplete:** `bday` (birthday), or no autocomplete for arbitrary dates.
**Mobile:** Always prefer native `<input type="date">` on mobile — it triggers the OS date picker.
**Desktop:** Custom calendar with month/year navigation, keyboard support (arrow keys to navigate days).
**ARIA:** Calendar grid uses `role="grid"`, days use `role="gridcell"`, selected day uses `aria-selected="true"`.

```tsx
function DateInput({ label, name, error }: InputProps) {
  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <input
        id={`field-${name}`}
        name={name}
        type="date"
        className={`form-input form-date ${error ? 'form-input--error' : ''}`}
        aria-invalid={!!error}
      />
      {error && <p className="form-error" role="alert">{error}</p>}
    </div>
  );
}
```

```css
.form-date {
  appearance: none;
  -webkit-appearance: none;
  position: relative;
}

.form-date::-webkit-calendar-picker-indicator {
  cursor: pointer;
  opacity: 0.6;
}

.form-date::-webkit-calendar-picker-indicator:hover {
  opacity: 1;
}
```

---

## 18. Date Picker — Date Range

**Use for:** Booking dates (check-in/check-out), report date ranges, event start/end.
**Pattern:** Two calendar months side by side on desktop. Selected range highlighted between start and end dates. Hover preview of range as user selects second date.
**Mobile:** Stacked months in a scrollable view.

---

## 19. Time Picker

**HTML:** `<input type="time">`
**Use for:** Appointment times, event times, reminders.
**Mobile:** Native time picker is strongly preferred.
**Desktop:** Custom dropdown with time slots in 15-minute or 30-minute increments.

---

## 20. Color Picker

**HTML:** `<input type="color">`
**Use for:** Theme customization, branding settings.
**Enhancement:** Preset color swatches + custom hex input. Show color preview swatch.
**ARIA:** Each swatch is a radio button in a group. Hex input has `aria-label="Custom color hex code"`.

---

## 21. File Upload — Drag and Drop

**HTML:** `<input type="file">`
**Specifications:** Drop zone with dashed border (2px dashed #D1D5DB), 160px min-height, centered icon + text. Active drag state: border color change + background tint. File list below with filename, size, progress bar, remove button.
**Accessibility:** The drop zone should contain a visually styled label around the hidden file input. Keyboard users activate via Enter/Space on the label.

```tsx
function FileUpload({ label, name, accept, multiple }: FileUploadProps) {
  const [files, setFiles] = useState<File[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    const dropped = Array.from(e.dataTransfer.files);
    setFiles(prev => multiple ? [...prev, ...dropped] : dropped.slice(0, 1));
  };

  return (
    <div className="form-field">
      <span className="form-label">{label}</span>
      <div className="file-dropzone"
        onDragOver={(e) => e.preventDefault()}
        onDrop={handleDrop}
        onClick={() => inputRef.current?.click()}
        role="button"
        tabIndex={0}
        aria-label={`Upload ${label}`}
        onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') inputRef.current?.click(); }}
      >
        <svg width="40" height="40" viewBox="0 0 40 40" fill="none" aria-hidden="true">
          <path d="M20 6v20m-8-8l8 8 8-8" stroke="#9CA3AF" strokeWidth="2" strokeLinecap="round" />
        </svg>
        <p className="file-dropzone-text">
          <span className="file-dropzone-link">Click to upload</span> or drag and drop
        </p>
        <p className="file-dropzone-hint">PNG, JPG, PDF up to 10MB</p>
        <input ref={inputRef} type="file" name={name} accept={accept}
          multiple={multiple} hidden onChange={(e) => {
            setFiles(Array.from(e.target.files || []));
          }} />
      </div>
      {files.length > 0 && (
        <ul className="file-list">
          {files.map((file, i) => (
            <li key={i} className="file-item">
              <span className="file-name">{file.name}</span>
              <span className="file-size">{(file.size / 1024).toFixed(0)} KB</span>
              <button type="button" className="file-remove" aria-label={`Remove ${file.name}`}
                onClick={() => setFiles(files.filter((_, j) => j !== i))}>
                &times;
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

```css
.file-dropzone {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 160px;
  padding: 24px;
  border: 2px dashed #D1D5DB;
  border-radius: 12px;
  cursor: pointer;
  text-align: center;
  transition: border-color 150ms, background 150ms;
}

.file-dropzone:hover,
.file-dropzone:focus-visible {
  border-color: #93C5FD;
  background: #EFF6FF;
}

.file-dropzone-text {
  font-size: 14px;
  color: #6B7280;
  margin: 8px 0 4px;
}

.file-dropzone-link {
  color: #2563EB;
  font-weight: 500;
}

.file-dropzone-hint {
  font-size: 12px;
  color: #9CA3AF;
  margin: 0;
}

.file-list {
  list-style: none;
  padding: 0;
  margin: 12px 0 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.file-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 12px;
  background: #F9FAFB;
  border-radius: 6px;
  font-size: 14px;
}

.file-name {
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.file-size {
  color: #9CA3AF;
  font-size: 12px;
}

.file-remove {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  color: #9CA3AF;
  background: none;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.file-remove:hover {
  color: #DC2626;
  background: #FEF2F2;
}
```

---

## 22. Toggle Switch

**HTML:** `<button role="switch" aria-checked="true|false">`
**Use for:** Binary on/off settings. Not a replacement for checkboxes in forms.
**Specifications:** Track: 44x24px, border-radius 12px. Thumb: 20x20px circle. Off: track #D1D5DB, thumb left. On: track #2563EB, thumb right. Transition: 200ms ease.
**Accessibility:** Must use `role="switch"` with `aria-checked`. Label associated via `aria-labelledby`.

```tsx
function Toggle({ label, checked, onChange }: ToggleProps) {
  const id = `toggle-${label.toLowerCase().replace(/\s+/g, '-')}`;

  return (
    <div className="toggle-field">
      <span id={id} className="toggle-label">{label}</span>
      <button
        type="button"
        role="switch"
        aria-checked={checked}
        aria-labelledby={id}
        className={`toggle-track ${checked ? 'toggle-track--on' : ''}`}
        onClick={() => onChange(!checked)}
      >
        <span className="toggle-thumb" />
      </button>
    </div>
  );
}
```

```css
.toggle-field {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.toggle-label {
  font-size: 14px;
  color: #374151;
}

.toggle-track {
  position: relative;
  width: 44px;
  height: 24px;
  background: #D1D5DB;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: background-color 200ms ease;
  padding: 0;
  flex-shrink: 0;
}

.toggle-track--on {
  background: #2563EB;
}

.toggle-thumb {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 20px;
  height: 20px;
  background: #FFFFFF;
  border-radius: 50%;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.15);
  transition: transform 200ms ease;
}

.toggle-track--on .toggle-thumb {
  transform: translateX(20px);
}

.toggle-track:focus-visible {
  outline: 2px solid #2563EB;
  outline-offset: 2px;
}
```

---

## 23. Checkbox — Single

**HTML:** `<input type="checkbox">`
**Use for:** Terms acceptance, opt-in, binary choice within a form.
**Specifications:** 20x20px box, border-radius 4px, checkmark icon when checked.
**Accessibility:** Label must be associated via `for`/`id` or wrapping `<label>`.

---

## 24. Checkbox — Group

**HTML:** Multiple `<input type="checkbox">` inside a `<fieldset>` with `<legend>`.
**Use for:** Multi-select from a list (interests, permissions, features).
**Specifications:** Vertical stack with 12px gap between items.
**Accessibility:** `<fieldset>` groups the checkboxes; `<legend>` provides the group label.

---

## 25. Checkbox — Indeterminate

**Use for:** "Select all" checkbox in a table or list where some but not all items are selected.
**HTML:** Set via JavaScript: `checkbox.indeterminate = true`.
**Visual:** Dash/minus icon instead of checkmark.

---

## 26. Radio Button — Vertical List

**HTML:** `<input type="radio">` inside a `<fieldset>` with `<legend>`.
**Use for:** Single selection from 2-5 options.
**Specifications:** 20x20px circle, 12px gap between options.
**Accessibility:** `<fieldset>` + `<legend>` for the group. Arrow keys navigate between options.

---

## 27. Radio Button — Horizontal

**Same as vertical but with `flex-direction: row` and `gap: 24px`.
**Use for:** Small number of short options (2-3) where horizontal space is available.

---

## 28. Radio Button — Card Style

**Use for:** Significant choices where each option needs a title and description (plan selection, shipping method).
**Specifications:** Each option is a card (border, border-radius 10px, padding 16px). Selected card: border-color brand, background tint. Radio circle at top-right or left side.

```css
.radio-card {
  display: flex;
  gap: 12px;
  padding: 16px;
  border: 2px solid #E5E7EB;
  border-radius: 10px;
  cursor: pointer;
  transition: border-color 150ms, background 150ms;
}

.radio-card:hover {
  border-color: #93C5FD;
}

.radio-card--selected {
  border-color: #2563EB;
  background: #EFF6FF;
}

.radio-card-content {
  flex: 1;
}

.radio-card-title {
  font-size: 15px;
  font-weight: 500;
  color: #111827;
}

.radio-card-description {
  font-size: 13px;
  color: #6B7280;
  margin-top: 2px;
}
```

---

## 29. Slider — Single Value

**HTML:** `<input type="range">`
**Use for:** Volume, brightness, price range, continuous values.
**Specifications:** Track height 4-6px, thumb 20-24px circle. Current value displayed as tooltip or adjacent text.
**Accessibility:** Must have `aria-label` or associated label. `aria-valuemin`, `aria-valuemax`, `aria-valuenow`.

---

## 30. Slider — Range (Two Thumbs)

**Use for:** Price range, date range, any min-max selection.
**Implementation:** Two overlapping range inputs or custom component. Filled track between thumbs.
**Accessibility:** Each thumb needs its own `aria-label` ("Minimum price", "Maximum price").

---

## 31. Rating Input — Stars

**Use for:** Product reviews, feedback.
**Specifications:** 5 stars, 32px each, gap 4px. Unfilled: #D1D5DB outline. Filled: #F59E0B solid. Hover preview fills up to hovered star.
**ARIA:** `role="radiogroup"` with `aria-label="Rating"`. Each star is `role="radio"` with `aria-label="1 star"`, etc.

```tsx
function StarRating({ value, onChange }: { value: number; onChange: (v: number) => void }) {
  const [hover, setHover] = useState(0);

  return (
    <div className="star-rating" role="radiogroup" aria-label="Rating">
      {[1, 2, 3, 4, 5].map((star) => (
        <button
          key={star}
          type="button"
          role="radio"
          aria-checked={star === value}
          aria-label={`${star} star${star !== 1 ? 's' : ''}`}
          className={`star ${star <= (hover || value) ? 'star--filled' : ''}`}
          onMouseEnter={() => setHover(star)}
          onMouseLeave={() => setHover(0)}
          onClick={() => onChange(star)}
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
          </svg>
        </button>
      ))}
    </div>
  );
}
```

```css
.star-rating {
  display: flex;
  gap: 4px;
}

.star {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #D1D5DB;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  transition: color 100ms;
}

.star--filled {
  color: #F59E0B;
}

.star:focus-visible {
  outline: 2px solid #2563EB;
  outline-offset: 2px;
  border-radius: 4px;
}
```

---

## 32. Tag Input

**Use for:** Adding tags, labels, skills, categories. Autocomplete + create new.
**Specifications:** Tags displayed as chips inside the input area. Backspace removes last tag. Enter or comma adds a tag.
**ARIA:** Input has `aria-describedby` pointing to instructions. Tags have remove buttons with `aria-label="Remove [tag]"`.

```tsx
function TagInput({ label, name, suggestions }: { label: string; name: string; suggestions?: string[] }) {
  const [tags, setTags] = useState<string[]>([]);
  const [input, setInput] = useState('');

  const addTag = (tag: string) => {
    const trimmed = tag.trim();
    if (trimmed && !tags.includes(trimmed)) {
      setTags([...tags, trimmed]);
      setInput('');
    }
  };

  const removeTag = (index: number) => {
    setTags(tags.filter((_, i) => i !== index));
  };

  return (
    <div className="form-field">
      <label htmlFor={`field-${name}`} className="form-label">{label}</label>
      <div className="tag-input-wrapper">
        {tags.map((tag, i) => (
          <span key={tag} className="tag-chip">
            {tag}
            <button type="button" className="tag-remove" aria-label={`Remove ${tag}`}
              onClick={() => removeTag(i)}>&times;</button>
          </span>
        ))}
        <input
          id={`field-${name}`}
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' || e.key === ',') { e.preventDefault(); addTag(input); }
            if (e.key === 'Backspace' && !input && tags.length) removeTag(tags.length - 1);
          }}
          className="tag-input"
          placeholder={tags.length === 0 ? 'Add tags...' : ''}
          aria-describedby={`tag-hint-${name}`}
        />
      </div>
      <p id={`tag-hint-${name}`} className="form-hint">Press Enter or comma to add a tag</p>
    </div>
  );
}
```

```css
.tag-input-wrapper {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  padding: 8px 12px;
  border: 1px solid #D1D5DB;
  border-radius: 8px;
  min-height: 44px;
  align-items: center;
  cursor: text;
}

.tag-input-wrapper:focus-within {
  border-color: #2563EB;
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
}

.tag-chip {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px;
  background: #EFF6FF;
  color: #1E40AF;
  font-size: 13px;
  font-weight: 500;
  border-radius: 6px;
}

.tag-remove {
  width: 16px;
  height: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  color: #6B7280;
  background: none;
  border: none;
  cursor: pointer;
  border-radius: 50%;
  padding: 0;
}

.tag-remove:hover {
  color: #DC2626;
  background: #FEE2E2;
}

.tag-input {
  flex: 1;
  min-width: 80px;
  border: none;
  outline: none;
  font-size: 14px;
  padding: 4px 0;
}

.form-hint {
  font-size: 12px;
  color: #9CA3AF;
  margin: 4px 0 0;
}
```

---

## 33. OTP / Verification Code Input

**Use for:** Two-factor authentication, email verification, phone verification.
**Specifications:** 4-6 individual digit boxes, each 48-56px wide, centered. Auto-advance to next box on digit entry. Backspace moves to previous box.
**HTML:** Use `autocomplete="one-time-code"` on a hidden single input for SMS autofill, with visual separate boxes.

```tsx
function OTPInput({ length = 6, onComplete }: { length?: number; onComplete: (code: string) => void }) {
  const [values, setValues] = useState(Array(length).fill(''));
  const refs = useRef<(HTMLInputElement | null)[]>([]);

  const handleChange = (index: number, value: string) => {
    if (!/^\d*$/.test(value)) return;
    const newValues = [...values];
    newValues[index] = value.slice(-1);
    setValues(newValues);
    if (value && index < length - 1) refs.current[index + 1]?.focus();
    if (newValues.every(v => v)) onComplete(newValues.join(''));
  };

  const handleKeyDown = (index: number, e: React.KeyboardEvent) => {
    if (e.key === 'Backspace' && !values[index] && index > 0) {
      refs.current[index - 1]?.focus();
    }
  };

  return (
    <div className="otp-container" role="group" aria-label="Verification code">
      {values.map((val, i) => (
        <input
          key={i}
          ref={(el) => { refs.current[i] = el; }}
          type="text"
          inputMode="numeric"
          maxLength={1}
          value={val}
          onChange={(e) => handleChange(i, e.target.value)}
          onKeyDown={(e) => handleKeyDown(i, e)}
          className="otp-input"
          aria-label={`Digit ${i + 1}`}
        />
      ))}
    </div>
  );
}
```

```css
.otp-container {
  display: flex;
  gap: 8px;
  justify-content: center;
}

.otp-input {
  width: 48px;
  height: 56px;
  text-align: center;
  font-size: 24px;
  font-weight: 600;
  border: 2px solid #D1D5DB;
  border-radius: 10px;
  background: #FFFFFF;
  color: #111827;
  caret-color: #2563EB;
}

.otp-input:focus {
  outline: none;
  border-color: #2563EB;
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
}
```

---

## 34. Credit Card Input — With Card Type Detection

**See pattern 13 in form-layout-patterns.md for full payment form layout.**

**Card detection logic:**
- Visa: starts with 4
- Mastercard: starts with 51-55 or 2221-2720
- Amex: starts with 34 or 37 (15 digits, CVV is 4 digits)
- Discover: starts with 6011, 622126-622925, 644-649, 65

---

## 35-50: Quick Reference for Additional Input Types

### 35. Rich Text Editor
Toolbar with bold/italic/list/link/heading. WYSIWYG area is a `contenteditable` div with `role="textbox"` and `aria-multiline="true"`. Toolbar buttons have `aria-label` and `aria-pressed`.

### 36. Markdown Editor
Split pane: textarea on left, rendered preview on right. Toggle between edit/preview on mobile. Toolbar with formatting shortcuts.

### 37. Currency Input
Left-aligned dollar sign prefix (static), right-aligned value, inputmode="decimal", auto-format with commas.

### 38. Percentage Input
Input with "%" suffix, inputmode="decimal", constrain to 0-100.

### 39. Date Input — Manual Text (MM/DD/YYYY)
Three separate inputs or single input with auto-format slashes. Input masking as user types.

### 40. Time Zone Picker
Searchable dropdown with grouped time zones. Show UTC offset and city name.

### 41. Language Selector
Dropdown with flag icons and language names. Each option shows language in its native script.

### 42. Emoji Picker
Grid of emoji in a popover. Search by keyword. Recent/frequent emojis section. Skin tone selector.

### 43. Address Autocomplete Input
Text input that triggers Google Places or Mapbox autocomplete. Dropdown shows formatted address suggestions.

### 44. CAPTCHA / Bot Detection
reCAPTCHA v3 (invisible), hCaptcha, or Turnstile. Do not use image-based CAPTCHA that blocks accessibility.

### 45. Signature Pad
Canvas element for drawing a signature with mouse/touch. "Clear" button. Save as PNG/SVG.

### 46. Matrix / Grid Input
Table of radio buttons or checkboxes. Rows are questions, columns are scales (Strongly Disagree to Strongly Agree). Use `role="radiogroup"` per row.

### 47. Sortable List Input
Drag-and-drop reorderable list. Each item has a drag handle. Keyboard support: arrow keys to move items. `aria-label="Reorder items"`.

### 48. Location Picker (Map)
Map component (Google Maps, Mapbox) with a draggable pin. Coordinates displayed in text inputs below. Search bar for address lookup.

### 49. Quantity Selector (E-commerce)
Compact stepper for product quantity. "Add to cart" integration. Min/max constraints. Shows stock availability.

### 50. PIN Input
Similar to OTP but for 4-digit PINs. Dots/asterisks instead of visible digits. `type="password"` on each input. `autocomplete="off"`.

### 51. Masked Input (SSN, Tax ID)
Displays partial mask (***-**-1234). Uses `type="password"` with show/reveal toggle. Auto-formats dashes.

### 52. IP Address Input
Four numeric inputs separated by dots. Each constrained to 0-255. Auto-advance on dot or when 3 digits entered.

---

## Input Type Selection Decision Matrix

| Data Type | Input Type | inputmode | autocomplete | Mobile Keyboard |
|-----------|-----------|-----------|-------------|-----------------|
| Name | text | text | name | Standard |
| Email | email | email | email | Email (@, .com) |
| Password | password | — | current/new-password | Standard |
| Phone | tel | tel | tel | Phone pad |
| Number (integer) | text | numeric | — | Number pad |
| Number (decimal) | text | decimal | — | Number pad with . |
| Currency | text | decimal | — | Number pad with . |
| URL | url | url | url | URL (/, .com) |
| Search | search | search | — | Search (enter=search) |
| Credit card | text | numeric | cc-number | Number pad |
| ZIP/postal code | text | numeric | postal-code | Number pad |
| OTP code | text | numeric | one-time-code | Number pad |
| Date | date | — | bday | Native date picker |
| Time | time | — | — | Native time picker |
| Long text | textarea | text | — | Standard |
| Selection (few) | radio/select | — | — | — |
| Selection (many) | combobox | — | — | Standard |
| Boolean | checkbox/switch | — | — | — |
| File | file input | — | — | File picker |
