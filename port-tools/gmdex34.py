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
    # find the CompassButtonView class object, list methods incl setters
    for cl in dx.get_classes():
        try:
            vm = cl.get_vm_class()
            cname = vm.get_name()
        except Exception:
            continue
        if 'CompassButtonView' in cname:
            print('CLASS:', cname)
            try:
                methods = list(cl.get_methods())
            except Exception:
                methods = []
            print('n methods:', len(methods))
            for mm in methods:
                try:
                    inner = mm.get_method()
                    print('  ', inner.get_name(), inner.get_descriptor())
                except Exception as e:
                    print('  ERR', e)
            break
finally:
    os.unlink(tmp)
