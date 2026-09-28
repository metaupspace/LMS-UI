# Missing Components Log

Components needed by a screen but not found in `Analyze-design-system/UpSpace Design System/components/`. One entry per missing component. Per CLAUDE.md rule 8: wait for explicit permission before building any of these as new components — hand-authored fallback markup is fine to keep using in the meantime (existing project precedent, see design-system-map.json notes on cards).

- [ ] **Multi-step wizard / stepper nav** — needed by `designs/instructor/code/assessment-editor.html` (3-step assessment authoring flow: Target & Deadlines → Rules & Timing → Question Selection). No `Stepper`/`Wizard` group exists in the 24 component groups. Continuing to hand-author this pattern (consistent with existing card-pattern precedent) using library colors/type/icons — not requesting a new Figma component for it.
- [x] **Accordion (module outline)** — needed by `designs/Learner/code/course-overview.html` (CDL-002-FR-02 expandable module/lesson outline) and the module list in `designs/Learner/code/course-player.html`. No Accordion/Collapse group in library. — built HTML-only, approved 2026-09-23.
- [x] **Lesson list item (with status: not started / in progress / completed / locked)** — needed by `designs/Learner/code/course-player.html` sidebar (CDL-003-FR-02, FR-06) and `course-overview.html` outline (completed lessons marked). Not in library. — built HTML-only, approved 2026-09-23.
- [x] **Transcript panel (timestamped lines, active-line highlight, click-to-seek)** — needed by `designs/Learner/code/course-player.html` below the video (CDL-003-NFR-03). Not in library. — built HTML-only, approved 2026-09-23.
- [x] **Tabs (segmented / underline)** — needed by `designs/Learner/code/course-player.html` to switch Transcript / AI Tutor below the video. No Tabs group in library (my-courses.html status tabs are already hand-authored). — built HTML-only, approved 2026-09-23.
- [x] **Chat composer (message input + send, suggested prompts)** — needed by AI Tutor panel in `course-player.html` and Ask-AI box in `course-overview.html`. Library has `Textarea input field` + `Buttons` but no composed chat composer; will compose from those two if approved. — built HTML-only, approved 2026-09-23.
- [x] **AI bottom bar (floating composer: sparkle pill → input → thinking → answer card, ⋮ menu)** — needed by `designs/Learner/code/course-overview.html` Ask AI (Google Docs–style, user reference in `designs/instructor/inspo/Screenshot 2026-09-23 at 5.39–5.40 PM`). Not in library. Built HTML-only on explicit user request 2026-09-23; ⋮ menu reuses Dropdown menu pattern, side sheet reuses Aside (Right).
- [x] **Rich text editor (toolbar: bold, italic, lists, link + editable area)** — needed by `designs/Learner/code/assignment-detail.html` written response (ASM-005-FR-06 "rich text editor"). Library has `Textarea input field` only. — built HTML-only, approved 2026-09-23.
- [x] **Skeleton loader (list rows + detail blocks)** — needed by `designs/Learner/code/assignments.html` and `assignment-detail.html` loading states. Not in library (earlier learner screens hand-author skeletons without logging). — built HTML-only, approved 2026-09-23.
- [x] **Empty state block (title + one-line description, optional action)** — needed by `assignments.html` (no assignments / no filter results) and `assignment-detail.html` (nothing submitted / no feedback released). Not in library. — built HTML-only, approved 2026-09-23.
- [x] **Tabs (segmented filter)** — reused on `assignments.html` status filter (All / To do / Submitted / Graded / Overdue). Same hand-built pattern already approved for `course-player.html` above. — built HTML-only, approved 2026-09-23.
- [x] **Calendar — Day / Week / Month** (now reuses the existing pattern from `designs/instructor/code/live-sessions-overview.html`, user request 2026-09-23; replaced the earlier compact and Google-style versions) — needed by `designs/Learner/code/live-sessions.html` Calendar view (LSN-002-FR-01). Not in library. List stays the default view. — built HTML-only, approved 2026-09-23.
- [x] **Date tile (month + day block)** — needed by `live-sessions.html` rows and `live-session-detail.html` header. Not in library (same hand-built pattern already used in `my-courses.html` Due soon panel, never logged until now). — built HTML-only, approved 2026-09-23.
- [x] **QR check-in scanner (camera viewfinder + result state)** — needed by `live-session-detail.html` for in-person sessions with QR attendance (LSN-004-FR-02, learner side). Not in library. — built HTML-only, approved 2026-09-23.
- [x] **Certificate document (rendered issued certificate: paper, frame, template title, learner, course, org, dates, verification code)** — needed by `designs/Learner/code/certificates.html` (card previews) and `certificate-detail.html` (full view). Not in library; reuses the existing hand-built `.certificate-preview` pattern from `designs/admin/code/certificate-templates.html` so learner and admin show the same template design. — built HTML-only, approved 2026-09-23.
- [x] **Document-shaped skeleton** — needed by `certificates.html` / `certificate-detail.html` loading states. Not in library (extends the approved Skeleton loader). — built HTML-only, approved 2026-09-23.

### Learner AI study tools — logged 2026-09-23, built HTML-only (approved 2026-09-23)
Restructured on user request 2026-09-23: sidebar item **Your Coach** (`designs/Learner/code/coach.html`, single chat box); Revision notes per module and Flashcards per course live inside `course-overview.html`; `revision-notes.html?course=&mod=` and `flashcard-study.html?course=` are their own flows. Reused as-is: Select, Textarea/Input field, Buttons, Badges, Modal, Toast, Progress bar, Message. Also reused approved hand-built: Chat composer, Empty state, Date tile.
- [x] **AI generation progress (titled step list)** — `revision-notes.html`, course-overview Flashcards section, `coach.html`. — built HTML-only, approved 2026-09-23.
- [x] **Revision notes document (takeaways, focus areas, definitions, examples, sources; prints to PDF)** — `revision-notes.html`. — built HTML-only, approved 2026-09-23.
- [x] **Revision notes row (per module, in the course outline accordion)** — `course-overview.html`. Replaces the earlier "Recent activity row". — built HTML-only, approved 2026-09-23.
- [x] **Flashcard (two-sided flip card)** — `flashcard-study.html`. — built HTML-only, approved 2026-09-23.
- [x] **Study plan block** — `coach.html` plan answers. — built HTML-only, approved 2026-09-23.
- [ ] ~~AI tool entry card~~ — dropped, the AI Learning home page was removed.
- [ ] ~~Flashcard review/edit list~~ — not built (user decision: edit-before-save out of scope).

### Learner dashboard simplification — logged 2026-09-24
- [x] **First-time learner illustration (inline SVG spot illustration)** — `designs/Learner/code/dashboard.html` first-time state. Not in library (no illustration/artwork group). Uses library colors only. — built HTML-only, approved 2026-09-24 (user asked for an illustration).

### Course Designer — My Courses + Course Builder — logged 2026-09-24
Screens: `designs/course-designer/code/my-courses.html`, `ai-course-generate.html`, `course-builder.html` (CRS-001/002/003/004, AI-001). Reused as-is from library: Table, Badge, Buttons, Input field, Textarea, Select, Dropdown menu (row "More"), Modal, Radio group (Icon card — creation choice), File Dropper (stack + filled/overflow), Alerts, Toast, Progress bar, Tooltip. Reused approved hand-built: Tabs (segmented), Empty state, Skeleton loader, Rich text editor, AI generation progress (step list).
- [x] **Course structure tree (modules → lessons outline: expand/collapse, add, rename, delete, drag-to-reorder, per-lesson AI-generated marker + empty-lesson state)** — `course-builder.html` left panel (CRS-003-FR-01, CRS-004-FR-06). Not in library. — built HTML-only, approved 2026-09-24.

### Course Builder v2 — block-based authoring — logged 2026-09-24
Screens: `designs/course-designer/code/course-builder.html` (rebuilt), `course-preview.html` (new, CRS-005), plus data-model updates in `my-courses.html` / `ai-course-generate.html`. Reused as-is from library: Video player (+ _Play button, _Video progress), Slider (audio progress/volume), Toggle (playback settings), Aside (right properties panel), Modal, Dropdown menu, Select, Input field, Textarea, File Dropper, Radio group, Badge, Alerts, Toast, Progress bar, Tooltip. Reused approved hand-built: Rich text editor, Tabs, Empty state, Skeleton, Course structure tree, Accordion + Lesson list item (preview), AI generation progress. Reused existing screen pattern: question editor (`instructor/code/assessment-editor.html` .question-unit / .option-item).
- [x] **Content block frame (hover toolbar: drag, move, duplicate, AI, ⋯; selected state)** — builder canvas. — built HTML-only, approved 2026-09-24.
- [x] **Insertion point ("+ Add content" between blocks, drop indicator line)** — builder canvas. — built HTML-only, approved 2026-09-24.
- [x] **Content picker (categorized, draggable block palette) + "/" quick-insert menu** — builder. — built HTML-only, approved 2026-09-24.
- [x] **Content Library browser (modal: upload new / choose from library grid, search, type filter)** — builder media blocks (CRS-009-FR-01/07). — built HTML-only, approved 2026-09-24.
- [x] **Upload status row (uploading %, processing, ready, failed, unsupported)** — media blocks (CRS-003-NFR-04). — built HTML-only, approved 2026-09-24.
- [x] **Image figure block (image + caption + alignment)** — builder + preview. — built HTML-only, approved 2026-09-24.
- [x] **Audio player (play/pause, progress, duration, volume, title, transcript)** — builder + preview. — built HTML-only, approved 2026-09-24.
- [x] **Document viewer block (inline PDF preview, open full screen, download; fallback card for PPTX/DOCX)** — builder + preview. — built HTML-only, approved 2026-09-24.
- [x] **Embed block (URL / embed code input, sandboxed preview, invalid + blocked states)** — builder + preview. — built HTML-only, approved 2026-09-24.
- [x] **Code block (language select, syntax highlighting, copy, title, explanation)** — builder + preview. — built HTML-only, approved 2026-09-24.
- [x] **File download block (name, type, size, download)** — builder + preview. — built HTML-only, approved 2026-09-24.
- [x] **Callout block (Note / Tip / Important / Warning / Example)** — builder + preview. — built HTML-only, approved 2026-09-24.
- [x] **Quote / Example / Key takeaway block** — builder + preview. — built HTML-only, approved 2026-09-24.
- [x] **Assessment summary block (title, type, questions, duration, pass mark, status, Edit)** — builder + preview. — built HTML-only, approved 2026-09-24.

### Course Designer — Question Bank (ASM-003, AI-002) — logged 2026-09-24
Screens: `designs/course-designer/code/question-bank.html` (list, filters, detail, editor, preview), `question-bank-ai.html` (AI generate + review), `question-bank-import.html` (CSV/XLSX import + review), plus bank picker / "Save to Question Bank" in `course-builder.html`. Reused as-is from library: Table, Pagination, Input field, Textarea, Select, Dropdown menu, Modal, Aside, Buttons, Badge / Badge group, File Dropper, Radio group (Icon card — question type), Popover (usage list), Alerts, Toast, Tooltip, Toggle. Reused approved hand-built: Tabs, Empty state, Skeleton, AI generation progress (step list), Content Library browser, Image figure, question editor pattern (`.question-unit` / `.option-item`), learner question render (`course-preview.html` `.q` / `.opt`).
- [x] **Tag input (chips + typeahead of existing org tags + "Create tag" + remove)** — bank editor, AI review, import fix. — built HTML-only, approved 2026-09-24.
- [x] **Checkbox (row select, select-all visible with indeterminate state)** — bank picker in builder, AI review, import review. Library has none (builder used a bare native checkbox). — built HTML-only, approved 2026-09-24.
- [x] **Question answer-key view (read-only options with correct markers, accepted answers, rubric, explanation)** — bank question detail drawer. — built HTML-only, approved 2026-09-24.
- [x] **Fill-in-the-blank blank marker ("Insert blank" + inline highlighted blank preview)** — question editor. — built HTML-only, approved 2026-09-24.
- [x] **AI generated question review item (select, collapse/expand to edit, source excerpt, Regenerate / Delete, AI generated marker)** — `question-bank-ai.html`. — built HTML-only, approved 2026-09-24.
- [x] **Import validation row (row #, status Valid / Needs attention / Possible duplicate, inline error list, Fix / Skip)** — `question-bank-import.html`. — built HTML-only, approved 2026-09-24.

### Manager — Approvals (CRS-013, CRS-014, ASM-004, WRK-001) — logged 2026-09-28
Screen: `designs/Manager/code/approvals.html` (queue, search/filter, course & assessment read-only detail review, workflow pipeline, decision dialogs). Reused as-is from library: Table, Pagination, Input field, Textarea, Select, Dropdown menu, Modal, Aside, Buttons, Badge / Badge group, Alerts, Toast, Tooltip, Progress bar. Reused approved hand-built: Tabs (segmented), Empty state, Skeleton loader, Accordion (module outline), Question answer-key view.
- [x] **Approval visual workflow pipeline & decision history log (multi-step progress timeline: completed steps with approver/timestamp/comments, active step highlighted with waiting time, remaining steps, and chronological decision audit log)** — `approvals.html` detail panel & workflow view. Not in library. — built HTML-only, approved 2026-09-28.

### Manager — Team Performance (RPT-002, RPT-005) — logged 2026-09-28
Screen: `designs/Manager/code/team-performance.html` (end-of-day summary, team KPIs, animated performance trend chart, individual learner table, dedicated learner detail page link). Reused as-is from library: Table, Input field, Select, Dropdown menu, Aside, Buttons, Badge / Badge group, Alerts, Toast, Tooltip, Progress bar. Reused approved hand-built: Tabs (segmented), Empty state, Skeleton loader.
- [x] **Animated SVG Performance Chart (Data-driven time-series line/area graph with SVG path load animation, interactive hover tooltips, time-range toggles, reduced-motion accessibility support)** — `team-performance.html`. Not in library. — built HTML-only, approved 2026-09-28.

### Manager — Learner Performance Detail (RPT-002, USR-002) — logged 2026-09-28
Screen: `designs/Manager/code/learner-detail.html` (dedicated full-page learner performance workspace: hero profile card, learning track progress, enrolled courses breakdown, assignments & assessments audit, activity timeline, risk flags, certificates). Reused as-is from library: Table, Input field, Select, Dropdown menu, Buttons, Badge / Badge group, Alerts, Toast, Tooltip, Progress bar. Reused approved hand-built: Tabs (segmented), Empty state, Skeleton loader, Activity timeline.

### Manager — Assessments & Assessment Detail (ASM-001, ASM-002, RPT-002, GRD-001) — logged 2026-09-28
Screens: `designs/Manager/code/assessments.html` (manager assessment workspace: KPIs, trend chart, needs attention callouts, assessment performance table) & `designs/Manager/code/assessment-detail.html` (dedicated assessment detail workspace: assessment metadata, performance summary, score distribution histogram, attempts analysis, question accuracy, concept mastery, learner submissions table). Reused as-is from library: Table, Input field, Select, Dropdown menu, Buttons, Badge / Badge group, Alerts, Toast, Tooltip, Progress bar. Reused approved hand-built: Animated SVG Performance Chart, Tabs (segmented), Empty state, Skeleton loader.
- [x] **Score Distribution Histogram & Concept Mastery Breakdown (Grade bucket visual distribution bar graph, question accuracy breakdown with struggling/mastered thresholds, subjective pending grading alert module)** — `assessment-detail.html`. Not in library. — built HTML-only.




