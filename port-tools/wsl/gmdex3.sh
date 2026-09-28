#!/bin/sh
set -u
python3 - <<'EOF'
import re, glob
methods = set()
for f in sorted(glob.glob('/tmp/gmdex/*.dex')):
    d = open(f, 'rb').read()
    for pat in (rb'speedometer', rb'Speedometer', rb'SPEEDOMETER',
                rb'compass', rb'Compass', rb'COMPASS',
                rb'speedLimit', rb'SpeedLimit'):
        for m in re.finditer(pat + rb'[A-Za-z0-9_$]{0,40}', d):
            methods.add(m.group(0).decode('utf-8', 'replace'))
print(len(methods), 'distinct matches')
for m in sorted(methods)[:80]:
    print('  ', m)
EOF
