#!/bin/sh
set -u
echo "--- tmp:"; ls /tmp/ | head -8
echo "--- root:"; ls /root/ | head -20
echo "--- uptime:"; uptime
echo "--- ksudm3q:"; ls /root/KernelSU-dm3q/kernel/kernelsu.ko 2>/dev/null || echo MISSING-KO-BUILD-TREE
echo "--- phone:"; echo skip
