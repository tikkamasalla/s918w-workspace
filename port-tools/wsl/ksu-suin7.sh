#!/bin/sh
set -u
grep -rn "bin/su\b\|bin/su\"" /root/KernelSU-dm3q/userspace/ksud/src/ /root/KernelSU-dm3q/kernel/ 2>/dev/null | grep -vi "ksu_bin\|resetprop\|sulog\|supported\|Consult\|result" | head -15
echo "=== bin asset dir ==="
ls /root/KernelSU-dm3q/userspace/ksud/bin/ 2>/dev/null; ls /root/KernelSU-dm3q/userspace/ksud/bin/aarch64/ 2>/dev/null
