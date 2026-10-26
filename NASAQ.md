# Nasaq Remote (نسق ريموت)

Nasaq Remote is a rebranded build of [RustDesk](https://github.com/rustdesk/rustdesk), licensed under AGPL-3.0 (see `LICENCE`).

Based on upstream commit `59f2953c94b8373f124dc38d4fd0635098f7c5cd` (hbb_common vendored from `edefa08b798b7fbf70b274a4cdbf701c9e06f7a3`).

Changes from upstream:
- App name `NasaqRemote`; Windows product name and macOS bundle name updated.
- Built-in ID/relay server `srv1121318.hstgr.cloud` and its public key.
- CI builds Windows and macOS only (`.github/workflows/nasaq-build.yml`, run manually).
