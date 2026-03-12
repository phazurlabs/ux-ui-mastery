# Error & Success Message Templates

> 200+ production-ready error and success message templates. Every template includes headline, body text, recovery action, tone, and ARIA live region announcement.

## Error Message Anatomy

Every error message should follow this structure:

```
[What happened]  — Headline (brief, specific)
[Why it happened] — Body (optional, when useful)
[What to do next] — Recovery action (always present)
```

**Rules:**
- Never blame the user: "We couldn't process that" not "You made an error"
- Be specific: "Password must be at least 8 characters" not "Invalid password"
- Always provide a next step: a button, a link, or clear instructions
- Use `aria-live="assertive"` for errors, `role="alert"` for critical ones

---

## 1. Validation Errors (Form Fields)

### Required Fields

| # | Field | Error Message | Helper Text (Preventive) | ARIA |
|---|-------|--------------|--------------------------|------|
| 1 | Generic | "This field is required" | "Required" | assertive |
| 2 | Email | "Enter your email address" | "We'll use this to sign you in" | assertive |
| 3 | Password | "Enter a password" | "Must be at least 8 characters" | assertive |
| 4 | Name | "Enter your name" | "This is how others will see you" | assertive |
| 5 | Phone | "Enter your phone number" | "We'll only use this for account recovery" | assertive |
| 6 | Address | "Enter your address" | "Used for shipping and billing" | assertive |
| 7 | Payment | "Enter your card number" | "We accept Visa, Mastercard, and Amex" | assertive |
| 8 | Date | "Select a date" | "Choose an available date" | assertive |
| 9 | File | "Choose a file to upload" | "Accepted: JPG, PNG, PDF (max 10 MB)" | assertive |
| 10 | Checkbox | "You must agree to continue" | — | assertive |

### Format Validation

| # | Field | Error Message | Example of Valid | ARIA |
|---|-------|--------------|-----------------|------|
| 11 | Email | "That doesn't look like an email address" | "name@example.com" | assertive |
| 12 | Email (specific) | "Check your email — it might be missing an @" | "name@example.com" | assertive |
| 13 | Phone | "Enter a valid phone number" | "+1 (555) 123-4567" | assertive |
| 14 | URL | "Enter a valid URL" | "https://example.com" | assertive |
| 15 | ZIP/Postal | "Enter a valid ZIP code" | "90210 or 90210-1234" | assertive |
| 16 | Credit card | "Check your card number" | "16 digits on the front of your card" | assertive |
| 17 | CVV | "Enter a valid security code" | "3 digits on the back of your card" | assertive |
| 18 | Expiry date | "Enter a valid expiration date" | "MM/YY" | assertive |
| 19 | Date format | "Use the format MM/DD/YYYY" | "03/15/2026" | assertive |
| 20 | Number | "Enter a number" | "Whole numbers only" | assertive |
| 21 | Currency | "Enter a valid amount" | "$0.00 or greater" | assertive |

### Length & Range Validation

| # | Context | Error Message | ARIA |
|---|---------|--------------|------|
| 22 | Password too short | "Password must be at least 8 characters" | assertive |
| 23 | Password too long | "Password can't exceed 128 characters" | assertive |
| 24 | Username too short | "Username must be at least 3 characters" | assertive |
| 25 | Username too long | "Username can't exceed 30 characters" | assertive |
| 26 | Text too long | "Keep it under 280 characters" | assertive |
| 27 | Bio too long | "Bio must be 160 characters or fewer" | assertive |
| 28 | Min value | "Value must be at least 1" | assertive |
| 29 | Max value | "Value can't exceed 1,000" | assertive |
| 30 | Date too early | "Choose a date after today" | assertive |
| 31 | Date too late | "Choose a date within the next 90 days" | assertive |
| 32 | File too large | "File must be under 10 MB" | assertive |
| 33 | File too small | "Image must be at least 400x400 pixels" | assertive |
| 34 | Too few items | "Select at least one option" | assertive |
| 35 | Too many items | "You can select up to 5 items" | assertive |

### Password Strength

| # | Context | Error Message | ARIA |
|---|---------|--------------|------|
| 36 | Weak password | "Choose a stronger password. Add numbers or symbols." | assertive |
| 37 | Common password | "This password is too common. Try something more unique." | assertive |
| 38 | Contains username | "Your password can't contain your username" | assertive |
| 39 | Same as old | "New password must be different from your current password" | assertive |
| 40 | Mismatch | "Passwords don't match" | assertive |

### Uniqueness & Availability

| # | Context | Error Message | Recovery | ARIA |
|---|---------|--------------|----------|------|
| 41 | Email taken | "An account with this email already exists" | [Sign in instead] | assertive |
| 42 | Username taken | "This username is taken" | Suggest alternatives | assertive |
| 43 | Slug taken | "This URL is already in use. Try a different one." | — | assertive |
| 44 | Duplicate entry | "This item already exists" | [View existing] | assertive |
| 45 | Domain taken | "This domain is not available" | [Search again] | assertive |

---

## 2. System Errors

### Network & Connectivity

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 46 | "No internet connection" | "Check your connection and try again." | [Try again] | Calm |
| 47 | "You're offline" | "We'll sync your changes when you're back online." | — | Reassuring |
| 48 | "Connection lost" | "We're trying to reconnect..." | [Reconnect now] | Patient |
| 49 | "Slow connection" | "This is taking longer than usual. Hang tight." | [Cancel] | Patient |
| 50 | "Can't reach the server" | "Our servers might be temporarily unavailable." | [Try again] [Check status] | Honest |

### Server Errors

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 51 | "Something went wrong" | "We're looking into it. Try again in a moment." | [Try again] | Apologetic |
| 52 | "We hit a snag" | "This wasn't supposed to happen. We've been notified." | [Try again] [Contact support] | Honest |
| 53 | "Couldn't load this page" | "A temporary issue on our end. Please refresh." | [Refresh] | Calm |
| 54 | "Service temporarily unavailable" | "We're doing some maintenance. We'll be back shortly." | [Check status] | Informative |
| 55 | "Scheduled maintenance" | "We're upgrading things. Back by 2:00 PM EST." | [View status page] | Transparent |
| 56 | "This feature isn't available right now" | "We're working on a fix. Try again later." | [Try again later] | Calm |

### Timeout & Rate Limiting

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 57 | "Request timed out" | "The server took too long to respond." | [Try again] | Neutral |
| 58 | "Taking longer than expected" | "You can wait or try again." | [Keep waiting] [Try again] | Patient |
| 59 | "Too many requests" | "You're doing that too often. Wait a moment and try again." | [Try again in 30s] | Calm |
| 60 | "Slow down" | "For security, we limit how often you can do this." | Auto-retry countdown | Explanatory |
| 61 | "Rate limit reached" | "You've hit the limit for this action today." | [Upgrade for more] | Informative |

### Data & Sync Errors

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 62 | "Couldn't save your changes" | "Check your connection and try again." | [Try again] | Calm |
| 63 | "Sync failed" | "Some changes haven't synced yet. We'll keep trying." | [Sync now] | Reassuring |
| 64 | "Conflict detected" | "Someone else edited this. Review their changes." | [Review changes] | Informative |
| 65 | "This version is outdated" | "A newer version is available." | [Refresh] | Informative |
| 66 | "Couldn't load your data" | "There was a problem fetching your information." | [Retry] | Calm |
| 67 | "Import failed" | "The file format isn't supported or the file is corrupted." | [Try a different file] | Helpful |
| 68 | "Export failed" | "We couldn't generate your export. Try again." | [Try again] | Calm |

---

## 3. Permission & Access Errors

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 69 | "You don't have access" | "Ask your admin for permission to view this." | [Request access] | Neutral |
| 70 | "Permission denied" | "You don't have the right role for this action." | [Contact admin] | Neutral |
| 71 | "This content is private" | "Only members of this workspace can see it." | [Request to join] | Informative |
| 72 | "Your session expired" | "Sign in again to continue where you left off." | [Sign in] | Calm |
| 73 | "You've been signed out" | "For your security, we signed you out after inactivity." | [Sign in again] | Explanatory |
| 74 | "Account locked" | "Too many failed sign-in attempts. Try again in 30 minutes." | [Reset password] | Serious |
| 75 | "Account suspended" | "Contact support for more information." | [Contact support] | Serious |
| 76 | "Invitation expired" | "This invite link is no longer valid." | [Request new invite] | Informative |
| 77 | "Link expired" | "This link has expired. Request a new one." | [Resend link] | Calm |
| 78 | "Feature not available on your plan" | "Upgrade to access this feature." | [View plans] | Informative |
| 79 | "Trial ended" | "Your free trial has expired. Subscribe to continue." | [View plans] | Direct |
| 80 | "Verification required" | "Verify your email to access this feature." | [Resend verification] | Instructional |

---

## 4. Business Logic Errors

### Account & Profile

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 81 | "Email already in use" | "An account with this email already exists." | [Sign in] [Reset password] | Helpful |
| 82 | "Username not available" | "Try adding numbers or a different variation." | Inline suggestions | Helpful |
| 83 | "Profile incomplete" | "Add a profile photo and bio to continue." | [Complete profile] | Guiding |
| 84 | "Account not found" | "We couldn't find an account with that email." | [Create account] | Helpful |

### Payment & Billing

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 85 | "Payment declined" | "Your card was declined. Try a different payment method." | [Update payment] | Calm |
| 86 | "Card expired" | "The card on file has expired. Update your payment method." | [Update card] | Informative |
| 87 | "Insufficient funds" | "This payment couldn't be processed. Try a different card." | [Try different card] | Discreet |
| 88 | "Invalid coupon" | "This coupon code isn't valid or has expired." | [Remove coupon] | Neutral |
| 89 | "Coupon expired" | "This coupon is no longer active." | [Continue without coupon] | Neutral |
| 90 | "Billing address mismatch" | "The billing address doesn't match the card on file." | [Update address] | Informative |
| 91 | "Payment processing error" | "We couldn't process your payment. You haven't been charged." | [Try again] | Reassuring |
| 92 | "Refund failed" | "We couldn't process your refund. Contact support." | [Contact support] | Apologetic |

### Inventory & Availability

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 93 | "Out of stock" | "This item is currently unavailable." | [Notify me] [View similar] | Informative |
| 94 | "Limited stock" | "Only 2 left. Order soon." | [Add to cart] | Urgent |
| 95 | "Item no longer available" | "This product has been discontinued." | [View alternatives] | Honest |
| 96 | "Quantity limit reached" | "Maximum 5 per customer." | — | Informative |
| 97 | "Service area unavailable" | "We don't deliver to this location yet." | [Change address] [Get notified] | Honest |
| 98 | "Time slot taken" | "This slot was just booked. Choose another time." | [View available times] | Calm |
| 99 | "Event sold out" | "All tickets have been claimed." | [Join waitlist] | Honest |
| 100 | "Booking conflict" | "You already have something scheduled at this time." | [View calendar] | Helpful |

### Limits & Quotas

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 101 | "Storage full" | "You've used all your storage. Free up space or upgrade." | [Manage storage] [Upgrade] | Informative |
| 102 | "Plan limit reached" | "You've reached the limit for your current plan." | [Upgrade plan] | Informative |
| 103 | "Team seats full" | "Your plan allows 5 members. Upgrade for more." | [Upgrade] [Manage team] | Informative |
| 104 | "API limit reached" | "You've exceeded your API quota for this period." | [View usage] [Upgrade] | Technical |
| 105 | "File limit reached" | "You can upload up to 10 files at a time." | [Remove some files] | Informative |
| 106 | "Daily limit reached" | "You've hit your daily limit. Resets at midnight." | [View limits] | Informative |
| 107 | "Character limit exceeded" | "Your message is too long. Shorten it by 50 characters." | — | Specific |

### Content & Upload Errors

| # | Headline | Body | Recovery | Tone |
|---|----------|------|----------|------|
| 108 | "File type not supported" | "Upload a JPG, PNG, or PDF file." | [Choose different file] | Helpful |
| 109 | "File too large" | "Max file size is 25 MB. Your file is 32 MB." | [Compress file] [Choose different] | Specific |
| 110 | "Upload failed" | "Something went wrong during upload. Try again." | [Try again] | Calm |
| 111 | "Image too small" | "Minimum size is 800x600 pixels." | [Choose larger image] | Specific |
| 112 | "Content flagged" | "This content may violate our community guidelines." | [Edit content] [Learn more] | Serious |
| 113 | "Duplicate content" | "This has already been posted." | [View original] | Neutral |
| 114 | "Processing failed" | "We couldn't process this file. Try a different format." | [Try different format] | Helpful |

---

## 5. Success Messages

### Account & Authentication

| # | Headline | Body | Next Action | Tone | ARIA |
|---|----------|------|------------|------|------|
| 115 | "Account created" | "Welcome! Check your email to verify your account." | [Continue to dashboard] | Warm | polite |
| 116 | "Welcome back" | "You're signed in." | Auto-redirect | Warm | polite |
| 117 | "Email verified" | "Your email has been confirmed. You're all set." | [Go to dashboard] | Affirming | polite |
| 118 | "Password updated" | "Your new password is active." | [Continue] | Reassuring | polite |
| 119 | "Password reset email sent" | "Check your inbox for a reset link." | [Open email app] | Helpful | polite |
| 120 | "Two-factor enabled" | "Your account is now more secure." | [Done] | Reassuring | polite |
| 121 | "Profile updated" | "Your changes have been saved." | — | Brief | polite |
| 122 | "Account deleted" | "Your account and data have been removed." | [Go to homepage] | Neutral | polite |

### Content & Data

| # | Headline | Body | Next Action | Tone | ARIA |
|---|----------|------|------------|------|------|
| 123 | "Saved" | — | — (inline) | Minimal | polite |
| 124 | "Changes saved" | "All your changes are up to date." | — | Brief | polite |
| 125 | "Draft saved" | "You can find this in your drafts." | [View drafts] | Helpful | polite |
| 126 | "Published" | "Your post is now live." | [View post] | Affirming | polite |
| 127 | "File uploaded" | "1 file uploaded successfully." | [View file] | Brief | polite |
| 128 | "3 files uploaded" | "All files uploaded successfully." | [View files] | Brief | polite |
| 129 | "Import complete" | "142 records imported successfully." | [View records] | Specific | polite |
| 130 | "Export ready" | "Your export is ready to download." | [Download] | Helpful | polite |
| 131 | "Copied to clipboard" | — | — (toast) | Minimal | polite |
| 132 | "Link copied" | "Share it with anyone." | — (toast) | Brief | polite |
| 133 | "Moved to trash" | "Item will be permanently deleted in 30 days." | [Undo] | Informative | polite |
| 134 | "Restored" | "Item has been moved back to its original location." | [View item] | Brief | polite |
| 135 | "Archived" | "Moved to archive." | [Undo] [View archive] | Brief | polite |

### Communication

| # | Headline | Body | Next Action | Tone | ARIA |
|---|----------|------|------------|------|------|
| 136 | "Message sent" | — | — (toast) | Minimal | polite |
| 137 | "Email sent" | "We've sent your message to alex@example.com." | — | Confirming | polite |
| 138 | "Invitation sent" | "We've invited 3 people to your workspace." | [View pending] | Specific | polite |
| 139 | "Feedback submitted" | "Thanks for your feedback. We read every response." | [Done] | Grateful | polite |
| 140 | "Report submitted" | "We'll review this and take appropriate action." | [Done] | Serious | polite |
| 141 | "Comment posted" | — | — (inline) | Minimal | polite |
| 142 | "Reply sent" | — | — (inline) | Minimal | polite |

### Commerce & Payment

| # | Headline | Body | Next Action | Tone | ARIA |
|---|----------|------|------------|------|------|
| 143 | "Order placed" | "Order #12345 confirmed. We'll email you tracking details." | [View order] [Continue shopping] | Affirming | polite |
| 144 | "Payment successful" | "Your payment of $49.99 has been processed." | [View receipt] | Reassuring | polite |
| 145 | "Subscription activated" | "Welcome to the Pro plan. Your next billing date is April 12." | [Explore features] | Welcoming | polite |
| 146 | "Subscription cancelled" | "Your subscription will remain active until March 31." | [Reactivate] | Neutral | polite |
| 147 | "Refund processed" | "Your refund of $29.99 will appear in 5-10 business days." | [View details] | Reassuring | polite |
| 148 | "Coupon applied" | "You saved $10 with code SAVE10." | — | Celebratory | polite |
| 149 | "Card updated" | "Your payment method has been updated." | [Done] | Brief | polite |
| 150 | "Shipping address updated" | "Your new address will be used for future orders." | [Done] | Brief | polite |
| 151 | "Added to cart" | "1 item added to your cart." | [View cart] [Continue shopping] | Brief | polite |
| 152 | "Item removed from cart" | — | [Undo] | Brief | polite |
| 153 | "Wishlist updated" | "Saved to your wishlist." | [View wishlist] | Brief | polite |

### Team & Collaboration

| # | Headline | Body | Next Action | Tone | ARIA |
|---|----------|------|------------|------|------|
| 154 | "Team member added" | "Alex has been added to the Marketing workspace." | [View team] | Specific | polite |
| 155 | "Team member removed" | "Alex has been removed from the workspace." | [Undo] | Neutral | polite |
| 156 | "Role updated" | "Alex is now an Admin." | — | Brief | polite |
| 157 | "Workspace created" | "Your workspace is ready. Start by inviting your team." | [Invite team] | Encouraging | polite |
| 158 | "Project created" | "Your project is set up. Add tasks to get started." | [Add first task] | Encouraging | polite |
| 159 | "Task completed" | "Nice work! 4 tasks remaining in this project." | — | Motivating | polite |
| 160 | "Assignment updated" | "This task is now assigned to Alex." | — | Brief | polite |

### Settings & Configuration

| # | Headline | Body | Next Action | Tone | ARIA |
|---|----------|------|------------|------|------|
| 161 | "Settings saved" | "Your preferences have been updated." | — | Brief | polite |
| 162 | "Notifications updated" | "Your notification preferences are saved." | — | Brief | polite |
| 163 | "Integration connected" | "Slack is now connected to your workspace." | [Configure] | Affirming | polite |
| 164 | "Integration disconnected" | "Slack has been disconnected." | [Reconnect] | Neutral | polite |
| 165 | "API key created" | "Copy your key now. It won't be shown again." | [Copy key] | Urgent-important | polite |
| 166 | "Webhook configured" | "Your webhook is active and will receive events." | [Test webhook] | Confirming | polite |
| 167 | "Domain verified" | "Your custom domain is now active." | [View site] | Affirming | polite |
| 168 | "Theme applied" | "Your new theme is active." | — | Brief | polite |

### Scheduling & Booking

| # | Headline | Body | Next Action | Tone | ARIA |
|---|----------|------|------------|------|------|
| 169 | "Appointment confirmed" | "March 15 at 2:00 PM with Dr. Chen." | [Add to calendar] | Specific | polite |
| 170 | "Booking confirmed" | "Your reservation at The Grand Hotel, March 20-22." | [View booking] | Specific | polite |
| 171 | "Event created" | "Your event is on the calendar." | [Share event] [Invite guests] | Encouraging | polite |
| 172 | "Reminder set" | "We'll remind you 30 minutes before." | — | Reassuring | polite |
| 173 | "Appointment rescheduled" | "Moved to March 18 at 3:00 PM." | [View details] | Specific | polite |
| 174 | "Appointment cancelled" | "Your appointment on March 15 has been cancelled." | [Rebook] | Neutral | polite |

---

## 6. Inline Validation Messages (Real-Time)

These appear while the user is still filling out the field:

| # | Context | Message | Type | Timing |
|---|---------|---------|------|--------|
| 175 | Email available | "This email is available" (green check) | Success | After debounce |
| 176 | Username available | "Username is available" (green check) | Success | After debounce |
| 177 | Username taken | "Username is taken" (red) | Error | After debounce |
| 178 | Password strength: weak | "Weak — add numbers or symbols" | Warning | On change |
| 179 | Password strength: fair | "Fair — try making it longer" | Warning | On change |
| 180 | Password strength: strong | "Strong password" (green check) | Success | On change |
| 181 | Passwords match | "Passwords match" (green check) | Success | On change |
| 182 | Character count | "140 / 280 characters" | Info | On change |
| 183 | Approaching limit | "Only 20 characters left" | Warning | On change |
| 184 | Over limit | "30 characters over the limit" | Error | On change |
| 185 | Valid URL detected | "Valid URL" (green check) | Success | On blur |
| 186 | Valid date | "Date is available" | Success | On selection |

---

## 7. Form-Level Error Summaries

When a form has multiple errors, show a summary at the top:

| # | Context | Summary Message |
|---|---------|----------------|
| 187 | Single error | "1 field needs your attention" |
| 188 | Multiple errors | "3 fields need your attention" |
| 189 | Required fields | "Fill in the highlighted fields to continue" |
| 190 | Mixed errors | "Fix the errors below to continue" |
| 191 | Resubmission | "Some fields still need corrections" |
| 192 | Gentle version | "Almost there — just a few things to fix" |

**Accessibility:** The error summary must be focused when shown (`tabindex="-1"` + `focus()`), and each error must link to its field.

---

## 8. Contextual Error Patterns by Sector

### Fintech Errors
| # | Context | Message |
|---|---------|---------|
| 193 | Transfer failed | "Transfer not completed. Your account was not charged. [Try again]" |
| 194 | Insufficient balance | "Not enough funds for this transfer. Available balance: $142.50" |
| 195 | Suspicious activity | "For your security, we've temporarily limited this action. [Verify identity]" |
| 196 | Market closed | "Markets are closed. Your order will be queued for the next trading session." |
| 197 | Compliance block | "We need to verify your identity before processing this transaction. [Complete verification]" |

### Healthcare Errors
| # | Context | Message |
|---|---------|---------|
| 198 | Appointment conflict | "Dr. Chen isn't available at that time. Here are the next available slots." |
| 199 | Insurance not accepted | "This provider doesn't accept your insurance plan. [Find in-network providers]" |
| 200 | Prescription error | "We couldn't process this prescription. Contact your pharmacy for assistance." |
| 201 | Record access denied | "You don't have permission to view this record. [Request access from provider]" |

### E-commerce Errors
| # | Context | Message |
|---|---------|---------|
| 202 | Cart item unavailable | "One item in your cart is no longer available. We've removed it." |
| 203 | Shipping restriction | "We can't ship this item to your address. [Change shipping address]" |
| 204 | Price changed | "The price for this item has changed since you added it to your cart." |
| 205 | Coupon restriction | "This coupon can't be combined with other offers." |

### SaaS Errors
| # | Context | Message |
|---|---------|---------|
| 206 | Workspace limit | "You've reached the project limit for your plan. [Upgrade to create more]" |
| 207 | Integration failure | "We lost the connection to Slack. [Reconnect]" |
| 208 | Concurrent edit | "Alex is editing this document. Your changes will be saved separately." |
| 209 | Build failure | "Deployment failed at step 3: missing environment variable API_KEY. [View logs]" |
| 210 | API error | "The API returned an unexpected response. Check your request format. [View docs]" |

---

## Error Message Tone Guide

| Severity | Tone | Icon | Color | Example |
|----------|------|------|-------|---------|
| Info | Neutral, informative | (i) | Blue | "Your session will expire in 5 minutes" |
| Warning | Cautious, preventive | Triangle | Yellow/Amber | "Unsaved changes will be lost" |
| Error | Empathetic, helpful | Circle-X | Red | "We couldn't save your changes" |
| Critical | Serious, urgent | Shield | Red + Bold | "Your account may be compromised" |
| Success | Warm, affirming | Checkmark | Green | "Changes saved" |

---

## Success Message Duration Guide

| Type | Duration | Auto-dismiss | Reason |
|------|----------|-------------|--------|
| Inline save confirmation | 2-3s | Yes | Low importance, obvious action |
| Toast (non-critical) | 4-6s | Yes | Brief confirmation |
| Toast with undo | 6-8s | Yes (but undo persists) | User may want to reverse |
| Success banner | Persistent until dismissed | No | Important information |
| Redirect confirmation | 1-2s then redirect | Yes | Brief confirmation before navigation |
| Payment/order confirmation | Persistent (full page) | No | High importance, reference information |
