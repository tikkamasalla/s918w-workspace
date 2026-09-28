#!/bin/sh
set -u
cd /root/essentials-src
grep -n -i "maps\|navigation" app/src/main/java/com/sameerasw/essentials/services/NotificationListener.kt | head -30
