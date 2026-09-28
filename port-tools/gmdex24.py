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
    methods = list(dx.get_methods())
    probe = None
    for m in methods:
        if hasattr(m, 'get_method'):
            probe = m.get_method()
            break
    print('probe:', probe.get_class_name(), probe.get_name())
    code = probe.get_code()
    print('code type:', type(code))
    bc = code.get_bc()
    insns = list(bc.get_instructions())
    print('n insns:', len(insns))
    print('first insn methods:', [x for x in dir(insns[0]) if 'out' in x.lower() or 'ref' in x.lower() or 'kind' in x.lower()])
    print('sample output:', repr(insns[0].get_output())[:200])
finally:
    os.unlink(tmp)
