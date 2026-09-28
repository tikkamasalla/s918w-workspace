"""Resync BTF struct finder.

Instead of walking the whole type section (fragile if any record kind is
unhandled), this scans for STRUCT/UNION records by their name offset and
strictly validates the member table. Used to derive layout constants.
"""
import json
import struct
import sys

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
]


def printable(b: bytes) -> bool:
    if not b:
        return False
    return all(32 <= c < 127 or c in (9,) for c in b)


def main():
    blob = open(sys.argv[1], "rb").read()
    (magic, version, flags, hdr_len, type_off, type_len,
     str_off, str_len) = struct.unpack_from("<HBBIIIII", blob, 0)
    assert magic == 0xEB9F and version == 1
    strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
    data = blob[hdr_len + type_off:hdr_len + type_off + type_len]

    def s(o):
        if o >= len(strings):
            return None
        end = strings.find(b"\x00", o)
        if end < 0:
            return None
        return strings[o:end]

    # map wanted names to all string offsets holding them
    name_offs = {}
    for want in WANT:
        needle = want.encode() + b"\x00"
        offs = []
        cur = 0
        while True:
            i = strings.find(needle, cur)
            if i < 0:
                break
            # ensure start boundary (preceded by NUL or at 0)
            if i == 0 or strings[i - 1] == 0:
                offs.append(i)
            cur = i + 1
        name_offs[want] = offs
        print(f"{want}: string offsets {[hex(o) for o in offs]}")

    out = {}
    for want in WANT:
        cands = []
        for noff in name_offs[want]:
            needle = struct.pack("<I", noff)
            cur = 0
            while True:
                p = data.find(needle, cur)
                if p < 0 or p + 12 > len(data):
                    break
                cur = p + 4
                if p % 4 != 0:
                    continue
                info = struct.unpack_from("<I", data, p + 4)[0]
                size = struct.unpack_from("<I", data, p + 8)[0]
                vlen = info & 0xFFFF
                kind = (info >> 24) & 0x1F
                kflag = (info >> 31) & 1
                if kind not in (4, 5) or vlen > 4095 or size > 0x20000:
                    continue
                need = 12 + 12 * vlen
                if p + need > len(data):
                    continue
                members = []
                ok = True
                for i in range(vlen):
                    mn, mt, mo = struct.unpack_from("<III", data, p + 12 + 12 * i)
                    nm = s(mn)
                    if nm is None or (nm != b"" and not printable(nm)) or mt > 3000000:
                        ok = False
                        break
                    if kflag:
                        bf = (mo >> 24) & 0xFF
                        bitoff = mo & 0xFFFFFF
                    else:
                        bf = 0
                        bitoff = mo
                    members.append((nm.decode(), bitoff, bf, mt))
                if not ok:
                    continue
                cands.append((p, kind, size, members))
        print(f"{want}: {len(cands)} candidate(s)")
        # prefer STRUCT (kind 4) over UNION; require member sanity via known field
        cands.sort(key=lambda c: c[1] != 4)
        if cands:
            p, kind, size, members = cands[0]
            out[want] = {"kind": kind, "size": size, "at": hex(p),
                         "members": {n: {"off": b // 8 if b % 8 == 0 else None,
                                         "bits": b, "bf": bf}
                                     for n, b, bf, t in members}}
    json.dump(out, open(sys.argv[2], "w"), indent=1)
    print("wrote", sys.argv[2])


if __name__ == "__main__":
    main()
