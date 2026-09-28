#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests

def search(term):
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
      'searchValue': term,
    }
    print('=' * 15, term, '=' * 15)
    for page in range(1, 4):
        data = dict(base, page=str(page))
        r = s.post('https://opensource.samsung.com/uploadList', data=data, timeout=60)
        trs = re.findall(r'<tr[^>]*>(.*?)</tr>', r.text, re.S)
        data_rows = [tr for tr in trs if 'showSrcDownPop' in tr]
        if not data_rows:
            print(f'page {page}: end')
            break
        for tr in data_rows:
            cells = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', c)).strip()
                     for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tr, re.S)]
            ids = re.findall(r"showSrcDownPop\('(\d+)'\)", tr)
            models = cells[0][:100] if len(cells) > 0 else '?'
            vers = cells[1][:300] if len(cells) > 1 else '?'
            print(f'page {page} id={ids} models={models}')
            print(f'   vers={vers}')

search('S918WVLS6CYB3')
search('SM-S916U1')
EOF
