#!/bin/sh
set -u
cd /root/essentials-src
sed -n '1,110p' app/src/main/java/com/sameerasw/essentials/services/receivers/SecurityReceiver.kt
