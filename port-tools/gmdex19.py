import zipfile
import glob as g
import logging
logging.disable(logging.CRITICAL)
from androguard.core.dex import DEX

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
dx = DEX(z.read('classes5.dex'))
strs = dx.get_strings()
print('n strings:', len(list(strs)))
vals = [s.get_value() if hasattr(s, 'get_value') else str(s) for s in dx.get_strings()]
print('has allowShow:', 'allowShowSpeedLimitAndWatermark' in vals)
print('has speedLimitSettingEnabled:', 'speedLimitSettingEnabled: ' in vals)
ms = dx.get_methods()
print('n methods:', len(list(ms)))
cnt = 0
for m in dx.get_methods():
    cnt += 1
    if cnt > 5:
        break
    print('sample:', m.get_class_name(), m.get_name())
