#!/bin/sh
set -u
cd /root
curl -sSL -o ndk-r28c-linux.zip \
  'https://dl.google.com/android/repository/android-ndk-r28c-linux.zip' \
  && ls -la ndk-r28c-linux.zip
