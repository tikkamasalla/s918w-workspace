#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://apkcombo.com/google-maps/com.google.android.apps.maps/old-versions/', timeout=40)
t = r.text
print('old-versions:', r.status_code, len(t))
import re
links = sorted(set(re.findall(r'href="(/google-maps/com.google.android.apps.maps/download/phone-26\.36\.04[^"]*)"', t)))[:6]
for l in links:
    print('  ', l[:170])
EOF
