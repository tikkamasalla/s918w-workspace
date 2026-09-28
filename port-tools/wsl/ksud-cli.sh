#!/bin/sh
set -u
grep -rn "ephemeral" /root/KernelSU-dm3q/userspace/ksud/src/ | head
echo "--- late-load cli:"
grep -n -B2 -A25 'LateLoad' /root/KernelSU-dm3q/userspace/ksud/src/cli.rs | head -60
