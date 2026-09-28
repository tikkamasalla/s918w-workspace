#!/bin/sh
set -u
grep -n "define MODULE_LICENSE\|define MODULE_INFO\|define __MODULE_INFO" /root/s918-src/kernel_platform/msm-kernel/include/linux/module.h | head
sed -n '/define __MODULE_INFO(/,+6p' /root/s918-src/kernel_platform/msm-kernel/include/linux/module.h | head -10
