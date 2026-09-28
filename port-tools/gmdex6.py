import re
import zipfile
import glob as g

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
z = zipfile.ZipFile(src)
hits = set()
for n in z.namelist():
    if not n.endswith('.dex'):
        continue
    d = z.read(n)
    for pat in (rb'speedometer', rb'Speedometer', rb'SPEEDOMETER',
                rb'compass', rb'Compass', rb'COMPASS'):
        for m in re.finditer(pat + rb'[A-Za-z0-9_$]{0,45}', d):
            try:
                hits.add(m.group(0).decode('ascii'))
            except Exception:
                pass
print(len(hits), 'distinct')
for h in sorted(hits):
    print('  ', h)
