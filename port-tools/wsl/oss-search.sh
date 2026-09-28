#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
urls = [
  'https://opensource.samsung.com/reception/receptionSub.do?method=sub&sub=F&searchValue=SM-S918W',
  'https://opensource.samsung.com/reception/receptionMain.do?method=receptionMain',
]
for u in urls:
    try:
        r = s.get(u, timeout=30)
        print(r.status_code, len(r.content), u[:90])
        if r.status_code == 200 and 'S918W' in r.text:
            open('/tmp/s918w.html', 'w').write(r.text)
            print('SAVED with S918W match')
    except Exception as e:
        print('ERR', u[:60], type(e).__name__, str(e)[:120])
EOF
