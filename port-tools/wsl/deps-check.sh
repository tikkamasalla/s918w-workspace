#!/bin/sh
set -u
for repo in 5ec1cff/android_bootimg Kernel-SU/java-properties Kernel-SU/ksu_props Kernel-SU/adb_client tiann/adb_client 5ec1cff/adb_client; do
  code=$(curl -s -m 20 -o /dev/null -w '%{http_code}' "https://api.github.com/repos/$repo")
  echo "$code $repo"
done
