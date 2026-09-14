# Japanese Baseline — Pokémon Ruby

This document records the current evidence for the Japanese release that serves as the historical baseline for the Ruby decompilation project.

## Baseline rule

The Japanese release is the comparison origin for regional research. This does **not** mean later regional releases are treated as inferior or overwritten by Japanese data. Fixes, additions, removals, localization changes, and region-exclusive behavior are preserved as separate branch history.

No retail ROM image is required or committed by this repository. Identity and reconstruction work starts from public evidence, public reverse-engineering material, hashes, hardware metadata, and reproducible analysis.

## Confirmed identity

| Field | Rev 0 / v1.0 | Rev 1 / v1.1 |
| --- | --- | --- |
| Title | ポケットモンスター ルビー | ポケットモンスター ルビー |
| Platform | Game Boy Advance | Game Boy Advance |
| Market | Japan | Japan |
| Language | Japanese | Japanese |
| Product/build identifier | AGB-AXVJ-0 | AGB-AXVJ-1 |
| Retail product code | AGB-AXVJ-JPN | product-code revision suffix under investigation |
| SHA-1 | `5c5e546720300b99ae45d2aa35c646c8b8ff5c56` | `971e0d670a95e5b32240b2deed20405b8daddf47` |
| Repository role | Primary historical baseline | Japanese revision branch |

## Official release context

The Pokémon Company official Japanese product page records Ruby and Sapphire as Game Boy Advance titles released in Japan on **2002-11-21**. It identifies The Pokémon Company as publisher, Nintendo as distributor, and Game Freak as developer.

Official source:

- https://www.pokemon.co.jp/game/gba/rs/

## Physical-cartridge / revision evidence

The Game Boy hardware database records a physical Japanese Ruby cartridge entry as `AGB-AXVJ-JPN` and exposes separate No-Intro-linked variant identities for:

- `AGB-AXVJ-0` — Pocket Monsters - Ruby (Japan)
- `AGB-AXVJ-1` — Pocket Monsters - Ruby (Japan) (Rev 1)

It also records board/component evidence for a Rev 0 Japanese cartridge, including an `AGB-E05-01` board and RTC hardware.

Source:

- https://gbhwdb.gekkio.fi/cartridges/AGB-AXVJ-0/

## Hash evidence

The current SHA-1 values are recorded from multiple public ROM-identification/reverse-engineering references rather than from a locally owned ROM:

- Rev 0: `5c5e546720300b99ae45d2aa35c646c8b8ff5c56`
- Rev 1: `971e0d670a95e5b32240b2deed20405b8daddf47`

Public references used in this first pass:

- https://github.com/40Cakes/pokebot-gen3/blob/main/modules/roms.py
- https://www.screenscraper.fr/romsinfos.php?alpha=P&numpage=6&plateforme=12
- https://archives.glitchcity.info/forums/board-109/thread-7192/

The hash values are suitable for identity tracking, but this repository does not redistribute the corresponding retail ROM images.

## Revision-difference research status

Community reverse-engineering research reports that Japanese v1.1 changes the header revision and fixes the Berry/RTC date-conversion bug, with only a very small byte-level delta reported between verified v1.0 and v1.1 dumps.

This claim is currently retained as **research evidence**, not yet as a repository-level `Matched` result. The next verification step is to reproduce the Rev 0 ↔ Rev 1 delta from public source-level evidence or other legally available byte-difference documentation and record the exact function/offset relationship.

Research reference:

- https://archives.glitchcity.info/forums/board-109/thread-7192/

## Public reconstruction coverage gap

`pret/pokeruby` is a major public Ruby/Sapphire source/disassembly reference and its README states that it builds Ruby and Sapphire. However, its current `config.mk` exposes only `ENGLISH` and `GERMAN` language build targets, with revisions 0, 1, and 2.

Therefore the public upstream cannot be treated as a complete Japanese baseline reconstruction for this project. Japanese source reconstruction must be investigated independently and compared against the public English/German source where structure is shared.

Sources:

- https://github.com/pret/pokeruby
- https://github.com/pret/pokeruby/blob/master/config.mk

## Evidence classification

| Finding | Level | Reason |
| --- | --- | --- |
| Japanese release date 2002-11-21 | Observed | Recorded by the official Japanese Pokémon site |
| `AGB-AXVJ-0` and `AGB-AXVJ-1` variant existence | Observed | Public hardware/No-Intro-linked cartridge database |
| Rev 0 and Rev 1 SHA-1 values | Observed / cross-referenced | Same values appear in multiple independent public identification sources |
| Exact Rev 0 ↔ Rev 1 byte delta | Hypothesis / external research evidence | Reported publicly but not yet reproduced inside this repository |
| Japanese matching decompilation | Not yet reproduced | Current `pret/pokeruby` configuration does not provide a Japanese target |

## Next tasks

1. Cross-check Japanese Rev 0 and Rev 1 CRC32/MD5/SHA-1 identities against additional catalogued sources.
2. Reconstruct a documented Rev 0 ↔ Rev 1 change list, beginning with the Berry/RTC fix.
3. Inventory all public Japanese Ruby source, symbol, map, script, text, graphics, audio, save, event, and communication research.
4. Compare each subsystem against the public `pret/pokeruby` English/German reconstruction without assuming byte identity.
5. Extend the same Japanese-baseline method to Sapphire after the Ruby baseline inventory is stable.
