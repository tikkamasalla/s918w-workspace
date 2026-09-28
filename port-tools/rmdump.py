import zipfile

z = zipfile.ZipFile(r'E:\phone-pending\Re-Malwack_v8.2.zip')
for n in ['action.sh', 'customize.sh', 'import.sh', 'service.sh']:
    print('=' * 25, n)
    print(z.read(n).decode('utf-8', 'replace')[:2200])
