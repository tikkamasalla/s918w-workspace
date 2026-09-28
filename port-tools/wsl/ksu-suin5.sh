#!/bin/sh
set -u
grep -rn "system/bin/su" /root/KernelSU-dm3q/userspace/ksud/src/*.rs | head -10
echo "=== utils 220-250 ==="
sed -n '220,250p' /root/KernelSU-dm3q/userspace/ksud/src/utils.rs
