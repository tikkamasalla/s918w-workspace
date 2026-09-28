#!/bin/sh
set -u
cd /root
python3 -c "import gzip; d=gzip.open('/mnt/e/s918w-port/kernel/config.gz','rt',errors='replace').read(); open('/root/target.config','w').write('\n'.join(l for l in d.splitlines() if not l.startswith('# ')) + '\n')"
grep -E '^(CONFIG_CC_VERSION_TEXT|CONFIG_LTO_CLANG|CONFIG_CFI_CLANG|CONFIG_SHADOW_CALL_STACK|CONFIG_MODVERSIONS|CONFIG_MODULE_FORCE_LOAD|CONFIG_TRIM_UNUSED_KSYMS|CONFIG_DEBUG_INFO_BTF|CONFIG_DEBUG_INFO_BTF_MODULES|CONFIG_LOCALVERSION|CONFIG_IKCONFIG)' /root/target.config
echo "--- tree:"
grep -E '^(VERSION|PATCHLEVEL|SUBLEVEL)' /root/s918-src/kernel_platform/msm-kernel/Makefile 2>/dev/null
ls /root/s918-src/kernel_platform/msm-kernel/arch/arm64/configs/ 2>/dev/null | grep -iE 'dm3q|gki|kalama' | head
ls /root/s918-src/kernel_platform/msm-kernel/ | head -30
