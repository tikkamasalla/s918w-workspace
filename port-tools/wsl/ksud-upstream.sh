#!/bin/sh
set -u
cd /root
git ls-remote https://github.com/tiann/KernelSU.git HEAD 2>/dev/null | head -2
git clone --depth 50 https://github.com/tiann/KernelSU.git KSU-upstream-check 2>&1 | tail -1
grep -rn "ephemeral" KSU-upstream-check/userspace/ksud/src/cli.rs | head -5
grep -rn -B3 -A10 "ephemeral" KSU-upstream-check/userspace/ksud/src/late_load.rs 2>/dev/null | head -40
ls KSU-upstream-check/userspace/ksud/src/ | head -30
