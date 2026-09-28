#!/bin/sh
set -u
python3 - <<'EOF'
import re
h = open('/tmp/oss2.html', encoding='utf-8', errors='replace').read()
print('title:', re.search(r'<title>(.*?)</title>', h, re.S).group(1)[:120])
# candidate API / search URLs
for pat in (r'/(api/[^"\s<>]{0,120})', r'(/search[^"\s<>]{0,120})',
            r'(https://[^"\s<>]*search[^"\s<>]{0,120})',
            r'(/reception/[^"\s<>]{0,160})'):
    hits = sorted(set(re.findall(pat, h)))[:15]
    print(pat, '->', len(hits))
    for x in hits:
        print('   ', x[:160])
EOF
