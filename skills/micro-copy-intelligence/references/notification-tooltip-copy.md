# Notification, Tooltip, and Contextual Help Templates

> 200+ production-ready notification, tooltip, and contextual help templates. Every template includes text, character limits, tone, timing/duration, and accessibility notes.

## Component Reference

| Component | Max Length | Auto-Dismiss | ARIA Role | Use For |
|-----------|-----------|-------------|-----------|---------|
| Push notification | Title: 65 chars, Body: 150 chars | N/A (OS-managed) | N/A | Off-app alerts |
| In-app notification | Title: 65 chars, Body: 150 chars | No (persist until read) | status | In-app alerts and updates |
| Toast | 60 chars | Yes (4-8s) | status or alert | Brief confirmations |
| Tooltip | 80 chars | No (hover/focus) | tooltip | Feature hints, explanations |
| Helper text | 100 chars | No (persistent) | — (aria-describedby) | Form field guidance |
| Confirmation dialog | Title: 50 chars, Body: 180 chars | No (requires action) | alertdialog | Destructive/irreversible actions |
| Loading message | 50 chars | Yes (when loaded) | status | Wait states |
| Changelog entry | Title: 80 chars, Body: 250 chars | No | — | Feature updates |

---

## 1. Push Notifications

### Transactional

| # | Title | Body | Tone | When to Send |
|---|-------|------|------|-------------|
| 1 | "Order confirmed" | "Your order #12345 is confirmed. We'll notify you when it ships." | Reassuring | Immediately after purchase |
| 2 | "Your order has shipped" | "Order #12345 is on its way. Expected delivery: March 15." | Informative | When shipped |
| 3 | "Delivery arriving today" | "Your package will arrive between 2-5 PM." | Helpful | Morning of delivery |
| 4 | "Payment received" | "We received your payment of $49.99. View your receipt." | Confirming | After payment processes |
| 5 | "Password changed" | "Your password was just updated. If this wasn't you, contact support." | Security | Immediately |
| 6 | "New sign-in detected" | "A new device signed into your account from San Francisco." | Security | Immediately |
| 7 | "Subscription renewed" | "Your Pro plan renewed for $9.99/mo. Next billing: April 12." | Informative | On renewal |
| 8 | "Receipt available" | "Your receipt for $49.99 is ready to view." | Neutral | After transaction |
| 9 | "Appointment reminder" | "Your appointment with Dr. Chen is tomorrow at 2:00 PM." | Helpful | 24 hours before |
| 10 | "Booking confirmed" | "Your reservation at The Grand Hotel, March 20-22, is confirmed." | Affirming | Immediately |

### Social and Communication

| # | Title | Body | Tone | When to Send |
|---|-------|------|------|-------------|
| 11 | "Alex mentioned you" | "'...what do you think about the new design?'" | Social | Immediately |
| 12 | "New message from Alex" | "Hey, can you review the latest draft?" | Personal | Immediately |
| 13 | "Alex liked your post" | "Your post about design systems got a like." | Social | Batched (hourly) |
| 14 | "3 new comments on your post" | "Alex, Jordan, and Sam commented on your update." | Social | Batched |
| 15 | "Alex accepted your invitation" | "Alex joined your workspace. Say hello!" | Encouraging | Immediately |
| 16 | "New follower" | "Alex started following you." | Social | Batched |
| 17 | "You have 5 unread messages" | "Catch up on conversations from your team." | Informative | After 4+ hours |
| 18 | "Alex shared a file with you" | "Q4 Report.pdf was shared to the Design workspace." | Informative | Immediately |

### Reminders and Alerts

| # | Title | Body | Tone | When to Send |
|---|-------|------|------|-------------|
| 19 | "Task due today" | "Finish the homepage redesign. Due by 5:00 PM." | Urgent | Morning |
| 20 | "Meeting in 15 minutes" | "Design Review with the team. Join the call." | Timely | 15 min before |
| 21 | "Weekly summary ready" | "You completed 12 tasks and closed 3 projects this week." | Motivating | Friday evening |
| 22 | "Don't forget" | "You saved 2 items in your cart. Complete your purchase." | Gentle | 24 hours after cart |
| 23 | "Your trial ends in 3 days" | "Upgrade to keep your workspace and data." | Informative | 3 days before expiry |
| 24 | "Time to check in" | "How's the project going? Update your status." | Encouraging | Weekly |
| 25 | "New content available" | "3 new lessons are ready in your learning path." | Informative | On publish |
| 26 | "Price drop alert" | "An item on your wishlist is now 30% off." | Exciting | On price change |

### Marketing (Opt-In Only)

| # | Title | Body | Tone | When to Send |
|---|-------|------|------|-------------|
| 27 | "Something new for you" | "We just launched [feature]. Check it out." | Exciting | On feature launch |
| 28 | "Your monthly recap" | "Here's what you accomplished in February." | Motivating | First of month |
| 29 | "Limited time offer" | "Get 50% off Pro for the next 48 hours." | Urgent | Campaign start |
| 30 | "We've been improving things" | "Check out 5 new features we shipped this month." | Informative | Monthly |

---

## 2. In-App Notifications

### Informational

| # | Type | Title | Body | Action | Icon |
|---|------|-------|------|--------|------|
| 31 | Info | "System update scheduled" | "Maintenance window: March 15, 2-4 AM EST. Save your work." | View details | Info circle (blue) |
| 32 | Info | "New version available" | "Update to v2.5 for new features and improvements." | Update now | Arrow up (blue) |
| 33 | Info | "Your export is ready" | "Download your CSV export before it expires in 7 days." | Download | File (blue) |
| 34 | Info | "Plan usage: 80%" | "You've used 80% of your storage. Consider upgrading." | Manage storage | Meter (blue) |
| 35 | Info | "New team member" | "Alex joined the Marketing workspace." | View profile | Person (blue) |

### Warning

| # | Type | Title | Body | Action | Icon |
|---|------|-------|------|--------|------|
| 36 | Warning | "Storage almost full" | "You've used 95% of your storage. Free up space or upgrade." | Manage storage | Warning triangle (amber) |
| 37 | Warning | "Payment method expiring" | "Your card ending in 4242 expires next month. Update it." | Update card | Card (amber) |
| 38 | Warning | "Unsaved changes" | "You have unsaved changes. Save before leaving." | Save now | Pencil (amber) |
| 39 | Warning | "Session expiring soon" | "Your session will expire in 5 minutes. Save your work." | Extend session | Clock (amber) |
| 40 | Warning | "API rate limit approaching" | "You've used 90% of your API quota for this hour." | View usage | Meter (amber) |
| 41 | Warning | "Browser not supported" | "Some features may not work. Switch to Chrome, Firefox, or Safari." | Learn more | Browser (amber) |
| 42 | Warning | "Slow connection detected" | "Your internet is slower than usual. Some features may be delayed." | — | Wifi (amber) |

### Error

| # | Type | Title | Body | Action | Icon |
|---|------|-------|------|--------|------|
| 43 | Error | "Sync failed" | "Your latest changes couldn't sync. We'll keep trying." | Retry now | Refresh (red) |
| 44 | Error | "Payment failed" | "We couldn't process your payment. Update your card." | Update payment | Card (red) |
| 45 | Error | "Upload failed" | "2 of 5 files couldn't be uploaded. Try again." | Retry | Upload (red) |
| 46 | Error | "Integration disconnected" | "Your Slack connection was lost. Reconnect to resume." | Reconnect | Plug (red) |
| 47 | Error | "Action failed" | "We couldn't complete that action. Try again." | Retry | X circle (red) |

### Success

| # | Type | Title | Body | Action | Icon |
|---|------|-------|------|--------|------|
| 48 | Success | "Changes published" | "Your updates are now live." | View page | Check (green) |
| 49 | Success | "Team member added" | "Alex now has access to the workspace." | — | Person+ (green) |
| 50 | Success | "Backup complete" | "Your data was backed up successfully." | — | Shield (green) |
| 51 | Success | "Migration complete" | "All your data has been moved to the new system." | View data | Check (green) |

---

## 3. Toast Messages

### Confirmations (Auto-Dismiss: 4-6s)

| # | Message | With Undo | Duration |
|---|---------|-----------|----------|
| 52 | "Saved" | No | 2s |
| 53 | "Changes saved" | No | 3s |
| 54 | "Copied to clipboard" | No | 3s |
| 55 | "Link copied" | No | 3s |
| 56 | "Message sent" | No | 3s |
| 57 | "Email sent" | No | 4s |
| 58 | "File uploaded" | No | 4s |
| 59 | "3 files uploaded" | No | 4s |
| 60 | "Comment posted" | No | 3s |
| 61 | "Settings updated" | No | 3s |
| 62 | "Profile updated" | No | 3s |
| 63 | "Preferences saved" | No | 3s |
| 64 | "Theme applied" | No | 3s |
| 65 | "Notification muted" | Yes: [Undo] | 6s |
| 66 | "Subscription confirmed" | No | 5s |

### Undo Actions (Auto-Dismiss: 6-8s)

| # | Message | Undo CTA | Duration |
|---|---------|----------|----------|
| 67 | "Item deleted" | Undo | 8s |
| 68 | "Moved to trash" | Undo | 8s |
| 69 | "Archived" | Undo | 6s |
| 70 | "Removed from list" | Undo | 6s |
| 71 | "Contact blocked" | Undo | 8s |
| 72 | "Unsubscribed" | Resubscribe | 8s |
| 73 | "Conversation muted" | Undo | 6s |
| 74 | "3 items moved to Archive" | Undo | 8s |
| 75 | "Task marked as complete" | Undo | 6s |
| 76 | "Member removed from team" | Undo | 8s |

### Error Toasts (Persistent or Long Duration)

| # | Message | Action | Duration |
|---|---------|--------|----------|
| 77 | "Couldn't save. Check your connection." | Retry | Persistent |
| 78 | "Failed to send message" | Retry | Persistent |
| 79 | "Upload failed. File too large." | — | 8s |
| 80 | "Action couldn't be completed" | Try again | Persistent |
| 81 | "Connection lost" | — | Persistent until reconnected |
| 82 | "Permission denied" | — | 6s |

---

## 4. Tooltips

### Feature Explanation

| # | Target Element | Tooltip Text | Chars |
|---|---------------|-------------|-------|
| 83 | Settings gear icon | "Account settings and preferences" | 37 |
| 84 | Share button | "Share this with your team or copy a link" | 42 |
| 85 | Archive button | "Move to archive. You can restore it later." | 44 |
| 86 | Pin icon | "Pin to the top of your list" | 28 |
| 87 | Filter icon | "Filter and sort your items" | 28 |
| 88 | Sync indicator | "Last synced 2 minutes ago" | 27 |
| 89 | Collaborator avatar | "Alex Chen — currently editing" | 32 |
| 90 | Status dot (green) | "Online and available" | 21 |
| 91 | Status dot (yellow) | "Away — last active 30 min ago" | 32 |
| 92 | Status dot (red) | "Do not disturb" | 16 |
| 93 | Lock icon | "This item is locked for editing" | 34 |
| 94 | Crown icon | "Workspace owner" | 15 |
| 95 | Star icon | "Add to favorites" | 16 |
| 96 | Download icon | "Download file (2.4 MB)" | 24 |
| 97 | External link icon | "Opens in a new tab" | 20 |
| 98 | Info icon | "Learn more about this feature" | 31 |
| 99 | Notification bell | "3 unread notifications" | 24 |
| 100 | Keyboard shortcut | "Quick search (Cmd+K)" | 22 |

### Shortcut Hints

| # | Action | Tooltip Text | Chars |
|---|--------|-------------|-------|
| 101 | Bold | "Bold (Cmd+B)" | 13 |
| 102 | Italic | "Italic (Cmd+I)" | 15 |
| 103 | Undo | "Undo (Cmd+Z)" | 14 |
| 104 | Redo | "Redo (Cmd+Shift+Z)" | 20 |
| 105 | Save | "Save (Cmd+S)" | 14 |
| 106 | Search | "Search (Cmd+K)" | 16 |
| 107 | New item | "New item (Cmd+N)" | 18 |
| 108 | Delete | "Delete (Backspace)" | 20 |
| 109 | Copy | "Copy (Cmd+C)" | 14 |
| 110 | Paste | "Paste (Cmd+V)" | 15 |
| 111 | Select all | "Select all (Cmd+A)" | 20 |
| 112 | Find | "Find in page (Cmd+F)" | 22 |

### Status Explanation

| # | Status | Tooltip Text | Chars |
|---|--------|-------------|-------|
| 113 | Published | "This page is live and visible to the public" | 46 |
| 114 | Draft | "This is a draft. Only you can see it." | 38 |
| 115 | Pending review | "Waiting for approval from an admin" | 36 |
| 116 | Scheduled | "Scheduled to publish on March 15 at 9:00 AM" | 46 |
| 117 | Archived | "This item is archived. Restore it to make changes." | 51 |
| 118 | Deprecated | "This feature will be removed in the next update" | 49 |
| 119 | Beta | "This feature is in beta. Expect changes." | 42 |
| 120 | Experimental | "Experimental feature. May change or be removed." | 49 |

### Disabled State Explanations

| # | Context | Tooltip Text | Chars |
|---|---------|-------------|-------|
| 121 | No permission | "You need admin access to do this" | 34 |
| 122 | Plan limit | "Available on the Pro plan. Upgrade to unlock." | 47 |
| 123 | Prerequisite | "Complete the previous step first" | 34 |
| 124 | Temporary lock | "This item is being edited by Alex" | 36 |
| 125 | Cooldown | "Try again in 30 seconds" | 24 |
| 126 | Empty selection | "Select at least one item first" | 32 |
| 127 | Form incomplete | "Fill in all required fields to continue" | 42 |
| 128 | Processing | "Processing your previous request..." | 37 |

---

## 5. Helper Text (Form Fields)

### Personal Information

| # | Field | Helper Text | Chars |
|---|-------|-----------|-------|
| 129 | Full name | "As it appears on your official ID" | 35 |
| 130 | Display name | "How others will see you in the app" | 36 |
| 131 | Email | "We'll send account updates here" | 33 |
| 132 | Phone | "Used for account recovery only" | 31 |
| 133 | Date of birth | "We use this to verify your age" | 31 |
| 134 | Address line 1 | "Street address, P.O. box, or company name" | 44 |
| 135 | Address line 2 | "Apartment, suite, unit, or building (optional)" | 49 |
| 136 | Bio | "Tell people about yourself in 160 characters or fewer" | 54 |
| 137 | Website | "Your personal or company website" | 34 |
| 138 | Username | "Letters, numbers, and underscores. 3-30 characters." | 52 |

### Passwords and Security

| # | Field | Helper Text | Chars |
|---|-------|-----------|-------|
| 139 | New password | "At least 8 characters with a mix of letters and numbers" | 56 |
| 140 | Confirm password | "Enter your new password again" | 31 |
| 141 | Current password | "Enter your current password to confirm changes" | 48 |
| 142 | 2FA code | "Enter the 6-digit code from your authenticator app" | 52 |
| 143 | Recovery email | "We'll use this if you lose access to your primary email" | 56 |
| 144 | Security question | "Choose something only you would know" | 38 |

### Content and Settings

| # | Field | Helper Text | Chars |
|---|-------|-----------|-------|
| 145 | Project name | "Choose something descriptive. You can rename later." | 52 |
| 146 | Description | "A brief summary to help others understand this item" | 53 |
| 147 | URL slug | "This will be part of your public URL" | 38 |
| 148 | Tags | "Add tags to make this easier to find. Press Enter after each." | 63 |
| 149 | Category | "Choose the most relevant category" | 35 |
| 150 | Date/time | "All times are shown in your local timezone" | 44 |
| 151 | File upload | "Accepted: JPG, PNG, PDF. Max 10 MB." | 37 |
| 152 | API key name | "A name to help you identify this key later" | 45 |
| 153 | Webhook URL | "The endpoint where we'll send event payloads" | 47 |

### Payment

| # | Field | Helper Text | Chars |
|---|-------|-----------|-------|
| 154 | Card number | "We accept Visa, Mastercard, Amex, and Discover" | 49 |
| 155 | Expiry date | "MM/YY as printed on your card" | 30 |
| 156 | CVV | "3-digit code on the back of your card" | 39 |
| 157 | Billing address | "Must match the address on file with your bank" | 48 |
| 158 | Coupon code | "Enter a promo or discount code" | 31 |

---

## 6. Confirmation Dialogs

### Destructive Actions

| # | Title | Body | Confirm CTA | Cancel CTA |
|---|-------|------|------------|------------|
| 159 | "Delete this project?" | "This will permanently delete the project and all its tasks, files, and comments. This can't be undone." | Delete project | Keep project |
| 160 | "Delete your account?" | "All your data, projects, and settings will be permanently removed. This action cannot be reversed." | Delete my account | Keep my account |
| 161 | "Remove Alex from the team?" | "Alex will lose access to all shared projects and files in this workspace." | Remove Alex | Cancel |
| 162 | "Delete 5 items?" | "These items will be permanently deleted. This can't be undone." | Delete 5 items | Cancel |
| 163 | "Empty trash?" | "All items in trash will be permanently deleted. You won't be able to recover them." | Empty trash | Cancel |
| 164 | "Cancel your subscription?" | "Your Pro features will remain active until March 31. After that, your plan will revert to Free." | Cancel subscription | Keep subscription |
| 165 | "Disconnect Slack?" | "You'll stop receiving notifications in Slack and lose access to shared channels." | Disconnect | Keep connected |
| 166 | "Revoke API key?" | "Any applications using this key will immediately lose access." | Revoke key | Cancel |
| 167 | "Leave this workspace?" | "You'll lose access to all shared projects and data. You can ask to rejoin later." | Leave workspace | Stay |
| 168 | "Clear all data?" | "This will remove all entries from this table. Existing exports won't be affected." | Clear all data | Cancel |

### Irreversible Actions

| # | Title | Body | Confirm CTA | Cancel CTA |
|---|-------|------|------------|------------|
| 169 | "Publish this page?" | "This will make the page visible to everyone. You can unpublish later." | Publish | Cancel |
| 170 | "Send to all subscribers?" | "This email will be sent to 2,450 subscribers. This can't be undone." | Send email | Cancel |
| 171 | "Merge these contacts?" | "This will combine 3 contacts into one record. Individual records can't be restored." | Merge contacts | Cancel |
| 172 | "Finalize this report?" | "Once finalized, this report can't be edited. A PDF will be generated." | Finalize | Cancel |
| 173 | "Process refund?" | "Refund of $29.99 will be issued to the original payment method." | Process refund | Cancel |

### State Change Confirmations

| # | Title | Body | Confirm CTA | Cancel CTA |
|---|-------|------|------------|------------|
| 174 | "Unsaved changes" | "You have unsaved changes. Save before leaving?" | Save and leave | Leave without saving |
| 175 | "Discard this draft?" | "Your draft will be lost. This can't be undone." | Discard draft | Keep editing |
| 176 | "Switch workspace?" | "Unsaved changes in this workspace will be lost." | Switch | Stay here |
| 177 | "Sign out?" | "Make sure your work is saved before signing out." | Sign out | Cancel |
| 178 | "Close without saving?" | "Changes you made won't be saved." | Close | Go back |

### Bulk Action Confirmations

| # | Title | Body | Confirm CTA | Cancel CTA |
|---|-------|------|------------|------------|
| 179 | "Archive 12 items?" | "These items will be moved to the archive. You can restore them later." | Archive 12 items | Cancel |
| 180 | "Move 8 tasks to Done?" | "These tasks will be marked as complete." | Mark as done | Cancel |
| 181 | "Delete 25 messages?" | "These messages will be permanently removed." | Delete 25 messages | Cancel |
| 182 | "Export 1,200 records?" | "This may take a few minutes. We'll notify you when it's ready." | Start export | Cancel |
| 183 | "Reassign 5 tasks to Alex?" | "Alex will be notified about the new assignments." | Reassign | Cancel |

---

## 7. Loading Messages

### Brief Wait (1-3 seconds)

| # | Message | Chars | Context |
|---|---------|-------|---------|
| 184 | "Loading..." | 10 | Generic content load |
| 185 | "Loading your dashboard..." | 26 | Specific page load |
| 186 | "Opening..." | 10 | Opening a file or item |
| 187 | "Preparing..." | 12 | Setup before display |
| 188 | "Connecting..." | 13 | Establishing connection |
| 189 | "Signing you in..." | 18 | Authentication |
| 190 | "Almost ready..." | 15 | Near completion |

### Longer Wait (3-10 seconds)

| # | Message | Chars | Context |
|---|---------|-------|---------|
| 191 | "Crunching the numbers..." | 25 | Analytics / reports |
| 192 | "Setting up your workspace..." | 29 | First-time setup |
| 193 | "Processing your file..." | 23 | File upload/conversion |
| 194 | "Importing your data..." | 22 | Data import |
| 195 | "Generating your report..." | 26 | Report generation |
| 196 | "Searching across all projects..." | 33 | Deep search |
| 197 | "Applying your changes..." | 25 | Settings update |

### Background Processing

| # | Message | Chars | Context |
|---|---------|-------|---------|
| 198 | "Processing in the background. We'll notify you when it's done." | 63 | Long-running job |
| 199 | "Exporting... This may take a few minutes for large files." | 57 | Large export |
| 200 | "Uploading 12 files... 4 of 12 complete." | 41 | Batch upload with progress |
| 201 | "Migration in progress. You can continue working." | 50 | Data migration |
| 202 | "Building your project... This usually takes 1-2 minutes." | 56 | Build/deploy process |

### Fun/Branded Loading (Casual Products Only)

| # | Message | Chars | Context |
|---|---------|-------|---------|
| 203 | "Good things take time..." | 25 | General wait |
| 204 | "Brewing your results..." | 23 | Search/analytics |
| 205 | "Making magic happen..." | 22 | Creative tools |
| 206 | "Teaching the robots..." | 22 | AI processing |
| 207 | "Warming up the engines..." | 26 | First load |

**Rule:** Fun loading messages are ONLY appropriate for casual/consumer products. Never use them for healthcare, fintech, enterprise, or any serious context.

---

## 8. Changelog Entries

### New Feature

| # | Title | Body | Tag |
|---|-------|------|-----|
| 208 | "New: Command palette" | "Press Cmd+K to search, navigate, and take action from anywhere in the app." | New |
| 209 | "New: Dark mode" | "Switch to dark mode in Settings > Appearance. Your preference syncs across devices." | New |
| 210 | "New: Real-time collaboration" | "Work together with your team in the same document. See cursors and changes live." | New |
| 211 | "New: Mobile app" | "Take your workspace on the go. Download for iOS and Android." | New |
| 212 | "New: API v2" | "Faster endpoints, better error messages, and webhook improvements. See the migration guide." | New |

### Improvement

| # | Title | Body | Tag |
|---|-------|------|-----|
| 213 | "Faster search" | "Search results now load 3x faster. We rebuilt our indexing pipeline from scratch." | Improved |
| 214 | "Improved file uploads" | "Upload files up to 100 MB (previously 25 MB). Drag and drop multiple files at once." | Improved |
| 215 | "Better notifications" | "Smarter notification grouping and a new 'mute' option for noisy channels." | Improved |
| 216 | "Redesigned dashboard" | "Drag, drop, and resize widgets to build your perfect overview." | Improved |
| 217 | "Enhanced security" | "Added support for hardware security keys and improved session management." | Improved |

### Bug Fix

| # | Title | Body | Tag |
|---|-------|------|-----|
| 218 | "Fixed sync issues" | "Resolved a bug where changes wouldn't sync when switching between devices." | Fixed |
| 219 | "Fixed notification delays" | "Push notifications now arrive within seconds instead of minutes." | Fixed |
| 220 | "Fixed export formatting" | "CSV exports now correctly handle special characters and large datasets." | Fixed |
| 221 | "Fixed calendar display" | "Events no longer overlap on small screens. All-day events display correctly." | Fixed |
| 222 | "Fixed login on Safari" | "Resolved an issue where some users couldn't sign in using Safari." | Fixed |

### Deprecation

| # | Title | Body | Tag |
|---|-------|------|-----|
| 223 | "API v1 sunset" | "API v1 will be retired on June 30. Migrate to v2 before then. See the migration guide." | Deprecated |
| 224 | "Classic editor retiring" | "The classic editor will be removed on April 15. Switch to the new editor now." | Deprecated |
| 225 | "Legacy export format" | "XML exports will be removed next month. Switch to CSV or JSON." | Deprecated |

---

## 9. Placeholder Text

### Search Fields

| # | Context | Placeholder | Chars |
|---|---------|-----------|-------|
| 226 | Global search | "Search..." | 9 |
| 227 | Project search | "Search projects..." | 19 |
| 228 | People search | "Search by name or email..." | 27 |
| 229 | File search | "Search files and folders..." | 28 |
| 230 | Command palette | "Type a command or search..." | 28 |
| 231 | Help center | "How can we help?" | 17 |
| 232 | Filter search | "Filter by keyword..." | 21 |

### Input Fields

| # | Context | Placeholder | Chars |
|---|---------|-----------|-------|
| 233 | Email field | "name@company.com" | 17 |
| 234 | Phone field | "+1 (555) 123-4567" | 18 |
| 235 | URL field | "https://example.com" | 20 |
| 236 | Message input | "Write a message..." | 19 |
| 237 | Comment input | "Add a comment..." | 17 |
| 238 | Note input | "Add a note..." | 14 |
| 239 | Project name | "e.g., Marketing Q1 Campaign" | 28 |
| 240 | Tag input | "Add a tag..." | 13 |
| 241 | Description | "Add a description..." | 21 |
| 242 | Coupon code | "Enter code" | 10 |

**Rule:** Placeholders disappear on focus, so never use them as the only label. Always pair with a visible, persistent label above the input.

---

## 10. Contextual Banners

### System Status

| # | Type | Message | Action | Dismissible |
|---|------|---------|--------|-------------|
| 243 | Maintenance | "Scheduled maintenance tonight, 2-4 AM EST. Save your work." | Learn more | Yes |
| 244 | Degraded | "Some features are running slower than usual. We're working on it." | View status | Yes |
| 245 | Outage recovery | "All systems are back to normal. Thank you for your patience." | — | Yes |
| 246 | Incident | "We're investigating issues with file uploads. Updates on our status page." | Status page | No |

### Account Banners

| # | Type | Message | Action | Dismissible |
|---|------|---------|--------|-------------|
| 247 | Verification | "Verify your email to unlock all features." | Verify email | No |
| 248 | Trial | "Your free trial ends in 5 days." | Choose a plan | Yes |
| 249 | Trial expired | "Your trial has ended. Upgrade to continue." | Upgrade now | No |
| 250 | Payment failed | "Your last payment failed. Update your card to avoid interruption." | Update payment | No |
| 251 | Plan limit | "You've reached the storage limit for your plan." | Upgrade | Yes |
| 252 | Feature announcement | "New: AI assistant is here. Try it in any project." | Try it now | Yes |
| 253 | Survey | "Help us improve. Take a 2-minute survey." | Start survey | Yes |

---

## 11. Accessibility Requirements

### Tooltips
- Must be reachable via keyboard focus, not just mouse hover
- Use `role="tooltip"` and `aria-describedby` linking trigger to tooltip
- Must remain visible while focused (no fade-on-blur)
- Must not contain interactive elements (use a popover instead)
- Minimum display time: 1.5 seconds after trigger

### Toasts and Notifications
- Use `role="status"` for informational toasts (polite announcement)
- Use `role="alert"` for error toasts (assertive announcement)
- Auto-dismiss toasts must persist for at least 4 seconds
- Toasts with actions (Undo) must be reachable via keyboard
- Critical information must not be exclusive to toasts — persist it somewhere

### Confirmation Dialogs
- Use `role="alertdialog"` with `aria-labelledby` and `aria-describedby`
- Focus trap: keyboard focus must stay within the dialog
- Focus moves to the dialog on open, returns to trigger on close
- Escape key must close the dialog (same as cancel)
- Destructive confirm button must NOT be auto-focused (prevent accidental activation)

### Loading States
- Announce loading with `aria-live="polite"`: "Loading content"
- Announce completion: "Content loaded" or "Dashboard ready"
- For progress bars: `role="progressbar"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax`
- Never rely solely on visual spinners — always include text

### Helper Text
- Associate with input via `aria-describedby`
- Must be visible at all times (not just on focus)
- Must meet WCAG 2.2 AA contrast (4.5:1 for normal text)
- Must not disappear when the field receives an error (show both)
