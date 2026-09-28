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
    # booleans n/o/p inside Lahiw via raw field table
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        if m.get_class_name() == 'Lrdu;' and m.get_name() == 'k':
            code = m.get_code()
            src_txt = []
            for ins in code.get_bc().get_instructions():
                src_txt.append(ins.get_name() + ' | ' + ins.get_output()[:100])
            # find iput targets writing Lahiw booleans: theeligibility/settings writes
            print('\n'.join(src_txt[:60]))
            break
    # dump all field names containing relevant substrings
    print('===== FIELDS =====')
    seen = set()
    for cl in dx.get_classes():
        try:
            vm = cl.get_vm_class()
            cname = vm.get_name()
        except Exception:
            continue
        try:
            fields = cl.get_fields()
        except Exception:
            continue
        for fl in fields:
            try:
                fn = fl.get_name()
            except Exception:
                continue
            fl_ = fn.lower()
            if ('speed' in fl_ or 'compass' in fl_ or 'eligible' in fl_
                    or 'watermark' in fl_ or 'overlay' in fl_):
                seen.add((cname, fn))
    for c, fn in sorted(seen)[:60]:
        print(f'{c} . {fn}')
finally:
    os.unlink(tmp)
