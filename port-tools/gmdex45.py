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
    # who calls Lbfpl.<init>(Z) with const/4 vX, 0x1?
    users = set()
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
            code = m.get_code()
            if code is None:
                continue
            insns = list(code.get_bc().get_instructions())
        except Exception:
            continue
        for i, ins in enumerate(insns):
            try:
                out = ins.get_output()
            except Exception:
                continue
            if 'Lbfpl;-><init>(Z)V' in out:
                users.add((m.get_class_name(), m.get_name(),
                           m.get_descriptor()))
                break
    print('Lbfpl.<init>(Z) callers:', len(users))
    for c, n_, p in sorted(users)[:20]:
        print(f'  {c} -> {n_} {p}')
finally:
    os.unlink(tmp)
