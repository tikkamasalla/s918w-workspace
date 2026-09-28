#!/bin/sh
set -u
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
KO=/root/KernelSU-dm3q/kernel/kernelsu.ko
VMLINUX=/mnt/e/s918w-port/kernel/vmlinux.elf
TOOLS=/mnt/e/s918w-port/Root-My-Galaxy-Payloads/kernelsu/tools
echo "=== check_symbol ==="
/root/KernelSU-dm3q/kernel/check_symbol "$KO" "$VMLINUX" 2>&1 | tail -8
echo "=== modinfo ==="
modinfo "$KO" | grep -E '^(vermagic|name|version)'
echo "=== strip debug, keep symtab ==="
llvm-strip -d "$KO"
ls -la "$KO"
readelf -SW "$KO" | grep -E '__versions|symtab|strtab' | head -6
echo "=== extract target symvers ==="
python3 "$TOOLS/extract_target_symvers.py" "$VMLINUX" /tmp/dm3q-symvers.txt 2>&1 | tail -3
wc -l /tmp/dm3q-symvers.txt 2>/dev/null
