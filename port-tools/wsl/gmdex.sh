#!/bin/sh
set -u
python3 - <<'EOF'
import zipfile
z = zipfile.ZipFile('/mnt/e/morphe/gmaps-latest.apk')
dexes = [n for n in z.namelist() if n.endswith('.dex')]
print(len(dexes), 'dex files')
for n in dexes:
    z.extract(n, '/tmp/gmaps-dex')
print('extracted')
EOF
ls /tmp/gmaps-dex | head -20
