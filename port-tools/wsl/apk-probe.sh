#!/bin/sh
set -u
python3 - <<'EOF'
from curl_cffi import requests
s = requests.Session(impersonate='chrome120')
probes = {
  'apkmirror-search': 'https://www.apkmirror.com/?s=com.amazon.mShop.android.shopping',
  'apkpure-page': 'https://apkpure.com/amazon-shopping/com.amazon.mShop.android.shopping',
  'apkcombo-page': 'https://apkcombo.com/amazon-shopping/com.amazon.mShop.android.shopping/',
  'uptodown-page': 'https://amazon-shopping.en.uptodown.com/android',
}
for name, url in probes.items():
    try:
        r = s.get(url, timeout=30)
        t = r.text
        print(f'== {name}: {r.status_code} {len(t)}')
        import re
        vers = sorted(set(re.findall(r'32\.1[67]\.[\d.]+', t)))[:10]
        print('   32.1x versions seen:', vers)
    except Exception as e:
        print(f'== {name}: ERR {type(e).__name__} {str(e)[:100]}')
EOF
