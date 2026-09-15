# Pocket Monsters Ruby — Decompilation

![Status](https://img.shields.io/badge/status-baseline_locked-brightgreen)
![Project](https://img.shields.io/badge/project-decompilation-blue)
![ROMs](https://img.shields.io/badge/ROM_binaries-not_included-success)

Decompilation and source-reconstruction project for **Pokémon Ruby**.

## 🎯 Goals

- Reconstruct game code and data into readable, editable source form.
- Document executable structures, data formats, scripts, assets, and version differences.
- Keep analysis, tooling, metadata, and documentation reproducible.
- Build a clean foundation for long-term reverse-engineering work.

## 🚧 Status

**Decompilation has started.** The first active byte-matching baseline is the English Revision 0 build (`AXVE`, revision byte `0`, SHA-1 `f28b6ffc97847e94a6c21a63cacf633ee5c8df1e`). Rev 1 and Rev 2 are recorded as secondary revision targets.

The repository now includes machine-readable target metadata and a local ROM verifier. The next phase is top-level ROM/binary mapping followed by matched source reconstruction.

## ✅ Bootstrap verification

Retail ROM images remain outside the repository. Verify a local image with:

```sh
make verify-rom ROM=/path/to/local/PokemonRuby.gba
```

The default target is `ruby_en_rev0`. Other registered targets can be selected with `TARGET=...`.

## 🗂️ Scope

- Code and executable analysis
- Game data structures
- Scripts and event data
- Graphics and asset metadata
- Audio and resource formats
- Maps and world data
- Tools, notes, manifests, and verification data
- Region, language, and revision differences

## 📌 Repository policy

ROM images and redistributed ROM binaries are **not included**. The repository is intended for reconstructed source, extracted/recreated project data, tooling, analysis, and documentation.

## 🧭 Roadmap

- [x] Establish initial baseline version/revision inventory
- [x] Lock the first byte-matching target
- [x] Add ROM identity verification workflow
- [ ] Map executable and data structures
- [ ] Begin matched source reconstruction
- [ ] Document assets, scripts, and formats
- [ ] Expand verified regional/language/revision coverage
- [ ] Add complete build and binary-comparison workflow

## 📚 Documentation

| Document | Purpose |
| --- | --- |
| [Project status](docs/PROJECT_STATUS.md) | Current stage, coverage, validation level, and next milestones |
| [Roadmap](docs/ROADMAP.md) | Recommended decompilation phases and long-term progression |
| [Version coverage](docs/VERSIONS.md) | Regions, languages, revisions, builds, hashes, and active baseline |
| [Research guide](docs/RESEARCH_GUIDE.md) | Evidence, confidence, and research-recording workflow |
| [Verification guide](docs/VERIFICATION.md) | Standards for Observed, Reproduced, and Matched results |
| [Repository structure](docs/REPOSITORY_STRUCTURE.md) | Intended long-term source, data, asset, tooling, and manifest layout |
| [Documentation hub](docs/README.md) | Entry point for format, executable, script, asset, version, and verification notes |

## 🧱 Repository growth

Real project directories are added when they contain verified material. The project will grow into `src/`, `include/`, `data/`, `assets/`, `tools/`, `tests/`, and related areas as reconstruction progresses; empty decorative trees are avoided.

See [Repository Structure](docs/REPOSITORY_STRUCTURE.md) for the organization policy.

## 🔬 Research and verification

Research findings identify the target version/revision and clearly separate hypotheses from observed, reproduced, or matched results. The active target inventory is also available in `manifests/versions.json`.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules, evidence expectations, commit guidance, and pull-request requirements.
