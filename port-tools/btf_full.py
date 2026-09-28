"""Full-walk BTF and dump authoritative layouts + id map checkpoints."""
import json
import sys

sys.path.insert(0, r"E:\s918w-port\tools")
from btf_layouts import BTF  # noqa: E402

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
btf = BTF(blob)
print("total types:", len(btf.types) - 1)

# verify full consumption: re-walk via internal logic is implicit (no error).
# spot-check known ids from resync: page record etc. by name lookup
for name in ("file_operations", "task_struct", "page", "mm_struct",
             "rt_mutex_waiter", "miscdevice", "workqueue_struct",
             "worker_pool", "selinux_state"):
    t = btf.find_struct(name)
    print(f"{name}: size={hex(t['size'])} nmembers={len(t['members'])}")

# resolve nested page offsets authoritatively
page = btf.find_struct("page")


def resolve(struct_name, path):
    """Walk nested anon members: path = list of member names ('': any anon)."""
    t = btf.find_struct(struct_name)
    base = 0
    for want in path:
        for m_name, m_off, m_type in t["members"]:
            if want == "" and m_name == "":
                pass
            elif m_name != want:
                continue
            # descend if more path remains
            break
        else:
            raise KeyError((struct_name, path))
        bitoff = m_off
        base += bitoff // 8
        if path.index(want) < len(path) - 1 or True:
            pass
        # find member record for next level
        tid = m_type
        nt = btf.types[tid]
        # follow typedef/const/volatile
        while nt["kind"] in (8, 9, 10, 11):
            nt = btf.types[nt["size_or_type"]]
        t = nt
        struct_name = t["name"]
    return base, struct_name


# page layout: union@0x8 -> compound peice; find compound_head/slab_cache/page_type
t = btf.find_struct("page")
for m_name, m_off, m_type in t["members"]:
    print(f"page member {m_name!r} byte={hex(m_off // 8)} typeid={m_type}")
