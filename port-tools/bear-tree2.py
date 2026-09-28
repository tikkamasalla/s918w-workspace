import json
import subprocess

out = subprocess.run(
    ['gh', 'api',
     'repos/bearinmindcat/morphe-patches/git/trees/main?recursive=1'],
    capture_output=True, text=True, timeout=120)
tree = json.loads(out.stdout)['tree']
paths = sorted(t['path'] for t in tree
               if '/maps/' in t['path'] and t['path'].endswith('.kt'))
for p in paths:
    if 'power' in p.lower() or 'speedo' in p.lower() or 'refresh' in p.lower() \
            or 'zoom' in p.lower() or 'offline' in p.lower():
        print(p)
