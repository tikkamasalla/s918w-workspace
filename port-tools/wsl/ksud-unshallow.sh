#!/bin/sh
set -u
export DEBIAN_FRONTEND=noninteractive
apt-get install -y -q linux-libc-dev 2>&1 | tail -1
ls /usr/include/asm/ioctl.h 2>/dev/null || echo "NO asm/ioctl.h"
cd /root/KernelSU-dm3q
git fetch --unshallow 2>&1 | tail -2
git rev-list --count HEAD
git describe --tags --always | head -1
