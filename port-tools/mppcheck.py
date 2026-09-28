import zipfile
z = zipfile.ZipFile(r'E:\debakarr-patches\patches\build\libs\patches-1.1.2.mpp')
for n in z.namelist():
    try:
        d = z.read(n)
    except Exception:
        continue
    if b'flexDirection' in d:
        print('FLEXFIX IN:', n[:80])
    if b'morphe-dbg' in d:
        print('DIAG STILL IN:', n[:80])
print('scan done')
