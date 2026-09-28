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
    # Lavmi details
    for cl in dx.get_classes():
        try:
            cname = cl.get_vm_class().get_name()
        except Exception:
            continue
        if cname != 'Lavmi;':
            continue
        print('Lavmi superclass + ifaces:')
        try:
            vm = cl.get_vm_class()
            print('  super:', vm.get_superclassname())
            print('  ifaces:', vm.get_interfaces())
        except Exception as e:
            print('  ERR', e)
        print('Lavmi methods:')
        for mm in cl.get_methods():
            inner = mm.get_method()
            print('  ', inner.get_name(), inner.get_descriptor())
        break
    # Lrdu field b type: which class holds j(Z) input?
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        if m.get_class_name() == 'Lrdu;' and m.get_name() == 'j':
            code = m.get_code()
            for ins in code.get_bc().get_instructions():
                out = ins.get_output()
                if 'Lppw;->D(' in out or 'Lppo' in out or 'Lppq' in out or 'Lppu' in out:
                    print('j-gate:', ins.get_name(), '|', out[:150])
            break
finally:
    os.unlink(tmp)
