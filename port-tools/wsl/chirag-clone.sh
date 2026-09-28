#!/bin/sh
set -u
cd /root
rm -rf chirag-src
git clone --depth 1 https://github.com/chirag127/morphe-patches.git chirag-src 2>&1 | tail -1
du -sh chirag-src
grep -rli "googlemaps\|google.maps\|gmaps" chirag-src/patches/src --include='*.kt' 2>/dev/null | head -20
