#!/bin/sh
set -u
mkdir -p /root/gate
cat > /root/gate/gate.c <<'EOF'
#include <linux/sched.h>
#include <linux/fs.h>
#include <linux/mm_types.h>
#include <linux/miscdevice.h>
#include <linux/rtmutex.h>
#include <linux/workqueue.h>
#include <linux/selinux_state.h>
static const unsigned long gate_sizes[] = {
	sizeof(struct task_struct),
	sizeof(struct file_operations),
	sizeof(struct mm_struct),
	sizeof(struct page),
	sizeof(struct rt_mutex_waiter),
	sizeof(struct miscdevice),
	sizeof(struct selinux_state),
};
EOF
printf 'obj-m := gate.o\n' > /root/gate/Makefile
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
KDIR=/root/s918-src/kernel_platform/msm-kernel
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  -j8 M=/root/gate modules > /tmp/gate.log 2>&1
echo "gate rc=$?"
tail -3 /tmp/gate.log
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  -j8 kernel/workqueue.o > /tmp/wq.log 2>&1
echo "wq rc=$?"
tail -3 /tmp/wq.log
ls -la /root/gate/*.o "$KDIR/out-dm3q/kernel/workqueue.o" 2>/dev/null
