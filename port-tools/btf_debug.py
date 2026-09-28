"""Debug-walk BTF types to find desync point."""
import struct
import sys

sys.path.insert(0, r"E:\s918w-port\tools")
from btf_layouts import BTF  # noqa: E402  (reuse header parsing manually below)

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
(magic, version, flags, hdr_len, type_off, type_len,
 str_off, str_len) = struct.unpack_from("<HBBIIIII", blob, 0)
strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
data = blob[hdr_len + type_off:hdr_len + type_off + type_len]

off = 0
idx = 1
hist = []
try:
    while off < len(data):
        start = off
        name_off, info, size_or_type = struct.unpack_from("<III", data, off)
        off += 12
        vlen = info & 0xFFFF
        kind = (info >> 24) & 0x1F
        kflag = (info >> 31) & 1
        if name_off >= len(strings):
            raise ValueError(f"type {idx}: name_off {name_off:#x} >= strlen {len(strings):#x}")
        # skip extra
        if kind in (4, 5):
            off += 12 * vlen
        elif kind == 6:
            off += 8 * vlen
        elif kind == 19:
            off += 12 * vlen
        elif kind == 3:
            off += 12
        elif kind == 13:
            off += 8 * vlen
        elif kind == 15:
            off += 12 * vlen
        elif kind == 14:
            off += 4
        elif kind in (17, 18):
            off += 4
        hist.append((idx, kind, vlen, kflag, size_or_type, start))
        if len(hist) > 8:
            hist.pop(0)
        idx += 1
    print("walked all types:", idx - 1, "final off:", off, "typelen:", len(data))
except ValueError as e:
    print("FAIL:", e)
    print("recent (idx, kind, vlen, kflag, size/type, fileoff):")
    for h in hist:
        print("  ", h)
