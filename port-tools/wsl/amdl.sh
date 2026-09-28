#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
url = 'https://www.apkmirror.com/apk/google-inc/maps/google-maps-25-26-04-774458481-release/google-maps-25-26-04-774458481-android-apk-download/download/?key=b4ff8ed0fc7dd7dd05f3d4fc77daf776ec2f6e0a'
r = s.get(url, timeout=300, stream=True, allow_redirects=True)
print('code:', r.status_code, 'ctype:', r.headers.get('content-type'), 'final:', str(r.url)[:130])
total = 0
with open('/mnt/e/morphe/gmaps-25.26.apk', 'wb') as f:
    for chunk in r.iter_content(1 << 20):
        f.write(chunk)
        total += len(chunk)
        if total > 350 * (1 << 20):
            break
print('saved:', total)
EOF
