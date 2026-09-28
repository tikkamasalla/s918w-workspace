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
base = {
  '_csrf': field('_csrf'),
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
for page in range(1, 11):
    data = dict(base, page=str(page))
    r = s.post('https://opensource.samsung.com/uploadList', data=data, timeout=60)
    trs = re.findall(r'<tr[^>]*>(.*?)</tr>', r.text, re.S)
    data_rows = [tr for tr in trs if 'showSrcDownPop' in tr]
    if not data_rows:
        print(f'page {page}: no rows, stop')
        break
    found = []
    for tr in data_rows:
        cells = ' '.join(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', c)).strip()
                         for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tr, re.S))
        ids = re.findall(r"showSrcDownPop\('(\d+)'\)", tr)
        if 'CYB3' in cells:
            found.append((ids, cells[:400]))
    print(f'page {page}: {len(data_rows)} rows', 'CYB3-HIT' if found else '')
    for ids, cells in found:
        print('  IDS:', ids)
        print('  ', cells[:600])
        open('/tmp/s918w_cyb.html', 'w').write(r.text)
EOF
