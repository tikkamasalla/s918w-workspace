#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://apkcombo.com/google-maps/com.google.android.apps.maps/old-versions/', timeout=40)
t = r.text
print('old-versions:', r.status_code, len(t))
import re
hits = sorted(set(re.findall(r'11\.126[^"<\s]*', t)))[:10]
print('11.126 hits:', hits)
links = sorted(set(re.findall(r'href="(/download/[^"]*|/google-maps/[^"]*)"', t)))[:15]
for l in links:
    print('  ', l[:170])
EOF
