import zipfile
import glob as g
import logging
logging.disable(logging.CRITICAL)
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
            print(f'{m.get_class_name()} -> {name} {m.get_descriptor()}')
