#!/bin/sh
set -u
cd /root/KSU-upstream-check
echo "--- ephemeral anywhere in userspace:"
grep -rn "ephemeral" userspace/ 2>/dev/null | head -10
echo "--- late-load in cli.rs:"
grep -n -B2 -A12 'LateLoad {' userspace/ksud/src/cli.rs | head -30
echo "--- git log for ephemeral:"
git log --oneline -S ephemeral -- userspace/ksud/src/cli.rs 2>/dev/null | head -5
