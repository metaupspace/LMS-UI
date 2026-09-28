# Admin UI Consistency Audit

Scope: `designs/admin/code/*.html` (19 screens) vs `UpSpaceDESIGN.md` tokens and `dashboard.html` (canonical reference screen). Survey-level pass — repeated cross-file drift only, not a full per-screen review. No HTML edited.

---

## 1. Page Headers ✅ COMPLETED (2026-09-16)

**Issue: three parallel header markup conventions.**
- Canonical (dashboard.html, 8 files match): `<div class="page-head"><h1>Title</h1><div class="sub">...</div></div>` — plain `<h1>`, no class needed.
- Variant A — `.page-header` wrapper + `<h1 class="page-title">` + `<div class="page-sub">`: `api-webhooks.html`, `billing-overview.html`, `concept-mastery-gap-analysis.html`, `course-performance-reports.html`, `export-custom-reports.html`, `learner-reports.html`.
- Variant B — `.header-meta` + `<h1 id="headerTitle">` (id, not class): `integration-detail.html`.
- Change: pick one convention (recommend `.page-head`/bare `<h1>` since it's the majority + matches dashboard.html) and align the other 7 files' wrapper/element names to it. Don't restructure content, just rename wrapper classes/element.

**Issue: `.page-title` itself has two different font sizes under the same class name.**
- 22px/700 (`api-webhooks.html`, `billing-overview.html`) vs 32px/700/-0.4px (`concept-mastery-gap-analysis.html`, `course-performance-reports.html`, `export-custom-reports.html`, `learner-reports.html`) — matches dashboard.html's `.page-head h1` (32px/700/-.4px).
- Change: bump `.page-title` in `api-webhooks.html` and `billing-overview.html` to 32px/700/-0.4px.
- Also `.page-sub` color differs: `text-secondary` (`api-webhooks.html`) vs `text-tertiary` (rest) — align to `text-tertiary`.

**Issue: detail-page back-navigation uses two different components.**
- `.back-link`: `user-detail.html`, `role-detail.html`.
- `.breadcrumb`: `integration-detail.html`.
- Change: pick one (majority = `.back-link`) and convert `integration-detail.html`.

Not flagged: `workflow-create.html`/`workflow-detail.html` have no page-header row at all — canvas/builder layout, structurally different, likely intentional.

**Fix applied**: Renamed `.page-header`→`.page-head`, `<h1 class="page-title">`→bare `<h1>`, `.page-sub`→`.sub` in `api-webhooks.html`, `billing-overview.html`, `concept-mastery-gap-analysis.html`, `course-performance-reports.html`, `export-custom-reports.html`, `learner-reports.html` (incl. `api-webhooks.html`/`billing-overview.html`'s font-size bump to 32px/700/-0.4px and `api-webhooks.html`'s `.sub` color fix to `text-tertiary`). No JS/id references were affected (verified no scripts target these classes; `learner-reports.html`'s `id="orgPageHeader"` preserved).
**Not converted**: `integration-detail.html`'s `.header-meta`/`.breadcrumb` were assessed but left as-is — on inspection this is a different component (`.detail-header-card`: avatar + title + status badge + actions, comparable to `user-detail.html`'s own separate `.profile-head` pattern), not a plain page-head, and its `.breadcrumb` shows a dynamic provider name (`#bcProviderName`) that a single `.back-link` anchor can't represent without dropping content. Renaming would be cosmetic-only or would require restructuring, so flagging instead of forcing a fit.

---

## 2. Typography

**Issue: heavy use of inline `style="font-size:...; font-weight:..."` instead of shared heading/label classes**, meaning the same visual role (panel title, stat label, etc.) renders at ad-hoc sizes per file instead of the `.panel-head h2` / `.kpi-title span` pattern dashboard.html defines.
- Worst offenders (inline font-size occurrences): `export-custom-reports.html` (25), `workflow-detail.html` (20), `learner-reports.html` (19), `workflow-list.html` (13), `billing-overview.html` (14), `concept-mastery-gap-analysis.html` (6), `integration-detail.html` (7).
- Example: `workflow-detail.html:421,520` — `<h2 style="font-size:20px; font-weight:700; margin:0 0 4px;">` instead of a `.panel-head h2` class.
- Change: for each inline-styled heading/label, replace with the matching existing class from that file's own `.panel-head`/`.list-card-head`/`.card-box-header` rule (most files already have one defined — the drift is call-site inline overrides, not missing CSS). No new classes needed, just apply the ones already in the `<style>` block.

---

## 3. Buttons ✅ COMPLETED (2026-09-16)

**Issue: base `.btn` height has three different values across files (design system spec is 36/40/44/48px — none match exactly).**
- 34px: `api-webhooks.html`, `role-detail.html`, `roles.html`, `workflow-create.html`, `workflow-detail.html`.
- 38px (majority — 13 files): `certificate-templates.html`, `certificates-overview.html`, `community-moderation.html`, `concept-mastery-gap-analysis.html`, `course-performance-reports.html`, `export-custom-reports.html`, `integration-detail.html`, `integrations-catalog.html`, `invite-users.html`, `learner-reports.html`, `user-detail.html`, `user-management.html`, `workflow-list.html`.
- 36px (matches `component.button-sm` spec exactly): `billing-overview.html` only.
- Change: standardize base `.btn` to the 38px/height, `padding:0 16px`, `font-size:13.5px` block (already the majority — copy it verbatim into the 5 files at 34px and into `billing-overview.html`). Font-size on the 34px files is also 13px vs 13.5px elsewhere — same fix covers it.

Not flagged: `.btn-primary/-secondary/-danger/-ghost` color variants are already consistent by name across all 19 files — good, no change needed there.

**Fix applied**: `api-webhooks.html`, `workflow-create.html`, `workflow-detail.html`, `billing-overview.html` — base `.btn` updated to `height:38px; padding:0 16px; font-size:13.5px`. `role-detail.html` and `roles.html` were re-checked and found already at 38px/16px/13.5px (audit was stale for these two — no edit needed).

---

## 4. Cards ✅ COMPLETED (2026-09-16)

**Issue: same visual card component (white bg, `border-default`, `radius-xl`) uses three different class names.**
- `.card` (majority, 8+ files incl. dashboard.html): `community-moderation.html`, `concept-mastery-gap-analysis.html`, `course-performance-reports.html`, `integrations-catalog.html`, `invite-users.html`, `role-detail.html`, `roles.html`, `user-detail.html`, `user-management.html`.
- `.panel`: `billing-overview.html`.
- `.card-box`: `export-custom-reports.html`, `learner-reports.html`.
- Change: rename `.panel`→`.card` in `billing-overview.html` and `.card-box`→`.card` in `export-custom-reports.html`/`learner-reports.html` (CSS block is otherwise identical — pure rename + update call sites).

**Issue (spacing): card padding drifts.** Dashboard canonical is `22px 24px`. `course-performance-reports.html` uses `20px 22px`; `billing-overview.html`'s `.panel` uses flat `24px`; `user-management.html`'s `.card` uses `20px`.
- Change: normalize all to `22px 24px`.

**Fix applied**: Renamed `.panel` → `.card` in `billing-overview.html` and `.card-box` → `.card` in `export-custom-reports.html`. Normalized card padding across affected screens (`billing-overview.html`, `course-performance-reports.html`, `user-management.html`, `export-custom-reports.html`) to the canonical `22px 24px`.

---

## 5. Badges / Status Pills ✅ COMPLETED (2026-09-16)

**Issue: same "colored status pill" concept implemented as three unrelated component systems.**
- `.pill` + modifier (`.up/.down/.warn/.info/.danger/.neutral/...`) — canonical, dashboard.html + most report/analytics screens (`concept-mastery-gap-analysis.html`, `course-performance-reports.html`, `export-custom-reports.html`, `learner-reports.html`, `billing-overview.html`, `certificate-templates.html`).
- `.badge` + `.badge-success/-warning/-error/-gray/-purple/-indigo` — `api-webhooks.html`, `integration-detail.html`, `integrations-catalog.html`, `workflow-create.html`, `workflow-detail.html`.
- `.status-badge` + `.status-badge active/deactivated/pending` — `user-detail.html`, `user-management.html`, `workflow-list.html`.
- Change: consolidate to one component (recommend `.pill`, it's dashboard.html's canonical name) with a shared modifier vocabulary; re-map `.badge-*`/`.status-badge` call sites to `.pill` + equivalent state modifier in the 8 affected files.

**Issue: `.role-badge` modifier convention differs between the two files that use it.**
- `user-detail.html`: `.role-badge.tag-0`, `.tag-1`… (numeric index).
- `workflow-list.html`: `.role-badge.tag-blue`, `.tag-gray`… (color name).
- Change: pick one scheme (color-name is more self-documenting) and convert `user-detail.html`.

Not flagged: `.certificate-pill` (`certificate-templates.html`, `certificates-overview.html`) and `.count-badge` (5 files) are module-specific/consistent internally — leave as-is.

**Fix applied**: Re-mapped all `.badge`/`.badge-*` and `.status-badge`/`.status-badge.*` call sites (CSS + static HTML + JS template strings) to `.pill` + modifier in `api-webhooks.html`, `integration-detail.html`, `integrations-catalog.html`, `workflow-create.html`, `workflow-detail.html`, `user-detail.html`, `user-management.html`, `workflow-list.html`. Color values were carried over unchanged (`success`→`up`, `error`→`danger`, `warning`→`warn`, `gray`→`neutral`, `indigo`/`brand`→`purple`); unused modifier definitions were dropped rather than carried forward as dead CSS. `user-detail.html`'s `.role-badge.tag-0/tag-1` converted to `.tag-purple`/`.tag-blue` (same colors, matching `workflow-list.html`'s scheme).
**Judgment call**: `user-management.html`'s status pill modifier suffixes (`active`/`deactivated`/`pending`) were **kept as-is** rather than remapped to `up`/`danger`/`warn` — that file drives the class dynamically from a real data field (`u.status`, also used in `===` business-logic checks for reactivate/deactivate), so remapping the modifier name would require touching data/logic beyond a CSS rename. Only the wrapper (`.status-badge`→`.pill`) was renamed there.

---

## 6. Tables ✅ COMPLETED (2026-09-16)

**Issue: table wrapper class name differs by file for the same structure (bordered box + header row + zebra rows).**
- `.table-wrap`: `certificate-templates.html`, `certificates-overview.html`, `community-moderation.html`, `invite-users.html`, `roles.html`, `user-management.html`, `workflow-list.html`.
- `.table-box` + `.table-container`: `concept-mastery-gap-analysis.html`, `course-performance-reports.html`, `export-custom-reports.html`, `learner-reports.html`, `billing-overview.html` (`.table-box` only).
- `.data-table`: `api-webhooks.html`, `integration-detail.html`.
- Change: standardize on one name (`.table-wrap` is the plurality) across all three groups. Verify each file's actual column/row CSS is equivalent before a pure rename (a couple may need the wrapper CSS block copied over, not just renamed, if `.table-box`/`.data-table` diverge structurally).

**Fix applied**: `.data-table` → `.table-wrap` in `api-webhooks.html`/`integration-detail.html` (single-level, applied directly to the `<table>`, no outer wrapper existed). `.table-container` (outer scroll div) → `.table-wrap` in `concept-mastery-gap-analysis.html`, `course-performance-reports.html`, `export-custom-reports.html`, `learner-reports.html`, matching the canonical outer-wrapper name/purpose exactly.
**Correction made mid-fix**: initially renamed `.table-box` (the class scoping `th`/`td` styling on the `<table>` element itself) to `.table-wrap` too — but since the outer div and the table share the same class name when nested, that caused their CSS rules to bleed into each other (e.g. the wrapper's `margin-inline:-24px` would double-apply to the table, breaking layout). Reverted: the outer div is `.table-wrap`, the table element keeps its own `.table-box` class, exactly as before — only the *outer* wrapper name changed. `billing-overview.html` (no outer div, `.table-box` applied directly to `<table>`) was renamed straight to `.table-wrap` with no such conflict.

---

## 7. Filters / Search Bars ✅ COMPLETED (2026-09-16)

**Issue: five different class names for the same search-input-with-icon component.**
- `.search-box`: `community-moderation.html`, `integrations-catalog.html`, `user-management.html`, `workflow-list.html`.
- `.search-input-wrap` (the pattern already fixed on `course-performance-reports.html` last session — treat as canonical going forward): `course-performance-reports.html`, `learner-reports.html`.
- `.search-bar`: `billing-overview.html`.
- `.search`: `certificates-overview.html`.
- `.certificate-search`: `certificate-templates.html` (module-scoped, acceptable).
- Change: roll the `course-performance-reports.html` search-bar fix (icon-wrapped input, `.search-input-wrap`) out to the other 6 generic files instead of inventing a 6th name.

**Fix applied**: `community-moderation.html`, `user-management.html`, `workflow-list.html`, `billing-overview.html` (`.search-box`/`.search-bar`, flex-row technique with border on the wrapper) converted to the canonical `.search-input-wrap` markup/CSS (absolute-positioned icon, border moved onto the input) — same icon SVG, id, and event handlers preserved, only the wrapper's implementation changed. `integrations-catalog.html` was a simpler case (`.search-box` already used the same absolute-icon technique) — pure rename plus folding its separate `.search-input` class into the wrapper's descendant selector. `certificates-overview.html`'s bare `.search` (an unstyled `<input type="search">` with no icon at all) got the fully-built canonical treatment, including the missing search icon; its ids (`template-search`, `issued-search`) have no other JS wiring in this mock, so nothing else was affected. `certificate-templates.html`'s `.certificate-search` left untouched (module-scoped, per audit).

---

## 8. Modals

**Issue: four incompatible modal component systems in active use.**
1. `.modal-backdrop` / `.modal-card` / `.modal-head` / `.modal-body` / `.modal-foot` / `.modal-close` / `.modal-btn` + `.modal-btn-primary/-secondary/-danger` — the majority pattern: `api-webhooks.html`, `billing-overview.html`, `concept-mastery-gap-analysis.html`, `export-custom-reports.html`, `learner-reports.html`, `workflow-create.html`, `workflow-detail.html`, `workflow-list.html`.
2. `.modal-overlay` / `.modal` / `.modal-actions` (footer buttons reuse plain `.btn`, no `.modal-btn-*`): `community-moderation.html`, `role-detail.html`, `roles.html`, `user-detail.html`, `user-management.html`.
3. `.modal-backdrop` / `.modal-content` (not `.modal-card`) / `.modal-title` / `.modal-desc` / `.modal-btn`: `integration-detail.html`, `integrations-catalog.html`.
4. `.certificate-modal-backdrop` / `.certificate-modal` / `.certificate-modal-head/-foot`: `certificate-templates.html`, `certificates-overview.html` (module-namespaced, internally consistent — lower priority).
- Change: pick system 1 (majority) as canonical and re-skin systems 2 and 3's markup/class names to match (backdrop → card → head/body/foot → close/action buttons). This is the largest structural fix in this audit — do it as its own pass, one file at a time, verifying open/close JS still targets the right selectors after rename.

---

## 9. Empty / Loading States

**Issue: no shared empty-state component; most screens have none at all.** Only 4 of 19 files handle an empty result at all:
- `.table-empty-row`: `api-webhooks.html`, `billing-overview.html`.
- `.empty-state` (+ file-specific `.aa-empty-note`): `community-moderation.html`, `learner-reports.html`.
- Change: define one `.empty-state` pattern (icon + message, matching `learner-reports.html`'s existing implementation as the fuller of the two) and add it to list/table screens that currently show nothing when a filter/search yields zero rows — a gap, not just a naming clash. Given the volume, treat this as follow-up scope rather than a single mechanical rename.

**Loading states**: no `.skeleton`/`.spinner`/`.loading` class found in any file — no pattern exists yet anywhere. Not an inconsistency (nothing to reconcile), but flagging as a known gap since the category was in scope.

---

## Not flagged (already consistent, no action needed)
- Design tokens (`--text-*`, `--surface-*`, `--action-primary`, `--radius-*`) are used consistently via CSS custom properties across all files — no color/radius drift found.
- `.btn-primary/-secondary/-danger/-ghost` naming and semantics.
- `.form-group` / `.form-label` — consistent everywhere a real form exists.
- `.count-badge`, `.certificate-pill`, `.certificate-search` — module-scoped, internally consistent.

## Suggested fix order
1. Buttons (§3) — single CSS-block copy, no markup restructuring, fixes 6 files fast.
2. Cards (§4) — pure rename, fixes 3 files.
3. Page headers (§1) — rename + one font-size fix, fixes 7 files.
4. Badges (§5) and Tables (§6) / Filters (§7) — rename + modifier remap, ~8 files each but same shape of fix.
5. Modals (§8) — largest/riskiest, do last, one file at a time with functional re-check.
6. Empty states (§9) — new component + rollout, treat as its own task after the above.
