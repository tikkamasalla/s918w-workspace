#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
import re
s = requests.Session(impersonate='chrome120')
t = open('/mnt/e/morphe/amazon-32.13.2.100.apk', encoding='utf-8', errors='replace').read()
m = re.search(r'href="(/r2\?u=[^"]+)"', t)
print('r2 found:', bool(m))
if m:
    import html
    url = 'https://apkcombo.com' + html.unescape(m.group(1)).replace('&amp;', '&')
    print('fetching...')
    r = s.get(url, timeout=300, stream=True, allow_redirects=True)
    print('code:', r.status_code, r.headers.get('content-type'))
    total = 0
    with open('/mnt/e/morphe/amazon-32.13.2.100.apks', 'wb') as f:
        for chunk in r.iter_content(1 << 20):
            f.write(chunk)
            total += len(chunk)
    print('saved:', total)
EOF
