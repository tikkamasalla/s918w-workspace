#!/bin/sh
set -u
cd /root/KernelSU-dm3q
echo "--- all git sources in Cargo.lock:"
grep -A2 'source = "git+' Cargo.lock | grep -E '^name|source' | head -40
echo "--- distinct git URLs:"
grep -oE 'git\+https://[^"#]+' Cargo.lock | sort -u
