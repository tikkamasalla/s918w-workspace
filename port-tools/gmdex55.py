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
    # who calls Lrdt.pu() / pw(Z)? -> the visibility decision chain
    users = set()
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
            code = m.get_code()
            if code is None:
                continue
            for ins in code.get_bc().get_instructions():
                out = ins.get_output()
                if 'Lrdt;->pu(' in out or 'Lrdt;->pw(' in out:
                    users.add((m.get_class_name(), m.get_name(),
                               m.get_descriptor()))
                    break
        except Exception:
            continue
    print('pu/pw callers:', len(users))
    for c, n_, p in sorted(users)[:20]:
        print(f'  {c} -> {n_} {p}')
    # Lavmi C(F)/D(I)/E(I,Lciyz): renderer callbacks for the speed overlay?
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        if m.get_class_name() == 'Lavmi;' and m.get_name() in ('C', 'D', 'E'):
            code = m.get_code()
            print('=====', 'Lavmi.' + m.get_name(), m.get_descriptor())
            for ins in code.get_bc().get_instructions():
                print('  ', ins.get_name(), '|', ins.get_output()[:150])
finally:
    os.unlink(tmp)
