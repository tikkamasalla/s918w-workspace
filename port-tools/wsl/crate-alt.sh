#!/bin/sh
set -u
echo "--- crates.io adb_client:"
curl -s -m 30 'https://crates.io/api/v1/crates/adb_client' | head -c 600; echo
echo "--- android_bootimg repo:"
curl -s -m 30 -o /dev/null -w '%{http_code}\n' 'https://api.github.com/repos/Kernel-SU/android_bootimg'
grep -B2 -A4 'name = "android_bootimg"' /root/KernelSU-dm3q/Cargo.lock | head -8
echo "--- ksud use of adb_client:"
grep -rn "adb_client\|adb::" /root/KernelSU-dm3q/userspace/ksud/src/ 2>/dev/null | head -10
grep -rn "adb_client" /root/KernelSU-dm3q/userspace/ksud/Cargo.toml
