#!/bin/sh
set -u
grep -B1 -A3 'name = "rustix"' /root/KernelSU-dm3q/Cargo.lock | head -8
grep -rn "rustix" /root/KernelSU-dm3q/userspace/ksud/Cargo.toml /root/KernelSU-dm3q/Cargo.toml 2>/dev/null | head
echo "--- kstep alive:"
curl -s -m 20 -o /dev/null -w '%{http_code}\n' 'https://api.github.com/repos/kstep/kernlog.rs'
echo "--- rustix fork candidates for rev 4a53fbc7cb7a07cabe87125cc21dbc27db316259:"
for f in ReSukiSU/rustix 5ec1cff/rustix tiann/rustix; do
  code=$(curl -s -m 45 -o /tmp/r.tgz -w '%{http_code} %{size_download}' "https://codeload.github.com/$f/tar.gz/4a53fbc7cb7a07cabe87125cc21dbc27db316259")
  echo "$code $f"
done
