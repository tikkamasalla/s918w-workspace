#!/bin/sh
set -u
python3 - <<'EOF'
import urllib.request
UA = ("Mozilla/5.0 (Linux; Android 15; APK Download Helper Audit) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36")
req = urllib.request.Request(
    "https://apkpure.com/google-maps/com.google.android.apps.maps/download",
    headers={"User-Agent": UA})
r = urllib.request.urlopen(req, timeout=40)
t = r.read().decode("utf-8", "replace")
print("page:", r.status, len(t))
import re
for pat in (r'href="(https://d\.apkpure\.com[^"]+)"',):
    for h in sorted(set(re.findall(pat, t)))[:8]:
        print("   ", h[:220].replace("&amp;", "&"))
EOF
