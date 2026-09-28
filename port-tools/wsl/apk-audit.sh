#!/bin/sh
set -u
cd /root/helper-for-morphe
python3 tools/audit_helper_sources.py --package com.amazon.mShop.android.shopping --output /mnt/e/s918w-port/apk-audit.csv 2>&1 | tail -25
