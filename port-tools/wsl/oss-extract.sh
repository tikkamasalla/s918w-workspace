#!/bin/sh
set -u
cd /mnt/e/s918w-port/oss
ls -la
python3 -c "import zipfile; z=zipfile.ZipFile('SM-S918B_16_Opensource.zip'); z.extractall('/root/s918-drop')"
ls -la /root/s918-drop/
cat /root/s918-drop/README_Kernel.txt 2>/dev/null | head -30
