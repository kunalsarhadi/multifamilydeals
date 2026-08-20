# CLAUDE.md — Multi Family Deals Website

This file is read automatically at the start of every session. Do not remove it.

## The Business

**Multi Family Deals** is an Edmonton-based real estate investment firm run by brothers **Kunal Sarhadi** and **Ankit Sarhadi** — both licensed Real Estate Brokers. **Kunal is licensed in BOTH Alberta and Ontario** (residential + commercial); brokerages **Standard Realty Co., 14811 114 Ave NW, Edmonton, AB T5M 4E5** (Alberta) and **Homelife Miracle Realty Inc.** (Ontario). **Ankit Sarhadi is a licensed Real Estate Broker in ONTARIO ONLY** — brokerage **Homelife Miracle Realty Inc.** (Ontario); he is NOT licensed in Alberta and is NOT a "co-founder / client service" — give him the same "Real Estate Broker" title as Kunal, tagged Ontario. Ankit carries the broker title on reviews.html ONLY. **Owner decision (July 2026): Ankit's name/mention is removed from every other page (about.html, guide.html, etc.) — he appears on reviews.html only.** Genuine client testimonials naming Ankit stay. **Kunal's two brokerages render on two separate lines on team bios — Standard Realty Co. (AB) first, then Homelife Miracle Realty Inc. (ON).** Because Ankit is not AB-licensed, keep him off Alberta-specific credential/licensing claims. **Site-wide footer credential line remains Kunal-only (canonical):** "Kunal Sarhadi, Real Estate Broker | Standard Realty Co., Edmonton (AB) | Homelife Miracle Realty Inc. (ON)" — do not add Ankit to footers unless the owner asks. Genuine client testimonials that mention Ankit by name are fine to keep — those are real reviews.

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
| `crawford-plains.html` | `/crawford-plains` | Portfolio — 8-plex Crawford Plains (newest; **complete build, now pre-leasing before closing** — NOT yet closed; higher priority than Inglewood) |
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
| `dual-income-homes.html` | `/dual-income-homes` | **Dual Income Homes, Leduc — second product line, NON-MLI (conventional financing)** |

(Plus additional blog posts not individually listed — see `blog/` and `sitemap.xml` for the full set. Sitemap is the canonical page list.)

## Site Architecture

- Plain HTML/CSS/JS — no build framework, no npm, no bundler
- All styles are inline `<style>` blocks inside each page's `<head>`
- **LIGHT-THEME REDESIGN (SITE-WIDE — COMPLETE, July 2026):** the **entire site** is now on the **light editorial "private-wealth report" theme** — cream/brass, fonts **Newsreader (serif/numerals) + Space Grotesk (body/UI)**, tokens `--paper #F5F1E8 / --card #FBF8F1 / --ink #1C1813 / --accent #9C6B34 (brass) / --accent-l #C79A5E / --accent2 #B0563F / --espresso #16130E / --green #2C8F5E`. **All pages are light theme now:** index, inventory, contact, ontario-investors, why-alberta (first wave) **plus** about, reviews, buying-process, faq, guide, crawford-plains, inglewood, calculator, and the **entire blog (index + 13 posts)** (second wave). Cinzel/Josefin dark navy/gold is fully retired. Do NOT "fix" any page back to navy/gold. The old color tokens (`--navy-*`, `--gold*`) are no longer used except as leftover CSS var aliases in a few ported files. **contact.html preserves the real GHL form (`vP9PwFhTgisGUe7787YO` + `form_embed.js`), the GHL booking-completion postMessage → `form_submit_contact` listener, and Meta Contact tel/email tracking. Trust/review wording is now consistent site-wide: "160+ · Verified Google reviews" (homepage strip, contact card, ontario proof band). Inglewood nav dropdown desc is "Set the standard" (status wording removed — both Inglewood and Sherwood are delivering soon). ontario-investors.html keeps the `guide_download` CTA (final CTA + footer + mobile nav) and the real Toronto client testimonial.** Homepage key sections: hero, trust strip, positioning, The Math (doors visual + comparison), interactive **plex explorer** (`data-plex` buttons → `data-plex-deposit/price/cash/units`), structural advantages, why-through-us, process, track record (Inglewood **delivering soon**), 10-month timeline, private-network WhatsApp strip, final CTA. All GTM/Meta/GHL/data-conversion plumbing preserved.
- **LIGHT-THEME PAGE BUILD CHECKLIST (apply to EVERY redesigned page — desktop AND mobile; owner standing instruction, July 2026):** when porting a new design/zip to a page, always include:
  1. **iOS/mobile polish (REQUIRED, non-negotiable):** (a) fixed nav gets GPU-layer promotion `transform: translateZ(0); -webkit-backface-visibility: hidden;` — this is the fix for the iOS Safari bug where a `position:fixed` nav with `backdrop-filter: blur()` stops repainting/responding during momentum scroll ("nav deactivates until you reload"). (b) `html { scroll-padding-top: 84px; }` so anchor-link jumps clear the 72px fixed nav. (c) any horizontally-scrolling table gets `-webkit-overflow-scrolling: touch` + a mobile-only `.swipe-hint` ("← Swipe the table to see all columns →", `display:none` desktop / shown ≤760px). (d) fixed multi-col grids (e.g. incentives 4-col, qualify 3-col) get mobile breakpoints (2-col ~860px, 1-col ~520px). (e) `@media (prefers-reduced-motion: reduce)` guard.
  2. **Preserve ALL plumbing:** GTM head+noscript, Meta base pixel + the tel/email `Contact` tracking, GHL chat widget, page-correct `canonical`/OG/Twitter + **every** JSON-LD block, favicons, `facebook-domain-verification`, and all `data-conversion` hooks that page needs (`book_call`/`phone_click`/`whatsapp_click`, plus `package_view` on inventory, `guide_download` where a guide CTA exists, GHL form + `form_submit_contact` on contact) + the global dataLayer listener.
  3. **Consistent shared UI:** real dropdown nav (The Strategy / Properties / Resources; Inglewood desc "Set the standard") + full footer + mobile hamburger (`#mobileNav`); standard WhatsApp bar — *"Private Investor Network — new listings reach our WhatsApp group before they appear anywhere else."* + **"Join the Network"**.
  4. **Compliance wording:** "as low as 5% down", "every sold project" appraisal (delta-only $20K–$200K), Kunal AB&ON / Ankit ON-only broker, no Calendly, 4% modeled rate, deposit/cash as RANGES (never a committed "all-in" total).
  5. **Verify before push:** headless desktop + mobile render, 0 console errors, no horizontal overflow, all interactions work. Build on a `feat/` branch, show screenshots, then push to `main` + the dev branch.
- **Inglewood status = DELIVERING SOON (not completed):** owner-confirmed July 2026. All redesigned light pages + the shared nav (site-wide) now reflect this — nav dropdown desc is "Set the standard" and the appraisal claim reads "**every sold project** has appraised above its purchase price" (NOT "completed/delivered"). inglewood.html status labels/meta flipped to "delivering soon" (July 2026 sweep). **Crawford Plains status = COMPLETE BUILD, NOW PRE-LEASING BEFORE CLOSING (NOT yet closed) — owner-confirmed July 2026.** Do NOT describe Crawford as "completed project / delivered / turnkey / sold"; use "complete — now pre-leasing before closing." crawford-plains.html + the site-wide nav dropdown desc ("Newest project · pre-leasing 2026") now reflect this. The build (construction/interiors) IS complete, so "photographed on completion of the build" and the appraisal-at-build-completion are fine; only the sale/closing is pending. The "Now Renting" hero photo shows a duplex-style face — unit count left at "8-Plex" pending owner confirmation (flag before changing). The blog case study "Anatomy of a Completed Edmonton 8-Plex" was left as-is (describes the completed build); revisit if owner wants.
- Fonts: **Newsreader (serif/headings/numerals) + Space Grotesk (body/UI)** via Google Fonts, site-wide (light-theme redesign complete). Cinzel + Josefin Sans are retired.
- Color tokens: `--navy-deep`, `--navy-primary`, `--navy-card`, `--navy-alt`, `--navy-border`, `--gold`, `--gold-light`, `--gold-muted`, `--accent-warm`, `--text-primary`, `--text-muted`, `--text-subtle`, `--slate` (index.html only), `--status-live` (index.html only)
- Social: Instagram https://www.instagram.com/kunalsarhadi — Facebook https://www.facebook.com/multifamilydeals
- Public-facing brand name: **Multi Family Deals** (not Team Sarhadi — that is the personal/agent brand)
- Nav: `<nav>` → `.nav-inner` → `.nav-logo` (left) + `.nav-links` (middle) + `.nav-cta` (right)
- Mobile nav: `<div class="mobile-nav" id="mobileNav">` — toggled by `.hamburger` button
- Footer: consistent across all pages, links to all main pages (the footer "Portfolio" link points to crawford-plains.html — the newest project, now pre-leasing before closing)
- crawford-plains.html gallery is LIVE and **now self-hosted** (July 2026): the 53 photos are committed as compressed webp in `images/crawford/{upper1,upper2,lower}/NN.webp` (2.6 MB total, max 1600px, q82), served locally like Inglewood. The gallery loads the local webp first and **falls back to the owner's Google Drive** (`lh3.googleusercontent.com/d/<FILE_ID>=w1600`, IDs still in the `SUITES` object) if a local file is missing, then to a "open the 3D tour" placeholder. So Drive sharing changes can no longer silently blank the gallery. To refresh photos: re-run `scripts/localize-crawford-gallery.py` (or re-download from the Drive folder `1fIFGyGz1ET0XyGSQbSxXxdSQ6Q4D6PAk` → subfolders "1. Upper Unit 1"/"2. Upper Unit 2"/"3. Lower Unit") and overwrite the webp files
- Nav (July 22, 2026): first tab is "The Strategy" (Our Approach / Why Alberta / Track Record → about.html#track-record); Properties lists Crawford Plains 8-Plex above Inglewood 9-Plex; Resources order: Buying Process, Calculator, Free Guide, FAQ, Reviews, Blog; mobile nav has Book CTA + tel link at top
- Appraisal track record (about.html#track-record + strips on index/inventory/ontario/contact/calculator/guide/crawford/inglewood): DELTA-ONLY policy — never publish absolute appraised values or purchase prices (deltas + values would let anyone back-calculate purchase prices). Claim wording: "every sold project has appraised above its purchase price, $20K–$200K" (standardized to "sold", not "completed", July 2026). Source: "independent AACI appraisal" (do not name the firm on-site). Letters are never published or sent — "on file, verification on request"
- **Buying process (canonical — from owner's Buying Process one-pager):** 9 steps — 1. Pre-Qualification (eligibility) → 2. Allocation Request (worksheet to builder) → 3. Due Diligence (preferred broker qualifies investor + project) → 4. Lender Satisfied (Letter of Intent) → 5. **Deal Firmed (first deposit to builder)** → 6. Preparation & Submission (awaiting CMHC Certificate of Insurance, 60–90 days) → 7. CMHC Acceptance (lawyer introduced for closing) → 8. Pre-Leasing Before Completion (property mgmt starts leasing) → 9. Project Completion. **buying-process.html already reflects this.** **The deal is firmed (deposit submitted) BEFORE the CMHC application is submitted — but do NOT spotlight that ordering in a way that could confuse or deter buyers.** Frame the deposit step as **conditional on PROJECT VIABILITY only** (NOT "CMHC approval") — deposit returned per the APS **only if the project is declined due to project viability**, NOT if the decline is buyer-caused (credit/bankruptcy). Owner-confirmed July 2026. **Also: never describe or portray the Letter of Intent as "confirming/guaranteeing the financing structure" (an LOI is a pre-approval, not a guarantee) — just name it; the owner explains it on the call.** These are applied site-wide (index timeline, buying-process.html steps 4/5 + protection box + JSON-LD, guide.html risk box, faq.html) — do not reintroduce "conditional on CMHC approval / if CMHC doesn't approve → refund" or "confirming the financing structure" anywhere. **Homepage timeline (index.html) = ~10 months total, NOT 20 — most projects close within ~10 months.** Do not restore the old 20-month / firm-after-CMHC-approval timeline.
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
- **Liquidity requirement (canonical — owner-confirmed Aug 2026, corrected):** liquid assets equal to **~10% of project price in total, with the 5% deposit counted INSIDE that 10%** — i.e. the deposit plus roughly a further 5%, NOT 5% + 10% = 15%. The earlier note here said "~10% after deposit", which was wrong and had put 15% into faq.html (visible answer + JSON-LD), inventory.html and buying-process.html; all corrected. The Eligibility one-pager's worked example is authoritative (on a $2.35M eight-plex: $235,000 liquidity required, $117,500 deposit drawn from it). **The one-pagers themselves have been corrected (Aug 2026)** — the Advantages PDF said "10% post-deposit liquidity" and the French Avantages said "liquidités de 10 % après la mise de fonds"; both now read "10% liquidity including the deposit" / "liquidités de 10 % du prix, mise de fonds incluse". Corrected files are in `docs/pdf-fixes/` — upload them to Drive as **new versions** of the existing files (Manage versions → Upload new version) so the file IDs and share links survive. **Still uncorrected: `5. Frequently Asked Questions.pdf`** — its "Who is eligible?" answer reads "the 5% deposit on hand, ~10% of project price in liquid reserve", which scans as additive.
- **PDF one-pagers are outlined text** (0 text layer, ~1500 vector paths/page) and no editable source exists in Drive. To edit one: measure the target line's baseline and x from `get_drawings()` path bboxes, erase with a `draw_rect` fill of `#F4F0E8`, and re-set the line in **Space Grotesk Regular at 7.86pt, colour `(0.29, 0.2667, 0.2314)`, pen x = 90.92** (solved by pixel-matching a re-typeset copy of the original line; verified against both the English and French one-pagers). Always diff the rendered pages afterwards to confirm only the intended region changed.
- **Cash required for a 6-plex (canonical, owner-confirmed July 2026):** the 5% deposit falls in the **$80,000–$90,000 range** — always quote it as a range, never a single committed number, and NEVER say "all-in" or any phrasing that reads as a fixed total commitment. Legal/title/closing costs are additional and vary by deal (confirmed on the discovery call). Do not publish an all-in total.
- **Calculator default rate:** 4% (owner standard — matches the inventory disclaimer and all site payment examples)
- **Calculator — CMHC premium default:** 5.4% (owner decision, July 2026). No "5.8% typical at 95% LTV" helper text on the field.
- **Calculator — property tax estimate:** assessed value = **85% of purchase price** × Edmonton mill rate (1.01738%). `ASSESS_FACTOR = 0.85` in calculator.html (owner decision, July 2026 — was 75%).

## Dual Income Homes — second product line (NON-MLI, owner-added July 2026)

`dual-income-homes.html` markets a **separate product** from the CMHC MLI Select multi-family inventory. It exists for investors who **do not have the net worth to qualify for MLI Select** — the owner's words. Do not merge it into the MLI inventory or apply MLI framing to it.

- **What it is:** brand-new detached homes in **Leduc, Alberta** — a 1,410 sq ft upper home (3 bed · 2.5 bath) over a 595 sq ft **legal** basement suite (1 bed · 1 bath). Two rents, **one title, one ordinary residential mortgage**. From **$499,000**.
- **NOT MLI Select.** This is **conventional financing** — 20% down, 30-year amortization, no mortgage insurance premium. **Never** import MLI framing onto this page: no 50-year amortization, no "as low as 5% down", no up-to-95% LTV, no points scoring. Underwriting is led by personal income, credit and net worth alongside the documented rents; eligibility and final terms vary by applicant and are subject to lender approval.
- **Availability: 8 homes, possession Summer 2027** (owner-confirmed July 2026). This count is **hand-maintained** — unlike inventory.html there are no per-unit cards to derive it from. It appears in **two places**: the hero pill on dual-income-homes.html and the promo band on inventory.html. Update both. The owner said he will tell us when any of the 8 move or sell — **do not change the number on your own initiative.**
- **Interest rate default is 3.79%**, not the site's 4% MLI figure. That is deliberate: 4% is the firm's modeled *MLI Select* rate, and this product is conventionally financed. The calculator recomputes live, so every figure stays consistent with whatever rate is shown.
- **Property tax uses a 0.75 assessed-value factor x 0.9395% mill rate** — deliberately different from calculator.html's `ASSESS_FACTOR = 0.85` x Edmonton's 1.01738%, because this property is in **Leduc, not the City of Edmonton** (owner-confirmed). **Do not "reconcile" the two factors.** Neither the factor nor the mill rate is surfaced in the UI — the field reads "Property tax / year" only.
- **Design source of truth is the owner's design handoff zip** (`MFD_Dual_Income.zip` → `Dual Income Homes.dc.html`). The page is a direct port of that prototype's markup and inline styles. **Do not restyle it or add UI the prototype does not have** — an earlier attempt added a cap-rate / cash-on-cash / DSCR returns row and the owner had it removed ("doesn't get asked in non-MLI product"). The only additions kept are the responsive rules the handoff itself listed as outstanding (results panel unsticks below 1000px, paired inputs stack, outlook table scrolls with a swipe hint, reduced-motion guard).
- **Grid track minimums matter:** Features & Finishes and Why This Works use a **380px** minimum so they lay out **3 + 3**. A smaller minimum fits 4 and the owner will flag it. Metric/stat strips live **inside** the 1240px container — never full-bleed to the viewport edge.
- **Number formatting:** purchase price and both rents display with thousands separators (499,000 / 2,200 / 1,200), formatted on load and blur, stripped on focus so typing is not interrupted.
- **Linked from** the Properties nav dropdown, mobile nav and footer across all root pages, the footer on every blog page, `sitemap.xml`, and a dark promo band on inventory.html. That band sits **outside `#propGrid` and carries no count hooks**, so the auto-derived MLI counts are unaffected — keep it that way.
- **No conversion event of its own** (owner decision, July 2026): its CTAs fire the standard `book_call` / `phone_click`. The owner markets this link to audiences whose contact details he already has, so a separate `dual_income_lead` event was judged unnecessary. Do not add one unasked.
- **Copy rules:** first person as Kunal; buyers are **"out-of-town"**, never "out-of-province"; never promise cash flow (figures are projected / pre-tax pro-forma / subject to lender approval); everything listed as included **is** included at $499,000 (no "optional"/"future"/"rough-in" language); keep the "Illustrations are artist's impressions. E.&O.E." and specifications-subject-to-change lines.

## Build Progress page (`build-progress.html`, added Aug 2026)

Construction proof page — dated site photography and clips from nine live projects, organised around an 8-month build arc. Its whole premise is that **nothing on it is a rendering** (the counterweight to inventory.html, which is all artist's renderings). Linked from the Properties nav dropdown, mobile nav and footer site-wide, plus `sitemap.xml`.

- **Design source of truth: `MFD__Website.zip` → `Build Progress.dc.html`** (a React prototype, inline styles only). Re-expressed as classes; colours, type sizes, spacing and copy lifted verbatim.
- **The page is GENERATED.** Do not hand-edit `<main>` — edit `scripts/build-progress-data.json` and re-run `python3 scripts/generate-build-progress.py`, then splice the produced `<main>` in. The `<style>` and `<script>` blocks live in the page and are edited directly. Static HTML is deliberate: every other page here is readable with JS off, and a client-rendered page would be an empty shell to crawlers.
- **Two different plate rules — do not mix them.** Lead and second-column plates carry the media's OWN aspect ratio with `object-fit: contain` (never cropped, never bucketed to a preset). Rail thumbnails and timeline stops are a uniform **4:3 with `cover`** — that is what keeps a rail from going ragged. An inline ratio leaking onto a 4:3 thumbnail was the original "images sized weird" bug.
- **A project's `video` is a property SEPARATE from `media`.** It fills the second column and suppresses `secondary`. Ignoring it silently drops clips.
- **Clips are click-to-play**, `preload="none"`, `src` attached on first click, poster frames committed alongside. Never autoplay, never preload — the library is ~47 MB. Clip paths are fixed by convention: poster = clip filename with `.mp4` → `-poster.jpg`.
- **Images load eagerly.** Do NOT add `loading="lazy"` or gate them behind IntersectionObserver — the handoff is explicit that this rendered as empty black plates.
- Media lives in `images/build/**` (24 photos) and `media/<project>/*.mp4` + `-poster.jpg` (10 clips). Owner supplies clips as unlabelled uploads; match them by extracting frames with `imageio_ffmpeg` and comparing against the committed posters — filenames carry no meaning.
- **Contrast floor:** muted greys on this page were promoted to `#6F695C` (>=4.5:1 on paper/card/alt) and `#847D6E` on espresso. `#8A8172` and `#A79E8E` fail on light backgrounds — do not revert them.
- Carries the standard WhatsApp bar (in the generator, not just the page) and `book_call` / `phone_click` / `whatsapp_click`. No conversion event of its own.

## Client representation — NEVER claim it (standing rule, July 2026)

**Never write copy that describes the firm, Kunal, or Ankit as representing the reader.** This applies to every page, blog post, guide, PDF, ad, and message template.

Banned phrasings (and anything equivalent): "represent you", "we represent our clients", "your agent", "your representative", "acting for you", "we act on your behalf", "buyer representation", "buyer's agent", "we work for you", "our client" used to mean the site visitor, and any language implying an agency or fiduciary relationship with the reader.

**Write the role in service terms instead:** we source, screen, model, coordinate, introduce, submit, and manage. Those are accurate and carry the same credibility.

**Dual AB/ON licensing is still a selling point** — cite it as market knowledge and professional standing ("licensed in both Alberta and Ontario, so I work in both of the markets you're weighing"), never as "I can represent you in both provinces."

**Not affected:** the site-wide disclaimer phrase "nothing shown here is an offer or a binding representation" (a legal term of art), and "representative" meaning illustrative/typical. Leave both alone.

Audited July 2026: the only violation was one line in the homepage founder block; it has been rewritten. Re-run a sweep for the banned phrasings above after any large copy change.

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
- Among Canada's strongest for interprovincial migration (soften '#1' without a named source)
- 200,000+ people moved to Alberta in 2024 — creates sustained rental demand
- New arrivals rent first — stable, employed tenants
- Purpose-built rental GST exemption may apply to qualifying CMHC MLI Select builds (subject to CRA eligibility)
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

**NOTE:** `.env` is gitignored, so a fresh clone (every Claude Code on the web session) has **no** `SHEETS_API_KEY`. In that case read the sheet through the **Google Drive connector** instead: `read_file_content` with fileId `1rv3GdNkdN89AmNthj1JeL2ulSgKL9x3NnIL7UxCbn20`. It renders the tab as a markdown table.

### Hotlist scope — ONLY the lines the owner names (owner instruction, July 2026)

**Do not proactively reconcile the site against the hotlist.** Sync only the specific line(s) the owner names, and nothing else in the sheet.

The sheet and the site legitimately disagree: the owner gives status changes verbally (e.g. Glenwood, Pleasantview, and the Mill Woods 6- and 7-plex are marked sold/sold-conditional on the site while the sheet still shows them AVAILABLE). **The site is correct in those cases.** Do not "fix" the site to match the sheet, and do not keep raising the discrepancy — it has been flagged and the owner has accepted it.

### "Sync line N" — the owner's standing workflow (owner instruction, July 2026)

When the owner says **"line N on the hotlist is a new inventory"** / **"sync line N"**, do the whole job without asking: publish that listing to inventory.html **with its Drive package link AND its elevation image**.

1. **Read the sheet** (Drive connector, above). Columns: PROPERTY TYPE · STATUS · PACKAGE · NEIGHBORHOOD · REGION · CASH FLOW · DSCR · TOTAL DEPOSIT · DEPOSIT STRUCTURE · COMPLETION DATE.
2. **Resolve the row.** The Drive markdown render is **off by one** versus real sheet rows (owner's "line 60" = the 61st rendered row). So don't trust the count alone — the target is the AVAILABLE row that is **not yet on inventory.html**, normally the **last** row of the AVAILABLE block (new listings are appended). Cross-check the neighborhood against the site before building. Only ask if two candidates both fit.
3. **Get the Drive package folder.** The sheet's PACKAGE cell is a hyperlink, and **the text export strips URLs** — you will not see it in the sheet content. Find it instead by searching Drive for a folder titled like the property: `title contains '<NEIGHBORHOOD>' and mimeType = 'application/vnd.google-apps.folder'`. Naming convention is `8Plex <Neighborhood>` (watch for older same-name folders — pick the one whose `createdTime` is newest / matches the new listing). Folders live under parent `1klHG36SRQQRNNmjuHKYsVYGfXFFhkoyU`.
4. **Get the image.** Each package folder holds `5. Elevation.png` (alongside `1. Brochure.pdf`, `2. Proforma.pdf`, `3. Location.pdf`, `4. Floor Plan.pdf`). List the folder with `parentId = '<folderId>'`.
5. **Confirm sharing** on both the folder and the PNG with `get_file_permissions` — you need `{"role":"reader","type":"anyone"}` or visitors can't open them.
6. **Build the card** by copying an existing `[data-card]` `<article>` and swapping neighborhood, cash flow, DSCR, completion. The CTA must be **"View Full Package →"** with `data-conversion="package_view"` → `https://drive.google.com/drive/folders/<folderId>?usp=sharing`. Never leave it as a contact.html/`book_call` fallback — `package_view` is what feeds the Meta retargeting audience.
7. **Counts need no edits** — Available / headline auto-derive from the cards.

**Card naming (owner-set, Aug 2026):** every Available card is titled **`<Neighbourhood> <N>-Plex`** — "Mill Woods 8-Plex", "Inglewood 9-Plex", "West Jasper 8-Plex". Always include the unit count, even when nothing else shares that neighbourhood: the old rule of adding it only to disambiguate drifted the moment a second Inglewood and a second West Jasper landed. **Do not put the word "Package" in the title** — the CTA underneath already says "View Full Package". The subtitle keeps `<Neighbourhood> · Edmonton` even though that repeats the neighbourhood; the owner is fine with it. `alt` text mirrors the title. **The neighbourhood is "West Jasper", not "West Jasper Place"** — the hotlist NEIGHBORHOOD cell says WEST JASPER PLACE but the owner's name for it is West Jasper. Sold Conditional and Previously Sold cards keep the inverse layout (unit count as the headline, neighbourhood beneath) — that is deliberate, they are compact scan-a-list cards, not sales units.

**Image hosting (updated Aug 2026 — the old "cannot localize" note was wrong):** this container's network policy **blocks `drive.google.com` and `lh3.googleusercontent.com`** (403 on CONNECT), so an `<img>` pointing at Drive will not render in a headless check. **But the Drive CONNECTOR can fetch the bytes** — `download_file_content` returns the PNG base64-encoded (it routes through the MCP server, not the container network). So elevations CAN be localized: download, `base64.b64decode`, write to `images/inv/<neighborhood>-<n>plex.png`, and point the card at the local path. Prefer this — it renders in headless verification and survives any Drive sharing change.

**Card frame is 16/10 with `object-fit:cover`. Ratio alone does NOT tell you whether a crop hurts** — it tells you how much gets trimmed; whether that matters depends on how much margin the building has in the source. Measured so far: Sherbrooke 1.658, Britannia 1.651, Mill Woods 1.635, Eastwood 1.664 (trim a sliver, all fine), Inglewood 9-Plex 1.263 (trims 21% of the height and still looks right, because the render has generous sky and lawn), West Jasper original 1.125 (trimmed 30% and took the roof and the entry steps, because the building filled the frame). **Verify by rendering the card, never by inferring from the ratio** — a 1.13 figure for the Inglewood 9-Plex was asserted from the West Jasper case without measuring and was wrong on both the number and the conclusion. When a crop genuinely does cut the building, **the fix the owner wants is a 16/10 re-render — ask for one** (~1600x1000; the second West Jasper came back at 1586x992 = 1.599 and drops straight in). Padding a near-square image onto a 16/10 canvas over a blurred copy of itself does avoid the crop, but the owner saw the soft edges immediately and did not like them — treat it as a stopgap only, and say so when you use it. Never crop the building to force 16/10, and never change the card frame (it would break the grid). If localizing is not possible, reference Drive directly — `https://lh3.googleusercontent.com/d/<FILE_ID>=w1600` — and always include the graceful fallback (`onerror` hides the `<img>` + its "Artist's rendering" tag so the card degrades to the placeholder panel rather than showing a broken image). Tell the owner to eyeball it live, and offer to localize to `images/inv/<neighborhood>-<n>plex.png` when they can supply the file. **Never** reuse another property's rendering to fill the gap.

**Git gotcha:** do **not** run `git checkout -B claude/... main` to sync the dev branch after committing on it — that resets the branch and orphans the commit, and the follow-up `git push origin main` reports "Everything up-to-date" while nothing shipped. Commit on `main` (or merge into it), push `main`, then `git branch -f claude/... main` + `git push -f`. Always verify with `git log --oneline main -1` and a successful `pages build and deployment` run before telling the owner it's live.

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

## Message Templates

Owner-approved client message templates live in **`docs/message-templates.md`**. When the owner says **"give me the allocation request form for {NAME}"**, return the Allocation Request template from that file verbatim with `{NAME}` swapped (change property/form link only if specified). Do not reword without owner sign-off — the copy is compliance-checked.
