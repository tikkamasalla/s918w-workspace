#!/bin/sh
set -u
cd /root
export GIT_TERMINAL_PROMPT=0
timeout 120 git ls-remote https://github.com/Dr-TSNG/ZygiskNext.git HEAD 2>&1 | head -3
echo "rc=$?"
