#!/bin/sh
set -u
pahole --version | head -1
echo "=== gate.o structs ==="
for st in task_struct file_operations mm_struct page rt_mutex_waiter miscdevice selinux_state; do
  echo "--- $st"
  pahole -C "$st" /root/gate/gate.o 2>/dev/null | head -4
done
echo "=== workqueue.o structs ==="
for st in workqueue_struct worker_pool; do
  echo "--- $st"
  pahole -C "$st" /root/s918-src/kernel_platform/msm-kernel/out-dm3q/kernel/workqueue.o 2>/dev/null | head -4
done
