#!/bin/sh
set -u
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
llvm-readelf -S /root/gate/gate-dwarf.o | grep -iE 'debug|BTF' | head
echo "--- try pahole verbose:"
pahole -C task_struct --show_dwarf_layout /root/gate/gate-dwarf.o 2>&1 | head -8
