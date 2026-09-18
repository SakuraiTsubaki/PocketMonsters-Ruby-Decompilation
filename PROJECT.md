# Target Profile: Pocket Monsters Ruby

## Known repository scope

- Repository: `SakuraiTsubaki/PocketMonsters-Ruby-Decompilation`
- Working target name: Pocket Monsters Ruby
- Platform family: Game Boy Advance
- Series generation: Generation III
- Exact release, region, revision, and build: **not yet selected**

The repository name is a working label, not proof of a particular binary. No address, symbol, format, or behavior should be treated as target fact until the exact build is identified.

## Language priority

Research, source selection, reconstruction, comparison, naming, and implementation decisions follow this language order:

1. **Japanese** — primary/origin reference.
2. **Korean** — second priority when an official Korean version exists.
3. **English** — fallback when no official Korean version exists.
4. **Other official languages** — evaluated after Japanese, Korean, and English.

This order is a project policy, not a claim that every title has an official release in every listed language. For titles without an official Korean release, use Japanese first and English second, then the remaining official languages.

## Identity checklist

Record all available items before substantive reconstruction:

- official title and product identifier;
- platform and execution environment;
- region, language, revision, update, and distribution form;
- hashes for user-supplied images, executables, modules, or manifests;
- executable/container layout and relevant segment identifiers;
- analysis, extraction, compiler, linker, and SDK tool versions;
- legal provenance and distribution constraints for every input;
- differences from related versions that affect addresses, formats, or behavior.

Store machine-readable identifiers in `config/target.json`. Keep the ROM binary outside Git and commit every storable non-ROM result.

## Initial research priorities

- Fingerprint the exact cartridge revision and document the header, memory map, and top-level ROM regions.
- Identify ARM and Thumb code boundaries, calling conventions, compiler fingerprints, and data/code references.
- Map pointer tables, compression, graphics, text, audio, scripts, and other target-specific resource formats.
- Build deterministic extraction and comparison tools around user-supplied, hash-verified inputs.
- Define byte, layout, or behavior-based verification for each reconstructed component.

## First milestone

The foundation milestone is complete when the exact target build is recorded, the initial file/executable map is reproducible, at least one research record has been promoted to an analysis with stated confidence, and all commands needed to repeat that result are documented.

## Non-ROM artifact preservation

Follow [ARTIFACT_POLICY.md](ARTIFACT_POLICY.md). Preserve all storable non-ROM research, source, scripts, tools, logs, manifests, tables, structured data, graphics, sprites, palettes, fonts, icons, tiles, converted data, patches, and verification material. Graphics work must include actual PNG output.
