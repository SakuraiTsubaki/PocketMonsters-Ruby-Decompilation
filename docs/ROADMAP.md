# Roadmap

This roadmap defines the recommended order for turning this repository from an initial research scaffold into a reproducible decompilation project.

## Phase 0 — Public-source census and target definition

Phase 0 begins from publicly accessible evidence because this project does not assume possession of a retail ROM image. The Japanese release is the historical baseline; every official regional, language, revision, distribution, peripheral, and linked-system variant must be traced without assuming equivalence.

- [ ] Maintain `SOURCE_INVENTORY.md` as the authoritative public-source coverage ledger.
- [ ] Search every defined source family, including official, archival, preservation, source-reconstruction, event, e-Reader, technical, physical-cartridge, forum/research, unused/debug, and community-reference material.
- [ ] Record search gaps and negative results; do not treat “not found” as “does not exist.”
- [ ] Identify mirrors, forks and derivatives so duplicated evidence is not counted as independent confirmation.
- [ ] Identify authoritative game versions, regions, languages, revisions, and updates.
- [ ] Use the original Japanese release as the primary historical comparison baseline and separately track later Japanese revisions.
- [ ] Trace every confirmed international target from the Japanese baseline and record additions, removals, fixes and localization-specific changes.
- [ ] Record hashes, product/build identifiers and provenance for each supported target when publicly verifiable.
- [ ] Define reconstruction/matching targets separately from reference-only targets.
- [ ] Preserve unresolved, conflicting and unverified claims explicitly.

**Phase 0 must not be marked complete merely because representative sources or the major pret repositories have been reviewed.** Completion requires the documented source-family coverage matrix and target-version matrix to have been systematically processed.

## Phase 1 — Binary and container mapping

- [ ] Document executable layout, sections, overlays, archives, and resource containers using publicly verifiable evidence and reconstructed source.
- [ ] Build file manifests and extraction/reconstruction notes.
- [ ] Record known compression, packing, and serialization formats.
- [ ] Separate findings by exact region/language/revision whenever layouts differ.

## Phase 2 — Symbol and subsystem mapping

- [ ] Name functions, symbols, tables, and major data structures.
- [ ] Identify engine subsystems and dependencies.
- [ ] Track confidence and evidence for each finding.
- [ ] Compare Japanese baseline behavior/data against each regional branch.

## Phase 3 — Source reconstruction

- [ ] Reconstruct code into readable, maintainable source.
- [ ] Reconstruct scripts, data tables, and asset metadata.
- [ ] Add extraction/repacking/reconstruction tools where needed.
- [ ] Keep version-specific source/data separated until byte identity or structural identity is demonstrated.

## Phase 4 — Verification

- [ ] Add repeatable tests and comparison workflows.
- [ ] Track matching or behavioral-equivalence status by subsystem and exact target.
- [ ] Document remaining mismatches and unknowns.
- [ ] Cross-check reconstructed findings against independent public evidence where possible.

## Phase 5 — Reproducible project workflow

- [ ] Provide documented setup and build/repack steps for legally supplied user inputs where required.
- [ ] Add CI or automated verification where practical.
- [ ] Keep generated outputs reproducible from repository sources and tooling.
- [ ] Keep the public-source inventory and provenance manifests current as new material is discovered.

Update this roadmap as the project scope becomes more concrete.