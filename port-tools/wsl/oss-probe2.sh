#!/bin/sh
set -u
export DEBIAN_FRONTEND=noninteractive
apt-get install -y -q python3-pip 2>&1 | tail -1
pip3 install -q --break-system-packages curl_cffi 2>&1 | tail -1
python3 - <<'EOF'
from curl_cffi import requests
try:
    r = requests.get('https://opensource.samsung.com/',
                     impersonate='chrome120', timeout=30)
    print('code:', r.status_code, 'bytes:', len(r.content))
    open('/tmp/oss2.html', 'wb').write(r.content)
except Exception as e:
    print('ERR:', type(e).__name__, str(e)[:200])
EOF
