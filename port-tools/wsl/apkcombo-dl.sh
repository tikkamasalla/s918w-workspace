#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://apkcombo.com/amazon-shopping/com.amazon.mShop.android.shopping/', timeout=30)
t = r.text
open('/tmp/apkcombo.html', 'w').write(t)
for pat in (r'href="([^"]*32\.17\.0\.100[^"]*)"',
            r'href="([^"]*download[^"]*)"'):
    hits = sorted(set(re.findall(pat, t)))[:15]
    print('---', pat[:30])
    for h in hits:
        print('   ', h[:220])
EOF
