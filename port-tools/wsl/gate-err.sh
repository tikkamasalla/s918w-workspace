#!/bin/sh
set -u
grep -B2 -A8 -iE 'error|warning: implicit' /tmp/gate.log | head -40
