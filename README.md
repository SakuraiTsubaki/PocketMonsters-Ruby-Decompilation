# Pocket Monsters Ruby — Decompilation

![Status](https://img.shields.io/badge/status-direct_analysis_started-blue)
![Project](https://img.shields.io/badge/project-decompilation-blue)
![ROMs](https://img.shields.io/badge/ROM_binaries-not_included-success)

Decompilation and source-reconstruction project for **Pokémon Ruby**.

## 🎯 Goals

- Reconstruct game code and data into readable, editable source form.
- Document executable structures, data formats, scripts, assets, and version differences.
- Keep analysis, tooling, metadata, and documentation reproducible.
- Build a clean foundation for long-term reverse-engineering work.

## 🚧 Status

**Decompilation has started.** The current phase is direct source acquisition and identity mapping. No ROM revision, region, language build, hash, symbol map, or binary layout is treated as authoritative until it has been derived from project-supplied source material and recorded with reproducible evidence.

Public decompilation repositories and third-party reconstruction projects are not used as authoritative inputs for this project.

## 🛠️ Toolchain and emulator

This is a GBA / ARM7TDMI project. Prepare the project-local environment with:

```sh
make setup-tools
make check-tools
```

The setup covers the host build tools, GBA/ARM tooling, pinned `pret/agbcc`, and mGBA. Third-party generated binaries stay under the ignored `.local/` directory. See [Toolchain and emulator](docs/TOOLCHAIN.md) for details.

## 🔎 Direct ROM inspection

Retail ROM images remain outside the repository. Inspect a local source image with:

```sh
make inspect-rom ROM=/path/to/local/PokemonRuby.gba
```

This reports GBA header identity, file size, SHA-1, and SHA-256 directly from the supplied file. Once a target has been verified and registered in `manifests/versions.json`, it can be checked with `make verify-rom`.

Run or debug a local ROM with mGBA using:

```sh
make run-rom ROM=/path/to/local/PokemonRuby.gba
make debug-rom ROM=/path/to/local/PokemonRuby.gba
```

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

- [ ] Directly inspect and identify the first source ROM
- [ ] Lock the first verified reconstruction target
- [x] Add direct ROM identity inspection tooling
- [ ] Map executable and data structures from the verified target
- [ ] Begin matched source reconstruction
- [ ] Document assets, scripts, and formats
- [ ] Expand verified regional/language/revision coverage
- [ ] Add complete build and binary-comparison workflow

## 📚 Documentation

| Document | Purpose |
| --- | --- |
| [Project status](docs/PROJECT_STATUS.md) | Current stage, coverage, validation level, and next milestones |
| [Roadmap](docs/ROADMAP.md) | Recommended decompilation phases and long-term progression |
| [Version coverage](docs/VERSIONS.md) | Directly verified regions, languages, revisions, builds, and hashes |
| [Toolchain and emulator](docs/TOOLCHAIN.md) | GBA/ARM tools, agbcc, mGBA, setup, and environment verification |
| [Research guide](docs/RESEARCH_GUIDE.md) | Evidence, confidence, and research-recording workflow |
| [Verification guide](docs/VERIFICATION.md) | Standards for Observed, Reproduced, and Matched results |
| [Repository structure](docs/REPOSITORY_STRUCTURE.md) | Intended long-term source, data, asset, tooling, and manifest layout |
| [Documentation hub](docs/README.md) | Entry point for format, executable, script, asset, version, and verification notes |

## 🧱 Repository growth

Real project directories are added when they contain verified material. The project will grow into `src/`, `include/`, `data/`, `assets/`, `tools/`, `tests/`, and related areas as reconstruction progresses; empty decorative trees are avoided.

## 🔬 Research and verification

Research findings identify the exact directly inspected source and clearly separate hypotheses from observed, reproduced, or matched results. Unknown values remain unknown until verified.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules, evidence expectations, commit guidance, and pull-request requirements.
