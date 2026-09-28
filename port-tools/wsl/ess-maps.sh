#!/bin/sh
set -u
cd /root/essentials-src
grep -rli "apps.maps\|google_maps\|gmaps" app/src --include='*.kt' 2>/dev/null | head -20
echo "--- low-power + maps combos:"
grep -rli "maps" app/src --include='*.kt' 2>/dev/null | head -20
