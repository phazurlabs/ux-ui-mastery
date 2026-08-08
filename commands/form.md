---
name: form
description: "Generate production forms — validation, error states, multi-step wizards, accessibility, complete React + Zod code."
argument-hint: "[form purpose and fields]"
---

# Form — Production Form Builder

## Before running

This command needs the form's purpose and its fields.

If the user invoked it with nothing and no target is evident from the conversation or open files, ask for it in one plain-language question and stop. Do not invent a target and do not produce generic output in place of the real work — output about something imaginary reads as authoritative and is worthless.

If a target is evident from context, use it and say which one you picked.


Generate complete, production-ready forms with validation, error handling, loading states, and accessibility. Output runnable React code with react-hook-form and Zod, or native HTML forms with vanilla validation.

## Generation Protocol

### Step 0: Gather Input

Before generating, collect:

1. **Form type**: Which form does the user need?
   - **Login** — Email/password, remember me, forgot password link, OAuth buttons
   - **Signup** — Name, email, password with strength meter, terms checkbox, OAuth
   - **Checkout** — Shipping address, billing, payment (card input), order summary
   - **Contact** — Name, email, subject, message textarea, optional file upload
   - **Search + Filters** — Search bar with faceted filters (checkboxes, ranges, dropdowns)
   - **Settings** — Grouped settings with toggles, selects, text inputs, save/cancel
   - **Profile Edit** — Avatar upload, personal info, bio textarea, social links
   - **Survey** — Multiple question types (single choice, multi choice, scale, free text)
   - **Booking** — Date picker, time slots, party size, special requests
   - **Multi-Step Wizard** — Multi-page form with progress indicator, back/next navigation
   - **Custom** — User describes their form requirements

2. **Tech stack**:
   - **React + react-hook-form + Zod** (default) — Production standard
   - **React + native** — useState-based, no libraries
   - **HTML + vanilla JS** — No framework
   - **React Native** — Mobile form

3. **Styling approach**:
   - **Tailwind CSS** (default)
   - **CSS Modules**
   - **Unstyled** (logic only)

4. **Prior Sumi outputs**: Check for `/tokens` (form field tokens, spacing, colors), `/layout` (container width for the form). Consume if available.

If no form type is specified, ask. Do not guess.

### Step 1: FORM SCHEMA (Zod Validation)

Define the complete validation schema before building the UI. Every field must have explicit validation rules.

**Schema generation rules**:
- Every field has a type, required/optional status, and validation message
- String fields: min/max length, pattern (regex) where applicable
- Email: valid email format
- Password: minimum 8 chars, at least one uppercase, one lowercase, one number (configurable)
- Phone: international format with regex
- URLs: valid URL format
- Numbers: min/max range
- Dates: valid date, min/max date, future/past constraints
- Files: max size, accepted types
- Cross-field validation: password confirmation, conditional required fields

**Example: Signup form schema**:
```tsx
import { z } from 'zod';

export const signupSchema = z.object({
  name: z
    .string()
    .min(1, 'Name is required')
    .min(2, 'Name must be at least 2 characters')
    .max(100, 'Name must be less than 100 characters'),
  email: z
    .string()
    .min(1, 'Email is required')
    .email('Please enter a valid email address'),
  password: z
    .string()
    .min(1, 'Password is required')
    .min(8, 'Password must be at least 8 characters')
    .regex(/[A-Z]/, 'Password must contain at least one uppercase letter')
    .regex(/[a-z]/, 'Password must contain at least one lowercase letter')
    .regex(/[0-9]/, 'Password must contain at least one number'),
  confirmPassword: z
    .string()
    .min(1, 'Please confirm your password'),
  acceptTerms: z
    .literal(true, {
      errorMap: () => ({ message: 'You must accept the terms and conditions' }),
    }),
}).refine((data) => data.password === data.confirmPassword, {
  message: 'Passwords do not match',
  path: ['confirmPassword'],
});

export type SignupFormData = z.infer<typeof signupSchema>;
```

**Example: Checkout form schema**:
```tsx
export const checkoutSchema = z.object({
  // Shipping
  shipping: z.object({
    firstName: z.string().min(1, 'First name is required'),
    lastName: z.string().min(1, 'Last name is required'),
    address: z.string().min(1, 'Address is required'),
    address2: z.string().optional(),
    city: z.string().min(1, 'City is required'),
    state: z.string().min(1, 'State is required'),
    zip: z.string().regex(/^\d{5}(-\d{4})?$/, 'Enter a valid ZIP code'),
    country: z.string().min(1, 'Country is required'),
    phone: z.string().regex(/^\+?[\d\s-()]+$/, 'Enter a valid phone number').optional(),
  }),
  // Billing
  sameAsShipping: z.boolean(),
  billing: z.object({
    firstName: z.string(),
    lastName: z.string(),
    address: z.string(),
    city: z.string(),
    state: z.string(),
    zip: z.string(),
    country: z.string(),
  }).optional(),
  // Payment
  payment: z.object({
    cardNumber: z.string().regex(/^\d{4}\s?\d{4}\s?\d{4}\s?\d{4}$/, 'Enter a valid card number'),
    expiry: z.string().regex(/^(0[1-9]|1[0-2])\/\d{2}$/, 'Enter a valid expiry (MM/YY)'),
    cvc: z.string().regex(/^\d{3,4}$/, 'Enter a valid CVC'),
    nameOnCard: z.string().min(1, 'Name on card is required'),
  }),
});
```

### Step 2: FORM COMPONENT STRUCTURE

Build the React component with react-hook-form integration.

**Component architecture**:
```tsx
'use client';

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { useState } from 'react';

export function SignupForm() {
  const [serverError, setServerError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting, isSubmitSuccessful },
    watch,
    reset,
  } = useForm<SignupFormData>({
    resolver: zodResolver(signupSchema),
    defaultValues: {
      name: '',
      email: '',
      password: '',
      confirmPassword: '',
      acceptTerms: false,
    },
  });

  const onSubmit = async (data: SignupFormData) => {
    setServerError(null);
    try {
      // API call
      const response = await fetch('/api/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || 'Something went wrong');
      }

      // Success — form will show success state via isSubmitSuccessful
    } catch (error) {
      setServerError(
        error instanceof Error ? error.message : 'An unexpected error occurred'
      );
    }
  };

  // Success state
  if (isSubmitSuccessful) {
    return (
      <div role="status" class="text-center py-12">
        <CheckCircleIcon className="mx-auto h-12 w-12 text-green-500" />
        <h2 className="mt-4 text-lg font-semibold text-gray-900">Account created!</h2>
        <p className="mt-2 text-sm text-gray-600">Check your email to verify your account.</p>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} noValidate className="space-y-6">
      {/* Server error banner */}
      {serverError && (
        <div role="alert" className="rounded-md bg-red-50 p-4 ring-1 ring-red-200">
          <p className="text-sm text-red-800">{serverError}</p>
        </div>
      )}

      {/* Form fields — see Step 3 */}

      {/* Submit button */}
      <button
        type="submit"
        disabled={isSubmitting}
        className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {isSubmitting ? (
          <>
            <Spinner className="mr-2 h-4 w-4 animate-spin" />
            Creating account...
          </>
        ) : (
          'Create account'
        )}
      </button>
    </form>
  );
}
```

### Step 3: INPUT FIELD COMPONENTS

Every input field must include: label, input, description (optional), error message, and proper accessibility attributes.

**Text input field pattern**:
```tsx
{/* Field: Name */}
<div>
  <label htmlFor="name" className="block text-sm font-medium text-gray-900">
    Name <span className="text-red-500" aria-hidden="true">*</span>
  </label>
  <input
    id="name"
    type="text"
    autoComplete="name"
    aria-required="true"
    aria-invalid={!!errors.name}
    aria-describedby={errors.name ? 'name-error' : undefined}
    className={`mt-1.5 block w-full rounded-md border-0 px-3 py-2 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm ${
      errors.name
        ? 'ring-red-300 focus:ring-red-500'
        : 'ring-gray-300'
    }`}
    placeholder="John Doe"
    {...register('name')}
  />
  {errors.name && (
    <p id="name-error" role="alert" className="mt-1.5 text-sm text-red-600">
      {errors.name.message}
    </p>
  )}
</div>
```

**Email field pattern**:
```tsx
<div>
  <label htmlFor="email" className="block text-sm font-medium text-gray-900">
    Email address <span className="text-red-500" aria-hidden="true">*</span>
  </label>
  <input
    id="email"
    type="email"
    autoComplete="email"
    inputMode="email"
    aria-required="true"
    aria-invalid={!!errors.email}
    aria-describedby={errors.email ? 'email-error' : 'email-hint'}
    className={`mt-1.5 block w-full rounded-md border-0 px-3 py-2 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm ${
      errors.email ? 'ring-red-300 focus:ring-red-500' : 'ring-gray-300'
    }`}
    placeholder="john@example.com"
    {...register('email')}
  />
  {errors.email ? (
    <p id="email-error" role="alert" className="mt-1.5 text-sm text-red-600">
      {errors.email.message}
    </p>
  ) : (
    <p id="email-hint" className="mt-1.5 text-sm text-gray-500">
      We'll send a verification link to this address.
    </p>
  )}
</div>
```

**Password field pattern** (with visibility toggle and strength meter):
```tsx
<div>
  <label htmlFor="password" className="block text-sm font-medium text-gray-900">
    Password <span className="text-red-500" aria-hidden="true">*</span>
  </label>
  <div className="relative mt-1.5">
    <input
      id="password"
      type={showPassword ? 'text' : 'password'}
      autoComplete="new-password"
      aria-required="true"
      aria-invalid={!!errors.password}
      aria-describedby={
        [errors.password && 'password-error', 'password-requirements']
          .filter(Boolean)
          .join(' ')
      }
      className={`block w-full rounded-md border-0 px-3 py-2 pr-10 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm ${
        errors.password ? 'ring-red-300 focus:ring-red-500' : 'ring-gray-300'
      }`}
      {...register('password')}
    />
    <button
      type="button"
      onClick={() => setShowPassword(!showPassword)}
      className="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-600"
      aria-label={showPassword ? 'Hide password' : 'Show password'}
    >
      {showPassword ? <EyeSlashIcon className="h-5 w-5" /> : <EyeIcon className="h-5 w-5" />}
    </button>
  </div>
  {/* Password strength meter */}
  <PasswordStrengthMeter password={watch('password')} />
  {errors.password && (
    <p id="password-error" role="alert" className="mt-1.5 text-sm text-red-600">
      {errors.password.message}
    </p>
  )}
  <p id="password-requirements" className="mt-1.5 text-sm text-gray-500">
    At least 8 characters with uppercase, lowercase, and a number.
  </p>
</div>
```

**Select field pattern**:
```tsx
<div>
  <label htmlFor="country" className="block text-sm font-medium text-gray-900">
    Country <span className="text-red-500" aria-hidden="true">*</span>
  </label>
  <select
    id="country"
    autoComplete="country-name"
    aria-required="true"
    aria-invalid={!!errors.shipping?.country}
    aria-describedby={errors.shipping?.country ? 'country-error' : undefined}
    className={`mt-1.5 block w-full rounded-md border-0 px-3 py-2 text-gray-900 shadow-sm ring-1 ring-inset focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm ${
      errors.shipping?.country ? 'ring-red-300 focus:ring-red-500' : 'ring-gray-300'
    }`}
    {...register('shipping.country')}
  >
    <option value="">Select a country</option>
    <option value="US">United States</option>
    <option value="CA">Canada</option>
    <option value="GB">United Kingdom</option>
    {/* ... */}
  </select>
  {errors.shipping?.country && (
    <p id="country-error" role="alert" className="mt-1.5 text-sm text-red-600">
      {errors.shipping.country.message}
    </p>
  )}
</div>
```

**Checkbox field pattern**:
```tsx
<div className="flex items-start gap-3">
  <input
    id="acceptTerms"
    type="checkbox"
    aria-required="true"
    aria-invalid={!!errors.acceptTerms}
    aria-describedby={errors.acceptTerms ? 'terms-error' : undefined}
    className="mt-1 h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600"
    {...register('acceptTerms')}
  />
  <div>
    <label htmlFor="acceptTerms" className="text-sm text-gray-900">
      I agree to the{' '}
      <a href="/terms" className="font-medium text-indigo-600 hover:text-indigo-500">
        Terms of Service
      </a>{' '}
      and{' '}
      <a href="/privacy" className="font-medium text-indigo-600 hover:text-indigo-500">
        Privacy Policy
      </a>
    </label>
    {errors.acceptTerms && (
      <p id="terms-error" role="alert" className="mt-1 text-sm text-red-600">
        {errors.acceptTerms.message}
      </p>
    )}
  </div>
</div>
```

**Textarea pattern**:
```tsx
<div>
  <label htmlFor="message" className="block text-sm font-medium text-gray-900">
    Message <span className="text-red-500" aria-hidden="true">*</span>
  </label>
  <textarea
    id="message"
    rows={4}
    aria-required="true"
    aria-invalid={!!errors.message}
    aria-describedby={
      [errors.message && 'message-error', 'message-count']
        .filter(Boolean)
        .join(' ')
    }
    className={`mt-1.5 block w-full rounded-md border-0 px-3 py-2 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm ${
      errors.message ? 'ring-red-300 focus:ring-red-500' : 'ring-gray-300'
    }`}
    placeholder="How can we help?"
    {...register('message')}
  />
  <div className="mt-1.5 flex justify-between">
    {errors.message ? (
      <p id="message-error" role="alert" className="text-sm text-red-600">
        {errors.message.message}
      </p>
    ) : (
      <span />
    )}
    <p id="message-count" className="text-sm text-gray-500">
      {watch('message')?.length || 0}/500
    </p>
  </div>
</div>
```

**Mobile input modes** — always set these for mobile keyboard optimization:

| Input Type | `type` | `inputMode` | `autoComplete` |
|-----------|--------|-------------|----------------|
| Name | text | text | name |
| Email | email | email | email |
| Phone | tel | tel | tel |
| URL | url | url | url |
| ZIP Code | text | numeric | postal-code |
| Credit Card | text | numeric | cc-number |
| CVC | text | numeric | cc-csc |
| Expiry | text | numeric | cc-exp |
| Street Address | text | text | street-address |
| City | text | text | address-level2 |
| State | text | text | address-level1 |
| Search | search | search | off |
| Quantity | number | numeric | off |
| Price | text | decimal | off |
| One-Time Code | text | numeric | one-time-code |

### Step 4: MULTI-STEP WIZARD LOGIC

For wizard-type forms, implement step management with validation per step.

**Multi-step wizard architecture**:
```tsx
'use client';

import { useState } from 'react';
import { useForm, FormProvider } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';

const STEPS = [
  { id: 'personal', title: 'Personal Info', schema: personalSchema },
  { id: 'address', title: 'Address', schema: addressSchema },
  { id: 'payment', title: 'Payment', schema: paymentSchema },
  { id: 'review', title: 'Review', schema: z.object({}) },
] as const;

export function CheckoutWizard() {
  const [currentStep, setCurrentStep] = useState(0);

  const methods = useForm<CheckoutFormData>({
    resolver: zodResolver(checkoutSchema),
    mode: 'onTouched',
    defaultValues: { /* ... */ },
  });

  const { trigger, handleSubmit, getValues } = methods;

  // Validate current step before advancing
  const goToNext = async () => {
    const stepFields = getFieldsForStep(currentStep);
    const isValid = await trigger(stepFields);
    if (isValid) {
      setCurrentStep((prev) => Math.min(prev + 1, STEPS.length - 1));
    }
  };

  const goToPrevious = () => {
    setCurrentStep((prev) => Math.max(prev - 1, 0));
  };

  const onSubmit = async (data: CheckoutFormData) => {
    // Final submission
  };

  return (
    <FormProvider {...methods}>
      {/* Progress indicator */}
      <nav aria-label="Form progress" className="mb-8">
        <ol className="flex items-center" role="list">
          {STEPS.map((step, index) => (
            <li key={step.id} className="flex items-center">
              <span
                className={`flex h-8 w-8 items-center justify-center rounded-full text-sm font-medium ${
                  index < currentStep
                    ? 'bg-indigo-600 text-white'        // Completed
                    : index === currentStep
                    ? 'border-2 border-indigo-600 text-indigo-600'  // Current
                    : 'border-2 border-gray-300 text-gray-500'     // Upcoming
                }`}
                aria-current={index === currentStep ? 'step' : undefined}
              >
                {index < currentStep ? (
                  <CheckIcon className="h-5 w-5" aria-hidden="true" />
                ) : (
                  index + 1
                )}
              </span>
              <span className="ml-2 text-sm font-medium text-gray-900 hidden sm:inline">
                {step.title}
              </span>
              {index < STEPS.length - 1 && (
                <div className="mx-3 h-0.5 w-8 sm:w-16 bg-gray-300" aria-hidden="true">
                  <div
                    className="h-full bg-indigo-600 transition-all"
                    style={{ width: index < currentStep ? '100%' : '0%' }}
                  />
                </div>
              )}
            </li>
          ))}
        </ol>
      </nav>

      <form onSubmit={handleSubmit(onSubmit)}>
        {/* Step content — render only current step */}
        <div role="group" aria-label={`Step ${currentStep + 1}: ${STEPS[currentStep].title}`}>
          {currentStep === 0 && <PersonalInfoStep />}
          {currentStep === 1 && <AddressStep />}
          {currentStep === 2 && <PaymentStep />}
          {currentStep === 3 && <ReviewStep data={getValues()} />}
        </div>

        {/* Navigation buttons */}
        <div className="mt-8 flex justify-between">
          <button
            type="button"
            onClick={goToPrevious}
            disabled={currentStep === 0}
            className="rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Back
          </button>

          {currentStep < STEPS.length - 1 ? (
            <button
              type="button"
              onClick={goToNext}
              className="rounded-md bg-indigo-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            >
              Continue
            </button>
          ) : (
            <button
              type="submit"
              disabled={methods.formState.isSubmitting}
              className="rounded-md bg-indigo-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:opacity-50"
            >
              {methods.formState.isSubmitting ? 'Submitting...' : 'Place Order'}
            </button>
          )}
        </div>
      </form>
    </FormProvider>
  );
}
```

### Step 5: LOADING, SUBMITTING, AND STATE MANAGEMENT

Every form must handle these states explicitly:

**State machine for forms**:
```
IDLE → VALIDATING → SUBMITTING → SUCCESS
                  ↘ VALIDATION_ERROR (return to IDLE with errors shown)
        SUBMITTING → SERVER_ERROR (return to IDLE with server error banner)
```

**Submitting state** (disable form, show spinner):
```tsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? (
    <span className="flex items-center gap-2">
      <svg className="h-4 w-4 animate-spin" viewBox="0 0 24 24" fill="none">
        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
      </svg>
      Submitting...
    </span>
  ) : (
    'Submit'
  )}
</button>
```

**Field-level loading** (async validation, e.g., username availability):
```tsx
const [checkingUsername, setCheckingUsername] = useState(false);

// Debounced async check
useEffect(() => {
  const username = watch('username');
  if (!username || username.length < 3) return;

  const timeout = setTimeout(async () => {
    setCheckingUsername(true);
    const available = await checkUsernameAvailability(username);
    if (!available) {
      setError('username', { message: 'Username is already taken' });
    }
    setCheckingUsername(false);
  }, 500);

  return () => clearTimeout(timeout);
}, [watch('username')]);
```

**Success state** (confirmation):
```tsx
if (isSubmitSuccessful) {
  return (
    <div role="status" className="rounded-lg border border-green-200 bg-green-50 p-8 text-center">
      <svg className="mx-auto h-12 w-12 text-green-500" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor">
        <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      <h3 className="mt-4 text-lg font-semibold text-gray-900">Message sent!</h3>
      <p className="mt-2 text-sm text-gray-600">We'll get back to you within 24 hours.</p>
      <button
        type="button"
        onClick={() => reset()}
        className="mt-6 text-sm font-medium text-indigo-600 hover:text-indigo-500"
      >
        Send another message
      </button>
    </div>
  );
}
```

**Server error state** (banner at top of form):
```tsx
{serverError && (
  <div role="alert" className="rounded-md bg-red-50 p-4 ring-1 ring-inset ring-red-200">
    <div className="flex">
      <ExclamationTriangleIcon className="h-5 w-5 text-red-400 flex-shrink-0" />
      <div className="ml-3">
        <h3 className="text-sm font-medium text-red-800">Submission failed</h3>
        <p className="mt-1 text-sm text-red-700">{serverError}</p>
      </div>
    </div>
  </div>
)}
```

### Step 6: ACCESSIBILITY REQUIREMENTS

Every form must meet WCAG 2.2 AA. These are non-negotiable:

**Labels and descriptions**:
- Every input MUST have a visible `<label>` with matching `htmlFor`/`id`
- Required fields: indicate with `aria-required="true"` and visible indicator (asterisk with `aria-hidden="true"`)
- Helper text: connect via `aria-describedby`
- Error messages: connect via `aria-describedby` and use `role="alert"` or `aria-live="polite"`

**Error handling**:
- `aria-invalid="true"` on fields with errors
- Error messages associated via `aria-describedby`
- Focus the first error field on submit if validation fails:
  ```tsx
  const onError = () => {
    const firstError = document.querySelector('[aria-invalid="true"]');
    if (firstError instanceof HTMLElement) {
      firstError.focus();
      firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  };

  <form onSubmit={handleSubmit(onSubmit, onError)}>
  ```

**Keyboard navigation**:
- Tab order follows visual order (no `tabIndex` hacks)
- Enter submits the form (default behavior, do not prevent)
- Escape closes any open dropdowns or modals
- Multi-step wizard: focus moves to first field of new step on advance

**Screen reader announcements**:
- Form submission success: `role="status"` on success message
- Form submission error: `role="alert"` on error banner
- Step changes in wizard: announce new step title via `aria-live` region
- Character count updates: `aria-live="polite"` on counter

**Touch targets**:
- All interactive elements: minimum 44x44px touch target (WCAG 2.2 Target Size)
- Checkboxes and radio buttons: at least 24x24px visual, 44x44px hit area
- Spacing between touch targets: at least 8px gap

**Color independence**:
- Errors: red ring + icon + text message (never color alone)
- Required: asterisk + aria-required (never color alone)
- Success: green + icon + text (never color alone)

### Step 7: PASSWORD STRENGTH METER (for signup/password forms)

```tsx
function PasswordStrengthMeter({ password }: { password: string }) {
  const strength = getPasswordStrength(password);

  return (
    <div className="mt-2" aria-live="polite">
      {/* Visual meter */}
      <div className="flex gap-1" aria-hidden="true">
        {[1, 2, 3, 4].map((level) => (
          <div
            key={level}
            className={`h-1.5 flex-1 rounded-full transition-colors ${
              level <= strength.level
                ? strength.level <= 1 ? 'bg-red-500'
                : strength.level === 2 ? 'bg-orange-500'
                : strength.level === 3 ? 'bg-yellow-500'
                : 'bg-green-500'
                : 'bg-gray-200'
            }`}
          />
        ))}
      </div>
      {/* Text label for accessibility */}
      <p className="mt-1 text-xs text-gray-500">
        Password strength: <span className="font-medium">{strength.label}</span>
      </p>
    </div>
  );
}

function getPasswordStrength(password: string) {
  if (!password) return { level: 0, label: '' };
  let score = 0;
  if (password.length >= 8) score++;
  if (password.length >= 12) score++;
  if (/[A-Z]/.test(password) && /[a-z]/.test(password)) score++;
  if (/[0-9]/.test(password)) score++;
  if (/[^A-Za-z0-9]/.test(password)) score++;

  if (score <= 1) return { level: 1, label: 'Weak' };
  if (score <= 2) return { level: 2, label: 'Fair' };
  if (score <= 3) return { level: 3, label: 'Good' };
  return { level: 4, label: 'Strong' };
}
```

### Step 8: COMPLETE FORM ASSEMBLY

Combine all steps into a single, complete, copy-paste-ready file.

**File structure for output**:
```
// 1. Schema definition (Zod)
// 2. Type inference
// 3. Helper components (PasswordStrengthMeter, etc.)
// 4. Main form component
//    - State setup (useForm, server error state)
//    - Submit handler (with try/catch)
//    - Success state render
//    - Form render with all fields
//    - Loading/submitting state on button
// 5. Export
```

**Every generated form must be a single file that can be copy-pasted and run** (assuming react-hook-form, zod, and @hookform/resolvers are installed).

## Output Format

```
## Form: [Form Type]

### Dependencies
```bash
npm install react-hook-form @hookform/resolvers zod
```

### Schema
[Complete Zod schema with all validations and types]

### Component
[Complete React component — single file, runnable]

### Input Modes Reference
| Field | type | inputMode | autoComplete |
|-------|------|-----------|-------------|
| [each field] | [...] | [...] | [...] |

### States Handled
- [ ] Idle (default)
- [ ] Validating (inline, per field on blur/change)
- [ ] Submitting (spinner, disabled form)
- [ ] Validation error (field-level errors, focus first error)
- [ ] Server error (banner at top)
- [ ] Success (confirmation message)

### Accessibility Checklist
- [ ] All fields have visible labels with htmlFor/id pairing
- [ ] Required fields use aria-required and visible indicator
- [ ] Errors use aria-invalid, aria-describedby, role="alert"
- [ ] Focus moves to first error on failed submit
- [ ] Form success announced via role="status"
- [ ] Touch targets meet 44x44px minimum
- [ ] Color is never the sole indicator of state
```

## Quality Gates

The output MUST include:
- [ ] Complete Zod validation schema with meaningful error messages
- [ ] Full React component with react-hook-form integration
- [ ] All form states handled (idle, validating, submitting, success, error)
- [ ] Server error handling (try/catch with error banner)
- [ ] Mobile input modes (inputMode, autoComplete) on all fields
- [ ] Accessibility: labels, aria-invalid, aria-describedby, focus management
- [ ] Loading/submitting state on submit button
- [ ] Single-file, copy-paste-ready code

The output MUST NOT include:
- Forms with no validation
- Missing error messages (validation errors without user-facing text)
- Submit buttons with no loading state
- Inputs without labels (placeholder-only is not accessible)
- Missing autoComplete attributes (breaks mobile autofill)
- Wizard forms without per-step validation

## Cross-References

When generating forms, draw knowledge from:
- `form-design-encyclopedia` skill — 200+ form patterns, input types, validation strategies
- `component-patterns-code` skill — React component patterns with code
- `accessibility-inclusive-design` skill — WCAG form requirements, error handling, focus management
- `performance-states-patterns` skill — loading, error, success, and empty states
- `micro-copy-intelligence` skill — error messages, labels, placeholder text, button labels
- `interaction-motion-design` skill — form transition animations, validation feedback timing
- `cognitive-psychology-ux` skill — cognitive load in forms, chunking, progressive disclosure

## Next Step

**Next** -> `/animate` — Add micro-interactions to form fields (focus, validation, submit)

**Alternatives**:
- `/layout` — Build the page layout that contains this form
- `/nav` — Add navigation around the form page
- `/a11y` — Run a full accessibility audit on the form
- `/sumi` — See the full journey map
