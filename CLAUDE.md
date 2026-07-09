# CLAUDE.md — Multi Family Deals Website

This file is read automatically at the start of every session. Do not remove it.

## The Business

**Multi Family Deals** is an Edmonton-based real estate investment firm run by **Kunal Sarhadi**, Real Estate Broker at Homelife Miracle Realty Inc., and his brother **Ankit Sarhadi**.

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

## Pages (15 total)

| File | URL path | Purpose |
|---|---|---|
| `index.html` | `/` | Homepage |
| `about.html` | `/about` | The Strategy |
| `why-alberta.html` | `/why-alberta` | Why Alberta — market data, vacancy rates, migration |
| `inventory.html` | `/inventory` | Active property listings |
| `inglewood.html` | `/inglewood` | Portfolio — completed 9-plex project |
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

## Site Architecture

- Plain HTML/CSS/JS — no build framework, no npm, no bundler
- All styles are inline `<style>` blocks inside each page's `<head>`
- Fonts: Cinzel (headings) + Josefin Sans (body) via Google Fonts
- Color tokens: `--navy-deep`, `--navy-primary`, `--navy-card`, `--navy-alt`, `--navy-border`, `--gold`, `--gold-light`, `--gold-muted`, `--accent-warm`, `--text-primary`, `--text-muted`, `--text-subtle`, `--slate` (index.html only), `--status-live` (index.html only)
- Social: Instagram https://www.instagram.com/kunalsarhadi — Facebook https://www.facebook.com/multifamilydeals
- Public-facing brand name: **Multi Family Deals** (not Team Sarhadi — that is the personal/agent brand)
- Nav: `<nav>` → `.nav-inner` → `.nav-logo` (left) + `.nav-links` (middle) + `.nav-cta` (right)
- Mobile nav: `<div class="mobile-nav" id="mobileNav">` — toggled by `.hamburger` button
- Footer: consistent across all pages, links to all main pages

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
- **Calculator default rate:** 5.25% (matches the inventory disclaimer's 5.25–5.50% modeling; do not lower it)

## Inventory counts are AUTO-CALCULATED

Do NOT hand-edit the Available / Sold Conditional / Coming Soon counts on inventory.html (status pills, section headers, scarcity block). A script at the bottom of inventory.html counts the `.asset-badge` elements per section at page load and fills every count. To change inventory: add/move/remove the card itself — the numbers update themselves.

## Why Investors Choose Alberta (key talking points)

- No provincial sales tax (written into Alberta's constitution — not a policy that can be reversed)
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

**GTM Container:** `GTM-WBW5QJQT` — installed in `<head>` + `<noscript>` after `<body>` on all 20 HTML files.

**Conversion tracking — `dataLayer` events fired on this site:**

| Event name | Trigger | Pages |
|---|---|---|
| `book_call` | Click on any CTA with `data-conversion="book_call"` | All pages (70+ instances) |
| `phone_click` | Click on phone number link | All pages |
| `whatsapp_click` | Click on WhatsApp link | contact, ontario-investors |
| `guide_download` | Click on guide/lead magnet CTA | guide.html, index.html, ontario-investors.html |
| `package_view` | Click "View Full Package" (Google Drive) on inventory cards | inventory.html (9 links) — added July 2026; build Meta retargeting audience off this |
| `virtual_tour_view` | Click "Open Full Tour" (iGuide) | inglewood.html — **verify a GTM trigger exists for this event** |
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
