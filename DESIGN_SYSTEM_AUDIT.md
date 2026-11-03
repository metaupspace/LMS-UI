# UpSpace Design System Audit: HTML Designs vs Figma Library

**Date:** 2026-10-29
**Design system source:** Figma file **"Component Library for UpSpace"** (`UiVBnW8QURRBLYALBJfrnD`), read live through the Desktop Bridge plugin.
**Designs audited:** all 96 HTML files in `designs/*/code/` and `designs/*/component/` (Admin 24, Instructor 27, Learner 16, Course Designer 10, Manager 9, Authentication 9, Other 1).

> **Source note:** You linked `UpSpace-Design-System` (`HAUo3VoNqJcl78thFa1P6E`), but the bridge was connected to `Component Library for UpSpace` (`UiVBnW8…`). Its 24 component pages match the local export in `Analyze-design-system/UpSpace Design System/components/` one for one, so this audit treats it as the same library. If `HAUo3V…` is a different or newer file, open the plugin in that file and re-run the audit.

---

## 1. Executive summary

| Area | Verdict | Key number |
|---|---|---|
| Font family | ✅ Aligned | 96/96 files use DM Sans. The only other fonts are monospace (code blocks) and Georgia (1 certificate). |
| Brand and semantic colors | 🟡 Mostly aligned | 226 off-palette hex uses (26 unique values). 115 of them are `#f0f0f0`. |
| Semantic token values | 🔴 Drift | `--border-subtle`, `--radius-md` and `--radius-sm` are redefined with non-DS values in 33–77 files. |
| Type scale | 🔴 Major drift | **66 %** of `font-size` declarations (1,966 / 2,969) are off the DS scale (13, 13.5, 12.5, 15 px …). |
| Spacing scale | 🟡 Drift | 32 % of padding, margin and gap values (3,177 / 9,925) are off the DS scale (10, 6, 14, 18 px …). |
| Radius scale | 🟡 Drift | 119 off-scale radii. 78 of them are `6px`, which the DS doesn't have. |
| Shadows / elevation | 🔴 Missing in DS | DS has **0 effect styles and 0 shadow tokens**. Designs use **74 unique `box-shadow` values** (426 declarations). |
| Buttons | 🟡 Spec drift | DS buttons are Medium 500 at 40 px. Designs use SemiBold 600, heights 32–48 px (38 px in 19 files), and variants the DS lacks. |
| Components | 🔴 Big gap | About 20 UI patterns used across the designs have no DS component (sidebar, top nav, card, tabs, checkbox, avatar, empty state …). |
| Dark mode | ✅ Consistent | Neither side has one. The DS color collection has one mode and no design file defines dark styles. |
| Traceability | 🔴 Weak | Only 9/96 files declare which DS components they use (`Library:` comment). |
| DS hygiene | 🔴 Issues | 5 component sets throw errors. 4,436 hard-coded fills in components. The Brand badge uses `#6941c6`, which isn't a DS token. |

---

## 2. Design-system baseline (what Figma defines)

| Category | Contents |
|---|---|
| Color variables | 325 in one mode ("Default"): the full Tailwind-style primitive palette (red → stone, 11 steps each), alpha light/dark, and a Semantic layer (text, surface, border, icon, action, link, focus, feedback ×4, brand, product 1–4). |
| Paint styles | 212, grouped as Base, Brand, Feedback, Neutrals UpSpace, Content and Secondary. ⚠ The local `colors/colors.json` has only 101, so the export is stale. |
| Text styles | 163, all DM Sans. Sizes are **9, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40, 48, 56, 64, 72**. Weights are Regular, Medium, SemiBold and Bold. |
| Radius | none 0 · sm 2 · md 4 · lg 8 · xl 12 · 2xl 16 · 3xl 24 · 4xl 32 · 5xl 48 · full 999 |
| Space | 0 · 1 · 2 · 4 · 8 · 12 · 16 · 20 · 24 · 28 · 32 · 40 · 48 · 60 · 72 |
| Effects | **None.** There are no effect styles or shadow variables. |
| Icons | Lucide and Hugeicons, 4,155 icon components on the Icons page. |
| Components | 73 sets/components across 24 groups: Alerts, Aside, Badges, Breadcrumbs, Buttons, Carousel, Charts, Dropdowns, File Dropper, Inputs, Messaging, Modals, Pagination, Popover, Progress Bar, Radio groups, Select, Sliders, Tables, Toast, Toggles, Tooltip, Video Player, plus Base (Feature, Pricing Header) and an empty Color Picker page. |

---

## 3. Token discrepancies (designs vs DS)

### 3.1 Semantic token values redefined incorrectly

Most design files declare their own `:root` variables that mirror the DS semantic names. The values below don't match Figma:

| Variable in HTML | HTML value | DS value | Files |
|---|---|---|---|
| `--border-subtle` | `#f0f0f0` | `#f5f5f5` (Semantic/border/subtle) | **77** |
| `--radius-md` | `6px` | `4px` (Radius/md) | **51** |
| `--radius-sm` | `4px` | `2px` (Radius/sm) | **33** |
| `--text-tertiary` | `#737373` | `#a3a3a3` | 1 (`instructor/code/assessment-editor.html`) |
| `--surface-raised` | `#ffffff` | `#f5f5f5` | 1 (same file) |
| `--surface-overlay` | `#f5f5f5` | `#e5e5e5` | 1 (same file) |
| `--border-strong` | `#d4d4d4` | `#a3a3a3` | 1 (same file) |

These variables also appear in the designs but don't exist in the DS: `--text-strong` (#404040, which the DS names Semantic/**icon**/primary), `--action-primary-subtle` and `--action-primary-soft` (the DS equivalents are `brand/subtle` and `brand/border`).

Files whose `:root` matches the DS exactly: `Authentication/code/dashboard.html`, `instructor/code/question-bank.html`, and all four `component/topnavbar.html`.

### 3.2 Off-palette colors (hex values not in any DS variable or style)

| Hex | Uses | Where | Likely intent / nearest DS token |
|---|---|---|---|
| `#f0f0f0` | 115 | ~77 files, through `--border-subtle` | Use `#f5f5f5` (border/subtle) or `#e5e5e5` (border/default). Note that `#f0f0f0` also appears 360× as a hard-coded fill *inside* DS components, so the library is inconsistent too. |
| `#f3f3f3`, `#e9e9e9` | 27 | Learner dashboard/revision-notes, Course Designer builder/preview/dashboard/my-courses | Neutral 100/200 (`#f5f5f5` / `#e5e5e5`) |
| `#e0e0e0` | 8 | Manager approvals/assessments/team-performance, Instructor AI generator/concept-mastery/learner-reports-list | `#e5e5e5` |
| `#7c5b06` | 18 | Profile pages (Learner, Manager, Admin), Admin certificates-overview/community-moderation/roles | Amber 800 is `#92400e`, yellow 800 is `#854d0e`. Pick one. |
| `#d9c58e` `#947b34` `#fffdf8` `#e8dcb8` `#f8f1dd` `#bfae7a` | 24 | Certificate files (Learner certificates/certificate-detail, Admin certificate-templates/certificates-overview) | Certificate "paper/gold" palette that doesn't exist in the DS. Either add a `certificate/*` token set or map to amber/stone. |
| `#7f56d9` `#f9f5ff` | 10 | Instructor grade-submission, grading-overview, session-attendance, submission-list | Untitled UI purple, which isn't in the DS. Use `brand/default` and `brand/subtle`, or `product/1`. |
| `#0b0b12` `#0f1117` `#171a22` `#2a2a33` | 9 | Video surfaces: Learner course-player/live-session-detail, CD course-preview | Use neutral 950 `#0a0a0a`. The DS video player uses `#0a0a0a`. |
| `#5b46e5` `#3b35be` | 2 | `Authentication/code/onboarding-org-details.html` | Near-brand. Use `#4f46e5` and `#3730a3`. |
| `#a5d6a7` `#f9c97a` | 2 | `course-designer/code/course-builder.html` | Material colors. Use green 300 / amber 300. |
| `#111111` `#333333` `#0f0f0f` `#fafaff` `#fffbfa` | 7 | scattered | Neutral equivalents |

### 3.3 Typography

- Font family ✅: DM Sans everywhere. The DS doesn't define a monospace font, but the designs use one in 10 places (code blocks, IDs). Add a `Family/mono` token if you want it in the system.
- **Font size 🔴**: 66 % of declarations are off-scale.

| Off-scale size | Uses | Nearest DS size |
|---|---|---|
| 13px | 496 | 12 or 14 |
| 13.5px | 487 | 14 |
| 12.5px | 383 | 12 |
| 15px | 153 | 14 or 16 |
| 14.5px | 97 | 14 |
| 11.5px / 11px | 167 | 12 (or 10, Caption-1) |
| 17px | 42 | 16 or 18 |
| 26px | 32 | 24 or 28 |
| 22px | 22 | 20 or 24 |
| 5px / 2px | 31 | Probably glyph-hiding tricks. Review them. |
| others (10.5, 15.5, 19, 21, 23, 30, 34, 38, 44, 74 …) | ~60 | n/a |

- Weight: buttons use **600 (SemiBold)**, but DS buttons use **Medium (500)**. This affects 46 files.

### 3.4 Spacing, radius and elevation

- **Spacing**: the most common off-scale values are `10px` (842), `6px` (765), `14px` (524), `18px` (250), `22px` (141), `3px` (117), `9px` (99) and `5px` (89). The DS scale jumps 4 → 8 → 12 → 16 → 20 → 24, so 6, 10, 14 and 18 are all half-steps that need a DS decision. Either add them to the scale or snap the designs to it.
- **Radius**: `6px` (78), `3px` (17), `5px` (5), `1px` (4), `20px` (3), plus one-offs (13, 18, 22, 70, 80, 99, 120, 160). The DS has no 6 px step, but it's the designs' most-used small radius.
- **Shadows 🔴**: the DS defines **no** elevation tokens. The designs invent 74 different shadows, for example:
  - `0 0 0 3px rgba(99,102,241,.15)`: focus ring (50 uses)
  - `0 12px 32px -8px rgba(23,23,23,.18)`: popover/menu (39)
  - `4px 0 24px rgba(0,0,0,.12)`: mobile sidebar (42, written two ways)
  - `0 1px 3px rgba(23,23,17,.1)`: card (18)
  - `0 24px 64px -12px rgba(23,23,23,.28)`: modal (18)

  Some DS components (Alert, Tooltip and 30 other nodes) do carry drop shadows, but they're raw effects rather than styles, so the designs can't reference them.

---

## 4. Component discrepancies: in the designs but NOT in the DS

Counts are the number of HTML files where the pattern appears. Items already logged in `MISSING_COMPONENTS.md` are marked 📋.

| UI pattern | Files | DS status |
|---|---|---|
| Top navigation bar | 85 | ❌ Missing. Each role has its own `component/topnavbar.html`. |
| Sidebar navigation | 79 | ❌ Missing. Each role has its own `component/sidebar.html`. |
| Card (generic container, course card) | 79 | ❌ Missing |
| KPI / stat tile | 54 | ❌ Missing |
| Native `<select>` | 55 | ⚠ The DS has a custom **Select** (5 types). The designs mostly use the browser's native select, so they look different. |
| Avatar (standalone) | 47 | ❌ Missing. It only exists as a badge icon option or a dropdown-header avatar group. |
| Search field | 43 | ⚠ Partial. Select has a "Search" type and Input has a leading icon, but there's no dedicated search component. |
| Empty state | 35 | ❌ Missing 📋 |
| Tabs (underline and segmented) | 31 | ❌ Missing 📋 |
| Checkbox (standalone, indeterminate) | 22 | ❌ Missing as its own component. It only exists inside Radio-group item (Type=Checkbox) and Table header cell. 📋 |
| Filter chip / tag input | 15 | ❌ Missing 📋 (tag input) |
| Skeleton loader | 11 | ❌ Missing 📋 |
| Stepper / wizard | 10 | ❌ Missing 📋 (still unchecked in the log) |
| Date/time input, calendar | 6 + | ❌ Missing. Native inputs are used. 📋 Calendar and date tile |
| Accordion | 4 | ❌ Missing 📋 |
| Timeline / approval pipeline | 2 | ❌ Missing 📋 |
| Rich text editor | 2 | ❌ Missing 📋 |
| Histogram / time-series area chart | 2 + | ⚠ The DS has line, bar, pie, radar, gauge and progress circle charts, but no histogram or animated area chart 📋 |
| OAuth / "Continue with" buttons (`btn-oauth`) | 2 | ⚠ The DS **has** Social button and Social button group. The sign-in and sign-up pages hand-build theirs instead. |
| Button variants `ghost`, `warning`, `success`, `danger-outline`, `xs` | many | ⚠ The DS hierarchy is Primary, Secondary color/gray, Tertiary color/gray, Link color/gray (+ Destructive set) in sizes sm/md/lg/xl. There's no warning or success button and no xs size. `ghost` corresponds to Tertiary gray. |
| Course-builder blocks (content block frame, picker, audio, embed, code, callout …) | 1–2 | ❌ Missing 📋 (approved HTML-only builds) |
| Certificate document, flashcard, QR scanner, transcript panel, AI bar | 1–3 each | ❌ Missing 📋 (approved HTML-only builds) |

### Component-level spec mismatches (pattern exists in both)

| Component | DS spec | Designs | Gap |
|---|---|---|---|
| Button (md) | h 40, r 8, **Medium 14** | h 40 (22 files), **38 (19)**, 36 (5), 44 (3); weight **600**; font 13.5 px in 17 files | Height and weight drift |
| Badge (md) | h 24, 14 px text | h 24, **12.5 px / 12 px**, weight 600, pill radius | Font size and weight |
| Input field | 14 px, label + field 80 h block | h 36/40/42/64, 13–14 px, r `--radius-lg` | Height inconsistent across files |
| Toggle (md) | 44×24, r 12, on = `#4f46e5` | 21 files hand-roll switches | Check sizes against the DS |
| Toast | 540 w, r 8, pad 17/24/17/20, fill `#f5f5f5` | 33 files, custom | Not traced to the DS spec |
| Modal / Aside | DS Modal (84 variants, set errors), Aside L/R/Bottom | 37 modal files, 8 drawer files | Matches conceptually, sizes are custom (820/600 px) |

---

## 5. In the DS but NOT used in any design

| DS component | Evidence |
|---|---|
| Mobile app store badge | No usage |
| Carousel image, Pagination dot group, Carousel arrow | No usage (no carousel anywhere) |
| Radar chart, Activity gauge, Pie chart | No usage. The designs build their own SVG charts. |
| Line and bar chart (DS set) | Not referenced. All 10 chart files hand-build SVG. |
| Messaging: emoji, reactions | Only `Message` (sent) is referenced, in `Learner/code/coach.html` |
| Social button / Social button group | Not used. Auth pages use custom `btn-oauth`. |
| Slider | `type="range"` appears in 4 files (video/audio scrubbing), not the DS Slider |
| Color Picker page | Empty page with no component, and no usage |
| Base: Feature, Pricing Header | No usage. Billing pages build their own plan cards. |
| Mega input field, Payment input type | No usage |
| Verification code input | ✅ Used (`Authentication/code/verify-email.html`) |
| Pagination (page/card types) | Used in 9 files, but hand-built |

---

## 6. Design-system (Figma) health issues

These affect how faithfully any design can follow the system:

1. **5 component sets are in an error state** ("Component set has existing errors"): `Alerts`, `Buttons/Button`, `Modal`, `Table cell` and `Table`. Their variant properties can't be read, which probably means duplicate or conflicting variant names.
2. **Duplicate button sets.** `Buttons/Button` (errored) and `Buttons/Button destructive` both have 528 variants and identical structure.
3. **4,436 hard-coded colors** inside components (no variable or style). The worst pages are File Dropper (1,159), Modals (1,163), Inputs (588), Badges (485), Radio groups (307), Buttons (224) and Tables (187). Brand logos and flags explain some of them. Others don't, for example `#f0f0f0` (360), `#dadada` (276), `#181d27` (189) and `#172b85` (408).
4. **The Brand badge uses `#6941c6`** (Untitled UI purple) instead of the DS brand indigo. That's probably why `#7f56d9` and `#f9f5ff` show up in the instructor grading screens.
5. **No elevation tokens**, but 32 component nodes use raw drop shadows.
6. **Two empty "Token Audit" pages** with the same name.
7. **Typo in names:** the "Popver" page and the "Propover" component (should be Popover), and the "_Activitiy gauge" component (should be Activity).
8. **A Mobile typography group exists, but the Size collection is the only one with a Mobile mode.** Text tokens use separate `Mobile/*` names instead of modes.
9. **The local export is stale.** `colors/colors.json` has 101 colors, but Figma now has 212 paint styles.

---

## 7. Per-role scorecard

| Role | Files | Off-palette hex | Off-scale font sizes | Off-scale radius | Off-scale spacing (of total) | Shadows | `:root` token mismatches | Files with `Library:` note |
|---|---|---|---|---|---|---|---|---|
| Admin | 24 | 41 | 694 | 76 | 1,184 / 2,945 | 155 | 41 | 0 |
| Instructor | 27 | 62 | 426 | 15 | 564 / 1,426 | 47 | 51 | 0 |
| Learner | 16 | 55 | 302 | 6 | 560 / 1,292 | 75 | 23 | 8 |
| Course Designer | 10 | 39 | 302 | 14 | 590 / 1,363 | 73 | 21 | 1 |
| Manager | 9 | 19 | 197 | 0 | 172 / 603 | 48 | 20 | 0 |
| Authentication | 9 | 10 | 37 | 8 | 99 / 263 | 27 | 8 | 0 |
| Other | 1 | 0 | 8 | 0 | 8 / 33 | 1 | 1 | 0 |

**Files with the most drift** (weighted: hex×3 + font sizes + radius×2 + token mismatches×5):
1. `course-designer/code/course-builder.html`: 11 off hex, 87 font sizes, 182 spacing, 26 shadows
2. `admin/code/learner-reports.html`: 56 font sizes, 12 radius
3. `course-designer/code/course-preview.html`
4. `course-designer/code/question-bank.html`
5. `instructor/code/assessment-editor.html`: 7 semantic token values overridden
6. `admin/code/certificates-overview.html`
7. `admin/code/billing-overview-2.html`
8. `Manager/code/approvals.html`
9. `admin/code/user-management.html`
10. `admin/code/certificate-templates.html`

---

## 8. Recommendations (priority order)

**Fix in the designs (cheap, high impact)**
1. Set `--border-subtle:#f5f5f5`, `--radius-md:4px` and `--radius-sm:2px` in every `:root`, or decide the DS should change (see 9 below). One find-and-replace covers about 160 mismatches.
2. Snap font sizes to the DS scale. Most of the 66 % drift is just 12.5, 13, 13.5 and 15 px.
3. Replace `#7f56d9`/`#f9f5ff`, `#e0e0e0`, `#f3f3f3`/`#e9e9e9`, near-black video colors and the onboarding near-brand colors with DS tokens.
4. Set button weight to 500 and height to 40 px (md), or 36 px for sm.
5. Use the DS Social button on sign-in and sign-up, and the DS Select where a styled select is wanted.
6. Add a `Library:` header comment to the 87 files that don't have one, so they're traceable.

**Fix in Figma (DS owner)**
7. Repair the 5 errored component sets and remove the duplicate `Buttons/Button`.
8. Add **elevation tokens** (xs, sm, md, lg, xl, focus-ring) based on the 5–6 shadows the designs actually use.
9. Decide on the de-facto values in the designs: a 6 px radius, 6, 10 and 14 px spacing, and `#f0f0f0`. Either add them to the DS or reject them.
10. Promote the most-reused hand-built patterns into the library: **Sidebar nav, Top nav, Card, KPI tile, Avatar, Tabs, Checkbox, Empty state, Skeleton, Stepper, Date picker, Chip/Tag**.
11. Bind the 4,436 raw fills to variables, starting with the Badge Brand color `#6941c6`.
12. Re-export `Analyze-design-system/` so the local copy matches Figma (212 paint styles).

---

## 8b. Component conformance: do the "library" components actually match the library? (2026-10-30)

Every page in `designs/*/code/` (88) was rendered at 1440 px, and the **computed** styles of each component equivalent were compared with the styled layer of the matching Figma variant (Default state, md unless noted). "Match" means every visible instance in that file is within ±1 px and has the exact color, weight and radius.

| Component (DS variant) | Files match / use | Main deviations (DS → designs) |
|---|---|---|
| Button Primary md (40h, px16, r8, 14/500, `#4f46e5`) | **40 / 59** | 46/44/38 px heights in 12 files; px 6 or 24 in 8 (icon or wide buttons) |
| Button Primary sm (36h, px14) | 3 / 4 | 34h, px12 |
| Button Secondary gray md (40h, border **`#d4d4d4`**, text **`#404040`**) | **11 / 49** | Border `#e5e5e5` in **46 files**. Text `#525252` (13) or `#171717` (4). 28 px height in 5 files (12 px text). |
| Button Secondary gray sm (36h) | 2 / 12 | 34/32h, px12, 12 px text, border `#e5e5e5` |
| Button Tertiary gray (`ghost`) | 2 / 5 | Red/indigo text (used as destructive or link) |
| Button Destructive primary | 14 / 16 | 1 inverted (white bg, red text) |
| Button lg (44h, px18, 16 px) | 1 / 2 | 48h, px22 |
| **Badge** (sm 20 / md 24h, px 8–10, **weight 500**) | **0 / 30** | Weight **600** (46) or 700 (14). **18 px height** in 16 files. Several have zero padding (fixed-width pill). |
| **Input field** (44h, px14, **16 px Regular**, border `#d4d4d4`, bg white) | **8 / 51** | **36 px height** in 33 files, 14 px text (53), border `#e5e5e5` (54), bg `#fafafa` (25), px12 (43) |
| **Select** (custom menu, 44h, r8, 16 px) | **8 / 55** | **Native `<select>` in 32 files**, r4 (22), 12–14 px text, heights 24–42 |
| Textarea (r8, px14, 16 px, `#d4d4d4`) | 8 / 19 | Border `#e5e5e5`, 14 px text, 3 borderless (inline editors) |
| Checkbox (`_Checkbox base` 16×16, r4, `#d4d4d4`) | 9 / 18 | **Native browser checkbox** in 9 files (no radius or border, OS styling) |
| Radio | 3 / 4 | 1 native |
| Toggle md (44×24, r12) | 1 / 5 | Radius computed as 0 on 4. The track is a child element, so check this by eye. |
| **Table header cell** (44h, px24, 12/500, `#525252`, bg `#fafafa`) | **2 / 35** | 39–41h, **px20** (35 files), weight **600** (37), bg `#f5f5f5` (28) |
| **Table cell** (72h, px24, 14 px) | **2 / 35** | 52–69h (denser rows), **px20** (82 instances) |
| Dropdown / popover menu (r8, white, `#e5e5e5`) | **5 / 5** ✅ | n/a |
| Pagination number (40×40, r8, 14/500) | 0 / 3 | 32–34 px, r4, 12 px, weight 600 |
| Progress bar (8h, r4, track `#f5f5f5`) | 0 / 2 | 4–6 px, pill radius. Other files use class names the selector didn't catch. |
| **Toast** (r8, 16/500) | **0 / 27** | 14 px text (27), weight 600 (20) |
| **Breadcrumbs** (14/500, link `#525252`) | **0 / 24** | Weight **600**, link color **`#a3a3a3`** in all 24 |
| Breadcrumb current (14/500) | 0 / 28 | Weight 700 or 600. Color `#171717` vs DS `#000000`, and the DS is the one that's wrong here. |
| Alert (r8, p16) | **4 / 4** ✅ | n/a |

**Takeaways**

1. **Systematic and cheap to fix (CSS-only, barely visible):** use border `#d4d4d4` on secondary buttons, inputs, selects and textareas instead of `#e5e5e5`, and weight 500 on badges, table headers, breadcrumbs, toasts and pagination instead of 600/700. Also: secondary-button text `#404040`, select radius 8, breadcrumb links `#525252`, and table-header bg `#fafafa`.
2. **Density choices that change the UI if fixed:** inputs and selects are 36 px tall instead of 44 with 14 px text instead of 16, and table rows are 52–69 px tall instead of 72 with 20 px padding instead of 24. The designs are consistently denser than the library. This needs a decision: either adopt the DS sizes, or add a "compact" size to the DS (the input already has sm/md/lg in the Mega input set).
3. **Not the library component at all:** native `<select>` in 32 files and native checkboxes in 9 files. These need the DS Select and `_Checkbox base`.
4. **More library bugs found during the spec pull:** the input **focus border is `#d6bbfb`** (an Untitled UI purple, not `focus/ring #6366f1`), the tooltip bg is `#818cf8`, the Brand badge is `#6941c6` on `#f9f5ff`, and the active breadcrumb is raw `#000000` instead of `text/primary`.

Limits: matching uses class names (`.btn-*`, `.badge`, `.pill`, `table th/td`, `.toast`, `.breadcrumb`). Components with other class names (e.g. some progress bars, custom chips) weren't measured. Only Default states were compared. Hover, focus and disabled were not.

---

## 8c. Cross-UI inconsistencies: the same thing done differently across roles and pages (2026-10-30)

How this was checked: all 88 pages were rendered at 1440 px, including the sidebar and topbar frames. Elements were grouped **by what renders** (geometry and computed styles), not by class name, because each role names things differently (Admin uses `card`, Learner and Course Designer use `panel`, Manager uses `panel-card`, Instructor uses `widget`). A visual contact sheet of each role's dashboard and main list page was also reviewed.

### Shell and navigation

| # | Inconsistency | Where | Suggested standard |
|---|---|---|---|
| X1 | **Active sidebar item uses the *info* tokens** (blue `#2563eb` on `#eff6ff`) in all 5 roles. Every other selected state (tabs, pagination, toggles, focus) uses brand indigo `#4f46e5`. | all `component/sidebar.html` + admin inline sidebars | `brand/subtle` bg + `action/primary` text |
| X2 | Sidebar width **240 px on the 4 profile pages**, 232 px everywhere else (72 pages) | `{Learner,Manager,admin,instructor}/code/profile.html` | 232 |
| X3 | Topbar contents differ by role. Manager shows **name + role text** next to the avatar and has **no search**. Course Designer has no search and no breadcrumbs (breadcrumbs removed on request). Learner's search says "Search courses"; Instructor and Admin say "Search". | `*/component/topnavbar.html` | One topbar pattern, or document why it varies by role |
| X4 | Breadcrumb root: Manager uses **"Workspace /"**, while the other roles use the role name ("Admin /", "Instructor /", "Learner /") | Manager topnav | Pick one convention |
| X5 | **No Log out in the Manager sidebar.** Learner, Instructor and Course Designer have one at the bottom, and Admin has two links. | `Manager/component/sidebar.html` | Add it |
| X6 | Topbar avatar is 34 px solid indigo with initials for Manager, and a 36 px photo for the other roles | topnavs | 36 px, same treatment |
| X7 | Topbar height 64 px on course-player, course-preview and the Auth pages, 80 px everywhere else. This looks deliberate (focus mode and pre-login). | n/a | OK. Record it as intentional in DECISIONS.md. |

### Page header and layout

| # | Inconsistency | Detail |
|---|---|---|
| X8 | **Page title (H1) has 18 variants**: 24 / 28 / 31.68 / 32 / 40 px, letter-spacing from -0.3 to -0.6 | List pages: 28 px (Learner, Admin, Manager, Course Designer) but **32 px** on Instructor lists (`learners-list`, `assessments-overview`, `grading-overview`, `live-sessions-overview`). Detail pages: **24 px** on Instructor and Manager details and all profiles, but **31.68 px** on Admin details (`user-detail`, `role-detail`, `integration-detail`, `organization-import`), so Admin detail titles are *bigger* than Admin list titles. |
| X9 | Subtitle under the H1 is 14 px in Admin and Manager, 16 px in Learner and Course Designer, mixed in Instructor. Gap below the title is 4–10 px. | n/a |
| X10 | Content padding: 32 px (Learner, Manager, Instructor), **37.44 px fluid** (Admin), 24/32 (5 Instructor pages), 36 px plus a **1180 px max-width** only on `instructor/dashboard` and `assessment-editor`. The H1 x-position varies (264 vs 269 px). | n/a |
| X11 | Dashboard greeting: Admin uses title case with a trailing comma ("Good **M**orning Alex,"), Instructor writes "Good morning, Professor Vance", Learner and Course Designer use time-of-day greetings, and **Manager has no greeting** ("Team learning overview"). | the 5 `dashboard.html` files |
| X12 | 12 pages have **no H1** (focus or editor pages: `course-builder`, `assessment-editor`, `workflow-create/detail`, `assignment-detail`, `live-session-detail` …). That's fine for layout but a gap for accessibility and consistency. | n/a |

### Content components

| # | Inconsistency | Detail |
|---|---|---|
| X13 | **52 card container variants.** Radius is consistent (12 px), but padding varies: 22/24 (most common), 20, 24/32, 16/20, 16/18, 18/20, 20/22, 12/14. **Manager** cards add a `0 1px 2px` shadow and a 16 px radius, which other roles mostly don't. | Pick 2 sizes (e.g. 24 standard, 16 compact) |
| X14 | Section headings: H2 is 16, 18 or 20 px with three different letter-spacings. **H3 is used for two different jobs**: as a section title (16–18 px, `#171717`) in Admin and Manager, and as a muted overline (12–14 px, `#a3a3a3`) in Instructor and Learner. | Define an H2/H3/overline scale |
| X15 | KPI value is 28/700 in most places, but letter-spacing is -0.4 (Admin, Instructor) vs -0.5 (Manager). It's **32 px** on Manager `assessments` and `team-performance`, and 24 px on Instructor `learner-detail`. The KPI tile layout also differs per role (icon placement, delta pill). | Promote a KPI tile component |
| X16 | Tabs come in 4 styles: segmented (34 px, white-on-gray) in Admin, Learner and Course Designer; indigo text with no indicator (30 px) in `instructor/grading-overview`; indigo 2 px underline in `instructor/reports-home`; and **13.33 px browser-default buttons** in `admin/certificates-overview`, where the tab buttons don't inherit the font, which is a bug. | One Tabs component (already 📋 in MISSING_COMPONENTS) |
| X17 | Initials avatars use 4 color schemes (indigo-50, indigo-100, violet, yellow) and 5 sizes (32/34/36/40/72) | Avatar component: sizes 24/32/40/72, one tint |
| X18 | Search fields are 36 px with a gray `#fafafa` bg on 62 pages, 42 px white on 13 (Learner, Admin, Course Designer), 36 px white in Instructor, and 38/40 elsewhere | One search field |
| X19 | Chips: 44 px with radius 12 in onboarding, 24 px pills in Admin moderation, and an unstyled variant in `ai-question-generator` | Chip component |
| X20 | Secondary-button heights: 28 / 32 / 34 / 36 / 38 / 40 / 44 px across pages (see §8b) | sm 36 / md 40 |

**Quick wins** (CSS-only, no visual redesign): X1, X2, X5, X6, X16 (font inherit), X4, and the X11 copy. **Needs a decision:** X3, X8–X10, X13–X15 (these define the page and type scale), and X17–X19 (best solved by adding the missing components to the library).

---

## 9. Fixes applied (2026-10-29)

Applied to 95 of the 96 files. Only CSS was changed (`<style>` blocks and `style=""` attributes):

| Fix | Changes |
|---|---|
| `:root` `--radius-md` 6→4px, `--radius-sm` 4→2px | 51 + 33 |
| Off-palette hex → DS color (e.g. `#f0f0f0`→`#f5f5f5`, `#7f56d9`→`#7c3aed` product/2, `#7c5b06`→`#854d0e`) | 198 |
| Font sizes snapped to the DS scale (12.5→12, 13/13.5→14, 15→16, 11/11.5→12 …) | 1,964 |
| Off-scale radii snapped (6→4, 3→4, 1→2, 99→999 …) | 110 |
| `.btn` weight 600→500, height 38→40px | 78 rules |
| `admin/code/dashboard.html` region-name column widened 104→112px (the 14px text caused a new ellipsis) | 1 |

Checks: all 96 pages rendered at 1440px and 390px. Horizontal scroll was 0 before and 0 after. Four new ellipsis truncations remain, and all of them are designed truncations (two mobile breadcrumbs and two KPI labels).

**Not changed on purpose** (these would visibly change the UI or need a DS decision first): spacing (6/10/14/18px sit exactly between DS steps), shadows (the DS has no tokens), the certificate gold palette, the `assessment-editor.html` semantic overrides (DS values would turn its cards gray and its tertiary text would fail contrast), component swaps (native select → DS Select, OAuth → Social button), and the Figma-side issues in §6.

### Pass 2 (2026-10-30): component conformance and cross-UI quick wins

| Fix | Scope |
|---|---|
| Control borders `#e5e5e5` → DS `#d4d4d4` (secondary buttons, inputs, selects, textareas, filter/search inputs) | rule-level; only rules where *every* selector is a control |
| Secondary-button text → `#404040` | n/a |
| Weight 600/700 → 500 on badges/pills, table headers (incl. `font:` shorthand), breadcrumbs, toasts, pagination | n/a |
| Breadcrumb links `#a3a3a3` → `#525252` (also better contrast); table-header bg `#f5f5f5` → `#fafafa`; select radius → 8 | n/a |
| Native checkboxes and radios → DS `_Checkbox base` look (16 px, r4, `#d4d4d4`; checked = indigo-50 + indigo check). Zero-specificity `:where()`, so existing rules still win. | 10 files |
| X1 active sidebar item → brand indigo (`#eef2ff` / `#4f46e5`) | all roles (CSS vars + 1 literal in `organization-import`) |
| X2 profile pages' shell column 240 → 232 px | 4 profile pages |
| X4 Manager breadcrumb root "Workspace" → "Manager"; X5 Logout added to the Manager sidebar (same markup as Learner); X6 Manager topbar avatar 34 → 36 px | Manager components |
| X8 page titles: Instructor list pages 32 → 28 px, Admin `certificates-overview` 32 → 28, `organization-import` → 28, Admin details (`user`, `role`, `integration`) clamp(28–32) → 24 px, which matches the other roles' detail pages | 9 files |
| X11 "Good Morning Alex," → "Good morning, Alex" | admin dashboard |

Result: secondary buttons now match on 32/49 pages (was 11), badges 13/30 (was 0), checkboxes 14/18 (was 9), radios 4/4, breadcrumb links 23/24 (was 0). Sidebar is 232 px on all 76 app pages, and no active nav item is blue anymore. Overflow: 0 horizontal scroll and no new clipped text. **What still fails is density** (input 36 vs 44 px, 14 vs 16 px text, table rows and padding, toast 14 px), which is waiting on the decision in §8b-2. The DS's own `#000000` breadcrumb bug also still shows as a mismatch.

Not done (needs a decision or a library component): density (§8b-2), native `<select>` menus, card padding (X13), H2/H3 roles (X14), KPI tile (X15), Tabs/Avatar/Search/Chip (X16–X19), topbar pattern per role (X3), a Manager greeting (no documented copy, so none was invented), subtitle size and content padding (X9, X10). X16's `certificates-overview` "tab font" turned out to be a false positive: the children set their own fonts.

### Pass 3 (2026-10-30): custom dropdowns and DS charts

**Dropdowns: 55 pages, 178 `<select>`s.** An inline "DS Select menu" block (built to the library's Select / `_Select menu` / `_Select menu item`) enhances every native single select:
- It shows a DS listbox (white, `#e5e5e5` border, r8, 16/Medium items, `#fafafa` hover, indigo check) and adds a search field for lists with more than 10 options.
- It supports full keyboard use (arrows, Home/End, Enter, Esc, type-ahead) and sets the ARIA attributes.
- Selects that still had the OS look get the DS chevron. Already-styled ones are left alone.
- The `<select>` stays the source of truth, firing real `input` and `change` events, so page filters and form values work unchanged.
- Touch devices keep the native picker.
- Tested: 99 visible selects across 55 pages open, filter and fire `change`. No JS errors and no layout regressions.

**Charts: 13 pages, 12 visible on load plus ones behind views.** An inline "DS Charts" renderer (`UpChart.line / bar / donut / progress`) implements the library's chart specs:
- 1 px `#f5f5f5` grid, 12 px `#525252` axes, 2 px lines with an area gradient, the indigo series palette, legend dots, tooltips, responsive redraw, reduced-motion support, and a screen-reader data table.
- The hand-drawn SVG/CSS charts it replaces are listed in the table below.

| Page | Chart | Spec |
|---|---|---|
| admin/dashboard | User growth: line | RPT-001-FR-02 |
| admin/learner-reports | Engagement trend: bar (follows range and learner) | RPT-002-FR-02 |
| admin/course-performance-reports | **New:** lesson drop-off bar, top 3 highlighted (in course detail view) | RPT-003-FR-04 |
| admin/concept-mastery-gap-analysis | Mastery donut + **new** stacked mastery-per-concept bar (follows filters) | RPT-004-FR-04 |
| admin/certificate-templates | Issued / revoked / expired: line | n/a (conversion) |
| Manager/dashboard, team-performance, assessments | Trend lines with target and metric/range toggles | n/a (conversion) |
| Manager/assessment-detail | Score distribution: bar (follows assessment select) | n/a (conversion) |
| instructor/learner-report | Weekly engagement: bar, inactive weeks in red (follows `?id=`) | RPT-002-FR-02 |
| instructor/concept-mastery | **New:** stacked mastery distribution per concept | RPT-004-FR-04 |
| instructor/concept-detail | **New:** before/after retake accuracy (only concepts with retake data) | RPT-004-FR-07 |
| course-designer/dashboard | Pipeline by stage + courses started: bar (stage filter kept) | n/a (conversion) |

Not added, on purpose:
- A pass/fail donut (RPT-002-FR-03): no page has the counts.
- An individual accuracy-over-time line (RPT-004-FR-03): no page has an individual time series.
- Charts for RPT-005: the spec asks for a table.

Derived mock data:
- The `learner-report` LNR-004 weekly series.
- The per-learner mastery levels on `instructor/concept-mastery`, copied from `concept-detail`'s learner data.

Open issues the agents found (not caused by this pass):
- The Instructor and Manager pages have no mobile layout (the 232 px grid stays at 390 px), so charts are cramped there. `learner-report`'s chart collapses at 390 px.
- `learner-report` shows "Avg 5.3 hrs / week" for LNR-004, which doesn't match her total.
- The old Manager tooltips' extra lines ("N learners active") were dropped.

### Pass 4 (2026-10-30): typography scale

Text was classified **by its role in the layout** (computed in the browser, since class names differ per role) and each element's *own* CSS rule was edited. Rules shared across roles that would need different values, and inherited or inline styles, were skipped unless they were checked by hand.

| Role | Standard | Share on the standard, before → after |
|---|---|---|
| Card / section title | 16 / 700 (hero titles ≥ 20 px kept as their own tier) | 34% → 83% |
| Card subtitle | 14 / 400 | 65% → 94% |
| List-row title | 14 / 600 (tile titles 16 / 600) | 61% → 80% (+16/600 tiles) |
| Row meta | 12 / 400 under 14 px titles, 14 / 400 under 16 px tiles | 39% → 73% (+14 px tiles) |
| KPI value / label | 28 / 700 · 14 / 600 | 71% → 100% |
| Page subtitle | 14 / 400 | 61% → 88% |
| Form controls | text 14 px; select values 500 | inputs 52/56 at 14/400; all product selects 14/500 |

- Hand-fixed: Manager dashboard "Quick Actions" and "Important Updates" were inline 14 px while sibling cards were 16 px. Also fixed: the instructor "Mastery distribution" title, `.q-title` rows on Manager assessment-detail, and the section headings on admin integration-detail and export-custom-reports.
- Dropdown menu text now follows its trigger's size (minimum 14 px) instead of the DS's fixed 16 px.
- Auto-width selects resize to fit their longest option in the loaded web font, so "All Direct Reports (24)" and "Last 7 days" no longer truncate.

Left as they are:
- The design-only "Preview / state" switchers (12 px).
- Values the classifier mistook for titles ("84%", card numbers).
- The 24 px hero titles.
- One `export-custom-reports` select that truncates inside its fixed-width grid cell. This was already the case before.

Checks: no JS errors on 88 pages, 0 horizontal scroll, no new clipped text, all charts render, and 95/99 visible dropdowns pass. The other 4 are the known `learner-report` reload artifact.

---

## 10. Method and limits

- **Figma:** read live through the bridge: variables (618 total), paint styles (212), text styles (163), component sets with variant properties, sample variant geometry (button, input, badge, toast, toggle, tooltip, alert, table header), and unbound-fill counts.
- **HTML:** static scan of `<style>` blocks and inline `style=""` attributes (base64 payloads stripped). Component detection uses class names and markup heuristics, so counts mean "file contains the pattern", not instance counts. Spot-check before acting on a single file.
- **Not verified:** whether the 1,426 inline SVG icons come from Lucide or Hugeicons. Only 2 files name an icon library. Path-level icon matching wasn't done.
- **Not covered:** hover/focus states, responsive breakpoints, accessibility, and visual (pixel) comparison.
