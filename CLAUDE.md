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
- Color tokens: `--navy-deep`, `--navy-primary`, `--navy-card`, `--navy-border`, `--gold`, `--gold-light`, `--gold-muted`, `--text-primary`, `--text-muted`, `--text-subtle`
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
