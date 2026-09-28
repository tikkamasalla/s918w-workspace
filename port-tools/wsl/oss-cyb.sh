#!/bin/sh
set -u
python3 - <<'EOF'
import re
t = open('/tmp/s918w_search.html', encoding='utf-8', errors='replace').read()
trs = re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.S)
for tr in trs:
    if 'SM-S918' not in tr:
        continue
    cells = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', c)).strip()
             for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tr, re.S)]
    blob = ' '.join(cells)
    ids = re.findall(r"showSrcDownPop\('(\d+)'\)", tr)
    if 'CYB3' in blob or 'CYB' in blob:
        print('IDS:', ids)
        print(blob[:3000])
        print('======')
# also: how many pages? look for pagination
pg = sorted(set(re.findall(r'page["\']?\s*[:=]\s*["\']?(\d+)', t)))[:10]
print('page hints:', pg)
tot = re.findall(r'(?:total|Total)[^0-9]{0,20}(\d+)', t)[:5]
print('total hints:', tot)
EOF
