#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
for u in ('https://github.com/Dr-TSNG/ZygiskNext/releases/tag/v1.5.0',
          'https://github.com/Dr-TSNG/ZygiskNext/releases'):
    try:
        r = s.get(u, timeout=40)
        print(r.status_code, len(r.content), u[-30:])
        if r.status_code == 200:
            assets = sorted(set(re.findall(r'/Dr-TSNG/ZygiskNext/releases/download/[^"\s<>]+', r.text)))
            for a in assets[:10]:
                print('   ', a)
            open('/tmp/zn.html', 'w').write(r.text)
    except Exception as e:
        print('ERR', u[-30:], type(e).__name__, str(e)[:120])
EOF
