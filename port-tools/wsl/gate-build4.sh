#!/bin/sh
set -u
KDIR=/root/s918-src/kernel_platform/msm-kernel
cat > /root/gate/gate.c <<'EOF'
#include <linux/sched.h>
#include <linux/fs.h>
#include <linux/mm_types.h>
#include <linux/miscdevice.h>
#include <linux/rtmutex.h>
#include <linux/workqueue.h>
#include "security.h"
#include "locking/rtmutex_common.h"
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
printf 'ccflags-y += -I/root/s918-src/kernel_platform/msm-kernel/security/selinux/include -I/root/s918w-port-nope\nobj-m := gate.o\n' > /root/gate/Makefile
printf 'ccflags-y += -I%s/security/selinux/include -I%s/out-dm3q/security/selinux -I%s/kernel\nobj-m := gate.o\n' "$KDIR" "$KDIR" "$KDIR" > /root/gate/Makefile
cat /root/gate/Makefile
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
make -C "$KDIR" O=out-dm3q ARCH=arm64 LLVM=1 LLVM_IAS=1 \
  CROSS_COMPILE=aarch64-linux-gnu- CLANG_TRIPLE=aarch64-linux-gnu- \
  -j8 M=/root/gate modules > /tmp/gate.log 2>&1
echo "gate rc=$?"
ls /root/gate/
