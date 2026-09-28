import tempfile
import zipfile
import glob as g
import logging
import os
logging.disable(logging.CRITICAL)
from androguard.misc import AnalyzeDex

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
with tempfile.NamedTemporaryFile(suffix='.dex', delete=False) as f:
    f.write(z.read('classes5.dex'))
    tmp = f.name
try:
    h, d, dx = AnalyzeDex(tmp)
    targets = ('allowShowSpeedLimitAndWatermark',
               'speedLimitSettingEnabled', 'speedometerSettingEnabled',
               'isSpeedometerEligible')
    users = set()
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
            code = m.get_code()
            if code is None:
                continue
            for ins in code.get_bc().get_instructions():
                out = ins.get_output()
                for t in targets:
                    if t in out:
                        users.add((m.get_class_name(), m.get_name(), t))
                        break
        except Exception:
            continue
    print('users:', len(users))
    for c, n_, t in sorted(users)[:40]:
        print(f'{c} -> {n_}  [{t[:34]}]')
finally:
    os.unlink(tmp)
