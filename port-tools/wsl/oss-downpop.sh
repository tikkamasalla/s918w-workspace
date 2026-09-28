#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
g = s.get('https://opensource.samsung.com/uploadList?menuItem=mobile&classification1=mobile_phone',
          timeout=30)
m = re.search(r'name="_csrf" value="([^"]+)"', g.text)
token = m.group(1) if m else ''
print('csrf:', token[:20], '...')
r = s.post('https://opensource.samsung.com/downSrcMPop',
           data={'uploadId': '14018'},
           headers={'X-CSRF-TOKEN': token, 'X-Requested-With': 'XMLHttpRequest'},
           timeout=60)
print('POST:', r.status_code, len(r.content))
open('/tmp/downpop.html', 'w').write(r.text)
t = r.text
# file rows
for m in re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.S)[:20]:
    cells = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', c)).strip()
             for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', m, re.S)]
    if cells:
        print('ROW:', ' | '.join(cells)[:220])
for l in sorted(set(re.findall(r'(?:href|action|src)="([^"]{1,220})"', t)))[:30]:
    print('LINK:', l[:220])
EOF
