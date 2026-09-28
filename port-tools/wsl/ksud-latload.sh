#!/bin/sh
set -u
grep -n "data/adb/ksud\|/data/adb" /root/KernelSU-dm3q/userspace/ksud/src/late_load.rs | head -20
echo "--- run() signature:"
grep -n -A8 "pub fn run" /root/KernelSU-dm3q/userspace/ksud/src/late_load.rs | head -15
