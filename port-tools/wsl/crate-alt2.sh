#!/bin/sh
set -u
echo "--- crates.io:"
curl -s -m 30 -w '\nHTTP:%{http_code}\n' 'https://crates.io/api/v1/crates/adb_client/3.1.1' | head -c 800
echo "--- magica wiring:"
grep -rn "magica" /root/KernelSU-dm3q/userspace/ksud/src/*.rs /root/KernelSU-dm3q/userspace/ksud/Cargo.toml 2>/dev/null | head -15
echo "--- ksud features:"
sed -n '1,60p' /root/KernelSU-dm3q/userspace/ksud/Cargo.toml
