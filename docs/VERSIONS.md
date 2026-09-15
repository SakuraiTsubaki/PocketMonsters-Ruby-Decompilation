# Version Coverage

This inventory is derived directly from the 13 project-supplied Pokemon Ruby ROM images inspected on 2026-09-16. ROM binaries remain outside Git.

## Verified target inventory

| Target | Region | Language | Rev | Code | Size | SHA-1 |
| --- | --- | --- | ---: | --- | ---: | --- |
| `jp-r0` | Japan | Japanese | 0 | `AXVJ` | 8 MiB | `5c5e546720300b99ae45d2aa35c646c8b8ff5c56` |
| `en-us-r0` | USA | English | 0 | `AXVE` | 16 MiB | `f28b6ffc97847e94a6c21a63cacf633ee5c8df1e` |
| `en-eu-r1` | Europe | English | 1 | `AXVE` | 16 MiB | `610b96a9c9a7d03d2bafb655e7560ccff1a6d894` |
| `en-us-eu-r2` | USA/Europe | English | 2 | `AXVE` | 16 MiB | `5b64eacf892920518db4ec664e62a086dd5f5bc8` |
| `fr-r0` / `fr-r1` | France | French | 0 / 1 | `AXVF` | 16 MiB | see manifest |
| `de-r0` / `de-r1` | Germany | German | 0 / 1 | `AXVD` | 16 MiB | see manifest |
| `de-debug-r0` | Germany | German debug | 0 | `AXVD` | 16 MiB | `ca5e3d415c4b47353a73a616878ba833f3648b7a` |
| `it-r0` / `it-r1` | Italy | Italian | 0 / 1 | `AXVI` | 16 MiB | see manifest |
| `es-r0` / `es-r1` | Spain | Spanish | 0 / 1 | `AXVS` | 16 MiB | see manifest |

## Direct observations

- All 13 GBA header checksums validate.
- Japanese and English builds branch from the ROM header to `0x080000D0`; French/German/Italian/Spanish builds branch to `0x08000204`.
- French, German retail, Italian and Spanish Rev 0 -> Rev 1 differ in exactly four bytes.
- English Europe Rev 1 -> USA/Europe Rev 2 also differs in exactly four bytes.
- Two bytes are the header revision/checksum. The other two alter the same Thumb calendar loop (`BLE/BGT` -> `BLT/BGE`).
- German debug shares `AXVD` revision 0 in its header but is a substantially different build.

Region labels come from the supplied filenames; code-level claims come from direct binary inspection. ROM binaries are never committed.
