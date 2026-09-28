#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
import re, html
s = requests.Session(impersonate='chrome120')
url = 'https://apkcombo.com/google-photos/com.google.android.apps.photos/download/phone-7.94.0.984908898-apk'
r = s.get(url, timeout=60)
t = r.text
print('page:', r.status_code, len(t))
open('/mnt/e/morphe/photos-794-page.html', 'w').write(t)
m = re.search(r'href="(/r2\?u=[^"]+)"', t)
print('r2 found:', bool(m))
if m:
    dl = 'https://apkcombo.com' + html.unescape(m.group(1)).replace('&amp;', '&')
    r2 = s.get(dl, timeout=600, stream=True, allow_redirects=True)
    print('code:', r2.status_code, r2.headers.get('content-type'))
    total = 0
    with open('/mnt/e/morphe/photos-7.94.0.apks', 'wb') as f:
        for chunk in r2.iter_content(1 << 20):
            f.write(chunk)
            total += len(chunk)
    print('saved:', total)
EOF
