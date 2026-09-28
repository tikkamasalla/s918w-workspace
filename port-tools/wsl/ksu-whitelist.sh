#!/bin/sh
set -u
grep -n 'UNUSED_KSYMS_WHITELIST' /root/s918-src/kernel_platform/msm-kernel/out-dm3q/.config
grep -nE '=(/|")[^"]*/(home|root|workspace|dpi)' /root/s918-src/kernel_platform/msm-kernel/out-dm3q/.config | head -20
echo "--- create empty whitelist at stock path ---"
WL=/home/dpi/qb5_8814/workspace/P4_1716/android/kernel_platform/out/msm-kernel-kalama-gki/gki_kernel/common/abi_symbollist.raw
mkdir -p "$(dirname "$WL")"
touch "$WL"
ls -la "$WL"
