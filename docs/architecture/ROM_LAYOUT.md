# Ruby Rev 0 — Initial ROM and Memory Layout

**Target:** `ruby_en_rev0`  
**Current evidence level:** reference-derived mapping with independently verified ROM identity; direct local byte-by-byte confirmation remains part of the matching workflow.

This is the first architecture record for the active Ruby decompilation target. It intentionally records only structure supported by current evidence and leaves unresolved boundaries explicit.

## 1. GBA address-space anchors used by the build

The public Ruby/Sapphire reconstruction linker script places the principal regions at the standard GBA addresses below:

| Region | Start | Reserved span in linker model | Purpose in current mapping |
| --- | ---: | ---: | --- |
| EWRAM | `0x02000000` | `0x40000` bytes | External work RAM; no-load runtime data/symbol region |
| IWRAM | `0x03000000` | `0x8000` bytes | Internal work RAM; `.bss`, code-in-IWRAM, COMMON/runtime data |
| Game Pak ROM | `0x08000000` | target ROM is 16 MiB | Entry point, header, code, scripts, libraries, read-only data, assets/data |

The linker model further records `.bss` from `0x03000000`, an IWRAM code/BSS area beginning around `0x03000F60`, and COMMON data beginning around `0x03001760`. These addresses are treated as **reference anchors** until reproduced against the active local target.

## 2. ROM entry and GBA header

The reconstructed startup source labels `Start` at `0x08000000` and branches immediately to the initialization routine. The standard GBA header occupies the opening ROM area and includes:

- Nintendo logo block
- 12-byte game title field
- 4-byte game code
- maker code
- fixed value `0x96`
- unit/device fields
- software revision byte
- header checksum

For the active target the verified identity is:

| Field | Value |
| --- | --- |
| Game title | `POKEMON RUBY` |
| Game code | `AXVE` |
| Software revision | `0` |
| ROM size | `0x01000000` / 16 MiB |
| SHA-1 | `f28b6ffc97847e94a6c21a63cacf633ee5c8df1e` |

The committed `tools/verify_rom.py` checks these header fields and SHA-1 against `manifests/versions.json`.

## 3. Header-adjacent hardware/data area

The startup reconstruction places Game Pak GPIO registers immediately after the normal GBA header area:

- `0x080000C4` — GPIO data
- `0x080000C6` — GPIO direction
- `0x080000C8` — GPIO read-enable

The public source also marks data beginning around `0x080000D0` as not fully understood. Region/language-dependent startup data must therefore be investigated separately rather than generalized from one build.

## 4. Initial ROM link order

The current reference linker model begins ROM placement at `0x08000000` and orders major content classes approximately as follows:

1. startup / `crt0`
2. main game `.text` objects
3. `script_data` — event scripts, battle animation scripts, battle scripts, field-effect scripts, battle AI, contest AI, Mystery Event command tables
4. library text — multiboot, m4a/audio, flash-memory libraries, RTC, BIOS/syscall wrappers, libgcc/libc support
5. `.rodata` — code-associated constants plus large portions of structured game data
6. additional data/resource sections later in the linker script, to be mapped precisely in subsequent passes

This ordering is important: source reconstruction must preserve object/section ordering when byte matching depends on placement, padding, alignment, or compiler behavior.

## 5. Early subsystem ordering visible in `.text`

The beginning of the reference `.text` order establishes several major engine families very early in ROM, including:

- startup and main loop
- sprites and text/string handling
- link/communication and RTC
- menus
- battle controllers, battle core, battle utilities, battle scripts, AI
- Pokémon data/logic and damage calculation
- save/load and trading
- overworld, field map, player/avatar, object movement, scripting and event data
- weather, tasks, UI, Pokédex/storage/summary systems
- contests, secret bases, TV, record mixing and Pokéblocks
- field effects and battle animations
- region map, decorations, minigames, Mystery Event, Battle Tower and end-game systems

This is an **ordering map**, not yet a completed symbol/address map. Individual addresses, sizes, compiler provenance, and revision differences will be recorded as they are verified.

## 6. Known reconstruction cautions

The reference linker source itself contains unresolved or historically reconstructed details, including explicit padding/gaps, unusual object ordering, and comments questioning why specific read-only data appears at certain positions. Therefore:

- reference object order is not automatically treated as original developer project structure;
- unexplained gaps must be preserved and investigated rather than silently normalized;
- region/revision-specific linker differences must not be merged into Rev 0 without evidence;
- modernized compiler output must be kept distinct from byte-matching compiler output;
- imported symbol names are references, not proof of original internal names.

## 7. Immediate next mapping work

- [ ] Produce a machine-readable top-level ROM section map.
- [ ] Record exact boundaries for `.text`, `script_data`, library code, `.rodata`, and subsequent sections.
- [ ] Build the first address/symbol inventory for startup and main-loop code.
- [ ] Record compiler/toolchain requirements and matching constraints.
- [ ] Compare Rev 1 and Rev 2 layout changes without contaminating the Rev 0 baseline.
- [ ] Expand version coverage to Japanese and other official language/region builds.

## References

- `pret/pokeruby` linker model: <https://github.com/pret/pokeruby/blob/master/ld_script.txt>
- `pret/pokeruby` startup reconstruction: <https://github.com/pret/pokeruby/blob/master/src/crt0.s>
- `pret/pokeruby` build configuration: <https://github.com/pret/pokeruby/blob/master/config.mk>
- Rev 0 cartridge/header record: <https://gbhwdb.gekkio.fi/cartridges/AGB-AXVE-0/fexcollects-1.html>

These references are used as research inputs. The repository's own matching claims remain governed by `docs/VERIFICATION.md` and the active target manifest.
