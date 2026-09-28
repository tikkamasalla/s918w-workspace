#!/bin/sh
set -u
echo "--- ksu_props forks, rev 699849f3e4db47b622bcb7fae8e76c728b1b65a6:"
for f in ReSukiSU/ksu_props JingMatrix/ksu_props MySU-org/ksu_props zaominn/ksu_props; do
  code=$(curl -s -m 45 -o /tmp/k.tgz -w '%{http_code} %{size_download}' "https://codeload.github.com/$f/tar.gz/699849f3e4db47b622bcb7fae8e76c728b1b65a6")
  echo "$code $f"
done
echo "--- java-properties on crates.io:"
curl -s -m 25 'https://index.crates.io/ja/va/java-properties' -o /tmp/jp-idx -w '%{http_code}\n'
python3 -c "
import json
vers = []
for l in open('/tmp/jp-idx', errors='replace'):
    l = l.strip()
    if l.startswith('{'):
        d = json.loads(l)
        if not d.get('yanked'):
            vers.append(d['vers'])
print('un-yanked versions:', vers)"
