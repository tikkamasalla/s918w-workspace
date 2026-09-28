#!/bin/sh
set -u
git ls-remote https://github.com/Kernel-SU/adb_client 2>&1 | head -8
echo "--- pin:"
git ls-remote https://github.com/Kernel-SU/adb_client d97a966435bebaa55017834869dec08150826aa7 2>&1 | head -4
