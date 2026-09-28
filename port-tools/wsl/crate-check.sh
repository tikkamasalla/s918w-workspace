#!/bin/sh
set -u
echo "--- pin exists?"
curl -s -m 30 -o /tmp/pin.json -w '%{http_code}\n' 'https://api.github.com/repos/Kernel-SU/adb_client/commits/d97a966435bebaa55017834869dec08150826aa7'
head -c 300 /tmp/pin.json; echo
echo "--- tarball attempt:"
curl -s -m 60 -o /tmp/adb_client.tar.gz -w '%{http_code} %{size_download}\n' 'https://codeload.github.com/Kernel-SU/adb_client/tar.gz/d97a966435bebaa55017834869dec08150826aa7'
file /tmp/adb_client.tar.gz 2>/dev/null
