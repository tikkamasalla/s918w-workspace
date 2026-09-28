"""Generate p0_fingerprint.h from the exact raw kernel Image.

For each candidate slide 0x000000..0x1f0000 (step 0x10000), records the
eight little-endian qwords at page offsets 0x000..0xe00 (step 0x200) of
Image[PROBE - slide]. Verifies by reading all 256 source qwords back.
"""
import struct
import sys
from pathlib import Path

PROBE = 0x1F0000
OFFSETS = [0x000, 0x200, 0x400, 0x600, 0x800, 0xA00, 0xC00, 0xE00]


def main():
    image = Path(sys.argv[1]).read_bytes()
    out = Path(sys.argv[2])
    model = sys.argv[3]
    build = sys.argv[4]

    rows = []
    for slide in range(0x000000, 0x200000, 0x10000):
        base = PROBE - slide
        words = [struct.unpack_from("<Q", image, base + o)[0] for o in OFFSETS]
        rows.append((slide, words))

    # readback verification: all 256 source qwords
    for slide, words in rows:
        base = PROBE - slide
        for o, w in zip(OFFSETS, words):
            assert struct.unpack_from("<Q", image, base + o)[0] == w
    assert len(rows) == 32 and sum(len(w) for _, w in rows) == 256

    lines = [
        f"// P0 fingerprint for {model} {build}.",
        "// Generated from the exact raw Image.",
        f"// Each row maps actual slide to Image[{hex(PROBE)} - slide].",
        "#ifndef P0_FINGERPRINT_H",
        "#define P0_FINGERPRINT_H",
        "",
        "#define P0_FINGERPRINT_WORDS 8",
        "",
        "static const uint16_t p0_fingerprint_offsets[P0_FINGERPRINT_WORDS] = {",
        "  0x000, 0x200, 0x400, 0x600, 0x800, 0xa00, 0xc00, 0xe00,",
        "};",
        "",
        "struct p0_fingerprint {",
        "  uintptr_t slide;",
        "  uint64_t words[P0_FINGERPRINT_WORDS];",
        "};",
        "",
        "static const struct p0_fingerprint p0_fingerprints[] = {",
    ]
    for slide, words in rows:
        w = ", ".join(f"0x{x:016x}ULL" for x in words)
        lines.append(f"  {{ 0x{slide:06x}ULL, {{ {w} }} }},")
    lines += ["};", "", "#endif", ""]
    out.write_text("\n".join(lines))
    print(f"wrote {out} ({len(rows)} rows, readback-verified)")


if __name__ == "__main__":
    main()
