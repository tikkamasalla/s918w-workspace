#!/bin/sh
set -u
python3 - <<'EOF'
import re
import urllib.request
UA = ("Mozilla/5.0 (Linux; Android 15; APK Download Helper Audit) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36")
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")
t = get("https://apkpure.com/apk-info/com.google.android.apps.maps")
open("/mnt/e/morphe/maps-info.html", "w").write(t)
items = re.findall(r'data-dt-version="([^"]+)"[^>]*data-dt-version_code="(\d+)"', t)
print("versions found:", len(items))
for v, c in items[:15]:
    print("  ", v, c)
EOF
