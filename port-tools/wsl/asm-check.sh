#!/bin/sh
set -u
ls -la /usr/include/ | grep -E '^l.*asm|linux' | head -5
ls /usr/include/x86_64-linux-gnu/asm/ioctl.h 2>/dev/null || echo "no multiarch asm either"
dpkg -L linux-libc-dev 2>/dev/null | grep -m3 'asm/ioctl'
