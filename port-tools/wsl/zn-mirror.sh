#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
r = s.get('https://modules.kernelsu.org/module/zygisksu', timeout=40)
print(r.status_code, len(r.content))
t = r.text
hits = sorted(set(re.findall(r'https://[^"\s<>]*?(?:\.zip|download)[^"\s<>]*', t)))
for m in hits[:15]:
    print('  ', m[:200])
EOF
