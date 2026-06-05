# 🎨 Kinetic AI - Complete Design Specification

## 🎯 Design System Overview

**Project:** Kinetic AI - RAG Personal Trainer  
**Version:** 2.0 (HTML/Tailwind Implementation)  
**Date:** April 2026  
**Framework:** Tailwind CSS + Custom Material Design 3 Colors  

---

## 🎨 Color System (Material Design 3)

### Primary Palette

```css
--primary: #006666;           /* Teal - Main brand color */
--primary-dim: #005959;       /* Darker teal for hover */
--primary-fixed: #73f0ef;     /* Light teal accent */
--primary-fixed-dim: #63e1e1; /* Medium teal */
--on-primary: #bbfffe;        /* Text on primary */
--on-primary-fixed: #004343;  /* Text on light primary */
--on-primary-container: #005858;
--inverse-primary: #79f6f5;
```

### Secondary Palette

```css
--secondary: #b61321;          /* Red - Accent/CTA */
--secondary-dim: #a40018;      /* Darker red */
--secondary-fixed: #ffc3be;    /* Light red */
--secondary-fixed-dim: #ffafaa;
--on-secondary: #ffefee;       /* Text on secondary */
--on-secondary-fixed: #70000d;
--on-secondary-container: #940014;
```

### Surface & Background

```css
--background: #f4f6fa;
--surface: #f4f6fa;
--surface-bright: #f4f6fa;
--surface-dim: #d0d5db;
--surface-container-lowest: #ffffff;  /* Cards, input */
--surface-container-low: #eef1f5;     /* Sidebar */
--surface-container: #e5e8ed;
--surface-container-high: #dfe3e8;
--surface-container-highest: #d9dde3; /* Stats card */
--surface-variant: #d9dde3;
```

### Text & Outline

```css
--on-surface: #2c2f32;            /* Primary text */
--on-surface-variant: #595c5f;    /* Secondary text */
--inverse-surface: #0b0f11;
--inverse-on-surface: #9a9da1;
--outline: #74777b;               /* Borders */
--outline-variant: #abadb1;       /* Light borders */
```

### Special Colors

```css
--error: #b31b25;
--error-dim: #9f0519;
--error-container: #fb5151;
--on-error: #ffefee;
--on-error-container: #570008;

--tertiary: #525d61;
--tertiary-dim: #465155;
--tertiary-container: #e7f3f7;
--on-tertiary: #e9f5f9;

--surface-tint: #006666;
```

### Gradient Effects

```css
.kinetic-gradient-text {
    background: linear-gradient(to right, #b61321, #006666);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.ghost-border {
    border: 1.5px solid rgba(0, 102, 102, 0.15);
}
```

---

## 📐 Typography System

### Font Families

```css
--font-headline: 'Lexend', sans-serif;
--font-body: 'Inter', sans-serif;
--font-label: 'Inter', sans-serif;
```

### Font Scales

```css
/* Hero Title */
text-6xl: 3.75rem / 60px (Desktop)
text-7xl: 4.5rem / 72px (Mobile large)
font-weight: 900 (font-black)
letter-spacing: -0.05em (tracking-tighter)
line-height: 1 (leading-none)

/* Logo/Brand */
text-2xl: 1.5rem / 24px
font-weight: 900 (font-black)
letter-spacing: -0.025em (tracking-tight)

/* Section Headings */
text-lg: 1.125rem / 18px
font-weight: 600 (font-semibold)
letter-spacing: -0.025em (tracking-snug)

/* Nav Items (Top Bar) */
text-sm: 0.875rem / 14px
font-weight: 500 (font-medium) or 700 (font-bold)
letter-spacing: -0.025em (tracking-tight)

/* Sidebar Nav */
text-xs: 0.75rem / 12px
font-weight: 700 (font-bold)
text-transform: uppercase
letter-spacing: 0.1em (tracking-widest)

/* Body Text */
text-xl: 1.25rem / 20px
font-weight: 300 (font-light)
letter-spacing: 0.025em (tracking-wide)

/* Caption/Label */
text-[10px]: 0.625rem / 10px
font-weight: 500 (font-medium) or 700 (font-bold)
text-transform: uppercase
letter-spacing: 0.1em (tracking-widest)

/* Button Text */
text-sm: 0.875rem / 14px
font-weight: 700 (font-bold)
```

---

## 📦 Component Library

### 1. Sidebar (Fixed Left Panel)

**Container:**

```html
<aside class="h-screen w-80 fixed left-0 top-0 overflow-y-auto 
              bg-surface-container-low flex flex-col p-6 space-y-8 z-20">
```

**Specifications:**

- Width: 320px (w-80 = 20 *4px = 80* 4px)
- Position: Fixed, left: 0, top: 0
- Height: 100vh (h-screen)
- Background: #eef1f5 (surface-container-low)
- Padding: 24px (p-6)
- Vertical spacing: 32px (space-y-8)
- Z-index: 20
- Overflow: Auto (vertical scrollbar if needed)

#### Logo Section

```html
<div class="flex items-center gap-3">
  <div class="w-10 h-10 rounded-lg bg-secondary flex items-center justify-center text-white">
    <span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">
      bolt
    </span>
  </div>
  <div>
    <h2 class="font-headline font-bold text-secondary text-sm tracking-widest uppercase">
      KINETIC ENGINE
    </h2>
    <p class="text-[10px] text-on-surface-variant font-medium tracking-tight">
      API Status: Online
    </p>
  </div>
</div>
```

**Icon Container:**

- Size: 40x40px (w-10 h-10)
- Border radius: 8px (rounded-lg)
- Background: #b61321 (secondary)
- Icon: Material Symbols "bolt", filled, white color

**Title:**

- Font: Lexend, bold, 14px (text-sm)
- Color: #b61321 (secondary)
- Transform: Uppercase
- Letter-spacing: 0.1em (tracking-widest)

**Status:**

- Font: Inter, medium, 10px
- Color: #595c5f (on-surface-variant)
- Letter-spacing: -0.025em (tracking-tight)

#### Primary CTA Button

```html
<button class="w-full bg-primary text-on-primary py-4 px-6 rounded-full 
               font-headline font-bold text-sm flex items-center justify-center gap-2 
               shadow-lg shadow-primary/20 active:scale-95 transition-transform">
  <span class="material-symbols-outlined text-sm">play_arrow</span>
  Sistemi Başlat
</button>
```

**Specifications:**

- Width: 100% (w-full)
- Padding: 16px vertical, 24px horizontal (py-4 px-6)
- Background: #006666 (primary)
- Text: #bbfffe (on-primary)
- Border radius: Full pill (rounded-full / 9999px)
- Font: Lexend, bold, 14px
- Shadow: Large shadow with 20% opacity primary color
- Active state: Scale 95%
- Transition: Transform property

#### Navigation Items

```html
<!-- Active State -->
<div class="bg-primary/10 text-primary rounded-lg font-bold px-4 py-3 
            flex items-center gap-3">
  <span class="material-symbols-outlined">speed</span>
  <span class="font-headline text-xs tracking-widest uppercase">Dashboard</span>
</div>

<!-- Inactive State -->
<div class="text-on-surface-variant hover:bg-surface-container transition-all 
            px-4 py-3 rounded-lg flex items-center gap-3 cursor-pointer">
  <span class="material-symbols-outlined">monitoring</span>
  <span class="font-headline text-xs tracking-widest uppercase">Analytics</span>
</div>
```

**Active State:**

- Background: rgba(0, 102, 102, 0.1) (primary with 10% opacity)
- Text color: #006666 (primary)
- Font weight: Bold

**Inactive State:**

- Text color: #595c5f (on-surface-variant)
- Hover background: #e5e8ed (surface-container)
- Transition: All properties

**Common:**

- Padding: 16px horizontal, 12px vertical (px-4 py-3)
- Border radius: 8px (rounded-lg)
- Icon + text gap: 12px (gap-3)
- Font: Lexend, 12px (text-xs), uppercase, tracking-widest
- Cursor: Pointer

#### Session Stats Card

```html
<div class="bg-surface-container-highest/50 p-4 rounded-xl space-y-4">
  <h3 class="font-headline text-[10px] font-bold text-on-surface-variant 
             uppercase tracking-widest">
    Session Stats
  </h3>
  <div class="grid grid-cols-2 gap-4">
    <div>
      <p class="text-[10px] text-on-surface-variant uppercase">Duration</p>
      <p class="font-headline font-bold text-primary">12:45</p>
    </div>
    <div>
      <p class="text-[10px] text-on-surface-variant uppercase">Queries</p>
      <p class="font-headline font-bold text-primary">24</p>
    </div>
  </div>
  <div class="flex items-center gap-2 text-[10px] font-bold text-primary">
    <span class="material-symbols-outlined text-[14px]" 
          style="font-variation-settings: 'FILL' 1;">
      check_circle
    </span>
    SYSTEM CALIBRATED
  </div>
</div>
```

**Card:**

- Background: rgba(217, 221, 227, 0.5) (surface-container-highest with 50% opacity)
- Padding: 16px (p-4)
- Border radius: 12px (rounded-xl)
- Vertical spacing: 16px (space-y-4)

**Heading:**

- Font: Lexend, bold, 10px
- Color: #595c5f (on-surface-variant)
- Transform: Uppercase
- Letter-spacing: 0.1em (tracking-widest)

**Grid:**

- Layout: 2 columns (grid-cols-2)
- Gap: 16px (gap-4)
- Label: 10px, uppercase, on-surface-variant
- Value: Lexend, bold, primary color

**Status Badge:**

- Font: 10px, bold
- Color: #006666 (primary)
- Icon: check_circle, filled, 14px

---

### 2. Top App Bar (Sticky Header)

```html
<header class="w-full top-0 sticky z-10 bg-white px-8 py-4 
               flex justify-between items-center shadow-sm">
  <!-- Left: Brand + Nav -->
  <div class="flex items-center gap-12">
    <span class="text-2xl font-black bg-gradient-to-r from-[#b61321] to-[#006666] 
                 bg-clip-text text-transparent font-headline tracking-tight">
      KINETIC AI
    </span>
    <nav class="hidden md:flex gap-8">
      <a class="text-primary font-bold border-b-2 border-primary 
                font-headline text-sm tracking-tight" href="#">
        Performance
      </a>
      <a class="text-on-surface-variant font-medium hover:text-secondary 
                transition-colors duration-200 font-headline text-sm tracking-tight" 
         href="#">
        History
      </a>
      <a class="text-on-surface-variant font-medium hover:text-secondary 
                transition-colors duration-200 font-headline text-sm tracking-tight" 
         href="#">
        Resources
      </a>
    </nav>
  </div>
  
  <!-- Right: Icons + Profile -->
  <div class="flex items-center gap-4">
    <span class="material-symbols-outlined text-on-surface-variant cursor-pointer 
                 hover:text-secondary transition-colors">
      notifications
    </span>
    <span class="material-symbols-outlined text-on-surface-variant cursor-pointer 
                 hover:text-secondary transition-colors">
      settings
    </span>
    <div class="w-8 h-8 rounded-full overflow-hidden bg-surface-container">
      <img alt="User profile" src="..." />
    </div>
  </div>
</header>
```

**Container:**

- Width: 100% (w-full)
- Position: Sticky, top: 0
- Z-index: 10
- Background: White
- Padding: 32px horizontal, 16px vertical (px-8 py-4)
- Layout: Flex, justify-between, items-center
- Shadow: Small shadow

**Logo:**

- Font: Lexend, font-black (900), 24px (text-2xl)
- Gradient: from #b61321 to #006666
- Style: bg-clip-text text-transparent
- Letter-spacing: -0.025em (tracking-tight)

**Navigation:**

- Hidden on mobile, flex on md and up (hidden md:flex)
- Gap: 32px (gap-8)

**Nav Item (Active):**

- Text color: #006666 (primary)
- Font weight: Bold
- Border-bottom: 2px solid primary

**Nav Item (Inactive):**

- Text color: #595c5f (on-surface-variant)
- Font weight: Medium
- Hover: #b61321 (secondary)
- Transition: color, 200ms

**Icons:**

- Color: #595c5f (on-surface-variant)
- Hover: #b61321 (secondary)
- Cursor: Pointer
- Gap: 16px (gap-4)

**Profile Avatar:**

- Size: 32x32px (w-8 h-8)
- Border radius: Full circle (rounded-full)
- Background: #e5e8ed (surface-container)

---

### 3. Hero Section (Centered)

```html
<section class="flex-grow flex flex-col items-center justify-center 
                px-12 pb-32 max-w-6xl mx-auto w-full">
  <div class="text-center space-y-4 mb-16">
    <h1 class="text-6xl md:text-7xl font-headline font-black 
               kinetic-gradient-text tracking-tighter leading-none">
      🏋️ RAG Personal Trainer
    </h1>
    <p class="text-xl text-on-surface-variant font-body font-light tracking-wide">
      Your AI-powered fitness assistant. Personalized knowledge, instantly.
    </p>
  </div>
  
  <!-- Bento Grid (Quick Actions) -->
  <div class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full">
    <!-- 6 cards here -->
  </div>
</section>
```

**Container:**

- Flex: flex-col, items-center, justify-center
- Padding: 48px horizontal, 128px bottom (px-12 pb-32)
- Max width: 1152px (max-w-6xl)
- Margin: Auto centered (mx-auto)
- Width: 100% (w-full)
- Flex-grow: Take available space

**Title Area:**

- Text align: Center
- Vertical spacing: 16px (space-y-4)
- Margin bottom: 64px (mb-16)

**H1 (Hero Title):**

- Font: Lexend, font-black (900)
- Size: 60px desktop (text-6xl), 72px tablet+ (md:text-7xl)
- Class: kinetic-gradient-text (gradient #b61321 → #006666)
- Letter-spacing: -0.05em (tracking-tighter)
- Line-height: 1 (leading-none)

**Subtitle:**

- Font: Inter, font-light (300)
- Size: 20px (text-xl)
- Color: #595c5f (on-surface-variant)
- Letter-spacing: 0.025em (tracking-wide)

**Bento Grid:**

- Layout: 1 column mobile, 3 columns md+ (grid-cols-1 md:grid-cols-3)
- Gap: 24px (gap-6)
- Width: 100% (w-full)
- Total: 6 cards in 2 rows

---

### 4. Quick Action Cards (Bento Grid)

```html
<button class="bg-surface-container-lowest p-8 rounded-xl ghost-border 
               text-left hover:shadow-xl hover:shadow-primary/5 transition-all 
               group flex flex-col justify-between h-48 active:scale-[0.98]">
  <span class="material-symbols-outlined text-primary group-hover:text-secondary 
               transition-colors mb-4">
    fitness_center
  </span>
  <span class="text-on-surface font-headline font-semibold text-lg leading-snug">
    Bench press nasıl yapılır?
  </span>
</button>
```

**Specifications:**

- Background: #ffffff (surface-container-lowest)
- Padding: 32px (p-8)
- Border radius: 12px (rounded-xl)
- Border: 1.5px solid rgba(0, 102, 102, 0.15) (ghost-border)
- Text align: Left
- Layout: Flex column, justify-between
- Height: 192px (h-48)
- Transition: All properties
- Group: For child hover effects

**Hover State:**

- Shadow: XL shadow with 5% opacity primary color
- Active scale: 0.98

**Icon:**

- Font: Material Symbols Outlined
- Color: #006666 (primary) → #b61321 (secondary) on group hover
- Margin bottom: 16px (mb-4)
- Size: Default 24px
- Transition: Colors

**Text:**

- Font: Lexend, semibold (600)
- Size: 18px (text-lg)
- Color: #2c2f32 (on-surface)
- Line-height: 1.375 (leading-snug)

**6 Cards:**

1. fitness_center - "Bench press nasıl yapılır?"
2. calendar_month - "3 günlük kuvvet programı öner"
3. nutrition - "Kilo almak için beslenme listesi"
4. timer - "HIIT antrenmanı kaç dakika olmalı?"
5. rebase_edit - "Deadlift form düzeltme ipuçları"
6. local_fire_department - "En iyi yağ yakıcı egzersizler"

---

### 5. Floating Input Bar (Fixed Bottom)

```html
<div class="fixed bottom-0 left-80 right-0 p-8 
            bg-gradient-to-t from-surface via-surface to-transparent">
  <div class="max-w-4xl mx-auto">
    <div class="bg-surface-container-lowest rounded-full p-2 pl-8 
                flex items-center shadow-2xl shadow-primary/10 
                border border-primary/10">
      <input class="bg-transparent border-none flex-grow focus:ring-0 
                    text-on-surface font-body py-4 placeholder:text-outline" 
             placeholder="Kendi sorunuzu yazın..." 
             type="text" />
      <button class="bg-primary text-on-primary h-14 px-10 rounded-full 
                     font-headline font-bold flex items-center gap-2 
                     hover:bg-primary-dim transition-colors active:scale-95">
        Sor
        <span class="material-symbols-outlined">send</span>
      </button>
    </div>
    <p class="text-center text-[10px] text-outline-variant mt-4 
              font-label uppercase tracking-widest">
      Kinetic AI can make mistakes. Check important information.
    </p>
  </div>
</div>
```

**Outer Container:**

- Position: Fixed, bottom: 0
- Left: 320px (left-80, accounting for sidebar)
- Right: 0
- Padding: 32px (p-8)
- Background: Gradient from #f4f6fa → transparent (top fade)

**Inner Container:**

- Max width: 896px (max-w-4xl)
- Margin: Auto centered

**Input Bar:**

- Background: White (surface-container-lowest)
- Border radius: Full pill (rounded-full)
- Padding: 8px with 32px left (p-2 pl-8)
- Layout: Flex, items-center
- Shadow: 2XL shadow with 10% opacity primary
- Border: 1px solid rgba(0, 102, 102, 0.1)

**Input Field:**

- Background: Transparent
- Border: None
- Flex: Grow to fill space
- Focus: No ring (focus:ring-0)
- Text color: #2c2f32 (on-surface)
- Font: Inter (body)
- Padding: 16px vertical (py-4)
- Placeholder: #74777b (outline)

**Submit Button:**

- Background: #006666 (primary)
- Text color: #bbfffe (on-primary)
- Height: 56px (h-14)
- Padding: 40px horizontal (px-10)
- Border radius: Full pill (rounded-full)
- Font: Lexend, bold
- Layout: Flex, items-center, gap-2
- Hover: #005959 (primary-dim)
- Active: Scale 95%
- Transition: Colors

**Disclaimer Text:**

- Text align: Center
- Font: Inter (label), 10px
- Color: #abadb1 (outline-variant)
- Margin top: 16px (mt-4)
- Transform: Uppercase
- Letter-spacing: 0.1em (tracking-widest)

---

### 6. Decorative Elements

```html
<!-- Blur circles for depth -->
<div class="absolute top-20 right-20 w-64 h-64 bg-primary/5 rounded-full blur-3xl -z-10"></div>
<div class="absolute bottom-40 left-20 w-96 h-96 bg-secondary/5 rounded-full blur-3xl -z-10"></div>
```

**Specifications:**

- Position: Absolute
- Z-index: -10 (behind content)
- Border radius: Full circle (rounded-full)
- Blur: 48px (blur-3xl)
- Opacity: 5% of primary/secondary colors

**Circle 1 (Top Right):**

- Top: 80px (top-20)
- Right: 80px (right-20)
- Size: 256x256px (w-64 h-64)
- Color: rgba(0, 102, 102, 0.05)

**Circle 2 (Bottom Left):**

- Bottom: 160px (bottom-40)
- Left: 80px (left-20)
- Size: 384x384px (w-96 h-96)
- Color: rgba(182, 19, 33, 0.05)

---

## 📱 Responsive Breakpoints

### Tailwind Breakpoints

```css
sm: 640px
md: 768px
lg: 1024px
xl: 1280px
2xl: 1536px
```

### Layout Adjustments

**Mobile (<768px):**

- Sidebar: Collapse to hamburger menu (hidden)
- Main content: Full width (ml-0 instead of ml-80)
- Top bar: Simplified (hide nav tabs, show only logo + hamburger)
- Hero title: text-6xl (60px)
- Bento grid: 1 column (grid-cols-1)
- Input bar: Left: 0 (full width)

**Tablet (768px-1024px):**

- Sidebar: Visible, w-64 (256px instead of 320px)
- Main content: ml-64
- Hero title: text-7xl (72px)
- Bento grid: 2 columns (md:grid-cols-2)

**Desktop (1024px+):**

- Sidebar: w-80 (320px)
- Main content: ml-80
- All nav tabs visible
- Bento grid: 3 columns (md:grid-cols-3)

---

## 🎬 Animations & Transitions

### Button Interactions

```css
/* Hover */
transition-colors duration-200

/* Active/Click */
active:scale-95
transition-transform

/* Group hover (card icon color change) */
group-hover:text-secondary
transition-colors
```

### Card Hover

```css
hover:shadow-xl
hover:shadow-primary/5
transition-all
```

### Input Focus

```css
focus:ring-0 /* Remove default ring */
focus:outline-none /* Custom focus state if needed */
```

### Material Icons

```css
font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;

/* Filled variant */
font-variation-settings: 'FILL' 1;
```

---

## ✅ Implementation Checklist

### Phase 1: Setup

- [ ] Install Tailwind CSS
- [ ] Add custom color palette to tailwind.config
- [ ] Import Lexend and Inter fonts from Google Fonts
- [ ] Import Material Symbols Outlined
- [ ] Add custom CSS for .kinetic-gradient-text and .ghost-border

### Phase 2: Structure

- [ ] Create fixed sidebar (320px, z-20)
- [ ] Create sticky top bar (z-10)
- [ ] Create main content area (ml-80)
- [ ] Add decorative blur circles (-z-10)

### Phase 3: Components

- [ ] Sidebar logo + API status
- [ ] Primary CTA button (Sistemi Başlat)
- [ ] Navigation items (4 items, active state)
- [ ] Session stats card
- [ ] Top bar logo (gradient text)
- [ ] Top bar nav tabs (3 items)
- [ ] Top bar icons + profile
- [ ] Hero title + subtitle
- [ ] Bento grid (6 quick action cards)
- [ ] Floating input bar (fixed bottom)

### Phase 4: Interactivity

- [ ] Hover states for all buttons
- [ ] Active states (scale-95)
- [ ] Group hover for card icons
- [ ] Transitions (colors, transform, shadow)
- [ ] Input focus states

### Phase 5: Responsive

- [ ] Mobile: Collapse sidebar, 1-column grid
- [ ] Tablet: 2-column grid
- [ ] Desktop: 3-column grid, full sidebar

### Phase 6: Polish

- [ ] Add Material Icons to all buttons/cards
- [ ] Verify color contrast (WCAG AA)
- [ ] Test all hover/active states
- [ ] Optimize shadows and blur effects
- [ ] Add smooth scroll behavior

---

## 🎯 Design Tokens (CSS Variables)

```css
:root {
  /* Colors */
  --color-primary: 0 102 102;
  --color-secondary: 182 19 33;
  --color-surface: 244 246 250;
  --color-on-surface: 44 47 50;
  
  /* Spacing */
  --space-xs: 0.25rem;  /* 4px */
  --space-sm: 0.5rem;   /* 8px */
  --space-md: 1rem;     /* 16px */
  --space-lg: 1.5rem;   /* 24px */
  --space-xl: 2rem;     /* 32px */
  --space-2xl: 3rem;    /* 48px */
  
  /* Border Radius */
  --radius-sm: 0.5rem;  /* 8px */
  --radius-md: 0.75rem; /* 12px */
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
  --shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
}
```

---

**Last Updated:** April 2026  
**Status:** ✅ Production Ready  
**Maintainer:** GitHub Copilot  
