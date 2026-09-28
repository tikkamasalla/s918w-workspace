Adds a complete, **device-tested** port for the Canadian Galaxy S23 Ultra
(`SM-S918W`, `dm3qcsx`) on firmware `S918WVLS6CYB3`
(`samsung/dm3qcsx/dm3q:14/UP1A.231005.007/S918WVLS6CYB3`,
kernel `5.15.148-android13-8-29539737-abS918WVLS6CYB3`).

This is the older 5.15.148 branch — a complement to the 5.15.189 S23-family
work in `docs/S23-porting-notes.md`, not a delta of it. Every constant below
was derived from this firmware's own boot image + BTF, then executed on
hardware. It also wires the profile into the app feed (with `rootHelper`,
which the app's auto-root pipeline downloads), so the Root-My-Galaxy app
supports the SM-S918W once merged.

## Hardware validation (physical SM-S918W, 2026-09-18/19)

- Exploit: slide/KASLR OK, full 32-object group, `uid=2000->0`, no panic,
  Knox warranty bit 0.
- KernelSU late-load: module `Live`, ksud stages complete, no panic.
- Manager v3.2.5: `Working <LKM> [Jailbreak mode]`, `32525-2`, exact
  kernel/fingerprint, SELinux Enforcing.
- Control ioctl: version=32525 flags=0x5 features=0x5 uapi=2,
  **`su_compat=ENABLED`**; Termux `su` → `uid=0 ... context=u:r:ksu:s0`.
- Temp root only (this boot); bootloader locked, no boot image modified.

## Files

- `src/targets/dm3q-S918WVLS6CYB3/target.h` + `p0_fingerprint.h`
  (audit `200/0/65/0`, offset gate `32+5 PASS`, P0 table verified by
  reading all 256 source qwords back from the raw kernel)
- `artifacts/dm3q-S918WVLS6CYB3/cve-2026-43499-app.so` (`104128`,
  `cb14959b...55718197e`) + `cve-2026-43499-root` (`27056`,
  `30a1ef26...69d47ba`)
- `kernelsu/android13-5.15.148_kernelsu-dm3q-S918WVLS6CYB3-kdp.ko`
  (`357048`, `eb7e4b4a...d8189bf`) + `ksud-dm3q-S918WVLS6CYB3-kdp`
  (`4629456`, `d972cd67...148f76a78`, v32525, `--ephemeral`)
- `kernelsu/patches/KernelSU-v3.2.5-dm3q-5.15.148.patch` + `.NOTES.md`
- `docs/SM-S918W-S918WVLS6CYB3.md` + KernelSU/Termux screenshots
- `support/targets-v3.json` — feed entry (`SM-S918W` / `5.15.148`,
  `slideSource: tracefs`)

## Notes

- The KASLR route uses tracefs: run via Shizuku, close to boot;
  per-boot success is probabilistic (succeeded attempt 1/8 on a fresh boot).
- Companion upstream PR: BuSung-dev/Root-My-Galaxy-Payloads#352 (same
  port, upstream URL form, without `rootHelper`).
