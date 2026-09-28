#!/bin/sh
set -u
export DEBIAN_FRONTEND=noninteractive
apt-get install -y -q unzip 2>&1 | tail -1
cd /root
unzip -q -o ndk-r28c-linux.zip -d ndk
NDK=/root/ndk/android-ndk-r28c
"$NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/clang" --version | head -2
ls "$NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android35-clang"
echo "--- apply samsung patch ---"
cd /root/KernelSU-dm3q
git apply /root/patches/KernelSU-v3.2.5-samsung-kdp-rkp-defex.patch \
  && echo SAMSUNG-APPLIED
echo "--- check dm3q patch ---"
git apply --check /root/patches/KernelSU-v3.2.5-dm3q-5.15.148.patch \
  && echo DM3Q-CHECK-OK
