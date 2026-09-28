#!/bin/sh
set -u
cd /root/KernelSU-dm3q
grep -rn "Kernel-SU/rustix" --include=Cargo.toml . | head
