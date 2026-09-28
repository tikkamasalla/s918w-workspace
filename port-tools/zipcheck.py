import zipfile
z = zipfile.ZipFile(r'E:\morphe\amazon-32.13.2.100.apks')
names = z.namelist()
print('entries:', len(names))
for n in names[:12]:
    print('  ', n)
bad = z.testzip()
print('crc-bad:', bad)
