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
    # booleans controlling j(Z): who calls j with const/4 v, 0x1?
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
            if 'Lrdu;->j(Z)V' in out:
                users.add((m.get_class_name(), m.get_name(),
                           m.get_descriptor()))
                break
    print('Lrdu.j(Z) callers:', len(users))
    for c, n_, p in sorted(users)[:20]:
        print(f'  {c} -> {n_} {p}')
    # readers of Lahiw booleans beyond nz printer: who calls c()/b()/a() on Lahio?
    print('===== callers of Lahio.a/b/c =====')
    users2 = set()
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
            code = m.get_code()
            if code is None:
                continue
            for ins in code.get_bc().get_instructions():
                out = ins.get_output()
                if 'Lahio;->a(' in out or 'Lahio;->b(' in out or 'Lahio;->c(' in out:
                    users2.add((m.get_class_name(), m.get_name()))
                    break
        except Exception:
            continue
    print('Lahio users:', len(users2))
    for c, n_ in sorted(users2)[:20]:
        print(f'  {c} -> {n_}')
finally:
    os.unlink(tmp)
