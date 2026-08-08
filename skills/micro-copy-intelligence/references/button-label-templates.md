# Button Label Templates

> 200+ production-ready button label templates organized by action type. Every label includes tone variants, character count, when-to-use guidance, and i18n notes.

## Naming Conventions

- **Sentence case** for all buttons: "Save changes" not "Save Changes"
- **Verb-first** for actions: "Create project" not "New project"
- **Noun-only** for navigation: "Settings" not "Go to settings" (when context is clear)
- **No periods** on button labels
- **No exclamation marks** on primary actions (reserve for celebratory moments only)

---

## 1. Account and Authentication

### Sign Up / Registration

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 1 | Create account | 14 | Standard registration | Neutral |
| 2 | Sign up | 7 | Consumer apps, casual tone | Casual |
| 3 | Get started | 11 | Onboarding-first flows | Encouraging |
| 4 | Start free trial | 16 | SaaS with trial period | Action-oriented |
| 5 | Start your free trial | 21 | SaaS, more personal | Warm |
| 6 | Join free | 9 | Community / social platforms | Inviting |
| 7 | Join now | 8 | Urgency-driven, community | Urgent |
| 8 | Create your account | 19 | Formal, personal | Professional |
| 9 | Register | 8 | Enterprise, formal contexts | Formal |
| 10 | Sign up free | 12 | Emphasize no cost | Value-driven |
| 11 | Get started for free | 20 | SaaS landing pages | Encouraging |
| 12 | Create free account | 19 | Emphasize free tier | Value-driven |
| 13 | Try for free | 12 | Low-commitment CTA | Low-pressure |
| 14 | Try it free | 11 | Slightly more casual | Casual |
| 15 | Start building | 14 | Developer tools | Empowering |

**Anti-patterns:** "Submit" (vague), "Click here to register" (verbose), "Register now!!!" (aggressive)

**i18n note:** "Sign up" vs "Sign in" are easily confused in translation. Some languages use the same word. Consider using "Create account" / "Log in" instead for clarity.

### Sign In / Login

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 16 | Sign in | 7 | Standard, most common | Neutral |
| 17 | Log in | 6 | Equally standard alternative | Neutral |
| 18 | Sign in with email | 19 | Multiple auth methods | Specific |
| 19 | Sign in with Google | 20 | Third-party auth | Specific |
| 20 | Sign in with Apple | 19 | Third-party auth (iOS) | Specific |
| 21 | Continue with Google | 21 | Auth as continuation | Seamless |
| 22 | Continue with email | 20 | Auth as continuation | Seamless |
| 23 | Welcome back | 12 | Returning user recognition | Warm |
| 24 | Sign in to your account | 23 | Formal, explicit | Professional |
| 25 | Log in to continue | 18 | Gated content / feature | Contextual |

**Anti-patterns:** "Login" as a verb (it is a noun; "Log in" is the verb), "Enter" (ambiguous), "Submit credentials" (robotic)

**i18n note:** "Sign in" translates more cleanly than "Log in" in most Romance languages. Prefer "Sign in" for international products.

### Sign Out / Logout

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 26 | Sign out | 8 | Standard | Neutral |
| 27 | Log out | 7 | Standard alternative | Neutral |
| 28 | Sign out of all devices | 24 | Security feature | Cautious |
| 29 | Switch account | 14 | Multi-account apps | Neutral |

### Password and Security

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 30 | Reset password | 14 | Forgot password flow | Neutral |
| 31 | Forgot password? | 16 | Login screen link | Helpful |
| 32 | Send reset link | 15 | Password reset confirmation | Specific |
| 33 | Change password | 15 | Settings, active session | Neutral |
| 34 | Update password | 15 | After reset flow | Neutral |
| 35 | Verify your email | 17 | Email verification CTA | Instructional |
| 36 | Resend verification email | 25 | Did not receive email | Helpful |
| 37 | Enable two-factor auth | 22 | Security settings | Professional |
| 38 | Set up 2FA | 10 | Casual security setting | Technical |

---

## 2. Primary Actions (Create, Save, Send)

### Creating

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 39 | Create | 6 | Generic create action | Neutral |
| 40 | Create project | 14 | Specific object | Specific |
| 41 | Create workspace | 16 | SaaS, collaboration | Professional |
| 42 | Create new | 10 | When "new" adds clarity | Neutral |
| 43 | Add | 3 | Adding to existing collection | Minimal |
| 44 | Add item | 8 | Generic add | Neutral |
| 45 | Add to list | 11 | Specific destination | Specific |
| 46 | New project | 11 | Navigation / shortcut style | Quick |
| 47 | New message | 11 | Communication apps | Specific |
| 48 | Compose | 7 | Email, messaging | Formal |
| 49 | Write a post | 12 | Social, blog | Casual |
| 50 | Start a thread | 14 | Discussion / forum | Social |

**Anti-patterns:** "New" alone (unclear what is new), "+" alone without aria-label

### Saving

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 51 | Save | 4 | Generic save | Minimal |
| 52 | Save changes | 12 | Editing existing content | Specific |
| 53 | Save draft | 10 | Unpublished content | Specific |
| 54 | Save and continue | 17 | Multi-step form | Guiding |
| 55 | Save and close | 14 | Modal / panel editing | Efficient |
| 56 | Save as new | 11 | Duplicate-and-edit flows | Specific |
| 57 | Save as template | 16 | Template creation | Specific |
| 58 | Update | 6 | Editing existing record | Neutral |
| 59 | Update profile | 14 | Profile editing | Specific |
| 60 | Apply changes | 13 | Settings, preferences | Formal |
| 61 | Keep changes | 12 | Unsaved changes dialog | Decision |
| 62 | Discard changes | 15 | Unsaved changes dialog | Decision |

**When to use "Save" vs "Update":** Use "Save" when content is being persisted for the first time or as a draft. Use "Update" when modifying an existing, already-saved record.

**i18n note:** "Save" can mean "rescue" in some languages. "Store" or "Keep" may be clearer in certain locales.

### Sending and Submitting

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 63 | Send | 4 | Messages, emails | Direct |
| 64 | Send message | 12 | Explicit message sending | Specific |
| 65 | Send invitation | 15 | Inviting someone | Specific |
| 66 | Send feedback | 13 | Feedback forms | Specific |
| 67 | Submit | 6 | Form submission (use sparingly) | Formal |
| 68 | Submit application | 18 | Job / formal applications | Formal |
| 69 | Submit for review | 17 | Approval workflows | Professional |
| 70 | Request access | 14 | Gated features | Formal |
| 71 | Place order | 11 | E-commerce checkout | Specific |
| 72 | Confirm order | 13 | Order confirmation step | Specific |
| 73 | Complete purchase | 17 | Final checkout step | Specific |
| 74 | Post | 4 | Social media, forums | Casual |
| 75 | Publish | 7 | Blog, CMS, public content | Neutral |
| 76 | Publish post | 12 | Specific publishing | Specific |
| 77 | Go live | 7 | Streaming, real-time | Action |

**Anti-patterns:** "Submit" as a generic (too vague — what exactly is being submitted?). Always specify: "Submit application", "Submit request", etc.

### Confirming

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 78 | Confirm | 7 | Generic confirmation | Neutral |
| 79 | Yes, delete | 11 | Destructive confirmation | Cautious |
| 80 | Yes, remove | 11 | Removal confirmation | Cautious |
| 81 | Yes, cancel it | 14 | Cancellation confirmation | Cautious |
| 82 | Confirm booking | 15 | Reservation confirmation | Specific |
| 83 | Confirm payment | 15 | Payment confirmation | Specific |
| 84 | I understand | 12 | Acknowledging warning | Serious |
| 85 | Agree and continue | 18 | Terms / legal acceptance | Formal |
| 86 | Accept | 6 | Invitation, terms | Formal |
| 87 | Done | 4 | Completing a flow | Minimal |
| 88 | Finish | 6 | Multi-step completion | Neutral |
| 89 | Complete setup | 14 | Onboarding completion | Encouraging |

---

## 3. Destructive Actions

### Deleting

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 90 | Delete | 6 | Generic delete | Direct |
| 91 | Delete project | 14 | Specific object | Specific |
| 92 | Delete permanently | 18 | Irreversible delete | Cautious |
| 93 | Delete forever | 14 | Trash emptying | Serious |
| 94 | Move to trash | 13 | Soft delete with recovery | Safer |
| 95 | Remove | 6 | Removing from a list/group | Neutral |
| 96 | Remove from list | 16 | Specific removal | Specific |
| 97 | Remove member | 13 | Team management | Specific |
| 98 | Unsubscribe | 11 | Email / notification opt-out | Neutral |
| 99 | Leave group | 11 | Social / team | Specific |
| 100 | Leave workspace | 15 | SaaS collaboration | Specific |

**Critical rule:** Destructive buttons use red/danger styling and ALWAYS have a confirmation step. Never place a destructive button where it can be accidentally tapped.

**i18n note:** "Delete" and "Remove" have different semantic weight. "Delete" implies destruction. "Remove" implies displacement. Maintain this distinction in translations.

### Cancelling

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 101 | Cancel | 6 | Dismiss dialog / abandon action | Neutral |
| 102 | Cancel subscription | 19 | Subscription management | Specific |
| 103 | Cancel order | 12 | Order management | Specific |
| 104 | Cancel booking | 14 | Reservation cancellation | Specific |
| 105 | Deactivate account | 18 | Soft account closure | Cautious |
| 106 | Close account | 13 | Permanent account closure | Serious |
| 107 | Delete my account | 17 | GDPR-style permanent deletion | Serious |
| 108 | Revoke access | 13 | Permission removal | Formal |
| 109 | Disconnect | 10 | Integration removal | Neutral |
| 110 | Unlink account | 14 | Third-party account removal | Specific |

### Dismissing and Declining

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 111 | Never mind | 10 | Casual cancel alternative | Casual |
| 112 | Go back | 7 | Return to previous state | Neutral |
| 113 | Not now | 7 | Soft dismissal | Gentle |
| 114 | Maybe later | 11 | Deferral | Gentle |
| 115 | Skip | 4 | Optional step bypass | Minimal |
| 116 | Skip for now | 12 | Implies can do later | Reassuring |
| 117 | No thanks | 9 | Polite decline | Polite |
| 118 | Dismiss | 7 | Close notification / banner | Formal |

**Anti-patterns for cancel/dismiss:** "Don't cancel" (double negative in cancel-subscription dialog), "Are you sure you want to not cancel?" (incomprehensible)

---

## 4. Navigation and Browsing

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 119 | View all | 8 | Truncated list, see more | Neutral |
| 120 | View details | 12 | Item detail navigation | Neutral |
| 121 | See all | 7 | Casual view all | Casual |
| 122 | See more | 8 | Expandable content | Casual |
| 123 | Learn more | 10 | Feature / info pages | Neutral |
| 124 | Read more | 9 | Article / blog content | Content |
| 125 | Explore | 7 | Discovery / browsing | Inviting |
| 126 | Browse | 6 | Catalog / library | Neutral |
| 127 | Browse all | 10 | Full catalog link | Neutral |
| 128 | Discover | 8 | Feature discovery | Inviting |
| 129 | Go to dashboard | 15 | Explicit navigation | Direct |
| 130 | Back to home | 12 | Return navigation | Neutral |
| 131 | Return to list | 14 | List detail back-nav | Neutral |
| 132 | Next | 4 | Sequential navigation | Minimal |
| 133 | Previous | 8 | Sequential back-nav | Minimal |
| 134 | Continue | 8 | Multi-step progression | Encouraging |
| 135 | Next step | 9 | Multi-step form | Guiding |
| 136 | Back | 4 | General back navigation | Minimal |
| 137 | Open | 4 | Open item / file | Minimal |
| 138 | Open in new tab | 15 | External link behavior | Specific |
| 139 | Visit site | 10 | External website link | Neutral |
| 140 | Download | 8 | File download | Neutral |
| 141 | Download PDF | 12 | Specific file type | Specific |
| 142 | Export | 6 | Data export | Neutral |
| 143 | Export as CSV | 13 | Specific format export | Specific |

---

## 5. Toggle and State Actions

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 144 | Show more | 9 | Expand truncated content | Neutral |
| 145 | Show less | 9 | Collapse expanded content | Neutral |
| 146 | Show all | 8 | Reveal all items | Neutral |
| 147 | Expand | 6 | Accordion / collapsible | Neutral |
| 148 | Collapse | 8 | Accordion / collapsible | Neutral |
| 149 | Expand all | 10 | Expand all sections | Neutral |
| 150 | Collapse all | 12 | Collapse all sections | Neutral |
| 151 | Show filters | 12 | Reveal filter panel | Neutral |
| 152 | Hide filters | 12 | Collapse filter panel | Neutral |
| 153 | Enable | 6 | Toggle on | Neutral |
| 154 | Disable | 7 | Toggle off | Neutral |
| 155 | Turn on | 7 | Setting toggle on | Casual |
| 156 | Turn off | 8 | Setting toggle off | Casual |
| 157 | Activate | 8 | Feature activation | Formal |
| 158 | Deactivate | 10 | Feature deactivation | Formal |
| 159 | Pin | 3 | Pin to top / favorites | Minimal |
| 160 | Unpin | 5 | Remove pin | Minimal |
| 161 | Archive | 7 | Move to archive | Neutral |
| 162 | Unarchive | 9 | Restore from archive | Neutral |
| 163 | Mark as read | 12 | Notification / message | Specific |
| 164 | Mark as unread | 14 | Notification / message | Specific |
| 165 | Mute | 4 | Silence notifications | Minimal |
| 166 | Unmute | 6 | Restore notifications | Minimal |
| 167 | Star | 4 | Favorite / prioritize | Minimal |
| 168 | Unstar | 6 | Remove favorite | Minimal |
| 169 | Bookmark | 8 | Save for later | Neutral |
| 170 | Sort by | 7 | Table / list sorting | Neutral |
| 171 | Filter | 6 | Apply filters | Neutral |
| 172 | Clear filters | 13 | Reset all filters | Neutral |
| 173 | Reset | 5 | Return to default state | Neutral |
| 174 | Refresh | 7 | Reload data | Neutral |
| 175 | Retry | 5 | Try failed action again | Neutral |
| 176 | Try again | 9 | Friendlier retry | Encouraging |

---

## 6. Social and Communication

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 177 | Share | 5 | Generic share | Minimal |
| 178 | Share link | 10 | Copy/share URL | Specific |
| 179 | Copy link | 9 | Copy URL to clipboard | Specific |
| 180 | Invite | 6 | Invite user | Neutral |
| 181 | Invite team | 11 | Team invitation | Specific |
| 182 | Invite people | 13 | Generic invitation | Neutral |
| 183 | Send invite | 11 | After entering email | Specific |
| 184 | Follow | 6 | Social follow | Social |
| 185 | Unfollow | 8 | Social unfollow | Social |
| 186 | Like | 4 | Social like | Social |
| 187 | Comment | 7 | Add comment | Social |
| 188 | Reply | 5 | Reply to comment | Social |
| 189 | Repost | 6 | Share to own feed | Social |
| 190 | Report | 6 | Report abuse / content | Neutral |
| 191 | Report abuse | 12 | Specific report | Serious |
| 192 | Block | 5 | Block user | Serious |
| 193 | Unblock | 7 | Remove block | Neutral |
| 194 | Message | 7 | Open DM | Social |
| 195 | Send message | 12 | Explicit send | Specific |
| 196 | Connect | 7 | Professional networking | Professional |
| 197 | Request to join | 15 | Private group | Formal |
| 198 | Accept invitation | 17 | Invitation response | Formal |
| 199 | Decline | 7 | Invitation response | Neutral |

---

## 7. Commerce and Payment

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 200 | Add to cart | 11 | E-commerce product page | Standard |
| 201 | Add to bag | 11 | Fashion e-commerce variant | Style |
| 202 | Buy now | 7 | Instant purchase | Urgent |
| 203 | Checkout | 8 | Cart to payment | Standard |
| 204 | Proceed to checkout | 19 | Explicit checkout nav | Formal |
| 205 | Complete purchase | 17 | Final checkout step | Specific |
| 206 | Place order | 11 | Order confirmation | Standard |
| 207 | Pay now | 7 | Direct payment | Direct |
| 208 | Pay $49.99 | 10 | Price on button | Transparent |
| 209 | Subscribe | 9 | Subscription signup | Neutral |
| 210 | Subscribe for $9/mo | 19 | Price on subscription CTA | Transparent |
| 211 | Start subscription | 18 | Subscription activation | Neutral |
| 212 | Upgrade | 7 | Plan upgrade | Action |
| 213 | Upgrade to Pro | 14 | Specific plan upgrade | Specific |
| 214 | Upgrade plan | 12 | Generic plan upgrade | Neutral |
| 215 | Downgrade | 9 | Plan downgrade | Neutral |
| 216 | Apply coupon | 12 | Discount code entry | Specific |
| 217 | Apply code | 10 | Discount / promo code | Specific |
| 218 | Redeem | 6 | Gift card / reward | Action |
| 219 | Claim offer | 11 | Promotional offer | Urgent |
| 220 | Add to wishlist | 15 | Save for later purchase | Specific |
| 221 | Save for later | 14 | Cart save-for-later | Specific |
| 222 | Reorder | 7 | Repeat previous order | Convenient |
| 223 | Track order | 11 | Order status | Specific |
| 224 | Request refund | 14 | Refund initiation | Specific |
| 225 | Contact support | 15 | Customer service link | Helpful |

**Best practice:** Show the exact price on the final purchase button ("Pay $49.99") to eliminate surprise. Never hide the total behind a generic "Complete purchase".

---

## 8. File and Media Actions

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 226 | Upload | 6 | Generic file upload | Neutral |
| 227 | Upload file | 11 | Specific upload | Neutral |
| 228 | Upload photo | 12 | Image upload | Specific |
| 229 | Choose file | 11 | File picker trigger | Neutral |
| 230 | Browse files | 12 | File picker trigger | Neutral |
| 231 | Drag and drop or browse | 22 | Drop zone label | Instructional |
| 232 | Replace file | 12 | Swap existing upload | Neutral |
| 233 | Remove file | 11 | Delete uploaded file | Neutral |
| 234 | Download | 8 | File download | Neutral |
| 235 | Download all | 12 | Batch download | Neutral |
| 236 | Export | 6 | Data export | Neutral |
| 237 | Import | 6 | Data import | Neutral |
| 238 | Import from CSV | 15 | Specific format import | Specific |
| 239 | Copy | 4 | Duplicate item | Minimal |
| 240 | Duplicate | 9 | Create copy of item | Neutral |
| 241 | Move to | 7 | Relocate item | Neutral |
| 242 | Rename | 6 | Change item name | Neutral |
| 243 | Edit | 4 | Enter edit mode | Minimal |
| 244 | Edit profile | 12 | Specific edit context | Specific |
| 245 | Crop | 4 | Image editing | Minimal |
| 246 | Resize | 6 | Image/element editing | Minimal |
| 247 | Preview | 7 | View before publishing | Neutral |
| 248 | Print | 5 | Print action | Neutral |
| 249 | Scan document | 13 | Camera document scan | Specific |

---

## 9. Search and Filter

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 250 | Search | 6 | Search field button / icon | Minimal |
| 251 | Search projects | 15 | Scoped search | Specific |
| 252 | Find | 4 | In-page / in-document search | Minimal |
| 253 | Find and replace | 16 | Text editing | Specific |
| 254 | Apply filters | 13 | Filter panel confirm | Neutral |
| 255 | Clear all | 9 | Reset all filters/selections | Neutral |
| 256 | Clear search | 12 | Reset search field | Neutral |
| 257 | Show results | 12 | After filter selection | Neutral |
| 258 | Show 24 results | 15 | With result count | Specific |

---

## 10. Contextual and Situational Buttons

| # | Label | Chars | When to Use | Tone |
|---|-------|-------|-------------|------|
| 259 | Get help | 8 | Help / support access | Helpful |
| 260 | Contact us | 10 | Support page CTA | Neutral |
| 261 | Chat with us | 12 | Live chat trigger | Warm |
| 262 | Give feedback | 13 | Feedback trigger | Inviting |
| 263 | Rate this app | 13 | App store review prompt | Neutral |
| 264 | Take the tour | 13 | Feature tour trigger | Inviting |
| 265 | Watch demo | 10 | Video demo CTA | Action |
| 266 | See how it works | 16 | Explainer CTA | Inviting |
| 267 | View pricing | 12 | Pricing page nav | Neutral |
| 268 | Compare plans | 13 | Plan comparison | Neutral |
| 269 | Book a demo | 11 | Sales CTA | Action |
| 270 | Schedule a call | 15 | Sales / support CTA | Formal |
| 271 | Remind me later | 15 | Notification defer | Gentle |
| 272 | Don't show again | 16 | Permanent dismiss | Firm |
| 273 | Undo | 4 | Reverse last action | Minimal |
| 274 | Restore | 7 | Recover deleted item | Neutral |
| 275 | Manage | 6 | Open management panel | Neutral |
| 276 | Manage team | 11 | Team settings | Specific |
| 277 | Customize | 9 | Open customization | Neutral |
| 278 | Set up | 6 | Initial configuration | Guiding |
| 279 | Connect | 7 | Integration setup | Action |
| 280 | Sync now | 8 | Manual sync trigger | Action |
| 281 | Verify | 6 | Verification action | Neutral |
| 282 | Approve | 7 | Approval action | Formal |
| 283 | Reject | 6 | Rejection action | Formal |
| 284 | Assign | 6 | Task/ticket assignment | Neutral |
| 285 | Reassign | 8 | Change assignment | Neutral |
| 286 | Escalate | 8 | Priority escalation | Serious |
| 287 | Merge | 5 | Combine items | Neutral |
| 288 | Split | 5 | Divide items | Neutral |
| 289 | Lock | 4 | Prevent editing | Minimal |
| 290 | Unlock | 6 | Allow editing | Minimal |

---

## Button Pairing Guide

Common button pairs for dialogs and forms:

| Context | Primary (Right) | Secondary (Left) |
|---------|----------------|------------------|
| Save dialog | Save changes | Discard |
| Delete confirmation | Delete project | Keep project |
| Cancel subscription | Cancel subscription | Keep subscription |
| Unsaved changes | Save and exit | Exit without saving |
| Send message | Send | Cancel |
| Form submission | Create project | Cancel |
| Payment | Pay $49.99 | Go back |
| Onboarding step | Continue | Skip for now |
| Permission request | Allow notifications | Not now |
| Cookie consent | Accept all | Manage preferences |
| Destructive batch | Delete 5 items | Cancel |
| Account deletion | Delete my account | Keep my account |

**Rule:** The primary action button goes on the right (or bottom on mobile). Destructive primary buttons use danger styling, never default primary styling.

---

## Character Count Quick Reference

| Category | Target | Max |
|----------|--------|-----|
| Single-word actions | 3-8 chars | 10 chars |
| Two-word labels | 8-14 chars | 18 chars |
| Three-word labels | 12-20 chars | 25 chars |
| CTA with context | 15-25 chars | 30 chars |

**Rule of thumb:** If your button label needs more than 25 characters, consider whether the context can be communicated elsewhere (heading, body text) so the button can be shorter.

---

## Accessibility Notes for Buttons

- Every button must have a visible text label OR an `aria-label` (icon-only buttons)
- Icon + text is the most accessible pattern
- Avoid "Learn more" appearing multiple times on a page — each needs unique `aria-label`: "Learn more about pricing", "Learn more about features"
- Toggle buttons must communicate state: `aria-pressed="true"` or `aria-expanded="true"`
- Disabled buttons should include `aria-disabled="true"` and a tooltip explaining why they are disabled
- Color alone must not be the only indicator of button type (e.g., destructive buttons need text cues too, not just red color)
