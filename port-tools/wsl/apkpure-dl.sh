#!/bin/sh
set -u
python3 - <<'EOF'
import re
import urllib.request
UA = ("Mozilla/5.0 (Linux; Android 15; APK Download Helper Audit) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36")
req = urllib.request.Request(
    "https://apkpure.com/amazon-shopping/com.amazon.mShop.android.shopping/download",
    headers={"User-Agent": UA})
r = urllib.request.urlopen(req, timeout=40)
t = r.read().decode("utf-8", "replace")
print("page:", r.status, len(t))
open("/mnt/e/s918w-port/apkpure-dl.html", "w").write(t)
for pat in (r'href="(https://d\.apkpure\.com[^"]+)"',
            r'href="(https://download\.apkpure[^"]+)"',
            r'(https://[^"\s<>]*apkpure[^"\s<>]*\.(?:apk|xapk)[^"\s<>]*)'):
    hits = sorted(set(re.findall(pat, t)))[:10]
    if hits:
        print("---", pat[:45])
        for h in hits:
            print("   ", h[:250])
EOF
