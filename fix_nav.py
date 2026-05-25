#!/usr/bin/env python3
"""
Fix nav issues across all pages:
1. Fix blog/index.html breakpoint 1100px → 1200px
2. Add Calculator to Resources dropdown on all pages
3. Fix calculator.html nav-inner padding at wrong breakpoint
"""
import re, os

ROOT_FILES = [
    'about.html','buying-process.html','contact.html','faq.html',
    'guide.html','index.html','inglewood.html','inventory.html',
    'ontario-investors.html','reviews.html','why-alberta.html','calculator.html',
]
BLOG_FILES = [
    'blog/best-canadian-city-multifamily-investing.html',
    'blog/cmhc-mli-select-guide.html',
    'blog/edmonton-vs-toronto-multifamily.html',
    'blog/index.html',
    'blog/mli-select-vs-conventional.html',
    'blog/mli-select-worth-it.html',
    'blog/scale-50-doors.html',
]

# --- Fix 1: blog/index.html breakpoint 1100px → 1200px + add nav-inner padding ---
def fix_blog_index_breakpoint(html):
    # Fix the wrong 1100px breakpoint
    html = html.replace(
        '@media (max-width: 1100px) { .nav-links { display: none; } .nav-cta { display: none; } .hamburger { display: flex; } }',
        '@media (max-width: 1200px) { .nav-links { display: none; } .nav-cta { display: none; } .hamburger { display: flex; } .nav-inner { padding: 0 1.5rem; } }'
    )
    # Remove the duplicate nav-inner padding at 600px if it's in the wrong spot
    # It's currently: @media (max-width: 600px) { .page-hero { ... } .blog-section { ... } .nav-inner { padding: 0 1.5rem; } }
    html = re.sub(
        r'(@media \(max-width: 600px\) \{[^}]*?)\.nav-inner \{ padding: 0 1\.5rem; \}\s*',
        r'\1',
        html
    )
    return html

# --- Fix 2: calculator.html nav-inner padding at 520px → move into 1200px rule ---
def fix_calc_breakpoint(html):
    # Remove standalone nav-inner padding from 520px rule
    html = re.sub(
        r'(@media \(max-width: 520px\) \{)\s*\n\s*\.nav-inner \{ padding: 0 1\.5rem; \}\s*\n',
        r'\1\n',
        html
    )
    # Add it to the 1200px breakpoint (which currently has: .nav-links { display: none; } .nav-cta { display: none; } .hamburger { display: flex; })
    html = html.replace(
        '@media (max-width: 1200px) {\n      .nav-links { display: none; } .nav-cta { display: none; } .hamburger { display: flex; }',
        '@media (max-width: 1200px) {\n      .nav-links { display: none; } .nav-cta { display: none; } .hamburger { display: flex; } .nav-inner { padding: 0 1.5rem; }'
    )
    return html

# --- Fix 3: Add Calculator to Resources dropdown ---
# Root pages use calculator.html; blog pages use ../calculator.html
def add_calculator_to_nav(html, prefix):
    calc_href = f'{prefix}calculator.html'
    guide_href = f'{prefix}guide.html'

    # Add after Free Guide in dropdown (before closing </ul> of resources dropdown)
    old_guide_item = f'<li><a href="{guide_href}" role="menuitem"><span class="dropdown-link-title">Free Guide</span><span class="dropdown-link-desc">CMHC MLI Select PDF guide</span></a></li>'
    new_items = f'''{old_guide_item}
            <li><a href="{calc_href}" role="menuitem"><span class="dropdown-link-title">Calculator</span><span class="dropdown-link-desc">Pro-forma &amp; DSCR estimator</span></a></li>'''
    if old_guide_item in html and calc_href not in html:
        html = html.replace(old_guide_item, new_items)

    # Add to mobile nav after Free Guide link
    old_mobile_guide = f'<a href="{guide_href}">Free Guide</a>'
    new_mobile = f'''{old_mobile_guide}
    <a href="{calc_href}">Calculator</a>'''
    if old_mobile_guide in html and f'href="{calc_href}"' not in html:
        html = html.replace(old_mobile_guide, new_mobile)

    return html

# --- Also update active category map to include calculator ---
OLD_MAP = "      'resources': ['buying-process', 'faq', 'reviews', 'guide', 'blog']"
NEW_MAP = "      'resources': ['buying-process', 'faq', 'reviews', 'guide', 'blog', 'calculator']"

def process(filepath):
    is_blog = filepath.startswith('blog/')
    prefix = '../' if is_blog else ''

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html

    # Apply fixes
    if filepath == 'blog/index.html':
        html = fix_blog_index_breakpoint(html)

    if filepath == 'calculator.html':
        html = fix_calc_breakpoint(html)

    html = add_calculator_to_nav(html, prefix)

    # Update active category JS map
    if OLD_MAP in html:
        html = html.replace(OLD_MAP, NEW_MAP)

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  ✓ {filepath}')
    else:
        print(f'  ✗ {filepath} — no changes')

os.chdir('/home/user/multifamilydeals')
print('Fixing nav...')
for f in ROOT_FILES + BLOG_FILES:
    process(f)
print('Done.')
