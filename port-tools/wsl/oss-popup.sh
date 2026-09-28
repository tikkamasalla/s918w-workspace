#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
# reload search page to get popup JS + CSRF
g = s.get('https://opensource.samsung.com/uploadList?menuItem=mobile&classification1=mobile_phone',
          timeout=30)
t = g.text
i = t.find('showSrcDownPop')
print(t[max(0,i-500):i+2000] if i > 0 else 'no inline fn; searching js refs')
# find script srcs that may define it
for m in sorted(set(re.findall(r'src="(/js/[^"]+)"', t))):
    print('js:', m)
EOF
