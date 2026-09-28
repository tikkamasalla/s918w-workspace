import zipfile
import glob as g
import logging
logging.disable(logging.CRITICAL)
from androguard.core.dex import DEX

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
for n in ['classes2.dex', 'classes5.dex']:
    dx = DEX(z.read(n))
    print('=====', n)
    strs = [s.get_value() if hasattr(s, 'get_value') else str(s)
            for s in dx.get_strings()]
    hits = [s for s in strs
            if 'peedometer' in s or 'peedLimit' in s or 'peedlimit' in s]
    print('string hits:', len(hits))
    for h in sorted(set(hits))[:40]:
        print('  ', h)
