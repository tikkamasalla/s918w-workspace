#!/bin/sh
set -u
cd /root
# Android clang r450784e (kernel's own toolchain, per /proc/version)
curl -sSL -o clang-r450784e.tar.gz \
  'https://android.googlesource.com/platform/prebuilts/clang/host/linux-x86/+archive/refs/heads/main/clang-r450784e.tar.gz' \
  && ls -la clang-r450784e.tar.gz && tar tzf clang-r450784e.tar.gz 2>/dev/null | head -3
echo "---KernelSU---"
git clone --depth 1 --branch v3.2.5 https://github.com/tiann/KernelSU.git KernelSU-3.2.5 2>&1 | tail -2
git -C KernelSU-3.2.5 rev-parse HEAD
