#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
import re
s = requests.Session(impersonate='chrome120')
for name, url in [
    ('aptoide', 'https://google-maps.en.aptoide.com/versions'),
    ('uptodown', 'https://google-maps.en.uptodown.com/android/versions'),
]:
    try:
        r = s.get(url, timeout=40)
        t = r.text
        print('===', name, r.status_code, len(t))
        vers = sorted(set(re.findall(r'2[456]\.\d+[^"<\s]*', t)))[:12]
        print('  2x vers:', vers)
        v11 = sorted(set(re.findall(r'11\.\d+[^"<\s]*', t)))[:6]
        print('  11 vers:', v11)
    except Exception as e:
        print('===', name, 'ERR', str(e)[:100])
EOF
