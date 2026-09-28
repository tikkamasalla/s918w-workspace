#!/bin/sh
set -u
for u in \
  'https://api.github.com/repos/LSPosed/LSPosed/releases/latest' \
  'https://api.github.com/repos/SoClear/OneUIX/releases/latest' \
  'https://api.github.com/repos/hxreborn/amznkiller/releases/latest' \
  'https://api.github.com/repos/Xposed-Modules-Repo/ru.mike.updatelocker/releases/latest' \
  'https://api.github.com/repos/hxreborn/punch-hole-download-progress/releases/latest' \
  ; do
  echo "=== $u"
  curl -s -m 30 "$u" | python3 -c "
import json,sys
d = json.load(sys.stdin)
print('TAG:', d.get('tag_name'), '|', d.get('name','')[:60])
for a in d.get('assets', [])[:8]:
    print('  ', a['size'], a['name'])
    print('   ', a['browser_download_url'][:150])
"
done
