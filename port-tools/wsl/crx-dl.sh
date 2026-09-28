#!/bin/sh
set -u
cd /mnt/e/morphe || exit 1
curl -sSL -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
  'https://clients2.google.com/service/update2/crx?response=redirect&prodversion=120&x=id%3Dolefkhnepnhckieapdkjebebogajcmel%26installsource%3Dondemand%26uc' \
  -o amzsort.crx
ls -la amzsort.crx
