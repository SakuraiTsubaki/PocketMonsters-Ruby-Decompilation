# Project Status

**Current stage:** Direct analysis started / target not yet locked

The Ruby decompilation is active, but no target build is treated as authoritative until it is identified from project-supplied source material.

## Version inventory

| Target | Region | Language | Revision | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | Pending direct verification | Populate only from directly inspected project source material |

## Progress

- [ ] Directly inspect the first source ROM
- [ ] Record its GBA header identity and locally computed hashes
- [ ] Define the primary reconstruction target
- [x] Add direct ROM inspection tooling
- [ ] Register verified target metadata in `manifests/versions.json`
- [ ] Document ROM/executable section layout from the verified source
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers
- [ ] Begin matched C/source reconstruction
- [ ] Reconstruct scripts, events, and behavior
- [ ] Reconstruct asset pipelines and metadata
- [ ] Expand version inventory across official regions/languages/revisions
- [ ] Add full build and binary-comparison workflow

## Current inspection command

```sh
make inspect-rom ROM=/path/to/local/PokemonRuby.gba
```

The command derives file size, GBA header fields, SHA-1, and SHA-256 directly from the supplied local file. Retail ROM images remain local and are ignored by Git.

## Source policy

- Project-supplied ROMs, dumps, extracted data, and reproducible direct analysis are primary evidence.
- Public decompilation repositories and third-party reconstruction projects are not authoritative inputs.
- Unknown version, layout, symbol, offset, compiler, or structure information remains explicitly unverified until reproduced from project evidence.

## Validation levels

- **Unverified** — proposed or recorded but not independently checked against project source material.
- **Observed** — confirmed directly in a specific inspected target or extracted data.
- **Reproduced** — the observation can be recreated using documented project inputs and tooling.
- **Matched** — reconstructed output is verified against the intended target.

## Next milestones

1. Inspect the first project-supplied Ruby source ROM.
2. Register its exact identity without importing external target metadata.
3. Build the initial ROM/header/binary map from that source.
4. Start the first source-reconstruction unit from directly observed bytes and behavior.
