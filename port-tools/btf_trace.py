import struct

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
(hdr) = struct.unpack_from("<HBBIIIII", blob, 0)
magic, version, flags, hdr_len, type_off, type_len, str_off, str_len = hdr
strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
data = blob[hdr_len + type_off:hdr_len + type_off + type_len]


def s(o):
    if o >= len(strings):
        return "<BAD>"
    end = strings.find(b"\x00", o)
    return strings[o:end][:40]


SKIP = {4: 12, 5: 12, 6: 8, 19: 12, 3: 0, 13: 8, 15: 12}
off = 0
for idx in range(1, 20):
    name_off, info, sz = struct.unpack_from("<III", data, off)
    vlen = info & 0xFFFF
    kind = (info >> 24) & 0x1F
    print(f"type {idx} at {hex(off)} name={s(name_off)!r} kind={kind} vlen={vlen} size={hex(sz)}")
    if kind in (4, 5, 6, 19, 13, 15):
        per = SKIP[kind]
        if kind == 3:
            n = 1
        else:
            n = vlen
        # show first/last extra entries raw
        base = off + 12
        if n > 0:
            first = struct.unpack_from("<II", data, base)
            print(f"    first entry: name={s(first[0])!r} val2={hex(first[1])}")
            if n > 1:
                if kind in (4, 5):
                    last = struct.unpack_from("<III", data, base + per * (n - 1))
                    print(f"    last entry: name={s(last[0])!r} {hex(last[1])} {hex(last[2])}")
                else:
                    last = struct.unpack_from("<II", data, base + per * (n - 1))
                    print(f"    last entry: name={s(last[0])!r} val2={hex(last[1])}")
        off = base + per * n
    elif kind == 3:
        off += 12 + 12
    elif kind == 14:
        off += 12 + 4
    elif kind in (17, 18):
        off += 12 + 4
    else:
        off += 12
