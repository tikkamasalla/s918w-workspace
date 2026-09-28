#!/bin/sh
set -u
export GIT_TERMINAL_PROMPT=0
echo "--- git protocol, live repo:"
timeout 40 git ls-remote https://github.com/5ec1cff/android_bootimg HEAD 2>&1 | head -3
echo "--- sparse index:"
curl -s -m 25 -o /tmp/anyhow-idx -w '%{http_code} %{size_download}\n' 'https://index.crates.io/an/yh/anyhow'
head -c 200 /tmp/anyhow-idx 2>/dev/null; echo
echo "--- codeload live revs:"
for u in 'https://codeload.github.com/5ec1cff/android_bootimg/tar.gz/153423f6310fd4ae187e32da48e97b9fc613b783' 'https://codeload.github.com/5ec1cff/adb_client/tar.gz/d97a966435bebaa55017834869dec08150826aa7'; do
  curl -s -m 60 -o /tmp/t.tgz -w "%{http_code} %{size_download} $u\n" "$u"
done
