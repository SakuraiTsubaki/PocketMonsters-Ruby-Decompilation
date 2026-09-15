# Version Coverage

This document is the authoritative inventory of game versions targeted by the Ruby decompilation project.

## Active reconstruction baseline

The first matching target is the English Revision 0 build of Pokémon Ruby. Source reconstruction starts against this byte-identifiable target before version-specific differences are expanded to other revisions, languages, and regions.

| Status | Region / distribution | Language | Revision | GBA identity | SHA-1 | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| **In progress** | USA / Europe English release family | English | Rev 0 | `POKEMON RUBY`, game code `AXVE`, revision byte `0` | `f28b6ffc97847e94a6c21a63cacf633ee5c8df1e` | **Primary matching target.** 16 MiB retail build. |
| Verified | English release family | English | Rev 1 | game code `AXVE`, revision byte `1` | `610b96a9c9a7d03d2bafb655e7560ccff1a6d894` | Secondary revision target; map differences only after Rev 0 baseline is established. |
| Verified | English release family | English | Rev 2 | game code `AXVE`, revision byte `2` | `5b64eacf892920518db4ec664e62a086dd5f5bc8` | Secondary revision target; map differences only after Rev 0 baseline is established. |

The Rev 0 SHA-1 and GBA header identity are independently corroborated by public cartridge-preservation data. The Rev 0/1/2 build targets and hashes are also present in the public `pret/pokeruby` reconstruction project.

## Evidence

- `pret/pokeruby` build configuration: <https://github.com/pret/pokeruby/blob/master/config.mk>
- `pret/pokeruby` Rev 0 hash: <https://github.com/pret/pokeruby/blob/master/ruby.sha1>
- `pret/pokeruby` Rev 1 hash: <https://github.com/pret/pokeruby/blob/master/ruby_rev1.sha1>
- `pret/pokeruby` Rev 2 hash: <https://github.com/pret/pokeruby/blob/master/ruby_rev2.sha1>
- Cartridge/header verification for Rev 0: <https://gbhwdb.gekkio.fi/cartridges/AGB-AXVE-0/fexcollects-1.html>

## Coverage policy

Rev 0 is only the **initial matching baseline**, not the final project scope. Generation III version research will continue to track Japanese, English, German, French, Italian, Spanish, and other officially released regional/language builds and their revisions where applicable. A build is not treated as identical merely because its title or nominal version matches another release.

## Status vocabulary

- **Planned** — intended for investigation but not yet verified.
- **Verified** — identity and hashes confirmed.
- **Mapped** — executable/data layout documented.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — used for comparison but not a reconstruction target.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes plus GBA header identifiers over filenames.
3. Do not commit retail game images.
4. Record regional and language differences instead of assuming releases are identical.
5. Separate the active byte-matching target from reference revisions.
6. Link version-specific findings to documentation, manifests, tests, or verification records.
