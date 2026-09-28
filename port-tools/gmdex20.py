import zipfile
import glob as g
import logging
logging.disable(logging.CRITICAL)
from androguard.core.dex import DEX

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
dx = DEX(z.read('classes5.dex'))

targets = {
    'allowShowSpeedLimitAndWatermark',
    'speedLimitSettingEnabled: ',
    'speedometerSettingEnabled: ',
    'isSpeedometerEligible: ',
}
sidx = {}
for i, s in enumerate(dx.get_strings()):
    v = s.get_value() if hasattr(s, 'get_value') else str(s)
    if v in targets:
        sidx[v] = i
print('string idx:', sidx)

found = []
for m in dx.get_methods():
    try:
        code = m.get_code()
        if code is None:
            continue
        for ins in code.get_bc().get_instructions():
            try:
                refs = ins.get_ref_kind()
            except Exception:
                refs = ''
            if 'string' not in str(refs).lower():
                continue
            try:
                out = ins.get_output()
            except Exception:
                continue
            for t in targets:
                if t in out:
                    found.append((m.get_class_name(), m.get_name(),
                                  m.get_descriptor(), t))
                    break
    except Exception:
        continue
print('users:', len(found))
for c, n_, p, t in sorted(set(found))[:40]:
    print(f'{c} -> {n_} {p}  [{t[:30]}]')
