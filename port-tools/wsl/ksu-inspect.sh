#!/bin/sh
set -u
cd /root
echo "--- clang file was:"; head -c 400 clang-r450784e.tar.gz; echo
echo "--- KernelSU source queries:"
grep -rn "ksu_syscall_table =" KernelSU-3.2.5/kernel/ | head -10
echo "--- resolver def:"
grep -rn "ksu_resolve_symbol_for_functable_hook" KernelSU-3.2.5/kernel/ | head -10
echo "--- hook_init head:"
sed -n '/void __init ksu_syscall_hook_init/,+25p' KernelSU-3.2.5/kernel/hook/arm64/syscall_hook.c
