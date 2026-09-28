#!/bin/sh
set -u
export PATH="$HOME/.cargo/bin:$PATH"
export GIT_TERMINAL_PROMPT=0
cd /root/KernelSU-dm3q
cargo update -p rustix@0.38.34 2>&1 | tail -8
