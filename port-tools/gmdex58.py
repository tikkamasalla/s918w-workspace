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
    f.write(z.read('classes6.dex'))
    tmp = f.name
try:
    h, d, dx = AnalyzeDex(tmp)
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        if m.get_class_name() == 'Lahiv;' and m.get_name() == 'f':
            code = m.get_code()
            insns = list(code.get_bc().get_instructions())
            print('total insns:', len(insns))
            for ins in insns[35:]:
                print('  ', ins.get_name(), '|', ins.get_output()[:170])
            break
finally:
    os.unlink(tmp)
