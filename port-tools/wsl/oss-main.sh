#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://opensource.samsung.com/main', timeout=30)
t = r.text
print('bytes:', len(t))
links = sorted(set(re.findall(r'href="([^"]{1,160})"', t)))
print(len(links), 'links')
for l in links:
    print('  ', l)
EOF
