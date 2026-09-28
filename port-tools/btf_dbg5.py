import json
import struct

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
(hdr) = struct.unpack_from("<HBBIIIII", blob, 0)
magic, version, flags, hdr_len, type_off, type_len, str_off, str_len = hdr
strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
data = blob[hdr_len + type_off:hdr_len + type_off + type_len]


def s(o):
    end = strings.find(b"\x00", o)
    return strings[o:end].decode("utf-8", "replace")


lay = json.load(open(r"E:\s918w-port\kernel\layouts.json"))
for want in ("page", "rt_mutex_waiter", "miscdevice", "mm_struct"):
    p = int(lay[want]["at"], 16)
    info = struct.unpack_from("<I", data, p + 4)[0]
    size = struct.unpack_from("<I", data, p + 8)[0]
    vlen = info & 0xFFFF
    print(f"{want} at {hex(p)} kind={(info >> 24) & 0x1F} vlen={vlen} size={hex(size)}")
    for i in range(vlen):
        mn, mt, mo = struct.unpack_from("<III", data, p + 12 + 12 * i)
        print(f"   {s(mn)!r:30s} type={mt:<8d} bitoff={hex(mo)}")
