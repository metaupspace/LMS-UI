# Learner UI Component Reference

> Phase 1 of the UI-consistency refactor. A reverse-engineered record of the Learner UI **as it is built today** in `designs/Learner/`. It is not a design system, a redesign, or a proposal, and it doesn't replace `UpSpaceDESIGN.md`. Where the Learner build differs from `UpSpaceDESIGN.md`, this document records what the Learner build does.
>
> Generated 2026-09-28 from a full read of all 13 Learner screens and the 2 shared Learner components. Nothing was modified.

---

## 1. Purpose

This is the benchmark reference for the Learner experience. In the next phase it will be used to inspect the Admin, Instructor and Course Designer UIs and write findings like "Admin does X; Learner already has the benchmark for this pattern (see C27)".

It is written so that a developer or an AI agent can rebuild any Learner pattern without reading the source again. Every value below comes from the actual CSS/JS. Line references point to the defining rules.

**How to read it**
- **Component IDs** (`C01`…`C107`) are stable handles for Phase 2 mapping.
- **Layout patterns** are `P1`…`P8`, **interaction patterns** are `I01`…`I24`, and **workflows** are `W01`…`W14`.
- Each component has a **Class** (A–E, defined in §30):
  - **A:** Design System component
  - **B:** Learner-specific
  - **C:** Extended DS component
  - **D:** Shared application component
  - **E:** Learner page pattern
- "Library" means the UpSpace component library (`Analyze-design-system/UpSpace Design System/components/`). When a Learner file's header comment says "Library: X", that is recorded as the file's own claim. Individual variant values were **not** cross-checked against each group's `components.json` (see §31).

---

## 2. Scope

**Inspected (read in full):**

| # | File | Screen / flow | Sidebar key |
|---|---|---|---|
| 1 | `designs/Learner/code/dashboard.html` | Learner Dashboard | `dashboard` |
| 2 | `designs/Learner/code/my-courses.html` | My Courses | `courses` |
| 3 | `designs/Learner/code/course-overview.html` | Course Overview (+ Ask AI, Flashcards dialog, Revision-notes rows) | `courses` |
| 4 | `designs/Learner/code/course-player.html` | Course Player (+ Transcript, AI Tutor) | — (no sidebar) |
| 5 | `designs/Learner/code/assignments.html` | Assignments list (sidebar label "Assessments") | `assessments` |
| 6 | `designs/Learner/code/assignment-detail.html` | Assignment detail / submission / results | `assessments` |
| 7 | `designs/Learner/code/live-sessions.html` | Live Sessions (List + Calendar) | `live-sessions` |
| 8 | `designs/Learner/code/live-session-detail.html` | Live Session detail (join, check-in, recording) | `live-sessions` |
| 9 | `designs/Learner/code/certificates.html` | Certificates list | `certificates` |
| 10 | `designs/Learner/code/certificate-detail.html` | Certificate detail | `certificates` |
| 11 | `designs/Learner/code/coach.html` | Your Coach (AI Learning Coach) | `coach` |
| 12 | `designs/Learner/code/revision-notes.html` | AI Revision Notes (per module) | `courses` |
| 13 | `designs/Learner/code/flashcard-study.html` | Flashcard study session (per course) | `courses` |
| S1 | `designs/Learner/component/sidebar.html` | Shared Learner sidebar (iframe include) | — |
| S2 | `designs/Learner/component/topnavbar.html` | Shared Learner top bar (iframe include) | — |

**Requested areas that don't exist in the Learner build** (recorded, not invented):
- **Assessments (quiz/exam taking).** There is no assessment list, detail, instructions, question UI, answer controls, submission or results screen. The sidebar item **"Assessments"** links to `assignments.html` (file header: "Reached from the learner sidebar 'Assessments' item (user decision: reuse that item, no new nav entry)"). Quizzes appear only as a **lesson type** (`quiz`) in the course outline and player. In the player a non-video lesson shows a placeholder: "Quiz lesson — content renders here in the build." (`course-player.html:604-607`).
- **AI Learning landing page.** Doesn't exist. `MISSING_COMPONENTS.md` records "AI tool entry card — dropped, the AI Learning home page was removed." The AI entry points are listed in §20.
- **Dashboard "Recent activity", "My progress" panel, AI tiles.** Removed in dashboard v5 (file header, `dashboard.html:12-28`).
- **Notifications panel, global search results, profile/settings/preferences pages.** Only the triggers exist (§5). None has behavior or a target page.
- **Pagination.** No Learner screen paginates.
- **Grading states on quizzes, assessment feedback.** Only assignment grading exists (§17).

**Out of scope:** Admin, Instructor, Course Designer, Manager, Authentication. They were read only where a Learner file explicitly reuses their pattern (noted inline). `designs/other-pages/code/verify-certificate.html` is linked from the Learner certificate detail but was not inspected.

---

## 3. Source References

| Source | Used for |
|---|---|
| `designs/Learner/code/*.html` (13 files) | All component, layout, interaction and workflow facts |
| `designs/Learner/component/sidebar.html`, `topnavbar.html` | Global shell |
| `UpSpaceDESIGN.md` | Comparison baseline (§28) — not modified |
| `MISSING_COMPONENTS.md` | Which Learner components were hand-built with approval, and why |
| `Analyze-design-system/UpSpace Design System/components/` (folder listing only) | Which library groups exist: Alerts, Aside, Badges, Base, Breadcrumbs, Buttons, Carousel, Charts, Dropdowns, File Dropper, Inputs, Messaging, Modals, Pagination, Popver [sic], Progress Bar, Radio groups, Select, Sliders, Tables, Toast, Toggles, ToolTip, Video Player |

**Implementation model (important for Phase 2):** every Learner screen is a standalone HTML file (CLAUDE.md Rule 7). Each file has its own `:root` tokens and its own copy of every component's CSS. There is no shared stylesheet. "Where used" therefore means "re-implemented in each of these files". Copies are near-identical but **not always byte-identical** (for example button heights and `--border-subtle` vary per file; see §8 and §28). Only the sidebar and top bar are real shared components, included at runtime through `<iframe>`.

**Mock conventions present in every data-driven page** (not product UI):
- Fixed mock "now": `2026-09-23` (14:00 on most pages).
- `localStorage` persistence for drafts, chat history, joins and study content.
- Keys: `upspace-asg-<id>`, `upspace-player-<course>`, `upspace-tutor-<course>`, `upspace-course-ai-<course>`, `upspace-ai-bar-off`, `upspace-lsn-<id>`, `upspace-study-v2` (shared by overview / revision-notes / flashcards / coach).
- `?state=` demo query params, plus a dashed bottom-left **"Preview" state switcher** on some pages (see C107).

---

## 4. Learner Application Architecture

### 4.1 Page map and navigation graph

```
Sidebar (every page except Course Player)
├── Dashboard ─────────────── dashboard.html
│     ├─ Continue lesson ───────────────▶ course-player.html?id=
│     ├─ Course overview link / Keep-going cards ▶ course-overview.html?id=
│     ├─ Coming-up rows ─────────────────▶ assignment-detail.html?id= | live-session-detail.html?id=
│     └─ "All work" ▶ assignments.html · "All courses" ▶ my-courses.html · first-time "Ask Your Coach" ▶ coach.html
├── My Courses ────────────── my-courses.html
│     ├─ Continue hero (in-progress) ▶ course-player.html?id=   (not-started fallback ▶ course-overview)
│     ├─ Due-soon rows / every course card ▶ course-overview.html?id=
│     └─ course-overview.html
│           ├─ Start / Continue / Review ▶ course-player.html?id=
│           ├─ View certificate ▶ certificates.html
│           ├─ Revision notes row ▶ revision-notes.html?course=&mod=  (&print=1 = Download PDF)
│           ├─ Flashcards button ▶ in-page dialog ▶ flashcard-study.html?course=
│           └─ Prerequisite links ▶ course-overview.html?id=<prereq>
├── Assessments ───────────── assignments.html ▶ assignment-detail.html?id=a1…a8
├── Live Sessions ─────────── live-sessions.html ▶ live-session-detail.html?id=  (&join=1 | &checkin=1 | &watch=1 | #materials)
├── Certificates ──────────── certificates.html ▶ certificate-detail.html?id=c1…c12 ▶ ../../other-pages/code/verify-certificate.html?code=
├── Your Coach ────────────── coach.html (links out to course-player / course-overview#flashcards / revision-notes)
└── (bottom) Settings "#" · Logout ▶ ../../Authentication/code/sign-in.html
```

- **Course Player** has no sidebar or top bar. It is a focused layout with its own header ("← My Courses" back link + breadcrumb to the overview).
- **Deep-link hashes and params:** `course-overview.html#flashcards` opens the Flashcards dialog. `live-session-detail.html?join=1` auto-joins, `?checkin=1` opens the QR scanner, `?watch=1` opens the recording and `#materials` scrolls to materials. `revision-notes.html?print=1` triggers print→PDF.

### 4.2 Page skeleton shared by 12 of 13 screens

```html
<div class="shell">
  <div class="sidebar-backdrop" onclick="…remove('sidebar-collapsed')"></div>
  <iframe class="sidebar-frame" src="../component/sidebar.html?active=KEY"></iframe>
  <iframe class="topbar-frame"  src="../component/topnavbar.html?current=Page+Name[&parent=…&parentHref=…]"></iframe>
  <main class="main"><div class="main-inner"> …page… </div></main>
</div>
<!-- page-level overlays: toast, modal, sheet, preview switcher -->
<script> window.addEventListener('message', e => e.data==='toggle-sidebar' && shell.classList.toggle('sidebar-collapsed')); …</script>
```

- Communication between the top bar and the page uses `window.parent.postMessage('toggle-sidebar','*')`.
- `revision-notes.html` and `flashcard-study.html` set the top-bar `src` at runtime to add a parent crumb. `certificate-detail.html` also rewrites it after load (`certificate-detail.html:253-254`).
- `coach.html` has no `.main-inner`. It uses a centered `.stage` instead (P6).

### 4.3 Rendering model
- Most pages render from an in-file JS data array into an `#root`/`#content` container with string templates.
- Every data-driven page follows the same load sequence: **skeleton → (450–500 ms) → content | empty | error**. The standard is "skeleton in place, never a full-page spinner" (comments in `assignments.html`, `assignment-detail.html`, `live-sessions.html`, `certificates.html`).
- User-entered HTML (assignment rich text) is sanitized through an allow-list `clean()` (`assignment-detail.html:389-403`). All other dynamic text is escaped with `esc()`.

### 4.4 Status derivation (single-source functions duplicated per page pair)
| Domain | Function | States | Files |
|---|---|---|---|
| Course | data field `status` | `not-started`, `in-progress`, `completed` (+ derived `overdue` when deadline passed and not completed) | my-courses, course-overview, dashboard |
| Lesson | data field | `completed`, `in-progress`, `not-started`, derived `locked` (sequential), `active` (current) | course-player, course-overview |
| Assignment | `statusOf()` | `todo`, `in-progress` (has draft), `overdue` (past due, window open), `closed` (past window; labelled "Overdue" + "Submission closed"), `submitted` (results hidden), `grading`, `graded` | assignments, assignment-detail ("Same derivation") |
| Live session | `statusOf()` | `upcoming`, `soon` (≤15 min, join window), `live`, `completed`, `cancelled`, `not-started` (instructor didn't start within 30 min) | live-sessions, live-session-detail |
| Certificate | `statusOf()` | `valid`, `expired`, `revoked` | certificates, certificate-detail |

---

## 5. Global Shell

### C01 · Learner App Shell
- **Purpose:** Two-column app frame with the sidebar, top bar and scrolling main area.
- **Where used:** All Learner pages except `course-player.html`.
- **Implementation:** `.shell` grid, duplicated in each page (e.g. `dashboard.html:52-58`, `my-courses.html:46-53`). Class **E**.
- **Structure:** sidebar iframe (col 1, rows 1–2), top-bar iframe (col 2, row 1), `<main class="main">` (col 2, row 2, `overflow-y:auto`), `.main-inner`.
- **Visual:**
  - `grid-template-columns: 232px 1fr` and `grid-template-rows: 80px 1fr`.
  - `height: 100vh` (my-courses uses `min-height:100vh`).
  - Sidebar iframe has `border-right:1px solid #e5e5e5`.
  - Top-bar iframe has `background:#fff; border-bottom:1px solid #e5e5e5`.
  - Page background is `--surface-canvas #fafafa`.
- **Content padding (`.main-inner`):** fluid, with **no max-width** ("Fluid — fills the main column at any width; grid adds columns instead of centering", `my-courses.html:51`).

  | Page | Padding (top · sides · bottom) |
  |---|---|
  | dashboard, my-courses, assignments | `32px clamp(20px,2.6vw,48px) 64px` |
  | live-sessions, certificates | `32px … 72px` |
  | course-overview | `24px … 32px` |
  | assignment-detail | `24px … 64px` |
  | live-session-detail, certificate-detail | `24px … 72px` |
  | revision-notes | `28px … 72px` |
  | flashcard-study | `28px clamp(16px,2.6vw,48px) 48px` |
- **States:**
  - **Collapsed (desktop):** `.shell.sidebar-collapsed { grid-template-columns:0 1fr }`, and the sidebar border is removed.
  - The collapsed state is toggled by the top-bar toggle through `postMessage`.
- **Responsive:** at ≤900px it becomes C06 (mobile drawer), and `.main-inner` padding becomes `20–22px 16px 36–56px`.

### C02 · Learner Sidebar
- **Purpose:** Primary Learner navigation.
- **Where used:** Every shell page, loaded as `<iframe src="../component/sidebar.html?active=KEY">`.
- **Implementation:** `designs/Learner/component/sidebar.html` (shared, runtime include; file comment cites "CLAUDE.md Rule 8's documented exception"). Class **B**.
- **Structure:**
  1. Logo row (`.sidebar-logo`, UpSpace wordmark SVG).
  2. `.nav-scroll` with 6 items:
     - Dashboard (`layout-dashboard` icon)
     - My Courses (`book-open`)
     - Assessments (`list-checks` → `assignments.html`)
     - Live Sessions (`video`)
     - Certificates (`award`)
     - Your Coach (`messages-square`)
  3. `.nav-bottom` pinned with `margin-top:auto`: Settings (`#`) and Logout (→ sign-in, `.danger`).
- **Visual** (`sidebar.html:36-48`):
  - Background `#ffffff` (not canvas).
  - Logo row: height `80px`, padding `0 20px`, `border-bottom:1px solid #e5e5e5`. Wordmark height `20px`, color `#171717`, hover `opacity:.8`.
  - `.nav-scroll`: padding `14px 12px 6px`, `gap:2px`.
  - `.nav-item`:
    - Layout: `display:flex; gap:12px; padding:10px 12px; border-radius:8px; color:#525252`.
    - Label: `13.5px/600`, ellipsis.
    - Icon: `19×19`, Lucide stroke-2.
  - `.nav-bottom`: `border-top:1px solid #f0f0f0`, `padding:10px 12px`.
- **States:**
  - **Hover:** `background:#f5f5f5; color:#171717`, and the icon lifts `translateY(-1px)`.
  - **Active** (`?active=` → `.active`): `background:#eff6ff (info-subtle); color:#2563eb (info); font-weight:700`. Note that the active state uses the **info blue**, not brand indigo.
  - **Danger hover:** `#fef2f2 / #dc2626`.
  - **Focus-visible:** `outline:2px solid #6366f1; outline-offset:-2px`.
- **Interaction:** links target `_parent`. Selection is URL-driven, not JS state.
- **Responsive:** see C06.
- **Note:** the file's header comment ("Only Dashboard is a real link today…") is stale. All six items now link to real files.

### C03 · Learner Top Bar
- **Purpose:** Page context (breadcrumb), sidebar toggle, search, notifications and profile menu.
- **Where used:** All shell pages, loaded as `<iframe src="../component/topnavbar.html?current=…[&parent=…&parentHref=…]">`.
- **Implementation:** `designs/Learner/component/topnavbar.html`. Class **B**.
- **Structure:**
  - Left: sidebar-toggle icon button (`panel-right` icon), then breadcrumb `Learner / [Parent /] Current`.
  - Right: search field, bell button, avatar button with dropdown (C04).
- **Visual** (`topnavbar.html:26-64`):
  - Bar: `height:80px; padding:0 32px 0 20px; justify-content:space-between; gap:16px`, background `#fff`.
  - Toggle / bell `.icon-btn`: `36×36`, `border-radius:50%`, transparent, color `#525252`, icon `18px`, hover `#f5f5f5`.
  - Breadcrumb:
    - `13px`, gap `6px`.
    - Links `#a3a3a3 / 600` (hover `#171717`).
    - Separator `/` uses `color:var(--text-disabled)`. **This token isn't declared in topnavbar's `:root`** (see §31).
    - Current item `#171717 / 700`, ellipsis.
  - Search:
    - Width `240px`, height `36px`, `border-radius:8px`, `1px #e5e5e5`, background `#fafafa`, `13px`, left icon `16px` at `12px`, padding-left `34px`.
    - Focus changes only `border-color:#6366f1` (no glow ring, unlike page inputs).
    - Placeholder "Search courses".
  - Avatar: `36×36` circle, `linear-gradient(135deg,#4f46e5,#0ea5e9)`, white initials `13px/700` ("SC").
- **States:** the search field is hidden at `max-width:700px`. The bell shows a static red dot (C05).
- **Interaction:**
  - Toggle → `postMessage('toggle-sidebar')`.
  - `?parent=` adds a middle crumb. `parentHref` is accepted only if it matches `^\.\.\/code\/[\w-]+\.html$`, otherwise it becomes `#`.
  - **Search has no JS behavior** (no handler; decorative).
  - The profile dropdown is described in C04.

### C04 · Profile Menu Dropdown
- **Purpose:** Account links.
- **Where used:** Top bar (C03).
- **Implementation:** `.profile-menu` / `.profile-dropdown` in `topnavbar.html:52-61, 104-112`. Class **C** (extends the Dropdowns pattern; not claimed as library).
- **Structure:** My Profile, Account Security, Preferences (all `href="#"`), then `<hr>`, then Log Out (`.danger`, → sign-in).
- **Visual:**
  - Panel: `position:absolute; top:44px; right:0; width:200px; background:#fff; border:1px solid #e5e5e5; border-radius:8px; padding:6px; box-shadow:0 12px 32px -8px rgba(23,23,23,.18)`.
  - Item: `padding:9px 10px; border-radius:6px; 13.5px`, hover `#f5f5f5`.
  - `hr` in `#f0f0f0`. Danger item text is `#dc2626`.
- **States / interaction:**
  - Click toggles `.show`, and any click outside `.profile-menu` closes it.
  - No Escape handling, no keyboard arrow navigation. `aria-expanded` is set in markup but never updated.

### C05 · Notification Bell (indicator only)
- **Purpose:** Unread-notification indicator.
- **Where used:** Top bar.
- **Implementation:** `.icon-btn` + `.dot` (`topnavbar.html:43-46`). Class **B**.
- **Visual:** dot `8×8`, `#dc2626`, `border:2px solid #fff`, `top:6px; right:6px`.
- **Interaction:** none. There is no panel, no count, and no page. This is the full extent of the "notifications" UI.

### C06 · Mobile Navigation Drawer
- **Purpose:** Off-canvas sidebar on small screens.
- **Where used:** All shell pages (`@media (max-width:900px)` block in each file).
- **Implementation:** CSS in each page plus `.sidebar-backdrop`. Class **E**.
- **Visual:**
  - The shell becomes `0 1fr`, and the top bar and main area span both columns.
  - Sidebar iframe: `position:fixed; left:0; width:260px; height:100vh; z-index:30; transform:translateX(-100%); transition:transform .25s ease; box-shadow:4px 0 24px rgba(0,0,0,.12)`.
  - Backdrop: `position:fixed; inset:0; background:rgba(15,23,42,.45); z-index:25`.
- **Interaction:**
  - The same `.sidebar-collapsed` class is reused with **inverted meaning**: on mobile it *opens* the drawer (`transform:translateX(0)`) and shows the backdrop.
  - Clicking the backdrop closes the drawer.
  - No Escape key, no focus trap.

---

## 6. Navigation

The Learner build uses four navigation mechanisms:
1. The sidebar (C02) for primary navigation.
2. The top-bar breadcrumb (C03), which gives context only.
3. **In-page breadcrumbs** (C07) on every detail screen.
4. **Back links** (C08) on focused and tool screens.

There are no tabs used as page navigation. Tabs only filter or switch views (§11). Row and card clicks are the main way to drill into a detail page (I05).

### C07 · In-page Breadcrumbs
- **Purpose:** Return path from a detail page to its list.
- **Where used:**
  - course-overview (`My Courses › Course`)
  - assignment-detail (`Assignments › Title`)
  - live-session-detail (`Live Sessions › Title`)
  - certificate-detail (`Certificates › Course`)
  - flashcard-study (`My Courses › Course › Flashcards`)
  - course-player header (`Course › Lesson`)
- **Implementation:** `.crumbs` (e.g. `course-overview.html:77-81`, `assignment-detail.html:80-84`). File comments say "Breadcrumbs — library pattern (Only Text, Arrow separator)". Class **A**.
- **Structure:** `<nav class="crumbs" aria-label="Breadcrumb">`, then link, `chevron-right` SVG, `<span aria-current="page">`.
- **Visual:**
  - `display:flex; gap:6px; font-size:14px`.
  - `margin-bottom:18px`; `20px` on overview and `16px` on flashcards.
  - Links `#525252 / 500`, hover `#171717`.
  - Separator icon `16px`, `#d4d4d4`.
  - Current item `600`, ellipsis.
- **States:** while loading, the current crumb shows a `160×12` skeleton bar (assignment, live, certificate detail).
- **Responsive:** in the player at ≤640px the links and separators are hidden, and only the current lesson title remains.
- **Difference from the top-bar breadcrumb:** the top bar uses `13px`, `/` text separators and a tertiary link color. The in-page breadcrumb uses `14px`, chevron icons and a secondary link color.

### C08 · Back Link
- **Purpose:** One-step return from a focused screen.
- **Where used:** course-player header ("‹ My Courses") and revision-notes ("‹ Back to <course>").
- **Implementation:** `.back` (`course-player.html:64-66`, `revision-notes.html:79-81`). Class **B**.
- **Visual:**
  - `inline-flex; gap:6px; 14px/600; color:#525252`, with a chevron-left icon (18px in the player, 16px in revision notes).
  - Player: `height:36px; padding:0 10px 0 6px; border-radius:8px`.
  - Revision notes: `padding:6px 10px 6px 6px; margin-left:-6px; border-radius:6px`, with `margin-bottom:18px`.
- **States:** hover `background:#f5f5f5; color:#171717`.
- **Responsive:** in the player at ≤640px the label is hidden and only the icon shows.

### C09 · Focused Player Header
- **Purpose:** Minimal chrome for the course player, which has no sidebar.
- **Where used:** `course-player.html` only.
- **Implementation:** `.header` (`course-player.html:63-77`). Class **B**.
- **Structure:**
  1. Back link (C08)
  2. `1×24px` divider
  3. Breadcrumb (C07)
  4. Spacer
  5. Course progress: 140px bar + "**68%** complete"
  6. Rail toggle icon button (C16, 40px bordered)
- **Visual:**
  - `position:sticky; top:0; z-index:20; height:64px (--header-h); gap:16px; padding:0 clamp(16px,2vw,28px); background:#fff; border-bottom:1px solid #e5e5e5`.
  - Progress text `13px #525252`; the percentage is bold `#171717` with tabular numerals.
- **Responsive:**
  - ≤1024px: the header progress bar is hidden and only the text remains.
  - ≤640px: the crumb links, divider, back label and the whole progress block are hidden.

---

## 7. Page Layout Patterns

### 7.1 Global layout constants
| Constant | Value | Source |
|---|---|---|
| Sidebar width | `232px` (desktop). The mobile drawer is `260px` | every page `.shell` |
| Top bar height | `80px` (shell). The player header is `64px` | shell / `course-player.html:36` |
| Content max-width | **None.** Fluid to the main column. Exception: Coach centers an `800px` column. The certificate document caps at `960px` | `my-courses.html:51`, `coach.html:70`, `certificate-detail.html:83` |
| Page side gutter | `clamp(20px, 2.6vw, 48px)` (flashcards `clamp(16px,…)`); mobile `16px` | `.main-inner` |
| Page top padding | list pages `32px`; detail pages `24px`; tool pages `28px` | §5 C01 table |
| Section spacing | `40px` between major sections (dashboard `.stack`, my-courses `.top` margin-bottom, overview `.section` margin-top, revision-notes `.doc section`); `32px` on the dashboard at ≤760px | |
| Stacked-card gap (detail pages) | `20px` (`.stack{gap:20px}`) | assignment/live detail |
| Two-column gap | `clamp(24px, 2.4vw, 36px)` (details); `clamp(24px,2.4vw,40px)` (dashboard); `clamp(24px,2.5vw,40px)` (overview); `20px` (my-courses top); `clamp(20px,2vw,36px)` (revision notes / flashcards) | |
| Card grid gap | `24px` (course cards); `20px` (certificate cards); `16px` / `14px` on mobile | |
| Header → content | `margin-bottom:24px` (page head) / `22px` (live, certificate head) / `14px` (section header → section) | |

### 7.2 Breakpoints found (max-width unless noted)
| Breakpoint | What changes |
|---|---|
| `1180px` | my-courses top section stacks; live-session rows drop the Status column (status moves inline); certificate-detail layout stacks |
| `1100px` | detail layouts (overview, assignment, live detail) stack and the side card moves **above** the main content (`order:-1`, `position:static`); assignments table folds the Grade column into Status; revision-notes / flashcard rails drop below as an auto-fit grid |
| `1080px` | dashboard 2-column grid stacks |
| `1024px` | course-player right rail becomes an off-canvas drawer |
| `900px` | shell switches to the mobile drawer (C06) |
| `880px` container (min-width) | player Transcript/Tutor show side by side (container query on `.main-col`) |
| `760px` | assignments table and live-session rows become stacked cards; dashboard hero stacks; flashcard dialog form becomes 1 column; live toolbar search goes full-width |
| `700px` | my-courses hero stacks and the grid becomes 1 column; overview side card goes to block layout; top-bar search hidden |
| `640px` | assignment/live/certificate detail compact padding; player compact (icons-only nav buttons); coach and flashcard compact |
| `560px` | flashcard dialog form becomes 1 column |
| `(hover:none)` | flashcards hide keyboard hints |
| `(prefers-reduced-motion:reduce)` | every page: `*{transition:none!important;animation:none!important}` |

### 7.3 Recurring page structures

**P1 · List page** (my-courses, assignments, live-sessions, certificates)
```
Page Header (H1 + subline | search right-aligned)        C10
→ Toolbar (segmented tabs · spacer · selects / view toggle) C45
→ [optional emphasised block: Continue hero / Next session] C22 / C25
→ Content: card grid | table | date-grouped row lists       C21 / C27 / C29 / C26
→ In-place skeleton → empty / filtered-empty / error         C102 / C103 / C104
(no pagination)
```

**P2 · Dashboard** (dashboard)
```
Greeting (H1 "Good afternoon, Sophia" + status sentence)   C12
→ 2-col grid  [Continue learning 1.7fr | Coming up minmax(300px,1fr)]
→ full-width "Keep going" course-card grid
Each section = Section Header (H2 + right link) + panel         C13
```

**P3 · My Courses** (a P1 variant with a top band)
```
Page Header → Top band [Continue hero 1.7fr | Due soon · Mandatory minmax(300px,1fr)] (hidden while searching)
→ Toolbar (status tabs · spacer · Type select · Sort select) → Course grid
```

**P4 · Detail page with sticky side card** (course-overview, assignment-detail, live-session-detail, certificate-detail)
```
In-page Breadcrumbs                                          C07
→ Detail Header (status/eyebrow → H1 → course/subline)       C11
→ Layout grid: minmax(0,1fr) | side column (sticky top:0)
     main: stacked .card.section blocks (gap 20)             C20
     side: summary/CTA card with actions + dl facts          C23 / C68 / C74
→ ≤1100/1180px: side card moves ABOVE main content, static
```
Side column widths: overview `minmax(320px,400px)`, assignment `320px`, live `340px`, certificate `340px`.

**P5 · Focused player** (course-player)
```
Focused header 64px (back · crumbs · progress · rail toggle)  C09
→ grid [main-col 1fr | rail 384px]  (rail collapsible → 0)
     main: Video stage → Lesson head (eyebrow, H1, Prev/Next) → Transcript | AI Tutor panels
     rail: "Course content" head + progress → module accordion
```

**P6 · Conversational page** (coach)
```
Centered column max-width 800px
empty:  vertically centered hero (AI mark, H1, sub) → composer → suggestion chips
active: thread (gap 26) → sticky bottom composer with fade-in gradient
```

**P7 · Study-tool page with rail** (revision-notes, flashcard-study)
```
Back link / breadcrumbs → Module/Set header with right-aligned actions
→ grid [main 1fr | rail clamp(280px,22vw,380px) (flashcards clamp(280px,22vw,360px)), sticky top:20px]
→ ≤1100px: rail drops below as auto-fit(260px) card grid
```

**P8 · Centered state page** (flashcards not found / revision-notes blocked / not-found pages)
```
Single white card, centered text, icon circle → title → paragraph → centered actions
```

### 7.4 Content grids
| Grid | Definition | Where |
|---|---|---|
| Course cards (My Courses) | `repeat(auto-fill, minmax(300px,1fr))`, gap `24px`; ≤700px 1 column, gap `16px` | `my-courses.html:127` |
| Course cards (Dashboard) | `repeat(auto-fit, minmax(240px,1fr))`, gap `24px` | `dashboard.html:83` |
| Certificate cards | `repeat(auto-fill, minmax(290px,1fr))`, gap `20px`; ≤640px 1 column, gap `14px` | `certificates.html:96` |
| Dashboard main | `minmax(0,1.7fr) minmax(300px,1fr)` | `dashboard.html:72` |
| My-courses top | `minmax(0,1.7fr) minmax(300px,1fr)` | `my-courses.html:72` |
| Revision-note tiles / sections | `auto-fit minmax(220px,1fr)`, `auto-fill minmax(min(100%,420px),1fr)`, `minmax(min(100%,300px),1fr)` | `revision-notes.html` |

### 7.5 Page & section header components

#### C10 · List Page Header
- **Purpose:** Title the list screens and hold their primary search.
- **Where used:** my-courses, assignments, live-sessions, certificates.
- **Implementation:** `.page-head` (`my-courses.html:56-58`, `assignments.html:53-56`). Class **E**.
- **Structure:** `<div>` with H1 and `.sub`, and on the right the search field (C37) on my-courses and assignments. Live-sessions and certificates have no search in the header: live puts search in the toolbar, and certificates has none.
- **Visual:**
  - `display:flex; align-items:flex-end; justify-content:space-between; gap:16px 24px; flex-wrap:wrap; margin-bottom:24px` (22px on live).
  - H1 `28px/700`, `letter-spacing:-.6px`, `margin:0 0 4px`.
  - `.sub` `14–15px #525252`.
- **Copy pattern:** title plus a one-sentence purpose line:
  - "Your assigned and enrolled learning."
  - "Keep track of work that needs to be completed."
  - "Join upcoming sessions and revisit sessions you've attended."
  - "View and download the certificates you've earned."
- **Responsive:** H1 becomes `24px` at ≤760px (live) and ≤640px (certificates). The search wraps to its own line, and in the live toolbar it goes full width.

#### C11 · Detail Header
- **Purpose:** Identify a single record.
- **Where used:** course-overview, assignment-detail, live-session-detail, certificate-detail.
- **Implementation:** `.head`. Class **E**.
- **Structure (varies by page):**
  - Overview: badges row (C49) → H1 → lead paragraph → byline (32px initials avatar + "Created by **Prof. Vance**") → stat chips (C24).
  - Assignment: eyebrow ("**Course link** · Module 4 · Binary Trees") → H1.
  - Live: status dot (C48) → H1 (struck through when cancelled) → "**Course link** · with Instructor".
  - Certificate: status pill (C49) → H1 (course) → sub "Template · Issued Sep 10, 2026".
- **Visual:**
  - H1 is fluid:
    - `clamp(26px,2.2vw,32px)/700/-.6px` (assignment, live)
    - `clamp(24px,2.1vw,30px)` (certificate)
    - `clamp(28px,2.4vw,38px)/-.8px` (overview)
  - Line-height `1.15–1.2`, `text-wrap:balance`.
  - Head `margin-bottom:22–24px`.
  - Overview lead: `16px/1.65 #525252`, `max-width:72ch`. An empty description renders "No description available." in `#a3a3a3` italic.
- **States:** loading shows skeleton bars at H1 size. Cancelled H1: `color:#a3a3a3; text-decoration:line-through; text-decoration-thickness:2px`.

#### C12 · Dashboard Greeting
- **Purpose:** Personal greeting plus a one-line status summary.
- **Where used:** dashboard.
- **Implementation:** `.greet` (`dashboard.html:66-69`). Class **B**.
- **Visual:**
  - H1 `clamp(24px,1.2vw+14px,30px)/700/-.6px`, `margin:0 0 6px`.
  - Sub `15.5px/1.5 #525252` with bold `#171717` fragments.
  - `margin-bottom:32px`.
- **States:** the sub line changes per state:
  - **normal:** "You have **1 overdue assignment** and **2 live sessions today**."
  - **empty:** "Welcome to UpSpace."
  - **loading:** "Getting your learning ready…"
  - **no-work:** "Nothing is due right now. A good moment to keep going."
  - **no-courses:** "Ready to start something new?"
  - **error:** "Some of your information didn't load."
- **Greeting time:** "Good morning / afternoon / evening" from the local hour.

#### C13 · Section Header
- **Purpose:** Title a section with an optional right-aligned link or action.
- **Where used:** dashboard (`.sec-h`), course-overview (`.section-head`), my-courses (`.section-label`), live-session "Next session" label, revision-notes (`.sec-h` with number).
- **Implementation:** Class **E**, with 3 variants:
  1. **Title + link:** `display:flex; align-items:baseline; justify-content:space-between; margin-bottom:14px`. H2 is `17px/700/-.2px` (dashboard) or `20px/700/-.3px` with a `13.5px #a3a3a3` sub line (overview "6 modules · 22 lessons · 4h 12m"). The right link is C17.
  2. **Uppercase eyebrow label:** `12px/700`, `letter-spacing:.06em`, uppercase, `#a3a3a3`, `margin:0 0 12px`. Used for "CONTINUE LEARNING", "DUE SOON · MANDATORY", "NEXT SESSION", and the overview "PREREQUISITES".
  3. **Numbered section heading** (revision notes): `28×28` r6 `#eef2ff` / `#4f46e5` number tile, H2 `18px/700`, and a right-aligned `13px #a3a3a3` count.

---

## 8. Buttons & Actions

### C14 · Button
- **Purpose:** The primary action element.
- **Where used:** Every page.
- **Implementation:** `.btn` + `.btn-primary` / `.btn-secondary` / `.btn-ghost` / `.btn-danger`, re-declared in each file. File comments say "Buttons (library)" and "library sizes (md 40 / lg 44)". Class **A**, with Learner-specific size deviations noted below.
- **Base (all files):**
  - Layout: `display:inline-flex; align-items:center; justify-content:center; gap:8px; border-radius:8px; font-weight:600; white-space:nowrap; transition:background-color .15s ease[, transform .1s ease]`.
  - Icon: `16px` (15px on my-courses, 17px on overview and certificate detail).
- **Variants:**

  | Variant | Default | Hover | Notes |
  |---|---|---|---|
  | Primary | `#4f46e5`, white text | `#4338ca` | — |
  | Secondary | `#fff`, text `#404040`, `1px #e5e5e5` border | `#f5f5f5` | — |
  | Ghost | transparent, text `#525252` | `#f5f5f5`, text `#171717` | assignment-detail, flashcards |
  | Danger | `#dc2626`, white | `#b91c1c` | revision-notes `.btn-danger`. Course-overview does this with an inline `style="background:var(--error)"` on `.btn-primary` |
  | Block | `width:100%` | — | Side-card CTAs |

- **Sizes as implemented (vary by file):**

  | Where | Base height / padding / font | `-lg` | `-sm` |
  |---|---|---|---|
  | dashboard | 40 / 0 16 / 14 | 44 / 0 18 / 15 | 34 / 0 12 / 13.5 |
  | my-courses | 40 / 0 18 / 13.5 | — | — |
  | assignments, course-player, revision-notes, flashcards | 40 / 0 16 / 14 | revision-notes 48 / 0 22 / 15 | — |
  | assignment-detail, live-sessions | 40 / 0 16 / 14 | 44 / 0 18 / 14.5 | — |
  | live-session-detail | 40 / 0 16 / 14 | **48** / 0 20 / 15 | — |
  | course-overview, certificate-detail | **44** / 0 18 / 14.5 | — | — |
  | certificates, coach | **36** / 0 14 / 13.5–14 | — | — |
  | inline row action (live-session rows) | 36 / 0 14 | — | — |

- **States:**
  - **Active:** `transform:scale(.97)` (my-courses, overview, player) or `scale(.98)` (assignment, live, certificates).
  - **Disabled:** usually `background:#e5e5e5; color:#a3a3a3` or `#525252`, border transparent, `cursor:not-allowed`.
    - Player uses `opacity:.45` instead.
    - Primary-disabled while submitting is `opacity:.75`, keeping the brand color.
    - `aria-disabled="true"` on `<span class="btn">` is used for non-clickable CTAs ("Submission closed", locked "Start course").
  - **Secondary disabled as "Saved" confirmation:** in revision notes it is `color:#15803d; background:#f0fdf4; border-color:#bbf7d0`. In coach and flashcards it only greys out.
  - **Busy/loading:** see C15.
- **Hierarchy convention:**
  - One primary per region, secondary beside it.
  - Cancel is on the left and confirm on the right, right-aligned (`justify-content:flex-end`) in modals and popovers.

### C15 · Button Busy / Loading State
- **Purpose:** Show that an async action is in progress.
- **Where used:**
  - Assignment "Submitting…"
  - Live "Joining…"
  - Certificate download "Preparing…" / "Preparing PDF…"
- **Implementation:** the button gets `disabled` (or class `busy`), and its content is replaced by `<span class="spin"></span>Label…`. Class **C**.
- **Visual:**
  - `.spin` is `16×16` (14px on the certificate list), `border:2px solid rgba(255,255,255,.45); border-top-color:#fff; border-radius:50%; animation:spin .8s linear infinite`.
  - On secondary buttons the spinner is grey: `border:2px solid #e5e5e5; border-top-color:#525252`.
  - `.busy{opacity:.7–.85; cursor:progress}`.
- **Interaction:** the Cancel button next to it is disabled during submission (`assignment-detail.html:744-746`).

### C16 · Icon Button family
- **Purpose:** Compact icon actions.
- **Class:** **C**. Implementations differ per context:

| Class | Size / shape | Style | Where |
|---|---|---|---|
| `.icon-btn` (top bar) | 36, circle | transparent, hover `#f5f5f5` | top bar |
| `.icon-btn` (player) | 40 (rail close 34), r8 | `#fff`, `1px #e5e5e5`, text `#525252`, hover `#f5f5f5` | player header, rail |
| `.icon-btn` (revision notes) | 40, r8, bordered | + **CSS tooltip** from `data-tip` (`::after`, `#171717`, 12px) and `.danger` hover `#fef2f2 / #dc2626 / #fecaca` | notes header actions |
| `.ib` (assignment / live detail) | h32, min-w 32, `padding:0 8px`, r6 | ghost, can carry a text label `13px/600`, `.danger` hover | file rows, toast close, copy |
| `.ib` (overview AI) | 34×34, r6 | ghost; `aria-pressed="true"` → `#eef2ff` / `#4f46e5` | Ask-AI answer head, sheet head |
| `.fc-x` | 36×36, r6 | ghost, tertiary icon | dialog close |
| `.ctrl` (video) | h36 (34 on recordings), min-w 36, r6 | transparent on dark, white; hover `rgba(255,255,255,.14)`; `.on` `rgba(255,255,255,.22)` | video controls |
| `.nav-cluster button` | 34×34, r8, bordered | calendar prev/next | live calendar |

### C17 · Inline Text Action (link, row link, link button)
- **Purpose:** Low-emphasis navigation or action.
- **Implementation (Class C):**
  - `.link` on the dashboard: `14px/600 #4f46e5`, hover `#4338ca` + underline.
  - `.link` in live-sessions, `.row-link` in assignments, `.link-btn` in the overview: `inline-flex; gap:6px; 14px/600; color:#4f46e5; padding:6px 8px; margin:0 -8px; border-radius:6px`, hover `background:#eef2ff`, trailing 16px arrow.
  - `.quiet` modifier: text `#525252`, hover `#f5f5f5`.
  - **Certificate links use info blue** `#2563eb` (`.cert-link` on my-courses, `.cert` on the overview), not brand indigo.
  - Prose links: `#4f46e5`, `text-decoration:underline; text-underline-offset:2px`.
- **Where used:**
  - Dashboard section links ("All work", "All courses", "Course overview")
  - Assignment row actions
  - Live-session row actions ("View details", "Watch recording", "View materials")
  - Overview "Expand all / Collapse all"
- **Convention:** state-dependent labels and emphasis. For example, assignment `ACTION` map (`assignments.html:176`):
  - `todo` → "Open assignment"
  - `overdue` → "Submit assignment"
  - `in-progress` → "Continue draft"
  - `grading` / `submitted` → "View submission" (quiet)
  - `graded` → "View grade"
  - `closed` → "View details" (quiet)

### C18 · Compact Action Buttons
- **Class:** **C**. Small bordered buttons used in dense areas:

  | Class | Size | Style | Where |
  |---|---|---|---|
  | `.sbtn` | h34, `0 12px`, 13.5/600 | `1px #e5e5e5`, `#fff`; `.primary` variant is brand-filled | overview revision-notes row: "View", "Download PDF", "Create revision notes" |
  | `.mini` | h30, `0 10px`, 12.5/600, r6 | `.on` → `#eef2ff` bg, `#e0e7ff` border, `#4f46e5` text | player panel heads: "Auto-scroll", "Clear" |
  | `.copy` | h32, r6, 13/600, bordered | label changes to "✓ Copied" for 1.6 s | certificate verification code |
  | `.today-btn` | h34, r8, 12.5/600, bordered | — | calendar "Today" |

### C19 · Send / Stop Round Buttons
- **Purpose:** Submit and stop in chat composers.
- **Where used:** overview dock and sheet, player tutor, coach.
- **Implementation (Class B):**
  - `.send`:
    - overview: 36 circle
    - player: 38, r8
    - coach: 40, r8
    - All are `#4f46e5` with a white `arrow-up` 17px icon, hover `#4338ca`, and disabled `opacity:.3–.35` while the input is empty or busy.
  - `.stop` (overview dock only): 36 circle, `#eef2ff` / `#4f46e5`, 12px square icon, hover `#e0e7ff`.

---

## 9. Cards

**Card treatment convention:** white (`#fff`) surface on the `#fafafa` canvas, `1px solid #e5e5e5`, no shadow. Hover (when clickable) darkens the border to `#a3a3a3` and never lifts. Radius is `12px` for list cards and detail sections, and `16px` for hero or large panels.

### C20 · Surface Card / Panel
- **Purpose:** Base container for every section.
- **Where used:** All pages (`.panel`, `.card`, `.card.section`, `.rows`, `.table-wrap`, `.outline`, `.cal-card`).
- **Implementation:** Class **E**.
- **Variants:**

  | Variant | Radius | Padding | Where |
  |---|---|---|---|
  | Panel | 16 | per content | dashboard panels, overview outline and side card, player panels, revision-notes cards, flashcard face |
  | Section card | 12 | `22px 24px` (`18px 16px` at ≤640px); H2 `17px/700` with `margin-bottom:14px` | assignment and live detail |
  | Side card | 12 | `20px` | certificate detail, assignment summary |
  | Row container | 12 | none; rows inside, `overflow:hidden` | lists and tables |

- **Where it diverges from `UpSpaceDESIGN.md`:** the DS says cards use `surface-raised #f5f5f5`. Learner cards are **white**, and `#f5f5f5` is used for table headers, certificate stages, tile backgrounds and hovers.

### C21 · Learner Course Card
- **Purpose:** Represent one enrolled course in a grid.
- **Where used:** my-courses (grid) and dashboard ("Keep going"; the file comment says "same pattern as my-courses.html (reused as-is)").
- **Implementation:** `<a class="course-card">` (`my-courses.html:127-156`, `dashboard.html:83-104`). Class **B**.
- **Structure:**
  1. `.course-photo-wrap`: 16:9 image with the tag chip (C52) top-left, and a completed check badge top-right when completed.
  2. `.course-card-body`: title → meta line (dot-separated) → footer (progress row if in progress) → action row (label + arrow, or "Certificate" link).
- **Visual:**
  - Card `border-radius:12px; border:1px solid #e5e5e5; overflow:hidden; transition:border-color .2s`.
  - Body `padding:18px`.
  - Title `16px/700/1.3`, `letter-spacing:-.2px`, `text-wrap:balance`.
  - Meta `13px #a3a3a3`, gap 8, with `3×3` dot separators in `#d4d4d4`:
    - "Mandatory" `#ca8a04/600`
    - "Overdue · Sep 18" `#dc2626/600`
    - otherwise "Optional", "Due Sep 30" or a duration
  - Footer `padding-top:18px; margin-top:auto`.
  - Progress: 6px bar (C46) + `13px/700` tabular percentage.
  - Action: `13.5px/600 #4f46e5`, space-between, with a 16px arrow.
- **Variants (by status):**

  | Status | Meta | Progress | Action | Visual change |
  |---|---|---|---|---|
  | In progress | Mandatory/Optional · Due | bar + % | "Continue →" | — |
  | Not started | Mandatory/Optional · Due · duration | none | "Start course →" | — |
  | Completed | "Completed Sep 10" | none | "Review" + "Certificate" (info blue) when a certificate exists | card bg `#fafafa`, image `grayscale(60%) brightness(.95)`, title and action `#525252`, 28px green check badge |
  | Overdue (not completed) | "Overdue · date" in red | as status | as status | — |

- **Interaction:**
  - Hover: border `#a3a3a3`, image `scale(1.05)` over `.6s cubic-bezier(.2,.7,.2,1)`, arrow `translateX(3px)`.
  - The whole card is one link. **Every card goes to the course overview**, including in-progress ones. The file notes this "deviates from CDL-001-FR-04" by user decision.
- **Responsive:** grid columns come from auto-fill (§7.4). One column at ≤700px on my-courses.
- **Loading:** `.skeleton-card` with a 16:9 thumbnail bar and two 14px lines (my-courses), or the same card with skeleton lines (dashboard).

### C22 · Continue Learning Hero
- **Purpose:** One emphasized resume target, the last-accessed in-progress course.
- **Where used:**
  - dashboard `.panel.hero` (`dashboard.html:74-88`)
  - my-courses `a.hero` (`my-courses.html:77-94`)
- **Implementation:** Class **B**. Two implementations of the same idea.
- **Dashboard variant:**
  - Grid `minmax(200px,40%) | 1fr`, radius 16.
  - Thumbnail uses `min-height:260px`, background cover, with a white pill tag (26px, `rgba(255,255,255,.92)`, 12.5/600) top-left.
  - Body padding `clamp(22px,2vw,32px)`:
    - H3 `clamp(20px,.8vw+14px,26px)/700/-.5px`.
    - "Next: **lesson title** · 9 min left" in `15px #525252`.
    - Progress row "68% complete · due Sep 30" left and "**14 / 21 lessons**" right, over an **8px** bar.
    - Actions `margin-top:auto`: primary **lg** "Continue lesson →" (→ player) + text link "Course overview".
- **My Courses variant:**
  - Whole card is one link, grid `1.1fr | 1fr`, `min-height:280px`.
  - Media has a bottom gradient overlay and a **52px white circular play button** (brand icon, `box-shadow:0 8px 20px rgba(15,15,30,.25)`) at bottom-left.
  - Body: eyebrow tag in brand `12.5px/600` → title `clamp(20px,1.6vw,26px)` → "Up next: Module 4 · Binary Trees · Lesson 3" → progress "Progress **68%**" + 6px bar → non-interactive `span.btn-primary` "Resume →".
  - Hover: border `#a3a3a3`, image `scale(1.04)`, play button `scale(1.08)`, button bg → hover color.
  - **Fallback:** when nothing is in progress, the label becomes "Up next", the text "Not started · 5h total", the CTA "Start course", and it links to the overview.
- **Responsive:** dashboard stacks at ≤760px (thumbnail `aspect-ratio:16/8`). My-courses stacks at ≤700px (media 16:9, body padding 20).
- **States:**
  - Dashboard loading: grey thumbnail + skeleton bars.
  - Error: C104 inline error with "Try again".
  - No courses: C103 "You're not in the middle of a course." + "Browse My Courses".

### C23 · Course Status Side Card
- **Purpose:** Course CTA, progress, assignment facts and prerequisites on the overview.
- **Where used:** course-overview `.side .card` (`course-overview.html:153-181`).
- **Implementation:** Class **B**.
- **Structure:**
  1. 16:9 thumbnail. It shows a `#d4d4d4` image-icon placeholder when there's no photo, and `grayscale(55%)` when completed.
  2. `.card-body` (padding 20): "Your progress **68%**" + 8px bar → note line → CTA (block button) → Flashcards secondary block button (C91 entry).
  3. `dl.dl` facts (C32): Type, Assigned by, Deadline (red with "· overdue"), Starts.
  4. `.prereq`: uppercase label + list of prerequisite courses with a check or empty-circle icon, linking to each course.
- **CTA by status:**

  | Status | Note | Primary CTA | Extra |
  |---|---|---|---|
  | In progress | "Last accessed: **lesson**" | "Continue →" | Flashcards button |
  | Completed | "Completed on **date**" | **secondary** "Review course" | "View certificate" info-blue link with award icon; Flashcards |
  | Not started, unblocked | — | "Start course →" | Flashcards |
  | Not started, blocked (prerequisites or future start) | — | `span.btn-primary[aria-disabled]` "🔒 Start course" (grey) | `.block-note` with warning-colored info icon: "Complete X and Y to unlock this course." / "This course opens on …". Flashcards button hidden |

- **Responsive:** sticky `top:0` on desktop. At ≤1100px it moves above the content, static, as a 2-column card (thumbnail spans 3 rows, `min-height:220px`). At ≤700px it becomes block.

### C24 · Course Stat Chip
- **Purpose:** Quick course facts.
- **Where used:** overview header ("4h 12m · Total duration", "22 · Lessons", "6 · Modules").
- **Implementation:** `.stat` (`course-overview.html:106-110`). Class **B**.
- **Visual:**
  - `display:flex; gap:10px; padding:10px 14px; background:#fff; border:1px solid #e5e5e5; border-radius:12px`.
  - Icon `18px #a3a3a3`.
  - Value `15px/700` tabular, label `12.5px #a3a3a3`.
  - Row `gap:10px; margin-top:22px`, wrapping.

### C25 · Next Session Block
- **Purpose:** The single emphasized "what's next" live session.
- **Where used:** live-sessions Upcoming tab (`live-sessions.html:111-122`).
- **Implementation:** `section.next`. Class **B**.
- **Structure:**
  1. Date tile (C51; `.today` when the session is today).
  2. Uppercase label ("NEXT SESSION", or the status C48 when live or soon) → H2 link `20px/700` → "Course · Instructor" → facts row ("**Today · 5:05 PM–6:35 PM**", clock + duration, video/pin + where).
  3. Right-aligned CTA column + small caption.
- **Visual:**
  - Grid `auto | 1fr | auto`, `gap:18px 22px; padding:22px 24px`, radius 12, `margin-bottom:28px`.
  - `.is-live` border `#bbf7d0`.
- **CTA logic:**

  | Session | Button | Caption |
  |---|---|---|
  | Online, joinable | primary lg "Join session" | "Starts in N min" / "Started N min ago" |
  | In-person, live | primary lg "Check in" (QR icon) | — |
  | Online, not open yet | disabled lg "Session starts at 5:05 PM" | "Join opens at 4:50 PM" |
  | In-person, upcoming | secondary lg "View location" | — |

- **Responsive:** at ≤760px the grid is `auto | 1fr` and the CTA spans full width.

### C26 · Certificate Card
- **Purpose:** Preview and act on one certificate.
- **Where used:** certificates grid (`certificates.html:95-113`).
- **Implementation:** `article.card`. Class **B**.
- **Structure:**
  1. `.stage` link (padding `18px 20px`, `#f5f5f5`, bottom border) containing the Certificate Document (C82).
  2. `.body` (padding `16px 18px 18px`): title link `15.5px/600` + template name `13px #a3a3a3` on the left, status pill (C49) on the right → dates list (`13.5px #525252`; "Issued **date**", then "Valid until …", "Expired on …" in `#a16207`, or "Revoked on …" in red) → `.dl-slot` (C84) → actions (`margin-top:auto; padding-top:16px`): primary "View certificate" (`flex:1`) + secondary "⬇ Download".
- **Variants:** Valid. Expired/Revoked: `.is-muted` sets the document `opacity:.72`.
- **Interaction:**
  - Hover: border `#a3a3a3`.
  - Download shows the busy spinner "Preparing…" for 700 ms, then downloads the PDF, then shows the "Certificate downloaded" toast.
- **Order:** valid (newest first) → expired → revoked.

---

## 10. Tables & Lists

### C27 · Data Table (Assignments)
- **Purpose:** Scan a list of work items with status and grade.
- **Where used:** assignments (`assignments.html:73-100`).
- **Implementation:** `table-layout:fixed` inside `.table-wrap`. The file says "Table — library pattern (Gray header cell, bordered rows)". Class **C** (library Table plus Learner responsive-to-cards behavior).
- **Structure:**
  - Columns: Assignment (title link `15px/600` + course `13.5px #a3a3a3`) | Due ("Due Sep 24" bold + relative line) | Status (C48 + sub line) | Grade ("84 / 100" or a `—` in `#d4d4d4`) | Action (C17, right-aligned, `width:200px`).
  - Column widths: due 17%, status 18%, grade 11%.
- **Visual:**
  - Wrapper white, radius 12, `overflow:hidden`.
  - `thead th`: `#f5f5f5` background, `12.5px/600 #525252`, `padding:11px 20px`, bottom border.
  - `td`: `padding:16px 20px`, `14px`, vertically centered.
  - Rows have a top border `#e5e5e5` (none on the first).
- **States:**
  - Row hover `#fafafa`, and the title turns brand color.
  - The whole row is clickable (`tr[data-href]`; clicks not on a link navigate).
  - Relative due text:
    - "Today" / "Tomorrow" / "In N days"
    - "N days overdue" in red `500`
    - "Submitted Sep 21" once submitted
  - Status sub lines: "Open until Sep 27" (overdue), "Submission closed" (closed).
  - Loading: 5 `.sk-row` skeleton rows. Empty and filtered-empty messages go in `.empty` inside the wrapper.
- **Sort:** overdue-open → in-progress/to-do (soonest first) → grading/submitted → graded (latest first) → closed.
- **Responsive:**
  - ≤1100px: the Grade column is hidden and the grade shows inline under the status; action column 176px.
  - ≤760px: **rows become stacked cards**. The table/thead are hidden and each `tr` becomes a white r12 card (`padding:14px 16px 6px; margin-bottom:10px`) laid out as a grid: title spans full width; due (left) and status (right, right-aligned); action full width under a `1px #f5f5f5` divider. The due and relative text join on one line with " · ".

### C28 · Rubric Table
- **Purpose:** Marking breakdown for a graded assignment.
- **Where used:** assignment-detail graded result (`assignment-detail.html:226-233`).
- **Implementation:** `.rubric-wrap` / `table.rubric`. Class **A** (library Table).
- **Structure:** Criterion (name + `12.5px` description) | Points (right-aligned, tabular, "36 / 40"), with a `tfoot` "Total" row (`700`, `#fafafa`).
- **Visual:**
  - Wrapper r8, bordered.
  - `th` `#f5f5f5`, `12.5px/600`, `padding:9px 14px`.
  - `td` `padding:11px 14px`, top border.
- **Visibility:** shown only when the assignment's result visibility is `feedback`.

### C29 · Session Row List (grouped)
- **Purpose:** Chronological sessions grouped by day (upcoming) or month (past).
- **Where used:** live-sessions List view (`live-sessions.html:124-149`).
- **Implementation:** CSS-grid rows in `.rows` (a table-like list without `<table>`). Class **C**.
- **Structure:**
  - Group: `h3` label (`13px/700 #525252`, e.g. "Today", "Tomorrow", "Fri, Sep 25", "September 2026"), then the `.rows` container.
  - **Upcoming row:** grid `96px | 1.6fr | 1fr | 150px | 170px`, containing:
    - time ("**1:30 PM**" / "1 hr")
    - title + course
    - where (video icon "Online · Zoom", or pin + room)
    - status (C48)
    - action (primary "Join session" h36, secondary "Check in", or quiet link "View details →")
  - **Past row:** grid `1.6fr | 150px | 1fr | 130px | 250px`, containing title+course | date | instructor | attendance ("Present" / "Late" / "Absent" in red / `—`) | links ("▶ Watch recording", "View materials").
  - Past rows have a header strip `.th` in `#f5f5f5`, `12.5px/600`, `padding:11px 20px`.
- **Visual:** rows `padding:16px 20px; gap:16px`, top border, hover `#fafafa`, title hover brand. Cancelled rows show the title in `#a3a3a3` struck through.
- **Interaction:** the whole row is clickable to the detail page. Only actions that exist are rendered ("never empty buttons").
- **Responsive:**
  - ≤1180px: the status column is removed and the status shows inline under the title. The past-row instructor column is removed.
  - ≤760px: rows become stacked cards like C27 (r12, `padding:14px 16px`, `margin-bottom:10px`). Time and duration join with " · ", and the action goes full width under a divider.

### C30 · Coming Up List Row
- **Purpose:** Combined next-due work and sessions (max 4).
- **Where used:** dashboard "Coming up" (`dashboard.html:74-81`).
- **Implementation:** `.list > li > a.up`. Class **B**.
- **Structure:** Date tile (C51, 44px compact variant) | title (`15px/600`, ellipsis) + meta (`13.5px #525252`, e.g. "Today · 1:30 PM · Live on Zoom", "<red>Overdue</red> · submit by Sep 27") | 16px chevron.
- **Visual:** list `padding:6px`. Row grid `44px | 1fr | 16px; gap:14px; padding:10px; border-radius:12px`.
- **States:** hover `#fafafa` with the title in brand. Overdue shows a red date tile.

### C31 · Due Soon List Item
- **Purpose:** Mandatory courses with deadlines, soonest or overdue first (max 4).
- **Where used:** my-courses "Due soon · Mandatory" panel (`my-courses.html:96-114`).
- **Implementation:** `.due-item`. Class **B**.
- **Structure:** Date tile (48×52 variant) | title (`14px/600`) + relative text (`12.5px #a3a3a3`: "Due in 7 days", "Overdue by 5 days" in red `600`) | 36px progress ring (C47).
- **Visual:** panel `padding:18px 20px 10px`, radius 16. Row `padding:12px 10px; margin:0 -10px; border-radius:8px`, with a `1px #f0f0f0` separator between rows.
- **States:** hover `#fafafa`. `.is-overdue` gives the tile an `#fef2f2` background with red text.

### C32 · Definition Facts List
- **Purpose:** Label → value facts.
- **Where used:**
  - overview side card `.dl`
  - assignment summary `dl`
  - certificate "Details" `.facts`
  - live "When & where" `.facts` (icon list variant)
  - coach plan stats and revision-notes summary (stat-grid variants)
- **Implementation:** Class **E**.
- **Visual:**
  - `display:grid; grid-template-columns:auto 1fr; gap:10px 16px; font-size:13.5–14px`.
  - `dt` `#a3a3a3`. `dd` right-aligned `600 #404040`, tabular.
  - Status colors: `.overdue` / `.late` / `.bad` red, `.warn` `#a16207`.
  - Small sub-lines (`dd small` `12.5px #a3a3a3`, red when late).
- **Icon variant (live):** `ul.facts` with an 18px `#a3a3a3` icon, text `14px #404040`, and a `12.5px` sub-line ("Opens in Zoom when you join", "Instructor").

### C33 · File Item Row
- **Purpose:** Show an attached, uploaded or downloadable file.
- **Where used:** assignment materials, uploads and submitted files; live session materials.
- **Implementation:** `.file` (`assignment-detail.html:132-150`, `live-session-detail.html:177-184`). The file says "library File Dropper · uploaded file item". Class **C**.
- **Structure:** 34×34 r6 `#f5f5f5` icon tile (file, zip or image icon by extension) | name (`14.5px/600`, ellipsis) + meta ("PDF · 412 KB") | actions (`.ib`).
- **Visual:** `display:flex; gap:12px; padding:10px 12px 10px 14px; border:1px solid #e5e5e5; border-radius:8px; background:#fff`. List gap `8px`.
- **States:**
  - **Default (download):** "⬇ Download" label.
  - **Uploading:** border `#e0e7ff`; meta "Uploading… 42% of 1.2 MB"; 4px bar (C46) with `role=progressbar`; action "✕" to cancel.
  - **Done:** "Replace" (swap icon) and 🗑 remove (`.danger`).
  - **Error:** border `#fecaca`, bg `#fef2f2`, icon tile white with a red alert icon, meta red `500`. Errors include:
    - "PDF files aren't accepted. Upload PDF, DOCX, images or ZIP."
    - "File exceeds maximum size of 25 MB. Compress or split your file"
    - "Upload failed — the connection dropped at 60%. Try again." (+ "↻ Retry")
- **Responsive:** at ≤640px the text labels on `.ib` buttons are hidden and only icons show.

### C34 · Previous Attempts Disclosure
- **Purpose:** Earlier assignment attempts, each expandable.
- **Where used:** assignment-detail (`assignment-detail.html:243-252`).
- **Implementation:** native `<details>/<summary>` inside `ul.attempts`. Class **B**.
- **Visual:**
  - List r8, bordered, with `1px` separators.
  - Summary `padding:12px 14px; 14px`: chevron (rotates 90° when open) + "**Attempt 1**" + date in `#a3a3a3` + right-aligned score ("84 / 100" or "Not graded yet").
  - Inner `padding:4px 14px 14px` shows the submitted block.

---

## 11. Tabs

### C35 · Segmented Tabs
- **Purpose:** Filter a list or switch a view in place. Never used for page navigation.
- **Where used:**

  | Page | Type | Options |
  |---|---|---|
  | my-courses | filter | Active · In progress · Not started · Completed (with counts) |
  | assignments | filter | All · To do · Submitted · Graded · Overdue (with counts) |
  | live-sessions | filter | Upcoming · Past (with counts) |
  | live-sessions | view toggle | ☰ List · 📅 Calendar (`aria-pressed`) |
  | course-player | panel switch | 📄 Transcript · ✦ AI Tutor (narrow widths only) |

- **Implementation:** `.tabs/.tab`, `.status-tabs/.status-tab`, `.lower-tabs/.lower-tab`. Hand-built and approved (`MISSING_COMPONENTS.md`: "No Tabs group in library"). Class **B**; the same pattern is reused by Course Designer (see §30).
- **Visual:**
  - Track: `display:flex; gap:4px; padding:4px; background:#e5e5e5 (surface-overlay); border-radius:8px; width:max-content; max-width:100%; overflow-x:auto` with the scrollbar hidden.
  - Tab: `height:34px` (36 in the player); `padding:0 14px` (16 in the player); `border-radius:6px`; transparent; `14px/600` (13.5 on my-courses); `#525252`; hover `#171717`.
  - Selected: `background:#fff; color:#171717; box-shadow:0 1px 3px rgba(23,23,17,.1)`.
  - Count: `margin-left:6px; #a3a3a3`, tabular.
  - Icons: 16px (view toggle and player).
- **States / ARIA:**
  - Filter tabs use `role="tablist"`/`role="tab"` + `aria-selected`.
  - my-courses additionally toggles an `.active` class.
  - The view toggle uses `role="group"` + `aria-pressed`.
- **Interaction:**
  - Click re-renders the list client-side.
  - Counts reflect the whole dataset, not the search.
  - In live-sessions the Upcoming/Past tabs are hidden while in Calendar view.
  - In the player the tabs show only below the 880px container width; above it both panels are visible side by side.
  - Default tabs: my-courses "Active", assignments "All", live "Upcoming".

### C36 · Calendar View Switch
- **Purpose:** Choose Day / Week / Month in the calendar.
- **Where used:** live-sessions Calendar (`live-sessions.html:161-164`).
- **Implementation:** `.view-switch/.view-switch-btn`. The file says "same pattern as designs/instructor/code/live-sessions-overview.html". Class **D**.
- **Visual:**
  - Track: `background:#f5f5f5; border:1px solid #e5e5e5; border-radius:8px; padding:2px; gap:2px`. Lighter than C35, which uses a `#e5e5e5` track.
  - Button: `12.5px/600 #525252; padding:6px 14px; border-radius:6px`.
  - Pressed: white with `0 1px 2px rgba(23,23,23,.08)`.
- **Responsive:** at ≤760px only Day and Month are offered, and Week is forced to Day.

---

## 12. Forms & Inputs

**Form convention:**
- Inputs are `#fff`, `1px #e5e5e5`, radius 8, text `14–15px #171717`, placeholder `#a3a3a3`.
- **Focus:** `border-color:#6366f1` + `box-shadow:0 0 0 3px rgba(99,102,241,.15)`. The top-bar search is the exception: border only.
- Labels sit above the field, `13.5–14.5px`, `500–600`, `#404040` or `#171717`.
- Optional fields carry an inline "(optional)" in `400 #a3a3a3`.
- There is **no inline field-level validation copy**. Validation shows as an Alert (C73) above the form area, or as an error state on a file row.

### C37 · Search Field
- **Purpose:** Filter the current list by text.
- **Where used:**
  - my-courses page header (360px): title match
  - assignments page header (340px): title + course
  - live-sessions toolbar (240px, full width ≤760px): title + course + instructor
  - top bar (240px, decorative)
- **Implementation:** `label.search` / `.search-input-wrap` + `input[type=search]`. Class **C** (library Input + leading icon).
- **Visual:**
  - Height `42px` (36 in the top bar).
  - `padding:0 12px 0 36–38px`, radius 8, `14px`.
  - Leading `16px #a3a3a3` search icon at `left:11–12px` with `pointer-events:none`.
  - Focus ring as in the form convention above.
- **Interaction:**
  - Filters live on `input`: trim + lowercase `indexOf`.
  - There is no clear button beyond the native type=search one.
  - my-courses hides the Continue/Due-soon top band while a query is present, and shows "No matching courses found. Try a different search." if nothing matches.

### C38 · Select
- **Purpose:** Choose a filter, sort or generation option.
- **Where used:**
  - my-courses "All types / Mandatory / Optional" and "Last accessed / Deadline / Title (A–Z)"
  - live-sessions "All types / Online / In-person"
  - flashcards dialog "Number of cards" (8/12/16/20)
- **Implementation:** native `<select>` with `appearance:none` and an inline SVG chevron background. Files cite "Select" from the library. Class **A**.
- **Visual:**
  - Toolbar select: `height:42px; padding:0 30–32px 0 12px; border:1px solid #e5e5e5; border-radius:8px; #fff`, text `13–14px` `500–600` `#525252`/`#404040`, 13–14px chevron in `#525252` at `right 10–11px`.
  - Form select (`.fc-in`): height 44, `15px`, `box-shadow:0 1px 2px rgba(10,10,10,.04)`, chevron `#a3a3a3`.
- **Interaction:** `change` re-renders.

### C39 · Text / URL / Date Input
- **Purpose:** Single-line entry.
- **Where used:**
  - flashcards "What should these flashcards focus on? (optional)" (`maxlength=120`, placeholder "e.g. hashing and trees")
  - rich-text link URL row (`type=url`, placeholder `https://`)
  - coach study-plan `input[type=date]` ("Exam date" / "Finish by")
- **Implementation:** Class **A** (library Input).
- **Visual:**
  - `.fc-in` height 44, radius 8, padding `0 12px`, `15px`.
  - Link input height 34, radius 6.
  - Date field height 38, `14px`, with the label stacked above (`13px/500`).
- **States:** the date input is disabled after the plan is saved.

### C40 · Textarea
- **Purpose:** Multi-line optional prompt.
- **Where used:** revision-notes "Anything specific you want to focus on? (optional)" (`maxlength=300`).
- **Implementation:** `.textarea` (`revision-notes.html:118-120`). Class **A**.
- **Visual:** `min-height:96px; padding:12px 14px; border-radius:8px; 15px/1.5; resize:vertical; box-shadow:0 1px 2px rgba(10,10,10,.04)`, with the standard focus ring.
- **Interaction:** paired with toggle chips (C44 variant) that write the selected terms into the textarea.

### C41 · Rich Text Editor
- **Purpose:** Written assignment response.
- **Where used:** assignment-detail submission (`assignment-detail.html:156-174, 618-666`).
- **Implementation:** `contenteditable` + `document.execCommand`. Hand-built, approved ("Library has Textarea input field only"). Class **B**.
- **Structure:**
  1. `.rte-bar` toolbar (`role=toolbar`): Bold, Italic | Bulleted list, Numbered list | Link.
  2. Optional `.rte-link` row (URL input + "Add link").
  3. `.rte-area` (`role=textbox`, placeholder "Write your response…").
  4. `.rte-foot` word count ("128 words").
- **Visual:**
  - Container `1px #e5e5e5`, radius 8, focus-within ring.
  - Toolbar `padding:6px; gap:2px`, bottom border `#f5f5f5`.
  - Toolbar buttons 32×32 r6, `#525252`, hover `#f5f5f5`; pressed `#eef2ff` / `#4f46e5`.
  - Separators `1×20px #e5e5e5`.
  - Area `min-height:180px; max-height:460px; padding:14px 16px; 15px/1.65`.
  - Foot right-aligned `12.5px #a3a3a3`, tabular.
- **Interaction:**
  - Toolbar buttons prevent `mousedown` so the selection isn't lost, and pressed state syncs from `queryCommandState`.
  - Paste inserts **plain text only**.
  - Link: the selection is saved on blur; Enter applies and Escape closes. A missing scheme gets `https://`.
  - Every input schedules an auto-save (C53).
  - The output is sanitized to `b/strong/i/em/u/ul/ol/li/p/br/a/div` with http(s) hrefs only.
- **Label row:** "Written response" with the right-aligned hint "Optional if you upload files".

### C42 · File Dropper
- **Purpose:** Upload assignment files.
- **Where used:** assignment-detail submission (`assignment-detail.html:176-184`).
- **Implementation:** `.drop` (`role=button`, `tabindex=0`) + hidden `<input type=file multiple accept=".pdf,.docx,.doc,.png,.jpg,.jpeg,.gif,.webp,.zip">`. The file says "File Dropper — library (dashed #4f46e5 on #eef2ff, r8)". Class **A**.
- **Visual:**
  - `display:flex; gap:14px; padding:16px 18px; border:1.5px dashed #4f46e5; border-radius:8px; background:#eef2ff`.
  - Icon: 40px white circle with a brand upload icon (20px).
  - Title "Drop files here or <u>browse</u>" `15px/500`, with "browse" in brand.
  - Sub "Format: PDF, DOCX, images or ZIP · Max file size: 25 MB" `13.5px #525252`.
- **States:** hover and `.over` (dragenter/dragover) → background `#e0e7ff`.
- **Interaction:**
  - Click, Enter or Space opens the picker.
  - Drag-drop adds files.
  - Each file is validated for type and 25 MB size, then gets a File Item Row (C33) with a simulated progress upload.
  - Field label: "Files" + hint "PDF, DOCX, images or ZIP · up to 25 MB each".

### C43 · Chat Composer
- **Purpose:** Enter a question for an AI surface.
- **Where used:**
  - player AI Tutor
  - overview side sheet (`.composer-box`) and dock row (`.ai-row`, a borderless variant)
  - coach (large variant)
- **Implementation:** `.composer-box` = auto-growing `<textarea rows=1>` + `.send` (C19). Hand-built, approved ("compose from Textarea input field + Buttons"). Class **B**.
- **Visual:**
  - `display:flex; align-items:flex-end; gap:8px; padding:6px 6px 6px 14px; border:1px solid #e5e5e5; border-radius:12px; #fff`, with the focus-within ring.
  - Textarea borderless, `15px/1.5`, `max-height:132–160px`.
  - **Coach variant:** padding `8px 8px 8px 16px`, **radius 16**, `box-shadow:0 2px 8px rgba(10,10,10,.04)`, `min-height:56px` when the stage is empty, `15.5px`.
  - Helper line `12px #a3a3a3`:
    - "Enter to send · Shift + Enter for a new line" (player)
    - "Answers come from your courses and progress. Check important details against the lesson." (coach, centered)
- **Interaction:**
  - Enter submits (`requestSubmit`), and Shift+Enter adds a newline (IME composition is respected).
  - Auto-height on input.
  - Send is disabled while empty or busy.
  - The input clears after sending.

### C44 · Suggestion / Prompt Chips
- **Purpose:** One-click starter prompts or term picks.
- **Where used:**
  - player tutor intro ("Explain in-order traversal", …)
  - overview dock and sheet ("What will I learn?", "How long does it take?", "Are there prerequisites?")
  - coach (`.sugg`, with icons: "Set a learning goal", "Create a study plan", "Plan my revision", "Improve my study routine"; and in-answer `.chips` links)
  - revision-notes focus-term toggles
- **Implementation:** `.suggest button`, `.sugg button`, `.chips a/button`. Class **B**.
- **Visual:**
  - `border:1px solid #e5e5e5; background:#fff; border-radius:999px; padding:7px 12px` (coach `8px 14px`; revision-notes `height:30px; padding:0 11px`).
  - Text `13–14px/500 #404040`.
  - Hover or `aria-pressed="true"`: `border-color:#e0e7ff; background:#eef2ff; color:#4f46e5`.
  - Coach chip icons 15px `#a3a3a3`, turning brand on hover.
- **Interaction:** click sends the chip text as a message. On revision notes a click toggles the term and writes it into the textarea.

---

## 13. Filters & Search

### C45 · Filter Toolbar
- **Purpose:** Hold the list filters in one row.
- **Where used:** my-courses (`.toolbar`), live-sessions (`.toolbar`), assignments (tabs only, no toolbar wrapper).
- **Implementation:** Class **E**.
- **Structure:**
  - my-courses: Segmented status tabs (C35) → `.toolbar-spacer{flex:1}` → Type select → Sort select.
  - live-sessions: Upcoming/Past tabs → spacer → Search → Type select → List/Calendar view toggle.
- **Visual:** `display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:20–22px`. Assignments tabs use `margin-bottom:16px`.
- **Interaction pattern (I01):**
  - Filters apply instantly, client-side. There is no "Apply" button, no filter drawer, no chips of active filters, and no "Clear filters" button.
  - A filtered-empty result shows a C103 variant with guidance ("Try another status or clear the search.", "Try another type or clear the search.").
- **Responsive:** at ≤700–760px the spacer is hidden and items wrap. Live search goes to the end at full width (`order:5`).

---

## 14. Progress & Status Components

### C46 · Linear Progress Bar
- **Purpose:** Show completion as a fraction.
- **Where used:**
  - course card (6px), my-courses hero (6px)
  - dashboard hero (8px), overview side card (8px)
  - player header (8px, 140px wide) and rail (8px)
  - flashcards session (8px)
  - upload rows (4px)
- **Implementation:** `.progress-bar-bg > .progress-bar-fill` / `.bar > i`. Files cite "Progress bar — library pattern". Class **A**.
- **Visual:**
  - Track `#e5e5e5`, fill `#4f46e5`, `border-radius:999px`, `overflow:hidden`.
  - The fill animates `width .4s cubic-bezier(.2,.7,.2,1)` in the player and `.25s` in flashcards.
- **Labels:** paired with a text row: "Progress **68%**", "68% complete · due Sep 30 … **14 / 21 lessons**", "14 of 22 lessons **64%**", "Card 4 of 12". Numbers are bold and tabular.
- **ARIA:** `role="progressbar"` with `aria-valuenow/min/max` on the dashboard, upload rows and flashcards.

### C47 · Progress Ring
- **Purpose:** Compact circular percentage.
- **Where used:**
  - my-courses Due-soon rows (36px, stroke 3.5, brand)
  - revision-notes "Your results" (56px, stroke 6, **warning `#ca8a04`** stroke on a `#f0f0f0` track)
- **Implementation:** inline SVG with `stroke-dasharray`/`dashoffset`, rotated −90°. Class **B**.
- **Visual:** centre text `9.5px/700 #525252` (36px ring). Track `#e5e5e5` (36px) or `#f0f0f0` (56px).

### C48 · Status Dot Label
- **Purpose:** Restrained status indicator: text plus a dot, no fill. The file comment says "color only where it carries meaning".
- **Where used:** assignments table, assignment summary, live-session rows / next block / detail header.
- **Implementation:** `.status` with `<i>`. Files cite "Badge (dot)". Class **C** (library Badge-dot, rendered without a pill background).
- **Visual:** `inline-flex; gap:7px; 13.5–14px/500–600; color:#404040` (assignments) or `#525252` (live). The dot is `7–8px`.
- **Assignment vocabulary:**

  | State | Dot | Text color | Label |
  |---|---|---|---|
  | todo | hollow ring (`inset 0 0 0 1.5px #a3a3a3`) | default | To do |
  | in-progress | `#4f46e5` | default | In progress |
  | submitted / grading | `#a3a3a3` | default | Submitted / Grading in progress |
  | graded | `#15803d` | default | Graded |
  | overdue / closed | `#dc2626` | red | Overdue (sub: "Open until …" / "Submission closed") |
  | resubmitting (detail only) | brand | default | Resubmitting |

- **Live session vocabulary:**

  | State | Dot | Text | Label |
  |---|---|---|---|
  | upcoming | hollow ring | `#525252` | Upcoming |
  | soon | brand | brand | Starting soon |
  | live | `#15803d` + **pulse** (`box-shadow` 0→6px ring, 1.6s infinite) | green | Live now |
  | completed | `#a3a3a3` | `#525252` | Completed |
  | cancelled / not-started | red | red | Cancelled / Not started |

### C49 · Badge / Status Pill
- **Purpose:** Filled soft label for category or status.
- **Where used:**
  - overview header badges
  - revision-notes eyebrow badges ("✓ Module completed", "🔒 Not completed yet")
  - certificate status pills
- **Implementation:** `.badge.{brand|gray|warning|error|success}` (`course-overview.html:84-90`), `.pill.{valid|expired|revoked}` (`certificates.html:71-75`). The file says "Badge — library pattern (sm; Brand / Gray / Warning / Error / Success)". Class **A**.
- **Visual:**
  - `inline-flex; gap:6px; height:24px` (26 on revision notes); `padding:0 9–10px; border-radius:999px; 12–12.5px/600`.
  - Optional 6px `currentColor` dot, or a 13px icon.
- **Colors:**

  | Variant | Background / text |
  |---|---|
  | brand | `#eef2ff` / `#4f46e5` (course tag, "● In progress") |
  | gray | `#f5f5f5` / `#525252` ("Optional") |
  | warning | `#fefce8` / `#ca8a04` ("Mandatory") |
  | error | `#fef2f2` / `#dc2626` ("● Overdue") |
  | success | `#f0fdf4` / `#15803d` ("● Completed") |
  | Certificate valid | `#f0fdf4` / `#15803d` |
  | Certificate expired | `#fefce8` / **`#a16207`**. This darker amber isn't a DS token; the comment says it "matches admin Issued certificates table" |
  | Certificate revoked | `#fef2f2` / `#dc2626` |

- **Overview badge logic:** tag (brand) + (Completed success | Mandatory warning | Optional gray) + (In progress brand-dot) + (Overdue error-dot).

### C50 · Lesson Status Icon Set
- **Purpose:** Per-lesson state glyph.
- **Where used:** player rail, overview outline, overview prerequisites, revision-notes lesson list.
- **Implementation:** inline SVG constants `I.check/I.progress/I.todo/I.lock` + the `.eq` equalizer (`course-player.html:257-261, 501-504`). Class **B**.
- **Visual (all 20×20):**
  - **completed:** filled green `#15803d` circle with a white check.
  - **in-progress:** `#e0e7ff` ring with a brand quarter-arc.
  - **not started:** `#d4d4d4` hollow ring (1.8 stroke).
  - **locked:** `#a3a3a3` lock icon.
  - **active/now playing:** a 3-bar brand equalizer (3×12px bars, `scaleY` .4↔1 animation, paused when the video is paused).
- Revision notes uses an 18px green disc with a 10px check.

### C51 · Date Tile
- **Purpose:** Calendar-date glyph (month + day).
- **Where used:** dashboard Coming-up, my-courses Due-soon, live-sessions Next block, live-session detail side card, coach plan days.
- **Implementation:** Hand-built, approved ("Date tile (month + day block)"). Class **B**, with 4 size variants:

  | Where | Size | Style |
  |---|---|---|
  | Dashboard `.tile` | 44 wide, `padding:5px 0` | **bordered white** (`1px #e5e5e5`, r8); month `11px/600` uppercase `#a3a3a3`; day `15px/700`; `.late` → `#fef2f2` bg, `#fecaca` border, red text |
  | My-courses `.due-date` | 48×52 | **filled** `#f5f5f5` r8; month `10.5px/700` uppercase `.04em`; day `19px/700` tabular; overdue → `#fef2f2` + red |
  | Live `.tile` | 56×60 | filled `#f5f5f5` r8; month `11px/700` uppercase `.05em`; day `22px/700`; `.today` → `#eef2ff` + brand text |
  | Coach `.tile` | 52 wide, bordered | weekday on top (`12px/600 #a3a3a3`), date below (`14px/700`); `.word` variant for "Mon"/"Due" labels |

### C52 · Image Overlay Tags
- **Purpose:** Labels layered on course imagery.
- **Where used:** course card, dashboard hero, my-courses hero.
- **Implementation:** `.course-photo-tag`, `.thumb .tag`, `.check-badge`, `.play`. Class **B**.
- **Visual:**
  - Photo tag: `11.5px/600` white on `rgba(15,15,15,.5)` + `backdrop-filter:blur(8px)`, `padding:4px 10px`, r6, at `left:12px; top:12px`.
  - Hero tag (dashboard): white pill `rgba(255,255,255,.92)`, 26px, `12.5px/600 #404040`.
  - Completed check badge: 28px green circle, 15px white check, `box-shadow:0 0 0 2px rgba(255,255,255,.9)`, at `top:12px; right:12px`.
  - Play button: 52px white circle, brand icon (C22).

### C53 · Draft Save Indicator
- **Purpose:** Reassure the learner that their work is saved.
- **Where used:** assignment-detail submission footer (`assignment-detail.html:186-191`).
- **Implementation:** `.saved` with `aria-live="polite"`. Class **B**.
- **Visual and states:**

  | State | Text | Style |
  |---|---|---|
  | Idle, never saved | "Your work saves automatically as a draft." | muted `13.5px` |
  | Saving | cloud icon + "Saving…" | icon tertiary |
  | Saved | cloud-check icon + "Draft saved · today at 7:12 PM" | icon green, text `#525252` |
  | Failed | alert icon + "Save failed — retrying." | text `#854d0e`, icon warning; retries after 2.2 s / 3 s |

- **Behavior:**
  - Debounced 900 ms after each edit, and forced at least every 30 s and on `pagehide`.
  - The manual "Save draft" button saves immediately and shows the toast "Draft saved".
  - Saving flips the status between To do and In progress in the side card.

---

## 15. Course Player Components

### C54 · Video Player
- **Purpose:** Lesson video with custom controls.
- **Where used:** course-player stage; live-session-detail recording (a reduced control set).
- **Implementation:** `.stage > .video` (`course-player.html:89-125`). The file says "Library … Video player (+ _Play button glassmorphism, _Video progress)". Playback is simulated with a clock ("swap for <video> in build"). Class **A**.
- **Structure:**
  1. Poster background.
  2. Bottom shade gradient (60% height, 0→.72 black).
  3. Full-size transparent hit button.
  4. Centre glass play button.
  5. Captions box.
  6. Controls: seek bar, then a row with Play/Pause · −10 s · +10 s · time "3:12 / 12:40" · spacer · speed "1×" · CC · Fullscreen.
- **Visual:**
  - Stage `#0b0b12`, radius 16 (12 at ≤640px).
  - Video 16:9 with `max-height:max(300px, 100dvh − 64px − 380px)` and a matching width cap, centred.
  - Glass play button: 80px circle, `rgba(255,255,255,.2)` + `backdrop-filter:blur(12px)` + `1px rgba(255,255,255,.35)` border, 30px icon. The recording uses 72px.
  - Seek:
    - Height 16 hit area; track 6px (8px on hover), `rgba(255,255,255,.28)`.
    - Buffer `.45` white; fill white.
    - 14px knob appears on hover or focus.
  - Controls C16 `.ctrl`, 20px icons.
  - Time `13px` tabular.
  - Captions: bottom 78px, `rgba(0,0,0,.66)`, r6, `clamp(14px,1.3vw,19px)`.
- **States:**
  - Playing: the big play button fades and scales to .85.
  - **Idle:** after 2.6 s of no pointer movement, controls and shade fade and the cursor hides.
  - Captions on or off.
  - Ended: End card (C55).
  - Non-video lesson: `.unavailable` overlay ("Quiz lesson — content renders here in the build.").
- **Interaction:**
  - Click the video, Space, or the play button toggles playback.
  - ←/→ seek ±5 s (the seek slider is keyboard-accessible).
  - Pointer-drag seeking.
  - Speed cycles 0.5→0.75→1→1.25→1.5→2.
  - The Fullscreen API is applied to the stage.
  - Position auto-saves to localStorage every tick (`FR-04: auto-save exact position`).
- **Responsive:** ≤1024px removes the height cap. ≤640px hides the ±10 s buttons (`.hide-sm`) and shrinks captions.

### C55 · Lesson End Card
- **Purpose:** Completion prompt when a video ends.
- **Where used:** player (`course-player.html:119-124`).
- **Implementation:** `.end-card` overlay. Class **B**.
- **Visual:**
  - `rgba(11,11,18,.78)` + `blur(6px)`, centred column `gap:10px`.
  - "Lesson complete" `13px` white at 70%.
  - "Up next: *title*" (or "Course complete") `20px/700`.
  - Buttons: secondary-on-dark "Replay" (transparent, `rgba(255,255,255,.35)` border) + primary "Next lesson" (hidden if this is the last lesson).
- **Behavior:** reaching the end marks the lesson `completed` and re-renders the rail.

### C56 · Lesson Head + Previous/Next
- **Purpose:** Current lesson title and sequential navigation.
- **Where used:** player below the video (`course-player.html:128-131`).
- **Implementation:** `.lesson-head`. Class **B**.
- **Structure:**
  - Left: eyebrow "Module 4 · Binary Trees · Lesson 3" (`13px/600` brand) → H1 `clamp(20px,1.7vw,26px)/700/-.4px`.
  - Right: secondary "‹ Previous" + primary "Next lesson ›".
- **States:** Previous is disabled on the first lesson, Next on the last (`opacity:.45`).
- **Interaction:** Next marks the current lesson completed (commented as a mock rule: "real rule comes from CDL-004") and autoplays the next one.
- **Responsive:** at ≤640px the labels are hidden and only chevrons show (`padding:0 12px`).

### C57 · Course Content Rail
- **Purpose:** Module and lesson navigation beside the player.
- **Where used:** player right rail (`course-player.html:213-224, 266-275`).
- **Implementation:** `aside.rail`, `--rail-w:384px`. Class **B**.
- **Structure:**
  - `.rail-head` (padding `18px 20px 16px`): "Course content" `16px/700` + close icon button (34px).
  - Progress row "14 of 22 lessons" / "**64%**" + 8px bar.
  - `.modules`: an accordion (C58) of lesson items (C59).
- **Visual:** background `#fff`, left border `#e5e5e5`.
- **Interaction:**
  - The header toggle collapses the grid column to `0` over `.3s`.
  - The current module is always expanded.
  - The active lesson is scrolled into view on load.
- **Responsive:** ≤1024px turns it into a fixed right drawer (`width:min(384px,92vw)`, `translateX(100%)` → 0, `box-shadow:-8px 0 32px rgba(0,0,0,.14)`, backdrop `rgba(15,23,42,.45)`). It closes after a lesson is chosen.

### C58 · Module Accordion
- **Purpose:** Expandable module rows.
- **Where used:** player rail (compact), overview "Course content" (large).
- **Implementation:** `.acc/.acc-btn/.acc-panel`, hand-built and approved. Class **B**.
- **Structure:** a button with a number tile, title + meta, and a chevron. The panel uses the grid-rows animation technique.
- **Visual:**

  | | Player | Overview |
  |---|---|---|
  | Button padding | `14px 20px` | `18px 20px` |
  | Number tile | 26px r6 | 32px r8 |
  | Title | `14.5px/600` | `16px/600` |
  | Meta | `12.5px #a3a3a3` "3/5 done · 42 min" | `13px` with dot separators "5 lessons · 42 min · 3/5 done" |
  | Container | rows separated by `#f0f0f0` | inside a white r16 outline card |

  - Number tile states: default `#f5f5f5 / #525252`; **done** `#f0fdf4 / #15803d` showing "✓"; **current** `#e0e7ff / #4f46e5`.
  - Chevron 18–20px `#a3a3a3`, rotating 180° when expanded (`.25s`).
  - Panel `grid-template-rows:0fr → 1fr` over `.3s cubic-bezier(.2,.7,.2,1)`.
- **Overview extras:**
  - Module description (`14.5px/1.6 #525252`, `max-width:72ch`).
  - Lessons list in a bordered r12 box.
  - Revision-notes row (C90).
  - Body indented `padding:0 20px 18px 66px` (16px at ≤700px).
- **Interaction:**
  - Click toggles `aria-expanded`.
  - Overview has "Expand all / Collapse all" (C17), and its label syncs to the state.
  - Default open: the current module, or the first module when not in progress.

### C59 · Lesson List Item
- **Purpose:** One lesson row.
- **Where used:** player rail (interactive button), overview outline (static `li`).
- **Implementation:** `.lesson` (`course-player.html:243-256`, `course-overview.html:139-151`). Class **B**.
- **Structure:**
  - Status icon (C50).
  - Title (`14px/500 #404040`; the overview uses `14.5px/600`).
  - Meta: type icon 13px + "Video · 13 min" [+ "· Done"].
  - The overview adds a right-aligned duration, a summary paragraph (`13.5px/1.55 #525252`), and a "Last accessed" tag (`11.5px/600`, brand on `#eef2ff`, pill).
- **States (player):**
  - Hover `#fafafa`.
  - **Active:** `#eef2ff` background + a 3px brand left bar (`::before`, inset 10px top and bottom), title `600 #171717`, equalizer icon.
  - **Locked:** `cursor:not-allowed`, no hover, title `#a3a3a3`, tooltip "Complete the previous lesson first" (C66).
- **Interaction:** click loads the lesson and autoplays. Locked and active items ignore clicks. Sequential locking applies when the course is `sequential:true` (FR-06).

### C60 · Transcript Panel
- **Purpose:** A timestamped transcript synced with playback.
- **Where used:** player lower area (`course-player.html:157-166`).
- **Implementation:** a panel (C61 shell) with `.transcript` of `button.cue`. Hand-built, approved. Class **B**.
- **Visual:**
  - Cue grid `48px | 1fr`, `gap:10px; padding:8px 10px; r8; 14.5px/1.55`.
  - Colors: default `#a3a3a3`; past `#525252`; **active** `#eef2ff` background, text `#171717`, timestamp brand.
  - Timestamp `12.5px/600` tabular.
- **Head:** "Transcript" + `.mini` toggle "↓ Auto-scroll" (on by default).
- **Interaction:**
  - Clicking a cue seeks there and plays.
  - With auto-scroll on, the active cue scrolls to one third of the panel height.
  - Captions mirror the active cue.
- **Empty:** "**No transcript for this lesson** Captions and a transcript weren't provided for this video." / "This lesson isn't a video."

### C61 · AI Tutor Panel (tool panel)
- **Purpose:** Lesson-scoped AI chat (AI-006).
- **Where used:** player lower area, alongside the transcript.
- **Implementation:** `section.panel` (`course-player.html:145-155`). Class **B**.
- **Structure:**
  - `.panel-head` (`min-height:62px; padding:14px 18px`): AI mark (C85, 30px) + "AI Tutor" `15px/700` + hint "Answers from this lesson only" (`12.5px #a3a3a3`) + `.mini` "Clear".
  - `.chat` (`padding:18px; gap:18px`) of messages (C62).
  - Composer (C43).
- **Visual:** panel `height:460px` (440 at ≤640px), white, r16, bordered.
- **Layout:** side by side with the transcript at a ≥880px container width (`@container`). Below that, both sit behind Segmented Tabs (C35).
- **States:**
  - **Intro (empty):** "Stuck on something in this lesson? Ask me — I'll explain it or guide you with a question." + 3 suggestion chips.
  - **Limited context** (no transcript): "This video has no transcript, so I have limited context here."
  - **Typing:** C63.
  - **Replies:** can include a Jump-to-timestamp chip (C65) and a Helpful rating (C64).
- **Guardrails in copy:**
  - Out of scope: "I can only help with content from this lesson. Try rephrasing your question about the topic".
  - Quiz answers are refused with a hint.
- **Persistence:** history persists per course.

### C62 · Chat Message
- **Purpose:** One chat turn.
- **Where used:** player tutor, overview side sheet, coach (sent-only).
- **Implementation:** `.msg` / `.msg.sent`. Files say "Message — library pattern (received #f5f5f5 w/ avatar, sent #e0e7ff 'You', writing dots)". Class **A**.
- **Visual:**
  - `display:flex; gap:12px; max-width:92–94%`, animated `rise` (6px, .3s).
  - Avatar 40px circle; the AI avatar is an SVG with a `#6366f1→#4338ca` gradient and a white sparkle.
  - Meta: name `14px/500 #404040` ("AI Tutor", "UpSpace AI", "You") + time `12px #525252`.
  - **Received bubble:** `#f5f5f5`, `padding:10px 14px`, `15px/1.55`, radius `0 8 8 8`.
  - **Sent bubble:** `#e0e7ff`, radius `8 0 8 8`, right-aligned, no avatar.
  - Coach sent (`.you`): the same sent bubble with max-width `min(560px,86%)`.

### C63 · Typing Indicator
- **Purpose:** Show that the AI is writing.
- **Where used:** player tutor, overview sheet.
- **Implementation:** `.typing` with 3 `<i>` (`role=status`, "AI Tutor is writing"). Class **A** (library Message "writing").
- **Visual:** bubble `#f5f5f5`, radius `0 8 8 8`, `padding:12px 10px`. Dots 4px, `#737373`/`#a3a3a3`, blinking and bouncing 2px, staggered .15 s.

### C64 · Helpful Rating
- **Purpose:** Thumbs feedback on AI output (AI-015 per the revision-notes comment).
- **Where used:** each AI reply (player, overview sheet), the overview dock answer head, the revision-notes document footer.
- **Implementation:** `.rate` group. Class **B**.
- **Visual:** "Helpful?" `12–12.5px #a3a3a3` + two 28–30px ghost buttons (thumbs up/down, 15px icons); `aria-pressed="true"` → `#eef2ff / #4f46e5`.
- **Interaction:**
  - Toggles: clicking the same rating again clears it, and the two are mutually exclusive.
  - Saved into the chat log.
  - Revision notes shows the toast "Thanks for the feedback".

### C65 · Jump-to-Timestamp Chip
- **Purpose:** Link an AI answer to a moment in the video.
- **Where used:** player tutor replies.
- **Implementation:** `.jump`. Class **B**.
- **Visual:** `inline-flex; gap:5px; margin-top:8px; 13px/600 #4f46e5; #fff; 1px #e0e7ff; r6; padding:4px 9px`, with a 12px play icon, e.g. "▶ Jump to 3:12". Hover `#eef2ff`.
- **Interaction:** seeks the video and plays. It is shown only when the reply belongs to the current lesson.

### C66 · Tooltip
- **Purpose:** Short explanatory hover text.
- **Where used:** player locked lessons (JS-positioned), revision-notes header icon buttons (CSS `::after`).
- **Implementation:** `.tip` (`course-player.html:264`) `role=tooltip`; `.icon-btn[data-tip]::after`. Files cite "Tooltip — library pattern". Class **A**.
- **Visual:** `#171717` background, white `12–12.5px/500`, `padding:5–6px 8–10px`, r6. The player adds `box-shadow:0 6px 16px rgba(0,0,0,.2)` and positions it 6px below the target.
- **Interaction:** hover only (mouseover). No focus trigger, no delay.

---

## 16. Assessment Components

**There is no Learner assessment-taking UI.** Nothing exists for an assessment list, cards, detail, instructions, questions, answer controls, navigation, submission, results, grading states or feedback for quizzes/exams (§2). What does exist:

### C67 · Non-video Lesson Placeholder (quiz/reading)
- **Purpose:** Stand-in content for quiz and reading lessons in the player.
- **Where used:** player stage when `lesson.type !== 'video'`.
- **Implementation:** `.unavailable` (`course-player.html:125, 604-607`). Class **B**.
- **Visual:** it covers the video area, `#111` background, centred text `15px`, white at 75%: "Quiz lesson — content renders here in the build." or "Reading lesson — …".

**Quiz as a lesson type:**
- Quiz lessons render in the outline and rail with the `circle-help` icon and the label "Quiz" (e.g. "Knowledge check", "Traversal practice", "Final assessment", with the overview summary "Covers every module. Pass mark 70%.").
- Assessment results show up indirectly in only two places:
  - Revision-notes "Your results" ring (C47), plus "Focus areas" built from quiz gaps (C93).
  - The dashboard and assignment grade blocks, which cover assignments, not quizzes.

**Adjacent, not Learner:** `MISSING_COMPONENTS.md` mentions a "learner question render (`course-preview.html` `.q` / `.opt`)" inside `designs/course-designer/code/course-preview.html`. It is a Course Designer preview of how learners would see questions. It was **not inspected** here. See §31.

---

## 17. Assignment Components

Page composition (assignment-detail, P4), main column in order:
1. Alerts (C73; overdue / closed)
2. Result (C69, or C71 when pending)
3. Instructions (`.card.section` + prose + "Assignment files" C33 list)
4. Submission: an editor (C41 + C42 + C53 + footer actions + C72 popover) or "Submitted work"
5. Previous attempts (C34)

The side column holds the Summary card (C68).

### C68 · Assignment Summary Side Card
- **Purpose:** Status, key facts and the primary action for one assignment.
- **Where used:** assignment-detail side (`assignment-detail.html:108-118`).
- **Implementation:** `.card.summary`. Class **B**.
- **Structure:**
  1. Status dot label (C48, 15px).
  2. `dl` facts (C32): Due ("Sep 24, 11:59 PM" + "Tomorrow" / "5 days overdue"), Points, Attempts ("1 allowed" / "1 of 2 used"), Submitted (+ "Late"), Grade.
  3. Actions grid (`gap:8px`, block **lg** buttons).
  4. Note `13px #525252`.
- **Action logic:**

  | Status | Actions | Note |
  |---|---|---|
  | To do / In progress / Overdue / Resubmitting | primary "Submit assignment" (scrolls to the editor and opens the confirmation popover) | Overdue: "Late submissions are accepted until … Your submission will be marked late." Resubmitting: "Attempt 2 of 2. Your latest score counts. Resubmissions close …" |
  | Closed | disabled span "🔒 Submission closed" | — |
  | Submitted / Grading / Graded | "View submission" (primary; secondary when resubmit is possible) [+ primary "Resubmit assignment"] | "1 of 2 attempts left. Resubmissions close … Your latest score counts." |

- **Responsive:** at ≤1100px the card moves above the content and becomes a 2-column grid (facts left in auto-fit columns, actions right). At ≤640px it becomes block.

### C69 · Grade Result Block
- **Purpose:** Released grade with pass/fail, feedback and breakdown.
- **Where used:** assignment-detail when graded (`assignment-detail.html:217-225`).
- **Implementation:** `.card.section#result`. Class **B**.
- **Structure:**
  1. H2 "Your grade".
  2. `.grade` row: `.score` "**84** / 100" (**44px/700**, `-1.2px`, tabular; "/ 100" `20px/600 #a3a3a3`) + meta "84% · **Passed** (green) / **Not passed** (red) · pass mark 70%<br>Graded by Prof. Vance on Sep 19 · Attempt 1".
  3. H3 "Instructor feedback" + C70 (or the C103 "No feedback has been released yet.").
  4. H3 "Marking breakdown" + C28 (only when visibility is `feedback`).
- **Responsive:** score is 38px at ≤640px.
- **Visibility variants:**
  - `feedback`: score + feedback + rubric.
  - `score`: score only, with a "No feedback has been released yet." empty block.
  - `hidden`: C71 "Results not released yet".

### C70 · Instructor Feedback Quote
- **Purpose:** Display the grader's comment.
- **Where used:** assignment-detail graded result.
- **Implementation:** `.feedback.prose`. Class **B**.
- **Visual:**
  - `padding:16px 18px; border-left:3px solid #e0e7ff; background:#fafafa; border-radius:0 8px 8px 0`.
  - Body is prose `15px/1.65 #404040`.
  - Byline "— Prof. Vance" `13px #a3a3a3`.
- **Related:** the same left-bar quote treatment appears as the coach `.answer` (white background) and the revision-notes `.examples li` (`3px` brand bar).

### C71 · Waiting / Pending State Block
- **Purpose:** Explain why a result isn't shown yet.
- **Where used:**
  - assignment grading ("Grading in progress — Your instructor is reviewing your submission. Your grade and feedback will appear here once grading is complete.")
  - assignment hidden results ("Results not released yet — Results will be available once released by your instructor.")
  - live recording processing / attendees-only (`.rec-state`)
- **Implementation:** `.waiting` / `.rec-state`. Class **B**.
- **Visual:** `display:flex; gap:14px`. A 40px `#f5f5f5` circle with a 20px `#525252` icon (clock, hourglass or lock), title `15px` bold, text `14px/1.5 #525252`.

### C72 · Submit Confirmation Popover
- **Purpose:** A lightweight "are you sure" with a summary before submitting.
- **Where used:** assignment-detail submission footer (`assignment-detail.html:195-204`).
- **Implementation:** `.pop` (`role=dialog`, `aria-modal=false`), anchored above the Submit button. The file says "Popover — library (white, #d4d4d4 border, r12, heading 16 bold)". Class **A**.
- **Structure:**
  1. H4 "Ready to submit?"
  2. Text "Your submission will be sent to your instructor for grading. [You can't edit it afterwards.]"
  3. `.sum` box: "**Written response** · 128 words / **2 files** · names", plus conditional lines "Files with errors won't be included." and a red "Will be marked late — it was due Sep 20."
  4. Row: secondary "Cancel" + primary "Submit assignment".
- **Visual:**
  - `position:absolute; right:0; bottom:calc(100% + 10px); width:min(360px,100%); border:1px solid #d4d4d4; border-radius:12px; padding:18px 18px 16px; box-shadow:0 12px 32px rgba(23,23,17,.10)`.
  - Arrow: a rotated 12px square at `right:52px`.
  - Animation `popIn` 4px .18s.
  - Summary box: `#fafafa`, r8, `13px/1.55`.
- **Pre-checks** (these show as Alerts instead of the popover):
  - Files still uploading → warning "**Files are still uploading.** Wait for uploads to finish, then submit."
  - Nothing to submit → warning "**Nothing to submit yet.** Write a response or upload at least one file." (focuses the editor).
- **Interaction:**
  - Focus moves to the Submit button.
  - Escape or an outside click closes it.
  - Submit enters the busy state (C15), then after 1.1 s re-renders as submitted, scrolls to the submission, and shows the toast "Assignment submitted".
  - **Failure** (`?state=submitfail`): the popover closes, the draft is saved, and an error Alert appears: "**Submission failed.** We couldn't reach the server, so nothing was sent. Your work is saved as a draft — try again." + "Try again".
- **Responsive:** full width at ≤640px, with the arrow at 22%.

### C73 · Alert
- **Purpose:** Inline contextual message at page or section level.
- **Where used:**
  - assignment-detail (overdue, closed, submit validation, submit failure)
  - live-session-detail (cancelled, not started, join failure)
  - certificate-detail (expired, revoked)
- **Implementation:** `.alert.{error|warning|expired|revoked}` (`assignment-detail.html:207-215`). The file says "Alerts — library, tinted by feedback family". Class **A**.
- **Visual:**
  - `display:flex; gap:12px; padding:14px 16px; border-radius:8px; border:1px solid #e5e5e5; #fff; 14px/1.5 #404040; flex-wrap:wrap`.
  - Icon 20px. Bold first line `600 #171717`.
  - **error:** `#fef2f2` + `#fecaca` border, red icon.
  - **warning / expired:** `#fefce8` + `#fef08a`, warning icon.
  - **revoked:** error colors.
  - An optional `.act` button aligns centre-right.
- **Copy pattern:** "**Headline.** One sentence on what it means and what you can still do." Examples:
  - "**Overdue — due Sep 20** You can still submit until Sep 27, 11:59 PM."
  - "**Expired on Mar 10, 2026** You can still view and download this certificate. Anyone who verifies it will see that it has expired."

---

## 18. Live Session Components

Detail page composition (P4):
- Main: Alerts (C73) → Recording (C76 / C71) → Location (C81) → "About this session" prose → "Session materials" (C33 list, `id=materials`).
- Side: When & Where card (C74).

### C74 · Session When & Where Card
- **Purpose:** Time, place, the join/check-in CTA, reminder and attendance.
- **Where used:** live-session-detail side (`live-session-detail.html:108-134`).
- **Implementation:** `.card.when`. Class **B**.
- **Structure:**
  1. `.when-top`: Date tile (C51, 56×60) + "**Today**" (`16px/700`) and "5:05 PM – 6:35 PM" (tabular).
  2. Facts list (C32 icon variant): duration; "Online · Zoom" + "Opens in Zoom when you join" (or "In-person · Room 4B" + address); instructor.
  3. `.cta` (top border `#f5f5f5`, `padding-top:18px`).
  4. `.reminder` box (`#fafafa`, r8, bell icon): "**Reminder set** 1 hour and 15 minutes before". Read-only; the comment says "No notification settings here".
  5. `.attend` row for past sessions: "Your attendance — **Present** / Late / Absent (red)".
- **CTA logic:**

  | Session | CTA | Hint |
  |---|---|---|
  | Online, soon or live | primary lg block "Join session" → busy "Joining…" → "Rejoin session" | "Starts in N min · you can join now" / green "Live now · started N min ago"; after joining, green "✓ You joined at 1:32 PM" |
  | Online, upcoming | disabled lg "Join session" | "Session starts at **5:05 PM** on Sep 25.<br>Join opens 15 minutes before." |
  | In-person, live, QR | primary "Check in" (QR icon) | green "Live now · scan the code shown in the room"; after check-in "✓ Checked in at …" |
  | In-person, upcoming | — | "Starts at **1:45 PM** in Room 4B.<br>You'll check in with the QR code shown in the room." |
  | Completed with recording | primary "▶ Watch recording" | — |

- **Join failure:** error Alert with the fallback link (C80) + secondary "Try again" (full width).

### C75 · Calendar (Day / Week / Month)
- **Purpose:** Time-grid view of sessions.
- **Where used:** live-sessions Calendar view (`live-sessions.html:151-204, 466-541`).
- **Implementation:** "same pattern as designs/instructor/code/live-sessions-overview.html (user request)". Class **D**.
- **Structure:**
  - Toolbar: "Today" (C18), prev/next cluster (C16), range label (`16px/600`, e.g. "Sun, Sep 20 – Sat, Sep 26" / "September 2026" / "Wed, Sep 23 (Today)"), spacer, view switch (C36).
  - `.cal-card` (r12): header row of day heads, then a scrolling time grid.
- **Time grid:**
  - 07:00–21:00, 48px per hour, 56px time column with `11px` labels.
  - Day columns with hour lines (`repeating-linear-gradient` on `#f5f5f5`).
  - Now-line: 2px `#dc2626` with an 8px dot.
  - Today's header: brand weekday + filled brand 32px circle date.
- **Events:** absolute blocks, `r6; padding:3px 7px; 11.5px/1.3`, time bold + title, laid out in lanes for overlaps. Colors map 4 states:

  | State | Background / text |
  |---|---|
  | upcoming | `#eff6ff` / `#1e3a8a` |
  | in-progress | `#15803d` / white |
  | completed | `#e5e5e5` / `#525252` |
  | cancelled | `#fef2f2` / red, struck through |

- **Month view:** 7-column grid, `min-height:96px` cells, date number top-right (today = 22px brand circle), up to 2 chips (`10.5px/600`, same colors, upcoming `#eff6ff/#2563eb`) + "+N more"; outside-month cells `#fafafa`.
- **Interaction:**
  - Clicking a day header or a month cell drills to Day view.
  - Events link to the detail page.
  - Enter/Space activate cells.
  - The grid re-renders on resize.
- **Responsive:** ≤760px offers Day and Month only; month cells shrink to 64px, and chips become 6px colored dots.

### C76 · Recording Offer & Inline Player
- **Purpose:** Watch a past session's recording.
- **Where used:** live-session-detail when the session is completed and has a recording (`live-session-detail.html:146-175`).
- **Implementation:** `.rec-offer` → `.stage` (Video player pattern, C54). Class **C**.
- **Structure:**
  - Head: "Session recording" + "58 min · Stream only".
  - Offer row: 160px 16:9 poster thumbnail + "**Available to watch** Recorded Sep 21 · 58 min" + secondary "▶ Watch recording".
  - Opening it swaps in an inline player (16:9, r8; play/pause, time, speed cycling 1/1.25/1.5/2/0.75, fullscreen).
- **States:**
  - available (offer or playing)
  - processing: C71 "Recording is being processed — available soon. It usually appears within 30 minutes of the session ending."
  - attendees-only: C71 "Available to attendees only …"
  - none: the section is omitted ("no recording → no section, no empty action")
- **Responsive:** ≤640px makes the thumbnail and button full width and hides fullscreen.

### C77 · QR Check-in Scanner Modal
- **Purpose:** In-app camera check-in for in-person sessions.
- **Where used:** live-session-detail (`live-session-detail.html:193-215, 474-495`).
- **Implementation:** a Modal (C99) + `.viewfinder`. Hand-built, approved. Class **B**.
- **Structure:**
  - H3 "Check in" + "Point your camera at the QR code on the screen at the front of the room."
  - Square viewfinder (`max-height:52vh`, r8, dark radial gradient) with 4 white corner brackets (28px, 3px), an animated brand scan line (`rgba(99,102,241,.9)` with glow, 1.8 s), and the caption "Looking for a code…".
  - Secondary "Cancel".
- **Result states (after 2.2 s):**
  - Success: Featured icon (C78, green) "You're checked in — Recorded at 1:46 PM for Design Critique Studio." + primary "Done".
  - Failure: Featured icon (red) "Couldn't check you in — You're not enrolled in this session's class." + secondary "Close".
- **Interaction:** Escape, the backdrop or Cancel closes it. Focus goes to Cancel on open and to Done/Close on result.

### C78 · Result Featured Icon
- **Purpose:** A large status glyph at the top of a result dialog.
- **Where used:** QR scanner result.
- **Implementation:** `.featured.ok|.bad`. Class **B**.
- **Visual:** 48px circle with a 24px icon and an 8px halo ring (`box-shadow:0 0 0 8px`). ok: `#dcfce7` / `#15803d` with an `#f0fdf4` halo. bad: `#fee2e2` / red with an `#fef2f2` halo. `margin:8px 0 18px 8px`.

### C79 · Reminder Note
- **Purpose:** Read-only confirmation of automatic reminders.
- **Where used:** live-session-detail When card.
- **Implementation:** `.reminder`. Class **B**.
- **Visual:** `display:flex; gap:10px; padding:12px 14px; border-radius:8px; background:#fafafa; 13.5px/1.45 #525252`; bell icon 17px `#a3a3a3`; bold line `#404040`.

### C80 · Meeting Link Fallback
- **Purpose:** Copyable meeting URL when the platform API fails (LSN-003-NFR-02).
- **Where used:** join-error Alert.
- **Implementation:** `.fallback`. Class **B**.
- **Visual:** `display:flex; gap:6px; padding:5px 5px 5px 10px; border:1px solid #fecaca; border-radius:6px; #fff`. The URL is in `ui-monospace 12.5px/500`, ellipsis, followed by a `.ib` "Copy" button.
- **Interaction:** Copy writes to the clipboard and shows the toast "Meeting link copied".

### C81 · Location Block
- **Purpose:** In-person venue details.
- **Where used:** live-session-detail for in-person sessions that aren't cancelled.
- **Implementation:** `.loc`. Class **B**.
- **Visual:** a 40px r8 `#f5f5f5` pin tile + room `16px` bold + address and QR note `14px/1.5 #525252`.

---

## 19. Certificate Components

### C82 · Certificate Document
- **Purpose:** Render the issued certificate (template, learner, course, dates, code).
- **Where used:** certificates card previews, certificate-detail full view. The file notes it uses the same visual as the admin template preview (`designs/admin/code/certificate-templates.html .certificate-preview`).
- **Implementation:** `.doc` using **container-query units** so it scales identically at any size (`certificates.html:77-93`, duplicated in `certificate-detail.html:90-106`). Hand-built, approved. Class **D**.
- **Structure:**
  - Paper `aspect-ratio:1.414/1`, background `#fffdf8`, r4.
  - Inset frame: `2.2cqw #f8f1dd` box-shadow plus an inner `1px #d9c58e` border at `3.6cqw`.
  - Org mark top-left: brand square with initial + org name.
  - Eyebrow (uppercase, `.22em`, `#947b34`) → template title (Georgia serif `4.4cqw`) → "This certifies that" → learner name (Georgia italic `4.8cqw`, **brand indigo**, underlined `#e8dcb8`) → lead text → course (`2.5cqw/700`).
  - Footer: instructor signature line, circular seal ("NL", serif `#947b34`), date signature line.
  - Bottom line: "Verification code CERT-A7X9K2 · Valid until … · Verify at upspace.app/verify".
- **Visual:** the only place in the Learner UI that uses a serif font (`Georgia, "Times New Roman", serif`) and the gold palette (`#f8f1dd`, `#d9c58e`, `#947b34`, `#e8dcb8`, `#bfae7a`).
- **Detail framing:** `.stage` (`padding:clamp(16px,2.4vw,36px); #f5f5f5; r12`) with the document `max-width:960px` and `box-shadow:0 1px 3px rgba(23,23,17,.06), 0 12px 32px -16px rgba(23,23,17,.12)`.
- **A11y:** in the detail view the document is `role=img` with a full `aria-label`. In cards it is `aria-hidden`.

### C83 · Verification Code Box
- **Purpose:** Share a certificate verification code.
- **Where used:** certificate-detail "Verification" card (`certificate-detail.html:116-121`).
- **Implementation:** `.code-box`. Class **B**.
- **Visual:** `display:flex; gap:8px; padding:6px 6px 6px 12px; border:1px solid #e5e5e5; border-radius:8px; background:#fafafa`. The code is `ui-monospace 15px/600`, `letter-spacing:.06em`, followed by a `.copy` button (C18).
- **Hint:** "Share this code with an employer or institution. They can check it at upspace.app/verify — no account needed."
- **Related actions (side card):** primary block "⬇ Download certificate" and secondary block "🛡 Verify certificate" (opens `verify-certificate.html?code=` in a new tab).

### C84 · Inline Download Error
- **Purpose:** An error local to one action area.
- **Where used:** certificate card `.dl-slot`, certificate-detail `#dlSlot`.
- **Implementation:** `.dl-err`. Class **B**.
- **Visual:** `display:flex; justify-content:space-between; padding:10px 12px; border-radius:8px; #fef2f2; 1px #fecaca; 13–13.5px #991b1b` + a small white "Try again" button (red text, r6).
- **Copy:** "Couldn't download this certificate."
- **Principle:** the code comment says "only this area errors". The page stays usable.

---

## 20. AI Learning Components

**AI entry points** (there is no AI landing page):
1. Sidebar **Your Coach** → `coach.html`.
2. Course overview:
   - **Ask AI** dock (C86) / side sheet (C87).
   - **Generate flashcards** button → dialog (C91).
   - **Revision notes** row per completed module (C90).
3. Course player **AI Tutor** panel (C61).
4. Dashboard first-time state link "Ask Your Coach".

**Shared AI visual language:**
- The sparkle icon and the **AI mark** (C85).
- The indigo gradient `#6366f1→#4338ca`.
- Scope hints under titles ("Answers from this lesson only", "Answers come from this course only", "Built only from this module's lessons and your results — nothing is added from outside the course.", "Cards are made from this course's lesson text and transcripts only.").
- Generation shown as a step list (C89).
- "Helpful?" thumbs (C64).
- Explicit "not enough content" empty states.
- Footer disclaimers such as "Generated by AI from your course content. Check key details against the lessons."

**Shared store:** `localStorage["upspace-study-v2"] = { notes:{"CS-301:2":{createdAt,focus}}, decks:{"CS-301":{course,createdAt,focus,short,cards:[{f,b}]}}, plans:[…] }`.

### C85 · AI Mark
- **Purpose:** Identity glyph for AI surfaces.
- **Where used:** player tutor head (30px), flashcards dialog head `.fc-mark` (32px), coach turns (32px) and hero (40px), revision-notes create panel (44px, `r12` with `box-shadow:0 6px 16px rgba(79,70,229,.25)`).
- **Implementation:** `.ai-mark` / `.fc-mark`. Class **B**.
- **Visual:** rounded square (r8 or r12), `linear-gradient(135deg,#6366f1,#4338ca)`, white 16–20px icon (sparkles; the coach uses `messages-square`).

### C86 · Ask AI Dock (floating bottom bar)
- **Purpose:** Quick, Google-Docs-style Q&A about a course from the overview page.
- **Where used:** course-overview (`course-overview.html:183-222, 865-1041`). The header says: "undocumented — AI-006 only defines the tutor inside the player. Built on user request".
- **Implementation:** `.ai-dock[data-state]` with states `pill | input | thinking | answer | off`. Hand-built, approved. Class **B**.
- **Structure:**
  - **Pill:** an 88px (100 on hover) × 36px white pill with a brand sparkle, `box-shadow:0 2px 8px rgba(23,23,17,.06)`.
  - **Card:** `width:min(760px,100%)`, r16, bordered. It contains:
    - an optional answer area (sparkle + 👍/👎 + "switch to side panel" + ✕; quoted question `13px #a3a3a3`; answer `15px/1.6`, pre-wrap; `max-height:min(46vh,380px)`, scrolls)
    - suggestion chips (only on the first open, when the log is empty)
    - the input row (sparkle, borderless textarea "Ask anything about this course…" / "Ask a follow-up…", ⋮ menu C88, round send)
  - **Thinking** row: spinning sparkle + "Thinking…" + round Stop button.
- **Visual:** `position:sticky; bottom:20px; z-index:15`, centred. The card animates in with `barIn` (8px + scale .98, .25s).
- **Interaction:**
  - Pill → input (or answer if a previous answer exists).
  - Send → thinking (0.9–1.6 s) → answer.
  - **Stop** cancels and puts the question back into the input.
  - Blurring an empty input collapses the dock back to the pill.
  - Escape order: menu → sheet → dock.
  - ⋮ offers "Switch to side panel" and "Turn off bottom bar". When turned off, the pill only opens the side sheet (the setting persists).
  - Answers are scoped to course metadata/outline and decline otherwise ("I can only help with content from this course…"). Requests for assessment answers are refused.

### C87 · Ask AI Side Sheet
- **Purpose:** Full-thread view of the same course conversation.
- **Where used:** course-overview (`course-overview.html:232-249`).
- **Implementation:** `aside.sheet` (`role=dialog`, `aria-modal=true`). The file says "library Aside · Right". Class **C**.
- **Visual:**
  - `position:fixed; right:0; top:0; bottom:0; width:min(440px,100vw); background:#fff; border-left:1px solid #e5e5e5; transform:translateX(100%) → none (.3s ease-curve)`.
  - Backdrop `rgba(15,23,42,.32)` fades in.
  - Head (`padding:14px 12px 14px 20px`, bottom border): sparkle + "Ask AI" `16px/700` + hint "Answers come from this course only" + 🗑 Clear (only when there are messages) + "switch to bottom bar" + ✕.
  - Thread `padding:20px; gap:18px` of C62 messages. The empty state has a paragraph + chips pinned to the bottom.
  - Foot composer C43.
- **Interaction:** the backdrop or ✕ closes it and restores focus to the pill. While the sheet is open the dock is hidden.

### C88 · Overflow Dropdown Menu
- **Purpose:** Secondary actions behind ⋮.
- **Where used:** Ask AI dock.
- **Implementation:** `.menu` (`course-overview.html:224-230`). The file says "library pattern (Dropdown menu / _Dropdown list item)". Class **A**.
- **Visual:**
  - `min-width:220px; padding:4px; #fff; 1px #e5e5e5; r8; box-shadow:0 8px 24px rgba(23,23,17,.08)`.
  - Opens **upward** (`bottom:calc(100% + 6px)`), with a `.down` variant.
  - Items `height:40px; padding:0 10px; r6; 14px/500 #404040` with a 16px `#525252` icon; hover or focus `#f5f5f5`.
- **Interaction:** focus moves to the first item on open. Outside click or Escape closes it. `aria-haspopup=menu` / `aria-expanded` are kept in sync.

### C89 · AI Generation Progress (step list)
- **Purpose:** Show the stages of an AI generation, with a failure point.
- **Where used:** flashcards dialog, revision-notes generating state, coach plan building.
- **Implementation:** `.gsteps` / `.steps` (`course-overview.html:336-345`, `revision-notes.html:167-176`, `coach.html:104-113`). Hand-built, approved, and reused by the Course Designer question bank per `MISSING_COMPONENTS.md`. Class **D**.
- **Visual:**
  - `ol` grid, `gap:10–14px`. Items `14.5–15px`.
  - Pending `#a3a3a3`; active `#171717/500`; done `#525252`.
  - Dot 18–22px circle:
    - pending: `1.5px #e5e5e5`
    - active: `#e0e7ff` ring with a brand top segment, spinning .8s
    - done: brand fill with a white 11–12px check
    - failed: red fill with a white ✕
- **Steps (examples):**
  - Flashcards: "Analyzing course content → Picking key terms and concepts → Writing question and answer cards" (800 ms each).
  - Coach: "Checking your progress in …" / "Finding what's left and what to revise" / "Building your schedule".
- **Failure (`?ai=fail` / `?state=fail`):** the failed step turns red, followed by "**Couldn't generate this right now.** Nothing was saved. [Try again in a moment.]" + primary "Try again" + secondary "Cancel" (flashcards) or secondary "Try again" (coach).
- **Revision notes** adds a skeleton preview (`.skel`) under the steps.

### C90 · Revision Notes Row
- **Purpose:** Per-module entry to AI revision notes, inside the outline accordion.
- **Where used:** course-overview module panels (`course-overview.html:308-320, 626-634`).
- **Implementation:** `.nr`. Hand-built, approved. Class **B**.
- **Visual:** `display:flex; gap:12px; flex-wrap:wrap; margin-top:12px; padding:12px 14px; border:1px solid #f0f0f0; border-radius:12px; background:#fafafa`. A 32px white r6 icon tile (brand notes icon) + "**Revision notes**" `14.5px/600` + sub `13px #a3a3a3` + actions (C18 `.sbtn`).
- **States:**

  | State | Sub text | Actions |
  |---|---|---|
  | Module not complete (`.locked`, tertiary icon) | "Available once you complete this module." | none |
  | Complete, no notes | "Key takeaways and focus areas for this module, made by AI." | primary "✦ Create revision notes" |
  | Notes exist | "Created 2 hours ago" | "View" + "⬇ Download PDF" |

### C91 · Flashcards Dialog (with card peek)
- **Purpose:** The entire flashcard create/view flow in one modal.
- **Where used:** course-overview (opened by the side-card button or `#flashcards`).
- **Implementation:** `.fc-overlay > .fc-modal.fc-dialog` (`course-overview.html:367-385, 1044-1053`). The file says "Modal (library)". Class **C**.
- **Visual:**
  - Dialog `width:min(680px,100%); max-height:calc(100vh - 32px)`, r12.
  - Head `padding:22px 24px 16px` + bottom border: H3 "Flashcards" `18px/700` + "Question-and-answer cards made from this course's lessons." + ✕ (C16 `.fc-x`).
  - Body `padding:22px 24px 24px`, scrolls.
  - Overlay `rgba(10,10,10,.5)`.
- **Body states:**
  1. **Form:** 2-column grid:
     - "Number of cards" select (C38)
     - "What should these flashcards focus on? (optional)" input (C39)
     - actions right-aligned: primary "✦ Generate flashcards" (or "Regenerate" + "Cancel")
     - hint "Cards are made from this course's lesson text and transcripts only."
  2. **Generating:** head (C85 mark + "Generating your flashcards…" + course) + C89.
  3. **Set ready:**
     - head "**12 flashcards** Generated just now · focus: …"
     - optional note (`#f5f5f5` box): "Only N cards could be made from this course's content. Sets aren't padded with material from outside the course."
     - **card peek**: 3-column grid of the first 3 cards (`#fafafa`, r8, term bold + answer 3-line clamp)
     - footer: primary "Study flashcards" (→ `flashcard-study.html`), secondary "↻ Regenerate", secondary 🗑 (opens the delete Modal C99), and the caption "Generated by AI from this course's lessons."
  4. **No source content:** "**There's not enough course content to generate flashcards.** This course's lessons don't have text or transcripts yet. Flashcards are only made from the course itself."
  5. **Error:** C89 failure.
- **Interaction:**
  - Focus moves to the first field on open and is restored on close.
  - `body{overflow:hidden}` while open.
  - Escape or a backdrop click closes it.
  - The entry button's label syncs to the state ("✦ Generate flashcards" ↔ "Flashcards · 12 cards").
- **Responsive:** ≤560–760px uses a single column and single-column peek, with 18px side padding.

### C92 · Revision Notes Create Panel
- **Purpose:** Explain what will be generated and take an optional focus.
- **Where used:** revision-notes before generation (`revision-notes.html:101-127`).
- **Implementation:** `form.card.create`. Class **B**.
- **Structure:**
  1. Top row: AI mark (44px) + H2 "Create revision notes for this module" `20px/700` + "A short, study-ready summary built from the 3 lessons you completed and your Knowledge check results."
  2. **Tiles** (auto-fit 220px): "Key takeaways", "Definitions & examples (N terms…)", "Focus areas" (`.off` dashed white when there's no assessment: "Not included — this module has no assessment."). Each tile is `padding:16px; 1px #f0f0f0; r12; #fafafa` with a 32px icon tile.
  3. Focus textarea (C40) + chips "From this module: …" (C44 toggle).
  4. Footer (top border): green shield + grounding statement, and primary **lg** (48px) "✦ Generate revision notes".
- **Visual:** padding `clamp(22px,2.4vw,40px)`, r16.

### C93 · Revision Notes Document
- **Purpose:** The generated, printable study notes.
- **Where used:** revision-notes after generation (`revision-notes.html:195-242`).
- **Implementation:** `article.card.doc`. Hand-built, approved. Class **B**.
- **Structure:**
  1. `.doc-summary` 4-cell stat strip (`#fafafa` cells, r12, `20px/700` values): Key takeaways · Definitions · Focus areas · "~6 min To review".
  2. Chips (`28px`, pill): "🎯 Personalized with your Knowledge check results" (brand), "Focus: …", "Generated 2 hours ago".
  3. Numbered sections (C13 variant 3):
     - **Key takeaways:** bordered r12 cards, 16px text, check icon, source lesson `12.5px #a3a3a3`.
     - **Focus areas:** warning-tinted cards (`#fefce8`, `#fef08a` border) with concept + detail + a white "▶ Review lesson" button; or success "Great work — no weak areas detected."
     - **Important definitions:** `dl` cards in a `minmax(300px)` grid.
     - **Examples:** `3px` brand left-bar blocks.
     - **Built from:** source lesson link chips.
  4. Footer: disclaimer + Helpful rating (C64).
- **Header actions** (C11-style header, right side):
  - icon buttons (C16 with tooltip): ↻ Regenerate, ⧉ Copy text, and 🗑 Delete (when saved)
  - secondary "💾 Save" / disabled green "✓ Saved"
  - primary "⬇ Download PDF" (`window.print()`)
- **Print:** `@media print` hides the chrome and rail, shows `.print-head`, uses a 2-column definition grid, and avoids breaks inside cards.

### C94 · Study Rail Cards
- **Purpose:** Context and navigation next to a study document or session.
- **Where used:** revision-notes rail, flashcard-study rail.
- **Implementation:** `.rail .rcard` / `.srail .rc`. Class **B**.
- **Cards:**
  - **On this page (TOC):** left 2px `#f0f0f0` rail. Links `14px #525252` with counts; the active link (scroll-spy through IntersectionObserver) gets a brand left border and brand `600` text. Hidden at ≤1100px.
  - **Built from N lessons · M min:** lesson list with green check discs and durations.
  - **Your results:** 56px ring (C47) + "Knowledge check — 3 of 5 correct · 2 focus areas", or "This module has no assessment, so the notes cover the lesson content only."
  - **Other modules:** module switcher rows (26px number tile + title + status "Notes" green / "Create" brand / 🔒). The current row is `#eef2ff`, and locked rows are non-interactive `#a3a3a3`.
  - **This set (flashcards):** "Created Sep 23" + 3 stat tiles (Cards / Seen / Left; `#fafafa` r8, `18px/700`).
  - **All cards:** scrollable list (24px number tile + term + ✓ when seen). The current card is `#eef2ff` / brand.
  - **Shortcuts:** `kbd` list (hidden on touch).
- **Visual:** cards `padding:16–18px`. Headings `13px/600 #a3a3a3`. The rail is `position:sticky; top:20px`, with a max-height and hidden scrollbar.

### C95 · Flashcard (two-sided flip card)
- **Purpose:** Study one term/answer pair at a time.
- **Where used:** flashcard-study (`flashcard-study.html:78-102`).
- **Implementation:** `button.flash` with a 3D flip. Hand-built, approved. Class **B**.
- **Structure:**
  1. Progress row "Card 4 of 12" + 8px bar (C46).
  2. The card: front "Term" label + term; back "Answer" label (brand) + answer. The front hint reads "Tap to flip · or press Space".
  3. Controls grid `1fr auto 1fr`: secondary "‹ Previous", primary "⟲ Flip" (min-width 120), secondary "Next ›" (becomes "Finish" on the last card).
  4. `kbd` hints.
- **Visual:**
  - `perspective:1400px`. The card is `height:clamp(260px,56vh,640px)`.
  - Faces `#fff`, `1px #e5e5e5` (back `#e0e7ff`), r16, `padding:32px clamp(20px,5vw,56px)`.
  - Rotation `rotateY(180deg)` over `.45s cubic-bezier(.2,.7,.2,1)`.
  - Front text `clamp(22px,1.2vw+14px,40px)/700`. Back text `clamp(17px,.6vw+12px,24px)/500/1.6`.
- **Header actions:** ghost "Shuffle" and "Restart", each with a toast ("Cards shuffled", "Back to the first card").
- **Interaction:**
  - Click or tap flips. Space/Enter flip, ←/→ move.
  - Touch swipe over 50px moves between cards.
  - Choosing an item in the card list jumps to that card.
  - Finishing shows a **completion panel**: green check circle + "You've gone through all 12 cards." + "Study again" (primary) / "Shuffle and restart" / "Back to course".
- **Responsive:** ≤640px shrinks the card (`clamp(240px,52vh,460px)`), shows icon-only Previous/Next (44px), and hides key hints.
- **Not built** (per the file header): "Got it / Still learning" (AI-007-FR-05), by user decision.

### C96 · Coach Empty Hero
- **Purpose:** First-run prompt for the Learning Coach.
- **Where used:** coach, before the first message (`coach.html:70-78`).
- **Implementation:** `.stage.empty .hero`. Class **B**.
- **Visual:**
  - Vertically centred in an 800px column (`padding-bottom:10vh`).
  - AI mark 40px → H1 "What are you trying to accomplish?" `clamp(24px,2.6vw,30px)/700` → "Ask about anything in your courses, or tell me a goal or deadline and I'll plan it with you." `15.5px`, max 520px.
  - Then the large composer (C43) and 4 icon chips (C44), centred (left-aligned at ≤640px).
- **Transition:** the first message removes `.empty`. The hero and chips hide, the thread appears, and the composer docks at the bottom (sticky, with a gradient fade from the canvas).

### C97 · Coach Turn / Grounded Answer
- **Purpose:** A coach reply, shown without a bubble.
- **Where used:** coach thread.
- **Implementation:** `.coach` grid `32px | 1fr` (mark + body). Class **B**.
- **Visual:**
  - Body text `15.5px/1.65`. There's no bubble, unlike C62.
  - **Grounded answer** block `.answer`: `3px #e0e7ff` left bar, white, radius `0 8 8 0`, term bold `15.5px` + definition `15px #404040`.
  - Source line: "Source: 'Hash tables & collisions' · Advanced Data Structures" `13px #a3a3a3`.
  - Link chips (C44) such as "📖 Open the lesson" / "Practise with flashcards".
- **Declines** (copy):
  - Outside learning: "I can only help with your learning…"
  - No match: "I couldn't find that in your courses, so I won't guess…"
- **Responsive:** ≤640px stacks the mark above the body (26px mark).

### C98 · Study Plan Block
- **Purpose:** A structured plan answer (revision, week, goal, routine) that can be saved.
- **Where used:** coach replies (`coach.html:118-147`).
- **Implementation:** `.plan`. Hand-built, approved. Class **B**.
- **Structure:**
  1. `.plan-head`: kicker (`12.5px/600` brand, e.g. "Revision plan"), H3 `18px/700`, goal line; a date field (C39) for exam plans.
  2. `.plan-stats` 3-column `dl` (Days · Study time · Sessions), with dividers.
  3. Optional `.plan-note` (warning-subtle strip with a `#fef08a` bottom border): "This is a tight schedule…".
  4. `.plan-days` list: Date tile (C51 coach variant) | linked tasks | "40 min".
  5. Optional tips `ul`.
  6. `.plan-foot` (`#fafafa`): primary "🔖 Save plan" + "Saved plans get a weekly check-in, and a nudge if you fall behind."
- **Visual:** white, r12, bordered, sections divided by `#f5f5f5` borders.
- **Interaction:**
  - Changing the date rebuilds the plan and shows the toast "Plan updated for Tue, Sep 29".
  - Save turns into the disabled "✓ Saved", locks the date, and shows the toast "Plan saved — check-ins are on".

---

## 21. Modals / Drawers / Overlays

**Inventory of overlays in the Learner build:**

| Overlay | Type | Size | Scrim | Component |
|---|---|---|---|---|
| Delete flashcards / Delete notes confirm | Modal | `min(420px,100%)` | `rgba(10,10,10,.5)` | C99 |
| QR check-in | Modal | 420 | same | C77 |
| Flashcards | Modal (large dialog) | `min(680px,100%)` | same | C91 |
| Ask AI | Right side sheet | `min(440px,100vw)` | `rgba(15,23,42,.32)` | C87 |
| Course content rail (≤1024px) | Right drawer | `min(384px,92vw)` | `rgba(15,23,42,.45)` | C57 |
| Sidebar (≤900px) | Left drawer | 260 | `rgba(15,23,42,.45)` | C06 |
| Submit confirmation | Anchored popover | `min(360px,100%)` | none | C72 |
| Profile menu / ⋮ menu | Dropdown | 200 / 220 min | none | C04 / C88 |
| Tooltip | Hover tip | auto | none | C66 |

### C99 · Modal Dialog
- **Purpose:** Blocking confirmation or focused task.
- **Where used:**
  - course-overview delete flashcards
  - revision-notes delete notes
  - live-session-detail QR scanner
  - flashcards dialog (large variant, C91)
- **Implementation:** `.overlay > .modal` / `.fc-overlay > .fc-modal` with `role=dialog aria-modal=true aria-labelledby`. Files say "Modal — library (overlay #0a0a0a/50%, white r12, 24px)". Class **A**.
- **Visual:**
  - Overlay `position:fixed; inset:0; z-index:80–95; display:flex; align-items:center; justify-content:center; padding:16px`. It fades in (`.15s`) on the live page.
  - Box `#fff; border-radius:12px; padding:24px; box-shadow:0 24px 48px rgba(10,10,10,.18)`, rising in 8px.
  - H3 `18px/700`, body `14px/1.5 #525252` (`margin-top:6px`).
  - Action row `justify-content:flex-end; gap:8px; margin-top:20–22px`. Buttons are 44px in the live modal.
- **Destructive confirm copy:** "Delete this course's flashcards? — You can generate them again at any time." / "Delete these notes? — You can create them again at any time." Actions: [Cancel] [Delete (red)].
- **Interaction:**
  - Focus goes to **Cancel** on open for destructive confirms.
  - Escape closes it. On the overview, the flashcards delete modal uses a capture-phase listener so Escape closes only the top modal.
  - A backdrop click closes it.
  - No focus trap.

### C100 · Backdrop / Scrim
- **Class:** **E**. Two scrim tints are used:
  - `rgba(10,10,10,.5)` for centred modals.
  - Slate `rgba(15,23,42,.32–.45)` for drawers and sheets.
- **Interaction:** every scrim closes its overlay on click.

---

## 22. Feedback / Toasts / Alerts

**How success, errors and confirmations are communicated:**

| Situation | Mechanism |
|---|---|
| Action succeeded (saved, submitted, downloaded, copied, shuffled) | **Toast** (C101), bottom-right, auto-dismiss |
| Page-level condition (overdue, cancelled, expired, revoked, didn't start) | **Alert** (C73) at the top of the main column |
| Action failed but the page is fine (join fails, submit fails, download fails) | Alert or inline error (C84) **at the action site**, with "Try again" |
| Validation before an irreversible step | Warning Alert above the form (C72 pre-checks), never field-level |
| Pending result (grading, processing) | Waiting block (C71) |
| Background save | Draft save indicator (C53), `aria-live` |
| Lightweight confirm before submit | Anchored popover (C72) |
| Destructive confirm | Modal (C99) |
| Copy to clipboard | Toast ("Meeting link copied") or the button label flips to "✓ Copied" |

### C101 · Toast
- **Purpose:** Transient success confirmation.
- **Where used:** assignment-detail, live-session-detail, certificates, certificate-detail, coach, revision-notes, flashcard-study.
- **Implementation:** `#toast.toast[role=status]` (`assignment-detail.html:266-270`). Files say "Toast — library (Success: #f5f5f5, r8, round check #dcfce7)". Class **A**.
- **Visual:**
  - `position:fixed; right:24px; bottom:24px; z-index:70–90; display:flex; gap:12px; padding:10px 14px` (`10px 10px 10px 14px` when it has a close button); `min-width:200–260px`.
  - `background:#f5f5f5; border:1px solid #e5e5e5; border-radius:8px; 14–14.5px/500; box-shadow:0 8px 24px rgba(23,23,17,.08)`.
  - Icon: 28–32px circle `#dcfce7` with a green check.
  - Optional dismiss `.ib` ✕ (assignment, live).
- **Timing:** auto-hides after 3.2 s (assignment, live), 2.6 s (certificates, coach, revision notes) or 2.0 s (flashcards).
- **Responsive:** ≤640px goes full width with 16px sides, at `bottom:16px` (56px on live and certificates, clearing the preview control).
- **Variants:** success only. There are no error, info or warning toasts in the Learner build.
- **Messages observed:**
  - "Draft saved", "Assignment submitted"
  - "Opening Zoom in a new tab…", "Meeting link copied"
  - "Certificate downloaded", "Plan saved — check-ins are on", "Plan updated for …"
  - "Notes saved to this module", "Notes regenerated", "Notes deleted"
  - "Copied to clipboard", "Thanks for the feedback"
  - "Cards shuffled", "Back to the first card"

---

## 23. Empty / Loading / Error States

**Convention:** states render **in the place of the content they replace**, inside the same card or container. A full-page spinner is never used. The copy is **"Bold sentence." + one plain sentence**, with an optional single action.

### C102 · Skeleton Loader
- **Purpose:** Placeholder while data loads.
- **Where used:** every data-driven page. Hand-built, approved, and reused by Course Designer per `MISSING_COMPONENTS.md`.
- **Implementation:** `.sk` bars with a moving gradient. Class **D**.
- **Visual:**
  - Bar `display:block; height:12px; border-radius:4px` (6px on my-courses). `background:linear-gradient(90deg,#f0f0f0 25%,#e5e5e5 50%,#f0f0f0 75%)` (`#f3f3f3/#e9e9e9` on dashboard and revision notes), `background-size:200% 100%; animation:loading 1.4s infinite` (1.5s on my-courses).
  - `.sk + .sk{margin-top:9–10px}`.
- **Shape variants (the skeleton mirrors the final layout):**
  - Table rows (assignments: 5 rows with per-column bars)
  - Session rows + next-block skeleton (live)
  - Course cards (16:9 thumbnail + 2 lines)
  - Hero (280px block)
  - Detail page (header bars + section cards + side card)
  - **Document-shaped skeleton** (`.sk-doc`, 1.414:1, centred bars) for certificates
  - Generation preview (revision notes)
  - Breadcrumb current (160px inline bar)
- **ARIA:** containers get `aria-busy="true"` plus an `aria-label` ("Loading sessions"). Skeleton rows are `aria-hidden`.
- **Timing:** mock delay 450–500 ms.

### C103 · Empty State
- **Purpose:** No data, or no filter results.
- **Where used:** all list pages, detail sub-sections, dashboard panels.
- **Implementation:** `.empty`, `.empty-in`, `.widget-state`, `.fc-empty`. Hand-built, approved. Class **D**.
- **Visual:**
  - Centred text. Padding `56–64px 20px` for list-level states, `36px 24px` in dashboard panels, `24px 16px` inside sections.
  - Title `15–15.5px/600–700`, text `13.5–14px #a3a3a3` (the dashboard caps it at `max-width:420px`), optional button `margin-top:16px`.
  - List-level empties sit in their own white r12 bordered card. In-section empties (assignment) use a **dashed** `1px #e5e5e5` r8 border. Certificates adds a 48px `#f5f5f5` icon circle (award icon).
- **Copy inventory (all observed):**
  - My Courses: "No courses assigned yet. / Check back soon or browse available courses." [Browse courses]
  - My Courses search: "No matching courses found. / Try a different search."
  - My Courses tabs: "No completed courses yet." · "Nothing new to start." · "No courses match these filters."
  - Assignments: "No assignments yet. / Assigned work will appear here." · "No assignments match your filters. / Try another status or clear the search."
  - Assignment detail: "Nothing submitted yet. / This assignment is closed for submissions." · "No feedback has been released yet."
  - Live: "No upcoming sessions. / Scheduled live sessions will appear here." · "No past sessions yet. / Sessions you've been part of will appear here after they end." · "No sessions match your filters. / Try another type or clear the search."
  - Certificates: "No certificates yet. / Complete an eligible course to earn your first certificate." [Go to My Courses]
  - Dashboard: "You're not in the middle of a course. / You've finished everything you started. Pick up a new course or review one you completed." [Browse My Courses] · "You're all caught up. / Nothing is due and no sessions are scheduled this week."
  - Player transcript: "No transcript for this lesson"
  - Flashcards: "No flashcards for this course yet. / Generate a set from the Flashcards section on the course page." [Back to course]
  - AI "not enough content" (flashcards dialog, revision notes): explanatory, with **no** fallback generation.

### C104 · Error State with Retry
- **Purpose:** Load failure for a section or page.
- **Where used:** dashboard panels, assignments, assignment-detail, live-sessions, live-session-detail, certificates, certificate-detail.
- **Implementation:** reuses the `.empty` container with `role="alert"`. The dashboard uses a dedicated `.err` row. Class **B**.
- **Visual:**
  - List pages: the centred empty layout with a secondary button (label is "Try again", or "Retry" on certificates).
  - Dashboard `.err`: a horizontal row with a 20px red alert icon, bold title + sentence, and a secondary **sm** "Try again".
- **Copy:**
  - "Couldn't load your assignments. / Check your connection and try again."
  - "Couldn't load your courses. / Check your connection and try again." (dashboard)
  - "Couldn't load your schedule. / Assignments and sessions will show here once this loads."
  - Detail pages add a second action: "Back to assignments" / "Back to Live Sessions" / "Back to Certificates".
- **Scope:** errors are sectional. The dashboard error hides only the dependent "Keep going" section.

### C105 · Not Found / Unavailable State
- **Purpose:** An invalid or inaccessible record id.
- **Where used:** course-overview, assignment-detail, live-session-detail, certificate-detail, flashcard-study.
- **Implementation:** Class **B**.
- **Copy:**
  - Overview: "Course not found — This course may have been removed, or you no longer have access to it." [Back to My Courses] (`.not-found` card, `padding:80px 20px`, r16)
  - Assignment: "Assignment not found. It may have been removed, or you're no longer assigned to it." [Back to assignments]
  - Live: "Session unavailable. It may have been removed, or you're no longer part of this class." [Back to Live Sessions]
  - Certificate: "Certificate not found. It may have been removed from your account." [Back to Certificates]
- **Breadcrumb:** the current crumb becomes "Not found" or "Session unavailable".

### C106 · First-time Welcome with Illustration
- **Purpose:** Dashboard state for a learner with no enrolments.
- **Where used:** dashboard `?state=empty` (`dashboard.html:108-118`).
- **Implementation:** `.panel.welcome` + inline SVG illustration (book, floating course card, play disc, twinkles). Hand-built, approved 2026-09-24. Class **B**.
- **Visual:**
  - 2-column grid, `padding:clamp(28px,4vw,64px)`.
  - H2 "Your learning journey starts here." `clamp(24px,1.2vw+14px,34px)/-.7px`.
  - Paragraph `16px/1.6`, max 460px.
  - Actions: primary lg "View My Courses →" + link "Ask Your Coach".
  - Illustration max 440px, in library indigo tints (`#eef2ff`, `#e0e7ff`, `#c7d2fe`, `#a5b4fc`, `#6366f1`, `#4f46e5`).
  - Motion: `float` (6px, 4s) and `twinkle` (scale .7, 2.6s), disabled under reduced motion.
- **Responsive:** ≤760px stacks into one column, with the illustration first at max 300px.

### C107 · Design-only Preview State Switcher (not product UI)
- **Purpose:** Let reviewers force demo states.
- **Where used:** dashboard, live-sessions, live-session-detail, certificates, certificate-detail.
- **Implementation:** `label.preview` + `<select>`, fixed at bottom-left (offset `left:244px` on desktop). **Not part of the Learner product.** Excluded from the component counts.
- **Visual:** `1px dashed #a3a3a3`, `ui-monospace 11px`, `#737373`. The file comments call it "deliberately utilitarian".

---

## 24. Responsive Patterns

**Summary by pattern:**

| Pattern | Desktop | Tablet | Mobile |
|---|---|---|---|
| Shell | 232px sidebar + 80px top bar | same down to 901px | ≤900px: off-canvas 260px drawer + scrim; content padding 16px |
| Top bar search | 240px | — | hidden ≤700px |
| Two-column detail (P4) | main + sticky side card | ≤1100–1180px: side card moves **above** main, static; may become a 2-column internal grid | ≤640–700px: side card becomes block; section padding 18px 16px |
| Dashboard | 1.7fr / 1fr | ≤1080px: stacked | ≤760px: hero stacks (16:8 thumbnail), welcome stacks |
| Card grids | auto-fill/auto-fit minmax(240–300px) | column count reduces automatically | 1 column at ≤640–700px, gap 14–16px |
| Tables / row lists | full columns | ≤1100–1180px: drop the least important column, fold it inline | ≤760px: **rows become stacked cards** with a full-width action under a divider |
| Tabs | inline | — | horizontal scroll with hidden scrollbar (`overflow-x:auto`) |
| Toolbar | tabs · spacer · controls | wraps | spacer removed, search full width |
| Player | video + transcript/tutor side by side + 384px rail | ≤1024px: rail becomes a right drawer; header bar hidden; ≥880px container → panels side by side, else tabs | ≤640px: icon-only nav, compact header, ±10s hidden, panels 440px |
| Calendar | Day/Week/Month | — | ≤760px: Day/Month only, Week→Day, month chips → dots |
| Modals / dialogs | centred, fixed widths | — | full width minus 16px padding; single-column forms |
| Toast | bottom-right 24px | — | full width 16px sides |
| Flashcards | card + sticky rail | ≤1100px: rail below as a grid | ≤640px: shorter card, icon-only controls, no key hints |
| Coach | 800px centred column | — | ≤640px: coach mark stacks above text; chips left-aligned |

**Motion:** every file includes `@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}`.

**Touch:**
- `(hover:none)` hides keyboard hints on flashcards.
- Flashcards support swipe.
- The video seek uses `touch-action:none`.

---

## 25. Interaction Patterns

| ID | Pattern | How it works | Where |
|---|---|---|---|
| I01 | **Instant client-side filtering** | Tabs, selects and search re-render on change/input. No apply button, no URL state, no active-filter chips, no clear-all | my-courses, assignments, live-sessions |
| I02 | **Tab switching** | Segmented control; `aria-selected`/`aria-pressed`; content swaps in place; counts in tabs | §11 |
| I03 | **Dropdown open/close** | Click toggles; outside click closes; Escape closes (⋮ menu only); focus moves to the first item (⋮ menu only) | C04, C88 |
| I04 | **Accordion expand** | Button `aria-expanded` toggle; grid-rows 0fr→1fr animation .3s; chevron rotates; "Expand all/Collapse all" | C58 |
| I05 | **Whole-row / whole-card click** | Cards are `<a>`. Table and session rows use `data-href` and navigate on click unless the target is an inner link or button. The inner action link carries `tabindex=-1` to avoid a duplicate tab stop | C21, C27, C29 |
| I06 | **Hover affordance** | Cards: border → `#a3a3a3` + image zoom + arrow nudge. Rows: bg `#fafafa` + title → brand. No elevation changes | cards, rows |
| I07 | **Skeleton → content** | Skeleton in place of the final layout, ~450 ms, then content, empty or error | all data pages |
| I08 | **Sectional error + retry** | Errors scoped to the failed section or action, with "Try again"; the rest of the page stays usable | C104, C84, C74 |
| I09 | **Success = toast** | Bottom-right success toast, 2–3.2 s, optional ✕ | C101 |
| I10 | **Destructive confirm = modal** | Modal with Cancel focused + red Delete, right-aligned | C99 |
| I11 | **Irreversible submit = anchored popover with summary** | Pre-checks as warning alerts; popover summarises what will be sent + late warning; busy button; toast | C72 |
| I12 | **Auto-save drafts** | Debounce 900 ms + 30 s interval + `pagehide` flush; visible save status; retry on failure; manual "Save draft" | C53 |
| I13 | **File upload** | Click/keyboard/drag onto a dashed dropper; per-file validation (type, 25 MB) inline on the row; progress bar; cancel / retry / replace / remove | C42, C33 |
| I14 | **Sequential lesson navigation** | Prev/Next buttons; the end card offers Next; the rail lists lessons with locking; moving next marks complete; position auto-saved | C54–C59 |
| I15 | **Time-sync highlighting** | Transcript cue highlighting follows playback; auto-scroll toggle; click-to-seek | C60 |
| I16 | **Contextual AI chat** | Composer (Enter to send), typing indicator, scoped answers with a decline message, thumbs rating, suggestion chips, clear, persisted history | C61, C86, C87, C97 |
| I17 | **AI generation with steps** | Visible step list; failure marks a step and offers Try again; "Nothing was saved"; regenerate replaces | C89 |
| I18 | **Join window gating** | Join is disabled until 15 min before start, with an explanatory hint; busy "Joining…"; hand-off toast; "Rejoin" after joining | C74, C25 |
| I19 | **Progressive disclosure of availability** | Locked or blocked actions render as disabled with a lock icon + a one-line reason (prerequisites, window closed, module incomplete) instead of being hidden | C23, C68, C90, C59 |
| I20 | **Only render actions that exist** | No empty buttons: recordings, materials and certificates appear only when available ("never invent materials") | C29, C76 |
| I21 | **Dialog open/close** | Opening moves focus inside; Escape, backdrop or ✕ close; focus restores to the trigger; body scroll locked for the large dialog | C91, C99, C87 |
| I22 | **Keyboard shortcuts** | Player: Space play/pause, ←/→ seek. Flashcards: Space/Enter flip, ←/→ move. Composer: Enter / Shift+Enter | C54, C95, C43 |
| I23 | **Copy to clipboard** | Clipboard API, then a toast or label swap | C80, C83, C93 |
| I24 | **Deep links into state** | URL params/hashes open dialogs or states: `#flashcards`, `?join=1`, `?checkin=1`, `?watch=1`, `#materials`, `?print=1` | §4.1 |

**Form validation:** there is no inline field-level validation anywhere. Validation happens:
- at file-add time, as an error row;
- at submit time, as a warning Alert;
- through disabled Send buttons while inputs are empty.

---

## 26. Learner Workflows

Only workflows that exist in the build are documented.

### W01 · Continue learning from the Dashboard
1. The learner lands on the dashboard. The skeleton gives way to the greeting (C12) with a status sentence.
2. The "Continue learning" hero (C22) shows the last course, next lesson, time left, progress and lesson count.
3. The learner clicks **Continue lesson →**, which opens `course-player.html?id=`.
4. The player resumes the saved position (C54). **Alternatives:** "Course overview" link; "Keep going" cards (C21) → overview; "Coming up" rows (C30) → assignment or session detail.

### W02 · Start a course
1. My Courses → "Not started" tab (C35), or search (C37).
2. Course card (C21) "Start course" → Course Overview (P4).
3. Review the header badges, stats (C24) and outline accordion (C58/C59).
4. In the side card (C23):
   - If prerequisites are unmet or the start date is in the future → disabled "🔒 Start course" + reason note (I19).
   - Otherwise **Start course →** opens the player.
5. In the player, the first lesson changes from not-started to in-progress when loaded.

### W03 · Continue and complete a lesson
1. The player opens on the saved lesson and time (or on the in-progress lesson).
2. Play (C54), optionally with captions, speed or fullscreen, following the transcript (C60).
3. The position auto-saves continuously.
4. At the end, the End card (C55) says "Lesson complete / Up next: …", and the lesson is marked completed in the rail (C50 ✓).
5. **Next lesson** (end card, or C56) loads and autoplays the next lesson. Later lessons are unlocked sequentially (C59 locked + tooltip).
6. The module number tile turns green ✓ when every lesson in it is done (C58). Header and rail progress update (C46).

### W04 · Ask the AI Tutor inside a lesson
1. Player → AI Tutor panel (C61), or the "AI Tutor" tab on narrow screens.
2. Click a suggestion chip or type (C43), then press Enter.
3. The typing indicator (C63) shows, then the reply (C62) with an optional "▶ Jump to 3:12" (C65) and a Helpful rating (C64).
4. Out-of-scope questions get the decline message. Quiz answers are refused with a hint.
5. "Clear" empties the history. The history otherwise persists per course.

### W05 · Ask AI about a course (overview)
1. Course Overview → sparkle pill (C86) → input with starter chips.
2. Send → "Thinking…" (Stop available) → answer card with thumbs.
3. Follow-up questions ("Ask a follow-up…"), or **Switch to side panel** (C87) for the full thread.
4. The ⋮ menu (C88) can "Turn off bottom bar". After that the pill opens only the side panel.

### W06 · Submit an assignment
1. Assignments (sidebar "Assessments") → the table (C27) sorted by needed action → the row or "Open assignment".
2. The detail page (P4) shows the Summary card (C68: status To do, due, points, attempts) and the Instructions with assignment files (C33 download).
3. Write a response in the Rich Text Editor (C41) and/or upload files (C42 → C33 rows with progress, validation, retry, replace, remove).
4. Draft auto-save (C53): "Saving…" → "Draft saved · today at 7:12 PM". The status becomes **In progress**. There's also a manual **Save draft**, which shows a toast.
5. **Submit assignment** (footer or side card) runs the pre-checks (uploads finished; something to submit) and opens the confirmation popover (C72) with its summary and late warning.
6. Confirm → "Submitting…" (C15) → the page re-renders → toast "Assignment submitted".
7. Status becomes **Grading in progress** (C48 grey dot). A Waiting block (C71) explains it. The main column shows "Submitted work" (read-only response + files).
8. Once grading is released: **Graded** (green). The grade block (C69) shows score, pass/fail, grader, date, Instructor feedback (C70) and Marking breakdown (C28), depending on visibility.
9. **Resubmission** (if attempts remain and the window is open): "Resubmit assignment" → the editor opens as "Resubmit assignment" with a Cancel (ghost) → earlier attempts listed in Previous attempts (C34).
10. **Hidden results:** the status stays **Submitted**, with the Waiting block "Results not released yet".
11. **Failure path:** "Submission failed" error Alert; the draft is kept; "Try again" reopens the popover.

### W07 · Overdue and closed assignments
1. Past due, window open → row status "Overdue" (red) + "Open until Sep 27"; action "Submit assignment".
2. The detail page shows an error Alert "Overdue — due Sep 20 / You can still submit until …" and a summary note about late marking. The confirmation popover warns "Will be marked late".
3. Past the window → status "Overdue" + "Submission closed", with a lock Alert. The side-card CTA is a disabled "🔒 Submission closed". If nothing was submitted: "Nothing submitted yet."

### W08 · Join an online live session
1. Live Sessions → Upcoming tab. The Next session block (C25) is emphasised; the rest are grouped by day (C29).
2. More than 15 minutes before the start: a disabled "Session starts at 5:05 PM" + "Join opens at 4:50 PM" (I18).
3. Within 15 minutes, or live: **Join session** (list row, next block, or the detail When card C74). Joining from the list deep-links with `?join=1` and auto-joins on the detail page.
4. "Joining…" → toast "Opening Zoom in a new tab…" → "✓ You joined at 1:32 PM", and the button becomes "Rejoin session".
5. **Failure:** error Alert "Unable to join this session. Zoom didn't respond…" + the copyable meeting link (C80) + Try again.

### W09 · Check in to an in-person session
1. While live, the row or next block shows **Check in**. It deep-links with `?checkin=1`.
2. The QR scanner modal (C77) opens with the viewfinder animation.
3. The result modal shows success ("You're checked in — Recorded at …") or failure ("You're not enrolled in this session's class.").
4. The When card then shows "✓ Checked in at …".

### W10 · Review a past session
1. Live Sessions → Past tab. Rows are grouped by month, with attendance and actions.
2. "▶ Watch recording" deep-links with `?watch=1`, and the inline player (C76) opens. "View materials" deep-links with `#materials` (C33 list).
3. The When card shows "Your attendance: Present/Late/Absent".
4. The recording may instead show processing, attendees-only, or no section at all.

### W11 · View, download and verify a certificate
1. Certificates grid (C26): valid first, then expired and revoked (muted).
2. **Download** on the card → "Preparing…" → PDF file → toast "Certificate downloaded" (or an inline error C84 with "Try again").
3. **View certificate** → detail (P4): status pill header, optional expired/revoked Alert, the document (C82), and side cards (actions; Details dl; Verification code C83 with Copy).
4. **Verify certificate** opens the public verification page in a new tab, prefilled with the code.

### W12 · Generate revision notes (per module)
1. Course Overview → the completed module's accordion → Revision notes row (C90) → **Create revision notes**.
2. The revision-notes page shows the Create panel (C92) with tiles, the optional focus field and term chips.
3. **Generate revision notes** → step list (C89) + skeleton preview.
4. The notes document (C93) appears with its rail (C94: TOC scroll-spy, sources, results, other modules).
5. **Save** → "✓ Saved" + toast. Other header actions: Regenerate, Copy, Delete (Modal C99), Download PDF (print).
6. Returning to the overview, the row now reads "Created … ago" with View and Download PDF.
7. **Blocked states:**
   - Module not completed → state card "Complete this module to generate revision notes." + resume action.
   - No lesson text → "There's not enough course content to generate this."

### W13 · Generate and study flashcards (per course)
1. Course Overview side card → **Generate flashcards**, which opens the dialog (C91).
2. Choose the number of cards and an optional focus → **Generate flashcards** → steps (C89).
3. The set appears with a 3-card peek → **Study flashcards**, which opens `flashcard-study.html`.
4. The study session (C95): flip, Previous/Next, shuffle, restart, jump from the list (C94). Progress "Card N of M".
5. After the last card, the completion panel offers Study again / Shuffle and restart / Back to course.
6. Back in the dialog: Regenerate, or Delete (confirm modal). The entry button shows "Flashcards · 12 cards".

### W14 · Use the Learning Coach
1. Sidebar → **Your Coach** → the empty hero (C96) with the composer and 4 starter chips.
2. Ask a planning request (e.g. "I have an exam next Friday…") → a coach turn with the step list (C89) → Study plan block (C98) with stats, days (C51) and linked tasks.
3. Adjust the exam date, which rebuilds the plan and shows a toast. **Save plan** → "✓ Saved" + toast.
4. Ask a content question → grounded answer (C97) with source + chips to open the lesson or practise flashcards. Anything outside the learner's courses is declined.
5. Asking for flashcards or revision notes returns a pointer chip to the course page.

**Assessment taking:** there is no workflow, because the screens don't exist (§16).

---

## 27. Component Relationships

### 27.1 Composition per screen
```
dashboard            C01 C02 C03 · C12 · C13 · C22 · C30(C51) · C21(C52,C46) · C102 C103 C104 C106 · C107
my-courses           C01 C02 C03 · C10(C37) · C13(eyebrow) · C22 · C31(C51,C47) · C45(C35,C38×2) · C21(C52,C46) · C102 C103
course-overview      C01 C02 C03 · C07 · C11(C49,C24) · C13 · C58(C59,C50,C90) · C23(C46,C32,C14) · C86(C43,C44,C88,C64,C19) · C87(C62,C63,C64,C43) · C91(C38,C39,C89,C85) · C99 · C105
course-player        C09(C08,C07,C46,C16) · C54 · C55 · C56 · C35 · C60 · C61(C85,C62,C63,C64,C65,C44,C43,C19) · C57(C46,C58,C59,C50) · C66 · C67
assignments          C01 C02 C03 · C10(C37) · C35 · C27(C48,C17) · C102 C103 C104
assignment-detail    C01 C02 C03 · C07 · C11 · C73 · C69(C28,C70) · C71 · C20(prose,C33) · C41 · C42 · C33 · C53 · C72 · C15 · C34 · C68(C48,C32) · C101 · C102 C103 C104 C105
live-sessions        C01 C02 C03 · C10 · C45(C35,C37,C38,C35-view) · C25(C51,C48) · C29(C48,C17) · C75(C36,C18,C16) · C102 C103 C104 · C107
live-session-detail  C01 C02 C03 · C07 · C11(C48) · C73(C80) · C76(C54,C71) · C81 · C20(prose) · C33 · C74(C51,C32,C14,C15,C79) · C77(C99,C78) · C101 · C102 C104 C105 · C107
certificates         C01 C02 C03 · C10 · C26(C82,C49,C84,C15) · C101 · C102(doc) C103 C104 · C107
certificate-detail   C01 C02 C03 · C07 · C11(C49) · C73 · C82 · C20(side cards, C32, C83, C84) · C101 · C102(doc) C104 C105 · C107
coach                C01 C02 C03 · C96(C85,C43,C44) · C62(sent) · C97 · C89 · C98(C51,C39) · C101
revision-notes       C01 C02 C03 · C08 · C13(num) · C49 · C92(C85,C40,C44) · C89 · C102 · C93(C64) · C94(C47) · C16(tooltip) · C99 · C101 · P8
flashcard-study      C01 C02 C03 · C07 · C46 · C95 · C94 · C101 · P8
```

### 27.2 Reuse and equivalence notes (for Phase 2 mapping)
- **Course Card (C21)** is shared, byte-for-byte in intent, between my-courses and the dashboard.
- **Continue Hero (C22)** has two different implementations: the dashboard version (text + CTA button + link) and the my-courses version (whole-card link + play overlay).
- **Status vocabularies are per domain**, but every one renders through either C48 (dot label: assignments, live) or C49 (filled pill: course badges, certificates).
- **Date Tile (C51)** has 4 size variants across 4 screens.
- **Chat stack:** C43 composer + C19 send + C62 message + C63 typing + C64 rating + C44 chips are shared by the player tutor, the overview dock/sheet and coach. Coach renders AI turns without bubbles (C97).
- **Generation stack:** C85 mark + C89 steps + a C104-like failure is shared by flashcards, revision notes and coach.
- **Side-card family:** C23 (course), C68 (assignment), C74 (session) and the certificate side cards all follow the same "status → facts dl → block CTA(s) → note" order.
- **Row-to-card responsive transform:** used by both C27 and C29, with identical rules (r12 cards, 10px gap, full-width action under a divider).
- **Documents:** C82 (certificate) and C93 (revision notes) are both print/download-oriented documents with a matching skeleton.
- **Cross-product sources:**
  - C75 Calendar and C36 View Switch come from `designs/instructor/code/live-sessions-overview.html`.
  - C82 Certificate Document matches `designs/admin/code/certificate-templates.html .certificate-preview`.
  - The certificate pill colours match the admin "Issued certificates" table (per file comments).

---

## 28. Learner UI vs UpSpace Design System

### 28.1 Learner UI language (recurring conventions, not evaluated)

| Convention | As built |
|---|---|
| **Canvas and surfaces** | `#fafafa` page; **white** cards, panels, inputs, dropdowns and modals; `#f5f5f5` for table headers, icon tiles, hover and stage backgrounds; `#e5e5e5` for tab tracks, progress tracks and disabled buttons |
| **Borders over shadows** | `1px #e5e5e5` on nearly every container; hover darkens borders to `#a3a3a3`; shadows only on floating layers (tabs pill, dropdowns, popover, modal, toast, drawers) |
| **Radius rhythm** | 6 (tab pills, menu items, small buttons) · 8 (buttons, inputs, alerts, file rows) · 12 (cards, tables, rows, modals) · 16 (hero and large panels, player stage, composer (coach), flashcard) · 999 (pills, chips) |
| **Type hierarchy** | Page H1 28px/700/-.6 (list) or fluid clamp up to 30–38 (detail); section H2 17–20/700; card title 15–16/600–700; body 14–15; meta 12.5–13.5 in `#a3a3a3`; uppercase 12px/700/.06em eyebrow labels; negative tracking on everything ≥17px; tabular numerals on all figures |
| **Text colors** | Primary `#171717`; strong `#404040` (secondary button text, prose, dd values); secondary `#525252` (subtitles, meta that matters); tertiary `#a3a3a3` (meta, labels, placeholders); disabled `#d4d4d4` |
| **Brand usage** | Indigo `#4f46e5` for primary buttons, links, progress fills, active/selected states (`#eef2ff` bg), eyebrows and AI identity. **Info blue** `#2563eb` is used for the sidebar active item and certificate links |
| **Status color** | Color only where it carries meaning: red = overdue/cancelled/error; green = completed/graded/live/valid; amber = mandatory/expired/focus areas/warnings; grey = submitted/pending/completed-past; brand = in progress/soon |
| **Button hierarchy** | One primary per region; secondary white bordered; ghost for tertiary; red for destructive; block-width buttons in side cards; lg (44–48) for hero and side-card CTAs; icons left of the label (arrow on the right for "go" actions) |
| **Action placement** | List rows: action right-aligned (mobile: under a divider). Detail pages: primary CTA in the side card. Forms: footer with status on the left, actions on the right. Dialogs: Cancel then Confirm, right-aligned |
| **Spacing rhythm** | Page gutters `clamp(20px,2.6vw,48px)`; sections 40px apart; stacked cards 20px apart; card padding 18–24px; rows 16px×20px; tight inline gaps 6–10px |
| **Density** | Comfortable: 40–44px controls, 42px search/select, 15px body in content areas |
| **Icons** | Lucide-style inline SVG, stroke 2, round caps/joins, `currentColor`; 16px in buttons, 18–20px in nav/controls, 13–15px in meta; `#a3a3a3` for decorative, inherited for actionable |
| **Imagery** | 16:9 course photos with a glass tag overlay; zoom on hover; greyscale when completed |
| **Page headers** | List: H1 + purpose sentence (+ search right). Detail: breadcrumbs → status/eyebrow → H1 → context line |
| **Tables/lists** | Grey header strip, 1px row dividers, whole-row click, hover `#fafafa`, title turns brand on hover, relative dates under absolute dates, status as dot labels; collapse to cards on mobile |
| **Empty-state style** | Centred, bold sentence + one plain sentence, ≤1 action, no illustration (except the first-time dashboard and the certificates icon) |
| **Loading style** | Layout-shaped shimmer skeletons, never spinners (spinners only inside busy buttons and generation steps) |
| **Modal sizing** | 420 (confirm/scanner), 680 (task dialog); sheets 440; drawers 260/384 |
| **AI identity** | Indigo gradient mark, sparkle icon, explicit grounding statement, visible generation steps, thumbs feedback, explicit "won't guess" declines |
| **Copy tone** | Plain, second person, short: "You're all caught up.", "Nothing was saved. Try again in a moment.", "Join opens 15 minutes before." |
| **Motion** | 0.15s colour transitions; 0.2–0.3s layout/transform with `cubic-bezier(.2,.7,.2,1)`; 0.97–0.98 press scale; everything off under reduced motion |

### 28.2 Token comparison

| Area | UpSpaceDESIGN.md | Learner build | Relationship |
|---|---|---|---|
| Font | DM Sans only, 400/500/600/700 | DM Sans 400–700 (Google Fonts) **+ Georgia serif** (certificate document) **+ ui-monospace** (codes, meeting URL, preview control) | Learner **extends** |
| Text colors | primary `#171717`, secondary `#525252`, tertiary `#a3a3a3`, disabled `#d4d4d4`, inverse `#fff` | Same, **plus `--text-strong #404040`** (DS only has this value as `icon-primary`) used for body/prose/secondary-button text | Additional token |
| Surfaces | canvas `#fafafa`, raised `#f5f5f5` "cards, panels, table headers", overlay `#e5e5e5` "dropdowns, popovers", modal `#d4d4d4` | Canvas same. **Cards are `#fff`**; raised used for table headers/tiles/hover; overlay used for **tab tracks, progress tracks, disabled buttons**; dropdowns/popovers/modals are **white**; `surface-modal` unused | **Different usage** |
| Border | default `#e5e5e5`, subtle `#f5f5f5`, strong `#a3a3a3` | default same; **subtle = `#f0f0f0`** in sidebar, dashboard, my-courses, overview, player, revision-notes (and `#f5f5f5` in the others); strong used as the card hover border; **`--border-popover #d4d4d4`** added | Divergent value + addition |
| Action | primary `#4f46e5`, hover `#4338ca`, pressed `#3730a3`, disabled `#d4d4d4` | primary/hover same; **pressed not used** (a `scale(.97–.98)` press instead); disabled = `#e5e5e5` bg + `#a3a3a3` text, or opacity .45–.75 | Different disabled/pressed treatment |
| Brand tints | brand-subtle `#eef2ff`, brand-border `#c7d2fe` | `--action-primary-subtle #eef2ff` (= brand-subtle) for selected/hover-link; **`--action-primary-soft #e0e7ff`** (not in DS) for sent bubbles, current module, dropper hover, focus-ring halos; `#c7d2fe` only in the illustration | Additional token |
| Feedback | error/warning/success/info × default/subtle/border | Same values; **added `--success-soft #dcfce7`** (toast/featured icon), `#fee2e2` (error featured), darker text shades `#a16207` (expired), `#991b1b` (download error), `#854d0e` (save failed), `#b91c1c` (danger hover), `#1e3a8a` (calendar event) | Extended |
| Info usage | info "not yet applied to any real component" | **Used**: sidebar active item, certificate links, calendar upcoming events | Learner applies an unused token |
| Focus | focus-ring `#6366f1` | `outline:2px solid #6366f1; outline-offset:2px` globally; inputs use border + `0 0 0 3px rgba(99,102,241,.15)` | Extended (halo) |
| Radius | none 0, sm 2, md 4, lg 8, xl 12, 2xl 16, 3xl 24, full 999 | `--radius-sm 4`, **`--radius-md 6`**, lg 8, xl 12, 2xl 16, full 999; 3xl+ unused | **md differs (6 vs 4)**; sm differs (4 vs 2) |
| Spacing | 0/1/2/4/8/12/16/20/24/28/32/40/48/60/72 | Uses many off-scale values (6, 7, 9, 10, 11, 14, 18, 22, 26) and fluid `clamp()` gutters | Different |
| Type scale | Label 16/14/12, Body 18/16/14/12, Heading H6 20 … H1 56, Caption 10/9 | Uses 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 17, 18, 19, 20, 22, 28, 44 + fluid clamps; page H1 28px isn't on the DS scale (between H5 24 and H4 32) | Different |
| Shadows | not defined | 7 distinct shadows (listed in §28.1 and each component) | Learner-defined |
| Dark mode | none | none | Same |

### 28.3 Component comparison

| DS component (UpSpaceDESIGN.md list) | Learner usage | Relationship |
|---|---|---|
| **Buttons** (spec-extracted: sm 36 / md 40 / lg 44 / xl 48, r8, gap 8, icon-only 40) | C14: md 40 ✓, lg 44 ✓, r8 ✓, gap 8 ✓. **Also:** 34px "sm" (not in DS), 36px used as the *default* on certificates/coach (= DS sm), 44px as the *default* on overview/certificate-detail, 48px labelled `-lg` (= DS xl); horizontal padding 12–22px; font 13.5–15px; ghost & danger variants; busy state; icon buttons 30–40px, round and square | **Uses + extends / diverges on sizes** |
| Alerts | C73 (error/warning tints, headline + sentence, optional action) | Uses (values unverified — DS not spec-extracted) |
| Toast | C101 (success only, grey `#f5f5f5` body, green icon circle) | Uses (success variant only) |
| Inputs | C37, C39 (+ leading-icon search, focus halo) | Uses + extends |
| Badges | C49 filled pills; C48 **dot-only label without background** | Uses + extends (dot label) |
| Dropdowns | C88 ⋮ menu (opens upward); C04 profile menu | Uses |
| Video Player | C54 player (+ transcript-synced captions, end card, idle hide); C76 recording | Uses + extends |
| Modals | C99, C77, C91 (large task dialog) | Uses + extends (large dialog) |
| Popover | C72 (anchored, with arrow, confirm-with-summary) | Uses |
| Aside | C87 right sheet | Uses |
| Select | C38 native select, custom chevron | Uses |
| Tables | C27 (+ responsive row→card), C28 rubric | Uses + extends |
| Breadcrumbs | C07 (arrow separator); top-bar breadcrumb uses a different `/` style (C03) | Uses; plus a second, different breadcrumb style |
| Progress Bar | C46 (4/6/8px) | Uses |
| Messaging | C62, C63 | Uses |
| File Dropper | C42 + C33 rows (upload / error / retry / replace) | Uses + extends |
| Tooltip | C66 (`#171717`, hardcoded; the DS flags the missing inverted-surface token) | Uses (hardcoded colour fills the DS gap) |
| Charts, Pagination, Carousel, Radio groups, Sliders, Toggles, Color Picker | **Not used** by any Learner screen | — |

**DS "known gaps" and how Learner fills them (observed, not endorsed):**
- *surface/selected missing* → Learner uses `#eef2ff` for selected lesson, cue, card-list item, current module row and TOC link; white + shadow for the selected tab.
- *Tooltip inverted surface missing* → hardcoded `#171717`.
- *Admin Sidebar background question* → Learner sidebar is `#fff`, not canvas.

### 28.4 Behavior not documented in the DS
Every pattern in §25 (I01–I24) is Learner-defined. The DS documents no interaction behavior beyond colour and state tokens. The ones most specific to Learner:
- auto-save drafts (I12)
- confirm-with-summary popover (I11)
- join-window gating (I18)
- disabled-with-reason availability (I19)
- only-real-actions rule (I20)
- row→card responsive transform
- skeleton-in-place loading (I07)
- AI grounding/decline/step-progress conventions (I16, I17)

---

## 29. Components Missing From the Formal Design System

Learner components/patterns with **no corresponding group** in the UpSpace library or in `UpSpaceDESIGN.md`. Most are logged as approved hand-built in `MISSING_COMPONENTS.md`; the others are marked *(not logged)*.

**Structure & navigation**
- Learner Sidebar (C02) *(the DS only mentions an Admin Sidebar token question)*
- Learner Top Bar (C03) *(not logged)*
- Mobile Drawer (C06) *(not logged)*
- Focused Player Header (C09) *(not logged)*
- Back Link (C08) *(not logged)*
- Page / Detail / Section headers (C10–C13) *(not logged)*

**Selection & disclosure**
- **Segmented Tabs (C35)**, logged
- Calendar View Switch (C36)
- **Accordion (C58)**, logged
- Previous Attempts disclosure (C34) *(not logged)*

**Cards & lists**
- **Course Card (C21)** *(not logged; `design-system-map.json` notes on cards are cited as precedent in `MISSING_COMPONENTS.md`)*
- Continue Hero (C22)
- Course Status Side Card (C23)
- Stat Chip (C24)
- Next Session Block (C25)
- Certificate Card (C26)
- Coming-up Row (C30)
- Due-soon Item (C31)
- Session Row List (C29)
- Assignment Summary Card (C68)
- When & Where Card (C74)

**Status & progress**
- Status Dot Label (C48) *(DS has Badges; the no-fill dot label is a Learner variant)*
- **Date Tile (C51)**, logged
- Progress Ring (C47) *(not logged)*
- Lesson Status Icon Set (C50) *(part of the logged Lesson list item)*
- Image Overlay Tags (C52) *(not logged)*
- Draft Save Indicator (C53) *(not logged)*

**Course player**
- Lesson End Card (C55)
- Lesson Head + Prev/Next (C56)
- Course Content Rail (C57)
- **Lesson List Item (C59)**, logged
- **Transcript Panel (C60)**, logged
- AI Tutor Panel (C61)
- Helpful Rating (C64)
- Jump-to-Timestamp Chip (C65)
- Non-video Placeholder (C67)

**Forms & AI**
- **Rich Text Editor (C41)**, logged
- **Chat Composer (C43)**, logged
- Suggestion Chips (C44)
- Send/Stop buttons (C19)
- AI Mark (C85)
- **AI bottom bar / Ask AI Dock (C86)**, logged
- **AI Generation Progress (C89)**, logged
- **Revision Notes Row (C90)**, logged
- Revision Notes Create Panel (C92)
- **Revision Notes Document (C93)**, logged
- Study Rail Cards (C94)
- **Flashcard (C95)**, logged
- Coach Hero (C96)
- Coach Turn / Grounded Answer (C97)
- **Study Plan Block (C98)**, logged

**Assignment / live / certificate**
- Grade Result Block (C69)
- Instructor Feedback Quote (C70)
- Waiting State Block (C71)
- **Calendar (C75)**, logged
- **QR Check-in Scanner (C77)**, logged
- Result Featured Icon (C78)
- Reminder Note (C79)
- Meeting Link Fallback (C80)
- Location Block (C81)
- **Certificate Document (C82)**, logged
- Verification Code Box (C83)
- Inline Download Error (C84)

**States**
- **Skeleton Loader (C102)**, logged (+ **Document-shaped skeleton**, logged)
- **Empty State (C103)**, logged
- Error State with Retry (C104) *(built on the empty-state block)*
- Not Found State (C105)
- **First-time Illustration (C106)**, logged

---

## 30. Shared vs Learner-Specific Components

### 30.1 Classification rules applied
- **A · Design System Component:** a library group exists **and** the Learner file states it uses that library pattern, with no material Learner-specific additions.
- **B · Learner-Specific Component:** built for and used only in Learner screens (hand-built or bespoke).
- **C · Extended Component:** based on a library group but with Learner-specific variants, behavior or structure.
- **D · Shared Application Component:** explicitly the same pattern as, or reused by, another product area (Admin, Instructor, Course Designer), per file comments or `MISSING_COMPONENTS.md`.
- **E · Learner Page Pattern:** a recurring layout or structural pattern rather than a standalone component.

When something could fit two classes, the primary class is listed and the secondary one is noted.

### 30.2 Full classification

| ID | Component | Class | Note |
|---|---|---|---|
| C01 | Learner App Shell | E | |
| C02 | Learner Sidebar | B | shared across all Learner pages via iframe |
| C03 | Learner Top Bar | B | shared via iframe |
| C04 | Profile Menu Dropdown | C | Dropdowns |
| C05 | Notification Bell (indicator only) | B | no behavior |
| C06 | Mobile Navigation Drawer | E | |
| C07 | In-page Breadcrumbs | A | Breadcrumbs |
| C08 | Back Link | B | |
| C09 | Focused Player Header | B | |
| C10 | List Page Header | E | |
| C11 | Detail Header | E | |
| C12 | Dashboard Greeting | B | |
| C13 | Section Header | E | |
| C14 | Button | A | size deviations (§28.3) |
| C15 | Button Busy / Loading State | C | Buttons |
| C16 | Icon Button family | C | Buttons |
| C17 | Inline Text Action | C | Buttons / link token |
| C18 | Compact Action Buttons | C | Buttons |
| C19 | Send / Stop Round Buttons | B | |
| C20 | Surface Card / Panel | E | |
| C21 | Learner Course Card | B | |
| C22 | Continue Learning Hero | B | 2 implementations |
| C23 | Course Status Side Card | B | |
| C24 | Course Stat Chip | B | |
| C25 | Next Session Block | B | |
| C26 | Certificate Card | B | contains D (C82) |
| C27 | Data Table (Assignments) | C | Tables |
| C28 | Rubric Table | A | Tables |
| C29 | Session Row List | C | Tables (grid rows) |
| C30 | Coming Up List Row | B | |
| C31 | Due Soon List Item | B | |
| C32 | Definition Facts List | E | |
| C33 | File Item Row | C | File Dropper |
| C34 | Previous Attempts Disclosure | B | |
| C35 | Segmented Tabs | B | also reused by Course Designer (secondary D) |
| C36 | Calendar View Switch | D | Instructor |
| C37 | Search Field | C | Inputs |
| C38 | Select | A | Select |
| C39 | Text / URL / Date Input | A | Inputs |
| C40 | Textarea | A | Inputs |
| C41 | Rich Text Editor | B | |
| C42 | File Dropper | A | File Dropper |
| C43 | Chat Composer | B | |
| C44 | Suggestion / Prompt Chips | B | |
| C45 | Filter Toolbar | E | |
| C46 | Linear Progress Bar | A | Progress Bar |
| C47 | Progress Ring | B | |
| C48 | Status Dot Label | C | Badges (dot) |
| C49 | Badge / Status Pill | A | Badges |
| C50 | Lesson Status Icon Set | B | |
| C51 | Date Tile | B | 4 variants |
| C52 | Image Overlay Tags | B | |
| C53 | Draft Save Indicator | B | |
| C54 | Video Player | A | Video Player |
| C55 | Lesson End Card | B | |
| C56 | Lesson Head + Prev/Next | B | |
| C57 | Course Content Rail | B | |
| C58 | Module Accordion | B | |
| C59 | Lesson List Item | B | |
| C60 | Transcript Panel | B | |
| C61 | AI Tutor Panel | B | |
| C62 | Chat Message | A | Messaging |
| C63 | Typing Indicator | A | Messaging |
| C64 | Helpful Rating | B | |
| C65 | Jump-to-Timestamp Chip | B | |
| C66 | Tooltip | A | ToolTip |
| C67 | Non-video Lesson Placeholder | B | mock placeholder |
| C68 | Assignment Summary Side Card | B | |
| C69 | Grade Result Block | B | |
| C70 | Instructor Feedback Quote | B | |
| C71 | Waiting / Pending State Block | B | |
| C72 | Submit Confirmation Popover | A | Popover |
| C73 | Alert | A | Alerts |
| C74 | Session When & Where Card | B | |
| C75 | Calendar (Day/Week/Month) | D | Instructor |
| C76 | Recording Offer & Inline Player | C | Video Player |
| C77 | QR Check-in Scanner Modal | B | |
| C78 | Result Featured Icon | B | |
| C79 | Reminder Note | B | |
| C80 | Meeting Link Fallback | B | |
| C81 | Location Block | B | |
| C82 | Certificate Document | D | Admin template preview |
| C83 | Verification Code Box | B | |
| C84 | Inline Download Error | B | |
| C85 | AI Mark | B | |
| C86 | Ask AI Dock | B | |
| C87 | Ask AI Side Sheet | C | Aside |
| C88 | Overflow Dropdown Menu | A | Dropdowns |
| C89 | AI Generation Progress | D | Course Designer reuse |
| C90 | Revision Notes Row | B | |
| C91 | Flashcards Dialog | C | Modals |
| C92 | Revision Notes Create Panel | B | |
| C93 | Revision Notes Document | B | |
| C94 | Study Rail Cards | B | |
| C95 | Flashcard | B | |
| C96 | Coach Empty Hero | B | |
| C97 | Coach Turn / Grounded Answer | B | |
| C98 | Study Plan Block | B | |
| C99 | Modal Dialog | A | Modals |
| C100 | Backdrop / Scrim | E | |
| C101 | Toast | A | Toast |
| C102 | Skeleton Loader | D | Course Designer reuse |
| C103 | Empty State | D | Course Designer reuse |
| C104 | Error State with Retry | B | |
| C105 | Not Found State | B | |
| C106 | First-time Welcome + Illustration | B | |
| C107 | Preview State Switcher | — | design-only, excluded |

### 30.3 Totals
| Class | Count |
|---|---|
| A · Design System | 18 |
| B · Learner-specific | 60 |
| C · Extended | 13 |
| D · Shared application | 6 |
| E · Learner page pattern | 9 |
| **Total components/patterns** | **106** (+1 design-only switcher excluded) |
| Layout patterns (P1–P8) | 8 |
| Interaction patterns (I01–I24) | 24 |
| Workflows (W01–W14) | 14 |

---

## 31. Unknowns / Areas Requiring Verification

1. **Library values not cross-checked.** Class A/C assignments rely on each Learner file's own "Library: …" claim and on the existence of the group folder. No per-variant values were compared against `components/<Group>/components.json`. The DS doc itself says only Buttons were spec-extracted, so "matches the DS" can only be confirmed for buttons (§28.3).
2. **No assessment-taking UI exists.** It can't be benchmarked. The closest artifact is the Course Designer preview's "learner question render" (`designs/course-designer/code/course-preview.html` `.q` / `.opt`), which was **not inspected**. Reading and quiz lesson content inside the player is a placeholder.
3. **Undefined token in the top bar.** `topnavbar.html` uses `var(--text-disabled)` for the breadcrumb separator but never declares it in its `:root`. The rendered colour (likely inherited `#171717`) was not verified visually.
4. **Non-functional chrome:**
   - Top-bar search has no handler.
   - The notification bell has no panel.
   - Profile menu items and sidebar Settings point to `#`.
   - Profile menu `aria-expanded` never updates.
5. **Inconsistent learner identity across mocks:** the top-bar avatar says "SC", the dashboard says "Sophia", and certificates say "Samira Collins". Recorded as-is.
6. **Stale comment:** the `sidebar.html` header says only Dashboard is linked. That is no longer true.
7. **Player data scope:** only CS-301 has outline data, and any `?id=` shows CS-301 (file comment). Behavior for other courses is unknown.
8. **Spec conformance not verified against `src/`.** Per CLAUDE.md Rules 2/5, these deviations and interpretations recorded **in the code comments** are listed, not resolved:
   - Course cards go to the overview instead of the player — "deviates from CDL-001-FR-04" (user decision).
   - Ask AI on the course overview is "undocumented — AI-006 only defines the tutor inside the player".
   - Coach answering content questions "overlaps AI-006"; AI-013 describes a goal/check-in coach.
   - Assignment overdue rule is an "interpretation of a spec conflict" (user decision).
   - Revoked certificates are shown to the learner (user decision).
   - "Got it / Still learning" (AI-007-FR-05) not built (user decision).
   - Lesson "moving next marks complete" is a mock rule pending CDL-004.
9. **Mocked behavior:**
   - Video playback, uploads, AI replies, join hand-off, QR scanning and PDF generation are all simulated.
   - Real timing, error codes and platform behavior are unknown.
   - The fixed mock date is `2026-09-23`.
10. **Visual rendering not checked in a browser.** All values come from source. Effective sizes of `clamp()` values depend on viewport, and no screenshots were taken.
11. **Which size is canonical is unknown.** Buttons (34/36/40/44/48 defaults), `--border-subtle` (`#f0f0f0` vs `#f5f5f5`), skeleton colours and date-tile sizes vary by file. This document records each variant, and Phase 2 will need a decision on which is the benchmark.
12. **Accessibility beyond what was observed:**
    - No focus traps in modals, sheets or drawers.
    - No Escape key on the mobile drawer or the profile menu.
    - Tooltips are hover-only.
    - Keyboard support exists where noted (§25 I22).
    - No audit was run.
13. **`verify-certificate.html`** (other-pages) is linked from the certificate detail but was not inspected.
14. **Course card "Certificate" label** is a `<span>` inside the card link, so clicking it opens the course overview, not the certificate. Recorded as observed behavior.
15. **Dashboard "Coming up" merges assignments and sessions** from mock data mirrored from sibling pages. How the real merge and sort would work is unknown beyond "soonest first, max 4".

