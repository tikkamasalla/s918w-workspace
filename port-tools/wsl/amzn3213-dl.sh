#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
url = 'https://apkcombo.com/amazon-shopping/com.amazon.mShop.android.shopping/download/phone-32.13.2.100-apk'
r = s.get(url, timeout=120, stream=True, allow_redirects=True)
print('code:', r.status_code, 'ctype:', r.headers.get('content-type'), 'final:', str(r.url)[:120])
total = 0
with open('/mnt/e/morphe/amazon-32.13.2.100.apk', 'wb') as f:
    for chunk in r.iter_content(1 << 20):
        f.write(chunk)
        total += len(chunk)
print('saved:', total)
EOF
