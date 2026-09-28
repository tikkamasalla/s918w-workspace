#!/bin/sh
set -u
grep -n "ensure_binaries" -A 30 /root/KernelSU-dm3q/userspace/ksud/src/assets.rs | head -45
