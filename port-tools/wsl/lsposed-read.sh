#!/bin/sh
set -u
cd /tmp
python3 -c "import zipfile; z=zipfile.ZipFile('/root/LSPosed-v2.2.0-7854-release.zip'); print(open('/dev/stdin').read())" < /dev/null 2>/dev/null
python3 - <<'EOF'
import zipfile
z = zipfile.ZipFile('/root/LSPosed-v2.2.0-7854-release.zip')
print('=== module.prop:')
print(z.read('module.prop').decode()[:800])
print('=== README head:')
print(z.read('README.md').decode()[:1500])
print('=== bin/ lib/:')
[print(' ', x) for x in z.namelist() if x.startswith(('bin/', 'lib/'))][:20]
EOF
cp /root/LSPosed-v2.2.0-7854-release.zip /mnt/e/s918w-port/
