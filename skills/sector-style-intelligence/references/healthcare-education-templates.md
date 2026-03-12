# Healthcare & Education Page Templates — Complete Implementation Guide

## Overview

This reference provides complete page-level templates for 5 healthcare pages and 5 education pages. Each template includes block sequence, typography, color application, spacing rhythm, component selection, responsive behavior, and React/TSX skeletons.

Healthcare templates prioritize accessibility requirements and HIPAA/compliance UI patterns. Education templates prioritize engagement patterns and progress motivation.

---

## PART 1: HEALTHCARE TEMPLATES

### Healthcare Design Principles

Healthcare interfaces must prioritize:
1. **Accessibility** — WCAG 2.2 AA minimum, AAA preferred. Many users have visual, motor, or cognitive impairments
2. **Clarity** — Medical information must be unambiguous. Plain language, clear hierarchy
3. **Trust** — Clinical precision builds confidence. Professional, calm aesthetic
4. **Compliance** — HIPAA-conscious UI: no PHI in URLs, session timeouts, audit trails
5. **Inclusivity** — Support for elderly users, screen readers, high contrast, large text

### HIPAA UI Requirements
- Session timeout after 15 minutes of inactivity with warning at 13 minutes
- No PHI in URL parameters or browser titles
- Automatic screen lock/blur when tab loses focus (configurable)
- Audit trail for all PHI access (not visible to user, but logged)
- Minimum 8-character passwords with complexity requirements
- Two-factor authentication for PHI access
- Consent banners before displaying health records
- Print/export watermarked with user identity and timestamp

### Accessibility Requirements (Critical)
- Minimum 4.5:1 contrast ratio for all text (7:1 preferred)
- All images have meaningful alt text
- All form inputs have visible labels (not just placeholders)
- Focus indicators visible on all interactive elements
- Skip navigation links
- ARIA landmarks on all major sections
- Keyboard navigable throughout
- Minimum 44x44px touch targets
- Support for 200% text zoom without horizontal scroll
- No information conveyed by color alone

---

## 1. Patient Portal Dashboard

### Block Sequence
1. Header (patient name + notifications + logout)
2. Upcoming appointments card
3. Quick actions row (book appointment, message doctor, refill Rx, view records)
4. Health summary cards (vitals, medications, allergies)
5. Recent messages from care team
6. Recent test results (with status indicators)

### Typography Map
| Element | Font | Weight | Size | Line-Height | Min Contrast |
|---|---|---|---|---|---|
| Patient name | Inter | 600 | 20px | 28px | 7:1 |
| Card heading | Inter | 600 | 16px | 24px | 7:1 |
| Body text | Inter | 400 | 15px | 24px | 4.5:1 |
| Label text | Inter | 500 | 13px | 18px | 4.5:1 |
| Metric value | Inter | 600 | 24px | 32px | 7:1 |
| Caption | Inter | 400 | 13px | 18px | 4.5:1 |
| Button text | Inter | 500 | 15px | 22px | 4.5:1 |

### Color Application
```
Background:             #FFFFFF
Card background:        #FFFFFF border: 1px solid #E2E8F0
Sidebar bg:             #F8FAFC
Primary accent:         #0369A1 (accessible blue, 7:1 on white)
Primary hover:          #075985
Success:                #15803D (accessible green)
Warning:                #B45309 (accessible amber)
Error:                  #DC2626 (accessible red)
Text primary:           #0F172A (near black, high contrast)
Text secondary:         #475569 (passes 4.5:1)
Text muted:             #64748B (passes 4.5:1 on white)
Border:                 #E2E8F0
Focus ring:             #0369A1 with 3px offset
Link:                   #0369A1 with underline (always underlined for accessibility)
```

### Spacing Rhythm
```
Header height:          72px (large for easy targeting)
Card gap:               20px
Card padding:           24px
Quick action button:    min 48px height (exceeds 44px minimum)
Touch target minimum:   44x44px
Section gap:            32px
Content max-width:      1100px
Content padding:        24px
```

### React/TSX Skeleton
```tsx
export function PatientDashboard() {
  return (
    <div className="min-h-screen bg-white">
      {/* Skip Navigation */}
      <a href="#main-content" className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-50 focus:rounded-lg focus:bg-[#0369A1] focus:px-4 focus:py-2 focus:text-white">
        Skip to main content
      </a>

      {/* Header */}
      <header className="border-b border-[#E2E8F0] bg-white" role="banner">
        <div className="mx-auto flex h-[72px] max-w-[1100px] items-center justify-between px-6">
          <div className="flex items-center gap-4">
            <span className="text-base font-semibold text-[#0F172A]">HealthPortal</span>
          </div>
          <div className="flex items-center gap-4">
            <button className="relative rounded-lg p-3 hover:bg-[#F8FAFC] focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2" aria-label="Notifications">
              <span className="text-[#475569]">bell</span>
              <span className="absolute right-2 top-2 h-2.5 w-2.5 rounded-full bg-[#DC2626]" aria-label="New notifications" />
            </button>
            <button className="flex items-center gap-2 rounded-lg px-3 py-2 hover:bg-[#F8FAFC] focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2">
              <div className="flex h-9 w-9 items-center justify-center rounded-full bg-[#0369A1] text-sm font-medium text-white" aria-hidden="true">AP</div>
              <span className="text-sm font-medium text-[#0F172A]">Alex Patient</span>
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main id="main-content" className="mx-auto max-w-[1100px] px-6 py-8" role="main">
        <h1 className="text-xl font-semibold text-[#0F172A]">Welcome back, Alex</h1>

        {/* Upcoming Appointment */}
        <section className="mt-6" aria-labelledby="upcoming-heading">
          <div className="rounded-xl border border-[#E2E8F0] bg-[#F0F9FF] p-6">
            <h2 id="upcoming-heading" className="text-base font-semibold text-[#0F172A]">Upcoming Appointment</h2>
            <div className="mt-3 flex items-center justify-between">
              <div>
                <p className="text-[15px] font-medium text-[#0F172A]">Dr. Sarah Johnson — Primary Care</p>
                <p className="mt-1 text-sm text-[#475569]">Thursday, March 14, 2026 at 2:30 PM</p>
                <p className="mt-1 text-sm text-[#475569]">Video Visit</p>
              </div>
              <div className="flex gap-3">
                <button className="rounded-lg border border-[#E2E8F0] px-4 py-2.5 text-sm font-medium text-[#0F172A] hover:bg-white focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2">
                  Reschedule
                </button>
                <button className="rounded-lg bg-[#0369A1] px-4 py-2.5 text-sm font-medium text-white hover:bg-[#075985] focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2">
                  Join Video Visit
                </button>
              </div>
            </div>
          </div>
        </section>

        {/* Quick Actions */}
        <section className="mt-6" aria-labelledby="actions-heading">
          <h2 id="actions-heading" className="sr-only">Quick Actions</h2>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
            {[
              { label: 'Book Appointment', icon: 'calendar' },
              { label: 'Message Doctor', icon: 'message' },
              { label: 'Refill Prescription', icon: 'pill' },
              { label: 'View Records', icon: 'folder' },
            ].map((action) => (
              <button key={action.label} className="flex flex-col items-center gap-3 rounded-xl border border-[#E2E8F0] p-5 hover:border-[#0369A1] hover:bg-[#F0F9FF] focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2 transition-colors">
                <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-[#F0F9FF]">
                  <span className="text-[#0369A1]">{action.icon}</span>
                </div>
                <span className="text-sm font-medium text-[#0F172A]">{action.label}</span>
              </button>
            ))}
          </div>
        </section>

        {/* Health Summary */}
        <section className="mt-8" aria-labelledby="health-heading">
          <h2 id="health-heading" className="text-lg font-semibold text-[#0F172A]">Health Summary</h2>
          <div className="mt-4 grid gap-4 sm:grid-cols-3">
            <div className="rounded-xl border border-[#E2E8F0] p-5">
              <h3 className="text-sm font-medium text-[#475569]">Blood Pressure</h3>
              <p className="mt-2 text-2xl font-semibold text-[#0F172A]">120/80</p>
              <p className="mt-1 text-sm text-[#15803D]">Normal range</p>
              <p className="mt-1 text-xs text-[#64748B]">Recorded Mar 1, 2026</p>
            </div>
            <div className="rounded-xl border border-[#E2E8F0] p-5">
              <h3 className="text-sm font-medium text-[#475569]">Medications</h3>
              <p className="mt-2 text-2xl font-semibold text-[#0F172A]">3</p>
              <p className="mt-1 text-sm text-[#475569]">Active prescriptions</p>
              <a href="#" className="mt-2 inline-block text-sm font-medium text-[#0369A1] underline focus:outline-none focus:ring-2 focus:ring-[#0369A1]">View details</a>
            </div>
            <div className="rounded-xl border border-[#E2E8F0] p-5">
              <h3 className="text-sm font-medium text-[#475569]">Allergies</h3>
              <p className="mt-2 text-base font-medium text-[#0F172A]">Penicillin, Sulfa</p>
              <p className="mt-1 text-sm text-[#DC2626]">2 known allergies</p>
            </div>
          </div>
        </section>

        {/* Recent Test Results */}
        <section className="mt-8" aria-labelledby="results-heading">
          <h2 id="results-heading" className="text-lg font-semibold text-[#0F172A]">Recent Test Results</h2>
          <div className="mt-4 rounded-xl border border-[#E2E8F0]">
            <table className="w-full" role="table">
              <thead>
                <tr className="border-b border-[#E2E8F0] text-left">
                  <th scope="col" className="px-5 py-3 text-xs font-medium uppercase tracking-wider text-[#64748B]">Test</th>
                  <th scope="col" className="px-5 py-3 text-xs font-medium uppercase tracking-wider text-[#64748B]">Date</th>
                  <th scope="col" className="px-5 py-3 text-xs font-medium uppercase tracking-wider text-[#64748B]">Status</th>
                  <th scope="col" className="px-5 py-3 text-xs font-medium uppercase tracking-wider text-[#64748B]">Action</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#E2E8F0]">
                {[
                  { test: 'Complete Blood Count', date: 'Mar 5, 2026', status: 'Results Ready', statusColor: 'text-[#15803D] bg-[#F0FDF4]' },
                  { test: 'Lipid Panel', date: 'Mar 5, 2026', status: 'Pending', statusColor: 'text-[#B45309] bg-[#FFFBEB]' },
                  { test: 'Thyroid Function', date: 'Feb 20, 2026', status: 'Reviewed', statusColor: 'text-[#475569] bg-[#F8FAFC]' },
                ].map((result) => (
                  <tr key={result.test} className="hover:bg-[#F8FAFC]">
                    <td className="px-5 py-4 text-sm font-medium text-[#0F172A]">{result.test}</td>
                    <td className="px-5 py-4 text-sm text-[#475569]">{result.date}</td>
                    <td className="px-5 py-4">
                      <span className={`inline-block rounded-full px-2.5 py-1 text-xs font-medium ${result.statusColor}`}>{result.status}</span>
                    </td>
                    <td className="px-5 py-4">
                      <a href="#" className="text-sm font-medium text-[#0369A1] underline focus:outline-none focus:ring-2 focus:ring-[#0369A1]">View</a>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        {/* Session Warning (hidden by default, shown at 13 min) */}
        <div role="alert" className="hidden fixed bottom-4 right-4 max-w-sm rounded-xl border border-[#B45309] bg-[#FFFBEB] p-4 shadow-lg">
          <p className="text-sm font-medium text-[#B45309]">Session expiring soon</p>
          <p className="mt-1 text-xs text-[#92400E]">For your security, you will be logged out in 2 minutes.</p>
          <button className="mt-3 rounded-lg bg-[#B45309] px-4 py-2 text-xs font-medium text-white">Stay logged in</button>
        </div>
      </main>
    </div>
  );
}
```

---

## 2. Appointment Booking Flow

### Block Sequence
1. Provider selection (search, specialty filter, availability)
2. Date and time selection (calendar + time slots)
3. Visit type selection (in-person, video, phone)
4. Reason for visit (symptom checklist + free text)
5. Insurance verification (optional)
6. Confirmation with calendar add

### Accessibility Requirements
- Calendar must be keyboard navigable
- Time slots must have clear available/unavailable states (not color alone)
- Screen reader should announce "Available" or "Unavailable" for each slot
- Large touch targets for date/time selection
- Clear error messages for invalid selections

```tsx
import { useState } from 'react';

export function AppointmentBooking() {
  const [step, setStep] = useState(1);

  return (
    <div className="min-h-screen bg-[#F8FAFC]">
      <div className="mx-auto max-w-[640px] px-6 py-10">
        {/* Progress */}
        <nav aria-label="Booking progress">
          <ol className="flex items-center gap-4">
            {['Provider', 'Date & Time', 'Details', 'Confirm'].map((label, i) => (
              <li key={label} className="flex items-center gap-2">
                <div className={`flex h-8 w-8 items-center justify-center rounded-full text-sm font-medium ${
                  i + 1 <= step ? 'bg-[#0369A1] text-white' : 'bg-[#E2E8F0] text-[#64748B]'
                }`} aria-current={i + 1 === step ? 'step' : undefined}>
                  {i + 1}
                </div>
                <span className={`text-sm ${i + 1 <= step ? 'font-medium text-[#0F172A]' : 'text-[#64748B]'}`}>{label}</span>
              </li>
            ))}
          </ol>
        </nav>

        <div className="mt-8 rounded-2xl bg-white p-8 shadow-sm">
          {step === 1 && (
            <div>
              <h1 className="text-xl font-semibold text-[#0F172A]">Choose a provider</h1>
              <input type="search" placeholder="Search by name or specialty" aria-label="Search providers"
                className="mt-4 w-full rounded-lg border border-[#E2E8F0] px-4 py-3 text-[15px] focus:border-[#0369A1] focus:outline-none focus:ring-2 focus:ring-[#0369A1]" />
              <div className="mt-4 space-y-3">
                {['Dr. Sarah Johnson — Primary Care', 'Dr. Michael Chen — Dermatology', 'Dr. Emily Rodriguez — Cardiology'].map((doc) => (
                  <button key={doc} className="flex w-full items-center gap-4 rounded-xl border border-[#E2E8F0] p-4 text-left hover:border-[#0369A1] hover:bg-[#F0F9FF] focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2">
                    <div className="flex h-12 w-12 items-center justify-center rounded-full bg-[#F0F9FF] text-sm font-medium text-[#0369A1]">
                      {doc.split(' ')[1][0]}
                    </div>
                    <div>
                      <p className="text-[15px] font-medium text-[#0F172A]">{doc.split(' — ')[0]}</p>
                      <p className="text-sm text-[#475569]">{doc.split(' — ')[1]}</p>
                    </div>
                  </button>
                ))}
              </div>
            </div>
          )}

          {step === 2 && (
            <div>
              <h1 className="text-xl font-semibold text-[#0F172A]">Select date and time</h1>
              <div className="mt-4 rounded-lg border border-[#E2E8F0] p-4">
                <p className="text-sm font-medium text-[#0F172A]">March 2026</p>
                {/* Calendar grid placeholder */}
                <div className="mt-3 grid grid-cols-7 gap-2" role="grid" aria-label="Calendar">
                  {['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'].map((d) => (
                    <div key={d} className="text-center text-xs font-medium text-[#64748B]" role="columnheader">{d}</div>
                  ))}
                  {Array.from({ length: 31 }, (_, i) => (
                    <button key={i} className={`flex h-10 w-10 items-center justify-center rounded-lg text-sm ${
                      [14, 15, 17, 20, 21].includes(i + 1)
                        ? 'bg-white text-[#0F172A] hover:bg-[#F0F9FF] border border-[#E2E8F0] focus:ring-2 focus:ring-[#0369A1]'
                        : 'text-[#CBD5E1] cursor-not-allowed'
                    }`}
                      disabled={![14, 15, 17, 20, 21].includes(i + 1)}
                      aria-label={`March ${i + 1}${[14, 15, 17, 20, 21].includes(i + 1) ? ', available' : ', unavailable'}`}>
                      {i + 1}
                    </button>
                  ))}
                </div>
              </div>
              <div className="mt-4">
                <p className="text-sm font-medium text-[#0F172A]">Available times for March 14</p>
                <div className="mt-3 grid grid-cols-3 gap-2">
                  {['9:00 AM', '10:30 AM', '11:00 AM', '2:00 PM', '2:30 PM', '4:00 PM'].map((time) => (
                    <button key={time} className="rounded-lg border border-[#E2E8F0] px-4 py-3 text-sm font-medium text-[#0F172A] hover:border-[#0369A1] hover:bg-[#F0F9FF] focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2">
                      {time}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}

          <div className="mt-8 flex items-center justify-between">
            {step > 1 && (
              <button onClick={() => setStep(step - 1)} className="text-sm font-medium text-[#0369A1] underline focus:outline-none focus:ring-2 focus:ring-[#0369A1]">Back</button>
            )}
            <button onClick={() => setStep(step + 1)} className="ml-auto rounded-lg bg-[#0369A1] px-6 py-3 text-sm font-medium text-white hover:bg-[#075985] focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2">
              Continue
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## 3. Health Records Viewer

### Block Sequence
1. Record type tabs (lab results, imaging, visit summaries, immunizations)
2. Date range filter
3. Record list (date, type, provider, status)
4. Record detail view (full report with values and reference ranges)
5. Download/share options (with HIPAA consent)

### HIPAA Compliance
- Consent confirmation before first view in session
- Download watermarked with patient name and timestamp
- Share generates secure link with expiration
- Access logged in audit trail

```tsx
export function HealthRecords() {
  return (
    <div className="min-h-screen bg-white">
      <div className="mx-auto max-w-[900px] px-6 py-8">
        <h1 className="text-xl font-semibold text-[#0F172A]">Health Records</h1>

        {/* Consent Banner */}
        <div role="alert" className="mt-4 rounded-xl border border-[#0369A1] bg-[#F0F9FF] p-4">
          <p className="text-sm text-[#0F172A]">
            You are viewing protected health information. Access is logged for HIPAA compliance.
          </p>
        </div>

        {/* Tabs */}
        <div className="mt-6 border-b border-[#E2E8F0]" role="tablist">
          {['Lab Results', 'Imaging', 'Visit Summaries', 'Immunizations', 'Medications'].map((tab, i) => (
            <button key={tab} role="tab" aria-selected={i === 0}
              className={`px-4 py-3 text-sm font-medium ${i === 0 ? 'border-b-2 border-[#0369A1] text-[#0369A1]' : 'text-[#64748B] hover:text-[#0F172A]'} focus:outline-none focus:ring-2 focus:ring-[#0369A1]`}>
              {tab}
            </button>
          ))}
        </div>

        {/* Records List */}
        <div className="mt-6" role="tabpanel">
          <div className="rounded-xl border border-[#E2E8F0]">
            <table className="w-full">
              <thead>
                <tr className="border-b border-[#E2E8F0]">
                  <th scope="col" className="px-5 py-3 text-left text-xs font-medium uppercase tracking-wider text-[#64748B]">Test</th>
                  <th scope="col" className="px-5 py-3 text-left text-xs font-medium uppercase tracking-wider text-[#64748B]">Date</th>
                  <th scope="col" className="px-5 py-3 text-left text-xs font-medium uppercase tracking-wider text-[#64748B]">Provider</th>
                  <th scope="col" className="px-5 py-3 text-left text-xs font-medium uppercase tracking-wider text-[#64748B]">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#E2E8F0]">
                {[
                  { test: 'Complete Blood Count (CBC)', date: 'Mar 5, 2026', provider: 'Dr. Johnson', status: 'Normal', statusColor: 'text-[#15803D] bg-[#F0FDF4]' },
                  { test: 'Hemoglobin A1C', date: 'Mar 5, 2026', provider: 'Dr. Johnson', status: 'Review', statusColor: 'text-[#B45309] bg-[#FFFBEB]' },
                  { test: 'Lipid Panel', date: 'Feb 20, 2026', provider: 'Dr. Chen', status: 'Normal', statusColor: 'text-[#15803D] bg-[#F0FDF4]' },
                ].map((r) => (
                  <tr key={r.test} className="hover:bg-[#F8FAFC] cursor-pointer">
                    <td className="px-5 py-4 text-sm font-medium text-[#0F172A]">{r.test}</td>
                    <td className="px-5 py-4 text-sm text-[#475569]">{r.date}</td>
                    <td className="px-5 py-4 text-sm text-[#475569]">{r.provider}</td>
                    <td className="px-5 py-4">
                      <span className={`rounded-full px-2.5 py-1 text-xs font-medium ${r.statusColor}`}>
                        {r.status}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## 4. Telemedicine / Video Call Interface

### Block Sequence
1. Pre-call checklist (camera, mic, connection test)
2. Video call main view (provider video large, self video small)
3. Call controls bar (mute, camera, share screen, chat, end call)
4. Side panel (patient notes, vitals, chat)
5. Post-call summary (visit notes, prescriptions, follow-up)

### Accessibility Requirements
- All controls keyboard accessible
- Screen reader announces participant join/leave
- Captions/transcript support (for hearing impaired)
- High contrast control bar
- Large control buttons (56px minimum)

```tsx
export function TelemedicineInterface() {
  return (
    <div className="flex h-screen bg-[#0F172A]">
      {/* Main Video */}
      <div className="flex flex-1 flex-col">
        <div className="relative flex-1 bg-[#1E293B]">
          {/* Provider Video */}
          <div className="absolute inset-0 flex items-center justify-center">
            <span className="text-white/30">Provider Video Feed</span>
          </div>
          {/* Self Video */}
          <div className="absolute bottom-4 right-4 h-32 w-44 rounded-xl bg-[#334155] shadow-lg">
            <span className="flex h-full items-center justify-center text-xs text-white/30">You</span>
          </div>
          {/* Provider Name */}
          <div className="absolute left-4 top-4 rounded-lg bg-black/50 px-3 py-1.5 backdrop-blur">
            <p className="text-sm font-medium text-white">Dr. Sarah Johnson</p>
            <p className="text-xs text-white/70">Primary Care</p>
          </div>
          {/* Duration */}
          <div className="absolute right-4 top-4 rounded-lg bg-black/50 px-3 py-1.5 backdrop-blur">
            <p className="text-sm font-medium text-white">12:34</p>
          </div>
        </div>

        {/* Controls */}
        <div className="flex items-center justify-center gap-4 bg-[#0F172A] px-6 py-4">
          <button className="flex h-14 w-14 items-center justify-center rounded-full bg-[#334155] text-white hover:bg-[#475569] focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-[#0F172A]" aria-label="Toggle microphone">
            mic
          </button>
          <button className="flex h-14 w-14 items-center justify-center rounded-full bg-[#334155] text-white hover:bg-[#475569] focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-[#0F172A]" aria-label="Toggle camera">
            camera
          </button>
          <button className="flex h-14 w-14 items-center justify-center rounded-full bg-[#334155] text-white hover:bg-[#475569] focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-[#0F172A]" aria-label="Share screen">
            screen
          </button>
          <button className="flex h-14 w-14 items-center justify-center rounded-full bg-[#334155] text-white hover:bg-[#475569] focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-[#0F172A]" aria-label="Toggle captions">
            CC
          </button>
          <button className="flex h-14 w-14 items-center justify-center rounded-full bg-[#DC2626] text-white hover:bg-[#B91C1C] focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-[#0F172A]" aria-label="End call">
            end
          </button>
        </div>
      </div>

      {/* Side Panel */}
      <aside className="hidden w-80 border-l border-[#334155] bg-[#1E293B] p-4 lg:block">
        <div className="flex gap-2">
          {['Chat', 'Notes'].map((tab, i) => (
            <button key={tab} className={`rounded-lg px-4 py-2 text-sm font-medium ${i === 0 ? 'bg-[#334155] text-white' : 'text-[#94A3B8]'}`}>
              {tab}
            </button>
          ))}
        </div>
        <div className="mt-4 flex-1 rounded-lg bg-[#0F172A] p-4">
          <p className="text-sm text-[#94A3B8]">Chat messages will appear here...</p>
        </div>
      </aside>
    </div>
  );
}
```

---

## 5. Medication Management Page

### Block Sequence
1. Active medications list (name, dosage, frequency, prescriber, refill date)
2. Medication schedule (daily timeline)
3. Refill requests section
4. Drug interaction warnings
5. Pharmacy information
6. Medication history

### Accessibility: Large text for medication names, clear dosage instructions, color + icon for warnings

```tsx
export function MedicationManagement() {
  const medications = [
    { name: 'Lisinopril', dosage: '10mg', frequency: 'Once daily, morning', prescriber: 'Dr. Johnson', refillDate: 'Mar 20, 2026', refillsLeft: 3 },
    { name: 'Metformin', dosage: '500mg', frequency: 'Twice daily, with meals', prescriber: 'Dr. Johnson', refillDate: 'Apr 1, 2026', refillsLeft: 5 },
    { name: 'Atorvastatin', dosage: '20mg', frequency: 'Once daily, bedtime', prescriber: 'Dr. Chen', refillDate: 'Mar 15, 2026', refillsLeft: 1 },
  ];

  return (
    <div className="min-h-screen bg-white">
      <div className="mx-auto max-w-[900px] px-6 py-8">
        <h1 className="text-xl font-semibold text-[#0F172A]">Medications</h1>

        {/* Warning */}
        <div role="alert" className="mt-4 flex items-start gap-3 rounded-xl border border-[#B45309] bg-[#FFFBEB] p-4">
          <span className="text-[#B45309] text-lg" aria-hidden="true">warning</span>
          <div>
            <p className="text-sm font-medium text-[#B45309]">Refill needed soon</p>
            <p className="text-sm text-[#92400E]">Atorvastatin has only 1 refill remaining. Contact your provider for a renewal.</p>
          </div>
        </div>

        {/* Medication Cards */}
        <div className="mt-6 space-y-4">
          {medications.map((med) => (
            <div key={med.name} className="rounded-xl border border-[#E2E8F0] p-5">
              <div className="flex items-start justify-between">
                <div>
                  <h2 className="text-lg font-semibold text-[#0F172A]">{med.name}</h2>
                  <p className="mt-1 text-[15px] text-[#475569]">{med.dosage} - {med.frequency}</p>
                  <p className="mt-1 text-sm text-[#64748B]">Prescribed by {med.prescriber}</p>
                </div>
                <div className="text-right">
                  <p className="text-sm text-[#475569]">Next refill: {med.refillDate}</p>
                  <p className={`text-sm ${med.refillsLeft <= 1 ? 'font-medium text-[#B45309]' : 'text-[#64748B]'}`}>
                    {med.refillsLeft} refill{med.refillsLeft !== 1 ? 's' : ''} remaining
                  </p>
                </div>
              </div>
              <div className="mt-4 flex gap-3">
                <button className="rounded-lg bg-[#0369A1] px-4 py-2 text-sm font-medium text-white hover:bg-[#075985] focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2">
                  Request Refill
                </button>
                <button className="rounded-lg border border-[#E2E8F0] px-4 py-2 text-sm font-medium text-[#0F172A] hover:bg-[#F8FAFC] focus:outline-none focus:ring-2 focus:ring-[#0369A1] focus:ring-offset-2">
                  View Details
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
```

---

## PART 2: EDUCATION TEMPLATES

### Education Design Principles

Education interfaces must prioritize:
1. **Engagement** — Progress tracking, gamification, celebration of achievements
2. **Clarity** — Complex concepts need clear visual hierarchy
3. **Motivation** — Streaks, badges, progress bars, social learning
4. **Accessibility** — Diverse learners with varying abilities and learning styles
5. **Focus** — Minimize distractions during active learning

### Engagement Patterns
- Progress bars and completion percentages on every surface
- Streak counters and daily goals
- Achievement badges and milestone celebrations
- Spaced repetition indicators
- Social proof (learners enrolled, completion rates)
- Encouraging microcopy at every stage

---

## 6. Course Catalog / Browse Page

### Block Sequence
1. Hero search (large search bar with popular topics)
2. Category navigation (horizontal scroll or grid)
3. Featured courses carousel
4. Course grid (cards with thumbnail, title, instructor, rating, price)
5. Filter sidebar (category, level, duration, price, rating)
6. Trending / popular section

### Typography Map
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Page headline | Inter | 700 | 32px | 40px |
| Course title | Inter | 600 | 16px | 22px |
| Instructor name | Inter | 400 | 13px | 18px |
| Price | Inter | 700 | 18px | 24px |
| Rating | Inter | 600 | 13px | 18px |
| Category label | Inter | 500 | 14px | 20px |
| Enrollment count | Inter | 400 | 12px | 16px |

### Color Application
```
Background:             #FAFAFA
Card background:        #FFFFFF shadow-sm
Primary accent:         #5624D0 (educational purple, like Udemy)
Primary hover:          #4815B5
Success/complete:       #1AA053 (positive green)
Progress bar:           #5624D0
Rating stars:           #E59819
Text primary:           #1A1A1A
Text secondary:         #6A6F73
Badge "Bestseller":     #ECEB98 bg, #3D3C0A text
Badge "New":            #ACD2CC bg, #003B36 text
Price:                  #1A1A1A
Sale price:             #1A1A1A (bold)
Original price:         #6A6F73 (strikethrough)
```

### React/TSX Skeleton
```tsx
export function CourseCatalog() {
  const categories = ['Development', 'Design', 'Business', 'Marketing', 'Data Science', 'Personal Development'];

  const courses = Array.from({ length: 8 }, (_, i) => ({
    id: i + 1,
    title: `Complete Course Title for Course ${i + 1}`,
    instructor: 'Dr. Expert Name',
    rating: 4.5 + Math.random() * 0.4,
    reviews: Math.floor(Math.random() * 10000) + 500,
    price: 12.99 + i * 5,
    originalPrice: 84.99,
    students: Math.floor(Math.random() * 50000) + 5000,
    badge: i === 0 ? 'Bestseller' : i === 1 ? 'New' : null,
    level: ['Beginner', 'Intermediate', 'Advanced'][i % 3],
    duration: `${10 + i * 3} hours`,
  }));

  return (
    <div className="min-h-screen bg-[#FAFAFA]">
      {/* Search Hero */}
      <section className="bg-[#1A1A1A] py-12">
        <div className="mx-auto max-w-[1200px] px-6 text-center">
          <h1 className="text-3xl font-bold text-white">What do you want to learn?</h1>
          <div className="mx-auto mt-6 max-w-[600px]">
            <input type="search" placeholder="Search for courses, topics, or instructors..."
              className="w-full rounded-lg border-0 px-5 py-4 text-[15px] shadow-lg focus:outline-none focus:ring-2 focus:ring-[#5624D0]" />
          </div>
          <div className="mt-4 flex items-center justify-center gap-3">
            <span className="text-sm text-white/70">Popular:</span>
            {['Python', 'React', 'UX Design', 'Data Science'].map((topic) => (
              <a key={topic} href="#" className="rounded-full border border-white/30 px-3 py-1 text-sm text-white/90 hover:bg-white/10">{topic}</a>
            ))}
          </div>
        </div>
      </section>

      {/* Categories */}
      <section className="border-b border-gray-200 bg-white">
        <div className="mx-auto max-w-[1200px] px-6">
          <div className="flex gap-6 overflow-x-auto py-4">
            {categories.map((cat) => (
              <a key={cat} href="#" className="flex-shrink-0 text-sm font-medium text-[#6A6F73] hover:text-[#1A1A1A]">{cat}</a>
            ))}
          </div>
        </div>
      </section>

      {/* Course Grid */}
      <section className="py-10">
        <div className="mx-auto max-w-[1200px] px-6">
          <h2 className="text-2xl font-bold text-[#1A1A1A]">Popular courses</h2>
          <div className="mt-6 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {courses.map((c) => (
              <a key={c.id} href="#" className="group overflow-hidden rounded-lg bg-white shadow-sm hover:shadow-md transition-shadow">
                <div className="aspect-[16/9] bg-gray-200 relative">
                  {c.badge && (
                    <span className={`absolute left-2 top-2 rounded px-2 py-0.5 text-[11px] font-bold ${
                      c.badge === 'Bestseller' ? 'bg-[#ECEB98] text-[#3D3C0A]' : 'bg-[#ACD2CC] text-[#003B36]'
                    }`}>{c.badge}</span>
                  )}
                </div>
                <div className="p-4">
                  <h3 className="text-[15px] font-semibold leading-tight text-[#1A1A1A] line-clamp-2 group-hover:text-[#5624D0]">{c.title}</h3>
                  <p className="mt-1 text-xs text-[#6A6F73]">{c.instructor}</p>
                  <div className="mt-1 flex items-center gap-1">
                    <span className="text-sm font-bold text-[#E59819]">{c.rating.toFixed(1)}</span>
                    <span className="text-xs text-[#E59819]">stars</span>
                    <span className="text-xs text-[#6A6F73]">({c.reviews.toLocaleString()})</span>
                  </div>
                  <p className="mt-1 text-xs text-[#6A6F73]">{c.duration} - {c.level}</p>
                  <div className="mt-2 flex items-center gap-2">
                    <span className="text-lg font-bold text-[#1A1A1A]">${c.price.toFixed(2)}</span>
                    <span className="text-sm text-[#6A6F73] line-through">${c.originalPrice.toFixed(2)}</span>
                  </div>
                </div>
              </a>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
```

---

## 7. Course Detail Page

### Block Sequence
1. Course header (title, subtitle, instructor, rating, enrollment count)
2. Promo video / preview
3. What you will learn (checkmark list)
4. Course curriculum (expandable sections with lesson list)
5. Instructor bio
6. Reviews section (summary + individual)
7. Related courses

### Engagement Patterns
- "X students enrolled" social proof
- "Last updated" freshness signal
- "30-day money-back guarantee" trust signal
- Course completion certificate preview
- Preview lessons unlocked for free

---

## 8. Learning Dashboard (Progress Tracking)

### Block Sequence
1. Welcome back header (streak count, daily goal)
2. Continue learning card (current course with progress)
3. Active courses grid (with progress bars)
4. Achievements / badges section
5. Weekly activity chart
6. Recommended next courses

```tsx
export function LearningDashboard() {
  const courses = [
    { title: 'Complete React Developer', progress: 68, lastLesson: 'useEffect Deep Dive', totalHours: 40, completedHours: 27.2 },
    { title: 'UX Research Fundamentals', progress: 35, lastLesson: 'User Interview Techniques', totalHours: 12, completedHours: 4.2 },
    { title: 'Python for Data Science', progress: 12, lastLesson: 'NumPy Basics', totalHours: 30, completedHours: 3.6 },
  ];

  return (
    <div className="min-h-screen bg-[#FAFAFA]">
      <div className="mx-auto max-w-[1000px] px-6 py-8">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-[#1A1A1A]">Welcome back, Alex</h1>
            <p className="mt-1 text-sm text-[#6A6F73]">Keep up the great work!</p>
          </div>
          <div className="flex items-center gap-6">
            <div className="text-center">
              <p className="text-2xl font-bold text-[#E59819]">7</p>
              <p className="text-xs text-[#6A6F73]">Day streak</p>
            </div>
            <div className="text-center">
              <p className="text-2xl font-bold text-[#5624D0]">85%</p>
              <p className="text-xs text-[#6A6F73]">Weekly goal</p>
            </div>
          </div>
        </div>

        {/* Continue Learning */}
        <section className="mt-8">
          <h2 className="text-lg font-bold text-[#1A1A1A]">Continue learning</h2>
          <div className="mt-4 rounded-xl bg-white p-6 shadow-sm">
            <div className="flex items-center gap-6">
              <div className="h-20 w-32 flex-shrink-0 rounded-lg bg-gray-200" />
              <div className="flex-1">
                <h3 className="text-base font-semibold text-[#1A1A1A]">{courses[0].title}</h3>
                <p className="mt-1 text-sm text-[#6A6F73]">Next: {courses[0].lastLesson}</p>
                <div className="mt-3 flex items-center gap-3">
                  <div className="flex-1 h-2 rounded-full bg-gray-200">
                    <div className="h-full rounded-full bg-[#5624D0]" style={{ width: `${courses[0].progress}%` }} />
                  </div>
                  <span className="text-sm font-medium text-[#5624D0]">{courses[0].progress}%</span>
                </div>
              </div>
              <button className="rounded-lg bg-[#5624D0] px-6 py-3 text-sm font-medium text-white hover:bg-[#4815B5]">
                Continue
              </button>
            </div>
          </div>
        </section>

        {/* Active Courses */}
        <section className="mt-8">
          <h2 className="text-lg font-bold text-[#1A1A1A]">My courses</h2>
          <div className="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {courses.map((c) => (
              <div key={c.title} className="rounded-xl bg-white p-5 shadow-sm hover:shadow-md transition-shadow cursor-pointer">
                <div className="aspect-[16/9] rounded-lg bg-gray-200" />
                <h3 className="mt-3 text-sm font-semibold text-[#1A1A1A] line-clamp-2">{c.title}</h3>
                <div className="mt-3 flex items-center gap-2">
                  <div className="flex-1 h-1.5 rounded-full bg-gray-200">
                    <div className="h-full rounded-full bg-[#5624D0]" style={{ width: `${c.progress}%` }} />
                  </div>
                  <span className="text-xs font-medium text-[#6A6F73]">{c.progress}%</span>
                </div>
                <p className="mt-2 text-xs text-[#6A6F73]">{c.completedHours}h / {c.totalHours}h completed</p>
              </div>
            ))}
          </div>
        </section>

        {/* Achievements */}
        <section className="mt-8">
          <h2 className="text-lg font-bold text-[#1A1A1A]">Achievements</h2>
          <div className="mt-4 flex gap-4 overflow-x-auto pb-2">
            {[
              { name: '7-Day Streak', icon: 'fire', earned: true },
              { name: 'First Course', icon: 'trophy', earned: true },
              { name: 'Night Owl', icon: 'moon', earned: true },
              { name: '100 Hours', icon: 'clock', earned: false },
              { name: 'Completionist', icon: 'star', earned: false },
            ].map((badge) => (
              <div key={badge.name} className={`flex flex-col items-center gap-2 rounded-xl p-4 ${badge.earned ? 'bg-white shadow-sm' : 'bg-gray-100 opacity-50'}`}>
                <div className={`flex h-12 w-12 items-center justify-center rounded-full ${badge.earned ? 'bg-[#ECEB98]' : 'bg-gray-200'}`}>
                  <span className="text-lg">{badge.icon}</span>
                </div>
                <span className="text-xs font-medium text-[#1A1A1A] whitespace-nowrap">{badge.name}</span>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
```

---

## 9. Lesson / Content Viewer

### Block Sequence
1. Lesson header (course title, section, lesson name)
2. Video player (or interactive content area)
3. Lesson tabs (Overview, Notes, Resources, Discussion)
4. Curriculum sidebar (collapsible, shows progress per section)
5. Navigation (previous/next lesson)
6. Mark as complete button

### Engagement Patterns
- Auto-advance to next lesson on completion
- Progress auto-saves
- Note-taking synced to video timestamp
- Discussion questions at end of lesson
- Completion celebration animation

```tsx
export function LessonViewer() {
  return (
    <div className="flex h-screen bg-[#1A1A1A]">
      {/* Curriculum Sidebar */}
      <aside className="hidden w-80 overflow-y-auto border-r border-gray-800 bg-[#1A1A1A] lg:block">
        <div className="p-4">
          <a href="#" className="text-sm text-[#6A6F73] hover:text-white">Back to course</a>
          <h2 className="mt-4 text-base font-bold text-white">Complete React Developer</h2>
          <div className="mt-2 flex items-center gap-2">
            <div className="flex-1 h-1.5 rounded-full bg-gray-700">
              <div className="h-full w-[68%] rounded-full bg-[#5624D0]" />
            </div>
            <span className="text-xs text-[#6A6F73]">68%</span>
          </div>
        </div>
        <nav className="mt-2">
          {['Fundamentals', 'Hooks', 'State Management', 'Testing'].map((section, si) => (
            <details key={section} open={si === 1}>
              <summary className="flex items-center justify-between px-4 py-3 text-sm font-medium text-white cursor-pointer hover:bg-white/5">
                <span>Section {si + 1}: {section}</span>
                <span className="text-xs text-[#6A6F73]">3/5</span>
              </summary>
              <div className="space-y-1 px-2 pb-2">
                {['Lesson 1', 'Lesson 2', 'Lesson 3', 'Lesson 4', 'Lesson 5'].map((lesson, li) => (
                  <button key={lesson} className={`flex w-full items-center gap-3 rounded-lg px-4 py-2.5 text-left text-sm ${
                    si === 1 && li === 2 ? 'bg-[#5624D0] text-white' : li < 3 ? 'text-[#6A6F73]' : 'text-[#6A6F73]'
                  }`}>
                    <span className={`flex h-5 w-5 items-center justify-center rounded-full text-[10px] ${
                      li < 3 && si < 1 ? 'bg-[#1AA053] text-white' : 'border border-[#6A6F73]'
                    }`}>
                      {li < 3 && si < 1 ? 'check' : ''}
                    </span>
                    {lesson}
                  </button>
                ))}
              </div>
            </details>
          ))}
        </nav>
      </aside>

      {/* Main Content */}
      <div className="flex flex-1 flex-col">
        {/* Video */}
        <div className="aspect-video w-full bg-black flex items-center justify-center">
          <span className="text-white/30">Video Player</span>
        </div>

        {/* Lesson Content */}
        <div className="flex-1 overflow-y-auto bg-white">
          <div className="mx-auto max-w-[800px] px-6 py-8">
            <div className="flex items-center justify-between">
              <h1 className="text-xl font-bold text-[#1A1A1A]">useEffect Deep Dive</h1>
              <button className="rounded-lg bg-[#1AA053] px-4 py-2 text-sm font-medium text-white hover:bg-[#158F45]">
                Mark Complete
              </button>
            </div>

            {/* Tabs */}
            <div className="mt-6 flex gap-6 border-b border-gray-200">
              {['Overview', 'Notes', 'Resources', 'Discussion (24)'].map((tab, i) => (
                <button key={tab} className={`pb-3 text-sm font-medium ${i === 0 ? 'border-b-2 border-[#5624D0] text-[#5624D0]' : 'text-[#6A6F73]'}`}>
                  {tab}
                </button>
              ))}
            </div>

            <div className="mt-6 prose text-[15px] leading-relaxed text-[#6A6F73]">
              <p>Lesson overview content explaining the key concepts covered in this lesson...</p>
            </div>

            {/* Navigation */}
            <div className="mt-10 flex items-center justify-between border-t border-gray-200 pt-6">
              <a href="#" className="text-sm font-medium text-[#5624D0]">Previous: useState Patterns</a>
              <a href="#" className="rounded-lg bg-[#5624D0] px-4 py-2 text-sm font-medium text-white">Next: Custom Hooks</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

## 10. Assessment / Quiz Flow

### Block Sequence
1. Quiz header (title, question count, timer if timed)
2. Question display (text + options or interactive)
3. Answer selection (radio for single, checkbox for multi)
4. Navigation (previous, next, submit)
5. Progress indicator (question X of Y)
6. Results screen (score, correct/incorrect review, recommendations)

### Engagement Patterns
- Immediate feedback option (after each question or at end)
- Progress bar showing questions completed
- Encouraging messages between sections
- Detailed explanations for wrong answers
- Retry option with shuffled questions
- Certificate generation on passing

```tsx
import { useState } from 'react';

export function QuizFlow() {
  const [current, setCurrent] = useState(0);
  const [answers, setAnswers] = useState<Record<number, number>>({});
  const [submitted, setSubmitted] = useState(false);

  const questions = [
    {
      text: 'Which hook is used for side effects in React?',
      options: ['useState', 'useEffect', 'useContext', 'useReducer'],
      correct: 1,
    },
    {
      text: 'What does the dependency array in useEffect control?',
      options: ['Component styling', 'When the effect re-runs', 'State initialization', 'Component mounting'],
      correct: 1,
    },
    {
      text: 'Which is true about custom hooks?',
      options: ['They must return JSX', 'They must start with "use"', 'They cannot use other hooks', 'They must be async'],
      correct: 1,
    },
  ];

  const totalQuestions = questions.length;
  const q = questions[current];

  if (submitted) {
    const correct = Object.entries(answers).filter(([idx, ans]) => questions[Number(idx)].correct === ans).length;
    const pct = Math.round((correct / totalQuestions) * 100);
    const passed = pct >= 70;

    return (
      <div className="min-h-screen bg-[#FAFAFA] flex items-center justify-center">
        <div className="w-full max-w-[560px] rounded-2xl bg-white p-10 shadow-sm text-center">
          <div className={`mx-auto flex h-20 w-20 items-center justify-center rounded-full ${passed ? 'bg-[#F0FDF4]' : 'bg-[#FEF2F2]'}`}>
            <span className={`text-3xl ${passed ? 'text-[#1AA053]' : 'text-[#DC2626]'}`}>{passed ? 'check' : 'x'}</span>
          </div>
          <h1 className="mt-6 text-2xl font-bold text-[#1A1A1A]">{passed ? 'Congratulations!' : 'Keep practicing'}</h1>
          <p className="mt-2 text-sm text-[#6A6F73]">You scored {correct} out of {totalQuestions} ({pct}%)</p>
          <div className="mt-6 flex justify-center gap-3">
            <button onClick={() => { setSubmitted(false); setCurrent(0); setAnswers({}); }} className="rounded-lg border border-gray-200 px-4 py-2 text-sm font-medium text-[#1A1A1A]">
              Retry
            </button>
            <button className="rounded-lg bg-[#5624D0] px-4 py-2 text-sm font-medium text-white">
              Continue Course
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#FAFAFA]">
      <div className="mx-auto max-w-[680px] px-6 py-10">
        {/* Progress */}
        <div className="flex items-center justify-between">
          <span className="text-sm text-[#6A6F73]">Question {current + 1} of {totalQuestions}</span>
          <span className="text-sm font-medium text-[#5624D0]">{Math.round(((current) / totalQuestions) * 100)}% complete</span>
        </div>
        <div className="mt-2 h-2 rounded-full bg-gray-200">
          <div className="h-full rounded-full bg-[#5624D0] transition-all" style={{ width: `${((current) / totalQuestions) * 100}%` }} />
        </div>

        {/* Question */}
        <div className="mt-10 rounded-2xl bg-white p-8 shadow-sm">
          <h2 className="text-lg font-semibold text-[#1A1A1A]">{q.text}</h2>
          <div className="mt-6 space-y-3">
            {q.options.map((opt, oi) => (
              <button key={oi} onClick={() => setAnswers({ ...answers, [current]: oi })}
                className={`flex w-full items-center gap-4 rounded-xl border p-4 text-left transition-colors ${
                  answers[current] === oi
                    ? 'border-[#5624D0] bg-[#5624D0]/5'
                    : 'border-gray-200 hover:border-gray-400'
                }`}>
                <div className={`flex h-8 w-8 items-center justify-center rounded-full border-2 text-sm font-medium ${
                  answers[current] === oi ? 'border-[#5624D0] bg-[#5624D0] text-white' : 'border-gray-300 text-gray-500'
                }`}>
                  {String.fromCharCode(65 + oi)}
                </div>
                <span className="text-sm text-[#1A1A1A]">{opt}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Navigation */}
        <div className="mt-8 flex items-center justify-between">
          {current > 0 ? (
            <button onClick={() => setCurrent(current - 1)} className="text-sm font-medium text-[#5624D0]">Previous</button>
          ) : <span />}
          {current < totalQuestions - 1 ? (
            <button onClick={() => setCurrent(current + 1)} className="rounded-lg bg-[#5624D0] px-6 py-3 text-sm font-medium text-white hover:bg-[#4815B5]" disabled={answers[current] === undefined}>
              Next
            </button>
          ) : (
            <button onClick={() => setSubmitted(true)} className="rounded-lg bg-[#1AA053] px-6 py-3 text-sm font-medium text-white hover:bg-[#158F45]" disabled={answers[current] === undefined}>
              Submit Quiz
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
```

---

## Cross-Template Summary

### Healthcare Pages
| Page | Key Pattern | Accessibility Priority |
|---|---|---|
| Dashboard | Quick actions, health summary cards | Skip nav, ARIA landmarks, 7:1 contrast |
| Booking | Calendar + time slot picker | Keyboard calendar, available/unavailable announcements |
| Records | Tabbed data viewer | Table scope, HIPAA consent, screen reader compatible |
| Telemedicine | Video call + side panel | Large controls, captions, keyboard accessible |
| Medications | Card list with refill actions | Warning icons + text (not color alone), large text |

### Education Pages
| Page | Key Pattern | Engagement Priority |
|---|---|---|
| Catalog | Search + grid with ratings | Social proof, badges, price anchoring |
| Detail | Curriculum + reviews | Preview lessons, enrollment count, guarantee |
| Dashboard | Progress + streaks | Streak counter, achievements, continue learning |
| Lesson | Video + sidebar curriculum | Auto-save, completion animation, note-taking |
| Quiz | Question + option select | Progress bar, immediate feedback, retry |

---

## Implementation Notes

### Healthcare Accessibility Checklist
- [ ] All pages pass WAVE accessibility evaluation
- [ ] All pages pass axe-core automated testing
- [ ] Keyboard navigation tested (Tab, Shift+Tab, Enter, Escape)
- [ ] Screen reader tested (VoiceOver, NVDA)
- [ ] Color contrast meets WCAG 2.2 AA (4.5:1 text, 3:1 UI)
- [ ] All form inputs have visible labels
- [ ] All images have alt text
- [ ] Focus indicators visible on all interactive elements
- [ ] Page works at 200% zoom without horizontal scroll
- [ ] Skip navigation link present

### Education Engagement Checklist
- [ ] Progress is visible on every surface
- [ ] Celebrations on milestones (course complete, streak milestones)
- [ ] Streak counter encourages daily return
- [ ] Social proof present (enrollment counts, ratings)
- [ ] Clear next action always visible
- [ ] Retry/practice options after assessment failure
