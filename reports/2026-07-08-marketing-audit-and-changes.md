# Marketing & Sales Psychology Audit — Changes Report
**Date:** July 8, 2026
**Scope:** Full-site review (all 21 HTML pages + sitemap) through a conversion/sales-psychology lens, followed by implementation of all approved changes.
**Deployed:** All changes below are LIVE on main (commits `f75efa7` and `3ba5517`).
**Audience for this doc:** future Claude sessions, SEO sessions, and anyone touching tracking, copy, or page structure.

---

## 1. Owner-set constraints (DO NOT UNDO)

1. **Google Drive links on inventory cards stay public.** FB leads signed up specifically for this data. Do not gate them.
2. **WhatsApp strips keep their green (#2AAF72) styling.** Do not restyle to gold/navy.
3. **Never promise "CMHC approval protection"** or any deposit guarantee. We do not offer this. The correct framing for the incentive item is "Purchase Agreement (APS) Exit Terms — exit per agreement terms if CMHC declines on project viability."
4. **Calendly is banned.** GHL (GoHighLevel) is the only booking/CRM path.
5. Brand voice: premium, institutional, data-driven. Never "get rich quick."

---

## 2. Tracking & analytics changes (SEO/ads sessions read this first)

| Change | File | Detail |
|---|---|---|
| **Meta `Lead` event moved to real submission** | guide.html | `fbq('track','Lead')` previously fired when a visitor merely OPENED the download modal — Meta was optimizing ads toward popup-openers and inflating reported leads. `Lead` now fires inside `triggerPdfDownload()` (i.e., on actual GHL form submission). Modal-open now fires custom event `GuideModalOpen`. **Expect reported lead volume to DROP and lead quality to rise — this is correct, not a regression.** |
| **New event: `package_view`** | inventory.html | All 9 "View Full Package" Google Drive links now carry `data-conversion="package_view"`. This is the highest-intent click on the site. **Action needed in GTM:** create a trigger/tag for it. **Action needed in Meta:** build a retargeting audience from it. |
| **Event `virtual_tour_view`** | inglewood.html | Pre-existing but undocumented. **Verify GTM has a trigger** or clicks are dropped. |
| **Blog tracking gap closed** | blog/mli-select-worth-it.html | Was the only page missing the dataLayer conversion listener — its 4 CTAs fired nothing. Fixed. |
| **Chat widget gap closed** | blog/cmhc-mli-select-50-points-explained.html | Was the only page missing the GHL chat widget. Fixed. |
| **Pixel documentation corrected** | CLAUDE.md | The Meta base pixel IS hardcoded in every page's `<head>` (the doc previously said GTM-only). **Verify GTM does not ALSO fire the base pixel — if it does, PageViews are double-counting.** |

### SEO-specific changes
- **sitemap.xml**: added missing entry for `blog/alberta-employment-growth-2026.html`.
- **Canonical fix**: that post's canonical + og:url were extensionless (`/blog/alberta-employment-growth-2026`) while the other 20 pages use `.html`. Normalized to `.html`.
- **reviews.html schema**: removed `aggregateRating` + `review` array from JSON-LD. Reason: self-serving review markup violates Google's review-snippet policy, and `reviewCount: 10` contradicted the on-page "160+" claim. Do not re-add.
- **Footers normalized on all 21 pages**: canonical order is Strategy / Why Alberta / Inventory / Portfolio / Buying Process / FAQ / Reviews / Blog / Free Guide / Calculator / Contact. Duplicate "Blog" links removed (3 blog pages), Calculator added where missing (10 pages), rogue "Home"-first template replaced (2 blog pages).

---

## 3. The inventory count system — IMPORTANT for inventory sessions

**Counts are now auto-calculated. Never hand-edit them again.**

A script at the bottom of inventory.html counts `.asset-badge` elements per section on page load and fills:
- the three status pills (`#countAvailPill`, `#countScPill`, `#countCsPill`)
- both section headers (`#countAvailHeader`, `#countScHeader`)
- the scarcity block numbers (`#scarcityGone`, `#scarcityReleased`, `#scarcityAvail`)

To change inventory, add/move/remove the **card** — numbers update themselves. (Counts had drifted 3 times in two weeks from hand-editing; this ends that failure mode.)

**Property handoff:** the same script appends `?property=<slug>` to every `a.js-property-link` in a card ("Discuss This Property" on available cards, "Join the Waitlist for This Property" on sold-conditional cards). contact.html reads the param and shows "Regarding: <Property>" under the hero. When adding new cards, copy an existing card verbatim and the links wire themselves.

---

## 4. Page-by-page changes

### index.html (homepage)
- Scarcity line under hero CTAs: "More than half of released packages are already sold or under conditional offer — see what remains →" (deliberately count-free so it can't drift).
- Ghost CTA renamed "View Active Inventory" → "View the Available Packages".
- **Compliance fix:** removed the overclaim "No capital is at risk during the build" (the deposit IS committed capital). New copy: "Your mortgage doesn't begin until completion — during construction you make no mortgage payments while the builder carries the project."
- Risk disclaimer moved BELOW the final CTA button (was directly above it — last thing read before the decision point was a warning).
- Trust label "$500M+ Real Estate Sold / Combined Sarhadi Group" → "$500M+ In Transactions Closed / by the Sarhadi Brothers".
- Mobile comparison table: Ontario/BC column restored on mobile (was `display:none` — the core contrast argument vanished for mobile ad traffic). Label spans full width, ON/BC and Edmonton values sit side by side.
- Mobile sticky CTA bar now mobile-only (was leaking onto desktop via inline style).
- Footer: Calculator link added.

### inventory.html (highest-intent page)
- Scarcity headline block under hero: "**X of Y released packages are already sold or under conditional offer.** N remain available…" (auto-counted) + DSCR plain-language gloss ("projected rental income ÷ mortgage payments; CMHC requires 1.10 minimum").
- `package_view` tracking on all 9 Drive links (links themselves unchanged).
- Second CTA per available card: "Discuss This Property" → contact.html with property param.
- Sold-conditional CTA now keeps its promise: "Join the Waitlist for This Property" (was "Join Waitlist — May Become Available" landing on a generic booking page).
- "Special Offer" section label → "Included With Every Package" (retail-speak removed).
- Jargon: "APS Exit Terms" → "Purchase Agreement (APS) Exit Terms"; "8 Mo. From COI" → "8 months from construction start".
- Mobile sticky bar: "Book a Call — Get Full Pro-Formas".

### contact.html (money page — biggest restructure)
- **GHL form moved directly under the hero** (was below 6 sell-cards, ~2 screens down on mobile).
- Section reframed: "Before You Book" → "**Reserve Your Call — Step 1 of 2**" + heading "Tell us about your situation (about 2 minutes)" + copy explaining the answers produce a pre-built pro-forma and the call time is picked next step. The form no longer reads as a gate.
- What-happens-next row under the form: 1. Submit (2 min) → 2. Pick a time → 3. 30-min call with live pro-forma; "Not a fit? We'll tell you — no follow-up pressure."
- Credential line by the form: "You'll be speaking with Kunal Sarhadi, Real Estate Broker, Homelife Miracle Realty Inc. — backed by 160+ verified Google reviews."
- Bottom trust bar switched from program stats (5%/50yr/$0 — visitor already knows these) to people proof: 160+ reviews / $500M+ closed / Licensed broker.
- GHL iframe got `min-height:620px` (previously if form_embed.js failed, the form collapsed to zero height — money page with no form).
- Reads `?property=` and displays "Regarding: <Property>".
- tel: link normalized to `tel:+14162007010`.

### ontario-investors.html (paid-traffic landing page — biggest gap fixed)
- **Hero CTAs added** (there was NO clickable element above the fold): primary "Book a Free Discovery Call" + anchor "See the Edmonton vs Toronto Numbers ↓" to `#comparison`.
- **Proof band inserted** before the comparison (there was ZERO social proof on the page): $500M+ / 160+ reviews / 500+ families, a Toronto-relevant testimonial, broker credential line.
- Primary CTA repeated after the comparison table and after the objections grid.
- **Not-ready fallback** before the final strip: free guide card + WhatsApp card (green kept per constraint). The page previously had no middle path — book a call or bounce.
- Final strip ghost CTA changed from "Why Alberta" (sideways exit) to "Browse the Available Packages" (forward motion).
- Mobile sticky bar: "Book a Free Discovery Call".

### calculator.html
- **Default interest rate 4% → 5.25%**, matching the inventory page's own disclaimer (5.25–5.50%). The 4% default was a credibility landmine for a data-driven audience.
- Defaults now model a realistic qualifying 8-plex: $2.0M price, 4×3-bed @ $2,150 + 4×2-bed @ $1,500, $15,500 property tax → DSCR ≈ 1.16, ~$17.6K/yr cash flow at 5.25% (in line with real listings at 1.16–1.29). At the old defaults + honest rate, the default screen FAILED DSCR — do not revert either half alone.
- "Keep this pro-forma" line under the CTA; CTA carries `?source=calculator`.
- Mobile sticky bar: "Book a Call — Review Your Numbers".

### guide.html
- Meta `Lead` on submission only (see tracking section).
- Mid-guide capture card after Section 04 (deposit math — peak engagement): "Want to keep these numbers?" → opens the same PDF gate modal.
- **Liquidity requirement corrected to canonical**: "liquid assets equal to roughly 10% of the project price (after deposit)" — was "additional 5%", contradicting inventory (10%) and calculator (deposit×2).
- Section numbering fixed: sections now run 01–06 (there was no Section 06; 05 jumped to 07).

### about.html
- "160+ Verified Google Reviews" trust stat now links to reviews.html.
- Founder credential block added under the manifesto quote (text-only — see photography note below).
- Not-ready fallback under the closing CTA: link to the DSCR calculator.
- $500M label sharpened (same as homepage).

### faq.html
- **MLI Select points contradictions reconciled** to the canonical framing: 50 points = minimum eligibility; 100 points = maximum benefits including 50-year amortization and highest LTV. (Page previously said 40+/50+/100+ in three different answers.)
- Hidden 6th category ("Common Questions", `#ai-search`) added to the sidebar + scroll-spy.

### reviews.html
- H1 now includes the site brand: "What Investors Say About the Team Behind Multi Family Deals."
- Self-serving review JSON-LD removed (policy risk).
- tel: links normalized to +1.
- **Owner decision (July 9):** NO direct outbound link to the Google reviews profile — a search-URL link was briefly added and has been removed. Keep review proof on-site only. Do not re-add external Google links.

### Blog (all 9 files)
- Footers normalized, conversion listener + chat widget gaps closed, sitemap + canonical fixes (see sections 2 above).

---

## 5. Canonical numbers (single source of truth — keep consistent site-wide)

| Figure | Canonical value |
|---|---|
| MLI Select points | 50 = minimum eligibility; **100 = max benefits incl. 50-yr amortization** |
| Liquidity requirement | ~10% of project price in liquid assets, after deposit |
| Calculator default rate | 5.25% (do not lower) |
| Modeled rate range (inventory disclaimer) | 5.25–5.50% |
| Phone (links) | `tel:+14162007010`, displayed 416-200-7010 |

These are also recorded in CLAUDE.md.

---

## 6. Remaining items — PRIORITY ORDER (July 9, 2026)

| # | Item | Status / what unblocks it | Expected impact |
|---|---|---|---|
| 1 | **Founder photos on site** — about.html manifesto, contact.html beside the form, homepage proof strip. Credential text blocks are already in place; drop the images in when they arrive. | **Owner is sending photos of Kunal & Ankit soon.** Implement immediately on receipt. | Highest remaining trust lever — site currently has zero human faces at commitment points |
| 2 | **GTM verification** — (a) create triggers for `package_view` and `virtual_tour_view`; (b) confirm GTM does NOT also fire the Meta base pixel (it is hardcoded in every page's head — double-fire = double-counted PageViews); (c) build Meta retargeting audience off `package_view`. | Needs GTM + Meta account access (browser session). | Every ad dollar optimizes better; highest-intent audience becomes targetable |
| 3 | **Deposit / cash-to-close anchors on inventory cards** ("Est. cash to close: from ~$X"). | Needs real price bands per package from the Google Sheet / Kunal. Never invent numbers. | Answers the #1 unspoken question on the highest-intent page |
| 4 | **Inglewood outcomes band** — lease-up days, achieved rents vs pro-forma, stabilized DSCR, + one buyer quote. | Needs real deal data from Kunal. | Converts "the building exists" into "the investment worked" |
| 5 | **True calculator email capture** ("Email me this pro-forma" → GHL). | Needs a dedicated GHL form ID + workflow. Current stand-in: soft CTA with `?source=calculator`. | Captures the site's most-engaged anonymous users |
| 6 | **Appraisal / track-record section** — ~10 past deals appraised $25K–$200K over purchase. Numbers-only cards (no purchase price, no addresses/legal/lot info, no client names), compact strip on about.html + full section on inglewood.html. | Owner will provide redacted data. Snapshot branch `snapshot/pre-appraisals` preserves pre-work state. | Proof-of-returns asset no competitor in this niche shows |

**Owner decisions on record (July 9):** photos incoming; NO direct Google-profile link anywhere (on-site review proof only); Drive links stay public; WhatsApp stays green; no "CMHC approval protection" language ever.

---

## 7. What to watch after deploy

- **Meta Ads:** reported Leads will drop (they were inflated by modal-opens). CPL will look worse on paper while true lead quality rises. Re-baseline after 2 weeks.
- **`package_view` volume** once the GTM trigger exists — this becomes the key mid-funnel KPI and retargeting seed.
- **Contact page conversion rate** (form now above the fold + reframed) — compare GHL form submissions before/after July 8.
- **Ontario page bounce rate** — it now has above-fold CTAs, proof, and a not-ready path; bounce should drop materially.
- **Calculator engagement** — the honest 5.25% default shows a qualifying deal; watch `calculator_complete` rate.
