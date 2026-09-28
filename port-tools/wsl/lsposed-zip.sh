#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120', allow_redirects=True)
try:
    r = s.get('https://lsposed.zip/', timeout=60)
    print('final:', r.status_code, len(r.content))
    print('url:', str(r.url)[:200])
    print('ctype:', r.headers.get('content-type'))
    cd = r.headers.get('content-disposition', '')
    print('disp:', cd[:200])
    open('/tmp/lsposed.bin', 'wb').write(r.content)
except Exception as e:
    print('ERR', type(e).__name__, str(e)[:200])
EOF
file /tmp/lsposed.bin 2>/dev/null
ls -la /tmp/lsposed.bin 2>/dev/null
