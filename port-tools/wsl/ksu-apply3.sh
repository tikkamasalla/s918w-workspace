#!/bin/sh
set -u
cp /mnt/e/s918w-port/kernelsu-src/KernelSU-v3.2.5-dm3q-5.15.148.patch /root/patches/
dos2unix /root/patches/KernelSU-v3.2.5-dm3q-5.15.148.patch
cd /root/KernelSU-dm3q
git apply --check /root/patches/KernelSU-v3.2.5-dm3q-5.15.148.patch \
  && echo DM3Q-CHECK-OK \
  && git apply /root/patches/KernelSU-v3.2.5-dm3q-5.15.148.patch \
  && echo DM3Q-APPLIED \
  && sed -n '/void __init ksu_syscall_hook_init/,/^}/p' kernel/hook/arm64/syscall_hook.c
