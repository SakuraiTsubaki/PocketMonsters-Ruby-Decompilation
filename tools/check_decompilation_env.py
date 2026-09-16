#!/usr/bin/env python3
"""Check the local tool environment for PocketMonsters-Ruby-Decompilation."""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / ".local" / "decompilation"


def which_any(*names: str) -> str | None:
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


def first_line(cmd: list[str]) -> str:
    try:
        out = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=8,
            check=False,
        ).stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return ""
    return out.splitlines()[0] if out else ""


def check_arm_clang() -> bool:
    clang = shutil.which("clang")
    objdump = which_any("llvm-objdump", "arm-none-eabi-objdump")
    if not clang or not objdump:
        return False

    source = "int ruby_arm7tdmi_probe(int x) { return x + 1; }\n"
    try:
        with tempfile.TemporaryDirectory() as td:
            c_path = Path(td) / "probe.c"
            o_path = Path(td) / "probe.o"
            c_path.write_text(source, encoding="utf-8")
            result = subprocess.run(
                [
                    clang,
                    "--target=arm-none-eabi",
                    "-mcpu=arm7tdmi",
                    "-mthumb",
                    "-c",
                    str(c_path),
                    "-o",
                    str(o_path),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=15,
                check=False,
            )
            return result.returncode == 0 and o_path.is_file()
    except (OSError, subprocess.TimeoutExpired):
        return False


def main() -> int:
    local_bin = LOCAL / "bin"
    local_agbcc = LOCAL / "agbcc"
    os.environ["PATH"] = os.pathsep.join(
        [str(local_bin), str(local_agbcc), os.environ.get("PATH", "")]
    )

    rows: list[tuple[str, bool, str, bool]] = []
    core = [
        ("git", ("git",), True),
        ("make", ("make", "gmake"), True),
        ("python3", ("python3",), True),
        ("C compiler", ("cc", "gcc", "clang"), True),
        ("C++ compiler", ("c++", "g++", "clang++"), True),
        ("cmake", ("cmake",), False),
        ("ninja", ("ninja",), False),
        ("ARM assembler", ("arm-none-eabi-as",), False),
        ("ARM objdump", ("arm-none-eabi-objdump", "llvm-objdump"), True),
        ("ARM objcopy", ("arm-none-eabi-objcopy", "llvm-objcopy"), True),
        ("GDB client", ("arm-none-eabi-gdb", "gdb-multiarch", "gdb"), False),
        ("grit", ("grit",), False),
        ("mGBA", ("mgba-qt", "mgba"), True),
        ("Ghidra", ("ghidraRun", "ghidra"), False),
    ]

    for label, names, required in core:
        found = which_any(*names)
        detail = found or "missing"
        if found and label in {"git", "make", "python3", "cmake", "ninja", "mGBA"}:
            version = first_line([found, "--version"])
            if version:
                detail = f"{found} ({version})"
        rows.append((label, bool(found), detail, required))

    agbcc = local_agbcc / "agbcc"
    agbcc_ok = agbcc.is_file() and os.access(agbcc, os.X_OK)
    rows.append(
        (
            "pret/agbcc",
            agbcc_ok,
            str(agbcc) if agbcc_ok else "missing",
            True,
        )
    )

    arm_gnu = which_any("arm-none-eabi-gcc")
    clang_arm = check_arm_clang()
    arm_compile_ok = bool(arm_gnu) or clang_arm
    detail = arm_gnu or (
        "clang --target=arm-none-eabi -mcpu=arm7tdmi works"
        if clang_arm
        else "missing"
    )
    rows.append(("ARM7TDMI C compile", arm_compile_ok, detail, True))

    width = max(len(row[0]) for row in rows)
    print("PocketMonsters-Ruby-Decompilation tool check")
    print("=" * 56)
    failures = 0
    for label, ok, detail, required in rows:
        state = "OK" if ok else ("MISSING" if required else "OPTIONAL")
        print(f"{label:<{width}}  {state:<8}  {detail}")
        if required and not ok:
            failures += 1

    print("\nNotes:")
    print("- Retail ROMs remain outside Git; pass them with ROM=/path/to/file.gba.")
    print("- Exact compiler matching will use pret/agbcc where required.")
    print("- LLVM/Clang ARM7TDMI support is accepted for immediate analysis/prototyping, not as proof of an exact retail match.")
    print("- mGBA is the runtime/debug emulator; Ghidra is optional static-analysis tooling.")

    if failures:
        print(f"\n{failures} required tool component(s) still missing.")
        return 1

    print("\nRequired tool environment is ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
