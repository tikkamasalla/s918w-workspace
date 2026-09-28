#!/bin/sh
set -u
python3 - <<'EOF'
import re
t = open('/tmp/oss2.html', encoding='utf-8', errors='replace').read()
i = t.find('navMenu')
print('count:', t.count('navMenu'))
print(t[max(0,i-100):i+1500])
EOF
