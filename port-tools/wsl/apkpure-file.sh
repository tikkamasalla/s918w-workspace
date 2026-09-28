#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
url = 'https://d.apkpure.com/b/XAPK/com.amazon.mShop.android.shopping?versionCode=1243230206&nc=arm64-v8a&sv=31'
try:
    r = s.get(url, timeout=120, stream=True)
    print('code:', r.status_code, 'ctype:', r.headers.get('content-type'))
    if 'apk' in (r.headers.get('content-type') or '') or int(r.headers.get('content-length', 0)) > 50000000:
        total = 0
        with open('/mnt/e/morphe/amazon-32.17.0.100.xapk', 'wb') as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)
                total += len(chunk)
        print('saved bytes:', total)
    else:
        print('body head:', r.content[:200])
except Exception as e:
    print('ERR', type(e).__name__, str(e)[:200])
EOF
