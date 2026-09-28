#!/bin/sh
set -u
python3 - <<'EOF'
import re
t = open('/mnt/e/morphe/gmaps-2636-page.html', encoding='utf-8', errors='replace').read()
links = sorted(set(re.findall(r'href="([^"]+)"', t)))
for l in links:
    if any(k in l for k in ('26.36', '26.37', '26.38', '/r2?', 'download/phone', 'apks')):
        print('  ', l[:220])
EOF
