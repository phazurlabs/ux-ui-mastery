# Form Layout Patterns — 30+ Patterns with Specs, Responsive Behavior, and Code

## How to Use This Catalog

Each pattern includes: when to use it, exact specifications (spacing, widths, label placement), responsive behavior at mobile/tablet/desktop breakpoints, and production React + CSS code. Patterns are ordered from simplest to most complex. For any form design task, identify the pattern that matches your use case, then customize the specs to your design system tokens.

---

## 1. Single Column Form (Default Pattern)

**When to use:** Most forms — signup, login, contact, feedback, simple settings. This is the baseline pattern.

**Why it works:** Top-to-bottom scan path matches natural reading order. No eye zigzag between columns. Fastest completion time for forms under 10 fields (CXL Institute research).

**Specifications:**
- Form max-width: 480px (small forms: 360px, complex forms: 560px)
- Field spacing (gap between fields): 24px
- Section spacing (gap between grouped sections): 40px
- Label: top-aligned, 14px, font-weight 500, margin-bottom 6px
- Input height: 44px (mobile minimum) to 48px
- Input padding: 12px 16px
- Input border: 1px solid #D1D5DB (gray-300), border-radius 8px
- Input focus: 2px ring, brand color, border color change
- Primary button: full width on mobile, auto-width (min 120px) on desktop
- Button margin-top: 32px above last field

**Responsive behavior:**
- Desktop (>768px): centered on page or left-aligned in content area, max-width applied
- Tablet (600-768px): same layout, padding adjusts to 24px sides
- Mobile (<600px): full width with 16px padding, fields and button go full width

```tsx
// React: SingleColumnForm
interface FormFieldProps {
  label: string;
  name: string;
  type?: string;
  placeholder?: string;
  required?: boolean;
  error?: string;
}

function FormField({ label, name, type = 'text', placeholder, required, error }: FormFieldProps) {
  const fieldId = `field-${name}`;
  const errorId = `error-${name}`;
  return (
    <div className="form-field">
      <label htmlFor={fieldId} className="form-label">
        {label}
        {required && <span className="form-required" aria-hidden="true"> *</span>}
      </label>
      <input
        id={fieldId}
        name={name}
        type={type}
        placeholder={placeholder}
        required={required}
        aria-required={required}
        aria-invalid={!!error}
        aria-errormessage={error ? errorId : undefined}
        className={`form-input ${error ? 'form-input--error' : ''}`}
      />
      {error && (
        <p id={errorId} className="form-error" role="alert">
          <svg aria-hidden="true" className="form-error-icon" viewBox="0 0 16 16" fill="currentColor">
            <path d="M8 1a7 7 0 100 14A7 7 0 008 1zm-.75 4a.75.75 0 011.5 0v3.5a.75.75 0 01-1.5 0V5zm.75 6.25a.75.75 0 100-1.5.75.75 0 000 1.5z"/>
          </svg>
          {error}
        </p>
      )}
    </div>
  );
}

function SingleColumnForm() {
  return (
    <form className="single-column-form" noValidate>
      <FormField label="Full name" name="name" required />
      <FormField label="Email address" name="email" type="email" required />
      <FormField label="Message" name="message" required />
      <button type="submit" className="form-button-primary">
        Send message
      </button>
    </form>
  );
}
```

```css
/* CSS: Single Column Form */
.single-column-form {
  max-width: 480px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.form-label {
  font-size: 14px;
  font-weight: 500;
  color: #111827;
}

.form-required {
  color: #DC2626;
}

.form-input {
  height: 48px;
  padding: 12px 16px;
  font-size: 16px; /* Prevents iOS zoom */
  border: 1px solid #D1D5DB;
  border-radius: 8px;
  background: #FFFFFF;
  color: #111827;
  transition: border-color 150ms ease, box-shadow 150ms ease;
}

.form-input:focus {
  outline: none;
  border-color: #2563EB;
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
}

.form-input--error {
  border-color: #DC2626;
}

.form-input--error:focus {
  box-shadow: 0 0 0 2px rgba(220, 38, 38, 0.2);
}

.form-error {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #DC2626;
  margin: 0;
}

.form-error-icon {
  width: 14px;
  height: 14px;
  flex-shrink: 0;
}

.form-button-primary {
  margin-top: 8px;
  height: 48px;
  padding: 0 24px;
  font-size: 16px;
  font-weight: 600;
  color: #FFFFFF;
  background: #2563EB;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 150ms ease;
}

.form-button-primary:hover {
  background: #1D4ED8;
}

.form-button-primary:focus-visible {
  outline: 2px solid #2563EB;
  outline-offset: 2px;
}

@media (max-width: 600px) {
  .single-column-form {
    max-width: 100%;
    padding: 0 16px;
  }

  .form-button-primary {
    width: 100%;
  }
}
```

---

## 2. Two-Column Form (Label Left, Input Right)

**When to use:** Data-heavy desktop forms (admin panels, CRMs, enterprise settings) where horizontal space is available and labels are short.

**Why it works:** Scannable label column on the left makes it easy to find specific fields in long forms. Common in data-entry workflows where users revisit the form frequently.

**Specifications:**
- Form max-width: 720px
- Label column: 200px fixed, right-aligned text, 14px, font-weight 500
- Input column: flex-1 (fills remaining space)
- Gap between label and input: 24px
- Row spacing: 20px
- Input specs: same as single column

**Responsive behavior:**
- Desktop (>768px): two-column layout
- Tablet and mobile (<768px): collapses to single column with top-aligned labels

```tsx
function TwoColumnForm() {
  return (
    <form className="two-column-form" noValidate>
      <div className="two-col-row">
        <label htmlFor="tc-name" className="two-col-label">Full name</label>
        <div className="two-col-input">
          <input id="tc-name" name="name" type="text" className="form-input" required />
        </div>
      </div>
      <div className="two-col-row">
        <label htmlFor="tc-email" className="two-col-label">Email address</label>
        <div className="two-col-input">
          <input id="tc-email" name="email" type="email" className="form-input" required />
        </div>
      </div>
      <div className="two-col-row">
        <label htmlFor="tc-role" className="two-col-label">Role</label>
        <div className="two-col-input">
          <select id="tc-role" name="role" className="form-input">
            <option value="">Select a role</option>
            <option value="admin">Admin</option>
            <option value="editor">Editor</option>
            <option value="viewer">Viewer</option>
          </select>
        </div>
      </div>
      <div className="two-col-row">
        <div className="two-col-label" />
        <div className="two-col-input">
          <button type="submit" className="form-button-primary">Save changes</button>
        </div>
      </div>
    </form>
  );
}
```

```css
.two-column-form {
  max-width: 720px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.two-col-row {
  display: flex;
  align-items: flex-start;
  gap: 24px;
}

.two-col-label {
  width: 200px;
  flex-shrink: 0;
  text-align: right;
  font-size: 14px;
  font-weight: 500;
  color: #374151;
  padding-top: 12px;
}

.two-col-input {
  flex: 1;
}

@media (max-width: 768px) {
  .two-col-row {
    flex-direction: column;
    gap: 6px;
  }

  .two-col-label {
    width: auto;
    text-align: left;
    padding-top: 0;
  }
}
```

---

## 3. Card-Based Form Sections

**When to use:** Complex forms with 10+ fields that can be grouped into logical sections — profile settings, application forms, onboarding.

**Why it works:** Cards create visual boundaries that chunk information (Miller's Law). Users can scan section headers to find what they need without parsing every field.

**Specifications:**
- Card: background #FFFFFF, border 1px solid #E5E7EB, border-radius 12px, padding 24px (32px desktop)
- Card header: 18px font-weight 600, with optional description in 14px color #6B7280
- Card spacing: 24px between cards
- Fields within card: 20px gap
- Form max-width: 640px

**Responsive behavior:**
- Desktop: cards have padding 32px, max-width applied
- Mobile: cards stretch full width, padding 20px, border-radius may reduce to 0 if edge-to-edge

```tsx
interface FormSectionProps {
  title: string;
  description?: string;
  children: React.ReactNode;
}

function FormSection({ title, description, children }: FormSectionProps) {
  return (
    <fieldset className="form-card-section">
      <legend className="form-card-header">
        <span className="form-card-title">{title}</span>
        {description && <span className="form-card-description">{description}</span>}
      </legend>
      <div className="form-card-fields">{children}</div>
    </fieldset>
  );
}

function CardBasedForm() {
  return (
    <form className="card-form" noValidate>
      <FormSection title="Personal Information" description="Your basic contact details.">
        <FormField label="Full name" name="name" required />
        <FormField label="Email" name="email" type="email" required />
        <FormField label="Phone" name="phone" type="tel" />
      </FormSection>
      <FormSection title="Address" description="Where should we send things?">
        <FormField label="Street address" name="street" required />
        <FormField label="City" name="city" required />
        <FormField label="State" name="state" required />
        <FormField label="ZIP code" name="zip" required />
      </FormSection>
      <div className="form-card-actions">
        <button type="button" className="form-button-secondary">Cancel</button>
        <button type="submit" className="form-button-primary">Save</button>
      </div>
    </form>
  );
}
```

```css
.card-form {
  max-width: 640px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-card-section {
  background: #FFFFFF;
  border: 1px solid #E5E7EB;
  border-radius: 12px;
  padding: 32px;
  margin: 0;
}

.form-card-header {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 24px;
  padding: 0;
}

.form-card-title {
  font-size: 18px;
  font-weight: 600;
  color: #111827;
}

.form-card-description {
  font-size: 14px;
  color: #6B7280;
}

.form-card-fields {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-card-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

.form-button-secondary {
  height: 44px;
  padding: 0 20px;
  font-size: 14px;
  font-weight: 500;
  color: #374151;
  background: #FFFFFF;
  border: 1px solid #D1D5DB;
  border-radius: 8px;
  cursor: pointer;
}

@media (max-width: 600px) {
  .form-card-section {
    padding: 20px;
    border-radius: 0;
    border-left: none;
    border-right: none;
  }
}
```

---

## 4. Accordion Form Sections

**When to use:** Very long forms (15+ fields) where users need to focus on one section at a time. Settings pages, configuration panels, application forms.

**Why it works:** Reduces visible complexity. Users see a summary of sections and expand only what they need. Especially useful for forms that are frequently revisited for partial edits.

**Specifications:**
- Accordion container: max-width 640px
- Section header: height 56px, padding 0 20px, font-size 16px, font-weight 500
- Section header: includes expand/collapse chevron (right side), section completion indicator (optional)
- Section content: padding 20px, fields with 20px gap
- Border between sections: 1px solid #E5E7EB
- Animation: height transition 200ms ease-out

```tsx
import { useState } from 'react';

interface AccordionSectionProps {
  title: string;
  isOpen: boolean;
  onToggle: () => void;
  children: React.ReactNode;
  isComplete?: boolean;
}

function AccordionSection({ title, isOpen, onToggle, children, isComplete }: AccordionSectionProps) {
  const sectionSlug = title.toLowerCase().replace(/\s+/g, '-');
  const headerId = `accordion-header-${sectionSlug}`;
  const panelId = `accordion-panel-${sectionSlug}`;

  return (
    <div className="accordion-section">
      <button
        id={headerId}
        type="button"
        className="accordion-header"
        onClick={onToggle}
        aria-expanded={isOpen}
        aria-controls={panelId}
      >
        <span className="accordion-title">
          {isComplete && <span className="accordion-check" aria-label="Complete">&#10003;</span>}
          {title}
        </span>
        <svg
          className={`accordion-chevron ${isOpen ? 'accordion-chevron--open' : ''}`}
          width="20" height="20" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"
        >
          <path fillRule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" />
        </svg>
      </button>
      <div
        id={panelId}
        role="region"
        aria-labelledby={headerId}
        className={`accordion-panel ${isOpen ? 'accordion-panel--open' : ''}`}
        hidden={!isOpen}
      >
        <div className="accordion-content">{children}</div>
      </div>
    </div>
  );
}

function AccordionForm() {
  const [openSection, setOpenSection] = useState(0);

  return (
    <form className="accordion-form" noValidate>
      <AccordionSection
        title="Personal Information"
        isOpen={openSection === 0}
        onToggle={() => setOpenSection(openSection === 0 ? -1 : 0)}
      >
        <FormField label="Full name" name="name" required />
        <FormField label="Email" name="email" type="email" required />
      </AccordionSection>
      <AccordionSection
        title="Address"
        isOpen={openSection === 1}
        onToggle={() => setOpenSection(openSection === 1 ? -1 : 1)}
      >
        <FormField label="Street" name="street" required />
        <FormField label="City" name="city" required />
      </AccordionSection>
      <AccordionSection
        title="Preferences"
        isOpen={openSection === 2}
        onToggle={() => setOpenSection(openSection === 2 ? -1 : 2)}
      >
        <FormField label="Language" name="language" />
        <FormField label="Timezone" name="timezone" />
      </AccordionSection>
      <button type="submit" className="form-button-primary" style={{ marginTop: 16 }}>
        Save all
      </button>
    </form>
  );
}
```

```css
.accordion-form {
  max-width: 640px;
  border: 1px solid #E5E7EB;
  border-radius: 12px;
  overflow: hidden;
}

.accordion-section {
  border-bottom: 1px solid #E5E7EB;
}

.accordion-section:last-of-type {
  border-bottom: none;
}

.accordion-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 56px;
  padding: 0 20px;
  font-size: 16px;
  font-weight: 500;
  color: #111827;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
}

.accordion-header:hover {
  background: #F9FAFB;
}

.accordion-title {
  display: flex;
  align-items: center;
  gap: 8px;
}

.accordion-check {
  color: #059669;
  font-size: 14px;
}

.accordion-chevron {
  transition: transform 200ms ease-out;
  color: #6B7280;
}

.accordion-chevron--open {
  transform: rotate(180deg);
}

.accordion-content {
  padding: 4px 20px 24px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
```

---

## 5. Inline Form (Horizontal)

**When to use:** Simple 1-3 field forms that appear inline with content — newsletter signup, search, quick add, email invite.

**Why it works:** Minimal visual weight. Does not break the user's flow. Action feels lightweight and fast.

**Specifications:**
- Form: display flex, align-items center, gap 8-12px
- Input height: 40-44px
- Button height: matches input height exactly
- Max-width: 500px for the entire row
- Label: visually hidden (use aria-label on input) or placed above the row

```tsx
function InlineForm() {
  return (
    <form className="inline-form" noValidate>
      <input
        type="email"
        name="email"
        placeholder="Enter your email"
        aria-label="Email address for newsletter"
        className="form-input inline-form-input"
        required
      />
      <button type="submit" className="form-button-primary inline-form-button">
        Subscribe
      </button>
    </form>
  );
}
```

```css
.inline-form {
  display: flex;
  align-items: center;
  gap: 8px;
  max-width: 440px;
}

.inline-form-input {
  flex: 1;
  height: 44px;
  min-width: 0;
}

.inline-form-button {
  flex-shrink: 0;
  height: 44px;
  margin-top: 0;
  white-space: nowrap;
}

@media (max-width: 480px) {
  .inline-form {
    flex-direction: column;
    max-width: 100%;
  }

  .inline-form-input,
  .inline-form-button {
    width: 100%;
  }
}
```

---

## 6. Search Form (Minimal)

**When to use:** Primary search on a page or app. Search bars in headers, hero sections, command palettes.

**Specifications:**
- Input height: 44-56px (larger for hero search)
- Search icon: 20px, positioned inside input left side, color #9CA3AF
- Input padding-left: 44px (icon + spacing)
- Clear button: appears when input has value, right side
- Border-radius: 8-24px (pill shape for hero search, rounded rect for standard)
- Optional: search suggestions dropdown below

```tsx
import { useState, useRef } from 'react';

function SearchForm() {
  const [query, setQuery] = useState('');
  const inputRef = useRef<HTMLInputElement>(null);

  return (
    <form className="search-form" role="search" noValidate>
      <div className="search-input-wrapper">
        <svg className="search-icon" width="20" height="20" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
          <path fillRule="evenodd" d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z" />
        </svg>
        <input
          ref={inputRef}
          type="search"
          name="q"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search..."
          aria-label="Search"
          className="search-input"
        />
        {query && (
          <button
            type="button"
            className="search-clear"
            onClick={() => { setQuery(''); inputRef.current?.focus(); }}
            aria-label="Clear search"
          >
            &times;
          </button>
        )}
      </div>
    </form>
  );
}
```

```css
.search-form {
  max-width: 600px;
  width: 100%;
}

.search-input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 14px;
  color: #9CA3AF;
  pointer-events: none;
}

.search-input {
  width: 100%;
  height: 48px;
  padding: 0 44px 0 44px;
  font-size: 16px;
  border: 1px solid #D1D5DB;
  border-radius: 24px;
  background: #FFFFFF;
  color: #111827;
}

.search-input:focus {
  outline: none;
  border-color: #2563EB;
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.15);
}

.search-clear {
  position: absolute;
  right: 8px;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  color: #6B7280;
  background: none;
  border: none;
  border-radius: 50%;
  cursor: pointer;
}

.search-clear:hover {
  background: #F3F4F6;
  color: #111827;
}
```

---

## 7. Filter Form — Sidebar

**When to use:** E-commerce product listing, job boards, property search, any catalog page with faceted filtering.

**Specifications:**
- Sidebar width: 260-300px
- Section title: 14px, font-weight 600, text-transform uppercase, letter-spacing 0.5px
- Section spacing: 24px between filter groups
- Checkbox/radio vertical spacing: 12px
- "Apply" button: full width at bottom of sidebar (if not auto-applying)
- Mobile: sidebar becomes a bottom sheet or modal with "Show results" CTA

```tsx
function FilterSidebar() {
  return (
    <aside className="filter-sidebar" aria-label="Filters">
      <div className="filter-header">
        <h2 className="filter-heading">Filters</h2>
        <button type="button" className="filter-clear-all">Clear all</button>
      </div>

      <form noValidate>
        <fieldset className="filter-group">
          <legend className="filter-group-title">Category</legend>
          <label className="filter-checkbox">
            <input type="checkbox" name="category" value="electronics" />
            <span>Electronics</span>
          </label>
          <label className="filter-checkbox">
            <input type="checkbox" name="category" value="clothing" />
            <span>Clothing</span>
          </label>
          <label className="filter-checkbox">
            <input type="checkbox" name="category" value="home" />
            <span>Home &amp; Garden</span>
          </label>
        </fieldset>

        <fieldset className="filter-group">
          <legend className="filter-group-title">Price Range</legend>
          <label className="filter-radio">
            <input type="radio" name="price" value="0-25" />
            <span>Under $25</span>
          </label>
          <label className="filter-radio">
            <input type="radio" name="price" value="25-50" />
            <span>$25 - $50</span>
          </label>
          <label className="filter-radio">
            <input type="radio" name="price" value="50-100" />
            <span>$50 - $100</span>
          </label>
          <label className="filter-radio">
            <input type="radio" name="price" value="100+" />
            <span>$100+</span>
          </label>
        </fieldset>

        <button type="submit" className="form-button-primary filter-apply">
          Show results
        </button>
      </form>
    </aside>
  );
}
```

```css
.filter-sidebar {
  width: 280px;
  padding: 24px;
  border-right: 1px solid #E5E7EB;
  flex-shrink: 0;
}

.filter-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.filter-heading {
  font-size: 18px;
  font-weight: 600;
  margin: 0;
}

.filter-clear-all {
  font-size: 13px;
  color: #2563EB;
  background: none;
  border: none;
  cursor: pointer;
}

.filter-group {
  border: none;
  padding: 0;
  margin: 0 0 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.filter-group-title {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #6B7280;
  margin-bottom: 4px;
}

.filter-checkbox,
.filter-radio {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
  color: #374151;
  cursor: pointer;
}

.filter-apply {
  width: 100%;
  margin-top: 8px;
}
```

---

## 8. Filter Form — Top Bar (Horizontal)

**When to use:** When sidebar space is unavailable. Dashboard filters, report filters, table filters. Common in analytics and admin panels.

**Specifications:**
- Bar: display flex, gap 12-16px, align-items flex-end, flex-wrap wrap
- Each filter: select/dropdown with top-aligned label
- Filter width: 160-200px each
- "Apply" button: inline at the end of the row
- Mobile: stack vertically or use a modal/bottom sheet

```tsx
function FilterBar() {
  return (
    <form className="filter-bar" role="search" aria-label="Filter results" noValidate>
      <div className="filter-bar-item">
        <label htmlFor="fb-status" className="filter-bar-label">Status</label>
        <select id="fb-status" name="status" className="filter-bar-select">
          <option value="">All</option>
          <option value="active">Active</option>
          <option value="inactive">Inactive</option>
          <option value="pending">Pending</option>
        </select>
      </div>
      <div className="filter-bar-item">
        <label htmlFor="fb-date" className="filter-bar-label">Date range</label>
        <select id="fb-date" name="dateRange" className="filter-bar-select">
          <option value="7d">Last 7 days</option>
          <option value="30d">Last 30 days</option>
          <option value="90d">Last 90 days</option>
          <option value="1y">Last year</option>
        </select>
      </div>
      <div className="filter-bar-item">
        <label htmlFor="fb-sort" className="filter-bar-label">Sort by</label>
        <select id="fb-sort" name="sort" className="filter-bar-select">
          <option value="newest">Newest first</option>
          <option value="oldest">Oldest first</option>
          <option value="name">Name A-Z</option>
        </select>
      </div>
      <button type="submit" className="form-button-primary filter-bar-apply">Apply</button>
    </form>
  );
}
```

```css
.filter-bar {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  gap: 16px;
  padding: 16px 0;
  border-bottom: 1px solid #E5E7EB;
}

.filter-bar-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 160px;
}

.filter-bar-label {
  font-size: 12px;
  font-weight: 500;
  color: #6B7280;
}

.filter-bar-select {
  height: 40px;
  padding: 0 32px 0 12px;
  font-size: 14px;
  border: 1px solid #D1D5DB;
  border-radius: 6px;
  background: #FFFFFF;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg width='12' height='8' viewBox='0 0 12 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1.5L6 6.5L11 1.5' stroke='%236B7280' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
}

.filter-bar-apply {
  height: 40px;
  margin-top: 0;
}

@media (max-width: 600px) {
  .filter-bar {
    flex-direction: column;
    align-items: stretch;
  }

  .filter-bar-item {
    min-width: auto;
  }

  .filter-bar-apply {
    width: 100%;
  }
}
```

---

## 9. Filter Form — Bottom Sheet (Mobile)

**When to use:** Mobile filter experience for complex filter sets that would take too much screen space inline.

**Specifications:**
- Bottom sheet: slides up from bottom, border-radius 16px 16px 0 0 at top
- Header: "Filters" title + close button + "Clear all" link
- Content: scrollable, same structure as sidebar filter
- Footer: sticky, "Show X results" primary button
- Overlay: background rgba(0,0,0,0.5)
- Animation: slide up 300ms ease-out

```tsx
interface FilterSheetProps {
  isOpen: boolean;
  onClose: () => void;
  resultCount: number;
  children: React.ReactNode;
}

function FilterSheet({ isOpen, onClose, resultCount, children }: FilterSheetProps) {
  if (!isOpen) return null;

  return (
    <>
      <div className="filter-sheet-overlay" onClick={onClose} aria-hidden="true" />
      <div className="filter-sheet" role="dialog" aria-label="Filters" aria-modal="true">
        <div className="filter-sheet-header">
          <h2 className="filter-sheet-title">Filters</h2>
          <button type="button" className="filter-clear-all">Clear all</button>
          <button type="button" className="filter-sheet-close" onClick={onClose} aria-label="Close filters">
            &times;
          </button>
        </div>
        <div className="filter-sheet-body">
          {children}
        </div>
        <div className="filter-sheet-footer">
          <button type="button" className="form-button-primary" onClick={onClose}>
            Show {resultCount} results
          </button>
        </div>
      </div>
    </>
  );
}
```

```css
.filter-sheet-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 50;
  animation: fadeIn 200ms ease;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.filter-sheet {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  max-height: 85vh;
  background: #FFFFFF;
  border-radius: 16px 16px 0 0;
  display: flex;
  flex-direction: column;
  z-index: 51;
  animation: slideUp 300ms ease-out;
}

@keyframes slideUp {
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
}

.filter-sheet-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 20px;
  border-bottom: 1px solid #E5E7EB;
}

.filter-sheet-title {
  font-size: 18px;
  font-weight: 600;
  margin: 0;
  flex: 1;
}

.filter-sheet-close {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  color: #6B7280;
  background: none;
  border: none;
  cursor: pointer;
}

.filter-sheet-body {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
}

.filter-sheet-footer {
  padding: 16px 20px;
  padding-bottom: max(16px, env(safe-area-inset-bottom));
  border-top: 1px solid #E5E7EB;
}

.filter-sheet-footer .form-button-primary {
  width: 100%;
}
```

---

## 10. Settings Form (Grouped Sections with Save)

**When to use:** App settings, account settings, preferences. Typically a full page with multiple sections.

**Specifications:**
- Page layout: sidebar navigation (section links) + content area
- Content max-width: 640px
- Each section: card or separated by divider
- Section header: 20px font-weight 600
- "Save" button: sticky bottom bar or per-section save
- Unsaved changes indicator: dot or "Unsaved changes" text in header

```tsx
function SettingsForm() {
  return (
    <div className="settings-layout">
      <nav className="settings-nav" aria-label="Settings sections">
        <a href="#profile" className="settings-nav-link settings-nav-link--active">Profile</a>
        <a href="#notifications" className="settings-nav-link">Notifications</a>
        <a href="#security" className="settings-nav-link">Security</a>
        <a href="#billing" className="settings-nav-link">Billing</a>
      </nav>
      <main className="settings-content">
        <form noValidate>
          <section id="profile" className="settings-section">
            <h2 className="settings-section-title">Profile</h2>
            <p className="settings-section-description">
              This information will be displayed publicly.
            </p>
            <div className="settings-fields">
              <FormField label="Display name" name="displayName" required />
              <FormField label="Bio" name="bio" />
              <FormField label="Website" name="website" type="url" />
            </div>
          </section>
          <section id="notifications" className="settings-section">
            <h2 className="settings-section-title">Notifications</h2>
            <p className="settings-section-description">
              Choose what you want to be notified about.
            </p>
            <div className="settings-fields">
              {/* Toggle switches for notification preferences */}
            </div>
          </section>
          <div className="settings-save-bar">
            <button type="submit" className="form-button-primary">Save changes</button>
          </div>
        </form>
      </main>
    </div>
  );
}
```

```css
.settings-layout {
  display: flex;
  gap: 48px;
  max-width: 960px;
  margin: 0 auto;
  padding: 40px 24px;
}

.settings-nav {
  width: 200px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
  position: sticky;
  top: 24px;
  align-self: flex-start;
}

.settings-nav-link {
  padding: 8px 16px;
  font-size: 14px;
  color: #6B7280;
  text-decoration: none;
  border-radius: 6px;
}

.settings-nav-link:hover {
  color: #111827;
  background: #F9FAFB;
}

.settings-nav-link--active {
  background: #F3F4F6;
  color: #111827;
  font-weight: 500;
}

.settings-content {
  flex: 1;
  max-width: 640px;
}

.settings-section {
  padding-bottom: 40px;
  margin-bottom: 40px;
  border-bottom: 1px solid #E5E7EB;
}

.settings-section-title {
  font-size: 20px;
  font-weight: 600;
  margin: 0 0 4px;
}

.settings-section-description {
  font-size: 14px;
  color: #6B7280;
  margin: 0 0 24px;
}

.settings-fields {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.settings-save-bar {
  position: sticky;
  bottom: 0;
  padding: 16px 0;
  background: #FFFFFF;
  border-top: 1px solid #E5E7EB;
  display: flex;
  justify-content: flex-end;
}

@media (max-width: 768px) {
  .settings-layout {
    flex-direction: column;
    gap: 24px;
  }

  .settings-nav {
    width: auto;
    flex-direction: row;
    overflow-x: auto;
    position: static;
    border-bottom: 1px solid #E5E7EB;
    padding-bottom: 12px;
    gap: 0;
  }

  .settings-nav-link {
    white-space: nowrap;
  }
}
```

---

## 11. Profile Form (Avatar + Fields)

**When to use:** User profile editing. Combines image upload with form fields.

**Specifications:**
- Avatar section: centered or left-aligned, 96-120px avatar, "Change photo" button below
- Fields below avatar in single column
- Form max-width: 480px

```tsx
function ProfileForm() {
  return (
    <form className="profile-form" noValidate>
      <div className="profile-avatar-section">
        <div className="profile-avatar">
          <img src="/avatar.jpg" alt="" className="profile-avatar-img" />
        </div>
        <button type="button" className="profile-avatar-change">Change photo</button>
      </div>
      <div className="profile-fields">
        <FormField label="Display name" name="displayName" required />
        <FormField label="Email" name="email" type="email" required />
        <FormField label="Bio" name="bio" />
        <FormField label="Location" name="location" />
      </div>
      <button type="submit" className="form-button-primary">Save profile</button>
    </form>
  );
}
```

```css
.profile-form {
  max-width: 480px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.profile-avatar-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.profile-avatar {
  width: 96px;
  height: 96px;
  border-radius: 50%;
  overflow: hidden;
  background: #F3F4F6;
}

.profile-avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-avatar-change {
  font-size: 14px;
  color: #2563EB;
  background: none;
  border: none;
  cursor: pointer;
  font-weight: 500;
}

.profile-fields {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
```

---

## 12. Address Form (Smart with Autocomplete)

**When to use:** Any form that collects a mailing or shipping address. Checkout, profile, billing.

**Specifications:**
- Use Google Places API or similar for address autocomplete
- Field order: Street Address (line 1), Apt/Suite (line 2, optional), City, State + ZIP (same row), Country
- State: dropdown for US, text input for international
- ZIP: inputmode="numeric", autocomplete="postal-code"
- Country: dropdown, defaults to user's detected country

```tsx
function AddressForm() {
  return (
    <fieldset className="address-form">
      <legend className="form-card-title">Shipping Address</legend>
      <div className="address-fields">
        <div className="form-field">
          <label htmlFor="addr-street">Street address</label>
          <input id="addr-street" name="street" type="text" autoComplete="address-line1"
            className="form-input" required />
        </div>
        <div className="form-field">
          <label htmlFor="addr-apt">
            Apt, suite, etc. <span className="form-optional">(optional)</span>
          </label>
          <input id="addr-apt" name="apt" type="text" autoComplete="address-line2"
            className="form-input" />
        </div>
        <div className="form-field">
          <label htmlFor="addr-city">City</label>
          <input id="addr-city" name="city" type="text" autoComplete="address-level2"
            className="form-input" required />
        </div>
        <div className="address-row">
          <div className="form-field address-state">
            <label htmlFor="addr-state">State</label>
            <select id="addr-state" name="state" autoComplete="address-level1"
              className="form-input" required>
              <option value="">Select</option>
              <option value="AL">Alabama</option>
              <option value="AK">Alaska</option>
              <option value="AZ">Arizona</option>
              {/* ... all states */}
            </select>
          </div>
          <div className="form-field address-zip">
            <label htmlFor="addr-zip">ZIP code</label>
            <input id="addr-zip" name="zip" type="text" inputMode="numeric"
              autoComplete="postal-code" pattern="[0-9]{5}(-[0-9]{4})?"
              className="form-input" required />
          </div>
        </div>
        <div className="form-field">
          <label htmlFor="addr-country">Country</label>
          <select id="addr-country" name="country" autoComplete="country" className="form-input" required>
            <option value="US">United States</option>
            <option value="CA">Canada</option>
            <option value="GB">United Kingdom</option>
            {/* ... all countries */}
          </select>
        </div>
      </div>
    </fieldset>
  );
}
```

```css
.address-form {
  border: none;
  padding: 0;
  margin: 0;
}

.address-fields {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.address-row {
  display: flex;
  gap: 16px;
}

.address-state {
  flex: 2;
}

.address-zip {
  flex: 1;
}

.form-optional {
  font-size: 13px;
  color: #9CA3AF;
  font-weight: 400;
}

@media (max-width: 480px) {
  .address-row {
    flex-direction: column;
    gap: 20px;
  }
}
```

---

## 13. Payment Form (Card Number, Expiry, CVV)

**When to use:** Checkout, billing, subscription payment.

**Specifications:**
- Card number: inputmode="numeric", autocomplete="cc-number", auto-format with spaces every 4 digits
- Card type detection: Visa starts 4, Mastercard starts 5, Amex starts 34/37 — show icon dynamically
- Expiry: inputmode="numeric", autocomplete="cc-exp", format MM/YY, single field
- CVV: inputmode="numeric", autocomplete="cc-csc", 3 digits (4 for Amex)
- Name on card: autocomplete="cc-name"
- Security badges: lock icon, "Encrypted" text, card brand logos

```tsx
function PaymentForm() {
  return (
    <fieldset className="payment-form">
      <legend className="form-card-title">Payment Details</legend>
      <div className="payment-fields">
        <div className="form-field">
          <label htmlFor="cc-name">Name on card</label>
          <input id="cc-name" name="ccName" type="text" autoComplete="cc-name"
            className="form-input" required />
        </div>
        <div className="form-field">
          <label htmlFor="cc-number">Card number</label>
          <div className="payment-card-wrapper">
            <input id="cc-number" name="ccNumber" type="text" inputMode="numeric"
              autoComplete="cc-number" placeholder="1234 5678 9012 3456"
              maxLength={19} className="form-input payment-card-input" required />
            <div className="payment-card-brands" aria-hidden="true">
              {/* Visa, Mastercard, Amex icons */}
            </div>
          </div>
        </div>
        <div className="payment-row">
          <div className="form-field">
            <label htmlFor="cc-exp">Expiry date</label>
            <input id="cc-exp" name="ccExp" type="text" inputMode="numeric"
              autoComplete="cc-exp" placeholder="MM / YY" maxLength={7}
              className="form-input" required />
          </div>
          <div className="form-field">
            <label htmlFor="cc-cvc">Security code</label>
            <input id="cc-cvc" name="ccCvc" type="text" inputMode="numeric"
              autoComplete="cc-csc" placeholder="CVC" maxLength={4}
              className="form-input" required />
          </div>
        </div>
        <div className="payment-security">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="#059669" aria-hidden="true">
            <path d="M8 1a4 4 0 00-4 4v2H3a1 1 0 00-1 1v6a1 1 0 001 1h10a1 1 0 001-1V8a1 1 0 00-1-1h-1V5a4 4 0 00-4-4zm2 6V5a2 2 0 10-4 0v2h4z" />
          </svg>
          <span>Your payment info is encrypted and secure</span>
        </div>
      </div>
    </fieldset>
  );
}
```

```css
.payment-form {
  border: none;
  padding: 0;
  margin: 0;
}

.payment-fields {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.payment-card-wrapper {
  position: relative;
}

.payment-card-input {
  padding-right: 80px;
}

.payment-card-brands {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  gap: 4px;
}

.payment-row {
  display: flex;
  gap: 16px;
}

.payment-row .form-field {
  flex: 1;
}

.payment-security {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: #059669;
}

@media (max-width: 480px) {
  .payment-row {
    flex-direction: column;
    gap: 20px;
  }
}
```

---

## 14. Login Form

**When to use:** User authentication — email+password, social login, magic link, SSO.

**Specifications:**
- Max-width: 400px, centered vertically and horizontally
- Logo/brand above form
- Email + password fields, stacked
- "Remember me" checkbox + "Forgot password?" link on same row
- Primary CTA: "Sign in", full width
- Social login buttons below with "or" divider
- "Don't have an account? Sign up" link at bottom

```tsx
function LoginForm() {
  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="auth-header">
          <img src="/logo.svg" alt="Company" className="auth-logo" />
          <h1 className="auth-title">Sign in to your account</h1>
        </div>
        <form className="auth-form" noValidate>
          <FormField label="Email address" name="email" type="email" required />
          <FormField label="Password" name="password" type="password" required />
          <div className="auth-options">
            <label className="auth-remember">
              <input type="checkbox" name="remember" />
              <span>Remember me</span>
            </label>
            <a href="/forgot-password" className="auth-link">Forgot password?</a>
          </div>
          <button type="submit" className="form-button-primary auth-submit">Sign in</button>
        </form>
        <div className="auth-divider">
          <span>or continue with</span>
        </div>
        <div className="auth-social">
          <button type="button" className="auth-social-button">Google</button>
          <button type="button" className="auth-social-button">Apple</button>
        </div>
        <p className="auth-footer">
          Don't have an account? <a href="/signup" className="auth-link">Sign up</a>
        </p>
      </div>
    </div>
  );
}
```

```css
.auth-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: #F9FAFB;
}

.auth-card {
  width: 100%;
  max-width: 400px;
  background: #FFFFFF;
  border-radius: 12px;
  padding: 40px 32px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.auth-header {
  text-align: center;
  margin-bottom: 32px;
}

.auth-logo {
  height: 40px;
  margin-bottom: 24px;
}

.auth-title {
  font-size: 22px;
  font-weight: 600;
  margin: 0;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.auth-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
}

.auth-remember {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #374151;
  cursor: pointer;
}

.auth-link {
  color: #2563EB;
  text-decoration: none;
  font-weight: 500;
}

.auth-submit {
  width: 100%;
}

.auth-divider {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 24px 0;
  color: #9CA3AF;
  font-size: 13px;
}

.auth-divider::before,
.auth-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #E5E7EB;
}

.auth-social {
  display: flex;
  gap: 12px;
}

.auth-social-button {
  flex: 1;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 500;
  color: #374151;
  background: #FFFFFF;
  border: 1px solid #D1D5DB;
  border-radius: 8px;
  cursor: pointer;
}

.auth-social-button:hover {
  background: #F9FAFB;
}

.auth-footer {
  text-align: center;
  margin-top: 24px;
  font-size: 14px;
  color: #6B7280;
}
```

---

## 15. Signup Form

**When to use:** New account creation. Keep minimal — name, email, password is the ideal core.

**Specifications:**
- Same container as login form (400px max-width, centered)
- Fields: Full name (optional — consider deferring), Email, Password
- Password requirements shown below password field (live checkmarks)
- Optional: "I agree to Terms" checkbox
- CTA: "Create account"
- Social signup buttons
- "Already have an account? Sign in" link at bottom

```tsx
function SignupForm() {
  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="auth-header">
          <h1 className="auth-title">Create your account</h1>
          <p className="auth-subtitle">Start your 14-day free trial</p>
        </div>
        <form className="auth-form" noValidate>
          <FormField label="Full name" name="name" required />
          <FormField label="Email address" name="email" type="email" required />
          <div className="form-field">
            <label htmlFor="signup-password" className="form-label">Password</label>
            <input id="signup-password" name="password" type="password"
              autoComplete="new-password" className="form-input" required
              aria-describedby="password-requirements" />
            <ul id="password-requirements" className="password-rules">
              <li className="password-rule password-rule--met">At least 8 characters</li>
              <li className="password-rule">One uppercase letter</li>
              <li className="password-rule">One number</li>
            </ul>
          </div>
          <label className="auth-terms">
            <input type="checkbox" name="terms" required />
            <span>I agree to the <a href="/terms" className="auth-link">Terms of Service</a> and <a href="/privacy" className="auth-link">Privacy Policy</a></span>
          </label>
          <button type="submit" className="form-button-primary auth-submit">Create account</button>
        </form>
        <p className="auth-footer">
          Already have an account? <a href="/login" className="auth-link">Sign in</a>
        </p>
      </div>
    </div>
  );
}
```

```css
.auth-subtitle {
  font-size: 14px;
  color: #6B7280;
  margin: 8px 0 0;
}

.password-rules {
  list-style: none;
  padding: 0;
  margin: 4px 0 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.password-rule {
  font-size: 13px;
  color: #9CA3AF;
  display: flex;
  align-items: center;
  gap: 6px;
}

.password-rule::before {
  content: '';
  width: 14px;
  height: 14px;
  border: 1.5px solid #D1D5DB;
  border-radius: 50%;
  flex-shrink: 0;
}

.password-rule--met {
  color: #059669;
}

.password-rule--met::before {
  border-color: #059669;
  background: #059669;
  /* Checkmark via background-image in production */
}

.auth-terms {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: 14px;
  color: #374151;
  cursor: pointer;
}

.auth-terms input {
  margin-top: 3px;
}
```

---

## 16. Contact Form

**When to use:** "Get in touch" pages, support requests, general inquiries.

**Specifications:**
- Fields: Name, Email, Subject (optional dropdown or text), Message (textarea)
- Form max-width: 560px
- Textarea: min-height 120px, resize vertical
- Success state: replace form with confirmation message

```tsx
function ContactForm() {
  return (
    <form className="contact-form" noValidate>
      <h2 className="contact-title">Get in touch</h2>
      <p className="contact-description">
        Fill out the form below and we'll get back to you within 24 hours.
      </p>
      <div className="contact-fields">
        <FormField label="Your name" name="name" required />
        <FormField label="Email address" name="email" type="email" required />
        <div className="form-field">
          <label htmlFor="contact-subject">Subject</label>
          <select id="contact-subject" name="subject" className="form-input">
            <option value="">Select a topic</option>
            <option value="general">General inquiry</option>
            <option value="support">Technical support</option>
            <option value="billing">Billing</option>
            <option value="partnership">Partnership</option>
          </select>
        </div>
        <div className="form-field">
          <label htmlFor="contact-message">Message</label>
          <textarea id="contact-message" name="message" className="form-input contact-textarea"
            rows={5} required aria-required="true" />
        </div>
      </div>
      <button type="submit" className="form-button-primary">Send message</button>
    </form>
  );
}
```

```css
.contact-form {
  max-width: 560px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.contact-title {
  font-size: 24px;
  font-weight: 600;
  margin: 0;
}

.contact-description {
  font-size: 15px;
  color: #6B7280;
  margin: -16px 0 0;
}

.contact-fields {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.contact-textarea {
  height: auto;
  min-height: 120px;
  resize: vertical;
  padding-top: 12px;
}
```

---

## 17. Survey / Questionnaire Layout

**When to use:** User research, NPS, feedback, quizzes.

**Specifications:**
- One question per page (for long surveys) or all visible with clear numbering
- Question number: prominent (24px bold)
- Radio/checkbox as large clickable cards
- Progress bar at top
- "Next" / "Back" navigation at bottom

```tsx
interface SurveyQuestionProps {
  number: number;
  total: number;
  question: string;
  options: string[];
  selected?: string;
  onSelect: (value: string) => void;
}

function SurveyQuestion({ number, total, question, options, selected, onSelect }: SurveyQuestionProps) {
  return (
    <div className="survey-container">
      <div className="survey-progress">
        <div className="survey-progress-bar"
          style={{ width: `${(number / total) * 100}%` }}
          role="progressbar"
          aria-valuenow={number}
          aria-valuemin={1}
          aria-valuemax={total}
          aria-label={`Question ${number} of ${total}`}
        />
      </div>
      <div className="survey-question">
        <span className="survey-number">{number} of {total}</span>
        <h2 className="survey-text">{question}</h2>
        <fieldset className="survey-options">
          <legend className="sr-only">{question}</legend>
          {options.map((option) => (
            <label key={option}
              className={`survey-option ${selected === option ? 'survey-option--selected' : ''}`}>
              <input type="radio" name={`q${number}`} value={option}
                checked={selected === option}
                onChange={() => onSelect(option)} className="sr-only" />
              <span>{option}</span>
            </label>
          ))}
        </fieldset>
      </div>
      <div className="survey-nav">
        <button type="button" className="form-button-secondary">Back</button>
        <button type="button" className="form-button-primary">Next</button>
      </div>
    </div>
  );
}
```

```css
.survey-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 40px 24px;
}

.survey-progress {
  height: 4px;
  background: #E5E7EB;
  border-radius: 2px;
  margin-bottom: 48px;
  overflow: hidden;
}

.survey-progress-bar {
  height: 100%;
  background: #2563EB;
  border-radius: 2px;
  transition: width 300ms ease;
}

.survey-number {
  font-size: 14px;
  font-weight: 500;
  color: #6B7280;
}

.survey-text {
  font-size: 24px;
  font-weight: 600;
  margin: 8px 0 32px;
  line-height: 1.3;
}

.survey-options {
  border: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.survey-option {
  display: flex;
  align-items: center;
  padding: 16px 20px;
  border: 2px solid #E5E7EB;
  border-radius: 10px;
  font-size: 16px;
  color: #111827;
  cursor: pointer;
  transition: border-color 150ms ease, background 150ms ease;
}

.survey-option:hover {
  border-color: #93C5FD;
  background: #EFF6FF;
}

.survey-option--selected {
  border-color: #2563EB;
  background: #EFF6FF;
}

.survey-nav {
  display: flex;
  justify-content: space-between;
  margin-top: 48px;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

---

## 18. Conditional Form (Fields Appear Based on Selection)

**When to use:** When certain fields are only relevant based on a previous answer.

**Specifications:**
- Trigger field: dropdown or radio that determines which fields appear
- Conditional fields: animate in with slide + fade (200ms ease-out)
- Hidden fields: removed from DOM or `display: none` — must not exist in tab order
- Preserve input if user toggles back

```tsx
import { useState } from 'react';

function ConditionalForm() {
  const [contactMethod, setContactMethod] = useState('');

  return (
    <form className="single-column-form" noValidate>
      <div className="form-field">
        <label htmlFor="contact-method">Preferred contact method</label>
        <select id="contact-method" value={contactMethod}
          onChange={(e) => setContactMethod(e.target.value)} className="form-input">
          <option value="">Select...</option>
          <option value="email">Email</option>
          <option value="phone">Phone</option>
          <option value="mail">Mail</option>
        </select>
      </div>
      {contactMethod === 'email' && (
        <div className="form-field form-field--reveal">
          <label htmlFor="cond-email">Email address</label>
          <input id="cond-email" type="email" autoComplete="email" className="form-input" />
        </div>
      )}
      {contactMethod === 'phone' && (
        <div className="form-field form-field--reveal">
          <label htmlFor="cond-phone">Phone number</label>
          <input id="cond-phone" type="tel" autoComplete="tel" className="form-input" />
        </div>
      )}
      {contactMethod === 'mail' && (
        <div className="form-field form-field--reveal">
          <label htmlFor="cond-address">Mailing address</label>
          <textarea id="cond-address" autoComplete="street-address" className="form-input" rows={3} />
        </div>
      )}
      <button type="submit" className="form-button-primary">Submit</button>
    </form>
  );
}
```

```css
.form-field--reveal {
  animation: fieldReveal 200ms ease-out;
}

@keyframes fieldReveal {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

---

## 19. Floating Label Form

**When to use:** Space-constrained designs, modern Material Design aesthetic.

**Specifications:**
- Label starts inside the input as placeholder, moves to top-left on focus/fill
- Label transition: transform + font-size over 150ms
- Filled state: label stays at top, smaller (12px)
- Input padding-top: extra space to accommodate the floated label

```css
.floating-field {
  position: relative;
}

.floating-input {
  width: 100%;
  height: 56px;
  padding: 24px 16px 8px;
  font-size: 16px;
  border: 1px solid #D1D5DB;
  border-radius: 8px;
  background: #FFFFFF;
  color: #111827;
}

.floating-label {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 16px;
  color: #9CA3AF;
  pointer-events: none;
  transition: all 150ms ease;
  background: #FFFFFF;
  padding: 0 4px;
}

.floating-input:focus + .floating-label,
.floating-input:not(:placeholder-shown) + .floating-label {
  top: 8px;
  transform: translateY(0);
  font-size: 12px;
  color: #2563EB;
}

.floating-input:focus {
  outline: none;
  border-color: #2563EB;
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
}
```

---

## 20. Split Screen Auth Form

**When to use:** Marketing-heavy login/signup pages where one side shows branding/testimonials and the other shows the form.

**Specifications:**
- Desktop: 50/50 split or 40/60 (content/form)
- Left panel: brand imagery, testimonial, value proposition
- Right panel: centered form
- Mobile: form only, brand content hidden or minimal header

```css
.split-auth {
  display: flex;
  min-height: 100vh;
}

.split-auth-brand {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 48px;
  background: linear-gradient(135deg, #1E40AF, #7C3AED);
  color: #FFFFFF;
}

.split-auth-brand-title {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 16px;
}

.split-auth-brand-text {
  font-size: 16px;
  opacity: 0.9;
  max-width: 400px;
  text-align: center;
  line-height: 1.6;
}

.split-auth-form {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 32px;
}

@media (max-width: 768px) {
  .split-auth-brand {
    display: none;
  }
}
```

---

## 21-32: Additional Layout Patterns (Quick Reference)

### 21. Tabbed Form Sections
Use tabs to switch between form sections. Each tab shows a subset of fields. Good for profile/settings with distinct categories (General, Security, Billing). Tab bar sits above the form content. Only one tab panel is visible at a time. Use `role="tablist"`, `role="tab"`, `role="tabpanel"` with appropriate `aria-selected` and `aria-controls`.

### 22. Full-Page Takeover Form
Modal-like form that takes over the entire screen. Used for critical or immersive actions (account deletion confirmation, data export, complex wizards). Dark overlay or opaque background. Close button at top-right. Escape key closes.

### 23. Sidebar Drawer Form
Form slides in from the right side as a drawer (width: 400-480px). Common for "Add new item" or "Edit details" in admin panels. Overlay on the rest of the content. Header with title + close button. Footer with action buttons.

### 24. Table Inline Edit Form
Clicking a table cell converts it to an input field for inline editing. Press Enter to save, Escape to cancel. Common in spreadsheet-like interfaces. Use `aria-label` to describe what is being edited. Show a pencil icon on hover to indicate editability.

### 25. Popover Form
Small form that appears in a popover/tooltip on click. Used for quick edits (rename, change status, add tag). Max 2-3 fields. Arrow pointing to the trigger element. Click outside or press Escape to close.

### 26. Stepper Form (Numbered Steps)
Form broken into numbered steps with a vertical or horizontal stepper indicator. Each step has a number, title, and optional description. Current step highlighted, completed steps show checkmark. See `multi-step-form-patterns.md` for full detail.

### 27. Conversational Form (Chat-Style)
One question at a time, presented as a chat conversation. User answers appear as chat bubbles. Input is at the bottom like a chat interface. Good for surveys and onboarding. Typeform-style. Animated transitions between questions.

### 28. Data Table Creation Form
Form for creating/configuring data tables: add columns, set types, define constraints. Used in database tools, Airtable-like interfaces. Column definition is a repeating row pattern: name + type dropdown + options.

### 29. Scheduling Form (Calendar + Time Slots)
Date picker grid + available time slot buttons. Used for appointment booking (Calendly-style). Calendar shows current month with available dates highlighted. Selecting a date reveals time slots as a grid of buttons. Selected time shows confirmation.

### 30. RSVP / Invitation Response Form
Minimal card-based form: name, attending yes/no (large toggle/buttons), plus-one count (stepper), dietary restrictions (checkboxes). Event details displayed above the form. Typically max-width 480px, centered.

### 31. Comparison / Side-by-Side Form
Two forms side by side for comparison input. Used in migration tools, A/B configuration, before/after editors. Each column has a header label. Shared submit button below both columns. Collapses to stacked on mobile.

### 32. Bulk Entry Form
Repeated rows of identical field sets for bulk data entry (inventory, order items, student records). Each row has the same fields. "Add another row" button below. "Remove" button per row. Optional CSV paste support. Table-like header row with column labels.

---

## Pattern Selection Decision Matrix

| Use Case | Recommended Pattern | Key Reason |
|----------|-------------------|------------|
| Signup / Login | Single column, centered card (#14/#15) | Fastest completion, focused attention |
| Contact form | Single column, max-width 560px (#16) | Simple, low friction |
| Checkout | Card-based sections (#3) or multi-step | Groups reduce perceived complexity |
| Settings | Sidebar nav + card sections (#10) | Easy navigation for long forms |
| Admin data entry | Two-column label-left (#2) | Scannability for frequent use |
| Newsletter signup | Inline horizontal (#5) | Minimal footprint, no page navigation |
| Product search | Search form (#6) | Instantly recognizable pattern |
| Product filters | Sidebar desktop (#7) / bottom sheet mobile (#9) | Does not obscure results |
| Dashboard filters | Top bar horizontal (#8) | Compact, inline with content |
| Quick edit | Popover (#25) or inline edit (#24) | No page navigation needed |
| Survey / quiz | One question per page (#17) | Reduces overwhelm |
| Onboarding | Multi-step stepper (#26) or conversational (#27) | Progressive, guided experience |
| Profile editing | Profile form with avatar (#11) | Combines media + fields naturally |
| Shipping address | Smart address form (#12) | Autocomplete reduces effort dramatically |
| Payment | Payment card form (#13) | Security cues + auto-detection |
| Complex application | Accordion sections (#4) | Manage complexity, edit specific sections |
| Mobile-first | Any pattern with bottom sheet overlay | Thumb-friendly, full-screen focus |
