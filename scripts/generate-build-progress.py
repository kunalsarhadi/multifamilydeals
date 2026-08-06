#!/usr/bin/env python3
"""Generate the static <main> for build-progress.html from the handoff data.

Deliberately renders to static HTML rather than client-side building the page
from the arrays. Every other page on this site is 98-100% readable with
JavaScript disabled, which is what makes it crawlable by AI systems; a
JS-rendered page would show an empty shell. Behaviour (plate sizing, video
click-to-play, rail scrolling) stays in JS -- only content is static.
"""
import json, html, re, os

D = json.load(open('/tmp/claude-0/-home-user/50c0f72d-33be-5ad3-b287-3516cd3ff11d/scratchpad/bp-data.json'))
P, STAGES, TIMELINE, ORDER = D['P'], D['STAGES'], D['TIMELINE'], D['ORDER']
ROOT = '/home/user/multifamilydeals'

def e(s): return html.escape(s or '', quote=True)
def img_path(f):  # bundle paths -> repo paths (images/ was namespaced to avoid a collision)
    return re.sub(r'^images/', 'images/build/', f) if f.startswith('images/') else f
def is_clip(f): return bool(re.search(r'\.(mp4|webm|mov)$', f or '', re.I))
def poster_for(f): return re.sub(r'\.(mp4|webm|mov)$', '-poster.jpg', f, flags=re.I)

def dims(rel):
    """Real pixel dimensions so each plate can carry its own aspect-ratio in the
    HTML. Without this the browser reflows once JS measures the image."""
    p = os.path.join(ROOT, rel)
    try:
        from PIL import Image
        with Image.open(p) as im: return im.size
    except Exception:
        return None

def ratio_style(rel):
    wh = dims(rel)
    if not wh: return ''
    w, h = wh
    r = max(w / h, 0.5)          # clamp only below 0.5, per the handoff
    return f'aspect-ratio:{r:.4f};'

def month_long(m):
    return f'Month {m[4]} &middot; {e(STAGES[m[4]])}' if isinstance(m[4], int) else e(m[1])
def month_short(m):
    return f'Month {m[4]}' if isinstance(m[4], int) else e(m[1])
def date_note(m):
    return ('Filmed ' if is_clip(m[3]) else 'Photographed ') + e(m[1])

def plate(m, klass, sizes_attr=''):
    """One photo or clip plate. Photos are eager (the handoff is explicit that
    lazy-loading broke rendering). Clips are poster + click-to-play, src set on
    first click so ~93 MB of video never loads up front."""
    f = m[3] or ''
    cap = f'''
        <figcaption class="bp-cap">
          <span class="bp-chip">{month_long(m)}</span>
          <span class="bp-stage">{e(m[0])}</span>
          <span class="bp-note">{e(m[2])}</span>
          <span class="bp-date">{date_note(m)}</span>
        </figcaption>'''
    if is_clip(f):
        src, post = img_path(f), img_path(poster_for(f))
        return f'''<figure class="{klass}">
        <div class="bp-plate" data-bp-plate style="{ratio_style(post)}">
          <video class="bp-media" preload="none" playsinline muted loop poster="{e(post)}" data-bp-src="{e(src)}"></video>
          <button type="button" class="bp-play" aria-label="Play clip: {e(m[0])}"><span aria-hidden="true">&#9654;</span> Play clip</button>
          <span class="bp-tag">Clip &middot; unedited</span>
        </div>{cap}
      </figure>'''
    src = img_path(f)
    return f'''<figure class="{klass}">
        <div class="bp-plate" data-bp-plate style="{ratio_style(src)}">
          <img class="bp-media" src="{e(src)}" alt="{e(m[0])} &ndash; {e(m[2])}" {sizes_attr} />
        </div>{cap}
      </figure>'''

# ---------- stats, computed from the data ----------
all_media = [m for p in P for m in p['media']]
n_photos = sum(1 for m in all_media if not is_clip(m[3]))
n_clips  = sum(1 for m in all_media if is_clip(m[3]))
MONTHS = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,
          'august':8,'september':9,'october':10,'november':11,'december':12,
          'winter':1,'spring':4,'summer':7,'fall':10,'autumn':10}
def date_key(d):
    y = re.search(r'(20\d\d)', d or '')
    mo = next((v for k, v in MONTHS.items() if k in (d or '').lower()), 0)
    return (int(y.group(1)) if y else 0, mo)
latest = max((m[1] for m in all_media), key=date_key)

# ---------- timeline ----------
tl = []
for month, blurb, src, credit in TIMELINE:
    s = img_path(src)
    exists = os.path.exists(os.path.join(ROOT, s))
    media = (f'<img class="bp-media" src="{e(s)}" alt="{e(STAGES[month])}" />' if exists
             else '<span class="bp-empty">No photo yet</span>')
    tl.append(f'''      <li class="bp-stop">
        <div class="bp-stop-head"><span class="bp-stop-m">Month {month}</span><span class="bp-stop-s">{e(STAGES[month])}</span></div>
        <div class="bp-plate bp-stop-plate" data-bp-plate style="{ratio_style(s) if exists else 'aspect-ratio:4/3;'}">{media}</div>
        <p class="bp-stop-b">{e(blurb)}</p>
        <p class="bp-stop-c">{e(credit)}</p>
      </li>''')

# ---------- project cards ----------
rank = {pid: i for i, pid in enumerate(ORDER)}
cards = []
for p in sorted(P, key=lambda x: rank.get(x['id'], len(ORDER))):
    med = p['media']
    months = [m[4] for m in med if isinstance(m[4], int)]
    stage_now = max(months) if months else None
    marker = f'Month {stage_now} &middot; {e(STAGES[stage_now])}' if stage_now is not None else ''
    lead, side, rest = med[0], (med[1] if len(med) > 1 else None), med[2:]
    grid = (plate(lead, 'bp-lead') + ('\n      ' + plate(side, 'bp-side') if side else ''))
    rail = ''
    if len(med) >= 3:
        thumbs = '\n'.join(f'''          <li class="bp-thumb">
            <div class="bp-plate bp-thumb-plate" data-bp-plate style="{ratio_style(img_path(poster_for(m[3]) if is_clip(m[3]) else m[3]))}">
              {'<video class="bp-media" preload="none" playsinline muted loop poster="'+e(img_path(poster_for(m[3])))+'" data-bp-src="'+e(img_path(m[3]))+'"></video><button type="button" class="bp-play bp-play-sm" aria-label="Play clip"><span aria-hidden="true">&#9654;</span></button>' if is_clip(m[3]) else '<img class="bp-media" src="'+e(img_path(m[3]))+'" alt="'+e(m[0])+'" />'}
            </div>
            <span class="bp-chip bp-chip-sm">{month_short(m)}</span>
            <span class="bp-stage bp-stage-sm">{e(m[0])}</span>
            <span class="bp-date">{date_note(m)}</span>
          </li>''' for m in rest)
        rail = f'''
      <div class="bp-railwrap">
        <div class="bp-railhead">
          <span class="bp-railtitle">{e(p.get('railTitle') or 'Earlier stages')}</span>
          <div class="bp-arrows">
            <button type="button" class="bp-arrow" data-bp-prev aria-label="Previous">&#8592;</button>
            <button type="button" class="bp-arrow" data-bp-next aria-label="Next">&#8594;</button>
          </div>
        </div>
        <ul class="bp-rail">
{thumbs}
        </ul>
        <p class="bp-swipe">Swipe for the full sequence</p>
      </div>'''
    cards.append(f'''    <article class="bp-card" id="bp-{e(p['id'])}">
      <header class="bp-projhead">
        <div>
          <span class="bp-units">{e(p['units'])}</span>
          <h3 class="bp-name">{e(p['name'])}</h3>
          <p class="bp-place">{e(p['place'])}</p>
        </div>
        <div class="bp-statuswrap">
          <span class="bp-status"><span class="bp-dot" aria-hidden="true"></span>{e(p['status'])}</span>
          {f'<span class="bp-marker">{marker}</span>' if marker else ''}
        </div>
      </header>
      <p class="bp-projnote">{e(p.get('note',''))}</p>
      <div class="bp-lead-grid{'' if side else ' bp-lead-solo'}">
      {grid}
      </div>{rail}
    </article>''')

MAIN = f'''<main id="main-content" style="background:#F5F1E8;">

  <!-- HERO -->
  <section class="bp-hero">
    <div class="bp-wrap">
      <div class="bp-eyebrow"><span class="rule"></span>Build Progress</div>
      <h1 class="bp-h1">The renderings turn into <span class="bp-em">framing, then keys.</span></h1>
      <p class="bp-lede">Everything you see on the inventory page is an artist's rendering, because the buildings are sold before they are finished. This page is the other half of that: photographs I take on site, dated, from projects at every stage &mdash; demolition through handover. Nothing here is a rendering.</p>
      <p class="bp-lede bp-lede-sm">I add photos after each site visit. If you want to see a specific stage that isn't posted yet, ask me and I'll shoot it.</p>
    </div>
  </section>

  <!-- STATS -->
  <div class="bp-wrap"><div class="bp-stats">
    <div><div class="bp-statv">{len(P)}</div><div class="bp-statl">Projects under construction</div></div>
    <div><div class="bp-statv">{n_photos}</div><div class="bp-statl">Site photographs posted</div></div>
    <div><div class="bp-statv">{n_clips}</div><div class="bp-statl">Site clips posted</div></div>
    <div><div class="bp-statv">{e(latest)}</div><div class="bp-statl">Most recent site visit</div></div>
  </div></div>

  <!-- TIMELINE -->
  <section class="bp-sec bp-sec-alt">
    <div class="bp-wrap">
      <div class="bp-eyebrow"><span class="rule"></span>The eight months</div>
      <h2 class="bp-h2">From firm deal to keys, <span class="bp-em">one stage at a time.</span></h2>
      <p class="bp-lede">Every project runs the same arc. No single site below has been photographed at all nine stages, so each stop here is illustrated from whichever building was at that point when I visited.</p>
      <p class="bp-swipe bp-swipe-tl">Swipe the timeline</p>
      <ol class="bp-timeline">
{chr(10).join(tl)}
      </ol>
      <p class="bp-fine">Months are counted from a firm deal. Construction schedules move with weather, trades and inspection dates &mdash; this is the sequence, not a completion commitment.</p>
    </div>
  </section>

  <!-- UNDER CONSTRUCTION -->
  <section class="bp-sec">
    <div class="bp-wrap">
      <div class="bp-eyebrow"><span class="rule"></span>Under construction</div>
      <h2 class="bp-h2">The sites I am <span class="bp-em">on right now.</span></h2>
    </div>
    <div class="bp-wrap bp-cards">
{chr(10).join(cards)}
    </div>
  </section>

  <!-- CTA -->
  <section class="bp-cta">
    <div class="bp-wrap bp-cta-in">
      <div class="bp-eyebrow bp-eyebrow-d"><span class="rule"></span>See it yourself</div>
      <h2 class="bp-h2 bp-h2-d">Photos are the <span class="bp-em-d">second-best proof.</span></h2>
      <p class="bp-cta-p">The best one is standing on the slab. I meet out-of-town buyers at the site and walk the whole lot &mdash; and if you can't fly in, I'll do it on a live video call at whatever hour works in your time zone, then send you the raw clips afterward.</p>
      <div class="bp-cta-btns">
        <a href="contact.html" data-conversion="book_call" data-magnetic class="bp-btn">Book a Discovery Call</a>
        <a href="tel:+14162007010" data-conversion="phone_click" class="bp-btn-ghost">Request a Site Tour &middot; 416 200 7010</a>
      </div>
      <p class="bp-fine bp-fine-d">All photographs on this page were taken on site on the dates shown. Renderings appear only where labelled "Artist's rendering". Construction schedules move; stage dates describe what was photographed, not a completion commitment.</p>
    </div>
  </section>

</main>'''

open('/tmp/claude-0/-home-user/50c0f72d-33be-5ad3-b287-3516cd3ff11d/scratchpad/bp_main.html', 'w', encoding='utf-8').write(MAIN)
print(f'projects {len(P)} | photos {n_photos} | clips {n_clips} | latest {latest}')
print(f'timeline stops {len(tl)} | cards {len(cards)} | main {len(MAIN)} chars')
