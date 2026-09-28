#!/bin/sh
set -u
for repo in 5ec1cff/java-properties 5ec1cff/ksu_props; do
  code=$(curl -s -m 20 -o /dev/null -w '%{http_code}' "https://api.github.com/repos/$repo")
  echo "$code $repo"
done
echo "--- adb_client pin in new home:"
curl -s -m 30 -o /dev/null -w '%{http_code}\n' 'https://api.github.com/repos/5ec1cff/adb_client/commits/d97a966435bebaa55017834869dec08150826aa7'
echo "--- lock wants:"
grep -B1 -A3 'name = "java-properties"' /root/KernelSU-dm3q/Cargo.lock | head -6
grep -B1 -A3 'name = "prop-rs-android"\|name = "ksu_props"\|name = "ksu-props"' /root/KernelSU-dm3q/Cargo.lock | head -8
grep -B1 -A3 'name = "android-bootimg"' /root/KernelSU-dm3q/Cargo.lock | head -6
