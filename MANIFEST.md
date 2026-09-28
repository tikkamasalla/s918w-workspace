# Workspace backup (2026-09-28)

Snapshots of the SM-S918W temp-root / port / Morphe work sessions.
Deliverables themselves live in their own repos/PRs; this is the lab
notebook: scripts, recovery toolchain, build logs, evidence.

## Contents

- `port-tools/` — one-off investigation scripts (adb helpers, APK
  analysis, DB dumps, LSPosed decompile, feed tools).
- `port-pytools/` — Python toolchain: `vmlinux_to_elf` (BTF/symbol
  recovery), `samloader`, `bin/`, plus vendored-dep manifest below.
  Third-party packages themselves are EXCLUDED (pip-reinstallable;
  several trip push-protection): `pip install pycryptodome requests
  zstandard lz4 tqdm pyelftools peewee certifi charset-normalizer idna
  urllib3 colorama samloader vmlinux-to-elf`.
- `port-src/` — `vmlinux_to_elf` source + kernel DB.
- `port-bin/` — small binaries (samloader etc.).
- `port-profile/` — dm3q-S918WVLS6CYB3 port profile inputs.
- `port-docs/` — port writeup, feed entries, patch notes.
- `port-evidence/` — logcat/verbose/module logs, screenshots, package lists.
- `morphe-notes/` — Morphe build logs + results (Amazon/Maps/Photos),
  `patches-list.json` patch catalogue.

## Deliberately excluded (regenerable / re-downloadable)

- `wsl-ubuntu-backup.tar` (12.6 GB) — live WSL moved to `E:\wsl`, no
  longer needed as a blob.
- `ndk/` + `ndk-r28c.zip` — stock Android NDK r28c (+ r30 in SDK).
- `oss/SM-S918B_16_Opensource.zip` — Samsung opensource drop (portal,
  captcha; `E:\s918w-port\oss` notes carry the portal id).
- `firmware/`, `kernel/` trees — extracted from the above.
- `*.apk` / `*.apks` build inputs/outputs — rebuilt from stock APKs +
  the patch repos (`morphe-patches`, `D-moniakPatches` forks).
- `morphe/jre21`, `morphe/morphe-data` — tool runtime + caches.
- KernelSU KO/ksud pair, payload `.so` — committed in the payload PRs
  (`BuSung-dev#352`, `HyperRamzey#2`).

## Where the real work lives

- Ports/payloads: Root-My-Galaxy-Payloads PRs above.
- App: Root-My-Galaxy (`custom-feed-tikkamasalla`).
- Modules: ReminderOngoing, PowerSaveSpoof.
- Morphe patches: morphe-patches (amzn sort, speedo), D-moniakPatches.
