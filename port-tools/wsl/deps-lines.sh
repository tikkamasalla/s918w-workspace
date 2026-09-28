#!/bin/sh
set -u
grep -n "adb_client\|java-properties\|ksu_props\|prop-rs" /root/KernelSU-dm3q/userspace/ksud/Cargo.toml
