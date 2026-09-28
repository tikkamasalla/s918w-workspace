import re
import zipfile
import glob as g

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
pats = [p.encode() for p in (
    'speedometerSettingEnabled', 'speedometer_enabled',
    'speedLimitSettingEnabled', 'speed_limits_enabled',
    'speed_limits_ever_shown', 'SpeedometerEligible',
    'CompassInNavigation', 'compass_overview_preferred',
    'speedLimitAndWatermarkMode',
)]
for n in z.namelist():
    if not n.endswith('.dex'):
        continue
    d = z.read(n)
    hits = set()
    for pat in pats:
        for m in re.finditer(re.escape(pat) + rb'.{0,120}', d):
            try:
                seg = m.group(0).decode('ascii', 'replace')
                seg = ''.join(c if 32 <= ord(c) < 127 or c in '\n' else ' ' for c in seg)
                hits.add(seg[:110])
            except Exception:
                pass
    if hits:
        print('=====', n)
        for h in sorted(hits)[:25]:
            print('  ', repr(h))
