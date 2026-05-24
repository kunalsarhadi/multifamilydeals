#!/usr/bin/env python3
"""Rebuild nav across all 15 HTML files to use 3-dropdown structure."""

import re, os

ROOT_FILES = [
    'about.html','buying-process.html','contact.html','faq.html',
    'guide.html','index.html','inglewood.html','inventory.html',
    'ontario-investors.html','reviews.html','why-alberta.html',
]
BLOG_FILES = [
    'blog/cmhc-mli-select-guide.html',
    'blog/edmonton-vs-toronto-multifamily.html',
    'blog/index.html',
    'blog/mli-select-vs-conventional.html',
    'blog/mli-select-worth-it.html',
    'blog/scale-50-doors.html',
]

# ---------------------------------------------------------------------------
# NAV CSS — replaces old .nav-links rule + adds dropdown styles
# ---------------------------------------------------------------------------
OLD_NAV_LINKS_CSS = re.compile(
    r'\.nav-links \{ display: flex;[^}]+\}',
    re.DOTALL
)
NEW_NAV_LINKS_CSS = """\
.nav-links { display: flex; gap: 0; list-style: none; }
    .has-dropdown { position: relative; }
    .nav-dropdown-btn { background: none; border: none; cursor: pointer; font-family: 'Josefin Sans', sans-serif; font-size: 0.7rem; font-weight: 500; letter-spacing: 0.04em; text-transform: uppercase; color: var(--text-muted); padding: 0.4rem 0.75rem; display: flex; align-items: center; gap: 0.3rem; transition: color 0.2s; white-space: nowrap; }
    .nav-dropdown-btn:hover { color: var(--gold); }
    .has-dropdown.active > .nav-dropdown-btn { color: var(--gold); }
    .nav-chevron { width: 0.65rem; height: 0.65rem; transition: transform 0.2s; flex-shrink: 0; }
    .has-dropdown.open .nav-chevron { transform: rotate(180deg); }
    .nav-dropdown-menu { display: none; position: absolute; top: calc(100% + 6px); left: 0; min-width: 230px; background: var(--navy-card); border: 1px solid var(--navy-border); border-top: 2px solid var(--gold); list-style: none; padding: 0.4rem 0; z-index: 100; box-shadow: 0 12px 40px rgba(0,0,0,0.5); }
    .has-dropdown.open .nav-dropdown-menu { display: block; }
    .nav-dropdown-menu li a { display: block; padding: 0.7rem 1.25rem; text-decoration: none; transition: background 0.15s; border-left: 2px solid transparent; }
    .nav-dropdown-menu li a:hover { background: var(--navy-alt); border-left-color: var(--gold); }
    .dropdown-link-title { display: block; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--text-primary); margin-bottom: 0.18rem; }
    .dropdown-link-desc { display: block; font-size: 0.7rem; font-weight: 300; color: var(--text-subtle); letter-spacing: 0.01em; text-transform: none; }
    .mobile-nav-category { font-size: 0.62rem; font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase; color: var(--gold-muted); padding: 1.2rem 0 0.35rem; pointer-events: none; margin-top: 0.25rem; }"""

# ---------------------------------------------------------------------------
# NAV HTML generators
# ---------------------------------------------------------------------------
def nav_html(p):
    """Return the <ul class="nav-links"> block. p = path prefix ('' or '../')"""
    blog = f'{p}blog/index.html'
    return f'''\
<ul class="nav-links">
        <li class="has-dropdown" data-category="why-edmonton">
          <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true">Why Edmonton <svg class="nav-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></button>
          <ul class="nav-dropdown-menu" role="menu">
            <li><a href="{p}about.html" role="menuitem"><span class="dropdown-link-title">The Strategy</span><span class="dropdown-link-desc">Investment approach &amp; team</span></a></li>
            <li><a href="{p}why-alberta.html" role="menuitem"><span class="dropdown-link-title">Why Alberta</span><span class="dropdown-link-desc">Market fundamentals &amp; data</span></a></li>
          </ul>
        </li>
        <li class="has-dropdown" data-category="properties">
          <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true">Properties <svg class="nav-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></button>
          <ul class="nav-dropdown-menu" role="menu">
            <li><a href="{p}inventory.html" role="menuitem"><span class="dropdown-link-title">Active Inventory</span><span class="dropdown-link-desc">Available 6–20 plex assets</span></a></li>
            <li><a href="{p}inglewood.html" role="menuitem"><span class="dropdown-link-title">Portfolio</span><span class="dropdown-link-desc">Completed Inglewood 9-plex</span></a></li>
          </ul>
        </li>
        <li class="has-dropdown" data-category="resources">
          <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true">Resources <svg class="nav-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></button>
          <ul class="nav-dropdown-menu" role="menu">
            <li><a href="{p}buying-process.html" role="menuitem"><span class="dropdown-link-title">Buying Process</span><span class="dropdown-link-desc">9-step acquisition roadmap</span></a></li>
            <li><a href="{p}faq.html" role="menuitem"><span class="dropdown-link-title">FAQ</span><span class="dropdown-link-desc">Common investor questions</span></a></li>
            <li><a href="{p}reviews.html" role="menuitem"><span class="dropdown-link-title">Reviews</span><span class="dropdown-link-desc">Client testimonials</span></a></li>
            <li><a href="{blog}" role="menuitem"><span class="dropdown-link-title">Blog</span><span class="dropdown-link-desc">Investor education articles</span></a></li>
            <li><a href="{p}guide.html" role="menuitem"><span class="dropdown-link-title">Free Guide</span><span class="dropdown-link-desc">CMHC MLI Select PDF guide</span></a></li>
          </ul>
        </li>
      </ul>'''

def mobile_nav_html(p, cta_class=''):
    """Return the mobile-nav div contents. p = path prefix."""
    blog = f'{p}blog/index.html'
    contact = f'{p}contact.html'
    extra = f' {cta_class}' if cta_class else ''
    return f'''\
<div class="mobile-nav" id="mobileNav">
    <div class="mobile-nav-category">Why Edmonton</div>
    <a href="{p}about.html">The Strategy</a>
    <a href="{p}why-alberta.html">Why Alberta</a>
    <div class="mobile-nav-category">Properties</div>
    <a href="{p}inventory.html">Active Inventory</a>
    <a href="{p}inglewood.html">Portfolio</a>
    <div class="mobile-nav-category">Resources</div>
    <a href="{p}buying-process.html">Buying Process</a>
    <a href="{p}faq.html">FAQ</a>
    <a href="{p}reviews.html">Reviews</a>
    <a href="{blog}">Blog</a>
    <a href="{p}guide.html">Free Guide</a>
    <a href="{contact}" data-conversion="book_call" class="mobile-nav-cta">Book Discovery Call</a>
  </div>'''

# ---------------------------------------------------------------------------
# DROPDOWN JS
# ---------------------------------------------------------------------------
DROPDOWN_JS = '''\

  // Dropdown navigation
  (function() {
    var dropdowns = document.querySelectorAll('.has-dropdown');
    dropdowns.forEach(function(dd) {
      var btn = dd.querySelector('.nav-dropdown-btn');
      btn.addEventListener('click', function(e) {
        e.stopPropagation();
        var isOpen = dd.classList.contains('open');
        dropdowns.forEach(function(d) { d.classList.remove('open'); d.querySelector('.nav-dropdown-btn').setAttribute('aria-expanded', 'false'); });
        if (!isOpen) { dd.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
      });
      dd.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') { dd.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.focus(); }
      });
    });
    document.addEventListener('click', function() {
      dropdowns.forEach(function(d) { d.classList.remove('open'); d.querySelector('.nav-dropdown-btn').setAttribute('aria-expanded', 'false'); });
    });
    // Active category highlight
    var path = window.location.pathname;
    var map = {
      'why-edmonton': ['about', 'why-alberta'],
      'properties': ['inventory', 'inglewood'],
      'resources': ['buying-process', 'faq', 'reviews', 'guide', 'blog']
    };
    for (var cat in map) {
      for (var i = 0; i < map[cat].length; i++) {
        if (path.indexOf(map[cat][i]) !== -1) {
          var el = document.querySelector('.has-dropdown[data-category="' + cat + '"]');
          if (el) el.classList.add('active');
          break;
        }
      }
    }
  })();'''

# ---------------------------------------------------------------------------
# Pattern matchers
# ---------------------------------------------------------------------------
NAV_LINKS_BLOCK = re.compile(
    r'<ul class="nav-links">.*?</ul>',
    re.DOTALL
)
MOBILE_NAV_BLOCK = re.compile(
    r'<div class="mobile-nav"[^>]*>.*?</div>(?=\s*\n\s*\n?\s*<section|\s*\n\s*\n?\s*<!--|\s*\n\s*<(?:section|article|main|header|nav|div class="(?:page|hero|article)))',
    re.DOTALL
)
MOBILE_NAV_BLOCK_ALT = re.compile(
    r'<div class="mobile-nav" id="mobileNav">.*?</div>',
    re.DOTALL
)

# ---------------------------------------------------------------------------
# Main processor
# ---------------------------------------------------------------------------
def process(filepath):
    is_blog = filepath.startswith('blog/')
    prefix = '../' if is_blog else ''

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # 1. Update nav-links CSS
    html = OLD_NAV_LINKS_CSS.sub(NEW_NAV_LINKS_CSS, html, count=1)

    # 2. Replace nav-links HTML
    new_nav = nav_html(prefix)
    html = NAV_LINKS_BLOCK.sub(new_nav, html, count=1)

    # 3. Replace mobile-nav HTML
    new_mobile = mobile_nav_html(prefix)
    # Try to match the mobile nav block
    m = MOBILE_NAV_BLOCK_ALT.search(html)
    if m:
        html = html[:m.start()] + new_mobile + html[m.end():]

    # 4. Add dropdown JS before </script> that contains hamburger code
    if 'hamburger' in html and 'Dropdown navigation' not in html:
        # Find the closing </script> of the hamburger block
        ham_idx = html.rfind('hamburger')
        if ham_idx != -1:
            script_end = html.find('</script>', ham_idx)
            if script_end != -1:
                html = html[:script_end] + DROPDOWN_JS + '\n' + html[script_end:]

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  ✓ {filepath}')
    else:
        print(f'  ✗ {filepath} — NO CHANGES (check manually)')

# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
print('Rebuilding nav...')
for f in ROOT_FILES + BLOG_FILES:
    process(f)
print('Done.')
