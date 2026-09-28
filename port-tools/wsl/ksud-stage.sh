#!/bin/sh
set -u
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:$PATH"
KSUD=/root/KernelSU-dm3q/target/aarch64-linux-android/release/ksud
file "$KSUD"
strings "$KSUD" | grep -m2 -E 'android13-5\.15_kernelsu\.ko|32525'
llvm-strip "$KSUD" -o /root/ksud-dm3q-S918WVLS6CYB3-kdp
ls -la /root/ksud-dm3q-S918WVLS6CYB3-kdp
sha256sum /root/ksud-dm3q-S918WVLS6CYB3-kdp /root/KernelSU-dm3q/kernel/kernelsu.ko
cp /root/ksud-dm3q-S918WVLS6CYB3-kdp /mnt/e/s918w-port/Root-My-Galaxy-Payloads/kernelsu/ksud-dm3q-S918WVLS6CYB3-kdp
cp /root/KernelSU-dm3q/kernel/kernelsu.ko "/mnt/e/s918w-port/Root-My-Galaxy-Payloads/kernelsu/android13-5.15.148_kernelsu-dm3q-S918WVLS6CYB3-kdp.ko"
ls -la /mnt/e/s918w-port/Root-My-Galaxy-Payloads/kernelsu/ | grep dm3q-S918WVLS6CYB3
