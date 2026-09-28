import re
import zipfile
import glob as g

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
print('src MB:', round(__import__('os').path.getsize(src) / 1e6, 1))
z = zipfile.ZipFile(src)
dexes = [n for n in z.namelist() if n.endswith('.dex')]
print(len(dexes), 'dex files')
counts = {}
for n in dexes:
    d = z.read(n)
    low = d.lower()
    for pat in (b'speedometer', b'compass', b'speedlimit'):
        counts[pat.decode()] = counts.get(pat.decode(), 0) + low.count(pat)
print('counts:', counts)
