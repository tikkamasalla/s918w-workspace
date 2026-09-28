#!/bin/sh
set -u
grep -n "MODULE_FILE\|KBUILD_MODNAME" /root/s918-src/kernel_platform/msm-kernel/include/linux/module.h | head -10
