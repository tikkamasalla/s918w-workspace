#!/bin/sh
set -u
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
KDIR=/root/s918-src/kernel_platform/msm-kernel
printf 'ccflags-y += -I%s/security/selinux/include -I%s/out-dm3q/security/selinux -I%s/kernel\nCFLAGS_gate.o := -fno-lto\nobj-m := gate.o\n' "$KDIR" "$KDIR" "$KDIR" > /root/gate/Makefile
printf '#include <linux/module.h>\nMODULE_LICENSE("GPL");\n' >> /root/gate/gate.c
rm -f /root/gate/gate.o /root/gate/gate.ko
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  -j8 M=/root/gate modules > /tmp/gate.log 2>&1
echo "gate rc=$?"
rm -f "$KDIR/out-dm3q/kernel/workqueue.o"
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  CFLAGS_workqueue.o="-fno-lto" -j8 kernel/workqueue.o > /tmp/wq2.log 2>&1
echo "wq rc=$?"
file /root/gate/gate.o "$KDIR/out-dm3q/kernel/workqueue.o"
pahole -C task_struct /root/gate/gate.o 2>&1 | head -6
