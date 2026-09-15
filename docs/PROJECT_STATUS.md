# Project Status

**Current stage:** Phase 1 binary mapping + initial source reconstruction

Thirteen project-supplied Ruby targets are now directly verified. `jp-r0` is the canonical reconstruction target; every other supplied build remains an explicit comparison/matching target.

## Progress

- [x] Directly inspect every supplied Ruby ROM
- [x] Record GBA header identities and local hashes
- [x] Define the primary reconstruction target (`jp-r0`)
- [x] Register all 13 verified targets in `manifests/versions.json`
- [x] Generate first-pass executable signatures
- [x] Compare same-game-code revision families
- [x] Identify and decompile the first revision-sensitive routine (calendar day-count boundary logic)
- [ ] Persist full 64 KiB block-hash maps and classify common/delta regions
- [ ] Finish reset/IRQ/main-loop call graph
- [ ] Promote stable function boundaries to matched source units
- [ ] Map scripts/events, maps, graphics, audio, text, save, link/peripheral subsystems
- [ ] Build per-target compile and binary-match workflow

## First reconstruction result

A calendar routine contains the first confirmed source-level revision change. Older supplied builds use `yearIndex > 0`; corrected revisions use `yearIndex >= 0`. The routine also walks the directly observed month-length table `31,28,31,30,31,30,31,31,30,31,30,31`. The exact mapping of year index 0 to civil year 2000 is still treated as a hypothesis until its RTC caller chain is traced.

See `docs/FIRST_DECOMPILATION.md` and `manifests/revision_diffs.json`.
