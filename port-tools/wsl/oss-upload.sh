#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://opensource.samsung.com/uploadList?menuItem=mobile&classification1=mobile_phone',
          timeout=30)
t = r.text
print('code:', r.status_code, 'bytes:', len(t))
open('/tmp/mob.html', 'w').write(t)
forms = re.findall(r'<form[^>]{0,300}', t)
print(len(forms), 'forms')
for f in forms[:8]:
    print('  ', f[:240].replace('\n', ' '))
# search inputs
for m in re.findall(r'<input[^>]{0,220}', t)[:20]:
    print('  IN:', m[:200].replace('\n', ' '))
EOF
