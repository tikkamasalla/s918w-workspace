#!/bin/sh
set -u
cd /root
ls ndk-r28c-linux.zip
unzip -q -o ndk-r28c-linux.zip -d ndk 2>&1 | tail -1
NDK=/root/ndk/android-ndk-r28c
ls "$NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android35-clang" 2>/dev/null \
  || ls "$NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/" | grep -m3 'android35-clang'
echo "--- patch prep ---"
apt-get install -y -q dos2unix 2>&1 | tail -1
rm -rf KernelSU-dm3q && cp -r KernelSU-3.2.5 KernelSU-dm3q
mkdir -p /root/patches
cp /mnt/e/s918w-port/Root-My-Galaxy-Payloads/kernelsu/patches/KernelSU-v3.2.5-samsung-kdp-rkp-defex.patch /root/patches/
cp /mnt/e/s918w-port/kernelsu-src/KernelSU-v3.2.5-dm3q-5.15.148.patch /root/patches/
dos2unix /root/patches/*.patch
cd /root/KernelSU-dm3q
git init -q 2>/dev/null; git add -A 2>/dev/null; git -c user.email=t@t -c user.name=t commit -qm base 2>/dev/null
git apply --check /root/patches/KernelSU-v3.2.5-samsung-kdp-rkp-defex.patch \
  && echo SAMSUNG-PATCH-CHECK-OK
