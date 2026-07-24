# Tracking Verification Checklist — GTM & Meta

_Generated from the code after the site-wide light-theme redesign (July 2026). Everything below is already wired in the HTML; this checklist is for confirming the **GTM container** and **Meta Events Manager** are configured to match. It needs GTM/Meta account access — the code side is done._

**GTM container:** `GTM-WBW5QJQT` · **Meta Pixel:** `3083326175185716`

---

## A. dataLayer events the site pushes — confirm a GTM trigger + tag exists for each

Every CTA/interaction below pushes `window.dataLayer.push({ event: '<name>', ... })`. In GTM, each needs a **Custom Event trigger** (Trigger type → Custom Event, event name = exact string) feeding whatever tag you want (GA4 event, Google Ads conversion, Meta CAPI, etc.).

| Event | Fires when | Pages | Code count |
|---|---|---|---|
| `book_call` | Any "Book Discovery Call" CTA click (`data-conversion="book_call"`) | **all 27 pages** | 107 |
| `phone_click` | Any `tel:` link click | all pages | 45 |
| `whatsapp_click` | WhatsApp link click | contact, index, inventory, ontario-investors, why-alberta | 6 |
| `guide_download` | Guide download / "Read the guide" CTA | guide (on real PDF download), faq, ontario-investors, blog/edmonton-vs-toronto | 7 |
| `package_view` | "View Full Package" (Drive) on an inventory card | inventory | 7 (one per available card) |
| `virtual_tour_view` | "Open Full Tour" (iGuide) | crawford-plains, inglewood | 2 |
| `gallery_view` | "View all N photos" button | crawford-plains | 1 |
| `form_submit_contact` | GHL form/booking completion (iframe postMessage) | contact, guide | 3 |
| `calculator_start` | First interaction with the DSCR calculator | calculator | 1 (fires once) |
| `calculator_complete` | Calculator reaches a viable deal (DSCR ≥ 1.10); includes `dscr` value | calculator | 1 (fires once) |

**Priority to confirm (flagged as unverified in CLAUDE.md):**
- [ ] `virtual_tour_view` — Custom Event trigger exists and maps to a tag
- [ ] `package_view` — Custom Event trigger exists and maps to a tag
- [ ] `gallery_view` — Custom Event trigger exists (newest; only on crawford-plains)

> Tip: in GTM **Preview mode**, load each page and perform the action; the event should appear in the Tag Assistant timeline with the tag firing.

---

## B. Double-count guard — the Meta base pixel must fire ONCE

The Meta **base pixel + `PageView`** is **hardcoded in the `<head>` of all 27 pages** (init + `fbq('track','PageView')`).

- [ ] **Confirm GTM does NOT also contain a Meta base-pixel / PageView tag.** If it does, every page view is counted twice and ad optimization is corrupted. GTM may fire *additional* Meta events (Lead, custom conversions) but must **not** re-initialize the pixel or re-send PageView.

How to check: Meta Events Manager → **Test Events** → load any page. You should see exactly **one** `PageView`. Two = a GTM duplicate to remove.

---

## C. Meta pixel events already hardcoded (no GTM action needed — for reference)

These fire directly from page JS, not GTM:

| Meta event | Fires when | Pages |
|---|---|---|
| `PageView` | Page load (base pixel) | all 27 |
| `Contact` | `tel:` or `mailto:` link click (with `contact_method`) | all 27 |
| `Lead` | **Only** on real GHL guide-form submission (inside `triggerPdfDownload()`) | guide |
| `GuideModalOpen` (custom) | Guide PDF modal opened | guide |
| `ViewContent` (`calculator_started`) | First calculator interaction | calculator |

- [ ] Confirm `Lead` fires **only** on actual form submit (not on modal open) — verify in Test Events by opening the guide modal (should show `GuideModalOpen`, **not** `Lead`) then submitting (should show `Lead`).

---

## D. Quick end-to-end test script

1. **GTM Preview** on the live site. For each event in section A, do the action and confirm the tag fires once.
2. **Meta Test Events** open in parallel. Confirm: one `PageView` per page (section B), `Contact` on tel/email, `Lead` only on guide submit, `GuideModalOpen` on modal open.
3. On `/inventory`, click a "View Full Package" — confirm `package_view` (used for the retargeting audience).
4. On `/crawford-plains` and `/inglewood`, click "Open Full Tour" — confirm `virtual_tour_view`; on crawford, "View all N photos" — confirm `gallery_view`.
5. On `/calculator`, change an input — confirm `calculator_start`; reach DSCR ≥ 1.10 — confirm `calculator_complete` (with `dscr`).

---

_Code side verified complete: all events present and firing in the HTML across all 27 pages (see counts above). Only the GTM/Meta account configuration remains to confirm._
