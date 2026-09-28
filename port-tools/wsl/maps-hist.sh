#!/bin/sh
set -u
python3 - <<'EOF'
import re, urllib.request
UA = ("Mozilla/5.0 (Linux; Android 15; APK Download Helper Audit) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36")
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    r = urllib.request.urlopen(req, timeout=30)
    return r.read().decode("utf-8", "replace")
t = get('https://www.apkmirror.com/apk/google-inc/maps/')
vers = re.findall(r'google-maps-([\d\-]+)-release', t)
print('recent:', sorted(set(vers))[:20])
EOF
