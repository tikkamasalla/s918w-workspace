#!/bin/sh
set -u
cd /root/essentials-src
echo "=== MapsState ==="; cat app/src/main/java/com/sameerasw/essentials/domain/MapsState.kt 2>/dev/null | head -60
echo; echo "=== MapsChannel ==="; cat app/src/main/java/com/sameerasw/essentials/domain/model/MapsChannel.kt 2>/dev/null | head -60
echo; echo "=== files referencing MapsState/power maps impl:"
grep -rl "MapsState\|MapsChannel\|MapsPowerSaving\|mapsPowerSaving\|maps_power" app/src --include='*.kt' 2>/dev/null | head -20
