import zipfile, glob as g
src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
print('src ok')
z = zipfile.ZipFile(src)
dex_names = [n for n in z.namelist() if n.endswith('.dex')]
print('dexes:', len(dex_names))
from androguard.core.dex import DEX
all_methods = set()
for n in dex_names:
    data = z.read(n)
    print('parse', n, len(data))
    dx = DEX(data)
    methods = dx.get_methods()
    print('  methods:', len(methods))
    for m in methods:
        name = m.get_name()
        ln = name.lower()
        if 'speedometer' in ln or 'speedlimit' in ln or 'speed_limit' in ln or ('compass' in ln and len(name) > 3):
            all_methods.add((m.get_class_name(), name, m.get_descriptor()))
print('TOTAL HITS:', len(all_methods))
for cls, name, proto in sorted(all_methods)[:250]:
    print(f'{cls} -> {name} {proto}')
