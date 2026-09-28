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
    hit = None
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        if m.get_class_name() == 'Lbfpl;' and m.get_name() == 'bQ' \
                and m.get_descriptor() == '(Z)V':
            hit = m
            break
    if hit is None:
        print('bQ not found')
    else:
        code = hit.get_code()
        insns = list(code.get_bc().get_instructions())
        print('insns:', len(insns))
        for ins in insns:
            print('  ', ins.get_name(), '|', ins.get_output()[:170])
finally:
    os.unlink(tmp)
