#!/bin/sh
set -u
cd /root
rm -rf morphe-patches-src
git clone --depth 1 https://github.com/rushiranpise/morphe-patches.git morphe-patches-src 2>&1 | tail -1
find morphe-patches-src -name 'Constants.kt' 2>/dev/null | head -3
python3 helper-for-morphe/tools/audit_helper_sources.py --help 2>&1 | head -30
