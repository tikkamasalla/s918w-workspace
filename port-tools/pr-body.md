Adds a complete, **device-tested** port for the Canadian Galaxy S23 Ultra
(`SM-S918W`, `dm3qcsx`) on firmware `S918WVLS6CYB3`
(`samsung/dm3qcsx/dm3q:14/UP1A.231005.007/S918WVLS6CYB3`,
kernel `5.15.148-android13-8-29539737-abS918WVLS6CYB3`).

## Hardware validation (physical SM-S918W, 2026-09-18)

- Exploit: slide/KASLR OK every attempt, full 32-object group on attempt 2,
  `uid=2000->0`, no panic, Knox warranty bit 0.
- KernelSU late-load: module `Live`, ksud stages complete, no panic.
- Manager v3.2.5: `Working <LKM> [Jailbreak mode]`, `32525-2`, exact
  kernel/fingerprint, SELinux Enforcing.
- Termux `su`: `uid=0(root) ... context=u:r:ksu:s0` (see screenshots).
- Temp root only (this boot); no boot image modified, bootloader locked.

## Files

- `src/targets/dm3q-S918WVLS6CYB3/target.h` — firmware-derived constants
  (audit `200/0/65/0`, offset gate `32+5 PASS`)
- `src/targets/dm3q-S918WVLS6CYB3/p0_fingerprint.h` — 32-row table from the
  target raw kernel, verified by reading all 256 source qwords back
- `src/targets/dm3q-S918WVLS6CYB3/README.md` — profile notes
- `artifacts/dm3q-S918WVLS6CYB3/cve-2026-43499-app.so` (`104128`,
  `cb14959b...55718197e`) + `README.md`
- `kernelsu/android13-5.15.148_kernelsu-dm3q-S918WVLS6CYB3-kdp.ko`
  (`357048`, `eb7e4b4a...d8189bf`, vermagic `5.15.148-android13-8`)
- `kernelsu/ksud-dm3q-S918WVLS6CYB3-kdp` (`4629456`, `d972cd67...148f76a78`,
  v32525, `--ephemeral` for temp-root)
- `kernelsu/patches/KernelSU-v3.2.5-dm3q-5.15.148.patch` + `.NOTES.md`
- `docs/SM-S918W-S918WVLS6CYB3.md` — full derivation/validation record +
  KernelSU/Termux screenshots
- `support/targets-v3.json` — feed entry (`models: ["SM-S918W"]`,
  `kernelVersions: ["5.15.148"]`)

## Notes for reviewers

- The KASLR route uses tracefs, unreachable from the app domain: run the app
  in **Shizuku mode**. Run close to boot; per-boot success is probabilistic.
- Root helper build `30a1ef26...69d47ba` guards `--late-load` via a
  bind-mounted logcat path (DEFEX kills any ksud exec parented by `sh`).
