#!/bin/sh
set -u
ls /root/s918-src/kernel_platform/msm-kernel/kernel/futex/
grep -n -B5 -A20 "futex_hashsize *=" /root/s918-src/kernel_platform/msm-kernel/kernel/futex/*.c | head -50
