import json
import subprocess

out = subprocess.run(
    ['gh', 'api',
     'repos/bearinmindcat/morphe-patches/git/trees/main?recursive=1'],
    capture_output=True, text=True, timeout=120)
tree = json.loads(out.stdout)['tree']
hits = [t['path'] for t in tree
        if 'maps' in t['path'].lower() or 'speedo' in t['path'].lower()
        or 'power' in t['path'].lower() or 'compass' in t['path'].lower()]
for h in hits[:40]:
    print(h)
print('total hits:', len(hits))
