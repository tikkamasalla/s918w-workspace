#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
ids = {
    'netcut-v1.4.9': '6234607',
    'netcut-1.7.7.fix-64': '6362913',
    'netcut-1.7.9': '6362914',
}
for name, aid in ids.items():
    url = f'https://xdaforums.com/attachments/{name}-apk.{aid}/'
    try:
        r = s.get(url, timeout=60)
        ct = r.headers.get('content-type', '')
        print(name, r.status_code, ct, len(r.content))
        if 'apk' in ct or 'octet' in ct:
            open(f'/mnt/e/phone-pending/{name}.apk', 'wb').write(r.content)
            print('   saved')
        else:
            print('   page?', r.text[:150].replace('\n', ' '))
    except Exception as e:
        print(name, 'ERR', str(e)[:100])
EOF
