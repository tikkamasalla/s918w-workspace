#!/bin/sh
set -u
python3 - <<'EOF'
import json
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
s.headers['Accept'] = 'application/vnd.github+json'
for q in ('java-properties rust parser', 'ksu_props'):
    try:
        r = s.get('https://api.github.com/search/repositories',
                  params={'q': q, 'per_page': 6}, timeout=30)
        d = r.json()
        print('###', q, '->', d.get('total_count'))
        for it in d.get('items', [])[:6]:
            print('   ', it['full_name'], '|', (it.get('description') or '')[:90])
    except Exception as e:
        print('###', q, 'ERR', str(e)[:150])
EOF
