#!/bin/sh
set -u
grep -n -i "apkpure" /root/helper-for-morphe/tools/audit_helper_sources.py | head -25
echo "--- headers:"
grep -n -iE "user.agent|header" /root/helper-for-morphe/tools/audit_helper_sources.py | head -12
