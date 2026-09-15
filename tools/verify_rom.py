#!/usr/bin/env python3
"""Inspect a local Game Boy Advance ROM for direct decompilation research.

Retail ROM images stay outside the repository. This tool reads a user-supplied
local file and reports identity metadata derived directly from that file.
It does not rely on public decompilation repositories or third-party target data.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifests" / "versions.json"


def hash_file(path: Path, algorithm: str) -> str:
    digest = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def decode_ascii(raw: bytes) -> str:
    return raw.rstrip(b"\0").decode("ascii", errors="replace")


def read_gba_header(path: Path) -> dict[str, object]:
    with path.open("rb") as handle:
        header = handle.read(0xC0)
    if len(header) < 0xC0:
        raise ValueError("file is too small to contain a complete GBA header")
    return {
        "title": decode_ascii(header[0xA0:0xAC]),
        "game_code": decode_ascii(header[0xAC:0xB0]),
        "maker_code": decode_ascii(header[0xB0:0xB2]),
        "fixed_value": header[0xB2],
        "main_unit_code": header[0xB3],
        "device_type": header[0xB4],
        "revision": header[0xBC],
        "header_checksum": header[0xBD],
    }


def inspect_rom(path: Path) -> dict[str, object]:
    return {
        "size": path.stat().st_size,
        "header": read_gba_header(path),
        "hashes": {
            "sha1": hash_file(path, "sha1"),
            "sha256": hash_file(path, "sha256"),
        },
    }


def compare_target(actual: dict[str, object], target: dict[str, object]) -> dict[str, bool]:
    checks: dict[str, bool] = {}
    if "rom_size" in target:
        checks["size"] = actual["size"] == target["rom_size"]

    expected_header = target.get("header", {})
    actual_header = actual["header"]
    for field, expected in expected_header.items():
        checks[f"header.{field}"] = actual_header.get(field) == expected

    expected_hashes = target.get("hashes", {})
    actual_hashes = actual["hashes"]
    for algorithm, expected in expected_hashes.items():
        checks[f"hashes.{algorithm}"] = actual_hashes.get(algorithm) == expected

    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a local GBA ROM directly")
    parser.add_argument("rom", type=Path, help="path to a local .gba image")
    parser.add_argument("--target", help="optional target id from manifests/versions.json")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()

    if not args.rom.is_file():
        parser.error(f"ROM not found: {args.rom}")

    try:
        actual = inspect_rom(args.rom)
    except ValueError as exc:
        parser.error(str(exc))

    result: dict[str, object] = {
        "rom": str(args.rom),
        **actual,
    }

    exit_code = 0
    if args.target:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        target = manifest.get("targets", {}).get(args.target)
        if target is None:
            parser.error(f"unknown target: {args.target}")
        checks = compare_target(actual, target)
        result["target"] = args.target
        result["checks"] = checks
        result["match"] = bool(checks) and all(checks.values())
        exit_code = 0 if result["match"] else 1

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return exit_code

    header = actual["header"]
    hashes = actual["hashes"]
    print(f"ROM:             {args.rom}")
    print(f"Size:            {actual['size']} bytes")
    print(f"Title:           {header['title']}")
    print(f"Game code:       {header['game_code']}")
    print(f"Maker code:      {header['maker_code']}")
    print(f"Revision:        {header['revision']}")
    print(f"Header checksum: 0x{header['header_checksum']:02X}")
    print(f"SHA-1:           {hashes['sha1']}")
    print(f"SHA-256:         {hashes['sha256']}")

    if args.target:
        print()
        for name, passed in result["checks"].items():
            print(f"[{'OK' if passed else 'FAIL'}] {name}")
        print("\nMATCH" if result["match"] else "\nMISMATCH")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
