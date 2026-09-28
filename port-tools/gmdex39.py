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
    # 1. who calls Lahiw.b(Z)? -> the real eligibility/settings writers
    users = set()
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
            code = m.get_code()
            if code is None:
                continue
            for ins in code.get_bc().get_instructions():
                out = ins.get_output()
                if 'Lahiw;->b(' in out:
                    users.add((m.get_class_name(), m.get_name(),
                               m.get_descriptor()))
                    break
        except Exception:
            continue
    print('callers of Lahiw.b(Z):', len(users))
    for c, n_, p in sorted(users)[:30]:
        print(f'  {c} -> {n_} {p}')
    # 2. readers of Lahiw fields n/o/p (settings + eligibility)
    print('===== readers of Lahiw.{n,o,p} =====')
    readers = set()
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
            code = m.get_code()
            if code is None:
                continue
            for ins in code.get_bc().get_instructions():
                out = ins.get_output()
                if ('Lahiw;->n Z' in out or 'Lahiw;->o Z' in out
                        or 'Lahiw;->p Z' in out):
                    readers.add((m.get_class_name(), m.get_name(),
                                 m.get_descriptor()))
                    break
        except Exception:
            continue
    print('readers:', len(readers))
    for c, n_, p in sorted(readers)[:40]:
        print(f'  {c} -> {n_} {p}')
finally:
    os.unlink(tmp)
