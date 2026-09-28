import zipfile
import glob as g
import logging
logging.disable(logging.CRITICAL)
from androguard.core.dex import DEX

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
dx = DEX(z.read('classes5.dex'))

m0 = None
for m in dx.get_methods():
    m0 = m
    break
code = m0.get_code()
bc = code.get_bc()
insns = list(bc.get_instructions())
ins = insns[0]
print('methods on insn:', [x for x in dir(ins) if not x.startswith('_')][:40])
