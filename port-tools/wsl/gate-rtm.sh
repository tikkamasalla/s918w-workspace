#!/bin/sh
set -u
grep -rn "struct rt_mutex_waiter {" /root/s918-src/kernel_platform/msm-kernel/include/ /root/s918-src/kernel_platform/msm-kernel/kernel/ 2>/dev/null | head -5
