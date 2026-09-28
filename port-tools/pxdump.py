import zipfile

z = zipfile.ZipFile(r'E:\phone-pending\PixelifySpoofing-vv7.0.zip')
print(z.read('service.sh').decode('utf-8', 'replace'))
print('########## microhooks head ##########')
m = z.read('patch_microhooks.sh').decode('utf-8', 'replace')
print(m[:1800])
