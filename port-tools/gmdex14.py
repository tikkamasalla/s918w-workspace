import re
import zipfile
import glob as g

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
blob = {n: z.read(n) for n in z.namelist() if n.endswith('.dex')}
print('dexes:', len(blob))

KEYS = [b'CompassButtonView', b'setIsCompassNeedleOnly',
        b'speedometer', b'speedLimit', b'compass']
locs = {}
for n, d in blob.items():
    for k in KEYS:
        i = 0
        while True:
            i = d.find(k, i)
            if i < 0:
                break
            locs.setdefault(k.decode(), []).append((n, i))
            i += 1
for k, v in locs.items():
    print(k, '->', len(v), 'hits in', sorted({n for n, _ in v}))

COMPASS_CLS = b'Lcom/google/android/libraries/geo/mapcore/internal/ui/CompassButtonView;'
for n, d in blob.items():
    i = d.find(COMPASS_CLS)
    if i >= 0:
        print('class CompassButtonView in', n, 'at', hex(i))
        # look for setIsCompassNeedleOnly nearby (+/- 64KB)
        j = d.find(b'setIsCompassNeedleOnly')
        print('  setIsCompassNeedleOnly at', hex(j) if j >= 0 else 'ABSENT')
