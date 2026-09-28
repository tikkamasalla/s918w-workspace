#!/bin/sh
set -u
cd /root/KernelSU-dm3q
cp userspace/ksuinit/Cargo.toml /tmp/Cargo.ksuinit.orig
python3 - <<'EOF'
p = '/root/KernelSU-dm3q/userspace/ksuinit/Cargo.toml'
t = open(p).read()
t = t.replace(
  'rustix = { git = "https://github.com/Kernel-SU/rustix.git", rev = "4a53fbc", features = ["mount", "fs", "runtime", "system", "process"] }',
  '# Original Kernel-SU org repo deleted; same commit via ReSukiSU mirror.\nrustix = { git = "https://github.com/ReSukiSU/rustix", rev = "4a53fbc", features = ["mount", "fs", "runtime", "system", "process"] }')
open(p, 'w').write(t)
print('rewritten')
EOF
export PATH="$HOME/.cargo/bin:$PATH"
export GIT_TERMINAL_PROMPT=0
cargo update -p rustix 2>&1 | tail -6
