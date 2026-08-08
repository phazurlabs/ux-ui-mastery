# E-Commerce Page Templates — Complete Implementation Guide

## Overview

This reference provides complete page-level templates for 10 essential e-commerce pages. Each template includes block sequence, typography, color application, spacing rhythm, component selection, responsive behavior, and React/TSX skeletons. Every page is provided in two style variants: Premium (Apple Store) and Marketplace (Shopify/Amazon).

Every template includes conversion optimization notes, trust signals, and urgency patterns specific to e-commerce.

---

## E-Commerce Design Principles

### Conversion Architecture
E-commerce pages exist to convert. Every design decision must be evaluated through conversion rate impact:
1. **Reduce friction** — Minimize steps between desire and purchase
2. **Build trust** — Reviews, security badges, return policies visible at decision points
3. **Create urgency** — Stock levels, time-limited offers, social proof
4. **Guide attention** — Visual hierarchy points to CTAs
5. **Reduce anxiety** — Clear pricing, no hidden fees, easy returns

### Trust Signal Placement Rules
- **Product page**: Reviews, ratings, return policy, secure checkout badge near Add to Cart
- **Cart**: Order summary, coupon field, shipping estimate, security badges
- **Checkout**: SSL badge, payment logos, money-back guarantee, support contact
- **Confirmation**: Order number, tracking promise, customer service link

---

## 1. Product Listing Page (with Filters)

### Block Sequence
1. Breadcrumb navigation
2. Category header (title + result count + sort)
3. Filter sidebar (collapsible on mobile)
4. Product grid (cards with image, title, price, rating)
5. Pagination or load more
6. Recently viewed strip (optional)

### Variant A: Premium (Apple Store Style)

**Typography Map**
| Element | Font | Weight | Size | Line-Height |
|---|---|---|---|---|
| Category title | SF Pro Display / system | 600 | 32px | 40px |
| Product name | SF Pro / system | 500 | 15px | 22px |
| Price | SF Pro / system | 600 | 17px | 24px |
| Original price | SF Pro / system | 400 | 14px | 20px |
| Filter label | SF Pro / system | 500 | 13px | 18px |
| Result count | SF Pro / system | 400 | 13px | 18px |
| Rating text | SF Pro / system | 400 | 12px | 16px |

**Color Application**
```
Background:             #FFFFFF
Product card bg:        #FFFFFF (no visible border, hover shadow)
Image container bg:     #F5F5F7 (Apple's signature gray)
Text primary:           #1D1D1F
Text secondary:         #86868B
Price text:             #1D1D1F
Sale price:             #BF4800 (Apple's sale orange-red)
Original price:         #86868B with line-through
Filter sidebar bg:      #FFFFFF
Filter active:          #0066CC (Apple blue)
Rating stars:           #F5A623
Sort dropdown:          border #D2D2D7
```

**Spacing Rhythm**
```
Category header:        padding 48px 0
Grid gap:               24px
Product card padding:   0 (image bleeds, text below)
Image aspect ratio:     1:1 (square) or 4:5 (tall)
Card image height:      280px
Card text padding:      16px
Filter sidebar width:   240px
Filter gap:             24px between groups
Page max-width:         1440px
Content padding:        0 48px
```

**Conversion Optimization**
- Large product images (focus on product, minimal styling)
- Quick view on hover (desktop)
- "New" and "Sale" badges positioned top-left of image
- Color variant swatches below image (max 4, then "+3")
- Price always visible without scrolling on each card
- Lazy-loaded images with skeleton placeholders

**React/TSX Skeleton**
```tsx
import { useState } from 'react';

export function ProductListingPremium() {
  const [showFilters, setShowFilters] = useState(true);

  const products = Array.from({ length: 12 }, (_, i) => ({
    id: i + 1,
    name: `Product Name ${i + 1}`,
    price: 199 + i * 50,
    originalPrice: i % 3 === 0 ? 249 + i * 50 : null,
    rating: 4.5 + Math.random() * 0.5,
    reviews: Math.floor(Math.random() * 500) + 10,
    colors: ['#1D1D1F', '#86868B', '#F5F5F7'],
    badge: i === 0 ? 'New' : i === 3 ? 'Sale' : null,
  }));

  return (
    <div className="min-h-screen bg-white">
      {/* Breadcrumb */}
      <div className="mx-auto max-w-[1440px] px-12 pt-4">
        <nav className="flex items-center gap-2 text-xs text-[#86868B]">
          <a href="/" className="hover:text-[#1D1D1F]">Home</a>
          <span>/</span>
          <a href="#" className="hover:text-[#1D1D1F]">Category</a>
          <span>/</span>
          <span className="text-[#1D1D1F]">Subcategory</span>
        </nav>
      </div>

      {/* Header */}
      <div className="mx-auto max-w-[1440px] px-12 pt-8 pb-6">
        <div className="flex items-end justify-between">
          <div>
            <h1 className="text-[32px] font-semibold text-[#1D1D1F]">Category Name</h1>
            <p className="mt-1 text-sm text-[#86868B]">124 products</p>
          </div>
          <div className="flex items-center gap-4">
            <button onClick={() => setShowFilters(!showFilters)} className="text-sm text-[#0066CC]">
              {showFilters ? 'Hide Filters' : 'Show Filters'}
            </button>
            <select className="rounded-lg border border-[#D2D2D7] px-3 py-2 text-sm text-[#1D1D1F]">
              <option>Featured</option>
              <option>Price: Low to High</option>
              <option>Price: High to Low</option>
              <option>Newest</option>
              <option>Best Rating</option>
            </select>
          </div>
        </div>
      </div>

      {/* Content */}
      <div className="mx-auto max-w-[1440px] px-12 pb-16">
        <div className="flex gap-8">
          {/* Filters */}
          {showFilters && (
            <aside className="w-60 flex-shrink-0 space-y-6">
              {['Category', 'Price Range', 'Color', 'Size', 'Rating'].map((filter) => (
                <div key={filter}>
                  <h3 className="text-sm font-medium text-[#1D1D1F]">{filter}</h3>
                  <div className="mt-3 space-y-2">
                    {[1, 2, 3].map((opt) => (
                      <label key={opt} className="flex items-center gap-2 text-sm text-[#86868B] hover:text-[#1D1D1F] cursor-pointer">
                        <input type="checkbox" className="rounded border-[#D2D2D7]" />
                        Option {opt}
                      </label>
                    ))}
                  </div>
                </div>
              ))}
            </aside>
          )}

          {/* Grid */}
          <div className={`flex-1 grid gap-6 ${showFilters ? 'grid-cols-2 lg:grid-cols-3' : 'grid-cols-2 lg:grid-cols-4'}`}>
            {products.map((p) => (
              <a key={p.id} href="#" className="group">
                <div className="relative aspect-square rounded-2xl bg-[#F5F5F7] overflow-hidden">
                  <div className="absolute inset-0 flex items-center justify-center text-gray-400">
                    Product Image
                  </div>
                  {p.badge && (
                    <span className={`absolute left-3 top-3 rounded-full px-2.5 py-1 text-[11px] font-medium ${
                      p.badge === 'New' ? 'bg-[#1D1D1F] text-white' : 'bg-[#BF4800] text-white'
                    }`}>
                      {p.badge}
                    </span>
                  )}
                </div>
                <div className="mt-4">
                  <div className="flex items-center gap-1">
                    <span className="text-xs text-[#F5A623]">stars</span>
                    <span className="text-xs text-[#86868B]">({p.reviews})</span>
                  </div>
                  <h3 className="mt-1 text-[15px] font-medium text-[#1D1D1F] group-hover:text-[#0066CC]">{p.name}</h3>
                  <div className="mt-1 flex items-center gap-2">
                    <span className="text-[17px] font-semibold text-[#1D1D1F]">${p.price}</span>
                    {p.originalPrice && (
                      <span className="text-sm text-[#86868B] line-through">${p.originalPrice}</span>
                    )}
                  </div>
                  <div className="mt-2 flex gap-1.5">
                    {p.colors.map((color, ci) => (
                      <div key={ci} className="h-3 w-3 rounded-full border border-gray-300" style={{ backgroundColor: color }} />
                    ))}
                  </div>
                </div>
              </a>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Marketplace (Shopify/Amazon Style)

**Key Differences**
- Denser grid (4-5 columns)
- Cards have visible borders and hover elevation
- Price more prominent, reviews count bigger
- "Add to cart" button visible on each card
- "Sponsored" labels on some cards
- Shipping info ("Free shipping") on each card
- Background is light gray (#F8F8F8) not white

---

## 2. Product Detail Page

### Block Sequence
1. Breadcrumb
2. Image gallery (main image + thumbnails)
3. Product info (title, price, variants, add to cart)
4. Description and specifications tabs
5. Reviews section (summary + individual reviews)
6. Related products carousel
7. Recently viewed strip

### Variant A: Premium (Apple Store Style)

**Layout**: Full-width hero image approach, then centered content

**React/TSX Skeleton**
```tsx
import { useState } from 'react';

export function ProductDetailPremium() {
  const [selectedColor, setSelectedColor] = useState(0);
  const [selectedSize, setSelectedSize] = useState('');
  const [quantity, setQuantity] = useState(1);

  const colors = [
    { name: 'Space Black', hex: '#1D1D1F' },
    { name: 'Silver', hex: '#E3E3E8' },
    { name: 'Gold', hex: '#F4E8CE' },
  ];

  return (
    <div className="min-h-screen bg-white">
      {/* Breadcrumb */}
      <div className="mx-auto max-w-[1200px] px-6 pt-4">
        <nav className="text-xs text-[#86868B]">
          <a href="/" className="hover:text-[#1D1D1F]">Home</a> / <a href="#" className="hover:text-[#1D1D1F]">Category</a> / <span className="text-[#1D1D1F]">Product Name</span>
        </nav>
      </div>

      {/* Product Section */}
      <div className="mx-auto max-w-[1200px] px-6 py-12 md:flex md:gap-16">
        {/* Gallery */}
        <div className="md:w-1/2">
          <div className="aspect-square rounded-2xl bg-[#F5F5F7] flex items-center justify-center">
            <span className="text-gray-400">Main Product Image</span>
          </div>
          <div className="mt-4 flex gap-3">
            {[1, 2, 3, 4].map((i) => (
              <button key={i} className="h-20 w-20 rounded-xl bg-[#F5F5F7] border-2 border-transparent hover:border-[#0066CC] transition-colors" />
            ))}
          </div>
        </div>

        {/* Product Info */}
        <div className="mt-8 md:mt-0 md:w-1/2">
          <div className="flex items-center gap-2">
            <span className="text-xs text-[#F5A623]">stars</span>
            <a href="#reviews" className="text-xs text-[#0066CC]">247 reviews</a>
          </div>

          <h1 className="mt-3 text-3xl font-semibold text-[#1D1D1F]">Premium Product Name</h1>
          <p className="mt-3 text-lg text-[#86868B]">Brief product tagline that communicates the core value proposition.</p>

          <div className="mt-6">
            <span className="text-2xl font-semibold text-[#1D1D1F]">$299</span>
            <span className="ml-2 text-sm text-[#86868B] line-through">$349</span>
            <span className="ml-2 rounded-full bg-[#BF4800]/10 px-2 py-0.5 text-xs font-medium text-[#BF4800]">Save $50</span>
          </div>

          {/* Color Selection */}
          <div className="mt-8">
            <p className="text-sm font-medium text-[#1D1D1F]">Color: <span className="font-normal text-[#86868B]">{colors[selectedColor].name}</span></p>
            <div className="mt-3 flex gap-3">
              {colors.map((c, i) => (
                <button key={c.name} onClick={() => setSelectedColor(i)}
                  className={`h-10 w-10 rounded-full border-2 ${i === selectedColor ? 'border-[#0066CC]' : 'border-[#D2D2D7]'}`}
                  style={{ backgroundColor: c.hex }} />
              ))}
            </div>
          </div>

          {/* Size Selection */}
          <div className="mt-6">
            <div className="flex items-center justify-between">
              <p className="text-sm font-medium text-[#1D1D1F]">Size</p>
              <a href="#" className="text-xs text-[#0066CC]">Size guide</a>
            </div>
            <div className="mt-3 flex gap-2">
              {['S', 'M', 'L', 'XL'].map((size) => (
                <button key={size} onClick={() => setSelectedSize(size)}
                  className={`flex h-10 w-14 items-center justify-center rounded-lg border text-sm font-medium ${
                    selectedSize === size ? 'border-[#1D1D1F] bg-[#1D1D1F] text-white' : 'border-[#D2D2D7] text-[#1D1D1F] hover:border-[#1D1D1F]'
                  }`}>
                  {size}
                </button>
              ))}
            </div>
          </div>

          {/* Add to Cart */}
          <div className="mt-8 space-y-3">
            <button className="w-full rounded-xl bg-[#0066CC] py-4 text-base font-medium text-white hover:bg-[#0055AA] transition-colors">
              Add to Bag
            </button>
            <button className="w-full rounded-xl border border-[#0066CC] py-4 text-base font-medium text-[#0066CC] hover:bg-[#0066CC]/5">
              Save for Later
            </button>
          </div>

          {/* Trust Signals */}
          <div className="mt-8 space-y-3 border-t border-[#D2D2D7] pt-6">
            <div className="flex items-center gap-3 text-sm text-[#1D1D1F]">
              <span className="text-[#86868B]">truck</span>
              Free shipping on orders over $50
            </div>
            <div className="flex items-center gap-3 text-sm text-[#1D1D1F]">
              <span className="text-[#86868B]">return</span>
              Free 30-day returns
            </div>
            <div className="flex items-center gap-3 text-sm text-[#1D1D1F]">
              <span className="text-[#86868B]">shield</span>
              2-year warranty included
            </div>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="border-t border-[#D2D2D7]">
        <div className="mx-auto max-w-[1200px] px-6 py-12">
          <div className="flex gap-8 border-b border-[#D2D2D7]">
            {['Description', 'Specifications', 'Reviews (247)'].map((tab, i) => (
              <button key={tab} className={`pb-4 text-sm font-medium ${i === 0 ? 'border-b-2 border-[#1D1D1F] text-[#1D1D1F]' : 'text-[#86868B]'}`}>
                {tab}
              </button>
            ))}
          </div>
          <div className="mt-8 max-w-[720px]">
            <p className="text-sm leading-relaxed text-[#86868B]">
              Detailed product description with features, materials, and care instructions.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Marketplace — Side-by-side layout, prominent Buy Box, seller info, shipping options, "Customers also bought"

**Conversion Notes**
- Sticky Add to Cart on mobile scroll
- "Only 3 left" urgency for low stock
- "32 people viewing this" social proof
- Express checkout (Apple Pay / Google Pay) above standard Add to Cart
- Estimated delivery date based on zip code

---

## 3. Shopping Cart

### Block Sequence
1. Cart header (item count)
2. Cart items list (image, title, variant, quantity, price, remove)
3. Coupon code input
4. Order summary (subtotal, shipping estimate, tax, total)
5. Checkout CTA (with express checkout options)
6. Continue shopping link
7. Trust signals footer

### Variant A: Premium

```tsx
export function CartPremium() {
  const items = [
    { name: 'Premium Product', variant: 'Space Black / M', price: 299, quantity: 1 },
    { name: 'Another Product', variant: 'Silver / L', price: 149, quantity: 2 },
  ];

  return (
    <div className="min-h-screen bg-[#F5F5F7]">
      <div className="mx-auto max-w-[1000px] px-6 py-12">
        <h1 className="text-2xl font-semibold text-[#1D1D1F]">Your Bag</h1>
        <p className="mt-1 text-sm text-[#86868B]">{items.length} items</p>

        <div className="mt-8 lg:flex lg:gap-8">
          {/* Cart Items */}
          <div className="flex-1 space-y-4">
            {items.map((item, idx) => (
              <div key={idx} className="flex gap-6 rounded-2xl bg-white p-6">
                <div className="h-28 w-28 flex-shrink-0 rounded-xl bg-[#F5F5F7]" />
                <div className="flex-1">
                  <div className="flex items-start justify-between">
                    <div>
                      <h3 className="text-[15px] font-medium text-[#1D1D1F]">{item.name}</h3>
                      <p className="mt-1 text-sm text-[#86868B]">{item.variant}</p>
                    </div>
                    <p className="text-[15px] font-semibold text-[#1D1D1F]">${item.price * item.quantity}</p>
                  </div>
                  <div className="mt-4 flex items-center justify-between">
                    <div className="flex items-center gap-3 rounded-lg border border-[#D2D2D7]">
                      <button className="px-3 py-1.5 text-sm text-[#86868B] hover:text-[#1D1D1F]">-</button>
                      <span className="text-sm font-medium text-[#1D1D1F]">{item.quantity}</span>
                      <button className="px-3 py-1.5 text-sm text-[#86868B] hover:text-[#1D1D1F]">+</button>
                    </div>
                    <button className="text-sm text-[#0066CC]">Remove</button>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Summary */}
          <div className="mt-8 lg:mt-0 lg:w-80">
            <div className="rounded-2xl bg-white p-6">
              <h2 className="text-lg font-semibold text-[#1D1D1F]">Order Summary</h2>
              <div className="mt-4 space-y-3 text-sm">
                <div className="flex justify-between"><span className="text-[#86868B]">Subtotal</span><span className="text-[#1D1D1F]">$597.00</span></div>
                <div className="flex justify-between"><span className="text-[#86868B]">Shipping</span><span className="text-green-600">Free</span></div>
                <div className="flex justify-between"><span className="text-[#86868B]">Tax</span><span className="text-[#1D1D1F]">$47.76</span></div>
                <div className="border-t border-[#D2D2D7] pt-3 flex justify-between text-base font-semibold">
                  <span className="text-[#1D1D1F]">Total</span>
                  <span className="text-[#1D1D1F]">$644.76</span>
                </div>
              </div>

              <div className="mt-6 space-y-3">
                <button className="w-full rounded-xl bg-[#1D1D1F] py-3.5 text-sm font-medium text-white hover:bg-black">
                  Apple Pay
                </button>
                <button className="w-full rounded-xl bg-[#0066CC] py-3.5 text-sm font-medium text-white hover:bg-[#0055AA]">
                  Checkout
                </button>
              </div>

              {/* Trust */}
              <div className="mt-6 flex items-center justify-center gap-2 text-xs text-[#86868B]">
                <span>lock</span> Secure checkout
              </div>
            </div>

            {/* Coupon */}
            <div className="mt-4 rounded-2xl bg-white p-6">
              <div className="flex gap-2">
                <input type="text" placeholder="Promo code" className="flex-1 rounded-lg border border-[#D2D2D7] px-3 py-2 text-sm focus:border-[#0066CC] focus:outline-none" />
                <button className="rounded-lg bg-[#F5F5F7] px-4 py-2 text-sm font-medium text-[#1D1D1F] hover:bg-[#E8E8ED]">Apply</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Marketplace — Denser layout, estimated delivery dates per item, "Save for later" section, "Frequently bought together"

---

## 4. Checkout Flow (4 Steps)

### Block Sequence
- **Step 1**: Contact information (email, phone)
- **Step 2**: Shipping address + method
- **Step 3**: Payment (card, PayPal, Apple Pay)
- **Step 4**: Review and place order

### Variant A: Premium

**Conversion Optimization**
- Single-page accordion checkout (all steps visible, expand one at a time)
- Express checkout (Apple Pay, Google Pay) above form
- Guest checkout prominent, account creation optional
- Address autocomplete
- Real-time shipping calculation
- Order summary always visible on desktop (right sidebar)

```tsx
export function CheckoutPremium() {
  return (
    <div className="min-h-screen bg-white">
      {/* Minimal nav */}
      <nav className="border-b border-[#D2D2D7] py-4">
        <div className="mx-auto max-w-[1100px] px-6 flex items-center justify-between">
          <a href="/" className="text-base font-semibold text-[#1D1D1F]">StoreName</a>
          <div className="flex items-center gap-2">
            <span className="text-xs text-[#86868B]">lock</span>
            <span className="text-xs text-[#86868B]">Secure Checkout</span>
          </div>
        </div>
      </nav>

      <div className="mx-auto max-w-[1100px] px-6 py-12 lg:flex lg:gap-16">
        {/* Form Side */}
        <div className="flex-1">
          {/* Express Checkout */}
          <div className="space-y-3">
            <button className="w-full rounded-xl bg-[#1D1D1F] py-3.5 text-sm font-medium text-white">Apple Pay</button>
            <button className="w-full rounded-xl bg-[#FFC439] py-3.5 text-sm font-medium text-[#1D1D1F]">PayPal</button>
          </div>

          <div className="my-8 flex items-center gap-4">
            <div className="h-px flex-1 bg-[#D2D2D7]" />
            <span className="text-xs text-[#86868B]">Or pay with card</span>
            <div className="h-px flex-1 bg-[#D2D2D7]" />
          </div>

          {/* Contact */}
          <section>
            <h2 className="text-lg font-semibold text-[#1D1D1F]">Contact</h2>
            <input type="email" placeholder="Email address" className="mt-3 w-full rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
          </section>

          {/* Shipping */}
          <section className="mt-8">
            <h2 className="text-lg font-semibold text-[#1D1D1F]">Shipping address</h2>
            <div className="mt-3 space-y-3">
              <div className="grid grid-cols-2 gap-3">
                <input type="text" placeholder="First name" className="rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
                <input type="text" placeholder="Last name" className="rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
              </div>
              <input type="text" placeholder="Address" className="w-full rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
              <div className="grid grid-cols-3 gap-3">
                <input type="text" placeholder="City" className="rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
                <select className="rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm text-[#86868B]"><option>State</option></select>
                <input type="text" placeholder="ZIP" className="rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
              </div>
            </div>
          </section>

          {/* Shipping Method */}
          <section className="mt-8">
            <h2 className="text-lg font-semibold text-[#1D1D1F]">Shipping method</h2>
            <div className="mt-3 space-y-2">
              {[
                { name: 'Standard', time: '5-7 business days', price: 'Free' },
                { name: 'Express', time: '2-3 business days', price: '$12.99' },
                { name: 'Overnight', time: '1 business day', price: '$24.99' },
              ].map((method, i) => (
                <label key={method.name} className={`flex items-center justify-between rounded-lg border p-4 cursor-pointer ${i === 0 ? 'border-[#0066CC] bg-[#0066CC]/5' : 'border-[#D2D2D7]'}`}>
                  <div className="flex items-center gap-3">
                    <input type="radio" name="shipping" defaultChecked={i === 0} className="accent-[#0066CC]" />
                    <div>
                      <p className="text-sm font-medium text-[#1D1D1F]">{method.name}</p>
                      <p className="text-xs text-[#86868B]">{method.time}</p>
                    </div>
                  </div>
                  <span className={`text-sm font-medium ${method.price === 'Free' ? 'text-green-600' : 'text-[#1D1D1F]'}`}>{method.price}</span>
                </label>
              ))}
            </div>
          </section>

          {/* Payment */}
          <section className="mt-8">
            <h2 className="text-lg font-semibold text-[#1D1D1F]">Payment</h2>
            <div className="mt-3 space-y-3">
              <input type="text" placeholder="Card number" className="w-full rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
              <div className="grid grid-cols-2 gap-3">
                <input type="text" placeholder="MM / YY" className="rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
                <input type="text" placeholder="CVV" className="rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
              </div>
            </div>
            <div className="mt-3 flex items-center gap-2">
              <span className="text-[10px] text-[#86868B]">Accepted:</span>
              {['Visa', 'MC', 'Amex'].map((card) => (
                <span key={card} className="rounded bg-[#F5F5F7] px-2 py-0.5 text-[10px] text-[#86868B]">{card}</span>
              ))}
            </div>
          </section>

          <button className="mt-10 w-full rounded-xl bg-[#0066CC] py-4 text-base font-medium text-white hover:bg-[#0055AA]">
            Place Order - $644.76
          </button>
        </div>

        {/* Order Summary Sidebar */}
        <div className="hidden lg:block lg:w-80">
          <div className="sticky top-8 rounded-2xl bg-[#F5F5F7] p-6">
            <h2 className="text-base font-semibold text-[#1D1D1F]">Order Summary</h2>
            <div className="mt-4 space-y-4">
              {[1, 2].map((i) => (
                <div key={i} className="flex gap-3">
                  <div className="relative h-16 w-16 flex-shrink-0 rounded-lg bg-white">
                    <span className="absolute -right-1 -top-1 flex h-5 w-5 items-center justify-center rounded-full bg-[#86868B] text-[10px] text-white">1</span>
                  </div>
                  <div>
                    <p className="text-sm font-medium text-[#1D1D1F]">Product {i}</p>
                    <p className="text-xs text-[#86868B]">Variant</p>
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-6 space-y-2 border-t border-[#D2D2D7] pt-4 text-sm">
              <div className="flex justify-between"><span className="text-[#86868B]">Subtotal</span><span>$597.00</span></div>
              <div className="flex justify-between"><span className="text-[#86868B]">Shipping</span><span className="text-green-600">Free</span></div>
              <div className="flex justify-between"><span className="text-[#86868B]">Tax</span><span>$47.76</span></div>
              <div className="flex justify-between font-semibold text-base pt-2 border-t border-[#D2D2D7]">
                <span>Total</span><span>$644.76</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```

### Variant B: Marketplace — Multi-step with progress bar, saved addresses, multiple seller shipping

---

## 5. Order Confirmation

### Block Sequence
1. Success icon and headline
2. Order number and email confirmation note
3. Order summary (items, totals)
4. Shipping details and estimated delivery
5. What happens next timeline
6. Continue shopping CTA
7. Account creation prompt (for guest checkout)

### Trust Signals: Order number, email confirmation promise, tracking promise, support contact

---

## 6. Order Tracking

### Block Sequence
1. Order header (order number, date, status)
2. Tracking timeline (ordered, processed, shipped, delivered)
3. Shipping details (carrier, tracking number, estimated delivery)
4. Map visualization (optional)
5. Order items list
6. Need help section

---

## 7. Customer Account / Dashboard

### Block Sequence
1. Welcome header + account summary
2. Recent orders (last 3-5)
3. Saved addresses
4. Saved payment methods (masked)
5. Wishlist preview
6. Account settings link

---

## 8. Wishlist Page

### Block Sequence
1. Page header (item count + share link)
2. Wishlist grid (product cards with "Add to Cart" and "Remove")
3. Price change alerts
4. "Move to cart" bulk action
5. Share wishlist functionality

### Urgency Patterns
- "Price dropped!" badge on items with reduced price
- "Only 2 left" stock warnings
- "Back in stock" notifications

---

## 9. Returns / Exchange Flow

### Block Sequence
1. Order selection (which order to return)
2. Item selection (which items, reason per item)
3. Return method (mail, in-store, pickup)
4. Refund method (original payment, store credit)
5. Confirmation with return label/instructions

### Trust Signals: Free return shipping, refund timeline, tracking

---

## 10. Review / Rating Submission

### Block Sequence
1. Product being reviewed (image + name)
2. Star rating input (5 stars, tap/click)
3. Review title and body text inputs
4. Photo/video upload (optional)
5. Fit/quality/value sub-ratings (optional)
6. Submission confirmation

```tsx
export function ReviewSubmission() {
  const [rating, setRating] = useState(0);

  return (
    <div className="min-h-screen bg-white">
      <div className="mx-auto max-w-[560px] px-6 py-12">
        {/* Product */}
        <div className="flex items-center gap-4 rounded-xl bg-[#F5F5F7] p-4">
          <div className="h-16 w-16 rounded-lg bg-white" />
          <div>
            <p className="text-sm font-medium text-[#1D1D1F]">Premium Product Name</p>
            <p className="text-xs text-[#86868B]">Space Black / M</p>
          </div>
        </div>

        <h1 className="mt-8 text-xl font-semibold text-[#1D1D1F]">Write a review</h1>

        {/* Star Rating */}
        <div className="mt-6">
          <p className="text-sm font-medium text-[#1D1D1F]">Overall rating</p>
          <div className="mt-2 flex gap-2">
            {[1, 2, 3, 4, 5].map((star) => (
              <button key={star} onClick={() => setRating(star)}
                className={`text-3xl ${star <= rating ? 'text-[#F5A623]' : 'text-[#D2D2D7]'}`}>
                star
              </button>
            ))}
          </div>
        </div>

        {/* Title */}
        <div className="mt-6">
          <label className="text-sm font-medium text-[#1D1D1F]">Review title</label>
          <input type="text" placeholder="Summarize your experience" className="mt-2 w-full rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none" />
        </div>

        {/* Body */}
        <div className="mt-6">
          <label className="text-sm font-medium text-[#1D1D1F]">Your review</label>
          <textarea rows={5} placeholder="What did you like or dislike? How did you use this product?" className="mt-2 w-full rounded-lg border border-[#D2D2D7] px-4 py-3 text-sm focus:border-[#0066CC] focus:outline-none resize-none" />
        </div>

        {/* Photos */}
        <div className="mt-6">
          <label className="text-sm font-medium text-[#1D1D1F]">Add photos (optional)</label>
          <div className="mt-2 flex gap-3">
            <button className="flex h-20 w-20 items-center justify-center rounded-lg border-2 border-dashed border-[#D2D2D7] hover:border-[#0066CC]">
              <span className="text-[#86868B]">+</span>
            </button>
          </div>
        </div>

        {/* Sub-ratings */}
        <div className="mt-6 space-y-4">
          {['Quality', 'Value for money', 'Fit'].map((sub) => (
            <div key={sub} className="flex items-center justify-between">
              <span className="text-sm text-[#86868B]">{sub}</span>
              <div className="flex gap-1">
                {[1, 2, 3, 4, 5].map((s) => (
                  <button key={s} className="text-lg text-[#D2D2D7] hover:text-[#F5A623]">star</button>
                ))}
              </div>
            </div>
          ))}
        </div>

        <button className="mt-8 w-full rounded-xl bg-[#0066CC] py-3.5 text-sm font-medium text-white hover:bg-[#0055AA]">
          Submit Review
        </button>
      </div>
    </div>
  );
}
```

---

## Cross-Variant Summary Matrix

| Page | Premium (Apple Store) | Marketplace (Shopify/Amazon) |
|---|---|---|
| Listing | Clean grid, large images, minimal info | Dense grid, add-to-cart on card, shipping info |
| Detail | Full-width images, minimal chrome | Side-by-side, buy box, seller info |
| Cart | Card-based items, clean summary | Dense list, delivery dates per item |
| Checkout | Single-page accordion, express checkout first | Multi-step, saved addresses |
| Confirmation | Minimal, elegant timeline | Detailed, cross-sell prominent |
| Tracking | Clean timeline, minimal | Detailed tracking, map |
| Account | Minimal dashboard, recent orders | Dense dashboard, order history |
| Wishlist | Clean grid, share | Dense, price alerts |
| Returns | Stepped flow, clean | Multi-item select, label generation |
| Reviews | Clean form, sub-ratings | Full form, photo upload, verified badge |

---

## Conversion Optimization Checklist

### Product Listing Page
- [ ] Above-the-fold product visibility (no empty space)
- [ ] Quick add-to-cart on hover/tap
- [ ] Filter count indicators (how many results per filter)
- [ ] Sort by relevance as default
- [ ] Infinite scroll or "Load more" (not pagination for mobile)

### Product Detail Page
- [ ] High-quality zoomable images
- [ ] Price and CTA visible without scrolling
- [ ] Reviews summary near price
- [ ] Stock status visible
- [ ] Related products below fold
- [ ] Sticky mobile CTA bar

### Checkout Flow
- [ ] Guest checkout option prominent
- [ ] Express checkout above form
- [ ] Address autocomplete
- [ ] Real-time validation
- [ ] Order summary always visible
- [ ] Security badges near payment fields
- [ ] Single "Place Order" button (no double-tap risk)

---

## Implementation Notes

### Image Handling
```tsx
// Product images should use responsive srcset
<img
  src="/product-400.jpg"
  srcSet="/product-400.jpg 400w, /product-800.jpg 800w, /product-1200.jpg 1200w"
  sizes="(max-width: 768px) 50vw, 33vw"
  alt="Product Name - Color Variant"
  loading="lazy"
/>
```

### Price Formatting
```tsx
const formatPrice = (cents: number) =>
  (cents / 100).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
```

### Design Token Integration
Replace hardcoded values with tokens from `ecommerce-marketplace-style.md` for production use.
