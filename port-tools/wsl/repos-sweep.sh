#!/bin/sh
set -u
for repo in LSPosed/LSPosed JingMatrix/Vector SoClear/OneUIX HeheJuice/OneUI-Settings-Hook hxreborn/amznkiller Xposed-Modules-Repo/ru.mike.updatelocker hxreborn/punch-hole-download-progress LSPosed/CorePatch KernelSU-Modules-Repo/zygisk_lsposed Dr-TSNG/ZygiskNext; do
  code=$(curl -s -m 20 -o /dev/null -w '%{http_code}' "https://api.github.com/repos/$repo")
  echo "$code $repo"
done
