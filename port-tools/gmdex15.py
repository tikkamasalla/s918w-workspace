import zipfile
import glob as g
from androguard.core.dex import DEX

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
for n in ['classes2.dex', 'classes5.dex']:
    dx = DEX(z.read(n))
    print('=====', n)
    for m in dx.get_methods():
        name = m.get_name()
        ln = name.lower()
        if 'speedometer' in ln or 'speedlimit' in ln:
            proto = m.get_descriptor()
            cls = m.get_class_name()
            code = m.get_code()
            nins = code.get_length() if code else 0
            print(f'{cls} -> {name} {proto} insns={nins}')
