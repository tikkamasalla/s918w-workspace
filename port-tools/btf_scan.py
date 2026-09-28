"""Raw BTF blob extractor for Samsung ARM64 kernel Images.

Implements the validation procedure from the project's PORTING.md:
little-endian BTF header magic 0xeb9f, version/flg/hdr_len checks,
section-bounds checks, and the required NUL byte at the string section
start. Refuses ambiguous Images (expects exactly one blob).
"""
from pathlib import Path
import struct
import sys


def find_btf(image: bytes):
    prefix = b"\x9f\xeb\x01\x00"
    candidates = []
    cursor = 0
    while True:
        start = image.find(prefix, cursor)
        if start < 0:
            break
        cursor = start + 1
        if start + 24 > len(image):
            continue
        header = struct.unpack_from("<HBBIIIII", image, start)
        magic, version, flags, header_len, type_off, type_len, str_off, str_len = header
        if magic != 0xEB9F or version != 1 or flags != 0 or header_len < 24:
            continue
        payload_len = max(type_off + type_len, str_off + str_len)
        end = start + header_len + payload_len
        string_start = start + header_len + str_off
        if end > len(image) or string_start >= end or image[string_start] != 0:
            continue
        candidates.append((start, end))
    return candidates


def main():
    kernel_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    image = kernel_path.read_bytes()
    candidates = find_btf(image)
    if len(candidates) != 1:
        raise SystemExit(f"expected one raw BTF blob, found: {candidates}")
    start, end = candidates[0]
    out_path.write_bytes(image[start:end])
    print(f"raw BTF: [0x{start:x}, 0x{end:x}) ({end - start} bytes)")


if __name__ == "__main__":
    main()
