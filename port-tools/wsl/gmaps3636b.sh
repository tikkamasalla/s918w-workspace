#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://apkcombo.com/google-maps/com.google.android.apps.maps/download/phone-26.36.04.973607363-apk', timeout=120, stream=True, allow_redirects=True)
print('code:', r.status_code, r.headers.get('content-type'), str(r.url)[:130])
total = 0
with open('/mnt/e/morphe/gmaps-2636-page.html', 'wb') as f:
    for chunk in r.iter_content(1 << 20):
        f.write(chunk)
        total += len(chunk)
print('saved:', total)
EOF
