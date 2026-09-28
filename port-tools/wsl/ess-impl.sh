#!/bin/sh
set -u
cd /root/essentials-src
echo "=== TileService:"; cat app/src/main/java/com/sameerasw/essentials/services/tiles/MapsPowerSavingTileService.kt 2>/dev/null | head -80
echo; echo "=== BatteryViewModel maps fns:"
grep -n -i "maps\|brightness\|screen_off\|goToSleep\|dreams\|doze" app/src/main/java/com/sameerasw/essentials/viewmodels/BatteryViewModel.kt | head -30
