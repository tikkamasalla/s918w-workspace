import re
import zipfile
import glob as g

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
d5 = z.read('classes5.dex')
for pat in (b'speedometerSettingEnabled', b'speedLimitSettingEnabled',
            b'speedLimitAndWatermarkMode', b'SpeedometerEligible',
            b'CompassInNavigation'):
    print('#####', pat.decode())
    idx = 0
    shown = 0
    while shown < 3:
        i = d5.find(pat, idx)
        if i < 0:
            break
        seg = d5[max(0, i - 700):i + 60]
        txt = ''.join(chr(b) if 32 <= b < 127 else '\n' for b in seg)
        print('---- occurrence ----')
        print(txt[-900:])
        idx = i + 1
        shown += 1
