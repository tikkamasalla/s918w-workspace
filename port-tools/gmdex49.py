import tempfile
import zipfile
import glob as g
import logging
import os
logging.disable(logging.CRITICAL)
from androguard.misc import AnalyzeDex

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
for dn in ['classes.dex', 'classes2.dex', 'classes5.dex', 'classes6.dex']:
    with tempfile.NamedTemporaryFile(suffix='.dex', delete=False) as f:
        f.write(z.read(dn))
        tmp = f.name
    try:
        h, d, dx = AnalyzeDex(tmp)
        for ma in dx.get_methods():
            try:
                m = ma.get_method()
            except Exception:
                continue
            if m.get_class_name() == 'Lbfpl;' and m.get_name() == 'bQ':
                try:
                    code = m.get_code()
                    insns = list(code.get_bc().get_instructions())
                    print(dn, 'bQ DEFINED, insns:', len(insns))
                    for ins in insns:
                        print('  ', ins.get_name(), '|',
                              ins.get_output()[:170])
                except AttributeError:
                    print(dn, 'bQ external (defined elsewhere)')
                break
        else:
            print(dn, 'no bQ ref')
    finally:
        os.unlink(tmp)
