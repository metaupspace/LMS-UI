# Context: Ideating the Billing & Subscription screen (UpSpace LMS Admin)

Paste this whole doc into ChatGPT (or any other model) when asking it to riff on redesign ideas for this screen. It has no access to the repo, so this is the full picture it needs.

## What this screen is

Admin-only page in an LMS admin console. One org admin manages: their subscription plan, seat count, payment method, invoices, and pause/cancel — self-serve, no support contact needed. Maps to spec IDs `BIL-001` through `BIL-004` (Subscription Overview, Change Plan/Add Seats, Payment Methods & Invoices, Cancel/Pause).

File: `designs/admin/code/billing-overview.html` — a standalone HTML/CSS/JS file (no build step, no framework), one of 12+ admin screens that all share the same sidebar/topbar shell and design tokens.

## Current structure (as of now)

1. **Topbar + left sidebar** — shared shell identical across all admin pages (logo, search/notifications/avatar top-right; Dashboard/Users/Roles/Org/Workflows/Certificates/Community/Integrations/Billing/Reports nav on the left).
2. **Alert banner zone** — one of five conditional banners shows at a time: 80%-seats warning, past-due payment, trial countdown, paused, cancelled. Each has its own CTA button.
3. **KPI row** — 4 cards: Active Tier, Seats (used/total + %), Next Billing (date + amount), Payment Method (masked card + status pill).
4. **One merged card** titled "Subscription & Billing" containing, top to bottom with light dividers between sub-sections (no separate boxes):
   - Seat consumption meter + "Change Plan" / "Pause" / "Cancel" buttons
   - Included plan features (checklist grid)
   - Tax ID & Invoicing Address (read-only display, "Edit" opens a small modal)
   - Payment method row (card brand, last 4, expiry, "Update Card" / "Remove" buttons)
5. **Separate card**: Invoice & Payment History table (date, invoice #, description, seats, amount, status, download/retry action).
6. **"Change Plan" drawer** — right-side slide-over (not a tab, not a small modal) triggered from the "Change Plan" button or any banner. Contains: a suggestion banner ("you're at 85% seats, consider Enterprise"), monthly/annual billing toggle, a 2×2 plan comparison grid (Startup Free / Growth / Pro-current / Enterprise-suggested), and a seat slider with live prorated-cost math. Footer: Close / Continue to Checkout.
7. Smaller modals: Update Payment Method (redirects to Stripe portal, no card entry in-app), Edit Tax ID, Pause (duration radio options), Cancel (reason radio options, required).
8. Toasts (bottom-right, auto-dismiss) confirm actions instead of native `alert()`/`confirm()` popups — only pause/cancel/remove-card keep a native `confirm()` since those are genuinely destructive.

## Design system tokens (shared across all 12 admin screens — changing these here would break consistency elsewhere)

- Font: DM Sans (400/500/600/700)
- Neutral grays: `#171717` (text primary) → `#a3a3a3` (tertiary) → `#fafafa` (canvas bg)
- Single accent: indigo `#4f46e5` (buttons, links, focus ring, "current plan" highlight)
- Status colors: success green, warning amber, error red, info blue — each with a `-subtle` background variant
- Radius scale: 4 / 6 / 8 / 12 / 16px
- Cards: white bg, 1px neutral border, 16px radius, 24px padding
- Pills/badges: fully rounded, small, used for status (Active/Trial/Past-Due/Paused/Cancelled) and plan labels
- Sidebar 232px fixed, topbar 80px fixed, content max-width 1280px

## Constraints for any redesign idea

- Must still work as a **standalone HTML file** — no separate CSS/JS files, no npm/build step, opened directly in a browser.
- Must still visually match the other 11 admin screens (same shell, same tokens) — this is one screen in a shared admin console, not a standalone product.
- All the BIL-001–004 functional requirements below still need a home somewhere in the UI — ideation can rearrange/reprioritize, not drop them.
- Mock data / no real backend — everything is hardcoded JS state for prototyping.

## Where we've already iterated (don't just re-suggest these)

- Round 1: copy read as AI-generated marketing fluff ("Multi-Step Approval Workflows & Pipeline Engine" etc.) — trimmed to plain, specific language. All `alert()`/blocking dialogs replaced with toasts.
- Round 2: page was three tabs (Subscription&Usage / Plans&Pricing / Payment&Invoices) that felt like stitched-together separate screens. Merged into one continuous flow + moved plan comparison into a slide-over drawer reached via "Change Plan".
- **Still open / what to actually brainstorm on:** it still doesn't feel fully cohesive — KPI row duplicates info already shown lower on the page (seats, payment method), the page is very list-of-cards/vertically stacked with not much visual hierarchy or personality, and there's room for a genuinely better information architecture, not just "un-stack the boxes." Open to reordering sections, cutting/merging the KPI row into the main content, rethinking whether Tax ID + Payment Method even belong in the same flow as plan/usage, alternate layouts (e.g., summary + detail split, sidebar-style plan switcher instead of a drawer, etc.).

## Business rules that must survive any redesign (source: `src/Billing.md`)

- Seat downgrade is blocked if active users exceed the target plan's seat cap — must show which plan tiers are even valid choices given current usage (currently 85 active users).
- Seat count can never be set below current active user count.
- Mid-cycle upgrades show prorated credit/charge math before checkout; all payment happens on a hosted checkout (Stripe/Razorpay) — the app never touches raw card data.
- Subscription states: Active, Trial (with countdown), Past-Due (grace period before non-admin lockout), Paused (up to 90 days, zero charge, full data retention, resumable anytime), Cancelled (access until cycle end, 30-day export grace period, then archived; reactivatable during grace period).
- Removing a stored payment method is only allowed on a free or cancelled subscription.
- Seat-limit warning triggers at 80% utilization.
- Two admins can both manage billing; actions are idempotent and logged (who/when).

## The actual ask for ChatGPT

Given all of the above, propose fresh ideas for how this screen's layout/information architecture could be better — more cohesive, better hierarchy, less "stack of cards" — while still satisfying the BIL-001–004 requirements and staying implementable as one static HTML/CSS/JS file matching the shared design tokens above.
