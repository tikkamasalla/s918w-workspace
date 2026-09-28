#!/bin/sh
set -u
grep -rn "bin/su" /root/KernelSU-dm3q/userspace/ksud/src/*.rs | head -15
echo "=== post-fs-data handler ==="
grep -rn "post_fs_data\|PostFsData\|post-fs-data" /root/KernelSU-dm3q/userspace/ksud/src/cli.rs /root/KernelSU-dm3q/userspace/ksud/src/module.rs 2>/dev/null | head -10
