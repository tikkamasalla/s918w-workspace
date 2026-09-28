#!/bin/sh
set -u
python3 - <<'EOF'
import re, glob
for f in sorted(glob.glob('/tmp/gmdex/*.dex')):
    d = open(f, 'rb').read()
    for pat in (b'speedometer', b'Speedometer', b'compass', b'Compass'):
        print(f.split('/')[-1], pat.decode(), d.lower().count(pat.lower()))
EOF
