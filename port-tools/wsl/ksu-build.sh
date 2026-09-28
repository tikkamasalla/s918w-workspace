#!/bin/sh
set -u
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
KDIR=/root/s918-src/kernel_platform/msm-kernel
OUT=$KDIR/out-dm3q
REL="5.15.148-android13-8-29539737-abS918WVLS6CYB3"
echo "$REL" > "$OUT/include/config/kernel.release"
printf '#define UTS_RELEASE "%s"\n' "$REL" > "$OUT/include/generated/utsrelease.h"
cat "$OUT/include/config/kernel.release"
grep UTS_RELEASE "$OUT/include/generated/utsrelease.h"
make -C "$OUT" M=/root/KernelSU-dm3q/kernel src=/root/KernelSU-dm3q/kernel \
  ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  CONFIG_KSU=m \
  CONFIG_KSU_SAMSUNG_KDP=y \
  CONFIG_KSU_SAMSUNG_RKP=y \
  CONFIG_KSU_SAMSUNG_DEFEX=y \
  CONFIG_KSU_SAMSUNG_NO_PATCH_TEXT=y \
  KCFLAGS=-DCONFIG_DEBUG_INFO_BTF_MODULES=1 \
  KBUILD_MODPOST_WARN=1 -j8 modules > /tmp/ksubuild.log 2>&1
echo "ksu build rc=$?"
tail -5 /tmp/ksubuild.log
ls -la /root/KernelSU-dm3q/kernel/*.ko 2>/dev/null
