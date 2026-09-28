#!/bin/sh
set -u
python3 - <<'EOF'
import re, urllib.request
UA = ("Mozilla/5.0 (Linux; Android 15; APK Download Helper Audit) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36")
def get(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        r = urllib.request.urlopen(req, timeout=30)
        return r.status, r.read().decode("utf-8", "replace")
    except Exception as e:
        return f'ERR {e}'[:80], ''
s, t = get('https://www.apkmirror.com/?s=com.google.android.apps.maps')
print('apkmirror search:', s, len(t))
for m in sorted(set(re.findall(r'/apk/[^"]*maps[^"]*/', t)))[:8]:
    print('  ', m[:140])
EOF
