#!/bin/sh
set -u
python3 - <<'EOF'
import re
t = open('/mnt/e/s918w-port/apkcombo-dl.html', encoding='utf-8', errors='replace').read()
for pat in (r'<a[^>]{0,200}(?:download|btn)[^>]{0,200}>',
            r'var [a-zA-Z_]{1,30} ?= ?"[^"]{10,200}"',
            r'/download/[^"\s<>]{1,120}'):
    hits = sorted(set(re.findall(pat, t)))[:12]
    if hits:
        print('---', pat[:40])
        for h in hits:
            print('   ', h[:250].replace('\n', ' '))
EOF
