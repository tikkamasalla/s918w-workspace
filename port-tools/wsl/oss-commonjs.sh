#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://opensource.samsung.com/js/common.js?v=202609190821', timeout=30)
print('common.js:', r.status_code, len(r.content))
open('/tmp/common.js', 'wb').write(r.content)
t = r.text
for pat in (r'url\s*:\s*["\']([^"\']{1,140})',
            r'\$\.(?:get|post|ajax)\(\s*["\']([^"\']{1,140})',
            r'/(?:download|release|reception|notice|board)[^"\s<>]{0,120}'):
    hits = sorted(set(re.findall(pat, t)))[:25]
    print('---', pat)
    for x in hits:
        print('   ', x[:160])
EOF
