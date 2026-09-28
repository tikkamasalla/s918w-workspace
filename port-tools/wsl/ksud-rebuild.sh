#!/bin/sh
set -u
export PATH="$HOME/.cargo/bin:$PATH"
export GIT_TERMINAL_PROMPT=0
NDK=/root/ndk25/android-ndk-r25c
NDKBIN=$NDK/toolchains/llvm/prebuilt/linux-x86_64/bin
export LIBCLANG_PATH="$NDK/toolchains/llvm/prebuilt/linux-x86_64/lib64"
export CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER="$NDKBIN/aarch64-linux-android33-clang"
export CC_aarch64_linux_android="$NDKBIN/aarch64-linux-android33-clang"
export AR_aarch64_linux_android="$NDKBIN/llvm-ar"
export BINDGEN_EXTRA_CLANG_ARGS="-I/usr/include/x86_64-linux-gnu"
cd /root/KernelSU-dm3q
cargo build --release --target aarch64-linux-android -p ksud 2>&1 | tail -3
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:$PATH"
llvm-strip target/aarch64-linux-android/release/ksud -o /root/ksud-dm3q-S918WVLS6CYB3-kdp
ls -la /root/ksud-dm3q-S918WVLS6CYB3-kdp
sha256sum /root/ksud-dm3q-S918WVLS6CYB3-kdp
cp /root/ksud-dm3q-S918WVLS6CYB3-kdp /mnt/e/s918w-port/Root-My-Galaxy-Payloads/kernelsu/ksud-dm3q-S918WVLS6CYB3-kdp
./target/aarch64-linux-android/release/ksud 2>/dev/null || true
