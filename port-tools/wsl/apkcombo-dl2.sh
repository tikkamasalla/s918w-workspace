#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://apkcombo.com/amazon-shopping/com.amazon.mShop.android.shopping/download/phone-32.17.0.100-apk',
          timeout=40)
t = r.text
print('page:', r.status_code, len(t))
open('/mnt/e/s918w-port/apkcombo-dl.html', 'w').write(t)
for pat in (r'href="(https://[^"]+\.apk[^"]*)"',
            r'data-[a-z-]*url="([^"]+)"',
            r'(https://[a-z0-9.-]*apkcombo[a-z0-9.-]*/[^"\s<>]+\.apk[^"\s<>]*)'):
    hits = sorted(set(re.findall(pat, t)))[:10]
    if hits:
        print('---', pat[:40])
        for h in hits:
            print('   ', h[:250])
EOF
