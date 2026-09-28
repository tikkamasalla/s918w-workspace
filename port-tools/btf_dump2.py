import struct

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
data = blob[24:24 + 0x345034]
strs = blob[24 + 0x345034:]


def s(o):
    if o >= len(strs):
        return "<BAD>"
    return strs[o:strs.index(b"\x00", o)][:48]


# walker said type 17 (INT) at fileoff 600, type 18 at 612
for off in (600, 612, 624):
    name_off, info, sz = struct.unpack_from("<III", data, off)
    kind = (info >> 24) & 0x1F
    print(off, (name_off, hex(info), sz), "kind=", kind,
          "vlen=", info & 0xFFFF, "name=", s(name_off))
# also dump 48 bytes from 600 as u32s
print(struct.unpack_from("<12I", data, 600))
