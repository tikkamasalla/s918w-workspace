#!/bin/sh
set -u
python3 - <<'EOF'
import re, urllib.request
UA = ("Mozilla/5.0 (Linux; Android 15; APK Download Helper Audit) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36")
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
t = get('https://www.apkmirror.com/apk/google-inc/maps/google-maps-25-26-04-774458481-release/google-maps-25-26-04-774458481-android-apk-download/')
for pat in (r'download\.php[^"\s]*', r'forcebase[^"\s]*', r'href="([^"]*key=[^"]*)"', r'location\.href\s*=\s*"([^"]+)"'):
    hits = sorted(set(re.findall(pat, t)))[:6]
    print(pat[:30], '->', [h[:170] for h in hits])
EOF
