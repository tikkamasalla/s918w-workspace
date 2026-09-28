#!/bin/sh
set -u
python3 - <<'EOF'
import re
t = open('/tmp/common.js', encoding='utf-8', errors='replace').read()
i = t.find('navMenu')
print('navMenu at', i)
print(t[max(0,i-200):i+2500])
EOF
