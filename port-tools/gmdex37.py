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
    f.write(z.read('classes2.dex'))
    tmp = f.name
try:
    h, d, dx = AnalyzeDex(tmp)
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        cn = m.get_class_name()
        if cn not in ('Lamcr;', 'Lbkrr;'):
            continue
        try:
            code = m.get_code()
            if code is None:
                continue
            insns = list(code.get_bc().get_instructions())
        except Exception:
            continue
        hits = [i for i in insns if 'CompassButtonView' in i.get_output()
                or 'needle' in i.get_output().lower()
                or 'compass' in i.get_output().lower()]
        if hits:
            print('=====', cn, '->', m.get_name(), m.get_descriptor(),
                  f'({len(insns)} insns)')
            for ins in hits[:20]:
                print('  ', ins.get_name(), '|', ins.get_output()[:160])
finally:
    os.unlink(tmp)
