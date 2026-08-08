# Fintech Page Templates — Complete Implementation Guide

## Overview

This reference provides complete page-level templates for 10 essential fintech/banking pages. Each template includes block sequence, typography, color application, spacing rhythm, component selection, responsive behavior, and React/TSX skeletons. Every page is provided in two style variants: Clean Modern (Mercury/Wise) and Bold Fintech (Cash App/Robinhood).

Every template includes compliance considerations, trust signal placement, and data security UI patterns specific to financial products.

---

## Fintech Design Principles

### Trust Architecture
Financial products must earn trust at every interaction. Trust is built through:
1. **Visual precision** — Pixel-perfect alignment communicates competence with money
2. **Data transparency** — Show calculations, never hide fees
3. **Security signals** — Encryption badges, 2FA indicators, audit trails
4. **Regulatory compliance** — FDIC badges, licensing info, required disclosures
5. **Consistency** — Every number formatted identically, every action reversible

### Compliance UI Requirements
- FDIC / SIPC insurance disclosures visible on relevant pages
- Required legal disclaimers in transfers and investments
- Accessible transaction records (screen reader compatible)
- Clear fee disclosure before any monetary action
- Two-factor authentication indicators
- Session timeout warnings with graceful re-authentication

---

## 1. Banking Dashboard (Accounts, Transactions, Spending)

### Block Sequence
1. Top bar (greeting + notifications + profile)
2. Account summary cards (checking, savings, credit, investment)
3. Quick actions row (send, request, pay bills, deposit)
4. Recent transactions list (grouped by date)
5. Spending insights widget (category breakdown)
6. Upcoming bills / scheduled payments

### Variant A: Clean Modern (Mercury/Wise Style)

**Typography Map**
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Greeting | Inter | 500 | 16px | 24px |
| Account label | Inter | 400 | 13px | 18px |
| Account balance | Inter | 600 | 32px | 40px |
| Balance decimals | Inter | 400 | 20px | 28px |
| Transaction merchant | Inter | 500 | 14px | 20px |
| Transaction amount | Inter | 500 | 14px | 20px |
| Transaction date | Inter | 400 | 12px | 16px |
| Section heading | Inter | 600 | 18px | 24px |
| Quick action label | Inter | 500 | 12px | 16px |

**Color Application**
```
Background:             #FFFFFF
Sidebar:                #FAFAFA border-right: 1px solid #E5E5E5
Account card bg:        #FFFFFF border: 1px solid #E5E5E5
Account card hover:     border-color #000000
Positive amount:        #16A34A (green)
Negative amount:        #111111 (black — expenses are normal, not alarming)
Pending amount:         #9CA3AF (gray)
Quick action icon bg:   #F5F5F5
Quick action icon:      #111111
Category spending:      Muted palette — #3B82F6, #10B981, #F59E0B, #8B5CF6, #EC4899
Trust badge bg:         #F0FDF4 (light green)
Trust badge text:       #16A34A
```

**Spacing Rhythm**
```
Top bar height:         64px
Account card gap:       16px
Account card padding:   24px
Quick action gap:       12px
Transaction row height: 56px
Transaction row gap:    0 (dividers only)
Section gap:            32px
Content padding:        32px
Sidebar width:          240px
```

**Trust Signals**
- FDIC insured badge in sidebar footer
- Last login timestamp in top bar
- Green shield icon next to account names
- "Secured by 256-bit encryption" footer text

**Compliance Considerations**
- Balance includes available vs current distinction
- Pending transactions clearly marked with gray text and "Pending" badge
- Interest rate disclosure on savings accounts
- APY displayed with required asterisk linking to terms

**React/TSX Skeleton**
```tsx
export function BankingDashboardClean() {
  const accounts = [
    { name: 'Checking', number: '****4821', balance: 12847.53, type: 'checking' },
    { name: 'Savings', number: '****9102', balance: 34291.00, apy: '4.25%', type: 'savings' },
    { name: 'Investment', number: '****7744', balance: 89432.18, change: '+2.4%', type: 'investment' },
  ];

  const transactions = [
    { merchant: 'Whole Foods Market', category: 'Groceries', amount: -67.42, date: 'Today', status: 'completed' },
    { merchant: 'Spotify', category: 'Subscription', amount: -15.99, date: 'Today', status: 'completed' },
    { merchant: 'ACH Deposit — Payroll', category: 'Income', amount: 4250.00, date: 'Yesterday', status: 'completed' },
    { merchant: 'Amazon.com', category: 'Shopping', amount: -124.99, date: 'Yesterday', status: 'pending' },
    { merchant: 'Transfer to Savings', category: 'Transfer', amount: -500.00, date: 'Mar 9', status: 'completed' },
  ];

  return (
    <div className="flex min-h-screen bg-white">
      {/* Sidebar */}
      <aside className="hidden w-60 border-r border-gray-200 bg-[#FAFAFA] p-5 lg:flex lg:flex-col">
        <div className="text-base font-semibold text-gray-900">BankName</div>
        <nav className="mt-8 space-y-1">
          {['Home', 'Accounts', 'Transfers', 'Cards', 'Bills', 'Settings'].map((item) => (
            <a key={item} href="#" className={`block rounded-lg px-3 py-2 text-sm ${item === 'Home' ? 'bg-white font-medium text-gray-900 shadow-sm' : 'text-gray-500 hover:text-gray-900'}`}>
              {item}
            </a>
          ))}
        </nav>
        <div className="mt-auto rounded-lg bg-[#F0FDF4] p-3">
          <p className="text-xs font-medium text-green-700">FDIC Insured</p>
          <p className="mt-1 text-[10px] text-green-600">Deposits insured up to $250,000</p>
        </div>
      </aside>

      {/* Main */}
      <main className="flex-1 p-8">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm text-gray-500">Good morning</p>
            <h1 className="text-xl font-semibold text-gray-900">Welcome back, Alex</h1>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-xs text-gray-400">Last login: Today 9:42 AM</span>
            <button className="relative rounded-lg p-2 hover:bg-gray-100">
              <span className="text-gray-500">bell</span>
              <span className="absolute right-1.5 top-1.5 h-2 w-2 rounded-full bg-red-500" />
            </button>
          </div>
        </div>

        {/* Accounts */}
        <div className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {accounts.map((acc) => (
            <div key={acc.number} className="rounded-xl border border-gray-200 p-6 hover:border-gray-900 transition-colors cursor-pointer">
              <div className="flex items-center justify-between">
                <p className="text-[13px] text-gray-500">{acc.name}</p>
                <span className="text-[11px] text-gray-400">{acc.number}</span>
              </div>
              <p className="mt-3 text-[32px] font-semibold text-gray-900">
                ${acc.balance.toLocaleString('en-US', { minimumFractionDigits: 2 })}
              </p>
              {acc.apy && (
                <p className="mt-1 text-xs text-green-600">{acc.apy} APY*</p>
              )}
              {acc.change && (
                <p className="mt-1 text-xs text-green-600">{acc.change} today</p>
              )}
            </div>
          ))}
        </div>

        {/* Quick Actions */}
        <div className="mt-8 flex gap-3">
          {['Send', 'Request', 'Pay bills', 'Deposit'].map((action) => (
            <button key={action} className="flex flex-col items-center gap-2 rounded-xl bg-[#F5F5F5] px-6 py-4 hover:bg-gray-200 transition-colors">
              <div className="flex h-10 w-10 items-center justify-center rounded-full bg-white shadow-sm">
                <span className="text-sm text-gray-700">icon</span>
              </div>
              <span className="text-xs font-medium text-gray-700">{action}</span>
            </button>
          ))}
        </div>

        {/* Transactions */}
        <div className="mt-8">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold text-gray-900">Recent transactions</h2>
            <a href="#" className="text-sm text-gray-500 hover:text-gray-900">View all</a>
          </div>
          <div className="mt-4 rounded-xl border border-gray-200">
            <div className="divide-y divide-gray-100">
              {transactions.map((tx, idx) => (
                <div key={idx} className="flex items-center justify-between px-5 py-4 hover:bg-gray-50">
                  <div className="flex items-center gap-4">
                    <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-100">
                      <span className="text-xs text-gray-500">{tx.category[0]}</span>
                    </div>
                    <div>
                      <p className="text-sm font-medium text-gray-900">{tx.merchant}</p>
                      <p className="text-xs text-gray-500">{tx.category}</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className={`text-sm font-medium ${tx.amount > 0 ? 'text-green-600' : 'text-gray-900'}`}>
                      {tx.amount > 0 ? '+' : ''}{tx.amount.toLocaleString('en-US', { style: 'currency', currency: 'USD' })}
                    </p>
                    <p className="text-xs text-gray-400">
                      {tx.date}
                      {tx.status === 'pending' && <span className="ml-2 text-amber-500">Pending</span>}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
```

### Variant B: Bold Fintech (Cash App/Robinhood Style)

**Typography Map**
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Balance | SF Pro / system | 800 | 48px | 56px |
| Account label | SF Pro / system | 500 | 14px | 20px |
| Transaction | SF Pro / system | 500 | 15px | 22px |
| Quick action | SF Pro / system | 600 | 13px | 18px |

**Color Application**
```
Background:             #000000 (or #1C1C1E for iOS dark)
Primary green:          #00D632 (Cash App green)
Card background:        #1C1C1E
Balance text:           #FFFFFF
Transaction positive:   #00D632
Transaction negative:   #FFFFFF
Accent:                 #00D632
Tab bar:                #000000 border-top: 1px solid #2C2C2E
```

**Key Differences from Clean Modern**
- Full-screen dark mode, no sidebar
- Tab bar navigation (bottom on mobile)
- Single prominent balance display (not cards)
- Swipe-able account tabs
- Green accent for all positive/interactive elements
- Bold, large type for balance
- Haptic-style feedback animations
- Floating action button for primary action

---

## 2. Transaction History Page

### Block Sequence
1. Page header (title + date range filter + search)
2. Summary bar (total in, total out, net)
3. Filter chips (category, amount range, status)
4. Transaction list (grouped by date)
5. Pagination or infinite scroll
6. Export button (CSV/PDF)

### Variant A: Clean Modern

**React/TSX Skeleton**
```tsx
export function TransactionHistoryClean() {
  return (
    <div className="min-h-screen bg-white p-8">
      <div className="mx-auto max-w-[800px]">
        <div className="flex items-center justify-between">
          <h1 className="text-xl font-semibold text-gray-900">Transactions</h1>
          <div className="flex items-center gap-3">
            <input type="search" placeholder="Search transactions..." className="w-64 rounded-lg border border-gray-200 px-4 py-2 text-sm focus:border-gray-900 focus:outline-none" />
            <button className="rounded-lg border border-gray-200 px-3 py-2 text-sm text-gray-600 hover:border-gray-900">Export</button>
          </div>
        </div>

        {/* Summary */}
        <div className="mt-6 grid grid-cols-3 gap-4">
          <div className="rounded-lg bg-[#F0FDF4] p-4">
            <p className="text-xs text-green-600">Money in</p>
            <p className="mt-1 text-lg font-semibold text-green-700">$8,500.00</p>
          </div>
          <div className="rounded-lg bg-gray-50 p-4">
            <p className="text-xs text-gray-500">Money out</p>
            <p className="mt-1 text-lg font-semibold text-gray-900">$3,247.82</p>
          </div>
          <div className="rounded-lg bg-gray-50 p-4">
            <p className="text-xs text-gray-500">Net</p>
            <p className="mt-1 text-lg font-semibold text-green-700">+$5,252.18</p>
          </div>
        </div>

        {/* Filters */}
        <div className="mt-6 flex gap-2">
          {['All', 'Income', 'Expenses', 'Transfers', 'Pending'].map((f) => (
            <button key={f} className={`rounded-full px-4 py-1.5 text-xs font-medium ${f === 'All' ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'}`}>
              {f}
            </button>
          ))}
        </div>

        {/* Transaction Groups */}
        <div className="mt-6 space-y-6">
          {['Today', 'Yesterday', 'March 9, 2026'].map((date) => (
            <div key={date}>
              <p className="text-xs font-medium uppercase tracking-wider text-gray-400">{date}</p>
              <div className="mt-2 rounded-xl border border-gray-200 divide-y divide-gray-100">
                {[1, 2, 3].map((i) => (
                  <div key={i} className="flex items-center justify-between px-5 py-4 hover:bg-gray-50 cursor-pointer">
                    <div className="flex items-center gap-4">
                      <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-100 text-xs text-gray-500">M</div>
                      <div>
                        <p className="text-sm font-medium text-gray-900">Merchant Name</p>
                        <p className="text-xs text-gray-500">Category</p>
                      </div>
                    </div>
                    <div className="text-right">
                      <p className="text-sm font-medium text-gray-900">-$42.50</p>
                      <p className="text-xs text-gray-400">Completed</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Bold Fintech — Dark bg, large amounts, swipe actions, colored category icons

**Data Security Patterns**
- Transaction details require re-authentication after 15 minutes idle
- Account numbers partially masked (****4821)
- Export requires email verification
- Screenshot detection warning on sensitive data

---

## 3. Transfer / Send Money Flow

### Block Sequence
1. Recipient selection (contacts, recent, manual entry)
2. Amount input (large numeric display)
3. Transfer details (from account, memo, schedule)
4. Review summary (all details, fees, estimated arrival)
5. Confirmation (success state with reference number)

### Variant A: Clean Modern

**Compliance Requirements**
- Fee disclosure before confirmation
- Estimated delivery time
- Exchange rate for international (if applicable)
- Cancel/modify window disclosure
- OFAC sanctions check (backend, but loading state visible)

**React/TSX Skeleton**
```tsx
import { useState } from 'react';

export function TransferFlowClean() {
  const [step, setStep] = useState(1);

  return (
    <div className="flex min-h-screen items-center justify-center bg-[#FAFAFA]">
      <div className="w-full max-w-[480px] rounded-2xl bg-white p-8 shadow-sm">
        {/* Progress */}
        <div className="flex items-center justify-center gap-2">
          {[1, 2, 3, 4].map((s) => (
            <div key={s} className={`h-1 w-12 rounded-full ${s <= step ? 'bg-gray-900' : 'bg-gray-200'}`} />
          ))}
        </div>

        {step === 1 && (
          <div className="mt-8">
            <h2 className="text-lg font-semibold text-gray-900">Who are you sending to?</h2>
            <input type="text" placeholder="Name, email, or account number" className="mt-4 w-full rounded-lg border border-gray-200 px-4 py-3 text-sm focus:border-gray-900 focus:outline-none" />
            <div className="mt-4">
              <p className="text-xs font-medium text-gray-400 uppercase tracking-wider">Recent</p>
              <div className="mt-2 space-y-2">
                {['Jane Smith', 'Bob Johnson', 'Acme Corp'].map((name) => (
                  <button key={name} className="flex w-full items-center gap-3 rounded-lg p-3 hover:bg-gray-50">
                    <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-100 text-sm font-medium text-gray-600">{name[0]}</div>
                    <span className="text-sm font-medium text-gray-900">{name}</span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {step === 2 && (
          <div className="mt-8 text-center">
            <p className="text-sm text-gray-500">Sending to Jane Smith</p>
            <div className="mt-6">
              <span className="text-5xl font-semibold text-gray-900">$</span>
              <input type="text" defaultValue="0.00" className="inline w-auto bg-transparent text-5xl font-semibold text-gray-900 text-center focus:outline-none" style={{ width: '200px' }} />
            </div>
            <p className="mt-4 text-sm text-gray-400">Available: $12,847.53</p>
          </div>
        )}

        {step === 3 && (
          <div className="mt-8">
            <h2 className="text-lg font-semibold text-gray-900">Review transfer</h2>
            <div className="mt-6 space-y-4">
              <div className="flex items-center justify-between border-b border-gray-100 pb-4">
                <span className="text-sm text-gray-500">To</span>
                <span className="text-sm font-medium text-gray-900">Jane Smith</span>
              </div>
              <div className="flex items-center justify-between border-b border-gray-100 pb-4">
                <span className="text-sm text-gray-500">Amount</span>
                <span className="text-sm font-medium text-gray-900">$250.00</span>
              </div>
              <div className="flex items-center justify-between border-b border-gray-100 pb-4">
                <span className="text-sm text-gray-500">From</span>
                <span className="text-sm font-medium text-gray-900">Checking ****4821</span>
              </div>
              <div className="flex items-center justify-between border-b border-gray-100 pb-4">
                <span className="text-sm text-gray-500">Fee</span>
                <span className="text-sm font-medium text-green-600">Free</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-500">Arrives</span>
                <span className="text-sm font-medium text-gray-900">1-2 business days</span>
              </div>
            </div>
            <p className="mt-6 text-[10px] text-gray-400">
              By confirming, you authorize this transfer. Funds will be debited from your account immediately.
              Standard ACH processing times apply. See terms for details.
            </p>
          </div>
        )}

        {step === 4 && (
          <div className="mt-8 text-center">
            <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-green-100">
              <span className="text-2xl text-green-600">check</span>
            </div>
            <h2 className="mt-4 text-lg font-semibold text-gray-900">Transfer sent</h2>
            <p className="mt-2 text-sm text-gray-500">$250.00 to Jane Smith</p>
            <p className="mt-1 text-xs text-gray-400">Reference: TXN-2026031201</p>
            <p className="mt-1 text-xs text-gray-400">Estimated arrival: Mar 14, 2026</p>
          </div>
        )}

        <div className="mt-8 flex items-center justify-between">
          {step > 1 && step < 4 ? (
            <button onClick={() => setStep(step - 1)} className="text-sm text-gray-500 hover:text-gray-900">Back</button>
          ) : <span />}
          <button onClick={() => setStep(Math.min(step + 1, 4))} className="rounded-lg bg-gray-900 px-6 py-2.5 text-sm font-medium text-white hover:bg-gray-800">
            {step === 3 ? 'Confirm transfer' : step === 4 ? 'Done' : 'Continue'}
          </button>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Bold Fintech — Dark bg, large green amount input, haptic confirm button, confetti success

---

## 4. Investment Portfolio Overview

### Block Sequence
1. Total portfolio value + daily change
2. Performance chart (1D, 1W, 1M, 3M, 1Y, ALL)
3. Asset allocation donut chart
4. Holdings list (name, shares, value, change)
5. Recent dividends / activity
6. Market news feed (optional)

### Variant A: Clean Modern

**Trust Signals**
- SIPC protection badge
- "Prices delayed 15 min" or "Real-time" indicator
- Brokerage account vs advisory account distinction
- Tax lot information accessibility

**React/TSX Skeleton**
```tsx
export function PortfolioClean() {
  const holdings = [
    { symbol: 'AAPL', name: 'Apple Inc.', shares: 15, value: 3247.50, change: '+1.2%', positive: true },
    { symbol: 'MSFT', name: 'Microsoft Corp.', shares: 8, value: 3412.80, change: '+0.8%', positive: true },
    { symbol: 'AMZN', name: 'Amazon.com', shares: 5, value: 945.75, change: '-0.3%', positive: false },
    { symbol: 'GOOGL', name: 'Alphabet Inc.', shares: 10, value: 1780.00, change: '+2.1%', positive: true },
  ];

  return (
    <div className="min-h-screen bg-white p-8">
      <div className="mx-auto max-w-[900px]">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm text-gray-500">Total Portfolio Value</p>
            <p className="mt-1 text-4xl font-semibold text-gray-900">$89,432.18</p>
            <p className="mt-1 text-sm font-medium text-green-600">+$1,247.30 (+1.42%) today</p>
          </div>
          <div className="text-right">
            <span className="rounded-full bg-green-50 px-3 py-1 text-xs font-medium text-green-700">Market Open</span>
            <p className="mt-1 text-[10px] text-gray-400">Real-time prices</p>
          </div>
        </div>

        {/* Chart */}
        <div className="mt-8 rounded-xl border border-gray-200 p-6">
          <div className="flex gap-2">
            {['1D', '1W', '1M', '3M', '1Y', 'ALL'].map((range) => (
              <button key={range} className={`rounded-md px-3 py-1 text-xs font-medium ${range === '1M' ? 'bg-gray-900 text-white' : 'text-gray-500 hover:bg-gray-100'}`}>
                {range}
              </button>
            ))}
          </div>
          <div className="mt-4 h-64 rounded bg-gray-50" />
        </div>

        {/* Holdings */}
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-gray-900">Holdings</h2>
          <div className="mt-4 rounded-xl border border-gray-200">
            <table className="w-full">
              <thead>
                <tr className="border-b border-gray-100 text-left text-xs font-medium uppercase tracking-wider text-gray-400">
                  <th className="px-5 py-3">Asset</th>
                  <th className="px-5 py-3 text-right">Shares</th>
                  <th className="px-5 py-3 text-right">Value</th>
                  <th className="px-5 py-3 text-right">Change</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-100">
                {holdings.map((h) => (
                  <tr key={h.symbol} className="hover:bg-gray-50 cursor-pointer">
                    <td className="px-5 py-4">
                      <p className="text-sm font-medium text-gray-900">{h.symbol}</p>
                      <p className="text-xs text-gray-500">{h.name}</p>
                    </td>
                    <td className="px-5 py-4 text-right text-sm text-gray-600">{h.shares}</td>
                    <td className="px-5 py-4 text-right text-sm font-medium text-gray-900">${h.value.toLocaleString()}</td>
                    <td className={`px-5 py-4 text-right text-sm font-medium ${h.positive ? 'text-green-600' : 'text-red-600'}`}>{h.change}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Compliance Footer */}
        <div className="mt-8 rounded-lg bg-gray-50 p-4">
          <p className="text-[10px] text-gray-400">
            Securities offered through BankName Securities LLC, Member FINRA/SIPC.
            Investment products are not FDIC insured, have no bank guarantee, and may lose value.
            Past performance does not guarantee future results.
          </p>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Bold Fintech — Dark bg, large animated chart, green/red color coding, stock ticker style

---

## 5. Card Management Page

### Block Sequence
1. Card visual (3D card render with masked number)
2. Card details (last 4, expiry, status)
3. Card controls (freeze, set limits, PIN, replace)
4. Recent card transactions
5. Spending limits / controls

### Variant A: Clean Modern

```tsx
export function CardManagementClean() {
  return (
    <div className="min-h-screen bg-white p-8">
      <div className="mx-auto max-w-[600px]">
        <h1 className="text-xl font-semibold text-gray-900">Card</h1>

        {/* Card Visual */}
        <div className="mt-6 aspect-[1.586/1] max-w-[380px] rounded-2xl bg-gradient-to-br from-gray-900 to-gray-700 p-6 text-white shadow-xl">
          <p className="text-sm font-medium opacity-80">BankName</p>
          <p className="mt-8 font-mono text-lg tracking-widest">**** **** **** 4821</p>
          <div className="mt-4 flex items-center justify-between">
            <div>
              <p className="text-[10px] uppercase tracking-wider opacity-60">Exp</p>
              <p className="text-sm">12/28</p>
            </div>
            <p className="text-sm font-medium">VISA</p>
          </div>
        </div>

        {/* Controls */}
        <div className="mt-8 grid grid-cols-4 gap-3">
          {[
            { label: 'Freeze', active: false },
            { label: 'Limits', active: false },
            { label: 'PIN', active: false },
            { label: 'Replace', active: false },
          ].map((ctrl) => (
            <button key={ctrl.label} className="flex flex-col items-center gap-2 rounded-xl border border-gray-200 p-4 hover:border-gray-900 transition-colors">
              <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-100">
                <span className="text-xs text-gray-600">icon</span>
              </div>
              <span className="text-xs font-medium text-gray-700">{ctrl.label}</span>
            </button>
          ))}
        </div>

        {/* Spending Limits */}
        <div className="mt-8 rounded-xl border border-gray-200 p-5">
          <h3 className="text-sm font-semibold text-gray-900">Spending limits</h3>
          <div className="mt-4 space-y-4">
            <div>
              <div className="flex items-center justify-between text-sm">
                <span className="text-gray-500">Daily limit</span>
                <span className="font-medium text-gray-900">$2,500 / $5,000</span>
              </div>
              <div className="mt-2 h-2 rounded-full bg-gray-100">
                <div className="h-full w-1/2 rounded-full bg-gray-900" />
              </div>
            </div>
            <div>
              <div className="flex items-center justify-between text-sm">
                <span className="text-gray-500">Monthly limit</span>
                <span className="font-medium text-gray-900">$8,400 / $25,000</span>
              </div>
              <div className="mt-2 h-2 rounded-full bg-gray-100">
                <div className="h-full w-1/3 rounded-full bg-gray-900" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Bold Fintech — Dark card on dark bg, neon accents, tap-to-reveal CVV, haptic freeze toggle

**Security UI Patterns**
- Card number never shown in full (tap to reveal last 4 only)
- CVV requires biometric/PIN to view
- Freeze card is immediate, one-tap
- Suspicious activity alert banner
- Virtual card number generation

---

## 6. Bill Payment Flow

### Block Sequence
1. Payee selection (saved payees + add new)
2. Payment details (amount, date, frequency)
3. Review and confirm
4. Confirmation with receipt

### Compliance: Display payment terms, late fee warnings, auto-pay disclosure

---

## 7. Loan/Credit Application Flow

### Block Sequence
1. Pre-qualification check (soft pull disclosure)
2. Personal information form
3. Financial information (income, employment)
4. Document upload (ID, pay stubs)
5. Review and submit
6. Decision / next steps

### Compliance: Truth in Lending disclosures, APR calculation, adverse action notice

---

## 8. Budget / Savings Goals Page

### Block Sequence
1. Total savings progress
2. Goals grid (cards with progress rings)
3. Individual goal detail (contributions, timeline, projections)
4. Auto-save rules configuration
5. Insights and recommendations

### Variant A: Clean Modern — White bg, circular progress rings, clean projections chart
### Variant B: Bold Fintech — Dark bg, animated progress, gamified milestones, celebratory animations

---

## 9. Financial Insights / Analytics Page

### Block Sequence
1. Spending overview (total, vs last month)
2. Category breakdown (horizontal bar chart)
3. Income vs expenses (line chart over time)
4. Top merchants list
5. Recurring charges detection
6. Savings opportunities

### Variant A: Clean Modern
```tsx
export function InsightsClean() {
  const categories = [
    { name: 'Housing', amount: 2100, pct: 42, color: '#3B82F6' },
    { name: 'Food & Dining', amount: 620, pct: 12, color: '#10B981' },
    { name: 'Transportation', amount: 340, pct: 7, color: '#F59E0B' },
    { name: 'Shopping', amount: 280, pct: 6, color: '#8B5CF6' },
    { name: 'Subscriptions', amount: 167, pct: 3, color: '#EC4899' },
    { name: 'Other', amount: 493, pct: 10, color: '#6B7280' },
  ];

  return (
    <div className="min-h-screen bg-white p-8">
      <div className="mx-auto max-w-[800px]">
        <h1 className="text-xl font-semibold text-gray-900">Insights</h1>
        <p className="mt-1 text-sm text-gray-500">March 2026</p>

        <div className="mt-8 grid gap-4 sm:grid-cols-3">
          <div className="rounded-xl border border-gray-200 p-5">
            <p className="text-xs text-gray-500">Total spent</p>
            <p className="mt-1 text-2xl font-semibold text-gray-900">$4,000</p>
            <p className="mt-1 text-xs text-red-500">+12% vs last month</p>
          </div>
          <div className="rounded-xl border border-gray-200 p-5">
            <p className="text-xs text-gray-500">Total earned</p>
            <p className="mt-1 text-2xl font-semibold text-gray-900">$8,500</p>
            <p className="mt-1 text-xs text-green-600">Same as last month</p>
          </div>
          <div className="rounded-xl border border-gray-200 p-5">
            <p className="text-xs text-gray-500">Saved</p>
            <p className="mt-1 text-2xl font-semibold text-green-700">$4,500</p>
            <p className="mt-1 text-xs text-green-600">53% savings rate</p>
          </div>
        </div>

        {/* Category Breakdown */}
        <div className="mt-8">
          <h2 className="text-lg font-semibold text-gray-900">Spending by category</h2>
          <div className="mt-4 space-y-3">
            {categories.map((cat) => (
              <div key={cat.name} className="flex items-center gap-4">
                <span className="w-28 text-sm text-gray-600">{cat.name}</span>
                <div className="flex-1">
                  <div className="h-6 rounded-full bg-gray-100">
                    <div className="h-full rounded-full" style={{ width: `${cat.pct}%`, backgroundColor: cat.color }} />
                  </div>
                </div>
                <span className="w-20 text-right text-sm font-medium text-gray-900">${cat.amount.toLocaleString()}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Recurring Detection */}
        <div className="mt-8 rounded-xl border border-amber-200 bg-amber-50 p-5">
          <h3 className="text-sm font-semibold text-amber-800">Recurring charges detected</h3>
          <p className="mt-1 text-xs text-amber-700">We found 3 subscriptions you might not be using. Review to save $47/month.</p>
          <button className="mt-3 rounded-lg bg-amber-600 px-4 py-2 text-xs font-medium text-white hover:bg-amber-700">Review subscriptions</button>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Bold Fintech — Dark bg, animated bar charts, green savings highlights, gamified savings rate

---

## 10. Identity Verification (KYC) Flow

### Block Sequence
1. Welcome / explanation screen (why verification needed)
2. Personal information (legal name, DOB, SSN last 4, address)
3. Document upload (photo ID front + back)
4. Selfie verification (liveness check)
5. Review and submit
6. Processing / result screen

### Variant A: Clean Modern

**Compliance Requirements**
- Clear explanation of why data is needed
- Privacy policy link prominent
- Data retention disclosure
- Right to dispute / appeal
- Encryption indicator during upload
- BSA/AML compliance disclosure

**Security UI Patterns**
- SSL/encryption indicator during data entry
- No SSN shown after entry (masked immediately)
- Document upload uses secure direct upload (not form POST)
- Camera permissions requested with clear explanation
- Biometric data usage disclosure before selfie step

```tsx
import { useState } from 'react';

export function KYCFlowClean() {
  const [step, setStep] = useState(1);

  return (
    <div className="flex min-h-screen items-center justify-center bg-[#FAFAFA]">
      <div className="w-full max-w-[480px] rounded-2xl bg-white p-8 shadow-sm">
        {/* Progress */}
        <div className="flex items-center justify-between mb-8">
          {['Info', 'Document', 'Selfie', 'Review'].map((label, i) => (
            <div key={label} className="flex items-center gap-2">
              <div className={`flex h-6 w-6 items-center justify-center rounded-full text-xs font-medium ${
                i + 1 <= step ? 'bg-gray-900 text-white' : 'bg-gray-200 text-gray-500'
              }`}>
                {i + 1}
              </div>
              <span className={`text-xs ${i + 1 <= step ? 'text-gray-900' : 'text-gray-400'}`}>{label}</span>
            </div>
          ))}
        </div>

        {step === 1 && (
          <div>
            <h2 className="text-lg font-semibold text-gray-900">Verify your identity</h2>
            <p className="mt-2 text-sm text-gray-500">
              Federal regulations require us to verify your identity. Your information is encrypted and stored securely.
            </p>
            <div className="mt-2 flex items-center gap-2">
              <span className="text-green-600 text-xs">lock</span>
              <span className="text-xs text-green-600">256-bit encryption</span>
            </div>
            <div className="mt-6 space-y-4">
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="text-xs font-medium text-gray-600">Legal first name</label>
                  <input type="text" className="mt-1 w-full rounded-lg border border-gray-200 px-3 py-2.5 text-sm focus:border-gray-900 focus:outline-none" />
                </div>
                <div>
                  <label className="text-xs font-medium text-gray-600">Legal last name</label>
                  <input type="text" className="mt-1 w-full rounded-lg border border-gray-200 px-3 py-2.5 text-sm focus:border-gray-900 focus:outline-none" />
                </div>
              </div>
              <div>
                <label className="text-xs font-medium text-gray-600">Date of birth</label>
                <input type="date" className="mt-1 w-full rounded-lg border border-gray-200 px-3 py-2.5 text-sm focus:border-gray-900 focus:outline-none" />
              </div>
              <div>
                <label className="text-xs font-medium text-gray-600">SSN (last 4 digits)</label>
                <input type="password" maxLength={4} placeholder="****" className="mt-1 w-full rounded-lg border border-gray-200 px-3 py-2.5 text-sm focus:border-gray-900 focus:outline-none" />
                <p className="mt-1 text-[10px] text-gray-400">Required by the USA PATRIOT Act for identity verification.</p>
              </div>
              <div>
                <label className="text-xs font-medium text-gray-600">Address</label>
                <input type="text" placeholder="Street address" className="mt-1 w-full rounded-lg border border-gray-200 px-3 py-2.5 text-sm focus:border-gray-900 focus:outline-none" />
              </div>
            </div>
          </div>
        )}

        {step === 2 && (
          <div>
            <h2 className="text-lg font-semibold text-gray-900">Upload your ID</h2>
            <p className="mt-2 text-sm text-gray-500">Take a photo of your government-issued ID. We accept driver's license, passport, or state ID.</p>
            <div className="mt-6 space-y-4">
              <div className="flex flex-col items-center gap-3 rounded-xl border-2 border-dashed border-gray-200 p-8 hover:border-gray-400 cursor-pointer">
                <span className="text-gray-400">camera icon</span>
                <p className="text-sm font-medium text-gray-600">Front of ID</p>
                <p className="text-xs text-gray-400">Tap to upload or take photo</p>
              </div>
              <div className="flex flex-col items-center gap-3 rounded-xl border-2 border-dashed border-gray-200 p-8 hover:border-gray-400 cursor-pointer">
                <span className="text-gray-400">camera icon</span>
                <p className="text-sm font-medium text-gray-600">Back of ID</p>
                <p className="text-xs text-gray-400">Tap to upload or take photo</p>
              </div>
            </div>
          </div>
        )}

        {step === 3 && (
          <div className="text-center">
            <h2 className="text-lg font-semibold text-gray-900">Take a selfie</h2>
            <p className="mt-2 text-sm text-gray-500">Position your face in the frame. We use this to match your ID photo.</p>
            <div className="mt-6 mx-auto flex h-48 w-48 items-center justify-center rounded-full border-4 border-gray-200 bg-gray-50">
              <span className="text-gray-400">camera</span>
            </div>
            <p className="mt-4 text-[10px] text-gray-400">
              Your selfie is used only for identity verification and is not stored after verification is complete.
            </p>
          </div>
        )}

        {step === 4 && (
          <div className="text-center">
            <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-blue-50">
              <span className="text-2xl text-blue-600">hourglass</span>
            </div>
            <h2 className="mt-4 text-lg font-semibold text-gray-900">Verification in progress</h2>
            <p className="mt-2 text-sm text-gray-500">This usually takes 1-2 minutes. We will notify you when complete.</p>
          </div>
        )}

        <div className="mt-8">
          <button onClick={() => setStep(Math.min(step + 1, 4))} className="w-full rounded-lg bg-gray-900 py-3 text-sm font-medium text-white hover:bg-gray-800">
            {step === 4 ? 'Done' : 'Continue'}
          </button>
          {step < 4 && (
            <p className="mt-4 text-center text-[10px] text-gray-400">
              By continuing, you agree to our <a href="#" className="underline">Privacy Policy</a> and consent to identity verification.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Bold Fintech — Dark bg, animated face detection overlay, green progress checkmarks

---

## Cross-Variant Summary Matrix

| Page | Clean Modern (Mercury/Wise) | Bold Fintech (Cash App/Robinhood) |
|---|---|---|
| Dashboard | White, sidebar nav, account cards | Black, tab nav, single balance focus |
| Transactions | White, date-grouped list, search + filters | Dark, swipe actions, large amounts |
| Transfer | White card on gray bg, stepped flow | Dark bg, large green amount, confetti |
| Portfolio | White, clean data table, muted chart | Dark, animated chart, green/red coding |
| Card | White, realistic card render, toggle controls | Dark, neon accents, tap-to-reveal |
| Bills | White, payee list, scheduled view | Dark, quick-pay grid, gamified |
| Loan App | White, multi-step form, progress bar | Dark, slide-to-confirm, instant decision |
| Budget | White, progress rings, clean projections | Dark, animated progress, celebrations |
| Insights | White, horizontal bars, amber alerts | Dark, animated charts, green highlights |
| KYC | White card, numbered steps, secure badges | Dark, animated overlays, checkmarks |

---

## Data Security UI Pattern Library

### Sensitive Data Display
- Account numbers: Always masked (****4821), never display full
- SSN: Mask immediately after entry, show only last 4
- Card CVV: Require biometric to reveal, auto-hide after 30 seconds
- Balance: Offer "hide balance" toggle for public viewing

### Authentication States
- Active session indicator (green dot)
- Session timeout warning at 13 minutes (of 15)
- Biometric prompt for sensitive operations
- Step-up authentication for large transfers

### Encryption Indicators
- Lock icon + "Encrypted" label during data entry
- Green shield during document upload
- "Secure connection" in transfer flows
- Certificate info accessible but not prominent

### Error States for Financial Data
- Insufficient funds: Clear, non-judgmental language
- Transfer failed: Actionable next steps, reference number
- Verification failed: Appeal process clearly linked
- Rate expired: Auto-refresh with countdown

---

## Implementation Notes

### Number Formatting
Always use consistent number formatting:
```tsx
// Currency
amount.toLocaleString('en-US', { style: 'currency', currency: 'USD' })

// Percentages
value.toLocaleString('en-US', { style: 'percent', minimumFractionDigits: 2 })

// Account numbers
`****${accountNumber.slice(-4)}`
```

### Accessibility Requirements
- All financial data must be accessible to screen readers
- Color is never the sole indicator of positive/negative (use +/- prefix)
- Transaction tables must have proper th/scope for screen readers
- Charts must have text alternatives with data tables
- Minimum touch target: 44x44px for all financial actions

### Design Token Integration
These templates work with tokens from `fintech-banking-style.md`. Replace hardcoded values for production use.
