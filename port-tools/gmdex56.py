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
    # Lahiv.f() / c() bodies: what feeds the show decision?
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        if m.get_class_name() == 'Lahiv;' and m.get_name() in ('f', 'c'):
            print('=====', 'Lahiv.' + m.get_name(), m.get_descriptor())
            code = m.get_code()
            for ins in code.get_bc().get_instructions():
                print('  ', ins.get_name(), '|', ins.get_output()[:180])
finally:
    os.unlink(tmp)
