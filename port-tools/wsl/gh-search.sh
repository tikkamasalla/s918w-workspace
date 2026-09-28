#!/bin/sh
set -u
python3 - <<'EOF'
import json
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
s.headers['Accept'] = 'application/vnd.github+json'
for q in ('S918WVLS6CYB3', 'S918W CYB3 kernel', 'sm8550 dm3q kernel samsung'):
    try:
        r = s.get('https://api.github.com/search/repositories',
                  params={'q': q, 'per_page': 5}, timeout=30)
        d = r.json()
        print('###', q, '-> total:', d.get('total_count'))
        for it in d.get('items', [])[:5]:
            print('   ', it['full_name'], '|', (it.get('description') or '')[:100])
    except Exception as e:
        print('###', q, 'ERR', type(e).__name__, str(e)[:150])
EOF
