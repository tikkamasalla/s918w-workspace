#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
url = 'https://d.apkpure.com/b/APK/com.google.android.apps.maps?versionCode=1068785740'
r = s.get(url, timeout=300, stream=True)
print('code:', r.status_code, 'ctype:', r.headers.get('content-type'))
total = 0
with open('/mnt/e/morphe/gmaps-latest.apk', 'wb') as f:
    for chunk in r.iter_content(1 << 20):
        f.write(chunk)
        total += len(chunk)
print('saved:', total)
EOF
