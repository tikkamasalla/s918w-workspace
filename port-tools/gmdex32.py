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
    f.write(z.read('classes2.dex'))
    tmp = f.name
try:
    h, d, dx = AnalyzeDex(tmp)
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
        except Exception:
            continue
        if m.get_class_name() == 'Lrdu;' and m.get_name() == 'k':
            break
    else:
        print('Lrdu.k not in classes2')
    # search all classes2 methods for callers of Lrdu.k / Lahiw.b(Z)
    users = set()
    for ma in dx.get_methods():
        try:
            m = ma.get_method()
            code = m.get_code()
            if code is None:
                continue
            for ins in code.get_bc().get_instructions():
                out = ins.get_output()
                if 'Lrdu;->k(' in out or 'Lahiw;->b(' in out:
                    users.add((m.get_class_name(), m.get_name()))
                    break
        except Exception:
            continue
    print('callers in classes2:', len(users))
    for c, n_ in sorted(users)[:30]:
        print(f'{c} -> {n_}')
finally:
    os.unlink(tmp)
