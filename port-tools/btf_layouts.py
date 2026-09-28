"""Minimal BTF parser for deriving kernel structure layouts.

Parses the raw BTF blob (header + type section + string section) per the
Linux BTF specification and resolves STRUCT/UNION sizes and member byte
offsets, following TYPEDEF/VOLATILE/CONST/RESTRICT/PTR chains.

Usage: btf_layouts.py <vmlinux.btf>
Outputs JSON: {struct_name: {"size": N, "members": {name: {"off": bytes, "bits": bitoff, "bf": bitfield_bits}}}}
for the structures of interest.
"""
import json
import struct
import sys

KIND_INT = 1
KIND_PTR = 2
KIND_ARRAY = 3
KIND_STRUCT = 4
KIND_UNION = 5
KIND_ENUM = 6
KIND_FWD = 7
KIND_TYPEDEF = 8
KIND_VOLATILE = 9
KIND_CONST = 10
KIND_RESTRICT = 11
KIND_FUNC = 12
KIND_FUNC_PROTO = 13
KIND_VAR = 14
KIND_DATASEC = 15
KIND_FLOAT = 16

WANT = [
    "file_operations",
    "task_struct",
    "page",
    "folio",
    "miscdevice",
    "rt_mutex_waiter",
    "mm_struct",
    "workqueue_struct",
    "worker_pool",
    "selinux_state",
    "work_struct",
    "list_head",
    "rb_node",
]


class BTF:
    def __init__(self, blob: bytes):
        (magic, version, flags, hdr_len, type_off, type_len,
         str_off, str_len) = struct.unpack_from("<HBBIIIII", blob, 0)
        assert magic == 0xEB9F and version == 1, "bad BTF header"
        self.strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
        data = blob[hdr_len + type_off:hdr_len + type_off + type_len]
        self.types = [None]  # 1-based
        off = 0
        while off < len(data):
            name_off, info, size_or_type = struct.unpack_from("<III", data, off)
            off += 12
            vlen = info & 0xFFFF
            kind_flag = (info >> 31) & 1
            kind = (info >> 24) & 0x1F
            t = {"name": self.str(name_off), "kind": kind,
                 "kind_flag": kind_flag, "vlen": vlen,
                 "size_or_type": size_or_type}
            if kind in (KIND_STRUCT, KIND_UNION):
                members = []
                for _ in range(vlen):
                    m_name, m_type, m_off = struct.unpack_from("<III", data, off)
                    off += 12
                    members.append((self.str(m_name), m_off, m_type))
                t["members"] = members
                t["size"] = size_or_type
            elif kind == KIND_INT:  # extra u32: bits/offset/encoding
                off += 4
                t["size"] = size_or_type
            elif kind == KIND_ENUM:
                off += 8 * vlen
                t["size"] = size_or_type
            elif kind == 19:  # ENUM64: vlen x {name_off, val_lo, val_hi}
                off += 12 * vlen
                t["size"] = size_or_type
            elif kind == KIND_VAR:  # extra u32 linkage
                off += 4
                t["size"] = 0
            elif kind in (17,):  # DECL_TAG: extra u32 component_idx
                off += 4
                t["size"] = 0
            elif kind in (18,):  # TYPE_TAG: u32 type + s32 component_idx
                off += 8
                t["size"] = 0
            elif kind == KIND_FWD:
                t["size"] = 0
            elif kind == KIND_ARRAY:
                off += 12
                t["size"] = 0
            elif kind == KIND_FUNC_PROTO:
                off += 8 * vlen
                t["size"] = 0
            elif kind == KIND_DATASEC:
                off += 12 * vlen
                t["size"] = size_or_type
            else:
                # INT/PTR/TYPEDEF/.../FUNC/VAR/FLOAT: no extra data
                t["size"] = size_or_type if kind in (KIND_INT, KIND_FLOAT) else 0
            self.types.append(t)

    def str(self, off: int) -> str:
        end = self.strings.index(b"\x00", off)
        return self.strings[off:end].decode("utf-8", "replace")

    def find_struct(self, name: str):
        for i in range(1, len(self.types)):
            t = self.types[i]
            if t["name"] == name and t["kind"] in (KIND_STRUCT, KIND_UNION):
                return t
        return None

    def layout(self, name: str):
        t = self.find_struct(name)
        if t is None:
            return None
        members = {}
        for m_name, m_off, m_type in t["members"]:
            if t["kind_flag"]:
                # kflag set: high 8 bits of offset are bitfield width
                bf = (m_off >> 24) & 0xFF
                bitoff = m_off & 0xFFFFFF
            else:
                bf = 0
                bitoff = m_off
            members[m_name] = {"off": bitoff // 8 if bitoff % 8 == 0 else None,
                               "bits": bitoff, "bf": bf, "type": m_type}
        return {"size": t["size"], "members": members}


def main():
    blob = open(sys.argv[1], "rb").read()
    btf = BTF(blob)
    out = {}
    for name in WANT:
        lay = btf.layout(name)
        if lay is not None:
            out[name] = lay
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
