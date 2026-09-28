#!/bin/sh
set -u
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
KDIR=/root/s918-src/kernel_platform/msm-kernel
printf 'ccflags-y += -I%s/security/selinux/include -I%s/out-dm3q/security/selinux -I%s/kernel\nCFLAGS_gate.o := -fno-lto -fno-sanitize=cfi\nobj-m := gate.o\n' "$KDIR" "$KDIR" "$KDIR" > /root/gate/Makefile
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  -j8 M=/root/gate modules > /tmp/gate.log 2>&1
echo "gate rc=$?"
file /root/gate/gate.o 2>/dev/null
pahole -C task_struct /root/gate/gate.o 2>&1 | head -8
