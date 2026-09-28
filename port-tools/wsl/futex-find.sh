#!/bin/sh
set -u
find /root/s918-src/kernel_platform/msm-kernel/kernel -maxdepth 2 -iname '*futex*' 2>/dev/null | head
