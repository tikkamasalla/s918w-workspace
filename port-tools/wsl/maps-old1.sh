#!/bin/sh
set -u
python3 - <<'EOF'
import urllib.request
UA = ("Mozilla/5.0 (Linux; Android 15; APK Download Helper Audit) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36")
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        r = urllib.request.urlopen(req, timeout=30)
        return r.status, len(r.read())
    except Exception as e:
        return f'ERR {e}', 0
print('apkmirror guess:', get('https://www.apkmirror.com/apk/google-inc/maps/google-maps-11-126-0103-release/'))
EOF
