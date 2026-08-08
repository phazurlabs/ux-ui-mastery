# Form Analytics

Measuring form performance: what to instrument, which metrics reveal which failure, and how to read them.

## Form Analytics — Measuring Form Performance

### Key Metrics

**Completion Rate**
- Formula: `Submissions / Form Views * 100`
- Benchmark: 20-40% (varies wildly by form type)
- Track both started and completed

**Drop-Off Rate by Field**
- Which field causes the most abandonment?
- Measure time from focus to blur per field; flag outliers
- Track last field interacted before abandonment

**Field Timing**
- Average time to complete each field
- Fields taking >30 seconds indicate confusion
- Compare against expected time for field type

**Error Rate by Field**
- Which fields generate the most errors?
- Track error type frequency (required, format, custom)
- High error rate = redesign the field

**Interaction Metrics**
- Tab vs. click navigation ratio
- Backspace/delete frequency per field (indicates confusion)
- Paste usage (especially in card/code fields)

### Analytics Implementation
```jsx
// Track field interaction events
function trackFieldEvent(fieldName, event, metadata = {}) {
  analytics.track('form_field_event', {
    form_id: formId,
    field_name: fieldName,
    event_type: event, // 'focus', 'blur', 'error', 'change', 'paste'
    timestamp: Date.now(),
    time_spent: metadata.duration,
    error_message: metadata.error,
    attempt_number: metadata.attempt
  });
}

// Track form-level events
function trackFormEvent(event, metadata = {}) {
  analytics.track('form_event', {
    form_id: formId,
    event_type: event, // 'view', 'start', 'submit', 'success', 'error', 'abandon'
    step: metadata.step,
    fields_completed: metadata.fieldsCompleted,
    total_fields: metadata.totalFields,
    duration: metadata.duration,
    error_count: metadata.errorCount
  });
}
```

### Funnel Analysis for Multi-Step Forms
- Track conversion rate between each step
- Identify the "killer step" (highest drop-off)
- A/B test step order and grouping
- Monitor review-step-to-submit conversion (should be >90%)

---
