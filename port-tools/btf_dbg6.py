import struct

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
(hdr) = struct.unpack_from("<HBBIIIII", blob, 0)
magic, version, flags, hdr_len, type_off, type_len, str_off, str_len = hdr
strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
data = blob[hdr_len + type_off:hdr_len + type_off + type_len]


def s(o):
    end = strings.find(b"\x00", o)
    return strings[o:end].decode("utf-8", "replace")


for p, want in ((0xA70, ("mmap", "pgd", "mm_users", "mm_count")),
                (0x1564, ("compound_head", "slab_cache"))):
    info = struct.unpack_from("<I", data, p + 4)[0]
    size = struct.unpack_from("<I", data, p + 8)[0]
    vlen = info & 0xFFFF
    print(f"record at {hex(p)} kind={(info >> 24) & 0x1F} vlen={vlen} size={hex(size)}")
    for i in range(vlen):
        mn, mt, mo = struct.unpack_from("<III", data, p + 12 + 12 * i)
        nm = s(mn)
        if nm in want:
            print(f"   {nm!r} byte_off={hex(mo // 8)}")
