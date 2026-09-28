#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://opensource.samsung.com/reception/receptionSub.do?method=sub&sub=F&searchValue=SM-S918W',
          timeout=30)
t = r.text
print('bytes:', len(t))
print('title:', (re.search(r'<title>(.*?)</title>', t, re.S).group(1).strip()[:100]
                 if re.search(r'<title>(.*?)</title>', t, re.S) else None))
forms = re.findall(r'<form[^>]{0,300}', t)
print(len(forms), 'forms')
for f in forms[:6]:
    print('  ', f[:220].replace('\n', ' '))
links = sorted(set(re.findall(r'href="(/[^"]{0,140})"', t)))
print(len(links), 'site links')
for l in links[:40]:
    print('  ', l)
EOF
