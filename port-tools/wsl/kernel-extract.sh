#!/bin/sh
set -u
mkdir -p /root/s918-src && cd /root/s918-src
tar xzf /root/s918-drop/Kernel.tar.gz
ls
echo "--- version:"
head -8 Makefile 2>/dev/null | grep -E '^(VERSION|PATCHLEVEL|SUBLEVEL|EXTRAVERSION|NAME)'
echo "--- dm3q configs:"
ls arch/arm64/configs/ 2>/dev/null | grep -i -E 'dm3q|kalama|gki' | head -20
