#!/bin/sh
set -u
python3 - <<'EOF'
import json
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
urls = {
  'aptoide-app': 'https://web-api.aptoide.com/api/7/app/get/package_name=com.amazon.mShop.android.shopping',
  'aptoide-versions': 'https://web-api.aptoide.com/api/7/app/get/package_name=com.amazon.mShop.android.shopping/show_versions=true',
}
for name, url in urls.items():
    try:
        r = s.get(url, timeout=30)
        print(f'== {name}: {r.status_code} {len(r.content)}')
        open(f'/mnt/e/s918w-port/aptoide-{name}.json', 'w').write(r.text)
    except Exception as e:
        print(f'== {name}: ERR {type(e).__name__}')
EOF
