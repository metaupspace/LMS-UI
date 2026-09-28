# Integrations Module — Build Plan

## What's already there

**Spec (`src/Integrations.md`) — only 3 real features, not the 5 IDs the numbering implies:**

| ID | Title |
|---|---|
| INT-001 | Integrations Catalog *(source has a typo: "Cataog")* |
| INT-002 | Manage Integrations |
| INT-005 | API & Webhooks *(source header literally reads `## **NT-005 — API & Webhooks**` — missing the leading "I", and out of sequence; its FR/NFR rows are consistently `INT-005-FR-*`, confirming INT-005 is the true ID)* |

**Known gap (already documented in `knowledge/MASTER_INDEX.md:21`, not something I'm newly flagging):** INT-003 and INT-004 have no content anywhere in the source file — a two-ID gap between INT-002 and true INT-005. Nothing to build for those IDs; they don't exist.

**Dependencies (`knowledge/DEPENDENCY_MAP.md`):**
- INT requires → LSN-001 — a connected video integration (Zoom etc.) has no effect until an instructor creates an online session and selects it.
- INT modifies → AUTH-006 — disconnecting Google Workspace SSO forces affected users onto password-based sign-in/reset.

No `DECISIONS.md` conflicts recorded for this module.

**Figma sitemap** (`Admin Sitemap`, node `860:18763`) — pulled the live connector graph:

```
Integrations
  ├─ Integrations Catalog (INT-001)
  │    └─ Integration Detail
  ├─ SSO Configuration
  ├─ SIS / HRIS Sync
  └─ API & Webhooks (INT-005)
```

**Important mismatch between spec and sitemap:** the sitemap has no node called "Manage Integrations" (INT-002). Reading the spec closely, this isn't a missing screen — INT-002's job (health status, reconfigure, reconnect, disconnect) is the *same* "Integration Detail" screen INT-001 uses after connecting, just showing a different state (Connected/Error/Warning vs. Available). INT-001-FR-05 already supports filtering the Catalog by status (Connected/Available/All), so "Manage Integrations" is really "the Catalog, filtered to Connected" → same Integration Detail page per row. One screen serves both specs — confirmed by the sitemap itself connecting `Integrations Catalog → Integration Detail` and nothing separate for "manage."

"SSO Configuration" and "SIS / HRIS Sync" are siblings of "Integration Detail" in the sitemap, not children of it — but the spec (INT-001-FR-04) describes them as the *same* per-integration settings panel, just with content that varies by category (e.g. Google Workspace shows Calendar/Drive/SSO toggles; SIS shows sync-field mapping). They're called out separately in the sitemap because their settings differ meaningfully, not because they're a different flow.

**What's built so far:** nothing for this module. `designs/admin/code/` has no Integrations file. All existing admin pages have an "Integrations" sidebar link, still `href="#"`.

## Proposed plan

**3 new files in `designs/admin/code/`:**

1. **`integrations-catalog.html`** — INT-001. Catalog grid by category (Video, Productivity, Communication, Data Sync, Storage), status badges (Available/Connected/Disconnected/Error), category + status filters, "Upgrade to unlock" locked state for plan-gated integrations, OAuth consent step shown as a modal (redirect can't really happen in a static mock — mock the consent screen + success/deny outcomes inline), links each connected/available row into Integration Detail.
2. **`integration-detail.html`** — one template covering both INT-001's post-connect "configure settings" step and all of INT-002 (health status, last sync time, dependent features, Reconfigure/Reconnect/Disconnect actions, disconnect confirmation with the graceful-fallback messaging from FR-06). Built with a couple of concrete example states/sections to cover the sitemap's called-out variants: a video integration (Zoom — session defaults), an SSO integration (Google Workspace — Calendar/Drive/SSO toggles, ties to AUTH-006 on disconnect), and a data-sync integration (SIS — field mapping). Same one-file-many-states pattern already used by `user-detail.html`.
3. **`api-webhooks.html`** — INT-005. API key list + generate flow (key shown once, then masked forever, per NFR-01), webhook list + configure form (event type, target URL, secret), delivery history per webhook, failing-webhook state after 3 retries.

**1 wiring task:** point the "Integrations" nav link at `integrations-catalog.html` across the existing admin files (currently `href="#"` everywhere, including the newly-built `workflow-*.html` files).

**Not in scope here:** the actual OAuth provider flows, real API/webhook infrastructure, or LSN/AUTH-side screens that consume these integrations — this module only owns the admin-facing connect/manage/API-key UI, per the dependency map.

## No open questions

Unlike Workflow, nothing here is underspecified — INT-001/002/005 are fully detailed with FR/NFR/edge cases, and the sitemap/spec reconcile cleanly once "Manage Integrations" is understood as a state of Integration Detail rather than a separate page.
