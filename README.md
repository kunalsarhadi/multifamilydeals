# Multi Family Deals — Website

**Live site:** https://multi-family-deals.ca

Edmonton-based multi-family real estate investment firm. Helps out-of-province investors acquire purpose-built 6–20 plex properties using CMHC MLI Select financing (5% down, 50-year amortization).

## Stack
- Plain HTML/CSS/JS — no build framework
- Hosted on GitHub Pages (CNAME → multi-family-deals.ca)
- 20 pages: 12 root-level + 8 blog articles

## PDF Guide

`assets/CMHC-MLI-Select-Investor-Guide.pdf` is a static PDF snapshot of `guide.html`.

**To regenerate after updating guide.html:**

```bash
cd /home/user/multifamilydeals
node generate-pdf.js
git add assets/CMHC-MLI-Select-Investor-Guide.pdf
git commit -m "regen: update investor guide PDF"
git push origin main
```

Requires Node.js and the `puppeteer` dev dependency (`npm install` to restore if needed).

## Version history
See `VERSION.md` for snapshot log.
