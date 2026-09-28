"""Audit target.h symbol/layout offsets against recovered ground truth."""
import json
import re
import sys
from pathlib import Path

port = Path(r"E:\s918w-port")
th = (port / "dm3q-S918WVLS6CYB3" / "target.h").read_text()
base = 0xFFFFFFC008000000

nm = {}
for line in (port / "kernel" / "vmlinux.nm").read_text(encoding="utf-16").splitlines():
    parts = line.split()
    if len(parts) == 3 and all(c in "0123456789abcdef" for c in parts[0]):
        nm[parts[2]] = int(parts[0], 16)

lay = json.load(open(port / "kernel" / "layouts.json"))


def tdef(name):
    m = re.search(r"#define " + name + r"\s+(0x[0-9a-fA-F]+)", th)
    return int(m.group(1), 16) if m else None


syms = {
    "INIT_TASK_OFF": "init_task",
    "PREPARE_KERNEL_CRED_OFF": "prepare_kernel_cred",
    "COMMIT_CREDS_OFF": "commit_creds",
    "OVERRIDE_CREDS_OFF": "override_creds",
    "ROOT_TASK_GROUP_OFF": "root_task_group",
    "SELINUX_ENFORCING_OFF": "selinux_state",
    "KMALLOC_CACHES_OFF": "kmalloc_caches",
    "ANON_PIPE_BUF_OPS_OFF": "anon_pipe_buf_ops",
    "SYSTEM_UNBOUND_WQ_OFF": "system_unbound_wq",
    "CALL_USERMODEHELPER_EXEC_WORK_OFF": "call_usermodehelper_exec_work",
    "ASHMEM_FOPS_OFF": "ashmem_fops",
    "ASHMEM_IOCTL_OFF": "ashmem_ioctl",
    "ASHMEM_COMPAT_IOCTL_OFF": "compat_ashmem_ioctl",
    "ASHMEM_MMAP_OFF": "ashmem_mmap",
    "ASHMEM_OPEN_OFF": "ashmem_open",
    "ASHMEM_RELEASE_OFF": "ashmem_release",
    "ASHMEM_SHOW_FDINFO_OFF": "ashmem_show_fdinfo",
    "CONFIGFS_READ_ITER_OFF": "configfs_read_iter",
    "CONFIGFS_BIN_WRITE_ITER_OFF": "configfs_bin_write_iter",
    "COPY_SPLICE_READ_OFF": "generic_file_splice_read",
    "NOOP_LLSEEK_OFF": "noop_llseek",
    "SLIDE_NFULNL_LOGGER_OBJECT_OFF": "nfulnl_logger",
    "SLIDE_SYSCTL_BOOTID_OFF": "sysctl_bootid",
}
errs = 0
for macro, sym in syms.items():
    v = tdef(macro)
    want = nm[sym] - base
    status = "OK " if v == want else "MISMATCH"
    if v != want:
        errs += 1
    print(f"{status} {macro} target={hex(v)} nm={hex(want)}")

# BTF-derived checks: (macro, struct, member-or-None-for-size)
btf_checks = [
    ("FAKE_TASK_USAGE_OFF", "task_struct", "usage"),
    ("FAKE_TASK_PRIO_OFF", "task_struct", "prio"),
    ("FAKE_TASK_NORMAL_PRIO_OFF", "task_struct", "normal_prio"),
    ("FAKE_TASK_PI_LOCK_OFF", "task_struct", "pi_lock"),
    ("FAKE_TASK_PI_WAITERS_OFF", "task_struct", "pi_waiters"),
    ("FAKE_TASK_PI_TOP_TASK_OFF", "task_struct", "pi_top_task"),
    ("FAKE_TASK_PI_BLOCKED_ON_OFF", "task_struct", "pi_blocked_on"),
    ("TASK_STRUCT_CRED_OFF", "task_struct", "cred"),
    ("TASK_STRUCT_REAL_CRED_OFF", "task_struct", "real_cred"),
    ("FAKE_TASK_TASK_GROUP_OFF", "task_struct", "sched_task_group"),
    ("FOPS_IOCTL_OFF", "file_operations", "unlocked_ioctl"),
    ("FOPS_COMPAT_IOCTL_OFF", "file_operations", "compat_ioctl"),
    ("FOPS_MMAP_OFF", "file_operations", "mmap"),
    ("FOPS_OPEN_OFF", "file_operations", "open"),
    ("FOPS_RELEASE_OFF", "file_operations", "release"),
    ("FOPS_SPLICE_READ_OFF", "file_operations", "splice_read"),
    ("FOPS_SHOW_FDINFO_OFF", "file_operations", "show_fdinfo"),
    ("STRUCT_PAGE_COMPOUND_HEAD_OFF", None, 0x08),
    ("STRUCT_SLAB_CACHE_OFF", None, 0x18),
    ("STRUCT_PAGE_TYPE_OFF", None, 0x30),
    ("WQ_DFL_PWQ_OFF", "workqueue_struct", "dfl_pwq"),
    ("POOL_WORKLIST_OFF", "worker_pool", "worklist"),
    ("POOL_NR_IDLE_OFF", "worker_pool", "nr_idle"),
    ("FAKE_WAITER_PI_TREE_ENTRY_OFF", "rt_mutex_waiter", "pi_tree_entry"),
    ("FAKE_WAITER_TASK_OFF", "rt_mutex_waiter", "task"),
    ("FAKE_WAITER_LOCK_OFF", "rt_mutex_waiter", "lock"),
    ("FAKE_WAITER_WAKE_STATE_OFF", "rt_mutex_waiter", "wake_state"),
    ("FAKE_WAITER_PRIO_OFF", "rt_mutex_waiter", "prio"),
    ("FAKE_WAITER_DEADLINE_OFF", "rt_mutex_waiter", "deadline"),
    ("FAKE_WAITER_WW_CTX_OFF", "rt_mutex_waiter", "ww_ctx"),
]
for macro, st, member in btf_checks:
    v = tdef(macro)
    want = member if st is None else lay[st]["members"][member]["off"]
    status = "OK " if v == want else "MISMATCH"
    if v != want:
        errs += 1
    print(f"{status} {macro} target={hex(v)} btf={hex(want)}")

# derived composites
misc = tdef("ASHMEM_MISC_FOPS_OFF")
print(("OK " if misc == 0x02A408C8 else "MISMATCH"),
      f"ASHMEM_MISC_FOPS_OFF={hex(misc)} (ashmem_misc 0x02a408b8 + fops 0x10)")
if misc != 0x02A408C8:
    errs += 1
print("total mismatches:", errs)
sys.exit(1 if errs else 0)
