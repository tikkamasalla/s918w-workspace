#!/bin/sh
set -u
export GIT_TERMINAL_PROMPT=0
echo "--- ls-remote no-prompt:"
timeout 45 git ls-remote https://github.com/Kernel-SU/adb_client HEAD 2>&1 | head -4
echo "rc=$?"
echo "--- cargo db state:"
ls /root/.cargo/git/db/ 2>/dev/null
ls /root/.cargo/git/checkouts/ 2>/dev/null
