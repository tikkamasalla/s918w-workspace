#!/bin/sh
set -u
grep -n "Su" /root/KernelSU-dm3q/userspace/ksud/src/cli.rs | head -15
echo "=== su.rs head ==="
head -60 /root/KernelSU-dm3q/userspace/ksud/src/su.rs
