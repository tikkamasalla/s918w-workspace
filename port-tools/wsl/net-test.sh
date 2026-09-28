#!/bin/sh
set -u
echo "--- dns:"
getent hosts github.com | head -3
echo "--- curl:"
curl -s -m 20 -o /dev/null -w '%{http_code}\n' https://github.com
echo "--- git with timeout:"
timeout 40 git ls-remote https://github.com/Kernel-SU/adb_client HEAD 2>&1 | head -3
echo "rc=$?"
