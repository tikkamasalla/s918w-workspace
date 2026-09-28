import zipfile
z = zipfile.ZipFile(r'E:\debakarr-patches\patches\build\libs\patches-1.1.2.mpp')
for n in z.namelist():
    try:
        d = z.read(n)
    except Exception:
        continue
    if b'alf-customer-ratings' in d:
        print('CSA ANCHOR IN:', n[:80])
print('scan done')
