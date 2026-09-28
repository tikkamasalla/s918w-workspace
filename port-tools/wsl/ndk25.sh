#!/bin/sh
set -u
export DEBIAN_FRONTEND=noninteractive
cd /root
curl -sSL -o ndk-r25c-linux.zip \
  'https://dl.google.com/android/repository/android-ndk-r25c-linux.zip' \
  && ls -la ndk-r25c-linux.zip
apt-get install -y -q gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu 2>&1 | tail -1
df -h / | tail -1
