# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

## Baseline policy

This project uses the original Japanese release as the historical baseline and traces every confirmed regional, language, and revision branch from that point. A later regional build is not treated as interchangeable with the Japanese build merely because game content appears similar.

The project does not currently assume access to any retail ROM image. Version identities are established from public documentation, hardware/cartridge databases, public reverse-engineering repositories, hashes, and other reproducible evidence. Unknown fields remain explicit rather than being inferred.

## Japanese baseline

| Status | Region | Language | Revision / update | Platform / build | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Verified | Japan | Japanese | Rev 0 / v1.0 | GBA / AGB-AXVJ-0 / retail code AGB-AXVJ-JPN | SHA-1 `5c5e546720300b99ae45d2aa35c646c8b8ff5c56` | Historical baseline. Official Japanese release date: 2002-11-21. |
| Verified | Japan | Japanese | Rev 1 / v1.1 | GBA / AGB-AXVJ-1 | SHA-1 `971e0d670a95e5b32240b2deed20405b8daddf47` | Confirmed Japanese revision. Exact binary delta remains a separate verification task. |

See [`versions/JAPANESE_BASELINE.md`](versions/JAPANESE_BASELINE.md) for evidence, provenance, and current open questions.

## Confirmed regional/revision branches — first-pass inventory

The rows below record confirmed product-code/revision branches. `TBD` hashes are intentionally left unresolved until a sufficiently strong source-to-build mapping is recorded.

| Status | Region / market | Language | Revision / update | Platform / build | Hashes | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Verified | North America | English | Rev 0 | GBA / AGB-AXVE-0 / retail code AGB-AXVE-USA | SHA-1 `f28b6ffc97847e94a6c21a63cacf633ee5c8df1e` | Public `pret/pokeruby` default matching target. |
| Verified | North America branch | English | Rev 1 | GBA / AGB-AXVE-1 | TBD | Variant existence confirmed; exact hash/product mapping to be cross-verified. |
| Verified | North America branch | English | Rev 2 | GBA / AGB-AXVE-2 | TBD | Variant existence confirmed; exact hash/product mapping to be cross-verified. |
| Verified | Europe / Australia English distribution | English | Rev 0 | GBA / AGB-AXVP-0 / retail codes include AGB-AXVP-EUR and AGB-AXVP-AUS | TBD | Europe and Australia use the `AXVP` product-code branch; packaging market and binary identity must be tracked separately. |
| Verified | Europe / Australia English distribution | English | Rev 1 | GBA / AGB-AXVP-1 | TBD | Exact region/hash mapping pending. |
| Verified | Europe / Australia English distribution | English | Rev 2 | GBA / AGB-AXVP-2 | TBD | Exact region/hash mapping pending. |
| Verified | Germany | German | Rev 0 | GBA / AGB-AXVD-0 | SHA-1 `1c2a53332382e14dab8815e3a6dd81ad89534050` | Public hash inventory; `pret/pokeruby` supports German builds. |
| Verified | Germany | German | Rev 1 | GBA / AGB-AXVD-1 | SHA-1 `424740be1fc67a5ddb954794443646e6aeee2c1b` | Public hash inventory. |
| Verified | France | French | Rev 0 | GBA / AGB-AXVF-0 | SHA-1 `a6ee94202bec0641c55d242757e84dc89336d4cb` | Public hash inventory. |
| Verified | France | French | Rev 1 | GBA / AGB-AXVF-1 | SHA-1 `ba888dfba231a231cbd60fe228e894b54fb1ed79` | Public hash inventory. |
| Verified | Italy | Italian | Rev 0 | GBA / AGB-AXVI-0 | SHA-1 `2b3134224392f58da00f802faa1bf4b5cf6270be` | Public hash inventory. |
| Verified | Italy | Italian | Rev 1 | GBA / AGB-AXVI-1 | SHA-1 `015a5d380afe316a2a6fcc561798ebff9dfb3009` | Public hash inventory. |
| Verified | Spain | Spanish | Rev 0 | GBA / AGB-AXVS-0 | SHA-1 `1f49f7289253dcbfecbc4c5ba3e67aa0652ec83c` | Public hash inventory. |
| Verified | Spain | Spanish | Rev 1 | GBA / AGB-AXVS-1 | SHA-1 `9ac73481d7f5d150a018309bba91d185ce99fb7c` | Public hash inventory. |

## Public reconstruction coverage

`pret/pokeruby` is a major public source/disassembly reference, but its current build configuration is not a complete all-region baseline for this project. Its configuration exposes Ruby/Sapphire, revisions 0-2, and English/German language targets. Japanese, French, Italian, and Spanish reconstruction therefore remain separate research/reconstruction work for this repository unless additional verified public sources are identified.

## Status vocabulary

- **Planned** — intended for investigation but not yet verified.
- **Verified** — identity and hashes or stable build identifiers confirmed from recorded public evidence.
- **Mapped** — executable/data layout documented.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — used for comparison but not a reconstruction target.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes over filenames as identity evidence.
3. Do not commit retail game images or console keys.
4. Record regional or language differences instead of assuming two releases are identical.
5. Link version-specific findings to the relevant documentation or verification issue.
6. Treat the Japanese release as the comparison baseline while preserving later fixes, additions, removals, and region-exclusive behavior as separate branch history.
7. Keep market/packaging identity separate from binary identity when the same language is sold under different regional product codes.
8. Use `TBD` or `unknown` when a hash, revision mapping, or branch relationship has not yet been verified.
