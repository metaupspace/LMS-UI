# Workflow Module — Build Plan

## What's already there

**Spec (`src/Workflow.md`, 8 features, fully documented FR/NFR/edge-cases):**

| ID | Title |
|---|---|
| WRK-001 | View All Workflows |
| WRK-002 | Create Workflow |
| WRK-003 | View Workflow Details |
| WRK-004 | Edit Workflow |
| WRK-005 | Duplicate Workflow |
| WRK-006 | Activate / Deactivate Workflow |
| WRK-007 | Delete Workflow |
| WRK-008 | Reassign Approver |

**Dependencies (`knowledge/DEPENDENCY_MAP.md`):** WRK depends on USR-006 (a deactivated approver blocks their step). WRK is used by CRS-011/012/013 (course approval) and ASM-004 (assessment approval) — those modules route through whatever workflow gets built here; they are not part of this task.

**Figma sitemap** (`Admin Sitemap`, node `860:18763`) — pulled the live connector graph; it maps 1:1 to the spec and confirms exact screen/nesting:

```
Workflows → Workflow List (WRK-001)
              ├─ Create Workflow (WRK-002) → Select Type / Set Scope / Build Approval Steps / Assign Approvers
              ├─ Workflow Detail (WRK-003)
              │    ├─ Edit Workflow (WRK-004)
              │    ├─ Reassign Approver (WRK-008)
              │    └─ View Items in Pipeline (part of WRK-003)
              ├─ Duplicate (WRK-005)
              ├─ Activate / Deactivate (WRK-006)
              └─ Delete (WRK-007)
```

No screens in Figma that aren't in the spec, and no spec features missing from Figma — clean match.

**What's built so far:** nothing. `designs/admin/code/` has no Workflow file. All 6 existing admin pages (dashboard, user-management, invite-users, roles, role-detail, user-detail) already have a "Workflows" sidebar link, but it's `href="#"` — inert.

## Spec gap found (flagging, not guessing)

`Course Creation.md:788` says self-approval behavior "depends on org policy in the workflow (WRK-002)" — but `Workflow.md`'s own FR-01–FR-11 for WRK-002 has no field for this policy, and it's not in `DECISIONS.md`'s conflict list either. This needs an answer before Create Workflow's form can be built accurately.

**Open question:** add it as a toggle in the Create/Edit wizard using only the two behaviors `Course Creation.md` already names (auto-skip vs. block-and-escalate), or leave it out of the mock entirely and note it as unspecified?

## Proposed plan

Following this project's own established pattern (Add User / Bulk Import were built as in-page modals, not separate pages — same CLAUDE.md rule 7 logic applies: a wizard step isn't its own URL):

**2 new files in `designs/admin/code/`:**

1. **`workflow-list.html`** — WRK-001 main list (filters, empty state, quick-actions) + **Create Workflow** as a multi-step modal (WRK-002: Name/Type → Scope → Build Steps → Assign Approvers → Review) + Duplicate/Activate-Deactivate/Delete confirmation modals (WRK-005/006/007).
2. **`workflow-detail.html`** — WRK-003 (config, visual approval-chain, version history, Pipeline section = "View Items in Pipeline") + **Edit Workflow** modal (WRK-004, same wizard as Create, pre-populated) + **Reassign Approver** modal (WRK-008, launched from a pipeline row) + the same Duplicate/Deactivate/Delete actions repeated per spec.

**1 wiring task:** point the "Workflows" nav link in all 6 existing admin files at `workflow-list.html` (currently `href="#"` everywhere).

**Not in scope here:** the CRS/ASM-side approval screens (submit-for-approval, approver review UI) — those live in their own modules and just consume WRK, per the dependency map.
