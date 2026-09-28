#!/bin/sh
set -u
cd /root
python3 helper-for-morphe/tools/audit_helper_sources.py \
  --constants morphe-patches-src/patches/src/main/kotlin/app/template/patches/shared/Constants.kt \
  --package com.amazon.mShop.android.shopping \
  --output /mnt/e/s918w-port/apk-audit.csv 2>&1 | tail -30
