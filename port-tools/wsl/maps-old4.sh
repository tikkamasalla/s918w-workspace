#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
try:
    r = s.get('https://apkcombo.com/search/google%20maps', timeout=30)
    t = r.text
    print('apkcombo search:', r.status_code, len(t))
    import re
    for m in sorted(set(re.findall(r'href="(/[^"]*maps[^"]*)"', t)))[:10]:
        print('  ', m[:150])
except Exception as e:
    print('ERR', str(e)[:120])
EOF
