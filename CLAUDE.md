# CLAUDE.md — LMS Docs

## Structure
- `src/` — primary product documentation. One file per module, feature IDs like `AUTH-001`. Source of truth for requirements/flows.
- `designs/` — design & user-flow documentation, organized by role/module (e.g. `designs/Authentication/`). Each module folder holds:
  - `inspo/` — reference screenshots (not this product, style/layout reference only).
  - `code/` — actual built HTML for that module's screens, one `.html` file per flow (see Rule 7).
  Most module folders are still empty (spec-first project — `src/` is ahead of design).
- `knowledge/` — navigation and analysis, built from `src/`+`designs/`, not a source of truth itself:
  - `MASTER_INDEX.md` — **start here** to find where a feature lives.
  - `DEPENDENCY_MAP.md` — check before touching a feature, to see what else it affects.
  - `DECISIONS.md` — explicit cross-cutting product decisions (and known doc conflicts).

## Rules
1. Start in `MASTER_INDEX.md` to locate the feature/module. Don't read `src/*.md` files whole — they're large (up to ~500KB, includes embedded base64 images at file tails). Use `offset`/`limit` or grep to the specific feature section.
2. Detailed behavior (requirements, edge cases, flows) must be verified against the actual `src/` doc — `knowledge/` files are summaries/indexes, never cite them as the requirement itself.
3. Before changing a feature: check `DEPENDENCY_MAP.md` for what depends on it or what it depends on, and check `designs/` for a matching design/user-flow area.
4. Never invent undocumented behavior. If something isn't specified, say so — don't fill the gap with a guess.
5. If `src/` docs conflict with each other (see `DECISIONS.md` conflicts section for known ones), report the conflict — don't silently pick an interpretation.
6. `knowledge/` files go stale — if `src/` or `designs/` changes materially, they need regenerating, not blind trust.
7. **One HTML file per flow in `designs/*/code/`.** Never bundle multiple flows (sign-in, sign-up, forgot-password, etc.) into a single file with a JS toggle — each flow a user could land on via its own URL/link gets its own standalone `.html` file (full doctype, self-contained CSS/JS, no build step). Link between them with plain `<a href="other-flow.html">`. Reuse the same design tokens (from `UpSpaceDESIGN.md`) and shared visual elements (e.g. brand panel) across a module's files for consistency, but each file must stand alone — don't extract shared CSS/JS into a separate file that others `<link>`/`<script src>` to, since these are meant to be viewed by opening the file directly, not served.
8. **New design work in `designs/*/code/` pulls from the UpSpace component library first.** Source of truth: `Analyze-design-system/UpSpace Design System/` (`colors/colors.json`, `styles/textStyles.json`, `icons/<lucide|hugeicons>/<LETTER>.json`, `components/<Group>/components.json`), indexed by `Analyze-design-system/design-system-map.json`. Fixed sequence for any "create/design this screen" request:
   1. Check the Figma Desktop Bridge plugin is connected (figma-console status tool) before doing anything else. If it's not connected, stop and tell the user to open/enable the Desktop Bridge plugin — don't proceed until they confirm it's on.
   2. Decide what components the screen needs and how it's structured (layout, sections), checking each needed component against `components/<Group>/components.json`.
   3. Report back which needed components are missing from the library (not found in any group's `components.json`).
   4. Log missing components in `/Users/musdev/Anurag Dev/LMS/MISSING_COMPONENTS.md` (create it if absent) — one entry per missing component, plain checklist, noting which screen/flow needed it.
   5. Wait for explicit user permission before building anything for a missing component. Only the missing components get newly designed — never redesign or restyle a component the library already has.
   6. On permission: build the missing component directly in the HTML output (using the library's existing colors/type/icons for consistency) and wire it straight into the screen. This is HTML-only — do not create or push anything into the actual Figma file/library.
   7. Every component the library already has must be used as-is (its existing markup/pattern from `components/<Group>/components.json`), never hand-rolled from scratch.
   If genuinely unclear on any step (e.g. which group a component belongs to, ambiguous screen structure), ask rather than guess.
