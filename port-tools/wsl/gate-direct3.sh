#!/bin/sh
set -u
cat > /root/gate/gate2.c <<'EOF'
#include <linux/sched.h>
#include <linux/fs.h>
#include <linux/mm_types.h>
#include <linux/miscdevice.h>
#include <linux/rtmutex.h>
#include <linux/workqueue.h>
#include "security.h"
#include "locking/rtmutex_common.h"
unsigned long gate_use(struct task_struct *a, struct file_operations *b,
		struct mm_struct *c, struct page *d, struct rt_mutex_waiter *e,
		struct miscdevice *f, struct selinux_state *g)
{
	return sizeof(*a) + sizeof(*b) + sizeof(*c) + sizeof(*d)
		+ sizeof(*e) + sizeof(*f) + sizeof(*g)
		+ (unsigned long)a + (unsigned long)b + (unsigned long)c
		+ (unsigned long)d + (unsigned long)e + (unsigned long)f
		+ (unsigned long)g;
}
EOF
export PATH="/root/ndk25/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin:/usr/bin:/bin"
KDIR=/root/s918-src/kernel_platform/msm-kernel
OUT=$KDIR/out-dm3q
clang --target=aarch64-linux-gnu -nostdinc -D__KERNEL__ \
  -I$KDIR/arch/arm64/include \
  -I$OUT/arch/arm64/include/generated \
  -I$KDIR/include \
  -I$OUT/include \
  -I$KDIR/security/selinux/include \
  -I$OUT/security/selinux \
  -I$KDIR/kernel \
  -I$KDIR/arch/arm64/include/uapi \
  -I$OUT/arch/arm64/include/generated/uapi \
  -I$KDIR/include/uapi \
  -I$OUT/include/generated/uapi \
  -include $KDIR/include/linux/kconfig.h \
  -include $OUT/include/generated/autoconf.h \
  -g -O0 -fno-lto -c /root/gate/gate2.c -o /root/gate/gate-dwarf.o 2>&1 | grep -m5 -i error
file /root/gate/gate-dwarf.o
pahole -C task_struct /root/gate/gate-dwarf.o 2>&1 | head -6
pahole -C page /root/gate/gate-dwarf.o 2>&1 | head -12
