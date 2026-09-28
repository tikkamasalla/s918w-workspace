#!/bin/sh
set -u
python3 - <<'EOF'
import zipfile, glob
src = glob.glob('/mnt/c/Users/Aows/Downloads/*maps_26.36*')[0]
print('src:', src)
z = zipfile.ZipFile(src)
dexes = [n for n in z.namelist() if n.endswith('.dex')]
print(len(dexes), 'dex files')
import os
os.makedirs('/tmp/gmdex', exist_ok=True)
for n in dexes[:6]:
    z.extract(n, '/tmp/gmdex')
print('extracted first 6')
EOF
ls -la /tmp/gmdex/ /tmp/gmdex/*.dex 2>/dev/null | head -12
