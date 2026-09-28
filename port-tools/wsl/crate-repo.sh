#!/bin/sh
set -u
curl -s -m 30 'https://api.github.com/repos/Kernel-SU/adb_client' | head -c 400; echo
echo "--- branches:"
curl -s -m 30 'https://api.github.com/repos/Kernel-SU/adb_client/branches?per_page=10' | grep -E '"name"|sha' | head -12
echo "--- what rev does ksud want:"
grep -A3 'name = "adb_client"' /root/KernelSU-dm3q/Cargo.lock | head -8
