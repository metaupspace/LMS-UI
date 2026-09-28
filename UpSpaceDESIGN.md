---
version: alpha
name: UpSpace-design-system
description: A neutral, systematic admin/LMS interface built on a cool off-white canvas, a single indigo action color, and a DM Sans type scale running Title/Heading/Label/Body/Caption. Unlike the marketing-site systems this doc is modeled on, every value here is extracted directly from the live Figma variable/style graph, not screenshots — colors and type are traceable primitive → semantic → style chains, verified for WCAG contrast, not estimated.

colors:
  text-primary: "#171717"
  text-secondary: "#525252"
  text-tertiary: "#a3a3a3"
  text-disabled: "#d4d4d4"
  text-inverse: "#ffffff"
  surface-canvas: "#fafafa"
  surface-raised: "#f5f5f5"
  surface-overlay: "#e5e5e5"
  surface-modal: "#d4d4d4"
  border-default: "#e5e5e5"
  border-subtle: "#f5f5f5"
  border-strong: "#a3a3a3"
  icon-primary: "#404040"
  icon-muted: "#a3a3a3"
  icon-disabled: "#d4d4d4"
  action-primary: "#4f46e5"
  action-primary-hover: "#4338ca"
  action-primary-pressed: "#3730a3"
  action-primary-disabled: "#d4d4d4"
  link: "#4f46e5"
  link-hover: "#4338ca"
  focus-ring: "#6366f1"
  error: "#dc2626"
  error-subtle: "#fef2f2"
  error-border: "#fecaca"
  warning: "#ca8a04"
  warning-subtle: "#fefce8"
  warning-border: "#fef08a"
  success: "#15803d"
  success-subtle: "#f0fdf4"
  success-border: "#bbf7d0"
  info: "#2563eb"
  info-subtle: "#eff6ff"
  info-border: "#bfdbfe"
  brand: "#4f46e5"
  brand-subtle: "#eef2ff"
  brand-border: "#c7d2fe"
  brand-on-default: "#ffffff"
  product-1: "#9333ea"
  product-1-subtle: "#faf5ff"
  product-1-border: "#e9d5ff"
  product-1-on-default: "#ffffff"
  product-2: "#7c3aed"
  product-2-subtle: "#f5f3ff"
  product-2-border: "#ddd6fe"
  product-2-on-default: "#ffffff"
  product-3: "#2563eb"
  product-3-subtle: "#eff6ff"
  product-3-border: "#bfdbfe"
  product-3-on-default: "#ffffff"
  product-4: "#0284c7"
  product-4-subtle: "#f0f9ff"
  product-4-border: "#bae6fd"
  product-4-on-default: "#ffffff"

typography:
  title-1:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    lineHeight: 88px
    letterSpacing: -0.8px
  title-2:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    lineHeight: 76px
    letterSpacing: -0.8px
  title-3:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    lineHeight: 68px
    letterSpacing: -0.6px
  heading-h1:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    lineHeight: 68px
    letterSpacing: -0.5px
  heading-h2:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    lineHeight: 58px
    letterSpacing: -0.4px
  heading-h3:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    lineHeight: 48px
    letterSpacing: -0.3px
  heading-h4:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    lineHeight: 38px
    letterSpacing: -0.2px
  heading-h5:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    lineHeight: 30px
    letterSpacing: -0.15px
  heading-h6:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    lineHeight: 24px
    letterSpacing: 0
  label-1:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    lineHeight: 22px
    letterSpacing: -0.18px
  label-2:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    lineHeight: 20px
    letterSpacing: -0.16px
  label-3:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    lineHeight: 16px
    letterSpacing: -0.12px
  body-1:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    lineHeight: 28px
    letterSpacing: 0
  body-2:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    lineHeight: 24px
    letterSpacing: 0
  body-3:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    lineHeight: 20px
    letterSpacing: 0
  body-4:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    lineHeight: 16px
    letterSpacing: 0
  caption-1:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 10px
    lineHeight: 12px
    letterSpacing: 0
  caption-2:
    fontFamily: "DM Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 9px
    lineHeight: 10px
    letterSpacing: 0

rounded:
  none: 0px
  sm: 2px
  md: 4px
  lg: 8px
  xl: 12px
  2xl: 16px
  3xl: 24px
  4xl: 32px
  5xl: 48px
  full: 999px

spacing:
  zero: 0px
  px: 1px
  2xs: 2px
  4xs: 4px
  xs: 8px
  sm: 12px
  base: 16px
  md: 20px
  lg: 24px
  xl: 28px
  2xl: 32px
  3xl: 40px
  4xl: 48px
  5xl: 60px
  6xl: 72px

components:
  button-md:
    height: 40px
    padding: 10px 16px
    rounded: "{rounded.lg}"
    itemSpacing: "{spacing.xs}"
  button-sm:
    height: 36px
    padding: 8px 14px
    rounded: "{rounded.lg}"
    itemSpacing: "{spacing.xs}"
  button-lg:
    height: 44px
    padding: 10px 18px
    rounded: "{rounded.lg}"
    itemSpacing: "{spacing.xs}"
  button-xl:
    height: 48px
    padding: 12px 20px
    rounded: "{rounded.lg}"
    itemSpacing: "{spacing.xs}"
  button-icon-only-md:
    size: 40px
    padding: 10px
    rounded: "{rounded.lg}"
---

## Overview

This is a Figma-native component library for **UpSpace**, an LMS/admin platform — 24 component categories (Alerts, Buttons, Toast, Inputs, Badges, Dropdowns, Video Player, Modals, Popover, Aside, Charts, Select, Tables, Breadcrumbs, Pagination, Carousel, Progress Bar, Radio groups, Sliders, Toggles, Messaging, File Dropper, Tooltip, Color Picker), built around one type family (**DM Sans**) and one deliberately narrow color system: a neutral gray scale, a single indigo action color, and four feedback families (error/warning/success/info).

Unlike a marketing-site design system reconstructed from screenshots, every value in this document comes from the file's actual Figma Variables graph — a real **primitive → semantic → style** chain, built and verified this session:

1. **Primitives** — raw scale values (`Color System/Primitive/*`, `Typography/Scale/*` and `Typography/Tracking/*`). Never applied directly to a layer.
2. **Semantic** — role-based tokens that alias primitives (`Color System/Semantic/*`, `Typography` collection's per-level groups). Bound directly to fills and text properties — this is what a designer actually picks.
3. **Component** — created only when a specific component's design genuinely diverges from a semantic role. None exist yet in the color system; typography's equivalent is the Text Style layer (semantic × weight).

There is no dark mode yet — the color collection is structurally ready for one (Figma supports a different alias target per mode), but values haven't been chosen, and adding a mode now would touch all 267 color primitives for zero current benefit. Build it after the light system has been used in production, not before.

**Key characteristics:**
- Canvas is `#fafafa`, not pure white — a deliberate choice to reduce eye fatigue on large surfaces, made mid-session after review.
- One action color (`#4f46e5`, indigo) — no secondary brand hue. `link` aliases `action/primary` rather than duplicating it, so both move together.
- Four feedback families, each with the same four-role shape: `default` (icon/accent), `subtle` (background tint), `border`, `on-default` (text/icon color when placed directly on `default`). `warning` and `success` needed a specific step chosen (not the obvious one) to actually pass WCAG AA — see Colors below.
- Typography is 18 semantic size levels (Title ×3, Heading ×6, Label ×3, Body ×4, Caption ×2) × up to 5 weights each — DM Sans only, no second family.
- Two known, real gaps found while building this system (not invented): no dark "inverted surface" token for Tooltip, and no distinct token for Admin Sidebar background if it ever needs to diverge from `surface/canvas`.

## Colors

### Text
- **Primary** (`{colors.text-primary}` — #171717): Default reading/heading text. ~17.9:1 on canvas — AAA.
- **Secondary** (`{colors.text-secondary}` — #525252): Supporting text. ~7.8:1 on canvas.
- **Tertiary** (`{colors.text-tertiary}` — #a3a3a3): Metadata, timestamps, low-emphasis labels. No stated contrast requirement — used only for non-essential text.
- **Disabled** (`{colors.text-disabled}` — #d4d4d4): Disabled control labels. WCAG exempts disabled content from contrast requirements.
- **Inverse** (`{colors.text-inverse}` — #ffffff): Text on `action/primary` and any dark/colored surface.

### Surface
- **Canvas** (`{colors.surface-canvas}` — #fafafa): Page background. Intentionally not pure white.
- **Raised** (`{colors.surface-raised}` — #f5f5f5): Cards, panels, table headers — content sitting one step above canvas.
- **Overlay** (`{colors.surface-overlay}` — #e5e5e5): Dropdowns, popovers, select menus — floating content above raised surfaces.
- **Modal** (`{colors.surface-modal}` — #d4d4d4): The strongest surface tier, reserved for modal dialogs.

### Border
- **Default** (`{colors.border-default}` — #e5e5e5), **Subtle** (`{colors.border-subtle}` — #f5f5f5), **Strong** (`{colors.border-strong}` — #a3a3a3): Standard dividers, low-emphasis borders, and high-emphasis borders respectively.

### Icon
- **Primary** (`{colors.icon-primary}` — #404040), **Muted** (`{colors.icon-muted}` — #a3a3a3), **Disabled** (`{colors.icon-disabled}` — #d4d4d4).

### Action & Interactive
- **Primary** (`{colors.action-primary}` — #4f46e5): The only action color in the system. `on-color` is `text-inverse` at ~6.3:1 — passes AA. (The lighter step, indigo/500, was tested and rejected — it fails AA by a hair at 4.47:1.)
- **Hover** (`{colors.action-primary-hover}` — #4338ca), **Pressed** (`{colors.action-primary-pressed}` — #3730a3), **Disabled** (`{colors.action-primary-disabled}` — #d4d4d4, shared with the other disabled tokens).
- **Link / Link Hover** (`{colors.link}` / `{colors.link-hover}`): Same values as `action-primary`/`-hover`, but referenced as a separate token because it's applied to text-color, not fills — kept as an *alias* of action-primary rather than an independent reference, so the two can never silently drift apart.
- **Focus Ring** (`{colors.focus-ring}` — #6366f1): Non-text UI element, only needs 3:1 — passes at 4.47:1.

### Feedback
Each family — **Error**, **Warning**, **Success**, **Info** — follows the same four-role shape:

| Family | default | subtle | border | on-default | on-default contrast |
|---|---|---|---|---|---|
| Error | `#dc2626` | `#fef2f2` | `#fecaca` | white | 4.83:1 |
| Warning | `#ca8a04` | `#fefce8` | `#fef08a` | **dark** (`#171717`) | 6.1:1 |
| Success | `#15803d` | `#f0fdf4` | `#bbf7d0` | white | 5.02:1 |
| Info | `#2563eb` | `#eff6ff` | `#bfdbfe` | white | 5.17:1 |

Warning is the one family whose `on-default` is dark text, not white — white on `warning/default` (yellow-600) fails WCAG AA at 2.94:1, even for large text. Success also needed a specific step: the obvious `green-600` fails white-text contrast at 3.30:1, so `success/default` uses `green-700` instead.

## Typography

### Font Family
Single family: **DM Sans**. Fallback stack `ui-sans-serif, system-ui, sans-serif`. Four real weights (Regular 400, Medium 500, SemiBold 600, Bold 700). "Extra Bold" text styles exist in the file but currently render on the same face as Bold — DM Sans has no true ExtraBold face loaded, so those styles are visually identical to Bold today. Don't treat them as a distinct weight until a real ExtraBold face is added.

### Hierarchy

| Token | Size | Line-height | Letter-spacing | Use |
|---|---|---|---|---|
| `{typography.title-1}` | 72px | 88px | -0.8px | Largest display text |
| `{typography.title-2}` | 64px | 76px | -0.8px | Secondary display text |
| `{typography.title-3}` | 56px | 68px | -0.6px | Tertiary display — same size as `heading-h1`; no documented rule for which to pick, treat as an open question |
| `{typography.heading-h1}`…`{typography.heading-h6}` | 56→20px | 68→24px | -0.5px→0 | Product UI section hierarchy — the most-used scale |
| `{typography.label-1}`…`{typography.label-3}` | 16/14/12px | 22/20/16px | -0.18 to -0.12px | UI chrome — buttons, form labels, tabs. Negative tracking distinguishes Label from same-size Body |
| `{typography.body-1}`…`{typography.body-4}` | 18/16/14/12px | 28/24/20/16px | 0 | Reading content |
| `{typography.caption-1}`, `{typography.caption-2}` | 10/9px | 12/10px | 0 | Metadata, fine print |

Every level above is available at 3–5 weights as a Text Style (`{level}/{weight}` — e.g. `Heading/H1/Bold`) — that's what's actually applied to text layers. The `typography:` block above holds the numeric primitives only.

A **Mobile** variant tree exists for 7 of the 18 levels (Heading H1–H6, Body-1) with independently-tuned values — the other 11 mobile levels intentionally reuse the desktop numbers. One open finding: Mobile heading tracking runs proportionally *tighter* than desktop's as size decreases (Mobile H1 at 36px: -5% of size vs. desktop H1 at 56px: -0.89%) — backwards from normal practice, where smaller text usually wants looser tracking. Not corrected yet — needs a design call, not a mechanical fix.

## Layout

### Spacing Scale
Base unit 4px, but the named steps aren't a clean geometric progression — `{spacing.4xs}` (4px) sits between `{spacing.2xs}` (2px) and `{spacing.xs}` (8px), and the naming itself has an inconsistency worth flagging: the source scale names one 4px step `xs2` (not `2xs`) and one 32px step `xl2` (not `2xl`) — asymmetric with how `2xl`/`3xl` etc. are named everywhere else in this system (Radius, for instance, uses clean `2xl`/`3xl`/`4xl`). Documented here as a real naming inconsistency, not fixed — renaming would touch every existing binding.

Full scale: `{spacing.zero}` 0 · `{spacing.px}` 1 · `{spacing.2xs}` 2 · `{spacing.4xs}` 4 · `{spacing.xs}` 8 · `{spacing.sm}` 12 · `{spacing.base}` 16 · `{spacing.md}` 20 · `{spacing.lg}` 24 · `{spacing.xl}` 28 · `{spacing.2xl}` 32 · `{spacing.3xl}` 40 · `{spacing.4xl}` 48 · `{spacing.5xl}` 60 · `{spacing.6xl}` 72.

### Size Scale
A separate, smaller scale (11 steps, 0–48px) exists specifically for component/icon sizing, and — unlike every other collection in this system — it's the one place already demonstrating a **Default/Mobile mode split**: steps above 16px shrink on Mobile (e.g. `5xl`: 48px Default → 36px Mobile). This is the reference pattern for how any future responsive or dark-mode variation should be structured — per-mode values inside one collection, not a parallel collection.

## Shapes

### Border Radius Scale
`{rounded.none}` 0 · `{rounded.sm}` 2px · `{rounded.md}` 4px · `{rounded.lg}` 8px · `{rounded.xl}` 12px · `{rounded.2xl}` 16px · `{rounded.3xl}` 24px · `{rounded.4xl}` 32px · `{rounded.5xl}` 48px · `{rounded.full}` 999px.

Buttons use `{rounded.lg}` (8px) at every size — confirmed by direct inspection, not inferred.

## Components

**Confirmed by direct inspection (Buttons page, 1,230 component variants):**

| Size | Height | Padding | Radius | Icon gap |
|---|---|---|---|---|
| `{component.button-sm}` | 36px | 8px 14px | `{rounded.lg}` | `{spacing.xs}` |
| `{component.button-md}` | 40px | 10px 16px | `{rounded.lg}` | `{spacing.xs}` |
| `{component.button-lg}` | 44px | 10px 18px | `{rounded.lg}` | `{spacing.xs}` |
| `{component.button-xl}` | 48px | 12px 20px | `{rounded.lg}` | `{spacing.xs}` |
| `{component.button-icon-only-md}` | 40×40px | 10px | `{rounded.lg}` | — |

**Known but not spec-extracted** (listed as page names for inventory purposes, not verified against real instances — see Known Gaps): Alerts, Toast, Inputs, Badges, Dropdowns, Video Player, Modals, Popover, Aside, Charts, Select, Tables, Breadcrumbs, Pagination, Carousel, Progress Bar, Radio groups, Sliders, Toggles, Messaging, File Dropper, Tooltip, Color Picker.

### Color Usage by Purpose
A separate "Color Usage Guide" page in the Figma file (and the underlying reasoning) maps each semantic color token to which component/purpose it belongs to — Page & Surfaces, Text, Icons, Buttons, Links & Focus, Alerts/Toast/Badges (per feedback state), Inputs, Modals/Popover/Select/Dropdown, Tooltip, Tables, Sidebar/Aside, and form controls. Refer to that page rather than duplicating the full mapping here.

## Do's and Don'ts

### Do
- Bind semantic color variables directly to fills — no Paint Style wrapper needed for primitive or semantic tokens; Figma supports direct variable binding.
- Use `action-primary` for every primary interactive surface; use `link` (which aliases it) specifically for inline text-color contexts.
- Use `warning`'s dark `on-default`, not white — white-on-warning fails contrast.
- Reuse a semantic token across multiple components when the value is genuinely the same (e.g. Admin Sidebar background = `surface-canvas`) — don't invent a new token just because the *name* of the place using it is different.
- Escalate to a component-level token — as a Figma **Style**, never a Variable — only when a component's design actually diverges from what semantic already provides.

### Don't
- Don't add component tokens speculatively. None exist in the color system today, and that's correct until a real divergence shows up.
- Don't treat "Extra Bold" text styles as a distinct weight — they render identically to Bold until a real ExtraBold face exists.
- Don't assume Title-3 and Heading-H1 are interchangeable just because they're both 56px — they carry different tracking and no documented usage rule distinguishes them yet.
- Don't add a Dark mode to the Color System collection speculatively — it mechanically works (per-mode aliasing) but should wait until the light system is proven in real use.

## Known Gaps

- **Per-component specs beyond Buttons** are not extracted. The 23 other component categories (Alerts, Inputs, Tables, Modals, etc.) are known by name and page location but their padding/sizing/state treatment hasn't been inspected against real instances — do that before writing detailed specs for them, don't infer from the button pattern.
- **`feedback/info` colors are new this session** and not yet applied to any real component — the hex values are computed and contrast-verified, but no Alert/Toast/Badge instance uses them yet.
- **`surface/selected`** (for selected table rows, list items, menu items) was identified as a likely-needed token but deliberately not created — no confirmed component need yet.
- **Tooltip's dark "inverted surface"** has no token — a real gap found while writing the color usage guide, not a speculative addition.
- **Admin Sidebar** — open question on whether its background should stay aliased to `surface-canvas` or become its own component token if it needs to diverge visually.
- **Mobile heading tracking** (see Typography) needs a design decision, not a mechanical fix — flagged, not resolved.
- **Spacing scale naming** (`xs2`, `xl2` instead of `2xs`, `2xl`) is inconsistent with the rest of the system's naming convention (Radius uses clean `2xl`/`3xl`) — documented, not renamed, since it would touch every existing spacing binding.
- **Dark mode** has no chosen values anywhere in this system — colors, or otherwise. Structural readiness only.
