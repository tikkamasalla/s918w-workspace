#!/bin/sh
set -u
cd /root
unzip -q -o ndk-r25c-linux.zip -d ndk25
N25=/root/ndk25/android-ndk-r25c
"$N25/toolchains/llvm/prebuilt/linux-x86_64/bin/clang" --version | head -1
ls "$N25/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android21-clang" \
   "$N25/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-strip" \
   "$N25/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-nm"
echo "--- config (keep not-set lines) ---"
python3 -c "
import gzip
d = gzip.open('/mnt/e/s918w-port/kernel/config.gz','rt',errors='replace').read().splitlines()
keep = [l for l in d if l == '' or l.startswith('CONFIG_') or l.startswith('# CONFIG_')]
open('/root/target.config','w').write('\n'.join(keep) + '\n')
print('kept lines:', len(keep))"
grep -c '^# CONFIG_.* is not set' /root/target.config
echo "--- prepare tree ---"
export PATH="$N25/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
export ARCH=arm64
KDIR=/root/s918-src/kernel_platform/msm-kernel
OUT=$KDIR/out-dm3q
mkdir -p "$OUT"
cp /root/target.config "$OUT/.config"
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  olddefconfig 2>&1 | tail -3
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  -j8 modules_prepare 2>&1 | tail -5
echo "--- verify ---"
cat "$OUT/include/config/kernel.release"
grep 'CONFIG_CC_VERSION_TEXT' "$OUT/.config"
grep -E '^(CONFIG_LOCALVERSION|CONFIG_DEBUG_INFO|CONFIG_DEBUG_INFO_BTF)' "$OUT/.config"
