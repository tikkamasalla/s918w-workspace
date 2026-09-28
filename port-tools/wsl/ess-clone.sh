#!/bin/sh
set -u
cd /root
rm -rf essentials-src
git clone --depth 1 https://github.com/sameerasw/essentials.git essentials-src 2>&1 | tail -1
du -sh essentials-src
grep -rli "low.power\|lowpower\|battery.saver\|power.save" essentials-src/app/src --include='*.kt' 2>/dev/null | head -20
