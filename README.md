# Multi Family Deals — Website

**Live site:** https://multi-family-deals.ca

Edmonton-based multi-family real estate investment firm. Helps out-of-province investors acquire purpose-built 6–20 plex properties using CMHC MLI Select financing (5% down, 50-year amortization).

## Stack
- Plain HTML/CSS/JS — no build framework
- Hosted on GitHub Pages (CNAME → multi-family-deals.ca)
- 20 pages: 12 root-level + 8 blog articles

## PDF Guide

The live investor guide is **`assets/CMHC-MLI-Select-Investor-Guide-v2.pdf`** — a
designed PDF supplied by the owner (Canva), **not** a generated snapshot of
`guide.html`. Do not overwrite it with `generate-pdf.js` output.

The filename is **versioned**. `guide.html` points at the `-vN` file in two
places: the `PDF_URL` constant and the manual fallback `<a href>` in the modal.

**To publish an updated guide:**

1. Add the new file as the next version — `assets/CMHC-MLI-Select-Investor-Guide-v3.pdf`.
2. Update **both** references in `guide.html` (`PDF_URL` and the fallback link `href`).
3. Leave the older `-vN` files in `assets/` so links already shared with investors
   keep resolving.
4. Commit and push to `main`.

Versioning the filename is what forces browsers and any CDN past a cached copy of
the previous guide. The unversioned `CMHC-MLI-Select-Investor-Guide.pdf` is
retained only for historical links.

**Download reliability:** the modal always renders a visible manual download link.
The automatic download (fired from the GHL form's `postMessage`) is best-effort
only — browsers can block a programmatic click that isn't a direct user gesture,
so the manual link is the guarantee. Don't remove it.

## Version history
See `VERSION.md` for snapshot log.
