#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120', allow_redirects=True)
r = s.get('https://lsposed.zip/', timeout=90)
print('final:', r.status_code, len(r.content))
print('ctype:', r.headers.get('content-type'))
print('disp:', (r.headers.get('content-disposition') or '')[:200])
open('/root/LSPosed-v2.2.0-7854-release.zip', 'wb').write(r.content)
EOF
ls -la /root/LSPosed-v2.2.0-7854-release.zip
python3 -c "import zipfile; z=zipfile.ZipFile('/root/LSPosed-v2.2.0-7854-release.zip'); n=z.namelist(); print(len(n),'entries'); [print(' ', x) for x in n if len(x.split('/'))<=2][:30]"
