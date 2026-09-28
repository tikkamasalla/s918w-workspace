#!/bin/sh
set -u
python3 - <<'EOF'
import re
import urllib.request
UA = ("Mozilla/5.0 (Linux; Android 15; APK Download Helper Audit) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36")
req = urllib.request.Request(
    "https://apkpure.com/apk-info/com.amazon.mShop.android.shopping",
    headers={"User-Agent": UA})
r = urllib.request.urlopen(req, timeout=40)
t = r.read().decode("utf-8", "replace")
print("bytes:", len(t))
open("/mnt/e/s918w-port/apk-info.html", "w").write(t)
idx = [m.start() for m in re.finditer(r"32\.17\.0\.100", t)]
print("32.17.0.100 hits:", len(idx))
for i in idx[:6]:
    print(".....", t[max(0, i-400):i+400].replace("\n", " ")[:800])
    print("=====")
EOF
