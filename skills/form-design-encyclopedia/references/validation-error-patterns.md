# Validation & Error Patterns — Timing, Anatomy, 100+ Message Templates, and Accessibility

## How to Use This Reference

This file covers the complete validation and error handling system for forms. It includes: when to validate, how to display errors, 100+ pre-written error message templates organized by field type and error type, async validation patterns, cross-field validation, and full accessibility implementation. When designing or coding any form, use this as your error handling playbook.

---

## Validation Timing — When to Validate

### The Four Validation Timing Strategies

| Strategy | When It Fires | Best For | Pitfalls |
|----------|--------------|----------|----------|
| **On blur** | When user leaves the field | Most fields. Validates after user finishes typing. | User does not see error until they move on. |
| **On submit** | When form is submitted | Simple forms, server-side validation. | Delayed feedback. User may need to scroll to find errors. |
| **Real-time (on change)** | As user types, debounced 300-500ms | Format validation (phone, credit card). Password strength. | Feels aggressive if too fast. Causes layout shifts. |
| **Hybrid (recommended)** | On blur for first validation, then real-time after first error | Best UX: does not interrupt initial typing, but gives immediate feedback once an error is known. | Slightly more complex to implement. |

### The Hybrid Validation Pattern (Recommended)

This is the pattern recommended by Luke Wroblewski and validated by extensive A/B testing:

1. **First interaction:** Do not validate. Let the user type freely.
2. **On blur (first leave):** Validate the field. If valid, optionally show a green check. If invalid, show the error.
3. **After first error:** Switch to real-time validation (on change, debounced 300ms). As the user corrects their input, the error disappears immediately when the input becomes valid.
4. **On submit:** Validate all fields. Scroll to first error. Focus first invalid field.

```tsx
function useHybridValidation(validate: (value: string) => string | null) {
  const [error, setError] = useState<string | null>(null);
  const [touched, setTouched] = useState(false);
  const [dirty, setDirty] = useState(false);

  const handleBlur = (value: string) => {
    setTouched(true);
    setError(validate(value));
  };

  const handleChange = (value: string) => {
    setDirty(true);
    // Only validate on change after the field has been touched and has/had an error
    if (touched && error !== null) {
      setError(validate(value));
    }
  };

  return { error, handleBlur, handleChange, touched, dirty };
}
```

### Debounce Timing Guide

| Validation Type | Debounce Delay | Reason |
|----------------|---------------|--------|
| Format check (email regex, phone format) | 300ms | Fast enough to feel responsive |
| Character count | 0ms (immediate) | No cost, immediate feedback needed |
| Password strength | 150ms | Users watch the meter as they type |
| Async check (email availability) | 500-800ms | Reduce server load, wait for user to finish |
| Cross-field (password match) | 300ms | Only after user is likely done typing |

---

## Error Message Anatomy

### The Three Components of a Good Error Message

Every error message should have three elements:

1. **What went wrong** — Describe the specific error (not a generic "Invalid")
2. **Where it went wrong** — Error is visually attached to the specific field
3. **How to fix it** — Provide a clear action or suggestion

**Example — Bad:** "Invalid input"
**Example — Good:** "Email must include an @ symbol (e.g., name@example.com)"

### Visual Error Anatomy

```
[Label *]
[Input field with red border                    ]
  [Red error icon] [Error message text]
```

**Specifications:**
- Error icon: 14px, color #DC2626, flex-shrink 0
- Error text: font-size 13px, color #DC2626, line-height 1.4
- Error container: margin-top 6px, display flex, align-items flex-start, gap 6px
- Input border: changes to #DC2626
- Input background: optionally changes to #FEF2F2 (red-50)
- Reserve space: use min-height 20px on error container to prevent layout shift

### Error Placement Options

| Placement | When to Use | Pros | Cons |
|-----------|------------|------|------|
| **Below field (default)** | Most forms | Closest to error source, clear association | Pushes content down (layout shift) |
| **Beside field (right)** | Two-column forms with space | No layout shift | Not enough space on mobile |
| **Tooltip/popover** | Inline edit, compact forms | No layout impact | Requires hover/focus, accessibility concerns |
| **Error summary (top)** | In addition to inline, for screen readers | Overview of all errors | User must match errors to fields |

**Recommendation:** Always use below-field placement as the primary pattern. Add an error summary at the top for forms with many fields and for screen reader users.

### Error Summary Pattern

```tsx
function ErrorSummary({ errors }: { errors: { field: string; message: string }[] }) {
  if (errors.length === 0) return null;

  return (
    <div className="error-summary" role="alert" aria-labelledby="error-summary-title">
      <h2 id="error-summary-title" className="error-summary-title">
        There {errors.length === 1 ? 'is 1 error' : `are ${errors.length} errors`} in this form
      </h2>
      <ul className="error-summary-list">
        {errors.map(({ field, message }) => (
          <li key={field}>
            <a href={`#field-${field}`} className="error-summary-link">{message}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

```css
.error-summary {
  padding: 16px 20px;
  background: #FEF2F2;
  border: 1px solid #FECACA;
  border-radius: 8px;
  margin-bottom: 24px;
}

.error-summary-title {
  font-size: 15px;
  font-weight: 600;
  color: #991B1B;
  margin: 0 0 8px;
}

.error-summary-list {
  margin: 0;
  padding-left: 20px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.error-summary-link {
  font-size: 14px;
  color: #DC2626;
  text-decoration: underline;
}
```

---

## 100+ Error Message Templates

### Text Fields (Name, Title, Generic)

| Error Type | Message |
|-----------|---------|
| Required | "Full name is required" |
| Too short | "Name must be at least 2 characters" |
| Too long | "Name cannot exceed 100 characters" |
| Invalid characters | "Name can only contain letters, spaces, and hyphens" |
| Numbers in name | "Name should not contain numbers" |

### Email

| Error Type | Message |
|-----------|---------|
| Required | "Email address is required" |
| Missing @ | "Email must include an @ symbol" |
| Missing domain | "Please enter a complete email (e.g., name@example.com)" |
| Invalid format | "This doesn't look like a valid email address" |
| Disposable email | "Please use a non-disposable email address" |
| Already registered | "An account with this email already exists. Sign in instead?" |
| Domain suggestion | "Did you mean name@gmail.com?" |
| Corporate email required | "Please use your work email address" |

### Password

| Error Type | Message |
|-----------|---------|
| Required | "Password is required" |
| Too short | "Password must be at least 8 characters" |
| Too long | "Password cannot exceed 128 characters" |
| Missing uppercase | "Include at least one uppercase letter" |
| Missing lowercase | "Include at least one lowercase letter" |
| Missing number | "Include at least one number" |
| Missing special char | "Include at least one special character (!@#$%^&*)" |
| Common password | "This password is too common. Please choose something more unique." |
| Contains username | "Password should not contain your username or email" |
| Same as current | "New password must be different from your current password" |
| Mismatch | "Passwords do not match" |
| Incorrect (login) | "Incorrect password. Try again or reset your password." |

### Phone Number

| Error Type | Message |
|-----------|---------|
| Required | "Phone number is required" |
| Invalid format | "Please enter a valid phone number" |
| Too short | "Phone number is too short" |
| Too long | "Phone number is too long" |
| Invalid country code | "Please select a valid country code" |
| Letters present | "Phone number should only contain digits" |

### URL

| Error Type | Message |
|-----------|---------|
| Required | "URL is required" |
| Invalid format | "Please enter a valid URL (e.g., https://example.com)" |
| Missing protocol | "URL must start with http:// or https://" |
| Unreachable | "This URL could not be reached. Please check and try again." |

### Number

| Error Type | Message |
|-----------|---------|
| Required | "This field is required" |
| Not a number | "Please enter a valid number" |
| Below minimum | "Value must be at least {min}" |
| Above maximum | "Value cannot exceed {max}" |
| Not an integer | "Please enter a whole number" |
| Negative | "Value must be positive" |

### Date

| Error Type | Message |
|-----------|---------|
| Required | "Date is required" |
| Invalid format | "Please enter a valid date (MM/DD/YYYY)" |
| In the past | "Date must be in the future" |
| In the future | "Date cannot be in the future" |
| Before minimum | "Date must be after {minDate}" |
| After maximum | "Date must be before {maxDate}" |
| End before start | "End date must be after start date" |
| Weekend selected | "Please select a weekday" |

### Credit Card

| Error Type | Message |
|-----------|---------|
| Required | "Card number is required" |
| Invalid number | "Please enter a valid card number" |
| Unsupported type | "We accept Visa, Mastercard, and Amex" |
| Expired | "This card has expired" |
| Invalid expiry | "Please enter a valid expiry date (MM/YY)" |
| Invalid CVV | "CVV must be {3 or 4} digits" |
| Declined | "Your card was declined. Please try a different card." |
| Insufficient funds | "Insufficient funds. Please try a different card." |

### Address

| Error Type | Message |
|-----------|---------|
| Street required | "Street address is required" |
| City required | "City is required" |
| State required | "Please select a state" |
| ZIP required | "ZIP code is required" |
| Invalid ZIP | "Please enter a valid ZIP code (e.g., 12345 or 12345-6789)" |
| Country required | "Please select a country" |
| Unverifiable | "We couldn't verify this address. Please check for typos." |
| PO Box not allowed | "We cannot ship to PO Boxes. Please enter a street address." |

### File Upload

| Error Type | Message |
|-----------|---------|
| Required | "Please upload a file" |
| Too large | "File must be smaller than {maxSize}MB" |
| Wrong type | "Please upload a {acceptedTypes} file" |
| Too many | "Maximum {max} files allowed" |
| Upload failed | "Upload failed. Please try again." |
| Corrupted | "This file appears to be corrupted. Please try a different file." |
| Dimensions | "Image must be at least {width}x{height}px" |

### Select / Dropdown

| Error Type | Message |
|-----------|---------|
| Required | "Please select an option" |
| Invalid selection | "Please select a valid option" |

### Checkbox / Toggle

| Error Type | Message |
|-----------|---------|
| Required (terms) | "You must agree to the Terms of Service to continue" |
| Required (consent) | "Please confirm your consent to proceed" |
| Min selections | "Please select at least {min} options" |
| Max selections | "You can select up to {max} options" |

### Textarea / Message

| Error Type | Message |
|-----------|---------|
| Required | "Message is required" |
| Too short | "Please enter at least {min} characters" |
| Too long | "{current} / {max} characters. Please shorten your message." |

### Username

| Error Type | Message |
|-----------|---------|
| Required | "Username is required" |
| Too short | "Username must be at least 3 characters" |
| Too long | "Username cannot exceed 30 characters" |
| Invalid characters | "Username can only contain letters, numbers, and underscores" |
| Starts with number | "Username must start with a letter" |
| Already taken | "This username is already taken. Try: {suggestion1}, {suggestion2}" |

### General / Cross-Field

| Error Type | Message |
|-----------|---------|
| Required (generic) | "This field is required" |
| Form not complete | "Please complete all required fields" |
| Server error | "Something went wrong. Please try again." |
| Network error | "Unable to connect. Please check your internet connection." |
| Rate limited | "Too many attempts. Please wait a moment and try again." |
| Session expired | "Your session has expired. Please refresh and try again." |
| Conflict | "This record was modified by someone else. Please review the latest version." |

---

## Warning Messages (Non-Blocking)

Warnings are not errors — they alert the user to a potential issue but do not prevent form submission.

**Visual style:** Yellow/amber instead of red. Warning icon (triangle with exclamation).

| Scenario | Warning Message |
|----------|----------------|
| Weak password | "This password is weak. Consider adding numbers and special characters." |
| Uncommon email domain | "This email domain is unusual. Please double-check." |
| High character count | "You're approaching the character limit (280 / 300)" |
| Unsaved changes | "You have unsaved changes. Save before leaving?" |
| Slow connection | "This is taking longer than usual. Please wait..." |
| Future date far out | "This date is more than a year in the future. Is that correct?" |

```css
.form-warning {
  display: flex;
  align-items: flex-start;
  gap: 6px;
  font-size: 13px;
  color: #92400E;
  margin-top: 6px;
}

.form-warning-icon {
  width: 14px;
  height: 14px;
  color: #D97706;
  flex-shrink: 0;
  margin-top: 1px;
}
```

---

## Success Validation (Green Check)

Show a green checkmark after a field passes validation to reassure the user.

**When to show:**
- After async validation passes (email available, username available)
- After complex validation passes (password meets all requirements)
- NOT after every basic field — it can feel patronizing for simple text inputs

**Visual style:** Green check icon (14px, #059669) to the right of the input or below the field.

```css
.form-success {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: #059669;
  margin-top: 6px;
}

.input-success-icon {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: #059669;
}

.form-input--success {
  border-color: #059669;
  padding-right: 40px;
}
```

---

## Async Validation Patterns

### Email / Username Availability Check

**Flow:**
1. User types and leaves field (blur) or pauses typing (debounce 500-800ms)
2. Show a loading spinner inside the input (right side)
3. Send request to server
4. On success: show green check + "Available"
5. On failure: show red error + "Already taken. Try: {suggestions}"
6. On network error: do not show error — let server validate on submit

```tsx
function useAsyncValidation(
  validateFn: (value: string) => Promise<string | null>,
  debounceMs = 600
) {
  const [status, setStatus] = useState<'idle' | 'checking' | 'valid' | 'invalid'>('idle');
  const [error, setError] = useState<string | null>(null);
  const timeoutRef = useRef<number>();

  const validate = (value: string) => {
    if (timeoutRef.current) clearTimeout(timeoutRef.current);

    if (!value) {
      setStatus('idle');
      setError(null);
      return;
    }

    setStatus('checking');
    timeoutRef.current = window.setTimeout(async () => {
      try {
        const result = await validateFn(value);
        if (result) {
          setStatus('invalid');
          setError(result);
        } else {
          setStatus('valid');
          setError(null);
        }
      } catch {
        setStatus('idle'); // Fail silently — server will catch on submit
        setError(null);
      }
    }, debounceMs);
  };

  return { status, error, validate };
}
```

```css
.input-status-icon {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
}

.input-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid #E5E7EB;
  border-top-color: #2563EB;
  border-radius: 50%;
  animation: spin 600ms linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

---

## Cross-Field Validation

### Password Confirmation

**Rule:** Confirm password must match password.
**Timing:** Validate confirm field on blur and on change (after first blur).
**Message:** "Passwords do not match"

### Date Range Validation

**Rule:** End date must be after start date.
**Timing:** Validate end date field on blur.
**Message:** "End date must be after start date"

### Conditional Required Fields

**Rule:** If "Other" is selected in a dropdown, the "Please specify" text field becomes required.
**Timing:** Validate on form submit. Also validate the conditional field on blur if the trigger is already set.

### Min/Max Total

**Rule:** Selected items must total a specific amount (e.g., percentage allocations must sum to 100%).
**Timing:** Validate on blur of any field in the group, and on submit.
**Message:** "Values must add up to 100% (currently {current}%)"

```tsx
function useCrossFieldValidation(fields: Record<string, string>, rules: CrossFieldRule[]) {
  const errors: Record<string, string> = {};

  for (const rule of rules) {
    const error = rule.validate(fields);
    if (error) {
      errors[rule.targetField] = error.message;
    }
  }

  return errors;
}
```

---

## Server-Side Error Display

When the server returns errors after form submission:

1. **Map server errors to fields:** Server response should include field names that match form field names
2. **Show inline errors** on each field, same as client-side errors
3. **Show error summary** at the top with a count
4. **Scroll to first error** and focus the first invalid field
5. **Preserve all user input** — never clear the form on server error

```tsx
async function handleSubmit(formData: FormData) {
  try {
    const response = await fetch('/api/submit', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const { errors } = await response.json();
      // errors = { email: "Already registered", phone: "Invalid format" }

      // Set field-level errors
      setFieldErrors(errors);

      // Scroll to and focus first error field
      const firstErrorField = Object.keys(errors)[0];
      const element = document.getElementById(`field-${firstErrorField}`);
      element?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      element?.focus();

      // Announce to screen readers
      // The error summary with role="alert" will be announced automatically
    }
  } catch {
    setFormError('Something went wrong. Please try again.');
  }
}
```

---

## Accessibility for Validation and Errors

### Required Field Indication

```html
<!-- Visual indicator (asterisk) + ARIA -->
<label for="email">
  Email address
  <span aria-hidden="true"> *</span>
</label>
<input id="email" name="email" type="email"
  required
  aria-required="true" />

<!-- Instruction text for screen readers -->
<p class="form-instructions" id="form-instructions">
  Fields marked with * are required
</p>
<form aria-describedby="form-instructions">
```

### Error Association

```html
<!-- aria-invalid tells screen readers the field has an error -->
<!-- aria-errormessage points to the error text (ARIA 1.3) -->
<!-- aria-describedby is the fallback for broader support -->
<input id="field-email" name="email" type="email"
  aria-invalid="true"
  aria-errormessage="error-email"
  aria-describedby="error-email" />

<p id="error-email" role="alert">
  Email must include an @ symbol
</p>
```

### Live Regions for Dynamic Errors

```html
<!-- Error messages that appear dynamically should be in a live region -->
<!-- role="alert" is equivalent to aria-live="assertive" -->
<p id="error-email" role="alert">
  Email must include an @ symbol
</p>

<!-- For non-critical updates (character count, password strength): -->
<p aria-live="polite">
  250 / 280 characters
</p>
```

### Focus Management on Submit

```tsx
function onInvalidSubmit(errors: Record<string, string>) {
  // 1. Find the first invalid field
  const firstErrorFieldName = Object.keys(errors)[0];
  const firstErrorField = document.getElementById(`field-${firstErrorFieldName}`);

  // 2. Scroll to it
  firstErrorField?.scrollIntoView({ behavior: 'smooth', block: 'center' });

  // 3. Focus it (after scroll completes)
  setTimeout(() => {
    firstErrorField?.focus();
  }, 300);
}
```

### Screen Reader Announcement Flow

1. On form submit with errors: Error summary (role="alert") is announced immediately
2. Focus moves to first invalid field
3. Screen reader reads: field label + "invalid" + error message (via aria-errormessage)
4. When user corrects the error: error disappears, "invalid" state removed
5. Optional: success message announced via aria-live="polite"

---

## Error Animation Patterns

### Subtle Shake (for Invalid Submission)

```css
.form-input--shake {
  animation: shake 400ms ease;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-6px); }
  40% { transform: translateX(6px); }
  60% { transform: translateX(-4px); }
  80% { transform: translateX(4px); }
}
```

**Accessibility note:** Respect `prefers-reduced-motion`:
```css
@media (prefers-reduced-motion: reduce) {
  .form-input--shake {
    animation: none;
    /* Use a non-motion alternative: flash border or background */
    outline: 2px solid #DC2626;
  }
}
```

### Error Message Slide-In

```css
.form-error {
  animation: errorSlideIn 200ms ease-out;
}

@keyframes errorSlideIn {
  from {
    opacity: 0;
    transform: translateY(-4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .form-error {
    animation: none;
  }
}
```

---

## Form Submission States

### Button States During Submission

| State | Button Text | Disabled | Visual |
|-------|------------|----------|--------|
| **Default** | "Submit" | No | Brand color |
| **Submitting** | "Submitting..." | Yes | Spinner + muted color |
| **Success** | "Done!" or checkmark | Yes (briefly) | Green |
| **Error** | "Try again" | No | Returns to default or red |

```tsx
function SubmitButton({ status }: { status: 'idle' | 'submitting' | 'success' | 'error' }) {
  const labels = {
    idle: 'Submit',
    submitting: 'Submitting...',
    success: 'Done!',
    error: 'Try again',
  };

  return (
    <button
      type="submit"
      disabled={status === 'submitting' || status === 'success'}
      className={`form-button-primary submit-button submit-button--${status}`}
      aria-busy={status === 'submitting'}
    >
      {status === 'submitting' && <span className="button-spinner" aria-hidden="true" />}
      {labels[status]}
    </button>
  );
}
```

```css
.submit-button--submitting {
  opacity: 0.7;
  cursor: not-allowed;
}

.submit-button--success {
  background: #059669;
}

.button-spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: #FFFFFF;
  border-radius: 50%;
  animation: spin 600ms linear infinite;
  margin-right: 8px;
  vertical-align: middle;
}
```

---

## Error Prevention Checklist

Before implementing error handling, ensure you have maximized error prevention:

- [ ] Use the correct input type (email, tel, url, number, date) for the data
- [ ] Set the correct `inputmode` for mobile keyboards
- [ ] Set `autocomplete` attributes for autofill
- [ ] Use constrained inputs where possible (date picker, select, radio)
- [ ] Auto-format inputs as user types (phone, credit card, currency)
- [ ] Show format hints before the user types ("MM/DD/YYYY", "8+ characters")
- [ ] Show character limits before they are reached
- [ ] Use `maxlength` to prevent over-typing
- [ ] Use `min`, `max`, `step` for numeric constraints
- [ ] Disable submit button while form is submitting (prevent double submit)
- [ ] Show password requirements before the user creates a password
- [ ] Suggest corrections for common typos (email domains, common names)
- [ ] Confirm destructive actions before executing
- [ ] Preserve form data on page refresh (localStorage/sessionStorage)
- [ ] Warn before navigating away with unsaved changes
