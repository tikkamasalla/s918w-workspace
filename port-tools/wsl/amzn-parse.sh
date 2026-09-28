#!/bin/sh
set -u
python3 - <<'EOF'
import re
t = open('/mnt/e/morphe/amazon-32.13.2.100.apk', encoding='utf-8', errors='replace').read()
print('title:', re.findall(r'<title>(.*?)</title>', t)[:1])
links = sorted(set(re.findall(r'href="([^"]+)"', t)))
for l in links:
    if any(k in l for k in ('download', '.apk', 'xapk', 'apkcombo.com/dl', 'redirect')):
        print('  ', l[:200])
EOF
