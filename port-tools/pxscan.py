import re
import zipfile

z = zipfile.ZipFile(r'E:\phone-pending\PixelifySpoofing-vv7.0.zip')
d = z.read('service.sh').decode('utf-8', 'replace')
print('service.sh len:', len(d))
urls = set(re.findall(r'https?://[^\s"\\]+', d))
for m in sorted(urls):
    print('URL:', m[:130])
print('---- download lines ----')
for i, line in enumerate(d.splitlines()):
    low = line.lower()
    if 'curl' in low or 'wget' in low or 'download' in low or '.zip' in low:
        print(i, line.strip()[:115])
