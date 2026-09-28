#!/bin/sh
set -u
cd /root/essentials-src
grep -rn "hasNavigationNotification\|MapsState.isEnabled\|maps_power_saving_enabled\|KEY_MAPS_POWER_SAVING" app/src --include='*.kt' | grep -v "MapsState.kt\|MapsPowerSavingSettingsUI\|MapsPowerSavingTileService\|BatteryViewModel\|SettingsRepository.kt" | head -20
