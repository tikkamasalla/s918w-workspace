import tempfile
import zipfile
import glob as g
import logging
import os
logging.disable(logging.CRITICAL)
from androguard.misc import AnalyzeDex

COMPASS = 'Lcom/google/android/libraries/geo/mapcore/internal/ui/CompassButtonView;'

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
for dn in ['classes.dex', 'classes2.dex', 'classes5.dex']:
    with tempfile.NamedTemporaryFile(suffix='.dex', delete=False) as f:
        f.write(z.read(dn))
        tmp = f.name
    try:
        h, d, dx = AnalyzeDex(tmp)
        users = set()
        for ma in dx.get_methods():
            try:
                m = ma.get_method()
                code = m.get_code()
                if code is None:
                    continue
                for ins in code.get_bc().get_instructions():
                    out = ins.get_output()
                    if 'CompassButtonView' in out and 'setIsCompassNeedleOnly' not in out:
                        users.add((m.get_class_name(), m.get_name()))
                        break
            except Exception:
                continue
        print(dn, 'refs to CompassButtonView:', len(users))
        for c, n_ in sorted(users)[:25]:
            print(f'  {c} -> {n_}')
    finally:
        os.unlink(tmp)
