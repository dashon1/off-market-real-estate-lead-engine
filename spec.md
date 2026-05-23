# Off-Market Real Estate Lead Engine — Sales Page Specification

## 1. Concept & Vision

A premium digital product sales page for real estate investors seeking a systematic approach to building an off-market lead pipeline. The page exudes professional authority and trust — like a high-end investment course meets sleek real estate branding. The visual language communicates "serious money system" with earthy sophistication, avoiding generic SaaS aesthetics.

## 2. Design Language

### Aesthetic Direction
Premium editorial meets real estate authority. Think high-end investment firm brochure crossed with modern SaaS elegance. Clean, confident, trustworthy.

### Color Palette
- **Primary:** #1C1917 (Rich Charcoal)
- **Secondary:** #78716C (Warm Stone)
- **Accent:** #D97706 (Amber Gold)
- **Background:** #FAFAF9 (Warm White)
- **Surface:** #F5F5F4 (Light Stone)
- **Text Primary:** #1C1917
- **Text Secondary:** #57534E
- **Success:** #059669 (Emerald for checkmarks)

### Typography
- **Headlines:** Inter, 700 weight, tracking -0.02em
- **Subheadings:** Inter, 600 weight
- **Body:** Inter, 400 weight, line-height 1.7
- **Accent Text:** Inter, 500 weight

### Spatial System
- Section padding: 80px vertical (desktop), 48px (mobile)
- Content max-width: 1200px
- Grid: 12-column, 24px gutters
- Card spacing: 24px gap

### Motion Philosophy
- Subtle fade-up on scroll (300ms ease-out)
- Button hover: scale 1.02, shadow lift
- Smooth anchor scrolling
- Staggered card reveals (100ms delay)

## 3. Layout & Structure

### Page Flow
1. **Hero Section** — Full-viewport with bold headline, value proposition, CTA
2. **Problem/Solution** — Two-column contrast blocks
3. **What's Inside** — Feature cards with deliverables
4. **Who This Is For** — Persona list with benefit focus
5. **Pricing** — Three-tier cards (Starter/Standard/Premium)
6. **Testimonials** — Placeholder social proof section
7. **FAQ** — Accordion-style common questions
8. **Final CTA** — Urgency-driven conversion section

### Responsive Strategy
- Desktop: Full layouts, side-by-side content
- Tablet: Stacked where needed, maintained visual hierarchy
- Mobile: Single column, increased touch targets, condensed spacing

## 4. Features & Interactions

### Hero Section
- Large headline with amber accent underline
- Subheadline explaining the transformation
- Primary CTA button with hover lift effect
- Secondary link to "See What's Inside"
- Trust badges (what they get: 30-day system, instant access)

### Product Cards
- Icon + title + description
- Subtle border, hover shadow elevation
- Format badge indicating PDF/Template/Tool

### Pricing Cards
- Three columns with center card elevated
- "Most Popular" badge on Standard tier
- Price with strikethrough original
- Feature checklist with checkmarks
- CTA button per tier

### FAQ Accordion
- Click to expand/collapse
- Smooth height animation
- Plus/minus icon toggle

### CTA Buttons
- Primary: Amber background, dark text, hover scale
- Secondary: Outlined, hover fill

## 5. Component Inventory

### Buttons
- **Primary:** bg-amber-600, white text, rounded-lg, hover:scale-102, shadow
- **Secondary:** border-2 border-stone-800, transparent bg, hover:bg-stone-100

### Cards
- bg-white, border border-stone-200, rounded-xl, shadow-sm, hover:shadow-lg

### Icons
- Lucide-style inline SVGs (minimal, consistent stroke)

### Badges
- Small rounded pills for format types (PDF, Template, etc.)

## 6. Technical Approach

- **Stack:** Single HTML file with embedded CSS and vanilla JS
- **No frameworks** — Pure HTML5 + CSS3 + minimal JS
- **Fonts:** Google Fonts (Inter)
- **Icons:** Inline SVGs
- **CSS:** Custom properties for theming, flexbox/grid layouts
- **JS:** Intersection Observer for scroll animations, accordion toggle