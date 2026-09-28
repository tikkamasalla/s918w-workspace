#!/bin/sh
set -u
sed -n '480,515p' /root/KernelSU-dm3q/userspace/ksud/src/cli.rs
echo "=== symlink refs ==="
grep -rn "symlink" /root/KernelSU-dm3q/userspace/ksud/src/module.rs /root/KernelSU-dm3q/userspace/ksud/src/utils.rs /root/KernelSU-dm3q/userspace/ksud/src/defs.rs 2>/dev/null | head -12
