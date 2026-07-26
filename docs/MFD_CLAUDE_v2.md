# CLAUDE.md — Multi Family Deals (master context)
**v2 — July 2026.** Business, brand, and compliance context for any Claude surface. (The website repo keeps its own detailed build-level CLAUDE.md; this is the general master.)

## The Business
**Multi Family Deals** (multi-family-deals.ca) is an Edmonton-based multi-family investment firm founded by **Kunal Sarhadi — Real Estate Broker, licensed in BOTH Alberta and Ontario.**
- **Alberta:** Standard Realty Co. — 14811 114 Ave NW, Edmonton, AB T5M 4E5
- **Ontario:** Homelife Miracle Realty Inc. — 821 Bovaird Dr W Unit 31, Brampton, ON L6X 0T9

The firm helps out-of-province investors acquire purpose-built multi-family properties in Edmonton using **CMHC MLI Select** — as low as 5% down and up to 50-year amortization on qualifying builds. Target investor goal: **50+ doors in ~4 years.**

**Ankit Sarhadi** (Kunal's twin) is a licensed broker in **Ontario only** and runs a **separate business, VIP New Homes** (Ontario pre-con + GTA resale). Shared "Team Sarhadi" parent identity; two distinct verticals. **Default to Multi Family Deals / Alberta.** On the MFD website, Ankit appears on **reviews.html only**; genuine testimonials naming him stay.

Contact: **416-200-7010 | sales@teamsarhadi.com** · WhatsApp group + GHL chat for nurture.

## Track record (public — verified)
- **$500M+ real estate sold (combined Sarhadi Group)** — always keep the qualifier
- **160+ verified Google reviews** · **500+ families served**
- Do not claim "premier / #1 / Top 1%" without a named source.

## Brand voice
Premium editorial, confident, numbers-forward; Ontario-vs-Alberta contrast framing. Signatures: *"We don't sell properties. We build portfolios." · "The math is not close."* Retiring the old hype ("ANOTHER WIN!") style. Say **"discovery call,"** not "strategy call."

## Visual brand system (current website)
Light editorial "private-wealth report." **Retired:** navy/gold + Cinzel/Josefin.
- **Palette:** paper `#F5F1E8` · card `#FBF8F1` · alt `#EFE9DB` · ink `#1C1813` · body `#4A443B` · muted `#6E6656` · dividers `#DDD4C2`/`#E4DBCB` · **brass (accent) `#9C6B34`** · brass-deep `#7A5326` · brass-light `#C79A5E` · terracotta `#B0563F` · espresso (dark sections) `#16130E` · footer `#0E0C09` · green (positive) `#2C8F5E`.
- **Fonts:** **Newsreader** (serif — headings + all numerals/stats) + **Space Grotesk** (body/UI/labels). Google Fonts.
- **Principles:** cream canvas, one brass accent, espresso dark sections, oversized serif numerals, uppercase spaced labels, generous whitespace, hairline dividers, **no gradients/shadows/decorative borders.**

## Key numbers (never invent)
- **As low as 5% down** (where DSCR clears 1.10) · up to 95% CMHC · **50-yr amortization** (vs **30-yr** conventional — never 25) · DSCR 1.10 min (1.15–1.27 active) · **modeled rate 4%.**
- **Social Outcomes points: 50 = minimum, 100 = maximum terms.** **Affordability: ~25% of units.**
- Entry capital $80K–$155K · closing $8K–$15K · **7–8% total cash to close** · 10% post-deposit liquidity · 25% net worth (Canadian assets) · 680 credit.
- Deposit ranges: 6-plex $80–90K · 7-plex $100–105K · 8-plex $110–125K · 9-plex $130–140K · 10-plex $140–155K (**range, never "all-in"**).
- Projected cashflow (not guaranteed): 6 $13–20K · 7 $17–20K · 8 $21–27K · 9 **$21–31K** · 10 $30–37K.
- Alberta: ~4% vacancy · strong interprovincial migration (soften "#1") · 200K+/yr inbound · ~40–50% lower prices vs Toronto · **$0 HST, $0 LTT, no Ontario-style dev charges.**
- Appraisals: **delta-only** — "every sold project appraised above purchase, $20K–$200K" (never absolute values; independent AACI; letters on file).

## Compliance guardrails (must-follow)
- No "guaranteed / risk-free / locked in." No "you qualify / you'll cashflow $X" — only CMHC & lender qualify; use **"projected."** No "we get you approved."
- **Letter of Intent = pre-approval** — never portray as confirming/guaranteeing financing structure.
- Deposit conditional on **project viability only**; refunded per APS **only if the project is declined due to project viability** (not buyer-caused credit/bankruptcy).
- **GST exemption: subject to CRA eligibility.**
- Alberta no-LTT/no-PST = **long-standing policy, NOT constitutional.**
- Equity recycling: **"refinancing or a HELOC"** — never "Pari Passu."
- Broker = **preferred partner, paid by the lender** — not "$0 fees."
- Ankit: Ontario-only; keep him off Alberta credentials; MFD site = reviews.html only.

## Projects
- **Crawford Plains 8-plex** — newest; complete build, **now pre-leasing before closing** (not closed — never "completed/delivered/turnkey/sold"). Back-to-back townhome (2 identical buildings). Independent as-if-complete appraisal +$100K over purchase.
- **Inglewood 9-plex** — **delivering soon** (not completed). Proof/case-study project.

## Investor archetypes
Primary: **French-speaking professionals** (PhDs, senior govt, capital firms) — full French channel (Sophie Voice AI + French calendar; route on explicit language signal only). Secondary: capital-firm partners/operators. Tertiary: out-of-province first-time couples (Toronto).

## Tech / infrastructure
GoHighLevel (CRM/workflows) · Zoya Voice AI (EN, 8am–8pm Toronto) · Sophie Voice AI (FR discovery) · MFD Concierge AI (SMS, Auto Pilot) · WhatsApp · FB/IG ads · Gmail · Canva. Master KB = single source of truth across the three AIs.
IDs: GHL locationId `9Qke2MKLac4hNcKlcN86` · Meta Pixel/Dataset `3083326175185716` · GHL chat `69fa444c3cc75785c76e6387` · forms: contact `vP9PwFhTgisGUe7787YO`, guide `w9WSkfoD0lYZLBl9fwv5` · timezone America/Toronto. **Meta base pixel is hardcoded in each page `<head>`; GTM `GTM-WBW5QJQT` must not double-fire it.** Calendly is fully removed — GHL is the sole booking path.

## Website (for build work)
Plain HTML/CSS/JS on GitHub Pages; inline `<style>` per page; light theme site-wide (all root pages + full blog). Deploy = push to `main` (live in 1–2 min). Inventory counts auto-calculate from cards on inventory.html. Full build-level detail lives in the repo's own CLAUDE.md.
