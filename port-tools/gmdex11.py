import re
import zipfile
import glob as g

TAGS = [
    'speedometerSettingEnabled', 'speedLimitSettingEnabled',
    'SpeedometerEligible', 'speedometer_enabled',
    'speed_limits_enabled', 'speed_limits_ever_shown',
    'CompassInNavigation', 'compass_overview_preferred',
]

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
for n in z.namelist():
    if not n.endswith('.dex'):
        continue
    d = z.read(n)
    for tag in TAGS:
        needle = b'L' + tag.encode() + b';'
        count = d.count(needle)
        if count:
            print(n, '| FIELD', tag, 'x', count)
