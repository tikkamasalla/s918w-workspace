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
        if m.get_class_name() == 'Lrdu;' and m.get_name() in ('l', 'm'):
            print('=====', m.get_name(), m.get_descriptor())
            code = m.get_code()
            for ins in code.get_bc().get_instructions():
                print('  ', ins.get_name(), '|', ins.get_output()[:130])
    # fields of Lahiw (state holder incl. n/o/p booleans)
    for c in dx.get_classes():
        try:
            name = c.get_vm_class().get_name()
        except Exception:
            continue
        if name == 'Lahiw;':
            print('===== fields of Lahiw')
            for fl in c.get_fields():
                print('  ', fl.get_name(), fl.get_descriptor() if hasattr(fl, 'get_descriptor') else '')
            break
finally:
    os.unlink(tmp)
