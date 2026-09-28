#!/bin/sh
set -u
python3 -c "import zipfile; z=zipfile.ZipFile('/tmp/lsposed.bin'); n=z.namelist(); print(len(n), 'entries'); [print(' ', x) for x in n if len(x.split('/'))<=2][:30]"
cp /tmp/lsposed.bin /mnt/e/s918w-port/LSPosed-v2.2.0-7854-release.zip
ls -la /mnt/e/s918w-port/LSPosed-v2.2.0-7854-release.zip
