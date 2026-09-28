#!/bin/sh
set -u
python3 /mnt/e/s918w-port/Root-My-Galaxy-Payloads/kernelsu/tools/audit_module_against_target.py \
  /root/KernelSU-dm3q/kernel/kernelsu.ko \
  /mnt/e/s918w-port/kernel/vmlinux.elf \
  /tmp/dm3q-symvers.txt \
  --manual-relocation 2>&1 | tail -15
