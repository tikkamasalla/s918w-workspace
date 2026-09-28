#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://lsposed.zip/', timeout=40)
t = r.text
print('home:', r.status_code, len(t))
import re
for m in sorted(set(re.findall(r'href="([^"]*\.apk[^"]*)"', t)))[:15]:
    print('  APK:', m[:170])
for m in sorted(set(re.findall(r'href="([^"]*[Dd]ownload[^"]*)"', t)))[:15]:
    print('  DL:', m[:170])
EOF
