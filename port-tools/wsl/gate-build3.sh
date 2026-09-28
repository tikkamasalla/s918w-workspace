#!/bin/sh
set -u
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
KDIR=/root/s918-src/kernel_platform/msm-kernel
OUT=$KDIR/out-dm3q
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  scripts/selinux/genheaders/genheaders > /tmp/gh.log 2>&1
echo "genheaders build rc=$?"
mkdir -p "$OUT/security/selinux"
"$OUT/scripts/selinux/genheaders/genheaders" \
  "$OUT/security/selinux/flask.h" \
  "$OUT/security/selinux/av_permissions.h" && echo GENHEADERS-OK
ls -la "$OUT/security/selinux/"
printf 'ccflags-y += -I/root/s918-src/kernel_platform/msm-kernel/security/selinux/include -I/root/s918-src/kernel_platform/msm-kernel/out-dm3q/security/selinux\nobj-m := gate.o\n' > /root/gate/Makefile
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  -j8 M=/root/gate modules > /tmp/gate.log 2>&1
echo "gate rc=$?"
ls -la /root/gate/
