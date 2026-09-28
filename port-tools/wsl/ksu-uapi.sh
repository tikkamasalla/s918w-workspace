#!/bin/sh
set -u
grep -rn "KSU_FEATURE_\|define KSU_.*1U\|uapi_version" /root/KernelSU-dm3q/kernel/*.h /root/KernelSU-dm3q/kernel/include/**/*.h 2>/dev/null | head -20
find /root/KernelSU-dm3q/kernel -maxdepth 2 -name '*.h' | head -20
