#!/bin/sh
set -u
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:$PATH"
pip3 install -q --break-system-packages pyelftools 2>&1 | tail -1
KO=/root/KernelSU-dm3q/kernel/kernelsu.ko
VMLINUX=/mnt/e/s918w-port/kernel/vmlinux.elf
TOOLS=/mnt/e/s918w-port/Root-My-Galaxy-Payloads/kernelsu/tools
echo "--- locate check_symbol:"
ls /root/KernelSU-dm3q/kernel/ | grep -iE 'check|symbol' | head
find /root/KernelSU-dm3q -maxdepth 2 -name 'check_symbol*' 2>/dev/null | head
echo "--- modinfo:"
modinfo "$KO" | grep -E '^(vermagic|name|version)'
echo "--- symvers:"
python3 "$TOOLS/extract_target_symvers.py" "$VMLINUX" /tmp/dm3q-symvers.txt 2>&1 | tail -3
wc -l /tmp/dm3q-symvers.txt 2>/dev/null
