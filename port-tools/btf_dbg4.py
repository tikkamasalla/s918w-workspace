import struct

blob = open(r"E:\s918w-port\kernel\vmlinux.btf", "rb").read()
(hdr) = struct.unpack_from("<HBBIIIII", blob, 0)
magic, version, flags, hdr_len, type_off, type_len, str_off, str_len = hdr
strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
data = blob[hdr_len + type_off:hdr_len + type_off + type_len]


def s(o):
    end = strings.find(b"\x00", o)
    return strings[o:end].decode()


# locate file_operations STRUCT via resync info from layouts.json if present
import json
try:
    lay = json.load(open(r"E:\s918w-port\kernel\layouts.json"))
    p = int(lay["file_operations"]["at"], 16)
    print("file_operations at", hex(p))
except Exception as e:
    print("no layouts.json:", e)
    raise SystemExit

info = struct.unpack_from("<I", data, p + 4)[0]
vlen = info & 0xFFFF
print("vlen:", vlen)
for i in range(min(vlen, 12)):
    a, b, c = struct.unpack_from("<III", data, p + 12 + 12 * i)
    print(f"  {s(a):20s} a={hex(a)} b={hex(b)} c={hex(c)}")
