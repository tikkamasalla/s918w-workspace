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
cargo build --release --target aarch64-linux-android -p ksud 2>&1 | tail -4
find target/aarch64-linux-android/release -maxdepth 1 -name 'ksud' -exec ls -la {} \; 2>/dev/null
