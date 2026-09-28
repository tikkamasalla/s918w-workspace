#!/bin/sh
set -u
ls /root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin/ | grep -E '^(aarch64-linux-android(33|21)-clang|llvm-ar|clang)' | head
echo "--- cargo full error:"
export PATH="$HOME/.cargo/bin:$PATH"
cd /root/KernelSU-dm3q
cargo build --release --target aarch64-linux-android -p ksud 2>&1 | head -30
