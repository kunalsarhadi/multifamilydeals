#!/usr/bin/env python3
"""Generate the static <main> for build-progress.html.

The design handoff is a React prototype (`Build Progress.dc.html`) that computes
everything at runtime from three arrays. This script reproduces that computed
model exactly and emits static HTML, because every other page on this site is
readable with JavaScript off -- a JS-rendered page would be an empty shell to
crawlers. Behaviour that genuinely needs JS (click-to-play clips, rail arrows,
plate re-measure) stays in the page's script block.

Fidelity notes, all of which the prototype is explicit about:
  * lead + secondary plates are object-fit:contain and carry the media's OWN
    aspect ratio -- never cover, never a preset bucket. Rail and timeline
    thumbnails DO use cover in a uniform 4/3 plate.
  * a project's `video` (a property separate from `media`) fills the second
    column; `secondary` is only used when there is no video. Missing this drops
    3 of the 12 clips.
  * `stageNow` is the max month across `media` only -- the video's month does
    not count towards it.
"""
import json, html, re, os

ROOT = '/home/user/multifamilydeals'
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, 'build-progress-data.json')))
P, STAGES, TIMELINE, ORDER = D['P'], D['STAGES'], D['TIMELINE'], D['ORDER']


def e(s):
    return html.escape(s or '', quote=True)


def path(f):
    """Bundle paths -> repo paths (images/ was namespaced to avoid a collision)."""
    return re.sub(r'^images/', 'images/build/', f) if f.startswith('images/') else f


def is_clip(f):
    return bool(re.search(r'\.(mp4|webm|mov)$', f or '', re.I))


def poster(f):
    return re.sub(r'\.(mp4|webm|mov)$', '-poster.jpg', f, flags=re.I)


def exists(rel):
    return bool(rel) and os.path.exists(os.path.join(ROOT, rel))


def ratio(rel, fallback='3 / 2'):
    """The plate's own aspect ratio, measured from the real file so nothing
    reflows on load. Only clamped below 0.5, per the handoff."""
    try:
        from PIL import Image
        with Image.open(os.path.join(ROOT, rel)) as im:
            w, h = im.size
        return '1 / 2' if w / h < 0.5 else f'{w} / {h}'
    except Exception:
        return fallback


# ---------------------------------------------------------------- media item
def item(m, project_name):
    f = m[3] or ''
    clip = is_clip(f)
    mo = m[4] if len(m) > 4 else None
    known = isinstance(mo, int)
    return {
        'stage': m[0], 'date': m[1], 'caption': m[2], 'src': path(f), 'clip': clip,
        'monthShort': f'Month {mo}' if known else e(m[1]),
        'monthLong': f'Month {mo} &middot; {e(STAGES[mo])}' if known else e(m[1]),
        'dateNote': (('Filmed ' if clip else 'Photographed ') + m[1]) if known else '',
        'alt': f'{project_name} — {m[0]}, {m[1]}',
        'month': mo if known else None,
        'tag': 'Clip &middot; unedited' if clip else 'Photograph &middot; unretouched',
    }


# --------------------------------------------------------------- plate parts
def plate_photo(it, fit, cls=''):
    if not exists(it['src']):
        return ('<div class="bp-plate bp-plate-43' + cls + '">'
                '<span class="bp-empty">No photo yet</span></div>')
    # A 4:3 thumbnail keeps the class's ratio; only free-standing plates take
    # the media's own measured ratio.
    ar = '' if 'bp-plate-43' in cls else f' style="aspect-ratio:{ratio(it["src"])};"'
    return (f'<div class="bp-plate{cls}" data-bp-plate{ar}>'
            f'<img class="bp-media bp-{fit}" src="{e(it["src"])}" alt="{e(it["alt"])}" /></div>')


def plate_clip(it, fit, cls='', round_cue=False):
    """Poster + click-to-play. The clip lands on data-bp-src so the ~93 MB video
    library never loads up front; the plate is sized from the poster frame."""
    post = path(poster(it['src']))
    ar = ('' if 'bp-plate-43' in cls
          else f' style="aspect-ratio:{ratio(post) if exists(post) else "3 / 2"};"')
    cue = ('<span class="bp-cue-round" aria-hidden="true">&#9654;</span>' if round_cue else
           '<span class="bp-cue-pill"><span aria-hidden="true">&#9654;</span>Play clip</span>')
    return (f'<div class="bp-plate{cls}" data-bp-plate{ar}>'
            f'<video class="bp-media bp-{fit}" preload="none" playsinline muted loop '
            f'poster="{e(post)}" data-bp-src="{e(it["src"])}"></video>'
            f'<button type="button" class="bp-cue" data-bp-cue '
            f'aria-label="Play clip: {e(it["stage"])}">{cue}</button></div>')


def mount(inner, tag=None):
    """The espresso mount every plate sits in."""
    t = f'<span class="bp-tag">{tag}</span>' if tag else ''
    return f'<div class="bp-mount">{inner}{t}</div>'


def figure(it, cls, style=''):
    inner = plate_clip(it, 'contain') if it['clip'] else plate_photo(it, 'contain')
    return f'''<figure class="{cls}"{style}>
            {mount(inner, it['tag'])}
            <figcaption class="bp-figcap"><span class="bp-stage">{e(it['stage'])}</span><span class="bp-month">{it['monthLong']}</span></figcaption>
            <p class="bp-cap">{e(it['caption'])}</p>
            <div class="bp-date">{e(it['dateNote'])}</div>
          </figure>'''


# ------------------------------------------------------------------ projects
rank = {pid: i for i, pid in enumerate(ORDER)}
cards = []
for p in sorted(P, key=lambda x: rank.get(x['id'], len(ORDER))):
    items = [item(m, p['name']) for m in p['media']]
    vid = p.get('video')
    secondary = None if vid else (items[1] if len(items) > 1 else None)
    rail = items[2:] if secondary else items[1:]
    dates = [i['date'] for i in items]
    one_visit = all(d == dates[0] for d in dates)
    rail_title = (f"{p.get('railTitle') or 'Dated sequence'} · {dates[0]}"
                  if one_visit else 'Earlier stages')
    # The prototype only pluralises the one-visit branch; pluralise both.
    s = '' if len(rail) == 1 else 's'
    rail_count = (f'{len(rail)} more photograph{s} from this visit' if one_visit
                  else f'{len(rail)} earlier photograph{s} · oldest at the right')
    months = [i['month'] for i in items if i['month'] is not None]
    stage_label = f'Month {max(months)} of 8 &middot; {e(STAGES[max(months)])}' if months else ''
    lead_span = 'auto' if (vid or secondary) else '1 / -1'

    # second column: the project's clip if it has one, otherwise its second photo
    if vid:
        vm = vid.get('month')
        vmonth = (f'Month {vm} &middot; {e(STAGES[vm])}' if isinstance(vm, int) else e(vid['date']))
        vit = {'src': path(vid['file']), 'stage': vid['label'], 'clip': True}
        side = f'''<figure class="bp-fig bp-side">
            {mount(plate_clip(vit, 'contain'), 'Clip &middot; unedited')}
            <figcaption class="bp-figcap"><span class="bp-stage">{e(vid['label'])}</span><span class="bp-month">{vmonth}</span></figcaption>
            <p class="bp-cap bp-cap-mute">Muted, no sound track &mdash; filmed on site.</p>
            <div class="bp-date">Filmed {e(vid['date'])}</div>
          </figure>'''
    elif secondary:
        side = figure(secondary, 'bp-fig bp-side')
    else:
        side = ''

    railhtml = ''
    if rail:
        thumbs = '\n'.join(f'''              <li class="bp-thumb">
                <div class="bp-tick"><span></span></div>
                {mount(plate_clip(m, 'cover', ' bp-plate-43', round_cue=True) if m['clip'] else plate_photo(m, 'cover', ' bp-plate-43'))}
                <div class="bp-t-month">{m['monthShort']}</div>
                <div class="bp-t-stage">{e(m['stage'])}</div>
                <div class="bp-t-cap">{e(m['caption'])}</div>
                <div class="bp-t-date">{e(m['dateNote'])}</div>
              </li>''' for m in rail)
        railhtml = f'''
        <div class="bp-railwrap">
          <div class="bp-railhead">
            <div class="bp-railtitles"><span class="bp-railtitle">{e(rail_title)}</span><span class="bp-railcount">{e(rail_count)}</span></div>
            <div class="bp-arrows">
              <button type="button" class="bp-arrow" data-bp-prev aria-label="Earlier photos">&#8249;</button>
              <button type="button" class="bp-arrow" data-bp-next aria-label="Later photos">&#8250;</button>
            </div>
          </div>
          <ul class="bp-rail">
{thumbs}
          </ul>
          <div class="bp-swipe"><span class="rule"></span>Swipe for the full sequence</div>
        </div>'''

    cards.append(f'''      <article class="bp-card" id="bp-{e(p['id'])}">
        <div class="bp-projhead">
          <div class="bp-projmeta">
            <div class="bp-projtags"><span class="bp-units">{e(p['units'])}</span><span class="bp-place">{e(p['place'])}</span></div>
            <h3 class="bp-name">{e(p['name'])}</h3>
            <p class="bp-note">{e(p.get('note', ''))}</p>
          </div>
          <div class="bp-statuswrap">
            <div class="bp-status"><span class="bp-dot" aria-hidden="true"></span><span>{e(p['status'])}</span></div>
            {f'<div class="bp-marker">{stage_label}</div>' if stage_label else ''}
          </div>
        </div>
        <div class="bp-lead-grid">
          {figure(items[0], 'bp-fig bp-lead', f' style="grid-column:{lead_span};"')}
          {side}
        </div>{railhtml}
      </article>''')

# --------------------------------------------------------------------- stats
photo_count = sum(1 for p in P for m in p['media'] if m[3] and not is_clip(m[3]))
clip_count = (sum(1 for p in P for m in p['media'] if is_clip(m[3]))
              + sum(1 for p in P if p.get('video')))

# ------------------------------------------------------------------ timeline
stops = []
for month, blurb, src, credit in TIMELINE:
    s = path(src)
    shot = (f'<img class="bp-media bp-cover" src="{e(s)}" alt="{e(STAGES[month])} &mdash; {e(credit)}" />'
            if exists(s) else '<span class="bp-empty">No photo yet</span>')
    cr = ('Photographed on site' if credit == 'Site clearing'
          else f'Photographed at {credit}') if credit else 'Not yet photographed'
    stops.append(f'''          <li class="bp-stop">
            <div class="bp-tick"><span></span></div>
            <div class="bp-stop-m">Month {month}</div>
            <div class="bp-stop-s">{e(STAGES[month])}</div>
            <div class="bp-mount"><div class="bp-plate bp-plate-43">{shot}</div></div>
            <div class="bp-stop-b">{e(blurb)}</div>
            <div class="bp-stop-c">{e(cr)}</div>
          </li>''')

MAIN = f'''<main id="main-content">

  <!-- HERO -->
  <section class="bp-hero">
    <div class="bp-grid-bg" aria-hidden="true"></div>
    <div class="bp-wrap bp-hero-in">
      <div class="bp-eyebrow"><span class="rule"></span>Build Progress</div>
      <h1 class="bp-h1">The renderings turn into<br /><span class="bp-em">framing, then keys.</span></h1>
      <p class="bp-lede">Everything you see on the inventory page is an artist&rsquo;s rendering, because the buildings are sold before they are finished. This page is the other half of that: photographs I take on site, dated, from projects at every stage &mdash; demolition through handover. Nothing here is a rendering.</p>
      <p class="bp-lede-sm">I add photos after each site visit. If you want to see a specific stage that isn&rsquo;t posted yet, ask me and I&rsquo;ll shoot it.</p>
    </div>
  </section>

  <!-- STATS -->
  <section class="bp-statband">
    <div class="bp-wrap">
      <div class="bp-stats">
        <div><div class="bp-statv">{len(P)}</div><div class="bp-statl">Projects under construction</div></div>
        <div><div class="bp-statv">{photo_count}</div><div class="bp-statl">Site photographs posted</div></div>
        <div><div class="bp-statv">{clip_count}</div><div class="bp-statl">Site clips posted</div></div>
        <div><div class="bp-statv bp-statv-brass">Aug 2026</div><div class="bp-statl">Most recent site visit</div></div>
      </div>
    </div>
  </section>

  <!-- TIMELINE -->
  <section id="timeline" class="bp-tlband">
    <div class="bp-wrap">
      <div class="bp-tlhead">
        <div class="bp-tlhead-t">
          <div class="bp-eyebrow"><span class="rule"></span>The eight months</div>
          <h2 class="bp-h2">From firm deal to keys, one stage at a time.</h2>
          <p class="bp-body">Every project runs the same arc. No single site below has been photographed at all nine stages, so each stop here is illustrated from whichever building was at that point when I visited.</p>
        </div>
        <div class="bp-swipe"><span class="rule"></span>Swipe the timeline</div>
      </div>
      <ol class="bp-rail bp-timeline">
{chr(10).join(stops)}
      </ol>
      <p class="bp-fine">Months are counted from a firm deal. Construction schedules move with weather, trades and inspection dates &mdash; this is the sequence, not a completion commitment.</p>
    </div>
  </section>

  <!-- UNDER CONSTRUCTION -->
  <section id="under-construction" class="bp-ucband">
    <div class="bp-wrap">
      <div class="bp-uchead">
        <div class="bp-eyebrow"><span class="rule"></span>Under construction</div>
        <h2 class="bp-h2">The sites I am on right now.</h2>
      </div>
{chr(10).join(cards)}
    </div>
  </section>

  <!-- PRIVATE NETWORK — the site-wide WhatsApp bar (not in the prototype) -->
  <section style="background:#EFE9DB;border-top:1px solid #E4DBCB;border-bottom:1px solid #E4DBCB;padding:clamp(30px,4vw,40px) clamp(18px,4vw,44px);">
    <div style="max-width:1240px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;">
      <div style="display:flex;align-items:center;gap:14px;">
        <span style="width:9px;height:9px;border-radius:50%;background:#2AAF72;animation:pulseDot 2s ease-in-out infinite;flex-shrink:0;"></span>
        <div style="font-size:.9rem;color:#4A443B;line-height:1.5;"><strong style="color:#1C1813;font-weight:600;">Private Investor Network</strong> &mdash; new listings reach our WhatsApp group before they appear anywhere else.</div>
      </div>
      <a href="https://chat.whatsapp.com/BYNf65k8iSf3fNOIrkZUvZ" target="_blank" rel="noopener" data-conversion="whatsapp_click" style="background:transparent;border:1px solid var(--accent);color:var(--accent);padding:11px 24px;font-size:.7rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;white-space:nowrap;border-radius:2px;transition:background .2s,color .2s;">Join the Network</a>
    </div>
  </section>

  <!-- CTA -->
  <section id="visit" class="bp-cta">
    <div class="bp-wrap bp-cta-grid">
      <div>
        <div class="bp-eyebrow bp-eyebrow-d"><span class="rule"></span>See it yourself</div>
        <h2 class="bp-h2 bp-h2-d">Photos are the second-best proof.</h2>
        <p class="bp-cta-p">The best one is standing on the slab. I meet out-of-town buyers at the site and walk the whole lot &mdash; and if you can&rsquo;t fly in, I&rsquo;ll do it on a live video call at whatever hour works in your time zone, then send you the raw clips afterward.</p>
      </div>
      <div class="bp-cta-btns">
        <a href="contact.html" data-conversion="book_call" class="bp-btn">Book a Discovery Call</a>
        <a href="tel:+14162007010" data-conversion="phone_click" class="bp-btn-ghost">Request a Site Tour &middot; 416 200 7010</a>
        <p class="bp-fine bp-fine-d">All photographs on this page were taken on site on the dates shown. Renderings appear only where labelled &ldquo;Artist&rsquo;s rendering&rdquo;. Construction schedules move; stage dates describe what was photographed, not a completion commitment.</p>
      </div>
    </div>
  </section>

</main>'''

OUT = '/tmp/claude-0/-home-user/50c0f72d-33be-5ad3-b287-3516cd3ff11d/scratchpad'
open(os.path.join(OUT, 'bp_main.html'), 'w', encoding='utf-8').write(MAIN)

missing = [path(m[3]) for p in P for m in p['media'] if is_clip(m[3]) and not exists(path(m[3]))]
missing += [path(p['video']['file']) for p in P if p.get('video')
            and not exists(path(p['video']['file']))]
print(f'projects {len(P)} | photos {photo_count} | clips {clip_count}')
print(f'cards {len(cards)} | timeline stops {len(stops)} | main {len(MAIN)} chars')
print(f'clip files still missing from the repo: {len(missing)}')
for m in missing:
    print('  -', m)
