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
    for cl in dx.get_classes():
        try:
            cname = cl.get_vm_class().get_name()
        except Exception:
            continue
        if 'CompassButtonView' not in cname:
            continue
        for mm in cl.get_methods():
            inner = mm.get_method()
            if inner.get_name() != 'setIsCompassNeedleOnly':
                continue
            code = inner.get_code()
            print('insns:', len(list(code.get_bc().get_instructions())))
            for ins in code.get_bc().get_instructions():
                print('  ', ins.get_name(), '|', ins.get_output()[:140])
            break
        break
finally:
    os.unlink(tmp)
