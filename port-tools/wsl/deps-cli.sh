#!/bin/sh
set -u
mkdir -p /root/.cargo
printf '[net]\ngit-fetch-with-cli = true\n' > /root/.cargo/config.toml
cat /root/.cargo/config.toml
export PATH="$HOME/.cargo/bin:$PATH"
export GIT_TERMINAL_PROMPT=0
cd /root/KernelSU-dm3q
cargo update -p adb_client -p prop-rs-android -p java-properties 2>&1 | tail -8
