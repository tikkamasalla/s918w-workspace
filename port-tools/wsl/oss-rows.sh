#!/bin/sh
set -u
python3 - <<'EOF'
import re
t = open('/tmp/s918w_search.html', encoding='utf-8', errors='replace').read()
# table rows
trs = re.findall(r'<tr[^>]*>(.*?)</tr>', t, re.S)
print(len(trs), 'rows')
for tr in trs:
    if 'SM-S918' not in tr:
        continue
    cells = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', c)).strip()
             for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', tr, re.S)]
    links = re.findall(r'href="([^"]{1,200})"', tr)
    print('ROW:', ' | '.join(cells)[:220])
    for l in links:
        print('    ->', l[:200])
EOF
