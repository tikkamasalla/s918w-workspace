#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
import re
s = requests.Session(impersonate='chrome120')
url = 'https://apkcombo.com/google-maps/com.google.android.apps.maps/download/phone-26.36.04.973607363-apk'
r = s.get(url, timeout=120)
t = r.text
print('page:', r.status_code, len(t))
open('/mnt/e/morphe/gmaps-2636-dl.html', 'w').write(t)
m = re.search(r'href="(/r2\?u=[^"]+)"', t)
print('r2 found:', bool(m))
if m:
    import html
    dl = 'https://apkcombo.com' + html.unescape(m.group(1)).replace('&amp;', '&')
    r2 = s.get(dl, timeout=600, stream=True, allow_redirects=True)
    print('code:', r2.status_code, r2.headers.get('content-type'))
    total = 0
    with open('/mnt/e/morphe/gmaps-26.36.04.apks', 'wb') as f:
        for chunk in r2.iter_content(1 << 20):
            f.write(chunk)
            total += len(chunk)
    print('saved:', total)
EOF
