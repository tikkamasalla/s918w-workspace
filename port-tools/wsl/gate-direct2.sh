#!/bin/sh
set -u
grep -v MODULE_LICENSE /root/gate/gate.c > /root/gate/gate2.c
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
KDIR=/root/s918-src/kernel_platform/msm-kernel
OUT=$KDIR/out-dm3q
clang --target=aarch64-linux-gnu -nostdinc -D__KERNEL__ \
  -I$KDIR/arch/arm64/include \
  -I$OUT/arch/arm64/include/generated \
  -I$KDIR/include \
  -I$OUT/include \
  -I$KDIR/security/selinux/include \
  -I$OUT/security/selinux \
  -I$KDIR/kernel \
  -I$KDIR/arch/arm64/include/uapi \
  -I$OUT/arch/arm64/include/generated/uapi \
  -I$KDIR/include/uapi \
  -I$OUT/include/generated/uapi \
  -include $KDIR/include/linux/kconfig.h \
  -include $OUT/include/generated/autoconf.h \
  -g -O0 -fno-lto -c /root/gate/gate2.c -o /root/gate/gate-dwarf.o 2>&1 | grep -m5 -i error
echo "compile done rc=$?"
file /root/gate/gate-dwarf.o 2>/dev/null
pahole -C task_struct /root/gate/gate-dwarf.o 2>&1 | head -8
