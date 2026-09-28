#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://google-maps.en.uptodown.com/android/versions', timeout=40)
t = r.text
print('uptodown versions:', r.status_code, len(t))
import re
vers = sorted(set(re.findall(r'11\.126[^"<\s]*', t)))[:10]
print('11.126 hits:', vers)
links = sorted(set(re.findall(r'href="([^"]*11[^"]*download[^"]*|[^"]*download[^"]*11[^"]*)"', t)))[:10]
for l in links:
    print('  ', l[:160])
EOF
