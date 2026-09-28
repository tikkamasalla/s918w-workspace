#!/bin/sh
set -u
find /root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/lib* -maxdepth 1 -name 'libclang*' 2>/dev/null | head -3
ls /usr/lib/x86_64-linux-gnu/libclang* /usr/lib/llvm*/lib/libclang* 2>/dev/null | head -5
