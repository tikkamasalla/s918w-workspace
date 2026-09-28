import json
import urllib.request
from collections import defaultdict

u = 'https://raw.githubusercontent.com/bearinmindcat/morphe-patches/main/patches-list.json'
req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
d = json.load(urllib.request.urlopen(req, timeout=60))
ps = d.get('patches', [])
print('v' + str(d.get('version')), '| total patches:', len(ps))
by_app = defaultdict(list)
for p in ps:
    pkgs = tuple(sorted({(c.get('packageName') or '?')
                         for c in (p.get('compatiblePackages') or [])}))
    by_app[pkgs].append(p)
for pkgs, items in sorted(by_app.items()):
    if any('photos' in (k or '') for k in pkgs):
        print('=====', pkgs)
        for p in items:
            tg = []
            for cp in (p.get('compatiblePackages') or []):
                for t in (cp.get('targets') or []):
                    tg.append((t.get('version'), (t.get('versionCodes') or {}).get('ARM64_V8A')))
            print('  -', p.get('name'), tg)
