#!/bin/sh
set -u
curl -s -m 30 -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
  -o /tmp/oss.html -w '%{http_code} %{size_download}\n' \
  'https://opensource.samsung.com/'
grep -oiE 'src="[^"]{0,200}' /tmp/oss.html | head -30
