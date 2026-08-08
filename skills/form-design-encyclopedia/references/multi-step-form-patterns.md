# Multi-Step Form Patterns — Wizards, Steppers, Checkout Flows, and Full Component Code

## How to Use This Reference

This file covers everything about multi-step forms: when to use them, step indicator patterns, navigation patterns, data persistence, validation strategies, conditional steps, and full production React/TypeScript component code. When building any form that spans multiple pages or sections, use this as your implementation guide.

---

## When to Use Multi-Step vs. Single Page

### Use Multi-Step When:
- The form has 7+ fields that can be grouped into 2-4 distinct steps
- The fields have a natural sequential order (personal info → address → payment)
- Some steps are conditional (skip payment step if using free plan)
- The form requires focus on one group at a time (reducing cognitive load)
- You need to validate data at intermediate points before proceeding
- The form represents a process with distinct phases (application, onboarding, checkout)

### Use Single Page When:
- The form has fewer than 7 fields
- All fields are related to a single topic
- Users need to see all fields at once for context
- Users frequently revisit and edit fields in different sections
- The form is primarily for data entry by experienced users

### Completion Rate Impact
- Single-page forms with many fields: completion drops significantly after 6-8 visible fields
- Multi-step forms: each step loses 10-20% of users, BUT the initial perceived simplicity brings more users into step 1
- Net effect: multi-step often wins for 7+ field forms because the lower per-step drop-off rate outweighs the multi-step friction
- Exception: do not add unnecessary steps just to make each step shorter — extra clicks add friction too

---

## Step Indicator Patterns

### 1. Numbered Steps (Horizontal)

The most common pattern. Shows step numbers, titles, and current position.

**Specifications:**
- Step circles: 32px diameter, border-radius 50%
- Numbers: 14px font-weight 600
- Connector lines: 2px height, connects circles
- States: inactive (gray), active (brand color, filled), completed (brand color, checkmark)
- Step titles: 13px below circles, optional on mobile
- Max steps displayed: 5-7 on desktop, 3-5 on mobile (collapse to current step + count on very small screens)

```tsx
interface Step {
  title: string;
  isComplete: boolean;
  isActive: boolean;
}

function StepIndicator({ steps, currentStep }: { steps: Step[]; currentStep: number }) {
  return (
    <nav className="step-indicator" aria-label="Form progress">
      <ol className="step-list">
        {steps.map((step, index) => (
          <li
            key={index}
            className={`step-item ${step.isActive ? 'step-item--active' : ''} ${step.isComplete ? 'step-item--complete' : ''}`}
            aria-current={step.isActive ? 'step' : undefined}
          >
            <div className="step-circle">
              {step.isComplete ? (
                <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
                  <path d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z" />
                </svg>
              ) : (
                <span>{index + 1}</span>
              )}
            </div>
            <span className="step-title">{step.title}</span>
            {index < steps.length - 1 && <div className="step-connector" />}
          </li>
        ))}
      </ol>
      <p className="sr-only">Step {currentStep + 1} of {steps.length}: {steps[currentStep].title}</p>
    </nav>
  );
}
```

```css
.step-indicator {
  margin-bottom: 40px;
}

.step-list {
  display: flex;
  align-items: flex-start;
  list-style: none;
  padding: 0;
  margin: 0;
}

.step-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  flex: 1;
}

.step-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
  background: #F3F4F6;
  color: #6B7280;
  border: 2px solid #E5E7EB;
  position: relative;
  z-index: 1;
}

.step-item--active .step-circle {
  background: #2563EB;
  color: #FFFFFF;
  border-color: #2563EB;
}

.step-item--complete .step-circle {
  background: #2563EB;
  color: #FFFFFF;
  border-color: #2563EB;
}

.step-title {
  font-size: 13px;
  color: #6B7280;
  margin-top: 8px;
  text-align: center;
  white-space: nowrap;
}

.step-item--active .step-title {
  color: #111827;
  font-weight: 500;
}

.step-connector {
  position: absolute;
  top: 16px;
  left: calc(50% + 20px);
  right: calc(-50% + 20px);
  height: 2px;
  background: #E5E7EB;
}

.step-item--complete .step-connector {
  background: #2563EB;
}

@media (max-width: 600px) {
  .step-title {
    display: none;
  }

  .step-circle {
    width: 28px;
    height: 28px;
    font-size: 12px;
  }
}
```

---

### 2. Progress Bar

**When to use:** When the exact number of steps is less important than the overall progress. Surveys, onboarding flows.

**Specifications:**
- Bar height: 4-8px, full width, border-radius 4px
- Filled portion: brand color, transition width 300ms ease
- Text above or below: "Step 2 of 5" or "40% complete"

```tsx
function ProgressBar({ current, total }: { current: number; total: number }) {
  const percentage = Math.round((current / total) * 100);

  return (
    <div className="progress-container">
      <div className="progress-label">
        <span>Step {current} of {total}</span>
        <span>{percentage}%</span>
      </div>
      <div className="progress-track" role="progressbar"
        aria-valuenow={current} aria-valuemin={1} aria-valuemax={total}
        aria-label={`Step ${current} of ${total}`}>
        <div className="progress-fill" style={{ width: `${percentage}%` }} />
      </div>
    </div>
  );
}
```

```css
.progress-container {
  margin-bottom: 32px;
}

.progress-label {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  color: #6B7280;
  margin-bottom: 8px;
}

.progress-track {
  height: 6px;
  background: #E5E7EB;
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: #2563EB;
  border-radius: 3px;
  transition: width 300ms ease;
}
```

---

### 3. Breadcrumb Steps

**When to use:** When users should be able to jump back to any previous step. Non-linear flows.

**Specifications:**
- Steps displayed as a breadcrumb trail: "Step 1 > Step 2 > Step 3"
- Completed steps are clickable links
- Current step is bold, not a link
- Future steps are grayed out, not clickable

```tsx
function BreadcrumbSteps({ steps, currentStep, onStepClick }: BreadcrumbStepsProps) {
  return (
    <nav className="breadcrumb-steps" aria-label="Form steps">
      <ol className="breadcrumb-list">
        {steps.map((step, index) => (
          <li key={index} className="breadcrumb-item">
            {index < currentStep ? (
              <button type="button" className="breadcrumb-link"
                onClick={() => onStepClick(index)}>
                {step.title}
              </button>
            ) : index === currentStep ? (
              <span className="breadcrumb-current" aria-current="step">{step.title}</span>
            ) : (
              <span className="breadcrumb-future">{step.title}</span>
            )}
            {index < steps.length - 1 && (
              <svg className="breadcrumb-separator" width="16" height="16" viewBox="0 0 16 16"
                fill="currentColor" aria-hidden="true">
                <path d="M6.22 4.22a.75.75 0 011.06 0l3.25 3.25a.75.75 0 010 1.06l-3.25 3.25a.75.75 0 01-1.06-1.06L8.94 8 6.22 5.28a.75.75 0 010-1.06z" />
              </svg>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}
```

```css
.breadcrumb-list {
  display: flex;
  align-items: center;
  list-style: none;
  padding: 0;
  margin: 0 0 32px;
  flex-wrap: wrap;
  gap: 4px;
}

.breadcrumb-item {
  display: flex;
  align-items: center;
  gap: 4px;
}

.breadcrumb-link {
  font-size: 14px;
  color: #2563EB;
  background: none;
  border: none;
  cursor: pointer;
  text-decoration: underline;
  padding: 0;
}

.breadcrumb-current {
  font-size: 14px;
  font-weight: 600;
  color: #111827;
}

.breadcrumb-future {
  font-size: 14px;
  color: #9CA3AF;
}

.breadcrumb-separator {
  color: #D1D5DB;
}
```

---

### 4. Vertical Stepper

**When to use:** When there is space on the left side. When step content is visible inline (expand/collapse). Common in onboarding and application forms.

**Specifications:**
- Steps listed vertically on the left
- Circle + connector line (vertical)
- Content area appears to the right of or below each step
- Active step content is visible; other steps show title only or a summary

```css
.vertical-stepper {
  display: flex;
  flex-direction: column;
  gap: 0;
  max-width: 640px;
}

.vertical-step {
  display: flex;
  gap: 16px;
}

.vertical-step-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-shrink: 0;
}

.vertical-step-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
  background: #F3F4F6;
  color: #6B7280;
  border: 2px solid #E5E7EB;
}

.vertical-step--active .vertical-step-circle {
  background: #2563EB;
  color: #FFFFFF;
  border-color: #2563EB;
}

.vertical-step-line {
  width: 2px;
  flex: 1;
  background: #E5E7EB;
  min-height: 24px;
}

.vertical-step--complete .vertical-step-line {
  background: #2563EB;
}

.vertical-step-content {
  padding-bottom: 32px;
  flex: 1;
}

.vertical-step-title {
  font-size: 16px;
  font-weight: 500;
  color: #111827;
  margin: 4px 0 16px;
}
```

---

## Step Navigation Patterns

### Next / Back Buttons

**Specifications:**
- "Back" button: secondary style, left side
- "Next" or "Continue" button: primary style, right side
- "Submit" or "Complete" on the final step: primary style, may change color/label
- Button bar: display flex, justify-content space-between, margin-top 32px
- On first step: no "Back" button (or disabled)

```tsx
interface StepNavigationProps {
  currentStep: number;
  totalSteps: number;
  isLastStep: boolean;
  isFirstStep: boolean;
  onBack: () => void;
  onNext: () => void;
  isSubmitting?: boolean;
}

function StepNavigation({
  currentStep, totalSteps, isLastStep, isFirstStep, onBack, onNext, isSubmitting
}: StepNavigationProps) {
  return (
    <div className="step-navigation">
      {!isFirstStep ? (
        <button type="button" className="form-button-secondary" onClick={onBack}>
          Back
        </button>
      ) : (
        <div /> /* Spacer to keep "Next" on the right */
      )}
      <button
        type={isLastStep ? 'submit' : 'button'}
        className="form-button-primary"
        onClick={isLastStep ? undefined : onNext}
        disabled={isSubmitting}
        aria-busy={isSubmitting}
      >
        {isSubmitting ? 'Submitting...' : isLastStep ? 'Submit' : 'Continue'}
      </button>
    </div>
  );
}
```

```css
.step-navigation {
  display: flex;
  justify-content: space-between;
  margin-top: 32px;
  padding-top: 24px;
  border-top: 1px solid #E5E7EB;
}
```

### Skip Step

**When to use:** Optional steps in a flow (e.g., "Add a photo" during onboarding).
**Pattern:** "Skip this step" text link below or beside the "Next" button.
**Accessibility:** Link must be keyboard-accessible and clearly labeled.

```css
.step-skip {
  font-size: 14px;
  color: #6B7280;
  background: none;
  border: none;
  cursor: pointer;
  margin-top: 12px;
  text-align: center;
}

.step-skip:hover {
  color: #111827;
  text-decoration: underline;
}
```

### Save Draft

**When to use:** Long forms where users may not complete in one session (applications, surveys, complex configurations).
**Pattern:** "Save and continue later" link. Saves current state to server or localStorage.
**UX:** Show a toast/notification confirming the save. On return, restore the user to the step they left.

---

## Data Persistence Across Steps

### Option 1: React State (In-Memory)

Simplest approach. Data lives in a parent component's state. Lost on page refresh.

```tsx
interface FormData {
  // Step 1
  name: string;
  email: string;
  // Step 2
  street: string;
  city: string;
  state: string;
  zip: string;
  // Step 3
  cardNumber: string;
  cardExpiry: string;
  cardCvc: string;
}

function MultiStepForm() {
  const [currentStep, setCurrentStep] = useState(0);
  const [formData, setFormData] = useState<FormData>({
    name: '', email: '',
    street: '', city: '', state: '', zip: '',
    cardNumber: '', cardExpiry: '', cardCvc: '',
  });

  const updateFields = (fields: Partial<FormData>) => {
    setFormData(prev => ({ ...prev, ...fields }));
  };

  const steps = [
    <PersonalInfoStep data={formData} updateFields={updateFields} />,
    <AddressStep data={formData} updateFields={updateFields} />,
    <PaymentStep data={formData} updateFields={updateFields} />,
    <ReviewStep data={formData} />,
  ];

  const handleNext = () => {
    // Validate current step before advancing
    if (validateStep(currentStep, formData)) {
      setCurrentStep(prev => Math.min(prev + 1, steps.length - 1));
    }
  };

  const handleBack = () => {
    setCurrentStep(prev => Math.max(prev - 1, 0));
  };

  return (
    <form onSubmit={handleSubmit} noValidate>
      <StepIndicator steps={stepConfig} currentStep={currentStep} />
      {steps[currentStep]}
      <StepNavigation
        currentStep={currentStep}
        totalSteps={steps.length}
        isFirstStep={currentStep === 0}
        isLastStep={currentStep === steps.length - 1}
        onBack={handleBack}
        onNext={handleNext}
      />
    </form>
  );
}
```

### Option 2: localStorage Persistence

Survives page refresh. Good for long forms.

```tsx
function usePersistedFormData<T>(key: string, initialData: T) {
  const [data, setData] = useState<T>(() => {
    try {
      const saved = localStorage.getItem(key);
      return saved ? JSON.parse(saved) : initialData;
    } catch {
      return initialData;
    }
  });

  const updateData = (fields: Partial<T>) => {
    setData(prev => {
      const updated = { ...prev, ...fields };
      // Debounce localStorage writes in production
      localStorage.setItem(key, JSON.stringify(updated));
      return updated;
    });
  };

  const clearData = () => {
    localStorage.removeItem(key);
    setData(initialData);
  };

  return { data, updateData, clearData };
}
```

### Option 3: Server-Side Persistence (Save Draft)

For forms where data must survive across devices or sessions (applications, insurance forms).

```tsx
async function saveDraft(formId: string, stepIndex: number, data: Partial<FormData>) {
  await fetch('/api/drafts', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ formId, stepIndex, data, updatedAt: new Date().toISOString() }),
  });
}

async function loadDraft(formId: string): Promise<{ stepIndex: number; data: Partial<FormData> } | null> {
  const response = await fetch(`/api/drafts/${formId}`);
  if (!response.ok) return null;
  return response.json();
}
```

---

## Step Validation Strategies

### Strategy 1: Validate Per Step (Recommended)

Validate all fields in the current step before allowing advancement. Prevents users from reaching later steps with invalid earlier data.

```tsx
function validateStep(step: number, data: FormData): Record<string, string> {
  const errors: Record<string, string> = {};

  if (step === 0) {
    if (!data.name.trim()) errors.name = 'Name is required';
    if (!data.email.trim()) errors.email = 'Email is required';
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
      errors.email = 'Please enter a valid email';
    }
  }

  if (step === 1) {
    if (!data.street.trim()) errors.street = 'Street address is required';
    if (!data.city.trim()) errors.city = 'City is required';
    if (!data.state) errors.state = 'Please select a state';
    if (!data.zip.trim()) errors.zip = 'ZIP code is required';
    else if (!/^\d{5}(-\d{4})?$/.test(data.zip)) {
      errors.zip = 'Please enter a valid ZIP code';
    }
  }

  if (step === 2) {
    if (!data.cardNumber.trim()) errors.cardNumber = 'Card number is required';
    if (!data.cardExpiry.trim()) errors.cardExpiry = 'Expiry date is required';
    if (!data.cardCvc.trim()) errors.cardCvc = 'Security code is required';
  }

  return errors;
}
```

### Strategy 2: Validate All at End

All steps are optional until the final submission. Show errors on the review step.

**When to use:** Surveys where users may want to skip around. Forms where any step can be visited in any order.

### Strategy 3: Progressive Validation

Validate on blur within each step (hybrid pattern). Block step advancement only if the step has required fields that are empty.

---

## Review Step Before Submission

The review step shows a summary of all entered data with "Edit" links for each section.

```tsx
function ReviewStep({ data, onEditStep }: { data: FormData; onEditStep: (step: number) => void }) {
  return (
    <div className="review-step">
      <h2 className="review-title">Review your information</h2>

      <section className="review-section">
        <div className="review-section-header">
          <h3 className="review-section-title">Personal Information</h3>
          <button type="button" className="review-edit" onClick={() => onEditStep(0)}>
            Edit
          </button>
        </div>
        <dl className="review-fields">
          <div className="review-field">
            <dt className="review-label">Name</dt>
            <dd className="review-value">{data.name}</dd>
          </div>
          <div className="review-field">
            <dt className="review-label">Email</dt>
            <dd className="review-value">{data.email}</dd>
          </div>
        </dl>
      </section>

      <section className="review-section">
        <div className="review-section-header">
          <h3 className="review-section-title">Shipping Address</h3>
          <button type="button" className="review-edit" onClick={() => onEditStep(1)}>
            Edit
          </button>
        </div>
        <dl className="review-fields">
          <div className="review-field">
            <dt className="review-label">Address</dt>
            <dd className="review-value">
              {data.street}<br />
              {data.city}, {data.state} {data.zip}
            </dd>
          </div>
        </dl>
      </section>

      <section className="review-section">
        <div className="review-section-header">
          <h3 className="review-section-title">Payment</h3>
          <button type="button" className="review-edit" onClick={() => onEditStep(2)}>
            Edit
          </button>
        </div>
        <dl className="review-fields">
          <div className="review-field">
            <dt className="review-label">Card</dt>
            <dd className="review-value">
              **** **** **** {data.cardNumber.slice(-4)}
            </dd>
          </div>
        </dl>
      </section>
    </div>
  );
}
```

```css
.review-step {
  max-width: 560px;
}

.review-title {
  font-size: 22px;
  font-weight: 600;
  margin: 0 0 24px;
}

.review-section {
  padding: 20px 0;
  border-bottom: 1px solid #E5E7EB;
}

.review-section:last-child {
  border-bottom: none;
}

.review-section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.review-section-title {
  font-size: 16px;
  font-weight: 600;
  margin: 0;
}

.review-edit {
  font-size: 14px;
  color: #2563EB;
  background: none;
  border: none;
  cursor: pointer;
  font-weight: 500;
}

.review-fields {
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.review-field {
  display: flex;
  gap: 16px;
}

.review-label {
  width: 120px;
  flex-shrink: 0;
  font-size: 14px;
  color: #6B7280;
  font-weight: 400;
}

.review-value {
  font-size: 14px;
  color: #111827;
  margin: 0;
}
```

---

## Conditional Steps

Steps that are included or skipped based on user choices in earlier steps.

**Example:** Checkout flow where "Shipping Address" step is skipped for digital products.

```tsx
function useConditionalSteps(formData: FormData) {
  const allSteps = [
    { key: 'personal', title: 'Personal Info', condition: () => true },
    { key: 'shipping', title: 'Shipping', condition: () => formData.productType !== 'digital' },
    { key: 'payment', title: 'Payment', condition: () => true },
    { key: 'review', title: 'Review', condition: () => true },
  ];

  const activeSteps = allSteps.filter(step => step.condition());

  return { activeSteps, totalSteps: activeSteps.length };
}
```

---

## Specific Multi-Step Form Patterns

### Checkout Flow

**Steps:**
1. **Cart / Order Summary** (often not part of the form wizard)
2. **Contact Information** — Email, phone (for order updates)
3. **Shipping Address** — Street, city, state, zip, country
4. **Shipping Method** — Standard, express, overnight (radio cards)
5. **Payment** — Card details or saved payment method
6. **Review & Place Order** — Summary with edit links, total, submit

**Best practices:**
- Show a persistent order summary sidebar on desktop (sticky)
- Show order total and item count at all times
- Allow guest checkout — do not force account creation
- Auto-save each step as user progresses
- Expiry indicator if cart items can sell out

### Onboarding Flow

**Steps:**
1. **Welcome** — Value proposition, "Get started" CTA
2. **Profile Setup** — Name, avatar, role/title
3. **Preferences** — Notification settings, theme, language
4. **First Action** — Create first project, invite team, etc.
5. **Done** — Success screen, "Go to dashboard"

**Best practices:**
- Allow skip on every step (no required fields during onboarding)
- Show progress but keep it lightweight (progress bar, not numbered steps)
- Celebrate completion with micro-animation
- Defer complex setup to later

### Survey / Questionnaire

**Steps:** One question per page (or 2-3 related questions per page).

**Best practices:**
- Show progress bar (percentage or "4 of 12")
- Large, tappable answer options (card-style radio buttons)
- "Skip" option on every non-required question
- "Back" should restore previous answer
- Do not show step numbers if the total is large (shows "only 47 more questions" which is demotivating)

### Application Form (Job, Insurance, Loan)

**Steps:**
1. **Personal Details** — Name, DOB, SSN/ID, contact
2. **Employment / Income** — Employer, role, salary, duration
3. **Additional Information** — Application-specific (education, health history, property details)
4. **Document Upload** — Required documents (ID, pay stubs, etc.)
5. **Review & Submit** — Full summary, legal agreements, submit

**Best practices:**
- Show "Save and continue later" prominently
- Use "required" judiciously — allow partial saves
- Show a completion percentage that accounts for required vs. optional fields
- Indicate which documents are required vs. optional in the upload step

---

## Mobile Multi-Step Optimization

- Step indicator: collapse to "Step 2 of 4" text or a slim progress bar (not full numbered steps)
- Navigation: "Back" as a left arrow in the header, "Continue" as a full-width button at the bottom
- Form content: single column, full width
- Sticky footer: "Continue" button stays visible at the bottom as user scrolls through step content
- Keyboard: auto-focus the first field when a step loads (but not if it causes the keyboard to open annoyingly on mobile — balance this)

```css
.mobile-step-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-bottom: 1px solid #E5E7EB;
}

.mobile-step-back {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  cursor: pointer;
}

.mobile-step-info {
  flex: 1;
  text-align: center;
}

.mobile-step-label {
  font-size: 13px;
  color: #6B7280;
}

.mobile-step-title {
  font-size: 16px;
  font-weight: 600;
  color: #111827;
}

.mobile-step-footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 12px 16px;
  padding-bottom: max(12px, env(safe-area-inset-bottom));
  background: #FFFFFF;
  border-top: 1px solid #E5E7EB;
  z-index: 10;
}

.mobile-step-footer .form-button-primary {
  width: 100%;
}
```

---

## Full Multi-Step Form Component (Production React/TypeScript)

```tsx
import { useState, useCallback } from 'react';

// Types
interface StepConfig {
  key: string;
  title: string;
  component: React.ComponentType<StepProps>;
  validate: (data: FormData) => Record<string, string>;
}

interface StepProps {
  data: FormData;
  errors: Record<string, string>;
  updateFields: (fields: Partial<FormData>) => void;
}

interface FormData {
  name: string;
  email: string;
  street: string;
  city: string;
  state: string;
  zip: string;
}

// Hook
function useMultiStepForm(steps: StepConfig[]) {
  const [currentStepIndex, setCurrentStepIndex] = useState(0);
  const [formData, setFormData] = useState<FormData>({
    name: '', email: '', street: '', city: '', state: '', zip: '',
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [completedSteps, setCompletedSteps] = useState<Set<number>>(new Set());

  const currentStep = steps[currentStepIndex];
  const isFirstStep = currentStepIndex === 0;
  const isLastStep = currentStepIndex === steps.length - 1;

  const updateFields = useCallback((fields: Partial<FormData>) => {
    setFormData(prev => ({ ...prev, ...fields }));
    // Clear errors for updated fields
    const clearedErrors = { ...errors };
    Object.keys(fields).forEach(key => delete clearedErrors[key]);
    setErrors(clearedErrors);
  }, [errors]);

  const goToStep = useCallback((index: number) => {
    if (index >= 0 && index < steps.length) {
      setCurrentStepIndex(index);
      setErrors({});
    }
  }, [steps.length]);

  const goNext = useCallback(() => {
    const stepErrors = currentStep.validate(formData);
    if (Object.keys(stepErrors).length > 0) {
      setErrors(stepErrors);
      // Focus first error field
      const firstErrorKey = Object.keys(stepErrors)[0];
      document.getElementById(`field-${firstErrorKey}`)?.focus();
      return false;
    }
    setCompletedSteps(prev => new Set([...prev, currentStepIndex]));
    setErrors({});
    setCurrentStepIndex(prev => Math.min(prev + 1, steps.length - 1));
    // Scroll to top of form
    window.scrollTo({ top: 0, behavior: 'smooth' });
    return true;
  }, [currentStep, currentStepIndex, formData, steps.length]);

  const goBack = useCallback(() => {
    setErrors({});
    setCurrentStepIndex(prev => Math.max(prev - 1, 0));
  }, []);

  return {
    currentStepIndex,
    currentStep,
    formData,
    errors,
    completedSteps,
    isFirstStep,
    isLastStep,
    updateFields,
    goToStep,
    goNext,
    goBack,
  };
}

// Main Component
function MultiStepFormExample() {
  const steps: StepConfig[] = [
    {
      key: 'personal',
      title: 'Personal Info',
      component: PersonalInfoStep,
      validate: (data) => {
        const errors: Record<string, string> = {};
        if (!data.name.trim()) errors.name = 'Name is required';
        if (!data.email.trim()) errors.email = 'Email is required';
        return errors;
      },
    },
    {
      key: 'address',
      title: 'Address',
      component: AddressStep,
      validate: (data) => {
        const errors: Record<string, string> = {};
        if (!data.street.trim()) errors.street = 'Street is required';
        if (!data.city.trim()) errors.city = 'City is required';
        if (!data.zip.trim()) errors.zip = 'ZIP code is required';
        return errors;
      },
    },
    {
      key: 'review',
      title: 'Review',
      component: ReviewStep,
      validate: () => ({}),
    },
  ];

  const {
    currentStepIndex, currentStep, formData, errors,
    completedSteps, isFirstStep, isLastStep,
    updateFields, goToStep, goNext, goBack,
  } = useMultiStepForm(steps);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!isLastStep) {
      goNext();
      return;
    }
    // Final submission
    try {
      await submitForm(formData);
    } catch {
      // Handle error
    }
  };

  const StepComponent = currentStep.component;

  return (
    <div className="multi-step-container">
      <StepIndicator
        steps={steps.map((s, i) => ({
          title: s.title,
          isActive: i === currentStepIndex,
          isComplete: completedSteps.has(i),
        }))}
        currentStep={currentStepIndex}
      />
      <form onSubmit={handleSubmit} noValidate>
        <StepComponent data={formData} errors={errors} updateFields={updateFields} />
        <StepNavigation
          currentStep={currentStepIndex}
          totalSteps={steps.length}
          isFirstStep={isFirstStep}
          isLastStep={isLastStep}
          onBack={goBack}
          onNext={goNext}
        />
      </form>
    </div>
  );
}
```

```css
.multi-step-container {
  max-width: 560px;
  margin: 0 auto;
  padding: 40px 24px;
}

@media (max-width: 600px) {
  .multi-step-container {
    padding: 24px 16px;
  }
}
```

---

## Multi-Step Form Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No "Back" button | User feels trapped, cannot correct mistakes | Always provide back navigation |
| No progress indicator | User does not know how much is left | Show steps or progress bar |
| Losing data on back | Infuriating — user has to re-enter fields | Persist all data in state |
| Validating all at end | User discovers step-1 errors at step-4 | Validate per step |
| Too many steps (>7) | Drop-off compounds per step | Combine steps, reduce fields |
| Steps with only 1-2 fields | Extra clicks for minimal grouping | Combine with adjacent step |
| No "Save draft" for long forms | User loses work on accidental navigation | Persist to localStorage or server |
| Auto-advancing without confirmation | Jarring, user may not be done | Require explicit "Next" click |
| Different layouts per step | Disorienting, inconsistent | Keep layout consistent |
| No review step for important forms | User cannot verify before committing | Add review step for checkout, applications |
