"""Find parent STRUCT of a member by backward scan + full validation."""
import struct
import sys

blob = open(sys.argv[1], "rb").read()
(hdr) = struct.unpack_from("<HBBIIIII", blob, 0)
magic, version, flags, hdr_len, type_off, type_len, str_off, str_len = hdr
strings = blob[hdr_len + str_off:hdr_len + str_off + str_len]
data = blob[hdr_len + type_off:hdr_len + type_off + type_len]


def s(o):
    if o >= len(strings):
        return None
    end = strings.find(b"\x00", o)
    if end < 0:
        return None
    return strings[o:end]


def printable(b):
    return b == b"" or all(32 <= c < 127 for c in b)


member = sys.argv[2].encode()
mo = strings.find(member + b"\x00")
print("member string at", hex(mo))
needle = struct.pack("<I", mo)
hits = []
cur = 0
while True:
    q = data.find(needle, cur)
    if q < 0:
        break
    cur = q + 4
    hits.append(q)
print(f"{len(hits)} raw hits")

# member slot layout: (name_off, type, bitoff). For member index k in a
# struct with header at h: q = h + 12 + 12*k  ->  h = q - 12*(k+1), k>=0.
# Try k in 0..400 and fully validate the candidate header.
found = []
for q in hits:
    if q % 4 != 0:
        continue
    for k in range(0, 400):
        h = q - 12 * (k + 1)
        if h < 0:
            break
        if h % 4 != 0:
            continue
        hname, info, size = struct.unpack_from("<III", data, h)
        vlen = info & 0xFFFF
        kind = (info >> 24) & 0x1F
        if kind not in (4, 5) or vlen <= k or vlen > 4095 or size > 0x20000:
            continue
        hn = s(hname)
        if hn is None or not printable(hn):
            continue
        if h + 12 + 12 * vlen > len(data):
            continue
        ok = True
        members = []
        for i in range(vlen):
            mn, mt, moff = struct.unpack_from("<III", data, h + 12 + 12 * i)
            nm = s(mn)
            if nm is None or not printable(nm) or mt > 3000000:
                ok = False
                break
            members.append((nm.decode("utf-8", "replace"), moff, mt))
        if not ok:
            continue
        # the k-th member must be our target with matching bitoff
        if members[k][0] != sys.argv[2]:
            continue
        found.append((h, hn.decode(), kind, vlen, size, k, members[k][1]))
        break  # one header per hit

print(f"{len(found)} validated parent(s)")
for h, hn, kind, vlen, size, k, bitoff in found:
    print(f"  {hn!r} at {hex(h)} kind={kind} vlen={vlen} size={hex(size)} "
          f"member_idx={k} bitoff={hex(bitoff)}")
