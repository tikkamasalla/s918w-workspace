#!/usr/bin/env python3
"""Offset gate: 5.15.189-tree layouts (pahole/DWARF) vs SM-S918W CYB3 BTF values.
PASS only if every checked offset is byte-identical.
"""
import re
import subprocess
import sys

GATE_O = "/root/gate/gate-dwarf.o"
WQ_O = "/root/s918-src/kernel_platform/msm-kernel/out-dm3q/kernel/workqueue.o"

# (struct, member, expected_byte_offset, object_file)
CHECKS = [
    ("task_struct", "usage", 0x38, GATE_O),
    ("task_struct", "prio", 0x7C, GATE_O),
    ("task_struct", "normal_prio", 0x84, GATE_O),
    ("task_struct", "sched_task_group", 0x400, GATE_O),
    ("task_struct", "pi_lock", 0x884, GATE_O),
    ("task_struct", "pi_waiters", 0x898, GATE_O),
    ("task_struct", "pi_top_task", 0x8A8, GATE_O),
    ("task_struct", "pi_blocked_on", 0x8B0, GATE_O),
    ("task_struct", "cred", 0x798, GATE_O),
    ("task_struct", "real_cred", 0x790, GATE_O),
    ("file_operations", "unlocked_ioctl", 0x50, GATE_O),
    ("file_operations", "compat_ioctl", 0x58, GATE_O),
    ("file_operations", "mmap", 0x60, GATE_O),
    ("file_operations", "open", 0x70, GATE_O),
    ("file_operations", "release", 0x80, GATE_O),
    ("file_operations", "splice_read", 0xC8, GATE_O),
    ("file_operations", "show_fdinfo", 0xE0, GATE_O),
    ("page", "compound_head", 0x08, GATE_O),
    ("page", "slab_cache", 0x18, GATE_O),
    ("page", "page_type", 0x30, GATE_O),
    ("rt_mutex_waiter", "pi_tree_entry", 0x18, GATE_O),
    ("rt_mutex_waiter", "task", 0x30, GATE_O),
    ("rt_mutex_waiter", "lock", 0x38, GATE_O),
    ("rt_mutex_waiter", "wake_state", 0x40, GATE_O),
    ("rt_mutex_waiter", "prio", 0x44, GATE_O),
    ("rt_mutex_waiter", "deadline", 0x48, GATE_O),
    ("rt_mutex_waiter", "ww_ctx", 0x50, GATE_O),
    ("miscdevice", "fops", 0x10, GATE_O),
    ("workqueue_struct", "dfl_pwq", 0xB0, WQ_O),
    ("worker_pool", "worklist", 0x20, WQ_O),
    ("worker_pool", "nr_idle", 0x34, WQ_O),
    ("selinux_state", "enforcing", 0x0, GATE_O),
]

SIZE_CHECKS = [
    ("task_struct", 0x1200, GATE_O),
    ("file_operations", 0x120, GATE_O),
    ("mm_struct", 0x3E0, GATE_O),
    ("page", 0x40, GATE_O),
    ("rt_mutex_waiter", 0x58, GATE_O),
]

fails = 0
cache = {}


def pahole(struct, obj):
    key = (struct, obj)
    if key not in cache:
        p = subprocess.run(["pahole", "-C", struct, obj],
                           capture_output=True, text=True)
        cache[key] = p.stdout
    return cache[key]


mem_re = re.compile(r"^\s*[\w\s\*\[\]\(\)]+?\(\*(\w+)\)\([^;]*;\s*/\*\s*(\d+)\s+\d+\s*\*/")
mem_re2 = re.compile(r"^\s*(?:struct|union|enum)?\s*[\w\s\*\[\]]*?\b(\w+)(?:\s*__attribute__\(\(.*?\)\))?\s*(?:\[\d*\])?;\s*/\*\s*(\d+)\s+\d+\s*\*/")

for struct, member, want, obj in CHECKS:
    out = pahole(struct, obj)
    if not out.strip():
        print(f"NO-DWARF {struct}")
        fails += 1
        continue
    hits = []
    for line in out.splitlines():
        m = mem_re.match(line) or mem_re2.match(line)
        if m and m.group(1) == member:
            hits.append(int(m.group(2)))
    if want in hits:
        extra = "" if len(hits) == 1 else f" (ambiguous x{len(hits)}, want present)"
        print(f"OK   {struct}.{member} = {hex(want)}{extra}")
    else:
        print(f"FAIL {struct}.{member}: want {hex(want)}, pahole says "
              f"{[hex(h) for h in hits] or 'NOT-FOUND'}")
        fails += 1

size_re = re.compile(r"/\*\s*size:\s*(\d+)", re.S)
for struct, want, obj in SIZE_CHECKS:
    out = pahole(struct, obj)
    ms = size_re.findall(out)
    got = int(ms[-1]) if ms else None
    if got == want:
        print(f"OK   sizeof({struct}) = {hex(got)}")
    else:
        print(f"FAIL sizeof({struct}): want {hex(want)}, got "
              f"{hex(got) if got is not None else None}")
        fails += 1

print("GATE:", "PASS" if fails == 0 else f"FAIL({fails})")
sys.exit(1 if fails else 0)
