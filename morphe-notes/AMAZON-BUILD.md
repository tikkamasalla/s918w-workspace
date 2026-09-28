# Amazon 32.17.0.100 Morphe build — 2026-09-19

Toolchain:
- morphe-desktop 1.16.0 (`morphe-desktop-1.16.0-all.jar`, 44,512,111 B)
- patches-1.22.0.mpp (SHA-256 1d392eca…a70a06), rushiranpise/morphe-patches
- Temurin JRE 21.0.12.1 (`E:\morphe\jre21`)
- Input: `amazon-32.17.0.100.xapk` (174,941,673 B, APKPure, arm64, code 1243230206,
  manifest-verified package + version)

Command (workdir E:\morphe):
java -jar morphe-desktop-1.16.0-all.jar patch -p patches-1.22.0.mpp \
  -e "Dark mode" -e "Disable search suggestions tracking" \
  -e "Disable video autoplay" -e "Fix Amazon manifest conflicts" \
  -e "Hide Rufus tab" -e "Open links in browser" \
  -e "Price history charts" -e "Remove ads" \
  -o amazon-32.17.0.100-patched.apk amazon-32.17.0.100.xapk

Output: `amazon-32.17.0.100-patched.apk` (120.7 MB, 5553 entries, CRC-clean).
All 8 patches reported Applied.

Install notes (when phone is back):
- Patched signature != Play signature: uninstall stock Amazon first if present
  (adb uninstall com.amazon.mShop.android.shopping — loses its app data).
- Then: adb install amazon-32.17.0.100-patched.apk
- Open, verify: dark mode / no autoplay / no Rufus tab / no ads.
