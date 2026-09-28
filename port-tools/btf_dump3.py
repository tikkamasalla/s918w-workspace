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
    return strings[o:end][:34]


words = struct.unpack_from("<32I", data, 0x40)
for i in range(0, 32, 4):
    print(f"{hex(0x40 + 4*i)}: " + " ".join(
        f"{w:#10x}({s(w)!r})" if w < len(strings) and s(w) != '<BAD>' and len(s(w)) > 0 else f"{w:#10x}"
        for w in words[i:i+4]))
