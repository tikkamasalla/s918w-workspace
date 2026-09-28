import struct

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
data = blob[24:24 + 0x345034]
strs = blob[24 + 0x345034:]


def s(o):
    if o >= len(strs):
        return "<BAD>"
    return strs[o:strs.index(b"\x00", o)][:48]


for i in range(14):
    name_off, info, sz = struct.unpack_from("<III", data, i * 12)
    kind = (info >> 24) & 0x1F
    print(i + 1, (name_off, hex(info), sz), "kind=", kind,
          "vlen=", info & 0xFFFF, "name=", s(name_off))
