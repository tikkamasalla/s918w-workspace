#!/bin/sh
set -u
cp /root/KernelSU-dm3q/kernel/kernelsu.ko \
   /root/KernelSU-dm3q/userspace/ksud/bin/aarch64/android13-5.15_kernelsu.ko
ls -la /root/KernelSU-dm3q/userspace/ksud/bin/aarch64/
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o /tmp/rustup.sh
sh /tmp/rustup.sh -y --profile minimal 2>&1 | tail -2
export PATH="$HOME/.cargo/bin:$PATH"
rustup target add aarch64-linux-android 2>&1 | tail -1
rustc --version; cargo --version
