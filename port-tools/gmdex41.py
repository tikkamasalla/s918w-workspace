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
    # who instantiates Lavmi, and who calls its A(Z)/B(Z)?
    makers = set()
    callers = set()
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
            code = m.get_code()
            if code is None:
                continue
            for ins in code.get_bc().get_instructions():
                out = ins.get_output()
                if 'Lavmi;-><init>' in out:
                    makers.add((m.get_class_name(), m.get_name()))
                if 'Lavmi;->A(' in out or 'Lavmi;->B(' in out:
                    callers.add((m.get_class_name(), m.get_name(),
                                 'A' if 'Lavmi;->A(' in out else 'B'))
                if len(makers) > 20 and len(callers) > 20:
                    break
        except Exception:
            continue
    print('Lavmi makers:', len(makers))
    for c, n_ in sorted(makers)[:15]:
        print(f'  {c} -> {n_}')
    print('A/B callers:', len(callers))
    for c, n_, w in sorted(callers)[:25]:
        print(f'  {c} -> {n_}  [{w}]')
finally:
    os.unlink(tmp)
