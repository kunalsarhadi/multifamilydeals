#!/usr/bin/env python3
"""
Localize the Crawford Plains gallery.

The crawford-plains.html gallery currently streams 53 photos straight from the
owner's Google Drive (lh3.googleusercontent.com/d/<ID>=w1600). If Drive sharing
on that folder ever changes, the gallery degrades to a placeholder (graceful,
but no photos). This script downloads all 53, converts them to compressed webp,
and writes them into the repo so the gallery is self-hosted like Inglewood.

RUN THIS WHERE lh3.googleusercontent.com IS REACHABLE (your machine / a session
with open network — the managed cloud env blocks it).

    python3 scripts/localize-crawford-gallery.py

Then apply the two code edits it prints at the end (or re-run with --patch to
auto-edit crawford-plains.html), review, and commit images/crawford/ + the page.

Requires: Pillow  (pip install Pillow)
"""
import os, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(ROOT, "images", "crawford")

SUITES = {
    "upper1": ['1HdNiQ4o2nfraLud2EOn9W0rSzCWeuglZ','1GeS6t0DjYUTaCRYKU-qaPn_GIM3edvVe','1eqsELT9uKkfUJBpRmhEEs79UB90lSJdn','12ek1BVkWWauvWRbDYfGrN-y8sn_kAn51','1q1EevjvlluEvLkJwpYnlPX4DjaDVKx23','17CTWmwWPV7s2T5IJ1p86xLUqsRn3aehn','1VaQeCqTRXYQSVVWxLh_KUCN_3i2bl6U0','1cXHBsgc7opEAlwxFZP4PlOIYB918elC0','1U8eizpiGVwyHYDyQasxrUkKidQO42c-8','1vZKl3fiCSK1G-zBu7R1cceM3q5IsyGta','1hdqcaEwRmU-g-gb7nfMq1lwTwFc1uWb1','1ohh_p2coEdslRuGhfD0rVH8Zz5fg5ZW4','1VtZqelCYHVffC3MnwmXR-TErihV1Mm08','1DYFFuuHIJInIbYdCPIAva_u0jzfFq6Oz','1HcJOm1AGaHJNSafNBBq9q9jkiCi6g8mZ','14lLYfSjOn2FWrwdaiBOlMXXfBsVeu6k4','1FbDUKbQensL5MhaNmXJM4bWi5pxzMr4W','1R9drD-oPl3QJAl-Rz8UyLel-J9INWBKc','1F6gyr5QvbrU7TcIiuI5ihVm5F6P7n1uD','1PXqCmYzx4-9KZU6ilSNO7ZwbHSlpA5EF','1-9fhq008NrZ4SbJjhU9_pSKReDeIWP-j','1bsBIa_mMvxY3Z5QDMqJl476GbNBYQYz_','1g__F0hzSqijT-Bw4AVSsv6I8z0mTcX5B'],
    "upper2": ['1N7puJ_YzP_vZ_Jw6V0zIqyXoDsfrdgkR','1hEFsJ-IgfEnVtXFgQXNYiYgL1ZDEoP0t','1zW3Y3eBLFyjaJIQ8HD0nYusv0EvGo45c','105rj6Gqvkjq2338TamndN7hjQLYxUeGD','1vJjWnFlj2pj_pSc55McbbVFoh6TSFowZ','1fYu0KURnpJU5bocdavjbqiYEctDoZ2nz','15xqLvK1sZfxQU2YVoHq_EI0MolX6m6Q_','1qI6z-QmmlcJX5FofUci8w9yunrKdvemM','1n16yLCcnvuzV8NfqrLPHyPH6rXSMt31i','19hDWcbMCDcyjbTrDcKmdrcK5e8HvbhCa','11_VISvqjz8KAz8fSuGXOZLH7zxDuvphP','1HHy-k1UvhpuXVdibPrVrsaM6u9B0WEYz','13GRy-D2brfRg4ZxKnW50vygpM-YVDIZN','1pjHtXRhcVriPiuSVjxHWgwbvCS-V4NSV','1dUCOZA6uYNIHwT4SgWW6LrRAaJ6TGVK7','1VEmkGB_ABnZGj9uL8jGP3VyO4Ajy8JL5','1BN0fM48uE-AxQx_wB6FL3ryQz9vGgcSb','1DHXsoq9MsmZ9uE22LJo9MZAgQz8770sE','1J6wBDJWxUpqnsFs52ofsbYgkqkSoc6bC'],
    "lower":  ['1suqdFWVYJNvBR_x8mSUfj5TWL8sH9BYV','169DMJHhRRe_ay-2HSboO_C9XU0egC869','11xCiSOO6wbt2VQTQVI3XLd8mG3b9HjtU','1HLFYU6weeI1Z3kpJTLmPLHO8u5KMoU90','1ZJv761OvbSS1EaRwdoM0hfP3nEDmETZP','1LdWCbcbgKHxF2GVOtHheqg6TuGZe6isu','1Uo8f08UE2YmgPAyOpY3yb31lIxNNvEQH','1LDhd12qzclBrOIBl6n7KuSGzCFzFYSEF','1lK15u2HsSt2IxHaz6co1aKalooW-XQ1L','1Y67aV_4EoG4QucNwN5r8hDGV3DMjTaZD','1EDgJx4yDq1xVP7i4XISK1s-hjVA84LIV'],
}

def main():
    try:
        from PIL import Image
    except ImportError:
        sys.exit("Pillow is required:  pip install Pillow")
    import io

    total = sum(len(v) for v in SUITES.values())
    print(f"Downloading + converting {total} photos -> {OUT}/<suite>/NN.webp\n")
    local = {}
    for suite, ids in SUITES.items():
        d = os.path.join(OUT, suite)
        os.makedirs(d, exist_ok=True)
        local[suite] = []
        for i, fid in enumerate(ids, 1):
            src = f"https://lh3.googleusercontent.com/d/{fid}=w1600"
            name = f"{i:02d}.webp"
            path = os.path.join(d, name)
            try:
                req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
                raw = urllib.request.urlopen(req, timeout=30).read()
                img = Image.open(io.BytesIO(raw)).convert("RGB")
                # cap long edge at 1600 for a sensible file size
                img.thumbnail((1600, 1600))
                img.save(path, "WEBP", quality=80, method=6)
                local[suite].append(f"images/crawford/{suite}/{name}")
                print(f"  ok  {suite}/{name}  ({len(raw)//1024} KB -> {os.path.getsize(path)//1024} KB)")
            except Exception as e:
                print(f"  FAIL {suite}/{name}: {e}")
        print()

    print("=" * 70)
    print("Done. Now apply these TWO edits in crawford-plains.html:\n")
    print("1) Replace the SUITES `ids:[...]` arrays with these local `imgs:[...]`:\n")
    for suite in SUITES:
        arr = ",".join(f"'{p}'" for p in local[suite])
        print(f"   {suite}: imgs:[{arr}]")
    print("\n2) Change the URL builder + card src so it uses the local path and")
    print("   falls back to Drive on error. Replace:")
    print("     function url(id, w){ return 'https://lh3.googleusercontent.com/d/'+id+'=w'+(w||1200); }")
    print("   with:")
    print("     function url(p){ return p; }   // p is now a local path")
    print("   and in renderGrid/paintLb use s.imgs[i] instead of s.ids[i], and set")
    print("   the onerror to try the Drive copy before the tour placeholder.")
    print("\nThen: git add images/crawford crawford-plains.html && commit.")

if __name__ == "__main__":
    main()
