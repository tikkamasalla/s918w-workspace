import struct

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
(magic, version, flags, hdr_len, type_off, type_len,
 str_off, str_len) = struct.unpack_from("<HBBIIIII", blob, 0)
strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
data = blob[hdr_len + type_off:hdr_len + type_off + type_len]

p = 0x45BC
info = struct.unpack_from("<I", data, p + 4)[0]
vlen = info & 0xFFFF
print("vlen:", vlen)
for i in range(vlen):
    mn, mo, mt = struct.unpack_from("<III", data, p + 12 + 12 * i)
    if mn >= len(strings):
        print(f"member {i}: BAD name_off {hex(mn)} type {mt}")
        break
    end = strings.find(b"\x00", mn)
    nm = strings[mn:end]
    ok = (nm == b"") or all(32 <= c < 127 for c in nm)
    if not ok or mt > 3000000:
        print(f"member {i}: name_off={hex(mn)} name={nm[:60]!r} type={mt} printable={ok}")
        break
else:
    print("all members valid")
