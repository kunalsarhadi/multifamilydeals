# CLAUDE.md — Multi Family Deals Website

This file is read automatically at the start of every session. Do not remove it.

## The Business

**Multi Family Deals** is an Edmonton-based real estate investment firm run by brothers **Kunal Sarhadi** and **Ankit Sarhadi** — both licensed Real Estate Brokers. **Kunal is licensed in BOTH Alberta and Ontario** (residential + commercial); brokerages **Standard Realty Co., 14811 114 Ave NW, Edmonton, AB T5M 4E5** (Alberta) and **Homelife Miracle Realty Inc.** (Ontario). **Ankit Sarhadi is a licensed Real Estate Broker in ONTARIO ONLY** — brokerage **Homelife Miracle Realty Inc.** (Ontario); he is NOT licensed in Alberta and is NOT a "co-founder / client service" — give him the same "Real Estate Broker" title as Kunal, tagged Ontario. On team bios (about.html, reviews.html) Ankit carries the broker title. **Kunal's two brokerages render on two separate lines on team bios — Standard Realty Co. (AB) first, then Homelife Miracle Realty Inc. (ON).** Because Ankit is not AB-licensed, keep him off Alberta-specific credential/licensing claims. **Site-wide footer credential line remains Kunal-only (canonical):** "Kunal Sarhadi, Real Estate Broker | Standard Realty Co., Edmonton (AB) | Homelife Miracle Realty Inc. (ON)" — do not add Ankit to footers unless the owner asks. Genuine client testimonials that mention Ankit by name are fine to keep — those are real reviews.

The firm helps investors acquire purpose-built multi-family properties in Edmonton, Alberta using the **CMHC MLI Select** program — which offers 5% down and 50-year amortization on qualifying builds.

The target investor wants to scale to 50+ doors in 4 years.

## The Website

- **Live URL:** https://multi-family-deals.ca
- **Hosting:** GitHub Pages (the CNAME file points the domain to GitHub Pages)
- **Repository:** https://github.com/kunalsarhadi/multifamilydeals
- **Local files:** `/home/user/multifamilydeals/`
- **Default branch for deploys:** `main` — pushing to `main` makes changes live within 1–2 minutes
- **Feature branches:** use `fix/` or `feat/` prefix, merge to `main` when ready

## IMPORTANT: Deployment Rule

Changes to local HTML files do NOT affect the live site until pushed to `main` on GitHub.
Always tell the user whether a change is local-only or has been pushed live.

## Pages

| File | URL path | Purpose |
|---|---|---|
| `index.html` | `/` | Homepage |
| `about.html` | `/about` | The Strategy |
| `why-alberta.html` | `/why-alberta` | Why Alberta — market data, vacancy rates, migration |
| `inventory.html` | `/inventory` | Active property listings |
| `inglewood.html` | `/inglewood` | Portfolio — completed 9-plex project |
| `crawford-plains.html` | `/crawford-plains` | Portfolio — completed 8-plex Crawford Plains (newest; higher priority than Inglewood) |
| `buying-process.html` | `/buying-process` | Step-by-step buying process |
| `faq.html` | `/faq` | FAQ accordion |
| `reviews.html` | `/reviews` | Client reviews |
| `guide.html` | `/guide` | Free CMHC MLI Select investor guide (printable PDF) |
| `contact.html` | `/contact` | Book Strategy Call |
| `ontario-investors.html` | `/ontario-investors` | Landing page targeting Ontario investors |
| `blog/index.html` | `/blog/` | Blog index / listing page |
| `blog/cmhc-mli-select-guide.html` | `/blog/cmhc-mli-select-guide` | Blog: CMHC MLI Select deep-dive guide |
| `blog/edmonton-vs-toronto-multifamily.html` | `/blog/edmonton-vs-toronto-multifamily` | Blog: Edmonton vs Toronto multifamily comparison |
| `blog/scale-50-doors.html` | `/blog/scale-50-doors` | Blog: How to scale to 50 doors |
| `calculator.html` | `/calculator` | DSCR / pro-forma calculator (defaults: $2.0M 8-plex at 4%) |

(Plus additional blog posts not individually listed — see `blog/` and `sitemap.xml` for the full set. Sitemap is the canonical page list.)

## Site Architecture

- Plain HTML/CSS/JS — no build framework, no npm, no bundler
- All styles are inline `<style>` blocks inside each page's `<head>`
- **LIGHT-THEME REDESIGN (index.html + inventory.html + contact.html, July 2026):** these pages were redesigned into a **light editorial "private-wealth report" theme** — cream/brass, fonts **Newsreader (serif/numerals) + Space Grotesk (body/UI)**, tokens `--paper #F5F1E8 / --card #FBF8F1 / --ink #1C1813 / --accent #9C6B34 (brass) / --accent-l #C79A5E / --accent2 #B0563F / --espresso #16130E`. They are **intentionally different from the remaining pages** (about, why-alberta, calculator, faq, reviews, guide, contact, buying-process, ontario-investors, portfolio pages, blog — still dark navy/gold Cinzel/Josefin). Do NOT "fix" index.html, inventory.html, or contact.html back to navy/gold. The remaining pages are slated to be reskinned to this light theme in later phases. **contact.html preserves the real GHL form (`vP9PwFhTgisGUe7787YO` + `form_embed.js`), the GHL booking-completion postMessage → `form_submit_contact` listener, and Meta Contact tel/email tracking. NOTE: contact.html Kunal card keeps "160+ Google reviews" (matches the live site); the homepage trust strip currently says "Five-star client reviews" — reconcile these two if the owner wants one wording site-wide.** Homepage key sections: hero, trust strip, positioning, The Math (doors visual + comparison), interactive **plex explorer** (`data-plex` buttons → `data-plex-deposit/price/cash/units`), structural advantages, why-through-us, process, track record (Inglewood **delivering soon**), 10-month timeline, private-network WhatsApp strip, final CTA. All GTM/Meta/GHL/data-conversion plumbing preserved.
- **Inglewood status = DELIVERING SOON (not completed):** owner-confirmed July 2026. Homepage reflects this; appraisal claim is worded "**every sold project** has appraised above its purchase price" (NOT "completed/delivered"). NOTE: the other pages + shared nav still say Inglewood "Completed 2026" — this is a known inconsistency to correct site-wide in a follow-up.
- Fonts: Cinzel (headings) + Josefin Sans (body) via Google Fonts — **on all pages EXCEPT index.html** (see homepage redesign above)
- Color tokens: `--navy-deep`, `--navy-primary`, `--navy-card`, `--navy-alt`, `--navy-border`, `--gold`, `--gold-light`, `--gold-muted`, `--accent-warm`, `--text-primary`, `--text-muted`, `--text-subtle`, `--slate` (index.html only), `--status-live` (index.html only)
- Social: Instagram https://www.instagram.com/kunalsarhadi — Facebook https://www.facebook.com/multifamilydeals
- Public-facing brand name: **Multi Family Deals** (not Team Sarhadi — that is the personal/agent brand)
- Nav: `<nav>` → `.nav-inner` → `.nav-logo` (left) + `.nav-links` (middle) + `.nav-cta` (right)
- Mobile nav: `<div class="mobile-nav" id="mobileNav">` — toggled by `.hamburger` button
- Footer: consistent across all pages, links to all main pages (the footer "Portfolio" link points to crawford-plains.html — the newest completed project)
- crawford-plains.html gallery is LIVE: 15 grid images + a 53-photo lightbox, all embedded directly from the owner's Google Drive via `lh3.googleusercontent.com/d/<FILE_ID>=w1200` (nothing stored in the repo). CAUTION: if Drive sharing on that folder changes, the flagship gallery silently blanks — long-term, commit compressed webp copies to the repo like Inglewood
- Nav (July 22, 2026): first tab is "The Strategy" (Our Approach / Why Alberta / Track Record → about.html#track-record); Properties lists Crawford Plains 8-Plex above Inglewood 9-Plex; Resources order: Buying Process, Calculator, Free Guide, FAQ, Reviews, Blog; mobile nav has Book CTA + tel link at top
- Appraisal track record (about.html#track-record + strips on index/inventory/ontario/contact/calculator/guide/crawford/inglewood): DELTA-ONLY policy — never publish absolute appraised values or purchase prices (deltas + values would let anyone back-calculate purchase prices). Claim wording: "every completed project has appraised above its purchase price, $20K–$200K." Source: "independent AACI appraisal" (do not name the firm on-site). Letters are never published or sent — "on file, verification on request"
- **Buying process (canonical — from owner's Buying Process one-pager):** 9 steps — 1. Pre-Qualification (eligibility) → 2. Allocation Request (worksheet to builder) → 3. Due Diligence (preferred broker qualifies investor + project) → 4. Lender Satisfied (Letter of Intent) → 5. **Deal Firmed (first deposit to builder)** → 6. Preparation & Submission (awaiting CMHC Certificate of Insurance, 60–90 days) → 7. CMHC Acceptance (lawyer introduced for closing) → 8. Pre-Leasing Before Completion (property mgmt starts leasing) → 9. Project Completion. **buying-process.html already reflects this.** **The deal is firmed (deposit submitted) BEFORE the CMHC application is submitted — but do NOT spotlight that ordering in a way that could confuse or deter buyers.** Frame the deposit step as conditional on CMHC approval + project viability (deposit returned per the APS if CMHC declines), matching buying-process.html. **Homepage timeline (index.html) = ~10 months total, NOT 20 — most projects close within ~10 months.** Do not restore the old 20-month / firm-after-CMHC-approval timeline.
- Canonical mortgage math: STANDARD RATE IS 4% (owner decision, July 2026 — this is the firm's modeled MLI Select rate; do not change to 5.25%). All payment examples site-wide computed at 4% ($2M: ~$9,500/mo 30yr vs ~$7,700/mo 50yr, ~$1,800/mo delta; $1.5M: ~$7,150 vs ~$5,800, ~$1,375/mo). Whatever rate is shown, the dollar figures MUST compute to it — never state one rate while showing figures from another

## Key Market Data (update here when figures change)

- **Edmonton rental vacancy rate:** ~4%
- **Edmonton population growth:** Canada's fastest-growing major city 2023–2024
- **CMHC MLI Select down payment:** 5%
- **CMHC MLI Select amortization:** 50 years
- **Edmonton avg 2BR rent:** ~$1,600/mo
- **Edmonton avg detached home price:** ~$470K
- **Multi-family cap rates Edmonton:** ~4.5–5.5%
- **Ontario vacancy rate:** ~1.5%
- **BC vacancy rate:** ~0.9%
- **Alberta provincial sales tax:** None (no PST, no HST)
- **MLI Select points (canonical framing — keep consistent site-wide):** 50 points = minimum eligibility; 100 points = maximum benefits including 50-year amortization and highest LTV
- **Liquidity requirement (canonical — keep consistent site-wide):** liquid assets equal to ~10% of project price after deposit
- **Cash required for a 6-plex (canonical, owner-confirmed July 2026):** the 5% deposit falls in the **$80,000–$90,000 range** — always quote it as a range, never a single committed number, and NEVER say "all-in" or any phrasing that reads as a fixed total commitment. Legal/title/closing costs are additional and vary by deal (confirmed on the discovery call). Do not publish an all-in total.
- **Calculator default rate:** 4% (owner standard — matches the inventory disclaimer and all site payment examples)
- **Calculator — CMHC premium default:** 5.4% (owner decision, July 2026). No "5.8% typical at 95% LTV" helper text on the field.
- **Calculator — property tax estimate:** assessed value = **85% of purchase price** × Edmonton mill rate (1.01738%). `ASSESS_FACTOR = 0.85` in calculator.html (owner decision, July 2026 — was 75%).

## Content repetition budget (standing rule, July 2026 audit)

- Appraisal claim: max ONE contextual placement per page (full grid lives on about.html#track-record only)
- Trust bar ($500M/160+/500+): index, about, reviews, inventory, contact, ontario only — do not add elsewhere
- 5%/50yr/GST checklists: once per page, only where the program is the topic
- A given review quote appears on ONE page only

## Inventory counts are AUTO-CALCULATED

Do NOT hand-edit the Available / Sold Conditional / Previously Sold counts on inventory.html (status strip numbers, section headers, hero headline). A script near the bottom of inventory.html derives every count from the rendered cards at page load. To change inventory: add/move/remove the card itself — the numbers update themselves.

**Redesigned inventory.html (light theme, July 2026) count markup:** the JS counts `#propGrid [data-card]` (Available), `[data-sc]` cards + `[data-sc-extra="N"]` (Sold Conditional total), and `[data-sold]` cards (Previously Sold, shown as **"N+"**), then fills `#statAvail` / `#statSc` / `#statSold`, `#scHeaderCount`, `#soldBadgeCount`, and the hero `#availHeadline`. The Coming-Soon pipeline is a compact banner carrying `[data-cs-extra="N"]`. **The ONE inventory number not fully auto-derived: if the hidden Sold-Conditional count changes, update `data-sc-extra` (on the "+N more" dashed card); if the pipeline count changes, update `data-cs-extra` (on the Coming-Soon banner).** Previously Sold shows the live archive count + "+".

## Why Investors Choose Alberta (key talking points)

- No provincial sales tax (long-standing policy; NOT constitutionally mandated — never claim it is; why-alberta.html words this correctly)
- Lowest provincial income tax in Canada
- Edmonton home prices 40–50% below Toronto/Vancouver — preserves cap rates
- Canada's #1 interprovincial migration destination
- 200,000+ people moved to Alberta in 2024 — creates sustained rental demand
- New arrivals rent first — stable, employed tenants
- Purpose-built rental GST exemption applies to CMHC MLI Select builds
- Alberta New Home Warranty Program covers all builds
- CMHC MLI Select requires separate utility meters per unit — built to spec

## Inventory

- The "Last Updated" date on the inventory page updates automatically via JavaScript (`new Date()`) — no manual work needed
- Inventory data is managed in Google Sheets — see the **Google Sheets — Inventory Hotlist** section below for credentials and sync instructions

## Git Workflow

```bash
# Make changes to local files
git add <files>
git commit -m "description"
git push origin main   # this makes it live
```

Never push directly to main without reviewing changes first.
Use feature branches for multi-step work, merge to main when confirmed clean.

## Google Sheets — Inventory Hotlist

The live inventory data is managed in Google Sheets. Read it at the start of any inventory-related task.

- **Spreadsheet ID:** `1rv3GdNkdN89AmNthj1JeL2ulSgKL9x3NnIL7UxCbn20`
- **Tab name:** `CMHC MLI Inventory List`
- **API Key:** stored in `.env` as `SHEETS_API_KEY` (file is gitignored — never commit it)

**To read the sheet**, load the key from `.env` then fetch:
```
https://sheets.googleapis.com/v4/spreadsheets/1rv3GdNkdN89AmNthj1JeL2ulSgKL9x3NnIL7UxCbn20/values/CMHC%20MLI%20Inventory%20List?key=<SHEETS_API_KEY>
```

When the user says "sync inventory", "update inventory", or "update the hotlist":
1. Read `SHEETS_API_KEY` from `.env`
2. Fetch the sheet using the URL above with that key
3. Compare with current inventory.html
4. Update inventory.html to match the sheet
5. Commit and push to main

---

## Google Ads & GTM

**GTM Container:** `GTM-WBW5QJQT` — installed in `<head>` + `<noscript>` after `<body>` on ALL HTML pages (root + blog).

**Conversion tracking — `dataLayer` events fired on this site:**

| Event name | Trigger | Pages |
|---|---|---|
| `book_call` | Click on any CTA with `data-conversion="book_call"` | All pages (70+ instances) |
| `phone_click` | Click on phone number link | All pages |
| `whatsapp_click` | Click on WhatsApp link | contact, ontario-investors |
| `guide_download` | Click on guide/lead magnet CTA | guide.html, index.html, ontario-investors.html |
| `package_view` | Click "View Full Package" (Google Drive) on inventory cards | inventory.html (one per available card) — build Meta retargeting audience off this |
| `virtual_tour_view` | Click "Open Full Tour" (iGuide) | inglewood.html AND crawford-plains.html — **verify a GTM trigger exists** |
| `gallery_view` | Click "View All N Photos" buttons | crawford-plains.html (3 buttons) — **needs a GTM trigger** |
| `form_submit_contact` | GHL form submit (postMessage from iframe) | contact.html, guide.html |
| `calculator_start` | User begins DSCR calculator | calculator.html |
| `calculator_complete` | User completes DSCR calculator | calculator.html (includes `dscr` value) |

**Meta pixel events on guide.html:** `Lead` fires ONLY on actual GHL form submission (inside `triggerPdfDownload()`). Opening the download modal fires the custom event `GuideModalOpen`. Do not move `Lead` back to the modal-open click — that corrupts Meta ad optimization.

**Primary conversion pages (send traffic here):**
- `/contact` — Book Strategy Call (GHL form + chat widget)
- `/inventory` — Active listings (high intent)
- `/guide` — Free investor guide (lead magnet / top of funnel)
- `/ontario-investors` — Dedicated landing page for Ontario-based investors

**Key `data-conversion` attribute:** every CTA anchor and button has `data-conversion="<event>"`. The global listener is in the inline `<script>` before `</body>` on each page — it does `window.dataLayer.push({ event: e.currentTarget.dataset.conversion })`.

**Resolved July 2026:** all blog pages now carry the dataLayer conversion listener and the GHL chat widget. No known tracking gaps in HTML. Remaining verification (needs GTM/Meta account access): (1) confirm GTM has a trigger for `virtual_tour_view` and `package_view`; (2) confirm GTM does NOT also fire the Meta base pixel — the pixel IS hardcoded in every page's `<head>`, so a GTM-fired pixel would double-count PageViews.

---

## Meta (Facebook) Ads

**Meta Pixel ID:** `3083326175185716`

**Pixel placement:** the Meta base pixel IS hardcoded in the `<head>` of all HTML pages (init + PageView). GTM must NOT also fire the base pixel or PageViews double-count — verify in the GTM container.

**Audience signals on-site:**
- Primary audience: Ontario and BC investors priced out of local markets looking for cash-flowing Alberta multifamily
- Secondary: Alberta-based accredited investors wanting to scale doors
- Persona: 35–55, high income, entrepreneurial mindset, already owns at least one property

**Retargeting segments to build:**
- `/inventory` visitors (highest intent — browsing active listings)
- `/contact` visitors who did NOT submit (abandoned booking)
- `/guide` downloaders (top-of-funnel nurture)
- `/ontario-investors` visitors (geo-specific segment)

**Landing pages for ad traffic:**
- Ontario audiences → `/ontario-investors`
- General Canada → `/` or `/inventory`
- Warm/retargeting → `/contact`

**Creative tone:** premium, institutional, data-driven — NOT "get rich quick". The brand is sophisticated. Visuals: navy + gold palette, architectural imagery, Edmonton skyline. Tagline direction: "purpose-built wealth", "engineered for scale", "50 doors in 4 years".

**Social profiles:**
- Instagram: https://www.instagram.com/kunalsarhadi (Kunal's personal brand)
- Facebook Page: https://www.facebook.com/multifamilydeals

---

## GoHighLevel (GHL)

**GHL is the CRM, booking, and chat system for this site.**

### Form Embeds

| Page | Form ID | Purpose |
|---|---|---|
| `contact.html` | `vP9PwFhTgisGUe7787YO` | Book Strategy Call |
| `guide.html` | `w9WSkfoD0lYZLBl9fwv5` | Download Investor Guide (lead magnet) |

**Embed method:** `<iframe src="https://api.leadconnectorhq.com/widget/form/<ID>">` + `<script src="https://link.msgsndr.com/js/form_embed.js">`

**postMessage listener:** both contact.html and guide.html listen for `message` events from `leadconnectorhq.com` origin. On form submit, fires `dataLayer.push({ event: 'form_submit_contact' })` to GTM.

### Chat Widget

- **Widget ID:** `69fa444c3cc75785c76e6387`
- **Embed:** `<script defer src="https://beta.leadconnectorhq.com/loader.js" data-widget-id="69fa444c3cc75785c76e6387">`
- Installed on all pages in footer

### Workflows Connected

- **Contact form** (`vP9PwFhTgisGUe7787YO`) → triggers Strategy Call booking workflow in GHL
- **Guide form** (`w9WSkfoD0lYZLBl9fwv5`) → triggers lead magnet delivery + nurture sequence in GHL
- **Calendly is fully removed** — do not reference or re-add it. GHL is the sole booking and CRM path.

### Contact Details (used in forms and workflows)

- **Phone:** +14162007010
- **Email:** sales@teamsarhadi.com
- **WhatsApp group:** https://chat.whatsapp.com/BYNf65k8iSf3fNOIrkZUvZ
