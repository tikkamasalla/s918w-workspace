#!/bin/sh
set -u
cd /root/KernelSU-dm3q
cp userspace/ksud/Cargo.toml /tmp/Cargo.toml.orig
python3 - <<'EOF'
p = '/root/KernelSU-dm3q/userspace/ksud/Cargo.toml'
t = open(p).read()
t = t.replace(
  'java-properties = { git = "https://github.com/Kernel-SU/java-properties.git", branch = "master", default-features = false }',
  '# Pinned git repo deleted upstream; crates.io 2.0.0 used instead.\njava-properties = { version = "2.0.0", default-features = false }')
t = t.replace(
  'adb_client = { git = "https://github.com/Kernel-SU/adb_client" }',
  '# Original Kernel-SU org repo deleted; same commit from author account.\nadb_client = { git = "https://github.com/5ec1cff/adb_client", rev = "d97a966435bebaa55017834869dec08150826aa7" }')
t = t.replace(
  'prop-rs-android = { git = "https://github.com/Kernel-SU/ksu_props" }',
  '# Original Kernel-SU org repo deleted; same commit via ReSukiSU mirror.\nprop-rs-android = { git = "https://github.com/ReSukiSU/ksu_props", rev = "699849f3e4db47b622bcb7fae8e76c728b1b65a6" }')
open(p, 'w').write(t)
print('rewritten')
EOF
grep -n -A1 "Pinned\|same commit" userspace/ksud/Cargo.toml | head -12
export PATH="$HOME/.cargo/bin:$PATH"
export GIT_TERMINAL_PROMPT=0
cargo update -p adb_client -p prop-rs-android -p java-properties 2>&1 | tail -8
