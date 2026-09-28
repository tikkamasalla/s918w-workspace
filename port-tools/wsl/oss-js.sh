#!/bin/sh
set -u
python3 - <<'EOF'
import re
from curl_cffi import requests
h = open('/tmp/oss2.html', encoding='utf-8', errors='replace').read()
srcs = sorted(set(re.findall(r'src="([^"]+\.js[^"]*)"', h)))
print(len(srcs), 'js bundles')
for s in srcs[:20]:
    print('  ', s[:160])
open('/tmp/jslist.txt', 'w').write('\n'.join(srcs))
EOF
