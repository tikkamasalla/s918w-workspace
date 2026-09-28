#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://apkcombo.com/amazon-shopping/com.amazon.mShop.android.shopping/old-versions/', timeout=40)
t = r.text
print('old-versions:', r.status_code, len(t))
import re
hits = sorted(set(re.findall(r'32\.13[^"<\s]*', t)))[:10]
print('32.13 hits:', hits)
links = sorted(set(re.findall(r'href="(/amazon-shopping/com.amazon.mShop.android.shopping/download/[^"]*)"', t)))[:20]
for l in links:
    print('  ', l[:170])
EOF
