#!/bin/sh
set -u
export PATH="$HOME/.cargo/bin:$PATH"
NDK=/root/ndk25/android-ndk-r28c
NDKBIN=$NDK/toolchains/llvm/prebuilt/linux-x86_64/bin
ls "$NDKBIN/aarch64-linux-android35-clang" "$NDKBIN/llvm-ar"
export LIBCLANG_PATH="$NDK/toolchains/llvm/prebuilt/linux-x86_64/lib"
export CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER="$NDKBIN/aarch64-linux-android35-clang"
export CC_aarch64_linux_android="$NDKBIN/aarch64-linux-android35-clang"
export AR_aarch64_linux_android="$NDKBIN/llvm-ar"
cd /root/KernelSU-dm3q
cargo build --release --target aarch64-linux-android -p ksud 2>&1 | tail -5
find target/aarch64-linux-android/release -maxdepth 1 -name 'ksud' -exec ls -la {} \;
