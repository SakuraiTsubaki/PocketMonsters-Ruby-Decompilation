# Toolchain and Emulator

This repository is a **Game Boy Advance / ARM7TDMI** Pokémon Ruby decompilation project. Tooling is selected for source reconstruction, binary inspection, exact-match work, and runtime debugging rather than copied from a different console generation.

## Required tool layers

### Host build tools

- Git
- GNU Make
- Python 3
- GCC/G++ or Clang/Clang++
- CMake and Ninja for auxiliary tooling when needed
- libpng development files for graphics utilities

### GBA / ARM tools

Preferred GBA environment: **devkitPro `gba-dev` / devkitARM**. A system `arm-none-eabi` toolchain can also provide assembler, linker, objdump, objcopy, nm, and related binary utilities.

For immediate analysis, LLVM/Clang is also accepted when it can compile with:

```sh
clang --target=arm-none-eabi -mcpu=arm7tdmi -mthumb
```

LLVM output is useful for analysis and prototypes, but it is **not** evidence of a byte-exact retail match.

### Exact compiler matching

Pokémon GBA decompilation projects use **pret/agbcc** for matching historical compiler output. This repository pins the setup script to:

```text
pret/agbcc da598c1d918402c42c0c0d7128ba14567f3175e9
```

The checkout/build is kept under `.local/decompilation/agbcc`, which is ignored by Git. Third-party generated compiler binaries are not committed as project source.

### Emulator / debugger

**mGBA 0.10.5** is the default emulator. It supports GBA execution, a command-line debugger, and GDB remote debugging. The local setup script first uses a package-manager installation and then falls back to the official x86_64 AppImage when possible.

Useful commands:

```sh
make run-rom ROM=/path/to/local/PokemonRuby.gba
make debug-rom ROM=/path/to/local/PokemonRuby.gba
```

Retail ROMs stay outside the repository.

### Optional static analysis

**Ghidra** is useful for larger-scale ARM/Thumb control-flow and cross-reference analysis. It is optional because the project must remain reproducible without committing a Ghidra installation or project database. As of 2026-09-16, the current Ghidra 12.1.x release line requires JDK 25.

## Setup

Run:

```sh
make setup-tools
```

The installer uses the host package manager where supported, builds the pinned agbcc checkout, installs or downloads mGBA when possible, and writes:

```text
.local/decompilation/env.sh
```

To add locally installed tools to the current shell:

```sh
. .local/decompilation/env.sh
```

Then verify everything with:

```sh
make check-tools
```

For inspection only, without trying to install anything:

```sh
bash tools/setup_decompilation_env.sh --check-only
```

## Network-restricted environments

If package mirrors or GitHub downloads are unavailable, setup does not pretend success. Existing host tools remain usable, and `make check-tools` reports exactly which components are missing. Re-run `make setup-tools` when network access is available.

## Source references

- devkitPro / GBA environment: https://devkitpro.org/
- pret agbcc: https://github.com/pret/agbcc
- mGBA: https://mgba.io/ and https://github.com/mgba-emu/mgba
- Ghidra: https://github.com/NationalSecurityAgency/ghidra
