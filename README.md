# PocketMonsters-Ruby-Decompilation

Clean-baseline decompilation and reverse-engineering project for **Pocket Monsters Ruby**.

This repository restarts from a deliberately small, stable live tree. Earlier commits remain valuable historical reference, but old directory layouts, migration trees, structure-version namespaces, and unfinished working trees are not restored automatically.

## Project principles

- Identify exact targets, revisions, languages, regions, and source provenance before making version-specific claims.
- Separate confirmed observations from hypotheses and unknowns.
- Prefer editable source, reproducible tooling, manifests, hashes, and verification over opaque generated output.
- Store byte-identical assets once only after hash or byte-level confirmation; visual similarity is not enough.
- Keep reviewable derived assets such as PNG previews when they materially help inspection and provenance is preserved.
- Do not commit retail ROMs, rebuilt ROMs, decrypted full-game images, keys, or disguised complete game images.
- Keep one current live structure. Git history is the history layer; do not create live `vN`, `PRE-VN`, `MIGRATED`, or legacy-history trees.
- Import useful historical work only after it has been reviewed against the current standards.

## Documentation

- [Documentation hub](docs/README.md)
- [Project standards](docs/PROJECT_STANDARDS.md)
- [Repository structure](docs/REPOSITORY_STRUCTURE.md)
- [Research guide](docs/RESEARCH_GUIDE.md)
- [Verification guide](docs/VERIFICATION.md)
- [Version coverage](docs/VERSIONS.md)
- [Roadmap](docs/ROADMAP.md)
- [Project status](docs/PROJECT_STATUS.md)
- [Asset workflow](docs/ASSET_WORKFLOW.md)
- [Repository ecosystem](docs/ECOSYSTEM.md)
- [Manifest guide](manifests/README.md)

## Current status

**Baseline established.** Game-specific work should now be added only through the stable structure and verification rules documented here.
