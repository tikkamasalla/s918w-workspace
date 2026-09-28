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
    # Lbfpl: fields (incl. the boolean), methods A(Z)/B(Z)/C(F)
    for cl in dx.get_classes():
        try:
            cname = cl.get_vm_class().get_name()
        except Exception:
            continue
        if cname != 'Lbfpl;':
            continue
        print('FIELDS of Lbfpl:')
        try:
            for fl in cl.get_fields():
                fvm = fl.get_field() if hasattr(fl, 'get_field') else fl
                print('  ', fvm.get_name(), fvm.get_descriptor()
                      if hasattr(fvm, 'get_descriptor') else '')
        except Exception as e:
            print('  ERR', e)
        print('METHODS of Lbfpl:')
        for mm in cl.get_methods():
            inner = mm.get_method()
            print('  ', inner.get_name(), inner.get_descriptor())
        break
finally:
    os.unlink(tmp)
