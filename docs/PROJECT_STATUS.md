# Project Status

**Current stage:** Baseline locked / binary mapping bootstrap

The Ruby decompilation has moved beyond repository-only setup. The first byte-matching target is fixed and a reproducible local ROM identity check is now committed.

## Version inventory

| Target | Region / distribution | Language | Revision | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| `ruby_en_rev0` | USA / Europe English release family | English | Rev 0 | **In progress** | Primary matching target; SHA-1 `f28b6ffc97847e94a6c21a63cacf633ee5c8df1e` |
| `ruby_en_rev1` | English release family | English | Rev 1 | Verified reference | Secondary revision target |
| `ruby_en_rev2` | English release family | English | Rev 2 | Verified reference | Secondary revision target |

See `VERSIONS.md` and `../manifests/versions.json` for identity details and provenance.

## Progress

- [x] Establish initial authoritative English revision inventory
- [x] Define the primary byte-matching target
- [x] Add machine-readable target metadata
- [x] Add local GBA header and SHA-1 verification tooling
- [ ] Document ROM/executable section layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers
- [ ] Begin matched C/source reconstruction
- [ ] Reconstruct scripts, events, and behavior
- [ ] Reconstruct asset pipelines and metadata
- [ ] Expand version inventory across all official regions/languages/revisions
- [ ] Add full build and binary-comparison workflow

## Current verification command

```sh
make verify-rom ROM=/path/to/local/PokemonRuby.gba
```

The default target is `ruby_en_rev0`. Retail ROM images remain local and are ignored by Git.

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a specific target build or extracted data.
- **Reproduced** — the observation can be recreated with documented inputs and tooling.
- **Matched** — reconstructed output is verified against the intended target.

## Next milestones

1. Map the GBA ROM header and top-level binary layout for the active Rev 0 target.
2. Establish the linker/build model and toolchain requirements.
3. Inventory code/data boundaries and the first symbol map.
4. Select the first code subsystem for matched source reconstruction.
5. Expand verified version coverage without mixing regional or revision-specific data into the active baseline.
