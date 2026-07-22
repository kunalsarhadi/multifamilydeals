# Audit Round 2 — Implementation Report
**Date:** July 22, 2026 · **Status: ALL TIERS EXECUTED AND LIVE on main** (commits `5d087d0` → `d3189ce`)
**Baseline:** reports/2026-07-08-marketing-audit-and-changes.md (round 1) + the July 22 round-2 audit findings.

---

## Tier 1 — Credibility & conversion (LIVE)

1. **Mortgage math re-based to 5.25% site-wide.**
   - inventory.html VS block: ~$11,000/mo (30-yr) vs ~$9,450/mo (50-yr), "approximately $1,600 — over $19,000 per year" (was $9,500/$7,700/$1,800 — computed at 4% while claiming 5.25%)
   - guide.html Section 01: ~$8,300 vs ~$7,100, "$1,200/month — over $14,000/year" with "(Figures at 5.25%; your rate will vary)" (was $8,500/$6,200/"$2,300" — not achievable at any consistent rate)
   - **⚠️ OWNER ACTION: have your mortgage broker sanity-check these figures — they are now the site's canonical debt-service example.** Canonical values recorded in CLAUDE.md.
2. **Landlord-experience contradiction fixed.** Homepage qualify item now reads: "CMHC does require documented landlord experience: one rental, even a basement suite, satisfies it. We'll confirm yours on the call." — consistent with inventory's hard gate.
3. **Inventory booking CTAs restored:** gold "Verify My Eligibility on a Free Call" button in the closing eligibility callout + a CTA row after the Available grid ("Want the full pro-forma, address, and deal terms…"). The page no longer dead-ends.
4. **Appraisal proof deployed to the four missing pages:** ontario-investors (strip between proof band and comparison table, with disclaimer), contact (line beside the form: "…Verification available on your call"), calculator (tied to the Year-1 appreciation assumption), guide (callout in Section 02). The claim + wording is identical everywhere: "Every completed project has appraised above its purchase price — independent AACI appraisals, $20,000–$200,000 higher."

## Tier 2 — Navigation & structure (LIVE, all 24 pages)

5. **Nav tab renamed "Why Edmonton" → "The Strategy"** with items: Our Approach (about) · Why Alberta · **Track Record** (about#track-record). The track record finally has a navigation home.
6. **Properties labels shortened:** "Crawford Plains 8-Plex / Newest completed project · 2026" and "Inglewood 9-Plex / Completed 2025 · set the standard." Two pages kept separate (per IA review — merge only when project #3 exists).
7. **Resources reordered:** Buying Process, Calculator, Free Guide, FAQ, Reviews, Blog.
8. **Mobile nav:** Book Discovery Call moved to the top of the overlay + a tap-to-call `tel:+14162007010` row added (feeds phone_click tracking).
9. **Homepage proof stack reordered:** hero → trust bar → appraisal band → comparison … reviews (moved down) → final CTA. Outcome proof now leads; the two review cards close instead of opening. *Note: the audit suggested an "Eight of eight" numbered sub-line — NOT applied, per the owner's standing "no number, say every completed project" directive.*

## Tier 3 — Page-level (LIVE)

10. **crawford-plains.html:** "South/Edmonton Location" hero stat → **"+$100K / Appraised Over Purchase"**; mobile sticky CTA ("See What's Available Now →" → inventory); `data-conversion="gallery_view"` on all 3 View-All buttons; orphaned comment removed.
11. **inglewood.html:** eyebrow → "Portfolio · The Project That Set the Standard · Completed 2025"; hero line "The build every project since has been measured against — and improved on."; track-record strip near the CTA.
12. **why-alberta.html:** "The Market Case, Proven in Appraisals" strip after the signals section (the market page now carries firm proof). Closing CTA already had both buttons — verified, untouched.
13. **buying-process.html:** "Lender Satisfied" → "Financing Conditions Cleared"; "Deal Firmed" → "Purchase Agreement Goes Firm" (visible + JSON-LD schema); appraisal line added at Step 06 with track-record link.
14. **faq.html:** two new Q&As in The Process ("What if the appraisal comes in below the purchase price?" — honest, no-guarantee answer; "How can I verify your appraisal track record?" — on-file/verification-on-request), added to FAQPage schema too; mobile category chip row added (sidebar hides <1200px — chips now give mobile users jump navigation).
15. **reviews.html:** "Team Sarhadi Real Estate" section → "The Team Behind Multi Family Deals"; bridge line to the track record after the last review.
16. **Blog:** full-width "Start Here" featured card (MLI Select Guide 2026) + two pinned paths (Edmonton vs Toronto / Scale to 50 Doors); **two new posts:** `blog/appraisal-track-record-edmonton.html` ("Why Our Projects Keep Appraising Above Purchase Price" — delta table of all 8 deals, privacy rationale, honest caveats) and `blog/crawford-plains-8plex-case-study.html` ("Anatomy of a Completed Edmonton 8-Plex"). Both fully wired (GTM/pixel/chat/listener/schema) and in the sitemap.
17. **Copy honesty pass:** contact's "Current Inventory Access — first look" → "Early Access Pipeline — coming-soon packages shared with booked investors before they're posted" (truthful vs public inventory); ontario's "Prefer to watch first?" → "Want to see deals before deciding?"; inventory scarcity hardened ("released to date"; "the strongest packages typically go under offer first").
18. **Label/figure sync:** inventory trust stat → "In Transactions Closed by the Sarhadi Brothers"; guide's Alberta development charges "None" → "Minimal — no Ontario-style DCs"; guide's 8-plex anchor → "~$2.0M–$2.4M"; calculator's "mention calculator" passphrase → automatic ("book from this page and we'll rebuild this pro-forma…"); CMHC premium field got a plain-language hint.

## Technical defects (LIVE)

- **T1 Lightbox scroll bug FIXED** (crawford): scroll position saved on open, restored on close; sticky bar also hides while the lightbox is open.
- **T2 Appraisal disclaimers added** to the homepage strip and inventory trust line (all placements now carry the as-if-complete/opinion-of-value disclaimer).
- **T3 CLAUDE.md fully refreshed:** page table + calculator row, sitemap declared canonical page list, GTM "all pages", package_view corrected, virtual_tour_view on both portfolio pages, gallery_view documented, live Drive-gallery note with the single-point-of-failure caution, nav structure, delta-only policy, canonical 5.25% math.
- **T4 Crawford appraisal card relabeled** "AACI appraisal at financing · 2025" — resolves the 2025-appraisal vs July-2026-delivery tension honestly.
- **T6 orphaned comment removed.**

## Deliberately skipped / needs owner input

| Item | Why |
|---|---|
| "Eight of eight" numbered claim | Owner directive: no deal count — "every completed project" only |
| why-alberta comparison-table compression | Risky content surgery; low value vs risk — revisit if page analytics show drop-off |
| FAQ "Common Questions" dedupe | Needs owner review — answers overlap but deletion could hurt AI-search capture |
| Project-anchored testimonial on reviews | Cannot invent quotes. **Send a real Crawford/Inglewood buyer quote** and it goes in |
| Buying-process time estimates | Needs the real "first call to keys" duration from Kunal |
| Crawford suite bed/bath rows | Needs the actual unit mix |
| T5: street address visible in the iGuide tour URL | Owner's call — likely fine for a sold portfolio property |
| **VERIFY: "Completed 2025" on Inglewood** | The year now appears in nav + hero eyebrow, sourced from earlier nav copy. **Confirm 2025 is correct or tell me the right year** |

## Standing follow-ups (unchanged)

Founder photos (blocks ready) · outcome data for Crawford/Inglewood (lease-up, achieved rents, DSCR) · per-package price bands · GHL form ID for calculator capture · **GTM triggers now needed for: package_view, virtual_tour_view (2 pages), gallery_view (new)** · confirm GTM doesn't double-fire the Meta base pixel.
