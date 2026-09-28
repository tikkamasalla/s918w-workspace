#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
g = s.get('https://opensource.samsung.com/uploadList?menuItem=mobile&classification1=mobile_phone',
          timeout=30)
t = g.text
def field(nm):
    m = re.search(r'name="' + nm + r'" value="([^"]*)"', t)
    return m.group(1) if m else ''
data = {
  '_csrf': field('_csrf'),
  'page': '1',
  'menuItem': 'mobile',
  'menuItemDesc': 'Mobile',
  'classification1': 'mobile_phone',
  'classification1Desc': 'Mobile Phone',
  'classification2': '',
  'classification2Desc': '',
  'classification3': '',
  'classification3Desc': '',
  'searchValue': 'SM-S918W',
}
r = s.post('https://opensource.samsung.com/uploadList', data=data, timeout=60)
print('POST:', r.status_code, len(r.content))
open('/tmp/s918w_search.html', 'w').write(r.text)
rows = re.findall(r'SM-S918W[^<]{0,60}', r.text)
print(len(rows), 'SM-S918W mentions')
for x in sorted(set(rows))[:30]:
    print('  ', x.strip()[:100])
EOF
