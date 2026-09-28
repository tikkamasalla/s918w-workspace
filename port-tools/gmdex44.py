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
    # 1. Lahio methods (renderer callbacks n/o touch)
    for cl in dx.get_classes():
        try:
            cname = cl.get_vm_class().get_name()
        except Exception:
            continue
        if cname != 'Lahio;':
            continue
        print('Lahio methods:')
        for mm in cl.get_methods():
            inner = mm.get_method()
            print('  ', inner.get_name(), inner.get_descriptor())
        break
    # 2. Lavmi init(Z): which boolean does the ctor arg set? and who calls it
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        if m.get_class_name() == 'Lavmi;' and m.get_name() == '<init>' \
                and m.get_descriptor() == '(Z)V':
            code = m.get_code()
            print('Lavmi.<init>(Z) body:')
            for ins in code.get_bc().get_instructions():
                print('  ', ins.get_name(), '|', ins.get_output()[:150])
            break
finally:
    os.unlink(tmp)
