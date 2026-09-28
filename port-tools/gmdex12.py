import glob as g
import zipfile

src = g.glob(r'C:\Users\Aows\Downloads\*maps_26.36*')[0]
print('src:', src)
try:
    from androguard.misc import AnalyzeAPK
    a, d, dx = AnalyzeAPK(src)
    print('dex objects:', len(d))
    keys = ['speedometer', 'speedlimit', 'compass']
    found = []
    for dex in d:
        for m in dex.get_methods():
            name = m.get_name().lower()
            if any(k in name for k in keys):
                cls = m.get_class_name()
                proto = m.get_proto()
                found.append((cls, m.get_name(), proto))
                if len(found) < 200:
                    pass
    print('total hits:', len(found))
    for cls, name, proto in sorted(set(found))[:120]:
        print(f'{cls} -> {name} {proto}')
except Exception as e:
    import traceback
    traceback.print_exc()
    print('ERR', e)
