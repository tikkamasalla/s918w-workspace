#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://modules.kernelsu.org/module/zygisksu', timeout=40)
print(r.status_code, len(r.content))
open('/tmp/znmod.html', 'w').write(r.text)
t = r.text
for pat in (r'href="([^"]*(?:download|apk|zip)[^"]*)"', r'(/[a-zA-Z0-9/_.-]*download[a-zA-Z0-9/_.-]*)', r'(https://[a-zA-Z0-9./_-]*zygisk[a-zA-Z0-9./_-]*)'):
    hits = sorted(set(re.findall(pat, t, re.I)))[:12]
    if hits:
        print('---', pat[:40])
        for h in hits:
            print('   ', h[:220])
EOF
