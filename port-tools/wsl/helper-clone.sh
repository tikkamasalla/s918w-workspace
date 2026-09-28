#!/bin/sh
set -u
cd /root
rm -rf helper-for-morphe
git clone --depth 1 https://github.com/rushiranpise/helper-for-morphe.git helper-for-morphe 2>&1 | tail -1
ls helper-for-morphe/tools/ | head
