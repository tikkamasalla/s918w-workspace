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
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        if m.get_class_name() != 'Lrdt;':
            continue
        try:
            code = m.get_code()
            insns = list(code.get_bc().get_instructions()) if code else []
        except Exception:
            insns = []
        print(f'{m.get_name()} {m.get_descriptor()} insns={len(insns)}')
finally:
    os.unlink(tmp)
