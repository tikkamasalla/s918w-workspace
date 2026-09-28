#!/bin/sh
set -u
cd /root/s918-src
ls kernel_platform/
grep -E '^(VERSION|PATCHLEVEL|SUBLEVEL|EXTRAVERSION)' kernel_platform/common/Makefile 2>/dev/null | head -5
echo "--- defconfigs mentioning dm3q:"
find . -name '*dm3q*' 2>/dev/null | head -20
echo "--- kalama:"
find . -maxdepth 4 -iname '*kalama*' 2>/dev/null | head -10
