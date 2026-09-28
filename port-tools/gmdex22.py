import zipfile
import glob as g
import logging
logging.disable(logging.CRITICAL)
from androguard.misc import AnalyzeDex

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
h, d, dx = AnalyzeDex(z.read('classes5.dex'))
print('methods:', len(dx.get_methods()))
targets = ('allowShowSpeedLimitAndWatermark',
           'speedLimitSettingEnabled', 'speedometerSettingEnabled',
           'isSpeedometerEligible')
users = set()
for m in dx.get_methods():
    try:
        _, invs, _ = dx.get_xref_from(m.get_method_idx() if hasattr(m, 'get_method_idx') else None) if False else (None, [], None)
    except Exception:
        pass
for m in dx.get_methods():
    try:
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
