#!/bin/sh
set -u
grep -n "DAEMON_PATH\|DAEMON_LINK_PATH\|BINARY_DIR\|ADB_DIR" /root/KernelSU-dm3q/userspace/ksud/src/defs.rs
echo "=== callers ==="
grep -rn "link_ksud_to_bin\|stage_daemon\b\|stage_daemon(" /root/KernelSU-dm3q/userspace/ksud/src/*.rs | grep -v "fn link_ksud_to_bin\|fn stage_daemon" | head -10
