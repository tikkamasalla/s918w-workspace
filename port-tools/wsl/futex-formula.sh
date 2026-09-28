#!/bin/sh
set -u
grep -n -B3 -A25 "futex_hashsize" /root/s918-src/kernel_platform/msm-kernel/kernel/futex.c | sed -n '1,45p'
