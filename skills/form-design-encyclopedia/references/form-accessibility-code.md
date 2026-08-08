# Form Accessibility — Semantic HTML, ARIA, Focus Management, Keyboard Patterns, and Code

## How to Use This Reference

This file is the complete accessibility implementation guide for forms. It covers semantic HTML for every input type, ARIA attribute patterns, required field indication, error association, group labeling, focus management, keyboard interaction patterns for custom inputs, autocomplete attributes, and full accessible form component code. Every form you build should pass the checklist at the end of this file.

---

## Semantic HTML — The Foundation

Accessible forms start with correct HTML. ARIA should supplement HTML semantics, not replace them.

### The Golden Rules

1. **Every input must have a label.** No exceptions. No placeholder-only labels.
2. **Use native HTML elements first.** `<select>`, `<input type="date">`, `<input type="checkbox">` are accessible by default. Custom components must replicate all native behavior.
3. **Use `<form>` elements.** They enable Enter-to-submit and assistive technology form mode.
4. **Use `<fieldset>` and `<legend>` for groups.** Radio groups, checkbox groups, and related field sets.
5. **Use `<button>` for actions.** Not `<div onclick>` or `<a href="#">`.

### Correct HTML for Every Input Type

```html
<!-- Text input -->
<div>
  <label for="name">Full name</label>
  <input id="name" name="name" type="text" required aria-required="true" />
</div>

<!-- Email -->
<div>
  <label for="email">Email address</label>
  <input id="email" name="email" type="email" required aria-required="true"
    autocomplete="email" inputmode="email" />
</div>

<!-- Password -->
<div>
  <label for="password">Password</label>
  <input id="password" name="password" type="password"
    autocomplete="new-password" aria-describedby="password-hint" />
  <p id="password-hint">Must be at least 8 characters with one number</p>
</div>

<!-- Phone -->
<div>
  <label for="phone">Phone number</label>
  <input id="phone" name="phone" type="tel"
    autocomplete="tel" inputmode="tel" />
</div>

<!-- URL -->
<div>
  <label for="website">Website</label>
  <input id="website" name="website" type="url"
    autocomplete="url" inputmode="url" />
</div>

<!-- Number -->
<div>
  <label for="quantity">Quantity</label>
  <input id="quantity" name="quantity" type="text"
    inputmode="numeric" pattern="[0-9]*" />
</div>

<!-- Search -->
<form role="search">
  <label for="search" class="sr-only">Search</label>
  <input id="search" name="q" type="search" />
</form>

<!-- Textarea -->
<div>
  <label for="message">Message</label>
  <textarea id="message" name="message" rows="4"></textarea>
</div>

<!-- Select -->
<div>
  <label for="country">Country</label>
  <select id="country" name="country">
    <option value="">Select a country</option>
    <option value="US">United States</option>
    <option value="CA">Canada</option>
  </select>
</div>

<!-- Checkbox (single) -->
<div>
  <label>
    <input type="checkbox" name="terms" required aria-required="true" />
    I agree to the Terms of Service
  </label>
</div>

<!-- Checkbox group -->
<fieldset>
  <legend>Notification preferences</legend>
  <label><input type="checkbox" name="notify" value="email" /> Email</label>
  <label><input type="checkbox" name="notify" value="sms" /> SMS</label>
  <label><input type="checkbox" name="notify" value="push" /> Push notification</label>
</fieldset>

<!-- Radio group -->
<fieldset>
  <legend>Shipping method</legend>
  <label><input type="radio" name="shipping" value="standard" /> Standard (5-7 days)</label>
  <label><input type="radio" name="shipping" value="express" /> Express (2-3 days)</label>
  <label><input type="radio" name="shipping" value="overnight" /> Overnight</label>
</fieldset>

<!-- File upload -->
<div>
  <label for="resume">Upload resume</label>
  <input id="resume" name="resume" type="file" accept=".pdf,.doc,.docx" />
</div>

<!-- Date -->
<div>
  <label for="birthday">Date of birth</label>
  <input id="birthday" name="birthday" type="date" autocomplete="bday" />
</div>

<!-- Hidden submit context -->
<form>
  <!-- ... fields ... -->
  <button type="submit">Submit</button>
</form>
```

---

## Label Association Methods

### Method 1: `for` / `id` (Preferred)

The most reliable and universally supported method.

```html
<label for="email">Email address</label>
<input id="email" name="email" type="email" />
```

### Method 2: Wrapping `<label>`

Works well for simple checkbox/radio inputs.

```html
<label>
  <input type="checkbox" name="terms" />
  I agree to the Terms of Service
</label>
```

### Method 3: `aria-labelledby`

When the label is not a `<label>` element or when you need to reference multiple elements as the label.

```html
<h3 id="section-title">Personal Information</h3>
<div id="field-desc">Your name as it appears on your ID</div>
<input aria-labelledby="section-title field-desc" />
```

### Method 4: `aria-label`

When there is no visible label (search inputs, icon-only buttons). Use sparingly — visible labels are always preferred.

```html
<input type="search" aria-label="Search products" />
<button type="button" aria-label="Close dialog">&times;</button>
```

### What NOT to Do

```html
<!-- BAD: No label association -->
<span>Email</span>
<input type="email" />

<!-- BAD: Placeholder is not a label -->
<input type="email" placeholder="Email address" />

<!-- BAD: title attribute is not reliably announced -->
<input type="email" title="Email address" />
```

---

## Required Fields

### Visual Indication

```html
<!-- Pattern 1: Asterisk (most common) -->
<label for="name">
  Full name <span aria-hidden="true">*</span>
</label>
<input id="name" required aria-required="true" />

<!-- Pattern 2: "(required)" text -->
<label for="name">
  Full name <span class="required-text">(required)</span>
</label>
<input id="name" required aria-required="true" />

<!-- Pattern 3: Mark optional fields instead (better for mostly-required forms) -->
<label for="phone">
  Phone <span class="optional-text">(optional)</span>
</label>
<input id="phone" />
```

### Form-Level Required Field Instructions

```html
<form aria-describedby="required-instructions">
  <p id="required-instructions" class="form-instructions">
    Fields marked with <span aria-hidden="true">*</span>
    <span class="sr-only">an asterisk</span> are required.
  </p>
  <!-- ... fields ... -->
</form>
```

### ARIA Attributes for Required

```html
<!-- Both HTML required and aria-required for maximum compatibility -->
<input id="name" name="name" type="text"
  required
  aria-required="true" />
```

---

## Error Association

### Inline Error with `aria-errormessage`

```html
<!-- When field has an error -->
<label for="email">Email address</label>
<input id="email" name="email" type="email"
  aria-invalid="true"
  aria-errormessage="email-error"
  aria-describedby="email-error" />
<p id="email-error" role="alert">
  Please enter a valid email address
</p>

<!-- When field is valid (no error) -->
<label for="email">Email address</label>
<input id="email" name="email" type="email"
  aria-invalid="false" />
```

### Multiple Descriptions

When a field has both a hint and an error, use space-separated IDs in `aria-describedby`:

```html
<label for="password">Password</label>
<input id="password" name="password" type="password"
  aria-invalid="true"
  aria-describedby="password-hint password-error" />
<p id="password-hint">Must be at least 8 characters</p>
<p id="password-error" role="alert">Password is too short</p>
```

### Error Summary

```html
<!-- Placed at the top of the form, announced immediately via role="alert" -->
<div role="alert" aria-labelledby="error-heading">
  <h2 id="error-heading">There are 2 errors in this form</h2>
  <ul>
    <li><a href="#email">Email: Please enter a valid email address</a></li>
    <li><a href="#password">Password: Must be at least 8 characters</a></li>
  </ul>
</div>
```

---

## Group Labeling

### `<fieldset>` and `<legend>`

The standard way to group related form controls. Screen readers announce the legend before each control in the group.

```html
<fieldset>
  <legend>Billing address</legend>
  <label for="billing-street">Street</label>
  <input id="billing-street" name="billingStreet" autocomplete="billing street-address" />

  <label for="billing-city">City</label>
  <input id="billing-city" name="billingCity" autocomplete="billing address-level2" />

  <label for="billing-state">State</label>
  <select id="billing-state" name="billingState" autocomplete="billing address-level1">
    <option value="">Select</option>
  </select>
</fieldset>
```

### `role="group"` with `aria-labelledby`

Alternative when you cannot use `<fieldset>` (styling constraints).

```html
<div role="group" aria-labelledby="group-title">
  <h3 id="group-title">Billing address</h3>
  <!-- fields -->
</div>
```

### Radio Group with `role="radiogroup"`

For custom radio implementations:

```html
<div role="radiogroup" aria-labelledby="shipping-label">
  <span id="shipping-label">Shipping method</span>
  <div role="radio" aria-checked="true" tabindex="0">Standard</div>
  <div role="radio" aria-checked="false" tabindex="-1">Express</div>
  <div role="radio" aria-checked="false" tabindex="-1">Overnight</div>
</div>
```

---

## Focus Management in Forms

### Focus Order

- Tab order should follow the visual order (top to bottom, left to right)
- Do not use positive `tabindex` values (only 0 or -1)
- Hidden fields must be removed from tab order (use `display: none` or `hidden`, not just `visibility: hidden`)
- Disabled fields should be in tab order but not interactive (browser default)

### Focus on Error

When validation fails on submit:

```tsx
function focusFirstError(errors: Record<string, string>) {
  const firstErrorField = Object.keys(errors)[0];
  const element = document.getElementById(`field-${firstErrorField}`);

  if (element) {
    // Scroll into view first
    element.scrollIntoView({ behavior: 'smooth', block: 'center' });
    // Focus after scroll animation
    setTimeout(() => element.focus(), 300);
  }
}
```

### Focus in Multi-Step Forms

When advancing to a new step:
1. Move focus to the step heading or the first field of the new step
2. Announce the step change to screen readers
3. Scroll to the top of the new step content

```tsx
function onStepChange(newStepIndex: number) {
  // Focus the step heading
  const heading = document.querySelector(`[data-step="${newStepIndex}"] h2`);
  if (heading instanceof HTMLElement) {
    heading.setAttribute('tabindex', '-1');
    heading.focus();
  }
}
```

### Focus in Modals / Dialogs

When a form appears in a modal:
1. Focus the first focusable element in the modal
2. Trap focus inside the modal (Tab cycles through modal elements only)
3. On close, return focus to the trigger element

```tsx
function useFocusTrap(ref: React.RefObject<HTMLElement>) {
  useEffect(() => {
    const element = ref.current;
    if (!element) return;

    const focusableElements = element.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const firstFocusable = focusableElements[0] as HTMLElement;
    const lastFocusable = focusableElements[focusableElements.length - 1] as HTMLElement;

    function handleKeyDown(e: KeyboardEvent) {
      if (e.key !== 'Tab') return;

      if (e.shiftKey) {
        if (document.activeElement === firstFocusable) {
          e.preventDefault();
          lastFocusable.focus();
        }
      } else {
        if (document.activeElement === lastFocusable) {
          e.preventDefault();
          firstFocusable.focus();
        }
      }
    }

    element.addEventListener('keydown', handleKeyDown);
    firstFocusable?.focus();

    return () => element.removeEventListener('keydown', handleKeyDown);
  }, [ref]);
}
```

---

## Tab Order and Logical Flow

### Rules

1. Tab order must follow reading order (top-to-bottom, left-to-right in LTR languages)
2. Never use `tabindex` greater than 0
3. Use `tabindex="0"` to make non-interactive elements focusable (custom widgets)
4. Use `tabindex="-1"` to make elements programmatically focusable but not in tab order
5. Hidden elements must not be in tab order
6. Within a radio group, Tab moves into the group; arrow keys move between options; Tab moves out

### Testing Tab Order

```
Manual test procedure:
1. Click just before the form (on a non-interactive element)
2. Press Tab
3. Verify: focus moves to the first form field
4. Press Tab again
5. Verify: focus moves to the next logical field
6. Continue through all fields
7. Verify: focus reaches the submit button last
8. Verify: pressing Enter on the submit button submits the form
9. Verify: no fields are skipped
10. Verify: no hidden elements receive focus
```

---

## Keyboard Patterns for Custom Inputs

### Combobox / Autocomplete

```
Tab:        Focus the combobox input
Typing:     Filters the option list, opens the listbox
Down Arrow: Open listbox (if closed), move to next option
Up Arrow:   Move to previous option
Enter:      Select the focused option, close listbox
Escape:     Close listbox without selecting, clear input (second press)
Home:       Move to first option
End:        Move to last option
```

ARIA requirements:
```html
<div role="combobox" aria-expanded="true|false" aria-haspopup="listbox" aria-owns="listbox-id">
  <input aria-autocomplete="list" aria-controls="listbox-id"
    aria-activedescendant="option-id-of-focused-option" />
</div>
<ul id="listbox-id" role="listbox">
  <li id="option-1" role="option" aria-selected="false">Option 1</li>
  <li id="option-2" role="option" aria-selected="true">Option 2</li>
</ul>
```

### Custom Date Picker (Calendar Grid)

```
Tab:        Move focus into calendar (to the selected/focused date)
Arrow keys: Move between days (left/right = prev/next day, up/down = prev/next week)
Page Up:    Previous month
Page Down:  Next month
Home:       First day of month
End:        Last day of month
Enter:      Select the focused date
Escape:     Close the calendar, return focus to the trigger
```

ARIA requirements:
```html
<div role="dialog" aria-label="Choose date" aria-modal="true">
  <button aria-label="Previous month">&lt;</button>
  <h2 id="month-label" aria-live="polite">March 2026</h2>
  <button aria-label="Next month">&gt;</button>
  <table role="grid" aria-labelledby="month-label">
    <thead>
      <tr>
        <th abbr="Sunday">Su</th>
        <th abbr="Monday">Mo</th>
        <!-- ... -->
      </tr>
    </thead>
    <tbody>
      <tr>
        <td role="gridcell">
          <button tabindex="-1" aria-selected="false">1</button>
        </td>
        <td role="gridcell">
          <button tabindex="0" aria-selected="true">2</button>
        </td>
        <!-- ... -->
      </tr>
    </tbody>
  </table>
</div>
```

### Custom Slider

```
Tab:        Focus the slider thumb
Left/Down:  Decrease value by step
Right/Up:   Increase value by step
Home:       Set to minimum value
End:        Set to maximum value
Page Up:    Increase by large step (10x normal step)
Page Down:  Decrease by large step
```

ARIA requirements:
```html
<div role="slider"
  aria-label="Price"
  aria-valuenow="50"
  aria-valuemin="0"
  aria-valuemax="100"
  aria-valuetext="$50"
  tabindex="0">
</div>
```

### Toggle Switch

```
Tab:        Focus the switch
Space:      Toggle on/off
Enter:      Toggle on/off (recommended to support both)
```

ARIA requirements:
```html
<button role="switch" aria-checked="true|false" aria-label="Dark mode">
  <!-- visual switch UI -->
</button>
```

### Custom Select (Listbox)

```
Tab:        Focus the listbox trigger button
Enter/Space: Open the dropdown
Down Arrow:  Open dropdown, move to next option
Up Arrow:    Move to previous option
Home:        First option
End:         Last option
Enter:       Select option, close dropdown
Escape:      Close dropdown without changing selection
Type letter: Jump to first option starting with that letter
```

ARIA requirements:
```html
<button aria-haspopup="listbox" aria-expanded="true|false" aria-labelledby="label-id">
  Selected option text
</button>
<ul role="listbox" aria-labelledby="label-id">
  <li role="option" aria-selected="true" id="opt-1">Option 1</li>
  <li role="option" aria-selected="false" id="opt-2">Option 2</li>
</ul>
```

### Color Picker

```
Tab:           Focus the color picker trigger
Enter/Space:   Open the picker panel
Arrow keys:    Navigate color swatches or move the color cursor
Tab (in panel): Move between swatches, hex input, and controls
Enter:         Select color, close panel
Escape:        Close panel, revert to previous color
```

---

## Autocomplete Attributes Reference

The `autocomplete` attribute enables browser autofill. Use it on every applicable field.

### Personal Information

| Field | autocomplete Value |
|-------|-------------------|
| Full name | `name` |
| First name | `given-name` |
| Last name | `family-name` |
| Honorific prefix | `honorific-prefix` |
| Honorific suffix | `honorific-suffix` |
| Nickname | `nickname` |
| Email | `email` |
| Phone | `tel` |
| Phone country code | `tel-country-code` |
| Phone national | `tel-national` |
| Birthday | `bday` |
| Birthday day | `bday-day` |
| Birthday month | `bday-month` |
| Birthday year | `bday-year` |
| Sex/gender | `sex` |
| Organization | `organization` |
| Organization title | `organization-title` |

### Address

| Field | autocomplete Value |
|-------|-------------------|
| Street address (multi-line) | `street-address` |
| Address line 1 | `address-line1` |
| Address line 2 | `address-line2` |
| City | `address-level2` |
| State/province | `address-level1` |
| ZIP/postal code | `postal-code` |
| Country | `country` |
| Country name | `country-name` |

### Billing-specific (prefix with `billing`)

| Field | autocomplete Value |
|-------|-------------------|
| Billing street | `billing street-address` |
| Billing city | `billing address-level2` |
| Billing state | `billing address-level1` |
| Billing ZIP | `billing postal-code` |

### Shipping-specific (prefix with `shipping`)

| Field | autocomplete Value |
|-------|-------------------|
| Shipping street | `shipping street-address` |
| Shipping city | `shipping address-level2` |

### Payment

| Field | autocomplete Value |
|-------|-------------------|
| Cardholder name | `cc-name` |
| Card number | `cc-number` |
| Expiry date | `cc-exp` |
| Expiry month | `cc-exp-month` |
| Expiry year | `cc-exp-year` |
| CVV/CVC | `cc-csc` |
| Card type | `cc-type` |

### Authentication

| Field | autocomplete Value |
|-------|-------------------|
| Username | `username` |
| Current password | `current-password` |
| New password | `new-password` |
| One-time code | `one-time-code` |

---

## Full Accessible Form — React Component

```tsx
import { useState, useRef, useCallback } from 'react';

interface FieldConfig {
  name: string;
  label: string;
  type: string;
  required?: boolean;
  autocomplete?: string;
  inputMode?: string;
  hint?: string;
  validate?: (value: string) => string | null;
}

interface AccessibleFieldProps {
  config: FieldConfig;
  value: string;
  error: string | null;
  onChange: (value: string) => void;
  onBlur: () => void;
}

function AccessibleField({ config, value, error, onChange, onBlur }: AccessibleFieldProps) {
  const fieldId = `field-${config.name}`;
  const errorId = `error-${config.name}`;
  const hintId = `hint-${config.name}`;

  // Build aria-describedby from hint and error
  const describedBy = [
    config.hint ? hintId : null,
    error ? errorId : null,
  ].filter(Boolean).join(' ') || undefined;

  return (
    <div className="form-field">
      <label htmlFor={fieldId} className="form-label">
        {config.label}
        {config.required && <span aria-hidden="true" className="form-required"> *</span>}
      </label>

      <input
        id={fieldId}
        name={config.name}
        type={config.type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onBlur={onBlur}
        required={config.required}
        aria-required={config.required || undefined}
        aria-invalid={error ? true : undefined}
        aria-errormessage={error ? errorId : undefined}
        aria-describedby={describedBy}
        autoComplete={config.autocomplete}
        inputMode={config.inputMode as any}
        className={`form-input ${error ? 'form-input--error' : ''}`}
      />

      {config.hint && (
        <p id={hintId} className="form-hint">{config.hint}</p>
      )}

      {error && (
        <p id={errorId} className="form-error" role="alert">
          <svg aria-hidden="true" className="form-error-icon" width="14" height="14"
            viewBox="0 0 16 16" fill="currentColor">
            <path d="M8 1a7 7 0 100 14A7 7 0 008 1zm-.75 4a.75.75 0 011.5 0v3.5a.75.75 0 01-1.5 0V5zm.75 6.25a.75.75 0 100-1.5.75.75 0 000 1.5z"/>
          </svg>
          {error}
        </p>
      )}
    </div>
  );
}

function AccessibleForm() {
  const formRef = useRef<HTMLFormElement>(null);
  const [values, setValues] = useState<Record<string, string>>({
    name: '', email: '', password: '', phone: '',
  });
  const [errors, setErrors] = useState<Record<string, string | null>>({});
  const [touched, setTouched] = useState<Record<string, boolean>>({});
  const [submitError, setSubmitError] = useState<string | null>(null);

  const fields: FieldConfig[] = [
    {
      name: 'name',
      label: 'Full name',
      type: 'text',
      required: true,
      autocomplete: 'name',
      validate: (v) => !v.trim() ? 'Full name is required' : null,
    },
    {
      name: 'email',
      label: 'Email address',
      type: 'email',
      required: true,
      autocomplete: 'email',
      inputMode: 'email',
      validate: (v) => {
        if (!v.trim()) return 'Email address is required';
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) return 'Please enter a valid email address';
        return null;
      },
    },
    {
      name: 'password',
      label: 'Password',
      type: 'password',
      required: true,
      autocomplete: 'new-password',
      hint: 'Must be at least 8 characters with one number',
      validate: (v) => {
        if (!v) return 'Password is required';
        if (v.length < 8) return 'Password must be at least 8 characters';
        if (!/\d/.test(v)) return 'Password must include at least one number';
        return null;
      },
    },
    {
      name: 'phone',
      label: 'Phone number',
      type: 'tel',
      autocomplete: 'tel',
      inputMode: 'tel',
      hint: 'Optional — for account recovery only',
    },
  ];

  const validateField = useCallback((name: string, value: string) => {
    const field = fields.find(f => f.name === name);
    return field?.validate?.(value) || null;
  }, []);

  const handleChange = (name: string, value: string) => {
    setValues(prev => ({ ...prev, [name]: value }));
    // Re-validate if the field has been touched and had an error
    if (touched[name] && errors[name]) {
      setErrors(prev => ({ ...prev, [name]: validateField(name, value) }));
    }
  };

  const handleBlur = (name: string) => {
    setTouched(prev => ({ ...prev, [name]: true }));
    setErrors(prev => ({ ...prev, [name]: validateField(name, values[name]) }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitError(null);

    // Validate all fields
    const newErrors: Record<string, string | null> = {};
    let hasErrors = false;
    for (const field of fields) {
      const error = validateField(field.name, values[field.name]);
      newErrors[field.name] = error;
      if (error) hasErrors = true;
    }
    setErrors(newErrors);
    setTouched(Object.fromEntries(fields.map(f => [f.name, true])));

    if (hasErrors) {
      // Focus first error field
      const firstErrorName = Object.keys(newErrors).find(k => newErrors[k]);
      if (firstErrorName) {
        const el = document.getElementById(`field-${firstErrorName}`);
        el?.scrollIntoView({ behavior: 'smooth', block: 'center' });
        setTimeout(() => el?.focus(), 300);
      }
      return;
    }

    // Submit
    try {
      const response = await fetch('/api/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(values),
      });
      if (!response.ok) {
        const data = await response.json();
        if (data.errors) {
          setErrors(data.errors);
          const firstErrorName = Object.keys(data.errors).find(k => data.errors[k]);
          if (firstErrorName) {
            document.getElementById(`field-${firstErrorName}`)?.focus();
          }
        } else {
          setSubmitError(data.message || 'Something went wrong. Please try again.');
        }
      }
    } catch {
      setSubmitError('Unable to connect. Please check your internet and try again.');
    }
  };

  // Collect all current errors for the error summary
  const activeErrors = Object.entries(errors)
    .filter(([, error]) => error)
    .map(([name, error]) => ({ field: name, message: error as string }));

  return (
    <form ref={formRef} onSubmit={handleSubmit} noValidate aria-describedby="form-instructions">
      <p id="form-instructions" className="form-instructions">
        Fields marked with <span aria-hidden="true">*</span> are required.
      </p>

      {/* Error summary (shown after submit with errors) */}
      {activeErrors.length > 0 && touched.name && (
        <div className="error-summary" role="alert" aria-labelledby="error-summary-title">
          <h2 id="error-summary-title" className="error-summary-title">
            {activeErrors.length === 1
              ? 'There is 1 error in this form'
              : `There are ${activeErrors.length} errors in this form`}
          </h2>
          <ul className="error-summary-list">
            {activeErrors.map(({ field, message }) => (
              <li key={field}>
                <a href={`#field-${field}`} className="error-summary-link">{message}</a>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Server error */}
      {submitError && (
        <div className="error-summary" role="alert">
          <p className="error-summary-title">{submitError}</p>
        </div>
      )}

      {/* Fields */}
      <div className="form-fields">
        {fields.map(field => (
          <AccessibleField
            key={field.name}
            config={field}
            value={values[field.name]}
            error={touched[field.name] ? errors[field.name] || null : null}
            onChange={(v) => handleChange(field.name, v)}
            onBlur={() => handleBlur(field.name)}
          />
        ))}
      </div>

      <button type="submit" className="form-button-primary">
        Create account
      </button>
    </form>
  );
}
```

---

## Screen Reader Form Testing Checklist

### VoiceOver (macOS / iOS)

1. **Navigate with Tab:** Each field is reached in logical order
2. **Label announced:** VO reads the label when each field is focused
3. **Type announced:** VO announces "text field", "pop-up button" (select), "checkbox", etc.
4. **Required announced:** VO says "required" for required fields
5. **Hint announced:** VO reads `aria-describedby` hint after the label
6. **Error announced:** When a field has an error, VO reads "invalid data" and the error message
7. **Error summary announced:** The error summary with `role="alert"` is announced when it appears
8. **Group label announced:** For radio/checkbox groups inside `<fieldset>`, VO reads the `<legend>` before each option

### NVDA (Windows)

1. Same checks as VoiceOver
2. **Forms mode:** NVDA enters forms mode automatically when user tabs to a form control
3. **Browse mode:** Ensure form structure is readable in browse mode (headings, fieldsets, labels)

### JAWS (Windows)

1. Same checks as VoiceOver and NVDA
2. **Forms list:** Ctrl+Insert+F5 — all form controls should appear with their labels

### Testing Procedure

```
For each form field:
  1. Tab to the field
  2. Listen: label is announced
  3. Listen: field type is announced
  4. Listen: required/optional status is announced
  5. Listen: hint text is announced (if present)
  6. Type invalid input, then Tab away
  7. Listen: "invalid" is announced when returning to field
  8. Listen: error message is announced
  9. Fix the input
  10. Listen: "invalid" is no longer announced
  11. Verify: error message is no longer present

For the form:
  1. Submit with errors
  2. Listen: error summary is announced (role="alert")
  3. Verify: focus moves to first error field
  4. Submit with valid data
  5. Listen: success confirmation is announced
```

---

## Common Accessibility Mistakes in Forms

| Mistake | Impact | Fix |
|---------|--------|-----|
| No `<label>` element | Screen reader users do not know what a field is for | Add `<label>` with `for`/`id` association |
| Placeholder as label | Label disappears on focus, not announced consistently | Use visible `<label>`, placeholder for examples only |
| Error indicated by color only | Color-blind users miss the error | Add icon + text alongside color |
| No `aria-invalid` | Screen readers do not announce the error state | Add `aria-invalid="true"` when field has error |
| No `aria-errormessage` | Error text is not associated with the field | Add `aria-errormessage` pointing to error element |
| Custom radio/checkbox without ARIA | Not recognized as interactive by screen readers | Add `role`, `aria-checked`, keyboard handlers |
| Tab order does not match visual order | Confusing navigation for keyboard users | Use DOM order that matches visual layout |
| Modal form without focus trap | Users Tab outside the modal to invisible content | Implement focus trap |
| No focus management on error | Users do not know where the error is | Focus first invalid field on submit |
| `autocomplete` attribute missing | Browser/password manager cannot autofill | Add correct `autocomplete` values |
| `inputmode` missing on mobile | Wrong keyboard appears | Add `inputmode` for numeric, email, tel, url |
| Submit button is a `<div>` | Not keyboard accessible, not announced as button | Use `<button type="submit">` |

---

## WCAG 2.2 Form Requirements Summary

| WCAG Criterion | Level | What It Means for Forms |
|---------------|-------|------------------------|
| 1.1.1 Non-text Content | A | Icons in forms need alt text or aria-label |
| 1.3.1 Info and Relationships | A | Labels programmatically associated with inputs |
| 1.3.5 Identify Input Purpose | AA | Use autocomplete attributes |
| 2.1.1 Keyboard | A | All form controls operable with keyboard |
| 2.4.3 Focus Order | A | Tab order matches visual order |
| 2.4.6 Headings and Labels | AA | Labels describe the purpose of the field |
| 2.4.7 Focus Visible | AA | Focus indicator visible on all form controls |
| 2.5.8 Target Size | AA | Touch targets at least 24x24px (44px recommended) |
| 3.2.2 On Input | A | No unexpected behavior on input (no auto-submit) |
| 3.3.1 Error Identification | A | Errors identified and described in text |
| 3.3.2 Labels or Instructions | A | Labels or instructions provided for user input |
| 3.3.3 Error Suggestion | AA | Suggest corrections for errors when possible |
| 3.3.4 Error Prevention | AA | Submissions can be reviewed, confirmed, or reversed |
| 3.3.7 Redundant Entry | A | Do not ask for same info twice in a session |
| 3.3.8 Accessible Authentication | AA | Do not require cognitive tests (CAPTCHAs) without alternatives |
| 4.1.2 Name, Role, Value | A | Custom controls have correct ARIA name, role, and state |
