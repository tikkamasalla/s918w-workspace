import json
import urllib.request
from collections import defaultdict

u = 'https://raw.githubusercontent.com/SatanMerde/D-moniakPatches/main/patches-list.json'
req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
d = json.load(urllib.request.urlopen(req, timeout=60))
ps = d.get('patches', [])
by_app = defaultdict(list)
for p in ps:
    pkgs = tuple(sorted({(c.get('packageName') or '?')
                         for c in (p.get('compatiblePackages') or [])}))
    by_app[pkgs].append((p.get('name'), p.get('description') or ''))

def clean(s):
    return ''.join(c for c in s if ord(c) < 128)[:150]

lines = [f"D-moniak v{d.get('version')} — {len(ps)} patches", '']
for pkgs, items in sorted(by_app.items()):
    lines.append('## ' + ', '.join(pkgs) + f' ({len(items)})')
    for name, desc in items:
        lines.append(f"- {clean(name)} :: {clean(desc)}")
    lines.append('')
open(r'E:\s918w-port\tools\dmoniak-list.txt', 'w').write('\n'.join(lines))
print('apps:', len(by_app), '| patches:', len(ps))
