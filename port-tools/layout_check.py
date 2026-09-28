import json

d = json.load(open(r"E:\s918w-port\kernel\layouts.json"))

# (struct, member, expected_from_S916U1_template)
checks = [
    ("file_operations", None, 0x110),
    ("file_operations", "unlocked_ioctl", 0x50),
    ("file_operations", "compat_ioctl", 0x58),
    ("file_operations", "mmap", 0x60),
    ("file_operations", "open", 0x70),
    ("file_operations", "release", 0x80),
    ("file_operations", "splice_read", 0xc8),
    ("file_operations", "show_fdinfo", 0xe0),
    ("task_struct", "usage", 0x38),
    ("task_struct", "prio", 0x7c),
    ("task_struct", "normal_prio", 0x84),
    ("task_struct", "sched_task_group", 0x400),
    ("task_struct", "pi_lock", 0x884),
    ("task_struct", "pi_waiters", 0x898),
    ("task_struct", "pi_top_task", 0x8a8),
    ("task_struct", "pi_blocked_on", 0x8b0),
    ("task_struct", "cred", 0x798),
    ("task_struct", "real_cred", 0x790),
    ("page", None, 0x40),
    ("page", "compound_head", 0x08),
    ("page", "slab_cache", 0x18),
    ("page", "page_type", 0x30),
    ("miscdevice", "fops", 0x10),
    ("mm_struct", None, 0x400),
    ("workqueue_struct", "dfl_pwq", 0xb0),
    ("worker_pool", "worklist", 0x20),
    ("worker_pool", "nr_idle", 0x34),
    ("selinux_state", "enforcing", 0x0),
]

for struct, member, expect in checks:
    lay = d[struct]
    if member is None:
        got = lay["size"]
        tag = "sizeof"
    else:
        got = lay["members"][member]["off"]
        tag = member
    mark = "SAME" if got == expect else "*** DIFF ***"
    print(f"{struct:18s} {tag:16s} got={hex(got):8s} expect={hex(expect):8s} {mark}")

print()
r = d["rt_mutex_waiter"]
print("rt_mutex_waiter size:", hex(r["size"]))
for m, v in r["members"].items():
    print(f"   {m:20s} off={hex(v['off']) if v['off'] is not None else None}")
