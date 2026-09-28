import re

pkgs = set()
for ln in open(r'E:\s918w-port\pkglist.txt', encoding='utf-8',
               errors='replace'):
    m = re.match(r'package:(.*\.apk)=(.*)', ln)
    if m:
        pkgs.add(m.group(2))

mods = [
    'io.github.soclear.oneuix', 'io.github.tehcneko.undo',
    'com.kieronquinn.app.darq', 'eu.hxreborn.amznkiller',
    'eu.hxreborn.gplayadblock', 'eu.hxreborn.phdp',
    'ru.mike.updatelocker', 'com.wmods.wppenhacer',
    'ru.mike.mapstweaks', 'io.github.chsbuffer.revancedxposed',
    'com.waenhancer', 'io.github.fzer0x.fuckmeta',
    'com.parallelc.micts',
    'de.binarynoise.betterBluetoothDeviceSort',
    'de.binarynoise.openWifiOnTop',
    'io.github.lsposed.disableflagsecure',
    'moe.lyniko.hiderecent',
    'com.tikkamasalla.powersavespoof',
]
print('=== installed? ===')
for m in mods:
    print(('OK  ' if m in pkgs else 'GONE'), m)

scopes = ['com.samsung.android.da.daagent',
          'com.samsung.android.incallui', 'com.sec.android.app.camera',
          'system', 'com.sec.android.daemonapp',
          'com.sec.android.app.launcher',
          'com.sec.android.mimage.photoretouching',
          'com.samsung.android.app.watchmanager',
          'com.samsung.android.dialer', 'com.android.settings',
          'com.samsung.android.themecenter',
          'com.samsung.android.app.telephonyui',
          'com.samsung.android.mdecservice', 'com.samsung.android.video',
          'com.samsung.android.service.airviewdictionary',
          'com.samsung.android.messaging', 'com.sec.android.gallery3d',
          'com.android.systemui', 'com.android.vending',
          'com.sec.android.app.samsungapps',
          'com.amazon.mShop.android.shopping',
          'com.google.android.apps.maps',
          'com.alltrails.alltrails', 'com.whatsapp',
          'com.google.android.googlequicksearchbox',
          'com.android.bluetooth']
print('=== scope targets installed? ===')
for s in sorted(set(scopes)):
    if s == 'system':
        continue
    print(('OK  ' if s in pkgs else 'GONE'), s)
