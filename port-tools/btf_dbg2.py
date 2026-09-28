import struct

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
(hdr) = struct.unpack_from("<HBBIIIII", blob, 0)
magic, version, flags, hdr_len, type_off, type_len, str_off, str_len = hdr
strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
data = blob[hdr_len + type_off:hdr_len + type_off + type_len]

for want in ("task_struct",):
    noff = strings.find(want.encode() + b"\x00")
    print(want, hex(noff))
    needle = struct.pack("<I", noff)
    cur = 0
    n = 0
    while True:
        p = data.find(needle, cur)
        if p < 0:
            break
        cur = p + 4
        n += 1
        if p + 12 <= len(data):
            info = struct.unpack_from("<I", data, p + 4)[0]
            size = struct.unpack_from("<I", data, p + 8)[0]
            print(f"  hit at {hex(p)} align={p % 4} info={hex(info)} "
                  f"kind={(info >> 24) & 0x1F} vlen={info & 0xFFFF} size={hex(size)}")
        if n > 20:
            print("  ...truncated")
            break
